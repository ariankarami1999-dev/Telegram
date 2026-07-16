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
<img src="https://cdn4.telesco.pe/file/Rp27jzV72hWWizsDsMax-MGd50NM72riWgCjv3Hue88xCXPacDhnMCocxbdHieFDN80f6--psAetYdvpm6r4APhJxAvjM030zflx3Vt4sT0ahLVcilkTmjccv7Q4o7rkUKNd46XKK_atiVKdIoq4gVoV3W07sZOhSWlBTG3uv-AUCWN1IJU0mRtLuuCvMw5kMA-euGZycbivY9TxzTulx0xQF0XSzGK5sU7icydYKTguJ75oBNCHV4ex0rFVs6ILiomZiXokepHVC1L8HTLCLRs9kkTjkVrlDD4ogW7q-D3WJUjiZ1ZOIBjg45pobii0Es-FX2PKH1qIq8juSjcEog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 07:27:19</div>
<hr>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDDDp9XY-saULu9JQAiWb0x-EASOFrEtiniGgNM8uJp-jlJRUtXmZCqg3mnMpajckWyDHu2TRb9JkDmLGx9w77hkhC5fq2L1zWSW2w_Mbg66s38n1rJbWxKNJXrRF8oz-DzXygNGGWlsfjZ6As9KdVLUkIyqaHIGRD-zTl-yl5kHrA1Dn900zlDsgw17IibQy3_r9Nq2MC7gMPaJxfT-G5Tas0sEsEsbgG8aCV9UEp-dwCk5nc8RGukcmsAayOJrHjEdXIfNuS2hq4GsnbRy-Fi_DGFSv6KbdGuVTwH2ZvXkSfwvEXlFw7UC27pptw-SsRa1Olcvy97i6wxHC5gfGLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDDDp9XY-saULu9JQAiWb0x-EASOFrEtiniGgNM8uJp-jlJRUtXmZCqg3mnMpajckWyDHu2TRb9JkDmLGx9w77hkhC5fq2L1zWSW2w_Mbg66s38n1rJbWxKNJXrRF8oz-DzXygNGGWlsfjZ6As9KdVLUkIyqaHIGRD-zTl-yl5kHrA1Dn900zlDsgw17IibQy3_r9Nq2MC7gMPaJxfT-G5Tas0sEsEsbgG8aCV9UEp-dwCk5nc8RGukcmsAayOJrHjEdXIfNuS2hq4GsnbRy-Fi_DGFSv6KbdGuVTwH2ZvXkSfwvEXlFw7UC27pptw-SsRa1Olcvy97i6wxHC5gfGLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=EykgZLzJyXWEZdoHR0VrlbUSt654FzIH5Ilj6C_-tAyeBm6IixGOC7f7gqCF9aygGq5pG8sDGZWXJxJUbTlZ2Mjfsr_63Mcc5FOS4hnX2sjsVR1xUP2r0Y2pYcf2tODqjWnutJIgQ67Mc7GD2OfDHSJZjEtgtVVqQk9Q-kbUlTWpgC5d8JyvFoEZGeHligAq7rlz8n2RiF_tp8iJ1imhOBG2fYxKFqA0bkRDRvu_idqz_8tqSKeuSB6KtvD-2630Li5cIJvS4_PKVpBBjdo9kbofh_Hp5GAcLxgpoLkJu2tzSaKob4APvrpbG4V9DYSwgSGjtPi3x4cXY9k2SoOtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=EykgZLzJyXWEZdoHR0VrlbUSt654FzIH5Ilj6C_-tAyeBm6IixGOC7f7gqCF9aygGq5pG8sDGZWXJxJUbTlZ2Mjfsr_63Mcc5FOS4hnX2sjsVR1xUP2r0Y2pYcf2tODqjWnutJIgQ67Mc7GD2OfDHSJZjEtgtVVqQk9Q-kbUlTWpgC5d8JyvFoEZGeHligAq7rlz8n2RiF_tp8iJ1imhOBG2fYxKFqA0bkRDRvu_idqz_8tqSKeuSB6KtvD-2630Li5cIJvS4_PKVpBBjdo9kbofh_Hp5GAcLxgpoLkJu2tzSaKob4APvrpbG4V9DYSwgSGjtPi3x4cXY9k2SoOtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=MYSo8VvGU7w57GPF_Rv1BKklxxrnKvYjZ5YjoP4GZQ_UuftOST-n9nJKBBNJiq-uMS83om15_h9oeMXST7brcrY92ctNp0qboZfitkuOE5WFuzYzsXiafv2E8TRVd6Ex0LYOP2jqkWV27oNCmnb-Ym59ruIBHKQ1JCejXx9FTU12140jYvLLUFBH4_eK2mjbZSzmj222sUapP-6G70_WBCSAYYgLyLEuBiSW5dNUUxrM0uXtOIgSKnyBdn73u3MtS0A6pt5n0MMsqzUg9sbw4BWiOePFduSkXAvGtK1Hdbnv_sk6DrICo1zSZ2iXp_Sz9XSOr7WgblsqTJi33-7_YjcV2hBs9RE12GsfrcqrNpcy7jDGLg1lZGvn6hq1WYo3w8P69OkK9A27KzkxPfNdSCyMg-GHlc8lSGBMEVwi0AVik8d74gFxzhxR0WQ46c7quuOiYDCBGrmKtRHWP-CHWqMG2XBS_5aR0ZxtpWRb8O3CO_SA7Xc2dAGr0egLQ5FV6j0Dc3oy7Kqb7no03kkEUNPp-QDlisuNOGCANDhsdsFLSPB8sXv6aJsUY-LtD7tSsOo78UdqircGdEdbpl64nutRPbvuqYwawpsQZXnhjr9aBeBkwTNK00ZNcvhuaU_ZL3ullYFe5JaRXnRf0wb0fpjyaYNkfgMe6DiahigGE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=MYSo8VvGU7w57GPF_Rv1BKklxxrnKvYjZ5YjoP4GZQ_UuftOST-n9nJKBBNJiq-uMS83om15_h9oeMXST7brcrY92ctNp0qboZfitkuOE5WFuzYzsXiafv2E8TRVd6Ex0LYOP2jqkWV27oNCmnb-Ym59ruIBHKQ1JCejXx9FTU12140jYvLLUFBH4_eK2mjbZSzmj222sUapP-6G70_WBCSAYYgLyLEuBiSW5dNUUxrM0uXtOIgSKnyBdn73u3MtS0A6pt5n0MMsqzUg9sbw4BWiOePFduSkXAvGtK1Hdbnv_sk6DrICo1zSZ2iXp_Sz9XSOr7WgblsqTJi33-7_YjcV2hBs9RE12GsfrcqrNpcy7jDGLg1lZGvn6hq1WYo3w8P69OkK9A27KzkxPfNdSCyMg-GHlc8lSGBMEVwi0AVik8d74gFxzhxR0WQ46c7quuOiYDCBGrmKtRHWP-CHWqMG2XBS_5aR0ZxtpWRb8O3CO_SA7Xc2dAGr0egLQ5FV6j0Dc3oy7Kqb7no03kkEUNPp-QDlisuNOGCANDhsdsFLSPB8sXv6aJsUY-LtD7tSsOo78UdqircGdEdbpl64nutRPbvuqYwawpsQZXnhjr9aBeBkwTNK00ZNcvhuaU_ZL3ullYFe5JaRXnRf0wb0fpjyaYNkfgMe6DiahigGE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKuOAqsHD7TgowGsFpr3nvkEvM3ymPiB_45EAbnlvsRqGyzG3gu2PasgN3CddWO9tVUfKJifT0iyIdHvBz-2brQiwxMpdGdeSQDMKr2O8WxJaJxLV9SkMiSBhKdPmXqXhlVuSrAlOvhkXtJQjTefOUObnsQEGkhh9Or2VSVQHHD776eZLVR3CAh06MK2DFOCsuq9eFGDfH7hW6o23FqReaTpb13HNZIkTxbRbbfHeGSYgf9Oj8IDHR1XgiFdLBw683niIgTNpqASY9wquYPcscCSMAfhWWwbAsIHQ5Ttg4YHDpeWoEn0_OYXbFCSeNXlIZwgy8MevP6H6Z-fPX8_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqbOdrHw9C2NtxilZNjWisC31l8r6Pnkk7BN2rJVv4hOIDbyYSzYtKUo-C7sQPexY4_gvyRhiTdN4Zd6df-9HIpfzVPIhe_pThZlaXWlgsn-O5u9DzxBLZRN0931wH89Kvn-vUEfMf9OVZrOBn6qrjOLNmnRX-LUy-WU7RbJwzr2orrDgLn7tepeSGb1y6atz7xJagshYL-d9Z9MPi3GOiEz2F5knvmhOugHtAnSYt1Pt_XAE_b41DHwm488eGBonR_YhAtoKzUVXXphXc8e1iJYkzvDRUi0Uqj2TK3nJm6KMHh5XMWz_9ub4jGLa-iLX1Ds7R-z_H-pEzc2NuF5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=kK0TPPJJlRzXUMG4mdQlG84R8D8US0MnxkbdABoooMFAcDGpYeWAk3IwtNaIuxDdbjbJyO9zXdQVjXuGHiSl0fnBtQ4-FqXyezlo5gWzUaF8aHkm9YUhYPagVHshGVe3OrPLRjsHHiS8uVP17rYHfD_fntFQR50UG5ilc0K83TgE5Oj0VlDy1e_XObBDPwysqoAFl1M6_-J5Kr88fDk-nZOyYfhwrnREy0YGenFTvJgHRPgjQ4O2GqpMd_XBoBpxBhQt7BqfLIV0_KuLRmqY_P2V5R3ykSIMFmnY5-04P_lxcleVvFzfyrMMRHq8eTuvOjVmLuB1euQajOQBz3Zbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=kK0TPPJJlRzXUMG4mdQlG84R8D8US0MnxkbdABoooMFAcDGpYeWAk3IwtNaIuxDdbjbJyO9zXdQVjXuGHiSl0fnBtQ4-FqXyezlo5gWzUaF8aHkm9YUhYPagVHshGVe3OrPLRjsHHiS8uVP17rYHfD_fntFQR50UG5ilc0K83TgE5Oj0VlDy1e_XObBDPwysqoAFl1M6_-J5Kr88fDk-nZOyYfhwrnREy0YGenFTvJgHRPgjQ4O2GqpMd_XBoBpxBhQt7BqfLIV0_KuLRmqY_P2V5R3ykSIMFmnY5-04P_lxcleVvFzfyrMMRHq8eTuvOjVmLuB1euQajOQBz3Zbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fI3y84eyqsPSV4Ax35-6-Y6lGlwmebz6kxpAsnr7KAOOuKQYHJ3r8eES0aiV7fHH2_uSsTYsMM8eCKMmgP9JmYzVUDRd1wuizJN0aWyx9u6WFVyeBhkWjmxIpufMLml0fmCdoSRtLUmyRm8aOj1XvO-zmeBeuzBa6mdQT6oIjyblKvFpw6-aaEERtZ-2q9tZwtLiBrhYkwsEyaO5hls1_17JsMFThxsEJy2O3q-9lH30FmZpgH0rnS7OtTp9SzySwRwsQ9HoJwrQltzFidIVo6-vWp_WHIKz4EWsjeh__f9ZU7vO82MMA5357Hx-KXlzZsAr6NdvCno4-1wmm_uxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fI3y84eyqsPSV4Ax35-6-Y6lGlwmebz6kxpAsnr7KAOOuKQYHJ3r8eES0aiV7fHH2_uSsTYsMM8eCKMmgP9JmYzVUDRd1wuizJN0aWyx9u6WFVyeBhkWjmxIpufMLml0fmCdoSRtLUmyRm8aOj1XvO-zmeBeuzBa6mdQT6oIjyblKvFpw6-aaEERtZ-2q9tZwtLiBrhYkwsEyaO5hls1_17JsMFThxsEJy2O3q-9lH30FmZpgH0rnS7OtTp9SzySwRwsQ9HoJwrQltzFidIVo6-vWp_WHIKz4EWsjeh__f9ZU7vO82MMA5357Hx-KXlzZsAr6NdvCno4-1wmm_uxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=fu35AScmuGREc1LlHMH6QIi7mTL5tRggtgK_l_gA_oNfNyYhAv-oyOg-L2us73waNxIqiaioBFzs-waHatjrFkp2LXLm61kVdwOhMCEU7Zg7jZYRgfoWw3AMwi0fc0IZVEJxfMzUW5xOyunLYbkNjyoOGV1Akf6I4aj8lhdSp6XQleTB6Mo0FTnbMpe9ZKxjjpMBHCevcSGsAAGSkMdZ3i6S_DVxNYf7_wsxJB6nWWcbCthqan5fHLFP4cU454rBCMJXHOhgqnQhJrBYQS3j3dnIuT61u9p7DM_E_kvtHe4kU8CJsCDFmvrLvu3vcE2g0wYCstA8zGSKUJhJZF6atw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=fu35AScmuGREc1LlHMH6QIi7mTL5tRggtgK_l_gA_oNfNyYhAv-oyOg-L2us73waNxIqiaioBFzs-waHatjrFkp2LXLm61kVdwOhMCEU7Zg7jZYRgfoWw3AMwi0fc0IZVEJxfMzUW5xOyunLYbkNjyoOGV1Akf6I4aj8lhdSp6XQleTB6Mo0FTnbMpe9ZKxjjpMBHCevcSGsAAGSkMdZ3i6S_DVxNYf7_wsxJB6nWWcbCthqan5fHLFP4cU454rBCMJXHOhgqnQhJrBYQS3j3dnIuT61u9p7DM_E_kvtHe4kU8CJsCDFmvrLvu3vcE2g0wYCstA8zGSKUJhJZF6atw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQFns4pwb-h-GbNx3WrqZ4qCCwZaWNWwSaxuPySFm7bfdZ-2R_Blhccoa_vTu6OzR0uFORCjTjvA9ypHn5xVTsm0OrCo3TDcexgj5QjVhs202h8UHagVK77sy8laA02WwLZXp8iOtfV5476t1-uEYgriVy63E4iIffoNQ0fHnTVutQWtrnWet4eyW0uENDSuNJ1owf4lbTw5SVDwtm_v-yjlgoSPGnvtOHIpEJ0aKszNudGEVZsjkd6roG9AWKHAaTpaXvaJVl9XKs32Ftj7Rgcadn-m-UptsG6rma-O-yGWeiet65-Z6fAXRfK7-i3YqCaEMbQZsPduB2Q-HBlCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5gbzsqtwC7jvznw-W2Rmbyb4ob2IOZ-cXqA1amkWVJWsy3Y61kxVnuLx4uYIxqNG48MWpf44A091aL-UwcBWXbjCbo2FgdsOiMT2VNNeF49u1gWOJ-ocuzHXaV8Xjd7Wt0zVrQHgJnHCMLLAF9_xN8o4mBqNQy_UW_fRmyGGuGIFzRUhRItMGr1_PIAv7cJZvr7b4eHHfDb-WgcwCRNe71CkIRzcp6nQAf4SqaOq8zY7z6PFSmjGJmT1tPThwn8UBYgOyE7iWxua6qR0rYHHsyamywaZ8fYrD2Finn1GW514sP3R3F1TiPBY_4rh1ZNBc3Q5Dct_N6LSbHgSwBn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=OSDLifeG0oaU6rIoMeF8T93G45MkWJsFVe0T6Yr5NOV9RIPEg6nzKhMb0uqm_-xbaWXyGQOWX66PQvNMfe0LU9oIC2DfkqtsFHgoyaWv4mBEHXQNIVJlHEk9aI_5CzBlzQ-EvAG5WQXkm6Ns3PZG1Dqt0uIAPt1iCtniknJDxGQbDCKa3-elw3jMOFOi_VGLsEDXCLhFk6_4TTeWgbIF7Lh2CStKUhyA2YCn7uaM8_bWkRrXp-XWLuCGrh7Qddb6ILRhKAFmTb7c6QzjpQ4sA9aHuYleBD_hHjlekfNIBt6-kKh9zbSOR0Tg2E52vZrCdm6YFohynl-B3CV-Uy_yqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=OSDLifeG0oaU6rIoMeF8T93G45MkWJsFVe0T6Yr5NOV9RIPEg6nzKhMb0uqm_-xbaWXyGQOWX66PQvNMfe0LU9oIC2DfkqtsFHgoyaWv4mBEHXQNIVJlHEk9aI_5CzBlzQ-EvAG5WQXkm6Ns3PZG1Dqt0uIAPt1iCtniknJDxGQbDCKa3-elw3jMOFOi_VGLsEDXCLhFk6_4TTeWgbIF7Lh2CStKUhyA2YCn7uaM8_bWkRrXp-XWLuCGrh7Qddb6ILRhKAFmTb7c6QzjpQ4sA9aHuYleBD_hHjlekfNIBt6-kKh9zbSOR0Tg2E52vZrCdm6YFohynl-B3CV-Uy_yqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=FVZR_ZsODoUGMA5A_Ep7d-AO6OdA1cR5GD4csXSzcr1bh_MykjEojkDoJcPT6DdDrmUTPbB5FudwTKqyel0_nScCHasPP89OVVu3kOk8kHNrcCspb-yrussF3kn0St0tIhMkXfLoGQo-w9hzyeFOZf-n8fx38-lFohdPVxkstaCjiMhvW_UZ5zdpgTieAk5qDVk6DI7O2x14rih6aTG3Dvm4yYUZZUNZUPWcXZHa5Kl7ph8iQUPMtAhLNpUNTgcKFmn8YrHaIq7bAynnlPO0bJG3unVHDfLro_vPXv7-_EyOlL07IVCNqVt_4e6nEhCTiDgJP1EfmwW19zqGdB75qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=FVZR_ZsODoUGMA5A_Ep7d-AO6OdA1cR5GD4csXSzcr1bh_MykjEojkDoJcPT6DdDrmUTPbB5FudwTKqyel0_nScCHasPP89OVVu3kOk8kHNrcCspb-yrussF3kn0St0tIhMkXfLoGQo-w9hzyeFOZf-n8fx38-lFohdPVxkstaCjiMhvW_UZ5zdpgTieAk5qDVk6DI7O2x14rih6aTG3Dvm4yYUZZUNZUPWcXZHa5Kl7ph8iQUPMtAhLNpUNTgcKFmn8YrHaIq7bAynnlPO0bJG3unVHDfLro_vPXv7-_EyOlL07IVCNqVt_4e6nEhCTiDgJP1EfmwW19zqGdB75qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Lf_fzbxcaMYWKIXYWIpkLbWrAf46o1xq7U7AHGflpZQlPQI6CgFjjc9bFYm-9yjXWnZVtfGjb7xmwuAdaACP-j9Fd6GGAHiBqjFIWXRsO5w_-J7WASocfjUlVF7sXu-jqk4OjXk6Qzz3DE3sF2JigyYYJUJnkuNfer4IyF3jd5vyc-tR1xkATwsDmMD2WXU5EGjVekrz4rmv3ui9f0M8xKv-nSx_2NeHHGTRx8YDN82hhq4eST3bhzdwpYHh7hKhi_uVJCE31Ys_R3dbrt2UGw6QS92RA0p3pTuSnpbVnSep09TuO5XQCrgRB5VhZ1oCyO56YVglfvICr2I9SSQW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Lf_fzbxcaMYWKIXYWIpkLbWrAf46o1xq7U7AHGflpZQlPQI6CgFjjc9bFYm-9yjXWnZVtfGjb7xmwuAdaACP-j9Fd6GGAHiBqjFIWXRsO5w_-J7WASocfjUlVF7sXu-jqk4OjXk6Qzz3DE3sF2JigyYYJUJnkuNfer4IyF3jd5vyc-tR1xkATwsDmMD2WXU5EGjVekrz4rmv3ui9f0M8xKv-nSx_2NeHHGTRx8YDN82hhq4eST3bhzdwpYHh7hKhi_uVJCE31Ys_R3dbrt2UGw6QS92RA0p3pTuSnpbVnSep09TuO5XQCrgRB5VhZ1oCyO56YVglfvICr2I9SSQW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0DZvVdn7YXUd0gcNJHIequ4n1Q6mrnde3SW_OhN4eewbDpfzl--N2NH27sl0kP_YoE9hjU1B1B4tnDbkTqLkbNNLHinap392-kLu5P3brlujChPJJ7mTM70ZvrXzLB287UlZlkgwomH27T5ubvXYFLzwk6zcLVvFU3jxyRAaEnhxAwdCQ7vqJs4Dt6xH9k_qmB_kPZIbNLQ5RDoRWwSg50OqQgFGlSdnEQe6hN-INc9qKgJk_IsFZEuI2r9o3x6_xjvIBtwjbu5XeXizFxOv-DI1a9yLlT0uXDGC1dz06gkxhDfNsxTuuqNZwV80iIB73viJpfsFw32-pz-_eN77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6VBFD8_j5GhRDuQ_EIpTPHEV48MdEqzNqm0hT_iOZfQY_rkg9qC7XNVW5W0NXaC1QXTi3KHgHrkY9-FmZkvLsZ8G5bdFZHqlQPFGeUqGzm972_adGk_dl5q3a6HrgJa1F5uVEYmedFvvkSua4l2bvImk1KD3LtgB1JKocWbaLl48cOoakz8z0zvXotVltYPc0pK0bULOke4K9aIJrJZ9icc98EXS8oYrh9lsdS2x_hNHOOmCrkA1TWLvG9W5CP-B5vKPXH0ZhkQVX3eK0goeUlzQjkt1wW7b_RpGbIIvu_6vf2gfGDVOQzJLI6eRoZJp-vWCNX3ru1WSmvQVfJj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=h548B51zMQQt28uRrqeMIvO3a-kb2RArbDwG0nBH9A1AxUe1v7jf66l4rFiJQhtc6LnEqwT_KLLALnmHv6icyBcAzm4LvuXJpT0iTg5f9FNZDv3HEeG8MKa6RPSUS3L2ylVrH2NkToAaOHtqvQwpjxIbz-pBagD5bdLyKmBCrfM_mgoMWCuGi2tqVPDZYBEK8AgjUJvk5n_8mwOi_2f8sWDzh_RrP9NvuKq4v3BT3u4VZqItvaubvoukA0mLXXcR4n2s9UQG3Ny1LZkfdmDeMmR16ZURIatQYzxdLDoF9espDKHmQ7VBVyrA84Y4mR0usdNSn6k4vxp9CnXNUCnZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=h548B51zMQQt28uRrqeMIvO3a-kb2RArbDwG0nBH9A1AxUe1v7jf66l4rFiJQhtc6LnEqwT_KLLALnmHv6icyBcAzm4LvuXJpT0iTg5f9FNZDv3HEeG8MKa6RPSUS3L2ylVrH2NkToAaOHtqvQwpjxIbz-pBagD5bdLyKmBCrfM_mgoMWCuGi2tqVPDZYBEK8AgjUJvk5n_8mwOi_2f8sWDzh_RrP9NvuKq4v3BT3u4VZqItvaubvoukA0mLXXcR4n2s9UQG3Ny1LZkfdmDeMmR16ZURIatQYzxdLDoF9espDKHmQ7VBVyrA84Y4mR0usdNSn6k4vxp9CnXNUCnZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz3njyS26Y6m1RRaTFFhgnn-YIxBtdmvZg7RESCoJjVsUTgRxnMnjSt6CUWZt-9x7FsJwZOrBmQr1tZJWMcGXcJbDey2rGD0h6oNGnk18tOva7OxPmbLAwHqC7uBJSuLhXBFy8YXRzf18FjDucViuIQ32bv2Edy4upNeG3dYBm2maRD5-uT_kPuzlH16Z2LM-AKnkUeDrCB7CrL1ofoHX9100sct64wz851XicCT9jaLsxB--PUQqXcEv-QoJZ1mLbTT7t7YKBVte4IAAHsVzLx2FFM5SfdA5z-sC4HguYeJvjxz7xnUhF0-8tYr2Gf18WATXjoGrPyBZ_8yXIi8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZU-MQChT6P32LaVTyFAcdVreYUypOuL3WIpArRVbcVCbMs0It1cRhE9i_Qrhgs_FZJL1igfIgLEUSJ-9v4FD80G4oOXdq3rq4kPnQZDwOkOKwkcCOnWjWzVEPP_UQaXtGN7jl1Sxknas84cWX6FTbImJFJ_JIidLfDdi299_EGFvQoNBEg0TEOMsgU2sg2ZGAaPc8fwWd4DFVqEM4avwGDLa7PPS1Xd6PfnOCkWHYdsh5GTpqD_aLieFSNK6cvfc698hXWXFeCCCalSV5XaEA4mQGhM6UC9K5mklJenFaXbXbzIJTmYr6wCJxHMshZVlgG5qLIxlSFVgxlfkX9V1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Rzq7vhgdRawEdNf2PWsqa0RBECx0rEv3BZ7eKLiVpnUca57rb45W0MJWP2Lu3qoz97YoMaGmbjA2uUk753QLY6iKmKYENit_6Yfn7BnAxg8fKC4YyU3w7-GEjbab8_uTEPoefQSpaOIyLg76Co0okakilER9735-hXteT-YlEBheqCG9gGuDqmlXwNezX11-35uyNtAjk_UsEkc5C3opZIYQij5En6mqqT587O96im3dS_b5JMGRCGow_fOnf02itC3NM6IRNXG2fy6gdaL0AXoAYyTJ-wnmNFSRjiIGkTbp144H47j4lV-X5VlgOa-W4SyjEj3f_C25_Kkdqq_qWUswxKNqwk6hTw74Qrck6-Pjt2VNpK0lN6MitVDoLYG1K0t92WPsZFg8E8KErLVUDA1pPW526W5_kIG9q4yUVFhUL-ol4lfNaYXBcduP43eby3pRvN7hxhDRU9kCmJRtS0zic72JuYXDRk1Zb4VcbyOkwOYtXzJZU4AoswqdY1WojAgl6Gr04fjt1MRwyjGQvx_chzL6YP1cmROS-lEHbCT3tmwivg49ccGm5Sx4FShg-iFHqXPsZtdvkAWwM6bPonougKksMjMOys0cICEh9K0_Yb3ncK_DRZVl6zgGUmXwC-0R-4CfCyA7CE8lJhpStXXH09W5T2TD-HL8xrjwuGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Rzq7vhgdRawEdNf2PWsqa0RBECx0rEv3BZ7eKLiVpnUca57rb45W0MJWP2Lu3qoz97YoMaGmbjA2uUk753QLY6iKmKYENit_6Yfn7BnAxg8fKC4YyU3w7-GEjbab8_uTEPoefQSpaOIyLg76Co0okakilER9735-hXteT-YlEBheqCG9gGuDqmlXwNezX11-35uyNtAjk_UsEkc5C3opZIYQij5En6mqqT587O96im3dS_b5JMGRCGow_fOnf02itC3NM6IRNXG2fy6gdaL0AXoAYyTJ-wnmNFSRjiIGkTbp144H47j4lV-X5VlgOa-W4SyjEj3f_C25_Kkdqq_qWUswxKNqwk6hTw74Qrck6-Pjt2VNpK0lN6MitVDoLYG1K0t92WPsZFg8E8KErLVUDA1pPW526W5_kIG9q4yUVFhUL-ol4lfNaYXBcduP43eby3pRvN7hxhDRU9kCmJRtS0zic72JuYXDRk1Zb4VcbyOkwOYtXzJZU4AoswqdY1WojAgl6Gr04fjt1MRwyjGQvx_chzL6YP1cmROS-lEHbCT3tmwivg49ccGm5Sx4FShg-iFHqXPsZtdvkAWwM6bPonougKksMjMOys0cICEh9K0_Yb3ncK_DRZVl6zgGUmXwC-0R-4CfCyA7CE8lJhpStXXH09W5T2TD-HL8xrjwuGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcipCLHHqVuAvc4Jcoyph4La0a1FisNs6KJAsI6DlmadJioUenEdfmBUfLzbGX3daI2pt0Rv-BQvJvRTWGgl0nUzVuGXUL_lzegee5ejSDN9AP7xjpCD7BFjF8olq5QgoXNqcVKVijdxFCwhxlycXRhHdBWs9t120AW1gWaf6o9VeTJCgMTUZGxf8hKFm8W1vFA1yFb3lodWlDjQbZCdLiozJ6no5vX2zI2K5vDPUKszXyMhQ9HMY3f3SVn4PpIxxL_FGYGAHiwy2qdgCqvhnHUVL4hvD3dehjBTMFpOX-hedOvWGxjb0B9hq_sIyZxxxGEOvSuuyHdqUmc0bJ-ITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=la-NmrBPpHKUg6WQbZLRuwnHxLn8sK0R3K8L1h2oqxhjGVlfEN7Oyum0Q1uXo8id2Iy883sxTX08RfE5H5Y5AUGPzuBFchbAHSnsTwXgHsliMecwQgY7QLBApOc85YdRMMH1sGjPTZjV8WEAoJvNeg4eJwOdu93LPmAUylqeK3-yZp9Lw76JrvDvFKi0vm9po1EG0btrQvhvs_gb00GdNTCGwcPBdZ1mzvX22m8x_r0Rni_xt6gAn1x22YHKjdXQxqsecZEmYM7LGKaYmIyxOnP3TU1bpjmiGUW9hA5Ca8hs-O2BMc4g5UpYAWGD3P2cGJiEKpxGxy1QTsMusV1qqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=la-NmrBPpHKUg6WQbZLRuwnHxLn8sK0R3K8L1h2oqxhjGVlfEN7Oyum0Q1uXo8id2Iy883sxTX08RfE5H5Y5AUGPzuBFchbAHSnsTwXgHsliMecwQgY7QLBApOc85YdRMMH1sGjPTZjV8WEAoJvNeg4eJwOdu93LPmAUylqeK3-yZp9Lw76JrvDvFKi0vm9po1EG0btrQvhvs_gb00GdNTCGwcPBdZ1mzvX22m8x_r0Rni_xt6gAn1x22YHKjdXQxqsecZEmYM7LGKaYmIyxOnP3TU1bpjmiGUW9hA5Ca8hs-O2BMc4g5UpYAWGD3P2cGJiEKpxGxy1QTsMusV1qqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2nB00rILhzJNhcTCbJuv-wkScEsGIneT5UHC3L-wjZUqlP4g9n2_RvX6NybMNLIC_0HZqYAo9eZXv5iJAUkzgz1tySaF0tlfvcZ5WuNpwR6TcPQ3znrmVkzrgt5U2-CXMkG3MLKXLSxoCndmMOMNkpo6PxUpaOpECy79G7K91923ihU8-OZU5YHq-V-dgfcGKHExsKp5zlA5EHK2exptmmRRDhtCwRpTej_5BScbKj2VUlW7CsuVMEP9mGvg9bJUQBOjEpvOdD4dKLK1gqH1e8yy8Kjcv3AV8PyWhMZOOMqSG6QGPEHJx4FgOtnmccc4J2shcMJEXqsQJ4HkTolsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=flx_RHi9xRLnohEcGY2-sh2gA_JLZw8GRnPHxXTN785hBZAzp8qKUEf5ob-SqkB0e6mQkc966KG3agW1gsZKuzYTzHBoRoN0-AXX4CVCq1u8ijOZ9M0is8cBwOLVx3k_F4U0BrX7s3O1WFas4U3GfuA96SRSXx2Jql20zrDhXs7BdBTBRrhR8NRAOtCo-drPzYJzdaNFXzpk5mlf7UaGkLW4w8Y-e8OA-kiMU4z99vwtH3-_ZoiO6ilJv6uDfCuJO6U8vWQM7WrUR7D_me1zQefxJVlwiS86B6ZEQ8hIxTgf_C6yYPJqm_KznpZbR2IBOHWVWVKiSLtX11vZNF6V7Z3luNOZDy--5-D9A3lDvEI1sobxbbmuUK8BGAjmAXWEHKM3YvQq_x8Ho8Ayl-Ad4C-NbGnE2ngkm4LvhvFTZFCpr9kzLnkJyVeBCseYlGeS_jWlZGQK_s7R-sw2A1SfSDtNmS0jKZmWhWtMqWaLjLFdN_Bwf_KzMjI5XMXGNh1XDy7HNskh5x_s5Db-LwFZ_VdeMjzgD8V-ySYQ9YHhRVjxJqMkxIT5IUSZjrbwFBQ7wPpZWQ_As43Dg9RKKFNMPz0G2i6Vb2TlIqnhAnreudG_-Mp4-8AUKiuvPFjhqk_LhwI7SI2KxfgLT8OuuxOXDoJcIZe6ocxNr1KEjcvLUGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=flx_RHi9xRLnohEcGY2-sh2gA_JLZw8GRnPHxXTN785hBZAzp8qKUEf5ob-SqkB0e6mQkc966KG3agW1gsZKuzYTzHBoRoN0-AXX4CVCq1u8ijOZ9M0is8cBwOLVx3k_F4U0BrX7s3O1WFas4U3GfuA96SRSXx2Jql20zrDhXs7BdBTBRrhR8NRAOtCo-drPzYJzdaNFXzpk5mlf7UaGkLW4w8Y-e8OA-kiMU4z99vwtH3-_ZoiO6ilJv6uDfCuJO6U8vWQM7WrUR7D_me1zQefxJVlwiS86B6ZEQ8hIxTgf_C6yYPJqm_KznpZbR2IBOHWVWVKiSLtX11vZNF6V7Z3luNOZDy--5-D9A3lDvEI1sobxbbmuUK8BGAjmAXWEHKM3YvQq_x8Ho8Ayl-Ad4C-NbGnE2ngkm4LvhvFTZFCpr9kzLnkJyVeBCseYlGeS_jWlZGQK_s7R-sw2A1SfSDtNmS0jKZmWhWtMqWaLjLFdN_Bwf_KzMjI5XMXGNh1XDy7HNskh5x_s5Db-LwFZ_VdeMjzgD8V-ySYQ9YHhRVjxJqMkxIT5IUSZjrbwFBQ7wPpZWQ_As43Dg9RKKFNMPz0G2i6Vb2TlIqnhAnreudG_-Mp4-8AUKiuvPFjhqk_LhwI7SI2KxfgLT8OuuxOXDoJcIZe6ocxNr1KEjcvLUGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5NuiteME5P8_JaxQWjeGCguf06HoE4Q633vqAyl70tsfzVx1VlO5YmjeairkJgOm01H7ZJ7V4XE1Kzubmc8srpUOQZtFXqlEkTgOh1j2YRRQ1Q73mBr1U8IHULoNeE4BHzcsEk4MnyfW0-TL6THCiB1iWmR-guoFB50cD74vyH0Bp5hlSVN7f2wVF7Eb4TBQGK-TIr5Qv4k9qYzgCg-xFpviEn8USPEdbdkKf8qzV5tgqWx1Aq42sCBvprDA1UdxEUZmxB0I517Ti7wRUuKaWOJdphdWSvD5jrRD43Cj5mS6ULeqm41NEKTtsDDR69wc6WKv3oA_Y3kGlzE_lgIpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0H3qKRR51A3aO88xwarLsiKGEsFp5fs63DSTOR2aA7BqVGHkHomMMOZ3pIdsM8wiOq5uCSVF9-Z8MA3QN2vX_sFS-5z8CWB6Viv9uShCn6WHVtekfRPvh4E3AlTYN5U5FXOWjen2R05uRdD4kv49q1_SBdE51MP3EFa4LQ9yvm_pKqDGZtRwnpjrKVS97JqH9wru5Y1pue50GkDYq5oKVQr9GzdD-vLT4XsipEE_-zVj-1yTfA7Edsesnp3V7FVFM_6Vgaa1GTygw4DOioB9q3e_WkwWk1f-YfWNJOBd90OxkD4Edvy526UwIv1z0UmueFOFGYInHx3yBzoEO_4tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfDtUioNv9mrQV3XER7UlVxx25VXXr58_I1mlh4ZMlbDlsxEZ7QY-KSshK1rs1nGEF0Zibepq2gjdVcQoLK2QpHnHDKeLiRcMgLrc3pFtYrOso9pgR4zGV2FLSJCzGwh16kmexvGbAjphw3KeC_-MVWjEAPWyo-MW3sF4mub_a4rKx_jwpvVlcjZgggo9VRSH2tvzQa-zmDWmKqOEmV9epalZAxBEGeN8rEkvfoQFkTb9T9L2WEwECEwi0VxxuNct20HukEQcMC-ARIirqi-Pdg7izFHKaThBKbER0-kCFYi4IKXIqg882Dfmw130RI4spyuiW-haI5GWwPE43n_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ktrI0ZrrPsBY22bZ_HMkc4MHx-JfjX1o-SFLNAyFa-ouIDOUprqVyzewmTbQa0FD5fSuehynEM8Y8LVt4Kbb8qB-KMXyH7fByh_zzakiitQZNqqVikcFvxpCR-_pGJKNMwdDiy4gRKX4OvHRFchQlOlbkro51cRRYdlBAQzTDWoi3-58uyV1LsitXDZym8GBf8tDQk4pKTrGE75KThLvr7d1Ha2q_WtbUhBmVNDKxc373H0cBC-r7R5z5v6tFkb31qAbr7hxkN-SfgyQ7OvyoEc0JqmmIpIqVg_Zb-_RvmY6xYaer4CzFMbt575xvO8Zc5892kIBky2_nTd4Y4qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fib-jVv4Q4Vdwxx0W2Y_Tf5R2wVQgTWPHseHOxolcf-A7X7w5BwGACVuYftHcvKFB2EgjTW7n4kwRowjuvqcAsfEjnrEJ_YQ2pZtNe9b2ArhROKLUu9ihFr0QUtTerdZmJA9rG39D1xyG8nbPwYXKnvUtNfeVMZoh_5tKiqcVbPhiSM0TpXcm25xIa6dZggfDSc3-JhIWiCFXGVkTls-dn37YFwLqDnbVK6Q37i6oh3Vf2WRXtTEBXVvd7OuI1V7MElUIZS838RpzShn3af3zG4r2dArmVU4wRCIZvWIIpKuWwyFfRX0A8o16Y9jjjRJJS8lNHra4P_yxhOOKPsyLQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3iznBWDLR7zRYhfV6Gwx69_WR63LtEOaf6gSZal__8sdzOC8yu6QqvahrHgGw4OmkOwqDXLKn_0Z0svQnlE30-kzhmLwoYLep6V2oKha23cQ_lIeeS9XzBCWfrc47NfMJfwUxYbekC5ZHRJbQY9HHSWwVnSTjwe0oonNTPvH9ZlQvLvlTUSFSsGIK5wZ_lepOC6weAEAuBsAZEHaO0Z7B0_Ekk1uQXrmitR34y5ajnfJo0sh3nJWfc5QQHQDGgBHLtrMQxzRZtz0W6kNLDBs_c53-dZEk1xEuMqO4YgUQS9HU4xi522fHkd4RhzC314Fzk5MpXz0bYJF6eYUXAPrUC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3iznBWDLR7zRYhfV6Gwx69_WR63LtEOaf6gSZal__8sdzOC8yu6QqvahrHgGw4OmkOwqDXLKn_0Z0svQnlE30-kzhmLwoYLep6V2oKha23cQ_lIeeS9XzBCWfrc47NfMJfwUxYbekC5ZHRJbQY9HHSWwVnSTjwe0oonNTPvH9ZlQvLvlTUSFSsGIK5wZ_lepOC6weAEAuBsAZEHaO0Z7B0_Ekk1uQXrmitR34y5ajnfJo0sh3nJWfc5QQHQDGgBHLtrMQxzRZtz0W6kNLDBs_c53-dZEk1xEuMqO4YgUQS9HU4xi522fHkd4RhzC314Fzk5MpXz0bYJF6eYUXAPrUC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkDTw-EnVqDYVfyQcCBppHUIKz-4MCZpVvL0KEk7-ePLkuHvpx1yYsmcuHW6Qi9gwMcjBzVEXmpOwkbEPYbldBubClXF4P7FuZhtDoeLfwxNdvVuPh0QTHQvV8Ui1gDwRzSQV9qatGhLJthvRD1BCemYRiFIDw3JGsW_VyGYvhOyzCdBpeEyVGNj7gRx-vNWtQkstRgfwNoRd-Lu9nHjaAf2uofzDXuvDiOvxxBsR-egg3oKVL0HYzsPledezjtau7T6eBu14cnbH7adMMoY6wCor_TY7_U47Cgxk2lfSLwDijvtXaJfieGJLj88VPffzGNAJFD2V410PtYKzvwD_z7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkDTw-EnVqDYVfyQcCBppHUIKz-4MCZpVvL0KEk7-ePLkuHvpx1yYsmcuHW6Qi9gwMcjBzVEXmpOwkbEPYbldBubClXF4P7FuZhtDoeLfwxNdvVuPh0QTHQvV8Ui1gDwRzSQV9qatGhLJthvRD1BCemYRiFIDw3JGsW_VyGYvhOyzCdBpeEyVGNj7gRx-vNWtQkstRgfwNoRd-Lu9nHjaAf2uofzDXuvDiOvxxBsR-egg3oKVL0HYzsPledezjtau7T6eBu14cnbH7adMMoY6wCor_TY7_U47Cgxk2lfSLwDijvtXaJfieGJLj88VPffzGNAJFD2V410PtYKzvwD_z7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=G_KxhxOmxpMx6hNtPEgWNkOK5n3IuUmnAeh3ueFbVKVAK5yz0OXSWBSBAOLfeMhh-qV128K_DUv0YjRkNWh_MO7lJAWttfQPeOM9nMyO58ZI2fPt0mgEUx1fEpWf81eL3dV1i8Oa60GBWIZKT9B7SZzAiA6gmhu3C0q7U2YbHUjrq59qitoGrfGGZW8_I2DAh00u4REZJug4sup8KuP_48S6-2ZC2N-FmSK46qEhBFXEI_-pWK06Isvc7knHojrL4N2TqQQdeSgS2nQct5Uxs92IjMbC6vJ5m8NtDi0IS-cfI9p1Eju29t0-WMNMIcoNrdrmSYgD_C-kHvReHfA_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=G_KxhxOmxpMx6hNtPEgWNkOK5n3IuUmnAeh3ueFbVKVAK5yz0OXSWBSBAOLfeMhh-qV128K_DUv0YjRkNWh_MO7lJAWttfQPeOM9nMyO58ZI2fPt0mgEUx1fEpWf81eL3dV1i8Oa60GBWIZKT9B7SZzAiA6gmhu3C0q7U2YbHUjrq59qitoGrfGGZW8_I2DAh00u4REZJug4sup8KuP_48S6-2ZC2N-FmSK46qEhBFXEI_-pWK06Isvc7knHojrL4N2TqQQdeSgS2nQct5Uxs92IjMbC6vJ5m8NtDi0IS-cfI9p1Eju29t0-WMNMIcoNrdrmSYgD_C-kHvReHfA_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=oiS49UQj_OfX7FTdGwW-VD-CYa0EuuwZKeVhZxSI6Swfvx8zRO3iJ2mIK_oD-xnukqTvXDgghYyzcoTEsWupJpVJyms3M7RLWEYutYpQq6_AuWVDyDS76NDs6-m7n61i5HSq-coBQUuGvAGwMUSrqSVt6y2VdaEuiXtdAxI3smXKQxST05FBgoWJ7FbuhMJ-xaX_tgfG4l6QjzpPhKmpDumCA7soc-N-EYnaQecPvlz99CmaYjdyiPlOiuHsr_Ug_SHpM_Ub2y3bA-B9aE27p1xw4UJL1fADsx8w4juI2vBGmp6Ofa8zY6heuguz5xrfJFSHAZUo-9NpxjHMfO1rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=oiS49UQj_OfX7FTdGwW-VD-CYa0EuuwZKeVhZxSI6Swfvx8zRO3iJ2mIK_oD-xnukqTvXDgghYyzcoTEsWupJpVJyms3M7RLWEYutYpQq6_AuWVDyDS76NDs6-m7n61i5HSq-coBQUuGvAGwMUSrqSVt6y2VdaEuiXtdAxI3smXKQxST05FBgoWJ7FbuhMJ-xaX_tgfG4l6QjzpPhKmpDumCA7soc-N-EYnaQecPvlz99CmaYjdyiPlOiuHsr_Ug_SHpM_Ub2y3bA-B9aE27p1xw4UJL1fADsx8w4juI2vBGmp6Ofa8zY6heuguz5xrfJFSHAZUo-9NpxjHMfO1rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=V7Jmf42mHb201u4TzkB5EKKo8sEvrhvK8ihvrxWBlxgj3YlRzv8jmoStLiVKzQYGyAVoJ2nQKMT16FouAsGmE0f8oQDvvniOixMnONFGpv5HJQuDdANU18EvXxNTMBWWs1VZdjWN_8dxUJcoCurGtDrgt5O5fnTWZy_yw5XUMZo-w7ezJOAV5qC5-ipDEs4Y3KeU2nkCk4LVC980GJBGxFGd51CKFWauuA5_rfJbaMYT8yycxLlj3ValQyj-RKskLpzPnvT2VCU-JyPYEqXsOM9sVpTSbV-Is7JTE9h41yHHyipQkYS_C_M4X_641ZBZHXFdscDwY8syA5ZaKAoyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=V7Jmf42mHb201u4TzkB5EKKo8sEvrhvK8ihvrxWBlxgj3YlRzv8jmoStLiVKzQYGyAVoJ2nQKMT16FouAsGmE0f8oQDvvniOixMnONFGpv5HJQuDdANU18EvXxNTMBWWs1VZdjWN_8dxUJcoCurGtDrgt5O5fnTWZy_yw5XUMZo-w7ezJOAV5qC5-ipDEs4Y3KeU2nkCk4LVC980GJBGxFGd51CKFWauuA5_rfJbaMYT8yycxLlj3ValQyj-RKskLpzPnvT2VCU-JyPYEqXsOM9sVpTSbV-Is7JTE9h41yHHyipQkYS_C_M4X_641ZBZHXFdscDwY8syA5ZaKAoyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=YuhwIGVojLjsavGPwpPNn6-Y81hFWzQCJyQL8ce390NVbXtghzu22HKFSAgWjj5-6gbaufxOIGzigjzxZUU-Ae8dDKCVLkrg41IhkxWuC_Ac8vcSrMZrS--FD53aZ5uM4_nN3iswmpbwNMkOwUyVB1YXmg6J2nkOYxVY1hfGNg21Nt2cCXWnLFMy1Ewp427zHAc7TNY5qUPkrZTKGCxY2aUgGpyqVZjnMhM7mRm_iISHb3yvaQ9HREp5p0rLZFAfoE4rG96cTXmJt4bvh_CD_kx24g_4La1pZiMllFaIrObxnu3FPh9KqnQbYbXUBWi1Kt-Pvs8ySvVVdYqSogYUtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=YuhwIGVojLjsavGPwpPNn6-Y81hFWzQCJyQL8ce390NVbXtghzu22HKFSAgWjj5-6gbaufxOIGzigjzxZUU-Ae8dDKCVLkrg41IhkxWuC_Ac8vcSrMZrS--FD53aZ5uM4_nN3iswmpbwNMkOwUyVB1YXmg6J2nkOYxVY1hfGNg21Nt2cCXWnLFMy1Ewp427zHAc7TNY5qUPkrZTKGCxY2aUgGpyqVZjnMhM7mRm_iISHb3yvaQ9HREp5p0rLZFAfoE4rG96cTXmJt4bvh_CD_kx24g_4La1pZiMllFaIrObxnu3FPh9KqnQbYbXUBWi1Kt-Pvs8ySvVVdYqSogYUtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d32ughA9eA6fNM2_J5oLBqLzlbzKdEUE72lzhULIVcWTLkPvwYoIBa2jPQAN6TnULl9Z2HZPIafew2mCu-F8R-7P-AYRHXNaGDDeytvLHhRTiCTyGcNjkiO8eUlFtUDfOMcVt_9fT9HoJKkG2vuzIAKgtLWxDC74ZKQ2e0zc1iFTYXVub2Cp6_S-UaH6krzOhQMpxa3wornMAJJENTTVeLy8K2C--SvirLw9UDsxfDQ7GUUkLL3_bN6k_moX1G-q7WEUqoIORPNko2lsNeCICny8srtF-3sxxqVsyeSU5RUp7b8KRoxsjbyfUlQxtQEqbfKtEHbNNSiK6GKHHRrXHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNuRq4lwcXiRBYb1iloKKTZLFCnhUDvQexdVpCsLG88ukgdh-GMq6X5o_nYZ_JzGAGMgVa8rcnfcbgg901MnUzLBJ88lRs-tMyPNb2GR9QGAzdBbaneDr0peZcywsBHJunjTZqBS7P95GFJqGFebAcrpE73S7W0VV-JLfGo-db0Y914An0krcOh4GRN0yTMfeqFXLefjEswL8MslfTbReg3b60O5TD81nQJv6Prxf8cZL_tZk2LsMLf_sypPCRhWm4h4W7Xf_NuUtg4AcScC_movXjJ8dv23gXdnqGOu0GKKcaZJ0iK0KXsLoUY3VG3zy8d53oHpAI1eBz8smbfZWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Qa8GcGahObRvFdHllWB9deCbHiZ15VdRivu2mb3ezLxeni44YqWMcTByx4AKceFCUT-asnu6K9VD2fyBqC_A384SUxBDniG7HkURoLUxVD_f0Ix2YKdFGeNsepnN0c-ExMV-_4gjWqUNnHbkUmkid_Ukl5YFwLi-Gqz8hDC2SoSxfvuJ8aVcBrR89u9VTbZB5Gwcs2OA-QEy653_Ic5cKnt3qDrRx2ZroqPiDiUq2iRm68Snx5VqYSPEVQu0wYm-huBvm67yNri4Evdk2QtoLkiDNi31F55C3IfTItP6jvQ3kpMAspPR21cLIDa_8eGyrfxGcbFxjPmcKthLNLzNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=Qa8GcGahObRvFdHllWB9deCbHiZ15VdRivu2mb3ezLxeni44YqWMcTByx4AKceFCUT-asnu6K9VD2fyBqC_A384SUxBDniG7HkURoLUxVD_f0Ix2YKdFGeNsepnN0c-ExMV-_4gjWqUNnHbkUmkid_Ukl5YFwLi-Gqz8hDC2SoSxfvuJ8aVcBrR89u9VTbZB5Gwcs2OA-QEy653_Ic5cKnt3qDrRx2ZroqPiDiUq2iRm68Snx5VqYSPEVQu0wYm-huBvm67yNri4Evdk2QtoLkiDNi31F55C3IfTItP6jvQ3kpMAspPR21cLIDa_8eGyrfxGcbFxjPmcKthLNLzNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdtAgya5DEuiodt34bmxeGLksHX05CPPDQaSvaW-hOJN8nlMubU3BBXhTRw4pEySJt1JLQX-uEG9M7PGYw482hRoQbtJXxR-nnNSwWUvabRx7k4SenwMqencrp2Eyefle4qljv_WrNIz-pP3I7-jKJtrw-4619xN8BE5Bp5eVKn_g9hCObHPwNEc_G1M4XATtxh0kUWUmQMBTOfOBpZhoVZy7KMoqMvjTI4DpfJx7-QgAHS-og_Owphcm9spTreRr6ME9NMy8BZClPYEangxMDG9wG3BHWneAF2CbF_4avStE4j9D8tubZEnFd4LsXqlvP_hi5Z8qVsg5_64Ed4iVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAjG6H4lEz9cE0bcTcKvwjK-I1UAk8Pcbhuv1sgonekplGLOGjhvPDDuLIui86XSXBt_I49wRR6cbwtykYR2J7gp5W1QgqwwstH_NEp4djltc0l3P2XR5iIBlnMvA91qBMsOJ83qhkPSRNkKNfG-U4Sljkw4WTQ8oJBABTgcowxJtNFwI7M56QGoMhBRja-oSefaP-RB7wqye7FIv42svkeV3HQfa_9NOdnml0ffaQd-6Q95RWnEonNDGxQtRiLHgxFmZrps0t7o6kEnr-TzdrpTZpCU9lMG0Tn8zyMTqZODV7p2BwlDmlG__MGQa4LHF3U5hDzY-St24yQVmh61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnU1CbydONHo3EYXHxRVQcy80D_qyi2PXU57fFMpf6SrEbVfH0mJ5b2GKEQWHinrjiWOtZi4hNxhlMwH9nTI7yqIs2NizbF_kCGVn9JNecZPZCgFzwqTsoSo6S-GawaWuQ7LdbVhGrBXYddqVdcuDcwJCYaB_MpMhSxAqU4mRx0iJEI092Lpz3qnzi8NSHStHiNBFlZGZy4hYgaDkpAaLCFNwVaV_QLePR9SzNEFfJK8JjOcHdyWAqErBHXtSm2J3HSfYZ0r3fEGTyCbBZUSuL-ITeNDgjXUjHqupwnFF6Ra7VRLZxWxoSwdqx31Mq6V_-QV2nH5n4tL4omPwjFMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jABTfIWGJUNaHdmeAp94Y83W6DhLVzdHwd324ZbnVPDaipu7wzlZFf6oP7rmFh3oGLPCH8lxO8iZtAq1lBfdo4eBVeASroiCx9mjbWFBW5uobIt8TZuc84XX9jTbh4Zkomt9tpjKMoXncRyNu04dke8hMqrJ2IvyBR2VhzOQ5NL9XG3SUCRX4sHKi7IBTRkXUKnYulR3VKpc772fPHall3UysmK7MoeolpdvTLavj1anPAIf3bOY-khCphvzreRBOHEoqVEA3HX1Ome0hNW87VNu5KsuXfvhCzASxoM26tJ1aEj1A8HHKmPYpfCbvl7TophJ62Merrko_egPni4qKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8iZBlE36iGQHmhHQCC5N7s4DAaThOFsMZd1CfiSNYJudSC8riwPswkcKPulE1VicD10cDb-pwAxHeAYvJIMYzKzUA5b7GdZA0hNp4pkBOM63aRxjpGe3GDpwhQmB7-C8Ic2Ibpj6mZ2BmJe26tFASi9q8Xot74-6Dwo8j25ngcoQPXCv6ACq2GP9Hxi4YwRkGOxw7LT9nPYy76dEkPJXumOzACTgesXcrIm_7IqASkpwbv6czlQWktkE8EfVXhHcU3eYXmnCkcIGl87BU9XKTQkLq4bC9D38n6hX7oB4hFI1tzteJhZ_K0mVqfIFCWbHkRPa0kZhbKBDWLk-LoIuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCFmuBEwIiqw3hFEEOTr5AG0raASZ7KICRQpdne-hZouy9dicEE0v4yKz9BFLNkVHK6AgKnyLwUzlmXcWU4fymikJDNculwxglSAQrOmsyyk008MTaqsltYL2xBUknj1lZ6-IQufL6gQRVV7fEQu1O_heRIFAm67-Z1NDIm040Pdna2pPCbfunZhWJUZx_ZVpDEYd6OpT6Xtl-wu29BqWemG1816Y06N0VpuoeLhl814DIpApc8nL3HokSZj1xD505x1PC_c4cmgOAYY4isCnQ8wx9Qx_-Ud1MGb4joOVIOTzrNjsf02ZHMoBUTzSo4WNhBWJh500JwI6CNYP-DS6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7NScueDL5gOQ9-0wNvkK4eu0wYIejoGnSwOskkZu8--aZDajm3ELGMTBwQ6mnt90oe-XW4AVwYh9XWaWGSBeCWTuaPTIkaMiDfo6tghGyNc1wNOFkFKYIQJcYv1ueo9c_o3CSbagwpcFTKwidZ_JgGTDdUKsCt1--AVLaabfX-YSK7jqYQYCT5_6TJMXdYHN6GF-0IsBKiYFckH527BJvfYXKw7Bz-FGR1m9CQkSlh1YGOD8li99DDHypAuig2ISHMyoHwVDxzHIeyIOwwvY-sw9nlUMgw45gGIBZJ0QoBcWpPg4g0mjkgTQFaQHK1XZt9DZJLMkeb9Th_LvsZOmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzs52PVhDypmVB7ygwRN30XHWoPqH4YQcedUt4yLz2zepRNOndjA88zLdfZmm_ahT6aW1MCaKSvSRbBTo363aog2I88JIu4uZ3Gl8AXdTf7iTscW-QNnYfnAV9PbSicesw2eJ2dieNDbDodCliDMFuysS4VGJpnUfQFAfJp34sJkTj8OFwjUz-8_rBhUenov5CvZPMWX9eEwbBGLjmG2wuYv9EU-mS2_aPtuoaC6Xr501JpIvpCyFukqQsOiaaTV9m-zQLXZUsH5egimfx7tA4EExe5LwgSa_ZQsZ3DjeB27TrS5ymAuGMWwOtis0IqAsehUhVNIZ8PV2fzC_ubhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_bwkwWoD7-lejqrWEQK6oGg_8ZFCuKXEiF_aHxLdCk4xraDR3dGn1v3jkFhpnJKgjwx8c7Zo9uWWwGoOG2enA4UOf0P83ci3kKtcYm7_QScxLmezCu0G4WB50h2k6uHydtu2ZZCkAM_zgD6949lx5bbXfMhLwINY6CM6jHw4ChkE6bwDUoiSj44I7Wjr_-lCSx4_qjWH_B8Pbwu1CNluOPf8m9W_6f4c6tCKKhhzxpWPUyRCTuUYHJWLl3D_xPbdD6vj8tttaGv4KeZdo_Au7EaomM58V5SXJUtWVW_Kbudbkd4RpZBL4x_XUsDlQJXMuMqP4iJXXT6ChsKxbbnPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWTMTqZqYtRS5NHHsG35Bt2Q8XjvQamKeyg-w8Ev7OHQDRJFYNKB6ysn1aiic6r2zIvDNQxBwPsvK7bEbuxAHW6s-Ys9605Ld4lcm2a_6hxUcnqCKCrxE_i_GMnkGy8mH2tIza_CW-YPx1rFpumDWLXe3Rws5djyCV1-mizbjDmjR402GhoUR2ovG40xdMuGhQ8r9-nbQL8edqSKqAi38DNyfoPZM0csUyUAfpoZ0J3BgViKCj3EshptOmFAbupafBIL7bdWVN2x2U7h9XAyHS9QYUA1ev60N2rHUOnxJatU05u5ugVcXVZD9JDx-ALnV523ZuJS-vfO777v6O7cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
