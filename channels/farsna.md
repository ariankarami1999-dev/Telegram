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
<img src="https://cdn4.telesco.pe/file/XlybhMHHXus_8rIZ9HXFN1RiU_E-J-r8TScup7v0Xgmid0t2eurvIziNoKfToJckJ1dR6FoVdkudzRmJkNpIiH-WE06cSJaoQM4pflNZtC7yL3hUZmoxiDIjoBR7bmyK_vZom8zxz4t6grmO2XcOV-458Oo0t6Npv7hQ_3JiE7M1vtkCdVw0rgO_6ZpSrVLMKxjcK-ARPMVYviZb4s0UZ1lEAeKxGqoalf0HnSN793cOgUnKsYUXm6zQ2aIIx2aC1YCIJdsckVMM0bl6dJFGF7--ldlAPd6lyw2vjXxTodKLAQyQ3Pd85Zkw81bAAv2vy6zq7xxDK0WRTRKMwciY-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 02:03:36</div>
<hr>

<div class="tg-post" id="msg-462349">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار در مقر گروهک‌های تجزیه‌طلب در منطقۀ کردستان عراق
🔹
منابع عراقی: مقر گروهک‌های تروریستی تجزیه‌طلب ضدایرانی در منطقۀ سوران استان اربیل عراق هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/462349" target="_blank">📅 01:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462348">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms28nPtCFqP4FsLY0P1lbYAn4vjpcUA0U0EtfsWTG_79-rr2h3H9MHGUzPGOOB9Xy084xGFaWTeMMPD7xExw-no0zuyKmT2D6CWRQVwJIdGe8Ap3BdJ0oQP9CJD05x4D_p4RYdrew4H3i8clnZm4H3Ka9Wleu_fYON_qHgHZKuEOdgSeLH4W3mYtELoRra4Ztgi1Gh_2Dv4I5buTtL2gzW8qpnkVz-i0bMMjLAaoo0zlyywEPKTQbu8gSydNjkJJoDWL0HgBX0zZ6kzz42rCVzcB7bmAyHq13jbG4bQmQ3phDFlQit5xc7tFIaW3FE67SCuiDUdPl0eG7RXh2R5S7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جابه‌جایی موقت المان «مشت گره‌کرده» میدان انقلاب برای مقاوم‌سازی
🔹
سازۀ «مشت گره‌کرده» که در آستانۀ مراسم تشییع رهبر شهید انقلاب به‌صورت موقت در میدان انقلاب اسلامی تهران نصب شده بود، برای انجام اصلاحات و بهسازی جمع‌آوری شد.
🔹
این سازه پس از تعمیرات، بار دیگر در میدان انقلاب نصب می‌شود.
🔸
به گفتۀ مدیران شهری، این تصمیم با هدف حفظ این سازه به‌عنوان یکی از نمادهای شهری شکل‌گرفته در جریان مراسم تشییع، و پاسخ به مطالبۀ شهروندان برای تداوم حضور آن در میدان انقلاب گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/462348" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/462347" target="_blank">📅 01:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایندگان آمریکا برای سومین‌بار با طرح استیضاح ترامپ مخالفت کردند
🔹
اعضای مجلس نمایندگان آمریکا در رأی‌گیری بامداد چهارشنبه، با آغاز بررسی طرح استیضاح رئیس‌جمهور آمریکا مخالفت کردند.
🔹
این سومین طرح دموکرات‌ها برای استیضاح ترامپ طی دو سال اخیر است که ناکام می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/462346" target="_blank">📅 01:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qx2mAXf0vv0xTI_inv9Gywas_Pk19xHvpTqOsH4edB0_WZoW0dYLHOkzPl4sB5T1eZS5zyczfa6ukiFHn3wndfXVb7dYBHNm0apmNquMXlS1VnHUdtJbdm8S377p1xQNU_NMbB7BrFJ4SgrfXffUbjHrl9tNHrwxG0snoi8hjRFCWvltnXQNHrwo-r4H4N1WMgvRq4x4giwqWXgZCuwMW9aZKTtLlznb4ZE5iXPXju2Y0bxU-4Iqi8zvMbUgHvW-4pafb9LqquPD3kUqoy8vNP6T0vRRFejP-eF-3CWRoBa8B6wUqZtyTCI-mhdEcm0nG0YEhxiI0vh3-NEKREUH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsjAWUX6LYUPIPSLt31CN7CY26VpdZVaSlu5iDWLi9zstqLLlH41423I9peKrRJMCFjOOkcr6g0Ew4wheVmUbUqP4zgna9TsZchnKRmTlgC4UCdFOCIRYOPHCceoaiQZAbmUmfFNbAwb7_ePyw5AziGZHp_ORXJt0vsuJSQvOkJZtZ-0dnStfbfk1r5hb_yuB2F2LYKo3t65xElT42Ty4yidil-qwXg1KW0KcIcCUnhTnzZ6Ntp8xpStcEHVxiTS3SSu1JOx9DqCwv8T6nh73I4q5_DNufBTtqYssogmOlUS7JLTCeC5Mb3MSQPzV23jkLZahgq7df3EwUmE-cs47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZsAf6e-C0lnR9neTKzmh8pqSWx824WDxrf5B0oRcEwZ8Wz4qZvzxcJRtj5NzpGaDFIYKZqrCyIQoSTG67FYye4sAeomQKVkFVFFNkf-cfrQi-Nx-mQfv6rOJ0PfQdwggNtq8r-DKPG13tdA3m4cpp59q4vL48QxDCV3IxM2ytdTGQV5TX0jmotBF7JSwnTEdoGvi3BI5CksQiRVoogr_FyNofANYQ3WMr8KPXIWP1raTL8FL9br8HV2ersF1i6Jnr48BO5C1vkFoN7E0UmjphRjx7absBVz_gz8qm9y3Xa4u8PMmAwnsbIp9wjGvISuFs_1_uHWKXk5mGGGuSwTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVRVsJRpRiIbnITggMNbvy4azNB-nsk1-Db-d94KZh4Cp5hHKG8UN_TZ02w0C58m-vms1dLQHZL--MfiweSf0WaN-Si7oYiTQgixZZvQ-k9CrGK2mGm9m70_VcWDQjCuECmdu8M8TWzPFsQtyYXn1vDhIGrEHNzP_OlStIBXciMTK1hB2c_WS4LFA-b-POK7f3twlXIJa17qbcdGt943YZ0-lFl-C_6sbFvN1Yz8aSGNcMdhHlSAwPo-MGw7LASXPGYmuMLWLGXogCGV5zOrUV2NjLQzYxmYH8nA2toAD_xvrcqeSX-A7LNCj1N-R465hFIcM4f2clv-FELEz9kfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GddshuTUlLTwk9h82VgS_xfFSFuH0eaOx5AfvXuOvXDyipknqU7LMYUFxgHYC0gl0sdPiZ5_gb1HNoup8Sy1nE9jVMHEsLMp9332cO5kLjGDkee8_l6MaJibwrNf3BPwW-Fr1jhcO3bNIo2VEQj0naJdGeah-IzbRaShT3Se_3m8rMLnrzdyrsaG_rJFTSTOeqLgNRhEgR-yLJUa_s6nFiMeHKfMuzoAfEpLS_7l-boq4LbYHAWMD4RQ9lGaODNnzpM_CozDq6T4EkwbUi4VsYDTdwefM7HaOWMQYUbPdM1-gbiXkEOnVShp6F4W24TQSqTxr2zlNBOQxMH37q64aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp_2uwn0vgOvKTfWtkg6oMfUd1FP35t20Sknkja_DcCUuYmS7Y2jWu0eYa7TLuZlJQLZMjutW2mrFByoXmexjK0BybhkvC18Rc5ofp73_9WuDdjtEvyVJBfkVp57fzH307fMIzIAYG0N6i31XFrEiUEfd9vyc47Nnd9Ud8q1-E3OeTP1x2Haj0FXl7tyzYP0PRtI1uhb58kUWVGSFKD89w1lE5vE8GWsmNwqNI3yITGBZwq0vvWwwJf4Zzn3EbxljSIxaBKQc44z7UV08OAPM3_V5Ad6_PkQ4QseIclBatu3a4fYm0Y4F9enG9s04RqYUdd9gUeZVNTy5O-83GQ2Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن ازدواج ۱۱۰ زوج تهرانی
🔸
جشن ازدواج ۱۱۰ زوج جوان تهرانی  همزمان با شب ولادت حضرت عبدالعظیم حسنی علیه‌السلام در برج میلاد تهران برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/462340" target="_blank">📅 00:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آخرین وضعیت تردد در مرزهای ایران و عراق
🔹
تردد زائران و مسافران از مرز خسروی بدون مشکل ادامه دارد، اما در بخش تجاری، حرکت کامیون‌ها و تریلی‌های صادراتی با کندی انجام می‌شود؛ طبق بررسی‌ها افزایش بازرسی عراق، از عوامل کندی تردد کامیون‌ها است.
🔹
در دیگر مرزهای ایران و عراق نیز روند ازسرگیری فعالیت‌های تجاری در حال انجام است.
🔹
رئیس اتاق بازرگانی اهواز گفت فعالیت تجاری مرز شلمچه نیز از سر گرفته شده، و بخش تجاری مرز چذابه هم از صبح پنجشنبه ۲۶ شهریورماه فعالیت خود را آغاز خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/462339" target="_blank">📅 00:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع عراقی از وقوع انفجارهایی در اربیل عراق گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/462338" target="_blank">📅 00:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE40mv-vEGEiuQuMDyU_4Hw9_iOyHphVS66Ysl8A-Z5pV7DXCP7v_MXJtr-9Wa8XMNDWYtaiXpOZUVSeHDZZhSBX2XQRkuYQ4CPl681Sl4GasUtyUkTGy7SKdjKNLB-kBtxouF_6DkyI8TwIV6KOe2fg-NF0K4irbR-EPz9zBKDfi4iWsohoS0YBptxAzlBRSvW1B2AfQZGW1SMvs_JFB6oAXil91ukORLdu_YwdHznBCuf0pKRNez6oifxWoNpmkg9QN-OThJvgcOaCK4RRNhAX1p9YK1GZr6SgbHOK-BGPl2cvWFp0R2ibfvMzFWoHzuWrAe5C9gkIK5sBUj0raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام
🔹
حماس در بیانیه‌ای شهادت نائل ابوعبید، فرماندۀ تیپ رفح را طی عملیات ترور رژیم صهیونیستی اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/462337" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۹  شب؛ روایت ایستادگی مراغه برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/462336" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ce02260f.mp4?token=Bu6fTsNOSIA2OBB3mq4YCd0TMQViejuJ96QAuvl8YTxGomF551eIYRJ3oetsKVvgN0AYOdcCKNs1dvDKG1aeNt2ctEGa7z4-EBqjO4GBxJdN66jExDsVtaBgXPRSGtvPIFvfLSYAkT3UCJnNpdfaLYb4uzgjqzuLvygTmCCc2r0x5lrhNIZgd3KfS_FtozAWdGmb1EWlDXJo0BJ0h0rKQ0kfRuAEr71ullzL89Z-SN9uQzTooRTRhB5VIqWK5sjDhA00_3cCQz5ARNvU6azRXWALAgWeRqkwippsd_yFtv6Ew0gE7OOXX0IlPI2N-ouA5TNczICGapGtw21GdmST_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ce02260f.mp4?token=Bu6fTsNOSIA2OBB3mq4YCd0TMQViejuJ96QAuvl8YTxGomF551eIYRJ3oetsKVvgN0AYOdcCKNs1dvDKG1aeNt2ctEGa7z4-EBqjO4GBxJdN66jExDsVtaBgXPRSGtvPIFvfLSYAkT3UCJnNpdfaLYb4uzgjqzuLvygTmCCc2r0x5lrhNIZgd3KfS_FtozAWdGmb1EWlDXJo0BJ0h0rKQ0kfRuAEr71ullzL89Z-SN9uQzTooRTRhB5VIqWK5sjDhA00_3cCQz5ARNvU6azRXWALAgWeRqkwippsd_yFtv6Ew0gE7OOXX0IlPI2N-ouA5TNczICGapGtw21GdmST_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رفیعی در برنامۀ سمت خدا: انکار خمس، انکار یکی از ضروریات فقه است
🔹
کسانی‌که سال خمسی ندارند، به دفتر مرجع تقلید خود مراجعه و برای تعیین آن اقدام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/462335" target="_blank">📅 23:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
سنگر خیابان میزبان ۱۹۹مین قرار شبانه کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462334" target="_blank">📅 23:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVQ9nckqWgKajip8QNsg6yTkTzQDAwXgRhWfgsMrLEK0-qKs482kJlj1CwUqwmxtcmbrw7gjMwdx7lrxh-_E9GSHcAFrFBm0NtB9XtMidC4nhxNsNux2ifhFvxKgB4kPsHuXpAcnDdehcwX9rq7m189FrrvxBQHp0I_HXawOWOdS1a6MH-XwmgznEX1rkEBVIBHw5J0qGeeDkb7WLIjuFoHsXWBPQUCg0K69oahx-I8dN2-PA8bAQ_N8hB4QHZ5BDamKZ4r3EF9B6m9tY58VZaGkaAnMTEZzLrQLDZjHH3Gp3I2hsD02Xir9_3HWq1Edf177VLZcAkyHU1ZMJYTXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلاک ۱۶۳ خودروی متخلف سوخت‌گیری در رودان منتشر شد
🔹
رئیس دادگستری شهرستان رودان: در ادامه اجرای طرح پایش هوشمند جایگاه‌های سوخت و بر اساس اطلاعات ثبت‌شده توسط سامانه دوربین‌های پلاک‌خوان، ۱۶۳ دستگاه خودرو شناسایی شده‌اند که طی ۴۸ ساعت گذشته بیش از یک‌بار در جایگاه‌های سوخت شهرستان اقدام به سوخت‌گیری کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462333" target="_blank">📅 23:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs7ZTH-lfWNGo1JZzWgQQMpalFftpkgKGSjj94LyoPY3eLLnqN71UPoRIbGRF8KIVX3HO4Gbx7VQbi2ljS9YAKi_HZPAR1989P97_yv3RZXwc7PD5lvnWB58tqUE_kFA-OtfQCrDjJz9pUs6O1A2PZgP5bKU32LSBvgLDhqZPoqb8gmuEsL-CPO8g-Z4DrRwj8x1z1chJZtmA2dePocVkR5oMmA9X0UHgGeYDzcSw9yrnTwKCKGHB-Kot28oQgQdhBw6KsgyqdSg5QrkZPDc9-BKRNo7HC6XU3bPVrQ0ZJTaIPJFQ-o7vrZ7syAXDMZOsS7-mHPn7BGCCfp-MvknQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtcRLATV7YNT9FKXQ4rC70zVcJ7y1nCup22XmmKnow6C3S4u8QEuBuU1ai6k-EH264WPv8s-MygsfVG6L1wHoVSobJykvtGGefgSJx-U0Q40dVS97SPpCuylWplrc32rLFFa-iDzTjtyEjGuC9scQhHTK7GE8FLlvHy5gLODjF7YaOxUjZFlF_U4fn5ta1BqQ57WzH5r4cYMvXSZm9PaAzimecmGBkYYa0XgmTzpKo1w7nGIGDXUJjJxMfNugg5c3MdDgvX8K2crfsU_TPRrdU4QB93_6PMDqWnHfRAaGyTHWaUjN5St5RToLhk8jsVJT_0t-492PZrh1FBXnWfYbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار الجولانی و بن‌زاید در امارات
🔹
الجولانی سرکردۀ شورشیان حاکم بر سوریه در سفری به امارات، با بن‌زاید، رئیس این کشور دیدار کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/462331" target="_blank">📅 23:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b19438ce.mp4?token=Jz5tKpXnYQ0yO7O4B7Fz1JBl4RGEvLoVeBLWUWGeiyj_fiOJ1Y7hSFdYc1k07Xrr9W05ghnZrJMBz4YhsSKQE2VGqylQBzGrx6nxqRmAya6m7G5sV-6GBQtCnABk4eLKenInOAjaa5qMMocKXLBiBLUVN1Sip3LpAfmAQVTo0FQXtt492XqalbTwwekjJc1Q8ydaUyWu8icADbzc6LGh7QjObyH_Z8DM_U-Ci2tvs7vpasRX99i7lctBMww0kQSCP-kOq7R1E_IyMTIG5qH-c_fqKcEnh8-a6QIjeiG65r-bCGcGsy920DBYfDCOP-cyPVha3PxQyYO39SI5bVpBUJo0ODdTgtI8Fe013XaLMnVzyv3K4UaEeWDTqGxWh4zWX0g19MGDeuEnrjvkWH4OlZjsTnVSfbDWdqI_0nlz-OF1SV_GSMvdUBqvnmwfreNvT_J87Nkq9c_BUWZtMzRGsCEzuZzRMsqN3HI2FDZc8p9jRAEErsm7fuGWvnn8Ow21xNsNdOF6LmIg5OMRHXC6JzanN3MnOBzTU33TRkD9te3bnDYqmzSVHNyJ6bve6Ja2ZmqnixuXYi52FZJVKVBTcEluwc1ak3dqtyIDstnIs45146ce0q3PK2XxUACvKjCM8I_qBVskQ_r9aY0CWJ_2-AYuGSug4CIG9thZ5oxZ8UI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b19438ce.mp4?token=Jz5tKpXnYQ0yO7O4B7Fz1JBl4RGEvLoVeBLWUWGeiyj_fiOJ1Y7hSFdYc1k07Xrr9W05ghnZrJMBz4YhsSKQE2VGqylQBzGrx6nxqRmAya6m7G5sV-6GBQtCnABk4eLKenInOAjaa5qMMocKXLBiBLUVN1Sip3LpAfmAQVTo0FQXtt492XqalbTwwekjJc1Q8ydaUyWu8icADbzc6LGh7QjObyH_Z8DM_U-Ci2tvs7vpasRX99i7lctBMww0kQSCP-kOq7R1E_IyMTIG5qH-c_fqKcEnh8-a6QIjeiG65r-bCGcGsy920DBYfDCOP-cyPVha3PxQyYO39SI5bVpBUJo0ODdTgtI8Fe013XaLMnVzyv3K4UaEeWDTqGxWh4zWX0g19MGDeuEnrjvkWH4OlZjsTnVSfbDWdqI_0nlz-OF1SV_GSMvdUBqvnmwfreNvT_J87Nkq9c_BUWZtMzRGsCEzuZzRMsqN3HI2FDZc8p9jRAEErsm7fuGWvnn8Ow21xNsNdOF6LmIg5OMRHXC6JzanN3MnOBzTU33TRkD9te3bnDYqmzSVHNyJ6bve6Ja2ZmqnixuXYi52FZJVKVBTcEluwc1ak3dqtyIDstnIs45146ce0q3PK2XxUACvKjCM8I_qBVskQ_r9aY0CWJ_2-AYuGSug4CIG9thZ5oxZ8UI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب تهران به عطر حضرت عبدالعظیم(ع) نفس کشید
🔹
فردا سالروز ولادت حضرت عبدالعظیم(ع) راوی حدیث و مورخ برجستۀ شیعه است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/462330" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e625c5de7d.mp4?token=Rwx_jOQuOSdFHF5h3ymNZ2wNgjEhM_rijhW7Fko3dDv0wVmeileNoP4751gZLI6STLBTiapCvf9TISt8xRO1z1Qex81r9_MW5DyI50yW3YJMt-Q15ob3A_81lqB_nWlTW9ZUJLMBlDOgw2IK0kejo_SCPPxttNY0YMK0atOxx8jGY19OWuwwAErmnIl6tMIRPw5Y7AiyqePC_OG-JsUpVkmbrBpvEX1JKvoO1Hj03kTWALKwBLBPKVo_8RLGtR_c_T5cAqFQfxLjvs6kj7EzkOr_MMgiujwOmyp1HMAMA4Vh31B9Da6wywSfnSfF0O8quTuKCnMennNkXtuSaizPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e625c5de7d.mp4?token=Rwx_jOQuOSdFHF5h3ymNZ2wNgjEhM_rijhW7Fko3dDv0wVmeileNoP4751gZLI6STLBTiapCvf9TISt8xRO1z1Qex81r9_MW5DyI50yW3YJMt-Q15ob3A_81lqB_nWlTW9ZUJLMBlDOgw2IK0kejo_SCPPxttNY0YMK0atOxx8jGY19OWuwwAErmnIl6tMIRPw5Y7AiyqePC_OG-JsUpVkmbrBpvEX1JKvoO1Hj03kTWALKwBLBPKVo_8RLGtR_c_T5cAqFQfxLjvs6kj7EzkOr_MMgiujwOmyp1HMAMA4Vh31B9Da6wywSfnSfF0O8quTuKCnMennNkXtuSaizPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در شب ۱۹۹ بار دیگر به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/462329" target="_blank">📅 23:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVW61vfofsziJVwVCDrz8GQxk9EjqHPDghvW5oj1TaBzWc9YOudM_awSSSzmDBWgFa3d0yohP4Z4UwSvF1zIHvEd7LwHl0kx34neVYmVNii73G5MNL4LJH6b8_bldTP7r3UI5l8HnUORzjso_6iYLGOvY-bT6QONYrqBkCwh9VdYPeFdpwJ62vhAc2jd4YOaBf2q7B9jUl7s6HyUq3-Yxvqnf-ZPBp8mG8C8xL_6hIvURzjas0o3--DV1LOHYHZsEg6byLOhEwJB20aQW-c_NozeAjZ8JJSIT4qAxbcbU_afBvARoJJSDspneamLLDYBgf3HZvG1Xix5fAecewmyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹ خبر خوب از جای‌جای ایران
🔹
«بستۀ خبر خوب» امروز را از گوشه‌وکنار ایران تقدیم می‌کنیم؛ روایتی از تلاش و امید در سراسر ایران.  تخلیه و بارگیری کالا در بندر سیریک ۴ برابر و تردد شناورها ۲.۵ برابر بیشتر از پارسال شد
🔸
بندر سیریک هرمزگان از ابتدای سال جاری تاکنون…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/462328" target="_blank">📅 23:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5fb9fd1.mp4?token=Q5tpaz3uA7rPvqOwfpAj3l_NK9qjgme3RptnrvRROizakmyOymAoRi9vpdbGC4n_ZG-hZxJVF0tUXKLgHkySI0EjzYsA1ml-7XGbKVAnU_SXaWTHxfTOaaSWvP18gz8sYYGYNVod8NaV6v6amJ-VURuvZMtuSUbm2cH1h9PpwQEtVjcAT4TZ5vBRyM73bfo3o2eo49jnGQR8WnaWy3d9uVGxR6yT4rYWspNT3-Vao3n4ZDvJbnfsRe9RoVppOnk-WpgtrRyZYLrtqrC-CnnvJo_H_flhi30wOt_2F-X-Rxbl-KW3cAbEFJNy94a6DJEb4C9mm17xl6HaNvHdhOfEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5fb9fd1.mp4?token=Q5tpaz3uA7rPvqOwfpAj3l_NK9qjgme3RptnrvRROizakmyOymAoRi9vpdbGC4n_ZG-hZxJVF0tUXKLgHkySI0EjzYsA1ml-7XGbKVAnU_SXaWTHxfTOaaSWvP18gz8sYYGYNVod8NaV6v6amJ-VURuvZMtuSUbm2cH1h9PpwQEtVjcAT4TZ5vBRyM73bfo3o2eo49jnGQR8WnaWy3d9uVGxR6yT4rYWspNT3-Vao3n4ZDvJbnfsRe9RoVppOnk-WpgtrRyZYLrtqrC-CnnvJo_H_flhi30wOt_2F-X-Rxbl-KW3cAbEFJNy94a6DJEb4C9mm17xl6HaNvHdhOfEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: نحوۀ پخش سریال‌ها را تغییر دادیم
🔹
در این روش سریال‌ها دیگر هر روز پخش نمی‌شوند و در روزهای زوج یا فرد یا آخر هفته‌ها پخش می‌شوند.
🔹
پخش هر روزه باعث می‌شد مخاطب برخی قسمت‌ها را ازدست بدهد و ارتباطش با سریال قطع شود. @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/462327" target="_blank">📅 23:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3123fc9ea5.mov?token=e75OIi0Ux8i6_G1h-JdBvlBkZQza3oAQS3HzfiUjQiMfYUOe9Cmmg0DNJ2pcJGWTuIVX6A2B1zImKHIIADXnoIwFnc_jwBnwwg2alGyHS7pPaJ74K7IjU54fDeFeDcfb9XQcgFqMdz0x5xOujo4AZ4laAMlCmDoKu8RyR3ArvabCZxw4m3xkya-gAKBoolUOBdvbXLfP5_anK2BxCVcoH8KPr3KOfgHLfQyS1MflgbBHMWEdjoIZ9YruswFOEW-RS1CP36Giq4LIMJTOn19EGRt_Tnq5wECsE7yjgfrBSFz6AgYZxcjh_lCMdQCzjDIIsiklLdIq0OMYbLndEU0UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3123fc9ea5.mov?token=e75OIi0Ux8i6_G1h-JdBvlBkZQza3oAQS3HzfiUjQiMfYUOe9Cmmg0DNJ2pcJGWTuIVX6A2B1zImKHIIADXnoIwFnc_jwBnwwg2alGyHS7pPaJ74K7IjU54fDeFeDcfb9XQcgFqMdz0x5xOujo4AZ4laAMlCmDoKu8RyR3ArvabCZxw4m3xkya-gAKBoolUOBdvbXLfP5_anK2BxCVcoH8KPr3KOfgHLfQyS1MflgbBHMWEdjoIZ9YruswFOEW-RS1CP36Giq4LIMJTOn19EGRt_Tnq5wECsE7yjgfrBSFz6AgYZxcjh_lCMdQCzjDIIsiklLdIq0OMYbLndEU0UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی پویش جانفدا: با وجود تکمیل ظرفیت گردان‌ها، سایت برای ثبت‌نام سایر متقاضیان باز است
🔹
افرادی که پس‌از تکمیل ظرفیت ثبت نام می‌کنند در لیست انتظار ذخیره و پس از هماهنگی با نیروهای مسلح سازماندهی خواهند شد.
🔹
در کمتر از ۱۰۰ دقیقه ظرفیت ثبت‌نام برای یک…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462326" target="_blank">📅 23:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dea6cc2c3.mp4?token=hwdmIEgH3yQqbdvAKLBllfY6qbWV-fPELYa3CEFVZ5qi0_J-bdT1YrfPkx7jTdxM11HBwYVWhca6jPLvYZ4Rh-cn-TahclkEhARTv6T4ZaFUTzA3CBgcS6LJgaRWTesaHKS5UztGSnErZR5YPIbsZPdBpinZ1VbGg4qHSSPAC1XKX5Mei7c0wN8BNE42im-gn35iOlhjWGzSLyYZGUZQ0Ua5x4X3oqjFDhlWF9W07VY0oMlKLW6x2Fjwb4cGMNtxmAAjMlmnO3qx-oYhbrA5d1arzMGSq0Q1J2EH5S1hdoyHy7H0s0sBxTP_28o491cuKZkmu8nmj2buPrZCIYBq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dea6cc2c3.mp4?token=hwdmIEgH3yQqbdvAKLBllfY6qbWV-fPELYa3CEFVZ5qi0_J-bdT1YrfPkx7jTdxM11HBwYVWhca6jPLvYZ4Rh-cn-TahclkEhARTv6T4ZaFUTzA3CBgcS6LJgaRWTesaHKS5UztGSnErZR5YPIbsZPdBpinZ1VbGg4qHSSPAC1XKX5Mei7c0wN8BNE42im-gn35iOlhjWGzSLyYZGUZQ0Ua5x4X3oqjFDhlWF9W07VY0oMlKLW6x2Fjwb4cGMNtxmAAjMlmnO3qx-oYhbrA5d1arzMGSq0Q1J2EH5S1hdoyHy7H0s0sBxTP_28o491cuKZkmu8nmj2buPrZCIYBq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: هر پژوهشگری که نسبت به نظرسنجی آمار مخاطبان صداوسیما تردید دارد می‌تواند از نزدیک فرایند این آمارگیری را مشاهده کند  @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/462325" target="_blank">📅 22:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9ced33d6.mp4?token=N0eGyclVbw3OMk0C3XTDQQ4bFUreXgzvxCd56eihiXrrqyVukCRzi_e67JHtz3_uOfdvhbUb3Q41WJpDolij7h9VKJmIthXUZTrJtt7UJo9sH9T5hjh1r7Rp8nAYraHnBy4sSm6c2KayXo3R3RWWnb7u9d0yE0AGYSXxIHQShR272-jchEWDSXHI57fnuwqmZeoEcCpWVJcZPuD3bIXoHIKWxrc6N5mt60_Y8dh9p3XcIS2FoDCFEGwH7T396MDF4_NZNJiRO2FfznATrbGZiazUIhToWyFfdgIwXXJfW66dfDOmpWHKX6uFRAjrvGB32meqzyHteOda92OAgLegfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9ced33d6.mp4?token=N0eGyclVbw3OMk0C3XTDQQ4bFUreXgzvxCd56eihiXrrqyVukCRzi_e67JHtz3_uOfdvhbUb3Q41WJpDolij7h9VKJmIthXUZTrJtt7UJo9sH9T5hjh1r7Rp8nAYraHnBy4sSm6c2KayXo3R3RWWnb7u9d0yE0AGYSXxIHQShR272-jchEWDSXHI57fnuwqmZeoEcCpWVJcZPuD3bIXoHIKWxrc6N5mt60_Y8dh9p3XcIS2FoDCFEGwH7T396MDF4_NZNJiRO2FfznATrbGZiazUIhToWyFfdgIwXXJfW66dfDOmpWHKX6uFRAjrvGB32meqzyHteOda92OAgLegfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هواداران استقلال در ورزشگاه بصره قبل از شروع دیدار با السد
🔹
نکته جالب حضور برخی شهروندان عراقی با پرچم‌های استقلال است. @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/462324" target="_blank">📅 22:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fe35fcf7.mp4?token=EU6-yg0sp8nzikkaM0uTHNNCKZ_Kis_YmNZph74jxnCg_tNcyReZ5jVLgKvVPtmNyecYiT5ikFpZJLjAzGcoMLy9eNRsxVr6-crNNq51LDG4uvh5_Ks9U0XBww97pLJ9Gvv49mQMcZHye-yWLS2MWwhNRlPjPCnD8Gtk62WY-pDWh9zHLAFVUjvbPojC5UCsw9VZmkB0cdG7SUSh_ZA3lLY2VAp-e65tEYK4jjN0gPM5VLaeNbdFxAleLiV4sYP4sZIkZdYijqm4UExgcAM3ni44QBgkXNBfGErmro73V0TArZuM8Fjkn3Lu8qKUPDvX07ZMx5UJlgcM5v0CurobSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fe35fcf7.mp4?token=EU6-yg0sp8nzikkaM0uTHNNCKZ_Kis_YmNZph74jxnCg_tNcyReZ5jVLgKvVPtmNyecYiT5ikFpZJLjAzGcoMLy9eNRsxVr6-crNNq51LDG4uvh5_Ks9U0XBww97pLJ9Gvv49mQMcZHye-yWLS2MWwhNRlPjPCnD8Gtk62WY-pDWh9zHLAFVUjvbPojC5UCsw9VZmkB0cdG7SUSh_ZA3lLY2VAp-e65tEYK4jjN0gPM5VLaeNbdFxAleLiV4sYP4sZIkZdYijqm4UExgcAM3ni44QBgkXNBfGErmro73V0TArZuM8Fjkn3Lu8qKUPDvX07ZMx5UJlgcM5v0CurobSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پس‌از دوره‌ای کاهش مخاطب، از سال ۱۴۰۲ به تدریج درحال افزایش مخاطبان رسانۀ ملی بوده‌ایم  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/462323" target="_blank">📅 22:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">جلسه فوری پاکنژاد و شریعتمداری در آستانه مجمع هلدینگ خلیج فارس
🔹
طبق خبر رسیده امروز محسن پاکنژاد وزیر نفت و محمد شریعتمداری، مدیرعامل فعلی هلدینگ خلیج فارس جلسه مشترک برگزار کردند.
🔹
پیش‌تر رئیس‌جمهور دستور داده بود تا مسائل وزارت نفت و هلدینگ خلیج فارس از مسیر جلسات مشترک حل و فصل شود.
🔹
جلسه بین پاک‌نژاد و شریعتمداری درحالی برگزار شد که فردا قرار است در جلسه مجمع هلدینگ، ترکیب جدید هیئت مدیره این هلدینگ تعیین تکلیف شود.
@Farseconomy</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/462322" target="_blank">📅 22:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b661f8b8bd.mp4?token=VNBk09SJ2UGH30_46XCLQKWnKBflSmquAM1DBpa_U7vgCULQf7cYKdr-4503DtY55Bv6ThXZu1D_ubdXj4gNojwy5TjoeGDfMQ3EP_UA9qAw6sRrp-Ig4S8K-kOfUurDvZ4WPpTAakvwdkYjHoxSu6a_FCXDly72xd9FRSVxhNtIIqWFnpgVPzHX2G_Nyr21RmpUtcyBGPIicDB01HDyYAdjVlKzE9hT7wGyu7N0LcJH1I4JTnt2mSZLoFqGv9AIbaur7XeTDdPaswN7ZkCIk2d7ymeZovfYeIHutWBcwnWpFKDEXj-g3vaTelgJ6iBedCmLgfgPGwg3MC10jUpCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b661f8b8bd.mp4?token=VNBk09SJ2UGH30_46XCLQKWnKBflSmquAM1DBpa_U7vgCULQf7cYKdr-4503DtY55Bv6ThXZu1D_ubdXj4gNojwy5TjoeGDfMQ3EP_UA9qAw6sRrp-Ig4S8K-kOfUurDvZ4WPpTAakvwdkYjHoxSu6a_FCXDly72xd9FRSVxhNtIIqWFnpgVPzHX2G_Nyr21RmpUtcyBGPIicDB01HDyYAdjVlKzE9hT7wGyu7N0LcJH1I4JTnt2mSZLoFqGv9AIbaur7XeTDdPaswN7ZkCIk2d7ymeZovfYeIHutWBcwnWpFKDEXj-g3vaTelgJ6iBedCmLgfgPGwg3MC10jUpCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پس‌از دوره‌ای کاهش مخاطب، از سال ۱۴۰۲ به تدریج درحال افزایش مخاطبان رسانۀ ملی بوده‌ایم  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/462321" target="_blank">📅 22:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/462319" target="_blank">📅 22:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4695adcd.mp4?token=m1LpT1XZaZQAiFEV_Be_B6_dR9zwOsbQl-xWklz3D8NNZRFKAfbLgIeM45CJrzlAeHgVE68KFLkxWRI-B3YaLPSiqgH52FwzBJtTNXlMeeZipv5H1rVq1gX9u2kR59Pecuekmggj_dgrHc--CfzzgiBz6sZEqGdiNoFpsiAinMFU2S0ZTTiNC_TCz5OVOh80FfxcbXuYkjBcNVwXG8WePWnjGiaXSF-WZniLGAUaaL6QHSzoKD26s1-kE9J9AkBx9s9aCL1sU_qRuSjaDyaBHjUfRltEP5DjqqNWa-pRPBznULQ9LtX_X55YqTsSA_VPufxuo86qWQiiZj0_vwKXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4695adcd.mp4?token=m1LpT1XZaZQAiFEV_Be_B6_dR9zwOsbQl-xWklz3D8NNZRFKAfbLgIeM45CJrzlAeHgVE68KFLkxWRI-B3YaLPSiqgH52FwzBJtTNXlMeeZipv5H1rVq1gX9u2kR59Pecuekmggj_dgrHc--CfzzgiBz6sZEqGdiNoFpsiAinMFU2S0ZTTiNC_TCz5OVOh80FfxcbXuYkjBcNVwXG8WePWnjGiaXSF-WZniLGAUaaL6QHSzoKD26s1-kE9J9AkBx9s9aCL1sU_qRuSjaDyaBHjUfRltEP5DjqqNWa-pRPBznULQ9LtX_X55YqTsSA_VPufxuo86qWQiiZj0_vwKXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ ترور مولوی یوسف گرگیج در زاهدان  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/462318" target="_blank">📅 22:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/462317" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e076801b.mp4?token=HPBBmzTTqC3YcnUoqFihwG3bMk9rK7S90u2u_gFCpolabTYImCIvXg532RuH4SOFb--8BQ5ifSyZpUHHwGRQKbHm3k6zamQSfjbHR4NrdAMLbu-goGQ46Yv0-ESFCVz3ZS_ZWYxTKdFD9LYXrridAqFsPzY99miz6t7PoP2S1eGJa_R3Av_MKJeoy7dIm8NaMVUVeOpBlLj100azwSV0_RPI3ZM8nfEAvPwV0F_AhzeYRaFDT1ELhdlGq6mApWrMuEJlOOAxWJbqnUxM72YYIaTxeJ3dpNG6h4XD0fmS-6Mo9wc1PPqIKcDyMhj7Lym0TDmwfMdM8CPVOT-OGPkuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e076801b.mp4?token=HPBBmzTTqC3YcnUoqFihwG3bMk9rK7S90u2u_gFCpolabTYImCIvXg532RuH4SOFb--8BQ5ifSyZpUHHwGRQKbHm3k6zamQSfjbHR4NrdAMLbu-goGQ46Yv0-ESFCVz3ZS_ZWYxTKdFD9LYXrridAqFsPzY99miz6t7PoP2S1eGJa_R3Av_MKJeoy7dIm8NaMVUVeOpBlLj100azwSV0_RPI3ZM8nfEAvPwV0F_AhzeYRaFDT1ELhdlGq6mApWrMuEJlOOAxWJbqnUxM72YYIaTxeJ3dpNG6h4XD0fmS-6Mo9wc1PPqIKcDyMhj7Lym0TDmwfMdM8CPVOT-OGPkuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پایبندی به هویت اصیل ایرانی-اسلامی می‌تواند مخاطب را جذب کند
🔹
محفل و معلی ثابت کرد می‌توان برنامه‌های معارفی را در فرمی جذاب ارائه کرد که مخاطبان زیادی داشته باشد. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/462316" target="_blank">📅 22:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dealTjrnWbciF1Mqtl-pxaYsRVEUb3LIyyH2IarbYASm8pYx4KqzUibyDFitLQ-IdNFoqTCBrQlUw0sv2RA0mBF0qLUss010PGfKIKC9EF1QlusnJV_qWNvfEKGp-8x5ICanFRzLSRlh-STkcOqU_Q2Sb57gywN2db3Cva2e2GvT1AKzCuUqN1Jyed6sO7_wBRwJ9NLH2GjSyNUP6XojMVW2xC-HM2G_vCFMXgUZJ5N08bWMjVcA4eR4jpFOmXNk2lEXU4cqzn_miDPts3yjLjfRyNtCvnVpXRcLaIsCBCnKaH1OeeWh5Dyboj_mfXYbHRF6P5x2racRDNL39axMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست محرمانه در آلمان؛ همگرایی نادر فرماندهان اسرائیل و کشورهای عربی
🔹
رادیو ارتش اسرائیل به نقل از سخنگوی سنتکام اعلام کرد براد کوپر، فرمانده این نهاد آمریکایی هفتۀ گذشته در آلمان میزبان کنفرانسی با حضور ایال زامیر رئیس ستاد ارتش رژیم صهیونیستی و فرماندهان ارتش‌های عربستان، امارات، قطر، کویت، بحرین، اردن و مصر بوده است.
🔹
سخنگوی سنتکام گفته: کوپر طی این نشست به همتایان خود اعلام کرد که ارتش آمریکا با وجود حملات ایران که پایگاه‌های آمریکایی را هدف قرار داده بود، قصدی برای خروج نیروهای خود از خاورمیانه ندارد.
🔹
به گفتۀ او کوپر در این نشست، گزارشی هم دربارۀ طرح آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز ارائه کرد.
🔹
این نشست نخستین نوع از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران در بیش از شش ماه گذشته بوده است؛ گرچه دیدارهای مشابهی بین فرماندهان نظامی صهیونیست و عرب در گذشته نیز برگزار شده بود.
🔸
رژیم صهیونیستی پیشتر سامانه گنبد آهنین را برای رهگیری موشک‌ها به همراه نظامیان این رژیم در امارات مستقر کرده بود؛ اسرائیل همچنین کمک‌های فوری در زمینه‌های اطلاعاتی، نظارتی و شناسایی از جمله اطلاعات مرتبط با حملات صورت‌ گرفته در ایران، در اختیار ابوظبی قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/462315" target="_blank">📅 22:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808a7154a8.mp4?token=kY4nwtjh7ftYdo8wXxCFGFxlYhJqS6rWTQ-UIiOpbceDD7zt6fKDYX2ZGceF3_ywU5xNrYXC6Zly4jKvJyRtHwOPcFTOBf8tlKUiqoHHkcQ3EDfkhuNMHOeVSOnjQNo3juNxpxxpsuW4hFkLr-VovY99Hu-X7OZuTFnrhB92oyST5JTh9WUtb45tiizqTQRsdCq_4drZR9EM0gA5clpB9pntx-jm3gtIFB6_KUfnJc2ZRNPWjNuxq6vLX5CsLNk3lBIaZyxNEOywgDctU4vOxGNSvpnfhgJT9hq6QKgx95_QaAB-hIykhm0vOYJozoyhe4HlU8koEl5XWo9hbnrjKnZMBfW74PMu0lHC0vlV6mJWPeYRO1eb12LNDCQn4SL-6ZHEzGJKa8qNi_S5R5720hCkml2_qjcLgXk5nAXbt622BxgaAVQZpQq1tDhpJIn9s8uQwtewvTM0tYpN4i7luB9lC9tMff5zHH577wMPZQng5VrX-FVzPNIV66ORmlDXJEJBvrIJD6DPPaatWu0hBUkTxNII_yTUc4MzoLS38Jp_9JQZShpZ8yp2zZzaZUmBkaHIqRdx-osmcpUMsWVdeMQBL21tH0Zf7Iha2713x9sPhY6cfp9FZ6_zkVVmWbIxaCh7IMS0ALPgwPQAKASppVeGGug5HJ5YIrBbbvS_sqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808a7154a8.mp4?token=kY4nwtjh7ftYdo8wXxCFGFxlYhJqS6rWTQ-UIiOpbceDD7zt6fKDYX2ZGceF3_ywU5xNrYXC6Zly4jKvJyRtHwOPcFTOBf8tlKUiqoHHkcQ3EDfkhuNMHOeVSOnjQNo3juNxpxxpsuW4hFkLr-VovY99Hu-X7OZuTFnrhB92oyST5JTh9WUtb45tiizqTQRsdCq_4drZR9EM0gA5clpB9pntx-jm3gtIFB6_KUfnJc2ZRNPWjNuxq6vLX5CsLNk3lBIaZyxNEOywgDctU4vOxGNSvpnfhgJT9hq6QKgx95_QaAB-hIykhm0vOYJozoyhe4HlU8koEl5XWo9hbnrjKnZMBfW74PMu0lHC0vlV6mJWPeYRO1eb12LNDCQn4SL-6ZHEzGJKa8qNi_S5R5720hCkml2_qjcLgXk5nAXbt622BxgaAVQZpQq1tDhpJIn9s8uQwtewvTM0tYpN4i7luB9lC9tMff5zHH577wMPZQng5VrX-FVzPNIV66ORmlDXJEJBvrIJD6DPPaatWu0hBUkTxNII_yTUc4MzoLS38Jp_9JQZShpZ8yp2zZzaZUmBkaHIqRdx-osmcpUMsWVdeMQBL21tH0Zf7Iha2713x9sPhY6cfp9FZ6_zkVVmWbIxaCh7IMS0ALPgwPQAKASppVeGGug5HJ5YIrBbbvS_sqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پایبندی به هویت اصیل ایرانی-اسلامی می‌تواند مخاطب را جذب کند
🔹
محفل و معلی ثابت کرد می‌توان برنامه‌های معارفی را در فرمی جذاب ارائه کرد که مخاطبان زیادی داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462313" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf0c3c353.mp4?token=XSeDut8uA1sgdMjij0FqX5-jXvNKvFO_TZP0ZydKzkuoiGMcpTVuHWO2GD6q-rm7SVLT-lv6q4gvvcjZpShypiml3TUImuO2hvc3qCeKQg0oZsgB4OJo9nwcxy1VPWepqOVWbu6SYUOcwx1z4Sp5hYgzksmPZkTua8XjjbrjdJ9Ggyuo4Msiu_arH5AH2tqTOEv6wTHPaqXzKewnmUu9RC3DMeUVHGRfn_YBXgPoaJgSyfCodz_9RBjogwGgz0U04SVPi9eiGbPO7WAzie5a_pN7V81YA3eYNlLvWwP13ybXMtpSUhDuk9UBYRbcrMjvABXSWhotJkhH1coS3ANoOSdKcZQeh0D1ibThl-yhyTbZA2HEO1eDGzb_kZ6H_fEsBJkGolWGwAwKRBpJ8nzklkD2ys9g6KwDmI12a-R8inNjKDUdx-GJfarZZCec03zdRRb8bd-I44_Z1G25edgFeBMrSFyEXkfsHZjm5hQa-bC6dgh1RZoYoLz-POnwP34Nu0PnCBXnvBrLbAO4QdenO8Bi2_r8tNzeR7gJhKbUnayr-wc-YNFHY8g_iLYhuIl7whZYOcvPFP0GpYmQC2RZ4QnwSopdOVB41LVMHGn5DJe28m-9iWdaEB49e8UJAjXoK8E9KF8smvL9xxCwcs3IktEfy0kds-g3VOmDuREaIx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf0c3c353.mp4?token=XSeDut8uA1sgdMjij0FqX5-jXvNKvFO_TZP0ZydKzkuoiGMcpTVuHWO2GD6q-rm7SVLT-lv6q4gvvcjZpShypiml3TUImuO2hvc3qCeKQg0oZsgB4OJo9nwcxy1VPWepqOVWbu6SYUOcwx1z4Sp5hYgzksmPZkTua8XjjbrjdJ9Ggyuo4Msiu_arH5AH2tqTOEv6wTHPaqXzKewnmUu9RC3DMeUVHGRfn_YBXgPoaJgSyfCodz_9RBjogwGgz0U04SVPi9eiGbPO7WAzie5a_pN7V81YA3eYNlLvWwP13ybXMtpSUhDuk9UBYRbcrMjvABXSWhotJkhH1coS3ANoOSdKcZQeh0D1ibThl-yhyTbZA2HEO1eDGzb_kZ6H_fEsBJkGolWGwAwKRBpJ8nzklkD2ys9g6KwDmI12a-R8inNjKDUdx-GJfarZZCec03zdRRb8bd-I44_Z1G25edgFeBMrSFyEXkfsHZjm5hQa-bC6dgh1RZoYoLz-POnwP34Nu0PnCBXnvBrLbAO4QdenO8Bi2_r8tNzeR7gJhKbUnayr-wc-YNFHY8g_iLYhuIl7whZYOcvPFP0GpYmQC2RZ4QnwSopdOVB41LVMHGn5DJe28m-9iWdaEB49e8UJAjXoK8E9KF8smvL9xxCwcs3IktEfy0kds-g3VOmDuREaIx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادری که با ۱۴ هزار صلوات برای امام زمان(عج) از شهیدش باخبر شد
🔹
شهید علیرضا رمضانی فرمانده ناوشکن جماران در سومین روز جنگ تحمیلی سوم پس از حمله وحشیانه آمریکایی- اسرائیلی به این ناو، شهید شهد شیرین شهادت نوشید و جاویدالاثر شد.
🔹
در آخرین تفحص از ناو جماران که با سفر خانوادهٔ شهید به کنارک در جنوب کشور انجام شد، بخش هایی از وسایل شخصی این شهید پیدا شده و عملیات تفحص همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/462312" target="_blank">📅 22:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb8fa557f.mp4?token=qDVxj8pWM1TMIaP0E351W3smMw8ad2p1oceiSyiSg7lTR8lzJugo5kxhGBRU1eIyQuqZZFiRaGGJDzFcLRJpHGfPbYyjdcWnm5n4M3i3IfHiSamQq7wuiXdoeWyNnCZ70cjpwreZp2BUJfWAjDao6RzOTEjAqGXXUsMBd9HNX83K2BvRpPuotgux6cIcghtYMq_WVkJtV0gLGP5m86pW8zBZS4VRS_w__9arqLo5HEj4Scl4GPRqxwF8ZB5DWip6uuDeCnnGphigSxLyBVqy4QJD-aTrOI-gbVRbopUq70-Q8gwKibnNIYkArY58N9-BzmI6lZRWNXHcH-clNwieeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb8fa557f.mp4?token=qDVxj8pWM1TMIaP0E351W3smMw8ad2p1oceiSyiSg7lTR8lzJugo5kxhGBRU1eIyQuqZZFiRaGGJDzFcLRJpHGfPbYyjdcWnm5n4M3i3IfHiSamQq7wuiXdoeWyNnCZ70cjpwreZp2BUJfWAjDao6RzOTEjAqGXXUsMBd9HNX83K2BvRpPuotgux6cIcghtYMq_WVkJtV0gLGP5m86pW8zBZS4VRS_w__9arqLo5HEj4Scl4GPRqxwF8ZB5DWip6uuDeCnnGphigSxLyBVqy4QJD-aTrOI-gbVRbopUq70-Q8gwKibnNIYkArY58N9-BzmI6lZRWNXHcH-clNwieeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقامت بروجردی‌ها در خیابان به شب ۱۹۹ رسید
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462311" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9927c80529.mp4?token=lSPpvTfyTjF4s8N6I9BmaB4TpPmuU9riAWBpZsqgJWfSeyi24XTs4QESf_GD6lwcSr2xt7WV1t4_Wk49ElxgRWwtASepOKEiB6vpYYj1gGzmrhQ0gAAbTwRiW94VxAAdx44gqmrwd3bJTLm7uOJWNUyIW5S-1Gzfs3OMD14Zw6d9_G_e9TBO26Y1M75h5sFmvV-lL3SdE_4y_q8dOMnuu3PLwEdbAbQJkhAvDDz6T6_b_83Qlnu1b6IoragzhHMmvTWVRv8DmkiDoU4vsjQzKaIzABMBJy-vo1qsNYb76qdfsCSnW5pHpyeD1LKz1PKRAvm-5Fe8u-LExncucQoGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9927c80529.mp4?token=lSPpvTfyTjF4s8N6I9BmaB4TpPmuU9riAWBpZsqgJWfSeyi24XTs4QESf_GD6lwcSr2xt7WV1t4_Wk49ElxgRWwtASepOKEiB6vpYYj1gGzmrhQ0gAAbTwRiW94VxAAdx44gqmrwd3bJTLm7uOJWNUyIW5S-1Gzfs3OMD14Zw6d9_G_e9TBO26Y1M75h5sFmvV-lL3SdE_4y_q8dOMnuu3PLwEdbAbQJkhAvDDz6T6_b_83Qlnu1b6IoragzhHMmvTWVRv8DmkiDoU4vsjQzKaIzABMBJy-vo1qsNYb76qdfsCSnW5pHpyeD1LKz1PKRAvm-5Fe8u-LExncucQoGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/462310" target="_blank">📅 22:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673a007c26.mp4?token=oGptYQKgJDGRyH7g12HEyQ_cKMUYVbcgfnadl3ZLPRi6d7OzsDeR29VMg057ZdblgRHuvrh2V1pz3f5xs6R6DmTEhiIzJW-4rUlvELlTEIP0o4UIxAwgYFi7gfBxTMtx78sLnK13A_GHrRxgehP9RKL0wR_xEX9IA6oTwEmyTmPJAIQh8IsPzBxDiW180-gz62LLHFiVs7LBOCuaDRjNvM2kPzU_d8iCYg8tlAMu2GskyzVAoDydR1cpCzbWM4jtLp-bF9EWNZmIKhF6SK2YT5ILxNEXx38CpQje3JnT9Smaje01r4qST2jXHtP46S_KsRPMT7Dxe3x3WremyLakzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673a007c26.mp4?token=oGptYQKgJDGRyH7g12HEyQ_cKMUYVbcgfnadl3ZLPRi6d7OzsDeR29VMg057ZdblgRHuvrh2V1pz3f5xs6R6DmTEhiIzJW-4rUlvELlTEIP0o4UIxAwgYFi7gfBxTMtx78sLnK13A_GHrRxgehP9RKL0wR_xEX9IA6oTwEmyTmPJAIQh8IsPzBxDiW180-gz62LLHFiVs7LBOCuaDRjNvM2kPzU_d8iCYg8tlAMu2GskyzVAoDydR1cpCzbWM4jtLp-bF9EWNZmIKhF6SK2YT5ILxNEXx38CpQje3JnT9Smaje01r4qST2jXHtP46S_KsRPMT7Dxe3x3WremyLakzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب تهران به عطر حضرت عبدالعظیم(ع) نفس کشید
🔹
فردا سالروز ولادت حضرت عبدالعظیم(ع) راوی حدیث و مورخ برجستۀ شیعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462309" target="_blank">📅 22:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای
وام ودیعه مسکن
که نیاز ضروری هر مستأجر است، چرا باید دریافت وام به داشتن آشنا در بانک وابسته باشد؟ وقتی به بانک مراجعه می‌کنیم، می‌گویند اگر داخل بانک آشنا داشته باشید وام به شما تعلق می‌گیرد! این چه روالی است؟
🔹
ما در زیباشهر،
منطقه ۱۱ زاهدان
حدود یک سال است پیگیر
برق مجتمع
خود هستیم. اداره برق ابتدا اعلام کرد اگر فاصله شبکه بیش از ۵۰ متر باشد، هزینه ترانس و شبکه بر عهده مردم است. اکنون شبکه در فاصله کمتر از ۳۰ متری ساختمان اجرا شده اما همچنان همان مطالبه را مطرح می‌کنند. لطفا این موضوع را پیگیری و رسانه‌ای کنید.
🔹
از ساعت ۵ بعدازظهر به بعد،
دستفروشان در بازار و به‌ویژه خیابان ۱۵ خرداد تهران
آن‌قدر بساط پهن می‌کنند که
عبور و مرور مردم تقریباً غیرممکن می‌شود
. چندین بار با ۱۳۷ و ۱۱۰ تماس گرفته و موضوع را گزارش کرده‌ایم اما با وجود وعده پیگیری، مشکل همچنان ادامه دارد. مردم واقعاً ناراضی و کلافه شده‌اند.
🔹
چرا
وضعیت حجاب در کشور
به اینجا رسیده است؟ ما این همه شهید دادیم که امروز شاهد چنین وضعی در جامعه باشیم؟ انتظار می‌رود پوشش زنان متناسب با ارزش‌های اسلامی و فرهنگی جامعه باشد، نه اینکه هر روز شاهد گسترش پوشش‌های نامتعارف در خیابان‌ها باشیم. خواهش می‌کنیم مسئولان به این
دغدغه فرهنگی و اجتماعی مردم
توجه کنند.
🔹
بنده سال ۱۳۹۸ از
تعاونی مسکن کارکنان شهرداری شهر جدید مهستان کرج
امتیاز یک واحد آپارتمان ۸۵ متری خریداری کردم. اکنون
پس از گذشت هفت سال
بنده و خریداران امتیاز واحدها که حدود ۴۰۰ واحد هست،
بلاتکلیف هستیم
متاسفانه هیئت‌ مدیره‌ای هم وجود ندارد که به ما پاسخ دقیقی ارائه کند.
🔹
در بحث
سهمیه و افزایش قیمت بنزین
، موضوع
تاکسی‌های شهری
کمتر مورد توجه قرار گرفته است. برخی ون‌ها و تاکسی‌ها عملاً فعالیت مؤثری ندارند و به گفته شهروندان، سهمیه بنزین خود را می‌فروشند. خیابان جیحون نمونه‌ای از این وضعیت است؛ برخی خودروها سال‌ها جابه‌جا نمی‌شوند و با وجود گزارش‌های مردم نظارت کافی صورت نمی‌گیرد.
🔹
لطفاً در برنامه‌ها و گزارش‌ها بیشتر به
معضل ریختن زباله در طبیعت
و مناطق محل زندگی مردم بپردازید.
🔹
سال‌هاست مجتمع‌های آموزشی مدارس روستایی غیرفعال شده‌اند. با توجه به کمبود دانش‌آموز در هر پایه، بسیاری از کودکان روستایی یا مجبور به رفتن به شهر هستند یا در کلاس‌های چندپایه تحصیل می‌کنند که کیفیت آموزش را کاهش می‌دهد. درخواست داریم
مجتمع‌های آموزشی ابتدایی روستاها مجدداً راه‌اندازی شوند
تا دانش‌آموزان چند روستای اطراف در یک مجتمع، به‌صورت تک‌پایه و با معلم جداگانه تحصیل کنند.
🔹
مدتی است به‌عنوان
پیک موتوری اسنپ
فعالیت می‌کنم. امروز در محدوده حرم مطهر، طی دو ساعت سه درخواست «اسنپ‌بایک» از سوی
مسافران خانم
داشتم. راننده پیش از پذیرش امکان اطلاع از جنسیت مسافر را ندارد و با لغو سفر نیز حساب کاربری من به‌دلیل لغوها مدتی مسدود شد. خواهشمندم مسئولان و شرکت اسنپ این موضوع را بررسی کنند و با توجه به اینکه اطلاعات هویتی کاربران بر اساس کد ملی ثبت می‌شود، درباره امکان مدیریت یا حذف این سرویس برای مسافران خانم در محدوده حرم مطهر رضوی تصمیم‌گیری کنند.
🔹
لطفاً موضوع
پرداخت معوقات فروردین و اردیبهشت بازنشستگان
را به مسئولان یادآوری و پیگیری کنید. هرچند این مبالغ در این شش ماه ارزش خود را از دست داده‌اند اما هنوز خانواده‌هایی هستند که چشم‌انتظار دریافت همین معوقات هستند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/462308" target="_blank">📅 22:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جاده چالوس از ساعت ۲۲ دوطرفه می‌شود
🔹
رئیس پلیس راه راهور فراجا: محدودیت تردد در جاده چالوس از ساعت ۲۲:۰۰ امشب رفع می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462307" target="_blank">📅 21:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQdOw6t25A4BcaYNIIGgPrI-tiTjeFhy591008zALjnKIwfe2-1xJWiW0YTNPHL22PZ3UMI8jeEuS7gBGkRoUPF6A9no7Cp7S4fBNjN9duV9LBNjEoyKHUIbyVynNaooLeisWRtSTcDrfGuFM-wcil_nO5J5L2Xb0az3qfk8SB9czCjMVdPKa7p4NAukMSVMdqhoSdxVDkR-xAME7AdYnka-3mXA-NlB9PAlyosWZpYphaqG8kT1qFLy0jKwzOxiSb_r_7Da9nfu9CdlOYxnLh77WvFkcasO37Aw_Y6_03rF8bUAHfPYSuL9RMENOnsCGzg2XiO4Ta5F79DBq7Xnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5ZOlpL4RxA8EhGF8yz4eoT4DCENnnQLowKDx2_AbduxeI8ty2_a0tdvN3wlKK2cPHh8tvvrPDo5a4jn8V0s6MQj8BWRXZjVmDiPqcjpvYMsk7eqmOJjRkEm9I3TDbhtBgJ-nFQumE2qMBc0D-97dIg26vX3gB2ug5bbPAosyBRSCFIuwllkb56LJHbsGfxMES1l-vqgXKQl8NUAU2AAEhMXbXHVq21Bu2PBo5zX8HbuAy2A4wPcce1_bD285OOl02_W5ZOALgM2Uvadl3Htp2HpYXM6ffKOTTM5gXwPPvSB8JVHw7Q0ylAaUQc-Qp12aud34DJcH5z6s07o4B-8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmWtbgM0odkqUxGzA624_ksbbxu246vBT3nYs-MHLN_kGJFxceQIdc9J5g9iZ7UeaBFaRtv8hvzyPKTpjq4zfTeLI-S4Frh0qB2BfMQmsgT4bl4oXgSlRi-W8C_epIDyOGteFZ3IFSdFUFyLonY6IxMActEf-cN1CygoD19xD9O5iterYdF9i0jRy7pqdovydT41CUThhEbWr3B1bdEO0iOtqbegSoODqVhlUlvb60dkFVN0bXnNMuW0FY3Vzi733YwR_RxU8A2iOZReOBf623g5eCOrDYbeWrHu-5O9y4g9yOSPjbuJ9fmY8QsotjDZzuXV4NoJvhzLr2YDRHNbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km7necAJdVxYALkXQKzbhhIXiMj4jLOoxxScZRjPPnkOKir6QgK-mEvid6pRnUKsH4xW6JN0fl4p8epPBJpkUjrQeFmIOaske3CA91CmLupaKa7DfwuTxRlgIyTVCs-cL4Z3E4u50PKxiIQMPYyhwZQN_haiaRakayjBWlcAlycEIbVMRh_qxHmnavoO1jhjKzumPrIB0AVx1CkyHoR1kdSgopo9NkN6m9ZyAEgHcPtSKi0XcJ62o_07DjxY4lv60gdKoXlc1SZesHuNhYJAp-S_FVy1Mn3p77QlRRzXg8xHMjAg1mMtkZIp324dhgr6S_MvY9d8osg6fnkJhMeNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE5y8h32EWqukRjtnzNwYt9G10nCKawb3tck8tQ6jPYaIFKO-w50rGF-k2f5t7yawqF9iWLge1gKhPTyWDnPgszZbsIfdZoTJypbcOaZ-ZoT9B8v52326_PqE8MyIp3rVhZP8wu5nQ992pHuxz7Rtx8xeP-w1oyaERI4f0oJTW4ICWrBtd9ie4EtJf0Kmd7pc8MGynF2BaTCQT1T9EEpVf4t03vpwNf8xWRUQMzyGzdAb6cT-eS-pL54NABTbGDyBLU5KknZ41HDNc58J1-MN11PFac9RQu1tYStySXonS55Y6oxBPvEdpm4xMipW__RtvAqxTgXAXgLRyoOgsfizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5lQjmuPv8aRg7PtgYFBHD_hWuOJNApedd9N_aoYhG22lhuxkLnhTezwLWFEnlTwNG7-o0P5LtR1Bo0rrmmle-FIYRNB3rejkjq-uFZXzGqR_0y7fwJG39SE7ga2dtTV66Bm6B3BvLHnZCHWemHO-qa5tUz2pkDvmdQaiQwqTBKQbf6rkhWvA-Xe4I3PJDs81vmHSNTkjTFwoSgBBoPyO4fmKOJb4HZHv6gGwADAlSdniAC-w3CMEn-hTUNYyGM8l76GCy9MofHwWVDHEsNE1zTqp7r_fNaftG-oBVC2I4iGra7C_ePKv940xkeBHRhzUUpe6pelzlKGxrGv_L-svQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWtuXuO1wApC4EvN9aWXf44ebvAQRQ2pS5FrdESXf1f-R6U_R4VUZFHRxuaMttP1pjeYztCMjpyxzNa7Y8-qC_TVZJ3--bb46u27cNWuytnx-p-XFhIyooFoBkfQEvdPUytn1lM4NngDOZCOGqkUgqFFWh54NfQas4YY5JtUxwVS_oicHzheyrZaYkyMMD1uqdYcHm-RaAp-07h2Yaf7a9XR_ZdURnJJDulpPnkfJbuS_qKC83AlgQx1f7n8ANi31_KN3M_yaQ4CZOldyDYhXADzmuicDb01QLpcs3PKGtkp2Q4C5AIOVvD9OqWYmsD3BpQhHpsQxnSNDG_6wkSBhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هفتمین نمایشگاه بین‌المللی خودرو تهران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/462300" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e5ba6a3.mp4?token=KiUSuYzgw69RatUD4AAAf5bcYb_9eO-JUvrRdm3kTUlOC9sax3xVpLtZMFRrS-RJWztmeUcXBaJpxg86F6X523BNBAEd3IevRQfk6tL1LPizuiM-ZZ0QLQNi5Kp19JF1hZxyajN_QDMXg5dxpVJ2xn8QGsmA8ZeGmIdeKuVhlDzLqYWWEVBwpnw5Gep1nROYCMZnHDlD1SUL6AG5QSBFvTEpCVFodtdRF7TvyJIzF5vwU5JKE6w_Tkm3m6ghfzjpqOmcsfYrFCL4Xj34K03wdpxR-9n4cEzdDiEgCWugZcaqgIU86hPhbI-SXt3plDx0qgPRVNFNjw3X7kyD6dhrDQpwl-MMVLV1BlWRyA2TV_PBu6jEhoJ_xwxGxuUHb4G3cz1Ypc79st5pv33l0L15MVteE4uaP2FDqHDnIEJi93FGQqW4a5ytzm-I2R72_g5tW_vWQOC75_7XdxE6SdD0xSSDJhc5NAYHfzX9zJWs3ixIZI94dcnQbU64br31ODzpNhM6KsShOLpfqzdNbk6Kn9FiF9ZlMe8e9_ZHeUdglub1l-AWQdIstGZWKAKlR_ULBy1lJT3cQezjB9YA11Fs2HPdVXS5Q1U1r63AExxf13Rc7-RWLc0vgAsHE0czO1phhkrVU1XYbpSYwUAEtJOBq3A_XZ6TmyOA_3TPJ4cZNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e5ba6a3.mp4?token=KiUSuYzgw69RatUD4AAAf5bcYb_9eO-JUvrRdm3kTUlOC9sax3xVpLtZMFRrS-RJWztmeUcXBaJpxg86F6X523BNBAEd3IevRQfk6tL1LPizuiM-ZZ0QLQNi5Kp19JF1hZxyajN_QDMXg5dxpVJ2xn8QGsmA8ZeGmIdeKuVhlDzLqYWWEVBwpnw5Gep1nROYCMZnHDlD1SUL6AG5QSBFvTEpCVFodtdRF7TvyJIzF5vwU5JKE6w_Tkm3m6ghfzjpqOmcsfYrFCL4Xj34K03wdpxR-9n4cEzdDiEgCWugZcaqgIU86hPhbI-SXt3plDx0qgPRVNFNjw3X7kyD6dhrDQpwl-MMVLV1BlWRyA2TV_PBu6jEhoJ_xwxGxuUHb4G3cz1Ypc79st5pv33l0L15MVteE4uaP2FDqHDnIEJi93FGQqW4a5ytzm-I2R72_g5tW_vWQOC75_7XdxE6SdD0xSSDJhc5NAYHfzX9zJWs3ixIZI94dcnQbU64br31ODzpNhM6KsShOLpfqzdNbk6Kn9FiF9ZlMe8e9_ZHeUdglub1l-AWQdIstGZWKAKlR_ULBy1lJT3cQezjB9YA11Fs2HPdVXS5Q1U1r63AExxf13Rc7-RWLc0vgAsHE0czO1phhkrVU1XYbpSYwUAEtJOBq3A_XZ6TmyOA_3TPJ4cZNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع و تدفین دریانورد شهید جمشید رجبی در بندر امام خمینی(ره)
🔹
دریانورد جمشید رجبی درحملۀ چند روز پیش آمریکا به کشتی کانتینری در حوالی جزیرۀ قشم به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/462292" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUcZ13ONuX0_t_Eb9THwP8IBrfjWmvkZ-7pOR0xSYQ1_5equJ8xXXEGVVXOqYlqC9QMiSMf7F8uTI0hvovYFZT1R3pAc9Ws-Nxi_py9-StjVULWaR6vGQe4X9iTwMt8yRojNj_LBSE6-8t6z_4q8oKa1iYONVmncKg0ACu9IVtBZdxI-ddHv6kfSAjnoTdR3NLI4d1XnuNkEIgMCXPWlY3eMrBM0ljxuLA9i7sp7ZpwuPdyRG_oK75EdyeqFYIVXE_yozdmnFde4SawDHn6lvb-s8ZlsMYOoiPHRh71pUlgP3ezjvdq62VeIVGZZBfZWJ2cO71-Qeuh-fH5DlcG7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهام‌های روایت آمریکا از عملیات نجات خلبان F-15E
🔹
خلبان F-15E آمریکایی در مصاحبه خود مدعی شده پس از اصابت موشک ایرانی، با چتری آسیب‌دیده و سرعتی تا حدود ۱۶۰ کیلومتر بر ساعت با زمین برخورد کرده و با وجود شکستگی کمر، بازو و شانه، خود را به ارتفاعات رسانده است.
🔹
امیرسرتیپ دوم خلبان عباس رمضانی، خلبان پیشکسوت نیروی هوایی ارتش، می‌گوید: این روایت از نظر فنی و پزشکی نیازمند مستندات بیشتری است؛ به‌ویژه درباره سرعت واقعی برخورد و میزان آسیب چتر.
🔹
افسر آمریکایی گفته برخورد تقریباً با سقوط آزاد و سرعت ۱۰۰ مایل بر ساعت رخ داده، ولی برخورد با زمین با چنین سرعتی، آن هم در شرایطی که گفته می‌شود چتر نجات پاره یا دچار نقص جدی بوده، موضوع ساده‌ای نیست و زنده ماندن پس از آن بسیار بعید به نظر می‌رسد.
🔹
رمضانی با اشاره به نحوه پوشش رسانه‌ای عملیات نجات، آن را فراتر از یک عملیات نظامی دانسته و می‌گوید به نظر می‌رسد آمریکا تلاش کرده از این حادثه یک روایت تبلیغاتی و روحیه‌بخش برای ارتش خود بسازد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/462291" target="_blank">📅 21:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN53aM-4hQ8Rj6cRKDmmxEzGejI4KHA1Jx7IC-cvd79CIo8lrZfhORhDF6jMtbZ7uGt9oBFsgzVGtpi0lVUitrgT-xnGsybVP-4dggqfVVgJCikjRm0bZwYAtGS12EDvgDXunI0lyIEaSCGNgn9avNJS1FCsydi0Kxa3gz9ep5WztSydPSHTt8PnnmH_h9w_C3-06A3vKWLdBLaQz5zZo0A7eyjg1xUJwY_c8yzIQD8o030svp3TymNswZAD-t9RZOoT-bAeZBw2vzvLFa2gk8hyCggtGUD8-LCA_At7WRiTo5M6_b3uJ8TUcrBWMdhL78-FogmClm6xP_5MHy33EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید مولوی یوسف گرگیچ فردا در زاهدان تشییع میشود
🔹
پیکر مطهر شهید یوسف گرگیچ فردا صبح از میدان امام حسین تا گلزار شهدای شهرستان زاهدان بر دستان مردم شهید پرور زاهدان تشییع میشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/462290" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
آغازی بر پایان حبس بدهکاران مهریه
🔹
مصوبات جدید مجلس برای تعیین سقف مهریه و حبس‌زدایی از قانون محکومیت‌های مالی را ببینید.  @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/462289" target="_blank">📅 21:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g59ypq6-lPQ1G1W3d6h3_jy1IKaFYD2iwQ-y74sakFd7FBqCRRx2pF3rfphJwQlpS4da4j3v3TQJ2ebrX7chKE_sana-lcq6OYl5TDE3SxTq9vgRdMdYzh8G65TB8VFqlo-D5IPFx5DJsIWiCozGI2_ErepkDmQuIg0_YjIcdPRMQtF_KAQfL3lfutTsEW5Zr0TU6vmHq7hgj11MiGbpEXj8W2ticDQ_NK_GkEkyT-BpnVeVSVH0KXZ0TLVWEHACBeFdjGDPbLve1JviT7yVkw45OmeDGEOvop75f4rHjjinM8AoEoyLHeSm1COn_mo8pYV22ApTv3OcLfobB9-EFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: باید کشور را دریامحور کنیم
🔹
دستگاه‌های کشور باید با بهره‌گیری حداکثری از ظرفیت‌های مغفول‌مانده سواحل و دریاهای کشور در مسیر دریامحور کردن کشور حرکت کنند.
🔹
برای نوسازی ناوگان دریایی آسیب‌دیده در جریان جنگ، باید سازوکارهایی ایجاد شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/462288" target="_blank">📅 21:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57790afc1.mp4?token=X9OIE1EKd8z0gNomem231MZvYOAV1_mZVYjnF8q55kAKrnQV3VI2HoxHozyboB6vlxz-pL43LifTnY2U-VZCMQ2mosNLkQJrVLubl2yOL1fihlV6_MHLBGG09xm31gIw4AN-kxyRueXk9v-KhjicJ3izFZjZfL6HpwSkp_SIMUE33dyMD80gcn4DuWLcZ937x_OXH03KL_7SmY8Q7_mF6wNzlA8_YVXCcDCjV8EeKKZqV7Vlynp_UhEybNBliw7Na8hTkSpayn2ZlXMBGDz1YQyyUWDZMTO3qXtLSunYLJYQX18g67WdFD0neofKHf05dfQfK8iFuf7IfCXM4On62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57790afc1.mp4?token=X9OIE1EKd8z0gNomem231MZvYOAV1_mZVYjnF8q55kAKrnQV3VI2HoxHozyboB6vlxz-pL43LifTnY2U-VZCMQ2mosNLkQJrVLubl2yOL1fihlV6_MHLBGG09xm31gIw4AN-kxyRueXk9v-KhjicJ3izFZjZfL6HpwSkp_SIMUE33dyMD80gcn4DuWLcZ937x_OXH03KL_7SmY8Q7_mF6wNzlA8_YVXCcDCjV8EeKKZqV7Vlynp_UhEybNBliw7Na8hTkSpayn2ZlXMBGDz1YQyyUWDZMTO3qXtLSunYLJYQX18g67WdFD0neofKHf05dfQfK8iFuf7IfCXM4On62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پرونده‌سازی علیه ایران تا ممانعت از حضور رئیس سازمان انرژی اتمی ایران در آژانس
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/462287" target="_blank">📅 21:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5UvHlOFUf_CMLGA7cspsafUg19oJLJrHeq9KKSzuGHCiO6HXHNZcdhtNJViWi9tYHTGpdfh5JA-4TZu3PQaeAvdkHBhrwvPQ3rQe19GkpISmqE5iPtnzA3IBpUYF67LOYuEFnI_58UpM8WYJyuzV9Jlqsjg-nEi_fLaTq4tOxW4asZMiuB4dndXtlkhJKGFlWtj7nhOcvE26q9qUnzb0EghCnra992EE60o-aJCQ74boBdWp2szQUTcuhDAQRMjio-U-2RJgbwH1vhXL8brwxwx0Wj7tQbej3TMDl-z10wMlfUvSL081nxWeoZ4tbQql2CvEHikNIoDwHVLKMVxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از تلفات سعودی در حملۀ نیروهای مسلح یمن به تجهیزات و ماشین‌آلات نظامی مزدوران در استان الجوف  @Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/462286" target="_blank">📅 21:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462285">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d17b718c2.mp4?token=vzrY4GmJy5eLKaBIM2THCk1oztoymqK0n3lNNsyUGuE1WKamllvY4oA1ZZTNDxhCeGG5IfTdBR_wvs-vPw6SLIbo_X5eg2tFBNnHrFSg3ETejsF5ZZ8mUAl-Om1E20n8i_6tk25ZL5ZR_7byvVYtNZfSWZfwkqXXHX-zgt_opKx3MJbV61i4EUSV1T-ARpxKCmZvtwICUjhi7kT7MHH-ZjymBMAYuvJk7DQNzkSbXrIsbq4O-N0_xagbHxwuYIM4MxGtf7c8zllgSdrf6Gve6Q9kwl6XYzRwSigns63Eg2j393-kpz7d6xPCutOVkay2I_NqITWis5iMhyempSIWnYWOwXrRWOzFaiRYtE_dlU_ImwRbwefYrK-rG2T0_akm2rBzr4REZJtvrrzROwmd_n6BWtxxCwVAKGHkE2wPPBUijs86v-FUDVnELhG9-f3KHc-CNU0qt8njKqmMUFh0k2s2taoKPx9YZoD0c_FgHAtZ4pAqsUPTGWKrl6lYygD3Qc0ngf1rtsb0t1ZX939seHJ0Vhz8rL74E8IYGZc2p2QD20W33jyjP_50xSZI1OG4AnmhwqIgePBTh1hysTywGrTcv75Ta_hx5S5tybnoc3jvQ5cZUxh4pRVBEzQLFNFEigsEs9kqkAK0VYahFvpbu-DiomDhbGP_MlhONKk8jrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d17b718c2.mp4?token=vzrY4GmJy5eLKaBIM2THCk1oztoymqK0n3lNNsyUGuE1WKamllvY4oA1ZZTNDxhCeGG5IfTdBR_wvs-vPw6SLIbo_X5eg2tFBNnHrFSg3ETejsF5ZZ8mUAl-Om1E20n8i_6tk25ZL5ZR_7byvVYtNZfSWZfwkqXXHX-zgt_opKx3MJbV61i4EUSV1T-ARpxKCmZvtwICUjhi7kT7MHH-ZjymBMAYuvJk7DQNzkSbXrIsbq4O-N0_xagbHxwuYIM4MxGtf7c8zllgSdrf6Gve6Q9kwl6XYzRwSigns63Eg2j393-kpz7d6xPCutOVkay2I_NqITWis5iMhyempSIWnYWOwXrRWOzFaiRYtE_dlU_ImwRbwefYrK-rG2T0_akm2rBzr4REZJtvrrzROwmd_n6BWtxxCwVAKGHkE2wPPBUijs86v-FUDVnELhG9-f3KHc-CNU0qt8njKqmMUFh0k2s2taoKPx9YZoD0c_FgHAtZ4pAqsUPTGWKrl6lYygD3Qc0ngf1rtsb0t1ZX939seHJ0Vhz8rL74E8IYGZc2p2QD20W33jyjP_50xSZI1OG4AnmhwqIgePBTh1hysTywGrTcv75Ta_hx5S5tybnoc3jvQ5cZUxh4pRVBEzQLFNFEigsEs9kqkAK0VYahFvpbu-DiomDhbGP_MlhONKk8jrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین امید ترامپ برای ضربه‌زدن به ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/462285" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462284">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
حدود ۲۰۰ شب گذشت که مردم پای عهدشان ماندند
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/462284" target="_blank">📅 20:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3_TCj4gQTIUOJNWJrEwKHDCgKFDCb3xcw36xYnGskY5-4KLQWQMedk0cIdJsmi7lc1P3kOoxA9vXEmuvBdcAE8YQHoz6LEqxSLhat76iXR6nC0s7m_58zT0M0Pc0WjeqjlDQ3nvVXizWrRI_G__PSfMd4AgCvgYeSWxdYlJrQ5yvV9fyVEV6Wy1C5HuEDMw874OtKH0dqVWIGetvUJACTfGteRniB-o9pRE7ZHFnHvgscYow7y4OF8x4ZZoQlQCfXJAb06Y-1jwcb0nK75bycfUchGcTn_n39_g-BCYmJVl6sfOhOpeDSwZgWY-lkB9XoDbLc1zNCOiKqYS9ajXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظۀ ترور مولوی یوسف گرگیج در زاهدان  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/462283" target="_blank">📅 20:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmn9UidFXZTGHKgr2b94fFtvD4MQy-z2A0viTMQyfVpPhl8Am2B3uKndQxC6MoVGzHTXkaOP0u_4qVGdUASLLzWndWmYZAITmOQ2UZDe89PLMPmaZs8CxlnnzNSqZY2EXMWL4SnFx_PSVyzdk6nrAYSjmOArsxIoUA5Qq49aN7vEJM9--Nxn8skmAiGcflY6L1MawTTFW9Bq34GvyJOUjhr-BN5egPryzBlDPSix4LMzrk6loKZ64PqnO9oeUGdvfh3A4I8jiH1JeAZHSF20qvMLG6x6K52ISyKPwu1cRykZPpqWxew9-YK83uTMARw5em7KC_wluFf0kGeAh0ErxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری…</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/462282" target="_blank">📅 20:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6116abbafe.mp4?token=jPrH3JbcHpguLZFwuyaHvIiURnslz8zewwwjHEt0wxcpHHV6BcBvwNUsUHIWTHFv3GQa8pJVBp-zv4pbfwK3T11uzyikkrAPWaO2RZdcHWMPbKHjnDmUExzkqbSOSXihGb-ZMmVJQ0l-fk8c6gu27T5TL4OIQVWtc3nM7DEJomDrNKi_iwjf6rFO59YHODgyvNBi0eW4Xs0o0FjEvWgCBGzaoY4fXU_EidwfHBZyRmv4ou_Wcgm4KMslNzkLcxjOWKGEhzx5fHURy-KxAaRZt85RNVf4nd_HAeZuO-_boiA9AOEAOAyErR9KLhlqzjjfAHmwxJ4hWd3QIx3ENY_UPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6116abbafe.mp4?token=jPrH3JbcHpguLZFwuyaHvIiURnslz8zewwwjHEt0wxcpHHV6BcBvwNUsUHIWTHFv3GQa8pJVBp-zv4pbfwK3T11uzyikkrAPWaO2RZdcHWMPbKHjnDmUExzkqbSOSXihGb-ZMmVJQ0l-fk8c6gu27T5TL4OIQVWtc3nM7DEJomDrNKi_iwjf6rFO59YHODgyvNBi0eW4Xs0o0FjEvWgCBGzaoY4fXU_EidwfHBZyRmv4ou_Wcgm4KMslNzkLcxjOWKGEhzx5fHURy-KxAaRZt85RNVf4nd_HAeZuO-_boiA9AOEAOAyErR9KLhlqzjjfAHmwxJ4hWd3QIx3ENY_UPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شهید حسین مهدویان، خلبان جوان نیروی هوایی ارتش که در حملۀ دو هفته پیش ارتش تروریست آمریکا به جنوب کشور به شهادت رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/462281" target="_blank">📅 20:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avt_o2l7D_1hiBpis46O0nHHMKe9Ma1bxcGGgkMbKL57KpUsVRX6xaFANYv6SPuLyRZBYzavO1hdW14VeKmK9om1r1tNjOQmj6HCUt-mZwewCf9qs_kRyHmB0khL2NEoKZGfB2P7856I8gFDr4CFsy0y58RBPmypOCMV1I8AEi0J6hx4zxLMzgf1InrGWEtS3yFef7W7UovGqMwvW_7h60a3-rkHxzaOezp8MQ-AzNvAXT16Cu99UzkO5UuATBZjgfwHqk-cPgRQ3mV6oOfWLiGu9_qN81aEJDBMWG9udEPXQVzyTnEUO7et_PmRs-iJiGUCfWSV_rzty4XovQJJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نیروی هوایی ارتش: ۳ خلبان ایرانی عملیات العدید، اسیر هستند و قطر باید پاسخگو باشد
🔹
امیر جعفری: دولت قطر هنوز هیچ پاسخ روشنی نداده و ما تا مشخص‌شدن سرنوشت این عزیزان، آنها را زنده و اسیر می‌دانیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462280" target="_blank">📅 20:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzf4BW1pFhYpEt_P4eHvlFPjoDi2QwLZkI3NwB2SnCsle3WiIUqmk4zthu_852FVrdV5vuVsG-7m_k8lJODn4r06X4F57tj4PkMDXSG10O7IOr2l2xjQWTTMxxlWNBOUfb6_cXb8CkNJIssyLU6T9ZIqo5eJL8GDgfe5X1ezVn66_MCaY1VtEh0SaPRt_he8nvz_JOWdhqsx865D-LkoV5FXuYJM_NAHeWRMC91H1zsfLXbmOyfBvDT31ViJOSepFH15NyneVhylfKn6blHi8OgyIwEgXVErqnBzSc8N823C9b6DPuomKnIBaimYOprfxVe2eMU57Uv9VgCvtZgOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: ایران تسلیم نمی‌شود؛ برنامۀ هسته‌ای ما صلح‌آمیز است
🔹
کمالوندی در کنفرانس آژانس انرژی اتمی: ایران از نخستین اعضای معاهده NPT بوده و همواره به تعهدات خود پایبند مانده است.
🔹
آیا بازرسان آژانس در بازرسی‌های مکرر و مستمری که از تأسیسات…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462279" target="_blank">📅 20:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqMezP_272NuLl8ABf3iZJiyujXlNXuu_vcRq76UAfz61-bSrJHHenWURD0ddsrSnDO7X6lv8a-6h9gSg8KxajOIf_byWpDwgz8CRyuqgnGnKQC8ugDHuP6PYJTisfobF-jxcODMHo8Xp2m8Brm4fQQeTjJs6S0KSGYYBY23TSeOsd0ojz02IY0r1MPXHxynqXpy0r3GB4uuiwCYm-4XdIvWWG3Yxo5sVsAfj0FVa3rmvtSVRWluOfMzsrVDit0NCuBYpIqcxWGGl_fvAAjQ7IqJ3ODW6tJBioEkZU84fxh5LPg5-SOBZ9tfNCtEk7Nz0jAz46s-GA5jLDBRsMjEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: ایران تسلیم نمی‌شود؛ برنامۀ هسته‌ای ما صلح‌آمیز است
🔹
کمالوندی در کنفرانس آژانس انرژی اتمی: ایران از نخستین اعضای معاهده NPT بوده و همواره به تعهدات خود پایبند مانده است.
🔹
آیا بازرسان آژانس در بازرسی‌های مکرر و مستمری که از تأسیسات هسته‌ای ایران انجام داده‌اند، تاکنون گزارشی مبنی بر انحراف ارائه نموده‌اند؟
🔹
مگر مدیر آژانس و شورای حکام حملۀ نظامی به تأسیسات هسته‌ای عراق در سال ۱۹۸۱ را محکوم نکردند؟ پس چرا حمله نظامی بسیار گسترده‌تر به تأسیسات هسته‌ای ایران محکوم نمی‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/462278" target="_blank">📅 20:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTKqAya-pfYqJ_kGqD24SEgejxW24phpKaUOv2sgPpdCN9HenIBKVqO6lp7gX4efAfn3cK9Gb4lTe02rY7DoIAIQP155GQ1vvMsz0lAfCFVvHPHhHFk_aVDVF5lboS4Lb_7MmeeRk9DTG6PB9pHjp2oRTsvLst9WryN3uxDvZ2Do10xuo1BH-yOQPhRTzeiJuk0IN56BfOIENoC3pXbUwFjh9i90Qw-qPTjEqPL6bu_Jx0euIsqh2HfELIPrFPjXuIQTos64StENHvQ4BIw6GzA9-fRy3qtrDRsCzw4GroiZeSvpI8TA-GR955wfv2NX6JtEikCzxkhSKpTAykxEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالزی سه محموله با مقصد اراضی اشغالی را توقیف کرد
🔹
بلومبرگ: مالزی چندین محموله به مقصد اراضی اشغالی را در بندر تانجونگ پلیپاس این کشور توقیف کرده‌است.
🔹
محتویات این محموله‌ها پس از توقیف یک محموله‌ پیشین که احتمال حمل سلاح در آن می‌رفت، تحت بررسی قرار دارد.…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/462277" target="_blank">📅 20:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17962f4555.mp4?token=KWRg91ThyHzjvLXgxiBZCjBZ-pNUrmZgUDBravIaCXFMccnfpgc6OH5Ja3ybzt4cGdtHKGs_nVJdNdou4E4s1idcbE0Atu81dV9TyWBT0IguokwoAXd5H9LLYArNlA1jUhBQtb5OsZH7kSUsTPhR8uc_UUSCZSpPcUtKrBegPWotLv56IDcZlRfN-sQa0ZTSrWc1rQ0dpjEuUAC0dHd574KwXO68RHgZnAkgHCWVoexUlkuizDCsaaJyl-jwGd1kmmFF7DIsQgerv53vNjsRi-I-s27IU1fgfEMJ-pJLtjb6y50n7i6u5A_giOkVjAoSZCl_HuzYCB0hfOfe0Jpq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17962f4555.mp4?token=KWRg91ThyHzjvLXgxiBZCjBZ-pNUrmZgUDBravIaCXFMccnfpgc6OH5Ja3ybzt4cGdtHKGs_nVJdNdou4E4s1idcbE0Atu81dV9TyWBT0IguokwoAXd5H9LLYArNlA1jUhBQtb5OsZH7kSUsTPhR8uc_UUSCZSpPcUtKrBegPWotLv56IDcZlRfN-sQa0ZTSrWc1rQ0dpjEuUAC0dHd574KwXO68RHgZnAkgHCWVoexUlkuizDCsaaJyl-jwGd1kmmFF7DIsQgerv53vNjsRi-I-s27IU1fgfEMJ-pJLtjb6y50n7i6u5A_giOkVjAoSZCl_HuzYCB0hfOfe0Jpq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: بیش از ۵۰۰ سایت ارتباطی در جنگ رمضان آسیب دید اما ارتباطات مردم حفظ شد  @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/462276" target="_blank">📅 20:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6EnD5gExhfhZeqcnRpqIlHTbFYEsr-vmq5utJhGBtqWf4kHmVwC6R07KTl0ugaOElUv2SqrJdawMdZ8OMtqr9FdMf1grGf25sbT2CXCT3yjTpEFZaWgCGUaqgPWChnueMZEf2P1T_E30jDfmuasPtYr6oYf943f2oNSZfVXLeAFgC6qeuNd-zmzH20P8rlSJSw22QU9MDj_GsYNdWhx8Xnx9W8VCeQ3fCHPqnyo-crCBA-SKhs_ddaO6UmoGvCjbot6nlgm-TrJyNes_CihZnXQNbpC1bcnaP7DnxSErQWNoXEpIKt-JJP1oITks-P3-aBzXccdObYQZ23BKyjtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برنامۀ رقابت‌های فردای نمایندگان ایران در مسابقات آسیایی
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/462275" target="_blank">📅 20:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVfDi4CHv4E6s1k0Xa7Ox1czFLxL6QSgEdGcMDVig1sc4M7Qg7HTEa-AN8pLQpESSTnIXzDxE8yhOS6Vz42ZxoxvIr-J2p8equshxM4xNwtGQezw9MVU3avWbE8w9JoMOHA0-VewGoGE9v5Fqck-PymDoraRpvBsbTkZLK9pcvdxNdiwTQCGdcFrwNgb2kpEZM4Jenw8DLA_UjovjWVUdq65ySlbssZQ3xTU2bOIFYTEqJvIxdq8iOicIHIjURY3uBLvqcT2PsxS8tagIoHtrswGG1sTaBiebfbAoSU52ig-jkpof0edYxsvGKAfXuYkAhWUjZatR-pceOjwNqHP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: روزهای تلخی در انتظار کسانی است که درباره ایران دروغ تحویل مردم داده‌اند
🔹
شایعه: ایران بی‌دفاع است.
🔸
واقعیت: صدها پایگاه نظامی آمریکا نابود شده و ده‌ها فروند هواپیما در آتش سوخته‌اند و این تازه گوشه‌ای از حقیقت است. به وقتش همه‌چیز را برملا خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/462272" target="_blank">📅 20:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌ عربستان برخی محموله‌های نفتی را لغو کرد
🔹
عربستان به برخی مشتریان اروپایی اعلام کرده تعدادی از محموله‌های نفت خام اواخر سپتامبر لغو می‌شود.
🔹
رویترز علت این تصمیم را بسته‌شدن خط لوله شرق به غرب عربستان و اختلالات کشتیرانی در دریای سرخ و تنگه هرمز عنوان کرده…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/462271" target="_blank">📅 20:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462270">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b9728ece.mp4?token=kfH1gYDkOHhibrZV-5f6OJbWIGlt9NzeIHjMI8GzKRFukM32Zt8sHmtzQsW-K1KWaL_rW6mK4w3ShSrqZ-ENoPbrDzcrQ5Grm8FxuaUoIsc85FtBfykwIHbK2xjH4QqoUzDBp_OpRamFM-RLfJDJJjer04JpukmUkgw4Qz_AjTKZsXQ35Pe2rcWWNuVNRscjUUw2onB6wt19Ppd7A2Mb44Ffx6t1oQ8KrbnVMwC7JThZ9tTpqOthuYhIInill-LgkOGHyjBAck_lQua1_aSKRVwKvMoGDys71kCQweELechod2N7TuyGMRpdtHzmNkwyA4dupRtK1kZ4Gm49uHp6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b9728ece.mp4?token=kfH1gYDkOHhibrZV-5f6OJbWIGlt9NzeIHjMI8GzKRFukM32Zt8sHmtzQsW-K1KWaL_rW6mK4w3ShSrqZ-ENoPbrDzcrQ5Grm8FxuaUoIsc85FtBfykwIHbK2xjH4QqoUzDBp_OpRamFM-RLfJDJJjer04JpukmUkgw4Qz_AjTKZsXQ35Pe2rcWWNuVNRscjUUw2onB6wt19Ppd7A2Mb44Ffx6t1oQ8KrbnVMwC7JThZ9tTpqOthuYhIInill-LgkOGHyjBAck_lQua1_aSKRVwKvMoGDys71kCQweELechod2N7TuyGMRpdtHzmNkwyA4dupRtK1kZ4Gm49uHp6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک عملیات تهاجمی که صفر تا صدش به نام محسن رضایی است
🔹
در تمام اسناد و جلسات، همه مخالف عملیات فاو بودند؛ او با تلاش بسیار بقیه را اقناع کرد که در فاو عملیات آبی-خاکی کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/462270" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462269">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb34c5af3.mp4?token=IrX08xM-PwxUfrsy_c3UQgCX3JCfANA7c3rOEVkq7hwOUgLRKw6uJwV0zcsFQBXJIJ1OHfRhzVQqFbw6qcPdIUY0MZVnTFmh4TALxCMGJC609qjw51xaebwn9B0U6ceMmMwDigO2MTttIvWbni2WBSVFAReM2w-uKTTiM2yjzW8tjw3BZCBmXm3StoIMPYPTqBd5mNQHfqLrVqKZ3iy7JA-FxdfVu0hnR29EuHOUE6i86r_w3OOaF0htIZH5loj5_7Hl5cfSqtp6KcVK2hbJa5wpj-0NlQ5cv8OzbAA0ZXHSu1V2RWQxbuszkWvzvmWG8M856PvxxXHhFz5BQuj1z4DSAuPbBfP7uuFdpnDcVgQfMdcB9w8T6Wkhe5mK9FtUuxkkF9O9iQFK_jU6jOWJW3Ae5g0DJ5k2Cj9OEDhxwjOKGxd6-8RlpyCXr2DL0wAHwxgHxBQiBpZc2fYzDGjFkpwB_8GHxuE4OjJ9EiosyOHnid_CVyUFBHvQunyDug8faP5jZOIOGTil5Jw7-w1cNXQte1Jm_-Pi7d_nS9APpBU0_HSQbFIxexj8oG1UglQ2mAWoXqGEcq_ugjlTpvnoI9F2qNoMwS4SrN0SFLhYPrsmwbCiBjXS0R03jmUUFZTRHN4hWe0B6QxIwAe12ChNePrTmEIqWj2kMDfm3mTg-i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb34c5af3.mp4?token=IrX08xM-PwxUfrsy_c3UQgCX3JCfANA7c3rOEVkq7hwOUgLRKw6uJwV0zcsFQBXJIJ1OHfRhzVQqFbw6qcPdIUY0MZVnTFmh4TALxCMGJC609qjw51xaebwn9B0U6ceMmMwDigO2MTttIvWbni2WBSVFAReM2w-uKTTiM2yjzW8tjw3BZCBmXm3StoIMPYPTqBd5mNQHfqLrVqKZ3iy7JA-FxdfVu0hnR29EuHOUE6i86r_w3OOaF0htIZH5loj5_7Hl5cfSqtp6KcVK2hbJa5wpj-0NlQ5cv8OzbAA0ZXHSu1V2RWQxbuszkWvzvmWG8M856PvxxXHhFz5BQuj1z4DSAuPbBfP7uuFdpnDcVgQfMdcB9w8T6Wkhe5mK9FtUuxkkF9O9iQFK_jU6jOWJW3Ae5g0DJ5k2Cj9OEDhxwjOKGxd6-8RlpyCXr2DL0wAHwxgHxBQiBpZc2fYzDGjFkpwB_8GHxuE4OjJ9EiosyOHnid_CVyUFBHvQunyDug8faP5jZOIOGTil5Jw7-w1cNXQte1Jm_-Pi7d_nS9APpBU0_HSQbFIxexj8oG1UglQ2mAWoXqGEcq_ugjlTpvnoI9F2qNoMwS4SrN0SFLhYPrsmwbCiBjXS0R03jmUUFZTRHN4hWe0B6QxIwAe12ChNePrTmEIqWj2kMDfm3mTg-i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی: رکن اصلی پیروزی، حضور ملت ایران بود؛ دشمن تصور می‌کرد «سه‌روزه همه‌چیز تمام می‌شود» اما همین حضور کمردشمن را شکست.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462269" target="_blank">📅 19:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBzErnK4HNmdmXGeaIvyulUseQGALCurOAK11nkSSkLMBD17WRLsAkRx6-uH6TvZOa6D99vhBXgSTqQ6rVuje9bOKqBl8KKw15_OColhWDpXikZ8K2kOP_ZePRC9Cs6eEOaLJDp3pQj36Nyv63oDS1QXsht4wKGF4Bfbk3raF1JEBFpT7ZX6f4xW76_VPYbRQ7VTYcM7oN7SV65hsfgv6BXPvIc2YXk0vKIFh8cL63ZDAVJcYwzELQIauIDis1llhttUuaIQ8PMmmlRC3f-OdvImVikqjsb7URZrrQXZ_wS8YNlleohZkYxFH_ADhKyYHKZAfXyLGMP4tDWPhgGcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالزی سه محموله با مقصد اراضی اشغالی را توقیف کرد
🔹
بلومبرگ: مالزی چندین محموله به مقصد اراضی اشغالی را در بندر تانجونگ پلیپاس این کشور توقیف کرده‌است.
🔹
محتویات این محموله‌ها پس از توقیف یک محموله‌ پیشین که احتمال حمل سلاح در آن می‌رفت، تحت بررسی قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/462268" target="_blank">📅 19:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdcf80027.mp4?token=gCRQh5zEq8bKAkbYhIN7_O_n1i0Nu_iAeAdPbQ0kKgEOdjVgZzNHrMoNFMoAcv3bwPFmL9EjP2ubPIZdDAvsvPCanWcM0pg6TLKXyA9UCzAhwuVTKqeBhRYoB1W04xRXBxNYeu0RTMdAugHi2g5W93FhKwbuDqEO5gMBCNqiBWwWlVyIGHtMC83rbUkMjMZ0cFi90crBqETYm-jiFqPifOjhjzLCSIDX3BdEn8DH7qWxxBsS8qY1zXRkP7iRBenB0aAnX9BOr6DAFjFCrbnnwaX3NMHI79sX6o53_3m855RwAPQmGTGB06AgNaFgB2jkenx-hrRJGy7YLR3my2Z_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdcf80027.mp4?token=gCRQh5zEq8bKAkbYhIN7_O_n1i0Nu_iAeAdPbQ0kKgEOdjVgZzNHrMoNFMoAcv3bwPFmL9EjP2ubPIZdDAvsvPCanWcM0pg6TLKXyA9UCzAhwuVTKqeBhRYoB1W04xRXBxNYeu0RTMdAugHi2g5W93FhKwbuDqEO5gMBCNqiBWwWlVyIGHtMC83rbUkMjMZ0cFi90crBqETYm-jiFqPifOjhjzLCSIDX3BdEn8DH7qWxxBsS8qY1zXRkP7iRBenB0aAnX9BOr6DAFjFCrbnnwaX3NMHI79sX6o53_3m855RwAPQmGTGB06AgNaFgB2jkenx-hrRJGy7YLR3my2Z_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیرزن هرمزگانی به رسانهٔ خارجی: با حضور بچه‌های سپاه ترسی نداریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/462267" target="_blank">📅 19:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89efe83b5.mp4?token=k66PJk7QnzGYdC8fTqvPcD8M3el3PK2fpUUvGIhAfPbCQxNg_Wcy4TFAbsEXquJC2QZAT7QsSV8gE8NYJQBXDvKfkR8KKfUjXjQSGPhV6g-tnonNB-4QH5XYROwMy1Y74OZbT8L8Lcu0A7i9vJYV15WOGm_QV4NxSu4F1CKmqeFFo8_YXYtHtqbt5c_TOyq9DXBGxXXxu0FlPSUJUuFPXXvSPSn8hFiMkZmcwP4r13CiUgCmtd41qy2JBlkkV79M48igLep7kUjbz9K7ffPjJAOjB36nmEP2qOxmUqByiOQZYNwGoRAMj_xQ2v92s3GRoPUL7nfjZzymwN-nMbocWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89efe83b5.mp4?token=k66PJk7QnzGYdC8fTqvPcD8M3el3PK2fpUUvGIhAfPbCQxNg_Wcy4TFAbsEXquJC2QZAT7QsSV8gE8NYJQBXDvKfkR8KKfUjXjQSGPhV6g-tnonNB-4QH5XYROwMy1Y74OZbT8L8Lcu0A7i9vJYV15WOGm_QV4NxSu4F1CKmqeFFo8_YXYtHtqbt5c_TOyq9DXBGxXXxu0FlPSUJUuFPXXvSPSn8hFiMkZmcwP4r13CiUgCmtd41qy2JBlkkV79M48igLep7kUjbz9K7ffPjJAOjB36nmEP2qOxmUqByiOQZYNwGoRAMj_xQ2v92s3GRoPUL7nfjZzymwN-nMbocWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات
:
بیش از ۵۰۰ سایت ارتباطی در جنگ رمضان آسیب دید اما ارتباطات مردم حفظ شد
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/462266" target="_blank">📅 19:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFC21iUVdkEthGkWjKfu3kkaheGlSPB2PF-LGlHpr5fAbBOLi3bDXVBfChCeRNgS89ZF3Huz1By3YQrds6ti7DpXhCamrdn7iUgwRgkIaDk2RWZc4g_W2p53lUxNcoV17u0wdI8msnGrS43_GlVdh1yIwlix4-8IDDc3wnvNalidqqqlzazL5Me8R8EzHiNlFw8gpZIRj5Q82uByysPHE17giaFrzanO0TdkWlatPgFB1fUCB5TprCU16Z9UL_EfoozZmkAo74d0nSWyd7iar0T4YSJZjxiP2lO7RdAM5Mw5zlkpRe5-YFdzFcjRe1XqcwNUMGcrrQ6-3CliIRmtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار عظمایی: گلوی جهان‌خواران را رها نمی‌کنیم
فرماندۀ نیروی دریایی سپاه در پیامی نوشت:
بسم الله الرحمن الرحیم
﴿وَنُرِیدُ أَن نَّمُنَّ عَلَى الَّذِینَ اسْتُضْعِفُوا فِی الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارِثِینَ﴾ (قصص، ۵)
🔹
ای ملت شجاع و تاریخ‌ساز ایران عزیز؛ سلام و صلوات و رحمت الهی بر شما بندگان برگزیده‌ی خداوند، که در این برهه‌ی تاریخی، چون موج‌های خروشان، با حضوری حماسی و حیرت‌انگیز، برای دویستمین شب پی‌درپی، در خون‌خواهیِ رهبر شهید امت اسلام و در حمایت از مظلومیت مردم ستم‌دیده، قیام کرده‌اید.
🔹
ای مردم نصرت‌یافته‌ی خدا، اقامه‌ی خون‌خواهیِ شبانه‌ی شما که برگرفته از مکتب عاشوراست، اوج حقیقت را بر پرده‌ی سیاه ظلم در این عالم به نمایش گذاشته و چون توفانی، کاخ ظالمان را در هم شکسته و جهانیان را متحیر ساخته است.
🔹
امروز دویست روز است که در کنار قیام شما، خلیج فارس و تنگه‌ی هرمز از حضور پلید ارتش تروریستی آمریکا و دشمنان اسلام پاک شده و تنگه‌ی هرمز در مشت‌های پولادین رزمندگان اسلام است. به اذن‌الله، گلوی جهان‌خواران را رها نکرده و اجازه‌ی تکرار و حضور مجدد و ظالمانه‌ی آنان را نخواهیم داد.
🔹
دلاورمردی رزمندگان اسلام در جبهه‌ی جنوب و در دریاها، وامدار استقامت و حضور باصلابت شماست؛ شما که تمام رنج‌ها را بر خود خریدید و در برابر همه‌ی حوادث، بصیر و آگاه بوده‌اید.
🔹
بنده سلام همه‌ی رزمندگان در جبهه‌ی جنوب و در سنگرها و خط مقدم را به شما می‌رسانم و ضمن طلب دعا برای نصرت و پیروزی رزمندگان اسلام، خاضعانه توصیه می‌کنم «این حضور مقدس را با اتحاد مقدس گره بزنید» تا ان‌شاءالله، با هوشیاری و حمایت از رزمندگان، دولتمردان و فعالان جبهه و جهاد، از این گردنه نیز با به‌کار بستن رهنمودهای حکیمانه‌ی مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای عزیز، عبور کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/462265" target="_blank">📅 19:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6gqgy6VtyBhJUVNEgKq1Y7pfxw80duUwJXjxxXsbOix8mYmn58rix5erSoEyeTtOpQbs8xCMBG2eqxPGIqj3K8LE68PLxdSj9qlKiXazMMkC5nTw2AXqxVBnUPdJsjEkofEBhq1DTUIdFHrvnK-uopdx29gSbbhrGdkpsbSBU9HsBUlOAXOSWQYMb8KqTQA9JGo-Ps47BzDRWeMbNQ4f4I4Dl0L1a7kGZJFNu2AvvuWGQQjr-mUJDpuMd0Ez8jse2y6y3BFxs4euS_RfzWyHQVL-_zOZKH7C362Do2E51tHo2_uTX0BCXboE3TnOTarbUn0qDUhYJtFxaZ_IDWHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی خبرنگار پرس ‌تی‎وی را ربود
🔹
پرس ‌تی‌وی: نیروهای نظامی رژیم صهیونیستی خبرنگار نقا حامد را در یک ایست بازرسی نزدیک به بیت‌لحم در قدس اشغالی ربودند.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/462264" target="_blank">📅 19:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCpdLM0KmEi8MXwAhYwCyuof5jLSaayikMxGvroqx4y78v0QiFQw-8w3vBUzMeD0xSNPBKO7bdog3P5TGUrtmOKz2MeTyUypvxHcoJ0olr9tOhfaacoD2L2Yh2Lex87RleTbjBBo9sGcNEGeLxrNMzKTykYyYaPkXrh5nMld_6md1ihC_STgjZkV5XlBjB-ceKthbaCapM1R7vd9IKMsbC5asMpQovVuoEuToYSO2xXEWFhedLU4k_QGzH8cas80NYiKwNtpf_igCx9aJD91uhsNFmCrB4VlnptOAlAJQtzZXuhA8xfONd8Su9NXL3St33SKC3HvGOTYavDP6kosSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: جوان با اراده ایرانی می‌تواند موضوع بهینه‌سازی انرژی را نیز حل کند
🔹
سردار ابن‌الرضا: همان‌گونه که جوانان ما در وزارت دفاع و نیروهای مسلح در برابر هجمه بالاترین سطح فناوری دنیا ایستادگی کردند، برای مقابله با آن راهکار پیدا کردند، و موفق شدند و همان جوان ایرانی و همان اراده می‌تواند موضوع بهره‌وری و بهینه‌سازی انرژی را نیز به بهترین شکل حل کند.
🔹
در کنار اقدامات فناورانه، باید به موضوعات فرهنگی و رفتاری نیز توجه کرد و این اقدام را به یک نهضت برای بهبود بهره‌وری و یک مطالبه بسیار پراهمیت تبدیل کرد.
🔹
در جنگ ترکیبی، یکی از شقوق این جنگ، تحریم‌ها به‌ویژه در حوزه انرژی است و اقدام در این زمینه را بخشی از جنگ و دفاع از کشور می‌دانیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/462261" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af96054db5.mp4?token=B8fwYX9J1-3kaDCeJaHi78-_JGyIunx36sdf2AjuSVZV4oqhzaxadDNtt75H1j7kqbkUEwo7Xf2-NheJjMU8HKr9L_eDwbowJ4pqn6OkmH8fqXWFh8vZIaPyITM9UHj3D4jviBsmfxfQqylv_bzsXIU_KOOhZBYw__5SFCfpl4DAjXwL2hngF5GMc3r-E8fQwXHuwv0dCoeWp6v8nejmAlsxKTN2PQMqOIPBJ7RuDl10nYHLWuN8jqzI5csLS1vG6zXSBW4-Ng_mVBXZfM2QzWxFI1gbfM6LRMv9XECkQR4R7RQgY_Ko5uYLhkhpaLPcSg4V9DMfGm8CzinLuqi3VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af96054db5.mp4?token=B8fwYX9J1-3kaDCeJaHi78-_JGyIunx36sdf2AjuSVZV4oqhzaxadDNtt75H1j7kqbkUEwo7Xf2-NheJjMU8HKr9L_eDwbowJ4pqn6OkmH8fqXWFh8vZIaPyITM9UHj3D4jviBsmfxfQqylv_bzsXIU_KOOhZBYw__5SFCfpl4DAjXwL2hngF5GMc3r-E8fQwXHuwv0dCoeWp6v8nejmAlsxKTN2PQMqOIPBJ7RuDl10nYHLWuN8jqzI5csLS1vG6zXSBW4-Ng_mVBXZfM2QzWxFI1gbfM6LRMv9XECkQR4R7RQgY_Ko5uYLhkhpaLPcSg4V9DMfGm8CzinLuqi3VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون برق و انرژی وزیر نیرو: با کاهش ۳ درصدی مصرف برق، حدود ۶ میلیارد یورو صرفه‌جویی شد
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/462260" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8aa349978.mp4?token=SPMIF8zkzbBAfSzlyhDXpFmi18kibH0WXHMkotDgjGzBUiXKhxTq9iz1DcHUHVeqRA8KpgG_0zt1fqkp9UqJAPi5UQSFzPmO0Nfa37resxOFGx4_JjiXLSXRIJcmmOCtsV319XUkYoH3thtUbl5kO51nNbARSU-hvVlQUfxfqehMrMoNDbJlSH4nDjBfbb8giigsIqAlFvX6u1e2buHyIHGr2TSaZFp5AWd--GoDE88c7lk7uVepwj9_-qSyrkhrGnzlVcqP5tU7ArnstIbTPxZ1iToYu_LJCGewXe-CztHsxhOfeI-ppE13QbCHSd6uIbOXrw4tprJ22HomgJUvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8aa349978.mp4?token=SPMIF8zkzbBAfSzlyhDXpFmi18kibH0WXHMkotDgjGzBUiXKhxTq9iz1DcHUHVeqRA8KpgG_0zt1fqkp9UqJAPi5UQSFzPmO0Nfa37resxOFGx4_JjiXLSXRIJcmmOCtsV319XUkYoH3thtUbl5kO51nNbARSU-hvVlQUfxfqehMrMoNDbJlSH4nDjBfbb8giigsIqAlFvX6u1e2buHyIHGr2TSaZFp5AWd--GoDE88c7lk7uVepwj9_-qSyrkhrGnzlVcqP5tU7ArnstIbTPxZ1iToYu_LJCGewXe-CztHsxhOfeI-ppE13QbCHSd6uIbOXrw4tprJ22HomgJUvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بحران مسکن زیر سایهٔ خانه‌های خالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/462259" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=UgsR3JcW_ncpEke1OFao9uR7-wJLJQ2oeyFLC-2TBq6BlsKkyuUP8x1-EmjlXgLjjR5ByJad59BzL3LTebyAHaVUlNyyVHDUzT1LlcUEEVU_CGnEfM8J70iIIFcQmSMiyRHKxVcCL7n_zl1sgwWGhwcimpt1YipKOCgCdo0CnLOeXo5sAAmscozI_9LECk8_umUtgjdyQMj0nNmR3vsaZguNxwyk7IW2fr-KBcCXZQ1bRuanEUlt60VWkYAqet_nrJXWghWEbISA7zy317cd4ucj8o_bd-aQYQ3gRqI0yE_AxUhfL4UZVz8NYf4tqYWu1Uz5wm600K_09K0a9mnOK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=UgsR3JcW_ncpEke1OFao9uR7-wJLJQ2oeyFLC-2TBq6BlsKkyuUP8x1-EmjlXgLjjR5ByJad59BzL3LTebyAHaVUlNyyVHDUzT1LlcUEEVU_CGnEfM8J70iIIFcQmSMiyRHKxVcCL7n_zl1sgwWGhwcimpt1YipKOCgCdo0CnLOeXo5sAAmscozI_9LECk8_umUtgjdyQMj0nNmR3vsaZguNxwyk7IW2fr-KBcCXZQ1bRuanEUlt60VWkYAqet_nrJXWghWEbISA7zy317cd4ucj8o_bd-aQYQ3gRqI0yE_AxUhfL4UZVz8NYf4tqYWu1Uz5wm600K_09K0a9mnOK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
برخورد یک سوپرنفتکش متخلف به مین‌های ایرانی تنگۀ هرمز
🔹
نیروی دریایی سپاه: سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقۀ ممنوعه در جنوب تنگه هرمز را داشت، بر اثر برخورد با مین‌های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/462257" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-8Ckya-KurFl6J4wyBmiHmTUW783LCB7xCDg4B-mjc17iUXYkvRUfK5TWGH1d-JGyLXogh9-l75BcEoGvQpm1ZnSZO2sRMkPV3hVnufAdntGOqMHiNGUlTja5kppiONbtlqnlLtzTQamuO9r4a_XIQsPuAmjFFJm3FrjbGud2GO268Dx8ofVG8S37QNaM2sHy06-f3XIAlHXzg9XlSWEMT7PlMkQceUYte07vZctV-MbkHBbdnyUpBA5uqvw0IS-cfiiVFf_euaNC2TkYf-V75g6vegbXRDNXE4rTY0SZPXPlfIU8XA5kPjsBkX3lJF2qNlKxGeEPKLPp_KJ5H_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: توطئهٔ‌ آمریکا در مرزهای غربی ایران شکست خورد
🔹
رئیس مجلس در دیدار رئیس اتحادیه میهنی کردستان عراق: در جنگ ۴۰ روزه آمریکایی‌ها طمع داشتند که از سمت اقلیم کردستان عراق اقدام امنیتی و نظامی علیه ایران انجام دهند.
🔹
اما با کمک دوستان شما در اقلیم و عکس‌العمل به موقع نیروهای مسلح ایران این توطئه دشمن شکست خورد.
🔹
آمریکایی‌ها و رژیم صهیونیستی همیشه به دنبال این هستند بین همسایگان مخصوصاً بین ایران و عراق اختلاف ایجاد کنند؛ به‌ویژه در شرایط حاضر که مجبور شدند هم سرزمین و هم آسمان عراق را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/462256" target="_blank">📅 18:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVer5aNuq0Mu__CrsdjEtOj3MmU2-a35MOtT8iS4lR_EePMimc3mZHKKG0yp5kTFlXFirlY-e-VvkdH-rGNAcuEFnsS26ksRCTqUQZDVRl90svoH9upoioT4D9-mjerOmaiLecdhXGRkta7vMp32yfOD-YXVElhc8wKENMS6qF3dNvXTQ0Fhr2LdliG9wDp0pscoYDJ9-qlmq8qgVNXU0TtBp0IGxQ1q7VBw7J-VneeQHhm6ug7zbJaXilBUyccNOtAE9K9LLTLl1mrYii0gfsLmn65dd8Tjz9igKciu4RZBxYjCPSrzVfXCTtX_NfJ5f6gWtQ9i7aB2CaWGddsK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: ۲۰۰ شب است که پاسداران کیان ایران‌مان، زیر باران بمب و گلوله و در میانه‌ جنگی تمام‌عیار، استوار ایستاده‌اند. آنان که دیروز همراه نبودند، امروز با آغوشی گشوده به صف ملت پیوسته‌اند.
🔹
پرچم عزت و فتح برافراشته است و امیدهمچنان درجان این مردم زنده. ملت مبعوث عزیزند و عزیز خواهند ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/462255" target="_blank">📅 18:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
ابرپروژهٔ عربستان تکه‌تکه شد
🔹
تصاویر ماهواره‌ای جدید نشان می‌دهد حملات اخیر یمن به زیرساخت نفتی عربستان به چند نقطه از خط لولهٔ شرق–غرب سرایت کرده و ایستگاه‌های پمپاژ این شریان ۷ میلیون بشکه‌ای را از مدار خارج کرده است.
🔹
در تصاویر آثار سوختگی در حوالی…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/462254" target="_blank">📅 18:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qFRbIv2CEWwuYxC1u48QyytchytPK2WIVnwJUFY1QT3jYsFR5JsaqsSMfvIaWjijyShqfaHyII7fImcIdf4lyArLn8kghxSU3rJLPKvvLmxSGhi-CLFiFzCk8WWXjPgUF5SB0l4uty1oaJnxKzMj5IonSoR7NevdJcFYdZB64o9YznAk99p6mktpM7CZxeLed0i0WwW-sjJwB43bYzpFhNri_TyoZVo0jMEC7qYOriASA-MUcFZmSNorFAVedVhLn07DGB1SxlTczAUgOM5B7BWvIBd-gBTBo8AViHd_4aUHdtOZ2lgcwJAxvybhzVR4jvqAwlerhyzQGiua_DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اف‌بی‌آی دربارهٔ خنثی‌سازی حمله عضو داعش در آمریکا
🔹
اف‌بی‌آی اعلام کرد که یک مرد ۲۱ سالهٔ اهل پنسیلوانیا که در حال طراحی «یک حملهٔ خشونت‌آمیز» در آمریکا بود را بازداشت کرده است.
🔹
جاناتان هانتر کرِیمر، ۲۱ ساله، اهل والنسیا در ایالت پنسیلوانیا، با نام «حمزه الرشید» شناخته می‌شد و براساس شکایت کیفری فدرال وزارت دادگستری، وابستگی خود به داعش را اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/462253" target="_blank">📅 18:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11785309b0.mp4?token=Frk9EGYrrx0D6hivkmP2O3bTCCWEqGZmQUneUhFZM5scu7eRn2fqxWqjarDA_GJ8qMSKU05aeg53wgfsj0Z3ja7XLsEmX4osco5DzPPMGcZRgJ_IApM6R_CXeG-ZmGh8Kxpapfpr2RjvVmICauS4vBqpW1CS06vutQQNq0FiLI4QJkdD0wzMiFzL8p1um02fII6LYgDip8rAPbmmeQnc02CO_hlEBmHIcD54qGV87wPBh9jBJF1NMRlXp3jz3AjW_uBnrdYZ001gKV5NB4gKkYYu2lbhB0YoY59tl5NEd3AzquFphsUd2bXwn3IsQqkUJvbxC302s9YjoRRbjiOn6Lg13HloFiYKu0P-p0Z0eteH47xpexSfZmiUXQNv8VA9xPc9fYls8kGvzS613_xrWgAgbvTzSUr3uk7boHmXl-38V3Wwg2e2aPe3aVwFqdMhBLdbioqP0clw4M1KlRMvLNvSLzOzLHlhGI4Z_wZFGEO71coicqxiMHVcuZLvo7N2Jpks1FYXOlw1l9zlG3wlgsoAV8uIT8zYehQ7YsqV7cGXURuul7shnNxgVr_EqEGB1c85DqSt-8mDuWqEic08mLF6d2k5Su2eycm3KYFNBSbXGc6Oj3TBkRv1H4zGWNOp-MCRnDnrs1T6juNr-prSkoxwbmncI5Nb129Qw928WiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11785309b0.mp4?token=Frk9EGYrrx0D6hivkmP2O3bTCCWEqGZmQUneUhFZM5scu7eRn2fqxWqjarDA_GJ8qMSKU05aeg53wgfsj0Z3ja7XLsEmX4osco5DzPPMGcZRgJ_IApM6R_CXeG-ZmGh8Kxpapfpr2RjvVmICauS4vBqpW1CS06vutQQNq0FiLI4QJkdD0wzMiFzL8p1um02fII6LYgDip8rAPbmmeQnc02CO_hlEBmHIcD54qGV87wPBh9jBJF1NMRlXp3jz3AjW_uBnrdYZ001gKV5NB4gKkYYu2lbhB0YoY59tl5NEd3AzquFphsUd2bXwn3IsQqkUJvbxC302s9YjoRRbjiOn6Lg13HloFiYKu0P-p0Z0eteH47xpexSfZmiUXQNv8VA9xPc9fYls8kGvzS613_xrWgAgbvTzSUr3uk7boHmXl-38V3Wwg2e2aPe3aVwFqdMhBLdbioqP0clw4M1KlRMvLNvSLzOzLHlhGI4Z_wZFGEO71coicqxiMHVcuZLvo7N2Jpks1FYXOlw1l9zlG3wlgsoAV8uIT8zYehQ7YsqV7cGXURuul7shnNxgVr_EqEGB1c85DqSt-8mDuWqEic08mLF6d2k5Su2eycm3KYFNBSbXGc6Oj3TBkRv1H4zGWNOp-MCRnDnrs1T6juNr-prSkoxwbmncI5Nb129Qw928WiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی جان‌فدای ایران: تاکنون ثبت‌نام در ۵۸۲ گردان از مجموع یک هزار گردان کامل شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/462252" target="_blank">📅 18:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌ انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
سپاه: لحظاتی قبل چهارمین MQ-1 در چند روز گذشته به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان شرق تنگه هرمز رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/462251" target="_blank">📅 18:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S28MsoNylIAYOjESI6DXQDOO6lulcPUvXB4aJA11L7rpD3zwx83huCDN9NE06DEZzOE0TEw79wpUsUPy_O39HezdRkJzGbkA9mRci-uUytuiprNwQ8wOArFJUBFaHXdGpqrN0GT0RZoglfTtt8Zng8aelK9oHd5SAW3LiRvBvQVqbUlLP-Lh33Xj4yt7n73Cp-zJgfugQvgvk4gON9p1QEzFjPkkJWiwBkplc2SUojtVIG3s1GEfR6w8ZUWXmTR3vaCuhBU7z0CDgVoGVxMDnW-bOIwGOFjMrfmG6ePBGDNYxS_sSbXiHYpYWuGdesFwsu6k7fsEy_K3xUrtbCLESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5ePqZD-UiBm5vuKn85ycM_XQJCIe_aKUzsWljV6HHTT8Xqo3drj-SaC3Sy6UUIbGIlyJ0K0v-YPbdzVrS8Y0NwvwZXtitVNtIk5aI-wX1jPJrhqNJjnzoxkuB-kM4fPFNuLFUPQIDl8S1FQL4EC1X2qfxY0qYUOm0wAcf309tK6uNP9_TlCpSSIUnw8ej41jPcJAzSl2ePu2rauEmmn9MmnU-H3m45PToCaizINAdEDoFsP2tlq_J2tjcq4lSQUkvro9XW-TmSTAyblPrWbKRzN4fxkgGNnQeQFGRKN246Wjf4Yz0OkKjmmwJjt0fazldw84Niw-d34F7LzTbzgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsO-e_NNypjCjUAKnQn1_-NKz1gz-KXs9UDHSdQPBqNMYJB53cMAsh66HQQqAg55_ZAmJwNX-4-rDlZFCEITmuPR_ovdZvHHerFPplXUnhowhySROV-j4zRoKUHc8dUobFyAB5o8pryupkm8BYkwyLnuHSQAekyuZXyhA_6LOXfNOzL2aqYQM4YTVEW7HkP620-Gb0IO5vVR5lSuA5mjozAh-96tOkLtdw_rPNzzBUJEwhZ_DfjleDzoSpomZUUkEEReX8htaeea8sN32WkljwpREf7wiUYLOZqkAw8hp3HptT0DGsYvMMad7OcJO3gVvHficoQKG6aav-6xT0nMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhQzW7ESaA2WCZmtJddYZO7ALG9y0i8yRV6_Qlgm5GP4n2gFC7bSN8OC4RsUJiikijugSGsmxPB3biFV-n63GQMWKve1HC_5BJWjT0pf0duGjkD_s3OEAMlbsofDhq9LePaswjI9dVEHLXhq3OTHfypYtZIqMHnfeqQ4etnMRggoRHAT8WBKfQWURwXUwKBA9-oFssIzGbPWdlSLrRaaWfJSEImgzjnZkTk5QscAfU1n62NAyOVIs97II4KAQRIn6bUXvNNQZflAVZLQFOLYJCR-WztjtUE7Ysx-ygcxdeMQ3LT2PKELWm8EcQIWvEXs5geQ2cSKm-0O0dtfQyG2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsOOnWYd7Ywzd_VcS41uiHyZk6G10IXLY7TfXEJLEMQVsnbgr01YUpGGHLWwfTywlAP0EJ6C-38XuWHTpeKQ7-6hHCoGWQgTptLuiu7al4Gf-JgecD4YwG-zfFNPm0rUCM_mAxaYoz14uyjEWRGa3BuH8grR7rOLHKii5fvVT_rLgxf5bVR6Wf9P1SNVwzIZzVXuFmPoipLhZFUymBBXRHb1_WP4RrAMmIpj-jyUkhe2VnciazAGgEFtC19VxbQQM7jLBP8gtYT4t2HvxsIK6v2U9rpRRt1ud1b9vFPhRWH5Zb723HxLQU7qaZq6hzyMVlxFxI8uD-tXUSPuGU3eBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار رئیس اتحادیهٔ میهنی کردستان عراق با قالیباف
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462246" target="_blank">📅 18:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYGtWtuBVU4U-BGJ-Av3L8l6z58zOWVETHHfzkcifU2W8wYGNZl1mh7IIQJtV6Jfgs8TsPpP8UNkfMKbjSSSGnZDVWA7biR-mgh6S3eSh7icanC0BsbcoW3ccSpnoPf3IvdVgiCQe4X1VrrGwXZSm_mcnT_zPULiAUlt23RitK9_icTaWxIsakyAalfFe-xx6dj188PiSs-zT6dSbrQyZLfMRnp2zv9H5uhcsGZt0ehLr4Nd6wiH-_PoTBJHVXUgyX0atO2-svoinNZl1-kzk3msNk4RIaEQLv4fmCtApmdva0MNIebZVqPaGRlZMG68_TrYqhbBxLWQMGg-xnw-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از دریای سرخ حذف شد
🔹
روزنامهٔ اقتصادی عبری کالکالیست:  تسلط نیروهای یمنی بر تنگهٔ باب‌المندب، تجارت دریایی اسرائیل را از هرگونه بهبود احتمالی در حمل‌ونقل دریایی جهانی حذف می‌کند و این رژیم را وادار می‌سازد به استفاده از مسیرهای جایگزین پرهزینه ادامه دهد.
🔹
این در حالی است که اسرائیل در ماه‌های گذشته جنگ غزه، تحت شدیدترین محاصرهٔ دریایی تاریخ خود از سوی یمن قرار داشت و خسارات سنگینی متحمل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/462245" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAQvIkP2DALQBbulgLkwN9B_I_yt3jxGX0OYWxfbebtgcgmXWsybqwHaDtRRm1_q-_u67eVAoQNnBd_DZLXOsK_kVV0pMpKnwNd_Ik_O7m8ajygYq9Qh0QSIDs6lyQrSL7KukThV2rUWov1nFRMRLSTqvzsMv4C5x2CuC5rJQkjTxy18MGW28bpqf1qFxhtUMyOmKjJTP9fVAVROVfT6lH5NaQllpr7Te4i7XEY8eEn3WKj5If8AmDd-ZJbAdXpT8fVVKmSHjeV9zow2TUt6NiP2kw2Xen2ib1881deP0i0VHbkIDr0r-Dzg3t8R02HS_lBxfq6AuZsOOURpxyEzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا «نسل زد» پیر به نظر می‌رسند؟
🔹
نسل زد، متولدین ۱۳۷۵ تا ۱۳۹۱ ، بیش‌از نسل‌های قبل در معرض فشارهای مرتبط با زیبایی و مراقبت‌های پوستی قرار گرفته‌اند و برخی رفتارهای رایج می‌تواند باعث شود جوانان این نسل پیرتر از سن واقعی خود به نظر برسند.
🔹
مصرف زودهنگام رتینول و محصولات ضدپیری، استفاده از بوتاکس پیشگیرانه، استرس مزمن، کم‌خوابی، کم‌تحرکی، مصرف ویپ و بلوغ زودرس از جمله عواملی هستند که شادابی چهرهٔ نسل زد را تحت تأثیر قرار می‌دهند.
🔹
فشار ناشی‌از مقایسهٔ چهرهٔ واقعی با تصاویر فیلترشده در فضای مجازی نیز می‌تواند استرس و نارضایتی از ظاهر را افزایش دهد.
🔹
داشتن روتین سادهٔ پوستی، خواب ۷ تا ۹ ساعته، مدیریت استرس، فعالیت بدنی منظم، ترک ویپ و تغذیهٔ سالم از راهکارهای حفظ سلامت و شادابی پوست هستند.
🔹
پذیرش روند طبیعی تغییرات چهره و پرهیز از استفاده افراطی از محصولات و روش‌های زیبایی نیز می‌تواند به حفظ سلامت پوست و روان جوانان نسل زد کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/462244" target="_blank">📅 17:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدور کیفرخواست پروندۀ کثیرالشاکی گلباران
🔹
دادستان شهرستان دزفول: پروندۀ شرکت نیوساد گستر ایرانیان موسوم به گلباران که بیش از ۸۰۰۰ شاکی دارد، طی ماه‌های گذشته در دستور کار مراجع قضایی قرار داشته و در روز‌های آینده برای رسیدگی به دادگاه صالح ارسال خواهد شد.…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/462243" target="_blank">📅 17:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHzizlvWQ-_6WS-fzru3BYPzpzRPLrE5tHzZ-E_wG0A0St_2q7oXHIelRRUmv2q1mEtLtruSqMRs0yoOnxw8eH8L8LLht0wmvhxjcMM4VbwaAnRsd-n-DZ0mHrocNOJrMKWkWdw2dHeShaJ9Typ1xzrS2KaIFLywIcYwzLyco1B5FpduJUHaVP9SqRorm3ZuseLXIO2G_GEodZtJuDHthjXdboGYo3So-C_FpB_JyPE9oikC4TVamiM1g01xd0ZwMdveU8YAJsTV2Xsp7gh_JDlO6yQmzoTBlrZROQEIXPRctsEXjHH-FTAGJbKhD3CgsVfxgN6eFh9k8jCsNcXLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرایهٔ نفتکش‌ها تاریخ‌ساز شد
🔹
بلومبرگ: داده‌های بورس بالتیک لندن نشان می‌دهد کرایهٔ روزانهٔ یک ابرنفتکش در مسیر خلیج فارس به چین روز دوشنبه به یک میلیون و ۳۵ هزار دلار رسید؛ در حالی که پیش از جنگ این رقم حدود ۱۱۲ هزار دلار بود.
🔹
این رکورد شکنی قیمت در شرایطی ثبت شده که تنش‌های نظامی در تنگهٔ هرمز شمار کشتی‌های حاضر برای عبور از این آبراه را به شدت کاهش داده است.
🔹
کرایهٔ ۱۵ روز سفر یک ابرنفتکش از خلیج فارس به چین حدود ۱۵ میلیون دلار می‌شود که نسبت به ارزش ۲۱۶ میلیون دلاری محموله ۲ میلیون بشکه‌ای، حدود ۷ درصد از پول نفت را می‌خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/462242" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665377c745.mp4?token=ik6K0DGPhOpK5vPekhr6RgSVezY1XvWk-WohP541_AA2vKMQgbQ_4m3p8qopr7gQ77xPMDCOL4ItT4wDGHdN5b7PgfiyphNCd-5awgZwsnrbmU8x9ji_ZxVnPZalipa_G1-jjbNQSzl0cUTBTwUOdGP3tvLLia2MLRvqpzStY6HDk7KO9jzLd0ytRzTInbAKDYhVSqzSmBgnvabJS2yNEhoP9cwL-FU8aX1O8293EqoO50hce7PogcyjYlq98cayzb_ttCID1J89mHrRcMIA3b1x0LdnnBPdKn4jdXEjMszWpyr7mBWdC5DIowLLV4asMqVowB4mJLQub2qKFA-UFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665377c745.mp4?token=ik6K0DGPhOpK5vPekhr6RgSVezY1XvWk-WohP541_AA2vKMQgbQ_4m3p8qopr7gQ77xPMDCOL4ItT4wDGHdN5b7PgfiyphNCd-5awgZwsnrbmU8x9ji_ZxVnPZalipa_G1-jjbNQSzl0cUTBTwUOdGP3tvLLia2MLRvqpzStY6HDk7KO9jzLd0ytRzTInbAKDYhVSqzSmBgnvabJS2yNEhoP9cwL-FU8aX1O8293EqoO50hce7PogcyjYlq98cayzb_ttCID1J89mHrRcMIA3b1x0LdnnBPdKn4jdXEjMszWpyr7mBWdC5DIowLLV4asMqVowB4mJLQub2qKFA-UFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل پرتاب دیشب کوکتل‌مولوتوف در پونک تهران با شلیک پلیس دستگیر شد
🔹
پلیس تهران از شناسایی و دستگیری عامل پرتاب ۳ کوکتل‌مولوتوف به‌سمت جمعیت حاضر در میدان پونک در شب گذشته خبر داد.
🔹
دیشب حوالی ساعت ۲۱:۳۰ فردی از بالای ساختمانی در محدودهٔ بلوار میرزابابایی…</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/462241" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-MmUgBQoBRcHTiDE2iVzpsYIQrkcGMsAJFJUo-TaMWJhba0IT4T3VAWM6des9_hCcfZbrNwAHxN5PaUulex_WKXBn0ArVbbOtKI6HbAnmdArLTtToestSAgfyRPOnSAobhwzg2AZ6a8Y6swy7uzuEWq3ZZItpB1Yi-8hNO732m2Xiuol91cNuku994L386vTTcjNELgrntuOCOOb05TaQ7KmSAVl6GvTOC_fk97aSNkNMR7csJoFO-2Ox1AdBfEJq-M7-rtDWivmwrDCczv2pTMeWIIKsCItVwRNaEFcXotEGvrxITREoOl94BHZbMZ0etGQPjiYTadWakJpcsifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکایی‌ها بلیت بی‌بازگشت می‌خرند
🔹
داده‌های تازه دربارهٔ شهروندی آمریکا و شمار کسانی که این کشور را ترک می‌کنند، تردیدهای جدی دربارهٔ چهرهٔ دیگر «رؤیای آمریکایی شدن» ایجاد کرده است.
🔹
آمار مهاجرت نشان می‌دهد معادله در حال وارونه شدن است؛ نه تنها شمار خروجی‌ها از خاک آمریکا افزایش یافته، بلکه هزاران نفر نیز شهروندی خود را به‌طور کامل کنار گذاشته‌اند.
🔹
بر پایهٔ جدیدترین داده‌های دفتر فدرال که مجلهٔ نیوزویک منتشر کرده، شمار آمریکایی‌هایی که شهروندی خود را ترک کرده‌اند، همراه با دارندگان کارت سبز که اقامت دائم خود را پایان داده‌اند، به بالاترین سطح از سال ۲۰۲۰ رسیده است.
🔹
بررسی‌های مراکز پژوهشی نشان می‌دهد فشارهای مالیاتی، فرصت‌های شغلی، شرایط بازنشستگی، کیفیت زندگی و حقوق باروری از جمله عواملی هستند که باعث مهاجرت شده‌اند.
🔹
همچنین تحولات سیاسی آمریکا از دوران نخست ریاست‌جمهوری ترامپ، به یکی از عوامل مهاجرت آمریکایی‌ها تبدیل شده است.
🔹
نظرسنجی شرکت «اکسپتسی» نشان می‌دهد ۸۹ درصد افرادی که قصد مهاجرت به مکزیک دارند، دلایل سیاسی را عامل رفتن خود عنوان کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/462240" target="_blank">📅 17:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=s-HLwb6aUXN-5hc5JcII04Kz5kpX0tVZtiv-MkmjkO6YNOXq-dD_1PDoM78uyVwb7DthQfadeBV_CXn8Sunj9A8iXbebO2RwAkxmEmR8aMSjpawZ7uSHzRqRdEWnbLjFvq5hITmVBPSLcwE9VVcLEsgX_IBtF8FaVse9Pn-j5qpLm2BW35K-9CDvFAgTvX4F78dxXVonzcUoMVOxrxQ6Pb4OCTGNBdLBl5mTXFMugorum4NHZa6s0i0Xsr526s89RRgtreRwRJY7FaKmmAtVkfaZljqMN7eq6PONSxDNFd6fqpXzTqsOjwgyFmmrTAvmTKW_1GazIFIhKsOfTAf5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=s-HLwb6aUXN-5hc5JcII04Kz5kpX0tVZtiv-MkmjkO6YNOXq-dD_1PDoM78uyVwb7DthQfadeBV_CXn8Sunj9A8iXbebO2RwAkxmEmR8aMSjpawZ7uSHzRqRdEWnbLjFvq5hITmVBPSLcwE9VVcLEsgX_IBtF8FaVse9Pn-j5qpLm2BW35K-9CDvFAgTvX4F78dxXVonzcUoMVOxrxQ6Pb4OCTGNBdLBl5mTXFMugorum4NHZa6s0i0Xsr526s89RRgtreRwRJY7FaKmmAtVkfaZljqMN7eq6PONSxDNFd6fqpXzTqsOjwgyFmmrTAvmTKW_1GazIFIhKsOfTAf5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه ۳ از نفتکش هدف قرارگرفته‌شده در نزدیکی سواحل عمان
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/462239" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تلفات مزدوران سعودی در حملات یمن به صحرای الجوف
🔹
رسانه‌های یمنی به نقل از یک منبع نظامی یمن: محل تجمع مزدوران سعودی در صحرای الجوف در شمال یمن مورد هدف قرار گرفته است.
🔹
این منبع با اشاره به اینکه در حمله مذکور، تجهیزات نظامی سعودی‌ها منهدم شد، خبر داد در…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/462238" target="_blank">📅 16:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f896bb57d2.mp4?token=cc7MCJ2dF0lqaz8HJjYuMR9VGUSNddMBQDgxa5My9bBtZzBAbOMsK4TdhJY4JI9MZC25IhZPq-DNCHrujPnnlFb5n1LdNR4L-KbqI2WCmQbTMk4AyOxQOuGXC2v_LrjwJDagMK2ViaoDgUaO4t855Pi4MjPF2w1ge2jcQiB7oomijpoUDnih4VdYOaeMqOeoRFZCNfwN8_Vr4fm9g2lCltSA3DARgMb7BA5Tik6VWZNm15pz8zFe-EsHPW9ORvQ_IqOvSjQMIcKfebAyu6kVYbPew7MZGuQ3hNjm2j7CS3wrLge7KBV2B5rnlmMMaczdvwnIVzxhWGkINclyWGUaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f896bb57d2.mp4?token=cc7MCJ2dF0lqaz8HJjYuMR9VGUSNddMBQDgxa5My9bBtZzBAbOMsK4TdhJY4JI9MZC25IhZPq-DNCHrujPnnlFb5n1LdNR4L-KbqI2WCmQbTMk4AyOxQOuGXC2v_LrjwJDagMK2ViaoDgUaO4t855Pi4MjPF2w1ge2jcQiB7oomijpoUDnih4VdYOaeMqOeoRFZCNfwN8_Vr4fm9g2lCltSA3DARgMb7BA5Tik6VWZNm15pz8zFe-EsHPW9ORvQ_IqOvSjQMIcKfebAyu6kVYbPew7MZGuQ3hNjm2j7CS3wrLge7KBV2B5rnlmMMaczdvwnIVzxhWGkINclyWGUaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: تمهیدات لازم برای تامین سوخت مایع نیروگاه‌ها در فصل سرد سال اندیشیده شده است.
🔹
تا ابتدای آبان‌ حدود ۳.۵ میلیارد لیتر ظرفیت ذخیره‌سازی گازوئیل برای تأمین سوخت مورد نیاز پیش‌بینی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/462236" target="_blank">📅 16:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1ecf6fe.mp4?token=styJnxlpoIHl0mmphmNCyCwtd4AuwNGkneCvu2AvrIpMMptA-ATiwjwK5qdnjheTO6lNeuwUJWE5E3JL9jwQIPCPJ4M1NyKfzP8-WGK9X73IaHXZNv4ubHUW6XeJY9c-KSBH75OBQh-NSN8ungrK509-L7WZ0W3asaKV4Z1dpm65GMUD5SNjbo5SASj6d62XJzymaUpKAFqFOuV4I1Btxho95p68FssBb42ARAV9ngRmPSQd4H5D8AsVu0G6Z17OSr17fabjnBzLnUdvMDeKvOJjY21DeywdEsxxmtlOt8cLEKOj2am3d7KnFEetxO220ss5q9T1Y1qr5UAsIX13fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1ecf6fe.mp4?token=styJnxlpoIHl0mmphmNCyCwtd4AuwNGkneCvu2AvrIpMMptA-ATiwjwK5qdnjheTO6lNeuwUJWE5E3JL9jwQIPCPJ4M1NyKfzP8-WGK9X73IaHXZNv4ubHUW6XeJY9c-KSBH75OBQh-NSN8ungrK509-L7WZ0W3asaKV4Z1dpm65GMUD5SNjbo5SASj6d62XJzymaUpKAFqFOuV4I1Btxho95p68FssBb42ARAV9ngRmPSQd4H5D8AsVu0G6Z17OSr17fabjnBzLnUdvMDeKvOJjY21DeywdEsxxmtlOt8cLEKOj2am3d7KnFEetxO220ss5q9T1Y1qr5UAsIX13fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدایرانی‌ترین ایرانی‌ها!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/462235" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgdzZl3j2irZYW8wZbk_hOJX2bCjno6KnuapMirK8ng6D65sEAj3PS99t9bsoSiCtNFKB3wF5dxkNRdM4OpNO1Y9T8DgfYFflcSzKE6WV8i5EiEfGikutnQANswCyGeTUYoFn2tRNxn-p-Zw9is7i4hNhuctTlNUU4faEVRw3jFyYE7ezDxVJTBSV532Izyg7tFeTasxFpSZ2BD3sVBHhQZh9RzmIonIRK8a4ITEHqAvJO_K0ExbOkvurYJMmxAWPp44kqvoSAqqwDBvW29h_FhCyPK9_UicwaErYFEM5BHMhGQlzV3Shf6pz4kRbh8fVCgnnrrFop6Vr830hy0P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حزام الاسد عضو ارشد انصارالله خطاب به کشورهای عربی: گاو شیردۀ ترامپ را هرطور که دوست دارید بدوشید.
🔹
از عربستان حمایت کنید اما در سکوت! حمایت خود را پنهانی انجام دهید تا مردم محاصره‌شده و مظلوم ما بیش‌ازاین رنج نبرند.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/462234" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462233">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec91e0dc7.mp4?token=s62OISI0EtLba3ZelYNrKeMDtyXGOoFbg9y6xEAqNE98CjptyFGXRGGFmfisb6LxB505pco6Bizwh6IaCcdOFRnnxH-BXFicc6Q6E7x67I3TLkG1MJGZ4ve5wrROlZd3tMRKmFVFNOPOx3w3Oerwbf8RDkQAO1xyZh0WUZzD4QvAXvd6h1w82FO31KdMiXIgR36uId6Hi7EaBlEBF3x63BBWctISE2N76uRvLMccUypimMQCLF64kC_uFaqt8bKAtJHR74CI2V0BwCRMTyAN7iHFx0mKJqk1SyhPHtx_rIKuyZWzTTVUuG_uTtNoZCq7hTT1wdl3YlEtLuCshAwJ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec91e0dc7.mp4?token=s62OISI0EtLba3ZelYNrKeMDtyXGOoFbg9y6xEAqNE98CjptyFGXRGGFmfisb6LxB505pco6Bizwh6IaCcdOFRnnxH-BXFicc6Q6E7x67I3TLkG1MJGZ4ve5wrROlZd3tMRKmFVFNOPOx3w3Oerwbf8RDkQAO1xyZh0WUZzD4QvAXvd6h1w82FO31KdMiXIgR36uId6Hi7EaBlEBF3x63BBWctISE2N76uRvLMccUypimMQCLF64kC_uFaqt8bKAtJHR74CI2V0BwCRMTyAN7iHFx0mKJqk1SyhPHtx_rIKuyZWzTTVUuG_uTtNoZCq7hTT1wdl3YlEtLuCshAwJ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامۀ سردار سید مجید موسوی، فرمانده هوافضای سپاه در پاسخ به نوجوانی که با پویش حفظ جزء ۳۰ محفل ستاره‌ها شروع به حفظ قرآن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/462233" target="_blank">📅 16:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">استقلال لرزه بر تن رقبای آسیایی انداخت
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/462232" target="_blank">📅 16:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HriC1mZ2rDJdqCieFcy2cAq7EUCfzNnrJpkGZxL705-nKNDtsyC0zmppOCMVDpVrixahoaGnf9eWmriLvXWAD0Hi2NhwV3nfq_SwKTtgfg5yQRWRhqwPXGUPC3qdEEM1s-O6_5SdZayLcJdnCQD1cZNNpMH40_-JU2NdGzy0bN_e5OWnicYoi4VMgcxCRIhWaGm1DP_N9o0r0g28vNDuttEy98HrEXzlWqxcuRclbXz0UWDAH5BHgPdGBt4gXgZfEC-ZgL-tlAR3zRkfjxLAgaQgTi5p08G472fcCCYi8MP0HCIhilOvHyTYt2LedVR1bgkYwCFWapiUSrhCX--fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی دولت: امیدوایم از نیمۀ مهرماه رقم کالابرگ را لااقل برای گروه‌های آسیب‌پذیر افزایش دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/462231" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امروز در بهمئیِ کهگیلویه‌وبویراحمد صدای انفجار شنیده می‌شود
🔹
سپاه بهمئی: از ساعت ۱۷ تا ۲۰ امروز انهدام مهمات عمل‌نکرده در شهرستان انجام می‌شود و احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/462230" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFXxCg_yq91Vgzcp5A4suErn6spQusD89HlxzPv1al3gBMczTCODsx48kk35u4tIvXMjON-qAKAj_PJLfBH_y5FR9k1wpwqVTiXNb24fdiGinMhtiPigAwQGRSOQhbNYUFELkkCibzf-Idq_BqBJX_CFyXIIq2nZi30VpWLdH7H19OttlV9H0Eh5HmBGaHvJAoktGBq9VoPVgxCP4bdTJR_BfJG6oA6JkZE16tnjEPR6Fazgh-WaFlNwG34eT8mf-Fy7QyAif2TjfC0ZyBe7PayGWMhoTgAnrrkc__70DWSk2tGMZqG-UyxMbEChpBHv0C6Bf4UPzkzA99g8_E6wMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/462229" target="_blank">📅 15:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9161e60a.mp4?token=rnAvimsDkaH0HnszQ9HBExXDdnWuEolidCLjToiY3BelhJIpzii5-2qYkU-HheBVQ1wZxqwY7j4j5M3Vn3yJgDsUaBLx-IACttjy1L9rsyUn71qWsvrR-KqflAexU0VTx6yiDn-p8XXMeA_sTuAjgMUiIfUQzTE_VI_j51nAuh9vcDAc7d3vaFtqi3J4-HDQOEDkoU2XDxoPQlXu9C4DEH8_-YinuuPOIJn278uS_N9MC5378y6sUbQPxU2KQ2CXvx92fZ80VLU2wEvKLH_eghHMjBCc5RwB-lm2jAaLl7GhYp6LAUfhAxyFMf8UVWXlRbVZxrdCGJMEUhhcUaY5DFlqJUjflpnvBmqcfEeuTdw4qXeyDkN2dT7DR9nI8cbvricc6I4w7mtBWcmdVHJH3v6EVYHzglqY3vwDjt0wD3iHCc1oJoDRcyhPqdHoQ4NT5PRolPuwBUkBV3cq_XohLLiPGiZ48TpQekJHAmm6TktmbpDoV05fn9upjUPdOO0eZq_-9IESxV95nWv6HbF5kqZxwrn4-oovF9I3jtpBOx5_r5VhcyhMShbUls1RjYoPBcM-8iTv0kEjZWQYOmbsoH72Pe20RIjOmpgJ0MB7RriL6DjwhLf5gwDnwuNLwaHVlP1wLCAC8OrDGpVs7Pt4VlCAAo3FKdz9cN70u8XPxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9161e60a.mp4?token=rnAvimsDkaH0HnszQ9HBExXDdnWuEolidCLjToiY3BelhJIpzii5-2qYkU-HheBVQ1wZxqwY7j4j5M3Vn3yJgDsUaBLx-IACttjy1L9rsyUn71qWsvrR-KqflAexU0VTx6yiDn-p8XXMeA_sTuAjgMUiIfUQzTE_VI_j51nAuh9vcDAc7d3vaFtqi3J4-HDQOEDkoU2XDxoPQlXu9C4DEH8_-YinuuPOIJn278uS_N9MC5378y6sUbQPxU2KQ2CXvx92fZ80VLU2wEvKLH_eghHMjBCc5RwB-lm2jAaLl7GhYp6LAUfhAxyFMf8UVWXlRbVZxrdCGJMEUhhcUaY5DFlqJUjflpnvBmqcfEeuTdw4qXeyDkN2dT7DR9nI8cbvricc6I4w7mtBWcmdVHJH3v6EVYHzglqY3vwDjt0wD3iHCc1oJoDRcyhPqdHoQ4NT5PRolPuwBUkBV3cq_XohLLiPGiZ48TpQekJHAmm6TktmbpDoV05fn9upjUPdOO0eZq_-9IESxV95nWv6HbF5kqZxwrn4-oovF9I3jtpBOx5_r5VhcyhMShbUls1RjYoPBcM-8iTv0kEjZWQYOmbsoH72Pe20RIjOmpgJ0MB7RriL6DjwhLf5gwDnwuNLwaHVlP1wLCAC8OrDGpVs7Pt4VlCAAo3FKdz9cN70u8XPxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتفاقی که مرزهای فیزیک را جا‌به‌جا کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/462228" target="_blank">📅 15:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlKmowr9P0-z9mwP2KFCykTnUC4h6BckLDc08lRM1vpO7lmEn5hwRLxzSJ-_uwB8rrGGVcdibRZ2wgqMVnOCwktNenWfz4L38EbOxOCPetZMyAfFJrEFYZ6vgN1qPLj4rk5CNNqyBvYr5kI9DQEuiu00Bs_LUpMvxx6dSMAIu3RPvQkBRBQlFT2U_lOTSwXbCBrWzSxrlsLaWJUV7TFLai6OQABmVzjrPXxA3X-Hw6ghpHjy0J7qzE2ny2wYhRZfxLhSgfP0Dw8d23_mNfIRY0AHY7pPliHp4B8eHGsVUwHicTfk8SlRwQ5AtwBs7JUgcRE5ZwP0Tk1yd_FgEhgWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز بحران بزرگ سوخت در جهان
🔹
مدیران غول‌های نفتی آمریکا که در زمان آغاز حمله به ایران به ترامپ دربارهٔ پیامدهای کاهش ذخایر نفت هشدار داده بودند، حالا از آغاز بحران جهانی سوخت خبر می‌دهند.
🔹
قیمت نفت خام آمریکا نیز از ۱۰۴ دلار عبور کرده، قیمت بنزین نسبت به سال گذشته بیش‌از یک دلار در هر گالن افزایش یافته و قیمت گازوئیل نیز در آمریکا رکورد تاریخی زده است.
🔹
ذخایر راهبردی نفت آمریکا پس‌از برداشت ۱۸۰ میلیون بشکه در دورهٔ بایدن و ۱۷۲ میلیون بشکهٔ دیگر پس‌از حمله به ایران و بسته‌شدن تنگهٔ هرمز، به سطح بحرانی نزدیک شده و در آستانهٔ رسیدن به کف عملیاتی ۲۵۰ میلیون بشکه قرار گرفته است.
🔹
مدیرعامل شورون با اشاره به از بین رفتن بخش زیادی از حاشیهٔ اطمینان بازار گفت که دلیل روشنی برای بهبود شرایط نمی‌بیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/462227" target="_blank">📅 15:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7-nn0vqiaxn7GtwwVftG65gocCkAfjkZQsz9QQHxonz5YrqcxPb3b7vW7-CT_wtt3VR4CSzaLO8Um3FsgNlVCOojCbCHkErNOvFb1q9gb7mrhFIqxanuF9kHFqB08bJMidf9EnSRAd9ocku5qOLtdpSDUSzEjHek03SYPfbEn2Qm8rrFzWWONHLFDpcZOlLDv_DTyAPOgx2Jx7CQMv2ybkZDgE9rX2RM6V96snImMiCmrffeG59FWBhWan1S0M7tcE_iEBN_d3stP_KfYF6PeTDiiaRB4R1HCRGonW0lpmzdA7KidSQMyIgyQZj_1auQ7DPt26TE6LO_FXuB5jSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بالاخره رهگیری اف-۳۵ خود با «آتش ایران» را تأیید کرد
🔹
پنتاگون برای نخستین بار به‌طور رسمی تأیید کرد که یک جنگنده رادارگریز اف-۳۵ این کشور هنگام مأموریت بر فراز ایران، «هدف آتش دشمن» قرار گرفته و آسیب دیده است؛ موضوعی که پیش‌از این تنها به‌عنوان «فرود…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/462226" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATr7S8jee_EVSRh06zzTXG_X5Tx3NoIdqWC_T4mIEakhuyfimEKIw-Yf_OB2yOXpis0Vd8kbO1OpiR-c65Jg16J3OADJ2D1QnnYRdYWt-oY28rQuLKXsBlr5nQqEkjN2JSDeRNKIkZJLZ6WAJ-g8qfDHsBAPHIUHbFIPtv_2FzKTX3wTvj295PgXXVZ1WpxlA2VSe_rsgp356AnD1jUk-XNHk6pRlqKgWgQKDd_bkon5YCKreaZtq6hA_uCH0VOoNEbgCWaeITnumx1Q9i-TklZ5mhJkH6byD1Ky2ugXrLeCiJb_H1Qt5m1cutwDIkOZQ6O09M6EEovIbU6DNxfNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره نفت گران شد و ترامپ یاد توافق با ایران افتاد
🔹
هم‌زمان با نزدیک‌شدن قیمت نفت به ۱۱۰ دلار، ترامپ باز هم در پستی در تروث سوشال از توافق با ایران نوشت.
🔹
تاکنون ۶ بار پس از افزایش قیمت نفت در بازارهای جهانی ترامپ محتوایی با مضمون مذاکره و توافق با ایران…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/462225" target="_blank">📅 15:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlFvpyKeq0w5k0pevegHqB1-z2mhUyJKN2KVII6DEItIK3mexG4e1TZk8I7XQxudAGrWfaW1NGHeSo42NH1T52TvFL6z0BEmJyqcY33pG5En027-p3fjTK_zHTJ2AEF5IhNqSKcqbdNu3xbkzLk1wQfVKWCFezyR6khMaabCV6Pohu2CJdwc9zPHnXXUBbDGi2gpYRnogBNUnJZcUXdQvDk7MMJgQJdHExw2giOmU_51CbbxaZAHZbbuz3psqsBy8uiUgsO0BMZtzI8eJ20KK_lqLliQevR5bHjvVIbHPPjympvQGz4C8lk4nBaUr619uswuimggiSCT5tLiDWR_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ویدیوی کامل گفت‌وگو با افسر شکارچی جنگنده اف-۳۵  @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/462224" target="_blank">📅 15:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvXTlG0zd0eE1eakfqsApVCPiXox17EXQMgW2t_mpNr93ZV5_DWmgdU1rWgUDAIj-Kf9G9Z7qKNpHCD5DcbwqubiSmSVVNRNIkGiQ1cJ0q6Ti2exULNSdT7TAbAdysz9iRLdzOMabfFd0Do_YIznwwAwVkhQ2Q8ivQgJx-zPeg3FxgrIgAxHmLDwAXN1aMWCcEvMPq20sNnoeB-f18-cbcdmQp06WbXYmSVk2xCTgspqWbiico-gU9qdGIF26hMJRearS95YARCRAuwrPq7JfGd31LLkpuZ41Oqzya9bnbmfk6TDMwirmZE2F3XKmAGIilMHaQw2PYdYAeM6EXZFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تأسیسات نفتی جیزان هدف قرار گرفت
🔹
همزمان با عملیات موشکی و پهپادی گستردۀ ارتش یمن علیه مواضع رژیم سعودی، تأسیسات نفتی جیزان هم مورد اصابت قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/462223" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxL0CEYffmGZ3sEYT2UzQqATA_bf1alpWQXRYQpcDFxX6FIYE8E5bc26nOLqTMGpOvBTqkN2U5LkL4DQKhOp7EVA4brx8dum71X-E8kDEuuIijMehPKC4g9I4a0fVMPRTRdWLKScNIm9qyFs3I51cKHekWwSk7_2Mnk4aEgT7dcg0wKWbndUIzAGllqrY-MZcGCH2kzJ2tHe6yVsiRiVkWgCOuv926hHlnIa_9kl8t9via8zcDxTG99JHUpXnbwXSTfxB1_RPG4prGo6PFkXLQx91wRSSoHyKjKiaI3XdpSe4KufHzInhpFmcDrRejT8HwFKyK31ZewCrn_kjotRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pflW6o345wypM65uGeeJMvIUBD_TLmYcSjPmQKZZA9phDigd71pE0zyo3JbsJTwNmk-UnhEXJyWXUE1kURFmxLjbtQT7TW67RfO3xDqvHEy8uvxVU5ZIFDJtdZrBDVDWguQhqnn7Ib25CatFSMYvlCR2kylQzVWP1NrdFBJO5Z70z3TcMv5fep4JCgTJlxh9-2SvJXchGsx2nFxSqmA_5PTGukkwIydT09lxpuLANM_lOpmX88eGWUAAeGYLMNZc9TpTQdggIuuEZizs23Vk1z1P9xsvf_6F7Cem69VPV-711Mz1astdwvE3TwikVc76M9Odl-2jNo6YpIJNsKXaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_FScmgyeIOlEHJEDQoql2w0pgKmfShKg0LKrCIh97epryg3ZT1cURWD_uUonIq2fJwQmhEvn3hrkrDHmvYN6dvbFbmhIVZ1AnjWeLhRYLujJ84Ag55I92gjBMqpFD5C-ZepHc-GJlmiij1Amcp2BgsfV-f3NaA7wEryc9wXG0Iauzgcocwuo1Qegwcmne_7iqTXx0-2LHGCtlGkz8mni1vYw9Y7WNK7qTV-4afYbBH94P5qZ7a-rwdxhyiGvWzWPGRRMVV5wqq9JYLhIFWQ1kCe9Bf-47W-NiCSlEtTYVI1iS_OteawfaU6TNXFZ5F8qjSmu6DyrcfVsL9SlcZ3pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🔹
پس از انتشار این مصاحبه، یک کاربر در شبکه اجتماعی ایکس اعلام کرد که با بررسی سوابق و تصاویر آرشیوی، هویت واقعی این نظامی را شناسایی کرده است. بر اساس این ادعا، فرد معرفی‌شده با نام مستعار «براوو»، سرهنگ «جاناتان بات» با نام عملیاتی «ویپر» است. این کاربر همچنین تصاویری آرشیوی از وی منتشر کرد و مدعی شد که هویت او را از طریق تطبیق چهره و سوابق موجود شناسایی کرده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/462220" target="_blank">📅 15:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: اگر گاز، برق، گازوئیل و بنزین را به قیمت ارزانترین کشور همسایه توزیع کنیم، ۷۲۰ همت در سال درآمد کسب می‌کنیم.
🔹
در این صورت دیگر قاچاقی هم صورت نمی‌گیرد و به هر ایرانی می‌توان ماهانه ۷ میلیون تومان داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/462219" target="_blank">📅 15:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpawPE0wFBobuAa4ncr6aee5FIAe4h1Z1v6aiT60nmSA7srORXGkcGKNDU2RHBO0Bz2a_61UFfzsot-2d5HM0sl8LEe9CvpQtNugMNt8mj6nZyXci5dzweuiMjwwwemiJ9HHV1ra_y1tTf2aCNzVARC0442BkSKn8G7g8YlPzdj_pTF56ii65xcxUk2y95P2evEw7YubTQYoX6QmK3JBR13l4KgTX35mWEVce5s1k9ZMuT0COUtp2NVbAj_zkCU1I05SVG3MCBfw6GKet35sS4M24wcRrs5X-Eddb1TnurIuG-XUxOcuPr2IJvmtoOveqUxDh2VZVfY7hP2-6UVNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓
چرا دانشکده خبرگزاری فارس؟
🚀
اینجا فقط درس نمی‌خوانی؛ کار می‌کنی، تجربه می‌کنی و حرفه‌ای می‌شوی!
✅
آینده‌ات را از همین امروز بساز!
📞
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/462218" target="_blank">📅 14:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار لوازم‌التحریر در آستانهٔ مهر داغ شد
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/462217" target="_blank">📅 14:54 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
