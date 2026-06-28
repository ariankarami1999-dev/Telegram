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
<img src="https://cdn4.telesco.pe/file/U6N0wJ1VquEIA4yffvfDYnDnhgl5N2RiWWE3Yj5P_aqYrRHT-K_R7s_ZJCjmJt3oqBXRvS3uYtWhcaE6FeSNnW1rQf3nNCfIBSaEdodbDPZeweYCLoVTvguLTLQPtyfmu_505yEbjdWV47QrSKNHi5adb1-PP-iBSdlHsSlOJIpymNzAN9R56fj8ru_qZxqVTNxTZeC2lKP_G_US4B-LKc6TTsB8f0dRWC94PiGcRQApShYc13q4Vze5Xirik1zum_Icd01WsrE9cwSDUHZxZoThueuyHLeWVwz-ivlum4oR5EFDYHh3Lvbo80gs-t42npzqjvmL-AQG-ITFemE74A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 02:25:41</div>
<hr>

<div class="tg-post" id="msg-445407">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
حزب‌الله: ارتش رژیم صهیونیستی دیروز یک‌شنبه، طی حداقل ۱۰ حمله به نقض آتش‌بس ادامه داد
🔹
مجدداً تأکید می‌کنیم که آنچه دشمن انجام داده نقض آشکار آتش‌بسی است که تاکنون به آن پایبند بوده‌ایم. ما این تخلفات را رصد و ثبت می‌کنیم و حق خود را برای دفاع از میهن و مردم خود محفوظ می‌داریم.
@Farsna</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/farsna/445407" target="_blank">📅 02:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445406">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6369c7b.mp4?token=V4C7SqPCtSM3RiIWSJ90nMpvgedNEEly1jWtz9YJp08bW8TsQ_Ju3TqpKjDmNxyGv5FBoYP5um77hB4IXL153hdIzmeXK54kv3YRuLQZRWJKUBdvVZu2rses1RXZwqL4QFKLhaV-pPNXcR0z5WcY_giAxmbrcsOz_YaARrbz2skpCHNALWjLqPmIyWXgEqkqnTA_Oi2ariBIg2NcdN5Qpi3woXF8nokIGBFmxsKCNgxnUMwpMeKCpwqBVOxBqU-NvEAIHzx5Qi4ju3p-2J8KJfOKhleRGy0qEnbB2qBfk4In2NoptmP1tde2bLl2M-txHqs0EKGWv_XgU8-F0CPBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6369c7b.mp4?token=V4C7SqPCtSM3RiIWSJ90nMpvgedNEEly1jWtz9YJp08bW8TsQ_Ju3TqpKjDmNxyGv5FBoYP5um77hB4IXL153hdIzmeXK54kv3YRuLQZRWJKUBdvVZu2rses1RXZwqL4QFKLhaV-pPNXcR0z5WcY_giAxmbrcsOz_YaARrbz2skpCHNALWjLqPmIyWXgEqkqnTA_Oi2ariBIg2NcdN5Qpi3woXF8nokIGBFmxsKCNgxnUMwpMeKCpwqBVOxBqU-NvEAIHzx5Qi4ju3p-2J8KJfOKhleRGy0qEnbB2qBfk4In2NoptmP1tde2bLl2M-txHqs0EKGWv_XgU8-F0CPBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف رضا پهلوی به «عاملیت» در جنگ: کارِ من بود!
🔹
درحالی که پس از انزجار مردم ایران از دشمنان متجاوز و مزدوران فارسی‌زبانش، سلطنت‌طلبان در تلاش بودند تا نقش و عاملیت خود در حملۀ آمریکا و اسرائیل به ایران را انکار کنند، رضا پهلوی به تازگی وارد صحنه شد و با یک جمله همۀ نقشه‌های اطرافیانش را به شکست کشاند.
🔹
او گفت یکی از دلایل عمدۀ حملۀ آمریکا و اسرائیل، حاصل سفر دو سال پیشِ من به اسرائیل بوده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/445406" target="_blank">📅 02:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445405">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaksFw9MAwb-F37X-bIilicOHFvBZUzBIzqUdbvDO86la0I4FE53affm14J1-fvowdffx2Xu92KosYkH6O1nNQM5SdnBqciEwtpl03eA-mh1-olKOADeiMYattZFJ5WN-jE9S1nc8Rr8BDuhU0gZbDfTxq-mZ-Lnb7qyIpDoPwYEDEPLSC_Pxm-VuMSuUvvszVjZtCSVOmLZr2cORqxPRLpoBRb_XWCpsLnDOdJIJz_XVvUmOEhZNxSLxm2hBDkXU_kp6h396CtzFuTGzDv8DFkqHQWS1kDRO0ZOkqkYjFUgjMbPLPsQISXLapgiIB7BJck3_7i092zW-iewpC363w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس صهیونیست‌ها از بازسازی توان نظامی حماس
🔹
شبکۀ کان رژیم صهیونیستی گزارش داد که ارتش این رژیم از روند بازسازی توان نظامی حماس در نوار غزه و تداوم کنترل آن بر این باریکه نگران است و خواهان بازگشت به جنگ است.
🔹
بر اساس هشدارهای مقامات ارشد اطلاعات اسرائیل به رئیس ستاد ارتش این رژیم، حماس هر ماه صدها بمب کنار جاده‌ای و موشک ضدزره تولید، و همچنین نیروهای رزمی جوان جذب می‌کند.
🔹
طبق این گزارش، حماس اخیراً آموزش‌هایی را برای اعضای یگان نخبۀ خود آغاز کرده و تلاش می‌کند پهپادها و تجهیزات ارتباطی را از صحرای سینا منتقل کند. همچنین در حال بازسازی زیرساخت‌های زیرزمینی خود در جای جای نوار غزه است.
🔸
فرماندهان ارشد به رئیس ستاد ارتش رژیم صهیونیستی گفته‌اند، حماس در میدان قدرتمند است، هیچ‌کس تهدیدی برای آن ایجاد نمی‌کند و این سازمان آماده نیست کنترل خود بر غزه را کنار بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/445405" target="_blank">📅 01:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445400">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADG55XQnWy-oorIQOSfZClJXat5HSdvlaa158JkWgpsPiDuIlteMkave-fCrpAmbC9ETCggd1J6mHp5l_2oH8Ny49bUV9lKdtMXYMf-UtA6JkhJlKq5163I6oKoHx3rOjofrBFSnkEsBHtjOzK3B7lOAnLIpnCaL5Jkuh5JOniNTlT1NhbJgSDz_ZR9LJOIIWVmbnHODRiS11qvwPjKq4Ulxvu4qCVfjmpDqZIXpde8k4va09HfwxxUuuiMobz6ZdsEND95ZIdtyPhTy-MhGvmanzR_IOURHmPCwF90xGLLEb0-dsGC9mFWFNeugJsGaxJFukvqUSC8f_kwklaipzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oP_Ja0hGH1aiUda_9Jsw0dnfIC1Sj3O6hAVllsrFNqYMWw-V6vs_c_SX6aBn1-Gc8xfkPVrk4qMC87e3d4KELCxFVZj8lIlJb-6ps7zTI5epDK67vkxOpADVGR_iND73MZ_SPJ7hyKQQz6BwlrWtFkF0u9fNIK2zbCFeRhoPwLlPSgxD43X5byZiBH7CvFzeUesn35pz1u4BijfGLAkIl8WQWwRByZ1I5LuJZyJrCgE7DjCnYsQKpTc4HR5d1oLJ8s1OYlNOd45eBXlC_KkhjqLJCWwwHyEjILXE_2t0MuToDmrpOGVN5UtoJCx0kst7y7V1u8TqgjHQUMBJuHAthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epXSaLeoBvd5fQH1iv7ZhY2GPT1L-pAgPB1Zc6ituYCgqbyeWjtnVudsmc_Hsw4mJF1wAF_JSv_0399RNZMLiH7WVSn0SxA7f_TKfDmxSW-RndrAMnCSIEdrWST0Qwr-vGhcHlhDKfFlBDIPyuRtZEn38YHCQFO_0b58Lrp_Uc-zkjrdyV8ZCBDKnU-vtnwUfcYVb6_qfmyE7b_tVBEFShG-bdMZgf1gaklN6Ze-D6bg9zdfVFtM781PmYgp6SIQK3rE4DhO60mpyNjeWAjzw7dA4PKfwtAVisjagZ4TW0M7UHlFC7bqaiKetL_TkD3NBH89NRtavSD4pB7izf5KrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDE8ZtAvtMabURvItxW0qnMmsSb273K5uXOCOu_pfBfk0XYejUuaUH0JRIXhjB6nCwrX-sj8JgMTaOkK1JDAjBUdXZqIiBQRcz65HML4SfcEuos56Hz36bkmX9FSxG3RLvyWPB5GPsGpOLNpF4f77J3UEGSvzwmGWXigG9AMgYOIBCIITnCAg-vih4n94e3kcpQ_eKAYGHUjHTzqhWEcJPLU1z5IY_ZdWIATsdyg-wPLNi5xw7ALX2Xtw3M-8bDVaCNI-vffpztN2mClmLPPMJxlu0dcWzzxNCo2muEq-_6IjhdhWVJdSRkLZERXTSjGMa4xOIJPr5qrZfB82nxcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PeZjircco0qAh6tNuyTMTPq80KZhqn0NLwClGvZNcmIrv7qhiFFqgmyPC2vJwmiZad1M3k5DFGY9jLbIivb1ohu-ECjy4XMIPmrV6bnxGdoPlor1dHsl_m7BN33o8x8lnmiO2BnaWXQFyZLoLGNkeZMcRSXEhrKCe2vN-wWOG03mB2BZGkai-EO3H13MxwWPGe_8hfl7q3SJn08D7sULzp2MaC5IFTkgUN_sdEbF1Tc2BX9yiiKBntC4wB7S8poNtNbDn6Zf5QhsGCEA5XIRSGFxZ3MWSzilCVi-8FsVQs5IdWEfyNKouvbczYA_mqE5SOcurvGdlYQ6i6jf0S9_jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/445400" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEOWIsm02lxP_fhPANInAo6QukQ3reiXjODF6UkwlOlLJOmz_1dZUrNNFU7ZUQsif4J2yECVEUDUpTfoQ0HbYesR9S6LJYmsX3VFasGO9VLwiOYF9si19-1ykLNTE-4gtGtqSDuUaU5CGU6yEraZl1zCcZJ2nEtBELpm05UqqLWLDT-28DgSclnH5D_72tjGQ0Ax6qpafOe1IbN_26T2qmM6resFwPCvPGgNgGrwbXzG3a4cpc1QBlss57Lz-FPsm3kyqlChArf4eZ6T9XTcV3ls60C9sNLc9bhrezJMpkelxLxJlkUmu4zLaBTNhgjfjNDiekfvpi78B_qPmCbqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCWt-BChP9YdlPICHmPvFyK-JKpiMf2ikt_SuXTZ3eB8bEJgqx63BZpMGrUMLCxOGCMQiQQBW_eoYlGvdlyBh4dHW9zoKwgtHam9J4CzXo2iHJrWc9mvGStGUvZM2XREIT4rfp-rscI73vuSqPpeePH4HVDnfdKBVA-yEbGGacmv6GOos2T6eLigcFsESf-8ZZXcheJE4M0JH2BTLudXwy_Ro0TqM5cQh-m97fazT5P6cWQNmI54OGAGukVBSDysp5xz0uXWf0A8a2q1RNTQy5mOrQUSOCAb8TKY6PuL7SDXDHb30DEJejcIhObZYXeGIUyPM4CrO_Co1M4fFUc8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJsrr5p6iWPH4lxytADwWDOeKPvZ5IxcoyFbeShnBf1db3VghQSlTDnXeIGEDF5AVlUlDnf2PRa063Mt-hLpC84zfzgQqX_bJj9m1_7mD4pBPIjVTStCv6S7WyuEK_fMZOSyYaNM5Nz387r9GtGRL-oS1UilTDaARYDbW6VLmXzBh52SYEUIAgYGRfO05Wg6vKG4I9WU4f1vd6lhcRV8F4w2MAnwYOPuhqu19StTFARIxBoY-ptc4T2MTNlUjcrLCqkn4CoU_j8RGNMms-ejsJ1i_PJITsPcPu7pccwm0s0KN8-4yhK8Hau0dSeeNWdo9nPRMiWCUcEO3iNuDUCiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ5114mcHLG1h9PxvlC9lw9Bs9Z-_7gRcIrwZMJaQBjGCTYfiyeycFrxqjXaN6iQcxCRecPgMGee08Vg2I5iyW3UkvVaM2XssxT--8s2f7KXPJMJy1lLfjImsN6TTgjWUadz8DSAY0COVdY3LsKEJJbJfuwPMg3-EShSSqwVAnF7JWoHp8qrLPBqhAIt1IkZW_GH4mn2DQP_x9_pdEOcR-HPBxHmucnwSWADHSMAf0Ea0_ehTjCTWkvNH71TLUHpW2Oh1WPZp2SNk-pz3ctMoO-TxkRlFUAgCx-zPUyBPkEh7c_OQ4dGXV2ynl3cWqjOhVfYfuHNHhglg-IQZ-ciqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRsyZxlapUjVCa7qtERclwQge9G4rgmoswRMHS69HJ8cXP8Kn1eVvkQ0glwk1CFr1PfQ0_AfJUmS_xApBfCmCRPrvrLJsMum688w4_ZMDvbP4tdTTgp_-sKgfDcogYZch1e16K_nLY_z7C8KtqJM6JHOFg3gVYfa164WCrmqEcGImI2kFoHLD1t83DlvvWYI1uCJgfojPGM33bXR6NgH0vLuSvCajBWzWecmgY_23MRukv8VulKtQq4LRuSOof_8IEDPg7Pc1kU2_te2kSoxocnBDpoEBZQ8C_EEBPZXrd5YRtR-RhADtp7DEJhxqE6aG_7a-qyzHGmWNlKQj_vtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIW3UZRTBvv7WeHQRcMwgFlTRagCO-INXyeIlkBPkDrORl4bwecqgyh-E3EOJ_P6d6VxjbSaWK1yTbPjdcPi3zpy6-Z4N1X9IXHoEFAcpcTRA605j1nPfmky13JJDzD2JLn5cOgdjqApU0blKgiQ2Oc9rmZTyzxEm_2PRjhPWNwf-QQC1V14PYzxQpDJRT7FvAh9t6pmp_4vHTGpQ0Y84CwSIsJvhNZ7OwgVZONaYTrRz6WXsKhXWvr9jevh7n3Wmnx7E7dmb5HNaNRKQ4dVRHxxfKE8-fsrn_orRw4-rKbnLSoyArdOehPFuuU-Nw0RS97N9qbU25iHPZgnSMzg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZRy5Rp5Y4-_OuR6mGtNjuUF8SvQVcPh-twUW_qSA6Pjh9lPsEMO90a97roL_jyQ2Ey04SI8MD-6QbsoFJ_F-WIhzoP1yXB4uw9gJbeA89nhfyuF3RbQqIZU1fdX56fTdala32RKLLaQHOTpSXAaXG0Pq9MvHfTo-2QTgkDv6ITpIfzeXnyTncrN_IhYsqbpBEDCiaXhfcx2xYWCtZqsQ4rQrqgdCimRitAvcOqn5rI2mmyZy5nX-MxJeCVBKdPYidYaSw7rQmbcB1lskmiHgcdS-KvVkCiMb6OCOH0fFdrrRf8evzINl7Hf8ZplK1qlZIepDcXLofB2qnEkGmwWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpalknaRO_m_gDTwu7IThu0gcVdkhw-P7ggbAJBBtYHnjSLuj6eZmbmOsGPazeNOtAXDYRsvF-_V-5ffqT3-MOggdrFOJ4_Lvp_hJm6aTKD3JXDJ8udbBZ4dFjZD0jv8rpAdVwyRtoq3FYYktKN9PWSV0rPdwMbdmHnRbUEf59Ad7B0_JDET7DJDKk34hl0915IatFCuaav_Zfhd7RieVLONUpRvL_TSoqyKgpOnEDlz45a9JKdOaOlA3sQU9peYDJJ68SsrYtbSSWLRxb-YTORRmL_QQaZNi6XmzVU28n5A852sn_KxmEToC63gQz-dAPffLZFujFxSn0XueufeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2aLFqvJo-VLg6RfdsZhdlxgK7r0vncaYxOx-lz1xVu27qUO_1ZfPF7LxjNJg4VviHgp2kUePvdeFAtmfp7cCB2fbICslkRwYVDG9N2CL4rb12-0-WUGRclKzyhz27PPBcuAn0WPEqPa9ILbBplT_KrVV2kWnRoGDLD1zuvSCQu1gnJDiGXX-TnoUlJx5Cr2boE5idlE16UlKg-AjH8LdHVqT-5l1e4ATEspVJRSXwEYhL8r0vCsri4bPei2K1T1hL11saBLoaoqA7bZRDICPE6fbZr57DEx2M29P3OiAdwN6QI_LKcE5vSy4MRy-0hArD6jxezBBdiwJtGtsH0HCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRobVXrnfciKRJxgcqhYpqWDBevKnspQ7DJmWhSapQZMvMIE-Rhd5OngjoBQW4Oi4bHVU4AGHddn4akk188YXjmjSW57Rf6i5ErYpZojuAvXD_oa3LvUjcyZuXsaK6rBvXZYYjBFCcvbzX8PXpE1A0Md92KOoQ2QqvdCoJIyN7TvHAwjNYrjR3lBn3dBOjrmiXaIRN2w7V00E5hF4hvTRzV0eyd1-ES16zxrPybwgRRsW4anAiOBbuRDD71oJPeP7mUrvmErpzYkjUpIClW9ksazHD1KuQXxZlCF5nqlLozbwVrSmGC04NChqOWkLoQmZxs_25n1LcAU5e64ZaYPMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/445390" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ4AyXMST-PzpRZ4fjulmvUj1Xj-94KchAcX4od0lqrrnweHqYbC15Nd9LVbRvoUAv1xCwEUeGSokkRhYDRsN7uscKLX7uqHubQejoCtbfWuThHvnJzGCAH4O4Xg--AfRA_QbTo7b6iyiv42TZff16URc32pdTOVlk-Zuud5bDzZuwa2EvOYcHArJqJL9OCL5JuYKx-7U9AnoDMP3nqPpddEBrPb_ZNGFj2DOm0FCbDsqXTe5IayPdaQ1WIdFx01T3gBTwySCgc9hUMT1GN86CuaCH8OXMJVpQaJYD-kJ5pHygChlzyjhQd2nTvuwIFNk8y83OYeUq4wA-lSLm4cDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با مشاور امنیت ملی عراق: ایران آمادۀ گفت‌وگو و تعامل بین کشورهای ساحلی خلیج‌فارس برای ایجاد سازوکار امنیت جمعی است
🔹
همه کشورهای منطقه با درس‌آموزی از تحولات چند ماه اخیر، برای شکل‌دهی به امنیت منطقه‌ای که شامل همه کشورهای منطقه و به‌دور از مداخلۀ قدرت‌های نظامی خارج از منطقه باشد، و همۀ ابعاد امنیتی، اقتصادی و توسعه‌ای را در برگیرد، تلاش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/445389" target="_blank">📅 01:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJISdbIweFKg3tyxhyTZxTd4W-K1g-z9fXz6lZWh2q-WtCwqkqdoVubS7v57rOM_e4O2jyqlB58xxR41X1mDXHfJgS0ZSxV6BCYrYZebg4lNQoJfFDtHg6Ttnjb97MN_d0b-DeTQRLqF6AYdnWkEewCIIok45gDc0_2vcSs2c7yY_Typ0KW4tQbxEBGAntytmvvL6hTtQBOeymNYyn0ztC6DBvzTGSsEafJR8LPDp6WIBFGEnQd_I90JJ0XlH2HYqsIZYdeKclg4LNJappG_ZwDTQvP8LwRLsbR9A4vQk3qxDJkwmDoqe-FTV3i4JmYLNWOUX73fGB-lHEeEc6wl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی در بغداد با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/445388" target="_blank">📅 01:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445387">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_H1NcCwS1lMDEFNmyM1EXaumddr2rThbvbhs3x2gp9F-A35_QUSRHfUWnefyj_SCDiXePlcbIJKsdqyqyndBlyoRiC_ry-asTLLXiFGnC2IdwFMiO3te0L299sPWUQRImgNbnjKUE-fiPxKkPR2KPxt-VePybGTUMnPNPWAiuC--RrH56vQgnMlLyBqYz2kdJk8PKkKLdp_MFTaujEmwXP5EFFwlW125qUjIryVCPo_osj9KiDU4i9rTcbv04566eIyHNj04ZmyISMBa4wbGQVRvhEA7CsZBHjbkROCiRWSsGAOm2iYSu8G6ic_3XhbPDaMLCkGgRGCx-8Td-ZEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معتمدیان: تهران آمادۀ برگزاری مراسم وداع و تشییع است
🔹
استاندار تهران: تمامی ظرفیت‌های استان برای برگزاری باشکوه و منظم مراسم بسیج شده و هماهنگی‌های لازم میان دستگاه‌های مسئول به‌صورت مستمر در حال انجام است.
🔹
سیاست کلی بر این است که مراسم وداع و تشییع در استان‌های تهران، قم و خراسان رضوی با اتکا به ظرفیت‌های مردمی برگزار شود و در کنار آن، از همۀ امکانات و زیرساخت‌های دولتی و حاکمیتی نیز حداکثر استفاده صورت گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/445387" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319a000b0c.mp4?token=hgf7HI8ADWlRtZlgoR7uZZ0ABylGdZVhCNZS1aVVElkXkhVIixkCzaVoBMu9AQxNfiUz7Qf9L8vOzba5M1G9KN9Ls3Ib7meTV9R9GlOZkIgSHaDvwbU_tb118tHIkRbzTGj27XGusPU7Ei_Qqnuzr4lMrbWD5nwmaQmGAh8lq_TMK66ff0XCe456Z2Boq3RTzNdFfA_1gIGmvtRxyqSYomZ8Ab18qFjgcpcLqaevslTPOkHlTb0LzwMNpHGdfx37fiocxJT8PFxgcOn2VHeKfjlltdUCLwC4VCLQQNoCXNktTnxI99sXpArJYoeOTHu0PU3HoQVHHsdIsVnkxNGAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319a000b0c.mp4?token=hgf7HI8ADWlRtZlgoR7uZZ0ABylGdZVhCNZS1aVVElkXkhVIixkCzaVoBMu9AQxNfiUz7Qf9L8vOzba5M1G9KN9Ls3Ib7meTV9R9GlOZkIgSHaDvwbU_tb118tHIkRbzTGj27XGusPU7Ei_Qqnuzr4lMrbWD5nwmaQmGAh8lq_TMK66ff0XCe456Z2Boq3RTzNdFfA_1gIGmvtRxyqSYomZ8Ab18qFjgcpcLqaevslTPOkHlTb0LzwMNpHGdfx37fiocxJT8PFxgcOn2VHeKfjlltdUCLwC4VCLQQNoCXNktTnxI99sXpArJYoeOTHu0PU3HoQVHHsdIsVnkxNGAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کانادا با گل لحظه آخر به یک‌هشتم نهایی جام جهانی رسید
⚽️
کانادا ۱ - ۰ آفریقای جنوبی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/445385" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حملۀ هوایی اسرائیل به جنوب لبنان با اطلاع آمریکا
🔹
نتانیاهو و وزیر دفاع رژیم صهیونیستی در بیانیه‌ای مشترک ادعا کردند ارتش اسرائیل ساعاتی پیش یک شبکۀ تونلی و زیرساخت زیرزمینی متعلق به حزب‌الله را در منطقۀ مجدل زون در جنوب لبنان منهدم کرده است.
🔹
ساعاتی پیش شبکۀ المنار نیز گزارش داد که جنگنده‌های ارتش رژیم صهیونیستی شهرک میفدون‌ در جنوب شهر النبطیه‌ را بمباران کرده‌اند.
🔹
نخست‌وزیر اسرائیل ضمن تایید حملۀ هوایی ارتش این رژیم به جنوب لبنان اعلام کرد که پیش از حمله، آمریکا را در جریان آن قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/445384" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOUiYK5VK9evRDCZlfnLG0o0ReyxynSorZht7ImtmquaK7d3GigLJeoR1S3sOW0N8BtgF7yWcJsDjTerJYrS3k4S-CPBehyw_w16B3pmqoplGaK1n2P6O7OfPQhiXZ31CBv-juHlHi90skcpJUMgHg8pViQIl7_mFtzHcRkjNYrBr-QHo5bBjw6WzePsgsUYnA1D0v2ayKBEQ6F1jPQPwnt50yBU4jvb9oheEGICSsTq4uUM0-_grpv9HDDBnY80XyDu65H4b9MVZX2Sj9RtBUccgy95n9LHJhIESoaTYwZMzkZjb3Z2X8bIcfGaT7LsY_HIG7ul9woJTxR-oXmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیراندازی به سمت نظامیان صهیونیست در جولان اشغالی از سوریه
🔹
رسانه‌های عبری گزارش دادند که از داخل خاک سوریه به سمت نظامیان صهیونیست در جنوب بلندی‌های جولان اشغالی تیراندازی شده است.
🔹
در پی این درگیری‌ها، ارتش رژیم صهیونیستی از منطقۀ جولان اشغالی اطراف روستای عابدین در حومۀ غربی ‌درعا را با گلوله‌های توپخانه هدف گرفت و همزمان دو حملۀ هوایی نیز به این منطقه انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/445383" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۴</div>
</div>
<a href="https://t.me/farsna/445382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۳ – کتاب آه</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/445382" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLr-odsufTQSxFn1InO614zK_1w46tZNHxIbe-Hay70UEA9M8UcWnTb4dOGpFG2y6Z3FVSuRRTzrZtcx0oPD_Giebkm5gjKgVi1Lv3BKBmGRequ9lB-ilGCH7IQ5WBQQk6cwE9Mo7N9lY_vLlowGIcZLvNi70IWFXtcFReFvASZui1_nOzGSfrtv-SfjHEKUgEGn6X-RCEFKqLfVe1NHvXm5E1Xp-PQTqADtxkxtFV7S_ftN5skwsHOgGW7pjp-ai5iPkZlIeAobbb_0kI8PQFFv_I3h4XO2VEAnrQ766TgYe1m3fkQrmQ-gLndyqygTXEdy2UJpLyBeJ7bV_ss0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت خودبزرگ‌بینی
🔹
«بزنطی» که از محدثان بزرگ زمان خود بود، نقل می‌کند که روزی امام رضا(ع) مرکب خصوصی خود را برای من فرستادند تا به دیدار ایشان بروم. من سوار شدم و به محضر امام رسیدم. آن شب تا دیروقت در خدمت ایشان بودم و از علم و دانش امام بهره‌مند شدم و سوالاتم را پرسیدم.
🔹
شب به نیمه رسید و من در دل خود فکر کردم که وقت رفتن است، اما امام(ع) به من فرمودند: «ظاهراً دیر وقت است و رفتن به شهر برایت سخت است؛ امشب را همین‌جا بمان.» من با خوشحالی پذیرفتم. سپس امام شخصاً برخاستند و بستری برای من پهن کردند و فرمودند: «روی همین بستر استراحت کن.»
🔹
وقتی امام از اتاق خارج شدند، موجی از غرور و افتخار وجود من را فرا گرفت. در دل گفتم: «من چقدر نزد خدا و رسولش مقام دارم که امام زمانم، مرکب اختصاصی‌اش را برایم می‌فرستد، ساعت‌ها با من هم‌نشینی می‌کند و بستر شخصی خودش را برایم پهن می‌کند! هیچ‌کس به اندازه من محبوب و مقرب نیست.»
🔹
در همین افکار غوطه‌ور بودم که ناگهان امام رضا(ع) دوباره به اتاق بازگشتند. ایشان بدون مقدمه، دست مرا گرفتند و فشردند و فرمودند: «ای احمد! امیرالمؤمنین علی(ع) پس از عیادت از یکی از یارانش به نام صَعْصَعه، به او فرمود: ای صعصعه، این که من به عیادت تو آمدم و به تو احترام گذاشتم، مایه افتخار و مایه امتیاز تو بر دیگران نشود و با آن بر برادرانت فخر‌فروشی نکنی؛ این تکلیفی الهی و اخلاقی بود که من انجام دادم.»
🔹
بزنطی می‌گوید: با این کلام امام، تمام آن خیالات و غروری که در دلم ایجاد شده بود فروریخت و فهمیدم که رفتار امام از روی تواضع و اخلاق الهی بوده است، نه مجوزی برای کبر و خودبزرگ‌بینی من.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/445381" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445379">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkX_HBTgNYftvujp48kl8EAjFhU5ZSdGNRGVpjkIOKvJ8DccQRtbCyyjV4lBrw7QhxMfwJ3wtZH9HBo8gtd4J7tneRzzhpO44qfH-_UUPiuG9_KxjlE_LiLOznUr3gYqfMalv-KlwNpbvUuZShIQwEHO23pkHahsIvKLA3Ptz0L04-v0TlLfJtMUPdPXMU3gX98BhHW7e-NsuUQ5Gz4twTuTmiCDuZpUt_OeTGLYh46YfnePZfPOfHJwl1PFFPnUHmJubVejQsDTIHmOCQQo0SRqU_DVLWucz6b9lARALrC7KxS_F2mB8tNc-3yvi49A_dXQE-RNmJJeX8-2tPzr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد دانشگاه شیکاگو: جنگ ایران توهم آمریکای شکست‌ناپذیر را پایان داد
🔹
رابرت پیپ: ترامپ اکنون ناچار است که با یک واقعیت مواجه شود؛ ایران به وضوح در موقعیتی بسیار قدرتمندتر از ۱۱۶ روز پیش (قبل از جنگ) قرار گرفته است.
🔹
شما شاهد این خواهید بود که جنگ ایران تأثیر شدیدی بر محدود کردن آمریکا به عنوان یک قدرت بزرگ در بسیاری از مناطق جهان خواهد داشت و دیگر کسی آمریکا را شکست‌ناپذیر نمی‌داند.
🔹
وقتی که ما نمی‌توانیم از پایگاه‌ها و ناوهای هواپیمابر خود در مقابل ایران محافظت کنیم، تصور کنید که ما در مقابل چین چگونه خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/445379" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445378">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvYzMj8Y8p-GlyKXW4fsIdCrq8vfBCA7SXShZxGs1i5oyrAGaLV2_PtYSDDfVD3UNtQoSytkQdnlway1BDrvLBW1L5Wsrx2sF7EI3h0iSLYPzoXxR_5S6uA4AZI3dTt1wmbzRQyZrULALZ1Sbp6Eq8IzbOiJZIDgybMzW2AMMt0DzVayVCFu1ClS9G0LnPFQYmbQ6K2KEbJ5avalbNhyTL_JZJlumMjI_xeAdekSBdLxpy2jQLhzQQq2iquIvavRs9mDrke02EbglQ_8R587BgFTHIHQ8qXPX_xHvX_emEetkHlQS7WBCph_Rsm8RM4f_PlF8hnXWIa5nWVtk4wF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: در تنگهٔ هرمز دخالت نکنید و به یادداشت تفاهم پایبند باشید!
🔹
براساس یادداشت تفاهم، تنگهٔ هرمز تحت مدیریت ایران طی ۳۰ روز به ظرفیت قبل‌از جنگ برمی‌گردد؛ هیچ کشور یا نهاد دیگری دراین‌باره مسئولیتی ندارد و هر دخالت یا تلاش دیگری اوضاع را پیچیده می‌کند،…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/445378" target="_blank">📅 23:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445377">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b382afadf4.mp4?token=P1vSHVFXR8oydGiNzBEZiL1QJkx_k3EAxeyCZ3MsK-W6Rl0MkGqkb2sIMruAjJI7xQkWKdRD6J23GSRKgWxm1Pl5zTedMd2NpxE0JRIDCPBtR1mPGuoduMiFXFk92VxKRw3qeA_8AgF1aqt7YvyJmmsZ_JwDVcDNjqtbWxUb_f3m6EYxP5Ora11b1HbhuoodaXV80TKvucD_rRQKOSxXiI3UXKGx-prkvEJLJ_nRN1s5pxA-yWn8As92WmHPgKkkSUY0LqE7L4gQIEBG6UIqEh5h3yK54YWcmqjM3XGZBK4u5kmCQ_lFKajqNRwJzcoeStPjHBsf78tQ_S4iTk0q8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b382afadf4.mp4?token=P1vSHVFXR8oydGiNzBEZiL1QJkx_k3EAxeyCZ3MsK-W6Rl0MkGqkb2sIMruAjJI7xQkWKdRD6J23GSRKgWxm1Pl5zTedMd2NpxE0JRIDCPBtR1mPGuoduMiFXFk92VxKRw3qeA_8AgF1aqt7YvyJmmsZ_JwDVcDNjqtbWxUb_f3m6EYxP5Ora11b1HbhuoodaXV80TKvucD_rRQKOSxXiI3UXKGx-prkvEJLJ_nRN1s5pxA-yWn8As92WmHPgKkkSUY0LqE7L4gQIEBG6UIqEh5h3yK54YWcmqjM3XGZBK4u5kmCQ_lFKajqNRwJzcoeStPjHBsf78tQ_S4iTk0q8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ شب، ۱۲۰ سنگر در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445377" target="_blank">📅 23:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445376">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f17b33ff1.mp4?token=nrqXQi6qLc9cFHsXRV2MOk8tc8eGitoePBkwxQQ_a-Acz_2bBqmNBb5Q_pqPNF5NWR0oV6PwIllSUBNwSSQzRNCBqQxzTTMF6qa2g1TZg7_EzvUJ3p7diQhzBot0BE7wpBcc7H8qVvWITL_5MUz6Xv4NFYibBTybcSmKEEOfrXDNhru7g2o2w70dVsMsRp_twbT65YcymBXftaWu8AaWWLsOWBsdy20sbypf02qUfRPh0z7UJG8B4pSDtyLXQt2pQsHHOI8fJb1sJEB-9oDLCMORWgC2dOUqix4OqlFAO70Ydl5B0Vgz0z0qpp-YjSJFqwHfZ3cQ4ULqpAYIGe4-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f17b33ff1.mp4?token=nrqXQi6qLc9cFHsXRV2MOk8tc8eGitoePBkwxQQ_a-Acz_2bBqmNBb5Q_pqPNF5NWR0oV6PwIllSUBNwSSQzRNCBqQxzTTMF6qa2g1TZg7_EzvUJ3p7diQhzBot0BE7wpBcc7H8qVvWITL_5MUz6Xv4NFYibBTybcSmKEEOfrXDNhru7g2o2w70dVsMsRp_twbT65YcymBXftaWu8AaWWLsOWBsdy20sbypf02qUfRPh0z7UJG8B4pSDtyLXQt2pQsHHOI8fJb1sJEB-9oDLCMORWgC2dOUqix4OqlFAO70Ydl5B0Vgz0z0qpp-YjSJFqwHfZ3cQ4ULqpAYIGe4-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع نیشابوری‌ها در شب صدوبیستم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/445376" target="_blank">📅 23:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445375">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
حملهٔ هوایی اسرائیل به جنوب لبنان
شبکهٔ المنار: جنگنده‌های ارتش رژیم صهیونیستی شهرک میفدون‌ در جنوب شهر النبطیه‌ را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445375" target="_blank">📅 23:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445374">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976c416f95.mp4?token=HMy2WaHS26b6kYAnTcP1gCCUX1gdU3FB41toyRNeH2vuszXnEI9VXis610usF2yEFT3XgFMIJkx7TTnWvz_0vTQ53ECTjHJbJcOJPRcyZoaoPUimbiZNh68g73_jeSV8zDJJtaklbqJtuUyQM7linCrbpCga3gBEkDmPnv5idbvCRQXtFBAJvLMwQVcqjlY5v9sIOQDAK3mRxvLMzaACADJcvu2VOsP0Qebg8pC4O4KeGApjy2ScPf2WGQqirVJQYkeij8QanVDfKGY6oabP541MFO22kcgeB4OIJK0p9WMa27jrODPNlnCmQUF_4qX6xN5JLNpf1owIo48cJqKeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976c416f95.mp4?token=HMy2WaHS26b6kYAnTcP1gCCUX1gdU3FB41toyRNeH2vuszXnEI9VXis610usF2yEFT3XgFMIJkx7TTnWvz_0vTQ53ECTjHJbJcOJPRcyZoaoPUimbiZNh68g73_jeSV8zDJJtaklbqJtuUyQM7linCrbpCga3gBEkDmPnv5idbvCRQXtFBAJvLMwQVcqjlY5v9sIOQDAK3mRxvLMzaACADJcvu2VOsP0Qebg8pC4O4KeGApjy2ScPf2WGQqirVJQYkeij8QanVDfKGY6oabP541MFO22kcgeB4OIJK0p9WMa27jrODPNlnCmQUF_4qX6xN5JLNpf1owIo48cJqKeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمر زمانه را بشناسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445374" target="_blank">📅 22:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445373">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54c4b3eb9.mp4?token=uIMAbIekj7jsWBnU2Nez3h2dqMxxO7rGbBKNN2-YdoxwCPxElDOD3JE2eZugtBBk8uHCpbSqJGzB3oAZd-HkkkVoO9mhdWu35s9SoLS097D97AYiBPX0Z-RYhUIX3qX0GB1orMWyNb-53anfy1tLjafsVd3HTEQ9at5jV0a47953NUjD7zRNA3MZCvhtVyqxIj73SeK7lp1Z5RUQSCQzR_gWECVNyVUO_zZDJtc5virVDE6r9KxvLdClj6NF2MYTQexuuDTbUEDicInQLkspANqkcsGAxEPF57ohmtvs7K0MAo_ygqbTFgZhPzTHOkmuLVVq5BdQh_HDPO3BCcdf_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54c4b3eb9.mp4?token=uIMAbIekj7jsWBnU2Nez3h2dqMxxO7rGbBKNN2-YdoxwCPxElDOD3JE2eZugtBBk8uHCpbSqJGzB3oAZd-HkkkVoO9mhdWu35s9SoLS097D97AYiBPX0Z-RYhUIX3qX0GB1orMWyNb-53anfy1tLjafsVd3HTEQ9at5jV0a47953NUjD7zRNA3MZCvhtVyqxIj73SeK7lp1Z5RUQSCQzR_gWECVNyVUO_zZDJtc5virVDE6r9KxvLdClj6NF2MYTQexuuDTbUEDicInQLkspANqkcsGAxEPF57ohmtvs7K0MAo_ygqbTFgZhPzTHOkmuLVVq5BdQh_HDPO3BCcdf_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ شب همدلی و ایستادگی گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445373" target="_blank">📅 22:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام بقائی به تیم ملی فوتبال
🔹
سخنگوی وزارت خارجه: آفرین به تیم ملی فوتبال ایران که یکدل و متحد، «هدف» را نشانه رفت و اجازه نداد فشارهای غیرانسانی نامتعارف او را از «دویدن» باز دارد.
🔹
در روزهایی که فشار، تنگ‌نظری، تبعیض و محدودیت، ادامه دادن را دشوارتر از همیشه کرده بود، تیم ملی فوتبال ایران نشان داد که پیروزی، غلبه بر تفکر تسلیم و ناامیدی است.
🔹
نه محدودیت‌ها بهانه شد، نه فشارها باعث  تسلیم. به دل خطر زدند، دویدند و تا آخرین لحظه امید و مهر را با اخلاق و رفتار ایرانی خود روی زمین سبز زنده نگه داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/445372" target="_blank">📅 22:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسلوونی: جنگ آمریکا و اسرائیل علیه ایران اشتباه بود
🔹
رئیس‌جمهور اسلوونی: باید گفت‌وگو درباره یک سیاست دفاعی مشترک اروپایی آغاز شود و وابستگی به آمریکا کاهش یابد.
🔹
جنگ میان آمریکا، اسرائیل و ایران یک اشتباه بود و فکر می‌کنم ترامپ این موضوع را فهمیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445371" target="_blank">📅 22:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
در ۱۲۰ شب حضور، مراغه ایستاده برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445370" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9arJN-w4dhMGGfDily05LiRhrahToUzab8FFrE5dTrH3fn9cBplgTyD4QUyMpBwLlzbdZgQQmcS28lJPhqYr3ADUBzIRekJjR1BXhfiJ6lPTolnDIU8WnALUEurrbpy1_UHY5gVYZw9EddQfni8DGnpNxX3qANL3tNv27tyPXi5YRaHKMiVrBGkUyjkh45asxPCvkPlgw56tluLZVmkdHko8THUMa74TwrbyuNcAAfZ1A72Fya89IRkkA5OUj9zCTq26CAdu0RKbi3kaQYJ4OaoAPfHR4GuYTY6MzkzjmkAJHHWKQTT8IhhCYEWHRW4n-2elw3AZSYfL0Afh51Rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاندار همدان در دیدار با مدیرعامل بانک شهر:
🔻
توسعه همکاری با بانک شهر، شتاب‌دهنده رونق تولید در استان است
🔸
استاندار همدان با اشاره به ظرفیت‌های گسترده این استان در حوزه‌های تولید، کشاورزی، گردشگری و صنعت، بر ضرورت گسترش همکاری‌های بانک شهر با بخش‌های اقتصادی تأکید کرد و خواستار توسعه خدمات بانکی، ایجاد خط اعتباری ویژه و افزایش حمایت‌های مالی از واحدهای تولیدی شد.
🔸
به گزارش روابط عمومی بانک شهر، حمید ملانوری شمسی در دیدار با دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر، با اشاره به نقش نظام بانکی در رونق تولید و توسعه اقتصادی، اظهار کرد: استان همدان با برخورداری از ظرفیت‌های قابل توجه در بخش‌های کشاورزی، صنعت، گردشگری و خدمات، برای بهره‌برداری حداکثری از این ظرفیت‌ها نیازمند پشتیبانی و تأمین مالی مؤثر است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445369" target="_blank">📅 22:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIUIlmk6Kh3S2HWdSKslZmz5WZe8zjVghjOMrAxsknBs0lKySZOieapGcDU15rHqOQtvJ05SQh_Ii59wxu1_qvKDz_Z0wBJXh85EihHxSjhFJ7loJvgf0FO2Eb5qf1ajRR4MyPJ7PzbVUogafQphPb2bbr7xJmGT5OeRRJ0rZeS8wiusg48VSxlPr7zcguXnvMNh0hGy1guvNUHoZfNvPa-x7bsxaadt_QMW1nRfs7cTOLWZNw-CnC5L8GBNg5AhHbxNhs4MzHB17uSdnjOdmMzXfbaMrhzn9WP2eMzb2h0iaPCV0iZIyE45f3g0FcL_P2UxQ_kvf7bWhRuUvNpqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فرصت‌های ویژه اُپارک تا ۱۸ تیر!
✨
با خرید آنلاین بلیت، ۹۰ هزار تومان هدیه خرید دریافت کن.
🎡
بعد هم گردونه شانس اُپارک رو بچرخون و شانس برنده شدن:
🎮
PS5
🏊‍♂️
اشتراک سالیانه اُپارک
🎁
کدهای هدیه خرید
رو داشته باش.
هم از هدیه خرید آنلاین استفاده کن، هم شانس بردن جایزه‌های ویژه رو از دست نده.
👇
همین حالا وارد سایت اُپارک شو</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/445368" target="_blank">📅 22:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/445367" target="_blank">📅 22:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445365">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d5000e52.mp4?token=HNpM69vIJTynnuFe7WxxSiQEsSLcV9CPA6TlLiNz47k9su28HobYU9U8oAtRmqaFhY38DX69zcGQyvjOJ79fU46yiPSkNxYMSlnDGz1gWqirL2_dADf3xXIevCzD4oA5zH4FSu0Vd4INb1Emu2Ge914z89WzuoXKi4D1tQ89iECv-xs9VJMSXi_6QCV8HDAXY7OpK149xFxP4_hnc8UDxvNTQ4NwNo7g3-D5pEoEoZEaezq3WxajvMvU5Tf64yrrWD73F7kmsdGpOkTfh7mP6VyLK9MqxxRnRiOw0JpdDM6gknr5vNkuisiIdUQXYTH1ZYiFQk8wFc3z2S1-hxEvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d5000e52.mp4?token=HNpM69vIJTynnuFe7WxxSiQEsSLcV9CPA6TlLiNz47k9su28HobYU9U8oAtRmqaFhY38DX69zcGQyvjOJ79fU46yiPSkNxYMSlnDGz1gWqirL2_dADf3xXIevCzD4oA5zH4FSu0Vd4INb1Emu2Ge914z89WzuoXKi4D1tQ89iECv-xs9VJMSXi_6QCV8HDAXY7OpK149xFxP4_hnc8UDxvNTQ4NwNo7g3-D5pEoEoZEaezq3WxajvMvU5Tf64yrrWD73F7kmsdGpOkTfh7mP6VyLK9MqxxRnRiOw0JpdDM6gknr5vNkuisiIdUQXYTH1ZYiFQk8wFc3z2S1-hxEvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمعات شبانهٔ مردم بجنورد ادامه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445365" target="_blank">📅 22:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445364">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL5Z42SKLjOzlXH1q5z-Rt-VFQXSe82H_zwYWsAFTk4ZpHBfTtOodwY4fDi-TJGvbF72N3UZuOwge3ix7O6U9Lu7f6dfzJPp1s6c_0gk80uB7-2l1pWXKewTQhpPSuqDwNei0kfyWCNEQO6NTSrqJJWQaaBpJZoBN7xJDJEYU4d6OF1_2mWQAGCDDMCwn7JMs_2MNQSaDaEubMwO67UxAy-SrICrswW45PVC899J0AO8nRO4MBh2Rzb4f_V33yl6pP-AADS0bgewk5DF9qxR5Bm1RsHFMC1P3aF3zrp93OziG5xwMO_j5BBD0RLQVQGr2r2kCpEOgv13Irl1T5jnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دفتر نخست‌وزیر عراق: برگزاری مراسم تشییع رهبر شهید ایران در عراق و عتبات، افتخاری تاریخی برای ملت عراق است
🔹
دولت و ملت عراق از هیچ کوششی برای برگزاری باشکوه مراسم دریغ نخواهند کرد.
🔹
آیت‌الله العظمی خامنه‌ای(ره) جایگاه رفیع و ممتازی داشتند و خدمات آن رهبر بزرگ برای امنیت و عزت عراق و جهان اسلام ماندگار است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445364" target="_blank">📅 21:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
سلام و ارادت. بانک ملی از روز ۲۴ خرداد تا به الان پول‌هایی که بابت فروش ماشین برام واریز کردن هنوز به حسابم واریز نشده. با توجه به اینکه بنده ماشین تحویل دادم و قرار بود پول واریز شود واقعا نمی‌دونم الان باید چیکار کنم. مگر می‌شود دو هفته پول ها معلوم نباشد کجا رفته؟ هرروز می‌گویند درست شده ولی فقط شما می‌تونید وارد سایت بشید نه پولی میاد نه پولی می‌تونی انتقال بدی.
🔹
کارمند قراردادی پایگاه سلامت برون‌سپار هستیم، حقوقمان ۳۲ میلیون تومان است ولی هزار بهانه می‌آورند و پیمانکار کم واریز می‌کند و برای بیمه هم ۱۰ میلیون تومان کمتر رد می‌کنند، اعتراض هم کردیم، جوابمون اینه که هرکسی ناراحت هست برود.
🔸
متاسفانه در شهرستان بوانات پیگیر مسکن ملی نیستند و به هر کجا مراجعه می‌کنیم می‌گویند به راه‌وشهرسازی مراجعه کنید، راه‌وشهرسازی هم می‌گوید به بنیاد مسکن مراجعه کنید.
🔹
از زمان افزایش قیمت بنزین هنوز سهمیه‌ای که قرار بود بر اساس پیمایش به رانندگان اسنپ پرداخت بشه اجرایی نشده، این سهمیه جوابگوی ما نیست لطفاً مفصل پیگیری کنید.
🔸
آموزش‌و‌پرورش تکلیف این مدارس غیرانتفاعی را در شرایط جنگی اعلام کنه چون با بدبختی هزینه می‌دیم اما آنلاین هستن.
🔹
من و همکارانم مربیان پیش دبستانی ضمیمه دولت هستیم که ۱۶ ساله داریم در دورترین نقاط در برف و بوران مشغول تدریس می‌کنیم. در جنگ و کرونا هم تدریس تعطیل نشد چرا وزیر آموزش‌وپرورش قول همکاری دادن اما الان انگارنه‌انگار! به خدا ما هم زحمت کشیدیم.
🔸
خوانسار تنها شهری‌ است که کمربندی ندارد و کامیون‌ها از داخل شهر رد می‌شن. لطفا پیگیری کنید.
🔹
وضعیت زائران در پایانهٔ مرزی مهران واقعا اسفبار هست اصلا اتوبوس تو پایانه نیست و هر کسی برای خودش یه قیمتی می‌ده لطفاً به داد مسافران و زائران برسید.
🔸
وضعیت اجاره‌بها در شیراز و استان فارس به یک «بحران» تبدیل شده است! ما مستأجران، زیر فشار قیمت‌های سرسام‌آور و بی‌ضابطه کمر خم کرده‌ایم. متأسفانه جولان بنگاه‌های املاک و قیمت‌گذاری‌های سلیقه‌ای، آرامش را از خانواده‌ها گرفته و خطر آوارگی هزاران نفر را تهدید می‌کند.
🔹
بی‌زحمت از وزیر کشور یا رئیس ستاد انتخابات پیگیر زمان انتخابات شوراها باشید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445363" target="_blank">📅 21:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0SnDr4p9ZnZ3nD_9oKL34oTZl0zO7CL8ERGEnxz09Zq_5650VtrbRh5Nfnj9bE3KJSP5tjRNDvvdvjsDoZxzzKRj1VEM3ZiWG-kiyIqb6CIQaDRIft289tqAWiCpqtccMZIxDEq5G3bhXVZTGZo7lfC6Tn0PA3swZKJmh-OSbIqnacUJ_A5e-snq5SN4yGJRtnqLSAYPg-Y6MI2xZOt2JaT-a-yFIMKYgyU8s-8EdKRfT78yr3T0zEl9_ToMCW7HAerg5Fs3xzH8o6OOmXEQym-VrGjULgLurXqpr9qPDDfz6E6YNztkkb1BtmBTlVKYqj2BWCxGkadHiYubsd80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی یگان تخصصی در نبرد با آتش
🔹
آتش‌سوزی گستردهٔ منطقهٔ بدیل بهبهان از شامگاه جمعه در تنگهٔ بالنگستان آغاز شد و به‌دلیل گرمای هوا، پوشش گیاهی خشک و وزش باد تا نزدیکی روستای پشکر گسترش یافت.
🔹
این آتش‌سوزی پس از حدود یک روز مهار شد، اما جان‌باختن یکی از اهالی روستای قالند که داوطلبانه برای خاموش‌کردن آتش وارد میدان شده بود، بار دیگر نبود یگان تخصصی اطفای حریق طبیعت را پررنگ کرد.
🔹
سردار رستگار، فرماندهٔ یگان حفاظت محیط‌زیست می‌گوید: پیگیری تشکیل یگان حفاظت محیط‌زیست پس از دستور معاون اول رئیس‌جمهور وارد مرحلهٔ جدیدی شده است، اما هنوز به مرحله اجرا نرسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445362" target="_blank">📅 21:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445361">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUBMz1qUiWn7k49Bl2Y9cddz_KcyWeSe00bSW5ryRqL-8oX5yMw-QipQdBpIu-q7La8KVvy1qsKKbiWtfYc9GNuyNJ2BSyqBm_GHu7FHE2jyNMV7QRGfwB3-NOQx6yizUXmXH-NOcNpkjrp-uSMKOcTiJino_RovJgK008zY__HDMHfGAFpJgI61p5SnY7m33NKWDOP9o0vbC6NrhlH0gSQHGfAQUhbns36ljcAk_Q3fQeBFnYGnmvPZgiJSzp2aB2eMDYNb80-gyWExrvdvnt4CWjzOH8mnfHA9WAyV09ad5-0gsFOoRO1GY1mJZ6bhrgMDDaP0_FLK3P5Y2mOGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با نخست‌وزیر عراق: همهٔ کشورهای منطقه باید از استفادهٔ طرف‌های متجاوز از قلمرو و امکاناتشان برای حمله به ایران جلوگیری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445361" target="_blank">📅 21:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445360">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df4abcf2c.mp4?token=M0DHepLNdkZVVaJfdZt5rx1WobWc3YF9pvdldfVAixvJuTu7LF4HO0cIcWuCx7yhm5va4Eq-0cT0bi865tpM6yS0CNWsJ3UPiL8qvHRv6Kv2lezi98p9hIwzQagyeYvBLrWar9Ogo_75xe55n9v3JlvNLtoTYS0DQZMLOkLKpg8bI1bKR7E2rSmyRiKUwKBu3AJ44Pc_Uk30fyDvVzFtI1wlp8fvHz7azx4qV5XqBbzPk-ZObMHW7FVwTKqd7GsceJAYD2OzlNPLBGyPfMUMVfOnbjplcUO1UbgtQQm2Qlyrz56s8RGIye9CiViz9xm3y8jMwL3hnlO_n5P1qTMKhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df4abcf2c.mp4?token=M0DHepLNdkZVVaJfdZt5rx1WobWc3YF9pvdldfVAixvJuTu7LF4HO0cIcWuCx7yhm5va4Eq-0cT0bi865tpM6yS0CNWsJ3UPiL8qvHRv6Kv2lezi98p9hIwzQagyeYvBLrWar9Ogo_75xe55n9v3JlvNLtoTYS0DQZMLOkLKpg8bI1bKR7E2rSmyRiKUwKBu3AJ44Pc_Uk30fyDvVzFtI1wlp8fvHz7azx4qV5XqBbzPk-ZObMHW7FVwTKqd7GsceJAYD2OzlNPLBGyPfMUMVfOnbjplcUO1UbgtQQm2Qlyrz56s8RGIye9CiViz9xm3y8jMwL3hnlO_n5P1qTMKhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کار: ۸۶ همت از حقوق بازنشستگان احقاق شد
🔹
میدری: با پیگیری قوه قضائیه، ۸۶ هزار میلیارد تومان از سرمایه صندوق بازنشستگی با رای قوه‌قضائیه به اموال این صندوق بازگشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445360" target="_blank">📅 21:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445359">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=BdNWkyS20yU8yqKyde6acnP8PL_gdEQ6kYEVTsGaDavZOhfdYF75X8F2fpLExFKpIbWmRwo772usuk042qNqJr-EfNlgHJJws0GUnM6-Orlke0NtlIa_bU7LUoLBVd5sDhCVos_0x3OXoqcSP0gZV3y_pv_6_rQzUAADAL2gr58DtviZ9zjFsvIh-vfOYPriGGlY6lMuQ-p4rx4_mNe4bA8cAZeTBU9kD5gl0jEte_lQKui4o_OoYlbn3oaaXcNKOgzhmGMQqnbZ0EqdTrCwZ38Zr0SRezkUmgI5XdObEkZyMrbeX3kLthwdqxk1B6P6UXxFZaw0MwZKhohqS2-R1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=BdNWkyS20yU8yqKyde6acnP8PL_gdEQ6kYEVTsGaDavZOhfdYF75X8F2fpLExFKpIbWmRwo772usuk042qNqJr-EfNlgHJJws0GUnM6-Orlke0NtlIa_bU7LUoLBVd5sDhCVos_0x3OXoqcSP0gZV3y_pv_6_rQzUAADAL2gr58DtviZ9zjFsvIh-vfOYPriGGlY6lMuQ-p4rx4_mNe4bA8cAZeTBU9kD5gl0jEte_lQKui4o_OoYlbn3oaaXcNKOgzhmGMQqnbZ0EqdTrCwZ38Zr0SRezkUmgI5XdObEkZyMrbeX3kLthwdqxk1B6P6UXxFZaw0MwZKhohqS2-R1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: جاده‌های تهران در روز تشییع رهبر شهید مسدود نمی‌شود
🔹
فقط به شکل مقطعی پیرامون محل برگزاری مراسم محدودیت‌هایی وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445359" target="_blank">📅 20:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f1a8e7cd.mp4?token=frHFhmTE7QdLYKZlX-UHTcvIC7RXBn6GMPhh2eLuHSZwgIkqXBCv2qvCy01S5uShweCQCBL4O0Fi0hIJ4PLtBO0OIm-OJ-KBe9KcH6aWHcKAHfMtF1VPx22R_6jTwu4m4pmitIReB7prpt04sLeEhs2kxAGSyT4-QeMr4e5vrUPAujQqK7wg9qmJ50rrLaovfRumFB1BHXXOuqSo7e9ZIP7hLvOdRFcdlKEovzPWfR_mENSHslF5_Wm9841zrT7BK3C27lwsWpvZXBwox5LhHlhsQ2XrCAWT6vXoWatjPG2j923Tv7BKqVh28BNZBCVoXH4x5C5n7J2s-DHzqP4RGjkn3Ne0-QVCTbK7cog4sqvVqA2U1nlYaWHEkyZdmLiy04RvnI-B_GX7l6iSNxNQI3fjb4yKiQOJ6NVBNYzZ71vr2a2xBbSPFgQyxs-dno7Inpy63ieDeKz30iAdbOkbvPjuCgKAEuqLZ4J_Rb9EMeTJFstbkHe8848CzMKhEbXgjlYVK9jBPQGObm9uhxLmJGh5WxsKQ9jzI2ZMv5AitbGNBQsIrEyppHeyv61oKau1CZ4UtNX1R_bFHdpiuhWZc09wP-EuDpPxLQAWZ8lXfrp0x0UUE7fjpyQUMvsL5jVvDavwynNca47EPsP7elsPfXWQbVe96Nb_vt0g_kcb4LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f1a8e7cd.mp4?token=frHFhmTE7QdLYKZlX-UHTcvIC7RXBn6GMPhh2eLuHSZwgIkqXBCv2qvCy01S5uShweCQCBL4O0Fi0hIJ4PLtBO0OIm-OJ-KBe9KcH6aWHcKAHfMtF1VPx22R_6jTwu4m4pmitIReB7prpt04sLeEhs2kxAGSyT4-QeMr4e5vrUPAujQqK7wg9qmJ50rrLaovfRumFB1BHXXOuqSo7e9ZIP7hLvOdRFcdlKEovzPWfR_mENSHslF5_Wm9841zrT7BK3C27lwsWpvZXBwox5LhHlhsQ2XrCAWT6vXoWatjPG2j923Tv7BKqVh28BNZBCVoXH4x5C5n7J2s-DHzqP4RGjkn3Ne0-QVCTbK7cog4sqvVqA2U1nlYaWHEkyZdmLiy04RvnI-B_GX7l6iSNxNQI3fjb4yKiQOJ6NVBNYzZ71vr2a2xBbSPFgQyxs-dno7Inpy63ieDeKz30iAdbOkbvPjuCgKAEuqLZ4J_Rb9EMeTJFstbkHe8848CzMKhEbXgjlYVK9jBPQGObm9uhxLmJGh5WxsKQ9jzI2ZMv5AitbGNBQsIrEyppHeyv61oKau1CZ4UtNX1R_bFHdpiuhWZc09wP-EuDpPxLQAWZ8lXfrp0x0UUE7fjpyQUMvsL5jVvDavwynNca47EPsP7elsPfXWQbVe96Nb_vt0g_kcb4LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما هم خیلی دوستتون داریم  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445358" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMHt2-3Uc1t6lHwCdJ98jza-sO_KIZOIme4xDd08-gzZ-gwNEf6tZpwMBn4xGk0jLRZ3pkQMQNcDBxcmIbGzYKeI87-d2yEi0dUQht74pw--rA9GD0LWXrTFv3ZYZq3fjHskMhHCF6LPda3vxNxiAb4yLZRy7wb_t_B9FJPpikKaF8pgmjAuL3PPDVjePT6jHnhj5q4gbY6ESRPa9gqgQeq-YBIlJWz0zDTv0oUaV0va0Xu38LyQJ3AxlV2tg4gQs8H3YeS2W6j5F9yyPUzkzPwR6l_8yRDMZPMWR9h3oNdez3I_6rewpO2EClL21ivpy7gMv3eann9itJsZsoEqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن‌کاری در تالاب میقان اراک متوقف شد
🔹
اداره حفاظت از محیط‌زیست استان مرکزی، دستور به توقف فعالیت شرکت‌های برداشت املاح معدنی در تالاب میقان را صادر کرد.
🔹
تالاب میقان اراک یکی از مهم‌ترین تالاب‌های ایران به‌شمار می‌رود که در کنترل ریزگردها تاثیر زیادی دارد و همچنین زیستگاه پرندگان مهاجر مانند فلامینوگو درنای خاکستری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445357" target="_blank">📅 20:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18ddfb9c4.mp4?token=PHykuGnnst5ln7NI4-ilhN-apqXM2htLsugO1d-_QB-JNtz1iXeWzH8nlicOV9MMFmXuafU89wKJBiai1mZe0fGsk8EUbyhqpaFegnuPpNDENA-WcaGUW3Gqg3AIVLcRqZXv-FUMm0RB3SHIW7NboP4oRrhTYuw5EdM71FUivkgTT9jlcJWVEttbBKKYrk0rzBlJSd6E0q1D_Sg9MuonbzxH7q-6vaV9DAgRe2v2zhzUu1NSXbodeOe0_3j84wNDPgcRULpSM4MSAq0YJ0DZ9mLHZQVuZoIkQwcgrKVk8rEV9i-BU1nxC7O8XW-Lw6NPxX0vVEGuYHvXEMArn0Bfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18ddfb9c4.mp4?token=PHykuGnnst5ln7NI4-ilhN-apqXM2htLsugO1d-_QB-JNtz1iXeWzH8nlicOV9MMFmXuafU89wKJBiai1mZe0fGsk8EUbyhqpaFegnuPpNDENA-WcaGUW3Gqg3AIVLcRqZXv-FUMm0RB3SHIW7NboP4oRrhTYuw5EdM71FUivkgTT9jlcJWVEttbBKKYrk0rzBlJSd6E0q1D_Sg9MuonbzxH7q-6vaV9DAgRe2v2zhzUu1NSXbodeOe0_3j84wNDPgcRULpSM4MSAq0YJ0DZ9mLHZQVuZoIkQwcgrKVk8rEV9i-BU1nxC7O8XW-Lw6NPxX0vVEGuYHvXEMArn0Bfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بخش‌های مختلف کشور باید همکاری کنند تا افشاگری‌ها در حوزه قضایی خروجی لازم را داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445356" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال: مذاکرات این هفته ایران و آمریکا لغو شد
🔹
رسانۀ آمریکایی وال‌استریت‌ژورنال به نقل از منابع آگاه خود نوشته دور جدید مذاکرات ایران و آمریکا که قرار بود این هفته در سوئیس برگزار شود، به دلیل درگیری‌های اخیر لغو شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445355" target="_blank">📅 20:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj41UAv6bNEqx1Uqv-A4vFBRmTn3f7Gl6dyWphrH2NfP9dOTVrQp6vqUU9NDBChDGrAK71DGL1hmMRaKHl0Txo8U81zpDEoQsohlIVrD0dJuoj7YcJesMVFKPmdIQlpiOvuRP2WUAtBvNKPdJO_oSTeYTxEEqFUY-cZnl9D2AOYXAoBdGp-MiEUFYH4IsiUPVYShv8jgnY21skUILPTowF2x9MvIhT3PE90jNw6IbUjg-hzGstNmJ7yl1QYnPICnThHqnXQs5nIYlV2PqBAgqY2hsKGpRjgoElUIdf0nMEqY-pzaejRdxLHY2Xoh0a3VsE7nk30BvgaCfZgoRihTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکاپوی انتخاباتی نتانیاهو با هراساندن ساکنان سرزمین‌های اشغالی
🔹
«بنیامین نتانیاهو» نخست‌وزیر اسرائیل روز یکشنبه در سخنانی با محوریت انتخابات پیش‌رو در سرزمین‌های اشغالی گفت که بقایای محور ایران همچنان وجود داشته و باید با آنها مقابله شود و چالش‌های امنیتی سنگینی پیش روی اسرائیل قرار دارد.
🔸
نتانیاهو در تلاش است تا با هراساندن ساکنان سرزمین‌های اشغالی، آنها را ترغیب کند تا در انتخابات آتی به ائتلاف راست افراطی به سرکردگی وی رأی دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445354" target="_blank">📅 20:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSZLyZ7c39UNllBJRDBMAeWXHFce4QoYvQvR-xHM3jt7LB7h1q8Y3sRiUg2osB6zVPDfyLqcHXytht7ALRPEc5cR3JWJXzuvPM_N5lsUuJIVBu_TPz0a5j3_KR96WVI-UBU97zD1pnRDO1G2f5eYDy_Wt3EeX2RrbP1AhaZRo42opnty9TJ_CIzyKsd8JFNoBJUKNDOghVcKA_oucskpss06xuPbCDBeb58iPpv69v61FnRgzo-SonOChiL-jhz-fibkvE8AgMBW8DZdiBDbvbf2vnapPaQgGxuVqHJwTi0Jcm0b_bxJc38ltGijcWP1Rwd-LYx3HsWKrp3UErgnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی گیرندگان وام هزار میلیاردی بانک پاسارگاد افشا شد
🔗
اسامی را
اینجا
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445352" target="_blank">📅 20:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsx8iT7W07gxf64rrNkoWgnhYfgKRP2igp6V7sowgtig9Ip8Z-UjRY3dhvqVMfretG6HlY1qeGQ96jXJo-SFIyqwLCsdMjw9OrVv3sEyPlG8g6sQ9Pi7vEZ0EeZ1eelEXJhko84Fye3O2Sk1KASFMyp6RibJtrYg9WV22j9c0AqsKiCl7yBzGEZJ2CT3AEq3aCp5NYIZmcSxNDUxYFT8ImDjPrA_Yy60RCFezzrWC7eQ09DbUM8UQSCkPUmShyatTn1fihEIPvhxiS8xO7NGYKO4km-e75DCe133owtamP3pm2w9epWv3UubQebPUma6kWzrn5Ba6EqeWPp4iQYZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVUYZhNfpFOFx94Tj5x97K8cYPGuMHwNcTQNbaNUT6XJTfql_QEYk9HEMfFcjIJgx9Z-wVeuHFVig-NOiQthny04lgWVJnvZJXV5Bs6RXZ0ThjNDYBxEHAuxHWcAx4yCcx4dxfR0FguezOb9hE9oUeJDwES0ce_ci8KkQXz3sjEx9s1TJS4bJheHZ8NZJJtN7EnNdCW48po2k8QFAmYi-VBEJPsv3QBd5Zi9U5iyFJtk9QEVR7m3S_9IP0S4FJhH0AaND4a6aRyzalLUYxSzgFq0xBswz1pDieZq7OOJpTCB_M6ofVbDvjahUEDaBpdYeVwQqoXtdSp9-y2w35KWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eslkqyq3XXLHjQsiycrML1Ke9oIwJbeYSdrDa_g7QxObPa7kHSqL77PBpsJHCPaLHraUZYe0sMQUbRFCCdWZ66IY7_bijDvumb-lJGNhmrAD8IgTaiwY-0RCXjfRvrhJy_xB7tozU2BuFSOKMgi0kIYPKY7nhs_8k9IfvEXqrzX2a5sY1cwN6ztf-fZPdhgXqE0crwZPPhbh0P35fG-c8_LFsfjJf6QKjudsYCdScnweqsVUeteV3U-Kl-HeRQX72GqaH9hIH15mhwS80DS8ZfxLog-qQiHk93g3PDMeozYy1cFSuysFQtsRH3gfRSuLS-7vXeVgkEfExDVXDRCRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGHkyO3jtWT3qTLSE7SmVHHfh1yiZF_iPKWm2N5eV6XYCxjHdSzw3b407BagWMEdgXdmbHjJldqcjyB5nZ04mARhAXX-r6l-4ACEJV4TIXY6f9WCi87K-lu_Z5CwH6FwuKT_AQkR2AOACxh4TYTEfG5-wU0GgESwAlJ7eL-7T9fGz6qAOK2PDF1pLBmYHrbz6a_sl79N5LI9cO7HKAAvnr5hh2TAEXIN0zfLvtk4e8c1E4qR9OMslgEP-T0rsuO2AKKeRn7P8Zj-uWxy92uFO-JkBn6FPPLdy29TWT3qsBUJV6YraRaDko9R2kGTGM1HmAjcuhpBvdnhYZ1IEmjvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo5m11vCN5MhwGTJ8E-8q1od6kbkHoQ3_INhbPVuhASWB9iicGCMetDN3yY8hXj9MJlvQztVbczGr6rqXqT84HNwz0LBXPyAuRL69GKgZleHWPY16jLWO42HOPnZNoGaTyBmNlWaaHWnWLF9qV408eYuxtVO27eokKQgY2lm3kiw9NwZwHysWnQ-DLeK_IgxQo2Z7qfQrqJllxpF--SJUwX2KxtO2CT_--WkohsULbBxSrelkhsTmcvuVwrpZWIaWSOBsZYX9PYWVskAc5AnhnZirFqsVqvA00JxKtqYQRG72ztPQozvVy1PoWsochHe5a7h9nAChOf6-m5QIiunMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t37XcCskXElK--Wrj-Ta6EJIt1uTbqIjRKCCcgIWc7rt36cWbMSQdS4JmGlIT_IovANcXPyAMkhliFnPQF4w9ESoDBbKfbIf-t6WBqRwSoWAb9q3QjGhXm4NtwWeyaixG3FyaH7vBfclZ2EjqruiCvjfYRHAQBPbBR3RNcvc0taNssj6LOCNtOcd4HsODw4ZtDyZAvBKZjUGtQcjVBJrhtTUwYvIsPzmyIJW9xuqyOGe5d4lmJsdVCUB72DTb0x9nIvA38UpjjRVG-1kKnbp94o6-mm5QJ70Z4vEFZChe3kz8GeAD0XLW9SKC-p52pGuSPRHnqXOCzsjWMNgOf54sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gwp-iDN-ylvduH4bOEk-QLSntOsmBgfEW1wO3iOSRzlPxCxE4Xt-c9CE3ugkgr0v2WFRFyJ-xjFvv6m6r2Sf4gux2kD4-oIk3eViwLgf-lh9h4IVFfsoI2xsWPzIz6rYkE1YmnhpwRMixn2rj6kGaOWQiT2IymX1__QitkJBpNhq54EzjAJMWjYZTekNt98oIZlyszUVaXrS4ZG027PbWILMErp_7XtSl5q9fEkMLYXBroo7i32y4SHAZgCzSOUzoE5wx2cD7cXnqJLJu8IhTNXgKrsglLYwiEHVI8taKe9CdzPtejn7W102enIaupkRwr-AW3geuTmIMopvq9cH_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روضهٔ ۴۰۰ ساله در خانهٔ شیخ‌الاسلام اصفهان
🔸
خانهٔ تاریخی شیخ الاسلام به عنوان یادگاری به‌جای مانده از دورهٔ معماری صفوی و قاجاری است.
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445345" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بستری رایگان کودکان زیر ۷ سال هنوز هم اجرا می شود
🔹
روابط‌ عمومی وزارت بهداشت: برخی در فضای مجازی مدعی شده‌اند که رایگان بودن بستری کودکان زیر ۷ سال لغو شده؛ این ادعا نادرست است.
🔹
مصوبهٔ رایگان بودن بستری کودکان زیر ۷ سال همچنان به قوت خود باقی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445344" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۸.pdf</div>
  <div class="tg-doc-extra">3.4 MB</div>
