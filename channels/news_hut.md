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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 20:23:49</div>
<hr>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU4hKJ54_8A66WjyTGsknpczwQvqc-hexRpX3B2z3w5TAQ5hzDAEMFDZ_0Fqj4fUQcjE-FsgFUeaaWCN916lBRQ7yBlb6bkY3T3MBlZuxK_dknHPEQ-hyGVghdPq6lBwJ5oyZvYb94pt3ScVdLsKH7A6EcHq_Jl2zHlA_OpZzgOo7_6bmRn0SdcTa-JepZ26EbsY_wRkVcLzD26ykimIbZT6jLWOymAQ2peZxrkNzv6wwrrRAFFE5xUDpVO2kI62iO-zYXPe2gN7MscIobfU5frxn5hOyZfLiY4XUkxFFz-qs2lHn4bktWunwdqRadfeRuZ91uuZbPJC8YxB3pzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbxlmlZi-ERl5z6sthzJoNQlcoNlUzcg5zR9-jNDdYi7JK8lK4ViK7yXCeg-pIZ1ysnD-9VMBEVqtr_FK-QvprilpVgsTOR8-hTUAMLdBKC2ge74-CcOQcy15eu9kMMWY8sJREpXqCiqW444q6R623cw4PcVzeRWI2W-QSLbfmxyZtxHYzlEMAbI2AOgrgJ-VBZHm2KkGnS0Z28XEvz_Nw-Q-qj9XoaDOP2ZEjKvy0Suqb9grUdWd2FdSRJc_kWIRZbZoVRl7ThDd44-znTyxvNQQSMjR2vcyuFPvTDOnwatF1PmH4shv_JMZQHhnc7Izj2_ZmhJwfQJAYM6XEss7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG45us2XbhwywF2s6ZswvkRDvrKfgt6zuHXAY4dnREBLVkExRvG_YjR5tk5xdfUc4QlCidtQZtJE_yhFWD-I5Vv2zmYL_S5_rsuaTD_px7KoOD7Kx2CNCPNg8X3bYOF1m3pkU0eRa9sOzklVReFMOYYDMY-xFXVBMVbBPnGSzP6QjljIFRtYXJh36SRxZA5JwPiXdu8KeQ9ddUOL1BrnXU3nW3czBliZZzE6yAQ3mmFE4PbX7Li-xPpIx7tVPGm5DM8so4KgMPIVN0KOqsev5x7Sw538sfQUm4791XozzuACL2Dr2cbBK3hCXWGfkdN55297L0aXW63aTE9MW4h4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=esL9qJEf4jBdW9RNaoHodK4q-7lCr6fuNVBWyk-mQxHvg1l1ieD7iPZ1YS-6LgaWsx1i1VwdTCTI_qctf4cJCSREJquWw7vw4pmiL62h6F4jMrBOcg4IKBauospGgUYU5Kq_W3eIWB0gFg7kDNhhKXRRrETUVX99QrOO30gebYhJ_0kEBDOi3aqzxoWEHIsyExARktEAbaYi2IS7ZQ6jZ8ifQ2X4D4s5q57krdGPOXcDwROkXyQzqZ2txfzDw6X9asmiL0qq0F67Po9RxyheZGHK6cqXYUBny2PnQXGU59KOiYAKTj-s2Phtg2auLBr9W_HrymVEV659PxV9CQcGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=esL9qJEf4jBdW9RNaoHodK4q-7lCr6fuNVBWyk-mQxHvg1l1ieD7iPZ1YS-6LgaWsx1i1VwdTCTI_qctf4cJCSREJquWw7vw4pmiL62h6F4jMrBOcg4IKBauospGgUYU5Kq_W3eIWB0gFg7kDNhhKXRRrETUVX99QrOO30gebYhJ_0kEBDOi3aqzxoWEHIsyExARktEAbaYi2IS7ZQ6jZ8ifQ2X4D4s5q57krdGPOXcDwROkXyQzqZ2txfzDw6X9asmiL0qq0F67Po9RxyheZGHK6cqXYUBny2PnQXGU59KOiYAKTj-s2Phtg2auLBr9W_HrymVEV659PxV9CQcGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acr5Nzm_9XWMPV6oWJaMhkqLOXVHMWZvDcc04FL9YSXPEWUMIbR78zrvBwtepEhvHfDsktTCAlCvYI4jEFROfbqbDwdYzwCamPBzwhAxlSy2sUmlfLiuVu13xB45Ag8J9S711NTwPfTnzPuhxDLVFBjSvYTwnEZ7bqbnf-DbCFe1OizPlfJXprOkkIw4RQk55MYRgYAQnZKmcHwS-MwmYM1_0FK4_n50w250vjXkMNzkCgdzwhNGFh2npHUVk7qzjKxl2GD-WxwUV-SUqRg20_xY_PqnY5rV432A83FzgEc1YaygmHZdfboiYRjE-AbJpSXA-hEQxDPuSFy6-j122Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRGpLApZguT9CxnnNBZyGqXXW4eR-EZIxeIQJTcSY7x88n6jvBjxTqLUFOK1MxcnAhq3UAdzn_y0dYuo0BuHdjGTc_BelKKtEdghI692jgt46mErEyojkhE5mHIgvdty_HcmeDpn-hQ7yVcVdngpTtsMcbvst5_2_3dhSJf6olSqztGmiWkMpsg-ngvp_aw3q9zC4TQyboElJ-pzR5GLVgAj3U4ZHPtsNqF_-JqGOL8tNBG1viA7mUx5E6DTk7h2P6wic8uV89LTDeGgBBZzGb4LYvsGr72SrjwCP9Bu1ipQrDQd-27552QsejkS6la4WJXdGvRPgURP3Xy8O9bYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=vjLhL8ua0-bfQSWh-i5o0WWX2X-jexpRbWqKrWFFPVhbwj7zWxonalencGu68YACdsFc0rerVyi6Nu8NXUUf14lE19Y8JVZ8caYAjyTyR0A-_JzDjWSrOWZAMEGcUa6loiZD6_f5uNueSvctmmO9SKcuK4Rva37j99WkJcu61YyRi2hFxNduXmHAdHlMwo39e2jDHDEBiNNVLeGpMw0fz3i4RSS7Nb_-kDFFk1ep-VKtBHjNXFW9jY65-fzUCpWAUqa2NnUwnayrbLST2FalAeStxE8skvjeo6H1LCe8Vx_kNVMHp5Rd1GnYDodIRFpjRJeVFXX2UtLXl411VRC7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=vjLhL8ua0-bfQSWh-i5o0WWX2X-jexpRbWqKrWFFPVhbwj7zWxonalencGu68YACdsFc0rerVyi6Nu8NXUUf14lE19Y8JVZ8caYAjyTyR0A-_JzDjWSrOWZAMEGcUa6loiZD6_f5uNueSvctmmO9SKcuK4Rva37j99WkJcu61YyRi2hFxNduXmHAdHlMwo39e2jDHDEBiNNVLeGpMw0fz3i4RSS7Nb_-kDFFk1ep-VKtBHjNXFW9jY65-fzUCpWAUqa2NnUwnayrbLST2FalAeStxE8skvjeo6H1LCe8Vx_kNVMHp5Rd1GnYDodIRFpjRJeVFXX2UtLXl411VRC7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGwbzr9PKmLnYXqs0K2dYUVI_r_PZs_vmoZs5a4TG2wwSlHRK9sF603ZgP7b2hvgmPQwtG3dHLnWJsbzUadepWtoxyvYTLUPXZgc7DCisVx6NCypeXEeaLPRAlQOWzXf6KQUwECxxjZ05rYzjGnTST9FecPDNDRUQNghOBecXbsjfOHjkHZpe8H_hl7qQf-m2NjVWtUOEJ-zX_sHj021rYiwxf9lKnEoQymr1tj-CKBff3Te9kC3kkfXo_7AcZ54EXFmcL8WjZzU4ghI8LcF31rIJsCmBHH7U6v9UNOubPKPvQEK_GP_XXjwnws1QlzJIQLhxq-D6-c3QC2Ztfd5CQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjjO2OP9XL8nG6mqZd27gShY3Gqvc4YwcoKnqM4_syI5UtZPKylDsOxTd2l_gutTuRQGV3e_0lfqiD74IRprDNnEANsPky7g6Fdv1EcQH5nLryjcdYbfsXWKRYglCwQ1LxQJ3AGModvjvGHJ1EC0gfRQTCAUkivYtfL0UOR20jhLZPTeW2ewVkGVJ47Tt6ET7LA6eavdOHaptO1yviJA6FQiYjuwQi2upptEQ98FAd9-LoCY1bd8JIBn8VVIyY8McCHPUcyzN2wrEyHO0o41H8gC9b9sP5sUj8nLsDbreXOyIAb6pQnSuXCKBxlPHnv1Jk1wJsubHbl5xzch_CTPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUrJp7CSOxQkvUaIhsRYHcxePSKj-jqfodL9LgsnC2tac4XHTPAABDu6Q3RYTNZG0eQubAy3T664e2sttcLuqpGMzLdClBFYtiQaboUWX7jsw-JWd2zYKPSNvuXo5DmOGawFoQ3wxbX9wWtL252H6VjPibx8l2HJQVEAnFdbMVVoL80JXIewzNT1uTULucihwCL2ajyXDbqvT-tVrN8WyZsCatgDJ0cTbDgHRJxvePb8E54lPm9CvQlJ4s2KBw_YmTssb9UWueuCcnmKwL5nJohbnw1TlRiBkhvurhsXsGt0DsVPPyMHK21KNGhtf41tJbDtTuEu790ZmiSAL96V5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPtHrkNe6IICZAu7a7TUB8UJ_P5mNmDjXuAm7uYlI1zSnMl5ZFrBGTTfxjzyn8BAx20tzhok7pYkyYwL5CEQI4qhWGZYwJ_OXclKVUVFflokoFy36jU57l4mSlAnF_A3vdJl2tWJLyYvi_0TMz2R3iQO1f8rCTvmZphq8Ho8L5Z-vxQH_DBFyDN0PhxmIs-GMoMOE1iD7k2frz8Te53sv_Y1OlpTiyVEXD3bxaE5rU1yXZFIq7MA3sZS82jgf1_w7eoGQvjPmm8XUc4O2xBNSRhw3sLUa8BAejX64-WGdRSA7y0cWvFHosVAfDzbb6UtmThO5qvjAIdBQ_aVLPkjQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=vmLt9_nKcqKfwFG7Ign1IMcoZbVRKm7fWcO-bQCHoPbVH0D2YzUq6sqXdkd06Ip_sztcf5eboIuqUsiI3avYf5UUndjmN0Duc5-qdcgPzDtPZ0oZueZHxX2XSea2tlF4t_0gmZwVEOLGHs1qmBe3IFY7N66YQmMSzbX2pix8nO6JbE2hqJG3lrrXlnTVOl6HEt019MuzmgKu1TZpg5RbnXvlHs-qbBxDVo4qdTosG263SNi4yXSSVCcWSWJSD5C_d0foHdrFs53x274K2i7vy9qKJIhiqtYjCrvuio-tAVTXVM8MgGLg5fDHZOEiQJ6AVt5wkU1qPzdclck8Tp9ozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=vmLt9_nKcqKfwFG7Ign1IMcoZbVRKm7fWcO-bQCHoPbVH0D2YzUq6sqXdkd06Ip_sztcf5eboIuqUsiI3avYf5UUndjmN0Duc5-qdcgPzDtPZ0oZueZHxX2XSea2tlF4t_0gmZwVEOLGHs1qmBe3IFY7N66YQmMSzbX2pix8nO6JbE2hqJG3lrrXlnTVOl6HEt019MuzmgKu1TZpg5RbnXvlHs-qbBxDVo4qdTosG263SNi4yXSSVCcWSWJSD5C_d0foHdrFs53x274K2i7vy9qKJIhiqtYjCrvuio-tAVTXVM8MgGLg5fDHZOEiQJ6AVt5wkU1qPzdclck8Tp9ozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjNbyPyY_JROPkw0j4CrnYl7SaiCgziSl7dFXppWk1rR7ybtU-UGBkoBPqd_7e3JrhzO9Ojm29k72VhCFBAE_8epA-jKNs4L7dyv-hS0T4lOA1XvGu8K88vRBLaKfJG-7eWNi0DsrOpyMEJNiVFhrsJKnbElftUCkklDSYc-F6XmdQPmtESDPO_GZ0NWlgCe5ZBT2cGPqVokszEslPv6_sE-5v_L34JPtFEj3YOeKVHUANPqzDOiA4FxeKGgGdR2ANSFQFB2sg5RFOUtvYO1sOYgwYtzb8ik2eHZkCI1uHfSmgoz26zmO99lKyizkyK9QXqrqREjEWNly08qUzqCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=T9shiYzn-aZ_WK1g0FHlOdbfSz5g7zv0urOZW8wzjXiq9XVuB3j6mcCNTUAE_rh5kJDmHgcfqtunOEqVEpnLoBcAHJdFsbhi1fnc2-g2qBRRpbyDpAq7m6TRGHxHXnBCprfUytyrfzkK-grk7A68qs6XgNzucYB3-Z0plY3yjRy3ilaV8XB74o0mCXj1Q5TTZjNQAh1m-cxyabVPt_W62tBxnnJ2zsoR-K07AXGaRB7jT9Trh6lVzIdh93y5515IMERO_B4NeZL8p_fi9zHeZO0vBm_2fOcJXb5cw_hyjnjxcV1pqIxDsy_xU2EchLArhVQtPtTmAu0KoCpLgG6zyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=T9shiYzn-aZ_WK1g0FHlOdbfSz5g7zv0urOZW8wzjXiq9XVuB3j6mcCNTUAE_rh5kJDmHgcfqtunOEqVEpnLoBcAHJdFsbhi1fnc2-g2qBRRpbyDpAq7m6TRGHxHXnBCprfUytyrfzkK-grk7A68qs6XgNzucYB3-Z0plY3yjRy3ilaV8XB74o0mCXj1Q5TTZjNQAh1m-cxyabVPt_W62tBxnnJ2zsoR-K07AXGaRB7jT9Trh6lVzIdh93y5515IMERO_B4NeZL8p_fi9zHeZO0vBm_2fOcJXb5cw_hyjnjxcV1pqIxDsy_xU2EchLArhVQtPtTmAu0KoCpLgG6zyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=tKL5oXfY16VxXvCBubrKvSoZa-8kN0c-KOt8oLFB_NN2BUOLeGiQEsBWBLdvNTVKDYYlZcXTotTFa1Iz1yaaFBZBDlJ3N666rgNevGMVlIyW4j9O1Rr1suHEDQJym2lAk4WDFnObpZVp9sBPe_Ce3GkFlJSJaE4Vm9jMXUyXEP912BnclqFM4zGDNviAkGvRxlaNzbZHgd7tlm0ECGLX4LArBuGeFddA8u8njU4QKYvvbeyaBkiWe2zJamVH-zgWbZDvrTmaFKU52S8M8ftBLuIZ4TWPPc7x6MdeuXz0wVmxEDjSHy13wT6uw10WxepdOWq7_GT_SKX-Z__T1leVvgeDrX0GbPJXy8iweZp4WDwgWXswf1GOB-oOSxrOvfDAi0IEiD2y4FymzkC8dbRQByMsrbvC2b8P3PBay2_MVsi4hnG_NALFg79tRoLkpWJJpP6uuM6Bb4mT4HODPzONkTV51bwqOFsQfdkfFHgsQ4814k_zXI3QTW3C4iDlOQog-5L9JV56cpe4lwNfswKQseFUds1VzbEJ7X7a3gy8Xh2MulAJgm_rCtw0L2XsheeAUE1uhrQPizCpryfT-0sxij-N6jucbhZMoOr2c9-v3DW3FCKPLUyEQ5Ti4aSq2cOsD79WfQPc5RfUvdtgCh4xs2MxH4haoHIWRfGb1l5qpsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=tKL5oXfY16VxXvCBubrKvSoZa-8kN0c-KOt8oLFB_NN2BUOLeGiQEsBWBLdvNTVKDYYlZcXTotTFa1Iz1yaaFBZBDlJ3N666rgNevGMVlIyW4j9O1Rr1suHEDQJym2lAk4WDFnObpZVp9sBPe_Ce3GkFlJSJaE4Vm9jMXUyXEP912BnclqFM4zGDNviAkGvRxlaNzbZHgd7tlm0ECGLX4LArBuGeFddA8u8njU4QKYvvbeyaBkiWe2zJamVH-zgWbZDvrTmaFKU52S8M8ftBLuIZ4TWPPc7x6MdeuXz0wVmxEDjSHy13wT6uw10WxepdOWq7_GT_SKX-Z__T1leVvgeDrX0GbPJXy8iweZp4WDwgWXswf1GOB-oOSxrOvfDAi0IEiD2y4FymzkC8dbRQByMsrbvC2b8P3PBay2_MVsi4hnG_NALFg79tRoLkpWJJpP6uuM6Bb4mT4HODPzONkTV51bwqOFsQfdkfFHgsQ4814k_zXI3QTW3C4iDlOQog-5L9JV56cpe4lwNfswKQseFUds1VzbEJ7X7a3gy8Xh2MulAJgm_rCtw0L2XsheeAUE1uhrQPizCpryfT-0sxij-N6jucbhZMoOr2c9-v3DW3FCKPLUyEQ5Ti4aSq2cOsD79WfQPc5RfUvdtgCh4xs2MxH4haoHIWRfGb1l5qpsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbfl4epeu1uSRG4LYHNyl8db9KRimbopWZNUG-_a72lV2ho_yDjZRXYH4Ku-KjIS8qqBrCCJ17LLQ4MWGfxgGcwBjGoa3NJVVEdnrdVq5L4ZLsH2zXqQGxQhRHU98MuOHZiB12SHiG-BiHvpqx0A6ski5BX5-SUzPGCcnblKCWW2mazIhHMb7nnd026KI_ylgaq8Ryeh9UAu5wqvHmHjklbfPeXqWZSPok0hkKdcY4R0GEySVChL5TzY0qVxtg5iBuk63H0aOSwo4wKm13dthD1s1vigWYVP7TlHa7LEK1R7B_A6Z2ocbc9MmkDKkMGTkS_I_TedYFu8PPr3uX5E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7i4m_5tagBeaaElrKmAFCi9e-yB8H-T7vgWb449gA2tSnzjpmw1WVnIplTWYDohav_HD-xp0018hfrRAl_TPJZlXD1-fEMykx-z5N8V0wUfNg21wnu8OZoEX6Nz9oJsZ_Ns3L_ci8oGWBukfYTAbJBSKnd4Z_1M9OCFK-uUGZJLsQHj8pQyOUp8fhBSM1CfwRoMlMXkvTbmOxkDRYQtEgHdCUtlp3rcyTpOijJCET1kYuocAVvuYKp3M653ftXrHHOSj50V93H310KgIXNbT1_E6FdXvJ39u6AkIoteTYK8tnNc9kH6Hs_kYR0OPkaaSONIH1pMp-HeaZYhmXyZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrAIu7cVdrBHVDo7j-zZEN4BtJ6TMMFl4DkYkabKlLhcZUrhbOoQuNUrfZQFkZDVGTLsUwQcz4kbW9LajHm0McOExeiXfSs1skdrBILR_0tBX6FUvmJ3Mq8NEyDr0z5hTF_eNO0lkTINM8o7Qa8vzkDo5ng2SCx9ZqNIoWXQ7_VcoJ6oNNDNZ19hUQga5GPy6CWJC8o9TTnZMdbjhDLj9cMXfjbWqWY0OU84fe9QIk4PWJIfi5Co5p_qClnvebOdVM7u-UCFYl6HqI87_yYS_lYgaO8Jnlb4Du4MzTjgZnn029PpjNxhSNHyjp5EEndWnrk7i8KfH1by2blgjOBzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iepah8C-sZXQETYodXG4ekcyAWSSdKhdGO7WmPAdMGLB1mp0J98a08HdoN4T_CSInfU55LQTpErt4M4XBN55xLTpDSTgmy9wIreiNEl1pChgeg_s6QbER6kOJzYgzUHAbHpefi0HLE3ao_95lOphTM5fUaFNL588xoGqOgnn-TjgAhmvKRCUfnwsLMVRAGLP5AcLPMMha7oeEgY_k2owAj-EpCdnW4BGoiNBjWOsv5gGDYhcjMLl2yVpQFhDWKboSHW7m8u8QrPoGNXYXvDIQnJ9kfqTSrqvPFiQhmY27-c0z9cMRDmqpQsjIRaGixCu2oYDUYBCA3oTZJ1w7-mOCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=VHXIH5T3NVffwP1bp470peE-a-dPGu9KOLtAWQXMx9A3bIDBytFtn-VLm6lXu9nYQGj1x3yiKdOaot2moYsK88G_ls67F5AK9j3ViVubDk2SaXm3j-ZsPhKnitmOiBLjTGXwQAA4Ch8Gn767utkSaG9GAxtOSffGHZDiS0jYdHhEoFseWYBb131ovBOx4mBCEa4YFNP586TJGmNV-gFDIKVHJIwKpOTaa4RrQvS4fZR2axMLgaPTgdGYpPjbRiIaR756zSJgU309Zifj9RoT7s6OOvBwoc9VFt5LYiyCvnfL7YTzWE_DNovodOimZMxmiOLVs18rsA6yCXVkRVEjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=VHXIH5T3NVffwP1bp470peE-a-dPGu9KOLtAWQXMx9A3bIDBytFtn-VLm6lXu9nYQGj1x3yiKdOaot2moYsK88G_ls67F5AK9j3ViVubDk2SaXm3j-ZsPhKnitmOiBLjTGXwQAA4Ch8Gn767utkSaG9GAxtOSffGHZDiS0jYdHhEoFseWYBb131ovBOx4mBCEa4YFNP586TJGmNV-gFDIKVHJIwKpOTaa4RrQvS4fZR2axMLgaPTgdGYpPjbRiIaR756zSJgU309Zifj9RoT7s6OOvBwoc9VFt5LYiyCvnfL7YTzWE_DNovodOimZMxmiOLVs18rsA6yCXVkRVEjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlF_8W4RbDfLQlRKzWCMbk_2mrsq75nRQMFFy6eHI0Pth5YxQs6VEDTC_nVwKo5-2VisvsyKX7E3Q1QS654VeIp1bSuV_2NHbo1gWDtlsWQU6dHXIJy2ooiJwIDNE6Icy93ika3HYmLyUX9KddrzgnDlWJ8tPlmGMcfdyMmqFwKfOeDT_gCwJ4Pqy7iTyHFOFMYLU90ZsypkOHT3x6P1Y4qkjZT-j6WC_gTsGydcqtogk-Kf5qL-9dla0fCL1p7f76ex79ayZxfEYEv-nYzIeeWsTxDAGygydRsGstkdF-pC1-lLy-_5in4Nua_X_bygSkKv4n7n7E6wOGYPZ9HFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=vGOJNhZhTdn-iih1nvM-HVZgWe08EP05doDhD4Sic1AjMEmLS5dB-csDmnFVAVGiFFRLui_K65sOevpPzlf9U8lSr1Qp9iDq0InxwG8nGOw1SEdw2F3qBKS1frSiDtfUlBe93z56SC8Yn-YgZhtKNLKZeWH4Rjp6Cgd2WqoKwMUT53PH9ttbdxc-M0QBPgjkR4OnD-l-aQwZXyBAspkdtuMNB6Mze3eOLghAmGXb98I275qNGhNQvcMCFXDiLggBvnJLNW2iip9_15wVs-5ooPM-mz0hsYPZUELElfYaaQBuROtMKdzlISztdEMybCF7jiGI1dcs2IcD6_7xJVk_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=vGOJNhZhTdn-iih1nvM-HVZgWe08EP05doDhD4Sic1AjMEmLS5dB-csDmnFVAVGiFFRLui_K65sOevpPzlf9U8lSr1Qp9iDq0InxwG8nGOw1SEdw2F3qBKS1frSiDtfUlBe93z56SC8Yn-YgZhtKNLKZeWH4Rjp6Cgd2WqoKwMUT53PH9ttbdxc-M0QBPgjkR4OnD-l-aQwZXyBAspkdtuMNB6Mze3eOLghAmGXb98I275qNGhNQvcMCFXDiLggBvnJLNW2iip9_15wVs-5ooPM-mz0hsYPZUELElfYaaQBuROtMKdzlISztdEMybCF7jiGI1dcs2IcD6_7xJVk_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=To5v0ggkDnfQmaSUeC01BwJsiuUWv7-BC82grz1mWrW6FZjL9ArAcgU1gtqLSywe2xrSHWL3wKMYJHepuTFduESxt6mvCXLEG9aMO8Sv7tR-fGxv2gRPcyuqrOKp4Nrg1rgvkfhxYYZF75wWTyCffa0F0zgHLsGQeRDLa2xQt6RTrI3On_62psJ0C42hfpSv88MgdqHgmAmQ0y2sIiSmRBiaaVL9h8XpEMunCUzbR-yWDm3zttcDLVilmDTX3qrwEr59vIWB0mckS8yaeQrbYLORucr5uA2RIRqrmJ6GS_8Dfff1sQY9YRWP5334agg4_0p6_3Gyn60e0S63ASF6Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=To5v0ggkDnfQmaSUeC01BwJsiuUWv7-BC82grz1mWrW6FZjL9ArAcgU1gtqLSywe2xrSHWL3wKMYJHepuTFduESxt6mvCXLEG9aMO8Sv7tR-fGxv2gRPcyuqrOKp4Nrg1rgvkfhxYYZF75wWTyCffa0F0zgHLsGQeRDLa2xQt6RTrI3On_62psJ0C42hfpSv88MgdqHgmAmQ0y2sIiSmRBiaaVL9h8XpEMunCUzbR-yWDm3zttcDLVilmDTX3qrwEr59vIWB0mckS8yaeQrbYLORucr5uA2RIRqrmJ6GS_8Dfff1sQY9YRWP5334agg4_0p6_3Gyn60e0S63ASF6Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=Vl4ZsSebdki49UQlaLAvTSLVXQJaePMb9CvwQ5nJT44ipYL6rjS72v2TWRkaMx8dhDTFDe33ny4EMAButbYbPag3xcwWamcZJaZiNJWYpcBMfmfmX0octWBiFKIR3gQwdcS4ml8a552v0FSj2yFmYUELdh1ZalRI0r79YSt2W7p27MVT9B75gA0ooheI2e90Hx8meGTqEDRUthcACV4rg3FtgfmO0HIXElhhyGZ9JYw98JEBKklKu5Wdg-S_rksw4eOYsRxRDD2ChmeNZ68tCvp95AES0z-Eoois5deYbZy5CxfjMhhBL6NhDl4v-id5RyxX-AiQktR82vZ55W7wsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=Vl4ZsSebdki49UQlaLAvTSLVXQJaePMb9CvwQ5nJT44ipYL6rjS72v2TWRkaMx8dhDTFDe33ny4EMAButbYbPag3xcwWamcZJaZiNJWYpcBMfmfmX0octWBiFKIR3gQwdcS4ml8a552v0FSj2yFmYUELdh1ZalRI0r79YSt2W7p27MVT9B75gA0ooheI2e90Hx8meGTqEDRUthcACV4rg3FtgfmO0HIXElhhyGZ9JYw98JEBKklKu5Wdg-S_rksw4eOYsRxRDD2ChmeNZ68tCvp95AES0z-Eoois5deYbZy5CxfjMhhBL6NhDl4v-id5RyxX-AiQktR82vZ55W7wsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=RcGIHJ-CwIt8FMP8n_z75Z2Br70_N0WcCGGyqXESUyYGoXa9i74vzQRlYWBfKfY2spjD4YRqfUpg7wt1Xq6eV8ZPP83goB95SRUiYEXvJ_a3CK8PYwN4BgNzwPv_3_uIekbDPTe_cs1qSi4wvVCcF3wtnNKdRY_qVTCtFk750OQmsZqZumfNWsZBGj2g_GujHzfVlHyaar6ArEkRtmTEFO7xV92MU1c_rNCGnjN-qTNJ0airB4oV9paZPCDWx3l6_OFZ1XZclpxTSEnZrzO4lzgRQZacg1JGkLB-RB2S1MDCrWMrrPeMkYugM2d3wGWQIXRisFNUOWxhoHVsp34xOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=RcGIHJ-CwIt8FMP8n_z75Z2Br70_N0WcCGGyqXESUyYGoXa9i74vzQRlYWBfKfY2spjD4YRqfUpg7wt1Xq6eV8ZPP83goB95SRUiYEXvJ_a3CK8PYwN4BgNzwPv_3_uIekbDPTe_cs1qSi4wvVCcF3wtnNKdRY_qVTCtFk750OQmsZqZumfNWsZBGj2g_GujHzfVlHyaar6ArEkRtmTEFO7xV92MU1c_rNCGnjN-qTNJ0airB4oV9paZPCDWx3l6_OFZ1XZclpxTSEnZrzO4lzgRQZacg1JGkLB-RB2S1MDCrWMrrPeMkYugM2d3wGWQIXRisFNUOWxhoHVsp34xOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=MDOljhy8oxfW3Uv0M-VS7nfgsr4dlg39IHZL_i8HKIjGk6p7NNzEuFf0nvV2QY912i7-Xh_Hb-XB1QAiUbjafkbuLn3IzzpN-7yg5hrQ7BVUlzW8g5FVks0ASiYpLKR4XsuXXyEI69TVTcWLkIDQRS8j0sqcgcBqJqzDdl35k9kErUNIt6J5ktoLPW9-UvZrQ2FOpoNtnbylbBeqNi9XSeLhHDXTzg3cjZYsXp3mRjEYAIZoYZSbGYDpgBAK_5mjrMokXxfSJB7xvmlaaRvlvvRYAJQoo6kMaDhRfoM4QPRrcZiSjdDqpFax-w3lYPQPO4bAb8HKh0COc1Cx0QABAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=MDOljhy8oxfW3Uv0M-VS7nfgsr4dlg39IHZL_i8HKIjGk6p7NNzEuFf0nvV2QY912i7-Xh_Hb-XB1QAiUbjafkbuLn3IzzpN-7yg5hrQ7BVUlzW8g5FVks0ASiYpLKR4XsuXXyEI69TVTcWLkIDQRS8j0sqcgcBqJqzDdl35k9kErUNIt6J5ktoLPW9-UvZrQ2FOpoNtnbylbBeqNi9XSeLhHDXTzg3cjZYsXp3mRjEYAIZoYZSbGYDpgBAK_5mjrMokXxfSJB7xvmlaaRvlvvRYAJQoo6kMaDhRfoM4QPRrcZiSjdDqpFax-w3lYPQPO4bAb8HKh0COc1Cx0QABAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=fJK3KuQzkGV1bQ9LWBKVZtsUs7VWp_nVKF_TX1d6Dl_Tjo7GLihXYWiS-OxmLoMXMXsJhq8ZE4GKhsnAGDC9a-8_L0ov7NvUCpcIFfNEm1PDXOsq6HrHRt4NXWqPz88hlHLj_k-Hh7-oijZhSFWG45LO2jnb_0sOdMq8a9Va-xoLTkrHR7ZSFGlJRKC73gghQcBF5v9Y0xzBloBdtjsEFZhkoBRducwbnAQMRYP_8fgUuXJXsQftfASu08-rAolQFOI7JEFyWeen1KpQko3Q_s1o67ds-dKEaixvCkwy13limldkzrEbBXTUBlB1CRcolADYAWDnDKYr_vZOr5tfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=fJK3KuQzkGV1bQ9LWBKVZtsUs7VWp_nVKF_TX1d6Dl_Tjo7GLihXYWiS-OxmLoMXMXsJhq8ZE4GKhsnAGDC9a-8_L0ov7NvUCpcIFfNEm1PDXOsq6HrHRt4NXWqPz88hlHLj_k-Hh7-oijZhSFWG45LO2jnb_0sOdMq8a9Va-xoLTkrHR7ZSFGlJRKC73gghQcBF5v9Y0xzBloBdtjsEFZhkoBRducwbnAQMRYP_8fgUuXJXsQftfASu08-rAolQFOI7JEFyWeen1KpQko3Q_s1o67ds-dKEaixvCkwy13limldkzrEbBXTUBlB1CRcolADYAWDnDKYr_vZOr5tfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEJEfXaLepvvXMHj1rek1emUm2ie3BqK5opSIkDOL6NOelNKhet3jtFKTG-KW7eDn8cObHOY3RwZ2Xp72VtyRLVsjSnk9qvaz_Q19OR0ZnreOI6ctYW9Wy326ULuebqOGANUAjTjrwev2qJMMB33StxexwsAHrs46uhpgLmv6GlN66WLG0Qjl6kqdIxnQueGvOWIa728XZ-pRNj3B__wXs-lUIfcU2r3yqO0AsFqgW-eZPU2OtdE0pcHpZWZHqECmCmV8ZLbQBDBJWydgLmjqkPXM0EIWQ2t_o-0qebdk_tQoHLU8WfrgG8NY3MIUZeHarSZQ_rc6Z41ESuvQYitOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0aKRl_PKw0rgFXy-PfO2PfV7cMwGtv8Im5BoyQzMPR-wxctIru0pfvBNP4V_n14GCiO4tWBPV_EJnyNm7H9S53HleIaghXNLOgTREC4Cqqlpt8Xm5ES4TpzYL1Jq-vxzEJPlYpF-K4onyaqjetcy3m63IsrDn8hKQ66uv7-PnMDaRFHBahCz1uaI4jrQiYoH70w39FIK6eLJ5pSxZFX-8A3NM9c832rw0IXPbb65ogxt7TIlTPjpb1QQEpmFAXG0ulVYK-79NLLkzLWR5oZhCOLGurk5BMpFbJ7H6b_6ODMBVrAPSPvuuGmIFemdIgQuxnrM2JLzJyfPi5wjmUe7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxORAqib__wLXYYflo_Q3RKmv1Lcw6vhiV2GJAeHm8sIXY8nvHJS9WLYZqMz_7Rt_XQgP5uG53vmlFh7lq7ebMZLbDsFPgCvBxTXxp2q-zIuPNUHDFi3zVPm757Hi5s7m2VWyXQQJMrWrXkoekl5FIu_UHBE_i86C_Sw5scCE1asyzSd1kO9WFf4pe7YED816g5WTrcUbmjdweoVwZeOk9EjVnzgp-ip4RDpH_Xlj6dMpKuMqKgqKcGEgWf78WU6ZH9v4iFjdtxi2UBNn6aYFVZUD1HxZ4sidsyWRq9S43suOs3XkiGS2JR5p8iV8evGALTpC8GTaLOHagzxAYRHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=PqRNgZMvvJkixYXrMtusPwWe8zOZsabm7JPhwfQAZzxLh8H7CI3FM1Y1KvjE5WgGTb1pjGF6iR1_bI9ivx7v0K8TGIfMYhxPqblLrhULube3l-V5EqOuf4vr5wbjLilTVw5BDLzg40oVr62bX3RSplqkojgWjBfqWFupcLMUozi827dIBNIW_1eGK-ydF5tBWpBQDY8DV9zZSCrkRuFzm4rKm-tqnqTdtydl5vb2CktYKsPMTdOMY2GNkTtVJX1Nof9STYvqNaO9nHtV6kVAYT0TUC6LysGr4t98fT7pNuDw8IzDV0BiosOcwSLswX4d4w8bznQsDP_GFc7vYSDSSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=PqRNgZMvvJkixYXrMtusPwWe8zOZsabm7JPhwfQAZzxLh8H7CI3FM1Y1KvjE5WgGTb1pjGF6iR1_bI9ivx7v0K8TGIfMYhxPqblLrhULube3l-V5EqOuf4vr5wbjLilTVw5BDLzg40oVr62bX3RSplqkojgWjBfqWFupcLMUozi827dIBNIW_1eGK-ydF5tBWpBQDY8DV9zZSCrkRuFzm4rKm-tqnqTdtydl5vb2CktYKsPMTdOMY2GNkTtVJX1Nof9STYvqNaO9nHtV6kVAYT0TUC6LysGr4t98fT7pNuDw8IzDV0BiosOcwSLswX4d4w8bznQsDP_GFc7vYSDSSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=HfZFhwPtzAATkIBBVSXOjsQwqzOb4XTFyrKpPU0hQD3tiTxOP3MaTu6kBAdOBAjuT-CapXJ8aUM93RDuCmK2oaW6J69eirP8QVrncQUL8kFMttu6rLq-BVByYxMGsmCiDu4aO_9uq3RIvbCqLDKkcczMCT8E-sXei43uWKVZfDhZ-rg5rGM6C7lzjN6GcdGblCf0J4cMxEhAnTfdODFat_VIFtmEDMQHy-UvJX7kw_BKR_Xylel7ef50qNvn6eouTohInKtd5_njksvCR6cJPcCo7YcAC5XF1cNjtI2mr3Ioh3CZOEKVoW6vvUj7A0gnp5X6l4J3XYW8b8hrQShFVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=HfZFhwPtzAATkIBBVSXOjsQwqzOb4XTFyrKpPU0hQD3tiTxOP3MaTu6kBAdOBAjuT-CapXJ8aUM93RDuCmK2oaW6J69eirP8QVrncQUL8kFMttu6rLq-BVByYxMGsmCiDu4aO_9uq3RIvbCqLDKkcczMCT8E-sXei43uWKVZfDhZ-rg5rGM6C7lzjN6GcdGblCf0J4cMxEhAnTfdODFat_VIFtmEDMQHy-UvJX7kw_BKR_Xylel7ef50qNvn6eouTohInKtd5_njksvCR6cJPcCo7YcAC5XF1cNjtI2mr3Ioh3CZOEKVoW6vvUj7A0gnp5X6l4J3XYW8b8hrQShFVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIuQVpftX6iszYM4AjEjhIv_eLnhuaaPVwGjc78uZuy_y1nuwnlYAvQO4VqAZDjFaTId8oYTLREkXzmkGFmaZGdNmFtgHVS7CGle4Pe3oHOKTQyq-_xvUNrz83XPUkwDrS5leq1FSVt_P_N8vPO7CNb0gBXJqeb5OInTZlodJtGHSJ37QYohKWIq1hwns4uE4myNGEYBRzlmREvRvk9iCflYNvoUa7W6RCX6L-AzyRyU_-eYQNsARI0pDhyVMqZb2KrW46dh4KhU1jkua9qs8OD4Oj-y68KQRyzX97rBKEEvJxVepSV0jBL8cA3cSXkQ7E3Pov9A3vsB-Gn4E1MTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=sXUeqA6ZJ32XAVMxFFJTqBLLGzlYMPWvpadO_I5U18VQHLxt9wDLyIC0Ut0AGTGnv8ADWTMIY4Ps-vFCnijhA9_uGufXE-ck9VtkSi6NceY205u_hMvh2cd_LoRup3zpTDgDkIEDKXekItxiXbvBQ-b0my4lVKRjiHbCaUS8xJhiCsqXeMnYurjF2-mnh4nqXO3XHSkULu3olHFsgs6qUwvERFlCLaUmUn4ItkEvfGpSSUjRz7B6_npdskQRgXE2f7JZen95qYqib1tb7sfbuyH4uzlLoZhD17FVHgU7MlYlyH5DJ8Sx4DvA6QdGW6eXDcGovLtOprGfZoJhfVgPtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=sXUeqA6ZJ32XAVMxFFJTqBLLGzlYMPWvpadO_I5U18VQHLxt9wDLyIC0Ut0AGTGnv8ADWTMIY4Ps-vFCnijhA9_uGufXE-ck9VtkSi6NceY205u_hMvh2cd_LoRup3zpTDgDkIEDKXekItxiXbvBQ-b0my4lVKRjiHbCaUS8xJhiCsqXeMnYurjF2-mnh4nqXO3XHSkULu3olHFsgs6qUwvERFlCLaUmUn4ItkEvfGpSSUjRz7B6_npdskQRgXE2f7JZen95qYqib1tb7sfbuyH4uzlLoZhD17FVHgU7MlYlyH5DJ8Sx4DvA6QdGW6eXDcGovLtOprGfZoJhfVgPtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXaOMbQcetXg3iEtzAdpDepqu8jBwmRyJ9g98wd_yepMxfLXoOWYot99TyM6X7RsaCuvygMNxJdr351dFpungf7LJtNQCTXoycfuH3Y4BNh2IoQ0y_xUusAkwUm8dXZEoM3E76Wq6-0sCBOJKSH7vEKkCE5aVwMS9WMEFr_tOg92-BmPAB8FR3zSNIdUw3CcTjw0R7GWnnMu88VP296TBmEt2f8fFDzwD9FkCqoBtGEvciw3sfgJNSyJ8kckXbYNOpZU4EV99j1OfLwoirTq2rFT9otLyodZcSS-L1t9e3t9W8PMJAEKBjP7f-M6lQinH8dgLyyaHRUYScWpe-qHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=ZD59vHhCHR4c2PGONBOgH728TKKkxXuSIrwMFljDKf9qcdtLsV63LHJTUFqjt76cyz8fDEBJgeTEvhyLXoLQG8GQkn7K9GLnl7sUCJk9LQqs-U7cUbrBgHznv9X_lVjjI48ff_kO86SfOLqF5YgfaRGZVf84cxAOOoMODhZYNMGcNl7K4OWkbWHo_HVD1yNPlyaBGhdX1k8SuATmffR0KjUfMSiB5c7CR1hVK5-2uT4bxY16NvE4GxCdipJncvo4Pl0Ze805FXrjV1oWkGwwZxzfurX5d-y4pAteK8uxKQkmQUBk9zC8EmoWrY_6Q6X7lwEXvTr0Gy3g10sh1LTcAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=ZD59vHhCHR4c2PGONBOgH728TKKkxXuSIrwMFljDKf9qcdtLsV63LHJTUFqjt76cyz8fDEBJgeTEvhyLXoLQG8GQkn7K9GLnl7sUCJk9LQqs-U7cUbrBgHznv9X_lVjjI48ff_kO86SfOLqF5YgfaRGZVf84cxAOOoMODhZYNMGcNl7K4OWkbWHo_HVD1yNPlyaBGhdX1k8SuATmffR0KjUfMSiB5c7CR1hVK5-2uT4bxY16NvE4GxCdipJncvo4Pl0Ze805FXrjV1oWkGwwZxzfurX5d-y4pAteK8uxKQkmQUBk9zC8EmoWrY_6Q6X7lwEXvTr0Gy3g10sh1LTcAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=KdzNPU5Xzur8OSArzP3vqCuliUMUETO2o-w2JWMqxIvNVcJFD_IBeM7aDjkjsdM6S3Esm4Z2HxNWrdOuvbgahFyp9tB2LJ4DtfeoV9IztM_M0Q2hNOMsXsPTpZq_rYsvrWGySds3hkBAQIwT03kqdQflGN_oBemWb1Au94jMNqYU5dofDISGktdlun7glkGtWKCPjdj8-mAIhdhSo-L45BpyQlk1bvn_nOX0okOAr1yCo_vc7Youefyg9BMYhRTUKsYI29ilba9H2qL5RsCDIPKlCbo3fcRPdEUfduP6I3TMZGtMxq56_TKqY1Ly9lrzGv3JQME2CFGrClnHiZ9jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=KdzNPU5Xzur8OSArzP3vqCuliUMUETO2o-w2JWMqxIvNVcJFD_IBeM7aDjkjsdM6S3Esm4Z2HxNWrdOuvbgahFyp9tB2LJ4DtfeoV9IztM_M0Q2hNOMsXsPTpZq_rYsvrWGySds3hkBAQIwT03kqdQflGN_oBemWb1Au94jMNqYU5dofDISGktdlun7glkGtWKCPjdj8-mAIhdhSo-L45BpyQlk1bvn_nOX0okOAr1yCo_vc7Youefyg9BMYhRTUKsYI29ilba9H2qL5RsCDIPKlCbo3fcRPdEUfduP6I3TMZGtMxq56_TKqY1Ly9lrzGv3JQME2CFGrClnHiZ9jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzScMSS4rgUAqRhP0cIGCFVZMzgu22xN0PvOZh8AQRp_rCAxkSbexWyRi6oSEWbcynF0dP2jL1KN-r1GLM_WqNhhvvnD9dRY4Fq-xBm4mcp1PgF2p3ZR09624Fc2GQQWawks1MQhqajVM2i9Je6erkM80B3kxrJsUAQeRaB3fZI2fyCnrhaM8R6rI3UOyey90QZJX4mnxH6Bqq-LN7uQau7VxzszN753oU91VuQzawgWukYDHjamUMBnfUYEt-3Vc9dekUY4-MJmPod5vQp27A9ujImM4Kz088XjslMWfXNhgTuXiwOyyKt8d9OBLIK4jsPRNb1wzXwzCX-xcLqwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=P-nKvwQvU0fJepmvNeX0pWpVobHKU4yBBoY6HJNRFk14oYXvYD_ECOR4FR6YFkEUYRB0e_xrG891dGcXjWoV_p-dIgv7cMe61W4Ws77lnjA_INzB-Vok1uG6fIMbxM9oAEWa-LY8k9jzzdiZfhtUqe0J3aMCX7fgkcI3onvk_4_9082MdmANQRhoM7aY88oVGF7odXY484AKVoNg-gDzGuBJAXaKwTg6hPh9NATW8lJ5GEEdrk9n6oyJq_j4eHMkaE0z7l7u4GZ7ZT5v_eRLuI8jQpq5Gr4mqQpbtczu3C97z1zfSAqudMX6UgmaBEM1eu1wtoZ3Pjm09HQN_xD_NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=P-nKvwQvU0fJepmvNeX0pWpVobHKU4yBBoY6HJNRFk14oYXvYD_ECOR4FR6YFkEUYRB0e_xrG891dGcXjWoV_p-dIgv7cMe61W4Ws77lnjA_INzB-Vok1uG6fIMbxM9oAEWa-LY8k9jzzdiZfhtUqe0J3aMCX7fgkcI3onvk_4_9082MdmANQRhoM7aY88oVGF7odXY484AKVoNg-gDzGuBJAXaKwTg6hPh9NATW8lJ5GEEdrk9n6oyJq_j4eHMkaE0z7l7u4GZ7ZT5v_eRLuI8jQpq5Gr4mqQpbtczu3C97z1zfSAqudMX6UgmaBEM1eu1wtoZ3Pjm09HQN_xD_NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MAFeMhS55C0I_SXGp1LN8aV0hbyNnyHZ48wmtZKWrsZdx1Ca_seN-wSsgEvQuwiNmpCSEhBNfmXR0qAXOA4js9kk1taxYWF29qnx0Evc43Wz_THKL09y4bBQOuK_beOCt3pn0YC1sharne24xSaPlDp5xgmffO8b1u-08sEe1Rjm5Jgi4GgvCQP8nakawBUfKQubuTtVrpf9N6svN_1rbBkaxm7PU4jD2qkNWdTZcUEhGPWQXMg7mjxa-GLgYFcCHkkehnStJBGk-MesWFeZEEWtW1Cr9Q63sxP5RQQXsfwx8VffYRrHGgFRI1Fpthc2956MjG21kDu_Et3hiSRVt4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MAFeMhS55C0I_SXGp1LN8aV0hbyNnyHZ48wmtZKWrsZdx1Ca_seN-wSsgEvQuwiNmpCSEhBNfmXR0qAXOA4js9kk1taxYWF29qnx0Evc43Wz_THKL09y4bBQOuK_beOCt3pn0YC1sharne24xSaPlDp5xgmffO8b1u-08sEe1Rjm5Jgi4GgvCQP8nakawBUfKQubuTtVrpf9N6svN_1rbBkaxm7PU4jD2qkNWdTZcUEhGPWQXMg7mjxa-GLgYFcCHkkehnStJBGk-MesWFeZEEWtW1Cr9Q63sxP5RQQXsfwx8VffYRrHGgFRI1Fpthc2956MjG21kDu_Et3hiSRVt4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn7JL6C9tac0zm5LiC-gHXJ5ee7G6MDyFmTEnCT-i9zBKO_ZbWndm0DM7ez5bXJSxwEAYNUi2XkF6zs5clvg16TLN9-o53YmiIwonG-5fTXTZFClI0UKmG_tt90cslQjDqKQkvJT6LDZjAZGYl4sO31B1Yd70CObBsuIGAajIPMNCFza4X8ns2mXv1HUUZOsaCplGXje5yf7As1kuEs0uKaRWqEEPu2QIs8qt_0Zg5nDhWo61cWY7KGDiuhUoDcxSvOMOpFZ0dyOXYhrz6QftsEz20R3y5bZqyUSGMgDk5zytIf6s2ACqY87FM3yBYx-3n8Be0EJgWBtho6CJhvp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eASz2kSJKdFHWjTW4dORJ_i9U6YDD08sIA2rlv1HuMImBKkf2VOW14oGI507Yjkb9uvQVXdpXBIPB6X10yr5LzR8au0XNAozSXxZxmkXXQTgmxxtjWOawntxx7SgS1wxXvPWbZb4MTfJlXw-kORiWl7eOJXAVKioxhUBKP3S8bBLv6qZu10MmuOPP82VZoAiR538ApZjHBC_RooBa00zd0474UewbE6pwQddwn9FBeuZ9VHL9qipepEFgPfgrZtnG8vhOl1-BADvbdTPqiejYzw7eqz35HeU3SsxLfgo-cHt6Y3pSZmwPEbEEijuz3TVa7BFNOHhGOWKhEICPFheIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2JY8lUzFeh46pRo_7atL-5imscBv9cZxVtP6AsYyj3dPsAjG8toVmRbkJGr-U_LeiQKPWda-y3eYx1uctLKqz9OJ5i02ihzXaFF5WsdG1ER3d28VFjT2ooaRG2BoClNwVNfrNCXhQgCV0E8f3Pa743VchEGIrmdcIeo7x_6d3sk2_gXAsIfhNqq1RO9GjrelD6JbAv0GQ1brO05pDZ9AR9MrDUxcYT-hswDAvLRa0gXOs5P65p4MzLsKz9BMxqpyux1lqQvkMI9UPlSLiOo2cmbAWN9jz8l82QskEv2xjUQ_WHrM7JcX_WC4b7Y4UD03IfonLIcbvCtas0G-c-UMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=kxkMhH67Wpa5iYOEIQ0snrYzyawkhcx0bAEahHXWR6RVuITwdCft1jzqXAz9hmZSN-4weT6D_AzULLvz0YAifyllq0FvwN-FjEuZQsUaMrLqLX_bwfEkjAkXz1hhc6kPqbCqlD8BDFp2_GWmejSRuaqwVL3N8zB7mngrvvoFpORkJeJSZD7-dWsXIBvXOc8ae5md2ZZMMRPK54-wbfWs4qm747Ww6_1QPdsZn-odqVWNFBRFtRM1zOQLxpU1OxaXg6U4gTvYhdXqLQ4wtoPtbH4tOXOLo6wxIjbt453b4aBTMe7jW4zT-gcPt-ASID_r3ESv93qO5HRAqKFBk2RgGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=kxkMhH67Wpa5iYOEIQ0snrYzyawkhcx0bAEahHXWR6RVuITwdCft1jzqXAz9hmZSN-4weT6D_AzULLvz0YAifyllq0FvwN-FjEuZQsUaMrLqLX_bwfEkjAkXz1hhc6kPqbCqlD8BDFp2_GWmejSRuaqwVL3N8zB7mngrvvoFpORkJeJSZD7-dWsXIBvXOc8ae5md2ZZMMRPK54-wbfWs4qm747Ww6_1QPdsZn-odqVWNFBRFtRM1zOQLxpU1OxaXg6U4gTvYhdXqLQ4wtoPtbH4tOXOLo6wxIjbt453b4aBTMe7jW4zT-gcPt-ASID_r3ESv93qO5HRAqKFBk2RgGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
