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
<img src="https://cdn4.telesco.pe/file/iTlvKHoaHmCU_0YdDnUHUscsOCcq1E1HBRv7UKT9sQvuk1qwy8EkI4gp70CZgvm6q4U9wE2F57MLDYSOAQ4ewhct-C2FbFUdZeNO1l9cmZNh2rMiH83L3AiP-w3U8stC7K6rV5lgeNeLPmB5QHUS83r0ghJRN1MnnBhe-HjCJ9alMA8AsE0dC0iG-0LPVUT0rJo6qGmhx43UkQo_Y8PhdL8i7-QYYREni1esZy510zG9ppNuOZpMhHdEW4A8Jm1F2SFwOHxgUMa1hEyqr9o3OYuxRbBODJ1J-o04Ze58J7xI0XsGyd6_29W4essNzn2-8lt8njDTAYaUOWx-D6-bEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 591K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQAawG_FO231zm8vDhsdY7ujlvPOr6s-_13roaQGWlBNXOIOXhymfMJGjoONvQlAzPffO4NHFP63iTjmR8c4Of8kS4LNJ3MTI28K4rmGlqiXlrU_cPoXRKUe9leOSYnJwRJ8bw8FtLWi0VTYw2r70HTZ9PaGdmP6bmobu5H9k_avEjSrArtjLxe4NLCyt_n0KGDrM2F23QEmlDZcxpCLIlKFD6Nk65xGKytY9r9P6qoTZN2OLDnHTdLlIzsOwIm4jvyw4p1ShHf-baI-tS-pcwVNY1RmOq6CTNkL2QF-lhAjq4RbfaE8XaQka-2DDOrsBW6EIfGVLHWJZd4JwSWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKD5NVIppBIN59y8490ZD-1tug5TIeIDIaSaaDvx9ZFBo72ncVjo_aY1QYEpORI6TsbBlbtb4arjoE4ct8A1FME857TpjVzypnziR6Wd8fJAEp6e5_66A3NcQ8V0YU-bx_fBO9hfM1btd7I9Lslm46EpOt9kYq2Jhi-lhUJ-9_RO6FOpfwEzxOWM-T6t3jE-jj8Y0god61RGbqBMce40qO5LaQZ6OlqYvRE8HcAqSEKE7DvLjFjL8KzepcZMBHpdjf0oopJH1NNdIyODzjZdh4Addg2RihRZooEjOg3JRi4GjSA9miIDmeH-YikuNlUbkqa12ke2GqLM91uEl4sg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLVa2M5VUBFUk7y0KTArMu0Bkw37ApEGBEOHjJZkEFFIlPEfpXvwhPy_aejNS4TT5LvBZlt2XTNPmK8SQG2rPWIEhK_e_8ZsxKYBvW45HHvvLIkOvKBmMpOMrWcKIFMUAX6FrRRQjQZVpaBCFBJmJesWZ8woPdOnGUsVT5qgA8xOpkRLzwmPAUjetXvsVhT472vLkqxuA1xn64dEKWjPL7vn1ZNNfrVL3hWSMtPq2YCgqQj_ajV89gkEKt2zuLzGbj0OkAJa14WCLs3-a_WBgdJ13fbPLPU84vhqdUJzKR1wCrIZjAeYW2_cvq1EhAW0Q-W69F82TJjt6E_DRe1ePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ataQeQ07tUag8VlT6eKWMz6PFlFcnWAR8vSwxsbEYmMRFYygZqT3Azu642an_cAJiKI1DenX-00jB0u_aNmiKbfQ9ExH2RQDeOwe0Ai73FKpwzUBrCxFAH8cmqCniYWDTmBwbz6S1qzliEv6SxsTkD-NfD4RrgjM7-s7zUyzT0Ai33fr-Qa_cJnOnvuNbvPEZyUZ9lgExTGCWIuIh-ewC2HulhGHVuWh0GXJeJHKiWnZS1PZDLoUr3A67dnCR883l3dhACMhus6ghU3PbwDWomW-qV-NfC38OEPtSsFziq_dZ4EFHz4izajIiVi14Y7XZAE1IDQsocgv0Q1AwWdSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9R4lXO4q1W1qqy7R85EOSflJrf8VjnC6h2EpsvaG4Cpdg4mqsKAlyD3PXAGlSL158cbGY4SB5TbYtNrjNpAER-obLhTAv8ubuaQovXjLJeCuWS3YxLLM8bGJ5d3UnACoAUkd_joPL4-mC4sdr9D6U1e7Qb0F2DJMUlQ15ZkVNfAN2uKvgoOIMSXKWdAnGsfEb2lhq1r01XP5LiukfNkhCI9wkWYt1_pBVTZKz24siWywB6tIlHMBd2GtDVvbwK6n1h1isvux9r5baHxFPRXiGRC-Zx3V_Qed0dj4U5SFkPTdlBLUu1FIEl6D4muXr2d4_RzbiSePjxzOwuJJ2prUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txTE-ce9KWfrhcsBtVSaMIzJV9MH3umNQjizlsv3RgHqImS3ZsfURI1OVnZAJzYRAkjnCqIN9hU_7mDfgCmUSrfGvku8VEH4gOYK5B4e0UM-7JP-QGtj4yXFv5PTbfx9ir-qpFC0vIAjsHbMRyhYeCMCz8fB7uG80tVIu4cqEwWCedhHRsIIvGSEs2UbmZ4eeTwACXu2D7FRzZa9YQlxIAqq_XExwuqlboFXum8pQ4VYJdDB3xWEAsAaS-pHZc9yIHSodcLlEFNKPApC8Orrnndlw_UjnSOh8wHWcNrL9Uoa0DhZyjYCLsWFPlUEEhQx1DrrZAyiXJOomMXgQqf0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgWPE3gmQhOqvEPOS_EteFPp79Ro-LB_ongMvrxCKvsPNWvyZXOtMJTjsJpb6SbygD95EUtY9hf2Ri6LEvTcQP4_oR3AKV2ECYr_izm1Yy4s8t_J4UCGXouDV_SHZirwZLQ0Spwk4hD6ZoarQarabC9qBbzimtqZRgPc0nf7CtESxlw4yKlMnbopdOp1OCJiQ8puB528urGBRYLIoSeqxBg4Z_jHWiPVQYAWE591YeyTYizEgmz-E6PnyFtwDBo93JQO7gmzbRVadDGYTd9WHa0yX4QWLea9nXYHIHHQKkq1EUK9NurGf4X-S2VojRxb75yI3Jr1sLoBnkHdJqvXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی هم ۴قسطه شدن!
بااسنپ‌پی می‌تونی از بین بیشتر از ۴هزار فروشگاه در شبکه‌های اجتماعی‌مثل‌اینستاگرام، بله‌وتلگرام در ۴قسط و بدون‌کارمزدخریدکنی تا دیگه با درگاه امن پرداخت اسنپ‌پی، خیالت از خریدت راحت باشه.
لیست فروشگاه‌ طرف قرارداد رو از لینک زیر ببین:
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/29188" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6gg6avdNPmBynAEAJLSO4aNsyWBqW2dA7ZNpjVeQdiCo5hRW_P3i_aOtjwn43tIUYhBE9NEjD0XG54rnAVdnxZk-lAzbgDDZLV56-EbiVmhlJgMkkuUeuyh6POlGI-ddzcr80j0fuGmXZR7DrlaTU3gfndKxCkeZvj7g4r-OrYwc1Ipmj59lkkSx-cmjdmbPMM_f5aHJLZDM5fjZBd_Z_pnMiRSm6w9xqEPcHOio_scs4UFe9YO1UmMlvvuXhU0Jf5V8KtLwR56j-RCrwEFcLxQBUnQdKIrbL16-T_xX9lieXnK2A6SYsW5ECsszC6BiGXVNqAtNb0FvQAlRHE_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2nZ-UeVdp2pDreRS5evJ63mwJu9CTkb7F94C1W01qQWs-SnfJYs3ZpX_gK4_ka9nbvkCI-zHIOBslRW33Rasa9dqjg66L5F8VG1xTOFOd-GSE-isAYEFJQ2l4dD-k5GrchGmDj97bCv1xEMLzau3qP1O6m-XihjP2Gqoci77TaIUI4kZAIjYOTp_4vAmCCjmLPsSmM1vYITCC89FPslMGqX8y_QgunuoZ3Tq0gKpiNbtwEt98NOqgVa8oMbsUzWVFTHXobEN2qgYHH_-QQSSrxFjZ9mhdSmQBR5Zwocf-T4Yx3lAPBhRxJKcabwgCtjg_zaCKvR5tmqbqDRPX2r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV4QGQbUSq0slNCydaJ4Wvh5DLeFwpuVBngdRJbxhFCDoBB2eyqwyH0dErGXc91lvKqgi9ta2yLcT-xQ8m3f30JK9nqXOAVrojLRlZc8RpqmGfsXGvaq3FN4OMtKnDbHMMsRMtoXtDsP7koOKh_IYqas-F6LzQkXuGXhiWkiC2qbVBlXF2BI3JuCZVw1T6iuDjzLKbLPx_90stDPLgdhBsgxxov5lI0al6c2ukH-QWX1VfYCmRRWKqJIOWUN9jz6a48CFoiU9TFxmxG-95-Uj8bBS_rN2VrSjbT__BULQo1Zc9v9C6g6NT0eFAxIoTq8EORXW7gbpsQhYIhp099yPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwI2Wa_YKgBRTzFsU3-7pN8DkQ42YISkeblwIWGCA-KWCUM5reRsRs8-jk-YkAAdUJOhieoVtjG5JC3Pzc05oBR9kQ00xcv7aWk_7lMvle7tIhWDgWBSP3lZ3ZYhwUShZinoU-fI3Lv4vPTkyhaO-GvUcZg3DVQ83slL-proKhbrpuoXW_kIkuZ_cBw5ba5SqwR2wlh_hFOyh4rWzMU9sSeemc5nmekNgG8R0PR3Efrd8Nm5cCP5BRuWeJ_pKPSKChonKKCS_-FxLKx4A1ROHpKEuGfKOMvuBKwLG68PQ4m2h7yGgdip_zlKMLcewAXmwp0wceQzHEnX5e7xIiZHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=c2BBFhIqgLC9z93o3aVZmkNBddVxoYz3L_bIq4ma6B6131iC9CoEjvlZYckjix8SzlZQYCj-bDdMSmAQHk9MmGDQ4VycWZdAS5i68NgmHOTF27uWa9tmxMmsIbIBjkOeYBjV90FSiga5XBpPRID5IS50AOXRQGdleMewQzQrVwlpEXUzt127yMpWzsaA9Em8NZKPKZ3E9FoKk0NLi5lrPZvMlRiE36PrfK5kaHkXXqoN2yJ7bXT9pJMoSwksO95g3URVRA1KYnAAXmn-Ok4WGrLvjmKZOotmbE3aUk9wYpovH2OUxUZBCnWtrQRNaXI5Gthg8QZRNzlKZRulaV3uvKjmay8GSbtOnCNxhpvbibDac6dOymN6YcKAJwtkXgcRb7kSBf8BNmwd2K-73oA25V_8nTznmuujwaBm-5lGf9NSH7UFiJc5A9MmauHCK5PGGLNN3zs-lSIQ8m3ZIiVpjNgCbtPPbn_l63BvAXPzoxLVpc3oTiKzIc25k533e14zI4g4prgIj4sEsUHiKpU37X9JGvNd_SrnlddK74G6GFW9BdEgzN1UuRkQmhtA_L8epz4uHNxDdIstziHuPuwtim-2XNm1_QR5PAgs2XKiFFa9-Siwjwskaw99s_CJH6QQUepBByEFHp_-SR39KJ2rRiz20yiD2gqsPqvuyMX_KcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=c2BBFhIqgLC9z93o3aVZmkNBddVxoYz3L_bIq4ma6B6131iC9CoEjvlZYckjix8SzlZQYCj-bDdMSmAQHk9MmGDQ4VycWZdAS5i68NgmHOTF27uWa9tmxMmsIbIBjkOeYBjV90FSiga5XBpPRID5IS50AOXRQGdleMewQzQrVwlpEXUzt127yMpWzsaA9Em8NZKPKZ3E9FoKk0NLi5lrPZvMlRiE36PrfK5kaHkXXqoN2yJ7bXT9pJMoSwksO95g3URVRA1KYnAAXmn-Ok4WGrLvjmKZOotmbE3aUk9wYpovH2OUxUZBCnWtrQRNaXI5Gthg8QZRNzlKZRulaV3uvKjmay8GSbtOnCNxhpvbibDac6dOymN6YcKAJwtkXgcRb7kSBf8BNmwd2K-73oA25V_8nTznmuujwaBm-5lGf9NSH7UFiJc5A9MmauHCK5PGGLNN3zs-lSIQ8m3ZIiVpjNgCbtPPbn_l63BvAXPzoxLVpc3oTiKzIc25k533e14zI4g4prgIj4sEsUHiKpU37X9JGvNd_SrnlddK74G6GFW9BdEgzN1UuRkQmhtA_L8epz4uHNxDdIstziHuPuwtim-2XNm1_QR5PAgs2XKiFFa9-Siwjwskaw99s_CJH6QQUepBByEFHp_-SR39KJ2rRiz20yiD2gqsPqvuyMX_KcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIxuUe6alT2HewDWgjIGtKXurcmBqg1ndTf7LySTQU4KxUNT0IHBnxqp0aBMCCI8jaiIdldTABFwjRFLpY0NQ5x70xdzH1nObjUH-ruCb1185Yb_S22mKMTKZUhKgXkwPtVSxVH5GzMkBJVD1I0aRyIRLP46-sSS1Jk0kIAyunQMd1ACexB_BF-IhjAlUn2oNrqy7gRmE3irJWoUHCiLrl-jCrk2gVOuUuoSHUvO_zr9YvVhijVPA84wP0P8zX1RMkYv1HB6VS96htkImiMOAXs8-Kf-0q9vS8Ef7f2hQ_P-wrdOFNTM8__OsyqriVta15ow8JpfDKqLO5g2CGRMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnYw9couK6ZUmAFnvWPPXs2bXjbG0SwtxqTxjQNMeGLZl5UnGVCX6Cz4XdDY47CvYqheMS3ZdbdDZBcKJsG-MsXTekMFCRj7ndyHAj5AiQMSmKC8Iy7zQKoJpkw5Wijql04VpOsfKNW6jzGg76V2N1QqApCl0XzLrKMOl1ONDRdeqosckK2DiQ81sCb9Fy6zUIpsKuyrSdhJ18RbvCfDza5slhZN4qe9nFWQKpLBW_lwl1vsTh8VEYh9WLyNtE8SyxNYeuyS_U6wquj7HSCBnN_JQyr1bEKbtOAaAtF4uLLNPp3d41Pnu28c05So4YcJ0Ghp5pRlskJMQwYlDBKF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InXIDMMVkdIVv4CJt55UvfsgxsXt_KPaNH7QVYLTjkU9UtpyPDFLloS5ahvysWMZQg-0R8_XFkYg82z-FeZvjMHdEwT75BfhpmwdYWCmrDobSRTLkSuvgH6Pnr0s4wbTmaW2fDE6MSxWqOVWQaJjZPDKuXu2mfkJF2t1Z0PcmomhWyXBTIrivfxmg8mFyWr62zxCKvS-fcEj5usrcaYi2Wv9nhItXtsCxP5Z_crSprCHHz97bHkw2Du0RClFSCE1PU5poSetLt4br69bgpuKQORk2OTXnEVK5uCAlW-AWlMWWC0O2WGlz9ROCI_cN8MNLGnfHhtyV7xb2wYZkyQIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfWhakMKuCqDtwecvfm3CgVyBdxP61pRLui4ZohQv3IBD7OJflzutil8_HycSGQiG8Ia3YCbMnKVyoJlijx2cRdBpB7L2basIGek_uZVtivZne_6FwZp0iBal9K54OqeAWCa7XhCjcaCwsw4xL-FiJd8CYFKE9KPOiMeUsBx1-OXVA5txvb-PKGK8Ul4MTjoSKf0fxiKbiIxRuAtitJaa4lxF5OCb1hq5_mKWvKmOcsJhTfvBLr8XZyHU955o5CHKj2qaH35GFlElnl_IhBPufX3LJ81OtqVUuatoxD5-Rzjjz-sIHqXYJ1LDOhsutPEMMQ1hb-RGw9OID9ly3Rw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=Ty9RGZgbuhAy8hXZnmTYUqaYmO25e4pi6cqjQztjDzYrAd3VHMoeN0U2QCOnKQwcmz7VsGFwnQDllR9UMo5Z7rlPEnwt2wEXO4o8pAVq7n9OvebkLpfNdw3-r3I-4Uog_rry5Q_WvuYP-9CchFAm990kVcCUw5Bxodb5ZTTWwGNhxeKVNsgPSiYn0G9flFdywB2yjkZ971ZlvD4W-yUaJkNXSsM0qkvoLgO1lJ6c6UvlRYWzZ8l_kuHeQp9L6e5IWxftiycwGOFmr8hH9Y3y5WDGYLfFsF1kDjPpNmztrncLUk8qu3kR_j0SPxIAvyiQHevbBnEEEs8lt7hAM7d6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=Ty9RGZgbuhAy8hXZnmTYUqaYmO25e4pi6cqjQztjDzYrAd3VHMoeN0U2QCOnKQwcmz7VsGFwnQDllR9UMo5Z7rlPEnwt2wEXO4o8pAVq7n9OvebkLpfNdw3-r3I-4Uog_rry5Q_WvuYP-9CchFAm990kVcCUw5Bxodb5ZTTWwGNhxeKVNsgPSiYn0G9flFdywB2yjkZ971ZlvD4W-yUaJkNXSsM0qkvoLgO1lJ6c6UvlRYWzZ8l_kuHeQp9L6e5IWxftiycwGOFmr8hH9Y3y5WDGYLfFsF1kDjPpNmztrncLUk8qu3kR_j0SPxIAvyiQHevbBnEEEs8lt7hAM7d6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDsphwxQgjIyrVnvS_r77PjBmZfRZxKcg3BRwEc9jQL6b0qz6d0yfgpFwN6hUr5cjs6haP6NZVqwm6G30idWAIM2-QF7Loj1Q5qxlX1zSxP_jAPNUwZlLaVCDMC2IZtBY03d13htuUCC5Q83nJV0wh8bHelUwvRLC1KcrEmZO79WyO_jhGDhFCqnXWxaB9uYAJT5qSVDrJ5Ue83PZAAWGta-PLJIafjq9SRr3Tpnc9cdZgmnduqWc0JIN4Bc1vdp1XRJQLzXkbuSLOZ4ujhyFazNOmwl4_PEd-PuNQio2vRLPr_FP2P_vLQrscv6fP38Q449cwMKRq0Kw5E8yXaUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpLOoUmW4qzeMEm37E5RH_unTzqT_sUY1Fb0bCEDhaU776U0QXa2L_NyoSf9Jnhyjk5L129rzo1ojtJ4b2K1EcieMPOr5zp0KpZdJ-Ap9TyhRHcCuNwjBidAh67gKetoWk6FpQin1-5Wzx1TnaHgbGmEEAQpgW7nVsiglOFg1XZ8Wp9hmi9_M0VW5PEU2893LCsULWJ1I6wMyuvCDygdJj1iCEuVw-BVFhGVxlgkMlEg_Ju7wz8KhPyP17qcwbsJ1p76BeBXkRJAXwsOo34hS2uA-FDTHFiuQG_t6IWXao-uJzekVZ_eNoxlF5tgN3EiAXBs4IwcSuJKPMFD938E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHcHqIDuF0Pxrl_k6JEhnliFI6O7rK2Js5jbJizqaFKTyICDlKuLDejOiB-OJ0UnqSagwFk2KjPtjIi_Te-Znr_kYIlGC4ZlJaRhEkOFPqVxzdGigOlSItxii-G_DPvy3Db3GWa4XmRXhw4q9U3B3sMV_uCyCwQySDdTUszXXjS4Cr2FHyY1mbTqH_q9Up919z-11a4dvThu3qERmuH5tvwJn3xEHd-x2ZFWA7aVgp-nbgCrD4bfmifGOHdxkjNbTin7Fm5yaZW-RB3g_GZZEb5iaOcl5gAHnJdYjUlQXJoNA2iS4FFQGqmD-eaBDlSpdZos61FBCZZ3ub92XeHMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9i6tv3xNpqU69tSlY5WJEvmZujXudh3wG_5_rL7yTORCDBphcPrhrjaXBHeTfz5lOXnKa6-IJv3wjyAz0sn9SvE4IT0nxpk9VVlvbvFP_jS8toS-ca-MkKsyLp79kUQoP1J1wqX-OT3EmPctk9FXzaNs7r5NcvK6e0rsDpF__CJr8zy-e4D9VIrr0oRmfaH1MfTrueF7G-FJqgLFz0H_SWlFLxncA_j0nX98NGGAJfMyYjwP3kHbGxFWOukNonSiHd45VLdG8MqqIlaxVJneUfJdEeNoJZTj4WKe1la7JBwMRmuYRN49uwU3BffLMnbniFJhUeEClVRrfO_tDVEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBpTj1of4Y7PapR7NOrkYvjmJMQ0YFIIcXeLxlO5d44yhwW3ZudQHIzzDKDvjGm7D60VWMw7BQloAl18KTsXRmW9jCEgz71QOA3a2yF5rVNpiRgmUgygB-kr9joTEucVNZzv_WHcEZfjApNIdXa8xtUkHiSTxxXahWb6DgYIBr9WT4GwJfDf9S_s4OmkPWbvoMb2UK0KrMKlMH09hMNQUkP2J0bUOPd7T8Kf-NW-41YZKZXOS6su_egbEApaHBgHlxJHzdpn6qpO4WI6VRPNe1rDCDMGmfX6E9WpJhDKSBKj3hGdnCkAEXaDAXENuL61bjugt539xqg2e-AT3Jm5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDEPlVFTASNA04EBGBZpcCQips5qGB389lT1zKZsGwdau9ygYgMdFevMi2Kw21D46XquEEBunIeF2Zd69V9obKVfijHjVxWQxC2f4VLG3yDFnsZa7qa01izaqhhXLdveZMP_M_1tvWqjNeUrokbXfz08eO8Z9fndjIjHpuLXRzTDPZ91vH3O64Zu0nw7yOxmT4e920evTeO3E8_tUUw3y8bCG8BHh2ZmcGxvuL33oRNYXTBKuVH2ZNKsDcLKE7vs6IRcetmhpcsN4WZ28RRgnUSE1f-nGdcplMmRSPuSJPLfk2b2yH0uIzUlTHeqg1f7oC6Vpjc3xRf8Rsq6Dv6GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQGSh6JyEpXqnB05IDpW6jaIAkg-19IvHwMJ51XUNgqxcnpWKRX3Y4G2yqSDBaHSC7ce9NpAK3Y01s76hqwQQBBXP35UQG1Uy84fftZ6SNLz_NrLokDOGyC06ctSVMyxRpzuMJKdBazTDUPEfqER6VFvEsMp6--UIiTLVHbDv8tFobofAG_kLaoVDtJFdPevwMVNFvz18S0XYfIdaj9hUMhiLOVSVdJ_Rjwlxy1FpGfP--yAqQ7X6a5J9uOvAXbr7A4xIXQbVYon69R9lv-QWyNfggRPvIA5B2sf4P5I7zvAQqRPhACBOJYkEZhbnANNKHq0JKQ6lYkNKvWJ1jCNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYTS-trzNgmpJGZduooqZI0l0JNZa0_Q3MkYdqZRUZBi9cflu7RfCguzwF6B4a4b8U4DB3fKfcpfheb-Jk5TC_3GweVMsTwrEe6CSdoXtu6pbMaDiYi5VPbI-8kjGTLJbVEFhVSWxx2x8R2bs_nLsTfJSy8aquxoii8fcVJZBq4ivSaaoqtFUboJHzxB0WPh6YX2JuLpKAhLmlfEDBc_G3Z2PgKHb87OgkKdY8gxfWnnpdvTBLxBvBN4Ae4XDZcIl4D05AFshqfTvYw2fA2fKIccPf7wQE493fDpvKGSquyUcRzGqUO2DRxh7IhRjRVc_ZwDu_Y6TkjHgijcqZ5Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBJr2PKSzj4T2iY7bscNFHw7DqlTYzi8fD783Gho7PAIg5MHotohmr_HrFPmxCBsAmvLFBhNqKQX9_lo6MVrQx5VzOqHtlhQn0ePCkcSk1uQhXqLu-YMFczx94Rqxyo61G7FzwodE8Fg1IfocZUJKAvM3RyeydxK__4FbjjqzEHwHL429xEv2NLBPENrnZEIbPcub_pjadVtw4Fm1Z-OY1XrnIF9nAr1Q3AF3CPKt_mA9A6kjKpGmQ01dx6UxP-12x9YHvIhc9bk0Qww29MnVjFou66A2zqyLdIDP_g2VS7yUrQVV-nXPuYQV6QRN1E9T4cCTQhlZZzDmPF_6dIYvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBLtNctKhUyaE-NiIfNq0pkCc_Xo5YUHzzQ3h9lUhQ-2Y0VvR9XhGWMGaLHh1orBhSKYLZmFexFeUPRjgG1Dh93oHpwQLt3JCau-WBndi3oqxndl_GMG_CnzlrrG_xdf2xLxLCM2bUrwPx4kOvlTSlwo__cDYPEDmcOr67aG5KWdbsPYbNJL2cOPel2_VKqDkSk1b-o4HnfcdDfOMVoabmsOoSAkPbLZAY3A8GMsIQfUtQFwyMtlTbpz0S68grzkvdnilIFdimvQyT6ek277IhJxxARxT-JFxiS95Ccv_IeRZk5-CRE2D3aez3d0fOB6anNYNmHZHcG7-RB7RkYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJV5xuwW3EdSK83kijHm_OI30fqsgYGQau5GTEMlZClwtv10iLU4knKrI-OQYdtcqG_4Zo4A3SK7kc_9VUld-tl5vmYtSLBZ10FSskSA4D7InLJ_SsBpOCsqnrY8AEB-N5Gd9b0VLwwGtnwRAIZieAWvYLbey7KeCKhJhE8yR9PTvqKGyXxXxmk5ThM25HiQUjSiY4N8pmvmfY5CTe4q8SuvWYTfQDVzwZm482EkGY9unNfTkcNTdwkSEjtl9I4eHY0GNM-GjgbeUvo-shsbSyfJp47MEY8Xra_mIBP3Zi0budvExSKo1esahn26ckgBf49LYcU0pqHucKo79ciCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29160" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFPGlHscl8LG99kWrdkhoqsS146M3Agth5DrFhrvBbgVC_Aa4O0PRg0ssmQPiUyxWw2iYwt5egNh66nXEYTLBdzZ9VqNamvWegm43TfT9S4fmaJZBRlxTKWkasAAKAyYPd1-ZFAeBES66rjW7G3-2VfUPGCtphIMV_rLfXZbvZz6Nal2XU4Nez__42eZzoNRVGdioge8s3PwmPqYp2-qvLeK46D0f5T424tRFplJKXpHtw3QTOaGFCuADjwY7_CSV0uiBqKccZGkaESzEVDh0TIPx0i0cclLY_a_iV-UClhcEpNqHt8aXXysj3yDA8Ykhhogn5AhQIGt8ecRkp2I_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO1mmWWe0o3qQBStYF8rlTTF3HW6nUDgxsesBHfOm91UXpwfPtFAIn47vN3uztaCzcQgv73wpyu7eK-r15UC_jkGirJ9dsacS-hLhrcgQI5WcxVgzp2TstUrMV-zgekqTSHSiYcXOT-hTIPTJGD8433LWhWtpteY8xdsW2fgAXt8XxE5V6d11Fmrzp0Er94FOKWAPqfPC-Rcw3uD38GvCXRn0sRN4eJGoRzr7xOq3ddWL4jQfCYHCfD6Z1q3fwAJInLhq7s2z8Sp_mCr41F7nfmqsyPpEf8E-yYtHEAH5WpdG_OW7clDeYCVt-d8G_owNqLmlFfx9aFUkFKx2njhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU6yz-xIeR13rCOGpZVxiZEv4NRzhImhfMd9-kNNI9na6oxrS6gzIt5vVAzYoWbEsAGIbA4n5ZcUyQuNTfNJpoaZCfEqfHLY_tkBky0mYRYRiRhwZh2XViPeEDtHMWEmCGIzeUVC8Ts2amX5TAN_Q2AKzZRIcEloc4-9Scs450t34HA8knikvCdzMzntzmvoO8MbWQKyu1ILo_4fWcOnvbyrMH8eZK_btFo9Yk5C4NRCwSJXvaKDOyiQWsckB38Xvb9z8Z1vSeN6xRTgRuThc1sKLrWl9CVzN4RSMvHffeDIjK8Ew4IBGRR31WTxymJ3t5idQigKbqcEzFskaLb3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=JUm9YAU3OxTrcixXMx3x0T8-r4eQXY59gIGK5OmnpHto01UtAoyJxiGj-SIJP5bd39YF1CmUlmVh6SQyIqvKapOIFPyp2JliEC4MOTPfDubZoZVWoGjnNQkwZsau5evNNKry9h2B9Iwjh3mu-SRyRK0o_8AQUK0vfgIWwv-rDRJY53RGmCJcZfXyM-70MTlI6uGRLU9a0cv6aksKPvYMcdFzoedWK6CFJ2Uez71Z0x3oL9lFAw5CEg94NpuCuAhjBl0x-M-UhaTwwe7-aDtjf5qfjMSl7zLFFxJdEve3bSLJsuuuvv6JMi5VJNBgWld8U2MbPPES8u0ybBFh-wYV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=JUm9YAU3OxTrcixXMx3x0T8-r4eQXY59gIGK5OmnpHto01UtAoyJxiGj-SIJP5bd39YF1CmUlmVh6SQyIqvKapOIFPyp2JliEC4MOTPfDubZoZVWoGjnNQkwZsau5evNNKry9h2B9Iwjh3mu-SRyRK0o_8AQUK0vfgIWwv-rDRJY53RGmCJcZfXyM-70MTlI6uGRLU9a0cv6aksKPvYMcdFzoedWK6CFJ2Uez71Z0x3oL9lFAw5CEg94NpuCuAhjBl0x-M-UhaTwwe7-aDtjf5qfjMSl7zLFFxJdEve3bSLJsuuuvv6JMi5VJNBgWld8U2MbPPES8u0ybBFh-wYV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeAiFnS6Sg6HMvbD3c7qJSKtT0xMIton4jb1PAdG_ZqaMZn_ZT0cO6AMLZBXxdBqXVgXNwYwUdXF5-K-s_ece62VAJMAvKrs4SXALmZjPusoNgRA791_VonplEWPsqhea3Qe7U8JyOVHkpfi9njc5--7f3by9_9pjMG8aUCQr2CWydCg4JHKoV_nAyyKiiBPOcF43cPKOTBB85GHl8HiDUd-sj7OMn42MxDABPrCxpwfcob-XfMunriCrAX2QQpwsoxByzYhiFtDOrwAxI6UI-MX5O9URC6t318R4_iUhN_cSXi9D35osBZegbaSWIF7dfbFix7JLn6mYPU_HusjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILqInobC5H_MNonFs58d7KYDJxJDd0hdz7EC_At-kj99W7_fgbaPMnWtc4AOT1-Cu4YEOTVYj9-GMuWFh6JPhRHjwrnF4_VfJYJWm2wGJ-v_QVxhKjuwZ6rZSLUDGHPolp4ci-g8yHmnxmZfxPE5zKXMx4YV5CQXZ-nI723olUbpxNAY69FF3AUpPCAvRmJnXKG63zrWJrxwTIFN7ybRZqCv98Xf4rQLF_12xAlZHVawOrv_cxGoT6V9y7lWbsUbsyKc-ayz009j9ywxCRMDspbp6iSZqXF9reaQcoOjDLNHCwnGz_lwrs-9wc2DXHWJz0ieDduGcUTEYgKQXEf6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seFVipTtKV8XmmA8RZbqMzOD4GBT8K5f6ZQJeDcMOEg95qanGeUjIxH3lTyd6QzfFv08Rn_JQZss7dMQY6p9kaXcIHCxQ7_H8Hd9i1vUwzZ010ETFdlbCxTATxmRxRLbkIRuOre91bai4HS8D8a7HPMnV492DEjyIPWOnIXIpToz_nhKXvsmktpOu-xQ61F7_jhvZitvRla-1HEtXaj7AoxLE0cS8dyMYCZ5rdCr4YAyklvTUPP8mF1aXQCaXUvol0Yh3H8cfFbL48VrGbgB2can74EcTI3yZVaQdVMu15I8pLO8W4rerO7tB2R4D9qCQf9_0H1F3w_G4Jx_4EPCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt4P-VEHNRlG1Bla8dJmnrPmyXJs6Q1jFKptx2XOGZgUMus971WwnK8us50y7JK4rux_8F1j5Gjq9yFrRSuxzRrAqnxKMMNZZyRC2EhsazcBCQbSKI8GH_DMpVpuiBlBa_2HOXdEilPTnYLrlHSCAi1MYrjZ9WdhDQKMqbq3DHBmd4iYVE57HG3hasSb67TnzhXM5FoAQnWXyhR9c4bvKCnJ4XesbIGthJ2MfiDeieu-hgoI9NPzvJ9Ht-Q_bWvzr0oFCtTzF9aQkWto9lgMoikl1vMq_FOGQNzDrRbdauh6CS9iJXH0I-v_uLNePmsD_WvvJwzqYdib4yPHACR1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb0C9Y4d1g5MuyqZwIziO6kLEgfd1kOKK5_SzYz_4Iv2VJWvH55srIqBc-RgAFXWyA8q5QJeb6jBptczCT9YlTtAkUymXU46HJoSHqqU0AwSG2OK1PQ1mMSV95DXfrJAvYZ-DFBxn9gmGSDPnF9bfHriUmapIeaLhIBZ4K-YuNEQFQucuJTNus0xZ9ENEz_23DaoReIGE__oQooVPPBRrVIuqdzzfnMStk8FStnJY2h35uDV8sbJ59LNWgqpP5GrN6RaaoPoEE77wJy6AZv3dWP0Eh3MUrXImNiSJ3Q-k6wuPOa9I1eCphHdfKvPekkZJ9dJ4TGZr1p2tn8JCiP37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=vw07Wls38N1fkSnxt9Hct74fNvMM_kD1ARve5HcRCI2wgqyyYwFrQO8DPC4s37N0jYrS9CH5gN8MEwjkuj5wG5VxZYu2iUrr8Vzm2re_GBjh8pAQIIgkGNh0yONJ0UKW9n4bZCqIkcZJy70vKZu0wE1zz5uxt1GKHjvtVwrzkemYBJwSK-i33HFrIs77cSJ0qcmTgPG9DV3ubnH2p8WVV7zfOwE6n748TXlpKdlABFJMJCJdehOysdhh1Ryg9JZU1xP2D0Yy7tUvkVC2zMK9Hiwrl6pTT9Gf7s-nUeEuizCnZhL7PIiedC-H4IJ1oaCuGZPPx49raqWEjOoKKeQ7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=vw07Wls38N1fkSnxt9Hct74fNvMM_kD1ARve5HcRCI2wgqyyYwFrQO8DPC4s37N0jYrS9CH5gN8MEwjkuj5wG5VxZYu2iUrr8Vzm2re_GBjh8pAQIIgkGNh0yONJ0UKW9n4bZCqIkcZJy70vKZu0wE1zz5uxt1GKHjvtVwrzkemYBJwSK-i33HFrIs77cSJ0qcmTgPG9DV3ubnH2p8WVV7zfOwE6n748TXlpKdlABFJMJCJdehOysdhh1Ryg9JZU1xP2D0Yy7tUvkVC2zMK9Hiwrl6pTT9Gf7s-nUeEuizCnZhL7PIiedC-H4IJ1oaCuGZPPx49raqWEjOoKKeQ7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmud-iqCcHP5r6TgUMxM8XKZDiXvGUGanUsh-rXKxPaX5zvXz3MRHZyxOYf0mByCOxyF9YLQFRkrOWHw7e5cITIYuP5BYG-Ja_1yhDBltHRxuciOGO8XjS8aAjU-CvlECCsDiQ0KWIZi3H9AnG3t_YUz9NNTiZUWyYEAp0nx9l-uxkrvulsYPEMqIVhA4Cn4YP8wqCRFTLgUOwozDBaBlCqb8EGettmmZY0gXnkfbFLiR-v50Z30cFbCwYqg2Mn5468UrV6p0H69IeWKjpNtZC1XiLsRoccIswsse_NdkSFHCaIMzM8pFV0AyG5CJa9SGoQ1f1nQDlYHaaeZI-n0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml_VAf3t9mZMyp6BFfaQkV8EVyD27KlTmv_Ct1QA1uYYzwmJMuc0Vcp43VKFdWVPsbVVX_dcryNyV1poJJQWO5LoK6CGlyjEGNcG47xJ0pmA1r7MCIOHEQjNa8IWk8nf2mJwBsGX6Nm8KECnO28vdMpPO1LbkHg8iMuO3dOG8AZfsGhqRMNB446aa3xhkkydlVG3PVbOPM-Bzx118QkPBakTKV7Vj70ac1UPQjR5agDELliPsSo2RniiduI_ozlsw93as-3WKvccYYNW2d4Hm2MRASXqz0JXTygq_kW7NrK7PTZh_D7va4cuOuAsjcY7RgGwMDrgdT_ni6HL7Vr4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rToqwTvbg2zgVRKz2myaJtnOL_GE0P0U17hxv4ZVr1AULWFZZzX_S4R_3DFlYGU_JGhj5qC-_A-oP1iAuA2wguCXbPL7HTPEJ-klov-CCLrLgkbV3lHq2EtinXz8zkV9UigLeDoMELZGEnQegWkcc8MIYGBx4RvOnVC7FAVg_15aK4MrOL03GUvXPmgZQug4zVgHK1GNeI41uvXUJxRgadgaMPzHoY8b9hvXuobLOv4_fVHozv8C83TNV2CzxqrR970Wnsyo9ygF3XHPHDDkWjZPbyG0M48KOjP6Q1sFh5rsvHEY5DRLEFI2TIBG4x2L-LMe94-EX64JYdGopdWqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxptYWJ26tBO6JnSimOa-7t8nRuCuhQA2jPvtiRnnuWnq2ez3gpgP5k0sxdiIA3SDPSeBcSUQEzSfNqvFkzO-D1fYtCwRhPiEdjZnDZAKqOAfUIuXTM_sTUcTC4dmWEGOg_QHc3rn4xfTA-GKZ5LnkrIvo31EwtaWjIv5R6VENDZMlydUBNvlLmH3HXgLVRmvdf_SD2JxCtoBFdcVRmqhFxAAOSkALzpqJVE37tUHpYjNYlPDCB6fzVpfOrDh4NtHmxAqu01hXjaND2jOQ8QN3s7_RqGY4AB11xPZNRT-CW3noo06UYAzg48ng_Q3rcWccZZkTg5aMbuVM7WOpclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUU1aurQittFCPjXto4MPgER7W6snE2ZBdE0VzOgIyqURX9fetTW5nmRMDPeYjGU61IqQcWOW5Qx0MgUYKDxAhGDDZoKJ4RkUlN6QWtm_uk3qTt-_xc2gp2k_XTAOSul0h9m7Q21O67tIMqX8cnDigcp3FQS1iZ5Pf1jm67QWl5rDzLarsP_41sVNgyx5yHzEnTRjT5nNhI7-EhcG6lJ1HNqEv_WphzTiKPGDCIX2QzuWITPiVnrW3fS7YO9eoeApicxXz_ffTbsJBOE7Iz0HoC4uCGiBeZIfu4H3woN6dXJJKpJTZVaMOwm-xIJ7ksSyPF4x4IhJ0X_uKFfzni9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUqYpJ3ZnE4f3lbVHfNTvMHzBQxRxT0L4u1WvsecYoeQlWdSvu7MUBbeGpvRIvq5hf9X51kq_btzWVAsgIVq5jV2-hvr9te08rf71eph-8ZgxyiqnKBZzPZixYT0H6yKywdN_oibHoztrVSeQSvqerZwpZKwpfZ3q7ucxcGXb38qHc4yzVgRyegRmoOWA2A5SjdlHP5yfWxCqKW1xeHA_Ycc9hXkbBmzMvL8RaP9_wxvrxzGZoZJksokRmefwZGT81Kcn6jZ4oeBuWZ-CI8qEbaebFdPEvqfd76dYX2MI9mnyJkMfRMqhND2D0mt57FWQkn4jZ71IvQJrnLgZ95R7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvKOWVdgX7sl1I-kodPjFb5PR7D2xPsUlWyxY8BYO1Vk5PH1p1BM60A7Cdu9aKrEyKAUWdD0K68g4v7MWX6U4O_W7VSYOHJoQSYNra_wGAcG_2XauQvvUA4NkqsQeG137tQTOsa9KI59BPfKg0pSekXqiiTcEV33o9czRNeSrVFGx6RrAuSV-s8lMrAKBM_5oxnckuAPAGnxvIDerCRSGGaCsLxilFz3j3-gukeeZyIURUTqam62PUXpms1GKisxfuZU_V8X6YdXmFfS79NpNiPdlhXOdcElijoK-I8uFO1WJgKVwcWyLmbQ_g-mkbPY3jDAd1blV6H_jmRqQmOmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk6bZ9227jV3Mth1H7xXCXMFNCTa5FRlZVGR6QwQKMaIX7lVS3wdT_LxlTAsbqV4IF1Up3AlgJgjdzCRNlgm54v-Hc9xSxSFSr0_rEotUDzwmVe96W54w90M6mkOY3OWGqPBGV6DVpcIK6Lj9bsCal7emYAQeDdSfsvbqQu8eleI9KgBEJ_hnO5Lg8a5qwbWecKcY9DMkvSmE7o-mtvRPemj2QjVXPtUJ_3yvpaUN2k-JJMVsVuAySzF8ZLFXeglBnvLLzVAaZlMsKBPc_3BbKpqPrMfeMKTFDHaQuKtWZWnv4-NMv5Lo5HLCXvpa7RBh2xuBE2213eVtIFoWfS26g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AWC-aDWsmB_WYot7ZOSY1oLGKeh_cLSoRRJYhm4QEWXz73Te7j7nk4_XrbF7NhPY5zBSF4aB0tZt7fd51o5VFj_GLi9AtkeHYgGDels29ukaM_rEK0PrkHa1wiL-FXZ7PjOHRfFD0pN67uWRBMWeG32rbCSVl33qMzpEkxkqCfsOlRaMl0yG0Ny9aZco2VtN3XlKWtxC336sWAeJ2H_BOVjW_VfeHCcYQN_tbVs_78VnyyYaU-yizDZ7t2ofr4g9ZZ60OW75DmR4tT-NRBe9PppXq7ymXr5YV0isF4eTjScFNNQ2r76lVsXwljbERhzwojcEcuT7ws5Q-IdPSnZG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AWC-aDWsmB_WYot7ZOSY1oLGKeh_cLSoRRJYhm4QEWXz73Te7j7nk4_XrbF7NhPY5zBSF4aB0tZt7fd51o5VFj_GLi9AtkeHYgGDels29ukaM_rEK0PrkHa1wiL-FXZ7PjOHRfFD0pN67uWRBMWeG32rbCSVl33qMzpEkxkqCfsOlRaMl0yG0Ny9aZco2VtN3XlKWtxC336sWAeJ2H_BOVjW_VfeHCcYQN_tbVs_78VnyyYaU-yizDZ7t2ofr4g9ZZ60OW75DmR4tT-NRBe9PppXq7ymXr5YV0isF4eTjScFNNQ2r76lVsXwljbERhzwojcEcuT7ws5Q-IdPSnZG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlSWfGy2LYRR_VsKqQJoMzEOei-OZz7btZoRGLtMvEfogcrFDAB-DLZUOFIdLHaJ1qMA4ftWEUsVheq7sW6mN5W1VYdY4yaIXl3T36X4qj1s2vPgZeiCPAXjJa5Kd_DpMeflaKIcU1u3lySjYEg5-zoOJLNiFOYb3rIdOW6-hbx-V5paR3U-DJRfn7pemjFFP_XMdtJBCn0shweFJ0xtjO0wCcXRcNhZOl6GiqQBHgh-ooksv6y09Ym8yqthJIqaLa7RdTZ7Q7vVODvCA66XJMmh-Gl9dFTXVhmOH_moT-I23mN4ZBuvr2KgC4cz3_rBqb04ib8INqBLrSrRyRrGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j05vyIIaapolMeYF2H_i1cLUnC7qBTjajoPFYobX0khvnKX0y1u_D4F_GjxDrHy_HLd2RMg7TIzqcF9dM11VcVJYFYqag7_wmJrhQxlMJXZfbWygadrElTGt3Ml9f82y9eFo3Xwh7iTcdYOBykKi3mb8YNG3W0oLX1IQGkoQxxLjXXjYQuKdDeXwlc4e75onjvnhgUTvTWGkztYRgpCCakW-DYRHUuZiJ2InsQxe7BKOrYWGphqR7SSeQtlh5XFRzKX0Vr2eY7Nz3kSn43cQnnG3CK-DUP9WBHA3MeuVMhrfh93TkG5b-Dl0sLivyUddQbcIxLKZWHHDgEsHOpvnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=q0Do8uS_JwSHeim_Jbw3JYgSzKzKYC8GIwGVyk0P1sQd1Ld795rhuXjsw1u2wtjpHtIEaDBpTp3lfH6896cV4YqH1NIxNTAtiqr0nHK-Um9psHw7J1rky0OKvzQtew3UFLW5JxLhbsXxvKKgJwv2yhL3S0QFHO9OV6tM0XEXgcppDdm5zfaY9blMl8JdpA-IUHJ9yZE76UuZM1KF44F2G1fV6_2m5bft4WEpa0XNg_6rwln_3-Mxeh7qyx5-f152IV7UWbS6308xHfJ4Yy1FupZwAwXrPw6FxWL8QO6fcGxVIXmt-jfWKHTjy2l_tUXRojReEYW6GTEieHQSMbk3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=q0Do8uS_JwSHeim_Jbw3JYgSzKzKYC8GIwGVyk0P1sQd1Ld795rhuXjsw1u2wtjpHtIEaDBpTp3lfH6896cV4YqH1NIxNTAtiqr0nHK-Um9psHw7J1rky0OKvzQtew3UFLW5JxLhbsXxvKKgJwv2yhL3S0QFHO9OV6tM0XEXgcppDdm5zfaY9blMl8JdpA-IUHJ9yZE76UuZM1KF44F2G1fV6_2m5bft4WEpa0XNg_6rwln_3-Mxeh7qyx5-f152IV7UWbS6308xHfJ4Yy1FupZwAwXrPw6FxWL8QO6fcGxVIXmt-jfWKHTjy2l_tUXRojReEYW6GTEieHQSMbk3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbdWg_fm7SdlCDoBXtLZO22MoCZZDlcBdV5-zsXCedsg9A4g7qv-M0bTgkJl5rOyT9wXZkI_rdg-5xYZM6q6FEfytBrGbEq54hUcZAQQpbmfo9Xm2Ze0tKqzdtLyPZnIgtOv6tKbSCKPiX2zpbgDlZ0mbj3IoKl9VYFFT2EStjhstuUFNngoatvVjXaegK7XriWWjLit25GgIcgJ4zmkkB7amfE7p4eTLfpbU3hYllFf17xkxm6kfdIPZB_ooO4h9YEGYZD-Iwi_QJfWlLk1af2IktF3YRY55kdfGUbYFv90u47lVMOYet_wCP2r7uH60qgkPwZIz6otvfRdjqA_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxXMq29hxdP2qLLuJRlEgL-W2wl8FFfOVY9I-Kd2nCwtnYW8dkjyYIgTW18-2AHNx89M69QLf94RrX1Sx_IRQKpH71j-6338OQ4w1g8kHK1A-sWC4AFL6AZxCuQozUAk31640IQvJKhkqbCH_UQv4SxIMfQtFZ8C-Lg82anE0E3HDVWXiyJxOERrvzPCRCcBq8VO8te1lQQj8Jk4_1CMW0leTb4aFkkC8Nbje173h0-Pm3SvL9eacpi-vkQhcYJ6nmB_j-tD_QVAXsbfmt6oQr26c1zHU6b2hBE45rchUl1MlfslpBN-z3VonIshN6oyKzj8z_Yg5k8rGLTWbM3lKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNlwxrVqwSvlW7vHs9BNQJBxH3k19bPJWvSll8EuCmtH-LFxBd0DZSKcc558t0PTENFyhf8OdCChGpbP90SlJPsKIDjh3rZDzdQPRfNQLSmFs2dqIv0-TRxoB0a9Tg3cDLAhiI0PDvaZkvP6axcl0nef8yz7q7zJA8Hzr9xO2KiLl8iRY9mfatRmre2CoeOkNtdC10K-GtMCZyXeKBFUqROzMA2vCY0ZoAmKym0hBlGDR50A2PuRxqhYfxss7XnihTU9fquEldCGNxWKP-iAqJfMPXmcqhrX16Oh8nNwVmAtzR4LsVZkeMuxwMZ3q8sKW1_Crb3gz9wTkCDKG-Pjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=TZBY5zU4IKW4JxMFKnWQ_HVKMRqEXC0YI66iqIOQ1qgiVXPYuUl9m2jaaaSjxzDEsIRlLfr9ZFbL6moCH3QuJHyS6IUZ4WUY9dvqUKTvdz-KGXCxN2i7B_x1AViLvmmDC1hmmhDyGwiP9oU8XJ1O3b5Sh_XeA_o1qRQCRRcN7bO56vk6-VQKwbXkNLTDVlVqS06WwvDT8PQUoIAz0rvHrj2QvkBOvNFYCb2tnBARGm4cgTMadQLrD9n_nZBiww9nfbsIFonAhGowzWqIqwIAqziItj3AvWwDbM-bAR0onujiYFGuU6vHaE-NR3OTJfX1gZsWUnhGE2nYDRur9gSeZ0TibkCqu3gQXuZbgnO1BwZh9pNXDr18Mhea_ZSlCy9s2JHjlKKVSloiuztIzylCs9fjFjca47fUz7okbnokq4T9rokBqzZRlBp5Q7eh1Xvg8hlklLCIsfyx6yq5ojdSi2pm6cnDFDUsy4fd0lldraFjfDUBT0KeSKXL52nnLMw9ObG5-ZOSRM8ZIXOrJvr5v6o8LblcTo-MN0gaGleZlanTO5I2I7Av60vpEgfnjNAb0G6Q8IL7zsu_2kdumqIp0jm-cCLZYSzvWn2XhfFmZdu1CIuy8fihsdWmKI-l72wfJys4B7-KHt58ZKO9gsrMm7p51bxz2pAD55CNkD6mOss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=TZBY5zU4IKW4JxMFKnWQ_HVKMRqEXC0YI66iqIOQ1qgiVXPYuUl9m2jaaaSjxzDEsIRlLfr9ZFbL6moCH3QuJHyS6IUZ4WUY9dvqUKTvdz-KGXCxN2i7B_x1AViLvmmDC1hmmhDyGwiP9oU8XJ1O3b5Sh_XeA_o1qRQCRRcN7bO56vk6-VQKwbXkNLTDVlVqS06WwvDT8PQUoIAz0rvHrj2QvkBOvNFYCb2tnBARGm4cgTMadQLrD9n_nZBiww9nfbsIFonAhGowzWqIqwIAqziItj3AvWwDbM-bAR0onujiYFGuU6vHaE-NR3OTJfX1gZsWUnhGE2nYDRur9gSeZ0TibkCqu3gQXuZbgnO1BwZh9pNXDr18Mhea_ZSlCy9s2JHjlKKVSloiuztIzylCs9fjFjca47fUz7okbnokq4T9rokBqzZRlBp5Q7eh1Xvg8hlklLCIsfyx6yq5ojdSi2pm6cnDFDUsy4fd0lldraFjfDUBT0KeSKXL52nnLMw9ObG5-ZOSRM8ZIXOrJvr5v6o8LblcTo-MN0gaGleZlanTO5I2I7Av60vpEgfnjNAb0G6Q8IL7zsu_2kdumqIp0jm-cCLZYSzvWn2XhfFmZdu1CIuy8fihsdWmKI-l72wfJys4B7-KHt58ZKO9gsrMm7p51bxz2pAD55CNkD6mOss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPjpmQZHRElXMvFvKQ0lXU3bwcJ2FC0z7t5MmzoC-2nAZfMFDrLWMl6durQZHMnTvAP2iYApbaPBtko_NR8QGE4JSRY9OcY782oWSfZP_v52s43vk46VwYKW_CErfGD_khL9aawvNcaixqYH_X9VztZSE7vpHK30rByEJpUdo4aSBpPZXyOXaVNVQf9oNa4IW-qfE118oOGzt1a5UaszQuioewin_FufMbItGNH30DGwnpXcFPwkLOp4RJXbTejvab8Lk_lmJk1OAaZklc9IjSlWa6zhDTYIlez_VHENUW4EtK3bBbI16CZoTm9BjwdW-brQHiP9oD6wCUuznP7jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI9gmejFr2hdBaF2z4trp0tPJtODhU-UQTXlw4mSUx47I0UIulhECkLxQb0kcxpWuBgAbwfDcd_eIWR8xeWy6XsMohC9_F2R_Cq2MdWgfIkp9KNgiWm0SgYyuvzEDeaXC4J5J9-S_wJbX2z8Ch20WYj54WzagZsQSFgpmIHfUaHIN9sd07iOV9iakjOkSppj2bQFdrAfEt85gumH--7B9k9f5HU0QQvhW3czgUxEnAV9M_iD6zv2LZEUJwDt54YCnpqWgyRipvgtYqFXvt-XlU1SLz3znnk_UtP5mVYXfwSmCkRyVGARo3cUppTMv5BzFtt0l77g-NArAYGak0HFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxSTJnWAExlwhFjbcKnwD3TBmhvL5vCwhw26IaHBBkqzqEnRheP-cVCUTRj1NBFj48zCnh8cz4_qvXadf2LhX20_Zwa1USlv3SSpIPmm4MadAFOcX0sAiJ0x21Om6W7rnCwFUD0uhtjTPy78e4Br2kCJTz7z7zxLgNjeJwKkLwUbaR7abFk00RRE9AtW4NAkBnAieAqI1zhCZ0zgKrj3_fg83SeciFAYrwINsj2VsSP0ddXvhwsHCYapf7TXLHhlYDCR4jQP5Pyrr5K0OjR6jlh8TFeC1ZxOB1Ke9NbFtVYayfBPcRbMxpyeOwzgN5wBkwzqYsolFnbGcyNStOiYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLyVtqjZZVrX7hlxkQ9dV1uiWp-xtvCC4H_OSH5580n6uGrfaOYtec5Tgm4ck-oxcEiyQV1JFUqBqrHFLXdqinYmERDqRZ6e7To6eZMHjd1M8-dR2A9JGhKvbVyG7sw9clpSGFZj3Z9DTQIXvIYPRMZy9VmdrOEz2Kxom_Knd5YYeo859V9mi5Vnfq68uzU52t-ynExUGlNH8VfVLScdTKlFNmqBj4radgCV7DCy8FwVqKWDZBiiuIl27CN9cijoOp0F91LI8k2prABnX22ym17D94sR7zHPJaPMtwwNompS3ybGCAMvmPKWHQdE8v2-KjzauQ-wYUEW_zvigWlbfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPArEb-QB0UChTbq8yT_6ntUC6prSLIv8-O0vGvjm77D2CYPAi4AJ4kf9wjVx6LWJthYdrw8fpMPRYs40oexantDsDWtA2E6e6ksBIvvaAOIK93h5r4XmW4uG6-mxh_SsY9XeRugkmZEtTe8Y4T6gp_H7aORc1F8y0S9JDEblOsqrgEFtidgxnm_cyDfqN3YQrKFGi6VvROTYlhOQzwutxvEGSWPs1n8Yfdq0rhaaDeuicDDr92Pvvjjo6tzaPSzaKLHL1LGoJGumPJjdr8JuBRuTMavJgnUsnetG2MVPR7pe4ZSmG1BLrGIpRhD135IAqAWUoa37j2kplLTwimUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=LbT69smg4xNLufJME_tGmOBpOeCc-MX2lJ-cYJzEie7Did1iR6BMv00rPWuO_go4D4ZHt2XQs93zU4n6vpfgBoS4ppgbdgXlEWFEtS9cZnD7jygkYGtUu9Ks8-IzQU2tikz4CFSUD01UkftOXyTrcsnYm6kU5OARg12T7NvXuNgmikSZ8vHThaiGVOdyFaBW638GHo_0NNpwDBpcvfFljNgkX9yH-t3LA7ptnxPK0wWseWK3_WcFWKrrQmZ2ofNpntHHswu3uvzhIyQn0HLs_-FQQIFOFitGM0hTgsOjLCtZ5VOMmPRaBqBjTG3IUsPBXTkbw8_eSscdwNVAKw5GWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=LbT69smg4xNLufJME_tGmOBpOeCc-MX2lJ-cYJzEie7Did1iR6BMv00rPWuO_go4D4ZHt2XQs93zU4n6vpfgBoS4ppgbdgXlEWFEtS9cZnD7jygkYGtUu9Ks8-IzQU2tikz4CFSUD01UkftOXyTrcsnYm6kU5OARg12T7NvXuNgmikSZ8vHThaiGVOdyFaBW638GHo_0NNpwDBpcvfFljNgkX9yH-t3LA7ptnxPK0wWseWK3_WcFWKrrQmZ2ofNpntHHswu3uvzhIyQn0HLs_-FQQIFOFitGM0hTgsOjLCtZ5VOMmPRaBqBjTG3IUsPBXTkbw8_eSscdwNVAKw5GWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm8pk9TrZDb7K_D2x5wOGDV7tq9HOP_0ItU4agfJS1-hh2tRMfIXJazx9sPWcQXa02UQ2O3E15RnmbAXC6KxJphETkAWUPyY0HZOtqZ_xIaB8gVy2j16srDluVWf4jfehcCgpF4bJqXW5fyAqGQXeLIjehaTWLdSEjCcZYgyCFw_DXJTc5lEyPaspw4pE_-cV9gXGTIw0dJnyLCu7PJBf61hnCJWEtYhZ6R3U1TtWpocIAOBNJyrUfWGTUiMbwKiEp6nH2vbIHMYB3WqQ85R9cXiIMBZ-GTnoyHW3tfOn8CyBanMSVpFAjfMcicv8To261IJc-2yy2cXQC3EMm2q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pevZXSG2qLeSNXSbV3lxtVQbniZhHQXqZFzNu1c7_XncHcmayww5NGaBfrK7uaZP4MMupVV58B5dgx-alHtqo2-cgdQ9uki_SlFM9hD_e74T3SXW19eODHLn-hbZrj8D4-HQcNuRYu4T5zfLE6zSq7jG-zqhcP1frgaebLWkslevYiYR9XNq3-hZZLvjJF-XaywSQ8gIB3sW0BoXpbGotXZd8lbmCvKoQ7ufK9Hjxbb9HhJcx64I0aOvk1FnRCzLLC_rjXQUh6-nKduH-DceeAxqn675-MlkzmWB8-a6kRYOs6dDzHdYWysgMnlGUw6vePLhtolPH-25cFlfZTOanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=uN1UQWideXaEd8X1Hx1darLEZZcdptd5wMKRsfvY6vKEj7_j9rgJeNeZ-L-vsfckHfbEAfskdlozm8DXAtb-tIqufFr4v6R92VyQtoA-YDPi2rezYwBDGdjrF1-SYuTUo-AgKYD1ujIN5eeHcpeHd9IG7qISix_fNtMf_4P9RWaqrjQNRUD5p7d8OA3xwohUxytt21fwonO4cbjRieI9wbGBayJjbI63IXJ0iG5Jif37hYPRe7IkPaAiV5k1UuamKW8J7e3W98CarhhXzOag4xZ1wqYWWl7ECZ0MTJFVfesXlwsyJPw0In2rT6s_wqSxN7mOS1jypHRg9tiQjRSN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=uN1UQWideXaEd8X1Hx1darLEZZcdptd5wMKRsfvY6vKEj7_j9rgJeNeZ-L-vsfckHfbEAfskdlozm8DXAtb-tIqufFr4v6R92VyQtoA-YDPi2rezYwBDGdjrF1-SYuTUo-AgKYD1ujIN5eeHcpeHd9IG7qISix_fNtMf_4P9RWaqrjQNRUD5p7d8OA3xwohUxytt21fwonO4cbjRieI9wbGBayJjbI63IXJ0iG5Jif37hYPRe7IkPaAiV5k1UuamKW8J7e3W98CarhhXzOag4xZ1wqYWWl7ECZ0MTJFVfesXlwsyJPw0In2rT6s_wqSxN7mOS1jypHRg9tiQjRSN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UalKFD6uqsMM3iNPwa-lSlG6LwmSqNsgk4zwf-aNJuI8ZonDcjCZQkcXkPSgEoaP9AjyLpmUSqXiUlSThAwBr2aCmdfkSuty146357FJ_hMxVtVTSwiPfjidRl9iVzM5ZD4G4tFK36-QR8W3sXSr5zkfEX9-rGw3mAQLQE6zB9bRaIGMgnF93tiMgUqv8rtg59MMVNiuvdwue_Cj8t9tK2Y2DQDFRrD19veniwkRAHE4zAV-HS9Xm_r7ajnU6CUoNTFcRfZpUfYJrjOeI4nYbClM0xhbp8ncrbxa0vfFb-sviWX3DAj5GqK25B-GYVoFxUuxIYUEucmmzM38av4fSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=t2c90Fvs1mU6i9u16fOa2iQzk-4TjX5U6VNYT8C2UxURbn8bFDeMdCPGeRCH3MWXEV_V7JIp6U7XPyIBEEO6bT8D7mWidBEaydvRllrhWsCZTh-KNYUkZLrAn6frJrxzHrEtxQiBLfuynwez_7CvRBD69jVrm0-4JKKNMlxLVRXlsWQr9TDdVCjSgrGgt_FVrDiFsthBkrgX4xfjS2tM7eDncueaukOdZLs0cnrB2vOVsVAzQ0jFQM2pnfhPZPeRS1On-2tPr3uPMd5Vpzw1xvNb7fJtcCm-4YXste1SQl3kJz6Kne69IG8xTdEQJwY-y4A0J-j4Yl0IOF6szaqoPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=t2c90Fvs1mU6i9u16fOa2iQzk-4TjX5U6VNYT8C2UxURbn8bFDeMdCPGeRCH3MWXEV_V7JIp6U7XPyIBEEO6bT8D7mWidBEaydvRllrhWsCZTh-KNYUkZLrAn6frJrxzHrEtxQiBLfuynwez_7CvRBD69jVrm0-4JKKNMlxLVRXlsWQr9TDdVCjSgrGgt_FVrDiFsthBkrgX4xfjS2tM7eDncueaukOdZLs0cnrB2vOVsVAzQ0jFQM2pnfhPZPeRS1On-2tPr3uPMd5Vpzw1xvNb7fJtcCm-4YXste1SQl3kJz6Kne69IG8xTdEQJwY-y4A0J-j4Yl0IOF6szaqoPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ04mjHGz-Y9tNcKkoThjWrh-Kn4h8RzHx3oO_kQCYhqGfrLMmYn8JGSgPXcNlZjvbBGGm1LBX9Yw0Cnfi73dHYDtJlydoa6xWicn8jWFaC0uC-go_kOatjEzp8oxd9pIxZnXyCFOz3uvqn9ImT7g8sCJdh_al8OeCJlBgrch7_Z7sY2BpT1mlETpqRlPgpguf3ADS4Qe179MEz7v7X2ZA-enRJ5g2LaRtdbO_PVp1k3abJBVhCDJ4qD-tSjt5scy9yIOdjkCtD0TE95c9Y0EBVX8GOWhtx_QIsOBVCfbX8npG3EsKlVLwvCPXntuXKidtIVcdAjmbQ7Sf_K9eRlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxpj9ZrV5oQJqkF5RpwK2ZGjY61uJPa651tZQJcCWf4RXhGkwrqaJeW4CLUEVTAX9U_JF_jAlYLpiFI5sQ67ClYSO-gEr3IG30aXLmn29J2Fp3BHbfh6URplovBaC42qGBaK-4kNRaNp1RDzKvcSfDKB4bDvkAI_dTOTAr90F-WoObPCmiVKbJY2hiHCqtbb8pfjtpYYB3Sd1gpbCNdmtj1xqaCiszKjob1Ob0WTtrN4dL5GjJZXQE58hGnjKOEaJujZkvZmwm9JpuC8m8WCi0h66au1xYfnsaqKaVHDDoZ5YsQC7-a3BkBOxNSD2iiEEl-B9__RWsUDpc6a0uoeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdmjhuFCytNCKkra7KlBBxi9wz5DkQBNGmZleqBBkN969tJHCzupFaOLtud5vYersJSMl8dYMBDBwufCX3KR8Ix9NxPg-xuapKzm0A9UiDg_xZctyL6IP0i7kNSJBQ7vyPwiwkAysZcM-1WbJ8GMZh-ygK0SnJhmVezsD-RNZKL2uqtvI-FFLsYOmhXOnWanYGdidLO22PwkTvPedc3euxqkklNNO1FVsRvWWDIj701xJryANjRhmBcDk-dO5RCEp21az_pIo8TXFuezAgIAFzbKX8FFYMeRcyKIaaSL3V7l3Hfw6lAnURa_BLyx2hGfAlLPxgJxVUVqjCsBv3pGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGV73cRSAtA25GE0ztkaguPqZVFeP43of4ExxGY4utOcOPL_pqlY2oUSUlecIsf-G3S36sHzYD-NqZE5rLXFfvQ8ak49EUc-PwEOUcckLfcT5BEs0Fx8uO8i2ivOBGwX_w38BpXEEwdk0R2hOPoRk6hfqUAAEGN0gSq2bVEi5rcp-Bh-FqwKAdFuKct2dpa1F9TxmURbj7MV5dvqqwB8yEn8fkvsFUiZL1ku-MiEJlUo2JQXs4GlZhElpBteA2Smli_JMfp3u5s4gTaLrtUWSKiUxrwAAKKuYVB1CQrwgeRmgbbucV70aLnJuYSR6n_T5BGyRNYiRpd-GZbc3thXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=s3Debcw1bGaLICdWnYgo5iXW1CpNNnGlbURoMDsMeQmV6o3KiZyHczklSsKfiP9ErzwillUKdQbeeMptR2cRJtZNch7P4NjZQPRyGn4lrNe6pwzrIFwhG9eLguNxfdyyGeOh2t52afc-ZsFt3uSAGSPHHDxhxQAeEvnHWs-cftxAayRWloHgjmyOpuyoN_ehD3sN17rG26WZHg9hYcTdxCIyE3ogKGMUN96MWQrirA62m2FE6DuQjPfnfYWophRTxSOhNU1Sg2Ga8GffPtZqjgh6tdKrxCPgDEUqNT2Ac8CiSEvwIHapwSDqtroTj8e9ou-jWqmmmqQCh0s8McjSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=s3Debcw1bGaLICdWnYgo5iXW1CpNNnGlbURoMDsMeQmV6o3KiZyHczklSsKfiP9ErzwillUKdQbeeMptR2cRJtZNch7P4NjZQPRyGn4lrNe6pwzrIFwhG9eLguNxfdyyGeOh2t52afc-ZsFt3uSAGSPHHDxhxQAeEvnHWs-cftxAayRWloHgjmyOpuyoN_ehD3sN17rG26WZHg9hYcTdxCIyE3ogKGMUN96MWQrirA62m2FE6DuQjPfnfYWophRTxSOhNU1Sg2Ga8GffPtZqjgh6tdKrxCPgDEUqNT2Ac8CiSEvwIHapwSDqtroTj8e9ou-jWqmmmqQCh0s8McjSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_NeDsvwuJP20eJNr8jBlxPmDsQr9IkddxAdDX0zf9MfRmWtVL23JQ12n0ZfkBRhXQVutq4oNbGkPB2RPOfA_asn18h8_BB4AVl7A-g7h-T7jLaFo9mxBcVMdXV5_PI-dFiPIIiLNyeNzjaJSTJKKXN7LdXM6OvhypVSlX-HPjZo_gjpouLDSKlYQc6Os2tk1rJ4MEdXpj2CyZbXoAkWNmMElKAKXHlclz3CeNylUAzuJEPePogQ8XfVmDfMsvdSrNdt5FckYNV7b4PgHMhs2pm2uGxcP29OCvBQg214PnbVWIuw_mXEDXy4qA5W_dpGB2BpxABDeGfp51OFlO26zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohuqa-9mulikrvM3lWaNlj_-j_QCcWJWU4tTDe9XOGu9Pr9mhOAZSbsaFuCIxhzqN8UZSHjgw-ZWyhySeSROO-Y2JcJkOZdvweIw6iC6Gi7WiE9qZ1_CZCixb-N1PWBnABnlRWwoIYrieXWEGWLXXglHr0kKUkX7Uh9f58xiF5yZSrh9gKkIMSYfHdYA5j250q1rPkABXdjWgSOW58CNUOpOKENQ034RsG54mosaBfQybpk4RkpSaa2F8coL2KV79clGHYOM6kmkR4n_5Mx_11vPP0QmxReRzSJ9LgXsXAZ6vZG3P6gb1B5bO-qFiceF2DDzYBT6ZJ4vq6dmjEwaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw4LGFTwPmhBW9pc5zYVf3o59j-5FZSMlf0Vzl2zkKy0vFUhOUS8R1OxF6jTolXjqzcqB8sqqo25t_lC9HJii59Cxgiuv4l2kdb3BOFZvA0py73_Mwqm9CSGBDYisUDXKKE28wRzvLWhNxD0Ed1PyLmVotmSTEEzNopOTe0lW-1M9QGg2BilVcumfKpXb1dvsBOFGzFm67Tb-QpWQYyiOqlUNWsFlylak1NqZy3KnJC1MyBwSaSkRGUnkk0WEHm7djxqHz7A_1EnXOiIw3jOg1zAqD1tssDQQdSuI-GzweiZo4FXNmzfXg_hI0R_9amz4-2hmfQTuAok-lFFptXmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVo2RSHy5tcmaVuaPG0vEc-wXgWwHcvLabRBo2RlRXXnWYYJSFNAiRoiUpAzyAdNtq9vF7X6wTqUn5qtucYvhrrgyKAycPeLn4q18SBLHMA9FR-P2XJIgkDAQXPcydtcwleEEgYMhdj8b5sjGf-jQEbzA7uH2oXAtgsNgaXZqVyBGtJq4HLVIh8Ap9Zu2o2BCV7nnmXLqBoEq9c3jLmlazutiBCUzubHBPraX33T6gUF0HVa8JaZHWn71EAADH1jzNVfkosSrEbQbvaa7GrhYCHrNcVMgi184ygO_f4C31WnulWQNZWVf5HBvzGmq-2tGayXq_dUQk92Hermyf6Ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8hdihpDu2_S_UPHaOIMNY3r-TKfny-U49_s1OfDIgqRsSiX0eaDJlW09mdsdmis3xDre-E7KXarSG3euYcAnKYv2nyXb9743heDZmIP8-jALaBq_YnFcR5uWcXmonMga_b6HASDCjb051Ef74i3AV-eePzP6m5Qemq1dM8op24uc2D6yW6IKswU7URW3Ls1Hv8xtlPZsT9Qrwdht3vk3MTevITnjjbOINZdIsItNMjqyFabYHKCG2fVk7_v0ziQlDsGE-8LCD7dJvfCq-1Jtco5pPGJj621HPBOtU1bml_oFxG9t-wcMzxdcquvzZh_xVyxrt1e0kG5yjf_Qz_5Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiN3ovcoifLMcDW1lXisqn1gAQfs8N2J4FSniR98xkZGe7_d3CpwxF5txAaqvqeUEePMmxZHXTtnv1lCXLNdk5YXIpkuhi1mJ6kFDYlnrKBO57PwyR9PTN8HKCD4V1omWA8PpGVByPsvdPJ54yFzmmlvHicQqjtA2AyaK4Ad6Nj0OwD4DAo3raXNChfgfNCB9tUqkXLIhvAbYlpp8vhg0fOft2SZeVFa7Gy3tRn1-M4wQw43TfJVOoFHVJ2YWd6wmJu7F1059TBogukDW6T4CdWytctr32ky-N8gK3C5IcLU89DqiFADvHqzZBuATIYpBCl5HGetoCREOZqYb79XPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNvtFVJIZL7zHzsVPqwI0B6J8FQy7gDiQE4naODamjQ2PQiGChIIHn3KLSEdkE7VgPXU59SzNL-Z2x4sxc_0RKz2lJnhcRVrM0nxX1Tm9v9xyviHcOzUYUQ_3uuwqYpz1gtPlQNdOUQLrkzcYxYG7I8Dwl4-b2QB4cKT5b4To3KCuLZZMtvUCQzbPS39g7OjNSSESyV7BhtOV4wpin0fg9jEjfQYGyNO7UlfQUiHZe6Szv18q4_UCfVO6xO4rzoJ--2WuhwK_O_H6iHqCI6029ib5Xw01jevy94v9dur-2hTFjeiZ1hlErzzFWSvvNtkc-q4WQcaRd1j-TCgF61tRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZASuE9IWKxHL8Ynec8ZZlU3W-vkGFMuo9rRRjjTqiEYeWsdAJP-lrT56Am6Z4XZAvwstpzF57MB9Rdt3MwLuZXEVgY5p0lCdBSPPyD4FKFqujZTwuWiskF8DZ8vM3TlNMeuplHzY4rLe1klvufhy6ZP773il3LVOK1hw8dbnlRWzSG5iQwGUzXbG3spmDpBGleYhmaldC3fzB7BHEhtgWpHRMGzNrRGx6_6i2NKFMHdziJSNKOexSoeuTUR2kRjd9YjPhM_YbhlCO8eIY0k1KBEyTfsn9G2aS5Tj6_JkSmlvfwAplLrNjyVe_8UQwYURcnH8znnolknzOr12r2Msrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRhemq4f9QpWIcHTo3YrRvhCBJO2wZJVKeXW2B0206bycsPH22X1WsfaMXxie4e6yteEzZ4O47Twcn3pXp87F7UdxnihxgNjO_VvvpJ5jdyzhh8r0i7n4x31cnZ04pq-9-mr5eXgZQki9UYh_Pr_MmYAmQT4sCkNw_5fSuM9r8OT1uQcrScYOJ-Ny6C7x293xQWiMz0_QgFcrzaG19K5wg-Tlwy00JBOR2MkA98N5MUat4_bonA7-CwLt9IsFMjTXNIERZhALoI2sdafe39RvrMuGEAM72Xh0STCvSl7jFo1yefsm1fRPJDDc72E9hYTidU3c0pJWDtkr6Lvk8TnqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6-uK12WBkN3issn0iF7L3MjrWMvgMJvo7YSsHFmUCVhgoqMO5U5E9_AfQwTYoMWYu-6BiSI-QG1xeFR5kZDG_toXpJBPUonTPQeaAi2WscsjDsYcORSBxITVGGH2EohCEh-AwmgdllCN1fvKZFlTJI5c_6RpKk97h5Er29-4W7oYUDsmlPqJlqB7d4DRyxfoDsYCRvDZazT6V3WzNjjft6IZnV3xi9Vub_IGdzE-sYXlMqrxUmpuUkGlzr9CvsLRNsmnBhIsnKr2iihOJfxVBSRke1m_Sa1yvVsblMBZ5qLBvx3q8MnmTi4eiriSjWU3oy2Mzz5w6TBwf92QSnybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=r-7PNdtnSc0BfACBGti5ClBX90LOnPMdmDy7qvNZf34Ly3iJKVMV-dPTgugwVq_FvYPVOS-NU9K_-4ifzn5WEGPVk1tLB_nUFUBJcIUYWjeFLwTDqFu1-_X-CkKr0uzDWsUap0VnCT0ByQuqb_A6TaBnZEw1f9IocS51aJXxNAEMJP8IkZU3FcjKK4BYjrFCUdMDKIlFBXlJb82yftaIIbMPktLBaEMs9VEGttVqqT7UBh0BnC_x96p0uPXjYw37_E_4T754QKq1EbeCFI3FZiVJ_OD1oyxN6HdCgiyFrDtrcpfrA37j0aLlV1QUvq5-y5T1U0b7DO7KjNO7Ko2KNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=r-7PNdtnSc0BfACBGti5ClBX90LOnPMdmDy7qvNZf34Ly3iJKVMV-dPTgugwVq_FvYPVOS-NU9K_-4ifzn5WEGPVk1tLB_nUFUBJcIUYWjeFLwTDqFu1-_X-CkKr0uzDWsUap0VnCT0ByQuqb_A6TaBnZEw1f9IocS51aJXxNAEMJP8IkZU3FcjKK4BYjrFCUdMDKIlFBXlJb82yftaIIbMPktLBaEMs9VEGttVqqT7UBh0BnC_x96p0uPXjYw37_E_4T754QKq1EbeCFI3FZiVJ_OD1oyxN6HdCgiyFrDtrcpfrA37j0aLlV1QUvq5-y5T1U0b7DO7KjNO7Ko2KNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBXMG5bsRlfhWkPPNcZIEV0GADZS3A-y5XtzS-Ko3JSByBhk2A72uSO5EShaFnetJbcrN8tv2kEaVQw53uhCqi3xn6kkVN96mfAqMZr7P0NJjU3DTYpMZnctnqp2_lJQKU9EcwMNCt6n2st_RO4Vq4FhTkIker2Have8YtlYiDwDMk-zgovh7rasKrgE2n20SlFtUiPbciz5ctQ-pIG3erKxwLD1t5lF82xbQwDHQvAA7sm4nw4Y1ihe1q6gN1rarFwt7sd2t0uYOflnmUHo4R9y6ZJD339fLiEhfBzTj42fTXo76LO2OhF7uVZ9FDelNhPEcyIxM9gdc5v6OR12kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiT7qvbK2AoEBiy5s19lzv8oPQlClEh5Hed9jUDJPUVpiApUasepQjB7ApOQS5xXwpBsctHmlAqxfdVL4YmEO2A7gqgKq5XZXU4g1TRtpETZncQnuMPIOmPfPR0iaRUdNAWlYXyrGvvTx2oLySLvZvWH8pmine9OHbA12ipQ36Rly2_yisrSVVqruL4nYOYET-pPLJJumk2_VJlS80F4kyU8ZNH30AbBBmbQBT5lESZ0Zu7tElUGt22MtglE02szAiddPmlMPZtbpcPNOaW2OqhwxBVO4fXzxDkGW2VtGoH2WZzkAdkN1Le5CvrbtBoXDOpeQC11iMLsIKDO0PAi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg5bIvE46ugUTYf-L6PY-p_EMYm-txWkz66CcmVgRpyKt3ELD-Q8XJdAiXfQ_gWrLoc8JBinAc7rdUG79B2d3BkIyEiTaWiTrqmKIeUgKxBZGbTvOvtnFbRF7u5G0yjfQwWBEsfQHo59f8K3bPYVLV5fv9375XI-5gTMt989jT-VGUOB1t0qoMGYWBUxSbFoN2b8xLUBKp3m9qqKGsXcCa_LgGczcR95aGFu58JyrQuuq5Ee6OA4lYjQzzTu8BV3M7Kau0edsLZoQ8f1b-9qFv00CpKmauTY52LeBgGLMklJMGjsVgAliixi0xOmR5NhjrFJGyPIA_8RGVc73T6bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0xifij7R2jxuY7ZKDBf-Y9YQ7WVW8hjEExEgeBVb1V-tq6Yljz3NqnNoGDIIbnXxRtg3H2yOK8BW9GcXeLTW4kFoy5prQUIqncA3n145DDPj-LSR6w7b1o-6bvAa2v_uloxDz3NhYHv6EKG60UBcG96kpF1-NZpjKuEisnDSGet7_XCV8moy5UkSUDiykl5OApLjlnlKWz7BsmKGAIhOnUZJeorAjVdqD6kdw9OmgKZLuYIzmdnadyu3x0exZYHs3QUXqhzFTMJMd7YD0-BdIHkIWVPjT2SLVdD8wyI7Ze14FfOHvFq6KlDAR847wt5xLl__WgylZfmJg1PI9JsIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=jv40BPmBkx1iQ4NyN5yRuS0KL6arQXb4ogP48lpoQRGDVgO9li3fOotVTZse5onqKgx1qFuEdP3zF2nz3ndzlnMD3Ds_Fp6p_5unWnAAC5tm2xHuu-Aituxf_Y9tP_LcFhgE9MVJlKPvcCL9Z_RKldY8wh0ZkYBCBMLaQOnaPIvRLfRcp2IB38QHvdGdzkhzCXmqNKtBuicl5Pq0aAFiZpB1Ah20ABA0M1XBi0TyEJdydjj7Gm_ElxJfuWXcIyzeKR9V42sGeJ1lnE-ciAEy60iozMIQQIf24FnHShz1FGxJ23oOskI3BSDf3UcEn-cQDvWRp9fuJrbOBcKP70uSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=jv40BPmBkx1iQ4NyN5yRuS0KL6arQXb4ogP48lpoQRGDVgO9li3fOotVTZse5onqKgx1qFuEdP3zF2nz3ndzlnMD3Ds_Fp6p_5unWnAAC5tm2xHuu-Aituxf_Y9tP_LcFhgE9MVJlKPvcCL9Z_RKldY8wh0ZkYBCBMLaQOnaPIvRLfRcp2IB38QHvdGdzkhzCXmqNKtBuicl5Pq0aAFiZpB1Ah20ABA0M1XBi0TyEJdydjj7Gm_ElxJfuWXcIyzeKR9V42sGeJ1lnE-ciAEy60iozMIQQIf24FnHShz1FGxJ23oOskI3BSDf3UcEn-cQDvWRp9fuJrbOBcKP70uSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1WSXU5HWWjgZM3tRqDxcqxF3ShyAgYjI34JZLQlA0zlZ_6PZw6Gy3rr9RIhLLelhP-RYmuLbKLfXnyyEaKzKA0ILBViEtRysntwlYsINV52psDKKyfEmvR5QCpUIdLEbDHv6YBut043HUM6M3G-eWDJJ_Nk6wOgehpYuXGL7YbhzTb6G92rRoo39iV9iljNelSNZhJIdfHUw7QG9yWYBBBCTCmQBxjCeI34rEt74GSTNvVe4JdXxcv3fARwn6_zP2czFOo6x4hyJNW6m9SGPcvxXFaxkJ1MxEIUFh1GqLwIGPioUy5PvH_cHlQG9u1mwi3zIFdAeFI_amExkLfwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec87v9hzWzVnpA-sfnXza0FiAsNMxx9xNcFIDIGD7J6MvluAQynMV1JCxgbDTTeLmb0Rm6yboE2CUfHPYE-gZT7slYaS7vgwYdn86Pql7KwIv-YLRlj7_H6DpruJAM4Fel_ztQKyM1CSkUryR-hBTr_GwbvP0BWV2TSEOS8nv1cyY0_XnuIzsDxbU-UXLXT2wnHfF2ngeo_kLvUdE32MEvC5qdGkG9hJK2QGLQ9CTuraDAFkTdcOn4uQAMEN7lbO26nElEmLHNwMCDkY2ojCjxHwA7g320zoBCsHUeHExse3ywb2SYlXAMou6fspVh7PQFHxe_xlLc9xMcF2Ar1K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehdSs_RiLtUH8d1dNf2rgGMttycgpV0UsbbH9iwVrtSyd01LHxLHdzw5gk4_5wFNQkcE6mZhrvQASqbCpm11rjZ5BkFr4vZxc5Ny3c22wPFZdD0jLP8HquXaIMhYGXNB7H3gGnTbGqGIViZ4_Xy_yKoILmuPRDG_yqZY1_4R5zqFHGSrbL0XPJ0BWWI8AjwToOBldvl9xBvT1iD_RPLnhvr0U8_-UZduGD2_MAnJNMkJ4CgroW02mIaRkf-tjkZ-CWWeOMQLMCESQGNjX5akoCzHMMkv4wLiaxvokLt1l7Yy4oIbKtZ7k2RXIFsSbtR1plHxxhKr0OQCLz8hThY6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz0dtKIu2aopK1kDZ4Iyqk84HKEa6_bQLu6xJZplTSbqmU1TS0syHOVsdlsKaOE257dfWzX3xwLS28EC-ZWWySh5bspZETSYo1lX42-2MZjNPm9Wu9jIkwlDgXTtPvvJgnmVHV56WjcUK_33qJ-GeykdFy7mNMjD4FE7u7sAAOA6XEyfgsGbbivODcNePHBjHIVFNATWy2S0y70HBa7b0QwfrV2tCemFP6IWVQNKtNelmY6oJBY12yXsgheRLSzKSjBmU42QZk7bGAQeYJDMmel0Xi-WxQ1NngXWv3s8UpEatzn-99Z3OcO0-EYtxdorsfKtQpn5T8BQSZelMun46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOmPJzEb_lW9jdd5fJcNbwWaW_ihttAb-lWOYTGsvJNaB7LK7RCDYUxInQlDLhX4YweJagBbfa_XtMEMvST79P7T3ubz0QsQuqBILkGV8HpoIRHp9OE4QCnEAI0E7W0hJHRdJi8Wm3zO24GVj3KGwbZLH0sBadraElDBm8muy_Ml7bbdTcwDXRUmXEzvNKjfW_jXFQ6lfH0BVz4CMx2wKu1LDFgiGniIks5zc8bTN5zEDtDjJbazG45QrFCZ9Pg-2qht-mYvp0owk3IZ582NoMRIF-YwRn1wJICeIS_lwaQPM_W0sCfvPEGWqWYbUNRwNobYHX_NnyssrGeIjC7YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
