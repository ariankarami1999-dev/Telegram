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
<img src="https://cdn4.telesco.pe/file/Ba70mH17qF5gSeJsIf0rVjuOb9zuzSqTcJ9ZWYCNaJSEbL28_wf6dADtwE6JSe5jaapxqEpYKe_npGHzgc-6CSmhK9OWZIqZKWCj58UMZzQke5sDJf3tQDF6mN97ZBLKPRbig7MYAicGsmOG7uLr93t1zbU0bq8hDXXZpFOSur4tMMmqpePiRq2wybgWFL-ooGizF2FeteTn1rG1zRmwaxnAG6krq2dY12p3yMbPK90KCPqXQi1Mqd9j30sHdz4trlqGdAZGJSh0EQNOCHLWxZiSL01yNnBdPX8KNa3v31AdBYrEvYZ9FvBQ1Oooh-xkSYQw_VbM3XtT4XQkqWZ_ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-149537">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض گسترده‌ای در مادرید در واکنش به آنچه برگزارکنندگان آن «هجوم ده‌ها هزار مهاجر غیرقانونی به سئوتا» می‌خوانند، در حال برگزاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/149537" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149536">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: هیچ هیئت فنی از ایران به نیویورک جهت انجام مذاکره با آمریکا سفر نکرده است و این مطالب صرفا خبرسازی رسانه‌ای است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/149536" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149535">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شورای عالی امنیت ملی: اینکه ایران در مقابل محدودیت‌های هوایی اخیر دست به مقابله به‌مثل نظامی می‌زند، تکذیب می‌شود
🔴
مذاکرات میان ایران با کشور‌های مربوطه برای رفع برخی محدودیت‌های هواییِ غیرقانونی ایجاد شده، با جدیت در حال انجام و پیگیری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/149535" target="_blank">📅 16:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149534">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/149534" target="_blank">📅 16:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149533">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/149533" target="_blank">📅 16:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149532">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzS5XTLU1Jgv0q50bYHhxKOYWsrcWx-4XHAY3mI5h6GxACYdCZBZxKn6K83TgAiGs_XHwHpNw6yn4TTCwTY7rnzkk59-6MWYAl3LtqMHLK7k_Tls4vbnmcKHr_PYQvAbjniwBuQNC0Nvs4IIn5YSEguXiU-iq1OhV_aQjy_kF9nz_ZkcM5ToO1096I01fa52BOcgEBAbbMV4lMuNj2H5bax17C9GTyHajOLQDl7UHSHEu9ZQ97k8xAN5kAgqpxF3RjKS9yt2VLsOYqAbFt8ZXCEw1fsP0QUMZSK8BWIG43jHT1wARsMEoQVqqO4yJiZ8qQNjU3XLNAS1MOeHem68xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : اخبار دروغ نباید در کاخ سفید اجازه انتشار داشته باشند!!!
🔴
این وضعیت مدت زیادی است که ادامه دارد و هزینه‌های بسیار سنگینی را به کشور ما تحمیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/149532" target="_blank">📅 16:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149531">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده:  آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔴
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده
🔴
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم های جدید و محاصره وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/149531" target="_blank">📅 16:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149530">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ :ایران نباید به سلاح هسته‌ای دست پیدا کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149530" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149529">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟
🔴
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/149529" target="_blank">📅 15:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149528">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDT1KI4nkoYY0HF5c9orAnHGGki0DdIHkePu877LsPhbxnKA2tk-tU2Zap1jevhnO94TCUH5IkfVqIz9wbzLV6FQukj805LdrFsxSdtPbdpgekJucXlzIm0L066S28iNMZBsgOhNi4EHJUXwKSnU_yUhrihRGykYmzj7ysV_OGSR7YEJ624D-8HZsSaHNNtHv-iCv-yESyxcwdR6JYVpW_j-H5eXvadCtr-cGVvh-x-UeAxtN3fwbkOD5qeQn6rCd0stQJ7rDuwd32vAIsbVnwgO7_X2BCRfynBLNlIIIUyFZV9XEKN8juSkeFTtQcitmYeDVGhsJO4OHNHg_N8rjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروند هواپیمای نظامی باری مدل C-130H متعلق به ایالات متحده آمریکا به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/149528" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149527">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyV8hoDOcYtk9tY4fZ-E1ijLOdLw5em5Fwy8X03Akc1zEeyUlv0ciFceIbyj5kzY-piZOGcDmiJxmr6zmiUZEPIW1qjuDLoE2Fx1-F812KMTBE2FtimReey7G5tySMxMrtzRUHGw9wg5T2Fmdax_yqqSpZzU1AnthoRn7aytO_5Q9YUVTcsSpmR4kML9d7434fjogWbWG1yekHYkI90gBGODCMI3dFg3ZfBqhWwfJui6RzxSJiE7q3MsnIf2kMqrGNcXM5GsQZWJy-FPe8QVAbCwNuGaJkalECpjhQMqtwFv5_jFaPi-fdL4Wh0KAOw7WJuLBfvtuKuLhztYU3HEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۴مهر روز سرباز هست، یادی کنیم از سربازان بی گناه پادگان بمپور
🖤
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149527" target="_blank">📅 15:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149526">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان در پاسخ به سوال خبرنگار الجزیره: چرا و برای چه باید با ترامپ دیدار کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/149526" target="_blank">📅 15:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های آمریکایی گفتند، دونالد ترامپ، رئیس‌جمهور آمریکا، پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیارانش گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران را از سر بگیرد.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/149525" target="_blank">📅 15:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / وال‌استریت ژورنال: آمریکا با بیش از 50 کشور تماس گرفته تا اجرای تحریم‌ها علیه ایران را تشدید کند و به آنها پیام داده است: در موضوع ایران یا با ما هستید یا علیه ما
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/149524" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صدای انفجاری در جزیره خارک ایران شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/149523" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مدیرعامل شرکت شهر فرودگاهی امام : پروازها به ترکیه، مالزی، چین، پاکستان و مالزی برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149522" target="_blank">📅 15:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3v_etDHcdznT_WCgO9jie30FAqwvDVDorA2K9PjcqWFB0G2YIOfLTzbLR1MDjC9EAY9Ht4sbzv08U_F3othKRt4WhAEGATWxaOyi9jWmMvh1RPbqEywwosGinnYC66OSGRfRMDUrNN3dEDuFEU12KtlizWLovP5YbE0mKGfbZA-wMNrHrFpHRDcEWz1No3YPhdTq34MJjUlhNOg6r-kGPnW0jOKsf3SS1nZYS8AsRT0t1cFrgm7tY_b5HYrMEn7w679qIHKithpt9aZja7xUfv3Ez9ZoI6BjRb214lru8dmrQv2oIaF_OE0Y0WMq7TUtyj1aBiQoSgnfSxxxczKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbEmP-23LJ6_MCUGmxUm9QwM4sBlfUQFtPrzHiak_IqvIbJXEhLlSUy2yQ9e2YXF1GuUA-XU9QSUwn6Fcxu0PoavwKxxVB570GkR-__zX305SJMd5AImrppgrWZPZEhQNFTtPZm3tAqp3pZwv-Tci7zyrBqMVgYpNOJzM1eCrncmDKdcuTkf3U6YD741dpx8qw01unSPW4097ZD1LOeGMlmSnD27QVUBoZwXGGpisXvMNzxOeobKxhcTab9HwnmDSIFJRsC_iMsjmVwxeHVM2TT689rOrDcB5T2hAZy_8wArtD37h1ewIpO0kirZjNXFelWR5fJz5lFylidhvSStlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد "گران" روسی که بر فراز اوکراین سرنگون شده اکنون به عنوان یک تزئین در یک سوپرمارکت محلی در ترنوپیل، در غرب اوکراین، به نمایش گذاشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149520" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
۱۱ کشته و ۳۰ زخمی در انفجاری در شمال غربی پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149519" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
واستریت ژورنال: آمریکا از بریتانیا خواست مجوز فعالیت بانک «ملی» در لندن را تمدید نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149518" target="_blank">📅 14:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر علوم: دانشجوهای عراقی به‌زودی به محل تحصیل خود در دانشگاه‌های ایران بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149517" target="_blank">📅 14:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WizKl4D8ZgHYcIJYkfpbIWUHhc1ZfRuK0MZVMPFPFO1MpW-EwAu0ns2i0APXDRujCk_hybSiC1mUeq-sQB78H7b96_6Jt7YgNzDjit2fv98yBbZJi4xZlBnI7Sq0v1IG__zCivXhBYK-r5kEp3qf98S_0smC2gGnM3trPrhHLFabJsG8QrCfmQ1N1x1H7t8ywCjgRzELoanwkFv-51_i_6WZhGjSYAeRBZyD9pj2EcOieArD7JjcMvHZ5F77ZYBYtNfVyLFP6agcEMZouR76SWCCZfFT1HVsynL7ycHzOjGOW0LpcRK7Qt9IFUqYQ09BBUkRWvKXouYm1EeEpPQrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«چرا باید منتشرکنندگان اخبار جعلی، مانند CNN و MSNBC، اجازه دسترسی به کاخ سفید را داشته باشند؟
🔴
با وجود پیروزی بزرگ من در انتخابات، تقریباً ۱۰۰ درصد پوشش خبری درباره «ترامپ» منفی است و سال‌هاست که همین‌طور بوده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149516" target="_blank">📅 14:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیروی هوایی عربستان سعودی، پروژه‌ی تصفیه آب منطقه‌ی الأکبوش و شبکه ارتباطات در شهرستان حیفا در استان تعز را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149515" target="_blank">📅 14:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مکرون از ریاست جمهوری کناره‌گیری خواهد کرد!
🔴
امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149514" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149513">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پایگاه دائمی پیشنهادی آمریکا در لهستان که «فورت ترامپ» نام گرفته، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
🔴
رئیس‌جمهور لهستان گفته امیدوار است ساخت این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل شود؛ مذاکرات درباره مسائل مالی، اداری و انتخاب زیرساخت همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149513" target="_blank">📅 14:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723913721e.mp4?token=sGLSSSlSeKt5PsyDeT_m3mSZxI8PtNaPJs4cvAhkcD5hFTets7OuhM7LsIAXCMQR9CZljQN9soiaVTuqVYn7gPlb4CegcAA02vz145Qu6TqzPvwlh8dEs_W5DH65UuFMeZX2S19GSaBLaStH-iQJuNut4SdS0VoymZBBtYu9W1M-UETr6JCV_og3kXLmMk7pZuh5ZlsJqoBQoMsJIWnRfZTzvUVEqXOmVrq8JMQ1KytwZ1BCmw2q_0upscoMNmEXq9rEwIz5yF271-XDmo79DYMAlmdmAQ1pJs6rsDEJ4NaIWE4uvGoHMAvM-wQux5O9jJChpPeOUTloQkAtvRFKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723913721e.mp4?token=sGLSSSlSeKt5PsyDeT_m3mSZxI8PtNaPJs4cvAhkcD5hFTets7OuhM7LsIAXCMQR9CZljQN9soiaVTuqVYn7gPlb4CegcAA02vz145Qu6TqzPvwlh8dEs_W5DH65UuFMeZX2S19GSaBLaStH-iQJuNut4SdS0VoymZBBtYu9W1M-UETr6JCV_og3kXLmMk7pZuh5ZlsJqoBQoMsJIWnRfZTzvUVEqXOmVrq8JMQ1KytwZ1BCmw2q_0upscoMNmEXq9rEwIz5yF271-XDmo79DYMAlmdmAQ1pJs6rsDEJ4NaIWE4uvGoHMAvM-wQux5O9jJChpPeOUTloQkAtvRFKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خیابان‌های تایلند زیر آب رفت و ده‌ها هزار نفر گرفتار سیلاب شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149509" target="_blank">📅 14:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با شبکه سی‌بی‌اس آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/149508" target="_blank">📅 14:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یاسر الحجاج سفیر عراق در تهران در گفت‌وگو با «العهد»: مذاکراتی میان عراق و ایران برای یافتن راهکارهایی به‌منظور ازسرگیری پروازهای شرکت‌های هواپیمایی ایران به فرودگاه‌های عراق در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149507" target="_blank">📅 14:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان به الجزیره: آنچه در یمن اتفاق می‌افتد به ایران ربطی ندارد و ما با همه کسانی که مورد بی‌عدالتی قرار گرفته‌اند، اعلام همبستگی می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/149506" target="_blank">📅 13:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149505">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هیمتی: تورم نقطه به نقطه بعد از ۱۵ ماه روند افزایشی در شهریور ماه کاهشی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/149505" target="_blank">📅 13:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149504">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان: قطر و پاکستان در حال حاضر میانجی بین ايران و ایالات متحده هستند و پیام‌های ما را به واشنگتن منتقل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149504" target="_blank">📅 13:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه‌های آمریکایی ادعا کردن، نتانیاهو داره آماده یک حمله تنهایی به ایران می‌شه و اگه حس کنه وضعیت انتخاباتی خوبی نداره، جنگ رو شروع می‌کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149503" target="_blank">📅 13:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جروزالم پست: نیروی دریایی اسرائیل در حال بررسی خرید هواپیماهای گشت دریایی و ضدزیردریایی Boeing P-8 Poseidon از آمریکا است
🔴
در صورت نهایی شدن این قرارداد، اسرائیل می‌تواند از این هواپیما برای افزایش توان شناسایی دریایی، عملیات ضدزیردریایی و گسترش برد عملیاتی خود استفاده کند.
🔴
گفته می‌شود این طرح در برنامه راهبردی دهه آینده نیروی دریایی اسرائیل قرار خواهد گرفت و در صورت تأیید واشنگتن، اسرائیل نخستین کاربر P-8 در خاورمیانه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149502" target="_blank">📅 13:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149501" target="_blank">📅 13:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرگزاری چین: واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149500" target="_blank">📅 13:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ پیشنهاد آتش‌بس ایران را رد کرد؛ احتمال ازسرگیری حملات پس از انتخابات میان‌دوره‌ای
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، پیشنهاد ایران برای یک وقفه هفت‌روزه در درگیری‌ها را که شامل بازگشایی تنگه هرمز بود، رد کرده است.
🔴
بر اساس این گزارش، ترامپ در محافل خصوصی در حال بررسی انجام دور دیگری از حملات هوایی پس از انتخابات میان‌دوره‌ای نوامبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/149499" target="_blank">📅 13:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly_YVdMq1Gx2UPxQmzd9_kyy6TcgnTcQC-Q3pQPHngAU-PJrsp9GzuaJN7ZoMuaTlt6vxeXMq7IacmQjdQZAAsx5C9zntzhaHxgIVArfWPuX8hbUP7yGvdl7md6fEaqfC4l4ridZvDqRxoXYqIoDT7RBOI23CCK8G3RclWv5cxW5q_GgkXJjT-MYDJTV-kDPcL0ui3irQkPNn2Nd430LcVhLLBBY4WCherfxvHQe90nl_5yYA9fgppSb9OTFwq7XqjM-3JTVhSsZFRoqD8lntM9Sh7HXum_BGFJijdKRPgikgFxbq4p8r7JV80H5xgyqkHge1-D9P1I7Je_FsZ07Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d0cfc6e2.mp4?token=gR_SbH6ZrLkMh5qJ5dHDZpBtFtHynLCW-bhFjHvpawcfjW4VkqZcruiVs0SCv6jWXZUrT8NTgho6I8BV7c5tSH0DkKEAOPk2RqPySAC0uKzl6kmsTdq-A6ryocjfsYcIMxT1KZD8wOCfSJb-NtMjcyyIjFkn_9jDjIdEpq-I1iUN2-RJWsUQE-wImLWj8nD4vpmYmCL6Y_iiBeMyUdAGCI5VNTbSj8YaHGrYB241-QvpIU2fmHtCfjjWLTjLRcb-Uqkt_-qFvIUtwZ2TFhpfQm9ZGRmu9XMiPrnJNozW2HYpwOq-13rBUCFzxxUJtP8JmPquGf16cuj3J-azN_mY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d0cfc6e2.mp4?token=gR_SbH6ZrLkMh5qJ5dHDZpBtFtHynLCW-bhFjHvpawcfjW4VkqZcruiVs0SCv6jWXZUrT8NTgho6I8BV7c5tSH0DkKEAOPk2RqPySAC0uKzl6kmsTdq-A6ryocjfsYcIMxT1KZD8wOCfSJb-NtMjcyyIjFkn_9jDjIdEpq-I1iUN2-RJWsUQE-wImLWj8nD4vpmYmCL6Y_iiBeMyUdAGCI5VNTbSj8YaHGrYB241-QvpIU2fmHtCfjjWLTjLRcb-Uqkt_-qFvIUtwZ2TFhpfQm9ZGRmu9XMiPrnJNozW2HYpwOq-13rBUCFzxxUJtP8JmPquGf16cuj3J-azN_mY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوایل امروز، حملات هوایی اسرائیل منطقه جبل الرفاعی در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149497" target="_blank">📅 12:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae558b3656.mp4?token=mLfY4vuyS-6EQeCq9urmN_vKU4DsfhOOyVc-CGlglPpspR5pRbmJ-RTfM9UwPS5CiJVwMeX-6xXm2orizADY9TKj3-MAgLFuU2VlSkBGNKyl9GA58awb5kblWcJfUC5BnHZ_oOykZO2a601LsNSiHg07yzma4DIkomsFIGCLolT1uaabETqrpvA96rmudieyLXvulgh3q3peSle3C7o4s0F71akygr7eUSLHA_vGUZgMir114KoN8JzGtpDbf92wJVeYRGXKspSOdJffVlG94qUWN6unmlcaXLvz4pqAKwEuLdJ7Fuo52ooUGkZo_Nko10qg-JfLD2g8r8X1nMpRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae558b3656.mp4?token=mLfY4vuyS-6EQeCq9urmN_vKU4DsfhOOyVc-CGlglPpspR5pRbmJ-RTfM9UwPS5CiJVwMeX-6xXm2orizADY9TKj3-MAgLFuU2VlSkBGNKyl9GA58awb5kblWcJfUC5BnHZ_oOykZO2a601LsNSiHg07yzma4DIkomsFIGCLolT1uaabETqrpvA96rmudieyLXvulgh3q3peSle3C7o4s0F71akygr7eUSLHA_vGUZgMir114KoN8JzGtpDbf92wJVeYRGXKspSOdJffVlG94qUWN6unmlcaXLvz4pqAKwEuLdJ7Fuo52ooUGkZo_Nko10qg-JfLD2g8r8X1nMpRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو مشهد، آقایی که توی این ویدیو می‌بینید، ظاهرا یه چک رمزدار ۱۰۰ میلیون تومنی نذر کرده و انداخته تو ضریح امام رضا، به امید اینکه زنش شفا پیدا کنه.
🔴
حالا بعد از یه مدت برگشته، رفته بالای ضریح و میگه زنم مُرد، تا پولمو پس ندید پایین نمیام
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149496" target="_blank">📅 12:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
واکنش حسن روحانی به سخنان اخیرش: اصلاً من نه کلمه رفراندوم را گفتم و نه کلمه همه‌پرسی را
🔴
بحث من، لزوم برخورداری «اهداف ملی» از پشتوانه مردم بوده است، نه برگزاری همه‌پرسی درباره دفاع در برابر تجاوز
🔴
اینکه جزو بدیهیات است که وقتی به ما تجاوز بشود، باید دفاع کنیم
🔴
دستاورد جنگ باید کاهش احتمال جنگ بعدی باشد
🔴
ایران همچنان در شرایط بحران قرار دارد و نباید تصور کرد با پایان برخی مراحل درگیری، مسئله جنگ پایان یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/149495" target="_blank">📅 12:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
هشدار نسبت رگبار در دامنه‌ها و ارتفاعات تهران
🔴
اداره کل هواشناسی:از بعد از ظهر شنبه تا پایان دوشنبه (۴ تا ۶ مهرماه) در بعضی ساعت‌ها مه رقیق گاهی بارش باران، رگبار و رعد و برق و  وزش باد شدید موقتی در دامنه و ارتفاعات استان تهران به‌ویژه مناطق شمال شرق پیش‌بینی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149494" target="_blank">📅 12:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مشاهده مخزن سوخت جنگنده آمریکایی - اسرائیلی در غرب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/149493" target="_blank">📅 12:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8a000035.mp4?token=WFC-GAvGEj0iaQkcYyZlMI6DAxqMMJca1RzDR_d7c4irWMKrR0vaogUqVlkHP8DMxbe3qSRya7dgLgmtKZDzkpKwUv0pcG9ZWNOo8Hz2SoRZSTLu6lgVxWSO6LdBB5uMTaXMi53URB8haiYGElscqGenY3mQOPbULXJid0kr2vIYh2Cs9ya2ewzOGROFRnfnjuq4LrCVTtkSUFeQ1QKpJgCPq055aa20ulQQFMExxPSvQTuO5eJfsWTyMfERy07caG-NUcTzwmZYGyAyqYUP0zwqJaG-_zh6I3GtFRkzhjvkXSG2lDYBdIw48cvIgHzLA-F0JaD7j8QavlEnFj5A_jC2YjWuguTnWdVCCZO1eRIssQHrK76PHxFrGE_25cxIQ4w0qMm_pABRQ5S5lomDvtNePP0BRTS4h3p803lQz88Xv49lmsCdKiIhtLcVU2MiwDvDMDEzwML1VXbmYBi-O2ttlmtMuIAdJ6k5yUV8PqCaJzjRInRccl92rqYaretp_GOW4Lm3jT1gyD4AOILn17j14GGylw43wItKUsOGoTxsFlzv05kkutygkWappKmZHb5u0PN7Jtjoi6z1Fs_DfnztFC4Fd7OSHmqCkcwgzhCkE9SV9TfEtmZFDFBlR9JFRlI_lGkGnGH5hVvFZucCLCcgEwjjyDzkoMw7e0vkOWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8a000035.mp4?token=WFC-GAvGEj0iaQkcYyZlMI6DAxqMMJca1RzDR_d7c4irWMKrR0vaogUqVlkHP8DMxbe3qSRya7dgLgmtKZDzkpKwUv0pcG9ZWNOo8Hz2SoRZSTLu6lgVxWSO6LdBB5uMTaXMi53URB8haiYGElscqGenY3mQOPbULXJid0kr2vIYh2Cs9ya2ewzOGROFRnfnjuq4LrCVTtkSUFeQ1QKpJgCPq055aa20ulQQFMExxPSvQTuO5eJfsWTyMfERy07caG-NUcTzwmZYGyAyqYUP0zwqJaG-_zh6I3GtFRkzhjvkXSG2lDYBdIw48cvIgHzLA-F0JaD7j8QavlEnFj5A_jC2YjWuguTnWdVCCZO1eRIssQHrK76PHxFrGE_25cxIQ4w0qMm_pABRQ5S5lomDvtNePP0BRTS4h3p803lQz88Xv49lmsCdKiIhtLcVU2MiwDvDMDEzwML1VXbmYBi-O2ttlmtMuIAdJ6k5yUV8PqCaJzjRInRccl92rqYaretp_GOW4Lm3jT1gyD4AOILn17j14GGylw43wItKUsOGoTxsFlzv05kkutygkWappKmZHb5u0PN7Jtjoi6z1Fs_DfnztFC4Fd7OSHmqCkcwgzhCkE9SV9TfEtmZFDFBlR9JFRlI_lGkGnGH5hVvFZucCLCcgEwjjyDzkoMw7e0vkOWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ای که فرزاد فرخ زاد دنبال عراقچی و تخته‌روانچی میدویید و ازشون سوال میکرد و اونا فرار میکردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149492" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9af12d6d.mp4?token=XRRzefN7qhy_19fKiqkyaL63cQ7AyoIfvWtzEQLKj5QLjHO0BqWBtAHqflpvTVSi54kezedVWWpxujf3Nu7iTQ7QwhJ6CtCSxzXITlHcvaxomH9Vnv38nxMc4SCAIi-cEfQtxnnvMvgLdLrrHe11wCw3V2K2QnuP5fFySxstuRyzKvv9QbhrjdflpEWDzpwUjYcg8Dej7-CWfhSY4xlqzmnd4Fp3nNVSoEH_WCbfFtVpZDoykraj8kMsnQHiXvDKSQvoKoN5VzJJXYihCvVPxEogwN472WKIVDeClaxpr-8P--p1mMB2nzAAWrjyo1S6KZWu_u5DVIJNIGRHP50veQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9af12d6d.mp4?token=XRRzefN7qhy_19fKiqkyaL63cQ7AyoIfvWtzEQLKj5QLjHO0BqWBtAHqflpvTVSi54kezedVWWpxujf3Nu7iTQ7QwhJ6CtCSxzXITlHcvaxomH9Vnv38nxMc4SCAIi-cEfQtxnnvMvgLdLrrHe11wCw3V2K2QnuP5fFySxstuRyzKvv9QbhrjdflpEWDzpwUjYcg8Dej7-CWfhSY4xlqzmnd4Fp3nNVSoEH_WCbfFtVpZDoykraj8kMsnQHiXvDKSQvoKoN5VzJJXYihCvVPxEogwN472WKIVDeClaxpr-8P--p1mMB2nzAAWrjyo1S6KZWu_u5DVIJNIGRHP50veQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: من در زمان بمباران در پناهگاه نبودم و گاهی در یک روز به سه وزارتخانه سر می‌زدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149491" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcBXO6BWKnXoDgSyj70Ja7FLOeAd_7BCTOZJNcMX7swZNhQEgjeCHVO0jg67OrCEtdo9MrHZ1S-8GzLZw93PN152mMNKfAX_pau8cj2KNTiJ3LOYTbgWrMwL1iOae8lSIfggAiM4h05Ur7g43KIJ0hTuvo-Bucgs7UZ_UR4EHA0VSdTTZgQxvTP4nKj9GqNnBK6sKIvOQ40xtzeSaC0zeB1VlVbMqmJIaYLJaSd_hymwyxZc7BYCrhn6f3cLY_LfgjHVgprrY53yb-Xm-RUCt4pA9VwhuT2lcV4QnzLLQeJnVNTZyNTGX9XrIXf3n8gWBDS4QihY3DHit4HAsoceug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای تانکر سوخت از پایگاه نظامی "العُدید" متعلق به آمریکا در قطر، به سمت دریای سرخ پرواز کرد و احتمالاً در حال سوخت‌رسانی به هواپیماهای جنگنده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149490" target="_blank">📅 12:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ux8ZfhCC_o2Wm93ZCEU156W6WDVhdV08CjVytVgABTo4kEGjsJo8kSPD_lGOqRVv1V8AueOS_iuGVmSPnhk3JZhr5hcAQFM3gkwGUg51lgM8O0W-qiAdnusf8NjBCJlXOBDwesU5jgakS2VVi5qAw4QmLjXSBam77kvJCCAt-oqyCJp7YU-VO5q0kaWuYWxayIFZT2Kc4p9d6iWYGgCZwo6mvKdkIgaJhnkPsf09Y1iuiN6mn4VSjGv73HIdTuqJ-OLRY_ijqwxfZ47OMCbytLdxifgmUsQuI4uBr2u27aU2Tm_XUFPxtgMaDKtYVdam1ynylkzv7_KIVvtiowIhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن در ۲۵ سپتامبر پس از شناسایی یک فروند هواپیمای شناسایی ایلیوشین Il-20 روسیه بر فراز دریای ژاپن، جنگنده‌های خود را به پرواز درآورد
🔴
وزارت دفاع ژاپن اعلام کرد این هواپیما از سمت قاره آسیا به سوی آب‌های نزدیک استان توتوری پرواز کرده و سپس تغییر مسیر داده و به سمت قاره بازگشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149489" target="_blank">📅 12:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وال‌استریت ژورنال گزارش داده ترامپ در محافل خصوصی درباره پذیرش شروط آمریکا از سوی ایران تردید دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149488" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از مقام‌های آمریکایی مدعی شد یک ارزیابی اطلاعاتی محرمانه ارائه‌شده به کنگره، احتمال حرکت عربستان سعودی به سمت ساخت سلاح هسته‌ای را مطرح کرده است.
🔴
این مقام‌ها تأکید کرده‌اند عربستان هنوز تصمیم نهایی برای ساخت چنین سلاحی اتخاذ نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149487" target="_blank">📅 11:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با  شبکه سی‌بی‌اس آمریکا: آمریکا برای باز شدن تنگه هرمز عجله کرد که باعث شد تفاهم‌نامه از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149486" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">طلا منفجر میشه
💢
تحلیل عجیب
🚨</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149485" target="_blank">📅 11:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=owIbhuGXV52z0x7yX3wUuynZINuHuqTI3t4wpSG1GhmTsPT3CmvBMMpb-WVnF8uOh6lWsA7mxKEObxGtxEZIuBEXJjIx-aTvRPEvhOeaTtySISUG4-5MNeahhofklJwGfMf2nkm_qTq2qJmLJlg6xPvM7m-KlVEOumeKXIaUgZE0eJ29UKXzdt_QIi9Nr2W7j0LOQuQE-vdG7BD-SucW8miZP3OLK_PpfJnScJJjcOYMywjhLu9WV8hoh7eh1HNw79DyNIWFbkXmA5-P3sT7wC_etJpTLhpQH-v9sJFlKnH8rDIfBVJibYHlW1eCE1EjYrOEjWmGbRzyE1QquWYT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=owIbhuGXV52z0x7yX3wUuynZINuHuqTI3t4wpSG1GhmTsPT3CmvBMMpb-WVnF8uOh6lWsA7mxKEObxGtxEZIuBEXJjIx-aTvRPEvhOeaTtySISUG4-5MNeahhofklJwGfMf2nkm_qTq2qJmLJlg6xPvM7m-KlVEOumeKXIaUgZE0eJ29UKXzdt_QIi9Nr2W7j0LOQuQE-vdG7BD-SucW8miZP3OLK_PpfJnScJJjcOYMywjhLu9WV8hoh7eh1HNw79DyNIWFbkXmA5-P3sT7wC_etJpTLhpQH-v9sJFlKnH8rDIfBVJibYHlW1eCE1EjYrOEjWmGbRzyE1QquWYT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از برخورد اتوبوس و تریلی حامل میلگرد در محور بیرجند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149484" target="_blank">📅 11:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149483" target="_blank">📅 11:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نشریه CNBC صادرات نفت خام عربستان سعودی با وجود قطعی خط لوله به بالاترین سطح از زمان شروع جنگ ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149482" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کارشناس صداوسیما:آمریکا تو جنگ نشون داد طبل تو خالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149481" target="_blank">📅 11:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=dBCahm4YcDfLb6qgLd2cahG1JOCBTuAQSnDUuV46UOH4Ebaav6zrvIEh5lT54piCoV-3mtoURXdXA5w6W9v5UIfDZw5Q10CvLusWXbTjQLvh7m2oboW-2dAfH98p4rNZcBHEtuSz5niMAxWIcY97peNbNOCabbzAQCnTGoFFKzkYh6I4J239l-_qCIrOKoY9rprL7eUw77aQE8K3eWRnPK32KOAXpB5JSgNkZst5STljmqwUVsY0yCZaZB5veeUgit9PLTCU6QymfpO_I8CGreUePvQJ9rkodr6-LjAL4siN4UiK8Ang4_o46zTnRsOay9LZX71D6erUM5m-LTABQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=dBCahm4YcDfLb6qgLd2cahG1JOCBTuAQSnDUuV46UOH4Ebaav6zrvIEh5lT54piCoV-3mtoURXdXA5w6W9v5UIfDZw5Q10CvLusWXbTjQLvh7m2oboW-2dAfH98p4rNZcBHEtuSz5niMAxWIcY97peNbNOCabbzAQCnTGoFFKzkYh6I4J239l-_qCIrOKoY9rprL7eUw77aQE8K3eWRnPK32KOAXpB5JSgNkZst5STljmqwUVsY0yCZaZB5veeUgit9PLTCU6QymfpO_I8CGreUePvQJ9rkodr6-LjAL4siN4UiK8Ang4_o46zTnRsOay9LZX71D6erUM5m-LTABQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با شبکه سی‌بی‌اس آمریکا: وقتی آمریکا به آنچه تفاهم کردیم، عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149480" target="_blank">📅 11:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00db30387a.mp4?token=l5NplzeXOevMh7iXijICkcV_CH4MVVTmfDipsnIERclUwd0mwkei8LRcoJkfBcnWRNfon1I3DjlqWQRcgpQGBMUnGtJ-2VYCp8e1rwTcqwND5spGlr_jxJy9g3mXeQAvOZkz6k9d6gnTr5UT2lNZ4w5sY7K1ul9lZY3iBUQuFROglZ_pgVGlAoWTlCaqfD3kl1_HIAHgRW1cuEgWJq10j-xm_cfvFJGzd1vDmVKZOAEqCg_X4-uUtpYaqpLjRhZif_8_kDuhYhfb322Pbii68Z9l7SKH_aj8ArnthXKaftatHkGbo3dBVdLWaohwah5kQKIfbJJuMo-3l3amBmsUNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00db30387a.mp4?token=l5NplzeXOevMh7iXijICkcV_CH4MVVTmfDipsnIERclUwd0mwkei8LRcoJkfBcnWRNfon1I3DjlqWQRcgpQGBMUnGtJ-2VYCp8e1rwTcqwND5spGlr_jxJy9g3mXeQAvOZkz6k9d6gnTr5UT2lNZ4w5sY7K1ul9lZY3iBUQuFROglZ_pgVGlAoWTlCaqfD3kl1_HIAHgRW1cuEgWJq10j-xm_cfvFJGzd1vDmVKZOAEqCg_X4-uUtpYaqpLjRhZif_8_kDuhYhfb322Pbii68Z9l7SKH_aj8ArnthXKaftatHkGbo3dBVdLWaohwah5kQKIfbJJuMo-3l3amBmsUNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: آمریکا و اسرائیل هر کس که دلشان می‌خواهد ترور می‌کنند، بعد می‌گویند او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149479" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=mDLIKFs3LaTfjxZ2KNAaqJ_J6FFELdZ1wva_G9XxDLt_U6gQzekb7oAqkobs0UoApbqQih1PapusWFDXRw_wMIhm6WhddHTphZFOWAuz25EvqZ2lzrqiVz1cQFeaxLi1kH2XmZbsXSOlf8NAaj4uOOtrsVacIreddqnYBNotNvAjCyznthBy0rOM9bir9onvHeD94GOkKYaRiDGUsnwSSyJu8XWwcf7mF6zehapM_0K35w0DGt3Dl1peyatqPZE5NTd5qk4ykTXB9DhQFoZ42qqp3mP1pOVEcV4FNvcwJa4QYKnJWI2EiZbGOl4nbDLXUZfq5htMDZ9p6JrnlwBTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=mDLIKFs3LaTfjxZ2KNAaqJ_J6FFELdZ1wva_G9XxDLt_U6gQzekb7oAqkobs0UoApbqQih1PapusWFDXRw_wMIhm6WhddHTphZFOWAuz25EvqZ2lzrqiVz1cQFeaxLi1kH2XmZbsXSOlf8NAaj4uOOtrsVacIreddqnYBNotNvAjCyznthBy0rOM9bir9onvHeD94GOkKYaRiDGUsnwSSyJu8XWwcf7mF6zehapM_0K35w0DGt3Dl1peyatqPZE5NTd5qk4ykTXB9DhQFoZ42qqp3mP1pOVEcV4FNvcwJa4QYKnJWI2EiZbGOl4nbDLXUZfq5htMDZ9p6JrnlwBTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا
:
هیچ ضمانتی وجود ندارد که آمریکا و اسرائیل دست ترورها بردارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149478" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بغداد: مذاکره مستقیمی با آمریکا برای مستثنی کردن برخی فرودگاه‌ها از تحریم پروازهای ایران انجام می‌دهیم
🔴
هشدار می دهیم تداوم بحران‌ها، پیچیدگی اوضاع را بیشتر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149477" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روزنامه کیهان خطاب به پزشکیان:
چرا گفتی به دنبال ترور ترامپ نیستیم؟
🔴
انتقام از ترامپ یک ماموریت الهی و حتمیه، خون‌خواهی مطالبه ملت ایرانه و ترامپ باید کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149475" target="_blank">📅 10:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCk-rm8XwdwzairOFdKzX2r1FfcHpp-QLDsPTPbl6dym65LjaJL1RzGVyaj6x9T4v9moO0Y_IWAgbbN7DNFVRpnvyoBlLju2d8wLn3_x0wiLY6d5jA_MP1ue-j2AzMSy4skdQCZ6_yBDIqbNg9gJGEWUMvI0K1Os7-YMs1gQvJO-HJRSp-jVB6pIpwphtjrT0O48eknsjMbpuAycEr2gqabQv858sH6uBVT3z4hnMjxUFhbpXW9-fc8rivdqeLJXyXEOamyC5bTbWuViIWaz4qW6jmP22SsT5YT7x44xq8iB_htZC-PtAq9uS_8zJj6NfvoOK7nRhT-eEOx-7id4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از دیروز هربار اینستا باز کردم سردار بلاگر اومده اکسپلورم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149474" target="_blank">📅 10:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان به سی بی اس: با رهبرمون ۷ساعت رو زمین نشستیم و حرف زدیم و کاملا سالمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149473" target="_blank">📅 10:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
توافق احتمالی فقط درباره پرونده هسته‌ای نیست
🔴
در مذاکرات جاری، علاوه بر برنامه هسته‌ای ایران، موضوعاتی مانند بازگشایی تنگه هرمز، محاصره بنادر، صادرات نفت و دارایی‌های مسدودشده ایران نیز از محورهای اصلی اختلاف میان تهران و واشنگتن هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149471" target="_blank">📅 10:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اتحادیه اروپا: در نتیجه پیامد‌های جنگ ایران بر بازار‌های نفت و گاز با بحران قیمت انرژی مواجه‌ایم
🔴
اگرچه اکنون آمادگی بیشتری نسبت به زمستان سال ۲۰۲۱ داریم، اما دولت‌ها باید آمادگی‌های خود را برای زمستان پیش‌رو افزایش دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149470" target="_blank">📅 09:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7KUMZayGuYHSCOkRVVVG0F1rPzBQKQmg-_Dc5UB6EXBTqmXFAujUQytsXU5Ojgi4fU5AEI0u2JYq4_97w4i6x2dFYO6IGp4_yVIPUonVjXvPXj4NArUmqp96m5tM7bloBvLP-KenjOPFncFdyaQ2iqCPaBLjy91AXMbR7hXBf7RzCS6Vnpbc7WxSUz2M4n3gon6RCbza045UweXI_Ami-bBXxtG9TnVNjLDinDKEvBHNel7dwKvwOjmY_kWxGyx4NDNZfrF6ZVEHl92aczMslAJn2f5TpWZBHt2FjCjOUr6gayh095GFWr3em-59MLEhgKIUdHoqDJ6-DCuv7HMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ایران در میدان دیپلماسی فعال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149469" target="_blank">📅 09:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وال استریت ژورنال:
🔹
طبق گفته مقامات آمریکایی، ترامپ پیشنهاد ایران مبنی بر آتش‌بس هفت روزه را رد کرده و به مشاوران خود گفته است که انتظار دارد بمباران ایران پس از انتخابات میان‌دوره‌ای ماه نوامبر از سر گرفته شود.
🔹
پیشنهاد ایران به این صورت بود که در ازای لغو…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149468" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پنتاگون: شمار نظامیان آمریکایی زخمی در جنگ با ایران به ۸۶۱ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149467" target="_blank">📅 09:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olGkCmlw7OrGDdJFD_Vf3CC2Zp5roYKtulqmMuRe8rnQX98nRDLeIMBp1ZOJeE8nME19VxI3cWSirmn0qetreohnLAlgb6pY3s1a0SundR69Ae6rzYhzsYszTQfrqK5yqCYAPc0v7y0iNR3X55amBjZQXqXHCd2oQq6Dz81n-OqXLJ5iL624JHQjPKhrD166OLK0fKRoLygiVc9c_GFQRrbUYzG4r01Nrp-C9jAUkQV3xrso_PdX7V5yAwCDhRz9G3Kp4H3wtOj3tnFQAn1AWsEY_oQNo9KRkFHg8siKFUDXjjazeuP3Fp0XnkV-Q4gYcD0FQnbhqjkcVGrnlGJlEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: تنگه ترامپ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149466" target="_blank">📅 09:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تریتا پارسی: نتانیاهو ممکن است پیش از انتخابات اسرائیل به ایران حمله کند
🔴
‏یک تحلیلگر اسرائیلی به من گفت که نتانیاهو ممکن است پیش از انتخابات اسرائیل حملاتی علیه ایران انجام دهد؛ به‌ویژه اگر اعداد نظرسنجی‌هایش شروع به افت کند.
🔴
‏ او محاسبه خواهد کرد که این حملات نمی‌تواند ایران را شکست دهد، اما ممکن است رقبای انتخاباتی‌اش را شکست دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149465" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149463">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
علیرضا تقوی نیا، روزنامه نگار وابسته به سپاه: جنگ سوم در خاورمیانه میان ایران و اسرائیل و آمریکا، قطعی و قریب الوقوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149463" target="_blank">📅 09:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149462">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149462" target="_blank">📅 09:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149461">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bec11227.mp4?token=SyX5m6t048dYNQuQqGkxDkb_PBJm0OOUlHVKJKEMX-he2k7BbktcGLV0wsTDXxjAYTyNV2aJ3HOzW4Wo0ZfuCY1ZPkclpOede7vBXlSoZzNaj3IBWihrJPGVwvFCQ747m5zJVx6HKEfjAKSFgbrTKzyS6PAnBwjmSD8igz-j33arf7QG91kZSFTu3YCu8SBNHbjb6pRWUlzxybax0hP8UZeMUKwYdH2ycyhocZzdebkSchR9FupM0A9DBIa5HBeo1UjvQyW43aHYcH2cJ1oOyJbXUc_EK67I2ekkpMNXaJ5nV2bRaU3sP12ZFXsdmJPsiiw9ELj2ntdDSyClOJsTyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bec11227.mp4?token=SyX5m6t048dYNQuQqGkxDkb_PBJm0OOUlHVKJKEMX-he2k7BbktcGLV0wsTDXxjAYTyNV2aJ3HOzW4Wo0ZfuCY1ZPkclpOede7vBXlSoZzNaj3IBWihrJPGVwvFCQ747m5zJVx6HKEfjAKSFgbrTKzyS6PAnBwjmSD8igz-j33arf7QG91kZSFTu3YCu8SBNHbjb6pRWUlzxybax0hP8UZeMUKwYdH2ycyhocZzdebkSchR9FupM0A9DBIa5HBeo1UjvQyW43aHYcH2cJ1oOyJbXUc_EK67I2ekkpMNXaJ5nV2bRaU3sP12ZFXsdmJPsiiw9ELj2ntdDSyClOJsTyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: روند توافق، با پذیرش آمریکا آغاز می‌شود
‏
🔴
مسعود پزشکیان، رئیس‌جمهور ایران، در پاسخ به پرسش CBS درباره زمان دریافت پاسخ آمریکا به پیشنهاد تهران گفت: اگر این پیام به رئیس‌جمهور آمریکا یا افرادی که در مذاکرات دخیل هستند برسد، طبیعتاً از همان روزی که آن را بپذیرند، روند آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/149461" target="_blank">📅 09:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149460">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6e918d01.mp4?token=Arz46opZbHffazlb5VPlsdG0pUKoBGNqI35nuSRnP8M884ol7C0kc6Q03-Qb94GonRTW78YZO0ZdjKGR54atyUxZD51AUtzRQX60pgD53gRwlMiMJN4dUog8qckrOxXMR0NhO9vLq24tcJf-9syJ-zYBuKd9KkqtlGxnbO-YhrYd1LqccGvIbC4VXgreaTNu7kBzeThDNcjPa3LGuLs0YjgZxUOImCyuOdqX-WR9Cf65lf-V29aNQfFP7klCEPZeL-h-Bz8YY037wKQjvE3RkK_lE0lNWEJJ4LqUP0y8nqA2Ae3iKnjdCmLHiZxy6r3UVwgsT-ux6O9DVXwwivvzj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6e918d01.mp4?token=Arz46opZbHffazlb5VPlsdG0pUKoBGNqI35nuSRnP8M884ol7C0kc6Q03-Qb94GonRTW78YZO0ZdjKGR54atyUxZD51AUtzRQX60pgD53gRwlMiMJN4dUog8qckrOxXMR0NhO9vLq24tcJf-9syJ-zYBuKd9KkqtlGxnbO-YhrYd1LqccGvIbC4VXgreaTNu7kBzeThDNcjPa3LGuLs0YjgZxUOImCyuOdqX-WR9Cf65lf-V29aNQfFP7klCEPZeL-h-Bz8YY037wKQjvE3RkK_lE0lNWEJJ4LqUP0y8nqA2Ae3iKnjdCmLHiZxy6r3UVwgsT-ux6O9DVXwwivvzj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: در صورت موافقت آمریکا، به چارچوب توافق اسلام‌آباد بازمی‌گردیم
‏
🔴
مسعود پزشکیان، رئیس‌جمهور ایران، گفت تهران پیش‌تر بر اساس تفاهم‌نامه‌ای که در پاکستان امضا شد، به توافقی دست یافته بود و چارچوب کنونی نیز همان اهداف را دنبال می‌کند.
‏
🔴
به گفته پزشکیان، خواسته‌های مطرح‌شده در آن تفاهم‌نامه اکنون به مراحل مختلف تقسیم شده تا روند توافق به‌صورت مرحله‌ای پیش برود.
‏
🔴
او افزود: اگر آمریکا با حرکت بر اساس این چارچوب موافقت کند، «همه‌چیز به شرایط پیشین بازخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149460" target="_blank">📅 09:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149459">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d078d7d0.mp4?token=czWAPYlWp0ubpjXcoPg38lC4270Fmc8R3Zs_cPFaM6A7aGVn2v2uG7DSBjlEdmTD4hxzimDdBJYMcfol-ZKfhPfQTizQReG-aWi91KLKo4Zy6UxoA1bwhTTunvHT63QFZuYFKYOszoqWwp8b-Z9C22ZTKv-BLR1xTLBzf7Ul_RNzL09i3K94RTdOWRkYnm_dWXgoj8UpUq1pn23329dbkXLN6TB7GfAX43rvJuwS3GywLSphCRuYsHqOsBug1xy_IANaRyaYtdaYmjFDbl0mdpoELwIdBVD9-BaEKroJb2zrFvvvuLdOedn8vBA5sVO7-GBr-IMa1cqw0n2dIzc-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d078d7d0.mp4?token=czWAPYlWp0ubpjXcoPg38lC4270Fmc8R3Zs_cPFaM6A7aGVn2v2uG7DSBjlEdmTD4hxzimDdBJYMcfol-ZKfhPfQTizQReG-aWi91KLKo4Zy6UxoA1bwhTTunvHT63QFZuYFKYOszoqWwp8b-Z9C22ZTKv-BLR1xTLBzf7Ul_RNzL09i3K94RTdOWRkYnm_dWXgoj8UpUq1pn23329dbkXLN6TB7GfAX43rvJuwS3GywLSphCRuYsHqOsBug1xy_IANaRyaYtdaYmjFDbl0mdpoELwIdBVD9-BaEKroJb2zrFvvvuLdOedn8vBA5sVO7-GBr-IMa1cqw0n2dIzc-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سی‌بی‌اس:
«اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران به آن پایبند خواهند بود؟»
🔴
مسعود پزشکیان: «بدیهی است که به هر تعهدی که بپذیریم، پایبند خواهیم بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/149459" target="_blank">📅 09:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149458">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان به سی‌بی‌اس نیوز: ما به دنبال ساخت هیچ سلاح هسته‌ای نیستیم و به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود به کشور را خواهیم داد.
🔴
تیم ۶ نفره از نهادهای مختلف درباره سیاست خارجه تصمیم می گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149458" target="_blank">📅 09:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149457">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8kWvPZB1ud-CDx0KZoI49EPtVXIfz7aQ-VUUmmBQvGVNZWrfVqa2lrYWjMBtPxmPiqRMSMhu4EgWWakUG9T3cah8AVGNg68ak_Mec8eRDu-oW5sxCbi4eo9pu8AHaI5DcAhtriPSvmu3wqHIhHqN_LjFa1lMn63XYV8ddCbzbv8gK3pVC1abbBuNxbtEw3BJKZn_iDAPAdcjGLKs86Rs7Yfpaa0vRVMXGLYyqW1dRSsHEY-C0G1drdLQGgcBzvDKdJfxNieTcm9g3d2ogZjP914dxbaplT67YwGWoMleSV2uFjkAPIemQ54jc9-Wk14xyu51GUwfsC3G1DPnmv6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر تند فرهیختگان علیه قلعه‌نویی: ۱۳ سال ناکامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149457" target="_blank">📅 09:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149456">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8710f402b8.mp4?token=rdg5d9sXufo7d6rrDVFuv2BlvVYDP7QIZiY0Qd8JzMB9YTUMdrN97Y7bn4iGW6S9u3dH0qocgw2YSzDwdmZLRxTxF0i8xmHqRZPc8-OKlVbIpd-_ScNUgrW1UgS_8cKI3TfiBdkidoc3tv8SUxYRCxDRLF5ySodaxS3Qv8W4rwQyCRyX1PD4ymqxiCAWbTa5_eUO7FVqPiGeDKzbjtMB310CXvHDq5upls5KNGy4YUh2zmoa0YrQnVO8oH5xD-RyO_kTiaB4I2bMV5h0qRCN6PktpDvl-I6xP4T7oECitPzfp-YL5pRck-q1t00oAyDsnP9rNf1-GdFoTGGKy-wcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8710f402b8.mp4?token=rdg5d9sXufo7d6rrDVFuv2BlvVYDP7QIZiY0Qd8JzMB9YTUMdrN97Y7bn4iGW6S9u3dH0qocgw2YSzDwdmZLRxTxF0i8xmHqRZPc8-OKlVbIpd-_ScNUgrW1UgS_8cKI3TfiBdkidoc3tv8SUxYRCxDRLF5ySodaxS3Qv8W4rwQyCRyX1PD4ymqxiCAWbTa5_eUO7FVqPiGeDKzbjtMB310CXvHDq5upls5KNGy4YUh2zmoa0YrQnVO8oH5xD-RyO_kTiaB4I2bMV5h0qRCN6PktpDvl-I6xP4T7oECitPzfp-YL5pRck-q1t00oAyDsnP9rNf1-GdFoTGGKy-wcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اون دزده که تو مشهد گوشی یه رفتگر رو زده بود دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149456" target="_blank">📅 08:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149455">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الزیدی نخست وزیر عراق ، به اداره امور اقامت و گذرنامه دستور داده که به شهروندان ایرانی در فرودگاه نجف اجازه ورود ندهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/149455" target="_blank">📅 07:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149454">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بر اساس گزارش شبکه نیوز‌نیشن، مذاکرات غیرمستقیم جاری بین مقامات واشنگتن و تهران در نیویورک، با میانجی‌گری قطر در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/149454" target="_blank">📅 07:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JykCsFE1yeueK80ZTo9J6t6-CuK636Lmvk141kdUOcZRXaiBTsrVStW5iOmrcxKT_4SY50keA8lnllHfmUhhuUBAcgFJMuBq3v_RKBoUjWDtntgafd3f30pEimh023m6SvveZjW6Ao6OdlWBBdA3AEO9B_PXUImllBEBbg_kzYjeDi7w9kwHbAT3qhEVhGLWR-iA0ZNGdhpuUcMJlHxvXnnpWfGaDRAo4Hsbnft8fjyF97pl4VPhNsODnq79FCOk1LyLvb1gEK0j026fKAjLuhE0UJz2aKQZMHC6cqIFaI2GHgyYBM6tUfm29IqAB7eMYZpRumdrs13fpz1oVfE2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
🔥
خرید
از ربات:
@
litvpn_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149453" target="_blank">📅 01:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149452">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmAVJMwl1bk7vNm_T3Oypgcskan1Ej00JYwhSxpuu6GE7OkJSfBzkxPskbv8uRARuvi-EdIx9cVa-c5B39gEhUB63eRT7u0OiwH-f5GDzao20k25hMezbNhSCqRqjcKt2I-4FbQDBeTNoavmB4o8Pf1jrnW2iigaN2zUI9upRcHlMWo0DP8K4Z1erYsom38dksyqchqpPzeBtTtHejqe6fPGq_h8oPwgHysyfrGBLw8K-4GNU16HAzuP2GzKoWzhx3eB-pIjktF-XC7w9s96tt7_-wV5Vam_WBxvQVrjiIBMMj2RVdQ6ImenjoCdhnJ3LXsbOOzRh6XNWnfjvLKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: عربستان سعودی تمام‌وقت مشغول التماس به اسرائیل برای کمک در برابر حوثی‌هاست.
🔴
اما در نهایت هیئت نمایندگی‌اش هنگام سخنرانی نتانیاهو تو سازمان ملل، جلسه رو ترک میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/149452" target="_blank">📅 01:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هشدار حمله موشکی در جیزان عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/149451" target="_blank">📅 01:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دوست دخترم میگه منو میگیری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/149450" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دقایقی قبل اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/149449" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💢
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
💢
مهلت هفت‌روزه از زمانی آغاز می‌شود که ایالات متحده این برنامه را بپذیرد. اگر این اتفاق فردا رخ دهد، اجرای برنامه از همان زمان آغاز خواهد شد.
💢
در صورت انجام اقدامات لازم، معتقدیم…</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/149448" target="_blank">📅 01:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhVmR6ZA_oAmbES_rXGPNy27Z5nubt393Lw0MyfTHvoWzXULJse5DKvqNKkAT0HG8Vhvmn17b5xOCD_xMljMDWvTJXNrgDc2J5X1A9eNL5gMvHvtdWRXQdoH0DLTiM-FtobDBmW7bYeKbM6VnWM980wNFRfiXL8OEgG2DikH_7lUBoe_nGnadFH-ejR4hsHMbPevB__yIrt8a5kEHHXm4Az1fO4TK1krGhhQcC-ZV8HI-cmbf3n6aK-HxmO0Hmzo-PVyr4WlW3O489sQma3At4eHKSQbG2hz3EQIBaTSP3J4EAEn5-rA9jmPA-R1yfJTsT7wrH64TETbUGyINow_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی‌زاده
:
دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/149447" target="_blank">📅 01:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع امنیتی ایران: خبرسازی رسانه‌های غربی در رابطه با مذاکرات کذب است
🔴
ایران شروط ۷گانه خود را به طرف امریکایی ابلاغ کرد و توپ در زمین آمریکا است.
🔴
دلیل بسته ماندن تنگه هرمز عدم اجرای تعهدات از سوی آمریکایی ها است و همانطور که پیش از این مشخص شده است تنگه هرمز با توییت، خبرسازی رسانه‌های نزدیک به کاخ سفید و فشار هرگز باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/149446" target="_blank">📅 00:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/149445" target="_blank">📅 00:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE06p_nNLiFrCPJr3Cpcvr6nRsuP4Au8CYvrHHLwRKlrkVnK8R-2V8GUB2dyXmldWi8Rhav_JqfZsPGaDuyNJiO90uGR6kHQWqNNA6M3tXfdBFo_vjvhu1IpH56zBoNUbC16hCvd5OL7UZk74w5uBvxCKFrJ-DlMr0HQCHrXoxma0fF3wxuXRZupEuXXK4jSLsPRhZ1coUUS17tWxRcDoNZuRumqlRIwtkVgbmkUVHlDExVd3nCUSQ5DciiGOoKmwqbJWj9z9FcMKH8rkp1MPNFe0x5bjAYK4nv9ORPfm8Dx5aA9-HtDA_E8r9HRxJq9G6NA3yTWkYqKLeZLqAb74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافق شد
⁉️
🔴
خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/149443" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: ایران بر بازگشت به تفاهم‌نامه اسلام‌آباد شدیدا تأکید دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/149442" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عراقچی : ایران یک طرح مشخص و 7 روزه را به ایالات متحده ارائه کرده است. در صورت فراهم شدن شرایط به دور از فشار و تهدید، تنگه هرمز ظرف ۷ روز می‌تواند بازگشایی شود. مهلت ۷ روزه به محض پذیرش طرح پیشنهادی ما از سوی ایالات متحده آغاز می‌شود که این پیام را از طریق قطر منتقل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/149441" target="_blank">📅 00:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تلویزیون: این جنگ تمام می‌شود آمریکا هم می‌رود ما می‌مانیم و این همسایگان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/149440" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجاب استایل‌ها از حموم رفتنشون هم فیلم میزارن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/149439" target="_blank">📅 00:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/149438" target="_blank">📅 23:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دبیرکل سازمان ملل: ایران به دنبال سلاح هسته‌ای نیست
🔴
آنتونیو گوترش در دیدار با پزشکیان: صدای شما و ایران، صدای صلح و میانه‌روی بوده است.
🔴
بر اساس ارزیابی ها، معتقدم ایران به دنبال دستیابی به سلاح هسته‌ای نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/149437" target="_blank">📅 23:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی سپاه: تا تحقق هفت شرط ایران، دست از تنبیه آمریکا برنمی‌داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/149435" target="_blank">📅 23:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجۀ ترکیه در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/149434" target="_blank">📅 23:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWPFqdJ0PYufeArxJQm1SFy3yaHpHbyVyddf5YYaVfey2GGKalUAxtQMcQBraVucl89u72eiVE4hzCfkiJ5ZFBW-QfJ4aZhYD7Dayi0a39ZztTlY1u9EKOwIGjBKgQU_VqNUApfC0s4lf9z5Ak16Bo4kGTC9WKfGmhW6wnmibtiecdkqli1z7YaqGAJXcouqfT3R4T4eQsHW9_qH7e1sWxRQ843i8fzCPLM_BFTYwmN1rVd2c_JDVOnWeGNsyhxUhMzCebVz03D1EUVnhxrRWMskU2i76wDS7A-mEdlCMNy_DwtjzRLZz7YNm4L9jZ15sDYyn0bMifsTcXXP499q-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع کنندگان شبانه از دولت درخواست کردند که حقوق نمایندگان رو قطع کنید و به حساب رزمندگان واریز کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/149433" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کریستیانو امانپور، مجری ارشد سی‌ان‌ان:
وزیر خارجه قطر، محمد بن عبدالرحمن آل‌ثانی، به من گفت:
🔴
«ما در چند هفته گذشته تلاش کرده‌ایم تا دیپلماسی میان ایران و آمریکا را دوباره به مسیر اصلی بازگردانیم.»
🔴
او افزود که مذاکرات غیرمستقیم این هفته «پیشرفت‌های مثبتی» داشته است
🔴
«ما واقعاً امیدواریم که دیپلماسی پیروز شود و بتوانیم راه‌حلی پیدا کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/149432" target="_blank">📅 23:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=PuA_STwLsHnbu1uHIeJz_44T9xpX9ycAx05ssPMOUcfJ2cRVXvpLOibaboqiTy5mG9FE34bYqmk4BtJRJf21QT9CtlDThA9KF9jH2K9rg1WA5IP_W98BhHovJw4MKz8rZwctoZT1M9jG32W9zIo6pNa-bRVvbz3CipVmhDolCW_WmQ7hcm7z2392VyfZOMjg9noa__LrzZe3DkROw3wtykz3Pi1isyXdqJgjPp_I8usvzk1p-6Zs-BLd2HFds_BM98AqXDN0ht63A_ueN88FDHa1coR4GX1PnWOboaf-5r_fGPmUso04Z8ERC7iGth4dJVUBKCBOIYK0DL69cDb6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=PuA_STwLsHnbu1uHIeJz_44T9xpX9ycAx05ssPMOUcfJ2cRVXvpLOibaboqiTy5mG9FE34bYqmk4BtJRJf21QT9CtlDThA9KF9jH2K9rg1WA5IP_W98BhHovJw4MKz8rZwctoZT1M9jG32W9zIo6pNa-bRVvbz3CipVmhDolCW_WmQ7hcm7z2392VyfZOMjg9noa__LrzZe3DkROw3wtykz3Pi1isyXdqJgjPp_I8usvzk1p-6Zs-BLd2HFds_BM98AqXDN0ht63A_ueN88FDHa1coR4GX1PnWOboaf-5r_fGPmUso04Z8ERC7iGth4dJVUBKCBOIYK0DL69cDb6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعارهای امروز پیر پاتال‌ها مقابل منزل حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/149431" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ایرنا ، خبر خبرنگار الجزیره درباره اعزام کارشناسان فنی به نیویورک صحت ندارد
‏
🔴
ترکیب هیئت ایرانی تغییری نکرده ‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/149430" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizz Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opGAuvB39RBwKG6C3Koh9Xyv5j2bzzm9yS04ghILaawVmUeTMyfAIH6xhzjm-D00TzedhCwEzrPtnKdAvohDWGEdTM80Z-LB-uUVXNeh8aOPWmkH2toJ_EN_Dz7kQT5bpSvXYOQAIZahJNDqCdHm406stGTyDOR_hBIK0uqLI1ze44XczACsgyjGjLF46IEdv8POv69-AqCIlvURjoQ3TqOVCd6O7OBuBn37ADEPyIB1uMuAAukUVFPeWvHqtO8taMAoCPVQtP23cBUh0SqRCmVpJu3NZyxdg4-ImxZ7sZCKU92wAWU00JPbQhT9OLu0KARQNx0OUcGqm2De69f2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💥
اتصال پایدار حتی در جنگ
💬
تعرفه ها
🔸
سرویس نیمه عزیز
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود نیمه عزیز
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس عزیز
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود عزیز
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫️
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 275,000 تومان
▫️
100 گیگ — 500,000 تومان
▫️
200 گیگ — 800,000 تومان</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/149429" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=PcHnsv6EDxVSZ5iGfEHH138Y_xAOSCplO5J1H9WViYdpU8lq81Pvqe857SYN9Cudb38bnmBsY1P1a33Kie8fcP6EkVI7ZFhkAmenPdgE5hdoC90S3HxzSOLQAA5v_k8pk7bbPJ830Tve4tDsfheSGPhyebo864rFdFPuxLwCZuRkwX-aD62YroNdeDjF-XfyzpgZUzKDRZvY6EDzErPS2b9D7ez7h6eols-hWNegLjt0z9NAj_ezkc3uOmC4N3j1w6Ojii8kSDvLokhHELgcfsXSkoBAeUwjI9Mrb2gKEfV6mMKVm2G-HrZJKpBqS6Us5VVkYfTOOSPPBN5NSzXt7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=PcHnsv6EDxVSZ5iGfEHH138Y_xAOSCplO5J1H9WViYdpU8lq81Pvqe857SYN9Cudb38bnmBsY1P1a33Kie8fcP6EkVI7ZFhkAmenPdgE5hdoC90S3HxzSOLQAA5v_k8pk7bbPJ830Tve4tDsfheSGPhyebo864rFdFPuxLwCZuRkwX-aD62YroNdeDjF-XfyzpgZUzKDRZvY6EDzErPS2b9D7ez7h6eols-hWNegLjt0z9NAj_ezkc3uOmC4N3j1w6Ojii8kSDvLokhHELgcfsXSkoBAeUwjI9Mrb2gKEfV6mMKVm2G-HrZJKpBqS6Us5VVkYfTOOSPPBN5NSzXt7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مسابقات کبدی بانوان، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش
😂
😭
@AloSport</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/149428" target="_blank">📅 22:56 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
