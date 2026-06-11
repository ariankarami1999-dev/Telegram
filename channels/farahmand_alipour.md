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
<img src="https://cdn4.telesco.pe/file/fCTAvFmpGhIiDlGKyMLZf_I6ZNZU6_lrgFlDmDO06hhkU7ZSRONIF3hQTVywJjNRy4cC7XLETBShSqnJW5XZDMUeZ40qx8gnfnvwQIeZ0GYSbC2cHfBZk7h-3sfVlKAwvuJMD_64Jn9T99ohgEDSYStewm_QKbMY8Jf1xWevoXn1Myg_gBEmsbk70NTbxbjddQsNrcH2dloMQYoVqaxXtaDRC1NDn3LHLTq8ZnH2U-xUx5ABqnDBxUG64TmcxBIQmnSkIMUm2K3uNqhhVXLNvz_NgKXTVJCv_lkOm9XtMtO6dUvUCk9S0dKW2bv98ychhkoD-EfCKAqhuK3nktKSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkVg761KSZAfaC4OXcuYo7SAJa1RjV237Yyf-QwFenlX-GsGqWOJz477oFhfsHAhWKuHXbAWG-F5YMnKMzamSyRIXJ8CtOjfZb7ne9BrNPkMxQybLCI3O69OdVTEM8eGeAm0pAY0zGRDisHqOuKZ2PLYErCWs-8mlWTAQiQh90ETl-PWzCIOnGjdNi0fRIR6FRiCC8vF5FE_DCCIgIhzGcQ1NPHLF3zQltHYbWiACiXB05QqzRilX4lqOH08r61ppiTZWvn27oT9eYp-TYPzjrNZ8fjpOW53IOU45qp53u0b1EbzvBXePp6CgKzyVRIlu5VQ77QTQks8iondQVmPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMi18clNUoQI1ROilnVuhi32ajlU8RgdgqhOEhHt60flc9ZY2wXQmZthYuNlr-hjsMq7BN5Q3gAIIwJxEWIeCS_Dl6ZQ9CeJBwoiEbBOLuP5rRA53oIwsG7Cd8-4fQKdB-lQMjln3EtnELnl4kQ5RHnYLPtQ3wDt_COloMFz32Iwu_4IIVv3mWr7o39k03U3IE2O-EeGhtT5oqhWuEA-JiNopo5QLopK9RaQ8-iXDzZSuk6NFy2C4iHUaD4zVqdiRpz45nfD90VL4m95ZZ2qAEorGMcnTzUtVrTjcVpmDVazcko0p0UH2CF-p-AYH8xLq7K69wnB7F9XrNpHr40DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmX6iy2saQtxdvvsqd3kWqS5sNsuVF0gZKmMCZODe4HJFbWL19Cd4_G-jI0TtpsrKpk-a_e7M0m1QKos0dbgu-aHVgGXujTtvZctEQLpAED9zB4RfLoE-tuS2IxBOQaGJtCraV1_qbUlAtBzjRW-NCR-rP8ZYQakKmHcuuxBxZk0TmI24e7y1Lsi7fFewNLufWr6q3IiTTni_KEAITXmzbOwmaey8P4vqJjDV6XDbd4MgZCjVNBTm-LCPO3BVfvSiTU0qvEyeCovxJ0H8Ik4JZ1ZLkn_bs2KW5qSCJqTgJM67g6rKBjePGW0hP70R3iu-_R7hT_h9raHogjNLYOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99gftpphTHyhkJ9xPEhGIPwVC0jf9TJz4vpgFHdB19oMbse0KS57Tgn3LMR_kzuT1begK0CcZgmKvFs41FUCl2_yMjnrP8B7UXYYwtduRw8u0o2zHhwSRX9bTl-s97kuEeBRrTeMwrbJFY5I-vuIzEbsaNNy_t4HArigrw2YLZBVTiQSUqoYNY27TKv46lB9ExDH9_M2gCHvnMSUMJTMiqceCfNL-dzixu7k3OSDXgGdaPLWxlNlYtJZwhtFP3n7PC482FANbvHknDB1YuMakdmcSLvwzrSXVVEf8-sdmXxT1gTvOtCPLnYzQeEPMq_xakCZmGWssWsWkkSaqGcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey7eJT4NVObbA6kVBWMq5evRhppYbNlcmFi40hTYdIHzxMHkFZ2eRXSs0JibS0GrHjNwYU1zkLyG0_2HSYqfXdvZcgV6ErdNGgVQPawcx2wmfl2NGhpaWbHieMydWEfiaW7dJDtK859zh9rigmZhOeO7BD5ddSWIVaNzszZ1J7xSJqetuhr9Z8IHYwYZSqg52xy0E_bUlfGIsFaLENq5S2cvUTpZV9XZseCkuf7MfhABP3Rt4lggm8EyAsVxL-vmqfx7u6zhtZQ8f19KNLp9kkT_CnLP-aHhXbYQ4r30B_e2o8naifT-RE0-c-pYesQccZYHyIkgah-L2oT8Fq_qaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atB3YCPwI8jVMqu56Nq2N2Bswp65QS5pMrqOgufkfXfyVpLB1bKTlpmTUSmfzSr0Jcb32TGFntjoxSgSgFCaLsjbpGFGGeMmTWt5lHKKYxHjwjLT-JDyJo48x1R_qKB1_Zv1D9KewdF5naYpnyeEuyu5tZfA5LNY_CblA6imq7FcLm3Zh39NS6nyNcx10O3oCf7ZaVRCIAPNWpIWLg3R_aUJ0YeWVNLSZ6YNUfcy2rT8-m1IeuW5hSwg5xaXCqJ5_XHvUymmKnGKwmFrY2Yv_4JQIzoWSCidGkMtuPxQ4DRMTCY6XcYHvIcZ733627Hyi1jw2UQJUj5mJgE5BfVpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1OmXew-CroxJt011D-X2UGI9BaAegzmxZKNIT2nERPWuZ0sI7rL-0vwcmLzu9Vm_UdtCxD-D9fiqcSOgmdoPS-jCUu4ktSdjT-qzDCwK-n0_2nRVZaBlIJJ_XYlkxSCDFhIL9h7MSKZNQNNLSRk-fsAS4Xx0CL7AD5RE46-4xzt5x-WTQixfJmD2upnO2OoXHJ1_Mg3xtKGRM3uirfXaQElO6H1k-uPIGVcgs73auFxVWzhL0GOWLKFm6kJ7lfnildwI2Rb9tQLSbqtjytAG-6CUAhQ-7Kc58YAoX4evVjWDp4cxthk6jhJrhKO1TC1uPyJF5375I_sZM7_9xnXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IazjAdyVy2Z87ji5ZgVSQUdUeRRApt_JVW47Zs3r3maLpV9H5gZI4ibO4kO8rVLVNK44u3Mc0si9yEs6hF3uGT-SC0oV5yf8FI30cBa79JpxYSKKm8saWTpOWowRMoQC3MeBnn9uVYwZDDAvD9D58GGvpQ9zqXTfuVtwxayLV5jIpNnFhb7zVKtzb9b_0pVYzLjQSgpri6Y2mIcM4QmiWMvzAgQ-jXXhMmscCS-lcwzj4T_dFhfPfjJ0fzsRx7vbCfrQJ2n0gOriu4kxwerUeD4cfc_PFKDywnXo3hyYDhvSzEnUzny7q2fHZV1wJf-pGiFBghc0B0HPbusu4Q8Xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKnl7O-0KSRH7CbDACgPtocOBRVON5vlyRyVLfUGdgzAYc79vP7UaMbCVBcrTLDmtUgW6uNnz1f2x87Hjz9W9xaDvy6QU1spL51Fi6acZcOMrUAS5gME1Ys4S93ILfpJSPhc_wMyTut2xWXKm-luyRVza5cwlDjzuQJ08Fsj-0__JfBBPmM2Lt91hqwbKNCa_MkK5wmGhSWt-RpmJjN_7Vm1m9fDgmRrKJ73DMGBX4WTaOzH7x8mVBeZ16mBK3A6NI_IQamiF-cZ90kcbknl_GHqas5_lU4aKaSi8NCGaKO4oNsIN10cozro67kGvGTIbjMRgbyyLNacDPm-5G_2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdAG3ePfDIbBN2qTXuGEGp23nfZqJAnsy4rNkq5MHzAWambS9EfruLn-58uiqCBddYXHHvynOKtjPxgKIQ4HfRK7Y6jD1o8PC4jEt_vkEy73fzaaYHk3wP7CkOx6ycMRn0P8we8kc46hno11Tc-DaD63Be0XWQNXCnFte2SrfzfouCAzBOiBEuREW4ITSWq_HGigqpNSyHBGsKwky0MCKqS_offSf5vyICFMcjR2uLSVfR4OSPGMPlK5DdBXuOhY1fyJDw4bd3-D15QeDWRkT549QBurTyILBNwWyP7-dfmDcx5xV327GzCQz0IOYG1JoC-OAkz4nj67NG7Isxn5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUuIXq_qf5SyBCf2j0W9MYEe8F1WnHN9LxPZoxfgF_sUQzRo9BLFBnwXwIcRzAK1ltZIkeTmYMRFSVqEZZt0xh6G-1gq54MRtLlcW_dP7r-sGzSW3MqbZFCR3fvn1VWLWfHRE1b-jmwb_PrdiuB4prQac4ZvCqJ8g1szL9XQGvNEvoDddoySbrgj5SLmy7_n0gSFZBvc1P3IGSF5SVVb1nhRp89QkZbk1hYABlfKznwnshqgZxPFkL2_VZeWAtBTYC9lCBvjtYw4APJwZDX5Bx07CVtt-invJtgYoP8kMpryN5Fv18FwaowDLkp6-5_M5ZC5o806JUvElLBAdTlqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3puGBFY2V8hgScBnJi9k-ah8Vchrv3Wiw7UxtUyqE1OEA0EAZn_hORV-AiIcqqN7yOqNEdagKFQpQ4EJRuq05IGsPAmeIhSPXm-QapiSBQ9DXrPG_uB8YAFPNY7usKQvO8P4ekHzDt0VDdNw9KFw2i5ov6z2tfJPK_O7xArA2MbMX9b17we9DgbKH7--JfQLIixbXFvHlHazMB1uTwtPdRr824TBpRydJOcG0gIht98Z4LkMsxs6NzsGomDRYPMpjk0tpXujF5liaGMS0YfzIfQuFBf7rTgM_Ob3wUGS3-AcMGB3-aRDqn82iHxNefkb1kpS6FxiH-TAruqEQ7UCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i29XbJyiZvqEUWEtlhGlRHVw0lJGqdo07ICK5ovhmRI72Dqp_ZocRIJu1fixhaQ9tIiOSCgeaOv7xrf4qm_uewT8x-J1iSkFIyzm0nTj4h_kPYUYDHZnENoXUpfw_I2DWql2clnps0CVpkTnHvpppMyi9_WVRkB5rsPWZCFiIDho5ZlgEDgbEEho-lyjXSmsCtwxqWOHYT6B1ql4MLqeoDFwds92XRJ-4G4w8leXG4EdObK7rAFvBTYln0dDJ1jW-fOKkkusnQksaHTSrR1HDXQUg1MYnc2eHYm4z9UpU9afs-yqq9-oGPvRAbKsGqVkQPPb7WKRQYuJJmH8OuKZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0M08ewzazZrE_gg6wy-kaSkB4BeFaKjvlstgEDXIeGSmdMtHDJqxn672-sjgXLNpBKciQN8-3JIk0j4hVK4yJwtZBiHsWgjjFvmj8MKVsc4_Q89vdGg8-78_WIQ2feWJh5_bI3mT2es55otc1-FSs-6BtJjNfXMG4pgFrNLdWSSxcwCH7ZUwCsBQkaOJAxw7ibO-GPOzotN6ibNh6p2CVJYylRHh5WldZR7EKacnEPLtlZsk3_b_3l0OP5Q-UrulXFuuJY-5U85KxSB6TaoUBBl1zEneSB5ztRe3Hd4y75djzqehnrKcRtRaVVrO-XlVhmIXfgKsfexSI1__uAADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH06cTuB-omzD8Mu0TyVnUkIj2avNe_RMv_o7DNWxWfHIJnNNVLbUkDqllytofrYq_Mxp95PCMcOtf5BI-1pDkVYn2bs_Px4DSuOQ5eCEDEexnRMgd3iSzhqv1qrCUzxpQNwiTqD5_o1XXnw6xv_dwLWGsfvZiixWBZNog3-_Pv6MmN9X7WqSJo0Xwo-bd6iEGBAqADoaJtSe9C1CoyegMqMEfDWuC6CNZHidVoefGBTE4goycJs0EJF_1AY5fiHOqLFVE0Xo5UTddUnU5smyUiW8PQM3GTM849LsClL5HPI5eankBusoLq1cDFhy88L4kTEPhtc6qHRrWNJt5n8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=CCQtdIim_Dmv3TKnEVZ7hwJ_-m-0A6J6IUZE1IGyAcpAeTEE3yHMRYOR1n6na3MaBiWJv3D3Tg0lmUL9mlI7ekFCoQKqY5ZhO3e9aoTf4QODAYyRrsnUPySyTZ0HsCgRuJPjSCrPpbyoQ7bGamZO0759e1TjvvWgZxQT5RzX1VYgBgi97DZhtAka05Tit6MZPlGcoA5epqlTmEC3dJLGRWa2S3wuPF-hfpA9aKG5yoyTNSGOQGXpT6XvjmBbJaNruOvurH_pRjDwez6NcbFAvTp3QlM5DzR7u-4urubsY3TPxjFD2xaFjYSJKrVkwkcz7VE3-puO7w5Nq0aJ7vVy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=CCQtdIim_Dmv3TKnEVZ7hwJ_-m-0A6J6IUZE1IGyAcpAeTEE3yHMRYOR1n6na3MaBiWJv3D3Tg0lmUL9mlI7ekFCoQKqY5ZhO3e9aoTf4QODAYyRrsnUPySyTZ0HsCgRuJPjSCrPpbyoQ7bGamZO0759e1TjvvWgZxQT5RzX1VYgBgi97DZhtAka05Tit6MZPlGcoA5epqlTmEC3dJLGRWa2S3wuPF-hfpA9aKG5yoyTNSGOQGXpT6XvjmBbJaNruOvurH_pRjDwez6NcbFAvTp3QlM5DzR7u-4urubsY3TPxjFD2xaFjYSJKrVkwkcz7VE3-puO7w5Nq0aJ7vVy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNmcQNRcDuDXK0AVJUWSTATJmzAdWxhsvaS5eVIaPyPo1Xi5n0ngP2_wftzQcohCZ-ZJYfv3b_NcL4eGqzy54ze-7upRIh_f_uaLyNirmDeR9XwaVU0fwZdyYzeuKIXWZQh1hzbk40qzbxxB5PvIlqP35fN6wgi5jTsNZfIQ-rLp5I9uXkgXqh4iDNrXfqZZ0sFduCOrgCy-avZJGFCQcgnBA2Dl8p7To00W8BjLtOXOirldHKUnC8SRVSw9Gf8O9b9z_CjYK_2lXZawtHiBYzQik7h4t3Ft_t6Gi1dvpODlRAmdeJTv7Ytc-9EXTLl_btoU7d2r7E9ksQymrZ-C8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZJ2m_cqruibqJn8moRqXJVOW7hfi6w5pySqINUq_tHnEVom7NcqmSsfiF7pol1tpq7h2cjv_lisqA_RW4K4IsIVeDJXpC_69-SNUX-4pFnj8cPNV_0yF6mto7_WRRPwkQx6kmwJPe8-YWg6vMLcGYR3xbsBissBJPjFxq-ZPZEGDTHCez4eYMEdkGW--VM4Mk_678DW5RtR0hYIO190cNnriW5kZDGtSc4iyO0bXMoa1Cs7qkauxGmb3tNiU6beuVD16w4NEMRwc6r7hAYGqT0A5tkfH7-ot97fdR4qvIZO-uTsBr7DMKhffzFrKYpwdILmlkM6G3Nku9l2-nS-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Dp_0pdSr6iha64JkWxhmLXIsrKCh1KvM65nJFFR97vVdBEyIaR8i4A9ubljj3O1LF_lpWp5yWAZ_ZDrqZ3jpkMqoss0m3YYLIsUCUrT3nkWfRN6l7PEU1NLWW3aF9SbYUzveJjmrcHJMKgmvC2rWD3q0Hz07zEt5ov7e4f92CN2pkAGRJ1ksS1O1wNYj2UC93IlErVP3m5_waU7XFM4FdMt7Uizw020ODyib-FcxZohp49cTmgkH2D3CPZ9Z2eC38rAPkeHsbe-_vcYQGNeGo5QidhnJ-WdmOlfyACaWLzJNvVA_hXE16Hi5go3m2BwMuaZbj53uLKTSBtnaNZiaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Dp_0pdSr6iha64JkWxhmLXIsrKCh1KvM65nJFFR97vVdBEyIaR8i4A9ubljj3O1LF_lpWp5yWAZ_ZDrqZ3jpkMqoss0m3YYLIsUCUrT3nkWfRN6l7PEU1NLWW3aF9SbYUzveJjmrcHJMKgmvC2rWD3q0Hz07zEt5ov7e4f92CN2pkAGRJ1ksS1O1wNYj2UC93IlErVP3m5_waU7XFM4FdMt7Uizw020ODyib-FcxZohp49cTmgkH2D3CPZ9Z2eC38rAPkeHsbe-_vcYQGNeGo5QidhnJ-WdmOlfyACaWLzJNvVA_hXE16Hi5go3m2BwMuaZbj53uLKTSBtnaNZiaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahLB4qaN2ifrQZ3d3UrC2JrnHE1RT3bzkH_v3pynMeT5U6xSGeHLWodLREG1sOTGqUmq9vTyXTWTtcGwRKdoc2_VD_ikr9C8Jv4gDAsJ4NkTqNdK-lPNg-lbWv7kDTEfoVqf2SZT6nExlm2LzspHL2xpDTxjAP0crAntlz3vv7LW5XanY_Rf10gNnuqzsgFlFVbIu9_LJ9ZmAkuZ15SW77ZF5HmI5njQPJ8LA82x9yfk_XkRU7kJd-KuvxoID52b9a4ZvNiD5G1MRY-hJLj-0kI8Els9n_-RN6eFCH5kWFe8CQ3pCjF2vKm4oxFVc6ql2VzIpqwN9xmajHoeF25v7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtPFFJfzrHaLsncSc_54z8-AnjHaa9HkmejTEZpBkvko3vUZuTNfAMTMm9_hUINwPwf6dYFTbD-4WzgYLiZUbhb2Uj1p6R0Urfx9jrhk5jv2wurXTRiuyDYrpUpFg7Co8q2I1CEFqVS9hetI6kyykIQoRoiht0SZP2mS4Rr4V2Nktvfgv7xk2fYXpcAHZLxW7H2JlfHOHD4gFEOy7-ECc_EtqfFbn6Wirg4Wp8sliXIcfj5ClzaZ5q0d_WjOISlc9wbOy1yr0X1R4ZRycp5mN9_Vs4PW1a9nenGLSMzxYKKCsFRH5lXZk40PSBRp-JUtCx6pqF6dSPcKQJ0uFFnHdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Z29ILQT4cBAQc-TuO-KunhqQDuY0K_AJJAS8nlTr9bdDlKKnGhgVg-h8ciS9Ka7c8O5J0BKTaro4n1KgnqNJVah2_GP8675am-OVMmelt2frG8NylalOR-lfpEKT3_ydlJYhCF_XQPP5VeeR6MkR4fMTwaPc5UpmdP9tcM4x_t5Dba93InOwd5SOUZfbcgGqS25Qgq4oM-puWvqT3_BS_GhdBYSvkyB1B0f1TPX4lNQTnKIxvNDrClPhFxEVfYWOZqdY1lYTitCYz5i2BeJH7Iya_a4t3y4kgrNqwt1m70Fv5EULhiZl-LmrlCP1TIeEl6Cz_NBPDlvyVneMdqL5oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Z29ILQT4cBAQc-TuO-KunhqQDuY0K_AJJAS8nlTr9bdDlKKnGhgVg-h8ciS9Ka7c8O5J0BKTaro4n1KgnqNJVah2_GP8675am-OVMmelt2frG8NylalOR-lfpEKT3_ydlJYhCF_XQPP5VeeR6MkR4fMTwaPc5UpmdP9tcM4x_t5Dba93InOwd5SOUZfbcgGqS25Qgq4oM-puWvqT3_BS_GhdBYSvkyB1B0f1TPX4lNQTnKIxvNDrClPhFxEVfYWOZqdY1lYTitCYz5i2BeJH7Iya_a4t3y4kgrNqwt1m70Fv5EULhiZl-LmrlCP1TIeEl6Cz_NBPDlvyVneMdqL5oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bg75GnJbURKuBZS8WZWThJEGfdtGhJRFiBAYG2PdmRBkwY27A7_Ealr_-EauXF6NDW7RneyZns4f_tVJ_8U8yfw1Y7JgZib6Z1adpvZR9dUq_-HAo18mgipX1rznDPEhq0dQdLSJLmXeHw4_-uqO-dqQe7MlEqB5YQBnO_ULo2bJdHhFnxM1TlbgbMEjLHeLH7JuHH7WBqjXp7n09j6lTvb8hAzY7s8j3zju5Xanh8__x4NYfHRk37jsUOl6mCgPNJD5HQ_Phc8FLofDt8u2uys2ACmrtMghPd8ltNkaR6lmeL1CCAaoN2usU4rnIku553K5xTMYJ9kKbeSEYEymqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QglkEuLLRYGT8DfhTVT05m57RKpcom4AoeS7KCUiw4h5_NdxKGSD05BVkExCG3WhVR-MJXcNTIf_c1U5sR5MWd0cDsMLXVidC4tPEunadihNZiBRsCZrARWjTuY4sr-wwBFkSwsduQlTRYK0lpceVmSix607KSI7BDwLUMpVBX-0xj5qMrh89OIdBxWouzOXd6SliXGDOEoB1-TwhjqwSiFmSWiKMcxMkyffs2llRaB7Eb2lFdU0B2I7PJ9DqSmB3AWffYEsfSjkmyURHpZF92iXUsaIznRu4hXiYxTHnk-N8DvomVzOAXePMItH-7Y4IK-o46fuvG4fj0dQKnmGAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=feF7NAIusK9lUf6AeVOhGZnmOfBkNPqgR0oxr2Ug-b2wxChGi0fGaO8m9jnKnRKcg-A-nbxGyThUz5GJ3oL7fO_S_xdxvmvcdHfG7Q3afHw_uu3e486aMxNd60dkSyNm-0LUUgJ2IrAWp_y9X1xnIIaL0OA2eXAFbvRyCmNdXQPimxTse3mOb1GQeaFhUifrYi6_zRdSyLPTkO9HWT2_FO_j-dgwbxVQrbQDUWTLjMmcL7f8GIaZilq_tr_KmiSrbBFGgpe1LoYP4TjPmMhHTf8-KO6dmglu13hQ6MgrsExT81N1KMxbDS5zh2bgfaxnaiJn24XUtu-G5t-5h7UxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=feF7NAIusK9lUf6AeVOhGZnmOfBkNPqgR0oxr2Ug-b2wxChGi0fGaO8m9jnKnRKcg-A-nbxGyThUz5GJ3oL7fO_S_xdxvmvcdHfG7Q3afHw_uu3e486aMxNd60dkSyNm-0LUUgJ2IrAWp_y9X1xnIIaL0OA2eXAFbvRyCmNdXQPimxTse3mOb1GQeaFhUifrYi6_zRdSyLPTkO9HWT2_FO_j-dgwbxVQrbQDUWTLjMmcL7f8GIaZilq_tr_KmiSrbBFGgpe1LoYP4TjPmMhHTf8-KO6dmglu13hQ6MgrsExT81N1KMxbDS5zh2bgfaxnaiJn24XUtu-G5t-5h7UxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZARim3Ov4tmBW8vBopJ-7G3_gP6FqmWURptEGql7jbXhxXuemGorLilcO00zbb3GWOGRF2WX1YvTtSSqCwqy4dgDDspuvL2CVEUZ0PKFZMmoUXqtEsnRgojZioxuAgQopPQRu9bD9xi7ThE2bFPNetpsryhrQeYunymBQUB_VmrIX-9iG4LhLGH2wU-SkuPeIqJhdhfCik5zz9ydbBBY0Q6Cj9Ig6oxmyfD94N1OzxUjSuD9dcXcde3hVfRb_D0XVjbwXsIDuWm2rpPb4rRFbwcXGhb6ZRbIkjkbHn2fGdPr76c6WU9HvFDedpMaISmIkAbkC4cMJNq5IV2RpRxA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6ddPdJFcGMvaFyX2O59Rn78QiBiG6QqvyfQ3zDgB14K3awRxEJ5TnTw5RN7zcQL1vMuHnrcllXR6BnAz5Kqxpl8ROlv7I3koS7mPMg0CqHz48RgKeyVE8lEx7iLtEP_bfvrQOQ3y7HIAx20-Y03ZacrBS8JHX_UK5vQQNnGtzyydLBJibHlbygWPOWMe62V_Gb_IuIEUm6-j8Kn9hZUhaqNtZujc43NX81lFfLLKK8AmpcvkgUIUjEiinuOZY5yRatLh76O9AbjhH8dTw7KVsXIOheFeWRofi302InJO0CItMGkPbsU6jLyPniaoy4kEj4P6W_GW8C3OpAcgXP8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdS09GZyheA_BTqgJ58CWiuD_25d1iFEYBSCbTZkXgMV72A_4KcEQDFqQF-RJM0dHfYrDRm10TrzNma2kd3Z-v5Dc2cBf05P8P35cs3JPAwMcvmMNcqnGB-dCvp9yMAppSzBiaa1vRtdPc-dklipbN1RxnNSs6a97stvQRw0d5ur_31hzrpdwxNf2C6uTRGgY1PQR73HSTyhHQKYldPigPFXLH8-yRStXL99TVHKrWaLzGY0ZQ02LrzQB481XAK9pKmLtZ6CwfVAta9-B2F4eR67tgVjrHwHoPgVOVmKykJWPH5MlkRgLW4nY4s7f04ijj-5s9aIsNVORotT24L-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDhYm1PALNzIHmMkqKYyO1rcQvTUL3iYAk27nxISUlSFh6BbIkkhnsHUE74kT_KA7hqwEIC1G396YJhkc2w1vFG651t5_ANdTyEj1ZRE4SdRyxkUm-crBrAlGAYrdcNblxUqSQ-mJaEJx-QkMwFA4UzJ3cjHn3rnGOYNQYO_FLQoVJUIoEIu794eOAcHHXr-nh9X5NxCs3OUqcLdOKOz8pHLvp3hHAvZiZSKWpZpwpnu45GUkkQqMfcNCmt77SDejp7SxWtC_jSDLB_UwfJXUtRzhfPwigsyxnIOa8nRZTIyvNly2nIR-zOvUPwejyvgUr-6G5U5g5J-Z5qFEXuMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVAgtutLxAlEDgJubtcIRsnU57RTqt1lwa-R0ehMEcfT1NdYjO1UbGna4xh9d-LRDTTbuT2yNSs8lfSmb4_5WjFa6leZ7pshCUKpkopTW9cKtN8JAPOuV2P13LhZ0IPH_ZW0pRyw5hy48fwlYRFfHsA-4wCBxfEGp7ZStYN3PRD5KBhxlFdPrDaQqTp3HaJfrXAf5MJ8I-eyz-1vRq-mEELwmWmrbwYkt1HL9VZwpJihjLPYf47sfudqH2GVQ8TtTEHfA0TXS6dx8DTir1LX8fBxwFITpVWJiGSE5-T7M439MH9XzeZVz8MCXW4GmaXHLzLxT9UE8MkFTxihtR4rmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPJJGi0twd-GAZlk-uJwoej7IcbuCQvi1WTpdsKqUM5VG_UD940GDKPE68xNSQHXlOyzPkeaSWmPONebrrxfraojGncEs8S7PJfEyAqkbQFvA7z8xgp_UIyFt3gB0LUKdTeV1ZJ-aPrpfgIHWYh3dpVtrN8rtpUucyqTD6CSoeQ_i3ZIcz6AHx4D2qyRMnRv5CQMZcS6C-QL9CTcKdXMMmkI-ppzW-ql5_diHlmN5pf9AF-f-s-pvfpDAhOATgOUMQuOB8bavYwwBymAlyscazQ6UqBwEShFBdjV31hUD2OgSLcufaApR_zzELIGRrrkZU5oBTDwjfHdNrIOEwaK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_FUqwv0vfULBiG_aBZWKLNaq0bOQJpja7ZVrTzjiyTqv_8wppE0Ad3wYQPeeA_UK7RfqBcnSiV1RHD6fQp6fN5HqrATfJmbzi8-f0LEQ0fS-ZH3gu3bMk0jbXIYqxdpAqp-R977dQk2qw7Xld3Yj43LYlR3CGjghVZx5gsk82WENTh4_JOwfgNrsC0j7AxarGq3D21S7Xlx1jZWIThN2vldYksjRUr9KWhKN7RjCLkkM2gU-gSRwc8kFKJRl7G44avpSdIOvTjYHFiTANBDQy9e15zqlFfiigQ0TgmeVbd3_2AGbHyYFtmlzQq18rHuYPCsRaFg_NXGnSTHNX3Ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhWUQUsI84XIFwWxvOO5U8FHCkOHZOToSgIs-IOqihZAfN4HxlxkGVRjBwrOeINN10uopglhWqWmGxgU1oDS63ugvDajU0OBGjW_XgpnP29XKWTts8ZaUndh7iR_CGmkfeXIXHVm3NN9_PhasrSAbbow-QA2vjjY5OLUk-Ryy7Vt1C-myKJNuV9M7zrAMFUyUczBYkYuMbooyuIqDjDKmBMnEq2cIVtytEmpSm1wY3IMZ9ptRyaYgjDOFr0ySKh1nuxnggWyfZWyUdHN98x0eneb7ZriFXp3y3JfJMxu5VvrszRslxzgbKy_Gin1qJtfEiSq3SysfFeghw6Fe6FO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=SivN8P4B37TedFJCIHF6B0qQNvaFHYQxDO68cbOnGi7WUfYkJgdgdew58Wxrvk_okhqKz__edHbWjh_QhgJGwjALzt3a3HFBFz2854Cryk-5T7XhZb6N9BNOauD7yXfMn0RjfV-uzVioKZaigMIeXg4NgKI0dH_Q5Ve3iZUe53NRBJ_GTNx90TU7pEoXqUTjUYLM24tBY4cdV-gN4qxizfC3Dk5A82qSMa1WSC9fvdDNV9MbwMS_wTye9pR8TZ2ie6ETqOLvOA-qrEph-keaj_MZNnOLlmKrhyrghuN0deH9PmLlMhcG_pHoS0vw_a9TNLAdlZeIOEiQjRfkWIPhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=SivN8P4B37TedFJCIHF6B0qQNvaFHYQxDO68cbOnGi7WUfYkJgdgdew58Wxrvk_okhqKz__edHbWjh_QhgJGwjALzt3a3HFBFz2854Cryk-5T7XhZb6N9BNOauD7yXfMn0RjfV-uzVioKZaigMIeXg4NgKI0dH_Q5Ve3iZUe53NRBJ_GTNx90TU7pEoXqUTjUYLM24tBY4cdV-gN4qxizfC3Dk5A82qSMa1WSC9fvdDNV9MbwMS_wTye9pR8TZ2ie6ETqOLvOA-qrEph-keaj_MZNnOLlmKrhyrghuN0deH9PmLlMhcG_pHoS0vw_a9TNLAdlZeIOEiQjRfkWIPhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeA-vDv-Mu-xHA9VSuWn34KRcWXmLKdLnIuqaYV4YUfVybmhf2kNM_RR82oIUNC1zrXifNQZ9SfYAnAYYWn3yHA4yuJaw4VvTwZvbFk6tQxNjptVgs_x2NMWkkuFW0UJOufv6XZTBIwvnQ1ZvW1gyeXddzLtDYdl4XZfsmZNRFK_84mr6EiF13HycBhuX5qfTEIwpgwvv_FpcL4RvcQcFVxKzB237-kFCDvFzaxV8KXh_a0TKi_1XNcBWOlpohlEwxFQnVJqJTrr5DyXZYphPLEcH_ZiPsdPBPsAJ7OAoUNFXYHdFhoas1OPudtYLghbpJyTYGJ35O-3s-1d18zkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=K4LqYmBIA9iUo4nXH0YGnynKbkC9cdPJTsHU6698P5uiBe7jQ3P0PzY77YjW3KoMhXutiR4OcA2KKCWtSD033kbv_wvarGvweIqBvb3Eom9pBEAXfwFeX728i04ysWQtLR1ZDAsjVkD_KNcKCCl-RVXVogeftihe5V3TO9cjID9Amu6ZWm9hB9SUv4N3vwWnVSfhFNnbYOHeb8-VNjuDCevJyX_iTUV3DpsF1fqp4YQJKaHpPUkE-yXe-lANhAgF1I43xD4785nYCiHfF62c4FmAFLYWUWJCKT27L2_FRFon1cFUWkgx50oN5Dm1GNR_uUL3uC9gX8mKYrY7XBipXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=K4LqYmBIA9iUo4nXH0YGnynKbkC9cdPJTsHU6698P5uiBe7jQ3P0PzY77YjW3KoMhXutiR4OcA2KKCWtSD033kbv_wvarGvweIqBvb3Eom9pBEAXfwFeX728i04ysWQtLR1ZDAsjVkD_KNcKCCl-RVXVogeftihe5V3TO9cjID9Amu6ZWm9hB9SUv4N3vwWnVSfhFNnbYOHeb8-VNjuDCevJyX_iTUV3DpsF1fqp4YQJKaHpPUkE-yXe-lANhAgF1I43xD4785nYCiHfF62c4FmAFLYWUWJCKT27L2_FRFon1cFUWkgx50oN5Dm1GNR_uUL3uC9gX8mKYrY7XBipXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=SvnttTElLYktlUGFI4xiFXzf-bkDnXW6DN44yfJVfK0lqkQmu3RE8E-jXx65qNiXhx2gEjnoDx5cycPZbsYHhZC00wwhkjWQJAZliyG3U8riQtNQHwOj9WgPcL7XjYzNFt03VnyBWY8keveiDA_XHNhg74UnlrDIsyIbWOcLgXYu5v_kUod91foD1az2JZBp8DrrOwzbppV-hWXRWpH0zvVfZMuleBvaXu80-U_WcEsRiAd4NtaChJ4ZSP9uH4TAmcVqPHlEmrvqOi05B4Wo5O0t1kN-0YKPulo9xT1Ill6xqhF71UXME9PKZ8fzI4ETmecRnCXyuLTli3CK_DQlnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=SvnttTElLYktlUGFI4xiFXzf-bkDnXW6DN44yfJVfK0lqkQmu3RE8E-jXx65qNiXhx2gEjnoDx5cycPZbsYHhZC00wwhkjWQJAZliyG3U8riQtNQHwOj9WgPcL7XjYzNFt03VnyBWY8keveiDA_XHNhg74UnlrDIsyIbWOcLgXYu5v_kUod91foD1az2JZBp8DrrOwzbppV-hWXRWpH0zvVfZMuleBvaXu80-U_WcEsRiAd4NtaChJ4ZSP9uH4TAmcVqPHlEmrvqOi05B4Wo5O0t1kN-0YKPulo9xT1Ill6xqhF71UXME9PKZ8fzI4ETmecRnCXyuLTli3CK_DQlnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=aBtWsBWWUE2W_Ypd2vIFUA-K-F9-Bqa4lPib5N-HvQ2Pf-N4On0gXwHR7kXSi97KQo7JTx1BOxdrNc5akqfkdyjbbTXrLim3SuWU3zS6dIG1rCSULW00e3hXNhTLIBsP9isC9B5y7tqvA0PIGMHSedU61Er70FzxFlIWZwr2-rxqYUvs9pUr8xyRSybw-Awjg-0CDrtuOtKzQQ1VVImOxcCwSwiR4N0IXS7PdDvgSJHmTEEu6hrLnWZAPmWavsOjpKND92Og_p5qiIrZoT4JcOTvX_A__-Mn0w15aetPHBDqeJCU_Iw7Gb_6OvhLcIP7WAjmhgjhj1IcgBclMJVISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=aBtWsBWWUE2W_Ypd2vIFUA-K-F9-Bqa4lPib5N-HvQ2Pf-N4On0gXwHR7kXSi97KQo7JTx1BOxdrNc5akqfkdyjbbTXrLim3SuWU3zS6dIG1rCSULW00e3hXNhTLIBsP9isC9B5y7tqvA0PIGMHSedU61Er70FzxFlIWZwr2-rxqYUvs9pUr8xyRSybw-Awjg-0CDrtuOtKzQQ1VVImOxcCwSwiR4N0IXS7PdDvgSJHmTEEu6hrLnWZAPmWavsOjpKND92Og_p5qiIrZoT4JcOTvX_A__-Mn0w15aetPHBDqeJCU_Iw7Gb_6OvhLcIP7WAjmhgjhj1IcgBclMJVISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdUGWrKADRiFQpzQR8yhZ7W0JiWXxnFvg6EPAy9URjI5-Y6cbnOHk0bpAfMajZQSWwHnCwOzhWu0LtD3nOyutA9_saOwcasNqUNnrNYFHHMRgTwIYyaq0jtKVftuWV-nbLrNe8BJQVK-zixIysQq2TMIyPnXyV9FIb38KRYuK51SDxra1sBsTT4hRdL_18SYklhCHyeEg17kH6JneBwhQARdUXAO9IFfcpZVzoLmmpWtB8J5Dm5RZd9_7XLQIOUQQJikuvn3w910V_I_dQe_vO1F0pqU_GMRLbOQW76i7RcmQ8573WyTL43Ig4ZZDBHMtYZMXbkeHdhU9OheUJtqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_jPJllgXbT0R1mWaVTqdaPbPk8vVitqD1EwaiqM6OAfHJMwa8qcbL-mU6Vf4RRu36AnuebHMJHA5O-1Ok8egnoSKVdZQ-ihD7sKZ843rD186he3vt60Mxk1lcRT6plZGaboPevWNDlIfou4NeCpePeWvQL-Gl3wa5PxCE-qJt7YNCHoaj94q33m2piXyyBVGy2uGfTplE-sb7U-pAGQBCwcJrAda28frTwreZHhVqMaVDFfNufx4jAvgropZHLsio1CSHu99NfJaizCFT7c_3PJ4Fz4QzgRTew3ktwacL7XtvDKBSy9W7fDTFFCMpbQfT7jIArAp2LGgq--eWG9hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=lVD6tuZozdR5kcH5O9853IVUdkc6cvAyBRy5G3NG-Yq6AEmhoeW8B49-_SEC1ppTCbDgfzskKlQfUccsd1KrCGsCPKRULnP27Sdf3wbFrX-0btwkSexq88XceVRXqNPA-6es6L3FfZeFxExZejhsHZd4dSdufYPi_PDLTw7kN1tpqw_-ewMuFzyMjLqyOXunx-2XPR3dDGQxMtn1ay256A04fLZxAVZONi4iYMncSP2jAtHsF8rtuJj_6nADpN2Y9z_z5xMvLrl3roEM8F_8K3r_x1uik4Zj9VtG_JMD64X14q4Cu2lBJ4ePXs0jpe_EExkELsfcRVZf98_wSCvAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=lVD6tuZozdR5kcH5O9853IVUdkc6cvAyBRy5G3NG-Yq6AEmhoeW8B49-_SEC1ppTCbDgfzskKlQfUccsd1KrCGsCPKRULnP27Sdf3wbFrX-0btwkSexq88XceVRXqNPA-6es6L3FfZeFxExZejhsHZd4dSdufYPi_PDLTw7kN1tpqw_-ewMuFzyMjLqyOXunx-2XPR3dDGQxMtn1ay256A04fLZxAVZONi4iYMncSP2jAtHsF8rtuJj_6nADpN2Y9z_z5xMvLrl3roEM8F_8K3r_x1uik4Zj9VtG_JMD64X14q4Cu2lBJ4ePXs0jpe_EExkELsfcRVZf98_wSCvAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=n0cYzl0N4n3_iPGi5X1kFM19XROD7cnOcGP2htRNQDzwzTvXP-Q4-rwsIk2aoMpH3h5a9Okx7R9K5sTlcvpAkTg3SL4OnvKxhhXBpFXqlgZUuX2eu7BuyfeZEK74LVICm7boF_OHuq8VMe6VYm3E7cvJxwCMWU-bQvUsDvGZXJKtdCAfOvjBhzZDDJJ8HTyrF48zO3mn1TUl29PS2SzvgLTfcnAqKoQ55U8egh4gKAue2YIKIc9GmrzsHzTWHmUn7SG1J43UZ4J0d0v18AYREHAozrWhDv43f8lj7uT9Rt8OzZNExfh-I7MMRBu6IH-R1N-4uKFBN6CbME80f2JZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=n0cYzl0N4n3_iPGi5X1kFM19XROD7cnOcGP2htRNQDzwzTvXP-Q4-rwsIk2aoMpH3h5a9Okx7R9K5sTlcvpAkTg3SL4OnvKxhhXBpFXqlgZUuX2eu7BuyfeZEK74LVICm7boF_OHuq8VMe6VYm3E7cvJxwCMWU-bQvUsDvGZXJKtdCAfOvjBhzZDDJJ8HTyrF48zO3mn1TUl29PS2SzvgLTfcnAqKoQ55U8egh4gKAue2YIKIc9GmrzsHzTWHmUn7SG1J43UZ4J0d0v18AYREHAozrWhDv43f8lj7uT9Rt8OzZNExfh-I7MMRBu6IH-R1N-4uKFBN6CbME80f2JZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOH_R3ajhmxjqxZiwmsbsWl_s6DrQ9B0BB5IAmK3J-DAjy0gJc2CEIOGvL27iDTb-7fZP2-U9EfqWJ4m4TiQQuT0QR_ewDNDSTjoxRYCSEE3zNiRLYJ1F6QuXut1jm774LvUDC_AwziZnpskggKdaqyiiH7YxIw0_RzwSFJ6E3WSRFOYP1AvDw24jkP2PtlJMhqNRjaW2B3lbD-Xb6eTuqOk43UwJn5-fnObM2DP0usobn2Pf7Z1hEjhHWrwvS6Mi1nR3YnaOFtr8GBJZc2VzzxtebngIQzKPxTwg7oS0ZKl7nVr-gsUJLyc_HZFaWypfoqsFT_vD05PBOQluv2Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=LZa1ew9N1U8Bo8Zu5uC5nnS05ZG4T_rrj-H4ixuIGFeLsPW6BppfdvYq3-x2nljKjWKQIUp8Xm9kHRBX_qNHv4nwPxvpfNAXBPVmgArIwbJD9yTznqmmX6zoXoi9UJ-Ajt131XK0yBTzr4nPV9raGjtX0sKOLHEiO9_h_NTnxxK8HIHq6cEAId4gip76EN6ds71l_JFxL8O0kFibqwrnVDRypa1gZ-_shAzZVN89RFNuYRZW7HX2UYmnP9cBiYpK8ewCGsZJGM2F8hlPOvKxjBodExWGQhSv0M5QzQs0VKwZxU4AqRnQgMvRFV3x69DkMQon3lG13afW1SAI3J-ecg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=LZa1ew9N1U8Bo8Zu5uC5nnS05ZG4T_rrj-H4ixuIGFeLsPW6BppfdvYq3-x2nljKjWKQIUp8Xm9kHRBX_qNHv4nwPxvpfNAXBPVmgArIwbJD9yTznqmmX6zoXoi9UJ-Ajt131XK0yBTzr4nPV9raGjtX0sKOLHEiO9_h_NTnxxK8HIHq6cEAId4gip76EN6ds71l_JFxL8O0kFibqwrnVDRypa1gZ-_shAzZVN89RFNuYRZW7HX2UYmnP9cBiYpK8ewCGsZJGM2F8hlPOvKxjBodExWGQhSv0M5QzQs0VKwZxU4AqRnQgMvRFV3x69DkMQon3lG13afW1SAI3J-ecg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taHM03-1B0kBd0Okd4Xk1zS76bsag0Pt4DNXTkrsoq67s3VmbXQkp04ccG622HC2pn4ZAviuSg-wzsiuwItKGa-z7wpCk5YJ7gg2WjsRA2jh5sT8kEEnQ4iX_Rv13OdlQiMvM0s-Bj2f2tp-G9KccR8qnX_S6xjrDmSHHVsq9bFXrm_G1gdD70NXLbEA693pGe9L-Vin531uinwlIfSKIahCEKnviESvU-lY5bthSs2wipsgckJ9X9rcOC4SyPN7MSqZ1q6uP9-4Q7ZVDnuXq8YIAr0iNsRDsWzn-rY11ok4MMb9Z0f__8c6KyCiy1A8qDdz-4-B5wKzf-0xFR_16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhsXxtyH6wMhQnLwbz2n3BAYDf9VXlP0sYCOk8Ai07FYCyqj3cWfwrE1_GwfjZguQfDgFiNEhA-jAGpltiOplpIOHvhlsPfVXlEUik-p4hmqTqCNGBCoBImfSFe5aazvBkoGkMPgkeh8Brz93RKo09polWvPg2xD5Bm91jVDSRwEmYG7iRGFXa0jc5oPqs8VG_xFoHuYLuD3N2D67QoFHKB_Tt-DRDl5TZs3emOgYON-8-Uf_QbR06lDt7JdhYRi2LEU72rjTJ_Y9L_-oXKFnQN8O9LGxs3EeintcB-yOjO-VRJOSQq_CUvfyFE-RXXbM6W1j_oS2SD7rO9yZbHVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Manw9xbgGz-BKRTSIXRagwmUT0oDErtGA9GxmrmghFjas9m63uxa8VNpKAasCtpxbBdgT45jgSCcujAlMw9uJzG_t5nUksI6LY8ak01DPKFRIlLItPZVtZ7beP1BmOjPDrZW6qKjZ3i695yJG14rC3dOKrhfWSc9oi6Qh60jmpbGY1VBPi2OhauyQSveBWRubovNsT8ccqcFGEfAy8DzZPiXVPlka7W4bTV_1PuwzAS8HSzFcWMz5XEGx9ZoBDp53K1qkhbE7E6WxtqY21TFmcpt7OBqRdUqXYeG17O-pMSjDvYqn6n_Vg_WScB1PqEvnOknTEoX-WZpniXXY-8A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW9PjZTsE3tSaiHvOzPHr5wpO9OZCH8FGVjgEfy4DUIbNKYdVm19SQO9DVlb3H_w-gaPqh2O_QdmWGS05qe66xwBYShU2dEspK2Nw1FRORHbF7YytJwxvfCKsTXdYDaXXY2w1yntYCXFqc0v_pVwfDC2Y7RmpYpacexYt7vfN6spNtVCzwyw6VMeFkfyE_AzWaad60YqII41A6EYe_N5_H4HtuM2nEaRlsFX5tifo1Wtio4Nqby5TTbn6O7ntVwCh6ggLC2Exn5jtVVUKvL7GAzBU4fp9bGWdRCgMo1OcOrubno6aAOzFlHKz9Cvh5Z91hzJpirGlo3kklQW_VMvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
