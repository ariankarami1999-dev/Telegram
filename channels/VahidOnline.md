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
<img src="https://cdn1.telesco.pe/file/gNqzxE3XLgtNAsbzDHN7OAij5_nZAreHb1rDdRv0fxBR0fDsJh8G7G4o8LHPuYhlHfoOCdrMgYmucRDqyIytPHUqq4Y75AQr6A_kXL17O1R1DbjACeOqtn-Cg-UIKWYtWboiCMn1ZNzouhDVxHKp8Wpcs2oWkdLDIZifaJFcTClHTiYLxoiUiI9VPyB-xP8xafypwpdM8D_0OgPYL5Q3rbBL6bmD1_oOyGvo_WP5vXy1bLbw4PveETB15stTeCAkTRnuov20p4HpejWwh6rbEgi2KFSu4FRiuhAE8QvBEomFscv03hdVL4osD1ar9c1Cnpn_hIcUqMhQuUpU4FNwYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 22:24:13</div>
<hr>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/011b067e31.mp4?token=rlhA36jx7-5BYFHcDd_atB25hF9ErFEYn4Jxovz5zmWE08rPyApIF6hQdC9GECYnQZglNoR0_upt8gbUgrTUeTWPbQIMNs2OwXs5LiWSUC1I_TD2HOu6UTwx7MoyrK1PwsThsIay_Vq4qsLv9EOg8ZJjQpuLVKVVvXX9LvXG2eHGV3oP9z7mWcG7aCTd1xV0iOFbEOyc1fiOH7WXHuRRpYu1RsYCXQoC68Z0rzQ0L7jCesvbAmCyebCATLlXwlqrWFVexz99bP8Ou7qNLCGJnhglQbhSWuggDiT-eFu9VN57iEisMaR-Ox47X4ua6QuAZbj1Y74dU5aD7iQ3FJ8X_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/011b067e31.mp4?token=rlhA36jx7-5BYFHcDd_atB25hF9ErFEYn4Jxovz5zmWE08rPyApIF6hQdC9GECYnQZglNoR0_upt8gbUgrTUeTWPbQIMNs2OwXs5LiWSUC1I_TD2HOu6UTwx7MoyrK1PwsThsIay_Vq4qsLv9EOg8ZJjQpuLVKVVvXX9LvXG2eHGV3oP9z7mWcG7aCTd1xV0iOFbEOyc1fiOH7WXHuRRpYu1RsYCXQoC68Z0rzQ0L7jCesvbAmCyebCATLlXwlqrWFVexz99bP8Ou7qNLCGJnhglQbhSWuggDiT-eFu9VN57iEisMaR-Ox47X4ua6QuAZbj1Y74dU5aD7iQ3FJ8X_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی هم تلویحا وجود یا عاملیت داشتن مجتبی خامنه‌ای در تصمیم‌گیری‌ها رو زیر سوال برد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/VahidOnline/75600" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=Bl7gb_py6PsDkybEx7A300_gK8XAEG-fyo2DBmh9gc-pUg31xhepOClwDp6YuBvPrzdEFPZH_y60E7S6p4XlvWiKv2Mag2e6quhaJSOV21kYVIV2ujBautyEHKDgICgZvlmF2mSzaTz2WUDmBZ8BsyYn5YjrEPNdWyHOVK-Tr8BtUBaKDY5w_rYr1sVn0G-YQKpt5qeJ6oMtdUhH9YmwTRonv89g-kf_Lmsu4h5EhxWxDvQ3qhQaWlq3s59cn73vIOSa5OJ1VkFLQl4wiBc1LSZCeiR35pF35wW6WgzOcdLGshQ_Tr6DJjTZEzSDrNbl3alv120fQ20h5ihdKxTW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=Bl7gb_py6PsDkybEx7A300_gK8XAEG-fyo2DBmh9gc-pUg31xhepOClwDp6YuBvPrzdEFPZH_y60E7S6p4XlvWiKv2Mag2e6quhaJSOV21kYVIV2ujBautyEHKDgICgZvlmF2mSzaTz2WUDmBZ8BsyYn5YjrEPNdWyHOVK-Tr8BtUBaKDY5w_rYr1sVn0G-YQKpt5qeJ6oMtdUhH9YmwTRonv89g-kf_Lmsu4h5EhxWxDvQ3qhQaWlq3s59cn73vIOSa5OJ1VkFLQl4wiBc1LSZCeiR35pF35wW6WgzOcdLGshQ_Tr6DJjTZEzSDrNbl3alv120fQ20h5ihdKxTW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، در کاخ سفید گفت: «جمهوری اسلامی قرار نیست سلاح هسته‌ای داشته باشد. ما نمی‌توانیم اجازه بدهیم.»
او افزود که در صورت دستیابی جمهوری اسلامی به سلاح اتمی، «در خاورمیانه جنگ هسته‌ای به راه خواهد افتاد، و آن جنگ به اینجا خواهد رسید، آن جنگ به اروپا خواهد رفت.»
رییس‌جمهور آمریکا تاکید کرد: «ما نمی‌توانیم اجازه دهیم چنین اتفاقی بیفتد، و چنین اتفاقی هم نخواهد افتاد. قرار نیست اتفاق بیفتد.»
ترامپ درباره محاصره‌ بنادر جنوبی ایران از سوی آمریکا نیز گفت: «کنترل کامل تنگه هرمز را در دست داریم. این محاصره ۱۰۰ درصد موثر بوده است. هیچ‌کس نتوانسته عبور کند. مثل یک دیوار فولادی است.»
او افزود: «هیچ کشتی‌ای نتوانسته بدون تایید ما عبور کند. و نیروی دریایی کار فوق‌العاده‌ای انجام داده است. و هیچ کشتی بدون تایید ما به ایران نمی‌رود یا از ایران خارج نمی‌شود.»
ترامپ درباره اورانیوم غنی‌شده ایران نیز گفت: «ما اورانیوم بسیار غنی‌شده را می‌گیریم. ما به آن نیاز نداریم. احتمالا بعد از اینکه آن را بگیریم نابودش می‌کنیم، اما اجازه نخواهیم داد آن‌ها (مقامات جمهوری اسلامی) آن را داشته باشند.»
دونالد ترامپ، رییس‌جمهور آمریکا پنج‌شنبه در کاخ سفید به خبرنگاران گفت که ایالات متحده خواهان دریافت عوارض در تنگه هرمز نیست.
پیشتر مارکو روبیو، وزیر خارجه آمریکا اعلام کرد که اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/VahidOnline/75599" target="_blank">📅 20:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=HNm82wDP0EcdtEwUngZjZ40rYGD3CZ1e92shckzF3jGN8BgoLfU-Def-r8k9_bfJbOxT6AoDMSVAdeDFDITBeDC-371c7md7BLW509RXFRoosPx_pxGac2JDaohGqHd4oenipCPRBZqyer2JnZRa0YuMGAgePCjPmN-PRguFyzXovHVpM1NCD6vVIq1FspNFp06FRjcn3DrHaLZlzN3SFJ8HOYh03DHRMV0g9Xs7aNEEZQCT81THLpBHbHD6e4rLa1_cqieBoB3gXIx6_T6aWhfoYbW8HVkfek1rFkr72bc8OwkWn3bb9arfiUkoQxVeb2yoiHQSjcHoT8omv1dSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=HNm82wDP0EcdtEwUngZjZ40rYGD3CZ1e92shckzF3jGN8BgoLfU-Def-r8k9_bfJbOxT6AoDMSVAdeDFDITBeDC-371c7md7BLW509RXFRoosPx_pxGac2JDaohGqHd4oenipCPRBZqyer2JnZRa0YuMGAgePCjPmN-PRguFyzXovHVpM1NCD6vVIq1FspNFp06FRjcn3DrHaLZlzN3SFJ8HOYh03DHRMV0g9Xs7aNEEZQCT81THLpBHbHD6e4rLa1_cqieBoB3gXIx6_T6aWhfoYbW8HVkfek1rFkr72bc8OwkWn3bb9arfiUkoQxVeb2yoiHQSjcHoT8omv1dSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز پنج‌شنبه اعلام کرد اگر تهران طرح دریافت عوارض برای عبور از تنگه هرمز را اجرا کند، رسیدن به یک توافق دیپلماتیک میان ایالات متحده و ایران غیرممکن خواهد شد.
او در گفت‌وگو با خبرنگاران گفت: «هیچ‌کس در جهان از سیستم عوارض‌گیری حمایت نمی‌کند. چنین چیزی نمی‌تواند اتفاق بیفتد. غیرقابل قبول خواهد بود. اگر آنها همچنان دنبال اجرای آن باشند، رسیدن به یک توافق دیپلماتیک غیرممکن می‌شود. بنابراین اگر بخواهند چنین کاری انجام دهند، این تهدیدی برای جهان است و کاملاً غیرقانونی است.»
او همچنین خبر داد که در مذاکرات با تهران برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «پیشرفت‌هایی» حاصل شده است و به گفته او «نشانه‌های خوبی وجود دارد»، اما واشینگتن با «سیستمی روبه‌روست که خودش تا حدی دچار شکاف و چنددستگی است.»
وزیر خارجه ایالات متحده با اشاره به این که مقام‌های ارشد پاکستان به عنوان میانجی مذاکرات امروز به تهران سفر خواهند کند، گفت: «ترجیح رئیس‌جمهور آمریکا این است که یک توافق خوب حاصل شود... من اینجا نیستم که بگویم حتماً چنین اتفاقی خواهد افتاد، اما اینجا هستم که بگویم ما هر کاری بتوانیم انجام می‌دهیم تا ببینیم آیا می‌توانیم به توافق برسیم یا نه.»
او در عین حال افزود که اگر یک توافق خوب حاصل نشود، دونالد ترامپ «به‌روشنی گفته است گزینه‌های دیگری هم دارد.»
پیش از این گزارش‌هایی درباره سفر روز پنجشنبه فیلد مارشال عاصم منیر، رئیس ستاد ارتش پاکستان، به تهران منتشر شده است. خبرگزاری‌های رسمی ایران این خبر را یک روز پس از آن منتشر کردند که وزیر کشور پاکستان، برای دومین‌ بار طی هفته جاری وارد تهران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/75597" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JbGxywyp2cBnKkjN9CfdJ4u8s2JuKbZ_7xkJiKCgWZa3HrwSqJsypQ613VkRhfvHiiP2OvoPhHNiaZLrOueDXKJ52U7AYUHznW1wpopr1oPqfuckpLaLEZewCDDzrs5tL7dRSB2VssqRf0xw6OubTvOojK7a0qQQStG2KKBeGnjllxoDFGzqexO45t__hxrt0d-dlwxaJunVR9s9J8E30m_TXIb_9KChOAGKuPPSx8R2Et75OFwxeJfRWLnTh7KRi0aPmBYB74MCVcONbhUQhUB73-zLC8A8yXwz5JqGmgkMiVucNJH9iPbgvMOM22c6cTDtcVanCWHJ8418ppVtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس نیوز به نقل از یک منبع آگاه از روند مذاکرات خبر داد که کاخ سفید گزارش خبرگزاری رویترز مبنی بر این‌که مجتبی خامنه‌ای دستور داده اورانیوم با غنای بالا در ایران باقی بماند را رد کرده و آن را نادرست دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/75596" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VeNQc0rhhWrZX2C8RXdulh7ecATjIV1xW7rr7LsEa3Nppo3YKiPIIbETf576sEFnB-EOWugHA4AKJ6Sy9iA_lGyh67FHFPvZ_x7P5wJbgLwoEG9uzTZ65USovNBEWaFoj79OagDyCQhQyObq136iPfcZmNhAAzedERB9bUoKTRupMixTHtXFJhTC3U9J1FHvXCgVYXfUgbUJ4zomPhAOQ0mWA7UPk_rAE75l-eRlVLGecDf4HvEMzCWrTFQzTwPV9k9K3R1QUt34jh7fFT4qfy2ICbkl2h44i1ErL23p-Rc9Ld5jgtXHAtj6psuzRpA9mRy-7DNoUm8cKkhK7dnF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تحقیقی FTM هلند در
گزارشی
نوشته که توماس اردبرینک، خبرنگار هلندی نیویورک‌تایمز و شبکه NOS در ایران، همزمان مشاور شرکت آبجوسازی هینکن هم در ایران بوده و برای این کار ماهانه تا یک‌سال ۵ هزار یورو دریافت می‌کرد. اردبرینک دریافت مبلغ را انکار کرده.
طبق این گزارش این روزنامه‌نگار به طور منظم کارهای جانبی (پروژه‌ای) برای این شرکت آبجوسازی در ایران انجام می‌داده است و نه تنها کارمندان اعزامی و بازدیدکنندگان را در تهران می‌گردانده، بلکه گفته این شرکت آبجوسازی را با وکلا و مشاوران محلی نیز مرتبط کرده است.
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/75595" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOXvPlUaUPBcOQer8iAzJ_WkZwQEIFP5qaOlRanXP4tA9b2XoMVxrgGSceZkGPV0z24OHowxTuanTyFcKoO1teSuR0rAW-xLPf_MHVFd-KiTzvuiMVINHwwqK17Lf5qDIdpKw-1FekctCjBS5Opv5H7FzPTmeK72r4AoraMPL0b-splrh5AtgCV33MRRg0xHCsvTnvk99RBjBgRF_KM3JxwtKaIQgx_-wz7ehfbnD10k_x8_8cjNmKQGHt8uYV5Bd1qJnZ923ulGra03jwnD1VBtlWzA_HRXfqtGj2Ua4CNkn9I_TxxKXshlmQpw5or9KCbRdSW3ASkz9XiJzRY1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انور قرقاش، مشاور ارشد رئیس دولت امارات متحده عربی، می‌گوید که برخی رفتارهای ایران در سال‌های گذشته باعث کاهش اعتماد میان کشورهای منطقه خلیج فارس شده است.
او در پیامی در شبکه اجتماعی ایکس نوشت که کشورهای منطقه طی سال‌های طولانی با «رفتارهای زورگویانه و تهدیدآمیز» ایران روبه‌رو بوده‌اند؛ رفتارهایی که به بخشی از واقعیت سیاسی خلیج فارس تبدیل شده است.
آقای قرقاش همچنین تاکید کرد که شکاف میان مواضع تند و ادعاهای دوستی از سوی ایران، باعث از بین رفتن اعتماد و اعتبار شده است «و امروز، پس از تجاوز وحشیانه ایران، حکومت ایران تلاش می‌کند واقعیت تازه‌ای را که از یک شکست آشکار نظامی به‌وجود آمده تثبیت کند؛ اما تلاش برای کنترل تنگه هرمز یا تعرض به حاکمیت دریایی امارات متحده عربی چیزی جز خیال‌پردازی و آرزوهای دست‌نیافتنی نیست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/VahidOnline/75594" target="_blank">📅 17:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=buufqrPdJIjHUJic26-Z8K_1LKCD_XijT0S6Trk6Ga6QSHZFqGHH0pjnj2dOR8DiVHTo0ZKsUQvkkXzsZTaOz6_jfn-wRISoigb9ne2jTwBXUBLuc0MgPp4w3ywzon2atwxODfCU5STWp2Xd1-sQvkU5oJHc4YdCkCJzZKFLnjmefwkMc-mjf_tXGX_NfKgSLx8Bv4vq8wmZLhHZI0_iKNzFHLhW-42ZcbU9TRW76wpnBnqhrlxhiP0zG2XclfHaDKQU49Hsqk5Pn47OQ4rumK-045rqmojyVR2vAUjzCxxNLXAKf02DRjIpk9eF36Zsh9ngzdzCtWIEBrkecdiNcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=buufqrPdJIjHUJic26-Z8K_1LKCD_XijT0S6Trk6Ga6QSHZFqGHH0pjnj2dOR8DiVHTo0ZKsUQvkkXzsZTaOz6_jfn-wRISoigb9ne2jTwBXUBLuc0MgPp4w3ywzon2atwxODfCU5STWp2Xd1-sQvkU5oJHc4YdCkCJzZKFLnjmefwkMc-mjf_tXGX_NfKgSLx8Bv4vq8wmZLhHZI0_iKNzFHLhW-42ZcbU9TRW76wpnBnqhrlxhiP0zG2XclfHaDKQU49Hsqk5Pn47OQ4rumK-045rqmojyVR2vAUjzCxxNLXAKf02DRjIpk9eF36Zsh9ngzdzCtWIEBrkecdiNcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریتانیا از توافق تجاری ۵ میلیارد دلاری با کشورهای خلیج فارس رونمایی کرد؛ توافقی که در بحبوحه تنش‌های منطقه‌ای پس از جنگ ایران، به گفته لندن «پیامی از ثبات و اعتماد» به بازارها می‌دهد.
این توافق با شورای همکاری خلیج فارس شامل عربستان، امارات، قطر، کویت، عمان و بحرین است و قرار است سالانه حدود ۳.۷ میلیارد پوند به اقتصاد بریتانیا اضافه کند.
لندن می‌گوید ۹۳ درصد تعرفه‌های کشورهای خلیج فارس برای کالاهای بریتانیایی حذف می‌شود؛ از جمله محصولات غذایی، خودرو، صنایع هوافضا و الکترونیک.
در مقابل، بریتانیا نیز برخی تعرفه‌ها را کاهش می‌دهد، هرچند نفت و گاز کشورهای عربی پیش‌تر هم بدون تعرفه وارد بریتانیا می‌شد.
فعالان حقوق بشر از نبود بندهای الزام‌آور درباره حقوق بشر در این توافق انتقاد کرده‌اند و آن را «عقب‌گرد اخلاقی» توصیف کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/VahidOnline/75593" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8hGLKA_7du-_5Dh9RPHLPRIuVMHfG0AraWpQGEt8Wkavd77crl7l3_S3DGW9qDTvYVkYvJe_v_RH0KFO3gWUiG6kp4i3lHL-UztBBa7fgzO6JU23g8zgFO-_998PuUGzeQheoT_j2RohGpjzorqbSfppAhoXi3XCNF30JI-xu8F0QXLwZ21n48zjC9D7GC2TX7kiZhbwn9ZHpQhFYLCGKZQVojeGS05TxNbrvG33205zmoj1euLxAM11BC6fkYb8FhdrZe6HiAmyHJ-5SwrcuqzDOZYrCkZjtqUevJ8Oc7Aw8m47ZjQbTSEyAtnDsXVnJfsSeOywsacRY4zpH9Orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی یزدی‌خواه، نایب‌رییس کمیسیون فرهنگی مجلس، گفت در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد و محدودیت‌ها با «ملاحظات امنیتی» ادامه خواهد داشت.
یزدی‌خواه قطع اینترنت جهانی را به مصوبات شورای عالی امنیت ملی نسبت داد و گفت این تصمیم به‌دلیل «مسائل امنیتی، امنیت کشور و حفظ جان افراد» گرفته شده است.
با وجود اینکه نت‌بلاکس اعلام کرده خاموشی اینترنت در ایران وارد هشتادوسومین روز خود شده، یزدی‌خواه گفت بیش از ۹۰ درصد نیازهای مردم در وضعیت فعلی برآورده می‌شود و مراجعات گسترده‌ای در اعتراض به قطع اینترنت وجود ندارد.
او همچنین گفت در قالب طرح موسوم به «اینترنت پرو»، تاکنون بیش از یک میلیون نفر دسترسی دریافت کرده‌اند؛ طرحی که منتقدان آن را مصداق اینترنت طبقاتی و تبعیض‌آمیز می‌دانند، زیرا دسترسی به اینترنت جهانی را به گروه‌های خاص محدود می‌کند و شهروندان عادی را از حق برابر دسترسی آزاد به اینترنت محروم نگه می‌دارد.
نایب‌رییس کمیسیون فرهنگی مجلس همچنین گفت شرکت‌های صادرات و واردات، مراکز علمی و پژوهشی، آزمایشگاه‌ها و برخی اصناف در صورت نیاز می‌توانند برای دسترسی به اینترنت بین‌الملل اقدام کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/VahidOnline/75592" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2nx2ghJTqkYDsZgj03_yQa6nrNBDL_KBxYeLnEE-YSCUB-m7sPJO852FWbyTPuBFOh5fKFEwULtrV9SLecXeLcHt0IE0e4v57FLavytyB2JmEks0ZHXmIRSGUw9kusSAtak1x8zYD5Gg6UFDmSfry9P0T7HTp7HRQsNprSD04KVEBzc_ZZwFR2ed_o0kE-qWDcRnVDLgDwwlhkjsFxVGKRMh0irb1_Jg1-gA36VqGqaHVnSmfX_121VA_gsBqVMOe7N0V5Y6aXE_3PXEOntRVpd1DGmhcnBFSvphioC3huPBSlaPwpryWnDHqp79v2WxbmGGpqgcw6oSgz4xgVqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد در حکومت ایران گزارش داد مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده ذخایر اورانیوم با غنای بالا نباید از ایران خارج شود.
به گفته این منابع، این دستور موضع تهران را در برابر یکی از اصلی‌ترین خواسته‌های آمریکا در مذاکرات برای پایان دادن به جنگ آمریکا و اسرائیل علیه جمهوری اسلامی سخت‌تر کرده است.
مقام‌های اسرائیلی نیز به رویترز گفته‌اند دونالد ترامپ به اسرائیل اطمینان داده هر توافق احتمالی باید شامل خروج ذخایر اورانیوم غنی‌شده از ایران باشد.
یکی از منابع ایرانی به رویترز گفت دستور رهبر جمهوری اسلامی و اجماع در ساختار حاکمیت این است که ذخایر اورانیوم غنی‌شده نباید از کشور خارج شود.
به گفته منابع رویترز، مقام‌های جمهوری اسلامی معتقدند انتقال این مواد به خارج، جمهوری اسلامی را در برابر حملات احتمالی آینده آمریکا و اسرائیل آسیب‌پذیرتر می‌کند.
@
VahidOOnLine
دقایقی پس از این خبر رویترز بهای نفت در بازارهای جهانی نزدیک به دو دلار افزایش یافت.
قیمت هر بشکه نفت خام برنت دریای شمال بعدازظهر پنجشنبه ۳۱ اردیبهشت‌ماه در بازارهای اروپایی از ۱۰۵ دلار به بیش از ۱۰۷ دلار افزایش یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/75591" target="_blank">📅 17:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X452vkkpM0nQTqvPpOJceEqJozAd9kZuG8VUH2mkHZnI9JMKGLzWBkxcZq5Rymjk4qAPFc6iTOAssAlXY450koYyxS_4t-xFZSkCG-FaSmzzzYI4thvVgSAz28kSXl6R60OtR4o0GN2Te8DAni-xPT7g6F_G-eE-J-nk2_d5F0dzNeTTmohafE0cM1S_w5cn7cRwBgcxgyuB74RlqFHJ63Dns8HgA6lBzOS0IQmXQGxOnJTpff1JvpDZgxbdMmleBvNClv1_8R1gv6_5vBTUGCtPmWucAcV2kLtsUbPbXr2difE0bTKPJttxVYuzDlQm_G7uFaesK4zfCFcAyZ6-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی کابی‌زاده، شهروند ۴۷ ساله و پدر یک دختر بود که در اعتراضات دی‌ماه در استان خوزستان بازداشت و پس از انتقال به مرکز درمانی به دلیل منع رسیدگی جان باخت. او دختری به نام حلما دارد.
بر اساس اطلاعات رسیده به ایران اینترنشنال از افراد مطلع از خانواده او، مهدی کابی‌زاده در اعتراضات اهواز به دست ماموران بازداشت شد و سپس به دلیل بیماری خونی و روده به بیمارستان منتقل و بستری شد. با این حال، مسئولان بیمارستان به دلیل سابقه حضور او در اعتراضات و بازداشتش از رسیدگی و درمان کافی خودداری کردند که موجب جان باختن او شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/75590" target="_blank">📅 17:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugLJDM8CRyU9Ir0dZpZwLfaE9Z3nyfyQlPQW5yBzAvrdLUHvko1RGKQGoxtdH3vpw80s3eTU29yRHbFsouzr8HSe92zlrrTWEM35UDTSpOzvFqEXp8DmXcH_8W4a8PoLy7ayZseqaqi3GH-gRaWliay6mWSt_n8Ey0aFCsstJ6iJAG4wCSeAq_P-yuaPAlIwoEPTfOr88vB9goQbOSnFAIbmKr10Ro0RBo4M-BKgt-bnCsw9MX3t3xYJ5PzarJ2HPuvIrncw8eheTWQI_av9j16Z2l4ia9ztZrMDmJCJ3clYSlQHSxwegFRylpTfCzLvB0P4yxaC3HPsiJH9M4aALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی دو زندانی را به اتهام عضویت در «گروه‌های تروریستی تجزیه‌طلب» و «قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه» اعدام کرد.
ارگان رسمی دستگاه قضایی ایران، میزان، هویت این دو نفر را رامین زله و کریم معروف‌پور معرفی کرده و نوشته که آنها صبح روز پنج‌شنبه، ۳۱ اردیبهشت، اعدام شدند.
میزان نوشته که رامین زله «پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند».
ارگان رسمی قوه قضائیه ایران همچنین نوشته که این دو نفر «اعتراف» کرده بودند که «برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور» با یکدیگر «همکاری» داشته و برای این کار، «سلاح» نگهداری می‌کردند.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75589" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/622e876399.mp4?token=JIp6xcKmWP1k3UO5Dh5DBCjpmQDrLHSb3Yeo8fqJ_xUr6WyZuB0BBZ43-mDShRzi1NyBYFFvAuvSQ7ijoZHXT42GnL1FVNqeMOYUydQLao6bP8rXYah0rdRFmeG3SXv3xNjiN1BQ47FU4rPNuo8TlSIAdfTE01VrUOI6aJTB2fYkUkgSPXZFFP5bTv3PzIxuWriwnPtIJz38owGafmvDEPHfWWS64L-zDHu0o2FZVPl1ubcTbLQR15Uwo0WPJq38flwEP2IXNFPFCWHQq08kLuKLtxNywgksjK8P4Ae7-aUUl8qnitgMzmxeTERvtcXT-3Tk3HXkX8J8KKzClK3pEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/622e876399.mp4?token=JIp6xcKmWP1k3UO5Dh5DBCjpmQDrLHSb3Yeo8fqJ_xUr6WyZuB0BBZ43-mDShRzi1NyBYFFvAuvSQ7ijoZHXT42GnL1FVNqeMOYUydQLao6bP8rXYah0rdRFmeG3SXv3xNjiN1BQ47FU4rPNuo8TlSIAdfTE01VrUOI6aJTB2fYkUkgSPXZFFP5bTv3PzIxuWriwnPtIJz38owGafmvDEPHfWWS64L-zDHu0o2FZVPl1ubcTbLQR15Uwo0WPJq38flwEP2IXNFPFCWHQq08kLuKLtxNywgksjK8P4Ae7-aUUl8qnitgMzmxeTERvtcXT-3Tk3HXkX8J8KKzClK3pEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'کمور، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75588" target="_blank">📅 03:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1R9xrBqQNg_VUHgbpnEZJ_Pl9Zow4t8LycYBSkag0cg5zLy0Woan_f-Stn_oOhRnkiaQUTpGVe81x9WJx6rvapuwQFJ7CuxCdG_0zFaCYSbWt7zVi6KDRXtSMJ98t8Ok24wKv6FDJzfVjYAPJ_wsRNTDN4nR-WqozcHqKUq56Nle5mlUZMRwV-JseKqk9FHuMReWDhIm6wui3dTBAQXUSOBaI7z4jdEvhMZQwOSiZVnnue3cALCKlB0uiRjjDwjudzldWhACpsOZ275zvQNjZZBZIMnyvKGIHpMpSLObyC2esOfAyx6FLgJLetpOONZMdL-9SAFOxEnm3rTnnb8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید در شبکه اجتماعی ایکس، روز چهارشنبه ۳۰ اردیبهشت در پُستی، عکسی از رئيس جمهوری آمریکا، دونالد ترامپ را منتشر کرد که زیر آن تصاویری از «دشمنان خنثی‌شده آمریکا بدست پرزیدنت دونالد جی. ترامپ» دیده می‌شود.
در این پست تصاویری از علی خامنه‌‌ای رهبر کشته‌شده جمهوری اسلامی، نیکلاس مادورو رهبر دستگیر‌شده ونزوئلا، رائول کاسترو رهبر سابق کوبا، و ابو بلال المنوکی از رهبران داعش که به جای تصویرش پرچم داعش نشان داده شده، منتشر شده است.
کاخ سفید در مورد کاسترو، روی تصویر او نوشت که علیه او کیفرخواست صادر شده است. در مورد مادورو روی تصویر او نوشت که دستگیر شده است. و در مورد علی خامنه‌ای و ابو بلال المنوکی روی تصاویر آن‌ها نوشت که «کشته‌ شدند.»
حساب رسمی کاخ سفید افزود: «عدالت اجرا خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75587" target="_blank">📅 03:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lqe_Mbs-iCQQUCe5bovjVQCv8sQLOI-aBmaSX8OXJzMvN0nmeoU1cbnIUdSofZ_DoICwu4zqR-8biBFfn6JIToeFtSBTSF_x37KbCsK_K1iKx-AsQUaSXuPh5MH5V4INPVe8AEyrkaAgzLMIq4sBoXcCd0Uca9N-GBXe37tfg4K0yV3r0IN-AZ1PWBYxooUVJjCMlxDdcCbc060R5xtNNrJtsLR2-1UQe_5Arf157pLaA3rCOYwiSWNno81IHYo5NdjE2oEOhAybLHDQBWTufTJG4yiZL0M7S7OnZFWD-zeXWAHa_8Kc0XivQX5cvUmSd-xZ4JM3Sg76DnmRvWrS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیل هیوم به نقل از «منابع آگاه» نوشت جلسه چهارشنبه ۳۰ اردیبهشت در کاخ سفید درباره ایران با اختلاف‌نظر شدید میان مقام‌های ارشد دولت آمریکا همراه شد، اما رییس‌جمهوری آمریکا در نهایت، خلاف نظر وزیر جنگ و وزیر امور خارجه، و همسو با دیدگاه جی‌دی ونس و فرستادگان ویژه‌اش، ادامه مذاکرات با جمهوری اسلامی را تایید کرد.
این روزنامه راستگرا نوشت ارزیابی مارکو روبیو، وزیر امور خارجه، و پیت هگست، وزیر جنگ آمریکا، این بود که در این مرحله، بدون اعمال فشار قابل‌توجه، از جمله تهدید به حمله و تشدید تحریم‌های اقتصادی، نمی‌توان از جمهوری اسلامی امتیاز گرفت. در مقابل، ونس معتقد بود تازه‌ترین پیشنهاد تهران نشانه‌ای از انعطاف است و می‌تواند زمینه حرکت به سوی یک توافق اولیه را فراهم کند.
منابع آگاه از این جلسه به اسرائیل هیوم گفتند که استیو ویتکاف و جرد کوشنر، فرستادگان ویژه دونالد ترامپ نیز در این گفت‌وگو از موضع ونس حمایت کردند.
آنها پیش از این جلسه با رهبران عمان، قطر و عربستان سعودی گفت‌وگو کرده بودند.
به نوشته این رسانه تنش در این جلسه زمانی شدت گرفت که ترامپ از ونس و فرستادگان انتقاد و آنها متهم کرد که رویکردشان به جمهوری اسلامی امکان می‌دهد زمان بخرد و به تصویر ایالات متحده و نهاد ریاست‌جمهوری آسیب بزند. ونس با لحنی قاطع پاسخ داد که دولت باید به دنبال پایان دادن به این کارزار نظامی، بازگرداندن سربازان به خانه، کاهش قیمت نفت و تمرکز بر مشکلات داخلی آمریکا باشد؛ پاسخی که حاضران را غافلگیر کرد.
اسرائیل هیوم در ادامه این گزارش به گفت‌وگوی ترامپ با رهبران منطقه اشاره کرد و به نقل از دو منبع نوشت که رهبران اسرائیل و امارات متحده عربی، همزمان با تاکید بر ضرورت حفاظت از تاسیسات حساس خود در قبال حملات احتمالی جمهوری اسلامی، از پیش گرفتن «سیاست‌های سخت‌گیرانه» علیه جمهوری اسلامی حمایت می‌کنند.
در مقابل، رهبران عربستان سعودی و قطر ترجیح می‌دهند از بازگشت به درگیری‌ها پرهیز شود.
این روزنامه همچنین به نقل از یک مقام آمریکایی درباره تماس تلفنی ترامپ با نخست‌وزیر اسرائیل نوشت که نتانیاهو از رفتار جمهوری اسلامی و احتمال وقت‌کشی تهران ابراز سرخوردگی کرد، در حالی که ترامپ بر پیچیدگی شرایط و دشواری‌هایی پیشِ رو تاکید داشت. با این حال رییس‌جمهوری آمریکا بار دیگر گفت که به رفع تهدید هسته‌ای حکومت ایران متعهد است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75586" target="_blank">📅 02:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKCd0ka1cAgzzWaZt_rNUY_4GoIl7-fy4YiGGGbupQNWaOpgj9xKhWDDSwqO9yHEiVC3subnM49uAD1ctrAHAk2UbVUvxnDY4fSQxEtl8Fnc_jWpXqR03YDxCwxXv-NkT5HI36OROxssE_yPMMGDbGQ137cnrjcGceWndthMuTub4kkKBz9Oa77XeBfuHs63DNeW9nLk61QQDR8i8KAmyyIedtLXAa2F5u48Tw6gGf34xoP6HIx9IQfKq5j7SJFgPWL7gxaZdPnMetETorMhtSZ9BYu1NWKh8uo9I75Lm6tRgO45Nu8AfKihOSpHn6R7i4Oo_oZUAqC9dyhF3M-FBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=gZKIw1D-9M7Spjg42ipEwH7pH7HCdsknPr_UgwfYZSodzF2E56-CHFPZ_7OXyK_WMVjeAwY22kC5Frqc9d_R5SHKOClriWHeUC7I-zKvMR9_G239fEjpVYFI2TTiaN2s5VfLgp8U_47bfLd8BSH1X9w9oK8wXgOrubjofsOY-ny1TlBHfHlc9txIBrFR-acOQ_io97k3KIO2tWOd_csptnyjSbRx6nHdUlXSpCiZRhEe-u3iaLHkV3wWyjsRJyqpCq1YXQ4iszLKGr2U-XvbyEMfhy5Fg9ENHpZoBZHoCUgh3Bo94Tqh_9t_OEJH8eEeRQm7itz0QAroMN30K3Uzbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=gZKIw1D-9M7Spjg42ipEwH7pH7HCdsknPr_UgwfYZSodzF2E56-CHFPZ_7OXyK_WMVjeAwY22kC5Frqc9d_R5SHKOClriWHeUC7I-zKvMR9_G239fEjpVYFI2TTiaN2s5VfLgp8U_47bfLd8BSH1X9w9oK8wXgOrubjofsOY-ny1TlBHfHlc9txIBrFR-acOQ_io97k3KIO2tWOd_csptnyjSbRx6nHdUlXSpCiZRhEe-u3iaLHkV3wWyjsRJyqpCq1YXQ4iszLKGr2U-XvbyEMfhy5Fg9ENHpZoBZHoCUgh3Bo94Tqh_9t_OEJH8eEeRQm7itz0QAroMN30K3Uzbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه چهارشنبه گفت حاضر است «چند روز» برای رسیدن پاسخ ایران به پیشنهاد واشینگتن درباره توافق پایان جنگ صبر کند اما هشدار داد که این پاسخ باید «۱۰۰ درصد درست» باشد.
او بعد از سخنرانی در جمع دانشجویان نظامی به خبرنگاران گفت اگر پاسخ ایران درست نباشد، تشدید تنش به سرعت رخ می‌دهد و افزود: «ما آماده پیش‌روی هستیم. باید جواب‌های ۱۰۰ درصد درست و خوبی بگیریم.»
ترامپ اعلام کرد که آمریکا در حال حاضر با افراد «خیلی خوبی» از طرف ایرانی مواجه است که «استعداد و قدرت ذهن» دارند؛ افرادی که به گفته او جایگزین رهبران پیشین ایران شده‌اند.
این اظهارات ساعتی بعد از آن است که سخنگوی وزارت خارجه ایران اعلام کرد تهران در حال بررسی طرح پیشنهادی جدید آمریکا است.
این طرح توسط اسلام‌آباد به دست مقام‌های جمهوری اسلامی رسیده است؛ همزمان با سفر وزیر کشور پاکستان به تهران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75584" target="_blank">📅 23:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OjCD64bTFRd86__mZjXU7rcIhOQPUT1cmxGFxQOAH2TR3YMVXxX-ahh385m_lA9b7BlosOid_exk5icl_iB-f1T9R9pwBL5ndpWHzKKJvzQAYKuY8cEONwWk1wBmpr9vxPdya6_1GJhh-XMsIe0pwZI5lcJpoLH2agHx1ncC-Z3-b_WD1jvGrlyEbxUSTaBrMXvAgImlEzWFI2hAg6X-4f4AX-023fhMe29F7_iFo1R2OzP4J4ZoE75MueNKA5h783QZrO49_h_4pc5K9lEX2KpHQShv3SiW-s_Tg1JFJuCXmUA5NaFh6NDsjRBMMiUuzfdJDq3AfEH7hjzpwt9SOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PVGf0x2o68pn9uH-JVdzp58jHx-tOtz9M6YoHy3I1KKcEuM-Wt1xwCkLro_wlgvQUKCvEvyxjye-Hv0AvqDh0vSoeVpL2Hr69LA7iRWruJXhxsbfriTv2u2sO9-CeCVPAXIZNYJuujzBcfGGfid_woovQmrF_J9OmGljwc41SZ3kMyP3JimbGKPkJZpVthNQ9GSIcLL5FLFjEOe_LPsG_pw3-yg69w3n3lzRg-9cxYND0OQcE6bQU8fMmsY5eVVppmyXAH11amSPPVKcdhAiomiJf8JOITmkfKCSdzzxHH9UsIDlHkXs0pFLPPvGnWY5FtIS8A2uYQcuIFQ5MF0aXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس در گزارشی اختصاصی اعلام کرد دونالد ترامپ در تماس تلفنی طولانی و «دشوار» خود با بنیامین نتانیاهو، از تلاش میانجی‌ها برای تدوین یک «تفاهم‌نامه» خبر داده است. بر اساس این طرح، آمریکا و جمهوری اسلامی با امضای این تفاهم‌نامه رسما به جنگ پایان داده و یک دوره ۳۰ روزه را برای مذاکره درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کنند.
به گفته دو نفر از منابع آکسیوس، این پیشنهاد با مخالفت شدید نخست‌وزیر اسرائیل مواجه شده و دو رهبر درباره مسیر پیش‌رو اختلاف‌نظر جدی دارند. یک مقام آمریکایی وضعیت نتانیاهو را پس از این تماس، «بسیار خشمگین و آشفته» توصیف کرد.
آکسیوس به نقل از منابع خود نوشت سفیر اسرائیل در واشنگتن نیز نگرانی شدید نتانیاهو از این گفتگو را به اطلاع قانون‌گذاران آمریکایی رسانده است؛ هرچند سخنگوی سفارت این موضوع را تکذیب کرد. یکی از منابع با اشاره به بدبینی همیشگی نتانیاهو به روند گفتگوها گفت: «بی‌بی همیشه نگران است.» کاخ سفید و دفتر نخست‌وزیری اسرائیل از اظهارنظر در این باره خودداری کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75582" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=lw1CJmvbjMQwCtecM3G0QmXqE9fJzABD98hJDwkeQc00XCeLMq4BtM8XjjG7VKBGMBLQNREZiXmkeM5ywsnWUlVZJ2EIGpxuan4B2eSr5bd7LiRaFG2ZBh_YYxJ8m81oJcpMzdqvrNgvnaMFoA5rYLwYRZX6WQF5oV0UjPWEe2oNyj8MovofNmMU0Ks5Se_Ir40PjN8v3P9kYzJ3lCwlTI-QU0LJh_ncp35fezXDHSeCZMPgWJiX3BLXBwXA8lOZBoG1ZV9sRqjTy0CDPrW-WEiNYXAucIvhBFEQFc_gIQn6wmB1rTbzVjE9nMtQZo8hK6BaTevhy_njP-W0UyNMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=lw1CJmvbjMQwCtecM3G0QmXqE9fJzABD98hJDwkeQc00XCeLMq4BtM8XjjG7VKBGMBLQNREZiXmkeM5ywsnWUlVZJ2EIGpxuan4B2eSr5bd7LiRaFG2ZBh_YYxJ8m81oJcpMzdqvrNgvnaMFoA5rYLwYRZX6WQF5oV0UjPWEe2oNyj8MovofNmMU0Ks5Se_Ir40PjN8v3P9kYzJ3lCwlTI-QU0LJh_ncp35fezXDHSeCZMPgWJiX3BLXBwXA8lOZBoG1ZV9sRqjTy0CDPrW-WEiNYXAucIvhBFEQFc_gIQn6wmB1rTbzVjE9nMtQZo8hK6BaTevhy_njP-W0UyNMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز چهارشنبه ۳۰ اردیبهشت با تاکید بر این‌که نیروی دریایی و هوایی ایران از بین رفته‌اند، گفت اکنون تنها سوال این است که آیا آمریکا برای تمام کردن کار بازمی‌گردد یا جمهوری اسلامی پای امضای یک سند (توافق‌نامه) خواهد آمد.
ترامپ که در مراسم فارغ‌التحصیلی آکادمی گارد ساحلی آمریکا سخنرانی می‌کرد، گفت: «همه چیزِ آن‌ها از دست رفته است؛ نیروی دریایی‌شان نابود شده، نیروی هوایی‌شان از بین رفته و تقریبا همه‌چیزشان را از دست داده‌اند. اکنون تنها سوال این است که آیا ما پیش می‌رویم تا کار را تمام کنیم، یا اینکه آن‌ها یک سند را امضا خواهند کرد؟ باید ببینیم چه پیش می‌آید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75581" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dDrliBWTZR5OvzgdZLdRoIu8sNFci8qXnjvmFRnoUJSdpeoGMY5w5hz2OaLU_9nTXSzLaTVTdWzCMwFKJFTy1i1uCAAnFkTRl9IkwrkLc5Rf7IHroBxuvGBazVLrBfokZ3Ih7Aan7IgzlAAuvgpDPJPt9F0AuDIjJbd_grUaDH3B0JBIUpGnnPZSnBF2wSrrNyiuXTuPZdzsNl3s1lyhJVefduyT-ZaRe7nH7jzS1Pplq6FSuZYq29emDbWkJvBM1B37mI-ZEWVO2rebn27WB9ov_gvfdBeiTa00CAFjxmTJZ-oGAdeI_4XkGnpcNR3SkUCFX0XEFXJpVlpNFErDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت، چهارشنبه ۳۰ اردیبهشت پس از اظهارات خوش‌بینانه دونالد ترامپ درباره مذاکرات با جمهوری اسلامی بیش از پنج درصد کاهش یافت.
بهای نفت برنت به ۱۰۵ دلار و ۷۰ سنت رسید؛ زیرا معامله‌گران به نشانه‌هایی واکنش نشان دادند که حاکی از نزدیک‌تر شدن واشینگتن و تهران به توافقی است که می‌تواند از دور تازه حملات جلوگیری کند و نگرانی‌ها درباره اختلال طولانی‌مدت عرضه در خاورمیانه را کاهش دهد.
ترامپ گفت مذاکرات با جمهوری اسلامی در «مراحل نهایی» قرار دارد، اما هشدار داد اگر تهران با توافق صلح موافقت نکند، آمریکا ممکن است حملات بیشتری انجام دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75580" target="_blank">📅 20:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75579">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fef1ZAUT3kBohmroBiQ4mWFQGs19ZmrgdKkBn7QigPvb2CA2PaMmUkb-RTN-OR0g_tCngOD1xVaW7teD-xfh2p7aqzZqR5eB64AuSBPBs65OMfESbnfE1ZxXKoQJvc6XbI7nyzaTdQwCAUDYcVovnAh7EXmCoXno-FniJmJjtkF02gJRtbAvsLzylhjaShtGfX1JDo-chpo3EuUQ4oskIrX_EWmvQWicfMh1j6S1uLrJQQ32kTKGj98HpsKlhl48WfDrmltqtjqWQ5CLGn1Hb5jyy5KACXAKDE3dJectzQZYFeEadhDY7OWhb0qIkzrHsObNTXPdvgor5jOB3U6Hpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیصل بن فرحان، وزیر خارجه عربستان سعودی، نوشت ریاض از تصمیم رییس‌جمهوری آمریکا برای دادن فرصت دوباره به مذاکرات با جمهوری اسلامی به‌منظور دستیابی به توافقی که به پایان جنگ و بازگشت امنیت و آزادی کشتیرانی در تنگه هرمز به وضعیت پیش از ۹ اسفند ۱۴۰۴ منجر شود، قدردانی می‌کند.
او همچنین از تلاش‌های مستمر پاکستان برای میانجی‌گری در این زمینه تقدیر کرد و در شبکه ایکس نوشت عربستان سعودی امیدوار است جمهوری اسلامی از این فرصت برای جلوگیری از «پیامدهای خطرناک تشدید تنش» استفاده کرده و فورا به تلاش‌ها برای پیشبرد مذاکرات پاسخ دهد.
وزیر خارجه عربستان سعودی افزود هدف از این تلاش‌ها، دستیابی به توافقی جامع است که صلح پایدار در منطقه و جهان را محقق کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75579" target="_blank">📅 19:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=PpaqNAMX5ehRWIHVkxgOBQ1l25RwDi-KxULka5X0OgF99QlEepojxg1u64uUi1Q6nOSubtL1wAWuYSfrv7HCVX1PUOuQX4yLHvXZLxS17ossL6NTAjEEJ38HdafZcZgbSB0MtpOQ1CMpzDuoXNmDgTVhSiO4cxI58oPIRBxEE-04H1L4icqntaIIbklBGCF1lLN4cagtAt4qS4DPxVANr0iFquxoZuFc0hUf2Qv1UTbrWl7suMsPOHcRjOlBFuLc3Wm11SpHk9WYg0Nsp6ilLWwlQxrMzj4gGdstC0IWEMFWl2Lu2Sfe5ziGUmX8ixaDjihVSaxPS-c_HMFqSFZzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=PpaqNAMX5ehRWIHVkxgOBQ1l25RwDi-KxULka5X0OgF99QlEepojxg1u64uUi1Q6nOSubtL1wAWuYSfrv7HCVX1PUOuQX4yLHvXZLxS17ossL6NTAjEEJ38HdafZcZgbSB0MtpOQ1CMpzDuoXNmDgTVhSiO4cxI58oPIRBxEE-04H1L4icqntaIIbklBGCF1lLN4cagtAt4qS4DPxVANr0iFquxoZuFc0hUf2Qv1UTbrWl7suMsPOHcRjOlBFuLc3Wm11SpHk9WYg0Nsp6ilLWwlQxrMzj4gGdstC0IWEMFWl2Lu2Sfe5ziGUmX8ixaDjihVSaxPS-c_HMFqSFZzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75578" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=GPz7kpKT5xu9DD2tYcb6cz35YkipGGCutqHp9RH9L2pbneCsPKPm9fzrMhoSuvSZ_mVIKpvu9rN9FJSZqiYiJzDQJ_-v-AicqTWKIPymbfnVTD9YG7SuHPJvXeAKczEZJGxjoECt3nNqDI3GWFYnaL7RafSEPuJQQKbvuh-X90ylVn7660z7XsPSlbCc1ftng3ypDoPZ9GT3q96dXwwfZilutdQ5A1lGHXdEOw-Sr8SLFizaUxYUmmhjOwSgiRWZXJZe2VnDMz9z-667F9NA4pwnzYRZL5h-BxulAMHb23fjQApCTYEDq2AyMcZZaiyJnAQu3l3GXiCQBUCfw4QBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=GPz7kpKT5xu9DD2tYcb6cz35YkipGGCutqHp9RH9L2pbneCsPKPm9fzrMhoSuvSZ_mVIKpvu9rN9FJSZqiYiJzDQJ_-v-AicqTWKIPymbfnVTD9YG7SuHPJvXeAKczEZJGxjoECt3nNqDI3GWFYnaL7RafSEPuJQQKbvuh-X90ylVn7660z7XsPSlbCc1ftng3ypDoPZ9GT3q96dXwwfZilutdQ5A1lGHXdEOw-Sr8SLFizaUxYUmmhjOwSgiRWZXJZe2VnDMz9z-667F9NA4pwnzYRZL5h-BxulAMHb23fjQApCTYEDq2AyMcZZaiyJnAQu3l3GXiCQBUCfw4QBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، پیش از ترک واشنگتن به مقصد کانتیکت، در گفتگو با خبرنگاران در فرودگاه به تشریح وضعیت تقابل با ایران و گزینه‌های روی میز پرداخت.
او با اشاره به وضعیت داخلی ایران مدعی شد: «در حال حاضر خشم زیادی در ایران وجود دارد، زیرا مردم در شرایط بسیار بدی زندگی می‌کنند. ناآرامی و تلاطمی در آنجا جریان دارد که قبلا نظیرش را ندیده‌ایم؛ باید دید چه پیش می‌آید.»
ترامپ در پاسخ به سوال خبرنگار درباره احتمال انجام یک «توافق محدود برای تمدید آتش‌بس» گفت: «ما این شانس را امتحان می‌کنیم. من عجله‌ای ندارم؛ هرچند موضوع انتخابات میان‌دوره‌ای مطرح است، اما در حالت ایده‌آل ترجیح می‌دهم به جای افراد زیاد، آدم‌های کمتری کشته شوند.»
رئیس‌جمهوری آمریکا همچنین با ابراز تردید درباره نیت مقامات تهران گفت: «من متعجبم که آیا آن‌ها واقعا خیر و صلاح مردم خود را می‌خواهند یا خیر؛ رفتار آن‌ها نشان می‌دهد که به فکر مردم نیستند، در حالی که باید خیر و صلاح کل منطقه را در نظر بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75577" target="_blank">📅 18:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R5GbxrNX8BQSo_bf4bFwEYsxe9HQQIOGaiREexuDu2qO9ClTv6F1axrCsE-7olOkMVDQTsuJXh_vLjf_Cb3yo92Ep9aNOZPbc35NvOAFLTMwtgDUbmS9G3zl4CvH8a6Pq3H0vsnWmq_J2221p3oyo3hHxkeuYIbMQrcu4oqrKHhGDp4CPbSy07Pr1R_lZY48TXq8SNX5olub2amu1XMTqcvw3NgbR6khkKxG0wVauATMOuKtnper5LlBZ5iNxvw0JV--MXMlxP-naDFMIZ_pq-3wxWj7Vl8Ba2tcOsecLM5vAek6U_fqjPhpePJAwXKaCd2N_2TtSu-qJYSG5yeNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U3-044Dbvc5NbLU47Oz3BiFNKhlD1f_d0lNSaX6Nrz_mrkQJNt4fLBtsFe_mwTsMxB2Ck9aow5VzPJYjlRyLeRwoKFlIoskMd8IxXLixxAaxCeWGxFCoLYo52HqIt03JiWrOk2srC5CdKuvjk_WSrfUHgPv-3hrDqIweGFgHNqLlUICfUkE7-Qc775SeKID0y2FQpTv35h2R6IQa6gqFi5V2oZIlSxiy01r1Z89gaHrvezfnlvdM_m-wYV-TiMMmt336PUg0RBePm5DFnGD0uBEQ21WoycS7wSLbVulZIRVuZw2TbKgKGUJkInC61Tu7PgSvYMJmOrV4sub62emzmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=bXhIoOhgz739DDcM_JZ4rEQOpc94FW0Z0_f7VAJ9aVx-VgUZpswYq3HOAx_pjW4ysLy4IOtAliSY5snKzxjmYY72ZlzzH9bsZiabE0PRGMhgqBJhK1asioMzJDiOK1G4AtHgNpn92oYbIenSXY8Fgy57DmNoIeftmCK-4xMkzVEe_cRdO1zNaniIa3dXoapLnK07GyqdrFo-t3whC1NSlHrUgVMTrLGvBg_4f6dn5LjeDjzj7OKIXE_W7BMzdnpNR6j_20dRC-Uc3UjWmxyG9Ul9YQWihmtAeWov0vi18hFui2ei85Xu_iFbXJWMw8xbIH_zrbh5lCeciNZRVELPag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=bXhIoOhgz739DDcM_JZ4rEQOpc94FW0Z0_f7VAJ9aVx-VgUZpswYq3HOAx_pjW4ysLy4IOtAliSY5snKzxjmYY72ZlzzH9bsZiabE0PRGMhgqBJhK1asioMzJDiOK1G4AtHgNpn92oYbIenSXY8Fgy57DmNoIeftmCK-4xMkzVEe_cRdO1zNaniIa3dXoapLnK07GyqdrFo-t3whC1NSlHrUgVMTrLGvBg_4f6dn5LjeDjzj7OKIXE_W7BMzdnpNR6j_20dRC-Uc3UjWmxyG9Ul9YQWihmtAeWov0vi18hFui2ei85Xu_iFbXJWMw8xbIH_zrbh5lCeciNZRVELPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز چهارشنبه ۳۰ اردیبهشت‌ماه درباره گمانه‌زنی‌ها راجع به سفر عباس عراقچی به نیویورک گفت:  «وزیر خارجه ایران برای شرکت در نشست شورای امنیت سازمان ملل درباره صلح و امنیت بین‌المللی دعوت شده، اما حضور او هنوز قطعی نیست.»
به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی «این نشست به ریاست دوره‌ای چین در شورای امنیت، روز پنجم خرداد برگزار خواهد شد، اما با توجه به برنامه کاری فشرده وزیر امور خارجه»، تصمیم نهایی درباره سفر هنوز گرفته نشده است.»
این اظهارات پس از آن مطرح شد که علی خضریان، عضو کمیسیون امنیت ملی مجلس، در یک برنامه تلویزیونی نسبت به احتمال سفر عراقچی به نیویورک برای مذاکره درباره تنگه هرمز انتقاد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75574" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/efWEny03ussWTIn9603lndUppcGGxS3C_rMK1cOV6dtRmNwrnlp5x-Xc4ZM9z-o-5cleoCmr5U97BRBq3QN-xWM28ie3fh4m0aafuXsPpUHdlrmRdX16c1VePzVSUSB7CpKGc_wbBdAGmy6_ieo7IjQ3mb0hx-1AKeGOsIfZ6603OTNuoxB6rgREMR_N0OA-V8Vwi_hpM2ERIoQKOKjRW2vfOWCt8AkVpU6RjX-MsIggP-uJ3RMfboBtKaOI-qWzpc6m7gWqgcwHDlX5L1kiDglHc-EzBzKqy-oYTprxfnGKrjnx3FNlgkbsBYdaTezL_vwWpcGiJzfatc8a-lq6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pXELvatRjQC8oGh-T-Fwo0-Hs1g7nmM2yjjKLF5lwyFiB3Zzz4au0pMcV_itgUUs5lRtmgJ0m7G_Tg3_7ZRjnksDzsH2ghnrWZvUSifQjXGzztLxsO_IpFH4G0GCNw8Zz8rez4sXYUAcVYGrEZiOXTVkYoNA4rlVIOxAcpW3OfDSCVFZ--UO_EQVIixESJhiplRp_OVM9tgrTomp5YaxLqrDcaoq96FVxxx2HZDyuXOIn-rYmDmrJbZZ2QWGiENgugE9ri9feWbIrV96r6nbyBJY0OSZau99s7ILQO2g7Qc0Ty6tlF9VEyv4IfFqT_dfnLnVdJfCYqUGRO60WxYohA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه گزارش داد رشید مظاهری، دروازه‌بان پیشین تیم ملی فوتبال و استقلال تهران، «هنگام تلاش برای خروج غیرقانونی از مرزهای غربی ایران بازداشت شده است.»
میزان در این گزارش رشید مظاهری را متهم کرده که «قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از کشور خارج شود.»
قوه قضائیه به زمان بازداشت این بازیکن پیشین تیم ملی فوتبال ایران اشاره نکرده است.
رشید مظاهری پس از کشتار معترضان در ۱۸ و ۱۹ دی، با انتشار ویدیویی در پنجم اسفند، علی خامنه‌ای را مسئول کشته‌شدن معترضان معرفی کرده بود. پس از انتشار آن ویدیو، تا مدت‌ها خبری از وضعیت او منتشر نشده بود.
خبرگزاری میزان گزارش کرده که مظاهری در «بند عمومی زندان» به سر می‌برد و قرار است به اتهام‌های «پرداخت رشوه به مامور دولت»، «فعالیت تبلیغی برخلاف امنیت ملی در شرایط جنگی» و «اقدام به عبور غیرمجاز از مرز» محاکمه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75572" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N1YtnC1PPZsLOEOMcpe0-Cm2gpp55ELn5gfbYT71XmZ3eKNK5aD9dE914PL8y11YOvjYA1MC_1dsqtWkn-p1vVwLEb4kZAaM55OxakUKVnybPY6YRo9xGDqC97pfOK6YT_jLDpjjjVcPPp4SKjFOTzRSKcK5ZBBhYjDW_FumQBgHDNl2osUG1D8JUwtXHsvLV5lu9xSxV3dvbuLad3jJeSY6r_es3OpPSQ_XXUhFMx6hrUi8FGX8TlL5boTrtVJTHUpLbDndf8BCn8ATTkw5BxLIFYkZAQ0HQYXKt7but2vYuKulIJ6kWH0vZUsxT9TuHNIcYDIKYeUdIKewmES3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در میانه اختلال در مسیرهای رسمی تجارت و فشار بر زنجیره تأمین صنایع، سازمان توسعه تجارت ایران واردات برخی مواد اولیه پتروشیمی و پلیمری را از طریق رویه‌های کولبری و ملوانی مجاز اعلام کرد.
این تصمیم نشان می‌دهد بحران تأمین مواد اولیه در صنایع پایین‌دستی به مرحله‌ای رسیده که حکومت برای جبران کمبود، به مسیرهای مرزی و غیرمتعارف متوسل شده است.
اما این تصمیم پرسش‌های جدی ایجاد می‌کند. مواد اولیه پلیمری و پتروشیمی کالای مصرفی ساده نیستند؛ واردات آنها نیازمند حجم بالا، کنترل کیفیت، استاندارد، ردیابی منشأ، بیمه، حمل‌ونقل تخصصی و تسویه تجاری منظم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/75571" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8UiZ-vvtRWwYbhzfGNnlBOTmdy9OODxD4DQPTVTsz9p4xm1i-otnRjuxNUqBi5W7GkAQsz-dqaCRrGXAtp-mzJxyMff9zfCLbE_CgSWSqIpJmuBQVpAwGnV-zUawJmoQstMEVv4clDhJnv5srKxIhAkYy2BYHef2Ysv-eUiCG8IdPlTNrJsrAyDmYgEFUnNNt0kwOL_4Dd75xlk6Lb0Ea5wMa2cibyPB2B562araUGKBaBFw7nE9VAIqQob-TpFXho6OqVTF9RAG8krreHs4J1iGTh1krA9OTQtC-nU1XfEvZgLX2C4y80pXCKQJYz5Am9WOKlqMtC9PK0ZVcAgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران با انتشار بیانیه‌ای تهدید کرده که در صورت آغاز دوباره جنگ آمریکا و اسرائیل علیه ایران، جنگ «به فراتر از منطقه کشیده خواهد شد.»
در این بیانیه با اشاره به تهدیدهای دونالد ترامپ و مقام‌های اسرائیل برای حمله مجدد به ایران آمده: «اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.»
عباس عراقچی، وزیر خارجه ایران هم در واکنش به اظهارات تهدیدآمیز دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال از سرگیری حمله نظامی به ایران، در شبکه ایکس نوشته «با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75570" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G73P58wM9ZqPskqCJI6kIFkQJsQz4kQBWAJA_j32zynqj8CdYFG3ilGeAK3NLlJ8g_CEHVKODpBf09H4AskMZ8sfdJD2zPee5wJmq-fhIx7d5fE_FfMMa3N7B41Y37Cvj-7gesnlyxalm78LT2Js-RmDJt9yfZrAWHCFYUsv1LrXlYOAUZw2HRW_OYuBaTRhn_RfqfFuqIfzst8oBnuYIBHIfj3TwF-GU7HbBW9_8Gn0FskQ_cIE4mIop_TtbOFGJjCi8uToBoqqjm2BAhoEUGnFzCBH-c-ppgx831uud44eTMqZY44IIT-CEMTUhl3LjPX3L1vd1tM7gq2mX_cpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران روز چهارشنبه ۳۰ اردیبهشت خبر دادند که محسن نقوی، وزیر کشور پاکستان، وارد تهران شده است. او روز ۲۶ اردیبهشت نیز به ایران سفر کرده بود.
خبرگزاری ایسنا اعلام کرده که برنامه و اهداف سفر این مقام ارشد پاکستانی در ایران «مشخص نیست». خبرگزاری تسنیم نیز گزارش داده که آقای نقوی در بدو ورود به تهران با وزیر کشور ایران دیدار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/75569" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX4UOIT6HVadgNJPULq8wZj5Zx-WndwUwAuYD27RO1YCmhhX8hCUp42aHrFnYIb0ibpSi-7zrNqaSJ---Z6YJXIQDfvMsc1roKAW4rUTezZ874maGS-S4L3GJq0GJmxo1ah0b8m8f9QYUr_tPe33cQ_vGq9W_QNuY_Yp5bsey3N0BWAfJzHdqBPeC7owR8464HI9ltMFO3jnzTmV1j4-jLy5UymaqvxbmbFHmkIRcB7WDCd6ZDbBavvl8QQA-LzsfUyV3RaCBadNLC7zHwrmQRBSH3XCLn534M5gjMTTGE7bywp8t7xA3v6XrPldn2m2S4KPYADfsywRrOEb1Nt01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از اجرای حکم اعدام قاتل الهه حسین‌نژاد، که جسد او اوایل خرداد سال گذشته در بیابان‌های اطراف تهران پیدا شد، خبر می‌دهند.
عصر چهارم خرداد ۱۴۰۴ الهه حسین‌نژاد ۲۴ ساله از سالن زیبایی که در آنجا مشغول به کار بود، بیرون آمد تا به خانه‌اش در اسلامشهر برود، اما ناپدید شد و وقتی خانواده‌اش اعلام شکایت کردند بررسی‌های تیم جنایی نشان می‌داد الهه از میدان آزادی سوار یک خودروی عبوری شده است.
جست و جوها برای یافتن الهه سرانجام پس از ۱۱ روز نتیجه داد و با دستگیری راننده خودرو به نام بهمن ۳۷ ساله و اعتراف به قتل الهه، جسد او در بیابان‌های اطراف تهران پیدا شد. متهم نیز پس از محاکمه به اعدام محکوم شد.
این قتل جنجال زیادی درباره امنیت زنان در ایران به پا کرد و تا مدت‌ها رسانه‌ها درباره آن مطالب مختلفی منتشر می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/75568" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggWrjh45Fk3uNYOpOOzHefhXknBeFrJGrhZpECb4GNjc0q2ZyeFzRYVLuD8-04jgujSQLH6S2o8d3wNUpCVjSqC67EQKKGOFPozl88dg9xqHzTDKKpAEHGOU54zm_ZINsnt6VhVIbEMLRqHoPuFwH9Z0t8sCnDKdQRNeRWBY0UUkvK7AGb_xj1uftjOUak3MLKjYW7fz3rBlmg1do61jrqp8DuQynshyv2kRJS74TflDo9htxsaabovHOiKCAShg-9v-VRHvIMJacEwIWS7bqQ852hIqpyKzirVwt-1cbHsgJRXZ1AKNFq10MHGIycwbDh_tEMcZCYrp1y06GVxrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حقوق بشری گزارش دادند دادگاه کیفری تهران پس از رسیدگی دوباره به پرونده شهرک اکباتان، سه معترض بازداشت‌شده در این پرونده را به دیه و پنج سال حبس محکوم و سه معترض دیگر را از اتهام مشارکت در «قتل عمد» تبرئه کرد. حکم اعدام این شش تن پیش‌تر در دیوان عالی کشور نقض شده بود.
سایت هرانا چهارشنبه ۳۰ اردیبهشت گزارش داد شعبه ۱۳ دادگاه کیفری یک استان تهران، میلاد آرمون، علیرضا کفایی و امیرمحمد خوش‌اقبال را بابت اتهام «مشارکت در قتل عمد» آرمان علی‌وردی، از نیروهای بسیج، محکوم کرد. هر یک از آن‌ها به پرداخت سهم مساوی از دیه کامل یک انسان و پنج سال حبس محکوم شده‌اند.
طبق گزارش هرانا، نوید نجاران، حسین نعمتی و علیرضا برمرزپورناک، سه متهم دیگر این پرونده، به دلیل «فقدان مدارک دال بر وارد کردن ضربه به ناحیه مشخصی از بدن علی‌وردی» از اتهام مشارکت در قتل عمد تبرئه شدند.
این حکم ۱۵ بهمن سال گذشته صادر و سه‌شنبه ۲۹ اردیبهشت به وکلای این افراد ابلاغ شده است.
این شش شهروند معترض در آبان ۱۴۰۳ از سوی همین شعبه به اعدام محکوم شده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75567" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=Dn8bDgjJpgwshoNoRoO1mZf-haY9NlO5JzEsumtjTNnRyBNFN8oVYO30jXMn5NFwzHttGQZ0fS36Mt9HSYtnYMI4GL1EUN02ejIwH5OAQ9MjGAKoZ5TrNcHS2BzFIxx99GIkQhJ8bWy9RMgXVnqVUIy_JDI-QK6Qe3SRMl8esFBkulqIzBzcqL1LChJpuOiNKRNGuT6A1JBm6P-4yKO_B_osFuZzyN29BgCCEK9Ak02_bbJMwtlPULUnlYLQpKd_xqnOWu5p2fZBWxuvik_BZLbah6Rw33ayJO-RKRZY2RSmTIUhHFIqE1jtJDc9UBwiHb9h4RyGTWqKrgkSIEEgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=Dn8bDgjJpgwshoNoRoO1mZf-haY9NlO5JzEsumtjTNnRyBNFN8oVYO30jXMn5NFwzHttGQZ0fS36Mt9HSYtnYMI4GL1EUN02ejIwH5OAQ9MjGAKoZ5TrNcHS2BzFIxx99GIkQhJ8bWy9RMgXVnqVUIy_JDI-QK6Qe3SRMl8esFBkulqIzBzcqL1LChJpuOiNKRNGuT6A1JBm6P-4yKO_B_osFuZzyN29BgCCEK9Ak02_bbJMwtlPULUnlYLQpKd_xqnOWu5p2fZBWxuvik_BZLbah6Rw33ayJO-RKRZY2RSmTIUhHFIqE1jtJDc9UBwiHb9h4RyGTWqKrgkSIEEgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین هم به خدمت شی رسید.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75566" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ocx4P6eRwq-5Z2HSKaDA-jY1D8uEr2axxJAUQncU4m99MbiSsJT7Lpv_tRJeLOSdIdFkn5iauBx614QrW2V_hrriomdqE3hCBU-zUN6TUZxZmzObisPM6Ny2cefvLVudiCqXYrIiYQfJH7cLhzW6qvrj_NIxiMeVEMwxy7rBC_39f_eEvqBjVtOXbjmYPmrtssRKTZI0FaDrAPbtG4DINgFrVRzBvVV0_grvmzrc1v3QlgJa1NU3HI-h54ecXc5n4a1H5T8Emk5aux6tZBB60bjN6LIbgx-57W8YSgujTSMfT5MjWaoqbIDYSJjgUL4kj1vPQoLi-E-rS0YQwyWplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین
تیتر نیویورک‌تایمز: هدف اولیه جنگ، روی کار آوردن رئیس‌جمهور تندروی پیشین به عنوان رهبر ایران بود
بخش‌های خبری مطلب:
به گفته مقامات آمریکایی، حمله اسرائیل که با هدف آزادی محمود احمدی‌نژاد از حبس خانگی در تهران طراحی شده بود، بخشی از تلاش‌ها برای تغییر رژیم و به قدرت رساندن او بود.
چند روز پس از آنکه حملات اسرائیل در آغازین روزهای جنگ، رهبر ایران و سایر مقامات ارشد را به قتل رساند، پرزیدنت ترامپ علناً اظهار داشت که بهتر است «شخصی از درون» ایران کنترل کشور را به دست بگیرد.
اکنون مشخص شده است که ایالات متحده و اسرائیل با در نظر داشتن شخصیتی خاص و بسیار غافلگیرکننده وارد این درگیری شدند: محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران که به دلیل دیدگاه‌های تندرو، ضداسرائیلی و ضدآمریکایی‌اش شناخته می‌شود.
اما بر اساس گفته‌های مقامات آمریکاییِ مطلع از این موضوع، این طرح جسورانه که توسط اسرائیلی‌ها تدوین شده بود و با آقای احمدی‌نژاد نیز درباره آن مشورت شده بود، به سرعت با شکست مواجه شد.
مقامات آمریکایی و یکی از نزدیکان آقای احمدی‌نژاد اعلام کردند که او در روز اول جنگ بر اثر حمله اسرائیل به خانه‌اش در تهران - که برای رهایی او از حصر خانگی طراحی شده بود - مجروح شد. آن‌ها گفتند که او از این حمله جان سالم به در برد، اما پس از این خطر جانی، نسبت به طرح تغییر رژیم دلسرد و ناامید شد.
او از آن زمان تاکنون در انظار عمومی دیده نشده است و مکان و وضعیت فعلی او نامشخص است.
...
اینکه آقای احمدی‌نژاد چگونه برای مشارکت در این طرح به کار گرفته شد، هنوز در هاله‌ای از ابهام قرار دارد.
...
سخنگوی موساد، سازمان اطلاعات خارجی اسرائیل، از اظهارنظر در این باره خودداری کرد.
...
مقامات آمریکایی گفتند که این حمله - که توسط نیروی هوایی اسرائیل انجام شد - به منظور کشتن نگهبانان مراقب آقای احمدی‌نژاد و به عنوان بخشی از طرحی برای رهایی او از حبس خانگی صورت گرفت.
این حمله آسیب چندانی به خانه آقای احمدی‌نژاد که در انتهای یک کوچه بن‌بست قرار داشت، وارد نکرد. اما پاسگاه امنیتی در ورودی کوچه مورد اصابت قرار گرفت. تصاویر ماهواره‌ای نشان می‌دهد که آن ساختمان ویران شده است.
در روزهای پس از آن، خبرگزاری‌های رسمی روشن کردند که او جان سالم به در برده است، اما «محافظان» او - که در واقع اعضای سپاه پاسداران انقلاب اسلامی بودند و همزمان وظیفه محافظت و نگهداری او در حبس خانگی را بر عهده داشتند - کشته شده‌اند.
مقاله‌ای در نشریه آتلانتیک در ماه مارس، با استناد به منابع ناشناس نزدیک به آقای احمدی‌نژاد، نوشت که رئیس‌جمهور پیشین پس از حمله به خانه‌اش از حصر دولتی آزاد شده است؛ این مقاله آن رویداد را «در عمل یک عملیات فرار از زندان» توصیف کرد.
پس از انتشار آن مقاله، یکی از نزدیکان آقای احمدی‌نژاد در گفتگو با نیویورک تایمز تأیید کرد که آقای احمدی‌نژاد این حمله را به عنوان تلاشی برای آزادی خود تلقی کرده است. این فرد مطلع گفت که آمریکایی‌ها آقای احمدی‌نژاد را شخصی می‌دانستند که می‌تواند ایران را رهبری کند و توانایی مدیریت «وضعیت سیاسی، اجتماعی و نظامی ایران» را دارد.
این فرد مطلع اظهار داشت که آقای احمدی‌نژاد می‌توانست در آینده نزدیک «نقش بسیار مهمی» در ایران ایفا کند و اشاره کرد که ایالات متحده او را شبیه به دلسی رودریگز می‌دید؛ کسی که پس از دستگیری آقای مادورو توسط نیروهای آمریکایی در ونزوئلا قدرت را به دست گرفت و از آن زمان همکاری نزدیکی با دولت ترامپ داشته است.
...
در چند سال گذشته آقای احمدی‌نژاد سفرهایی به خارج از ایران داشته است که به گمانه‌زنی‌ها دامن زده است.
به گزارش مجله نیولاینز، او در سال ۲۰۲۳ به گواتمالا و در سال‌های ۲۰۲۴ و ۲۰۲۵ به مجارستان سفر کرد. هر دو کشور روابط نزدیکی با اسرائیل دارند.
ویکتور اوربان، نخست‌وزیر مجارستان در آن زمان، روابط نزدیکی با آقای نتانیاهو دارد. در طول این سفرها به مجارستان، آقای احمدی‌نژاد در دانشگاهی مرتبط با آقای اوربان سخنرانی کرد.
او تنها چند روز قبل از آغاز حملات اسرائیل به ایران در ژوئن گذشته از بوداپست بازگشت. زمانی که آن جنگ درگرفت، او حضور علنی کمرنگی داشت و تنها چند بیانیه در شبکه‌های اجتماعی منتشر کرد. سکوت نسبی او در مورد جنگ با کشوری که آقای احمدی‌نژاد مدت‌ها آن را دشمن اصلی ایران می‌دانست، مورد توجه بسیاری در شبکه‌های اجتماعی ایران قرار گرفت.
...
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75565" target="_blank">📅 06:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RngJ9ut3EUmNoxoEXPxvOsImQu1TbALJ2OaU5HeQTWGCrkQjiymx_sTkFaQTJWUJ2XEsNvsdnT7RclUmfWD311Pn2iUDfBsm1nAheuWWUlUIL0birpRbPE4-vmnOVUJ3EoWg1sfCgsocCWIofRIQeTvXbULX8yDs0rgGR2fsZp86e5bHw88JGt1qcMeRKU4rWyo69P37WZDPoMcBdJAtf8N2IVG4tqL039_8RqrwYAZbv8SnCz9PoraDvqh1-Jsq_jtClN5_2LAUCSLmCSrUNtiHy1nHYE_aZsZAkfZlvzW9ch_K7q03x0wYQBLnh6ZGj_JYLGI1j6_nBU_kl-Pz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در یک سخنرانی در کاخ سفید گفت  ایران قرار نیست به سلاح هسته‌ای دست پیدا کند. نمی‌توانند سلاح هسته‌ای داشته باشند. ما نمی‌توانیم چنین چیزی را تحمل کنیم و آن را تحمل نخواهیم کرد.
او گفت ما نیروی دریایی آن‌ها را نابود کردیم. نیروی هوایی آنها از بین رفته است. سامانه‌های پدافند هوایی آنها از بین رفته است. تمام تجهیزاتی که برای جنگ استفاده می‌کردند از بین رفته است. تقریبا همه چیز از بین رفته است.
ترامپ افزود: نمی‌خواهم بگویم رهبران آنها از بین رفته‌اند، چون بیان آن چندان خوشایند نیست، اما واقعیت همین است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75564" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tC0UPzcHlfTzK58PkGj2ICQgMorrljhUGn56ONJDnALQvSY5biW5Akldrn4EV3L9i2W0ndC0bkej7nTEFluIxfHrgR1Dha5H8jlqq7p-R-22kSV-S_gp4L-36p_4CO6tvn6w8zQUkZsaUdOrNThEvp95JMB8-yppT57a5zCDkbPEfGOpaeFttYqZPxuFmemW_N6PXsvNbj_-Rec0s5fKo4nW-bYAllVmnS4gxmJrgdoPfEqjWe1EYEffPQcOW0JnMDvRgXmLjzOSu5YMN62T51Tv0TsDphNxg5MXYEnfY87Je_FdGoixi7W3XP6vj4G2lI0iuEZCuM2g_re_BQcqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه در قشم
آپدیت:‌
تصویر بالا:
#زلزله
به بزرگی ۴٫۷ در عمق ۲۰ کیلومتری بندر لافت در جزیره قشم هرمزگان
پیام‌های دریافتی:
سلام وحید دو زلزله شدید بندرعباس رو لرزاند
ساعت ۳:۱۱ دقیقه بندرعباس زلزله اومد
همین الان ساعت ۳:۱۲ دوبار به مدت ۱۵ ثانیه وحشتناک بندرعباس لرزید
من بندرعباس هستم دو بار لرزید
زلزله اومده خیلی بد بود
زمین لرزه نسبتا شدید ساعت ٣:١٠ بامداد بندرعباس
بندرعباس هستم فکر کردیم باز زدن دقیقا ۲۰ ثانیه همه جا میلرزید
چند دقیقه پیش زمین لرزه نسبتا شدید اومد دوبار تو فاصله خیلی کم بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75563" target="_blank">📅 03:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSAWkvNSTil7CEOGTb23xG4AFo3CWH_G_hIaCU9EoekueEveA4fs_vLraDLXgVjPH-nGDEOFuBJYGh7Mt5j0YpTpRFqleh2lQnKovi5I56-hZp9yUgjGvp0IwyMXjf0W1UvIOtxkJ6HFXYQpqwPbMdJW83SZj-SOr2axyhVqr0g3IbIZUjfrI_KGt4eaDBxkv0aG9Vq4hSq3oknUMbKBCfvkVYv5I9YCTeduwMOgNfVy0G6DnC-_JBA6Cmx2hRyB61CJ_kaiotMJwdipz_bDNQo3t2OtheywdrkuS2XyoQlyyFsihse2qhZT6YubmSVWMrXO4QXJa-4ak_yJpBeEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا روز سه‌شنبه قطعنامه‌ای را برای توقف اقدام نظامی در ایران پیش برد.
پیش بردن این قطعنامه پس از آن صورت گرفت که سناتور جمهوری‌خواه، بیل کسیدی از لوئیزیانا، به آن رای مثبت داد. کسیدی چند روز پیش، در رقابت‌های درون حزبی ایالتی برای ادامه حضورش در سنا، به نامزدی که از حمایت ترامپ برخوردار بود، باخت.
به گزارش سی‌ان‌بی‌سی، با وجود اینکه قطعنامه اختیارات جنگی با نتیجه ۵۰ به ۴۷ به تصویب رسید، اما هنوز احتمال کمی برای تبدیل شدن به قانون دارد. این قطعنامه باید ابتدا در سنا به تصویب نهایی برسد، سپس مجلس نمایندگان به رای بدهد و سپس نیز، دونالد ترامپ به احتمال قریب به یقین، آن را وتو خواهد کرد.
@
VahidHeadline
چهار جمهوری‌خواه هم‌حزبی ترامپ همراه با همه دموکرات‌ها به جز یک نفر، به آن رای مثبت دادند. سه سناتور جمهوری‌خواه نیز در رای‌گیری غایب بودند.
باوجود تصویب این آیین‌نامه، حتی اگر قطعنامه‌ای در سنا با ۱۰۰ عضو هم به تایید برسد، کار دشواری در مجلس نمایندگان خواهد داشت که تحت کنترل جمهوری‌خواهان است و پس از آن نیز باید دو‌سوم رای کنگره و سنا را داشته باشد تا بتواند گزینه وتوی احتمالی رئیس‌جمهور را دور بزند.
طبق قانون اختیارات جنگی آمریکا مصوب ۱۹۷۳ که در واکنش به جنگ ویتنام تصویب شد، رئیس‌جمهور آمریکا تنها ۶۰ روز می‌تواند بدون مجوز کنگره عملیات نظامی انجام دهد و پس از آن باید یا جنگ را متوقف کند، یا از کنگره مجوز بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75562" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eG1kpzObxTAajgR61cAxigrIHXv6wobwF0bpuLQjEH0SxU4gRAHEYhqcVO-uqv2XuhwjwVs67fjdHWuSTuZCwAuSJ2zAaTA2wNi_FLLAI5vpJhFiMJv5jEG3j97Gprc6QUA0iTnazawl_nbhmt9RttR7TRIzwajhYdzyagOWA0S8ulBP3la3NufwKJhj71jsEO9liDtkT7HbDMTt8G_3ZsC36nQfwh5JUxZijdf7xEQdrU1voIwFoEK-W2RKz5cursuLD93Lx_NU-FfHX7pki3IHGBoW8DYdoNQQ4sRoGjdq5HC3MmU2PsQf8fk14T8BqTeVi8W2p8JU3sFAvrvqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mz9oVA6dvEFIzZzCA__OCwkP9GyJviun2dQovY-M0o3hZVwmzql96o9smoEbjnaTKFxTXuf3xKllqqCtshx3d4BYjBL2Ig8mURZj40lhJF5Xqg7ilLGfj587-Pjm_le8SThve4EHSUbZs0fJhJl7UvytlFSNF-3iLvtX5iJSht89k4uVzCTk7KuDbIJubDZcTPrbJUfy7wctUumP5hWPg1YvqsgkG1uVJ1wh1aIM2K9WWsVwbs6vDz64TzDIVeUKqrJ_mbR0tq2L0GTv3N0o2_TxXu5_frIf7I-N2D8MPnPXltKtWZp-Q5ehCo2ijFqPWIW1LHRm4364gb97dKhlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OnaVVGpu4dlo2xhnRaQe15qbk2zXHDHeUrEdsL9Bhmb9G2lnNjev4nLVmX-0pxfyuHQyHKpJMOj9SxnddMH6xa6mzvL_bcTeFvXfTrlU8BIJjMKzlgwzRyF99rOhdAmEaC3O_yIMkBWQwagm3fPacy3K4pntKDNIDbg-PyFdzkUghwP-A2wL6oDhEFLT5a7CMgar4gwuIAdpLr2wcUFlErdZ4q309r9eadmVlEvwGcFRJkQ5yhcg8O0fg4xw43-eEjWd8IW2RVMCYJinJJIY4XD_Kdbj3DORlynIum1iUV3PzO6Awrcfxrpe0_PbeeJogI4941XagNiME2D25FMZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nrBRtj82oKzjTeLoZZsL5WZ4gkmL7A0mQINZR7tpLdnw72njNbRKg4SmXOMYyiL85sn4z63dggH0GbgJwcNZkWAygb1LomhsPP9TKoEO9pNo7A-qJewCojHRuNPj4z3MGvGCUGL8JAotvMBiiMchUxz1piGt3qfaTAT9XWpa0Uav0vPjZMmLPjbj2ArIf7A5XGbAVCdOXkc6YzctZG2swUhaA7aHopeHf0MTTWXJyCsRNzbBxfIHk_VoBbMKL9uswOa6ArJyY4_ZmidlwNyXESGm5HpAdVjfVCgcPCnAjFU2x6bGEJmwn985-LJOQLH0KxWTmVzhMlInJIp27w_3mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=P17PqA1avwNpLxHpqIsfq80NAbLXaSEbY2LJ-7LgqKyzIgBjScKTBJtzPM8QXL8DNza0zuhsCD2TcdP2QK0ZqyfZUKPlrq4fMMmya2yN7UXn0dOcEcpvbopYPqU1tzDAEw5wNcB8dxmdVwRvIIp0Ui6bVHGTCse-YmdUxGGmxBC7oqavoRBkuvCQDWPUwLzU4USttBzLRix-cAaJEtbO89Ki_rHqPx6bhNVVBz4jQbPhBe8WjrnarMbjS8QnJk0OAUHAKMZvSoAXG7aoidboK7Y7IfsEWrPD5v4azO88d-xWv9LdpuoPOF2Ki4GbiFw8r_z0tj8xioNRC0fKltoaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=P17PqA1avwNpLxHpqIsfq80NAbLXaSEbY2LJ-7LgqKyzIgBjScKTBJtzPM8QXL8DNza0zuhsCD2TcdP2QK0ZqyfZUKPlrq4fMMmya2yN7UXn0dOcEcpvbopYPqU1tzDAEw5wNcB8dxmdVwRvIIp0Ui6bVHGTCse-YmdUxGGmxBC7oqavoRBkuvCQDWPUwLzU4USttBzLRix-cAaJEtbO89Ki_rHqPx6bhNVVBz4jQbPhBe8WjrnarMbjS8QnJk0OAUHAKMZvSoAXG7aoidboK7Y7IfsEWrPD5v4azO88d-xWv9LdpuoPOF2Ki4GbiFw8r_z0tj8xioNRC0fKltoaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهور آمریکا، گفت واشینگتن و تهران پیشرفت زیادی در گفت‌وگوهای خود داشته‌اند و هیچ‌یک از دو طرف خواهان ازسرگیری کارزار نظامی نیستند.
ونس افزود: «ما فکر می‌کنیم پیشرفت زیادی داشته‌ایم. تصور می‌کنیم مقام‌های تهران نیز می‌خواهند به توافق برسند.»
او گفت آمریکا می‌تواند کارزار نظامی را از سر بگیرد، اما «این چیزی نیست که ترامپ یا ایران می‌خواهند.»
ونس همچنین گفت: «فکر می‌کنم جمهوری اسلامی می‌خواهد توافق کند، اما تا زمانی که توافق امضا نشود، نخواهیم دانست.»
@
VahidOOnLine
جی‌دی ونس اعلام کرد که دولت ترامپ برای دستیابی به توافقی جهت پایان دادن به جنگ تلاش می‌کند، اما او همچنان شاهد وجود شکاف و گسست در میان سران ایران است و موضع مذاکراتی تهران شفاف نیست.
معاون رییس‌جمهور آمریکا گفت: «خودِ ایرانی‌ها هم دقیقا مطمئن نیستند که می‌خواهند در چه مسیری حرکت کنند؛ آن‌ها در حال حاضر کشوری چندپارچه و دارای شکاف هستند.»
او در ادامه افزود: «در ساختار حاکمیتی این کشور، رهبر وجود دارد و در رده‌های پایین‌تر از او نیز مقامات زیادی هستند که بر روند مذاکرات نفوذ دارند. به همین دلیل، گاهی اوقات اصلا مشخص نیست که موضع واقعی تیم مذاکره‌کننده چیست.»
ونس  با اشاره به اینکه هنوز روشن نیست این تشتت آرا ناشی از ضعف در هماهنگی است یا سوءنیت، تاکید کرد که نتیجه این وضعیت، ایجاد فرآیندی مبهم و سردرگم‌کننده بوده است. ونس در پایان گفت: «با اطمینان می‌گویم که گاهی درک این نکته که ایرانی‌ها دقیقا می‌خواهند از این مذاکرات به چه هدفی دست یابند، بسیار دشوار است.»
@
VahidOOnLine
جی‌دی ونس گفت اعضای تیم مذاکره‌کننده جمهوری اسلامی برخی ویژگی‌های ایرانیان، از جمله «هوش و سختکوشی» را دارند، اما همزمان مواضع «بسیار تندروانه» نیز در میان آن‌ها دیده می‌شود.
معاون رئیس‌جمهوری آمریکا با توصیف ایران به‌عنوان «تمدنی بزرگ و پرافتخار» گفت مردم ایران «شگفت‌انگیز» هستند و جامعه ایرانی-آمریکایی در ایالات متحده نیز نمونه‌ای از این ویژگی‌ها را نشان می‌دهد.
او در عین حال افزود گاهی مشخص نیست تهران دقیقا چه هدفی را از مذاکرات دنبال می‌کند و ساختار تصمیم‌گیری در جمهوری اسلامی را «چندپاره» توصیف کرد.
ونس همچنین بار دیگر تاکید کرد واشنگتن اجازه نخواهد داد جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند و هدف مذاکرات، جلوگیری بلندمدت از بازسازی توان هسته‌ای جمهوری اسلامی است.
@
VahidOOnLine
جی‌دی ونس اعلام کرد: «فکر می‌کنم ما در حال حاضر فرصتی داریم تا رابطه‌ای را که طی ۴۷ سال گذشته بین ایران و ایالات متحده وجود داشته است، بازتنظیم کنیم.»
معاون رئیس‌جمهوری آمریکا که در نبود کارولین لویت، سخنگوی کاخ سفید، مسئولیت نشست خبری روزانه را بر عهده داشت، در ادامه افزود: «این همان چیزی است که رئیس‌جمهوری از ما خواسته و ما به تلاش در این مسیر ادامه خواهیم داد. اما برای این کار، همراهی هر دو طرف لازم است (یک دست صدا ندارد).»
ونس با تبیین خطوط قرمز واشنگتن تاکید کرد: «ما به توافقی که به ایرانی‌ها اجازه دسترسی به سلاح هسته‌ای را بدهد، تن نخواهیم داد. بنابراین، همان‌طور که رئیس‌جمهوری ترامپ به من گفت، ما در حالت آماده‌باش کامل نظامی هستیم. ما تمایلی به پیمودن این مسیر [از سرگیری جنگ] نداریم، اما اگر مجبور شویم، رئیس‌جمهوری آمادگی و توانایی پیشبرد آن را دارد.»
@
VahidOOnLine
ونس افزود که به‌تازگی با آقای ترامپ صحبت کرده و رئیس‌جمهور آمریکا تأکید کرده است که مسئله اصلی برای آمریکا این است که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند.
ونس یادآوری کرد که اگر چنین اتفاقی بیفتد، کشورهای حاشیه خلیج فارس نیز به‌دنبال سلاح هسته‌ای خواهند رفت و سپس کشورهای دیگر جهان هم همین مسیر را دنبال خواهند کرد.
او گفت: «ما می‌خواهیم تعداد کشورهایی که سلاح هسته‌ای دارند محدود باقی بماند، و به همین دلیل ایران نمی‌تواند سلاح هسته‌ای داشته باشد.»
وقتی از ونس پرسیده شد که آیا ممکن است روسیه مالکیت اورانیوم غنی‌شده ایران را در اختیار بگیرد، او پاسخ داد: «این در حال حاضر برنامه دولت ایالات متحده نیست. ایرانی‌ها هم چنین موضوعی را مطرح نکرده‌اند.»
@
VahidHeadline
جی‌دی ونس همچنین گفت واشینگتن می‌خواهد جمهوری اسلامی فرایندی را بپذیرد که تضمین کند ایران حتی سال‌ها بعد از دوران ریاست‌جمهوری ترامپ هم نتواند توان هسته‌ای خود را بازسازی کند.
او گفت: «ما می‌خواهیم نه فقط تعهد به عدم دستیابی به سلاح هسته‌ای را ببینیم، بلکه می‌خواهیم تعهدی برای همکاری در یک فرایند ببینیم تا اطمینان حاصل شود که نه فقط اکنون، نه فقط وقتی دونالد ترامپ رئیس‌جمهور است، بلکه سال‌ها بعد هم ایرانی‌ها به دنبال بازسازی توان هسته‌ای خود نباشند.»
او افزود: «این چیزی است که ما در مذاکرات در تلاش برای رسیدن به آن هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=PvyKdWOETAkq1u1WQ36MGC8cJFUeCSvIe2uvwsGSXi4C5eIiBPL9lG8C1Ou5r3pTc3B1jI2fWIX_77bt_pwA-PBqHu4PVz3cMPzrF5-T7bdG8eqhpY7uUFFHZOf6AzAmR6th95YjM8s9w9Ite8l7Onm9KrT7-7BUnlV9zgG812F74qNF3HUTIe9ROQcDLSNpzPjdWq1ezcIMK_ydnRraDAR39v-3-Y3mJRlYxBLitmYx4TaJ7xtasce46jIGLWODHzt1MdWCUvSI6X4UHNfGr-WYA4_oNdcO-byjqAHp2Who-CYp_kEy0K1eIrZCQmzfkrRkc_NRO2E5WUL3_7LIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=PvyKdWOETAkq1u1WQ36MGC8cJFUeCSvIe2uvwsGSXi4C5eIiBPL9lG8C1Ou5r3pTc3B1jI2fWIX_77bt_pwA-PBqHu4PVz3cMPzrF5-T7bdG8eqhpY7uUFFHZOf6AzAmR6th95YjM8s9w9Ite8l7Onm9KrT7-7BUnlV9zgG812F74qNF3HUTIe9ROQcDLSNpzPjdWq1ezcIMK_ydnRraDAR39v-3-Y3mJRlYxBLitmYx4TaJ7xtasce46jIGLWODHzt1MdWCUvSI6X4UHNfGr-WYA4_oNdcO-byjqAHp2Who-CYp_kEy0K1eIrZCQmzfkrRkc_NRO2E5WUL3_7LIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا سه‌شنبه به خبرنگاران در کاخ سفید گفت ممکن است مجبور شویم دوباره به  ایران ضربه بزنیم، مطمئن نیستم.
او گفت منظورم این است که دو یا سه روز، شاید جمعه، شنبه، یکشنبه، چیزی در این حدود، شاید اوایل هفته آینده؛ یک بازه زمانی محدود، چون نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای جدید داشته باشند.
رییس‌جمهور آمریکا ادامه داد که او دوشنبه تنها یک ساعت با تصمیم‌گیری برای انجام یک حمله فاصله داشت، اما این حمله را به تعویق انداخت.
او افزود جمهوری اسلامی برای رسیدن به توافق التماس می‌کند.
ترامپ درباره جنگ گفت: «همه به من می‌گویند این کار محبوب نیست، اما من فکر می‌کنم خیلی محبوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=ptLHog0lJPlStEnEU8QCNjHXkoBIYKgf8NexRA3MrbubRf0lv5xjr8H3WYAQzbj2x59Cr29noS12OQ_ifAUSf8X9ZQ4trorFDGtqjp1Z4uGz6bSTQV7XtOweDSIZxnbp5FDc2pX8b_uqfrTSEHD840FOtfnzLfFWg7h82yQ4Lv6EGNDmfScY1ICVGa3zJ-TKUTdFrHBb_pJ_B4uvBi4VPezGzYa0cELz6DGoxDaV7NgYH4Ed59r5d2I3k6RixSZo0RBSwV1vMiPWFwjq6yoYvdEaAn69RioUO79T9tMzJqI0DJRiILmhG5SdF1G0Pp2wYeA-XnCBjUG_lis3g-G3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=ptLHog0lJPlStEnEU8QCNjHXkoBIYKgf8NexRA3MrbubRf0lv5xjr8H3WYAQzbj2x59Cr29noS12OQ_ifAUSf8X9ZQ4trorFDGtqjp1Z4uGz6bSTQV7XtOweDSIZxnbp5FDc2pX8b_uqfrTSEHD840FOtfnzLfFWg7h82yQ4Lv6EGNDmfScY1ICVGa3zJ-TKUTdFrHBb_pJ_B4uvBi4VPezGzYa0cELz6DGoxDaV7NgYH4Ed59r5d2I3k6RixSZo0RBSwV1vMiPWFwjq6yoYvdEaAn69RioUO79T9tMzJqI0DJRiILmhG5SdF1G0Pp2wYeA-XnCBjUG_lis3g-G3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی کارزار ایران‌اینترنشنال برای یافتن هویت پیکر جاویدنامان در بیمارستان الغدیر تهران، ویدیویی از لحظه قتل جاویدنام آیدا عقیلی به دست ما رسیده است.
آیدا عقیلی، ۳۴ ساله، شامگاه ۱۸ دی ۱۴۰۴ در شرق تهران با شلیک دو گلوله ماموران به سرش کشته شد که پیکر او را پیچیده در پتویی چهارخانه در حیاط پشتی بیمارستان الغدیر یافتند.
@
VahidOOnLine
مربوط به این تصاویر تکان‌دهنده: @
VahidOnline
این ویدیوی دلخراش: @
VahidOnline
اعتراض‌های چهارشنبه ۱۷ دی:@
VahidOnline
#بیمارستان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ekrEvpO1abVl5Zgwx_dSNYrQ5cFM7ps451mNsWuRca2QIRlQGcSOTKxaAPTiljpe58CyeD9SjbU6ipHTZP0rdCozqDuF44v0yJi46hVdxMKs8xhSVwnEaMQHT6tIypyVkBCo_S4acG_3pzwoz7yRhckSk0ygYjVV_NgTi9W1ZeitjAvhykgMN-0MsLMZhQIrh2RirMg77CdU4RVem-B7Ooa1r5ZIdddcV4ejUEKTnzwjv_FiSgIS3fhx1YpkRORqvvj2T1SoOck6GvfiEZHh3iPjCo1L62UfdVOGHH7_uUiBuAUNMi09A4t8EW7dQFJJJl3jbgI5pIowcZR1Oq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-cB_wZ9C5rFvB8gnqX_gyU_ytxBT2MXR3i6youVNa12aFfyDYSmC-_it_hCVc88qP1KN-ZT4IvLVGmCbz5aaXBCWaNDf6cqsBGk5Wa7JY0wmcUoC2IeWaeUEU-AxIE3zUQbVXKtzE_e5hR37X9q1AIPRNVDBlL2bFZZNvxuWQUzL8I89wtRkVID8PhkFwoF6QPWJk3znptOnT5lO7UCOjDVyv8jUmuhUJs8Tt-T1qtYXbv6cx8wK1HLZnxeZrswGvKgn-qFXHbGXPmax9H9BmSON559KtGchwwSC6qtT3i22ZXOOuCZYsNeLVaHNESgoPr8yIgYyn3EGOGefusMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
+ بحث‌هایی دیگر:
twitter
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td0nYlZEJtsGayGvJ3LhOPCxSpcrRj0DWiRhw6PLpiXIu63nPXUZ-GqTEnCvNDuGthR5wiT2DOFEsc4FKxu0u6EcylbEXMxgdRrO0zmmJJF5sBda1ZEtV6GKjchpuv7-InhDRNZ36CfrIr9xQP6XjqlhDWU5mVKd4OvwO1bt8RbexEE21xELLbfeKI7isI9fyYVTAP1KJW06jQO01KWvRMaactalOsykkqdffMSmEtchZS_trqLRWhwcOIOaZ_-8gqjMRK_eacN1D4htHGA2siS0VOH0rT6UL2-ffIutmBfpWOyEQpk4mLKr492pqSs78RPyGPX4zWy6YeyGhPj9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1K0VwpCq3y7es-wsrct0gLdH_YhBiRjXV-J6UzC70E1r_rXws1z-Ra0XA10Ni3qK7xxaaQPaQQV5CYLf_WVHElY5RxUIVA4fD1qpAEdBFXcHEFZ9wu_41B2BOgr7QEuamxNXtjXC1rY9Hov6suufeN2ablcN3ZyX5yvmIx0xwC348LDSGoIQGjaIs8nrelWKv4k6EvmEVxj1UVlFZi_3c0LB-1XD4uNeWkOgOxR0vHN65ED4NorsOzsterWMuf5lQ-QcS45chANBEJLfEY3Jxyu5f-hiwT34Zb7aknldj67yy-E28fA53qsDlTqk-DxUfVVWTmbf5En3LblyRaWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIqZbwoTP06SDKe6IyWj0S4RQFzkXKc8nE2cv9huQLz1TbStF9yclbPCY9rtWrLmFie5xBX3C06vzS1sRX9U7TWgV2iVjVMbSEEbQIlgECQhk9fbvk4O4-DXTA782k9B4-2nXccTDLsbBVBH5Ve0wnTm98qpvfNBXn1bj8h-REjZeW-_9j0WFzyGAhIrXDV1tL1z5vEA_0zCG04qPGkX8WavZ4dFQkQ8zHuBqWDIxVHYzNeZlmNJbxOc5eiLXQg4_4dDP_dN-njaX9lAMvtnhCPuuf2FbNQcgTkYPA13iLtT9cDR-RhFonaLSfd6pr5PIjO41hloqQF2o70MWGHgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8iAN4QkAwPt-EIHsb6gI8UfQZ_VVnQ26iGTWLGexxptUeljVUf_-Zd9au-MV0kte7Lo8SmFnvBQqPByFHaopdYEm0w0aXBaP3hR2b7hnxDfp4mPEQojdwkfmfu4Blt1gLC0eyPQL6cyl3EG9UiAAN_f25rKXrK9TM_AIaMMAxctw28gY1H6uMhNxMNkUKSnAluaVduHbHWM7L1jOLRcHoNAN72JEhrfBrUfreQp9HwH5fzpKcAYhuEzSVMEf7HOO-cBxWUAB19Jd70zVEBuSW1Dg8ivR4GU4VwblpuWnLEDkvTbxCq8CNtBnA9_0EZEzlHR9mBvZM9Q1_EruGoCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/olmjmuPVIP2m0T1nHtXJhZJZR8yUCGUs_YOvYO5f1dK6nerARkQWkwCJw2uSx8KAr2tFAYOEzAEMR5kdtd-dRWHGCksEzGqEwgH6Z_Tqgg2wg6JkBefNAFOJAkierUGNo25nZ1j-0z6JWZ1BlNdFNJc8cVTKn4-A-T3aHcaMiSP_-JV67OSr59hTbci-EqUv3czkQXd_skS1L2f7eJAtN-Tyh8vQ293X2DYUUTv8qbcVk0wuAjDKTEK5hCECRqYUhrhTBQvCRSC2oYCjeR5n4DyIkuKqq45Rwdk19X7Xwn-NY0I77D0Fa_Kg87EzVmf6O_q4VTsxbYh0D6Rd9LfSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3F6qfM4cQwCH5OQBkydvH2HwltNiXtnQ3esDJBK1KlL1dlMd6XkM6N9DvnikVXIPp7WgeiQIW-U26YIQtCJCY_MoM1tX20b2zQIiQDuReOwGZ0Z15V5giaZlXzcxrjjluL6Ry30RkcfcUdRpXC3zswnoh33JQ2fslQMKMK1G7xxzb9SuXURyBudZRIyddexG0WK4u7vR1jkmDGmpzAO_K5oCxM5-uzs_6uzmnD2BSftE5pKgU3pA3OQV6y_0If0vipF2yHmhPwdLVX6KYOOu-p1UpL0WDTBIQxwy1EUDZv-iKT7ZZzz9TsK1K-eWLzb6trtYfvXyEnrlqMbriQBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله فردا را به تعویق انداختم
پست ترامپ ترجمه ماشین:
از سوی امیر قطر تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی  محمد بن سلمان آل سعود و رئیس امارات متحده عربی محمد بن زاید آل نهیان، از من خواسته شده است حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛
زیرا مذاکرات جدی اکنون در جریان است
و
به باور آن‌ها، به‌عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
این توافق، نکته مهمی را در بر خواهد داشت: هیچ سلاح هسته‌ای برای ایران!
بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دانیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده فردا به ایران را انجام ندهیم؛ اما همچنین به آن‌ها دستور داده‌ام که آماده باشند، در صورت حاصل نشدن یک توافق قابل قبول، در یک لحظه و بدون درنگ، حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/75545" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k1R_j1iMExamQ-iIOxBeL0EAVNByhGGD-HFn291To9B0iHJkv59yjc8wMjaO6J1lDEbMxTZ_bzNeNQhE_oGLbx31YcLVTCDwpXwCwgiuM8lL0XK2BX08StNY_3Wx3FZ7LfUxn3sYchHgFB6ixXTIge17Ehss9icAiLZXNtFjznPFzr1nLUTPo6aW_lE6iKce2GjC0gmF__bliuDcWxc170OKmjo7vv6G1X9kNfs-ERHIE3WGl56qn1XuWIOxsG547A_i7ylZeGfCCW-MUiMSNmJ6KmWKnt9SqytYnleVS5IEVEFxwlVX0sJl-gf6tGw-pbjoeBdpIOXX4gIPDfHQ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز دوشنبه در گفتگو با نیویورک پست اعلام کرد که پس از دریافت آخرین پاسخ ناامیدکننده تهران در مذاکرات توافق صلح، «به هیچ وجه حاضر به دادن امتیاز» به ایران نیست.
ترامپ در مصاحبه تلفنی کوتاه، ضمن ابراز نارضایتی از آخرین پیشنهاد تهران گفت ایران می‌داند «به‌زودی چه اتفاقی خواهد افتاد».
به گزارش نیویورک پست، وقتی از ترامپ درباره اظهارنظر روز جمعه‌اش مبنی بر اینکه مایل به پذیرش تعلیق ۲۰ ساله غنی‌سازی اورانیوم ایران است سوال شد، جواب داد: «در حال حاضر به هیچ وجه آماده دادن امتیاز نیستم».
ترامپ ادامه داد: «من واقعا نمی‌توانم در این مورد با شما صحبت کنم. چیزهای بسیار زیادی در حال رخ دادن است».
رئیس جمهوری آمریکا همچنین گفت از تهران «ناامید یا کلافه» نشده، اما هم‌زمان تأکید کرد ایران به‌خوبی آگاه است که ایالات متحده می‌تواند فشار بیشتری وارد کند.
ترامپ گفت: «می‌توانم به شما بگویم آن‌ها بیش از هر زمان دیگری خواستار توافق هستند، زیرا آن‌ها می‌دانند ما...به‌زودی چه اتفاقی قرار است بیفتد».
وقتی درباره ادعاهای منابع منطقه‌ای مبنی بر اینکه ایران تلاش می‌کند در قبال هر دو مسئله هسته‌ای و بازگشایی تنگه هرمز در برابر واشنگتن «سیاست صبر و انتظار» پیش بگیرد، سوال شد، ترامپ گفت «چنین چیزی نشنیده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75544" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gngBNF_BHyjVFyacI1EIIPjBKhqptRQ0nTCwKLt8bDwqrClu9r0QiS15qnRqpRztbYaZvNs4Oo3UwRmRlP0V_JZ4zkbtHzGRjc_07E1cuI95OT9aKWShnEH9APST4gq_1ZcPdZnXdXaj0Sbe_tlCbzXsPuCDHWghN1UO4hJs9HWnqdIV5kIHVQ7lZql-YKp8_yAJ-V-7wYrwdOJYDikX0pTu4k3LdEV7k1HOnXO65ZbvVtpeqh5UGERhupzvY37VrngY3x3g_lRO8mwnK4NM07vZwlNKfX-SC3NPMN0me9d0opLSsiw5nVBxZML3jSrOLH_28InAhThBLvLlAPEKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، دوشنبه گفت که آمریکا در حال صدور یک مجوز عمومی ۳۰ روزه برای فراهم کردن دسترسی موقت به آن بخش از نفت روسیه‌ است که در دریا سرگردان مانده است.
بسنت در شبکه ایکس نوشت: «این تمدید، انعطاف‌پذیری بیشتری فراهم خواهد کرد و ما با این کشورها همکاری خواهیم کرد تا در صورت نیاز، مجوزهای مشخص صادر کنیم.»
او افزود: «این مجوز عمومی به ثبات بازار فیزیکی نفت خام کمک خواهد کرد و اطمینان می‌دهد که نفت به آسیب‌پذیرترین کشورهای از نظر انرژی برسد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75543" target="_blank">📅 21:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lu98qJhUPufZwSfo6176GW22BPjHD0JDerih7IbuNDL-4hicRJRMi6F0uLkVs7CVwiKsq5m88Cj15d1q2nPw-_QA-DVfG0-t_y6h6v1oXl9gS2279bt3EbZWqr9VXLjZUERoAov78GN8Zs9rOdhPzaGLkRYxqdTYrDkSHHREIlGqc0n2xq9XeyBUglrywCRnJPh1jEa-uGui2RQNoVeuO04PzXnlXoWi4m0c2d6zlZTGRlHVHbLmmDra7Qct0LTz32zye7fr3PqdVTUVZriWtmlD8PrFd9JDXtBboCimlZYZio_tBqNfiZF42epbYHbneWAOtA4E3OyQ6rrwPYduKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fmpnM2KrIugDGbU94iSd7LwsEtubV8PB2MUswNy-BtLIgUgKOSRbbj0TDPm2PWuef_jKL51TpNvErNuQnt-zYtS-9YjpcYtrOSDBJS0J8tc5hfRhXhTyhE3DE4vCeKav1QZMJ3WWlqybINatfI--0HlpwADmKAvQakjafKxBy5CJOq3KWFmkn8ny-KczMJRAYnmNJ4XnRxM16kPlHAvtv0WxFK6Z8sayXVCDgPxxyUKl5W9-HH2qfPmKVsf-CCpsUzCgGTvX4sMSNKYkmAruD2Zc6CokVshTf2Y6_jB4XuFFvbLgRmWTiyQpkxZTT_J87FCE9pvlEXLu4gsZuFmelg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس، روز دوشنبه ۲۸ اردیبهشت ۱۴۰۵ به نقل از یک مقام ارشد آمریکایی و یک منبع آگاه گزارش داد که تهران پیشنهاد تازه‌ای برای توافق ارایه کرده، اما کاخ سفید آن را «پیشرفت معنادار» ندانسته و برای دستیابی به توافق کافی نمی‌داند.
به گفته مقام ارشد آمریکایی، اگر ایران موضع خود را تغییر ندهد، مذاکرات «از طریق بمب‌ها» ادامه خواهد یافت.
بر اساس  گزارش اکسیوس، مقام‌های آمریکایی می‌گویند دونالد ترامپ خواهان دستیابی به توافقی برای پایان جنگ است، اما هم‌زمان به دلیل رد بسیاری از خواسته‌های واشنگتن از سوی ایران و خودداری تهران از ارایه امتیازهای قابل‌توجه در برنامه هسته‌ای، گزینه ازسرگیری حملات را نیز بررسی می‌کند.
دو مقام آمریکایی گفته‌اند ترامپ قرار است روز سه‌شنبه نشست تیم ارشد امنیت ملی خود را در اتاق وضعیت کاخ سفید برگزار کند تا گزینه‌های نظامی را بررسی کند.
آکسیوس گزارش داده پیشنهاد تازه ایران که شامگاه یک‌شنبه از طریق میانجی‌گران پاکستانی به آمریکا منتقل شده، تنها تغییرات محدودی نسبت به نسخه قبلی دارد.
بر اساس این گزارش، در پیشنهاد جدید، توضیحات بیشتری درباره تعهد ایران به نساختن سلاح هسته‌ای آمده، اما هیچ تعهد مشخصی درباره توقف غنی‌سازی اورانیوم یا تحویل ذخایر اورانیوم با غنای بالا ارایه نشده است.
در حالی که رسانه‌های دولتی ایران گزارش داده بودند آمریکا در جریان مذاکرات با لغو برخی تحریم‌های نفتی موافقت کرده، مقام آمریکایی به آکسیوس گفته است هیچ کاهش تحریمی «رایگان» و بدون اقدام متقابل از سوی ایران انجام نخواهد شد.
این مقام آمریکایی همچنین گفته است: «ما واقعا پیشرفت زیادی نداشته‌ایم. اکنون در نقطه بسیار حساسی قرار داریم و فشار بر ایران است تا به شکل درستی پاسخ دهد.»
او افزوده است: «زمان آن رسیده که ایرانی‌ها امتیاز واقعی بدهند. ما به گفت‌وگوهای جدی، دقیق و جزیی درباره برنامه هسته‌ای نیاز داریم. اگر این اتفاق رخ ندهد، گفت‌وگو از طریق بمب‌ها انجام خواهد شد و این مایه تاسف است.»
در ادامه این گزارش آمده است که ایران و آمریکا هنوز مذاکرات مستقیم درباره جزییات توافق ندارند و گفت‌وگوها به‌صورت غیرمستقیم برای رسیدن به چارچوبی مشترک ادامه دارد.
این مقام آمریکایی مدعی شده که ارایه پیشنهاد تازه از سوی ایران، با وجود تغییرات اندک، نشان می‌دهد تهران نگران اقدام نظامی بیشتر آمریکا است.
در مقابل، مقام‌های ایرانی همواره تاکید کرده‌اند که این ترامپ است که برای دستیابی به توافق عجله دارد و زمان به سود ایران پیش می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75541" target="_blank">📅 20:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQRBwxQvjQrFeB9LtI5ZEPKC9hRGC9HbWsgBgsn3vOKc0e-wIIfQWHWR-Axu1mddhHeG_AZQpKvtIUXVSor9hVvdVlQ2Y9Jlh79ZGwqrLaKfy-5uSkZqIBokUpxtrzr7ZrNIMai592wJLZgv3iGxAL8I60CHZ7GgTXChSQav1XpWhwk9TYJh8eKGJB-5ctFtdz0IW8LkekanpsoV6AuisBEY-eu5nI-7sweHbui3HTwrbpkXC0nxWfj1SvKSHllng9SXsrAEQRp_qaczLXb98njUkxR65W9lstju26hUJSzG9GVAnRdJYVaYYROnJlG1dXFR7ZAnWwbPSCHZrj8keg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmcmA7L3KMkgQWEotQvhmodsm0Mk_YsyzYd1bg5zf8Ix9m7xzyZqhkqDTP9FKxX40qE_yANWsN3vgwwSbfXqNWCOdvUaEdSO2mOVJ4Dr5PyCaAnRQ8wL8Jzjl_iYIyPZ8q3X_R41IqzUu2Y3gkmdtgYoxaWDpZC2nOUCNzo4Ux7ZYobPbA4r6DIMNnTkMuD7AsgAkVMty-Adt48-ZcygDQP_okYHiILFTgEo9EGtH-yj_sHE-jJm2J5nDjWMjEh8PHyZikCc9yx6CEuYwRPNZ3vGzcp3n8_hC7lIC4CN93CHy9jsJqlDxb4der0TGNDBvr05yrxsPuJP9FLsYyJofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruyyg-zB7FyDx6u-T0CF8eitz2M9o6ZKk3hxsFXh8Qya9eneR06Wwj3SF3gSluUek-6ckDm8KngkFqQquO6HpkavbS14Isb5uoXKDc_jG9z4sF6EIyapeN5cmGMD1dQWKKkVf4f4l1IJkm0UGQ88WLK_-fFQQ8vNddbVbWlQIuwsovBI8siYXgQ7M1lv0Nesuf8JmfOKok4HV2xWkbEaktP_Sfh0N_pwHyyuu79mFyAT1y5TO1oH3peIKtgyUtSZUqei9wHzfN6YgweArR7WGeQzMPpCe1nPk9aZIkQOngFcJlVepq70_Sn6pfO4l6DoE2cQmqdT_6FY8XN7Yo8vUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sw4HQqezMr2jOw_JZrDvzuBWUL0UI97ZXmNwNbtJolw2qMyoYLd3VCQiv_tGWjOgGyxDJN9XEDpx6VbjmUJWNrLcUI-3Ree5JShAnJc8cPxkD2pGYVV6OEiqbSz0be7dtxtys6rVz9niE3z-x6G8ySlOMDMdqpev-Z55hf-lt3CpogGBgJ6WaFSjn8_lnrfZdZk56JXc8wttz1Y_pe_UO9uMrCKhHnfy4vOgEiN6qqzGz392e0d2VItwKdZ2uP9h1OSZ3I55JuzQn1dKDNZCIrM8b0OFTcMq25LcfEDFGclUSmJelgEnQXrBN7IoHVpwHP5i_dCwXLK6O4bQ-bMftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cd88qZNwac9za0ZUS73TxItwU5pr_Nsz9JphiL-NsQKn-6YtMJPy2oEqSs-MtULufPZFqR2HPYDNpP2_Zpwdx2L6jXy56fyvigv2g7X2kXvCs51holB6CyRAU-c9XJjtZWHGtIIMdKg0yLhaO4rRVO3hxU8j_KfLc-SDS6mVt5DJ15SMWG77pevfu12q0XXt762zeDG1AEZf69apPWPYzYCg9PBj5DM63q4XyVjOZPbDxlmPpmcUWa8tqwFGqzKi0LICJ58-K8DepZh2WSKvPAcobaWh7Lv8N-tzX6cpbdqo-V2MNNCWMzm3J7Y98ZsX9Uum7zUsTQ_URMhAxTw-2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت ماه به نقل از «یک منبع نزدیک به تیم مذاکره‌کننده» جمهوری اسلامی نوشت که تهران «جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.»
ساعتی پیش از انتشار این خبر رویترز به نقل از یک مقام پاکستانی گزارش کرده بود که اسلام‌آباد یکشنبه شب طرح پیشنهادی اصلاح‌شده جمهوری اسلامی ایران را به واشنگتن تحویل داده است.
@
VahidOOnLine
خبرگزاری العربیه، روز دوشنبه ۲۸ اردیبهشت ماه، بر اساس «جزئیات درزکرده» از آخرین نسخه پیشنهادی ایران به آمریکا، از مجموعه‌ای از خواسته‌ها و پیشنهادهای تازه تهران که بر آتش‌بس، تنگه هرمز و پرونده هسته‌ای تمرکز دارد، خبر داد.
طبق این گزارش، ایران خواستار یک آتش‌بس طولانی‌مدت و چندمرحله‌ای شده و همچنین درخواست کرده بازگشایی تنگه هرمز به‌صورت تدریجی و با تضمین‌های امنیتی انجام شود.
بر پایه این اطلاعات، تهران به‌جای برچیدن کامل برنامه هسته‌ای، با یک توقف طولانی‌مدت فعالیت‌های هسته‌ای موافقت کرده است. همچنین پیشنهاد شده انتقال ذخایر اورانیوم غنی‌شده به‌جای آمریکا، به‌صورت مشروط به روسیه انجام شود.
العربیه همچنین گزارش داده ایران از مطالبه دریافت غرامت عقب‌نشینی کرده، اما به‌جای آن خواستار تسهیلات و امتیازات اقتصادی شده است.
بر اساس این گزارش، ایران همچنین خواهان دریافت چندین تضمین بین‌المللی برای هرگونه توافق احتمالی است و تلاش دارد پرونده دریایی و موضوع تنگه هرمز را از پیچیدگی‌های مربوط به مذاکرات هسته‌ای جدا کند.
در بخش دیگری از این گزارش آمده است تهران خواستار نقش‌آفرینی پاکستان و عمان در مدیریت هرگونه تنش یا اصطکاک احتمالی در تنگه هرمز شده و همچنین بر استفاده از ادبیات و چارچوب سیاسی‌ای تاکید دارد که امکان «حفظ وجهه سیاسی جمهوری اسلامی» را فراهم کند
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1eT_DiAJdpEMcG8njPoIH4Z19mPOMBEaQLoHCEzsovjgm9LVttrREelCGQfMKc7P0LkjEoszbqx3bcK5dseEtO7ZEXaysDr_-Lm4Ca8I6VEGkLOEIXYp6uzbvm_YznZdoUlQ1Jx_ciGLCJW7_K-YKzAi96S_CyIylQnu4qtQvD-0QrwG0HGaHWIcuvwJ29_2o0apuhkfSk_W9lPYuZ8xZrfrXjMrTCINwr6xym5ej8Zq8sByOcuCyRMU9o06lrN8HtmeF5bAnosWHgjy9mlPdrJ5STz1sOMQZY_V6vRi4mETz3jc7toIMvjI8c0phRFUaT4sRhzo0Z5WLD-OA16lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS5gpAfu1EG4H_eujk56PCWaAXF9B8BRd2z4PugGOTzJox1sWiiq0wskMYp8wzbxzdZyoJn2ZqGItYHI_t_cCr9S6m6n9nSnR7kFerwfWonhJplGIPhw7pRDo3ZlslLRjs173mq9zabk4CvnXNpFgsKzuN7nzRXJ4I6NB9SrFUCsj-M8duO9zn74XjbjCTmXx0hSCY4NsnZbz2Qzcp0m9nXxYJXtvczoWtGiVjjPl6TibhrZL1hxdGW9ivVLmpEOF4vAUTSBVMHPcdb3t0gXB6urEKDMx9mISNa9a-JdQcw6jnojTkI9Sl1f54OjM2bNLL22xAUCT86ZO5Z0vAzDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgs75BFZhiaKqNOGp98C_qafw9XPv556034ET_ImpZQQ6sJdbDcITN4q6pWJbcl3cnByHoGpy2GwVJBSqvTDvDk6IQFFEHsVmDspamtf04on60sk_w7B28dSjvNZP1h-skM4S-fWvCjWDeZHoX7br-q1IYIEdNv3L4ynX0ABDsAQSTsJFTyamnl9zarPl7Q8ZXRb3EIasbhFqo5wC9HIin64McHJqxYTrF1C8F8-4NcTs_S9-QwdVU5B9ypCmXdHMMyZcn2UWM_TP1AtV8DtheAMv_I_syK5EBUu4vnUPKIPGPbjf1WBKlyrlgWE5if944K2T3uoJqCKeuv2D3A94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nME5r6Y4e3VAixy0DP3qCqINjzkMks8bnTk5NuIXco4pyucoehI1OHJh7_P2evE9C7VcM3C3Q_JGTDBkfHziFqHhucG8J_s1C7j89_6o78WDdGL9F40ZxFoQctdsfjCW-ezXUjz1dJdHp3yOgcuBCSbfOKw0x8whfeLYHNbKoGXzFXguwdNijGcqHwlB9vzA8NXj6ny0kWz0K1A7Zx6_IM0CDxCNJ-hdjrJi0e-bpnMN8jP7GOmlCzk7-1kJLj6mU45KjrZGbUcfyfilwYpMONXo0_FfrrHcNwyxAUlsfQyN5NVkaPZso0RQ2qNRayllZFZky7M_j18IAi_9VD_rag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OpXs5AJmaW82XaInKDAh7cXDXZSTm93fPVVprzMjT4gWiBDivrDeBAp2ytVBH1aySh_lK6xVe477c52ZC5yko8itpheUYcNWc3n2oUgyjFvQ_PsnZlvUEbWpg_gFLO2Hh3KzGJnCCEfWt-q8yA4kX90BooWdQQ4wxHRicLPfea-5Tt97Pr8RkL1BQn9pOVq-v-ep92og0WAL-sbmf3GFdR0o30VyJs0Y74RyfgCWKXhl2QwccYjieSD5jfm_ri9ueIAfpJe864p_dXmePvEXTEdf5Yf8Y5tUTsk97iQtaT4vUuHxRS4_NUwaCuNgvtksbuUv0h5-sF7Blnub3K2O5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/djrRRaeBEbkoZZvqyKUVSL4peWslA7rqi1Lwb9BF6LHGM8V8-qltpByzKsSm8NFuZVYIXYXuZzptgSh7EK5EWpnKSQg8V8rcCOIW9jMqsQK9NQar0btr2TD9HzRsQEWg_JUBUAdohGhuvJEsRwtATMErPlnrGgLLulaUGkew5bDNEhokzDc9-l0VshYMID-kjc00P-EdJc9E9TIlSH7o-Y76lnFybMuwjvmfha7Wiy1TZ8zlJymXlWsBC_QYo7PcGui84IKXYUfu2uObxblUHum-4ViCoIHWCz6t3wa-ZwT6KassEP2jUYUopEhwfLFxKSFlM6D1ASetPAFzMr2yLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران می‌گوید روند مذاکرات تهران و واشینگتن، «ادامه‌دار» است و حکومت ایران از ایالات متحده، «اصلاحاتی» در پاسخ به طرح پیشنهادی خود دریافت کرده است.
اسماعیل بقائی در نشست خبری روز دوشنبه ۲۸ اردیبهشت گفت: هفته گذشته، علی‌رغم این‌که طرف‌های آمریکایی به‌صورت علنی اعلام کردند طرح پیشنهادی ایران مردود است «اما ما از طرف میانجی پاکستانی مجموعه نکات و ملاحظات اصلاحی را از نظر آن‌ها دریافت کردیم».
او افزود ایران بعد از این‌که طرح ۱۴ بندی خود را ارائه کرد، «طرف آمریکایی ملاحظاتش را مطرح کرد. متقابلاً ما نیز ملاحظات خود را مطرح کردیم. از روز بعد از ارسال نقطه‌نظر آمریکایی از طرف پاکستان، ما با مجموعه‌ای از پیشنهادات طرف مقابل مواجه شدیم که در این چند روز بررسی شد».
سخنگوی وزارت خارجه ایران به‌دلیل آنچه تبادل «نقطه‌نظرات متقابل» طرفین به یکدیگر نامیده، تأکید کرد که «بنابراین، روند [مذاکرات ]از طریق پاکستان ادامه دارد».
بقائی جزئیاتی در مورد اصلاحات مدنظر ایالات متحده ارائه نکرد.
@
VahidHeadline
او همچنین آمریکا را به «خیانت به دیپلماسی» متهم کرد و گفت واشینگتن دیگر «به‌عنوان یک طرف معتبر» در عرصه بین‌المللی تلقی نمی‌شود.
سخنگوی وزارت خارجه جمهوری اسلامی تاکید کرد تهران در مذاکرات با آمریکا همچنان خواهان آزادسازی دارایی‌های بلوکه‌شده ایران و دریافت غرامت جنگی است و این مطالبات را «حق ایران» توصیف کرد.
بقایی همچنین درباره تردد کشتی‌ها در تنگه هرمز گفت موضوع ترتیبات جدید امنیتی در این آبراه صرفا «مالی» نیست و هدف اصلی، حفظ امنیت تردد دریایی و صیانت از «حاکمیت ملی ایران» است.
او همچنین در واکنش به گزارش حمله به یک کشتی کره جنوبی در تنگه هرمز، بدون اشاره مستقیم به عامل حمله گفت «نباید عملیات‌های پرچم دروغین را دست‌کم گرفت» و مدعی شد هنوز مشخص نیست این حادثه توسط چه بازیگری در منطقه انجام شده است.
@
VahidHeadline
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، در پاسخ به پرسشی درباره گزارش‌ها از قصد امارات متحده عربی برای حمله به جمهوری اسلامی و سفر مقام‌های اسرائیلی به این کشور گفت: «ما قرار نیست با گزارش‌ها این واقعیت را از یاد ببریم که تهدید اصلی کدام طرف است.»
بقایی با تهدید کشورهای منطقه از جمله امارات متحده عربی گفت: « اماراتی‌ها از اتفاقاتی که در دو سه ماه اخیر افتاد باید درس بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L83WcR1fL6Y7NBDWwO3nWFoq8sbmhZ-FJiAFN6kLrzPt-FBFsssvb3jJgQvkLJRUYl-NCLF4vgJfTrKQfYeqKDw5XFbAjHVY36tw7PFPDBZqa6dRIhmsZYY9VfRxRd6OjM-mmumC4BtTrdjD7Gkjrl2ur0RrxuDlMr743_5a8NcveJJF8wo1TDV9NbuDe93CnE8678ZiHDTuQNPfqeVWaa4LyHq0uVAvpLB_5_aKfpvz9nIptorSGy9n6VvPJyF3oc51FkVVrXVd2Fm6lSsGCxkUoRuZhc3cWxmN-O2iWT6oxwzrD7S-eZyAswmMDnm6LWOoiy9MQQzeh8iKWZBKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I3dER-VTXpBL8i6nSV8kbBvZLd_D6LE3n8d252bxW8_WSVFR-C6nvNVEvJUDQPWmHIXf18fwIxE-m-rECnJMY3QiV9dbCoRFHiR_ryV0A8axrM4q7GaQh8rHWcMo4DK4bk3Sz2EktBcNLtiknlM5kaXXIcgEYomfE22zmUZyMiQgt-DdOyD2MJKa091v7IwvJbNovuXwdCtcX5tER3Tm1XCVKRu9P8uRqltbK0fUkRYTlCUWMdZwDZCJdHur_W8CMY70-1QOyG5oiiW9IB1GM4RODyXtHs8V_to7KxaAVLFwe3wAMdMujMtRIeP9eOJaKMQjcGymTFV8fn1EfnQg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل روز دوشنبه ۲۸ اردیبهشت گزارش داد که ایران در سال ۲۰۲۵ تعداد «بی‌سابقه» دو هزار و ۱۵۹ نفر را اعدام کرده است؛ رقمی که باعث افزایش آمار جهانی تا بالاترین سطح از سال ۱۹۸۱ به این سو شده است.
این سازمان مستقر در لندن اعلام کرد که در سال ۲۰۲۵ دست‌کم دو هزار و ۷۰۷ نفر در سراسر جهان اعدام شده‌اند، هرچند اعدام‌های انجام‌شده در چین در این آمار لحاظ نشده است.
عفو بین‌الملل گفت «هزاران اعدام» در چین، که بیشترین استفاده را از مجازات اعدام در جهان دارد، انجام شده، اما جزئیات به‌دلیل «محرمانه بودن داده‌های دولتی» در این کشور کمونیستی نامشخص است.
این سازمان افزود که آمار جهانی سال ۲۰۲۵، شامل اعدام‌ها در عربستان سعودی، کویت، مصر، یمن، سنگاپور و ایالات متحده، نسبت به مجموع سال ۲۰۲۴ بیش از دو سوم افزایش داشته است.
در این گزارش آمده است: «این روند بیشترین شدت را در کشورهایی داشته که مقامات در آن‌ها با محدود کردن فضای مدنی، خاموش کردن صداهای مخالف و بی‌اعتنایی به حمایت‌های مقرر در قوانین و استانداردهای بین‌المللی حقوق بشر، کنترل خود بر قدرت را تشدید کرده‌اند».
به نوشته عفو بین‌الملل، «افزایش بی‌سابقه اعدام‌های ثبت‌شده در ایران» در حالی رخ داده که مقام‌های جمهوری اسلامی، به‌ویژه پس از جنگ ۱۲ روزه تابستان پارسال با اسرائیل، «استفاده از مجازات اعدام را به‌عنوان ابزاری برای سرکوب و کنترل سیاسی تشدید کرده‌اند».
عفو بین‌الملل و دیگر گروه‌های حقوق بشری گفته‌اند که پس از اعتراضات گسترده ضدحکومتی در دی‌ماه پارسال و همچنین پس از آغاز جنگ با اسرائیل و ایالات متحده در اسفندماه، استفاده از مجازات اعدام در ایران افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgsCP1GraEYR5brAX7UNLNWfIusu63yHAld6qzX-9t3enBKj3HJ7uB7oIJ7JW6AUMwj_ahrWIwF3jRBP4_Aer4e98oMF5CpDDbU-ew7dVg2O3Ql5ilwq7-OKR4OfiXIpGsPVjfBAaOCzq4kxW2Cg1eCEl-RosmLvt-UIcpomG9JAPWjw34v6AMB8ZclNdWAieV08V__uIi_Bf2-NLIgJOaQnjG_idB1bR0vx4r8SZfq8t9a7SkUmKvhKAs1j0hlDIgMrb4pH3fwOh4txozRP8Nn0FLu6juMnD2YOFnAiRPGvnmsE2_3so88Stoa5eMLFYsyqDEZOn7So_Vyn18bWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2j-s3wXr51xN3M3pv1Zznm2_GUGM70SfeQDPHwVOFy8U4HF6ZehZ0YXOvqIDE3iHRcObAXMh1oQQzNQ7e8DJQD0pziZF4VPHAkdrnZ30XsgfKKgBgViYMYqvds30SNftzAycEi_0CF9XGdpQDCf-bIJQUl8AxAvJ-9LrR8RLgsAv-zDRLaBbD22EwqC_no4svCEJtVW_llNcD5zXCSBfzwilrIAFMshPhS9jdBBFpdOC1yVJhT6_Dcjt16RSQEOjQ23M5ciIIetyErlXHvindLU1DFY6KsAQTKGjLVSA05ueZ1YY5IaQScKf5O-bfJiGnuu9b0VuZXFByWe9-8llQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWmPkwpOr06etWfn1vdbV2x3cB9aaHcz2TNiy2ej4TA4y935uzq9ra6BwSwwXnr6KH-Is6gj0w-XDqFJqaO3rKdoJUAwdxnPsbZ7Vm8FOoYzRNUum6t8u2IjI5ZXVBK8W0Nl1KmymkJrLjf0RTWgNCFkQQvzP2eMnGDLg0k9fl7Dn4nWkLwqwcuH0Vj3wLAB2B4Jv7nrAEEv1-UcwGGoTC6kvCdlmUZbIW1eSge38H-Lvy2XtJYCHTITBO4kmqVJSn3UgGDoSzhvQraIU4X9RiWzqhx8tnPExT3LfNHSH-uVykumKVL0-QPE4_woweabLJkljzg0nP1LPwsNAadrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ترامپ به فاصله چند دقیقه‌ چندین تصویر مرتبط با ایران را در تروث‌سوشال بازنشر کرد.
ترامپ همچنین یک تصویر جدید از پرچم آمریکا را منتشر کرد که در پس‌زمینه آن نقشه خاورمیانه به مرکزیت ایران قرار دارد و از همه کشورهای همسایه فِلِش‌هایی به سمت ایران نشان داده شده است.
او همچنین چند تصویر و پویانما را بازنشر کرد که ناوها و پهپادهای آمریکایی را در حال هدف قرار دادن پهپادها و قایق‌های تندرو جمهوری اسلامی نشان می‌دهد.
@
VahidOOnLine
طرحی که سه‌شنبه از قایق‌های جمهوری اسلامی
پست کرده
بود رو
دوباره
منتشر کرد. ساعتی پیش‌تر اون
انیمیشن دیروزی
رو هم
دوباره
پست کرده بود. تصویر ساختگی یا طرح گرافیکی دیگری هم
منتشر کرده
با عنوان اینکه نفتکش‌های خالی برای خرید نفت به آمریکا می‌آیند.
اون پستش
علیه اوباما و بایدن با طرح گرافیکی قایق‌هایی با پرچم جمهوری اسلامی در کف دریا رو هم دوباره
منتشر کرده
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoKfedYas_Wf3eMa9EAnpo9OTdv-wz4-9zhwOLOmvBYIEVV5eaOHcOR4EbTfTJCp9zhhk_XnDdW_QbhpNslGxZystYsw6gf9b6e8Lo5OQ6o-0e5KVL-ak0_krVCPNkr2clj14PDlbpHKYLInjsAf8mr7WDadro2myWNclbE6217H7ivRVPi3ayjujzfZ_giCahJINSLkT34G4J0l2rX4cZuFvXE3RDyVK16CtmTvi1zeFqh995xVUWyIxlsqkjyqaLefiz8Fqdcf4hEoI7G6Lja2szzDTH1w4LJgxidHLw4b_VY3yk6IfCoOr6NYq7q3QD8OExcG6wQAdlR6tghkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3uhWpNGx1DlfzLG_uP5RIEUgrkVj06TtEorRjj41qMqaGUMCo9VD27JC83ER59cZnHFgAyIy8CE_YcLH8iIHVG_J4AfCzuHf5pGStV8fM0oWg3SiuboSSZuMUOa5r-Oun28CmUAwj2pj7O5je1nAqsZJmyzinLayPnaDG0qhnqxjGtnGqL8H9E_QJRjVYXB0LeSYxCGxPfoA9bLUbhg_FOAJNKiIFhEmUobUANuSQn1U0vptQRci0cY5MAKiVO23EpzWYhfbgOrkyY2-j34y960914OjzgU3NWCvDIljQITso0nXvsvzOBIh20CeaArBKoov6a_cdo0AkAC1Gh1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qf3F-j2uHRbGdBf0B-_rGwzkWHF9DYIXkOtrRfZqn7OBLYaQSppsyT76V64kRiG6Ody9LS_nXjODptdrHOlYmuLpLYEnNIG3riZ8S1l4Ygnrzg3A7Oq-dDjvtdWHcPH8KGiehp4Dv3b2JhDf4-Y1thlD5VqYJoPxEqSUzjeBm6bJqxWth16KBMwueW68PEUNadmkuVhnOa_YO5Sm3wq5oyfH4UoPS2iUz2oPYfY-WR2uHNuiSUKzA6qjemVPp3o7qiK9Qt3Yr8ofFcEZJ8Zg56mJMxHshxyxecl1WPZanGMqQIMB-QZ7KFgUOR-EGKX6WHP2oG4IilJ3HTWfsPVjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhAVIERxQFIPJwU_nYrhkups_Tc6QWMQiQwnvY0xkYEIxUGojsqMoubZs3P6xNwXKO5ohC9U16iDJnlqa2ThVOEsQabTetkSWCi7XIWlADwcVUXa9PGBqYA-2KUOjB7npWOPWmtQY4Ruq9NDBUJ9ZHnkfUP7bydsheN4W7Gr-y3_YKe2YRTm4imb6pdPr71UBwiIXm-TNn0PNTPUxBSypc9gQub-e_8jPJvQOH4RsUxOl-KxmC_1RiIEaR-7D-3Yx6Et_aA-Kt-kbP74O2UsXf5s5s_CVYbHEzRdYHAMqLuyjn9y_BxQMcgZiQ7C-0owZjJlqTT0TvMT7s_5gAlhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHI2qKX7xuAUExBHYCwspN0U0MroGLcjTOmti-uFTLA5lKsUMyUzISlHXQBOYqHgfA--uRHKYb5cOnUQ6bdsRQk0sa0hsy4pGgLn_HbvVv8QZzjS-y7oP_dHv7OPvrSRys8V4XYXzPy4iVmZ6xbZ3CfaPhallpVRh3t0_ibTUg3ggTxNDjnnms8izYreNHBL33WycF71SsryAXCAXWg3XpgxtV7wn4czAS7Vumtavaq-IczOGkP6ONtqeFM9snWg36ztQbcO1FIXVuI5w2f4s9Yts9Thc1vvQULnB3gHJ0UUw2lh46fx-HZqLlj_eUsW37q2nTy77PayzO5f42mZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qPdklH4LPY5-qllWMBFL8HOEw0HJla2PuLVETRqyf0ZPI7Xfq5AHMUJq_vu3zxAD4I_B0Ses94FabC8osxpMDj8u5qhAtlXYPSsxomQgls0v4aSkk37MHhbWnYWH9Fpr1ysP82USLu_FK26fsNBBmAyFJ4LEW-0Hj6Et2RmFZgaNB_JRqfENDnULnzLti6vedz9rCUI22cfrhtmFr-zenu_b-FyzGCdJZqrMRvp2nYbitOCaOdC47Lf-VLFAvv9RhhaixKChOUWvIXXfrOLXDu0X1Jx9qCaku_fzRMV9tbxNCiF6PjXLcpr8PyJDb_EzLYF4FCwBRysahC9Co2kSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bIc9VR6mV3Dh9UVP2N5Etstz86shRGtGMmhT3UuDSmhg_IgGSDzWyPDMym9qSr8cd7ztjE_4otlYVKFPNTwd_RKeqfupoa3Yv0pbJU6F2zpKzmUsum2qaCpzRKRJnzNI_3ij1TAgbsOzAezMa5PXUKv32ehFXek39I9KZz9kW_rqFuTQWQB4oYQyoeJamgtjRb-OJBDaifUs5IO-qI0DxIJnM9tGngQ_gy816D2aLRds2EGcZqSkYaZef2ulzbjySpdNz6yvM7nZdIPCex_SbbCUMlpoKOxI_8z70Lhgq6B8CdCLQfYznH8kHioMpse13pYC7LjvlMLGVaLrySWCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ixH09UW1_nDMCYo3SJyywRcPehCc7A0nk40QmS651Jti_G6vb5k6RzTUd8ty7NWZiK8LHFX_OFI6zbU63S1Mb7gb9480rYvo1sestetMTVsEWw-L_XBVT7A5TlHDvrII85FQSBLPvlJHrUjOcDmfgjdrv0P6TDNdrBRGwU1bbjezXiHoiKy3PwndxVzrj9AJtX3U-jGyDKtfpDBAVwBGy3Qa-eKILa_KQYYR2uwhrIFasQhj_32yNjUABUjXJEPWBszWJbucZxFLpc909V_n-pV1uavG3Xs42nf4kxpIHYMNRt97I8DrvJWwkG_cBOplrD-ll0mQOsM4dorXqZAb1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VtMex0adFpjpr-4trkmzwPSoMoZ6hAMURJj0u1oLk8ZMnt_vN8yBZ69LrpqzS043JUWgktmMOgfoYaj5FHIB5365HPNMJFwOwGgcNsITn8rz4mgUoqN_5IpYm-SHKxth-z04VOAA0R_t74IbHfYbBSDR1zeKCPg3z6oH_yUJm1WQFsS-ELQ5DEZDdxQuzqXhzbL_Z2DXKTQ3ouqTB4eNmXC8biovRu2mKdv7K_wmtVKAWAmtGNMSDrXRYZMxyN9VoJtdR39uq59-bTMvdsfgJ4X-7NHd8_c2QhnqfcXyqyUBJLg0eNkTs-2sRe1IG_jLBGVlnNv-bhhgUtGM7y7R1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFibZJkSwZiLSuuWXRbqtDS2PJydNSX7aH8LnGdJ9wzPdG3W2z6UoAuWXJGojYVIa18oSmwqSaTR3IH-3xZcjpue4VCebnky0_v3hapeuGvJ7ZwGpmwdYi7sKQVx6BVNt1oAn-4wLRPvneZ6A8OK2rTP287OJBU2ZU0UqLPV3DC-jyq26hRDchybeyY8cM4Fz0VcAg5U86_rfwylSu2e5r5a3-kXadgpNL1o9XG1Avr4w1QdRDeq8Y_McH4neZ3XaR6r8tiX-8griakT5W7elNRp2hQ5CZ-wsq60Rc8su7Dve5FC5DSncrj5NcgQmob9mQ5a22YOp4pfg9Tk1phEQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0F-D-GtyAWCzISRvdmSmC7zZRLm9VVIYXkuk9ByO5mU5ZZaABNVhCNuoKmDmzREfcZMqWrtaVetdlMcLKwKLqrIhXKeqA9Byvbr1UVTNBAHoJTs9cGQ5Oz3VkA7--z_M9UwUDwb3gM9bN0lx7imabECzRujSFX4hEeo7oW3CDoVrN3KGafpcoDiaUqhNwof3XECOkeheitv_8gPgAJ7mm-p84o7s73b4iyAdKBqByWQDsf2rItrBguKF2A0LYBQ56NHipg7cRxpCVh8xIJQrYHeJGR3iiUGjFlGAE9zywEGk3g5Gtx2as-qql3agEblMoek8WRDBdmEpaovUThNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS8cIpFurkOKeVcWcFiPR_IGyVJRrrssLnE2pJot_hb6xJQZrBVlPnLHM3_UIL9TVHUFn1mMNnRWNFysSU3KRaOf2b5x1UUuOPiwfF_GboCOng71M7Q_5X4x5i0-oAvVj8430kyg4zq6ryNZBtRITkB-f4BVEwr0ufRmFrwwpaLnhkgGVDuhwu8roLpeR7wZqo2XMkg9Ou8FSnnTgMLUMvpufui1cNWeeTJS76uJmeYkaw4JOy-cUa0ZjyRlMJ5wO9IZaBZxf6GpY5kLzdQ5bP6WtW3P6-3bEOSLjr2U9dRuRT6xhNNND_mA-6TqFbGzkwcpq-Jm6Jy87pBw2KsKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-6xwwdjpaPglYDwpDz6y36925uJ7l4Zfa66QVlGFsBjawW5vzrYQjKbFILCh1XIcD96eb9pbdmUpWyI4eyVKjd1Q8VK3_SrcJe8MkHsq-q06Z5sDnC-LdfMOJXuand7uYKO07ZHJNfxpeo_bR2jNlvw86wG7vVFC9nTYzPo2H4vq6bWFiAXtApLNvb4AmTbKyYqLipl0XNS39bw3zK-YzAkU5Yaf8a1UAa5oFbrN_yv6Rn-auUC0JQwADUBVZdecILohnsQ7ofTNnSi5sTtjcTymrUaLW6DtOILCvSW40izb0iRNazlmaXRmoPP-UEhx3Iyaw5os2PHXPtzx3zLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUpIddzPN9BSgBcQO8NbNQ7vBDIKb-sn5nmPcJeuFXoLrCnpdwVRePPt8fRjakr6CYX0ynnha4UyUdoxGyHbYiZJOVRBoowvFHRPR7oGiN3BoHF3RG2cmhHEIOKr7QluyHn5v9wvZKnuG0_sr2TRckMMLDkQgv5tF21dxQo7-KUCrO-Znpm_9e6aUmXaWce188FLswW0rgZhWV5ptKjgYuinpq2lL4pm-j_gRj3bxEa_DlIDEnhaGd1-C6L6zqDWGirSyJy9JRHkh0rUSBc1rHSCCj2yUUBmxqiLeUFk-FeXU33gugiyIcfInOxqb77MFXEDggjSX23kTOqAADRs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3OtTYdhc1E9AcFB9ynJg6GTol6JIE2_IjCFcY2g76ikyKLEw2_-2ibaUBVOP9r0x_3OoPQ8Dhb8WQXeNkc8H_MXDpn5y3kdPinhcc_trtNWBV_jHioaJoncZheOsMb0IZSmQ125uACImOAomnWREOnH7YNKkS3QTZA0WtVNkP6FIDwwBXtyNVlukKBs77821fzFk45_GA0ZMLQCO2HkQD2fCjm8OwmEZ9g2Tr-cWGZnKPjXGCv-0DamGZYOmKXxMBxQmV2quUMjFPQFAAMFIzF95DwFLZqhwe-KMinUXrN49qracECiE1H6a1nZmdsnz899B9-H1OcVUYQCFNxNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1RTI0Z45SX_Mh4mth6ZO07dG53yWCloFRTz1ouQy7lcQw9EjFV4yMvSZPnBE7HiS8j6ewHc1QI2AYMmwqJ_hbc2fP-XZpma1hLs_VH32Lx_bCTvcxJrBXPDsVOC_-pavLgiH-wVemnT6TINKFir-TaLpH2VIb1xs2vl8vlWw33KaXB5zcmJIEc28dtAXANzQ83MqmC2XfpWkHdxctUv_jH05vjDs2MmlEuM_l-ULAwEWf0fbC-KW_IYQ76H35VCMqU_Xt2vSnMX3h0R_oIuHVDuw8r_zylIJ8Cvq_GdW7HBu_SUjDjXBFI3uGla01Vw-6F4xgparR7veFwkNC0Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=BhHho2QxLW9Ep1dHGwgBHhxT6OthZd8EYq8mWNvrVcLtrVT4O9XEYcxdasj2joAHWrojD9d2ljCLOHJDytzDecmx43ounw1mQIIMoah8Es0eBrlksZgAfdMFxX_iL-bSgFAScH7iGzW9gk83_QZiq8NZmOCFRX_OTWGaanTAhFPDCVtOTGrrawkdRuq5UMSDCjbGkd3t2pFPska8qS1vXu3p9c1mxDN2qj0oBI0B84qYtpAb4BmK1tmxK5EcfXaf6zvESKKH2k5317IKBoT89Q_GNlsNO7LNIXOj_nntsJxMGS64_GUkGuPKNfMGGaBx8-MqRD1nvCsHI0IOWEvj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=BhHho2QxLW9Ep1dHGwgBHhxT6OthZd8EYq8mWNvrVcLtrVT4O9XEYcxdasj2joAHWrojD9d2ljCLOHJDytzDecmx43ounw1mQIIMoah8Es0eBrlksZgAfdMFxX_iL-bSgFAScH7iGzW9gk83_QZiq8NZmOCFRX_OTWGaanTAhFPDCVtOTGrrawkdRuq5UMSDCjbGkd3t2pFPska8qS1vXu3p9c1mxDN2qj0oBI0B84qYtpAb4BmK1tmxK5EcfXaf6zvESKKH2k5317IKBoT89Q_GNlsNO7LNIXOj_nntsJxMGS64_GUkGuPKNfMGGaBx8-MqRD1nvCsHI0IOWEvj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAF7Wfpdzu_hYPL-Xrv90s5cYe2wtafGFRNHu4smiUPmS-MqC9YcY5UNoD_xVE3zEy97EzTPlQK86eoGphh3PTx_bShQS6JFc85qPLltWEuw0O9qMeuZXvjrmLFbyocWOYNGmjVe8J4m255ISL-jtv-3dBf6LRM5ymfK4CcOf9kzsdABzEwTWqMSfaiHI5d_mgSVrR1--I9uSM0eNmMLkuhiOxMaLc0QBZ9sNjeTCZHnzTPDU9Ox_TgUQYHltjH-0CLTDZWUi1rn4uVOqElvrlCol3x_o00s0ibca_bM2yGNC4Pf6XqbdClq1S6ydvGGnkrvjKcxUDGmyP3kd6DO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KfMiQR8SIR1ueQnkkPNeIH5yVew7qfYqqvXMssSGfRHcADq3UVjZ0YQzGZi11_81pzWNVKrLyeHBYZFMjcAXNfvnOCUjU7lWAgWec3I_VtdqBlkYuPmPAEj4sry4eepWCgFD-ug2tRh3gg-KPRqEGI9njOtFKwbkMY5hRB3WcC9zwa_WDmyCm8aH7O51Slc6kg6Pbu51BucHmhp7jAKAaSuQuJlzpQqJ6iGIclt7RdtbuunDeNtHNUa0C82i8vffzwx3Fc59n24DK0DwR5aHi26gz7tR3uIFCPK-1JP9bl_BJYK4AvY5Dp1u-vAYudL2AIXaliBy70Il3MXFQ2Me1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BcGfX3FcRY3vHsn9YNOmRmqzkkikntV3MIp7NiurMe5z_okf_kqOWtZMICXOVT6qN9G8fYmWDuK-y08WB8CjzKcSVFJqRgzJKF6FjKe7vp4_AjdneTuWNxbw8ovmFm531b3nszx3OCPFSgtWr5rTYzdomAklRzV9nHkHC26FXUaGytNCbyRIvtQHJ2bIQ2x2SHnhV3AsS1Efufgqx7NMPT9A7gEwsBx077N9x93w9O74ciSi4uY5V1B00zTrY7LXV4nhBOMo2qBjcqTg91et_lDOhgXBfflhVldnHClNFdMZ_B_pfUhm5rm77pgjw5rAkWDQw-01o1kyH9mewgaYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AJGsqzeyt_P2ftcA1Lkv5UdsQ1JGfHwYALgsNwG4UZJSMG0zlogpcRylfKwE5v6mLRkcu_5z4AEpKDbk_Rx5lqsxMLC_Uh5vbx-kAOVpqhZdTWojV1YtpgDNDMPiRmS5k3bKcf08g84KlhOLTtXKIq2T0UxpASgNyDVswrGC6zYy9lAvzBv9fJd-56MJSb25_voTci6kmdAyzwDIKxMHcrXHXazJP-OY2jJbb_QNKXy87N_Biyu_lYHCw3uUGPZY_F_PROxWnmpna2TJu13nPpHPZfWdEYP2gJngdh2T_u1HQ1M4XzSloFX_GR6SAHCWbbZZLW0u4s4v2VCLsbaE1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=B3pepZXhdUUPDBG2em6mw9bVFOTIRYeu0oALrwT3iSDsVITNJwjvvd4-vuLZigntKV9_dIUNmLcgJ1jeV3gxRn6l4WzQ5U6Tl9ZyGnF7I6fEeh0U--iOE8eNZPKRT9QOMmBijfx7EpyfsLvFOV8JvEIpY0eq7envw7p-0bpETv6YZxAFwi4bIXn-wbavWGdK8vT_cLszWvJAf_fGCPknbgxSUc5Vub-9MYdxvdD747PhFZrhUgjqNllpsRehVwDXA-i7UpKp7zAlPjGEj-b6gRRVsTeMiVQWbBK__KuTS8YxLY9ysOcsU25ffwwmshSiZGs3tUQuTMnXdFDABoLMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=B3pepZXhdUUPDBG2em6mw9bVFOTIRYeu0oALrwT3iSDsVITNJwjvvd4-vuLZigntKV9_dIUNmLcgJ1jeV3gxRn6l4WzQ5U6Tl9ZyGnF7I6fEeh0U--iOE8eNZPKRT9QOMmBijfx7EpyfsLvFOV8JvEIpY0eq7envw7p-0bpETv6YZxAFwi4bIXn-wbavWGdK8vT_cLszWvJAf_fGCPknbgxSUc5Vub-9MYdxvdD747PhFZrhUgjqNllpsRehVwDXA-i7UpKp7zAlPjGEj-b6gRRVsTeMiVQWbBK__KuTS8YxLY9ysOcsU25ffwwmshSiZGs3tUQuTMnXdFDABoLMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=hXH-cZedQA6CpqveVsvsw_Fw6OXTH7PvlncaxTS1mS5sbCTm2OOZzpqRTJGRJiD3Jfz6_5NoVPAQXnJuzwschVuZeugz0JsdS97DCB7TDeX-ClI772ODPYK30kPwDw4KIFpC5YQTvNFJcAkONe5Rt0j3iz2vnsJOf7DBgc4r39WiPnpz79cj3eZXgbuANc9HCgpPLtOdpjZ6wZu4ffcXUKwO1b5U-hpya-g1rXwt4RlP7VmGQKSRiaFkkF9JQFAsBDsy3cwXgrdonpAUxqi7iJqvNrFyT91WCXegPOJ_UlEFnPe-JY30JTOGs1kdUlQWTlZ7kKaf3idOuMEL3Zf5Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=hXH-cZedQA6CpqveVsvsw_Fw6OXTH7PvlncaxTS1mS5sbCTm2OOZzpqRTJGRJiD3Jfz6_5NoVPAQXnJuzwschVuZeugz0JsdS97DCB7TDeX-ClI772ODPYK30kPwDw4KIFpC5YQTvNFJcAkONe5Rt0j3iz2vnsJOf7DBgc4r39WiPnpz79cj3eZXgbuANc9HCgpPLtOdpjZ6wZu4ffcXUKwO1b5U-hpya-g1rXwt4RlP7VmGQKSRiaFkkF9JQFAsBDsy3cwXgrdonpAUxqi7iJqvNrFyT91WCXegPOJ_UlEFnPe-JY30JTOGs1kdUlQWTlZ7kKaf3idOuMEL3Zf5Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=LwNm0E2fH5CzwIicaiLluGvc3fODp9q9sJgdS8AgBWhQ1aSQUMdJbQA831bqZcE990SSeITMhy8CMYNFYPH6v5C54UwM8nHalmDqW-t3azR3_VvXuFRkq8UWGQDrphW7PTapbXKJTg6wmF45lljWHOlOKN0Ch9FbTF_zSetAjLVpnLn0V1XeoPTvQR-cMvIQr9V9I3aDJVshb8XqJuSUTFudL9mCaga89CAP_kyYAKcmeRd3yNhE9lvenh0DvxusLQrS4XvmEiIgwd0EhpoW35CxShD1IzZMMesvsRqCRybF8jhcsRB5Z139dV9uOWk2eH-LA4lTppFC2jw5tF27IA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=LwNm0E2fH5CzwIicaiLluGvc3fODp9q9sJgdS8AgBWhQ1aSQUMdJbQA831bqZcE990SSeITMhy8CMYNFYPH6v5C54UwM8nHalmDqW-t3azR3_VvXuFRkq8UWGQDrphW7PTapbXKJTg6wmF45lljWHOlOKN0Ch9FbTF_zSetAjLVpnLn0V1XeoPTvQR-cMvIQr9V9I3aDJVshb8XqJuSUTFudL9mCaga89CAP_kyYAKcmeRd3yNhE9lvenh0DvxusLQrS4XvmEiIgwd0EhpoW35CxShD1IzZMMesvsRqCRybF8jhcsRB5Z139dV9uOWk2eH-LA4lTppFC2jw5tF27IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7pDiyEeloHxyxEHlzuzqqoyxNWC-6z_JcnfU8zd8Cu9XgkmJv3tDHub1iNxiahvwIr4xuOPbxvLiebTEMZB3rv4uQiuMKcvbz6GmgjI92JP5oSuMJtDElW8-02incqQtGrGzSXutOiGJ-0sXQyP3PM54kUnYgU2s4TzT8YkAaiwULMU3u1e-3-ojFtUe13bmw1kdLrRO8l2lxpxH0N6-N9Bzc7FRdX4MB9BK_luNA2JuNndzFmCCDEJOPdZ_X6p8bOQqtfktaVV7ZaqCrUb2VEcBWV7wQy0CR20AxwqPvbAXhM83FtSN1CyG4jTV19GHIQo_Pvh6dFWAx4PxCEiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T8NcL5woH_mLcXcswmqVAUQLkBGOsJtQn68EMhVymocSChIZCQxnfm3xeYYBsdj11L97-otJISGTuryqszI_ZWEWultXmK1Npv98RQLN7688e35rW3AVT8QrNtcJBqfMuVWeWF0ZC1GQJMMebRwLt5wSmEZ7oeRdK7jQ5Wdl5_Uo-hRep7ZqvPUvfdhBPNtAqfxD0HD1fSAv_Hb8S76rAlL0ylO3wRS6BzeeRnNp4EWFwcb9dk37PkPSlINGbGrAj7skU6moWzdmdkwT8yY4YIJdrkxNz1-U0xJqKDtaR3u0HQSWixp8xwbX_FFyc-pCNlJWjLn7Ud3-Ph-UI_7qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qadyXGN06K9_Qm2D5BHKJ31DMF-0EE9FrpN1EospOxUepbh4D_kqq72tVJ9_NQHz6R5W5afXL0PSDWpSaV1HOYcMEdqa_8HsXVYxxA1WPgHx4wLEUZwKTsjZH1egRVLNQHF3AvTFGULV6TpwU_YVaeazRdFDCliOl7FwxtOmfmpSko_Uh3oTEQEfqI7uc-fQh6sfB9icMvHqdxoumsxInIRBIEE9GiWgH3Cb5qkfvdglQ2oYorqsVZmwzjS9JDICp46RC3IjH734tuX4z-maDu955AklQ9Wo0RbkHPFZoW_x-3MyHXZGOFukrQzXHaV2btqOq90hS4_r8phzd8GUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mahIcSTqCLpJhnd2yr3SXtXk2qnU4RpzprAa1J70IrXkMY-OEgRDYhpB08AW5y18WB4S0bjcRjJG3Hr6y13YL4_3I0LlmwBDrOthnTuQB88SqgODwQi1EaX2kuGmBQbcU-dMOMmWsWwXyZnKFDhsertkXEAgqzIjskXXgssUBr6NmCsCpCZvIbukHV1eiqhCSXCnLlt32Z1YOkMuUWIhwJni4kCpKw4c5ilJYFvQxNmyMZe2pAIn9YMmbO1tPTgY_pSLB6KfIm6CXwfe3ZEvtGSEiwEnwXtIJ4JcvLGmWmHKCTb9kuojoSAqe1ZhzDaCEq1s3HObAr0LRsh5SNNL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VLXO3fdd0DiVKjWiuoibEqAgo2guajRODIZCKOkB-TvCVDzTnlFl3Hv_EvA4HwvcmcbkUfx2L9NlmH5I6FPMNuaOKzNjoA-_2NRRGzraeztb_I8L3yzMQqysB30YxxNLM7Flt-1d6mmPwqtFWFcNSgzSuXZJpuyOgCqnndglfZpbCGr8XKcXCZcdgRnCZ6V3V2G9YVeAT_4huOGqlMAIOqQ1y-aa-TSKvMw3g5vhIoHo2YIsMrlEPMlAmET3Dr1z44wRYnE7hH2ZxdBT3S9xVJDReawSSCzpPaOvfYQolaVmscf7a6dcsVcMpzxipENuayWBfswML-mq5vs21At1TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3kKaavajZeuvrP2jgJgGlFeR95xIyA2Rr_MOxbTElXt0sSQiJU98PR0A_idphSXj-xdI9WHl5XG8GKX6qTsuI1o7KAZbrN2f0XdECqQHTZ3KbQBjX6h0lq0e4xviapIsAfum9emSHBKeZw7CQmccUccqx9r5mG09j7rnjCr2_DofS4HX0E8r8JohbRIHnuZn-LE6divJoH7MRalmypHIj8ugdYu12mGWOZMwrzaNgiiNr4fn6LCp4EExZshDFae1T6PcFWAUeX3z1SVhNLXItozh2ONYEi5zVYyTt9e3QICKa_cXzkUl3N-Qax2DXDS-1Wg8vF-RLHwtoTCoOXvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii81sovJr7U2PA6US4e77oUehLGI2Vn4XVzl9WqDe4sAHtaZ6i77Dlm46hLDR62TktInVwxzc3fUcYxl3YbOSd988GigCj2rVweQ87tVuflTB5W87tzJK4IK4lDjXF4Mhox0CB-CW1LzybeMdKZZ_GsQFHICzTKl5vxd9RGi9ZMd1ibKbLRQHgdbC5Qj7g3TMufkbYev9Z9S7dcRR2a3-AvLOYUlfLVD_jmK13xTJdWG2zi6STPw6yNxYJrazfAy8xajUjuvOR0hFIqxldMQQnqHKtcuUg2fZdbErze9z-jR9Ciaf8FKPDXP6WQQyGhJba5AY4xotT2lNyFL-MPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YlaXdZJartPHFBwdmPGI_IN2vBDWWM-2oN7-Eivviqxv07N_UP9qTO_2hk9f2bGjbTIYKSJLI_tniSjwVeI2bYXjsygNMBCa2SB8LgARKz5y8A4ZMRDYvW0HUrcvtvIHJFzUikFA8UQd8o87HEhQCcPf9Ue0KuWW0c-RkgtruO1FDNuhgw4yxEe_Hkf8Trx7di7ZMjo-z1DOuOvMQZ9WsXXjiE_okjRpSwa2m5mh2T1PyTmJ8RsScZTLcrB1W9axezC2dxhSc8_YE0cCDa09TMYtwoAHbCktIGHm-JO2PuVBa3M0di7pKieDE0aYS75xPNtIwgxscomgzKSYvekr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJYpafkTlqxzAOhuaWs90mtvbqOk1cYPEZqXaC3NJIijjAfO7RRbzVriTmUKoU4vPkTbH2bIn7Ra8i-Ek1lQoMUfLtGl6QZzeMCAnRM8rC3s8UgvbTKp0utn0UywXNNkO0oBcVAw6_HDrHV53IlvxIU-OkM6xzSHeiG-1c_H6OJgZrBOOeFXE7c2tvdxRw4Y1c3qTjOaLtQDJi0qjYfTT4R753Hh97qkl2ILouEtSrFFOqkt2I4Tu-ftq_plgkZTvMExafyG1hhxrcWvau-oe05uB__h61NbBdkZU6ZvD9HygO57zrT46-ERXxUqxI0YueOsxKlk5Xn9fHL20k9s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=jDZLpZ88MbjjetvqwGSHy-JbyW1hNwVV8tv9l3eWox4hLdxaUVgnpmrxyevi9YuQhmfioWzEFDUY4U3agxS3qV1imDXFyEbahwvAZ9Bma7N19_9dEJYX7GMVRx4Apgi_njQo8DljJ7C9Gce-9jV17Tf0EiC5y7QoZtINvh6r_vLTGyQNHkyLRp69OJ-p42Qc5WPeRDmwpR9kD11hi-0jZg3-tmGALEisl2QfF87YJzIzRfVz4FrjEEEvyM1kCyyXok8gow6OH8mBXPJzqM9rHLEw_4htIzgytuz6s4YqOX8-DG3uoS3ZFBSgD4nBgbtLFUuWiKYEobeQOqw-E9yHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=jDZLpZ88MbjjetvqwGSHy-JbyW1hNwVV8tv9l3eWox4hLdxaUVgnpmrxyevi9YuQhmfioWzEFDUY4U3agxS3qV1imDXFyEbahwvAZ9Bma7N19_9dEJYX7GMVRx4Apgi_njQo8DljJ7C9Gce-9jV17Tf0EiC5y7QoZtINvh6r_vLTGyQNHkyLRp69OJ-p42Qc5WPeRDmwpR9kD11hi-0jZg3-tmGALEisl2QfF87YJzIzRfVz4FrjEEEvyM1kCyyXok8gow6OH8mBXPJzqM9rHLEw_4htIzgytuz6s4YqOX8-DG3uoS3ZFBSgD4nBgbtLFUuWiKYEobeQOqw-E9yHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eekejin2PvQ6YuAi0-ngHzXx9NMAV8EgZepzaEu1qhLMW22lX1jiQa0zHFIPDcjqWDqLAZ9YlSTZK0Usa52IuuWBFRt_pT_OwElvSEl56ijkdoX0Ym3wvqJ648lgP7SKruIbcqNnHIPnDvUw9yk7pRP6HdeNsQe_PX1frfng8gh7ROBeac-WpJtM3Q-lqm_iWjRbXpA-HaB9beeyKnI8kCNmDDPX2ZES1d24pwhEYXaTF1HxaWOsoBjMdX0Xczu9JT8a_u550VgfmRKE8MqJ6hqS9t-wiFaUwZo5jibu9Z9xWHZsklXwgHAmABbp2KLkCHDgCHbrlyYXgyIYW7c4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=RDQ1lDk1VVbNSEX83y9nSJK1JnzcMAAk_YH6vvTTBNUCbxJyJxWgydRJJc7ZuAyDBumZETzy3-m0TU95fVZqWkKcN-_aRuhxtPBLEPAnexiyx_T_K_9GhFXSPBGVHKub0UWqFOgLERzN1WhPWWFmzUo8dit_vXP25b7JTnnEcwvIkIUPFzTmbe87ry9crBDNUveqhg920cnKxUd2X7HPbHgMW24XO6J6iNIW3Edti_agrpenpaAdRk2Tp6oRNbIy7-qz5Xm5Htxic9-EW9yejwWe6b25awPwSsIuIz9ManbsYB3TjkykSHlhfSZnUe1ykep1WevW_q1xfLKU-MRwSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=RDQ1lDk1VVbNSEX83y9nSJK1JnzcMAAk_YH6vvTTBNUCbxJyJxWgydRJJc7ZuAyDBumZETzy3-m0TU95fVZqWkKcN-_aRuhxtPBLEPAnexiyx_T_K_9GhFXSPBGVHKub0UWqFOgLERzN1WhPWWFmzUo8dit_vXP25b7JTnnEcwvIkIUPFzTmbe87ry9crBDNUveqhg920cnKxUd2X7HPbHgMW24XO6J6iNIW3Edti_agrpenpaAdRk2Tp6oRNbIy7-qz5Xm5Htxic9-EW9yejwWe6b25awPwSsIuIz9ManbsYB3TjkykSHlhfSZnUe1ykep1WevW_q1xfLKU-MRwSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evel9zbqd4dUTwXtN396ZxiigmC95BeGXkOQsuQUftE86DHLAU775tuZhOz9BgcEaho-VzHfvEBoRhhgA9lB24QuBebubj_S6TdY3ECHTimHV7V7Vm74MyPBqS-F2VkrKZ6Q-zEptCZ63VgzxiDlVnocujaawMXLemhlFKvu-F0ATzx_-j0lf1bSpSaAZccUDfQymqfE0SFki8uI08C7OIEZAJ1hHQ-k0tplCuGe34OprE4H-8_MUHRuj-2MomH396AnuqVFKT6bXgm60qnJ_KmJ_UO6ubokZz8fwF9J1l5JGCsEgYwV5WymV2j8YBAx4fXpTPlOSgY3k92QgbwrHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2npZD_V09Qze2bG7lh2B9Mhk8vy8EMFfP8uXdqySJK_qF3lvploT5ohbS_nOKkNmnjaWC9gDboafcqor7It1tD4Sq830NHMKnK-HWWwhzZ4ZY1T8iPZqHCX5rKN6A2hSje3m6g2n2pVBBDjErK6U5yMkgGjsHMY0rmYQqW4jMFTQudDGhO1mw_wfM-28ahWtbFKqJz-uGjgN2s5mHijkpVSGycfQuo3bOUC1xerOw7upBRjd9PkFVBmX3OvcIK61HnVgbupbjL1Kcy0eD9RwKZ9mnk4PIEjMSPqPYLvTx3eyDVR_z5YRd4aNIKM1_ah2LPFTDdpNJeTP34tUGhpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pKPDCd5MUbk13V9UxJ1th2w0k59VVhV7EIq5A67D8oeu9GibrjLzXy5ri4spD2kvwj1WrH5loWpUsh-89LaObsMHVdtqqb0PO2KQQSydgGlW4OuWkH1bZsaFttFwzvWvmAL4XWw_8vIertidNGlyjZMehbXPYQOdl9sqWP5q8SusO9x_zZmq_0_tb1iswfj8-WK_HC1ngT-s3Rr7i_EpUSdNz_A-iBavdNniRYYnW6JkmZBogOEF5WkwZTJ4JGGs9ttHhUba4JzokGN4AO4J6SZJGlyS47ULkMyA9o7y4njaumlG47_sjculuY9I_n_ztuIeezlWQQtxCObSTFhYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G0B7l82FC4gtaCbs6qAO7XdXQFpSSnpD6etZ9Npiy0QlieJgpOQDlB-OO_wd3PV2KG-a4n1zEjeK7V189pcrCG8lPDhcc-skfLFPk1ob-YI4g5O2KD92KbLUbJIF-zqLJ0lr5to-_KybYvRgg40RhvlBFv-KOWfcAJjAX5c_vkx5bMsE_MTvsks-XIkQRKX2UABedZzR4i7sXuq_TQ7q9oAKDRhI8MJYJ7p5CBv2wIO5fAojzjl17Or0g3UrswYAI8UwM5YU8Ib3_Xp4Tc1Uaq-Km0UU7EDpXAYkleBn9LT5Qt7tkyIQtMkP4ZJ_BvqUvbpCv5zcvM2tDZjnepTJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eiQrmLC2bjcOa0NvuDP5JX0uTfF5h0p5m_bcJqTf4xaaftrWVOwe9TnNfAq3nQearLW_2VKyj1D1wgr22sG2yKDOVFfMlJTE5oN6MW5kRmG_S6APGUHVqUZeyttrXiSrQsNcA3gtQweAo2ZKzHUKwGDLyGhVAkDsxLI-M2Hp3-K7kDSBa7lyPSN1kqhmrkwWQ4gEpIeoKNat4V8RSZBS6veJjQFSOKZBt5lNSAddYLN9wRpOslyWjhBm1DJwVoXDMNJOlUEkgweBSv2LBk0N9q1WWu6BGV1q5UB3z1aIGRW8uHv0u2X_yWDIlwkBL6zWgbQ3OlDt3OOqLx4zDyR6nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=GjL5i9mttrICylyqclJKIEcg_8AyVB6T17wZoa9NglCZ3pW2T-5xpgt3Us2m-WXtPfb64VnRd47v03LJ7c8x3zAkqGIgl950MmMWdHrBTxRgN_73yCWvp_2fvnFW1w48TkibFrWjsCyzE2cD9gJEft9vlmpErhHAcBqiIFQDRpKzaUZqxRPGRegUW-WtaKI50hde2x8vDatzUnnrj7SVIx_P8Mrh0i7GGGO1_v_hkNuzEfJKwEtno4voBWtU1UR4ZLWS3miXYKhl4RbJQbtNvh22SNpoZUkdxrIO7v9L9U_zBpsjaWs-zKwabeeyqlbA0r10-rfn-BHwUE6xohM7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=GjL5i9mttrICylyqclJKIEcg_8AyVB6T17wZoa9NglCZ3pW2T-5xpgt3Us2m-WXtPfb64VnRd47v03LJ7c8x3zAkqGIgl950MmMWdHrBTxRgN_73yCWvp_2fvnFW1w48TkibFrWjsCyzE2cD9gJEft9vlmpErhHAcBqiIFQDRpKzaUZqxRPGRegUW-WtaKI50hde2x8vDatzUnnrj7SVIx_P8Mrh0i7GGGO1_v_hkNuzEfJKwEtno4voBWtU1UR4ZLWS3miXYKhl4RbJQbtNvh22SNpoZUkdxrIO7v9L9U_zBpsjaWs-zKwabeeyqlbA0r10-rfn-BHwUE6xohM7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np4UZsJeXTVdB98ketopXbyoa9i8wREUzkGtE8bXYplXVbffpJcGfpLaKOtygMpIPITM4jBEMud12hJE-pWJjryceyZXANKyOnbIfcTwupOpblJQJ-jijgRmT4zqmeLOLs5nZe05hXBUyJ51gsDf2xamUgQ_Mo845KIUB7yit2umSde9ZZHAEaOEbE8hng8kpMAAnzanvMWsy1xnaPisgvSsFC39s2CS9JZq2iV0CJmF3xxK62zmaZPrnxNUZ_ZXIO6CoJ-YLGhnEcZCyGAAYMBpxzAbxoRNnGpge4RSQLulgtU7srFaEciQcwfVrSEsDBNgvrFgdLh9_4Yy2kLyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_nYARu1MjzCSeu5L-4OGY5KscSqbLybuMTDAAz-ryBk8r46zTiXHn2Ey-DXmOYB1KDJDDMAQlLQHOektkDjSxiZ8eugsm1olwtmJGdPxW1wOFQgVsq51lOLA8pK0YPOjxcgSw7uhbLpeHKphE7aAnavUEedEXFHpKXXv7a3r9LqEuqzZFhN11VakOZD9YANJv1oq9FqxAtcuO9bragHQqdDTpyR2u6diGmteIGMfolWMXCYvEsufb7GPmAidaHxKo6gcuJ0OZwPhX0hWkMiR_aTLBrL0aQyHuqaL4QKEBxYNKKIhQPPtabvhuhJYqwQPr_0uGQxRjHO6Zov1DBD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OxrZodD36cCuxdGYVC656Fa_zHw3WMdmNLCb7PXpYmSV7Szld1fC_cIZiV2rSKFFgfG99EFOn5RZBJSCt6f4EjLI5zdaOLh1bQIamfE59q6FB__HeO_ySDfJdcdVUWJWUGo4WfMlOfLJ0zLPOaAoYOCOlayzqDs259EpU4qaAiDPiCOytiyaLtGtp0-Tt_rO6MGFhic3T5-q9oy8pPqy7zcPI7j2d518F8kmwgbi1O7suLykN0HVJd-Amaeybol4cnAJEgpPZX9zBtU1yUVztf1gVzQ1-z__xYnTqI1BWstOR8UOIfODbjgeaUeORT-os1IKfLl0o--PLawXeAzmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D9KiPwqUg9-pVelGzEFXWemBpS_ERdAeErPH-bUne0d7MFZzHIooc_3e-YuDn8j7L_zjNsykHwoLufx5wAvzrSbHFY5lLRPdy2U_TO-pQ2k1Dbzms6r67VkoPgANweOgidfU0037hQESNnrxyDeRbbMzYqcBmolpgbAyM1anCpE5u4dFEjq0cHgzIC7zYnRKLO1ZfTQiWE6ECpkTCipjfmsd81miNd6W367l6xLariAbvZt6JIdZESDOzj1RdclJYJJMaSwEy7ITg85KPXNX3l7WtH_KadK9lOu8lXGx7tr0CPvFwhuPH803RhQij7-VunzfAnxDKHzLAMesdy3Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ckny0-QVZ6eaEIFt-Fh0TRnczCmMhxY1VZl5dZuLVXzmbPR0AGgdiCKZYMPuMAxsHbkiHbs33yHKnrPwG8r_bfwZ1VtZJMNhUbITF-8TaeT5pexj-QVH4ibQlSOWwE9ftekj4sCZYTu60ZJHORAyuCrNoDruSbfKsBQj1bZ1uzUDPl67cKIgtUYXoG3TZczIr16eEmGpQ3MvwQL4HGUF7BOYvsXGIIOKnT6XVOF9WJeJP8CDUppAa4gErR1q0z0mVULkAFFFaBfpSmCaqyxnMJY3lpBsdRF6nmwtYBmTkT_A9j3DnhabePz9sFw4s-_Xldu_U-t_X-HXsW0qmc229A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihLr9RnSro0EefR79Y3vFUlFGK1mt-qNakIW5Or0SH74QIts0MKTIi4DZMGuOkEnQQSvaQZOlJIf123u256krlMSma2a712HOnOgAVFmtxj48moKU0klHlSUP3k9RNR_5rn3N4xQEDK71yOEi7H_jyYI9xauYBOUtcBut5EI3wiUSEbFkAF7PCEMsrUD5SCyqovSoIzkvhvHs0KgM-dyHaY5wrlJwPHswXD8pCFpQtpFyhraEA9noCuxEweeXuUjngndsEx4i_rZZVjO9iqO07GGvNRJj9VdZz14IVo4_6xya2SUsIgpZU8Iot5LoWBktZLdif3Rqg6Yj9n953BCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VGM2a7x9FlDvbwvqYYUrPZABmVQ0uWhQ2fXeyk1eJ4Wwa_sE3a1siqmDMwY3ot2P1SSUOkCZbkt5WYOA8tBU3JumSQAKw-_uCFZYJxTurGGDDU5FfyeZGmYTA7YSn0V-N-VpfFJNiNd0Dgc_BgybJ1aWmLWaQYPQHqWTuTWtGZZTRqCeJZMBzYppG5crDIWR7GWV3Sb9G5g5a4CG_ov7AiP2XzzUIjBpFCqV-OdpamoP5flGp-HnOJefK7soO_h-GuJctDd5AmcHHbG-N9ANskk2WBBWh1RPFb91vz2y5EiB-oc0v8YsG-qR7slMr-pV0I6IpOZTG9A2ZMYou6_Gbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_CnDwbfxAFgzj9SNDayaeQztzgozGUANmCPZz1r7nSdUORKeGDwAuS7PVALzSjFuNnnnu4YEp2ibscBVXEV9_2aYcGT_MVm6gkfrcmOWBMbs5-zYn18szXqSiNti4ipnaryzBl6ucWRYyLH8WXs9WgnifdkvU82EC_OiaQdLnCGb8iYU6t9Zf1-odJwmPYkfZZ-X8WIqsWvPyN__xy1n-NbbeYlxKDFsz-ThY8s5_U9BjU4pZ6oaiZsXUkah1yA2V0ixF7bg7edgYGsRXaDHs2v3wSaz7V5e-ZNdxeoalBjDgr29qEdYRjypUi6uRoL6hay3M1PsH3M2lYLfYkQVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCvoaGUgaOsyq0s5FqiGqzfhHBXlNpf7J4WP_LtFxB-jaKd-lJMYRA5eR8jkD_4qbmRY3lOfrZUPCy2E3NkholANtzL2oC-7rhwKhe3F-Br26L6pzg4gmzPHRV1Y_G3ZwMRQPII_b1V4IWP72vyDgGQEL_5_uLWspMdG2CNPTOwqtqsDNP1iHf3hHVTM7L5PZmfcElgGzZoXzWZpee4xxFEJejeu7gTHVBPQgfP-tP6aXw0ioY2M3KU5gB5tEqNRODUwCBV3gTe9q6U78ayPJ0HNqm5xu6Nzy8mBNGuSmvdxHIZKfA3n2vXXLOg7ghBHdwysEDqMB4Pgz5998vbRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2WoZ9c7C9j5WXoG8twuXdv1LZkW2OauApXSFrUXIJ_H36Vmul2kpsf5WiIKxdmjqcRF1UjYZOFxAxxY2p7-o7anRBKePreMMFJbJwWjV7atvzDQcytRnUlaY_UvQcEET2AqpNXzJb7tkAOIqsT2cRMQOCxM_qUttjuGiRVb-HGhDjRelks0TjWLsBlNeCCSQMH2W_VYdXGoFhJsVXxSTwvwlmricOBAhl5f3mLA8ml3Geu2lbOK0EzetL0R8KP9z_V-m2_yYLZGYXi8JcbqQeOQ3xmJrRC2qxvexqTdPRc1BUSkjlGJ9O_R6qB9XMHtOxImqGXNKKg1G74wtihqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mScoQOD71qBSAB-fep_sgVR31abpxlGzT8dKOuc0V028jVDcpczrsvPVZbgmjvamE0L6KfRCizFzVRhg8xMy_Pm7rel9dxt2hqwc7jEiTfk8UkZZYxohKzPC-mejjA6aFWGqeMa1UXulJouGeXppYUUz1th_f3dXtWLkh5-2mMMrZkHNqtd19bdxTdHgUcAL7WyUa6x7ftBPLYlGp19uPAwIu90WRZD-YoQjQJtKWj6UMMulGcAgZEljeRvNwpHPWOpb9FVWbQ06vBnpdY4sTSSqiiboRftQjNR5jzzbrRIkNaXLfpC3CL9Px0KT697Xfy1qY8eBJXTF6NHdd7eJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayC17KVYqybjiUJNvlLI11JI9_3AMcxDsTzokvz-xfUIjbTpGAbxXFcawX5l2a4f_bTOIJ8WABeShYbeVgO_IsaCgiAXGnN3mWEI1JsOGaDJzGEMq4WdLR8cbq88lyeXjQUaoDodMQIFXJu1j_fzofeA8HCs2Swxr72MhIt7p3OckzIsXCouadK9yOa2kZfnwm_zEIExzvdCMFQLTI2n5XbHnd_zQQO1ir5jCKetmLFuiLGIcq9MSyj4JqpkZ7LTmdkuk44B4CVHXt-ECoWcFZqZHLnvxDloFmcp89jHdBlIE--chPWZJRrGqMvYbrsHgfyi2lGVZ9V9PVu1vO3iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U96OaqgmZyLr8A2lj7UZWwK4sfPh9FK_Pohan1aC4mS_4G_zX5dD4BReRA-dluv8p7nwOraCOaLvngawl5es1dlrHQrooyxBopZgQvV_eyyXVoX_IGw9kc-sz1Uu1mhDpG_X5_8hL_akrVxRgFKZn9FaeP19fAK8c1aJDGa6hrqFbb4ZqTBKN5kZlNsfIEurwdieS9vv8--9kKOb1kdo1-AcSsIgO5bFD7vwx0Ho8FvDfI99LZirpRCzmDqh3vjIS2SIFjbnEy4O4606x-3K9e1CBp2CO7alGnVsDLoDwO-pyWmlb0qrkaGDg65HI3eyfjUx08AzqE8iFjCt1aiOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQDLK7WxNRUbpzz0wY-2YSq7CG_lWr6IjljT88ZGxpkR9WHtpu7yYm_ckUeg1y8Mi-D2GC_Uj19-hv5eDDOCTmvc_wAuMac6ZeMTh4_UhfHt3zkMZAzNnZLuBFl3Y6Nb_lrRFBxzaOmhTqaOMWwssvr1eMUHcCfcZHy6xKO_wVkHIHrBq5eqtox61X-O0XLoFo0Bppw7HlJWYcxb9WKDwfnWrcdMLTxYN3-Dohv6YCud51wYzxEXcCEVM5rTPXE87x8cHoNZ1tNnhJqBbZV_2jO8VogcRvQmTnbjLLobOaQNkvLKgWONgaYbLZ-qxxNdoGFE2jPMzxxWmZ6SWHRQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHjZN1vtEtLqUVfo4YqS07o7dPobXWySSqI5asf3CsiTXCVcTAF0E_JzBX-xFZdzRNemRM8fk_yMgzDje0JsbnTWUN67MX7PK0GPPiMIUfII2_BmBOs5mSrcjCrF6qjQmT4TjqsPMPpqTOx0wzx05iNiFV_fH4vIr1NUkp3v5IhQ5Qkz2SN_MK47RnK1oaDNnDXPJCBt6bGl2gxBEQPwLrzzzvaNfcq6T_zISy4r__Afmerz5nXIywRbuRhTEEWzAYrgl9PWNObY8PXKf3Gpb3RLUlBHJzJkHou3-TSOgdy34u9IuiggFjFDXaexb6mmxFKfYwQ3hdCp4q0viOdoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYW3bNw94p3O4ztNjygOra0vPiaNmg8FvnvvTCrun1fibp3vkn_cSZTdUYiq9DTH9HeMiz6XuivxBtoe5sWPP8G5ReFrRTuft5dfWbkweAyPOPllojnlWKJzJt92ornWyPFcnOFoqiNncn3LZbu-kKvKy2-dM0rnoCfx_gkX7hw7KASVWATda5IlRklPAd_5vbxMtpa3wvGs5weDM1G_rde_6aIf9dxFejgMshusez1hVGjy0rfW30t4OxJg7TxceJ0f-ft_Xurn3ROH8TvpunaQUw7Waqdd2OCar__6PmPBZaW9lNtYZNsiH24EqLd9xvOq8M05QOvHL5eediurqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoLSn8rBXCsnKn9ocYuWlZc1vetGumMFKLwj84HnTtedYv1M9OqU3OUngtuOikDLWySkz-_PXyxxBXsEdsSyzGHEwwzIYMq1S66yFKZfVhDI8sH4zgkQJlUQpX-Vi_nnB5fpJLykENTtwus_08vbDZiwivESRCvduwqrXDp0cSaC3Lu2TE1iOeuDC7xCNJX16xvPm267mmL9HpQBkI-OKqtas27DePstYyxnXaNy86ChcZm7gcqFPqYiyjHgQGbyfjQWnM8VMRk7kRI3o7KDdrn7XeTfkcaf59COFOQgFZmCM6NDBsSDAvnm-mFCFnmqhR4zpwDv9lRuAj4zMMTUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