</div>
<a href="https://t.me/farsna/445341" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۷.pdf</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445341" target="_blank">📅 19:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkY-4Rf1zU8W-2Mc-fcJSNOlnRvyqHmyYSPZF4LQZ1W9H0eHdLIYV2076XKoMQMolL1MyOCvc2x9PZ0gIPvMCe5oYhzc9zemHKX9bJQ8-g_BO0J7Uf7SoejSwSU_3LodeBP_kPK_wK6zKMcZewiQU9jS-PqcJQm5Mh8juC25ytHLKFIPF8gAESGx3ohBKQTrGJ5I2J7c9CoTaTaAyYsK324Rx2lPhQBQ5GhvoqxlEBe2iHWttX3oVmYeL-by1OgTrAyLE8rgM7EVJnjDI0RjCAZq3K9dAipBTTBIkSH4G1AUFGu9GH50dioOUpImWNQO92MzoXKscm3BfwM8xfPjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کاروان ملی سوگ میناب» به راه می‌افتد
🔹
صالحی‌امیری، وزیر گردشگری با اعلام خبر راه‌اندازی «کاروان ملی سوگ میناب» گفته این کاروان با مشارکت گروه‌های هنری، به‌زودی راهی در شهرهای مختلف کشور راوی مظلومیت کودکان میناب خواهد بود.
🔹
همچنین تولید آثار تصویری و فیلم‌های کوتاه و نمایش آن‌ها در نمایندگی‌های ایران در کشورهای مختلف نیز در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445340" target="_blank">📅 19:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445339">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVTOZjjo5Kop1wzJkKtLvNelJiWmLegm2pKzOJNCW2wcw6OyavXr1O5AS1dqTVCsG-Y9fYa8z2rS9oDWYnC1Om2JH2pQO76w-Vg5G4TevXD12T8MH90rtX-VUEve7EP0yTLGRQ_TkDhfiG9ZC0aod7AenDyPmmGCMKwxgSqpjLrYt3zOnSgURwIWOotIa9hgGpsJ_h3KUyg6vV-7-POfNJOL4-FtgkUSLPE7YX3hV5ISpcKxzW9YSfdh3QpOBqBAWjgGKGGW0-ZW_WUCjI3zsftset-o8NFvE2yC-ByOkF4EZWpDplM5Hwn2XFYm2YV5NUniPPLVBifVq0DpUosIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توضیحی دربارۀ مطلب یکی از کاربران فارس
درپی انتشار تحلیلی از سوی یکی از کاربران «فارس تعاملی» مبنی بر لزوم ساخت بمب اتمی توسط ایران برای دفع شر آمریکا، و بازنشر این مطلب در رسانه‌های خارجی، به اطلاع مخاطبان گرامی می‌رسد:
🔸
«فارس تعاملی» یک بستر شبکۀ اجتماعی است که به‌طور موازی با خروجی رسمی خبرگزاری فارس فعالیت می‌کند. این فضا برای ارائه دیدگاه‌ها، تحلیل‌ها و پرسش‌های کاربران در نظر گرفته شده و هیچ‌گونه ارتباطی با محتوای خبری و تحلیلی تولیدشده توسط خبرگزاری ندارد.
🔸
همچنان که پیش از این نیز اعلام شده، معیار تشخیص اخبار رسمی و مورد تأیید خبرگزاری فارس، نشان نقره‌ای خبرنگار همراه با لوگوی اصلی این خبرگزاری در کنار مطلب است. بنابراین، هر مطلبی که فاقد این دو نشانه باشد، نظر کاربران محسوب می‌شود و لزوماً بیانگر موضع خبرگزاری نیست.
🔸
همۀ مخاطبان می‌توانند با عضویت در پلتفرم فارس مطالب و دیدگاه‌هایشان را منتشر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445339" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445338">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZQHCxQn7FU2ZVxH5deRtwWsLFsI18vdruZgSk-QQ62EMQ1yDVOkD7l1Za-yyqmJLiqIay5QxY3CIaytxUqKtetdy0tTOW-s4yBSgavodQs14xV9E9Hy98iDqrhXCoKgsmSXwGNb1e7EQVnQV9LjLdp4iXdJ0lG8KvvIMVJTA2Mejbzdve3C1w4NTMpRZAnGxQNIDMGJUMHVRwEvVs5jbOVsQ6cvrG4LZjxq0OyCnelSyoOmF-5WSPeMlToCpQIENsMBPLANbD3uqCVh4i4j9eGt-vAX4mkgfQhCdrSZxprnQMrXsr37cQ3wivnbzOWRw4GqXPdLnd0lK9eecJd3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: اظهارات اردوغان را به آمریکا منتقل می‌کنیم
🔹
اردوغان دیروز صهیونیسم را «ایدئولوژی نسل‌کش، اشغالگر و توسعه‌طلب» توصیف کرده و گفته بود مبارزه با آن، برای بقای ملت ترکیه ضروری است.
🔹
نتانیاهو در واکنش به او گفته: صحبت‌های اردوغان را جدی می‌گیریم. این تهدیدها را به اطلاع متحدان آمریکایی خود خواهیم رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445338" target="_blank">📅 19:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afdae49aa.mp4?token=QeDodquZMskvBVQyMbiiIvzyJ2Yw3gBtlNW5v2zSlUYZnoh-T-0jyyLQsra__67Ve0YmwAAgqO5pW4U68RNZceeH5dxNzBMBwa6wc-KZHT1Fgh7yrZJOraRU5ZACGzUypx1dfdWCNpZdAju_1R2aE879rc4rN8TQ1dEB7LauJbOOKB1T51TCXx6QtwhEeZwAx7OyAYfifd6v0RAcgdb-kNOlQRCpfOMrK78sl8vCHw_sw27NnfoVKFhEze-ssPzf1rttvzmx9hPjc2DenS8Yv4kcFwGiITZPrW_UPzGOV5Y5_UiPotJmmJg9vCwYDH6iLWzUBAQk92Da0Z1jskJhAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afdae49aa.mp4?token=QeDodquZMskvBVQyMbiiIvzyJ2Yw3gBtlNW5v2zSlUYZnoh-T-0jyyLQsra__67Ve0YmwAAgqO5pW4U68RNZceeH5dxNzBMBwa6wc-KZHT1Fgh7yrZJOraRU5ZACGzUypx1dfdWCNpZdAju_1R2aE879rc4rN8TQ1dEB7LauJbOOKB1T51TCXx6QtwhEeZwAx7OyAYfifd6v0RAcgdb-kNOlQRCpfOMrK78sl8vCHw_sw27NnfoVKFhEze-ssPzf1rttvzmx9hPjc2DenS8Yv4kcFwGiITZPrW_UPzGOV5Y5_UiPotJmmJg9vCwYDH6iLWzUBAQk92Da0Z1jskJhAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده هتل «پلازا» در اربیل عراق
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445335" target="_blank">📅 19:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meeF21PmviRfwUUvs6kfILZgQPcbqH-hFiRoyBw2bXIsqMqtIUHIWhKEGxuhCdfjGdm4tW5R9fflnWnPYhgZF3GJ-7zVtk5xrp9zGiX-qjpsJh3F_k8X5udCJaJMWC1ERLs7R9ARHyn5bDfj6SYd18AsWLHfjlaZFpUmCy4XA0iBxGVJPa4e3V-MHBH6XlvJbLbgcewI2wgE4MYGgnUuM2epbAAV0NjUeKJV-Kg9EijuYC9pAnQzPZ2raDHo9GAmQJhafH3894wGH2yMvNWa-F7afaWPUeJieGfeYt03G0bp4MlIa_Dx76bMQDgpr676IECUbJFX8CK51BbRnBehCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایست پلیس به ۴ هزار شوتی
🔹
رئیس پلیس امنیت اقتصادی: در ۲ ماه اول امسال نزدیک به ۴ هزار خودروی شوتی توقیف شده است.
🔹
در سال ۱۴۰۴، تصادفات مرتبط با خودروهای شوتی ۳۵۸ کشته و ۵۱۳ مصدوم برجا گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445334" target="_blank">📅 18:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1635c434b8.mp4?token=P9fzbba8u2qc4fDvvjM9HxheZxPLpYjDBlTCfhWSqzt4qI-n2_snV-rUiaYiP0V3agshLYqwww-IqlICMZe37ygJraCh4Wpx5o6mBMGiKM7G0Vsw_9SWUrP_GIdQqbau2kYRaSj1AOjhUKyxBVVpTtg-RvW4GuBh-jlHrMcgaXYkmgNq3ZE1OMwOUk89y1CHtmHVfKlzhNNhNJP94aFfU8xuZDYPXbMh6qicx3N8U1mYASZ9NvBZ3gWZMgSaqhU6G3YJuSsXPhTjMuWveQIyuzi2Whgf0WeVAqlj9W0eF3SiSflnTQbyy88rErlDkSz_S2J02NkX7xjarcqpat4p1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1635c434b8.mp4?token=P9fzbba8u2qc4fDvvjM9HxheZxPLpYjDBlTCfhWSqzt4qI-n2_snV-rUiaYiP0V3agshLYqwww-IqlICMZe37ygJraCh4Wpx5o6mBMGiKM7G0Vsw_9SWUrP_GIdQqbau2kYRaSj1AOjhUKyxBVVpTtg-RvW4GuBh-jlHrMcgaXYkmgNq3ZE1OMwOUk89y1CHtmHVfKlzhNNhNJP94aFfU8xuZDYPXbMh6qicx3N8U1mYASZ9NvBZ3gWZMgSaqhU6G3YJuSsXPhTjMuWveQIyuzi2Whgf0WeVAqlj9W0eF3SiSflnTQbyy88rErlDkSz_S2J02NkX7xjarcqpat4p1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: پیکر رهبر شهید انقلاب در پایتخت و ۳ شهر زیارتی عراق تشییع می‌شود
🔹
با تدبیر و همکاری دولت عراق مقرر شد که تشییع پیکر رهبر شهید انقلاب در این کشور صورت بگیرد.
🔹
نخست‌وزیر عراق ستادی را برای همین هدف تشکیل داد که امروز جلسات مشترکی را برای انجام آخرین هماهنگی‌ها با این ستاد برگزار خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445332" target="_blank">📅 18:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ربات اسکان زائران تشییع رهبر انقلاب راه‌اندازی شد
🔹
در آستانه برگزاری مراسم تشییع رهبر انقلاب، ربات ثبت‌نام اسکان زائران با هدف تسهیل خدمات‌رسانی آغاز به کار کرد.
🔹
این سامانه در ۲ بخش فعالیت می‌کند؛ در بخش نخست، زائران غیرتهرانی می‌توانند درخواست اسکان خود را اعلام کنند.
🔹
در بخش دوم نیز شهروندان تهرانی که آمادگی میزبانی از زائران را دارند، می‌توانند اطلاعات محل اقامت و ظرفیت پذیرش خود را ثبت کنند.
🔹
برای دسترسی به این ربات در
ایتا
،
بله
،
سروش پلاس
و
روبیکا
روی نام پیام‌رسان کلیک کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445331" target="_blank">📅 18:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7YnvWQuYBwk9ItzVJtjcWmsdgz3TWORLUa_Ek3L4yAFh3vXFCUFsa4BrhvIuCMSwE_gyWQXfShvGcYxZNp2MTKIxDWjUAMKxxTr9LeB5uBRE-VmMd7JlrmOg_WZbE1kMiunmaQdD1RxBlyAZ1eeJwJqY5RFQAbNjX7QXF12HKab4bcWUN6bVVV_3C2ibY9hTTEBZLj0pSFo2EZbzUiKXP4i6msK_ng8PGgNXnyzFPahfi1Y7x9BjqM2wnIyYHYw6B4r5USqq9ogjyW-pNYfdSx0slFlvlDtNb2X8Q2PveiqhojnegxidHdXNSW1ePqgQZ8zxiopMCzGdVGBsxVeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج تیم ملی والیبال ایران در هفته دوم لیگ ملت‌های والیبال ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445330" target="_blank">📅 18:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
لحظهٔ شلیک موشک‌های سپاه در پاسخ به تجاوزهای آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445329" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e027d9d098.mp4?token=lT0J-K5d_LykZwmdb5t_Sk1Xz782VfN2gFXNOSdeKymli1SrIkCtWZQydwsao2LhWXDku-0_Ix7UFOjRxTnwPwYDXdXt55Tedazv3nNMu_9L05LLFOrB7_eFBU25NuZU_IwdWXAdIptPqCiU5Hshl9McL6fP1B6-WisJy3X72en1OaZ7SiNVSQ1teFJSyLL950QyPPRa3hnGabznmpuDStHjS3y5HdAQhGG7NTLl-a4HPIDeqN2N36bimO9xa2PL-L_S-28B0MX_KHEQ3CFwGqFDY5S-KSAghMhPN8TlmTCFCdlFeRHiTX6wS89gbB0uDMPKgBT4cP-UvpnBmkxOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e027d9d098.mp4?token=lT0J-K5d_LykZwmdb5t_Sk1Xz782VfN2gFXNOSdeKymli1SrIkCtWZQydwsao2LhWXDku-0_Ix7UFOjRxTnwPwYDXdXt55Tedazv3nNMu_9L05LLFOrB7_eFBU25NuZU_IwdWXAdIptPqCiU5Hshl9McL6fP1B6-WisJy3X72en1OaZ7SiNVSQ1teFJSyLL950QyPPRa3hnGabznmpuDStHjS3y5HdAQhGG7NTLl-a4HPIDeqN2N36bimO9xa2PL-L_S-28B0MX_KHEQ3CFwGqFDY5S-KSAghMhPN8TlmTCFCdlFeRHiTX6wS89gbB0uDMPKgBT4cP-UvpnBmkxOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران از سد کوبا گذشت
🏐
ایران ۳ - ۱ کوبا
🇨🇺
۲۲| ۲۱| ۲۵|۲۸
🇮🇷
۲۵|۲۵|۲۰|۳۰
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445328" target="_blank">📅 17:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIP9wtV5IzAGRx08owtqQsSdcwhbRQmYt4QNl4yQC8gBsv3bPcOaMVzvNapQV8I9hULcTBJGUs-2t77tY7ubgAXhXjWgeWnlP8JmkBC1qStOeeu1_c2x3LimYRNKXxfn4zPpM5bhpXvJ4TwCxde1ztqFLnhcLWqifbWhtRvzKcinFRjvkA1Prxd2r1XZCbDmbT7nnwfJD55pfZ8OxTjLyDLUjc0Dyl4-E5FQn58772FS9B9gdUjITrJe6euhW9EtA3hqqo0VY6pjKw3PfU4LhXG7t1ElUvo2eHH-nS3DI5JI8-eIyqV6F-TbvQVD-7-us9guyuhJhuCHaRvZEPFO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: با جدیت پیگیر خاتمۀ جنگ در لبنان هستیم
🔹
رئیس‌مجلس در تماس تلفنی با همتای لبنانی: در گفت‌وگوهای هفتۀ گذشته در سوئیس یکی از مهم‌ترین موضوعات بحث پایان جنگ در لبنان و حاکمیت و تمامیت ارضی این کشور بود.
🔹
این مسئله جزء مهمی از بند اول تفاهم‌نامۀ اسلام‌آباد بین ایران و آمریکاست که در گفت‌وگوهای سوئیس، پس از اشارۀ جدی هیئت مذاکره‌کنندۀ ایران به موارد نقض این ماده، مقرر شد یک واحد کنترل منازعه بین ایران، آمریکا و لبنان تشکیل شود و این واحد روند اجرای این ماده در لبنان را پیگیری کند.
🔹
هدف ما خاتمۀ جنگ در لبنان، بازگشت آوارگان به خانه و کاشانۀ خود و رفع اشغالگری و خروج رژیم صهیونیستی از سرزمین لبنان است و با جدیت پیگیر این موضوع هستیم.
🔹
رئیس‌مجلس لبنان: آنچه شما در سوئیس پیگیری کردید در جهت منافع مردم لبنان است، اما دشمن صهیونیستی تلاش می‌کند موضوع اعادۀ حاکمیت و تمامیت ارضی لبنان در چارچوب تفاهم اسلام‌آباد را از طریق دیگری دور بزند.
🔹
تفاهم واشنگتن بین لبنان و رژیم صهیونیستی یک توطئه و فتنه است و امام علی(ع) می‌فرمایند فتنه بدتر از قتل است.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445327" target="_blank">📅 17:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2O0r52KEJ7-IYv-MDOPVDldUFZOddeEXyMnqT8PrrHBXRwlzQzj7LutRTyfKw-QkkyjUrhyM09BS7VHY2YjtTLsIYr7tGr6SyrN-YmRVVRQ-OODw-3s3IPPXLu7VREL_9k1K4t3ZqjMqmKEth4QT3aAYpvvp6VyxBdhikSQhHu3gGyYJ5u_r6Yd6ARaCz16qfdKgyCT4oF6E1L3aZ16lw0j8DJTzcBwQr3WfgozjymZX_mbzkRXm2xKnA9fLfPuURxy4j8mVrsim70RJ-I134LfDyinle2lmNbvcxKelcqx9t3lFAOfQyElWceab3jHzUQkcH31P_ncdiGTgF8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: حزب‌الله ستون خیمه و حافظ حقیقی موجودیت لبنان است
🔹
پس از سالها تجربه دیپلماسی میگویم :«آزادی بدون استقلال سیاسی،قفس طلایی است»؛حزب الله ستون خیمه و حافظ حقیقی موجودیت و استقلال لبنان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445325" target="_blank">📅 16:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11900a29b4.mp4?token=cDXebAG_HhvDdeuNKwKRRviRIEpLt93WaiIBZSyi5zHNxd9SrPNE6NwZgzp7N-p8xdL97GfDC0Sz0nVf21sDqMU5mTraWM57PX72ZREP_LeXXHP40WKbulYKZWwIjAXeD8zxsICvKci4LnX1X0lLyhbpw9WpU2O8kODTn5I00NRcrhG8QPVvKomRI2tGBaB_2TyqXt9NefV2PhAM5ACl_a1-rNe7_PknHULuQK1M1T23tMy29TQZ0YHdJsqFSnkZpNiCOeKbfxmQvru2KZ9Xd6oKV_uCCVUoo67wU_wSy9321LPKzidKMEEgG9CEouxVsoq60B_tYNb0DTehPs3OuwUyIGzOCBhJoL_G_LwmxK6SFqAnd-JbogyZi0q2uWUFir9GmIJeTa7BryiUqV0JGq902MTJlHSZGuwKM4fIMOpuOzuJoZaSln9wRsYrqUvv1Fzn8rv_Qk4UXlHHjEtd_nwmUu_kOolEZrq11jisx3Tb3BbfoR_uEL6-w1mElUVZVOymHKOPDllCbRZTvVj03gA46CpjomaAYBfZW7dn54oaGIhuksR8p_77LNme6tQC8EFVNU1rmzJl05VNcRQQXEaGWxo-_MkDnSmy7b46NcL7MYJ3owj49yvT-JKTBzI9qira4K4FtIBraEcLyCI66BRhVyrbE6JoEMdmweIxjz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11900a29b4.mp4?token=cDXebAG_HhvDdeuNKwKRRviRIEpLt93WaiIBZSyi5zHNxd9SrPNE6NwZgzp7N-p8xdL97GfDC0Sz0nVf21sDqMU5mTraWM57PX72ZREP_LeXXHP40WKbulYKZWwIjAXeD8zxsICvKci4LnX1X0lLyhbpw9WpU2O8kODTn5I00NRcrhG8QPVvKomRI2tGBaB_2TyqXt9NefV2PhAM5ACl_a1-rNe7_PknHULuQK1M1T23tMy29TQZ0YHdJsqFSnkZpNiCOeKbfxmQvru2KZ9Xd6oKV_uCCVUoo67wU_wSy9321LPKzidKMEEgG9CEouxVsoq60B_tYNb0DTehPs3OuwUyIGzOCBhJoL_G_LwmxK6SFqAnd-JbogyZi0q2uWUFir9GmIJeTa7BryiUqV0JGq902MTJlHSZGuwKM4fIMOpuOzuJoZaSln9wRsYrqUvv1Fzn8rv_Qk4UXlHHjEtd_nwmUu_kOolEZrq11jisx3Tb3BbfoR_uEL6-w1mElUVZVOymHKOPDllCbRZTvVj03gA46CpjomaAYBfZW7dn54oaGIhuksR8p_77LNme6tQC8EFVNU1rmzJl05VNcRQQXEaGWxo-_MkDnSmy7b46NcL7MYJ3owj49yvT-JKTBzI9qira4K4FtIBraEcLyCI66BRhVyrbE6JoEMdmweIxjz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولر را با این چند کار ساده سرویس کنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445324" target="_blank">📅 16:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubMFCGKlK_RcixnEPUEKIrj2Ic1wunT1ooGRnV1UBTmRG1d9jyyfT9bKpJzj52-iftYj5eKwxlyReYC_roKfXWkMmugAsjDcbmQBYG67t5wPigh0ADShBut3VklTdJdvyZrL2WvUrQw0j2L-pxK3iY6SK7BhZLXRyaww4xT8TvVnLLOjHwmugVyfkX0glQcZpp2t4flC4znUyrRmQmMgNyXjvqMKmGlPZTJbNNlm9n6y1d6iK6OWihCzWy8UHvZV8Pl9XJJh_IefPPagq_HinZKXhXXRNehYlkEdA4o-0kxLg0iVg6t24UjnNL20z3F8Bl3jlHX4OgEADe3eCkbQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با خانوادهٔ شهیدان خطیب و موسوی
🔹
رئیس‌جمهور در ادامهٔ برنامه‌های سفر خود به قم، با حضور در منزل خانواده‌های شهید حجت‌الاسلام خطیب، وزیر شهید اطلاعات دولت چهاردهم و شهید امیر موسوی، رئیس فقید ستادکل نیروهای مسلح، دیدار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/445323" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyzfQ8xMwhb47ATcR4pb8Nklt9cxwJT0yUvZ8F5BijXLDkEmyfP1ePqhWbqUIa7rmOBok0ZC1p1OUH-82SmlKYz_27Kr4_Yu1gmNfDtIqJTpenGVde_H75A_4_WH_dQcLZVqVh0qlMmmL86SLfgZTeiMl5m10AkMauAUlqkGr7wGeAJOcgl5Yac61MIraVQzhkh-JlxWYUWfJYBrHBl559Yhbc7XWC7itTvA8He0npAY51UutVskxXal9Zb_DQtrM8tAD50cOt0zEnQThCVhGBjRDiKlyd4729Cxte7WgvmaT4CKFb-laHsgb4KA5i2nnNlbVlG7KQsR9Z_n2w364Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط بالگرد در عربستان با ۱۴ کشته
🔹
براساس اعلام وزارت انرژی عربستان یک بالگرد متعلق به آرامکو در منطقهٔ رأس تنوره سقوط کرده و تمام ۱۴ سرنشین آن جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445322" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69df37528.mp4?token=L2SaAsJz2kzNSl6BXEWL78d9dUfcrxAobcvdfqh9hHvSbdNC5IXMPbSNwF-p_4Rvh2M9T2mpaQLwjhG-WqpTGympGl0TurkQkuBHx05BSIXZSQHKLg3MQ6dL0J7BFurtuuH9mJ1jqQcC0x9BkM5UC_5aMBJZrFmMNnV4XM73KCDY3X1K6Juc7wGX68JB0rvKfStg5O7N5_jDQtBxjEIbO6dJa04ZOTgTJplmhNqDxG3QmCdmFabjxDAlj53ATZEpdvJy3EPRD-tOBNLvL7IV3Jguj4EkYQaAmGHZojm0Z6fuUfEYipnCpKBC9pPfWgBT67uPeH7mlfbiezgineAKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69df37528.mp4?token=L2SaAsJz2kzNSl6BXEWL78d9dUfcrxAobcvdfqh9hHvSbdNC5IXMPbSNwF-p_4Rvh2M9T2mpaQLwjhG-WqpTGympGl0TurkQkuBHx05BSIXZSQHKLg3MQ6dL0J7BFurtuuH9mJ1jqQcC0x9BkM5UC_5aMBJZrFmMNnV4XM73KCDY3X1K6Juc7wGX68JB0rvKfStg5O7N5_jDQtBxjEIbO6dJa04ZOTgTJplmhNqDxG3QmCdmFabjxDAlj53ATZEpdvJy3EPRD-tOBNLvL7IV3Jguj4EkYQaAmGHZojm0Z6fuUfEYipnCpKBC9pPfWgBT67uPeH7mlfbiezgineAKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چطور از گرمازدگی در تجمعات جلوگیری کنیم؟
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445321" target="_blank">📅 15:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار بمب‌های عمل‌نکرده در محدودهٔ فرودگاه شیراز به‌مدت یک هفته
🔹
ارتش فارس: عملیات خنثی‌سازی بمب‌های عمل‌نکرده در محدودهٔ فرودگاه شیراز از امروز به‌مدت یک هفته اجرا می‌شود؛ احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445320" target="_blank">📅 15:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrHfFwRQQYrkxN1s5sXRpn9hJBz9e0K6Azw0YjLCZo6zxT0xYqF0-me2P-zphy_E3x3DTwOk_7Eji_jhul-3aeO3fCAqVnza1ko5SZ7j1SWrp-dHVyUOa19mVs0rjIr9ZGlwwDPc8QdMVCvcr_ukMoGhHk9dMqlE3FWnkXopcnnjUgLeFwuHyd1Lc38g4-Be9OQ31oMK7YUj5PeEA_g2RvVTbX53Y0dYKk5-Mga_gtNgMJyRqsCuqbNKsTlTCRKnYEtfvqKKt61mH65xmEFLkF9hg1paMk-jmNIWV-zUSjOVVADnnUFfuQNhsxqsRFyB2CILqjz5UGl_bGtnkrqhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش سامانه‌های دفاعی پیشرفتهٔ اسرائیلی به قطر و عربستان
🔹
بنا بر ادعای رسانه‌های صهیونیستی، شرکت‌های اسرائیلی «البیت سیستمز» و «صنایع هوافضای اسرائیل» (IAI) سامانه‌های دفاع موشکی و قطعات مورد نیاز جنگنده‌های پیشرفته به ارزش صدها میلیون شِکِل را به عربستان سعودی و قطر فروخته‌اند.
🔹
به گفتهٔ روزنامهٔ هاآرتص، اسرائیل با وجود نداشتن روابط دیپلماتیک رسمی با کشورهای قطر و عربستان، روابطی از جمله صادرات سامانه‌های پدافند موشکی و کلاه‌های رزمی برای جنگنده‌های پیشرفتهٔ اف‑۱۵ را در پشت پرده با دوحه و ریاض پیگیری می‌کند.
🔹
این روزنامه مدعی شده که قطر برای حفاظت از جان مقامات ارشد خود نیز به سامانه‌های شرکت‌های اسرائیلی از جمله سامانه‌های شرکت «البیت سیستمز» (Elbit Systems) مجهز شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445319" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f04c60bf.mp4?token=ozxIbzCmHw2pxTqNwl8MOVApbagmqInDre1RvUDqlvRB9jifn-y9hLvR6ZrK8fxsw7V4SZ-J-KPWS_UzFxfrl43t48eZvfHrAk7ipoeqqn2-ry-HhiJRT9W8hMmD9uPNFRlYS2dXhFfXzxlSVoOFO7vD-__eXE3vhgxCW-9oGcQF06NKAN0_faHivcopuPTw5AbWC9N1QLDWHlZThhex6rKjqZtUmGCCu65_bkbhJpTOJ74ZV_TpAzTmZezoIDMXOyho2HaHT0m5tNSsanQBXOnbc0NhzCNod1q8HqJV1ljBALHT0AqgoNlJGt0BDONrHCLgDL9A3pQ5KP2Ge9dNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f04c60bf.mp4?token=ozxIbzCmHw2pxTqNwl8MOVApbagmqInDre1RvUDqlvRB9jifn-y9hLvR6ZrK8fxsw7V4SZ-J-KPWS_UzFxfrl43t48eZvfHrAk7ipoeqqn2-ry-HhiJRT9W8hMmD9uPNFRlYS2dXhFfXzxlSVoOFO7vD-__eXE3vhgxCW-9oGcQF06NKAN0_faHivcopuPTw5AbWC9N1QLDWHlZThhex6rKjqZtUmGCCu65_bkbhJpTOJ74ZV_TpAzTmZezoIDMXOyho2HaHT0m5tNSsanQBXOnbc0NhzCNod1q8HqJV1ljBALHT0AqgoNlJGt0BDONrHCLgDL9A3pQ5KP2Ge9dNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گِل‌فشان‌ بندر تنگ کنارک سیستان‌وبلوچستان فوران کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445318" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXKwjihBdQUmMLcl96Sn1CfLZDjWmGJ_XGXLwbSn-XQjyF-7h82HqrpbITIxxLBuondnXeMpeg_mwuJMRlPpkxhySqvkXzLlIdF-gX1zwe7-3WInJkZUzdQby3D6ttUUTNQMVYz6h0kmpmGDINEJ_77G80F03JemNU5fPpnEh-euH2IwBIkxEeHJJi2Iw9hYyyxYCECLt2faCy1wAJQNdhazIq-CPDqZRUPLNXP9yCtSca3qfvFIUOA-Kvg03HqBRcWnBkTXrtqGWcYxff5nJ6JaY7wqjtqPqgp0fBk1r5WHR8pUMbLfyNL4uetXA61KZcqh1ZGuDgN7Ixf7fiBJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
🔹
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445317" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYuTNO1Z6GWNanHc79xueWcF6orpEKE9ckADqHGijHOyXoomwtc_fWlTxYWZOVtoRpcq_aiPJn781rt2uGEU5JAZIvn_K5OL3FnJcRo-rtYASM6lts4HBgM_0UYoiOVRHdMDSaOJjKCEAdNtOdIkmD9uorOaDd6W86kSFDuaMI0QSiqrxn1vIj0JjAoORgl-W99DElx035WhrPsliFFx21OrWmuhPCQJWDabz9p8O_BtuDMccMHrbIaBhyr5EJHEaF9BoUfxx6Jwqk1SBIjHjPtWpxXhnpCCEnMNpMx7gQruynivEjt-llZytBTMDzaxX3Li0DDp230A-w7wTm92HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌صورت رسمی آغاز شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445316" target="_blank">📅 14:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk5xRHms8gAncvdlZqHAFWVh_oIQUq_9C0p2EzL0R0w4jgw4ObvZ3sBRXf_8cKSQnv7z5Y7HNzA0svM-E7qfR2uEmIK0O8Z7Jz_pjJde1gbcUbN64vxr6XkAC0LZQek-x1nQyd0HiZutvCq_0-tTjFnOj1EweOWb-CEW69JoIvB86E6UEVziYgIB3eq-K9l5OlpHlWJ4c4jipTmwLPDa02OkFPeNzvYI1TLeizAXV9Kh4VGdhLxHiMLbeTyDy8zfiydkFb6rcyjqvSgEo4Y9IozcJmwzVRNXhZ9y25n9vnb765hKYz78ZM2Ovc7Fc1Fp2LjOcpHhbYgtQ9Y-s7-eHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5mM94JD7GcyheD9lfsKKpq0K_56YZiN0n4Yk5q1PKZpmQXqBnTHKPLwIrZJ0BhOo25sMF3brw2NhY9nY0Qh9Mn5n6KrLPhgLPQoRq1se35OUxOLCcmz-qgx2rDwTtTypMbKq-uguayNubVmgLShQV0XKk1J9ib5HVSvx7Iy_87Q3LjXogcXiEOOvJGtbDFp5EYtxcHMkWDoiCdM7tbtQ9PEGWe1EzaoQmNDhK00awAuIjFICxrXIWNdmdOolJCTcUeFhNmT0fLsoHx32TdffG9aC-diqyCE9IEdXXLCYHzzsbJFVv80t59kOblra4m1esOTINsURRYecEBLuSaGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5HH5nt7dASqYF3v5fGSimBVaOK5I6PwIDM3NlEI9Wtsg_jzV2orNbS_EeAWdCVFfrJYt0mOMw2rGzqm8SlLUYCljOhLEeH9HlciSVHJx79H-ee5fLIF3OlqhM3dWTrSoh3R-kJIbR5kc69KeY2crk9icA1rsL-n7wUN_BXM9S9zifVWvYzH4Vw17Ms0YeyfolkbHn1H9OIjOQVntANHq2XxYS-esGOnqTpMo3zjXj3UPPe8VcjlmgJdOMGW8Z3tOc9SB7R1kSXb2jwGerupKm4v7RhzSa94vNR1Fmit-4RIcCctLiq1u21zq4hxU1IMvMXWUut6J8fNQFOydahc8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقچی در بغداد با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445313" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445309">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQlfKdAO61ndZYkyxkgneVkZ569mXM3I6oRXVy3r9r9iIwxeKqHP4MOLGt33fjWlRFRe0XNTktzdGPbJtvXA98tqROs4Il-mprgeLHFtHZVUNjIaZ42xC7LILKaHoUQnfDuTCJQ2kziB6-5svfMLvHzFfE2yJWdTUhdoDXzHIq8eB4Gqq45ecMw70DoZKzzP0_XoSaLFezpvDPwa-7b8GeS8k-2lwQ4ejXy_TlKaZIr2kDtkRFf6DQgqvn8rJktVBVLT6xsacV6mDtDsxSjaSQ7bvPeKEy1KiLtudpNFnv5MlrvU02rTKOIqtDNsZ8xx5CJhBXS7tV-JcDHvfqd5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBvVA5CXAREeuo_ptXBhNLCsEhp3ypQT6cA7GLAx5e-_K9CRcShnn_5e-DqR7F9r5GkXTfT27pv1C9uu1UzxNiKKUTgBipues_IZfG2g8j5Dlc-oXY-XLCiTVXfnxkareobERqYgAzv0BtRda1i90wvSEOqc8J2QsojludzpCJNubM3RijdHx1xD5pYAV5dyRR_MiqMU3LOi66Ww2IVasOx2OGV-t-2gRjJEjdhzegex2q2gkYS7YcsYfsgcPhUwJ5nCXCKGtJOKr5hR764DLYBFFvv3UlSIeDx4u5o3288piqLjn4Px2Teo9n74ddYLpFpxTlzhiRS-p9xA9fVdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbqlZgUM6EZ2nEQjF8mbhToNRjeXhRr1_EFQs76HbtTWcX4HMHBM7BRHgfbl85JwxherCR3hmKppg26tr9I-LlO3gYGGHjKerMZKmMmenRVF2A3yP2ttNKAN5mTwQLheYf7SXx7BHg6n-sH4JhZ1GdhRoMY00jbTh5v-Q1Mcj0wpmPHkuXDryUfWTEYLL1ufm9ZA2ResDS_0PEQpG86XNKqUA0K2icja2-X6penpR3Ha8QjXPzgGGr89L-l1Up3Nh1eXyKWwspdUVLgMCuYKvVJKgDYC3jHSg3Ak7DJRT96ufh6O4KMwvTwGMFpyV_RH6pnukZhLqYgJEHpN32K0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLa9VyCnF8XOwsb_h3UbAKWRQilFvJq-7LxZoXsUhfw4lhw8GhzzcT9w85RYbwgFBVg1z4Re2-r1Ok7p43eyIE0F-BPUtNd4vMniCYPGPJJW3ET2tUwcHCZWxJwVwt03kJ3ly085qabQuoWftc1hKPxVFRMJ4Ma-2_DGCF73phKv2kCKJ1zJdpyfKZZU2isMhSD9_d131OKaHYW2BHJrs_vxtyR5itRgOxL1sMJq9ENNzfgYppLa6ARzCWXklBw-ddoVqxhmqaXJ06jfwfS6mYaBEPu_WbSkyyCEK5ImFT9nPfSjAnTlSgxysJS0RKlHy22QQPXB1OreaMTbLj2i5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی: از پیشنهاد وزیر خارجهٔ عراق برای تشکیل چهارچوب ۲+۶ برای تأمین امنیت خلیج فارس استقبال می‌کنیم
🔹
براساس بند یک تفاهم جنگ در لبنان باید تمام شود؛ مسئولیت حملات رژیم صهیونیستی و عقب‌نشینی از مناطق اشغال‌شدهٔ لبنان با آمریکاست.
🔹
امنیت خلیج فارس باید…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445309" target="_blank">📅 14:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445308">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7JBQGWhT4XmZVgTztsYf2cCx5oEChJRZbGVulHRDfIjKaafLZe23mUM6npJZZs1O59ucXrMjGcdx6cOe9_F3U7M_M145oThwMXx-PbCfDEu_I6lnKLcDX72nONVc9AZhwQGsEnHaSjcAv5S0-2N-Ufdqxczn-868Ak66trr-yv4yn05nFEHxoe3d_hh95FHIZCy_Nt_1bWKGcMyJAk5oenuoPOr-Pf5TF4HY0gU41zKy6EbGiT9AbA32q652KYofSH6i8wBKegUQokjfmB8nhFRaGRVQ866dNMMsvZRPcB7Jd9YtLT7CjnMrlc6lzJExLWSR9YIYHqZtDKd7R_v2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف تمام اموال ساعدی‌نیا در نوشهر
🔹
دادگستری نوشهر: اموال ساعدی‌نیا در نوشهر به‌دلیل اتهام حمایت از اغتشاشات و ارتباط با جریان‌های معاند، با حکم قضایی توقیف و برخی دارایی‌های او از جمله یک کافه در شهر پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445308" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445307">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445307" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeqIH2PEZDu4znEBhQmtdF5w-vZ6fUmt_x7qHDw_c5VcsBIlvZcDFl4xxdS7HLBGd43Xmb1CQoogElDx62mvHUbVqF5ZyEpej97X9-wDAc1_xfGp5xOxaeO3imYn7LhLNMx2vDYIPhIapMhOShh1LpOmrSs9mbCU9qNEYYdDWsIxvsOOpTQFqJ7Q7GN8HsqunjUJlgj2w0mnEsm78xvsi04QaIDizauwB_fJsZ8UJR_t0EMJadwdLmVPB7oE98Qk26kbT5bW5OoQnn9DO4u9p_eWd1u8yvBUxrGGphJ4amh6K43rlqFnUioAuS9NHt9CTA6mSWSXR5F95oaVkHi9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله مکارم‌شیرازی در دیدار پزشکیان: نزدیکی بیشتر دولت و رهبری باعث آرامش مردم می‌شود
🔹
هرگونه سستی موجب جسورترشدن دشمن می‌شود و هر اندازه اقتدار بیشتری از سوی مسئولان نشان داده شود، دشمنان ضعیف‌تر خواهند شد.
🔹
مردم با وجود دشواری‌های فراوان، ایستادگی کم‌نظیری…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445306" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445305">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: در قوّه‌ٔقضائیه باید اجرای عدالت به پایه‌ای برسد که هر مظلومی آن را مأمن خود بداند و به‌خصوص کسانی که به‌نوعی از قدرتی برخوردارند، جرأت تعدّی به حقوق دیگران را نداشته باشند و باب سفارش و توصیه در آن به‌طور کلّی مسدود شود و داشتن آشنا در بخش‌هایی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445305" target="_blank">📅 14:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445304">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: قوه‌قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخش‌های نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445304" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: قوه‌قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخش‌های نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445303" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ متن کامل پیام رهبر انقلاب به‌مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش  بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت اسلامی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445302" target="_blank">📅 14:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام رهبر انقلاب به‌مناسبت هفتهٔ قوه‌قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445301" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مرکز مدیریت حوزه‌های علمیه: در صورت نقض تفاهم باید به دشمن جواب دندان‌شکن دهیم
🔹
مرکز مدیریت حوزه‌های علمیه در بیانیه‌ای با اشاره به پیام رهبر معظم انقلاب دربارۀ یادداشت تفاهم رئیس‌جمهوران ایران و آمریکا، بر لزوم صیانت از حقوق ملت ایران، هوشیاری در برابر بدعهدی طرف مقابل و حمایت از تیم دیپلماسی در چارچوب تحقق کامل مفاد تفاهم تأکید کرد.
در بخشی از این بیانیه آمده است:
🔸
بر رئیس‌جمهور، اعضای شورای‌عالی امنیت ملی و مسئولان دیپلماسی کشور شرعاً، عقلاً و قانوناً لازم است در صورت هرگونه نقض عهد دشمن و عدم پایبندی به بندهای یادداشت تفاهم، به‌سرعت و قاطعانه از مذاکره خارج شده و پاسخ دندان‌شکنی در عرصه نظامی و دیپلماسی بدهند.
🔸
بر همۀ مردم بزرگ و مبعوث و انقلابی ایران لازم است ضمن حمایت از مسئولان در میدان دیپلماسی، تحقق بندهای یادداشت تفاهم را مطالبه و بر رفتار و گفتار مسئولان نظارت کنند.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445300" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام رهبر انقلاب به‌مناسبت هفتهٔ قوه‌قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445299" target="_blank">📅 13:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDR9DfjcKHXMkZ94M6wVSe_ZB5s3OBWy56x2E_xXpkmElo7tW5Lt4JB4V2rb3PQJi5ROYduqNVValsXpfRgGq9OWkY8Rx5AXtcIKtuYO2kYybCWaxlgThGR-Z8rQAq_laSxrHygIUGH-RCUZUkI_N2Dl1VrM3t0OXpi7etm6B7rXi-k9_LLIhP-HqEQWJNia36ktxoF1HPVaMiVoV_jsRx9NsxBi2on9ZYOnACPoNQpKSeMMOW1Zyjdvy8k8CIOlyDJ2Fxa8xnO7Ng-WOL1fBrLSTnjEOn1f2H8-PBgJB4cuJlu4JvZxwcrKzbkbfwyQgo8Z7SsL-JEPwveZBfkCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله نوری‌همدانی: رابطۀ مسئولان باید با رهبری رابطۀ امام و رهرو باشد
🔹
آیت‌الله نوری‌همدانی در دیدار با رئیس‌جمهور: معتقدم اخلاص و تدین جناب‌عالی می‌تواند در پیشبرد امور و خدمت به مردم نقش مؤثری داشته باشد و این ویژگی‌ها سرمایه ارزشمندی برای مسئولان در…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445298" target="_blank">📅 13:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979577ff6.mp4?token=Wl1B0bYL-n1TvyzqbDXTkp1HDtDW6I6PrOutdR-MWNzLa616HMRPbRdi2DkgO2aya5ScFnXyQRk6bW8Ud8WUHJob8mP4rSmkxAUP5KaAivtIlK6ieHlFuJrfCvWwXAE24pTWYehe7XP6ff1dZhzTrOkOuBU4zPL4WWAy9DEbUjnXdMysb8zeN-oZMERecX3qT7uw90Y-7U3mrcHzz64pQKepF9XeUhQLdUbxWSrWs1Lq1I-qQBXAuMenakCEiFn2d8RvHx3gvM7JHpl-L9mAgUoowqeLYkxr-_30PBbkgAketzUB3H5-BeTCrf-mgZeWYmD-tZEH0mImgzIidcPEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979577ff6.mp4?token=Wl1B0bYL-n1TvyzqbDXTkp1HDtDW6I6PrOutdR-MWNzLa616HMRPbRdi2DkgO2aya5ScFnXyQRk6bW8Ud8WUHJob8mP4rSmkxAUP5KaAivtIlK6ieHlFuJrfCvWwXAE24pTWYehe7XP6ff1dZhzTrOkOuBU4zPL4WWAy9DEbUjnXdMysb8zeN-oZMERecX3qT7uw90Y-7U3mrcHzz64pQKepF9XeUhQLdUbxWSrWs1Lq1I-qQBXAuMenakCEiFn2d8RvHx3gvM7JHpl-L9mAgUoowqeLYkxr-_30PBbkgAketzUB3H5-BeTCrf-mgZeWYmD-tZEH0mImgzIidcPEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع انفجار در تل آویو
🔹
منابع خبری گزارش دادند یک خودرو در منطقه «حولون» در تل آویو منفجر شده است.
🔹
منابع صهیونیستی اذعان کردند در این انفجار ، یک اسرائیلی به هلاکت رسیده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445297" target="_blank">📅 13:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7DmUQMcy2cD9gdGLvfbHKvHUkVDDXFkTPOPmvRamqt9hg5XiXJ0Riu4kahEDOzVQ-VeOZ40yiaaDKV-NuN4fTDxtiBsATpBCeAi4C-9Q4TQhtz-f1QlLPUGh6WLO4ZIGhXrjIY2cYKeGyHXIE9X8Log44bcVcQpnV8iuI_pHLxN9D7Tlvg-1zq9fSfg7Qmwe1-NhXK1ZSMHp3JvPxFW5diRUuMMirZ4xGG4FjNfHraO3nbILX4wo7E6eu0Kyc7Mg0BYsgiuAt5OT1pGGQeeg8sfP3J9xkQ3c8ttOTxx0moWHhH3V2baJNX9NzD0xwVQdF6lsOJu1Ez2zjkhnd2pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Psce35DB2czUDyhy5TIEt87RP1rlFWBRXoQJpJ3jYvLLw73QB9djrscfDLcKxA_80KR3pOYNrdcsNp42xkNrATU06_C4SwgQJdf1nwYc7_6Jm2OpcYU4RXuZihVhxGaMaYl_bNHjaTxjwQMqyrjBuiD1wMuBFe8eq-j1nUn1k9fOI2WqAYHvCNKqQQgbORlZivFp5QWwIMdHAO_OzfgNeekrL1qFLYhqxGVA7aG3AmUYMyF3X7cwWDRq8S-2i0jNQN2pG2f6dGXBaId_fGbWRF7aPO_JaRCzwNaQjgE-oWgDPbKDOnpKx7ZHVssuGLnu9ffmR0MgIt50B-u-Miag2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان به حرم حضرت معصومه(س) مشرف شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445295" target="_blank">📅 13:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFhOWGIlgm_KDFw1faV0PyZa2CTjA5zPhwMAStXhs7gjumay7cdpoe3wkpeUMZcorjhMUMW5Xs5_25AZLlj3bMEFjYaUSre22wEkQBlqKJ33yckMaSgRFTU3ZJZqzbZjw-sDDdB4b0Oj86DMGi2zJlyhuPpma-YqR42B2YdP-ScS5KE1Ue-rFsB_1XnVrz9kzzIzQdfTZDTLpve21L6KJtZfCPmJWMS7ObrsNfrNDjaPhQY50xuw8V3fCx4YXfjImZJNxYB7huOuWztsZkuFGNjOD64L3_gGW4QA21iE5IWL5mmbtxe5vCafk7a0eue26Iv4F9OdREb4aRPca4AeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تعامل دولت و قوه قضائیه زمینه‌ساز گشایش در حل مشکلات مردم است
🔹
پیام رئیس‌جمهور به‌مناسبت هفتۀ قوه‌قضائیه: امروز بیش از هر زمان دیگری، جامعۀ ما نیازمند گسترش عدالت، تحکیم اعتماد عمومی و تقویت سرمایه اجتماعی است.
🔹
دادرسی عادلانه، حفظ حقوق شهروندان، مبارزه با فساد، دفاع از حقوق عامه، کاربست رأفت اسلامی و صیانت از آزادی‌های مشروع مردم، از مهم‌ترین پایه‌های حکمرانی مردمی و از مطالبات جدی ملت بزرگ ایران است.
🔹
در شرایطی که کشور برای عبور از چالش‌ها و دستیابی به افق‌های بلند توسعه، نیازمند درک مشترک، انسجام و همراهی در همه ارکان نظام است، تعامل سازنده و هم‌افزایی میان دولت و قوه قضائیه می‌تواند زمینه‌ساز گشایش‌های مؤثر در حل مشکلات مردم، تسهیل فعالیت‌های اقتصادی، حمایت از تولید و سرمایه‌گذاری، ارتقای امنیت حقوقی و بهبود فضای کسب‌‌وکار باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445294" target="_blank">📅 12:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b966a1d4.mp4?token=Ci15QksaPFGyl-x9xdBqArPiOwZmbOeWg7Ta53F81-KJNQRD0xjFXSMpiaMBtKzYdqjr52DtWA2SzXqGK2kcK4Jjn9B_FaU-oSd_EVKg8sVl9FQsnpe4HxzPRvpQSHQfYlBNk79PchcLKEcjpvLnPZLALs6KgV8NgQ_0aKX8XEG6-Z7DWii_CnY-tsVP_Sv7w6GRjgZetcqcb4aErxMpRryN5IPmmKY7PvF4BbJyYt-bB2qXN3pMs5qbYN6h96-NCnDHJ2HcKF_x-OBGqopnlSl7nUlYGx3s_gjl0zgGotx2eJyUoxfHHxY5mUqk90cfNDmuQ3fBi_O75VwaueER9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b966a1d4.mp4?token=Ci15QksaPFGyl-x9xdBqArPiOwZmbOeWg7Ta53F81-KJNQRD0xjFXSMpiaMBtKzYdqjr52DtWA2SzXqGK2kcK4Jjn9B_FaU-oSd_EVKg8sVl9FQsnpe4HxzPRvpQSHQfYlBNk79PchcLKEcjpvLnPZLALs6KgV8NgQ_0aKX8XEG6-Z7DWii_CnY-tsVP_Sv7w6GRjgZetcqcb4aErxMpRryN5IPmmKY7PvF4BbJyYt-bB2qXN3pMs5qbYN6h96-NCnDHJ2HcKF_x-OBGqopnlSl7nUlYGx3s_gjl0zgGotx2eJyUoxfHHxY5mUqk90cfNDmuQ3fBi_O75VwaueER9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در تنگهٔ هرمز دخالت نکنید و به یادداشت تفاهم پایبند باشید!
🔹
براساس یادداشت تفاهم، تنگهٔ هرمز تحت مدیریت ایران طی ۳۰ روز به ظرفیت قبل‌از جنگ برمی‌گردد؛ هیچ کشور یا نهاد دیگری دراین‌باره مسئولیتی ندارد و هر دخالت یا تلاش دیگری اوضاع را پیچیده می‌کند،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445293" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbSrso2h2lXvi3zQQ-rCXe8zAtWm1JfgYmOgE_w6rXIakQOVxpTOnizxDC2svN3V7anqYqemJpc9M65vPqdcl8OebKmVYdhYNwuq1hXzlIlo2Frs_Fmjg9sfXXSFB637GJUkRXSlg_yC12MSnmhoJI-OBxzJ5eifndp3ErRdZN0dy1OWKdtYufVYM6VxI6OuhM37CF0k6CRq8a5Z9kCn5H_FxyEe9jj4fsHtSMrf9YymkPAzqtTH4j8lBAT2hfTKthQzpD4HiPwrhvpSQzMO1_Rrs8dJJrFYymAid3RmLfTA1cnTG8WYYB6f3wqIfDWt-Mm5TpGUFXKMCElOtFFvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش ۲ درصدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۱ هزار واحدی به ۵ میلیون و ۷۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445292" target="_blank">📅 12:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce21f683d.mp4?token=M7B9ZDZo7Hmfb39-Qg3-wa_3z484WHxB3bSIyED9z0J3SMAFjrynjmf6Y3hnlwn8mKZjFx4SmAtCLfrkusFFmuWc-ruXzpIZz-RF844W6nRVGXoJMyHqFnL-9gZ-muB7fXzylSyE_Ro6Z0VmYl5XS_N-onL4MJbwFrvYJ71DN5lRll4RfsP2MZCbW12ue84RVQp0ihDkVNhD8qIo1_VcP77tLrdVkLjlTKs1fobThwwaEJ8aNzmEeePLWKNhFFxPFLRZav2NH251NXIBne5waL6ysH8G8-iQu-IdiPgGSCU67o9dSIkHSTvPEnmHm7m-voWVsW804DJUIJ6BVBPNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce21f683d.mp4?token=M7B9ZDZo7Hmfb39-Qg3-wa_3z484WHxB3bSIyED9z0J3SMAFjrynjmf6Y3hnlwn8mKZjFx4SmAtCLfrkusFFmuWc-ruXzpIZz-RF844W6nRVGXoJMyHqFnL-9gZ-muB7fXzylSyE_Ro6Z0VmYl5XS_N-onL4MJbwFrvYJ71DN5lRll4RfsP2MZCbW12ue84RVQp0ihDkVNhD8qIo1_VcP77tLrdVkLjlTKs1fobThwwaEJ8aNzmEeePLWKNhFFxPFLRZav2NH251NXIBne5waL6ysH8G8-iQu-IdiPgGSCU67o9dSIkHSTvPEnmHm7m-voWVsW804DJUIJ6BVBPNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هدف سوم من انجام هماهنگی‌های لازم برای تشییع پیکر رهبر شهید انقلاب در بغداد، کاظمین، کربلا و نجف است
🔹
با تدبیر و همکاری دولت عراق مقرر شد که تشییع پیکر رهبر شهید انقلاب در این کشور صورت بگیرد و نخست‌وزیر عراق ستادی را برای همین هدف تشکیل داد که…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445291" target="_blank">📅 12:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc39ece711.mp4?token=iBPnBbIqJ_Jidc2mrki4TMGAWJJpHBs5_76awAW55sMPIGZPdaxjgVTnvjUy6nCJ0Lg7LjM_qX9wUiG6LqlFfRh7WwJzLul14ml3i4ByNrvVcVFGuu-0CFasokcMyHFcu33oUyun3twBT_saLuuLEnGwZ9U1GmfpMM6Mv1lOEO9eI120_MxtB9Ku9pv7OjU8jIJq3uc8Doe__VqUrlij6gXqM_O6x5VTws9KbDa7c0QRYHO1hLexAsWtu3UyD3AM1PQzb8qYicBVmDoR0CoyTR8Hh8iRTOIaRH5g4hAC2btaGlK9YGE1xYEGVC1pOf-mKmHwR8LfNFrePcNttZPI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc39ece711.mp4?token=iBPnBbIqJ_Jidc2mrki4TMGAWJJpHBs5_76awAW55sMPIGZPdaxjgVTnvjUy6nCJ0Lg7LjM_qX9wUiG6LqlFfRh7WwJzLul14ml3i4ByNrvVcVFGuu-0CFasokcMyHFcu33oUyun3twBT_saLuuLEnGwZ9U1GmfpMM6Mv1lOEO9eI120_MxtB9Ku9pv7OjU8jIJq3uc8Doe__VqUrlij6gXqM_O6x5VTws9KbDa7c0QRYHO1hLexAsWtu3UyD3AM1PQzb8qYicBVmDoR0CoyTR8Hh8iRTOIaRH5g4hAC2btaGlK9YGE1xYEGVC1pOf-mKmHwR8LfNFrePcNttZPI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هدف اول سفر من تشکر از حمایت‌های دولت و مردم عراق در جنگ تحمیلی علیه ایران است
🔹
دولت عراق مواضع بسیار خوبی در محکومیت تجاوز و حمایت از مردم ایران گرفت. همچنین ما از مردم عراق حمایت‌ها و پشتیبانی‌های بسیار زیاد و دلگرم‌کننده‌ای را دیدیم.
🔹
هدف دوم…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445290" target="_blank">📅 12:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7306e07762.mp4?token=Yos1dfKB73WFg5o4jjutpryHizir4lhlKhinzEh_qcIwpg1JvdW496Ikv864mD6P3su7FIS_mArZ2YPny4O4BeSSzgoG0UcSbHv7DyXMEnkodpbPHm1DOXnwXIVMbl5r6n4g2a_5b4Lks75Ut3L0-NufL0PhJvLUggzt-jdM25Pxvbes1Q0O5o8N7_Q6rt-tEekoWH_cMA2-xXbiI79amqqfXKvRCBOE4n8nZ9e7ZNmgONWEFpG-vjTX5gdjbImDQb9RyDhyRP-cAKV_t5fjJAhoejez5xlcQBYHiKDvJdDYg_XM7m0Sfr0y8HiW5SAZdtjQudMhJiyP0p9wgOA1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7306e07762.mp4?token=Yos1dfKB73WFg5o4jjutpryHizir4lhlKhinzEh_qcIwpg1JvdW496Ikv864mD6P3su7FIS_mArZ2YPny4O4BeSSzgoG0UcSbHv7DyXMEnkodpbPHm1DOXnwXIVMbl5r6n4g2a_5b4Lks75Ut3L0-NufL0PhJvLUggzt-jdM25Pxvbes1Q0O5o8N7_Q6rt-tEekoWH_cMA2-xXbiI79amqqfXKvRCBOE4n8nZ9e7ZNmgONWEFpG-vjTX5gdjbImDQb9RyDhyRP-cAKV_t5fjJAhoejez5xlcQBYHiKDvJdDYg_XM7m0Sfr0y8HiW5SAZdtjQudMhJiyP0p9wgOA1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عراقچی در بغداد با همتای عراقی دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445289" target="_blank">📅 12:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ثبت‌نام خادمان مراسم وداع با رهبر شهید
🔹
شهرداری تهران با هدف تسهیل خدمت‌رسانی به شرکت‌کنندگان، راهنمایی و هدایت جمعیت، حفظ نظم عمومی و پشتیبانی از بخش‌های اجرایی مراسم تشییع پیکر رهبر شهید انقلاب، از علاقه‌مندان دعوت کرده تا در این حرکت به‌عنوان «خادمین امام شهید» مشارکت کنند.
🔹
علاقه‌مندان می‌توانند از طریق نرم‌افزار شهرزاد یا شماره‌گیری کد دستوری *۱۳۷*۳۳۳# در این حرکت شرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445288" target="_blank">📅 12:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445287">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIQ6V00znmqGUtF_J3yNjW_ClxJSKqYaqOu0bLPHg6d5HJ18hu8sGzq8ZWlqNgnCZ8t0l36VExmQa0ahCtCfKWAlMICtXmYp3P5pDK7RmvweDG1AQEW6mmyG_TIz0E9lz7PK7TN6zKsirMOhxTXNDg4TSkES0gpEBLitUdXP42Eg-BLWWzcxu_pi6_CHpuch5VOJjznUYbwcPKIK1X3A3baaruf6Xm60TC_RdQXxxuYWlR34p0sSp6Ndrobaz5V9WFVLipYeWL_bHqSiFfZE5WdOe8g_XxZmrB0Q8maE_kZKwOu0v5OhSZtXP9mnqmicovi9R6_PXPf_2IFx3nD_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا تفاهم را از چند جهت آتش زد؛ تکلیف ایران چیست؟
🔹
اقدامات اخیر آمریکا در حمله به ایران، موضوع لبنان و آزادسازی دارایی‌های مسدود شده، چندین بند از تفاهم اولیه را نقض کرد. تهران نیز در میدان، به اقدامات خصمانه آمریکا پاسخ داد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445287" target="_blank">📅 12:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حملهٔ جنگنده‌های اسرائیلی به جنوب لبنان
🔹
منابع خبری گزارش کردند که جنگنده‌های صهیونیستی لحظاتی پیش، شهرک «دیر سریان» را بمباران کردند. یدیعوت آحارونوت دربارهٔ این حملات گزارش کرد: مسئولان صهیونیست این ارزیابی‌ را دارند که آمریکا محدودیتی برای آزادی عمل نظامی اسرائیل در لبنان قائل نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445286" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445285">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bdd99163.mp4?token=XcKK3xdVCjEx-1zqcUN3KmxPJIbEBUTjcjqHtHQoBCaOlw5r87hYv07toPYOhTgUEYBOOBRQ1uFef_65y5TlhtdYPgKYmz_pAnMeYxDSgokqW1nBivOj2E8eUto7rBqzVyIiGaVFMBcyxYf7VMqgKA0hq02NGULIhwZWTKg4TBvHb9NXXUfQHZii6RGMchdJ5pUd_Nz0iKRE9nKxcpZb9t14NXdweTUpV9oKN3PRHVUfhFv6oZoTbJO9omaV87_h-bQ_f4ErUykMsG-oH3-YDv8EeDN75Spaf9Fkskelz9uQvWtJoukNkhcDcZuE0tN8nbAHqam77WRXB9FVrWrgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bdd99163.mp4?token=XcKK3xdVCjEx-1zqcUN3KmxPJIbEBUTjcjqHtHQoBCaOlw5r87hYv07toPYOhTgUEYBOOBRQ1uFef_65y5TlhtdYPgKYmz_pAnMeYxDSgokqW1nBivOj2E8eUto7rBqzVyIiGaVFMBcyxYf7VMqgKA0hq02NGULIhwZWTKg4TBvHb9NXXUfQHZii6RGMchdJ5pUd_Nz0iKRE9nKxcpZb9t14NXdweTUpV9oKN3PRHVUfhFv6oZoTbJO9omaV87_h-bQ_f4ErUykMsG-oH3-YDv8EeDN75Spaf9Fkskelz9uQvWtJoukNkhcDcZuE0tN8nbAHqam77WRXB9FVrWrgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
عملیات قاطع موشکی و پهپادی سپاه در پاسخ به تجاوزهای آمریکا
🔹
سپاه پاسداران: مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445285" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDTlXdNhVXMcRNxlt_1v1o-n9DfDsr2dyOLyB-15PRPFUAOAm66oQE4X3F4ShwUECsFGt0cyE0Y9NrBczDHj6UNjvxMCuNsPqGZgrOuUeJCvdgdrO8oT2fmuX0SrhqiJGTFexbO_gn9JckzsD7JQjlC9Dujni3p2djbRU6uYMx6H6ATFpiaCprkYkxQaF0d4-ETEB7wrnahxMwmY9MNnLb7husDKahNulYb54PVBKuwfJeIeqlISICH8HUrmqmdWQDPP9OVcZ_nwP5ZZI4h7775BQL4wQwKrWJS8pRoxbJgPADCPM_lMLJuALRF6tRz5xfRlk_mbdzph69yo9dp16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjoV86Y-WNm-0feY2VbjSW_wj82iBiaK1itF2HZFCcGFR4OLPmiPFh6Mlyt5hOAeVsfKUXHSXy6JXyzdUCopQfbR40v8QQZWbSck4YcoNGn7I0wb72gWNTD8wI5OTyLZYOdCVQik1PHDhv3QmTWxr1yeZuB7pba09EbXZg3bPV9COmD9k6LuPHA_jAInH3M_3VlY9oYYPBx72lIIu_Acp3l7Kc0nKuWJciK5iZaGst8AZPOM33LITSC1JyxhzsGqk167GQQubuENDvzDRTBiDaRIBHsxrT91D_jaPyF0xSfPbM9R3GKFrGKNC1bFMSISkV3lZGWZQiwDCvIug1LHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0oyAYgn4wNix8_Vipd9W_A3B-qzaDvHv6QtRy9ODi-tYMO0zu8S7gU4APfrXO827ATLhYOA_DwS9HblwtWgPvPsHs0SHnR8fC0dk3dpLC2VsWVnP31VQDBg6LYZ7dzA95PUXTyH3fHTvdpjUFJJcoDgAHI2voBwBK9OFz1eMEun1eeWQ0CvVq8QvQakiG2ASLTlAtwJh60zUxeGzr3b2WDqWE27PHu6oj6W3ciEjPOvw_32GLq42cyqisjE2rcOf7gGJ2uUWyxzVoCDri7ROAln8-_npXtLsRHmTpukY42uAyjZnAANfxLFJFpGIt60rfaD3_IsI5cOB_MX8PFMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw8vEzo1to-Y64XFB8U3p8hLb4aiEdVzvOq70-uls0Fly8TIBHZetqJMa_dco29Zv6lacRUJQ-8Sg7KMikvgTtU3eARsGrDKaSJsyEEvlVEyX_CpZcAp1kRe6p9FELrR4ew6j7m4BQh-YS9angczbfh33tB-O66cztHuTFAcZT9O5gUP1XgttxDV3n29XSioP1XeVe_WYtAZVon4Km1cMhGhAu8AAWQPwlSo3DioJ9rswPGqnFcpp8J2mL2yMZjaX0tOdAqYC3JG3dpB-MQlMwu-zeK3g3SGGC0_utW1WeCcXR3yAGaEPmHc4X0-b1fcFHUKYE_MgoWuUYskjW-AEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان به قم سفر کرد
🔹
رئیس‌جمهور به‌منظور زیارت حرم حضرت معصومه(س) و دیدار با مراجع عظام تقلید وارد شهر مقدس قم شد. @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/445281" target="_blank">📅 11:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82fd1339.mp4?token=hdJ7MkXh2l6pMpc54LhjOHssVAUkvPYGPFaVGa7QKKUUPYnov799Oq4RS5ir51MyaqJvByp14X-sULB6zqZj8LrSPtDz_FV-ldOy9uGkjBj_nMRPXfsD3BqO90T8WS-HxIyv0LaisV8hBPrp5nKsNcqr5Q49yHxs6NfnM5lY3H5Of5fup84DBlBre82B-Q_zR59xG43rFiVkXALU5FrPJpbO0N-83Q96_bGrlRHuo4fj7soGTFIIQOiP7XLu2fR1_9SWtyDKB9p5_61VRJgOYB7ZGCiVPY3vEHOb3e1WZVIyZXhUujQE2_JsXiSL5Hj2JyUzBNT1Csbb_84mREVIeXBaMmN_Mxl3gZsm3708tfUVWXaImY1Y0AZDM4hfBREh5fUKzJC6kvIiDerC0ZRKfirbCNZ2g8drb1HoJrmUTrOJxopaRMZxgy_ezgvxT73K-efPsD2Fe9wpyU4KeI7FyUnJXWOHencHMCZD-_0t79pBcBkWXaMnj1RUpQIVXrwsFUg7Tqebkepyi5SEVY2Jg_UHaK9dqro5oHPs5QfA7YxXyddQy1R3mivP27p1PWfuG8-GsjGA34MYnTUXtr1Kv2bY6K8kp1ZMAj88jUeJbnKiqXh2bvRY339SmGVxkBsRH1tT71n_cgBGZnKg5x644tpL4KphLg89xOmcbgUXd0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82fd1339.mp4?token=hdJ7MkXh2l6pMpc54LhjOHssVAUkvPYGPFaVGa7QKKUUPYnov799Oq4RS5ir51MyaqJvByp14X-sULB6zqZj8LrSPtDz_FV-ldOy9uGkjBj_nMRPXfsD3BqO90T8WS-HxIyv0LaisV8hBPrp5nKsNcqr5Q49yHxs6NfnM5lY3H5Of5fup84DBlBre82B-Q_zR59xG43rFiVkXALU5FrPJpbO0N-83Q96_bGrlRHuo4fj7soGTFIIQOiP7XLu2fR1_9SWtyDKB9p5_61VRJgOYB7ZGCiVPY3vEHOb3e1WZVIyZXhUujQE2_JsXiSL5Hj2JyUzBNT1Csbb_84mREVIeXBaMmN_Mxl3gZsm3708tfUVWXaImY1Y0AZDM4hfBREh5fUKzJC6kvIiDerC0ZRKfirbCNZ2g8drb1HoJrmUTrOJxopaRMZxgy_ezgvxT73K-efPsD2Fe9wpyU4KeI7FyUnJXWOHencHMCZD-_0t79pBcBkWXaMnj1RUpQIVXrwsFUg7Tqebkepyi5SEVY2Jg_UHaK9dqro5oHPs5QfA7YxXyddQy1R3mivP27p1PWfuG8-GsjGA34MYnTUXtr1Kv2bY6K8kp1ZMAj88jUeJbnKiqXh2bvRY339SmGVxkBsRH1tT71n_cgBGZnKg5x644tpL4KphLg89xOmcbgUXd0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این ویدیو را نمی‌توانید تا آخر ببینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445280" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be510b3fa.mp4?token=eydJuC3wieYwpYDdIxxOZAWd_2PfF5InN_3TIPq3pEFlYmKyOkPFG7oCEqrYl9mPOpDVD68B1wC38I60FBr7t0XYYLQwGCR2wf6_I4OjCNTIz7sScC_QX656jEu_NomB-7qUy0Xfx1l5d9no7Ovp-LmWLnSg_5oEiJFpnsI8RiBF5SDjAxEdIgEoNnw56noKr_-oEa-qLKNqBcOlHKS99q6Gjy6QvtX8as7I8ad2y0gdZEXOiCDHGBtbIcEqy0rp8wpwLFLOaIAqGIurCfFCGh4zK8eoyGILRFrFxw_7MrAg1dy3Q8aVFZ6fgAceGiX9GrHJAmcz7RhbaymTAiQidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be510b3fa.mp4?token=eydJuC3wieYwpYDdIxxOZAWd_2PfF5InN_3TIPq3pEFlYmKyOkPFG7oCEqrYl9mPOpDVD68B1wC38I60FBr7t0XYYLQwGCR2wf6_I4OjCNTIz7sScC_QX656jEu_NomB-7qUy0Xfx1l5d9no7Ovp-LmWLnSg_5oEiJFpnsI8RiBF5SDjAxEdIgEoNnw56noKr_-oEa-qLKNqBcOlHKS99q6Gjy6QvtX8as7I8ad2y0gdZEXOiCDHGBtbIcEqy0rp8wpwLFLOaIAqGIurCfFCGh4zK8eoyGILRFrFxw_7MrAg1dy3Q8aVFZ6fgAceGiX9GrHJAmcz7RhbaymTAiQidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات پهپادی روسیه در تلافی حملات اخیر اوکراین
🔹
به‌دنبال حملات پهپادی کی‌یف به تأسیسات انرژی و زیرساخت‌های مسکو، پهپادهای روسی مناطق مختلف اوکراین را هدف قرار دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445279" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445276">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj5AZ_z674RabYrb53TwXMZcqG6rCFpYQoLSeEA8M69wOsDMszw4Qea6eXI2dD_-0uTPrGljoTPomucT4UobNSLRYYqk6DYF_Z4jZo0BgAln3H7_plZT_0vQ89tze32AOPWr803khTCmyjlXZO0QqJMKbZo54qxQtnQtxTX6VBxyg6F-ERFBYl2u16UZYpYw-Szth-j_M9MznhVifcE3DCKI78gi2YV2plWDdSmNBzCDjnMLP-4R8uNwxYOQwcF1WaFwW7dNp81UN6P56TZqbTLiVlDCAWp0nskvjiRtO-CINtMhB9fI2GPREFKYYyLWJGrVr2AGgIMbo97EVI_EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRFeDLn935Z6CTAxtYH6Z5aeZ1mkOf07UjKbViQL3lOSPcCzZQfqxt-cZ-xQO_6h-41JZq0J3p0V8VMPhA82VIVi-tjoLB3OibG1Rf2kG5eGY5hPewsP3smzgMsQQz9Np9uK42t87oVuzh6M4jY6Cwy2jJP08N1osMHGV_BN6MOpGbXJ9OTp1Tkhd_9hT1Xn47e66O-rMeVA3iwBlyWmzDDfyEwvttKDVj_hUYdeGocwiLHsJMdzC9M6NmWAEmDzEBwRmohIoxZlYvyqWvALnOkMW0WUyq2PcML4azfvbqsJ3VK8NW9VjB-UGUTSChkNJP3wR_cn-4x_SvnVdPiMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPp4Bh-0myFtmEkb1_AFuzlHtYtoTe03ErXHDvs8BXFb37_cpHKj20IwA6EdZCDduiv8Dj1Gj8oPccxnkQfwb3jkVKeuDuIFDXlnKHBPXomYTq14J3gWwd0VNuZXRzXoQYllBjiypNv-DKeLlNS5lG-GKL3LYliYZMluqNeQUpr8gklKd1xN4y-nvTd4T30efOcfyZQ4r__1JQsUjuG8YvHZAp6LZNSyyVnrzHcI5ocRB3LeMECy5N4w_pGjaZ6yckc4cYJ-JxyWEOsqxdViOn4tP6iyBDD2c9M8CrWP1yd_bR20D48K7D7pgoKhu7A_FcqJqksglTy3dMCPBW5yfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی در محل شهادت شهید سلیمانی و ابومهدی المهندس به مقام این شهدا ادای احترام کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445276" target="_blank">📅 11:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445275">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc600a860.mp4?token=OTBTO_4MlQ16uky4-G03nefPc2NlZfBHDi5XqjEMX8pA09kqfqDkQX1dx1-6ZNNXy4QSLFnkxx2ou1RIoeyd2--lpDA-PGZ1_d-NUzd4jJgSHryE-5ohUgS5G4AwDyOknCL9qAWjaQhlKVWwDHeoYaHSmSVDC8599fiRsMWQ-lJq0LeMAUEOifgWY5cyh5wCCr8dbvm3e3UbpP0LXL97966PhgN3Cdbn9ySFjiD9P5QKUAU_kKcGz0GuYvI17A1H73uIDUrdFiIe_5N7TlIEGJ0X33GIg8mrTgZycSHoEJ0sSRbOY9_GL0iFYpgEVTcyJmIjkwXnWDHZNtFeYI7T9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc600a860.mp4?token=OTBTO_4MlQ16uky4-G03nefPc2NlZfBHDi5XqjEMX8pA09kqfqDkQX1dx1-6ZNNXy4QSLFnkxx2ou1RIoeyd2--lpDA-PGZ1_d-NUzd4jJgSHryE-5ohUgS5G4AwDyOknCL9qAWjaQhlKVWwDHeoYaHSmSVDC8599fiRsMWQ-lJq0LeMAUEOifgWY5cyh5wCCr8dbvm3e3UbpP0LXL97966PhgN3Cdbn9ySFjiD9P5QKUAU_kKcGz0GuYvI17A1H73uIDUrdFiIe_5N7TlIEGJ0X33GIg8mrTgZycSHoEJ0sSRbOY9_GL0iFYpgEVTcyJmIjkwXnWDHZNtFeYI7T9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از رهبر شهید در ارتش که برای اولین‌بار می‌بینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/445275" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445274">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121e2116ec.mp4?token=AGZ4PRVwBYfu2bOEdixwpiAYzjX40jqGsQolevWJS0GN4H6r000ejWMmDQSl1U-a-QRh9rnJo0AAqPXPln_7Plxx7tcfsUnRIWJSeQ79FkqvCReNzWPuiSReY_cf1YR9D-jiB5XgJON6_fYxS5pJ6yvi9a5LXedfOTU7vLBeFIwmnnzWianfaVwI3wDaQKpdDjvariIAYiWYfYz3d-VsEmtzT1uXWQ_lCtsoO3lccJ3DgPs0DIo8kyFfJX7yzS4M31m3cYtl1k7wthER5lgL5ScxmW9hCKh-pvRuBdu8CECmerQyggxozqO0uoeZPll4KK4kFy5Jn3XFhJeq8xHsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121e2116ec.mp4?token=AGZ4PRVwBYfu2bOEdixwpiAYzjX40jqGsQolevWJS0GN4H6r000ejWMmDQSl1U-a-QRh9rnJo0AAqPXPln_7Plxx7tcfsUnRIWJSeQ79FkqvCReNzWPuiSReY_cf1YR9D-jiB5XgJON6_fYxS5pJ6yvi9a5LXedfOTU7vLBeFIwmnnzWianfaVwI3wDaQKpdDjvariIAYiWYfYz3d-VsEmtzT1uXWQ_lCtsoO3lccJ3DgPs0DIo8kyFfJX7yzS4M31m3cYtl1k7wthER5lgL5ScxmW9hCKh-pvRuBdu8CECmerQyggxozqO0uoeZPll4KK4kFy5Jn3XFhJeq8xHsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابِ متفاوتِ احسان یاسین در شب‌های محرم ؛ خواننده ای که خادم عزاداران حضرت اباعبدالله(ع) شد
احسان یاسین تنها
خواننده سبک الهی - عرفانی کشور
با حضور در چایخانه هیئت عبدالله بن الحسن (ع) در قامت
خادمی عزاداران اهل بیت
به سوگواری پرداخت .
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445274" target="_blank">📅 10:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445273">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlCRdA9yJglYro-beWaRGQxMQDGUlicelsavbiVh1ypEcbxvxpjwtk_iItlKWvKx_BRE7KwzXF5_QjreYHknYQ3STdkgvTgNf6Bdp_uw7n6n77Wn3n1ayWUybii9ZL6VCy1qBmMZZiQJg5N5GVJFyGmumElJskoq0SeNLt-K0MqGwLTFILpGag2CDn_ZoYDTcb9wj-6wlpYzoeOfiQoVvRpJclTSJBGHjn1BKuJjd8uYa4_-RG71pklcBPY5Wm2ERpMorL4SPt2nKDRZBPok78_moXM3Zpe9GWgXYsWtkW-f2jN85w-exk0l7M6-mG-L59KVQoXnXSOFDSb7AR_9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445273" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445272" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303480ddde.mp4?token=UQmMBizFTB6-ZZ917OhO7XLx-DaV0mkypAVWmPSMwDmX-oDsqIZUPF9chcHq5zNTYZUm9He-8HEmrEr_t86Ov-vL2-LIxuITkdNXBk-PCdOMYIm-sMcVae5PZxp4N5HIknmPMwSxSIqBqnsO7xs7u_vb5PHy5Z2Du6KEQNYDJKw8qhd7UHlJGeGaJOb4jWZcL9zIwn1JIsl2uIML5MPrnmvyKYO4e49Gkd7H9INqmGlkSLCJKWvW6tNGkjiu_ZSH3OAbv0bGNQZW8uMAJNaVCTabjejnJgThleDkZa7fS1io-E3jxZmu0V9omQTRXpgM1PfOsrGFHpdg0GQSh7psbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303480ddde.mp4?token=UQmMBizFTB6-ZZ917OhO7XLx-DaV0mkypAVWmPSMwDmX-oDsqIZUPF9chcHq5zNTYZUm9He-8HEmrEr_t86Ov-vL2-LIxuITkdNXBk-PCdOMYIm-sMcVae5PZxp4N5HIknmPMwSxSIqBqnsO7xs7u_vb5PHy5Z2Du6KEQNYDJKw8qhd7UHlJGeGaJOb4jWZcL9zIwn1JIsl2uIML5MPrnmvyKYO4e49Gkd7H9INqmGlkSLCJKWvW6tNGkjiu_ZSH3OAbv0bGNQZW8uMAJNaVCTabjejnJgThleDkZa7fS1io-E3jxZmu0V9omQTRXpgM1PfOsrGFHpdg0GQSh7psbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
🔹
برای مثال، در روز‌های پایانی جنگ از پهپاد‌های جدیدی استفاده کردیم که مراحل تحقیقاتی‌شان از گذشته شروع شده بود و توانستیم آنها را در دل جنگ عملیاتی کنیم.
🔹
همچنین موشک‌های بهینه‌شده‌ای در سطح نیرو‌های…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445271" target="_blank">📅 10:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5397b19d2b.mp4?token=XaLXoB1ta9deJzN0d8_2HyMh6GYLoXvLF93lfvD1r9YjPJX_cnm8t_zJT88XlZtuwHKx50fDMbUCHzoun0HACnseSf4GeLFDr1UmHOtJWfyN85ORMqfYnzOOE8ALE9-v3ZJhSlIC6gkYit4dNnoiEBjrUDOamH-rzmmfbiayqfzTiw4YIPEnpLnMGQ1yFCZMyJ5kj0fk5cbyjeWnTWvZMkloj4qUviuEXXbKnnUuyO6GrF7-MvfBbBLaGUh3YCM1ljzCkXmfR6W3Ek9qHxhD_PPjWO0WwWtUpBMYtez8izJWnrnJ2o13FMTaOKbddDKBlkgXxGMezRkUJs0eYjRJP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5397b19d2b.mp4?token=XaLXoB1ta9deJzN0d8_2HyMh6GYLoXvLF93lfvD1r9YjPJX_cnm8t_zJT88XlZtuwHKx50fDMbUCHzoun0HACnseSf4GeLFDr1UmHOtJWfyN85ORMqfYnzOOE8ALE9-v3ZJhSlIC6gkYit4dNnoiEBjrUDOamH-rzmmfbiayqfzTiw4YIPEnpLnMGQ1yFCZMyJ5kj0fk5cbyjeWnTWvZMkloj4qUviuEXXbKnnUuyO6GrF7-MvfBbBLaGUh3YCM1ljzCkXmfR6W3Ek9qHxhD_PPjWO0WwWtUpBMYtez8izJWnrnJ2o13FMTaOKbddDKBlkgXxGMezRkUJs0eYjRJP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی راهی عراق شد
🔹
سیدعباس عراقچی وزیر خارجۀ کشورمان، صبح امروز برای انجام یک دیدار رسمی از عراق، عازم بغداد پایتخت این کشور شد.
🔹
عراقچی در این سفر با مقام‌های ارشد عراق دربارۀ مناسبات دوجانبه و تحولات منطقه‌ای و بین‌المللی رایزنی و تبادل نظر خواهد کرد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445270" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445269">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899d7b7908.mp4?token=YUPPGUSSenjPq6Lr8Qp_CnH9z8Q0bSf1cunfulnU0Hspklqx2Z_6Z4d7ewgYFP4t7N2x2NLf65btdFaA5PL4NndOScnTUXjX58uY9cpLHSQgrO8Cq2iqRf4P3YXMc7-V6-n3S9WuXqAjeS29sagLbPZHBe0xIuNlQxWn6SXHtZxJe41VklIDpUnyvwtrqeIyiKAFb64hVcYIn_4EJCjnPJwt8KucL8qoUqkyKr4FON9UKbnaWaEaBHMqV2FJJ4v-ibK7G9evvWpWFFHo2AOa3fur7wjJjf7rfMaQTAxz9j_0VzgL8uzqKHy5XEUyCAj4DCDxw-OwlmdfsxnJ27-Q1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899d7b7908.mp4?token=YUPPGUSSenjPq6Lr8Qp_CnH9z8Q0bSf1cunfulnU0Hspklqx2Z_6Z4d7ewgYFP4t7N2x2NLf65btdFaA5PL4NndOScnTUXjX58uY9cpLHSQgrO8Cq2iqRf4P3YXMc7-V6-n3S9WuXqAjeS29sagLbPZHBe0xIuNlQxWn6SXHtZxJe41VklIDpUnyvwtrqeIyiKAFb64hVcYIn_4EJCjnPJwt8KucL8qoUqkyKr4FON9UKbnaWaEaBHMqV2FJJ4v-ibK7G9evvWpWFFHo2AOa3fur7wjJjf7rfMaQTAxz9j_0VzgL8uzqKHy5XEUyCAj4DCDxw-OwlmdfsxnJ27-Q1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
🔹
برای مثال، در روز‌های پایانی جنگ از پهپاد‌های جدیدی استفاده کردیم که مراحل تحقیقاتی‌شان از گذشته شروع شده بود و توانستیم آنها را در دل جنگ عملیاتی کنیم.
🔹
همچنین موشک‌های بهینه‌شده‌ای در سطح نیرو‌های مسلح، هم ارتش و هم سپاه، با کیفیت بالاتر به‌کار گرفته شد.
🔹
این نشان می‌دهد که ما در عین حال که از تجهیزات موجود استفاده می‌کردیم، از حوزۀ تحقیق و توسعه نیز غافل نبودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/445269" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445268">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74179bfa7b.mp4?token=ENfh0PQqb_jMZRBzv5n25293Zu9JpQV4ZgwhtHp9XD1lxKIuydOf6iL3EANMhBVada09cNVssF23a4_iKuNhCMQePD7Acv8uMYuu9qfCWmDxBEtgN6Krp6SoDkpg_HxSDPpm5EBPKPZ-5sy4C6RWbFl6bjWGBqic5mns8InQ0_ibkr4aY12WHGKDd2eSrP_DbEocRCTjUjdVBeAYQ-djlhdeiPfvryVt4ovUDWxk8teYBegQNWIzdp-lF0gzTNuoMVphZEZabKmBcgT8ZsrUq-zJ5BuMnqLq1D17nEilRFrrqecGdyJcuZ-t4JO538wxoT-lsAAUd1ettRylQgQURw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74179bfa7b.mp4?token=ENfh0PQqb_jMZRBzv5n25293Zu9JpQV4ZgwhtHp9XD1lxKIuydOf6iL3EANMhBVada09cNVssF23a4_iKuNhCMQePD7Acv8uMYuu9qfCWmDxBEtgN6Krp6SoDkpg_HxSDPpm5EBPKPZ-5sy4C6RWbFl6bjWGBqic5mns8InQ0_ibkr4aY12WHGKDd2eSrP_DbEocRCTjUjdVBeAYQ-djlhdeiPfvryVt4ovUDWxk8teYBegQNWIzdp-lF0gzTNuoMVphZEZabKmBcgT8ZsrUq-zJ5BuMnqLq1D17nEilRFrrqecGdyJcuZ-t4JO538wxoT-lsAAUd1ettRylQgQURw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانهٔ صهیونیستی کان اعلام کرد به تصاویری دست یافته که لحظهٔ هدف‌قرارگرفتن نیروهای ارتش صهیونیستی در حملات حزب‌الله در «مارون‌الرأس» در تاریخ ۲۵ مارس ۲۰۲۶ را ثبت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445268" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
