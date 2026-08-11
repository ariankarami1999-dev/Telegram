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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 12:57:05</div>
<hr>

<div class="tg-post" id="msg-680264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmvASZvgROLuSd_PTMX-CFr_zf3duJ-7Yiim9nupFPJdAA27MoLxgtaU7gxRpfbBMPZrr_WGwSxWkeGO2NQEQg35bdcSHJU0qgIeMWA-8J3E0DFAE9N6Db9QcYyoalKt2zmk33yC43VuXrgpkqjeqK2LfL6yNbmfYnhLLyqT3cBgJ-ldhdDwhu0b0Ngfyn6BBFBwa9fo3kSjx1npDjHGcxc37Gmc95G0vArTmhhTVx8iwQoBTiq8Jj1tdHgQtA1bmqOa2N191zpNdbBxybnT7Uxer8Jycruaph9OT3oKpnoraQ--aw8DxtMlbsA9OTBXimHWkariicC5BJoUssXu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۹۰ درصدی عبور نفت از تنگه هرمز
🔹
تولیدکنندگان انرژی در خلیج فارس بیشتر از قبل انتظار دارند که کنترل ایران بر تنگه هرمز، پایدار باشد.
🔹
عبور نفت از تنگه هرمز از ۲۰ میلیون بشکه در روز پیش از جنگ به ۲.۲ میلیون بشکه در روز در هفته گذشته کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/680264" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپشن‌های ماشین‌های چینی تمومی ندارن
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680263" target="_blank">📅 12:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDGpt238vYOlQeq1Ff1s1zPamH3pwQy3PYlftgSd6V85pS2V3cGzo7vBtkQOfl8P7zSOkOIeszBpktTqdN_8gnwE2mq4zZukOJa-uQuWfaofJwLRscNiMKPYcCwXbOKProaAy1cKXWkAC0w3CgD2_oH57KeWnOBT7EGyMF5gwWxv3UTPTkNYC76wcYfT_jUpOPzrVy9eQ9ZU-jrrpyygx1k5Xy5VdA3Appg9vxMNfGRXsExPtpf0w1-9NeVm3TUg6usCplk18DGWogEQNNtiJWHuUItCngRLO31OxXF9FdjaJTbBaVPQYd7oVL_TxcfZjp50a2tuozkgzt_f5urARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680262" target="_blank">📅 12:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEx41BSC9998ltvsvim5XrwgxEj8kKQGPRe4M6r5VUyMy94zvvQWNuEHQFWqirmHWPVQa563vpRVJDp6GAOMIkSwl7GmCg3eAb1bDUG26EzfPAdyzerTvVvqda1JXnab7UhdyRwqf767zAdDwRKWWg4JbyzFow6UhnkjOJuP2n6yvr6j5cjqsmTlIFSaac_zXu44yWGk6f1IXMxUVA6TAY6LgbLARYkS3YnIGd3MKq9j_PEhm3278Ej121LwCJo7k3ZJWB9CsdHq0LT_n1DVFSgFqJSyj1xhl5fis7menwUYmFYSYqzGfo5aJJRgjyHd2exMyXLkAVKQWsxphI4v0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول پیشتاز توسعه زیرساخت هوش مصنوعی
🔹
پایگاه خبری رویداد ۲۴ در گزارشی با اشاره به نیازهای زیرساختی هوش مصنوعی نوشت که آینده این فناوری برخلاف تصور عموم تنها در مراکز داده یا مدل‌های پیشرفته ساخته نمی‌شود و به شبکه‌های ارتباطی قدرتمندی وابسته است که داده‌ها را میان میلیاردها دستگاه هوشمند جابه‌جا می‌کنند.
🔹
بر اساس این گزارش، بانک جهانی چارچوبی با عنوان «4Cs» را معرفی کرده که شامل چهار ستون اصلی «اتصال»، «توان پردازشی»، «زمینه» و «شایستگی» است. اهمیت بخش «اتصال» در آمار کشور ما نیز نمایان است؛ جایی که تعداد کاربران فعال 5G همراه اول به ۴.۴۴ میلیون نفر رسیده و ترافیک روزانه داده در شبکه آن از مرز ۳۸ پتابایت عبور کرده است.
🔹
این گزارش تاکید می‌کند که ضعف در شبکه‌های ارتباطی می‌تواند ظرفیت کشورها را در بهره‌گیری از هوش مصنوعی به شدت محدود کند؛ بنابراین توسعه نسل‌های جدید ارتباطی، پیش‌نیاز اصلی برای ورود موفق به عصر فناوری‌های آینده است.
لینک گزارش:
https://www.rouydad24.ir/fa/news/465938
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/680261" target="_blank">📅 12:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X75AR_ubebKQ4O0p5WTdItySsEG9sswTqWgXeW4Wbi3gnsAxGz19E8ts54VldkNbL0wLsLIfs3sXuEBjqPBJp8cE0Nt4tsI8Z5giU-qitGXe1WnQnFnoviP-zBDgE_RshY7YIZW8-8BAleSxp7jvZn_6V3tbRAZ4XF1uI-_N6CVcd_QBYhy7B8k5BKHFbG184UR3ADyYDC2vfqQDf0hy5flsjh3R54XqWBb9EcV58OZrBjnax8xhgCFo109Kzz5_v8EOrMvrkI5v6VhNsOHIQfNcgOEmfU4ejfKXj4hITmhv-OmFfTcNfqC5VxdbeOif210v3ERcmVVRmn5mTlfjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با رکورد جدید هفته را تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۲ هزار واحدی به ۵ میلیون و ۷۳۷ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/680260" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر ارتباطات: با قطع اینترنت، امنیت تأمین نمی‌شود.
🔹
استانداری خراسان‌رضوی: ورود ۶ میلیون زائر به مشهد در ایام دههٔ آخر ماه صفر پیش‌بینی می‌شود.
🔹
فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات امروز در بندرکوهستک انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/680259" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680257">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/680257" target="_blank">📅 12:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680256">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109fd84ca.mp4?token=qC6ELezqVhJPsSc6rumN8thKY5hUqiM1CDiMRW3HqVxBqD1T9YfvhrfBGAWEFXDuwJTGY6i_qKylcGXCuq1dA4ujqlVBy6pNyD4z22EPYFYofaEJp6Odwpb9Dz6PBNbbdmJ1yIA_qbtVas33gzR1GvK7s3NnpEdflbJggXTtLIzPu6eA9eGyoMZp-aSiq2ei0ISRhyGGR09DG4FIMf3QY8rUjeCcC5yzuk7a4NUTj9Y9cDvXZFwOb5OM_QR5esUKw54rgvgyCyuxevy6A6DyMo6MBFA9FhCpreY7Qet2_AlGc-EsxcQBiqfR_HMhFIEiwa2bfIE03doiK0p-TU2bfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109fd84ca.mp4?token=qC6ELezqVhJPsSc6rumN8thKY5hUqiM1CDiMRW3HqVxBqD1T9YfvhrfBGAWEFXDuwJTGY6i_qKylcGXCuq1dA4ujqlVBy6pNyD4z22EPYFYofaEJp6Odwpb9Dz6PBNbbdmJ1yIA_qbtVas33gzR1GvK7s3NnpEdflbJggXTtLIzPu6eA9eGyoMZp-aSiq2ei0ISRhyGGR09DG4FIMf3QY8rUjeCcC5yzuk7a4NUTj9Y9cDvXZFwOb5OM_QR5esUKw54rgvgyCyuxevy6A6DyMo6MBFA9FhCpreY7Qet2_AlGc-EsxcQBiqfR_HMhFIEiwa2bfIE03doiK0p-TU2bfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده از آب‌پاش علیه مهاجران در مرز لهستان
🔹
نیروهای مرزی لهستان برای دور کردن مهاجران از مرز، از خودروهای آب‌پاش استفاده کردند؛ این اقدام با واکنش‌های متفاوتی در فضای مجازی همراه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/680256" target="_blank">📅 12:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680255">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اتومبیل کایزر دراگون؛ خودروی کمیاب ۱۹۵۳
🔹
اتومبیل کایزر دراگون (اژدها) در سال ۱۹۵۳ تولید شد و تنها ۱۲۰۰ دستگاه از آن ساخته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/680255" target="_blank">📅 12:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی پنیک‌ها خاموشن و هیچ علامتی ندارن، اما می‌تونن از درون آدم رو‌ مورد حمله قرار بدن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/680254" target="_blank">📅 12:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQQm2pFdvoVLAdSXD83nDPbyQjdpch4T7e9STVvPn1xkur4bx5S-u5h0-0ZsfHJdUH0NMf2l5o8VJJZK2-9tjW-Z1bc17esW38eQrSONUr3ZfWcJ3cQtkJIuEuaJC3TJNjtdLV2i87cCIYp0XVp_1ZN7UvNNaUuxDQlDhkfpReUREMQFS18R9QLqCU7GWXlAoR5yqXLFMykI0-GKqK5x9kBvWeRk5YflI8M2sr9N1WewUeUdkbYqFsNZiAk8NbF89hfQiW89pzxVslbYJAMcV8P137p5r-6zhaf1YaIoVbNcXxcFujmZqq2ERisxeIXoEtslZZ1SntC0T6jU-Sps6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون قرعه کشی، 50 دلار برنده شو
🎉
۵۰ تتر سرمایه معاملاتی، برای کاربران جدید ورسلند که باهاش می‌تونی  ترید کنی و سودش رو برداشت کنی
💸
🔻
فقط کافیه ثبت نامت رو تکمیل کنی و به صورت آنی، 50 تتر رو دریافت کنی
🔸
بدون قرعه‌کشی
🔸
بدون واریز اولیه
همین الان ثبت نام کن و از 50 دلارت استفاده کن
👇
🔗
ثبت نام در 5 دقیقه
🆔
https://t.me/versland_io
🆔
https://t.me/versland_io</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/680253" target="_blank">📅 12:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k54aBWs5Gac2JL2Q4AH_5TcsOIhRG8p93fkf3gVFSaVKWiFmN95ndQbRbTDzCYWuM0KjhWWv4Vm2Dv4t3X-P7dX02oP87q4qM4DNR5FXR2SGNoUEr6KxTieNdHHgARXFxV67t0K85bOBeR8S34wuZRNNQOiwP5NfAEzTio-aXQ4MClsVunbTdNi6ILK1i7TwYfmgv3cktu2s7SfDhdLkeWVErsyxinpj6OVhQ2Eb-P1vPbvv49OdyaAJ5fOetV_A2VvpIk4jalYO9jt8-dvi85_2cTunGei0yrMBt3MxUeUwuC4ekh8Z4KxOy2fUoUnlaGqm74YCdf46K_gNbM2G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشار اسد به اعدام محکوم شد
🔹
دادگاه جنایی دمشق بشار اسد رییس جمهوری سابق را به صورت غیابی به اعدام محکوم کرد‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/680252" target="_blank">📅 11:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAh_-Jztut5HXf0LBg-pS1nqWgqIyk0nb6bclEVTPzgXU9D5s8IlDy4PyygCz9dInohpQMTj-VNAc5RJSXhhNvGTuirxCKBirUamOeuoDm_A1THFEKSP8n5bXfx60nnnZIKh3ex_7botc3-3HH-Dvoo-o_lhPKBLVcKINS6tuZrzqfIf7i5o_vmpQ2DlMXe3hLcBhDSDG0mD7pv7dJxUCFnflWVDCB-n2T1AB6oVLQDhrK4-jI_Q-WEwmGqiKmGr7POKrN65LLfRyL0thnb1OCIrTtkoDx2jP1w3oCpoNiMX30cFfcQrh7o3riAnQV4LADPxkVYZ8ylAomfVg7GQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت از زیر ۸۰ دلار به حدود ۸۹ دلار بازگشت و به مرز ۹۰ دلار نزدیک شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/680251" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف در نامه‌ای به پزشکیان خواستار ارائه فوری لایحه اصلاح قانون بودجه ۱۴۰۵ برای تطبیق بودجه با شرایط جنگی شد
.
🔹
استانداری آذربایجان‌غربی: حجم آب دریاچهٔ ارومیه نسبت به سال گذشته افزایش ۷ برابری داشته است.
🔹
وزیر بهداشت: شرایط موجود کشور برای حذف ارز ترجیحی دارو مناسب نیست و نیاز به بررسی‌های بیشتر دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/680250" target="_blank">📅 11:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RykvMyrkPQRpvOPqxnddRxNOQi3hsvw_l-qYHvE_6GtVaYKghW1egUw7QX-_mJ9-Qj0rdABKJwTy5cAVL_1BkHKlzWd8H3dD5YDxb_2vemQK_G-2mU90o5mXf0pJNaf418sSS_6uQZbZdGI5k--CV8gVZJ-JKfSjmcGqfXCHYbL-7WMQpRLSS6Yh-_GyYg7cYbkfr_WJaCcG611Tu-4g0HpcN9C6sH-yFyp41uPQjNOEIVu26aEaVT1nOEbixUmcTU9IqJs6H4KQkLAXX5KRO6Rew3SlfXWU0UnkDp1pk04B9G-eetfgJmfNKoWAfbKQX3LZ_Azx-rT7339_FzbriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRHs8ZMTVyzTtIMUfOIf-CD1QoX8iGrZBAk0QEZglZq09qpnJ0GG3xW-2Ez_NhKWvvCHX7tK2k-4r6yzNQmIlD-1-M2VcwEvl51s6yPmcfGet_E47HhhDaeETEMsdz6pFzzPbxXhibMaZgfsjst3uM5tl9CP0oLuFLw1r1DdEc7M4o8HXAypVmHJRxAhmJYS9l4rPLNchtiGCVIqxVCWChqhodOiSHhaUaxqgYeFl5s0EOSyAAa2ANtGAMOXQghQ3M1-u7bN9rv2TYn__fP-l1_Nsda8Dwb6gdcXCuHW3kWzqa4Q3RMSQnPQ52dzFkRIOSorDSP2szxv5cZuSGH6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVzczK5e9mjIwi20UNsKISMFA_b4lCWOj3NcAte5YgEhfxhKbp7Fdu062LYqFmjNhMHtN_GBGlMvN3pD3WSyhfZEd-kbNEvm08ogQowjpxo3OllD7QOCVtjaTcO4A9j-NCebA2mEYs2CI619r0v2J8OpTPsrl6nc65HNkI14MZ0Fen1vvi3FFAfZ7DyjPQbLiWpZcpybQGlQiUgi0FInTHrc1Le6LJdVenQHQkGr3rTSveqcoCUHVl4Wdd7eBwJJuNwYA12yyGQNzW4aDRJMG1CebUZ7IDMYhDezWaNo1Nuziuqfsq6y-BS3Wyl0lhD-ndYjZO_DLOaovmuGEaqM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDqCPpLfOXPf04QY8gVc5NUlhQlS99hQyjWWDeoHyO9RSdzJ_6us8LzRWNeU7cbKu7M-JChx6O82xVvpeS6iB6DPMBA1Nq9hByYr8yys1-6AlXqTa_YS0yILV4817YcsdFGJn6BPOJsMZQWdXLwnxM4l2fUj7CSd-XvLFP4Ez8Lu46VWSdBCp77cuTEdUxSOZf6abEKsqaV8NFqkEzoEQ00oQTmKnvpy1UfHbCnd2MMKkLEGxmqhrdgMhUL-X7jhZQ-sXd6axQmIre76hRjHWX5mhZutPTGovpT9-xNuCQrYgbLHJJp3tMUNne1CCG5MP-MYc5GzVqSxxcG619dsJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوشی‌های جدید سامسونگ وارد ایران شدند
🔹
گلکسی زد فولد ۸ اولترا (Galaxy Z Fold 8 Ultra) با حافظه ۲۵۶ گیگابایت و رم ۱۲ گیگابایت که جزو گران‌ترین‌ها به حساب میاد، حدود ۴۳۷ میلیون تومان قیمت دارد.
🔹
ارزان‌ترین سری هم، گلکسی زد فلیپ ۸ (Galaxy Z Flip 8) با رم ۱۲ گیگابایت و حافظه ۲۵۶ گیگابایت، از حدود ۳۰۰ میلیون تومان شروع می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/680246" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
کاهش تردد کشتی‌ها در تنگه هرمز
🔹
تردد کشتی‌ها در تنگه هرمز روز دوشنبه به ۶ فروند کاهش یافت؛ در حالی که میانگین ۱۰ روزه حدود ۱۱ فروند و پیش از جنگ ۱۳۰ تا ۱۴۰ فروند در روز بود.
🔹
داده‌های کپلر نشان می‌دهد سه‌شنبه ۴ کشتی وارد و ۲ کشتی، شامل یک شناور LPG و یک کشتی حامل سوخت، از تنگه خارج شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/680244" target="_blank">📅 11:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVIG8JLScQMZK1uoTQ-gV_G5VTb-rEFQw38hW8wM3ENB6SQDOKlVP1CX7icFnAFPEDnLj2lfWnPYSKW5SNKKr-W9pKklF1BKKMsUqLGHu7OMFV9_f2BLlYt5QEocIuEXBitxvvtHA7GA3-waBT8DiaUB3IE15agCKUkdEgxehiN1X9cj49o7Y0s3EAbB79d-m3AvefjNSRDrA0OsZmkxcDmE8G4Sat44cEml3lH676VDrWQj-Y9D4lkHGP_f2DTnP86HRSktO7gBxSuEFzV0kSKfERfxJc2j-rbS3H8MO75IcAsIM0wv0fVDyOodEHOOzJo5jWxpqboLTCPkEcMjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از سقف عمارت هشت بهشت اصفهان
🔹
علی آذر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/680243" target="_blank">📅 11:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا چطور جورکش ریال شد؟
🔹
وقتی ارزش ریال پایین می‌آید، پول مردم کجا می‌رود؟
🔹
مهرک محمودی و ملینا جعفری از تحریریه ماهنامه پیوست برای آرش برهمند از عددهای بالای تسویه و برداشت در پلتفرم‌های آنلاین طلا، از جمله طلاین، می‌گویند؛ عددهایی که می‌توانند نشانه‌ای از تلاش مردم برای حفظ و مدیریت سرمایه شخصی در روزهای بی‌ثبات ریال باشند.
🔹
اما یک سؤال مهم‌تر هم هست: وقتی طلا از گاوصندوق و طلافروشی به موبایل ما آمده، آیا فقط شکل پس‌انداز عوض شده یا بخشی از کارکرد پول هم دارد به پلتفرم‌های طلا منتقل می‌شود؟
🔹
روایت «پیوست هفته» از بازاری که این روزها طلا در آن فقط یک کالای سرمایه‌ای نیست؛ گاهی باید جور ریال را هم بکشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/680242" target="_blank">📅 11:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: تورم در بسیاری از استان‌ها، ۱۰۰ درصد است/ فکر می‌کنند با اعلام آمارها، فضای روانی جامعه آشفته می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
دستگاه اقتصادی ما نتوانسته کارش را خوب انجام بدهد. همه گرانی‌ها ناشی از جنگ نیست، خیلی از آنها ناشی از سوءمدیریت است.
🔹
رییس اتاق اصناف کشور روایت می‌کرد که همزمان که یک کالا از یک زنجیره به زنجیره دیگر انتقال داده می‌شود، یک فاکتور الکترونیک می‌دهند و یک مبلغ دیگر در کنار آن ردوبدل می‌شود؛ این بدان معنی است که رانت و فساد انجام می‌شود.
🔹
مردم از ما بیشتر می‌فهمند و می‌دانند و راهکار این نیست که پنهان کاری کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/680241" target="_blank">📅 11:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کارت کنکور سراسری سال ۱۴۰۵ یکشنبه منتشر می‌شود
.
🔹
هشدار آب منطقه‌ای تهران؛ همچنان در دوران خشکسالی هستیم.
🔹
سپاه اصفهان: احتمال صدای انفجار کنترل‌شده در صفه و بهارستان تا ساعت ۱۴.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/680240" target="_blank">📅 11:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4dd75d13.mp4?token=H1wDdeOi_WWS9hBQTNn8hUltyXx6Pece5IbwZZbgEzIbsz2PRTPxpTYgw2AOwA3Hjyt84EMGhO-5TFlwkLRGAPnW9VtNbm1pnFmA5OCSbXb_7wjrdl5iKw0Ony3q7RHgWet8bLj7InnX2UrRSSo9emVytrmpzixMYisL5qRMPpCzoWCvTWgaRbfkicgy46sPldH443fPOrovMIOeGqSXADd8mCnU1atwz1W4K5b4tf8eccugotamPsEHbCr7YjAgA9sg63qFjaRA6rp0uWOmhF3HQOVf8zxRReRVt96Ii1l1ZKwiAbjkAKh8gzbFnlPR-s2Z3O9fpwoxg_0E-bHdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4dd75d13.mp4?token=H1wDdeOi_WWS9hBQTNn8hUltyXx6Pece5IbwZZbgEzIbsz2PRTPxpTYgw2AOwA3Hjyt84EMGhO-5TFlwkLRGAPnW9VtNbm1pnFmA5OCSbXb_7wjrdl5iKw0Ony3q7RHgWet8bLj7InnX2UrRSSo9emVytrmpzixMYisL5qRMPpCzoWCvTWgaRbfkicgy46sPldH443fPOrovMIOeGqSXADd8mCnU1atwz1W4K5b4tf8eccugotamPsEHbCr7YjAgA9sg63qFjaRA6rp0uWOmhF3HQOVf8zxRReRVt96Ii1l1ZKwiAbjkAKh8gzbFnlPR-s2Z3O9fpwoxg_0E-bHdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ شیاد : اگر من نبودم، ایران به سلاح هسته‌ای رسیده بود؛ مجبور بودید آن‌ها را « قربان» خطاب کنید
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680239" target="_blank">📅 11:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6ca5ca28.mp4?token=uut-sp0MGMxuMbkVdSBWpNa3bI4gmDR0RlZNDkqoHmsnKMzC_0FI7u6GB6beuwVr3PnYzQS3IEyT4ahdzku4XdfButQsPeyzL7a5YumMvor9xuWu_jdkD8Vcskx_R86YEtQBgL_DBzQBbBDVUvpWy48kVRsdVEh7GA4n3cLLt18S9cCfG_4iEJFSBdB-ZjB2lSN_51oTm-o9itZCQJeQF1msfyAGrdBA5THFZDX3ULIAtmcQVyKQvPuOclIPC9BPGqvJg9qhAm2MxRKxxSRl570npmSeN8bXVFj-ecemmGVTZmB0pJnN6XxOWzjryhud7wdPxU-Co1wjulKyNjEBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6ca5ca28.mp4?token=uut-sp0MGMxuMbkVdSBWpNa3bI4gmDR0RlZNDkqoHmsnKMzC_0FI7u6GB6beuwVr3PnYzQS3IEyT4ahdzku4XdfButQsPeyzL7a5YumMvor9xuWu_jdkD8Vcskx_R86YEtQBgL_DBzQBbBDVUvpWy48kVRsdVEh7GA4n3cLLt18S9cCfG_4iEJFSBdB-ZjB2lSN_51oTm-o9itZCQJeQF1msfyAGrdBA5THFZDX3ULIAtmcQVyKQvPuOclIPC9BPGqvJg9qhAm2MxRKxxSRl570npmSeN8bXVFj-ecemmGVTZmB0pJnN6XxOWzjryhud7wdPxU-Co1wjulKyNjEBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: در جنگ اخیر نیروهای مسلح ما جانفشانی کردند و بزرگ‌ترین ارتش ظاهری دنیا را عاجز و شکست دادند
🔹
این اصلا شعار نیست؛ یک واقعیت است که همه دنیا به آن اعتراف می‌کنند.
🔹
در جنگ اخیر، جمهوری اسلامی ایران خود را به دنیا ثابت کرد و نشان داد که یک قدرت سرسخت…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680238" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680237" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ کمبود مهمات آمریکا را گردن بایدن انداخت
ترامپ شیاد: بایدن با ارسال مهمات به اوکراین، ذخایر آمریکا را کاهش داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/680236" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هانتر بایدن: نتانیاهو تجسم شرارت است، دیگر نمی‌دانم به مردم چه بگویم
پسر رییس جمهور سابق آمریکا:
🔹
واقعاً چشمانتان را باز کنید. برای یک دقیقه قلبتان را باز کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680235" target="_blank">📅 11:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680234" target="_blank">📅 11:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عراقچی: هیچ‌کس فکر نمی‌کرد که ایران دشمن را مجبور کند که برای مذاکره درخواست دهد  عراقچی:
🔹
هیچ‌کس فکر نمی‌کرد که ایران بتواند این‌گونه در مقابل آمریکا، با همراهی رژیم صهیونیستی و حمایت بسیاری از کشورهای دیگر، از جمله کل کشورهای غربی و برخی کشورهای دیگر که…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/680233" target="_blank">📅 11:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEJfLubjWESKU_7yjZGkalWn0CgjjjuxIPhPWeqX9bus17IyYrD5__oGk2a9isYmHakblBvREtCCFeo7aXA1fItEv38A7IJN3B8CYi3y3ggKyAtYSVoWKe3nfo384vneBVPhQRg0k6sqo7A2AwU7addQomCucOSXA47f7b1uX1ObEPzin2k3kRQWKqgBjgVrfdx60JJ8E6NhpxH1XdYAAAvUF1avz6NVJXIxZI39ihsdX4ho8Q3YCjaiAr5Fvw54ND8s08TdIuCmTsXuktyIkOx98yYNBXGQtqpBmWiYQ_OlmPjHV1mvGXJCO4FR-EaS4c_-mGBCLzMIHq__vhtpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sskarh59K3_S3UIgxcX8qEoWmfi-eNwBsTl9j6xy-CTZfu6faA_aSH_v26_v80ZHAAVCmUB1t926f-tpgUpYDjslrZRO-I0JdzzDZAkK45LKpOSPTj6KF3G7ifOyFjvJjl9iBclwg5YJMoHUmypMKrwIkke-BxP6eXxn8q4t6Zg3-FQpvF9SSAcRRPTjpVLbAYp_Eny0Y7rrQagFeoxvAg7z6D-jaw90fIfvf3B4Wp6spt76QMtgvbe-1hsYqnVkiESBOfKpXaaiXU11DV9USaieJ8UjQfZLCidr1o5dsLfyixcVlYA88nFMZljEFdfuzL4rBKIEdYUHIN1YFsFtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghPdmmK6_miedAEaeteaNqEN3WoTQrqZJtvy12OUYJaB4cphSiTbdjxQLmsyV4IgNlbWsRE3aWcRnjYY3gVRyMqvR3db1QFSzEXmi7WzlMCxz8tgVTMkANYYWMKOed4-xvwQmrTogKqpG7WioK6HU_SWgaSF7Ax2kMKhEL3uxPUzu0MV7XwT42EZqlL2okGhf6G7HLZWzBntnDldUOa5hsQJdZHjlUG3k-NoRsLxNbPfL65oTAW2AgdgssihJmGz6hyJ0xS3UFRBUa9sJy6GqqawlrToF0hMTcxdQmZNTmF5uam4TqDsfDo5I8G-d6MIr7Um7MV8Cv18zqYtkvRu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت تاسف‌بار بهداشتی در منطقه گردشگری دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680230" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
عراقچی: ایرانیان خارج از کشور و شیعیان جهان میلیون‌ها دلار در زمان جنگ برای بخش سلامت کمک کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680229" target="_blank">📅 10:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی: افزایش قیمت بنزین منتفی است/ حذف کارت‌های سوخت آزاد جایگاه‌داران
سخنگوی کمیسیون انرژی مجلس:
🔹
حذف کارت‌های سوخت آزاد جایگاه‌داران به صورت پایلوت در استان کرمان آغاز خواهد شد.
🔹
براین اساس، سهمیه کارت‌های آزاد به سهمیه کارت‌های سوخت شخصی افراد منتقل می‌شود تا ضمن جلوگیری از قاچاق؛ توزیع سوخت به شکل عادلانه‌تری صورت گیرد.
🔹
برای مصرف‌کنندگانی که نیازمند سوخت بیشتری هستند نیز تمهیدات ویژه‌ای در نظر گرفته شده که به‌زودی توسط دولت اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680228" target="_blank">📅 10:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz_8dSbcvQSHoFO6B1F1FxVd987BT2CZ-qNCkuLMb4HpLSmdiDwv3VqDMSv2r43qDGMTLP_v0k13NYdE2aZlQCRWmP3dNujenJdpFaYqD4uAVPNyR8rMrzaW9iR8CjGO44N58vS6ei3YzqCKiG-l4A5fuLEXScF11zcu_Mqp0dwN4OVT3a6snZF-0T4O2zHQXmGvIVz1vyeN0OD_eGxG-yYFyADsHsiIVXCVAqpMYSU0sdjAlZWrF5BpSdLBQkGLYaUH5hz4n_8TfsvpK23SwbpziWUAiydSxQnVmN1CCXeADFr1aOalevOZWCRQI-OEX4j7LRDY7HJdfTBx1t-8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/akhbarefori/680227" target="_blank">📅 10:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d142c98d.mp4?token=leEU2ccJAlPbaqZJqXtMgkoBERyOPj4yWs7GPHfDLkGJRLYe3fGM5ju2WmFmWdwEnP6txqtg19l0gCUsNbHoYCutX4-xJAHHRQP8eWW3-7SEWnM3UiEZeGBrvEnGnLCVv6z_2diD4Kmzxtjv3JpW1Pj8Yyk1SLKDB4-cajgSHc02eP25REUFxi9629wDA69HF2a2Z1G3dTvSSmtRLTGCSTNzU-A8LnX8v_kFvnItspI7e85iq-hZZJrqmVKShcLBERBcEHKl8rOtxx65LdB-O_gqPSzE9jx8eQGxJznkJcXcLGM0XJUt2Ap-OSdWM9oJTNWw2mx9WJQK7aPNYhZ_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d142c98d.mp4?token=leEU2ccJAlPbaqZJqXtMgkoBERyOPj4yWs7GPHfDLkGJRLYe3fGM5ju2WmFmWdwEnP6txqtg19l0gCUsNbHoYCutX4-xJAHHRQP8eWW3-7SEWnM3UiEZeGBrvEnGnLCVv6z_2diD4Kmzxtjv3JpW1Pj8Yyk1SLKDB4-cajgSHc02eP25REUFxi9629wDA69HF2a2Z1G3dTvSSmtRLTGCSTNzU-A8LnX8v_kFvnItspI7e85iq-hZZJrqmVKShcLBERBcEHKl8rOtxx65LdB-O_gqPSzE9jx8eQGxJznkJcXcLGM0XJUt2Ap-OSdWM9oJTNWw2mx9WJQK7aPNYhZ_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایرانیان خارج از کشور و شیعیان جهان میلیون‌ها دلار در زمان جنگ برای بخش سلامت کمک کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/680226" target="_blank">📅 10:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد
سردبیر وال استریت ژورنال:
🔹
گزینه نظامی در برابر ایران «غیرممکن» است. هیچ‌گونه فشار اقتصادی علیه ایران جواب نخواهد داد.
🔹
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد و آمریکا نیز تا حد زیادی موشک‌های خود را از دست داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/680225" target="_blank">📅 10:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پیکر شهید «بهروز مصلحیان» پس از ۳۸ سال با آزمایش DNA شناسایی شد
سپاه فجر فارس:
🔹
پیکر شهید «بهروز مصلحیان» از شهدای لشکر ۱۹ فجر پس از ۳۸ سال شناسایی شد. پیکر این شهید والامقام با انجام آزمایش DNA و نمونه‌گیری از مادر و خواهران وی شناسایی و تفحص شده است.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680224" target="_blank">📅 10:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک چین در هوا منفجر شد
🔹
جدیدترین موشک چین کمتر از ۹۰ ثانیه پس از پرتاب منفجر شد. آژانس فضایی چین هنوز بیانیه‌ای در مورد این حادثه منتشر نکرده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680223" target="_blank">📅 10:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680221">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzKk6_JSUs8A0RuKTbNzF-oZWkDApyoQPwjMXCeCBeaOn9OU8t8o0bsQFknuWTDErDJeBofU3bfpGjsUHErLaQSeFfoSRQvhqDhjqmqD1OHGk_gUvyE5lzgG8e4RKmi5ThlyFF7wM-DTdIWgER8emfNNVFiNw8E_K5ExEHsDnzl2QHpF6MahRh_Jf037-V-g0-XVN2Faeik4s0mN1guF0uA5QAb_TAfV7IIS5m5X6S35J2BeBbrnh0V_ZNRJx3po5-0ckpZGe94vwPRGeK7M8KZfjFeP9OKufGq-GTslC1B73QhC3NeKtsgh4fMWxx9GNN6WKrVUzEqzDzx9Dcav0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcIiUoiUHGYkM5Rc9Cysz-GCxNPhxPs8kemsp_fgx13HXCiTcfp1MiB3t8LbDbO-aYv1Ap-bqg_WRAYuerwytl9j6Z3XyYH8ikvydjFtKsGxnXo20A_REi-oA9IRCcTfn0vhed-XY_OGtwjC7QyadmtGTYFBve6SA8Y5WBVzOVNqAyzVeEeBCDf_J1mhpX1nq1wBVRiFuahKGcxd41hmjN2ck_CrQNGLuGlKklG1WmamtUKH4fI2FeDz7OcA6B_gzmTV3yhPtBXr555k7qfxThAViYh-DfR6R9qd3AAEqE4lYRO-U7Xw8jNfa5kMAj10_PT1JlkE8FwE0TIQAFbCKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیدا شدن پهپاد ناشناس در سواحل شمالی ترکیه
🔹
رسانه‌های ترکیه اعلام کردند که یک پهپاد ناشناس، در دریای سیاه در ساحل استان دوزجه پیدا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/680221" target="_blank">📅 10:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطر و طعم این ته‌چین، مزه‌‌ غذاهای خونه‌ مامان‌بزرگ‌هامون رو می‌ده
😍
مواد لازم:
🔹
یک استکان زعفران دم‌کرده
🔹
دو استکان ماست
🔹
دوقاشق چای‌خوری ادویه ته‌چین
🔹
یک استکان روغن
🔹
سه عدد زرده تخم‌مرغ
🔹
فیله مرغ آب پز
🔹
پلوی آب‌کش #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680218" target="_blank">📅 10:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYTI5jy5MIwgpojxxgYb2PXSwJLcq4Fm8GaT9OF78nPSa1ULCb4dBwpb5zO0G5Ednydw1ndHPBNAM942aaFaGl5rpboBzf0jWh2rcvp6VY2_hdfNOc6R7r2ykVKFtJFLYQAYX5VQ45FcgMPSTVQFAlacLSVMysViIoBbWkg5Q65Uaa9092Uq4nL_dhrvhxym7hkBdAjnRphul9bPqOmy5MTfUI20C4kaEVCEFQ0PWIZecY7GnDGyTu4yIKNEhWGfVADcXQiPrmOc_hKkzzaGl4ERvOBkqwnmoEfXI6M5yL__zCInvd8Ap7zXTz0Dvrpxzhm5pG9PqD6Ks6DXEq16BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه دریایی در باب المندب
🔹
شبکه الجمهوریه یمن و برخی منابع عربی از هدف قرار گرفتن یک کشتی عربستان سعودی در نزدیکی باب‌المندب و وارد شدن خسارت به این کشتی و تلفات به سرنشینان آن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680217" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmJbRLl0zz_SwMGgHacz7X0xiB7uL6mzkw3qvCFarQeQVqocc2jQmz374AV1ceNTg_FOSeA-ffAt62hsxtc48MriXJTR4qhiYP71Q_EZuZWxDqYCDxQBlXGADE_1AkOHPBBneWqO1dAMKYloqLCHokeHuDZWmzmCN8mhVaIKgAKonuRp2LzkchjMkOWEagjm_40whNVooQzt1cGchi5s59XOQVkqImat1UdS8-QZMh2gBJ7T_YW_xUsM6b8PIn4EW3CTOCGLsI1ew2a-543samHJIKbHkaF--7Jj9KVUe_whI6b1pab1WhE8toaQ7YMmufc8MBpnupqBblhLyoAtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5JNKhDMgjDWB6DBHery7HT8U6qOM0qOG-VJe1EBYN0kHxaFdD7axd9LjaoSRjqrU7rr1LcUknfgzxwnZ2OtIv02kiZGc0wrIB4ib8FuM0XgIc5WMpkbtA2a9NTNvAGShHke2Dn8MaKp6QkAK6xy5CGQTL5omjziasJsEjhG6ScBxDmtm5NBBM8H37EY4N2AULqYvKWEFA4yBQbsN2gNJ8jxJha4R184Ep2tfR6OYaQiFbwlN6MQCM9g3ZnI7fkd1jJvmCxuNqcjjr4AsEYbwJXprH5SeanJ3bGVPAGxzvTlcKQjgqlrQTXTqJXdfJrl_JxSLEL06xNH0I4piphZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rulio6HXXmDJ1TjL4Es2DtQItObAZUzTEOmJEy69_uY8wbDMPBKdjGolX7qDa5pq4WqWqatKL_y-6ahpd9wNLqwgIg5uvffsvu27N2DrxF5ja4c4hZLC6uC_0HoPV39LLfTuu890B_-7GxLDeo5waqh9iWlr1NqQuZ48ezNcEb_FaPHfLY4pYwNAppRWIfwV4DETpycXhNkLXkDrA0sUjmB-2CWwve5v6BLqPE4kRZg86VH7yypZRTe8raihkoawWR6jI6mE4rV34Hh2ngpCbzG2wzzHbFSGw20dyG6pZ562vtwTfRhHv_G_alu75Ap6OgIzEZnpi2DRgyFrZXKagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrNZWmD1UuHkwf_O0Fd3Q9B48HUakS_6X7QXZVDZSHsvIUt4aD8VJwDuQPig4wDC-KiJ2h88hAfD3EgZDbNm5eJfOsFlj_l5kabOPMlFZfEHZZxxmpDQNUWBMqhihfnvg06FxzFpMVkZPNdUOe50qHhbS9AHiTbyfc_P0r6hn1lAWxysAVc-IajXlYo8hplfGlF17kS2HFt2iA_oTk7qhPYF0xEUon7E8QWla_QJHGAQrCjOs-rPCaQiWAe-ZIBp5CF4GyCa4xlWPLOMfpV3phRTDcDgscX5XeP4cyOCeyIEPDpAK70EjvwMYF10FSjbu_e_9RAQJ3rsiml8WaF1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6PB7QvH0m5E4D0AG8WUxy2nBn1yOEMZGZWBuRkGTjUSzH3oW8ah016ixJD7jpr2sCC110gAwFDSUptfxE5MLYLNWg2MepR5c1kOOZU_OaudJFWCFjHrZ7RAV8ySd03jeU2mj8NxVND2u5gs1xFit1zxccDUgNhxE41ANhTxTudJdzGvqnTkgNhqaopfX_6XWbNlRgnIy3mPoRYL1-0cAkd3N5JDy8PZefiJCwHNKAljXCCltiMTMXXbyRbBMbfAqCDOwtxCp6dbNTLAxBrIUZjMuy_UueFCVWtxUr9-9IBmelr9PfiXyD3rNJal5OLASGG8HEn2btjRLi71Fu_xfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBr9scHCImDJwNEqV2Q6YTjAyCWauZmT_MzYpEMxnzl8mVy5NzOB0vInWS_N2TypJu8Yuk59QxHSaFfS3DngQuTi7gSD94KmOREIjoJc1vl6wNoODvnU_xu89CbiAKr9nFxVfJ4NpJLfzyBNlUHXfYB6hzJqFOK7AOT0UCf_BPWjw283lwlym3k9kdee5RdonTVvVKKbP0QKXuKCumhg4vdAawZ4ybXFWDxl_dwYPAMD7GrxcjI0oeh7eiqppmm-qf9G4UxDdSU_Ig_edaopSJGUMGJffqArTyg1yAiQF6hplakTfzaCMi0JkfOneNt4NDpHEdxmT_Q2HjwZwB3ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJ3mCAG5BjgG8VRjDrNSqX8PmBkgp5dyQInkuHlpTTDFQ7UdUmPN-M6GMngeRaHd472--m7Kx9SZbPqNzTrmIlgInZT1bBuWELRBp1uaLPlEjCe3wvQ8lmnLjunRjWY1YN7NUYkY5avJZf-hG9btls0yQDrA1WrHyImAxtYsa11qO4AKSwfoxGLXJ-gqYMNCg5v-dQ4GgBv1q30CEHb1kL22q4-i6mN63_FrHSZ-6lCbc-nODxzAKOP9tB5Jqdvm4SZjLq6L1_Tg7LY1iAg8kPzD7g0goznPK3YYhLDvXC7nR6AHUkcYeERAuGAw6lpRfJunrXNd5LGSE4j_-Ppw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai23omX7MCVQxs3pGmkWBG2kcfPsH1_-0TKidPeKNoXC5f6faLs_Uk5joe_7CeswdNND9va9iT-8Sz6qGj4kyzQgCuTc92tt5iSn6bdqMVajjB6B8RHc62tXAvAWMi39Od2ki2lMsqoUpCejJM8qNuo71Ttc-uqkuSRyE_hC9r1fmsELd0A_VUDBYkUtRB3IgXWAKWa2nLIU9OFS8iKcVlINKbSQkX3HI0WZcSbPGJHzjaQ7v1CGlqSEryjrJHMj0dS24h4CmFG9gWU4bb0Jstw4JkIsldM-resQnFod0YRVCuQZ8Dd3wHJCDnJqu6X3dr9gvmJEqnG_ELbEesAWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhyXxgGuqt57GJZ3VRaMZkZBSQ2aSA6f9c3ecIcEcixU1ZJL2ZKNcrHdxtdrFo22LOSFc9ic66dPfuacYZ-fCy0OsdgVqVDf1VSd66colSDjSRU4ChrFhXWB0ERH5hWeZPhSUHApiXvOKOUFdbEKbUpQWTFDEuMDg59lBarYdOpkdjZZWKJht_wHQsqSNHVk1mSTF7kCK4lk0Jwcb-8BLlboQqFYNrUJRzyxVL8vo3-RiAXC5sEv5oH0YRKgd-4hZgUfqPTqNdT6Rv9ZBvhdWr11XH1_ftuMEVtRqs3lIH3pYYsvyA18fGOjII-rFAvEGdWtIl41wuiU2ZAZKFp7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4UjMhyGCgmBtuwuPa-_S1g30Pw4oEzfgb2magxKXLTS-7CFt2BmcHgP6xW4Ke6_j-TKW2Wr2PaVxwJObrcDOrpZxCJ06FsSTNBQQkvf5InAsxtHtr4TROeEM7e92DTQUth2X6ohrHMi62JckjENHo8CfzFqOROsqcj_KAZOM7Ct4072u-oxaigJGaa3ukpRU0TQtL9GjK5IfraIQUpmHPCMmEEAPL4CByAgNCtLu0hOI8LB9DTDOtc-b0IM5pEqKyXAVpBNIAy8m9RmmQ4J9sLJdzRjmsgG7N63faSZ19PPULebBOx9lF2eMS--YICsLrCgXkpp0PGn1474vZ8qVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر پیاده‌رویی زائران امام رضا(ع) به سمت مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680207" target="_blank">📅 09:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680206">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند و همزمان عوامل آتش‌نشانی نیز در محل حضور داشتند. با حضور به‌ موقع نیروهای انتظامی، گروگان آزاد و فرد گروگانگیر مهار شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680206" target="_blank">📅 09:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آخرین وضعیت ترافیکی راه‌های کشور
🔹
جاده چالوس از ساعت ۹ صبح امروز، به‌دلیل ترافیک سنگین، در مسیر شمال به جنوب از مرزن‌آباد به سمت تهران و کرج مسدود و مسیر جنوب به شمال یک‌طرفه شده است.
🔹
ترافیک در محور چالوس، محدوده‌های پل زنگوله تا هریجان و هزارچم سنگین گزارش شده است.
🔹
در آزادراه تهران–شمال، محدوده سنگان، تونل‌های ۱۶ تا ۱۸ و انتهای تونل البرز ترافیک سنگین است.
🔹
آزادراه قزوین–کرج در محدوده پل فردیس تا پل کلاک و آزادراه کرج–قزوین در محدوده حصارک نیز ترافیک سنگین دارد.
🔹
در محور چالوس مه‌گرفتگی و در محور فیروزکوه بارش باران و مه‌گرفتگی گزارش شده است.
🔹
تردد در محورهای منتهی به مشهد، شامل نیشابور–مشهد، تربت‌حیدریه–مشهد و قوچان–مشهد روان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680204" target="_blank">📅 09:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: با ایرانی‌ها در مرحله مذاکره هستم؛ آن‌ها مذاکره‌کنندگانی بسیار باهوش هستند
🔹
سه استراتژی برای برخورد با ایران داریم؛ نظارت دقیق بر وضعیت این کشور، زدن ضربه‌ بسیار شدید به آن‌ها و فشار اقتصادی
🔹
به هر حال به تهران «فشار اقتصادی» وارد می‌کنیم.
🔹
ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد توانست./ انتخاب
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680203" target="_blank">📅 09:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
انصارالله: عربستان در پی تبدیل المخا به یک مرکز نظامی بود.
🔹
شبکه ۱۲ رژیم صهیونیستی: آمریکا به روند خروج هواپیماهای سوخت‌رسان از فرودگاه بن‌گوریون ادامه می‌دهد.
🔹
آلمان خواستار مذاکرات سازنده برای پایان دادن به جنگ علیه ایران شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680202" target="_blank">📅 09:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
۴ فوتی و ۳۰ مصدوم در پی واژگونی اتوبوس زائران مشهد در خراسان جنوبی
🔹
صبح امروز واژگونی یک دستگاه اتوبوس حامل زائران مشهد مقدس در منطقه قهستان خراسان جنوبی، چهار کشته و ۳۰ مصدوم برجا گذاشت.
🔹
امدادگران هلال‌احمر در حال امدادرسانی به حادثه‌دیدگان هستند.
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680201" target="_blank">📅 09:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: اگر یک پل ما را زدند، باید دو پل آن‌ها را بزنیم/ ما بسیاری از زیرساخت‌های دشمن را نابود کرده‌ایم که اطلاعات آن‌ها توسط دشمن سانسور شده است
محمدرضا رضایی کوچی، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
نیروهای رزمنده ما خیلی از زیرساخت‌ها، پل‌ها و نیروگاه‌های دشمن را مورد هدف قرار دادند؛ منتهی اخبار بیرون نمی‌آید.
🔹
نزدیک به ۵۰ هواپیمای ما آسیب دید که حدود هشت مورد آن‌ها عملیاتی و فعال بودند، مابقی از رده خارج شده بودند یا در تعمیرات بودند.
🔹
در بحث خسارات جنگ آمارها متفاوت است؛ وزارت اقتصاد، وزارت راه و بانک‌ها هر کدام یک آمار می دهند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680199" target="_blank">📅 09:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادغام ستادکل و قرارگاه خاتم؛ آغاز یک ساختار جدید نظامی در کشور
🔹
فرماندهی معظم کل قوا طی حکمی ضمن انتصاب سرلشکر پاسدار خلبان علی عبدالهی به عنوان رئیس ستادکل نیروهای مسلح، بر ضرورت تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیاء(ص) تاکید کردند؛ ادغامی که براساس تدبیر امام شهید از سال گذشته آغاز شده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680198" target="_blank">📅 08:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر حرکت زائران پیاده امام رضا(ع) به سمت مشهد
🔹
موکب هیئت قرار به همت همکاران هلدینگ رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/680196" target="_blank">📅 08:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
انتقام عجیب عروس از مادرشوهر: ۳۰۰ گرم طلا را با بدلی عوض کردم!
🔹
زن میانسالی از عروسش به اتهام سرقت ۳۰۰ گرم طلا شکایت کرد.
🔹
عروس اعتراف کرد با تهیه کلید یدکی گاوصندوق، از طلاها بدل مشابه می‌ساخته و آنها را با اصل جابه‌جا می‌کرده است.
🔹
او گفت به دلیل اختلاف با خانواده همسرش، طلاهای اصل را می‌فروخته تا از آنها انتقام بگیرد. تحقیقات درباره این سرقت‌های سریالی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/680195" target="_blank">📅 08:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وال استریت ژورنال: ۴۲ هواپیمای آمریکایی در حملات ایران منهدم شدند یا آسیب دیدند.
🔹
بلومبرگ: کمبود موشک‌ فشار بر اوکراین را افزایش خواهد داد.
🔹
پلیس راه البرز: ترافیک سنگین در آزادراه تهران - شمال؛ یک طرفه شدن مسیر از ساعت ۹
🔹
فرماندار بوشهر از خنثی‌سازی مهمات عمل‌نکرده دشمن در بوشهر
خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680194" target="_blank">📅 08:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگر از فروریختن ساختمان‌ها در کلمبیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680184" target="_blank">📅 08:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین‌هایی برای فرم‌دهی به پایین‌تنه و میان‌تنه
🔹
اگر به‌ دنبال تمرین‌هایی برای تقویت عضلات پا، زیربغل، کمر و شکم هستید، این حرکات را امتحان کنید. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/680183" target="_blank">📅 08:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL8ni_JZlQF6lFgD4S5LWJbUHxuzF5JuJ08FTVT7aCWwyY-zr4-ZZauAe0lodIzzT7pBvQTIsikqEQe6FCZywoXppWIgeaC25rHBCS-Xg7lhR7dxOzzh838Qogg_hILO5LGFkMUaDCICIACjuiWhlmlY7iOrjHEkG79hCx4ly6SFMrDx6IeY5Y-TalAjhWL1u8W2x5OlJiXGNFGjstTLT_-4hEfKQTrPgFF4ch71sChLbvDh0MKw0im4Nq8zkFJBPC0x-L7peCJmw124VDIPpGS-QZ4usxeIk6pCyyypfgaCBlk-bR_vFOGMutkTV85RMg_JDzIKopE_2LBh3D34Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ در ترکیه از ترس ایران با کامیون پذیرایی جا به جا شد
واشنگتن‌پست:
🔹
دونالد ترامپ، پس از حضور در اجلاس ماه گذشته ناتو در آنکارا از ترس تهدید ایران، به صورت مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه خارج شد.
🔹
طبق گزارش واشنگتن پست، ترامپ پس از سوار شدن به جت قدیمی ایر فورس وان، دقایقی بعد مخفیانه به یک هواپیمای کوچک‌تر C-32A نیروی هوایی منتقل شد.
🔹
او از طریق یک کامیون پذیرایی فرودگاهی که معمولاً برای بارگیری غذا و سایر تدارکات استفاده می‌شود به آن هواپیما رسید./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/680180" target="_blank">📅 07:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نما در نمایشگاه AWE ۲٠۲۶ شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680179" target="_blank">📅 07:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBmcSU1jo1r3Ae4OCKXJjJzij9adMrr_kUDiB_m_WmRHN2Jh1in0RMzFpmWXg40DnFc1gF8pzcBesZpTz-K34pIYWoTvMZ74_pQdt5g-TYz6xbofcmUxM3Rzf2KBy2I5SsBfTz6D7ZJ6N5sCfgeksspjeOfpHzLbzh0F_OIWij5A-uDtwv-1bK3D8sHXOoTcTcnlSaJUYlBRjall_dS6rCOvuvWYylpHWmOYz5q59qWzGlZoVfDd7Nb_PmBAgVNi4CwlbeqN8b4EfIU1IbUtbYC231K5vvBCkP1bcJuct5w8EyhfRm5FJnlwd8D2Jg7MSUM2laNuIuUOfAvvbTKDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۰ مرداد ماه
۲۷ صفر ‌۱۴۴۸
۱۱ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/680176" target="_blank">📅 07:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680174">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ovyiuw6WSdVYSR4cJLhnDKdqupaSIzWceds1V629nxYDsnUfbfdKHp41EHK-QQZhuJqmnVf6v_RZlLbqhRDBz-FWRJJGaulGRbIcqsMu9BLYXJqBm5oGnD0Hb3LcZCmYssKtVUvJMpQ7ERePpS7tSIH_CHyAJePDW7IN8scbsgiPCeV8R7tn6_YKH9xT3xCnwU_jopbytYuhya-7dTLnmWbB4-lY2E_ovRuQ2vMoX4vo-Q8x8toUZa5c2AAwD9lBMOV7Xg3IG3nCthCwYIsBPgtXimlMW1KkbEMZzgxahb0ybSGGbI-UOhM_CQy04JCqz8zLzB2muL8rCm4KpzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسوایی اخلاقی رئیس فیفا فاش شد
🔹
طبق گزارش یک نشریه انگلیسی، او در دوران حضورش در یوفا به مدت ۵ سال با یک زن رابطهٔ غیراخلاقی داشته و از سمت خود سوءاستفاده کرده است.
🔹
پیشتر نیز پروندهٔ اخراج او به دلیل زدوبند با ترامپ مطرح شده بود. حالا این افشاگری در ۳…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/680174" target="_blank">📅 06:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-c-j93cFqWYo_mAqzHBNc5DVYarzh9yy1rJ2jAdFBWpaSnbbACtynJtYickGUGTh8yD1NlWELeOB7xhoxbFn1_WV_sFHna4nH-ZGKuczHgUuyRLlU3nDK3MdhkdtPuiSDomDEgx4dUlsSsZt2d5gRYTOJrt0YVkNKLkZUvSEyRazrWTN4CZrQ14rzSr0AsiY7APAPgSyCNXRaCjawTY26sgb3aoDeS9T7qyeHTuxCol4vEWgJ1F6TsAIDQQ4aIaBQHp58eMjFtEhZekmJrwHjrO5qNIPVYlv7bcWZTi7VzN1jgSHgD4dSlHv3bRkovIS1Q659e9yGMFjyssH478RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/680172" target="_blank">📅 03:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین
🔹
منابع خبری از وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/680167" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R26vwlxhNlWw1vSVsKzKl5pFSM_0RkbmXUcZdgqZAw1Wrl6DrzQORSxFOKV5jmPnHWmz-isj-q63zztNqURNm5j2VgsnyUq5m-esk92vXjaG9JUwntaVr6f1pVBIv5I4auns19vwimpxT0Tz_9CBuRZ0b4L_1BXmNo5bgW3VPq1g6qteYmkrBiJCcufmR1xs6XiXJZk4vO0cTh-1gja-OdLgqdd5wy4xzK9e9kEREeIUbfXDKMBwvuWLm12UaLWiBuvw9f8Ts2vjBlX5ceQckhs2g0nPD78NqjpjCNXd371vQfjgaBDEp1spS0GJtCOMOKARwM6XjCkj_uapC01mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔹
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/680164" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrQlz-V4HlXPEXhhGKjoR1YEE6AqOsNvJrTqrITZSy6RzbGFV3k_PtqTXoB3O4THpXm1Kd2uHRzxMngxYoLFkf-YUi_tImjBpyHCr2DG__6eeGmDHEr3OLJv6fwdeAoLveYLH6qSN76FriJSeMW8tx7YACBAp_UkDuWb1_FUF_Lh-olwxSuAgP1xDcuAVOcG0hCIONFczd3lOdfUa03Fb-9tu463PRffhZMjRCeaaFwhR94F-JpnQDgKl0akY9wXXhs1l7jQc73ndiKISKvOoVuiMoABvb6scGx-5O40BReaOFroBtWR4Ep4Sy25GKwr87FgMH54TTfXTWsXwBUD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرایش جدید فرماندهی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند. بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.
همچنین سردار سرتیپ پاسدار احمد وحیدی با اعطای درجه سرلشکری عهده‌دار فرماندهی کل سپاه پاسداران انقلاب اسلامی شد و سردار سرلشکر پاسدار مصطفی ایزدی مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفت. در ادامه این احکام، مسئولیت فرماندهی نیروی دریایی سپاه به سردار دریادار پاسدار علی عظمایی و ریاست سازمان بسیج مستضعفین به حجت‌الاسلام والمسلمین حسین طائب محول شد.
🔹
هشتصدوسی‌‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/680163" target="_blank">📅 00:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان حضرت ابراهیم رو اینجوری نشنیده بودید!
برنامه متفاوت پُلاریس رو در تلویزیون اینترنتی مدار ببینید
👇
▫️
https://youtu.be/4feAD2lqlHI?si=8_SmjCmzNJ7rwuSR
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/680160" target="_blank">📅 00:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده / در تحقیقات اولیه متهمان به قتل اعتراف کردند  فراجا:
🔹
پس‌از دستگیری متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده؛ تحقیقات و پی‌جویی، توسط کارآگاهانِ پلیس آگاهی در خصوص علت و چگونگی وقوع جنایت در جریان است. همچنین…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/680159" target="_blank">📅 00:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گزافه‌گویی‌های فرستاده آمریکا به سازمان ملل علیه ایران
مایک والتز، فرستادهٔ آمریکا به سازمان ملل، در مصاحبه‌ای با شبکهٔ فاکس نیوز:
🔹
وقتی ایران پای میز مذاکره با مذاکره‌کنندگان ما می‌آید، صحبت از پول، پول، پول است. زیرا آنها بمباران‌ها را تحمل می‌کنند.
🔹
آنها به دنبال دسترسی به پول نقد و دارایی‌هایشان هستند که ما مسدود کرده‌ایم؛ این همان نقطهٔ فشار است.
🔹
این فشار همراه با محاصره، چیزی است که در نهایت باعث می‌شود ایران عقب‌نشینی کند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/680157" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بذرها روی خط؛ گامی تازه برای کاشت منظم‌تر و بهره‌ورتر
🔹
در این روش، بذرها با فاصله‌ای مشخص روی نوارهای زیست‌تجزیه‌پذیر قرار می‌گیرند و سپس نوار در خاک کاشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/680154" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680153">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGkQRrsN4R0Lq5DyARi1-22eyFHtI762BacF7jCjeYmzILkxiFhfChWilCspQvQow3dZ3cD1a2OOcwO407yC3A09zhMORjn0Egz31vNoPlg5xc6nYyo1pTDhe_7anjAcxbzY9qq61gc_ow_-E9xddZi341eDLOtM84w6QhSvKUpFH3EqwIu5y8q4PoEdOziA07H7XpGahxYi3C3o9xx6lGfm4UNg0fUaCrUFLK4pwdcSMMay8nQdlaPwtRGAeZ0rTaC9ZJLNkefn4KlWj4CgTyw3pJ8vmYyoTT2cpD9P4SSCQRCqzlovNc-yf3fm4GnRTROaF-cthGA_B2mTqNvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/680153" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680150">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سقوط صادرات فرش ایران از ۵۰۰ میلیون دلار به ۳۵ میلیون دلار
سپهرزاد، رئیس کمیسیون فرش دستباف کشور در اتاق اصناف ایران در
#گفتگو
با خبرفوری:
🔹
طبق آمار گمرک در سال ۱۴۰۴ میزان صادرات فرش دستباف معادل ۳۵ میلیون دلار بود، در حالی که در دهه ۷۰ و ۸۰ این رقم برابر با ۵۰۰ میلیون دلار در سال بود و تنها یکی از تجار ما در سال ۳۵ میلیون دلار صادر می‌کرد.
🔹
در سال ۲۰۰۰ سهم ایران در صادرات فرش در جهان به ۳۲ درصد و سهم هند به ۱۴ درصد می‌رسید و در سال ۲۰۱۹ این آمار برای ایران به ۸.۶ درصد و سهم هند به ۳۵ درصد رسید و در سال ۲۰۲۶ اصلا در این جدول نیستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/680150" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاست ترامپ دیوانه: هر جا خوابت آمد؛ بخواب| وقتی رئیس‌جمهور آمریکا یک چرت مبسوط می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/680148" target="_blank">📅 23:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
معاملات ۵۵ میلیارد دلاری ایرانی‌ها در پلتفرم‌های رمزارز خارجی
🔹
داده‌های سال ۱۴۰۳ نشان می‌دهد حجم معاملات کاربران ایرانی در پلتفرم‌های رمزارزی خارجی به حدود ۴۰.۵ تا ۵۵.۵ میلیارد دلار رسیده است.
🔹
به گزارش TechRasa Insight حجم معاملات در پلتفرم‌های داخلی بین ۲۷ تا ۳۷ میلیارد دلار برآورد می‌شود. دسترسی گسترده‌تر صرافی‌های خارجی به معاملات آتی، اهرم‌های معاملاتی و ابزارهای حرفه‌ای ترید از مهم‌ترین عوامل جذب معامله‌گران ایرانی به این پلتفرم‌هاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680143" target="_blank">📅 23:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۵۶۸ هزار نفر در صف وام ازدواج هستند
علیرضا نثاری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مبلغ مصوب تسهیلات قرض‌الحسنه ازدواج ۳۵۰ میلیون تومان با کارمزد ۴ تا ۵ درصد است و حدود ۵۶۸ هزار نفر در صف انتظار دریافت این تسهیلات هستند و تنها حدود ۱۲ درصد از تسهیلات مصوب در چهار ماه اول سال پرداخت شده است.
🔹
بانک‌ها موظفند قسمتی از منابع داخلی خود را بابت پرداخت این تسهیلات به انجام رسانند و بانک مرکزی باید سهمیه‌های بانک‌های عامل را مشخص و تا پرداخت این تسهیلات به متقاضیان نظارت لازم را داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/680142" target="_blank">📅 23:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680141">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: آیا پاسخی به نتانیاهو دارید؟
ترامپ:
🔹
من امروز در شبکه "تروث سوشال" (Truth Social) پاسخی را منتشر کردم. پاسخی خوب دارم. رابطه ما بسیار خوب است، بله
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/680141" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی اساس ترامپ دروغگو درباره ایران: آنها می‌توانند مشکلات ایجاد کنند، اما ورشکسته هستند، آنها پولی ندارند
🔹
ایران کاملاً ورشکسته است. آنها به سربازان خود حقوق نمی‌دهند.
🔹
نرخ تورم آنها ۳۰۹ درصد است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/680140" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680139">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک ترامپ جنایتکار درباره ایران: ایرانی ها صدها هزار نفر را به قتل رسانده‌اند
🔹
اکنون آن‌ها در حال پرداخت بهای این اعمال خود هستند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/680139" target="_blank">📅 23:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: تنگه هرمز چه زمانی باز خواهد شد؟
ترامپ دیوانه:
🔹
الان باز است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/680138" target="_blank">📅 23:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را پاکسازی مین کرده‌ایم، شاید شما این را نشنیده باشید
🔹
ما کنترل ۱۰۰ درصدی این تنگه را در اختیار داریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/680137" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: گاهی اوقات دوست دارم من هم سنا را از بین ببرم، اما این را نمی‌گویم، من این کار را انجام نمی‌دهم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/680136" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما شاهد انتخاب افرادی هستیم که دیدگاه‌های جهادی دارند، تقریباً در همه جا، ما با کمونیسم و جهادگرایی روبرو هستیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/680135" target="_blank">📅 23:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دروغگو: رئیس‌جمهور بعدی، اعتبار زیادی را به خاطر کارهایی که من انجام داده‌ام، کسب خواهد کرد
🔹
لطفاً به یاد داشته باشید که این کارها را من انجام داده‌ام، نه آن‌ها
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/680134" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ شیاد: هیچ اتفاق بدی از کارهایی که ما انجام می‌دهیم، نخواهد افتاد، هیچ اتفاق بدی رخ نخواهد داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/680133" target="_blank">📅 23:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: برخی از گروه‌ها تقریباً هیچ مشکلی با اوتیسم ندارند
🔹
این گروه‌ها، افرادی هستند که به شدت به دنیای واکسن‌ها علاقه‌مندند.
🔹
هر سال، میزان ابتلا به اوتیسم افزایش می‌یابد، و این افزایش روز به روز بیشتر می‌شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/680132" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ده‌ها سال پیش، کودکان تنها بخش کوچکی از واکسن‌هایی را دریافت می‌کردند که امروزه مورد نیاز است
🔹
در آن زمان‌ها، مردم بسیار سالم‌تر بودند و البته، میزان بالای اختلال اوتیسمی که امروزه مشاهده می‌شود، وجود نداشت.
🔹
دلیلی برای این میزان بالای شیوع اختلال اوتیسم وجود دارد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/680131" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: واکسیناسیون برای بیماری‌هایی مانند هپاتیت B، کووید-19 و آنفولانزا، و سایر بیماری‌ها، دیگر برای همه کودکان توصیه نمی‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/680130" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه اتفاقی خواهد افتاد؟
ترامپ:
🔹
شما متوجه خواهید شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/680129" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2443a36c99.mp4?token=j2zKSPL2XXcFKbJuxZwoWnJ4F5gGn3tHUlRr7d35xMtFPirg5d9LYuJ5fqI4FcN_84TWqXn3J1kdj1MXMarMHalUpWRiqj8Cx8NuMp-SnhxZ6PektZ9izFKYp6AHCaornBEtRphKOY04yiAKgFoSZsgggrxAHd2g_srJ3-KW7uwRIzXvkJLSA33B_mD5C81NPMFnY_ixTDLUCl_QrKrO71z0ADFd8eGRO-xBJJ9nlT9N5JUKFa_prD3r6nKYjZXblpvXsVNhQTKO_nYFIJVYJ7cIbUes_RniEZ-QJ1fvmR8VB53aWl0aky5kkRAv7SfNwA-OC9Jp3pDM0uGM-LphCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2443a36c99.mp4?token=j2zKSPL2XXcFKbJuxZwoWnJ4F5gGn3tHUlRr7d35xMtFPirg5d9LYuJ5fqI4FcN_84TWqXn3J1kdj1MXMarMHalUpWRiqj8Cx8NuMp-SnhxZ6PektZ9izFKYp6AHCaornBEtRphKOY04yiAKgFoSZsgggrxAHd2g_srJ3-KW7uwRIzXvkJLSA33B_mD5C81NPMFnY_ixTDLUCl_QrKrO71z0ADFd8eGRO-xBJJ9nlT9N5JUKFa_prD3r6nKYjZXblpvXsVNhQTKO_nYFIJVYJ7cIbUes_RniEZ-QJ1fvmR8VB53aWl0aky5kkRAv7SfNwA-OC9Jp3pDM0uGM-LphCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ درباره ایران: اگر خساراتی باید پرداخت شود، به نظر من ایران باید آن خسارات را بپردازد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/680128" target="_blank">📅 23:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3TFgYaeUaNaX4JCXNIFTAtx1k5Rc-DOWuSBIs37iXHEFU9QoEw7B9phi0Vy0SRKJMM0guOiEv2eJr35QfokP4L4RFcIHHbQEnb79lQC4n7CofRfVGdSuEuqixWX2k-ycBwPqNyM3xXKCamPDe83CFblO0HH_1nKkYF8bRtCK0ZiRedXg0T1YlVJ5IfhX70C1WMoV5AwnMj0WXkHBBkkhRrNe3BoAgLKcKQ0MMaN87VkkKhi_mc96kScp8uyIL0GSVu6v7qrOVwzEQLdHxG_P_xLH4Ay-U06IOSEL6ovV0wAk4VMZZr7KtwRmxBvQAoI3K3u--oz3lxVM2HrjH8QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه ایران: وزیر خزانه‌داری آمریکا به «خفه کردن» ایران از طریق تحریم‌های اقتصادی افتخار کرده است
🔹
این ادعا، فراتر از تأثربرانگیزی محض، گواه روشنی بر اعتیاد اجباری آمریکا به تحریم‌هاست. هرگاه واشنگتن ناتوانی خود را در پیگیری دیپلماسی نشان می‌دهد، به تحریم‌ها پناه می‌برد و هرگاه این تحریم‌ها نتیجه نمی‌دهند، صرفاً دوز آن را افزایش می‌دهد.
🔹
این دیگر «سیاست» نیست، «عادت» است؛ و خطرناک‌تر اینکه، اعتیادی است که جای تفکر را گرفته است. ایران طی دهه‌ها نشان داده که با این لفاظی‌های فرسوده خفه نخواهد شد. خطر واقعی این است که سیاستمداران آمریکایی، با چسبیدن به این عادت بد، آخرین شانس‌های باقی‌مانده خود را برای خروجی کم‌آبروتر از بحرانی که خود ساخته‌اند، از بین ببرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/680127" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن رئیس جمهور متوهم آمریکا تمامی ندارد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/680125" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل درست کردن یک شات قهوه به صورت متفاوت و جالب
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/680122" target="_blank">📅 22:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان؛ رئیس ستاد مرکزی اربعین: هنوز شرایط حضور زائرین در عراق با خودرو شخصی فراهم نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/680120" target="_blank">📅 22:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۴ تنی با ماه؛ فالکون ۹ چه بر سر سطح ماه آورد؟
🔹
ماه حالا یک زخم تازه دارد؛ بقایای موشک فالکون ۹ اسپیس‌ایکس با سرعتی سرسام‌آور به سطح آن برخورد کرد.
🔹
این برخورد که چند روز قبل رخ داد؛ اکنون نخستین تصاویر از دهانه ایجادشده، توجه دانشمندان را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/680119" target="_blank">📅 22:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFd9HswKgN4A9ZK7N8JeVGkXboOF6ptG8ddNIQ_u8gGxrI-JwrsC5gsIueVpvDitkW1Pas0fu_IzrZi7wQ77bDW5ev5gzIyL6Uox889igIf9gHoR33SnEByi8Z2eh6M7YU4gGGXPOmq28wtF4UIVYXBhjCYT0jiX8ItWmQnvScQ77Y_hLgNx6k-jlAcCedBh3KSj28goNcWTNTwrFq_Mc9IXEc8gmrhJXCucWEKfSjtprNukuzjZ0V8zsq61tgi2f1q893maw7kq0uv5LdXW3aQXu-j51Twsg4d2icUAavFgZRxBo6X7N7D0pcez52Su2_zWYMWkwRUYGJLRDsepSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قواعد دیده‌شدن محتوا در سرچ گوگل تغییر می‌کند
🔹
گوگل در حال تغییر شیوه ارزیابی محتوا در جست‌وجو است، تغییری که با گسترش پاسخ‌های هوش مصنوعی می‌تواند قواعد سئو را دگرگون کند.
🔹
بر اساس گزارش Search Engine Journal، گوگل برای سنجش حضور آنلاین برندها و محتوا از سیگنال‌های بیشتری استفاده می‌کند.
🔹
به این ترتیب، موفقیت محتوا دیگر فقط به تعداد کلیک‌ها وابسته نیست و میزان دیده‌شدن، اعتبار و حضور یک برند در پاسخ‌های هوش مصنوعی نیز اهمیت بیشتری پیدا می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/680118" target="_blank">📅 22:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
موانع واردات بیشتر شد؛ انتخاب مردم کمتر
🔹
واردات خودرو که قرار بود به تعادل بازار کمک کند، حالا خودش به یکی از گره‌های اصلی این بازار تبدیل شده است. جزئیات موانع تازه واردات خودرو را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/680116" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd1qbGTZiDL7SVGPZg46lrMVQ-ey1-1xzRdhiVODCRKg-Sse3tD8A_yaUsiE7WEWHlwvd4ufggmrFluEK1vhUSevgVos6x1nOFb_hYswT33pD6FoirJRHjxbncIuitwcTKNo567eJWyd1aJweQEiWOykTozyFtUtvIyj5EvdtpQSQfeSd2DrF6GXfkSxa8PYDueZ3g4K_OA4tIt4AGCoA4w4SeivVkfQnhT36_GSGwgPnV7rFvetcOYqACrLpGONmGgZvAt6vP0sU-VSfjuY4cdHl2qWMy73CSSYWdCkT-zEwxTUc6QN0693R4k2Cb3lEFcc9snhYLPrdSVBXz4UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خردمند، پیش از سخن گفتن می‌اندیشد
🔹
امام علی(ع) در حکمت ۴۰ نهج‌البلاغه یادآوری می‌کند که سخنِ سنجیده نشانه عقل و پختگی است. انسان خردمند ابتدا حرفش را در ذهن و دل می‌سنجد و بعد بر زبان می‌آورد؛ اما سخن عجولانه گاهی در چند ثانیه چیزی را خراب می‌کند که ساختنش…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/680113" target="_blank">📅 22:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob30-pJvwmZqRcbNWnccrl1tHvhMlliN6JHH8IgfcLa9x32iQ8MktvimSDqidflEkShVdTW_pok1hOzsMd3w3fhhAH9RYfqE0e3OnH_R60H4iiCsok9QkMuqx5Iz_bvISaDtQbRWN8CFasP15A5TxQSPYj5xfzPI987cD2uC35TYGw-D1ievNwmmmQEpBf75qYLDYZfYX7LEUhbUajmVyZ8YAOob7XNWbnzGKWnW-hzx_mdE0Sv5oEYAF45S7I2IbBGNhy_9lDvJXlgVBksmiCfBTJBBxq6S2ktq-epZ9Y5I2-otUd3sf47q129hYzayrud_7brpQxdO4ShOGtW8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های مفید که برای استخوان‌ها خیلی مفید هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/680112" target="_blank">📅 22:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: حدود ۸۰ درصد واردات کالاها به کشور از جنوب انجام می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
درحال حاضر حدود ۶۰ تن کالای اساسی نیاز داریم.
🔹
فردای روز تشییع رهبر شهید در مشهد، راه‌آهن تهران به مشهد مورد هدف قرار گرفت که کمتر از ۱۳ ساعت دوباره شبکه ریلی را به مسیر آوردند.
🔹
با فرض اینکه در جنوب محاصره دریایی شدیم و نتوانستیم کالایی جابه جا کنیم، به راحتی از شمال و کشورهای حاشیه کریدورهای زیادی داریم.
🔹
کریدورها نیاز به ساماندهی دارند و میزان فعال بودن آنها کم است مثلا با پاکستان خیلی محدود می‌توانیم کالا ردوبدل کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/680111" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2xLDNbyX_9cVouc_H9yxkx5Rv4qdSswXSYXFJ9N-GI_oNGSBViAHnZQP6Up-o_tCiPnlMWO9oQE9QeBQ1aYSu0DKsQI95NwHLBtAm5u0qofu1jDW4o9vt4_Q_mArISf5gmHRnysu2NSk9AbH9pZSfem_gShX9VhkFm4OVAQ-PmC6hZkB1y5kxpvtEqYO3fl6i-3cFtqLjomSblYVHWyE0q20ZeveOVBg-NI2qIzmtGZ3DdbM2Y48su2nMyiuOnjPvKTw8mlUl8W-U3kbQSGGCoSlv-ddiCdpEF-NJ83T3YCvolw-XuiqRcZLwjMU--PTpu-yrxAT7UVqTeeTNrtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
خبر فوری برای مالباختگان گوشی در سراسر کشور
🚨
اگر در ۳۰ روز گذشته گوشی شما در ایران یا عراق گم شده یا به سرقت رفته است، همین حالا از طریق لینک زیر سریال (IMEI) آن را در سامانه همیاب۲۴ ثبت کنید
تا فرآیند ردیابی و اطلاع‌رسانی کشوری برای گوشی شما فعال شود.
📲
ثبت سریال و فعال‌سازی ردیابی:
https://hamyab24.ir/l/nzw
https://hamyab24.ir/l/nzw
⚠️
توجه: اگر گوشی شما در همیاب۲۴ ثبت نشود، فرآیند ردیابی و اطلاع‌رسانی کشوری برای آن انجام نخواهد شد.</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/680110" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میگ-۲۹ اوکراین سقوط کرد
🔹
یک فروند جنگنده میگ-۲۹ اوکراین در جریان یک مأموریت رزمی در منطقه اودسا دچار سانحه شد و سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/680106" target="_blank">📅 21:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی پزشکیان و حداد عادل با معادل فارسی پازل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/680101" target="_blank">📅 21:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ایران از اوکراین غرامت خواست
ادعای شبکه سی‌بی‌اس نیوز:
🔹
ایران از اوکراین بابت حمله مرگبار به یک کشتی ایرانی در دریای خزر درخواست غرامت کرده و ادعای کی‌یف مبنی بر تصادفی بودن این حمله را رد کرده است.
🔹
در حمله ماه گذشته، یک ملوان ایرانی جان باخت که اوکراین بعداً آن را یک اشتباه اعلام کرد. از آنجایی که مقامات ارشد اوکراین به انجام این حمله اذعان کرده‌اند، تهران انتظار دارد کی‌یف غرامت پرداخت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/680099" target="_blank">📅 21:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxwBP_f_oWe2GyoTqLv0MC88WXTiXUoYyTn-IlmPFODLO0pje2UcK4ahGD-Wnv1zVNVLvBtiSE4gxJbypZH523w8gz9CBICrleJqpdXTK72Qkgoyw9CWtuzuNN0gepfvLxeK0sv7kEzNXDcirsvyVJSsY4ZvBtF278vulzyIP7CNaIbC69MQ_luFQ7ChGAw6GCopVCSTNZNcczMtzTx0cpfAIji5lBStgi-3RKkHIGtFmo83M3tlcn9QN9i3wdHmVNvUHjYjNOMxM1CqM5UQ6BPdRY2u8ThtR0Sg6QltBodSueIqyULaCgD1K0dTU8_5DSf1pFdWxCUGJ7TtugAqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش مراقبت سلامت همگانی در کشورهای مختلف به چه صورت است؟
🔹
مراقبت‌های بهداشتی همگانی بیش از یک قرن است که به اشکال مختلف وجود دارد؛ آلمان اولین سیستم بیمه سلامت ملی جهان را در سال ۱۸۸۳ تحت نظر بیسمارک معرفی کرد.
🔹
امروزه، کشورها از طریق مدل‌های متنوعی از جمله: خدمات درمانی ملی، بیمه سلامت اجتماعی و ... به پوشش همگانی دست می‌یابند.
🔹
ایران از پوشش گسترده سلامت و شبکه مراقبت‌های اولیه برخوردار است و خدمات اولیه در شبکه بهداشت به‌صورت رایگان یا با هزینه بسیار پایین ارائه می‌شود، اما همه خدمات درمانی برای همه مردم رایگان نیستند.
@amarfact</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/680098" target="_blank">📅 21:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد هواپیما با یک خودرو در فرودگاه میلان
🔹
یک خودروی خدمات فرودگاهی حین مانور در فرودگاه «لیناته» میلان، با بخش جلویی بدنه یک هواپیما برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/680095" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی مرعشی با ریش یوسف سلامی: بهترین ریش دنیا رو داری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/680094" target="_blank">📅 21:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyD20qz43MkXAT-uVOQEWhg2te0FqavQncLyjfTD5O7hMubftQBgVzyDBFy2-8LQkOH5s-X0GtedJzkKkrexA3-oEbqjAXqTGbJg3DbVEannyDIvsUk1Ujr4PIzM152l2LGf8sKRaa-9p51XYkNcUOouS1LuplU5bbb8ghgpAOO4l5alQSn1tp5rpzKXZ9beEB524tkGGTAQ6qdTv-stCfF_iQ5thj5Oq3pdFjSaSOSvT34KgGOOdwhD5yuq3TVNTxRHDxlFP8ZcllS-i6VRSjrOTkGoMZ0CFQb1X_ljCXWVNyjBm1pqKjLn2on72AqVXL23MlFspdMZE_7o5SEs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متری شیش و نیم
🔹
کارگردان: سعید روستایی
🔹
ژانر: جنایی، اجتماعی، درام
🔹
بازیگران: پیمان معادی، نوید محمدزاده، پریناز ایزدیار، فرهاد اصلانی و…
🔹
خلاصه داستان: یک پلیس سرسخت در تعقیب یکی از بزرگ‌ترین قاچاقچیان مواد مخدر است؛ اما این پرونده خیلی زود او را وارد…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/680092" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
