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
<img src="https://cdn4.telesco.pe/file/djbIAeR2SgH0QLY90ep8InQ7S2x7dTt7vaf_Hd-HMmhSscdnBW5BfC4NoNUSKPvBdhwvqIILWFpVpype44retZSXUP-l0ki5J8aLZjlzHvcDk2t7Bcwy656O9lFQJT4hzJP96DDam0LdYPoV5GVhFQHrQtqI9CTL9OC8Jxy6XBQZf6O4wWLLdBsFxWUpTrbihJ8TY_6Dvt28k5uFD81sGVsSmK19bIdlDuDuaAQ3GA640CBurIiBkQjllf7pU-6GkdusZiEGhfFyDeX491J7XFkfugg_6ntBAuIu-LoDR9ftQ6v7bi8nWt2PhsCmw6kc_k1edCcizgizQ7QSnYfQNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 22:44:19</div>
<hr>

<div class="tg-post" id="msg-681785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/akhbarefori/681785" target="_blank">📅 22:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رئیس‌کل بانک مرکزی بر پیگیری مسائل صادرکنندگان و پیمانکاران ایرانی در عراق
🔹
رئیس‌کل بانک مرکزی در دیدار با تجار، صادرکنندگان و پیمانکاران ایرانی در سفارت ایران در بغداد، مسائل و موانع فعالیت اقتصادی در بازار عراق را بررسی کرد.
🔹
موانع بازگشت ارز صادراتی، مشکلات تعرفه‌ای، مطالبات پیمانکاران و نیاز به ضمانت‌نامه حسن انجام کار از مهم‌ترین موضوعات مطرح‌ شده در این دیدار بود.
🔹
همتی با تأکید بر اهمیت بازار عراق برای فعالان اقتصادی ایران گفت این مسائل با جدیت پیگیری خواهد شد و بانک مرکزی برای تسهیل فعالیت صادرکنندگان و پیمانکاران ایرانی و افزایش هماهنگی میان دستگاه‌های دولتی و بخش خصوصی تلاش خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/681784" target="_blank">📅 22:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/681783" target="_blank">📅 22:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان رو به مدیران: شما می توانید در روش آموزش تغییر ایجاد کنید
🔹
هر چیز که در جستن آنی، آنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/681782" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدال بلژیک با بزرگترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ  این کشور
🔹
بلژیک با بزرگ‌ترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ مبارزه می‌کند.
🔹
این آتش سوزی تاکنون ۳۰۰۰ هکتار از زمین‌ها را سوزانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/681781" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681780">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Nz0EqjrY6xU91-fsaoL1YygN78UlDGdctHhAa-br0LgU8FR-GTkP8B8y4fKYsVmcqK30i0RQx5dUcxjQK3QJA5jmM3jeya3tqFu3aHrvyFYZB5FxrVw7jjm4at-ofXcKnTHxO_bnRTTWNGXg1SiQrVaJTnzE1fWbEGe59IBRYV6aVSLbBE-fM502UTiZXV1bFLkP-pDjU6WKKPsX2Dr7JceWAweJ_M0muM-LvwuTwty4rhIoPSTMKg8c16Lb9poSdljjKHKWPceDLYjmgVGfhrYrrz_kQ0CSfTcfAmqSfi6RfPLQrdKrpUHQs5bmNXAPxm9vtp3U1d2XZ5cvA3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری کارگروه ملی امام رضا(ع) با حضور تولیت آستان قدس رضوی و وزرای دولت در حرم مطهر رضوی
آیت الله مروی، تولیت آستان قدس رضوی:
🔹
آستان قدس برای اداره حرم مطهر و ارائه خدمات در داخل حرم، به بهترین شکل ممکن، نیازمند کمک دولت نیست؛ اما آیا تأمین پارکینگ در خارج از حرم نیز باید بر عهده آستان قدس باشد؟
🔹
سالانه حدود ۳۰ میلیون زائر به مشهد می‌آیند و هر زائر نیز دست‌کم مبلغی را در این شهر هزینه می‌کند. طبیعتاً گردش مالی حاصل از حضور این تعداد زائر، رقم قابل‌توجهی است، اگر از این گردش مالی و درآمدهای حاصل از آن مالیات دریافت می‌شود، انتظار ما این است که سهمی از این درآمدها برای توسعه زیرساخت‌ها و خدمات مورد نیاز زائران اختصاص پیدا کند.
🔹
انتظار داریم در حوزه حمل‌ونقل ریلی و جاده‌ای، به‌ویژه مسیر مشهد ـ تهران، شاهد یک جهش واقعی باشیم و زمان سفر ریلی این مسیر کاهش یابد.
🔹
از مسئولان درخواست می‌کنیم برنامه‌های مربوط به دهه پایانی ماه صفر را به‌عنوان یک موضوع مستقل ببینند و آن را صرفاً ذیل عنوان و سازوکار اربعین تعریف نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/681780" target="_blank">📅 22:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دندان آخری قصد بیرون آمدن را ندارد باید اینگونه آن را بیرون آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/681779" target="_blank">📅 22:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آموزش و پرورش آماده برگزاری حضوری کلاس مدارس در سال تحصیلی جدید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/681778" target="_blank">📅 22:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapptrip | اسنپ‌تریپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAzVzMZ5ouN35IrEXIOFZGDanT2hKjPUKzGxVKlNEmN9sOWwvALxFRwjFHb8V8r2FlP6oP5ROMc_7QWAMXJFeu7i_ZgPSDezmtCPuJV-vKJANEnrOKEKW1Af70NMiSrVLlnxNCgCwXnK14xdPEvRaANyxEJuleBBGspNAfXayqoEmmx7WLLJzLs9yrm1BR3JptjZ4u083S_Giwdidwnls_m6gZ7ixvDUFpvmU1V--QN5KszIN3GzNUEUfnIVdm4Pf26Q5BkbVDqb1molvzc0MNWhDzZmzU2GOTInBbgjv9yqowDJKDRDYKLS93AeychctEs1xiIJ_qcTU0e2rMYW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
: پیش‌فروش بلیت قطارهای شهریور:
«
دوشنبه، ۲۶ مردادماه، ساعت ۸:۳۰ صبح»
🔺
تا ۵۰ هزارتومان تخفیف
با کد:
SHAHRIVAR
50
✅
خرید از وب‌سایت اسنپ‌تریپ و یا بخش «بلیت سفر» در اپلیکیشن اسنپ
🚂
خرید مستقیم:
https://snp.tips/40lda
🔹
@snapptrip</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/681777" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
اعلام آمادگی جمهوری اسلامی ایران برای کمک به زلزله‌زدگان اندونزی
🔹
مسعود پزشکیان در پیامی به رئیس‌جمهور اندونزی ضمن همدردی با زلزله‌زدگان این کشور از آمادگی ایران به منظور ارسال کمک‌های بشردوستانه خبر داد.
🔹
متن پیام بدین شرح است؛
بسم‌الله الرحمن الرحیم
جناب آقای پرابوو سوبیانتو
رئیس‌جمهور محترم اندونزی
🔹
وقوع زمین‌لرزه شدید در شرق اندونزیغ و جان‌باختن و مجروح شدن جمعی از مردم آن کشور، موجب تألم خاطر شد.
🔹
اینجانب مراتب همدردی و تسلیت صمیمانه خود را به جناب‌عالی، دولت و ملت دوست اندونزی، به‌ویژه خانواده‌های داغدار و آسیب‌دیده، ابراز می‌دارم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/681776" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bvxX-Z8fn-xnLXxJkp8VfKeuFeugB48vzLFD8f_-8fFE6gI6CRLACRlcQjY-XaBeMDxKb4V-wzMdSV7oAEsHbDxkO492q17HRltCA7ylyQtImP37pA9CkDUQS7yFpgXAuZj4pU9K4LRWMW-g986UDOCd3YCVHmYPPpbn0it7xyEcdGpOBwyDPPqBU39naQmrtfq3Ujlb-Dc3pjjZ0hTQD1_-BxaR9r8sE7IcV3dTfn556WSRmuG7DaDZD4HpX3uyNt3O8qhf-xBy2PYnNin_JADu_uHbsm8TJVx5QMadhd7BdT3NtZnWYNvMXtK5xF9HFRsw6dGr4Z5TKH_3ymPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جعلی یک کاربر هندی درباره ایران سر از سخنرانی نتانیاهو در آورد
گلف‌نیوز:
🔹
این ادعا ابتدا از سوی یک حساب کاربری هندی منتشر و طی چند ساعت، توسط حساب‌های پرمخاطب اسرائیلی و سپس شبکه ۱۴ اسرائیل بازنشر شد. در نهایت نتانیاهو هم در سخنرانی خود به این ادعا استناد کرد.
🔹
فاکس‌نیوز نیز این ادعا را مطرح و آن را به‌عنوان نشانه‌ای بالقوه از نیات هسته‌ای ایران بررسی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/681775" target="_blank">📅 22:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش تشخیص کابل شارژر اورجینال از فیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/681774" target="_blank">📅 22:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زخم اصلی اقتصاد
🔹
ما در میانه جنگ و تنش با آمریکا ایستاده‌ایم، جایی که اقتصاد ضعیف، می‌تواند به اندازه یک تهدید نظامی، امنیت یک کشور را به خطر بیندازد.
وقتی ارزش پول ملی زیر فشار است، تجارت دشوار می‌شود، هزینه تولید بالا می‌رود و سفره مردم کوچک‌تر می‌شود، دیگر نمی‌توان اقتصاد را با همان نسخه‌های دیروز اداره کرد.
🔹
اما زخم اصلی، عمیق‌تر از جنگ و تحریم است.
اقتصاد ایران سال‌هاست از بیماری مزمنی رنج می‌برد؛ دولتی که به‌جای داوری، خودش وارد بازی شده است.
فرقی نمی‌کند دولت، خود را عدالت‌خواه بنامد یا توسعه‌گرا، محافظه‌کار باشد یا مدعی بازار آزاد.
🔹
وقتی قدرت سیاسی از سیاست‌گذاری‌های کلان عبور می‌کند و به قیمت، تولید، تجارت، سرمایه‌گذاری و کوچک‌ترین تصمیم‌های اقتصادی دست می‌برد، حاصل اغلب یک چیز است؛ رقابت کمتر، رانت بیشتر و آزادی کمتر.
🔹
دولتی که به نام حمایت، قیمت تعیین می‌کند به نام عدالت، منابع توزیع می‌کند و به نام مدیریت، بازار را محدود می‌کند، دیر یا زود انگیزه تولید و سرمایه‌گذاری را فرسوده خواهد کرد.
🔹
در چنین اقتصادی، کارآفرین دیگر تمام فکرش معطوف به مشتری و نوآوری نیست، بخشی از ذهنش همیشه درگیر بخشنامه فردا، تغییر مقررات، مجوز، مالیات و تصمیم ناگهانی سیاست‌گذار است.
🔹
و درست همین‌جا، بخش خصوصی واقعی عقب می‌نشیند و جای خود را به انحصار، وابستگی و رانت می‌دهد. جایی که سود خصوصی می‌شود، اما هزینه‌اش بر دوش جامعه می‌افتد.
البته آزادی اقتصادی به معنای بی‌قانونی نیست. دولت باید قانون را حاکم کند، مالکیت را امن نگه دارد، امنیت ایجاد کند و با انحصار و فساد بجنگد.
🔹
اما مشکل از لحظه‌ای آغاز می‌شود که داور، خودش پیراهن بازیکن را به تن کند و بعد نتیجه مسابقه را هم تعیین کند.
🔹
رفاه با فرمان ساخته نمی‌شود با آزادی مبادله، رقابت، امنیت مالکیت و امکان خلق ارزش ساخته می‌شود.
🔹
شاید سؤال اصلی این نباشد که «کدام دولت بهتر اقتصاد را اداره می‌کند؟»
سؤال عمیق‌تر این است «چرا باید دولت تا این اندازه اقتصاد را اداره کند؟»
🔹
شاید برای نجات اقتصاد، پیش از آنکه چیزی به آن اضافه کنیم، باید دست از دخالت‌های اضافه برداریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/681773" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-xZ8in2HVNPYX3JGuD4Ke53bhr9SYP11UNaHkqbdgnKOLzXC51Snhat4h_778VWq0kodT_E0ADEFNm7dRprXdWPgErlmOttHj2Szm2PG60UAq4-GXehEKGXeExZvW8FkPKXro5mtitGNx0h3EOi1z7qSLdzqfoNTmWhFaQB9VQcqZLW-uzEK7U3pcC1wj31K07mVrvGYf64uOdob3kArDJzZ3fSn5hQqxJXJhDTics7j3CZ2WJIWiV8k-4d9VUBOKdw50xn0i2uyrX5vhBIBvm4DFuvWMuuWgmY97FXhZrhPgFQBNbT_ATlGprE_GiajSCovOslZmrnUXL3fwsphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعضی رفتارها، آرام‌آرام فاصله می‌سازند؛ حتی میان نزدیک‌ترین آدم‌ها
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که خشمگین یا شرمنده‌کردنِ دیگران می‌تواند رشته‌ محبت و صمیمیت را سست کند. رابطه‌ها فقط با حضور حفظ نمی‌شوند؛ احترام، ملاحظه و حفظ حرمت آدم‌هاست…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/681772" target="_blank">📅 22:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عارف: دشمن می‌خواهد شکست نظامی خود را از طریق جنگ اقتصادی جبران کند
🔹
معاون وزیر نیرو: در تلاشیم دورهٔ زمانی صدور قبض‌های برق را کاهش دهیم
🔹
وزیر دارایی عراق: بستن تنگه هرمز اثرات مستقیمی بر اقتصاد عراق گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/681771" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
احتمال تشدید درگیری‌ها بین لبنان و اسرائیل
کانال ۱۲ تلویزیون اسرائیل به نقل از یک منبع امنیتی:
🔹
ارتش در پی وقایع ارتفاعات علی طاهر، خود را برای تشدید احتمالی تنش در لبنان آماده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681770" target="_blank">📅 21:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEUIS9FxuimFYIaZkoBF2tXaEmeC3LSKVMnSp9DVpTQUEkcbwe2376Kx08FdHLB8SXlLdaR8H2q78L35V446bRASgqzRrsELIAoYag3M7CeoEvNvwYh7Eo4J7o2nq-ciI3PULy3rIu9FCZM7ji5sXv_RIAeodvIvjm200dUPP5fjV3oS0ELTgmPuS-YnHoBFJV-rIvIavvZHa6c7tHntXo8ISE_vwk9P3JScR4LbImMiKeSI3PxkuT49XOIO3HVAjhiyTY3vIH64TgLiLcCkwKUk9FQ1Wul9LaK1t8VpCpKhzlUUx3hyTPbFB2i3yQlp72hZ-NIKzPdjkRjs51Rl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده توپ طلا در راه ایران؟
یکی از بزرگ‌ترین ستاره‌های فوتبال جهان در راه ایران است؛ اما هنوز هویت او رسماً اعلام نشده.
طبق اطلاعات منتشرشده، یکی از برندگان سابق توپ طلا قرار است به‌زودی در اتفاقی ویژه مرتبط با ایران حضور داشته باشد؛ ستاره‌ای که سال‌ها در بالاترین سطح فوتبال اروپا بازی کرده و افتخارات بزرگی در کارنامه دارد.
نزدیک شدن به پایان مهلت نقل‌وانتقالات لیگ برتر، گمانه‌زنی‌ها را بیشتر کرده؛ اما فعلاً هیچ نامی به‌صورت رسمی تأیید نشده است.
کدام ستاره در راه ایران است؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681769" target="_blank">📅 21:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4a0d90a9.mp4?token=SArPQqRwHr7wAoSeVogczAu4HvdjBbaDwZIqyq202VZXRn9aIxW-L85N4Kkt2LhE9A_bcQn0UTqdAic01ap1U8y5j_RyJ2v6eYqstOLQcFzihqehmolSNSU5rQLiNSReN2mcKE_uHVGDNLTtWC88nxuPyfLSfywWmpPqrwrMw4RUuh9qqrGEYa9KIlWtYhEwCqeB4L4kGoCCvVBtJIjXwvrDEYmwqyodVxwSqhaF1YGZJLP0rzeBNWHtAXj2ZwCJTKmfIFdZv386ReoQYNaVqShpUcBQqq8qPyMMMGepHMV5-6SGf3USxNqSR5OwKHoLAvLvttSmky4SfyFfB-zodcABBav1KxeJF0XMYVZrMBkXA6PnAigEfgdqpixsBojFXPEZqyuZjP83OJBVF6WOwZGW2f4lphWpLSVhIusrXD9crWGpz0cTMhG8LvkwJhpuhqjYGHEwbWhGQdywNZ2KIC4e-H1TwwreSPBuuOvU8LzeWIiA05vut_lXBBaUlmv2Rwxm5L9LTAzB-Xd2U_V1CFFLpeepKyCa4_O6tR5TmBzMi5KSQ8kKQ5yJY5MPXYpVDXomATB_1CKA7pw58xj9Pp97GoAAtX7hMHg4_ZOoqDiO56yreI3rDTKN_AJacEgwIX4O9yzgjUPf4QD9YUUZf8myu2xcMgAE19FiKSlzYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4a0d90a9.mp4?token=SArPQqRwHr7wAoSeVogczAu4HvdjBbaDwZIqyq202VZXRn9aIxW-L85N4Kkt2LhE9A_bcQn0UTqdAic01ap1U8y5j_RyJ2v6eYqstOLQcFzihqehmolSNSU5rQLiNSReN2mcKE_uHVGDNLTtWC88nxuPyfLSfywWmpPqrwrMw4RUuh9qqrGEYa9KIlWtYhEwCqeB4L4kGoCCvVBtJIjXwvrDEYmwqyodVxwSqhaF1YGZJLP0rzeBNWHtAXj2ZwCJTKmfIFdZv386ReoQYNaVqShpUcBQqq8qPyMMMGepHMV5-6SGf3USxNqSR5OwKHoLAvLvttSmky4SfyFfB-zodcABBav1KxeJF0XMYVZrMBkXA6PnAigEfgdqpixsBojFXPEZqyuZjP83OJBVF6WOwZGW2f4lphWpLSVhIusrXD9crWGpz0cTMhG8LvkwJhpuhqjYGHEwbWhGQdywNZ2KIC4e-H1TwwreSPBuuOvU8LzeWIiA05vut_lXBBaUlmv2Rwxm5L9LTAzB-Xd2U_V1CFFLpeepKyCa4_O6tR5TmBzMi5KSQ8kKQ5yJY5MPXYpVDXomATB_1CKA7pw58xj9Pp97GoAAtX7hMHg4_ZOoqDiO56yreI3rDTKN_AJacEgwIX4O9yzgjUPf4QD9YUUZf8myu2xcMgAE19FiKSlzYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار عجیب یک شهروند شیرازی با خودروی آتش‌نشانی
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/681768" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a37ebdf.mp4?token=ZE3xms4BVooU6a7rL8pmH7bZ8xuvbxlBS25kra2m_nfoBS790moOuW5xsZGK-kNIQmkuA7Vm2YJgQ4-tXyCwnhQI5lM9RbM9xlpykHM00Xj-CqJQRtE2BLkYcSZtfhAC3rd8CZv4-NrEBXdqVHlL_OCGMixx8wvxp24x1BsHpeSkLRlY69qIZ21lCgTmt9Iy0alKjZ5wc4FZ4erRMZ_cdEQ9WsSfhE_t7tdtfkHups_VaqmsLu2cpHVHChGnuFn_Zpf8ZEUxun4Qz2V_31nLJptt2-CPFlnAOcX5q-8sCPb7y1U__c1uwhUzeqv8i9Zf3CaKDX_J7PZ4V-SpmOdaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a37ebdf.mp4?token=ZE3xms4BVooU6a7rL8pmH7bZ8xuvbxlBS25kra2m_nfoBS790moOuW5xsZGK-kNIQmkuA7Vm2YJgQ4-tXyCwnhQI5lM9RbM9xlpykHM00Xj-CqJQRtE2BLkYcSZtfhAC3rd8CZv4-NrEBXdqVHlL_OCGMixx8wvxp24x1BsHpeSkLRlY69qIZ21lCgTmt9Iy0alKjZ5wc4FZ4erRMZ_cdEQ9WsSfhE_t7tdtfkHups_VaqmsLu2cpHVHChGnuFn_Zpf8ZEUxun4Qz2V_31nLJptt2-CPFlnAOcX5q-8sCPb7y1U__c1uwhUzeqv8i9Zf3CaKDX_J7PZ4V-SpmOdaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لطفا بذار ذهنت استفراغ کنه
🔹
با دیدن این تیتر تعجب نکنید و این ویدئو رو ببینید، شاید به شما کمک کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/681767" target="_blank">📅 21:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681766">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID7nFBtHr6uvQSM9P0OF7he5VoBcHGy8SM9Mup_60UmQoSGTJj6fnOeSTA7Do5-8HjYR8f4px4mPdMlnkFkIP4ylkOIyNm3g3oPuMaeWII1r9uE8kQRf6X8-dackdNJlS0OND5AOXzZj_Di89yROQpmtsYpoN6RBpUUQG925Fmbfm08QBCPlyKv7v7lNo-HuiafBGMAmDDL7qACR4uO48Xvw6sUaI1BLGaGrrIphyIKs9A5tp3SveQq42HY63MAO5DCoTZOBu6fQH0OakxuvzqOEJr5qzCdk30tIc7eIs8EFZfW4C8v4RgKCclcR7JkzFd6yZ9HdaSyHvLAyDJVhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این صفحه و پیام صادر شده از آن درباره قطر که منتسب به فرمانده نیروی هوافضای سپاه است جعلی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681766" target="_blank">📅 21:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681765">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=BiBVWD2c7KaPxgDEVGCH0CnFZkhckmbBRmKsoJBek1JcUZfxiqthc603xQ0Oe_z0_EqAqI8ZuM2JpqOl4hMm2kNRBGfpzSmO0ErsQTp5XSyudT3VCt9MUx5dGqkN9cgrwx1GVie2NeuQLcRE1i2rGCU7-A_FUn-_m2VSnyJ5aDVzisatIg1UqiwDXubPFidFppsVg63Ar2Xh1RMfqEribeoJJXoUo43vyAR6dwWYc3XxMQOcSq6ADxCcsTYBIKG1zCc2V1Er3mSKgUX3lg5kKwiSBoXnTu6_HnyoqJZbiUmI8Y8fP-9czz6RWS7eXH0sIJ-tdpETtCozAT8Ai7p5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=BiBVWD2c7KaPxgDEVGCH0CnFZkhckmbBRmKsoJBek1JcUZfxiqthc603xQ0Oe_z0_EqAqI8ZuM2JpqOl4hMm2kNRBGfpzSmO0ErsQTp5XSyudT3VCt9MUx5dGqkN9cgrwx1GVie2NeuQLcRE1i2rGCU7-A_FUn-_m2VSnyJ5aDVzisatIg1UqiwDXubPFidFppsVg63Ar2Xh1RMfqEribeoJJXoUo43vyAR6dwWYc3XxMQOcSq6ADxCcsTYBIKG1zCc2V1Er3mSKgUX3lg5kKwiSBoXnTu6_HnyoqJZbiUmI8Y8fP-9czz6RWS7eXH0sIJ-tdpETtCozAT8Ai7p5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: از دولت درخواست می‌کنیم اصلاح قانون بودجه را در قالب لایحه برای مجلس آماده کند؛ مجلس آماده است بودجه‌ای با محوریت معیشت مردم و برای حل مشکلات آنان تصویب کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681765" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681764">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120771984.mp4?token=ESt0m_URZ7KDKXGbpaoCBz1WJTsnhdo_y9gg-2c-d47ia6738_cGrCAL6AczXXuWRdoJyOfRiLMZ7jm2dYHI_XtKOKYFuRa3FJPFQ8TyBpDYYsBmvwk7CJP4FZPBbuNVtKgR57Ijrv_SK1dwPJQMoltOuP09a74Epv2JTAqg2Hb7TF3g5aSX1ITc6HTHA5N-79CKflHaRtRtO4XXAXPvPMHSckJZvyu5MbmDbiR7LsF8xl5z7A_JXyfm7WbkSvtAEdD_NEgC5qD4s9hIeBElfr-vmzt30sj6jkkWXGc2pWNjNTxUtuwdmCU5ilyl-v6e6sFJmO16jPqILQv0nqnpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120771984.mp4?token=ESt0m_URZ7KDKXGbpaoCBz1WJTsnhdo_y9gg-2c-d47ia6738_cGrCAL6AczXXuWRdoJyOfRiLMZ7jm2dYHI_XtKOKYFuRa3FJPFQ8TyBpDYYsBmvwk7CJP4FZPBbuNVtKgR57Ijrv_SK1dwPJQMoltOuP09a74Epv2JTAqg2Hb7TF3g5aSX1ITc6HTHA5N-79CKflHaRtRtO4XXAXPvPMHSckJZvyu5MbmDbiR7LsF8xl5z7A_JXyfm7WbkSvtAEdD_NEgC5qD4s9hIeBElfr-vmzt30sj6jkkWXGc2pWNjNTxUtuwdmCU5ilyl-v6e6sFJmO16jPqILQv0nqnpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: رژیم صهیونی درحال تلاش جدی برای تصرف مناطق و تاسیسات استراتژیک علی‌الطاهر است/ رزمندگان حزب‌الله لبنان با تلاش نظامیان صهیونیست برای پیشروی در ارتفاعات استراتژیک علی الطاهر مقابله و ده‌ها اسرائیلی را زخمی کردند./ ارتش رژیم صهیونیستی درپی ناکامی‌های خود بمب‌هایی را بر روی منطقه علی‌الطاهر انداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681764" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681763">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل به نقل از یک منبع امنیتی: ارتش برای احتمال تشدید تنش در لبنان در پی رویدادهای ارتفاعات علی الطاهر آماده می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681763" target="_blank">📅 21:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681762">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای بلومبرگ: انتقال مخفیانه نفت از تنگه هرمز توسط اعراب
ادعای بلومبرگ:
🔹
به گفته افرادی که از این محموله‌ها اطلاع دارند، انتقال نفت از طریق تنگه هرمز به‌صورت مخفیانه و بدون شناسایی، و سپس انتقال محموله‌ها به نفتکش‌های دیگر در خلیج عمان، با حداکثر ظرفیت ادامه دارد؛ این روند حتی با وجود حملات اخیر به کشتی‌ها متوقف نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681762" target="_blank">📅 21:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681761">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5b727823.mp4?token=EtIsahzErpiU5W1Fiv_7yni372p0aDqw07vo6lhMDjOvW9mcNsQ62-mhIO344e-_o1i4tCLrC1XhK7S5quv5kBrKOfE2KHxpxOdY_zxIg-xJOrRpNN4-eRNaUyAs6xnqQ_s_X-xxkFFA9pO4JEo_ZDRs4dRFXfSmnId4xL7YYbAWaMz172UhIfzdjh8NScB4MFXvWPp4VWeYBDX1GBiIGyAiEsNYMvQfoqMN0CJ_CPP2PHVj8U2zLFIGJvl0uU0QUJjfn9DjhX7JreREfYSzWRbpSotRANMBcfxsD46zUvhv1PpqxjBapqHMNjMhoaFinFfk72JY0fhqH6A0f1O2m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5b727823.mp4?token=EtIsahzErpiU5W1Fiv_7yni372p0aDqw07vo6lhMDjOvW9mcNsQ62-mhIO344e-_o1i4tCLrC1XhK7S5quv5kBrKOfE2KHxpxOdY_zxIg-xJOrRpNN4-eRNaUyAs6xnqQ_s_X-xxkFFA9pO4JEo_ZDRs4dRFXfSmnId4xL7YYbAWaMz172UhIfzdjh8NScB4MFXvWPp4VWeYBDX1GBiIGyAiEsNYMvQfoqMN0CJ_CPP2PHVj8U2zLFIGJvl0uU0QUJjfn9DjhX7JreREfYSzWRbpSotRANMBcfxsD46zUvhv1PpqxjBapqHMNjMhoaFinFfk72JY0fhqH6A0f1O2m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع معترضان به نسل کشی اسرائیل مقابل موزه‌ای در اسپانیا
🔹
در شهر بیلبائو در اسپانیا، مردم در اعتراض به نسل‌کشی رژیم اسرائیل علیه فلسطین،  مقابل موزه گوگنهایم روی زمین دراز کشیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681761" target="_blank">📅 21:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681760">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
جهش دوباره مسکن تهران؛ هر متر نوساز ۲۷۰ میلیون تومان شد
🔹
پس از حدود دو سال رکود سنگین، بازار مسکن تهران در نیمه دوم سال گذشته وارد فاز جهش شد.
🔹
متوسط قیمت آپارتمان‌های نوساز طی یک سال از حدود ۱۲۰ میلیون تومان به ۲۷۰ میلیون تومان در هر مترمربع رسیده است. متوسط قیمت واحدهای نوساز تهران به محدوده ۱۵۰۰ دلار در هر مترمربع نزدیک شده است.
🔹
این ارقام مربوط به واحدهای نوساز است و طبیعتاً از میانگین قیمت کل آپارتمان‌های تهران بالاتر محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/681760" target="_blank">📅 21:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681759">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVE8FYn0CR3PLvNCUvdc-9DCDBycCkB05MSbd7LyURoFgtUROQFC4CWS7m3k7TiDJxKv9OCOJTJKsxDjWzb_GKs2FQb8iU5_soPRwbIkvBNjnG2lgf-TCsFrZa3Eo2zd9mv_USRU_KK4oXEvcHLN62R5ZUBHga92WexsoNjOmrZKQIyl7lK4i7eCoHAE0MHhCkViBNDGIsiPeqD2MjnsxEoECbwJlTC3w7-RF-w7XGYQbNoQlrvI2EGJuGAzHN8OJ7EkMu_C9EGn9_qlNkkBQx-OiTbxd1Ef3QbstSmuRrEJzEXtV7l2ZCZYAVnRWnEH1y2nCV8KITUHnDhuY4maYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی امور خارجه ایران: واشنگتن کانادا را «ایالت پنجاه‌ویکم» خود می‌خواند
🔹
واشنگتن بر کالاهای کانادایی تعرفه وضع می‌کند، واشنگتن به کانادا توهین می‌کند و به‌دلیل دود ناشی از آتش‌سوزی‌های جنگلی، آن را به مجازات تهدید می‌کند؛ پاسخ اتاوا: متوجه شدم، قربان
🔹
در همین حال، اتاوا برای جلب رضایت واشنگتن، در جنگ غیرقانونی و انتخابیِ تحت رهبری آمریکا علیه ایران مشارکت می‌کند، پاداشش چیست؟
🔹
اینجا شب هاکی در کانادا نیست؛ اینجا تیم مزرعه‌ای واشنگتن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/681759" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681758">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بسم الله الرحمن الرحیم
یک مجموعه بزرگ فرهنگی و پذیرایی خوشنام درشهرمقدس مشهد و نزدیکی حرم مطهررضوی (محدوده چهارراه شهدا)
از افراد متدین، مومن، خوش برخورد، با ظاهری آراسته
در بازه سنی ۱۸ تا ۴۰ سال
با حقوق خوب و مبتنی بر شایستگی
(با غذا و مزایا )
به شرح زیر استخدام می نماید.
میزبان و خادم زائر در حوزه پذیرایی غذا و نوشیدنی
۴۰ نفر آقا و خانم
آشپز، کمک آشپز و پرسنل آشپزخانه ۲۰ نفر خانم و اقا
خدمات و نظافت  ۵ نفر خانم و اقا
صندوقدار حرفه ای ۴ نفر
از متقاضیان و واجدین شرایط دعوت می گردد حداکثر تا ساعت ۱۸ روز سه شنبه ۲۷ مرداد ماه ۱۴۰۵ رزومه عکس دار و مشخصات خود را به بله ، روبیکا یا  ایتای  شماره ی زیر ارسال نمایند.
📱
09120880710</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/681758" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681757">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197ac01bef.mp4?token=j8ckyse4xQWPTf1pzbfbV-p2b0-RYpIi0tEUp843_JQnljkFiZw50AgRFGEuRwUMNCFlIeYKI2RESfaRlwdg2863Mo03RXjg6b0qdUHjOJUMoTZPPYwzCU9FZ_2YDWLtPtwr7PO8DuFx2JhAjFLYaRzG-J9IoVDNstkXzmEzvJH4OeZjiK9AtLCeL1ZMnQtKbk9eOMIt7ZkMLS8-b6BCGWkf1crXHCGry2KM15JBKwbM7bsJA0QrFW51wP63IEvSoJ081rcvGg21ytSmdgQ9Q5_pxeKKrFm_XG_On3HHp5hCw8YMAwb-LdsgDwFWn-zZvttc4OvSA9Sw9YW4EtXEojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197ac01bef.mp4?token=j8ckyse4xQWPTf1pzbfbV-p2b0-RYpIi0tEUp843_JQnljkFiZw50AgRFGEuRwUMNCFlIeYKI2RESfaRlwdg2863Mo03RXjg6b0qdUHjOJUMoTZPPYwzCU9FZ_2YDWLtPtwr7PO8DuFx2JhAjFLYaRzG-J9IoVDNstkXzmEzvJH4OeZjiK9AtLCeL1ZMnQtKbk9eOMIt7ZkMLS8-b6BCGWkf1crXHCGry2KM15JBKwbM7bsJA0QrFW51wP63IEvSoJ081rcvGg21ytSmdgQ9Q5_pxeKKrFm_XG_On3HHp5hCw8YMAwb-LdsgDwFWn-zZvttc4OvSA9Sw9YW4EtXEojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دلیل کناره‌گیری سخنگوی کاخ‌سفید را اعلام کرد
🔹
ترامپ در گفت‌وگویی با یک خبرنگار گفت که وی دریافت که کارولین لویت فرزندانش را بیشتر از ترامپ دوست دارد و این موضوع او را بسیار نگران کرده بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/681757" target="_blank">📅 21:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
راز عروج دو دختر نوجوان در تجربه‌ای میان زمین و آسمان
🔹
00:06:50 وسعت نگاه روح هنگام خارج شدن از جسم
🔹
00:16:00 پخش نور شاخه‌ای از آسمان بر مقبره شهدا
🔹
00:20:50 حضور ۴ فرشته با بال‌های نورانی
🔹
00:25:30 رؤیت شخصی با شکاف بر فرق سر و انگشتر زیبا بر دست
🔹
00:35:15 تأکید به آموختن مسائل دینی و ایمان به عالم غیب، قبل از دوران بلوغ
🔹
00:52:30 رد شدن دست از بطری آب و عدم توانایی برداشتن آن
🔹
01:02:20 ترسیدن از نگاه سلولی بر هیبت پدر
🔹
قسمت سی‌ودوم (روح و ریحان)، فصل پنجم
🔹
#تجربه‌گر
: رضوانه عرب نظرگاه/ ریحانه رشیدی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/681756" target="_blank">📅 21:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681755">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfa90b88f.mp4?token=hjYSCnW7WL_xXWljKMAUsce-9qRvvEdI0tLIzFTxqOuAgS0LGgXs7dLjeHGMea5d4UeP3_qJMfEZk5Lx1AzkLxXaCAKF1FEEDznRvgNryIn2acn-sUtQJ_VOd7YbAIk-fnsihVHC6BxaOfdPE_LiWdOZoPB2SvMt12EIOUgFKq9EPB28RUHNs4Otx3LJc2GSNTb4ByTFzq21iHFl484BCK6VYvlOK3YxloN31AK6TnlWAffuSbCTVKDpcTM4TDiI_v_4XB8WzfLqPhcuI2G3ZG-d4Z7ZfDWbR5026MTsGCvyQr0TaT7EvssaC0SNBTlIknO8bJLMFIqSj81-FFRoUajUzN_Gzom8XTowrMwaAKAjeAyucMAnsh97E63LuozP4aYxJGdiAnPkc3kl0WzS8q3ePBaPmZ2CIvRLkswLbs9Ji-U3oPveMS_3-cSkLRd3Xqvvp3epOGJUToExPX93bcxntqF10mmG0SWEsysrRmYE40BnMagDDYc_4Oh-mWKUfvssMSlq-rEgGmLc8gAGo09SjlamYhU4f4gElF09euLW7U1mw6W_R1ytlYmgduqSw7crdz03UjCm9LVoNB7-xrfuWTpXsUbXRVgT_Klhs9yDxSF1x4OqAg0QnGYa5CMMgbSja2df-k31J8nZ9h1W27eBF3hccN9c43GmBJBIAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfa90b88f.mp4?token=hjYSCnW7WL_xXWljKMAUsce-9qRvvEdI0tLIzFTxqOuAgS0LGgXs7dLjeHGMea5d4UeP3_qJMfEZk5Lx1AzkLxXaCAKF1FEEDznRvgNryIn2acn-sUtQJ_VOd7YbAIk-fnsihVHC6BxaOfdPE_LiWdOZoPB2SvMt12EIOUgFKq9EPB28RUHNs4Otx3LJc2GSNTb4ByTFzq21iHFl484BCK6VYvlOK3YxloN31AK6TnlWAffuSbCTVKDpcTM4TDiI_v_4XB8WzfLqPhcuI2G3ZG-d4Z7ZfDWbR5026MTsGCvyQr0TaT7EvssaC0SNBTlIknO8bJLMFIqSj81-FFRoUajUzN_Gzom8XTowrMwaAKAjeAyucMAnsh97E63LuozP4aYxJGdiAnPkc3kl0WzS8q3ePBaPmZ2CIvRLkswLbs9Ji-U3oPveMS_3-cSkLRd3Xqvvp3epOGJUToExPX93bcxntqF10mmG0SWEsysrRmYE40BnMagDDYc_4Oh-mWKUfvssMSlq-rEgGmLc8gAGo09SjlamYhU4f4gElF09euLW7U1mw6W_R1ytlYmgduqSw7crdz03UjCm9LVoNB7-xrfuWTpXsUbXRVgT_Klhs9yDxSF1x4OqAg0QnGYa5CMMgbSja2df-k31J8nZ9h1W27eBF3hccN9c43GmBJBIAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات خاص و پر از احساس بوسیدن دست مادرها در استودیو برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/681755" target="_blank">📅 20:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d3798d25.mp4?token=t4CR8yyDjGHyp9dOZBl26k8vnSId0Oms6dq-933mWb2We8MIgJpr50X1zJ7SQNGNUlqj32ThKL7dCam91kQdR2iP0kVZamqYOaOvB7VtUobLZHCy6EsKrRG5vWsVwtIBoW2GMOa2Ym3D4zZGcBeSiORV7HV-GeOqVhYVMDRJ6z__mExGL8COl7UjfMiHrStYrPW9R6Qmnjos974Jb8qdzh2E04xAYXxxsMHahIlTk23Oud4YsLqDd-c681IiEYdPD7BjjwObSkhWki2p1wVmao5ptyMsavSis8ZM6Lb4SIKeppPkIxCGMT_zDJWrsIVknt_dMTukG7uIOUFrS7Oitg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d3798d25.mp4?token=t4CR8yyDjGHyp9dOZBl26k8vnSId0Oms6dq-933mWb2We8MIgJpr50X1zJ7SQNGNUlqj32ThKL7dCam91kQdR2iP0kVZamqYOaOvB7VtUobLZHCy6EsKrRG5vWsVwtIBoW2GMOa2Ym3D4zZGcBeSiORV7HV-GeOqVhYVMDRJ6z__mExGL8COl7UjfMiHrStYrPW9R6Qmnjos974Jb8qdzh2E04xAYXxxsMHahIlTk23Oud4YsLqDd-c681IiEYdPD7BjjwObSkhWki2p1wVmao5ptyMsavSis8ZM6Lb4SIKeppPkIxCGMT_zDJWrsIVknt_dMTukG7uIOUFrS7Oitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نوستالژیک چند نام ماندگار؛ وقتی خسرو شکیبایی، بهروز وثوقی هم‌نشین شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/681753" target="_blank">📅 20:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681751">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d6a33f311.mp4?token=EDkHd9SVML2byHJCwU9iquwB1H6AxeOQYxFwQklD8rnkZRUHANU_KToVjaCb7NPyVgOVFqrUHE6yG6GSZjI-BheZkyxIhwd02FrJSFf-tDGSyjtI6UYa2Xmh2V2Exd-3ebfzmutDOFIldRIvYvPoaemJaJUknb6p3btm5l1XdW1VuG8y_5izxlCzaX0RsnMRk-TZD-HxlitVnzPQzJCcF6mYv28fKCPz1bZb41OUSfBNsiTccteneW8JDXhRlgOjxI8P3Px1LA-SJczOu4N9pttgidszlwYI4cBlco51yt91PoM0Kjuto_bk0xC6oXIPa6gOSvuzIxXZnfEQAF9dmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d6a33f311.mp4?token=EDkHd9SVML2byHJCwU9iquwB1H6AxeOQYxFwQklD8rnkZRUHANU_KToVjaCb7NPyVgOVFqrUHE6yG6GSZjI-BheZkyxIhwd02FrJSFf-tDGSyjtI6UYa2Xmh2V2Exd-3ebfzmutDOFIldRIvYvPoaemJaJUknb6p3btm5l1XdW1VuG8y_5izxlCzaX0RsnMRk-TZD-HxlitVnzPQzJCcF6mYv28fKCPz1bZb41OUSfBNsiTccteneW8JDXhRlgOjxI8P3Px1LA-SJczOu4N9pttgidszlwYI4cBlco51yt91PoM0Kjuto_bk0xC6oXIPa6gOSvuzIxXZnfEQAF9dmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681751" target="_blank">📅 20:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681750">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
لس‌آنجلس‌تایمز: رویکرد خفه کردن اقتصاد ایران توسط وزیر خزانه‌داری آمریکا رهبری می‌شود
ادعای لس‌آنجلس‌تایمز:
🔹
با نزدیک شدن به شش ماه جنگ با ایران پس از پیش‌بینی یک کمپین شش هفته‌ای ترامپ، گزینه‌های کمی برای پایان دادن به این درگیری دارد.
🔹
رویکرد فعلی، یعنی خفه کردن اقتصادی ایران، توسط اسکات بسنت، وزیر خزانه‌داری، رهبری می‌شود که در بررسی‌های پیش از جنگ ترامپ نقشی نداشت. گزینه‌ها عبارتند از تشدید نظامی، پذیرش پیروزی ایران از طریق یک مذاکره ساختگی و ادامه فشار اقتصادی./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/681750" target="_blank">📅 20:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681749">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggniwys4WWKrz3RsRzaQfSLRkF0sSJoww0q0LBIuaEno2v_EK40G1vSffAsVnMpOfq44tf-bXkqFfSIkjkgZiqn8rcgy2S3Yb07xt8csRRAU3CnyPizgBIKdMfnFtfe3vOHF0MWxxQzbHljYT6J5Kk7n5edN4c9NQw1YkzLo4XKSiLtug-tFXPR4BJGQXaXjNTH8YwMZRPkfgc3GGn07OqmrOZGa0HBcyIr6XUMpMuTrUUbysjxL9nBpzHyO42jpfy57XGc9tQVTQhHKsYZG8uX1tp84NF3UaUzl8hqOuEJcpMVpqcxvRzVTcSLsgB0M3UZvvRqe_bKNubBWRzh8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«به وقت ایران» همچنان پربیننده است/ محصول سازمان اوج در صدر مخاطبان تلویزیون
🔹
بر اساس آمار مرکز متا، «به وقت ایران» با ۲۰.۵ درصد مخاطب در تیرماه در صدر پنج برنامه پرمخاطب تلویزیون قرار گرفته است. این برنامه در آمار مرکز تحقیقات صداوسیما نیز ۲۴.۵ درصد مخاطب داشته و در تلوبیون، در روز ۳۰ تیرماه، به ۱۳ میلیون بازدید رسیده است.
🔹
«حسینیه معلی» با ۱۹ درصد، «جام ۲۶» با ۱۸ درصد و «پدر امت» و «سمت خدا» هرکدام با ۱۷ درصد در رتبه‌های بعدی قرار گرفته‌اند.
🔹
در کنار این آمار، یکی از نکات قابل توجه درباره موفقیت «به وقت ایران»، این است که این برنامه از تولیدات خارج از سازمان صداوسیما است و به همت سازمان هنری رسانه‌ای اوج تولید شده است./ فرهیختگان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/681749" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEY5Jia4I-0bZZUWy-F5e2b6Tg4Zh1aiUDTwDB6KFxoL_8pienc33_5s0kYEBHIplHdzFry1ZyLRZFi784BKbbTUZG4CKPJmPHxXcpBbFN_QQcEJsg4bkFxo-UvltSLjsHeItb1wQXGnRiOmJbsqEbdTTlpVFcGefuPMRFGldtZ2ZHtrQJyDXcUnpwhBAbeXXaeijEEoGtu-Wf_d9zgnh3_Xq5W_huWZEQjpYcFD_dkuKjGtcynNQObFDlEpmI7JZe6IgUrgNwEecD4haYh_T0UKOWD0Oej64RSy_s4Ee72dnbjpuk-KY7FBl1ltGZbUDPRiJc5FlYwTndievWlQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4Fman0y--WdA1kuTpsv0AUb3MxYNNYYkiNInABvEUPaTDZEvBZCIVTmICPnjZIn8TbCkQ4b-bJYkqlZtnmJr-4wM5QA7IAmeSJTK1HgaYJO8dMciju8jIWDz1x3A4uIC_ViMA1ql_bfGumjx0xGQmiySgrL_KdDp41hfK2zuCMg5n0qbkCCOsNxgbI5uAmqngBCEs2NLRG3wfwB8MAGaP3-mNKElR_V7_exp9CPz-169JHWz8HuKTdQGAB_Ogws83Rp9_fY2jLf4NPY1yh2V4zkhm2Y2n-WZIxAP4fi0sg5M9NBM-4VXLykfAM94MGm3fz_yh5OE2MUgwvcEpYCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRwwtFyx9SeAPlH58nHklCO6qR4XB7XlDyN5hgPL3pBnkV2aifiHOhcImgaCZ5ZV-3AZuC-Kh_mevLjaDgTx97Ug5E2pC79u6tjPGxj6fUUTRECZSAS4rFSHejBUjntEVmn55lIQZ54v8C7mSBZmOAnfnjIP_oxnSBH6SHflE51iIDw-pyvZybKAH5J5oDlbU_02w18263p1wY-mNrzT5eGtvmHbQpkNZUlna8EhoqVaPiUA--dibN_VX6tvOs8mcy2EVZz8fui6NgbDRyAhbqoXhFxl29Ex01HVAyKgHpqgwKPCbhdjtYoq6gNDsPuQd_e2u0UYp6GdN3e92Ac8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsBj_Rga1uNtTgttyG7tHJRdRX6RqKjhLMmUdVobydAoCiegag4vorZTX0OJXgTLMgxHjWQ9GBFvYt3tyWZzyRFGNHMcSQKPpdXjBQGemA_5Vc3CIU_c-wT6LVY4znQXg-fAYmcEHK-3pRahKXXwh6srHJwTN1k-_nS2s6pHcwv-qA3YToNJEsUx8l3tSuLksPf0X1kYYhM4yqqQdIEtFvhmKurDChU0lisFkmtAq4XJI8a153zzi9UhtfjWtkcRXQTaJ7D1kuMmzRQQiuXebjJqiIhG-VEjkAKH5mNQLs9dqkk-3bCQHiQ4tlBhnktD5hnDqxQ5wzqmQORR0HeuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAX5ePkmEZSe3KLAH4d7Ub7Pt7JVOInCP2lNi8MYyirty7jN9jZ0hzOfiakAuc1NpjWSr5XE6XfkU5yfom_A3-_DSJQbRTTZ96Lxi0t1gFeAMTdPLIyfBerrX2P2N1h_slHBaUwpl9mHY4wjmILgBbXu6dtI5_HpI87riGxuNVoSFtVySjyTarRLiFTEOcZGxMYD6hutI4s6Idg4IgMK9qoxyz-U2UJKGPbWKmFE7-iOr8XjkSEVtFGPW4OSv-1i2n1Uw9vN5-oi0khKmQkR9G0Tq5JqyNm5kdOjRfhJywIrDhfZkEaXFzQGHz3IZBfaIn8FQ0slOugip_njyr4eYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgogEnUd7e_pWud_izbpGQ02zGI67v0tZNcErpbRZd705YLI_pu-sQPk1yNyRMmVbvDACLWwZwbyv4uspgB9MtFrQkbyBchk3U3GYkZStKjOkW2DsVHbY9VOCX_KySCzAdP0eGbryU30UzQ-OLd76ScSjAxZnuIOmuhJGC_AlmyCT5o6YlfmeFkzIZsNGX0iRXm0sLZS5VBTjahs-NLccE3JGmopZ6N_Nr5c3KYPzJ8kFzJthS9joPJJTWtN_Vw7YkHLLO71C3SA1mdCRTl5U4UnJLpouZXU7DdmrdbEZc8wIopu1yljtMWyxAVs6zRWLYZIETYYsBbKzW6TxCKqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNU4BFL8tY24F852qp7ZHauGeSPc-Eqb5Pple-jgTHZgFZfSINJoAOguDa3dsI6XXDpl-MJYywciIRoHuCstJeyIxo8ezSsZ2rQ84viYxbkPuiwWO2JRaKGujX_NA9vXVg01nTJWtZfHHPcplLMfnAqhGBFozJz53Ubb5bIoqfOgNF6lKHy-uzP-uHWp436UWmdigOtyUXa1_mlFBwW8e8x9Caf87naJ50kUfVA6BLX15iPx5IChJN4qb2fXFJkFqkvG1sxIhccIvN_aruOfL9kCGyMn-cmcT2aDa8yCANx4TXyL7EHkwlxsj83_4F4YryE2cuppw9ks6v8bIIUcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از جلسه هیات دولت که بعدازظهر امروز یکشنبه به ریاست مسعود پزشکیان و با حضور اعضای هیات دولت در نهاد ریاست جمهوری برگزار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681742" target="_blank">📅 20:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR1RVyzGc9EMiSR0l2T35Eagl1QiOgrKyqQ4SsG4z7uGnfysZ1XnfcBEsaV48YvWO7oS0HxiUWAWUms-gVZdLYxGpZQFkhg2k5Vz5zUGL75965s1HwSgC0399GsSgVVaz0Y3ETnKzlYAh9NStoMMPPfrWY7seggDN4Fn8HfLxEYr-vKdaU1S3jJtafGKAYN5iSSw9mMrEjS8Tlnj11WkOQoXWTzjAytwGibVkv9TW2UVfomViqiKn1KWx2bO-3Giv1eNkc8KnrquyvYSmJaPEooq9nNPdjGCcCJb3BGX7ZCn4eqhXggWMBTj22KWAwdNb_IS7D48rFgcFpVONkkR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfFWjSH9SJbWAoAP-aqSLYVADtSO1GwfUL42mFGlnF27HqXoP-GLRsg4jMQRHX153pe6TprEsZFnynnF8Vtf0ollonVxfUdCY_YR4TXOn0MljikcnCilKGwpNqvELT6OKs0MvF0yJ--abYPGauTO0BmT87EiuMtXI0HQkEknmU_LcGNWdhnjI9DW012aD_0LrGlZ6KREzIhs0Qxo2CjkpDIoeVwf9HvZHAsDchrg3Gu7lKWD0fyyjwOwTVQ3agWfB-cFSH9ctqT10AEyIIG_1BfXpEsiSLSuvl0-ugeeePd9FEZEzFjOGC8bpC2kI1nB_O2FUutz8m78nU2XKXLXFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کشورهایی که بیشترین فرصت‌های فریلنسری را ایجاد می‌کنند
🔸
آمریکا با اختصاص ۳۶.۸ درصد از سهم بازار، بزرگ‌ترین ایجادکننده فرصت‌های شغلی برای فریلنسرهاست و پس از آن بریتانیا، کانادا، استرالیا و آلمان قرار دارند.
🔸
اکثریت قاطع فریلنسرهای آنلاین در سراسر جهان را جوانان زیر ۳۰ سال تشکیل می‌دهند و «توسعه نرم‌افزار و فناوری» و «خدمات حرفه‌ای» اصلی‌ترین حوزه‌های فعالیت فریلنسرها جهان هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681740" target="_blank">📅 20:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU5bKugYiUHpl3muy4wSVhAtDPxBKGdjZvRY0EE6Oj5pHfHiUo4XjyUzyJpU8aJBYWlpJ01JGyW_52AO6rHE1yRxO4QPH6fkmtzg1adKDqhDdL_7KdEOKth9kBo2-MjyMs3aI7v5u9M9oFLwHVCiGJyMpUx7g8HyqGIOj2dS_da08LjgSApe0m4xyzVLB_R_xFuqnaEgA7pff0hMtg1P3yL9U31Uch1gfMfz59WjdNuOvl8qNGe0FGoM2ToRtZzG5m53zWr9c-4tz0_bQX5ZDKXWDdWXMosftxKaAmRxeZOw_c9kgJv5FpiJag8141Wb6_puUG-IF9Up3oJNBeIcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذات شور، ترش یا بیش از حد تند شده؟ هنوز برای نجات طعمش دیر نیست؛ با چند ترفند ساده، تعادل را به غذا برگردون
👌
🍲
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/681739" target="_blank">📅 20:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkGyb8Jk-qogAyYOOC3xn6xxGYoFCx4UheRwnZ3vPGrsqUMF39kilTkTbZi01UEQ8aOBjf3LnOFshayn6qQKraHQKZgVcjyzxePlE0H6YP91Hw3mVXRs0ChgyiKCnsSPfdIbXg4MRqsuorV_3c8wRQfqpllwX-0y6_ocr4eqeEb8je7GF6R837aW3QRvM4Otl0JIp4caG8iguvar1Y2cKqcr1Youj2y_Bfp3eIaHZjHwGzv1cMjSxgXP557O11Rxr40d8pMKr68jKaReGdlvlWIUhK7DH1a6yQf3bbI1o3Wa4qf6Sq9GxWUEn3laKfccMElLxBqUSahSlWVqpkR4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو شکست بخورد؛ پیروزی را به آن‌ها ندهید.»/ خبرفوری
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681738" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmfdOU60K7mpHl9KKbFvFdtL-fXYowJjoUuLPVTy2Uc8LkBM4Lz7XuDeaXp4raV4OR-5QE__ZRebZnxkknA4r7aPpIvYeW-A--iwf3QOpdWHBunuJDfZNWuIF1aK0K1hiH_3h70Wrg7DKJXjTWN1IYv3Of_kfPgav1fXjhLIVOrq0a2tJjhmJh_JWw-2x7Pjo-47c4lgMr4jlI29e2nVXEAfELEY2F32kVrDWm-ExOKOeXMXb6nCTj2tI4g-BxxxkVbQA7kL3YnKwtRBfXBeUahIx8xYRvr-i7m2v2RU6Ncwg7yWRF3RmUhJ3bpQPxA5lX6jXmB_eHIIEIZUECf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای از آثار حملات یمن به تاسیسات نفتی جازان عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/681735" target="_blank">📅 20:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پزشکیان: کسانی که در داخل کشور ما اختلاف ایجاد می‌کنند باید بدانند که این کار فقط به نفع آمریکا و اسرائیل است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681734" target="_blank">📅 20:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aShMGDEj0sMHzU3TplYjCGQfXhzjnumfpe0YPFVz4dEUiAuJxz6DAgnX6CDnsbtES8J1FnXImPgGO5QnrO7g8I7HVXfEhMHUH9XtVBy6t8B9wKkQNdJbFoeQa24-8YGehstPF2-RLdKgzTVzQOwliskERRaCO9NONusAUVsqCCE3VnLW0WYtQwOaxgh6zaJV-mICWOAjIhpltktbWc4l_dldGJL5X71AeO59Li8VxJJIu3SZONjkgdn-5cao3qxHTuqz7JYJna8BhrlaJ4K5QO9202yfJqB6OWbl9Ux-k1NDhUbZYvlsfLc-mrV2QBYeH1WxI1QsEl5qK7ZU0kB7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم ملی
🔹
مسئله بنزین دیگر با تصمیم‌های مقطعی و ملاحظات کوتاه‌مدت حل نمی‌شود و به یک اجماع و تصمیم ملی نیاز دارد. هر تصمیمی که گرفته می‌شود، نباید بار آن ناعادلانه بر دوش مردم باشد. اصلاح قیمت، اگر ضرورت دارد، باید همزمان با اصلاحات اساسی در نظام مصرف و تولید سوخت انجام شود. خودروسازی ناکارآمد، خودروهای پرمصرف، ناوگان فرسوده و سیاست‌های نادرست، سهم بزرگی در افزایش مصرف دارند و باید اصلاح شوند. همچنین لازم است توزیع یارانه سوخت شفاف‌تر و عادلانه‌تر شود. مردم با یک تصمیم سخت همراه می‌شوند، اگر ببینند همه در هزینه و مسئولیت اصلاح شریک‌اند. بنزین نیازمند تصمیمی ملی است، تصمیمی همراه با انصاف، شفافیت و اصلاح واقعی.
🔹
هشتصدوسی‌‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681733" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پزشکیان: کسانی که در داخل کشور ما اختلاف ایجاد می‌کنند باید بدانند که این کار فقط به نفع آمریکا و اسرائیل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/681726" target="_blank">📅 19:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حمله روسیه به تاسیسات تولید شهپاد اوکراین
خبرگزاری تاس:
🔹
وزارت دفاع روسیه اعلام کرد که پهپادهای روسی به تأسیسات تولید و انبار قطعات مربوط به شهپاد‌هایی حمله کرده‌اند که اوکراین از آنها برای حمله به شهرهای ساحلی روسیه، کشتی‌ها و زیرساخت‌های دریای سیاه استفاده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681725" target="_blank">📅 19:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tO1G7LA46oLlBGR-l47h8vNB4sVXZnPGEryFwX8de8FaPRzbEiH8i55wRoQIwP4bjErg7LV8n7qC7B5265onjmADcX7p09vjmJqUdr8YdQJHY3lyOvgURKXMfB3yqG5KSsmmdYv5KwLxp8EuJNkCAxr2462qDu785mA56gJdfR3-P51DkBipyyzNAqzVIWDaTOculcBIEUts077E411pQdahPbp-FpxUkB8q0KL7-p-zk2RHE-SwSlxwU4LUoCWvBCAJfNo2NZF3wqsyiP_SGLuF2CbLNcESU_gnKxvQk6sKmX3l7gw1a4OH1dbaJHcD5LDvgk2D01teT5KoAHUJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصوّبات مجلس براساس نیازهای مردم و معطوف به امیدآفرینی و آینده‌سازی کشور باشد
🔹
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681724" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920a41a2ca.mp4?token=jGhRtFubjZjaRZ1Jb80ibmJZq9LxV13YXI12mZmI8SXYeLLNJFy_-vCnnI0W0KPxTSOcdoeVqUbg3QGGG3LAmeA4AWkcEykzIa9xKE4s-NoB5mkV7YnQt_QxICIn2oPkKwzEzLTh2ba1ti9_jHDTbJSfGzkh7QNYPQbZ-M9Txf1DtB2ihhQJWr2P6OGl3JkzFH39gdl4s9ehipD--6CTCtzDdGh7Bhg7jyN7h_iw3sz3LtcNZVcJEevkh0tD2tE7IrUVuTj37TwEI8Ir1TjlZxxmR6valngYA9TkxEYvXCaoS_EZrBT-EqHWdYzAQUJJxFoGUwmnX-LkL8Gj2t8kUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920a41a2ca.mp4?token=jGhRtFubjZjaRZ1Jb80ibmJZq9LxV13YXI12mZmI8SXYeLLNJFy_-vCnnI0W0KPxTSOcdoeVqUbg3QGGG3LAmeA4AWkcEykzIa9xKE4s-NoB5mkV7YnQt_QxICIn2oPkKwzEzLTh2ba1ti9_jHDTbJSfGzkh7QNYPQbZ-M9Txf1DtB2ihhQJWr2P6OGl3JkzFH39gdl4s9ehipD--6CTCtzDdGh7Bhg7jyN7h_iw3sz3LtcNZVcJEevkh0tD2tE7IrUVuTj37TwEI8Ir1TjlZxxmR6valngYA9TkxEYvXCaoS_EZrBT-EqHWdYzAQUJJxFoGUwmnX-LkL8Gj2t8kUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
در پی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/681723" target="_blank">📅 19:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه را دریافت نمی‌کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/681722" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکود شدید بازار لوازم خانگی؛ مردم به جای خریدن تعمیر می‌‌کنند!
اکبر پازوکی، رئیس اتحادیه فروشندگان لوازم خانگی در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت کالا، کاهش قدرت خرید مردم و شرایط اقتصادی باعث شده بازار لوازم خانگی با رکود شدیدی مواجه شود و مردم به جای خرید کالای جدید، بیشتر به سمت تعمیر وسایل خود بروند.
🔹
فروش مستقیم کالا توسط تولیدکنندگان و کارخانه‌ها در فضای مجازی و همچنین گسترش فروش اقساطی توسط فروشگاه‌های بزرگ، سهم کسبه را در بازار کاهش داده و فعالیت واحدهای صنفی را دشوار کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/681721" target="_blank">📅 19:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ دلبر سه‌رنگ من
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/681720" target="_blank">📅 19:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
واشنگتن‌پست: کشورهای حوزه خلیج‌فارس در پی اخراج پایگاه‌های نظامی آمریکا هستند
روزنامه واشنگتن‌پست:
🔹
کشورهای حاشیه خلیج‌فارس به دلیل بی‌اعتمادی به راهبرد جنگی دونالد ترامپ در قبال ایران، در حال بررسی درخواست برای تخلیه پایگاه‌های نظامی آمریکا از خاک خود هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681719" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رئیس سازمان غذا و دارو: در سال جاری دو سوم داروها در دو مرحله گران شدند
🔹
دارویی که با کشتی به صورت کانتینری ۳ هزار دلار حمل می‌شده در شرایط فعلی با ۳۰ هزار دلار به صورت هوایی وارد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/681718" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ml31d9E7wSy0jR4x3tnl-HtTIpcg1nSN4GedpTr7ZJYr9xo1e9gt4ZCBFbPiHYPvNygCoob1zJUHyYO-fL7j9h9T9LSwrQUMVaGGCiU0IQbIzmcixLf0iPRPF5gLqi2q_tfuhF2C5m39kJDXkM-91e_V97VO-EZFdjg8sCcq7MnEnIo-pbCyc3lUaWXdfxnY2sZfemBjCk2TbBO4JZj7lgJqUNLYN3MZ3l-NO-NTeo9odZaFOlz8rCDaL1WTHkqbCLETvSSJouufLBuQA3hOLD0QOhZk4XgufD0P0wOWqIkWQBzeYCFUEyRC8AQwtabeneSx9THGNDuOhr2gIeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه، کسب‌وکاری را در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به همراه عکس کسب‌وکار برای ما ارسال کنید.
🔸
روایت شما می‌تواند الهام‌بخش کسانی باشد که می‌خواهند از صفر شروع کنند؛ بهترین ایده‌ها و محصولات نیز فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه آن را خواهند داشت.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/681717" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi2yoe8SCxwFKh7sE08GSoOicvwB4NHVLQTfguHK-VqlTpXSTAwi2Dhu9wqdmnlY7FcMqQH-Z0V20MKfTtQVpyG66nYwP8aWTsozpR-LO2jGnulSz0e1Xk8yHRNTBYaf6N-YvHL6hiGQ-PqzAp87FgHEc8YUAgD8nmcK34-ABjHPF8OtaAQnryZraKICTO6whBB8TDNu91DbhR8FoTtPNM8uUQyJrPXGgGnFftopJV_LKvqw8rwBsOYdfLTtA1-LYw6o9h5Dydr4H8v74bFyS8AnJnEMogkaVqPTuGJdMmhEIAofw-msk5khIABtUw7SEUowTZeUXsAz3mkIi2LyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که نامش با نوگرایی، طبیعت و دگرگونی شعر فارسی درآمیخته است؛ نیما یوشیج
🔹
نیما یوشیج، از برجسته‌ترین شاعران معاصر ایران، تنها یک شاعر نبود؛ او آغازگر جریانی تازه در ادبیات فارسی شد و با شکستن قالب‌های سنتی، راهی نو برای بیان احساس، اندیشه و تجربه‌های…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/681715" target="_blank">📅 19:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
دریا همینطور که بخشنده است بی رحم هم هست
🔹
این دو جوان هرمزگانی ۵ روز در دریا سرگردان بودند و بنزین تمام کردند که صیادان بحرینی آنها را پیدا می‌کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681714" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فاکس نیوز: تفاهم‌نامه ۶٠ روزه بین آمریکا و ایران فردا منقضی می‌شود.
🔹
تاکنون درخواست‌های بیش از ۶ میلیون نفر برای مطالبه خسارات مادی و معنوی جنگ ثبت شده است.
🔹
جنگنده‌های اف-۱۸ اسپانیا یک پهپاد مشکوک را در حریم هوایی رومانی سرنگون کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681713" target="_blank">📅 18:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN7FKgRj767mJUVm8ssPNWuy5gyUB3oOcqsLO-htAtpRe9SQZDt5muWiDafjNaX0-w__ZJHm-3Ng2gToPO3P8t5uSdgnJrqsjG3wan5tNh4oRXe2MlHCVIo5a8zXOWSPdCTvu1W5jpxz7ArvUWkwTIlpzhKQCRui6XTJJDE2bSKX_JS93ljoB_ImG1D41OyniyhuyhpQWbCfFnrQVEb86nqZCB6MlKTlPNvb4GHSrI20czqPhr6ACfKz8igXHsxzc26YlL3iEwlm1V5GTIiLysZfriGK622SCdmPX7ZeTaid_qqJYcLWkpLbnmF3nH03irYT3jR9eiyHkVLJIH4sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو ممکن است در پایان فصل از فوتبال خداحافظی کند
رونالدو در مصاحبه‌ای با مجله ووگ:
🔹
احتمالاً این آخرین سال من در فوتبال خواهد بود؛ بعد از آن، زمان زیادی برای استراحت، سفر، تماشا و بازی کردن پدل خواهم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681712" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0c01f9ac.mp4?token=krzeURJASihaxrItFhxxBzeQx_dzb3tpvkIfSZQYlCtKLkJCzVk2e3TLMkepe3bzFpZrZ4AUGHX3UNUGG4b1sgPBMMcNreheES67lQMzEhRTXvD1-fNBCQZsRkLwfWe_oHuKo8XiBng8q-si94CAJU6wVWP8WyBxduIlltdsPjqqWx_XAwD2EIQ-lx_HD2wDiCcpgD74szK8PUqnr-wmLEy0DUDd6fdrRbGQK4s2NZE_t_Fy1KBz2W52LWQjx9L0ALZ3xHOuzjZSAti6yZudEJpDHgWq07zWMaPodp99SGvDFMYbpNV3dFrI9g9SOiLHPb3MTWzNXfw6Aq5u_4wbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0c01f9ac.mp4?token=krzeURJASihaxrItFhxxBzeQx_dzb3tpvkIfSZQYlCtKLkJCzVk2e3TLMkepe3bzFpZrZ4AUGHX3UNUGG4b1sgPBMMcNreheES67lQMzEhRTXvD1-fNBCQZsRkLwfWe_oHuKo8XiBng8q-si94CAJU6wVWP8WyBxduIlltdsPjqqWx_XAwD2EIQ-lx_HD2wDiCcpgD74szK8PUqnr-wmLEy0DUDd6fdrRbGQK4s2NZE_t_Fy1KBz2W52LWQjx9L0ALZ3xHOuzjZSAti6yZudEJpDHgWq07zWMaPodp99SGvDFMYbpNV3dFrI9g9SOiLHPb3MTWzNXfw6Aq5u_4wbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی وسیله‌ای برای باز کردن درب کنسرو نداریم چیکار کنیم!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681711" target="_blank">📅 18:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/681710" target="_blank">📅 18:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
هاآرتص: هزینه جنگ غزه برای اسرائیل به ۱۴۲ میلیارد دلار رسید
هاآرتص:
🔹
جنگ غزه که از ۷ اکتبر ۲۰۲۳ آغاز شده، به طولانی‌ترین و پرهزینه‌ترین جنگ تاریخ اسرائیل تبدیل شده و هزینه آن به حدود ۴۲۰ میلیارد شِکِل معادل ۱۴۲ میلیارد دلار رسیده است؛ همچنین بدهی ملی اسرائیل حدود ۴۰۰ میلیارد شِکِل (۱۳۵ میلیارد دلار) افزایش یافته است.
🔹
رژیم صهیونسیتی در ابتدا انتظار داشت جنگ حدود سه ماه طول بکشد، اما ذخایر مهمات برای جنگی کوتاه‌تر آماده شده بود و مصرف برخی مهمات به دو برابر پیش‌بینی اولیه رسید.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681709" target="_blank">📅 18:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5XyGhl3kRPHO7WJhxifCLWrauYpe8H1E1aMw26F37eUoLfAoIMzNWW2dgmuoY7hlHNblpD-bTmNzoAP1LQzTmem2nl9q5BslCTYTVVOeryEgQmrKuVU3g3_6BS6vvag_rvmz8FyZu5KqStIf0pgD2y86eUMx1XvJbUrgHxc-pC5KDiPXW5t5901U2uNskJcbKh2mv72GF-GSFnH5zlOCdSvs3AfOwVFJxy8xfLlesBT5sKezXXx3vboQ7tnBV7TMN57DcjVefAu9NZXl2RGnd2no5UPt4qMqgZNoKPDdvh8urYSmfrz8DCzASn2-EvtacrT-yK_C5WYhXumeIv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارگیری روزانه گازوئیل از خاورمیانه و روسیه نصف شد
🔹
از حدود ۳.۱ میلیون بشکه در ابتدای سال به ۱.۵۵ میلیون بشکه در ۱۲ اوت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681708" target="_blank">📅 18:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خاتمی:یادداشت تفاهم فرصتی فوق‌العاده برای کشور است؛ امیدوارم این بار فرصت فراهم آمده از دست نرود.
🔹
سخنگوی ستاد انتخابات: شعام تصمیم گیرندهٔ نهایی دربارهٔ زمان برگزاری انتخابات شوراها است.
🔹
پاپ لئو خواستار پایان خشونت علیه فلسطینیان در کرانه باختری شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/681707" target="_blank">📅 18:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026aec7222.mp4?token=ZeVhdZ8C0uSwLiAllvnikd21GFViupSNfVyRv3QE_IYPRSDpWqEIrJZ8_jYIH_HQhTc4M74MHmEH1DJiwVbHNw6DtSRCWks31VddVZaguld5y6ce4wI94BhWYxVRB2etJZ7pV72wlbfMMUUJRjEwfqqsTSEdjxgSYIprSmOTz6aJTQEqNQ2aZiv0U_W5q6A2CZ6h0IFoVO1ljsH-PKR_2hMyAfEvfwAlG0qslQeHamNCajspXElCy-TYy7uaiFaWzvoIlTocfAClFTYqaScYKDENWyl4kPy3Xxky0wZ3NjQkzQ8n8pGBqFh37KmbvWBqNil9ApmtM5r6RQsO9d578Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026aec7222.mp4?token=ZeVhdZ8C0uSwLiAllvnikd21GFViupSNfVyRv3QE_IYPRSDpWqEIrJZ8_jYIH_HQhTc4M74MHmEH1DJiwVbHNw6DtSRCWks31VddVZaguld5y6ce4wI94BhWYxVRB2etJZ7pV72wlbfMMUUJRjEwfqqsTSEdjxgSYIprSmOTz6aJTQEqNQ2aZiv0U_W5q6A2CZ6h0IFoVO1ljsH-PKR_2hMyAfEvfwAlG0qslQeHamNCajspXElCy-TYy7uaiFaWzvoIlTocfAClFTYqaScYKDENWyl4kPy3Xxky0wZ3NjQkzQ8n8pGBqFh37KmbvWBqNil9ApmtM5r6RQsO9d578Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681706" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پایان جهان شاید زودتر از تصور باشد!
🔹
جهان حدود ۱۳.۸ میلیارد سال پیش با رویدادی موسوم به مه‌بانگ (Big Bang) آغاز شد. از آن زمان تاکنون، بشر توانسته مسیر تحول کیهان را تا حد زیادی درک کند، اما همچنان نمی‌دانیم که چه پایانی در انتظارش است.
🔹
پژوهشی جدید که هنوز در حال داوری علمی است، احتمال می‌دهد جهان حدود ۳۳ میلیارد سال دیگر به پایان برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681705" target="_blank">📅 18:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW179nJD6dYaucU4cindA_6QCHM5Mi2As4rQ5ce7VNZpr12yQycryctGFEGf4DRapaEk5nUQYmNudWWRSyDSpWsZ6qpTc32A6-Snsj6uejH6X8vQENlK2_MjUD-bK1OXHFJ1WdGTZzs7WiAAcHLPQgXA2YiPxYV3jsObrax-pDjzF-Q9UwWOmoXsoWDZ7cMkKWyhOgPTtu4Wik-qX1B8xGqJ0U5odr5wH2hZI6fve20efELjt54BYicwy2JG50d7KlAoo3N_nkEmZ4T4ByMeAylKj6Nyb26qqIe4TQ4mzxy6uACE4EK67e-6yrsc0B3DqBxFxSvEYacmYaFanRpoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ۷۲ ساعت گذشته سه کشتی در تنگه هرمز مورد اصابت قرار گرفتند
🔹
طبق آخرین ادعای مرکز اطلاعات دریایی مشترک (JMIC)، از زمان گزارش قبلی آن در ۷۲ ساعت پیش، سه کشتی هنگام عبور از تنگه هرمز مورد اصابت قرار گرفته‌اند.
🔹
دو فروند از آنها در آب‌های سرزمینی عمان در حال حرکت بودند، در حالی که فروند سوم در مکانی نامعلوم هنگام حرکت به سمت تنگه مورد اصابت قرار گرفت.
🔹
هیچ آسیبی گزارش نشده است و در هر سه کشتی به سفر خود ادامه داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681704" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حمله خونین با چاقو به نگهبانان بیمارستان مدنی کرج!
🔹
فاجعه در ساعات غیرملاقات؛ همراهان یک بیمار که قصد ورود با زور و خارج از وقت قانونی به بیمارستان مدنی کرج را داشتند، پس از ممانعت نیروهای حراست، با چاقو به نگهبانان بی‌دفاع حمله کرده و آن‌ها را شدیداً مورد…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681703" target="_blank">📅 17:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8LpCN5lYnm7ttnvsLWj3JmfO2gsZN-iTCVyGJlOkuLbpWaQrLNpNDYYL3aBpxCHwBsz0Pgys6wG8kqpJaDWl0aXMv3oOsRv3RROy4QnMWY7GI_oyvDmWRGB0F-TZniqC2ch-QFspQ3LGnWKnG7LC2pnIWsnNkGHO8fVwBs6YqfFPoyQdO_mURG0M1SEQw1OybdatyaN1VDjGd-F4-GkqDd--nd5aEXjSEF1fciH5Qc5DEmYN69El_2ilUH3nocBK6qa9YzaMlFTECb8eoWRRu7AWhGUFDUOBq4fHHvF8iSbkV7j8ysW4J24hGtOTmdlINAo3bY1YFP1O87tZRhrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخمل کوه زیبای لرستان
🤩
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/681702" target="_blank">📅 17:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/681700" target="_blank">📅 17:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
آکسیوس: میانجی‌ها همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفتی نیست
آکسیوس به نقل از منابع آگاه منطقه‌ای:
🔹
میانجی‌های پاکستان و قطر همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفت ملموسی حاصل نشده است.
🔹
پاکستان ارزیابی‌هایی خوش‌بینانه‌تر از واقعیت ارائه می‌دهد تا این تصور را ایجاد کند که روندی رو به پیشرفت وجود دارد؛ تصوری که می‌تواند به شکستن بن‌بست کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681699" target="_blank">📅 17:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9stw2HyypcjOkY1UwUk-wRj3jYeaQAj5_iREQcW7yZ8hFk9x_AHeTZRU482Myk2hxHFH1o9_0CFFqmSRyvXxxsNH3he53sksnKOo1OEHgY7QcFze23qDEHzStvrNBYvsGefAlGtgWAE7nIS9Zq5nr6M9Qimy3Kg30sLaTUeiK_9w_5oP04D83SHeR8Q8A_hMi5Bd1IRT7sl2d0B0XgTY3U206X5DwGqZ1z031TQyHdDMq8Yu56DiA7BOUxhac1NHJymNh6JD_EWVbzNM13PfYIVkjC12OzDSBfTtNty04VuzJTaTIL543ayAtiNK-bXQqbC0FkwMYS1gThodJQbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۰
🔹
رکوردشکنی بانک کشاورزی در پرداخت قرض‌الحسنه؛ رشد ۶ برابری در سه سال اخیر
🔻
مبلغ تسهیلات قرض الحسنه پرداختی بانک کشاورزی با جهشی چشمگیر از ۷۰ هزار و ۵۴۶ میلیارد ریال در سال ۱۴۰۱ به ۴۱۳ هزار و ۸۸۳ میلیارد ریال در پایان سال ۱۴۰۴ افزایش یافته که نشان‌دهنده رشدی ۶ برابری در سه سال اخیر است.
🔻
این بانک در چهار ماهه نخست سال ۱۴۰۵ نیز با پرداخت ۱۷۱ هزار و ۲۲۶ میلیارد ریال تسهیلات قرض‌الحسنه، روند رو به رشد حمایت از متقاضیان این تسهیلات را تداوم بخشیده و ۶ برابر نسبت به مقطع چهارماهه ۱۴۰۲ افزایش عملکرد داشته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681698" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bybh-GGMrqUD_nqIWDUqQeoqtYEAyRvrgYiWgqwojGte5o_ZHw-QBzh7O2NdaRDq2J-o_-g8Syq7VqO_b-OjW5PGwUHgB4NOv5vl-PYuewv2w2xG0YvF_TosfTZ8yodQEAyAuU8sMareLtsgL1osXYqkS0FteU5WJIqwMPu-Ltc2V9K1MglbqkOWaIvbPntJfK2-ZlmIamhO0GJs7mUgeesyuD1TC50wv50cWff7toQLD0kRJJx1JPSZCibHW-9zeSHGQqyWMAVCx8hhSzNFdcFFH2TXVjqB-IjtSQNZBJPkR4YaSH0mtxXWibJZN5coZlgBmYEEozH7VF2w5381mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از گوشی جدید ۶۶۰۰ نوکیا که از سری کلاسیک خود الهام گرفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/681697" target="_blank">📅 17:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بیداد کارت‌های بازرگانی اجاره‌ای؛ ۲ میلیارد دلار ارزی که تبخیر شد!
«سلیمی» عضو هیئت رئیسه مجلس:
🔹
کارت‌های اجاره‌ای بازرگانی بیداد می‌کند و ۳۵ درصد تعهدات واصل نشده ارزی مربوطه به دلیل همین کارت‌های اجاره‌ای است؛ سؤال این است که چرا دولت برای اجرای این قانون ورود نکرده است؟
🔹
قوه قضائیه حدود ۳۰۰ کارت اجاره‌ای را کشف کرده که به میزان ۲ میلیارد دلار است و این مسائل نیازمند توجه جدی است و باید با این مسئله برخورد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681696" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681694">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCCfeS0YsNBzyqOowkU2QWFaAGH1dhvwWWI1Y6r8d2qDgY0hqBFSvb1DAtQfnVkN8Sb00FHWUXOy1z4gJ80PMUTPKWjYy1IdJQS2U0ghdOzRlj627l8q-UaYqTMrsJlJHoBym2D8ZjD-34Fa9NzLJuCApMchWKvq_shUWF-ZkADeZqeZzawsAtBoy44FIFzIP2nL9kVO-V5UnKKEAX0uOVQHar06d3q8RvSPiaxd_WY_sOhFjljlgYdTgYyXB0Kb7dTnrjrjreSxlQu3eK72aZP_nGOvfdbY2eKxyFEW1MozmNIJtbniQGLoFp8qGUHDhB4wgCZKiDzC9BFdl6b8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین بازارهای سهام جهان
🔸
آمریکا با ارزش بازار ۶۹.۸ تریلیون دلار، با فاصله‌ای چشمگیر صدرنشین بازارهای سهام جهان است.
🔸
پس از آمریکا، چین با ۱۱ تریلیون دلار و ژاپن با ۶.۷ تریلیون دلار در رتبه‌های دوم و سوم قرار دارند.
🔸
نکته قابل توجه این است که از ۱۲ بورس برتر جهان، ۶ مورد آن در آسیا قرار دارند که نشان‌دهنده سهم بالای این قاره در اقتصاد جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/681694" target="_blank">📅 17:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردسرهای تسلا در هندوستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/681690" target="_blank">📅 16:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ودوم از فصل پنجم
🔹
در این قسمت تجربه‌ نزدیک به مرگ دو خانم نوجوان با محدوده سنی ۱۰ سال به نام رضوانه که در حین تمرین سرود بر مزار شهدا روح از بدن جدا و توسط ۴ فرشته به آسمان عروج کرده و با رؤیت و دعای فرد سبزپوش با شکافی بر فرق سر، به جسم باز می‌گردد و خانم ریحانه که بخاطر سرماخوردگی شدید در حین استراحت در منزل، روح از جسم ایشان جدا و تجربیات جدید و شنیدنی را درک می کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گران
: رضوانه عرب نظرگاه/ ریحانه رشیدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681689" target="_blank">📅 16:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل ترمیم و پرکردن مجدد دندان آسیاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/681687" target="_blank">📅 16:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وام گرفتن همیشه راه نجات نیست، اگر می‌خوای وام هوشمندانه بگیری این ترفندها رو از دست نده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/681686" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده کل ارتش خطاب به ترامپ جنایتکار: غلط میکنی می‌گویی تنگه هرمز برای آمریکاست
سرلشکر حاتمی:
🔹
رئیس جمهور جنایتکار آمریکا می‌گوید که میخواهد تنگه هرمز را بخشی از سرزمین جنایت، اعلام کند، شما خیلی غلط می‌کنی! او بعد از آنکه واکنش‌ها را دید، اعلام کرد که شوخی کرده است.
🔹
شوخی این حرف هم، غلط زیادی است چراکه اینجا ایران است و حافظانی دارد که قلم پای شما را خواهند شکست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/681683" target="_blank">📅 15:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله خونین با چاقو به نگهبانان بیمارستان مدنی کرج!
🔹
فاجعه در ساعات غیرملاقات؛ همراهان یک بیمار که قصد ورود با زور و خارج از وقت قانونی به بیمارستان مدنی کرج را داشتند، پس از ممانعت نیروهای حراست، با چاقو به نگهبانان بی‌دفاع حمله کرده و آن‌ها را شدیداً مورد ضرب و شتم قرار دادند!
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/681682" target="_blank">📅 15:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
چرا خاموشی‌ها دقیقاً مطابق جدول زمانبندی اعمال نمی‌شود؟
معاون برق و انرژی وزارت نیرو:
🔹
برنامه اعلام شده از طریق سامانه برق من یک برنامه احتمالی است و در صورت بهبود شرایط شبکه، خاموشی پیش‌بینی شده اعمال نمی‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/681680" target="_blank">📅 15:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل گرانی مسکن در ایران چیست؟</h4>
<ul>
<li>✓ تورم</li>
<li>✓ دلالی و سوداگری</li>
<li>✓ عدم نظارت جدی بر بازار</li>
<li>✓ افزایش تقاضا و رشد جمعیت</li>
<li>✓ کمبود ساخت‌وساز</li>
<li>✓ نگاه سرمایه‌ای به مسکن</li>
<li>✓ افزایش قیمت مصالح</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/681678" target="_blank">📅 15:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس انرژی از عرضه بنزین سوپر در معاملات ۲۸ مرداد با قیمت هر لیتر ۸۹ هزار و ۷۰۰ تومان خبر داد.
🔹
پزشکیان: در روش‌های آموزشی باید به معلمان و مدیران مدارس اختیار و آزادی عمل بیشتری داده شود.
🔹
سوریه پروازها به مسکو را از سر گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/681677" target="_blank">📅 15:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر نیرو: به دلیل سنگین شدن بهای برق در بازه‌های دوماهه، در دستور کار است تا دوره صدور قبض‌های برق به یک ماه برسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/681676" target="_blank">📅 15:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای چین‌های یکدست این ترفند رو یاد بگیر
🔹
یک‌ترفند کاربردی برای علاقه‌مندان به خیاطی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/681675" target="_blank">📅 15:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681674">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeYsuUd8gxym14whn0amBGLbkKfN7ud7j1oFyFGNNYeoZeoWzW0nJ_w0bnCJNf7qznhEAVePu6d6aCMoBlvrFw4Fy5Tde9zhMtjHNDRFAZwBalMHQdcrB_uDnTb3ECXDSnAoKGPafbMvBBD2S05VwkXuihiGvsyD1EsDk4DbpsTIfiFypn4ENSuz87rNNVoc1n1rFSzPaYxzqXqBrUJ-Z5I3yBh6w6shLEqBOZos3WrqFz05BO9QDYlS3rJ5JdVfObcdc7fMjOEL1WhsiddvjpBQRzMPrDylssWo5axFr2lhRDDYic57ZpHYpXWJzQpFyWacLarT5ZVLtN-tzO28WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مردم قروه و دهگلان در مجلس:
زمان بازنگری در ممنوعیت واردات ۴ قلم لوازم خانگی رسیده است
🔹
محمدرسول شیخی‌زاده، نماینده مردم قروه و دهگلان و عضو مجمع نمایندگان استان کردستان، با انتقاد از ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را شکست‌خورده دانست و گفت ادامه آن علاوه بر محدود کردن بازار و افزایش فشار بر مصرف‌کنندگان، درآمد رسمی مرزنشینان را کاهش داده، قاچاق را گسترش داده و درآمدهای گمرکی و مالیاتی دولت را نیز کاهش داده است.
🔹
ممنوعیت واردات لزوماً مانع ورود کالا نمی‌شود؛ بلکه مسیر ورود غیررسمی و قاچاق را هموار می‌کند.
🔹
از نیمه اردیبهشت، میزان واردات رسمی چهار قلم لوازم خانگی حتی از مسیر کولبری، ملوانی و ته‌لنجی صفر شده است.
🔹
محدود شدن تجارت قانونی مرزی، بخشی از درآمد رسمی مرزنشینان را کاهش داده و فشار مضاعفی بر معیشت آنها وارد کرده است.
🔹
ممنوعیت واردات باعث شده مردم به کالای باکیفیت و متنوع دسترسی کمتری داشته باشند و هزینه تأمین کالا برای خانوارها افزایش یابد.
🔹
وقتی واردات از مسیر رسمی انجام نشود، دولت از درآمدهای گمرکی و مالیاتی محروم می‌شود.
🔹
ادامه ممنوعیت واردات، بیش از آنکه به نفع تولید و مصرف‌کننده باشد، در عمل به ضرر هر دو تمام شده است.
🔹
زمان آن رسیده است که ممنوعیت واردات لوازم خانگی جای خود را به یک سازوکار شفاف، هدفمند و مدیریت‌شده بدهد.
🔹
این سازوکار باید ضمن حمایت واقعی از تولید داخلی، مسیر قاچاق را محدود کند، درآمدهای رسمی دولت را افزایش دهد و امکان استفاده مرزنشینان از ظرفیت‌های قانونی تجارت را فراهم آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/681674" target="_blank">📅 14:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSfyY17bJQYk8nCGuBcKCgtxxkqPNrd4kckhVG8EqWPxHd4SJChYCQ4ZMD6Pl6VaAzuLrYydfl9yuIAngEiTFpY-dRY8af6xUuzJPTm9DxM1exI64lCAqhg2dLT98xnNWAgaecZRgdb5Krt_XIXD8lO5ep-K-bfKagtazpTexPiiY3I9M3PWwtRp-QdAzmj-QmGj9w8u-VHWng_oxDVPPsx0rctDWB9k5Viweb33exHQNHhMJemibZQjR7H6TvUJ86cQDE7jn_hRoEHI7Y2TAzNkGeOK364VLLVtB1F2AWXY8H9QxMe7G_Uv1WlpxACVFMSrMdppjh9GHZtQSUMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید
فرماندهی سپاه پاسداران انقلاب اسلامی:
🔹
فرمانده کل سپاه با تقدیر از شش ماه جهاد رزمندگان اسلام تاکید کرد: شما در گرمای سوزان جنوب، سرمای ارتفاعات شمال و زیر آتش سنگین دشمن با عملیات موفق آفندی و پدافندی، مسلح‌ترین ارتش تاریخ جهان را به زانو درآوردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/681672" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اولین تصاویر از جانی بی‌رحم چهارراه گلزار کرج  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/681670" target="_blank">📅 14:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استانداردهای دوگانه برای «حقوق زنان»
🔹
برای ایران: تحریم، فشار، تیترهای داغ
🔹
برای صهیونیست‌ها: سکوت مطلق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681669" target="_blank">📅 14:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هر آمریکایی متجاوز به ایران را بکشید یا تحویل دهید، ۵ میلیارد تومان پاداش می‌گیرید
طرح جدید ارتش که توسط سرلشکر حاتمی فرمانده کل ارتش اعلام شد:
🔹
پنج میلیارد تومان پاداش برای کسی که هر آمریکایی متجاوز به خاک و آب ایران عزیز را بکشد یا به واحدهای ارتش تسلیم کند.
🔹
همینطور اگر هر زن ایرانی، یک آمریکایی متجاوز را بکشد یا دستگیر کند، مبلغ پاداش دو برابر یعنی ده میلیارد تومان خواهد بود./آوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/681668" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/681667" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران کشتیرانی در راین آلمان به دلیل کاهش شدید سطح آب
🔹
سطح آب رودخانه راین در آلمان به دلیل خشکسالی طولانی در اروپا به شدت کاهش یافته و کشتیرانی را در آستانه فروپاشی کامل قرار داده است. در برخی نقاط، سطح آب به تنها ۸ سانتی‌متر (و حتی در شب به ۶ سانتی‌متر) رسیده است، در حالی که عبور کشتی‌های باری نیازمند حداقل ۴۰ سانتی‌متر آب است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681666" target="_blank">📅 14:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال عجیب خبرنگار از رئیس‌جمهور: نوه‌هایتان به شما نمی‌گویند کاری کنید که مدارس مجازی شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/681665" target="_blank">📅 14:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا و رژیم صهیونیستی قرار دارند، اما ملت ما شجاعانه، مردانه و خالصانه ایستاد و جنگید.
🔹
بنده به‌عنوان برادری که به جزئیات کار آشنا هستم با همۀ وجودم می‌گویم که ما در این جنگ هم در بعد نظامی و هم بعد سیاسی به معنای واقعی پیروز شدیم.
🔹
تفاهم‌نامۀ بین ایران و آمریکا سند افتخار و پیروزی در راستای تثبیت پیروزی در میدان دیپلماسی است.
🔹
البته معتقدم که مردم ما حس این پیروزی را به گونه‌ای که اتفاق افتاده، حس نکردند و در برخی موارد نتوانستیم این حقی که مردم داشتند را به درستی ادا کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681664" target="_blank">📅 14:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ایده استایل شیک برای خانم‌های محجبه و خوش‌پوش #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/681661" target="_blank">📅 14:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
امید به‌ زندگی در ایران به ۸۰ سال رسید
وزارت بهداشت:
🔹
امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/681659" target="_blank">📅 13:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/681658" target="_blank">📅 13:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سرباز نیروی دریایی آمریکا به شرایط ناوها
🔹
یکی از سربازان نیروی دریایی آمریکا با انتشار ویدیویی، از شرایط ناوها انتقاد کرده و با لحنی طعنه‌آمیز می‌گوید: «بیایید عضو نیروی دریایی شوید!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/681657" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متیو مک‌کانهی ۴۰ دقیقه ملکه زنبور را در دست گرفت
🤯
🔹
متیو مک‌کانهی برای فیلم جدیدش، ۴۰ دقیقه ملکه زنبور را بدون آسیب زدن به آن در دست نگه داشت تا هزاران زنبور دورش جمع شوند و این صحنه بدون جلوه‌های ویژه ضبط شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/681656" target="_blank">📅 13:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اندیشمند برجسته آمریکایی از ۳۰ سال نیرنگ و عملیات آمریکا علیه ایران؛ از ترور تا جنگ اقتصادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/681655" target="_blank">📅 13:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
ادعای اکسیوس:
🔹
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند؛ آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
🔹
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
🔹
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد؛ او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681654" target="_blank">📅 13:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال در اوگاندا؛ بازسازی دوران استعمار
🔹
برخی از گردشگران سفیدپوست در اوگاندا با پرداخت پول به افراد محلی، خود را روی تخت‌های آهنی حمل می‌کنند؛ اقدامی که یادآور دوران استعمار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/681653" target="_blank">📅 13:05 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
