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
<img src="https://cdn1.telesco.pe/file/BxXmMurg0yJJoPNIZWMZ4qqg4Mrta8ceIOsca45az64CBhNFoqUDfzzAQw9Wt8kt32A2x4ebzA2pOPMu-a5__t-rCcbFYpsbMhkD9hOk5OgnfcIOLIzuTJHeIcDADPMQ5EyxzRbwxKM_LDI_pp3EqXkkV02Hvf7EnHbCDykS3E_89y6z4_Sr9HxffuaHzc_yrCEt95icyucLy7g7JTOFvq2XZai2iJsCApUfjuy1q8o51EJcTqXNdNup8Yfj2SglkdTgrEhrCUwTeeG9XCzXjm5RpT5tpesphse2LcKRmwhem56fcHfo98SGXHOUyL-9qKht6lsWCxk9Mb7oZxVeFg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 22:06:34</div>
<hr>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKiV6jDt3CCgpQfXdm5ecyZe-tAK4sfwDEsrVFMbs-_4lZD0iMC1ELHShHlJZlEzT0fWnzmM3VwuPQ7qo0CUtrT_tU8j4KyuXYtTVPA-1qDpuj50m4wZyBqqGG6vZY7rKLEsGSdr37nWHCiWOWj4ztO7uP2EUa0ezBvxNoN0zEFJFE_jXh3mhdgLoCVNOAKKiDTjjyXMOH5UzW1gVBGkcIAr1GSfBwgr--erLmX4h3l8Avozsh1MKZJBg2gPrZyZ6lXBYW-Y6dNpXTXu0HEoMhChzSutxN8GEUlAxsQy2InRVBhkB-iKub_9fQ1KXxLQ69wg6syaXowBfxU8RpSrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW1Cpcjo7RWWv0d40vK6ZbVkKBwIVK4XvVcfKsqMITKLaxOJz86mFOG11gw9FGkWBTC8Xc4x2VaHkwTciIYHGKVO5hnBLr2Yscn6hLYSGQfQ4QwaxJ_mF4qqjGQrcrRsuE5e-J3j5At2WwRMIx5GwRIiCUrohVKEtJGxdiuwjOhMgZ7mer-mwIEnyy8d5cXX6R690MN6ZcEAn2eJwrm4ymL2JU4EZfDbiy5BNpSGP4dnQKDwXsjl-oFGhqFXnsyGaz5qLgFvLzk0R0aIG2ICAviLmi_XOCMp-DgDoYytgmDCe7gIPgRqTFdWQmYPiJJ7smG2PYu3i6w0kAS--uU5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqkvst42AkE1zYZUxb7tj4ZVPpRZIlEuwfBoMvOhoZ727sE_5eW9l3En-te7dF_FyEHI1ksF3b008uQWNy4pu4wsrvE1DMyW-zIN6DwtjSPrdmAHgKXKtpD36jbs82x5aP3UQRbEltEp0KNZIXg8YRqYnyTLHfWYDa-CY0J3ltABXUnw6teppLivUbUmO3a_FMOqM7_4SW_MZClKYLjlgnkKWR7DoJ6j30IyB84oWKLgh7jw-x0LLJpDyrEVlJqYi8mrxeDo31QloP8mzBlHNhLQ-GnQMs_q6WxHC7JYRtJU9XxOOm6CJUhVF8M8lXflf2rhWHMUNPFC85GaQNS-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIG1U2wqn7OouvMpgXhOoFxLC2w0edEETYm8UGRqI81lKS2-sChtp5xanVJPAfmYdV9vf8biCZG9jbJT-TcIFgrzDPRD3yYI414susH51on8lfUucE29SK-PAfXqjZqiOX0CX2RaxTWj02LGHJ_tsJvLO46vHvkoJ222Tk4hNADGWwXZnM4OJ31HTfq2Ycghu4LcxxqDWrYBH-OD75MJzU6TR77coE4IZcdsQPwly0naA4mdHwSxMtdeIu1QfgH8Bu2fJ5BVrrGqc-eh_xl0eHDisL1uX0Wqizpf7owTqYVknGpx6rnSOYm0t4FJ7DatAhcF_MIYxBCraxX2x6Odww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=i1g1GK-1pEdY9ajZ-2l0-KsAJjsQOWtARwbP-ZfiLecKCmU-EaXO-2uCP8CO-KNue3jt0z1q1iYxKE6lfEO4UXwrdl4APkYgFaZLoRgYmegl2dUP8TGR_eBNEf6ymOMkE2lRweG_faAG-46B_GSXZpf95lau7kZ-iYfPNy7RbWP5Cp7Ch7wuPNS80H2hDOzyGKMDk9aX7zx4xFo8sOSLWKlsflHL1ALumFUFpCQUSXOEkJMLYzV-w-aSGaJKGBNUQkf8n71XE2O7mdYYzm_IlaugQ6SyO4c4m0svhO8PenYjxTbC-34dYyMsrgzxo4OVoxhfcqOKt5AGiJLU4d1OKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=i1g1GK-1pEdY9ajZ-2l0-KsAJjsQOWtARwbP-ZfiLecKCmU-EaXO-2uCP8CO-KNue3jt0z1q1iYxKE6lfEO4UXwrdl4APkYgFaZLoRgYmegl2dUP8TGR_eBNEf6ymOMkE2lRweG_faAG-46B_GSXZpf95lau7kZ-iYfPNy7RbWP5Cp7Ch7wuPNS80H2hDOzyGKMDk9aX7zx4xFo8sOSLWKlsflHL1ALumFUFpCQUSXOEkJMLYzV-w-aSGaJKGBNUQkf8n71XE2O7mdYYzm_IlaugQ6SyO4c4m0svhO8PenYjxTbC-34dYyMsrgzxo4OVoxhfcqOKt5AGiJLU4d1OKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbY9XkwTonv7ZIAqWZiVGyov7kZ1AIODuJWrJAsxpK-JtmckLun4ICm__rykUJN1UXAKB9Hg8RLqeloZZmG94biWVNEic-mDm5s19AB8Gx3La0aWujqb5WL6xmgjP1JVULVWCwMedOBsw94bGuB5HMrjEqT0UQfDJ262e7TWHmaXdUKtII3ACnmSlfs1HYS2xbwGUGgTG7ae-boLYWSW4PvcBKAGHlI5h8xGhK0SWlsAh2ci0SZeX7QAonQLrCsxjk8I9K5jcsWu6ema9X0ZR0Qq5oRwzE_Ec-HPcxFDHLU7fOtTdLbUHnmJvOKuzxIadq92YCcZ_IgP5-a8HAUZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hHhSjMS2n6SNIVlbfUpVGAu6laFQ0ICCudWIyKkrYCJ7y31a7AdHfTKoKLLim5Q5yRVEwdzvSC-fPpMom-rAUiS2nzN2-rEwqxJ_g2LX7jIxjdHktlx5D1ry2Nnfl1tgFSvZFmlBNNnCOVAbrhU1_mM6Sk7P2xLeGNpQQ8N6PoRrgWHcYOAZWHujc8-TItdB3Qxy55OhNhMFTaWfAOXItWk9r2VElhc-sRuQImlJpcrnFUJHCfRTmo_r_kpT5TsL-OHAM9H0ZYmjzsrsGUjWFkWEcC9kl9TP005OV4n151LmRrXDZ0btHrqYj1Jx2igIjvaZfavfh6rkhy4WK9wHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی به نقل از سه منبع آگاه گزارش داد جنگنده اف-۱۵ای آمریکا که ماه گذشته در ایران سرنگون شد، احتمالا با یک موشک دوش‌پرتاب ساخت چین هدف قرار گرفته است.
به گفته یکی از این منابع و یک مقام آمریکایی آگاه، چین همچنین ممکن است در روزهای نخست درگیری، یک رادار هشداردهنده دوربرد را در اختیار ایران قرار داده باشد که این رادار توانایی شناسایی هواپیماهای رادارگریز را دارد.
ان‌بی‌سی نوشت مقام‌های آمریکایی همچنان در حال بررسی سرنگونی جنگنده اف-۱۵ای هستند و هنوز روشن نیست تجهیزات نظامی احتمالی چه زمانی به تهران تحویل داده شده است.
کاخ سفید به ان‌بی‌سی گفت شی جین‌پینگ به ترامپ اطمینان داده پکن تجهیزات نظامی به ایران نمی‌دهد. سخنگوی سفارت چین در واشینگتن نیز گفت پکن صادرات نظامی را «با احتیاط و مسئولیت‌پذیری» کنترل می‌کند و با «تهمت بی‌اساس» مخالف است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75800" target="_blank">📅 07:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMMie3fAnIZOhZaMVsFcp3nC-CGCtotfp7Ry0xnAyJHZ0Q4J-m726OGYqQ3b8p45d0iwp28p4U9at6UXsfJc-sDrhrvTbvRjQbwd8PgbOkX7_4OWhllCAEjDMp6H9bzy4RtAYjCI4UMWl5iyxJqvHLJTLwc5XlHrfoHNuOqeXWINlWHz10gZkWhlFWVgpYMYNA3AXvhaQ_dB3rePrwWnvZTgAw0VuvCWQ9Nir1wegZa4AKiOQ4corDjTpQVYFNxcIHt-96A_RIHRrvE59fNvt1MS_Sso0j8_9wbqFwyqK_4qjgAq1AfEC2jWKckdjhaqinmX0a9ykfjAXMaC_cex2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'به جای پول نقد قطر موافقت کرده ۶ میلیارد دلار  اعتبار در اختیار تهران قرار بگیرد تا کالاها و محصولات اساسی را از قطر خریداری کند'
یک منبع آگاه از روند مذاکرات به ایران‌اینترنشنال گفت سفر قالیباف به قطر به شکستی دیپلماتیک منجر شد و با وجود درخواست تهران برای آزادسازی فوری و بی‌قید و شرط ۱۲ میلیارد دلار به صورت نقدی همزمان با امضای یک یادداشت تفاهم اولیه با آمریکا، مقام‌های قطری این درخواست را رد کردند.
به گفته این منبع، مقام‌های قطری تنها با آزادسازی نیمی از این مبلغ تحت محدودیت‌های سخت‌گیرانه موافقت کردند.
بر اساس گفته‌های یک منبع نزدیک به یک مقام قطری حاضر در این گفت‌وگوها، دوحه از انتقال مستقیم یا نقدی این منابع به ایران خودداری کرده است. در عوض، این پول تنها به صورت اعتبار در اختیار تهران قرار می‌گیرد تا کالاها و محصولات اساسی را مستقیما از قطر خریداری کند.
این محدودیت در شرایطی اعمال شده که آمریکا به شدت با اعطای دسترسی مستقیم و بدون محدودیت جمهوری اسلامی به دارایی‌های نقدی مخالفت کرده است.
آمریکا ابراز نگرانی کرده است که تزریق مستقیم پول نقد می‌تواند برای تهران فضای تنفسی اقتصادی حیاتی ایجاد کند و به آن اجازه دهد حقوق‌های معوقه بخش عمومی را پرداخت کرده و در دوره‌ای از تنش شدید منطقه‌ای، تجهیزات نظامی را از کشورهای دیگر تامین کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75799" target="_blank">📅 03:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=kQxJflTiNFK0V-YS-um8bbDvTayjGAZiBfNxCiE621HjosKpW4hGkD9vDWK4x3XLxynVTufXg2gVQZvBcvuNPUpOmzZ3QJWhfds08Kz_MYPd2mW4xEueCdoHyXsMXLjwTQDILEhu-FueTVWNh-q7XCj7PT-_eU25fvKV64aSbZchR0q_0S0x32RvvRW8QH5J6i1HySWmr4FRRcK5ZyeMZJtADvumWdJQdfNT6NEE-ah1mDE3qAJS0H22hGcuFonFrPcWn77Wa5CjnFnRYAghyLFvEmk-hVVcHQC66qBSqNAQ0fBezSmQP-VJ1CnvT29XRgkrzFePP6Xx0LvYF98Kdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=kQxJflTiNFK0V-YS-um8bbDvTayjGAZiBfNxCiE621HjosKpW4hGkD9vDWK4x3XLxynVTufXg2gVQZvBcvuNPUpOmzZ3QJWhfds08Kz_MYPd2mW4xEueCdoHyXsMXLjwTQDILEhu-FueTVWNh-q7XCj7PT-_eU25fvKV64aSbZchR0q_0S0x32RvvRW8QH5J6i1HySWmr4FRRcK5ZyeMZJtADvumWdJQdfNT6NEE-ah1mDE3qAJS0H22hGcuFonFrPcWn77Wa5CjnFnRYAghyLFvEmk-hVVcHQC66qBSqNAQ0fBezSmQP-VJ1CnvT29XRgkrzFePP6Xx0LvYF98Kdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، بامداد شنبه ۹ خرداد با انتشار تصاویری مدعی شد بقایای یک پهپاد متعلق به آمریکا و اسرائیل که در حوالی قشم هدف قرار گرفته، کشف شده است.
تسنیم بیان کرد این پهپاد با واکنش پدافند هوایی ارتش هدف قرار گرفت و منهدم شد.
پیش از این خبرگزاری مهر به نقل از منابع محلی گزارش داد یک ریزپرنده در حوالی قشم از سوی پدافند هوایی هدف قرار گرفته و منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/75798" target="_blank">📅 02:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9AG5ERQEQMucFD98J4DqJomVe5DLWYZtHAcNPPBIAoLJgwtWsgHMtQi4y4PcsmWsJ7GWdUdpSBmQ6A5Lc6Gre7lWvft2x2hDQmg5T3lVTa1mvhIFCjTtH0pGzXwsAlv9r3hjd7ZVUWRrwHYYvHR1vC24GQwjRDu-E815EWFinr05byWDHspr_U_xSwQ3VBebBOKKUFVGYPgvOMutfr6Bq5czHrdv5frQe4XvcajaZ9ptTcOgnxEINLTnDnhPLKsV944v2tBS8erDr4ygm8Y8FZ_fyziQ2Vrs-9RP1MIdJhRCJy8VvxWKsvTpg2Lm3wqmvgb4iIeGfbvoJYsVJA3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌پست، یکی از آخرین موارد اختلاف بر سر راه توافق احتمالی میان واشینگتن و تهران، چگونگی آزادسازی مرحله‌ای دارایی‌های ایران است که در قطر نگهداری می‌شود و برای اهداف بشردوستانه در نظر گرفته شده است.
بر اساس این گزارش، منابع مالی مورد بحث مستقیما در اختیار حکومت ایران قرار نخواهد گرفت، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده می‌شود و سپس این اقلام به ایران ارسال خواهد شد.
نیویورک‌پست به نقل از یک مقام دولت آمریکا نوشت پرداخت تدریجی این منابع به اجرای تعهدات از سوی ایران، از جمله بازگشایی تنگه هرمز و پاکسازی مین‌ها در تنگه هرمز، وابسته خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75797" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=LZI-7Pj3SHCTICS6coGayOzJzpO5FYTlvzTToC6th8Z5nrkWgADjGYlUlb6NmblAID22eCmgUIv7NDB4XzgN-TaxSNyLYU6vJPwaFw-nnT09MYqrp-L6gll95s90pqPmfedIJsgYuSBBTJHIF8h5Ah2vH4Gh31rocKp78do50QBMScCvlsaF8XmNFS5PIirB3DG0InFB-sUJnj7WI3kH_DksWRvvPY33Zci-VdXg4rETVCm8jk0we_8ei4ynY9n6pjzan21ImajMJcRl8AF_goI2vipi8JfRrD_R0ZCdj9UQyPIsxypQNPMLH-BACt4f0QQbqxaM1HiyemiKbQBkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=LZI-7Pj3SHCTICS6coGayOzJzpO5FYTlvzTToC6th8Z5nrkWgADjGYlUlb6NmblAID22eCmgUIv7NDB4XzgN-TaxSNyLYU6vJPwaFw-nnT09MYqrp-L6gll95s90pqPmfedIJsgYuSBBTJHIF8h5Ah2vH4Gh31rocKp78do50QBMScCvlsaF8XmNFS5PIirB3DG0InFB-sUJnj7WI3kH_DksWRvvPY33Zci-VdXg4rETVCm8jk0we_8ei4ynY9n6pjzan21ImajMJcRl8AF_goI2vipi8JfRrD_R0ZCdj9UQyPIsxypQNPMLH-BACt4f0QQbqxaM1HiyemiKbQBkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز جمعه هشتم خرداد در «مجمع اقتصادی ملی ریگان» اعلام کرد که واشنگتن حدود یک میلیارد دلار از دارایی‌های رمزارزی مرتبط با حکومت ایران را به طور مستقیم توقیف و کیف‌پول‌های دیجیتال آن‌ها را ضبط کرده است.
او با تاکید بر اینکه این اموال در واقع پول‌های دزدیده‌شده از مردم ایران است، اشاره کرد که بسیاری از صاحبان این حساب‌ها هنوز متوجه ضبط دارایی و کیف‌پول دیجیتال خود نشده‌اند.
وزیر خزانه‌داری آمریکا همچنین افزود واشنگتن با همکاری نزدیک متحدان اروپایی خود در حال ردیابی و توقیف املاک و مستغلات، از جمله ویلاها و خانه‌های متعلق به این افراد در سراسر اروپا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75796" target="_blank">📅 23:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1DKLT3cka7rmvW3v5-gZX5R4xJQwZ4ij5CoIioWHt-jzXDaOxsoloM_7cpWh7ynhECXgoj776Q1Cc5d7FstI0ECjGrNGKBHm1sqL5p1BbmbV1wAjfeEh0xXpGHiwRVd_E7cRgW5PceT_PjYFTxk7tptAaOS4y2axbi8e-lyPokeUJ9lCHkOfuZ93RMvn7954XKWNdi3UoeEMF9Vewlj7EmOaNkzfUa_lsKfLN6tdBV-vTsKmQ26B7puu9Iou3ORkeWEKpFfc8_VQ5bPL65t4YynFWhX1Od-DQLR0jtsu_xjttMS_2E6Nq_NOZoV5r3q4Ic-uAZ7pECl9HBx4WANtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از یک مقام ارشد آمریکایی گزارش داد نشست دونالد ترامپ در «اتاق وضعیت» کاخ سفید دو ساعت به طول انجامید، اما رییس‌جمهور آمریکا هنوز درباره هیچ توافق جدیدی با تهران به تصمیم نهایی نرسیده است.
این مقام افزود دولت آمریکا معتقد است به دستیابی به توافق نزدیک شده، اما برخی مسائل از جمله آزادسازی دارایی‌های مسدودشده همچنان محل بررسی و اختلاف‌نظر است.
@
VahidOOnLine
یک مقام ارشد به خبرگزاری آسوشیتدپرس گفت که این جلسه در حال بررسی چارچوب توافقی بود که آتش‌بس را به مدت ۶۰ روز تمدید می‌کرد و مذاکرات در مورد برنامه هسته‌ای ایران را پیش می‌برد.
این مقام رسمی در مورد اینکه آیا ترامپ پس از این جلسه تقریباً دو ساعته تصمیمی برای پذیرش این توافق اولیه گرفته است یا خیر، اظهار نظری نکرد.
sky
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75795" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDQpmh-f_xnZ9weP5asfzBYQbUYAxkKxZ5XaNdMCL73MFCFI2Cx_XK7Y4QOvxYiOpA9pMM9kzH174etF8p5pDhEPgdkopBvW0IwnU_v_nL0tAo1fn_PIJdBAAeyHNDTVhcQdFzURLtNMCh7TFq31P63cGg2qt3YRGcH_Y55vPsqM858IzgYndPs6sd_3W2HBW7SQ7fBo_ypJoacpLfB24wUjg8ogRNkXUygB_eHQ0qDPfv8-vNmbNh-vnOKH60NxTyV23xP4hfneOkKuZ-2nvJT9NMfswPVxdwRK7wz8fpNn1u5srr5C3B0BYL3o90EPs6l65ioTmweIse4pod0fPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال روز جمعه هشتم خرداد، در گزارشی اختصاصی به نقل از منابع آگاه فاش کرد که امارات متحده عربی در طول جنگ، ده‌ها حمله هوایی را علیه مواضعی در ایران انجام داده است.
منابع وال‌استریت ژورنال می‌گویند نقش امارات در این کارزار نظامی، «بسیار عمیق‌تر» از آنچه که پیش‌تر گزارش شده، بوده است.
بر اساس این گزارش، این حملات با هماهنگی کامل واشنگتن و تل‌آویو و با اتکا به اطلاعات ارائه‌شده از سوی آن‌ها انجام شده است.
اهداف امارات شامل جزایر قشم و ابوموسی در تنگه هرمز، بندرعباس، پالایشگاه نفت جزیره لاوان و مجتمع پتروشیمی عسلویه بوده است.
حملات به عسلویه که به صورت مشترک با اسرائیل و در پاسخ به ضربات جمهوری اسلامی به زیرساخت‌های انرژی امارات انجام شد، واکنش‌های شدید بین‌المللی را برانگیخت و واشنگتن را وادار کرد از اسرائیل بخواهد حمله به تاسیسات انرژی را متوقف کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/75794" target="_blank">📅 22:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#قشم
پیام‌های دریافتی درباره فعالیت پدافند:
سلام وحید
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
21:26 هشتم خرداد جزیره
#قشم
صدای توافق خیلی بلند به گوشمون رسید. حدود یک دقیقه صدای شدید پدافند، احتمالا برخورد موفق با پهباد نفوذی.
درود همین پنج دقیقه پیش پدافند قشم داشت شلیک می کرد درگیری بود
ساعت 21:25
همین الان پدافند قشم فعال شد و یک چیزی رو زد
🔄
آپدیت:
تسنیم: "در پی رصد ریزپرنده متخاصم دشمن آمریکایی ـ صهیونی در حوالی قشم توسط پدافند هوایی ارتش، بلافاصله در عملیات موفق مورد اصابت قرار گرفت و منهدم شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75793" target="_blank">📅 21:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZlC6kaW1ukfEpQxO6Qs-8IEAZheziw01rEbUE8ngNKmhFPGvkyjZwuo1jg0laG3qzvpfPiOiKR6136BPnz7DDxgnuDGzd36X3xKegVRznnqXwz9xl3Tb9hwLrSLqfYSVGGf47vpIt_8_q7EFYAZ_eKKTElQblM-Qk5KKYpYYEB5RjCuoNm9OjKI3_Q9d9AUeb3u15PGc4CG-Ce2XX0XlsFEeCxsoHIIh5iP6vCT_d5qjl1gzFpcvZ9ICwAGrG15Ec6kFfAMHZsc7BirkzMVPFKldlxc7EZAVWqPzFfjBUUW8U2mZfrrCvRuQUtA2AUcptpwq8NprYYaeO8H8PhbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ پستی از نیوت گینگریچ، رییس پیشین مجلس نمایندگان آمریکا، را در تروث سوشال بازنشر کرد که در آن نوشته شده بود: پس از بررسی جنگ ایران در این هفته، متقاعد شدم ترامپ در آستانه یک پیروزی تاریخی قرار دارد
IranIntlbrk
پستی که گینگریچ ۸ ساعت پیش نوشته بود، ترجمه ماشین:
پس از آنکه این هفته را صرف بررسی جنگ ایران کردم، اکنون متقاعد شده‌ام که رئیس‌جمهور ترامپ در آستانه یک پیروزی تاریخی قرار دارد. نقطه عطف واقعی برای من زمانی رقم خورد که تصمیم‌ها و مانورهای رئیس‌جمهور ترامپ را نه از منظر یکجانبه‌گرایی آمریکا، بلکه از منظر رهبر یک ائتلاف تاریخی چشمگیر بررسی کردم؛ بزرگ‌ترین ائتلافی که تاکنون در خاورمیانه مدرن شکل گرفته است.
همه می‌دانند که اسرائیل متحد مهمی است. اما آنچه کمتر درباره آن صحبت می‌شود، عمق حمایت امارات متحده عربی، قطر، بحرین، عربستان سعودی و دیگر کشورهای منطقه است. برای دیکتاتوری ایران باید بسیار تأمل‌برانگیز باشد که دریابد حتی یک متحد ندارد که حاضر باشد محاصره دریایی آمریکا را به چالش بکشد. آرام‌آرام، به‌تدریج و با احتیاط، متحدان اروپایی ما نیز در حال صف‌آرایی برای کمک در خلیج فارس و تنگه هرمز هستند.
بخش بزرگی از مانورهای رئیس‌جمهور ترامپ علیه ایران زمانی معنا پیدا می‌کند که او را نه صرفاً یک رئیس‌جمهور یکجانبه‌گرای آمریکایی، بلکه رهبر یک ائتلاف ببینیم. من بخش زیادی از چند هفته گذشته را صرف بررسی گزینه‌های نظامی کردم؛ از جمله پیروزی در نبرد خلیج فارس و تنگه هرمز و، در صورت لزوم، استفاده از سطحی تکان‌دهنده و خردکننده از قدرت نظامی؛ مشابه آنچه رئیس‌جمهور نیکسون و وزیر خارجه کیسینجر در کریسمس ۱۹۷۲ علیه هانوی و هایفونگ به کار گرفتند؛ اقدامی که هر دو رهبر معتقد بودند ویتنام شمالی را به پذیرش آتش‌بس و آزادی اسرای آمریکایی متقاعد کرد.
اگر این یک کارزار یکجانبه آمریکایی بود، می‌توانستم با اشتیاق از یک کارزار نظامی تهاجمی‌تر حمایت کنم. اما در عین حال روشن است که چنین اقدامی ائتلاف را از هم می‌پاشاند، زیرا متحدان عرب ما متقاعدند که ایران هنوز می‌تواند خسارت عظیمی به میدان‌های نفتی و زیرساخت‌های آنان وارد کند. ائتلاف‌ها ذاتاً کندتر از کارزارهای یکجانبه عمل می‌کنند. با این حال، ائتلاف‌ها در نهایت قدرتی به‌مراتب بیشتر را وارد میدان می‌کنند.
من نیز مانند همه دیگران از سرعت گفت‌وگوها با این دیکتاتوری سرخورده‌ام؛ اما پس از بررسی توازن قوا و گزینه‌های در دسترس ائتلاف از یک سو، و دیکتاتوری مذهبیِ ایران از سوی دیگر، آماده‌ام بگویم که رهبری ائتلافیِ رئیس‌جمهور ترامپ ــ چیزی که تقریباً هیچ‌یک از منتقدان او نمی‌خواهند به آن اذعان کنند ــ در آستانه دستیابی به یک پیروزی عظیم تاریخی است.
و اگر دیکتاتوری ایران در نهایت ثابت کند که به شکلی نومیدانه به موضعی انتحاری پایبند است، زمان کافی برای یک کارزار نظامی با قدرت و اثربخشی عظیم وجود خواهد داشت. در هر صورت، ما در آستانه یک پیروزی شگفت‌انگیز برای ارزش‌های خود و برای خاورمیانه‌ای امن‌تر قرار داریم.
NewtGingrich
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75792" target="_blank">📅 21:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEY5x19Brbib2g8GaSQE5PPAfv0ZMwdpo5ad5BlBq6DVicB2WS_4KUkmh_xCpilnwTTIpWlyMZjvceDDv_IKTKOVTfY2wsEVth9-1_4eDWvdsDYzc7z-cxmjh-Av-rdeKRlT2ke0XgqyJp2Dxb55a1axb-lKMx0ulqKL1aiR8B3wKp2O_uLOENu8m2lID19en918hUSNe-gXYBL9M5vZBLDauMAaDgeMP4xlFs1Kiwq-wN9qDR0XFc34Z4paHX5tW2iTx5iC_vXAdbAbNldbypEDx3p1ZPeLxbU5hy4lUHn2jEQerd5HqJEc5okWUDoic4x6J7ohmzYBH6IzTdXRvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی خانعلی‌زاده، عضو تیم رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت که در متن تفاهم احتمالی هشت بند از ۱۰ بند بیانیه شورای عالی امنیت ملی که به تایید مجتبی خامنه‌ای رسیده، رعایت نشده و زیر پا گذاشته شده است.
او افزود که تفاهم‌نامه کنونی برخلاف بیانیه آتش‌بس شورای عالی امنیت ملی است و مشخص شده که اساسا مذاکرات پسااسلام‌آباد، بر مبنای شروط رهبری انجام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75791" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ia82aWDpNR0pkdD6JPDJoh2gbH3Luggd_0i_Q2jzAGI_BaTs6lRAZqvTOnonqCq0Wkr8QbjqXkI3-TVZhaSGu7OsVqSNSep8DFmVL9JAuQIJEosHRSyqtQ5gE8rJ55jRNnbvunXQteiq3LL7jx6uGL-cl8FNJv160-eQVob5tRPPguRbiVB4kqNOd57ArnAjOGkALPgkmxyRhyszeKR0PIYpYXPMp3IOnNzzZXAxgTrl_ih85gM_zl8ZdrqlQEzpKDQixO30CsPfJhFbAuY5u1jIYAjgc7rnVbCu5wc-kcTDm5quABOjEHjCApksPIpbAIY1UoLZxdjXTxAH0dX53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه ایران در مصاحبه‌ای با صدا و سیما گفت که تبادل پیام‌ها ادامه دارد ولی هنوز هیچ توافقی نهایی نشده است و افزود که مدیریت تنگه هرمز باید توسط ایران و عمان تعیین شود.
او بار دیگر گفت: «در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد پرونده هسته‌ای هیچ مذاکره‌ای نداریم.»
این اظهارات در حالی از سوی ایران مطرح شده که آقای ترامپ فهرستی از خواسته‌هایی را که می‌گوید ایران باید برآورده کند، مطرح کرد که شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای، باز کردن تنگه هرمز بدون دریافت عوارض، مین‌روبی کامل این آبراه و خارج‌سازی ذخایر اورانیوم ‌غنی‌شده ایران با همکاری آمریکا و تحت نظارت آژانس و سپس از بین بردن این مواد است.
@
VahidHeadline
پیش‌تر: خبرگزاری فارس، نزدیک به سپاه پاسداران، نیز به نقل از یک منبع ایرانی دیگر اظهارنظر رئیس‌جمهور ایالات منحده دربارهٔ توافق احتمالی با ایران، را «آمیخته‌ای از راست و دروغ» خوانده است.
این منبع گفته که در متن توافق بندی درباره باز شدن تنگه هرمز بدون دریافت عوارض وجود ندارد و تفاهم بر سر نابودی دخایر اورانیوم ایران را نیز «بی‌اساس» دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75790" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5Sfnbo-J6rPvaXtcv3DO7wfWz3xvS8YFUId8Q51whbRKBoipbiHaTv5FJd5sPpUqLagtK9Ut-tYvB3EzsEHvJoN7W1iHgopjNOxu7j8QYDf28ZQuqAjhvSQ1p_u_P9fdWF_MHMQVhEsFIdw2NPyPpI3eYMpZZZzC79XMq2_2u8rH3veBI9MmkGnuDL0O9nVgEGwPrXs6oTiKTpksl38xwsKCUSqcfsMnJ22qcXlMEPpczipZwPbFx2Up01clf6xpFT5UU65cjNmbIYjmrSh0xemZPUJCuXS4PCmkEHxV85sQG2UMR1KwKcgztZsuRuO6093QbcdbTB5kLw41d4lSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
پست ترامپ، ترجمه ماشین:
ایران باید بپذیرد که هرگز سلاح یا بمب هسته‌ای نخواهد داشت.
تنگه هرمز باید فوراً، بدون عوارض، برای عبور و مرور آزادانه کشتی‌ها در هر دو جهت باز شود. همه مین‌های دریایی، اگر وجود داشته باشند، برچیده خواهند شد؛ ما با مین‌روب‌های زیرآبی فوق‌العاده خود، شمار زیادی از این مین‌ها را از طریق انفجار از بین برده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده‌ای را، که تعدادشان زیاد نخواهد بود، جمع‌آوری یا منفجر کند.
کشتی‌هایی که به‌دلیل محاصره دریایی شگفت‌انگیز و بی‌سابقه ما در تنگه گرفتار شده بودند ــ
❗️
محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدران، مادران و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده، که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده؛ در حالی که کوه‌هایی که عملاً بر اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فرو ریخته‌اند روی آن قرار دارند،
❗️
توسط ایالات متحده از زیر خاک بیرون آورده خواهد شد؛ کشوری که، طبق توافق، تنها کشور در کنار چین است که توان مکانیکی انجام چنین کاری را دارد.
این کار با هماهنگی و همکاری نزدیک با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و سپس این مواد نابود خواهد شد.
❗️
تا اطلاع ثانوی، هیچ پولی رد و بدل نخواهد شد.
درباره موارد دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
💥
اکنون در اتاق وضعیت جلسه خواهم داشت تا تصمیم نهایی را بگیرم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75789" target="_blank">📅 18:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=XShzhPHsLiQ3sFG_cZZJPu4PZiBdCFAEjj3p7Wc7V7zjgzv0_BE60BM8XycCIoTQTnU2_2u1lkYvYI8wRIBoQ8pQYmhRIERiAMkDolFT0fzl2QZ7qoXnqWWlrGHZ7GmZbImWvWF83wNYL17Af_f5juLzDW2n5q4-Fsqz67IS-390Lw-kmjxYTlpQr0RSiNS5_Pf6XNjyzyCCev8UcOkC48MFCv0j4ZgygcG4vfpzDLr6vEcgTQ25Wr1ipNv0nSPdeFgmzlspiPe0YQQSD7cuVT-7ZVglBY7yjfcFry9WBmaXEBnBrcDiygQQXgLT-q43eftd_k4-_2OQ5qr07yY9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=XShzhPHsLiQ3sFG_cZZJPu4PZiBdCFAEjj3p7Wc7V7zjgzv0_BE60BM8XycCIoTQTnU2_2u1lkYvYI8wRIBoQ8pQYmhRIERiAMkDolFT0fzl2QZ7qoXnqWWlrGHZ7GmZbImWvWF83wNYL17Af_f5juLzDW2n5q4-Fsqz67IS-390Lw-kmjxYTlpQr0RSiNS5_Pf6XNjyzyCCev8UcOkC48MFCv0j4ZgygcG4vfpzDLr6vEcgTQ25Wr1ipNv0nSPdeFgmzlspiPe0YQQSD7cuVT-7ZVglBY7yjfcFry9WBmaXEBnBrcDiygQQXgLT-q43eftd_k4-_2OQ5qr07yY9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با شرح عبور موشک‌های تاماهاک در مرز عراق و ایران در شبکه‌های اجتماعی و چند رسانه منتشر شده و گفته می‌شود مربوط به روزهای نخست جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75788" target="_blank">📅 17:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=jZnZKvUfoCig6YQeh-Zv3EYD29wJZ35SruzdRWgJ9Hs66XdYSVjN8cqVZn1hXJXJWrR4-yIHS72Yn-K9WArZOQd8ciNpQCz19BmXPZfIlxUwA_fCyfs880AFxGN8cIVotzG-qGwLrjC_3xa53NdCgQlQoLyDueu_WqnThYCZBYmxJXle15F2ObPq3uLNWdjDJ9NdUd0vgnUpvZsoysWeayOZjwFPsgeOmTKS0SDvzVeFmjUzNI4hU7THQ15yVq10bTMTOp0fU99F4oqlJpGTkDPi9W-MTsAhRoRXb2XAQ9sMzuKb7AWvUSfQsp-J-jVvtiDuiaZYZxvtP0uCXVKZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=jZnZKvUfoCig6YQeh-Zv3EYD29wJZ35SruzdRWgJ9Hs66XdYSVjN8cqVZn1hXJXJWrR4-yIHS72Yn-K9WArZOQd8ciNpQCz19BmXPZfIlxUwA_fCyfs880AFxGN8cIVotzG-qGwLrjC_3xa53NdCgQlQoLyDueu_WqnThYCZBYmxJXle15F2ObPq3uLNWdjDJ9NdUd0vgnUpvZsoysWeayOZjwFPsgeOmTKS0SDvzVeFmjUzNI4hU7THQ15yVq10bTMTOp0fU99F4oqlJpGTkDPi9W-MTsAhRoRXb2XAQ9sMzuKb7AWvUSfQsp-J-jVvtiDuiaZYZxvtP0uCXVKZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه هفتم خرداد ماه اعلام کرد عمان پس از دریافت هشدار واشنگتن درباره پیامدهای احتمالی مشارکت در طرح دریافت عوارض از کشتی‌های عبوری از تنگه هرمز، به آمریکا اطمینان داده است که برنامه‌ای برای اجرای چنین طرحی ندارد.
بسنت روز پنجشنبه در نشست خبری کاخ سفید گفت که صبح همان روز با سفیر عمان گفتگو کرده و از او شنیده است که مسقط هیچ برنامه‌ای برای دریافت عوارض در تنگه هرمز ندارد.
او افزود: «به او گفتم این موضوع از اساس غیرقابل قبول است و او نیز نمی‌خواهد افراد عمانی یا موسسات مالی عمانی را در معرض خطر تحریم قرار دهد.»
بسنت ساعاتی پیش‌تر در پیامی در شبکه اجتماعی ایکس هشدار داده بود که وزارت خزانه‌داری آمریکا هر فرد یا نهادی را که به‌صورت مستقیم یا غیرمستقیم در تسهیل دریافت عوارض در تنگه هرمز نقش داشته باشد، هدف تحریم قرار خواهد داد. او تصریح کرده بود که هر شریک احتمالی این طرح نیز با مجازات و تحریم روبه‌رو خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75787" target="_blank">📅 17:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwl-dhEkNPT89p7rlIzm8g0yqMPlK6BoYbq4y_3RBvDMsmo-MJLdMwKVZ5CxiXgk7dYZiFpu4TL3GI0OZ_Z-bbpi_Nrr4xVHv2ex5csu-JYkt5Gbg5hhEL4h-sCXDpB1HTwHRwdyGu_8st2FjX1jxUdOAtdxJjKTAgvUboQQEqQ8UzspGaciRUlnDD1Phmqvakfq-YKgkTbfCC2d8fbrBNal0Hlkss39DbUb62to48o4EqXQNw3ISTiFRzebFUIC7liy0G-dhGykm4fKal1xMgR1a-H6xWBWmx_GOYydKZ86C1NOOyWP9ufPzSDO9a0T3OsttdbZuo-t9Cn5Q4731g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
به گفته این منابع، بسیاری از نکات مرتبط با برنامه هسته‌ای جمهوری اسلامی در مذاکرات جاری حل‌وفصل شده است.
بر اساس این گزارش، جمهوری اسلامی با نظارت بین‌المللی بر تاسیسات هسته‌ای خود برای جلوگیری از تعطیل‌شدن آن‌ها موافقت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75786" target="_blank">📅 17:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YEiJ7NW9fyC_ru4DcFWdcovG4LNdaYbywnwa8QL1Ox4LVcsal5LKLqI7gcwQQ1JCpz0DMVhdVCRQ8eYyJE1efoX7VvEvQ88WXGrHXte1bvVnMyQkp8RRKdE24PvWfuAXidwrql00AdFtmlUoL950Jw99gWIEvMUQIni0gTjESIGcl8oOKlWeacC6WJpFdGOvOlv6Ar8x-3f8bgxKfLwbT6vJ-7cG5YLiZqG52zLc0xIZbZbfmqwZ7pCtZiNMXH48aGV6OesG-LB1HzCCkMRIA9uKrNTa632YYilhScUu_in2ndmnD4g0liBfTLhXWy8yOf21FFOQbY1kSVwrGPSCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی با آمریکا، روز جمعه تهدید کرد که تهران امتیازات مورد نظر خود در توافق پایان دادن به جنگ را با «موشک» می‌گیرد و پیش از اقدام واشینگتن درباره این توافق اقدامی نخواهد کرد.
او در شبکه ایکس همچنین نوشت: «هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است.»
این موضع‌گیری یک روز پس از آن انجام شد که چند رسانه غربی خبر دادند آمریکا و ایران به تفاهمی برای تمدید آتش‌بس و رفع محدودیت عبور و مرور کشتی‌ها در تنگه هرمز رسیده‌اند، اما این توافق منتظر تصمیم و امضای نهایی دونالد ترامپ، رئیس‌جمهور ایالات متحده است.
قالیباف در پیام خود اعلام کرده که «اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد».
از سوی دیگر، رسانه‌های نزدیک به سپاه پاسداران می‌گویند گزارش‌ها درباره توافق تهران و واشنگتن صحیح نیست. خبرگزاری تسنیم در این مورد به نقل از یک «منبع مطلع» نوشت: «متن توافق تا این لحظه جمع‌بندی نهایی نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75785" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV5kJZxBFx8MrVva0ckaqFaORnEnjrqs_6pkV7YQs5Ctm4H42fyEGeWH3QxgAY_MdAvZyoRw-kYFa32A8GxM70DCLgOGRUDV6eb6N-7kakX8Xn2_0W_9MaesjWq7aLW0jqYxrRffV2qVb7cscjdQpxizTVJBH-QAfVtnrd2ujp1TgW-dnwmWVcgigF5WAzyOdoIe9BwSBYeQX8ezBW3ITiem0ccxxGSwYy1NAag4CzzLJLiKN6R2Bd0Eu4KFMR4elict9toB2SoKztIV0xgkJV93mJIZd37b2TmCYRqcczdEShhQ6tw0PgtFmIDlRPOzFuOd1vhGUXOFPJWgOU6mQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از ابتدای سال جاری تاکنون، اجرای ۶۶۰ مورد اعدام توسط جمهوری اسلامی را مستند کرده است. با این حال، به دلیل ماهیت پنهان‌کاری و غیرشفاف بودن سیستم قضایی ایران، آمار واقعی به احتمال زیاد بسیار بیشتر از این رقم است.
‏
🔸
از زمان آغاز جنگ، آمار اعدام معترضان و افرادی که به جاسوسی و اتهامات مشابه علیه امنیت ملی متهم شده‌اند، با سرعتی نگران‌کننده افزایش یافته است. «اعترافات اجباری»  قربانیان، اصلی‌ترین «مدرک» مورد استفاده در این احکام مرگبار بوده است.
‏
🔸
این اعترافات در شرایطی کاملا مبهم و تحت فشارهای شدید جسمی و روحی اخذ می‌شوند. جمهوری اسلامی به طور مستمر این اعترافات اجباری را در رسانه‌های دولتی پخش می‌کند تا از آن به عنوان ابزاری برای توجیه اعدام‌ها و سرکوب مخالفت‌های عمومی استفاده کند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/75784" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoICUO11A_uxVD7J54vKsD8yqJJ_bu3byHOoJRbhBozMJ4IIz7tnMcR1GK6yGblPfzbhycdVOynu9n7WBn5PDwoG-rrKLnRb8mnXtBELiY9lThQjSsJ7ls8sAiycGB69WnDye9fayL396bU1Ua5NWYYvjBXvljtODkY521frx0lwSwB4E33ObbG6n39k2ArDi_42ikm8iVIvEiXy2x39fLPUJSiN6_RCj-fO1wm3FeKIXFuMCa6iOSOSBTlMlzHJfRl-IvbQqMzeeYZKOMW_78pXPixkTnlEbX8olELOuQZ0-D2P7zo4mUlH_9S5eeFOgQnAYoaA6mnk1_TV-r5BwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
شیخ تمیم بن حمد آل ثانی، امیر قطر، در تماسی تلفنی با دونالد ترامپ، رئیس جمهور آمریکا، در مورد تحولات منطقه‌ای گفتگو کرد.
دفتر امیر قطر در گزارشی از این مکالمه تلفنی اعلام کرد که شیخ تمیم بر اهمیت اولویت دادن به راه‌حل‌های دیپلماتیک و گفت‌وگو بین همه طرف‌ها به امید جلوگیری از تنش‌ها و تشدید بیشتر در خاورمیانه تأکید کرد.
در این بیانیه آمده است که ترامپ نیز به نوبه خود از نقش قطر در حمایت از تلاش‌های میانجیگری پاکستان بین واشنگتن و تهران قدردانی کرد و «از تلاش‌های قطر برای رفع اختلافات و ترویج کاهش تنش در منطقه» تمجید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75783" target="_blank">📅 02:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=QtX-7wwakAOyETghydkrQtI3gzUzby9OV7etiUsGt69-AseWj5oDuiNOJiqllhAaIh03Bo2NeGoohTKIshlTYmeuj9VgS_XNMe2K6sO4FatuzDT7qB39obXlmvSV4HGfb8AYMSB4i1ddj3lKHQLmf3ag-dFARGhxnBMF_TYh7hRdXkLhp_qpTlAy1fatv4v96z7SqbJoiKmpHiujnuXBoBhKRuuVEIN4kPP2E8b_9rveLA6IWQWekp6Zfb7C1sufWMISBWREyjRwqN02O2bycaYAEBsjyBJwzU3YlV5FHSgZZG7gk7AYlY5j_EUECjmuq_T7WQvs92fGejyylJ4rEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=QtX-7wwakAOyETghydkrQtI3gzUzby9OV7etiUsGt69-AseWj5oDuiNOJiqllhAaIh03Bo2NeGoohTKIshlTYmeuj9VgS_XNMe2K6sO4FatuzDT7qB39obXlmvSV4HGfb8AYMSB4i1ddj3lKHQLmf3ag-dFARGhxnBMF_TYh7hRdXkLhp_qpTlAy1fatv4v96z7SqbJoiKmpHiujnuXBoBhKRuuVEIN4kPP2E8b_9rveLA6IWQWekp6Zfb7C1sufWMISBWREyjRwqN02O2bycaYAEBsjyBJwzU3YlV5FHSgZZG7gk7AYlY5j_EUECjmuq_T7WQvs92fGejyylJ4rEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: جی‌دی ونس می‌گوید ایالات متحده در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «حداقل تا حالا با حسن نیت در حال مذاکره است.»
جی‌دی ونس: خب، فکر می‌کنم گفتن دقیق اینکه رئیس‌جمهور دقیقاً چه زمانی یا اصلاً  تفاهم‌نامه را امضا خواهد کرد، سخت است. ما در حال رفت‌وآمد بر سر چند نکتهٔ زبانی هستیم.
کاملاً واضح است که به نظر من، ایرانی‌ها — آنها یک معامله می‌خواهند. آنها می‌خواهند تنگهٔ هرمز را باز کنند. ما هم می‌خواهیم تنگهٔ هرمز را باز کنیم.
🔸
چند مسئله در مورد موضوع هسته‌ای وجود دارد: ذخیرهٔ اورانیوم غنی‌شدهٔ بالا و همچنین مسئلهٔ غنی‌سازی.
پس می‌دانید، ما با آنها در حال چانه‌زنی و رفت‌وآمد هستیم. ما واقعاً فکر می‌کنیم آنها حداقل تا حالا با حسن نیت مذاکره می‌کنند.
داریم پیشرفت می‌کنیم و امیدواریم به این پیشرفت ادامه دهیم تا رئیس‌جمهور در موقعیتی قرار بگیرد که بتواند توافق را تأیید کند.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/75782" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y70Ssyvrqu1yggJkSBu5dHcPX7oYYA-vNs1eeevVtQefu0G1y2T2waZrG_wr7JU80idITsIK2-finFrGhE-tiRyXIWsyY_58NMxxuK69_44FLr5GlxuaXT4k7jVLaQIBFM4BN3lTQ-h_pkDVhnxPTuDXTvBhpRRK8aQZ2ds0Z9wbMez2avFs0mWvaERDSVo-JS8VBCwqzacUBsFuIAgUgMFqLyxRi_fUtL1kMWMNlfszToBn18ZGuqD5TeFZbxzTpnYbj8YumDN4aGpVr0tSc4GH5hQNf9pVV45nx78DvaCKZHOryuTQwo2RGykMZBTvfLgs8ueqm-GXM4Fz00XtcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که نیروی دریایی سپاه شامگاه پنج‌شنبه در نزدیکی تنگه هرمز به ۴ «شناور خاطی» که قصد عبور بدون هماهنگی از تنگه هرمز را داشتند، «شلیک اخطار» کرده است.
همزمان، گزارش‌های منتشرشده در رسانه‌های اجتماعی از شنیده‌شدن صدای انفجار در هرمزگان و بوشهر حکایت دارد.
@
VahidOOnLine
ساعتی پیش پیامی دریافت کرده بودم که در پست قبلی نقلش کرده بودم و الان به اینجا منتقلش کردم. پیامی از شهروندی که درباره یکی از اعضای خانواده‌اش نوشته بود: الان قشم بود. پلاک موقت دادن بهشون گفتند فقط از جزیره خارج شید سریع
همزمان با خبر بالا هم پیام‌هایی داشتم:
صدای انفجارهایی در بندر عباس شنیده میشه.
صدای انفجار داره سمت قشم و دریا میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/75781" target="_blank">📅 23:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rf5jD_zBZm_23CCnpV4KN27NG60A9p50hF01cYrDZ9O_q8Shb3HlI4ukIEe8rDjYIsFTBgRtWN39dG1nlsOm4x6f4YVWYagssT2gJd3MHrQ0fVRlmYsBBklLvoWRDD_OKxuhEdP1ANGIFYdlTz2rMeV3O7ghDzvww2nCeurUNRryfQRMpG1F3h9-5D-IavXhDE_IpQ-9vs8FqyiXZ6uhM-NNT_eTpptBUpB_2qeeoLK5Rps5GK0MQ_HHeNUIBuyU0fvmb_z3_cs6c5yMmsWia2z4bWL40wYiTo436c2qkQFJRMqHfWaAc-iEU4i0bim8HHU0FqozAiUVPiqmEx2JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
#جم
در استان بوشهر
پیام‌های دریافتی درباره شنیده شدن صداهایی
:
▪️
همین االان 10/42دقیقه موشک از جم پرتاب شد
▪️
الان جم رو زدن...صدای انفجار زیاد ۲۲:۴۰
▪️
سلام آقا وحید
امشب ساعت ۱۰:۴۶ ۷ خرداد
بوشهر شهرستان جم نمیدونم صدای پرتاب موشک بود یا جنگنده ولی خونه ها لرزید
[معمولا این دو صدا با هم اشتباه گرفته میشن.]
▪️
درود بر وحید جان آنلاین از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
🔄
آپدیت:
مسعود تنگستانی، فرماندار جم، به خبرگزاری صدا و سیما گفت نیروهای مسلح جمهوری اسلامی «یک هواگرد» را در آسمان این شهرستان در استان بوشهر هدف قرار داده‌اند و اکنون وضعیت منطقه عادی است.
@
VahidOOnLine
یک مقام آمریکایی ادعای صداوسیمای جمهوری اسلامی درباره سرنگونی یک هواگرد آمریکا در استان بوشهر را رد کرد.
به گزارش رویترز، این مقام آمریکایی که نخواست نامش فاش شود، گفت هیچ هواگرد آمریکایی در نزدیکی بوشهر سرنگون نشده است.
@
VahidOOnLine
آپدیت: تصویر بالا
به صور رسمی هم از طریق
سنتکام
تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/75780" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql7YkGSTscpj82lgWHJI-gU-1bRQf-hNejASn8JFYcHg_E3lcRoL9IT6lkT7mej_RUtxBWfj5DtPt49dLihEZsVozVskbc3ADVJ9uBfkJAnfa7J07HvU8Q3uD0cW__csSxEOerptvV3NskgriovMVHLO4yu9jOnaM08bkTlsBZuAZ9ZnoroSEh8xAPaXca053sDEISWzXG0B4zD2dMp_oamrXXsiqZVHgYbsR38DF58OmB2H_Ab3RvcvCPYapxO4_wvUkQzTiSFInbcaVFDpHeoYpMIUCWMiT5JLiZ99nOTed1LzmA1Emi-eQqQLmUACM6I-MBuxTM7SKUYMG7LpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارگان خبری مجموعه فعالان حقوق بشر در ایران خبر داد که تارا و کیمیا داوودی، دو خواهر محبوس در زندان اوین، توسط شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی در مجموع به ۱۶ سال حبس محکوم شده‌اند.
براساس این گزارش، کیمیا داوودی به اتهاماتی از جمله «ارتباط با گروه‌ها و شبکه‌های معاند» و «اجتماع و تبانی علیه امنیت کشور» به ۱۰ سال زندان و تارا داوودی نیز به اتهاماتی شامل «اجتماع و تبانی علیه امنیت کشور» و «تبلیغ علیه نظام» به شش سال حبس محکوم شده است.
این دو خواهر در تاریخ ۲۴ دی‌ماه ۱۴۰۴ در جریان اعتراضات سراسری در تهران بازداشت شدند و هم‌اکنون در بند زنان زندان اوین نگهداری می‌شوند. به گفته منابع حقوق بشری، بازداشت آن‌ها با خشونت نیروهای امنیتی همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/75779" target="_blank">📅 19:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRI0Fzp0WBZpS-vJg7d4ubPCg14Hh97gaS08Y1kj3wNhKKqCQsQA6Lpp5ZaXUh5BVaMwgKoKXpmCbwvrD91UFWt8r_g8PCB9QzwUlUA2lQpE9n_YyKAJLRfGi3B4uiP5N-ZamhI8rCzvP8WRa14ZzGTLnOyHMy6OqgHhCROVW1kLFG_mFGoB0Dnqa33WwDGaDBhWRChQpq_Es-dU2j2A9ty3PZTw7NK66QU15uONEdb7ns2Ac5BajYGg520XtU9JRDHPU6s8rzDlQjeWEhja4k_Iw9oab6s3D2R6MJX44RTIiHeuDbawDmCko_RdDg5R2ONL0lu1yCBgx-5Y46cUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی گزارش داد که مذاکره‌کنندگان آمریکا و جمهوری اسلامی به یک یادداشت تفاهم با مدت ۶۰ روزه برای تمدید آتش‌بس و آغاز مذاکرات درباره برنامه هسته‌ای ایران رسیده‌اند، اما دونالد ترامپ، رییس‌جمهوری آمریکا، این متن را هنوز تایید نهایی نکرده است.
مقامات آمریکایی که نامشان فاش نشده به این رسانه گفتند که شرایط توافق تا سه‌شنبه تقریبا نهایی شده بود، اما هر دو طرف هنوز نیاز داشتند تایید مقامات ارشد خود را بگیرند.
مقامات آمریکایی افزودند که طرف ایرانی اعلام کرده که تاییدهای لازم را دریافت کرده و آماده امضا است.
تهران هنوز این موضوع را تایید نکرده است.
اکسیوس نوشت مذاکره‌کنندگان آمریکایی جزئیات توافق نهایی را به ترامپ گزارش دادند و او درخواست کرد چند روز برای فکر کردن زمان داشته باشد.
@
VahidOOnLine
بعدا
فاکس‌نیوز
هم خبر مشابهی منتشر کرد.
و گویا به همین دلیل هم می‌خواستند اینترنت را باز کنند. پیروزی جلوه دادن با اعلام جشن و پروپاگاندا در جو جام‌جهانی و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75778" target="_blank">📅 19:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kVieke46tzoBykJMSaTz99ZrGTWHLux-yg0fB8lkkyyx-Z_RRrvWsNoYi_1EuxFqSmOeChQz4ve5gW9NlH6YtdteBh3G1_RapNfkWKdVvsXMS3ZjXoyuU16sWpviv_O-c3zdchrfMKw0dlgtZfDIuOnnmjCoQOsoXXL68P0YQJwpQiQEMpyAWgdKqE-CQweYlZsL9rCsheCesZVUG9TRnyYM0ZVm08pv61cQ-CBjbnRlN5eWG1p-kHEyESTYO-5JdOjnuQnQ83BR0DjEOMHHd6FhzJ-ZLKNtH6GyCRioNUaR9j5U3Iy0BOxLUo2NgfOhiAVuPlr9hWT3J8o-sZzM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PPa8R_rHVVG3-bZT-f4Y0titQaG0ejbHkUe1lrjiagt0M4Oosys4tg9GND5sf4e4xNvIoSMBBxxjps48w_b3iHlMXechKljD-RnhD-TFjs5diwqAHDmmmtnWiSIfKlNntreFakWtb8WJEOgZ639Uye6XN3AHjsoaenxBJs8FGWB_Ytgmk3rG9ZQLURF752S3CQsIysnfhXJgCn1hI1N2HeY-qpswGZX6lQP8Vv9W0pFotf5qWfwAZdo4_sFyFO97iRVVkNXsdA7YdBe7JRdMUcXeS1zFShuYuldGes5-vi3i_e0xwr-a4vErQ97PLSjRhSWOjD_sis7oToR1gMXWHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس از انتشار پیامی منسوب به مجتبی خامنه‌ای درباره «نابودی اسرائیل تا ۱۵ سال آینده»، رسانه‌های ایران تصویری از دیوارنگاره جدید در میدان فلسطین تهران منتشر کردند که بر آن جمله «اسرائیل ۱۵ سال آینده را نخواهد دید» نوشته شده است.
در پیام منتسب به مجتبی خامنه‌ای که رسانه‌های ایران آن را منتشر کرده بودند، آمده است اسرائیل «به مراحل پایانی عمر منحوس خود نزدیک شده است.» در این پیام به سخنان علی خامنه‌ای در سال ۱۳۹۴ اشاره شده و تاکید شده است که اسرائیل «۲۵ سال بعد از آن تاریخ را نخواهد دید.»
@
VahidOOnLine
سپاه پاسداران روز پنجشنبه هفتم خردادماه با انتشار بیانیه‌ای به مناسبت کشته شدن محمد عوده  و عزالدین حداد، دو فرمانده حماس اعلام کرد منطقه جز با محو اسرائیل روی آرامش نمی‌بیند.
سپاه در این بیانیه از حمایت جمهوری اسلامی از «محور مقاومت» تاکید کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75776" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vndgBE6shyAgx2TbvPvtI4G2OsumbeQ9rB9d0LOv-Saoh9UUaLTo4ylctA1jnVdEp9FTrpQsoRuhAKHQHk19Kvdagd0Zz5N_oUdjkhxO2A1E3rupZuWDvegzAmL6SbGljNrSa6fw4R6MG_aT7icCNSyxx8VADmZB3Bb2veenXz2EwuAq6hzFR2zVs7GS-MCTloQz6fAtz6ESwARu_Db69LpgVAwBsIQ_FEzrWcZ2oz3sMqVD5h1-VMnGUbc7_EOXr2qSMHJwfohpnwQ8RFKewdsHN9mvM2T7WpjKGybVo6vSABo1kX6VjDiZO305oo3KCuOYEtj4EbeCLe4N5cYryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pMOAPjAC2GOj87MAZGbddvSHcWgDfsosvqfeL9LYf3GqUD4OE40yw5j7GULop_4AawCc3LT368B4xdDiW8wZsYPZIyC8kF65rekuBg_dz1X5Ryx8jZRmMhwemsjSO9cqwVRd6-xWHViXZypgA02TYP1d2jH5gY7-kBCfT-X9ol7WCUw2c1AiTkXwtWn2rL3sA1LRAMGYyIbKVhU78MuEZLeQ-RbLmO2jzME6N41hrL4p6q1Wx9dauS20VEOP5-5dYxqkCZu0Kv9uN6b56NaGMQSm2ZR3ITvC6NYTaPciGL25uBSgI98CZHnJaqpBgedWUHjpNCHcYNtWU1z2rMrGTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنج‌شنبه در پیامی در شبکه ایکس نوشت که ایالات متحده در راستای افزایش فشار بر تهران و باز نگه داشتن تنگه هرمز «دسترسی هر دو شرکت هواپیمایی ایرانی به اماکن فرود، سوخت‌گیری و فروش بلیت را متوقف خواهد کرد»، اما جزئیات بیشتری ارائه نداد و به نام دو شرکت اشاره نکرد.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، با تاکید بر اینکه این کشور به کارزار «خشم اقتصادی» علیه حکومت ایران ادامه می‌دهد، در شبکه ایکس نوشت نیروهای جمهوری اسلامی حقوق دریافت نمی‌کنند، پلیس‌ها سر کار حاضر نمی‌شوند و جزیره خارک تعطیل شده است و اقتصاد و ارزش پول ایران در سقوط آزاد قرار دارد.
او افزود سازمان مدیریت تنگه هرمز از سوی جمهوری اسلامی یک شوخی است و امروز وزارت خزانه‌داری آن را تحریم کرده است. ما به هر نهاد شرکتی یا دولتی درباره پرداخت عوارض یا پنهان کردن آن به‌عنوان کمک هشدار داده‌ایم.
بسنت اضافه کرد با تشکیل «دیوار فولادی»، محاصره دریایی آمریکا باعث شده میزان نفت خام ایران در دریا به پایین‌ترین سطح تاریخی برسد.
او تاکید کرد تنها یک نتیجه رضایت‌بخش در مذاکرات این روند نزولی را متوقف خواهد کرد.
@
VahidOOnLine
دولت دونالد ترامپ نهاد موسوم به «سازمان تنگه خلیج فارس» جمهوری اسلامی را تحریم کرد
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75774" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aKtqMgBc37GxYsxZs2SjNv5GAjEgFePRJ1P9_zGykInjxu_Ud3ydXYw8O6kKDwTzhvNaeoYn44Sbj2hy1cj851q2L_pczDGcDXSiaRXel2F6a9GTxcwJ06yCDLvnSMU9lw_AOzb7pykOoJIHzdmDi-U4SEPlrJhofyuPv2mY4khktFM8BXs-o68ohIZ3f8AU2cxCc25l3OHTbi73ibl-z67zSGcmHlmRB0CMMcCYNSfpka7VuiiYMr0wdOkMgpkjAtUa9Hup1yvr4VZ7fRZj8K7VFrpbzjOOGrg9nMK0o1X3mpu2cumVwvm4Ezegzig8FEVxtZus7Mb2SvBpXxeD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZdO5EmNrUOvDcE1to_cPvznSO-l19TBpoQtkJ460oPSgMJQgVcU2yC0CbYiaWHc6a_L2pf_O_pTEOuPpUU0ukVIeFCcDqn-p4P2NOlecfcXTJ7yaRocXEbWMdL0Gn9kEE31i-mCmSy4EJWy6UXFonKjvBeOAg2htenPkmHvyIeZhKgQPcYMUH6-YzPNP69ZM9r1g90ucApWe4asrYP6app7QdNu2AKQIFnm9-ys0KXKLw1jVFH_SOkpHzzg-ODm0iSoAQUMwr43H0se8KUGBsQ_xPF4fh9Xqoo_hIVOf-b5G9ZkP-6NTKz6aXjvSa_L-bXfCmMmHxWsWrLVihuvcNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خارجه کویت حملات اخیر موشکی و پهپادی رژیم ایران به خاک کویت را به عنوان یک تشدید تنش جدی و نقض آشکار حاکمیت و امنیت محکوم کرد.
این وزارتخانه روز پنج‌شنبه اعلام کرد که تهران را کاملاً مسئول حملات اخیر می‌داند و حکومت ایران خواست فوراً و بدون قید و شرط حملات را متوقف کند.
@
VahidHeadline
اسماعیل بقائی سخنگوی وزارت خارجه ایران، حمله بامداد پنج‌شنبه آمریکا به مناطقی در بندرعباس، را «تجاوز» نامید و آن را محکوم کرد.
آقای بقائی این حمله را «نقض فاحش حقوق بین‌الملل و منشور ملل متحد» دانست و افزود: «شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخگو کردن متجاوزان آمریکایی است.»
سخنگوی وزارت خارجه ایران می‌گوید آمریکا «به‌طور مستمر»، آتش‌بس میان دو کشور را که از ۱۹ فروردین اجرایی شده، «نقض» می‌کند.
سنتکام با این حال تأکید کرده که این اقدامات «سنجیده، صرفاً دفاعی و با هدف حفظ آتش‌بس» انجام شد. این دومین بار در سه روز گذشته بود که آمریکا اهدافی را در ایران هدف حمله قرار داد.
@
VahidHeadline
فرماندهی مرکزی ارتش ایالات متحده، سنتکام، حمله موشکی ایران به کویت را «نفض فاحش» آتش‌بس خوانده است.
این نهاد در حساب رسمی خود در شبکه ایکس نوشته است: «ساعت ۱۰:۱۷ شب به وقت شرق آمریکا در تاریخ ۲۷ مه، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.»
سنتکام نوشته است «این نقض فاحش آتش‌بس توسط رژیم ایران، ساعاتی پس از آن رخ داد که نیروهای ایرانی پنج پهپاد تهاجمی یک‌طرفه را شلیک کردند که تهدیدی آشکار در تنگه هرمز و نزدیکی آن ایجاد کردند.»
فرماندهی مرکزی ارتش آمریکا می‌گوید: «تمام پهپادها با موفقیت توسط نیروهای آمریکایی رهگیری شدند و آنها همچنین از پرتاب ششمین پهپاد از یک سایت کنترل زمینی ایران در بندرعباس جلوگیری کردند.»
سنتکام در ادامه آورده است: «فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای کماکان هوشیار و محتاط هستند و ما همچنان به دفاع از نیروها و منافع خود در برابر تجاوز توجیه‌ناپذیر ایران ادامه می‌دهیم.»
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای در شبکه ایکس، حملات خصمانه با موشک و پهپاد به کویت را به‌شدت محکوم و تقبیح کرد.
@
VahidOOnLine
وزارت خارجه قطر در بیانیه‌ای هدف قرار گرفتن کویت با موشک و پهپاد را به‌شدت محکوم کرد و آن را «نقض آشکار حاکمیت» این کشور و «نقض فاحش قوانین بین‌المللی» دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75772" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hggd548u7Y9SonYhdsRVGhrgQKYgILWyn0zEo_Nc1psN8EUrx582eLyzxcrjxpKYUBUyDxlHRDMuWamtWoX2Cg-mtvNItbwV-JBrSXouifMNxux7kbqp84_4sZ4xMNSks8UYOexmO4KxfZy9FCd0uIPglPFedCubIFkP1TcpJ1bCyOnVUgHhyN2i6NJXied8jTGc_NslMe5tfYOYVQRKxh0CK-ES3VZVt_pU0bh0wS57o9ZS27NyaTRge121-gLR1GBXUHphrDIojSC8v61YPFx8KNExfsGRo9pEzv669YyslqYD0zBEd__PzW1ZkFjQI6A_hvPIjRJYXoTbf2WQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را خطاب به نمایندگان مجلس شورای اسلامی منتشر کردند که در آن می‌گوید «ایجاد تفرقه و تجزیه اجتماعی»، در کنار جنگ و فشار اقتصادی و محاصره، «طرح و نقشهٔ کور دشمن» است.
مجتبی خامنه‌ای در این پیام که روز پنجشنبه هفتم خرداد منتشر شد، همچنین به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داد که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
وزارت اطلاعات جمهوری اسلامی روز گذشته در بیانیه‌ای هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
وال‌استریت جورنال نیز روز پنجشنبه در گزارشی به نقل از تحلیلگران هشدار داد که ادامهٔ محاصرهٔ دریایی آمریکا علیه ایران که به کاهش ذخایر ارزی ایران انجامیده، می‌تواند احتمال بروز اعتراضات جدید در ایران را افزایش دهد.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75771" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWXbuZ1bnPG9fO0HabhvxN2L2SmwvBx3k-pSBHlK_c9y8FWp8u_2-alCQM7nBuT2XGNnsQ2GhQKS-_9s1tB-QuZt5BgbTINvXTGcliqoVqZV66vOLwVNinnOuj9WoaIHN0yyy76572R3I4EwZHs1u9jLw9hkqYTexTibAVUcxeZJIPvPeQWRiERPFzC7_mnX2_JASCoQDNoVYv1mUiWoVXwd_h197gWgPX3SLQmLhdpKzSfDw8pTndVA-yN9XgbuuT3-K9et9C36fF_zm5Uc_4kY-fSmBXvbSYkQbiAA3dU3ccpEN7ddqWwKMpvQrgdnauL1-_Lq3CVCVrSQjiLPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری آمریکا اعلام کرد «جاناتان لودهولت»، شهروند آمریکایی ساکن استاتن آیلند، به‌دلیل مشارکت در طرح «تعقیب و قتل» مسیح علی‌نژاد، فعال سیاسی ایرانی-آمریکایی، به ۱۰ سال زندان و سه سال آزادی تحت نظارت محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75770" target="_blank">📅 18:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYb_uaIkd3W1-oBAVJcSuRed6WnupMMz1UO8YF0xSvBKtxe7j2Ne9sv0yA1TjPgHJf4lREfijNaHTI2M_xq5vga4Q4gYZpR7WYyOwDHB9e_Ymj0xwOocA-6O5ZCmTiXvA80P2erj8o64UicObGlKvgXHZU8MBbMY_0ESZWvkm8xAHTKnAugTmzGV-83ebBB3nsll_xovrGeRaqUhTXgiGZNrQrfgg4atrAoFJGVLV1iHWHg0WauLvyhlyABISx2TWIgxNXA3kQO7vsN_2eevgP3zsceufty6UkrtuTeqrFyl1QgsO-3ORMr8wUCru13w_6XN8pnMTDow-F0JzniGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، در پیامی به «غلامحسین محسنی اژه‌ای»، رییس قوه قضاییه نوشت: «قوه قضاییه زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد با قاتلان داخلی و خائنین به ملت نکشید و خوش درخشید.»
این تمجید از عملکرد قوه قضاییه درحالی صورت گرفته که در طول روزهایی که از جنگ ایران با آمریکا و اسراییل می‌گذرد دستکم ۳۹زندانی سیاسی اعدام شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75769" target="_blank">📅 18:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht0Ruz7PURume42ut612SSzgT2OvxlkFXPrBSfjompQWhC1j1YekdJhBLecGftG1RryJkpt2lSB2NN9KlHgPYg-2knvMZSAYsRDwDHMd4VRt13bI7DoT4GDsg56Ized2dq0raVYKbVMx-4Gcdr62Xc8EzG-KgYQ2-Guswk0HbFmuOxNMALZHfEsGfjmC3PLAY4kTsuyyDWEai_nAjnJMLEkoCJFbaTx_Bgc1bx8vZHGGCjmfZOdsvalSC3tplkL8YdjFTtWdFVEuc97oYYSDRSCBAXQ1j6iz8VzCikJxN2xGFjIzTofcqLTK83lQP-nlqOT_Avn3hRJte6VKAQk_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس، نهاد ناظر بر اختلالات اینترنتی، اعلام کرد که علیرغم اینکه دسترسی به شبکه جهانی تا حد زیادی در ایران بازگشته است، اما شاخص‌ها نشان می‌دهند که کاربران همچنان با فیلترینگ شدید مواجه هستند.
نت‌بلاکس، این فیلترینگ شدید را مشابه دوره مابین اعتراضات سراسری دی ماه و آغاز عملیات نظامی علیه جمهوری اسلامی، حدفاصل دی ماه تا اسفند ۱۴۰۴ توصیف کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75768" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4I5_d2NQ0LiGOlf1sMZepYltOQdfmxDjGHGaAtDhsfGDqFpnNJFEW0ap9B7dLiNGYN7xcWhoURkKaNN8SslKeqNrfg3Z8U4Js3jZ6dZs9YMUYbCcvN2k0lttEoziK3eogaT350Ro7IR245FjndoxZDm7ECwm7FnQgqSDA4qMjef8iKvcn2sm0i5tczSBc8DzHkhx-eafN6lIL2w78tYkKW4IGt85i20CtVougXA8HfZW3lf4eA-bSZmkBUZKhssiv6W9Eq0Y6B_q59xIykq4OANANEHuoDiLwenyYjA1I0abdfSIInOfUOp3DNMkT-IrFf_FwfCapXp59UDKi08gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر پیکرهای بی‌جان و شیون مادر  تصاویر دریافتی از: 'بیمارستان الغدیر #تهران، بامداد جمعه ۱۹ دی' Vahid #بیمارسان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75767" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=e_DlUQUWOL8dQBxW5tGgEiLW1fAO5FBc1fFXj4r4Jl212BH60wiy8nZMpa7d8LbH5z4MIHKLsPX1eEruphsRPmhJBbXvC07VMSeQk2JuCRCXtUWz8gJsToIyYSnDINXuLzS76mVpDvmuAw1PP9T8fHVNuuBm3Mx_GpXjVL4Dek_tnBPdJiqNb_YR8xORxbKMya2sRbXiVrxPwfQiFvcoP_3_F-UXnSazmsGpOEszvMHbE0PLufP2DbcQTDopiegkYl833ja0deQrQ1amNSKfon2Yg_ak7GozM3r99Moq9Zm5k_PXj9w0yaBrxIgLntDK3O4PybnwuBUpvN6Mhpjq4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=e_DlUQUWOL8dQBxW5tGgEiLW1fAO5FBc1fFXj4r4Jl212BH60wiy8nZMpa7d8LbH5z4MIHKLsPX1eEruphsRPmhJBbXvC07VMSeQk2JuCRCXtUWz8gJsToIyYSnDINXuLzS76mVpDvmuAw1PP9T8fHVNuuBm3Mx_GpXjVL4Dek_tnBPdJiqNb_YR8xORxbKMya2sRbXiVrxPwfQiFvcoP_3_F-UXnSazmsGpOEszvMHbE0PLufP2DbcQTDopiegkYl833ja0deQrQ1amNSKfon2Yg_ak7GozM3r99Moq9Zm5k_PXj9w0yaBrxIgLntDK3O4PybnwuBUpvN6Mhpjq4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'رد موشک شلیک شده در آسمان
#امیدیه
خوزستان، پنج‌شنبه ۷ خرداد'
Vahid
☄️
سپاه اعلام کرد در واکنش به حمله‌های پرتابه‌های هوایی آمریکا در سحرگاه پنج‌شنبه به نقطه‌ای در حاشیه فرودگاه بندرعباس، یک پایگاه هوایی آمریکا را که مبدا این حملات بود در ساعت ۴:۵۰ هدف قرار داده است.
سپاه تاکید کرد در صورت تکرار حمله‌های آمریکا، پاسخ جمهوری اسلامی «قاطع‌تر» خواهد بود.
@
VahidOOnLine
رسانه‌هایی که بیانیه سپاه رو نقل کردند، از جمله خبرگزاری رسمی جمهوری اسلامی، ایرنا، نوشتند "ساعت ۴/۵۰" حمله کردند که یعنی چهار و نیم ولی با توجه به اینکه با دو رقم اعشار نوشتند احتمالا منظورشون چهار و پنجاه دقیقه بوده.
اما این هم عجیبه چون آژیر در کویت و پیام‌ها از امیدیه مربوط به ساعت ۵:۵۰ بودند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/75766" target="_blank">📅 06:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/raN9XqLH6Ct1QC3HmUgnj6wsnj0u1Xz1vHM-MWXp0TKqUke2_WwjcIqVvWSjt-OvgVJwVxlZCdmyoPdl7x8oNQPYpzJvYpFkpPrI5Itas-4pLQJT2V1G5oRy9Oez3nmZHJpeneDPJsHHaQYGIZA5_rJ75KRrqVcwVED7Fg6eYXeCA76NcVuVlXbqFubQKhVVrdjV1A9ziRghm_cJSxruPnV9DhkQdGIDqxTRJ0pwsk8DoqtsOGn-MP9_Uk4wq3YYJk8EILtKFnBlnELEiYO5E9d9z1b9o6F4_8lfHWSu4S04armX2NipgV1RkA0J3-r4DZLwAaIbwJbyjffcqfBxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p0yzeHZVZMnPQt-EMjNu7RpA0ZKwnv6cK9ZMN3TBLkaFPa8oBZiy1B9QKOQ1vNTKWVRlSZdIP9XrsZGLE7bwupok9kDCXevs5DS-7oJHY94bL4ZTwery-Xt38mbZnGJqMrrPginaEJLzLE4rbjnajoXwmMD1k7UVzaQPhq4-QBjT9G5-UIhsK_ptHeGcr6m8ZkWxPlp7osOI1ren7KzrWjfQhLsHUwQ2hFOJ3Qe2_UYbzDxDe2-P2YRFA8KmlLNK9BmBSXzt1MMh_kQyMIoyWbx5c_IeQVg2pHTm0OA4VK8bb_Iy6JfjxVaHYZ-xybhxaLa5OYVSyF_BiLasgXTgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NApTAPHJGF55-X0GpOw_c3MErrCIvWuATfRbxa6MvwV5QpiA4EuOC9_4WEPOu6YAtzZMWBb00pNEI3VvOGB5jPTznCGt-hQYgtuK18g6mIQJb2gF0ESgIqeLQLbJdi-CXUbJdxuO5oXVDn1wgwRzqFxh6zOcNDWCmUvb1w71qNry1UnLaPIY-0ZvY2PzknVLfIuBiNnATIIbQntYCQ2H2fQMfoQdGDCG8VK_jKM9pBBJAxighCxz-hM5o-n3GAcZZQaw6Di_PmLqdnsXQfrCEQpxUVn-KYQS1r782Wh7tBx9OpEIWsxb28LytGSpaDUtptgJMUfsN10BlznktwAkSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از
#امیدیه
در خوزستان پیام‌ها و تصاویری دریافت می‌کنم  که میگن حدود ساعت ۵:۵۰ موشکی شلیک شده و سمت تونل امیدیه میانکوه صدای انفجاری شنیده شده.
یکی نوشته لانچر هدف گرفته شده.
دقیقا میشه هم‌زمان با
شنیده شدن آژیر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/75763" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFi09MP2ALvQo0XCWlaf_HwJgOqSEqR01TAAt33ERhecKn8Z7A8UsWWFaakQe-r_fuPK-hDdNWKgIOYtz14HyJIP_6QNCVTVW-RqE_g_FfSC8CuwNMWPP8gEereiK1lX8pZewvHNrnj7SlJnR6tJMqI9WqOeXxrB-kP9zbHupfSyHPo0E0pcFbv4Lz9RMxXItTyLTnnxvdSiscQE95nSb-5op_9u68oc5Cwj2Gv6Hz-VM3cKOeg_WwlzeS-V3tZz0JYbewcbcj8cPCyGT45BPloXetp4n_1pVym2Q3TnfzfGkp-wlugJirotBKwMxpOFBk7JVHb-v5wdgoVmwdyOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید الان کویت رو زد ۵/۲۰
وحيد همين الان اژير كويت فعال شد
سلام صدای پدافند و تقریبا ۲ تا انفجار در کویت
درود وحید
🙋🏻‍♂️
اینجا ساعت ۵:۲۰ به وقت کویت صدای اژیر اومد و رو گوشی ها هشدار اومد
ولی هنوز هیچ رسانه‌ی کویتیی دلیل این اتفاقو نگفته
آپدیت:
ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور حملات موشکی و پهپادی «متخاصم» را رهگیری کرده‌اند، اما مشخص نکرد این تهدیدها از کجا منشأ گرفته‌اند.
ارتش کویت در بیانیه‌ای اعلام کرد صداهای انفجاری که در کشور شنیده شده است، ناشی از رهگیری این تهدیدها توسط سامانه‌های دفاع هوایی بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75762" target="_blank">📅 05:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3e4Zh2HZE5_3PMkBguj9K976EWEUPrgHr7N2XFtBALE-VC5_2T3_Nd5w1T2HnCIEZV9uzk5pufWSaqVFCM_MGXb-yoOMjg0EPiFN3bfn3DF8l1ajjrOaD5WvT6O9O3N8mddjX4A80resCguqZ4jUT71rNRZ9mK2hETLEGL6frKZNv8Mox_CONyyxEY4hjZ6YHaikmrz24wCfysqEY6mvDaqN_3NNBErIAz73GBP8_tmRCCuThFBtEX1Lxhr3J5dW5uc7h0aqXXGVxX5mSYNEe12XtgB6f8YyGmvGRV9zPN2RvMTWemVFPv5IouQ9lYbMy71oKJd8r-W6xda5v0wog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسوشیتدپرس به نقل از مقامات آمریکایی گزارش داد که نیروهای فرماندهی مرکزی آمریکا چهار پهپاد تهاجمی یک‌طرفه ایران را که در نزدیکی تنگه هرمز تهدیدی ایجاد کرده بودند سرنگون کردند و یک ایستگاه کنترل زمینی را در بندر عباس هدف گرفتند که در آستانه پرتاب پنجمین پهپاد بود.
@
VahidOOnLine
در همین حال، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، به نقل از یک منبع آگاه نوشت: «ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.»
تسنیم درباره حمله هوایی آمریکا به نقاطی در شرق بندرعباس نوشته نیروهای آمریکایی «به زمین سوخته‌ای در اطراف بندرعباس شلیک کرد که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/75761" target="_blank">📅 03:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی:
چهار تا صدای انفجار پشت سر هم اومد الان
ساعت ۱:۳۳ بندرعباس
درود آقا وحید همین الان سه تا صدای انفجار اومد تو بندرعباس ساعت ۱:۳۳ دقیقه
حاجی صدای انفجار دوباره شرق بندرعباس همین حالا  سه تا پشت سر هم ساعت1/43 دقیقه
سلام وحید
۰۱:۳۳ شب
همین الان بندرعباس صدای ۳ تا انفجار اومد
سمت بهشت بندر
احتمالا باز مثل سری قبل باند فرودگاهه
بندرعباس ساعت ۱:۳۰ هفتم خرداد صدای جنگنده بعدش سه تا صدا انفجار اومد
سه تا انفجار بندرعباس
ساعت 1 و 33 دقیقه بامداد پنجشنبه 7 خرداد صدای سه تا انفجار رو از بندر عباس کس دیگه ای هم گزارش کرده ؟
شبیه صدای موشک زمین به هوا بود
بندرعباس صدا اومد
سه بار
درود. ساعت ۱:۳۲ دقیقه صدای سه انفجار شدید در بندرعباس اومد و خونه شدید لرزید.
ساعت ۱:۴۷ باز هم صدای دو انفجار دیگه اومد
صدای سه انفجار بندرعباس همین الان
سلام وحید جان بندرعباس چند انفجار وحشتناک پنجره خونه لرزید 1.38
دباره زدن بندرعباس ساعت 1.49
۳تا صدای انفجار بعد صدای پدافند
سه انفجار پشت سر هم و یکی هم ده دقیقه بعدش بندرعباس رخ داده
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/75760" target="_blank">📅 01:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PBU8sSO5omsyCmqC3z8fU4-DSdnfMW2Dm_CY4s0_xyoS_fK7kRklimDCZgXNYgDN1XTcSI4bZvRADgMalh7yqaYZhOWFlYkoy3H43KshFHC_hJfnmca0wdbdmf7ZA69qQtINJ5eEa2SHeRQxuFmOnCpPf1GefwNphyHlMGBEX_HOATVTYued34_WgPlJtxgm70K_8cnFht8oVuszZd_Z7y4CDAWFqG-NtrBstzbf1HLtOJSc_SLviyoQWJHlyWiUXm6Yfzb6wHJwC-KkPlq-baLp84v2yR5gNEo1ixfHYKLKgYwUPdv61DBqHDKszFI7tFi65SsxaOKiNEVBxjGLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=X884LWimOegcAg6XReS8Qvrm80POFmun-hTG8TYMBSghTdw-6g_X5wxDV-028nf7ummyqw7ioOnIpCjCRFIheok7yMlfVhtynEkVZ6FnWrLZNzoLWh_FdfV7hLtz9GkLmBR7yVYGsYEOpg7O-n3AsTsV8HgO5DID3o2wLd7PDAb5eWcNBZ9c0urFqax14EgEoacor28cU-FSW1M2t_m8TtGmBa0iIglzRLRBwchGJaxhbmIgpGrJTysF9x88JvZiVwQfo_81EV9J91humAH0LT3OSfnG4vM7_x3-Kr0q-JajnPoYI9GFy2XCAiH3v7fW0uSZ7PTQe6s9nkVSmYyUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=X884LWimOegcAg6XReS8Qvrm80POFmun-hTG8TYMBSghTdw-6g_X5wxDV-028nf7ummyqw7ioOnIpCjCRFIheok7yMlfVhtynEkVZ6FnWrLZNzoLWh_FdfV7hLtz9GkLmBR7yVYGsYEOpg7O-n3AsTsV8HgO5DID3o2wLd7PDAb5eWcNBZ9c0urFqax14EgEoacor28cU-FSW1M2t_m8TtGmBa0iIglzRLRBwchGJaxhbmIgpGrJTysF9x88JvZiVwQfo_81EV9J91humAH0LT3OSfnG4vM7_x3-Kr0q-JajnPoYI9GFy2XCAiH3v7fW0uSZ7PTQe6s9nkVSmYyUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره لغو یا کاهش تحریم‌های جمهوری اسلامی گفت واشینگتن «درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول» صحبت نمی‌کند و تاکید کرد: «هیچ تحریمی، هیچ پولی، هیچ چیزی.»
او افزود آمریکا کنترل پولی را که جمهوری اسلامی ادعا می‌کند متعلق به خود است در اختیار دارد و این کنترل را حفظ خواهد کرد. ترامپ گفت زمانی که جمهوری اسلامی «رفتار درستی» داشته باشد و «کار درست را انجام دهد»، اجازه دسترسی به این پول داده خواهد شد، اما «در حال حاضر چنین کاری انجام نمی‌دهیم» و «این دو موضوع به هم وابسته نیستند.»
ترامپ همچنین درباره انتقال اورانیوم غنی‌شده گفت با انتقال ذخایر اورانیوم غنی‌شده ایران به روسیه یا چین موافق نیست.
@
VahidOOnLine
دونالد ترامپ در پاسخ به سوالی درباره کنترل تنگه هرمز توسط تهران و عمان گفت این تنگه برای همه باز خواهد بود و آب‌های بین‌المللی محسوب می‌شود. او تاکید کرد هیچ‌کس آن را کنترل نخواهد کرد و آمریکا بر آن نظارت خواهد داشت.
ترامپ افزود کنترل تنگه بخشی از مذاکرات است و ایران تمایل دارد آن را در اختیار بگیرد، اما چنین اتفاقی نخواهد افتاد. او درباره عمان نیز گفت این کشور مانند دیگران رفتار خواهد کرد و در غیر این صورت آمریکا مجبور خواهد شد آن‌ها را منفجر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/75758" target="_blank">📅 21:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M3JJvS5juX7gZsRwh2jaQq9uSV_yPlFJPqnXRwhLBuwL1IjfwrU0CcObwBhpNsbpHdatye-47T0V_qkG0HdLADJfzWtBSIp3dYzrkWh28UhKMqpvBQ8d1XGGus2XnAr-W2P2qmtMW-3BLrKuA1b-uFyPSK4Q1KKCT1PLbBwoMokFzNstxVLmwzMbFDdzwMzv5AnD7yCJ0vKXWM9aGz4cJxWtF5PP2zBgP8JfD1iLHTgo-3cq4QRdO_nCmfw9mBTRLM-Y7W8iBl-z5ecNTJ2x65ouvlGG-gD-L9auTTKKM8lptYw_qSlmEzqOvZJ--gpUrWM9xmSyblTP-Ms0OPdIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه گفت که ایران در ازای کنار گذاشتن اورانیوم با غنای بالای خود، از لغو تحریم‌ها توسط واشینگتن برخوردار نخواهد شد و از پیشنهادات ایران برای توافق پایان جنگ ابراز نارضایتی کرد.
ترامپ پیش از برگزاری جلسه کابینه خود در یک تماس تلفنی کوتاه با شبکه پی‌بی‌اس نیوز، در پاسخ به این سوال که آیا توافق فعلی به این معناست که ایران در ازای لغو تحریم‌ها، اورانیوم با غنای بالای خود را واگذار خواهد کرد، گفت: «نه، نه، اصلاً. خبری از لغو تحریم‌ها نیست، نه.»
او اضافه کرد: «آن‌ها قرار است اورانیوم با غنای بالای خود را کنار بگذارند، نه در ازای لغو تحریم‌ها. نه، نه، اصلاً.»
ایران بیش از ۴۰۰ کیلو اورانیوم غنی شده تا حد ۶۰ درصد دارد که در تأسیسات زیرزمینی هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون است.
رئیس‌جمهور ایالات متحده ساعتی بعد در ابتدای نشست کابینه خود در کاخ سفید گفت که ایران بسیار مایل است به توافق برسد، اما آمریکا هنوز از توافق پیشنهادی رضایت ندارد.
ترامپ در این نشست در حضور خبرنگاران گفت: «ایران خیلی مصمم است، آن‌ها خیلی می‌خواهند که به توافق برسند. تا اینجا هنوز موفق نشده‌اند... ما از آن راضی نیستیم، اما خواهیم شد.»
او سپس بار دیگر ایران را به ازسرگیری حملات نظامی تهدید کرد: «یا به آن نقطه می‌رسیم، یا اینکه مجبور می‌شویم کار را یکسره کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75757" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D-HscLTH24xp4iChyTpWhbXx8LaVFetaxMoVJIEKgAOoAzMfIhNJXcpFPYlZaIYGFS83y0bITjoV6OP8ni026tDVpFNTRJmW0eWssxvFJwTyacbxwL72LClUIz1j6EJp6geZPid47xFJU2lCKfuvTjMJO8RdSLTWtD5bLlGjzvI5lsDLOaxIrtlhzgk_mn6seNxh0cb8IvhWAQ2lO81iRjj6y-yqTy2k1Skk3gc8AEYIj_-cE79uxhdKjDtVH8G-sWKoOBmSAL_-MktUZZ_vwXD3wQNEgnbnRLKNqswVb6ZZ0OZ3i7TPfk1eBzdAddEGUWfINjitGbCdvWDDLZJ68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر دلخراش از اجساد مردم کشته‌شده در بیمارستان تهرانپارس تهران
⚠️
دو روز پیش ویدیوی دوم رو با تردید منتشر کرده بودم و نوشته بودم نمی‌دونم درسته یا نه. حالا عکس‌هایی از بیمارستان تهرانپارس با شرح جان‌باختگان ۱۸ و ۱۹ دی دریافت کردم که نشون میدن اون ویدیو…</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75756" target="_blank">📅 20:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=dkAZ338jlzya0PpnPOdITFzg8HqxWXm4FANH8NIn-Hvdqz6tI-K90qvjumUSDh7wR6YqfhuenDd9FnTFd_Rk3p__wcVrs0YHlvdihbtWsZ0WMjgTjIWejcJGGUKO2x6vdlGEaz7P7kI-xve16wrxylfXch7UOmEANa64o2TeU4FpLFokK6V9iKZXd-GOk7tWAwfVjIUnh3unMS8utS05E1Feq8wZvp1nkpYxrj9JEHuJJc-5yX6QcF3SflGk9pVuutMFUPoAaZtUCEcqvljehkymf63QZGqZBLmk51z7Sglcv_nauiNp93MCeCC3iqiSf4sRChi6ZP_4jRKPdlQmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=dkAZ338jlzya0PpnPOdITFzg8HqxWXm4FANH8NIn-Hvdqz6tI-K90qvjumUSDh7wR6YqfhuenDd9FnTFd_Rk3p__wcVrs0YHlvdihbtWsZ0WMjgTjIWejcJGGUKO2x6vdlGEaz7P7kI-xve16wrxylfXch7UOmEANa64o2TeU4FpLFokK6V9iKZXd-GOk7tWAwfVjIUnh3unMS8utS05E1Feq8wZvp1nkpYxrj9JEHuJJc-5yX6QcF3SflGk9pVuutMFUPoAaZtUCEcqvljehkymf63QZGqZBLmk51z7Sglcv_nauiNp93MCeCC3iqiSf4sRChi6ZP_4jRKPdlQmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد، در نشست کابینه در کاخ سفید درباره مذاکرات با جمهوری اسلامی گفت تهران «بسیار مشتاق» توافق است، اما مذاکرات هنوز به نتیجه نهایی نرسیده است.
ترامپ گفت: ما از وضعیت فعلی راضی نیستیم ولی خواهیم شد.
رئیس‌جمهوری آمریکا همچنین جمهوری اسلامی را تحت فشار شدید توصیف کرد و گفت: «نیروی دریایی‌شان نابود شده، نیروی هوایی از بین رفته و همه‌چیزشان از دست رفته است.»
ترامپ افزود جمهوری اسلامی «در حالی مذاکره می‌کند که چیزی برایش باقی نمانده» و هشدار داد اگر توافق حاصل نشود، آمریکا ممکن است «برگردد و کار را تمام کند.»
ترامپ گفت: «آنها تازه دوباره به اینترنت برگشته‌اند، چون به‌شدت تحت فشار قرار گرفته‌اند.»
او همچنین گفت اقتصاد ایران «در حال سقوط آزاد» است و تهران به‌دلیل فشارهای سنگین، گزینه دیگری جز حرکت به‌سوی توافق ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75755" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری فارس به نقل از «منابع آگاه» گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، ممکن است در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق میان ایران و آمریکا نهایی شده است؛ اقدامی که به گفته این منابع می‌تواند با هدف اعمال فشار سیاسی و اثرگذاری بر افکار عمومی انجام شود، پیش از آنکه اختلافات باقی‌مانده به‌طور کامل برطرف شود.
بر اساس این گزارش، این سناریو در حالی مطرح شده که هنوز برخی موضوعات میان دو طرف حل‌نشده باقی مانده و روند مذاکرات به مرحله نهایی نرسیده است.
در همین زمینه، یک عضو تیم مذاکره‌کننده ایرانی در گفتگو با فارس تاکید کرده است که تا زمانی که همه موارد مورد نظر ایران حل و فصل نشود، هیچ توافقی قابل اعلام نخواهد بود.
به گفته این منبع، جمهوری اسلامی ایران تنها در صورتی که اختلافات به‌طور کامل برطرف شود، نتیجه مذاکرات را به‌صورت رسمی اعلام خواهد کرد و هیچ توافقی پیش از رسیدن به جمع‌بندی نهایی، مورد تایید تهران نخواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75753" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Td-MtCFkDaY8p9efdAmDP4pftIM57edEnh4RH9fVQajDnvKEhSJraKR6vBZo0sq_1QkseuHanwC4UG29-VbtwKkA0_DrzibFzmHDS76NhtaDGrlNLpQLRlKNe9gqU_BRXrQ6YLLYgiq1UeCNe25h9bxGRJPf--eItJwhFVNSo69axdfRuWaC3ceI0oMcnl5ypP2AsNIFveqy1KqU_p7nvHIwOAjsYeWzsV2-zyEB2DAZhoohPV8k0iRypTtudN7Vd0okzE2xdbk3IPMWk83DNomV_JGcMva-h2s80aB8sIcox8AVGH59lWJ35QGymH8Vq3dG7M9GmGOh0VHz4gyoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=GMKO-v6Ef3w0Wu7i8lA0W3Wb5INVFVODJK0ear3KE1hzFIsCeIQ4kMPan2N6KeLojK50GVD0QvcrIttpYOpdFSKaGx1u0PO1tLjxUI5ahSCAMjrpryuX33Oo0mxwGXkc02JrA9RKsVesIrTAIR-O3xHvXB467vI3bU0fBNOFwkszrovWVEqbZ7nGULqN4Vz3E3mmy0V60PdxfWnyZcgHeQH0RXcohQU904w_GnvZM1HXtw8Go6dKzLc-XaMU44N9VJ--1ydMOXbN0EFFUgo8KcnEdcr9CEcsaKeCFL0a_69ziEJ6n7HfX6mDDMfRIQEi9vMGXSXjp0BLGLfpcK9FLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=GMKO-v6Ef3w0Wu7i8lA0W3Wb5INVFVODJK0ear3KE1hzFIsCeIQ4kMPan2N6KeLojK50GVD0QvcrIttpYOpdFSKaGx1u0PO1tLjxUI5ahSCAMjrpryuX33Oo0mxwGXkc02JrA9RKsVesIrTAIR-O3xHvXB467vI3bU0fBNOFwkszrovWVEqbZ7nGULqN4Vz3E3mmy0V60PdxfWnyZcgHeQH0RXcohQU904w_GnvZM1HXtw8Go6dKzLc-XaMU44N9VJ--1ydMOXbN0EFFUgo8KcnEdcr9CEcsaKeCFL0a_69ziEJ6n7HfX6mDDMfRIQEi9vMGXSXjp0BLGLfpcK9FLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آتش‌سوزی
در یکی از برج‌های مجتمع مسکونی پامچال در چیتگر
#تهران
تصاویر دریافتی + منتشرشده، چهارشنبه ۶ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75749" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzvoUI_KXzJlrbyLBECsBrvNjgQnIxiulc6PRUPo1tib1IAVmoRDJsPRcHo-To6mpPp8devbl-qAyWdrI5OVw0JoOFM6Og-DgZXpchweLyUjEpK4QTVE0KcLH-fWYiUJagajV23RN9BDOVWPM1EoMjY2y4GrsHfVtuq91rBMTMdYB-TR3T4COGWXFxD4SfjtVLuR-jncirQLdY-W93xpM2xwGedx_t1014mEYc7VUWTsBBKGRgf7q17PhtnLY08O0RsgNnxMR0pMLExUnf2E4lNA8ZncRiYmK7X4GPIR4fGrWf1QdWrSmGh5BHihpPuwCs255-MdneGvvf1NRGhPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید روز چهارشنبه اعلام کرد گزارشی که از سوی صداوسیمای جمهوری اسلامی منتشر شده و به پیش‌نویس یک چارچوب اولیه و غیررسمی برای تفاهم‌نامه میان ایران و ایالات متحده اشاره داشت، «صحیح نیست» و تفاهم‌نامه مورد اشاره «کاملاً ساختگی» است.
تلویزیون حکومتی ایران ساعتی قبل گزارش داده بود که پیش‌نویس یک توافق چارچوبی با ایالات متحده شامل تعهد به لغو محاصره دریایی ایران، بازگرداندن رفت‌وآمد در تنگه هرمز و خروج نیروهای آمریکایی از منطقه خلیج فارس است.
کاخ سفید در بیانیه‌ای اعلام کرد: «این گزارش رسانه‌های تحت کنترل ایران حقیقت ندارد و تفاهم‌نامه‌ای که آنها منتشر کرده‌اند کاملاً ساختگی است. هیچ‌کس نباید آنچه رسانه‌های دولتی ایران منتشر می‌کنند را باور کند. واقعیت‌ها اهمیت دارند.»
گزارش صداوسیما
مدعی شده بود که آمریکا متعهد به رفع محاصره دریایی ایران شده و در مقابل، ایران تعهد داده تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند.
تلویزیون جمهوری اسلامی همچنین گفته بود بر اساس این پیش‌نویس، «مدیریت و مسیر عبور و مرور» کشتی‌ها با ایران و همکاری عمان انجام خواهد شد و آمریکا تعهد داده نیروهای نظامی این کشور از «محیط پیرامونی ایران خارج شوند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75748" target="_blank">📅 18:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PipQ7EQ4cZoTCIIywghWcRi9hjrg0WFyH_3J10jY37nXRkLNeg-Kn6jbqI9sWNfbpAQAehZjExXS1klUtzADQKR2cCsOWpSeXCTbfikXhinZN7rRaGYalHHb9Y7lsEImefzx5cc1kla63_us5hhPDnxz34CNHyiWKuDhG0ltqbcMTaOw1J08NW_h8B1G0Rz_BkYNZeSQUzQw1gwh-rasA5eHJ2RyF3WnRIqq6hUuKYd2YMAgqR67PG9-cfvrsdDEQrA7a1eFuTOMOG1sJ-EBjS0FjscXSSU4Ef2GpbjKsmbJG7dbP5kfZHqBDlAZ582sp_k4IvmT7CY5i5TUD_wEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد در شبکه اجتماعی تروث سوشال با انتشار تصویری ساخته‌شده با هوش مصنوعی، از شبکه سی‌ان‌ان انتقاد کرد و نوشت این رسانه نیروی دریایی جمهوری اسلامی را قدرتمند نشان می‌دهد، در حالی که شناورهای ایران در اقیانوس غرق شده‌اند.
در این تصویر، جمله «سی‌ان‌ان: نیروی دریایی ایران قدرتمند است» در کنار تصویری از شناورهای غرق‌شده جمهوری اسلامی در کف اقیانوس دیده می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75747" target="_blank">📅 18:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCcYiAboKVYaLveuHsk4HxdBvZo_4y1b9XNNyrW_Gs9GolUGmsStNJCA68xFViDJaRWDDqsNl6qWHD-aOCDH-Z0oPaXRoc5yTCgOZflCgoQsOly6JPk03PS4gPHRBsVN4ssl6oXCwC9extID4JmzI_gHomyOB8ykTDI81wAKlGudKrmukQb26jBS6zjVPif_U8aOPq_TkDr-7LkeqOmfuFpKKyfi08GRiKPpjvaLAn1AXTaZmwaSNgfdFDhd7_8fBWnkqcj5pOgRlhvWDPpkuAOyZNouhVsEd8un9V4qvymSNqFsvKFpl1gETaZ_VB1fOoHAT48PN82rMHGuRcxAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گروهی از کاربران در شبکه اجتماعی ایکس (توییتر سابق) پست‌های انتقادی گزارش‌گونه از تحولات و رویدادهای سیاسی خارج از ایران منتشر می‌کنند، خطاب به شهروندانی که پس از حدود سه ماه به‌طور تدریجی با فیلترشکن موفق می‌‌شوند به اینترنت وصل شوند.
‏این پست‌ها که با عبارت‌هایی مانند «
وقتی شما نبودید
» یا «بچه‌های ایران که تازه وصل شده‌اید» آغاز می‌شود، همزمان با کاهش تدریجی اختلال در دسترسی به اینترنت، به محلی برای مستندسازی و بازاندیشی انتقادی نسبت به تحولات سیاسی‌ ۸۸ روز گذشته تبدیل شده است.
@
VahidHeadline
دوستانی که تازه وصل شدن یدونه «
سلام وحید جان
» سرچ کنید آرشیو کامل از اندر احوالات ایرانی جماعت در زمان قطعی نت رو براتون میاره
iamroyaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75746" target="_blank">📅 18:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=SJAe26roCxnGor-hO0z3Xe8T3nHAHN__34KGf2AKsTI56VpkL6W5yxyb6hQwpsL6fHispLCU1mVkdY5iCSd75BJ3hJigw5vAvbxRlrQblFpeb_BQhTxroSJFYEmW_lJItKcacObeb-SxAR5ao5E2okmydncq6027MpmsS816tZkTyK2k6Mc2syTia7DZMg3bL4GvbkvTjzGlC-NYIGroZqPHoAFzUhUaw1msEBkfnT-geN1ynKGFUNxshWINAm6tm4LDJ-x6AF8ccHGWw4Ncm9KC9hteNQkQnOApbQFjcsrSr502h4Qe9fgPgDSTVqbfYNqRBJpmj0iEw6K2RC1mvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=SJAe26roCxnGor-hO0z3Xe8T3nHAHN__34KGf2AKsTI56VpkL6W5yxyb6hQwpsL6fHispLCU1mVkdY5iCSd75BJ3hJigw5vAvbxRlrQblFpeb_BQhTxroSJFYEmW_lJItKcacObeb-SxAR5ao5E2okmydncq6027MpmsS816tZkTyK2k6Mc2syTia7DZMg3bL4GvbkvTjzGlC-NYIGroZqPHoAFzUhUaw1msEBkfnT-geN1ynKGFUNxshWINAm6tm4LDJ-x6AF8ccHGWw4Ncm9KC9hteNQkQnOApbQFjcsrSr502h4Qe9fgPgDSTVqbfYNqRBJpmj0iEw6K2RC1mvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما اعلام کرد به یک سند غیررسمی اولیه از چارچوب ۱۴ بندی تفاهم احتمالی میان ایران و آمریکا دسترسی پیدا کرده، سندی که به گفته رسانه‌های ایرانی، هنوز نهایی نشده اما حاوی جزئیاتی درباره وضعیت تنگه هرمز و حضور نظامی آمریکا در منطقه است.
بر اساس این گزارش، در پیش‌نویس منتشرشده آمده است که آمریکا متعهد می‌شود نیروهای نظامی خود را از اطراف ایران خارج کرده و محاصره دریایی را متوقف کند. در مقابل، تهران نیز تعهد می‌دهد ظرف مدت یک ماه، عبور کشتی‌های تجاری از تنگه هرمز را به سطح پیش از جنگ بازگرداند.
طبق مفاد این سند، کشتی‌های نظامی مشمول توافق نخواهند بود و مدیریت مسیر حرکت کشتی‌های تجاری در تنگه هرمز با همکاری ایران و سلطنت عمان انجام می‌شود.
صداوسیما همچنین گزارش داد که هنوز چارچوب نهایی تفاهم تدوین نشده و ایران تاکید کرده بدون وجود «سازوکار راستی‌آزمایی» یا همان مکانیزم اطمینان، هیچ اقدام عملی انجام نخواهد داد.
در بخش دیگری از این گزارش آمده است که اگر دو طرف طی ۶۰ روز آینده به توافق نهایی برسند، این تفاهم می‌تواند در قالب یک قطعنامه الزام‌آور در شورای امنیت سازمان ملل تصویب شود.
@
VahidOOnLine
🔄
آپدیت:
کاخ سفید: گزارش رسانه‌های جمهوری اسلامی درباره تفاهم‌نامه تهران و واشینگتن کاملا ساختگی است
کاخ سفید گزارش رسانه‌های جمهوری اسلامی درباره بندهای تفاهم‌نامه احتمالی را «کاملا ساختگی» خواند و گفت نباید به روایت رسانه‌های جمهوری اسلامی اعتماد کرد
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75745" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjN0KrZClO8b8Sd0VpKoylu9hcZILxdxOrrhnu5a0xMM9NLJgB16SKLBxGRsE4IbQTCaOgkuvhiler6fQBOwzymzdrgn1XUGqdzMAioxhr8rL_vSt0uPpeGWo5axBZvafWrU7lReKX32rvYOmiJir5aq2vmils51KI3ryNfev7pk3gotVYZuxJ8uTZSOJIHYxy3aCbpoMII_9oWZkLgDETIuLRToltiKwqL3Q_NlM9jDpA49-CNKayy-kOcddhYKtkQ2czXE5PBnPo9W9z2aAKPrYjusWuIQWmNTMGgdICQ4Ktqz_i9-zZ4iWvQJz_EVVz9lwtuAlgL8eXlD6exUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در تروث‌سوشال گزارشی از جروزالم‌پست را بازنشر کرد که بر اساس اطلاعات اختصاصی «مدیا لاین» نوشته است موارد آزار و تعرض جنسی به زنان بازداشت‌شده، به‌ویژه زنان جوان، در زندان‌ها و بازداشتگاه‌های جمهوری اسلامی در دوران آتش‌بس افزایش یافته است.
در این گزارش، زنی جوان به نام کاملیا گفته پس از بازداشت خشونت‌آمیز در خانه‌اش، دو هفته همراه هشت زن دیگر، از جمله دختری ۱۶ ساله که با ساچمه از ناحیه صورت زخمی شده بود، در اتاقی ۲۰ متری نگهداری شد.
به گفته کاملیا، او پس از انتقال به سلول انفرادی و خودداری از اعتراف اجباری، در اتاق بازجویی هدف خشونت قرار گرفت، لباس‌هایش پاره شد، با باتوم مورد تجاوز قرار گرفت، به‌شدت کتک خورد و به تجاوز گروهی تهدید شد.
جروزالم‌پست همچنین با اشاره به قطع گسترده اینترنت، بازداشت‌ها، ناپدیدسازی قهری، آدم‌ربایی، تهدید روزنامه‌نگاران و مخالفان در خارج از کشور و افزایش ناگهانی اعدام مخالفان نوشت سرکوب در ایران تشدید شده است.
دونالد ترامپ پیش‌تر نیز با انتشار پستی در تروث سوشال خواستار آزادی هشت زندانی سیاسی زن در ایران شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75744" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AfturfugMY2VgAeERNZqm27kFX0MHoiQS_G4WJ65pgnpUEDi_hI6MgddTjpImtnvYyGYtVxEzxKT1F_gL2yxVUJt5PCyvRlGyZdHpV-Zf9C-CpXBnb7dgI5vxaQYkmk6xIAsXSxhH3QppN0tn5O4i2nIXnqut29Ae3F4mb4cmgakKj3ZDeToBKBX_-pTlds3-PeHGxG4vYpfr0cvF9zszhoVOU-kpgTmtg8RUOOV5exj_sH8D-Q5NzZdKQXnXLdA5SyFnmKe_XGk9gP8TgFLg50xr1UOPJl6UWpB6vNhhUlx2Yh6I0mfH054LWqWNRCABfNZng3sjnEgIiXwEanbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lLaxhYmRwk5RE7PityiXBXbKFjZWvieBrfDpe4zFv2d-9jrVfWEeTljwzuLjFaTfBhs1E3hKHAAcLtU3dWZpLoa_lsOZ7GiOum_0pzWtcV22mepDCpuuNn6SGilVlPIHlQyK9Z3nAUHe3Ga57V5_wjgzIguockkzAM0DwtW_Iznly0EP2OE9z1cqjoCmJUhCDLGh1RlutrTZdiQHYmJZdlaygssrjAWwgDzp-2LIordw_e95lx_SKaJTggnv4pasfjHX9VJEzd7xV6DWIQMX6ji1AyAqKGj4QqCa6eFj_a8J4fB_YG48k5MD7ynUySYauiRj_eWIMBN4d5RawRwVdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز چهارشنبه ششم خرداد هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
این وزارتخانه در بیانیه‌ای مدعی شد که «تشدید فشارهای اقتصادی و متعاقب آن، انجام تحریکات گوناگون اجتماعی توسط عوامل دشمن و رسانه‌های مزدور فارسی‌زبان بیگانه، با سوء استفاده از برخی کمبودها و گرانی‌ها» یکی از محورهای مورد توجه آمریکا و اسرائیل است.
هشدار درباره احتمال ناآرامی همزمان با افزایش شدید نرخ تورم و و گرانی کالاها و همچنین انتشار گزارش‌هایی درباره کاهش شدید درآمدهای دولت جمهوری اسلامی در پی هفته‌ها محاصره دریایی آمریکا و سقوط شدید صادرات نفت ایران مطرح شده است.
این در حالی است که اعتراضات دی‌ماه سال گذشته نیز بعد از افزایش مداوم نرخ ارز در بازار و مناطق تجاری ایران آغاز و بعد از چند روز با افزایش تعداد معترضان، با خشونت شدید نیروهای امنیتی و کشتار هزاران نفر مواجه شد.
وزارت اطلاعات همچنین درباره «عملیات تروریستی و تجاوزات مرزی بویژه در شمال غرب و جنوب شرق ایران» و انواع عملیات «ترور و خرابکاری» هشدار داده و مدعی شده که آمریکا و اسرائیل به دنبال وارد کردن «انواع سلاح، مهمات و ابزار ارتباطی غیرقانونی، بویژه استارلینک» به ایران هستند.
ابراز نگرانی از رواج اینترنت ماهواره‌ای استارلینک در حالی است که بعد از ۸۸ روز قطع سراسری اینترنت در ایران، از روز سه‌شنبه شهروندان توانسته‌اند به شکل تدریجی و محدود به برخی سرویس‌های اینترنت جهانی دسترسی پیدا کنند.
@
VahidHeadline
این بیانیه که با عنوان «سخنی با ولی‌نعمتان و هشداری به دشمنان» در رسانه‌های داخلی ایران منتشر شده، ادعا می‌کند که «دشمن شکست خورده در جنگ نظامی، بدنبال تولید دستآورد برای خویش، گرچه از طریق جنگ نرم، می‌باشد.»
این بیانیه در حالی صادر می‌شود که اسماعیل خطیب، وزیر اطلاعات جمهوری اسلامی در سومین هفته جنگ در حمله اسرائیل کشته شد و دولت هنوز جانشینی برای او معرفی نکرده است.
وزارت اطلاعات در این بیانیه علاوه بر اسرائیل و آمریکا، بریتانیا و اروپا را به همراهی با این دو قدرت متهم و کشورهای عرب حاشیه خلیج فارس را به‌عنوان «غلامان متمول» مسئول تامین مالی «جنگ ترکیبی تمام عیار» علیه «مردم قهرمان ایران» معرفی کرده است.
وزارت اطلاعات در این بیانیه معترضان و مخالفان جمهوری اسلامی در خارج از ایران را تهدید کرد و نوشت: «مزدوران ضد انقلاب و تروریست‌های مقیم خارج کشور و حامیان آن‌ها نیز از آتشی که می‌افروزند در امان نخواهند بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75742" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dm3MqihBJnimZpeJCtTyH59qUtTZx9ovvhaNya1mzxx11vPkShc2nAsdFsQQpki8CDZ4AoULGDyx33TZUNUT1-WM1H55R-CJuhdnuNhLoCIBer5WvSV2TocBjicE_y5FqHVw1ep5LQpBlWlduINr_KRTpxJFKvt9VfKKrKQ5tcidjGq02XgZ8tNEHndj7OhepifCurTG0d3gjDxCYful-Jb4EvN3-Ev1aSkt7up9MKHnbbM50AVZeDufllpTYx3DoOfUzHiijFgwuSQv7Yo4xritWUG5q2ECCAyPFrKDPqYaEcxsZ0oakOWrepbRBcO4k02cU8n8qV27EMJsREcSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی در روز سه‌شنبه ۵ خرداد گزارش داد که حملات دوشنبه شب نظامی ایالات متحده به اهدافی در جنوب ایران پس از آن صورت گرفت که تحلیلگران اطلاعاتی، مجموعه‌ای از اقدامات نظامی بالقوه تهدیدآمیز جمهوری اسلامی را در ۲۴ ساعت منتهی به این حملات شناسایی کردند.
هواپیماهای جنگی آمریکا دو قایق تندرو سپاه پاسداران انقلاب اسلامی را که سعی در مین‌گذاری در تنگه هرمز داشتند، غرق کردند.
این مقامات که نخواستند نامشان فاش شود، همچنین گفتند که جمهوری اسلامی پهپادهای تهاجمی یک‌طرفه را به سمت حدود دوازده کشتی جنگی نیروی دریایی ایالات متحده که در خلیج عمان و دریای عرب یا اطراف آن هستند شلیک کرد. این کشتی‌ها در حال اعمال محاصره دریایی آمریکا علیه جمهوری اسلامی هستند.
طبق این گزارش تحلیلگران نظامی آمریکا همچنین فعالیت‌هایی را در برخی از سایت‌های موشکی زمین به هوای جمهوری اسلامی در نزدیکی تنگه هرمز شناسایی کردند؛ فعالیت‌هایی که امنیت هواپیماهای جنگی آمریکایی مستقر بر روی زمین و آن‌هایی که روی ناو هواپیمابر آمریکا در منطقه به عنوان بخشی از نیروی اعمال‌کننده محاصره دریایی حضور دارند، تهدید می‌کرد.
تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، روز دوشنبه در بیانیه‌ای گفت که ایالات متحده «برای محافظت از نیروهای خود در برابر تهدیدات نیروهای» جمهوری اسلامی حملاتی را به اهدافی در جنوب ایران انجام داد.
سایر مقامات پنتاگون گزارش‌های رسانه‌های داخلی در ایران را که در روز سه‌شنبه مدعی شدند یک پهپاد آمریکایی «ام-کیو۹ ریپر» توسط جمهوری اسلامی سرنگون شد، رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/75741" target="_blank">📅 04:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8Lve7_471avRAq1nUMtvqNyyV9yuzuUTu0R0gzVNtQtsiyZQCTySO_nJWHREkkpg0BwosscQYT7ez75eDnRgaKIO3cg9ZvY1L0xVtgw59A2jK72IWd-EWRWZEQXhAWxhnV6SX7uvmBX8b0uUeXQi48QjMfavC2oe69BRG4F6_xqex-7ravfBwLK_w2vGPuM7bXCJZyG3nThTj2EgoSMMofv0YCzLPwjYIJOJeLlHjgbqwktZAvInMHDm1SDtTaH5PZsty87eAlyZQo8oQoLr678Y1D6YtLHhVU_NiX5pbQpwLiEW5y4lRhW5UvqdLj_LYr2Fl-rBpEkvoKouR7VyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
با توجه به احتمال نامساعد بودن شرایط جوی در روز آینده، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/75740" target="_blank">📅 00:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pk7KteHVWGU8e6rxxSACGUGsQ8t8jFIrKGPQkRyYrZpoVJbV2LwWwKHVvTrIqGo-ggqB1mVR8JTEZcPnXSo9N9DkkRkwb-3k-AljibPvY7PJnK4updOYkgOsQNmrucU6f5i7Fnf862lngSo9VTfwysWOBJvWHfcD1m9OFEO-ygkDh3KmlSEhqlcyyzdfBpnFh3zjp6HRTyoA4bH3QnQe7A1q8xMC1jtIJ_ysp613DyiJGpadFKnsjCxnlhEUQRXLSEEaluT0PMzwRfLbjwp5oTaLSC2unqvQNmIGlHEKdvSffpg6oNdKTQvPbuGKTHKWyT4h6UP-FLCLh3QGMiptDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ متنی که
۸ روز پیش
منتشر کرده بود رو دوباره پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر کل ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بگذارد و دست‌ها را بالا ببرد، در حالی که هر کدام فریاد می‌زنند «تسلیمم، تسلیمم» و با هیجان پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمز شکست‌خورده، چاینا استریت ژورنال، همان وال‌استریت ژورنال، سی‌ان‌ان فاسد و حالا بی‌اهمیت، و همه دیگر اعضای رسانه‌های جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و اصلاً هم رقابت نزدیک نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها به‌کلی دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/75739" target="_blank">📅 23:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnohsz5vBip8DRDfA5paMknwSL1AyLgVtfYldt0xwgKDj3z567k8aVA2h9jhjUMKRKE29KnaA-mOeyhF09iGsviUdt6vDMc0ICU-zT4hrp4kPoTicPlw4JT5ZszpAAKAR3d-_kOhWxeNckLc0yaqbhBnesOuELpKXiRN8BJGmbduqZlAxJYLc6-2plNA51Ksxdc3gpCrIoj_2t2NJ6Tf5wIRYF2vYRcGGquKjfAXPCYvonOICAQYaeyBgfDTsUTSf4-NYQyLoCWRF0mQi0watgQYfTVRjFImbi2Rzur1UvsxZOnYcGyoWKA_W3OxpSAT3C2d02fShXkO_NFEF1k9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، قرار است روز چهارشنبه نشستی کم‌سابقه با اعضای کابینه خود در اقامتگاه ریاست‌جمهوری کمپ دیوید برگزار کند؛ نشستی که به گفته یک مقام کاخ سفید، همزمان با نزدیک شدن مذاکرات مربوط به ایران به مرحله‌ای حساس برگزار می‌شود.
خبرگزاری فرانسه با انتشار این خبر نوشت که انتخاب کمپ دیوید، اقامتگاهی دورافتاده در کوهستان‌های مریلند که ترامپ برخلاف بسیاری از رؤسای‌جمهور پیشین کمتر به آن رفت‌وآمد داشته، نشان‌دهنده حساسیت گفت‌وگوهای پیش رو ارزیابی شده است.
روزنامه نیویورک‌پست گزارش داده که موضوع ایران محور اصلی این نشست خواهد بود و همه اعضای کابینه  [
از جمله
تولسی گابارد، مدیر مستعفی اطلاعات ملی] در آن حضور خواهند داشت. بر اساس این گزارش، مسائل اقتصادی نیز در دستور کار قرار دارد.
کمپ دیوید در گذشته صحنه چند تحول مهم دیپلماتیک به رهبری آمریکا بوده، از جمله توافق‌های سال ۱۹۷۸ میان اسرائیل و مصر در دوره جیمی کارتر و نشست ناکام اسرائیلی‌ـفلسطینی در سال ۲۰۰۰ در دوره بیل کلینتون.
این دومین سفر ترامپ به کمپ دیوید در دوره دوم ریاست‌جمهوری او خواهد بود؛ نخستین بار چند روز پیش از حملات آمریکا به برنامه هسته‌ای ایران در خرداد ۱۴۰۴ بود.
@
VahidHeadline
🔄
آپدیت:
محل جلسه فردا عوض شد به کاخ سفید
چند پست پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/75738" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sXN9oVq5qLRSCrocFQEkgmyP8eUGzMUVZPjF1e7BPopztWIjnEs3Y6vhwR2tFi-tK_19sev_KPoLNhwknY9upJT_QgkZr-_CyV1qKdMHox_Hb1Gr2Kvz2YhgtUPxQwxkG_JAKTyHjkmf8jSMBAIq9WYKsj9eUYkvMyKONX9UmMW_N8J-wbfrmqx_x5Zs8fZ3HmYs8hjhBQZrKRp7HrU5rfOf2e5fxg0xfYnoxQjtN10nNVJgi0oPsgmkVBIFlrbFWdmy4Zl-pRaUp0jVQ35j69wah1gjw2lhXpoRJVXPrR0Bk7cDKr1a_ystFBa_Ym9CTbLIx6BS6ecM6emwkjtd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش فارس، خبرگزاری وابسته به سپاه، محمدباقر قالیباف، رئیس هیات مذاکره‌کننده جمهوری اسلامی ایران که روز دوشنبه در راس هیاتی با همراهی عباس عراقچی، وزیر امور خارجه و عبدالناصر همتی، رئیس بانک مرکزی، برای رایزنی با مقامات قطری به دوحه سفر کرده بود، عصر سه‌شنبه، پنجم خردادماه، به ایران بازگشت. بر اساس این گزارش، محور اصلی گفتگوهای میان مقامات عالی تهران و دوحه در این سفر، رایزنی درباره بازگشت پول‌های مسدودشده ایران بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75737" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L590UNaIwz_BKcw-QqBFCBnuJ0a1ywPGofxwDQUR1ubQoJAnCHJOnxgOWKDvL81gcyjTo5Z7ZL3DLn_kT8saxYB85jiHEJxh3o5NRLCJVzh61EHst5q1Qk5MVmuoXVL2tiCIgfZuEzZe3k6g6KFfUh7jPcxyqoybQHvzhctxGHplvu8U-93kluUexuNnukoOe5SWjazRq87T-abAVP0VxGYWPS9EVNIL__B-rlfJ5ab6oaT3y3GM6yLbeuDnWaQq6-UKNJncxSL2LNmzmXNTdMwAIEOouY4r_Z4IwvQm9Mu8zJ-okhsOifmNHqNFnz2lpbsn4dtBDceiT1_cSoNdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز سه‌شنبه، به نقل از منابع خود مدعی شد که طبق متن ۱۴ ماده‌ای یادداشت تفاهم بین ایران و آمریکا، منابع بلوکه‌شده ایران، به میزان ۲۴ میلیارد دلار باید در طول مذاکرات آزاد شود.
آنطور که این رسانه نزدیک به سپاه پاسداران از قول « یک منبع آگاه نزدیک به تیم مذاکره‌کننده» گزارش داده، ایران تأکید دارد که نصف این مبلغ باید با شروع مذاکرات، در دسترس قرار گیرد، و بقیه در طول ۶۰ روز منتقل شود.
این گزارش می‌گوید که سفر اخیر عباس عراقچی و محمدباقر قالیباف به قطر هم برای تفاهم دربارهٔ اجرایی‌سازی این مطالبه، و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
همزمان، احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد که چند روز پیش، قرار بود ۱۲ میلیارد دلار از منابع مسدودشده ایران، از طریق روسیه وارد شود، ولی آمریکایی‌ها مانع این انتقال شدند.
هنوز هیچ مقام رسمی در دولت آمریکا، این ادعاها را تأیید نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75736" target="_blank">📅 18:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DPwV-OSKOQEluhDPzGfIjLqvLPK8vusO2QzED2mWbYqG2yKgAu4bDubxBkkJo05hZvv_UCIjnRuy3U5Zg0VSLSsZhYZO1E5J8VQ5GM3IBqoM06JzgBIV0nFohNNu9OorDC8I6dAjvXj63lqFKY_qxUMfb_Zg08zGm3-jl_S_nDBJZzcd9B9q031SYnR7oX4nH0IwmBw49P8dCPkCiXaDCYVyDryQkrBLIUp8xtikX0hrUUz6G96-m_JT_5e0-18Di9noZaf8VCAm5gEzgEL9HQJ4BIVvIVkErrFnF4StdGeahRSXBnXAaYjp6iebF0g9_uWc4UUM2rryXQZ3xUsymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sRPd0XYTm0ZgiohUFkfAsrjvQcEzmhdNU-5APoclgyvyY6G9XTq7kIuEGt26RN6EMGsIpVKXqqUTEEtviAlEJ3k1SKbUSdYX7a6lI_CNjwbEBtU1o6--qw5rxNtYmrClJBkOj6-CBL4GWvolGzFWBTaULHtV3RKM9hfa9BIt0OoFPFPxWBK_Uf15TQ7MyA80BB-elxnG1FTv-bcf5u8uXP04xsw_xkEi4v5APPXKJzbhu7KwrW-F4UnfDTw23QPpdKViXQA1gEpdicXBBJMv04g5ri__vKyRhteZXYNII6T-y3lbOjNkmHtLZS1DpV9ox-fUaVkad_yQXmK0hSqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OViDUSaItfy885fyMfWt2-Tws3Mb5fALzC_YpS6kUQ0S9FloyBPA8p6GLT5mmGh3g-YHEFLMDUe5PdR5Bfd_8QIfgPxjcZkuxXmN_ddQKzy8rcg9hJI3R0JBOz6iaLNe9fiFHvrtgiONcXfb4KAcqH3jKBj8SifsRN0wMFFZCE0ig8q3uAWv4JeDq6epEBoj6TBbtVS7_090q_JoFC4O-w9ez0rBH1YA1IOCTWlPvpjsK1gL4IEf5tq5sJwXmCDFV_5Qjqd_yrX6mQzbb2-ovlfrw3ioTheGXWLhMmTEqeQNIgpWbV69f_k45cP1vRf87ibKZMUL3iZY-H2nhV-sBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yf2eu9YSbtdbfZN3Ub6QUSZuoDxP1O0dZGdZTj3OPLymO7KmjPC3o4feJQOxsMpCDs5WbncuAq5k3pTt9BMiJalhUrr0mFMqxA3rRDxdOVWLHjLlzTRAC6Q4170n8pZfdDp7QOvEKNlbWAFb_2P6WZJktbNhgqfOnHMFMKYytANNTHpZLtdEBSsfQuuDEBgMI-nPhOPVohXpNLh7aDgz4eKW3NOE4hGqyk6WVCFiO8vm7WdtRGrs8mZKxYacKRhYmhcMFd-dluQnbfJ3JRGWsHdNJJktX-QMSHCzgZVm9fS19XpGM5IUgr8aJcqKSCgEzHBSY8mWl9rOisbN5mz1UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد پایش وضعیت اینترنت در جهان، اعلام کرد داده‌های زنده این مجموعه نشان می‌دهد اتصال اینترنت در ایران در هشتاد و هشتمین روز قطعی گسترده، به صورت نسبی در حال بازگشت است؛ هرچند هنوز مشخص نیست این وضعیت پایدار خواهد ماند یا نه.
@
VahidHeadline
ساعاتی پیش از این واقعه اخبار دیگری منتشر شده بود:
در حالی که مقام‌های دولت مسعود پزشکیان از آغاز روند اتصال کامل به اینترنت تا ۲۴ ساعت آینده خبر می‌دادند، دیوان عدالت اداری اعلام کرد دستور توقف اجرای مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» را صادر کرده است.
این دیوان ظهر سه‌شنبه پنجم خرداد اعلام کرد «به‌دنبال طرح شکایاتی، دستور به توقف مصوبهٔ ایجاد «ستاد ویژهٔ ساماندهی و راهبری فضای مجازی کشور» داده است» و افزود: «تا زمان رسیدگی نهایی به شکایات مطروحه، مصوبات و تصمیمات این ستاد قابل ترتیب اثر نخواهد بود.»
مرکز رسانه قوه قضاییه نیز اعلام کرد دستورات و مصوبات ستاد ویژه «به دلیل بررسی غیرقانونی بودن ساختار ستاد، تا زمان رسیدگی قانونی قابل اجرا نیست».
@
VahidHeadline
بعدش:
همزمان با اعلام دیوان عدالت اداری مبنی بر صدور دستور توقف بازگشت اینترنت، ایسنا به نقل از «یک منبع مطلع»، روز سه‌شنبه، پنجم خردادماه، گزارش داد که با صدور دستور اتصال اینترنت از وزیر ارتباطات و فناوری اطلاعات فرآیند اتصال در حال انجام است و طی ۲۴ ساعت این امکان برای همه فراهم خواهد شد.
این درحالی اتفاق افتاد که تنها یک روز پس از مصوبه «ستاد ویژه ساماندهی فضای مجازی» برای «بازگشت اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴»، دیوان عدالت اداری با صدور دستور موقت، «اجرای مصوبه ایجاد ستاد ویژه ساماندهی فضای مجاری» را متوقف و مصوبات این ستاد را تا زمان رسیدگی نهایی، غیرقابل اجرا اعلام کرد.
همزمان، انتخاب نوشت که کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری تحت راهبری یک مقام ابقا شده دولت ابراهیم رئیسی، «شاکی قضایی» اتصال اینترنت بین‌الملل هستند.
ایران از زمان آغاز جنگ در نهم اسفند، به مدت ۸۸ روز، در خاموشی دیجیتال به سر می‌برد.
@
VahidOOnLine
محمدرضا عارف، معاون اول پزشکیان، در شبکه ایکس نوشت پیرو دستور پزشکیان «گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد.»
او افزود: «با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود.»
عارف در متن خود درباره «گام نخست» و وصل شدن اینترنت برای شهروندان توضیحی ارائه نداد.
این در حالی است که پیش‌تر فارس، رسانه وابسته به سپاه نوشت دیوان عدالت اداری اعلام کرد که در پی طرح شکایاتی درباره ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»، هیات تخصصی صنایع و بازرگانی این دیوان، با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت صادر کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75732" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YyIqbPMVYYFi70hcpvINeY0UcRjKq0p4OUj1zZSAMbqO2myt9jR2ztJAZjAqCe8CZpaHDSNIpPiPZEMspSKoLAqzOL4QIDHntvN9mBvencDpurLWx6qBRYDBucwlBw1SH5xVRH9PoG26PFEhxI_za6PG56YsCJsOASbkxqjYpqIJXmsT_MpghKwCLbK_s2EDF9ZeyWZn5vBj_C2wl3KX-qKgvHrfUWcc9hbPQNE-gkqzcgmkKmOtgL0uLADCZsNfMPY17VHIvm3rw36ea_dlGacPo-WiQ6UCnqoIljmTpaEVqr7vRWTrDAJWqbEd7W5KUSRJ1gR2B271OQwP6YIicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75731" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QJOpA647sz4UL-nwIvHVwb7x3G3e6dEJmg7RPcfiv36O6cNoX_hfXEl7eFhiA7l_edx7ZfSaNKfbNZBWJUDBqf08ZypXQ0cdhwfqY7x9k4uKCRRYLR_5lMART0B5nwHC_hduenGqrjjp2lQNd2_-xhijpnxJz6_sx7Q3fF4Hx9-T_txPfkdXO05ES10xwvl5OFlHNLGQ-You6MjcyPX2kKMutecy0BPoDsSPEMS9FXqtDj7gyZDjEeB0TZviHGaTDIrFdJLda1HQEzlpbQteRoQVIOEDHwAQJ-dqvj1N2AAkWAw-rpPNFfiNjkxOoWi-Yuhbe7xwzBr8LGBMgySN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jGHmaXxAkMPSHBzQGUx1zDUhS4vTDRv8Pes2XbwG5DHqJSUO05HustOoMxRMLg3QUCR9y0838mcjAqqV-UW5pvrGyLYWaMVty73IJIbNGySqTCxdEGA1ABuLqLIYCNdQwF1F5Jk8nYA5d0wiAXOeHDzCenEFGnQtijOW0_TMBUrsFsZ2clmG-rrBOuNtgGB2K1cCtcHDTL4pZ35Y28cQyGd4XWi3BVDk8BAmsMrH8uHxgaFicGYbZWSj7sMRFQ-8WVyKx3CuPWUryxjAZTpOG4K564XYcPynk5Lud9qoEXZTIz4vAydZzx41uorYgHWobvx5x_QVaNAgy53PMk32CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران روز سه‌شنبه پنجم خرداد پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را به‌مناسبت برگزاری مراسم حج منتشر کردند که در آن می‌گوید آمریکا از این پس «نقطه امنی برای استقرار پایگاه نظامی در منطقه نخواهد داشت».
او در این پیام توضیحی دربارهٔ پایگاه‌های آمریکایی مستقر در کشورهای خلیج فارس نکرد اما هشدار داد که «سرزمین‌های منطقه دیگر سپر پایگاه‌های آمریکایی نخواهد بود».
مجتبی خامنه‌ای همچنین با یادآوری ادعای ۱۰ سال پیش پدرش علی خامنه‌ای درباره اسرائیل، مدعی شد این کشور نیز «به مراحل پایانی عمر» خود نزدیک شده و «۲۵ سال بعد از آن تاریخ را نخواهد دید».
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی را از او منتشر می‌کنند.
@
VahidHeadline
در پیام منتسب به مجتبی خامنه‌ای با اشاره به گفته‌های ۱۰ سال پیش علی خامنه‌ای، رهبر کشته شده جمهوری اسلامی، اسرائیل «رژیم متزلزل صهیونی و غده سرطانی» توصیف شده و آمده است: «اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله.»
این سخنان در حالی عنوان می‌شود که اسرائیل و آمریکا در یک سال گذشته در جریان دو جنگ، مقام‌های عالی‌رتبه  سیاسی و نظامی حکومت ازجمله علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، را کشتند، بخش بزرگی از برنامه هسته‌ای جمهوری اسلامی را نابود و تاسیسات و زیرساخت‌های نظامی و اقتصادی ایران را به‌شدت تضعیف کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75729" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NafdMmwsvynf4R14z1JW-PgtGg5oN42OyuUHuhAQilRJGK5m-Bnm4qwnW2_7HLAJoY1HneyG4vTqc3UbqJpp3L7hYc6PQpMU6_XZTtm8nNk-2wJ6kX42SgbUw021JbkePqUtUgeMzB1Pm2IgrL8zorFCzHnW1hnTup_v21NgHGUAW82Vi1nJnFNuKFM7wgdpKW-cF95uugClNnuiHgONeGD3b6jY1LwYzh8RDnBEftnEuWxZkDqmF6huGuhPq3IO40hM5Gs7z_-Q8WADhO_bqCcpljWwmPIOYV721-ry6iUIQ_jv4K_Y45bNhVLU2QFBwXy83JUpb5vgpxI_V4-SlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر می‌گوید گزارش‌هایی که ادعا می‌کنند دولت این کشور برای تضمین نهایی‌شدن توافق با ایران، ۱۲ میلیارد دلار به جمهوری اسلامی «پیشنهاد» داده، «کاملاً بی‌اساس» است.
ماجد الانصاری سه‌شنبه پنجم خرداد در شبکه ایکس نوشته که این گزارش‌ها «توسط طرف‌هایی منتشر می‌شوند که به دنبال برهم زدن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش‌ها و تقویت ثبات در منطقه‌اند.»
او افزوده که تلاش‌های دیپلماتیک قطر که با «هماهنگی» شرکای منطقه‌ای انجام می‌شود، «شناخته‌شده و شفاف است».
ماجد الانصاری انتشار این دست روایت‌ها را «تلاش‌های مذبوحانه برای خدشه‌دار کردن اعتبار» دولت قطر نامیده که به گفته او به‌عنوان «یک بازیگر بین‌المللی قابل اعتماد در مسیر دستیابی به صلح» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75728" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YRL2figjT55z4d17EPbv3KjUKDubd-lfykJrX59GAB69PShUjn_VbYYUp6SZ43oK1vLYKwxuAweMsnKzTQxQ3QnoXNOO6Qtj9WXqZ1yWwm5psayzj1j5e7Kppa03OMRdHErLvH-8xyBa_tIpJ1H26_znO3ods37ahvPOt5WNfh73Py3g6SEAye1uMGcbc1YTUhcRCY5vh17f7Hak3ODQftr2RBWwuogU68itNVUsQvRBxa-wd6zvEdtTw1GwPULZ2C6cvjTIK7wIB4zcyrShDz8e1YkFWPmrF4qc-284tJbDvXf4JNCkwy12QUcdhceXOtgHkvHloISxWCUpr1_rVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPspDaxWzAcmBc3do959PywE4v2aG56yOQWG5msol1B0fYxM70UMCbg7jFluw-HIqONQ1dMPjK8Sc7cCvbTwGZu0bx14xyjWnBp3aXK4UIFVAZg28QZJKHxezlmPzF-IVz8Gpqh8kJktH2KcdWdLTBHIGXLiUHeD0McDUyhldsedzGi5utUzYBtuT0D-1PgASnQ89p3-QOICM_AW3JNqr5csV4TERf2-fGpBlXJ886lL_7lqsQzDayjBEnf_i6t2q8dzqQ9dCYfe3aboFFVd6poRwBVusSniLMpfMkKFXkQqmN1IoN1o0dKvPTiEDgX30jEVZ6BXSH6lRkhVcxepFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h9ewewvC-Fmn5jGbsL70LrMTg6gVBFxTKaIhT0B-RVW7CN0jp4u8ex8Ej2ZwLelni5yEG1d-DwIuSGdvuiFSuhFNHejGfRNFZv-fTf3ElzAI-W8mpZG8LSQ6jSf9YyTGM9twbo5kH92xAGQBZavnWxFxGsdMG0jZvfGqSKmc2CjB2REV-ocrIEnPzUeSLrxNmPM9rUi7orCtHNXlp9-xckJ0RlMVrV6iDraAvoupDqYSjOKZEeiDFA6fdc5kGD313-nAyuLhUZgosuaQR7psLt-0pDYnguwfQhrTVGyGPj7T-bDTU8HPc_odf5NsN7v7selSc-94BaO4S2TO6lEA4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه، اعلام کرد غلامرضا خانی‌شکرآب به اتهام «همکاری اطلاعاتی و جاسوسی به نفع اسرائیل» اعدام شده است.
میزان مدعی شده او «سرشبکه عملیاتی موساد» بوده و پس از تأیید حکم در دیوان عالی کشور اعدام شده است.
در روایت قوه‌قضائیه، اتهام‌های سنگینی به او نسبت داده شده است؛ از جمله جذب افراد برای عملیات خرابکارانه، دریافت پول نقد و ارز دیجیتال، تعرض و اسیدپاشی به خودروهای افراد مورد نظر موساد، آتش‌زدن اموال عمومی، تهیه بمب و ارسال آن به تهران، تصویربرداری از نقاط هدف و حتی مأموریت برای فراهم‌کردن مقدمات ترور یک خاخام یهودی در یکی از کشورهای منطقه.
ابهام اصلی پرونده، نحوه انتقال خانی‌شکرآب به ایران است. میزان نوشته او در خارج از کشور شناسایی و با «فریب اطلاعاتی» به داخل کشور هدایت و بازداشت شد.
@
VahidHeadline
میزان نوشته است: بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشورهای منطقه با هدف شناسایی و فراهم‌سازی مقدمات ترور یک خاخام یهودی بوده است.
@
VahidHeadline
گزارش دستگاه قضایی اشاره‌ای به تاریخ بازداشت و محاکمهٔ متهم نکرده و در عین حال وی را «از اراذل و اوباش یکی از استان‌های کشور و دارای سوابق نزاع و شرارت» خوانده و ادعا کرده است که او «به دنبال جذب افراد و به‌کارگیری آن‌ها در داخل کشور برای اجرای اقدامات ضد امنیتی بوده است».
از روند محاکمه این متهم گزارشی منتشر نشده و گزارش قوه قضاییه نیز مدارک و مستنداتی از اتهامات ارائه نداده است.
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75723" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dqxVFuGy5aE1O81AYpPrmLgQPGh_KCfzRA_nsNeC_HZ6E22QzXmA3QllJH8Ye67GUesAPgYg9ba-39RT1OdLXYoZc2wXy_BccR6O0_lB5yiuTd_4BPyooVuwpjzvPVCn7aWI7uCS2uYFA8ct2K6eysYgWH6Elr-GwsBo7u5Xib2AeggflWYXlUI8WtLPvEgPqWQKJbgy2cd7bUFVSqN9RtYiiTvAK-dStXYrd74vZeB3mFqgHCqyvGqSO_ZRO11jKUXJ_ryJseMvlbU3QjLmdiqjnhzpNNdCCL6DQf7gIyVUTpM0ZcEeMHbEBFtlromBm4aZ2ozyNdq3O_VZByrehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lPbKK-p4d8FkGYf_-AGU4cYc3bEenrHdDfUzvQZnvW9kmjzwQy6pbOooMKBn_JwNLcmg9OEqvCEWTKU8Z_bjtqRm3w1VR_75o6c5VohYGAyi0lDazC_WgHqNLMkG2NFrW3zIIu7C6uuxNIuUTCXKW9YhcEl-LUuy_2rQmM0bWbEsSht1T5IR9RlbAkQc7WSqU4a7vH997gbAQZiFZvIQmmgi1DJcuJ2BbvPOR_59aHrL6G27ddxKk6tbnL0C8K6AWVyzkmAXe6qSEoPVCnI5Rx2xi0r4G293jNwQpTHdb_H_yjBi1nq6mwL0rzOe5P7euAoDlgBpFRHi2AP6Xmoi2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با وجود حملات اخیر آمریکا به سامانه‌های موشکی و قایق‌های ایران در خلیج فارس که وضعیت آتش‌بس شکننده را متزلزل‌تر کرده است،‌ مارکو روبیو، وزیر خارجه آمریکا روز سه‌شنبه گفت که توافق با ایران «همچنان امکان‌پذیر است.»
او در هند به خبرنگاران گفت: «امروز مذاکراتی در قطر در جریان بود،‌ و باید دید آیا می‌توانیم شاهد پیشرفتی باشیم یا خیر. فکر می‌کنم بخش زیادی از زمان صرف دقت در کلمات و واژه‌های به کار گرفته در متن اسناد می‌شود، بنابراین چند روز طول خواهد کشید.»
آقای روبیو افزود: «رئیس‌جمهور تمایل خود را برای انجام این کار ابراز کرده است. او یا به یک توافق خوب دست خواهد یافت یا هیچ توافقی نخواهد کرد.»
آقای روبیو به خبرنگاران گفت که تنگه هرمز باید باز باشد.
او گفت که آنها به هر حال این مسیر را باز خواهند کرد و افزود: «آنچه در آنجا اتفاق میافتد،‌ غیرقانونی است و باعث بی‌ثباتی برای جهان و غیرقابل قبول است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75721" target="_blank">📅 07:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwCfQxhnsdUuYvtQhN-5c2UbqbcHUAu8zc7TOPDrP3hPr4t6s2CwNUzWWTQ347YQeWA2DWvF2VkuFBavfEu620fBj92lqpY6uaapzWNaEvot_5LbgVS3qHP_gF0_phW58c-5Hd0N7C8pdOUyDYMWZ_4XfYz_Z6N-0TXLqxeRCUWSW-_qAA7ryJTFB3hS3kMiEZIlWMXemfq4jhhh59ptlh1tE0pUOEHcE04DQBzL7nEizhnWeQNMq6QVPX4bYOUcnM0KIF-VHXbdnD1_t9VA0_a6i8La4mJGdZvQD6BnkTRhXnCFCjRz4Ujbaa_bSbAvqcUmGNiiQIlGpqGNFMdLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اواخر دوشنبه به وقت واشنگتن گفت مارکو روبیو وزیر امور خارجه، به در خواست همتای روس خود سرگئی لاوروف، با او صحبت کرد. در این تماس تلفنی، دو وزیر درباره جنگ روسیه و اوکراین، روابط دوجانبه و اوضاع ایران صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75720" target="_blank">📅 06:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/veNZFRal3m-ucVQU8brAXee0EIR2kYGBzP5DtuCoiRf-6WvRmA5WLCYtQff5qUEd65tL50F5v5ABFKdFHhJTPFX4XJvWCaGLMskkBmwCDnEduE77D-xyeIgkXAkBWlXnP35TKHRqcvLsm9eGqSgsTrPKiJG1JG0AruGzYb-9nUS1S0bMZRe_o3nHw7MU2482-E9Ls60rWFLLnKa-FDfVp8ScFVnJ4dXj5rEOz6IrkFtJGzJnOdMnaLaK2fip9esniROKuPOdqDMVRRNtUMbbLgu7TkBdxeT7ob5y7c8tt1q2ok-DV54Me6jOWaiVUp9r6-d0Rr0jQT0QT3mKTwN71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75719" target="_blank">📅 05:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNoie5k5Dm6XL5HPodzpyjG4kjwRxBbst-yirD5D6eTU0Od5k03l8_uy2cP2EmmE8WWdTsoQOtGjvmpnPxPlNkiOCZvnkwbznyd-zNx-F7oTcsiDex_INBMXW4a47oGxC6Fd5eT-CMW_rzvj83B6TpR6gT8YxYfdKUPvrAX2FEAO5e7cnw5ibd3bePLtEHTCX6WLl1HEHD-azIVoR1BW-IUgwvLPfUiODkJ__j9GiWma_nTMnFEulYT5OWilC3MvEkeJ0peNy2hjezYIzTOXz3iWJhpdLeXHBf4b0ZxNqV3Nv5ltOQvpBX0XBux823YAb9C0Kq24TfacFOMLzUkEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رماندهی مرکزی نیروهای آمریکا - سنتکام - در بیانیه‌ای اعلام کرده است: «نیروهای آمریکا امروز (دوشنبه) در جنوب ایران حملات دفاعی از خود انجام دادند تا از نیروهای ما در برابر تهدیدهای ناشی از نیروهای ایرانی محافظت شود»
در بیانیه سنتکام آمده: «اهداف این حملات شامل سایت های پرتاب موشک و قایق های ایرانی بود که تلاش می‌کردند مین‌گذاری کنند. فرماندهی مرکزی آمریکا ضمن خویشتن‌داری در طول آتش بس جاری، همچنان به دفاع از نیروهای خود ادامه می‌دهد.»
ایران هنوز واکنشی رسمی به این گزارش نشان نداده است، اما برخی از سایت‌های ایرانی از هدف قرار گرفتن دو قایق تندرو سپاه در نزدیکی سواحل خلیج فارس و کشته شدن چند نفر از سرنشینان این قایق‌ها خبر دادند.
نیمه شب دوشنبه به وقت ایران،‌ برخی از ساکنان بندرعباس و شهرهای حاشیه خلیج فارس، از شنیده شدن چند انفجار و فعالیت پدافند ضدهوایی خبر داده بودند.
رسانه‌های رسمی هم این گزارش‌ها را تایید کردند اما اعلام کرده بودند که علت این انفجارها مشخص نیست.
@
VahidHeadline
درباره همون وقایع ۲۴ ساعت پیشه که اخبارش تازه داره منتشر میشه ولی بسیاری از منابع جوری جلوه میدن انگار مربوط به ساعت‌های الانه.
احتمالا
اون پست ترامپ
هم که تصویری از قایق‌های مهندم شده با پرچم جمهوری اسلامی گذاشته بود و نوشته بود «خداحافظ»، در اشاره به همین واقعه همون موقع بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75718" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CbmcvFKR-mkpnapaM1ugZno5-Qp2TL22_b07TG67BW3sOmSHs9UvFn6tFMQuAavwkP86TMOUJHuDSYiP0dk0jZmRzhCCKDHPbVmsNIafNSGkFsJFg7I0cW5_TDsJNvLY634LQ8fnEJWPbtI2UBblHgNFqKZbo-tynVI6CAWLlWGkBYZeMTT_22nIWCS9k8upXp4ljq5fSG3qymT_JgdXSmikn31w-XlJHfaV_MiQcuOzJkEBDhql5PnRJFZdIpDvnxk9mXtIFPT0UZ7kt6nGnHdzPur_gMvrbAlsfrONHoaRmTwwYwIZB9Wf0YiuiysmuLRwkoskEaOcbjh9GVHPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A46yoDppEEq3lS1QB1lTj3XNJG8yGJfQNwir5ohZB_gRcFrvlkn3Ye5NE3X3mO2Sl8874AN6mXiZz4aIpB999LAxpWA5wJG-XXSsZvMezgf4u5asSlOLhqjquTS3fP0SA9nAwj_AHXy9ZjXvhJSHvamwqp-K9op8Ktfhdb6zn7DhyWMH0UO6q0Fyf_v0FCcjXRlOln6klqImOvRro-TVHA535QZm7yEsJddGCuakWBHqAl_c0964yU6j2PZzqaxiGEwZOjK62-hcdbWPxZRd73kJj320Uy69U_wy8pWJfo03bZLD8Us1J5NcW92_wV2fm53Zn4-Kw1vNL9iPVchRTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
آپدیت:
پست بعدی: آمریکا اعلام کرد که ما بودیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVJLaruGVa-Ju1NIKS9QBMdu4qEeGaTRaYvyqwtptQvSbOyjqT4axbkt59lGRe7V82dK6GyzEwBcqxTVWN7F0PzSSpVY3tNRBTua2JZdX_HbEqHWhtg3wK1VXwixnZC3ZQHpJC7nl1CURoN2ICbqn926xaTMugsMqWk8NbdXclNO8KPwvLniRj4C5GwOL_lF2soLpfgGf2efT8pyJU65lFBq20dRluqwdxrhgoW5J19W1O-hGvct_9i7aF00kSW_J6Gg7Lv4fWLGCylcA_iIIdk8eoUO-QS-A8CW93kNIVOvmXKMXHLxZ9fy2xPxQGbUubjvIey7qWucccLEenPlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اورانیوم می‌تواند در همان محل یا جای دیگری نابود شود
ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
آپدیت:
کانال‌هایی غیررسمی نوشتند که به فرودگاه بندرعباس و اسکله باهنر حمله شده. منابعی مطرح هم با تاکید روی غیرقابل تایید بودنش نقل کردند ولی منابع رسمی چیزی ننوشتند که لابد مذاکره و توافق به خطر نیفته. تکذیب هم نکردند. حتی منابعی هم مدعی شدند حملاتی از سمت اسرائیل یا امارات بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=YWo-n072wa6DKtStys_EUt2QQiuZ2SBJ6WptnZY2qPXz8Q5_3BE_JeCvY8Df-uEWFHpjdbP4Ahz-xOm8yPbz3VsgFvFBn-Me3ROYzAAEQqijDhJQwXS8nuvomwGVY4gevj9ziwqFZFvf5CPGbLuwy76_Dobzcsua3sk8H_iHYkj6WjIdO1PFl4KBHdvVubf_e3dqtasq_BahPf3DMhe74cwAbw7KdCCHwlxfEGnZyziwfolzT_EcbuNEctV-ZlNLR4rwWyVkguq86krLLOaPJ5rBykCI5Rcv1VnCeypZ49ZrX39ZwCM33jLNZQtamm-2nCJkHSBH1uXXNcim6s9NOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=YWo-n072wa6DKtStys_EUt2QQiuZ2SBJ6WptnZY2qPXz8Q5_3BE_JeCvY8Df-uEWFHpjdbP4Ahz-xOm8yPbz3VsgFvFBn-Me3ROYzAAEQqijDhJQwXS8nuvomwGVY4gevj9ziwqFZFvf5CPGbLuwy76_Dobzcsua3sk8H_iHYkj6WjIdO1PFl4KBHdvVubf_e3dqtasq_BahPf3DMhe74cwAbw7KdCCHwlxfEGnZyziwfolzT_EcbuNEctV-ZlNLR4rwWyVkguq86krLLOaPJ5rBykCI5Rcv1VnCeypZ49ZrX39ZwCM33jLNZQtamm-2nCJkHSBH1uXXNcim6s9NOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YclZtkXTfnSQ7-RSFzDWFpwfANwTpO3U8Ev_4tJPi_G05CALjltpBzs3kCFQyRhtE1jGn5P5c8t9FCxkxWQdmblmKxgnvrEZ7Qvv7sYGebv9p902X2Bw9RlNkYF5pNhtEkLl1kndyFlpz5pn6RZ23vL5lRUlFnubrCOjrrlUHEzwZ2rssr6ncN0vm0Z6Nw4zhv-LhCyzjwbT9nUDlN_2DMPqRuNwOm3r0q17dElzYepesTl9Dxu-Xn5riRzKHNmFVpQnywUmuWWZmkg5VNd-4vxhS0bn8BRfOI2muUMQIECkp3H1h52pYQpMTlKeptE5aIbx0pFFEAGEK87d4QLV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMK_okgg8p0PXvFa9p7ldGvJX4MqGM3DKccJDxgqZMpOTvEvH04_JCEtPaYjK7NcniPJ4cBiQXGdPUE-Z1-DcF7D3fLfeNkf_9vYzLfyd4Tq3yMXxXJq0KXdf5C3gCp_LbzX5ootoApAyIMJQN3PU-pmJPEQYSmb1ia29y5SMudwPy4qQEhqgm-1JrFQ0auR9TlT9oNysE76ArgVKe5tDZZZF8VsBd1WmVKoPfEMfABiglXDsStxDWFj_KlgoXhu6dTxKHUzBneuPQ5TQqeJVmM1hX8mUAr8jqDC5IHDcxwI6drU7jpdTV18zYyqfuX6dH0OveKTAIKTLd8oXu11rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZVOztA6dytv3BF0FVoWysLO9MXsvkhboYzrqlrRoWaV9qoAwLQWsunTs27yup0WYrGnwpKGT2gWujQ_QFqwcmMZdP0e7y7LYli6kYz5y5L1aJc6TCQMGpbIrpVyz5B0Z4iuO2Bwd5Weq3QRFCZ7tCvOigVFOOdt01co_9U207TdP25LwvNmG6P3-Pb3jbmZ_X-mXAkJi1KBUZyQ7OljggT74P35VOPNrXPGG6NdhOMIgTSa6Hfv-4lij0OvdQzrpE7wjpLcwvl6c-JPAist0uGxe1OAn0Ebnh3dK6kXXWTIsd96BMUDoEjHWxEfBESeSHroLHya_mdPtxXTK62MkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dLpcI3k8C9srxL2HR6uZlXzyS_uyTkd35hzdIueheSI_mEsTrtspICK_D_dMuC6cB8O6zwcmbEmWwm45otRW6AUHMN4vl5Xx_k8xobXv6YGkktRmILOlDnJAi11oioHNv8gf0cR2KEmuCCSrcqwF_gKcWqQH-fu_ccqibeF2-aIvV7zt7gWsERDp35WBpoeWeX5dHSGE6XLT7nccHD1cp9S8zIq7bEYdXwNZlklMHNon_DowBZZbosE3t69uPDezah1bJefYLypox0wLMG-GTvwuj4Z18GLqFc2X8uQQVyw9gDHRzXl1LuwJaNzn8sfzQzp3qFxW_wRRLQlrwRnvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vtDmOsVjGOsSWtrVjT9i9qaMHVYaLiCv1JF9irL4aQDaiLkXbetiavaTXbKHjzokEyzG0oc83A4qbSn5PtkeEjPUJ0LomFvtmPJDkKlAMf22a2dBjCUljQO1WU-17YvsZ65T0_vBJp-ToNJeN8VvTuhdKGjEBsTaKyUtKhiGQg8s-4j2vqGwl2Um4pE4EidAkO6MHrUdTeXMjDifAqLQAX0W3-oAPVXjfAnvOolinCGVomq_5zS-a2Jk6iT_30Vg-L50mL4nKIn93Wzlvfthy9sYpos_Yfd3_Jqhxlb_ZezM9vpmMLTFnt0kDYBhT_OyJQkkCQpqXSDfPhPW1Sm-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pb6T6zYflqzyrMYv_TgZ4nIGum_khQ7-nBplJ9v31nkZS1XkN0W2UhmnL4Ku22A9u7F6lV6Db1M87r70Ijq1vJ30M-hScSAPFZklwvS5YXSZ9mXHWNFxt2WQyFPpTvxb6uU-rHbvbMBQBelAp4LP_R-vxySgmHbp-GuceL28aFTYV9_ui0CiZ6WJS1qUB1PZqdKPGMhSmsOyVPt1ChX2TXlVlLCVGbkt3GM8Nfxr8DvNJf_Mo6KdH_KeuBFTsuQK1AhdgS00SQcVfUAn5Y4loPlmBPxKbMH9PItHPX2fHWuTE0a2FjIgegAfy1QNw4QT9ORPQnDnlmhq7ZB1Wcd4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TmHapuxTACWdyrK3JnuOk5nmZvKVU55AGYfUE2QncIEAOL6_QwvbnJM_aivEOjY2gOwY_nS2YQTnAlHCSoeD788GZTnu0-dK5Wi_mmKkgNu_pQLcto4lKITellOD4PiRXkfQXJ48bFxhvZd2FJildTNThwI3grkkjgSnMo2nvkV9tf4tRZUuQkkzkBnSQCaZZyJiNi44MSqFxxVfZzwOVu5XVQ9OzsF7IFqhsJ9GyCoOmxP5uBlt1yyPNhzQ1fcHwFks_nIBCVEFtJ7wbnJcUvWJg6fNlwRWWgzNI-SY1uSAWg1pKB8qFm-StoNXRPAOepIP-uE2EmWy-9HFycDMyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SL9yKy5onnQXXtfkJUXQMm0CgenNusq4A5Mf6rYDJCUcZcpn8n-s3zSpyKdjgqnhfXjAkEsrQQjYT6imNRoaJVwhU6FTQiYUaSvFIl4S_WHaEQezfpFWZR3WtyaAWd55gp0Vjo8t6FOTAdRHZvxYsATqhbg_Ih8-16XV56jY5cRSSLGhzDAEg69wQsWFrpX1XWaz2DEXZqFwDbNHOM6jg3lL_df73SZrlC_aLVU1WgQw62gFLleZ-Twdi9vkW0wQR2dhx5UDb2hlCo-Q_dsa-m0l_GRevgVIsrAPfwYudYZKE8sHvp3zyOqfGagQkpvrezwsb4_bghTyqOYRHj1qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H2Tb7JIWQ8MwvZ5Kf2hboAVkZTIxAcd2V46RJn3jXiDKgpTwXH5QhXXVxiAamX42ast9fJLlGvOoz-SK5RQO6GAx99HYrL_Yf4SBsq1S7oRLCpj30QxQyvL4BceH1AMyPicNjuL1XYUTq2nXIG13n0vsPETJ2kfyw7FoibI4XU97UiZ45rsAIRJMGDii3-iMb5BdkSy34sRnxi0xYxv-2hJSJrbEGAbYuC4uzLgdwPceNcybgN7dKlc_kQtpKK7os767k9CZ5mZe2a-iU-SFCJXkSMeb4YL8JErLt9h7ZAhI0-2IMeW-Sv-CiNqn7mQIK3XJBRtODeZGNQxV5A-dkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Igw1rEU1OSfiDAwY1_yYgCAxjp4dCaR6evEcnujsrymHlT_xrXRY0S_QAwyZI41FWw1TbaZ8yzfNWHPD3GwumL5es3ZHa5S785EVZ8Eq0axU8i3zZWT4vMOBSCygOTHzU4lU2zDtIs-X-d5nbXpvNZGNLWuBDQl1Vr-KM5XijNeTZiDt9E8eth9KgLVEQsvfuJ1Zrhnb23rEgeUa2dTQ_VW2k0PE9qNrxdwJZvhi0yN0USn1rBxMaXmPtiRYLEAPVd9i4gIwjg8bKzzFG1s16qgY7sT6uX_Tqo5cbIlDWELz0dVfDxyPGuJffkHWxfDHT-l3xNeWUdiN2noCzZex1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XzlUsLAiadfytf7KGdF3FBfFMyq70-O7OHvdsXtWAvYsn7EJahc8fLnsMVp6KLCdZEpOp_YBDmFWahCuMGXsbZ_Tn3tYQ_GKJdvokXZf3udRP9WWXvk-PtTTMh19z_JcA7sIhsHBNHxrNXNYysW2Yu-BA9XqGS-oZZIlt4p5Cq7HA3fEL7Nl18X0qLO9bz26WOqL-Capf5B1WvD-1t80L70Q9PGTwuI5cFCW-aVe1zGcwNv0V5DnCP5NYoFycvbsOP_OYbG4shFS_6cMAFmoZTvhIaHA5llZCujItI0kTbqURscKmN3MCMXUPXcqOoE1H9j9c2db7zJtePInEc8R3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL9reJ4aer9hc2bDE8bDpAGbSDllecMsc3Nnf5XM3SKFSQXMRak70eCQv1MPII5aPNPpZ8ohGcNkFXKP1s6BBD-8Bh1YCGEYfJKF07y-1RG0olrRn_fOpSh2UTEagbs92MgAXF_L6fJ4csUBOsYBJGxqnNat2f6ZMqBB0X4nJaasIyg7000p43gfyWUE9QuKGErLgPR8eVfj_BBtEFrpMczu6C482nAkv0P-tswVdNeB3XQsh_yZJ1NU0bvHyCVs1Ohv_BLe4Mv9lL2otc5rp7cpWQ6TVGWqX_QjbfBvAAR8AdTKA4ijAlgLo6oBjzUXxBX-7rdKwvQOgHdxC0UmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKxkQOwyCrqiYxDCxkXTgzZt854fNMw5i_2ersmx_-lo3oIvR9dRXSI2s568rl4i42DXZU8liF4PuInbhVTzZs8Roe8JFSAfyKhcBVCeSFXhB3o4-o4ZOGjEXoGV4pcypHnh3CbsJQjuwC64oNeJj8M0nY9DXhBjZOBHJ6mh9pb1LEmMAqu72TOtkg1OCx9p1Ajpr2rvRMkPfemAUDm6H_R5J8BW1RxcLTU6iH5J_EX6HKlq1-Y66v_a5l3Gl6DRag2QUwCrm48MrMraTaKbeMe1hMtRdzkzKKZK_PaL9dMOAdqqtadyCciI8gDpJc1jrynQ8bvqA_6scXoiK4aoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lEcwDLell-2nPFESEhPdIVCtmwpkjYv6C2brMrkWEl5C5oIeu4GLSmdhzV2seRdln33nkTC_wbKsEH3mqC7koJi1EYMAfprMEQlE-IzTlIv_scGDxAMOOSeLu4R08h4ohqU_pHqovQFxqvnFkSsbc94yq6yP26iEPk9-GNwda2Yrqg53pWHQw3JBoZzG2XXgabutG3LAnLrsl25fgIpDKeOEmw_wxLiUZyDIYiruPRqkhzGe6MAYZysQmmdjiESrYsv7DyvrjIE-1usn_YO_UASJMwwbx7C8h4HmNroFro5q0nOdtwZVbkvmrJrvKLc5-NvMchCcYzG3NRg7fKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmCOMKlL7ZzmixiukIMZZJowraAGyc7j8DbrUTjbcom69Xdr3Vtsu8DuKTioV6WO0XDLu4Kz710mcJgTq-P3ktXYQ1QEzUGRt0m6bHq0DevjQpyNIoAfftQlfzaJx797bNhyGXjEoNBOnBeoSyZYuw9p1B_pcMMAeFB7MBJqOvpXNI1cWoroOtA1uQuO63r_Xeb9qXznnrQdnyXv5pf3CKu3KJQkz7DC1r3nu_rHRruXDNxh8FDPKSUJQIrosRyyycOtxTJUgnbFpVlz7rJeaDkawLsT5E3hnZgFxwNDOBy_4UVM4GW8IEdh2Olqbra0GA2KBXF12JWprkyj2USX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdNqhUuxvxWlWkDFf8owit9vHHFR1iCfNZ7KObnl3JVNfdvIWo9zaoIDvoMthE5Mj4wA7m-gJri4bOkiqVEEQuv1zx7m3rNc2piG2OTqaWO9YiY5qtyoflyop_F4-_ofDhbtPCKCrSGUWf-Uo_7Yu_0kHkTdNhXlpmdBR5wi5RSzBC8WR-45cCrVZUuxiIDd5uFLq_Oq6L1Hjk_R8Tzm3WtSboHslTztDTHvUNZ4OP_Ry6jeXQ8Gp_CLjopE_gkjDbNzLe6aNsqThH7Sqn80Yq5nkThvWxJKSFjZphDE460iBeXpxiIChdWiGoyrr4SZw9g685qVn-xzqWlAty0dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asw8GX5G4iwSKl8X24Mg5EvVxR9G2DEt-TPYQnA7IyNji0rUaKtI5cwB8I0eaPI-7FyJmcnNSpI62PaF_Hc1-4KV1UGJKTOMNOhwmDhQYw3cykPEqTfyqqhQWyZVwDvmmzipiJmCL5oLNePVSuphk6o7hNuRNBEoEiJJ5HAHMHPSO7zxPQP3tCohsRYumqpq0gLrCL-28jjbWl-WIsyj1zzqp21-6fCviV1SvtCKHLG_b36I-MVgL4pYRtmQcc5ZFCbQwdFL_lB6YTr3PJvGGwQhCvstP5oA-iznDQcNfWusgm0CwprsR_YpvI-pVcNqAFJ8IqAy3RqvzJr7ZIFkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایالات متحده، روز دوشنبه چهارم خرداد گفت که واشینگتن در مذاکرات جاری خود با ایران، «هر فرصتی برای موفقیت» به دیپلماسی خواهد داد.
مارکو روبیو که اکنون در هند به‌سر می‌برد در جمع خبرنگاران گفت که مذاکرات با ایران همچنان «در حال پیشرفت» است و خوش‌بینی محتاطانه‌ای نسبت به توافق احتمالی برای بازگشایی مسیرهای کلیدی کشتیرانی و از سرگیری مذاکرات هسته‌ای ابراز کرد.
او که روز گذشته از احتمال توافق با ایران تا پایان روز یک‌شنبه خبر داده بود، گفت: «همه ما باید مطمئن باشیم که یا به یک توافق خوب خواهیم رسید، یا مجبور می‌شویم به شکل دیگری با این مسئله برخورد کنیم. ترجیح ما این است که یک توافق خوب داشته باشیم.»
دونالد ترامپ، رئیس‌جمهور آمریکا نیز شامگاه یک‌شنبه در دومین پیام خود درباره روند مذاکرات با ایران اطمینان داد که توافق احتمالی با ایران «خوب و درست» خواهد بود اما هیچ کس درباره محتوای آن اطلاع ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75695" target="_blank">📅 09:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPReaXxfodL8VyKVX0p6eKwhky6WIzduqZq_dmHpMUVCez1WQ6naUGuRQSBdiVHW84kFrSIIijdGIgqJhrZCk0oV5YWkbRDofMbOxTO5F71jHa01ISGe-u6Km88siNWan79wuYrSCltrHmIMz0Hykm3xBP2MWcygcSJBB-fl2ma5N8ZQQ5lhCV3z4TYW6VYnOLh_gNTsthuXgOJ_F2J0-zjsfxqnLggFuPmDzOoPEgt5aBF9HNwUwlXJXiKWh3BM2WketaKB08TqkfaaOK2FZm510kK7dw4TpIxTBR4SYdB4Pz70Qgf0rkFRlDSiflvc6gW8e1w4R2pb1OlfqMuHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم اعدام «عباس اکبری فیض‌آبادی»، از متهمان پرونده اعتراضات دی‌۱۴۰۴ در شهرستان «نایین» اصفهان، صبح روز دوشنبه ۴خرداد۱۴۰۵ اجرا شده است.
«میزان» مدعی شده که عباس اکبری از «لیدرهای مسلح» اعتراضات در نایین بوده و در جریان حمله به فرمانداری این شهر و برخی مراکز حکومتی، به سوی ماموران امنیتی تیراندازی کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75694" target="_blank">📅 09:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGQl3weRZV-uKWjIMqrJmGmu1rosy3kTzFnBaF_sJgYdOrs8bILu7jz7N23_iIBcy9ZAuCsMT-NN3lJFYEpqN6x7LAdgt66epw_FLqMNNddqgCXz1AH-KdlG4bx_AsbEO8MU_4VjPW1DEIcn6fkrZn0GW0l44fLbwG9ku_JdHzBNAeA_r8n8EhSCJw0UTtW5f17nqclDnPBlic0WD3t4_QxJPYgf30iLZq_Pw_bDK2RvSyJsmhXxPVMdSgFsfPxLKVSQSjlqEI7zAsHmanLDY5sjrsXhFbuhurrxIj56RXWOr2TGdfAVteBm7YJOiHe-YlJN6U-zJnz6XDgFCWMlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: مجتبی خامنه‌ای در مکانی نامعلوم با دسترسی کم به دنیای خارج پنهان شده است.
ترجمه ماشین:
اطلاعات نهادهای امنیتی آمریکا نشان می‌دهد که رهبر عالی ایران عملاً در مکانی نامعلوم پنهان شده، دسترسی محدودی به جهان خارج دارد و ارتباط با او تنها از طریق شبکه‌ای پیچیده از پیک‌ها امکان‌پذیر است؛ این را مقام‌های آمریکایی آگاه از موضوع گفته‌اند.
به گفته این منابع، مقام‌های ایرانی که مجوز همکاری با دولت ترامپ را دارند، برای برقراری ارتباط در داخل ساختار حکومتی خودشان با دشواری روبه‌رو بوده‌اند؛ مسئله‌ای که یکی از دلایل اصلی تأخیر در روشن شدن جزئیات توافق احتمالی با ایران و توافق‌های قبلی بوده است.
دو مقام آمریکایی گفتند وقتی آمریکا جزئیات پیشنهادی را ارسال می‌کند، دشواری دسترسی به رهبر عالی باعث می‌شود گاهی پیش از دریافت پاسخ از سوی آمریکا، تأخیری طولانی رخ دهد.
سخنگوی کاخ سفید از اظهارنظر درباره اطلاعات مربوط به محل حضور رهبر عالی یا روش‌های ارتباطی ایران خودداری کرد.
یک مقام ارشد دولت روز یکشنبه گفت رهبر عالی با چارچوب کلی پیش‌نویس توافق فعلی موافقت کرده و دونالد ترامپ، رئیس‌جمهوری آمریکا، در تروث‌سوشال نوشت که انتظار دارد ظرف چند روز آینده پاسخ نهایی اعلام شود.
مجتبی خامنه‌ای، رهبر عالی ایران، که در حملات آمریکا و اسرائیل در عملیات «خشم حماسی» زخمی شده بود، برای جلوگیری از حملاتی مشابه حملاتی که به کشته شدن پدرش، آیت‌الله علی خامنه‌ای، منجر شد، تدابیر بسیار شدیدی اتخاذ کرده است. علی خامنه‌ای از سال ۱۹۸۹ تا ۲۸ فوریه بر ایران حکومت می‌کرد. مجتبی خامنه‌ای از پیش از آغاز جنگ تاکنون به‌طور رسمی در انظار عمومی دیده یا شنیده نشده است.
یکی از مقام‌ها گفت اطلاعات به‌دست‌آمده توسط نهادهای اطلاعاتی آمریکا و اسرائیل از داخل حکومت ایران، امکان شناسایی و حذف بخش بزرگی از رهبری ارشد ایران در جریان جنگ را فراهم کرده است.
منابع گفتند در حال حاضر بیشتر رهبران ایران نور روز را نمی‌بینند، هفته‌ها در پناهگاه‌های به‌شدت مستحکم می‌مانند و جز در موارد کاملاً ضروری از صحبت با یکدیگر خودداری می‌کنند.
یکی از مقام‌ها گفت: «تماشای تلاش آن‌ها برای فهمیدن این‌که چطور با هم حرف بزنند، تقریباً مثل تماشای یک سیتکام است. آن‌ها کاملاً به ستوه آمده‌اند.»
شدیدترین تدابیر احتیاطی از سوی رهبر عالی اتخاذ شده است.
بر اساس طراحی این سازوکار، حتی مقام‌های عالی‌رتبه حکومت ایران هم نمی‌دانند او کجاست و هیچ راهی برای تماس مستقیم با او ندارند.
در عوض، پیام‌ها از طریق شبکه‌ای از پیک‌ها منتقل می‌شود که با هدف پنهان نگه داشتن محل حضور رهبر عالی ایجاد شده است.
یکی از مقام‌ها گفت: «به همین دلیل است که می‌بینید برخی می‌گویند: "رهبر عالی با چارچوب موافقت کرده" یا "منتظر پاسخ درباره نکات نهایی توافق هستیم." هر اطلاعاتی که به او می‌رسد، از پیش قدیمی شده و پاسخ‌های او با تأخیر زیادی همراه است.»
رهبر عالی در قالب کلیات با زیردستان خود ارتباط برقرار کرده و به آن‌ها جهت داده است که درباره چه موضوعاتی می‌توانند مذاکره کنند و چه موضوعاتی نباید مطرح شود.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75693" target="_blank">📅 03:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bzEFO_3hErYk07kGYacpRIrPfZirHEkzRHzewLPeEpz6bS0gJRT4BpqILl7xIBNz6UDXgVjQuLfoMCG6FKi1DpRu3n0SvykCS0iEguwwXw1BVKlCntkWDUrIHfNYqso3Mv0t9Yx9hrYbke1MHVEmgKrw9PAj1PqeZCeFBTtkRwUTTWfIttHfdgfYKDQYKh12VwpMZtDuudvGs-yvOtDJnVWRfHJIP3pwP8r_9_8YwgWtPkoQWoy647Z0ug1re1fYib6rWnDA3zxUq_UG5LSa3bvTV1aW7rgFX9xAMgidyyMGrhY6xVhxxQbmj7Rdk9cmTiNorV7Z-4U1WNRMyT5MeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HQr6gSa8IcxRneZ6mGrl70zybEhz0h_k1_dN_aksUuNfs6rs0VWk-8qzXMmDmlK42dfJo0jsbMemVVfkhm0yR7r1m_XMmUb-FEYTFgQi6wU3cqCFbYsqE_WVIhaQbpsM0YszulD9Kbk22Ctlr7mHuFDgDwWgTTtE_P_fMYkG7bGEkYbInb_crVz1_XYaVgWl09ZF1ytE-g8iuYWLf0nbv-Nk6tjctZyETlODhgS2QX9z-790z1Fihwbm49BXpYhUEqtXKyKR4v7yFvUudx0P5DdNhAwwFtiMXYItOGtR6QrSi8pLtMjgfEsC8yXngdF-gt1Z_3bX7pRiwsfPnG4f7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با شبکه «فاکس‌نیوز» اعلام کرد که واشنگتن هنوز به توافق نهایی با تهران دست نیافته است و هیچ توافقی امروز یا فردا امضا نخواهد شد؛ این مقام مسئول با تاکید بر این‌که آمریکا تسلیم خواسته‌های طرف مقابل نخواهد شد، افزود که تمایل و تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، این است که یک فرصت ۵ تا ۷ روزه دیگر به مذاکره‌کنندگان بدهد تا توافق را به مرحله نهایی برسانند.
بر اساس این گزارش، یک توافق چارچوبی با ایران تا روز یکشنبه تا ۹۵ درصد پیشرفت داشته است و اگرچه دو طرف بر سر کلیات مربوط به ذخایر هسته‌ای تهران و بازگشایی تنگه هرمز به توافق رسیده‌اند، اما چانه‌زنی مذاکره‌کنندگان بر سر جزئیات و «ادبیات دقیق» متن این تفاهم‌نامه همچنان ادامه دارد.
@
VahidOOnLine
تسنیم، خبرگزاری وابسته به سپاه پاسداران، روز یکشنبه به نقل از «یک مقام مطلع» گزارش داد: «هیچگونه خوش‌بینی به آمریکا ندارد و رد و بدل پیامها از طریق میانجی پاکستانی نیز دائماً با در نظر گرفتن بدبینی به دولت آمریکا صورت می‌گیرد».
تسنیم به نقل از این منبع در ادامه نوشت: «تا این لحظه تفاهم نهایی حاصل نشده و چالش در بعضی بندها ادامه دارد، اما حتی اگر تفاهم اولیه‌ای نیز صورت بگیرد، به معنای تغییر نگاه ایران به آمریکا و اطمینان از اجرای تعهدات این دولت نیست. آمریکایی‌ها سابقه بسیار بدی در مذاکرات دارند که بدبینی ها را تقویت و تثبیت می‌کند. پس حتی اگر تفاهمی نیز صورت بگیرد ایران در طول روند پس از اعلام تفاهم، اقدامات آمریکا را زیر نظر خواهد گرفت و در صورتی که آمریکا در آن مرحله نقض عهد کند، ایران اهرم‌های خود برای مواجهه با آن را حفظ خواهد کرد».
تسنیم پیش از این نیز از «کارشکنی‌های آمریکا» در بندهای تفاهم از جمله در آزادسازی اموال بلوکه شده ایران گزارش داده و نوشته بود: «همچنان امکان منتفی شدن تفاهم وجود دارد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75691" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rf-VBF7m4elX5sh-rFV8VAxjIw421rhI4JzSoDLXdKqD-d-mXs83f8lfvYVJK7FXZ-GggDI8icjMHHiVYZx9aj0khl9geSSKXu58q69YAinIsfM62xcVLNWD93JQtM2u47NVv8H5g9FUc09GCqAPRciiBca_sTBxSSC9u5lQyHEfRIbFfAvN8uh9nDtPgYGajS51IOqEmE2VNM2Mk9O8aaqF4NSMnD2gMRZt3RZ4kgzYf_hxN43GSc5nRTaj1cIObuJFuQpdwrOaOuR8GZLRH9g4qCyFcdbUiABqzGptMk4p3W4Z8ptll6U-TLC8HDS94AoaJMvWwbhNVbeRP4oSNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری حکومتی تسنیم، شامگاه یکشنبه سوم خرداد ماه، به نقل از دادگاه انقلاب تهران اعلام کرد، رای اولیه پرونده موسوم به «بچه‌های اکباتان» صادر شده و طی آن چهار نفر از «متهمان اصلی» به اتهام «افساد فی‌الارض» به اعدام محکوم شده‌اند.
به گزارش تسنیم،  اتهامات ۹ نفر از متهمان این پرونده که به دلیل کشته شدن «آرمان علی‌وردی» بسیجی حامی حکومت زندانی شده‌اند مواردی چون  «وارد کردن ضربات چاقو،اخلال در نظم عمومی، اخلال گسترده در امنیت کشور، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور، توزیع کوکتل مولوتف، وارد کردن ضربات سنگ به آرمان علی وردی، ضرب و شتم آرمان علی‌وردی و فعالیت تبلیغی علیه نظام» عنوان شده است.
بر اساس این گزارش، دادگاه انقلاب تهران متهمان ردیف اول تا چهارم پرونده را به اتهام «افساد فی‌الارض» به اعدام محکوم کرد و متهمان ردیف پنجم تا نهم نیز به حبس از یک تا پنج سال و مجازات‌های تکمیلی محکوم شدند.
@
VahidOOnLine
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی چهار تن از متهمان پرونده «شهرک اکباتان» را به اتهام «افسادفی‌الارض» به اعدام محکوم کرد؛ این در حالی است که دادگاه کیفری پیش‌تر اعلام کرده بود انتساب قتل به متهمان به‌صورت قطعی ثابت نشده و امکان صدور حکم قصاص وجود ندارد.
خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، روز یکشنبه در گزارشی تلاش کرد صدور این حکم را توجیه کند.
بر اساس این گزارش، رسیدگی به پرونده در دو مرجع موازی انجام شده؛ دادگاه کیفری به اتهام قتل رسیدگی کرد و دادگاه انقلاب به اتهامات امنیتی از جمله افساد فی‌الارض.
میزان مدعی شد که پس از آن‌که کمیسیون پزشکی قانونی و اداره آگاهی هر دو اعلام کردند تعیین فرد وارد کننده ضربه مرگبار به آرمان علی‌وردی ممکن نیست، دادگاه کیفری سه تن از متهمان را از اتهام مشارکت در قتل تبرئه و سه تن دیگر را به پرداخت دیه و حبس محکوم کرد. اما در مسیر موازی، دادگاه انقلاب همان متهمان را به اتهام افساد فی‌الارض به اعدام محکوم کرد.
به گزارش خبرگزاری هرانا، میلاد آرمون، نوید نجاران، مهدی ایمانی و سید محمدمهدی حسینی چهار نفری هستند که حکم اعدام برای آن‌ها صادر شده است.
چهار متهم دیگر این پرونده یعنی امیرمحمد خوش‌اقبال، علیرضا برمرزپورناک، علیرضا کفایی و حسین نعمتی نیز هر کدام به پنج سال زندان، دو سال حبس به اتهام تبلیغ علیه نظام، دو سال منع فعالیت در فضای مجازی و دو سال منع اسکان در تهران و البرز محکوم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75690" target="_blank">📅 00:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bR9KDy-s3mEQQaRXvHJVEgax22KG-Bg4vqU4b77nFGCYhjEn0l48khvzdxKPg5a1A6ivf8ciRF43KkIzMP_MZVgR1LW35pA7M17wFQ_puzIuco2MeTogD7jx-QK9VvtgHO91Bf5lfoGL0jThI6FOp8HZd9RcQq2BvSkONJSdW4G0rqo6GOeOSeVx5uk2VAJhmwUKZ0O_hivB67pAS1pjzdawtemch6NInOx9D95hw0nQHftiacwytQ6dPbWtkHPVpg1jrEbrO9Byx96VT3Nb8V1M1UxyU_U6Q0BXCJyFdddCkGBplGjK4vZZOT326fNwwmQztT3fPJELKjQQhOOVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ
روی تصویر بمب نوشته: از توجه شما به این موضوع سپاسگزارم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75689" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOwSty6T36YlSkTF23kkx488jlH7QlliexiVIzczTMwT8LevoetsdibG4oXlmjdKaVwEnVsoM_MFbVOgcSkZX3q-PtgPDAT417UVbNxd9nqIvl9Xa5r3thMfAltgYBAqKaMDcsETJysGY7bo9XHJYz6O_YMVbsHgwOvPye0KQigDth02YsRQt4OdnbTtl6gh_AzcgJz68TNNjzdwscqo6OvUzefzil0P67RI_sHhtXckmbkdaKcU1ZV3e4_hgsih7aoww7A-mNIcsEDzkE4w0hE2u7b6n9sePJLSh7nEcUAKtWhLAllVMGy64Pm0ipQXWh56R3EAA_cdNYcya00-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در گفت‌وگویی کوتاه با نیویورک تایمز گفت: «ما موضوع را به بعد موکول نمی‌کنیم. مذاکرات هسته‌ای مسائل بسیار فنی هستند. شما نمی‌توانید یک موضوع هسته‌ای را در ۷۲ ساعت و روی یک دستمال کاغذی حل کنید.»
او افزود: «در حال حاضر، هفت یا هشت کشور منطقه از این رویکرد حمایت می‌کنند و ما آماده‌ایم این مسیر را ادامه دهیم.»
این در حالی است که آقای روبیو ساعاتی پیش گفته بود که ممکن است تا شامگاه یک‌شنبه خبری دربارهٔ توافقی با ایران اعلام شود که می‌تواند به‌طور رسمی به جنگ خاورمیانه پایان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75688" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmmAbaBZ-OlZ9pQYmYPrgcRS2xT7spW_gQbqcIN9hLNtTOQ1Cmn3iK6zTSxxdJpDK1sDmVlm_8RRnIDpTFQhW_6BVESd6dS-HiKPEOKXdWXsmBVL9efgtjgoZPoMvyaCC_IN9-4rGw2iQn7_wnbfrJAAH2HcAhqlWTYs56CiTEIpyP6YlEI3yBFDClmwBhBNdNjTGFI7IC1qBbqIacWuv7ClLtUFfFIw-59k_JM61DhDzj0mm9KF6gEKcRwxhtuCZfC3s4lOyqHiYcQsamb5h0Rn0D5VSQZGaNz9FMETSQKDc8_T0R-4U_LWn5FdiQABNA5sxsc214ITDsju20g_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر توافق کنم توافقی خوب خواهد بود
ترجمه ماشین:
اگر با ایران توافقی انجام بدهم، توافقی خوب و درست خواهد بود؛ نه مثل توافقی که اوباما انجام داد و مبالغ عظیمی پول نقد به ایران داد و مسیری روشن و باز به سوی سلاح هسته‌ای پیش پای ایران گذاشت.
توافق ما دقیقا برعکس آن است، اما هیچ‌کس آن را ندیده و نمی‌داند چیست.
حتی هنوز به‌طور کامل هم مذاکره و نهایی نشده است.
بنابراین به بازنده‌هایی که درباره چیزی انتقاد می‌کنند که هیچ اطلاعی از آن ندارند گوش نکنید.
برخلاف کسانی که پیش از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد انجام نمی‌دهم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75687" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzXz7-Dqom9Jl5Nm_ZScUtU9Qm0vgmb3cx5W3W_hP5L0sLuH15Be2YRm1ZUfzAzV4l6eIaTxnPORGQ3pG5YSQkZNjZaAf1bnDMTXcxxoSFRphNX-kzFEjXecpkNNP6HSWiOJTXcvQEk96qNAsN5rCt1ryGq9jF5i6QwDSTTfXYPp3mVmGPFIlmYR3XCpPQ4Bwm-lA0ksdYmsEJ3Oqp7qTEYfaMWH3kiSCEA7U3Svwx65zQgxc91sP9xA3JMQDAGRJYIAaW9KLw7rVWrbwUjln-veZxw4FrnGDHk8m3u6BUhYB1z1hXzzsV7brvim5knLFHciyhJX6b18niM9U4kmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آکسیوس، روز یکشنبه سوم خرداد ماه، به نقل از یک مقام ارشد دولت دونالد ترامپ گزارش داد، «چند مورد جزئیات حل‌نشده» میان تهران و واشنگتن باقی‌مانده است و به همین دلیل توافق میان ایران و آمریکا احتمالا امروز امضا نخواهد شد.
این مقام آمریکایی به آکسیوس گفت هنوز بر سر برخی بخش‌های توافق «رفت‌وبرگشت» وجود دارد و اختلاف‌ها بیشتر بر سر عباراتی است که برای هر یک از دو طرف اهمیت دارد: «برخی کلمات برای ما مهم هستند و برخی کلمات برای آن‌ها.»
آکسیوس به نقل از این مقام ارشد کاخ سفید نوشت، ساختار تصمیم‌گیری در جمهوری اسلامی «سریع عمل نمی‌کند» و روند دریافت همه تاییدیه‌های لازم چند روز زمان خواهد برد.
به گفته این مقام، ارزیابی واشنگتن این است که «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، چارچوب کلی توافق را تایید کرده، اما اینکه این روند به توافق نهایی منجر شود، «همچنان یک سوال باز» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75686" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDSUhUBbsg6H0-ZLn5KmAMnna0JINXhRCYqDGjWWN-SqIqu5ddKOl0qiq_akEOv10y6raFdlJykO9mRYqGcQJfkO2U6gst2v1XMYVLOSihIhtGNMS0c2vX2Xh2nFXzC0-i2J-OgQnr6mxt9oTxv0SmZvzDYLI6oOKmmwld0Z7BQNF448Gp1SJE4ZdALHz0ndCgqZrDAZusjvQtLZQfmvtxUUkfRSnTMdLju0jDdAr9-IJjGOaTAswjiMHpzzAmPsB6362sTw6LbW1EjoUNCqHm5kpg2re0X_QTlz2wOrJl_xuDADG_rKt989cu3OoMUG2xoOjTR3yefPl0_K1nWpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او و دونالد ترامپ توافق دارند هرگونه توافق نهایی با جمهوری اسلامی باید به‌طور کامل تهدید هسته‌ای را برطرف کند.
او گفت این به معنای برچیدن تاسیسات غنی‌سازی ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک این کشور است.
نتانیاهو افزود ترامپ بار دیگر بر حق اسرائیل برای دفاع از خود در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، تاکید کرده است.
او همچنین گفت سیاست او، همانند سیاست ترامپ، همچنان ثابت است؛ ایران نباید به سلاح هسته‌ای دست یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75685" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EP5WM96QuJpYdixebSOUgndmptPu8a8iYuL_6VA_P8uYKgICPJQQcdgr51oFeWdjSbpNG034JRW4SnO3RsmTY6LKAz735vrD5QSWiJI8kSLF647SFXtUZ5--URmeieql5aGfaDt8fP6Irr5euBDrAD_vWvq4wN-Ih_wNR_64QVINuokOAuh5gNWbQxxpSbFwDLLbKVaygYBiZ98bcL4ptuLuAF41t6lewMgkaH_7Va7M0eQSStjJVXABVP__y7SSgIWNvAihxmPpdjIDDJ61y5eo7vwQGlMe5sgkgqbhzEHR_0ntXaMrBoTvYn8rtdOOdLKKUJXwpVOsbUTcu1Sj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ سخنان پزشکیان را نشان داد: آماده‌ایم به جهان اطمینان بدهیم
ترامپ اسکرین‌شاتی از
توییت
خبرنگار فاکس‌نیوز رو پست کرده که نوشته بود:
مسعود پزشکیان، رئیس‌جمهور ایران: ما آماده‌ایم به جهان اطمینان بدهیم که به‌دنبال سلاح هسته‌ای نیستیم. ما به‌دنبال بی‌ثباتی در منطقه نیستیم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75684" target="_blank">📅 18:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bifkbmVN1a8Bm8IlyWz0e83RHZ5MWRR7qirCTSgT16NYKjBzi0l8qthRaFkQLD_ERZ6OVC__gTDZlmiSTlKSA3Q4v2uVU_PUI7o7TCsdyj56aXjwfAACJ8cvbYAhuU-JOmA2xCV-A8TXflxtKqI82pZjm1Rwe2Mgm0L61yIk0pJhCRp3d915AQW6IqmDvMBgpcDhISsbSyZHACjiAKwhK8EE0G7JnQp7BqTy_ywb8tNAKOP1hvn4JoBiBDmJarl9vFBpvNcHgfd-YW0kR2F8Ba8blSJ1tN48E_-UZHWgipnLbXA--O14NDSDLhYC5NqUaRp1e4cyr3U3qRgFzYq0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTvDyd82k1CkDHIA-FGf_0ggo1QhW7XGpqoRrEPp3PaFURjKhU-ZDOjgmjpdWwJRqM83hFu3oUJK1M2i8EZ_qo8wVPavVKGIzdbaDfTuOxKt8qMNJyXT7kXtcS651etcIBpY8mA0d8AnOnmJqqgs6DhP64KCkX2StLdgBAdpLBNpS0PHpjtqTgiBOkiNCRUitc1dVjGgbVri9eyZkBnMTRoK8AzWYOb4njW3MaIzODfiN66oi0eVmtUJ59LbyNCwmjwct5tqS3-o7wP9044t-lpC_xwGBgZ-gvfdiMYI5W2WC8miexcVffIkGgzT7cDLIBCsi8LKoXZQ77MbU7uozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEBE6No08_pjURGgXx4yrWY9PDuHfZ9p3VPrQiPqn6LVZV5xI-GEj9sxIhFItwC5U5HSmrj52T4T7PLbyeSKVo6OmhluSuL5LZBPhPBYEB6jnRcr9jZVIGmOtOVOVhzMYMVsXiXuwqvKFJ_xSw7In3tW_JCXkprVjNvPn79lB4CgLcvsJxLSAgYxgUUOGsSfXU_YbLrU518ZeE7Dnjld2CHLLFjPF7PN6o4ecDsudtwq5vU2RyQs8B2QkL7YiHYA8v5GEFJM1es28Viia1EpOL8flXa5umi_vzUFtbZmP01u4ISaH0EtjFW11mL29z5_xbB_bJeHe8C3RbiIi5z0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
