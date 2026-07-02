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
<img src="https://cdn4.telesco.pe/file/lLXwe67IM6q4i7_wEk8EmefCQz56-Kpj1Lf9O9W2WspQKQZWCsldUdzuc7CCDCUQuaB8J52mhtscpBf8okUALc9CiW8uTxZ8EBJMY6_QZEGurLYODtEiQ5aSUEUvTaVTBw3pXK8J2Tg5bPGPq_lMw6tT-osUyXNVwhOZxU7wM2MSx9WpMmGkIwXPF1QlgT6xlKqxpg2PdE-Aq27ogBKYRPrbxfxe4NsCSv54w-1Wns0hsUGLFBQnzAse9GoP8AdG8fiTTmCdsNKAJMj4Mzs1m8-OgYVsYzsv-5es8sF50Od6QZ1C6oDFNcv3H7ysF1eUMbSE7y1sM1zmvK_vw2UZ6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-445989">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SorbvzLR35PrAcZBE-k694jDglWzn9PImX9S10ZBok_XTh9CYYsBzzjMZQ9gFVGFeALXl7D-S2DjzOji41YafuP0yLzUZ7Te0B9jT3Mze42C-mTdlJoTPSfUD61XZjNpqk3DlwTQmbaOxQTWXOiKdmQ-Y_3v4q-EeiQ9Mvv0lYZVZpq9hPLf6_NbRPR_NxQi_dcCqq919jX8nk-eWebDcNFzWJZ3W1K63fnXee25bnpE_9yUPsYIaDwEWP-DeLNI4g-rDERpfqXZnkWEyhi6kw_9KTDj9XbWjC5H3eXU3lAPm_ZWrbC9EPGQcoCp17_COsYxKRfyqyLxZH4H_LkesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ۵ نفرۀ گروهک منحلۀ دموکرات متلاشی شد
🔹
در پی ورود یک تیم از گروهک منحلۀ دمکرات به مرزهای شمال‌غرب کشور در روز گذشته برای اقدامات خرابکارانه و تروریستی، با رصد اطلاعاتی سربازان گمنام در آذربایجان‌غربی و پشتیبانی آتش رزمندگان قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به‌صورت کامل متلاشی شدند.
🔹
در این درگیری که در ارتفاعات مرزی شهرستان پیرانشهر صورت گرفت، این تیم پنج نفره به‌طور کامل منهدم شد و اجساد آنان به‌همراه انواع سلاح و تجهیزات در اختیار رزمندگان قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/farsna/445989" target="_blank">📅 13:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGO79RooN-fOXyNccMtGw-NGnUjRdTB8OWvm9iWuatkZQVoSz3CTbYEhRGUyo7rHLUyw4JKaMgrfZ24ewrphYNGtjO6njaHfs1MSc3bLCGnlbualHY8f9mNYyR-MEiutbFpPDVuq8SteqYOCUyNCVpt-Jk_xzizVocuJFAEtEbzGN7VIh7ldz4waD9NRilNqQEeJxKb-1ISh0SAA354s9HJvOkllvUIbAAuHNdETMHgsvGIT2wTRkvCl_WYgo2C5KLpNHFr2eLBSYt_yKHO9zMlJ0Ee2FY7bSn_I-rNTVexXbz7JlGgl2W1fqTvWtj3ThjpxC7ieejvpT3ZAtFyl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: برای بدرقۀ مردی که تا آخرین لحظه استوار ایستاد؛ همه می‌آییم.
@Farsna</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/445988" target="_blank">📅 13:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVnUwg7TEvbdtR1CdArYmC60rLglLMM-CM84FmhooE9FWzBwy1sBRq2-PjUnG0w7X1-CTQUhTiLJ5X_coLlkMALDcEp-sKT1LV3bG7eSJObMtdtj74nsokaQbUYoypHxS1jmC9gjPOid3PbB7QNwW9PPT91KwNt4xmivYEUJLCIISXiaKK7XlBNQTnt3rqT97d4jeVNwDqgVXpJidz5XTPqY6KuzG5N3Fchl_FK9AFUh-MhXra0GbOxf7e6Qumc8TEkhkUEW1FBCLSVyGw_hnLQBzhxkcbZ0xeAmQ5b3GqDdHi7qzCC2T3CUn25T3ORl0DoykRFmDdzqyl43sNBwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: شهید اکبرزاده پاسدار حریم ولایت بود
🔹
حجت‌الاسلام حاجی‌صادقی: شهید محمد اکبرزاده انسانی وارسته، متواضع، پاک‌نهاد و پاسدار حریم ولایت بود که بنا بر گزارش‌های واصله، در جریان فتنه اخیر و در پی جنایات رژیم منحوس صهیونیستی و آمریکای جنایتکار،…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/445987" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445986">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجموعۀ چهارباغ در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/445986" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445985">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_epNcvYHeC_Tz5mEv7kiZUbN8bZB9Crr0ceCsUqtJ_Mc_p8q_0zu-Vd3aaDPmopVtHLJns0k--n97bYnjqqev3B0t5KP0k_Wi1LpahuZufBIz32KNG-K-zsm2whgZp-O92Falm-4PZKN45x1XizBTh0V3d55taah8W4ihnCPZZ8IB-bMZ436fJ0ZeOF9c1yeR3PFi_r4nBaVN200Uj_by2zhIDPnPsdoE0vw4ZQco5KkVCIuuI1BnguBScAtl-rt0nj0HNkDYVnHsk_7YgSSmzP04W8Oikx2Y7YZ9eMRIKkQjyVIok_VYo4y2-hisZ5OC1wTobjs1p5hnCOa3185g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/445985" target="_blank">📅 12:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445984">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/445984" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح قدرتمند ایران اسلامی می‌باشد.
🔹
تمام شناورهای نفتکش و تجاری موظفند برای هرگونه تردد امن از تنگه هرمز، از مسیری که ایران تعیین نموده است، اقدام نمایند.
🔹
هرگونه عدم تمکین و خروج از مسیر تعیین‌شده یا بی‌توجهی به پروتکل‌های ناوبری جمهوری اسلامی ایران در تنگه هرمز، با پاسخ بی‌درنگ و مقتدرانه نیروهای مسلح مواجه شده و امنیت شناورهای متخلف را به خطر خواهد انداخت.
🔹
همچنین، مسئولیت هرگونه تلاش برای دخالت در امور امنیتی یا هرگونه اقدام مخل در تنگه هرمز توسط آمریکا، تهدیدی علیه حاکمیت ملی ایران تلقی می‌گردد و با واکنش سریع و قاطع روبرو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/445983" target="_blank">📅 11:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445977">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5paAfnNVRuMGuSUtv4BPelI64CSkN4dZih2DqzkFyojGBEFy18VM7R4QuGOu7As17fU_QlDgmHauwBcQgO31K2c2yITjmr1nIWPcknuvjb263Rfb4XuDWNA1Yp_wwf3V7A92uNYxqBxJ7D6OhXoi4BgxTpZz6nWgcohAmiJw9vJgnMPqaaGyiXIo86e4rfTai8gYks-DjQcZoF2o8-rrY-NYbQ_pZA4JN3ln-gaOzb9DD3WpLNFMS_a28UWnmFHAb0rQlAJ2MsIY-wvCuIHYDMQR9sQOusVMJ1Q6XWGyVl5QwVdM4d9AuzSEfy-HPapeOLz3aEHY_u-HmaKO8IGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXHpiqM9i8_Rb8RHmkmvG7jk6fRJJMBIXeqBUng9GsOGcbpMvzoBI6YHT507LAC4_ownE9QrUS3tSUvuWjxIwOdlQ-af0yKYepcDV9pTZKn8uX9SZhI8Dg-EqP3upRnOOMBEQXiz2xV_0qftluhCH7SvPl6gQCvVuKz-NQtzZkkqA_N_xFSPGxQ5WBUqKCeRFULisiRD2Zrh7RPHMXKg3Xij0nSoYYtI3Hc2gQe-QtayBZF9wQi3XjI-m6M92ezkBJGAV_sM7aCA-5YYezbQHbYrSFSZO5-PgMCOmhRjd7eZKHXIciAtWbwQYBslny97cFzUzpCvjtthQv6vC-MAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efj2ax0Fxtc7bHFotJZMrWoFPuHppy-n_hWx9bYhyf2jcw3RX-xtxqQXASD9ihQ4lIQcdT_SACIIZrgSXD1dchVjYjFyxpqJwyQSwmIWpfKlZ_CskOlu-O9wh1TfbixHxcf9pUanRznkrZAA1mAoW-Qp2900EznMOngcGpDFP-0vuCZudQbQwXIAbP6KCZ_qf0gAl5Q3Dchte3kp6uKTQ7o5Kdmalq05PvNPIJVIaqah_Z4CIcMTe2kfovXfPtl16pcSctcmFZ_MOADBezW9QljIM7PdRfUk2ox76KQnc_D3bfqmbb6TiQkTUHU6dYUHthwzusqFp7DJiXPMbuSb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnErD7tSJlcjlZM5CjgVojSqrf840tAkXyBNjMBwOsPLosqK47vMNZZ58MuUoBpLwOtxIdgD1oed2U3iv6_x3h4QhhAUrSEOZoqFjjE1yO6ZgGe9xf5t2LZEFedVGJMbVbNx-N0tQHr61Qh_uLzMRitPo4esyflZvOIDYMh6hiLRYL4xNfuLlQkP3YSbvRZJYUdFq2TNO30biWgLC93iLo0RCo_vBNxHgH5dbesNVrx0XwPvIuUH8bG3JvEdR911G8MOb-mRcWpvJXTJT_SxxrBtcMMSCXHzFxa8-DyC0OxvfvQJdxmwQmnn82z36uhDd4GFaR36NWgBYCBg8KDaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0NcnwFSasbGOn3wv9TtkboKaKX3_GP-2sx7ld-1JxW6Mlgzj-yX-rWRpt-b7QJULMjzdRHt_Pr1Rxr6eTMaK63jsJtic8-ooREVdtu2SDqN5b4ukHjWP6VFwKTBF1IRknEDWFFgOdhMemvG857j4c8a-g3Wv1tyzE1BTwxQkjAg9zy4OScoVoMUKPD9gcXAAWg7Bivmu2wHPUKHGrHjoC3QfbqGGxYv7a_LURlilRWu8XJ7eVQ5dJPCoBm8GXMOX2Z7IHuKYqZ-a2gycZYjcWdOfGNLkA9AjSqKB_6ONQA6LdQ7TDEEPmC6weyEzMDSjVKE5CjXfzlQloamhOKTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS7r_6tPJhWce75K7MwuWf8fXoj2TfbwARGKdwwjWAZmO0v1WhrS9jMFlJksNLFdLcVQ8U3nhdZr27xyYnJ-tc0Mkybh8KRWiAcBpJImQfaB9_x1sIRfXyYk3aR_C1qrbBGVjDSVZsnP9aKW2y1HFkYFAUBbsRtBPqC7rm0mCdXDC5U_elGCUFkDR3xiloN5uO8dFCzjDIFbA9h6TykJA3rKNm5fQ6n8ZP2ioN0Nses-xZ-e6vtN0oCEc8epPqtQ34hBuCSIeDuhdxxkRw_rSeCfV-_RhIHFBCyxkUgBiSM5AxVnm3VdmJzHvAnAzf0Cd7MTCXAiuJkaEHWzis55Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برگزاری مراسم وداع با همسر شهید رهبر انقلاب
🔹
مراسم وداع با معلم شهید خانم زهرا حداد عادل، عروس رهبر شهید انقلاب و همسر شهید رهبر معظم انقلاب شب گذشته با حضور غلامعلی حدادعادل، خانواده ایشان و جمعی از همکاران و دوستان وی در مدرسۀ فرهنگ تهران برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/445977" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445976">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: خودروی حمل پیکر مطهر رهبر شهید به شکل ضریح حرم امام رضا(ع) طراحی شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/445976" target="_blank">📅 11:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445975">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائرشهر امام خمینی(ره) در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/445975" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف تریلر حامل ۷۶۶ کیلو تریاک در استان فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/445973" target="_blank">📅 10:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/445972" target="_blank">📅 10:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محدودیت تردد تهران-شمال و چالوس
🔹
تردد در مسیرهای شمال به جنوب آزادراه تهران-شمال و جاده چالوس از ساعت ۹ صبح امروز تا اطلاع بعدی ممنوع است.
🔹
در آزادراه تهران-شمال، چالوس، هراز و فیروزکوه مسیر جنوب به شمال ترافیک سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/445971" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xp4vCqQK8Du4ExJNpdTwzLQd9KRWJaWRhyK1_a8Czxkx0VzBGbRQzldeOrb8HOPv9NVJWqtgthuTBnMy0qBlVGVe0DiOaA_r1Ate7bZtGxpxkTlHHwAJ6uJKuz3ENikWboQnUYB24326YW6HvyGtIQT39N36OWX_Eq-RN4eR7hUevteg1oKckZ-KH5nmxFN5HLPCEWP2Q9hDslLJacQgheT1wl88EJxHLXTF4mYzokNXkwr1tk7qB3CpeaCOLJM8oxEonUqnXh1VvgLzSVOXZAN5Pv5Rpk2BwyyOoiOkWD1S4UQpAea4hb5pX2WgdFsbk9-hR0XJ_ga1D7XVUDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در آستانه میزبانی از بزرگ‌ترین رویداد ادبی تشییع امام شهید
▪️
آیین بزرگداشت بین‌المللی شهید آیت‌الله سید علی خامنه‌ای با حضور شاعر برجسته فلسطینی و چهره برتر ادبیات و هنر مقاومت، استاد تمیم البرغوثی و دیگر چهره‌های شاخص رسانه‌ای جهان عرب؛ به همت پردیس بین‌الملل سازمان هنری رسانه‌ای اوج برگزار خواهد شد.
🕓
جمعه ۱۲ تیرماه ساعت ۱۷ الی ۱۹
📍
تهران، شیان، میدان شهید تجرلو،
مرکز همایش‌های بین‌المللی کشتیرانی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/445970" target="_blank">📅 10:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzlh5_sluka39awzrJise-bWxmu3JJ4-ucjFSvLNKGJFJNSeQPnMjrx4qriGHmlhAPjMSlYSQCkCUDzB-9vJ70XXm-A34McYpmmoiFxWfSJfPzxsgPP1DqJHR5IUC1l3NRgZmNJuXtgUmw-SBAP-LhA6p3Bcu14KoBiz7nCDGJzj6G5GbxtJKdSjRe56GzqEb5TJ--g_VYce8zewMS1T9PL2SdSMvQ9SMYsffhiQ-HwadQMcbbiXsozy7HI-pyjAiFFemcCTLqc4O3tT0q49BYKwUWf-3rb2E2ZfPz2RlMCwOuJrfDWsE-l3NONvdwYLsiGmfJnDFUX0iXGZTH2R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
پذیرایی موکب بانک شهر از عزاداران مراسم وداع با رهبر شهید انقلاب اسلامی
🔹
در حالی که ملت معزز ایران و جهان اسلام در فضای پر از اشک و اندوه، خود را برای وداع با رهبر بزرگوار و شهید انقلاب اسلامی آماده می‌کنند، موکب بانک شهر با هدف خدمت‌رسانی به عزاداران و تسهیل امور میزبانی در این مراسم بزرگ، در یکی از نقاط پرتردد پایتخت ، آماده پذیرایی از جمعیت عظیم مردم است.
🔹
موکب بانک شهر با استقرار در محل سازمان فرهنگ و ارتباطات اسلامی (ورودی بزرگراه شهید همت)، مسئولیت پذیرایی از عزاداران و شرکت‌کنندگان در مراسم وداع رهبر شهید انقلاب اسلامی را بر عهده گرفته است. این موکب با بهره‌گیری از کارکنان داوطلب بانک، به صورت 24 ساعته، ارائه خدمات متنوع به عزاداران رهبر شهید انقلاب را در دستور کار دارد.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/445969" target="_blank">📅 10:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/445968" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgR5rba7H8SwgJyx20OFSHNw1akjDukN8YadKsIDYW5_jGBu0ScKY5Q5QPifL7xjwnPEwa6NdzTa-H9xhKYe6ag-sBy7bP8clliJMmUeNovTgMoDSkpur3P1ql5mG1itUtVLiaQ4AmQ1J4FSt-9YRzXqzCFP8ViYA4oBfTJ-ZLYvG2N5ptEGE_9qtFmcVixa2Flyeg-cBwuNTJzHrOqMEo82VxWL4Kr0qgrZHUd-HE7xNkv85XwSRvkQFwFfVxPwplNwo-iVmSrVzGpai-bJwWBJzxR3Quja5EhMDBPZ04xSVfvI9PYKBzoLSh-K62p0jh7oq7KR4DM_mjbTCi-hNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری و لبریز از داغ فراق، به بدرقه بزرگ‌مردی می‌آید که عمر پربرکت خویش را در راه اسلام، استقلال ایران، عزت ملت و آرمان‌های بلند انقلاب اسلامی سپری کرد، مردی که به نمایندگی از ملت شریف و سربلند کشورش هیچ‌گاه در مقابل استکبار جهانی سر خم نکرد و تا فتح قله شهادت مردانه در مقابل ظلم و ستم ایستاد.
🔹
تشییع پیکر مطهر رهبر شهید انقلاب اسلامی، حضرت آیت‌الله العظمی شهید سیدعلی حسینی خامنه‌ای، تنها یک مراسم بدرقه نیست، تجدید میثاق یک ملت با راه پرافتخار شهیدان، با ارزش‌های انقلاب اسلامی و با عهدی است که نسل‌های این سرزمین برای پاسداری از آن ایستاده‌اند. عهدی که با اشارات خمینی کبیر رحمت‌الله‌علیه با صاحب‌الزمان عجل‌الله تعالی فرجه الشریف بستند و تا آخرین نفس پای آن ایستاده‌اند.
🔹
امروز چشم تاریخ به ایران دوخته شده است. حضور میلیونی و حماسی شما مردم بزرگ، جلوه‌ای از عشق و وفاداری خواهد بود، حضوری که به خواست خداوند، این بدرقه را به عظیم‌ترین و ماندگارترین بدرقه تاریخ بشر تبدیل خواهد کرد، حماسه‌ای که عظمت روح یک ملت را به جهانیان نشان خواهد داد.
🔹
از همه مردم عزیز ایران، از جوانان پرشور، خانواده‌های معظم شهدا و ایثارگران، زنان و مردان غیور این سرزمین و همه دلدادگان راه حق دعوت می‌کنم با حضور باشکوه خود، صفحه‌ای پرافتخار در تاریخ ایران اسلامی رقم بزنند و بار دیگر نشان دهند که ملت ایران در لحظه‌های بزرگ، یکپارچه و استوار پای عهد خود می‌ایستد. باید برخاست و ندای خون‌خواهی ملت را به جهان رساند تا دنیا بداند ملت شریف و نجیب ایران در مقابل ظلم و استکبار سکوت نمی‌کند و از خون امام خود نخواهد گذشت.
🔹
همچنین از همه مردم شریف و فهیم ایران دعوت می‌کنم همچون همیشه، با روحیه ایثار، همدلی و مسئولیت‌پذیری، در برگزاری هرچه باشکوه‌تر این مراسم بزرگ یاری‌رسان خادمان خود باشند، باید یک‌پارچه با خدمت به زائران و شرکت‌کنندگان، رعایت نظم و آرامش و همراهی با دست‌اندرکاران، تلاش کنیم تا این حماسه ملی در شأن مقام والای آن رهبر شهید و عظمت ملت ایران برگزار شود و این حماسه تاریخی به عنوان سندی انکارناپذیر از استواری ملت ایران و آزادی‌خواهان جهان در تاریخ بشر به ثبت برسد.
🔹
امروز هر قدمی که به سوی این مراسم برداشته می‌شود، ادای دینی است به مجاهدی که خود را وقف مردم کرد و هر قطره اشکی که بر این مصیبت جاری می‌شود، نشانه پیوند عمیق ملت با خادمان صادق خویش است و هر ندای وفاداری، گواهی است بر تداوم راهی که با خون شهیدان آبیاری شده است.
🔹
خداوند روح بلند آن رهبر مجاهد و شهید را با انبیا و اولیای الهی و شهدای راه حق محشور فرماید و ملت بزرگ ایران را ذیل توجهات حضرت ولی‌عصر ارواحنا لتراب مقدمه الفداء و تحت اوامر رهبر شجاع، دانا، دلسوز و داغدار این ملت، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای حفظه‌الله در ادامه مسیر عزت، پیشرفت و سربلندی یاری نماید.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/445967" target="_blank">📅 10:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم مهیای بدرقهٔ رهبر شهید می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/445966" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌ها آمادۀ بدرقۀ پدر امت
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/445965" target="_blank">📅 09:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین تصاویر از آماده‌سازی خودروی حامل پیکر مطهر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445964" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۶۰۰ خبرنگار خارجی مراسمات وداع و تشییع رهبر شهید انقلاب را مخابره می‌کنند
🔹
وزیر ارشاد: حدود ۶۰۰ خبرنگار و نمایندۀ رسانه‌های خارجی در کنار رسانه‌های داخلی این مراسم را پوشش خواهند داد تا ابعاد مختلف این رویداد برای افکار عمومی جهان روایت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445963" target="_blank">📅 05:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرود پدر ایران
🔹
تصاویری ماندگار از رهبر شهید انقلاب، به‌همراه قطعۀ موسیقی وداع
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445962" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔹
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445961" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/facVrfe8rt66B4zYB61kkx_HdK_COt6cwrHRy33WjAdEknx2Xw1WhLtvUcgAdCvDyvmmxvk20UACdZC4I1T-5tyaWegRBCXZea_TnfOdwszbAv2rI6S6LBrg5h83EUl1D2-Z3HQ78a6j1PyeiVoOb9cO0A3cpEuNzCtUhQDI4FC1VQ9cB0YtSt_8O1Y2KAFRdlEtT_tPtfqS0HMiSYDkt9tDAs8DbQQzmYA-EzCwORGRwsvoXh74ZU6Od_Hp_yadhbs_u5wl5CEcY1poFNqeS5y6Zh4d8LKWKYM2Wm77BQO0F669m9aDVqb8YxRDUmPQ1EPzNmh37TbBFAbtIl-mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رئیس دانشگاه علوم پزشکی ایران:
تمام خدمات درمانی در مراسم تشییع و وداع با رهبر شهید انقلاب رایگان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445960" target="_blank">📅 03:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGxtTYEbxl9q1Ly3_kS_ozguZkkIvJaqB1YOsG5XBWOVvj6DUmnhXHY4UYSUSqchnHZuNJJ8HuJsQuYruOGSGMlaTXmTRa9DSnZAz-dK7p1a772Gs9cDysp5tVIASxt8CiDKfVgPI8AUsz0SsJwsFWQK-LZGXo8twZvDsfAANapsxy39rwKviztPxilOVpSmdV4vB5SNajbr-dcDKbfU20Wy3qOfiOabzIk_Bo2JDgaJSjxx_xWcrzMSugOkVqQqbmiW6ZdDICGb5VNTewPpQq1niO4-Dz8PiWPpyRnMe5BgMYwRgN_4mVByLC7VygIQSxBCjXI0VVBId0LWybmtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۵۰ میلیون نان و استقرار نانوایی‌های سیار در مسیر تشییع رهبر شهید
🔹
سازمان بسیج اصناف: با مشارکت اتحادیه‌های نانوایان سراسر کشور، ۵۰ میلیون قرص نان در حال تهیه است و ۱۶ نانوایی سیار نیز در تهران و حومه آن مستقر شده‌اند تا کمبودی در زمینۀ نان احساس نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/445959" target="_blank">📅 03:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعضی‌ها دینشان گلبول سفید ندارد!
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445958" target="_blank">📅 03:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محل وداع با پیکر رهبر شهید در مشهد مشخص شد
🔹
شهردار مشهد: محدوده بدرقه و وداع با پیکر مطهر امام شهید و خانواده ایشان در مشهد در ضلع غربی تقاطع چهارسطحی آزادگان و در محدوده بزرگراه حضرت سیدالشهدا خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445957" target="_blank">📅 02:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وقوع چندین انفجار در پایتخت اوکراین
🔹
رویترز به نقل از شاهدان عینی گزارش داد که صدای چندین انفجار در کی‌یف، پایتخت اوکراین شنیده شده است.
🔹
شهردار کی‌یف اعلام کرد که پدافند این شهر درحال دفع حملات پهپادها و موشک‌های بالستیک است.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445956" target="_blank">📅 02:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzczy55HkU7BxHX84qMHx9UuwpCaFpiItHAUYyWxNerLgf0TaBtcXaNgJS0HJ4ZcXp3sDd1pBFNbfynY5LSCfBTQWX7CE6YyPD9767l6fdsueq3-0Hlw18BusCtNQLnVGIpSWnPNl_llfO1rhAblQWTM3BLKWjm3-tE_PWxDxNIcfRcSVOj9jGTXW4xI6BkW97jBjTZXCbXQkW3T5K0d69NlleHlRDBibt6wP0Ki0-QWfmwEZQ4LEKCrOVstRTNg-0dOmidpz5rfM2wvgDsvspvfQSRym7eEHIMZP1TXBve3LO2fZOd-N232oNZ1ZFYnr_Hv38mP1PaopAyak4L3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/445955" target="_blank">📅 02:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حملات صهیونیست‌ها به مرکز نوار غزه
🔹
منابع فلسطینی از حملات جنایتکارانۀ اشغالگران به مناطق مسکونی در مرکز نوار غزه خبر دادند.
🔹
به گفتۀ منابع خبری، توپخانۀ اسرائیل مناطقی در شمال شرقی اردوگاه آوارگان البریج در مرکز نوار غزه و اطراف پل وادی را گلوله‌باران کرد.
🔹
همچنین پهپادهای رژیم صهیونیستی در ارتفاع پایین در شهر خان‌یونس در جنوب نوار غزه درحال پرواز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445954" target="_blank">📅 02:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubSoh2CHAd5s3Ll1MMvTgwii-bcQtKIZNtnvQoX3AHhDLA9ml3mFpM8cOnzPZzOaqEskikcBI3h2PEW1RcPXlgPpMQJKa0oef4v3Uc3596xmPLQUCeA3CXAeRq-xh62S0plxNrxqjwKVVy3Blhng-P6qKcOFiH6U-RJXImSuqR3jYFj1bMykDDKcvYSr2dC8cB5rV4tnUZ49OkaMIB_2lT_7UYagwMdmQe9-tNAI_hLcpM7oAmsm5HYe6P72yGC-0WKH2HA0e-yuDJ9CNMMBdIUyHINRSWhjtul926twYodIgRxF6-LyNvlUnTWCu0u5u52dZQbkrGNRu_ZU7nBxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلای ژاپن را سر سنگال آوردند
عقب بودند و به بازی برگشتند
بدون دوکو، بدون دی‌بروینه، با تیلمانس!
شوک بزرگ به سنگال در یک‌قدمی صعود
بلژیک ۳ - ۲ سنگال
@Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445953" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب سوریه
🔹
منابع خبری از گلوله‌باران حومۀ شهرهای قنیطره و درعا در جنوب سوریه توسط توپخانۀ رژیم صهیونیستی گزارش دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445952" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جزئیات تعطیلی واحدهای قضایی در ایام تشییع رهبر شهید
🔹
تمامی واحد‌های قضایی در استان تهران در روز‌های ۱۳، ۱۴ و ۱۶ تیرماه تعطیل است.
🔹
تمامی واحد‌های قضایی در سراسر کشور دوشنبه ۱۵ تیرماه نیز تعطیل خواهد بود.
🔹
همچنین تمامی واحد‌های قضایی استان قم در روز سه‌شنبه ۱۶ تیر‌ماه و استان خراسان‌رضوی در روز پنجشنبه ۱۸ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445951" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
برگزاری مذاکرات فنی غیرمستقیم ایران و آمریکا در دوحه
🔹
رویترز: گفت‌وگوهای فنی ایران و آمریکا به‌صورت غیرمستقیم در دوحه در حال برگزاری است و در این میان، قطر و پاکستان نقش میانجی را ایفا می‌کنند.
🔹
نمایندگان اصلیِ ترامپ در مذاکرات با ایران، یعنی کوشنر و…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445950" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
دلنوشته‌های مردم در «کشوردوست» تبدیل به نماهنگ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445949" target="_blank">📅 01:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrniQv1lwJXmk0fqooJjC6p4FVSMH4MHwiOSxqaIATUmQLZEKEwwI9TwJREli6NyAKCH3u5RPsOqgX-UqyQ38G89IbtX8cq_mpK4DoCfJvUJQrSMy7eR-x3dNPCBDEMk3FmVc4YZXAJKbo4mjAWqs8NByUewHBdCyEqGg_dnU2eJVxlX-VeT_q_2wNG0IMiB6U6PBabIuMniFGAUb7pSE8b2J6hAX2V2a410GnrNJpTxj1ZD94PrIS5gzO29TUEwLTRkAap1lKfKI7Tp7V-JVVXGx2l1VArj5sHmil27Mm0UNIgf4c1PA2mZyKB7Z8kxk5XaYmqYP_1lbCprdb2xnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی محور هراز پس از ریزش سنگ
🔹
مدیریت بحران مازندران: محدودۀ پنجاب در مسیر شمال به جنوب محور هراز که شامگاه چهارشنبه به‌دلیل ریزش سنگ ‌و به‌منظور حفظ ایمنی مسافران مسدود شده بود، بازگشایی و تردد در آن به حالت عادی بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445948" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445945">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445945" target="_blank">📅 01:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445944">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445944" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyM5VwoYIJ-4RABAJD_xsG8YMOIfZag5LM9LePt1AaBFRQO6aucQAWPidPjMLgfs0VY2CV0wxX661PPMo15be7kvBwrUQSHIUCdFhJwLZ3l8jUFgYsFf2aNS2X0rt3JISdm9jdkA-M0lz7nTXMA-_sNHdhVgbKuiEWMAVBomaROCv3Qy5XiaImvdt7iS9Flvgu1-LljRI97AhjKgxPWkVBrWSWuMKQQtUcClcF2zMdkmUnxin0B8TqfoYtS4gzP3fycyK0U8bx35BVZFC1elMQdxMWqZgDdaRrZ4FpTym3rkfIGYQNPBNHck3cipHYJDQLywZ8aWKsKwNv5f7QeAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnfokLda0HtCETJrMCVhfNPUgR4mpZZDRuR4r1VDhEh-eqFVnNuMGsDPq9RQCGdvAhDdZOz5SXNDDnp_nsCNtDaeWFqRJWA3VGs2S5lqZEjA8yiUOmVPlOB7A-IxU9kr6Wh8Wn2Qg-p1B-l6q21EStw0hdZqLqkc840ZCS0mlPAYVZCYnsl09nOYpuyWTwjLQIysnMKf35P6zfqefTAzRnBlF4PTuBYB9L3ZMLsklZ2uTkZIWCW65Twk-lniyLKePrpP9UlE5X1DES5qsx87JvjmuV2-skHl0jktEX5wlbXtJjt7fSLxX0G_DLkJbEWboM-hRoOjmzOodvwtQO2ToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUU0SyoafYp6rBA9dyktfxuSnGGP3UQczjVj99lR8qmGlZ2QkPWPfOayLAHrCk8kFT8iPN94vatuT5VD-6HT3xK-ZVr0uxu1YZxdYQYtCIeTcGWS2VhsX1-Q24XJVXKE2dlin5kc9FBwOb2-gjuKPRN8HrOblLabiEw9EYScTtHIGNpntHZBwBDxQtFOUeuU3CryeSo4zd9SjWWq1iRP1MzEWy_xS2cS-sixHYYRzkqRF4IokI6fIUpC6J9kn3me39YH-3gRd-RaASDPilLtQtONDSgVBLlJSo5bvlQZhlaKvhAONkqVu1uxKvtliMqvXrURcMdvdF4vheUUEP57ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445941" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldaXFx3l3frLFWQhgntFF2LKnPAkoaeuA_eui9rIynjG6NBGZW2hSF63-y6_i98tVhzKGRWhnfZ-Rb5H40_b9EeHz-_3wTdOdrLi4iFMYRCUF-Zo38zpjYqpUyreZBfk9DXHbxECSpAqF9y0mIgye5s0qJKx-7QCoLB6uDWPvqdkc8UXlKYjVmf7wonL7MawSrExslxcK6KrmfD0lw1Yj9MFAgNSPH-CukYhV6rGL0kYSlLW6rW7XMImZsoyTr_zaDcGKEgNUrTH5RhdMUz5ZahlEpTrpjvAHY8_qyGDXb-_bOoFT465Hatk2OxXVUa1WGtZDCP_PbLQPy4rX36lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKMaH2fQzGocoCBR9SVpyIOAi_bh2zZza8on8DOKCtxJHuqWLaBe4BG02Y2-93fGEhQyEZ_fNsKldX9cC5SV-N5QqVtWywip-5d09ZHX-bsIcNvhyp_riDlPehfWH445bNqw2qMMKPEby66AVryFiWouAd_2_W8iktCfBBRyPflz26kYRQwItEDny0koUhubhSUiqZr_DloPKD-vwhCCz3SmCU3xQ-32ZoI9Oo0YFNDAagAs2SwKBS5qKeGOXljZv5Sc5nKZKKvJmzb_sG9X_KP28p0shMk17VJ-mauKMdgjToNMZtI8CoPxwhB5_MIpuO3bjZjgX5F8CxR5E_Mg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baNMu9wI5MC5oKHuDiYfNxr8mUCm6by_AKWmVwsitxAaU4H4w9i2O9q7J78WSS4nJsHS46cYwvcEZekIzVkkep1JlUM-3EYxYCeL_lLUGWbxJ0JckjJqS1YeFsEWtNivJW1FNoyytY3tzKfRtoURKrtvNA7k4OeyxAxxBgRE6zw5exfLMq75bz4uyDPT0XY9ONE7Hpi1L0Y33W6Tj5Zh1XkApa06BNZuiQgcnn2CP5N6sw1sRz6e70HG5_F3M5dJeQMZqa8gCqI_c1-NpHghHcgPa8WG388B_3qrJ8NN9D0wAIE6PJg2meZh6meH9Y3nLggBeAJvfR46C3cDqYNqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEiuR4XRQ8713XBAd56l9d1FWkxeq58DQBFp4Q3ugKe3-pgWRD7fh48IlOoNnZtHvaUMwm--WcnpxDNfG2WgDSElh3eu5klURSqr5KE-FlGNa6WrMJRfUZKO2VqLEEqwSnwigPeN4NTJPO5nMsr8S8eKyr2E5NRfF4EtgHfHzXbcVAitVfPSNs2zuXSdbrx7BQYgVIp8GvVP5bE22L9UU4gpUcQKV5FxVfTmAACGgJYSj7GXpUoiC9xHJbHSTxXmPFNfdgNSGlTwxMcRcHUDELDFOF_F9aBzLTxrw3aB20WxxoiO1x5bRqXFgXEtKiN3OlCyOycjxBBuWYIUo8SLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4Rba6zTtg_xlTVBIgbUyfYcwAIXtFaePTqUoHGeXo-5dB5fOqlMtaDoe_OD1AmNMYAOtI5y1ejj089EWMs3eWsyjUldTqXW_KoX9hVmR9JyqCInpqwkzJyb65vL5BjlseYYZBNSXT5wc3x9U_Gmq1vnxLNU8m_JHWGpZbN7ZiJ7QdBDlWY6OXjta4I9k3u6fUEwMuMt50TDDlASJf9e_42eOv_GpSf5EiNe4v54PNITbs-UKzim-kFcbvEgh0yx7JueanFSpXywciF6d82USHfHdCQY5Nnkd-ME3mcEzR-uLa1WX9vMvAePzofSojf3993wPktxJGKctvWA-s5BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGETAaVtlLwdCJ9Fb2r2PKd5v8o45B79eVivmBGgZVXzK1cGvuruhWrbuujezOWi5DtkevlswoEOYj07zJeV7m0pwrIKNCn-uXebfPZHF8aOmP9aRz0IXb60v7hwEzFuO4pMm2grvc_T0E0LDtnu6KokMJaq8pZQeAIShZvoC7QYFleuD2p3OvKyvj8DZPCoXZ4uT_04efwwUPC8E6TbKa4mczPyD1OJZ0s2gR9wN_TA0II3k82V3CZmC3ouA67wJQAFtfQdC9phnMQIQ7Lsc8gNmkmSGzNwtwhQ_c-WU4e3fzYQYedso9C7IEFinISV8BNCEcrs1uG1cmVIHHRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugy9CHeRMwhswj8wdorT0pyTNmpq_9ckN8N5x3Ex0k0DjlPLinvE_0-nfkT1otp8HW-hSY39VspuPSVoqDaJO7a6vjYtr7IG8QIYYrTS8iZ9jnqf1_7HFTFJg7xL4tcQv6Ik8eDQ8qPzNExjAQX-FHx6cbU1GpxZb_TLwNIzIBPKR5EAIQEnTlPi-rbIdu_ce7cFDuR6IlNTtC3syFIC8lHexuMi9YqquVetKPTe_YYwYFnNmSvxgLkNMANCGFBXXus_1JwDtaUOsFmjI2KVGkLufWASN_OqEnujbga2GNovqtyZMlwBCQ4VKR3maVNa_QqSUtHngEDQ7w2Q8MTQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_PCZwOc5dsS_3BKOdz5kY-vh_LJANnYVs0DxAzu8CqWpHHX_dbRlbpxuZINAf_kBl4ZuAef13t98svRshccSVMLOdOlzdjzGzuxITqJNmUxbDN7A3sibIL-M9uKbia20uL9lPW9Xcm8ZSJHZhYMLYGtsE7QL2-5aSQQyiEEMGH35B5U7KsXpo4B9t6a9EUeLBc5iznxBkSN8XWvT1E96UtTLIKWkkFVN6S0awhgf75DpATyUhj1iZhMVs9tny_W-pN73IqeeNHAMsnWFyEKxiU63ZUFngSishbYTygoFyBeS8WeK22I35F38WebfdlKdFxiJcMDr-1M9OCiXYr4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVR1Iq0a3eFoGGc0ZRQLmUoqu7rfNfVer4GNgM_uFwAbLxu639KdniOz29__vKhtVru19kEeq8QNZy8NZZx2selXVBesl7u0cDm6DJ2pAWE9lF4nklLlYWZ1TqMhmLwfdxqcGAjfVu_K_63m4eUK0Y7_anldWArCJeNgmG8x236htXczuwzbdZXlIGioc6H8lBIdDtC_raqkWt7CKo3aNI3zEOoLpYPS-CiHOZzlrczrJ2sckJjACxIzQW8l38CurD88wIYprcHlb9weJAtWyHlq7wUgzBzxEAOmdndeciv3EiWoiYHDkBwPG6LvAPY1lUQdZpej4cRmWS8NyM-W4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sX3PC3qKj9dVBjU7DrHpEwl8YbcvML7KI4g8aPxz4YBajMZhLiZO_r-n25ymyuTmJgDhVQMRLvrzeVnQDsXkGlnqy96TyCTsZR0xEcTi9KDjFpTLNFUoaodamh4vng8Xy0VGB7_3JcH1b2fQHm__FEtmWQINlnQnq6GLVQyrQSs7G_YKYQYwJO6n7Gt13WCzLw6jchzUEkFTAtnxT-8UJDJ_TEbKB0s2lWVQLIbLs6zWyelxchjLc8DH_DvuvarCjmvYkZXbNujLxczzSXkK7kTiueIyA42gLX7d4jNyo73gh5kTFfrjtlagWDp4LBp1tVJA2gYA3k9JtVZSnE2Xmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445931" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhPPMu2U4GXIW2PRox4KCIEhTRCLGMo0luxXftBaikF9SWQqbVkEMgvecxgjV-jxI7aJRhmk9gXYYDnlKcQ-crTPNWe9Q1g9U9FBZPUqu4D5MepYhB-Zvcz7qfvO0MNh8qzgabUGcT9_6wqVCFCINfiXBxVzG7wwe7umk-RJDeRgEQCugaO_C1YDZ8cvTmFMQxzTityRwBKROWrTWHQN19b8in0qyAh7zhYDUQnEpzmpvgBE33MzeUFo-aC5rN65llF3ZMZQyDlXY8Q5jd1hNwofKmx_b0jx6JqWrLlOf_Inf9g0IMqZ3JKetiWALJQaOadZZxjc2M4p2B9beB4rGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهدای اراضی فلسطینی برای ساخت سفارت آمریکا به قیمت ۱ دلار
🔹
رژیم صهیونیستی و آمریکا توافقنامه‌ای را امضا کردند تا سفارت آمریکا در قدس اشغالی ساخته شود.
🔹
به گفتۀ سفیر آمریکا در اراضی اشغالی، قرارداد اجارهٔ این زمین برای ۹۹ سال است و ایالات متحده مبلغ ۱ دلار را به اسرائیل پرداخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445930" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb8gATv_jxk7qB2qcqjvzTbFM_P7AKFgVE-fszocRk-hG4Z_ES_ycDHKTYW14qhegFg29hHS8yJL3ElaTEPqiCoUFGlZhSN2sY9BEovPs445v7HUHKKMTWQBnHMJmpUI2Ju8k7dkg4z9ncCQVlv_5G5sOvxDRSLYaB1lChUC8VKWIPKFu2rvscljK0Vb7A_qU99Y7DxRVK8lI9spn8CzJ8EaNwrmfArb2nVGLcDH6yyQA7gtHS8Cz6x_wySUMlcPncWzPC9kp9OBM_Qn6Xdy1TpS5MBspVj5G_3lVnop5dYIna0xW6jMUXUP1vMjmtrwIcmMI8tpi3va-gjbB2zm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفرهٔ شراب
🔹
«منصور دوانیقی» خلیفه عباسی سفره اطعام بزرگی پهن کرد و بزرگان، اشراف و شخصیت‌های برجسته مدینه و جهان اسلام، از جمله امام صادق(ع) را به این مهمانی دعوت کرد.
🔹
امام صادق(ع) بر سر سفره نشسته بودند که یکی از حاضران درخواست آب کرد. اما خدمتکار به‌جای آب، ظرفی از شراب را آورد و به آن مرد داد.
🔹
به‌محض اینکه ظرف شراب در سفره قرار گرفت، امام صادق(ع) بدون هیچ‌گونه درنگ یا ترس از ابهت حکومت خلیفه، بلافاصله از سر سفره بلند شدند و مجلس را ترک کردند.
🔹
هرچه منصور و دیگران اصرار کردند که ایشان بمانند، امام قبول نکردند و در پاسخ به این رفتار فرمودند: رسول خدا(ص) فرموده‌اند: ملعون است و از رحمت خدا دور، کسی که بر سر سفره‌ای بنشیند که در آن شراب نوشیده می‌شود.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445929" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری برای رهبر شهید در اجتماع مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/445928" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🔹
ممبینی، دبیرکل فدراسیون فوتبال: از AFC درخواست تمدید مهلت معرفی نماینده را کرده‌ایم اما درصورت موافقت نکردن کنفدراسیون، نماینده ایران بر اساس جدول لیگ معرفی خواهد شد که گل‌گهر خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445926" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
امشب طوفان گردوخاک هم مانع از نمایش غیرت میبدی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445925" target="_blank">📅 23:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض سحر امامی هنگام سخن‌گفتن از تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445924" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها بازهم تا پاسی از شب در خیابان‌ها برای دفاع از ایران حاضر هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/445923" target="_blank">📅 23:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ2LlairVBF0HG-GH4F48WAEciTFDbt_n51EUpgroT0Cv6cRpI0Y9tXLa59BZeaOkQF75ipZ3aL9Q8DtoioZ0r2XWj8-DYLvaS7DwUFlhUtf2bh9FOE07NaG-iU9pzbcz4upROo1mw0_j_j7hfZk7Kb27XMwDgi_bFYoLSrKLBoBxBi3gDd8lm3HxBdLafqR_e4sTlJLBgHLea-33SYJex7FxkKxcYuXNWB-x6HBX4jKbCX3w_NvXGkyQqeGqLBw90AnzMZgih9EWd-nTs_r4d99ow4GKMbB3bV87Lz5uro2gBiLruHIUhrOpd5MDBwK2f4v-KYFpGD7rU3CR3Q6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات مشکوک اسرائیل در شاخ آفریقا
🔹
شبکه المیادین گزارش داده که اسرائیل محموله‌ای مشکوک به وزن هزار کیلوگرم را به سومالی ارسال کرده است.
🔹
المیادین به نقل از منابع آگاه خود افزود که اطلاعات موجود حاکی از آن است که این محموله شامل سامانه ارتباطی پیشرفته و مدرن با کاربردهای اطلاعاتی ـ نظامی بوده است.
🔸
رژیم صهیونیستی و منطقه جدایی‌طلب «سومالی‌لند» حدود ۲ هفته پیش رسما افتتاح سفارت این منطقه در قدس اشغالی را اعلام کردند.
🔸
الحوثی، رهبر انصارالله یمن هم یک هفته پیش گفت
که یمن در قبال هرگونه حضور و استقرار احتمالی صهیونیست‌ها در سومالی‌لند که در فاصلۀ اندکی از خاک یمن دارد، دست روی دست نخواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445922" target="_blank">📅 23:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk-Iq0U6QhHkBJNunM0v2nYSIGExwXJDQVhH421Q5KTW-u4cvEnESCn4kBstu3ED43ufQcKytvKj-vtc7SfKtdN0e6uet9dpGDVOpW2tZ9qlnb_0M806p3LOKRrYr9atOzjs2ER2IWd-7piWNyGj4qe_9HMVYrNcR8cFXUzEhhV77q1SkVKidu5UMkOjGaIw8arSr7IppYacBu91ht3CtANUNiqhXGXdPv8gU4ZYvQ965Y_SHoc06NRUG1pn9X3B5eUNZ1-5UPMalZtcaYjh9XUmok6sZltyj-RDT35RT2k-rB6ajQb-t900oAALNeNPYsxaSsjCmo-w8vUtSbpw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصرار دولتمردان لبنانی به تداوم مذاکرات سازشکارانه با اسرائیل
🔹
نواف سلام،  نخست‌وزیر لبنان گفته لبنان همچنان به‌دنبال  یک چارچوب توجیهی و مقدماتی برای مذاکرات است که مسیر گفت‌وگوها را مشخص می‌کند و هدف آن رسیدن به یک توافق نهایی است.
🔹
نخست‌وزیر لبنان اظهار داشت که اگر «چارچوب» اجرایی شود، منجر به عقب‌نشینی اسرائیل از مناطق اشغالی و بازگشت اهالی آواره شده به روستاها و خانه‌هایشان خواهد شد.
🔸
این سخنان نخست‌وزیر لبنان درحالی است که سران رژیم صهیونیستی از جمله نتانیاهو و کاتز در روزهای گذشته چندین‌بار به صراحت اعلام کردند که از منطقه امنیتی در جنوب لبنان به هیچ عنوان عقب‌نشینی نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445920" target="_blank">📅 23:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما و سوئز باید برای ما رایگان شود
🔹
رئیس‌جمهور آمریکا در اظهار نظر جنجالی دیگری گفت: کشتی‌های نظامی و تجاری آمریکایی باید اجازۀ عبور رایگان از کانال‌های پاناما و سوئز را داشته باشند.
🔹
ترامپ افزود: از روبیو خواستم فوراً دستور عبور رایگان کشتی‌های…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445919" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jka_cwTwM5Ji6fnwae-SGWHIXDV0ByeBR1vI6cIfFzpCd5zf-al4EvHOt912u4UDfSfGgdKUSSl4AZjPZGUJyz17dapCxFsR3_I_FbM8rKELt0uEdeUxFRbRrUn5OQMamfRPUgyWdNgjemfpW-RhgJGdnPMMajGzTG-yd7NAWw9XLgMd8qNk_i6OCZcXpSY925yiMfJtTeb0vrlF_kI-rsWqEVJ9x5EonSdJ4IGT_ODDKGoR1lJ2nleautzBupNBgP7nlST4Puzbq9LoIrj5uD0Y8k8elPnKXrkcKBWzsHCUSlkf8_RF7iB1XfgY31iJupL76Cfecz5UIrUj0GNVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان انحصار دبی در تجارت خارجی ایران فرا رسید
🔹
جنگ اخیر و اختلال در تجارت دریایی، یک واقعیت مهم را دوباره یادآوری کرد که اقتصاد ایران نباید به یک مسیر و یک کشور وابسته بماند.
🔹
پل‌مه، دبیر انجمن کشتیرانی، دراین‌باره می‌گوید با کاهش تنش‌ها و بازگشت ترددهای دریایی، مسیرهای تجاری بین ایران و امارات دوباره به راه افتاده اما ایران نباید مانند گذشته تمام ظرفیت تجاری خود را در این کشور متمرکز کند.
🔹
او می‌گوید توقف کامل تجارت از مسیر امارات به دلیل مشکلاتی که برای فعالیت‌های اقتصادی جنوب کشور ایجاد می‌کند، امکان‌پذیر نیست اما می‌توان با توافقاتی با سایر همسایگان مثل پاکستان، عمان و عراق وابستگی تجاری ایران به امارات را کاهش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445918" target="_blank">📅 23:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بحث دسترسی بازرسان آژانس به سایت‌های بمباران‌شده کذب است
🔹
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای‌عالی امنیت ملی تعیین کرده، نمی‌دهیم.
🔹
طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای‌عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔹
در…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445917" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: هیچ خیمه‌ای جز خیمه ولایت، خیمه امیرالمؤمنین نیست
🔹
من وظیفه دارم برای همه مردم ایران که با هر سلیقه و دین در سایه جمهوری اسلامی زندگی می‌کنند، نوکری کنم. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445916" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: کسانی هستند که نه در دیپلماسی به کشور کمک می‌کنند و نه در جنگ اما من ایستاده‌ام تا هم بجنگم و هم دیپلماسی را انجام دهم
🔹
بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید و اجازه دهید مردم آرامش داشته باشند و به جمهوری اسلامی افتخار کنند.…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/445915" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌. @Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/445914" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
آستان قدس رضوی: در خصوص موضوع محل تدفین پیکر قائد شهید، آستان تمامی تمهیدات لازم را اندیشیده و پس از تصمیم‌گیری نهایی توسط بیت شریف ایشان، جزئیات آن به استحضار ملت عزیزمان خواهد رسید.‌
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/445913" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔸
قالیباف: واقعاً هیچ. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445912" target="_blank">📅 22:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری بروجردی‌ها برای رهبر شهید در شب ۱۲۳ حماسه مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445911" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین پیام از طرف مردم به آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/445910" target="_blank">📅 22:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
نماهنگی به زبان کردی که اهالی کردستان عراق به رهبر شهید انقلاب تقدیم کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/445909" target="_blank">📅 22:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📷
بازگشت بازیکنان تیم ملی به کشور  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/445908" target="_blank">📅 22:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد اسکان شهرداری تهران در برنامه پرچمدار: در تمام بوستان‌های تهران برای اسکان زائران مراسم تشییع رهبر شهید، امکانات مهیا می‌شود
🔹
هلال‌احمر قرار است در فضاهای باز شهر تهران مثل پارک‌ها، برای ۲ میلیون نفر چادر بزند.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/445907" target="_blank">📅 22:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیه‌های ضروری برای حضور سالمندان، کودکان، مادران باردار و بیماران خاص در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/445906" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای قطع مصاحبۀ قالیباف در شبکۀ خبر
🔹
مصاحبۀ محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در گفت‌وگوی ویژۀ خبری صداوسیما پیش از پایان کامل سخنان او متوقف شد.
🔹
هم‌زمان، کانال رسمی آقای قالیباف نیز با انتشار پیامی از قطع شدن این گفت‌وگو خبر داد. این موضوع واکنش‌ها…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445905" target="_blank">📅 22:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
خداحافظ ای مه‍ربان رهبرم
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445904" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: همهٔ شما فرزندان من هستید، به معنای واقعی کلمه دعایتان می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445903" target="_blank">📅 21:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما همان ملت مبعوثیم که خیابان‌ها را عرصه رزمایش اراده‌ها کرده‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/445902" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌  پزشکیان: باور من نسبت به جایگاه رهبری مبتنی بر عقل و اعتقاد است
🔹
باور من نسبت به جایگاه رهبری صرفاً یک باور احساسی یا تعبدی نیست، بلکه مبتنی بر درک و اعتقاد علمی و عقلانی است. در طول سال‌هایی که در مسئولیت‌های مختلف حضور داشته‌ام، همواره از هدایت‌ها، حمایت‌ها…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445901" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
در جریان تصمیم‌گیری برای مذاکرات رهبری عالی‌قدر فرمودند که اگر سه‌چهارم اعضای شورای عالی امنیت ملی رای مثبت دادند همین روند را در پیش بگیرید که در جلسه‌ای که برگزار شد از ۱۳ نفر، ۱۲ نفر صرفاً…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445900" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
در جریان تصمیم‌گیری برای مذاکرات رهبری عالی‌قدر فرمودند که اگر سه‌چهارم اعضای شورای عالی امنیت ملی رای مثبت دادند همین روند را در پیش بگیرید که در جلسه‌ای که برگزار شد از ۱۳ نفر، ۱۲ نفر صرفاً رای مثبت ندادند بلکه بحث و تبادل نظر کردند و قاطعانه حمایت کردند.
🔹
امروز عده‌ای دولت را متهم می‌کنند که شما از نظر رهبری اطاعت نکرده‌اید، درحالیکه قطعاً اگر ایشان دستور می‌دادند جلسه و مذاکره‌ای صورت نگیرد، نه جلسه می‌گذاشتیم و نه مذاکره‌ای صورت می‌گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445899" target="_blank">📅 21:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f146f4f970.mp4?token=dqRQS-qzf_bQTRQkMjHH6LTdzObVDA_6v0HiFkCHjNq_AIOkgUm2SP1HE6Pdu5CdStM6ka7njJUrdWu_UDPgA56XnS4z4ZC_XI6rnaBKL54jKtQO4wkBlA6-mwz65JW5wPRSs4ogEZuPBxfIJplE1scRkgQlij5VylSnxUQV3UrmRxziTDxtoOHS1Ui7k79SrKRGG2z3w4JO6OfH4i75ddJYEqBKP9Z-zw8gBn_rUAi6iWnAeTZRvcEQdLgqH-x8KzCwpFu5jDJSd2h8VPyuGFhiev-ksM9S_zO3gG_ibzZRhLHBuCJ9jHnKHfU-kVJam4suWV-RJYt3pv0ev3vjSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f146f4f970.mp4?token=dqRQS-qzf_bQTRQkMjHH6LTdzObVDA_6v0HiFkCHjNq_AIOkgUm2SP1HE6Pdu5CdStM6ka7njJUrdWu_UDPgA56XnS4z4ZC_XI6rnaBKL54jKtQO4wkBlA6-mwz65JW5wPRSs4ogEZuPBxfIJplE1scRkgQlij5VylSnxUQV3UrmRxziTDxtoOHS1Ui7k79SrKRGG2z3w4JO6OfH4i75ddJYEqBKP9Z-zw8gBn_rUAi6iWnAeTZRvcEQdLgqH-x8KzCwpFu5jDJSd2h8VPyuGFhiev-ksM9S_zO3gG_ibzZRhLHBuCJ9jHnKHfU-kVJam4suWV-RJYt3pv0ev3vjSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای حزن‌انگیز یاسوج در آستانۀ وداعی تاریخی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445898" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پزشکیان: دفاع از نیروهای مسلح وظیفهٔ من است و با تمام توان از آنان حمایت خواهم کرد
🔹
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند.
🔹
بنده معتقدم اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد و به این حمایت افتخار می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445897" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رهبر انقلاب درگذشت پدر دبیر شورای‌عالی امنیت ملی را تسلیت گفتند
🔹
متن پیام رهبر انقلاب اسلامی به این شرح است:
بسم الله الرّحمن الرّحیم
🔹
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر حفظه‌الله‌وایّده؛ سلام علیکم و رحمه‌الله و برکاته
🔹
خبر رحلت والد معظّم حضرتعالی واصل شد. بدین‌وسیله مراتب تسلیت خود را تقدیم می‌نمایم. امیدوارم آن‌جناب در سایه‌ی پرمهر صاحبان این ایّام صلوات الله و سلامه علیهم اجمعین مورد رحمت واسعه الهیه واقع گردند.
🔹
همچنین آرزوی سلامتی و طول عمر با مزید توفیقات ظاهری و باطنی برای جنابعالی و سایر بازماندگان دارم.
سیدمجتبی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445896" target="_blank">📅 21:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ee6ef08.mp4?token=ebcP81mXqujiB7BduktPaZNOZFaE_w_XI0uczmAXqhxGUC0dn7l-7OGwX3t_Nq8TCS1fiPMyFcx_ysSbIY7UfTy3jCCbjv1XvnOx6avB6aHbhl1Z6oLF1vRSXUquCOpWktXvafYLKzHYTtJg2idYBTN8qLJq8_vjBh3U7HNnMY74hCCkxR26aqOGY_-TO-ojQbE4EY2XjwPBExqyrw5D58sNheUkNknL3OmnHUg1VjTEe9U71KY2yATKgJjfdggTGd8FPa3p7yumtSoTPpHd4ZcApmpLikAaDQVX_w6jGnFnWsws2kdSgRSQwCwhiMb2C4ECjGbAtvedjIVRv0xxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ee6ef08.mp4?token=ebcP81mXqujiB7BduktPaZNOZFaE_w_XI0uczmAXqhxGUC0dn7l-7OGwX3t_Nq8TCS1fiPMyFcx_ysSbIY7UfTy3jCCbjv1XvnOx6avB6aHbhl1Z6oLF1vRSXUquCOpWktXvafYLKzHYTtJg2idYBTN8qLJq8_vjBh3U7HNnMY74hCCkxR26aqOGY_-TO-ojQbE4EY2XjwPBExqyrw5D58sNheUkNknL3OmnHUg1VjTEe9U71KY2yATKgJjfdggTGd8FPa3p7yumtSoTPpHd4ZcApmpLikAaDQVX_w6jGnFnWsws2kdSgRSQwCwhiMb2C4ECjGbAtvedjIVRv0xxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش زدن مزارع و خانه‌های مردم لبنان در دو شهرک بیت‌یاحون و حدّاثا به دست صهیونیست‌ها
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/445895" target="_blank">📅 21:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ba789f78.mp4?token=bSnJFGpACuC2mH09EEgnB00DaBXh4Q6lmeoAtBaQvvghFd2nPBkv5tcYaLvGEwTyuiFIP87UtrF2QFqjrnMB9yUCFXtCf73cHho1zOVHqf9dhHPlTtp8vaOKLhAfj9asR6dsfw48sP1rQhf8jUrFfBIZiQK9os6lRJXSBKB5M6aiK_u5v9nG8oV7FfF4Dz7JyerQrWN9PbAoR8Ur7Pnzm7F-0LL6JjNsVBJC_ykxv01HTRcnA8pamxuSN1Ge738utxzzrTRbvfs6jt4V8aONwjMzHJXQjwxoU4ZOlNPMw3mMfeCCs21AgXQU7Mf8T8nbJnWrACqyvkaDh5CFEqdeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ba789f78.mp4?token=bSnJFGpACuC2mH09EEgnB00DaBXh4Q6lmeoAtBaQvvghFd2nPBkv5tcYaLvGEwTyuiFIP87UtrF2QFqjrnMB9yUCFXtCf73cHho1zOVHqf9dhHPlTtp8vaOKLhAfj9asR6dsfw48sP1rQhf8jUrFfBIZiQK9os6lRJXSBKB5M6aiK_u5v9nG8oV7FfF4Dz7JyerQrWN9PbAoR8Ur7Pnzm7F-0LL6JjNsVBJC_ykxv01HTRcnA8pamxuSN1Ge738utxzzrTRbvfs6jt4V8aONwjMzHJXQjwxoU4ZOlNPMw3mMfeCCs21AgXQU7Mf8T8nbJnWrACqyvkaDh5CFEqdeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قفل دروازۀ کنگو بالاخره باز شد
🔹
گل اول انگلیس به کنگو توسط هری‌کین.
⚽️
انگلیس ۱ - ۱ کنگو @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/445894" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
از دفاع از فردوسی تا مجسمه والرین
🔹
رهبر شهید چگونه بزرگ‌ترین مدافع هویت و فرهنگ ایرانی بود؟
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/445893" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a246913bf1.mp4?token=XOmE05aML4mM4mfiaeQSEjyNPECK5tUsbXPtw25lOX1_kFdkI90kpLFn8qY7apHYAozCHEkrmNMYxfksZG5KLDDPQzkxEjdVgNGhLDv14G7w2CbZ8exwj57yTMt7S4rqZmJGhIe2_74BXB_TnTQX5DePtEYY2RNPxUfzvyWeFZbNe5Sh0xBDzzrKNVeKjBXjiLl1_Zrxpffei2DO7LThKp3vUm0PU9QSHh0vKJ-p0jpSOh9jIcLRx1CpiIrb9_vsBKJG0FNWgmn90B5yBZV2yO1slVqL0sW13MF88h1WpHgy9OWFpx4LawUJextK8vxnakAd7t75ld4tgTqwThK_6q0oAoWP51_wVRJteOCzyCaEman_BLtmlkAQIPhreuFqw8MNqXZZVevK_fJYO0o-x3p7Ki2gSJcg0_bZvCWDCjEk_evjNTqinab7b4RPM98jdNtB_UwbjlrD9ScRxEd6Ny1pXaB5XZoRxidl0A9hvykIIBWKMFdnymlE_N1fqrdeZLeqB2tnnUMfVaCaM8xWHRTnnDdIuYfvppD0kfEGnh3rZHrpPzqbjVIHHHk-Qh4iTsQjjIgUxHi9DtD1nJ5L_fQpr8QnU86ieYAtLyOOnC4q6zGBLCyF0_I8Pp76c2LOUJO3Pm2jVJoOKuTAQTIUmQuCnxap177vosIbtC2W-os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a246913bf1.mp4?token=XOmE05aML4mM4mfiaeQSEjyNPECK5tUsbXPtw25lOX1_kFdkI90kpLFn8qY7apHYAozCHEkrmNMYxfksZG5KLDDPQzkxEjdVgNGhLDv14G7w2CbZ8exwj57yTMt7S4rqZmJGhIe2_74BXB_TnTQX5DePtEYY2RNPxUfzvyWeFZbNe5Sh0xBDzzrKNVeKjBXjiLl1_Zrxpffei2DO7LThKp3vUm0PU9QSHh0vKJ-p0jpSOh9jIcLRx1CpiIrb9_vsBKJG0FNWgmn90B5yBZV2yO1slVqL0sW13MF88h1WpHgy9OWFpx4LawUJextK8vxnakAd7t75ld4tgTqwThK_6q0oAoWP51_wVRJteOCzyCaEman_BLtmlkAQIPhreuFqw8MNqXZZVevK_fJYO0o-x3p7Ki2gSJcg0_bZvCWDCjEk_evjNTqinab7b4RPM98jdNtB_UwbjlrD9ScRxEd6Ny1pXaB5XZoRxidl0A9hvykIIBWKMFdnymlE_N1fqrdeZLeqB2tnnUMfVaCaM8xWHRTnnDdIuYfvppD0kfEGnh3rZHrpPzqbjVIHHHk-Qh4iTsQjjIgUxHi9DtD1nJ5L_fQpr8QnU86ieYAtLyOOnC4q6zGBLCyF0_I8Pp76c2LOUJO3Pm2jVJoOKuTAQTIUmQuCnxap177vosIbtC2W-os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاکمیت ایران بر تنگه هرمز هر روز بیشتر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/445892" target="_blank">📅 21:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f292d12ed5.mp4?token=CXt0u57Vl17iaA5AcppG33ZXS2KhPzch1xWjE14XIqwCnf6Tn-MFPz34YivKFljuaBT9P9n4jwHNHN8BpNMsogNvS5riKyo05_ZMZEH4FMjnvyJNcR_TrNPTbJbvOPsAkW85dhu3RHtN_HbiDe74yjVwKN7m_Pb3xMGHY_uXOiztJkx9Ej9nVYS9B_s0VngkXqsiQZ1MNnQLnSfbQfmA_deyYriYg32kz9Q7acoZWZlvojo6mcF69Iz9n46MBH8HViJ569jHG31pRGyO5ct9nuPtHoh8pQyIUmSKUOHnKuGqozPxUYrn3ZOmfTBx9uCl0HH9kBfFqrHs_SsFxJWpEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f292d12ed5.mp4?token=CXt0u57Vl17iaA5AcppG33ZXS2KhPzch1xWjE14XIqwCnf6Tn-MFPz34YivKFljuaBT9P9n4jwHNHN8BpNMsogNvS5riKyo05_ZMZEH4FMjnvyJNcR_TrNPTbJbvOPsAkW85dhu3RHtN_HbiDe74yjVwKN7m_Pb3xMGHY_uXOiztJkx9Ej9nVYS9B_s0VngkXqsiQZ1MNnQLnSfbQfmA_deyYriYg32kz9Q7acoZWZlvojo6mcF69Iz9n46MBH8HViJ569jHG31pRGyO5ct9nuPtHoh8pQyIUmSKUOHnKuGqozPxUYrn3ZOmfTBx9uCl0HH9kBfFqrHs_SsFxJWpEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنگو از انگلیس پیش افتاد!
⚽️
انگلیس ۰ - ۱ کنگو @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/445891" target="_blank">📅 21:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b78f01e3.mp4?token=c5ySgxa4fLDutQHQuS2PqF0w4Kxh3gZ6-7-B4_NAjyUgzZUn2idJ8t9htiIz_nCC8ER6MizTCakjleRePyZUeQBLaxsH_QDn6HNUxlMwnGCDKYoEMxT8qFCBK8uQVW5bsaoPtwxKCW3aDNoJqd1QObi0boFG3DfwU8x8C46GUQYVT5BUUsJI8k0fYLfvWQIDIpqrSkf7n_cj3FjxR_lfaRknzZfHCN-7-_sfyd6j3ofkGv_Pip2LVucPe9kaJK7o6LZY6i3LHVlvFjXhrIpsiwJPjUYvMtOQbdrfrsQLOQAhrrZSfFaEaFBeKRnwYgiuCXvfIAzEa-GRJeSNWgRSTKvQv5I5sPN6JtEVmqd_nXbdAIk3pnPawHODJCYHQB47fUUMQB6wDpvfhj5F3ThtmzpKgwn7wBgSPk6okE07ZIoZuJWvnapFGe-Uy1tIxNSjRr-BhshXVrrScTVvZY4xtD8DHTD-Srxhcxon9wjtkqoMfPHrNjUFmYOjTifJPoxL_uGoDHclrQ5Ri5G1jzgSQgb7tyq3EI_VEIHT-OSpnkilhMWrUl6LwsABap8hlOoKpsH_KwiH4Vrd0LNDsXiN0hO-LonlDpBxfK03PM408vSnAFpn07u2GAy06qi59hPg8HjvUwpaA7EH9GGmM_N4kY6qYfvcodRM9i9lmZj_lC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b78f01e3.mp4?token=c5ySgxa4fLDutQHQuS2PqF0w4Kxh3gZ6-7-B4_NAjyUgzZUn2idJ8t9htiIz_nCC8ER6MizTCakjleRePyZUeQBLaxsH_QDn6HNUxlMwnGCDKYoEMxT8qFCBK8uQVW5bsaoPtwxKCW3aDNoJqd1QObi0boFG3DfwU8x8C46GUQYVT5BUUsJI8k0fYLfvWQIDIpqrSkf7n_cj3FjxR_lfaRknzZfHCN-7-_sfyd6j3ofkGv_Pip2LVucPe9kaJK7o6LZY6i3LHVlvFjXhrIpsiwJPjUYvMtOQbdrfrsQLOQAhrrZSfFaEaFBeKRnwYgiuCXvfIAzEa-GRJeSNWgRSTKvQv5I5sPN6JtEVmqd_nXbdAIk3pnPawHODJCYHQB47fUUMQB6wDpvfhj5F3ThtmzpKgwn7wBgSPk6okE07ZIoZuJWvnapFGe-Uy1tIxNSjRr-BhshXVrrScTVvZY4xtD8DHTD-Srxhcxon9wjtkqoMfPHrNjUFmYOjTifJPoxL_uGoDHclrQ5Ri5G1jzgSQgb7tyq3EI_VEIHT-OSpnkilhMWrUl6LwsABap8hlOoKpsH_KwiH4Vrd0LNDsXiN0hO-LonlDpBxfK03PM408vSnAFpn07u2GAy06qi59hPg8HjvUwpaA7EH9GGmM_N4kY6qYfvcodRM9i9lmZj_lC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیه‌هایی برای حضور در مراسم تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/445890" target="_blank">📅 21:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هشدار پلیس دربارۀ فریب با وعده رزرو اقامت و پارکینگ برای مراسم تشییع
🔹
پلیس فتا: عزاداران در ایام مراسم وداع، تشییع و تدفین پیکر مطهر قائد عزیز شهید، مراقب لینک‌های جعلی رزرو اقامت، پارکینگ یا دریافت بلیت باشند و به لینک‌های مشکوک در پیامک یا شبکه‌های اجتماعی اعتماد نکنند.
🔸
موارد مشکوک را به شماره ۰۹۶۳۸۰ یا سایت
پلیس فتا
گزارش کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/445889" target="_blank">📅 20:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44719355c2.mp4?token=RkXmncZJMf9wYGsUB7MXBDxiYdb5fTbPwYEEfvJUegJWUseRgkt-VNql1F6prdy7mYwuQFPfvP71rpG05AcUGRgbNAXpWalooyPyaeS_40dU6lmtjRTqhcnsYHOBvQAiYgbDg0uG33-mxmWXgwVXl68l1ac7lMYeR-vi2Vp1ZZr34ZS6_04bVhodETmM4uO3fgP2eHdiklrWccOH-MbaVIYaHUkz6FdDDKNEWq2wdGNN9rP_PUalqhi4Yb0fxZyDNQ3rGbfE1lw9N8wrUVqrTuetoLIdMpWOaRcwsl_gwOzLCKko9s4KaMahLGoKY17DcrYzNFmKF9-KixTHPWB-gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44719355c2.mp4?token=RkXmncZJMf9wYGsUB7MXBDxiYdb5fTbPwYEEfvJUegJWUseRgkt-VNql1F6prdy7mYwuQFPfvP71rpG05AcUGRgbNAXpWalooyPyaeS_40dU6lmtjRTqhcnsYHOBvQAiYgbDg0uG33-mxmWXgwVXl68l1ac7lMYeR-vi2Vp1ZZr34ZS6_04bVhodETmM4uO3fgP2eHdiklrWccOH-MbaVIYaHUkz6FdDDKNEWq2wdGNN9rP_PUalqhi4Yb0fxZyDNQ3rGbfE1lw9N8wrUVqrTuetoLIdMpWOaRcwsl_gwOzLCKko9s4KaMahLGoKY17DcrYzNFmKF9-KixTHPWB-gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاقبت بی‌توجهی به فرامین ایران در تنگه هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/445888" target="_blank">📅 20:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b1f2f281.mp4?token=A4nPwyAjE9W4LM6_wfvJQohE6Oz2HKUUPYTF9WDBe7kE3UxhmVp6qAVbS8N1CUOIJLLSli7dwZc16p9_ISTrotAkbhf9EfJS4ITO4T5phJj64CwthKAQGlaOxoyGae-3Q-7wfMAEBGcGgp9wv-OtrfT_CzRyTMASWxGqvOr5nLxhQeBz2fKPEOMKBkR6_kwF-gHX-Ln_S_akNbwyeVYcUpP-FORUY0k9cskAWlUAFWwsooaOaJ8wnvkPa3ihAsotsDPbqKeVeVSJhe6H3GscfrBhhkuWZk_sNZS8KlLIhLPUTe9-_WDa-tgEQtbYyCQyxHb50S39NhP75VV2HHLYh44dRsuYiebon5ISs841eS9lkBjDPTPU2ZCu42UiqZgbq0pFcSJzQw4MTXA1aV55VmdI0YzrqqW1gOsHfbq2SogeY6mVT19vZ9j34h-AaT7aFEHqxAriapMADcHZIuS25ARiuCR7ZmRMtWUR41X5npFGwYLxD4e26cemnu7QvzDj5UnRrz3gkdxWlNyjO96D9QZYUwGPj_psOT3Oj0_l0Y5WPNhlFloYwncoVpuLzOlkcdh9ZXuwOwbCYIuXysgJcQgPUSI9m9ffE0_qoArGFvn5i10iRl-YSkA7Qjxe81ip_pfo5Wzbj8_902ZIFg0h5oPCo_pU8FL4iVu7hgfj1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b1f2f281.mp4?token=A4nPwyAjE9W4LM6_wfvJQohE6Oz2HKUUPYTF9WDBe7kE3UxhmVp6qAVbS8N1CUOIJLLSli7dwZc16p9_ISTrotAkbhf9EfJS4ITO4T5phJj64CwthKAQGlaOxoyGae-3Q-7wfMAEBGcGgp9wv-OtrfT_CzRyTMASWxGqvOr5nLxhQeBz2fKPEOMKBkR6_kwF-gHX-Ln_S_akNbwyeVYcUpP-FORUY0k9cskAWlUAFWwsooaOaJ8wnvkPa3ihAsotsDPbqKeVeVSJhe6H3GscfrBhhkuWZk_sNZS8KlLIhLPUTe9-_WDa-tgEQtbYyCQyxHb50S39NhP75VV2HHLYh44dRsuYiebon5ISs841eS9lkBjDPTPU2ZCu42UiqZgbq0pFcSJzQw4MTXA1aV55VmdI0YzrqqW1gOsHfbq2SogeY6mVT19vZ9j34h-AaT7aFEHqxAriapMADcHZIuS25ARiuCR7ZmRMtWUR41X5npFGwYLxD4e26cemnu7QvzDj5UnRrz3gkdxWlNyjO96D9QZYUwGPj_psOT3Oj0_l0Y5WPNhlFloYwncoVpuLzOlkcdh9ZXuwOwbCYIuXysgJcQgPUSI9m9ffE0_qoArGFvn5i10iRl-YSkA7Qjxe81ip_pfo5Wzbj8_902ZIFg0h5oPCo_pU8FL4iVu7hgfj1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه برای آخرین دیدار با رهبر شهیدشان آماده می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/445887" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
ندانستم که این دریا چه موج خون‌فشان دارد...
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/445886" target="_blank">📅 20:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۲.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/445884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۱.pdf</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445884" target="_blank">📅 20:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cbb42bef.mp4?token=e2Lxft8q0dmBUc1hbvnLP0C8u1y4yyCb9kPLPRuqXuSuQGgohFrDEN6JhzsortcHSppeEc2f2NqK8_YSy8hst6L6XJs-8A9cw11Wp-G28j3_gDAkHVSFlWi2U-pTM5bHAxoQrdNYPyE-tchJiwiU-v7HolplF-G69VXtQlRVl3b-dZW1AeOYeoQciPnT11oFgM2pz9HVymqOQqTB5KPwx_pOUtuQXnDCv-K12SvhQZhjqSe7nD66JSq6lDBqQLb5ZyT-l9KmBUWTHCy5TJTbue0yx4SQ98l6XTtyhT7dPSPyUDtIPxPSq7GUs8szl_82P4p-zsGOIHf6NwS91Td-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cbb42bef.mp4?token=e2Lxft8q0dmBUc1hbvnLP0C8u1y4yyCb9kPLPRuqXuSuQGgohFrDEN6JhzsortcHSppeEc2f2NqK8_YSy8hst6L6XJs-8A9cw11Wp-G28j3_gDAkHVSFlWi2U-pTM5bHAxoQrdNYPyE-tchJiwiU-v7HolplF-G69VXtQlRVl3b-dZW1AeOYeoQciPnT11oFgM2pz9HVymqOQqTB5KPwx_pOUtuQXnDCv-K12SvhQZhjqSe7nD66JSq6lDBqQLb5ZyT-l9KmBUWTHCy5TJTbue0yx4SQ98l6XTtyhT7dPSPyUDtIPxPSq7GUs8szl_82P4p-zsGOIHf6NwS91Td-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنوب لبنان همچنان زیر آتش حملات اسرائیل
🔸
شبکهٔ المنار گزارش داد که رژیم صهیونیستی در ادامهٔ نقض تفاهم آتش‌بس، در حمله‌ای پهپادی، شهرک النبطیه الفوقا در جنوب لبنان را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/445883" target="_blank">📅 20:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5bec92ce.mp4?token=JMf1UI-WeVJhGlC3vHXvrQilp25nyRm2JkHvXpjDDqr3KfrALmQkslQ-GWhiesv9nIEXHAOXV8_ocxQO3sSWzh_NoPTd8hdGuxhRJAIZ7zZQJm-X0aXuAUr83nC696BaSvlx7sf3NlFM55XHlVpZ6XY0Bl2_dD6YHHXPBVuaQsHEOLtXdegMbwiEzKx33J3MIhWgdsSY0SltwzXV6LLKZyNe5d1GNwKrw7IGNk-eVaGuRoQ1-3Fby7dxNWJRtiR2oigQEPqEoMj0SN9yti1ANTB4jgxyKKpHaQKNliNF9VY5HqGtedLF-Og5EDeV3MRq_TzaB0RkOHLRRDpoIwu6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5bec92ce.mp4?token=JMf1UI-WeVJhGlC3vHXvrQilp25nyRm2JkHvXpjDDqr3KfrALmQkslQ-GWhiesv9nIEXHAOXV8_ocxQO3sSWzh_NoPTd8hdGuxhRJAIZ7zZQJm-X0aXuAUr83nC696BaSvlx7sf3NlFM55XHlVpZ6XY0Bl2_dD6YHHXPBVuaQsHEOLtXdegMbwiEzKx33J3MIhWgdsSY0SltwzXV6LLKZyNe5d1GNwKrw7IGNk-eVaGuRoQ1-3Fby7dxNWJRtiR2oigQEPqEoMj0SN9yti1ANTB4jgxyKKpHaQKNliNF9VY5HqGtedLF-Og5EDeV3MRq_TzaB0RkOHLRRDpoIwu6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران در برنامه پرچمدار: قرار است از همۀ مدارس تهران برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید استفاده شود
🔹
علاوه بر مدارس، مساجد، دانشگاه‌ها، ورزشگاه‌ها و سالن‌های ورزشی نیز برای این منظور پیش‌بینی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/445882" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c5e51114.mp4?token=TwHGaTaLeKuC1UMuFZfnk5hGSqfT34n7bua0tklZMGZw6-4saToakutaENZyFgEYUV62pJtwNhlFKx6QBX_5eKLqWxrticKtyqNvszbSGezuI-Evjwa-kQCBXXZnAQEsKhsTOm7fNgnmNcnAQUWnqyi3SjHCek10LNmxMim_xPCDHGPBACXFLaoBfX2dB7Gr5G1IxjUGxox4gpQo09YOrtAbCbs_VJo3_G4T52Y-c7dKHI8pJkN-AcgdkkMaavJg4_Vjn3wNSzcrF2klUzfdlNHgDENxkLRJd-Gnb8DWirwwlEME6WixuIYOmslw3evGqXrnHxrvFiHKu8oKscpJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c5e51114.mp4?token=TwHGaTaLeKuC1UMuFZfnk5hGSqfT34n7bua0tklZMGZw6-4saToakutaENZyFgEYUV62pJtwNhlFKx6QBX_5eKLqWxrticKtyqNvszbSGezuI-Evjwa-kQCBXXZnAQEsKhsTOm7fNgnmNcnAQUWnqyi3SjHCek10LNmxMim_xPCDHGPBACXFLaoBfX2dB7Gr5G1IxjUGxox4gpQo09YOrtAbCbs_VJo3_G4T52Y-c7dKHI8pJkN-AcgdkkMaavJg4_Vjn3wNSzcrF2klUzfdlNHgDENxkLRJd-Gnb8DWirwwlEME6WixuIYOmslw3evGqXrnHxrvFiHKu8oKscpJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بهمن‌موتور برای تغییر کاربری ۱۲۰ هکتار زمین کشاورزی
🔹
گروه صنعتی بهمن طی ۶ ماه اخیر ۳ مرتبه برای تغییر کامل کاربری یک محدوده ۱۲۰ هکتاری زراعی در جوار روستای دانش شهرستان قدس تهران تلاش کرده است.
🔹
طبق گفته شاهدان محلی این شرکت این‌بار به بهانه ایجاد پارکینگ خودروهای مراسم وداع با رهبر شهید، این منطقه را دیوارکشی کرده و در آن اقدامات عمرانی را آغاز کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/445881" target="_blank">📅 20:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=D3KAB8xjAtjqVKwmHQ64Hr1JF6JJkVro6DPa-vxBbxaxVw5OTehHr-1aDmYgW_1EWKi1w1H7ouf8yHFNhMqoOV-3bc-bjpb-bxtRlvrCe9LjVjfB76fxGqlP8jTJH8VtelC0hX1ETRJma-AxFD6NiNRoyKXUSBaW0gNrw1bhmO-X_KlRN9mXcxTxUEkK6qZ7z5idpYhOnaRTwuwGzvrJULo5yelYOrWqAjFj6vkhaCSukFq5bL08F0QM_78fuJtjkRxSalbW5c6NNoZ8VPvrm8WQkUdsww37mekSPpxr5fKLA8N5OroSABM8dEnisv5yYx8tqnT-GWK7Ru5tnHaMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=D3KAB8xjAtjqVKwmHQ64Hr1JF6JJkVro6DPa-vxBbxaxVw5OTehHr-1aDmYgW_1EWKi1w1H7ouf8yHFNhMqoOV-3bc-bjpb-bxtRlvrCe9LjVjfB76fxGqlP8jTJH8VtelC0hX1ETRJma-AxFD6NiNRoyKXUSBaW0gNrw1bhmO-X_KlRN9mXcxTxUEkK6qZ7z5idpYhOnaRTwuwGzvrJULo5yelYOrWqAjFj6vkhaCSukFq5bL08F0QM_78fuJtjkRxSalbW5c6NNoZ8VPvrm8WQkUdsww37mekSPpxr5fKLA8N5OroSABM8dEnisv5yYx8tqnT-GWK7Ru5tnHaMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: دشمن در تلاش است به دستاوردهایی برسد که هنگام جنگ نتوانسته به آن دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/445880" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d85ac7627.mp4?token=oxTZvtlPpCB-u8_fIGWVvztw6HoBbxesk76Ib9Cfh4oshfZtWORTV6rvoD0NEo4Z3iPcesbQjEAnv4YiB4Cj9uuNBEhlUlJKv12H9sd_Oj5Lcz5903ycRQ7rpU71lW33ZDL_nVS8-GTADAEBhtEzMx0Rc94h7B2wxdMWQcM8EqYmR-tvvFbQH-G9VKW5AsOsSeQ5oA5sulLr14L9r7pj4TFwS0tuD1o0VJ4Yt0T1KpJmjKz_S9stgRuV_muHvS0Oo4Yk8thTV4S61cSlbOb6HJIhA1f89k78489vdctm2SFPv7DqaXpN_NOLyzL-eTVYe-a4Iyh5YV8th5z_UBbd5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d85ac7627.mp4?token=oxTZvtlPpCB-u8_fIGWVvztw6HoBbxesk76Ib9Cfh4oshfZtWORTV6rvoD0NEo4Z3iPcesbQjEAnv4YiB4Cj9uuNBEhlUlJKv12H9sd_Oj5Lcz5903ycRQ7rpU71lW33ZDL_nVS8-GTADAEBhtEzMx0Rc94h7B2wxdMWQcM8EqYmR-tvvFbQH-G9VKW5AsOsSeQ5oA5sulLr14L9r7pj4TFwS0tuD1o0VJ4Yt0T1KpJmjKz_S9stgRuV_muHvS0Oo4Yk8thTV4S61cSlbOb6HJIhA1f89k78489vdctm2SFPv7DqaXpN_NOLyzL-eTVYe-a4Iyh5YV8th5z_UBbd5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس مقابل خواستهٔ اسکوچیچ کوتاه آمد
🔹
با کوتاه‌آمدن باشگاه پرسپولیس از موضع قبلی خود دربارهٔ مدت قرارداد با اسکوچیچ، به احتمال فراوان این مربی کروات در روزهای آینده به‌عنوان سرمربی جدید سرخپوشان معرفی خواهد شد.
🔸
اسکوچیچ از ابتدا خواهان عقد قراردادی ۲…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/445879" target="_blank">📅 20:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c113ecd4.mp4?token=BAB0mO3OeBFjFbpIXNwQpNYXhukh1jaDsZy8g6-97KNkwGzqsht__20-ZbPFQAgTS1KsBuD-WGuJJEVsZqvS46XfwXtDV9devJzBaJSsPJvhpGcQe5upTTRya_lBX7TudqV1QybQlZxWBPE_IPw1sfvT8MItulEVnlJj9ceP72f5Z7cTgH-_NPOUdcXhxmr5nQjaUHT3bmrOFJ3AGIavh_Stx2nUHTZE0JnvT-bx9s8xN72p2qiG5CKKAIcGkmtVAHqrDw-f43g7J8vSuTXqzONkoYFdubF9i4WxBkLxOJamdZ07lO0cgQ8Q56CrwgG02PTCdNkXi-WVvsmagNonEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c113ecd4.mp4?token=BAB0mO3OeBFjFbpIXNwQpNYXhukh1jaDsZy8g6-97KNkwGzqsht__20-ZbPFQAgTS1KsBuD-WGuJJEVsZqvS46XfwXtDV9devJzBaJSsPJvhpGcQe5upTTRya_lBX7TudqV1QybQlZxWBPE_IPw1sfvT8MItulEVnlJj9ceP72f5Z7cTgH-_NPOUdcXhxmr5nQjaUHT3bmrOFJ3AGIavh_Stx2nUHTZE0JnvT-bx9s8xN72p2qiG5CKKAIcGkmtVAHqrDw-f43g7J8vSuTXqzONkoYFdubF9i4WxBkLxOJamdZ07lO0cgQ8Q56CrwgG02PTCdNkXi-WVvsmagNonEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: هم‌وطنانی که به‌صورت کاروانی یا با خودروی شخصی در مراسم تشییع رهبر شهید حضور می‌یابند، حتماً خود را به محدوده تعیین‌شده برای استان خود برسانند
🔸
برای هر استان، محل مشخصی در تهران جهت اسکان و استقرار زائران در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/445878" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c5fed497.mp4?token=ci9efvwT2U4CBonmWIoQ2EyAoklnmREcjt9-RdVpTa1eBFntRkqxIG039FzihIOiTOwO2LxSXzRzUE4iYL-LbiZfHReqoUZi2qd86e42O0i6T5DROT1D3nRRlOI7rM979-IZLbwpK7SE-uHo5rci46cBgc8ELWvtYr13ojmeBe47_TNozIFU7nJr69_xw5UcAFXlJyHNrDqyqfBOCGCtD59c4ZSTWN5YdjPxTs78bq8npEaSt_YWvsgOI6epi8bLinwpoTDj-COZzKZ19Cszl7CoIWUq2cPWU97YlFfCHUsAhOOy5aLWgoC7EQPsit7SU2DxBaaY4uEiMEtf6QUVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c5fed497.mp4?token=ci9efvwT2U4CBonmWIoQ2EyAoklnmREcjt9-RdVpTa1eBFntRkqxIG039FzihIOiTOwO2LxSXzRzUE4iYL-LbiZfHReqoUZi2qd86e42O0i6T5DROT1D3nRRlOI7rM979-IZLbwpK7SE-uHo5rci46cBgc8ELWvtYr13ojmeBe47_TNozIFU7nJr69_xw5UcAFXlJyHNrDqyqfBOCGCtD59c4ZSTWN5YdjPxTs78bq8npEaSt_YWvsgOI6epi8bLinwpoTDj-COZzKZ19Cszl7CoIWUq2cPWU97YlFfCHUsAhOOy5aLWgoC7EQPsit7SU2DxBaaY4uEiMEtf6QUVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامه‌های فرهنگی مراسم وداع با رهبر شهید امت در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/445877" target="_blank">📅 20:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نماز بر پیکر مطهر رهبر شهید ۶ صبح یکشنبه اقامه می‌شود
🔹
رئیس ستاد آیین وداع، نماز و تشییع پیکر مطهر رهبر شهید: اقامۀ نماز بر پیکر مطهر ساعت ۶ صبح روز یکشنبه برگزار می‌شود و از مردم می‌خواهیم برای حضور در این مراسم زودتر در محل حاضر شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/445876" target="_blank">📅 20:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyiCOnDTu7p52BZyOv4r5GnpNHqIqkVYET2KIk8TTockZJ5EvAEDk0us3e-dB0SsQgnm_1YotlL3JC2ibZqzIoyjXqAXq-MWzQiyR9-Cjl8DsU5wsZoEthiORJPU3ttNijKfGNVArPMW0k2SAAZlEa19lWJ3lFNJQlfUp3U-BcpWom2-0JyJbQhEW05oLazpJfZad5KloAIuYKOfvBUOaAA8__6dlFyjjyIdLB4PDIX9scbE0A0yHOkKzJ1G6YWQ9utRf4YfCk0xFjvyAf0W0OLsbsZgBi4kQXFWv8QlXarbw_L547F-e4nG_XDfxwXY8J3PrB2D6MddLAIgssZfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445875" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/703007658e.mp4?token=lsiWYTUbaEbGangdS3nePtLofPF9sIhyVk2KB6fc72VI_3cHZRHVMfnu0OHs4cRNybSMzQe1ErMp018ItfEXDuS5XCmRjnU1KYxY_KyTCYYTfnnjUTGMQHLOKrWpoLJgVgJRSA9BghdHsbJqZ9r3CJsNNWSbdsbgehhMYJ2OlhkjXGHgdC-OB7Mjb-hOQx2j9pKROep0vLeOvwDhEXN9Zv5kKy9wumt5VuIqhrQccpMmB6ijU16hjeGe-5PcUbZJHjyYeNEML08zghj3ruNwIK0HRsPGHAVIa5joc7dbRIckvbQs2dE1UQyM3SAKFL1xDa4TiVwKf-ChYu4ce1B76IWy46Oxf31HEp126d6D74dA9Y78ulpF6p0xMAWDSbZYvaYM3GlNjQ8SszzreYgrtyJlD3MRtNietC6RUIfyIMGdu6zPy-mY3tOghAe1SVeKlNjfFLXSKcicq7gfh-h81SeyRkGKJjUZXActslQAjDUvY_BOxX1K33xLO1lsbrGAp2x41lTFE6w81nqjA7J1D4JIGAR7rYwf29pxBWPI5GMQewlWxLjfxCAleCS9AF3aML0xgxCP9_z6CO00MszUiuZO8fHRVuFZuyCXcH08yyPjN5bCKzggqYdoDIKRNd4aZD-9zy0WuMPzVPmk7czmJd7JAJq67nsfF533ZZnCkRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/703007658e.mp4?token=lsiWYTUbaEbGangdS3nePtLofPF9sIhyVk2KB6fc72VI_3cHZRHVMfnu0OHs4cRNybSMzQe1ErMp018ItfEXDuS5XCmRjnU1KYxY_KyTCYYTfnnjUTGMQHLOKrWpoLJgVgJRSA9BghdHsbJqZ9r3CJsNNWSbdsbgehhMYJ2OlhkjXGHgdC-OB7Mjb-hOQx2j9pKROep0vLeOvwDhEXN9Zv5kKy9wumt5VuIqhrQccpMmB6ijU16hjeGe-5PcUbZJHjyYeNEML08zghj3ruNwIK0HRsPGHAVIa5joc7dbRIckvbQs2dE1UQyM3SAKFL1xDa4TiVwKf-ChYu4ce1B76IWy46Oxf31HEp126d6D74dA9Y78ulpF6p0xMAWDSbZYvaYM3GlNjQ8SszzreYgrtyJlD3MRtNietC6RUIfyIMGdu6zPy-mY3tOghAe1SVeKlNjfFLXSKcicq7gfh-h81SeyRkGKJjUZXActslQAjDUvY_BOxX1K33xLO1lsbrGAp2x41lTFE6w81nqjA7J1D4JIGAR7rYwf29pxBWPI5GMQewlWxLjfxCAleCS9AF3aML0xgxCP9_z6CO00MszUiuZO8fHRVuFZuyCXcH08yyPjN5bCKzggqYdoDIKRNd4aZD-9zy0WuMPzVPmk7czmJd7JAJq67nsfF533ZZnCkRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برگزاری آیین نخل‌گردانی ششم محرم در نیاسر اصفهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/445874" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584a83a1dc.mp4?token=Kqki3_urmTcddRalcWwl57nemZpWpZbHdKAx5YHXOjhaTaqH8hLv8t4AlKCYG0uirDA0tN_wThGgrSYkDrQRrFeBszkAbH1GL9PemeMiNw58l-4szSR2xYIjhwlBdTscNC8CULWwZgfsusWssPxLtx11Sn-GDlMD2t6cbvbvgJ9zIyVmJ5BJ4wSoFFP79J2_gUiTWHymZ-Hu-Q6tCtr8JvvwkemH95o28nFzeGQTKo8-0nFZVtwtpMt-FgvDu9Wp6pJRYgge5Wt2WJG0JnheR_xJ-DQ8D69Nxh6nkxe1xsrkaTsT-Trhb0ep49wwpCm7l_HO6h30dnVhwMTx5OGyGwBTQWadlB94Li_YIf9Mgjj8NiWGwuIp3RfgznLOY_ibSZX_wV4OZjfZj_s104tdJ0cQLSVcTmg0IdrEq9RgMl13SdCnUpCKL1PvAxz7I3_twCcnmSQxCDvyMGJJgmxaZGt5ObTUtGAPMrfLXzWCF3F7k1ilPdnmN9nAAqMpIQ6rEdyE7iJ9cT4_VLnVf1vbAsFoKHRMBaStTU2Y1bTU64bKe8H0OFFlryGvQ0SqWZjkHyLeBc9_QAWJkLmDhoLPcxrNSZx-reVtUQt4-N6Yyww8ndOpQ3-UrzRJsXg0Lqu1s1lfy0Aby_-QUFPzHBbvnaMy7GLBcMQ57jGtkWKaKOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584a83a1dc.mp4?token=Kqki3_urmTcddRalcWwl57nemZpWpZbHdKAx5YHXOjhaTaqH8hLv8t4AlKCYG0uirDA0tN_wThGgrSYkDrQRrFeBszkAbH1GL9PemeMiNw58l-4szSR2xYIjhwlBdTscNC8CULWwZgfsusWssPxLtx11Sn-GDlMD2t6cbvbvgJ9zIyVmJ5BJ4wSoFFP79J2_gUiTWHymZ-Hu-Q6tCtr8JvvwkemH95o28nFzeGQTKo8-0nFZVtwtpMt-FgvDu9Wp6pJRYgge5Wt2WJG0JnheR_xJ-DQ8D69Nxh6nkxe1xsrkaTsT-Trhb0ep49wwpCm7l_HO6h30dnVhwMTx5OGyGwBTQWadlB94Li_YIf9Mgjj8NiWGwuIp3RfgznLOY_ibSZX_wV4OZjfZj_s104tdJ0cQLSVcTmg0IdrEq9RgMl13SdCnUpCKL1PvAxz7I3_twCcnmSQxCDvyMGJJgmxaZGt5ObTUtGAPMrfLXzWCF3F7k1ilPdnmN9nAAqMpIQ6rEdyE7iJ9cT4_VLnVf1vbAsFoKHRMBaStTU2Y1bTU64bKe8H0OFFlryGvQ0SqWZjkHyLeBc9_QAWJkLmDhoLPcxrNSZx-reVtUQt4-N6Yyww8ndOpQ3-UrzRJsXg0Lqu1s1lfy0Aby_-QUFPzHBbvnaMy7GLBcMQ57jGtkWKaKOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌روی و نمی‌رود غم تو از دل
...
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/445873" target="_blank">📅 19:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd47bf230.mp4?token=Az4CngbvNXCIJqFrCKGh1j9w_dN_nMEVIdmczM0SchvHgsLOzrXI_byjNfKtqqgyF8QXEh1z1ypE8n6gstztdXlXC0Mpit8z5DE-93RQeoU4o6Gf2vrhQT4zHAWLNi1ehvO4eVLYx8l3li4a-WyrKqhN9ywtVKPYvI34lQ8BhYDqVWCIgg9g7i8RZ6OMNIF6WyYsnxRHqhyGBcWK1-f-oGsseMbZJ5jOHojnZwq8cwjtLoyhL9f_QWphlkVnidZmNfquzTm4uu2jbFJ9jPz3n3ERbJ4JMVkTn90B0Ly0lWCfumaWq0zc0i64GfDSkbwR_XMxKoh1Mi8-wJLlenLOKK33mJHXJgIRZCT9WH8426hbtZyQxnTalsqfggVFHTC8pX4XxK-1w0wUp2WGAaks9dHWPfoeDaCzIQPECBsfnzXweMmbg4f1YBoosPtfr92R69jFQqvoJ9i3l1FraGwF15_0tIyn7LsehVWVd5e1WbPwWKn453yssTfPtKVIIBDt8qkQZXXy9UdyP4tRtLOTU_CgSTR-3f4wHQde7FUvLFjqjQUU2scCyrbGB6PehwNHcjSrcXzaJ8ImS-OZTgSihIqHGB55b4KTQ23O2-xZiLE5oeAGIpYPbgHXG2l8adNAWBbQWy4QRZoDygjlypD0P7buav1cwuLGF75jLM-Ff58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd47bf230.mp4?token=Az4CngbvNXCIJqFrCKGh1j9w_dN_nMEVIdmczM0SchvHgsLOzrXI_byjNfKtqqgyF8QXEh1z1ypE8n6gstztdXlXC0Mpit8z5DE-93RQeoU4o6Gf2vrhQT4zHAWLNi1ehvO4eVLYx8l3li4a-WyrKqhN9ywtVKPYvI34lQ8BhYDqVWCIgg9g7i8RZ6OMNIF6WyYsnxRHqhyGBcWK1-f-oGsseMbZJ5jOHojnZwq8cwjtLoyhL9f_QWphlkVnidZmNfquzTm4uu2jbFJ9jPz3n3ERbJ4JMVkTn90B0Ly0lWCfumaWq0zc0i64GfDSkbwR_XMxKoh1Mi8-wJLlenLOKK33mJHXJgIRZCT9WH8426hbtZyQxnTalsqfggVFHTC8pX4XxK-1w0wUp2WGAaks9dHWPfoeDaCzIQPECBsfnzXweMmbg4f1YBoosPtfr92R69jFQqvoJ9i3l1FraGwF15_0tIyn7LsehVWVd5e1WbPwWKn453yssTfPtKVIIBDt8qkQZXXy9UdyP4tRtLOTU_CgSTR-3f4wHQde7FUvLFjqjQUU2scCyrbGB6PehwNHcjSrcXzaJ8ImS-OZTgSihIqHGB55b4KTQ23O2-xZiLE5oeAGIpYPbgHXG2l8adNAWBbQWy4QRZoDygjlypD0P7buav1cwuLGF75jLM-Ff58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عصبانیت مجری MBC عربی از دست برتر ایران
🔸
مجری شبکهٔ MBC عربی: ما این توافق‌نامه را شرم‌آور می‌دانیم، یعنی خود آمریکایی‌ها در آمریکا هم چنین دیدگاهی دارند که این توافق‌نامه کاملا به نفع ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/445872" target="_blank">📅 19:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQWd3TMCjJ6eqiobNB-K-XX9sRn5TJn_SeHf4e8oiZsW_OXfrKagVP8Bbcrmod1X1uRGFLXSQqmvoWdDE3QAkb4h4kbG7Q0YDKddsAh_2-VxrKIvfjdzUvHmsumeT7NUPuyLqbpEUDecgyscVqis0KDnBo8Q3xx3uW5KnnOHyRYiUSsNGClJIXKLRzQheQWiKs4N__aedeb9PG8xYdiMRWw1Ri-luI4FWpa1sAz4Z0zJreu2ZhXWIyb0xDMGAWuqTkscCEkxydYIO-CGa0HvLqFdLrMi825vQuzFYcpZ_AI82jiQz7-pez5filQ6m8pIzMU3HrxJzpy5PkVwUs53Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/445871" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341edfec61.mp4?token=AmO86IFitZDvtXGAY8R2bXAcOEGvj0iyRDoKSf7LimpZbryoYiIoTqB2XzVvCX5Q-DYZCNktWkvBTWlIe8lpIGkFpqLfwyZp0TOjwyIZmXgQ2Czr3VUZ9F9dyXBDuxuO5h6Hz4e281K-4ggqKq1pBAOW0i6Y8pkLiBfhq6_hfLU6IHAqGdmWyU7U3drK2USZv2PLiCkvcWS-AeOy5lH532o6mx0odJwTOh3g9S51xq3eXnajkyH-s-fRQLNsagFRVbQ0NKXg9uOduF2Ez-PJ4WJ504BEqiqZxLMot49biPCyJQIf-XQJK98w4N3rq_SPSORq0QxBCga7KLoBbwOpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341edfec61.mp4?token=AmO86IFitZDvtXGAY8R2bXAcOEGvj0iyRDoKSf7LimpZbryoYiIoTqB2XzVvCX5Q-DYZCNktWkvBTWlIe8lpIGkFpqLfwyZp0TOjwyIZmXgQ2Czr3VUZ9F9dyXBDuxuO5h6Hz4e281K-4ggqKq1pBAOW0i6Y8pkLiBfhq6_hfLU6IHAqGdmWyU7U3drK2USZv2PLiCkvcWS-AeOy5lH532o6mx0odJwTOh3g9S51xq3eXnajkyH-s-fRQLNsagFRVbQ0NKXg9uOduF2Ez-PJ4WJ504BEqiqZxLMot49biPCyJQIf-XQJK98w4N3rq_SPSORq0QxBCga7KLoBbwOpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنگو از انگلیس پیش افتاد!
⚽️
انگلیس ۰ - ۱ کنگو
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/445870" target="_blank">📅 19:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMgMiWuGsrjsRpxlR_YqB3uycX7oldKB2qjXJZuop5Q5w2o9Lo5WQuk4RJI9xEm_shOzXfHouasw708QrHRKCAiBdaJj64CX54gW9otQJQNz97yMq5-DJ60P3bZL4ePYSwU6NPIdc8CywSEvEm9nD1tWWxTHBWoiRolTHS1uO1QoJb5RVDgfJfxd_TspaYVxtHeH6gPBH0HvBAguyoxlBgk9kpDDiU03J__Xo8Az2IwarmKUkzlEZxdo4aB2BsE-COzUCiUqNJ6OwDpEpRrhFsGu3cqgxfR4rJPPhcfI2akbLEQ4IXSNf1WedA5abQmmmEfzxNh8cuoNwlo0rjcllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات برنامه‌های فرهنگی مراسم وداع با رهبر شهید امت در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/445869" target="_blank">📅 19:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHGVVhnUBKvUi8O08_dnIfQhneg5H68Nv164Mm3_wcUH8v08aMN21zxXJF4TY-vpZGqlBfukEPgVKjgIxdNaiCjFrofsj47Hmk65lCMJV5HGr8qXvdgjLNrLQOJUn6XQAtAimZp-exjmUlihERJSP7t7gbRwSCqneVuZrfjeXz3Dt6V7ZFGrNMKu7exosX16ZFy1D3yVoEk2ip95_JQl5nE_NQqBr5QUZbC0qLJDs55ITpDd_gTHcehnHQAUwHP2zi3pvXF6BZGP9Sdq0vUA95AczubzYmMXo3cNkttJMWnExHKgc5e3dfYoyku_uph-55wOkZ3pWS7K4uCPt95rhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفع ممنوعیت صادرات محصولات شیمیایی و پتروشیمی
🔹
گمرک: صادرات محصولات شیمیایی، پلیمری و پتروشیمی با رعایت مقررات پیش از محدودیت‌های شرایط اضطرار، بلامانع می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/445868" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
