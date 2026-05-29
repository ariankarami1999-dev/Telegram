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
<img src="https://cdn4.telesco.pe/file/Uvw97F-ziHL8j6qzVbl1Ow9kc_zD6959PREcpDVGDUxITFwM-o-RyyDm2b1K60DQaR10eJ2V_N8YMpfeAlDeMuxfvLuLXBy5_honBAq1x0LY19dUAPfuwVFd3AvqD6FsSKvDZOc9MKwk_Md9VAMeU8bRyIKj8WKj_pEUir2wL3L1g75U-zoiXpiKmsFxeGrILjgZ_b9sLC9kxSkW18ehsJxTxmav2dhzL6vTsN1LKaBrnwwosGDxeh4TAGlbRK4UUvIMrLlqGh55D9qMYDlX9lMe1azYb6YAQULwsj8pA6SVW7XDm-HXvEElThpXpQ0MjsEti14e452b6_VTyqTzqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-438537">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد
🔹
براساس هشدار هواشناسی، از بعدازظهر جمعه تا اواخر شنبه ۹ خرداد، وزش‌باد شدید، رگبار، رعدوبرق و کاهش قابل‌توجه دما آسمان مازندران را تحت تاثیر قرار می‌دهد.
🔹
به گفتۀ مدیرکل مدیریت بحران مازندران، اسکان و هرگونه فعالیت‌های تفریحی در بستر و حاشیۀ رودخانه‌ها و ارتفاعات این استان در این‌ بازه ممنوع می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/farsna/438537" target="_blank">📅 05:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438536">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اظهارات طوطی‌وار ترامپ درباره ایران
🔹
رئيس‌جمهور آمریکا دونالد ترامپ در مصاحبه با فاکس‌نیوز ادعاهای اثبات‌نشده‌ای را که بارها درباره ایران مطرح کرده دوباره بازگو کرد.
🔹
در حالی که دونالد ترامپ موفق نشده اهداف نظامی‌اش را در جنگ علیه ایران محقق کند او مدعی شده ایالات متحده ایران را از نظر نظامی شکست داده و به همین دلیل «همه برگ‌های برنده» در مذاکرات در دست آمریکاست.
🔹
او تأکید کرد که هر توافقی با ایران تنها در صورتی امضا خواهد شد که «معامله خوبی برای ایالات متحده» باشد و این «خط قرمز» واشنگتن است.
🔹
ترامپ همچنین بار دیگر مدعی شد که نیروی دریایی ایران به طور کامل ناپدید شده و نیروی هوایی ایران هم کاملاْ از بین رفته است.
🔹
وی همچنین گفت:  «اگر نه ماه پیش ایران را با بمب‌افکن‌های بی‌۲ بمباران نکرده بودیم، آنها اکنون صاحب سلاح هسته‌ای می‌شدند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/438536" target="_blank">📅 05:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438535">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ec776bf7.mp4?token=NQCz4G3HQjVEtiECpReF2MVJ82C8b-XwWeob6oisGQWB7tMhDLSuNwFOIXREhQHuPX9hkMsJXSnUbbi1-lx8wZ9EC40WLE-sANK9M5WfFw9e5pMFaY5uNdCVjnLNifiwDR8gs5NQuufwsPCq8uxhNJK5yOoEVAYYhnCG0r8vsOaglhwPZbcmAN1n0w9xGFr59mhqacbkHzoy73SWd69wN8_Vg2ZePi77eZr6Pr-KdzJGeHxUrQKkGJk2OhitPxsq-AjWQR4cbArCqYrmKMFqmxOUWcB7TGT84Wvl19G1LyW5Y-nQA0ygCbhUFkaL_2RlK1wBzBIALxvSCUnjhwWIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ec776bf7.mp4?token=NQCz4G3HQjVEtiECpReF2MVJ82C8b-XwWeob6oisGQWB7tMhDLSuNwFOIXREhQHuPX9hkMsJXSnUbbi1-lx8wZ9EC40WLE-sANK9M5WfFw9e5pMFaY5uNdCVjnLNifiwDR8gs5NQuufwsPCq8uxhNJK5yOoEVAYYhnCG0r8vsOaglhwPZbcmAN1n0w9xGFr59mhqacbkHzoy73SWd69wN8_Vg2ZePi77eZr6Pr-KdzJGeHxUrQKkGJk2OhitPxsq-AjWQR4cbArCqYrmKMFqmxOUWcB7TGT84Wvl19G1LyW5Y-nQA0ygCbhUFkaL_2RlK1wBzBIALxvSCUnjhwWIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌سازی قمی‌ها در شب هشتادونهم
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/438535" target="_blank">📅 04:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438534">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s18WrRaOzCsLgHyFPFk1p0ja2exGl0xriXde23jdtrmH_wYOZopuMzGUyqIwR-HqP9Jbw0p-z9m5EIx5_Oo5XS9OMEHR_Wb83FpuZhmhk4-i6pDbu5ctf-BFPPct5EW8NSQ79X_w5g_n4oOVZWifobPMnDFgj3b2-ZpYy5NWu-oirUHPOn-rvvGfvviNtNVE5ld0gkyuHRM38QUm_FjRkWcRn8TO-fy-HpgmWOvH3ebAC6iM1bk2jyUWDz99G0AQT3rbMIUdzKuOohbWeUc1JzkIy4m_zMRiY0U01F196hR7_tuHLj6N4oJzjbn2SbJh4CzKuGBoLIQ7djgl8ySc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاس بیش از ۳۵ نفر در مدارس ممنوع شد
🔹
با اعلام وزارت آموزش‌وپرورش، در سال تحصیلی جدید تشکیل کلاس بیش از ۳۵ نفر در تمامی دوره‌ها ممنوع اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/438534" target="_blank">📅 03:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438533">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808f313e66.mp4?token=bVu6udAB-V9WJYsPhblt8CgPsc1IA6GYII7ESVRJWuuEHZv-pTmzqoqXcY9-7v1wLMxcAqcsQaGv5_GbBFUp1RptjoI3crkQqFNGE3juz670aQC1v93ihyDhWMfkatHtP1UkNVFE4AacSKfYKkVypjMMFcAGtd96IY1RdZqnVmCtDkPMmQDjLJMLDd-s_xCb8aiGkIshxlSVwBv4pTTrfzVv63At2jGsaHyYEfvvCpwTtbAJDeuOYJ4slU4JDo7H6ctHP37FMUziM5tb-VpGBSFVcX4wGfFDFar2zwK9MPgNsd-Uvswkk2NbCKzYtMYdSF0312fqDvDxIxqtWpMAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808f313e66.mp4?token=bVu6udAB-V9WJYsPhblt8CgPsc1IA6GYII7ESVRJWuuEHZv-pTmzqoqXcY9-7v1wLMxcAqcsQaGv5_GbBFUp1RptjoI3crkQqFNGE3juz670aQC1v93ihyDhWMfkatHtP1UkNVFE4AacSKfYKkVypjMMFcAGtd96IY1RdZqnVmCtDkPMmQDjLJMLDd-s_xCb8aiGkIshxlSVwBv4pTTrfzVv63At2jGsaHyYEfvvCpwTtbAJDeuOYJ4slU4JDo7H6ctHP37FMUziM5tb-VpGBSFVcX4wGfFDFar2zwK9MPgNsd-Uvswkk2NbCKzYtMYdSF0312fqDvDxIxqtWpMAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستور نتانیاهو برای گسترش اشغالگری در غزه
🔹
انتشار ویدئویی از اظهارات نتانیاهو در شبکۀ ۱۲ تلویزیون اسرائیل از طرح جدید و گام‌به‌گام تل‌آویو برای گسترش اشغال نظامی نوار غزه پرده برداشت.
🔹
نتانیاهو به‌طور رسمی اعلام کرده که به ارتش این رژیم دستور داده تا کنترل خود بر نوار غزه را به ۷۰ درصد افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/438533" target="_blank">📅 03:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438532">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzmPWGI_5I8fgggf9jTJ51wJkSCmIKUvNeK9PIps87DlplSO5JstXs3_YbKvP--9QY8f8P4eUZD8u4UmHZZFUEvWADOJBJ206oiC6Tv_YqJBmRP4TpZIgAfEDb_GO8N_75xcxAqwy7lZFvb-mLS0KC6zs7TXj-ljY2YjWsNxQkV26-2cA0kxskpAI-9D5mAmYKn_mARIks10xUMOs0NYT2_ZlSjH75ipx-rshvNZ_oXYD_6Ns73WW-5aCfIZL-BsBn-VbtfSWTvcOT0Kd2QPPJxWeD5D-m0Gvu2YZayXrFaDK4epPpfsLAalrDxFB7UUQ_SFGI2qhWwW2o8c0WU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار اتحادیۀ فرودگاه‌های آلمان: حذف پروازها و جهش بلیط در راه است
🔹
کمیسیون اروپا هشدار داد که اگر وضعیت در تنگۀ هرمز بهبود نیابد، بازار سوخت هواپیما در اتحادیۀ اروپا ممکن است با کاهش شدید عرضه مواجه شود.
🔹
در همین راستا اتحادیۀ فرودگاه‌های آلمان اعلام کرد اگر قیمت سوخت هواپیما به همین منوال افزایش یابد، تا پایان تابستان ۲۰ میلیون مسافر اروپایی پروازهای خود را از دست خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/438532" target="_blank">📅 02:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438531">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای سنت‌کام: هیچ هواگرد آمریکایی  در نزدیکی بوشهر ساقط نشده است
🔹
ستاد فرماندهی مرکزی ارتش آمریکا سنت‌کام در بیانیه‌ای مدعی شده که هیچ هواگرد این کشور در نزدیکی بوشهر هدف قرار نگرفته و ساقط نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/438531" target="_blank">📅 02:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C81zeq_IjcgL5ZW4IBPbq14vucDjKvsU6SYdlPhjjP1P7-GGM-_-1YZPPFl3wam8belH2tuqZAU_mA_zLa_mOn2oH1q-Hxbi2EZVwMb9449JBz3lkqJtoS0Qkek_n_2wdC2Z7-XvdTEvM30lHGaGtZcnCHUBBnVbZblaRUTTaJXctxXNKmbXXnBQrPTe8Vm-EFsedPhuJullY2NnBGhOw456Nfg3FDbGStDNWPk6fYVHLJUNw8vEmKfpnPYWMyt6pop0HgjQVqwnUMFmmxQN6SH2usKOaimTaSSaJq45M0rlp7y-DQjrmqVKIZbnvB3H1nsLzBFDHcwREvtan9xVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv-1Dy_uvp6cnyLrlT0TwJ-JIcXNcjFUKkYMB-Nfq1QPFYuxIkBgQpSeQYT2y1oe0gfmerZG7K92b110KlkRQgpZfUMfUSolXENIKtM6mLYfdKnUx1ejWKFiuBsocqALE7pqSu1ID-va7aOv8hENfbHA1PoFYuKPpeTRlKYY-mx11KRIiqu1MrJ6rW_KRaCJWe-k6Wy5tI_idm_3fzTFQFepmRIepsPHjjnFg7Vr4dsmw001tM855Hv7UDIv17wFIuVDMnt-Zm-TzlKFX5DNNwZGh4w6FEeKMCRjOVxrrQ9N8BLrmY3FMS8J4AXSNT1K6kQ11_CrpOIekUmzePgYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o536YyaT2NHpYCw2CaYKWqeiGzE758adaZRfrDVXu0GGbrM7bN3_rYvpw6viQpGet8c_KUV9RD1W2Z2t1uy-KKkA-n4mDwXgzM93xGGCBhIv4II9UAvSOnj3QbADDFWlmRY1whlnm51hE-Xjz4FI9dcds96uhsy3cjSemDBzdfcgCpmkcfjuobLg_9hq17ADDKVF9ckzqKQVYtik_Z7H1jpCfJMr7yROjdxRaZL9buywYNzqZ84aD352huCD8_7jBqZpjK9qmfVbPeWk-HSJQchpxMJJO9JxWLMQwcIGic-s-Nchh0leAwGt5tGpet8zqnIAeWZ4LKHcsFbGSirdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcZ_bGDD9mOnObmVgGEiZVEk8ipsTOxxTU_wrq5R9D4fuZRNSIA9fhJ8UuDWlzJkdjg8STdwRnPyQCSWidU7LGw26iu6BURwbg0h0G3_kINaokQVrmxegT8Eyhqha_0z7fvYMhsDgsRdA3JS4kp50WGqqmmgepPJTaEJNF1TLX5Ty4jQeFqn3sMZfwxbq-gdswlrzfDvV50tiDeUsHGVzbq9zL9QmDrw_b3BOJMKdsZTd9sz-imAFvBSnWu2Cfk8rz2HIDckCW9bQ11dau78GCFkJdpOeRZzsRu8_9pfsk1shN0II7uIfjhA6_Ttt9NoFKSgHqwfGvvCh67HJEwq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fl6nsgLnIrIc-r-35Gb_C1oOddGS6E_86-ZcBThVFx3eBk1j1fe7MoSHIgx2dBR-p7eeBLlAvinvlt7WAGN1_yyS8C7nZmCoMTbBJ_3TZSWVChyyjlpulK4OXBDxfqKjB0whZC6NHG4prYLS4kBFuzrLY255ytrYTOF8anXtbn3j3L4RguegVLSin0UKHtiS_pUlq2fRMccA6vC09L5MrTb6bMLvFw9wZ_aQ-7relx_vDHRr5sETaQoEeEb3AL10qKN-CCK3tRMj4t8U2z4PRQ3SUYCJ0yCFJt05EWZmJWYkzxXeEIbkhsvA3jJ73Z7cfERAw18gX0FlvbXH8zo2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/il4FDuc4FXPQS8YHzUGW7mGfd54vs7Q9PoI1wh0WE2pXJYrcSIe_xVorGKVx0Ch3B2-duJgZ6ms99n4BIvYHaxyUPdCJkyHxMZuyoO4OMOr4QG-9a5DDnpggnGBBV5yfVK9QLVlraA5L5GLUXdvgVMGYrKrsuKIK-KpCzvBDhh80zUKg0ULCaNPsx2DPBa_RvlNNGh3e60pTrA0VZP_RSxkQq7Q6ynJLXDzSy_0dThFbEaUbSsBtuLVA6BPGjqnUhPbvjTRgSJNOhmPVfQ7YFKccJL3RU9VtJhEXRLKAhfTxKsR5VQhXdO5HL8C09tjNeuEQrJuwdMXU26gfF-1YTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nY8_p_XiNle_D1PgnFVefRjIM2Qmetpy8zof8NoFy1uUz7EurhU69-dvGa_0O8DGYKFX4sJJlfwGTErVmeInQy_x7U82AdjTdqMjI9bGqggK5l8Se4wHwVNrU_tljXnUD1K1i1ZpQtLPRTGG2pKjOQWgeaD6wd_VmKLrzJlMy8UKHY_LaqG1Zls_q_aW935cbQpOj5ZEnYwn6kuNPcZJnVOzhM0t_kxHfrHg29bxfaUeGycdkVZg41SNKgmkZN_UzgSj8vAVhzcLWbaE5DYJ1yYJGZz5LCccIzLUbcbXsiROttCmv_-iU5cwnfHrnuZ8c33iC80owmeF-NAjlQWH_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم یادبود شهدای خانواده امام شهید و رهبر انقلاب در حرم حضرت عبدالعظیم(ع)
عکس:
محمدحسن اصلانی
@farsimages</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/438524" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
حماسۀ فسایی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/438523" target="_blank">📅 01:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5a5cfdb7.mp4?token=jBjQwbSpzMtqMtj_2-46An927EiWB4dEtmuPg1Bhl_GccN3e1EHjJVN5U4MLGVe--O1nVe4lEaF7yleGy59lYt-I-zNdsf8euOAn23JSU3k63GU1omR0ZrtOVs2EKOAtCiTZXBGNwo6J57jnOaOzcmiTzjRwmiEA01JpAIfPzwvFaNEnkF-CqLm5g-VpLPRWgtKoqJ5pKhhhvM-M4LGW4miAOBJIKwkt4z8r0c8eqTtTjbAJQb5AXja0T4oUCwbPcvbOPWQOsuTKJwelsxH9frTqcVkSMSV2bQjkcBh79KgwvGtdyHIn0SocYqTj96B4yd81TvJMd_72DN-ZYNO3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5a5cfdb7.mp4?token=jBjQwbSpzMtqMtj_2-46An927EiWB4dEtmuPg1Bhl_GccN3e1EHjJVN5U4MLGVe--O1nVe4lEaF7yleGy59lYt-I-zNdsf8euOAn23JSU3k63GU1omR0ZrtOVs2EKOAtCiTZXBGNwo6J57jnOaOzcmiTzjRwmiEA01JpAIfPzwvFaNEnkF-CqLm5g-VpLPRWgtKoqJ5pKhhhvM-M4LGW4miAOBJIKwkt4z8r0c8eqTtTjbAJQb5AXja0T4oUCwbPcvbOPWQOsuTKJwelsxH9frTqcVkSMSV2bQjkcBh79KgwvGtdyHIn0SocYqTj96B4yd81TvJMd_72DN-ZYNO3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای نشستگان در مقابل خانۀ خدا، به ایستادگان در مقابل دشمنان خدا دعا کنید
🔸
ویژۀ ساعت شهادت شهید حاج‌قاسم سلیمانی و همراهان در فرودگاه بغداد
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/438522" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC_mruw_H0mG1TvZGbSnbyT3m5GQ-QNBXKIKrBZCuCBxqJQiF_Tq2yL1U8am5gEYsAG2NWzA6ALo2usVOC0I2AKMmaTBMqM4UrdAEm-P6R5QFJHdXFohkjc2esCauNsSyzjRpNEXXdcoe1GUb1BlomjI1WEEXiHhcj3cyhh4mhbTwIL6eBTuXD9sbncP9OS1PgpKk3TOrwliMG3JEb9jgwfeZz6sYenwdVF0nAGZ3MYY3zuLw2d_ZR11WGBSdEPNQx3ZkuJltDkCJcQmHFWGTNpWCAryGexLkjLV5k0lU8QM5LmDhYl9yxVTywrejsW0TzsrLWnacNiMuwGIvMWEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز بالاترین تورم ۳ سال اخیر آمریکا را رقم زد
🔹
تازه‌ترین داده‌های رسمی وزارت بازرگانی آمریکا نشان می‌دهد که نرخ تورم در این کشور طی ماه آوریل با شدیدترین شتاب ۳ سال اخیر افزایش یافته است.
🔹
دلیل اصلی این تورم، افزایش شدید قیمت انرژی درپی جنگ‌افروزی آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن اختلال در ترانزیت نفت از تنگۀ هرمز اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/438521" target="_blank">📅 01:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjAtHPkAF93M46Bb6AWcz05651Ez4FI3zqLvSKwd4RBbpLROv-sb54okkVYUnn6XItj-9bnNtw3NNjZzWXhuTgIQUYB-SrSw2Q0M7YkvbIoXkdO5Ag74jzKb0tRljL9Bdmrt7F32mUmzAlzleCDFtQBR03ei0_homE_v63QefVLmY2F4c8Jb4QBvncBvaOnHCdwEcRxH2-7Mow3Ik4RJ9mHb3Ui4eXtddPI-J1uE2a0_pgQqyUNvhtbIIwIxQbXnJkwpUf3vwOPlIoKAZ4901hF54qCiba4TrTjvGsWkImD-HlKV1t26mbmaNunp-JbQGDULMXFOz-eVRMBJ8bROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه تهدیدهای آمریکا علیه عمان را محکوم کرد
🔹
سخنگوی وزارت خارجه، تهدید وزیر خزانه‌داری آمریکا به اعمال تحریم علیه عمان، متعاقب تهدید قبلی به «منهدم کردن» عمان را تلاش برای باج‌گیری از یک دولت مستقل عضو سازمان ملل متحد و نشانۀ دیگری از ورشکستگی اخلاقی سامانۀ حکمرانی و سیاست‌ورزی در آمریکا دانست.
🔹
بقائی خاطرنشان کرد: تهدید به اعمال تحریم علیه عمان به بهانه‌ای واهی، اقدامی مطلقا غیرقانونی و مغایر با اصول بنیادین منشور ملل متحد و حقوق بین‌الملل است و جامعۀ جهانی می‌بایست با واکنش مسئولانه در قبال این رویکرد، مانع از عادی‌سازی فزایندۀ نقض هنجارهای حقوقی بین‌المللی شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/438520" target="_blank">📅 00:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حملۀ موشکی حزب‌الله به محل تجمع نظامیان صهیونیست
🔹
حزب‌الله اعلام کرد، محل تجمع خودروهای زرهی و نظامیان ارتش اسرائیل را در منطقۀ زوطر شرقی هدف حملۀ موشکی قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/438519" target="_blank">📅 00:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی از جنوب کشور
🔹
دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
🔹
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
🔹
برخی رسانه‌ها از وقوع انفجار…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438518" target="_blank">📅 00:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmN5XMW0dGEGGc6bYZmH3FGIk9T1HiE9BDAWSrGxE5ShxCWBrwmWkVVbFrQOnA8TFtFqdw_5kB04g_pF0PLh8ltHrcmkFABkRV6Ni4s9HLdHSO0llzLxhqH2U4HoUVu3_gpyEjoteil5BUN6AZ6xMjIZeNuKKMnKSJUYr1_QELqH3swGDeOS7T__NKSFLXwSv74THtkZGdZhlDQ_u5-vhERUQGzs_jCcgQ8ZF06BZJHnH0a1VjNRhLBy5XVUkIpQysZzqRtxSxcfbMWImCdnI2bxNg3XH5D-8s5Af0IHLfnTEg-GAf504GZKfYGF6At-89Wc-gRWZWAHSVmg5N-F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرد مغرور
🔹
روزی مردی ساده‌لوح به سمت بازار حرکت کرد تا برای خودش الاغی بخرد. در راه، یکی از دوستانش او را دید و پرسید: «با این عجله کجا می‌روی؟»
🔹
مرد با خوشحالی گفت: «به بازار می‌روم تا یک الاغ بخرم.» دوستش گفت: «بگو ان‌شاءالله!»
🔹
مرد بادی به غبغب انداخت و گفت: «ان‌شاءالله دیگر برای چیست؟ پول که در جیبم است، الاغ هم که در بازار فراوان! دیگر چه نیازی به ان‌شاءالله است؟» و بدون توجه به حرف دوستش، راهی بازار شد.
🔹
وقتی او به بازار رسید و در میان جمعیت و شلوغی چرخ می‌زد، یک دزد در یک چشم‌برهم‌زدن، جیب مرد را زد و تمام پول‌هایش را دزدید.
🔹
مرد که بعد از مدتی دست در جیبش کرد، دید کیسهٔ پولش نیست و دست از پا درازتر، بدون الاغ مجبور است به خانه برگردد.
🔹
در راه بازگشت، دوباره همان دوستش را دید. دوستش که او را پیاده و غمگین دید، پرسید: «خب، چه شد؟ الاغ را خریدی؟»
🔹
مرد با لحنی مغموم و پشیمان رو به او کرد و گفت: «ان‌شاءالله پولم را زدند، ان‌شاءالله الاغ نخریدم و ان‌شاءالله دارم دست‌خالی به خانه برمی‌گردم!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438517" target="_blank">📅 00:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b478ab8c6b.mp4?token=szYHnieD1ftxEyrO-Q2JFQcRL6s2HODAzxgLU-gqC0fSEhkKXAbWiQRm1kZyyxTs4A_bEU_61fLe3SogUz7iziSK1ibuvsHTd9kQxMvAFiJS1tCu7crZo5Wjcpabk9D1NJdImIx6NV4I8nctV3LM-bv-O3iw66a7Z0rBpIZKM4V16bfY3TREip2SGQ9EaYHv5ZKyc18L6RkOAtUwshxt6jceqmSuSLCa4cT1huP4nBI76_2oVT913uoU5-4ToOnTUvARtsERS3iJnlj9umEO_YR6dKXU4kQzWu-OXwG9VfyKE9yedopHN2gQd5vZ6I9PR7sT82ioAo6KV35bQ3gXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b478ab8c6b.mp4?token=szYHnieD1ftxEyrO-Q2JFQcRL6s2HODAzxgLU-gqC0fSEhkKXAbWiQRm1kZyyxTs4A_bEU_61fLe3SogUz7iziSK1ibuvsHTd9kQxMvAFiJS1tCu7crZo5Wjcpabk9D1NJdImIx6NV4I8nctV3LM-bv-O3iw66a7Z0rBpIZKM4V16bfY3TREip2SGQ9EaYHv5ZKyc18L6RkOAtUwshxt6jceqmSuSLCa4cT1huP4nBI76_2oVT913uoU5-4ToOnTUvARtsERS3iJnlj9umEO_YR6dKXU4kQzWu-OXwG9VfyKE9yedopHN2gQd5vZ6I9PR7sT82ioAo6KV35bQ3gXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستگاه ۸۹ قیام مدافعان وطن در آبیک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438515" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی از جنوب کشور
🔹
دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
🔹
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
🔹
برخی رسانه‌ها از وقوع انفجار در استان‌های بوشهر و هرمزگان خبر داده بودند که بررسی‌های میدانی فارس وقوع انفجار در این استان‌ها تا این لحظه را رد می‌کند.
🔸
بامداد امروز هم پس از تعرض دشمن به مناطق شرقی بندرعباس پایگاه مبدأ این تجاوز مورد هدف نیروهای مسلح جمهوری اسلامی قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/438513" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acd386934.mp4?token=pcqtYxwzZ7IZ-kMA9tGdnUIK-OeByW6rTrFnZQ56B_WO67QmlWGNSbRi7rGHGnNLLtWrL_ULFhLVP4JL-ORULO9TVJSlsheAYdWCynoePZmLkN3yvvU7t0Cz0r1kXdROPbICYPc9JXn18weGMdrOx7pe3DxyfTdvIbWSJGbhFV2VvBKWPT7fjZu7ycqxnueVXO0xgSfA3cZm7la0AIG_CBeWB_eK4w9L99ahAijlo3Tp8Rh78xrx0D-M3jgycp5U2uW18Yke7U4OG9zMOBLa2ud6ZfmFsuAUJtPpJeThDGDcbh_ojrfPtn8S-0GBidfx3N8x9Rw1CXUt4wkN8pX1yRdxA7B8es3KOycwPD-NRSJ9lWsLMcf30AVJ-ggj1ipIvKsapNbJ0eandP540rY4Eklwq4YwX8tl80cb482iyBjhtAZ2a1awRA_oe7pPSLUqQudv-2FsR24VPY9ZjIs9_lEP5as-pcLBCSD1b0TGdQ2j-EWmXnQrHdxRxuvRJEnk8545Jb_PS6vVaBcWWLp8REzlw83YD687g5uvn1PWIMMIkYCPBubeopRTcNox0zEcUw52ouoP5O-1tUB9T7wlUXSdQANuOyVnDmjwYhRId4je4nShEfTGduO3Qx42E_wDMf7PNYgV9fYSvsS3f-ysnzA8FKhdigx8HAj33SSjiWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acd386934.mp4?token=pcqtYxwzZ7IZ-kMA9tGdnUIK-OeByW6rTrFnZQ56B_WO67QmlWGNSbRi7rGHGnNLLtWrL_ULFhLVP4JL-ORULO9TVJSlsheAYdWCynoePZmLkN3yvvU7t0Cz0r1kXdROPbICYPc9JXn18weGMdrOx7pe3DxyfTdvIbWSJGbhFV2VvBKWPT7fjZu7ycqxnueVXO0xgSfA3cZm7la0AIG_CBeWB_eK4w9L99ahAijlo3Tp8Rh78xrx0D-M3jgycp5U2uW18Yke7U4OG9zMOBLa2ud6ZfmFsuAUJtPpJeThDGDcbh_ojrfPtn8S-0GBidfx3N8x9Rw1CXUt4wkN8pX1yRdxA7B8es3KOycwPD-NRSJ9lWsLMcf30AVJ-ggj1ipIvKsapNbJ0eandP540rY4Eklwq4YwX8tl80cb482iyBjhtAZ2a1awRA_oe7pPSLUqQudv-2FsR24VPY9ZjIs9_lEP5as-pcLBCSD1b0TGdQ2j-EWmXnQrHdxRxuvRJEnk8545Jb_PS6vVaBcWWLp8REzlw83YD687g5uvn1PWIMMIkYCPBubeopRTcNox0zEcUw52ouoP5O-1tUB9T7wlUXSdQANuOyVnDmjwYhRId4je4nShEfTGduO3Qx42E_wDMf7PNYgV9fYSvsS3f-ysnzA8FKhdigx8HAj33SSjiWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بسیج؛ روایتی از ناگفته‌های جوانی تا شهادت شهید سلیمانی  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/438512" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290a136232.mp4?token=gud4CQO0nSYEs5RLtn8JOe0Kx6fJlFC3N2PSh1P2CcX8bL2mk5yGZ1U-Bjp2nY6MNCLNTmoA4NApKANNDFqeJ528vVAgPmqdWnflJrTR43UIQy3HAm7dR1_U9XfZu5KlKbHqDcP6oO-HK-y9gMbtnr69U_Y64DE0OY8kPEbK_7XhZpmpflXU03tK696mFZ7DL8Sw_mNSX05Tg3_6UGzB2hLolo7h8vjTXy8A2nwD-QbnkHjCpawTejt6BjwT0DNAQa0ETwCVNOA9sojau7FXsj2qtGku-I17d1JF5hOFSFEhGQExB_pC7afwRX6pS1uTUEtcvSSKaLPUHbPxtZUy7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290a136232.mp4?token=gud4CQO0nSYEs5RLtn8JOe0Kx6fJlFC3N2PSh1P2CcX8bL2mk5yGZ1U-Bjp2nY6MNCLNTmoA4NApKANNDFqeJ528vVAgPmqdWnflJrTR43UIQy3HAm7dR1_U9XfZu5KlKbHqDcP6oO-HK-y9gMbtnr69U_Y64DE0OY8kPEbK_7XhZpmpflXU03tK696mFZ7DL8Sw_mNSX05Tg3_6UGzB2hLolo7h8vjTXy8A2nwD-QbnkHjCpawTejt6BjwT0DNAQa0ETwCVNOA9sojau7FXsj2qtGku-I17d1JF5hOFSFEhGQExB_pC7afwRX6pS1uTUEtcvSSKaLPUHbPxtZUy7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌نوایی خرم‌آبادی‌ها در شب ۸۹: حضور در خیابان به جانمان پیوند خورده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438511" target="_blank">📅 23:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e475c738dc.mp4?token=iINJksz0OzufTFswz_OsWnqpc9gDueAzr4CC92cXkJ4GYAQ4ll0A-XI5VwjH_0Y88iYUJlR7Y4mSr896TVSj1UDf_Eb-hNVTD8ZkCA9ZosPOCktxH9BbqnRNuuZJ73tnyNVYoBe5dkO1Gq6_ZIhzlXr2CWI2GJvcAs3rguu_4Xb6kTfmnQak0I1n7ClHb-A0QWM_eSJxCOLthgqGFtmwFQvWNmiPYsPLsCN7J7sc7MGmIrVHcbXa8yDkJfQp9JIbkNWpob3Qx5ufgpdMZUl-aVWstnC5ooXOhLnhg8HyW_iNl7i2CO0_Npg92MmGL3tsu27yLQCn-ZKadkYOH91_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e475c738dc.mp4?token=iINJksz0OzufTFswz_OsWnqpc9gDueAzr4CC92cXkJ4GYAQ4ll0A-XI5VwjH_0Y88iYUJlR7Y4mSr896TVSj1UDf_Eb-hNVTD8ZkCA9ZosPOCktxH9BbqnRNuuZJ73tnyNVYoBe5dkO1Gq6_ZIhzlXr2CWI2GJvcAs3rguu_4Xb6kTfmnQak0I1n7ClHb-A0QWM_eSJxCOLthgqGFtmwFQvWNmiPYsPLsCN7J7sc7MGmIrVHcbXa8yDkJfQp9JIbkNWpob3Qx5ufgpdMZUl-aVWstnC5ooXOhLnhg8HyW_iNl7i2CO0_Npg92MmGL3tsu27yLQCn-ZKadkYOH91_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی دختر دهه‌نودی در اجتماع مردم کاشمر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438510" target="_blank">📅 23:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شهادت یک مامور پلیس در سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان اعلام کرد که ساعتی قبل استوار دوم عیسی عباسی که در حال عزیمت به محل کار بود توسط افراد مسلح ترور شد و به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438509" target="_blank">📅 23:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f137fb22b.mp4?token=BUwAJRVZ4HsWlyV2gZz87ON1eu1P3Yx0aPRayWUyA9rDVP03pHr9o2-kEDZbcpdzIi18LJ2bvLrYDfSWCT6-JBCDlXNQHpUFXe54J63kBYQajIzu44p7q5fED3Rh1_WaIpdujFezSicUlV2UsBAB4rAx5D1BG7_ijqi8mU3T-NFfklQNg0E9yx7uk7OgXTsg_QocT4vtuAWCELKfJG3Di4DL9kv_r6vQg23a9rIB2IJFXVLAOEyBg_LnpDYGNryWWxTJ5Ax0JH2C6Fc87z6b5dV722dGy59lWqK0XiEwcrFLrgkMyXliujCdN0xHpJB-__nLL4Mr-Yf01z6mwwlEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f137fb22b.mp4?token=BUwAJRVZ4HsWlyV2gZz87ON1eu1P3Yx0aPRayWUyA9rDVP03pHr9o2-kEDZbcpdzIi18LJ2bvLrYDfSWCT6-JBCDlXNQHpUFXe54J63kBYQajIzu44p7q5fED3Rh1_WaIpdujFezSicUlV2UsBAB4rAx5D1BG7_ijqi8mU3T-NFfklQNg0E9yx7uk7OgXTsg_QocT4vtuAWCELKfJG3Di4DL9kv_r6vQg23a9rIB2IJFXVLAOEyBg_LnpDYGNryWWxTJ5Ax0JH2C6Fc87z6b5dV722dGy59lWqK0XiEwcrFLrgkMyXliujCdN0xHpJB-__nLL4Mr-Yf01z6mwwlEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۹ شب حماسهٔ یاسوجی‌ها در میدان اقتدار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438508" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9e55123b.mp4?token=A_UzUWhkPxjwjjOhZI_W7tRL-Il7NVvFSZj0Y0VtfLkd3tYS7irg6eyFBEHkWyr65XSLWM1DPR8ankMzg4bz1_MuGKQ28XUdMA-8d0alA2lfIGWChfRdoYwxzslN3f6VyBxsh3Npqnh1olxeSKB0Ban7EQ1Xa1LCBFUpdC1MJNR0uzlFvspUL3WTqinWC_890SOsDief0Eplw-BQUcOx5HfADnxfyqT4zVVvcuUM8H_vVDoYpAUN-KOjjAFaTVn-BjC6Ea1vVoqiITW4k1wOy0tx6WompEUbGeeq-kDZv3Et2XkUgYbpVvC9oP_VR0KObHEFly977OMnaWcbv4ML3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9e55123b.mp4?token=A_UzUWhkPxjwjjOhZI_W7tRL-Il7NVvFSZj0Y0VtfLkd3tYS7irg6eyFBEHkWyr65XSLWM1DPR8ankMzg4bz1_MuGKQ28XUdMA-8d0alA2lfIGWChfRdoYwxzslN3f6VyBxsh3Npqnh1olxeSKB0Ban7EQ1Xa1LCBFUpdC1MJNR0uzlFvspUL3WTqinWC_890SOsDief0Eplw-BQUcOx5HfADnxfyqT4zVVvcuUM8H_vVDoYpAUN-KOjjAFaTVn-BjC6Ea1vVoqiITW4k1wOy0tx6WompEUbGeeq-kDZv3Et2XkUgYbpVvC9oP_VR0KObHEFly977OMnaWcbv4ML3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۸۹ حضور مردم غیور لردگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438507" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0a90505f.mp4?token=IKdViU08fQOJKbkJznz2rYJZcX7ICidpyXW1GRpkWicZ0RqVOi5eyfmW12n7UPH-56qh0k_B-cQdcxvkldnKBVfsTRhqH0o3mLSD5qAhheESm-xXbQ0IDhAz4H0CvCSodd2sH36ly8lpUAtX1ofrTxP-DvvFA9Tnv2eLagMPkABC12kZOdXe4TT2ELuTT3meiG7SjfI4HMq_cJVAaM8pae9jeYQjHC4jNNOoSBifKmVbs4uMhTOO8PCIl3T4_CdfakAUrLqmYExfmuZX5fVz4aVPOvEbVxQL_RlLUyxvoahuPt7xZXTSC6j5unO1xlc9Gw2XDyC9PUxYxIhxKIsftFhozOL3uNfx5sBRKPgnNYgOIF7IOd6EDHDIHfwUTlRwQdAmdBnTjgwtD-88KOaObb4BoG54SKJo3P9NmkPXDFoq3cP0sN9kLEs_buXLxqNHkmvp8SAH8jeKe-51LxYvQPTAbLzNe4S9lbG0Um34lOFoVX7kphg35eAK3RHqM3D4IcCp-Yp1lbnCRTuoUzV-o1D74Sk355UVCrxo1jT79K1V8IeMGj8vtIGzc25nLn4KKqCiIMszHZc4fgQVJ9viGx8WMJJpPGuyaRZdtO2fQCU47lj8pFV2hy7fNYfFyF2b2q0YKb-DjOMgKMTjvaWdBMS9BRiPNVip5Kh9BGme7-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0a90505f.mp4?token=IKdViU08fQOJKbkJznz2rYJZcX7ICidpyXW1GRpkWicZ0RqVOi5eyfmW12n7UPH-56qh0k_B-cQdcxvkldnKBVfsTRhqH0o3mLSD5qAhheESm-xXbQ0IDhAz4H0CvCSodd2sH36ly8lpUAtX1ofrTxP-DvvFA9Tnv2eLagMPkABC12kZOdXe4TT2ELuTT3meiG7SjfI4HMq_cJVAaM8pae9jeYQjHC4jNNOoSBifKmVbs4uMhTOO8PCIl3T4_CdfakAUrLqmYExfmuZX5fVz4aVPOvEbVxQL_RlLUyxvoahuPt7xZXTSC6j5unO1xlc9Gw2XDyC9PUxYxIhxKIsftFhozOL3uNfx5sBRKPgnNYgOIF7IOd6EDHDIHfwUTlRwQdAmdBnTjgwtD-88KOaObb4BoG54SKJo3P9NmkPXDFoq3cP0sN9kLEs_buXLxqNHkmvp8SAH8jeKe-51LxYvQPTAbLzNe4S9lbG0Um34lOFoVX7kphg35eAK3RHqM3D4IcCp-Yp1lbnCRTuoUzV-o1D74Sk355UVCrxo1jT79K1V8IeMGj8vtIGzc25nLn4KKqCiIMszHZc4fgQVJ9viGx8WMJJpPGuyaRZdtO2fQCU47lj8pFV2hy7fNYfFyF2b2q0YKb-DjOMgKMTjvaWdBMS9BRiPNVip5Kh9BGme7-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم جانشان را برای اسلام و وطن می‌دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438506" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6436e2ce.mp4?token=KZ3iZsy5Ee09HJyOtT4FD-kYpsEYiKgJQ7NcG2PDiO0B97xGTpcCyQqul7hbL8dmTn7LUv2GUp-G9FP08RBYkNGOoM3ELC4thcoJFT8qG04rZqqhZa0hChYo9ISvQS1-iS2So5C7zkLdfzA-GTP5nrLBAaSoQ1yFxqVhuVdeik38AR5q2EiNZ5fkrySfDsywYhwZ-A1JzxzQXXjE5ilLkvaCh-vxogtLXnthdZKI3M-1nbncjDsNdZXr7zL8pgb9mlZD6UhdTcS0ZR2CPaOWx3cIoXxkpIWW8lOOwrCvsT_-R3rXBoRNNyWn1rFVSBNowf1u5Coi39UItENCBlZWTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6436e2ce.mp4?token=KZ3iZsy5Ee09HJyOtT4FD-kYpsEYiKgJQ7NcG2PDiO0B97xGTpcCyQqul7hbL8dmTn7LUv2GUp-G9FP08RBYkNGOoM3ELC4thcoJFT8qG04rZqqhZa0hChYo9ISvQS1-iS2So5C7zkLdfzA-GTP5nrLBAaSoQ1yFxqVhuVdeik38AR5q2EiNZ5fkrySfDsywYhwZ-A1JzxzQXXjE5ilLkvaCh-vxogtLXnthdZKI3M-1nbncjDsNdZXr7zL8pgb9mlZD6UhdTcS0ZR2CPaOWx3cIoXxkpIWW8lOOwrCvsT_-R3rXBoRNNyWn1rFVSBNowf1u5Coi39UItENCBlZWTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار هشتادونهم مراغه‌ای‌ها در شب‌های دفاع از میهن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438505" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c835b11e79.mp4?token=gAb9EX-x0qJBRC3bLY8PdzWT2EPG-jtBF9cjRd4XCZgoubRHV-mha7Uc8fak5_2HatA7MfQH5nhgM6asj3kTcIyqx5u2YOqCoHBf8QbuvuJolKRTjf6iMRE3E-3NlImTU1AQWUZZ3d4n3I2jAcgVMYguzBeT0YEvxKZbjnHCQr_mLKK6qf2QzmK_12hxvAi4nC2DqmEi8qwstei_uGK8VjZ_EtjEt7hFFxlR_afA6RZSynVwFPJHg2yKA2IagpbyAF70ruhfejTdCdae-taGSxmnlS50fugGhL8FbxlERb2gFqKssxc1mBzfou8l4WO6bOb1reLCzXvWuSlxaqqI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c835b11e79.mp4?token=gAb9EX-x0qJBRC3bLY8PdzWT2EPG-jtBF9cjRd4XCZgoubRHV-mha7Uc8fak5_2HatA7MfQH5nhgM6asj3kTcIyqx5u2YOqCoHBf8QbuvuJolKRTjf6iMRE3E-3NlImTU1AQWUZZ3d4n3I2jAcgVMYguzBeT0YEvxKZbjnHCQr_mLKK6qf2QzmK_12hxvAi4nC2DqmEi8qwstei_uGK8VjZ_EtjEt7hFFxlR_afA6RZSynVwFPJHg2yKA2IagpbyAF70ruhfejTdCdae-taGSxmnlS50fugGhL8FbxlERb2gFqKssxc1mBzfou8l4WO6bOb1reLCzXvWuSlxaqqI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب:  نمایندگان مجلس مطالبات عمومی را بر نیازها و منافع جناحی و گروهی و منطقه‌ای ترجیح دهند
🔹
برای ایفای نقشی در تراز ملّت مبعوث‌شده، مقدمات و الزامات گوناگونی نیز مورد نیاز است که در این مجال مختصر، صرفاً برادران و خواهران گرامی را به مطالعهٔ…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438504" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484727e1e3.mp4?token=jReFCtfomL-afZC2Vm3Ja_uFU2gH1xGX8VVn2wI_C1ELp77mIHskg0Gl8g3-2HWhFc1-BR632n9ooyXxICXLTpKR8JsHzZcD92uiM5LIvsXl_ffBCsNtlwemNa5dLh_Q6obAkPpSsFZf45erIxEqs04nmj8PQcDDPhlj9b3kfIHqo3DqeJ-R8FY5cOm4Hv17xHUADOX0J3HjXLJ1-LSmGsfVBQGxGsbSx60BEJeBgMrTFdhqyIlXB5mS8qqwqzkK4z1HW55Xk3hlpQ7pwPgzL2OpR4zC-m7BOvcdwTxynAbSrTQsv7eeqrwgYVVVVvivNnTHihZnqxF-ph0vGY11fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484727e1e3.mp4?token=jReFCtfomL-afZC2Vm3Ja_uFU2gH1xGX8VVn2wI_C1ELp77mIHskg0Gl8g3-2HWhFc1-BR632n9ooyXxICXLTpKR8JsHzZcD92uiM5LIvsXl_ffBCsNtlwemNa5dLh_Q6obAkPpSsFZf45erIxEqs04nmj8PQcDDPhlj9b3kfIHqo3DqeJ-R8FY5cOm4Hv17xHUADOX0J3HjXLJ1-LSmGsfVBQGxGsbSx60BEJeBgMrTFdhqyIlXB5mS8qqwqzkK4z1HW55Xk3hlpQ7pwPgzL2OpR4zC-m7BOvcdwTxynAbSrTQsv7eeqrwgYVVVVvivNnTHihZnqxF-ph0vGY11fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلزار شهدای میناب، میعادگاه جدید عاشقان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438503" target="_blank">📅 22:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حزب‌الله: طی یک ساعت ۳ تجمع نظامیان صهیونیست را هدف حمله قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438502" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cc809c60.mp4?token=VbyF5FbHWlogAL5u5PjXuSojI7LP0OE19ry9-M0ctgkutR5R0iE4sp07xmUlkA82c97sKSylHFd6Fc6zukssQMv3SrIcAGTGxpUQnQEAtXP6a5kCj_HsNXxUeXgjGDGumdoH1R6Rtvu3vv2aS0NUq_UXmnPOXYuAZ1W-rU5Ehk-C9HwzgUkp88oTNg1RCKRPZj3os53ViwPpvUxeXBeQP29E5c69mfbiSMp06hmovvqxtyOKqtrrLViNr8eju1zrJzFUL68ClgyeunxXan2fsTS0RtFNBD-P9Yk1K8NxApjXdyoTgQVv94fXsejLkdpr_Xio8PyXrsaorKG_Uj-JBAVQ2LpUpiF3Z4rE1ikrhAU7JIxOf40OA9KbQsG2PDPNbhYLHKf0Fsty33BUD9RHRjsA94DfnFPaCaPmrp397Qw7eEU-cXg1jUtiXUM0CEPMBwBdu_AnO0cyp_pechwNqsAEJn0G924GTVEMcdJ_M1os3R9mRI7Degt0mNE-n5EHZm6izAhDH2BOM_6t_Kkd4YYiCubtpWsvEHkQ6TXq3atNA3Zv9qtz4eaW-Wx-PfW3HCZ0JSnf755HIWcLSlUlZH7U91f4Z4J6ItBEYf17q83lGSn0aTeGJCJF9C0MSvEU5Q26SkipoxbrDaTXtSzKEgJmOOMUqsJKA8u55_NQdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cc809c60.mp4?token=VbyF5FbHWlogAL5u5PjXuSojI7LP0OE19ry9-M0ctgkutR5R0iE4sp07xmUlkA82c97sKSylHFd6Fc6zukssQMv3SrIcAGTGxpUQnQEAtXP6a5kCj_HsNXxUeXgjGDGumdoH1R6Rtvu3vv2aS0NUq_UXmnPOXYuAZ1W-rU5Ehk-C9HwzgUkp88oTNg1RCKRPZj3os53ViwPpvUxeXBeQP29E5c69mfbiSMp06hmovvqxtyOKqtrrLViNr8eju1zrJzFUL68ClgyeunxXan2fsTS0RtFNBD-P9Yk1K8NxApjXdyoTgQVv94fXsejLkdpr_Xio8PyXrsaorKG_Uj-JBAVQ2LpUpiF3Z4rE1ikrhAU7JIxOf40OA9KbQsG2PDPNbhYLHKf0Fsty33BUD9RHRjsA94DfnFPaCaPmrp397Qw7eEU-cXg1jUtiXUM0CEPMBwBdu_AnO0cyp_pechwNqsAEJn0G924GTVEMcdJ_M1os3R9mRI7Degt0mNE-n5EHZm6izAhDH2BOM_6t_Kkd4YYiCubtpWsvEHkQ6TXq3atNA3Zv9qtz4eaW-Wx-PfW3HCZ0JSnf755HIWcLSlUlZH7U91f4Z4J6ItBEYf17q83lGSn0aTeGJCJF9C0MSvEU5Q26SkipoxbrDaTXtSzKEgJmOOMUqsJKA8u55_NQdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروهای نظامی صهیونیست‌ها یکی پس‌از دیگری شکار می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/438501" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743ec3e77d.mp4?token=ojUzpHJRmsjYCeb8qmeO_56tVNspbbnWQLfh7idYJwBJAAj9Lscg0F5aYEZ8NN8uk0d5Sn1VTQCtG7EHXd5eM-0Cp-HFb8XXv1XwkkO88OiS4btIJ3VBLLikkWHNCR8p8aZ0u9f0egRYxtwFJ3-eOBwBi5Bdjl4BCi128whxFKS27sO3qIqxeowm1C4sTO9YIklK3E2e2MfuKwg5TFPKWHENWbOOBGEKBLSOl-yi0gm25O7Y-7dprG-dRcTTWVhkprR6z083ZqyLZ3iYCiiKQ5_V4pNmJ9I3S3DTaSgwkms2YbqdCxdVhpdwueSRGqlviwNwWl6LQgjQxn2SUeoVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743ec3e77d.mp4?token=ojUzpHJRmsjYCeb8qmeO_56tVNspbbnWQLfh7idYJwBJAAj9Lscg0F5aYEZ8NN8uk0d5Sn1VTQCtG7EHXd5eM-0Cp-HFb8XXv1XwkkO88OiS4btIJ3VBLLikkWHNCR8p8aZ0u9f0egRYxtwFJ3-eOBwBi5Bdjl4BCi128whxFKS27sO3qIqxeowm1C4sTO9YIklK3E2e2MfuKwg5TFPKWHENWbOOBGEKBLSOl-yi0gm25O7Y-7dprG-dRcTTWVhkprR6z083ZqyLZ3iYCiiKQ5_V4pNmJ9I3S3DTaSgwkms2YbqdCxdVhpdwueSRGqlviwNwWl6LQgjQxn2SUeoVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار مرگ بر آمریکا و مرگ بر اسرائیل در پایان مراسم یادبود شهدای خانوادۀ امام شهید  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438500" target="_blank">📅 21:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAPb_uqW8KW_nri4KI-kmQlKH4_FGKsVuIVEnNydC0f5jnIO4I2rhGWYa14aEHUGwbXUxJVYGZshl2bMfc5kTubQC3SuKTqIzX13jwGWHD-S_keS8wzja1PSe8nqlobuK5f_rK6_FkjfSHPD-GMnOGr0LqGfw2hwN2u_oEDeQjsAKh6IyChQhKV4EYzdglumNRJeCGSQUQ0kJbbAwAFhvkqW9Wjp8rFQe17-OgrbWRPL0vYXHLw7ACgFQp_0Z6WRfIdLV6hlnRftAyEBP6asULQ8g7L5LMlF2tVQuYfSt2JMZeuYdmx0pJ-UfDQcVZ-D6-Rx1CAbNgGw4SX5N7B-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N37b6hXUbUCOTRGqCS1ik2SG8LxLzna7HoZUPAJXW6CsTg86WAq3dAlD1HwqAiOeUSwEB7rQyqgvvPXmesV1UfLjHqmpCIC69FR0pGianprJ_ev0ZDhLyZ4Yzs9-MIC1ePSE_VrqFTdxjlHEKOPpA_OU__5v8D6jjOF55CM1lKKr4f0jUsy6hW-xQ_Pj3wwTi7E0n5Yi1c5zGCQN5_BL3deXUq4d7vAreIXJjpgGQHcQTFocq3_QMcg4Qy5YuKP3g9d3UnRcmuOAjRI5FBc-8L8Xk_VnSu4u3XICXFlMMM3_Hq0jPmt-XLG_VeW53b4Ep-0OqUKG-hxl9XyoVQ5OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Z-xC8n61VgxHmfhnnJseGFrewslhSCrz5zHW308LZkD8ozUQ_d8g68k8SsPj8JYJnkUVHg2NrLkqO_fS9wzdvZR86zJP8h60PIRvtaPU_lnELj2EsOjHga_s0CkQQAz8ooD4eSuDZ1sVgbTILVHumstFG4j-MqcpT86HJqzxE4U1pFrQAK13Hy0CITkxt4f9nQluCqKYNbynr2rPrn3VCp1ZZH8e4HcrIgRHGt_dbMIcd4seJ4oDvAjoIkZPylu6nNTpdeILlxWDUwqC3LgI3OrRh_9cH7IREWtkdoZp4MfhHWXd6msM8FtFZ0WZJkMeukNv0sFg9BpW2W0b1pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orqpGy3VkbUyLnjfn1z3nRorYUjZpdTcAhiLp8lqEEthWD518iS5wkqM3zbJqwbFlfaHQMgrBb5JsuCPfN9cMOhELhEyrFrPGKXx9m23Z27TavDw2qMg93aTt74JgAtPXHv-RJOAxNYLNFKOIxyn6ZYpF8UUoAtaZN4M_ZEh8qsQrgkzqkXECeBi1z5QDO4xL4tanAMw9isGQXoo66NldC2qZX6rKw_TScd2ER16jm7kLdztZYr8HtkEvuL6EVflv3oh4a9GGV0D544mibOfVfxzbiLdDQaQtlHmoQ3rm9lFJWVtcRjBZMqzgAGlA69MJ1awbUUnYahVvj4Vr4cCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs5AxfG06eFCwkkhIVewm1_YGmbIeKRqKeejfr3tPFPEilgRzCsvCo4r0GvATEFSMgXNoRF3fxQiLbsyIdXNLSQjL5qr0YeEj3wj5jVfe9kYJbSRgGd-wiruHYnGX-Pu4UB8Lrbo0g7nCcL_eR6u4uBuge2eKAwoUSoHoV92fPkvO91NWADghlaJNO6hXObJ360aureLUh6XDFytNHBGBUfWamdeEKGPxvuw7vSrACWILS7gUjGcZWLqBkWT5v7mS9SovovT7qqYXrBHw_K-T1gHL1KwUasGS7UJcwYQnHPa60W_WOUGY80KP33hCh44nlSPHWwv_UidxRwvxk4I6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH8tDRWBe8f3MCPr1fDi5_1SvQ1eLX3LCZ3GAvHJtG4KPE6pWkIS100dCUkmGPqIr1yGWYyCi205Z5AyKgdawd8qeSaqIdkjncQLA7KZlYDDystk84Ux7iHPHNShGY74_l7UCo68a7Jvsg6h_P_BD9yaIS8VPNJ4Y28xHp21bpaIBSleZ2Po394xyjhnRrq9TEpOLtoeVzRrDmWlqYBxSlWgH2lBwaPsioAUsy4ZvDz15_kLDFtEySMlqp2OTRxH8Ybzi7JFlaYNAdOjpQAfFzZW6K2g4ICViGHO9HiTQxIx7k1Dm80-q7EFUW81YCsfX_GeCzr8CcksrOpv8eH2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVto8uqRnn4EQW2xRLWoOUzeIZyH5NOyRwNcN89io91syZkZxNmYRYbfcm1PDHKurYS9RYxpeRlaqqzRSoBIqsCA2h3LdCtUWIUQm4vbP5hFbOeR4HQWmJ5DVoPd43Itr1AfzKezYfYvBDGiC_GVpC1Xy3yizbDcGm0T_TrkXNU1-2gRJnIEtTRgom-20OTyMucQgetqKThLwm1IsuoaxWTynCm4YcVcCDbcnZXpd4Tq7N7Xh2cDZp0bNdblXxkn4WRrP_ENPooodZ4vscUMkbcmJOam-EArtlXxffMVRbo_0vc5if9-UWiW4B03iq9Y4tlONZrM-3F4eppT0igmoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت سردار سپهبد پاسدار شهید حاج محمد پاکپور
🔹
مراسم بزرگداشت معمار امنیت پایدار، فرمانده سلحشور، خستگی‌ناپذیر و مردمی کل سپاه پاسداران انقلاب اسلامی، سردار سپهبد پاسدار شهید پاکپور پنجشنبه ۷ خرداد ماه ۱۴۰۵ در مسجد پیامبر اعظم شهرک شهید محلاتی تهران برگزار شد.
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438493" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esGj3DmITrBRFBxqTDyV_qDVHLgRu1BTgrbf4FoRW4g-YHDIEUgeP14WeKJRsY5oyWHMUit83gWBPNu45S9xwPTmcZFOlAOPDa1oZ2_15MBPFprPKRUVShsXvxiPGpKh0oW6fav-ythALNsup9RJIPwE29P--IO-mYXtkuh_A70itErZYNHYJNokdY0XNLlkBaJdNtiAL4LtMC_CPdIe8Q1NA9f5YPdetb35TnNK9umyqTaAFLnaufiT_smBIRj-vVZ_xLg2oVjMFXkNJ0AX8luWLnpe8HnCUNJqg1SKR6h1yJoK15k4b1yG9jLhewQTT97W5WZ2BFi0BkcrILqCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ارائه طرح‌های اختصاصی بانک صادرات ایران برای تأمین مالی تولید و اشتغالزایی در بازدید قربان اسکندری از شرکت لوله و ماشین‌سازی ایران
🔹
همزمان با بازدید قربان اسکندری، سرپرست بانک صادرات ایران از شهرک صنعتی شمس‌آباد، طرح‌های اختصاصی این بانک برای تامین مالی بلندمدت و تقویت همکاری با شرکت لوله و ماشین‌سازی ایران به منظور افزایش تولید و ایجاد اشتغال، مورد بررسی و پیگیری قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438492" target="_blank">📅 20:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ef50a486.mp4?token=dhRV4_EEhgKLxaiNzLiBObYJrJYUL5qWnkbFL4dfppac2R517H0JL4d5IKLQgfQF1yl-lFNzyk8qYCzLfdDOCpwhUw00oRJzuyJMfWtv2DrfwQOBsT1NwGK39bfhPaqwytuEWS-bqr3pp5I-2iPxU8T8gsSYLXw6nZLy8gRCrAyrp5g2m8v1W3qEG_7vdHYIigi1u9g_IUEB4SHzLiud3JOSyTkFfCRCcIgu7oNmg3THd-Ycv8qbXwJWyefRBg9xaTuI-kZijhtNkqayKdIkSJ7Gq0nAX4uwlhZ513XPz9A50ZPM6Ftjt_JLKEs8gksm2_GAmMkfBznjU-_sLPf8LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ef50a486.mp4?token=dhRV4_EEhgKLxaiNzLiBObYJrJYUL5qWnkbFL4dfppac2R517H0JL4d5IKLQgfQF1yl-lFNzyk8qYCzLfdDOCpwhUw00oRJzuyJMfWtv2DrfwQOBsT1NwGK39bfhPaqwytuEWS-bqr3pp5I-2iPxU8T8gsSYLXw6nZLy8gRCrAyrp5g2m8v1W3qEG_7vdHYIigi1u9g_IUEB4SHzLiud3JOSyTkFfCRCcIgu7oNmg3THd-Ycv8qbXwJWyefRBg9xaTuI-kZijhtNkqayKdIkSJ7Gq0nAX4uwlhZ513XPz9A50ZPM6Ftjt_JLKEs8gksm2_GAmMkfBznjU-_sLPf8LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک تعطیله؟ نه برای ما
😎
💡
پیشخوان‌های شهرنت بانک شهر بعد از ساعت اداری هم در خدمت توئن؛
از افتتاح حساب و صدور کارت هدیه
🎁
تا انتقال وجه، مسدودی یا صدور مجدد کارت
💳
و حتی خدمات صندوق‌های سرمایه‌گذاری
📈
همه‌ی اینا، راحت و بی‌دردسر، تا ساعت ۱۰ شب
🕙
بانک شهر، همیشه همراه شهروندان شهر
❤️
برای مشاهده آدرس پیشخوان های شهرنت
اینجا
کلیک کنید.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438491" target="_blank">📅 20:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438490">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/438490" target="_blank">📅 20:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438489">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab3f20a4e.mp4?token=hSVi_NWFsM7ZaQb8MG8owa2R_WMnnSy9c3qJviNzj9S1AedR6EDf45tO0sONBKLzbPFeZyF3UG-bx2XkRpYuYwkn2Z0FmwfZ8IcqXvb_4yZB6cEJHxcppbpItAvMq6lKhu8eWk3hM_xx1A4sJGz3GGaJW8QRS9G7GqIMU3FbKpIGDoPGj2uYx1ID_uERd1hoQSDl-6rpdRfz45lIkVFx_DST7aFhr5ZwjQJIT9Tq9yuniV3KK5H7xtuM9G5XeXNrBUsaznbDWQoGjjSRDTVCM0nKB2xsWXTLsGMv3xZeXO_tqdsgVwBwiZvHHJqk4YTW8TXeSRM7SuBtCOpAST-DjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab3f20a4e.mp4?token=hSVi_NWFsM7ZaQb8MG8owa2R_WMnnSy9c3qJviNzj9S1AedR6EDf45tO0sONBKLzbPFeZyF3UG-bx2XkRpYuYwkn2Z0FmwfZ8IcqXvb_4yZB6cEJHxcppbpItAvMq6lKhu8eWk3hM_xx1A4sJGz3GGaJW8QRS9G7GqIMU3FbKpIGDoPGj2uYx1ID_uERd1hoQSDl-6rpdRfz45lIkVFx_DST7aFhr5ZwjQJIT9Tq9yuniV3KK5H7xtuM9G5XeXNrBUsaznbDWQoGjjSRDTVCM0nKB2xsWXTLsGMv3xZeXO_tqdsgVwBwiZvHHJqk4YTW8TXeSRM7SuBtCOpAST-DjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جبهه مقاومت باید با فشار نظامی، اسرائیل را مجبور کند که از لبنان عقب‌نشینی کند.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438489" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=VJQAamynF4Ro5H_rhMjbe7L8IivDK7cNlN8qJetH76GOSjEsne9FRNiC1ip8fwi7guCD2oOSre-IBgv-x78ZvyAot-r66uOk1Q45q9VRmnhSVEqlPYe6WpfQ0Dq4f3jU0bPEyuz4KCRM7tfu8nofgpouEDZCEdY7mdkNB49FxYj9CEXCVm17vbbNnPciz4mqUAextD92KAkhA7hkfso5IBVdtt4dqITVQ63jnNZQLt0ks54gT6JhqGwDV7EKbRAMJZwc2Y5puq5iyCkeyH_BEHUBvipPFNRDKJYIJXZb_lPf9nRRcfZ-Sph5-WQJWLgTORk3QBzSebVoUHg7IGVkRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=VJQAamynF4Ro5H_rhMjbe7L8IivDK7cNlN8qJetH76GOSjEsne9FRNiC1ip8fwi7guCD2oOSre-IBgv-x78ZvyAot-r66uOk1Q45q9VRmnhSVEqlPYe6WpfQ0Dq4f3jU0bPEyuz4KCRM7tfu8nofgpouEDZCEdY7mdkNB49FxYj9CEXCVm17vbbNnPciz4mqUAextD92KAkhA7hkfso5IBVdtt4dqITVQ63jnNZQLt0ks54gT6JhqGwDV7EKbRAMJZwc2Y5puq5iyCkeyH_BEHUBvipPFNRDKJYIJXZb_lPf9nRRcfZ-Sph5-WQJWLgTORk3QBzSebVoUHg7IGVkRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم
🔹
تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438488" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438487">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d043550950.mp4?token=bOs7IC8BIU6CBQqHR2-KO9PFWRx-pihHej834BGCGLhrwuaH6gthK5xd82Jfml-ycIF32e2SrqLPvBAQZRI0PdnDsQ1cvHv1etUlc0D3pu-B1q7yGXsLiGkdqi-MtZHnT-_3XywWTdPPWIyYyr9Wt_HC0T4wCBZkrabA9UNH5db_WQ3BEVGfY36zhG13dqiPv0W3Of4PpPMUvPj-9KJPRRdZu2NJyNuz4WqFmtHNrzXQehA7Xof1MpAU6i-Dk2PREtXLlH5SswoX_KWO4eSVYE60IHATa5NyYQjrYueE77nl7oP6_ThHVPRVzGrYsTPn0hsMo91hKuRHbDrQRnRWUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d043550950.mp4?token=bOs7IC8BIU6CBQqHR2-KO9PFWRx-pihHej834BGCGLhrwuaH6gthK5xd82Jfml-ycIF32e2SrqLPvBAQZRI0PdnDsQ1cvHv1etUlc0D3pu-B1q7yGXsLiGkdqi-MtZHnT-_3XywWTdPPWIyYyr9Wt_HC0T4wCBZkrabA9UNH5db_WQ3BEVGfY36zhG13dqiPv0W3Of4PpPMUvPj-9KJPRRdZu2NJyNuz4WqFmtHNrzXQehA7Xof1MpAU6i-Dk2PREtXLlH5SswoX_KWO4eSVYE60IHATa5NyYQjrYueE77nl7oP6_ThHVPRVzGrYsTPn0hsMo91hKuRHbDrQRnRWUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله تا داخل محل استقرار نظامیان اشغالگر رفت و آن را منهدم کرد
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438487" target="_blank">📅 19:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438486">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248fd81892.mp4?token=MZeXZFyQU_eu9hv5D_KWHtZJZMl7B3c1Oc5BQcAHL7coAZjVjC4_aF8DFaOnpKdYb0JcBBLvWycsv-MhbYg0QdTi477_11TjFDjs2jRupnZDc-pn2cYKLgk1zV0eHJubo2oe7cgWKyR6DrXGA42VxSfuJ3TZxNNr6L16O_GqzAmDJ17WFir0SQsIuHEBrZx45PMtXc27BcWXzJriagN4YDCDrDAqi1ejHEFJHtd6MnlPD_A270jcU_v5jpD0Fnoc33NaaW_bYjFyryVwAKrsFcRQEgAI4ojdFZTzILIX9ZIirGy8N0swlHpwky8-F5ojxwRntTS2hGwXqJwUXNGmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248fd81892.mp4?token=MZeXZFyQU_eu9hv5D_KWHtZJZMl7B3c1Oc5BQcAHL7coAZjVjC4_aF8DFaOnpKdYb0JcBBLvWycsv-MhbYg0QdTi477_11TjFDjs2jRupnZDc-pn2cYKLgk1zV0eHJubo2oe7cgWKyR6DrXGA42VxSfuJ3TZxNNr6L16O_GqzAmDJ17WFir0SQsIuHEBrZx45PMtXc27BcWXzJriagN4YDCDrDAqi1ejHEFJHtd6MnlPD_A270jcU_v5jpD0Fnoc33NaaW_bYjFyryVwAKrsFcRQEgAI4ojdFZTzILIX9ZIirGy8N0swlHpwky8-F5ojxwRntTS2hGwXqJwUXNGmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🔹
طرح و نقشهٔ کور دشمن پس از جنگ تحمیلی و فشار اقتصادی و محاصرهٔ تبلیغاتی و سیاسی، ایجاد تفرقه و تجزیهٔ اجتماعی برای جبران شکست‌های میدان نظامی و به زانو درآوردن ملّت است، و لازم…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438486" target="_blank">📅 19:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438485">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96a4b128c.mp4?token=oT3o-1C0vkz3nq8m3_4UGgYqemXbVciJkbSeppLDnHbaAp3WJxVdeMevj0V9ErzfuxkPwMrVNenWrWMOUA0WPkJj8I6hDSFxjwxI9xFjpzIWqMNuDv9Cyr18ajmC4UNy1uQhunh5EO14iK1y5d-HUpqqNQoFyWNrqC4K-EzvKLBh_Rv-oUVQRptycYjwQDv1CUB5Gpvih5E6sfAa9T_Hqy4qXGd6bht1MAN57p-qpUDArYPhkhlBYUdR0_C5Uhrmj-xKa6isKETUhum5xwTkaOFeZi2Th5BmfHiHmoEQm0Pbp1LiX4Tfi1jUZsUvMeeFGqAvv5UGBXqHYG2K-4Bibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96a4b128c.mp4?token=oT3o-1C0vkz3nq8m3_4UGgYqemXbVciJkbSeppLDnHbaAp3WJxVdeMevj0V9ErzfuxkPwMrVNenWrWMOUA0WPkJj8I6hDSFxjwxI9xFjpzIWqMNuDv9Cyr18ajmC4UNy1uQhunh5EO14iK1y5d-HUpqqNQoFyWNrqC4K-EzvKLBh_Rv-oUVQRptycYjwQDv1CUB5Gpvih5E6sfAa9T_Hqy4qXGd6bht1MAN57p-qpUDArYPhkhlBYUdR0_C5Uhrmj-xKa6isKETUhum5xwTkaOFeZi2Th5BmfHiHmoEQm0Pbp1LiX4Tfi1jUZsUvMeeFGqAvv5UGBXqHYG2K-4Bibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: دشمن در جنوب لبنان بزرگ‌ترین ریسک تاریخ خودش انجام داده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438485" target="_blank">📅 19:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438484">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74263a0709.mp4?token=IlR3coMJa3IaSUG4yRuwwl_oJd99-T37qwqp6meyJ94Rsxq2NkwEBRp2PnaC6MbS88ZfunB8oGBouD6SfolbrUmoOGBpzsVS0Db5TxUEmh69Pjir-eX1-cE-jVXcwF-N15yTciqK8TKJz2W8HVpArCm_mp2xGxc8KQOvb2ywsuByiyKv6qSV_2VAnEnEshhD1XLXpT1_jkk6A_BYPTDnY0Zm1J8dGiOq_n_qPnxsEgjzxGLHO33AZA4moLFoVxeBPJbIKNlLGljABOqJQYNWH8OjrvYWtA-KAxx8G0Cv16hGN2H-FkWk3zO-Yfu8TA2_2WrplDZ3gmdVdOD_htlCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74263a0709.mp4?token=IlR3coMJa3IaSUG4yRuwwl_oJd99-T37qwqp6meyJ94Rsxq2NkwEBRp2PnaC6MbS88ZfunB8oGBouD6SfolbrUmoOGBpzsVS0Db5TxUEmh69Pjir-eX1-cE-jVXcwF-N15yTciqK8TKJz2W8HVpArCm_mp2xGxc8KQOvb2ywsuByiyKv6qSV_2VAnEnEshhD1XLXpT1_jkk6A_BYPTDnY0Zm1J8dGiOq_n_qPnxsEgjzxGLHO33AZA4moLFoVxeBPJbIKNlLGljABOqJQYNWH8OjrvYWtA-KAxx8G0Cv16hGN2H-FkWk3zO-Yfu8TA2_2WrplDZ3gmdVdOD_htlCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمود کریمی: حامل ۳ پیام از رهبر انقلاب برای این مراسم هستم
🔹
خانوادهٔ رهبر شهید در ثواب این روضه شریک هستند.
🔹
میدان و خیابان را رها نکنید.
🔹
از شهید صادق زرین یاد کنید. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438484" target="_blank">📅 19:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e199577f.mp4?token=cndeqr0Xg7mtM6V9aIvrF-W0dzUYKbmkJBIcOjr5OXMLG6YKjmlR6Ae_9RtXZIGiN2mEBIZc3ttuGQkgsNIpVj06Us9wupkwE-gMp0sKgm0nyU70rYrIyEmztTe8-yV_xWa7x2XRk_UJ5oqCKjje25ON3wYQ32R4-1D2x2w_6w9R9BkbIsU2hGYWIrLGdde8asYQsMS56R3Y0oGs4iOWx-k4T_wQN1Jinm35-89tiQvMS33E_7D_7GeowT5OOS52RE5jk9epcnhvnGiacqM4E7SBeXGbKRVFmHfSrLpunRyEGq6ZptnnyRhUvsU_s1cHQKmk_mVxIQ75Wgwm0q_5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e199577f.mp4?token=cndeqr0Xg7mtM6V9aIvrF-W0dzUYKbmkJBIcOjr5OXMLG6YKjmlR6Ae_9RtXZIGiN2mEBIZc3ttuGQkgsNIpVj06Us9wupkwE-gMp0sKgm0nyU70rYrIyEmztTe8-yV_xWa7x2XRk_UJ5oqCKjje25ON3wYQ32R4-1D2x2w_6w9R9BkbIsU2hGYWIrLGdde8asYQsMS56R3Y0oGs4iOWx-k4T_wQN1Jinm35-89tiQvMS33E_7D_7GeowT5OOS52RE5jk9epcnhvnGiacqM4E7SBeXGbKRVFmHfSrLpunRyEGq6ZptnnyRhUvsU_s1cHQKmk_mVxIQ75Wgwm0q_5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جنگنده‌های اسرائیلی حملهٔ بزرگی به بیروت کردند و خط قرمز را شکستند.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438483" target="_blank">📅 19:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438482">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8587c2b060.mp4?token=iibpne0Qzkf4p3pGanCjhpO8TdSZUoryRvq8B04paE8aKiZOi4tIv4SXDaRcZ9WSHA4v9Xkf5AOkDEav866Mjh6GDFyRy6pfhOsKZ5zFleHcETBivqNjI6UKFJOetzYrMqrzgUFvHbMvXR7BsE5ZJPuiq17dV8J21ubasXnF7FjBgvZ2eUVhhrj5WonRV43X85IOJh9aW7-sFz5jNekRr8e6miWXgXSgn7LCw_mZ5S_YySeCO4G0j8GZmJYpsQAuavb9a5jUZEnSTkE03Nci6T1ZlNLHrgUZRdUwxrkv-eB428VOQzlwOK4w_NArbo_WbqJ7JrxCp3NEzzAFmj9P8ROQv1vldqpLnKkvuPA2zKiVetoVRn62sIyNSMSDcyYMNNmYkybXfChNMU5AVIFeGPH-aDRIo4Yot5OA3bh1abt1FRJzAEOV2rzFMAh76vArNqkHiOtI76e7LOE6ol2ZxYZh_ABCGS-sVR2RWDChv0hYe964mzSII5kX2gc9E6y_G9eAhaLPkG6YjwNP340KRlC_GQ2NZInyxBZvvuhmY_4teaPuicVqlC1iE7BllzlEq7C5dCR9s-Tl-q-3SvSzyYj7sMd-ppx4EhL6qM7syYLSHdQRMEEY8yQc4mK9_iMGp2k2t35I1qQGjnnYfL84HBgWDEqx2SCebiBegjPcAn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8587c2b060.mp4?token=iibpne0Qzkf4p3pGanCjhpO8TdSZUoryRvq8B04paE8aKiZOi4tIv4SXDaRcZ9WSHA4v9Xkf5AOkDEav866Mjh6GDFyRy6pfhOsKZ5zFleHcETBivqNjI6UKFJOetzYrMqrzgUFvHbMvXR7BsE5ZJPuiq17dV8J21ubasXnF7FjBgvZ2eUVhhrj5WonRV43X85IOJh9aW7-sFz5jNekRr8e6miWXgXSgn7LCw_mZ5S_YySeCO4G0j8GZmJYpsQAuavb9a5jUZEnSTkE03Nci6T1ZlNLHrgUZRdUwxrkv-eB428VOQzlwOK4w_NArbo_WbqJ7JrxCp3NEzzAFmj9P8ROQv1vldqpLnKkvuPA2zKiVetoVRn62sIyNSMSDcyYMNNmYkybXfChNMU5AVIFeGPH-aDRIo4Yot5OA3bh1abt1FRJzAEOV2rzFMAh76vArNqkHiOtI76e7LOE6ol2ZxYZh_ABCGS-sVR2RWDChv0hYe964mzSII5kX2gc9E6y_G9eAhaLPkG6YjwNP340KRlC_GQ2NZInyxBZvvuhmY_4teaPuicVqlC1iE7BllzlEq7C5dCR9s-Tl-q-3SvSzyYj7sMd-ppx4EhL6qM7syYLSHdQRMEEY8yQc4mK9_iMGp2k2t35I1qQGjnnYfL84HBgWDEqx2SCebiBegjPcAn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ هدفمند رژیم صهیونیستی به بیروت  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438482" target="_blank">📅 19:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438481">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/149889b796.mp4?token=j-41FzQtM3Ygc0YYScZjQtJXGic5Ee80ivYLqlCRsLr6dgRXr4L5zoHfaQBur_JNWElrI0uTYMevCgx9vwrNx_kR9nY5i758uCvclkdWRnl2ShAG_iMM-MgbD8glIgop5DdE4QVIUDxtzzro_-5tV9BX_HVFNKjobFVYnj4QezZ4rMxFQUKXjf9qTseXy81RG4b4YrZ5vE7CNFf8Agh57-6KwkC6PtHWFlQ5lbiEr1vjgoiXFXeTxh7mlRtPS5U_3N8h60np_tir2_-N3yNon6dPa6P9xqU6bkMszKvgP3XpkRMIWF91Rfrhb6SqaOC2kGxJtFKiGLiQZ-KPRRns1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/149889b796.mp4?token=j-41FzQtM3Ygc0YYScZjQtJXGic5Ee80ivYLqlCRsLr6dgRXr4L5zoHfaQBur_JNWElrI0uTYMevCgx9vwrNx_kR9nY5i758uCvclkdWRnl2ShAG_iMM-MgbD8glIgop5DdE4QVIUDxtzzro_-5tV9BX_HVFNKjobFVYnj4QezZ4rMxFQUKXjf9qTseXy81RG4b4YrZ5vE7CNFf8Agh57-6KwkC6PtHWFlQ5lbiEr1vjgoiXFXeTxh7mlRtPS5U_3N8h60np_tir2_-N3yNon6dPa6P9xqU6bkMszKvgP3XpkRMIWF91Rfrhb6SqaOC2kGxJtFKiGLiQZ-KPRRns1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکی که با آرزویش در برنامهٔ محفل همه را غافلگیر کرد!
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438481" target="_blank">📅 19:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438480">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjzMVtXX3AZ9HCUFNXbQNJ6W9N2Cx3fyP0nv6lLLqeqixqZ78S3Yju9s6NmFPBV5rYzg7dLvGF69J240Pfda6vlafG-ErKiqdbNpgirYV9MDxycO3uRc4ZcBMw59otEe-Loj53xgenwZfGw7aLPrHP2nE696O-bbxdaykHWi65g_Rs_uB1VJ6OBmZJYMlzY1eiZVRIfGvOKk9NbaNTpUKaACI9vVaNDVzczy5O569hBxNjeJYbPEsDPE-nNCc_G0dqKA7nxtsQNf7rmP96G779jVQqgKnU4ITrWhnJmUT8zbH-S2INlMBfRKkYbQzk1GR9q0pM7ONpk7Czxepv-WEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج‌فارس، در فهرست سیاه آمریکا
🔹
در ادامۀ دشمنی و مواضع ضدایرانی آمریکایی‌ها، دولت ترامپ از تحریم سازمان تازه تأسیس «نهاد مدیریت آبراه خلیج‌فارس» خبر داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438480" target="_blank">📅 18:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438479">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d011e645e.mp4?token=bdDojDcRaNsmDt9kKEzTc5EPHQBs0iUIsb0cbl0XM5_LOywsH2i_0ChksrZqCTWwep3dIgdQdPa6DQpF69oBhMug_DkE7QeSseFO95x1ijiFC9k78xDDHGxGGMZ6JkDZpKNUUQ4-xBQBL7YKu7GtVSDOfrX3NlAphse-JJkHIQrFFlcNBbbto31KvWzbvVBcxpq6on_LkmvgwtB6B0ReiGUUT__WU2NhAE7SqRRHZn3XIuTT9o_bBwEUSXHQIhb417P1EjyLUxrIAiCg1b2MBH9fjfzE3nkPjh1NclGDCO3T-TR6BjeoFAR-1dbG0arHOb7QvIvB5yDRs5ZsUeqRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d011e645e.mp4?token=bdDojDcRaNsmDt9kKEzTc5EPHQBs0iUIsb0cbl0XM5_LOywsH2i_0ChksrZqCTWwep3dIgdQdPa6DQpF69oBhMug_DkE7QeSseFO95x1ijiFC9k78xDDHGxGGMZ6JkDZpKNUUQ4-xBQBL7YKu7GtVSDOfrX3NlAphse-JJkHIQrFFlcNBbbto31KvWzbvVBcxpq6on_LkmvgwtB6B0ReiGUUT__WU2NhAE7SqRRHZn3XIuTT9o_bBwEUSXHQIhb417P1EjyLUxrIAiCg1b2MBH9fjfzE3nkPjh1NclGDCO3T-TR6BjeoFAR-1dbG0arHOb7QvIvB5yDRs5ZsUeqRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر خیره‌کننده از حضور بی‌نظیر مردم ارومیه در تجمع شبانه
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438479" target="_blank">📅 18:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-48.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/438477" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-47.pdf</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438477" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0520652d2.mp4?token=TpnVRbj_ohsys1Fdem-9TTTmao2cOjoggU7PTXQ0QAW-GKH6DAocGE8zz1R-8hbWcPKtEvZGh8SFd-1kb74o8rEsS6mgwnx3WEBlbJv-fs35QzlOpk8GJSYlwQzVMhGbGkAB_R4KwXhrkx3jQwOsN2Hep8WXGNv-BEXnAzjR16K8aI-MZqbQa6KxbnUAbiQs42WlShI3Qm0xlUMjVn8FhTtvLiKBKU04g_LDuasUwGpbfKkcuRE7uHwB1-XkkTGk1a8VZjqczVX-GvSKDbXIruteej2v_bw-eKJigszgL-3vrO1HLFb7sJ2cEfDxR4qZD3cGGhFMB_ryQojpC6BemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0520652d2.mp4?token=TpnVRbj_ohsys1Fdem-9TTTmao2cOjoggU7PTXQ0QAW-GKH6DAocGE8zz1R-8hbWcPKtEvZGh8SFd-1kb74o8rEsS6mgwnx3WEBlbJv-fs35QzlOpk8GJSYlwQzVMhGbGkAB_R4KwXhrkx3jQwOsN2Hep8WXGNv-BEXnAzjR16K8aI-MZqbQa6KxbnUAbiQs42WlShI3Qm0xlUMjVn8FhTtvLiKBKU04g_LDuasUwGpbfKkcuRE7uHwB1-XkkTGk1a8VZjqczVX-GvSKDbXIruteej2v_bw-eKJigszgL-3vrO1HLFb7sJ2cEfDxR4qZD3cGGhFMB_ryQojpC6BemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌نوشتهٔ سیدمحمدباقر حسینی خامنه‌ای، فرزند رهبر انقلاب و نوهٔ رهبر شهید خطاب به مادر شهیدش توسط یکی از هم‌کلاسی‌هایش خوانده شد  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438476" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b107b539.mp4?token=RA265Cr8KR4Kgtjq54OHqbCwHfMLJaVcCIVSgpTEnZ4ZNAHBmgvBDBP4X3jwBPYmrk9gnQcuauFYuhwIEyhVqILOi3xBKLqO-_yKpP43iCThh_OqsrL8DOG5s6kq8QXvJolgQWdiqgdpr7yjUHaAUZDnmLV22Cc3RVqJzE_u13eKAH77_Unp2Q0QpynRWmDz9xWm6nbRZbe0yW3c0f9kGPfZZMx4jZb1z6IS5PPWKoof5gImF3xITGAA5CZh2Pa2pKxa1UsALXp2vTQ6Pzr1IfxEoQdqhLR_jpHRCa9DY8YRuo9ttKqLX0gXspJyCF5UthHCj6a0KNN2Nq3rMGYSTZIYk1tVHdWPA31lLQL-j7SF4vw8cZhLsSR35yO2Fl4eYwefdxRbTLfQQgH9RZtcZuqD3u2n__EG8gr807VziLLliXAPMrtbkNpDNt8gHEXzL8wwpzJ8mim7SvbfnaPacqS9HMMTt5zAwhJPhYzDJWCj07ASBu8FU-8xJiA_i-UsyAG3qOmccVPavxMuXKBSSNrpGHU7tKh-htJwqIJ0hhhmfHlFXIeFsyNMKFJVYXQqVT-llNpLETh3yC3zS19GF3ZtJqBi8E1V9-4CjkXAG2AhjHEzK5xGzeCpQWfJUsvwISZ45jpAQB2_EdsT67RM2FXJjli74zWQfc7iQgNV3-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b107b539.mp4?token=RA265Cr8KR4Kgtjq54OHqbCwHfMLJaVcCIVSgpTEnZ4ZNAHBmgvBDBP4X3jwBPYmrk9gnQcuauFYuhwIEyhVqILOi3xBKLqO-_yKpP43iCThh_OqsrL8DOG5s6kq8QXvJolgQWdiqgdpr7yjUHaAUZDnmLV22Cc3RVqJzE_u13eKAH77_Unp2Q0QpynRWmDz9xWm6nbRZbe0yW3c0f9kGPfZZMx4jZb1z6IS5PPWKoof5gImF3xITGAA5CZh2Pa2pKxa1UsALXp2vTQ6Pzr1IfxEoQdqhLR_jpHRCa9DY8YRuo9ttKqLX0gXspJyCF5UthHCj6a0KNN2Nq3rMGYSTZIYk1tVHdWPA31lLQL-j7SF4vw8cZhLsSR35yO2Fl4eYwefdxRbTLfQQgH9RZtcZuqD3u2n__EG8gr807VziLLliXAPMrtbkNpDNt8gHEXzL8wwpzJ8mim7SvbfnaPacqS9HMMTt5zAwhJPhYzDJWCj07ASBu8FU-8xJiA_i-UsyAG3qOmccVPavxMuXKBSSNrpGHU7tKh-htJwqIJ0hhhmfHlFXIeFsyNMKFJVYXQqVT-llNpLETh3yC3zS19GF3ZtJqBi8E1V9-4CjkXAG2AhjHEzK5xGzeCpQWfJUsvwISZ45jpAQB2_EdsT67RM2FXJjli74zWQfc7iQgNV3-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزار مرتبه جانم فدای خامنه‌ای...
🔹
مدیحه‌سرایی مصطفی سماواتی در مراسم یادبود شهدای خانوادۀ امام شهید و رهبر انقلاب اسلامی  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438475" target="_blank">📅 17:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83d18d28d.mp4?token=epYeTwisuPXYZKlcJbDJMXbY7Lc8WQ9lAsaPmy8LPQEyYwVSySulAKkEhJV1en_0NsigZjL8PlR3FDJobbudZ3Ya_txJEV431GuI0Gw2OagGdWRERSwuTWMyeBWE4vuJ8l3v1Z0TpvyjK2jzQroiMCZQweUmNCzCe4EPvoUKSHp_90tFdp3OwXxcFfb5V-aTPStVeQ0JGUPRvza90Gk4nnbFFZdBhc1SKzvUCTAyhtIw6yfVVkTuxHYt6tcmhIZvGJn98rw7Lwc8ixa4Z4x0XJjRP3E2qdHQ7nkd-ihQsyADRvbuEUI2n1B5jfz16-OkHvTJloTGY86tj11JQeXkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83d18d28d.mp4?token=epYeTwisuPXYZKlcJbDJMXbY7Lc8WQ9lAsaPmy8LPQEyYwVSySulAKkEhJV1en_0NsigZjL8PlR3FDJobbudZ3Ya_txJEV431GuI0Gw2OagGdWRERSwuTWMyeBWE4vuJ8l3v1Z0TpvyjK2jzQroiMCZQweUmNCzCe4EPvoUKSHp_90tFdp3OwXxcFfb5V-aTPStVeQ0JGUPRvza90Gk4nnbFFZdBhc1SKzvUCTAyhtIw6yfVVkTuxHYt6tcmhIZvGJn98rw7Lwc8ixa4Z4x0XJjRP3E2qdHQ7nkd-ihQsyADRvbuEUI2n1B5jfz16-OkHvTJloTGY86tj11JQeXkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امنیتی وزیر کشور: شهید پاکپور میدانی‌ترین فرمانده تاریخ ایران بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438474" target="_blank">📅 17:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm0ytBfOM3MPUek0AdXhziLUECneeYzg8jkPF2qk0NDnxD7TnimxNT7BpsBNjSkzQLwMT5BJUf5wHul6OCBrwWx1JeIBJyCWeGzRhc--gsuDXsxYXWGaQNTWEfNqTlLIZ4A0kVsYk8T5k3FZrT62r3UsQKH0dA6Pd_5T-9DSQrpMxYeSPcwb7Ag-9rHxI-VD1Rewb0K8ZsH2Q4_zUz-wVwXiH7bPEKsNGTq_spBi9tYcJzlXgg8jzj7pwDKUkMdyrnMLqMTqdqDtv2diT1EdUHOO-hqnZMtkKGUoS2NU2VyuTMLbtuhVJRAj73ZhZYhoWSkNleWTaVsbJa0zOZsbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان روز ملی جمهوری آذربایجان را به علی‌اف تبریک گفت
🔹
رئیس‌جمهور در پیام تبریک روز جمهوری آذربایجان به رئیس‌جمهور این کشور نوشت:  ۲ ملت مسلمان ایران و آذربایجان دارای اشتراکات فراوان تاریخی-تمدنی، فرهنگی، دینی و زبانی هستند و این پیوند، دوستی ۲ ملت را مستحکم و استوار ساخته است.
🔹
پیوندهای گسست‌ناپذیر ما، سرمایهٔ گران‌سنگی برای توسعهٔ مناسبات میان ۲ کشور فراهم کرده؛ جمهوری اسلامی ایران پس‌از استقلال جمهوری آذربایجان همواره از توسعه و گسترش روابط مشترک حمایت کرده و خوشحالیم که در راستای خواست و آرزوی ۲ ملت، امروزه شاهد روندی پویا در روابط ۲ کشور هستیم.
🔹
امیدوارم که این روند پویا که طیف متنوعی از موضوعات دوجانبه، منطقه‌ای و بین‌المللی را شامل می‌شود، همچنان با قدرت و شتاب بیشتر ادامه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438473" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c1eea896.mp4?token=QJXytk0HIqhdzlbPVllBgSLpHMlTM9AMrZfQFjMUr2GaV0rG_XWVEsUeQJ0bghIo7CkbZmjiPdUwUsK7-pn4bqX5qQdVNNKJ_kzAsPobq8Tt16msJqKh10SmsLy5ERL5mDP5_bKytPOm07-LgdPPHAvEw6dKNnRjdPRtTUhsDLofaRHlQVeos1cKui3A4HaXoAZJ7TKljxZpZRVhc6YRc0SNn97IdF48JKZt5oemK82m8hDrJ0m8FgCmN44J9m23cvyU2yLCkuqkUQgqLN7S9ajHUyu5OfDnv0xuGfLmgQwsOnLeue6ZKuQBiKsFyNsF62n2SCJTUj2hfdCOeWwjgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c1eea896.mp4?token=QJXytk0HIqhdzlbPVllBgSLpHMlTM9AMrZfQFjMUr2GaV0rG_XWVEsUeQJ0bghIo7CkbZmjiPdUwUsK7-pn4bqX5qQdVNNKJ_kzAsPobq8Tt16msJqKh10SmsLy5ERL5mDP5_bKytPOm07-LgdPPHAvEw6dKNnRjdPRtTUhsDLofaRHlQVeos1cKui3A4HaXoAZJ7TKljxZpZRVhc6YRc0SNn97IdF48JKZt5oemK82m8hDrJ0m8FgCmN44J9m23cvyU2yLCkuqkUQgqLN7S9ajHUyu5OfDnv0xuGfLmgQwsOnLeue6ZKuQBiKsFyNsF62n2SCJTUj2hfdCOeWwjgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون هماهنگ‌کننده سپاه: شهید پاکپور اعتقاد ویژه به مردم داشت  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438472" target="_blank">📅 16:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9834fbae49.mp4?token=dsiVdTDZS1FOW7Jzm2zFirJRW5wytRupuP5wVL3yYq_oCwnxTR2AF6jba7f1siQ_-_MxPR1UuofQ6VNVZ_nYFe3LqkkFza3-_XxbJ5mi3izy3fyFE4ooL_gFy_OaTq9GFa7ck6U2Fkg9FrqOBEVLTdcaxMD_nLjr006LCq7TcopjP-cHQf2-4mWWboEbWqTLvXXm1Chbneeex0WUvELyVS5iOgPCk56nYP1l3ygUJcxKqIssD97M1wlIQm4eC-tiBHoX6MobAFSe6m8yGZMRWey3b3mctf7RBN1trPfAPkf1I7QfyE4yZlaTW4W8FaYKC2v5K2kTyVeKD6zOnAzgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9834fbae49.mp4?token=dsiVdTDZS1FOW7Jzm2zFirJRW5wytRupuP5wVL3yYq_oCwnxTR2AF6jba7f1siQ_-_MxPR1UuofQ6VNVZ_nYFe3LqkkFza3-_XxbJ5mi3izy3fyFE4ooL_gFy_OaTq9GFa7ck6U2Fkg9FrqOBEVLTdcaxMD_nLjr006LCq7TcopjP-cHQf2-4mWWboEbWqTLvXXm1Chbneeex0WUvELyVS5iOgPCk56nYP1l3ygUJcxKqIssD97M1wlIQm4eC-tiBHoX6MobAFSe6m8yGZMRWey3b3mctf7RBN1trPfAPkf1I7QfyE4yZlaTW4W8FaYKC2v5K2kTyVeKD6zOnAzgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
مجلس يادبود شهداى خانواده امام شهيد را در پخش زندهٔ فارس ببینید  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438471" target="_blank">📅 16:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438464">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43311032d1.mp4?token=iBAZd3Mrs_JGcnXjFml6FerMLmGWZeFX6ADwf03rqfyIYPK1nAZ5yrvvSz8sV4EALQwrwwu3VqUi0X6zRqX7XGrC4_vvoj3Qw4c3VbN1wLI7hXtdAJT_68RoysXwPMP0csCnAN2kHdVk2gQyFO8Kp-Xr4D_haqPp3VOaU3X51TEv2jkYEfU1f2yml4TbC2F43nmoRXHZi24fftts6IfH9Iw0asThnaCV2P78hV4PBzJAWjAMQSe2JMlU26kled8HURvM_6Bni5HArdbVX16qI4E_2iUA7QXqT4JcqpaidzOk4J5yOZHXi7MSwTOMUcJIWNJdzBtk3U9yGVtfWG3Skw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43311032d1.mp4?token=iBAZd3Mrs_JGcnXjFml6FerMLmGWZeFX6ADwf03rqfyIYPK1nAZ5yrvvSz8sV4EALQwrwwu3VqUi0X6zRqX7XGrC4_vvoj3Qw4c3VbN1wLI7hXtdAJT_68RoysXwPMP0csCnAN2kHdVk2gQyFO8Kp-Xr4D_haqPp3VOaU3X51TEv2jkYEfU1f2yml4TbC2F43nmoRXHZi24fftts6IfH9Iw0asThnaCV2P78hV4PBzJAWjAMQSe2JMlU26kled8HURvM_6Bni5HArdbVX16qI4E_2iUA7QXqT4JcqpaidzOk4J5yOZHXi7MSwTOMUcJIWNJdzBtk3U9yGVtfWG3Skw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام جزئیات اولین یادبود شهدای خانوادۀ امام شهید
🔹
آستان مقدس حضرت عبدالعظیم حسنی که پیش‌تر از سوی رهبر شهید به‌عنوان «قبلۀ تهران» نامیده شده بود، با نظر مقام معظم رهبری و بیت معزز شهید، میزبان اولین مراسم رسمی یادبود شهدا خواهد بود.​
🔹
این مراسمِ مردمی،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438464" target="_blank">📅 16:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55a46cd00.mp4?token=Iv3BkoTy7utUSVA-8N5mn--uqvmk11qdbNpIn_kFeE6MHrjkjf6jUL2SeO17z__Lt0dgRg9o1xnIUQH9qbuxVv3qgdEBzQhTNKPhrcHtsduO_SpTuZqBgBudDSgtl2IjyfTgNLsVpTsyVu_28OgKjmFU6H-R2sbUdn8XIqXtgstDsAXoObIXyWsliQh4EvyPqu0WOavFApLU0UzUc08-bkflRExHzPy0CSnSWTW6mGb2IUrdHHCb1HLyZu1Smd0m7MbZyMO014xajjlIHBdfXWxu_w6Xr-AYDM9PwXnwE9Qnhy1PKc-yLN7FU8bBvuZV4yYtencRK8676qX4nktIVQFR2eCpg7ynGxBuP36fDnML9ETaWDBDMWrxlNs--nd4o6U3uVotw2PXWr_IRtGryjz7evotkZZobdhw_a2WolJc_ipkUmFXzceavWUbAubT4sN3m0fDa969rYHeJq6J7SYh0Yt9WQjjKOFA3DDuYWJF4DqfG203giLxXpAriZDHcqgTFade3lrQXX0sTFSvFQCBPjhlgp73ax0YdEH0lpHg6Z53dkBHlu2Q-HLHR1TbEPG8iu46RBS8W4JsMIR3mLgpLdATitoiBEPSTGz343nCYrK9MTMKgu8JkwUrderyjGKvZqKFybBCqS-9SJ4NiSbCHpThvn27YYr8CZnMV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55a46cd00.mp4?token=Iv3BkoTy7utUSVA-8N5mn--uqvmk11qdbNpIn_kFeE6MHrjkjf6jUL2SeO17z__Lt0dgRg9o1xnIUQH9qbuxVv3qgdEBzQhTNKPhrcHtsduO_SpTuZqBgBudDSgtl2IjyfTgNLsVpTsyVu_28OgKjmFU6H-R2sbUdn8XIqXtgstDsAXoObIXyWsliQh4EvyPqu0WOavFApLU0UzUc08-bkflRExHzPy0CSnSWTW6mGb2IUrdHHCb1HLyZu1Smd0m7MbZyMO014xajjlIHBdfXWxu_w6Xr-AYDM9PwXnwE9Qnhy1PKc-yLN7FU8bBvuZV4yYtencRK8676qX4nktIVQFR2eCpg7ynGxBuP36fDnML9ETaWDBDMWrxlNs--nd4o6U3uVotw2PXWr_IRtGryjz7evotkZZobdhw_a2WolJc_ipkUmFXzceavWUbAubT4sN3m0fDa969rYHeJq6J7SYh0Yt9WQjjKOFA3DDuYWJF4DqfG203giLxXpAriZDHcqgTFade3lrQXX0sTFSvFQCBPjhlgp73ax0YdEH0lpHg6Z53dkBHlu2Q-HLHR1TbEPG8iu46RBS8W4JsMIR3mLgpLdATitoiBEPSTGz343nCYrK9MTMKgu8JkwUrderyjGKvZqKFybBCqS-9SJ4NiSbCHpThvn27YYr8CZnMV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون هماهنگ‌کننده سپاه: شهید پاکپور اعتقاد ویژه به مردم داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/438463" target="_blank">📅 16:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438461">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c73bcbed.mp4?token=Tfe-FYcCXtU6PYq_P_XlDvuvP9Er-3s6XY42bA9pnfdN8yxJAlgaanJlHiFnRQKaVZ8P7RPHdb4fTIUvQDiEjVBgBauDjXxutSKbGTQVrW9hcdRpStTRuqpnwUv3xtyTkcG6xFcv4tzbGCC8-4YIpNGH9Zw2RM5mZLKU4ykcp1K7kO5usjuRQ2YgieSZX7_HhkvSQOVFDJw_0DxxLOYC3akpHEpUKKV0pcyGFV-_dI1dzhdUuGzZlxcELJuJGKX6f4TM56E7JQw_GM6_uHSRoy9WxItYrkvAQ5vuFDTxapaIh6lskMF-0q8Es1xFObcsPlfiiTQG8LPreJ92aoplPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c73bcbed.mp4?token=Tfe-FYcCXtU6PYq_P_XlDvuvP9Er-3s6XY42bA9pnfdN8yxJAlgaanJlHiFnRQKaVZ8P7RPHdb4fTIUvQDiEjVBgBauDjXxutSKbGTQVrW9hcdRpStTRuqpnwUv3xtyTkcG6xFcv4tzbGCC8-4YIpNGH9Zw2RM5mZLKU4ykcp1K7kO5usjuRQ2YgieSZX7_HhkvSQOVFDJw_0DxxLOYC3akpHEpUKKV0pcyGFV-_dI1dzhdUuGzZlxcELJuJGKX6f4TM56E7JQw_GM6_uHSRoy9WxItYrkvAQ5vuFDTxapaIh6lskMF-0q8Es1xFObcsPlfiiTQG8LPreJ92aoplPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژهٔ ارمنستان با سامانهٔ ایرانی و پهپاد چینی
🔹
ارمنستان در رژهٔ روز جمهوری خود انواع تسلیحات و تجهیزات خریداری شده از ایران، روسیه، هند، فرانسه و چین را به نمایش گذاشت.
🔹
راکت انداز توس-1 (TOS-1) و سامانهٔ جنگ الکترونیک Pole-21 روسیه، تسلیحات هندی شامل موشک‌های MLRS پیناکا، هویتزرهای خودکششی «سزار» فرانسه و سامانهٔ پدافندی ارتفاع پایین مجید ساخت ایران، از جمله تجهیزات رژهٔ ارمنستان هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/438461" target="_blank">📅 16:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438460">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEEuBC9KInFZVImAe5oR1zWcQUM9FccESwdjdxEZmvcHelKZo3cZ7_6dgVbyLy3X3AeMtJgNuTB8f1c2uZUcizOK1dAqJgffSm03AEFQr8x14Da4zNxI-aJMWA_n7SE9lx4O2sdorXFIXT13MQX9cm-__IYN4ClkoODp8sDUPTKXOIUZIEsBoCAuLVR61nj26D2w8v_zk9tAwSaxOx6vbXuP5KQLVUV5f1NQbomrXWp46quTBTy4uC6nltvmnP2Pyr0xi9CWUyY5HMCOLhf2CdylolZ_V3bmIKKSoKVf4KmKLiZ1RwOBZaY9h-OPOayDKMaOz-TpXRzrl7YcywTkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتارهای ضدونقیض ترامپ زیر ذره‌بین روان‌شناسی
🔹
این روزها مردم جهان از حرف‌ها و تصمیمات رئیس‌جمهوری ملقب به «مرد دیوانه» بهت‌زده مانده‌اند و او را با دروغ‌ها و ادعای‌های ضد‌و‌نقیض‌اش مورد تمسخر قرار می‌دهند.
🔹
برخی‌ها نیز معتقدند که دروغ گفتن ترامپ و تغییر تصمیماتش در کسری از ثانیه، سیاستی است که او برای پایین نگهداشتن قیمت نفت، گول زدن جبهۀ مقابل و درگیر کردن اذهان عمومی استفاده می‌کند.
🔹
فتحی‌آشتیانی، رئیس انجمن ایرانی روان‌شناسی: ترامپ، شخصیتی خودشیفته دارد؛ با تمام ویژگی‌هایی که یک فرد خودشیفته ممکن است داشته باشد.
🔹
خودشیفته فردی است که خود را کاملاً قبول دارد و دیگران را به‌طور کامل نادیده می‌گیرد. از دیگران سعی می‌کند بهره‌کشی کند، دقیقا مانند رفتار ترامپ در برابر بسیاری از کشورهای عربی، مثل همان تعبیر معروف که می‌گویند او در حال «دوشیدن» این کشورهاست.
🔹
اگر برچسب «اختلال روانی» به ترامپ زده شود، مسئولیت کارهایش را تحت‌تأثیر همین اختلالات تفسیر می‌کنند و می‌گویند رفتارهایش ناشی از بیماری روانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438460" target="_blank">📅 15:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYUfnlbsin793WE8SomymNXL8LJ9EBxViZNojwQSPG3_jI7q5e_ZRCVzPP_jtcLrZ1STrGk8KwnYm2WoVKDT7eB3XfOSdWrp77IFaZ81iw1kRgDOhZQzxmTw4f4Ayu_ZjPaxj6RONGzNDxApF4ZYTWIbg6W-YYcrLQLVsBLqv9POsDeRC2G0eiM8RPmOpPUvKEtKYFTXDWzJSnkoKtfFeFLecWqHfQon4JWjd-xB-9-QVsUBpto8qYGrVsNM1kdCsJDMxmPzsU6sg6P4qx03ckGDszE2jUgvMd8ER_CP0PlRggdXsZoj1VzjuszE2C1NUSmEpGlXlrQj5lpotyQtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je4yvLe7heGAXpfQDis37NfHx6--taqR6CrG4978Rgg9ZhHARWnCt-yTI_3MZJLF3jSLwuE-u-yiVc0yjveatNVDeW8jeo2268WK7ZypU2X-2bAuJWVFdrwhaUjoFIet7__Uovl7sy09g1FYuWXDJREvAbLqmcov9jlDRyKpDJBu56znoYYmPhjnR0nFbM2QW9_O6mgC-lvvaVvLaPIXR8cQVogQ9Mk-H9p0SSiyTf1ZiTVqTV4nW-DUw4_xPgFoeCzgh7YSRCF-ITtJZUubCqevRShVEtAAAihuLk2Zyi5CFpII0me-tF09ahQotg-_h1JwmXbxCOcWc30XXXAo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH7FWZ4ADqIwCxmc2LX2fVW5sGpgeOJWYvcv_ML0nAYe04QOUsiEUvTicW8OTVQtT7uJvFaLASuJNuSLfs64_lvLPfYyRZzcyBj8M6UV28saox36gfceKVGeS8rC6qA-5kiHSxbPqCvEIzv5eYzPb5rdVKD2u6cb-Upskh4rf-XiNIj9KXpkL1BUMQkK_n18abfR20mQ3-re-o51PsQuDpdfwQi4BPvHU7WynJ1uTeNWIDImWi3I3XvpQZzQiIIkcG085xS6Yb2cQLCGDobRcy54N5vvNm-ijziR-z1sRMP0r_IZN0KhhlF_igyVabC1i_UMS1uLEiOCUaabd1UBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1pd7l7IMUNW-iNA4Qxx_x1ApH3D5q4iOqN_pMdhd41Eb6Z2p-fm6INpifZySGGjtG7HrmW9e0KGnQd67vx3ryCUUZc7B6jC2_1G2g4nNq8qkR9h-lBKNQFal6htnwVSkFKDknicUioU_guTG1KxHc7pgmnP0UFFWiPRqrVFElNjQiu5XTqPUY6n7c6tU4Tc6FnVya5nE0JuImwAtV2YMO8PshPRGHMOLk4gIzZRIxI9dOUkBI0b30OVsq5tq4r0qr-4bilr2NmhQcWpWELnEKHJIs1VSqGkn6tq6vrAqIfOhFPGNn-Qo9eTY8eO0cE6cAhfYtSVHgydAhyuLCgrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rU-RLVVs-N9UarNo8vUzorsBbKE_NI_KCWHaYImkUpMm87WcvBT9qymQFyZN7RFXJmk8NfcPOStKwvgig0n2KhgUZxOnt-Z12CdbRLw6_S5Wo9uxJrvCo1mBc2wWamRsivAHY9iL2zrvTId0gwe_xxZKuEtUK9X1q-o6mnmDksd0p9cAhgXyXFv165MgfmPmySbQVqjzqdyGTmJlV4QPhpwUckXK2Nt_PstAzx5YmicsRk7DkCqmLxMMIqwH3JRDyuL2DO3BEhTwcILFcsLlsEMCxWIk_raLwjtwZboGmdOt8mKMhlminmvfr6egU2DJOGbqAgqoh-7ziqLULNv1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juYVaplwhIxaVfLdKIr1cnFWfPqgdGyif26AidoTFbjunioRedcqowQr8ThAtXedNjDfBi9qS8BT-dmIar8CMk__zmoyUaLWKSeKbmFqd8F-AVR6bP6453HOsdqmvHb73xX4pbk9DL7Kzcsm9YHnIyK_39YpinM7Wh1fJLYYqNNz9-qXfaTS6tk7IN9511UxV8slXhOGUE5lFd75ceucd_fDLp5EWbV5WrBarI-m9kvIfKd8vvIxh3olU9Vd4ae105JifOVKceDMR1qb0iDFWAeHLatHHdhmDO9CI6Q7qlVJJwe91mIZPu1f7VBx2amaIFhMRvwhXYLkR0MXt1oNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftA2O_cuZFVazQ0fyEyteQBZ_M6N-Kee2RlWHJW08rJSleYNh2rhsePnX9LICN2YVP5sZSAwOEyYCaNsWMCvSp03fy-bbD5yygJBVkAuRLFMHDbnMWjmOrxI0931TvGFVfqGSU9r_GKsjlvOyt7TaJdPvhpncBE6YmN-rLwjFAzmh3DYYaA-CAEFVcNIiXwfIy7F2gq5rnZXQ08VPaTJ2b42cLWqcRaLz3zg62GgaCybP6pbODQUTIpsIeFcxWEXRl-Pmy6KzLSgEUj8XZyMlHRjFAcHZItEuQAliRSCjQjMHYpMTm2EUXblDOu1oeMSo7cquAGrbCEijEKeygfNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«اردی‌بهشت کتاب» تمدید شد
🔹
رویداد «اردی‌بهشت کتاب» که با شعار «در هوای کتاب‌خوا‌ن‌ترین رهبر دنیا» در باغ کتاب در حال برگزاری است تا پایان فردا تمدید شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438453" target="_blank">📅 15:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0370276cb1.mp4?token=hnle2TUeWBz6vPtw802bKz48durmASeqSw9kccpBGHNDt6RWJQE0yfva9MS43WU_FiWDIIhnUzL03mzX4fL74r0T_DRm6LuW-bnVDIgfQAjo8MZNa65jzeyE61YjUld0dXWWq6UV1S1romS-b7jeSv3PBefhrB2w30Wsg785aTqhq1OMmM0YLpZAAhowtNInE2anOiEtSMSGRAEnUJo0gARtQyXkgT5DwfCrMBriXrVg-yrX-aIE68weM27dfAPZCDSWiEw4nexA4OV8_yKu5d2SycKSr8eQfZVCcGVNGvPK1PwSib8kvWrJpaEHkeSxm12pBi9wS-fr6AYg4ceE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0370276cb1.mp4?token=hnle2TUeWBz6vPtw802bKz48durmASeqSw9kccpBGHNDt6RWJQE0yfva9MS43WU_FiWDIIhnUzL03mzX4fL74r0T_DRm6LuW-bnVDIgfQAjo8MZNa65jzeyE61YjUld0dXWWq6UV1S1romS-b7jeSv3PBefhrB2w30Wsg785aTqhq1OMmM0YLpZAAhowtNInE2anOiEtSMSGRAEnUJo0gARtQyXkgT5DwfCrMBriXrVg-yrX-aIE68weM27dfAPZCDSWiEw4nexA4OV8_yKu5d2SycKSr8eQfZVCcGVNGvPK1PwSib8kvWrJpaEHkeSxm12pBi9wS-fr6AYg4ceE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: در حال حاضر، به‌دلیل جنگ آمریکا با ایران، وضعیت تأمین موشک‌های سامانهٔ پاتریوت پیچیده شده است
🔹
دراین‌خصوص به رئیس‌جمهور و کنگرهٔ آمریکا نامه ارسال کردم و در آن چگونگی تأثیر تأمین تعداد کافی پاتریوت‌ها بر پایان جنگ اوکراین را تشریح کردم.
🔹
اروپا باید در قارهٔ خود، از تمامی ظرفیت‌های لازم برای محافظت برخوردار باشد. ما به پدافند دفاع موشکی بالستیک بومی اروپا، به تعداد کافی و با قابلیت‌های لازم، نیازمندیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438452" target="_blank">📅 15:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">شکایت بین‌المللی پرسپولیس برای تغییر جدول لیگ/ قرمزها امیدوار به ۲ امتیاز
🗣
باشگاه پرسپولیس همچنان پیگیر پرونده مربوط به دیدار با ملوان است و مدیران این باشگاه اعتقاد دارند استفاده از سینا خادم‌پور در ترکیب تیم ملوان غیرقانونی بوده و این مسابقه باید با نتیجه ۳ بر صفر به سود سرخ‌پوشان اعلام شود.
🗣
مسئولان باشگاه پرسپولیس در روزهای اخیر با ارسال نامه‌ای به دادگاه عالی ورزش، خواستار توقف تأثیر امتیازاتی شدند که تیم‌های استقلال و تراکتور از بازی با ملوان با رای انضباطی کسب کرده‌اند.
🗣
از نگاه مدیران پرسپولیس، این امتیازها به‌صورت مستقیم در جدول رده‌بندی تأثیرگذار بوده و تا زمان تعیین تکلیف نهایی پرونده نباید در جدول لحاظ شود.
🗣
شنیده می‌شود دادگاه عالی ورزش نیز دراین‌خصوص مکاتبه‌ای با فدراسیون فوتبال ایران انجام داده و از مسئولان فدراسیون خواسته توضیحات و مستندات خود را ارائه کنند. گفته می‌شود قرار بوده فدراسیون فوتبال تا امروز پاسخ نهایی خود را به این مرجع ارسال کند.
🗣
در پرسپولیس خوش‌بینی زیادی نسبت به سرنوشت این پرونده وجود دارد و مدیران این باشگاه امیدوارند در نهایت یا امتیازهای مربوط به دیدارهای ملوان مقابل استقلال و تراکتور دستخوش تغییر شود یا ۲ امتیاز به پرسپولیس اضافه شود تا به اعتقاد آنها عدالت در جدول رده‌بندی رعایت شود.
🗣
بااین‌حال، هنوز هیچ تصمیم رسمی و قطعی از سوی مراجع ذی‌صلاح اعلام نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438451" target="_blank">📅 15:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
سپاه پاسداران: جز با محو رژیم صهیونیستی، منطقه روی آرامش نمی‌بیند
🔹
بیانیۀ سپاه پاسداران به‌مناسبت شهادت دو تن از فرماندهان مجاهد و غیور حماس: شهادت «مجاهد محمد عوده (ابوعمرو)» به همراه همسر ام عمروو سه فرزندش «یاسر، یحیی و جمیله» در حمله هوایی رژیم صهیونیستی به شهر غزه و نیز شهادت «عزالدین الحداد (ابوصهیب)» از فرماندهان کتائب شهید عزالدین القسام را که نزدیک به چهار دهه با صهیونیست‌ها مبارزه کرد، بار دیگر پرده از ماهیت درنده خویی و شیطان صفتی رژیم پلید، جلاد و تروریست صهیونی کنار زد.
🔹
سیاهۀ جنایات حدود ۸ دهۀ رژیم جعلی و غاصب صهیونیستی بار دیگر این حقیقت را به جهان بشریت به‌ویژه مدعیان حقوق بشر و آزادی ملت‌ها تأکید می‌کند «جز محو این رژیم کودک‌کش و اهریمنی، از روی زمین، منطقه غرب آسیا روی آرامش نمی‌بیند و طرح‌های موسوم به صلحی که رئیس‌جمهور خبیث و قمارباز آمریکا از آن حرف می‌زند، جز کشتار، قتل و ترور نیست.»
🔹
شهادت این فرماندهان سرافراز نه تنها مقاومت را تضعیف نخواهد کرد، بلکه باعث تداوم جهاد تا آزادی فلسطین و قدس شریف خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438450" target="_blank">📅 14:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
🔹
نیروی دریایی سپاه: کنترل هوشمند تنگه‍ هرمز با اقتدار کامل درحال انجام است و طی شبانه‌روز گذشته ۲۶ کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگهٔ هرمز عبور کردند.
🔹
دریافت مجوز…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438449" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bac5da19d.mp4?token=MQMZ2NyQCYrrXWQB4arEIS7AuxvgH66W4xlef1GhwS0AFtqYXxf1U82pnE29WNdvnaIfrfRjxXAIQbQuS3vzvB8987HF5We8CBey6WXSksnSbYMToS-dn-VXE6LoCiphQH9yOkLYSItoSegrwQ7VltEiwi4Aam0VtpHGeuA16je07r-fkvvA6GlZVJKKcGHtdvhRwEM0xblVrKq1MEnSHwVu28Gs0yOlNufBmj6P5lksvxSTha3r_K_0UAoHWF_IKTauTDqcde0gda4qNmoy2A5uMZC5MuhWO9k8_lctYIBK6d-TjbuqrUkXhUyronkVd6IqDKX1DLU_NNZzOpV-sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bac5da19d.mp4?token=MQMZ2NyQCYrrXWQB4arEIS7AuxvgH66W4xlef1GhwS0AFtqYXxf1U82pnE29WNdvnaIfrfRjxXAIQbQuS3vzvB8987HF5We8CBey6WXSksnSbYMToS-dn-VXE6LoCiphQH9yOkLYSItoSegrwQ7VltEiwi4Aam0VtpHGeuA16je07r-fkvvA6GlZVJKKcGHtdvhRwEM0xblVrKq1MEnSHwVu28Gs0yOlNufBmj6P5lksvxSTha3r_K_0UAoHWF_IKTauTDqcde0gda4qNmoy2A5uMZC5MuhWO9k8_lctYIBK6d-TjbuqrUkXhUyronkVd6IqDKX1DLU_NNZzOpV-sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش پربازدید نشریۀ آمریکایی آتلانتیک از علت شکست ترامپ در حمله به ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438448" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeece2279c.mp4?token=Q2TwiciSAyAny5KZWzbmA8qOwT-5M2v2prOPrjzMarcOyrRS_tqbK73fVVUeX5m3-V7wbsBB_NJCo1X2HfWlchYrAvyLz_ujAoodfCrAhK53va41-xejCxErdJJFz-JyzVhGVLU48uOolvrfgK1ES-XueDwdOjd00UG0W41IFHu5VFrdP7884FardnuF2UDn7G_Ob5B19-a1WZVs89GsbpNLr23tPOsZM-zn5ppXH1pxFy9PbVCi1prwvT3sVrILeoXIeBLQb2aPebXzdXfbcpWw9mlt6Hopke6rN9lvv7QEml0KPPD76eW8I_2cngTjoxkT9zMAlH0HUEg7tFTo8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeece2279c.mp4?token=Q2TwiciSAyAny5KZWzbmA8qOwT-5M2v2prOPrjzMarcOyrRS_tqbK73fVVUeX5m3-V7wbsBB_NJCo1X2HfWlchYrAvyLz_ujAoodfCrAhK53va41-xejCxErdJJFz-JyzVhGVLU48uOolvrfgK1ES-XueDwdOjd00UG0W41IFHu5VFrdP7884FardnuF2UDn7G_Ob5B19-a1WZVs89GsbpNLr23tPOsZM-zn5ppXH1pxFy9PbVCi1prwvT3sVrILeoXIeBLQb2aPebXzdXfbcpWw9mlt6Hopke6rN9lvv7QEml0KPPD76eW8I_2cngTjoxkT9zMAlH0HUEg7tFTo8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ هدفمند رژیم صهیونیستی به بیروت
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438447" target="_blank">📅 14:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaQ8HStdHxVXoSCRLNKdaOYOjV9z0tdRScNdSx8BAvwxTvkrAkZIXhxbdICCJIxtFGrDhEOL3BR7sTCxBJtABwdZS21DsNf1vaxXlhyApWPw22Z3mD18nNdqZ9QbtMf8TWac6Sig0Xdvqe6BqG0IhJJxN3EHsR8yByLql0NQN-Xr7b-b5HpH-RD13raLDKbP_TTxQp2bD7Lvru74jckW3-bkDDsMGoWX5gS7Kk1TJHoN47-iNiZ92gsDfdEHn-drRgrMTs2ewDRxu_CSP84mDI7scZilGdcb-x4GAoVHaaegkFb1aOyNZLYszS788nzQ0ITpUt1oLU0ScM1_DnCS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فراری یمن، در ریاض درگذشت
🔹
رئیس‌جمهور پیشین یمن عبدربه منصور هادی که پس از تسلط انصارالله بر پایتخت این کشور به عربستان سعودی گریخته بود، امروز در سن ۸۱ سالگی در ریاض جان داد.
🔹
یک منبع یمنی به خبرگزاری فرانسه گفته منصور هادی در پی یک بحران ناگهانی در وضعیت سلامتی‌اش، در پایتخت عربستان درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/438446" target="_blank">📅 14:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🔹
طرح و نقشهٔ کور دشمن پس از جنگ تحمیلی و فشار اقتصادی و محاصرهٔ تبلیغاتی و سیاسی، ایجاد تفرقه و تجزیهٔ اجتماعی برای جبران شکست‌های میدان نظامی و به زانو درآوردن ملّت است، و لازم…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/438445" target="_blank">📅 14:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438443">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfb4011b3.mp4?token=UCrm1e_ILjs8FO9HqsonP_gX-ZUSktKTpoCpSa2xjEHDooMNN3_YaR2tG-DnkOq7foaRn-hWWSjZ70pWVTRNgSVYj-XN5tRjwCLqB-fnRiQG5PwOdniCd21vFNgD0Q1AlDN1ogMoXFXOuWDJnXP9xhzdATIiJj6HKmJfBE9dP8vjnFc3JR-Er-dvysha09xdtugk4_JmUz2ZCZjCyJDylz-RTWC9Nn3F_daHFgHQKP4iS6979hH_hHGn3pmVlKAqOE_-_r4A1do-ETPTu75z_hLZy6Oqv2RT4ST2_VpHxqwJrAq8wNzovxRDekhtBwAIbVOChhq-Cwn5c2t21r_vNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfb4011b3.mp4?token=UCrm1e_ILjs8FO9HqsonP_gX-ZUSktKTpoCpSa2xjEHDooMNN3_YaR2tG-DnkOq7foaRn-hWWSjZ70pWVTRNgSVYj-XN5tRjwCLqB-fnRiQG5PwOdniCd21vFNgD0Q1AlDN1ogMoXFXOuWDJnXP9xhzdATIiJj6HKmJfBE9dP8vjnFc3JR-Er-dvysha09xdtugk4_JmUz2ZCZjCyJDylz-RTWC9Nn3F_daHFgHQKP4iS6979hH_hHGn3pmVlKAqOE_-_r4A1do-ETPTu75z_hLZy6Oqv2RT4ST2_VpHxqwJrAq8wNzovxRDekhtBwAIbVOChhq-Cwn5c2t21r_vNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
🔹
نیروی دریایی سپاه: کنترل هوشمند تنگه‍ هرمز با اقتدار کامل درحال انجام است و طی شبانه‌روز گذشته ۲۶ کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگهٔ هرمز عبور کردند.
🔹
دریافت مجوز و هماهنگی برای تردد در تنگهٔ هرمز یک امر قطعی است و همان‌طور که قبلا اعلام شد عبور از سایر مسیرها به مثابه اخلال شناسایی و با آن برخورد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/438443" target="_blank">📅 14:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438442">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df96e57a31.mp4?token=cBkBNTvpiVWo6WPZkneHYby3zJAqz4VIzRKhLtAZjrUmy_YMvhnuaQUidw6KgW-FTk7Y8bDfMd23QCJDMgCK9m-4tKj52twGoiAeNDPyFBMPOJoqQadS2Y3JyGWFz7kQOeS_qYQ-kzRNxmxOXr8Bzazq4ecNsPBitxeS2ZKpO5rbFmYJ7ntc4wzB6xaSJlPmNYe0PL7Mtgv7Gr4-_EVNswpPMMyVDO5dKPQ7iuRy0ThN689VnHpfp9s2V8toXSnNq7DOf64EcEHDTKgfiHoY_V_Ojw34S8fUJgmW30A-oWSdI6kAfRhE_2YOy7LsguMVgCHbDeUVp2tvFKPVP3K2ApLrLIAdSU_uuxf1DONAOvpn4n5ogCaY_I1L-102wnaxnTwsFTl57hsSbK1S1mV5pWw5Q7aLDe3Uyd6mH4NLh_JVB6iZIe91UsaNBP7MafTSdHGnzZVFnVJtiQ_q0PqR2j0bwjBki730c-sZF00CTwgQHfWB5cYLwUgFXujB96m1pKHcqHbmBWPq5duPOuXysZglbR6vrTJ4wr_joMJx9sbjFBm5jhi298Qcg3VP7bvau5w27pGtudCJaig5r7vsCUNNzrex7SAGmGcapne_Dq9y88s8SRLzWp6rVcwyzE-GJ-XsVW1R6ca_qjBRy8iG6ArleGvcAPaoKj0pv9P-tXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df96e57a31.mp4?token=cBkBNTvpiVWo6WPZkneHYby3zJAqz4VIzRKhLtAZjrUmy_YMvhnuaQUidw6KgW-FTk7Y8bDfMd23QCJDMgCK9m-4tKj52twGoiAeNDPyFBMPOJoqQadS2Y3JyGWFz7kQOeS_qYQ-kzRNxmxOXr8Bzazq4ecNsPBitxeS2ZKpO5rbFmYJ7ntc4wzB6xaSJlPmNYe0PL7Mtgv7Gr4-_EVNswpPMMyVDO5dKPQ7iuRy0ThN689VnHpfp9s2V8toXSnNq7DOf64EcEHDTKgfiHoY_V_Ojw34S8fUJgmW30A-oWSdI6kAfRhE_2YOy7LsguMVgCHbDeUVp2tvFKPVP3K2ApLrLIAdSU_uuxf1DONAOvpn4n5ogCaY_I1L-102wnaxnTwsFTl57hsSbK1S1mV5pWw5Q7aLDe3Uyd6mH4NLh_JVB6iZIe91UsaNBP7MafTSdHGnzZVFnVJtiQ_q0PqR2j0bwjBki730c-sZF00CTwgQHfWB5cYLwUgFXujB96m1pKHcqHbmBWPq5duPOuXysZglbR6vrTJ4wr_joMJx9sbjFBm5jhi298Qcg3VP7bvau5w27pGtudCJaig5r7vsCUNNzrex7SAGmGcapne_Dq9y88s8SRLzWp6rVcwyzE-GJ-XsVW1R6ca_qjBRy8iG6ArleGvcAPaoKj0pv9P-tXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام رهبر انقلاب به‌مناسبت سالروز افتتاح اولین دوره مجلس و آغاز سومین سال فعالیت مجلس دوازدهم
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/438442" target="_blank">📅 14:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438441">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: نخبگان جامعه از اختلافات پوچ سیاسی و برجسته‌کردن تفاوت‌های اجتماعی پرهیز کنند
🔹
از جمله مصادیق تقوا، رعایت نعمت عظیم وحدت ملّی و انسجام بی‌بدیلی است که حول پرچم ایران اسلامی به ملّت بعثت یافته ارزانی شده و در زمره‌ی مهمترین عوامل ظفر در مقابل…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/438441" target="_blank">📅 14:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438440">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: دستورکار اصلی مجلس تمرکز بر شعار سال و ترسیم نقشه راه حرکت دولت متناسب با دوران پساجنگ است
🔹
لازم است مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.
🔹
جامعه،…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/438440" target="_blank">📅 14:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438439">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: هم‌افزایی با دولت، نوسازی کشور، اعتلای فرهنگ و حل مسائل اقتصادی و معیشتی اولویت‌های نمایندگان مجلس است
🔹
در این میدانِ جهاد، صندلی نمایندگی، به‌مثابهٔ سنگرِ خط مقدّمِ تحوّل در مسیر پیشرفت کشور، قلمداد می‌شود؛ لذا شایسته است، نمایندگان ملّت،…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/438439" target="_blank">📅 14:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438438">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: مجلس نقش مهمی در اِعمال ارادهٔ مردم دارد  ​
🔹
مجلس شورای اسلامی عُصارهٔ ملّت، مظهر مردم‌سالاری دینی و رکن قانون و قانون‌گذاری در جمهوری اسلامی است که نقش مهمی در اِعمال ارادهٔ مردم دارد. ​
🔹
اکنون با سپری‌شدن ۳ ماه، از دفاع مقدس سوم، عیار باطنی…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/438438" target="_blank">📅 14:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438437">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‎‌ ‌
🔴
رهبر انقلاب: از تلاش‌های آقای قالیباف، در راه اعتلای کشور قدردانی می‌کنم  ​
🔹
عید سعید قربان و سالروز افتتاح اولین دورهٔ مجلس شورای اسلامی را، به همهٔ ملّت عزیز ایران اسلامی و نمایندگان محترم مجلس شورای اسلامی، تبریک می‌گویم و به این مناسبت، از تلاش‌های…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/438437" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438436">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/438436" target="_blank">📅 14:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438435">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/farsna/438435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438435" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438434">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم منتشر خواهد شد  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438434" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم منتشر خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438433" target="_blank">📅 13:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bdcd9a40.mp4?token=eLJ-pUxPV-1Cdp5iux2pVys-wvmhRIew1E8fc-zRyS_II6OOvTnlAfJ9WjMCngrLkwvdVCkC4-SvMTY4Xui-dTgTRJuzUTZQroYdwdrTG0-up_kDsSHSs9Cj4mDE7V4MgYyyWm94HgUXBqV7XU1YslAHBKknsTgTrDl99EFmU5Uv1QC5lTD51rrMJJ4WoWFDFVNs1Q2VDnJJNHO_d-qILm9HziXiMcq_ThK27-1wue5j68YrGo4b-m5DBNbWwhrWNYLkig-JzBDfu8lfEzUnbt_CRIgOSlf7LYgNDvoCdXdJFX70F4mNs01kb6TLu5Zw_ZjeBcq4L4UMCZOMrcXA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bdcd9a40.mp4?token=eLJ-pUxPV-1Cdp5iux2pVys-wvmhRIew1E8fc-zRyS_II6OOvTnlAfJ9WjMCngrLkwvdVCkC4-SvMTY4Xui-dTgTRJuzUTZQroYdwdrTG0-up_kDsSHSs9Cj4mDE7V4MgYyyWm94HgUXBqV7XU1YslAHBKknsTgTrDl99EFmU5Uv1QC5lTD51rrMJJ4WoWFDFVNs1Q2VDnJJNHO_d-qILm9HziXiMcq_ThK27-1wue5j68YrGo4b-m5DBNbWwhrWNYLkig-JzBDfu8lfEzUnbt_CRIgOSlf7LYgNDvoCdXdJFX70F4mNs01kb6TLu5Zw_ZjeBcq4L4UMCZOMrcXA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ بررسی طرح رایگان‌شدن مترو و بی‌آرتی در شورای شهر تهران به هفتهٔ بعد موکول شد
🔹
سروری، نایب‌رئیس شورای شهر تهران: با وجود برنامه‌ریزی قبلی برای بررسی طرح حمل‌ونقل عمومی رایگان در صحن امروز، به‌دلیل ارائه‌نشدن نظر نهایی و کارشناسی از سوی یکی از کمیسیون‌های…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438432" target="_blank">📅 13:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8xACVKqlTyYOY2nMCYODszH1xBQILhwK4eIJWPM_NthR7tQD8VDC68v4ZsRYZh3usV-vcyNJa34dnE0qIEl1-UhYnC_ULMkCQt3gD9HxAxkCsaDwu297LtSAf32Nbbsplid4Tiqrgg-eBgzDLcfOiVodEJtKLrPsXoR3Hwe1Aj9sF4IcPI8_k8iRkkvBxolsrzwhSUmP_H8NEIG3C-QOLJtcRUKpaq0fpa-35i8TDW9YQKWp_0YQIEsyjEiEi3tHKH455KW7TD7BoVY1zRadKYb5yo7FedSsgDOAzAduu9UUkX9qW-S8tJl2ZhOtKwucG1-fI05zJsqGlR-jnR-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت ستون دیجیتال ارتش آمریکا شد
🔹
رویترز: وزارت دفاع آمریکا اعلام کرد قراردادی ۵ ساله به ارزش ۹.۶۹ میلیارد دلار برای یکپارچه‌سازی مجوزهای نرم‌افزاری مایکروسافت و دیگر شرکت‌های فناوری امضا کرده است.
🔹
این قرارداد، تمام خریدهای نرم‌افزاری پراکنده میان شاخه‌های مختلف ارتش آمریکا، جامعه اطلاعاتی و گارد ساحلی را در قالب یک قرارداد واحد جمع می‌کند.
🔹
پنتاگون می‌گوید هدف اصلی این طرح کاهش هزینه‌ها و جلوگیری از خریدهای تکراری و پراکنده‌ای است که طی سال‌ها در بخش‌های مختلف نظامی ایجاد شده بود.
🔹
این قرارداد شامل سرویس‌هایی مثل اشتراک‌های «مایکروسافت ۳۶۵»، ایمیل، ورد، اکسل، پاورپوینت، خدمات ابری و مجوزهای نرم‌افزاری داخلی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438431" target="_blank">📅 13:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1793d0e1b.mp4?token=bkTqVOeCuKqaH1q8qsZRY1if9znGfHBknpd5KD5UOC7vEccRI3oXUGVXoijtLs6ce_6PS1ZYR5G9FKBtFKDLvErM4B5YqPkt0skZo7mQwKWJIQMFeGN6gu62Yb9eSs0L4HD9chd4mwk526JMvSllBAm2VG-n0xQ_BeJdhtNGZdKHE7O4BNpBm7fPrYK4e-TCFHNKHoDNVKfN5gTf73ctlsp5GBcJiNlLDDC0_kiYRSafX6N9Mnj4TFzShK442RIJiNLbCymDb1eC3Z5UsYXQ6s98b35Ay5nWF5Qi2up3IxRGznYB87hpTKgVlThc7TStXNaNbBNJZuAMZuq72IEZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1793d0e1b.mp4?token=bkTqVOeCuKqaH1q8qsZRY1if9znGfHBknpd5KD5UOC7vEccRI3oXUGVXoijtLs6ce_6PS1ZYR5G9FKBtFKDLvErM4B5YqPkt0skZo7mQwKWJIQMFeGN6gu62Yb9eSs0L4HD9chd4mwk526JMvSllBAm2VG-n0xQ_BeJdhtNGZdKHE7O4BNpBm7fPrYK4e-TCFHNKHoDNVKfN5gTf73ctlsp5GBcJiNlLDDC0_kiYRSafX6N9Mnj4TFzShK442RIJiNLbCymDb1eC3Z5UsYXQ6s98b35Ay5nWF5Qi2up3IxRGznYB87hpTKgVlThc7TStXNaNbBNJZuAMZuq72IEZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین از ساخت نیروگاه هسته‌ای در قزاقستان خبر داد
🔹
در جریان سفر رئیس‌جمهور روسیه به قزاقستان، توافقنامه ساخت نیروگاه هسته‌ای توسط شرکت روس‌اتم روسیه در قزاقستان، به امضای طرفین رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/438430" target="_blank">📅 13:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgrCDBwYB5Kv53LCP-SOgnyQ7FT3UKAjPPn271Hu1_OTVQEl3rmc4Z0NEUotbsDCqj6FPxCOkSSoTUmxtUCKbFwhXlGDcl2EEldaBjNA9r-XSJoou36vNavtOTlHv2wyYsMdU5jj9PMNwqxlMzNPi_7EiDp4vqCYYmdgIOsW_EJPprBXBFKV55oSU4ZOiT8CZElRDKUKHfF--wVcESqIbMElN0EjCzGQtA4nYt_nK-Ia5o1HT7P3QSeNZ50QZpxpAmRx-qcT-BnTRdtbLtfN5ROPz3TY6ieM1eojHvE4ZtR5vTs4iKXWmJObJ6uprvAKnhZBmNJta8SN51s0hwAX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دعوت محمدرضا طاهری از مردم برای شرکت در مراسم یادبود شهدای خانوادهٔ قائد شهید و رهبر انقلاب
🔸
این مراسم از طرف خانوادهٔ رهبر انقلاب پنجشنبه و جمعه از ساعت ۱۶ تا ۱۸ در  مصلای حرم حضرت عبدالعظیم حسنی(ع) برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438429" target="_blank">📅 13:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">توقیف محمولۀ سیگار و عینک قاچاق در مرز
🔹
فرمانده مرزبانی فراجا: مرزبانان پایگاه دریابانی بندر لنگه محمولۀ ۹.۸ میلیارد تومانی قاچاق را کشف کنند.
🔹
در این عملیات ۳ ميليون و ۸۱۷ هزار نخ سيگار خارجی، ۴ هزار و ۳۴۶ عدد فریم عینک، ۳۲ دستگاه فن کویل و ۱۳۴ دستگاه لوازم برقی آشپزخانه قاچاق ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/438428" target="_blank">📅 12:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6cb621aa.mp4?token=AMlioCWRZdhQVhVImeOR_4xkyhfMelWWfn3CIk3Ls4EJadPDno8nfH4LQd3A3A018eedag2MTU8kdWb3kL2iIZ-lP6FJlDIPvCSulibRYQfQClqtDE4vg98IqSF11i8pFAaYdQIw9tOGQe6S7Klxh9aN_iAPmTs9fwj1qr43ncaUxW9-6YKKvZl2wCriBiyFpa0HnebNno-GEYLHxf68zDb8wx-LTq3ohJtQAzL4hzG6MoZQAaK_RCnapTd5ywUhSNloV5WcmlkzUCNMvGOwYdqONsxaJs-0M7KLio1aSH-RPCAOwWPBzdy800KNT8tuTQ_G_05hdwojR6BGCPgR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6cb621aa.mp4?token=AMlioCWRZdhQVhVImeOR_4xkyhfMelWWfn3CIk3Ls4EJadPDno8nfH4LQd3A3A018eedag2MTU8kdWb3kL2iIZ-lP6FJlDIPvCSulibRYQfQClqtDE4vg98IqSF11i8pFAaYdQIw9tOGQe6S7Klxh9aN_iAPmTs9fwj1qr43ncaUxW9-6YKKvZl2wCriBiyFpa0HnebNno-GEYLHxf68zDb8wx-LTq3ohJtQAzL4hzG6MoZQAaK_RCnapTd5ywUhSNloV5WcmlkzUCNMvGOwYdqONsxaJs-0M7KLio1aSH-RPCAOwWPBzdy800KNT8tuTQ_G_05hdwojR6BGCPgR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صفر تا صد سامانۀ «باهم می‌سازیم»
🔹
شهروندان می‌توانند با مراجعه به سایت
BAHAMTEHRAN.IR
یا ارسال عدد ۱ به سرشماره ۳۰۰۰۱۱۴۱۱۱ در بازسازی شهر مشارکت داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438427" target="_blank">📅 12:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2EDKe_ZfW8UTbDb-XQu8klcoLkaIEeZk270_vE_E6EVMm1Lw_0hsE5PInER262i2YhtisK8TO3stjqlGgfeZmvmFrseNCVDgXBvAeuklb_SwlNbez63-KkhKBC-HOZlKx_sai1P5vPSgOFzbH7R8Vdsh-E1RSxvN-c4sDLg6B4V98GcdkznIjkujnFWEVl7QKUQIde02uGeBjDRXrkYJFlmkBva1BO2BepMdV5gHpAxYCEWbIE_vXvdrn7FUZAk5TnhArz3KKSHTkd5ZilG8T3az618ZLWi9j0HlfdRHLBg7yT7I3f7dn-1HgXmOOB38oQVuJzPoVvffx7u3jzycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
اعلام آمادگی بانک صادرات ایران برای نوسازی و توسعه زیرساخت‌های سلامت در انستیتو پاستور ایران / تأکید اسکندری بر حمایت از امنیت سلامت کشور به عنوان یک مسئولیت ملی
🔹
در پی خسارات واردشده به انستیتوپاستور ایران در جریان جنگ تحمیلی سوم، سرپرست بانک صادرات ایران به همراه اعضای هیأت‌مدیره و مدیران ارشد این بانک، با حضور در این مجموعه علمی، بر اعلام آمادگی بانک صادرات ایران در روند نوسازی و تأمین تجهیزات تخصصی آن تأکید کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/438426" target="_blank">📅 12:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh04jJ3WLALPELnmRYP2l0D2saaPfZBI5JDyRo6SVRsluvlDUkU6JBv2mJPFtX60TKtzjToOnJGMbiWdEZsoIHk90Ea9kWRwF5FHxFVtd86OlEQkzFZxVMW7sPcmdS3dxkl4SGo4yTZwL-or1DSrAt4BgKjgY25HY9J8gGDCZ0Jxm_nxMszEtRM1m2lmhb4fzghcWi3J253b_jc7k-1nNscZ0vTevKwy-G6N699WPmasO7pSZ1kalRFVtd-YtGtnZo8FblG2DJJ1CiVyt5aGvtCErPLliT8ewK5rrQ8U3UN8Gu7cNnPvn8MddT8BPTCf3l1TB_6gGayF4oZ7BY299Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه روی لینک زیر
کلیک کنید
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/438425" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/438424" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptDTye80h7Al4vKM_q8lE8aOcudSWi6D58fiaLBaMeqjZ17SRxaCuMSogCaHml1GmkJ2rmVQnVwABvl1YR-N-g9_X9hBhYoZsNuWnAZY3berNrKgxDLleJcL89XcaeL-rPcYDV4o2O_hDUkIDwEVoZ5AY5uKsARD1YVyUP9-8O_97b--LVjP_jzb1Dy2ud-y1THU7J-lHBievf2IINumExDVp5nNkhuIlQB_kNnlhmpS1sja1e8CulydhPzh3fq1lOP4FeQ_cg9deMpMo-R46mDY7Bb86DQZ67TEsjLzha8w3_B3bhmTbvj_sQI6b6Kro-rmmcJG0iRs6ah4faVWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قوه‌قضائیه در زیر بمباران از صیانت حقوق مردم دست نکشید
🔹
رئیس‌مجلس با قدردانی از پیام تبریک رئیس قوه‌قضائیه نوشت: قوۀ مقتدر قضائیه با مسئولیت حضرت‌عالی و تلاش سخت‌کوشان عدلیه، در زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد قاطع…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/438423" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
رسانه‌های صهیونیستی: از صبح امروز، ۵ پهپاد حزب‌الله تجمعات ارتش اسرائیل را در جنوب لبنان هدف قرار داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/438422" target="_blank">📅 12:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGH7NsayxW-2ngzZPhgMCWhIpjogzm8MYK23f3aNQpJdtfnyQPTj4LasH8onxH32kzHmCso3lSyFhQvmx2aWw92ZECi5x-sPabcQgMO3KBZGIbbkkWvUUl2OF_CHmL7YAAFRDCCtmbtwTrd1IssfZweEdkUZEz7ojc2CuzMq-k2AUgSAXrHdV4aVJnhvt_Qd-8w9QNf5BTLIDsd0PnxLDSGR7XW7S9S7wEjJ-KinpL0VA8OKzbb-0wiF15Pvsg7yZnEhU8iOTMs1kcWddGQkkKmYP85m3FOJNoRPfAhEFDyHbGYn8yMvpfomUmBCxRyo_9ZS8askK0bcJ0tWsyhRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ابراز نگرانی سناتور آمریکایی از وضعیت «شوکه‌کننده» ذخایر موشکی آمریکا
🔹
سناتور آمریکایی مارک کلی روز یکشنبه در مصاحبه با شبکه سی‌بی‌اس از تجاوز نظامی علیه ایران و مصرف بیش‌از‌حد مهمات آمریکایی در این جنگ انتقاد نمود.
🔹
وی در این باره اظهار داشت: «پنتاگون…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438421" target="_blank">📅 12:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438420">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ837PLW6PyA2LuzeRIIgAJqEBCm6Xub91LGoZQmNF5VrGp5LxXV0EW4g8A8Dk-a3u9-hmnUA1KlXxHLNrRlErB9wYY7igpu-v5HghZESMUsiS8USlP0JStnHUJBW0tRxFDwB9B0bdaf891h3lMrmFnWRvSxgr3sAJoy_2V1weB9ldfuYE0dq-1xHuC3KPPgcd46QwUrdN2vau9dfU7-immVvhmFXTI72rM1ir_tWqobeKhuOXtLeIg6ZhSwIWIcQVVZS5_i7PnWakcsL5cDTION6zZfVpWOuxHl8Ly2N9bu6z5hFDEd1H8E221iZVqMg3fuXMYY8elB141fZDSxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره شمالی: تحت هیچ شرایطی به ان‌پی‌تی نمی‌پیوندیم
🔹
سفیر و نماینده دائم کره شمالی در سازمان ملل متحد کیم سونگ، امروز در بیانیه‌ای تند و صریح اعلام کرد که پیونگ‌یانگ «به هیچ وجه و تحت هیچ شرایطی» به معاهده منع گسترش سلاح‌های هسته‌ای (NPT) پایبند نخواهد بود…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/438420" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438419">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwUGt4P_b4LhgmOQuoP6sCOCU4CC44fvge7iHwKCqZNxuDpf43Xjm8H5zuBGjltFvzNlEKPPZ1xH2d0OEDsWi-TBtBFZRQ4TAt9HX4yWwMRab8NHwP7CYrmxOR6kck-VRA9goAB7Ckw66vFCluZtwlKY8qX3eyC3Wm_P7X2LroYgFYS_5i1n085kXDaOIi_DoVxZ1W1FiFdO5yCOS3eHqlideiddrL7siexgEOZEbj9CjDgR-PCeNhXq_ythSUw8zRi9BWHjBAYsQEqBH5dEsUG5GCPDb4oE0Ews7SF5ry1Eedr_fdDqTdkur1XYfHnALfmQp-Iwkl0zhgYw1rmGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها و وزارت راه علیه ساخت مسکن
🔹
در‌حالی‌که حدود ۱۶۲۰ همت از تعهدات بانکی وام ۶۵۰ میلیون تومانی در قانون جهش مسکن هنوز پرداخت نشده، وزارت راه و شهرسازی سقف وام مسکن را بدون ضمانت اجرا به ۸۵۰ میلیون تومان افزایش داد.
🔹
براساس گزارش رسمی دیوان محاسبات کشور، شبکهٔ بانکی طی ۴ سال منتهی به شهریور ۱۴۰۵ مکلف به پرداخت ۲۲۲۱ همت تسهیلات در قالب قانون جهش تولید مسکن است، اما تاکنون تنها حدود ۶۰۱ همت از این تعهدات عملیاتی شده و ۱۶۲۰ همت، معادل حدود ۷۳ درصد تکالیف قانونی، همچنان پرداخت نشده است.
🔹
بسیاری از کارشناسان معتقدند وقتی وزارت شهرسازی هنوز نتوانسته (یا نخواسته) بانک‌ها را به پرداخت کامل وام ۶۵۰ میلیونی ملزم کند، افزایش سقف تسهیلات به ۸۵۰ میلیون تومان بیش از آن که اثر عملی داشته باشد، نوعی بازی رسانه‌ای است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/438419" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438418">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHAPgSkBiu_UpQ0Qis4mcB2xngBz8D9kuU3VpcZBCXB4JGEWPW05R3gHs3cBqS9ZKrAH71vOp30-LhK3UsK2WnscQCENxPGbpfL0DZSQvgLn1v8do1UHIvFCdYv9RHT4rz14T8YZfqa8tCfde_TDa3wa4UKEHjqxVpQeZ0wYV5J6k8EzUFx-SrafO8Eg3W6OUbNcnYpQ3l8AaMsNZpcFU8CDq5FepPM9WUhskwJWzBNKraiu6WwTev0tuYkXyUIkXprEbdQw4l2L6l_FL-ZIhvkaK_eyG5KNJTIIObMc9OUtJvoQQc2U44cI_PDFuS76jOW7NASRcTogd46tnzZjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریفان ایران در مقدماتی جام ملت‌های زیر ۲۰ سال
🔹
حریفان تیم ملی فوتبال جوانان ایران در مقدماتی جام ملت‌های زیر ۲۰ سال آسیا معرفی شدند.
🔹
گروه A: کره جنوبی، قرقیزستان(میزبان) فیلیپین و  لبنان
🔸
گروه B: ازبکستان(میزبان)، سوریه، هند و بنگلادش
🔹
گروه C: ایران، ویتنام(میزبان)، کره شمالی و فلسطین
🔸
گروه D: اردن، تاجیکستان، بحرین(میزبان) و افغانستان
🔹
گروه E: عربستان، قطر(میزبان)، عمان و هنگ‌کنگ
🔸
گروه F: عراق، تایلند(میزبان)، امارات و ترکمنستان
🔹
گروه G: ژاپن، یمن، کامبوج(میزبان) و کویت
🔸
گروه H: استرالیا، اندونزی، مالزی و لائوس(میزبان)
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/438418" target="_blank">📅 11:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438417">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X91s43iffBzsFbqd_oZPFPbx66UyXzYxD3pPxpKhIirvD84xm45bm-7ir-VKQS35IA1bg7Fzfg8Z7QbFuHavRLaC1OLphB4aM2KTdMjg1aSCkBwcwXzna4GB_n_ThAlbRasebcYkv2IEJAsSncOD2hYO67_MHMXsPHl_5F4YNywyzGv8aX42DXvkZVghVo1EZSv5KIwMqh2HrvzDxurXYUUkKcr0GF_PniDJMQ_Pzb6ZMNXuvbGr7HCYq3skhL5-uzHZyF9ZmTze09OpirJVxBXnG_4lDEhN95TWY9tvzihM5yjQ7eJncX78O7LwaWyk6RlecJgFb054Ob7dcDnIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در فهرست سیاه عاملان خشونت جنسی
🔹
به‌گزارش جروزالم پست، سازمان ملل متحد نهادهای اسرائیلی را به فهرست سیاه کشورها و گروه‌هایی که در مناطق جنگی مرتکب خشونت جنسی می‌شوند، اضافه کرد.
🔹
میدل ایست آی نیز نوشت: گزارش‌ها و شواهد گردآوری‌شده از سوی گروه‌های حقوق‌بشری نشان می‌دهد که پس از آغاز نسل‌کشی اسرائیل در غزه، خشونت‌های جنسی ارتکابی توسط نظامیان و شهرک‌نشینان اسرائیلی افزایش یافته است.
🔹
سازمان زندان‌های اسرائیل در فهرست سیاه ۲۰۲۶ سازمان ملل قرار خواهد گرفت و سایر مقام‌های این رژیم هم تحت چارچوب نظارتی برای احتمال شمول در آینده قرار گرفته‌اند.
🔹
نمایندهٔ اسرائیل در سازمان ملل متحد در واکنش به این تصمیم: به‌دلیل این اقدام، همکاری با دفتر دبیرکل سازمان ملل، آنتونیو گوترش را متوقف خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/438417" target="_blank">📅 11:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438416">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTYELMmrz1fgFX_5WPMSb-ACGSvkmntOnuNK2XZM0JmNXIQPmASygzLq3Q6Uk4sdnXlRVIDN1_CJ0i5QGdKYvFWqdLyxmTL5wdGbq5MQMpn7_rt59l62Pr4RVDSYpid1cmxs1Maa0qArz2uix0-mPqADAHSAzY7lzzUpNqJHtm17XR14NGczgCNqaLJd_r_eV7xih7Mg0MJflLrUoe4Znv5MwrgyyGE0hB_nNmm_c5TBQl_3jGqAW1df1ukfadnKW5HNOYs7crXMqoTOg1LCWoFctCI2j2BvzNih1x_3S39d-AlFNsfof1xT2w3aC9KWx0IZ_oWjXh7ajAHW0kLPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی نقض آتش‌بس و لفاظی‌های تهدیدآمیز آمریکا را محکوم کرد
🔹
سخنگوی وزارت خارجه: اقدامات تجاوزکارانه علیه تمامیت سرزمینی و حاکمیت ملی ایران، نقض فاحش حقوق بین‌الملل و منشور ملل متحد به‌شمار می‌آید.
🔹
شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخ‌گو کردن متجاوزان آمریکایی است.
🔹
نقض‌ مستمر آتش‌بس ۱۹ فروردین از سوی آمریکا، به‌ویژه تعرض به کشتیرانی تجاری در منطقه‌ خلیج فارس و آب‌های آزاد و نیز تعرض هوایی به مناطق جنوبی ایران ظرف چند روز گذشته، بر عزم ایران برای اتخاذ همۀ تدابیر لازم جهت دفاع از حاکمیت ملی و تمامیت سرزمینی ایران وفق ماده ۵۱ منشور سازمان ملل است.
🔹
تهدید به «انهدام» کشور دوست و برادر یعنی
عمان
که همواره نقشی سازنده، موثر و مسئولانه در قبال صلح و امنیت منطقه داشته و طی سال‌های متمادی در مقام میانجی روندهای دیپلماتیک، مساعی جمیله خود را در خدمت صلح و ثبات منطقه به‌کار گرفته، نه تنها نقض اصل بنیادین منع تهدید به استفاده از زور است، بلکه نشانۀ خطرناک دیگری از عادی‌سازی قانون‌شکنی و قلدرمآبی در روابط بین‌الملل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438416" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438415">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRGY2P0_HxO5e7qYbPateNnWlK2AZMLi1K7gqs3IhB-TcSx7uyJDYv736chsMHpdZlaPab1TX2rB-zh_NEve3ZVFmS-poK6HLUq4-kLCidbWLep2o9VjyBPjHETR1ZQMjlG2fF595JBPQdk6ZdgKx2cTYhD2EzNGF0OsN62M8FdghKqTwO5jOGm5REXdYH7yI4WMYk5EKqHq1yWPeaxtr14QycMKFe86fIOFd17TKeDvNP8dALqzLQ4tu2ktcElcVRdNM1Nz5IOLhYfB6RGG0UpTlJXsXowRPePOM9NM7v1Lldcq7XsV3xJM46KaGNAg6F512k8fSaPD8Pn_NLjuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمارانی که به‌خاطر قیمت، دندان‌درد را تحمل می‌کنند
🔹
هزینه‌های بالای دندان‌پزشکی و تحت پوشش نبودن خدمات آن دلایل اصلی عدم رسیدگی مردم به دندان‌های پوسیده‌شان است.
🔹
طبق شواهد، حداقل هزینهٔ عصب کشی یک دندان، ۶ میلیون و ۸۰۰ هزار تومان می‌باشد.
🔹
اگر دندان کشیده شده باشد، هر واحد ایمپلنت به تناسب کیفیت جنس آن طبق تعرفهٔ مصوب ۲۳ الی ۳۰ میلیون تومان قیمت دارد که در برخی از کلینیک‌ها این عدد تا ۵۰ میلیون تومان هم بالا می‌رود.
🔹
اندوکراون یکی دیگر از روش‌هایی است که معمولا برای پر کردن دندان‌ استفاده می‌شود. انجام این نوع روکش بین ۱۱ تا ۱۳ میلیون تومان برای بیمار هزینه دارد.
🔹
پر کردن با مواد نیز یکی دیگر از روش‌های پر کردن دندان‌های عصب‌کشی شده است که ۴ تا ۱۲ میلیون قیمت دارد.
🔹
به‌طور کل میانگین هزینهٔ درمان هر دندان بین ۱۵ الی ۴۰ میلیون تومان است، بدون اینکه بیمه‌های پایه ریالی از آن را پرداخت کنند.
🔹
طبق آمارهای موجود، هر ایرانی حداقل ۶ دندان پوسیده دارد از این رو تعدادی از مردم با ثبت‌
پویش‌هایی
در بخش فارس من خبرگزاری فارس، درخواست تحت پوشش بیمه قرارگرفتن خدمات دندان‌پزشکی را داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438415" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438414">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fe08de28.mp4?token=be_TXoLsAWFlnNmfcyliKI4hmsrhpLWIuaMyPAZMDa-ulMPZZXXCWKhtY3em4oHT6OC4nyB4mpjuBt-frh_Aqr6XZ1xlEe_0-NsW44HyxaopVWxOfE-GpCRWm5-exRxirbUpEWxAJK7hqiC61Okc9a6lJj8UdLqAkKnlnxMKpD7C1X_DPeLSZsFEPPRnmDwU9Q16HyeS0jqanE-n2lWFCcCXLu8evaqDlHom89MN-eRE9NaI7w2oD6JXZN8YqNebPkb_Ar0goM4HQpJkUz1GJPyk8Gr16TMrA4eiw4K7pNSyF4rfA0fReglHduhw4DkdSdpMCET3iINK5LVa-nS3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fe08de28.mp4?token=be_TXoLsAWFlnNmfcyliKI4hmsrhpLWIuaMyPAZMDa-ulMPZZXXCWKhtY3em4oHT6OC4nyB4mpjuBt-frh_Aqr6XZ1xlEe_0-NsW44HyxaopVWxOfE-GpCRWm5-exRxirbUpEWxAJK7hqiC61Okc9a6lJj8UdLqAkKnlnxMKpD7C1X_DPeLSZsFEPPRnmDwU9Q16HyeS0jqanE-n2lWFCcCXLu8evaqDlHom89MN-eRE9NaI7w2oD6JXZN8YqNebPkb_Ar0goM4HQpJkUz1GJPyk8Gr16TMrA4eiw4K7pNSyF4rfA0fReglHduhw4DkdSdpMCET3iINK5LVa-nS3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/438414" target="_blank">📅 11:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438413">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2Rc1qJOWpJS31T4CWKgCcceqyK8ENkN1GZftsc6R0vyVzTsPBnNWPKfsiZ99EJjZ9JLYCNTMq1SjWq9_xu0DeZLugmjhD_4zDJGA1HNejt-qCsO8DzUkCMbsgVvkN9R-oxOc23nwiwxnZf65Hf5zoM5_3H9rsiqgl4C0b1PGFcPB437OE07IIDCwUH1XrxLfQgStacVdvbZkYXIS5N4Fdh9sjAJh4num7u2JWA2H0bARiAJoCHw9Ov3h7LUjXpLGWDWRm1Kui6rNpNqYU3GQr1V4SThnHd4Js24hFLP-5xo80r-1gac1Ym4WTxvjE-AZPkAbbiwjKWle5w7UFatjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تبریک اژه‌ای بابت انتخاب مجدد قالیباف به ریاست مجلس: دکتر قالیباف حقاً و انصافاً در جنگ‌های ۱۲ روزه و رمضان در عرصه‌های میدان و دیپلماسی جهاد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438413" target="_blank">📅 11:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438412">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hem8v-iO9WAGE-8WkUBCaWNwokwVSRPBIhlk8j4OOmJtQfcCMzi2ZZv5W68MD7aO5zCYOwSU55SKE2Y_J2Cvc1Itr3REmGqa4-RymHTuoJIO6D2xTaCZZzRzUg5UHz5IXfnRSlT5c3Poh-ZexGR_zddVswThj7CbozDYD53YprbiXZy5J38HwlX6LohvT9JslzUDX-DmgWj9HsB3YFonzOt-t5-ozTRa2K88Py63iRYarJPY1jCkFBKdibEHHObyvEr-E1vdDYc7DaL0x5pHBKvGlFNu2Aqo3l0f_RNXchKg_IciPzTlWh9U0hhhXUPZ7NBIpYcLAdjDqZ5k-oLKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به قالیباف: این اعتماد حاصل حضور شما در عرصه‌های حساس خدمت به نظام و ملت ایران است
🔹
بی‌تردید، نقش‌آفرینی ارزشمند جناب‌عالی در دوران دفاع مقدس و پس از آن حضور همزمان در عرصه میدان و دیپلماسی در جنگ‌های تحمیلی اخیر در صیانت از عزت، امنیت و منافع…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438412" target="_blank">📅 10:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438411">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFPvDGBizfrWbqcvfIHKN8MAcvIewCilZvocN6QDSAV5oEqkfzs7gJGkLiCc3t3VmUks_V7nO7Z5ZWm7MJNDoP0dVQQlfdPB7R75J8IeWivHZWB8NV72wAqh8dir2xaqAq4H7hfiRoJaF5-pGqlorQWsJ_rb7uOeTfRB_W5Y6YSGzE79ElLL8PtRs40fvf-TsCILIB0-EnGIu-ECPuZgFKJEjYpx66odiHNXRRxWGB2c6oF_r_L9HQ2IW57hCmcms8-3JIJHDbJHdZ8OWoMs3l-bvj5t4-wD3DysrjIqS8fky97UP8uE2VK2nEThzpjlz1Krk94fZqukeOcEUjBxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: شهید شیرازی تجسم امانت و ولایت‌مداری بود
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا با حضور در منزل شهید شیرازی، فروتنی، تواضع و اخلاق حسنه را از ویژگی‌های برجسته آن شهید برشمرد.
🔹
سرلشکر عبداللهی: از همه مهم‌تر و به‌یقین، شهید شیرازی مورد اعتماد و امینِ رهبر شهید انقلاب بود. این امانت‌داری در حساس‌ترین پست نظامی کشور، نشان‌دهندهٔ ایمان راسخ و بصیرت راهبردی ایشان است.
🔹
حضور و مشاوره‌های آن شهید بزرگوار، با توجه به اشرافیت کامل ایشان بر مسائل نظامی، امنیتی و راهبردی، همواره راه‌گشای مؤثر در برنامه‌ریزی‌های کلان نیروهای مسلح بود. همه فرماندهان – اعم از ارتش، سپاه و فراجا – از وی به نیکی یاد می‌کنند و او را الگوی مدیریت جهادی و ولایت‌مدار می‌دانند.
🔹
مسیر ایستادگی، استقامت، صبوری و مقاومت، وعدهٔ الهی است. ما در برابر دشمنان ظالم جز این راهی نداریم و پیروزی نهایی از آنِ صابران است. در این مسیر، بی‌شک صبوری و شکیبایی خانواده‌های معظم شهدا می‌تواند موجب افزایش روحیه رزمندگان ما در جبهه حق علیه باطل گردد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438411" target="_blank">📅 10:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438410">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فواد ایزدی: ایران نه غزه است نه لبنان
🔹
کارشناس مسائل آمریکا و بین الملل: پیشنهادم به مسئولان این است، من اگر جای آنها بودم اعلام می‌کردم که هرباری که از این به بعد به ایران حمله شود تنگۀ هرمز یک ماه بیشتر بسته می‌ماند.
🔹
اگر با این نوع حملات به‌صورت جدی برخورد نشود تهدیدها ادامه دارد.
🔹
ما به آمریکا امتیاز نمی‌دهیم ایران نه غزه است نه لبنان.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/438410" target="_blank">📅 09:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438409">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاری کویتی در محضر قرآن رسوا شد
🔹
قطعهٔ «عاشت یدا ایران» با صدای یونس شاهمرادی قاری ممتاز ایرانی، در پاسخ به آهنگی علیه کشورمان که مشاری العفاسی قاری مشهور جهان عرب خوانده بود، منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/438409" target="_blank">📅 09:32 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
