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
<img src="https://cdn4.telesco.pe/file/JrcdLPVoSWmdR8xeAAa-jWDZeC4M_onXXPkasPvqhCmVWm9ztMGhXs5ip9cD6YArjg_4_cJWAD1IhY4xrK3LhuZvUzMcMiw4u8hkEIHpoLQudnSN6yEAweK8tTjJuv26PAjq9gW-0mLOS7H1FfngV-WW_0ut0Uv7QJnYBFSD6ONRjmycQl1u6Z4BYzUwFH39BqJjEG4DadAvio0hGXViaKajM_EXcS512POC2wr8ajK-fend86VqoI4ISgNVHDaAD1rVNhy8N7igAlCKeRdJLVM5GgurshbcH8JzjtBSudCM_YcMCVvhhz2-r_t0rH0Ip1zd_eC3khsbOqGIpWfFag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
<hr>

<div class="tg-post" id="msg-462871">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-F6s68SeYUJ7dcnu_0t7cu71QZ6ZJ8ZghPe_tfmFhCk9EDQ2aDD9_u13GXxqrdKBQBw2U6tPJJZjXBjF1H5e_hS6qt-Jc7hkfMbmAp8CxE4L_SVpJ5FkmbFmu2DDgoQrmD_CIUCJytUonNbgEXXO4NUiHR7nBgyC86UiOo8spGEC0mJIs8qle-6nM5TNab0bqQuOb8RPn3yeG1zCEAHoBQNCzaT7kCydyzMzdZSgqOd-8WP4xrNbAYvafsgMKuMMU4Xaaf0gxW6L0vKFVfBfOnobmJOUtypqTOPNX7kQ_X-k0LIG47pr7tnODnjJd2Ed57AFO42BS7IW_t8fAqeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: دروغ‌های وزیر خارجۀ آمریکا در رابطه با مداخلۀ ایران در موضوع یمن-عربستان، نمی‌تواند جای واقعیت‌ها را بگیرد
🔹
سخنگوی وزارت خارجه در واکنش به ادعای بی‌اساس وزیر خارجۀ آمریکا مبنی‌بر مداخلۀ ایران در موضوع یمن، نوشت: دروغ‌های مارکو روبیو نمی‌تواند جایگزین…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/462871" target="_blank">📅 22:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462870">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fINTfo0NnrUamRmDFovo2_SxIpussrjrhaTicJe3cIn8ULfkc5RQ4qg7Fh93lKBixCb_DCplZVzqLy9nrVW7-Z4bb7zsMCg8y7LbF68oXPqTTktSlCSlV-u8TmnErSkNjBHJkcq8kbbGSJ4hAmSyolqTBOKnrkTpxx77w7dy9BaHs7a6eDh0qTySlLYDidJuC-1FwRDW03K64HOVcxKSAro9nKaKgXNALPcRRIBB6woOimdSdk95w2sAQpcUt3nuPEPXaDzzrRfWpsYRdSEUtgoGvPILIt5I5u4MF1ir21uCb_5hnDoTSU_fE_jTQIQ5DyNjs_GCeH3a9Zv9fOc55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۱۳ قاچاقچی مواد مخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: در جریان ۳ عملیات مشترک فرااستانی ۳۷۱ کیلوگرم انواع مواد مهدر کشف، ۱۱ خودرو توقیف و ۱۳ قاچاقچی دستگیر شدند.
عکس: مصطفی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/462870" target="_blank">📅 22:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462869">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQAlVqkGbNcjZRSejkM1zFZfAPKP9UxfstNtMW7yPc_X_mREp029ra6uv6Rk267o2dx5GW6GUfOZVaj0Y1ssiPGi8QVH8_X9JkDDWUG-jMFA43WdkJnBYn8GV7RMwrkBS-dZVwFpCQBCmVBSPvRSkn4NVoRec2xentLbq1H0M1IXe3oyWOiY-A1nnjiCCvz90MtJ2RUBf3V7gkTXK-ufSljGFP5WKoWPTc47JkOIn2jTHYkFw3RLysOEX49FrX_kBqIQl3y852Hkms2sisgT8-FhF3ag-MKx1qbTlX_Z2xRs1ZJppI-ZOYm_g5vbHa8khzXI90kA1d0pAgk2RO1Dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین مهاجم خارجی استقلال برای بازگشت
🔹
داکنز نازون از طریق نماینده خود شرط کرده که ابتدا باید مبلغ ۶۰۰ هزار دلار را که بخش بزرگی از آن مربوط به پیش‌پرداخت فصل آینده‌ و قسمت دیگر طلب باقی‌مانده از سال گذشته است( طبق ادعای بازیکن) را دریافت کند و سپس در…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/462869" target="_blank">📅 22:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462868">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff2597e4b.mp4?token=bvApDFaiwc2lSnXXISz28ovXFc7Cf7MtokUCa4RMvOadTV2SD2RaOKEKqcJA4IXzWxeVLwB7YGdTjGZZjddWLyv7aMergD8806x-vMAS9JrGL5BSb15LNUetgrnWrxfcRVQaNpNMxkzMeC32V3WjbV3Z7VXSiEuajq0JY_ox0kYKlQFarwtlVChTCTvwsLjar8jODEalmBCuSy1r31oaBoiknyQAQPLj4d5rVKPC5TDlv6FaJjDUjeyNgTkLleKdOU_wIg4xhLVyD8SwbASXKvRx9Ei-gZemWoDkCGNmmf15EB7bPX5-4WJlnnSqAIKWCBrqs0HZXxURJkUiGeUogwh8j5YdmGr7wURAbhnAxgeFsibKjy-n9-xYe3wxXLfkrxDplQ_r0b6oUh0nYe4tFwNVRtW4qTlSrK_tgHOmC9TYlf_70s-hpZUOqt2PdHRONCxb7-owMrTxK3E2_yKPOwNDxL4H1EBT4321gKm10n-IwfFz6IFqW_op7aaKQJGfDhDmtFfY0d4sPyjk_wmiJBMsjWzBWApYUwOhVcaaYeZgOYQt0tibpUJ-7SacdYml95bjRlHrcFZxzTqig1s1QvkZR5LK-oy8r63V7Iz_wZwGoMdBhO3Gmp7mnHxL99NyMtgsDrTLHNWQLta9pODEFvfrEk-fQ_sWxO7VIJyjzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff2597e4b.mp4?token=bvApDFaiwc2lSnXXISz28ovXFc7Cf7MtokUCa4RMvOadTV2SD2RaOKEKqcJA4IXzWxeVLwB7YGdTjGZZjddWLyv7aMergD8806x-vMAS9JrGL5BSb15LNUetgrnWrxfcRVQaNpNMxkzMeC32V3WjbV3Z7VXSiEuajq0JY_ox0kYKlQFarwtlVChTCTvwsLjar8jODEalmBCuSy1r31oaBoiknyQAQPLj4d5rVKPC5TDlv6FaJjDUjeyNgTkLleKdOU_wIg4xhLVyD8SwbASXKvRx9Ei-gZemWoDkCGNmmf15EB7bPX5-4WJlnnSqAIKWCBrqs0HZXxURJkUiGeUogwh8j5YdmGr7wURAbhnAxgeFsibKjy-n9-xYe3wxXLfkrxDplQ_r0b6oUh0nYe4tFwNVRtW4qTlSrK_tgHOmC9TYlf_70s-hpZUOqt2PdHRONCxb7-owMrTxK3E2_yKPOwNDxL4H1EBT4321gKm10n-IwfFz6IFqW_op7aaKQJGfDhDmtFfY0d4sPyjk_wmiJBMsjWzBWApYUwOhVcaaYeZgOYQt0tibpUJ-7SacdYml95bjRlHrcFZxzTqig1s1QvkZR5LK-oy8r63V7Iz_wZwGoMdBhO3Gmp7mnHxL99NyMtgsDrTLHNWQLta9pODEFvfrEk-fQ_sWxO7VIJyjzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در شهرهای یمن به خیابان‌ها آمدند
🔹
میلیون‌ها یمنی در ده‌ها شهر این کشور به خصوص در میدان السبعین صنعاء به خیابان‌ها آمدند تا حمایت خود را از نیروهای مسلح یمن در برابر عربستان سعودی اعلام کنند.
🔹
شعار تجمعات امروز آن‌ها «برای حمایت از نیروهای مسلح، معادلهٔ محاصره در برابر محاصره و افشای دروغ حمله به مکه» اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/462868" target="_blank">📅 22:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462867">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptBzG7_XNzX-WUawdz--jvFXxNxxiBedUA2oBRLpO4FJ_vvVkUW1uKGoYBJgf1ln18A8TCv5w5nHBa0c9ETAAyhqg613igXscc9m3tTbDbu1DmCMbSb6jXZsQ9bnSMmDWA4z65QxizEUVA1haCIg6S1s6eJecMdGZf684QMBK8gIvu8nvIBLqxx1pWu1T6AGe5XjO8X-oi35JkN__I8Bci0HEMGiw8s-3wkF1iDyFolfJiwIECCyavuOfhX2orHMkIDPiR7gN64ZScBVR-Up7XaLS5s8t1YQi_d1NBlc0S1WPYRrifsFxh5hsXhRYpAhdSkjlARONvApAdbe1yGaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ حامی ترامپ به رکوردشکنی مخالفان جنگ در آمریکا اعتراف کرد
🔹
نظرسنجی فاکس‌نیوز امروز نشان داد که ۷۱٪ آمریکایی‌ها معتقدند که دولت ترامپ برنامه‌ای برای پایان‌دادن به جنگ علیه ایران ندارد.
🔹
علاوه بر این، ۶۰٪ آمریکایی‌ها می‌گویند که اقدام نظامی آمریکا علیه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/462867" target="_blank">📅 22:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462866">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
تو را به خدا وضعیت
شاهین‌های تحویل‌نشده
را دوباره پیگیری کنید. سه سال و خرده‌ای است که منتظر تحویل خودرو هستیم و هنوز خبری نیست. واقعاً این وضعیت قابل قبول نیست؛ مگر کسی نیست این
خودروسازها
را پاسخ‌گو کند؟
🔹
شهرداری اهواز
اعلام کرده بیش از ۳۰۰ نقطه از شهر با مشکل
جاری شدن فاضلاب در خیابان‌ها
مواجه است. با توجه به نزدیک شدن فصل بارندگی، ضروری است شهرداری و آبفا هرچه سریع‌تر برای رفع این مشکل و جلوگیری از تشدید وضعیت اقدام کنند.
🔹
خواهش می‌کنیم به مشکلات
شهرک ۲۰۰۰ واحدی مدائن در پاکدشت
رسیدگی کنید. متأسفانه هیچ‌کدام از مسئولان شهر پیگیر مشکلات و مسائل این شهرک نیستند و مردم با مشکلات مختلفی مواجه‌اند. این شهرک عملاً به یک
منطقه جداافتاده
تبدیل شده است.
🔹
خواهش می‌کنیم به وضعیت پرداخت
وام ودیعه مسکن در شهرستان بروجن
رسیدگی کنید. ما مستأجر هستیم و به این وام نیاز داریم اما
به هر بانکی مراجعه می‌کنیم می‌گویند اعتبار ندارند
و حتی اعلام می‌کنند چند سال است وام ودیعه مسکن پرداخت نکرده‌اند.
🔹
نهضت ملی مسکن
برای ما به یک کابوس تبدیل شده است. بیش از چهار سال است که منتظر هستیم و من برای تأمین آورده، حتی مجبور شدم چند قطعه سکه بفروشم تا بتوانم چهار مرحله ۴۰ میلیون تومانی را که چند سال قبل اعلام شده بود، تکمیل کنم. حالا بعد از گذشت این همه سال، برایم اظهارنامه آمده که
یا ۸۰۰ میلیون تومان واریز کن یا امتیازت لغو می‌شود
! از طرفی، سامانه قوه قضاییه هم دچار مشکل است و حتی امکان پاسخ‌دادن به اظهارنامه وجود ندارد. واقعاً سؤال ما این است که با این شرایط اقتصادی، یک متقاضی مسکن ملی چگونه می‌تواند یک‌باره ۸۰۰ میلیون تومان پرداخت کند؟ ما به امید خانه‌دار شدن وارد این طرح شدیم، اما حالا نه می‌توانیم پولمان را پس بگیریم و نه توان پرداخت مبالغ جدید را داریم.
🔹
با وجود اعلام
آموزش‌وپرورش
مبنی بر اینکه نباید بابت ثبت‌نام در مدارس دولتی وجهی از خانواده‌ها دریافت شود، در یکی از
مدارس شاهد شهرستان رفسنجان
به‌گونه‌ای مدارک موردنیاز و چک‌لیست تایپی به والدین داده می‌شود که هیچ اثری از مبلغ درخواستی در آن نیست و فقط حق بیمه ذکر شده است. اما در نهایت مبلغ قابل‌توجهی به‌صورت دستی اعلام می‌شود و حتی گفته می‌شود در صورت پرداخت نکردن،
اسامی دانش‌آموزان به‌دلیل عدم پرداخت در کلاس اعلام خواهد شد
. اگر دریافت این مبالغ قانونی است، چرا شفاف اعلام نمی‌شود؟ و اگر قانونی نیست چرا با متخلفان برخورد نمی‌شود؟ متأسفانه به نظر می‌رسد تا زمانی که خانواده‌ای شکایت نکند، این مبالغ از مردم دریافت می‌شود و حتی مشخص نیست نظارت و حسابرسی دقیقی بر نحوه هزینه‌کرد آن‌ها وجود دارد. از طرفی
خانواده‌ها نیز نگران‌اند که اگر شکایت کنند، فرزندشان سال آینده با بهانه‌های مختلف از مدرسه کنار گذاشته شود
.
🔹
واقعاً نمی‌دانیم آیا مسئولان این مطالب را می‌خوانند و به آن‌ها ترتیب اثر می‌دهند یا نه؛ ان‌شاءالله که این‌طور باشد. عید غدیر سال گذشته، ۲۴ خرداد بین خودروی لیفان و یک دستگاه وانت نیسان
تصادف
شد. با وجود اینکه مقصر حادثه ۱۰۰ درصد وانت نیسان تشخیص داده شده، هنوز بعد از گذشت یک سال و سه ماه نتوانسته‌ایم به حق خود برسیم.
قاضی به پرونده رسیدگی نمی‌کند و حکمی نیز صادر نشده است
. ۱۵ ماه است خودرو در پارکینگ متوقف مانده و ما مرتب برای پیگیری پرونده به دادگاه مراجعه می‌کنیم. در حالی که طبق نظر کارشناسی حتی یک درصد هم مقصر نبوده‌ایم. این چه عدالتی است؟ برای احقاق حق باید به کجا مراجعه کنیم؟
🔹
حدود دو ماه است
آب شهر طرقبه مشهد هر شب از ساعت ۱۰ شب تا ۶ صبح قطع می‌شود
. با وجود پیگیری‌های متعدد از آبفا و مسئولان منطقه، مشکل همچنان پابرجاست. مسئولان می‌گویند مشکل از برق و پمپاژ است اما نتیجه برای مردم فرقی ندارد.
🔹
آزادراه حرم تا حرم
در مسیر گرمسار تا قم و بالعکس،
دو بار عوارض دریافت می‌کند
اما
وضعیت آسفالت
بسیاری از قسمت‌ها
بسیار نامناسب است
و به خودروها آسیب می‌زند. از طرفی تردد خودروهای سنگین در لاین سبقت نیز باعث ایجاد مشکل برای سایر رانندگان شده است.
🔹
لطفاً پیگیر
وضعیت چاله‌های حدفاصل تقاطع روستای خین‌عرب و روستای فیریزی
، به سمت محل باسکول و تخلیه زباله‌های شهرداری باشید. خدا شاهد است وضعیت جاده به‌قدری نامناسب شده که برای جلوگیری از افتادن خودروها در چاله‌ها، باید در چند مرحله مسیر را تغییر لاین دهیم. این جاده کم‌عرض و آسفالت آن نیز فرسوده است و تردد در آن خطرناک شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/462866" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68556d2192.mp4?token=hwifWgPVHeI-LDbX9Q3TgfNEcQkC88zdjnxz2tGA95vXZIpa8USIM8vec2HQxBSEw_dmjik0ilIlZUoLsvksbe2HqsQ3K7K8OgV1qektB5F6igO7_FaUum5SCqLYHwyGdxiPazQltBvJVdOs4BDELBTtL3awNxvtCC5swXix0samz8Sh4kYi6okMeRZZSbdw2nQP0P0xH1Z2mfiqogSg_jkUqS2ZRjcWhtlWdHdXfQyIOqpu-KCBLjO9koZrVuUQOP99YJ4AoE1ie-u2gB5BrM6vVj-_TrLOKBiGRIRI7IpXCdEW-w_eqe9kMDRiJN1MstZvgaAEcqgheMD8VsOTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68556d2192.mp4?token=hwifWgPVHeI-LDbX9Q3TgfNEcQkC88zdjnxz2tGA95vXZIpa8USIM8vec2HQxBSEw_dmjik0ilIlZUoLsvksbe2HqsQ3K7K8OgV1qektB5F6igO7_FaUum5SCqLYHwyGdxiPazQltBvJVdOs4BDELBTtL3awNxvtCC5swXix0samz8Sh4kYi6okMeRZZSbdw2nQP0P0xH1Z2mfiqogSg_jkUqS2ZRjcWhtlWdHdXfQyIOqpu-KCBLjO9koZrVuUQOP99YJ4AoE1ie-u2gB5BrM6vVj-_TrLOKBiGRIRI7IpXCdEW-w_eqe9kMDRiJN1MstZvgaAEcqgheMD8VsOTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از تجمع ۲۰۲ نظام‌آبادی‌های تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/462865" target="_blank">📅 21:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ae86d509.mp4?token=nS0vmcaft8knDNjf_mJnNMyvVqoWcRvuFP_f9iR-MGu8JEkdqt53wH8St500VguqTcO4mXeYoGY6UXZBuECKcVx0o8bBv34iC4e8qVOTRzXuAHtcROlLuAqB-lAyLi0v9sQdMEXQyeHjBv1Xhdu__22u8j6i3yiqOO3sghvJIGvlSyD-Vey9Sb10fj9iqYPInk5LZdZleQhT93s8JQ9N8QjoZXYchHZeers1e7uvVETf7ccqGNvsYWOnZqG8CYq4WwMaM8R_dNkHfroFFuZpViDxs-juu1Ydh6uy8ekNwGlE2qS0MELAUfYngoUEIDDT5jsfeOmeHHH65iJy7FvHPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ae86d509.mp4?token=nS0vmcaft8knDNjf_mJnNMyvVqoWcRvuFP_f9iR-MGu8JEkdqt53wH8St500VguqTcO4mXeYoGY6UXZBuECKcVx0o8bBv34iC4e8qVOTRzXuAHtcROlLuAqB-lAyLi0v9sQdMEXQyeHjBv1Xhdu__22u8j6i3yiqOO3sghvJIGvlSyD-Vey9Sb10fj9iqYPInk5LZdZleQhT93s8JQ9N8QjoZXYchHZeers1e7uvVETf7ccqGNvsYWOnZqG8CYq4WwMaM8R_dNkHfroFFuZpViDxs-juu1Ydh6uy8ekNwGlE2qS0MELAUfYngoUEIDDT5jsfeOmeHHH65iJy7FvHPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از قدرت‌نمایی امروز جان‌فدایان ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/462864" target="_blank">📅 21:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9kFIEGsOW9lEEt2umJ8wKBD5YVuUtD1tnDdg_ZakeN6BEYB1zNBW6ppDCCJUufXl7OQkLS7XOwTDdoFY9BFVi6ZpMxJo8DUWeKM_3L91_i3FAB6Ys6BWc9F4x6LgmXQt14rTEkraP0nUiHJ16GjglP2f_OlWS9n1VUR1gCv7_gkAU-bj9fBUgOvtp_YonQugOKHUuSM-SxL1EuadUmUy2kCMPLoVjIzf3hkL3miXN4pRBjL4QtRHON10xhDSY1oYH4qFQMY5CmyXHB5VfObwFa-Z-aF2beAcK8YpIXWhmYuzJpofWeurg_KWNGeSgTym00MCRwI95L2gMkcu1sg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال دست‌یافتن چین به قطعات حساس F-35
🔹
نشریهٔ پولیتیکو: این تابستان، قطعات حساس هواپیمای جنگندهٔ F-35 به‌طور غیرمنتظره‌ای به هنگ‌کنگ منتقل شدند؛ درحالی‌که قرار بود از استرالیا به ایالات متحده برای تعمیرات ارسال شوند.
🔹
این موضوع باعث ایجاد تحقیقاتی در کنگره شد؛ زیرا نگرانی‌هایی وجود داشت که ممکن است فناوری‌های طبقه‌بندی‌شده در اختیار چین قرار گرفته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/462863" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbijRk9zwd_XSgBHK12lqQ9Lq5etVN1HjMCa4uh-0yhnlnLUnqhsseBzokdqTZ9HXTg7lJgSLYA9zryhU1ofvTGF4XldRHJgQMlPNTuQCwwLoCpKW6x3gM6FYg6pqVtuJPx7M7OgH63ZjRWO7OeGVgMzomUGyoRKSIz4Hh1Xqe1K5HyFlS02TBVlws9tqA54jF9g9CZj6_R03Yce4HFlVMQyHJYXpwmBQsLGI-8nmfIhBRRal3RHtLZE6d06ZQ2JiGWelRfltI3-liGgfw1GUPR6Ja3mKkQPfQDLfoN76yNiB4D7rdbsZWhgatkEYL1VZylRASve44y6JaDO_DycKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ قالیباف به ژنرال دن کین: آنچه روزی برایتان کابوسی وحشتناک بود، الان به یک روزمرگی تبدیل شده است
🔹
رئیس ستاد مشترک نیروهای مسلح ایالات متحده آمریکا پیش از این در کنفرانس نیروی هوا و فضا و سایبری ارتش آمریکا گفته بود: از این به بعد باید این فرض را مبنا قرار دهیم که یگان‌ها و آرایش‌های نظامی ما توسط سامانه‌های خودمختار شکار خواهند شد، در سراسر طیف فرکانسی با اخلال مواجه خواهند شد و به‌صورت لحظه‌ای ردیابی خواهند شد.
🔹
قالیباف در پاسخ به این مقام آمریکایی نوشت: دورانی که در آن F-35ها و F-15های شما شکار می‌شوند و شما مجبورید گزارش دهید که فقط آسیب دیده‌اند، همین حالا هم آغاز شده است. چیزی که زمانی صرفاً یک کابوس وحشتناک بود، اکنون به واقعیت روزمره تبدیل شده است. با آن کنار بیایید.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/462862" target="_blank">📅 21:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIZ_Ty3Z3qp-MEfVTqT7IKis1QLj6srbeQgWC78SDOQ7fBBiCFaPRUZGOAiVSVAf-51pa3nP1S6xC1o4t_9jPUpbxvY18OreY2Q_0BnrVftJAxsCpU8iFGKQKRrg2R_4Jt-yMEu_qOjQIPIWEeN-ujiRpRDw76QR8RtrvE9yw8ma_GrRqLfPeVQswUnl2SgKDZtsPdusU9BH7ofQptdr_EuXmnQWn4itOc8OPnEcQEsp1ALcwdMpU5kE8wwU0ZBgutXoZSyzgnclmafMm_YMFz-Yw-qYOHheGyOG9VTpA8DhYmYxv92Ra2BSZeVGKnw7fOWSHY_WncFZ0Q3sEh4uHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳ ریشتر در عمق ۱۰ کیلومتری، دره‌شهر ایلام را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/462861" target="_blank">📅 21:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAxXPZjm2uZ9OzWsChZ8qhsLa5b9ty2d2cSJgpgyNv9IDUJrJ5j5YLGdTsbvzMc2UkpseKIexcisJ0nQI_cprN1zEDTPQFSC7-RTYzHL6FZocfzN4MmfD47QWYPVNmDOJl0NexpSgP9Z9UbsWErgRLSFcpRh4ZrHiXncwS0spnX09i8PlHkex0J8CJOwyDjAkb_Zuji5111t-d4W50aOsjXWwWIv_8RSQvHlwUD9qwc5TRWQ6CmX3sMy4EhlEA-6i18dHlFLD0SruS2DtC9yojTvbjYO5diqvU8o1_3zS5dwb_SI0Fg-wdTrIcE5rxsN3xng-GT-p0I9Ac-7BZi6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یادداشت کمتردیده‌شدهٔ رهبر شهید خطاب به جان
‌
بازان حزب‌الله در جنایت پیجری
🔹
عزیزان من! از امتحان الهی سربلند بیرون آمدید. صبر و استقامت شما یکی از برترین جهادهاست. شفا و عافیت و عاقبت‌بخیری شما را از خداوند متعال مسألت میکنم.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/462860" target="_blank">📅 20:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHis2so65Wi0_xs6Sqn0G58DaPTjrfwJ2m1LBT1AOSXT3tHeNdLl0SdfjvvGdahuGqEvx0W8MZMlhyA91RmnjX-xFLvvKVfgGK8cvnyPuCl9OV1f4Hzyv4OixAGNflLSz4NBE8ojx_YvqdqcGWSKo7oedxUI7PXlxhsHkbg29qHmEtRbTucp2vrDGjMNtd_yKcyiITBC5ZerySzlIiykpAHRaaYHHDgGzJD9_FWzsRHxMyWjl5yE1QpyESW0EhRWfKxEByV1HMYg7gIp3MDWznOqbHxBuA0SUdwqjt4YslV5DXL8ADtDG33C448dZHhUHi-HIoageVOYyRSKpbLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPUAGzqlmqfIFIKNvlVcG7vQpnJx9QbSzlbj6jgO5h4yWrD-k3krah8dGspEhbJE_h8X_bXTEPEFHjWgjJCo__OTbbkrplLRlcsQP-SB3OKts38-5InTQKExrOUTVaGSCZNYaBkzO2EBj8tIfVpPnnBESUmAN8YLoO-NigzxNkuYpqPHTLHx1GHr-GUDr4GttHNaSScl_ZVv3bHzc06EI_CRHHIkPucj6I7vXqP9AUqJGdKQldDZVYMr40CR2hTcosifuiS0y-tHuojz8smJGCXeucdPDR9IaNTcescMG2eP2SbFQF4A5kXB1FmVDZ6s7uj7F86gnLD6kq8PxTZSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hq-gL-yuhD3Ci3SeFiBtZxYXovQAciw6CG3jurHSboV1si9bpiazoCzFvY_rKJiRrZYO5Lzbpcf8mmNuKohsOSCvXy7NG1QgjRrTpx-d-us8oC-072NTusmai-ocn6hHjK1omEiqditWmSo9IYJVM65t7d_A7TXZkfIk7jBYj18UvWCgEq-RSvjVYDtO3M1f37xFqjQ2id8RSuKIrHZhHJQVbJdNu-0FXScjEMuyMdff1SbxtmgVWI4FhJtqPLw6QDDnO09v8L2VNnbMs3YRm622tUXiJsQ7Hj5k2KhHhpFYjafKIPChwGdUckDeX6ikZ6hMfRXM7zRaqDpztEUPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usE6FxU7CKppM-VD6lJyO_LBEWtYl6v9Z6U0l6nsutT6NFSaiCHiePY1NYenAuLdCpjeIRsGQdHLMipW2w7v2k0dnGU4B8SXKBHZ9Y7N8Sft95Cc7nrBLOO9qiPMbRQPjbYWAhNF7OA0jJcL7HHC6kM0sJ7FJPevNw8ECFulaqPwtYXMtKfM6UW-oel1cAyZCenuRhwzwSPRKkRTa6UtSfY8Jia42xbfwqCUgH990pkdRA5_-Wx-mIArlLFV06vE75jLsRBRufbPQtDE7b4A_IaQ_ZIjAGjd4XTmSaxFzJhmmB8vaQyZOC2GN-QFo8aVGOSA7LYCnB-CgNUkVz1r8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHAu7YdT6FYmua_9eCFldd1bgWNFXAS0X04NixJ5hVmzQvO5UMW5uoVvOCWcVCPchQOWOZUsOVY3TqPk4iFFo2EqLVOjYGIOMNFLTheTWMgBAU0xQMQdNUSAf2bNtrU_YoxyBK5NWnn7KNsN_SG8xVwjhLwWQMxme9UJ7ihNWJLLWQON3UorkPZYg1z6CaTmUCQjbDSH2zfq2m4oH2MBorRVW0kMRh8c1FZlyyMNjWqAfzF_cukbqL-vLt2DK7r_4MUqcMw_Gs5or-k98rgIUEYZR7982-NMUoacs0VrQFpRJn1_f48fy24fHUCsAHlRYljhYsX8D1bx4xZdc3lbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRgmqZ7nXf3OGQqE0zAA6mZwcQ5SZNmjJGxKOOlDdGxoVq8dm2iHkEqBZYHaBSWdaAtrfxixCBB-BqZhHr-oqbKp53ezVT_LYomqYs0c21grLBwHPRIwMe-l3YF4rasRiqbRBVrT9erWPzKGh_wTAST6IibGwHpaJooyHzPyzbGKFzWaO3nu5OKHZ_8OgxkHgaaqbqFG-vv1KhWNkesfIoGoJ862r2VYQHfBsoWQPMb6WsQlNGn4UPb_R28eR0mbSeCW_zwbtTOg9gNY9N6OanETB_DR9s1_3urvXXCt_PMd3DLWrGWpGinrRG2r0h_ov_qp4b_Xg9XwOw-LuQ6hWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dltQg6O6aKhAem9iRR1izvi_ZSNkOfm2lruZ5YxCQm9tb0YknOM9R3Qi_-35YsF9W5-N0qaeKEJTvMv6wU9wno18LY8JzzHqkSnonbZtOPkE0-GVkw51j60_couBZD1HDCexycm61o5n6DrdX7gYuKBZ7YwjdlrmTHL6vj_FlzEB8nC1Gg9fGtePANzkRegEp19EDC0WfBtNhMCtYylErSJ8JQfD7N16OYJwy-FZrD8-1DasUqcVxM4T51AkA1hXvf2i5eaRlerx0nThG2aoIJRVZSxjtMPuFnJAoaZgmFdN1DzyZMQ0KsANLeI2gdw9yzP9OTGJokh63Y4D3eLoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flnji5zg7S8P0oZKWUy2RWyAwgXjUvDiKvBrOgTsDxfV1TYTFJNRhWSHCC8iuAU4FZlhf-6grneNPrG92jIgWYHkkxjEaQpTZApCps_ifGp63wYJXsidwc6WnAbwCBgQfb3IFS9D2br-u0cBgx5LkBE-7Oq_dTDwdDbv1iLqEPir0vRQhdbEiY443eGsGZnbSOxo1eTKTv1uGMirjFK6DpNFN04cMAlN2lE1BsXCLh7rX26kCjeG7L_mfjIS656reoyK5eJEl-WXIUNPORX7qYGQ9XEWFaY2OesRPXMoeNo3oXpSyMGuwRiUKpMMZ2rzrCv6DlgHlNN3u3nGmeA4eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مدافعان خاک پاک وطن امروز حضور خود را به رخ  دشمن کشیدند
عکس:
امیرعلی مصطفی‌لو
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/462852" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZ-l7sJMxQ3SG6z6vJzVgks-nBH_sDmHxLwsHner3ZR20bITlbooTYg5c7Vo9aCwZoeBNSLnpl4WYtb-3gQrzN6Mi4vIRf6s0IqCLewf2URQq7frsho9RnPaMbmq5xMMCsjWCWk72WCDgiyj_ejIDpfVK6yZ_HTp-cqGOipspDGU8Mf8X97Wnq5DR10GsjUBPgaVgJP31RBUPi9amcH6EPxeOwy9l6DgSAIgYiOS9k48ZOTfdRkzjjPtNqkC4ZqQlrKKI1KRsCrCzpDnPGVqobZ3poLlMKwdemPRWOX721_w8e40ucu0LZq8HyDpnzhuj7cQJWd6cewbDaXyX-ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارین پالیسی: آمریکا تقریباً با هر معیاری درحال شکست در جنگ است
🔹
جنگ با ایران در مجموع برای واشنگتن «یک فاجعهٔ استراتژیک» بوده است. این درگیری آسیب‌پذیری‌های جدی ارتش آمریکا را آشکار نموده، نیروهایش را بیش‌از‌حد پراکنده کرده، تاکنون میلیاردها دلار برای آمریکا هزینه داشته و بحران انرژی جهانی ایجاد کرده است.
🔹
با وجود همهٔ این هزینه‌ها، ایالات متحده دستاورد بسیار اندکی در ایران داشته و در برخی موارد، اوضاع آمریکا در برابر ایران بدتر شده است.
🔹
تقریباً در هر معیاری، از توانایی ایران برای اعمال قدرت در منطقه گرفته تا توانمندی‌های نظامی‌اش، قدرتش و وضعیت برنامهٔ هسته‌ای‌اش، ایالات متحده درحال شکست‌خوردن در جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/462851" target="_blank">📅 20:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bde5e4d3.mp4?token=Z9F0reEuhCxFUXxr9MfSwFqIsBNp8GHfXEkC_hh46SxM8JuFr6RR7lVH_jrtPhtJ4AlZlYJsuiaHFOaLeGim0kmfJxxw_VxNoJ6YWzP42XJ5m6qROOtNHbHDusEdmP5CEyfNq6vQZ7tECwANyk2mvyxFUoljHYXhIyRGHmVrTrdsUHmjLEBkR04cxQBusEK2-8Bls6ghF4QmlD6AjS5-HJG_LheCJNvKy-XaOKr8xgRqYvaSZKThzta4a9F4RUwc7gdQPExsXW6YriHb8Asx0ZcQSYSpkz_AH212lNkOVtKtX0LvhOwPt5Lhi75Z9r1PThyRNYgEwz-yZiwF1IXuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bde5e4d3.mp4?token=Z9F0reEuhCxFUXxr9MfSwFqIsBNp8GHfXEkC_hh46SxM8JuFr6RR7lVH_jrtPhtJ4AlZlYJsuiaHFOaLeGim0kmfJxxw_VxNoJ6YWzP42XJ5m6qROOtNHbHDusEdmP5CEyfNq6vQZ7tECwANyk2mvyxFUoljHYXhIyRGHmVrTrdsUHmjLEBkR04cxQBusEK2-8Bls6ghF4QmlD6AjS5-HJG_LheCJNvKy-XaOKr8xgRqYvaSZKThzta4a9F4RUwc7gdQPExsXW6YriHb8Asx0ZcQSYSpkz_AH212lNkOVtKtX0LvhOwPt5Lhi75Z9r1PThyRNYgEwz-yZiwF1IXuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سلطنت‌طلب‌ها به رژهٔ جان
‌
فدایان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/462850" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY-5j62avl8hgSP-RvOwwnHPWeP_9AuHXm7Nz-OWSqQ2pLmLBhJyMVo81gnkIwOIvRF8VpmRxGqhvCANQ9cHOHSjXeYJdMXqbodIackKgH62yV3RCkdR0i2bd4Og00oTckVxB5kUGAqgtXLyxr3aMNh17kmWy26BSbKo3vmguDwSCLWqnKa1X2RBITCR6J5Oo_ARdJjrxdYk5uIPkFO9r36JXfouW8lzonGPRq3bLp8f4vGSwMmB5apXnIETN4XLAHnd9n5_7d0nZa1jaOv3wSXwT5b6aFI1xkdr1Wnv2ApMhPv2YhFvqRVVR6ZoDfXEAT5R9vJTPOtvoRcM2zML8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: توطئهٔ داعش‌گونهٔ دشمن سعودی ناکام ماند
🔹
یحیی سریع: تلاش‌های جنایتکارانه‌ای که دشمن سعودی در صنعاء به‌شکل داعش‌گونه انجام داد، ناکام ماند؛ این اقدام بی‌پاسخ نخواهد ماند.
🔸
هنوز مشخص نیست که منظور یحیی سریع از طرح داعشی عربستان سعودی در صنعاء چیست؛ هرچند برخی کاربران عربی از خنثی‌سازی یک عامل انتحاری در تجمع امروز میدان السبعین در صنعاء خبر می‌دهند که این موضوع هنوز هیچ قطعیتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462849" target="_blank">📅 19:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47762d3d6c.mp4?token=nd8a2UcJ9oXGbiMAY3XJYqFvbL_7DAZpIP5-tX5W8S5vo7uJ1DMZTZuaN_S1qjdh2viAM2893VhZbTy76h3Rii03ieoXvaGi_2Jvg2NybC17a52yC87xR_KB-j0A60mSOnv07S1PzCyrBkiYoj3Al60PCMLhr1o5QZZDIZDfy5XXq0eWiM85Z_bxB4ch_TEDpgg-UtOKAGRPhYpGtv0iYCwOqiOity-2fMyZNLLRGMpFRkJvL_vPLHvxThKdAuzSYayu5e4hykHIVlwLJ_IXIaKK310Vfcchyqwg8HzGiscaeAEeu3Zl5fhvTgs09g4Z-4L2-aXfbC7xp1hCFuL9yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47762d3d6c.mp4?token=nd8a2UcJ9oXGbiMAY3XJYqFvbL_7DAZpIP5-tX5W8S5vo7uJ1DMZTZuaN_S1qjdh2viAM2893VhZbTy76h3Rii03ieoXvaGi_2Jvg2NybC17a52yC87xR_KB-j0A60mSOnv07S1PzCyrBkiYoj3Al60PCMLhr1o5QZZDIZDfy5XXq0eWiM85Z_bxB4ch_TEDpgg-UtOKAGRPhYpGtv0iYCwOqiOity-2fMyZNLLRGMpFRkJvL_vPLHvxThKdAuzSYayu5e4hykHIVlwLJ_IXIaKK310Vfcchyqwg8HzGiscaeAEeu3Zl5fhvTgs09g4Z-4L2-aXfbC7xp1hCFuL9yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زوج‌های جان‌فدا دست به ماشه شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/462848" target="_blank">📅 19:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCUhiqQf49KZXooKT4ps5eBXVLDgV5RVRzWgdgeOnfiwAHvZ2yAyT1oS-JrG0qYejMtFCMO9D9Z0abj6TY4kcH_K3ghLY_K98PL-kEj6aupB5NJ5nnmnDQGGKZfLtlgrYr3UHYWgszU0bRW3R0PYRu7WsdRoSLJ8WTkSyfTixE_hvl6-uXI2ri8f1SU89a4Ech9uo5cTxq62PVDBZp0nIJzB8miM24QINhdYl9AQ0bk1WZzNKLBaveW7yvEcsAy41EfIOp6A0DcYWWe6ni8GejVsiKPNs3WkF8x060aOubSH1uCUMYJIkFtuEuwCp0s0tC543g4ils_xaXc2awWJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dImCDVsJu2x53te63-DoGHH6En-mAmMKHoXxUWziXIlJMdISv1WDHpO1YcM_PazWCixugzRUJP5pLRA2alhZeXF6RRV0YIVvmov9UeO-uUzb-Afy74_BCqfltAaIHxM81ZO6u6DhEqYIv67mSY7kym5xPNueD4f70yDR4HVLuMqJUOe1_z6NxsWzK7Wu7QWleTHl_Xi3fiWGMDJsNfjMqK_1KZMERxEj2AjsKcj_lwTl1y9mMRXOd2N2IhR2te6TRzqjkZzkQUQWuHQTu1kJZoUdzBybs7PNMyZREPGO4vGkdlZ3XANNGZi-fru5GfUdYYrzy2HUDjvvzpV6jk9T-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9R-WX6AOdO3T-cU3gY7X-ApV-at7Au11hGgybG2AnXA3UNt-3x4sRrIR7277Q17_ekp7q-ISwHOavb-vI1ewgDeZWKipuNYEfK52wK6oLD6En46924cXCvWxQ_gY2iA7ZPBZ5vc0MtCWIsvgRaCOmDbADX3tU3p7JXdtEOPyjOQTYy6Te6_77z36oBlF3ouRbOTtZA7AESOSWsuPNTco9666GmQQTz9389Eo9fLLV1iva8KSbutaUyBd39kHA2LJpB5FrtTgi_EOpMsbwjWn-VnAOzo9-Ipt-wdP1MK26OQswQHACfdvJnqPuPlxPRwqMZ7njRULLM32SG_A7Usog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5QV3ZksAMC6MMii2xti3K_vHF55MT9owzOnxo1D03FEPfYoJy0Y1d7YlEQ0wuRQwL9f4_IfzweiOdlaBQN4hMCFDKIwbcD84hcNb2urcXmsfuoSpavf60rE8BikC4b2Ynbe18KgwRhVu7OmZbpfcHlLs8nGO9PWMDp9VZHwxNeUtmYacOpUpEkaBzP8WVL6gkgjKVEInIGccHgGqcCUaPlm51AKkEpWWLCUQ-x8j27DF_tB93klWd8PDkXAPh4Ap5ILYmp2qHFqLAYoVlijbJmlsynUV5p_oyIxj4k9xDLiSWk5cp35PD97GYPwLe0YDQeAeHKMQ3nZy6LiQWLmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHV5eJIR6npPZ2rwdI7lPSfHe2dHhEMEDu-hlpA8-dMqDxLf5rYOdpJiPPIQbrp62uu2fD4aIeCspIDP_3Lr9AmPqfxbpGnbaFvE_EBF33hHKvbVFVknN2KZdmezRNWQCX5JuHp1CIjF-HmHrjcWbH-QSbvhKzAv6RCxH-O6w6nctyqsPtzTPj6PTRzh9zxqhr4tljoZIGEz_-c8cbdyx1D0nzVt-Y57smtmvDkc9b6CHFoGPSHsjIyNOEy5ChtpPxiRx6i9FnwyuPhUPYuvE0MuZceRLpVEEQye8N64MmObLmscuSsESRcJ3CpFU5B77JqwkHZzdQg0S2xoMX1gGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBcYbyRvh1ox7oK1V_4L0VZWZ3gPCL-rZ1TE0xnyMb7NhnnJZxygvU3WiGyHHeDXdEjsQIx_TUxWLlSQr6QaysfKfRXdnH_TdJ-M_JNsczHPs2ylAtp7uPykCeDGedYrCyQDCWdxDT2R8_e7w03LeoKM_Y_BZs5xCI-sBxMNufp_xV1UokV9uyz0CYXjoIXPt5I8VsgUuWwN3D-e521jac8Xn9xwzIxB0h88NnfxKMXwOn_1IMEjWdeT3m5LbxV9Nnmwwc5Hy3zW9NeDUJF1hxJwNmOASewYZUDdXB-ov_bMKas5KgsmAr_NU_izXOerZvCHRd00KtGf0Cp2nhUxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YU8AHZKTdf1hnI-FqVdQGYVhRqv1rWtVTwGzEXf46lVAiQgUMI47ABvEYW8U1J4lguYpskxXtWWLxuSs_rMuY2umL-Jui85xzYvvg_JSlpCkGpHhoSJxQE_JzfzNZOaxRG3nPe0DPqugthp1VEJseDH9_18dtouGK_nb9WdzIeybpf6JqrW1UYY0JdvxgbfWi-_rNI-bC8wd_0r4kTIvTkcqEG9eTRa24Fzh77_E2QZZz_2eRDHC7BCPXI9kkqzxdtRZmF4Fwgdmw24aruklD1LDPuhRSJOhAmbsdD4l1hhrnzNVXmPsVjV7geE9n9vXlC0HPLlOizFoY4z9TFPC8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دارت‌بازها در جام وحدت به‌خط شدند
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/462841" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
چرا پایگاه‌های آمریکا هدف قرار می‌گیرند؟
🔹
قاسم، کارشناس عرب: علت اصلی هدف قرار دادن پایگاه‌های منطقه‌ای آمریکا این است که چتر حمایتی واقعی اسرائیل، حضور نظامی ایالات متحده است؛ اخراج آمریکا یعنی سقوط خودبه‌خودی و کامل اسرائیل.
🔹
وقتی کاخ سفید مدعی است امارات و بحرین در رهگیری موشک‌های ایرانی و بمباران علیه ایران مشارکت دارند، انتظار دارید ایران دست‌روی‌دست بگذارد؟
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/462840" target="_blank">📅 19:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462839">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNFUpdqKKQB8odRvdNRuEZH2sfgrmwW5JWxrMpw2WjC5skX3LNmwNzdRzTehZ5NilpI39RWZftx3XbEodI-Q106Sm6r6y5b9znDFYZ7MquFoRxztYZVBKdRon-2-i-nECrjdW4cLRj9YjVrDHF-uikSfQoMETzdgZrS7jCu0Nm5ignMaQoK3Hds82QLOG0tLw-HDes5jl5D68UlxnWQjKP_Zp-TnhlRyRWUUf5oN9a4ofWaEn0pXXBXad41UCr6VoE9iYe64JoZqnGycJfySX9kBrydBbRFqFHi7lkgjYPhrJWJKVoFanEe5kRNx6MWbDxahwZ70Dm1Ylv8fKLgNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ حامی ترامپ به رکوردشکنی مخالفان جنگ در آمریکا اعتراف کرد
🔹
نظرسنجی فاکس‌نیوز امروز نشان داد که ۷۱٪ آمریکایی‌ها معتقدند که دولت ترامپ برنامه‌ای برای پایان‌دادن به جنگ علیه ایران ندارد.
🔹
علاوه بر این، ۶۰٪ آمریکایی‌ها می‌گویند که اقدام نظامی آمریکا علیه ایران تصمیم اشتباهی بوده و ۴۷٪ از رأی‌دهندگان می‌گویند که این درگیری در بلندمدت آمریکا را ناامن‌تر خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462839" target="_blank">📅 18:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab535862.mp4?token=kNtwsVlklyZLuRYF0MwzopnlpG2hSLDw_nB8Tgi4YjKrL9qBsfe9niccINT_zBDSqW5txZvlnrS2ke7cBbA-0M-qayRsrnWK9lhHDX0P4hGzhInotOg06Vcl0cnv4GNTMpSr5VSpdzOZhOrd0H1Vzy6DhPh4rhCmmEXo5_u5dRiEW8IBQVsAq3iWBTkrsZlRiwpV-G2fGfnPvLsiD18rzSdzMQP9ZiFB305RChgQpa0O4eUvbUH5pNeTG2GASa8qimZwgxbpBCttzqluHy4ZOE4YZdsXvpgDBGQjLcu5KQgUGpzBjDQ-65dZIiL267sUzcUhuoy4U3p4VbNxebsbCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab535862.mp4?token=kNtwsVlklyZLuRYF0MwzopnlpG2hSLDw_nB8Tgi4YjKrL9qBsfe9niccINT_zBDSqW5txZvlnrS2ke7cBbA-0M-qayRsrnWK9lhHDX0P4hGzhInotOg06Vcl0cnv4GNTMpSr5VSpdzOZhOrd0H1Vzy6DhPh4rhCmmEXo5_u5dRiEW8IBQVsAq3iWBTkrsZlRiwpV-G2fGfnPvLsiD18rzSdzMQP9ZiFB305RChgQpa0O4eUvbUH5pNeTG2GASa8qimZwgxbpBCttzqluHy4ZOE4YZdsXvpgDBGQjLcu5KQgUGpzBjDQ-65dZIiL267sUzcUhuoy4U3p4VbNxebsbCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رزمایش ۳۱۳ هزار نفری جان‌فدا با حضور رئیس‌جمهور  عکس: دانیال همتی @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462838" target="_blank">📅 18:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4a67f557.mp4?token=jCMIBsxCwigyaGFAyGYry_RKSKo2_nALSExORMjpynmGrpApWgi6KwtuS0NNqVU_nijRzLQpE-wil1fiwM0QihZ0wTCUDsWO3YoSeKXUc53AUqztFzlHZ1Ihce6JXLS2LJtguWBONewcnbmfW_GroeGoUifSDJBfe10QF-7eSGUk9sLwQzfySPDZmcINkhYFwvz0GpTp5nViRBJxNCrk_KNETWYt6j5SIsueCretVwKtKuP5-LcGMQI2UG2rA5j3rSM2KMCnTOau_9er2BUC-KrO7tHMepdIW6Hy48uWsSUszk05SYJLcwoGr9_fFRte2xGF0t4qnkSOPsA4Ei6TSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4a67f557.mp4?token=jCMIBsxCwigyaGFAyGYry_RKSKo2_nALSExORMjpynmGrpApWgi6KwtuS0NNqVU_nijRzLQpE-wil1fiwM0QihZ0wTCUDsWO3YoSeKXUc53AUqztFzlHZ1Ihce6JXLS2LJtguWBONewcnbmfW_GroeGoUifSDJBfe10QF-7eSGUk9sLwQzfySPDZmcINkhYFwvz0GpTp5nViRBJxNCrk_KNETWYt6j5SIsueCretVwKtKuP5-LcGMQI2UG2rA5j3rSM2KMCnTOau_9er2BUC-KrO7tHMepdIW6Hy48uWsSUszk05SYJLcwoGr9_fFRte2xGF0t4qnkSOPsA4Ei6TSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی سپاه: برای مقابله با هرگونه اشتباه محاسباتی دشمن ۱۰۰ درصد آماده‌ایم و با قدرت پاسخ خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462837" target="_blank">📅 18:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzaBWvT-xOaeZ2CzQ28EWNBnJs0dvUITHHU0_cH2H_9ncYtS9lk7ufMTx3WbUW0lOHYC3LP-ZV4k9FYlH2hqBz5JWdiuQSDbSYemVxQVnt8eOD5MoLZvdH-719DXU5kqmucGaCV7FY032koBfmm9KPQ-s11wJy-dQP_Womny636mbzmgfVu0Q39gHL2BJURiTpf_ZQVmSAUzBggoPeEqWWpW4ZuxQ-qwWf2_5nYtlg2B-04Iy2HHPiOA9_xDMYLrvF1sdRlVk2T2Jcjj3Wsw3vTsq7Ceqz32w3mu6QfiUM0XBuoSXt82vtxo0wHOlCA1cIAiqn6yYmGxRurZVH0bPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بسکتبال با شکست مقابل کره‌جنوبی به رده‌بندی مسابقات آسیایی رفت.
🏀
ایران ۵۱ - ۷۷ کره‌جنوبی @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462836" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnDQuSNS3TnzT1HUfOziBNW5PPYuAvU2d2JJObnRGt937jPBO_S6Vj9X4UV7xW3wmFoGQaNjLqGF7fFr-p31stM-Jk8-m6Jm6iw3Nb4T5wjKV11EEiLoI-vVdWXOTnou1B1RSgwmGota320rn-bgn1OTFvKRrRcyhr3y71onHWPvAFHNNIjGekUPL81OHLzNF2oYYbws4PpfbhPBzIkwdR2ZWl_GSJWM_lUeiUrxzsuxIlcqhgaAZdT9c3uJ3RjbiD5EIOLepQMwKTrgY3VNOrSmraOhjTso_7XnoLO5dz0Hww6hlnjw5EB8LU2-YnQxf4CQMO8sJAHZKJFsTuhqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست ریاض از کشورهای مختلف برای تأمین امنیت باب‌المندب
🔹
در حالی که دولت یمن تأکید کرده است باب‌المندب به روی همه کشورها باز است جز کشتی‌های عربستان سعودی، یک مقام نظامی عربستانی تلاش کرد این موضوع را یک بحران جهانی به تصویر بکشد.
🔹
عبدالله بن سالم الشهری، فرمانده «ائتلاف دریایی دفاعی» (ائتلافی که ریاض برای مقابله با یمنی‌ها اخیرا ایجاد کرده است) گفت: دفاع از آبراه‌های بین‌المللی یک مسئولیت جهانی است.
🔹
او در گفت‌وگو با خبرگزاری رسمی سعودی، ادعا کرد: هر تهدیدی علیه آزادی دریانوردی با پاسخ سخت مواجه خواهد شد؛ بلوفی که با واقعیت میدان همخوانی ندارد و ارتش یمن همچنان مانع عبور کشتی‌های سعودی از باب‌المندب می‌شود.
🔸
«ائتلاف دریایی دفاعی» در تاریخ ۳۰ جولای گذشته با مشارکت ۴۳ کشور در عربستان شکل گرفت، اما به مانند دیگر ائتلاف‌هایی که ریاض تشکیل می‌دهد از صدور بیانیه‌هالی محکومیت فراتر نرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/462835" target="_blank">📅 18:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpd6s-N6S-560lSy1pYhqcWRkHj6qG0LoqSSPwLJRH-nOoWg3rbQPI08JjUS0RMxMiif_8V8mRIqtEnOdoEqxOIlBCja2kAZuQktqm-EF7qmajdtPdDhyJqly7cjXGa-I9yDTFMa-I05XvMz1wIhMzqXrP8FK4a39v9tF87Tl4XoC4ztUtBkxCdV5xj2QgpsWITsiAWVFpzv_w5GO9_VIG38GguBAv_FAgTtrCvnl5ZxumKUfUeWtVKjtaxN_ibeSZJl4NWK4Y8RCoC0eC2UUCA3w8vY21ze4uVlzPg9_LgKOk2qpvGmdT35jpnNinx5Ro2fBLbDl0L7lR-fRCDLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۱ مبتلا به تب کریمه در یزد؛ گوشت را ۲۴ ساعت در یخچال نگه دارید
🔹
معاون دانشگاه علوم پزشکی یزد:  تاکنون ۱۱ مورد ابتلا به تب خونریزی‌دهنده کریمۀ کنگو در یزد شناسایی شده است.
🔹
این بیماری  از طریق کنه‌های موجود روی بدن دام منتقل می‌شود و علائم اولیه آن مانند سایر بیماری‌های عمومی است اما می‌تواند به‌سمت بروز علائم خونریزی در مخاط پیش برود.
🔹
اگر گوشت به مدت ۲۴ ساعت در محیط یخچال نگهداری شود، حتی درصورت آلودگی، ویروس از بین می‌رود.
🔹
یکی از نشانه‌های گوشت بهداشتی این است که علاوه بر عرضه در مراکز مجاز، دارای مهر و برچسب دامپزشکی باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/462834" target="_blank">📅 18:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462833">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb70a6a84.mp4?token=dL0Mp4V2TEQbxA7VNTptg0_0snkaabEm6F7CzymGxTRk6SOU68aUs0el87HJCPyriA5j-2-JLoNlg8upntqavRDzuaIYilVLKOCGh4hnui_t4y2RT4OIQzAVetOV5xqZZepfDxqJ3Sp3l1vWm8AfXcinTtyNaOjxSyaWdmD1K2wlPsGZqq4etMIvdZ_coWbaiQlcvwC3taPMTJ8Ig_QRT1iIPbDm6vb-LmmplMX8KI0lt82ZdUL09EW2ZQJ2QNtD4SApT_VIKTaNcanffQJo1dKhzDNjcbIKsTvjU5xnRY7qj1jRZh9x6Ayw_QNmNi3u_ykCSFGXBI9sEMm8DXkG9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb70a6a84.mp4?token=dL0Mp4V2TEQbxA7VNTptg0_0snkaabEm6F7CzymGxTRk6SOU68aUs0el87HJCPyriA5j-2-JLoNlg8upntqavRDzuaIYilVLKOCGh4hnui_t4y2RT4OIQzAVetOV5xqZZepfDxqJ3Sp3l1vWm8AfXcinTtyNaOjxSyaWdmD1K2wlPsGZqq4etMIvdZ_coWbaiQlcvwC3taPMTJ8Ig_QRT1iIPbDm6vb-LmmplMX8KI0lt82ZdUL09EW2ZQJ2QNtD4SApT_VIKTaNcanffQJo1dKhzDNjcbIKsTvjU5xnRY7qj1jRZh9x6Ayw_QNmNi3u_ykCSFGXBI9sEMm8DXkG9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): با مردم با اخلاق متناسب با خودشان رفتار کنید اما در اعمال نه
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/462833" target="_blank">📅 17:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462832">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLTMbHD1mVAtInyqLuL68kl_zbL8Isd7em8dTpJc1tawrqhFNm1hQF3evFhuB5bvoG1ykNceaJYLn3b48lYkKJd_3SF5kQbRoUMUzef7NO1_f3zJyGWMIUMRro8yoAi0ZmGJUixQ1FjpQDlAUqd1gWO4BvSVcQL2mpmnePSkBVlz_fkyQk54HhkIK_uw_2gB3PIvurHHYTyurIS4sWOBHcVfOMeHG-5AlTMiFQQ_OrXNOEQOpM3fXKLyc59WfaD0RSSTzqjsVaGU7om-X6c5JKHK4KFjDD_u5QrEOJ_kB3eNlZnB7wiNtFHQrjXHUT-WNgjpUmbiBpII-uB0hVMG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبت ایران در راه ابریشم جدید چین رسید
🔹
چین درحال گسترش حضور خود در کریدورها و بنادر غرب آسیاست و حالا فرصتی به‌وجود آمده تا ایران خود را به یکی از حلقه‌های اصلی راه ابریشم جدید تبدیل کند.
🔹
یکی از مهم‌ترین پرو‌ژه‌های چین، کریدور شرق-غرب و اتصال چین به بازارهای غرب آسیا و اروپاست که ایران در این کریدور مهم‌ترین نقش را دارد.
🔹
در ماه‌های گذشته نیز آمارهای راه‌آهن از افزایش قابل توجه تردد قطارهای چین به ایران حکایت دارد.
🔹
اتصال چین به آسیای مرکزی، خزر، ایران و سپس بازارهای جنوبی و غربی، درصورت تکمیل زیرساخت‌ها و رفع گلوگاه‌های مرزی، ظرفیت شکل‌دهی به یک شبکۀ چندمسیرۀ تجارت را ایجاد می‌کند.
🔹
حالا که قالیباف، رئیس مجلس، مسئول پیگیری پروندۀ روابط ایران و چین شده، انتظار می‌رود این رویکرد از سطح توافق‌ها و وعده‌ها عبور کرده و به پروژه‌های واقعی در کریدورها و تجارت دو کشور تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/462832" target="_blank">📅 17:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462831">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUkxA_PIHn3J04Cq1VpBvfkKb9HmQq5nowtlNumtyTUIEQTQ-oUtAXah0MRmoymT8O-gWMovQ3qiuba6V6iy35swvqNaCxpvWxwL9yAemc1l8hB_581ukTvBnhNrl-x6cAw9x_ZQBJfJp1kQsQss8Bsq2hyM2_MTqVMN4a_1jDIHm62OOUP4Jw6OZNEyEoYOvHFZI3WPTGQ2fJ6bbeQvbBb8XlBc9IRSAM4GALdmEzIlDq3qAyN5CXkZOYQd5K8cxlOjhuD2D4UBFzDL-6OQ10LAZhuTshWg1kp5nBES05xJNu95ovzT8KRLNrt-XndCIeXz7L54kG0-NHFIedxTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: ۱۰ هزار کلاس به فناوری‌های جدید مجهز شد
🔹
طبق دستور رئیس‌جمهور، ۱۳۰۰ مدرسه و ۱۳ هزار کلاس جدید اضافه شده است.
🔹
۸۰ هزار کلاس بهسازی و ۱۰ هزار کلاس به فناوری‌های جدید مجهز شده‌اند.
🔹
زیرساخت‌های شبکه شاد تقویت و بیش از ۹۵ درصد کتاب‌های درسی توزیع شده است‌.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462831" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nF8lfNyWMrhkNXRyV21wSLJDqVb3EWpclxXE_z04ORvTSggGh64EnYKH_gbOi8R85XGSNqg7CjGvAlhRtSGaj6g73g8hLwd8KS8OcPNm0avgVSkLLU7JqFi9qJFulgjamkW0CiIWKIZznpH_IXTXSo6I9U7FBBb_iLTPJcj1Ii0LQ-DE0zP2EANCzN_C1_CHiVVl-HSPjyF-7GD2ikVR3AOyxRW0zzsNDcKW_ZOk8noi4pnARjbaMlcl2eF8x5J_NTpllcUQS0AOr1TBygWpQLdmAToufqP5jEOAVngCbVijm3Viv6al155vbLwkeM3aeuLInNszNcLE9ylOFrjwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1t12U2v1WeoOeD21S1o5sMmtw6yYwXsv6jPS1WJ_NDQ6vG2WrDV6K9i-ZivgRHLn49IF9FPXdjd8A7lSvbMI5100x0m5rVCKP9wIzRXajiqsOa0s3bkKItBda2gbZ3g2EsdGTGC2auNGeq7uN5vhcCVryQqC9KKWt8PP8ZaJfABerH-9PsqizBYnnA_MjRFa6BK-nLCYIR2Nd-37LD70OEzx811IHSTh9wCQ-lo6YaCMmy29SXsXHzGthL8KO4N85_XCWeNr791HwJmMtt9Yx2QgqWCmSpVDaY_FKZU4s_TgQGYNt03BgyapzWp0yYVf7jcD9Pc2otGeUGiLnM5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOypQ4lDnp0xjS_gPJmHqxJQB-qO6skWQQkbk-ShRu0ztmf3ckZRz5Jgn5kHtOAHl3Cf7SvxNIdA7CvTwvPSLbMAXepvuAwDOL12A85CtcoyFzhEEttGGWzys608qLZb4-4RyfgHm1OoqxQM9mGjLpet2ZAiw0MbFFmHN6hs-xLY2hLay-MVJ5VwKjrD1Xh_Ez28QaokKW6PEOoRkUej0u3S9st7mu4cLLwgnKbRSDDEqaTiLy9WSE_EueRjSCAgCkJlcSUNlFaN9z7YbNZNgpKYk0LUFMw0GelcmqE2rJQCa8Av2g-FZoWFemcl51nsFulOW6ehq0R5GPDZqilfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAl3NaPkUF0FOXp5Y8KYNFokK2u48vn_d5RQrOiUYQo8XeOvoxPWH3Kc7tyEJqJMLcXVwUxqHmvum7EyTYhb2cAdaerW1CAGljrGDjn-xAIMlg9aLkkcE2N_IZOHxViQX6EM9NEphD_oF7cRPnLaUud58H04ErE9tqujslusoVb-xpWU0lCADiv0slnK-jiOFUzOFF5ErZ4Ffo6nT0dNZvLFx_8DpAuPkCgGaYOl5BHvMohjwYDY3ihmZz59uwpo3Nf4-Em73aQYP9s8c4X6eCDLJsTvEi2KyRECwYmXCf4Efnn0W-DzQTnib64kAv8WvGXRmvfwVgcb0QTovu_j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FH5oDjB5KETDKf800252uyTwBkR8r10TH2D56L5xYJSaWszKq_DU-u0790bD0V2XYFeCeEgofs5tKF7b4cae2iOpWUP8widAI1di1VROaSyE0RccrIu3uonxVuYfL82oW4RX-UomdbwN7uWS3wzW-VdSCecyF153OdVK3qurWpDSCUCA35TH1bnl8kGDLRk7r0hzzEAmExT0ntgXROmFlJ2UlMzAV8DLLgZm70ok-12xcDwjJvqBnN-ejWvySgF544Td1QtINlmkZ7_TCT7gNoV5-ofKEe93AROtoPuxcAat7Z1_cDwL3M2UX9y2NDFoUp_wcLwb4sAOrw_NDxHYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkgAdRwAL9G_ESnPNUJnYuLgCr2OFsmls2R4OilQMQjdmFoViwV3A1nekSuaIVQiPuK0x9VJ0LBmyLfXsrgHX-kRlGt49rf_Q0rvvi_ETFOtuDpFX67YAmUojwzQyIO-j3Tm-iB3M9K48jLR66Fhv0YnXCXwfsPn-sjL3hqSGWv-9AXyynA4qXGRD15_etcm4p5PcFCBOjjAHF1xUEKIsKw-QcPPGJSC7xU_AuxgxjGm7fa7MhgxB2X6rPE2ajdD6GG9zkJYyUroEnYU_hsmUx08Ykv7xd_DkvXVm1r7YDBdKcG12n2E4-fK5Lsn1Her5ccYSmIqOg563Hy-52Uzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHoizb1d6o7FlUXqgkgrR5Qs1x8BVEAkJPw_rDScJGQyoN4BZDBj6lwHHCnv2KuWouozyFXw7OYgtsdYsDqMQmC3nGtAKKWnIZ61GOzrm8mwzZivl0ZC38yOxDlJfKCPsl-lt-oqDn1AtGVrqetKmftZX8DS3ufb_0S7nPnFPo84MQTRBPL4oGBYJG8K0Ek8IT7h2DK9RqUuhtchWfKR9ZSZH0QGLJtFUu3VaAYKKtUXVC3Dy2CLwPHsQh0OZkDfCe66Y59rjZxqREEFnA5hkq9eIWsO9t-5eo9UdfR928I-j6A36pVlt7DzqGXEN9ae2hQak--uguJS3Xj10Scnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cy5vJecaC1pT2F-gEpek5GHz9-mfo-Txf1VYrbnUhihXVHHAPYj5FxuIsxJXzMYiA3FAGl1tWW90bz42K-8nxaf-8SBJqYFcFTtJY9502WJ4wwj71BUKjccBDRZVVKsRCA3tUjq_okln_cmPHtTHXTGB3XuIf8C53Cre66vCz6JeD76Ezw23YZrLZ4DDhSRN1OgHOFx6F7WD3f8u44eOtb6XL8D9zrJs9__pEEYBJrMzBA85d0ajgCYOUfnalP42ycIlk1LETCvU0PNqvMsYFnTSD4JHL_asWJFHKIPr1_erpS3np8PYAUfV7Q-wrUWILoQ-Oq_xei3Pt3mX186iPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش ۳۱۳ هزار نفری جان‌فدا با حضور رئیس‌جمهور
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462823" target="_blank">📅 16:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65312619.mp4?token=t-tLV8XQ7ePFBVBagFbSYJeatZki9VGlLBiikWV1I3St06py75ilHXpEmA9Tl97KERMwJnliHKAwg7n0zaEzUgsp_OEYpl6nkFZLVX9WnQ6Eb62j9C23OsFhx_ZpJ2yy8vFeTjBThEry4SvuNZMHnFdnlrWz2R_PKkp-t-XlosIqefq8izr7cJLnppDu37sCxc3MNCRyQyWLU4wRIY_qObtED2wKD1rbeMA5dy1J5a5mym64oxsasURr3TQPWnKtMnDIYN-oKvp2zaW8Fsk1EvxURfsBZyrpIE4PC3V4s3FeBQgYm6KTkidVftLAoWGGwRai85OaydDNsvZz6cJVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65312619.mp4?token=t-tLV8XQ7ePFBVBagFbSYJeatZki9VGlLBiikWV1I3St06py75ilHXpEmA9Tl97KERMwJnliHKAwg7n0zaEzUgsp_OEYpl6nkFZLVX9WnQ6Eb62j9C23OsFhx_ZpJ2yy8vFeTjBThEry4SvuNZMHnFdnlrWz2R_PKkp-t-XlosIqefq8izr7cJLnppDu37sCxc3MNCRyQyWLU4wRIY_qObtED2wKD1rbeMA5dy1J5a5mym64oxsasURr3TQPWnKtMnDIYN-oKvp2zaW8Fsk1EvxURfsBZyrpIE4PC3V4s3FeBQgYm6KTkidVftLAoWGGwRai85OaydDNsvZz6cJVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم صعدۀ یمن در حمایت از پیروزی‌های نیروهای یمنی  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/462822" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3yVBjR1fSm_HNtgtNHTtXrf6SH7cAbIrqvPPiB3d907H0Q0jb89JA2jW315TaBFemB900Iu-BpbYL8937z_13HbbELU08e9OVT2H6Ly5S1RKfHPyR2AzKrbtAmrxgdp2wqyl-lWE8jaqXrIngg3SFSHW5o17dpEGmZGEz9Oe4oTwde6lyfBlnfArIB6nb7Q-0AD-AVJSng73PrB5pNq8WJkU1wvusZUq9_UYPjIrQXjyYEFjSNAAc_p_Lp0reeCFxlZ7RjGKRX2vS_kFMxb8_LbQ3j7cUA4cSu7XlBxg1zzmCAFnZTCJQ0GIbOfkJn9bjBz-n0J0eBdh9xNgVpn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف صادرات نفت عربستان به اروپا در ماه آینده
🔹
بلومبرگ: شرکت سعودی آرامکو به مشتریان نفت خود در اروپا اطلاع داده که پس‌از حمله به خط لوله پترولاین، ماه آینده نمی‌تواند نفتی به آن‌ها اختصاص دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462821" target="_blank">📅 16:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabba91c77.mp4?token=kvyMyoq1hlvfIm_kd6hX-CtR0xqtfpS48Ce4QbQ-HwtTLcLdGIsZbAuWOAeAOE2CaZsEzvt8YvSvfwVV4qK6taOofzmCG3vyP2XQpUyGoIl_4IJCxYWSgpqO1xFE8eYKv4hX_ZbDAvPKpufHvQV_MCFRPzywm4ruP0QkWwNW9GCkFKkp0WkFm2t46jzYnY6fr8KhZ-KuXijiivSD4l88IrZs1VFoCv1ToiK2KNgkXCwkgPv_SkKX2lzQ53WAhhmnRHk5cGil0aD7A-3cBoXAv7eoOr0bqpYdFathgRSz2bT5EffASB5QwtODNkM92FyV9bJBzS0XLw3BNlUjRAGj-rvJcAeEVE63vKfke_gtQh30kQX7K3WMZy_RbpF4g2AyWFcS0xEeo0JlMZfN_B7OSeuPO8lfR2xDSviIfXNNUSU-KwuQGw6b0fHbb8jAGyol6T3FX7no6u9KSQq6_S6DdlwMo9seRq8frmT-OSnDqTaoc1eQpHr81bENpi2L8WZnNZEHI-EO_dbZfVnmzlRGxtd5qMAKtqkOOwydSK6XwVNzr2CGwHVnyyG2jzhOvg8wGymf9_tYbklOEBBvVjQMpf8cgcUs4v98ajLOpGNBaRfPpgQlalAvrPvVzFdI1M7_lA9B22FGCJ50Dy7NJoI2hWZXSRJVllFv3zqw3G-5vMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabba91c77.mp4?token=kvyMyoq1hlvfIm_kd6hX-CtR0xqtfpS48Ce4QbQ-HwtTLcLdGIsZbAuWOAeAOE2CaZsEzvt8YvSvfwVV4qK6taOofzmCG3vyP2XQpUyGoIl_4IJCxYWSgpqO1xFE8eYKv4hX_ZbDAvPKpufHvQV_MCFRPzywm4ruP0QkWwNW9GCkFKkp0WkFm2t46jzYnY6fr8KhZ-KuXijiivSD4l88IrZs1VFoCv1ToiK2KNgkXCwkgPv_SkKX2lzQ53WAhhmnRHk5cGil0aD7A-3cBoXAv7eoOr0bqpYdFathgRSz2bT5EffASB5QwtODNkM92FyV9bJBzS0XLw3BNlUjRAGj-rvJcAeEVE63vKfke_gtQh30kQX7K3WMZy_RbpF4g2AyWFcS0xEeo0JlMZfN_B7OSeuPO8lfR2xDSviIfXNNUSU-KwuQGw6b0fHbb8jAGyol6T3FX7no6u9KSQq6_S6DdlwMo9seRq8frmT-OSnDqTaoc1eQpHr81bENpi2L8WZnNZEHI-EO_dbZfVnmzlRGxtd5qMAKtqkOOwydSK6XwVNzr2CGwHVnyyG2jzhOvg8wGymf9_tYbklOEBBvVjQMpf8cgcUs4v98ajLOpGNBaRfPpgQlalAvrPvVzFdI1M7_lA9B22FGCJ50Dy7NJoI2hWZXSRJVllFv3zqw3G-5vMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌گویند شما از گرانی خوشحالید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462820" target="_blank">📅 16:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332d0ce5e2.mp4?token=ZvFSHu12kULve77Xn7LHsZ42hQPywjlnQNiYIK4xf_cqK3xNpL-OgNC9a3kpSXDOKUagD3f02CqtZrFwJw9PeswfsEgLco4hXNk0r2ddh3wVkA9JKlkUCWSrzFRsTXzlO-AvKtol2teYKch6wUMo5rEOfHFGCfU-v9xIaSNy8DdjqUBuJjoiypY66nk8q3-bJWLoMsCifNhoR5kCiEEpF3CbN63DvXHYQgY2D-s4hvVmAsXr_EFMsS_iCtfSfIwj-vIrYgoUdRFcjltnIlUrExsMDFO828FAzLg_rtYMLBykS97Jgz5LN_jrdDxUxayEiwm-e9lGaob4vDjX_WJNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332d0ce5e2.mp4?token=ZvFSHu12kULve77Xn7LHsZ42hQPywjlnQNiYIK4xf_cqK3xNpL-OgNC9a3kpSXDOKUagD3f02CqtZrFwJw9PeswfsEgLco4hXNk0r2ddh3wVkA9JKlkUCWSrzFRsTXzlO-AvKtol2teYKch6wUMo5rEOfHFGCfU-v9xIaSNy8DdjqUBuJjoiypY66nk8q3-bJWLoMsCifNhoR5kCiEEpF3CbN63DvXHYQgY2D-s4hvVmAsXr_EFMsS_iCtfSfIwj-vIrYgoUdRFcjltnIlUrExsMDFO828FAzLg_rtYMLBykS97Jgz5LN_jrdDxUxayEiwm-e9lGaob4vDjX_WJNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعری از شهریار با صدای رهبر شهید انقلاب
🗓
۲۷ شهریور، روز بزرگداشت شهریار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462819" target="_blank">📅 15:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwKiZwJFrejyW89qLEkXE8QkiULgCNm-G1oRve0758Da5V3iSFdT_70mCnllTxF9ssonAY-TNpMovxtdgeGwgmp7tl9D6F0eRUcfk0MpSpirCPD5eiplORF25XsiDXQ-Gj3s35fkF0icJEULHbeViQdVGd70hfva6j7HMCfpjVy-nAjr4hvW4ecOvqDfuwigYsiMoxWCzNalmWvCcteFXgshRYHLzWx6gmeKMVkgBurM7n-T6fvM2vQrppGU-4diq0MGWJkfnVqdbVl5uCJM0QgXQWEMbpy_QUBuCQ_4vX0eYMJjnO5PdtcBy0PmxosVHDKcU8pFupdz0-Bh_GFi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندۀ قرارگاه ثارالله: امنیت کشور مدیون مردم جانفداست
🔹
سردار نجات: ما خادم این مردم هستیم و ما باید بتوانیم قدردان ملت ایران باشیم.
🔹
مردم ما از ابتدای انقلاب مقابل دشمن ایستاده‌اند و درنهایت بعثت مردم با شهادت امام شهید اتفاق افتاد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462818" target="_blank">📅 15:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLsas7jO4ujsD8Y9RZEmclQYnJN6DVzmnAevBCI4xqqMjA6BXeYcLTF8PkEg7bFLCBQJSPFAA-BMPGFyW9mm28l-aGNjnJ3DJMr4ZAOT8xXSjndRxiQXWlTD839eKc51hUq1WSxfEK8Dc30-JqpC7vXfkL62qdspIwoj3ZUGMTp6b0Y0LvS4l9KQoTv5qoje85DWSvBpM0IlIuPIb8IxviDVlT9wO-L8774iAffEYOHMQJUHncFUmmNhzTl6ya8erTFQhzsJ17EbxsBOnxFuEk3T1MfTmS56Sr0Ua8SSsdxip9jN3d_UI_ht8MyNEonPrL_dW3V4VW-nnOqB1sEGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال-بیرانوند؛ شایعه یا واقعیت؟
🔹
شایعه پیوستن احتمالی علیرضا بیرانوند به استقلال بعد از پایان دوران خدمت سربازی جنجال‌برانگیز شده است.
⏺
دروازه‌بان شماره یک تیم ملی معتقد است شایعه انتخاب استقلال به عنوان مقصد آینده‌اش حاصل برخی‌ها شیطنت بوده و چنین چیزی حداقل در برهه فعلی واقعیت ندارد.
⏺
از طرفی پیگیری‌ها از باشگاه استقلال نیز نشان می‌دهد این باشگاه در حال حاضر هیچ برنامه‌ای برای جذب علیرضا بیرانوند ندارد و با خرید محمد خلیفه روی این گلر این جوان سرمایه‌گذاری کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462817" target="_blank">📅 15:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77002ffb.mp4?token=S2Iud_KS_Bdy2Hi9LF2_F3zbXJN8_rwkwCRRXPMXzcy0bqEKZeq1LaXpW8YygCKPa9u5HAcoDO6CphqLrVD_LdCzwfkG3lUgIlYdrnNB9sCaHILYKCXSftENEhuH7LqtnIQbVjXQxpVpOfTTenIliTIzhSOA7MoYK-Szve7zpCTUuWeOSqv5YLHF5ztWn0CX7Q2eJXGrynlourYEZuH9x1wvns_sTnk5_kO8c-tnSTGzawq5nFJaHyH6A3A7yEOVto2pLdfFs-sN3w-j-8XRyMGZyNZEU_sL9X6cMEIBeqguHsTX6RlvP8bdyhwB8WtYS4zNSEub1ECrU4s-ORGOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77002ffb.mp4?token=S2Iud_KS_Bdy2Hi9LF2_F3zbXJN8_rwkwCRRXPMXzcy0bqEKZeq1LaXpW8YygCKPa9u5HAcoDO6CphqLrVD_LdCzwfkG3lUgIlYdrnNB9sCaHILYKCXSftENEhuH7LqtnIQbVjXQxpVpOfTTenIliTIzhSOA7MoYK-Szve7zpCTUuWeOSqv5YLHF5ztWn0CX7Q2eJXGrynlourYEZuH9x1wvns_sTnk5_kO8c-tnSTGzawq5nFJaHyH6A3A7yEOVto2pLdfFs-sN3w-j-8XRyMGZyNZEU_sL9X6cMEIBeqguHsTX6RlvP8bdyhwB8WtYS4zNSEub1ECrU4s-ORGOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار اعضای دفتر امام شهید با خانواده هنرمند شهید پوریا شهبازی
🔹
شهید پوریا شهبازی از هنرمندان تئاتر و آهنگسازی بود که ۱۰ فروردین در مأموریت داوطلبانه در ایست و بازرسی کرج، با حملۀ دشمن صهیونیستی-آمریکایی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/462816" target="_blank">📅 15:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H88ohkww2Dnm5vE30yUlY3QgCshET8KmaLxxzc_Ybgg7yIz2Di4uiaMcsnefGWVEJ8rSe3VBFhsGBko9-HVklz7m8fgIpC5EDHwR0HNcWuHpfPO8CWoj7lNwRxi24HrLJVz6gIa2jAOHog-17u2hW_JEgAlxuzX8Cq4g4dn-HNzW14_DWc7I2fTfTlOPS7xSLC5m9ZJYxyG65xRKmgbjvnKuJ8xvwNTBgxtlOYsCzuRnjrLs1yHAS6FIQEwy6mzwOSt4Kqk_GFcDMOHHoJDzUYeBp0XpikeU_wK7qYY5WvrUeo7iD5Y2tt-1w31vTrbXVjBB5xNTs5RhQPvIizdxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkLV5tyeu7LyHuk3nDfGcTv1fFpxpnVgxbmNnanqPwthd0qnrwgDPvIDMGKTAoOfGvgP_Y4TZo01rW2pyRKw9HoMiKZ3OXOYgV8fxs3girjPET4IAjZJKKtWAgz0QspfKxvPix4jjQWRTpTVIiSnCtKv3kXZfMvRnHogf_6kfHuKS9eshVzz8swOUxoGXugzdsxTJZ5HSaO_Sr_JYoWauE_WDVhTvhd0C5f56beK4vIs7QyTslDaGpEAP7_qBJgEfNI0KSQZsmjwglA1OKkf_rSkdjM3pHRaVlimvLpzliMGWs8V9TIRCRL9AhXWPMUn_he2Bol9LKfFDT0jUir7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8NPGWD4kgESoVl_07xUHUUCzImc7yaU8fnkMwjHc5Hg3YT8S0ImIgsSP0pkTZaIvBTVm1rNTLS6CHKr825EAsrF0HbzYpHyLtKZmVjScRPRQ8kbcQCZcd1EyVxX91TAeenKyZng1uAchwtLFTPLBB-3p5vuC86SLpSpTeInOkczQ7G5nlii5__KHIq5UIlPD3j8fLK4LVUy0Lpn2240WFhaUfm_82pOwV1bm_CFeeoB5ktwf-NnaP5zAFh8FlecYNq3krYOOHYKfvb4k6Vh-krvR6tAxWIxEb79k4iYq-euJiWF9oTFtFR7sYHcFEW_1PjZOXxL-Ea35jrckXrS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkLV5tyeu7LyHuk3nDfGcTv1fFpxpnVgxbmNnanqPwthd0qnrwgDPvIDMGKTAoOfGvgP_Y4TZo01rW2pyRKw9HoMiKZ3OXOYgV8fxs3girjPET4IAjZJKKtWAgz0QspfKxvPix4jjQWRTpTVIiSnCtKv3kXZfMvRnHogf_6kfHuKS9eshVzz8swOUxoGXugzdsxTJZ5HSaO_Sr_JYoWauE_WDVhTvhd0C5f56beK4vIs7QyTslDaGpEAP7_qBJgEfNI0KSQZsmjwglA1OKkf_rSkdjM3pHRaVlimvLpzliMGWs8V9TIRCRL9AhXWPMUn_he2Bol9LKfFDT0jUir7Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از آثار حملات شب گذشتۀ ارتش روسیه به مرکزی در جنوب‌شرق اوکراین
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462812" target="_blank">📅 14:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01da4d854.mp4?token=cmwQx8rPu2_WEkdvTnEU24bFYhyhoosOKy_eMzMR9_lVm46BkC2eWAI7LVnfg9lrfnnBTT5Dg2WhXvDaqUM801dhZPWGs485sCBRLj6iAdfLQXaKXcBRmU9Teyr96tkBJXcuLAy_DRJsYYupKY7uH_U7oXNzhIsOEgyNoVnbK2KNEAdVpO5hBx8p9UwMXyw7uYb5nCLGcpxLhwLRK0LB6BNjLRu-pSWattmteR9u6OVjJ7X8Gc_Kn0j8UQmklbubI404nhGIxYEfw-QXRNwoot068GWMNP5xE9qOYdpNCCN9-eNT063cQupt9oGnp9zRpUv3VwSe5PhKkJlSbtYwCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01da4d854.mp4?token=cmwQx8rPu2_WEkdvTnEU24bFYhyhoosOKy_eMzMR9_lVm46BkC2eWAI7LVnfg9lrfnnBTT5Dg2WhXvDaqUM801dhZPWGs485sCBRLj6iAdfLQXaKXcBRmU9Teyr96tkBJXcuLAy_DRJsYYupKY7uH_U7oXNzhIsOEgyNoVnbK2KNEAdVpO5hBx8p9UwMXyw7uYb5nCLGcpxLhwLRK0LB6BNjLRu-pSWattmteR9u6OVjJ7X8Gc_Kn0j8UQmklbubI404nhGIxYEfw-QXRNwoot068GWMNP5xE9qOYdpNCCN9-eNT063cQupt9oGnp9zRpUv3VwSe5PhKkJlSbtYwCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم صعدۀ یمن در حمایت از پیروزی‌های نیروهای یمنی
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/462811" target="_blank">📅 14:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462810">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9384af4849.mp4?token=CUw9iHo0YudU1aiLQcdTIX8uZCaLIWjfQJ9a-fkcQtmJm0TpdITuEcrshFPGCHjrkZzgYBv3ty7g-R_EzwUtKxnP_gCzjF5qPD3IQLKDJCeiEqrbOCQBZZ_-lSCyK8ZWNTG8IiCZsE9hZ0vNmn9IK-LBz1tNwUa1U_3dzjcPn29WfmYbXLiDL1mOLTP5zniFDEO4nEALW51H8f1haE53b7xwLHFrQx6BlI1LXJtbnnG9MoZwOQZ5zUSNYdrbVMPo2mT9hNoSAxOPnSFe9lmojcN3LHhzhwIV5o_yzV4B1Q3oA4kGMEibPm7jL-TdKR7BXshtd_q4hst_35x1bAPXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9384af4849.mp4?token=CUw9iHo0YudU1aiLQcdTIX8uZCaLIWjfQJ9a-fkcQtmJm0TpdITuEcrshFPGCHjrkZzgYBv3ty7g-R_EzwUtKxnP_gCzjF5qPD3IQLKDJCeiEqrbOCQBZZ_-lSCyK8ZWNTG8IiCZsE9hZ0vNmn9IK-LBz1tNwUa1U_3dzjcPn29WfmYbXLiDL1mOLTP5zniFDEO4nEALW51H8f1haE53b7xwLHFrQx6BlI1LXJtbnnG9MoZwOQZ5zUSNYdrbVMPo2mT9hNoSAxOPnSFe9lmojcN3LHhzhwIV5o_yzV4B1Q3oA4kGMEibPm7jL-TdKR7BXshtd_q4hst_35x1bAPXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌آرایی یگان‌های مردمی جان‌فدا در رزمایش امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462810" target="_blank">📅 14:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThDJY8FuMQjffmB554sFas3B3V3YvYuss1D7hQkWMFOpbvcvT7lA4dFyjQ-Fxist8ZjgNeVt3nDjYTOuarRmHKfH1LzPsIdlcryWDxHyvCNrNATd1cRjHq8bkQ3zHBr6QGe7b4xrWXBwdIswkEMZPsic1KSjjZTL1Soy1yZTSfi1PFLKJ98hUM-qaIBr8GRIezj6TZiUERlWzcTlYGv3G4Nt55mOfIrOV4PnkA5u2NzxsC5EkuMPH10MTIeYM0TGJlbfP1N5bTs-QYlWEU_bCKFdEkma3w2EplVkDP0Ay1elkp0LzmWKLGYOcfPGnMnx5XyoRfg7dBO9N6A9lCplMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjD-L42hWT8gekqHJCmKwTRC-JNcxWEp8mJjOp-O6QmbeG49Sa0vp2fz1HtRi28pgjSwGME_Fi2S9NAKASxJdCVsOc3RhEQw4cgs1nX6k2sRn5B2wiFOPWelgAn8rHFMng-h7PMF67a-n9ovETuZDIr0xb6NPk_9g9r3CcJzEc8mDw8uC3kMAe-WSivQUh_Hp58-92qr-auJjq9mdI_BFzOdtm9uMh5QgvpL5lGUvwIM36cBr8Co9b1GzKr1tWTyBfGSgybAEEgBWgBoUGSrheiUxls8d_SmfgZ3wR-FpkXZQ1N0f3It8VTpJDFuZ455vmR6E8lbNmSe_cjzmr3XSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRHdXnsSTEeYqjLG6hMJRLMspFKx5LiEEKWycpgc3nmlJKc3vmeSuwbRfOYmA-oblIMJJ5HoJpas-YwcME0CYa1INyVooEYXs7ME6fJojIvsmGUlQ_VXs0hkzYT9bRChnZ5CIC7QO02I5WCizYxnTcu9LrNAneYivo3bA_GNfgY8VGSg8zOPI0YJySJDvc4k81IKlc6SLKuHY0r1OXRmLgRN0elbZyPVD-iNgU6PiaAS9mhU8U829B69mbeTpivUkdvbuzYD9tIVjwXL5t1aKgC7z7s5Wj93tQSzOKrz2-xvWLR2jUFf_O8x8nTCmye6glxTUaqX3cxWGGhcUPlcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp2GXaFKW8EwuhJmZdmTYtoP_VTiYmJhex3sZBpCBOLh0HXKWk21Y7Lbqqg-Uj9I93P8qN8ZiQIdpTE5IHuI9yDvvxkckSc07yygIQQbsnhupm3c0AbvwPMilST1u04yhK8oX1V-y9gIcBtot1l04CDbTq8hiT7C3ERkpNhgo1l_y2EN4G8pE1tO_k1vzKH1EC9Ph32o0KyklJVZu_uwEzNi-dLZPtM3oYUdfP6K_ckdEzZVQ36Bab0JfJBifsFE52H6MVIvkiRAhTB-GYwbrhNdXBc4zUUnYHW2gnVGQEJvkFaM1lmPUj1HdF9VOFMmaspMITSLrxjk0HZXfqCJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfyUHs1NJ4n_FUNTeQgSRTMWC_IbcehmS1VuLhGWiOT2QYB5B6fNvdfzcbEILaYkR-rJ4p5XnXJjLFBn1uqcUHCmuSDTQisTtN_iqSAiyj8IMA78b4GPcTG_YThJ_uC3p0QjXtrC3F0LHrEPb_mFIakEXMgJUTyvtQIVKYtixbujGZB5vSR2mYOG9_Mc-vjO0irWQHQ3KE-ObCdN0h5qFHMg45XTe-eVMsERREUsZNCujzbz9RCGObRDXs4vH6Y8pmLIhhn-DK76YOVlBMc-yF0uWSABuMYVwTcP_Qji-I8dU_iHghW5IWozPd2XDYdGN48WV7yFogz8s9SNR7xAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQqT4A7apZT9RFVUFYaRup-KMVKiQ19TycBIWi6IGt7bo4jADDUpY_Mssx5QDCWPweOps0HSe_uHxQKfVIGtTjSfkR_X3U5ftURcz-BsEe_0REjxOkGPUT6Z5wfu8ZjTWC_WTqwwAuw-C_U8_A3c8R5oqNV0QkUK5NV4Zu0_R3BCr4FKdODGVnz2-ZOANc1LwCuFLipFy04Pggn82uu_HUu3I4lmp0u-J3Y7XYxNCOc0P5v5iyyIGksJq_3pkEgAn2qkkhx85yDdR21Z_rltHE5J0iMuEbwMXynGY-suzmeOgPDbzKhrxwpeGq9zx2sFRr2uoFq3gEi1_GDjsrTIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyhaw1MnPxN2X48hz4PfeAkmooXaS_UA-yt2wPPJsR1B8qZi1AsgI6-WjX-gAWu4KEpqtT9Z6Tlvu5eoR2mz2YVVqb0kpDV2hUDuATR-0xr4Ey99fUYRE-k__SQn9AIRA1EhXVyZLx69Mc0gWGF1JTiXQXFWk6X7H3cAtHOFbQd1-pgXGe4jyON1v6wkhwRmrftWi5kvjtUmC8DVhA976h2HCS2iI8Rk6-ZSGvo1r8m6166_ZGtGfhO6IQ2SGJqSM0ixVrjMCR746HHbYjZu12QqlJmi8OT2MO2uBjQeJ2Hpal67JrBygFsOA57WGNBafyY3W2oiM-Xd3G1VGQ9t0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماکان کجایی؟
🔹
جشن پرواز بادبادک‌ها در همدان به‌یاد دانش‌آموزان شهید میناب.
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462803" target="_blank">📅 14:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-9eVJe0WpeJ8sqxGCubzp7ZAj9X_Zjt_ei95Y10vU_jSJmLePd_cCUuFXODDKbTzlrYZzlPYrqciXcHDrs_sl2O0mtHB9I5JeUALzEhkPiAQbgJL09IwV6MvF_ecN2zemc00Y40Fk3XY5FOUJgeLZAtwtzipNAhNJwywYeTO3XJa3zrFwwXmKhHun8SvKaTy4fGIk-6LK548olkOyjpE1ku-DoFDyqf8o8gAIodz5Tbh65PpW7q0CWpCpF8vWUJQQwmzsoaFsHJzrA7G0bckPnz2W930mGPz9DEPbS7xpKsU74K3lby102XQcbwypPT7pb6Assbm_shY_ojTCjZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زخم کاری چین به آمریکا در میانۀ جنگ با ایران
🔹
گزارش فایننشال تایمز نشان می‌دهد چین حجم دارایی‌های خود در اوراق قرضۀ آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۸ تاکنون رسانده است.
🔹
پکن با کاهش ذخایر دلاری خود، به دنبال کاهش ریسک‌های ژئوپلیتیکی و مصون‌ماندن از تحریم‌های احتمالی مالی است.
🔹
این اقدام چین در میانۀ جنگ آمریکا با ایران، می‌توتند فشار اقتصادی بر واشنگتن را مضاعف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462802" target="_blank">📅 14:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ded40dc29.mp4?token=TfYNUpOcMunI_3vLjsaIj2jpbunnQyyBm2QVeXGpHjc8bwwj77TTp7pApXMRhut_ViCWEzPNvYSljoduZjzv8zFL7pA6hGzCkpYQksrj2TCi_p5aI_GzzMkXIpWSGp4HKYrM6BwNNejdFVr-yh-WDYiCLl2-kpaW3QIfoZ5VyCTiN_5IOnps3a7-6iaGYCpS7T-uIOLotm1N_bQ5WHFfRR8csxKh7VwO-kPzSwi97nPVLDvT4bjeXW-cx74C7Zi33RHDXn3H9lDPnAonVGsykoQNC-dhbdEOp3R9OcE60MIyqb5qciDWtaRBPDpx7w8pYjH0F7_qvDASt58QNr8Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ded40dc29.mp4?token=TfYNUpOcMunI_3vLjsaIj2jpbunnQyyBm2QVeXGpHjc8bwwj77TTp7pApXMRhut_ViCWEzPNvYSljoduZjzv8zFL7pA6hGzCkpYQksrj2TCi_p5aI_GzzMkXIpWSGp4HKYrM6BwNNejdFVr-yh-WDYiCLl2-kpaW3QIfoZ5VyCTiN_5IOnps3a7-6iaGYCpS7T-uIOLotm1N_bQ5WHFfRR8csxKh7VwO-kPzSwi97nPVLDvT4bjeXW-cx74C7Zi33RHDXn3H9lDPnAonVGsykoQNC-dhbdEOp3R9OcE60MIyqb5qciDWtaRBPDpx7w8pYjH0F7_qvDASt58QNr8Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از رزمایش جان‌فدایان ایران‌زمین
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462801" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3c5fae1e.mp4?token=PCUie-AdxUJu67BoKjUUHQjD772DkWWWRWiW6injQfHzNQYolSBIYqbPguWh9Vp8UmNF2__SPGMtsMIxYrWtL0kYNUJdWqjFoDYE5WvEVEXg1DvFYeiNnaK4ge1_ypIJkkhs4449UeB6ObMqfo91OeuwTlWbCuLrIOSZdPgH3VapbbKNACpZVKI5XWTBzoQcBpMgPFdQ1nufpkKb1DWNl8tFFShK9L7vDZ6G4sHNxlCAPPvjAuqov9l4NR-XrHz-zF1HRaQDSBmqXPeFcyRAM8FwUkKMbTqLY0bEr8SbFb0oaBuQtTmnBBADJ-r_MhaxWYGkdBNM_pMT3jjvKAWUNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3c5fae1e.mp4?token=PCUie-AdxUJu67BoKjUUHQjD772DkWWWRWiW6injQfHzNQYolSBIYqbPguWh9Vp8UmNF2__SPGMtsMIxYrWtL0kYNUJdWqjFoDYE5WvEVEXg1DvFYeiNnaK4ge1_ypIJkkhs4449UeB6ObMqfo91OeuwTlWbCuLrIOSZdPgH3VapbbKNACpZVKI5XWTBzoQcBpMgPFdQ1nufpkKb1DWNl8tFFShK9L7vDZ6G4sHNxlCAPPvjAuqov9l4NR-XrHz-zF1HRaQDSBmqXPeFcyRAM8FwUkKMbTqLY0bEr8SbFb0oaBuQtTmnBBADJ-r_MhaxWYGkdBNM_pMT3jjvKAWUNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش «جان‌فدایان» تهران؛ ۶ ساعت پس از آغاز، خیابان انقلاب همچنان در تسخیر جمعیت
🔹
رزمایش ۳۱۳ هزار نفری «جان‌فدای ایران» که از ساعت ۸ صبح امروز در تهران آغاز شده، با گذشت حدود ۶ ساعت همچنان ادامه دارد.
🔹
برخلاف اعلام اولیه، جمعیت حاضر در خیابان انقلاب اسلامی -حدفاصل میدان امام حسین (ع) تا میدان انقلاب- چندین برابر تعداد اعلام‌شده است.
🔹
خیابان انقلاب و اطراف آن هنوز شاهد حضور گسترده مردم و جان‌فدایان کشور است و رژه همچنان در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462800" target="_blank">📅 14:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5683a85a1c.mp4?token=cxtnP4MKEhTR-43I0_yeqNQA5o2px32MSANprWPvP9AHNGlaNiEGjEbOGasQS1OtIC2ueITHGa6AQw32QemuDwhcCPLDB8eDOhRFuBJcq-FajJh9gFxMoEZXPLgF1AldRqpOvo2oO9U9SilmJZTSQR3KBg14n1-3fMKC0TB2f11Gtg-8dc4cWdjEmWRu6e8oRakOoruPlTTear6acQgxXiOn2aU7TzdT1IeZyVQjgYhDKuo72iRmCFE4PT9_cme88QKYbp2k_XgF0UDKpjvzqHUK2n-S36uk6b_YRQ1UnawuG7Z9e7bPwbtlKkxSG1DfVG9M9GnG7-M_NUI8ZAnkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5683a85a1c.mp4?token=cxtnP4MKEhTR-43I0_yeqNQA5o2px32MSANprWPvP9AHNGlaNiEGjEbOGasQS1OtIC2ueITHGa6AQw32QemuDwhcCPLDB8eDOhRFuBJcq-FajJh9gFxMoEZXPLgF1AldRqpOvo2oO9U9SilmJZTSQR3KBg14n1-3fMKC0TB2f11Gtg-8dc4cWdjEmWRu6e8oRakOoruPlTTear6acQgxXiOn2aU7TzdT1IeZyVQjgYhDKuo72iRmCFE4PT9_cme88QKYbp2k_XgF0UDKpjvzqHUK2n-S36uk6b_YRQ1UnawuG7Z9e7bPwbtlKkxSG1DfVG9M9GnG7-M_NUI8ZAnkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال به بار نشستن طرح‌های برزمین مانده هلدینگ خلیج‌فارس
🔹
هلدینگ خلیج فارس طی دو سال اخیر با تمرکز بر رفع گره پروژه‌های نیمه‌تمام، مسیر بلاتکلیفی را به بهره‌برداری و تولید تبدیل کرده است.
🔹
در این مسیر واحد اوره پتروشیمی هنگام، طرح تولید پروپیلن ارغوان گستر ایلام، طرح تولید گازوییل یورو۶ نوری، صدف خلیج فارس هایکو کارون یا تکمیل شده‌اند یا به بهره‌برداری رسیده‌اند.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/462792" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDSqnKL37OaBsDNkZtQAVKesbrzd4FcXmKObiOe7xwHtjoZ-OroaHzWUKOWzunKXFBpHZb5pkPWH7WZsVNWmn6LRIS6knUk0rQvXTB44tfu_j61PboZrWKPZeG2oaaH9Oq34sh9e52QrQwaDM-_V1M-alqScDkf6qmh0R76em-HZnrDgzwSLUvEh3mm4WLpJgmNfKUX_QrnfGs1uHlMkGlqsqkuJdPSKoAZbJNCPDpVDw9KHeuLUfP78kADxS74UHx3PyrsairJkI9Dx58bRHyg5n1Bcy8iC97tijo270xcqkU6uFU383g-6kSkzqj6YnWLpw12TzqxsMGqv0Q2t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/462791" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/462790" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3763fb0f9b.mp4?token=hdNvWnVX52jWKnRZVjg6uL4bpimJ06U48nIqLArwMdqwVu0Gcqv-D_eOqPXf6W1A_Fr_zyCcDAJvWjuNyBaGcL4XfjL4dvpn1PKkaTH19E8ECXefdhMwRr3-SFT-TFfiGJYTjWa75XsZdXPZjMuWFt5sT64skEmQiYB_DtN6q8bhYH2li4qYnsEWF8QROM15l43gTBT1a8FcbKnQ6bp9qEoDCg7jY4aJ5WOYHlag1mhhIEnoI0K56WinQVQJYRhVQn6KjQTdZ5bUobRJxSW71m8RxxcQ9WX_PRiXPJ64GwLWNRhznXnwroNP74LYJ45IGLSu_MW1UZrzQsPskVDqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3763fb0f9b.mp4?token=hdNvWnVX52jWKnRZVjg6uL4bpimJ06U48nIqLArwMdqwVu0Gcqv-D_eOqPXf6W1A_Fr_zyCcDAJvWjuNyBaGcL4XfjL4dvpn1PKkaTH19E8ECXefdhMwRr3-SFT-TFfiGJYTjWa75XsZdXPZjMuWFt5sT64skEmQiYB_DtN6q8bhYH2li4qYnsEWF8QROM15l43gTBT1a8FcbKnQ6bp9qEoDCg7jY4aJ5WOYHlag1mhhIEnoI0K56WinQVQJYRhVQn6KjQTdZ5bUobRJxSW71m8RxxcQ9WX_PRiXPJ64GwLWNRhznXnwroNP74LYJ45IGLSu_MW1UZrzQsPskVDqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروس و دامادهای جانفدا در میدان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/462785" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926a0e6955.mp4?token=CLdBlmi-YeY882TaNUwXrI9CS3LKX_-k0abWFwU5-rxAgtNpURzPeNTCXJjjzAc_uCmKSo3YLPcwEBIAZjKcU1qyhE0EtUTN21NKJD62XYAnmX6Go_9B1GZ63LFcc5g66jlkU8qRuJryIcMuE6deUHjfFTPSp3Y7lA5wuSi9E7KsJB7VNsQO5mjAKkOU5yfQE_bq86RMep4s4rfKNw_Jj4uRXAEIUGEFggRCGoRxWT7zT9nJ0onQiQ6lVG5XxZSQcpmf57Y9xDpz89CrG4-O3FL9IW3fBa_c5s6Iy6fSMqS1ffN0Gtr0gR2ss0Q2tZPAvncSDf3IkzWJ4ccDt4-Z4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926a0e6955.mp4?token=CLdBlmi-YeY882TaNUwXrI9CS3LKX_-k0abWFwU5-rxAgtNpURzPeNTCXJjjzAc_uCmKSo3YLPcwEBIAZjKcU1qyhE0EtUTN21NKJD62XYAnmX6Go_9B1GZ63LFcc5g66jlkU8qRuJryIcMuE6deUHjfFTPSp3Y7lA5wuSi9E7KsJB7VNsQO5mjAKkOU5yfQE_bq86RMep4s4rfKNw_Jj4uRXAEIUGEFggRCGoRxWT7zT9nJ0onQiQ6lVG5XxZSQcpmf57Y9xDpz89CrG4-O3FL9IW3fBa_c5s6Iy6fSMqS1ffN0Gtr0gR2ss0Q2tZPAvncSDf3IkzWJ4ccDt4-Z4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در مسجدی در پاکستان با حداقل ۱۷ کشته
🔹
وزارت کشور پاکستان از کشته‌شدن حداقل ۱۷ نفر و زخمی‌شدن ده‌ها نفر درپی وقوع انفجار در مسجد مقر فرماندهی پلیس در شهر کوهات در ایالت خیبر پختونخوا خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/462783" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB_WQyf1j6lX8Iy-XVAyxdv1rxWZplVOmuQAyDtGcPLw3pWWcQr5lwhm0hZ3f2UGsefW-37LL7NKKhz4zyBRYc8xWr0-eJoNRwwfQHiInvzgIO_Bl9inouN6Mc1ff5i0jZ8qs1eBzcEB1hcVpSv0DEGyFxcX_BhkiHPXTi-b7m4w9alcfrMVIrA2-0eBbFu42V7JKpAXOLP9XnzNGsvAn2Kb-OwRaIIpWQyffiibM8xlQcHP0i9X7k5Vxx92x1d3Xlc4YvCO-rDnf1LVFNnex40miWDsi30f8BKFafjVrF6bHlhSQkmCgNMoJNEggLi5adE57W_0faqWTbo5FlwdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعۀ تهران: تا تحقق همۀ شروط رهبر انقلاب، مذاکره‌ای در کار نیست
🔹
حاج‌علی‌اکبری: دشمن به استیصال افتاده و برای مذاکره التماس می‌کند و میانجی می‌فرستد اما تا زمانی که همه شروط رهبر انقلاب محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود.
🔹
اجتماعات مردمی تا هر زمان که خدا بخواهد و لازم باشد و رهبر انقلاب صلاح بدانند، ان‌شاءالله با قوت، طراوت و ابتکارهای تازه ادامه خواهد داشت.
🔹
به حمدالله وضعیت میدان خوب است و رزمندگان ما اشراف کامل بر صحنه نبرد دارند. مدیریت کامل ایرانی تنگه هرمز نیز یکی از موضوعات مهم این روزهاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462782" target="_blank">📅 13:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb35813c4.mp4?token=NhMQjS3nQWhHQ0TscMz2sy24DT9og-QeFxBy5zJwV6_bH7snUS0BUomYshPG9ghTm3Q70CPxE8wx6J-hYhQt58NqyA7DtLuT913y1CtvGRbg6fWNVdxUK1kH-7J0aEH8ABI1DuR3BlaC2gUwlPw0ueCnPyYJwjc-PG5Cq9kfVHkbS7ekan0htc-6r1AQxIQ1l0cnw-k4YLKFX5Ytyip2Gm1ve55pZL5WTraBJJbt-XcUUE9LSWkiicTDF7gQiO4F4RmB6cQXTZKfkb86I-qrBwVga78RV6HEVMngFN0fBcEBu7FMJi5pmauXMi8lLgkhVqXpOsEeBM7VlU5V-amDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb35813c4.mp4?token=NhMQjS3nQWhHQ0TscMz2sy24DT9og-QeFxBy5zJwV6_bH7snUS0BUomYshPG9ghTm3Q70CPxE8wx6J-hYhQt58NqyA7DtLuT913y1CtvGRbg6fWNVdxUK1kH-7J0aEH8ABI1DuR3BlaC2gUwlPw0ueCnPyYJwjc-PG5Cq9kfVHkbS7ekan0htc-6r1AQxIQ1l0cnw-k4YLKFX5Ytyip2Gm1ve55pZL5WTraBJJbt-XcUUE9LSWkiicTDF7gQiO4F4RmB6cQXTZKfkb86I-qrBwVga78RV6HEVMngFN0fBcEBu7FMJi5pmauXMi8lLgkhVqXpOsEeBM7VlU5V-amDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لغو اجباری جانفدا در خیابان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462781" target="_blank">📅 13:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKfwF3DSMs8YmQ8Y3JIHps1O3rFmKDAtGrBZjbF0IJhFVeOUaQWaqbV1nWF2TCUVb60YxdSKD-_wcNQHDuaB723aUVymo-TevzreGFjt_FfBcCJkmdz6R7qgel5jxMQVY7UNp_tcsEmFA_S92lQmrhQTHfGiykISXjjzTkwTeugLgygv5gdstGa0MD-miibNARlh9hbAQA1OWZrgKHGA-RA20O_Phc3leAaNEFZORPd-SZXtf16g4QdTHTDV6hUJey64Kv8oi4xoMaSd3_E4MQRR-iPjdGNR25QO6UhOzFNHWtan-ipK-iOS0NpDFdjMzzhRJI2-qRV8sxXgtDphug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون حقوقی وزارت خارجه: آمریکا نمی‌تواند با خروج از شورای حقوق بشر از جنایت خود در میناب و لامرد فرار کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462780" target="_blank">📅 13:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94906501b5.mp4?token=J7A5YGDAUACVmYKtWKUtfghLaoCbBNG5LoNO0q_iBU62X4xC1VKj-MRvBY1NVWQxmhcsd-z4HnELmWjO8fujAPOti3nTSgnIQMd4hpHX7d7fMDujF92o2_eLUofhCJg3r8XYv3WLTIACboli0d98LBjUwxU3tix7kmHcJhzkeT6IQX2tyxP5mL7dL0WHvrH3JiZqsYa8qFNjXCk-i2ramqGa4aztqC33oGlg_vlFMaHqEwDzGzctit3VO7tdEAZwxUgIXpDRzfMDFJs5Lid8K3TELT_XlAoa_JeECRc50INPk9oeh2MXprDQXLz8lGbZFgsnEtH7YQYDheLIagavww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94906501b5.mp4?token=J7A5YGDAUACVmYKtWKUtfghLaoCbBNG5LoNO0q_iBU62X4xC1VKj-MRvBY1NVWQxmhcsd-z4HnELmWjO8fujAPOti3nTSgnIQMd4hpHX7d7fMDujF92o2_eLUofhCJg3r8XYv3WLTIACboli0d98LBjUwxU3tix7kmHcJhzkeT6IQX2tyxP5mL7dL0WHvrH3JiZqsYa8qFNjXCk-i2ramqGa4aztqC33oGlg_vlFMaHqEwDzGzctit3VO7tdEAZwxUgIXpDRzfMDFJs5Lid8K3TELT_XlAoa_JeECRc50INPk9oeh2MXprDQXLz8lGbZFgsnEtH7YQYDheLIagavww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلبه چوبی، پوشش قاچاق ۸۳ کیلویی مواد مخدر شد
🔹
ماموران گمرک مرزی پس‌از مشکوک‌شدن به یک محمولۀ کلبۀ چوبی که درحال عبور از مرز ایران به‌سمت ترکیه بود، آن را توقیف کردند.
ماموران با بازرسی این کلبۀ چوبی موفق به ضبط ۸۳ کیلوگرم مواد مخدر شامل تعداد ۱۶۴ بسته انواع ماده مخدر گل و حشیش شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462779" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bttvwbcaE6kwPLbcD7fZyD-5uIKMEmL4-BLnEvYGdq90X7BgCmAcs6EeyyrahY6AyeqdQ2aewQmmIl_8uyG5DIfqFJWY3vO7Sktu6QeIVwMq5mCVRNEO1qe9oGj813nQieYp2Ov9ZxTvm3PJxonqiuBKhPKxAqlG8pG3yEWG5eKdYnakH5kC8M7baU7pBuYKsLn1BZjJgMTs-lNDxYrnhvkzEEwqPfEOqLtnFN_5QfpPPBoGDrsZICmhvnAJDYyuxSMZtDKOr61qTO8_FFODeR3OrmqayUkSWB9io0zqspiIPTRksHDYxvE3OSzxYxvXauXyu2QgAW4DYzkG7Ec6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان از ترس یمن دست به دامن چین و ایران شد
🔹
مطابق گزارش رویترز، عربستانی‌ها پس‌از ناامیدی از  کمک آمریکا برای مقابله با پیشروی نیروهای انصارالله در یمن، حالا دست به دامن چین و ایران شده‌اند.
🔹
رویترز نوشته عربستان سعودی از چین خواسته از مقامات ایرانی بخواهد که تهران از نفوذ خود برای کاستن از شدت حملات و پیشروی نیروهای یمنی استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462778" target="_blank">📅 12:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsw34JQx5NDHLc1326m8kkaAK7XnOLPLBmxTlJdtaRlh3xSWO078Knzzxpdj45a5NEV8ZglH67VK-jyrUGy0gOzY6WgddXukmwEwWfh9YDdFmw961k2AejcncQDRfpqovVhJe9dSktUaz38DBIUzL2POMx38-acZz2b_q8fDduDXIZnGwtqdxMTQfp56Ka1dUY-qgqO7KygDr5TCFFtFvjHjsy8QLosMdE5cvlAM02IfMUbAPpaY93VgK_Q80EmF8k1qGdLD9NzFgIpnv7FpfjffukSd8QQK8gRlNi_cFjOfRDo6PSazCvFmXVUYVkp5b0d1YZ3sIDbR06Po9lW3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال ایران با پیروزی مقابل بحرین به نیمه‌نهایی بازی‌های آسیایی ناگویا صعود کرد
🏀
ایران ۷۹ - ۷۴ بحرین @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462777" target="_blank">📅 12:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd3063f18.mp4?token=JMnE6HW-qEs1L-JmVj2rG2Zq_zGpIHuPrKXE9JpFGEvdUbiIW9SJFEN-E2kvg-uJDyeHHGK-phHX1dWBfPcSWZwQh7RIa35fSvt71zOLbtm2-38eEdrUcj7H7NrFRr0-0-oItsHHDoINjlO-W1hQxMUprkb_Gal90PRvpdQfsfqVVQAtaKz6UCgINYmk1Hytf09wvzL1qHoPcCIfqw-IVGf0TEjGE818GsgVI8WzT54QaSStBDOXNOPDBZyv5EzNeFGt3MpXblDAPRSDXZgtyIYR5WeXGMMCXTPM1Xr7E4F_QvaiTim3A5JM67aOnYZ4AoF-N3hiN_DG7k_GAc8Yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd3063f18.mp4?token=JMnE6HW-qEs1L-JmVj2rG2Zq_zGpIHuPrKXE9JpFGEvdUbiIW9SJFEN-E2kvg-uJDyeHHGK-phHX1dWBfPcSWZwQh7RIa35fSvt71zOLbtm2-38eEdrUcj7H7NrFRr0-0-oItsHHDoINjlO-W1hQxMUprkb_Gal90PRvpdQfsfqVVQAtaKz6UCgINYmk1Hytf09wvzL1qHoPcCIfqw-IVGf0TEjGE818GsgVI8WzT54QaSStBDOXNOPDBZyv5EzNeFGt3MpXblDAPRSDXZgtyIYR5WeXGMMCXTPM1Xr7E4F_QvaiTim3A5JM67aOnYZ4AoF-N3hiN_DG7k_GAc8Yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژه داش‌مشتی‌های جان‌فدای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462776" target="_blank">📅 12:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c114b1bd47.mp4?token=Gs4K7LNvr4S4n3eniriwXOQd7TY88Gp6mgZAGSw_bxsgizE3DByppLZU3ZWW7Be6Ds6WBza6KKpHCLlt-DTSfKiuePuIq9_smTU_tSL__QzHsZDNBPdNFH8WhY-nYW8CfDEHGuqd8YH0d_7zhzowD4hvwLvaBHFeln7ZZjraanzduDto_Fz7BMbgU2wEXcNlnKnBDq6C9UEIFT_lEb5EbsmVawTH0Ee_7iYRDSEMGsQumqwJOPNrZ-2KL49yHXUuLuccjSGBaqb78WyBY9UDU5pKx4cqjWwHQXFoz4NLEc4mC47ySVJ8maNfHThoQB6Y3TFRJhvP77944zZB4cTq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c114b1bd47.mp4?token=Gs4K7LNvr4S4n3eniriwXOQd7TY88Gp6mgZAGSw_bxsgizE3DByppLZU3ZWW7Be6Ds6WBza6KKpHCLlt-DTSfKiuePuIq9_smTU_tSL__QzHsZDNBPdNFH8WhY-nYW8CfDEHGuqd8YH0d_7zhzowD4hvwLvaBHFeln7ZZjraanzduDto_Fz7BMbgU2wEXcNlnKnBDq6C9UEIFT_lEb5EbsmVawTH0Ee_7iYRDSEMGsQumqwJOPNrZ-2KL49yHXUuLuccjSGBaqb78WyBY9UDU5pKx4cqjWwHQXFoz4NLEc4mC47ySVJ8maNfHThoQB6Y3TFRJhvP77944zZB4cTq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش تماشایی جان‌فدایان ایران در پایتخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462775" target="_blank">📅 11:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73d5f49b2.mp4?token=XbRAd17o08JlXaDWv5KuBGRWlcoiir3ufbEGsrbsEgSzRCN9bOcuJI6LE4hfpfPUS8LC8mAPmmEAUvXTiQRUx_ghnOmcLsGKJbd1FX6_v1rVkwDpwVIcrF78yDrhAyKCbhsD_cKcJ0J0RgEb8IfuTA9NlvT4e8dxLi0WsFxPEe9nd2dDAY4AyKMJVfa-9YEDD9UtysD9FDHQvHoTnO2PRoIXeqUYFd_bMRKylVurSS8lxA-WQZ5ctnjPEsawui-nXqb_P16rn5M1cdNXE4wYC9w67M6p1hALX0BXXQLaRwCc1ndymKAPnljQLJZaa8dk2Nfl9fMwtz7HTfLjkiX1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73d5f49b2.mp4?token=XbRAd17o08JlXaDWv5KuBGRWlcoiir3ufbEGsrbsEgSzRCN9bOcuJI6LE4hfpfPUS8LC8mAPmmEAUvXTiQRUx_ghnOmcLsGKJbd1FX6_v1rVkwDpwVIcrF78yDrhAyKCbhsD_cKcJ0J0RgEb8IfuTA9NlvT4e8dxLi0WsFxPEe9nd2dDAY4AyKMJVfa-9YEDD9UtysD9FDHQvHoTnO2PRoIXeqUYFd_bMRKylVurSS8lxA-WQZ5ctnjPEsawui-nXqb_P16rn5M1cdNXE4wYC9w67M6p1hALX0BXXQLaRwCc1ndymKAPnljQLJZaa8dk2Nfl9fMwtz7HTfLjkiX1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462774" target="_blank">📅 11:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDb_ilFJ_UJFfpOnVB7hkbBCC-VWrrnma3ejQELEDBSTgWHSRaW5lv0UKjbIOldjpNbi7CynLwwjqDClySvu8HVsP55OhJqy-nfrfvKvXJIPiOkCSDOMf_V4T3TpNNEmLU--TJ1rKyewvpORFLKrPSXF3Rw7W6S9j8B77egGAw24glJ9zIde4-nT9aszbUIBuPDaEw53bwaJV0TFO4hp-L6dK3Krm73Yg0yhKjLkc6BMu2_bh_vMQwfLAl9oCBtlQc7WZEroBBd_5WEWb6GLulPfQE1Jn85PVTxBtN8JVhcZKFBuQbfzFW0cQ0dD8yVT0cBDtVsKXXMqJTYda0j2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg-Oc0T0_MVX0qz6FccpYMbzovEhr4XD5kuQLbpIsvFrmD0V2KM8jVkxhp2MoG7Nfc_6DC5mV42aOD20XmBt4uR1ohJGg4H2ccQjMGAr0OOzsxb66sVg142d6uGr67FbHGNhn1Wv8f8tby6jhwMKbq3fafM_7spg3v6CO1QOg1UgINioyM97evkEQXw3GHLinv44JM5xDQlMS2rs1PjRJwLTUtOzBxvUq-f03sN7Wum5FpT7E7ua824iL2VyRCi1ExyOR6gOs0lYsi_Wl7MahMxTxgGxkTVqJK1QoyCjHJrEP-G1DqAr_ELUsgBmkKvkmpxNAEBl1P-ceVNamufYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFOCLJWvBlkldq-iyNCgHPQenB0y8Cpr31ToAi9AVYfLHGi01XB41TdAiQRrRwaKA44PsEBTw_HRU_6xTpUMXtt1OKNpFWq0c90Zw2eeR-7d-F6ROCCi3d737iFlMRUoJ8KFNWm-LSi9-0rDcfU3p_k4_wtHjgp_UKOZrALyqVs1MjhSLMmuMPotKY_dEnhPgFTya4kBo4gqe2izln7m5rl-xf5A2qZCOigKPoDTz6yGJr_v3ce4wtvpbMXtS5iQ5nZcvm8H_XQ2Sj1-KEG3NvRW1n-OsIJj4LS_H0TegXhgY6GAuf4qjLVEH1wRA-rJPbLN3YUgK252FFIceUzaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4n5FL4R456jXlUXHVtMgCsEtVi6kDaoKYp-Mi-zVys0hjgEjtpZabiMBgSO3Gh359o2vsyQjZUmCaIHKAEgG8QibObI_cLDrJgDObBG9kf3cnONRc0ItNEe92Z0dqWVYWP7yCVq8Wtj1xArnZmf-cRhlRSeohogcV1Qd_ILpcXS2cWbSdiRLnLamYWgEah_mgNeJsXr03ZWrX6_pkhNW2XCYLq9J-dizs8d7M97jOwzDDaqh2dlf8OokATZcqLOE3mWhSV1c4PJaMs-sMxqhpg35dbZK8uAP-okO4BU_6fVzfp3v7hvJafk1AzRsp70vt2bMNdOdyTFnOaa_2Jvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNh7z3-bj9MNyXwbUmFLwMsxypBo9OrXsJDzHsAbjj2SKORf5c9dnWDQmo70I6uP2QQ0sVnyxw7ESvoVlU9wqMQsl5k20f4gI-WEwydEfWMhugEnYVhAxmwAZ6ungYIhy-FgNIhzEd2SPl7WJRsUp1cutkXsbrdEOcfGXXOD2-wR6RRZx29GBTV7orNiciO1oXRgpGy5Y3ShHlZmKwB6RHHebHv0ifZuLHs5_agRGVqTF4hONR7w03yCWrSQy36X0Dic5EFVQ6D42yerUwnjGxrUKYr0gX7OkBNF-V1UTjBkktAdjya3B6LK4p0PMxeqikxvv0c4vu_ODWMBf7KuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2bMtsGQ_qYS3_z1LJu4unnTz7CSp7cK8_qj_eBg3oOSMpHYb6i0ek-kPI_UYUmk8WtBVt2IyWLkRBHZQNXcaKFkhX_zwijdod02-PiJfGudLRf5wC6Ri6K_4E8-aIuNzojmmv6sWdzI2Xqnfny9ogi6_ZjoYEtLOnfOs7IQmNb5i3R2ByY1lm4wG8Qgeay2M_pSOBOH6v9OZ_fPaEeZF6ROVSF9OdqixiqdGw76H1k4Tlk9Wc2BjolUI3iM1RFIp9Mu18m_qVSyIZ6Jw_GA7IfLUEr4_c9q21DZr1JWRPx6CXRXBHPXifANhyndMP0qA0LkguzsN_IY6mrS9e8mVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAVedQrs1YlafVkumVVYpMVqO5HTwYlzxdYODIvwKtdD01bl-PkQGSBdiUSnvii7mJvnbuEqQBscVGraf5YKz0wZWPNPM_BBRqJXbGcg_3FcF6dThfrUN81ezUqTEQ2G-4E2BgKMDKhH7qwDzjEaAaoZBL0EFVdtxXRLn_KF_0kKjHPvfxswi2hd9skCiXgpHGtuagPto4o8HsqkOJOmy20sPYkZyar1jFVSEhWHdZuWxBf-sP3fx7yisyFwv6FPR2bk3odGfzoKB5hL0bk4dRzGZVV9JiDyspf5wjruyntw_YUgJszGNYExVHBHwpbWXdPsyHYZrln_JJZfCMr91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDlAtD7RWbQZzdW_h1fZU_E7vsDyJVFnyn0RS12oB-aQSkAd5bvkns08UP0b8M9SsBiogxooyxj2zOErQTinKgk9qEuXhG-2jhLGT0uUwHSU0r-2UnftuU2vh9vKE_nKvg8ja9TGipCeoea3e0XmUCJg4BPR3SBM1El98RcfxU1s95PWVw27AJZ32V86K-peIfEhhpc5PiOYo3yAyHfbGJ9eThHK_sAAHP_Y2sjIk45ObiydJihpvwtD3qy0dgQWAcni9x2MWoddbKjBcGFedIGeEwJEkjYWit2nOUCp_2teJCpQFu2VQzZ7PZpgKc8pvbidT-Chc1IBSj6kVL8yVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۳۱۳ هزار جان‌فدا در قلب تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/462766" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbjR5I7rw35SEeQ7bVpkZhmCLunjC-x2nmZLIHrcuzVFAHjSPlWljmbTrqOjmY85onVjyA819pZXVrm1e534EkdXG6uzCU78tBwgCOgM4xvbMROIx2MEkWW8oU2aQz5UBeABXYqZcSB43IZbO0S5sAhR55xYYojXz5n81zMP3jIQpAwJ4Mnff-rFzlbcD94g6-oBsYEFM4tAV4zY4JV6un7Ka8Jh97Qugsi-f3oX5FFpKsdFEofmVoytvLFvDV9D94y_ysuqdPcWf1ulUHddw20mgrMO7biNaS-45iI4xfCItWF23MLG0oXdcWBlvixUW1QnmPhbtdlANBBkONo2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462765" target="_blank">📅 11:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d896b9322e.mp4?token=n4GWvEN4Go6lp1W_3KJoY4X5CSpaYeHEGc_DF0bcJ5uP8IJFgwzvygKuB0cbLS3StORB5MHaA0VDsCTh6xIsjvgTSP33q_QHpyqMoAFgH6qwMwQ1lEFwNxznNdFJH7N3EWF9pplGTjiPzD2EH6zaKPj50HfEefNOZf3QfQxCvkkD5iI9qC2go0Ota50qTFbZ5oSIAV5vzkFn2JKe2HAdJUpEXQW77mAshWqObsweRmU_6X87GjuQJH8AbARhs0Q3NuzK0gsUWlEclJl-JCpKt6PT09bjstT7fI45_IPEzP6-MX5T85CD8IFwk8ZMbAQrMKiUOUdzZnrgBCpq_44eGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d896b9322e.mp4?token=n4GWvEN4Go6lp1W_3KJoY4X5CSpaYeHEGc_DF0bcJ5uP8IJFgwzvygKuB0cbLS3StORB5MHaA0VDsCTh6xIsjvgTSP33q_QHpyqMoAFgH6qwMwQ1lEFwNxznNdFJH7N3EWF9pplGTjiPzD2EH6zaKPj50HfEefNOZf3QfQxCvkkD5iI9qC2go0Ota50qTFbZ5oSIAV5vzkFn2JKe2HAdJUpEXQW77mAshWqObsweRmU_6X87GjuQJH8AbARhs0Q3NuzK0gsUWlEclJl-JCpKt6PT09bjstT7fI45_IPEzP6-MX5T85CD8IFwk8ZMbAQrMKiUOUdzZnrgBCpq_44eGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجویان علوم‌پزشکی با عکس‌های هم‌کلاسی‌های شهیدشان در رزمایش جان‌فدا حاضر شدند
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462764" target="_blank">📅 10:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNFRHZfuhIHwgSnEhHdpjnBuqN7YkXLI7y0dbcbPM8aCm_RFCRKUkVo6GZEsD7nzZvDnTzSZo6Q_woKxqjc1h2KSDvIr0ExAV4y5BPf1JtDlDz2TzKPZgDTBm2SOR2h0-023qjAnsb1dcCHVEsVeBaWzqEMoviRmOWvarr3CnPg86YhFCfpPbibq2Dawur15Sb4cVrS1V0aKgNx-dXw6DXOV93Vbf6Jf1TLrV2-SDU1nxeQZL2aAH2udbUF2bM_tP-l0m66Pbbx_P4YAKYYyEW_GaDLqMylGa4g0bPiw8RjLW_sh2r31AQpq2278WZrQlxZLJj0ff_D4lU0KI6EAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هلاکت ۲ تروریست در درگیری مسلحانه در زاهدان
🔹
بامداد امروز نیرو‌های قرارگاه قدس نیروی زمینی سپاه حین گشت‌زنی در محدوده خیابان دانشگاه زاهدان، به یک دستگاه خودروی سواری مشکوک و با آنها درگیر شدند.
🔹
در جریان این درگیری ۲ نفر از تروریست‌های مسلح کشته شدند و یک نفر از آن‌ها دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462763" target="_blank">📅 10:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7c004397.mp4?token=VDvB2aZXRokrUDqS0yGaPCnVFNpX25FW8iBbwxqlO0OrHd9zoAdseo-JjD6shm4p__qg_acrr9fk9r0NraUz919xAvJZpuXeYE9JOyCYzNAqkpqFBnVrHXcbos0IGFksd5yBzWYshXgf-f5lHMKbjbvWMrwzox_vyaadlXUjEsI_yJZ7BiC1eCCMaXpoW2gqGr7-DZFQra-yKKTNTTUfuqejMc56Rk2upOfqP3369K3GrGbCbX_PTe7ECKsW0NZBS67uZQNKF_C244yIcwP7uyI1K_HbcsAXpuAZggLIDc1ON2LJ1nTkUHijKJR01AePLvt5vMXQ1LiYmBNKG873UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7c004397.mp4?token=VDvB2aZXRokrUDqS0yGaPCnVFNpX25FW8iBbwxqlO0OrHd9zoAdseo-JjD6shm4p__qg_acrr9fk9r0NraUz919xAvJZpuXeYE9JOyCYzNAqkpqFBnVrHXcbos0IGFksd5yBzWYshXgf-f5lHMKbjbvWMrwzox_vyaadlXUjEsI_yJZ7BiC1eCCMaXpoW2gqGr7-DZFQra-yKKTNTTUfuqejMc56Rk2upOfqP3369K3GrGbCbX_PTe7ECKsW0NZBS67uZQNKF_C244yIcwP7uyI1K_HbcsAXpuAZggLIDc1ON2LJ1nTkUHijKJR01AePLvt5vMXQ1LiYmBNKG873UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه حضور مردم در رزمایش جان‌فدایان میهن
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462762" target="_blank">📅 10:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad65eba82.mov?token=dgiJHZxp78G-JbeqpodNI2PcVO-SafCp8cFYbavvxEJsy7nF9MVNWeNjFRRXyU3WYtFXopCXhnDosYuqyqHEg-ZdpTtU04g33nDFVLmZvTKWbVdvGWCfKkyZJVG80kHtiigSYHvs8IOMe_nvoczWEipBSogdPuenWqiXyMO_JMEdhsFg1rKm7t_knv2UynhJIsZyBZqAbwkADMDAd_1SPJiFE0Zh3WgteuMVLdC7ZkuaoX0OQHIdC37_UCEmDD1T9bCgdUh2Y4OgQ-A3pztT3oYh1AmKgjUP0Iy_Katb1gnecZRf_fgN4UbIGtsaCKtm8qYia85OPLlvw9LX9S1EiDE2jAT1AmaXiwtaGtWKaJdMPrvTXXirA2dMreF4YYZb-ng6RPaNY7RWZICoRvhsfcEfJgVCloSFpkZBSE14wERc9zHOvYfOOsZpo-kEE_NWk6DcpqMEac_z01AIETb8f8O3mIKd9dZVXkMuDRTnYU_zhtBoaOXRXbvq-TFeXipIm6YwBZPs2mLaHfeWbSeU0mDFPZ9Ols0XTTwwdYxop1bRi-anJF02M2hOfcBInIwZrsd01IoqlUHC1Oc5J0x1qnYR0yId9IK7OdOrJtg1dIjDtOEQDh2T5H2_KQKZvCbt6ejIuvSrAhqiZbn-Y0cpbGBcOxYhrLF028HkidHAp08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad65eba82.mov?token=dgiJHZxp78G-JbeqpodNI2PcVO-SafCp8cFYbavvxEJsy7nF9MVNWeNjFRRXyU3WYtFXopCXhnDosYuqyqHEg-ZdpTtU04g33nDFVLmZvTKWbVdvGWCfKkyZJVG80kHtiigSYHvs8IOMe_nvoczWEipBSogdPuenWqiXyMO_JMEdhsFg1rKm7t_knv2UynhJIsZyBZqAbwkADMDAd_1SPJiFE0Zh3WgteuMVLdC7ZkuaoX0OQHIdC37_UCEmDD1T9bCgdUh2Y4OgQ-A3pztT3oYh1AmKgjUP0Iy_Katb1gnecZRf_fgN4UbIGtsaCKtm8qYia85OPLlvw9LX9S1EiDE2jAT1AmaXiwtaGtWKaJdMPrvTXXirA2dMreF4YYZb-ng6RPaNY7RWZICoRvhsfcEfJgVCloSFpkZBSE14wERc9zHOvYfOOsZpo-kEE_NWk6DcpqMEac_z01AIETb8f8O3mIKd9dZVXkMuDRTnYU_zhtBoaOXRXbvq-TFeXipIm6YwBZPs2mLaHfeWbSeU0mDFPZ9Ols0XTTwwdYxop1bRi-anJF02M2hOfcBInIwZrsd01IoqlUHC1Oc5J0x1qnYR0yId9IK7OdOrJtg1dIjDtOEQDh2T5H2_KQKZvCbt6ejIuvSrAhqiZbn-Y0cpbGBcOxYhrLF028HkidHAp08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در رژۀ جان‌فدایان ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462760" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462759">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b0c9915.mp4?token=rGYvBCEx3NGFfoODpOBKNAbzsHV-ZOHhH8Iz0-DrGsFi069DnFUncJ1NR4G1IM-8VQRQbR8mIXpQGCqOc9hN4vtxugXjmXZkv851DU43U6DZy7dfKqH5wZnOnYARFPpB2ymN5KpDlCymljsUZc_vjGMTfw9a2xZboCq4VQ7308ZRZ9X9Y82EnQMvmv-TMWPs4B-hodHTn8b-Taf3qnWGG0vEIJxazLhnX1ShdFe7JfkLaq7HdWiIW-xJjz1BayvYayPVxwhIkfEST6Jh1dJKvL_N_X20Qo_2kJ3_yw5Yo26X6F47AvLU2dfnfIOMzjHjWk6Eh0Z0CHA7ykwoi58s0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b0c9915.mp4?token=rGYvBCEx3NGFfoODpOBKNAbzsHV-ZOHhH8Iz0-DrGsFi069DnFUncJ1NR4G1IM-8VQRQbR8mIXpQGCqOc9hN4vtxugXjmXZkv851DU43U6DZy7dfKqH5wZnOnYARFPpB2ymN5KpDlCymljsUZc_vjGMTfw9a2xZboCq4VQ7308ZRZ9X9Y82EnQMvmv-TMWPs4B-hodHTn8b-Taf3qnWGG0vEIJxazLhnX1ShdFe7JfkLaq7HdWiIW-xJjz1BayvYayPVxwhIkfEST6Jh1dJKvL_N_X20Qo_2kJ3_yw5Yo26X6F47AvLU2dfnfIOMzjHjWk6Eh0Z0CHA7ykwoi58s0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای لشکر صاحب‌زمان(عج) آماده‌ باش
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462759" target="_blank">📅 09:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adwx7rfTpIpzAL6jj91sU9a0CxcdflX4IBpnh3V2ayX87412_kQ7xzB4F3Kwh5qfEei8-UdnGh4UhAUqpI3I12gkCi4MmPl4omL7_9fs7utz7r9GnwUEYKOc6UIvaKz30PV2ABTi27vSTe_-mBUyJb2a4S97tlUe1Fcd4_I_EutwBLO28ayPZT6zlTRVcmpyLejPg1P5YJDXEc2Gz_2xc3AtVvkIizyVpVA12uFeQO--Z9fKguhi3LT2mfm-ZbTP_40z2jbdh5k1931i1A97KwBThVBSMtG5_Sxlpg-7ppQAzLpQegJRcXis5ukPJjS0Y7yTKnE2-Ih0padBrs9Acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chGjv6YWFaHXS_zhXC8xom9jCy7hTAqLoR3J9ejqPklzR1YA1BmAAl8DfWBS9OnV5UmsdQ9KhxAQ1chvbZdqoyEzJMiZRLE-IEyeYNGivZhSxiUCQgZKAxT4M1RhEhCymaLroXB8xZVWb2xryrjzOaBA95dISgqoymk-tHtoHJDTcrc2MSPqPAOAy1wXyptecVj9yP6kcc8nRH7DGtwExMqxgEUYH0ua1UkFZfrvJJJpEixCbWc6pWNlfdpPGz_xdQXEvC-xqu-Y3LsAq1FsvRrC9e6Ufxh-6LJlIVNjBKRasrj75LyL4sJdgQZAzuqDLLmlAqVwUSLptRVliORHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaqAHNwlHt4o1nGUR3kQYsYKhuJRM-TiC_OkZvi08w4C3YSeB4JQMMYzSVwOdNAf_tzK4AZnkkbPc_x85dOmMtuqTtM1rMbjTXei5d2rr0byQi2LMl9kXAwk6NkL91mTlycMsFV8GR6bUP5rynnjfECPNo9Yil3p6kAHntjuWCMxcNiJo4QroDTFkhsMA6gFUO5_e0WiYC3oGZGuhba9Lw0Y_99L7foy27W5xXWLlESmYI8lA4MX0VgZRxbmxdd90_cujrI86a-I6S_ImQF2IciLgdxF3sOXkzX96MjNuk5Mc1g1KCjzMw7zPbaNlgGJKdDCg3r0N7BVjl-ifaEk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDF5lBYm1yYbOiDOefOFgNwJPFeGruUwV4-gFGn8SvraMegQNFLqPY_KWBdPMc9gUEm4hrAf6ECJDjsu_bNOuxoGFUTowCP0buR0zNp2pAaz3Uz8b3nnqr_Wi8ddRQmhSmoElQuzu-WB7jELJfSHdNdOKvZFvckPSH5oHWm7Qq7R0zRX9aKzdO6fttKP6QzngvQh7HUqR6ZbWD-07XsIkB1jJXvtNz9gEPOY3xrm0kFmSob55zpvtBbU3wSlQ8BnVDknQzS7t6J67FmKkilGFkPeZMYoSrUXulsn8VHNcmIZw_nB4CvW7oQrkx4etQnDXhu6TcDnssUFTlOcUDp_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ71W60lEVylzBGeJ3zZg_LWvSsUcfhax-5CPJbRUmzngjDQsxUgAEVNFOqKLBNRUwYbORG-xnszuaYCaMpDomLW84Ga_XmA20ceT_Mnllmi6CVIn0GmkdI-_2O2HMRQJCBef0USD9PB2BeQxGNzvWjIL-BSmc3L7uZOfCMT5P3gJG46g7dyjcAmD2sNmUfVa10ApTR_oLg7Ig1US3hKi5HlRe0ho4Ea7WsEzMhbaANq5KY0I7AyYkC-xsYCqO_sfu2-_APk6PCL_-sbhtiGX8lBM-a8fPyZ5FN7AGN3hAajV3TbPkbwrNLShLpogbHCeyLrx484_bV4OdDOSl6o5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXVKlgVgqxvQ0WY8u5-N_1EKaOlQRPZNiAulpkF0l8OdFHFiH_tlETBcyqmWKgLFb_m_xY1TVXkVGN7S_oWxprkRhkTBq0cfJfeM-h1VMFMn3mWt8a6HpZ6dSygW0Hanls1tabDVZBDs-Go-oEHSJYglJE-dwjlK7iIvmvwwb4Zx3yrpI5exILUaJ-5VxAQi9W_uAzLlV_w9L06WF6YS1W4jZiZHUHFnvH4YuS6g8pD-I779ajv-fpNtxVhYH2qqutqxXJ7PJ2YkqDVn5YM07_Ck4TvRnNvevM7QgPF-fQIFQEz2-2-Mp9dlOVy2EyusS2H4CK535ez9Q_VxnwNKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCCMZW616vhmx94574kEQALYFrLXyNiRnOeCLCIZxvhocxleLlBcKhGL51vqG4Qtg-A2EQAfnrZvkjgKSPJzIhVQuToUIh243QeTkszNsQ8qdMMeMF5WMdTZ2M37gWVYITngccXMu5NdtT3oZOlj7rLft_TmuFNU5VCiNw28Fp-u4O7D-qDWzyqmuIkw8a1Ddp2iCQQyBV416mkyE8ZCLzGWemqNwvww2diHuuFYc9C8_54x_nyfutolG6bZm3GK1QJfhOmc8Y0KBPKfyDO002iiMvDRkZHp_e8RrNdAYL6aFBfHLbGvsDt5XQal6b6QmFnCjenLAKWjsz1g_3uwlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جان‌فدایان بی‌شمار ایران امروز لرزه بر تن دشمن انداختند
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462752" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJpO6ev-iWI3mzkobXexB8mDUgkgnB5UrA_arDvLfq6-frr_bxY1SWFwPa2DpXWnJ7IwAGZpLhyABN8z0kqcICC1kpH-tZuLJaZvqDAO3WDb78hIou8qNn0BWLxEcoj3YTJEft_sGvr7g8Z9b1nyO_Vhjzg3mQTKQ13tEjseXsHJW5fHFuV_oVDf9c_N4WyWXnDaZTIr4V6LBmoKCK9CYB7vDjvDW-DhamhGp9USdekmI-9f0X2u6gjyORte_OdKPJZ3QQpkrCy1Nq3SiOAFUMSaT4dNTDn1Bh-wovA1iY60jok8VCNMnQ2YxzWaPCkMVpbF02f_lzPN9SHOW9UNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462751" target="_blank">📅 09:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462744">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXTquW4UX5j3G7YOat8VcR-bTgRiOlhrUbHlmFf64-_x4fyW_omYVgD-Vio3A-c3Ysk-EYvBibqERD9r95792_Ac6W79cHB0nCN7Nfv-fKdt-l9WEV4QZXm6p79TBEOEzjhJ8CBaYIecVAaVVmtqoLD-iW_fJScZWaVtfTI9LoeH_lH6fMuLcgvKMWW8p_HCNNteSxGGZcEyhnaYrFKHETS4OoP_WMDFOuc_eXrXLuxev-wJrD_Rf4-yCvnh0s-yi7kzozUIwkBPl52f9SjJC-0YCogFjDhECr_fqayX8lw3nn-dg4tygocdq76-zUWRrUH7lLjnLQpqhYjUzYjYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjOM3bpGnPkgIQi8RspIZbWHHPUJwC2E594J31WyEzV3j2EjuEN0wnzInQyI5uouvL3Dfgch1Ebm7wEfyP2mLIF6kIVY_qfQ6azKAltX3oiEqMV4joK-e_CanGDZuI6g6tCbH3da0C9hS1DYq8jF_s5EdJwbDQ8G9Uvfeqb1Ua2mIrl_wj8qCIP3Z63qNN58nrKROXqN3jbggnw0Vw_rerV3Oli1XS_J7Dz0y_tbC3yof-xGsL5qvjTu1Sc-FRcO1YiaUo0yBipLTnUuy16RK64h0mkPB-VPkGhZx15pAs1MIuZ81lc2oe_JAXUwxxo3Td_N7JzREigC_Ny7ggNddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAJOdqME4wTaYl4q30WKiJz6OcLF5KDPUYsNVd_D6qGnBWuF2btgBj8P6BrYwOOW02W7Vq4bI8rw7MeVQlQtTsHfabSKpte99uRWaV_TXX30U5B_PXXFyUZ2J2LULCZG78o3O5A8FBP5HtGEFi9IiBC2Ubyho8r0gvzCqNh-1ZwiSRz0D8YvldqJdnm73izJTpRy_NF8f5lqLYuj2hNqYha5POxwyg31xRbeuDK7qbjXHnzAHDUI6xmIM9VroBxa2z3jbx9rSPZ-Kaxw1O8xblAl-SPX0j3oBEyaj1FQn8uC7xcnx_XSlvXFdDRgtz1RURYAdjNObub7imc735wpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnDgYnMAchdmsEIRwwXV0LiAEWpuNbpxABSE0m2sh6BBD0A-bzReCPdTF-ZOqLwo57gWg2CEOKp_rNNzW7ugfFRSp4M4_JdSWkWJfkeG6ejweyEbDh8OPtTqFUYwdyPCkEXhUH7wLqAinfylhfcEP6GuBLkSYSJ3XPSywV_u0qOD6UYX4_50qB43mO776ZLn8wpEzyabhSrfxPs19HuX7b8kUU-7zDib3gFQSUPflHp_VWUuU0ruocbrs4zV7oQxKtWvdJRJJtCnrtV_K6Wff4w6I9B76gUEg5yuFbYv-UY5YD3RrECQr22OYwQCv9QlbXZ8jy2XiYjCy4mMIdyrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Af0MNDgYJSS4KxcaOPFGkyp0KBvOLZWdYb_UjQFFXvqsx3VKpFtr8U8pX0QLQhf6IuN1JEcFECw30nnqXErj8fZyRnGilqR27mNDK3VeozJAyE87fpNuaEbCrJu9jw5ifBEuR7F8T5ZJllmlF9sy8xMPq_KupsUx5T1VSIg7j9SG8Oe42dROBPBsutX2zVgUyAQVIBruAqSRP-pWjlMRufm1oJM6I-JLCV5rQMilMMeRktgmOLpNZ8kxF8Nk8oXxjTyKp4E0j1Q8U-zxvjUJXGcfr-01DBSiZPPAR5BkSAnQpZrByiv6IzM04BFr75WQ90doljLzBL3-1N-u1Bq_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXIayvGqTYRkXkMX-73WPKQxV5UIW28GgrIRdHF9qg9HErvwAtrbfXWBceyKKvE1PBYJORRjk7p52x2JNcMFfcmSVKrJaLB5hhIqiRZTW4oCAWBVLMPcLlki_j8Uen-Ph3tb7cSwAVvcX7vT8nzpCseZCfRUnAsa1OrJYKbDcOib_DnstnPKcAerJucZ3Wwtj1FF53_ERp1ZXKV-7Ro3RhlWvsn7NBo2pinod6Kd-0tGCbZxbKrxWdF_Rhl_updyQ0oVO9GEMhwvHfC3XARldgaWoI2On-TIpu3U4NZGFtwHWkE0G6bxjhPNy6_XXwpJTirnIbBEMhkw9SPJD4fkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlGdVzvdyVl8hmhJOKG1J5mLnf1HslTxK2X6G_EDiaObkuHHtnr8BFg3tsJZ_1zhw01gDO8u3V94nY_h0pgcWMIaqRjjz_pptM2dct8ucx9YsSnL3rqp7ssTELNKSuy9_SGJBEul5VSJaHEmyiuHhlMpu67goXQhnPNFjsldjYoc_9OjYxW_oOoNRjT-tjPQiqTcU6HVLOGhVOjlILz3d3JbqJXzhLFa-0vtsXk3hkMUFIDRMYPVoScLeIx_GbNs6RA7AXhZmJigyeMhgcZ8jAK6kxsIJXrPMGBqCJ9_a1ugZH8DCym0VOY8G2sWBYOo6-tSV6NDj2oFPv4K9CiO4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از ساعات اولیه رزمایش ۳۱۳ هزار نفری
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462744" target="_blank">📅 09:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907997fb6.mp4?token=TFwi9rTZRw1va2jUZyBCIGzJWvYAJl0He0QRyP2h95gYWHpCt8FCvv71KQMgnubqFqv0qPkA0Zus_pfG4rUg_KAtWlBGdBpwd6DnJYDbnnFpEi054mE95Us2eCFldvJmDAImnandNdLI6TCotDWkYyfBthjlfhPv7zMSOKx3kyLNfu8N_Q5DGj2YtzlYpuvWQ0aYnxW2EIuc-gJ5UAOHkT-zwuA2TZbXq7N78jLDjhAgKuM0EY1Jrui2gXaurJ5IfOzyt0d0CbRqh0n6qML6Etk4Rlr771wuzEbXW_Jdws9vmsnng-uAvpIlje_kQlvDKWfBM6OLIxvfER0a9JUnUYJ8cNBkvzE3G8Upr9N_G5btFPknVhhd0g03GaGOOkshFb5lhJlLvr6Jp4FRpQzgI6kLvgHo2FBZY3maXrfx0Zhi553qZ9aXRjg2WiJweKyp_luxhZOZA_-cd7ZbmKkGAW3QsyxbH2XDKPasJ1_ta36fnCGOLn4t9XvjgJKktGmcJoviQhaZK8lHOpBeOy8jHuOK4q2KSoQ9jqtZrejpAEh-PBTgfZiPgGMF_So8Qr7rSK07rOz9M-kNhEohfZypls2lbFl5Co3OlvmyaSp30GEYHVwgVs0wLiiDnwBhqNom2MDhgAv9sEOELs7NaNCWDkPUmSdy84KqqqynQ2MGZOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907997fb6.mp4?token=TFwi9rTZRw1va2jUZyBCIGzJWvYAJl0He0QRyP2h95gYWHpCt8FCvv71KQMgnubqFqv0qPkA0Zus_pfG4rUg_KAtWlBGdBpwd6DnJYDbnnFpEi054mE95Us2eCFldvJmDAImnandNdLI6TCotDWkYyfBthjlfhPv7zMSOKx3kyLNfu8N_Q5DGj2YtzlYpuvWQ0aYnxW2EIuc-gJ5UAOHkT-zwuA2TZbXq7N78jLDjhAgKuM0EY1Jrui2gXaurJ5IfOzyt0d0CbRqh0n6qML6Etk4Rlr771wuzEbXW_Jdws9vmsnng-uAvpIlje_kQlvDKWfBM6OLIxvfER0a9JUnUYJ8cNBkvzE3G8Upr9N_G5btFPknVhhd0g03GaGOOkshFb5lhJlLvr6Jp4FRpQzgI6kLvgHo2FBZY3maXrfx0Zhi553qZ9aXRjg2WiJweKyp_luxhZOZA_-cd7ZbmKkGAW3QsyxbH2XDKPasJ1_ta36fnCGOLn4t9XvjgJKktGmcJoviQhaZK8lHOpBeOy8jHuOK4q2KSoQ9jqtZrejpAEh-PBTgfZiPgGMF_So8Qr7rSK07rOz9M-kNhEohfZypls2lbFl5Co3OlvmyaSp30GEYHVwgVs0wLiiDnwBhqNom2MDhgAv9sEOELs7NaNCWDkPUmSdy84KqqqynQ2MGZOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژه یگان‌های جان‌فدا در طول خیابان‌های تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462741" target="_blank">📅 09:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f58446e2.mp4?token=YrPk3uEJvLLLIxrkAaM6uYrd4AGWEWPc25wjciQCVN0oV2joGZydzd6ovXaa7Trxdo53refX7gqu2e8eRroxMOX-aSf9ZNzkIzDQEL8y3IjL0ZnJfC0oehd326xKStZNL9fVEYtXbBw_6yLI2tFFOPL0Bvgof8aB2ven5zdwh6FP3m3Ze86R8qCc20hhSsZp2noNLN0RRaFu9p5xSMuKA2dOfkFFPBb0CNQMNjm84kE3zuVs1KaPNB96kPLTNFv6wTSL9cRwPhi3p_B3LwuqXkG0UgAO0rV6MDmGF17CQ2ZZQMWJ8k1w-Nj6t6RmcsD6HFFANxnbecGbcYEoWZepjLZK4g0KvuIapXYmvUIKhmuyTbydBBZthbGqq4jV4WUlpqZ8gdViz22utIKqxCgi5IakcFtZ4bmHD1L8KOSDxC0a9XZ4x5f4DdOO-jDhFxI0Aog3K_6pYrsrCibPz8ULhcloXckXFX1571jCldIcLUVqBpEVyvUQM6HMqXXW9Vo_soRr8Huz89Ead2-enKyMZrJs_V1wzveynEtgjPLpaB4rtj-PR7xNCQ91ELrkHEKPPfWeTtAAnXLXFnHc13uVicPmF2WpcdJXvrCXiAr7n277RLKDExB6SeF9Ph7k42rFfJk0Am0UjiSC7IKCdPZCsCwe5XiYAip-eGfu5jVZkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f58446e2.mp4?token=YrPk3uEJvLLLIxrkAaM6uYrd4AGWEWPc25wjciQCVN0oV2joGZydzd6ovXaa7Trxdo53refX7gqu2e8eRroxMOX-aSf9ZNzkIzDQEL8y3IjL0ZnJfC0oehd326xKStZNL9fVEYtXbBw_6yLI2tFFOPL0Bvgof8aB2ven5zdwh6FP3m3Ze86R8qCc20hhSsZp2noNLN0RRaFu9p5xSMuKA2dOfkFFPBb0CNQMNjm84kE3zuVs1KaPNB96kPLTNFv6wTSL9cRwPhi3p_B3LwuqXkG0UgAO0rV6MDmGF17CQ2ZZQMWJ8k1w-Nj6t6RmcsD6HFFANxnbecGbcYEoWZepjLZK4g0KvuIapXYmvUIKhmuyTbydBBZthbGqq4jV4WUlpqZ8gdViz22utIKqxCgi5IakcFtZ4bmHD1L8KOSDxC0a9XZ4x5f4DdOO-jDhFxI0Aog3K_6pYrsrCibPz8ULhcloXckXFX1571jCldIcLUVqBpEVyvUQM6HMqXXW9Vo_soRr8Huz89Ead2-enKyMZrJs_V1wzveynEtgjPLpaB4rtj-PR7xNCQ91ELrkHEKPPfWeTtAAnXLXFnHc13uVicPmF2WpcdJXvrCXiAr7n277RLKDExB6SeF9Ph7k42rFfJk0Am0UjiSC7IKCdPZCsCwe5XiYAip-eGfu5jVZkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز رزمایش ۳۱۳ هزار نفری جان‌فدایان ایران با رمز «لبیک یا خامنه‌ای»  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462740" target="_blank">📅 08:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44e5b9d94.mp4?token=KNBBIOK8TVOnym6Bc50xm8HMZWbpbCOoj6I2I_sZvseFo06mMozXgLTKDCp7I3Bj5HRIEeNi2Lv3szYUHNwRzfrqWRXJcLLIXJKGWf0xx8PRRcBGmzhHEo5WH6J00BNrR0hvf-GBseDnuPL4-In3t1fipZ67m_O9L6PXPjXzEIbdAH92N5g7pvukK_47e3q1l2nK-_7sBz_LLDnuNjcsU9PblJSMF93NLnAZtCHs5lFFGJLsn9fYlwrtmuCAsl7OdhurD9aczXfPA6OBk_lLr9wW1r4qRtIkmh8HPJmXokZlPgJsQZd83TuERk5qjynZRmsBiY3As4Zg75lXzvJ7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44e5b9d94.mp4?token=KNBBIOK8TVOnym6Bc50xm8HMZWbpbCOoj6I2I_sZvseFo06mMozXgLTKDCp7I3Bj5HRIEeNi2Lv3szYUHNwRzfrqWRXJcLLIXJKGWf0xx8PRRcBGmzhHEo5WH6J00BNrR0hvf-GBseDnuPL4-In3t1fipZ67m_O9L6PXPjXzEIbdAH92N5g7pvukK_47e3q1l2nK-_7sBz_LLDnuNjcsU9PblJSMF93NLnAZtCHs5lFFGJLsn9fYlwrtmuCAsl7OdhurD9aczXfPA6OBk_lLr9wW1r4qRtIkmh8HPJmXokZlPgJsQZd83TuERk5qjynZRmsBiY3As4Zg75lXzvJ7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز رزمایش ۳۱۳ هزار نفری جان‌فدایان ایران با رمز «لبیک یا خامنه‌ای»
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462739" target="_blank">📅 08:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgIKRvxoSAfNy44D46kff7pdad6laetndHmb4fbz63Wnji2p0VIc0r5iqredWc7hJ6gK_NcCiuSNR3odAjLwlMdfoUVnXSC2UwAgXlunsODC3cNckxqUfYqS_JRDsdCm4WZ02VxFXykVJe21eVsfJWgdai7hoqlRqEKtcFZtM77bphjcvZce68ZPddqhojL4rTPTuuJ6VgWvSmbuRplV-62piZ2drmjjoyB8UEDgdc13elCJsx7lqTSInestD_bO3xcaCDzjAeLHIns4gEyhcctBkmXMnEQOlgs18mtnfdSFKhHZi8RrN9JMgbGeErwRmKTKhNCgeTtD2KJhKdetPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدیان: ماموریتم‌ در تراکتور به پایان رسید
🔹
جلال امیدیان مربی تیم تراکتور با انتشار پیامی خبر از جدایی از کادر فنی این تیم را داد.
🔹
وی در زمان حضور ربیعی به تیم تراکتور پیوسته بود و در کادر فنی نکونام هم حضور داشت.
🔹
امیدیان دلیل کناره‌گیری‌اش را تفاوت شرایط فعلی با مسیر حرفه‌ای و اهداف خود اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462738" target="_blank">📅 08:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rs6YcWybIQ9gAqo73Q-fraZescQUIvwSKN6TJvc-fSTc-pKGDGQoDRN5EeVGjlrBWtC8GxQHBkSaHvmpHR4rhUWp3tuQzhlFa_P9mDXcjCSE3ESdjVvfEzczzs8xHO4wXoS2SefgSIHvA-wWn8tkpiC4ZFhe0En2XcjTBC-TUKbgpus6XziY1oa6FuGfgAJsm1jAlE4DZ6q3oLDS7QWf8hDvmrtcgvZ22gsjjrwdsKJTsTBD4F956DKFlsf8O2yIB03E0LDCS5vRixtCzAYR4UNugR2tCXG-rqfoblqtsLY7quqOdnOEp02vnw8_gM-C4Qru0Uk3PFXTpsWkl-CZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-Cg91O3vxQeU3T624BXBRdLOE6Nur5e7PerPgeDR2sQ0i--FP04yZzj12VwDlvH3RjwaIUoaKS5f_L6PlcTP7F8ARUnvJlVb9YDhyA91Q5DmJ9XXopZYIk53etwYcoRd4ENe6949stnVx3NWvN15x9TNtY1aG0hOtRzYmDj3dbd-s6Se7c1lsfhhprCPDYf23BybEH10Sr8kTG8TDuOSwN_e8p4i0uMLXD54K61s6Yd1qUw7W6k3oJOe3ssRyawrka2Fnlc55BGesJwtYUHMMBk6zxOhED35_PVqwhEdyJ3eSWcV7n5Vsw69M46BPG1MarIosluJIDy0W6XjQCvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU_7cfgs3yT6s_ZeZkDhoVyb6xHndDmlODMNdl_hsUPQ8IhsvLhj3354Sh_atsmb-Cj6IdXqlj-QYYi5pmRx2n_enk-lsLrfwDwLqy8XV11oCBJHI5HvcI5wkBY3XP10VrDv_HJgiaW8Ej6eOZTJzi1-70cSj1DZOGhN21G0ivRduEBInI-v_HMwMgcQtAR8Ba54u-Ag0gK-cNOiU5jBkU8kbMus1mDzG4lLekK8X2NJbvYqbNLqftHdaKkU8rbSNcJJKicHjiKyn4FNuGPxH4jb75ox4KqKnChftX2tNsxR7mnYvDN1n5ziB-LjbZBVa_B-tNGIjlwEfuCOh96hqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn2JhWqjIZu0sZbrz_U8cTckjFMPE-Ga7SqcL0jNCaYzlg_cgoDend49RVJpEnHchONJW9Z54L-M8aVlqGbPT9gkTkP3fbnQQBjevrUS0qVyxOFO_s4xvJSK_c9mdt8bvCVSLEeSBlsRBGELBjtGmYpRMvBQLqnYBjy8fcamSLErkE7T2GHg8BYnmM_LH1mjQI3DqX2NLC87Ar_W18_1RY0NkuZuQbF5ufFNPWWQgzb9J0Ozo3LD35k_cUIIQAtPNoqtDyepyLUJKT9YPCE1P5ZhnU8n9dQm5zJZdlpuFPp6YBKHm1qqhL0uOvcDdij96lDAXPCU8VUGSgQR-uo0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-rYw5KL19S3nDkjG5WWsYHAJDpfAmqu82XRx07WObsmou2GSR_Mgi_3XNDFsIODjgCmaUVqu0yp9hDqxc6B7lJYM5bUoZDMWq_tM12m94xaYjFzbEb1I8FdEac8uk0xS7hvfIbLhVpC7AyXN7wiZP9ywt6Xn8W6T125ix8vdsQciWlLd0upb23jw7djueyIwpJ7woBT2lSqeKxWljhtVyfi5LJDLmlvzJ1cfMy1g2igaxVe1lhKhRte6V5sj5o6wvaCkhYmGZPtIDOxdnSOzzeyYVvbkMOlm29CZowavX8h4KyTn8uTEqVPurmv1M5CEYo5sumU3xCD_GsoAF9hXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZW_97pwFEmaG5r4KV1HsndDi0M3JZhRRuAVo20Ft0MBQo2pM-MJrgdK1h9SXsnoD1I5-xF9BBFjzk4gieAfgUQkZmU-u83F-MUzvg2I5giql1sI6qrSE26CK6-i0-vqu9GW3Qp4HHkqqgFaUnVaCk7grkvVM263mX0sA7Ljfpu9gz2YGrj6hDLPMOt_fWV3ftyYIWJ2t7LWvmA9ze5fR9nM7aL_BYewegWXV8JV5832rzKcpl7proVu_7EqDT-Mj3VQ6_-qhywP28Hetmqg-qQsQ3fYSUJMi4MOWTYihlO42KxgDRFX7V1PLSyTweegixct4cwYXsnfR9KN1a9Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8CP8JDYwrmpqBVp9WmRqm611jKisIxCktH3f633r1WZ-awWYh910_AB9RkJbi8RAGzo0vzIAlr10gN3ZLMyIDWR6WwpGCTwaMt8XTE-pETRPD_HeBPULwZugs589ywvfxxqdy6w6_vlYqwNahJLqxaxDwYODl6Gsth9g6TvwfwbJ2hf5ZplYvI6a2we_DJ6h9_4gnh4cIjnLhrj5dGf8FKGewXrNgSjs8m_Ymb_OQBGDhN5cOe308D_B1n26HJF3Z4v0uSGoOcHEAp9d-jzcaOSW_1kBzYV0rG7W4w9NGkau-w2S-f6MMWzDF4Fcz7V0Wy38t12DGS4MpnPORW4jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آبادانی‌ها در تکاپوی مهر و مدرسه
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462731" target="_blank">📅 07:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlubIR4iCPc2AXCAWoPPkWrkET6z5EQzSGYFh8WYhE4J6KUPhI5Ml7ciIL_pKO8vEF2D-agQzrEHhcsMP7gTMB8BbZkpPZA4KQFmNo75cNKFAi6M4t95W_uWvEIm-XfCmNnaMnQywGVetMogwTCkVJVsSc33qXUbMalkJgSiMxI-0x3tij84ML7zt5cYh7XxRZz0MrMa-PF86YrF-1_efLHDvwKyUliIoKmDjEYssk_p8SgOaJlXqHBTL6utOrhesLZwt1CF5fvZCQMDipUCdrFpBdo8UvfKw7QXrIB2Q2PYC-0qtTlk_KCsX5SJiS_3G_4zGmK4PIE2hi_xekkOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن روزانه ۵۰ نفر در تصادفات جاده‌ای، در شهریورماه
🔹
جانشین پلیس راهور فراجا: در ماه جاری بیش از یک‌هزار و ۶۰۹ نفر از هموطنانمان در پی تصادفات جاده‌ای برون‌شهری جان خود را از دست داده‌اند، که به‌طور میانگین روزانه بیش از ۵۰ نفر می‌شود.
🔸
شهریورماه از جمله ماه‌هایی است که ریسک وقوع تصادفات و حوادث جاده‌ای در آن بالاست و لازم است مسافران، به‌ویژه در روزهای پایانی این ماه، برنامه‌ریزی مناسبی برای سفر خود داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462730" target="_blank">📅 07:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2IAqNbdk2pkkrTEea4QQSql4NgZx89S5DcO81OxXvcWU-QaRQbN9ununJ_D_uO4ETVu6fvKfuEwMcIvCzF9urTkrE1M0046zvVpjGTxyTtYijEapHYNl3__pQRqo4gDyNaVZ6m5glLBojSfYGazG-5bFBmFdeMT455oM5G7FXnoVs56W6p9S4Jljv93pFqXmWPerH_JLCnK_D2-bZ_SbYeSwYX-JzY7Qc-0mzTDb3oKPiviljjCo4V7dNwMaRYDMtH-ieccRndRuEL23N6qJcX8uSaHE4vjMBGA6glipAtFLEx4XDpWTFng0QuhO710EZaNWtgxB1h0RYZz8V22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ بارشی جدید از بعدازظهر شنبه وارد مازندران می‌شود
🔹
براساس هشدار سطح زرد هواشناسی، فعالیت سامانۀ بارشی از بعدازظهر شنبه ۲۸ تا اواخر وقت یک‌شنبه ۲۹ شهریورماه تمامی مناطق استان را فراخواهد گرفت.
🔹
طی این مدت، رگبار باران همراه با رعدوبرق، وزش‌باد شدید موقتی، مه و در نقاط مستعد بارش تگرگ پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462729" target="_blank">📅 06:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7z0Wwy9JbuxZicuryyJNlXeI3PDEz7C1qLeNSJ5WAneRL0dXLXNd16yzwhBZnQFIXlu0zgX51DCxFZclsatwLlmolRX6bOttCAs-oLmd4wkG4STWMVnU8JpnTUOTnebpQdz69GERkfYGX-TB9DnvX2Oiu8BJ-llWiPpRql-QrwXOdyGxd34gRbRjrfRQj0VS9-3kKRdHnsTAhh1gwFopywJgjzIX42OQ4a3hzkr5JEmNTYvuObWygPTZol7Vg9nMHgvcFJiEKPZDtehbdsPTpdDFFmgX9xdq06NjC0yfyCPQ6ct5lu5z04k0K9f4pGphmMPidcVxG3aBSNYXFHJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان: ترکیه و پاکستان مارا در برابر یمن تنها گذاشتند
🔹
یک مقام سعودی در گفت‌وگو با شبکۀ ۱۲ تلویزیون اسرائیل از عملکرد پاکستان و ترکیه در قبال تحولات یمن انتقاد کرد و گفت این دو کشور به‌رغم اظهارات حمایتی، همکاری عملی قابل توجهی با عربستان انجام نداده‌اند.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462728" target="_blank">📅 05:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH1GTkT1ctobwoi_1ZRO8_Fb_ejSK8dMF0uCEeG7iv7TKbfz76xKfMtv5Fq4cdDDVSjOXVCjp9DjHpS-gBLMhuukRli-XlEqFeIXXOW9mmtELFmi9z-qWOs696rAVSn6r0cDajtvFqDpR08U0-8FIehtDIN9zgerUJ_vTf3d3spIb9s8XAcqrJ6Sbg-XM3QOWsnrI8p25sv2ely4sdDlYla96EPNus8FGp_YoDobAgeaxIKuytDWJhstpBzmC41d1MSDPxRA11VZSzjQ348eP2ZZwghpqrxzxhu__NED5_LIMF1aG9xYR1jQmrkw-WWVyYJSszsoTd_aCMNNKPMjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات جعلی برای اینستاگرام دردسرساز شد
🔹
دادگاه آلمان متا را در قبال تبلیغات جعلی منتشرشده در اینستاگرام و فیسبوک مسئول دانست.
🔹
این پرونده پس از استفاده از نام، لوگو و تصویر مدیر یک پورتال مالی آلمانی در تبلیغات سرمایه‌گذاری جعلی شکل گرفت.
🔹
طبق گزارش رویترز، حدود ۲۶۰ مورد تخلف مشابه در یک ماه گزارش شده بود و حذف برخی آگهی‌ها تا ۶۲ روز طول کشیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462727" target="_blank">📅 04:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fcfcb13.mp4?token=hRqnOCF2IWrzuBH0cGIjeWJOK81j2QNb8AeWywkXV-T3p_cFo8I3kQQEGVRVYND8nnwQ-RI70qE4ne56bOBOh23WRIbFmGaVTRDy8-pkAEH5LDLkmmOib7IeInZGHZvaL7jlys2fe79KL5MzglE9wnnw0eYq4puqrzUrfViRomkXdUpu8WggVNjzfy_8rGiySSXhqNbWYcaqmhE7h9e9Kp1bDbPK0nzptM5La2DNWaSsNjzp0eSwvwMzahim9feNjDq0MKZgykcSyc-YX1oKx-3_I252ZiOZVq4Lt-QF9c29abf9CigjR_b4Xl-s34isPKtsb_NbG4VzFxbqQv_RWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fcfcb13.mp4?token=hRqnOCF2IWrzuBH0cGIjeWJOK81j2QNb8AeWywkXV-T3p_cFo8I3kQQEGVRVYND8nnwQ-RI70qE4ne56bOBOh23WRIbFmGaVTRDy8-pkAEH5LDLkmmOib7IeInZGHZvaL7jlys2fe79KL5MzglE9wnnw0eYq4puqrzUrfViRomkXdUpu8WggVNjzfy_8rGiySSXhqNbWYcaqmhE7h9e9Kp1bDbPK0nzptM5La2DNWaSsNjzp0eSwvwMzahim9feNjDq0MKZgykcSyc-YX1oKx-3_I252ZiOZVq4Lt-QF9c29abf9CigjR_b4Xl-s34isPKtsb_NbG4VzFxbqQv_RWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا دعا کردن مثل خرید اینترنتی نیست؟!
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462726" target="_blank">📅 04:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عربستان: ترکیه و پاکستان مارا در برابر یمن تنها گذاشتند
🔹
یک مقام سعودی در گفت‌وگو با شبکۀ ۱۲ تلویزیون اسرائیل از عملکرد پاکستان و ترکیه در قبال تحولات یمن انتقاد کرد و گفت این دو کشور به‌رغم اظهارات حمایتی، همکاری عملی قابل توجهی با عربستان انجام نداده‌اند.
🔹
این مقام سعودی گفت که از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.
🔹
وی با اشاره به شرایط دشوار عربستان در مواجهه با نیروهای دولت صنعاء گفت که ریاض در شرایط کنونی به حمایت عملی متحدان خود نیاز دارد، اما تاکنون آنچه از برخی کشورهای منطقه دریافت کرده، بیشتر در حد اظهارات و مواضع سیاسی بوده است.
🔹
این شبکه در گزارش خود نوشت، نارضایتی مقام سعودی از پاکستان و ترکیه در شرایطی مطرح شده است که عربستان برای مقابله با نیروهای دولت صنعاء با فشارهای فزاینده‌ای روبه‌رو است و آمریکا نیز حاضر به کمک به ریاض برای مقابله با یمنی‌ها نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462725" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c730A4k6oKmxCGQdbyesiQTQndTZLRoRtfSUilr_jlujQ5lAMgWtDiXiP82wqgUD5AAJrL7qMsHdbJKXkfx5M7jlrPndD2s8tVWP4t8dv9wE7Wy99CJc-hkh3f1kOxs-p48BQv5eQkYI5LLXYXtCvCcZT0ZZgREncZucojcucX6mwBCcIbo_eCVedARTbNBUqrlU1Dq_bAxVl1kueNwPuqxOoaIhGwX1P_9zP46ouGypHdtpX6uNUGcRgKIQNnSTr9Kyasxf6mmwaKOv0a_2voiP3lPM80r_5rHzEOm9kDfHJT1IoVymZ7doNZAOl3huEHi428eHy7EmRT0Gkx2sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریل‌گذاری تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان، در کمتر از ۳ روز
🔹
عملیات ریل‌گذاری در تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان با فعالیت سه‌شیفته و در مدت کمتر از ۳ روز توسط قرارگاه سازندگی خاتم‌الانبیاء(ص) به پایان رسید.
🔹
تکمیل ریل‌گذاری این تونل، گامی مؤثر در مسیر پیشرفت و تکمیل پروژۀ راه‌آهن راهبردی چابهار-زاهدان و توسعۀ زیرساخت‌های حمل‌ونقل ریلی کشور محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462724" target="_blank">📅 03:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACD9qnj7k-gI8NGmK1cUmnC7RoSs4j338ibCDLDWS9_a9aRAMNfuko2eJ7bgguQ6LFrCiXGNgOPilM7k-9bH9Yrs92DL5WZyuVp8Qyuys1beWefN3kdDh_DKEwX5-jI6fxkyEiY3sLsWr5hijfm-46Xg5Yw-f6EWOzNV-xRjAFHPgVQnTTXm3ab39LDqMbgQoXQzMJZxQLH8ikekItktwELCB0NXVOehUglFUDNL0cLk_CyzzBswLfJKQbbl9Vir-5wavoezPYAeEvjjASPlgrkN3ZVfkgm_XVOCCsbsg7HmAV-QzGAmrASQktyGBupZmG1W50DLVOmU9DZl6OuquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-ZTe550vBTxuIKgy_1KgdJDCCjFBKgdERur_MTHuriIhph_fq9LyJ3kHsAL1yFFYyBdkWJ2GgSmLZ28LKEc59vDCgHIddFiNqr8EI_3SrkxfRVtFj6olf8iXp8Y1aggyFIS39YiFwxonFIigD9EUc4X5FP-QrfowgSBJrnsLHfVxePYetPKTgtZr4d0TG8aQCL1JImI_-3ejiqZXQEL4zIxWD1kGHV-gogTVDH-pYzt-2d8MBCGtYB6waW_afF2h9kxxNdrfjFqX3UyxTGxYIDOEg_CPARJ35cgxdWnYEZ5g0C9rHJCrw90XJveOE_ZfByzmuU_VI5Kw8P-rI1F9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkP48WZSGLc8dy19Yi9-fNwm52Sf5hbL9dM9SxLauCG2qj3gin5-QiEKjtfKubvb4Hvucv-_gFuFjeGXtGGuiD4vxYobHDouLvuqNQAA8PnlQKseAWqh-urp93puvFhxqurq5_DzqYlH3sD09TzE-Xq_oftT8BbA3TbaIg3K-N5nPpC7tpDc4nek4LNHUcgJ7rAcg2PdnhqwA91RV24PGab35PM60cjYL1QMFGTxw-lDo1zjZA44WkKSO-ecbxpcKrS3Ub1Zs8mcWR2d1Ee2cTuh8p8vYfYl7Ar5b_WbfrqbZfsANwBYWeSiYX1rSBCVRvVzLEECE1lqIKheyn4RvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامۀ خروج تجهیزات ارتش آمریکا از عراق
🔹
کاربران عراقی تصاویری از کاروان نظامی ارتش آمریکا ثبت کرده‌اند که در حال حرکت به سمت اردن مشاهده شده است.
🔹
این کاروان نظامی از کردستان عراق به راه افتاده است.
🔹
ارتش تروریستی آمریکا قرار است تا ۳۰ سپتامبر به حضور ۲۳ساله خود در عراق پایان بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462721" target="_blank">📅 02:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار در اطراف اربیل و سلیمانیۀ عراق
🔹
شبکۀ المیادین از شنیده‌شدن صدای یک انفجار در منطقۀ «مصیف» در حومۀ شهر اربیل خبر داد.
🔹
همزمان برخی منابع عراقی هم از حملۀ پهپادی به استان سلیمانیۀ عراق خبر داده‌اند.
🔹
به گفتۀ منابع عراقی، پس از شنیده‌شدن صدای انفجار در اربیل، هواپیماهای نظامی آمریکایی برای گشت‌زنی به پرواز در آمده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462720" target="_blank">📅 02:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWZ9SNWexUBJtnCfYFAoKK-l-So-FKs8go5Lz4eHjvAH8iCM9AzP2IITjbd8l8mRm0DANPGRZl_BJyD7XMXHJKgNuBMErPk4aM-x6StiSMFy3GGNdKlpVMzgxT4ll9vkS3FDvkHUA_Iy28Ij9hGUpTvtbucB3UCExYAjZW9HKPA_GuXHadwzy5T_si-ut1WCSJSv98eMkQ90zPFHq1jEjEmWxaPcC8H0secOhl5vll8rMqKBnjlO5WXJD06x9Bt4L0Ic9-3mtBkGcLubKulxOLqBHG9WHz1A-QT2yXzsnM1q1GDj-TIQaX32fbZY5HhaBzqTkCz-s6f7tQkWkbuxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: دیپلماسی هم‌تراز میدان حرکت کند، دشمن شکست می‌خورد
🔹
در شرایط فعلی، جنگ‌های محدود، ادامۀ محاصره دریایی، آتش‌بس و مذاکره، چهار مؤلفه‌ای هستند که آمریکا در قبال ایران دنبال می‌کند.
🔹
در این شرایط، عرصۀ دیپلماسی نیازمند دقت و هوشیاری است و مذاکره یا عدم مذاکره باید متناسب با شرایط و منافع کشور تعیین شود.
🔹
اگر قدرت دیپلماسی ما پابه‌پای میدان و در تراز شرایط حرکت کند، می‌توانیم در برابر دشمن موفق شویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/462719" target="_blank">📅 02:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فعال شدن پدافند هوایی در جدۀ عربستان؛ پروازهای فرودگاه جده تعلیق شدند
🔹
منابع غیررسمی از به صدا درآمدن آژیرهای هشدار در فرودگاه شهر جدۀ عربستان سعودی و تعلیق پروازها در این فرودگاه خبر دادند.
🔹
همزمان برخی منابع از فعال شدن سامانه‌های پدافند هوایی در این شهر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462718" target="_blank">📅 01:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از حضور شجاعانۀ حاج قاسم سلیمانی در منطقه‌ای که ۳۶۰درجه در محاصرۀ دشمن بود
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462717" target="_blank">📅 01:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4ucy-7gqTmxsKU8NyQoUwXZD7fz0i4JEiJF_humDB6xQg0xNEbdtCqbCSEFFx1SRIHRB5p-Wgdol1P5d1L99kiKSOpj_bA3W5tgBaZNCJ4RSiBD6gG3UaP7Pg9lGdFStp9PqULzbhzbt-RHwnLKT1PL6x28PJoW0WhV9Uo83kj5w1ksPkLVdfcTq5yxdGJK9tOijtzhSUfZfBIoIYQil20_GIqkX5ij0EL3EiPad3zqG4_71auBb_qgWkQu5ZZkmVm1iDG0A4oOs0GDiaCDbRHqsLG_2nOPhuglqaFY7_xodjb91u3wEItFzcQJxMZomaP9l-jf_AIolIy8W1eMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب دو راکتور سنگین در پتروشیمی لاوان توسط قرارگاه سازندگی خاتم‌‌الانبیاء(ص)
🔹
عملیات نصب دو راکتور سنگین در پتروشیمی لاوان با موفقیت انجام شد.
🔹
پتروشیمی لاوان به عنوان یکی از واحدهای مهم زنجیرۀ تولید محصولات پتروشیمی و مواد اولیۀ مورد نیاز صنایع پایین‌دستی، از ظرفیت قابل توجهی در تأمین نیاز صنایع داخلی و توسعۀ تولید محصولات پلیمری برخوردار است.
🔹
توسعۀ این‌گونه واحدهای صنعتی، علاوه بر تقویت زنجیرۀ تامین مواد اولیه، می‌تواند در افزایش ظرفیت تولید داخلی و توسعۀ بازارهای صادراتی نیز مؤثر باشد.
🔹
اجرای عملیات نصب تجهیزات سنگین در این مقیاس، مستلزم برخورداری از دانش فنی، تجهیزات تخصصی، برنامه‌ریزی دقیق و توانمندی در مدیریت عملیات‌های پیچیده مهندسی است.
🔸
این عملیات بیانگر ظرفیت مجموعه‌های تخصصی قرارگاه سازندگی خاتم‌الانبیاء(ص) در اجرای پروژه‌های سنگین صنعتی و نفت‌وگاز، و استفاده از توان و دانش فنی بومی در پیشبرد طرح‌های زیرساختی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462716" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4kYKTgHReCnd0WY8kkj_Za5R_f0xqo6ZrNvGEhpw1u7IXwXhyRHeyz-C3qaHwZo_BnaLHD8goLCorHUpsZ3Imdg4tSLjvxT3YlJiPuJ8c9L-yhk-eyzoDa1yTESJ8bft1-9hP_wIaEowOROfGFLZoKRq8XG6ZJb3vNZmWog4HIgJCCm91VkvWUz6YxCeKF7qIcTrIxZiJlf7jX0yEHR7zLqTOqZLiszbfEIQp5V2JTcuhnAKpMl8zPcLpmPnHb2nnkc26nbmBkTQTqFOdCwLkkcCxelRwwevSe2hqiVi-we2o5RclXWLhgVetGQRCn9en7X6GqSfYx8LWagUZcXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش نمایشی اسرائیل و یونان در مدیترانه
🔹
رسانه‌های عبری از برگزاری یک رزمایش دریایی مشترک توسط اسرائیل و یونان خبر دادند، در حالی که این رزمایش تنها شامل چهار شناور بود.
🔹
با این‌حال رسانه‌های عبری با بزرگنمایی این مانور،‌ آن را «پیامی به اردوغان» خواندند. ترکیه در سال‌های اخیر تنش‌هایی با یونان داشته و در ماه‌های اخیر، مقامات ترکیه‌ و اسرائیل بارها علیه یکدیگر موضع گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/462715" target="_blank">📅 00:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
سپاه: نفتکش متخلف با پرچم کشور توگو مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد
🔹
نیروی دریایی سپاه: شب گذشته نفتکش متخلف ترند با پرچم کشور توگو، با تحریک و فریب ارتش کودک‌کش آمریکا قصد عبور غیرقانونی از تنگۀ هرمز را داشت که مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد.
🔸
نیروی دریایی سپاه بار دیگر اخطار می‌دهد که عبور غیرقانونی از تنگۀ هرمز جز نابودی شناور متخلف نتیجه‌ای نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/462714" target="_blank">📅 00:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz3AcR341pvocVZJw4ZpwmIH9-eJaPAJ3UNEmLZMMDsUmA3F49pYHAuVegSG5GyoOAtHSf00vsO4XpmTSOKG3yc1qO7DuCGylLbowfuFARPjTiHjdfPzZ7W0wkkRPEZ36vQx796RMSj8Dxdnm4qMkhKPtW6Ww7U03SUMer1U1OFifVIOxxxEOoM_TYwLUCTL904Hdt4iyf7XMlcAtET_xJN9d4JDKxUJDZ_qYfpjEuvANMz87fcJuaKy1VChVPFlbClJBcoMuVuAOwR-BgnQ-YMSGURoVP9186QXm_PHz5f7M3cV8Ih8lE3PIuOTmpET5nAsr8UpccTOwL3SIrogwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Viw0_Nyv8nxG-3Sj0PJXcyYQBgN2JD_NHkvDoG2LEwsd7LC8PAXIgmDvJ2YbpIzvg2kwzNVl9MCxBH1Ezu0oXOkTbxUPuP08AV5CR4rIQvnhBhnZX6stVzaA362iFxAg6kRo4WjDhiJWp-oSK3I0CxqIbVr_t0uJJBP7Uonso6QH0mxTkf4g5JtGGbPZIP3YTVfc69YirfmYjraV_PfOrgdKMlj8vXK4tpSwlNMomESs3As7yKiPHyuRqnZUaaOJLE2nup8qoC_UHRT1AYO4LMSltKuoSpzpN0yXeMajxqP5nXoFRm3DLf3gQGx8BftdQhMMmk5aFgG1m0IIyT5X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qm420GUA3jmpN9KLfxweBCkp2q_x1glOfM91dZPfzupgQ9-ewH3_2LdLNZB6nEC8QE1jORz0lBBUmFaZtY_sAUJKXtJZQ51LcsNN0LXcxKMkdVxZ7ovDvzhSqJl-OmCznIxc6q-LS5lZ4l20emEhUssgHg5q7tfGfM741OyzLB0xQ--aSK55bFAA35aFjb6_OOJ0o6m054d0uxF3_h5h5v04bmeMZXD6Fvfj2V2RcPcd1bwR8hfoUUtGBzt_nsGSv3lcqb8x_EMGxh_siTb2BzDJ3LPwmfigMAy2O7Pq8YOUabNlMqUEJXJOoH-jxAWh-LCcVsJjD4ATz11Fe8FGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMbCa_LCzOtMPoaboOo0vaieHl-rkg2gBIvNjRLZA4-sSoW-Q6d8GsBNmMcWW3om6bsSS3ocTvaQFXGMKlo8xlqOSoIbv4JxHgSvQmxxRmrgpA7W6QLrYBaV0r0NEChTBLOQI-tDWJVKdtAwXCH8sQTt_zp1D0fG6L3GlGo-9plQ-2kgYaXg68PVgQo1Q9PhCCyWLUc0vthLsTPaKrYdENXsiuYSm5x6ZioVemQO8936V1VvvPfmtdfRuTdjKmYIC-vKWg8Ysq37jjr6E_BkuiawZ2jo6c7nJJnGGnNPmykksU5BgqQFb286UAs0Rt23kIkq8ZkRoh7Q_2ThqSd_nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور حجت‌الاسلام محمدی گلپایگانی داماد رهبر شهید انقلاب، و پدر زهرای شهید ۱۴ ماهه در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/462710" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/462709" target="_blank">📅 00:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foGnK4TaklpiOvfu9L--xP5tPdPFvxU21AllVDsqLgZfnrqE1QTBHuN6MN68Towe1_4k4Bgum0TvmV97FQ2db-t3oQY4mL4tCQzMeIDMTJcXf5_fxzt25pC9pZ9zGp9Az2kclxU9I9ODgmGFRWs7NE_490u9_soppsm3K06oHoEafRJcpf6FYy5bQ4RTcRVjHQv8FprBUOPzfDrvACYbkQEZzazKfbXOST4pWKeIRzUTtCYPw8ZbPyvmSdigMTqFIEXnO_dSFWTLONrR03gxj8GafVQhAOfgOGh9FqBtJmJ8Q7KIaz0TG4HWu1Tjrxp41FhTZ9kdcCoivcjXwAGlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما خیلی مراقب کشورهای حاشیهٔ خلیج فارس بوده‌ایم
🔹
ترامپ در مصاحبه با اکسیوس گفت که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای استفاده کند.
🔹
او گفت: می‌خواهم بدانم کشورهای حاشیه خلیج فارس در چه وضعیتی هستند و اوضاع‌شان چگونه است. ما بسیار مراقب آن‌ها بوده‌ایم.
🔸
کشورهای شرکت‌کننده شامل عربستان سعودی، امارات، قطر، بحرین، کویت و عمان می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/462708" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462707" target="_blank">📅 00:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxYJsGZw4GBAAVLoLrW42KB0RbiWviZ06Ia2wjb4ImWc_4DXNnJJafdZX-duGiYCx6d7YRpbuiH1oco2FA9kXDyGTFuQw9MecomRac8FpQQW0Umq-2NQ86gs3bvYYuh5D0cte4OlnUr2parvOhxmByLWDeu5Rr-FqHFphcFFDKgz0Uhs1nMpbQ4hL1ExH6S5f4vjp3rLPghY5-jjD45hUFYKn9aCnGXJ8t804DIQSUnNk58BuR3Y7r_p17DR40hgHCT61L31ruU6C5He8EEcet42OJ44fDo3bWg9bKcPGKi0fa9Uto5jjuuw5W7ocUMlBL6R8Pq3ySxXcX3QxI5Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxTM6QuSZp4JIbiEPP7dxTMrUCp_2_NZv312lmZK3i4u_aXj0-6fvREqvegvhUnA9dZW2gE3vWDUiDF-OHYft1tfZsgxVLy_MBc9FGFEdDEL1EhgLjQsTH53K6ryKs9D_0eMag3GyzjS4Cw-V6aeXc_DJF6Aw-6rRy5Hub1G5TCWGRiHLNL9KeAmhVHgvIgt1d2lpDtSV2dSTjHgK-EVWl4f_pXqtxxGgEDwzgpOUEhqm7Ax65LoY8kaHEGWQtp0SxDAEjL5s9toXRLUnS7JR29vmUmX8ufvE35dMxUYjnOorxm5ch0iR5OmFxkMg20hBn8gi6-Rja46l7FUPwwc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elCCIChbcfAprzOUfmwzL-I-E16C1MzPHHvLyOVDpsjCj-YQwuQWOmYGiYEdHWVHPnagipmEm_xsHr2ghp3W9rebI5ZLLHV7Ta_48z8EmS_QfnkmdCqgMbp5l5xF1pmIggdEYAttYAn25mG2MswZO-TXAI9dhDZjDv1oDsusFZJXGKcq5e9zTD808Ifjunm1YuJ6yuYJjlawLjmDAKKD1OUs6M1aicibasG_0n28Pm8wH1B0E9_xMu6oNsC4h7v1bFUM7tNHv2WxKCmYXxyIVBqGZJEjeK1yBYZNu9dspVOF0IspASDguxwKR1vUHHMKwWd4PUc2yxxEn0_I-GFhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVH20lGP-IcjMiIQjUtxTs4fWe2zJ5SZ2VnHCVQASyllfYx8BfAvX4vL0zx3RENobpOF-sOJXv389OwSSFddO0NB4nEOU_D2lIzPfjv-LuH46voTwvxOpjgdKFR1FG2jCi7dx9CL_B3e_6cbdnYUnxyWOwTSol26OHBFOA3BJK28SYj5cCOCU7FQZXZeizRR6JzXHrg4vHrmxPouOvRKmXa89Hc3i8PaOuDtHEQFsgeomOpYziOA3RjbeTb9Ihw8t27p5eWJeaQYFiPzfAzh6Dy8KsE5jP224PJRaCohwmQ_yCVumUVCxPo5_2rek9jUQOSHTpDFKW757WOk2T6uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiZN1Yp0U6HSlh18ZK_B81Dc3edogeJ3SIC6_Mu96N9Tu_fUek4jP8zlgw7G3XC2YYQPCG_u03wf0WYQSbFYA2IUlpaQQa8sKP_Yv5xOk_sM4DDZakL5Axk81CpNxRk6DudbAbhTXhyhQe_8-397rtV_EI1RN3uPzsk03BBZssw2CKfIamIUjYxYVUO1wqE2M9AvafFFqx_VpO1XfyQ8qSBkK1wjnL5tV6juFMoCa3GYEe6y_05BkDiwPleuZ48xQ6BofbQSw69CLnD0Um7WQSVq9W_nBFwUwkKj5WOcTYdPOUKGiuU-ZDbVZawBoIkUghucJlKyV34xowfBSfDUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmRCtE9SbWKK1iNpeXsEZLalCqr0prWU4dAjbJul3zEPTTZkFpkWn4I6IrsX3udUwNEGxxL_WI_66gJPTZZw2LvvuwsRbkRwrQzJCLbt4S5vWH1sg4ZZjZ1cdX_QKQYdB3Ddw7_sIfWqyjf1WEAiyRw8J9yOLkN4TksgmfsvhQzjXKZMEru3sZSVAx4Ri0tFxuljI2-Htunr5YP0qbeKYGJxMbrj87lf7PzsppV0BiFtg9ZVu0_3D7gPqug82Jlijn16kMNmbxyo4E5x-Smune3OHEXR15VEIzoacdSyXN9WkYEshiUKo_mIQ_FiJk-Zl4yIoJdGsmOrzJ70t8vIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwforE1gBvNl9E2zVHZhf7ove5yWBlVLWN14kSQ4S3gNFP9mLrVQEzCLCcnsLRlVsWnnZYyJ5lKpJ8cV6PP6bc5f6JwWLNcLXGhb0CmxOPokM26o611qI51bZ-J8Zgw39CrAQN5BWakVpT8Hq-ZyTj9bYn-eWz4s1t8BIwZW3yUpZdNg3OJULDeTyFTVHta12nsb7IOHCUB1x_t8JQRB5NznmREckLFt0ryWk1_U4YytSTMq7Rr6a8fgkzRujENjVt7IGIdHAlWxs5JBGDtCCxIPTSC4jG0ddQS_Avf6FCVx3ALpei4x4l5itCSSEydT-M1ys1paQj01_nD1IO892A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خشکناب به یاد شهریار
🔹
روستای خشکناب، زادگاه و خانه اجدادی استاد شهریار، امروز میزبان رویداد فرهنگی و ادبی «یک روز با حیدربابا» بود.
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/462700" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqFpY8ZyADvQQ8eN-h3yOEoISX4pKhz5YqP29vwZTprThd6s3DVB-_eTRcXS1O6kVQSVFsAUJpDrIfAmhKvVWxnJH8n9OBXMiq4BviGlQYTf1xPh9_rArd47gPbYN2DJ6RiAE8mr1I-FFes2Dt9nlOj5pjwshS781b2rZkU_juvwq_r-m4szj_BqtqyeJkK88cAq41DZIpCrsO_4TwDesT-6YXCX6cAYdi-jqDS-QFAA5g_og9fdeRkt9mMd03PnfCYvQVCnZbY2dPd4W3bUgsAE_ZjJlEb65Kbo9jxm7WX2O1UbUKHziKYN4iZCzD8BO2LG9G6wNcMY9Hwr-74eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد
🔹
اتحاد مقتدرانه ۲۰۰شب حضور، میان اراده‌ٔ ملت در میادین و فرمان راهبردی رهبری، نه تنها یک پدیده بی‌نظیر تاریخی در سپهر بین‌الملل، بلکه یک واقعیت تغییردهنده در معادلات قدرت جهانی است؛ هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462699" target="_blank">📅 23:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhtxGzIdymEZLcds48OojfbrCFr39994WdVGG1WpO221kZQESwAbwgeo8NQpCHuygbwXaKL9t2FDq7KT_3ULXayvaA0XC9D5HotOxkg1BlNra-sBjgDFq2ZKoQq2ApSIdHRII4vg6j4TlTm7v96LkEi90NxY0PKY-ypyNUqFeFcwkY9VbyfoqNZPXPkoT7UyDgn7BWpa7ES9ASolyDOlT5VNbjsesEVvNzStN79lMsjKc0gvR3n45mVIpS5u_-IWBvUoU3mqKXDSBxLFMWTn-k5tN3MKVKoHyxnAs5UlJcBIedpBZChQ6r8ULCfFVkdkg5DtG8GZ7ZFycPat9-WdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFxcHQqdfIlnDG4XPOPCTOnl_q6RDcWcMynefVUlaU8jJUOWlY9a6f6zTysaU7CDj1s5B1VBZ0iMckrKGKeJSqD0yOJijpJUzvmwSoWI0518Wsnc93An3k72PrFMJc_UmCDTQaGEC2O723zVQVysUnlQax8BMjX0uggbnNrvwMOKAYv5u8YGpW_1VBeEM5r0ncMSsaUYdg8Me635CYiURH9zxBHfTdRLPhg5tH1UlO7IB4ue2Yeky26OXbcYxHO5Gt9u7OFE9cesD33-GEeLc4qWuoUk-0VT4NspUulyFSDMvUXQHarEnCDYeZDp87bzV-2PQw0rC3omI578FLH59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0Yy2yMSbJcaWB1_BhTcxctWRv7qE314Ear_LtYoJobD_cgyEScu4T5YSgL9XWiYHbWnEPn2QT4fCIydmzYqSVM72wb8JNY5-X8gtHzXPxBFC_Y-BaahtoK3JCu0iUC3wvE4kq8LtjqDXiPO7eL3S0JOShf5GpySinObO-X6iDja7rrbDqDb-BHZwMCOXkAJw6bh2kJ8oMz6_eS8qUu5PHNqPytTKMEOly1zxuoLTP9abR5Poy1neM1GUOIGhL-FOjiQb5kks9ZKVRwGLj6JsSR5XeWMJChqZ8F2HgeFEzObcZQi2rgETa-M4yYMGwaeEfImPBtLLM2eUNSsR7b2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku1gWjlcKVaYhJFg0LqBID9kLaH-QuzaUX5QKzFX7UTgcEKwJILIOPqpts2lJoVoOMexhW26LUsFnAqGlD_9xHVwAHkc0rp3wSUVfsCpbKok0qZIPiYnd9KentVYrW1_pmtOkQ4RnuOlhqdmOvvjIRO3Nu_VXiAmlFQcaXGw0nELlfBEioyp4bcUYJ0kR9dJgNi_IdKrQtRlKz_jq-iJ-reYm2eoZOo1NoOXn4KzPqXgm39bazaQdkmAcKsh_oo1smUK1Hgk9V9Krvoalbisu8En0W0juS9jPgKXvEfwiE-pM3Y99ZAJTKAwf7p000wYzQjFaE6wVGo6SUNJ-D_WNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3rVSLwMLKRVIOBxwhSMLDBB8AgKwZ0vS9Aa308LQPqrOxCDpc8vDganSEGOqRBGTXXzQbpQ_VPozt8MORM-ZHdKab8RRD7tlV1B2f7UQX4SkvLiZe4fGFsN3rTNiH_OcKBNRqXF6u7M9JIBwCjt7Sh_VRIO_kGx6qskvhfSMX-IaGAOlLEVbCYO-MEWdZPNGdXaG0ABdcwrUcDvARlJWb7rrn-u-DO92UW8S8GrGsG_6YxfmbrCU3khnyeGHu3XPlIAqqCkxH0Q5ttNb6oIxkVWIWyew9tC8qA18nLikTqy_M0ZpRu59eA8b08WmZVG58TIlEgDzCK1YejHYyDa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2Q9dObhrBNUWYQiAlA8Q7P_9FdthmxzobYX2z-QnWg4XznJJSvzGAGJPagqYFe3B4BoBfLVXa9kFJMDcn_fmaAllw5KHcG__yjSi36yma-a7rYPccsn-HKurrwcLe9CyTywkM2Co8I5kzV4o9AoA3LG2lNhVLP39b63eyMi-RZdiWwKAxjdFoJsi6U514rY3lGYT_oJY1lo00pEpsSmg8tFyn8YC2w_sVm8H3o0UjVQPPJCvTR-xaFXV0NO1MTIR1bmunV6cl0O5lE1ILHTK_Jt2IP_FC_gi61kB_m-l5cdPVdb3POhHSQXUSQVFIrbBUE-bzb9zcpsoz-39p4_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLCN5O7j0TVNzvVB7dFAQSslZGr2ym-cajEZFN_EAD9tRQSTO2vs-6_JUJNfGNya8ki_r_ZuR2hZYJq7TuzUqP846m6Jui-Ob_z2ZPegAt_D5teHN2kePoOp7Hmw_Cpv97G8Gy9trtAzQMRaFUaMulhhRtTkLSyqKtWegP3knEYN9Pem9zCm2oHWgdlJ6SXbPA0LOWIFOhvsJljAcbDT8Y58yUtsbFExnagHgn-ug5Ty95gMf_FCExCKH9mFWf3EJQ-B1wp3qsJmo4mbUJ1zSSYbIMY6PcSJ6e-hccsiZYWXIxkvAfxaNVZm6-4HS2RHKSnnTlebpnWVDZUlvZ3XTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز بختیاری‌های کوهرنگ در دومین کنگرهٔ ملی شهدای چهارمحال‌وبختیاری
عکس‌:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/462692" target="_blank">📅 23:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462691">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-QBFjVglaMmYMlK9TOjZKroNguw52ZlOvOfL0MkJ7Q0G24aN4w2JWk0PE4D-vkM4fI95UDl224fWqYCBH-Euepa2cAq5P6EbHzrpMEd7VR8195GaSxy-k0LtWa7NLENqCLNY6IDzwW1W2Bjaf3wdRfO0dcFTpOztzmBCEq2-2gzmdcHzPTiNc7p70eSX3XkrXRg0EQNUEniW6T4CVJqHGGH3BdL7q4xEG5fg5IFZTqoLsm9NX9PsSwaLbRqfTDglRXMs4F8fQQWNrkqt5Nl4HeaJ8gv50BoF9BNDgO7kOlmvTTwXke2cb44geUQm4DgpVGIRbNBEjoH-eGu4V9dBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه امنیتی در تنگه هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) روز پنجشنبه از وقوع یک حادثه امنیتی در نزدیکی سواحل عمان خبر داد.
🔸
طبق این بیانیه، گزارشی از یک حادثه امنیتی در تنگه هرمز در ۱۶ مایل دریایی شمال شرق خصب، عمان دریافت شده است.
🔹
طبق گزارش‌های اولیه، خدمه در سلامت هستند و در زمان این گزارش، هیچ تأثیر زیست‌محیطی تأیید نشده است.
🔸
بررسی‌ها درباره جزئیات این حادثه همچنان ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462691" target="_blank">📅 23:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462690">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تب و تاب «میدان‌یار» در تجمعات شبانهٔ مردم گرمسار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462690" target="_blank">📅 23:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkM46UStfv0tZLlZHqA4w-Z5QONage21HPvbZtn1keso0ZVf2b5oqlr6JuzSBW1lDR7xSBQ7zYnfriQptyJzUiQ8-dO5pJsSompdk_GuYU0tLUxjYAQboRm3dEqbjL_uvUxceMQXnv5LiBK4MbXeJde21wn7r6MKKbOfzB1yGsM3ycNmyjD13ZlWRfdnoMCbn3BbnmP6_4kybCJCgNmPhB00HgVmCwaab-zte4-uxc4THJ7V6w0aE2r_VJ3DKn-AHptDimc8SuMWIzWLfNpz37aqwSp0vGRhL9fxKgg6fMDQQYc0TyDQVB4mRg-To0lCkQvtzClpnD4CQFaQ9YhuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از لبخند ماندگار شهید مرتضی لاریجانی
🔹
جمعی از اهالی رسانه امروز با حضور در منزل شهید لاریجانی با خانوادهٔ این شهید دیدار کردند.
🔸
همسر شهید مرتضی لاریجانی در این دیدار با اشاره به خصوصیات این شهید بزرگوار گفت که نمی‌دانم آقا مرتضی هنگام شهادت چه چیزی دیده بود که اینطور لبخند به لب داشت.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/462689" target="_blank">📅 23:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462688">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج حضور کاشمری‌ها در ۲۰۱ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462688" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462687">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3kbRxZQRztE0u6XEWDIiFI_BhNgrcLJlGCq8SBKO1awpF_P8Dw4zNvDudj8fmyUi2ikIBkUccLhmsRAv5Q8S8P9BiwvO0Ym0Osd9wicsyGqQg1GTw6hI0HlASDKry3UK8EisG5sULfhfyozRmZrcgy8Muz81cnXGvAUrOheFzC60GNhNIOdAwaMpWiyYsgoI9pfEmp18_OPZiyNqHWgkdoFaHRowqexZbNoFSNOyEdeEVDJ-S1_eTKPWu28gDrgkIEZq5UyVflwXvre3_vpIjDRRRXDooZCFXXWrhJ41msbAS5mwjC-wjO7HryyKG0pftUWc6VuD1Lp6BHcPLGHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: وتوی پیشنویس قطعنامهٔ غیرقانونی آمریکا توسط چین و روسیه، مانع سوء استفاده سیاسی از شورای امنیت شد
🔹
نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔹
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔹
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462687" target="_blank">📅 22:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
خبرهایی دربارهٔ حملات موشکی یمن به عربستان سعودی
🔹
منابع خبری گزارش دادند در این حملات، «خمیس مشیط» و «ابها» هدف قرار گرفتند.
🔹
سازمان دفاع مدنی سعودی ضمن تأیید این حملات، از فعال شدن آژیرهای خطر در ابها و خمیش مشیط خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462686" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
