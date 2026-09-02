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
<img src="https://cdn4.telesco.pe/file/Z17RYuk81tmqgAh_WGWk64EVsk3jINzG7njZQdsKhucRoTdO_l8zOpUZ0CABknwXxWQzKwycZ2ZKFm_C0gTGVoDm7RWeJTj4WRHbWgFmPSKfp8eAGMB5ofmkmR5TgKb-lUnPgWZWuu7_mn1-2D1Frdj1Hc3qg2Q3QdRi5SluxacRummaZzdFDYogAeiC1uEDH2TIKQ3Zm5eF8DTmFOlwMNugIFMBfSLqNzXp3TRJxhF5RHMHND9cmwde9HL8Sf1F3qSNTBgXu4ukM7fBKQhkzbXMSrpAkV3p4QonsAnp6DrvqrmDwRyKzU0QQ-AqmbDRb4Jsf84u-gxCMr-sKO0Hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGstG3cb-Eu5QypDeIkE2SfEWVWava7UMRuNxyw73AhIyVcffL77VRwSzAwFUU6B7t3c5Hqoq2WFDcp1Ue1DvLtqsmf9UQVCtTxalHGRSXq68WToUqNNONWkbhJ0QSlvS4FE9uxhAUe0ntx_pCOf5EeoEo7UejiI4Gh1cnwGtX1FFixKRrhr5Ds6SO7c-6uvlV5Zpe4k6HieYqLnrBwgoE7SaLK1m4xYGToH5ltB9wXOwR4CVUPiAtbMttJV0hrS4yXF521Ejf8jXWyS26oMYVAZcJzZ7a8PC28bbn9d0s51OXSPvgi-PZwRH40nmYdP3yzXADLx_f6Q0se4TeXU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nFJiX2Ij31dcv4AsEg4XA5dAw8CbbTK-3x-kPidSHKQa2JC6O_DHY98AiW2D7Ly8Ma1ZxyQgvlXcxbgLbeJTXFOcdghR2P6ztPAuFwolrw6rLy-AT0by2BrQOBK5ETDmk7p4bpKGjmMs6t84KCFnC2oVLgswZmmElOGcuRTF1xQGbSHE5ruAvLCGpB-PZ6QGYdVjj6dYuUP4xuGt1p0SKesHv0onEH6r940MIIP5WcaXDclI7m0KHsYx9zx0QQWuAUmm-f5eM4ZLccD4qjzxUBF_oTinz8DRv1Fj6ky91je1mA3vQ1IXagNYStyijgv8BCRgOAPmQtqJztuEJDvkIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nFJiX2Ij31dcv4AsEg4XA5dAw8CbbTK-3x-kPidSHKQa2JC6O_DHY98AiW2D7Ly8Ma1ZxyQgvlXcxbgLbeJTXFOcdghR2P6ztPAuFwolrw6rLy-AT0by2BrQOBK5ETDmk7p4bpKGjmMs6t84KCFnC2oVLgswZmmElOGcuRTF1xQGbSHE5ruAvLCGpB-PZ6QGYdVjj6dYuUP4xuGt1p0SKesHv0onEH6r940MIIP5WcaXDclI7m0KHsYx9zx0QQWuAUmm-f5eM4ZLccD4qjzxUBF_oTinz8DRv1Fj6ky91je1mA3vQ1IXagNYStyijgv8BCRgOAPmQtqJztuEJDvkIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=OyoyABuHhD56yNuI1MTU6hwhNL8oIsdahZZqVk0A5kgFWsBYf-FB0l5xaK8S3mlHj-MaoGHUDGd-BYdkk3fyRwKULYH5wup8rImrkOjYePezP2eUwh6oB6QFGRanmtEA-oPsC2yzzT7mG6qfS-z0BQZO-cxa9Cw1et_z_c_KqkEqapwgA0m59Btk0YMBZ8fcKPjl2WAcpQspqZ5MQFBDxfDwl8K0B7aDyfpBUYfIO4nOlF9LCyA6SXDYpYk_isXOFvYkJzlKXisZikxPjXT-NoL97DMyhtYcLXCcYQR22EezmCH3WPBCPhRh545blyohAamw9ulC1SrkEnc3NYtVuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=OyoyABuHhD56yNuI1MTU6hwhNL8oIsdahZZqVk0A5kgFWsBYf-FB0l5xaK8S3mlHj-MaoGHUDGd-BYdkk3fyRwKULYH5wup8rImrkOjYePezP2eUwh6oB6QFGRanmtEA-oPsC2yzzT7mG6qfS-z0BQZO-cxa9Cw1et_z_c_KqkEqapwgA0m59Btk0YMBZ8fcKPjl2WAcpQspqZ5MQFBDxfDwl8K0B7aDyfpBUYfIO4nOlF9LCyA6SXDYpYk_isXOFvYkJzlKXisZikxPjXT-NoL97DMyhtYcLXCcYQR22EezmCH3WPBCPhRh545blyohAamw9ulC1SrkEnc3NYtVuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcuuYeuICSV1VxaR17GcxJWXaEoosg2LAdeTiqMH_JZDD8j54kf8v-O65c_ibMMpV6mMr8HgCytg4oPC2KdTaiiG0B0-x6OG_FmKGLk_BC5odNBaH21rkkQk113sTim5V5M_TxjMWw2G9dTtuxIsTF1GqXYU1sM0BY6ZZ2xhOkD-3TNbhiOsoI2EtbjUhh79JQAlDPU5VJT55Vu9J_DeGhj8h0NQZ0gjmoiYs69qy2UPlpvqKsRxVcd-z68tAmMtU8I9_C4WJM7gjwRxvkMKX-kBH0WoMXMuggn1ge24uys1meU8wkQou1dfu6S533cIMXDxOtvry6UhXkM6UdxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEA08RYVrDH4kL1jn79kOqBKdcjYovDEYlYwgUiFx35-ezlMYUI89DW0PHt0zCkiLLXKeIzjBB7FZpFlQs5XX3qJsoiHXeK_AxMIKv-_RXu0EbfUyrumpOC1dL6IMrVJa_NiHBeLUp2N65SXxwIqDHO0iBoxHP4cIjNkJ1-rrTwkL8eyMNC1CM7WMd1X_90dlYHUCZmM3D92AjbADK46spLS3wgBGG0boLGphXwOJf6Jw_NgvCzGl72q0UOEoAyoPeZM3dZ8t1gsF7WhX8ein7ZNI6f5sqHmr5K2eXzEQswl1CGWCzbWF4YL73qO8s9GO888B6o38tlrfjrKe4dnCcCdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEA08RYVrDH4kL1jn79kOqBKdcjYovDEYlYwgUiFx35-ezlMYUI89DW0PHt0zCkiLLXKeIzjBB7FZpFlQs5XX3qJsoiHXeK_AxMIKv-_RXu0EbfUyrumpOC1dL6IMrVJa_NiHBeLUp2N65SXxwIqDHO0iBoxHP4cIjNkJ1-rrTwkL8eyMNC1CM7WMd1X_90dlYHUCZmM3D92AjbADK46spLS3wgBGG0boLGphXwOJf6Jw_NgvCzGl72q0UOEoAyoPeZM3dZ8t1gsF7WhX8ein7ZNI6f5sqHmr5K2eXzEQswl1CGWCzbWF4YL73qO8s9GO888B6o38tlrfjrKe4dnCcCdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139418" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/139417" target="_blank">📅 19:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244018c05.mp4?token=Wi-qJZcDvVRNXym6_R0FoaO740YJ_GQn3KEe5rbuhzdG_hTiOT2aMRYdJjgvzLHpSeAtjira2UOH-Xo3AufTJCingj-EdehR0imjkUDCC7JHuXBTWaYCTn9DWRaLkYwBZWuyqYPoJwt2uWGCWPIXF3rcOFld4PLjkakbFiXlnWziCTRATAJWXLstTEEXrQiGWH_FTLLtHS8xb-XKlg30wiBySe22y1ITo_q6OjezxARfHJIs4k9TrKGNSNFhgN8ikCqZN49MgbslhGE_E5_QiA72BRLELCoNqL1f5kWeWapnW76ogUsv00BDehoe5OMvi0zDt3Mf2AbS3KTGOVqcdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244018c05.mp4?token=Wi-qJZcDvVRNXym6_R0FoaO740YJ_GQn3KEe5rbuhzdG_hTiOT2aMRYdJjgvzLHpSeAtjira2UOH-Xo3AufTJCingj-EdehR0imjkUDCC7JHuXBTWaYCTn9DWRaLkYwBZWuyqYPoJwt2uWGCWPIXF3rcOFld4PLjkakbFiXlnWziCTRATAJWXLstTEEXrQiGWH_FTLLtHS8xb-XKlg30wiBySe22y1ITo_q6OjezxARfHJIs4k9TrKGNSNFhgN8ikCqZN49MgbslhGE_E5_QiA72BRLELCoNqL1f5kWeWapnW76ogUsv00BDehoe5OMvi0zDt3Mf2AbS3KTGOVqcdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/139416" target="_blank">📅 18:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139415" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139414" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139413" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139412" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139411" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44157a322f.mp4?token=TkDogyvPrk5fxkkZ55u6ZTJgVKQSu2nco4UhTSBY3EfMB0mzo-5gzDQmYN2BIVaSb_v1_WZOiTdGja4eFbrgDHXmzxoduPdv7V6a5zjflKm7Le9wedE8UuEGn3DV9ZlopigoaeXkvRR3U2_V2nTL43L6D8OoCq2TvUhyRu8TewHS7X-b2BePKekud6QOxP5Rh7YDBoGHqgQHf2D5d7BJA1Wikyi65VeOmuZLcX1Nk1l85I-drYjgI87pMYvoWyQa0eLtPYPzEUkVBnKhubGAvPjNu0MUrY8R0CEfZKBTdFDJlTfGy3rgfIHC4ddzcBwzjabMh7ruSJCWcQb1Ru9IN4wbJHxtbq9WKe_sqcox2VDT-TFVHn49Izg_Byt72f1wNFFNB7cUZT_P12z_z6SMTkRfyXrsac1NPT8uc_C7tIdHDIRiN26uZPBkN1ezrMEipJUpNwfAT_JKBReyFjftcx8PbnUC_yolVCKRWydX_EifigDzaU638r4wVwi6Ya4xDZDPz5dMjZkwnZrEKSaWq-rd2T-A3qV0VXDL-ahTjbDhJBf3TRkBmAzrok3lNJz0mlAdHYZK1FFQKbfT-jsS6rc6-WPpho6N8O1M4Zcxx5vX-xDxFw0VdCk2U2qlmNji3eZjD3ScX_Ufw6hPPgD5KUw4VwWUTB_MsDxz3KGx2Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44157a322f.mp4?token=TkDogyvPrk5fxkkZ55u6ZTJgVKQSu2nco4UhTSBY3EfMB0mzo-5gzDQmYN2BIVaSb_v1_WZOiTdGja4eFbrgDHXmzxoduPdv7V6a5zjflKm7Le9wedE8UuEGn3DV9ZlopigoaeXkvRR3U2_V2nTL43L6D8OoCq2TvUhyRu8TewHS7X-b2BePKekud6QOxP5Rh7YDBoGHqgQHf2D5d7BJA1Wikyi65VeOmuZLcX1Nk1l85I-drYjgI87pMYvoWyQa0eLtPYPzEUkVBnKhubGAvPjNu0MUrY8R0CEfZKBTdFDJlTfGy3rgfIHC4ddzcBwzjabMh7ruSJCWcQb1Ru9IN4wbJHxtbq9WKe_sqcox2VDT-TFVHn49Izg_Byt72f1wNFFNB7cUZT_P12z_z6SMTkRfyXrsac1NPT8uc_C7tIdHDIRiN26uZPBkN1ezrMEipJUpNwfAT_JKBReyFjftcx8PbnUC_yolVCKRWydX_EifigDzaU638r4wVwi6Ya4xDZDPz5dMjZkwnZrEKSaWq-rd2T-A3qV0VXDL-ahTjbDhJBf3TRkBmAzrok3lNJz0mlAdHYZK1FFQKbfT-jsS6rc6-WPpho6N8O1M4Zcxx5vX-xDxFw0VdCk2U2qlmNji3eZjD3ScX_Ufw6hPPgD5KUw4VwWUTB_MsDxz3KGx2Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
مصاحبه با مادر و دختر پرسپولیسی
✅
پرسپولیس امرور برنده دربی خواهد بود؛ شک نکنید.۲-٠ استقلال را می‌بریم؛ علیپور و بیفوما گلزنی خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139410" target="_blank">📅 17:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=utbrqpXTCRrqTTGlrksfSsZ4UUQ7AYGm2rGcbeR_Ybzz8yPKrMVr0OaPRVyZlW7UscEQ6a3jSFhFv2fHkCoM_I3kXP7I09VcPxrVFz53rVIhvaufTWqDX8093IUTHNSPPlfb12LZ9rcpCbYStHv02xOq5qlCOJrxieN_WNuRrOrLx0alelo3xaOyrCzjpQUXmmQ3y3KUVhMaoxW7BFnAQjHB2juq_1gprlan3Ni3UOJqbv5Rm0WBEJkX3Op7ZMQ0qRlk11cxBnrSyUzeAV0fXVREKnDAc1CIJtmrqwebx6IRpC4nvRIH1E6x4YJLvMSQNCwtF2rY40k8G_kLRyX5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=utbrqpXTCRrqTTGlrksfSsZ4UUQ7AYGm2rGcbeR_Ybzz8yPKrMVr0OaPRVyZlW7UscEQ6a3jSFhFv2fHkCoM_I3kXP7I09VcPxrVFz53rVIhvaufTWqDX8093IUTHNSPPlfb12LZ9rcpCbYStHv02xOq5qlCOJrxieN_WNuRrOrLx0alelo3xaOyrCzjpQUXmmQ3y3KUVhMaoxW7BFnAQjHB2juq_1gprlan3Ni3UOJqbv5Rm0WBEJkX3Op7ZMQ0qRlk11cxBnrSyUzeAV0fXVREKnDAc1CIJtmrqwebx6IRpC4nvRIH1E6x4YJLvMSQNCwtF2rY40k8G_kLRyX5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
ترافیک سنگین در مسیر ورودی به سمت ورزشگاه نقش جهان اصفهان در آستانه  شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139409" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=Phm7CWxn8TQtTj23C-St8Dt-E6PpCXLREhLVGbczYvjBmaoVecZ1J1E7nDVS8YwDHii2MxYgEm6_TKwqXIX992JNM2BM0sJjBzBcNIofR9WI_D7ryb6lmBl5TfGqqkMj4M2JjJVxER25-MM19n7Pj6X9iHAglsX3xe5TwM3ZB6Tut5RMSMgTEFVk4r7ToTfR1tsj0VVkXQA21rcXn6bGSljDXD9p8zAUq3DCiXatuVGJ6i76ucclGBBandWWK0jv6KaltTI0Lv5rtjlZPaQBo2Kq-T8cz7JzmvLooIDtfwZgus7JA3TXzFYQd6l_w8tTvTQ6kaxqVVx770r7GJ0Iw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=Phm7CWxn8TQtTj23C-St8Dt-E6PpCXLREhLVGbczYvjBmaoVecZ1J1E7nDVS8YwDHii2MxYgEm6_TKwqXIX992JNM2BM0sJjBzBcNIofR9WI_D7ryb6lmBl5TfGqqkMj4M2JjJVxER25-MM19n7Pj6X9iHAglsX3xe5TwM3ZB6Tut5RMSMgTEFVk4r7ToTfR1tsj0VVkXQA21rcXn6bGSljDXD9p8zAUq3DCiXatuVGJ6i76ucclGBBandWWK0jv6KaltTI0Lv5rtjlZPaQBo2Kq-T8cz7JzmvLooIDtfwZgus7JA3TXzFYQd6l_w8tTvTQ6kaxqVVx770r7GJ0Iw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
هواداران استقلال و پرسپولیس در مسیر ورود به ورزشگاه نقش‌جهان اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139408" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282676305a.mp4?token=kEUNbcPmq-qvLisrYMZffyYnGaT9MnQAxi-lH8t7vQjKHHUCYPKbMBtohIqoELjhou4cu7iPnP9UuyZv3SIM1w7nbBXij55Djql6ShX6smEs_T4oDZvgbqcwoY5wOgMKNFXCjOhYNHSKs6lRoE8HcNVpqc59tqDpvJgoa5pA18AZdd4xMWuLuXt71S4YmKEhLqR3NmIH8Yc8hYyeAUiVeLihYUxWk8WN_ypPdV8vD1tY3pBicUoX-27PZyb7J1pi3WLKaPscwOIMZQ_oNj_j5481QKxUyrSSLpsby4x0P6C-Cshsee0Bp9dR5pPnaFr6leaIa3czqZRXZQ6mFoBr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282676305a.mp4?token=kEUNbcPmq-qvLisrYMZffyYnGaT9MnQAxi-lH8t7vQjKHHUCYPKbMBtohIqoELjhou4cu7iPnP9UuyZv3SIM1w7nbBXij55Djql6ShX6smEs_T4oDZvgbqcwoY5wOgMKNFXCjOhYNHSKs6lRoE8HcNVpqc59tqDpvJgoa5pA18AZdd4xMWuLuXt71S4YmKEhLqR3NmIH8Yc8hYyeAUiVeLihYUxWk8WN_ypPdV8vD1tY3pBicUoX-27PZyb7J1pi3WLKaPscwOIMZQ_oNj_j5481QKxUyrSSLpsby4x0P6C-Cshsee0Bp9dR5pPnaFr6leaIa3czqZRXZQ6mFoBr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور دو جیمی جامپ پرسپولیسی و انجام خوشحالی رونالدویی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139407" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=avrTLfdJ5_frlSGpu5FUsT3OZG3ZUb6udP5WOgIVZkUaICWo4qsMrs1PfPEOG6AnC270Sv2WnewcTdahFF0W8bcOGgmwhWHncfkHmfGimdhE22cRu4N1ATXvu0PLRyh0ZI8bdx6ps5WJmw0Vg9ZpQko_S1FZr9tY_mXOp0JE6GTOTUqBNJqF3Y6q9hmaMNlzYhJ-6u89nb24aBbXMyUqgyn6l7ha8FdO8AJe8MixCVewRH_49IuVs_JMKDAA_n6qi-KGL4iOXqJH9O2S3ITtnyyz344-u2EPVPsIMLq6p2hyBci08-WU7Efq4hY_d0_R71jS96NQZI9eTCsAhW4BCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=avrTLfdJ5_frlSGpu5FUsT3OZG3ZUb6udP5WOgIVZkUaICWo4qsMrs1PfPEOG6AnC270Sv2WnewcTdahFF0W8bcOGgmwhWHncfkHmfGimdhE22cRu4N1ATXvu0PLRyh0ZI8bdx6ps5WJmw0Vg9ZpQko_S1FZr9tY_mXOp0JE6GTOTUqBNJqF3Y6q9hmaMNlzYhJ-6u89nb24aBbXMyUqgyn6l7ha8FdO8AJe8MixCVewRH_49IuVs_JMKDAA_n6qi-KGL4iOXqJH9O2S3ITtnyyz344-u2EPVPsIMLq6p2hyBci08-WU7Efq4hY_d0_R71jS96NQZI9eTCsAhW4BCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139406" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=e5x0BxkFeNV3ZzxyX96os8OyumZH7D_GlAP7pkN44t5cyeY2-6-zmFcU-4AHsdYUIzJ17dbWn8XKef1TJVR5oTnYstFoLQpnGEg9b1wi1WuXKQNCzMDZRhoa2d0_aq1zuihLjGj0Bm1il9o2fnXIMP5OCC_RGgpScbTSXlkjvwTqxBQ3kgYQynaH0VGlaMg2huJbXP9SJpn-52-TvhmtZDaZ7Mcw3hOv37kb2DM3kkR5ZYv7odwR5MUFMdvCy0H4zprSc8cZs5bTz4ijkTGAxcSHObjxUjUKcbcC01T-reTOP9wGuaBZPhrsIJ7cnNi7_qVlnpcKCNNTPBMwA8I5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=e5x0BxkFeNV3ZzxyX96os8OyumZH7D_GlAP7pkN44t5cyeY2-6-zmFcU-4AHsdYUIzJ17dbWn8XKef1TJVR5oTnYstFoLQpnGEg9b1wi1WuXKQNCzMDZRhoa2d0_aq1zuihLjGj0Bm1il9o2fnXIMP5OCC_RGgpScbTSXlkjvwTqxBQ3kgYQynaH0VGlaMg2huJbXP9SJpn-52-TvhmtZDaZ7Mcw3hOv37kb2DM3kkR5ZYv7odwR5MUFMdvCy0H4zprSc8cZs5bTz4ijkTGAxcSHObjxUjUKcbcC01T-reTOP9wGuaBZPhrsIJ7cnNi7_qVlnpcKCNNTPBMwA8I5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
🔴
🔴
مروری بر بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139399" target="_blank">📅 13:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZVLxRcjYzAtdvfVD-7NY8Ex_MsrqrqTLddOip2z3L18X7Z09_vpjkVUWvGdWurK9ggJ72hMrUTZ7fN64xNxE3WubW-CsRSZCs6Ppc632mo0R7ZVlEXUwfCh8wuYNlekRTOiW-2CkaES-XrxZEmWN6WgzcXh7WGCtkKyKWHYr1dP_cHnnvHY7Bvw0husukH-wcbxIWGbDVwrQ_2QfydDa4sP3-wLdaLKo5NdvUGcVcRYRckUVIczMxYNHurdx_nMenrYqRW8X_6tSsK7JD2ozppiLj3KsmCpv3dpP6G88cXRBaSW5_I5Ay-Nju-HxPG_CDklag68g-MrCGY9TEu3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اصفهان در آستانه یک نبرد بزرگ!
⚽️
پرسپولیس و استقلال؛ دربی پایتخت در حساس‌ترین جدال فصل برای شبِ فراموش نشدنی.
[
استقلال
🔵
🆚
🔴
پرسپولیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139398" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
نتایج 19 دربی اخیر پرسپولیس و کیسه:
📊
در 19 دربی اخیر دو تیم 8 برد سهم پرسپولیس و 11 مساوی سهم دو تیم بوده، و نکته اینکه کیسه بردی نداشته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139397" target="_blank">📅 11:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139396" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=DSV8khAw2TlH4-bd4ruOzZ3_ZHabjNP1Jbueza0TCDnGrdDpRivmC20lHz-nXS2qAvtW4S6_LeL06LXv1mQ-WaJjXTxZcWG7pwobVmDxAO_ueUi_8LI9v0dKJN1CjZr8nziA39G4akFKG_k-QIGDHnXxD6msIptPmNUiPuSrQCAME1FEFoCUVK99FwYC98CXM0SmPsVFtDC2VTe_ngmqg4jJtqxnEfvT6FNftlcbVPVp5965h-_xKZKCVno7nag2itKrUjcw4QSBDE3ktt_6AqRetYcNmtw0fU7ZZp43pORk_M0c952d-1p-ODGrD1WzALfXHO51Ymvlxt0pQv6_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=DSV8khAw2TlH4-bd4ruOzZ3_ZHabjNP1Jbueza0TCDnGrdDpRivmC20lHz-nXS2qAvtW4S6_LeL06LXv1mQ-WaJjXTxZcWG7pwobVmDxAO_ueUi_8LI9v0dKJN1CjZr8nziA39G4akFKG_k-QIGDHnXxD6msIptPmNUiPuSrQCAME1FEFoCUVK99FwYC98CXM0SmPsVFtDC2VTe_ngmqg4jJtqxnEfvT6FNftlcbVPVp5965h-_xKZKCVno7nag2itKrUjcw4QSBDE3ktt_6AqRetYcNmtw0fU7ZZp43pORk_M0c952d-1p-ODGrD1WzALfXHO51Ymvlxt0pQv6_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
بهمنی، سخنگوی سازمان لیگ: 6 هزار بانوی هوادار تماشاگر دربی 107 خواهند بود/ درهای استادیوم نقش جهان ساعت 12 باز می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139395" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566218d82d.mp4?token=myi7HOvTkZ-NhYqux0xf6bCSXGFJ7OqjiLJAAZpy7Dc5ibgbL7UTTng1Vr_Fhjgf2Fer5_ZbnpvBCRTv-PWu6YkfnVzhLBa9lyLFUJxm3QcsZbtkUlFZ-KAfw4VuH5_0Z3OrGKRZMlKMTJ7qA7Fro3UAOFwRAAH0WeMzHgwpyxN57QaO82TwZnloIY0_z8vAjvwqx8ZIThf6PZ3GRJ1zGSHYwLTM3ndh8a50LBVb4qXFDsSoc0r0yotlFnuEcwUGrDah6-bCnB3KBN3qpnD04Vk0QnL9pVcE0EgPzgD7fqrxcisVhwP0Vw2c8VQcZXWGw7jY2OOyy6xJcDUCHT_WOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566218d82d.mp4?token=myi7HOvTkZ-NhYqux0xf6bCSXGFJ7OqjiLJAAZpy7Dc5ibgbL7UTTng1Vr_Fhjgf2Fer5_ZbnpvBCRTv-PWu6YkfnVzhLBa9lyLFUJxm3QcsZbtkUlFZ-KAfw4VuH5_0Z3OrGKRZMlKMTJ7qA7Fro3UAOFwRAAH0WeMzHgwpyxN57QaO82TwZnloIY0_z8vAjvwqx8ZIThf6PZ3GRJ1zGSHYwLTM3ndh8a50LBVb4qXFDsSoc0r0yotlFnuEcwUGrDah6-bCnB3KBN3qpnD04Vk0QnL9pVcE0EgPzgD7fqrxcisVhwP0Vw2c8VQcZXWGw7jY2OOyy6xJcDUCHT_WOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فیلمی وحشتناک از حمله دیشب به سیریک
🗣
بیچاره مردمان این منطقه
🖤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139394" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrInQf85wpx2bLXizLYso1gf28aaZHaZEwL9OQAGVML7TvJ8XDmnPos8mJqfKcvvpIIHAwxTTLfPbEf7utKx1uhRuk_euHumtDli6SjRFtCehv2_LFITSqpZt2MzhtvSyAdC4IIxq9kCRKDyD1riGizX640FDdNNzPKnv2toY6ber9p0uF8tGvFWXthGFmA3xHEpwfjeQjlCIEn3LwOPbvsfmBmrBD1hEL8E6szELg8KNowm2MV4oTQuxcxxz2X0uAjtBAM9iCcPknKL4RGFoeaw1ESX7JrVyX9x3_rBbK2QeBtsOW8GYmT-89xo9XQBB39w4kHbld2H08FARNlxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139393" target="_blank">📅 10:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
برای کمک به تیم ملی امید  هفته هفتم لیگ برتر فوتبال لغو شد!
✔️
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139392" target="_blank">📅 10:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4F__hm4guk-IOflj03RVxaQs1KwEYOE79gB3dENOOmC7tvWH4_3w0JFFObyxX8loi141xrmMI6xGZhPlBENfKlj4zUxNqZB1BW8btrwxrlXtl7pB6GAS70QLa7kEmwxtFajyj4EQhMWPttmn9B-L_SQoozdIInBkqp2Cqzmu2kOAiXuVAiUR0NeYkFPX2hJGGUspZgqYRNT7HOogdBRwAB1hcsWnepj5peKA6EYxTvXv7D90wLBI3IePVPKPJP1VqUGG-SBYcz7oEYDmRDEnKZUCZxvCwQSU_VWAXghohR5RkfHQU7VQQNUrFlFNHdTDuCkcWofkNKP_rbzKSH0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
تسنیم: شایعات الکی و بی مورد نسازید، دربی با حضور تماشاگران و بدون هیچ تغییری در استادیوم نقش‌جهان امروز برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139391" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihAowfYwQtGqYfYULrt6Gyhuk2bzrqUrvdPgJlLfHAredjwmNDseUns8U8ZBuRnNAX-Um5617iID_EVRciDCGZbI6sw6KmWvDkWn1W1adEbbtVCmPeUhHMjRV-f99AYj_samVQOhAbi5vbQRD-PioDZzLsZKSVf7T8S-UJbp4gCyQs-Q0aEnYOOUT1HWQ3JNlHL3SCTfeORIAxe0xDfub0ZVLaONvp9sJIZhsBF9W8rWrCktK2VS-o8kjezZhkN5Lb2QBszcsKg4ZEVUdmGSDBNxguJHXEBnVgoaraulD-gegEk9l4vnDif340zUFjhfzZi3W-t6henhsWq8BgIeJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139389" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❤️
تکذیب شایعه برگزاری بدون تماشاگر دربی استقلال و پرسپولیس در نقش جهان
⚪️
⚪️
استاندار اصفهان شایعات مطرح‌ شده درباره برگزاری بدون تماشاگر این دیدار را تکذیب کرد و گفت: این مسابقه با حضور تماشاگران و طبق روال پیش‌بینی‌ شده برگزار می‌شود./ مهر
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139388" target="_blank">📅 09:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
خبرهای رسیده از فدراسیون فوتبال حاکی از اینه که احتمال لغو یا برگزاری بدون تماشاگر دیدارهای فردا لیگ برتر، از جمله دربی وجود دارد
❌
❌
تصمیم نهایی به‌زودی اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139387" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🇮🇷
صبح روز دربی و پر از استرس بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139386" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB5SB77JiOzsbqKYSQERx17bc1fzE6kW252iA4OovT5RiLshmb7YwUNjKzYyEsJQjEfV4-Fmpr-17x95sx8xojalN-FTDJGxEZfm9_6mcfk_Fcl5Ji3-TJW6gP9nSvrUuJg2Nn-uUy9Qqd2Bdz1J55Hh1wtDTsDUgZUpi1dSveyYxPBGDOKCXyYlonWXctY8tdzmrJDrhE2qtZODpdGGUddyIca4rPgTkU0V5CpSTsmU7FIpUzUCrR_PU3kSWQjfDhFNL6TXmYj2OluH6HNX5OhUZ_jMOf7zWcHkq8qYL7-Kh97SVbiwejP6FxU1dFf9ZJyXI4jMY6pRwsSc34lftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
الکساندر زورف
🆚
لورنزو سونگو
🎾
آندره‌آ گِریِری
🆚
الکس د مینور
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139385" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
فووووووووووووری
🚨
شورای تامین استان اصفهان فردا 8 صبح جلسه اضطراری داره
🗣
سه سناریو پیش رو دربی پایتخت قرار داره
⏺
1_ برگزاری دربی پایتخت بدون مشکل
⏺
2_ برگزاری دربی بدون حضور تماشاگران و عودت پول بلیط به هواداران
⏺
3_ لغو دربی پایتخت و برگزاری آن…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139384" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/139383" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
ترکیب احتمالی پرسپولیس:           ‌‌‌‌‌   نیازمند تیکدری زارع کنعانی عیدی  ‌‌‌    پورعلی خدابنده‌لو ‌‌‌    عمری بیفوما محبی      ‌‌‌‌‌‌‌‌       علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139382" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139381" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
در صورت بالا رفتن درگیری ها، احتمال لغو پروازهای داخلی وجود دارد و از این رو تیم ها برای سفر به اصفهان باید برنامه خود را تغیبر داده و با اتوبوس راهی این شهر برای انجام دربی شوند
✔️
✔️
البته تا این لحظه خبری مبنی بر لغو پروازها مخابره نشده است///طاهرخانی…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/139380" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
تموم شد
✔️
اولین توقف تراکتور تو قزوین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139379" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-0lBvwmvQszQQo1vz9OdHVfwMX9Y_6H_2eOyRRlVKIioPNR3D894mgZHrHcTdMoWAj860U3H2e6CFPSYMXxiyCKiOx4REO04RMl4slsHh90qNwGepd53Xx3KhxPKdP41d629oZWTpve0HexQEeN0MZMFg_osrlUON_j5aRycHNfPXR7Kg-TCnKLJKRoPDnvs0GKEP3p8lVgKbIp0NNFt-BzyWr6oQ6qlx6t32Xrv_zN2f8Wp-0hGhB32o6DWqanbuW1ze3QJ_fZ1p8wj_NHXOzdt7xT5NJiHjyeLGYN45Uh9GUSMv5lcfRUPnjBTYymyuNhdawpMz5Y2vfI_xkRiI5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-0lBvwmvQszQQo1vz9OdHVfwMX9Y_6H_2eOyRRlVKIioPNR3D894mgZHrHcTdMoWAj860U3H2e6CFPSYMXxiyCKiOx4REO04RMl4slsHh90qNwGepd53Xx3KhxPKdP41d629oZWTpve0HexQEeN0MZMFg_osrlUON_j5aRycHNfPXR7Kg-TCnKLJKRoPDnvs0GKEP3p8lVgKbIp0NNFt-BzyWr6oQ6qlx6t32Xrv_zN2f8Wp-0hGhB32o6DWqanbuW1ze3QJ_fZ1p8wj_NHXOzdt7xT5NJiHjyeLGYN45Uh9GUSMv5lcfRUPnjBTYymyuNhdawpMz5Y2vfI_xkRiI5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
⚽️
❤️
حمله شجاع خلیل زاده به عادل فردوسی پور: من دو سال است که فحش می‌خورم اما خم به ابرو نیوردم، فشارهای زیادی روی منه و خدا رو شاهد میگیرم که یزمانی می‌خواستم از فوتبال خداحافظی کنم اما این کار رو نجام ندادم، دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور
🔻
همه مردم تبریز می‌دونن عادل فردوسی‌پور با تراکتور مشکل داره از زمان برنامه 90 همین بود، الان هم همین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/139378" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139377" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139376" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
سهراب بختیاری‌زاده: می‌خواهیم ریتم خوب شروع لیگ را ادامه دهیم و پرسپولیس حریف خوبی است که به امید خدا بتوانیم آن‌ها را شکست دهیم و با روحیه بالاتر راهی لیگ نخبگان شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139375" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
تراکتورسازی تا دقیقه ۷۷ نتونسته به شمس آذر گلی بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/139374" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/139373" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/139372" target="_blank">📅 20:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔻
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود.
🔻
ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/139371" target="_blank">📅 20:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به کنفرانس مطبوعاتی نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139370" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139369" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
فوری/حملات آمریکا شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139368" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139367" target="_blank">📅 20:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th4JYDr_uO62rn-7Rga9BX8ey0nMLAIZKS_hZEceLoueJFDczuaiVkoBTASM62oTP7GX2S0E3Lf00Ku80xoL2l_jcN7pF_dzK0Y4lQ8JtfE_EbjxHTOMQPLASNBRAcah7KpCscUM6Mg4-BlBemf3nTWyOIesKSfQfI18OkVJoOa6muMOLVmve_iQF0Y8GbG6D0cHDKZ4jPJHKMKI0GA3kGF9WRDGBHwRR-pZSYmp1AjFeDLXWAGNRyHyBPOBs9Xkd2cnkJ4Sx-YJE7p3g5l305DZHkDknRcCqSzTCQTwDEVJWj5HPOS_jWXOierOqdmsblxnuuEk-m8hDkJC1yXgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
نبردی برای صدرنشینی!
⚽️
الهلال و الاهلی؛ جدال غول‌های عربستان
سه امتیاز، هدف مشترک دو مدعی.
[
الهلال
⚽️
🆚
⚽️
الاهلی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139366" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes   ﻿</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139365" target="_blank">📅 18:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
با اعلام کمیته انضباطی قرارداد یاسر آسانی با استقلال قانونی است و مشکلی برای همراهی این تیم ندارد
✔️
البته خب انتظار دیگه ای هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139364" target="_blank">📅 18:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlEnchP45UlTKxV0i2es2hJG-Ufq47dI1Gc88d_Q-32mA-ssvSHR08beqd2lx9wm3FFRK3xAaPcJQaNAA5JD14dmWqfsiAyvvx4kV6Qnd57pA8Vd6hr-bYRKDUTxuJZoLR3-2x5rsSvPa1sXtKeiZ-ayJ41Leq7vt_UNRmAuv8Y6ySC-4_wXyjUf8ep8IYXyJKMFjdgQDcmgdP0y6VVKFLKJOgHxmO1-FISnpJMTWnLmSTDCpg2W9xVpuiN-sXe_PxFZpLiHtr8WiGMcFGzyPa4pI-YEQ9VR49Q2xvx_yCwQ1cx_wsLNZ2yoS302duskD9Hrv2A-Nqgh31BX_8SYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139363" target="_blank">📅 17:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swW5twemfQ9RHLDljBBa22CpV8fcDi-5dh00MM3GpwaoinMlJh5aA7UD9rjLAtyMvdXoPoBWGNLdWxAJirlFjNuWnQl6OZixmdn9_a0DW8TEg6gs_TZWAs_DCE7K1mz_li-M9SLo495sn4MF11ISBAltQupND5RjTCHXCVkFHNtr4BHoeSDMtfXLFZvjhWs44PeELVpPmL2h3xWKpd5IYc0u1lzrW6_CopuYaLIXfeDRIY4QJAEBRwyntaO7tgnbcA0SEOvpZDor70VzG9Z1U2EyJvfL5Gnme_Tjblnh-Zd_5kb4SEYEz9_GBpiF7SR0AFazt4tir9nI8seVO0W1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کاروان پرسپولیس راهی اصفهان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139362" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
کاروان استقلال با تاخیر به اصفهان می‌رود
⏺
پیش‌تر قرار بود کاروان استقلال همزمان با پرسپولیس و ساعت ۱۶ با پروازی اختصاصی پایتخت را به مقصد اصفهان برای برگزاری دربی صد و هفتم تهران ترک کند.
⏺
با این وجود به دلیل همزمانی حضور تیم‌ها در فرودگاه و رو‌به‌رو…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139361" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
تیم داوری دربی ۱۰۷:
⚪️
داور: موعود بنیادی‌فرد
⚪️
کمک‌داوران: علیرضا ایلدروم، بهمن عبداللهی
⚪️
داور چهارم: سیدرضا مهدوی
⚪️
ناظر: اسماعیل صفیری
⚪️
داور VAR: میثم حیدری
⚪️
کمک VAR: علی احمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139360" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139359" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
💢
💢
💢
گفته میشه تارتار قصد داره ترکیب پرسپولیس مقابل استقلال رو بازهم تغییر بده و عمری برای مهار آسانی بجای سرگیف وارد ترکیب بشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139358" target="_blank">📅 14:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139357" target="_blank">📅 14:55 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
