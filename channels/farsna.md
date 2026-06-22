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
<img src="https://cdn4.telesco.pe/file/L5tMIbqpAf5dILxJnuZbLcyH7kLhyr1ZyyUiwPPDo8TVS8jOP9Fd7QqIhpDd7cgpI5GE0W9IFolxedC2etQYpLP4hBSgiUwJMZeBBmnz9kh02n_xFXtH-XpiRG9cND4ZBGkqYYwx3VOrEJ7h48RwJ-dqkC9T3Yf-vWnjaY2OVk3SwuPXMnte0bAcCL0zgiOucJFA5L2WUI-lV6rc2ikgshCnhAcseRUO0WxY3I-U2HjwUg0CqvI6d2oeQ68s3Wla5l-b0hy-oeNy3qEyBHt_-cpvbSIoYir9yNe66wlM5BfD5i84gEOv2XHcWMUba8FErYV_2N2iW3BCOTnOLS-meA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-444092">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/444092" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
|
شب هشتم محرم
🔗
سایر مداحی‌های امشب را
اینجا
گوش کنید
@Farsna</div>
<div class="tg-footer">👁️ 23 · <a href="https://t.me/farsna/444092" target="_blank">📅 21:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444091">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 336 · <a href="https://t.me/farsna/444091" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444090">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">هدف آمریکا از «رفع تحریم نفتی» چیست؟ ونس پاسخ می‌دهد
🔸
وزارت خزانه‌داری آمریکا امروز با صدور یک اطلاعیه مدعی شد که یک مجوز عمومی برای معاف کردن صادرات نفت ایران از تحریم‌ها برای یک بازه زمانی ۶۰ روزه کرده است.
🔹
پیش از این جی دی ونس، معاون دونالد ترامپ، رئیس‌جمهور آمریکا درباره انگیزه‌های واشنگتن از صدور چنین معافیتی برای خبرنگاران توضیح داده بود.
🔹
او چند روز پیش در جمع خبرنگاران تصریح کرد که تحریم‌های ایالات متحده علیه ایران در سال‌های گذشته بی‌اثر شده بود و واشنگتن به دنبال راهی برای رصد شبکه فروش نفت ایران بوده است.
🔹
وی روز پنجشنبه گفت: «صراحتاً بگویم، ما این اقدام را امتیاز بزرگی به ایرانی‌ها نمی‌دانستیم؛ ایران هم... آن را امتیازی برای خود تلقی نمی‌کرد، چرا که عامل بازدارنده آن‌ها از فروش نفت، تحریم‌ها نبود.»
🔹
ونس اضافه کرد: «آن‌ها بدون هیچ تخفیفی، نفت زیادی می‌فروختند، زیرا تحریم‌ها اساساً ناکارآمد بودند. در آن مقطع، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به سمت چیزی شبیه به سیستم بانکداری سایه سوق دادند.»
🔹
معاون رئیس‌جمهور آمریکا اضافه کرد: با لغو محاصره ما در واقع قادر خواهیم بود تا حدی ببینیم که سیستم مالی آن‌ها پول را به کجا می‌فرستد و از کجا دریافت می‌کند. این یک منفعت واقعی است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/farsna/444090" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
دیشب سربازان ایران در ۳ جبهه جنگیدند
@Farsna</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/444089" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ed475c50.mp4?token=djyw5Z-Db7K-TojtK4E-K5uUBvUWQsMNiDupaENSP8JnWL1IiF8ySirGWwfdFuexumhqxpYsLLIpk6wYUd4bA820JXJ5Oged3csII_hYhdIU78cCd2sziVSctUz3yKv_7OmlomeWSL-fvjysh6-_f03x2OF-w9gPQfzY1pKCieOHWbWIkM0Yoyc4DZGsFEulUaIY4t0Q8Zlq98S1DRgEaafM2QXf9bT9hd1nVcZTGcn75OC2Vi1mgG1LOdHyhz-sweO8SyIGhkyx3TtiXEsDJ_lnlIyuyRR2ivLlwOpsMxlO1SuuWAxpr7wq7SwKhS1oew5Vd73084DoSxaGnL849w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ed475c50.mp4?token=djyw5Z-Db7K-TojtK4E-K5uUBvUWQsMNiDupaENSP8JnWL1IiF8ySirGWwfdFuexumhqxpYsLLIpk6wYUd4bA820JXJ5Oged3csII_hYhdIU78cCd2sziVSctUz3yKv_7OmlomeWSL-fvjysh6-_f03x2OF-w9gPQfzY1pKCieOHWbWIkM0Yoyc4DZGsFEulUaIY4t0Q8Zlq98S1DRgEaafM2QXf9bT9hd1nVcZTGcn75OC2Vi1mgG1LOdHyhz-sweO8SyIGhkyx3TtiXEsDJ_lnlIyuyRR2ivLlwOpsMxlO1SuuWAxpr7wq7SwKhS1oew5Vd73084DoSxaGnL849w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اجازه نخواهیم داد [دشمنان] حقوق کشور ما را نادیده بگیرند و سرخم نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/444088" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dec6eb76.mp4?token=r9ttaQHuRG4PbHPlHStDGIGHR8P8P36PoOTpUBEKIQDG1tNWSGt0IQO-YohioT5W7VRlIQBjcn7jOXJm5744ZC8Lc8ZWW--_yxQ9vEXx0W81AKfOmC-Nzw1sioaJXAhCg5h9cUwpR1idWi2OYcFm1vNlwtT7CakU6hzR0pMObEb9Q7SIl41gsqpeDrb8wQbjIop8e7tXys1u9rFe4dVipI4h2azxt5LiUC8W8wBa3LbaPu1pG175DW_0_ERexPFyqrIWLeB3_IB2YVyTQghUn9ngrY7AcCT2UKWpqpbfi9xzEM3228MfHzuEKdhToP2MoSZZJ0DTBgxff4vmY0iClg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dec6eb76.mp4?token=r9ttaQHuRG4PbHPlHStDGIGHR8P8P36PoOTpUBEKIQDG1tNWSGt0IQO-YohioT5W7VRlIQBjcn7jOXJm5744ZC8Lc8ZWW--_yxQ9vEXx0W81AKfOmC-Nzw1sioaJXAhCg5h9cUwpR1idWi2OYcFm1vNlwtT7CakU6hzR0pMObEb9Q7SIl41gsqpeDrb8wQbjIop8e7tXys1u9rFe4dVipI4h2azxt5LiUC8W8wBa3LbaPu1pG175DW_0_ERexPFyqrIWLeB3_IB2YVyTQghUn9ngrY7AcCT2UKWpqpbfi9xzEM3228MfHzuEKdhToP2MoSZZJ0DTBgxff4vmY0iClg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
🔹
مذاکره یک‌ روش مبارزه است و دوگانگی در مذاکره و میدان وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/444087" target="_blank">📅 21:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f870b96bdf.mp4?token=CPBrS9EJfdlwuGYlBK2UD83BShpi16H2CpHIzNNLusp60BzNIW0X1mpM5osPKgu4esvvw7xNPjPDfua2f8mh8E_zrCqWHoeW1xgGG9pzsjCmW7u87UmFqKQu_YmEfF9t5uCrt2Iauwbb7dS3KlU-8gcozWLc7fyFZJ83TTlVWGbMyhfo6btYRozlY4TPgs8Iuk9WdHf7p38rpGbUC97hoRKBhLzm_z0mGIABRPDyJcXr5UkKgUcsFVOiM7LsYy58uW7xAMK50JPxT8aH8Q7PPWL5TlWVEyP9ezDFg19RPXClHeVRZubfP3ka3e0J6FzhhjPQaJjP9uwKmtJd0XvQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f870b96bdf.mp4?token=CPBrS9EJfdlwuGYlBK2UD83BShpi16H2CpHIzNNLusp60BzNIW0X1mpM5osPKgu4esvvw7xNPjPDfua2f8mh8E_zrCqWHoeW1xgGG9pzsjCmW7u87UmFqKQu_YmEfF9t5uCrt2Iauwbb7dS3KlU-8gcozWLc7fyFZJ83TTlVWGbMyhfo6btYRozlY4TPgs8Iuk9WdHf7p38rpGbUC97hoRKBhLzm_z0mGIABRPDyJcXr5UkKgUcsFVOiM7LsYy58uW7xAMK50JPxT8aH8Q7PPWL5TlWVEyP9ezDFg19RPXClHeVRZubfP3ka3e0J6FzhhjPQaJjP9uwKmtJd0XvQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
🔹
مذاکره یک‌ روش مبارزه است و دوگانگی در مذاکره و میدان وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/444086" target="_blank">📅 21:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8516b58a9.mp4?token=TZ_7WHs9G6cgt6XmPptTK-tv92fjB_0942UxCR60K8tkGvHcOEBw2NP_QIGMhQQJnVXlXHu7KPF16075H_HyAbKtvOosQL5LAVAJs8ZJBZJHAzRLyQwpOr_w_Sv1nGDSbls4asSVU1PhD18OtnYkc34qEJJ0p70f5iwjVtpqQ3j-3fgVzM6lKxKxZYCmDJXX_giiNR9ngCL0MTmOMiWREzwb-dmJFKfuFZiqcJ4Xy2nK2AP5vdvSAUIlDQ0mpZDyrsW7qyCWploZdkNaCbpbaeZxHHRLUVcW-e92RXv99Coz0m7vWac-eEcwPHBUo_ZyuU48hcfyAYGUt8dqYzE0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8516b58a9.mp4?token=TZ_7WHs9G6cgt6XmPptTK-tv92fjB_0942UxCR60K8tkGvHcOEBw2NP_QIGMhQQJnVXlXHu7KPF16075H_HyAbKtvOosQL5LAVAJs8ZJBZJHAzRLyQwpOr_w_Sv1nGDSbls4asSVU1PhD18OtnYkc34qEJJ0p70f5iwjVtpqQ3j-3fgVzM6lKxKxZYCmDJXX_giiNR9ngCL0MTmOMiWREzwb-dmJFKfuFZiqcJ4Xy2nK2AP5vdvSAUIlDQ0mpZDyrsW7qyCWploZdkNaCbpbaeZxHHRLUVcW-e92RXv99Coz0m7vWac-eEcwPHBUo_ZyuU48hcfyAYGUt8dqYzE0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی مقابل اتریش پنالتی خراب کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/444085" target="_blank">📅 20:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7QTDWrOz3vJRaLM6-m1UgqYWMaR24fnrV0i7voU-GlFMgP3Slyz2KEuuePevDBXjjJohBflKSzHfTicvfe2mLu514r-XfY7cTNPdHGY5QSldnM3g4korg6eTwpboR8EusPkOa2wSgEcVtn6vv1VJrbFT3-VIr7H34IH8GIPstUc7XxiFV1o8yPdkjSrf9t8DKSx88dnwrDo4FRJw9zTW7Qga8NA8dffvm1TlfiO1woUdHPAFB3MFBEstlM_ql_XiD9xh6s8bQpgKH2YOR1XmKxVX9YD6gSV1T_q37EdeZhgB8lem3U7xO9yJ6QGOwRCheQQSedAh-sndBbShNTqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: ایران با بازرسی‌های عمده موافقت خواهد کرد
🔹
ترامپ در تروث‌سوشال نوشت: همه کاملاً مطلع هستند که ایران با «بازرسی‌های عمده تسلیحاتی» جهت تضمین «صداقت هسته‌ای» در آینده‌ای طولانی موافقت خواهد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/444084" target="_blank">📅 20:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1svzK9_Q1vH_z9KVsbaoEJ8GETIi4_NeeVjHcS28XmWO1mWL546QUBOLHaF9Nicc-Yax7XZ3L7l3H2eEmlxd5-AmlVEljH87Uz1qm84kXNeWQFS2l6_oyPtzAkxVKUriNexs2u5B-F4gdvTM2zpGRK2HRR7yp8g7yoVMlwoOMZ1yubequmr4FnXhlVtDCwUR6M-KGUxO48K0P3CNq3dNJLwlFI3o3FZWctx4qqEeXltM5Z4XlQgqb-Q8Bq3GHo9vd5jtcsjryarc7z2II7YoXr-WD2vv5511u3ybsDiT6nSzP5SUVI5poFBxW61YUFmW90yJHbpH0tWG9LQChS4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید خودکار قراردادهای اجاره با سقف ۲۵ درصد
🔹
وزیر راه و شهرسازی گفت: بر اساس مصوبه سران قوا، قراردادهای اجارهٔ مسکن که تا پایان سال ۱۴۰۵ منقضی می‌شوند، در صورت درخواست مستأجر، به مدت یک سال و با حداکثر افزایش ۲۵ درصدی اجاره‌بها و ودیعه تمدید خواهند شد.
🔹
مراجع قضایی نیز صرفاً به دلیل پایان مدت قرارداد، از صدور حکم تخلیه به درخواست موجر خودداری خواهند کرد.
🔹
این مصوبه با هدف حمایت از خانوارها در شرایط ناشی از جنگ تحمیلی سوم و هم‌زمانی با فصل نقل‌وانتقالات بازار اجاره به تصویب سران قوا رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/444083" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6db886dbe.mp4?token=trPPyxSRLT5_WpiyOR0aQrvofr-TSQ5T1yg6ggCkdNn2Mm9akivzLzwVisKDFfCSNr8dUwQvSli2yqkbTrRCZcsrT8KyezK3Ye5Al3fPYBzlkrzViWcVtdILQtDR03C8lPJZAhkh54E84BCXv0EWycUAFohLpJQq3wZUVnyCWITBwByrk66upX7Z7IoMtgnN5QoUvNBxiplq2Srff9cngWE2Eb5y17Fl_sxV5TouS2CPe5V8H5uTTmsvR1wY6YusVHUnGMF30cYvh_wwRkQ_DJHzW69ctZjijpnLNZuC3nUUCFb6FhcgmRffznU6m0uLnP2IO0IM32q0bQIdRNuIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6db886dbe.mp4?token=trPPyxSRLT5_WpiyOR0aQrvofr-TSQ5T1yg6ggCkdNn2Mm9akivzLzwVisKDFfCSNr8dUwQvSli2yqkbTrRCZcsrT8KyezK3Ye5Al3fPYBzlkrzViWcVtdILQtDR03C8lPJZAhkh54E84BCXv0EWycUAFohLpJQq3wZUVnyCWITBwByrk66upX7Z7IoMtgnN5QoUvNBxiplq2Srff9cngWE2Eb5y17Fl_sxV5TouS2CPe5V8H5uTTmsvR1wY6YusVHUnGMF30cYvh_wwRkQ_DJHzW69ctZjijpnLNZuC3nUUCFb6FhcgmRffznU6m0uLnP2IO0IM32q0bQIdRNuIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها دروازه‌بان تاریخ که توپ طلا گرفت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/444082" target="_blank">📅 20:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu-iZYVrYVuQZSTHtIcah5VxcKY2FtmFFGFzfx21UIYofWP4-whKTTZAuLbwSX8ToTaBaJ9qUjU4zvl6Ow4aUa5GmpAjIgmW-v3GInoU96s9wcOwZf1yVvTa5_YwPtutqBXYEuYtrWIYg32yqQSyqTaoRFxoFrL3MK32SKBQWIdP8ICBpxZ0yNgDZBGnT1aeacD_G3swoaleMFM6eAlCveeZqKBr4zBu7mxnT-ao5PhbS6p31Pl03Cifdp1pAMGmS5kvW7DolgDqaev9FyM8GbuAeMepjjQY4IVRZOLBKnxh6d6ocNP8JMywz0VNiViDDSitV_bQzT2KKtvlvSwtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هنگام خرید ملک مستأجردار این نکات را فراموش نکنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/444081" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajdsQumW6b0J93tEf2o3w6vNKaVOq65rm74mCH28cXfmsVF7ncA64tQqxCtdna32GuG8YvbosmFGNQ2HmZkkgHWrXTc0Tm0L-dwqilER-ssX8n-Pw8VUrHNFREa9X3Ti_uYVXEkHRWvF0vndm-wBwBXAnjEuqewfSCaxFQkxsObDvuGuIf3Yk5jt8bspIlLs5G2deVhlEzt3UD1YgxFFwz-nX6L96kK154XtZtp7jTwPqn2Pmzh1IsoCmFm8mrfg-iHJeTkrFWD50bG9lyJC9wfWOcPV9eavFA2eMnhUunOHAfotPJDyQSN7aSzkbZSpGy28hPyvLD3nKKcfI0mpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سفر اتوبوسی تهران-کربلا مشخص شد
🔹
رئیس اتحادیهٔ تعاونی‌های مسافری: قیمت بلیت اتوبوس در مسیر تهران-کربلا بر اساس نرخ مصوب، ۴ میلیون و ۲۰۰ هزار تومان تعیین شده است.
🔸
همچنین نرخ بلیت اتوبوس از تهران تا مرز مهران نیز یک میلیون و ۲۷۰ هزار تومان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/444080" target="_blank">📅 19:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbd067a6.mp4?token=V8E_Edqy8ECo7Cm0O_274bkkq9CUUxhk4-8FxPYv9bcAziJ2olRHRhSNUPnkTpksLwVE4_1Mm3Ga1HrCdmrRUPYOIab9anF10pcyZ_bc6Y-Dp7mVmNlA0Hi-Z-wANqWs55R1HYVsxW10t_l3ux0cGYKkMW486NYh9ZoGyVrgllyek-S5C3n2-FJ0fjgrgRoSIHK8PTV00qdtFdtrUjbNHxMGcdhwpKrwnQq6V0tltl19RQx-9LTWtY5rC4sTUHOvYbRlHPyCUO6APefD-wKbTboHY12wlX2TKtk0f8dBzvbtPZSHSUDMrjBDks3kSNgnWZmk8M820SYxltBmoSehcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbd067a6.mp4?token=V8E_Edqy8ECo7Cm0O_274bkkq9CUUxhk4-8FxPYv9bcAziJ2olRHRhSNUPnkTpksLwVE4_1Mm3Ga1HrCdmrRUPYOIab9anF10pcyZ_bc6Y-Dp7mVmNlA0Hi-Z-wANqWs55R1HYVsxW10t_l3ux0cGYKkMW486NYh9ZoGyVrgllyek-S5C3n2-FJ0fjgrgRoSIHK8PTV00qdtFdtrUjbNHxMGcdhwpKrwnQq6V0tltl19RQx-9LTWtY5rC4sTUHOvYbRlHPyCUO6APefD-wKbTboHY12wlX2TKtk0f8dBzvbtPZSHSUDMrjBDks3kSNgnWZmk8M820SYxltBmoSehcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: موفقیت تیم ملی حاصل وحدت و همدلی است  رئیس‌جمهور درباره بازی تیم ملی مقابل بلژیک:
💬
شاهد بودید که چه صحنه‌های زیبایی خلق شد. بازیکنان با تمام وجود تلاش کردند و سرود ملی جمهوری اسلامی ایران را با افتخار خواندند. امروز ایران در صدر اخبار جهان قرار گرفته…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/444079" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_lvYYe8QI5B7wVhL5UCK6KAWnlX_D2AsHYYJTyBzq77032-sl8QS6cHHeWpfilI4F8jbrLGIGqqq9VM316MOHy30zVvkvUEKChBOKpdQI_XPUvFmic7RjrDLMa7xfKP-cqpRPPedaTFwJLyCgNhiIG8Jat6jmuFLLHt-Xk_rOQ356Dvnz2aW83EH6X2An8kRXWjOzm-Pl-AV7ZXxrp83l-qcHZpnw9aWEEGeG12ih5h5UP2aXiTeRc97bdDNz32nGd1wepPLcVIMBXw9xEIWHv2VNvV1XDm04DEn3naHvtnifjLDRl2nR9Qa5Fz2LGoornraCx_xT72BO80DFp9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب کامل ۱۱ هزار ساختمان در جنوب لبنان به دست صهیونیست‌ها
🔹
بر اساس ارزیابی سازمان ملل متحد، رژیم صهیونیستی در حملات هوایی و عملیات تخریب خود در جنوب لبنان بیش از ۱۱ هزار ساختمان را کاملا ویران ساخته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/444078" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند
🔹
گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند.
🔹
پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/444077" target="_blank">📅 19:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOWDbwCAYqFcxvELghuEds7wEUie_Gn_uInYyzHYAPtJbp7sO7KsspcJWj4TSCmXRKn3LK-AAe3xdYcpMZ7CwlKFJl56TimnCG0nxVwZKzxtFlTHV6y2fDcGzi8kVJ0pFapHsoUgxAdk47BDqogRrYXgWWets3k7rNUbARw3QGuJoX9Ibio5L-N5yeyKE3AXOOq6XqiNpwpAFwY6iIs__QqFiMFhPfetajLCGT1uJiZ6Vxsi7MyGousNxUiCjrIZzT6YGnsWUn9tYq8_GiwbkI_xM7s_HDa0epQS4hzIdRHGV0dfguZwBQeCi4e8z6aiY5qlV1JO07Ts1xpFFQBCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/444076" target="_blank">📅 19:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad93d5844.mp4?token=J6GbFr7OOZV-qLGVg5Q2oQrL_2nPiTwn0smpEv7sCShFtXnsz3G-HWNGoZG5iUAx_1XAUd0jVniPW33Nd2mmqt-LKhVmfB_LB4vIVBIYgxqOE4eKKS1rgp4mFkQD7TUnAzR2PZUk442SmIhm2jvmGVCZKPI0VW98MMCbCnCp8R-wbGtv6UK_HEDYhL3gZ-K3M692ra6CoUcBMgB9nyQx-KhjH1y1ZQGcpk7yNfv0jvCcZvusnkdRGmrolXcWqoMiecPkdcPjsUtfp5PI_uwNXZ6bkH386KAJEX9U5spduWI4YWooUSIBV7tMUFKrdv1M3IPsEMUJk9IkgalZJkVDLllHs93eljmuY95Q6R_9T5vIFMIWmHgrqi32yRj7R2vh3lOrA11dfV4LQUb8iSJHqsTN_HmAEohX0RjoqRvFb22hAffWRd4j-QJJ83lxl6Y_wB0VDFF1-3OHeNizBo7-FFgySlVSRdNb7amg0e5eLn-O7HMkKzzR_JYhesx74j0zCMwvNRq5nHeXIJl-BvMOXHWRWZSRqtO4mUMXoiSCFMhgApmKh3nxscvFf8PXMa9gOYn2-w7hmUjWc7Pm8bZwsafMqYoUY20-SqwcRNTlQgN8WaCm6IOuh9MmVBQj0LGB3oR1q4YaB9ghIAwAXbz9JeZVmOp9YvrjggbAh6jp9Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad93d5844.mp4?token=J6GbFr7OOZV-qLGVg5Q2oQrL_2nPiTwn0smpEv7sCShFtXnsz3G-HWNGoZG5iUAx_1XAUd0jVniPW33Nd2mmqt-LKhVmfB_LB4vIVBIYgxqOE4eKKS1rgp4mFkQD7TUnAzR2PZUk442SmIhm2jvmGVCZKPI0VW98MMCbCnCp8R-wbGtv6UK_HEDYhL3gZ-K3M692ra6CoUcBMgB9nyQx-KhjH1y1ZQGcpk7yNfv0jvCcZvusnkdRGmrolXcWqoMiecPkdcPjsUtfp5PI_uwNXZ6bkH386KAJEX9U5spduWI4YWooUSIBV7tMUFKrdv1M3IPsEMUJk9IkgalZJkVDLllHs93eljmuY95Q6R_9T5vIFMIWmHgrqi32yRj7R2vh3lOrA11dfV4LQUb8iSJHqsTN_HmAEohX0RjoqRvFb22hAffWRd4j-QJJ83lxl6Y_wB0VDFF1-3OHeNizBo7-FFgySlVSRdNb7amg0e5eLn-O7HMkKzzR_JYhesx74j0zCMwvNRq5nHeXIJl-BvMOXHWRWZSRqtO4mUMXoiSCFMhgApmKh3nxscvFf8PXMa9gOYn2-w7hmUjWc7Pm8bZwsafMqYoUY20-SqwcRNTlQgN8WaCm6IOuh9MmVBQj0LGB3oR1q4YaB9ghIAwAXbz9JeZVmOp9YvrjggbAh6jp9Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مگر می‌شود به شخصی مثل ترامپ اعتماد کرد؟!
🔹
چه کسی می‌خواهد به آمریکا که دشمن آشکار ماست اعتماد کند!؟ مگر می‌شود به آمریکا و رئیس‌جمهور پیمان‌شکن، متکبر و فرومایه‌ی این رژیم اعتماد کرد!؟ مگر ما با تجربه‌ای که داریم می‌توانیم به امریکا اعتماد کنیم!؟
🔹
همانطور که مقام معظم رهبری فرمودند، تعدادی از مسئولین، دلسوزانه و با حُسن‌نظر و مبتنی بر تشخیصی که در ارتباط با مصالح نظام و نحوه‌ی مقابله با دشمن آمریکایی داشتند، شیوه مذاکره را برگزیدند.
🔹
این امر به هیچ‌وجه به معنای تسلیم در برابر آمریکا نیست؛ اما متأسفانه گاهی برخی افراد، بی‌توجهی می‌کنند و سخنانی بر زبان می‌رانند که دشمن را خیالاتی می‌کند و دشمن در توهم وجود اختلاف و انشقاق در داخل کشور فرومی‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/444074" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX1QXngigU8l0wh06j2RfPcEPpr0iwoEuYoJn6pa6ZWmefyW2qkQOa40MKTaZsCaUXshoGhUxZoes4xWyY0Trbg3g8MMQZFArY8DKeBGex__M1QJWeJcAX50Wf5vCwr0m57ZL1ITT8WUa3yYZnvZDSE9nTiRwJE_6Iom1YWvpNv7A14wyPIw9dCWAdqPmGcMUmHviJME7yHdyG1Zf89KROuPNImW_HL-myRFxTp9bLscPzdt0asLnQT3Q7f4gDXiB9faKve2scufLNdKD-9SRQLjCpCrCWe6kh2aMiYqs_s27iR_FBwJ0zCgV8feWXi3AfWo6CF1f0MfpD6eLvMXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم عمان شد
🔹
رئیس مجلس به همراه عراقچی، وزیر امورخاجه، برای دیدار با سلطان عمان عازم مسقط، پایتخت این کشور شد.
🔹
گفت‌وگو دربارۀ تثبیت ترتیبات ایرانی برای اداره تنگه هرمز یکی از اهداف این دیدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/444069" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
ونس مدعی شد که «ایران بازگشت بازرسان آژانس بین‌المللی انرژی اتمی به این کشور را پذیرفته است».  @Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/444068" target="_blank">📅 19:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VvAGC2WdexyO-PeXTjXi57GmHTQ6VLTm6UmMAHwx2fn9FZeNfkglplnpAGTgwsxtmqwSdaFzsuU6Ji7CyESZoE6_4x7FEcQUeg4xJTj1dwLcEvM7bNIMBs0ofeekbMF64FKcWrVQO4tanAawxSZq8Gh4DjsR6oGFNgrkY8m3lCbzqRks-1ZfOohvoeRr93alka_9xSK8ivZHxX15HEK3nNyr3HPoUIYx3pp31Ep-5j2xBcerSIsRcG4OJKAAAhdWSkRYQakMORxIf65iF5pOWw3RLoVoP5FPCaqBmeJRsDBmOV96EKhR7tgITimAx0H_yZ2ok9_tZsKH714-K9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوای محرم را از قاب فارس تعاملی گوش کنید
تازه‌ترین نوحه‌ها، روضه‌های و مطالب منتشرشده از:
◾️
مهدی رسولی
◾️
میثم مطیعی
◾️
حسین طاهری
◾️
مهدی سلحشور
◾️
سعید حدادیان
◾️
ابوذر بیوکافی
◾️
محمد اسداللهی
را می‌توانید در صفحۀ اختصاصی هر یک از این مداحان در فارس تعاملی مشاهده کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/444067" target="_blank">📅 19:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۴.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/444066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۳.pdf</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/444066" target="_blank">📅 19:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1uMqZhzwm0OxWEVqLJ7SpGbMB6eLHjY4srh4wSSGSLyKA3Nm_y4iEAJBwiinMHIEOfIMEJSHAOnXgjpMbhW1f3y79spbZXFj4WFmCwsUZFH5iVV8Uz1LQntdNwRifUhfk1qFSIE5JBflv18MvTuPEiv3LyaSlODzQgRdPPM9Qko6pVNyqSTnk7B7ceXGrXyaCJ6ikqgPegLzUdFyrq5JZqohajw3GPrElJEe248_s40dLvb8LRAzyNcK1Kvez7QabwADzLMOX9eVEUGldhlebzuL7y-vwB9jtzC9cEkou1-zvSX_ppAmIkuTnHthx-E6t9CiJ-HzcTeW6zk6FNc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: موفقیت تیم ملی حاصل وحدت و همدلی است
رئیس‌جمهور درباره بازی تیم ملی مقابل بلژیک:
💬
شاهد بودید که چه صحنه‌های زیبایی خلق شد. بازیکنان با تمام وجود تلاش کردند و سرود ملی جمهوری اسلامی ایران را با افتخار خواندند. امروز ایران در صدر اخبار جهان قرار گرفته و از ایران و ایرانی با عزت و نیکی یاد می‌شود و این دستاورد چیزی جز نتیجه وحدت و همدلی نیست.
@Sportfars</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/444065" target="_blank">📅 18:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe4SfMzlzD07P4ulO0H_bwU84zlz6pySugauzSW-HUvScQ41sEMeeO9oj6bRYqgZtiLrNJY5cz_DVRq7KOmvcElZT7U2IfTD0uaSre4eoiuw_K_nsINFLFr02HPMW6RvrV95F6RskyX4Y3hq0YVzcRlLnP6Il0U-NV37662jzj6_mgRSHTRR0ZnyHfNuZe5zKC7MKN4c8Fc6BL1l3PiZaAWa-YkgFp18g_b0wl4Ix8OOCghP8yRho8Hsr1oaC8iGdIV59hLjyvKcBhh8N-FnlZoC3x0VMcPzE0hn92JYydmVMmSqW0P2n8SoiIG397SA-OOA_jFJIOS_RBdBs1ue1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران چطور در جام جهانی صعود می‌کند؟  سناریوی اول: پیروزی مقابل مصر
🔸
صعود قطعی با ۵ امتیاز؛ ایران در این صورت به‌عنوان تیم اول یا دوم گروه راهی مرحلۀ بعد می‌شود.  سناریوی دوم: تساوی مقابل مصر
🔸
ایران ۳ امتیازی می‌شود و همچنان شانس خوبی برای صعود دارد؛ اما سرنوشتش…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/444064" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzELcmq54JL_LrQdeYoM73aGroSmFYGGnbk7HaPF4K2B5L-71DoUILPYc82Z2z48a-_250LzBn-8AsSkYr099GgdnMRbBOkKLR_QLqDgRKx5e5Q4QJE6zc9Kiq78ucJ0BKY3oqa76l_SdioKRmcZ0jwim6RlT3vKSyDkk55b7jKlhsfTacHKRIZjW3A0NUKJ63ZMZ9YvclxQUzYZapYxkvLY16-ULXuF7qcBUPm5AakL5Ej059R5ziv3rR3H8Gn1-jvLkrgihGDBEZ_GdkhN5svu-SMFk4RlU-J6V7tX_Kk-gFxawI3cYxNW7aVCL09-qV09RShdsJ5TcSEh3F9M6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات دنبال تسلیحات هندی
🔹
رویترز: هند و امارات دربارهٔ یک قرارداد تسلیحاتی بزرگ در حال مذاکره هستند که شامل موشک کروز مافوق‌صوت «برهموس» و سامانهٔ پدافند هوایی «آکاش‌تیر» می‌شود.
🔹
امارات طی هفته‌های اخیر برای خرید تسلیحات از دیگر کشورها به تکاپو افتاده است و مذاکراتی را با کشورهای متعدد در این زمینه آغاز کرده است.
🔹
اگر چه، سلاح‌های پیشرفتهٔ آمریکایی نتوانست از این کشور حاشیه‌ای خلیج فارس در مقابل آفند نیروهای مسلح جمهوری اسلامی ایران محافظت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/444063" target="_blank">📅 18:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cev0WEHLWuDXCxcSUwjM2NlC3zHfRMEeZAYESNEFskkq4BnZGP46etlz08MDmy_gVePefTQ25ZGYKKsbev4lfpYxRy3RpNU9F67aumMGyZOoOPaF-vh7uPfQFISipsPzxv6_hrPbFW7Che6LIm51TK9-3JHQoFdcoQ1xsGm7UWufEzwFLAEW9YJJV-4T9ge7PW-O109IoMZD18ohrLcXfAUMzBtPRHTUFSC5M0jc4-SnEOoKShxijqd8qWYCdxyj0P6MuBseNTeAZ7bZfqrnhRVaQD6ufwA5I-7kfgGJCy1zkz4hPm8n5358dPDQFRps4ncYc-HLBhw1Sdvvs-MoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاقات عجیب‌وغریب در حریم تخت‌جمشید
🔹
سرپرست پایگاه میراث جهانی تخت‌جمشید در گفت‌وگو با فارس اعلام کرد شهرداری مرودشت برای توسعۀ شهری در حریم این اثر تاریخی با یک مشاور قرارداد بسته و درحال طراحی و تعیین محدوده است؛ درحالی‌که پیش‌تر ابلاغ شده بود که امکان گسترش محدودۀ شهری در این محدوده وجود ندارد.
🔹
ماجرا به تغییرات و تصمیم‌های چندساله دربارۀ محدوده‌ای موسوم به «محور مهدیه» برمی‌گردد. این منطقه در نزدیکی حریم تخت‌جمشید قرار دارد که حذف کد روستایی آن و سپس طرح الحاقش به مرودشت، زمینه‌ساز ورود دوباره این موضوع به طرح‌های توسعۀ شهری شده است.
🔹
هرچند این مصوبات در مقطعی متوقف شد، اما درنهایت شورای‎عالی شهرسازی دوباره با کلیات طرح جامع مرودشت و الحاق این محور موافقت کرده است.
🔹
مدیرکل میراث فرهنگی فارس هشدار داده توسعۀ محدودۀ شهری در این منطقه می‌تواند ارزش زمین‌های اطراف تخت‌جمشید را افزایش دهد و احتمال تعرض به حریم این اثر ۲۵۰۰ ساله را بیشتر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/444062" target="_blank">📅 18:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe1c522cf.mp4?token=IfHB--guV6cBTtrXF9FpspALWnLrqYPUpWMuacoYXkSIr9nWlyCWoBna_TDZ7jkGPk3eamAFqc8FyE0-fxaiKrR6rVUvbtyyU2RKebRMMcHKK35XwFZPvEtz-d8TTqkMAmacBpVJUU9buxZgErFD-A4y4yJCs-AKrRFmJo37DxcN4mLIar6J1UJhxC8j0jR8Jg1H8b3O2CX6lT1md1g4MKqbgZfPMhJU2KCJeqqjSivCv0MJBpAQNX1_9TRr1_afj8r7bEEPLLV1wVNnIUjZPeGCbRHwVvTaJ5ydFEtrYOyCKkeoE6quoi__O7GL_ldHroE9a1xOhAlkkkOa6WtxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe1c522cf.mp4?token=IfHB--guV6cBTtrXF9FpspALWnLrqYPUpWMuacoYXkSIr9nWlyCWoBna_TDZ7jkGPk3eamAFqc8FyE0-fxaiKrR6rVUvbtyyU2RKebRMMcHKK35XwFZPvEtz-d8TTqkMAmacBpVJUU9buxZgErFD-A4y4yJCs-AKrRFmJo37DxcN4mLIar6J1UJhxC8j0jR8Jg1H8b3O2CX6lT1md1g4MKqbgZfPMhJU2KCJeqqjSivCv0MJBpAQNX1_9TRr1_afj8r7bEEPLLV1wVNnIUjZPeGCbRHwVvTaJ5ydFEtrYOyCKkeoE6quoi__O7GL_ldHroE9a1xOhAlkkkOa6WtxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشویق ایستادۀ ملی‌پوشان ایران پس از دیدار با بلژیک در استودیوی جام ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/444061" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2770cc08b3.mp4?token=W6bSbElCGKquG3rmVGuw3HM4dbPjfMdQFLCPYRrCjZo6PRvFhM2RUdHr3423AkQCefUnYIjSqNxGcSmLLpaC1nGLHEaQhTLS1ScdtCCzKFMOwXVnjwUwmdysi9Ft4aLq5CR3FOdwoTM_dGjhtUUO8WeHi3o69wWdeYPZhL1wL4E3AaD90yQoOnusJLqDT0Bkf_pTq0uhcubQFiac--kZAwe6DP9ZDexIWRF4Ou5tN8Hq7NEfwkhb9lrbo__UMk-q1KhRCXp5GbZJWyVFJ0VHbI4PuOXw5C1FZLxQZA7u-SS1weEo8FNaHVxlvNi6KvYBeVfPRq-ItkXdZTRwaJNJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2770cc08b3.mp4?token=W6bSbElCGKquG3rmVGuw3HM4dbPjfMdQFLCPYRrCjZo6PRvFhM2RUdHr3423AkQCefUnYIjSqNxGcSmLLpaC1nGLHEaQhTLS1ScdtCCzKFMOwXVnjwUwmdysi9Ft4aLq5CR3FOdwoTM_dGjhtUUO8WeHi3o69wWdeYPZhL1wL4E3AaD90yQoOnusJLqDT0Bkf_pTq0uhcubQFiac--kZAwe6DP9ZDexIWRF4Ou5tN8Hq7NEfwkhb9lrbo__UMk-q1KhRCXp5GbZJWyVFJ0VHbI4PuOXw5C1FZLxQZA7u-SS1weEo8FNaHVxlvNi6KvYBeVfPRq-ItkXdZTRwaJNJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانویی که مزد کارش را امام حسین(ع) داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/444060" target="_blank">📅 18:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f2aa661.mp4?token=Ko8_8sPGzcCN1tZKnNW4fRh7NjX6rDeU3V1nOGvY-0wjY4KZ7rX-xlCi9py2-mWwWqs9R-QAonnLeLJmR-_VB3uzVoTg0gimQykRk2p81ghARjcKaIz8EkXgtQnC48_GVW_ilmxSJ_cAc7AHLGHt6fdTZ4BGZEd3Sm1GAXEAh0aEjDDYp7x0NlDGI1ZOpYrJm6-360Q56xnPvuUr617COBB8xKR-FCODGdO01XWhqJ0-D9RrkwknYZq0bOw5KlDeLbOtY32Ci6azEXwkoX5i65gLH7A-x8601u6lwq_EJ-tHxP9zmiszxebcKF66MdgZhtz0aD4XLnjwrhrO2JTqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f2aa661.mp4?token=Ko8_8sPGzcCN1tZKnNW4fRh7NjX6rDeU3V1nOGvY-0wjY4KZ7rX-xlCi9py2-mWwWqs9R-QAonnLeLJmR-_VB3uzVoTg0gimQykRk2p81ghARjcKaIz8EkXgtQnC48_GVW_ilmxSJ_cAc7AHLGHt6fdTZ4BGZEd3Sm1GAXEAh0aEjDDYp7x0NlDGI1ZOpYrJm6-360Q56xnPvuUr617COBB8xKR-FCODGdO01XWhqJ0-D9RrkwknYZq0bOw5KlDeLbOtY32Ci6azEXwkoX5i65gLH7A-x8601u6lwq_EJ-tHxP9zmiszxebcKF66MdgZhtz0aD4XLnjwrhrO2JTqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: علی بیرانوند به جهان نشان داد یک ایرانی چگونه از کشورش دفاع می‌کند
.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/444059" target="_blank">📅 18:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تعداد قابل توجهی از مردم آماده‌اند تا در مراسم تشییع رهبر شهید انقلاب شرکت کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/444058" target="_blank">📅 18:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f8acdd9c.mp4?token=VuYQA43uGFH-dbl1zoYowbVqgBa0MQdzO95VyM5QvJsrvDJ1_7DmuGZCeBSU9r5J1JnwYGQy7SXhVstd3FI88TadbPAOVQmhwQ_WcdEAzvQSiOQeyi7Wi2HcqmLThoqemSIrcArbbw7hTrBs2-P_9fLmTb9yTSVKJ-oTp6Oxyl5bvc6T07Pj7rNUThh8-74nghzqNjJVHnxPFf5r3YuIUHW4i6cAWIbxv_r7u7-fyoesVnxl0KxU4MixwTTAXew96MP2BZye-u2amJH6a-Vb67eMQb5px9VvyfGyfRKQBTkeg7xRZTLGdzQcGjd4Brror84K5t4SMsm4AvJYOuk_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f8acdd9c.mp4?token=VuYQA43uGFH-dbl1zoYowbVqgBa0MQdzO95VyM5QvJsrvDJ1_7DmuGZCeBSU9r5J1JnwYGQy7SXhVstd3FI88TadbPAOVQmhwQ_WcdEAzvQSiOQeyi7Wi2HcqmLThoqemSIrcArbbw7hTrBs2-P_9fLmTb9yTSVKJ-oTp6Oxyl5bvc6T07Pj7rNUThh8-74nghzqNjJVHnxPFf5r3YuIUHW4i6cAWIbxv_r7u7-fyoesVnxl0KxU4MixwTTAXew96MP2BZye-u2amJH6a-Vb67eMQb5px9VvyfGyfRKQBTkeg7xRZTLGdzQcGjd4Brror84K5t4SMsm4AvJYOuk_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برگزاری مراسم وداع و تشییع رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/444057" target="_blank">📅 18:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKqai1SqgapW7lYL18Caj164D1lOul1XQWM_KCnYiyo2vhOMEUIyTnVDVuuyLYZ1rcP2K37W455GX8--YwHuXRVSkBOsAcKizCMlv9QY3GW0hUCp5hD0HM1V5-8rRdFOu-PX34SB4eXYOjZMlXP606yU1R3fE7WWEC3rrKGbZPbTDsQ1PElxM82t0L4xgyplqMpEJsd9d0S0AGjvlAg9s6HW9vp1MDr00Ry3i6rm4vGLfA06A4dq3xv8c6hmI2hhYVRJx6fEZ6Pm6ZKPmuZztgzH_jhH5h5-w39NceT9UV8Km4CvRx4sDnA7ynslJRT80QxUMsR2g-t5p9fJwbe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ هزار دانش‌آموز خواستار تعویق امتحانات نهایی به بعد از اربعین شدند
🔹
کاربران فارس‌من در پویشی خواستار تعویق امتحانات نهایی به پس از ایام اربعین شده‌اند و گفتند: با توجه به حضور گسترده خانواده‌ها و دانش‌آموزان در مراسمات و پیاده‌روی اربعین، همزمانی امتحانات با این ایام موجب افزایش استرس، اضطراب و ایجاد نابرابری میان دانش‌آموزانی می‌شود که در مراسمات مشارکت دارند.
🔹
حامیان این پویش از مسئولان وزارت آموزش‌وپرورش می‌خواهند که برای حفظ آرامش روانی، رعایت عدالت آموزشی و افزایش کیفیت ارزیابی‌ها، زمان برگزاری امتحانات نهایی را به پس از اربعین موکول کنند.
🎉
اگر شما هم موافق تعویق امتحانات نهایی هستید و می‌خواهید به جمع این ۷ هزار نفر حامی اضافه شوید، از طریق لینک زیر از این پویش حمایت کنید
👇
👇
👇
https://farsnews.ir/gomnam__3__1__3/1782066119787494110
@Farsnews_My</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/444056" target="_blank">📅 17:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3f775d67.mp4?token=hcu_18zg0lEdih1q7Txs_aZGt6FxaPBt-qrP7vUFN9QWGCUGynUn61RCm-1onJR37d-SKthxOhz0OeKS6ToWTnqP-f7mwwr73Oos8kHPrlTSTeoiRPEwUR7r82YH3amHxnUvwpNOaPluG58BcfwawYHkzAtHG_VFk-1ILEQjmI6YHPsoqgAqTSMOkn9wZsoq4l-3B2feEgTGJdVMyl5II0vM1DMvFGafUny5elUEQWFBkrQD6z7RuacX-mG9f2VVXoNSAf2Slhf-EZH_IMk7ktt1rJbojc3uFu3LOG1nxz7BixTpzQAn-ir9_FytF3hZjfGPat90ucGNqzoFRaLCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3f775d67.mp4?token=hcu_18zg0lEdih1q7Txs_aZGt6FxaPBt-qrP7vUFN9QWGCUGynUn61RCm-1onJR37d-SKthxOhz0OeKS6ToWTnqP-f7mwwr73Oos8kHPrlTSTeoiRPEwUR7r82YH3amHxnUvwpNOaPluG58BcfwawYHkzAtHG_VFk-1ILEQjmI6YHPsoqgAqTSMOkn9wZsoq4l-3B2feEgTGJdVMyl5II0vM1DMvFGafUny5elUEQWFBkrQD6z7RuacX-mG9f2VVXoNSAf2Slhf-EZH_IMk7ktt1rJbojc3uFu3LOG1nxz7BixTpzQAn-ir9_FytF3hZjfGPat90ucGNqzoFRaLCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/444055" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a16cdeca.mp4?token=XfhUif5jGo0LrRuIemZ1S78zK8lBV06TVfKLtPLkLjH2cwx6L_ao1EO_YIkH_TLAVvKwcOIX2sLba7k1RK9_x3RzWBYdfpXU3nyau3lMEYoq7d2xL2dsbhhuxTryCnRjHAMVqDW7U2fiNfycJBfZq5vc-RhgVeeGwp9V7WlDqYS3qLsvXzFAXa08ezk4W366iSyP06mNnzEYpT3yeoi4_SLs2aRS1CvTXWzMp60_FGcvZHvtVV9JZm9YKC3blIKaapelVHISL_VnP07zHCxDwvYTVcB3BhbgHLcno06DfhdG7AYOL0bqygI2cdjCLfXmuzEZd8Z6BHN_jW-D2yiGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a16cdeca.mp4?token=XfhUif5jGo0LrRuIemZ1S78zK8lBV06TVfKLtPLkLjH2cwx6L_ao1EO_YIkH_TLAVvKwcOIX2sLba7k1RK9_x3RzWBYdfpXU3nyau3lMEYoq7d2xL2dsbhhuxTryCnRjHAMVqDW7U2fiNfycJBfZq5vc-RhgVeeGwp9V7WlDqYS3qLsvXzFAXa08ezk4W366iSyP06mNnzEYpT3yeoi4_SLs2aRS1CvTXWzMp60_FGcvZHvtVV9JZm9YKC3blIKaapelVHISL_VnP07zHCxDwvYTVcB3BhbgHLcno06DfhdG7AYOL0bqygI2cdjCLfXmuzEZd8Z6BHN_jW-D2yiGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتفاقات مهمی که در سوئیس رخ داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/444054" target="_blank">📅 17:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHPTnID95zaaPAkLcI-_6Q9f66MRzG8skn9w474YM1bsstqNrNELPVgFQZMVxS6REl4rQpLI9lAmOCODYFBSWF7TzRn5hxSVhmB1AUOzxl8E1H46sBtXlPv7a9M_FgcZxFahtk8CCQOA4vyx-dPQryEuxPu0j_3EhU71i8ISA_9oi99ir8kQDsrpCb8nU_uExGKqLduAZYtHx_aZOm-AqlJt6hP-D0cj10wB0W-IKeLas-fhZTtBWoUEMqhu_D3d2Xpb4UuP0eMeBzpWYGO1caXyjYcEGHY-XKyLcwuUf4rcl-DkqZp3W48UFMcdWf87iBdq5fUXFSfB0cumCLqqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuUvadpT3_DBhKmkLI9vzmIgL7yUsbu2MrRCXAKkpC6G3eLi7WWxu7sCTVFVmFDqpr4pI5rgeSF3fVRm0RpBpW84Xf6-ataZG4A-mw1RXcYcyLI7r98duy-m4q5l50UR5xiYzQPR4QeZFhaadC9joaotu3-kFAI31zEOL1yvxNrON0BNZjdG8Tb4-a1AqgIqRO7e7PtjxJMLotMujVG8TjUxn93DNgttG2Wa7Ql9Z0gL7U7D8mpYqrXcMWG7AFV_Ytj6dOqgYC7sa9I_qOBJdUWqOEKYP_EX9Ti0pm61DjebxKVCjHCTTyzVxwNQOxQwjWcttHZ7gIYbTTtdJRFGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1HTA48OwEftWJnXnSqUxy3XfAZqZnBg5VQV0bkl-nbOVCWeSdUpQKTkGT-CrZoqifzgD8YLgHqz4Jpu9nmv1J2SUjfvAYEFWjJENrL-Pp7dV8Jevh4oeGQFshkTs-Blgia47jTZaWi9sZWSyHHOA0AYBZbkybPBxj7kDFwWI_TAVV33nSCXBerCnJweJLbfOsFEbUd30492VwHa-PNK-r1dJ0ND_UUbTG8Hx1wzDPIW4VrZzZ6v1biAbEYUXZC31ohOh2kGcGdSvTZCQDFMrS91CS5DbzKHOAwrsGlGiHWHcpi4knkFrwXvlmzq79qCSWZ-H9naO720_fdGEPEQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GW1cQwlfNGgkWHhRtutYKyG0MEngT-MgDlJwKZTT4yuM7ANwFY1WmLJqX1x5Twx0oosMzpYe4gS-FeejcQR__cUjc7llTPjU6l_G8v5DACcb0nZrt8qjengVY3xn9ZhSKsi7mnmeI_xW1tilVOWn-sNfsaXLWcvT_v9Vji9lyotJkWihVriXhmdzc76gZjP6awiEYFY6l4Uvqb-B5uTGSB3Pbo3afll7oKTd3UX0iy357ZBiYkvh2jzm_jheCj3dUPUGXAIszqel1DdMaV5L7u6-Yz0zblpAHZ60ijOKvnYwB0tkm0Affz_pIfJHtl-EikwRArMORjR6RaFAV8KT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daCFhIneuglG-PTDK5K0lH62m71m4S3TuAR59X1KU8pbpkHXU83RPw9RiejK4tjq1ib4LzphTHqRUwDqgGzJ4CeiCZUFvJeZJO8CeuNPCWkQ0L_5_zHv5P1FkvrGsSbqsR4KDt-O16KYk1JjgylY09GF1yc6R-DZ2h3auX2J3me0sUZJquf9-IjMzK9EKmNSTO5HDKUPo_pV2wgU1jukkWKHJaZmwa1xeFpuAqlTYWjuTSiXOgt6QF2DKIRQY2q5Y61PFrKOgjLO3wUPJ4FeVZX1BCeyVI1Iz_oLms5QP_wPBFKsuqmq2P41rJTIDQsfrEKI-SMQyRjqQSMtiU63Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPts0_ST3-wTmZxgmTJmUNeKj9p4lpIWyO3kF0Ofvl2WYOIKORaLe7EuE4yVXPkP6k3IEuCNO3W-oK3lsrHL-dyB2vHSE8dyjN9PkubE5HIQIgZ1j2dhEs8oddAtmveOwnoIc2kY_5HCaYSX0WVG3gkSUaKM-EsQAay_JRNQfWgmf2VKpWV6s8YPV4_WKaeIuy-0BJQlIQ9qUzvqYbhEXrWS-rTAIYT5EdTp84IC1Y4FrFyLvTQooMotDhXlC5J7dzTEXF6N1p1gJVdcH-PghIblOpJNgKxhlCy1zh7fA9xEzP1X969u-IAL803wud47VbIep0p3oo6E_b-MVyAF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Un6eBCiy7qKYJxCZwNircS4xVjpa4Twd2a5yWxp29P5XduGKUn8Xby3-GxCPfZowMV_ZSAPq7o8emaUHZPxbDKMUrmchDvOZT8-Kki5FD8rxXLflcvcTids1OyDJC1k5c4IxUW766p35hf2k7H5sga0kpMfZleuN9MA4FmLHSJds7FTeMC_lba146FlatLUdMfdiOZCcJXvmnMe4e0_99ZEkrG81xb9XtmkL0CWjAhUKgkcDG6fPbVx-p4k-Qmwt03msg9_QMbpxSbElO-38m0rlDJbNCrUZxcMA8BLXEtwB-eaSrHhMYr3IX-cDZL5e-mar7Kuxs4ugEAZhL6Sjww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات تنیس روی میز انتخابی تیم ملی ایران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444047" target="_blank">📅 17:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
مجوز خزانه‌داری آمریکا برای معافیت صادرات نفت ایران از تحریم
🔹
وزارت خزانه‌داری آمریکا مجوزی برای معاف شدن صادرات نفت و محصولات پتروشیمی ایران از تحریم‌ها صادر کرده است.
🔹
دولت آمریکا در بیانیه‌ای گفته که «تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و محصولات نفتی دارای منشا ایرانی» تا تاریخ ۲۱ آگوست ۲۰۲۶ از تحریم‌ها معاف شده است
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/444046" target="_blank">📅 17:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af61564701.mp4?token=dd_WZ669Pi9_3TbEIL5YP1sgvNpTSa6EKQT3R3rQ7opD_2NDFkRKmjIeZ0KlyxMVJW0YpAaNNHCJNOhejqkThN1Tnm0NBoY8AeMCY-jEtP57sJ7hsb-RHnwVVtsc41_vf5f3dLEDWssw1A5alxwPB3esOcwMIYhPqVajntGc1i0S7nd844iTfLkkyxcthzlUa_fJDz__XVPbbWKftdfNuGMpfDrx9RiA4tvCFmwpda_r_baTm2wQnrxHKKWwOPavUUBGqOrLov4xi6QR-584gKSE66fWjRwC7jDFVrMn6gFIAOeacSYdBj0dwQtbqxWHcygKZFnbXl22fx-VgUPVL2hpjtCQY7d-NZhuclBJTlHSuKRVrsn8K41O907IAbJULZWcTOXIvSPsxqj1m_8lLDNcoM0tmZzjquxo9RtQMEPbGsnX97U9kc3nv-C-ZndEeUSYjwQ-Uc4Y8bPmSjKeFRWLbaqObEutzvLFDrjUl38SRmeMTNoq0vCB-dcPcrclU7aeYwqHwuLiEzhQAmx6pi1WVyddMAms1tsY4Th917cvGtPkEtbG3AmA54QlGPR9LYxD_fg5PRPfI-kAOHFC7m52oaND3nhgnJqbk0-SF9LlSb88dY5-QMiHWtVOGFl4iMjLkFnz3nvipDLntC8f8q8sy-bOuhAdHj4Mcnnn-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af61564701.mp4?token=dd_WZ669Pi9_3TbEIL5YP1sgvNpTSa6EKQT3R3rQ7opD_2NDFkRKmjIeZ0KlyxMVJW0YpAaNNHCJNOhejqkThN1Tnm0NBoY8AeMCY-jEtP57sJ7hsb-RHnwVVtsc41_vf5f3dLEDWssw1A5alxwPB3esOcwMIYhPqVajntGc1i0S7nd844iTfLkkyxcthzlUa_fJDz__XVPbbWKftdfNuGMpfDrx9RiA4tvCFmwpda_r_baTm2wQnrxHKKWwOPavUUBGqOrLov4xi6QR-584gKSE66fWjRwC7jDFVrMn6gFIAOeacSYdBj0dwQtbqxWHcygKZFnbXl22fx-VgUPVL2hpjtCQY7d-NZhuclBJTlHSuKRVrsn8K41O907IAbJULZWcTOXIvSPsxqj1m_8lLDNcoM0tmZzjquxo9RtQMEPbGsnX97U9kc3nv-C-ZndEeUSYjwQ-Uc4Y8bPmSjKeFRWLbaqObEutzvLFDrjUl38SRmeMTNoq0vCB-dcPcrclU7aeYwqHwuLiEzhQAmx6pi1WVyddMAms1tsY4Th917cvGtPkEtbG3AmA54QlGPR9LYxD_fg5PRPfI-kAOHFC7m52oaND3nhgnJqbk0-SF9LlSb88dY5-QMiHWtVOGFl4iMjLkFnz3nvipDLntC8f8q8sy-bOuhAdHj4Mcnnn-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهین تسلیمی، بازیگر: زندگی‌ام به ذکر «یا حسین(ع)» گره خورده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/444045" target="_blank">📅 16:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY43Mn8E5ml8KmJuTu54vXg8EkPl3LSt_jnny-a14QDge8vXsSZpFzeWoo8TPIpvDV-82d-hNNaS-2RcwmDrj01QSpZx8aHFAG4oNWqsG_sng7y3Mt3mOEtm7usVpv7KPDb7BT0LqysQw41bhfRpl6Nhq-KpoV_QyBomR1CDCUQTAIp2qq4vRR0j0RF_aG9XMQmtMaF87RSBTaFwRoywxwQKJ5oQt1y2iIFkhJP54tLjruxkG6GSaMB-kzIy-wKWhfJMUi2PPi22MIzhxZo9QkbxoBZOm3JoOIH1BvAHTk6aSaiYtsk45LfPs0NTLT143hce4VC-IQA0jZMb5wbKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز صادرات نفت عراق به آمریکا را صفر کرد
🔹
جدیدترین داده‌های ادارهٔ اطلاعات انرژی آمریکا نشان می‌دهد که صادرات نفت خام عراق به آمریکا در هفتهٔ منتهی به ۱۲ ژوئن به صفر مطلق رسیده است.
🔹
این رقم در حالی ثبت شده که یک هفته پیش‌تر، صادرات نفت عراق به آمریکا حدود ۱۰۷ هزار بشکه در روز بود.
🔹
علت اصلی این توقف، اختلال کامل در صادرات نفتی عراق به دلیل جنگ منطقه‌ای و بسته شدن تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/444044" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0RSlsGvPZajlbYLfGLR2ivemja40DTu8OVnN7Zg1XaRFcI3U5VnYZdxAP0TrQ2R7X9pF4gjinzE-1ImGFsrgtptS6Nt_idC7UQegHEktz5tMsv1ZbPcEOfIAAKFxXBCXp9Wueb9k9_wb531oPUQbMx4V-i9oN_prxTJP8RAjIdpdOuqEWj9eHktVA6vrxQKdo1JPnMcVNIApp5yfpTEf-nCFvmknuJuQM_Gn1dQiV4n56MLLBuoeQKZVWnLONYO2hm5EoXzMT7ezhqXAUe_Oo3jE878U_QFwjwo4twLrLQU_fmV8cgz3LuMa3EyPPnW4MrQRCRnKWCB-ayGinUABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرهٔ قرارداد ستارهٔ خارجی استقلال باز شد
🔹
بر اساس آخرين پیگیری‌ها استقلالی‌ها امروز باقی ماندهٔ مطالبات فصل قبل یاسر آسانی را که نزدیک به ۱۲۰ هزار دلار است را پرداخت کرده‌اند.
🔹
یاسر آسانی پیش‌تر با ارسال پیامی به استقلال خواستار دریافت مطالبات خود از این باشگاه شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/444043" target="_blank">📅 16:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVHYnrWvmhpJqa53zIZT-5OIOSJsuKVnjDn6K5AWKeXs75OCM1Hs3qRBuHCKgroZBcoZ9Wfq2NnD5qEf4FVTF78yjM1_ZLpv0bRrtAZC1bxGbVXaXHK8SeN2S6KnQZKNg2pKjp78OZPmqPhSkkpIZKfNoyxCOcItgvswsqc_QfqQdTI7jetwSoF0onQLjcRL6HvldhEKn0ZYG9zHmKvducMLVW0X5V2K0qC9M72vGbKvOYy6dfckwusNBU7z33bjpjr47E3TSMeulEL0QbkCP0DOFiUGy7rwnXunboWlPHI_HYKxO5gV8GsUunANsNv2Lhgfto74aA9OFL7DLPmEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیب هر وعده قلیان برابر با ۲۰ سیگار است
🔹
محسن فرخ‌پور، متخصص ریه: هر یک وعده کشیدن قلیان، از نظر میزان آسیب، با مصرف یک پاکت کامل سیگار برابری می‌کند.
🔹
هنگام کشیدن قلیان، فرد حجم بسیار زیادی از دود را در یک بازه زمانی بسیار کوتاه (حدود ۲ ساعت) وارد ریه‌های خود می‌کند.
🔹
این حجم بالای دود در مدت زمان کم، می‌تواند آسیب‌های بسیار خاص و شدیدی را به بافت‌های ریه وارد کند که با مصرف تدریجی سیگار متفاوت است.
🔹
اگر فردی تصور کند با محدود کردن مصرف به هفته‌ای یک بار، خطر را کاهش داده است، در واقع در حال وارد کردن فشار شدیدی به سیستم تنفسی خود در همان مدت کوتاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/444042" target="_blank">📅 16:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنگ‌زنی مردم سبزوار در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/444041" target="_blank">📅 16:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGV5nC-lnkXT-FQM2HgINvET1YTcyfGR8rIKzZFNmNgzEBEcRsHjySRODgGW_Zi4bMtSuNocAgBWfaJFJRdn3kISSruO2uspUrZj6VIIrmrbMrp-VAbCtb5BttCl_ZhMMxTUR27HuwNa1A3_jy-3-cxOIgv9yNxfIS0XX6JGr9Sg3o5b2pd1fK_hZpSJYD0h2rlSbhhDGpxfTcCkMGXCYbnlfPIufuh82hG1NF8mnQNOz83WbS6YDcGH0CXiYn_jw4yIEXCctUYaIFKRHO0MwdtPvDVUwShi2nOId3oBrXk_ra7has24T-8VV0ZVswLYT_CZHvpMpwhgwpnMurHV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تأكید مدیر عامل بانك صنعت و معدن بر حمایت از تولید و بازگشت ظرفیت‌های صنعتی به چرخه اقتصاد
دکتر محمود شایان، مدیرعامل بانک صنعت و معدن، در حاشیه بازدید از نمایشگاه ایران اگروفود:
▫️
در دوران جنگ، خطوط اعتباری ویژه برای صنایع غذایی و دارویی اختصاص یافت.
▫️
هدف، تداوم تولید و تأمین کالاهای اساسی بود.
▫️
حمایت از سایر واحدهای صنعتی نیز ادامه داشت.
▫️
بانک از بازسازی واحدهای آسیب‌دیده حمایت می‌کند.
▫️
بازگشت ظرفیت‌های تولیدی به چرخه اقتصاد در اولویت است.
▫️
توسعه صنعتی با استفاده از ابزارهای نوین تأمین مالی دنبال می‌شود.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/444040" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMV6MXKUBUyan_7zOtyhLAb2Av0VsBAIJbZh-UkGyL9NZ2TuMdOr48X92KyGayk_N2-Hhp3VR-Zu0DJlEMzOZ7II01m8wUaF3I8_1YkPS_jyXP9qBtXbrBU6xVhfFTQmq7APEk1fftIyTJs4wwfyHS3F2erh-O2crT8aZH_aQyClpfbq1YGAAiWRCaWFrOKhUANMZako8LUoiyTCRqQgZxJovPmuoMe3dXKbbKDE2e0dw4Hbm8zLYDcS27FWNkGTlnWUErew4CkxExiNjw4vXpwM-WahpJppIT-SapuVFCM-P2Oo8CUsSY4NnNHKS6xbM7_IxbwtcWcPjbTnDFzXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/444039" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/444038" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8j7em-SENrZghaavR9jL3GBpG01HR4vavKEbyy6gqLct_y-8RmSxwz2J_KQJkh9MYQN8O0ayPjn3MleheCtNena0M9XXgGbyb3XQ9LGYJc0fetepsIiK-NXNwNEhBE5yXy0WenH61Ys0MUAao_-W9p48zkFv3bJfK-3NLoSanVI1KwEzmtpNsdGgyVFhyOgKXQb9eq6AEtBZYsOl5HXtBsk-DLNDOJHq60_3hjvnM5bMknSbFODBa0ecXpMtWmbmjEcVQb_ETzY59X9AASL-OFsyHMeKaub0STZOOU0PEDI0FP9ATMeGOBoYlq6H4cswmD6WBNpjoFylCQCdc9Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان در راه تهران
🔹
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/444037" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2baQfab8D1M4RoQofbQiO_DPrZcsgDWsDT8Z6-b_M8jyMCFUjhjlfZ1IgJMXiEA-6Ruy8Fc1R3DJs1QzV8BNogN1XUpmoZ3dImMc6e2H5iSax_QKyWTQwfiwc9HWDPwALoje6_qqm4r6AZxgUo7jYO6Ge2ODuwsmzN9em3N8Sx_4HNmZWrYq0P143PrLnwdkY1EetD9BsrZ6yyM_cmIq-PBksafZgFcKElscOIB7HOE5JwBQlvoT_2Cm0mStTd71S-GtmYf3rvj3nApNHr3l_ss_artrKW8jtPPcCBJj3FCIOmE2e9kXdGrNUjn0IYSnZSvkQbmBEpme6c3orEhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۴ تُن سنگ طلا در ۶ کارگاه غیرمجاز تبریز
🔹
دادستان ورزقان: درپی بازرسی از ۶ کارگاه غیرمجاز فرآوری طلا، ۱۴ تُن سنگ طلا کشف و ۵ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/444036" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acd6299aa.mp4?token=JaPVKUUeJMgzf_GOKORIApMq-PFJeQCSzjGWbRRw-oQ7TI00tSESaaWXL-M5gGGO7fAvEaKUFEsJTW_-CtcbG6TKbmirCdXUaPb-VeYkrW4rdEtXpkD_k9hrd7pZrL3aRVFit1YARNo_OXobZh0Na3zcAirjPx4FNeeDp54wJGvrYkX3XomQY1D9M_OUihRsCGYEfe_tDTpfXRaP5qKNFXBlLdGRNqhAzu8gbMoSJXTVFqMG-Gi0wnW6SohdnsTw3CQTemvnBD-hpUoMIq2vpg5eaGSNG3GzIwdkcSQfdtOfbk-Xw0ARXNhM3fqAR2BlDIP7-_D3ysSC2e0iui39uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acd6299aa.mp4?token=JaPVKUUeJMgzf_GOKORIApMq-PFJeQCSzjGWbRRw-oQ7TI00tSESaaWXL-M5gGGO7fAvEaKUFEsJTW_-CtcbG6TKbmirCdXUaPb-VeYkrW4rdEtXpkD_k9hrd7pZrL3aRVFit1YARNo_OXobZh0Na3zcAirjPx4FNeeDp54wJGvrYkX3XomQY1D9M_OUihRsCGYEfe_tDTpfXRaP5qKNFXBlLdGRNqhAzu8gbMoSJXTVFqMG-Gi0wnW6SohdnsTw3CQTemvnBD-hpUoMIq2vpg5eaGSNG3GzIwdkcSQfdtOfbk-Xw0ARXNhM3fqAR2BlDIP7-_D3ysSC2e0iui39uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات آخر در ناو دنا دقیقا چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444035" target="_blank">📅 15:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrObUXDgDaSCdA2FDtSwC1rlTRwt-3vtTYm1NC-m_a0hn7wLAxRS9f9pqsjpT1USCJLgIUObebO-vW_5pjaevGcBCGG6MEyefxZZymaumjTkxyHj1sPLYSVV2fnBAGpnbzOJ_lba6mgGO24kk1CZapx1g9QCi6nPOm1vPuazjISlbpScsGX4XzI5BxOfj7Npc4ZzSsUHLHrO0OtB-USfwAgB4h0wpUuMzZJqCTVnv4Y07FIzf4MyKP0Sluk55LyWi0TR-ZZqjyMxynmqR3mKDGOT-sxASbVwmzuOzu2f1jhTIsLQ4GlsRAh0xqfvkgSpp92iAd0S0SLVLhOLm8VwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه پدافند هوایی خاتم‌الانبیا: نیروهای مسلح در آمادگی کامل قرار دارند و ما برای هر سناریوی دشمن آماده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/444034" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سروش‌پلاس‌ هم اختلال پیدا کرد
🔹
بعد از ایتا، پیام‌رسان سروش‌پلاس هم به‌صورت موقت با اختلال و قطعی مواجه شده است.
🔹
علت اختلال، قطع برق در یکی از دیتاسنترهای شرکت زیرساخت اعلام شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444033" target="_blank">📅 15:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-TYCaXlOo-SXVozpuDSzdmMcaU4iU_Bz7i0AoG07BDLhuwEi6zE4FEMtM2Wwb4ss09iZHuB1VFAm28kNUTvdWl2F-Z9_V94jZMkshKbfYjKTXnfyACFktgZA-RauW36H8ZdKoexKRMUO0Wlgk-Cpfn2A7lB-mTWn9PPT82pJX3MwJD9Bepw6NlVqF8TmkZoQHApt4CdgOM93EShFyLKwP_kXScI0dPIX67JEcanhTl-D0zjyFvj7PLJMxjVnnXhAd1Og70CABhqjR_Dix57tHE3O22FM2cdpBEiiaJhiu_J1aQuYlm3MiKwGFbjUAqLeQ4rRRRGW-IefAc2huh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعنه اوسمار به پرسپولیس
📲
خدا همیشه خوب است. متعهد بودن، حرفه‌ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است.
@Sportfars</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444032" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/444031" target="_blank">📅 15:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a1ddb47b.mp4?token=epmFwA3_olA8nCaSegE_ZX4xgb1vHYqQM16pkPbZEj-6nCmE89fVd3AGXEDq_WJ5e7xEqUDCbOPqi-HFKmaMJde61XCsrxDvJeLBvfPuSkUh3a_BYK5BybwthFPSnBEvfsHhtdg8WHgfN7dDkyEbcouPHeDL06vNoGD-aFoHDJHRe9nWbKvThT3S23WwzUWvlVp1c6aNjqz-oEH5e43VNJotyuTyN8ny7l77nY0C0ar3wzWO2qUZOTMJSvW21DABRxCFRtnLje5tKHnqsOTApHVHsZfx4NBvVZczwTCnH1lG0lHMBLxt0XCR6MzoLswuGl3SK3HjZJA7exT18lvQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a1ddb47b.mp4?token=epmFwA3_olA8nCaSegE_ZX4xgb1vHYqQM16pkPbZEj-6nCmE89fVd3AGXEDq_WJ5e7xEqUDCbOPqi-HFKmaMJde61XCsrxDvJeLBvfPuSkUh3a_BYK5BybwthFPSnBEvfsHhtdg8WHgfN7dDkyEbcouPHeDL06vNoGD-aFoHDJHRe9nWbKvThT3S23WwzUWvlVp1c6aNjqz-oEH5e43VNJotyuTyN8ny7l77nY0C0ar3wzWO2qUZOTMJSvW21DABRxCFRtnLje5tKHnqsOTApHVHsZfx4NBvVZczwTCnH1lG0lHMBLxt0XCR6MzoLswuGl3SK3HjZJA7exT18lvQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: معتقدم می‌توانیم به نقطه‌ای برسیم که هم تمامیت ارضی لبنان و هم امنیت اسرائیل حفظ شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444030" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e821a5697.mp4?token=JmhPigX10j4jz2zdWe2nw5BT4t5goxWTz3GnJxRnPsj4opF426ioMv30jJZuRjoafYZ1jHIlaONj1WnAgkSBtd5oBSJcRcAh6MjQInu_DITMYaBn8vtg4bsIfzKwzIVuYSjtTnWjEZCn1RqjifC-3KH4UY_h-hnoOCllX1XtTcbZVPNrKSAu3F7mpVjE4VpmB3UPcrgVKucJmdnr-G522CkDYb5UcuVmIX6tFITAylJdPkA1Gv17LepmqypMOVg7U-QHxAuni_A7WZgkfofpcmFSn0114m4NXt_1AcjtKmkNTwVRpKS4uuufy2SMX8QdN26-_nCNfAkfwkT6sjmNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e821a5697.mp4?token=JmhPigX10j4jz2zdWe2nw5BT4t5goxWTz3GnJxRnPsj4opF426ioMv30jJZuRjoafYZ1jHIlaONj1WnAgkSBtd5oBSJcRcAh6MjQInu_DITMYaBn8vtg4bsIfzKwzIVuYSjtTnWjEZCn1RqjifC-3KH4UY_h-hnoOCllX1XtTcbZVPNrKSAu3F7mpVjE4VpmB3UPcrgVKucJmdnr-G522CkDYb5UcuVmIX6tFITAylJdPkA1Gv17LepmqypMOVg7U-QHxAuni_A7WZgkfofpcmFSn0114m4NXt_1AcjtKmkNTwVRpKS4uuufy2SMX8QdN26-_nCNfAkfwkT6sjmNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: دیروز به ایرانی‌ها گفتیم وقتی شما کُری‌خوانی می‌کنید، نباید انتظار داشته باشید که ترامپ به آن پاسخ ندهد
🔹
وقتی حرف‌هایی می‌زنید که واقعیت ندارد، رئیس‌جمهور به آن واکنش نشان خواهد داد، من به آن واکنش نشان خواهم داد و آمریکایی‌ها هم به آن واکنش…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/444028" target="_blank">📅 15:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec29282.mp4?token=VATBYskqsiz1CER8avpIXvH4SzVyfQHZ3XIURsgO_MDcWEVpdYqWyge-7T4NclTGEOSA2HB_GQ87phUL4Yj9K5L9f_LPsDD_EiQxr81lf2CTk0L4j3FXWSDDfYD4sxMAO0SQf1-WzkwdiPTpvl8pdByEiuCSlc_5vzidsVwjgYG5sdZ5rPsg7-SCGVBqFwUXVIlCrf1nnUUjWZDp13woZhzGshir09YbeD1Oi9MgaoZg3aZkQcgf3Vko2g_wcxWsb6fxcTroBKrYhBTyNkjoiBmvw612kpAVoir1K_vnKzBkeE23Owlk8tY-J1BGcPrnMJvjSGTU8O-3peCpwpMXmqV6xxHX1CvHZGDSbShzFfzqXdmcFEvXT65ukh7RU773NO-tqmY_SMnlCS3NBo3Oeu_gDyzCfVxMgARGxspgLFo2Vrdn3ONY7phcEzvMYmdIHEQysm3lypvcOlDs5LnMi6lLIMCdd144a1nU534Hoy4ksBOEG3u3zm3htidSLMjfvplxs8jXO8KeePR7vEYhugV-NVtCUW8DX3g_rkAqYkuwbgw8jH6a1iF4OGMrD73a9DZrNB7bshWOb1yxmuRt18-HNGO5Qx4iZaT5zN237yE4cvWxe9s01a-VB3j7HihNQtYVoRa4eqdJYMPFWPqlsEOV3GL2u6E41xXYmtZghQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec29282.mp4?token=VATBYskqsiz1CER8avpIXvH4SzVyfQHZ3XIURsgO_MDcWEVpdYqWyge-7T4NclTGEOSA2HB_GQ87phUL4Yj9K5L9f_LPsDD_EiQxr81lf2CTk0L4j3FXWSDDfYD4sxMAO0SQf1-WzkwdiPTpvl8pdByEiuCSlc_5vzidsVwjgYG5sdZ5rPsg7-SCGVBqFwUXVIlCrf1nnUUjWZDp13woZhzGshir09YbeD1Oi9MgaoZg3aZkQcgf3Vko2g_wcxWsb6fxcTroBKrYhBTyNkjoiBmvw612kpAVoir1K_vnKzBkeE23Owlk8tY-J1BGcPrnMJvjSGTU8O-3peCpwpMXmqV6xxHX1CvHZGDSbShzFfzqXdmcFEvXT65ukh7RU773NO-tqmY_SMnlCS3NBo3Oeu_gDyzCfVxMgARGxspgLFo2Vrdn3ONY7phcEzvMYmdIHEQysm3lypvcOlDs5LnMi6lLIMCdd144a1nU534Hoy4ksBOEG3u3zm3htidSLMjfvplxs8jXO8KeePR7vEYhugV-NVtCUW8DX3g_rkAqYkuwbgw8jH6a1iF4OGMrD73a9DZrNB7bshWOb1yxmuRt18-HNGO5Qx4iZaT5zN237yE4cvWxe9s01a-VB3j7HihNQtYVoRa4eqdJYMPFWPqlsEOV3GL2u6E41xXYmtZghQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حامیان پهلوی هر روز به یک نفر حمله می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444027" target="_blank">📅 15:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edf909c74.mp4?token=QoHn-zx5rdi-54aKGHY8rz4uFKdotyIpK2i5g34tCeUaYEiaxJgjSNdFcEnBLSiokf-WFRiVbLbfCj1FHkCXZZ4FVLvF8GZ3lExT2JbeLknLERL5h6tsgaRa7JkZlCYTQj34X7QmGwUrfBx1n8T47AdWMZhuyl9Sivu54P4yPPSUh2AgdbJF2twunFJU8-VVzln6QdJ70zuR3y1vDmWQspMO5grY9R0MxjluoV709s5qZ3PkWPoFQzF9HNDGz0VJ3YBkHttJdZwvEDX3udTpxSodaH0qHAxcW9PIpoisUeHj5_Kn2c5bJpFEJFARxNNVw31xd_DWLexSAHsCAjbHEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edf909c74.mp4?token=QoHn-zx5rdi-54aKGHY8rz4uFKdotyIpK2i5g34tCeUaYEiaxJgjSNdFcEnBLSiokf-WFRiVbLbfCj1FHkCXZZ4FVLvF8GZ3lExT2JbeLknLERL5h6tsgaRa7JkZlCYTQj34X7QmGwUrfBx1n8T47AdWMZhuyl9Sivu54P4yPPSUh2AgdbJF2twunFJU8-VVzln6QdJ70zuR3y1vDmWQspMO5grY9R0MxjluoV709s5qZ3PkWPoFQzF9HNDGz0VJ3YBkHttJdZwvEDX3udTpxSodaH0qHAxcW9PIpoisUeHj5_Kn2c5bJpFEJFARxNNVw31xd_DWLexSAHsCAjbHEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اسرائیل حق دفاع از خود را دارد
🔹
ما می‌خواهیم مطمئن شویم درحالی‌که آن‌ها از این حق دفاع از خود برخوردارند، در پشت صحنه روی این موضوع گفت‌وگو کنیم که چطور این درگیری‌ها را کاهش دهیم. @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/444026" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeUqdnmUyWWUpCaj3ILIrsGQoYOekh4Q9oLSJG2-hgfTWFQaowHk0e6OZejWa5bWursHtosAJJZp4ODL6aubhzh6qotvKdGuJsuQhZEZZW27nyhybtYwDCuWEGLtg-Nv4FJ-OjlbKBu3lZvF_9RDz0syfnXU9K1kE3VtfEYayHd0hyJpIr4cV1QCbNmAO9wCuRQGD3HoUU2WkYIUgZHSJ1O8j0-mSNUyqZsxO_JeZ8BlL0p6qQbVpUJvRaTpx6A4wn3FWwNud5GyD4CQi3lPYUYilcRBxKkReNpn9bbjYpBEx6BUZ4H5YOSk8vrmCGNrzEHkMDpUF8eQSG0bIt77kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcdTJKubRquVa4DkycO_d7VP3y7OroCoOLMpSi_d_aLWxCm3QMm-uutnlAbZiRFf5iVZ-vl_B2MLwre8pKVIoSu9oSM7XS8oBU6oue6-XPkBKRwwnJBHOehm4aKrI7ccPZsKTIdCX0k9bJgdU9TKqQMahGuoq13L24cfhE5rDQYOKEkC_46gvp3KCXhAka5lHbERv_n3Rc2J1zOQxGjlF5CPf9frzXHqRPsz-VQviNRdS5__KZh_-ova7mTSTlP3OnaZdTTMJKOSLBuvpF9KEI5zZR4-UaddimDXI-5UvrTjPvkwSF9tk1_qrBQkqo1fegWpS7wp87cg2AMoFGtmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3IUAhNcDRW4CQAPWGE4O2n3_XxpLsHG6kM1RfRAEABs1TwfSXS1pyedH1C-tVmgXhybAerqFNJC56WED48SYzLREj8wkRSDea5A18heJG5fHZ5v2hYf2Mj2CBOdJNBFTH_YOxjs_sindc0LVmLoBf44j3J-c87VhmlmmWNwRXkdPy7zRutYbYTi6xOeHgkb_3nBHFzboCt0UzLaYTWY14Bl4dczZzlnY7MZQAWq2Jlt47n0rwqrXEl8q30OzOgPKX6HYw2LCnuBqwYzYzmjDzZOCE2eMq0gFXPXIrqWiecEpQiYyblKVNHBEH4z1Xn-Yn9y0QG8J4lphKP501SELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU2dI-6_9EJO5EBflsfSn4ZicUB5rKkfmt0DloyLgXRVuLcVTYWXA2NHUwGh7I8pvJE3MEWahAeoOtL7wjjyZ4qFLgCwNPG7lH_M_SRrr7c1W4LeDOvDdT3S71pnLAKXpRo5BimBhx4Z8f1Fu5l9fnabHFXpqND3VOic9fgIl4EWnLWEWs1_-XluN3EskiZJHZRxqOxLY79i0vSGOOnBAbJ5hSrGBnhxFVO1PwsuiiWmd-gAKhFNMaQisCEYYnTN5l3DQ1dY8FiqkbBLPaYsEYbJ_C6eVBhdwtQkGaH8sRquEiXx6rUBfwQddT7mdDiWA6EfYixjC9khYRhAtL8lTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idT-8hu7SyKcBPQWCDc1mG6_p-YG1JF5D41Qpq_ZFsKgEWKiTn4uvh-jBQtxR8xKbBf0ZCwZfejBghklMfiTvnzKaUSb5FWFHCfGmEiD7UPXZXpc7S2v6_EJH5OiJD30Kk72jpcO6cVkGgf4jMPI6rY_NXsu6nG-o9G4Qy90zyDMr4Bi2iuhQanFN6B_mvdx-zyqM9eGQMtR8MJDXEWr-D6UiXIsFmwe7gbENFZKGs116icvzn0tuA5lFaVoQ3KC9Gum4pQ4-dZl94YEGaifkA1dG2R1qDozFQoD5Zi64nIGW3CPjAv7AhCaJKUi1yJOpNaQJA9BPPSAhaR1ekskXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFt39_OguWaSTyLr3OvfUVMya413wz_5eMvYOyxRfNFFNr_RY7LeJg_9M7B-mCTpnx4umEX6OLbncDmPjXvGFYWLbv0NiV75hkxf5h1v8fzG-EO58bjIIE0taYik1T2iYzV1nFyPlMhamyZQTqsKvv1Mac2yh3ddxZk_9fW5KEtIGJCduDBSWE0M30qDKyQxYqV7sLZAcKoQ-kwdhx4AxAPxKmvxBHHeVjdWF5DFtEC32mPv551ZU81aJSME22cAXReEaHVDaZductfpDxWtw4SLuY4Cs_Psoj5MTu-WYJ2etI7WGO8-AMHkY84RS7TyxoE5qOKUTvdquYWK22mVmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وقتی خمره‌های سفالی بوی نذر می‌گیرند
🔹
هرسال با آغاز ماه محرم، در طول ۱۰ شب اهالی فین بندرعباس حلیم نذری خاصی در خُمره‌های سفالی طبخ می‌کنند.
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/444020" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0fd76046.mp4?token=XxJj_DkgasXXLcTNCnYDo6AxJJlRW1aVHJCWyk2H8YdJgsVkNe_CgTD0mJ_cKHXEAOqJj46cGr-ud3X3gBQhqnUq2oh9ctWS__pp7r9cN2szb-dszHITx4UfkLtkJqYsdn8JG6Awb90ArpeNbFznJZpe80_7fgvwnnsgZa2YIWHPZHdCwFCCT-jlnlHuYIIPcLzw8iXv8dve6Nsd6EDiIPPraJFVpRRU1r1FLuwJ4HUMb_3Ww7DiHyQBKlMeLqx9XYJx8V0lLHVYMQvfDkGgkAUg8rycCmGANfCsarc8gKEySdzAzxSx5gBPRcorRM0HgOh0GRlWwcPtRMsSyooegg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0fd76046.mp4?token=XxJj_DkgasXXLcTNCnYDo6AxJJlRW1aVHJCWyk2H8YdJgsVkNe_CgTD0mJ_cKHXEAOqJj46cGr-ud3X3gBQhqnUq2oh9ctWS__pp7r9cN2szb-dszHITx4UfkLtkJqYsdn8JG6Awb90ArpeNbFznJZpe80_7fgvwnnsgZa2YIWHPZHdCwFCCT-jlnlHuYIIPcLzw8iXv8dve6Nsd6EDiIPPraJFVpRRU1r1FLuwJ4HUMb_3Ww7DiHyQBKlMeLqx9XYJx8V0lLHVYMQvfDkGgkAUg8rycCmGANfCsarc8gKEySdzAzxSx5gBPRcorRM0HgOh0GRlWwcPtRMsSyooegg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: همان‌طور که ترامپ گفت، گاهی اوقات آتش‌بس‌ فقط به این معنی است که شما کمی کمتر شلیک می‌کنید
🔹
در مذاکرات می‌خواستیم مطمئن شویم هماهنگی لازم را ایجاد کرده‌ایم تا اگر شلیک یا درگیری بین اسرائیل و حزب‌الله رخ داد، [با ایران] در گفت‌وگو باشیم و راهی…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/444019" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d26db87a.mp4?token=Y9JOkX-n4vHtkePjHNNf3iGfolxKA_xogcA753MHZzzHd7R0GXT_8E2zpjna2VzlqsTMrV9Sh3LduqabokLw6UjV_3GhIwlQ_c_TY5eHA9uTOASqQf1Bxp_j109meGpsqHny3vNOOJA2UwGOlbyPwYzkih10UfWgTkQ-5BHpmnZBGF-Kb_RUdLD3r-RkPL0Wl1D7hEOp8nMIyZp82smyAHxyUdDIZtfPRykl_2BjRLX9NKlO8QcvQT1B6dp2qsJLeTfhyzDVLzT5F8dmL7gpXb7zSUaYmE9OqDXdBKSHJ9GCciCwB9h2Q_IuS_aKSm6Gm-mj4UjWYYnWHlmSxCS0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d26db87a.mp4?token=Y9JOkX-n4vHtkePjHNNf3iGfolxKA_xogcA753MHZzzHd7R0GXT_8E2zpjna2VzlqsTMrV9Sh3LduqabokLw6UjV_3GhIwlQ_c_TY5eHA9uTOASqQf1Bxp_j109meGpsqHny3vNOOJA2UwGOlbyPwYzkih10UfWgTkQ-5BHpmnZBGF-Kb_RUdLD3r-RkPL0Wl1D7hEOp8nMIyZp82smyAHxyUdDIZtfPRykl_2BjRLX9NKlO8QcvQT1B6dp2qsJLeTfhyzDVLzT5F8dmL7gpXb7zSUaYmE9OqDXdBKSHJ9GCciCwB9h2Q_IuS_aKSm6Gm-mj4UjWYYnWHlmSxCS0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: همان‌طور که ترامپ گفت، گاهی اوقات آتش‌بس‌ فقط به این معنی است که شما کمی کمتر شلیک می‌کنید
🔹
در مذاکرات می‌خواستیم مطمئن شویم هماهنگی لازم را ایجاد کرده‌ایم تا اگر شلیک یا درگیری بین اسرائیل و حزب‌الله رخ داد، [با ایران] در گفت‌وگو باشیم و راهی پیدا کنیم برای متوقف‌کردن این شلیک‌ها.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/444018" target="_blank">📅 15:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444017">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596445e94c.mp4?token=BbvZip5mvX-FF4RH1YDUelgtX09hbBmU5Wc972Z2qCXU2LZrF7VkyJLvV8w9LUVWAABSdI3Zfx89xMskd2A7g-x5Lhq5pO2eZqytLJxKYoz5Q8bny2w8Nf_iPeVlU6-L0SzW5we9449a28PH11T2xds9KPnZ6AcgNID7dQAR85iJAQpN5cZWxaJ3ZWPGvjIeRFVFabfeWq8Zu0sOeJBJKIrpjq6sCMoaOZ5wHUUpUKCmjPyDPT6L3Wf3rAhvHYEqumuUDnbZZD8_ahz3W7t79v_KahJhbc3wN2-uRrbRQ34xsadU0ZNnUbcWbbMok6ivwSUb0llnQ_zPhl3mCX_Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596445e94c.mp4?token=BbvZip5mvX-FF4RH1YDUelgtX09hbBmU5Wc972Z2qCXU2LZrF7VkyJLvV8w9LUVWAABSdI3Zfx89xMskd2A7g-x5Lhq5pO2eZqytLJxKYoz5Q8bny2w8Nf_iPeVlU6-L0SzW5we9449a28PH11T2xds9KPnZ6AcgNID7dQAR85iJAQpN5cZWxaJ3ZWPGvjIeRFVFabfeWq8Zu0sOeJBJKIrpjq6sCMoaOZ5wHUUpUKCmjPyDPT6L3Wf3rAhvHYEqumuUDnbZZD8_ahz3W7t79v_KahJhbc3wN2-uRrbRQ34xsadU0ZNnUbcWbbMok6ivwSUb0llnQ_zPhl3mCX_Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات امروز اوکراین به پالایشگاه‌های مسکو  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/444017" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444016">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igTUakqyCisvkFIZ-qPDBcbjdPbChtx6ZwWaLqKkdvXa_3s92A_Bv4-CbtR247Mdd6Tn_hh4LtMkm1OzBQWvVRW7sOXhdxeGwI9QfKDHBr_6jH3OvJ2v-lLk9Jt1kd7YYPFChgM-XUBw8JIn9X9z1hli4EZbxCZ1Hk0bwbyKv7zm81Cof9xF-btGWSRzU2FJ0zmSIOCTlMy7qveKpyqqCSmmH-hQCXfIIINaeKbfzFxzKNXGu246ZupH0yUv31yWd_EtNk7aQmi7aQkopoFpX-kOWdiroEPXeJ6P2-rNeLscyTUMJAgFMgbdc8jqgO5232QGx_Fa6Ms57IsfOXXEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم صادرات نفت و پتروشیمی تعلیق شد</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/444016" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444015">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS_eTnJb6hw3FH-cOjScVEdfTB1w1J0lBR903oX6-kk59E54oOz4x9a9ponBjZ7Hv9R8ihx-Bxibwny5gHFgqdv8r8cG3BF0hPkKv_e-xZ3VfovmSFcJNaiLIrTfX42BvRqUEi73ONMbsl8l7FqKb_N2XUUAW-63rRoVSwetPAqu8EtuDG5S1401yxS79JskoneMVnAYZ3utAQhDcbigq-7OpioZKTs6-XX0us8oCoHNtJDMy_YB240ygX7uVts3wV9oscnI9rzIWEeuRY6A1-Zj0GH8cLdFfPIpH5Mj5hSL548qo7xXVOsJOKUS_RcRtmAxlJjqdC8MIANT1HX4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ مذاکره‌ای دربارۀ برنامۀ هسته‌ای ایران در ۸۰ دقیقه دور اول گفت‌وگوهای سوئیس، انجام نشده است.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/444015" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444014">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4929d7f10b.mp4?token=jJYcBltWF8OldKOcmZ0KVwBiCzk9n8xU8SzYlEBH7lZlH-EzkYar7SHHb_7Rm3iRe3jKfsiGpA1XAZuE5fFx8wjrWrqRDK5opaLUmGlwzA0uaJC1yo-QXVvxExT9FosvSRBo1UvoqmgUG7nom7lBdE0etrgaExYVEep8g29N7vD6E9zTR8QcQHH-yoxMyQ2fY0e6vP_C60KZ58d7WYf-w70va0p7H_aVuocGbtPeUvYt7bm93H0Q-_vnAmlyB-UVdpQD5mbSGHVkPdZ-4FYSukSAFgNXSiwDkxiEzWERqS0MCx6OldDUQhvZ7JLyDmp0SGtluNSdKmDBvyeYUyLwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4929d7f10b.mp4?token=jJYcBltWF8OldKOcmZ0KVwBiCzk9n8xU8SzYlEBH7lZlH-EzkYar7SHHb_7Rm3iRe3jKfsiGpA1XAZuE5fFx8wjrWrqRDK5opaLUmGlwzA0uaJC1yo-QXVvxExT9FosvSRBo1UvoqmgUG7nom7lBdE0etrgaExYVEep8g29N7vD6E9zTR8QcQHH-yoxMyQ2fY0e6vP_C60KZ58d7WYf-w70va0p7H_aVuocGbtPeUvYt7bm93H0Q-_vnAmlyB-UVdpQD5mbSGHVkPdZ-4FYSukSAFgNXSiwDkxiEzWERqS0MCx6OldDUQhvZ7JLyDmp0SGtluNSdKmDBvyeYUyLwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برف‌روبی مسیر کوچ عشایر در روزهای پایانی خرداد
🔹
روزهای آخر خرداد ماه، موسم کوچ عشایر خلخالِ اردبیل است و این روزها مسیرهای تردد عشایر درحال برف‌روبی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/444014" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444013">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYON9Ab7QCx7d5J_3pv3BFxZFZBaeYPVCHvKA_ehPKtJnhhrOpnwFmOxImiPmPXMqtd5gKDp6SI89JIsIx-9SQlGEWpvYskhNkjoDTcOpHq2ROMcrvuMxqIpV-AX8IaB-tdNOqAdVbbME9h9GC7DHIFGkZw-AbKWSml4JQr6vbCcrPYsI6dPPGrhH0cuuNa0VDGryUh1PomumShr4FCIWhKUxVEKPNH5hKuIDeWfCaPYw7jroCCVt1qg1hChdjKF9a_Daj2taVuTNgKuDMibluupeYoQ34X22ubLvegS-6LflN5lRBnLIQE2CZYrTGI6oUspU_AAykDCG9wPxEvmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال در ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/444013" target="_blank">📅 14:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444012">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjkDcL1LqBIpohkw7P1SbQLGBlYwjrDmXaQfOKLIk-ocahDJcMcKJSq8TxCQBRCbVtK-i4JKFJmUokiyWKwPse_tTPp9WF_Bn8sgUqfWhHLuRUiUcS5CyltpLuaEgVA1MwWISkLZ-GGwqZ2f-3LmN4yb6J-6ZRRHCBUvH2SYNZ7aSQqaKeS73SVIXoXODEz4BATr3epXpKsOvHqx0Kwt-xfvhopJdnbsxOsKY1EoKf0O1E3Qqfx1zKDPaevAnw39S12aKLeaeM6-VA1qLH1Vg2Lv8wqDYeKcBnCTuudRF9A9kMy-AdBYQ7jQlGyCmMVxMNKkCRHIt986SS18Ilb3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال در ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/444012" target="_blank">📅 14:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444011">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XnwuhF47RXzYDxvR3gbmLnrD0hTNAFV0UyBAoWhw3SqO_PziIGz2wMMeNSItTfjy2S99c1F-dpk1SWtbTezkkbYOva8jxLetjrzPzvXtN-KgHA15i5KZ3V4Fcc6r8pFRAnYWWKL_a_aOinNoXYByV6dRtcShek-Y_omP9tcOrAnphQJuneMQp8ueeVmd5-96tWPiRDKfvJejVjjolzx05a60_xZc-uylbESHpX9zclyp30DCysXVddjLvn95Z3pl5jDnH2qcUnax-TEXbN3CAxaMMCC0I_7v8VFuTxU1zXeFumSNh1uwodQi2dW0kxDCBWLRgnIRdOWCwvN3r8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی روضه‌خوان حضرت علی‌اصغر(ع) شد
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/444011" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444010">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
🔹
المیادین به‌نقل از منابع پاکستانی گزارش داد که انتظار می‌رود رئیس‌جمهور ایران فردا عازم اسلام‌آباد شود. @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444010" target="_blank">📅 14:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444009">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2b8417da.mp4?token=E65GKRryWzc4SVt7bwsJWHYtiJpkU6lbE8_3dCQOg6rSJTLwPPBYMaZ7xYUX7eZa5wJeS_T2PaZxAxLrJHlcPC5drUv47uv6Ce6GnhU4DDGEjj3DMyqUe4FA4OcyeAyobwX9dDDqwTloJH5uQAuS6lGHyP1fufqr-YLiOSRJKHello6jigGwT7gOs8xdT3ZeHYuQ4teCc-Xem27skvOaO8eJwR5blS_3p_0Fl9U6OoaXFv1FTObUWzMaX_leUbos7SLMehXPeMM3acewBWOfohcG18zGDgBgq4TSUhzDW2FVpn_IZDLcTlRM4UVKJYwZatpziwhH7rynld5Xt_hl-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2b8417da.mp4?token=E65GKRryWzc4SVt7bwsJWHYtiJpkU6lbE8_3dCQOg6rSJTLwPPBYMaZ7xYUX7eZa5wJeS_T2PaZxAxLrJHlcPC5drUv47uv6Ce6GnhU4DDGEjj3DMyqUe4FA4OcyeAyobwX9dDDqwTloJH5uQAuS6lGHyP1fufqr-YLiOSRJKHello6jigGwT7gOs8xdT3ZeHYuQ4teCc-Xem27skvOaO8eJwR5blS_3p_0Fl9U6OoaXFv1FTObUWzMaX_leUbos7SLMehXPeMM3acewBWOfohcG18zGDgBgq4TSUhzDW2FVpn_IZDLcTlRM4UVKJYwZatpziwhH7rynld5Xt_hl-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رئیس بورس: بازار سرمایه از مرحلۀ تثبیت عبور کرده و در مسیر رونق قرار دارد
🔹
برای ورود بازار به رونق ۴ برنامه داریم. نخستین برنامه، تسریع در عرضه‌های اولیه است و در هفته‌های آینده شرکت‌های بزرگ‌تری وارد بازار خواهند شد.
🔹
توسعۀ ابزارهای مالی دومین برنامه…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/444009" target="_blank">📅 14:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooWVQtbbTBWsKUBqbBCXiXOt9KUrYZtoNvqxKfwHLLmkHIeo0m5jekGGsIzCNCf9HtY5TjZGH_r2kN_B6yvbswDAbNaJeqzXkJ0yXc969lYUCKfgQ179hy8SI78mRSYkd_vtHsKgPYPNjumq-qOykcIu62xUZkapIZseqSs4ElWBSyAaIJt3TWUGElnVwLPBZFyw8ovppYXy5Wl0BvsGkRk7PGDCGQrNm5CU-95wPbwp7xTDxtvCz-XxsErALhsy_-PUOojlCSawFy4yhr_6x_jZzXp3V-2C8Bl1eM4CWJGyG3Sj6YtJUnpsJhjePWptVXBZjiAiFkzZUdo_WNIQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvPdnbsrsEqaP2tFpKeKRyZacsRchbJXp4E_Z9l8JXKWXk983fxriBV2mntHDvixwc98RQrl4H-f3Ut6afuXygSR8XYkOTqUZjlXVtF9z-XNAMxbHaectB0BEYO6XsiMkUt8cHRm0QLXY-yTDkfvkdQalnBzBjtaXh63fLgRg03h0ZpD8GtQ_WQ8LlEfacb10-gKlFK275tTqotgtaJN48vhMec9ByM-MiFY4UvUNa1C3fgDfUb-M5u4RaK4Nc-VxwnzIwexocfn4xtn-Vr_vapCQbJ-JC58RGBeJ3IUdRNJ40H6x29HpKbYKUDDfmQY2NQquSmjSKm9Pucog_8gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXlftBeHoaCwAyf4ImcuNa6SH7o4uLSaGdjNHmViKhsHCZuIPfb7oogqDvuj6UapG3ZpvedHxNdBr7s3FQT59ZVKj-tTVibTSxd8U68f32HpVdZDl5HMf0Kvin1pp7IMC1MiFWfAPQdtnu1dvXkoix0MdZ7lDOE_HcSEf0WV_ssu5mRxAwuZWWHZvlPRTFz3GTm81VLG7cl6mvjVHg4ps2Ip7Uf7DBeAhw2ZM-uBYC4MfPrAPjjhKK9xyJ2h_pVh0hGJ2gZ0k9UoekuxxIk_SB-rLe_S4kj-wKwQ57SFi3Jen3UT25MJ97Pol3C0sycCQ5Gt8l3xCBJvtnZtsF29VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-ZQVBMoMded0hFQHRXLwzDC0oI9OEym626A9K0uPPzjuGJsPnE9WBM18Xxi3zouGpSyCfqHPRht4nSrpiPOXEKyZSpwGCEDR9hEPP3JKA7nhpZfdZE0BHUJJBkWlI8lT-CVao_AXx-tZl8O2pIrM-kDWvoLs839ZGUg9vitM1gNGbeZJ09GGJZOzBIOdwPumLOGkXNtbhjMMxoSm75E27vS8LT3swgCNtvUmjuAWCVwypaxZ2a-OBi0os3W6CpL5ZisscrvAymCD8BrV2SPu2zGnDPv-cCw7jCK0Bo1ncxmVOAb_DX9zgksbVzmHKPfpHzERqU4CenuRCnSMdnzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK19m7xZxWIZa_ziSQfk3oRspXC9J8eiEiMfx3k9CevS2rlvgUd9V6_NUxAdHBeW7TZ7AGtSGWt6IVR5wDX8r1jXz8D4XVZc6HPK1eDAzxLeuS86mwAnDxmXbOaXZET4onZ51C1pWZqlZE0J7mo8cOqQgVeFdA7UHfaHigjjMU8ZRSfj3T05tv4Gracl5fuOygcRqKJ7teLe2J_44i7ISNHfxXLHeG9aO_S1y3-UwZLke9JrcsFOa5-W0qEXE9tYIVWzmCVdJZGA0Fdg8Ha1KcFr6tem4grADq0ISPMFWBocrcQufchzSjwBM-ZO81hwkKzHShoCJ_z7UWxm5bjkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGW5_rniYycfvj1wmNOJqC5hkuWvJZerwY-ZQjvJkJq75u_9cdR17xNKoiItYR4Lq_rkX_ndRJG7Mi9G6TFOTY4oOCI5hBSwQds7gKLhD-eQ_fz0mL0F4p1Mb10oXO6uRRoZJHmRop6910oNbVhxwE2U0OW8q5Sp07HL1eoAXLum1moLOm_2hic2e3c5XfOcpYNd4BzG47WxXG8eT_OQBQ0daJAjakh16OxjyGbWZerMQC4gDCuXFPegnkO_HE4eLiytadqgx7c7fQ81s07HBigWTUqQEuMXFSMSWGHOoMG0cbXU96iuIdct_pZNbKG2d_4olx4FoQERdD-PeYTPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRlO4qz8JkK2QTS-y8U6ukqU1-z0T3WwDq5YOn0I4YbElWzyFn9vztlfp4sVannmq-0PQbxssPLb1QKDpPUGkFq3r6n8y_DUxMqYOqX3wpq20p0oU8cMrcSPYmcd0IDfDusa4clzbRwcOXiY36qJ4isBsWANmvu9BpHfDL0OMHl1lbBO_e_5V0wpwekJmRRuay061yHR8Ke648ZoLJaKAdGuMtRd2q1TO9aMxOO8IiAIKBFxV_AfgFEiilNY_7NtRGBMm0v51Mh6KqNRRrGhHzELX_GsrVWDlV1bQfh2pbJEcufdGyhiYNVC_a8JJteig1bYc2yV2OWu7jPXLhQYSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهرۀ این روزهای ورزشگاه آزادی را ببینید
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444002" target="_blank">📅 14:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If6Bfasd1lP3TuGhx8YzymDJSSsCAFya1O-N8LvvbnNJdElORIgHUI2I3oHcVL0sSh4bvj_fKPFHj6cCXGYsnzV9MCPPumhUnehtUo0YWu4APQ-MtFcjrvBEfwiAnuJKg9dQ44HLh_5mV2ui0evcXAyDO7bUK0C0dcj_PgeDggTDH3XgRqVRSmhUKdFNlGQnaUCVDZmDkvhuhAC9Z-RJVuBzW3ayYjGAnMCvyWCXN4KmBy4nJSFItajBB5-5c_ba4FUZoqXVLMX388UVNw7u3TQGk5yN9H38gymCVUfqUk-uSBudqqgZVFrRKdrxpRXxFC1PQ5-6jO_-x9w3DpzQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دیدار مدیرعامل بانک شهر با مدیرعامل شرکت مهندسی و ساختمان صنایع نفت (اویک) تاکید شد
💠
توسعه همکاری‌های مالی و حمایت از پروژه‌های کلان صنعت نفت و گاز
🔸
در راستای تقویت تعاملات میان نظام بانکی و صنایع راهبردی کشور، مدیرعامل بانک شهر با مدیرعامل شرکت مهندسی و ساختمان صنایع نفت (اویک) دیدار و درباره توسعه همکاری‌های مشترک به گفت‌وگو پرداخت.
🔸
به گزارش روابط عمومی بانک شهر، در این دیدار، ظرفیت‌های گسترده بانک شهر در حوزه تأمین مالی پروژه‌های بزرگ صنایع نفت، گاز و پتروشیمی مورد تأکید قرار گرفت.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/444001" target="_blank">📅 14:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8CmEiEGh26uG7Nl-23ynPxcNYCuYOafAF4GWufqCSWYxG9ge6XFjP6-F_RHNgH_1txNHal26LAboHIBjEhokMFB18d3vuC4sH3uq_61Z7wv63EZDGBgrCKTdlfMAAgR_SfUxWv_afg0VxvmZoCEWwSf5hnR8w-oq4Pt_OzkMBNJHcuXoFV8Q-eX4dH0VsLF6uf73_ya4zvpGZQfbzhirAoXG2L22uPtGzAjH4wE4ZbFwoCWrahvLJHYv3oxSHXzonxNvWax6Ja_IpDrP37VWbVc0Le7DZ2T0pc-at_79MbSbGE2bk00Ko22JQlwr8JmRHOdAYd14dx6j5ZSsNeStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در جلسه شورای معاونان شرکت ملی صنایع مس ایران اعلام شد
‌
🔰
افزایش منابع زمین‌شناسی مس ایران به ۲۲.۳ میلیارد تن/ ثبت عمیق‌ترین گمانه اکتشافی کشور
‌
🔻
شرکت ملی صنایع مس ایران با ثبت رکورد ۵۵۰هزار متر حفاری اکتشافی، افزایش منابع زمین‌شناسی به ۲۲.۳ میلیارد تن و حفر عمیق‌ترین گمانه اکتشافی کشور در معدن میدوک، دستاوردهای جدید خود در حوزه اکتشاف و توسعه معدنی را در نشست شورای معاونان ارائه کرد.
‌
🔹
در نشست شورای معاونان شرکت ملی صنایع مس ایران که با حضور دکتر سیدمصطفی فیض مدیرعامل شرکت برگزار شد، مهندس شهریار متوکل معاون اکتشافات و توسعه معدنی گزارشی از مهم‌ترین دستاوردها و برنامه‌های این حوزه ارائه کرد.
‌
🔹
براساس این گزارش، شرکت ملی صنایع مس ایران در سال ۱۴۰۴ موفق به ثبت رکورد بی‌سابقه ۵۵۰هزار متر حفاری مغزه‌گیری اکتشافی شد؛ رقمی که معادل حدود ۷۵درصد کل حفاری‌های اکتشافی ایمیدرو و شرکت‌های تابعه و وابسته آن به‌شمار می‌رود.
‌
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6Rc
‌
@mespress_ir</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/444000" target="_blank">📅 14:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/443999" target="_blank">📅 14:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۵۳ هزار واحدی به ۵ میلیون و ۷۳ هزار واحد رسید.  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/443998" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtyvfKrooZRPvnKPKMjntzTUGLsdNaZwfxsqxoPw-VgAiGCx_CgF-MsQlxY08jWN2bCaIqdBYLOFhLbjT1VJqsn7YBzSTUQaRnnigybV8E5ddrFUMtdOF3j96vPtxCCh1MoPLDzmlmH3D5U3NGtJ7_SNEO-wclGtT6sqO3Kzc74lAW0IbuihsIvdLbOjaWYuVKF1edRslhcnY-AwzEYuDAc_t1dF2Tau426kXpi1Aae72mabYzjC1pNNleY8JqfoBRmwO8JJBqkKCLN1cKj9Klghd1HOPM0srRcXgCQ0koGG-YSfh_XlC1EsmB-TOieUfI2i6dogDWGOsgIzfk6tCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنگ تحمیلی اخیر ۳۵۱۹ نفر شهید شدند
🔹
سخنگوی قوه‌قضائیه: براساس آمار پزشکی قانونی، در جنگ تحمیلی اخیر، ۳۵۱۹ نفر به شهادت رسیده‌اند که از این تعداد ۳۰۰۲ نفر مرد و ۵۱۷ نفر زن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/443997" target="_blank">📅 13:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwQYNQ92hD5YGqQN29gCpXjDDk_AiMoin1Dd1hvEXn6vv1SzksFfAqbgmgRn5HB72CnR9ihXDu1tCLGxuUXXXBW88Nzrza9bXUy35_wJ9VxIVvMnJDkyzGTKGC4t2j8gg1LQqtcazEujXZDiLHj2I1DX0kEtLVJuCw1NeG7GoEI1mphNLIAcokw4nZSH7ngZXziEmto62HzLYQ7YS25K1bz86DQ7KJ-4SR914m_CCBRm3Zyf_l43eLNsMIcrNZ8BvBodjCZj_qWG_gWJ7Ehr9iUMrJ9kKcsW18ftPNV7AgAPRsl-bo6wR6Ki81bgLPPAdRDjroP7YQ2KHLHDepJd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاره بلژیک: دروازه‌بان ایران همه چیز را گرفت
🎙
ماکسیم دی‌کویپر، مدافع چپ تیم ملی بلژیک:
🗣️
من واقعاً با یک حس خیلی بد اینجا ایستاده‌ام. ما شایسته پیروزی بودیم و موقعیت‌های کافی برای بردن بازی داشتیم، خود من هم چند فرصت خوب داشتم.
🗣️
امروز از آن روزهایی بود که دروازه‌بان هر چیزی را که به سمتش می‌آمد مهار می‌کرد. با این حال، موقعیت‌هایی که داشتیم واقعاً کافی بود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/443996" target="_blank">📅 13:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mipbi23medAuqMKMm1Y56JJ_C5XBOD3LYYQdzs_GeojFbt-HwkXJ6_r9bwV6_G0otJcX8CYvEza7HTgznMyD0pKLR2NL2pDN1J-fTN0j7OTcs_HmT0y_eVI0ejRhoIJYTfQfJoif2kPFTt9Nkp3v8DtGx0oZAIIhNJVgBn8YowchzlAzpvcPn7HDxcQGAGR6FdobBF6BPS7Wu4_PNHtWVmWG9nclq6srT643tKhk6Xri-gfHBepYJDbWuyt-MjxAtyP6MqeWn5l0ux4-ixlUDa_SdbXTVIVoIMSXQKqOnV6x4DzAcWsm16bY24mWsxb8YaHEc5zd_5bipnTGEX1rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
🔹
المیادین به‌نقل از منابع پاکستانی گزارش داد که انتظار می‌رود رئیس‌جمهور ایران فردا عازم اسلام‌آباد شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/443995" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAFIZN3PXvrWhOcnn2-qCwW7yz7pl6LHsd5Z6pso1T08oT31J-D3aSr9DmED376LVuu3bpBTwk5hD_WzYt7t1Pn0xvqrD8p51T2PlMEgb2CZnEPKsaiKewTBbLyIlVt_9ZDZXi3RptIPtr8RrvTOlr8IjlJnmumeUmGqz_qiqZkK0Y2YDqL_1iod_HSu3RGyE8ctob6hgQCvFoJ1_1-nF6OU08NIHhJXoFnL0Dzwp8HggwRhJSVTugPJYrYgH6g3SxfRI_Jq0yUb5lTDbo4T7Pol_0SFxe9BpqnQqJMBjF6ky_tA6jX_MqUB-hi9--p1vLjkj9prxP5WVZ3OgTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ لیتر سهمیهٔ بنزین تیر خودروهای شخصی شارژ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/443994" target="_blank">📅 13:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d95cf9b1.mp4?token=fQ4OoboVzO4YVCAMui7LW-W69L3yqOBIjw0qR7jFEQW5XIpcrwHIHVPEp8ImuUFiSLE_OJ9sHDZ8pDy8uhQ62caPHfqxjJ94RVsdONp3YLTtbWyM1CWT21he4Wl5VqKajlmG5YvB7m-UrWvu-BbR4RPw8myJ7WibNdkG4eEtrOY8uiaCAafz3c7J4cRNUbUIxnFEJw4XYaj498koWB2ZmTUgD05egnleRTODqlyLSFapQXFB_vyIMMBDfyDcdIzmhDI0xhk9f1iQsE6MjwL1NWejbcONUl5NlCU7AEklYsLzlzZAqEItDk2CBPX8WWAW_BksPD41sKh8lQ9MARSQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d95cf9b1.mp4?token=fQ4OoboVzO4YVCAMui7LW-W69L3yqOBIjw0qR7jFEQW5XIpcrwHIHVPEp8ImuUFiSLE_OJ9sHDZ8pDy8uhQ62caPHfqxjJ94RVsdONp3YLTtbWyM1CWT21he4Wl5VqKajlmG5YvB7m-UrWvu-BbR4RPw8myJ7WibNdkG4eEtrOY8uiaCAafz3c7J4cRNUbUIxnFEJw4XYaj498koWB2ZmTUgD05egnleRTODqlyLSFapQXFB_vyIMMBDfyDcdIzmhDI0xhk9f1iQsE6MjwL1NWejbcONUl5NlCU7AEklYsLzlzZAqEItDk2CBPX8WWAW_BksPD41sKh8lQ9MARSQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا به افتخار ایران کلاه از سر برداشت
🔹
واکنش تماشایی بیرانوند برابر بلژیک و نمایش دلاورانۀ تیم ملی در جام‌جهانی واکنش‌های زیادی به‌همراه داشته است.
🔹
خبرنگاران و کاربران شبکه‌های اجتماعی به نمایش شجاعانۀ بازیکنان تیم ملی ایران مقابل بلژیک در ورزشگاه سوفای…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/443993" target="_blank">📅 13:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2JSLCVsHNfSL49YvX0sqidaaTJWHQp10cqyBjvK9ZQMrkxIoj80PHI0a6yF1MEr82kpNIzKWbMZU1jbIKQTH3cam8oP_R9f5_cuipUskzw1H1AA9qJwFtULRxTOnr0DUHeJf4Ud4BKIZMhtGmKbKYm3ztMYIO82pJOdz3zUc9VLI-75S_l3FygepowmXdFss_z0QNbVo3pa73uJZfKYDZen0NJA8ZTw7rnz8vBUly7HL_K2I2KRE0aZMco7_r43LmBHY-_5XeXTouVwPvSvm6NwrfuQWmmQOUkatgfjrcCXmURZi0riiXFamGjBVgyIKpXi-FzhamfcEMpFA119Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
پیگیری خبرنگار سیاسی فارس از تیم مذاکره‌کنندهٔ ایران در سوئیس: کارشناسان همچنان در سوئیس هستند و روند اجرای تفاهمنامه را پیگیری می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/443992" target="_blank">📅 13:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=spln8eT53BFTl_PuNi6RDoJSa_qPGDzEaBrzqKqGGwqDMVCO0RFcT26MSY4g_1BUHZ_B8GmMEpjD0T_pQa3hYlURaj1bJmF4W5ErEQbiTOesrICR4nTK3Cp50zoaW-FO8rCENlAbWtOY7FutSHMth6SGAykRi9L-GGdj_57WUq4xBxIVercuM6NfvKadYZ8gyQDLWahQCvsl-UfbJGncK63_arEjIl-90GUPzjHZhHdOCHGToXKwjv56aHwBsA_AqfvQf5jPqy4wy3rk7YXgl0p_LAbOKEe6KXrRUcqvTzYgp4Jxr6rIVZWnSZ6D76oeZYvg0U8ZHqAWbKzeIsiH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=spln8eT53BFTl_PuNi6RDoJSa_qPGDzEaBrzqKqGGwqDMVCO0RFcT26MSY4g_1BUHZ_B8GmMEpjD0T_pQa3hYlURaj1bJmF4W5ErEQbiTOesrICR4nTK3Cp50zoaW-FO8rCENlAbWtOY7FutSHMth6SGAykRi9L-GGdj_57WUq4xBxIVercuM6NfvKadYZ8gyQDLWahQCvsl-UfbJGncK63_arEjIl-90GUPzjHZhHdOCHGToXKwjv56aHwBsA_AqfvQf5jPqy4wy3rk7YXgl0p_LAbOKEe6KXrRUcqvTzYgp4Jxr6rIVZWnSZ6D76oeZYvg0U8ZHqAWbKzeIsiH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: صدها راه برای عبور از بن‌بست اقتصادی وجود دارد
🔹
شما استادان و متخصصان حوزۀ پولی و ارزی گردهم آمده‌اید تا راهی برای برون‌رفت از این وضعیت پیدا کنید؛ امکان ندارد در دنیایی که در آن زندگی می‌کنیم، راهی برای خروج از این شرایط وجود نداشته باشد؛ نه‌تنها یک راه، بلکه صدها راه برای عبور از این بن‌بست وجود دارد.
🔹
چرا مردم هر روز وقتی از خواب بیدار می‌شوند، ناگهان مشاهده کنند که قدرت خریدشان کاهش یافته؟ شما و ما سیاست‌گذار و تأمین‌کنندۀ امنیت اعتباری مردم هستیم؛ پول مردم را می‌گیریم و زمانی که می‌خواهیم آن را بازگردانیم، دیگر ارزش گذشته را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/443991" target="_blank">📅 13:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c525fa3b8.mp4?token=Gyl7r5kPVpcS4ADtDJ1lKri1BiW5IRTjDOvGY4HcaE6xXW9CQbwAGv9G8OQLk9V4TNEv3mb3P4jUgDKHXW1408U7tUFuFtW0h3RFWanFTWFduSXO1LfpwWPkKDx8vwRthO0d2LaQkjeRUjWc_Kw_WNzsH5P4AgkAzpuZH4LfcbEu-gsc0evqUou_GpvKsQpHahrbmIyzAft6pdUTCMVb-z_xrdsRpNlF0KAhnlKFepdVx26o_7aX_UuEeFZoFduwGuqLzMA48JZsgExN5hfKLLn4hCH8s453qRJQbTgC1AU7W9GgdkpjyGXjr_pIKP2gXOt2v4zGFcnbprp05Gf7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c525fa3b8.mp4?token=Gyl7r5kPVpcS4ADtDJ1lKri1BiW5IRTjDOvGY4HcaE6xXW9CQbwAGv9G8OQLk9V4TNEv3mb3P4jUgDKHXW1408U7tUFuFtW0h3RFWanFTWFduSXO1LfpwWPkKDx8vwRthO0d2LaQkjeRUjWc_Kw_WNzsH5P4AgkAzpuZH4LfcbEu-gsc0evqUou_GpvKsQpHahrbmIyzAft6pdUTCMVb-z_xrdsRpNlF0KAhnlKFepdVx26o_7aX_UuEeFZoFduwGuqLzMA48JZsgExN5hfKLLn4hCH8s453qRJQbTgC1AU7W9GgdkpjyGXjr_pIKP2gXOt2v4zGFcnbprp05Gf7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین کشتی کانتینری پس از رفع محاصره پیش‌ازظهر امروز در بندر شهید رجایی هرمزگان پهلو گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443990" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edaiRe-p9THsR12DrXi10wC7nkMibeF0uwr_XqsWploHeGaNpAdd4RfMjEe9YH6DzyjfGB5X_LXlehEdDoK2NyosHoco7cB3UdnG7T_W2Ku-IteeY8B3l9Q1jlcCi6RMi28Z1KCeCX6VEuglBsOzWc5Z85V0l7nmgElmxB2YSZkWWYC9D5R98Z7hexSYgNTA6bwZ0v7JExf3kOxHeOVVdMziHbW0gxVf4YFqaq2apQ9Fv2HFGo5Js3U8WqV_U8NCb-Zz6Ft2IG_gW0zmlLGjDo0CfxGngbAHtSAoElQ9juZJFm5xfU8gt8ULtiex3la1V0uvY3sFb67o7nokDUwwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJTqv5kd5FrhPpjMSZ_rvEE9ij1dXbo_58mfM3goY4-GPFT-75QoR6nqg_tNpA_ATtrfoXESqiGOJpu_9FK2RwmEDvo8ezHc3n4fe-tR1PfrY2dYwQaFgOOuJOiGTAPyvxhwcZfsrxBebTm94wF1Phjp1hnK5OCaAWkiQGJKtIFQqq75xt-qUUOoBjVCNOiFj_psidRptnoN9tmOx2lv2gGhMSdkYWCuUYnTyB2UwV4t2l_ZhYd4FiBlkJ7_VXND2P94XVZklwH8EBevqoshpA78xugNwKr1-pCYn9TnTyT0lBNxEXeJRc69fueUiTN7EtcgdJgllP2DArtl6IjsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPzQGKfTGUgRcTTMF7DwLGpVxHgX3bBfY20u-7UjRyeP6CuaVt8xYgcPd8_0lyLqCpG0H4tD1fCuwyDYRCwNIp_ryU91JIKfZ7y1kjijxUDeoEw-1DGk7-wS3qLrY2D9xWfTcUeKxPSOxM2Esdm8RkqoqdJsCycNxS3Fwf5uLEB678f5162yBNNmTwMBJzuMEexCSTXESaIHzfhhKvn37twiIfJAEHKe0cEZSjcRNIDur2l7ExvdFxCXrMm67QWnspkQj07875geUA2P0keojlPcNti2QHoy3h6Kl-ylBdanmSwZbVFNZ0FEZhz9aLmiVN3baosxg4uYK-sLtEd6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjthyKxjmyhFeQjrRtcZJFHw_ETHr9RwGuolhbf66bVSaccsU7KFEqnb3kriJnzDgILBQZbk1eW1ZZXr2SIsMheCtS9-XRRZtrkFNjGj5S-kE2ESlYfm9dwNQErfJZTPXUoqMFxoD0I_Wr7_Y8-gO8yrV0mS8jFl_Cpji66aXkQwGNXkPTnFvDIK12EaTBQZJRzU0tpdT7d2yXQDZ4PR5aRAB5juAYkDqZpU3b5pH29u6oehpAdYIKXIN-jFVWO8xHkOiRTdMF9loCVuqHn-0Iq4QEmGuG5v1WGA0Fb4LkGbtPC7zPBk4q_SiC26wN_TiFW0dJzMp_eoirEtjH7L-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتشار تصاویری از سردار سیدمجید موسوی و شهید طهرانی‌مقدم
🔹
تصاویر دیده‌نشده سفر سال ۱۳۶۳ جمعی از نیروهای هوافضا سپاه به سوریه برای آموزش پرتاب موشک اسکاد در روزهایی که ایران هیچ موشکی در اختیار نداشت و امکان خرید آن نیز فراهم نبود، سفری که بعدها به یکی از نقاط آغاز شکل‌گیری توان موشکی کشور تبدیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443986" target="_blank">📅 13:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoZec1DtF8wSMLA30UH8NfivqboOsrSuPrBFF9chQ33NtNpu1XCf1V3b4_jczMqln7U3rPEt5SIOShLTo_a4DEmfYyYrs4rkC0vBEKFaPTeVscpM2Gd31WKAVQFcc9HN-c8MPHbmI9I5wmTmplRujE333M7zm-UhlJHtUA8Ljf7FqkxQZCIBqAHp4kOhOzdOmwhjlm3_Vz-nHxSBxCJhudoFwckhVkcPuPCsD5xxz550nuUXEZM8mxQx6Dz-VsHGMDoBB8w0N4FYVbTavuzN_vkGj-S82jgba6pc-YFr5ImNP-Bh1MdzidfMWjfniS5jo6Qk25NZNRuP_I62yTGkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران و بلژیک رکورد مصرف اینترنت کشور را شکست
🔹
براساس آمار شرکت ارتباطات زیرساخت، همزمان با برگزاری دیدار ایران و بلژیک در جام جهانی پیک مصرف اینترنت کشور به ۷.۵۶ ترابیت بر ثانیه رسید که نسبت به سقف ۵.۵ ترابیتی هفته‌های گذشته، افزایش ۳۷.۵ درصدی را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443985" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5mM-MfaK5eThETtgrhWDgQM74Ohl0x0UJdKW-M1Pq-ogI3ZE0tTJkZRyPg50M2ke1NIViZW2Hc4qIhKZgEfe2PQE2qZvKyxwflP0lkT5H0BhelxnMlFCvDzZyNUgtWfMq8mEmzu5DM5Wsu8fPnEZbzG1Env98w6731BWyGbw-oN8VcO4L58tenI9u8pKGCaMYD9ZF3tV0ZqGQRjbR2DP1Q-fVBaiM87XzSHOHn743SWAP50f0FQuVRplZUOaUFEqbuBYkpyxH5syxURY0U6ZYEmhYxn4KwVcCbwGHAKEr00EQ9qNgv45OIzgv-Ue_7QVPT1llmy6MRNG7hRIZiWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2AUw2_DZVmPlPlzA_5rEwrJSIX_bHGtLRw36yFmjS3ZFeKdpGOsUaGVC4f6tr6kCMjd_gDS33aN0fJNQZLWyvph8tfNuud9-p_qJQTZZ1i7HBU_JdXharuT-rlC_c6_aVaiFNIuIWJ_pixN3TYZFTHCBywBnhlalN445C0gxTE-GdfeVS62sI1kQMUqAE-0cubbNQHl1RTs5Id9hbBZlSywJbl6GxykQ_GLi_swRqSU9B9Oq2wMn3xOkcCnAkOpIWfxx9rvwGzoS3SZrBpNzOrGghFRJQ0VV0mUmRf7XJWXzc5tjYJi5DRJuiqEdMCwRt0uB_86Q6_KKXcD3Zuy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiqVFK4xUVTBVq66uvyDGGJRypQ4qjR4gjRepiS3-noEDG4dXFlNi_KVsLSqemYBGhkfqmLWbMNSKxZ0q0rd8iJwQzvkI153AFscFFwyjwZCk6dxo9dol1XIGXQJcXjI8hRAIyDJHkj8SqSIbX7E-N_4T5i34Py7NShMu0tSdT7ZTzeyei1aZ4xmg-We1X-fEJaTbUHJq0lJg-0ryR2COk22HSPSFmJIS8g3TMrSKsr6LhocQJoppLV_dxuIxmliLIjQVcyK8v6KWdfdo5KzqBUWmAW5IKpEyvxvzP9HYGHMNh5wgaM1Kvcj108UaiDIyToly2eqZslVW1azjqj3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIi1P4qeEx5ioDAgDz8eMBtGZyE6n4IL0_d2X6y0zu96Fxd9XPNmUY5ldRaiJFyKTZ8LWCpHQ6a0AGU90o_XAPflsE-g6C2MRmMnqBFClLbC726dzr6bXhlsyoWrbLvMZymXKxSiaczTpJesvbySs87PMDNaQ2ipOije0aWdPpyqx_oyDNvk6H-d5LCzi5nuwnpKYIJFuKSR8OD-y9diAi7gO-XO2bsmzytCyf6Ev3k_B2tLLoVS7z848fkopKCRe1D4qOPTNlpdad7B36g2a47iBdvs2ZvXeTP8DEtgmGQPCXMFrZVUmLN9Ittv3LLP67ZkdH6W3K9n_hXicgwlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Is5eGNe8Kuockdtle27xkOHbaQPjcuojsX-zCsShjPjnR965ZYObcw6aRMO4zvVq_3qccZIa8DgjkQdIfDr3UVFOjAToN1vjgP6mgK_THZN9cYf8wibuOKcHry8H8Z1ckwUi5jLaS2eG1D-xGkIbm0TUhIryDTdYQv81_6Caza-0OuCenjtNVTDMRnGW4IJJ8i-vQb7Jclf4TkOtexwTmfbD3kRNXSmAW-0nF7cANL49q08aZ9Vgu-e7pA_Hwn9YJYuOhZiABeBTJrw4-ovZ8QLQeEfJajUH9VhAT8V2_n1r5pNKFzOz_gFUr1nI30wo1pXkR1H1-Y0KrpZ4w9vuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEaSlgwmAV4pKoTZ-zWa3n540ThkhlNEPGRgBg7QcQGVKF0KX4dElhgQCdCyWkoYR0h5Bm7CbXqA-meULIJuuwkbxJgCsmfbKGxCXUdipPVAsa0oBsl9D6yR1YX0H4Pn7CnamQyCnCfJvtvVfFLT43DBWTSe6wIMQw1mvVPSNQFYtVTfLOYqLodNxqd-pSgpOSqg142mGGsexFTPk9HUs8xKa4duhiiQsPuUds89G6pVWktstYwIU3i-crRnKqa7VObTak8aR9J8VEwB-wFWtgUJDoDL78-yMvChtWJbjhg4iwNw3_3-5scXLl8mZOnQhI07cFC5I_cmPnuYycwhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuYsa4PFD59sJIt3gV9heTue-lX5C7iuySiHuK0gRm3yseiq3fCRZuMWUlupEE3xo6g9lQcZP5t838QpQ-vwEhrqp31yMFSiMtxTLwJ8AZvF_ks4fI9o9XyW2muwsTumO-dmKEHyNyH_vtCL23nJnm6v7My-N52aVYFxhA2QoM07GPBc0Lirrxl19s_xSiwHxTYAehcsb3vO23edxJqyeTUbR0Sp0lA9EFABYiEItziTGYfX57bbQcC9Si_Jo1mHVoJImYbBwbdJC0QzErbu8IUGGHU_rWPclLKPXq6zT1Spa_eygQrhO5U59xpAEb7K605S0XCVO13q1891wAYt3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: تشییع پیکر رهبر شهید انقلاب روز چهارشنبه ۱۷ تیر در شهرهای نجف و کربلا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443978" target="_blank">📅 12:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFcaeG4XNQrDHq97QDLT06xNlS4ZOjhs_NDcCdtUBpe86FwF_o9oaxZv8IupNl9mt4fP14tpDxKjT23SgaQS2aAPaHAtOusyaQk7gW8oizsb9NjGAAa7-itsW-7ZBtt5NgEVJl6Al6I_ONvLyWIp7IcDwptQMbzMqbRu-QfzartlCgkYQKMj91gJTfwWFmMS7-MYsSk59wSmqgDn4fXsnQeXDv03wXL_P3eXcS2ezFa_xmf7lEgVVKr-7saj89Rv0JyReurh-u7tos7kBTzvukipUnC6LWHXlGtVG3zvGF1h6UO5LUmQ1tiUAYvYBXRjpHIewCNf6lZCAWPHM-YC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۵۳ هزار واحدی به ۵ میلیون و ۷۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443977" target="_blank">📅 12:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/053f57ed74.mp4?token=kOxDn0YkFltTuQTCEwfBDH0Y7Pf5KgIJ3m95A573LFpvHjA-1qvlBMs32RuNm_nO8mm3xTnsY_iKvxZ8cTvZ3miR-o2y38cP8CoHQ8nmSxocWjxSnU22RLD-MKyWKuXF-8YwvrkeH162PeOmdxCymy7whEl_HzhTv4PbUhmGxYQ9a-2Kl6A7NJU73MzqR8H6OFOWR34LCqMBV0hVar-DEIzBQO9LzlKKyivqqZIVmRTMkcF0MBOm_a_tZUIJeMxaZamqa36EQ1fs3GvfmKT4WBJYx0iZGQXjfL8IjnU60_Vn0v2lx_zFrvWnhipFXazejTRoANYSmdq-RcQlBPNXMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/053f57ed74.mp4?token=kOxDn0YkFltTuQTCEwfBDH0Y7Pf5KgIJ3m95A573LFpvHjA-1qvlBMs32RuNm_nO8mm3xTnsY_iKvxZ8cTvZ3miR-o2y38cP8CoHQ8nmSxocWjxSnU22RLD-MKyWKuXF-8YwvrkeH162PeOmdxCymy7whEl_HzhTv4PbUhmGxYQ9a-2Kl6A7NJU73MzqR8H6OFOWR34LCqMBV0hVar-DEIzBQO9LzlKKyivqqZIVmRTMkcF0MBOm_a_tZUIJeMxaZamqa36EQ1fs3GvfmKT4WBJYx0iZGQXjfL8IjnU60_Vn0v2lx_zFrvWnhipFXazejTRoANYSmdq-RcQlBPNXMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
پاروزنی نروژی‌ها در میدان تایمز نیویورک
@Sportfars</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/443976" target="_blank">📅 12:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHFUD3kEcPogOZ7xNsuwIzHCUYgHSrZQDKnIoSyJlEa-6LbqDqFBxz1DV8zpAAR_rl1MaBKcAcl51xVV_Hy_kFfSFcSnYBZPH1WpqtT5CJTw_t9B2TYI96paFVFBIEQ5PAf4y_-QfgUokGZJmXhzQpi8QtMSYQE6tTknkY_sBhVAFFposUH92hP7n9St4ZhOF8sDJWj3tLdQu2Qaqb9rqHH2Z-F0RKB9b9hmEL2Gqmpi0npAU3Y713ePN_hp6a_sZElsAdmYWG2LfrPLwqt9zQuIBbbD27jyKOk091AzI_1MpmuOAdzu2Ji1KtoB47NHJRoUFFeG9edqfwB-oTvt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک تُن انواع مواد مخدر در يزد
🔹
فرمانده انتظامی یزد: ماموران پلیس در ۴ روز،‌ درپی توقیف ۱۰ خودروی مربوط به قاچاقچیان، يک تُن انواع مواد مخدر کشف و ۱۴ قاچاقچی نیز دستگیر کردند.
عکس: مصطفی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/443975" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">استانداری هرمزگان: صدای انفجارهای بندرعباس ناشی از خنثی‌سازی مهمات جنگی است
🔹
حوالی ساعت ۱۲ ظهر امروز صدای ۴ انفجار شدید در شهر بندرعباس به گوش رسید. معاون امنیتی استانداری هرمزگان در این‌باره اعلام کرد: صداهای شنیده‌شده در بندرعباس به‌دلیل انفجار کنترل‌شدۀ پرتابه‌ها و مهمات عمل‌نکرده و باقی‌مانده از حملات آمریکا و رژیم صهیونیستی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443974" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ تکلیف افزایش حقوق بازنشستگان مشخص شد
🔹
درحالی که طی هفته‌های گذشته میلیون‌ها بازنشسته در انتظار مشخص شدن وضعیت حقوق سال ۱۴۰۵ و صدور احکام جدید بودند، تأمین اجتماعی سرانجام اعلام کرد احکام جدید بازنشستگان و مستمری‌بگیران صادر شده و از عصر امروز قابل دریافت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443973" target="_blank">📅 12:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilVUaYxtZQQ2BfO1hy1f-1_PUHnB1mEkhlscOLjn0GEMEIhcQOgUaIQctJ7y8E9ukWvecBEo-S9D-duPpRpn1wnjP4uH_Mjmg9_peuz6AhSbPcU2-x0IoqbTRTNJPv1s8ikqHSJx0NUECOyRs6WmdVskrHuCaHpW0csX3TUKsip95BIn4YWX_wPPwpivBFaqguMP6hyb0WggATR0MacHL3GtnIOl8p1L7k4eLtGFCsBgTLIFz9olX9FNviDfLM3cQoXG1s_hkXVjo1k3MZShdCglXGGzT-3jXv_ut7TvnhUBYYTHr0fNNPqF5bUsmxMX1IeJCx65w4lIn245lIh1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع انگلیسی: نخست‌وزیر به ته‌خط رسیده و استعفا می‌دهد
🔹
روزنامۀ آبزرور در گزارشی مدعی شده  که کی‌یر استارمر، نخست‌وزیر انگلیس احتمالاً روز دوشنبۀ آینده استعفای خود را اعلام کرده و همزمان برنامه‌ای برای انتقال آرام قدرت ارائه خواهد کرد.
🔹
استارمر که در ژوئیه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443971" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXKPG8C86JNrSDtA8RbNRoMztsrmvSLm9txSdJ2kATeUQRUORLYSuA8yDlDCjossqTl8O60c2WZl4JL5te2KdiibT0x0q909IndjyaBAkVZVAxtw0e9zANOVMruAVG8IsF7pzrz_-GEEbjzo0Z2u9SF59qmFa7pGavTfQXalSaQCn42gq77tmUiIUElvJiSA6e85JmGn6oqwLyweamkTouF8a0uA5-KOgeZL5Syq0Q8HVqEWZo4TKG1bmkQuVq1wLgywuGKP7EuqQxB8JgdgQI3GdA5acTmeA6vJkxbxx0y48tXi6uqMxJhEu954xjcRFhkzI5dj8WUgnSaH6HN3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی: در روزهای آتی بخشی از فشار تورم کالاها کاسته خواهد شد
🔹
برنامه‌های جدی برای کنترل نقدینگی و مهار تورم و نیز تأمین ارز مواد اولیه و واسطه‌ای واحدهای تولیدی داریم.
🔹
بخشی از افزایش تورم کالایی به محدودیت‌های وارداتی ناشی از جنگ باز می‌گردد که در روزهای آتی از این فشار تورمی کاسته خواهد شد.
🔹
با پیشرفت مذاکرات، انتظار داریم درآمدهای ارزی دولت افزایش و قدرت تأمین ارز بانک مرکزی از محل منابع مسدودی، افزایش داشته باشد.
🔹
با برقراری آرامش در منطقه و پیش‌بینی‌ای که از درآمدهای دولت و منابع بانک مرکزی وجود دارد، انتظارات تورمی کاهش پیدا خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443970" target="_blank">📅 12:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
هیئت مذاکره‌کننده ایران، سوئیس را به مقصد تهران ترک کرد
🔹
هیئت مذاکره کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی امروز سوئیس را به مقصد ایران ترک کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443969" target="_blank">📅 11:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw--DSK3Ac8rosMaDu6YjKjDdyZdefyIjDkn5ZR3d47svEsM7jkbJiFxWIJHh2lR6pw_3-QDhvjSBXB85bfRwQkIhpxVYA2-HiToIll96IQ6zBBWmLeNDW6SbS4fuW5QLzqUpNz-7XiIL03kRWlwV5nb_BZmYdMAlOBdJ2S54sgFSgl7tEogOu5pQ45Y32lWM-4LWrMDjHauUPYjv8GGm04Z8mHk47C-sTWiqJe78fL64hTBJCkNulVM2I5gOVOWpJVpBoh0ElUoAzsgA0_OGPXSxP1lDrm5MSnYKxaTGhWOA4tKTpnisqzgrKky7bEMvD0nzL344xCIB37diC_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات ۳۶ میلیون بشکهٔ نفت ایران در یک هفته
🔹
تانکرترکرز: ایران در یک هفتهٔ گذشته، ۳۶ میلیون بشکهٔ نفت خام صادر کرده است؛ تقریبا به همین میزان نفت نیز همچنان در آب‌های اطراف ایران و روی نفتکش‌ها درحال حمل یا ذخیره‌سازی شناور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443968" target="_blank">📅 11:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My3AWFr2uExTtB0Kb94e9ZJmJzs6WEEWIH0DI9XydYiDSgpBrE-fQJMYOa7tWd5iBPhadD23irN71w2ondJtYmVr1zEFnnMStKERqnRF4x-H3xXOjysGFtKXosxrQgbpD5u0cL2eM0cLKCbxmNsvSNOGN3Mijg0gFVLIl-JxNqKpKRltXRq_Oejz1txswT9UoZewNft2tJ3ct0J0Np68aznLRgm8Pi49Bkk8DOZYrNndGirrbMX8GC8U1Wht7gt7vbQacOK3Vtq6Tqy5rETsaIzRBQc_ZGoDE6MI0yC9JGxw-7UuoOm6dCKSvmBOSJQ45QstjuSmUFCiZzCWn2TcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفحص پیکر ۱۳ شهید در جنوب لبنان
🔹
سازمان امدادونجات لبنان خبر داد که پیکر ۱۳ شهید در منطقهٔ النبطیه و مرجعیون را از زیر آوار بیرون کشیده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443967" target="_blank">📅 11:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy6A6FLAL5fCB9up6Pn5VewCxKGgBxK-T1Uj6nRCwj_KFhrqKWhlQVo5ZdOZZcqhXBneRx_wqk-G5kR_Am66TaHQjnxYuVNKwQ9SfCkC1pi2mU3OLmKMm9u3N77qF6Tx0vmH5xWtCScvfEFO9illUF8fni64nsV7btLSYED0-IbqM_zKXspojneCF9fBVLJs9x1a0mXy17ZKXaut_Kh9YEk7Kv8UDb-lcSJe4dBwtGo69xDQ1LBpRpqegPjn5gmIGmy-oLE0arhZjv_Uq7roKUoHPVbJWGk4pYYx0xobibNHTyixxta_RA0S2ehWljyRqeZCB3nyXDQNV0j80XWc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول گروه G جام جهانی پس از تساوی ایران و بلژیک  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443966" target="_blank">📅 11:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXg8RIPlg7VF-zuvpFnvaE0NnSHNi-9Qk8Pv9FgfjPEWpUBKLm44KxDInk9Uwy6HgMgi3plERdPnLNwWn1A26C5S7LDlcTzBtcxozbg37OblxjiLpKYxs7BH8nWagOfsoWT9L1PHMxZd51wkmALcxwZ0hCudSs-5s-b0d1HGtMQUEtrAk-rNj9a9H8GHbl_siRfpEyIcWGj8Pt7PSa3wBYyvG3CtJeRlyFyZeeh-Y0PmzdLI4PHHWS3qhruZGDL-BljCKhXgBZCQ8taVMz8EHUSmE0pEb6nme196ETvpal8HFIoNSbyFikQYb-19HvIbfKYr3FHxuLtfPg9ScTINcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRElNdzPbiphMIREgL01y3qyJpg5phZOu-A05yb_sDTrXQM9qfyX9VelhRG4gbLIOFb7oBk5_UWems14Et1IkW1j0qFoB2_2KrnZzH67IbJ0m-1QnLqpce5tqzvFTSIdmD5MV4Mphf7gPeWCDhJMaoLIU8pQr6yWOZ9h9xVonjtuggFbMrq8gH3N0BMWGaG3wRzOOWEmSHdD88UVULp2lyYdPLVCrSHuDiPYIM7az8zPiflDvhNXUZ2QOJsuF0Ron7IXhpTNTZpu2ri3Pyld_rEp7G3sAFrWKmdl-84jCmuBD5mYJA7xwh63eP9Qpu_NaH9CMvus8ylp2BHHY8_WTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL06eFHvmWCLeHgtTFQaxRNIA6tHHP6Q1aYMlm3gm8XOulu3AsUWDyCCTw_u_20QJK--0eR04EpVdUJlDwtOKh-NuVgmqr0Nash6SqfpzlKl0mNW4dAInW0lPhk03sffehIAk_2e0APAugW_mXs2pBW1hgPERAtj4NoLXzPXbA9SnrC9N20SToVuBUxa2J0rHBiBNW40pJZl03wdE5Zl_53qPENpc5z0i0zNPh5DJ5XLH9LTPOJa2uXdehLXb_MBTfLq3-KWtxYzAoyPMhBnjd_5VarQF9QYPv5kIGb4e1esGlWa9heVz6pCixFxdZNmP85HFkt4vzx1SthIYzpvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bufq2p1_fio54VLljGiPKNJZuAfW4yvnLu-i1IM_dxYzh1TmPSRGJTLSpMKQSIf-VhQoEKRTvKEWHc9b2bsFaVQJ7d_VtzLxFXSHcfXg4wErzVLoAHzcofUQbjbOBuEnroF59PHnEhPOgOr9M2FEyNbyZbJhIANwETdmrvowXXVutH3OIZGiju5H-hmI-2nDhrHwC85zL4JPl5L2LdV53Uu_Kd9afifa3WNocO8tKA-lYr3uDYVuEmb8dpnWTCBnW4n5Q7AHrPzgp7jWqS_pal-bqAlR8Nf58qkg8uh8l-oq2XQ4qe93OXlZHGzPMsyI8OJ0LvKwhnPYJPirm1jALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttS_k2fh-7CeCvSaWZTBqEMTdeSeSKiwKcELZkBQU1EwGBWxoNts7R5FdwMjEfhJqXJ7kmWO-MC9Hjb95AMhmscf6V1J7rlEl91wlh5Q0C37abx0Gf7UcfGC3FgOVfoXklrOvGIpNQiA2BixwwseRxggxnVzkLzPkl6tBX6kYdts-nh0mZgd0e6XCJQDcrwFpfLFnMm42XdZD16HWsn-LZAIRkR78Hsh7c2XPx4bsxnRLfvHNZ5CtvazscOAfTABWz60ZRLapu1tSYSAjYeHrjtXCVV6vRMbXNJDR3bZJedezzUDSl_QKCcXg0p7LOPU1EvDBB5rS_w66ssUjIrmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvqDTUYlVucBgYQADlEgPUtUdwzqmIPqCzc3D3dRKfBpqQjuI8M3-_6LYM6oyUPRTPjYoTQiP8K6HUekjqhMQXws2h5btnBWZHtuPElKf3n2Wva4eOerFSYaxkIXropZYe8Bhfxr3xRsvyW9dkopNF37zwFZHKVdMuJ2--9aoo2lfMti6DnMV3su9SuZ9V2sfTR_D8AttPaaEtVHO8X-uXozlMy40b7SRYQjSRWBP8gmXh5vL2ywNvhq6ZGeyvhNkYr08frtbPEP5GcACkexI1iRjUiI2d5onpeFKx4nzRFr04hJ4QKUbRKcqe9BhAG0IoP5qySt64lF_0dmwYhTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA2b4Drd_cPy3px1TgqIJ2QRSQZ4ZY288mSgQTJuPVcAkRZQJCrJA8X8FoOEmDEofgUsusPWQYKZhSGoqqjK2LJDaQNWzSUVnvlclcycVGW6IlpH_oIR3k6RiWdNaRGYKHPelI267NantwIPhDPgWrgp23ugvmFLyFL-a0Is8S5ZVkQ7OTU-Tx7IKvTPK_mCMeZQFEAnbJRYpdOLndlAEUtNTmNA_iyAW1MuET24XJW-JA-WV03hbzLGdf40haE2o9n8YQ4VGTA5XP82e91HzASmyRJq-yGLn_bGuCOSxCDZdE8hYYVcFLEiIoJ87ukpSe9W9GELTE9Xf_pomGhY1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌های محرم در بجنورد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443959" target="_blank">📅 11:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443957">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr2jb8ayEuV3ZZR8PHHtpZYKmtvnQJoveHPeQZ2EzH0ERl1IoOX8kR2_C7QHcSHOmK-kPIRGtOvftDD9j3ODtqAtBBsiLoIpqVMk-pcBrGQgJaChhPAWu3afdfy6CPnv1HFJGyTNjkaJbC3TebvhtnXcvskEs49hPMGcqYl6OqDIoaTb7cOi1E2HwS6k9lC55Ky6xEZdTi-bdC5T2spuziU9E7D3LedenEEMbAH3RiuWdfH0MDUAQDKaKtCRHitL4hOycmfs01gY6ko4O0tCzhg8D0GL1lMkMaaelJOAGfJaOZGoKmlaqaNdUfREY7hfX8yM4ZGj9l_Htshzcn5Daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هیئت مذاکره‌کننده ایران، سوئیس را به مقصد تهران ترک کرد
🔹
هیئت مذاکره کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی امروز سوئیس را به مقصد ایران ترک کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443957" target="_blank">📅 10:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443956">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b86576d.mp4?token=WwLbnS5twC5mGsvqbywPCW0Xh6b8UTx7RFKBd-9xjQaulVV9T2Lv_xyaga5Ou1wLL5Mf_dsWmsOjPij-0V6ZgnX4qcPLPIJT9Iegb6wJy5NTOiz6pE4OixeEO1OUyKkKc73FnF_zeSDvHJmbwumtcSFqnlEeU3N8EMEg4gPjzgNIAloHJFHhVl69DH206N8IsU8NxMlSHdxljnyQAd9OA-Ecdq7HFAyQ-LwTdGd0hTbyK4hTcYlDjTKwagTAIyVc-FJMYbcsF41f_JGVYiV7pnbfznAuCB2A7HyJfyaoGmdzpWlWrOosecwOwYJnJp56Bg2MkW2wYMZJ7lYEcYBxXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b86576d.mp4?token=WwLbnS5twC5mGsvqbywPCW0Xh6b8UTx7RFKBd-9xjQaulVV9T2Lv_xyaga5Ou1wLL5Mf_dsWmsOjPij-0V6ZgnX4qcPLPIJT9Iegb6wJy5NTOiz6pE4OixeEO1OUyKkKc73FnF_zeSDvHJmbwumtcSFqnlEeU3N8EMEg4gPjzgNIAloHJFHhVl69DH206N8IsU8NxMlSHdxljnyQAd9OA-Ecdq7HFAyQ-LwTdGd0hTbyK4hTcYlDjTKwagTAIyVc-FJMYbcsF41f_JGVYiV7pnbfznAuCB2A7HyJfyaoGmdzpWlWrOosecwOwYJnJp56Bg2MkW2wYMZJ7lYEcYBxXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: مراسم تشییع پیکر مطهر رهبر شهید دوشنبه ۱۵ تیر در تهران برگزار می‌گردد
🔹
در این مراسم، پیکر شهیدان دکتر مصباح‌الهدی باقری، سیده بشرا حسینی خامنه‌ای، زهرا حدادعادل و زهرا محمدی گلپایگانی نیز همراه با پیکر رهبر شهید…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443956" target="_blank">📅 10:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443955">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: تشییع پیکر رهبر شهید انقلاب روز چهارشنبه ۱۷ تیر در شهرهای نجف و کربلا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443955" target="_blank">📅 10:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443954">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1GNXQ2TZWT-9sa3wQgYX0T8Qy0hXDG1-u0NTmRjmqyxLnOBn1TKsUqHWZcKPt5_LoZM5qNM-kG3SNxdNsgMo5KsCvmssB7rysWD327tywUoRkEa-iDwt_Wx6ad4vOmzAp0tdZ3oEyX1ODHLkbcldbshVRMjuv1tTAtnHqt4ajrgzaVYnoL0SaWAm32p32sKjxHPZ3EhvRkQ5McDH_YbqPHWnPW6xcuzev13n9IbBoIaTDaq1DGICECCJwFd3CUPFJQIGtWhNl6NjdcIHZ8Y-q1qkptV6uiq446TzdVnpwk5a7gOiuJvIYok-H4U8IE_Q3VJiAPfS9iYEsUJSIrVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صاحب عدد در ایران فوت شد
🔹
۶۹۷ سال پیش در چنین روزی، ریاضی‌دانی در کاشان از دنیا رفت که عدد پی را تا ۱۶ رقم اعشار محاسبه کرد و تا ۱۸۰ سال، هیچ‌کس به گرد پای او نرسید.
🔹
غیاث‌الدین جمشید کاشانی که در حدود سال ۱۳۸۰ میلادی (۷۵۸ خورشیدی) در شهر کاشان چشم به جهان گشود، در غرب به «الکاشی» (al-Kashi) مشهور است و از او به‌عنوان واپسین ریاضی‌دان بزرگ دورۀ اسلامی یاد می‌شود.
🔹
شهرت جهانی کاشانی مدیون محاسبۀ دقیق عدد پی (π) است. او در سال ۱۴۲۴ میلادی، در رساله‌ٔ محیطیۀ خود، عدد ۲π را تا ۹ رقم در مبنای ۶۰ (شصتگانی) محاسبه کرد و آن را به ۱۶ رقم اعشار تبدیل نمود:
۲π = ۶٫۲۸۳۱۸۵۳۰۷۱۷۹۵۸۶۵
🔹
این عدد آن‌قدر دقیق بود که تا ۱۸۰ سال بعد، هیچ ریاضی‌دانی در جهان نتوانست آن را با دقت بیشتری محاسبه کند.
🔹
کاشانی فقط به عدد پی محدود نمی‌شود. او را باید مخترع روش‌های امروزی انجام ۴ عمل اصلی حساب (به‌ویژه ضرب و تقسیم) دانست.
🔹
همچنین او اولین کسی بود که کسرهای اعشاری را به‌جای کسرهای شصتگانی رواج داد؛ نقشی که یک قرن و نیم پیش از اروپایی‌ها انجام شد. برخی منابع او را مخترع نخستین ماشین‌حساب آنالوگ نیز می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443954" target="_blank">📅 09:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443953">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🖼
جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443953" target="_blank">📅 09:54 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
