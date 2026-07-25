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
<img src="https://cdn4.telesco.pe/file/BC-mhdXhf2ejNninwu1tvFgBvD0nsx_gHeooRZ-GCUq-b51D7xteGBusRQoY7NZ-GAm1uVS_tvZlD19jremcmI5C_cmgv8BjGMaglf2e9jGWS3Uo8MR-x0sGxXmShgmBqrpj5feCFKiYYwnKWUwHLCt27MoEOJbnlkgPm_0rlEO9uQUsY6fu_XmRzXtSlurxkgjE1YpqprBtgXcjO3M_XiFh0gHuwV3QnIwZuwcB7QMP-AToBqPLAug2GetDhNEgelrT3r6PAAw9c6f3FfWhB0kx-x2IgeZgKRMeuTjAu75S25oFFXsxnRbLOwZ4XexJZrA5-QK6kuGEgumxy_ktuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 19:27:26</div>
<hr>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgkYvPAQh-DjN_QUclGZRnexFEBDOJPHdNhAUwzxFD0j8WH5ZfK30_nJA7a0Cp1SvwsAOcSaAdJ5BH7UD4HPuD6P7qRcy5TJYHVEq6yRmGt3G8Ih8KRbG_inBaptd4xerYnYCijnPuPtwc4kHhfgVbIG05RDHYxIScaouuV1jwzWoK7VWaNYJtiVH8PvqdMQSyAT020UuMH0nuPzx3Ecl2MsXqaWuKW6kbSKyH5ysb8UQaWCq31pP81egOEQK02SeUczNyW0J6GgQoiu-Lrc9nsd7muPgXmE2MB7ha21WXhxgSkymDqvM5sN-9HFK0whitmpKAOdjVonNrvwDmDEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZF7SicmL8dk6H75WJYkR8thwOE9yXuGHskyy500aTKw9egmgfO_OO3zTOPATvyHcjvMItp-ymD0NcAg89ncUr0QmN6NBLSvXca2DO48gecv3UoL5Yf3tJFshIHphjzMCVP04G_HkHZnRoIwzNK3oGCuSRsfzNcqpOg2Glk_8tcth776W8bJOao3yZgP4-n4cw3vpEfEFBHAii8bGPaWzZ3N_iwYFXgJ7oq9aiO_ZOOl7Urs6IgeyTWtvP1YtX3I0k7vqImYIK19vES37KSptjs3BzSdWbeH86T5Zu7gOyCgE4RvfKyKNzPTjYHkwji8nw1MiaXExhshXvOeQzxZqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=R6K2PkcaFFEsZwWN9y9TtwYu1DSGIpmXPm_-VowpQbhZrcPLFY-Rm0EXB_JqcPZitbneZcf8zBlgAsJUCSXJ3gNUEqEtz1L_sCLwdK3N8oxPvUEm2JTYNeMXS2XbDCkOsUgtA3uyqJNIl8nXUyllt_XYh_b_CEKf6g4LnaIWnMMtFhBF5OMPsQg1U0MxjsZ2LYvkJ3bh_MV6WUajlF8myddnuszYzKNeH0GG9XX0uZkp8ayTqC6SAgkwn2wBC6tdpjQNeDJZ669ebg0XnFkr8zsVXpFYvJAJ9k8A35gNPNp0xZBhg2wopW2e9caz2LHXD7DcqaMQinz9oFlwp-x8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=R6K2PkcaFFEsZwWN9y9TtwYu1DSGIpmXPm_-VowpQbhZrcPLFY-Rm0EXB_JqcPZitbneZcf8zBlgAsJUCSXJ3gNUEqEtz1L_sCLwdK3N8oxPvUEm2JTYNeMXS2XbDCkOsUgtA3uyqJNIl8nXUyllt_XYh_b_CEKf6g4LnaIWnMMtFhBF5OMPsQg1U0MxjsZ2LYvkJ3bh_MV6WUajlF8myddnuszYzKNeH0GG9XX0uZkp8ayTqC6SAgkwn2wBC6tdpjQNeDJZ669ebg0XnFkr8zsVXpFYvJAJ9k8A35gNPNp0xZBhg2wopW2e9caz2LHXD7DcqaMQinz9oFlwp-x8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=Fd06riwZDh9kTivlGyIiH79zoXQ3LyzZccPxPq-EUDeeKmHkzRFJdYNIOdhm6I7v9fuXvsfj3GgU5uEiOBCnMhvQuNMfPWV85hmrwtF-6r6gkBXZ09b1Yor7KVcqNkCKcy5b4E9vgjOw517LyCKteq6jnct46oip7-X253SQUs2JGc9Udp17QZCb20rYoRSjEeD9y3z-hDBTEG95zym5a8lRxvzR6ooHN6XskAZ4TvzAtJFCFTk0OHSMLnWbzeO1_alP2aP6AEiGdLa9H_qqeOfkCTmFQaN1pD5UVmZUzVYPAfkX3EFH84ZhZ2e19n2llxmS3U77S6ZTSfODA9cbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=Fd06riwZDh9kTivlGyIiH79zoXQ3LyzZccPxPq-EUDeeKmHkzRFJdYNIOdhm6I7v9fuXvsfj3GgU5uEiOBCnMhvQuNMfPWV85hmrwtF-6r6gkBXZ09b1Yor7KVcqNkCKcy5b4E9vgjOw517LyCKteq6jnct46oip7-X253SQUs2JGc9Udp17QZCb20rYoRSjEeD9y3z-hDBTEG95zym5a8lRxvzR6ooHN6XskAZ4TvzAtJFCFTk0OHSMLnWbzeO1_alP2aP6AEiGdLa9H_qqeOfkCTmFQaN1pD5UVmZUzVYPAfkX3EFH84ZhZ2e19n2llxmS3U77S6ZTSfODA9cbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=o7BpE4RDNI1Bh3HK-GDpQ_FEvEDxV9U7gQtwiloH0uiO0rpUgu1w9ExCSkhRpivQXLO8j90xFOAgjJSvVshhMPnwY1hHjqwPcbBrpsuRGQHEUITagND02jXBL2PQdOe0TMeYeW5u7-q8B5UTjjnuNAbCwPJPkkjxuBDsLgwLkTUyOeolv42lMC9zvHnfYJPXxEdwVyLGaRh-6ZDzSwX6Yof3GLY54m6qMODsH0Rocg4n-NmJut1ETj48eVuoX_5lnrVqkDxFDkwlZiNvdhaYyjAlzQzBdXvHGgOL6lnOzkH79u0T66MBZ-gwWvMo1V5aLm7R-XYhfrFEZeBVCM5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=o7BpE4RDNI1Bh3HK-GDpQ_FEvEDxV9U7gQtwiloH0uiO0rpUgu1w9ExCSkhRpivQXLO8j90xFOAgjJSvVshhMPnwY1hHjqwPcbBrpsuRGQHEUITagND02jXBL2PQdOe0TMeYeW5u7-q8B5UTjjnuNAbCwPJPkkjxuBDsLgwLkTUyOeolv42lMC9zvHnfYJPXxEdwVyLGaRh-6ZDzSwX6Yof3GLY54m6qMODsH0Rocg4n-NmJut1ETj48eVuoX_5lnrVqkDxFDkwlZiNvdhaYyjAlzQzBdXvHGgOL6lnOzkH79u0T66MBZ-gwWvMo1V5aLm7R-XYhfrFEZeBVCM5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=V_6ucBfx-Z4ThVIzyAggVh9qApzVFwmQi4ypAlUqUS6i-QluBsTBXeMWtH167OHEbRyhU7mlWFsm_Yt87Cy_wBMZkDO90TAU0wrqRGTrI7VdIcHIppGIchmZ1YR1uxMpDoXeGuvesr1hKlmvbyhQAGJ6tIvKaGzvmTE2RDShOCv4CZCSZ5KrQ94EkuJUf_B_y_pMgr6qSxpoV47Bmny4xNrHFqygRg19k9amf_nEt-MNRCgtEXBsr-rLFR0duUXczcHqUhEZPh5HjNjkE7b60ajU1Q-5CZ1kGwsH7lQ5n92sZ0FTqdJREHI3lTYBsPWIMX9rFoXWh-L300HP2H0eDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=V_6ucBfx-Z4ThVIzyAggVh9qApzVFwmQi4ypAlUqUS6i-QluBsTBXeMWtH167OHEbRyhU7mlWFsm_Yt87Cy_wBMZkDO90TAU0wrqRGTrI7VdIcHIppGIchmZ1YR1uxMpDoXeGuvesr1hKlmvbyhQAGJ6tIvKaGzvmTE2RDShOCv4CZCSZ5KrQ94EkuJUf_B_y_pMgr6qSxpoV47Bmny4xNrHFqygRg19k9amf_nEt-MNRCgtEXBsr-rLFR0duUXczcHqUhEZPh5HjNjkE7b60ajU1Q-5CZ1kGwsH7lQ5n92sZ0FTqdJREHI3lTYBsPWIMX9rFoXWh-L300HP2H0eDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=TfcDNyhOqAdPvzF496gF_eMYyhw1cpFIe8ZVt7XjcDgQw3YKXFV-ErXebRHGTqvtbCfSig2oXNQs11_U7h070CT7Gfyg7QYwcylS2law0SjlD3HHqlQSI6Na6U7-Fzl0YvcC8OCYepYzyg79gOC5IyWUw87Xg-Sx62bQYclU7JaEwzBQG5mVtXj1_CzZ6M_e1M_3mIVc5IKoK1Xkva7NWnxcOdK5Zmzn8ozO8M_menL0VY63hTp78UG2IyeZq19iZio-VV5M_A57XU7LCbQlfVAFi73i_CxG-Z-fQ6Nu6XkU_SskBVC2z7DOUheWMi1INruBygsBx-fdnKzZ4Bg0aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=TfcDNyhOqAdPvzF496gF_eMYyhw1cpFIe8ZVt7XjcDgQw3YKXFV-ErXebRHGTqvtbCfSig2oXNQs11_U7h070CT7Gfyg7QYwcylS2law0SjlD3HHqlQSI6Na6U7-Fzl0YvcC8OCYepYzyg79gOC5IyWUw87Xg-Sx62bQYclU7JaEwzBQG5mVtXj1_CzZ6M_e1M_3mIVc5IKoK1Xkva7NWnxcOdK5Zmzn8ozO8M_menL0VY63hTp78UG2IyeZq19iZio-VV5M_A57XU7LCbQlfVAFi73i_CxG-Z-fQ6Nu6XkU_SskBVC2z7DOUheWMi1INruBygsBx-fdnKzZ4Bg0aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=npuHGqhXtMSNtKR19oFVHAqvqS5QqUViFqoolFrUQG9G9rgiii8-wUZfdkICb9aMEwCmtQBUypPBwhAizXWAX542jc82apptitmpVSgKQfvhAVjLADbaw4p3cOFSOvcCoPM8VSkIMg1nQesqWYabsbIK1LRJ4t-Dc1KqGqSviXQsxEjpu80cxqejKNmI9tD5WqvST4ahQ3k3kZmC8O-LKc7VQdPHiwnB3w8ju3gLXbq9H3GXb9fzUAAbGXP5Ev67FMfr3OEFE8GkrVGFxdlNyORl8-kpJ45Y2boC0_7VwbrRGsUg9m85O1J5yEo1tM7hzDkbpyXvuMq-joKTHXrFjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=npuHGqhXtMSNtKR19oFVHAqvqS5QqUViFqoolFrUQG9G9rgiii8-wUZfdkICb9aMEwCmtQBUypPBwhAizXWAX542jc82apptitmpVSgKQfvhAVjLADbaw4p3cOFSOvcCoPM8VSkIMg1nQesqWYabsbIK1LRJ4t-Dc1KqGqSviXQsxEjpu80cxqejKNmI9tD5WqvST4ahQ3k3kZmC8O-LKc7VQdPHiwnB3w8ju3gLXbq9H3GXb9fzUAAbGXP5Ev67FMfr3OEFE8GkrVGFxdlNyORl8-kpJ45Y2boC0_7VwbrRGsUg9m85O1J5yEo1tM7hzDkbpyXvuMq-joKTHXrFjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU4hKJ54_8A66WjyTGsknpczwQvqc-hexRpX3B2z3w5TAQ5hzDAEMFDZ_0Fqj4fUQcjE-FsgFUeaaWCN916lBRQ7yBlb6bkY3T3MBlZuxK_dknHPEQ-hyGVghdPq6lBwJ5oyZvYb94pt3ScVdLsKH7A6EcHq_Jl2zHlA_OpZzgOo7_6bmRn0SdcTa-JepZ26EbsY_wRkVcLzD26ykimIbZT6jLWOymAQ2peZxrkNzv6wwrrRAFFE5xUDpVO2kI62iO-zYXPe2gN7MscIobfU5frxn5hOyZfLiY4XUkxFFz-qs2lHn4bktWunwdqRadfeRuZ91uuZbPJC8YxB3pzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_E8kpUaiXD10b51JYOG0OmpeMe6mmAcz51jcEruSajWcErMFWXJZVLieFuVrNil0XBRDAa5oXXbDWPazVdi8zt9gz9HAXOSxu45o1T6afuNvXyjp0bxDzp_DE-BFAY05Re31mi_FcWMRB9UOKfivG2Up3GoAJtq-xowxK6s6Zp5obBnJW-5CGL9bbYGz1mDaEriqpbhG_oP1W_r6nXsx7CCYRIj-Ydx_ldOWjF4fK7PhzxuFoPf3q7Tx-QgCFSGPl4JCHBWD66tsD4LUbzR5wJbY1nCaDWAXvam_IhBne2RLt8jEkLxH3oivqflhKTa4wZhNJRUCh7RR6Qff7Ta4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIB4v26pGjwO3YEVigZAlIjR1cIxbFCTLXHH5_5_x5Ua55Yk3MxRznMrJzx0B3g5XfMw_jm0-WsULm8zNnF-D1rReq971HjL7Uz204h30ROLYYqmOmjg1lWrwtHblni54ow6-fxWpC6b7BYuzr7gaE3816QiUlAHxL2cbi8eBvd6_AhvKX4bUY31Aa1CMGSYWEXdz6RjjcfGdPp-Cyglr_hqNCkwz-0Nc9RamKizQAYu8YArPT9-p785D1ov5IHIQEYhaLDa3G_N7Qhf9S9Bnu3tTlib5mNLO8FqoUg8abQJJ4-OfIgO8KBrKdJQHCwnOnsIuWzYdl3KahOdSRljwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=j3M83j7aH_ldKHsgK_0nuNOKlTcg1GnopmA8CllHCDEYIRKDrWEkwADrf9dC1RnB3cxBpbMyVq-L7lD16SHPkxUOjYcTkJZ5tUBMKZopjLU1BgaHK_uyO7z5fXEHVFLlisNxKVJVLzgKyE-eqNvj5MpEyRpIcx6orSAwVVszG5dMdW2kGmQJRb__W0KdCA43f-5dAv-3EMCdIHF1ygojTxxda3YuyKbOjZ8zCqv8DeCciMxR37KjxnRlWRsBSaTSHnO0DJvbJf79nhybWWSROy6p1a1kpf0ZDv_p0ZXpHP72lFFjIlmot2CHPmJ7FowIN2GJiEOxXAOGpTesEm8IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=j3M83j7aH_ldKHsgK_0nuNOKlTcg1GnopmA8CllHCDEYIRKDrWEkwADrf9dC1RnB3cxBpbMyVq-L7lD16SHPkxUOjYcTkJZ5tUBMKZopjLU1BgaHK_uyO7z5fXEHVFLlisNxKVJVLzgKyE-eqNvj5MpEyRpIcx6orSAwVVszG5dMdW2kGmQJRb__W0KdCA43f-5dAv-3EMCdIHF1ygojTxxda3YuyKbOjZ8zCqv8DeCciMxR37KjxnRlWRsBSaTSHnO0DJvbJf79nhybWWSROy6p1a1kpf0ZDv_p0ZXpHP72lFFjIlmot2CHPmJ7FowIN2GJiEOxXAOGpTesEm8IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjFTtSpHKIJFcgXofHWh7G961uc8dGjUDgtgI3zrHf7yt6zqcA_HiMtU81qtt5KyE7KpE68J6r9ZjLN7n83cP0nrHIyRxGvwpYd7GEKVIr2FKfUrByXjeb45XCapeCBE_6lesTWOt2nZ4aHaxVCejyZq121teLDT3Z8LRdeJTRMkJl5QYLDd6cThl5paE54D08v9nn5cgjrLA3kZAEwmCO0Bfo8Jp-hvaKsulddyTm3hwunp6Aa-MVRLcCSObJsstUQYy_KiUv3GSA9g8NpvCoeDCei5UJSRlASfHuY-ZVoisWt56mU31JjrVYgwnDUQpiizk5KVrv5oeQOfrMGD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3sc2FnwdXH2CUpD2EX9qoajkiTE8kLfsg8B7vCFiMQqjdjmq2Seb7dBOLNU-45EXyNmPlEIMhHVaekcZdJluRwVQSvPd3iRubc1EWvyQkaILqFjK-GyRtal3sZPpsagjj42AnO1ji8KGyvM5SjQgdM6cMxqDqm-AmeiCOD41bOT_WU6qPPcyym-dtqYC_1t6c8p1fQj6Z9kuXqJ7ohkk-RiXOAPO1KrWOKFryu7jLR1iYtB4JhcIyfdNrzzZdnJ06mN-I4TD33EaKNmLLoX2HwDZbRUQ0Z5Q_XaDqYY3_JBic5ddHi3btn0W6Wku54nzxtTdzX9dDkoM3rxHSeB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=Ext9hGPoSB2Q3r1sNVwfqry3JKrlYm1CPvC-LIobalGA2clw6T_g5_Mmgrw3p-sHT5hh5RBjkPS-ciRCPiCiDaoea8rwE-82RX31tpBHWDzVMIqOGnJo-8W7usH7zKJCcnTaXedqa4kOdA-O2H0RDmiF4lr0Ayzdv-nd40qC_6eVZCmNJ42bXHv5s4y7D-1j-wdK4MtHum3dENAhtX97a2GCQLG-usB0KXYNHR6ZMayj1j69J1QCGxZxVzeYdPpG9d6KlCc3hZoHQsjmA1FToyEBTePa6RMlccpEPtD_2XpKJo55I7eVJC2uVn9qPYkTNj8puJ2JFDHtCsq0gjBmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=Ext9hGPoSB2Q3r1sNVwfqry3JKrlYm1CPvC-LIobalGA2clw6T_g5_Mmgrw3p-sHT5hh5RBjkPS-ciRCPiCiDaoea8rwE-82RX31tpBHWDzVMIqOGnJo-8W7usH7zKJCcnTaXedqa4kOdA-O2H0RDmiF4lr0Ayzdv-nd40qC_6eVZCmNJ42bXHv5s4y7D-1j-wdK4MtHum3dENAhtX97a2GCQLG-usB0KXYNHR6ZMayj1j69J1QCGxZxVzeYdPpG9d6KlCc3hZoHQsjmA1FToyEBTePa6RMlccpEPtD_2XpKJo55I7eVJC2uVn9qPYkTNj8puJ2JFDHtCsq0gjBmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwbnuQPqxGd4NBYY0GIcUS0U9NqD_hVpq5u0QVwMG6NQsO5k6m0mdLzJ2fOmKnmYOsItq7pZ9bxLBohz2ZYpnGDYMzgx-MPQrSXp0sWEK5sCY_C9AgRMAZqfVcpY1rQG8Ri9bu5BuG2niKsv3ETzKRFsekktW-Fiw5r8LX2Xc-ooIqzdJtiOdbnFN_JKw5I3JHnU9mGj6JEWQZvMMmPynnqzv8jaAtLA_7RxCsay666HIzZj8ymjISg83ilxcOblxVxG9HmxIabq_Z-fMZpDQmzyWcksZe9PPgHY2FldLOWJ3rnJKtBidmnXSkB5pgUqDFwHAjGhn7-LEZ39ma991Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebart4w28UwhIgvYuxB-WQKX5MNDllz-OL1xjdhqsc5c2eSApGg0SuGdGAMy27JfWkJzsshS-cpkFha7of8BgjxToNhZMCOWhD4d8wmBrDJonn90xaGmsYw1mC_BWUDBdwp6arqITaChEJiiRDNxFSWkM_7ebxR9_y9tOxGOufrlC2t0Va1shH_9AkLdtJBVEmSTdoqKmXFLeqUmLpgiqwOtlH6JkAJdxLrO92KI9xiMum8aYCBEbrk4JmfyvVVCe2WXr6LMQBm4Iqn3xk7_r6XW34kW14C1VtCvJXZDJLK_7xwR50fYAdJwfb0Zf5j-JjuGH-PNMZzHgd2oXeDoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBrpc08nnJEBI0M6tKbgn4vsHJIAE5rNyFD-6VTfF5eebJw07n0-eLHhMZiHVuGKYv6u5K27ZKtbsBz-pKBJRRjY9RAI8rPMh-JskwlWcb3-wKtZIYxPnSJ1EqbNGggxHKql_BUdCjbqNm_lJ9sGYMHaEOc93ZSkbSvrNO76rE1rHvh4J8fAhN7Cm-yqNGv6FNPHT2MQGKSk40Ob4KBergc0mvq7L01c02PcIzVlfVm1MskXuxpsKZZzwbuTHw09OGf5MGsL5ZKyzFbMwyjpHre-XtB2NrbLiFlTetD4GmwfxHYy-bQdZmwkSy_hq4BwtUznK7XjwI4SX9-KPppM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCVhdU6gSpzc-6H1jDwYx1iI9Fp5STB464mSEj8RmZkB_roYi3rQrYMt1OdWPzWclIg6Ywp2lpAG-7wQjlwprdeKCS_RqWjlrarK4P4TisZ54D9kwzk8bQDRWJRRwaEb2H16O5YF9ewce-u2gsl972Ew95rsnE9h7xKT3X37XRb5T3W-W6h1RF7fq_9AFBUJuevbDK8DWAGQ-DPXRL9WbKcFDqHGKFN6IdEkHmzmSLzlwU_jRoGmBACg36N5ZQiAj84wJvk9KkcBRhlkKmeuN1xSdzrAM7W0VJS0sCpIuoHH-abgMz8G9RC4STnyny9TB61A6QN6WZKClHWkzdHUdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=k6wx5BxWhsJNZGSB_Kbj8rBoAWEmC7G2LfvYUTA8aqEcA4Y-yKqNggF-A_q58EMWq_vlR1WcoPbGhpTrKXUklfN9PnUL6CQUd8DBYctw8LCGvz6TKiWuPx6UIzMPY984bKncUS5hMjsir0gxRv6LXoHTulbDtoLFTy5T2FY0q9SIOcXIzJOVSnvZdiOV6C4fz_Fz9zV8VJuSRs0LKAtCenFXKB99fgbtGmsCnPle5k40-SoBxP8WXRpdi5g1ghPQUc0QSoNqp1E_nFlbnkQwnNWMFMJVFHYQXQzZIIBLTP4iBG79c4PU5b5qF8ND0arVJfwcymltB5_thvzV_SS2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=k6wx5BxWhsJNZGSB_Kbj8rBoAWEmC7G2LfvYUTA8aqEcA4Y-yKqNggF-A_q58EMWq_vlR1WcoPbGhpTrKXUklfN9PnUL6CQUd8DBYctw8LCGvz6TKiWuPx6UIzMPY984bKncUS5hMjsir0gxRv6LXoHTulbDtoLFTy5T2FY0q9SIOcXIzJOVSnvZdiOV6C4fz_Fz9zV8VJuSRs0LKAtCenFXKB99fgbtGmsCnPle5k40-SoBxP8WXRpdi5g1ghPQUc0QSoNqp1E_nFlbnkQwnNWMFMJVFHYQXQzZIIBLTP4iBG79c4PU5b5qF8ND0arVJfwcymltB5_thvzV_SS2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=HoOoEEipSikNS-WmZn4Vx-doS9PZGdpGH3fKrMQGyLqHqcEKeLiq-WoPTQL64_2GocZQydCFreH0RJfPqijXXHz2Jlvt6uq2RAKIzca4yKHDvXBVZZoSZ5ReW7sa_rXOJIML7u_3GKLUPMGNES45XlBOKi0_pRoMsuzC2p1c2m1bJC3772mj764iTWdxD_pcbLWmdfbDV0C4mH78-kvJKpyDXstfg1ABgf5h4j1xBmZxmC15YNlITkLxn070Il2wDIVaL604VhfvPOe40kjSVMrVZP11V1CLv2kIPn2oZHn2yGOL1CNfwPdfRXNMTOg4ptCdQwtJsGoa2TkNx1l-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=HoOoEEipSikNS-WmZn4Vx-doS9PZGdpGH3fKrMQGyLqHqcEKeLiq-WoPTQL64_2GocZQydCFreH0RJfPqijXXHz2Jlvt6uq2RAKIzca4yKHDvXBVZZoSZ5ReW7sa_rXOJIML7u_3GKLUPMGNES45XlBOKi0_pRoMsuzC2p1c2m1bJC3772mj764iTWdxD_pcbLWmdfbDV0C4mH78-kvJKpyDXstfg1ABgf5h4j1xBmZxmC15YNlITkLxn070Il2wDIVaL604VhfvPOe40kjSVMrVZP11V1CLv2kIPn2oZHn2yGOL1CNfwPdfRXNMTOg4ptCdQwtJsGoa2TkNx1l-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgPG1fj8RXJ9aPhJ-iU5RphGl-YUEU077LtF0quAPXAFWiYXsrUvJA6QD_sDYvK1wdQPqYwvBGPh3CCuWi4fLyRJ1Xdg41V6kK5b7JO7BgxPoddq1u0UO3tYRlgddk774B7m5BSsFHYCOB3Q70w97ii6iGyX0bUlTX2RDUv1LjwzihQ7ta7agJGc09JrV0w_NqVj4E46XcI7oS3NCXsdCeuC0PKuotvfqMTXdlOBn__7r8dSi9Vqt1XfI0kQbUq3ceYzh8TQTa_wZ38nspZJ9XOldMUrNrSfspbYNSQEAagOHUt_ErxhrnHw8xpMksLGgnl8QH1bm2Olny1V4Vp74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=Gp5e5P1SxhD83-VQ7ixxBVbBE-TCHihBeup37Qx-vTV-KmHMsmpLxxza-1LttE2TF6E9qOYF_0xHTz1faEeOnSYYpAIYcYndE7uZJTWD5BRsKkRBQOCljP7DpPguZQL4hRPCE7v9SUqapO9XtIDlYoIbpGhAZdkkq2rLjtIsm1gzGrbO0uBL0xcc_k03yR9cuZVMzYxZF45x4Xf5xBWCvycDQA2YQjuRfqRiwsAAEThy6tm0NjdNXrkGmVcXX2Bpc3J7_y2W6LyoMoxxViU7ZdQ6-hwje8JGnZVxoRoONy9SJ1iQNTRXWd7aeA0Th0lITVAS0-4DsxvmgGO9lbBhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=Gp5e5P1SxhD83-VQ7ixxBVbBE-TCHihBeup37Qx-vTV-KmHMsmpLxxza-1LttE2TF6E9qOYF_0xHTz1faEeOnSYYpAIYcYndE7uZJTWD5BRsKkRBQOCljP7DpPguZQL4hRPCE7v9SUqapO9XtIDlYoIbpGhAZdkkq2rLjtIsm1gzGrbO0uBL0xcc_k03yR9cuZVMzYxZF45x4Xf5xBWCvycDQA2YQjuRfqRiwsAAEThy6tm0NjdNXrkGmVcXX2Bpc3J7_y2W6LyoMoxxViU7ZdQ6-hwje8JGnZVxoRoONy9SJ1iQNTRXWd7aeA0Th0lITVAS0-4DsxvmgGO9lbBhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=kYushrIMXv95FtwAypQE66hTFdzHVIDz4gp0hvllS1pi2KRHyZbE5m4SDLlWcPAHA4nIkRxpkqectNxUnmoQmMAhXTlNuv56Be6hicCCvdiXpf5xPJkmE2HF9ICGgstsg6qfQru-a-QUvSfFvALc8iby3yaH8lPUSfRqGDBm6UT5O_4i7oZKu3c7PIBK-SiR_xCx81IMtfJCAjynOg0mNWFp5MDp75Zx6j2ZKtwmokL6QhiSFUTilVCfeWkVKB90luL1eJMZ-0isu6rmrEM5Fb08IKQQ1vfk61pl-VddCIFkC1Kwh5FnynljRTFI7uiZrTVaN8vLNNRUsXLb9-OjWI2tkNxaJPaiYJyzZP0mMmd_7tdC2ZJ6_ffTxScSQ3L0ikfU5lCUZhS4qANxJCKrBCavz49FSiq0jMgKJQosRKsHZy7kGyedwcR7SBiNTZ4pc1blxO55c0lJXeWdYTDfPvREUtpq4H0ROiIWRcZpyoL_iPmJ6-8SFJC50VoZ7tYL_A7ocv7-5PMv_pwMU7YQsEUqqUK54CLEeoCIQEV1mKk9RG-Q406iPc7J8CTfkdXn7Fjs_bOnLH3sxBdBVYIclq4IhhUBXNle2cPtgOxIVJdj6eVoQoko1w-4frPeHS2AnTBA5wCHewi2R2KOwNOqEXgSYyjHTPAYAjqboJQ267o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=kYushrIMXv95FtwAypQE66hTFdzHVIDz4gp0hvllS1pi2KRHyZbE5m4SDLlWcPAHA4nIkRxpkqectNxUnmoQmMAhXTlNuv56Be6hicCCvdiXpf5xPJkmE2HF9ICGgstsg6qfQru-a-QUvSfFvALc8iby3yaH8lPUSfRqGDBm6UT5O_4i7oZKu3c7PIBK-SiR_xCx81IMtfJCAjynOg0mNWFp5MDp75Zx6j2ZKtwmokL6QhiSFUTilVCfeWkVKB90luL1eJMZ-0isu6rmrEM5Fb08IKQQ1vfk61pl-VddCIFkC1Kwh5FnynljRTFI7uiZrTVaN8vLNNRUsXLb9-OjWI2tkNxaJPaiYJyzZP0mMmd_7tdC2ZJ6_ffTxScSQ3L0ikfU5lCUZhS4qANxJCKrBCavz49FSiq0jMgKJQosRKsHZy7kGyedwcR7SBiNTZ4pc1blxO55c0lJXeWdYTDfPvREUtpq4H0ROiIWRcZpyoL_iPmJ6-8SFJC50VoZ7tYL_A7ocv7-5PMv_pwMU7YQsEUqqUK54CLEeoCIQEV1mKk9RG-Q406iPc7J8CTfkdXn7Fjs_bOnLH3sxBdBVYIclq4IhhUBXNle2cPtgOxIVJdj6eVoQoko1w-4frPeHS2AnTBA5wCHewi2R2KOwNOqEXgSYyjHTPAYAjqboJQ267o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbfl4epeu1uSRG4LYHNyl8db9KRimbopWZNUG-_a72lV2ho_yDjZRXYH4Ku-KjIS8qqBrCCJ17LLQ4MWGfxgGcwBjGoa3NJVVEdnrdVq5L4ZLsH2zXqQGxQhRHU98MuOHZiB12SHiG-BiHvpqx0A6ski5BX5-SUzPGCcnblKCWW2mazIhHMb7nnd026KI_ylgaq8Ryeh9UAu5wqvHmHjklbfPeXqWZSPok0hkKdcY4R0GEySVChL5TzY0qVxtg5iBuk63H0aOSwo4wKm13dthD1s1vigWYVP7TlHa7LEK1R7B_A6Z2ocbc9MmkDKkMGTkS_I_TedYFu8PPr3uX5E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8-nf9YrVbTg312LfeQTf17mD2rXXalPV8W6Tn_M52n_cgdinjJnYcvHmSMK-JyV-UOiQDyPhyspybjKjDFVD5-DN2WpF_kf2bEM73fuLzL8ZD-C3EExcOnQdnb1rgfYx2tbA9r69IK_PyrCUbxP_XeuWzYS4V5m7hnXrjBT_sUO5WCnXmVcxtsqvVQgiArBipj_VP8PXo8m7DUNnV6t3E8xeXuqPZd-T2mPOun7uW4FllMAJr_pWX-Qb1LUWNg-wc_zSyqET-imB589YIGaWdML1AvtT0nyOzrPUP88DLKZqcrBTkEIDRSTVYPsrsD-yEJSmpZtyQwPX1myf0v3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCqGg5BlpVBIev5sB7AKkfQMMr6DE9fuTM3fbEn870p0lBAoy5Duy8hXwqHrDLlAJFfubktkAFDslQiNCSZSzUULokVi4UxqJ51IHtqqfgmmCINHzQGPAqGT1-6mEzHqNcIqqNufDL_VgbC7avlP4HEVC-sYdX0BfDxKWkAMGYv10tOl48ka_uTXTL32HdeX0Q6Se68g7sYcJUrJL5DZ26tNvHyMjZupYDfiMxNP56G3HyYRB7Qpqa_VxUDShKvehuqVPMG-CYUKL8lCLnObDTTiNbEM2VzR9GiRfSiXIAo8kO5nqJ1QjeGae_aBlQiRnP1xfPRuCyhVifLn_lxbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEEDY8df73EpQ3jOYhv92EZ0zxyDs-iBbWgvk7wYjNfCh0fYh2Ee8-_iAC7CDGBbY31UV_wKBDyTzlxxTq8941RSvJgQxk86-z-uIYbfIHstonM1tHOnZHn6TSC3iMDJHpGGJ8Y_bortBu8AYtLg6-0g034ezQIdCnIkN3S845ROKGfgiJRkR9pEpRp7SVdfzSqGygcLV-ImUX5oE-gsdwUC22AhwCgcv3cqagUXTm3EcdBQAiRWDEWHm0naE6lkqwvG_kOl3bLg5z9vYCh6o0lPWAHuMP2Pgmuv_OLpX8JJfSThE594qYM7B2eZ7sB5pMf5biujURqkLG3oLAAf4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=XiTmx7KHH0Ycx615hl4M4w-acfzpBt6ErgpB-knYgryVdjSa9tOfNEibVp25L87BceMOl7yTe6NSF-7Lo7H-39HGrg1f8UvE0TFd25DA--otTdU2eWoD-jQ_s3oKAsWJMoA2GAcdg9REy2zp1r9sLmRpgzggfu2O1wHw-5hFEHQOS49feGYNf_Jjruxp96M9Ut4qIA4hLEzGpQJEulslKF2GbZYKbv9tXTRwEdga1b3qmJ-2-hMTcbOhs75pJcMUbq9MJua4HClaqOOWojgyD2v2N9SgvqRM7SaACRgNv5LK9wYJM6V-dFhdDh9vK2tw5H9YCmaImJzbF5Vxr-A3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=XiTmx7KHH0Ycx615hl4M4w-acfzpBt6ErgpB-knYgryVdjSa9tOfNEibVp25L87BceMOl7yTe6NSF-7Lo7H-39HGrg1f8UvE0TFd25DA--otTdU2eWoD-jQ_s3oKAsWJMoA2GAcdg9REy2zp1r9sLmRpgzggfu2O1wHw-5hFEHQOS49feGYNf_Jjruxp96M9Ut4qIA4hLEzGpQJEulslKF2GbZYKbv9tXTRwEdga1b3qmJ-2-hMTcbOhs75pJcMUbq9MJua4HClaqOOWojgyD2v2N9SgvqRM7SaACRgNv5LK9wYJM6V-dFhdDh9vK2tw5H9YCmaImJzbF5Vxr-A3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXGIcY-YqZK9Ht2hnDWsCnHLWQqRU5Tby6sTOz6WymDfcfbjF8S1vboNRAMzqh9CKsO0jbyCHBG97YMa4mlpwuA_P1n1fi6Jaf9VjHo2JA5hx6Hs09Z3KtTOiiY5erRHvZmNkS2wclu0UWvPeFOeMiZx6UEwu0lTKLkKzZCsO4BE-0pjwU0rxxFKgHOq8CjGPSxsxqKeVUnkfz22S9Q1I9psZo7teTgVwgZN9LcCOpof2MUZA_Iotd1i6jwlDNvKpZl3F1zjppsO687uyAFaMsqDgEaWKZAQbbV5K-BhsmTwUcB5P4IkYOaSDxjpTyMpT_ZUISniOttkDlDHua4LpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jphIJd9ZAayMNxhA1LlILsnE9ocC7waqVtpppT0KiXWklls9sch0Xh-xLPw0lj5yU2P-i1vhl2Mh8RIabwk9tpJksn05zSG-Jnez1ymwsJnfpyFOuOmjClBSduklbdrF9MHFx_MriNBSfHcLUZr83yGjEy8PXABDGXXm65vOoMutMJn1mNuKL1wjaMfWAOhhT2vD4FMmY8opuq4NoKiYuxh5yZfbXSRzhlvGm7hh1iBu2iwlUpE_YiqMWbnbijVioj4FO_ZYm_7UNsrnlB2Ad5tvySKPYAiYNy0gvxayn_ofwLZU4t6-H3XGJ-3OpIEHH2azQXmYqlgKTsZpMsqJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=BgTFN5zz43-eGdaI6zXAbyRZks4DMIlkJCJZxPfe8uNB5RD7Skiv4FuGgKWgRnNW9fm2N_m2gkaUW_pkma9zPtliDP0oVmE7t-_RN1x74EYea7wk33me3v5cOPkekHaghqX5ZlHPB223-FJZD590ppUvwzTQOjRVD2mIcOkp48u8zRGLflq_RahUKH3NhxBTN0dhwYMZe0BcNzw6H2kUyIhbRFw3Ys2V8jrH5hqJ3vXVsg_mWsWNxO6i43jPjUK1Zr4vEUpZD8PabAP5Et22Ty-dZTTqxK3DEwogAb9xJh9wqtTBxNvHRH-nT7GGKgK4J4EcJQ10xr6eCWlrLgEcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=BgTFN5zz43-eGdaI6zXAbyRZks4DMIlkJCJZxPfe8uNB5RD7Skiv4FuGgKWgRnNW9fm2N_m2gkaUW_pkma9zPtliDP0oVmE7t-_RN1x74EYea7wk33me3v5cOPkekHaghqX5ZlHPB223-FJZD590ppUvwzTQOjRVD2mIcOkp48u8zRGLflq_RahUKH3NhxBTN0dhwYMZe0BcNzw6H2kUyIhbRFw3Ys2V8jrH5hqJ3vXVsg_mWsWNxO6i43jPjUK1Zr4vEUpZD8PabAP5Et22Ty-dZTTqxK3DEwogAb9xJh9wqtTBxNvHRH-nT7GGKgK4J4EcJQ10xr6eCWlrLgEcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=f1yF3zh6ZeM3SD624aCx935D2JCEEdv2vNDLbo8cki2xLj7rGWkH5ViNbSREs_9z5wYbFYAdOd_8JxeHPVCVGvP-I06I6OSfVuTvLUGqrTXMMGV7DxPDb0Vit0Kzpbd9aiGlOLlAugPWujYt1ZBECedtlSZ-yAAFAo9_XBFhmTH8dK1jWvsvVfxFuNyY0WVm7200LFO_dswqbSXMusno_1gaZiHNOZMmVm3BMK7Cb6UjI5aoGbOhC4Q-ESszb1BcPiF9kMj0HaD4r7aET-9Fqd6aF5rJ-JZuKVv2yVUOj0QXhiIHgBCckIOHpeN5ILb_huCW8FeTic1TZ95Vz-rSww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=f1yF3zh6ZeM3SD624aCx935D2JCEEdv2vNDLbo8cki2xLj7rGWkH5ViNbSREs_9z5wYbFYAdOd_8JxeHPVCVGvP-I06I6OSfVuTvLUGqrTXMMGV7DxPDb0Vit0Kzpbd9aiGlOLlAugPWujYt1ZBECedtlSZ-yAAFAo9_XBFhmTH8dK1jWvsvVfxFuNyY0WVm7200LFO_dswqbSXMusno_1gaZiHNOZMmVm3BMK7Cb6UjI5aoGbOhC4Q-ESszb1BcPiF9kMj0HaD4r7aET-9Fqd6aF5rJ-JZuKVv2yVUOj0QXhiIHgBCckIOHpeN5ILb_huCW8FeTic1TZ95Vz-rSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=T2Ifdr8qkuRBErtuTQVzL0YXksWp90QwMl0oIN5bGnFUeRYrTe5H0daIfuTTPWGv-F8TEr9vtBHBu15QbNTB5-Uo0OEmarGBbf1uGET2uXV0YxZpk-8agXtBe7arHRwh1NmW8IXQDwAQf4O8_1-dD37XIR4SYFcbx6lDwv7bVRdBdAf6-vTpcvzPo5VT5Rwm0zUYWSX7VV7Ow8ZSG48F-CFF1dwPCqu7ZzM0PCz3UxQBFUCHqva7NtSzRRhC1Zr2GUu_zA_a72W6C8N3LzB7kDMtss_0qiAcAJYNycjtGh0L5ksHTeYlPzeGFC_mqpwlgYRxLuI8J_JaLAUxxA_7AzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=T2Ifdr8qkuRBErtuTQVzL0YXksWp90QwMl0oIN5bGnFUeRYrTe5H0daIfuTTPWGv-F8TEr9vtBHBu15QbNTB5-Uo0OEmarGBbf1uGET2uXV0YxZpk-8agXtBe7arHRwh1NmW8IXQDwAQf4O8_1-dD37XIR4SYFcbx6lDwv7bVRdBdAf6-vTpcvzPo5VT5Rwm0zUYWSX7VV7Ow8ZSG48F-CFF1dwPCqu7ZzM0PCz3UxQBFUCHqva7NtSzRRhC1Zr2GUu_zA_a72W6C8N3LzB7kDMtss_0qiAcAJYNycjtGh0L5ksHTeYlPzeGFC_mqpwlgYRxLuI8J_JaLAUxxA_7AzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=lNJjqHTOz9VUXEtaUk5SnopR2T-v_Ymd10KfD8UzWjR-V_Xjgt6bN0hP7wvoHW7XKDQ9wOa2hKCpzc1eFVwi57sQ46BDL7Bhrwq1dzM337aWPcM26QzfCr2-0UiVOVTy_irhrME5fYELpAprCTEFOe9Smw5q9Y13bq43QzJh9nZtnyukNF7HcmzaGnptmlS1frd7Kg8CeJtDvcyt8WGh7l41NnqJW8oZsA7FWnW_Duvbmfl-a2CTgDMAxPp1GkvECjmmoNXTJWx9qX6wMileDlpYepFjYlMXl-fBJxUuRtZrL7v46I1AerYdz_yrCk2KyqAy9GeEmurNSzrHkxxOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=lNJjqHTOz9VUXEtaUk5SnopR2T-v_Ymd10KfD8UzWjR-V_Xjgt6bN0hP7wvoHW7XKDQ9wOa2hKCpzc1eFVwi57sQ46BDL7Bhrwq1dzM337aWPcM26QzfCr2-0UiVOVTy_irhrME5fYELpAprCTEFOe9Smw5q9Y13bq43QzJh9nZtnyukNF7HcmzaGnptmlS1frd7Kg8CeJtDvcyt8WGh7l41NnqJW8oZsA7FWnW_Duvbmfl-a2CTgDMAxPp1GkvECjmmoNXTJWx9qX6wMileDlpYepFjYlMXl-fBJxUuRtZrL7v46I1AerYdz_yrCk2KyqAy9GeEmurNSzrHkxxOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=coUjiA0F9x_fKlVDzfSxMCrx-FJsYuptC2aE5TdgMzNPEEo94Eo51kvzRbQMRZd0351B1rMW-7cSZb8x9aXaHGYJUyJrY7AVLNEpy1lfQ__nUIcBijoMRQ0K2zcg7dH8eL9G0JHffnFZ_vDnTZloK_3Xji7DatzLeecyrN4bZ9LJbcV8g1NlOkIGDstpsrD3iOE1eZ-J-8uyGuQgOEuebIj5a6MfCkJdCoMEzmbfKtlV6-p473nAD5qAEYaGvSkT8XFcfj0XDHsMpvdrgPTAt9YiO5EjwY9EpNKY1gegbQ72wEHut-PX--PpFw5oGhz14WLHIEZTeIyKqtXdZEICSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=coUjiA0F9x_fKlVDzfSxMCrx-FJsYuptC2aE5TdgMzNPEEo94Eo51kvzRbQMRZd0351B1rMW-7cSZb8x9aXaHGYJUyJrY7AVLNEpy1lfQ__nUIcBijoMRQ0K2zcg7dH8eL9G0JHffnFZ_vDnTZloK_3Xji7DatzLeecyrN4bZ9LJbcV8g1NlOkIGDstpsrD3iOE1eZ-J-8uyGuQgOEuebIj5a6MfCkJdCoMEzmbfKtlV6-p473nAD5qAEYaGvSkT8XFcfj0XDHsMpvdrgPTAt9YiO5EjwY9EpNKY1gegbQ72wEHut-PX--PpFw5oGhz14WLHIEZTeIyKqtXdZEICSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=gr_AjFWOya_-I4-Xro0rC0Zevz1laVbJT2SxW4y7KAl8ouyqw13HkCDLiNTx-j5dByxubCRo-nEmehXQpzNY-6_PJiR1_uQs8qRodDUkDmNXfTxSnTqw0h6pQ87sfoT2-NjclXcobCGWED1hCziarEBPfyK_ddZNADR6-OgzVS-vtNLdoH81RDGKd4CWKTXFbIKZuVru48eZzRhys3dZA1v4IUDYy_rbSU1WbBasalEW2Aq64q97xp7slL6blbvwzIrLQmGrY38Us4Zmdv5jmtkZJe9CiJVwtdn6-Yg0YU2Rfsh81Qdg5CXyDRMtnRPdJZb6fuoxYrMDpth4okJldw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=gr_AjFWOya_-I4-Xro0rC0Zevz1laVbJT2SxW4y7KAl8ouyqw13HkCDLiNTx-j5dByxubCRo-nEmehXQpzNY-6_PJiR1_uQs8qRodDUkDmNXfTxSnTqw0h6pQ87sfoT2-NjclXcobCGWED1hCziarEBPfyK_ddZNADR6-OgzVS-vtNLdoH81RDGKd4CWKTXFbIKZuVru48eZzRhys3dZA1v4IUDYy_rbSU1WbBasalEW2Aq64q97xp7slL6blbvwzIrLQmGrY38Us4Zmdv5jmtkZJe9CiJVwtdn6-Yg0YU2Rfsh81Qdg5CXyDRMtnRPdJZb6fuoxYrMDpth4okJldw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEJEfXaLepvvXMHj1rek1emUm2ie3BqK5opSIkDOL6NOelNKhet3jtFKTG-KW7eDn8cObHOY3RwZ2Xp72VtyRLVsjSnk9qvaz_Q19OR0ZnreOI6ctYW9Wy326ULuebqOGANUAjTjrwev2qJMMB33StxexwsAHrs46uhpgLmv6GlN66WLG0Qjl6kqdIxnQueGvOWIa728XZ-pRNj3B__wXs-lUIfcU2r3yqO0AsFqgW-eZPU2OtdE0pcHpZWZHqECmCmV8ZLbQBDBJWydgLmjqkPXM0EIWQ2t_o-0qebdk_tQoHLU8WfrgG8NY3MIUZeHarSZQ_rc6Z41ESuvQYitOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcWHXC8bL0DDkmNVKbe2Pab3EpAx0jPekDMvUOkfgCqAmFUKiAGquPIzgkSuBr2yLJJJRaMhwZjDC09o5ZmMjUuv0J0B-cteQsSarmxzPlO5HC4GVsxnOajaNHNOKuDL9ftC0LHnZNxOKMW6KPk2dz19dAtg4Bo0e_q-z78OfO-mgtIbZ-lrD7-ILzFtYmgWM-nNQi6qGzaiHoByuAwn7kg0IB9tcvk9WIZmM-Wib9EtC8nFnwuaNJ2R8cIvNn_lwG_lffYoeq7L69L__qkktLjDcNe-Pzs-OE1sF14huWS_8d4GOR1e0n_j5Ld3R1R_7zVXWIQNkM4wdFBnCxN5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZugIozd2R4AaM6wkpkJcKG8vZu7NwbuXSsi3hBa_lKVXJHcsq8pblnm9Z87sfDJOAnqMcjQvMq9Z6y8ln80MIk3U7qHXrtdJtsnQqWk80wjG8pjkoHSn109KJ6cF7QwjFIrDyoHmiEqeciWEKiC_8YKEv1Y5SBbzSyUm0KeoaXfL8ljwx1bH5BRomxD020XkuS-cOgdeaTRR1oAwrcLQTr9vLvDzJ8X21dOfaTn6JKtE_z9eUapem6qrxhNCYpxJYVa0UvUxvTaK_IkOCqI1Nq8TcQMiQZAxHzAV9Gmk-4L-P_bwlgldDb3Bg4amohCacb1I21YWaZjJ0qzbPRzY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=DVXqUgA3vnnXu1b0usibUQNBvgWWvASvhdacXab-FKO0rwyJLTeaXn6DsQulr0LoEAJtvUnmcNKwxmmZ_oM7xGkWx2Id8Nc8AHxjjfbVuSanIY5z_h2rwjJucVSqZHAMocMxueLgPOZaCWbjD96xbG-aQMYWNg7-yRhwqABMG55lB6ZARGIWdpkvf_g70tmoAi6_-mYxodXC4cAGZCNBF16fGsSr-Q4ogp9OxTv23VDiRe4uCHNV-xrF7a-OYx43EBR_SArEYazO231GFUnrZiBXJ9PAc4RDwHDcuyF9hE8FzF0AUlJKQbMTHkg8WDTMXxC2FSUEqo1luIvhK_MDDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=DVXqUgA3vnnXu1b0usibUQNBvgWWvASvhdacXab-FKO0rwyJLTeaXn6DsQulr0LoEAJtvUnmcNKwxmmZ_oM7xGkWx2Id8Nc8AHxjjfbVuSanIY5z_h2rwjJucVSqZHAMocMxueLgPOZaCWbjD96xbG-aQMYWNg7-yRhwqABMG55lB6ZARGIWdpkvf_g70tmoAi6_-mYxodXC4cAGZCNBF16fGsSr-Q4ogp9OxTv23VDiRe4uCHNV-xrF7a-OYx43EBR_SArEYazO231GFUnrZiBXJ9PAc4RDwHDcuyF9hE8FzF0AUlJKQbMTHkg8WDTMXxC2FSUEqo1luIvhK_MDDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=kDrs1vA4JM_M3-GIJ47olUFpGLuVECTll8QRkOgDUmJUTctp8iVkRRPgRDBQQzBEGp9a-ZR_4QGZVKzvSyi4ItoES4KsBNxl0stuPBM2_u_IQrpL-WdaYGVb0VywGaZNnghxB9kngzh5WD0ri9v84yzJuxMfe1dchNztsN-9I0ISN2QKZ2SUtpXX7OdBIrF4MS1ogRyzLSNq9vdGyW4VwfcT1tBjDVgVPOJTC7R_XZadAcjB-INg-XJRHh97lOdxXz6N82hGxtWhwsr_XkpJ8jCYstec9W1WAt5HCSeFBDQ_G__HraOBuvoTwq51eRUc8qXF42GwjpDdvR_x-pvcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=kDrs1vA4JM_M3-GIJ47olUFpGLuVECTll8QRkOgDUmJUTctp8iVkRRPgRDBQQzBEGp9a-ZR_4QGZVKzvSyi4ItoES4KsBNxl0stuPBM2_u_IQrpL-WdaYGVb0VywGaZNnghxB9kngzh5WD0ri9v84yzJuxMfe1dchNztsN-9I0ISN2QKZ2SUtpXX7OdBIrF4MS1ogRyzLSNq9vdGyW4VwfcT1tBjDVgVPOJTC7R_XZadAcjB-INg-XJRHh97lOdxXz6N82hGxtWhwsr_XkpJ8jCYstec9W1WAt5HCSeFBDQ_G__HraOBuvoTwq51eRUc8qXF42GwjpDdvR_x-pvcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=bnWR4mPg3FhBZJ5CTx4r05jtofF0YpvCtupns9ne-ph_Drodt253UoUu4lwprSs-rl47stZdEZLTHIi_zB3LC2ONb6dk_2gbgzBqxUUyvCsSHYFUxGTJQpY8JKdisaEzaw9vRFVFN3XaYefsKsDkPwsrpuzfKZiurb1OpwmCklehLvEHbKx1jrlTHECwq0oxXnrPQPt_Mk2wdSCwj9kxkhYHK-1hJaI8OtY6lg-Nfz3-RgiHkBK1hssDf7gM9vaZHNizjj_vaUwD7p9QXHUynyhqgF72Jh08ugcgIfkJnIVf4ZpZym6QCi-J0ia80bQ8cVx7KG5CO-JNW0orv1PIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=bnWR4mPg3FhBZJ5CTx4r05jtofF0YpvCtupns9ne-ph_Drodt253UoUu4lwprSs-rl47stZdEZLTHIi_zB3LC2ONb6dk_2gbgzBqxUUyvCsSHYFUxGTJQpY8JKdisaEzaw9vRFVFN3XaYefsKsDkPwsrpuzfKZiurb1OpwmCklehLvEHbKx1jrlTHECwq0oxXnrPQPt_Mk2wdSCwj9kxkhYHK-1hJaI8OtY6lg-Nfz3-RgiHkBK1hssDf7gM9vaZHNizjj_vaUwD7p9QXHUynyhqgF72Jh08ugcgIfkJnIVf4ZpZym6QCi-J0ia80bQ8cVx7KG5CO-JNW0orv1PIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foaEqfGJ8p_I_0L2eDuqNBkpGqZjWXaeKYS1-ykACEaFeShuVMWiz_jda2WCftfq69yOH7rEpf6xk5Fk7AIIhOiDpl_Bjp-6QA-w9YIlAiS8VvU-rdeJTNa7_9dSPoOx7ecC6jufAw_7wQRIsCcn_TpzoZWblc-p91604xnXLcCSGMObNKafGBD9KVcMJYoIxTYxsOZryWL9_650kXIG02Mf8PQ4o71Jq8EvfImAsD7Q4YoDelwxQNGO7UVFAt4xtJaEtsFCmkriEH1pZ_EEvpvNirybC2ogPr4uFCCJlt-wEygQUnJ0cF05D4kZHosfqBrGolUcB9zo5YYycpJtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=in-obg73BWodSNfvY-wrAaGhWigXwUXp1R0iv48wkRn5wAsxvcRxaPARRlRLZq2tsZ0BRoaPt05035NYJktImqRmP5MYsVtxpiqOwJTUEU1SPzbPfnEdsrVqGCypCsbySLQKts13EsrhOWUWEzGkOJleZTOEF3y4PT9Ie0PIgtfLy3_Cx4knL5zLJiC4JyUEdxLN9i7jSZpusZlj8z-ZxD81uFlJoKfIT_1edtT_PP74fnOT8xDNUwbC00nn8r2vYePztHHePpa2BsmOI3gIDMDQdGdXxnvfy4ttxgR_KZGOAJYogfkcjjjgYHGYPgGGpXDLM8cgddLfIMHT5T-4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=in-obg73BWodSNfvY-wrAaGhWigXwUXp1R0iv48wkRn5wAsxvcRxaPARRlRLZq2tsZ0BRoaPt05035NYJktImqRmP5MYsVtxpiqOwJTUEU1SPzbPfnEdsrVqGCypCsbySLQKts13EsrhOWUWEzGkOJleZTOEF3y4PT9Ie0PIgtfLy3_Cx4knL5zLJiC4JyUEdxLN9i7jSZpusZlj8z-ZxD81uFlJoKfIT_1edtT_PP74fnOT8xDNUwbC00nn8r2vYePztHHePpa2BsmOI3gIDMDQdGdXxnvfy4ttxgR_KZGOAJYogfkcjjjgYHGYPgGGpXDLM8cgddLfIMHT5T-4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=mMzE6Q60M6SgMAJPB9Z2qs1kUG5FxrL5WhWzIQXa-pqYJbTVKuliWsscSzipyhxLqC8SZ1EI3HOhUIVUFn56WC6Cg4jsBH03YUu2_ieJ0J8lhLPo2yhhW_778t13HOQPRpvIf-gNBwilmh8ovU0uukE19p6QpipY0ik0Prbn5HyNxKobNMQ5yC0p8YuPhqKwzuYPllVe50K5CKABE4GYIiQSw3cpwbiD-z0ucYDW4z3o8RT6HrRz7aM1EisqvQ9-osw41MZaeAuyEDUhLXuoa3xftPs5bLRioFtr6tGAbCdBsyWvrPMtT3OZxnbb6bZDb_1NcswyF22ZMHzxl3tHpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=mMzE6Q60M6SgMAJPB9Z2qs1kUG5FxrL5WhWzIQXa-pqYJbTVKuliWsscSzipyhxLqC8SZ1EI3HOhUIVUFn56WC6Cg4jsBH03YUu2_ieJ0J8lhLPo2yhhW_778t13HOQPRpvIf-gNBwilmh8ovU0uukE19p6QpipY0ik0Prbn5HyNxKobNMQ5yC0p8YuPhqKwzuYPllVe50K5CKABE4GYIiQSw3cpwbiD-z0ucYDW4z3o8RT6HrRz7aM1EisqvQ9-osw41MZaeAuyEDUhLXuoa3xftPs5bLRioFtr6tGAbCdBsyWvrPMtT3OZxnbb6bZDb_1NcswyF22ZMHzxl3tHpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obYmUHxegMkF9627gZEfd74AJD-86rej_okX6Cz-Xgw-0LtfzmJmvi9wWtWf9i9hUcb_5C3RE58Oozzf86idj4QOCN-8Z6ZjWcsTl33pDCyM1HY4hJ3s2PhlvKkdNmd59RMj-lJKfwuwZYWuKmN-oEJ3N9GyPxYmQuY5-phSTMht-TyPsPfz_IROO_T-BeMEMztKGfn9AHGmtNANk4NaCFIUrYaXUqyYssoA5kPHfsYUbCVw_pKAObRnSpLzvu36hysT0yirnRuAKLk__ukmxeGGOAiClKOmBfIYBJnPGQJhdqyWvo979I7OMoT4CQWVdNyzkgdv8cGdkMP6J2Uwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=jn0eKrG548DumU08dh8Vwdb0na9KEepny9wGs5GdTmVpS1tbQfco3_pnyW6V7cKdqMA4pO1ipXnH0BcWG4Gldux0EAGOOa3gANaZiJoh9nrp0uTKJObeYCH1Gs0MDDaPfBlDQ2ri1_c5rfMjHu_A_42O3PUutDAkOgFsiG9jwIfqzL8mtcsfnzKewJljBozfv_d4FHNqnZLlYWVVHU8zJ8rNfk0ztFIkXUlAvvOVZi-3LKpHY-S5_k1ol7kREzA1jz7UU2caW5btk152aRQxW0MeitmobVfFjkJ0JUinHqvwOqy1LPlSvSjYeOon9lwZ4l_8kAZxqpzfvyfOvjyS_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=jn0eKrG548DumU08dh8Vwdb0na9KEepny9wGs5GdTmVpS1tbQfco3_pnyW6V7cKdqMA4pO1ipXnH0BcWG4Gldux0EAGOOa3gANaZiJoh9nrp0uTKJObeYCH1Gs0MDDaPfBlDQ2ri1_c5rfMjHu_A_42O3PUutDAkOgFsiG9jwIfqzL8mtcsfnzKewJljBozfv_d4FHNqnZLlYWVVHU8zJ8rNfk0ztFIkXUlAvvOVZi-3LKpHY-S5_k1ol7kREzA1jz7UU2caW5btk152aRQxW0MeitmobVfFjkJ0JUinHqvwOqy1LPlSvSjYeOon9lwZ4l_8kAZxqpzfvyfOvjyS_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=P5TJpC5hMt7CYYQ0ERshAK6M6i7nu0t8ji9ZX3DsfBUgah2ZXpvihwduz_ZQNP8NvnbwldMdMlAN9mSLxGmQPfRXHDi9ddDQOrBngOsMh_en3lJ7muoQeMuG_GdkvcSh9jQ-y5c2qgldNLTFRrpgDTjFrOvW21xFx1YWf9Xrydds7Mwm4oKYAQNezZHbiyP7jR3Uu5O6mmAVpVnqvMoiZDClfH8F3vLaz8XzUK89kwsx-90kEn0srPNAU1K1r20z11tfkg2DNnNmMsvisV5ugn-PbGu8ZkMvAOAsAtBOiDIZTg7hvqQ0xqbZuyxNW6vMKp_iV4J_iOoFyJs6Zh_Byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=P5TJpC5hMt7CYYQ0ERshAK6M6i7nu0t8ji9ZX3DsfBUgah2ZXpvihwduz_ZQNP8NvnbwldMdMlAN9mSLxGmQPfRXHDi9ddDQOrBngOsMh_en3lJ7muoQeMuG_GdkvcSh9jQ-y5c2qgldNLTFRrpgDTjFrOvW21xFx1YWf9Xrydds7Mwm4oKYAQNezZHbiyP7jR3Uu5O6mmAVpVnqvMoiZDClfH8F3vLaz8XzUK89kwsx-90kEn0srPNAU1K1r20z11tfkg2DNnNmMsvisV5ugn-PbGu8ZkMvAOAsAtBOiDIZTg7hvqQ0xqbZuyxNW6vMKp_iV4J_iOoFyJs6Zh_Byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=JSJ0o91cqIBySNiT3o-tcNPBWinujijiDdnlcSlC63jtMEazxpr3aJrmRu559LqFyy4ZNa8Ru0YhZ7sz1ykZb964Ds_EU557mZi7RCtsLlvpFrA82eqALE6fcECC51tBsLEMJGPiqPFpjb4W1P_pG7I-Gyi6UaHDNyaY_P-_pVFFC_elMCkUxthTFCY8mZdARSxnTeB8tkL65vztmDLHbbEDcOwMNZsCQlEENhQ58d1xihuYQfjuhGq1FPGr6I_9N0Q7xLm5-w1Tx6qdmOVa_fzcpuzO9zQYJsNPX9v1ZayA2Crw73Zbxc8SkTJLdkip9I1pi4aphaA02gGwwrA-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=JSJ0o91cqIBySNiT3o-tcNPBWinujijiDdnlcSlC63jtMEazxpr3aJrmRu559LqFyy4ZNa8Ru0YhZ7sz1ykZb964Ds_EU557mZi7RCtsLlvpFrA82eqALE6fcECC51tBsLEMJGPiqPFpjb4W1P_pG7I-Gyi6UaHDNyaY_P-_pVFFC_elMCkUxthTFCY8mZdARSxnTeB8tkL65vztmDLHbbEDcOwMNZsCQlEENhQ58d1xihuYQfjuhGq1FPGr6I_9N0Q7xLm5-w1Tx6qdmOVa_fzcpuzO9zQYJsNPX9v1ZayA2Crw73Zbxc8SkTJLdkip9I1pi4aphaA02gGwwrA-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQhbQCsJqUNhqMPT0fSZrxC0tZEMv8wasGs1MwvD7pn0X4GeVIYYqXi3IahS9fGLVAuYlRzviWN1KecDBDOq-6RFe3LRUZGSKOz3XKz-EN4CJWta5pBSBc5yHZWT4Zyn8oE__UKR-YkgDXsjm2pk0dBDOscio6xKFAaoM57f5OCRQW_1SQcLU99RxwucdjvD1zH_qwFRx0i3u9ffLIyouPyA2upD7TG5N7NWW5wfH9paXs8976rXRphKoWIfPkk5PUdD2FyxS56xmNKgTpTexoqjn_lrBzKE3g-Ikyt7V-3xDuSXRMP78SSFTzf2JXONX1-rkP6BrfEwo79_7rj13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=Rvqof-puyIpBKH02duP8oGh3al9pKJK7rbf2UimwOcqTWs1qHFtaTZum7TUXQe4taSIHU8GvYyU2X6Gz-dcvcSyIZ8kDt9Ostrzev4a_zhYSojuYIDFpR5dh9qix-NrMp3ZHBXckxTGt6AzAveuIf9IRn7eat2DSl7mdf7uQQadJSFnPq6mB5IxIcz59Gi9qWZODm02IO7jytPiFPVmptshreeCTCyRoMGxU4LDpKqkXmw5b7OW-jejkksl8T1jgEecINrk7wAOnSV8E8bMGTJ0yGUIH36muJ-QN7Iq6CCZUmzS1oqFbdoZGUkfiR55HT3VVAzlld8A7sUpkRSX4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=Rvqof-puyIpBKH02duP8oGh3al9pKJK7rbf2UimwOcqTWs1qHFtaTZum7TUXQe4taSIHU8GvYyU2X6Gz-dcvcSyIZ8kDt9Ostrzev4a_zhYSojuYIDFpR5dh9qix-NrMp3ZHBXckxTGt6AzAveuIf9IRn7eat2DSl7mdf7uQQadJSFnPq6mB5IxIcz59Gi9qWZODm02IO7jytPiFPVmptshreeCTCyRoMGxU4LDpKqkXmw5b7OW-jejkksl8T1jgEecINrk7wAOnSV8E8bMGTJ0yGUIH36muJ-QN7Iq6CCZUmzS1oqFbdoZGUkfiR55HT3VVAzlld8A7sUpkRSX4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=G5jHErsUlY-yDIda8job_w5RxRbHv9sWJpLPTlv3GWsC0hSqVFAhcbYY6WHUZ2NTvCeDM72iJ4SRh47DTbrhYO_G2iVAuTJqejhUKa4hLIcH95h5EbM693T2xVgJI7cTiodx15yGfL1XNFhS8QeeteIGiBkfSYYMq7JaiggzO0_5RX1LTM97yCJCG0Gu7R-owSS6XTM_qnN7-9c-m1oMYvu8LddMRXWsSRx2pgddY5eZ-iixcCXR0pHYxlGfHN7CypjM7gLckqheO0CONSq7r295lfYDhESD9LkTIA6ZOQ8asERYtWqTMDBW2adHrZyLDKBR79C-dPWO7xTHSdth64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=G5jHErsUlY-yDIda8job_w5RxRbHv9sWJpLPTlv3GWsC0hSqVFAhcbYY6WHUZ2NTvCeDM72iJ4SRh47DTbrhYO_G2iVAuTJqejhUKa4hLIcH95h5EbM693T2xVgJI7cTiodx15yGfL1XNFhS8QeeteIGiBkfSYYMq7JaiggzO0_5RX1LTM97yCJCG0Gu7R-owSS6XTM_qnN7-9c-m1oMYvu8LddMRXWsSRx2pgddY5eZ-iixcCXR0pHYxlGfHN7CypjM7gLckqheO0CONSq7r295lfYDhESD9LkTIA6ZOQ8asERYtWqTMDBW2adHrZyLDKBR79C-dPWO7xTHSdth64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehY7cjh2jSbQzwdMQ0eFLPuhy5gBt9bNDTfGcxsu7cQUWD4QpIqn8xX8a3IwFLrgVn_t-0qHqgLBYXz2k9X1pGaUE6s-n9RqxitCS7gozoI1sM9Hg29Dndo1l19oGPVqFGQvrUdm7-yW-ln2wO87fDMqEd9ROdbGDeYQeVLli7mBubjFJYHIMz6cjRgjw1DUfwadtzcHGaIRcbLp1WPHLrBg1ZFeT4MDGgzcZU9cJXK2O8MhL9HDJ3eQ9rrEkRsXwk4MeCEyOt4MgVn-8ksbKts1iwHXRFAAgRgTEBIwysaLLYVoWywkxOQ2SDphwvqDbf2-TsQ4YicYsgkgVD9jBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MN5OKI6lEW6CT5O2XfTrUaJKBFWuU9mVFoIYAMCS1U4HOHYo7cg8wrZWZrgs4YHTyDldDxvvz2Ac1T5iMVbMl79uB1vJweD4_Bh9-iSPObtbRiETXj-tmivrQx8yX0Blb59cQCxXPyUECpiFCqEyMqQOAa0coXT4zN-cp97nRNEG1vCSzG8CWzH8sTt4PP0Ri4zD5feCp68zEScTyK6I43_UeOGyztKsWSKQ29IlaG6uGkfY6M3oe6KlUePdQDQ3ojGcU649BCN21_bcPd4LAnxZLtQiKGJbGSMyDdvyPEGM5wF3RldQOQTaHJg0fqunfQOhKEjoZLLIiBQcPPiUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2JY8lUzFeh46pRo_7atL-5imscBv9cZxVtP6AsYyj3dPsAjG8toVmRbkJGr-U_LeiQKPWda-y3eYx1uctLKqz9OJ5i02ihzXaFF5WsdG1ER3d28VFjT2ooaRG2BoClNwVNfrNCXhQgCV0E8f3Pa743VchEGIrmdcIeo7x_6d3sk2_gXAsIfhNqq1RO9GjrelD6JbAv0GQ1brO05pDZ9AR9MrDUxcYT-hswDAvLRa0gXOs5P65p4MzLsKz9BMxqpyux1lqQvkMI9UPlSLiOo2cmbAWN9jz8l82QskEv2xjUQ_WHrM7JcX_WC4b7Y4UD03IfonLIcbvCtas0G-c-UMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=QR441CmTV2VvOY6bD4auEdVpt9FT7bBLhSabmWQ_h-dhcNBhEmnf4AQ_UIC51127PoFQSLbaNRm1MeOEyaW2TNvzNekN6WK1_GRZlF2Dqs1QDRp3jzFS1jEZt3Ch2f0CizcyYUVnLCCZN878HVbrJZdZ3NkdykWuz6jsSZmm6l3xyO-2B8ektOHwKUoTJkOHVYbjG5bJ__0SsK7vMnVFMs6VGPixr93rer7LOxGXKLk-FNTIhDOncHMYVDvoMSQxX4EN4IaU4ds2pPa8ru2Pk3Ce-WbcAKwB63LMZqf8hvFEvaLgJcXvOD-7Duf8rIjlyJPUUOHgje70RZqlKt1LwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=QR441CmTV2VvOY6bD4auEdVpt9FT7bBLhSabmWQ_h-dhcNBhEmnf4AQ_UIC51127PoFQSLbaNRm1MeOEyaW2TNvzNekN6WK1_GRZlF2Dqs1QDRp3jzFS1jEZt3Ch2f0CizcyYUVnLCCZN878HVbrJZdZ3NkdykWuz6jsSZmm6l3xyO-2B8ektOHwKUoTJkOHVYbjG5bJ__0SsK7vMnVFMs6VGPixr93rer7LOxGXKLk-FNTIhDOncHMYVDvoMSQxX4EN4IaU4ds2pPa8ru2Pk3Ce-WbcAKwB63LMZqf8hvFEvaLgJcXvOD-7Duf8rIjlyJPUUOHgje70RZqlKt1LwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
