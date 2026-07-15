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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvG_j5wRpsMPaT6N3me0-4b7T79BMHgrYBnaQgR0tP_hPPOg2c7edciRaSDNxZONTVXygurEIgP3pk3Xt0R22huFUnsGs5D2BrJLpHwpzeOm6TPVjsZCd3z_n8qiJltyTPEUbpO2BkW1CxnlJAAqnaEIQDB-HsNgYv5ycZrEQyJ8IfU9AIrYRicFF_jitVtocZRtr0Ir7f1zBAcBinj0iLZM6PyGCl-YaR2qpz9HYHR-H3BXcgeM73iAVuvqVKWgQKDdnrPpKBTa5l-sU-iC4zQdXn4HC6r8iENHH1ChyOYdyeug_EBi4oQGKWplfV7FBCK4o42a3GTOBfsg84HBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=o4DG_J7nVQ2K7tJlMT63ljtkbJr6vLt2oNYdX9_Q9ez1QLeCy2MAM2D_iaXvZgrFaxunuZ1WGk5cp7FC_Cvwtu5LW0N1pT-LIbLNZxWGVkrk1ohWsJFZq0DK4-1pqjflASmKQPEMQJ9C6jR5ZXyjiqSnFNUqiRQn6PICCzbBGc0T-gm8BRyF0V0J4pyB7LGefiWpWVKF5MvFY5ZhQUS_H25dPA5FxaWuwWWZSOYpLC1NOpJA7E3qIcRP0UJcAOdwty5VMLiq4c4MIFktb_6Efhlo5aJUVu28W9Jy4SFgV1mIudLuQ5V9ndr3pXMlW-_Py15T6dECrHZdusDnXXQgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=o4DG_J7nVQ2K7tJlMT63ljtkbJr6vLt2oNYdX9_Q9ez1QLeCy2MAM2D_iaXvZgrFaxunuZ1WGk5cp7FC_Cvwtu5LW0N1pT-LIbLNZxWGVkrk1ohWsJFZq0DK4-1pqjflASmKQPEMQJ9C6jR5ZXyjiqSnFNUqiRQn6PICCzbBGc0T-gm8BRyF0V0J4pyB7LGefiWpWVKF5MvFY5ZhQUS_H25dPA5FxaWuwWWZSOYpLC1NOpJA7E3qIcRP0UJcAOdwty5VMLiq4c4MIFktb_6Efhlo5aJUVu28W9Jy4SFgV1mIudLuQ5V9ndr3pXMlW-_Py15T6dECrHZdusDnXXQgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ijAdfFjdwoGWscf9BgqNbLw4bx2W5l9QF2_ioJYUkZs8itNMM-lhXI61qi7V_QaJ_bbcXed0pSrjOlEyYClk4ZyJ6V88_xREnW7aYTbI21yWjFZ0FnEu4ujBloEyxZem_UT0HJXO4YImii2wlzYU24ANctjZoKDeicn9QEyL-FbOClXhHvN8ZAQpYvPmag3XJkAvPP0cfwD11wnj_IGOKvWpeo8X8ZnXtfa7MNMcUklJizVGl6euj1nbvOaSqiBqyQz6mmdRv-D_7Uk33pDYDOXjlaY6_KVzd3YqWUpveDdcVWKxvhjoIl4Bu3KkytDooJxzn-g9H4HTcSVeeHQbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ijAdfFjdwoGWscf9BgqNbLw4bx2W5l9QF2_ioJYUkZs8itNMM-lhXI61qi7V_QaJ_bbcXed0pSrjOlEyYClk4ZyJ6V88_xREnW7aYTbI21yWjFZ0FnEu4ujBloEyxZem_UT0HJXO4YImii2wlzYU24ANctjZoKDeicn9QEyL-FbOClXhHvN8ZAQpYvPmag3XJkAvPP0cfwD11wnj_IGOKvWpeo8X8ZnXtfa7MNMcUklJizVGl6euj1nbvOaSqiBqyQz6mmdRv-D_7Uk33pDYDOXjlaY6_KVzd3YqWUpveDdcVWKxvhjoIl4Bu3KkytDooJxzn-g9H4HTcSVeeHQbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=juerbcx8VVSQyB7Brx_2BdVv7QumJ0ziBSDFynGab1xUlyq9yErpMhxlXMEmTQZ_xi_1juyiAsomUKKEjW6cs52QkF5y9WjIG7A7KXXQok0k-mwzk76YLCA7QT7TfX4_EmKwvI25_1HoMhdaWUh3rKtLu1Al4hpuC0yLQgcDWiQuLdvna2vjHCOofEi2inda1Mzey858o613bmnbPvTAKi6N1fpxM4PleE1ax22kvZs2gUNZ0vNglg9aJxAl_vms9NYUMRLEAL2T26rQeh271EbgKghB5rRCpFKWkSisptN2L_f6HrYzaTzSFRAeQeAfE9d5EmMpGHd9vvBHNkYEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=juerbcx8VVSQyB7Brx_2BdVv7QumJ0ziBSDFynGab1xUlyq9yErpMhxlXMEmTQZ_xi_1juyiAsomUKKEjW6cs52QkF5y9WjIG7A7KXXQok0k-mwzk76YLCA7QT7TfX4_EmKwvI25_1HoMhdaWUh3rKtLu1Al4hpuC0yLQgcDWiQuLdvna2vjHCOofEi2inda1Mzey858o613bmnbPvTAKi6N1fpxM4PleE1ax22kvZs2gUNZ0vNglg9aJxAl_vms9NYUMRLEAL2T26rQeh271EbgKghB5rRCpFKWkSisptN2L_f6HrYzaTzSFRAeQeAfE9d5EmMpGHd9vvBHNkYEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=YrEnZ-sQWLkroZ9190rSlHb6G2JVUhP7sjYpDIV1qAdE14PgI2Db-wQ9S5JpJDUYEIEXFVUSYN5biebTn2GnQt_2C-JGgvnzyxyfN31mryKI9SVMRea0wCgVyhiKDjSL-H5mIUqXs3kJcmk0y3TxhpZyi7JLALnX0WSx64rMi8Y773XRoTwnemFO_l-nAV_2B3Q3B2_bbsh32mXo8rAogKSnzMfrqm_OzS1g8gytCjgVeg3NiIAIOYCVAEGeBNHN9IrI51xuhZBmZUIlemYPArPhf7PqH--vBbWkejG605su2zlHoV-3CUSxHV-SRx4wjgltFp1VvgsQ9VCldJHeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=YrEnZ-sQWLkroZ9190rSlHb6G2JVUhP7sjYpDIV1qAdE14PgI2Db-wQ9S5JpJDUYEIEXFVUSYN5biebTn2GnQt_2C-JGgvnzyxyfN31mryKI9SVMRea0wCgVyhiKDjSL-H5mIUqXs3kJcmk0y3TxhpZyi7JLALnX0WSx64rMi8Y773XRoTwnemFO_l-nAV_2B3Q3B2_bbsh32mXo8rAogKSnzMfrqm_OzS1g8gytCjgVeg3NiIAIOYCVAEGeBNHN9IrI51xuhZBmZUIlemYPArPhf7PqH--vBbWkejG605su2zlHoV-3CUSxHV-SRx4wjgltFp1VvgsQ9VCldJHeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUCoqMWmjldsuZWyEJdKcaYkaigKRGcnsH7MyF-enKJvNMQwrTw3hvsSExwELoELQgNiCajr18vnACfrzFuXugufkuOY0HJZyqvrVQmmfxKLvrS3wMK1DyJcNRJRSRLeEfMz4BU-M3zzN4ziftpC0vq1a0vXe-YUJGH7CXvTpZ2kocXamGAZglk4VdOKYvk5tvAyqEpKvtZbpUvbzMAjZzFM7835GOLI-EXOLborNETbqjgWuv_qT1-jpaluEGzsBBJpVDta8-ydplVcAAgcN7qf918Dvi9h76rpnFcULPTyLE87gmbU7ylYo3toghVWUeMBHN-0aDuQnc-6Uh3kDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVd1mtfDxLLsbh1QgdlXNBOJQWVVSH8-AuJ2tlDRPal7tdYO0B2nMNtbVO5k7aKY7AvnUtNrLrNBwNPpYg9C8DuysvrqZDYgrvXcFlFjD1o3DK_ootMSI6YfsdDBrduR5iRRIFdh_64Rv0wVo92XnR2GmhuiczSr9zNEZGjZXAAyKdmIByTxWHM0NhBQ1p4qHEsZOnLVmAckPcwDLoGLeG_2gcSJ9LyZzRLyH7rReZ2OVOiMQ8_NE-kAQfe8zgq3fRgMGiSLywaxJiJKdIsFhX7LH3mDGmBSFgqyTnf0z-gyhLRrHlMtDHgQGTLs8ZmFDHJdKjANkYlCq8tlI7YMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=RYD7uIR-AZ5NbncSqXcSCYKdDQFvC1Ubcjq0d_gQAj0r4pedheZQmY0R6NEeGp9gsRgjsvqUkbX9Rxhjns-HsA_DerdcPdr305BrJbFKlTDydtrfGx6Lq2W_Moewr346AXkcLuqv2azE_pC3uBxTAKtCKWVra2czx6DrmHcXF9ZcTpQxJRH9OIS5z8Qd8wTYYJdT4lM5JKO9X-t3TYKIgS8TmSkpsUQo2-WNAWHMI9tu4IBfi0MKXD7Cfb6tEwI56MsOJs6bPYAVtgg8f3weM34p-uRaQjvp_Ahezi3huBZ9bS3e6j7qP-EDKYiYHXcYWP-Sb9TtvCtMB-NCKd_BnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=RYD7uIR-AZ5NbncSqXcSCYKdDQFvC1Ubcjq0d_gQAj0r4pedheZQmY0R6NEeGp9gsRgjsvqUkbX9Rxhjns-HsA_DerdcPdr305BrJbFKlTDydtrfGx6Lq2W_Moewr346AXkcLuqv2azE_pC3uBxTAKtCKWVra2czx6DrmHcXF9ZcTpQxJRH9OIS5z8Qd8wTYYJdT4lM5JKO9X-t3TYKIgS8TmSkpsUQo2-WNAWHMI9tu4IBfi0MKXD7Cfb6tEwI56MsOJs6bPYAVtgg8f3weM34p-uRaQjvp_Ahezi3huBZ9bS3e6j7qP-EDKYiYHXcYWP-Sb9TtvCtMB-NCKd_BnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f1VYVZE95gL4kEB8gmUjS8yr-iMKhMnEsKkGgl-LDqUQm4I7G-RYTTKZfddsO9G0JFv1rEaWbyPTYFZj_vhwXKfzp5pPOD-z0BwuXbxpDWg01h5IPYu0h3jFfaX-NzvCR1FaW14zwf-yG-hAL73GNj9YDMRT88sAtrlPtke9izXDaGU87l97oOnBSOqaiECWcVv90wNQ4cQIH0gvX5DWw5NyoVrxlIK-nM-rU0uNIvjs15hW0XhTC6Rvj1EIErVRoA6AHbRKnz_HAOaCVo-SVMdGxy9c2ri63WTDEu3jIRF7eq4uwCJvUcusJ6Qg-1ZqILV-6oilIgHPzjXrRLfixJX5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f1VYVZE95gL4kEB8gmUjS8yr-iMKhMnEsKkGgl-LDqUQm4I7G-RYTTKZfddsO9G0JFv1rEaWbyPTYFZj_vhwXKfzp5pPOD-z0BwuXbxpDWg01h5IPYu0h3jFfaX-NzvCR1FaW14zwf-yG-hAL73GNj9YDMRT88sAtrlPtke9izXDaGU87l97oOnBSOqaiECWcVv90wNQ4cQIH0gvX5DWw5NyoVrxlIK-nM-rU0uNIvjs15hW0XhTC6Rvj1EIErVRoA6AHbRKnz_HAOaCVo-SVMdGxy9c2ri63WTDEu3jIRF7eq4uwCJvUcusJ6Qg-1ZqILV-6oilIgHPzjXrRLfixJX5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=i9iuLTqlXs5V0NZKlZntpE480EvefbsZd7S23C8g3BgSPjnkNbZIOjbPl-rmUggwD7gAg6jS20Gc0YLSnGEdhS0iQ4Mwzc7tY994mfzuBeSSfctT5t4AiPETzgN6s6VS5V6LCJ5QvM3JB87S3ErYJQ742bR88C9APW2b0vffYmOXWa6AGThXduujkd5NLdcm4Zp5CKU-X2n7nRbWuqrEkOZ6r8CMmOLy1e1nj1ps_Tv9rFAl68GrIssgh7yO6ZPqrGOtwPeboWLf1-g5s5V5zrLEOwbWm1LPQ3SaciJjaXMjW9wqP10ChVHpORqVxj-kq-w1rVw0sMBl0T4kVSGh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=i9iuLTqlXs5V0NZKlZntpE480EvefbsZd7S23C8g3BgSPjnkNbZIOjbPl-rmUggwD7gAg6jS20Gc0YLSnGEdhS0iQ4Mwzc7tY994mfzuBeSSfctT5t4AiPETzgN6s6VS5V6LCJ5QvM3JB87S3ErYJQ742bR88C9APW2b0vffYmOXWa6AGThXduujkd5NLdcm4Zp5CKU-X2n7nRbWuqrEkOZ6r8CMmOLy1e1nj1ps_Tv9rFAl68GrIssgh7yO6ZPqrGOtwPeboWLf1-g5s5V5zrLEOwbWm1LPQ3SaciJjaXMjW9wqP10ChVHpORqVxj-kq-w1rVw0sMBl0T4kVSGh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0DZvVdn7YXUd0gcNJHIequ4n1Q6mrnde3SW_OhN4eewbDpfzl--N2NH27sl0kP_YoE9hjU1B1B4tnDbkTqLkbNNLHinap392-kLu5P3brlujChPJJ7mTM70ZvrXzLB287UlZlkgwomH27T5ubvXYFLzwk6zcLVvFU3jxyRAaEnhxAwdCQ7vqJs4Dt6xH9k_qmB_kPZIbNLQ5RDoRWwSg50OqQgFGlSdnEQe6hN-INc9qKgJk_IsFZEuI2r9o3x6_xjvIBtwjbu5XeXizFxOv-DI1a9yLlT0uXDGC1dz06gkxhDfNsxTuuqNZwV80iIB73viJpfsFw32-pz-_eN77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyv8fW88eTq5q8_CBOx_CHhd52rq-Zg8XObXly2IYYD1rnswLwKHvB51xwj5vCb9tmZ5ij7gy85vnGb0_dUtU2kB8vPx50VzB2HTYsMd9FuVVI6xTSXNoV4JtzrRX4LPEul8juthb0giHvjRIE_S_-9lu2DkwMZw7g2FqzN_XVnCbQStBvAe_xHsUXJHqVwpVGVr7oWJgE6bgx5ra4jXCdjG8xwnvRiFF4FKhXAw6VGb-YJ_gjm_TxHEjdIO9bH2wmCJiNiWqpPCt7AYOMpzOeCFSIiZvAW3pt4X6Q1tD7bltCiLmPvBmXivHUsxk8LbfaE9yWltljSM4TIdPClbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=NSuLVgFg-s_heR2j6-O9qXSwi5R9GHHaqvmt_28M-j2lhZ6NtmQL8vn2ExLWXzb5MFLeI-LZokHx7VFfYf0F0a34ytKqTv-pdkiNs_EXe5VrxrMwvvvMNo0okCvtxmY0R8u6mDUUuIuukJ0HJmBz9hg3TLKFM-vehDtxUV2YCpyOdNKwMK_1ZQgQ0VILI37Vy56PNMEyR6vb7zHCFhmj8OtzXzCjX0UiCxg7ITZCFvnIHGSmvZs9ERGAoIRIU3Jrurlz57__xWpd4eg5nsF_pzqjlYdhY9vWqtpTzIVI8ejgn5-gfbi_KuNaS2eaodUVtuD7CcGM1CTAKgYlGS73Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=NSuLVgFg-s_heR2j6-O9qXSwi5R9GHHaqvmt_28M-j2lhZ6NtmQL8vn2ExLWXzb5MFLeI-LZokHx7VFfYf0F0a34ytKqTv-pdkiNs_EXe5VrxrMwvvvMNo0okCvtxmY0R8u6mDUUuIuukJ0HJmBz9hg3TLKFM-vehDtxUV2YCpyOdNKwMK_1ZQgQ0VILI37Vy56PNMEyR6vb7zHCFhmj8OtzXzCjX0UiCxg7ITZCFvnIHGSmvZs9ERGAoIRIU3Jrurlz57__xWpd4eg5nsF_pzqjlYdhY9vWqtpTzIVI8ejgn5-gfbi_KuNaS2eaodUVtuD7CcGM1CTAKgYlGS73Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHDtu047zLHow5uptuWPJYuxIHDjDMqykNj81r9ftkxvajNqzAirX-m3h5S5-nogv1ZNc0N5Jbv3yZCOaNM7_Y1IkQZYQR_VI0E6pjg0pXv-3nZIEkSfL-mu8wIyzvHKkcXobQuLUbu4FO9mSnK-5bOr-BG3zqYhU-yOOtzcQZPp1tRi1C70YT_VRsBlgyQVRnjempgmYYYJTbWdLnbX5j_5vP5gozpyhOCn5hhANuEF_Ge_8bbqw9haucBlYaGW2x9FoA7Oyba-UfT7nlifGlxMpIsJv4_9-7aDwGnEEskFv47oVNT59Ik_Bwfspqjk5bmzSEFh7J1jpLJzAHWPlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA0r8l_mXdIZ4x2dac-BnqkRWvawh77ac7w3x5xF5aGjO3dM1iDunCRJhDGZnZZVZPo-QM7Q-tBE4JOd2S8rygZ0QwCqqqQWzXTCC-tYW73abgoX0PiztKQOThxvzFO2s1UFWSJnaQp9FXyZo-ts4y2BcPW1OfRSupl0KFAjyDqy0ulsJ-gF4dLvM3Sftm21MhXGuiEfd2PDK0HEmhStvy3kjCY2wQjOCt-BTzwU70Oia4-j7sbIZuHkYWpMO95Y4HWooRSAxSZgeMoJleBVxnVXs-hEXxYFO_q9y8Zxe5mpc6dTYT8yjQzoKSxcbBYud3djX4vMyEb9V7l-GITPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=XH1Gf_nRO7RciE1Vuh2uPVG-f0vYa-yRRIZoQbP5KKRU_S2IbYtQZi3RET9uUQ3x6mEBn0_wsv08ll8qAtEmyNCvJ5xJThmtrjFODFM36RuySfdxoPtXwkxEOZH3pAfr-KlotsXRYR07NcFVFv7Xz4f48zEUrbJwczwi1oZt7JHZgxCu8Oaajxori_0_p6gKvmVrPAGDlT67fZZZmAphnaDFa9Wff2B1CdNiweQkO_mEaeiCdW6sn-EgfzWLc14ro4YZYEeMI_PlTk6QbRkJK7JDTeLC0B86Fgf1lU0x3k36tTGbYomBSipQcandgcDoFpm8BI57KiNh2zH9yKiGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=XH1Gf_nRO7RciE1Vuh2uPVG-f0vYa-yRRIZoQbP5KKRU_S2IbYtQZi3RET9uUQ3x6mEBn0_wsv08ll8qAtEmyNCvJ5xJThmtrjFODFM36RuySfdxoPtXwkxEOZH3pAfr-KlotsXRYR07NcFVFv7Xz4f48zEUrbJwczwi1oZt7JHZgxCu8Oaajxori_0_p6gKvmVrPAGDlT67fZZZmAphnaDFa9Wff2B1CdNiweQkO_mEaeiCdW6sn-EgfzWLc14ro4YZYEeMI_PlTk6QbRkJK7JDTeLC0B86Fgf1lU0x3k36tTGbYomBSipQcandgcDoFpm8BI57KiNh2zH9yKiGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSLGLe30cSl_-MvBun_I9SNOMT9j7yaUEfqwoPwAncm8Wq80pBy0iY6SedfhSHhvhvJOVwp01AhDKCL-tNh4dGWc_ke5m4bchLiz2mFXbnnzkIFJorOZaTDWfrzlQ0ZIiUd71kKPnGgSguQpcdK1_LgC29A4taxGhPjknw9mxK_pr_n8irWTAj5-hyb6P3jU18K3CYDZV18zuZAomEejv4igqNbX4hBvcYkRYLpMV4zh90-Y1XgLDAY8gKN1LqAnrsZVdoziR7AukeGDwb9dwhpP1QttD55GQoDcGGeri7_4ktzDUgs074oszgv84DPgLTwwLu1P3Udx-IYlg37jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmPPGDK4fYh1w-86RxqRXJqIJu0bdy4FB-SO27mXMQDmnrkDHk8spcx-jP2LpJjG90Jg16ERrtnNzypK2TJK3cKxxW-_9oNrq_oKAurVZCLq1HuaO0Z8f3EpgYpfqp-fP8ZLXsNSiGdQg0zTqtuTNmIO53XeXpu9NtEmHC16fRWn2PP0XSfn6m3jGAVve1B-r5U-9FBEXXXEe4JrFNURNjPv5h6wKFnvHHsPCHC_nt4pmjeUz2kQpdqXqOv83tfEkysdG6r7OhGcNtrUukb_f8cFKiK0IoNKBpl7rSsmDlTlw5CbjvO8GzyyBto3mYc8-8ENqwaNRZda-eVXXXyL4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Evky2JUbEMbcPmRMuKz_bt1eT_sCNOocX8M2wflVG_zxF7Dqzsl0s-Q20X8dXG9EfCEEZIVwJZDgKnLIdYEHYTMds1bZ7ijFVLMtqPwQt4oBob6_tLKtWAafBCp3uR_ryVBKGKoN7Cha-QbjiosjGaX-oD3YuXupr8AgMdbiWl9C262SeaogmVQT-OpykAxIv5tZVL2HtqD3NfY3siylaGOgnQnFlXESxZT79G6FKsrzV-IJNqkZAQD2_ud9jT2L1AeY5DQTp0TIDlESC2deiy-mketIK-RsgkFZj6DjNuTdQAPCM0x6ssK732R0diOWgyUqc7GPWGtqTw_lexqEYxB-s2giotH5ZFIBrRpsLq1Iojvb67gF0HN_mKKFLxjW1Bx3sMLpVM461bHcuks9aFLtycS2mrNVGXrZEkSmmZA7-weQxRVMO59Xyg3P-IEXIBtuGisbdo5WSP_QgoeEsvRkraJSSUoT76c6IWK-rmhAJc0bpLfdLKT4t7ao6PVBxQl4I9QUrjO4v7MQXqS706G5Cje5C3CcSSpXs0UWoM6HZdXjrMiZ0w-IzevW5he9SKIT6aFwxNUHsCQC2Yi4E0Z5fTARU9XarxQ9iQoPSdmKxwyPIgZcgk6jIb54YvH4eLXBdyh6L1jwTi2X91hmvyVowEBieYr_wdHfty59KkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Evky2JUbEMbcPmRMuKz_bt1eT_sCNOocX8M2wflVG_zxF7Dqzsl0s-Q20X8dXG9EfCEEZIVwJZDgKnLIdYEHYTMds1bZ7ijFVLMtqPwQt4oBob6_tLKtWAafBCp3uR_ryVBKGKoN7Cha-QbjiosjGaX-oD3YuXupr8AgMdbiWl9C262SeaogmVQT-OpykAxIv5tZVL2HtqD3NfY3siylaGOgnQnFlXESxZT79G6FKsrzV-IJNqkZAQD2_ud9jT2L1AeY5DQTp0TIDlESC2deiy-mketIK-RsgkFZj6DjNuTdQAPCM0x6ssK732R0diOWgyUqc7GPWGtqTw_lexqEYxB-s2giotH5ZFIBrRpsLq1Iojvb67gF0HN_mKKFLxjW1Bx3sMLpVM461bHcuks9aFLtycS2mrNVGXrZEkSmmZA7-weQxRVMO59Xyg3P-IEXIBtuGisbdo5WSP_QgoeEsvRkraJSSUoT76c6IWK-rmhAJc0bpLfdLKT4t7ao6PVBxQl4I9QUrjO4v7MQXqS706G5Cje5C3CcSSpXs0UWoM6HZdXjrMiZ0w-IzevW5he9SKIT6aFwxNUHsCQC2Yi4E0Z5fTARU9XarxQ9iQoPSdmKxwyPIgZcgk6jIb54YvH4eLXBdyh6L1jwTi2X91hmvyVowEBieYr_wdHfty59KkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLH8vt3akF2o0xUnpJ4CWWIuvLGJgcQU_5OG1NiI9dVokuvrJ1W-h6fPO3ekdd6vAi7MH0g4SnJdgOwcM7upXp0km4DoKXzbKpmV_Ze7JmeWGIksphIBdNMtUMICTRsNcjNw2hOYDxbVxcUvp_m1wyEDMWsurpw7ov2nvby5SDHRKDVsIxVhPFNBcw4umeekuC3utZ-YNPLWdLeYfVCYNsujdC9xtCvUajoDvKXBPyMA1lcIKGG2m6vrbVSywpLVZSsD7pt1btjZQB-EVFHoyQv61vWWocbhGEDTnTKuUmSHrfrLS5Tm0sDcsq5NFLemkVivXIbo2HYoL0EHfiskWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV5UoNRqrhYlaUJFEjpH4PoX40yKfVn7WGoVodl_LSnK_4t1EgChsO8qdqDRIbp5Z0yxoItaeNUAZQ1aGhZ3Q77Eo6f8xNDDHfmsg_XLQHjFduBYy_8Cld_5tzz0H3Up5Q3zbaxf8Mbo-UflkFYy-SVceJUjKQnAg_o0QyzKHpKknHuOvyYoESu30lRLiT-RfzTXw-dWMIuhy7AOcvf2Vl_T9RooIxVs4qGQXdddKBs_Q4JRaJavzbC6-93fVbEP3I0MZ-_VbB-XD-8z3n999sO9P1wnoYU8s0ptRCcPmdtsspW8MKx50qmQdrebljvdgvtoH1mHdDc1I7sEKVXkNKQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV5UoNRqrhYlaUJFEjpH4PoX40yKfVn7WGoVodl_LSnK_4t1EgChsO8qdqDRIbp5Z0yxoItaeNUAZQ1aGhZ3Q77Eo6f8xNDDHfmsg_XLQHjFduBYy_8Cld_5tzz0H3Up5Q3zbaxf8Mbo-UflkFYy-SVceJUjKQnAg_o0QyzKHpKknHuOvyYoESu30lRLiT-RfzTXw-dWMIuhy7AOcvf2Vl_T9RooIxVs4qGQXdddKBs_Q4JRaJavzbC6-93fVbEP3I0MZ-_VbB-XD-8z3n999sO9P1wnoYU8s0ptRCcPmdtsspW8MKx50qmQdrebljvdgvtoH1mHdDc1I7sEKVXkNKQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=R_7D5OCe-2XKBdy3_ceVLxKWiz67Hz98s5j0FVffvl7c01NvgxSGFuZ2xZ9AyNEHazyP6VrIlEpBEaWpIUO1LUtvUTheb2kUYXorW0yMS2blcH2S09DOiqf7L6PXjoYTjsbZAUKvpGXQWmPX1u2k8t1nh3qELmStWkV1yo8MzuPBIkC8pMSFh_8eHaSDhFCKVq6UQQL8oAJ7PJtt-ONKpZwiOL9OaSOVjzLpatagKAOxtFa9CdFEbDy59F3ZLvmBXjBe8jLVU6xU_4PA5jvBumI5kP3mrsGecH9CM_ZhbnLUjnUxXknnAe4W0HzVtr5900TB0WFJIjESpsnntqitTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=R_7D5OCe-2XKBdy3_ceVLxKWiz67Hz98s5j0FVffvl7c01NvgxSGFuZ2xZ9AyNEHazyP6VrIlEpBEaWpIUO1LUtvUTheb2kUYXorW0yMS2blcH2S09DOiqf7L6PXjoYTjsbZAUKvpGXQWmPX1u2k8t1nh3qELmStWkV1yo8MzuPBIkC8pMSFh_8eHaSDhFCKVq6UQQL8oAJ7PJtt-ONKpZwiOL9OaSOVjzLpatagKAOxtFa9CdFEbDy59F3ZLvmBXjBe8jLVU6xU_4PA5jvBumI5kP3mrsGecH9CM_ZhbnLUjnUxXknnAe4W0HzVtr5900TB0WFJIjESpsnntqitTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNl9o-fe32pOunPmukyiXLrAs4cxvNr-x_FhGojcZ1ZMArbXmV-igtGJVku86fcniGHZ9pC9riWVD5fHOaZ7DvcrFOhMJje_z6zLq6n2jXTIZM9jzu7Rm73ACAeKe-c5_ZdTWVFkqPeQK1cSmgHgz8GpoKSZxUq3StZmA8khaWKYiB7UtFBdb5taVWVnESBaijvIj7NBppBWJg8PgNQzM_fWb6IW_irr1Nja1F16shdacsfjtRtjMQLYB3V0cttqJbNJap6EAv0WQhWjKYEvCpVQmijMcDZqikCQErxveFYIRTJg_2MWqVkD8ZlPiIJjmjMTCZkDjn7oaP8gQWh52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=eG2yq9etlS6wUN8-mkXYRdBTPMbB_dg0gjBLAv8fqf8ml6zsNWy4OebWncSMLJQhV5RJMHGRCm5sjfpg7pycYqP2x6aWqUE1bdaA2A303tbGtT4giDA4ErFEN33W1VXfXTROlvWPgoUt6dW84e8jwKV31zxzDD_Yd4Ou3gqRLRMrdFEVEqvPDN8B8lSSvXqKEWJ6CdYFXuVpdcqEPuvtJw5C5l0T8XsW0J4y0hhLMuZUHWt1JAA5Z73e4j9JP7msyb8SowH1Wlytb4aZIp5bgOjeMZ-GURGwWkOXR-IjZDk5-qUdGe8cs_CE4Z9aCl37gKqM8cqKYjzjQnM99HlT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=eG2yq9etlS6wUN8-mkXYRdBTPMbB_dg0gjBLAv8fqf8ml6zsNWy4OebWncSMLJQhV5RJMHGRCm5sjfpg7pycYqP2x6aWqUE1bdaA2A303tbGtT4giDA4ErFEN33W1VXfXTROlvWPgoUt6dW84e8jwKV31zxzDD_Yd4Ou3gqRLRMrdFEVEqvPDN8B8lSSvXqKEWJ6CdYFXuVpdcqEPuvtJw5C5l0T8XsW0J4y0hhLMuZUHWt1JAA5Z73e4j9JP7msyb8SowH1Wlytb4aZIp5bgOjeMZ-GURGwWkOXR-IjZDk5-qUdGe8cs_CE4Z9aCl37gKqM8cqKYjzjQnM99HlT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=EFk4LVoNzWDKgS8ALTndOQj7EsSjvIjgLF9le_gkz340jlSWsVTGvE1t81bfeaf7EpP20jSBLmvPdloY5wI-iRUqrPyje1Qyua0VAxPNEVw5JAJb8Ph8vq-9WZ7Hu3PmveLPzDlnGEG2V_2iyYOCUTHTAxPywa1v9MKTac4KeDdM0AfiFAg-vZFKKu1VETk_76nvoOYHK8zeLn1tcRM7eM9buY_1cktfj2hnyyUsCuyxwXOorf5BC7C2BHoYo844XJGDpJ4JqjtCSiDM8TRxFLfrbzB9j7Z3N96chLJww_lJtrsjYThzUoSF2MtPRWBhJpcn2UUw6Iexax_jlw2O558NEtnaCzaTLuL8mA4219cv1IzCS68xbfHMLlJrFPX4MKln0xEXT-gXQfriCQ7lka9_YOmv_eugYjmZoOKDp4oR7pJiR8n0narBGCIvFG-i51YcsF7c1_ugiO1KxjC1IPK-wXTmdzcTIxM33FXG-4ErD_3fwB2Cfok0CSMX-8QOXDQF-UuaNVKp91xnTgBvM9Gx4OMs0ZHgJ-PpvG3pe3g3-NqX1NnDzG6Bf7BEkAQzCmWOkx8vDBu3hc4EYPlM3C_A-1PxOH2SAEc3uSOCSG8jJXkhszpdksceQBJSmRojN2QULsvf5pDfJimsmwewoCJHo986p6VpWQRIsUNT3FE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=EFk4LVoNzWDKgS8ALTndOQj7EsSjvIjgLF9le_gkz340jlSWsVTGvE1t81bfeaf7EpP20jSBLmvPdloY5wI-iRUqrPyje1Qyua0VAxPNEVw5JAJb8Ph8vq-9WZ7Hu3PmveLPzDlnGEG2V_2iyYOCUTHTAxPywa1v9MKTac4KeDdM0AfiFAg-vZFKKu1VETk_76nvoOYHK8zeLn1tcRM7eM9buY_1cktfj2hnyyUsCuyxwXOorf5BC7C2BHoYo844XJGDpJ4JqjtCSiDM8TRxFLfrbzB9j7Z3N96chLJww_lJtrsjYThzUoSF2MtPRWBhJpcn2UUw6Iexax_jlw2O558NEtnaCzaTLuL8mA4219cv1IzCS68xbfHMLlJrFPX4MKln0xEXT-gXQfriCQ7lka9_YOmv_eugYjmZoOKDp4oR7pJiR8n0narBGCIvFG-i51YcsF7c1_ugiO1KxjC1IPK-wXTmdzcTIxM33FXG-4ErD_3fwB2Cfok0CSMX-8QOXDQF-UuaNVKp91xnTgBvM9Gx4OMs0ZHgJ-PpvG3pe3g3-NqX1NnDzG6Bf7BEkAQzCmWOkx8vDBu3hc4EYPlM3C_A-1PxOH2SAEc3uSOCSG8jJXkhszpdksceQBJSmRojN2QULsvf5pDfJimsmwewoCJHo986p6VpWQRIsUNT3FE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwc1M0lDMNv5g8Xg9m-KeU0s98W2iKMG5ogepyqi9U4CKeeCbtBZVU1s_aACGdoVXpSs3XBJFxmh_x6QrHVkC8ec-JpBKkljiFGfCICGyjtQWeYYKUsmxCiVWVG8E2Q0pamcgnIPpD7pWSp3KZs2ZJLIzwgjEwzWIf0GDzR8OosOt3xRl97kRvtm7yvEvbwz1DNogC51rEKtUMprf3vsl6dP92VqJGG2miqA4ZmbcJHa2PmkiRuYMpk5iXhF1bdE0prOM2JNyfmFrGevMWwlpJ0yz7cYxo3I4tn_wBcf4DbHesVhMmnfkRTGiWzmSmh0v4NFNXNFmgHac06X0qQBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUm-9Kte7woz-_dcO2qV3TCBjKLw_NPqd-TbrmKhRD-_0IdZ9op-VIqbWtcp2pbm7WVO_z9I4xHvJMsoGeQHMvlNRvPqO9i3sgXDUWV6dNE1VZlMa67mXhwVZH2jI2ue_QItPokvi8C0kq38WnkYx9ZUVJf1l8Wu9UYLhFth8hweor552bWmNqG8idjU5w5qFBk9UaD6owXjNP-IjySjSgp0Da1w4xMKhKd6PY3MxGsY635uqv8XfabcT-fZ0YZYWh9Dwl-EKPzIzoO6TuDf2GuXPR4hKCHhad6iGJFWTjLihYkHjfgDv9XbvGXawH-EEhLTr00bNejO0GP1mSw-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DALdI4LufhXwaeILU_uR7SDSi7fa53j7zXmfBgINiYsPGIwnVIGzwkxUtdnYEQbBFodt0wHyf3YoMnWDhhX2lMsCdD8wm3HqMgq7ayn1wpjRu9FX2aL7Qwo3N9VunrjIsVIWYl1kfzddl5vBrbHiAeowQQr8zwOkaBb_TrBzI5eqoi_Xeqa3dzCA_TfzAhTQfJ9moUMQb-KTY_m3g0gbPn5WRBpEzfzjJr7v5RKzzT4R7nBIK66YOG05qfbKZoGsmT1Ni5npFW7fCq2iAOk_K7oYeVVBMhCPDPr9U3x08y-Hj0tCdSZN_uE_JnACgl1WN3w8nUczFCmLwR1S-3EyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYfKhZyzK8KmetolpeWU5Fq8ThlTN7owM6xxgIZ49BnmeoAz1U704qBg6QiWhDl7NMe42OX6jmRwLoBH7Gq9IGIWoUfcOIjxkofCKnMEXcry1KHSHVpIUEexf1Qyhoxk-m3k_YZ-U8u4OgQPmDEnCQhUdEXB8kraxGY9jbL_bMWopLBUbmsmVYDTX2T2cb_AlEHmyosYYjCU1yshhw0LFNG40EzddiKx3BKAa1Vlx05pFxHyUZRWbsInXYbpSvfj3c4ZZ8vxDF8kSSDZzDxUAOb9XXV2781NFk2ZboQFVbebnfE8CXaWfIfubh9blp_AKtGvWqqrcYR6YUA5gL5jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNn-bDYxido441Rza1QgptTynoLsGMPd2K3_NGz4MUcTcl9Me-lyCDbchEQhBS__Qp5bTfpyhmf9ss98njO25UfiW-1auJhPj7URYF-rJw4x6ntFV899J1m5cSKAxE3Yo3BDGSsdCcDgU0TBMf1pTWlnNt5kvYTG69k4Vd1lHUdky90sspXUoANflvIjUhSYqdbfpk7KTveie1Qeth9s4oSv8wahsUgji1Fe0Y-tGA_huFBRASzoJ8WNlJ8UhDMDIBYAfxQlzAPr8J-KBfYBfeqbYdzjGtcIrlGeGEeM-UpQfZf1WCI8fteG63FR0prkPuYr7o6nsj6h1x2dYqxHuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAaPewmjGjVcArYt4MGelqvk9dm-Qfp_LCooi5jI45_7yqpaxtGrr8d4cGHeXDE4KP7LQZZQwfP20esNOmax79OUrNZGr4csjvEoMw9IwOYBBsJ06iAfFAk8UBO3Qi3BZVe8PDZHnvhyLNHxxoKRz92Oexbfcy-ehT-xw6l_SounWxz5fCUS86TaXR3QcY5OmKnMX1MexUVFGe8o6oP5YM8GSuxQmd3jQ8haAu33AE7ApENEFi3ZE6sxlhwuwzX8UzyGtbsoQ5B9mcco_KeduMEheJeQR14MXPQBr1NIFQmuyLSLUsftXuduBmP1HX2u58LDw9290JfxMRF_1srHYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5ql6BIEtaK6H6ZEPvxW9nFeuSvFwAhltGMo6R2Eg8w8LIhODdWRQmZzAbmfPNs_c8-8AD3pnzqA04gnBh1uumb2jhTsysDtWQb9CBSXqun1rzM7NIdWI0rQkYbpaz8_lwhOFmkrVkVSY0U2JYXzxFpnQMc30orhgMS7sGJuormdTpMRtujffkK3onWbe9QvoS_8p8sljJ0CbLFU7Lqt1XS4xaiTIRovUL0RqzCMnU_S-aIghgXvJvR5FkB25NzR79Ywympa1Yh_yYYoEYVCrEBzNvfOicgxnJyirWHJFxT5nISRHG-0w6gPihurcjsTgFwv1WVuqanwO1NlPahbPVVEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5ql6BIEtaK6H6ZEPvxW9nFeuSvFwAhltGMo6R2Eg8w8LIhODdWRQmZzAbmfPNs_c8-8AD3pnzqA04gnBh1uumb2jhTsysDtWQb9CBSXqun1rzM7NIdWI0rQkYbpaz8_lwhOFmkrVkVSY0U2JYXzxFpnQMc30orhgMS7sGJuormdTpMRtujffkK3onWbe9QvoS_8p8sljJ0CbLFU7Lqt1XS4xaiTIRovUL0RqzCMnU_S-aIghgXvJvR5FkB25NzR79Ywympa1Yh_yYYoEYVCrEBzNvfOicgxnJyirWHJFxT5nISRHG-0w6gPihurcjsTgFwv1WVuqanwO1NlPahbPVVEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plAc7801WVkNKAS8HRzwSxg5xqc27CNtCHeQFuzYrZ9DFT3GtlP6TsNZ5zVcrZsqRJ5vLwvnoAA2DblN0jAVjSc68Tny8wl2Pig55kp37VZE6AqVW1oPPmwVqnf1JzMoD2qHpC6-Vvgq1biCwLwd53qEgJkGXdvS1BpSzseS5tAiyTOZF45zC-N-i8u5Z6zggNkOkrSn_FeRtnSz3OT7itF5e-TN8NbMAU32Q2pG7cpxnCOIfzuB9JouH9ZDpsKSL-cLDwXNugof-GZKo2VzSnbLs-yUIvBRi_RCruiFO_rpVl8rRPPVtzj0xFsDn0K_Wwlzs5fjA5jbH_cdW0rz-RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plAc7801WVkNKAS8HRzwSxg5xqc27CNtCHeQFuzYrZ9DFT3GtlP6TsNZ5zVcrZsqRJ5vLwvnoAA2DblN0jAVjSc68Tny8wl2Pig55kp37VZE6AqVW1oPPmwVqnf1JzMoD2qHpC6-Vvgq1biCwLwd53qEgJkGXdvS1BpSzseS5tAiyTOZF45zC-N-i8u5Z6zggNkOkrSn_FeRtnSz3OT7itF5e-TN8NbMAU32Q2pG7cpxnCOIfzuB9JouH9ZDpsKSL-cLDwXNugof-GZKo2VzSnbLs-yUIvBRi_RCruiFO_rpVl8rRPPVtzj0xFsDn0K_Wwlzs5fjA5jbH_cdW0rz-RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=iK-4TgjCqcF4NmxtTl21s8JhhZKE-f8Pd4RYWlYmtqvOIujjYkn5tnCvNkJ8q7ymk0Jbyln7sj2elrCosJUAigQ58ZGYrj4bhO3RQK9VpZwb0K32M-FSzrUrJ5NO05biINW9KjR-L27GK4GPl4_5-2XO6DSlPJ8m4EYPcpoT2ZgmVe16OeyYabaU4ebtTfdxc9pds8foPUvkpMs-iHAaPZmy7LrSj02-QT5s6l0ZYwxzBcFrcVrxEP9F1sXBb4ovGKYhfvoUvk8cz0S9hkQUoT8qVGpM4DzUkiGzeG-ExRdD3jW-7FPPxwgqFgJ2RvvaKTDPOsudnMo9k_9tezJCng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=iK-4TgjCqcF4NmxtTl21s8JhhZKE-f8Pd4RYWlYmtqvOIujjYkn5tnCvNkJ8q7ymk0Jbyln7sj2elrCosJUAigQ58ZGYrj4bhO3RQK9VpZwb0K32M-FSzrUrJ5NO05biINW9KjR-L27GK4GPl4_5-2XO6DSlPJ8m4EYPcpoT2ZgmVe16OeyYabaU4ebtTfdxc9pds8foPUvkpMs-iHAaPZmy7LrSj02-QT5s6l0ZYwxzBcFrcVrxEP9F1sXBb4ovGKYhfvoUvk8cz0S9hkQUoT8qVGpM4DzUkiGzeG-ExRdD3jW-7FPPxwgqFgJ2RvvaKTDPOsudnMo9k_9tezJCng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=rcmvY1nVH7jqb1RfI7kaOFG0tVKczO3CcaJItGdmN09QxTb413rqc07TMG4E_RRg8d7-SZ_H7deHjsxwA8JmRfU64cIFsOJP8nd1L5Kp2QdtOgzZcyTI4wFigDzphzc8DSL5vqbrpvpKgusHzW8hIvRGSCK9XasXWdGLFpSNhVvG8U9SvNcWAVekx_wWyc-NPruJSjMK-zswrgn4GF6V40iFHifzkGeE94BdHz-ELvojuFPKxXjJo_hEVzKJ8A0VOTpLMdoBatkCJ3an-rdAM07g2Z3oi9vby6MmNWttAI1J1HV96PFjqGdnWM-pxtkF62_hSkWrb91oOhJ84Z4x7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=rcmvY1nVH7jqb1RfI7kaOFG0tVKczO3CcaJItGdmN09QxTb413rqc07TMG4E_RRg8d7-SZ_H7deHjsxwA8JmRfU64cIFsOJP8nd1L5Kp2QdtOgzZcyTI4wFigDzphzc8DSL5vqbrpvpKgusHzW8hIvRGSCK9XasXWdGLFpSNhVvG8U9SvNcWAVekx_wWyc-NPruJSjMK-zswrgn4GF6V40iFHifzkGeE94BdHz-ELvojuFPKxXjJo_hEVzKJ8A0VOTpLMdoBatkCJ3an-rdAM07g2Z3oi9vby6MmNWttAI1J1HV96PFjqGdnWM-pxtkF62_hSkWrb91oOhJ84Z4x7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=h6f-gxynve2PebrLsjQ05CminrYETnc2ZRQZJVahuJyuwKlnnqDexvJLy3lHYU6O4GKWEPCcAsUmYlvLfe3StkIiI6vdkWibhuTzNzMHeM8FfK1sIGtuFj32XyeOQq7JNXeB5bDqWWqFyv_G_VUv_38Wxf0AJ__h3bs-gJMuNCVfC94ZRSlQimqNHBqrjZ6UxAxTcoi710LUEfSD1pJ7bJ1lLG9fwX-0-OyMY5owUONlSiS1Pn2kwMcKVW7uXh8jBoINV5mJ0QZN4stHlSjB98atP7gO6YAvnAZKcWZZSoefeN2eYs1bKNtdQrwmnb6ILLvLvLuOB7mvPoS3-nPgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=h6f-gxynve2PebrLsjQ05CminrYETnc2ZRQZJVahuJyuwKlnnqDexvJLy3lHYU6O4GKWEPCcAsUmYlvLfe3StkIiI6vdkWibhuTzNzMHeM8FfK1sIGtuFj32XyeOQq7JNXeB5bDqWWqFyv_G_VUv_38Wxf0AJ__h3bs-gJMuNCVfC94ZRSlQimqNHBqrjZ6UxAxTcoi710LUEfSD1pJ7bJ1lLG9fwX-0-OyMY5owUONlSiS1Pn2kwMcKVW7uXh8jBoINV5mJ0QZN4stHlSjB98atP7gO6YAvnAZKcWZZSoefeN2eYs1bKNtdQrwmnb6ILLvLvLuOB7mvPoS3-nPgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=lME1yXr5pPflVTP2Ja7tyfjQH9j_9daf3pqbs0YQtm6TII5ciwkzI1dNcFF3Jwmi6-GWzvgquHbclCLfXS4YpLXnaUCqG_c88dkSomlwmcbD9ob4ZMyaIDLpc0OkMSk1vM-BvROorcy_ylmCTDw8G27pVFNo9SKGi1WZ3v7hMFoY1eIZKj2_YL4rlAFa9D0pSxD-wKlw-VY56YgfD3NjGiioWmhiInIQGI_MVJI_k-iDTkJOwpNSUg4MxUctAJg5pBBefmNgzUjGDhNqga6nAWEdXREPQW3x5hc9ooEBDCP6N8G4e9MXY7fSjhEPnRrTnsAtWJ7wbFe3UHVzWPY_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=lME1yXr5pPflVTP2Ja7tyfjQH9j_9daf3pqbs0YQtm6TII5ciwkzI1dNcFF3Jwmi6-GWzvgquHbclCLfXS4YpLXnaUCqG_c88dkSomlwmcbD9ob4ZMyaIDLpc0OkMSk1vM-BvROorcy_ylmCTDw8G27pVFNo9SKGi1WZ3v7hMFoY1eIZKj2_YL4rlAFa9D0pSxD-wKlw-VY56YgfD3NjGiioWmhiInIQGI_MVJI_k-iDTkJOwpNSUg4MxUctAJg5pBBefmNgzUjGDhNqga6nAWEdXREPQW3x5hc9ooEBDCP6N8G4e9MXY7fSjhEPnRrTnsAtWJ7wbFe3UHVzWPY_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh-NB-VHuYnxR6RyIpYJtDnq4CNQj-qC-3kMXILH5yuy65lLTPt5bDgmD6z8Md1qF47DJekttRccIsBxrA4p1rFbNnWBY7STpsNR7QmNiG3B6nOgxCQlAL-NC3_ul7w-KCReZNay1DhJxHQzvFtAkLIiWy3nzEm64WqctLbL5kBKxeNKOFI1865BomQD7TWAAnwE54BTtmhpGOwWaovcD7mY2excDb1I8a3RxuFOBfd7wRNQi_gHByOySDgbsKqWNjBpCxcRlclO0EaKtr9jwdq4q0hed10ya0fd3T8nJ_lIu-b5lKUir8xqMV1Ud-Y5lMdhjbLHhvSCTVRJyUaA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5cPWAFn-hSCdoOE1i3rpOIXe-26orfJMqxP5z4BqQgKj1nMzdt8XseBinH9D9tQpZUn53A96vGQ6TsbJ0XKqs5pP2xaRwlctnBoi5cJn7paNCJsDXSrdU-BKhW3bsK18dF377IijIEAj0UZ2KRIpx4UpvvTtWH288Pvl95BBV2-Xlrti05GGndCzCgx-eYK_aWdzkYpYdV3_R00E1SnBh5FFQbj04ZpiaEZ82bRupPZ_OVkHuBHHqZfH0xRARx-kQ5WPUro11Fk8Sqql8nYdttGO7THXKoSbfEXBmOl18t8cxHYrsyX8GdEfb2dby70hEjpEV_jh0EcTCv2CW-l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=Z5HgfhZjGxYbaNeu0sm75V-BfdKypCY1-9iWj7NpjkSjHOiPGHSRElKEar4SiY6J6lBLVmmux4RHUsuUAREMmuAiGKqu4xgA61zLK32w3E8LVPs3DndDYI-4_SCzbw9Wh5tqFlA-11ODTq5sVJlkkaZiRPQ_4UwahPBPm0h47LA4MDHqhLqWOyK0dwya8yKG-Jg6XZ5i_vt25hlERwMXHAlzjim3LOty1Y8RUYGpjSYoJm_57IqPAu1ZcfcdPaMCBVpGvzvdJnaYaEN1p8pyVFbAcng8_TSESQRLF1vEyRUCF0vYer9kx3QgU_9dkwRMwpmLwHazYcSoE-yUAKG75Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=Z5HgfhZjGxYbaNeu0sm75V-BfdKypCY1-9iWj7NpjkSjHOiPGHSRElKEar4SiY6J6lBLVmmux4RHUsuUAREMmuAiGKqu4xgA61zLK32w3E8LVPs3DndDYI-4_SCzbw9Wh5tqFlA-11ODTq5sVJlkkaZiRPQ_4UwahPBPm0h47LA4MDHqhLqWOyK0dwya8yKG-Jg6XZ5i_vt25hlERwMXHAlzjim3LOty1Y8RUYGpjSYoJm_57IqPAu1ZcfcdPaMCBVpGvzvdJnaYaEN1p8pyVFbAcng8_TSESQRLF1vEyRUCF0vYer9kx3QgU_9dkwRMwpmLwHazYcSoE-yUAKG75Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFNsiN98scShmCB7JUcAlDfKJqmrwlsS6eH9zXtlNHQuhZcXjuo_h6VKpXSksymo5fbpuSC64p4Vo26wjyK-783141Zrh3A7tMkOL0aClNsgtTXXpthq427k9nh7FOtHRUYfiHiN3pRlAesM3DY3Zz_qUeWTZNbCd8-YRAIxuy9qcBpt0iRqVZgDVSgjg8Ps7ZTLWRZXKQehfszFf8cSKplsmHboh4EOEz8LoQ8nZ4smGRihxsOYmUqa2b54yP0SgFBeltw1w5SpmUEwZoyhVeP7cihbxaaPm3ly06dksK_XpX0DYXVNGmQ7LPj-ULVsxJbB9Ztx_GcQ854wVUuMRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=qvxlLCBhLTjPJ2YGM3ISvJYtRu_JrjLRFX_95MKhizIBSzlVm6akkMYbIe3fGjxUyKPfCBMKIH-2jW6vNXlODp0wSqjGIi21KXR_2BTEn9yu_GeHyRvp3mRSwbWVA5t4uVAupe31TnRrSQOpliZ1jqAQVZYZlwfc9IH8H-9QtvbRSpfJxOlnu5rs_axcHlPrt_wxd6Z0oSDumOD1UnOqCMJzrXarV3-jM3X0oibYI3h9dAG3ZefZFtPc4POW7HFiTn0NYMxNlcUctN4ihsnfQK6YPjHvj6hz9PS8QitAbw2fiRcc623IoEbFiBvDcYNcInZeEw5hnL0hixNkb9LNwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=qvxlLCBhLTjPJ2YGM3ISvJYtRu_JrjLRFX_95MKhizIBSzlVm6akkMYbIe3fGjxUyKPfCBMKIH-2jW6vNXlODp0wSqjGIi21KXR_2BTEn9yu_GeHyRvp3mRSwbWVA5t4uVAupe31TnRrSQOpliZ1jqAQVZYZlwfc9IH8H-9QtvbRSpfJxOlnu5rs_axcHlPrt_wxd6Z0oSDumOD1UnOqCMJzrXarV3-jM3X0oibYI3h9dAG3ZefZFtPc4POW7HFiTn0NYMxNlcUctN4ihsnfQK6YPjHvj6hz9PS8QitAbw2fiRcc623IoEbFiBvDcYNcInZeEw5hnL0hixNkb9LNwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRPjPtmCp2tKpUu3gjW-fviufpqOL_HShjK61Dz20-utr4YfqbwnGZdlim6pbstrO5pY2hGXMEOpIyQyT-FFwnJaUM6xKtDhNl6D_2vTbH9xNs3MKZQUX66wFfdaoWwlthcM8F1dfYUHh_hqFO2cRcZzYhw-QTihhw8S4CaVK6cs9Gs4eKgPYffG2yixbkIBnK7e25tXm1NlO8cPpl7u7TJgapoVDFbsRNGOUjy-cyO5rV6OzNUqMQGetCt_AuuqQbNzmMAGPPsQKlgnijyLgMU9vg9xTXEHUaFyxFYR1HdPggvTXe1JgelQUkoLerbh43M_CNs75OnMNAbUykTaQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee8kHae2QafPuy3JDBS3Wu1wl3a-xOmtRHyjy_6MvT0dxaHW6FPYQLsNUZ9GUyL7fjrHACVsUQ_L4RTVhyNT18wZImDrshCoyC-55GOtl4aBt_xC9vhb4mHJvuNz05ZjyREMmWfGRILiZ5fYvWq_OneoMPYuYfYLJeiia731l-iocv9Ttqaf8s047I-H8zkKyN06JbaJalozS2qZnTsUYExq7TtCYJCix5CYuzrqCpDTe2g5OHHgupd4cTBlzM9i-ARWJR4Y9h-9wADpD-QlhY4pvE7aJX7tj216Oa91m9G5wHA8p7jUgOD57grk5lw7Vwu7LftVDbEO3GpUS308JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8KnQftB4Vyu1WYFx2JgemOlF5EVW0-CUaMSBA-eDHof9S6-Yq1sxnmXMwZN_PAp3ooKuvu0QIEa5FpL3sT3kWtFGYnt9DoH4-fAcHTsYl5pjqBzypZf4NqYgwIPvFolzlnrJ_2zkENiXySZcVU1jYHKpcxW3I7rFv8zCOt620kV3IAIw5lOG75uPZa2TUNmjr_XgpAABDej70Yz5-zxmDIGLYkyGu63Kkddtgxe8hU9E9WwO_4PyIhRnUAPgbp9tP0AkUjnOLNO_rxbAnS2qB-bjwzbJ3f5i8-WYl4oNu2kaAFB-YTO5hLUm5w-sn8IiGAOHcuSWD7tcX3s2o2KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1j2AR6zsplqdZNWrC1jbGjK9UGrDgdaVpscmoq5Zhz_hS5iVhQl5_wsoHNBrGpUeRjzqttQp6LcLWhR0F995GL6l9ABW1POPrYPpJa8L0ceeFPln4TEi6M44jlGBk2nlu7C5VyvLWj1JefirWxa6eb2Jd1Tua2Y9yR9ocHXlBO5P3aHyC0AQ6czwS5VwB5RfiC77Y72LSSEb9MQJFxKNPWieQOVzQZXNsUXOZ8PScAFpkrqrr15EIez99Gq02tPWITMRw_mNBZYESof2ICmVRFKqkzwdyp-0XolB_jWJPH--xx3Ykuzey8YGNFKwpnvhgZjsXZ0D0MIXWRc7I0vDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oltc1TYzpc1zNZYZjPLOQhKURGskBA6Aq7sN1Q2wV9ziXjjm8MBuN5d3U32t2AkNSilzSWcmk5Lx1aM44yPim9iRFomHdXokoAMURz1Kwe396PfZ91UbjQF4K4ItL0kKKhjCQd6k478VDYF7IvX5HJKYkHm7sH7Lvm-5gkB9tMWsyYa7qXaZz8JCmJjj2TR1IYM5KPF1KyhOlS_uFjq31sDNwvSszPywb0aS9nrbOOmW9DW3mZv9kdbNh4tP0mCMXzsSCt3mLjNjglymGMTNhE47U8Ck_9LD0rTmYDzxvtWWCPwduUB1ZviK9zdwKMcIpyT_XyaDnFlA2wFwI2zF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXmjbU3WbOphCE_buaWy0mBIot9ZfinH19E9pGEKaLvPX-6733-p3cBg5IJOBtJDHC7Nqa9BVJztPZnxL_JMOmpU_Q8HtoI4w_TUD4kouSKthp2K90udQuRJ3iK3BMbSJUztJv0I6JltYOe9SDpepvzLnKyPsQi-r97KwgQxEBD-xSnhvXA8gBdQ-8H72M2LIuAwaRBrK6UIME8YIP6HDUPc93omiR2M6c1SywWVL3mnXth6CNqxWPI-ALMnkcnmXqndQa39ixkQ2PmOSLvf5jgNff2-LxTJY2hTF6q8UtSjz05rC618RoLI4yVLZZeNionhZr1jOMA6CAYeCiEm4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWKlp1C84y-SQxLHS71m-9-Oi_24j8qtAX6hz_gK9nXR3CMjH2BgpndLlkz05SE2jKxouJxH-HST7ooTpuggylrDtqVakeU9VKai-AQLq3vOC7ufXLkpNfifx23ElkwECrQH-vahQ0XlgGDoTzzhLrPaYIVF5fbWRVrbs_7J-vWEB8z2NhUtbCP58xKn74Wffq18TlAGZlOMAhEPZPGof3BUwB9dNzB-KmPOkswpKGK2VTHiftPAj8lQNP0J5Y-BvjqbScFj2tXWDiXVbuD87qdqTAG6SD9MeW0whj5HHUAvTZE4vmdDF8JJFenE5ev9clGqOqnRRLKneyTAOfkMcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur7sYxqPw3ihF5-VvNvWT4r1Rbv789W084bvzdIM-XhpO_Y0cHmWfBVDZprktWD-EjHUj9ZJbmM3zmw5S-ai9GUOYbL4sC30q8B8mXH8EmSXodMlPzfyOYOldJ17Kea-Ayr4xgy3aRMwBJ4cBgZ3BqeeddofTeP4PGezHzTHhgWGpxBevPVKZJhMWiR_MbkY3WLLkFpV4JucJvcZHUHKyKvm8HABNmpmv7iMoS0j2s36q7mFtNRutkfSz5tL1qfo441kPVBDdhCgW70gDYp8GyvJndVr11IHH6fI4yORJWsvuYTu79W4bgCNEmf3gMdKYA1AIIzo01lBuzskC-9XHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfW8JN21qC2sjxCeBqiew2yF80LTsVCt3542AbyHS2XevAeaS4hODTdSx8PtnMLE-yGTedwfBjznTS3xLphvUnUcnPM6Lszo2V7WKbaAUcG05DeR_Sq5xmpf_mgn4Cn-SN1_7IQJIgN0zEbl_AT1pKU7FkJpRcbUp3FwoB4lhJGyjY2P6HEvpQdSRsQPRva0VwFAmyE-muIK1ytGiWbxAc97xguw-iidnkrG9T-PFSyqSRKrlzX9uDKHK3u7KM2xa-fJoyUoudesjWT_sIlITSq9sKekkfCZZDOKYu7b6jY9HPnojAU6IwfCrt_BxflRVgReWIvYsP5x4iJzZqiqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZLrtrFeQM5auJoGSMpR75eLCLkJq5vDJg0enOgzOoqot6YPabsyZPCnF3hRJPbVJMxcVvglK0Api8qXQxbrBV6LHnAQEOFxXIz-xtAYI-TbfYtohGGLmRJLv3MjQgOHabolwUKk97PogEOHYBFVruNhG9bUA3_FcOfQ40THe9_C8YqJu6-TsM9T3xbLCCz9SSy7hone0-oWYkv4KOCLOH6XcLMqqO6NHZHVW7vT-cGQJe-CeTU3eQiWBcF22LIypv9zuFaWgWEzOU9jy0-YVqrerACNUhthbYFnpD2M-n0WLSNSKIprkeP09APbMjkjHuqSaTVfI99mkavTwv26LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
