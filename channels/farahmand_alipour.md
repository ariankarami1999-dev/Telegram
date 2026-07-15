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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDtoBUvfbJ39Au6Rk7tUBj9xJ1WgC6OgSfdQSiRnwNGDwSBoONWMcOe1ZlQAla89lDB6FNpY-f_wBhzo6Q6nLf4yJEWylk261ngT6lX5NylvC6mX68GF89KvhwgY1AgEotYB6uEa2pcW4AOr2qNNzn0nHgWZJLJ75L5gf7DdEyTzUtbm1hbs790jqOZIcNCTFxDmjd57fVqY7SYfspdOd0bo2wrnXlM_g9vxRRpkRgNIHoAa58OrtRmIua6lyHrqMvvL-s7eER0o6qemgITrgMwEJrIcr8HewfAhL4qlUOsN-eZ04KvgcjOSTZO5XVZ8QVw1Lj4fqOM31dNrlpuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwk0MF1CymWQNvBspQ8qRvgCbc9OMnrwCCLvSSTmnNZG7h63TSeiBWtiMjICz44yaJh8FcDCbzEZAQrmBV-uZwz5BLiYRSq8gMvbZtzFABq742ir3Fnz48EBeSeG-EPf6pVH32S5ObLKiOmWTCPNl1wuKN6B2T09g9Q7bfvv-G-lBTFyukyL9TxmjkYB6TwNTMVSXGFJcYhgHAysEy799dAyianAAZdGsNOyLQVXCKCuthOA4kdvPxzKbtTCbGn_MFVUHfjstJ8fsr3VUoNl5ywPXjJRTMk_QEj_zesVne1WPthz_tBI_0fIXMMiubnDq-1X9wrTkke9IXGEUrNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=kxUHmvDaGCUiGVFA4Z-TPajerepMWZWgH7yBcFrvHCqav6IE4mp5bFahXsmiWZz0V0oEE_AK71IyEAmcGfBiRlgcMMrh0WHbyEpPn0HmDiVMig8npG6VnnmeDONmdYjKYijNh_peHTdSIw8vtmoJ69x8kERbw13kexIc0fnBJ7T5_ut03b6q6QVo3czO7iM-pqG6It_4JcrNh4NgzTtLv2v4OBeJsufrnLH2_XxevPLjWGxn4JXjBw_lJpei7cab5jL-wWBiDlhFf0201HK4BlWEKEGANVx0_0g0p5B11wkELUkMPLpJULLBbVF0or7hCBu-PfvYRA_JHWtJK_0iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=NUJpRwMmcErmKOMXPwTPmwidxKbxO_xIEovTZ3e2sNTv93lgJV14d3vNWOA8O2xwigmVk-nZImdUjJV7nEHDwqT-UxnvKB39nCCK0emspc_bkS3q8DG9GbkgJIbhVAJXYdMwCQZTasVsBnF5bwU9JsMNiTCcIlbPCGkua9RQkYee-dqLVjBZECX_b6eK_M8bgqxDy0Td7ox-MArsrbHMqalR7suaN9c-D-Zts0gW2OXXmR5JA9FeCiHu0xSR6xNBMUC0QIoX6qASdNAzpCIGB7-sNrg9tJl6r9ujMXUBfiY9yMNq2oNuzV-ths36bkNJkqF4X5mvhXPdxxMFeNWdGSwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=J7lmiUmWdyW-RL5x2-i15L8phbIJ_P6cDdUFCvAcUnBEZMJfDyeUbRtnIZObQ_5VJrJKXL_DdKLhOj5xhDwQcQJsgyxkN8Taz8VyglmaByrHCvTiPbVCGNKrBjdMAhMDvWLPqrLtDSmHCAj09bMKNfQ_210MIafNy2N7ricDjKIs0Yd-sVGP3ryK58sOR900ve6Nq0VxE1pPlB-LnSG984qpVz47RjBBBJrlKCluKHtC_2cd-z_3cQl9e2Mya4tuVcfOi_8cTckus1mxgEh8LCouFyQB_yEBpWQ4SQUFInX9-MbnmVS9mahv3bQgQ3nG1dJtLpB3W7Nav7YF-JLP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_NxrDf3lqgi08vo8y-vLhn240A_uzfeiQYrm-_DqPBGXpK1Gf-smStOIYIsNGZhKuHwC0d7SPvqqIPuVtXbMlfDdNEVYrEKgpmvdJKw1jAs997HPCWzBwlYLblGOzYkSIiHevncRnVvP0sLaiHpuouyAAhC7quzcwB3MrcJuQNbJZCMpUkd0Nyv1I9wBuOnUzPBnfJVCpFIB_tz9LgUu1fos7ImgwiqCLH30MOkbe7zg6iCNlcT4IRqgZdyxzj9K-3itP1fg550uH-Ucq9r1nWZg61nt77YVNw66phZ_fWlWYpkmrCPp-kieaFtXxoSI8kKgGGqXuU2k4tKXGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVU-nDZkvVMadV7tl3LNLTuxH72pYU5CaNIsDpSVAfsYyWebLiP8fhqd727ZvWTwz2u-zDA4xF0zWoyg2IFWTcY0B4qovADQl-SCOxzhUPXuYiEZuEjk3eJYAsD9PDTpG3M5qKyjXFI9bXNVt4ANlpq7x-xWP6MmFRa6H57xCSejt71lZd-ngv7jIdaGFFXHrElikrNWv_-WkQRgIAECXSmEDWz7IhnnMYdfLXb1KMNczAgpHEXsWY4zZqlta8I1QjB249pzOjAAINpWiH_NpqYQobDKJaIWptEaxlPOURJOARy3H8YMisIQSTSeta5rg2zo38F7EHphnLi0wWWvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=BI7blTNc4DAgtiT-V1PeoCa66mb3TZZnCQ2LbbNat84x1Te_T7NX__vk6qdtiCmH8qPNY7oC_Q-lEhA3HyGuvJejhd1FFl2CuQC3JvDsXdsd_YKyXOW6jT5hnIXU5DPnSnuEnlli4wLlyE5QF9z2Ouum4IEqSVhu52JuXTrlf8lZb1sYYlg_aHXUZgbB4_aA-lh9ak10EZ2cfHum0IdWZlNTuz669wWlsihJ7wagQ0U0yzkn2rOVlfFKrGd_bUwRx6FDE99vY8IT54ZHvWK8Gh4_5S7o9650sEtbuXJ6y9A_QIPQea4c8ub_W5aXHGFyLR89X8FXMoDvSFwJWhU1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxIznt_LFKAV0-EcwG9bO6r8r90P5LdWuVtxz2_lED6myjGUz2mSGeae_dxe9AkIikMdPZ4cIB69BByP1JgPy6ySTekChqMUfHV0lEtHW9qEu-lVk41Vpph0AJhaSHmFCFOjX9JnTvyrDo68cew9FqDm5OhVBa25qUEbw8fQaTTXLF22bvz3I1gKhJwg6MFc0s1qsz6MhQm-L-ghm9oF2cpmwf9SRS4--RJC-vAYNYHYVCm0Di1pqow58X-0kMZA5QOkhYMzLPMYK6o7VaNF1L-SLuAE__XfG5qKrD65o79gQKuNe4MuTDbYGRlWv8C0d1KI2SyQXO3dSpOWzPf0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioAlXwoT1WjcSVkXHdC8oKgqvQxwI7L9M-XaqsyLeti0UKKxsC2U90KF-2U0dYwAt_gH6x9uf4gySU-d44vzxyonALETRk6reFC4u-Q5ozI9mk9-1uWkAhEj51sqxvGvAORSJvqJ7GF2HsCN8yjzr8Yq4NjxSAvnmlaKegNFvguvGic35-yIskyrxm518SyVtGV7dIgfZBbq8pRmAk9e7QPPtWuw0bj_VFvb2TvqppCobHn-VRWhCxzh6SIgFa7cKQNLV75AbmW_tRFdd4NuMvTXtDj0IYbz6QsDPFKx3TsFWpoR7RG3EBwsNou0EAiK1Y42bf2SUIhqFdl7_KTmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4lHm4YH5jA64S3H7J4h0oEVsAt6eCNQOUs4BUZtyiz5sdl28UeiAF1u_y1YibnyoeJ2z4LXx8cPpJaZL_nRF_6ezlc7dMqCS64-GWSdTF2gkxkHLetBPUTs47yiVTcZCTAT--uJS8PTGlQj0SCI7obamRDZB-REONosXSGXt79-lgXFSKBpocHFVW1LeOWSoD292vmrkbruUaq_6KBXMZR59cnAcb0L3boYXo4RL8Ab3If8qYlHdt2CuC77KZYo4NNzJ914hq63GptcVAS2hxR3mFBeSyr59PC8eDAhQrmFHVeLNJqqFocemYxZTDzTqfizQszAlcb_QLIDcxHYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bt6RisPe0084FSzbzPNYm5x-3E8k8YH13b7x6LVeBz1eLYHkkiOMPlFGCMR5wj5HB4rT1adFhG0MWjqFi1lI4R2fFQVJvFnQv4UqbPzec1jGraH5MCn5hT50hd8-tFOfR1O14WJnX6-YvtmokMS84URio4VD8ieVRVaLrxJiFhVX_xmp01xrRexP400cOi4F8sEu54DWYu6isBQVOw1zHJpoUAVQuko5_nnQ9aivyyOVxSBq5qWDPX9tVsGA5jbDpvM016AVsTw4mDfVP34Dj_CAiPLAvLu90_uhuQYJqOwMO8x448hMTrXQOt9H0AgQ9yqEY9d3j1cBjZ69UYaf2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=YJ_ahBNX0CB8E1_PujKGxpovK_AgRNwIwgZgBAteHBIEySDx8JWkFZ03GE6QRtia33BHZ1rfOJlXmGMidCv6TK8YN25NsKTiZ0fBTV40d9L260tcaeuWXuBS8OkCHjrZ1WiQ8ufPckN0YFCNB5jlOPHEHSBsJ-4QxyhtlX8lA7TPm_9ef04Po8AQuBzIKcsXRbO0B7j1lWacmPG1uEF3gLCEFMbTs_SaWMg_BIyPza_gqBvYcTXBDUQIVLy6RTZlvSNZpkipH8HWgwMhOcqbymfJFgZ1wJLwJ8bORmLeO3NttHVxf_5v6L5yURJSe1oXfg6LJg0gomjkOqYTixgfiw3TDl597dwARUi2NEgppPHYsl7gOFxEDrDw2_OFqkHTJSMAIp7o_s7YWK43s_jtz3lee_VUWLNipVv3kNpIK419xJ9ipLqH4ZvZ9O0z60gE-W2XYtrd37raN1Rabhd7LvojZwStTbCMHtxmmYVzSVCqE5FxcesJ8xsiLLABHqBrRk7qUl39LZ6A5fEO_RRC_9h66c-yj_tDZiEThqRy3jxUaTKdD94fHMuI78lLxuVUUxP2eztmVdqc_rhfi5PnnCzJIs6tFlnE6phtTl13lUIsxRAlMzhvnXjBOKHoi9gPtdfUB2YcT2IFuIkSAz5LxazdRkw8CfCSp3p7CP89E_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=YJ_ahBNX0CB8E1_PujKGxpovK_AgRNwIwgZgBAteHBIEySDx8JWkFZ03GE6QRtia33BHZ1rfOJlXmGMidCv6TK8YN25NsKTiZ0fBTV40d9L260tcaeuWXuBS8OkCHjrZ1WiQ8ufPckN0YFCNB5jlOPHEHSBsJ-4QxyhtlX8lA7TPm_9ef04Po8AQuBzIKcsXRbO0B7j1lWacmPG1uEF3gLCEFMbTs_SaWMg_BIyPza_gqBvYcTXBDUQIVLy6RTZlvSNZpkipH8HWgwMhOcqbymfJFgZ1wJLwJ8bORmLeO3NttHVxf_5v6L5yURJSe1oXfg6LJg0gomjkOqYTixgfiw3TDl597dwARUi2NEgppPHYsl7gOFxEDrDw2_OFqkHTJSMAIp7o_s7YWK43s_jtz3lee_VUWLNipVv3kNpIK419xJ9ipLqH4ZvZ9O0z60gE-W2XYtrd37raN1Rabhd7LvojZwStTbCMHtxmmYVzSVCqE5FxcesJ8xsiLLABHqBrRk7qUl39LZ6A5fEO_RRC_9h66c-yj_tDZiEThqRy3jxUaTKdD94fHMuI78lLxuVUUxP2eztmVdqc_rhfi5PnnCzJIs6tFlnE6phtTl13lUIsxRAlMzhvnXjBOKHoi9gPtdfUB2YcT2IFuIkSAz5LxazdRkw8CfCSp3p7CP89E_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMxuUvIJjwzhbyARG6t_toqfdY7r1GRsUnna6PbO-edfS7NUYnY8xgF5-oEMPl23I9xcXzFbfB6YDMusytLhBBHeCI0qlxoMamrjf0uxWbNuGRL1vGMDeuAeuTteKntkg126bk3C818N4mVqHuuY3vm6bcRO_IVkYtD5tdyxMEp1FI6jMVUGX6-cjWsfNCc1d0Y1FJNLl11MlY4ichaSN8rqV1_bz7X74AXuDhdr34oextvgiXxIeHMy39kpQabL4WZCNjQq46QB4K5RB-hR3eVFpJlyZnsbUs5THG6ItCgw068nuGyfq6DAHoXLjFjj_ecpIMZA2e70nsC8rVuk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV08K2YuHTY1HSnMe-4UMF1uX7Mr7h_FhMo_ujD42LRGtq_YVcXHvtNw-bw79dlrAHphuSGGshY725B8E9j5hKSc9ivrH9cZmyAhp826YyiGeVOLjaXRbrzQ8DJyimBdpUyDTpjk8mGspkIpgYqYBMo2BMzcoGIrvJ8ihydhE4XQRjgkeH6ro3BLlI6w1nvzOxarfIEjyzlN03rhORvRfaH7dIlocmFdveoU4fVL8YImf29cQ-D2QGML0WIG3d62GoBtZcODk71utpcJlpxWBs7NYhBMK8PGVXPo28Us_OWMa08pj9OATsMEQugS6SjFSU5aG4xsmvOb1X5s4AylOV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV08K2YuHTY1HSnMe-4UMF1uX7Mr7h_FhMo_ujD42LRGtq_YVcXHvtNw-bw79dlrAHphuSGGshY725B8E9j5hKSc9ivrH9cZmyAhp826YyiGeVOLjaXRbrzQ8DJyimBdpUyDTpjk8mGspkIpgYqYBMo2BMzcoGIrvJ8ihydhE4XQRjgkeH6ro3BLlI6w1nvzOxarfIEjyzlN03rhORvRfaH7dIlocmFdveoU4fVL8YImf29cQ-D2QGML0WIG3d62GoBtZcODk71utpcJlpxWBs7NYhBMK8PGVXPo28Us_OWMa08pj9OATsMEQugS6SjFSU5aG4xsmvOb1X5s4AylOV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=TSSTYb178wN9q0OctYxuvWcgXHHsCVI3djdq2eWO5P5IeA3V3rzvEPHN5wTe9xOA3dIDQmLEYb8qNcRkHB0vncpPVV-oZYxpxgjtFSmcN8yoLy_4Q1IJDX6y_RuEWJHoeQ1hkvDwEo453Mgy86963cXltkXCAdlXhhFO2D_mDkm-LwhabX78tkCJU2UIpizhSFLTUcwYjHHTUBexnTwAQQlbJH-EbAvWm5rh8DT87kXaT4PHNwkzDCeV9HeXtnNrZUHUqVD-k5vD8yel_uKette4kkg-SE1a173Hw7ge871zphD0VOVHgOrb9XYLeiJOuJzERwb-x2LZOQVHvdHL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKKbjsXrnHBnQCpkWdd7wMgo83FgtoerIGthZ6DQ-_AoKXExAA8WDxOms2IXBZBALS6lSE9B_wn2yenWKuPZWM4-o_QZLIGOd_R9y6rOlg-WEU134In5T-Fs-Rw-vtjuZItnP15yEK8aPLOvtu4MLPLh8jkx6KEVp7wQpw73d4VdmskT9JxHgp28TbnweMe3iSLlVh_A9OX-lI104NrZofJnscLr0c84pNRoKMXE1wTYmp_2tkrAw18EO_MWFVcSp_gV6nMtYdbrb9yexqwb0f5kkscbqN4p6NTYo1rvsi9ihe46FtXzkHr_4B55kah4XgjwV3SPOZzl64MrCq00cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=e7a63FPFLN1ZbavgEn6II_zPlknUaMiqq0BXIUY1uYEUeXj9FFLs81JXt5NQojx6eMxEeA-H9RA1i2t2987cKq9PUpqf_IoWEb9bj18jam9J1RX33tbX37jbsIPDsFQz3yUZOd5YMF6TYe3X8yd65eq7EoLJ6syXVpa-5udu0_YF4U0IbBLhXY9ImWL7-rq3zT-rXl3FLz_Z9MzMAeDCLmw4qiMov8gzeHbOPFM8mIObcY8iHrxLzfhpSGQvekMpHhZ-j65kRWWKNWTMtFbdLwR4vo-ltrYAp0HkEP0ceLwctqQTG4Tc-BePYmeBPOWcWoGETmSMDME3Hqinm0sF5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=e7a63FPFLN1ZbavgEn6II_zPlknUaMiqq0BXIUY1uYEUeXj9FFLs81JXt5NQojx6eMxEeA-H9RA1i2t2987cKq9PUpqf_IoWEb9bj18jam9J1RX33tbX37jbsIPDsFQz3yUZOd5YMF6TYe3X8yd65eq7EoLJ6syXVpa-5udu0_YF4U0IbBLhXY9ImWL7-rq3zT-rXl3FLz_Z9MzMAeDCLmw4qiMov8gzeHbOPFM8mIObcY8iHrxLzfhpSGQvekMpHhZ-j65kRWWKNWTMtFbdLwR4vo-ltrYAp0HkEP0ceLwctqQTG4Tc-BePYmeBPOWcWoGETmSMDME3Hqinm0sF5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=Rb8qB6Ee81NP5yrk8RTwkJPsww9yvJZFflWYyZ4USLTCAuIu9T5KjJ4wZuQqjl--Wpr1YWy3BHkH6lqQNO0N4AyRN698tFoquPQKAUR4dRKoNm7kyBqQcEHgqhWm0kcN52LWfiJPwzmKPPPiU39OxeuMKAUpRi46nJw3iGFtRAhZvTOutu_tPobU9KWqKIjMpTU36u1SHXmM7TjH29GTXtIaDRPz_btOTy5pdpVlm38J4mVRqh0JRBw0CnsjbK_lFVtbyVghqSX-1FiA5qe_a17VpWHaDKqEbjZ5HvdctrS4p0O6rPQvRkqbu8ADi7kBUgNdOnKXhcGmoDbEzOoh8K-bbRVMDz6esxcA4MEt05fN21SozCPAXzQjeJAj2QKZ7dVcWqMO9xL1eKwGW6Bi3p8wJ5Pe4Gh3p-iS0SyqS_Lwj9gW21xQchiewqTV8GnhelImCqJZ2mVKPdw250GNvLN8N_tr6vbdu9JFgsQLadWkWujcONO8MoxMDCzZXGjGiRMvb2RfXsivH6Obciex3X2gI2JGl_MmUQZvFN-_RcGi6-CD32Yt7csubIcNKYezal1Gv62scgT_xjDWVT0aXJnVazQc5hHX5G46_SP-Grfakh7bV6BmyEKVwhFRDfyzaKWMOdACdkaBXMVNkFGsUo0N7ne3a24WtRdggHnSoQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=Rb8qB6Ee81NP5yrk8RTwkJPsww9yvJZFflWYyZ4USLTCAuIu9T5KjJ4wZuQqjl--Wpr1YWy3BHkH6lqQNO0N4AyRN698tFoquPQKAUR4dRKoNm7kyBqQcEHgqhWm0kcN52LWfiJPwzmKPPPiU39OxeuMKAUpRi46nJw3iGFtRAhZvTOutu_tPobU9KWqKIjMpTU36u1SHXmM7TjH29GTXtIaDRPz_btOTy5pdpVlm38J4mVRqh0JRBw0CnsjbK_lFVtbyVghqSX-1FiA5qe_a17VpWHaDKqEbjZ5HvdctrS4p0O6rPQvRkqbu8ADi7kBUgNdOnKXhcGmoDbEzOoh8K-bbRVMDz6esxcA4MEt05fN21SozCPAXzQjeJAj2QKZ7dVcWqMO9xL1eKwGW6Bi3p8wJ5Pe4Gh3p-iS0SyqS_Lwj9gW21xQchiewqTV8GnhelImCqJZ2mVKPdw250GNvLN8N_tr6vbdu9JFgsQLadWkWujcONO8MoxMDCzZXGjGiRMvb2RfXsivH6Obciex3X2gI2JGl_MmUQZvFN-_RcGi6-CD32Yt7csubIcNKYezal1Gv62scgT_xjDWVT0aXJnVazQc5hHX5G46_SP-Grfakh7bV6BmyEKVwhFRDfyzaKWMOdACdkaBXMVNkFGsUo0N7ne3a24WtRdggHnSoQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIBluMnrFWSmeHpVw2nrk9Uw4fFKcvrlTg9BpIpi12xKCxT0fceTg__hGbqeHMhL-x8iOZkOaXJd0iogb1e32_g3nqTX-nRHlss_7DwChNZ_W3JfLcHUHVCN-IHnXQ2z6zV3SdMeVd3sREO2PAoJMfx4jL9Xi_JIOfCjtd7MhcVYtnlgxRkRjDM0y0EYD1n5HkxcUFhbnIOUy_SwEkuIma7dRDLJrIWpXCuxy8vaRxChKIQSi15WXr2ts0YS0iJfiS0i458i6XrV4Iz_-l-1QTJNpK_eNuOT7C7qVCP28u7fUuaJ6k4-4NU3EdGG8qL09m51UpdhHh3JUxQ-dAqvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQbev4N1lzKVkzWqsHngz0jMiUJoYDnSjxSt2YUY9eby48grp0Nm-xHhZl_qW51fxLtx-dK6Wu1IUypbRC5Pq2f21u-OOSIIDjnfgNLS25iqJ-LEGOsFcIJLAMJzxeC8FtIgSzwUXLQDE-ikXOo4KwQ1i0iy-BrtSudIwKRcmfvks1sVhLWLQtisalrOGyG8_efRM7a5ya52o4FJacdbjaYWzsDQcE2nLQRoXsPIBy-qWki81sOz48FKdF1zjHh8_JD61UeCw3ZPMs4fUlnXUtJv2vZCGjRlZnk5UzMiMSLxO12EN_2ZtKh1E_WP1uQZWwrI2OQbWAIchTZbv6rTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6o-PD_1uI8vhPj26coZNxP-cztslB2rDS--bFa5Sg5-x4pOCWP9jPdrH8roGo2ygfKhtX7xe2PjBsiB89jUXmzXxC2GruQKYtE9GsoDXY_dxCAQIjO1KF8N7bUG6nGvIqAoJkXsq_0J0wxqqNCWNCfrYhSgXt9VqK_CBcLD0uSIAcNzFY-RKdH0y0NAbY02scuKqf2mO-nZzU_nm6npI8bL48536XbmBojO8fewVa4T9knERWpQTR0tMoeaLOy-XQYazk2tIyFvjqMtoLyS1yMDBahU0DD10ITDQY_jLitR1ereqSYe0wE_YWH65BS-iBeRJ7-IO3CLzEjJhqz0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECZV7PJxhCBoZRHARE7c7g7tGdXQQ5n-6FDUwKBXKcvQjRlTHETxX9ebHkev4Hfray2eE3-C46BxqohOinVOQ4RzHvq2R7-w1ul7PO13ql3LLEI0rnMed9NCVnrpVPHhx3OfLx0HpWP9v_ntIrqSXnA3csmyQuhNMIdrit50HHwTFH5lC746HoibyMvmf6hLgLpryADTJcjeXqdBVD5nCVpwEBCNdImlSIQg-WZ70M7GY0ZhsIm46KhuPjqewAGxZJcFSTFFdlw4v0HSIQaLGJK1WPVYscrqyoAyaAzTw6eI214Y2nN98nfNqAiFEZ9VKr68G20AHgTYTxPvqkPksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRMfHj7vwyJcPKRW4UaVXNoJLNfL-LmQhR2HoQRbC2XXvK7TkEMGDvvqbuSq_sdi2L0SOjDVBqvGgyTrx8-as8K9qrUQPIeKiMQ4vih3Be_5YOmbNRY42vU9QfhxcqQ7mwgghoob_C6Ug279chOuNOICVIxKUOmOvBxUQVNmZXFdfQ4AoKeAg03D_TSWxyKOeWzRHuqtt2X8GDD31W7m29o2CSQZ8RXtXlqQw5HBkExSC5ARrGTQnAn3Us5Y-ZTW0RYd5MKSil_1L1xz7GPm_SiwReKYq8kvnNO3Sk6MxryD6rND79cj1RUyfNaLcrMljJfociDR9kcC1zfhVG-frw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqryzEcoGXjKn_ddZmlHyR5Gx6sWqPV1_v2XGz7pnS2x6T5J41RLNSSNQEUn_ZPIr6HpvSFepaoH1KRwN7w_Fp3Dy9D6lLWctsxDLiHkT8WATCgXHWT7w-GVPpWsM8hnyGBl41jGaBGeLImG2T782ShVRT3Wj5RSAn5HxtelBqw1Q_UbYo0iIflesSif9VHIuQKcy6xuOyABVPlnZp6JsrKB2_g9yrbtuf1Z8YncKv89vrr9_cv6vMd0tTGFQnUAJelkW2kL-jSZ4pOsUAcyUrAY6UFWGa1WCyueKpa1mtjs9nVQR5XYQclCRMtPLhzW8WkJ9r7kwEdDPaY5ROO97A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3jtoqR523mxfFphUWax0YH-yEayJyMuyDXxqPpc9R_B5OevKpJPTmvRwlgJhohtnI0Ui4G9ECZSYQYXKdkUPyOE6ZTsmV0h8iE9rEZoRK6sRiiFGgVNGuwEpX6_QUZ1xY-EYLGj--B_vlMr9yIRStpQGZo25pPmV7_g9GV7ziuqEa5RYewk2gzeaC-S8UvsLQ7RwYCJOIpHrVixajJ7_3W9O6jrJPSKt3RaFlBCFNB1ReC8IKWl8kkjAFwbpO3mMY7dbbESSqEWngNx4Ha7LHU7fCJDxotSCgy5VOqaeMc77a2ufTJ4ygz53XlkzOhCO7xR3hjlCj6MBINNtNHaJmLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3jtoqR523mxfFphUWax0YH-yEayJyMuyDXxqPpc9R_B5OevKpJPTmvRwlgJhohtnI0Ui4G9ECZSYQYXKdkUPyOE6ZTsmV0h8iE9rEZoRK6sRiiFGgVNGuwEpX6_QUZ1xY-EYLGj--B_vlMr9yIRStpQGZo25pPmV7_g9GV7ziuqEa5RYewk2gzeaC-S8UvsLQ7RwYCJOIpHrVixajJ7_3W9O6jrJPSKt3RaFlBCFNB1ReC8IKWl8kkjAFwbpO3mMY7dbbESSqEWngNx4Ha7LHU7fCJDxotSCgy5VOqaeMc77a2ufTJ4ygz53XlkzOhCO7xR3hjlCj6MBINNtNHaJmLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56ppNcX7VhP1vR8pi0vOotQjj9MjZlMAQsVqmxqS6wsiZ2NJIDTBMxHspeL32Q-Ue7M4uR01AkLXScOOislW5_Vg2G0zA8C0iagK11eSxADAmYiGhKFh0l7Y7c3rgJhyuy-28ThRig8oT5WJgOl0Nm4YJXfDBqm2meNtTrmjcJbCVR7t96Mm3NZUzUSVUIqpClCq4l1ltrAz-9TbAi6KXGMCadjFjCxyIEx4RKMPyIeuIye5ptEd-lHJoIDOKKGzhXDAlYadNS8jt-k7BTh2rLTTQ8VR-SXDR1m4AA98fAxFKh5HBONhPIZcas7Msxc1O7k9G6-A0-LnEBcU8NTKTCb30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56ppNcX7VhP1vR8pi0vOotQjj9MjZlMAQsVqmxqS6wsiZ2NJIDTBMxHspeL32Q-Ue7M4uR01AkLXScOOislW5_Vg2G0zA8C0iagK11eSxADAmYiGhKFh0l7Y7c3rgJhyuy-28ThRig8oT5WJgOl0Nm4YJXfDBqm2meNtTrmjcJbCVR7t96Mm3NZUzUSVUIqpClCq4l1ltrAz-9TbAi6KXGMCadjFjCxyIEx4RKMPyIeuIye5ptEd-lHJoIDOKKGzhXDAlYadNS8jt-k7BTh2rLTTQ8VR-SXDR1m4AA98fAxFKh5HBONhPIZcas7Msxc1O7k9G6-A0-LnEBcU8NTKTCb30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=sGcxk129J-qYW0fogajx9n2MvRAmzJYnCo5tHsCaOMoIdcp9STLcXDXJadRGA2cEqJKh8x5gyalgPOsMUifxIpdUqBXRdWNFkbH5aKAegqfvZAxrkrjkY41ymipaSwLY2nZXNWrj4jdQcAVEpSN78sPkB769oYxJt2ClIqm0fyfamptCSNwzjrmQRlHbWyJk3zUoxR6Pz8Gm5oSi0ywdqJ6KQJR16yzECbOqEAKQdVa8b_B-hWlIMvux1HB5uM4PLpfbXnVWHtkhwSn7p1eE11XSXxGoGErRO3aq2COFQewr2ieQAy5m40nbnqr1zulul3Uv3dkIfQOipJXpZEl-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=sGcxk129J-qYW0fogajx9n2MvRAmzJYnCo5tHsCaOMoIdcp9STLcXDXJadRGA2cEqJKh8x5gyalgPOsMUifxIpdUqBXRdWNFkbH5aKAegqfvZAxrkrjkY41ymipaSwLY2nZXNWrj4jdQcAVEpSN78sPkB769oYxJt2ClIqm0fyfamptCSNwzjrmQRlHbWyJk3zUoxR6Pz8Gm5oSi0ywdqJ6KQJR16yzECbOqEAKQdVa8b_B-hWlIMvux1HB5uM4PLpfbXnVWHtkhwSn7p1eE11XSXxGoGErRO3aq2COFQewr2ieQAy5m40nbnqr1zulul3Uv3dkIfQOipJXpZEl-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=iwlYkoHpBSgQpUbMW2vRx7pwa7ISOMA_zFtPF3aolx6oSGDp2Dp4JHWoVlfgbP91q0JaGtr2AKaPnhwc-PiPy_Ea-rMYcNY1SVdgbh5iTbIi5H7-LbzPk5aY0ep1oXglLggM8p7jJZhf3EMk2Yxu7Hxg4OYd6on7LL_Pi4vG2UCIxmvPE-aIRAHBO2X2oLoXw583XBm_Yefqu5IhVfF9wVQr1sXm-HF9brvcOvLcdThBPTBq-7-7zCOWXuxsmcT3wMBGuvFzSWyc5UWeFegZlPIEipZ4W1A_9-MYfVKVv60WRDnQK4EiOefcZlxe8qWoB2_ubQY9v2TpBil_a5pgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=iwlYkoHpBSgQpUbMW2vRx7pwa7ISOMA_zFtPF3aolx6oSGDp2Dp4JHWoVlfgbP91q0JaGtr2AKaPnhwc-PiPy_Ea-rMYcNY1SVdgbh5iTbIi5H7-LbzPk5aY0ep1oXglLggM8p7jJZhf3EMk2Yxu7Hxg4OYd6on7LL_Pi4vG2UCIxmvPE-aIRAHBO2X2oLoXw583XBm_Yefqu5IhVfF9wVQr1sXm-HF9brvcOvLcdThBPTBq-7-7zCOWXuxsmcT3wMBGuvFzSWyc5UWeFegZlPIEipZ4W1A_9-MYfVKVv60WRDnQK4EiOefcZlxe8qWoB2_ubQY9v2TpBil_a5pgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=ujBdVxYX_U_FreLob9qU5T1Xigig_13tI4qknj2Ws5QK2eqkz6dzjCTDTOgaAbtVKXPes3Flq6drVRxkCrIML6XALIOXwRFdIEdhNaiReGYjAfqRn9yK4xTmBGOX54dJng72TgSzRrxEFwYGRih21PzL2hK5EDsZMhoDo0FCWw10FYKSYNVn3Tekfe7lFh5ESvtHTnPkgI8GxXhFXgI8Lli1eBf_VmGJgQ0Vz247lW5H_JWiJvEuaQ7Z1K3dUimBbRdut5I_2zmw1bDhjCH8kBeHD7LdsVxiykfEdN8BUtP7MugnM0wyC4yu4UyyE-d47mskBN2qSWerHMWYJTtpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=ujBdVxYX_U_FreLob9qU5T1Xigig_13tI4qknj2Ws5QK2eqkz6dzjCTDTOgaAbtVKXPes3Flq6drVRxkCrIML6XALIOXwRFdIEdhNaiReGYjAfqRn9yK4xTmBGOX54dJng72TgSzRrxEFwYGRih21PzL2hK5EDsZMhoDo0FCWw10FYKSYNVn3Tekfe7lFh5ESvtHTnPkgI8GxXhFXgI8Lli1eBf_VmGJgQ0Vz247lW5H_JWiJvEuaQ7Z1K3dUimBbRdut5I_2zmw1bDhjCH8kBeHD7LdsVxiykfEdN8BUtP7MugnM0wyC4yu4UyyE-d47mskBN2qSWerHMWYJTtpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=NKRiSbGp7Mkde0qO6cMqZBW2wkevP74_gOeekfJKLCjbLYN0hpat94W8y73KTK0_xMH3NMcYslycyLpLz-NYfcZMhLzJ6Kr5sXPz0ZcTWFieWqBOntHaPsBrCueZq6NHX1tcpYtep0x_59Kkl3gfqkaSM2Tom_L42cy5LPlx8mQ6U8h5rk9BF7X-Vbl9nlv39wVs7xzH7iKvLnHcEzG8R6GbH6iT12caV7bXRPQYUdeAwOkTncugPRi3_V8Bk5Ds4cqOwPBtm6TR_3O2FDo-22YquyCVU7Fgq-AgqhlEyAdDmpvKxgzbKXg9X0TzGFzxt-7oG-dl7ukLc8xiFKOVlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=NKRiSbGp7Mkde0qO6cMqZBW2wkevP74_gOeekfJKLCjbLYN0hpat94W8y73KTK0_xMH3NMcYslycyLpLz-NYfcZMhLzJ6Kr5sXPz0ZcTWFieWqBOntHaPsBrCueZq6NHX1tcpYtep0x_59Kkl3gfqkaSM2Tom_L42cy5LPlx8mQ6U8h5rk9BF7X-Vbl9nlv39wVs7xzH7iKvLnHcEzG8R6GbH6iT12caV7bXRPQYUdeAwOkTncugPRi3_V8Bk5Ds4cqOwPBtm6TR_3O2FDo-22YquyCVU7Fgq-AgqhlEyAdDmpvKxgzbKXg9X0TzGFzxt-7oG-dl7ukLc8xiFKOVlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlT_KiP2MNFgZM96uAjYpghdHn6iWm8HSOaNeMOSDBer3PIENEpAkAngBXpR7xjaYhh7fKyg7h0D8IpLWy_NaQof596Xo3woJEWRbhjlvfJYmOMCVXxE-WtJWa2_QI2TK8RxedGhryaJghxr7qaMnGXGgvZX3aUayMRo6mH-EBaao-QhA7f_r_iJQYwcn_L3aDkT3h5Gx_jF4IyJpBJQC2NDU2NfdsRBBBjiU4UOa5TfRRTg9yxyTPyHkFvwXvZQS5zyHIn3mL2yUMPZWopR-iporTEEIlO7Pbj2uIczYn31nGiuQ96Rq9Dt7WsSfziVnv4IoS9tYVsKY222jM-1gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2cKLCFgqUvrvecVDqag84uClFTpKtm4PwkOv28rwi6FRhgi34eBGp5mkNEGf4_gklSs8squCy1Q7bdOh6pGhH6lFU48yIYoTuVMkPLGorSfEnP56YeEcilg5A5dNvjGas9oHTiAunBWQYyCGmCC_QjQ4fzSD9eClco8U-ILqMBsk2oTsDOK54_a2LKrKTqPzKE_kY-aZPQ83KW0xqqnOl-tuwL04p3fIYjOMeKNUE4234ryL94dNeFZQrwJKPlven3VpBvL3CfofevLpUh3nxhJTBT_ZUoF6yGoYLQxBuvdVZ-BgKUsL7XoBP7zHL_UxqXZejTg0L9vt5fNvOz1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=LOPHTP14qva9_PDEzNfM9fTCGcC9xaQVwd2wOvtbUU9WjsyvAoZ6EwjNs2xSvzjSAy0FAFdWVMbzJMapQlStZdfE8V-_Sx_XjmDQO-Ls1wZafRsxZf9Y9-Jnu-EqcrhXQrMccLhA1ZcaTOFGY-xMRafPBA1U4_-x6aHRwzmSzY4Fez4wMxKAien4sqhSikQvZEx67xm8DoafZxzlc2dyJtJsYLHdVrELY_jGDukNK-G0lTXCykvoA9-l5_tkeTa99sdYgXTIGZXt6B0NKzqJCv1vheN3kMTm7LCrd4_XCzP3q3FRvaxQm89vh1a3g8ZSF35crQdaaWOAJAnCPL6kGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=LOPHTP14qva9_PDEzNfM9fTCGcC9xaQVwd2wOvtbUU9WjsyvAoZ6EwjNs2xSvzjSAy0FAFdWVMbzJMapQlStZdfE8V-_Sx_XjmDQO-Ls1wZafRsxZf9Y9-Jnu-EqcrhXQrMccLhA1ZcaTOFGY-xMRafPBA1U4_-x6aHRwzmSzY4Fez4wMxKAien4sqhSikQvZEx67xm8DoafZxzlc2dyJtJsYLHdVrELY_jGDukNK-G0lTXCykvoA9-l5_tkeTa99sdYgXTIGZXt6B0NKzqJCv1vheN3kMTm7LCrd4_XCzP3q3FRvaxQm89vh1a3g8ZSF35crQdaaWOAJAnCPL6kGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbJvfOyT8dHDt-Devm5b7OleSr1AZTGVvFQyo2Co7BGvY5pXOB8FC7G-FRVtL9FQdB_x7tJ5GN3OZ6XZzfzQq1qDNIOWgbzl5bqdDA6iQ4jpnPl335zW-iQpm0nbrO0OnArRDoWVDtl-ERceB2MNxVQhMZG6rFfkUkQ3Nn1TB_qXGkhvcDTB-VwWzI6aRghf0pGojl8414_vnJdbOaqCxr57kZ5jKmEAwijGMMM9XFKqs_sIT1xXuGfmshMdgf7Pxl0BvcCq-mYFDHNnIxSugq8SDj5QMBWbxjghUwImuDNDECCEhMm9cuzMz6EO6X16rfca_-K--5LKD-HYj69fDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=SQlhZceqz46PWm2P5klKffTIoJjNUQuuObGKEASiaJY8aATa42XETbelhj10pqrjU6emB_FkCyO_28tPqs9eO1nAZzpeIcmz9hg3zLAtmsA5xh0mRRx2oT7QJF-gAttS64qVaEMJrM8o-Vw9o8DXtRjPX2rbskHNzhBoxcyj9oJC7bMBt30zHKMf2wa3sj8Ckeyqwv76c-3cbRS0f2tuWcs61tCU7lTt04vIYR6CgeQaa4BjKqcEB5FEzxczrvi0ECWRXo3QfcQ9ruyhxKAC2XiyuoJKqH2b8jlQ0dqZRcED4jUgaagUTBaiwOI8WQAiIyjs1xM23d65rOo1_EJl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=SQlhZceqz46PWm2P5klKffTIoJjNUQuuObGKEASiaJY8aATa42XETbelhj10pqrjU6emB_FkCyO_28tPqs9eO1nAZzpeIcmz9hg3zLAtmsA5xh0mRRx2oT7QJF-gAttS64qVaEMJrM8o-Vw9o8DXtRjPX2rbskHNzhBoxcyj9oJC7bMBt30zHKMf2wa3sj8Ckeyqwv76c-3cbRS0f2tuWcs61tCU7lTt04vIYR6CgeQaa4BjKqcEB5FEzxczrvi0ECWRXo3QfcQ9ruyhxKAC2XiyuoJKqH2b8jlQ0dqZRcED4jUgaagUTBaiwOI8WQAiIyjs1xM23d65rOo1_EJl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWYaO_i42CbmuS3uqi0COfaoFiaC2ewnh0_OLwsKJ11RWwlFpxYXESrw3xJxnY0oY4pPMvk0XLz31me2ZU5Rl5XO-qkvUWSlLtl3LGJZzOa5KBarPZsYKPhzCenOsxMP28HZ49R7f2Dv6OA3POmwAoh1gyce8_X_JIry57tB0rV8CuREswPtsGuE2sgeqwd4kHnaXNmFX3FdW-RlhOgsGI6b0cI7o7XeTimmN5W8ql4_QRtYkbdHw3-pQG-ZAJObghT_UQywuYfvvAEcwX23KgkJcrWYH1hdm3oF6oF7NA429LsYLPvA9ch89W1mnzePTmV1m1FQK401bRo5wADdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOKLpcYXIDZd-6va_CEjg0LrIPQ6pplparcs98MfpuPogvPTD2Yu305zPW0-PaL8OUE8HRxG3d3Zd8jCnWSWRjoX29I4WBi-_Cisj1TEPi7elL6NvUXrUeC1zZrqAKvQ0cVUVaFRQbkoHCqSwCr0XsIwcOMsmIp1fl9jU-TOeBlMREHiWyxMBqzj9ZIvPVFyhH_lxTGNhlhDTMtI3VD_gqTdUpArgP5Uu8mdgllKF0Kla4Uxqdawo8qCQj_2dqKpc66F-1s9aJwn2_MACeFg3MnuvvvzpX1e8TJEm62QAhm-uyOjEzCAzNiCn_MHb40dc08hOJPIEJI4HMOxl859CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoFwA8jTBA3S6qaVFttFq1cS-sucp62V8T3Ug9lSPSf2bks5Y6OfXLMag7k1SA1HYHrByLXmoD2ApYYYLj98eYJ8zchTRBGxBKGTMmOPH5vCp7WTR7M10YDPnTr2oDL2I9usrnZwY2FNEEXzWyEPYZ7gwrJqQzh_eol3jfxiDPG8p34tWmILhFM40qhieCktzQU6CK_EMrVyVDNiU0TwSwvadTqIPNccBwqxaV4OS5JYn-_A2565DEOkLEKFJyL0h1HULM8PkRjIeKLF3Ik9uDGMHBfbi4AFsKDho728WxO7GkFefrFLhcfpoijoW33iZL0I-T3d3sGsILYcnBu61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH5NmlyFPfiNMAdG6eMwtzceOQ9cfFmSuO0XoY4H39_gcaa-Xnqe0GwN52VObpZHzwplWQaJAYTMK1thpRkNVE-jQ3PFv9CmS1CtsXzUwN7f4LhIUEcFXX1ykKlBXJBfI-pMazh_pls7KABvwqrWM58mV6gDnD3uRd7ztY5BrJbRzdBJnIcnQr5xrpIWPa-ocRdIO9h3jg5R_Am4ohRgcNr8PRrrFTJSZTTGtXGi3jzldBr_B-yjFVR8kPUu9kbmnPw1ATuhPvTmtgaElqDEXgCYuEi3U2AmzBdQDKZ38oCx-s921nhZx-Po5YBrK5hULxtI0U3awtRejbAjA8Ho8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GAP752RoIePWjVLRFCg7rvKOAGQlGsZ9Gl-PH_P5wjTOX03Nh6gZ-3QonKCLQ0OpgaVi1jnDqI1kMZZZdkIIBYGHUMOy11aflYunq3U_2wGstYD7l-O3TLc_yjwxeGN64kLjjgC3sUofs6ZBHMXcI2bdLNK20_2fhJ-SwjRNP_hCj0KWWp5jhFEZw_xoMOHTQevResbZvW72K8YZXNlv0Xi4aWEWAyJpXU64J-Q2NA99DNfy_rzXTY4ucgGnlAXh5xMDeF_lCIXKgDtQbmsXsfMYDWxm29iBkNfOk8n5rIwjcENkZOzDuNrerpztR8Tdk1GxXSR-rsRo4FHQXDVJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tkvli3JrS-AHspMBYxprpxKCvNxmu9CJZLpoDVddVNw6nmmuJ2ErdvacsQDwMYCCe0MRLBCNbAS28YEIR62ebHyzlWoNsrxziBUgFmwykYTxj04XU36SEAc0MfMO2573hkyejFj4vA9Q5UZeD6Y4TRM8DtLfmmBgdjD8xYnYVReTkgMf6GL_RVzxFYWGJA1qj6xcCxc8mKwaS6iCLPIe3oEq59fwjwJhifEQy_YVhpf-IxncHmoSLKpWW2wKkhHteStTH07ctLFcvk27jDyr0hzy-JVifNVZ6tYCc2OrgDggwmkBbj9cDVPOfS8phW4HDYdCzSVypXPEi2Ov5aWIdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm2Emc7jd0BZxDHuw4oYfiYwjfjvB3RV_qqiO-t9M6jaQPlznH4k4c9qP3WuQ_Vn3DRSxwaHnk5k7AsUMNuMleWOz2s0uFM4dMMJHbvGy38BndZANiGNBubQ6iKnkACrEqS6nRzvOTLQ0eJIOk3vj60ZCFO45Ebc1kDUvdMB3tiAtkrpsnm7PBbsSxqwrveZcvgMQd8OPY2uowaA85oCGQgUjjFT649kUhZ5ugwGReNZL-HCgNwRzvpczQ2s3MJgQaistiLhV8Ijbtlpm9B1RSm1Y7eSkr5E5VFAVegHeG3WnQHNzxKcwrV2cpm-bKxk4ZkhaY5CgsZDwnoGe9Ixnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyQLrfuxSr4yzlIBZRU46Lw9K-HPkaddrtliTKX_6LkHPgDHKaxIEhoFFXtKQZ6PONfWjeMzQs3VuFRuyoSQybifsUzcFrWARG7a02I2etKTgcshGq8fwwlno6ps1C34lSSmDkp0MEFS_IbHBZ4pwYqTKd8GCcDHuAnqYRNmI04Ja04SKLzy-dlZbFNYz5F8Jc1C5hY0HTGh53b4qOz02ZqDByGFXVP7WL51U1YGr_fWmCaCwwxp4c-I2XUfsLIy2uTDOWMwknPwoLF9vvf2qwLUSuZBDoNzBG466FJVzkxI1UC3i--CJuwX0nSYJnNbMFO0UgOBwiwWeqRfh1SGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvYzIBZBNYTrEwkGthQKDCUb1cPSBox_XAe8nG4i73jtVQk-tM9ZItH955wCjAkybSLEPkS3LD9r3SUphAjlkznJvZYhCkoF5uKTHbxudFTdL1mcuOiVOhiLiY2WPmOo_6rz-pHtfyn_CoVQG54Kw15KMnn4GyylYA_kM7j65K1gfeCldNnBo6M7zdgXAlziqSo5fyny8tE8UkE2rhp0KovuWT9Tk8CNLanhIxG97m1OGRmZrF9BhwWqi4cTVqJSM3swWPSGzXdOXKkwode2AIm-pCGjhDnfPQp6mivu1SPzChNZnGfRDeR84zgJfSFJ17TdYXcCy4iwT9qV9wDkLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/narGhoxbHn0utH9hpfJGKITtfwc3t6XoRKID-wbVTFDza1DvSWFLK96y2NITH9fJIRXZU3uCjoZyTb-jDvQlp7igmJMkwSUmSR9VaGpTO8Wq4MF2RlT2S3H8EVRYbvxuWdTsxovbzZ0RVJvSrFsyzSIK4aCKlVxKkfthRbHJe0Syx8CfbTGwvbCKb5npi1vM-a967cKT98saxLhJ7vMr6BPsFEs-j1aVODIqKYNvTeNxmTbJVpTCjQu8LAeK8avsIgQjK2VduVKcIQ7rGgYL2ERJ-U7L6_9yG6Q2UFIANms54aq7ZusWODNY1v8ra5ma-76NMm2iGldlIuLD-HMtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHdTJeOAUrhVuy6Lzot94ZQpZJKoB85xKw9vwooCgpVfRf2lkrsvCG8PZVbLFvdysmE3bwPXRkH2meLuaDMPsWDTjlpsQnX_tFKU4V_TmM8eIgLZBbFVwTOnoNy4zn6gnCLogdFai-HK7rf7I2JmWoQjdXfwjgOqkRwrDQryTgnDoXUjxEpTDFAMU-7PxUBq6Pk6NrdAevs-pYe1MakDM1GGPNxYfWoMtMUMwPPDYXv6mSM2WeitJyOFIawox47cmO68fPN_E45ZzKGktcSBofWvXcMNh9-ZRE4Kmkx5hbsKOrJYIv9RH06RLeCGZRayOkAaO_GbXd2sGM2XSEb6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XfCAMfd3cEsjriWfDJrPq_KKh-1jEEaP92q6tRdL1Ovvf3XnwdUebPdh803eu02_yYCAPLpB2t9XQNSZNebzfoqt6FFwWjWcfV6QYsqBD73w1Y9OVDCcoLdSfEDX3OTik62Yg2kGFSESx73t0xg7wbza4XaklXBAxL43ER1w0hsBAC9v6G_iko9gpGaK7oZjAanIy_Ax9w63S7hFahGSPHIaMBShgocS3mZlbJDV0Cmh9d3a5CfyEWOHb1n8wujF40HSjriSi0zHMJRCk6ktrDyjTcG6aHatj-pDO-7i-hnFK9Y0yF2RLWiYXDW_RbzxBc1dNTXyoZ2JcdSaiiXQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XfCAMfd3cEsjriWfDJrPq_KKh-1jEEaP92q6tRdL1Ovvf3XnwdUebPdh803eu02_yYCAPLpB2t9XQNSZNebzfoqt6FFwWjWcfV6QYsqBD73w1Y9OVDCcoLdSfEDX3OTik62Yg2kGFSESx73t0xg7wbza4XaklXBAxL43ER1w0hsBAC9v6G_iko9gpGaK7oZjAanIy_Ax9w63S7hFahGSPHIaMBShgocS3mZlbJDV0Cmh9d3a5CfyEWOHb1n8wujF40HSjriSi0zHMJRCk6ktrDyjTcG6aHatj-pDO-7i-hnFK9Y0yF2RLWiYXDW_RbzxBc1dNTXyoZ2JcdSaiiXQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
