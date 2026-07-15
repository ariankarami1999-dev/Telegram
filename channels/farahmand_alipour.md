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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 18:12:16</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDtoBUvfbJ39Au6Rk7tUBj9xJ1WgC6OgSfdQSiRnwNGDwSBoONWMcOe1ZlQAla89lDB6FNpY-f_wBhzo6Q6nLf4yJEWylk261ngT6lX5NylvC6mX68GF89KvhwgY1AgEotYB6uEa2pcW4AOr2qNNzn0nHgWZJLJ75L5gf7DdEyTzUtbm1hbs790jqOZIcNCTFxDmjd57fVqY7SYfspdOd0bo2wrnXlM_g9vxRRpkRgNIHoAa58OrtRmIua6lyHrqMvvL-s7eER0o6qemgITrgMwEJrIcr8HewfAhL4qlUOsN-eZ04KvgcjOSTZO5XVZ8QVw1Lj4fqOM31dNrlpuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwk0MF1CymWQNvBspQ8qRvgCbc9OMnrwCCLvSSTmnNZG7h63TSeiBWtiMjICz44yaJh8FcDCbzEZAQrmBV-uZwz5BLiYRSq8gMvbZtzFABq742ir3Fnz48EBeSeG-EPf6pVH32S5ObLKiOmWTCPNl1wuKN6B2T09g9Q7bfvv-G-lBTFyukyL9TxmjkYB6TwNTMVSXGFJcYhgHAysEy799dAyianAAZdGsNOyLQVXCKCuthOA4kdvPxzKbtTCbGn_MFVUHfjstJ8fsr3VUoNl5ywPXjJRTMk_QEj_zesVne1WPthz_tBI_0fIXMMiubnDq-1X9wrTkke9IXGEUrNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=k--9uDZbpeYbUKddSeaezlvR3-fAG7NsCKNr2pFrh1FqbJ5M0nBheP588nCz8p3uuUl77yPU6cNEWfQ3-vZsotuxhTSDYQPDmEw4NJN00RuVu3xIifz_X-Lc9kEdeO4ehkkw8isTFrtWROvteXYzCi0VUfyX9hNra0J1JLkn1lnx67pXfMTQX6-rlngUqZLNYWVaeNP6GQ44xMOKGRwCG2eAItslgpwKXF97TrHYa-VjeQoaywrXu4b-UJ9nOZWZvR4U1gfC211duZHji-q7lUcDhnYE1L-S9GIGglkI5qCzESjyQkT_0FkyyRg1xxRXRYDMLdnzcrYIK5hEovQJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=k--9uDZbpeYbUKddSeaezlvR3-fAG7NsCKNr2pFrh1FqbJ5M0nBheP588nCz8p3uuUl77yPU6cNEWfQ3-vZsotuxhTSDYQPDmEw4NJN00RuVu3xIifz_X-Lc9kEdeO4ehkkw8isTFrtWROvteXYzCi0VUfyX9hNra0J1JLkn1lnx67pXfMTQX6-rlngUqZLNYWVaeNP6GQ44xMOKGRwCG2eAItslgpwKXF97TrHYa-VjeQoaywrXu4b-UJ9nOZWZvR4U1gfC211duZHji-q7lUcDhnYE1L-S9GIGglkI5qCzESjyQkT_0FkyyRg1xxRXRYDMLdnzcrYIK5hEovQJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxIznt_LFKAV0-EcwG9bO6r8r90P5LdWuVtxz2_lED6myjGUz2mSGeae_dxe9AkIikMdPZ4cIB69BByP1JgPy6ySTekChqMUfHV0lEtHW9qEu-lVk41Vpph0AJhaSHmFCFOjX9JnTvyrDo68cew9FqDm5OhVBa25qUEbw8fQaTTXLF22bvz3I1gKhJwg6MFc0s1qsz6MhQm-L-ghm9oF2cpmwf9SRS4--RJC-vAYNYHYVCm0Di1pqow58X-0kMZA5QOkhYMzLPMYK6o7VaNF1L-SLuAE__XfG5qKrD65o79gQKuNe4MuTDbYGRlWv8C0d1KI2SyQXO3dSpOWzPf0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioAlXwoT1WjcSVkXHdC8oKgqvQxwI7L9M-XaqsyLeti0UKKxsC2U90KF-2U0dYwAt_gH6x9uf4gySU-d44vzxyonALETRk6reFC4u-Q5ozI9mk9-1uWkAhEj51sqxvGvAORSJvqJ7GF2HsCN8yjzr8Yq4NjxSAvnmlaKegNFvguvGic35-yIskyrxm518SyVtGV7dIgfZBbq8pRmAk9e7QPPtWuw0bj_VFvb2TvqppCobHn-VRWhCxzh6SIgFa7cKQNLV75AbmW_tRFdd4NuMvTXtDj0IYbz6QsDPFKx3TsFWpoR7RG3EBwsNou0EAiK1Y42bf2SUIhqFdl7_KTmqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=l0aWx_0K1Ow-ULzwciaf4G_5tLpzGtVw3O4uCNC0Y2WY2AgaCfmaoQ10XN2evttS6j748Yzkx9jn6wmgCsTklzWW9YyCcs5FtUYb-nJcn-GQSXOI8jRoG0wueNvyjfY8V9MZqNJlSWP2A0Ljrqj7rc72M5P_ALQcBBNz0I09YXegs-1wHeAQElTaAe_v_EFa42Ph6Y4AniColsONn20uQKhesPQEy8N0GYnJPCsXLktsW6tyqS70BKxl61MoW9PrNEELbQXKAf3RBX-lyzFO1Z1zYmCI9Fdvl39xsebsig-nAnHezvlL4gkA0HlSVMk1HWA8_gLOriFT7_eJrCRA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=l0aWx_0K1Ow-ULzwciaf4G_5tLpzGtVw3O4uCNC0Y2WY2AgaCfmaoQ10XN2evttS6j748Yzkx9jn6wmgCsTklzWW9YyCcs5FtUYb-nJcn-GQSXOI8jRoG0wueNvyjfY8V9MZqNJlSWP2A0Ljrqj7rc72M5P_ALQcBBNz0I09YXegs-1wHeAQElTaAe_v_EFa42Ph6Y4AniColsONn20uQKhesPQEy8N0GYnJPCsXLktsW6tyqS70BKxl61MoW9PrNEELbQXKAf3RBX-lyzFO1Z1zYmCI9Fdvl39xsebsig-nAnHezvlL4gkA0HlSVMk1HWA8_gLOriFT7_eJrCRA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4lHm4YH5jA64S3H7J4h0oEVsAt6eCNQOUs4BUZtyiz5sdl28UeiAF1u_y1YibnyoeJ2z4LXx8cPpJaZL_nRF_6ezlc7dMqCS64-GWSdTF2gkxkHLetBPUTs47yiVTcZCTAT--uJS8PTGlQj0SCI7obamRDZB-REONosXSGXt79-lgXFSKBpocHFVW1LeOWSoD292vmrkbruUaq_6KBXMZR59cnAcb0L3boYXo4RL8Ab3If8qYlHdt2CuC77KZYo4NNzJ914hq63GptcVAS2hxR3mFBeSyr59PC8eDAhQrmFHVeLNJqqFocemYxZTDzTqfizQszAlcb_QLIDcxHYYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb9gpdhPrqcplf0EQNR9XNiKQ7NrjHu145x8eHBJ0K5o2v4Y5pHB2i2XWTB1YF-8JsUCKAMkgc9S6CIPFRTgp2OUlGIgRCzftaFUD2D7-wWTKGwJk02qMsgHryBFUNZ8b5iNaRYD0OAgntcIth0z8n_jYaFUfEBA-7LO_iz2058lloP8BUzJKfnRYH92XDTEz7BypwDLAvazH-EluX3JGN3DQsErF_1lBURZ4PGGC3Mx5CGN3ZugrDEKjrtwvKXYwfJDgRirFSRR-H9Y9ErhqdbvbQYDIaEQoptd8dlAloe77lwt7jZaHcz8voOkmQoTOa5Tz0pLrYpcw0x5sPe31g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=pKo-evco5YBub5YyL1SH2JfXljETYY46kCp63EQ39VzxRglivep7m4YXdEOMWhLHZkK2WwXQldFuOjopEINEDnru8QP1p1M7mfTwzaQJaJZ6LFheQJQP7M9eyG2MeFROWcgK4-6Ijj-je31w6QQ5feTBB-jZwRmLGlemEXGS3pnfTamWueezn-yAxpHPaddH0aAIxIp7zMK0x4Z1cMDbub-YqUYr3qVVAf0RAcmFKSMXsni2OqbE1z-v_bmxhuA58PXGBbnrRj-lVGquQ3ZC5iL-xRxxnNurFGZUCXZh6nj9BWhVZo0RFn_q8wS-C7p9TV4_SsZSqxTq7R-htfnb8qve1wU1n8ToNQszpa1yrvxBir1O_ix_r6BcvzBMaQHNBDuVry2-9XSv-lgHNarL33r-Lj9TKUxraqz1EUfoJEFkywwAY8QSMGaS7V2pnOy9Su_IFYRYvFjSSCIV8TUqoeytKL33B7XIgWl38A6vsvsxjGqiphwsJS3DGQBzzUll0xPhJqYoMFEyGIDnPPrNRhtRQZYp-xGM-VlBwuNMkOjpuVVgPiQDftVWLz09YZaoro3XLIdloesulWals9qUklk_hQ0L9rElZ5G6jPDJMdi74foOcTvvUUbg4zFJ_QUW79okVf-loxHfPJpnrPqS0y84A_AWpxXHTCZj6BpO9FM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=pKo-evco5YBub5YyL1SH2JfXljETYY46kCp63EQ39VzxRglivep7m4YXdEOMWhLHZkK2WwXQldFuOjopEINEDnru8QP1p1M7mfTwzaQJaJZ6LFheQJQP7M9eyG2MeFROWcgK4-6Ijj-je31w6QQ5feTBB-jZwRmLGlemEXGS3pnfTamWueezn-yAxpHPaddH0aAIxIp7zMK0x4Z1cMDbub-YqUYr3qVVAf0RAcmFKSMXsni2OqbE1z-v_bmxhuA58PXGBbnrRj-lVGquQ3ZC5iL-xRxxnNurFGZUCXZh6nj9BWhVZo0RFn_q8wS-C7p9TV4_SsZSqxTq7R-htfnb8qve1wU1n8ToNQszpa1yrvxBir1O_ix_r6BcvzBMaQHNBDuVry2-9XSv-lgHNarL33r-Lj9TKUxraqz1EUfoJEFkywwAY8QSMGaS7V2pnOy9Su_IFYRYvFjSSCIV8TUqoeytKL33B7XIgWl38A6vsvsxjGqiphwsJS3DGQBzzUll0xPhJqYoMFEyGIDnPPrNRhtRQZYp-xGM-VlBwuNMkOjpuVVgPiQDftVWLz09YZaoro3XLIdloesulWals9qUklk_hQ0L9rElZ5G6jPDJMdi74foOcTvvUUbg4zFJ_QUW79okVf-loxHfPJpnrPqS0y84A_AWpxXHTCZj6BpO9FM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o75drC5N1pbsFUyBS6DlNcg7xpMOq4BGHyjwQYNfcaqR8mnP0YuNDWnF_HxlNXs6JnIosWQsmSSVO5b4RTjSvtrnYTQzfQpb7pFG3j-1Kqe4bt_4-4Nz9WC29CFvq9W8z9p1QLYKxIR9bqhn-5TNgr0HHgH4mZxevm6T8BNlvx6BfpIysMzHZYN24kc2gmGffUNGrkbdY9urrXE3xHDNN0YWSsypx0nZLwLRpHZHGxgwr3ZDLcZT505BHqu3Q0NWFUM7XRXoXuT7coXGGMVLEYXrlJ2yYmjjbf647X9F4rAbOBOH7qBBK6VC-GtH7F42ZT2U51iFuIze7jgwdgoXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcVzlAe3R7AF5otxfrC-SUay8OgE9TYcTqxN9MXropi1EAilzXn18g18VXu7eZCNJGE2OGXfU1aQg7uh-CWWA1lAVTvbtEAufhtWTQD9idFYhDdEGbHRcb07dECVjFOkWkCZun_l7F-BimW36-D1Nj3dh3nbRmlvaz6ONLVKKlGKTYCPXLSe5QfaRWWSdN4S0twAv0qOTdv0aClNGqkVgN4h35Nw337QMaI4ZpCXMfnFUshmq8-rdWdGhB04rTt7k5B0HGV3te5cUAw3CC0NyDy13ZN-RNbfzVL17SVH4kv7JCP0sKolBLC02jTsZ6QgGnkTEhTUq7PykPn0Vrjh95AP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcVzlAe3R7AF5otxfrC-SUay8OgE9TYcTqxN9MXropi1EAilzXn18g18VXu7eZCNJGE2OGXfU1aQg7uh-CWWA1lAVTvbtEAufhtWTQD9idFYhDdEGbHRcb07dECVjFOkWkCZun_l7F-BimW36-D1Nj3dh3nbRmlvaz6ONLVKKlGKTYCPXLSe5QfaRWWSdN4S0twAv0qOTdv0aClNGqkVgN4h35Nw337QMaI4ZpCXMfnFUshmq8-rdWdGhB04rTt7k5B0HGV3te5cUAw3CC0NyDy13ZN-RNbfzVL17SVH4kv7JCP0sKolBLC02jTsZ6QgGnkTEhTUq7PykPn0Vrjh95AP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=DhNDeMDM46uM7WJmjTWzC5wX2yX5wqwbRA_cXy6_FOUguKlvdurOWE84tZAt2PMQu2xnHs7_Wa8IwQrPmb0WksKr_IcX4_eCxIn_NqIfPfscEbO2TE-byCNfOQfJPj7iOv0rAFTcwxqMBGj1I_S95DD97Wlmykz_d3mIXto2eCHdtQ3g7zn62UDHHKRcKCwYsHk_O21cAmosu5UsG9ElefCNAPqZ55wdL4p8-kUhrCBdybZncWpBrNh6Kro7RYU4SpjeSoB0kIRMwr4bewwqEcNcJzL4clUulmFQbQTruRlq6hnfTtMamefNfAMROOi7uctyjP5GkRdgT_ZYCtKGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=DhNDeMDM46uM7WJmjTWzC5wX2yX5wqwbRA_cXy6_FOUguKlvdurOWE84tZAt2PMQu2xnHs7_Wa8IwQrPmb0WksKr_IcX4_eCxIn_NqIfPfscEbO2TE-byCNfOQfJPj7iOv0rAFTcwxqMBGj1I_S95DD97Wlmykz_d3mIXto2eCHdtQ3g7zn62UDHHKRcKCwYsHk_O21cAmosu5UsG9ElefCNAPqZ55wdL4p8-kUhrCBdybZncWpBrNh6Kro7RYU4SpjeSoB0kIRMwr4bewwqEcNcJzL4clUulmFQbQTruRlq6hnfTtMamefNfAMROOi7uctyjP5GkRdgT_ZYCtKGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkM2aDjhVQVmQo_CmyfsBsqSUcQ7GDZTMwGioI8XLwhlz0pc9wEWDuL9JNtjV9P0vrqMMfinLLehGECoptX85TSPX1HpCQDUK_aRR3fbTp4Dpf_xW1guWYPz0oLrrZb0bjz1XDk2JvEb848lUFEqwJl5Pmm9AiFUMOQYBvMD5B8YK6Nd4yMiMw9OKNbByE4TF6G9zzBggihvUKE_4hXefBTLQZ7Srh5CWhs4h3o4MUJX1fzH4p-HIm8_FwyHtwNrHeFce4rsEQW7ad0xA_tC8qYFZuemTm4EAMGBpji5tcfKVr7PgmsAgvI0kRQwVBAtHpfbLphlTl3N1ZFyR61g5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=Gf4jaljK7YHj5S4IpESPRYGdjYUlxK0E-DhPSF3DYrpE_-rbN7Ef8yquqxS3ecqC_iAW7vaefAviFAB20K5JqDfX9PJEAMKG-A9L2VYA_hNlNoYRgTqqP7uiQZSa50LaI7wXinpOs8romyFxBQPejSIIrbNvHrk7-Ymu9SYZmPhVruI2tcKwoDDqYoIez-6oi4acrhOJ83YqVRVZQfu2rgvp7k76CXSNZGj_cRf50i1tXiIU9lGWSfIca4dtYPZHVprd6Sm_oiuNUJxFl3puhG_b1cDaHHj92pavduqAvbPQv8qOxnDhS9Q3UO6ULOOZpu65EplTqQJ_pGS7W_m_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=Gf4jaljK7YHj5S4IpESPRYGdjYUlxK0E-DhPSF3DYrpE_-rbN7Ef8yquqxS3ecqC_iAW7vaefAviFAB20K5JqDfX9PJEAMKG-A9L2VYA_hNlNoYRgTqqP7uiQZSa50LaI7wXinpOs8romyFxBQPejSIIrbNvHrk7-Ymu9SYZmPhVruI2tcKwoDDqYoIez-6oi4acrhOJ83YqVRVZQfu2rgvp7k76CXSNZGj_cRf50i1tXiIU9lGWSfIca4dtYPZHVprd6Sm_oiuNUJxFl3puhG_b1cDaHHj92pavduqAvbPQv8qOxnDhS9Q3UO6ULOOZpu65EplTqQJ_pGS7W_m_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=RD5Kayys_lh7dGX7X4-f49GeYsrm6Sz2QDAIEDx_v_SEgb1C1UurCti8hT-EIqme2e_QV1Np95AeVFm4xDek5qf2KGjsOHPrnIrrRz5AX25NfgggSV3I49qGF9WAQpEIseRPtMxRh3dQPQubNh92UNBvoDUT3CnUQWkRweGVvX3moZpXdF4Fjteh_c7_4idbXj63O-Gw24WqoftaUm40CmX1pVptnrOTT4eEIw3X8CbTk6xQVJhpAThtz9CKV8BwNN0vR4FrQ3jmn3XzO62-F7FmDn_zN8KkheMHgurPkQZrra0AjYKLLfuc3V235nQUdVpu6fxFKO4U1hpsL__smE8_VGf8c1TcCjivgwf4cz6vJpPU_xXqNDKSOhoFqQ9oe6ZvSYm1hDOYLVrzt9irmn5UHk2OQZwU-GLoYXCAcpASJfmxHonhlZ-4YTeXXENw83V9DMNNOdOBQ9juHkcRXE6--Vnk6uvE-F20w4xKZHFBnEtZRGwInrmUkSQopENRtkDDke4Ym4pvPe3aPC45j04fVOZlazA3Cbv_e3MiqkUWzorIrOxNqM1UySHeJMVnfEtPSCVW1i4_L--SzuwbtuImBsE1tmhsXIAG0soPPIhERxpHb__vpPi7NHn5D4N-VvpDSwzoh3IkHMddLORB_rqvGHW9TmN50w2ylyvfyDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=RD5Kayys_lh7dGX7X4-f49GeYsrm6Sz2QDAIEDx_v_SEgb1C1UurCti8hT-EIqme2e_QV1Np95AeVFm4xDek5qf2KGjsOHPrnIrrRz5AX25NfgggSV3I49qGF9WAQpEIseRPtMxRh3dQPQubNh92UNBvoDUT3CnUQWkRweGVvX3moZpXdF4Fjteh_c7_4idbXj63O-Gw24WqoftaUm40CmX1pVptnrOTT4eEIw3X8CbTk6xQVJhpAThtz9CKV8BwNN0vR4FrQ3jmn3XzO62-F7FmDn_zN8KkheMHgurPkQZrra0AjYKLLfuc3V235nQUdVpu6fxFKO4U1hpsL__smE8_VGf8c1TcCjivgwf4cz6vJpPU_xXqNDKSOhoFqQ9oe6ZvSYm1hDOYLVrzt9irmn5UHk2OQZwU-GLoYXCAcpASJfmxHonhlZ-4YTeXXENw83V9DMNNOdOBQ9juHkcRXE6--Vnk6uvE-F20w4xKZHFBnEtZRGwInrmUkSQopENRtkDDke4Ym4pvPe3aPC45j04fVOZlazA3Cbv_e3MiqkUWzorIrOxNqM1UySHeJMVnfEtPSCVW1i4_L--SzuwbtuImBsE1tmhsXIAG0soPPIhERxpHb__vpPi7NHn5D4N-VvpDSwzoh3IkHMddLORB_rqvGHW9TmN50w2ylyvfyDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXzR8iZOjacJfDrMcHIqhK2YTUekgxKyGv6cYBFymGiEnvGOkmhrrsByqSmOwZujZaEuGHOwPnf87H1p9kiU7OsvxdQ8O-pJm5JNlbeOdqY3ytH50-zA71POf4WTq-cbB1blYXQNIVOVjOH28W2wRbJ0CwQ9XTriCVQvzOFwzNylKBUV-SQ-JCRto6i40qW-UrDpWkC1GtwEmtApK6ibVl7XyaLR8a6zPZ5VyfvP6r7nIAlBQdst_tC8kslpzGFLq7QBDnVaB_aElZKfzx6P6QJOa8A1k2u7bPDVYL6Sn-i108W4oX27vJq-F992uytQX7kJn4cxbmZ1SarQ_0kQqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB2Ok4IUyTgzzhK1DQoECNKxGDmt2utnjP7k9nXYUizC_IiME1QkXhubUzF12RTEItXBiDbuK_dyjH0lCzW1GfrSpfu2jl9t0bRND7b8_BaE7Z63BWUDetlEEYq0Ivfjxzcfvp99fM3JTZUHVeLwDfFBWP3bHwzMoonv4_JSEBCZ3T8eLAtLluh1TN7dYeWRmGFBrS5zCIdn3KLdlNWmTS6qkcEkooWG6EbFPgb2HOuu8XG9SlwIcPQ1k8DmgSz-pRgGPTsOaBV9lhIbRcq3Ez5_b-W8NzY6bHH28fvQeYTvntI-E_8pfc_FV2ROS0V-TmkFDGwOgVf-sscE5sVjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXfx3FEWyolVFAv64CCQ0st3O3GAeqp1ouloLm0-jIGvpnEgQuluNEIxWh9DlGQcLq7EW7zdHkNgyHYFJG5RaTFx5b39ijnVkbrXYMIhIgK4HRoMKwUMGACATQzNRYuY7uEIM-sVk2cbPgGTPqr5TiBY_mEOe809YoTKy7AdedpbJsTqvQBOQFd0M0LC3NArSDrvNRYXzGKAbRoW5sSeTBqf43WHMXIaKNFSqv4Bz01lF5SSoTU8GS8iOJ2EUlQ850W4y5HGn8wrcmnCEg3IL3IzvtatSXr6m0s4Rn-yMO7ecVnvhA3hkh8UpoChXrrE_8aBL9Dimxnv0X4kPYRTWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtjBURAdrST7tZ7bajsdDurBTSSOb9HxQhukkaz_GLu1lpH5Bp7RzIrxHSxjPpGzhnuqsQVVZI-mA3cOXkWmzJKV3nDw95XRxt-q3Bi0boKaWGUVN_AOK9aX2ADNj2wvju4jcKrxDUCjz0ARAVRhgdgjdoTha6TtA0lZ4vf78TJNmwHZ2ONmQcMOOEAin6URwpYxXkMAUjCvX93YP6NPx4BGSw4og4cHgSsqaRpvlo2bCl42-p-Cx_yBHAZjygwFXvE2R5yMUu-_vB2tQ3pKvhUJRisbQGxMUlrsrzvB4bV6x3nqs3VZvUcJXyh7FcTv1Kt_bAsA_3FI2eA2hWca8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-uOxtfOgYw9aufiLM8Muwijr_OnNT2_ax5pYVyHLOkOwMgxoPCfmEEewjINGY-XVXKUR5F6LTJiqYiWljrp-gXdh4Jy8zb_2coajJto3kGLxkOK6XZsJbUnGv3lAwzqmC_vJhtVOMjXiwD-KR11GStG8YqdgQ2HSzNKdO1sQPMdT0WAprcJ1dT8X5lEm82eeHY1VJr3NKpfbN2EMyDvaIYRPsFK75buuq8J2LWsloIBWXgSgzON4StGp43e7Bt1cZqrzU_z0pceTwJXaVyk_oh_6UiCCkJc_0Y4Uoql-Sd4F6q7YgbVsi1gNZ4vYGLUTI2RwTJhyHRSLBAhjyeF5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMhWujB7sxGytduR-egSa1f6Q_y0qa6C1XTrG-Osk3vdCuzySjo9qIS8f7Iqo2ebliwRdS4acsZAHYjjK2_OhVkv2hkMsOLrxePxNqGETHw9DQDiCzC3yY33BdJMBk1YwPxSeVPCCwE7ziaxnqp72nISUvpleBhP7kkkCjrJToS8uUBHsKdXdcyfk_MkXn5ZD42rSxo9HvQ8Z4SXFvQIEBuSLgsenCJIiNWDzPizulsSYT9IqbbB-CnMDqBK_o7LMEmQuXKgeTjzYrvnOhDqHDr4hcEnel6gUoaJJhTBmZ8qBSQEMEqBjXU7wwWyHoqnyWJa3UuZtxwaKSSm6nLcFg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qnE-yjExTFuqdeNmuv3ySkGV3Rn4SwqVfwVbs2wOynFc0swpofmx51Nr-_a53yQQOD1rcNAGg66rS0YyQ7hcdm7npeUSXnmMNP-aQTEgszr_yE6tX4T7_Ak2Tqkx2CIzvShi5_fMM_F--gqkq_jpCLJBLwZpqpJGe02KU4O2XQzhLvTlazwIp3o_j1GypDyYbF6km3xpl1UAhqlTb7HWAi_Mh_BuhA_ZzQLTTzGVz8O3agwuxLEeBw6ysKx6OJsyG7cyYdLVZL9wyEgo3lns7ywaDlVXxu4giRn__tMk2E9Vzqbk5pLfE8sX_q_5PfHoooVmFlgZwqBUmI2Gn2c32pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qnE-yjExTFuqdeNmuv3ySkGV3Rn4SwqVfwVbs2wOynFc0swpofmx51Nr-_a53yQQOD1rcNAGg66rS0YyQ7hcdm7npeUSXnmMNP-aQTEgszr_yE6tX4T7_Ak2Tqkx2CIzvShi5_fMM_F--gqkq_jpCLJBLwZpqpJGe02KU4O2XQzhLvTlazwIp3o_j1GypDyYbF6km3xpl1UAhqlTb7HWAi_Mh_BuhA_ZzQLTTzGVz8O3agwuxLEeBw6ysKx6OJsyG7cyYdLVZL9wyEgo3lns7ywaDlVXxu4giRn__tMk2E9Vzqbk5pLfE8sX_q_5PfHoooVmFlgZwqBUmI2Gn2c32pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pq9rPgSvuDgJzKLVzYraqlUaWjrUhVNbuBGiRGnqsRl0JUpRBpk3cg4zLQZsEjIQ3-y8kvLp3tRF5IhlHl2TCck_kZq-zoeg2GyrN0leM3WkE2t0jw8JwhtUHyXkJ_Y4oawGeL-n13iV_FnbQoPBMLaCc820c-CDx6a-l7bKrp9BatoFreBlusB6P92MvIr44ebbY_ZuObwSfLYj-AeJdQt3Yyg7Mavcm0E4XE1a83Vs7KOVVmie9hqULOSWOxGDf_r5H4we84f0zXWLV7xU39cUmglQxAA4ieMPoRgVT6UftTVMuSVgsg_-3ohaQ-GsSndI017XOgtfwxwqHiFixpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pq9rPgSvuDgJzKLVzYraqlUaWjrUhVNbuBGiRGnqsRl0JUpRBpk3cg4zLQZsEjIQ3-y8kvLp3tRF5IhlHl2TCck_kZq-zoeg2GyrN0leM3WkE2t0jw8JwhtUHyXkJ_Y4oawGeL-n13iV_FnbQoPBMLaCc820c-CDx6a-l7bKrp9BatoFreBlusB6P92MvIr44ebbY_ZuObwSfLYj-AeJdQt3Yyg7Mavcm0E4XE1a83Vs7KOVVmie9hqULOSWOxGDf_r5H4we84f0zXWLV7xU39cUmglQxAA4ieMPoRgVT6UftTVMuSVgsg_-3ohaQ-GsSndI017XOgtfwxwqHiFixpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=tXX36ldj0tmn-YrYCehR_jkVNiZGssWRQMa24lAPQHhiwYWWdxmVVMXQj8fUrtINQqZNrar1p53hRtFay4PBZ4cQnK0TzwxtKdDTPHAv-94pofv2MKhpiCs4pafm7cBNtf3lo8UroTd7mCPhEc0r0ckZL9w4m7zKOLwfTlUPJ2KVX-CIvHIf7nbBIc9FNwWEwqMMyyL-AyWkSzJl8kOCFjkyuHkiCZHs6QTyeQgXsC15EJ4FrbmcaV3Bsci5WoAKhw_3DSg8zke2OB7nyia6m6QQHsfwmfeyEZz82RumLasMRQpbeQvQeZpbDKW4lfgG2RLEd-0GojPGAS8fR9yEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=tXX36ldj0tmn-YrYCehR_jkVNiZGssWRQMa24lAPQHhiwYWWdxmVVMXQj8fUrtINQqZNrar1p53hRtFay4PBZ4cQnK0TzwxtKdDTPHAv-94pofv2MKhpiCs4pafm7cBNtf3lo8UroTd7mCPhEc0r0ckZL9w4m7zKOLwfTlUPJ2KVX-CIvHIf7nbBIc9FNwWEwqMMyyL-AyWkSzJl8kOCFjkyuHkiCZHs6QTyeQgXsC15EJ4FrbmcaV3Bsci5WoAKhw_3DSg8zke2OB7nyia6m6QQHsfwmfeyEZz82RumLasMRQpbeQvQeZpbDKW4lfgG2RLEd-0GojPGAS8fR9yEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=CC826FpsrLeo-cQ8Z-74K3rqhXI6gK4sd5ArasMCI1dhf2BUpdOfpTlp_uf8EPnBxEI-gEji_4f6UPVyV8rKPTwDiJEfTHkHdsxRTXDv5L6V9zKnn4GoB7bOhHHFJkG5MmvcWOhdcxHGQ2gzYnMPe5gfZRyJQIbKSDatKihsuKQaz42FoB0aZtDHBMQeG5WkQBvOf5TtyIYsUIS8m_BHMnY8vTtDwqLZHqR5hQNftv4sJ3A4np7LVdZL6KNS-7ZKtL3utH8BekdASSJ2JqEqnvSh1JEAVwOEdRxI3ATu-3Z2m74V4ZfH9FycFkJQ2ZsoIFnwpaVJ8dYCSqq2Nq41Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=CC826FpsrLeo-cQ8Z-74K3rqhXI6gK4sd5ArasMCI1dhf2BUpdOfpTlp_uf8EPnBxEI-gEji_4f6UPVyV8rKPTwDiJEfTHkHdsxRTXDv5L6V9zKnn4GoB7bOhHHFJkG5MmvcWOhdcxHGQ2gzYnMPe5gfZRyJQIbKSDatKihsuKQaz42FoB0aZtDHBMQeG5WkQBvOf5TtyIYsUIS8m_BHMnY8vTtDwqLZHqR5hQNftv4sJ3A4np7LVdZL6KNS-7ZKtL3utH8BekdASSJ2JqEqnvSh1JEAVwOEdRxI3ATu-3Z2m74V4ZfH9FycFkJQ2ZsoIFnwpaVJ8dYCSqq2Nq41Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=sHH6hZ4iMVGCLo_YpufgT4OXDXrI3SshdNGhija4RQc7JZHU4MAukBCEUebH0dIKXVj_i9XkAA9nHTt1nWl82dwzL5xEMpRorswwIlW9Zj8Pu8xTquZL9ALQ05-7L8HNzPa7hCyEpkEftqRkz49Skf440J2nPVtX6m2QxIWH20BIMabyyZAoTns5dH_Q0RWRFUBxinSUo5hV7TmszNFWug7wRLCXnt4-kswtkYDTyIe9cDp7Gs_6Q-26h6SSlrnVC8Hm1tHLk6dOIeqIdhagO-ALQN9wtfBX9KZBdqN6-mxiY3GUnO8p0E0JUL48_ieXpCx6Rv_5ChBO4jASEH3G9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=sHH6hZ4iMVGCLo_YpufgT4OXDXrI3SshdNGhija4RQc7JZHU4MAukBCEUebH0dIKXVj_i9XkAA9nHTt1nWl82dwzL5xEMpRorswwIlW9Zj8Pu8xTquZL9ALQ05-7L8HNzPa7hCyEpkEftqRkz49Skf440J2nPVtX6m2QxIWH20BIMabyyZAoTns5dH_Q0RWRFUBxinSUo5hV7TmszNFWug7wRLCXnt4-kswtkYDTyIe9cDp7Gs_6Q-26h6SSlrnVC8Hm1tHLk6dOIeqIdhagO-ALQN9wtfBX9KZBdqN6-mxiY3GUnO8p0E0JUL48_ieXpCx6Rv_5ChBO4jASEH3G9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=VjST_M3KIZ9BpVjM_sj397XJpcAMisYOXVpMO-4Z4rLWUQHPk5Xn_DWGHv_1LC9Bx0tlcheFQ8uqeymniQV4yBohO8mOq9zoN5Nr6w84WnWLcrrZifJs3H-A4_u-1YxDga2Yn91mMUb6_vwONhzdF7_k7-AyAA00yOV2wx8n4gbIOXhEIZnW_Dd-FniRdufUquFh2ov_eBa_YUOX10ldjhdm7i2kFJ6u6k-0Be_nn2rryqCrHkIJZy3nYz_FFVMVb6WyWb2iiD2XykxW_8dPvRKG3GisKNccdQ4AWof4vFlo2NdVdVBdiR-le3dr6nHbDtdN1St64XtetuP3eTA79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=VjST_M3KIZ9BpVjM_sj397XJpcAMisYOXVpMO-4Z4rLWUQHPk5Xn_DWGHv_1LC9Bx0tlcheFQ8uqeymniQV4yBohO8mOq9zoN5Nr6w84WnWLcrrZifJs3H-A4_u-1YxDga2Yn91mMUb6_vwONhzdF7_k7-AyAA00yOV2wx8n4gbIOXhEIZnW_Dd-FniRdufUquFh2ov_eBa_YUOX10ldjhdm7i2kFJ6u6k-0Be_nn2rryqCrHkIJZy3nYz_FFVMVb6WyWb2iiD2XykxW_8dPvRKG3GisKNccdQ4AWof4vFlo2NdVdVBdiR-le3dr6nHbDtdN1St64XtetuP3eTA79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNYlXcuqrbkOm7ZF7MqNgrQk-rFBmy2mU2NnYCbsnysArzhSXxa8BPVgHj2aJYOKOCZYNzHO35kevFoo2EDCjIBcxpJJBM0h8mANMMyqRQZPE_bj45FmOOoOKlaRRjxBd7zJb7BDiFfEPIGcZoSRPoJWdOma1Y4wRYVS8PfbGpwVpWfetA3W1SQ-hBtiU5bhtUV6wQpbRCXlYLNm1WA-ULIdbBIfP2g9s4wrE6-bu-eMA43Wn9YU6GsaLpEwP-aO60ZCgQ3Nv8pPxBnPYX5d1Jyje5kW6nReSw31fzoVu0m_odm_0bBLZCHbXZ80_G6VD_1sN91wX41Ke3b09nzrLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHMei_U0FhyKegOg1YqT3d1jjRd4yjrhTvKJuHBEbkxlQcvXCYhRwVLqk7yXkT21C9D-o4pwfW20XwVrV1yQefPIKI_ET-NlZgjC4SlsIQlVBjFNFo2S62LaTp43ZN1OHzL7f2GK0fGpa99lC9CBuM9rCq3kZL3kCTdzrQ7sow8uLcLizaVU0HylLGkN2lgArguNOcQ7BwRcct1-OCBiQBll6In3rDNt0BUCJZNuq5PrfxCsPbhdBvXSED2xjzm6F9vRs9RzTB8hdfDTWbf55vA4BUBjhLd8BtUAIgyBNyP33FWSuyXRAYM42l6u3A-4qwuuxTb1UmCnVOW2r5bNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=M9dXJ4Fr4hdniiRqKIZXouY_f1jSnz7QBqSSU-3_-OiCJS8IED3G1NeNHV00qt-NSMwzWQUwNjo7XC1KmM-J9pH2fhgmINx8panN6dy1qnk2nsj0MWeBTFYViEsF3gtlvDyiFvAEcrsSEbJ-T2XnRppa7dIgQ-olE7Nq16D-sc8YhA3N_Kde3Cf1L4HcALnf6oKwI_8IDlR_UDIbBTt2oUE_eUg-2Ed_ztpp8sG8OtEB8XkA7TQFg8cg7dVfmg4q5_BwaJTobLg2v0RlcLJF6Xeh1ZtMHiPgowvITApQN8SUmQsqMDOKjdRYUxv7RVl_tp985fD75etrM3kbS6A7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=M9dXJ4Fr4hdniiRqKIZXouY_f1jSnz7QBqSSU-3_-OiCJS8IED3G1NeNHV00qt-NSMwzWQUwNjo7XC1KmM-J9pH2fhgmINx8panN6dy1qnk2nsj0MWeBTFYViEsF3gtlvDyiFvAEcrsSEbJ-T2XnRppa7dIgQ-olE7Nq16D-sc8YhA3N_Kde3Cf1L4HcALnf6oKwI_8IDlR_UDIbBTt2oUE_eUg-2Ed_ztpp8sG8OtEB8XkA7TQFg8cg7dVfmg4q5_BwaJTobLg2v0RlcLJF6Xeh1ZtMHiPgowvITApQN8SUmQsqMDOKjdRYUxv7RVl_tp985fD75etrM3kbS6A7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOEsYd9brvnGlbOLo-qQHqMNSVDNiiQlriMdhqwmE2A2ITxZg4hWexjqzfmyXokuj1YgqRb4N9CuIz_vxzclC4oQttBgGXZyvuCLOhxGIFMiefYJhcdi61ZzfzwcVY39GF6ErQmnsXaesOQHFkB_2a8YZ6GKlBGKzAJZcuodZlMarB0PARjlue1OFhniK-DaV5smlBUxySDRg8qLyOAYUmhON75PUvBkfXcs2ej2GoEnLidoqa8eM1VoKjeLgz7Mg7KoGJzZYaZSwoi7iACfhRvnj9Yz9TegwLBzML03JgIbJMRu9Tb7Qvowf3PmByxYJeWOD_-lLjZzCL0GdbAHQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=vzP3xRrVftsE2_9uR7M_d53OeLFxfgZNZpJ5un3G1TOKfxQ5VXOo5cVDCMqBwyzCAcDCnUr3-5cEmJgToKs0naLGTx8lHvlWxBBcKsdoslJwClUa10dTAxH0bsRBnSktFFs5cU2lwcErGiGWBQZ-bWZfqsLT5s5BuGlBS8P5jnilm6j_v37wMFa8YUOteDWL3yfihzfDsSRVX8lirpZCcCFnxk0NJ5iIab1hGd8X3MeOxZLw2gghovwu4BKDUYn6-_VeqVqPxdQqfTSbcWEMqvgbQeGN2kZcg8HaAo_XxCsx6K1uVjxjAQjkg4jsNBbi1biUayrtAb8rlwSJhufEEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=vzP3xRrVftsE2_9uR7M_d53OeLFxfgZNZpJ5un3G1TOKfxQ5VXOo5cVDCMqBwyzCAcDCnUr3-5cEmJgToKs0naLGTx8lHvlWxBBcKsdoslJwClUa10dTAxH0bsRBnSktFFs5cU2lwcErGiGWBQZ-bWZfqsLT5s5BuGlBS8P5jnilm6j_v37wMFa8YUOteDWL3yfihzfDsSRVX8lirpZCcCFnxk0NJ5iIab1hGd8X3MeOxZLw2gghovwu4BKDUYn6-_VeqVqPxdQqfTSbcWEMqvgbQeGN2kZcg8HaAo_XxCsx6K1uVjxjAQjkg4jsNBbi1biUayrtAb8rlwSJhufEEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctnPAAcsP7uff0kmDYsArVlbg0P2gQXs6ANKLbolP5aYbRWpwjZ7jS4YBT5y7fKC_0bBnLe_o2kPRIANbZJMprDj1kDf1xj62kzLNHIOboBB00idDU0WixATrLlL3oeiOhviApogrp4rYC22NrCtTyU1hDON8T4iruWb_QixB07-XJ0KuSVARjtK-Nq_iDQ6r_oEn44Otm6QDWuS-J6NloFP3fUZs6bVejaSHPytv1YZJb0uIcpck_u07KdeSN9iJSsmpfJfA5oXOQsEllhcTCmYF8sA_b2lHwvjNww-whWBZ7dYLBbVn2FuO0PtXzYEuqmNcfon_pHvJmH1AVwRNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0fCMLPvrxt-bw8oNuQj_0LlTyLe1JXK2_uOIx2A8AU-UkmwbP6OqPOX_W4Motm6VWI-iRZqD-cB3c7zhF2T4iFrhmBUb4U2PXhvjWp8wePIc-4Fg0g4tLvPjhI7AqOKb2QpVWV_6EhafFOv4_MO_Qyl70ba98FfXEQ9Qj_Vr_2NBXEic2g5YkjafQnAQZNlQb80sq8K6MOHQpfZ9PaBlfwNCitDa-TPbaa1ER_ew9jxc95PlXB8bq0nh3eqYHt0IYFfMCipNppoWhHZrOa8ZUaoZ4SWoMwyFw3__lr10pd1RodJ7jKVjtg2PlNOXdgADzsy9d16pQThxyUy7ApR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXLLIdQKQt2av77OWcVmuUOtW5nlRyPkbt9kL5DZA42jdjH4CmZAq-_89Wyg0OuhvqhHDOxNeXnOrvQa-59OTCzgMv4X2SjeDXBU2nNFf-I0CZODrMLJgmFLUYmu9AC-6LbwhvmfUGdLmWFTz18OhhJipn16yydGW3-KbC1Gg0570YYUXJ7NXWb6wCtaCjm-0liHxp_04AfP2_vgQb7I8pL7J9Itr9MQQRcT6EFoAjEs3Fb8pZd9QOYrHOQ19XqXMDub-dfwfJTMdSBYBccTdTc8bpbtbF_RgB2Y_57XyCS1VrGTTSqWfPP-ndKNxRIhLDZYYt70K0c3qLbvB5UmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X805vlRk6mTLPI1mLFPD-5lT9mgWS-qm3hidjhn-Lj9I47z_P9nqjeZXLgT01SXYufrc2hudM5WdkD8ibwM2aTR3RxFPk8JM9BM6SqRSzBDE9Sfgq8lw1D6PTbUh33FqWhKFnDx9zYvn38BQTFmQo3oDJswJjib6jnGkMoobYI-XN09zNNhljzXzrlbQO-TKo_eZXmDD7N8kVgKvTm3BSwyYRg65kyfXu1EUpCnO_ouPiSuXjpoLxqClX5BJ2549FLnS-ZmGM0mdJOUNILvUeADf1inIF_rtEOlzWPsnllo78CvlSvxdW6labMrNJLL0DcX9Bp0dvOctUID9n5Lnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBYS2i9uyoQBdSarYCnyzr-I2XiW90k4UztCP-saYl6j5MYKZld5YTEywHOu9HhBppEVUIPxK0KssnGHFYsOaydwT0em5BgbBxMU-wrNtVpwsnIq2GaBqF5Zfwexxi_jHJF4Qj7mPmU3alznvp10crQ7VDo8d43kebpj_Snsm5CHMifM3mVJCLIhKqwdwHKJhfa9zQnBoeN9CjJbwUoXsqmopaEfQ83I5o78nwQBvWEbBVNxIyFQJ815mjWscIVCHKHTdU2EsaUHRxwdCq_HEroDqX7N2uo_Luamp5BGPjCn5vkMA5UNRZX6_gtzQgCy9LOZYeO6JOP6D_9UZHUjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlK8x9qV0bqaxycwptPpqPI9UXwUH8CpDLwhUimDXOJoTowD--6OTlSCTn0vr2SvV2Hr2Zc_8qLF8rgfFVHavmwzogT2WWyTxp_fk9C1NfHRadcB5LU44qvMK9dRc8Vlm2C29h4eRIoprWuTJf439PDufp6ufpiZeJy2KL56u_844Lib_v9YaLno2gm_eqgtX8wfXO-XMaAIt2CElF00i16M24w9Z1XtllZXe5-skjlaq_cFi2pHvYpT8g1F8OqYEQ3kKIYbmzsqnDD7KouOA1XfaPaoyG5KIBMXsBI9p577WnGm-IF4c8qGMJA1rL6pB4_Pk3Ls_B5i2w0uDbNBMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbAk-YA-Ok0F4nEctINDKmUUYaL507bES5pznKxMLU08bPYVjHSXur7tmG3F4SpW1NdUGR1W7VyBRJCPIyCIDObZ09XCr1CE8OHCpPQ2BcFLMZPlpin8P6xcvKsneTrLUjHu_lVONrHfOmV6M40t7v2CMGVzdtD53zH2Z7fz_WffSRnbRlovoNF2zyuA2kxpL5S65AXyxLM7DBqwqdGpU2wXlvFUxcGHwvCqnrSPfg0fbtKkCpNic1ubZjVhpRQ7QwfJAJNbPhAOjYlTUAMrVHnVd-HEM6u-ZC8W_LOwkjl0fzJO7bcECrqpYvcwtrC4RWnT5U5qhiJa1_KTa_vM7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7d1cNldMAJ4KbT_zXXU78xEQ2XFe4I-aO37owXh3NMNBPZSEYl2TGv00gY8eVdAXZQVGSzHuOj7hkY7WdhzVanpWT6CbqNoaM8pUIrG3E-AhSO0Fcbte7OU4qeWBY78AK_TkBoPV7XpfP3wERMuetWEX9xVzFLbrqHzBzeoK4miqnmN-l_EgQVaaiC2_gMELNalQdCwKttUSOf4VuV6-iXX2ym3M2uMzQTXb7wGLCSB-w8aoyke7eZZSj6R6ZZ8XnqODde1F4B30EwC82XHPxFSSX0Da_izgXVJTfKXYPBmYU29sI_zsgUDAsxa4vTQycmDXeWoII2Np6uBxewdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhkLPAEBolutAY8h1VZrlmbx2icU7WSRREdWoK1V-rxsa_jKIfQHYhePvOPoUDO38V4X0x2wwAnYTJumdVQFR7tVo28ossuChbjhoqiGcf7YJqBA9J3SinajgRKzFBxGyQ4wDLlngRo-u7LnhrUCbkJz1Fsb48yACJ_n6-Li5pTVYU-sU3EASLQ9Xp3WaycdlnQ7uHto1ppDnPoHDlPjDx-ZTw7d_ft_i-NlNRPn2232eVXpm-EEmIEhCNhMG-vpmspVNM6A4YVrZieMgrQo39AwzkBqEIye76x7-vZtAoA0RKXgYSohUOrbGhDVGS5AblflUY2mj_BHJCFS7aGDig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4-wL3rZOffGNT1UCtQDGgwmnckepPaFBcodtjJAu_kDFb6s23Cz-xtWdOC8bg5tC2MKzS1W4orJQH_9jfV08FT98CbnTjjQ31zYNl_KSc3kzEs_ltCV6joKXTNBVQ07IArUDaDb1RvYxk8qYo8YRCF-iLcb1IFyiS7dhE6_mD9Ahnrt8fTvOrwPGf_QOfCcB_vmkzD6qDLdy9L4MExnhSzk6No1v-KO-YPhwA80eH6Cpm4aNXLHMOOj96UhNP5YMdAAMZYYqz_m4vuDLlWSUHWQxS95edPm5HBk_Gy22gesOKFS644G_Iq9suwezECx4_HwxrdPODzqphWOIZPC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqYZEeySL52gqXefhOy-ttatEp11AJ6oK9GnpJnpHmApnjLNVeUGfNF8A9cK6QOWZktFlFf9xebrHcg24tMufGRiOyS7fyKfdcyLdOfvN9B5tYtCFJNQ9CEcBrJ7-PFTeTYEIgKDFLBYx9tw4uLJCgCdWAugZiq05O5yxlPI2wZWrXat1pqANPcuVu2Rgrs3iR43ZzcwUc7-WGRemSbnXjyq61dbNSqQEC4gPqJfm-r0k7l0ED3-RG_-tcdCZwHRw2oHj7Jc_W6E3qpYCMy-Z4_nhVxJ9bh1xBDs5YYsG80dcalPrfapc2BVcAOB2jLu668Yme0xEkEC3J5ZpbAOJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=j3r6Eu7NM7-ywULUw4w5Oa1QgIXsa8uHvowyU2L5BmPYLctiQpTHCt5Z6G-aY9Actr-kW5Md46wwoyfVjGeUW7vqK3f3rYnYIUZLi1pF2nbAHdhyhRXPnPmC6_3QZ0mwqLlpbxKwspbOBulmT8npTwUXSxeWvXwwwZU7FOBThQhGHUD98c6h0uHEWEOgUcvJbSUmpPUkeRlWiKrXuzUajccyvN6SebLqk-yYB6Uix2nQvMJEqs4Lpy-QRve7LunyQxM3VgfwLzJHydSXpUHmbVpaAepkiufdKA9ndim0-THy_-jjPUCfQ24qrt68MxihhCHg-7LniO70hlSQ2GDrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=j3r6Eu7NM7-ywULUw4w5Oa1QgIXsa8uHvowyU2L5BmPYLctiQpTHCt5Z6G-aY9Actr-kW5Md46wwoyfVjGeUW7vqK3f3rYnYIUZLi1pF2nbAHdhyhRXPnPmC6_3QZ0mwqLlpbxKwspbOBulmT8npTwUXSxeWvXwwwZU7FOBThQhGHUD98c6h0uHEWEOgUcvJbSUmpPUkeRlWiKrXuzUajccyvN6SebLqk-yYB6Uix2nQvMJEqs4Lpy-QRve7LunyQxM3VgfwLzJHydSXpUHmbVpaAepkiufdKA9ndim0-THy_-jjPUCfQ24qrt68MxihhCHg-7LniO70hlSQ2GDrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
