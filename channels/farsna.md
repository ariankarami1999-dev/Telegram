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
<img src="https://cdn4.telesco.pe/file/P1B9SJAAZxVwbOAq3Hb5KNL-aJBwx1esg_xSw8cjnLOCJcjtAo76HMA6oiEh5aX6wVNHMHf7K57fXaZI6MBDOe-4bQHo2p7V-3zBBtbUtoZm67NoJjetmb9iNGW6ZlLsK2o2EQCgjZNxcQzkHl1jkGGtmGW3g2jMbiiNzUKFaeX-rdtUui6fA0TH8RVKXMq3_-a7O0xa6eBmJQGagIcoxj1997Uny7saeneMya3-3H9CMe7pfZkpaYXqboJMDRAjBKPa2cFJOvJKz_3VQ2yWr9icVBWKdjs3YrEXgxSJdGwuM4D1UoslxmqEVRY8dOAKZhs42rmFCmbas3F-Us6reA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-465869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c247275233.mp4?token=R0e_9glt3e4_TSTLtYXcGTXO4usHqcB0p3fTP9O7xi_mX4lhNKA14AZeW-MyTnx1rjI2pz3A223y98KGVspTk1TqaTbz9LClMY6BoA4RGPWF0_SCAKawUeqeGU4W6wfye_L3AFB6m4jjPYocHc79y0FnZh2sjyeWBSYsRVy3L3j-pAAkHW1qF0widjsw03mgGB1HGkpHT7ctJVuQGs2ULQLVFxn05i_MfSPueoLJz6IunMNqZMs0NRSXuc-2LVj6JB6DU-3xSVWrlW9SXgAGSJMbp0fPxXS-bAI_p06_HwY7C3O_begPPISzRbjfCP1Yz7goVRjzLcG8YwmVAFQkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c247275233.mp4?token=R0e_9glt3e4_TSTLtYXcGTXO4usHqcB0p3fTP9O7xi_mX4lhNKA14AZeW-MyTnx1rjI2pz3A223y98KGVspTk1TqaTbz9LClMY6BoA4RGPWF0_SCAKawUeqeGU4W6wfye_L3AFB6m4jjPYocHc79y0FnZh2sjyeWBSYsRVy3L3j-pAAkHW1qF0widjsw03mgGB1HGkpHT7ctJVuQGs2ULQLVFxn05i_MfSPueoLJz6IunMNqZMs0NRSXuc-2LVj6JB6DU-3xSVWrlW9SXgAGSJMbp0fPxXS-bAI_p06_HwY7C3O_begPPISzRbjfCP1Yz7goVRjzLcG8YwmVAFQkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واژگونی یک دستگاه کمپرسور در محدودهٔ سد نرگسی کازرون
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/farsna/465869" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
حواشی بازگشت بیژن مرتضوی و فاطمه معتمد آریا و خالی‌بازی سکوهای طلا
🔹
در قسمت چهارم «پشت صحنه» گپ‌وگفتی داشتیم درباره بازگشت بیژن مرتضوی و فاطمه معتمد آریا، خالی‌فروشی سکوهای طلا، باخت فوتبال ایران مقابل کره‌شمالی، لغو پروازها و تیک‌وتاک الزیدی با آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/465868" target="_blank">📅 18:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متلاشی شدن یک تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: با اشراف اطلاعاتی دقیق، یک تیم تروریستی که در ارتفاعات غرب شهرستان راسک مخفی شده بود توسط پاسداران گمنام امام زمان (عج) شناسایی و طی یک عملیات غافلگیرانه مورد ضربه قرار گرفت.
🔹
درنتیجهٔ این عملیات، ۲ تن از تروریست ها به هلاکت رسیدند و تعداد دیگری تحت تعقیب قرار گرفتند.
🔹
تیم یاد شده اقدامات تروریستی متعددی را در کارنامهٔ خود داشته از جمله در اقدام تروریستی اخیر خود، عبدالرئوف اسحاقی پاسدار بلوچ اهل سنت را به شهادت رسانده و همچنین به ایست و بازرسی شهرستان راسک حمله کرده بودند.
🔹
این تیم تکفیری تروریستی همچنین برای ترور عزیزان بومی حافظ امنیت استان طی روزهای آتی برنامه‌ریزی نموده بود.
🔹
لازم به یادآوری است از مخفیگاه این تیم تروریستی یک دستگاه استارلینک و مقادیری سلاح و تجهیزات تروریستی کشف گردید.
🔹
قرارگاه قدس نیروی زمینی سپاه اعلام می‌دارد خدشه در امنیت مردم عزیز استان سیستان‌وبلوچستان خط قرمز بوده و تیم‌های تروریستی تحت اشراف اطلاعاتی قرار داشته و در زمان مناسب به سراغ آن‌ها خواهد رفت و از هیچ تلاشی برای انتقام خون عزیزانمان دریغ نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/465867" target="_blank">📅 18:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599fd9e125.mp4?token=l51kfUL8r2iSp0yFlxN4W0A7W44OPENwa8zGKpin5-PAkpG8rPnENv5eZUYeIPm9XZw0UQi5cNKC5zvqmKKPToHhWy_goIBY_vI5JxIOK7-lU8lcMrRJYB673nHOU4ZXlwXsrBAs4sWuYIuUltBu94--kegD0nULUrnUyy-rrwevP36lhxPsuZanAn7s_EXh6pQ7BiFVaaTeSFocWzE_H69GNNHDVvRufUAeM3hLyI3DUqzLrEwel9U9diOUuQVh1knudLnKyVAePRsvUrZovnWJ3U7Yxm8cFWq9ZSzEvHrDr54CB3iOMIh-nwxvXzo1sa0GE7FNRXkYSUJJFCGsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599fd9e125.mp4?token=l51kfUL8r2iSp0yFlxN4W0A7W44OPENwa8zGKpin5-PAkpG8rPnENv5eZUYeIPm9XZw0UQi5cNKC5zvqmKKPToHhWy_goIBY_vI5JxIOK7-lU8lcMrRJYB673nHOU4ZXlwXsrBAs4sWuYIuUltBu94--kegD0nULUrnUyy-rrwevP36lhxPsuZanAn7s_EXh6pQ7BiFVaaTeSFocWzE_H69GNNHDVvRufUAeM3hLyI3DUqzLrEwel9U9diOUuQVh1knudLnKyVAePRsvUrZovnWJ3U7Yxm8cFWq9ZSzEvHrDr54CB3iOMIh-nwxvXzo1sa0GE7FNRXkYSUJJFCGsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راحله امینیان در ضاحیه بیروت: هرجا رفتیم، اولین پیام خانواده‌های حزب‌الله سرشار از محبت به مردم ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/465866" target="_blank">📅 18:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PARAyUXq9FFTTEBjdwBGUc4g-bLdc-rEMlTVVe268G9x9dgab80hKJvws0Qt4v5G1pUWjnM0XwjS8UScYJufaexB6Fahr_ZrWAQy-VO3kPH0szPwZDIhicXVk8giwe8eEmYYVdk4zaHzXqT4iCnPsRew_MEiOURTqoy7JnP-IzVa_JeQXvSxLors0alDeAPRWRDBlrN8f1Udl6hp4bLxP5aqG3DD1ljeT2PNikdS5_MRiFtpHFnnbH5c4x71YVr-ykd5hXkj3s-mXdo1lDU4ew-mdWG83DOOB3OkEjSpmkrEXhI_Zl_lEbW0QmK7ha7gRRm9STPV9xPP5Hx_IIy2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ سلاح جنگی در کرمان
🔹
فرماندهٔ انتظامی کرمان:  تکاوران پلیس با استقرار هدفمند در ایستگاه بازرسی پنگ، خودروی سواری پژو ۴۰۵ حامل سلاح را شناسایی و طی یک عملیات ضربتی متوقف کردند.
🔹
در بازرسی از این خودرو، ۳۴ قبضهٔ کلت کمری به همراه ۶۸ تیغه خشاب مربوطه کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/465865" target="_blank">📅 18:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1yxLjhbWCtHMP-4YW7uA15pnlJ3VPu0TcUxiFvbdtOVRQfZ2Za7czVcJzo_GuuDUP3IxhgbrBt6f08p1Ov0O_kNLtxsOxBT0xBzKx4xin7MCiOXk6TFjgJXSK_f4o7m7KOnY1qcKXQJF2BOLEXSEKxAvSe2KR-JqYbFQGTGh9XpsLcpTRA5iIIYCrW7eNsbzYBjEb0pEI-N_KZWjK2jO2H5QOopg8M5S9dwXU55aFAVhcdXQpBiX-dQJNqSVZM0MXLiUd8tmgB0EBvtA2-40N3tt5HNdtBoImNNN_NgI-7y8HDg15eAy8RTgD9ylqKsCi9owxY1GRuX59rGyfdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از سرلشکر شهید محمّد شیرازی، رئیس دفتر نظامی فرمانده کل قوا در کنار حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/465864" target="_blank">📅 18:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2d934eb4.mp4?token=oLKtSap61fLawYbMePh6YyNFbxy-iidDgae1fBsRn0BTYciRLnaqkDoUOMm_VrFax-wi3_aKAfJm87rWrsC-Da70cA4T1RBnVgJZo6X1qXlwt4sNRS4dPjmxN5rJFHxINjjDWo8frsDRBpLlI7rUe9UI646lFpG_-FLfpDcQHYPVafcluaja43mdvWX8IvwcRqstOBL2JFwwZxzed2Z2PifQM15XL29fJ8n5NgKQcBqic0KoCTlAhrTWmZp-_YlIlVZ_vKCsfRpCjMlGj67eB20e9bRtq-yzgC4thRXmZ2m7420jI9XDViKvnsk9cW_TrgnmE0QiRoZf3yp9uPIrlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2d934eb4.mp4?token=oLKtSap61fLawYbMePh6YyNFbxy-iidDgae1fBsRn0BTYciRLnaqkDoUOMm_VrFax-wi3_aKAfJm87rWrsC-Da70cA4T1RBnVgJZo6X1qXlwt4sNRS4dPjmxN5rJFHxINjjDWo8frsDRBpLlI7rUe9UI646lFpG_-FLfpDcQHYPVafcluaja43mdvWX8IvwcRqstOBL2JFwwZxzed2Z2PifQM15XL29fJ8n5NgKQcBqic0KoCTlAhrTWmZp-_YlIlVZ_vKCsfRpCjMlGj67eB20e9bRtq-yzgC4thRXmZ2m7420jI9XDViKvnsk9cW_TrgnmE0QiRoZf3yp9uPIrlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یامین‌پور از دیدار با خانواده شهید هشام عبدالله؛ می
‌
روم انتقام خون آقا را بگیرم
وحید یامین‌پور نوشت:
🔹
شهید هشام عبدالله، گفته بود زندگی بعد از آقا را دوست ندارد، در وصیتنامه نوشته بود: یاصاحب‌الزمان میدانی از رفتن سیدعلی سینه‌ام چقدر تنگ است و چه اشتیاقی دارم برای پیوستن به او. نوشته میروم انتقام خون آقا را بگیرم.
🔹
هشام اسم جهادی «قنبر سید علی» را برای خودش انتخاب کرده بود. ۱۰ روز بعد از شهادت آقا، هشام شهید شد و ۱۰ روز بدن ارباًاربای او روی زمین باقی ماند.
🔹
پدرش از همان اول اشک می‌ریخت. می‌گفت ما همه در همین خط شهادتیم ولی هشام زرنگتر بود.
🔹
گفت روز قبل از شهادت هشام، خبر شهادت برادرم را دادند. چند روز بعد خبر شهادت دامادم را. دیگر توان نگاه کردن به چشم‌هایش را نداشتم. حاج سعید روضه علی‌اکبر(ع) خواند. وقتی گفت «علی الدنیا بعدک العفا» انگار حرف دل پدرش را زده بود؛ حرفی برای گفتن باقی نمانده بود...
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/465863" target="_blank">📅 17:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu1qpTAMwNNGE8lb2kOLAw8yW8kybpL6CaWwfwVLxxTQ0dS8_CijJkeOB2z3kzO5l84eQdweZ2MfY0j7u0hWPN8KvRKJle-VY8qGuqUjtKh9GWqp4gX2Yw_dQIoEO8E_It8wHAe876tV0Ep4vzuCxH18YP8s-Ut2cIE9jktikoo4Do3rZYri7g_Ds5fxnxK0PL5jZltAEBggNxJWwkD1OekTpC8w__1BgmLGeMxXCVrulQbvxLVTrzCso6X9gVxnbqOKK2NhOgnY2MCs4cLjnlGKrLhreL0x3P5cfbejE3tM1UDeKhvFFRbqSlNElPXNdUCDrPVHsm-0psaq95r3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای کاهش قیمت گازوئیل دست به دامن اروپا شد
🔹
دولت ترامپ از آلمان و فرانسه خواسته برای کمک به کاهش قیمت‌های فزاینده سوخت در بازار جهانی، بخشی از ذخایر استراتژیک گازوئیل خود را آزاد کنند.
🔹
دولت ترامپ تهدید کرده در غیر این صورت، احتمال اعمال ممنوعیت صادرات…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/465862" target="_blank">📅 17:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3v0FatsvtlHIHFCWBn-Bndh8d1SBugoyO7MBXeuiXVsVo8YbPWRgOi_kqol_wzC_67I_4dmwXRq7B9p1XALPYai6MvymvDNAF1t03CnvCIPp9Kk0wcWOkfh6PArnRIlLw9Q0td8ho2DbU5Hi2WZZNwYua5IaRJub72CwWAcVt2rqQNrJ_kZXxsuayuC34VINmR6OhkQjWrc3ygy4MV55ohpXVoq_1QOg4eqhhA2zUfu-2MvCcvgXTBoyU2bpem6s2u0798itKnuSogdC5c1Bwde2hIVCii4I-Wz0wSUI18O9jJX9VqIJtwmxrW_vaxq_LVikbRgPs7JO2yC4sxrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ترامپ: ایران آمادهٔ تسلیم شدن است
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد: ایران آمادهٔ تسلیم شدن است؛ ما الان می‌توانیم به راحتی پیروز شویم.
🔹
من معتقدم بلافاصله پس از انتخابات پیروز خواهیم شد، اما شاید حتی پیش از انتخابات. @Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/465861" target="_blank">📅 17:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UemRI4LfinBOgLcQJsV0hnG6wXtNUbZHwgkTnyKufpjF3IgXJxh69kfpt3rVpay9sh7qWGHb2hFy3-qBOVG96V5b4PKNfvfSknLDn6qFosjzm_N6pauld1iI-PvY4aKq7h9fdqHwhEWTyi5uDjGgtr4qIvZalsafcG4hlDI8UuiJ_hfEfPvBvCPLRJTfBCkX2p0rgIryzQr7k5sIqYNBJfsrpJEnWyqTq2IL6rldzHMpMwacvlB2I71nxfsgPBomvzHBO_iqJvZ1Z2XWUqVCDdfl1jy_nVhajdPXuVb7LByohv4MHDBkFinQ9WkTfb2DTlIAXyY1wGS50BZXcvIuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بوسۀ دختر طلایی تکواندو بر پرچم ایران
🔹
دور افتخار ساغر مرادی با پرچم مقدس کشورمان پس‌از کسب مدال طلای بازی‌های آسیایی. @Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/465860" target="_blank">📅 17:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XieAjr2WSLasn7S5akgqDbgt3PRbxBjo7-30mvDdK4NyDp-_MpEmhllRgR0-Uffey3SjauzESPUZ3RbaSZxGuEdEzXjK5EKIRgKj5OkMOI8cuDorxbfbJJ8t1TOb5i15X8wtHdiAxhEBf93MUb6keLyptA_vFa89FRIVd9rwGqaCAgd73XKPmG4n9xQBDLWTZLUa6YcECIDLBYZwtX7AFvMyjAZLfTaibeGsAFkNderghGD9hq2t5DfmHRLR2x8H5-phmA_r1ym-RqHg4CXmQJgccxHIFn-oR9ypEovk7wDGd3TwleKv1DK4pFLJsDvhUI6t6cnMvylthrHylVQ-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این محصولات آرایشی و بهداشتی را نخرید
🔹
سازمان غذا و دارو با اعلام فهرستی از محصولات آرایشی و بهداشتی از شهروندان خواست از خرید و مصرف این فرآورده‌ها خودداری کنند.
شامپو:
🔸
Loreal
🔸
Moluoge Oil
🔸
SUKIN
🔸
DISAAR
ماسک و کرم مو:
🔸
Pantene
🔸
Moluoge Oil
🔸
ECHOSLINE (Ki-Power Veg Mask)
🔸
RESTOREX (Hair Mask)
روغن و سرم مو:
🔸
Pantene
🔸
Loreal
🔸
ARMAME (Keratin Argan Serum)
🔸
ENZO (Hair Serum)
🔸
LOSSOFF (Magic Complex)
روغن و سرم ماساژ سر:
🔸
Max Lady (بادام، شترمرغ، جینسینگ)
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/465859" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwmrJsS3dM7deCJCaXMBdkwZ5PF_Nwk3NvWsaJnG5aCQjO69bJNIpQ7JELt2rkT7zxEKDVIqbQ7wOlIjkNjhWjxXNWezyd3iZrBM3tE6HFd00M3n2L5PyA8vau6veXHj8BICvfQWUab7tb3ikEU2RbknDHa5QnwQrvU06MaTaHlXsXhPDGFnlAKfPcrZqpoYx2T9__Lx9rViZ6-6AhqAS-0pwX-RnNwUn0UfOD7wAqkvud3DK9vWGOHoQoJ0tJ-7bBMQaYliF76QzhpBgooPOiCi6jl05c7pky6Cp8auUtrtw8po_9Eqzdh_ITaa8uRjmxDaojGxhrjEJLXRUVe0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراهی پاکستان با آمریکا در مسئله تنگه هرمز
🔹
وزیر امور خارجه پاکستان که کشورش مدعی میانجی‌گری برای پایان جنگ تحمیلی آمریکا علیه ایران است، با موضع واشنگتن علیه تهران همراهی کرد.
🔹
محمد اسحاق ‌دار ضمن مخالفت با کنترل ایران بر تنگه هرمز، خواستار بازگشت وضعیت این آبراه به زمان قبل از جنگ تحمیلی آمریکا علیه ایران شد.
🔹
رسانه‌های پاکستانی به نقل از وی گزارش دادند: «عبور کشتی‌های تجاری [از تنگه هرمز] باید نامحدود و بدون هیچ گونه هزینه و عوارضی باشد».
🔹
وزیر خارجه پاکستان در بخش دیگری از صحبت‌هایش درباره «پیمان مکه» نیز گفت: «کمیته راهبردی، سیاسی و دفاعی تحت توافقنامه مکه به زودی در ریاض تشکیل جلسه خواهد داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/465858" target="_blank">📅 17:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6b308b97.mp4?token=MbfMul3nB6de7aSGzakAq_Hm7mZ6xsn4Itm2jrj1f-nckGd00U5gGMG4m8y8_u3I6Ih5q3LG-ILRC6kD2nLaYNl60P8tAJpMgFhWQqcTsJ-8vuISDpUg9tEp9rwqMDmGxJoLaVDtsSpPra_N7SG5TRBKBC61X4RwkB9nwu73TQ1QoxU_IWVhMTTsNLS8kMdkh_PstJU_4Oq3qbB-F2zGb1xlE_0xUZfNjFF6kJdB0z_v1xmwF00Bt4qHhREVwf683-GL35CnkaLb94oKQ4ksn6YbxCEUwoHg-82TcQakmwHDQyCYsCW3rR6lALR-X5HpzFD_8v5-1aJWSDTEECszPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6b308b97.mp4?token=MbfMul3nB6de7aSGzakAq_Hm7mZ6xsn4Itm2jrj1f-nckGd00U5gGMG4m8y8_u3I6Ih5q3LG-ILRC6kD2nLaYNl60P8tAJpMgFhWQqcTsJ-8vuISDpUg9tEp9rwqMDmGxJoLaVDtsSpPra_N7SG5TRBKBC61X4RwkB9nwu73TQ1QoxU_IWVhMTTsNLS8kMdkh_PstJU_4Oq3qbB-F2zGb1xlE_0xUZfNjFF6kJdB0z_v1xmwF00Bt4qHhREVwf683-GL35CnkaLb94oKQ4ksn6YbxCEUwoHg-82TcQakmwHDQyCYsCW3rR6lALR-X5HpzFD_8v5-1aJWSDTEECszPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سالمندان از شنیدن این کلمات ناراحت می‌شوند
🗓
امروز روز جهانی سالمندان است. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/465857" target="_blank">📅 17:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
انفجار جدید در تنگهٔ هرمز
🔹
شرکت اطلاعاتی امبری اعلام کرد یک نفتکش با پرچم پاناما هنگام عبور از تنگهٔ هرمز «هدف اصابت یک پرتابه قرار گرفته و ستون‌هایی از دود درحال خروج از آن است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/465856" target="_blank">📅 17:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKWiRmA3laQBIBEW8-vwqLjWVKaaEOyl2wxBT50FJbgpyccAZe0ukibk75qszWFl16OuiXKkZWpGNdcTiLMz_QenYZDlwvZBD7ZPCfta4atoz6gyFJbFNfXbj6ExvUN9dx6UUJa8auz00wU1Z0_NEE8rw1MdRxwYuNM8FoOGE7WZu1xf9TjqDER9ysma7_bvwiTXFJhP40i2UilcdbcBiurX7TU26CLjC0gQZcU5CtSUnEgjga-Nbb3YZX-4EN73T93dVW9z5BVCFbrwW6aQUdhS9VVCWg3C71VCY-QHVd-qRcSWffvTxVowURE1UxWqoktqpjjQ6ih1l7mwJggv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای کاهش قیمت گازوئیل دست به دامن اروپا شد
🔹
دولت ترامپ از آلمان و فرانسه خواسته برای کمک به کاهش قیمت‌های فزاینده سوخت در بازار جهانی، بخشی از ذخایر استراتژیک گازوئیل خود را آزاد کنند.
🔹
دولت ترامپ تهدید کرده در غیر این صورت، احتمال اعمال ممنوعیت صادرات گازوئیل آمریکا به اروپا را بررسی خواهد کرد.
🔹
این مسئله یک دوراهی دشوار برای کشورهای اروپایی ایجاد کرده زیرا کشورهای اروپایی از یک سو برای مهار قیمت سوخت داخلی تحت فشار قرار دارند و از سوی دیگر باید ذخایر کافی برای مقابله با احتمال تشدید بحران انرژی در زمستان را حفظ کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/465855" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzbmg89AhmLpbkoqhaFD13vIIvUBgRbMQJJL-Q8uqOXeXFRygIO0u0OauGClvtrGgQ7LqRgKD_7iMw01p-Z71R5xOEv-Bi3xJIp5Et-nN3HAjCHaU0zvKXpNKzEaKjCV9vQyZK8gqLTTV3OGYRcb_mpnKCRSvdGh_Y6vVuzRepLKfA7A8K3cYdOPP25TR9nFj5xzTvDM2RNWH2cwDZvdAwSVIyN4jyACE3NfIw2uL6tGAdatoiEIoT-RzlHu3AfOILhskhR5U4g04QX9tXcb6wPGvXzcvd4wZgLwyO8Jm3NY2R3GhnNNSh9TXxB1PldSwmaiwNrDPtmuDQhAPFNwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض ۵ هزار دلاری هرمز بر کالاهای کشورهای عربی
🔹
با تداوم مسدودیت تنگۀ هرمز، شرکت کشتیرانی مرسک که بزرگ‌ترین شرکت کشتیرانی دنیاست اعلام کرده برای حمل کانتینری به کشورهای حاشیۀ خلیج‌فارس تا ۳۸۰۰ دلار هزینه اضطراری دریافت می‌کند.
🔹
براساس اطلاعیه شرکت مرسک، این شرکت برای محموله‌های مرتبط با بنادر کویت، بحرین، قطر، امارات، عراق و جبیل عربستان و برخی بنادر عمان، نرخ اضطراری تعیین کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/465854" target="_blank">📅 16:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWAqAY6Bm4morkkWOmRuAJ3e6fVGpLqaCsMHUMuq0FLDoZM99bw0IfRfXPYYw-qHMevtk3cSvtb_M5m7CRXSWjIUh0wL-DEEH0Djs65vLD0iNvRsoQpp7-nh5ko0B4Q-Y_yiFOcDtPVBMEZ0h3jl0QQabTPIGW8julzKTceRpOfHe-wDFIRUXq-z1GgBWyFMHF44ZlFXXNnTIB0pAqiSMwmVzD4mYxrV1v_Pqpb5POKwcQmoIDFk_vHd1NJeZ-Cb6J_75GRgH8msFMroQf2DLu-DYGUCPnrTp3NTF83JdhMzcpZoLn-no11Ng_Zg96z54QwJgmj7smFExCxK8SUZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کمک‌های نظامی عراق و چند کشور اروپایی را به آمریکای لاتین داد!
🔹
با وجود مخالفت نمایندگان دموکرات کنگره، دولت ترامپ ۵۲ میلیون دلار از کمک‌های نظامی اختصاص‌یافته به چند کشور اروپایی و عراق را به کشورهای آمریکای لاتین واگذار کرد.
🔹
به گزارش واشنگتن‌پست، بر اساس این تصمیم، ۵۲ میلیون دلار از بودجه‌ای که پیش‌تر برای اسلواکی، مقدونیه شمالی، تونس و عراق در نظر گرفته شده بود، به پاناما، پرو، اکوادور و کلمبیا اختصاص می‌یابد. بخشی از این منابع به‌ویژه برای اسلواکی و مقدونیه شمالی در قالب بسته‌ای تصویب شده بود که هدف آن حمایت از کشورهای اروپایی آسیب‌دیده از جنگ اوکراین و تقویت توان دفاعی متحدان آمریکا در برابر پیامدهای تهاجم روسیه بود.
🔹
حذف کمکهای نظامی آمریکا به دولت بغداد در شرایطی صورت میگیرد که علی الزیدی نخست وزیر عراق همواره تلاش کرده منافع واشنگتن را در اولویت خود قرار دهد؛ راهبردی که در داخل عراق با مخالفت و واکنش‌های گروههای سیاسی مختلف روبرو است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/465853" target="_blank">📅 16:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYPoXImg5nar-BvgYXpM0RkTiyq6TMBy3J_Ib0nLQUATTcP3QG61hVzQCJnKh7BFkfrAsUN0qnYdZHintTEcy2g-AC68HjGhfyNd-tFzEUu2nfvLrTy1BqzM6vi2xWOUbvFY_80gyiivWhqGlbEr4lfXCokSxFKaD_wDCnaCqyeph_AUQCLxJCs6uUZqVD2amb7Qul7B8bxOrhaAahXGA4ugMsUXBs11GLM_4_K6qT530KG0sD0rgAacqHOAZzwIBYZ9bDHKieXeLwwuOBfMvCh46WXX2sl9_k-a9NosXPy3CQtPCZNj985ogKJxBQj32li8rartu5YPTdIs4ghDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به التماس افتاد: اگر به من رای ندهید دموکرات‌ها مرا استیضاح می‌کنند
🔹
ترامپ دیروز در جریان سفر انتخاباتی خود به ایالت‌های تگزاس و اوکلاهما، از هواداران جمهوری‌خواه خواست انتخابات میان‌دوره‌ای ماه آینده را جدی‌تر بگیرند.
🔹
ترامپ خطاب به هوادارانش گفت: «لطفاً تصور کنید که من نامزد انتخابات هستم، چون واقعاً در برگه رأی قرار دارم. اگر پیروز نشویم، آنها در نهایت مرا استیضاح خواهند کرد».
🔹
اظهارات ترامپ در حالی‌ است که حتی بسیاری از جمهوریخواهان حاضر در انتخابات هم تلاش می‌کنند به دلیل عملکرد ترامپ از نام او فاصله بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/465852" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlme9tbh_UrH_oxRHt1KipHkg7ze-kWgcxwWccDh4LmbFMJ4-LET7aiYNaqB9CHM4bSthrrvHFBiMoA2epFmAMEiu_40SmKupqjTtT1rlS32wB85b7O9Zt0xOmUKFjvQXkGuq5eDizjsm6vbo5P-EC74n-iUgzBkVP4H6UNJD8BjEs6Ua-uLESuiFxmg7vYEvuQCgPn70ymUbVafzVGXOceI8XIG7uoO9xIR0u83vW0DwwB5G8KmDT-6qtTEUgjiWOLnKeIjy2F9svYXG49ZEb6tabg_R1P5FtlFDAEwK-0NArzAxttUNXMfT_Tf0aj3NkiWRICB3i2qyBakCA0oZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465851" target="_blank">📅 16:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c8bc66dd.mp4?token=HK5ybBb3UvwTs5ioagkBS6_KdKnbnOE43c46JqG-MIaJzUcKsF8cgafZgHIyktklUxIBBI-M_plwNONiCbBSvKPAHmiXVx57nW-6cX65PjzioS1ipLUpZAL-TWjtJ6T88EXGfNXWfQO_I-T8NtNzDVGhcdCZrXiRjxjUH83vp7HIG2wal7Qa8tWIBlOD7o-c_4c9YwdFXZKuO3ipVOvEr-EJdxsFty3VZSBVOvdpfxmM12UX2TgPSpcf0M4qC8UsG6X9ZVaqk8EjrVuZdn-BuJN3Xt2fdSKY3mufJeIW6Wr4IjmDAbYx0Dc4pjicQA_LDZwe1vZOFo8pgdmbLkpztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c8bc66dd.mp4?token=HK5ybBb3UvwTs5ioagkBS6_KdKnbnOE43c46JqG-MIaJzUcKsF8cgafZgHIyktklUxIBBI-M_plwNONiCbBSvKPAHmiXVx57nW-6cX65PjzioS1ipLUpZAL-TWjtJ6T88EXGfNXWfQO_I-T8NtNzDVGhcdCZrXiRjxjUH83vp7HIG2wal7Qa8tWIBlOD7o-c_4c9YwdFXZKuO3ipVOvEr-EJdxsFty3VZSBVOvdpfxmM12UX2TgPSpcf0M4qC8UsG6X9ZVaqk8EjrVuZdn-BuJN3Xt2fdSKY3mufJeIW6Wr4IjmDAbYx0Dc4pjicQA_LDZwe1vZOFo8pgdmbLkpztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر ایزدی: غافلگیری‌های فناورانه برای دشمنان داریم
🔹
جانشین فرمانده‌کل سپاه: نیروهای مسلح ما به‌ویژه سپاه پاسداران در عرصه‌های زمینی، هوایی، پدافند هوایی و دریایی یک خیزش بلندی را برداشته‌اند.
🔹
نیروهای مسلح از انواع فناوری‌ها استفاده می‌کنند که برخی از آن‌ها در صحنه مورد استفاده قرار گرفته شده و برخی دیگر نیز در آینده مورد بهره برداری قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465850" target="_blank">📅 16:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmFxpBPeM0CnILhnJSTaN_UCHR0UHdZE4GO1UBHELZx-2PLQtwPFa4BxITWqeipMDAPEQICCTBv5zLwB80Vd22TONIf8kfXL-9_l2AAY8TEGF5aCGMvpoGkLx4FZjIHYHwvRbQsaiMd0KdEBUwi5T-A8ekaoqsjJtX8UT4X53JZwqUTnm7Y9DNhiLt7xDNtcV3zGxALeF2rAqb5E8WKdKH0VlUtZcLzQV65vr723iZcpN5tNmbAIDvz2mbYml60bZ7KqY4SgtayNI0EaI5sxaru9NAypdzTYH5PLdLc2flZG2eyGolbuPgP4gO7PEIE9DjrggcpY6wyR8ozGi9cllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرائتی: در مساجد باید به سوالات کودکان و نوجوانان پاسخ داده شود
🔹
هم در مسجد و هم در مدرسه به پرسش‌های کودکان و نوجوانان با منطق روشن و رسا پاسخ داده شود.
🔹
تقویت حس پرسشگری در آینده‌سازان و رفع شبهات و تحکیم عقاید آنان از لوازم تعلیم و تربیت اسلامی است.
🔹
امام جماعت مدرسه باید با رعایت اصول روانشناسی، ارتباط صمیمانه با دانش‌آموزان برقرار کند.
🔹
سازماندهی امور اقامه نماز در مدارس را می توان به دانش‌آموزان و پدران و مادران آنان واگذار گردد تا بین خانواده‌ها و فرزندان آنان نوعی رقابت سازنده برای میزبانی از نمازگزاران در مدارس ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/465849" target="_blank">📅 15:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMl2hZcA1MGRALlpMXcKY9ot4ElRI3_aGmt5HkdUKDWkk68x0pCq6h8UUwktoOJO5mzmuo_XdwwlOt5Q0E-M3Cphkjr4KrrL3WFsffCOXsG8Bj67oEf1qZL5M4QU8rwxrmSBZjRscFftmH6D8L8ZEqp8DS_KdjB8DD1GHp0vZ-q7VU8yFzw8P0tkzUDQJkbRLZGxxwiUdlWPcqZ1HWUU9wWCAWhoOLD2ilDcwY2ATG5xQn6JRcroKUfJ7BIPI9Q2vEcde2KkPJQlOhlay-6Rzjojh-0S8ryOec7ZrtmKcFe1m1MvCPRd8HKvURUeOxUzlX2CPj8hasFKISiyC5fU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب ‌جمعه تهران: روند پایان حضور آمریکا در منطقه آغاز شده است
🔹
حجت‌الاسلام ابوترابی‌فرد: مقاومت ملت عزیز ایران، محور مقاوم و ملت‌های قهرمان افغانستان، عراق، لبنان، غزه، فلسطین، یمن و همه جهان اسلام، آغاز پایان حضور ننگین آمریکا در منطقه است.
🔹
این جنگ پایان تلاش آمریکا برای تسلط بر منطقه را رقم می‌زند. این نگاه تحلیلگران هوشمند جهان به این جنگ نابرابر است.
🔹
ملت مسلمان منطقه و ملل جهان شاهد بودند که دموکراسی آمریکایی برای ملل منطقه چه ارمغانی داشت و چگونه خون پاک صدها هزار مسلمان، زن و مرد و کودک، در افغانستان و عراق بر زمین ریخته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/465848" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c33znEM2FzF7M_HYtmXFIeW-kNJcTe-JLR_kjOFTB1Fda1AoqE0buSdBtafGQTkXsojGe8gGjSJaLH9IXEeFg0VLSM0Jsz952922PP4zKqzHxl6ffOgDVccdcZ2QAJKzY0bgv0wDBaFDwE8P8d51QrrpunEOt10ztVzVmBRD9Iiah6RqsAdeUbo2kV3GDzTPnDeTw76m0mYtztWtPhAMfe0femIN0R3YaDPGbK9P_LbfMOr707AvD4pRlInzUJIlKyQMQEHRJA5axI45nXYhK2AwInBsoMGm716vx1EimS3ku-z3XSTkoHmlJVDcX3dWRCr7ZHsatsyL1UEMLPRVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله علم‌الهدی: مسئولان طوری رفتار نکنند که آمریکا تصور کند به مذاکره محتاج هستیم
🔹
آمریکا امروز بار دیگر در محاسباتش اشتباه می‌کند و فکر می‌کند مقاومت مردم تا قبل از نوامبر تمام‌ می‌شود و تنگه هرمز باز می‌شود.
🔹
مردم ما تحت‌تاثیر فشارها و تهدیدات آمریکا قرار نمی‌گیرند و امیدوارم عزیزان مسئول ما نیز متأثر نشوند و این تهدیدات در آن‌ها اثر نکند.
🔹
متأسفانه بعضی از عزیزان ما در مراجعه و مذاکره به آمریکا، ژستی به خودشان می‌گیرند که آمریکا آن را در دنیا پخش می‌کند که این‌ها انتظار مذاکره دارند و به مذاکره و تمام شدن جنگ محتاج هستند، نه ما.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/465847" target="_blank">📅 15:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c9623fd.mp4?token=r-jMeWktm1ys2kloqz5aWxs99vAcchAWFzT7kSy_rLvNv_mAi8SL4Aqt_YCLbH1GhQdde6hw4BSlJ0QoYTH-k2Ai6Rjb8lddxo7vSGxMSO6ITKDtLGV1yrIk3WF0N3P_hlXMbERdnGA9CxXxO-CGdXOs_E0WUGTgd0UAUTYLyk2_totLEMaJe60WWcLR6XgdOd0NIsaF8EH05GGIWqrw2M5kI3rme2EZr9nw_QHH31N7ym37ocqvKZ0WgUhIxpxlcxBP3VYvt4WF0rLf4WHFoR2P7PMItWORBDl1mRQz4nURbOxUdB12RWu2_U-1lmZMgOBhHg_aXyZF5DzvIIPK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c9623fd.mp4?token=r-jMeWktm1ys2kloqz5aWxs99vAcchAWFzT7kSy_rLvNv_mAi8SL4Aqt_YCLbH1GhQdde6hw4BSlJ0QoYTH-k2Ai6Rjb8lddxo7vSGxMSO6ITKDtLGV1yrIk3WF0N3P_hlXMbERdnGA9CxXxO-CGdXOs_E0WUGTgd0UAUTYLyk2_totLEMaJe60WWcLR6XgdOd0NIsaF8EH05GGIWqrw2M5kI3rme2EZr9nw_QHH31N7ym37ocqvKZ0WgUhIxpxlcxBP3VYvt4WF0rLf4WHFoR2P7PMItWORBDl1mRQz4nURbOxUdB12RWu2_U-1lmZMgOBhHg_aXyZF5DzvIIPK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت رزمایش جانفدا در کرج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465846" target="_blank">📅 15:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gynPG-3jjGEku9qIxxSFrSJ6yuMGtOudNNLRZHjDu3gRd8cfZJzS3z7JpL84NnjWSaE7QY9BHGTGRBA2faPCADTJ-lt8V57xob2M3_RBEP3cS6diqBOsq_06_92Ce-3Kfdx3pHSiwj8fiXmwa6E626U_xv0Z3kejJtTK_NIv6t4kK45uHLj9eBnto1dGzcpr0F5GBkrJgUGkZ_mD290FFgNsxSn1YW1DTCTAa6_0mnhjwbabCmEA77P8xkmLSK9bTkR4HIHAHqFRTJhNyqpuDryji2Oy46in1mKRgyyE5xPqwdAIdID_1dzk7axhLLnzV92qrSREAqzW5vuqPWuC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخیر‌ۀ گاز اروپا نصف شد
🔹
آمار زیر ساخت‌های گاز اروپا نشان می‌دهد،‌ ذخایر گاز کشورهای اروپایی به کمترین میزان ۴ سال گذشته رسیده است.
🔹
کشورهایی مانند آلمان و هلند ذخایر گازشان تقریبا نصف شده و به ترتیب ۵۷.۹۷ درصد و ۵۸.۸۹ درصد ظرفیت گاز دارند.
🔹
در آمار کلی هم حدود یک‌سوم میانگین ظرفیت ذخایر گاز کشورهای اروپایی در ماه اکتبر ،زمان اوج سالهای گذشته، خالی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/465845" target="_blank">📅 15:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee0d567c2.mp4?token=q9b5zjkOfbdL-RhqjarVhNj1cLKbeajG7-gTRXYR5e9aJh08kvK_MBITRxTEz6EUEfsrRAWiRdmxsUrwPYPNsTbb5HaYhV-l7452oO5Dxrb5mPFUes0Pc84uHwKJYeSucqDKPzO4cS_cnBnEG4Qz-X3fu-sF6nGxqw8VjVspMoQyaRSjreC1doaSYIFGzYR7aARKQJtp7alGqVdIj-8Ii8zCttBhwhjQcDzbvD5DX48ryC18Hp1lVPwWS2EGh5iEJiiW_lVErru-cIvuIuOp1834UNcKT9Vze8xniv5jNLqZ3DVy0Ew-IGcy_99Qk-Dw2d53ngBY0jaRCGoj0TIfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee0d567c2.mp4?token=q9b5zjkOfbdL-RhqjarVhNj1cLKbeajG7-gTRXYR5e9aJh08kvK_MBITRxTEz6EUEfsrRAWiRdmxsUrwPYPNsTbb5HaYhV-l7452oO5Dxrb5mPFUes0Pc84uHwKJYeSucqDKPzO4cS_cnBnEG4Qz-X3fu-sF6nGxqw8VjVspMoQyaRSjreC1doaSYIFGzYR7aARKQJtp7alGqVdIj-8Ii8zCttBhwhjQcDzbvD5DX48ryC18Hp1lVPwWS2EGh5iEJiiW_lVErru-cIvuIuOp1834UNcKT9Vze8xniv5jNLqZ3DVy0Ew-IGcy_99Qk-Dw2d53ngBY0jaRCGoj0TIfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آئین سنتی-مذهبی قالیشویان در کربلای ایران
🔹
این مراسم که هر ساله در دومین جمعه مهرماه در مشهد اردهال کاشان برگزار می‌شود و یادآور شهادت امامزاده سلطان علی بن امام محمدباقر(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/465844" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شهادت یکی از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
روابط‌عمومی قرارگاه قدس سپاه: تروریست‌های مزدور دشمن با کارگذاری بمب کنار جاده‌ای در یکی از مسیرهای مواصلاتی استان سیستان‌و‌بلوچستان، اقدام به یک عملیات تروریستی کردند که درپی آن، یکی از رزمندگان اسلام به فیض عظیم شهادت نائل آمد.
🔹
روند شناسایی، تعقیب و پاکسازی عناصر تروریستی و مزدوران دشمن، با قدرت و قاطعیت تا نابودی کامل آنان ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/465843" target="_blank">📅 14:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw_bRwTqBIDoYKugIgT888CVcd62mMLDBLdRavy_VS9M2NbYd1aBZcndnd97pxSIM41NaEBuKBT6jRDdbAS4sdhtJ_QsrPD7z4hNWQcmBoQA9Akc8F7bZXbAZOYDeOJVQW8nlYttKwBPLhdV-R_as7jJniZ_70e5bg0LKxReLg_guMuS9KxqdhQWy7JAeIQqDkSdXdLszRlRmEwJSlhDwOYrN42FhUkJjWtZfRxC6KwO_2H7rfGmIVPiUwnq-u6uZiG47y4wAe8C_HYYA0HcFp-n9-82_lEnPzsIGyf6Ju0X-0f3nbb6tyKTDrJQfouZJV_SgJYFBjtYW_Sr7LiCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر درگذشت حجت‌الاسلام قرائتی نادرست است
🔹
پیگیری خبرنگار فارس نشان می‌دهد اخبار منتشر شده در فضای مجازی درباره سلامتی حجت‌الاسلام قرائتی نادرست است.
🔹
این استاد بزرگ قرآن هم‌اکنون برای حضور در اجلاسیه سراسری اقامه نماز در مشهد حضور دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465842" target="_blank">📅 14:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b367731d2.mp4?token=P4MNPJ_NQCvJXbUF8ehjDOkta7Pge6WnXAb8iGsoWXlbTrmCQV5quln6zRUbKIILeKKF51S7_Gdbx0RKmOHHWrK1c3Q8P902zQIQEdw_IHQjfy5UewgbJVYkeMm7em9g4YH3rCjBg9QU8qu83zRBOu6Kn5BuNKLTsL5-_9qNhPozfkk-BhAWEf0DE6nq3I71YD8XJQgKH2JG5F2SDjt-A9YglXp1wqMbj07U3OLM3F-9wDKLmcuTeGNK1xWTHa-4FUI_mOooQ0PLApAPP8PlCjQNBqTZnIH4_wa-qNfdPXzzNeAnkToLvawFx0vDQUof9AcxxU-he2gBIKZphKga4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b367731d2.mp4?token=P4MNPJ_NQCvJXbUF8ehjDOkta7Pge6WnXAb8iGsoWXlbTrmCQV5quln6zRUbKIILeKKF51S7_Gdbx0RKmOHHWrK1c3Q8P902zQIQEdw_IHQjfy5UewgbJVYkeMm7em9g4YH3rCjBg9QU8qu83zRBOu6Kn5BuNKLTsL5-_9qNhPozfkk-BhAWEf0DE6nq3I71YD8XJQgKH2JG5F2SDjt-A9YglXp1wqMbj07U3OLM3F-9wDKLmcuTeGNK1xWTHa-4FUI_mOooQ0PLApAPP8PlCjQNBqTZnIH4_wa-qNfdPXzzNeAnkToLvawFx0vDQUof9AcxxU-he2gBIKZphKga4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تکواندو هم طلایی شد
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم در فینال رقیب ازبک را در دو راند شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/465841" target="_blank">📅 14:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6aa37163d.mp4?token=Xn0yI9EBHevOMGaLrlPfWnVW0yFw7dy_B0w1xVexBu9k9GDU-YvHDkyiQOkwvdYqY0fwQOm6WQHsJ36mh7EV952JSmdAr7pVkxxD8ra2DXlc2c1y6sIffHBMRE9VUnwAWtOxakSLmmm4opQIf5QaCHLFP0L-gasx9qpZKLJIXdH101kZwgh9jUiaf94wHZua-qbNcDjXTEJgcz_wthQw2EJ9YM1egBSqqj-0OUtvyAMD3_unOz8HD3SQDRsciwntX-UBXvsjoedRTPhAVuLn8mQXIsUU_U5OrTSkO0vc_gTgPopSqRMljQlOMmFARnR1ALhdyNEecXpxsMk58165lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6aa37163d.mp4?token=Xn0yI9EBHevOMGaLrlPfWnVW0yFw7dy_B0w1xVexBu9k9GDU-YvHDkyiQOkwvdYqY0fwQOm6WQHsJ36mh7EV952JSmdAr7pVkxxD8ra2DXlc2c1y6sIffHBMRE9VUnwAWtOxakSLmmm4opQIf5QaCHLFP0L-gasx9qpZKLJIXdH101kZwgh9jUiaf94wHZua-qbNcDjXTEJgcz_wthQw2EJ9YM1egBSqqj-0OUtvyAMD3_unOz8HD3SQDRsciwntX-UBXvsjoedRTPhAVuLn8mQXIsUU_U5OrTSkO0vc_gTgPopSqRMljQlOMmFARnR1ALhdyNEecXpxsMk58165lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
زارع در آسیا هم تاجگذاری کرد
🔹
امیرحسین زارع در فینال وزن ۱۳۰ کلوگرم کشتی آزاد حریف ژاپنی را شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/465840" target="_blank">📅 14:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🎥
زارع در آسیا هم تاجگذاری کرد
🔹
امیرحسین زارع در فینال وزن ۱۳۰ کلوگرم کشتی آزاد حریف ژاپنی را شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/465839" target="_blank">📅 14:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8165271cc7.mp4?token=LkCLs-GBlg0rLRmGwxtp_UJvzC13wmOMN7YeCChadwQMxPr__iGC3Sx6U32nN8pmJReaqukCg6NxwK3NAPbDpu_cjhkEYstNfW09rbf7eg944RfoHJPGlQG5XlXuL4V0EovFmPcCh4mPMtFGIiqf9IFjDrwxoKMguvAVftG_rstzZK-4YjyAxjZDNMIsCPVXI4fX3Jp34AfSAUtYYfPSWoTIR_P8VVuTgcyNsXgwXUQx-dRV7QwvJ7RfupYS79Ip3sIfNYqf-vNUlFDxxuyFAS0tHl_r20rSZBb6LUjTJAQzWvaXO_BG2xSnZddu15KYrJN9s0TDMozqw_iA5K0WwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8165271cc7.mp4?token=LkCLs-GBlg0rLRmGwxtp_UJvzC13wmOMN7YeCChadwQMxPr__iGC3Sx6U32nN8pmJReaqukCg6NxwK3NAPbDpu_cjhkEYstNfW09rbf7eg944RfoHJPGlQG5XlXuL4V0EovFmPcCh4mPMtFGIiqf9IFjDrwxoKMguvAVftG_rstzZK-4YjyAxjZDNMIsCPVXI4fX3Jp34AfSAUtYYfPSWoTIR_P8VVuTgcyNsXgwXUQx-dRV7QwvJ7RfupYS79Ip3sIfNYqf-vNUlFDxxuyFAS0tHl_r20rSZBb6LUjTJAQzWvaXO_BG2xSnZddu15KYrJN9s0TDMozqw_iA5K0WwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخودی برای ایران طلا صید کرد
🔹
محمد نخودی در فینال وزن ۸۶ کیلوگرم ۹-۶ مقابل هایاتو ایشیگورو، نایب قهرمان جهان از ژاپن به پیروزی رسید و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465838" target="_blank">📅 14:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsxHRX4bRkubnNQcOwXcs8tag4hDerPZcjkyFHeecFt7lnPSbtP8UnA470qa7wQOX4Lhm9AL0TW_A2SJvqc0Ec3RkmC7U_P0m4p2q8B38rf6Bk23MzRRKPnQcOY4mRh49rO06LYEe0KkBzD4YBbSaxR2iV2FIrRfY0WiIywXkpRGz-8CnX5IVxyhDcVny239M9crds30TMRpecpgZLCiiCoV7YGXloeYuotnhsirHeTNDvnIUiYCsAocKJiKJzIbGMzFzw1AfqwVO_DFCQF6TBCRMdV4y0W5gDAwOTbxfGowaNyN5pciVPQ7UdcSwmR2hokEQnMVPScyRUvBHIyKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان ایران یکسال بیمه شد
🔹
بنابر آمار وزارت جهاد کشاورزی، امسال ۱۴.۲ میلیون تن گندم تولید شده است.
🔹
نیاز گندم نانوایی ۹۰ میلیون ایرانی مجموعا ۱۰ میلیون تن است و تولید ۱۴.۲ میلیون تن گندم یعنی تا مدت‌ها هیچ مشکلی در تامین نان وجود نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465837" target="_blank">📅 14:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVmEeiOh0XF66eakjU5QmOOTxYKfjBqTjz4-xzBQI-E4cnskiX6ejtYZpims7sQX82bNJHfZXDtWAK7TMWkMUd0f_eGqm04fPjjLNwXyFw5yrDle1dUFBD0jvW82frS3Rmg5O35njv8byaPG8tHI-uuBo9kELoV0nQ_88fZ69-yHXm89F3uufz8t9mCNUzWGpz1kuSIW51SaSYoxLaNlf-CPmeL375ZOqBjmR0bwLP4hjcoYxE6nZ_GM4sJqW9Wl6gX1ijGAeBT4OUXQILKiiuVXLSQd6OCMvURYfZ6kRjUYtP0IXu0Q4CP5L-76HsBmIJD88Th5LcJfBojgvM0eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ «إنا علی العهد»، امروز تهران
🔹
هم زمان با بزرگداشت دومین سالگرد فرماندهان سرافراز جبهه مقاومت ازجمله شهید سیدحسن نصرالله، شهید سیدهاشم صفی‌الدین و سردار شهید نیلفروشان، اجتماع بزرگ «إنا علی العهد» امروز از ساعت ۲۰ در میدان انقلاب تهران برگزار می شود.
🔹
در این مراسم سید محمدرضا نوشه‌ور و علی‌الرضا عزالدین از کشور لبنان به مداحی خواهند پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465836" target="_blank">📅 13:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucFS_F8Pe6qFmDYv14R5XeBBSOKJY9GMY_IJZy2PyEZGXr-KCF2S8oHq9K4bwCxCf1IhDVIzbwiC_TYN383HCQj3GqE4qcI-4QseOX6SWxVRXbKlDarQXHE57fLlJWPYYeyjz8VKfTLgPLEY0AuiQgncX3ChMbsy7X_tR26H4p3OcWOrxd_KelZYK9lLF5ZF9bwcB-TlB_S7WdAiTtaBvIExD-_PG5I9hY8TA4tFYkQ4fMWdPPee3f-2iwCSNWtnAiu-rXRXi5jRVo4ZRr44m5Ba5lWomkP8cAWXtSxZtaBbzDuxOJCSoy06uOXfdEAvItu2jz458UiC2C-gEa8ssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور ابراهیم‌زاده برای برنز  به قهرمان المپیک نرسید
🔹
عباس ابراهیم‌زاده در رده‌بندی کشتی برابر کیوکا قهرمان المپیک و نایب‌قهرمان جهان از ژاپن ۳ بر ۲ شکست خورد و به مدال برنز نرسید. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465835" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgOG5TD6yDZXHBkfeFyag_habLNaUZ53lCwRCUg5C491C8P80msOBly3T7WyDpfHlzqvKeQg86aeJkRxiNDVdYa8TKUBHd_o9kJfuA4y4XUuwJNqzVO16LngkPt0o3qML9R2wwE_oe3TkSzq3zKmP9AyNLA1qxH_xVckA98qGJufpLBPLA2e98XH3939U7GWbMkbv4etpr5Sktip4OoJ_f4bRh2RlhiI7322SxIpZfefr1V_dcus0HTpeC6WGaaz1dIFupaM-5gVO2zxmjFpc7REBCpJI5wbxHeVJ6z6rFYr0GRGPJiH52mwoyvlyr-zkXTxr4AXqANMvPYrIMqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوشنر؛ مذاکره‌کننده صلح غزه، سرمایه‌گذار جنگ اسرائیل
🔹
گزارش تحقیقی شبکه خبری سی‌.ان.ان فاش کرد داماد دونالد ترامپ در زمانی که برای مذاکرات صلح غزه فعالیت می‌کرد در شرکت‌های مرتبط با ماشین نظامی رژیم صهیونیستی سرمایه‌گذاری کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/465834" target="_blank">📅 13:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امام جمعه موقت هرمز: تجاوز از خاک کشورهای منطقه، اروپا را هم ناامن می‌کند
🔹
حجت‌الاسلام شهدوستی: رژیم صهیونیستی با این عملیات طوفان‌الاقصی آسیب‌پذیر شد و ملت فلسطین با ایستادگی، قطعاً پیروز نهایی خواهند بود.
🔹
نیروهای مسلح ایران با اراده‌ای راسخ در برابر زورگویان ایستاده‌اند و پیروزی از آن رزمندگان اسلام خواهد بود.
🔹
اگر خاک و آسمان کشورهای عربی در تجاوز به ایران به کار گرفته شود، نه منطقه روی آرامش می‌بیند و نه اروپا در امان می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465833" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff724153a.mp4?token=KsfwA1sNui3QdmhDLwfytjkk90tAPw-An9k13Z6zlD28-SQXdp5Bh8LmEo8zWaqEOw0P_XBybqqwo1AV_BbxpO0rCbubewM18iA8C-C1riy6Z65BZ23A0DU0UryPJ3N879jTgr4fucywug65z4YYiACCG9ZN5YVOj7FDQRDKY9bO2e3jE7P2dusQhfva5QjavntDHtc1S-tTrcNet4tlwCLLV1x4oZj7MLu9Ipr9osP3BdPLWoZr2_8WY6ht0046RJtLROOv0g4amaJCnqfeXTYhNlbpQcUcv4wwa_R6_OSObA3yywla4U-3DewJa3BYPuhF1A09_jMS0wg71GMspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff724153a.mp4?token=KsfwA1sNui3QdmhDLwfytjkk90tAPw-An9k13Z6zlD28-SQXdp5Bh8LmEo8zWaqEOw0P_XBybqqwo1AV_BbxpO0rCbubewM18iA8C-C1riy6Z65BZ23A0DU0UryPJ3N879jTgr4fucywug65z4YYiACCG9ZN5YVOj7FDQRDKY9bO2e3jE7P2dusQhfva5QjavntDHtc1S-tTrcNet4tlwCLLV1x4oZj7MLu9Ipr9osP3BdPLWoZr2_8WY6ht0046RJtLROOv0g4amaJCnqfeXTYhNlbpQcUcv4wwa_R6_OSObA3yywla4U-3DewJa3BYPuhF1A09_jMS0wg71GMspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر تکواندوکار ایران در آستانه کسب مدال
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم مقابل حریفی از هنگ‌کنگ به پیروزی رسید راهی نیمه‌نهایی بازی‌های آسیایی رسید. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465832" target="_blank">📅 13:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktZ78AQD5cHnubbS6zSJiuqLz5LHTvgYJpEjcYy7Kx85zUG0WxA5uTQAtUTZbKkMtuV--Nz42UNUBssDq3snAjVsybeeoKeJGhwtZJptQYsUVTYlNxydqq3M72SQ_0CuTlhZWJRt_rkr1VDo5E-JoY5VwKTsAh-BzP8Zby4qfjgmzfCOWwacbdl9vDrO-nbALO4h_hy212JyLmqU8dRi9GeZ4luKcPpYS0pQwF3BdPE5ihXY1wJr4ToTWfDI6KMRzqi5iFkbKfS3Ze70_GDyEIpvb1MhpbLqhNpUvDYXPkhN1ZXsgNe23-OL6oRJaYNjSyFjlLGGaqz8XfAEadEMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
والیبال ایران مثل آب‌خوردن به فینال رفت
🇮🇷
۲۵ | ۲۵ | ۲۵
🇵🇰
۱۳ | ۱۵ | ۱۱
🗓
شاگردان پیاتزا فردا ظهر در فینال به مصاف برنده دیدار ژاپن و چین خواهند رفت. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465831" target="_blank">📅 13:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465828">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTAeIZamuer9rfhaDB3umqTxmP6XA7fNGXQdBWQJe20hRV0x5ir3qvZ4bYTWFwNTwil-sf6zvzPpvdXlSxQ51GFcnRSUrwWiocRCVbDHp851EZS0hkATAobv5fljG4dalLYw1PxFd1UcnqYCcCy9NSF0ueBlTnwUSi_AyitZ2ynFYZRuzUnv6N_1PUrC4EDwXTulZR8mQO8NngB9WPK6mOmfR6SvQltzMTOhWrAWKg4OP_gURT2LScZBGIAYg0K8G6k_EAC21NtHk_MOKk94ABngb4z-Kp1KmnRhUzhVDDFPokxpBBJ7F2stPhlsOxXnpWIaraVMIKkQMKYFRYEKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ فینال ‌و یک رده‌بندی در روز اول کشتی آزاد
🔹
ایران در‌روز اول مسابقات کشتی آزاد ناگویا ۳ نماینده داشت که از میان آن‌ها زارع در ۱۳۰ کیلوگرم  و نخودی در ۸۶ کیلوگرم به فینال رفتند.
🔹
همچنین عباس ابراهیم‌زاده در وزن ۶۵ کیلوگرم هم به دیدار رده‌بندی راه پیدا کرد.…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465828" target="_blank">📅 13:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465826">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">✅
مسکن کارگری؛اولویت وزارت تعاون کار و رفاه اجتماعی
🔶
ساخت مسکن کارگری از اولویت‌های وزیر تعاون کار و رفاه اجتماعی بوده و این موضوع مهم به مرحله عملیاتی رسیده است.
🔶
گفتنی است در جریان سفر احمد میدری به آبادان تفاهم نامه ساخت مسکن کارگری با شرکت‌های تابعه
#تاپیکو
شامل نفت ایرانول، نفت پاسارگاد و پتروشیمی آبادان به امضا رسید.
🔶
همچنین یکی از محورهای اصلی سفر روح‌الله شهیدی‌پور مدیرعامل
#تاپیکو
در سفر به بجنورد موضوع مسکن کارگری بود که در دیدار با استاندار خراسان شمالی مورد بحث و بررسی جدی قرار گرفت.
@tappico1381</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465826" target="_blank">📅 12:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465825">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKDCczBbK4MZ7cupgZn-xM62kCvewlwY2iUvu_vWI4I-QfIl8sb_alAGYyk69JiehO1oSCzOtcL9z0epfjA_Fk704od5z1lWVYNZfLtt-Y4RCWvkQPnwIsiZhGZpZhJhYGZDhqJmg7IMoGPD4fhPlILO_s6X0RdAjwbPPmn_8Y9vgvdAc14o5H2UNbxvHYNeLaukdF4Yrv9t8mqDkt4pNiR6aStF6NZP32z_eon8nyPwseVUmzMxa2Axx4rlS8bjkuPH5vKa-_R3sbXD6um9ESwjLO6fITQyC67iAUhodJUYFmDbbvxCfdE9q-p1BukFzvcgt32rwKC738tgbjV4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465825" target="_blank">📅 12:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465824">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/465824" target="_blank">📅 12:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465823">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrbZ5IHRTFjQdPH3aNFcGOYPcl5alVMYv-Wt2uVbVuORRCbkyAryIJOa7FkUX8F_BN7i0ApviCaXA7RKhCqUbn4VMR4fnxaq0dBjLDwm-7re2woc-NAclzBEDKWhq6pGp4m7UcNPEOwnqj8_5kWTwL98FHq-vm_ZxSiaOIH2-1tEoIpMlihshk3AJ3ggbrRXtTW0VQpO0Et85LOVmx9iHd6FZzAvOJBtLiMvYdIQ7l_3hsSDkpPzPBnU9sq2RHpuTMPgAiQvLXd2HRDyPiRdABusweeY8Y9Ob8Akc3cx62Zn_L9xsN40RqlMNroCuj5ghz-4fycrnzSLlsQP5bZqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک کشته در سقوط هواپیمای سبک اسرائیلی در شمال فلسطین اشغالی
🔹
کانال عبری «حدشوت بدون سانسور» در خبری اولیه اعلام کرد یک فروند هواپیمای سبک اسرائیلی در نزدیکی وادی قرع، در منطقه وادی عاره در شمال فلسطین اشغالی سقوط کرده است و نیروهای امداد و نجات در حال عزیمت به محل حادثه هستند.
🔹
منابع عبری از کشته شدن یکی از مجروحان این حادثه خبر دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465823" target="_blank">📅 12:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465822">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvZTQHEtRqq6h73YtxLOYRu1T94erQUibiXu0b6_gRtcVdzFrSJXYos11_7X4qMJABfQzGGIuq8XPD7ER0B0LkBfi_Y2NlmndYIGXgVCiaqDnnJRyHMdFPbmR3jRvXCAMq3WLl5sJ7rps6CtO1wRTbBJ2wC8jQKffDIwhPxqHcNSjx1mANFoXn5lwdfsfVqZsuY_RsSnlbfZrixM-emaM2QPWf7-eHqmwptbP5yL8Ckuy2lTQIMiSYz6b8PL1yc8s9rcNnF53IFg2ghWJeHt8GUF7DGm4JM5IphuNzZ1nYCRnOnJKsknDsgMSRLgHf9PWKp6EekX1y5WAcee3EEWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
والیبال ایران مثل آب‌خوردن به فینال رفت
🇮🇷
۲۵ | ۲۵ | ۲۵
🇵🇰
۱۳ | ۱۵ | ۱۱
🗓
شاگردان پیاتزا فردا ظهر در فینال به مصاف برنده دیدار ژاپن و چین خواهند رفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465822" target="_blank">📅 12:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465821">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
عملیات حافظان امنیت علیه تروریست‌ها در راسک
🔹
یک منبع آگاه در گفت‌وگو با خبرنگار فارس در زاهدان: از صبح امروز اقدام عملیاتی حافظان امنیت علیه اعضای گروهک‌های تروریستی در راسک اغاز شده است.
🔹
گزارش اولیه از هلاکت تعدادی از تروریست‌ها حکایت دارد و این عملیات همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465821" target="_blank">📅 12:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465820">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oimaKR5wBcbkpW-ckmSztAqJ44Mc0zOd6FLDRCd5X-LWDMfoJpL9HJv8j9p6ZrfwS8YHQo4NUDSMV2LYdkf53hqYTuOqzowYZAtDTdqBCLu8LdxWQtgFdtR4GTUWflt1vL-OgrztFR-tKt88nlwMyTt5e18oTHYIZ-9_XZcYkQrilQCauwFkg3bJE_J7Qc8zR3sBFQuMWXihNH4bFJB7_ek5jRYcHGYsdY2lBp3wFdBjgaXN_27g7c6UWrPt49OLOIxDwTYgyWFm9eqz3f6_7UmiiLAcXOtFFRSCFb1-f4tsuVF2nuz8iDn06WxUd3f8-Giy3y4d635LfVdT3OuRFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت فرمانده ارشد مزدوران سعودی در تعز
🔹
شورای ریاستی دولت دست نشانده عربستان در عدن اعلام کرد سرلشکر محمد الخولانی، رئیس ستاد نیروهای واکنش سریع در درگیری با ارتش یمن  در تعز به هلاکت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465820" target="_blank">📅 12:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465819">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43992abfa.mp4?token=KyXwTPpNEieIgXUt3_IFBe0qq4fZ6QNQwRL9y_pzl5d_ok_7hdzApNjA3oIrPF8KWUrUX27bjPNNoy2BxKNIlxqIufzYY0Ks_X2TVgjyFRfDTIcncQWv2Ss_PucXxfze4dtt9PXxHuPVndx5a7pVC5Ha-eqSy0mY4if9hqOYPHT7KvRFQ8PlWuxpCP9UiX2QN4h6VuKQ7RkrcgGKeEg6y3kp_uUH8e6lV0vi0QoXVNuMudv8afCdbfLs_fe6sb5BTpo-rxx3LGJ7lRoMCVSj0TRismeMJ0Md_VZ2AZROKXFwkVfAPozNuh79qJkUGUn5oFVlbdZizkIqTGWu9BySzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43992abfa.mp4?token=KyXwTPpNEieIgXUt3_IFBe0qq4fZ6QNQwRL9y_pzl5d_ok_7hdzApNjA3oIrPF8KWUrUX27bjPNNoy2BxKNIlxqIufzYY0Ks_X2TVgjyFRfDTIcncQWv2Ss_PucXxfze4dtt9PXxHuPVndx5a7pVC5Ha-eqSy0mY4if9hqOYPHT7KvRFQ8PlWuxpCP9UiX2QN4h6VuKQ7RkrcgGKeEg6y3kp_uUH8e6lV0vi0QoXVNuMudv8afCdbfLs_fe6sb5BTpo-rxx3LGJ7lRoMCVSj0TRismeMJ0Md_VZ2AZROKXFwkVfAPozNuh79qJkUGUn5oFVlbdZizkIqTGWu9BySzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر تکواندوکار ایران در آستانه کسب مدال
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم مقابل حریفی از هنگ‌کنگ به پیروزی رسید راهی نیمه‌نهایی بازی‌های آسیایی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465819" target="_blank">📅 11:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465818">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcmP6GTOMIsqMo9YkFMc4N3utddzbKJTejApkbnrWZ6gg68lEsJ5tp70WguIAuoQxtQo02vpSwGDBYifNrHco2ustEVQeK0svsosi9BMTqjvovziea_d8lF4sk-SZ4dhbN5Ri4jHxbbKYWrOoFid4vPSS_KRRSsMv0sUoIngLs8lpPqrj9WeoR5DCECmeEH2EZto15ULvQci-lGtJ_KVPYcsIJTBCi8KlM10NZbKKLr1kBhYM9r25lu-X9NLDPOtusp2mGMcCmehC0C9gZo4OcVdefU7eMGygfdFyE34hCbXUzxURu7X9FWvPjADYiplkVLz7pvmi-7fN4OvDfRxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج‌گیری مداوم جنگ پهپادی روسیه و اوکراین
🔹
درگیری‌های پهپادی میان ارتش روسیه و ارتش اوکراین شب گذشته هم در سطح فراگیری ادامه داشت.
🔹
وزارت دفاع روسیه گفته پدافند هوایی ما دیشب ۶۴۶ پهپاد اوکراینی را در چندین منطقه سرنگون کرده است.
🔹
وزارت دفاع اوکراین هم در بیانیه‌ای گفته روسیه در ۲۴ ساعت گذشته ۸۸۹۱ حمله انتحاری با پهپاد در جبهه‌های مختلف علیه اوکراین انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465818" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465817">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۴۵۰ ضمانت الکترونیک در تهران اجرا شد
🔹
دادستان تهران: طرح «ضمانت الکترونیک» که با هدف کاهش بازداشت‌های کوتاه‌و غیرضروری اجرا شده، امکان انجام فرایند ضمانت در حدود ۲ دقیقه را فراهم کرده و تاکنون در ۴۵۰ مورد اجرا شده است.
🔹
پیش‌تر اجرای فرایند ضمانت چند روز طول می‌کشید و در این فاصله شخص در زندان می‌ماند و این بازداشت غیرضروری آسیب‌هایی را برای فرد و خانواده‌اش به همراه داشت.
🔹
با اجرای این طرح، اطلاعات سریعا استعلام و پاسخ داده می‌شود یا وجه لازم تأمین می‌گردد و از بازداشت‌های واقعاً غیرضروری و کوتاه‌مدت جلوگیری می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465817" target="_blank">📅 10:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465816">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnX_0vTFaqFc-YnQkKTDcL9eSHK_HGD8turWZ_CXE6_CE_GSRincK0blPM4qMblfBlnbaYaBptheyDLXc67axI1y329FW8_4Ua7mu8brhbcQxucU4wCvYlRjQawL0pKOc5iJbDosh1x4r3izWfqfMs9SIRCTbpl7gm9D30AWS344k2BxHUUo0axFbgCQf6bir63qvjdk-um0uF9w-zbM1FU7_-NoDCyNIbim3k6FX5i4MtdfUbJDr6aGniCr7AASEmmCNGWnB28BiONCmzOOz_yAkwWPUljWCEBvGmRevbTe0fhyeLN2L33kvw7-sXM7U1eSY4P-rDMqQ_VBE8XJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نخودی هم به یک‌قدمی طلا رسید
🔹
محمد نخودی در نیمه‌نهایی وزن ۸۶ کیلوگرم کشتی آزاد با نتیجه ۳-۰ مقابل شاوایف از قرقیزستان به پیروزی رسید و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465816" target="_blank">📅 10:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465815">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANWTAh0GcON_ALUK5YL7wpmjHI_23HlNzNQvjkHuiUUpCLsr3w34jLkmufYNNTX4_9tNnLhTkaDHgzJYIpBnd1cwcAG35Ut1PH21CLo6ux_AVdFwsyZgoSaVCIYtL2IzRXzR1fUX2nxPHA4YdyVEc6JEnZe-P4zD-Ywy2ebZIhxxMx5QIZ_CNvVXsdcS09QOQu-6rotKpn3akhqS9l7mGRHFM6yij5pslOHYaW43Ni8eFJZN7nbsyGqzbihM0x9hDKIhwv3p8Q3IOD_FC49ALVl4s3GFa_100I6F6xqTCJge8VXWB0fECLSzF52Bvz5I8PvEsCNj48OnNgA3KR3GiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عربستان صلاحیت اداره حرمین شریفین را ندارد
🔹
وزارت امورخارجه یمن: حکومت سعودی که دیدارهای محرمانه با نمایندگان رژیم صهیونیستی برگزار می‌کند، صلاحیت اداره حرمین شریفین را ندارد و امین مقدسات اسلامی نیست.
🔹
رژیم سعودی اماکن اسلامی را به پروژه‌های سرمایه‌گذاری تبدیل کرده که اقدامی توهین‌آمیز نسبت به مقدسات اسلامی است.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465815" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465814">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR9l0hAu0C6AzsMpBY6upU8XFi4vCsMupm2G6KZlq8QNGGd9w5qPqffR-IpEFnFfrC_Qgbg-48lCCtC5aF-ueUbhDFjdT8MD_5DgsP3Gea9KsEZKCah_x4PNmCaRHB5WUPepuyCMP1fzh-6sVetcELmXra1fHdPgaxJW6NMz_bmiuwmjCJcWkk3ZPzEKJmlNy9QfQsL0f9IAMvYpmNj04CnvX57bzQe2hfpY9ZaKwjvf_MaP60dDEnEPQ8fd2aQvsH49CWoLOFEF4m6VEVhdAyBJnNi6nwxo0BBoJ1WoVT434h247vt-mgGGutB0SDouGtaVVzGnr3DPz-EUETWTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله کره‌جنوبی به اوکراین: زلنسکی می‌خواهد بین ما و کره‌شمالی جنگ ایجاد کند
🔹
رئیس‌جمهور کره جنوبی اوکراین را به تلاش برای دامن زدن به جنگ در شبه جزیره کره متهم کرد.
🔹
جائه‌میونگ امروز در ایکس خطاب به دولت اوکراین نوشته: اگر اوکراین از ما عذرخواهی نکند ما اقدامات بیشتری اتخاذ خواهیم کرد.
🔹
رئیس‌جمهور کره‌جنوبی همچنین نسبت به اظهارات زلنسکی درباره احتمال وقوع درگیری نظامی قریب‌الوقوع میان کره‌شمالی و کره‌جنوبی «عمیقاً ابراز تأسف» کرد و گفت چنین اظهاراتی می‌تواند به منزله تشویق به جنگ در شبه‌جزیره کره باشد.
🔸
اختلاف میان ۲ کشور پس از آن شدت گرفت که زلنسکی، در مجمع عمومی سازمان ملل اعلام کرد اوکراین ۲ سرباز کره‌شمالی را که هنگام جنگ در کنار نیروهای روسیه به اسارت درآمده بودند، به کره‌جنوبی منتقل کرده است.
🔹
مسئولان کره‌جنوبی از این اقدام خشمگین شدند چون معتقدند موضوع انتقال سربازان کره‌شمالی قرار بود محرمانه بین کیف و سئول باقی بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465814" target="_blank">📅 10:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4wcrS73h__uRmXqXRu1NZUjCuJU6askZqkM8MpfDpRh-Z3_iFRXxTSzZfONqP7aRZ9LMTkLrTgCzaggZ8kiwF_IEcrLU41pyyQTFNQgFC67Tigmq8eMzlAsKJK_tZAQ_DmcuTm5Uo3DK8jMzZwWDqHGAbf3joA3NfRiKWplLj88ANSlcv2K0nrFPbxfdpuBl22CkUOfEzjfaR1l3_7g9q9BTk5QO2hABN3EI3UwM7pZTn65u2a2v6k5ekpeLxz2Sjd37gQaWm-6h-pr6rFIdiwclJpaGso3HrkgETU4AjZTDqy9ZD8hyh0lhJ73r5Ky1GraJK667oKeO_giLc-nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X71Ro6eadmxu8T4UqY2gJAMykh8AV1j4VHv9_phGvLPr-NOO4Ny97_bCeAB5ytXfeq2Q0E0LrY7cDARfO5uEGBQP-7Ogxq66P7O-4Wx2YAgmH-m4MS1IboFf8-SvfMkB9mbmN6Hgzx1Qt1SMWJ5_0jvv4OaPDs3AWC8JaHqdoF_2mO_d86yu47XLvCQMQX2pFLZNi7cdZAXlw7qcs386iRrSeaJRkPjKEAKvSnykC8Q_r5sJeWEXHHpkhPwoJ5CqbwNiX76141dvMkkO82Xaidfm_xnD8wqoVvGuwji8aI_onhENxrG5GypGHpgMSHkfKBmjqlTsviObwpsPn2C2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br2nnx3AMIxO2sLEMCxJ1B7_Gp4Z49tdkL8y7gTTyZp7BFPK65wDN31r7vswxocWIeG7fXFFzIHOtCv8Vc5A_dPpClPquoXT-fhhLHwVNx5QfITDaQQHYM0sPDiUU1JIBjhpx7_-3A3rFR_Y78oQmweulD9bbMEOsazQl-Fvdn8VZBirl63oSsR6ZUse4nn0q-swv8CpIleT11eO3p3uLqwLA2q1arEPPwA91d8cuS2wDQ7l_RB3PQf6bgOPErvgboJ-8MYRX3N_bWdSdRVTULtHUn95uQ32DRyzAEqtQyJ7Mmd_XpP6gGDUsgCwBd8RgyRTiwwkuOas68FbvK6Jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWExiAqwHRRLSdUbAKu8Pe9wBvtvCk6BvJS9bgN0UN26Y2HUs-XiLpV1ZW_QigGnELUtGW2V-MO7qmymJV5AjtC-OjU5CDErA8-lYlpFxR6poSh5pnZ12Gz66hxHMbNOCHl_Hy83kb1ycbQ0L7R5zeZey2CxaGzjpwqyRQB3ng3bVw35dJiP2NCoq0lvEuTpB8AHLbVZ8XZWHB8aO1lLNQJKL_FOu7rxL9dA-zPY5NdoGywxri_7OeCRFXL3F-LAOCcc2UZm9bS6agfcs6bmdwA-CMfKA_-U_j5RK4QTEDFYehW8Poczmmeam7tm38wUPLkXOImTJsfCy7e759jyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlouhPeAMbHhT8McKnc9hz2nOTMYPO8F8ESC3D4Q9OQV4RR-rnEQs6dHuLoTTPDbjQ5XxqbAoSh-gV0Zr5R5Y6Pe_BNxq59W1AZI4fINkZKZP9isG8UJmSObWSer9dGqN2UKE-9zh508GVWCS-sGzJylToAEoBgKJiBQs_oQdeVqQAAZQ5Hg5uZfNiLSN4vUECzrQDohQgironmCQVHJxMydkACY92k2cJqYnWbZqiVedH5A-WbNW2CG_6oLKRakNirCApdT_wMBIl2keE1sIWT2-CaIXjCTh22i3SZZchiT8RldiBIngtrvAIu-ZsyvH77CINm5I1iqAY9U_3dPsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پل سنگی «هوره» یادگار عصر صفوی بر روی زاینده‌رود
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465809" target="_blank">📅 09:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=VHX7IEB4ILIXw2GB2N3uuKYnAAt92vR2vlXmzxIHaNQGrTKNqWCh6Ks52N8stsoDZKqg4vXWybllT62eqfxdSogsrUvYfpig5DtJpNE09fQWZmR0PFlvVrM_jijU-JzPRA56tACIZUSBXHULDeoo8vcMwQSVF3mlkv443Ks3_KjjGK3CMEupEAgnbHKzv49keJ4_oHBIItSoQH_D-mTFxDdL8-QUcrqumesnQZjUEVDTuPlbWbij-kDeOqO0bj6eurMPgmXqFEw2Nd4Rxsc-THenO-XiOwMhdnyd9Sx-g1_bxuOzshanLcDt1s1rhMXrtv5Ff4W5wIXa-jQNvscNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=VHX7IEB4ILIXw2GB2N3uuKYnAAt92vR2vlXmzxIHaNQGrTKNqWCh6Ks52N8stsoDZKqg4vXWybllT62eqfxdSogsrUvYfpig5DtJpNE09fQWZmR0PFlvVrM_jijU-JzPRA56tACIZUSBXHULDeoo8vcMwQSVF3mlkv443Ks3_KjjGK3CMEupEAgnbHKzv49keJ4_oHBIItSoQH_D-mTFxDdL8-QUcrqumesnQZjUEVDTuPlbWbij-kDeOqO0bj6eurMPgmXqFEw2Nd4Rxsc-THenO-XiOwMhdnyd9Sx-g1_bxuOzshanLcDt1s1rhMXrtv5Ff4W5wIXa-jQNvscNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی با انتشار این ویدیو از انفجار در فرودگاه نظامی تنفتناز در حومه شهر ادلب سوریه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465808" target="_blank">📅 09:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d97cbf38a.mp4?token=JxkKpfKTW4zs8HCXVePuFz5XUtO07Zyr33HACh2H_0B9qXBiSgbyFq-WA36YKPNs2A6TistiaucHcNoyxrKhazVXx9_88ceV6MvYWaUd73Nkd8JHotpJE8_hBqVg2uqkuVBPHuvFqJ8TKwiLlsnI7zd43VTOLPxcOm5SMrFt_htMwnkEHhUVIU6ud-MnVx3fN3rvZ_w8-zCxKkfxiV5fhtwi0uIqvkznGRnbeRJiwYpJPd5HFxEHNsFvYTPZSTT6I-01hMBexP9bB5GFWZ29m-9j9NGmfHUGDOtxnyTmgje-bV9gYvwyTWGF_247UBgRUEKqAAa6Vv5gew5C-tVzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d97cbf38a.mp4?token=JxkKpfKTW4zs8HCXVePuFz5XUtO07Zyr33HACh2H_0B9qXBiSgbyFq-WA36YKPNs2A6TistiaucHcNoyxrKhazVXx9_88ceV6MvYWaUd73Nkd8JHotpJE8_hBqVg2uqkuVBPHuvFqJ8TKwiLlsnI7zd43VTOLPxcOm5SMrFt_htMwnkEHhUVIU6ud-MnVx3fN3rvZ_w8-zCxKkfxiV5fhtwi0uIqvkznGRnbeRJiwYpJPd5HFxEHNsFvYTPZSTT6I-01hMBexP9bB5GFWZ29m-9j9NGmfHUGDOtxnyTmgje-bV9gYvwyTWGF_247UBgRUEKqAAa6Vv5gew5C-tVzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی پدر برای دختر شهیدش
🔹
پدر شهیده فریده مختاری، معلم شهید مدرسه شجره طیبه میناب هر روز با کوهی از دلتنگی بر مزار دخترش می‌آید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/465807" target="_blank">📅 08:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d261efb5.mp4?token=QNN0fKe0JYWur1UME6-ymux0bYicHT5M05waMMif9foV2GD1fOd82NhGVgGG93hkbSRp44agNQlNJK6WOHUOVhsnxf_NX3mfaUwcZhzLZabLhcdH1AmF0XxLDp6uirAoQllHhAdUX7EFjpS67-x2CCsmXAu4UhCZjUiapZrIiP50HTuV27AhDfGlh_hYmPj-Lpy2W4fmYINADhwx9yPLyd9CvHQG0JkuS_hKWgv789BTgWHObpVO4lo_Ul5b65PVRY8-9xJlIWt5_jG15JItDmvw5FAHQnrb5uYhSAnuyY9saLxwb4_0hEp7z0hp9Lb_u8ls4n3ZdTdABsAEZiDgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d261efb5.mp4?token=QNN0fKe0JYWur1UME6-ymux0bYicHT5M05waMMif9foV2GD1fOd82NhGVgGG93hkbSRp44agNQlNJK6WOHUOVhsnxf_NX3mfaUwcZhzLZabLhcdH1AmF0XxLDp6uirAoQllHhAdUX7EFjpS67-x2CCsmXAu4UhCZjUiapZrIiP50HTuV27AhDfGlh_hYmPj-Lpy2W4fmYINADhwx9yPLyd9CvHQG0JkuS_hKWgv789BTgWHObpVO4lo_Ul5b65PVRY8-9xJlIWt5_jG15JItDmvw5FAHQnrb5uYhSAnuyY9saLxwb4_0hEp7z0hp9Lb_u8ls4n3ZdTdABsAEZiDgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع در ثانیه‌های آخر به خودش آمد و فینالیست شد
🔹
در نیمه نهایی سنگین‌وزن کشتی آزاد ناگویا، امیرحسین زارع که تا ۱۵ ثانیه به پایان بازی از حریف خود عقب بود با زیرگیری تماشایی در لحظات پایانی ورق مبارزه را برگرداند و فینالیست شد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465806" target="_blank">📅 08:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7051dc5c.mp4?token=AkyueV5lfe3-AtL-2pSfVOh7YVtjQzPLJSldxqrfc2wEcKM44XiVVYGVW4HK0jG1yGrjhYlPXws_5BXnKzyY8ZHZP8QRAvyDewdUQWb6awccxJerUGWKZvA7ifCEZpFfsU8nYVl8u0_X4OjP74dVeaBKudE4SSN13213tc2Lq7wPkhhRuNH824E9sn9fXFP7IuhwQEQDYGHZBaCLXyKgYXonRDuk-zv0DKpnNNdtvHc-J4PGWz6uYngz261XqfUFAMBiJFVwD5_j9Ry3Oo-A3iD7pBMlKKi5sAHwVwDvUhorbOvvKbvDn42N1--CF-LmEXbmkFCWVcjs2viehS2HLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7051dc5c.mp4?token=AkyueV5lfe3-AtL-2pSfVOh7YVtjQzPLJSldxqrfc2wEcKM44XiVVYGVW4HK0jG1yGrjhYlPXws_5BXnKzyY8ZHZP8QRAvyDewdUQWb6awccxJerUGWKZvA7ifCEZpFfsU8nYVl8u0_X4OjP74dVeaBKudE4SSN13213tc2Lq7wPkhhRuNH824E9sn9fXFP7IuhwQEQDYGHZBaCLXyKgYXonRDuk-zv0DKpnNNdtvHc-J4PGWz6uYngz261XqfUFAMBiJFVwD5_j9Ry3Oo-A3iD7pBMlKKi5sAHwVwDvUhorbOvvKbvDn42N1--CF-LmEXbmkFCWVcjs2viehS2HLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ زارع به نیمه‌نهایی رسید
🔹
امیرحسین زارع در دومین دیدار خود با نتیجهٔ ۱۱ بر صفر ساپاروف از ترکمنستان را مغلوب کرد به نیمه‌نهایی راه یافت.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465805" target="_blank">📅 08:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شکست چوپان مقابل حریف ازبک
🔹
امیرعباس چوپان، در یک‌چهارم وزن ۹۰- کیلوگرم جودو مقابل حریف ازبکستانی ایپون شد و شکست خورد.
🔸
چوپان باید برای رسیدن به مدال برنز در شانس مجدد رقابت‌هایش را ادامه دهد. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465804" target="_blank">📅 08:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ابراهیم‌زاده هم پرقدرت شروع کرد
🔹
عباس ابراهیم‌زاده پس از استراحت در دور نخست، در دور دوم وزن ۶۵ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر ۰ مقابل حریف سریلانکایی به پیروزی رسید و راهی یک‌چهارم شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465803" target="_blank">📅 08:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هشدار هواشناسی برای استان‌های شمالی کشور؛ مسافران مراقب باشند
🔸
هواشناسی گلستان: از ظهر امروز، وزش باد نسبتاً شدید تا شدید، رگبار و رعدوبرق و افزایش غلظت گردوخاک در برخی نقاط استان پیش‌بینی می‌شود.
🔹
هواشناسی مازندران: رگبار باران، وزش باد، رعدوبرق و صاعقه…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465802" target="_blank">📅 07:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هشدار هواشناسی برای استان‌های شمالی کشور؛ مسافران مراقب باشند
🔸
هواشناسی گلستان: از ظهر امروز، وزش باد نسبتاً شدید تا شدید، رگبار و رعدوبرق و افزایش غلظت گردوخاک در برخی نقاط استان پیش‌بینی می‌شود.
🔹
هواشناسی مازندران: رگبار باران، وزش باد، رعدوبرق و صاعقه از عصر جمعه ۱۰ مهر تا عصر شنبه ۱۱ مهر در نیمهٔ‌غربی استان پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465801" target="_blank">📅 07:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465800" target="_blank">📅 07:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  نخودی هم طوفانی شروع کرد
🔹
محمد نخودی در دور نخست وزن ۸۶ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر صفر مقابل ربیع ابوعریاله از فلسطین به پیروزی رسید و راهی مرحلهٔ بعد شد.  @Sportfars</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465799" target="_blank">📅 07:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465798">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V24DHBRqqarDUyS6ZSlRiwzlRUEm_hn4nejf8mh5IW6hzZC-upExwWaDICxW4s1TDFW-IElgNIoI-JxTU328zYwh42zZ0XdeaLE84Ks97Jq6EDNeArmjJvn83TT8wt2OL_3ZDou55utfDXV40HHjRe35m3_PC5dncPBa7JO2uY1hs50TunUbbQVNVH1FCDy-ZdWKxJKfhVGd3cqlfAECCiuBBEOPssLwReirtDqMGksXHLC8TDj5g5VwTfGPJC1bAorgcFq83dIdrRM7wGIKoRWxEkli91WoAqWRIdryjU4yY7LfiCcgiD-7-ph7cn2GZWA0tu5GLUXTyl6-HxTs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشکار چینی با دندان به جان حریف افتاد
🔹
در اتفاقی عجیب در رقابت‌های جودوی بازی‌های آسیایی ناگویا، جودوکار چینی در مرحلهٔ یک‌چهارم نهایی وزن ۷۰ کیلوگرم، بازوی حریف ژاپنی را بیش از ۲۰ ثانیه گاز گرفت و با تصمیم داوران بازنده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465798" target="_blank">📅 07:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465797">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdHdie6W1bnkUl-PPlj0JreYvbPzODKxn9L1QfsO3v0ZJ1B9ToTchq1PzlKe9ZkUkvrRBcEW8Sb3YTsk52L3K9gsZCQq_deNtiGZ_oJtKM1iMCTeRTyFiKMw_MIGfuXt_8naxaiLpiApdLnP6jlzjTvKvMu0XJAmxBElGKEzZhzYMeM5XkoqO_D9GiQpfLd965pQk5pl_NpnJISabeD1UnK4UYKndngQvfGuEBcjnqqSJ9oDgNsXhbVveLpO_o51oFfcJj7gjx2tJ5ow9Su8MgpSsodXTDEBC5khInnaJZ6A9pE9qnJftY6smStIhhBFTbTU04K5nhXtOo-ffcWn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست چوپان مقابل حریف ازبک
🔹
امیرعباس چوپان، در یک‌چهارم وزن ۹۰- کیلوگرم جودو مقابل حریف ازبکستانی ایپون شد و شکست خورد.
🔸
چوپان باید برای رسیدن به مدال برنز در شانس مجدد رقابت‌هایش را ادامه دهد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465797" target="_blank">📅 06:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465796">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">برد مقتدرانهٔ زارع مقابل حریف ژاپنی
🔹
امیرحسین زارع با پیروزی آسان ۱۰ بر صفر برابر حریف ژاپنی راهی مرحلهٔ یک چهارم نهایی شد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465796" target="_blank">📅 06:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465795">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ابراهیم‌زاده هم پرقدرت شروع کرد
🔹
عباس ابراهیم‌زاده پس از استراحت در دور نخست، در دور دوم وزن ۶۵ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر ۰ مقابل حریف سریلانکایی به پیروزی رسید و راهی یک‌چهارم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465795" target="_blank">📅 06:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شروع دختر جودوکار ایران با برد
🔹
مریم بربط در وزن ۷۸- کیلوگرم جودو با امتیاز ایپون مقابل «خوسلن اوتگون‌بایار» پیروز شد و به مرحلهٔ یک‌چهارم نهایی رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465793" target="_blank">📅 06:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c5f635a2.mp4?token=pGfLC7YLe0o5uTazFuAIEh2n2hBCKkbMhufq8_nkiGXQLe7_rVjM5EdfURt5iXA8Q0Zq4uDGn4-YmtiIS-_khlSI337JsqsBVn9hfM-XcMYbblZiTO4CGo9fMwzRM3U9C6gX25onggAbyljN6iEtGg5VLmW6dfDB8HA4nF3QP-FMi8o9HYgqsx3sArUAzaFhEJuNOFqRTpg5aUPGv_U8JBV9tbjY97WWALHlSYNrNYKgokl91SLrizW3DT8j7gbMFost_IR0aeoP3kPJcgNbPhWdvrHD483rKcJf0o0VoArJIZFkmyckOlPBWKS1GpbleIki_iCkyZs2g3AGMrGQog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c5f635a2.mp4?token=pGfLC7YLe0o5uTazFuAIEh2n2hBCKkbMhufq8_nkiGXQLe7_rVjM5EdfURt5iXA8Q0Zq4uDGn4-YmtiIS-_khlSI337JsqsBVn9hfM-XcMYbblZiTO4CGo9fMwzRM3U9C6gX25onggAbyljN6iEtGg5VLmW6dfDB8HA4nF3QP-FMi8o9HYgqsx3sArUAzaFhEJuNOFqRTpg5aUPGv_U8JBV9tbjY97WWALHlSYNrNYKgokl91SLrizW3DT8j7gbMFost_IR0aeoP3kPJcgNbPhWdvrHD483rKcJf0o0VoArJIZFkmyckOlPBWKS1GpbleIki_iCkyZs2g3AGMrGQog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکواندوکار مجازی ایران پیروز شد
🔹
رقابت‌های «تکواندوی مجازی» برای اولین‌بار در تاریخ بازی‌های آسیایی، برگزار می شود و امیرسینا بختیاری به عنوان اولین نمایندهٔ ایران در این بخش  مقابل حریف ازبکستانی به پیروزی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465792" target="_blank">📅 06:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
نخودی هم طوفانی شروع کرد
🔹
محمد نخودی در دور نخست وزن ۸۶ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر صفر مقابل ربیع ابوعریاله از فلسطین به پیروزی رسید و راهی مرحلهٔ بعد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465791" target="_blank">📅 06:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برد مقتدرانهٔ زارع مقابل حریف ژاپنی
🔹
امیرحسین زارع با پیروزی آسان ۱۰ بر صفر برابر حریف ژاپنی راهی مرحلهٔ یک چهارم نهایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465790" target="_blank">📅 05:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صعود نمایندهٔ ایران به جمع هشت جوجیتسوکار برتر ناگویا
🔹
پوریا طاهرخانی در یک‌هشتم وزن ۹۴- کیلوگرم استایل نوازا به مصاف جوجیتسوکار ۲۱ سالهٔ قزاقستانی رفت و با نتیجهٔ ۲ بر صفر به پبروزی رسید تا به مرحلهٔ یک چهارم نهایی راه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465789" target="_blank">📅 05:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تکواندوکار مجازی ایران پیروز شد
🔹
رقابت‌های «تکواندوی مجازی» برای اولین‌بار در تاریخ بازی‌های آسیایی، برگزار می شود و امیرسینا بختیاری به عنوان اولین نمایندهٔ ایران در این بخش  مقابل حریف ازبکستانی به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465788" target="_blank">📅 05:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حملهٔ موشکی و پهپادی به مواضع نیروهای سعودی در جنوب یمن
🔹
منابع محلی از حملهٔ موشکی و پهپادی به مواضعی در شهرستان البُرَیقه در جنوب یمن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465786" target="_blank">📅 04:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
عملیات انتحاری در مسجدالحرام صحت ندارد
🔹
برخی منابع خبری خارجی ویدئویی قدیمی را با این ادعا منتشر می‌کنند که مربوط به خنثی‌سازی یک عملیات بمب‌گذاری انتحاری در مسجدالحرام است؛ اما ظاهراً این ویدئو مربوط به فوریه ۲۰۱۷ است.
🔹
در این ویدئو، مردی سعودی که از مشکلات روانی رنج می‌برد، نزدیکی کعبه روی لباس‌های خود بنزین ریخته و قصد داشته خودش را به آتش بکشد.
🔹
در آن زمان نیروهای ویژه امنیت مسجدالحرام بلافاصله وارد عمل شدند و او را مهار کردند و مانع روشن کردن آتش شدند. این حادثه هیچ خسارت یا مصدومی بر جای نگذاشت.
🔹
بنابراین، ویدئوی منتشرشده مربوط به یک حادثه قدیمی است که اکنون با روایتی جعلی دربارهٔ حضور یک «انتحاری» و «کمربند انفجاری» دوباره در فضای مجازی منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465785" target="_blank">📅 03:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT7SpRKX1NZGD0lgc4a_IXxZVfe9I0WjlZMt6t8ZrT8SYeCbglkjdcnqkOWhrHA5PBsFBFi4OQXzx4iocq7Tsq9gG5YaZbpeN4FDOPkCFdeOB0Co3kb_etlOc5a71WFlDcRmiSbhDcvzjBj_UbeNLwPekM5LKxjJBQBD5LSZLRsIL6_lJatpMT6kNBZKyEqD5JHA87W808xYAYPdlUwslm8ifcnFDDZqfJghr9CKnLhE6EKhJm67t8ObnLATUYlyCTFCB7Lpwllc2wEFEEOiNs91WEzKwCpwGSh8I-l91U_w4PGgLL4bshqVmjx75xLUDSK2OVs4w-gJHEzzMxTA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویروس‌ها پاییز امسال حسابی جولان می‌دهند
🔹
با آغاز زودتر فصل بیماری‌های تنفسی، فعالیت ویروس‌هایی مانند آنفلوآنزا و کرونا از شهریورماه افزایش یافته و وزارت بهداشت از عبور شیوع کرونا از مرز هشدار خبر داده است.
🔹
با توجه به شباهت علائم بیماری‌های تنفسی، نمی‌توان تب، سرفه، بدن‌درد یا گلودرد را صرفاً به کرونا یا آنفلوآنزا نسبت داد؛ اما واکسیناسیون آنفلوآنزا برای گروه‌های پرخطر، از جمله سالمندان، کودکان زیر ۵ سال و بیماران زمینه‌ای توصیه می‌شود.
🔹
ماسک در محیط‌های شلوغ و بسته، شست‌وشوی مرتب دست‌ها، کاهش تماس با افراد بیمار و رعایت فاصله می‌تواند احتمال انتقال ویروس‌ها را کاهش دهد. افزایش بیماری‌های تنفسی لزوماً به معنای ظهور بیماری ناشناخته نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465784" target="_blank">📅 03:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465783">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c587ec776f.mp4?token=AxoMc5q1i76Wv5cklRh3AkKiIMfUhtPNOhUiNwP1rSynfyB91iECl-qoA3voMS6FLbT0881uPybuplNZQ2SJ8mdI9YQ6WX2ATfRgNfVqZchUBZDxhkPSilcm5yioCm8w8q8MYGZ6ewT5gdImjTgno-XNUHhUwthcvZSKOX-fBxK2xfsHHOd6ovul4Fd609fTLFd8C3MQzT8a1OBcWcfeFoj3eGeVPXRV0yl1yaTGW6gcBC7t8SzLUzEEp9pNc5-gO1baZZ0W5I7uSjYzt_bh1lSbNUVBsEWugP87Xy-Al48s031ww6VD6ROr7dcCA079UPuCl2vXfpaJbouM59oKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c587ec776f.mp4?token=AxoMc5q1i76Wv5cklRh3AkKiIMfUhtPNOhUiNwP1rSynfyB91iECl-qoA3voMS6FLbT0881uPybuplNZQ2SJ8mdI9YQ6WX2ATfRgNfVqZchUBZDxhkPSilcm5yioCm8w8q8MYGZ6ewT5gdImjTgno-XNUHhUwthcvZSKOX-fBxK2xfsHHOd6ovul4Fd609fTLFd8C3MQzT8a1OBcWcfeFoj3eGeVPXRV0yl1yaTGW6gcBC7t8SzLUzEEp9pNc5-gO1baZZ0W5I7uSjYzt_bh1lSbNUVBsEWugP87Xy-Al48s031ww6VD6ROr7dcCA079UPuCl2vXfpaJbouM59oKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): واجب عبادت خداست و واجب‌تر ترک گناه
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465783" target="_blank">📅 02:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQoP4i799DZRE8z0JgtyX6W3OUAlwtg-banG0bWCK4HvkPHPFhBeaRApBu2j6CABnxNeR2yBrs9fjgm9EaX7JJYYgpP5q3wXmLCSJ17KD6gy67_SlATRFE7C_9ixtIm3kJWh32vWzJ9n_mkF2KSgeGVHDMESTdR0EAlueiJDwFMXjIblu5NHwwrjETR2aQy_w9GzOJ4a-sxrO0kSqM-SJ1JiMY4sKnf-NNc7KmBiV740adpfR5TqtQHc2mcVbc9WMhZoxl_1D2a8DsNdLvaBQlOVhffL7EWXRO3ftDGlVRo98QsCYO841uTetv6Z-ipwZPNWhf-q9CQuaUB8wQQHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف برلیان‌های قاچاق ۱۰۰ میلیاردی در فرودگاه امام
🔹
فرماندهی پلیس فرودگاه امام خمینی(ره): مأموران گیت بازرسی به محتویات چمدان یکی از مسافران خروجی به مقصد استانبول مشکوک شدند.
🔹
با حضور مأموران و بازرسی دقیق بار، ۹۷ گرم سنگ برلیان که در جدارهٔ چمدان جاسازی شده بود، کشف و ضبط شد.
🔹
کارشناسان ارزش این سنگ‌ها را بیش از ۱۰۰ میلیارد ریال برآورد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465782" target="_blank">📅 02:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSGtKEtSnYNpIJYygg3bj6sUONPFjRRvqTogLjWm0fWSIjiIxk9hbJXTr8cs61_wCrTD9R6yDSNLQnbbpx0dk78SKpRK8PUvzl7AoDX1BkHg2sPhIF3Kfm1jK8bqGQd2yAHyORMOHI6CA6C-lEsF7y0y_06ehki66YTUvfBkd1qa_vrCwYSKPf9ij0geNwqxU-zk6cC9mnr5YaWlc4Ph2X0F4PQZAHDlOXbjIE6vw7AUgrKvHOjb2Ox6vu2cpb52yBIj9I1g9ypeDC-vhnBMzDXuv5aiJ0DBiWO7j2lNrfHCqs1_gabWA8VELV4WPQ6BgeYNCQDe0vG6YcabrgSl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: رهبر شهید فرمودند انتقام خون حاج‌قاسم اخراج آمریکا از منطقه است؛ امروز شاهد گام‌هایی در این مسیر هستیم
🔹
مشاور عالی فرماندهٔ کل سپاه: آمریکا سال‌ها در این کشور حضور داشت و هزینه‌های سنگینی متحمل شد، اما در نهایت مجبور به خروج شد و این تحولات نشان داد که قدرت آمریکا آن‌گونه که تبلیغ می‌شود، نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465781" target="_blank">📅 02:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2WkbqKhM_F1POq9zqMpCTqCKfqu10Nft8kv6MJIz5dBUj4wVA3MY-4sEgV43i39xF5-y5pHvIYgkh1noJ2Yb5lfVaPG0Xi1vMJjXAg4IHF6_eCVychaOjaXsZYk3M707mi56_v-RuMfXcmierGW4lgpjkJKrBfIY0QwIHhtE-M6S6v2G5BuL6vr_wW9bDOUtzbRkW4iaKmO_qg6ufB2659Sr4lDV0F4BCIZRU1eOhgm0mMA_Tfu-OsTcpwTQesj5GD1nVcUUush-W9_4eOLhHIh5vfooa4aVrqW64NIGO-zBugOdQyxJ6uz2_JFJU42Cj-s5IVMh77qEVC5BMYeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ترامپ: ایران آمادهٔ تسلیم شدن است
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد: ایران آمادهٔ تسلیم شدن است؛ ما الان می‌توانیم به راحتی پیروز شویم.
🔹
من معتقدم بلافاصله پس از انتخابات پیروز خواهیم شد، اما شاید حتی پیش از انتخابات.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465780" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مخالفت حدود ۷۰ درصد آمریکایی‌ها با جنگ علیه ایران
🔹
نتایج یک نظرسنجی جدید نشان می‌دهد نزدیک به ۷۰ درصد آمریکایی‌ها معتقدند جنگ آمریکا و اسرائیل علیه ایران ارزش جنگیدن نداشته است.
🔹
بر اساس این نظرسنجی که روز پنجشنبه از سوی مرکز تحقیقات امور عمومی آسوشیتدپرس-نورک (AP-NORC) منتشر شد، ۷۱ درصد از بزرگسالان آمریکایی از نحوهٔ مدیریت ترامپ در قبال ایران ناراضی هستند و ۶۹ درصد نیز معتقدند جنگ در ایران ارزش جنگیدن نداشته است.
🔹
این نظرسنجی که با مشارکت بیش از ۲ هزار بزرگسال آمریکایی انجام شده، همچنین نشان می‌دهد آمریکایی‌ها از عملکرد دونالد ترامپ، رئیس‌جمهور آمریکا، در زمینه اقتصاد و افزایش قیمت‌ها به‌شدت ناراضی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465779" target="_blank">📅 01:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFSO_0PI0PxncNEaPEju4H8LThrvLgPgdwFLkNfLZJ9aFwxhWtKWTLQKpY6iI11tUoTdW0hb27xwQCGxL73Vt6yBpeHlq0EAyO-t_VeNunqmLlPSC6kji3XHwWzl9SrkgOYk_HnnCiCwRc0SQ7n7U0BmDixyT53uEUpuSwZH8BgKcfp3TXOr4HY-V8kSlhJm_6S5L9KWN-p3Gp02Hxq053JW0POm3OQxGeexvTO60MU6Umny8HOJ9XKePJnLFR3jhkKZg3tcO1jRWbpiMaydFQKwO2yUkgxdy9SE0Ventz8f0eNiGVRPQ8HYGeFUei_du0flvkdSCFpHE0ZiPsP4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری وال‌استریت از دروغ بزرگ در مورد بازبودن تنگهٔ هرمز
🔹
کیم فوستیر، رئیس تحقیقات نفت‌وگاز اروپا در HSBC گفت اگر ادعای عبور زیاد نفت از تنگهٔ هرمز درست باشد، قیمت نفت باید ۷۰ دلار می‌بود و نه اینکه از ۱۰۰ دلار بگذرد.
🔸
وال‌استریت ژورنال هم در ادامه نوشت: به زبان ساده، یک جای کار می‌لنگد. بازار چیزی متفاوت از آمارهای ظاهراً چشمگیر صادرات می‌گوید. اگر واقعاً این حجم عظیم نفت به بازار برگشته و عرضه به وضعیت عادی نزدیک شده، چرا قیمت‌ها هنوز این‌قدر بالاست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465778" target="_blank">📅 01:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc659a405.mp4?token=ocB6-kRrEck6uTh-KVrhJHVZ237JO3DNQ-SK1L-Bdj1rSBSMspDbp5yDaD_A037dfEcP4GS0UHHnCNEHBTIoOZRClIMW9uxe-id3hH-ySLpRu8ebgpzRBnK8sHon1OtqdnFA4f_YaMAplXi91ghPoFikIWvmtPt3csuYYSVne4aJy6nig-WQh51XLZxZ6I4H6UOYciI5wK_iqcR43HUhNqaf3HlLkPSNyk7ZAXMlzy2T_xPBLj4O7mzEn0plktTxqGKKaTxRDmBQCU1UIkJzEr10diml9YfBWVPHor6GT8sFQONfksZhAdyG6j3_FqUGJhFEwF1tffTwMM8WXu_CGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc659a405.mp4?token=ocB6-kRrEck6uTh-KVrhJHVZ237JO3DNQ-SK1L-Bdj1rSBSMspDbp5yDaD_A037dfEcP4GS0UHHnCNEHBTIoOZRClIMW9uxe-id3hH-ySLpRu8ebgpzRBnK8sHon1OtqdnFA4f_YaMAplXi91ghPoFikIWvmtPt3csuYYSVne4aJy6nig-WQh51XLZxZ6I4H6UOYciI5wK_iqcR43HUhNqaf3HlLkPSNyk7ZAXMlzy2T_xPBLj4O7mzEn0plktTxqGKKaTxRDmBQCU1UIkJzEr10diml9YfBWVPHor6GT8sFQONfksZhAdyG6j3_FqUGJhFEwF1tffTwMM8WXu_CGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظلوم‌نمایی سعودی‌ها با شهر پیامبر
🔸
رسانه‌های عربستان درحالی از حملهٔ یمن به مدینه خبر داده‌ند که نیروگاه برق هدف قرار داده شده، ۱۰۰ کیلومتر با مدینه فاصله دارد.
🔹
پیش‌تر یمن با حمله به خط لولهٔ نفت عربستان، صادرات نفت این کشور در ساحل دریای سرخ را مختل کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465777" target="_blank">📅 01:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6414482cf.mp4?token=YFcHDRhlyuL98phYp1Na8vMOIj1LJwkHywqGzRibzBcVzWnNQU_vGf6_j9XXq93cf5XpImiLpGgVJMQGLjAOgMa27dYwMebJ5TxR2-drh0lu2bw3U84A8KFs3SyGkqwJ453YrV0zkPTUjRUsrr11M6EIgSutt3JdoAaZ_bGb93UY4mhPCQa6RMbUHo6jz0l9hRiaTxgtXF89KN4dznlBQRuqbo11eT8Kr6qQIJO9_N_jy2r9OBKI_0DLAD-B5brk6hJwix4H0pn0Yxvgd-paX8MGrDWmqnVRZfAA5haZGbbuU_ZBESPWyv5VL1YPLcVBKz_NA_cXwqR4jxjdWxE8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6414482cf.mp4?token=YFcHDRhlyuL98phYp1Na8vMOIj1LJwkHywqGzRibzBcVzWnNQU_vGf6_j9XXq93cf5XpImiLpGgVJMQGLjAOgMa27dYwMebJ5TxR2-drh0lu2bw3U84A8KFs3SyGkqwJ453YrV0zkPTUjRUsrr11M6EIgSutt3JdoAaZ_bGb93UY4mhPCQa6RMbUHo6jz0l9hRiaTxgtXF89KN4dznlBQRuqbo11eT8Kr6qQIJO9_N_jy2r9OBKI_0DLAD-B5brk6hJwix4H0pn0Yxvgd-paX8MGrDWmqnVRZfAA5haZGbbuU_ZBESPWyv5VL1YPLcVBKz_NA_cXwqR4jxjdWxE8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زارع: سلام نظامی به پرچم ایران از قبل تمرین کرده بودم
🎙
امیرحسین زارع:
🔹
سلام نظامی به پرچم ایران را از قبل و حدود دو ماه پیش از مسابقات، زمانی که جنگ به کشورمان تحمیل شده بود، با آقای درستکار، تمرین کرده بودیم.
🔹
در سالن تمرین یک پرچم شهید بود و با سرمربی آن حرکت را تمرین کرده بودیم که ان‌شاءالله اگر به لطف خدا طلا گرفتم، احترام نظامی به پرچم بگذارم. یک خوشحالی دیگر هم انجام دادم که تاجگذاری بود و آن را در سال‌های قبل هم انجام می‌دادم.
🔗
صحبت‌های امیرحسین زارع را در
فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465776" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌ سردار قاآنی خطاب به عربستان: جنگ با یمن را تمام کنید
🔹
شما یمنی‌ها را خوب می‌شناسید و ما نیز آن‌ها را خوب می‌شناسیم. به نفع خود شماست که محاصره را تمام کنید و جنگ با برادران مسلمان یمنی خود را ادامه ندهید. توصیه ما به شما همین است.
🔹
فردا چه پاسخی در برابر…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465775" target="_blank">📅 00:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌ سردار قاآنی: جمهوری اسلامی حتی در اوج شرایط جنگی کنار ملت‌های تحت ظلم ایستاده است
🔹
جمهوری اسلامی در اوج شرایط جنگی نیز دوستان خود و کسانی را که مورد ظلم آمریکای جنایتکار و رژیم صهیونیستی قرار گرفته‌اند، رها نکرده است و پس از این نیز در کنار آنان خواهد ایستاد.…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/465774" target="_blank">📅 00:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465773">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ سردار قاآنی: حزب‌الله، لبنان را به قطب افتخار مقاومت تبدیل کرد
🔹
لبنان زمانی حیاط خلوت بسیاری بود، اما از زمانی که حزب‌الله قهرمان تأسیس شد و پا به عرصهٔ مقابله با اشغالگری و مبارزه با رژیم صهیونیستی گذاشت، این کشور روزبه‌روز اعتلای بیشتری پیدا کرد و امروز…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465773" target="_blank">📅 00:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465772">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌ سردار قاآنی: آمریکا با همه امکانات از عراق اخراج شد و از ایران هم شکست خورد
🔹
آمریکای جنایتکار با ذلت دم خود را روی کولش گذاشت و از عراق اخراج شد. مردم عراق امروز به برکت مقاومت آن ملت و قهرمانان جبههٔ مقاومت، اخراج آمریکا را جشن گرفته‌اند.
🔹
آمریکا موظف…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465772" target="_blank">📅 00:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465771">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سردار قاآنی: با حضور هرشب مردم در میدان‌ها، شاهد دوره‌ای جدید از مقاومت هستیم
🔹
فرماندهٔ نیروی قدس سپاه: آمریکای جنایتکار با این فرضیه وارد میدان شد که ظرف چندروز ایران اسلامی را به تسلیم بکشاند، اما ببینید با چه وضعیت خفت‌باری مواجه شده است.
🔹
این مواجهه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465771" target="_blank">📅 00:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۴</div>
</div>
<a href="https://t.me/farsna/465769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۳ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465769" target="_blank">📅 00:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTWaTddu2Y9jYr0YUWlDv0ZiAdYAQBEXb3dzMU7-3N55BC_yj6OYxkEnccBrOmM1yINtdc9_syrHbklV8KzQ-uOIEQWPApaiPJAqWLDRjWWmrBzjRWMNaGm06WJYgMHSa4WIfWfx-sggpq3OSKoS2QsNMsGzlWYBLqVkxnFVJik5hIbwxsQ878AufVo7-wbx47QvN52Ma7pR7vrqLh98FSexR60-S8Xnc-9iBn9KuGjDWAxc3-r2oByM8JK9arTK4YobLb8J1qGpxiqiBrEou9a_68SIvy2g-6-Fj8dZlfx9p1N2m8gnTt9tI-YyqA8GuZ9Mn7W2rvgecme83tUkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است از اروپایی‌ها بخواهم اقدام به آزادسازی ذخایر اضطراری گازوئیل بکنند
.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465768" target="_blank">📅 00:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملهٔ جنگنده‌های سعودی به یمن
🔹
رسانه‌های بین‌المللی از حملۀ جنگنده‌های عربستان به صنعا، پایتخت یمن گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465767" target="_blank">📅 00:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVFiGXNmHOwktj69wzPnC4JMyrOyRYv1ARayuZ44BXMn5deNWvAxPoqoMv3Y2y_cf70EI1xyhEPNiEpmqyHFN9v1IIAbjW-7fRVPRhOA-M5Y1voMOMpJwe22LWPSVuvgMVk4Y1-8hWH6kGCuGK-yScFNZjc8s6J5XS0ilYexlAggsmVtEeb400rSE1YptKcUUy1tcEpvY84l5kV2k1k_zeWfeMqJ6r63jE7WZSQxJiJn-aSnpCgqjlL_OJdlIdQ0EDWlNN_b01nDiUHM9SafHaX9K083thaATThhN3fYoyFHOINViU33oS-9LCT69IROb-IFFTTAW5e2BNBMO5s9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: با حضور هرشب مردم در میدان‌ها، شاهد دوره‌ای جدید از مقاومت هستیم
🔹
فرماندهٔ نیروی قدس سپاه: آمریکای جنایتکار با این فرضیه وارد میدان شد که ظرف چندروز ایران اسلامی را به تسلیم بکشاند، اما ببینید با چه وضعیت خفت‌باری مواجه شده است.
🔹
این مواجهه را در دیگر صحنه‌های مقاومت نیز می‌بینیم. در لبنان دیدیم تبلیغ کردند که حزب‌الله از بین رفته است، اما شاهد بودیم که حزب‌الله چگونه ایستادگی و ضربات مهلکی به دشمن وارد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465766" target="_blank">📅 00:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRYNATafQFp3piVwv3iJuHZRsSXNWEZxKLhJCTt5VQ6ekRQemmGSadGDw_sVfw8wadBDoRVnxtE1yvOFok7y0ZQw1QCyXkDY2p7JX1KP21BeYGdxndmxtnsMdOAQaMv8i_plGAbBzjBzVsfzEd36yDnqH8jWgcljozhwS7TDVEtkQwDGtAw06S1RxBnGEW2RW9_VuswnLgo9CA2xshg88yKIKQdPLxAfRRtowwlr78Ghp7dz2Wp6IkD_9PUBnDkv35pfPNQOFyhBrOXaN3PLr_mV_RhoSFzGU3yL9xu6Ll3r-NxXf04lMjmJQQkSkbWyFoq6rhPFM_O1jPjLrjX0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه همین لباس زیباست نشان آدمیت
🔹
روزی ملانصرالدین با لباسی کهنه به یک مهمانی رفت، اما صاحب‌خانه با داد و فریاد او را از خانه بیرون انداخت.
🔹
ملا به خانه برگشت، از همسایه‌اش لباسی گران‌بها و فاخر به امانت گرفت، آن را پوشید و دوباره به مهمانی برگشت.
🔹
این‌بار صاحب‌خانه با خوش‌رویی فراوان به پیشوازش آمد، خیرمقدم گفت، او را در بهترین جای مجلس نشاند و سفره‌ای پر از غذاهای رنگارنگ جلویش پهن کرد.
🔹
ملا که متوجه شد تمام این احترام‌ها فقط به‌خاطر لباس نوی اوست، آستین لباسش را جلو کشید، داخل غذا برد و گفت: «آستین نو بخور پلو، آستین نو بخور پلو!»
🔹
صاحب‌خانه با تعجب پرسید: «این چه کاری است که می‌کنی؟» ملا گفت: «من همان کسی هستم که چند دقیقه پیش با لباس کهنه آمدم و با داد و بیداد بیرونم کردی؛ حالا که لباس نو پوشیده‌ام این‌همه احترام می‌گذاری. پس این احترام و غذاها مال این لباس است، نه مال من؛ آستین نو بخور پلو!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465765" target="_blank">📅 00:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOQlld6_NYeT1iHL5fcN7xumn5eF6EG-BRLkZh_GF2BnMsIfijcrlQ5fehh42xvlNV9XvFNL6herKjEiROnLoAepk3Q-HUEWwBM9czdHRQ4XE7AVr0UQHPci8MilaSoln7jNm-LfSJauO0qLlBT1ntg3_ft8XgH53QolIDAtu3ucSSG8mGYVVweXWxdFaK1OjojahKYtPVr1YAurfV5nsQt84iz1aV0v2Gu2SMl39Di73KCJJKbyym7se4j3ZLop2ypZnOu2RnTiztfnaRBBOZ2aUVXS2det-HHLV9GdIQZ2lYh9y4hdl69yh8dXeCuAmxgVKN0sw1qFu-n1AX9XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465764" target="_blank">📅 00:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLBWn7KS6JndWKZXp5XsxgihsWHduaduNNjTSVjVeCp8B7HcKmW3IsNEh9qG3wS06UXvydtIFSWQRPoPHpRq9qkD5le7dH5F6Sxwjly5HPEp7dGBaTkakz73AIy6mw-T3-rb2COay5Bcv53JmCPgDtIVIebhxG1ZGvjUxsVmbbvr5-f4vDAka2zybnc1uigjJsPJEcHCQldQv7shnNefKL5FahtDNzmCupnpMI0rpbm34FOMo8biAhnD3csaWF3AYqg_20o5Osmt-zxeOAc-w-FOz3f19oiSxyz-vd46RtfoyRU6VhWlK3uhPv0hWHZDOgVn275OMKt6DbWhjPm14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوپرنفتکش متخلف در هرمز منفجر شد
🔹
منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465763" target="_blank">📅 23:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
منبع آگاه: برنامۀ نتانیاهو برای پیروزی در انتخابات، کشاندن ترامپ به یک مهلکۀ جدید با ایران است
🔹
یک منبع آگاه منطقه‌ای در گفت‌وگو با پرس‌تی‌وی: سناریوی مضحک ربایش هواپیما به مقصد سرزمین‌های اشغالی از مبدأ امارات و فرود آمدن در عربستان در حالی روز چهارشنبه اجرایی شد که ۳ روز قبل از آن، نتانیاهو با همراهی چند مقام ارشد امنیتی و نظامی خود به امارات سفر کرد و این پروژه در آنجا بحث و نهایی شد.
🔹
در آن سفر علاوه‌بر موظف شدن امارات به نقش‌آفرینی در پروژه‌های منطقه‌ای رژیم صهیونیستی، مذاکرات چند جانبه‌ای با حضور مقام‌های چند کشور عربی دیگر  برای طراحی یک عملیات پرچم دروغین و انتساب آن به ایران برگزار شد.
🔹
هدف از این عملیات وادار کردن ترامپ به مهلکه و دور جدیدی از جنگ با ایران است چرا که نتانیاهو به شدت نگران است در صورت برگزاری انتخابات کنست در شرایط کنونی، ائتلاف او قادر به کسب اکثریت و تشکیل دولت نخواهد بود و در این صورت، با برکناری از نخست‌وزیری، باید ادامه حیات سیاسی خود را پشت میله‌های زندان طی کند.
🔹
نخست‌وزیر جنایتکار رژیم صهیونیستی امیدوار است با تسلطی که بر کاخ سفید و شخص ترامپ دارد بتواند بار دیگر او را وارد یک جنگ گسترده کند و از سلاح، اقتصاد و اعتبار رو به افول آمریکا همچنان برای ترمیم وضعیت بغرنج سیاسی خود استفاده کند.
🔹
در ایران، با رصد کامل تحرکات دشمن آمریکایی و صهیونیستی و سناریوخوانی از احتمال حماقت جدید به بهانه پروژه مضحک نتانیاهو در ربایش از قبل طراحی شده هواپیما، این آمادگی وجود دارد که در صورت هر گونه شرارت دشمن، ضربات سخت و ویران کننده به‌گونه‌ای به رژیم صهیونیستی و آمریکا وارد خواهد شد که از پرچم دروغین و بازی جعلی خود پشیمان شوند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/465762" target="_blank">📅 23:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwn_5XnWwlIrDyrWU8Vr_tF_wpEjlXEMQIaCbGjqUTi9R6o4mA6D0kEMWDuP9atDOYcu0gh6tLqK4FN28Uh0u1Ybhh02h8OI-GwkmoYljMoSIHwYIu9iAjpcSDzufZeoQzWOFAjL0cHTv_j1T0WAOH-jT03cNFgt4ifsxhrQkKKwF3U-6P-m5nbNPxaC1k6COYr7apu20m13wHm2AKccwiTzwAY0r_PSgWEk1HRMOvxvQ1UClSGa4NlGdMy3Z9g1gkCOkBmtE1CkJKmG4gIncrD1_ylaYOIMWhJLQefKGcn4Kz03sEoca4waL3fF7X0Ike5NTyNC14tz0PXvVPHnsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxDXl0CoIQSOZ1LTFdfMpFf_KsUWCyHPjhUIwuHQVlGriGSz8nsqi54mG2xQ4VJVGdyJByONCboM0WG91ytWj_hIPPfhpwkqBY46LA8r0s2gtfbXgvtqmUMAbhwwGsfn49j6eaNwNNw21Qfaykl7xCiNVg72xjBLQ2HO4GV1BgiUftKii_dmsGM0_fOO5glGUtqjGj2HcnhQ2wpkg2CZ7Dj_p8LYVDeMudF-KHSQixIOYVvyabOtXXMMnhPjki1G9d4-sEj1FkBIXiC8P8hnSKBS1aAnQal2ZFKndGiRTrYyDHgtFKst7sgMUl2w5jvQNa8YYPWHrEvqbdwtEOCzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hs5UHJvVNTw4pv8EIQCmnrwcWdOoPlFvzznjB6DKJwhmWRB8Z430DEK1ssvot_9uGkR3Iu83GIRImqXBXxDyOzQ7-vaYURU20rDpjTF23G0hPfh-YY8msGZMhORpl1XuvqkNollFXUVSURm_BuJ8wtXgt-NAI0B0ENlQZcQ0oNs7__1_tlhKSL7LX4EA70fhVzmgWI43X4RVGuZJSonQLGoWA8OlHQPtUe4LJ_4qQsKC81Ue3CCE1Q_2a2ZZgKOyCHKUvBP5j24t8Gs70M5usPGez5n2GO4BWkoa7xoZcCCV-5jVxu5s16ClJap31TZJLxrTf0wPvjC_-0kqc03zyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/465759" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌ ادعای بلومبرگ دربارۀ پیشنهاد مذاکراتی عراقچی در نیویورک
🔹
بلومبرگ مدعی شده، وزیر خارجۀ ایران، در دیدارهای خصوصی با دیپلمات‌های اروپایی و منطقه‌ای در حاشیه مجمع عمومی سازمان ملل، پیشنهاد بازگشت بازرسان آژانس اتمی به تأسیسات هسته‌ای بمباران‌شده ایران را در…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/465758" target="_blank">📅 23:07 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
