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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IRIhMok3xsIlQAiQSYxJYWubrCgyya2gHbNsRAwnnq3-wKqo-DcDjeQHNEzHNtTB89jeCvWltrb61PK1cr95znfSRukDWNlcOmx0HjxL24aqcfS-D5vx1ZEIFj0UO_RIafa9x1z8G6WSiQzsHPyK2MHBWoXNrEhKVzIgigaeCaNTHHoD5xADbRbJP-V6QNhQgLNuxK9aS_vETJ5ckRT6CLLJQP6ZkIM4eAT8ofx3AKPHeaVY5ZwBgJ3MZoXzZU_-nRTpq0rglt1dFNonbmk4kAszGpcrqSTDaEQ2QB1AKOmjH4EPGSPZxVHkVgNJVFIXfsHlJy7faUnONVhsb7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b91aNAu8FQx4HLXLqJ_-FOS4206A4_Ak7IvZAQunJybouvF5T3ld0oK2lf8M4KyR04LFDmxBLg3mlWdh7_BoaK7jiA4OLly4LZ4AuWpM2ulNjK7Ac5wku4TjJ_Hhu9-K8HldgHnpcIKD_yoXeKaDl94dG0Em6zEMA_SqYPnGJhyOhTKD3Wmha2kbVwBpVClhYJXEcm_AK2Fje9uwPmrE758xUJO4oOjRDc1uvnJm1LfZL1bmyioYcoWt5bgWr8aEPY0darge8-MAt2Kf6RkCHg6YV3ZWOZ_ZySbSABibFvF74uwCnSsJ4j5C8VSURzoqSmW6YL9qEFx8sjMvctcnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG2-bYrgDb4QAE3vv8-j5CU6TiUbwYkkplrruvY83ukiVVUkZJjT3xjaLU_fZQK1q6dPd6j3SD7U57nCuxzf3BSCy95rL20JumSki86RSkD2Y5LSNxLvo4OL27O-SQJ4T7tfLV0X8o0YKfaGIMudVxDbFLD6Pcy8-7G9rH6QbtyYYiHrwsC-Rcd6b8CdVeA4omQ_JaPO5fdSIkNeR89AyiHuS7ubud0FpGC3rKUWLKpCnkPAgrkj-IKsnNo_wt894txLduLwUKv3pH8uN1sSwFZU3U6YcgGO10efRfzUg_jqstoTd-doa0rlOJjF6hyImJdtMKv2szOx8IlYUATOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=efOjL8pg07hjHsH_Z93MTV2qmKBXjrsu0QQwPGUkQARgjYFTahgpmOktBpH1_LL4FVtBenZF2j2m6VmviT0lPQZct4S1iuLhhoCb_z7A7WsRoW4vHK6Ha76TYfdFH2ZUUbh7bevSt4TFXznUJjf3wXyh_I4HVU-6UscHU4rdkPiwci7K_7RkY677kQ2s4GYXdHhgRTFiYZUO-Dwx5kX_CWiw2OvBhSTiHPv9BKSNNGwX23DPvQIJ7zc5EBMNoAV1mvlAKNNu7n3Qpwz8-lkCC944Q8kHkuLqtliFAy8gm2vsF5U255Jyj_zt9nt5YwRLLQ6zUgjqSz9a-87npcYvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=efOjL8pg07hjHsH_Z93MTV2qmKBXjrsu0QQwPGUkQARgjYFTahgpmOktBpH1_LL4FVtBenZF2j2m6VmviT0lPQZct4S1iuLhhoCb_z7A7WsRoW4vHK6Ha76TYfdFH2ZUUbh7bevSt4TFXznUJjf3wXyh_I4HVU-6UscHU4rdkPiwci7K_7RkY677kQ2s4GYXdHhgRTFiYZUO-Dwx5kX_CWiw2OvBhSTiHPv9BKSNNGwX23DPvQIJ7zc5EBMNoAV1mvlAKNNu7n3Qpwz8-lkCC944Q8kHkuLqtliFAy8gm2vsF5U255Jyj_zt9nt5YwRLLQ6zUgjqSz9a-87npcYvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=vNMmQ-FOztL4_I5wexLoOZilkoqn43tJhulo4-SkwS7OePCr3EDXYIaBLSSYZLjDdWUbIjLDNQZQ4V7BioKUFI4EsRqWwrd3KQ_DsaO59x05Lv7iREm9jRLrhRXzL8pPObiRNYeBXSpVSm5YI99ClUc7VeZ4HTMIGthdN1pIz4SFNJgy5NnnXJ7bLRCDfrugQ_L8m84Tpk6Dq93NDGRXh-kkVCKKjuwQnWBC31z5TrHcJsLpQTSyie2rhtqxa2Il8jK2ig9Xx5p5pxaYzYfr8xt3SzQ7nF_im58Gl1C6SbxVYMV00OJuEr9DOgAY-85iAa_Ko8LA4yvjaKJoEy0XMCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=vNMmQ-FOztL4_I5wexLoOZilkoqn43tJhulo4-SkwS7OePCr3EDXYIaBLSSYZLjDdWUbIjLDNQZQ4V7BioKUFI4EsRqWwrd3KQ_DsaO59x05Lv7iREm9jRLrhRXzL8pPObiRNYeBXSpVSm5YI99ClUc7VeZ4HTMIGthdN1pIz4SFNJgy5NnnXJ7bLRCDfrugQ_L8m84Tpk6Dq93NDGRXh-kkVCKKjuwQnWBC31z5TrHcJsLpQTSyie2rhtqxa2Il8jK2ig9Xx5p5pxaYzYfr8xt3SzQ7nF_im58Gl1C6SbxVYMV00OJuEr9DOgAY-85iAa_Ko8LA4yvjaKJoEy0XMCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=qI7XIhAdIjO4VhAvCPSLNM_20WLN6ryf9W6GGQu2AAWKv6YpLOf7QWFYoirqWZD1teLPjq4QLs0prqJmTb-bfUXtbSeExYGE3Hs9J6TH424jxDIj6RTCgG0CC2GOW8EoRWrQ8b8khZU8PJBv1fHMMLlZPoBEeiQkptrMGRgqtx57HUwxBRKbYz5EQcBnhLsaxF2az7KXJ3-2uwVYcEyzr-byu0_iPJbTI0If-wlWkDEDdCElBPV3sfjArtWzlZlcq6PDHCpRYIOdouQpGijQN4yh4XuJXnagvFzIgvsTc_3zrWMztyYhmxz-UE6BsckNH1460waiOiJ2j1j-ZfIQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=qI7XIhAdIjO4VhAvCPSLNM_20WLN6ryf9W6GGQu2AAWKv6YpLOf7QWFYoirqWZD1teLPjq4QLs0prqJmTb-bfUXtbSeExYGE3Hs9J6TH424jxDIj6RTCgG0CC2GOW8EoRWrQ8b8khZU8PJBv1fHMMLlZPoBEeiQkptrMGRgqtx57HUwxBRKbYz5EQcBnhLsaxF2az7KXJ3-2uwVYcEyzr-byu0_iPJbTI0If-wlWkDEDdCElBPV3sfjArtWzlZlcq6PDHCpRYIOdouQpGijQN4yh4XuJXnagvFzIgvsTc_3zrWMztyYhmxz-UE6BsckNH1460waiOiJ2j1j-ZfIQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhID3zfPqecu7tcxT4SZfX0EQHWFW29uv5EuC5uKDiXuJ57hC0Pky3z19mK5Yolz8caWYl7AkquqhJEXnppyWAFFJxuvOxVR-Nqt_w6kqNhB7D3qmwptEUs03lb6KrYw6HPRA3Hn6OHdq5_IPgumpQbtVzml-87VINpOQRm-7QzXgBPvCV_h-zDPkJ-hAENs4bOYyBOSBvzZ7Eflc14h3OVSFMH0Ajr4KvXnGetfU6KQ_jVhOIOlAzQjMBOUq7DMETlz0AoS5JN4SGwawxqJRMwbTAPk4mT7kKhf-5mvhhDRW17SqEyLKKOq4S5Ps8sP7bGCHdjKAblazzjBEKYDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY34jKA5AK6m3mqRy9_fOJKSQU9aiWY-ZkPfKlqkyWl5SnFI0E3VsBiuSNJX6tm32GEnvCh6D1bNXv8XpoTq14spmTInaEyw-iqc78URKt7dbKf6lK1wM-orPgjm9ZP1HiuT1OcmwUAsZNppKnyGacDXqQ4cVMxo4VobuSNEZxADcIiSaJicXmw8I91OXMtWBQnIdpxcx-43DxLp_KnCbseRQtmO60gM9I37uZivkBCqoPuxu0w68-2Bdprx8x2i4azsNmiY6GlYpsbsi5swljkw0VLDdz3GPmUL-Wihac6IKIU6Axsb2F-65tdFsb8sU3_qMB0daXLsHgYVrLjZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=UbWr8FIVz_4oyPPPdJX7rHdnaW4n4fdKZFSAR4PIWZupQ3vOxaE261KecdmHYzocH7Z9DzGQ9We3kQ_ETmt7qwzC-jCdI0eJXFDgxlZzjxY4dD905EPuk_Lfvfbyc3MWlh-FzMhMXREG-teR1EOh0TjkgXia4rk14r_XnpsuaczsNSwMcT-vSHVnvO290wNi74g1NO_HfxzdREuE_GgNMgB1PS-vcPuFLvwHrOSe2rNqOO6EwTl-yvywOY8sN6tk3NVMmqE6qqqkEfOBQ-KpJHQPeWP-tBTDbfMNKTZBa-oAfY2-2nt3tXOdqArFh5CeIkJLkVzBRhovSOXrDdugMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=UbWr8FIVz_4oyPPPdJX7rHdnaW4n4fdKZFSAR4PIWZupQ3vOxaE261KecdmHYzocH7Z9DzGQ9We3kQ_ETmt7qwzC-jCdI0eJXFDgxlZzjxY4dD905EPuk_Lfvfbyc3MWlh-FzMhMXREG-teR1EOh0TjkgXia4rk14r_XnpsuaczsNSwMcT-vSHVnvO290wNi74g1NO_HfxzdREuE_GgNMgB1PS-vcPuFLvwHrOSe2rNqOO6EwTl-yvywOY8sN6tk3NVMmqE6qqqkEfOBQ-KpJHQPeWP-tBTDbfMNKTZBa-oAfY2-2nt3tXOdqArFh5CeIkJLkVzBRhovSOXrDdugMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrRoWOQs308wQmRMOAAKGbRk-dRA4fpZ6qQFge3zs_-rBLbUDx_9Q-mPeXldTmO56mmfTH9PsNQL55CJ006KLd5ytf3x-dcEWyCix_3aFWRbe7i6V7hUhsWO34Ssx-cjQMatXbytLoJac_wr0mnMm1wTURrmMgXzAJN8AF93SkZq8_zt96ugYtZXti_koKV7Nbr0_MeM7kbCTrdsZQ_CIC9AqRIGlReQShpKvQw3T9JfBvioBFUIUN-2KaexoPuTiqmUbf64Ae-6l3ZT3vtaohkWa1recqf8S5v75ygVQ4vlQnVc5_QJAgF_oVBA2oM9HFjevW-c5n0GYeADFtmGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TczSPDnlDgbdLICU4Vpn3QSz1MWS2G8nU_JD1udzh2lNL5C9F7__kYiRXSBLu7nwsbFE356llJODq5e6xpdpADFMLHsTJgz5jCDM3IW7pQ1NrWVudNoojuaEUpRpD8Ios9_UQjYvhdRrQxal2crJQToxb8_94OgOV-T6uHJ4wUkT-XFYwXNE2Tn4LGPtWLpEEuJ0MK3Z7LvCUOVRrMQmxi0_WGy0X_8Va5l3j1ZnryWdCeLVydnLeEcSb-RyzBZv4_wQlH0gl-S9KRx--9tsUaMAEb-lL-NE9SgmGqtoZ2Uo1OAXyMOrK21U14y2XeSAsL9qMuNbxlX4U70hMmRvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN7pdjmphVVBUcIvNzw3KIa_FJhWAyN4qMVwCCIsnJ_hJdys9Ulb7jOR7uBV792ITZrjjBzBKFHXJrRjuQIHTIZc8lztsb-kGiASzV4MWUfwVNibm6q3QGu59lsLJCbbJ2cpH1LsuLF6yrFckdddObqPFKJjpmvSKT96rN_-BVsAP_5TP3EcT3hPQALcLpzIBx567l09f5j6OIp3bPKEL7Vs-xdQSnMxhTNCs2WCjykZ83C_Gznk1EFa_BNSJmiRT9dD5ojJvsmC_WUaqCFbBk-D-R7dB2lkURB8KwTPDvtsNkuEGZa0Xg2gupTkwSSYkdBrOFf2MvdfIaq8rAbBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1tK-e4d8KVNIkzUhSp62285K8qxDBl4m2De2Ydk4RsdVG9ajE-ZWIf8uxr-MmqUGyNCfiJjFCoIRK9iyjx4hLWchIhqTjCaa1ihvJ-iOD1a-htT62k6rPvpHP4HQ18jbhAJp7YLd0HsZz5SwGEu3KU90_m61DfCbFQxTlH49DwcyJcWh1UkRBfePf6T-LfBMi0rSq6_9Ktyu-TUvRuAVQUxdwdPfU-hRdmEigUwYa2rZw2rVAKiFVH6Tyf-znjWNoyGmdDtawi3kG6N8sXLKZjMMmmr53xrZaOk6QFfKm0AucXZ2dp-vzP5JfwgxU660WL9ny_u_5gQwhRAOniZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=UA_Sbg3BWruy1zvWOemW4W11f-8eT72W5oI7u5Lm796t3GIPKcvX1bWQU0GprXW8TrWwQ8rK7dcphyDomXLY4NN0rUwleZ2lWykWPQhjxaqLhaSOVLe46mc_DQlM8uOlivnUOFOdDA2SQxL8OLXngILAS4mVPoX10bE0kfjgpeQ6yUl97cGbCa2B-sth5euyKpQUP0DRDc-0q8CaIeRZB6KOK3QpbMF97uD9_iS8D3al3lxVImx7MrTPEVnLQ4Ysm6RvnTDMu8yKUkI1PSdtPO1W1RqmZoU2c91ZZ2hxTPW7lMuVLsGQRM6eZxGKw-6VkjdkcsSNIsy5Co1-lCs2bbaVEpybG3WkYMEZPpDlY4XEGbk5IrIYS_vkVSso0tTraBO-wuDWITfrWzQ03FhVSDEwq91AVQec1Bok09LmIWM9qjEGAGsf92hqBMLgKYkqPQ4QgGSVl3m-iWmu6uULiwXMETJuVFjUGhNtG1Z65BAbqTXkGOimP1qtvCamzr_T8PWsMG1SGcwj3mAtj2LcdViM0ir9UjKEaZVSgbPsvXlzECnOz7ScxE7w-36cgzbRP9RWg3QP0LhKa6CGqnv9C1yACCHjAI-fojJsSl4G2mdTUAvk7ZBMlzF-yOoUTfnZyxQ-AUruQ9AxEinTdc7C_SoA3K9eq2ZwmbR0hzCioDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=UA_Sbg3BWruy1zvWOemW4W11f-8eT72W5oI7u5Lm796t3GIPKcvX1bWQU0GprXW8TrWwQ8rK7dcphyDomXLY4NN0rUwleZ2lWykWPQhjxaqLhaSOVLe46mc_DQlM8uOlivnUOFOdDA2SQxL8OLXngILAS4mVPoX10bE0kfjgpeQ6yUl97cGbCa2B-sth5euyKpQUP0DRDc-0q8CaIeRZB6KOK3QpbMF97uD9_iS8D3al3lxVImx7MrTPEVnLQ4Ysm6RvnTDMu8yKUkI1PSdtPO1W1RqmZoU2c91ZZ2hxTPW7lMuVLsGQRM6eZxGKw-6VkjdkcsSNIsy5Co1-lCs2bbaVEpybG3WkYMEZPpDlY4XEGbk5IrIYS_vkVSso0tTraBO-wuDWITfrWzQ03FhVSDEwq91AVQec1Bok09LmIWM9qjEGAGsf92hqBMLgKYkqPQ4QgGSVl3m-iWmu6uULiwXMETJuVFjUGhNtG1Z65BAbqTXkGOimP1qtvCamzr_T8PWsMG1SGcwj3mAtj2LcdViM0ir9UjKEaZVSgbPsvXlzECnOz7ScxE7w-36cgzbRP9RWg3QP0LhKa6CGqnv9C1yACCHjAI-fojJsSl4G2mdTUAvk7ZBMlzF-yOoUTfnZyxQ-AUruQ9AxEinTdc7C_SoA3K9eq2ZwmbR0hzCioDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhGI_ZLqRWwp9g7VOHlXQlzkCLXYqVxxKANter3CrIxSITN_cQwO-DKmCFsKXFp6MXP8s6GRS7Jjex3GsoE-N2gR69aSKKX2eg9gKAFTRST-3t7jk7T_DTLS8EyMpZKGqwr7fZ4r67hhiQbELZo2oQZ0KCXq57Grp-mEdI2bKvLTG96huUKDtB5OZO3jK4-oM-Z8EoYvfFqMINA59MTx7VXRhamXgq3XcdNPVv9iubI1LVIIbAP-Odt0N36JKLt-N-6yiXRs4oDMLZidTFG9PFmrKHy1cqsWLlF0yU1poywfEvYuSEuqQXE708pRAwHEtMAYL6GtgTEuOpwWorB4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EQmCsmjPB_IF6BoG1ehmFBMoUeC8_EMYk8t8fbhEhvtIZCfQ0943Lsfi8GaoL2q13TRo8o9i_1BoTdoT5ngtLMqQHV9Eo1duiZKvj5ZgEP2auCTLpsGDfIU1HoQtSx6cx6u29Nb5D-c2uUSX7gBMmt4dEvcep6_1lPpSF7PJLPXb7t2E1ns0hjWSditCH4HE0sH5T9AQQINRYzY14SNC37pYvGFNZvvj0UnSZoJbIPRExOcQsh6k4hWNBBvulnVJ-SuNawGg4fOgxfLKIhTXO0JQ1Mq4Ra3lVZGZzKiJgX3k2TWYA6fUk-2iFewBUiH4yqF8I2JqqBKyCMQZy3Hy-0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EQmCsmjPB_IF6BoG1ehmFBMoUeC8_EMYk8t8fbhEhvtIZCfQ0943Lsfi8GaoL2q13TRo8o9i_1BoTdoT5ngtLMqQHV9Eo1duiZKvj5ZgEP2auCTLpsGDfIU1HoQtSx6cx6u29Nb5D-c2uUSX7gBMmt4dEvcep6_1lPpSF7PJLPXb7t2E1ns0hjWSditCH4HE0sH5T9AQQINRYzY14SNC37pYvGFNZvvj0UnSZoJbIPRExOcQsh6k4hWNBBvulnVJ-SuNawGg4fOgxfLKIhTXO0JQ1Mq4Ra3lVZGZzKiJgX3k2TWYA6fUk-2iFewBUiH4yqF8I2JqqBKyCMQZy3Hy-0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=T4lU4I9BJhb5Wd5oJpBY7OIpnSty_6TJry9wFUwQnUstN8FJ4oofdVvkRzBAE-eXunv0Gi269UePFadjsxqWBqH85xLqtPIhnYAgk6HKKOuG8EVwWnsbTIxM0J_1U-6FpkeSSbh-ilAKIJqAdVxcCDMLUBdjM386keKlorrYD6bZ6v0aLwtWB9xlcSxi-Li7cOXcTrtAk7XaUrZ9124pW2EkrMs1CddqgrG9klL58HtLqq75uc5An6gEIXuQGGPG5qWABsV7fmcmZbhg3hGIo6RstlW18wy58XV9NS4GYH-WtJgIXWMUuu4cPn40c7HWJFWQ4mAqqaFB8yCXNMnlsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=T4lU4I9BJhb5Wd5oJpBY7OIpnSty_6TJry9wFUwQnUstN8FJ4oofdVvkRzBAE-eXunv0Gi269UePFadjsxqWBqH85xLqtPIhnYAgk6HKKOuG8EVwWnsbTIxM0J_1U-6FpkeSSbh-ilAKIJqAdVxcCDMLUBdjM386keKlorrYD6bZ6v0aLwtWB9xlcSxi-Li7cOXcTrtAk7XaUrZ9124pW2EkrMs1CddqgrG9klL58HtLqq75uc5An6gEIXuQGGPG5qWABsV7fmcmZbhg3hGIo6RstlW18wy58XV9NS4GYH-WtJgIXWMUuu4cPn40c7HWJFWQ4mAqqaFB8yCXNMnlsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEHPwVDp0T5IG9PxN5ekon0OaM3JTEZrbNIldPzKqBpzMqPfYVjv0KZ9u9XvpjVWgA2JSdl83ku9i6049b4gMqltF3vBuZWj3ShCkB12xcyrttjJQE6KhhKLmlso1hZLTIuHGE_9Cr25H0PGr0qzJQyoUlZ_Q0pclqTrFqQf1KoBcnOGxjUVyTtQn5TPuuBb-_lAew0sIlR8tZ2HttMT13y-l7RDS2gf5qyC-vWZmEwaJg35Tjd-FqEaW7XVKpYqY87SGQHMWks6Q9mIi05Tmy56azSHL7ny0OuvA0nlGfKntgBtjgabUSiC8x7m2c1rSisPBRgEOQgXF4iOhGCYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=UBCaH1WPJdKP1yjCwrXV0Miogl9IX4Rn47eSyTxA2o8OX6GXDj5AAYZ-yLsG9KT0NOzBszlrqAfWSQOG3YAeAvHC4tzc7AYfO7jIqjgmSx9vbTaDGw_lT5xKVvdOrSZjYAov3g2WI_JQhlhkmj40a9IVp5W7_Nnj2vYLULbvkPrtStDa3Cww0l-vXRFfPYIudonz3dHMz5lcOefHgNTefatflEMD0QNTRk0H-UEllvSzBYhxOXW52q1xplF_LvT-UepY9csfGuaAvym52dUZbwwu5djg3mNywVjyDvw1YzLjA1VKd3ILbYdMwcol_t4enmfewk7G5iqxVOO5AKXmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=UBCaH1WPJdKP1yjCwrXV0Miogl9IX4Rn47eSyTxA2o8OX6GXDj5AAYZ-yLsG9KT0NOzBszlrqAfWSQOG3YAeAvHC4tzc7AYfO7jIqjgmSx9vbTaDGw_lT5xKVvdOrSZjYAov3g2WI_JQhlhkmj40a9IVp5W7_Nnj2vYLULbvkPrtStDa3Cww0l-vXRFfPYIudonz3dHMz5lcOefHgNTefatflEMD0QNTRk0H-UEllvSzBYhxOXW52q1xplF_LvT-UepY9csfGuaAvym52dUZbwwu5djg3mNywVjyDvw1YzLjA1VKd3ILbYdMwcol_t4enmfewk7G5iqxVOO5AKXmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=IH-4wB-7Ri3qJ9lZK50IEc9S6L0_3gFAjgIZCkkkep7aWIc87cr-MHxhz61yjwzcIRQq9lQ1f25eWHfdTDdVWoGHTe8xvBLFJLR8aVSXw4O0nL7PRRQNzV3HB78ucsApQs79FiUuD7zZe3OLXJzn1XT0cqFqu9UKYHrUZLjzw6OucL_Qj78QiyrBF2Nkan4Nd7GNVQRClbJICazOBphA_RK5amb_E5kn4LvRGuS7-ABjBea40KZEP6Kghu94YBmavShPG-i2cHJ6fvGWt3FCiP4btGuJuzE0gptrapVVPdA6N8FbUNnwv0lAg5U7AqjrmSzxN8krupqRbuB-iCQUQkPni9ZOWqL0-h-5wZ8oTVFrJVJDnXNzIQy6M6mUoiLxnrtwaBSUBnyulclD74EkZSWoImrEQYFVh-OCZ11TQ6xs1tKPcWt4ykp4sYzbZaZ1TV91oSIa3ONo9K3_edaw3TioG3NFp02RO2fs_qNWwX5KPWEPV7bEkl020RUrv-JYvgjwoocndk9kCJ2aCAhEd1wWaVCcB3LRguxLEWql2Ojt_3k3w-_sfGg2FVsTv5FJdLha5W126eb234wGvMb1II0PP8b3V9KO5ovDEe0YEZpj1wH2qgWzQEK_LmSuf5e3o4yEWH7JeeENcOXoqoN-dr4RPk2Ci6YOnf-T-FPCNz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=IH-4wB-7Ri3qJ9lZK50IEc9S6L0_3gFAjgIZCkkkep7aWIc87cr-MHxhz61yjwzcIRQq9lQ1f25eWHfdTDdVWoGHTe8xvBLFJLR8aVSXw4O0nL7PRRQNzV3HB78ucsApQs79FiUuD7zZe3OLXJzn1XT0cqFqu9UKYHrUZLjzw6OucL_Qj78QiyrBF2Nkan4Nd7GNVQRClbJICazOBphA_RK5amb_E5kn4LvRGuS7-ABjBea40KZEP6Kghu94YBmavShPG-i2cHJ6fvGWt3FCiP4btGuJuzE0gptrapVVPdA6N8FbUNnwv0lAg5U7AqjrmSzxN8krupqRbuB-iCQUQkPni9ZOWqL0-h-5wZ8oTVFrJVJDnXNzIQy6M6mUoiLxnrtwaBSUBnyulclD74EkZSWoImrEQYFVh-OCZ11TQ6xs1tKPcWt4ykp4sYzbZaZ1TV91oSIa3ONo9K3_edaw3TioG3NFp02RO2fs_qNWwX5KPWEPV7bEkl020RUrv-JYvgjwoocndk9kCJ2aCAhEd1wWaVCcB3LRguxLEWql2Ojt_3k3w-_sfGg2FVsTv5FJdLha5W126eb234wGvMb1II0PP8b3V9KO5ovDEe0YEZpj1wH2qgWzQEK_LmSuf5e3o4yEWH7JeeENcOXoqoN-dr4RPk2Ci6YOnf-T-FPCNz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOf9ZbabXVth4YflxpOGUYkD0ZMUp7fQ-ADHE61agyBZnxBcd41BDKVa4bFFGmY76G9l0YrBT-tWikWUf6I6q29M2mz_zGivfpt9du32iIQwqw__MIm8tmmQ7H-MdvwLVTyTcLg7x1bxNa46iYtCq3Wj2K6HxO8MV61Y9RPYkFhQA3Y9xKWWqG3zfPqslTpBgRV83xQ1jTkwcv69uWXvWlchX_l0bwcBMtOmcjk0ns1r42q0T_BSRY6yvj8-ZmLl4Ofi8-sLJsWiUhoUhYZz2XHsglfD4t8T_5TJdlXhPUilS1MI7sLuoQW9FYKw2PR97efEXsPNjE6vElmnKQirw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kb1fhADQwr8nQf-s5kLtG-5tPSCerjepaRDNYme5RdTQIbEmJjCZU0wF8tzF21_VpmxVLvmwKjCwFq5Kwi0Gvrmjq_DwcyOU2lwqBvhf9pllYOdlWH68-8kAPnu5FL9Djlru5qlj6Btyvyqh4GVYYOqkvptzJW7wU4ReW2uKbfpWXGiJ9_N5N3dyZ9RX9pUXkV9Dmv1um4S176uAoO_2DkiZLUaqfxTB6HN4j5lv9FjaNXQSpUk7N0qB7fQRK-HI-eAK-0cVuEppTjk0EjjvpXLcRtIhCHRC18Qz8ZlyclbOyeuYlKUGrLz7Nazd6Trh78OWrzI-otWuvKS1O-Fmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcl_KJvaLY6t-4joGeNzodryBFoykGCjUpHTWwjZOIp_jJSwDY9kjbEe83O4jmlba0fcC5UlKRYAQz2qdW5xrQRN1pzcKs0DMQ4gzGWDCIfGcCH7E0I7zH34CErYmYiuFSvU7vdQVkYAYOw2iFFJlq4yGhovQcmo3lh6r0s8BIs59s3-3tYXIE8kMobxVHRLbqq0fTtL8H4qvk555xWvROoyPXxjlNcmy0OaO-ERMdkXcrnQ0qYvsiXl3C6AOZjMye9-4C6I2C9MGS1rXcjYh0KCO5-OD6wflzKNJUE2JjNHgdMYQaaf6KQGB3qpLlUemJS8UawLJrzXVVNJrr1hEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTKq7mD1ffMDKBS0XG4YAWiW5nbvBe0myfXg6_qBT06NtaBR6uNrKz4XodqLAzcNttCuSjflMthMgmw1SCXOlQ4KHJEE_Zj89aJ1J_O4FcK284l-SzikDUf6Ct36E83nADMTj_4z6nwyOSkIU899KP-iB3qdq49XwNeXX92uDQcbcq0_bwy6bmkfDOjL98CJgSYZ2NxuffHIOg0BGrW9yC4BkvwsVWlvkEbH5qrfG7G8l1_uCtUL_GG82gii-UA7tv38fBSUqvwpcn34UtmfGJP5CD90EFmtV_8A-f5J8Fxux2E2X1As4SPkm5Lm2ArHjYh1PpWcivfeTKfDM8cXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhz__HnFLMpguupgBFIwtHjefLJGpZG4v194maZpIHY3NiaU2700Togt9PE55LtrEexCEwNMSQjfYsh4MXUByb_qtS7ysT6ms74xy16OLjh9LH9-T99ObEnneqRTc1Ik2l0UAJ4xqJ8zCcwXkWKcjARB9ORuLTgUnxu3V_z6dpaoHaSgAOcIO61H2s78AZvr-PW8dNPeEgYwwnE5ZzKlffrl6smO2c1fwP7bZGV30kKU72DbxwHj-2J1G7A119lW7SzRavKUcS5MRtEQ6m37XqMeLcbrZ2cblNuL1z5Hl5wJ6b_z66vinhv-O-snA291FMYzRxCMle093bsZeRSwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy7RV_2HMXry7mwcLt6GkzR2NV9UWbLmVn6K8FJ1A3aemxxVhTK9aUvBp2krdA_EMkDcKWTdAfx2gMBtXxU2B65MuO2vvhnOk1UhLWzvcmnKxqkKe3FTXBtLeGke2HWopdnd4hsyxUv8UcSEP3kudJHQmaAnz05w9cUgY9tnlTOsd1WrKysEH3uU8A4QFWb-gYpFx4fS9kU-J_Ny5e7Ers0G6OC3i5XUHdDFEl--yE-8yw5dZqxPKGYC8J4XUwlIIqR4u-F-RQhFW0IPVshy8km1pW1GlqVBcwpGpTLvvYzNqG9UCendLFjJoKdwL6HDYzE_UIiWeIPCdzCskxXagg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qg85x4aMPI-_FWRA2sHDmdim0sRhclqKnp20_9DWN85lb7HywMZKN6mmceyDarwM3qTlNWBppJKqYIzvFmh3Pcdg4_K3lpKuGP9TnvrLABNy4ufgBgF0DUK90aARrNQt6lE1gl-xTXQpi4lQteQ0jHeTr60lXr5k2mctf4ynAeQ4p7uVMOmnkWCBzo072jPHucGraqQ12MrFdaTf4GprggZdDyni1dTwoglIQBr1Jkc-CBjH-w3rOU-l5ie1RXahS6aweWqUEU233Jl5lFcLInQsWLkrxQVDaNFruwjAiNLu5QA44iXUjEWe9kFKVREhjKvEDxl2pJ4SCFeMJRn1GHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qg85x4aMPI-_FWRA2sHDmdim0sRhclqKnp20_9DWN85lb7HywMZKN6mmceyDarwM3qTlNWBppJKqYIzvFmh3Pcdg4_K3lpKuGP9TnvrLABNy4ufgBgF0DUK90aARrNQt6lE1gl-xTXQpi4lQteQ0jHeTr60lXr5k2mctf4ynAeQ4p7uVMOmnkWCBzo072jPHucGraqQ12MrFdaTf4GprggZdDyni1dTwoglIQBr1Jkc-CBjH-w3rOU-l5ie1RXahS6aweWqUEU233Jl5lFcLInQsWLkrxQVDaNFruwjAiNLu5QA44iXUjEWe9kFKVREhjKvEDxl2pJ4SCFeMJRn1GHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pp6ped7ece6_D2jgdFHesrmcBlg453zvSYngvex7lFp-MeYnH8rBfMC4Q2fOYK0QjVirCJXnnZwd6N2VFHhcmN2OJUFC46hYbQPfuZ_jO2VLCnJbJd72jsZGZfCGr7UY7QOiGW_m8V83kfxZJvc3NTJcee_xzGtLkSELI6NUliF3IEd3ByphcXmiDKbmdVkIm56yOFX6wORAwhS9d1kn2V-THKJh9R5-UD52vkmyqP0f5vDfJiGtC1u5l0Peb3m8nfXs-Zt4CxpF8nDKDIw6bItKFY8uRIpdhXPy8O4AIKNRWEulMv0CVJXAQNbf77EQMMY8kYCKaNvBgGNiZiC7Bro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pp6ped7ece6_D2jgdFHesrmcBlg453zvSYngvex7lFp-MeYnH8rBfMC4Q2fOYK0QjVirCJXnnZwd6N2VFHhcmN2OJUFC46hYbQPfuZ_jO2VLCnJbJd72jsZGZfCGr7UY7QOiGW_m8V83kfxZJvc3NTJcee_xzGtLkSELI6NUliF3IEd3ByphcXmiDKbmdVkIm56yOFX6wORAwhS9d1kn2V-THKJh9R5-UD52vkmyqP0f5vDfJiGtC1u5l0Peb3m8nfXs-Zt4CxpF8nDKDIw6bItKFY8uRIpdhXPy8O4AIKNRWEulMv0CVJXAQNbf77EQMMY8kYCKaNvBgGNiZiC7Bro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=mdzglabqaNxT8qBxaZWa37_DbpZ9ElfHBr3XJhGMl-Y-r9mCPvCcEsVFtVZQk8RBt4fmhp-wr1-dWImgl82wL-1rA4rnU6VPYe2WCU4SYfx3kFXqTqiRsJKCStYXkhSIMxAbR7pJaAwXZ4JEglD1-pu0oT_jpZjgjE1dVT7KkPIAWnV1BVFW2HWZpfryrybIKRQJ6doCpgpOWWW66NI8JYYeycpFPddEIMnT_BOYbMcRUoLqPgHT5HbImrsvpieUXWsfozKMGn-1pWr4YbvArscWS9Ke5IICGaWtC0-vUqHfResMVvdqL5q4l4G20TpyLhmX1ew-lknprhZ0hx60Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=mdzglabqaNxT8qBxaZWa37_DbpZ9ElfHBr3XJhGMl-Y-r9mCPvCcEsVFtVZQk8RBt4fmhp-wr1-dWImgl82wL-1rA4rnU6VPYe2WCU4SYfx3kFXqTqiRsJKCStYXkhSIMxAbR7pJaAwXZ4JEglD1-pu0oT_jpZjgjE1dVT7KkPIAWnV1BVFW2HWZpfryrybIKRQJ6doCpgpOWWW66NI8JYYeycpFPddEIMnT_BOYbMcRUoLqPgHT5HbImrsvpieUXWsfozKMGn-1pWr4YbvArscWS9Ke5IICGaWtC0-vUqHfResMVvdqL5q4l4G20TpyLhmX1ew-lknprhZ0hx60Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=cj49Oa10Ip-YZpzsdx4tCGtXOiyD4tDJwWbJTTNP22XZBbLrOJP8gI9N-3ElDbk4uf43eD9BJ3yjHZhLgs7lz-dtofvFU43vj7ZRl3zqqaYnxEQ7xz-WNGFsJkt6N-PW6kKw8FKRyWuqnR6qUlgx_F_Ok7eDcK7vxupL9rpZ9zKvjFYjGwGudcfu9lLLIzYKjL1JcEfM6qxlf5aujMeEWvFof85JfUrNCc1NipC4WbpyR_3DFCYTGCjwWM9-vyko8PAIBPib-NS5mFfCns95sYQc1aN01MZ-YvHcoGkstYzBIlbNNwD3Wpifv1aoCR2J25keTgfn4jHEilTS7uK0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=cj49Oa10Ip-YZpzsdx4tCGtXOiyD4tDJwWbJTTNP22XZBbLrOJP8gI9N-3ElDbk4uf43eD9BJ3yjHZhLgs7lz-dtofvFU43vj7ZRl3zqqaYnxEQ7xz-WNGFsJkt6N-PW6kKw8FKRyWuqnR6qUlgx_F_Ok7eDcK7vxupL9rpZ9zKvjFYjGwGudcfu9lLLIzYKjL1JcEfM6qxlf5aujMeEWvFof85JfUrNCc1NipC4WbpyR_3DFCYTGCjwWM9-vyko8PAIBPib-NS5mFfCns95sYQc1aN01MZ-YvHcoGkstYzBIlbNNwD3Wpifv1aoCR2J25keTgfn4jHEilTS7uK0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=dxHnRAWRfaHS-jVi6xSldd68dPyEQVtKMUiIkDrPOTXdY4D5-JlI506qWuaWmGSpcHG_jPuq6hjHIiO5gKZvyBXJkYchyH0wpYvCSCZwAGjJLayd28doSG0QNNp7k3ARKrPUHFrkAZ_J7v4VCOb81x9YRiCXNw36skOKERoaw0TwK8a2Nfu5Z-ME75_hc-W5qIn80ZtaKGnCTclisJkJaGlaufzjiIOcSzfEL1gQRn0RtVMoQ0RM_PJd8wjlMyqNS5z_E2GAE4OyUiZFnmxzk8u_kRr7UzXqJNH5PdnVerLbHinSKHF1e9uQ5GU5DMCTZp04bcooV0WhnPhJLi9fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=dxHnRAWRfaHS-jVi6xSldd68dPyEQVtKMUiIkDrPOTXdY4D5-JlI506qWuaWmGSpcHG_jPuq6hjHIiO5gKZvyBXJkYchyH0wpYvCSCZwAGjJLayd28doSG0QNNp7k3ARKrPUHFrkAZ_J7v4VCOb81x9YRiCXNw36skOKERoaw0TwK8a2Nfu5Z-ME75_hc-W5qIn80ZtaKGnCTclisJkJaGlaufzjiIOcSzfEL1gQRn0RtVMoQ0RM_PJd8wjlMyqNS5z_E2GAE4OyUiZFnmxzk8u_kRr7UzXqJNH5PdnVerLbHinSKHF1e9uQ5GU5DMCTZp04bcooV0WhnPhJLi9fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=NVhL6Wb1I0HjGUkccLXqlSL3yiuWgqGluAq_g8CdbsiqLCDyi2Xs0W5BgoqrJGfOXyjpAlEFy0J1zjQ0mUL1i7gvVY0KM-jEd5_mujcaXChgXN2RD1_OVl5LKPzlP6zoQ4T16kXctmwsSmJFXC9RCUTYc_XFEUnw2296sIkoD7_HsMbqWsdo7Ju35xLVgeickUhnQvATOjbl5sLkFg0jHZggo3av9mfUEK4rnKWa8T29-h3G1gRqaLlmbadKO_mY1f6b3cHs2EjIT8oGtZsnZk3UJKzRwJnPem2YFddVXUC0eJmWZ64qRLHbStdsyZmxLIDNN_eoS83vfohaf2ewAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=NVhL6Wb1I0HjGUkccLXqlSL3yiuWgqGluAq_g8CdbsiqLCDyi2Xs0W5BgoqrJGfOXyjpAlEFy0J1zjQ0mUL1i7gvVY0KM-jEd5_mujcaXChgXN2RD1_OVl5LKPzlP6zoQ4T16kXctmwsSmJFXC9RCUTYc_XFEUnw2296sIkoD7_HsMbqWsdo7Ju35xLVgeickUhnQvATOjbl5sLkFg0jHZggo3av9mfUEK4rnKWa8T29-h3G1gRqaLlmbadKO_mY1f6b3cHs2EjIT8oGtZsnZk3UJKzRwJnPem2YFddVXUC0eJmWZ64qRLHbStdsyZmxLIDNN_eoS83vfohaf2ewAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxeVoZN2G3JdBJ8vk4F9YTUyzf0wHZKL6QvCPzUzf8aJsJjoQ80iLSjXZ_b0id7cu74PoTVUYSwmLwzk2aN9q9RVxQBNJiZ3M4ATIrbnUZg5qo0txV7bJwyM9FKf79dkx5gRsVoEGIIyn1KK6QUSreArMHeHAVyVLkDrnUM9giAZPNvtrLjtbzssIuhq-cPGQxIm8c8lF0HtQYXNAltw5aJ5hj4WKp7PS9LKNDHpxRbykzMe7XI1HSCIqJqPruRm8iJqFlk8KrswDdG4XqZ7l390fyqjF0dzKIuIskZxKjBqsnxtJ8dtv2o-_frybv0aKCYHiVBuVJ4n0jx5L0Od8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XysOVtA7RET780l-DaonQFksvJWCLMegX0olsQyE0iiP2ci9WDgAwNoNKI-LdRZ6QO4OXd0Im5r-MTlLWIa_QT0--_Hx0cQ8oUoz2SMl5A2M93kx8POGnmDBbu66nFDZlY0PBXMgILvTJksreyQXTbcNO8-pyuAJFyON10gMA3LODVqXgdIfhyeuIKtKjjt8zhaA25ctPeqA-l2uyUFPHZZ5ObvckdYwzxD8Kbrq3XxgDAQZz1GQkXOdgjB-7_7O9WhGgA_6GtwC4IO7__GBLa1a4EgwFKGOz7HnmaKIPi1pxZZICHQWugEqCF2zy66c64eDhQ2zU3dMEUMcttPVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=hqUEQfmoWQro8fqabRDBOUKPIZrghpIZupAmeT5_G3Bmkl9NNRA031o6Ai5vc9vtP8vRpjYm18hI0Kr0p8GupsjWC-UyDGqTsckglRMysv5dIXAE3fZlw7Aj9u_goLCBjxe289OmpAQdP7syR7ZhUmzBIEh_w0CjhE0ksYr9DZ-iebpRPm7r7uFqhBVjlTRE_bEO49_1OlZcw9IGuZqPGgn7l0ePXcLJX49lI8bnzba0B0TWHeZhRW3ui3E1jFK91zPZabI4m4B1DZ-vvbF0SM0JNTRoa5wDGSMQ_FGjZcC9n7EJesfoGJTkOsmVc3BmSlGYmaSof596HMj3Gvk88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=hqUEQfmoWQro8fqabRDBOUKPIZrghpIZupAmeT5_G3Bmkl9NNRA031o6Ai5vc9vtP8vRpjYm18hI0Kr0p8GupsjWC-UyDGqTsckglRMysv5dIXAE3fZlw7Aj9u_goLCBjxe289OmpAQdP7syR7ZhUmzBIEh_w0CjhE0ksYr9DZ-iebpRPm7r7uFqhBVjlTRE_bEO49_1OlZcw9IGuZqPGgn7l0ePXcLJX49lI8bnzba0B0TWHeZhRW3ui3E1jFK91zPZabI4m4B1DZ-vvbF0SM0JNTRoa5wDGSMQ_FGjZcC9n7EJesfoGJTkOsmVc3BmSlGYmaSof596HMj3Gvk88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezHrmy6DJAaamBR-pAHhENlMAIffVk9zbpAgQhSLvSQ8LuUo2q1BABQW8cghCFqkDmrPGSWExm40eQdTLEsztU659YVNInWE-qX16DyIKAsVqI0yYlKEDjQUu2tEQrro0SlPWDTbS0G7NrI_NmOjAa-8jdhr1SxmFANUmLbJ22X8A3L3Hfsuk8PtY4svjBzFXSNqbwBaNKLuVB2ElWfF-czvg9I_U5P1Ve9zsI1FhTPV095J7a554pHfujANSG8VzJBhihk5uo1r8ZMsiTWI0QkkuohJ24Fo3pBq5VVptGl2IXJ_5djL06Rl23yKde3HBQv277phReCRs33lotqzVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Jbk_CWn_Kd30GbXWQTBIt2KRwv2syMjY_KqQQCBJGLWHa32Avq9RjXAjA1XuKrlHUx3APh6t8qu7KxvMTs5z7Ue6C283055IrQVf3imeQg7zy--yqQWRI3EChziH0kX0Xv2t2ORl_Aht1TQjcce2eJfTaib6tFGghcXuDT0XwMc6aKXZmjaeTtwRmWXULYVrathU_ykc3VQqqMXg__Hs-nprXt8hk0eayqy70QhgwT1aWgFtcLvaPXOQjXMdg5ww9G2OLoSQ7pJG2kJMJR-bbt_0mGnEPgJ90J7PHhEISkkdFtx8cN5ITjrkDAOoIZ87uShGaZWaWaYFk1twotkJoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Jbk_CWn_Kd30GbXWQTBIt2KRwv2syMjY_KqQQCBJGLWHa32Avq9RjXAjA1XuKrlHUx3APh6t8qu7KxvMTs5z7Ue6C283055IrQVf3imeQg7zy--yqQWRI3EChziH0kX0Xv2t2ORl_Aht1TQjcce2eJfTaib6tFGghcXuDT0XwMc6aKXZmjaeTtwRmWXULYVrathU_ykc3VQqqMXg__Hs-nprXt8hk0eayqy70QhgwT1aWgFtcLvaPXOQjXMdg5ww9G2OLoSQ7pJG2kJMJR-bbt_0mGnEPgJ90J7PHhEISkkdFtx8cN5ITjrkDAOoIZ87uShGaZWaWaYFk1twotkJoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfi46MGbNDsc1-rGwrvqZ95MLve4iIGmd0CjrpIcCtedWFztTT2BrBpblCJOx3fBnE4ZlolTNUlq5MDNmnZ6r4FfY4l6XnEJZZKD9FtXuSE-JcebuMkHQ9Fex_5c80IO3S6hd2GhMZkHg4zHNVh8EsCV0kOE68LUqjPI_1F7i_7yhqZXKJqHcRaY5i8XK3UbwcpH2BkNmWRFGh6gE4DpUk0NDtt-iv1jmeaV969WgvCn4lRLvw70pI7xHGolMq6kbb7g2Io4AtbsEh5Anzf9B4H3wWctsXRNfjzYvJjP_fODTWgqmzT2IPCZoZP3sB4nqlvOEoML9VE4ngYOBbzOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-iI_Weq38bi8aO_yNPchHvbXUPKBUt98QqdmWIWnrbyvotCeDpjxHWTQU9hcuJN_TTzRdFIyRvGWAfDL9UFIe4uTYyZsiOAqgv9e_e9VIwU5Qv5xFH9KyGqq6BdEMCCdEV2QTaO1JL176HBZjsAbgSImDo9sxCNz5KRDOReVntGTOHGHF0h14mMS2pYiMen7vexjGSMVQls4SEYm67MrCW9JHiu6V3aIkX2HmY0GiNexz8MU1LoXY4Au-kX37JYkM5Xd1FA7JGoH124uQ6-4Irl3ZntxR0R0qx-cpg3Z1K3bhaCwEvmJbColSiE4W2E8KTNWG4-mHw0ffA9RG5dcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEDVDj8uqkPmI5rfcOEGMFCns9x999AaYSXiLvh3jF7CaSBO3bncPnmbgZLIQYGtIYdxasRpwLOW7iY0zdA8xRxUyideS9qrTkKNxsU_g_fYZRZt6WC6RDnqKlhwPrNE3F3aYbqqbOE1woNFINBzidWqFO1fm_8HFV_zWGAm2vvOmg3m76nHruXajqE89P9A7i4EEQX-qI0ElxOH8ztimlvJJBQyeIvrHulW_KxGMGAcINgwioud5K8Bww9aEpMP3GgMN6TRaqfkacBiCQa2KS9Tzh_n786rfBSJFw6dxoK-d1vJN1AwGam43DmG7RISdmQ8tQjYay7zl3Vz5tcznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVLY709OYH7b-1C1chOqjrdrEDctjMzoWc907fG8SduLelbFMO5gkogHiT2EM8yCnAQvCaQIzCV-_fc1JtXozWUa-mAWHZmE8OhDetQW_57rlYjnXMhH2Yy82fiEF5a3oAyqLjc0YrVG-uNjZh-ihlialFMfmXHdf_6rVJQHpj3OtMRmyP8GVyS_nNS7ZmGMdCa4qxMuAJta-iv-lKO76jId3Y8abMmbWW75qCBQtsumKel16TkzzpxK4fYSrJRYlAIZW6ChYaZN9q7amjQ7rVt4-NxSTthowvoDBna08uT9zGr5RPBU5pRoxfjOM8zASLMaKj455hbSD8HncP7cFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QI-aVVPeFai4enkEQD8VWrIvRfAYVf9GZJCmfxgbZGInfQRDjmE6t84mF89mHBq-c1HZrnLZFud_EmQgXioOhz_jRoxGI2EJg9n6rVX2RawSlt-NtISKV_FnKjttevoGGhvRutE6tz1ki04z6NcyJEP65lCES-E7A36Si5crf7fn96hRroMIEhQT7yh0Gsc6IVQYJlmfLoVkpXaLrqgXOIv7FN6xMmixvej0X7r-dyeGQtuCWCn3ymzpu1UFu6dj7unbv6D63ANxtkiCZ-Z5QBAuQU3A0_-nsMFxvICJ7rYUFA_x7f5m_lKcLipAEfFi4EwXYXYV0lBE7HHtTLlOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X95m8kQAyPUHY0T6pFypziFnfkIXzuh6EBrr6YOi5N6AvRcUdxV3xEGMoeU6TZRYaslgAc1mh7kE7XaHO57pM5ER-3MfREqtJHxc-liXhcS8WySBPGVVPQcP_VxfFnpGFiZW7BKem4tOWTcEhGyNvoQoTjXnxL_DdY6mwdcaYMVmancN780gPMLNH1J3PbIqn5FwEYZLIQ000ZoIl7SGQ-D07ppJAeIb5AJfx6bEa2IFUBJIKyDmXUC1B_Jd4YLsXBeoSUpdKXbzhaWGorW9XOZrxBa7rf578i_t8FXzLMmwrBiHaCaR7aT8Whc_SkXv2rSwjz5lZhNZ3o_fx-L1tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9dhvGv0unZoZaLlk0qegUMV4ddqJaT8b5A5PFafKqvI8hYXqnIl3GEHqLqRHF3buhAR8-Iro9-AoMu0sDvPt73kkirRrzFdZTIU8dY4Ip8sywXeG5o1tu7sOySCD-P6j7s5yz_UM0Yd61N4EZ4BnVIc6MyEIJpYg_xQ3gD5ko7ugeDiGT9MPbJPzKbfCtY3OuHPK5lrV23hZC8DDhoOG_VlIG-VrBYp_D9LRizyUFLhUfFM-VhNHmeXdqkgogjkD9tTfxwc_n_NX_cIFL6vJXfVq_0dRKUdHAy_78dA8nNc4AVDn9vsNINTQA3pKOIBjl-qvSvccUu93H8xN994Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOHSC6iBr9oLeQOzQe1BY7j3F817dFhCfoHlJ3oPO8WIz6TXO_F_rBUMoVHXrvsNVG4HD0U_LZqi4ZkOdWP4y1cT9KKSzDcSXqkZ6ucSsNiSYco4UBGolFCLTrBh8ryVavgv6RZxpErBC84rkpXhaSLvN3jPygamdnzhJOO-nMYKDNK132_qzBdSofYyadP1avy-GKqY61QpdEdlROf5qArqVa8OTla406Q_q_32q8a60iV9iKsI5Z5sQ8Epy8IIYMJtzPCLjprbREPD8S6VJRHhwKIU8dgLVlERqtFOFd0_B1lyG7fytoBg0OyhHZya75YdwtJ84ir99lNmnhRkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNpt2zugs7ztA42je-YL5xBepp2vvn5YjbR1yT7JjBXscMyptPCfa40d0O3ydoG7qlPEA2z-daF5NGVzlhuovv7V6DDYMh9DNUM1lf-CtCyETrtF8fxvFmbd_V1bMZ0gPipskjMZlM6ZH1KVXl2Ydy2RBKCK8o3GZE20O2tRflAoDY-BQpU_5kCvlGzKPvFk5La_nO6-AnicFnXGByjqM0cHoAPkCziWcVZhP5wmovpxh98dMa9RY2M3ZzDS9-OIeJ7LYkHh-Dy02p4pqMLGhxw0vmU7vrtuA4X0ebWROey2eAv_Ao4bw3cZGlv5siHlwtGCwypyfkuDxfg9HjFsvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUkFZcexDpR4Ay_Zoopd04lOqAonIyrc4qF_4GTRirPeTBFdKQ99BsPfhIKLXWmGXTGdXAlPgWU8Hf_1B_b8irsFU9OLc6GRggz7orn9wns8NG2IoIu0spj4KxwGMEWYNehh18zT10nKv-MidDKrYn6rauyS1p9U316tE-2NWgplOCyjwZqnByksWDoQM4xv1mdNB2MklaQ0kFCfZGN2K54FJYbbFdIItQVG-S5BcB5CuVx-itkr9n5h39gjxotPG2mmtSD7eJlEbaOTzlbQNFYAgFpVPyvw7Pwc-Qxs3K3fqBYJMbW3k_pwEj9TGD3nkMZk58AbfwUIreexTfeJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
