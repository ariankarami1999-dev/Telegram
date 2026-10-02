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
<img src="https://cdn4.telesco.pe/file/km3I2FZkpcnvbzpwWfbocmColbrdlA_wXGHWWkdDO60dS_5IokmMmRxvTB5a85-MyBizCUq4SpK5Jz488o7JtkgCsaI9xNtOes95Ny0zSRBJNM3yIgvq0QhsjeQkhjNcXTE_ZnAAKKBV6xmuaZ03asWx8ONw15PrX5Gb4u9dcmX92NFq2NdomuPtv5I4Jts5UaHiT9c8Xri-VjwBFuhP4dEwC-w63Rs-CNYuWjtXST6IDcOn6wna9TMOq20FQDEBOzi4iz5T8_3lSCk54vAK27vSopbIwUMwm8IIL6L3vsi6sRb4_l-_vDb0c30BhUeSvYVzaWQ3dn9R5krbhqzBQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUcQIUQ2wT0xSI7tjBg8YS7nJ6iDieSv5Ap-mHBlVzU6fZGz9fvBWaZX-11xE8EUkafZl12w30H_TM0iLWWdeIw_qCUbVlIRJdfBZiK8RDb2wI5YtCgiXizp_XJyHTK00KjGLNR3D3xBNg73A4S4cltZmNJcnnyS_5YQs064MJIgpwuThNov4rb-qrcIRWXNoTdRn0O4fOJ3qjhptgqQOVy1IgGr3AvC5PTVu2VtLHaDBbHrKg3a9KpvSZK1IXTE0n_tEzXOR09omQNUNbQYghkazmT9Kx4vP01DgZ5XL5juPjCGI19nLl4MpS91CD9QSAJBn4fho1_71taitRh8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgcnzZKjzCdbkAbzH0pn2ZFkqpfvJKYBTAMG0ab7oLcf68ds6kSTjOMHJJg28zq64x0ZZ2Kvt0AS_hVd94pAQqAV1kwll9YZe7oGqHek7kdp_X1--ymD-qYbRxu52FHEdaTnQwIQ0zNbtg602DabaJtlkAroS_onFjmEZmxVlnivLK4D560pI94MWM_twtNv258gth-cJ6dVP2xKHGxLQXp5Y9l7i29a9LzzqwIFE9NwL63GLG6ODJtOUhN20D6zAEUOSCC_YNrtKGSn1UhFOtCXtCyjwNKCYwzvk1Zq62S63PjrDrlx5RZFpK0o5fFTXnXtkYCubO7cem8vBn1PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=QENVR9eBuAwZz1bMPuxzGjYHYA5OoldIAqAFyjGBST8QE-_fd_Y66FWSw7lvm1s3Wjl2aISDrSEOoYH6U08EMD0G-Jxv6rTI7odMpxIoNBkCZsc9NwlH6i_hr421zXxPWxRnZVqRj97dDg_bli1P8Z-Cr0jerfWf5KwEjsoEP3TWPiF4J03KOdGgqlc84mfuxW9MgHi8YgSgJVwmk-Gwhun7iv-aBaaeiAL489NFA6fq8JjesFkX_ekJ5C-vMmNPoEqTVeuHtGe2_lKKPxn-zbZcCsPc8ChEgBXCx0eczKS_aY3ASP_1uckeSqOI2eJEyI9iakN5BxnHuyfkuh2d9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=QENVR9eBuAwZz1bMPuxzGjYHYA5OoldIAqAFyjGBST8QE-_fd_Y66FWSw7lvm1s3Wjl2aISDrSEOoYH6U08EMD0G-Jxv6rTI7odMpxIoNBkCZsc9NwlH6i_hr421zXxPWxRnZVqRj97dDg_bli1P8Z-Cr0jerfWf5KwEjsoEP3TWPiF4J03KOdGgqlc84mfuxW9MgHi8YgSgJVwmk-Gwhun7iv-aBaaeiAL489NFA6fq8JjesFkX_ekJ5C-vMmNPoEqTVeuHtGe2_lKKPxn-zbZcCsPc8ChEgBXCx0eczKS_aY3ASP_1uckeSqOI2eJEyI9iakN5BxnHuyfkuh2d9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Zyk8uzt-q2IZRFusxQj-mSOVVy1pZNCxDDQP4ATM6zWpYTMdluVMFWZOcpaJfCEclbfRiQQXMkMlp9sliEj0hw11LhwoMEAKqgCtDHkXLA3apdufUfIe4TvAYmLqxZ89IqfDdg2p5q1Ly1FZaRijeKY0_xaR5XWObC_SYWUajgnGPPYb86PS1zV1m7eBlNR3hWlJ_aQjEWxuAJOugg2RslEFF6SxUCxv6oYG0ENQSAFWBac5y1OHLfdUpY_HFfKKoeWkleHGd8aXgI_-3lOFH9p0Ey4yBUQZzF8gzPO9ZN6RjZPhDQgU3GpmN-3pNNBURK-heJNICV6-S0V1JNINRwtotIvRM_yDx5MaCUQQhoAz5O1SRYKliFOea8qcPbC6eDImJDkb0cm89Wd7z_xEqMg0vB1LXJfYGk-0S9XOle9Tyzq4LHalF7hCQco_nD8klZ_VX5VEhoxVtkLFwjvtUh3jaDBrvwqTf8lNlnBsuRO1y6eAsc_Wg_tvxuoyNfRPGQgb-y5gV9HHyimxMZXpl2q6YuQfnjLHP7JUxqcbAfbz-RX-NzSpRftVjrel-mVSsgQ5H6NCLn6pgikhbZJmOyxy_9Jc88fVDsQO3Gb9wB6rmbIWt4mOdP3oTun4KT4FV0pYKkX_m5iuZN6a8jGRJrRVog9F0DobWNkLbRDlTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Zyk8uzt-q2IZRFusxQj-mSOVVy1pZNCxDDQP4ATM6zWpYTMdluVMFWZOcpaJfCEclbfRiQQXMkMlp9sliEj0hw11LhwoMEAKqgCtDHkXLA3apdufUfIe4TvAYmLqxZ89IqfDdg2p5q1Ly1FZaRijeKY0_xaR5XWObC_SYWUajgnGPPYb86PS1zV1m7eBlNR3hWlJ_aQjEWxuAJOugg2RslEFF6SxUCxv6oYG0ENQSAFWBac5y1OHLfdUpY_HFfKKoeWkleHGd8aXgI_-3lOFH9p0Ey4yBUQZzF8gzPO9ZN6RjZPhDQgU3GpmN-3pNNBURK-heJNICV6-S0V1JNINRwtotIvRM_yDx5MaCUQQhoAz5O1SRYKliFOea8qcPbC6eDImJDkb0cm89Wd7z_xEqMg0vB1LXJfYGk-0S9XOle9Tyzq4LHalF7hCQco_nD8klZ_VX5VEhoxVtkLFwjvtUh3jaDBrvwqTf8lNlnBsuRO1y6eAsc_Wg_tvxuoyNfRPGQgb-y5gV9HHyimxMZXpl2q6YuQfnjLHP7JUxqcbAfbz-RX-NzSpRftVjrel-mVSsgQ5H6NCLn6pgikhbZJmOyxy_9Jc88fVDsQO3Gb9wB6rmbIWt4mOdP3oTun4KT4FV0pYKkX_m5iuZN6a8jGRJrRVog9F0DobWNkLbRDlTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDkJ5C5C5ybZ0LxvQH15TP0XsJ7PlFO68O2dXvi-b7TAN2aRPI0PUrPQ60bALacq5Kea5LMA4-EzpiGdLT8pJZavGOoasd4GUuSoWmsS48Y2L1SfAxm8r2u37SQg6VRFcReivbPZJIxqvLx7Rr53BFsbhRWKf9L27XjSKozZkfjowmAf0irwYIPd8_kJFJTnw0JM-BPFSFVqSkkn3fFGAj-_dzfoj8ijH_JFnMhvYVq2LB0Y23KkeYE_cjgfra7zKfIVfHbgsOmiV4AY-qTWFaX2QFNd0UqzOkT83Mf7y5fF-wwPGqHv8-GdUqyOPbioJhYXU5xu928RAz7BiEiO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQj6idDclAZeRighCi-i2XPtcvTFscwz26ix190fSMGCNy7Fk8v2Tz3wavAtRmWdUR4MxWV2lkF3u-SIPjsTaMAwuzdQHSuM4X-9mN_zkrdPJqLTFdXrNVms4gzn8qQ_ONQIrQyrKKZIiNTrZMf3riWdq4Xc_JsCm8FfPjEThwC7v3rpmRSHaLWK4MVupaaOjwAQOD5_laEEJymwggW4RTVU-BV-zErAbIXPzvfSJNo_M6wsD4fAmt1ZHpAwRzK88Ef4RviIezQR2TMUgS8lwTFOv-f1WAZUNDAphg5uGwAB22tarPfkcKyTCGUiYHXpAnq_wdoe1Pf82-tX-hx3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWZQnrzlC8HAJaZUYfs9BwMk0HBchVqPr_6G7k2lnRbLTON9mFYyQxegFfTzkFXR5dtFuubylw4OTw3aI0sJdp4FkwOtMOcipnF5YcP2z2QbLFVHU6HPoHeNGa8N7im1zON21w3VX5kYfqmj1qPBEhMJuO1HJbO8kSF8ESXY1wUJ90SfkCuPI5sksOBp6bfFsYxHN5NuNMpp1pZ32Tbg0rdboS79STDWrv6uywd1xOy5YYEyv0JP0KGITpW6J7B0pZPmhlvwXwPBvGDYcXE9eCTuoZxGnktDmQKTMLC6FJJkCq5FiczMjdS-2ig19kS4Ot46ngsxyeq9pX5Q5Sr4Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=shEyha_sHqJj8vF_z3dUcyEymqjSZbLTeWi0Z6yxe6Pz_gBPlAO1ASYSX-LOQfxMFnUyPZh-2cpGLTrwf0R77bLGtEB_ujywoV-4ddiZoW1bhOqA_0qVabQ3EdIZXseoGlzE9H-STnnhiunTfclb6KbMUozO-5r_uYwDmS8ztjRSv-XZyrvrORHVRFY5b0cvDf4g5_JaGS7ZikErQZI2f3RJ36JV_Z37Oaw-dY8Jm8NAPbVZTqkvw5ajOdVdfVHRMAsCq3DVxe-RAlH9p8ONzl0Bj_I4XHiW9M_VNifF70UYKuEYIXxlO6_lIcUU5jTvtXOhAXJVWPWVw4bmgtoBIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=shEyha_sHqJj8vF_z3dUcyEymqjSZbLTeWi0Z6yxe6Pz_gBPlAO1ASYSX-LOQfxMFnUyPZh-2cpGLTrwf0R77bLGtEB_ujywoV-4ddiZoW1bhOqA_0qVabQ3EdIZXseoGlzE9H-STnnhiunTfclb6KbMUozO-5r_uYwDmS8ztjRSv-XZyrvrORHVRFY5b0cvDf4g5_JaGS7ZikErQZI2f3RJ36JV_Z37Oaw-dY8Jm8NAPbVZTqkvw5ajOdVdfVHRMAsCq3DVxe-RAlH9p8ONzl0Bj_I4XHiW9M_VNifF70UYKuEYIXxlO6_lIcUU5jTvtXOhAXJVWPWVw4bmgtoBIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=SP78hCq_WEPMbNnT-0a7m8ZUBl_JTtUr509XvOCY7xPSEwRQp9Iac3BHBFL9Tjdzp9dDHMEplWojn5nPpNHf3xL-iVKRsY9oXHfUuBxOfLA6Ber68mGeLFPTyVYeTe6YtjqFabsb61dxMsNDwXB_o-etN_r-mxyLtbDZPyiIA6Byfv_gpR0Jg_o3cn1tbTG4ep3qbU6yhPiXKu9zhE9DhZLePvOj0a03u1bAnJEo3_HQRd7RqWLRoZRD0o62bJNIMRfBvKYgL4gI4InFYTC3DLXVQuM9gqDNsZ0q8ctL9O7diH_Nvo2n4O2-eSA7cq4ijnnOftyQ0N8NzC5oEsR2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=SP78hCq_WEPMbNnT-0a7m8ZUBl_JTtUr509XvOCY7xPSEwRQp9Iac3BHBFL9Tjdzp9dDHMEplWojn5nPpNHf3xL-iVKRsY9oXHfUuBxOfLA6Ber68mGeLFPTyVYeTe6YtjqFabsb61dxMsNDwXB_o-etN_r-mxyLtbDZPyiIA6Byfv_gpR0Jg_o3cn1tbTG4ep3qbU6yhPiXKu9zhE9DhZLePvOj0a03u1bAnJEo3_HQRd7RqWLRoZRD0o62bJNIMRfBvKYgL4gI4InFYTC3DLXVQuM9gqDNsZ0q8ctL9O7diH_Nvo2n4O2-eSA7cq4ijnnOftyQ0N8NzC5oEsR2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcu8bFEAr5fJqC1-vXwVdBotP9ZK6_01Aw61sODGzzCEwyNeQwjRcwFCw6OMcMI4tpmVQsml-ui3XCm38X_KgyW7AKp73Lg-dik25Miqh6TSycO02jkjGbRLDsiNxHgWslvF78WQIBRHDDqddBPEoKxrk5zWQufTOIgB9bInj9BsdNaZyM8O3dBI-fCYo2gqUD-jRhWo0fSayMv146X6A7frgZ_oSZGeC_Kwr0Erj6vje7oz5TBb-WgRRl-PNfaFEjAg7QqVZAhSkwUs2DHu5sjpg1fREI-VWxTxx8VkAYokS_QTuoyzWrf_mHFml5IFiIrlqdaHX8bRVq4TuLRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Fxxh7qlmIza0-pRv6YRncEgHCuje98wlrhs2MaW-PVN7rcrgI0Khd56_DE2a2SZwkCF7B6x1vOxqdXXU1iwUjjbwkGDI88b4iTBvH7nR1wINCRNoOHIzW_v7sIBrvI0x73ZJq2dCEGMm05rkOTEZD06Cr8pELLTY0L0YB87msilJzkjWsuKx74-AtYIlxj5X74HChowOhXmTq3FcKjoggKEEovpBdaJ-Sje2Su7HIVD8Mix9oblXry9KZJJmOCepYycemA8H1Iz8QvYYMGzBTNak2aUwHzYi9398reVurrnO_eIn02a-PCTvwamc5glBWNUaeVfd3L5xRsG552BQUUopZeprWXxddSC3S0D7TPlVPm8A6CDTql3pJ1SlTbch7-k8cQvhzMrGEZnEcysbBknftsqbrk1quvg-WQnkZt-S4ILon0SU-mKdGKR-lRn3COMdo590J3YSZ-VvkN6jEf2sMnT3QJ0YUixzS_huzM1mIvFc2cxUooXTzrrKNTqdvmiLUFqLSQytasdi6y2FZQQwodRF9N7MuifKibh0j7IU6rXjGhgxd_ciRTXcgxxKE2p6uyP6EyIdAeqDQ-zs0hV9iGrKEoCg_pm-A3TdxSEcblW6iH22Q3QEL0A9WJjwi9wm8Y776XAU6kn6b0XqdppXfCZPkgX1kX3LQ1Ekejo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Fxxh7qlmIza0-pRv6YRncEgHCuje98wlrhs2MaW-PVN7rcrgI0Khd56_DE2a2SZwkCF7B6x1vOxqdXXU1iwUjjbwkGDI88b4iTBvH7nR1wINCRNoOHIzW_v7sIBrvI0x73ZJq2dCEGMm05rkOTEZD06Cr8pELLTY0L0YB87msilJzkjWsuKx74-AtYIlxj5X74HChowOhXmTq3FcKjoggKEEovpBdaJ-Sje2Su7HIVD8Mix9oblXry9KZJJmOCepYycemA8H1Iz8QvYYMGzBTNak2aUwHzYi9398reVurrnO_eIn02a-PCTvwamc5glBWNUaeVfd3L5xRsG552BQUUopZeprWXxddSC3S0D7TPlVPm8A6CDTql3pJ1SlTbch7-k8cQvhzMrGEZnEcysbBknftsqbrk1quvg-WQnkZt-S4ILon0SU-mKdGKR-lRn3COMdo590J3YSZ-VvkN6jEf2sMnT3QJ0YUixzS_huzM1mIvFc2cxUooXTzrrKNTqdvmiLUFqLSQytasdi6y2FZQQwodRF9N7MuifKibh0j7IU6rXjGhgxd_ciRTXcgxxKE2p6uyP6EyIdAeqDQ-zs0hV9iGrKEoCg_pm-A3TdxSEcblW6iH22Q3QEL0A9WJjwi9wm8Y776XAU6kn6b0XqdppXfCZPkgX1kX3LQ1Ekejo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=XYspbYQYHNxf490r2da23G_JGAT-8gd16CppH6DIokF9WOSpOj-ZEIwfapnxBgNiL1imAbs_bVrZI2utobhjyEcby6Ib905ON0loeyhiT5_rKoXMICwiEx0i3SvAe-7f2YFb3gcqpzjz5-fPnLIeFiBXMgzIn-XCH4bDQaLf5ljpceJ_15EQ6gmXAr1ZVmqIElpvzoeI9gNQLiEBB5Fca2oZ7U19rvg1iHRAlY_LqIm0FWwbc9wS8NVJPYfAv_qQ2eYjB67YY2sCKgZj-nOIKgOprXikNTL26bw-MejW3Z1aAVc5IJB9wJW1VBkNavAjnXwHa1V2GRXI70mpFqdXPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=XYspbYQYHNxf490r2da23G_JGAT-8gd16CppH6DIokF9WOSpOj-ZEIwfapnxBgNiL1imAbs_bVrZI2utobhjyEcby6Ib905ON0loeyhiT5_rKoXMICwiEx0i3SvAe-7f2YFb3gcqpzjz5-fPnLIeFiBXMgzIn-XCH4bDQaLf5ljpceJ_15EQ6gmXAr1ZVmqIElpvzoeI9gNQLiEBB5Fca2oZ7U19rvg1iHRAlY_LqIm0FWwbc9wS8NVJPYfAv_qQ2eYjB67YY2sCKgZj-nOIKgOprXikNTL26bw-MejW3Z1aAVc5IJB9wJW1VBkNavAjnXwHa1V2GRXI70mpFqdXPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP86bIVtPi9mAqOG0Xt1I131-Jv5xxUB3v3L1UZKSs7v-Q7q-o3rNe0DqxS-5h3Kn4T6M1H44wjXGh5BJdgUUzVe6c18GXm3_l1AQN4z9AVgH0iM0oR0QyMSHBP6-Cbu-663k7JhSy10CfyHh6rW4WxBLxK5EDW4tbkJpprVLuoVTz_dIcfMDcEB2dzBRewJ1lF5AnITdi_uQ49vjaMJiWWHefbCagbWxbX89P1wNaudNzfpVI2DELn54iC7GZtc6weIK0d3t9DYiKk3RIvVDrskjOUdtL6ZoFYXAJW32VACP0YRqk5r97NYnJK2DYH2o5KdtbWlWeYDiFUPNoWuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=fKuDZeBS02Myl_Fk72a0kFfLa6npS1k3dabOR_js_6SyI-S9lu8Dl9IgC8B9pe70NtC5htD2bsFpnJGW8aSvuUTo0eknNbM5snzZkJQdBhTqee7yUddeCnehhlkWMdy2gMINveTbSraGfwXzzKI9DWRh4DKyRLalj3r0kcs7ZGcvQblnkPM3clgD_hpU8ykLwndj_JwWT2NsIkeCOhxx14qivElSwy3MrPCLewAywKdzrLEYOZI0f0dz3p3FIFsJ0vw0abP7EEQE7MEViegmyRP8jEMHLzNzkX56e0_rJ9aZlntvOUciTofqtzVcL2vPFdsLdorY9PQ3h9J2hcB8rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=fKuDZeBS02Myl_Fk72a0kFfLa6npS1k3dabOR_js_6SyI-S9lu8Dl9IgC8B9pe70NtC5htD2bsFpnJGW8aSvuUTo0eknNbM5snzZkJQdBhTqee7yUddeCnehhlkWMdy2gMINveTbSraGfwXzzKI9DWRh4DKyRLalj3r0kcs7ZGcvQblnkPM3clgD_hpU8ykLwndj_JwWT2NsIkeCOhxx14qivElSwy3MrPCLewAywKdzrLEYOZI0f0dz3p3FIFsJ0vw0abP7EEQE7MEViegmyRP8jEMHLzNzkX56e0_rJ9aZlntvOUciTofqtzVcL2vPFdsLdorY9PQ3h9J2hcB8rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO3-dvaN-lix2hN-LK0anig0k7MXhFylvwL5RFfH9yYbSY7kV_rXaZLzkdnUo4MoovMB3A2RtSccpMjxFoqgZTHLlkTm-_1jSFSLgN1jSE-5tMr0s-0YcvTlDq99lmxosS-4F3fECwxVPMr4U7MfpQgF-Y7gkhN76Dh3ZWyUJs5tKdkyuXZ0tiNbNgdk-McFlFGbZHdyFceNfbOJdyKva3iXIBZ_EelbFr36UYTeQV-JjdWKFViowa5J5nSn6P-4B-i6p65chMg40szpA_3BUbG6BSOiQT20K0UMx-LmA2weXI6O94l6NZhvuuad38AF3rsG1QIxLoy-kF2GzgCsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV-Ht9KIcg9L89QRlnt8i3AhZN0E7Vb0c1LABKP_oBDUN28UuOx4PIHMIlaLyOCtgiCmnMBY32H7j6LuPaHg8rnnSPxkQcrc1tmy2adxIbVqj4rmD--DPZe8VL6rSViW-LHDTHsLgNVbHCr9RGzqiBQYqZA3RKrzzIntXfaTQT2I4YdJtyWZiVH8x8tgMWmA4osjMlyROA7rjpaO5RhJv_j4c6d7QbJrNPNQR8iOAstTajhKCxJoUaW2KNLuam98hArPjoYRqK0mbZXq71OF5DH7WINuD6ZJe2eoT2XLhc2oizZoePymFwkugiFB89Pf6bW_87glkDZbkM3YduIlqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=LwUfAa4HKBb27TnWSarJXwUA6LnYNB3A2J7JCBLFPazOMgoyE6s-l8eLsg8Kt4x_hjfSyYj-nkn2EBKcpvLKtdI3QzYglsy_sdC-ljhx4XylMNp-4bEtLFVePtpkxjSt_JJv_AX-ERKnNfmOZdSAnSFfG30Y9NfKoHmz94FwoxillIm6W0oW0uDIdvLy58f2EOIRbUtFnxmFoBke_FXk3gzY7BfSN3MCknVbHflkiqn5gRU_cmjn5_CsP9-u4UJEnqIVUHBjiUiuCs2xrOqkustwKQpTmnOwk3Q_ZchGha8sHcaN33FKCCe5ECwZn_vKyX9f6q67qY_VS1RuZFAzsqbnH0PAuX82qS35MiuFCsykyncvVbYiS8I4X5KrPJ5JYorZkL7UwLk5Dm0V-U20j8Izu4I78Obd2mquRZ6eeYlkUcUv-fx784QktgVdNEzwgQN36-_hfVdZElV2lom3Kk4LnShFK72ygBO_2bd4fhx6P9DwAjeETG7VLS2jxwXA3-ncl8sy452z6a3izSygyO-PgWklpIvWCCxChdII8ZiWVpbS1RHeeTa7WZILzl4ylMR38PRUJ_r23NPOYk_jGSxgrLiJKLT_daQWuHM5OYXL7FCqVJeKRg2zsD1rwxxbJpVQd7RRWykP206Rrug6v-kwqidYZL2Vuqdi1XX-rm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=LwUfAa4HKBb27TnWSarJXwUA6LnYNB3A2J7JCBLFPazOMgoyE6s-l8eLsg8Kt4x_hjfSyYj-nkn2EBKcpvLKtdI3QzYglsy_sdC-ljhx4XylMNp-4bEtLFVePtpkxjSt_JJv_AX-ERKnNfmOZdSAnSFfG30Y9NfKoHmz94FwoxillIm6W0oW0uDIdvLy58f2EOIRbUtFnxmFoBke_FXk3gzY7BfSN3MCknVbHflkiqn5gRU_cmjn5_CsP9-u4UJEnqIVUHBjiUiuCs2xrOqkustwKQpTmnOwk3Q_ZchGha8sHcaN33FKCCe5ECwZn_vKyX9f6q67qY_VS1RuZFAzsqbnH0PAuX82qS35MiuFCsykyncvVbYiS8I4X5KrPJ5JYorZkL7UwLk5Dm0V-U20j8Izu4I78Obd2mquRZ6eeYlkUcUv-fx784QktgVdNEzwgQN36-_hfVdZElV2lom3Kk4LnShFK72ygBO_2bd4fhx6P9DwAjeETG7VLS2jxwXA3-ncl8sy452z6a3izSygyO-PgWklpIvWCCxChdII8ZiWVpbS1RHeeTa7WZILzl4ylMR38PRUJ_r23NPOYk_jGSxgrLiJKLT_daQWuHM5OYXL7FCqVJeKRg2zsD1rwxxbJpVQd7RRWykP206Rrug6v-kwqidYZL2Vuqdi1XX-rm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoQTpAGTsk1aVZdKV134P4FrAT2JK-xdGol5qGhIfZunmQohz66Cdm1eTB39BzQkL4EOWnj7IoxpT96g2NUUxCt0VvyURAUX8GnbIrB004art3rI-ZMELq-WdsTdVzaLtTIphwtZcLlAkbbrisvcalD3kWZi5Dk7qAxBP1Mo3W-ZKkIiJsCzQlLCA29r7_yeoIFnzweqtjqbN4UHahD9EJUNyk8ePFTNRtp9B--o0jGyJ9KivK6KEjaVpeC_Cj2ZXFuJg7YHYjqGiBNItPHwFg3lBA9mYqZB4uaKi8phkPO1kwiVPZAOBphm7H6sz4AEQJcMzrmIRPHKqefZjalI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki0GN_IPEniI8qTP59m2fDP00HNnSlAkWbtbVsLdpkyrr4y_2ajb-g8aP5-ZM_oSeHlEmwH4OhXH52glTPMzXp4PGNH7uV1kj9kGpMIOTQxbQvL4v4YlIrIM5Vl_eeo5FZPJ-8bke_KUNXvr3AD-xClj0knv8KbwvCXhoSK47ZEak_r7U0z-CBqWu5yzHatIJXeVz0ww5t-HQvk0xAwVhfSq6gKkEdOM_fo6qv-ynSMzPPbvsh5PYG0jKNrh4x6-R93rNfAmYXomq21PJZfRIQF9nrhl87-XSvoU7JV1kTufGNWwttBepRyaR6tggktcsnXWUcTPPDh6-fwg4poS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=HKumPbb_A1DZfJL50O_YCtXkcLtCCQ1Y152Dqbma7LD6DReJo0D5J-I4_X3CnwxoT3G5ok90IdNy05dZC9SgykBUYZZB7gshuvC1dVWWyPugNiV8FUJaYAla15xCYsMntqwVsmr3OXKwW6HPQDBmrEye_hqd_wNHEBnGSZdDVNBF8h7f65g5KZ1pmh8HHIG2dryoX91w72Fke7cjtebXR7AoyubZQ-8bQW99ISvzofFBX9GmmLY02nzi3ihmfGqKjSOTU3dIMZ9AZrhcA9w3kTOOnUJIv0An8iLlwvg3WwtpfpI-FHWuPJS0BNI_au_mwKGJzC2oZdgXOXq2McmYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=HKumPbb_A1DZfJL50O_YCtXkcLtCCQ1Y152Dqbma7LD6DReJo0D5J-I4_X3CnwxoT3G5ok90IdNy05dZC9SgykBUYZZB7gshuvC1dVWWyPugNiV8FUJaYAla15xCYsMntqwVsmr3OXKwW6HPQDBmrEye_hqd_wNHEBnGSZdDVNBF8h7f65g5KZ1pmh8HHIG2dryoX91w72Fke7cjtebXR7AoyubZQ-8bQW99ISvzofFBX9GmmLY02nzi3ihmfGqKjSOTU3dIMZ9AZrhcA9w3kTOOnUJIv0An8iLlwvg3WwtpfpI-FHWuPJS0BNI_au_mwKGJzC2oZdgXOXq2McmYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=g4zsu_FvyIkxmpr4UnlZuyJO2X_gD_F32jTMM9RRWRvKGQ_-j6SHPGVSk6n23ymLI-JHPfK2PkAcRw6AeEl89fJHJDxZN-0XdGxEwWWJT8TAg91RL1-lR5AHHK9zijX5uAWpsy64DuczRga7qM0yvqWMuLrc5XTaWE7sCIeXpNUUdF8s4Q9G5NG6NwqxbJzrdnM9CvnAmcRs1Z4wKaOSR6DYN3GJ7wX40-0eG-lLndchaC_poTz9N2zgWjxZZV8PF3tAuGfkCCdKVEgeRbYnKSkJxpSRhcjLEsD8oWZXq8-q59c_187tDI70WxKGXfQT-K6iycrV3pFintxLTgXiiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=g4zsu_FvyIkxmpr4UnlZuyJO2X_gD_F32jTMM9RRWRvKGQ_-j6SHPGVSk6n23ymLI-JHPfK2PkAcRw6AeEl89fJHJDxZN-0XdGxEwWWJT8TAg91RL1-lR5AHHK9zijX5uAWpsy64DuczRga7qM0yvqWMuLrc5XTaWE7sCIeXpNUUdF8s4Q9G5NG6NwqxbJzrdnM9CvnAmcRs1Z4wKaOSR6DYN3GJ7wX40-0eG-lLndchaC_poTz9N2zgWjxZZV8PF3tAuGfkCCdKVEgeRbYnKSkJxpSRhcjLEsD8oWZXq8-q59c_187tDI70WxKGXfQT-K6iycrV3pFintxLTgXiiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=YQkbg-qFFVmNJ7X-yXsBoZKOro5pyhNnu35xGDePFbMSYofoWSsNpaF9nr6TxmrjM8P_ofuVpPkkfYBVHuM7lQi8ZY-RO_wN19m_4EE-4Sc6b8enTTQhfDt5JeJQzFTE3tM6mc1x8a4VvlN9iQpnODoX9MIXeVQT90M6clkFPCdJRCKdtao0zhjXaXWa5CX0RZ919KDgZd3B4QGnhSzB5Pgm-mQqnzLfRN7qCEF4k_g3X0WlhN6eG0c5sMcCFf8RQ0GE4G-bAQFVtRVkYkvO2hlF7usJWPDb2TQCFgd-rJd-9VwhsPWI82-y-GkkffvijeoOLlQMrPG0-ot_4VsjIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=YQkbg-qFFVmNJ7X-yXsBoZKOro5pyhNnu35xGDePFbMSYofoWSsNpaF9nr6TxmrjM8P_ofuVpPkkfYBVHuM7lQi8ZY-RO_wN19m_4EE-4Sc6b8enTTQhfDt5JeJQzFTE3tM6mc1x8a4VvlN9iQpnODoX9MIXeVQT90M6clkFPCdJRCKdtao0zhjXaXWa5CX0RZ919KDgZd3B4QGnhSzB5Pgm-mQqnzLfRN7qCEF4k_g3X0WlhN6eG0c5sMcCFf8RQ0GE4G-bAQFVtRVkYkvO2hlF7usJWPDb2TQCFgd-rJd-9VwhsPWI82-y-GkkffvijeoOLlQMrPG0-ot_4VsjIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_IZliTGNs9Ivk3wN_rtOBHxrNB7UNc0CfO-teDe5VO_srFFNcvmqjVNB0UoSn4OrYKxiLPSM0XJMCWfSInnoktZmXn5z2_3_fTgVP86G4XUGSQT1KzoXjZoWjjOcaRzNS7N8jcCE-o8srSz7BUy24EEbBqr3LND9mJsBP2Q-O3C-RIrpvqjmHne9kGKlVtmr3nfPQ1YBPlFgXTsdH1qBIifxprERu3hupweDLcigby3A7SoEAI4MYq3a3gJaUmSe-1lUYeotxL9OtOqDzsu4CJGgEKEEwM-rge89_SosqmUMo1MAcVFdKIktjYk2JyCvF2RCO9goUIBk7-Pp7v5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EPCcKNG6sfWC_YlxozrlMo7NLJdg7-1_0RC-wMEzToeKzBzY6m5Mq28hhWm8g51bo4XE_UVNbEXWQJAQZFkoSya7IjBly0v4Uc-r8bPpBz7_y9XqfqQUK7mIBbt6fYEDQmdCk2-zqrDlBWyD-UWs5iHZ7UtkBZ1ZjC6qfesNhzdmGTHay4uasW2OkABlsnkdaSeI4gg07px9hwNHfJjR3uD0UGpZyg8oTbodc70M58JcjVes5LrVEKLfbCPEbWXb0hGfn-O7apsDPGyanu995oon6NcOkb00FwPjgOTtX1yndMJHQrQ7OBsZMLYN9LFOkeZG-HFMKj9mrkkESqQLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EPCcKNG6sfWC_YlxozrlMo7NLJdg7-1_0RC-wMEzToeKzBzY6m5Mq28hhWm8g51bo4XE_UVNbEXWQJAQZFkoSya7IjBly0v4Uc-r8bPpBz7_y9XqfqQUK7mIBbt6fYEDQmdCk2-zqrDlBWyD-UWs5iHZ7UtkBZ1ZjC6qfesNhzdmGTHay4uasW2OkABlsnkdaSeI4gg07px9hwNHfJjR3uD0UGpZyg8oTbodc70M58JcjVes5LrVEKLfbCPEbWXb0hGfn-O7apsDPGyanu995oon6NcOkb00FwPjgOTtX1yndMJHQrQ7OBsZMLYN9LFOkeZG-HFMKj9mrkkESqQLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=nOA1i1EnVM1uI3VTzGJ9bou1UJ7gnZq-TWtbuDjrzhf26htpaeUqFERWb7wi5L-ye4ug6mBtSqCCNc7vLVBKNzyVaHmcsBDSK29FYrp8RGlccupBnxpXLMRh5F3n-m9jCAOFwNuHmRds3s1_FSyLd_wPG7NfsxyYZxvf3an41dw1BRfNOKIFijVQecoD0QhzF_c6bWeQV5NUFtEVCbsLflLc2Eo49okOh4z7_DPT8zWNeS5T7_0sbsOUeXYnk0sS5Ab3ELiUTnDSGOXc1LBQuzvx5f-msG_ysuoMBPdnwpP46Tjy6pQnK_lwOS1AeVxv00HrEFqNYL8WqCtCA7ASOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=nOA1i1EnVM1uI3VTzGJ9bou1UJ7gnZq-TWtbuDjrzhf26htpaeUqFERWb7wi5L-ye4ug6mBtSqCCNc7vLVBKNzyVaHmcsBDSK29FYrp8RGlccupBnxpXLMRh5F3n-m9jCAOFwNuHmRds3s1_FSyLd_wPG7NfsxyYZxvf3an41dw1BRfNOKIFijVQecoD0QhzF_c6bWeQV5NUFtEVCbsLflLc2Eo49okOh4z7_DPT8zWNeS5T7_0sbsOUeXYnk0sS5Ab3ELiUTnDSGOXc1LBQuzvx5f-msG_ysuoMBPdnwpP46Tjy6pQnK_lwOS1AeVxv00HrEFqNYL8WqCtCA7ASOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkrF7_7ligYcQW2XcfUXrBarmw5za-iMYyBXuQsFu4fCxlnxL9K9EKDfIlBfOER71K00OHQG1A-FfystNknulTCsFeaYLkEWtBt1-zswAKumKsnf9CJEuLlRJjoIdDuI5V1wVWS_McJZhJBTylQcPbo5_TcjjF8PLHNq0PLp__Jrt4BGJWL6quAWlqn86OMlPfqKIkPnQMHcPz6ayxoRqrmteyhNn1aFXmZ9-dht2zC-M3mdcLTWEiw_tjapHcc6UJE6o3O1BUvnnCBR-5hAD8O3EaBDH2QZFlSnzFuuUuNz9WwLFWQfVtX4wg7o4fwEvtSqyPAWosjxGRiChvt6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=lLzRCSuNQwPCHAgOZWjZTgqx9moEgPCwIHTVvqYIjNORbvTEYPXAZXakMPCHYGtVJXX8bW91btsBLsffo7ZugnZfmh2T8fUF-tWUiwNHdZ9dLw9gxXve2_SwKHT9CyUUfCKzr0trNwVZ4bP3Anr_u5HJJKTzSXUm2OCbpn2rjM3UiRevOOncqhPi9yUNKQsfIsvCs03MwpViVKC6sjInrDn8qt6pigKi_WL5G6gfY_PjedB4jLYK7ecHCHF5vlvJ0BgN20kRuCoWQIxRB8RDxk5K-q11AX1lDFw_92XbHCqWR1vBur4KjwVy4rf_Eoogb6Sl3qLjaKPbP3bOUw5SJSt_44lLZmTQAEVQ5SqoDntSOqsylrFVfcs8K7fFbiR37ZCmdIpV78gloC2N4eqCZPtQKXCbNDGvXnTwJ8adcWdNWTO5nQFYtVOME7ZjbiZa75MzQjpvCODCeObFj7h6x1s4eYKgU7GZeFZbNqfclp2wXgBwDJVJ7h1CMRG2ykyRjUfKWdBVR4jrV5CQJt4VrknQoNbwN8vQ6zQh9dJECBHON6ziUWQvuVqLs8WtCHxYnh7mArwWBEHzAYM4-oXcAQVxnstTfDdPhobbd69qaxGnZvvTOPLlxPGWXbF67yUbdBXCkhzzQJn0_CX_NPHlT-gGOS5_IuBIOColHnUCfc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=lLzRCSuNQwPCHAgOZWjZTgqx9moEgPCwIHTVvqYIjNORbvTEYPXAZXakMPCHYGtVJXX8bW91btsBLsffo7ZugnZfmh2T8fUF-tWUiwNHdZ9dLw9gxXve2_SwKHT9CyUUfCKzr0trNwVZ4bP3Anr_u5HJJKTzSXUm2OCbpn2rjM3UiRevOOncqhPi9yUNKQsfIsvCs03MwpViVKC6sjInrDn8qt6pigKi_WL5G6gfY_PjedB4jLYK7ecHCHF5vlvJ0BgN20kRuCoWQIxRB8RDxk5K-q11AX1lDFw_92XbHCqWR1vBur4KjwVy4rf_Eoogb6Sl3qLjaKPbP3bOUw5SJSt_44lLZmTQAEVQ5SqoDntSOqsylrFVfcs8K7fFbiR37ZCmdIpV78gloC2N4eqCZPtQKXCbNDGvXnTwJ8adcWdNWTO5nQFYtVOME7ZjbiZa75MzQjpvCODCeObFj7h6x1s4eYKgU7GZeFZbNqfclp2wXgBwDJVJ7h1CMRG2ykyRjUfKWdBVR4jrV5CQJt4VrknQoNbwN8vQ6zQh9dJECBHON6ziUWQvuVqLs8WtCHxYnh7mArwWBEHzAYM4-oXcAQVxnstTfDdPhobbd69qaxGnZvvTOPLlxPGWXbF67yUbdBXCkhzzQJn0_CX_NPHlT-gGOS5_IuBIOColHnUCfc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy2iVGJ3JPShMFNMv6vy5fsbXEpXl9E9-Y2b2TK-3OqJ3MrD0zWDGYcCo7r3wH7zBQ6R9SoawuSP3nrTkgkto7hM3DxlvCm9Y36HpD_kGpsCfGsm7YOGiNK9SuHSH3q_YhHKTYqBoKOhaVoQlpXWCgEOMF-L5CpGzPWz0P4cDLqI34a9afbQkI7oHHhcsxReCArUq1MoiGw7XfBfcLBEc8O4ywJ_yCCLI0iFTKt7SF1lgXbVsgMQB9T0L3YNnAiN8gccDSMGl6-X5AY22DwFMLgzY-WP80QGrb51v6sWkjeSESHSlvl8AlvkZnp1rmfC7Ezz_cAQu-yrpoDfHLvDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=iqbEqtJzALtLAPAGcyY73Ox2NFj7Ap5n5hFoaztDkRAnVhLlAGnu3spKwcnH83uGGljbqXwD6EKjdL3OaYZojx5PSHo1SqPaeY0ZtDJNfe5WDqPQ8XxDf_Fb881z-imbiDTpbEp8ESMH4xKNVjpwA7pSATXOiEA32aPZahesRLS09GXfuaSpVOWZt9h8tzLQ3L8zpGwTOGrTuQuWLgs27k-NIhPBlLccn09E_IPePkm7Q0QLb_1LS_2RhjozqWFmIjIedBnuWl2CSr36UYbxGtU5HrymkuGsTDuNuTxTJJ_sYUy0zQ1X4j3XFUDoiS4yQr7Ad4dzNfrLWzq0Ktj5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=iqbEqtJzALtLAPAGcyY73Ox2NFj7Ap5n5hFoaztDkRAnVhLlAGnu3spKwcnH83uGGljbqXwD6EKjdL3OaYZojx5PSHo1SqPaeY0ZtDJNfe5WDqPQ8XxDf_Fb881z-imbiDTpbEp8ESMH4xKNVjpwA7pSATXOiEA32aPZahesRLS09GXfuaSpVOWZt9h8tzLQ3L8zpGwTOGrTuQuWLgs27k-NIhPBlLccn09E_IPePkm7Q0QLb_1LS_2RhjozqWFmIjIedBnuWl2CSr36UYbxGtU5HrymkuGsTDuNuTxTJJ_sYUy0zQ1X4j3XFUDoiS4yQr7Ad4dzNfrLWzq0Ktj5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfWuKHVYpvvmMVPLMUK5mN59yEE2ItzUe1M679dZtMLaruhk7L-pS5JMXxAKPa2ttQ2kQuDTVgHJof08kjvRVB8XM_WWjkmN1WwUsIov_jttLlPHI29oO20OXFvuKNHdGbiB4ucklhX82XyQ7OoSMOqmHwB55EdfgC6vXlPduWs4rMwtcB4YsLWKpKsvdMqJxeDI4F9rsCmXbljx1I6F56VLdMknarOhib-IB8uSrmPon430KYEBlCTIpvRRJ68WzhCpxFh9wPdqhcPcbIZoX5UbQJWr-U-y2zkBSAsTyjcIMj7I-VjXZ_EohfOGs-mY6YCWBzNJ2Tz9w2x620iALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Euyjd5HowLbRc8pJkuZnXD9ebMP-3zGKsKxBXAdIDBXPzmMljXW-Wh0d9yQJfhKrEY6N1T38G4x0GkyNL7Gkfk2wE197L6Wc3u-6iWG-C5KSNmodsgTEQ5OeQ9a7v0UsmYlB4F_ua_laCCtfEUqHxxZ1tqaKxMdI0itUrBQzB-LVE3emTuiNqEzyEPkGIThln2rfWqbuR_d14qqEnMzYSczz-pUu3lYq9dp_ntGmCZGRdlDTbSPlmBEHvyQCPo24pcOgZPm-IeLFUTFJdupJSyKediw445OaPV42udolin-6dogtUGDWQvn3Q6dMQcXJZFJn8FylLGe9MSLS5WEP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_mXBwvzXK7I9F7p3aIaM-hnpbSTbC42JkfVLvDCCgJSeJGkXT1-8qd0MjPkc_-o6KVMth1uow_ZgNxNARqO3vI-ltJA7vUCIgFcyr1hN011rEYeuYLOq8WwJPUycVcHT1P7-nL-w0ljrXf9qy1Q7BhtLhJiJMb6BKMFjobn_2AN-FoKvr86JGNYcGBQ-UIZC5tN6KcdtmPka2cVxb7JWsPG9r5b0dB619URIFWs9AsKHyJblaF8rrOLVggyX3Xs4YQMMeKBrzRfEhklQTL451hweztjJ87hZCTR9il0f05DgL6XpYUJ0dcRpHUqDXHE-mkQrZ35TjiYZDCKF0XBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IP4-zC8JqfU1lvUwb5CIxWIuJeGcQhgvdl8v0HmFAfEeC_IkxxHGhGJHTPfHkxQc-13r748Wt6ujegEzXpokiIr6eEsIIAI8urjmI_5txBsFC7NFdvzddwsxFpvs8ACm9gWqABuE706oTyDhiRGtzIK2AfI_v0t8PEGt1k2yV5_kixzolDyfzY_IKAvnGZ0IBn-LGMIP5gwqxW-wRJR-CAzjL6RkU1XFk5TGHpcstNfqyv1Y2hr2hIb7VelqEhnsaS6AfvC6_xQz_TH9BWRleFolAKaV3XJkxQ4MbqupbZW-2N_ZbnG4UaaUfqbAeydAXNGRQiTOx9E8hnzLCYtSqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IP4-zC8JqfU1lvUwb5CIxWIuJeGcQhgvdl8v0HmFAfEeC_IkxxHGhGJHTPfHkxQc-13r748Wt6ujegEzXpokiIr6eEsIIAI8urjmI_5txBsFC7NFdvzddwsxFpvs8ACm9gWqABuE706oTyDhiRGtzIK2AfI_v0t8PEGt1k2yV5_kixzolDyfzY_IKAvnGZ0IBn-LGMIP5gwqxW-wRJR-CAzjL6RkU1XFk5TGHpcstNfqyv1Y2hr2hIb7VelqEhnsaS6AfvC6_xQz_TH9BWRleFolAKaV3XJkxQ4MbqupbZW-2N_ZbnG4UaaUfqbAeydAXNGRQiTOx9E8hnzLCYtSqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY8ZC8ehZdjgNvd9SuK20jm243gLd4bxAxRp2g-w46lPwg3qpkiKdZZXxIKtrUMoD7n8UBM9zIW4XIAwIM0-n3D9Qqo761EAJMGNu1rJZv13knTHvfhuBUwcGRqAnm2gKC0VNFMrhQ6tkBdNIA_vIQikCoMdNWVnrB5E2SgVv1rNpj7Zw4yGPd3FvrpuxztoPnWY8qDJtXfT3qezoQAP7MsPlr8_he_ykcNFf5f6jm3qRe8P5pE-iCnRwuja7Nql1AHgc3-n55UU2f3IabJcP7H9vSCWks0FrGn8Frz2Z4QboPCeKzxmSPLwwGGaAYSmH9OZ4Jw0dbQoe8IIOGy_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu069EvPT5vaPualzRUln-0oWP3otj5fRSot6rmYpHtvZlrB6GqUG0F3XYacVCQ-4bpaob3B_6k1A-7Tc3GaoaDdTAQTHy9bFv2_03iLpufGIksxHwmo83LYD7YIoLg4DxHQooDareQ_f0poaryITPZW43FSxUv2IX9l_8chpLWgKzggWcgr3P1Y3jtxayqelq9fOxg5RAIk50y5ADua4BfGXJe97aQgHmCZefTGqVbK0aB8c6haP3zlrBhj_C2GF9rDpNYj7afp8y4b2sXHzjudb9F7P0ttUIxFVK1Wh6j00ZCwomBcDkDB1BX_wB9ndzGRm7eqhJUhDgZXJ4hAXi5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu069EvPT5vaPualzRUln-0oWP3otj5fRSot6rmYpHtvZlrB6GqUG0F3XYacVCQ-4bpaob3B_6k1A-7Tc3GaoaDdTAQTHy9bFv2_03iLpufGIksxHwmo83LYD7YIoLg4DxHQooDareQ_f0poaryITPZW43FSxUv2IX9l_8chpLWgKzggWcgr3P1Y3jtxayqelq9fOxg5RAIk50y5ADua4BfGXJe97aQgHmCZefTGqVbK0aB8c6haP3zlrBhj_C2GF9rDpNYj7afp8y4b2sXHzjudb9F7P0ttUIxFVK1Wh6j00ZCwomBcDkDB1BX_wB9ndzGRm7eqhJUhDgZXJ4hAXi5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=a-fnZ31hkysJ3axXEOQ4dzP9dm9IjaIBoNh-QjTGkgT-_IebHdGeueECJtCDQ7JzGCitA583JOimnPkyOYsQqkoyLEJ10aMtmzxp2ytDRLzllVSLQmpyxcJeWFKTnYfnBn3B6OI-BhjYsYPJMKxeEMQdAhTHzNzmJsDuB8YIZiZutl1VLRJktHEjGrERazmIeB0_bH4zigPPJql9B6CthNo0MjTwh2e0Q_Idw9v3iJz4tM3VrEb30zLCy3cMtc-tRaKLBDLEORqZIf0BO8ztUzGzvLRggX5a60_8eiAlK1Vsl0VVP8boAhqY7tGp1ZOXIoBK2WYCe3q77RfOhRPD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=a-fnZ31hkysJ3axXEOQ4dzP9dm9IjaIBoNh-QjTGkgT-_IebHdGeueECJtCDQ7JzGCitA583JOimnPkyOYsQqkoyLEJ10aMtmzxp2ytDRLzllVSLQmpyxcJeWFKTnYfnBn3B6OI-BhjYsYPJMKxeEMQdAhTHzNzmJsDuB8YIZiZutl1VLRJktHEjGrERazmIeB0_bH4zigPPJql9B6CthNo0MjTwh2e0Q_Idw9v3iJz4tM3VrEb30zLCy3cMtc-tRaKLBDLEORqZIf0BO8ztUzGzvLRggX5a60_8eiAlK1Vsl0VVP8boAhqY7tGp1ZOXIoBK2WYCe3q77RfOhRPD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=h91g8ZEkj6iIEgetsDVFP4x5yG6UpTZofB1Cv7jcHbEjXFFxZKU9-_E-eSqiMpDcFi5PpX_T8K8NCZ97VP8BxaC3fMqZheDPQ_yYzG0sL-C_68z0TL2F104Zsl2H7GL26g5NzBG6qk2Z8spwzPhJDLgI9qSzh-6CQszaAWv9OWa0f0FMyBGPDzjCQyc66jrNvfdYwEbAtOuoVP6bpSGq81p9ATuhZiD6G8SM7ipFZpTrGcdmgwoqYqWVR6bok-reybCxuSiznkXh-i93PPXIkA4Fm990DhBmlWiDxUyBE8VrjSnfNGpoUtWIJ8tILkDHSKb3XN-p6f3WCJ8irbSmQQMlBKPK3EXyUPFmdapyiqWggnqQW1TFaekz2S0MlYjQOoK1CfhY-Zfj3Tb5EJH-avp7upT_N1M-_CF3LqUuFtP5LPDHy4DgbFQPdv5jDL0pm989_97K1WhB6qv0EH2zTGc7CoJRBV3j49facN-3q2vEA2NriDmoAuE5WWmBFPR9L0SHf0uV6XysrMkrPy8MpmeLK7EtDt9RWNK1MnGUjdhfjFuGQ_BEJlHZJ5Qn_t5H5dt1rDxpkmV5nOPW8WW4oum4zkMoSZs_OY_NbL_INqBXSPG6rJNXGds3n-8jH8vOWU7N6QjJSnPKVAXNquaMx2WG7K1wEKWTmD1nb-GmDpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=h91g8ZEkj6iIEgetsDVFP4x5yG6UpTZofB1Cv7jcHbEjXFFxZKU9-_E-eSqiMpDcFi5PpX_T8K8NCZ97VP8BxaC3fMqZheDPQ_yYzG0sL-C_68z0TL2F104Zsl2H7GL26g5NzBG6qk2Z8spwzPhJDLgI9qSzh-6CQszaAWv9OWa0f0FMyBGPDzjCQyc66jrNvfdYwEbAtOuoVP6bpSGq81p9ATuhZiD6G8SM7ipFZpTrGcdmgwoqYqWVR6bok-reybCxuSiznkXh-i93PPXIkA4Fm990DhBmlWiDxUyBE8VrjSnfNGpoUtWIJ8tILkDHSKb3XN-p6f3WCJ8irbSmQQMlBKPK3EXyUPFmdapyiqWggnqQW1TFaekz2S0MlYjQOoK1CfhY-Zfj3Tb5EJH-avp7upT_N1M-_CF3LqUuFtP5LPDHy4DgbFQPdv5jDL0pm989_97K1WhB6qv0EH2zTGc7CoJRBV3j49facN-3q2vEA2NriDmoAuE5WWmBFPR9L0SHf0uV6XysrMkrPy8MpmeLK7EtDt9RWNK1MnGUjdhfjFuGQ_BEJlHZJ5Qn_t5H5dt1rDxpkmV5nOPW8WW4oum4zkMoSZs_OY_NbL_INqBXSPG6rJNXGds3n-8jH8vOWU7N6QjJSnPKVAXNquaMx2WG7K1wEKWTmD1nb-GmDpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=mlau98Tr2UuV1HBhvsh5mlTpK2BHuYqMQdYqy2z_STlNF21ruaJqzV9bHgB9mfSRtIWF3ACC8qoIJbPFeY7p7OMkp15EA4YOrFD-oQG8R2cJy7ByieXCeWdxhhY_uVLbGSkBk7g54U4bvTasxctGgxH4dbSpeodMOICz6Y6U49R2k52hAXK7w3aSgH9o-d91DKOtGqPKr6gXWX5xithflNd61DL9ojw8Bwec2sI3r-jTJDA45Q79R9UAe25_M6k8CO9zd0jUdErQWQvXjl6QU9D-_uAtPpR7d5ZjtbVlNRsij1qBowjvAKPO1F9kSUNG6N8VqUccxSaPxWX3CqrRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=mlau98Tr2UuV1HBhvsh5mlTpK2BHuYqMQdYqy2z_STlNF21ruaJqzV9bHgB9mfSRtIWF3ACC8qoIJbPFeY7p7OMkp15EA4YOrFD-oQG8R2cJy7ByieXCeWdxhhY_uVLbGSkBk7g54U4bvTasxctGgxH4dbSpeodMOICz6Y6U49R2k52hAXK7w3aSgH9o-d91DKOtGqPKr6gXWX5xithflNd61DL9ojw8Bwec2sI3r-jTJDA45Q79R9UAe25_M6k8CO9zd0jUdErQWQvXjl6QU9D-_uAtPpR7d5ZjtbVlNRsij1qBowjvAKPO1F9kSUNG6N8VqUccxSaPxWX3CqrRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czQnc40XTMKKUDSirAaUPQ6Enz53B1qPOVCAsDnXH9FZzwm4NiVfUMehMWN2Z_a60Lnj3rhLGgppaE3hhUvF7wOQd_qyIT6b9jEJQq4Y7vNKEN1lg88aPYAnlFV_CsZ4xPsMFrBELClbC7T4x1g9aBs4t-fgLZdTbGj8TQIiO4h5NwjSsv8N-LbDNuNAwCDYMZBimbGnkqQg3eljHJardJTT07pyCsR2gLRzLPGOgK2J2gD_5d_bDFoE999FGITbBMLiLq8XROioM32FwRLP6QdWCbatPawSIR0Ely_8mvTI4a_P4126zBAal6zb4yq_CpOl-SSzlF6waFtp7xelHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oOgcEzdeKtdRUkGKc_Cy9sZwQIjhCtpCSXvKfTJJTqJCv2ikbZ9tC-uVzIbxJICWNtXfh3K2qXwY1FtHKKsxvmbz5URn8VZae2E8pTnDVTG3ebC6bNEvNdBzr6r-D4h7qDvEoHdououB6LCwSQ8QUPOISB6V3wFBVcrVKMxmQ8lEN4rAPNLcXHYQhSAWKIHUqiA68-ZeXE6IPyhsE2MyDeHyzfAarzmOi-MaCYLPlfRzH6n-gtaETqEf4hh6hLeZetNyCBLp95F4bzFDz-UofBUa2hgDSsMhambVu3h3lY7zjpYoMkzjTgY7nAvxzbFz0mzZ6nEldewpzRsWzwonYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oOgcEzdeKtdRUkGKc_Cy9sZwQIjhCtpCSXvKfTJJTqJCv2ikbZ9tC-uVzIbxJICWNtXfh3K2qXwY1FtHKKsxvmbz5URn8VZae2E8pTnDVTG3ebC6bNEvNdBzr6r-D4h7qDvEoHdououB6LCwSQ8QUPOISB6V3wFBVcrVKMxmQ8lEN4rAPNLcXHYQhSAWKIHUqiA68-ZeXE6IPyhsE2MyDeHyzfAarzmOi-MaCYLPlfRzH6n-gtaETqEf4hh6hLeZetNyCBLp95F4bzFDz-UofBUa2hgDSsMhambVu3h3lY7zjpYoMkzjTgY7nAvxzbFz0mzZ6nEldewpzRsWzwonYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=q5Cwg0pLFMeRXguEqLS80tw8EYtSnCqoD-I3lluUBYUg70NXODh1ZpgGXsqBf7yUfUlxIFngBya0LTy4PAc9mq9Xi4EecBmmYeNcA_N2jEm_E-pl7uqb96x0LLV813JPMOGwbzseqpyRspunpQv0YDzozNbHWm0sREAzOkkOIX8pS1y6JqAPlV0Cydtn4geGclJAoX3wXvteUGpOQ1U-_orhwPPee08VXoGRN_mF6n2ANdySaxUjleh6ZeaPBKJzYZONxWDZzcE_T8thfXwhdUVqaKmR6w3be_46WPJEflmK35Itx1CW2u9k0YDHabkfe0UqnQILtxzXFAuMyJDyeJ6fRFSNjJb0qXrpUEYMdbwLyCPwvmQZVXu5LhxvSNQm0usHDpAtT51VrLGCjRXllh_SScLyEWt0GSQPmlepAQJB4h2VNIXJZUsnzmKNlVrN7U3O9RhujspvfgdsOpvTZsxUxiMGtSdaqvtr1rWZO8UH1ZhGWcQRgV8l5R3i8SxUZQS816l0XlHd7GPePH36m8qQy62ET490lj5tZYuzNC20yp6cn6wLAHN0LF972EIFdHidhp4vf2LA-61PasCZlOG8svF229xi2TGprtrOasCR4DRqBBW5xNvBIAoG07KMv162DCSAQSFNvKM9zIlCujEa7rdVwRXlOg0rZmbTzUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=q5Cwg0pLFMeRXguEqLS80tw8EYtSnCqoD-I3lluUBYUg70NXODh1ZpgGXsqBf7yUfUlxIFngBya0LTy4PAc9mq9Xi4EecBmmYeNcA_N2jEm_E-pl7uqb96x0LLV813JPMOGwbzseqpyRspunpQv0YDzozNbHWm0sREAzOkkOIX8pS1y6JqAPlV0Cydtn4geGclJAoX3wXvteUGpOQ1U-_orhwPPee08VXoGRN_mF6n2ANdySaxUjleh6ZeaPBKJzYZONxWDZzcE_T8thfXwhdUVqaKmR6w3be_46WPJEflmK35Itx1CW2u9k0YDHabkfe0UqnQILtxzXFAuMyJDyeJ6fRFSNjJb0qXrpUEYMdbwLyCPwvmQZVXu5LhxvSNQm0usHDpAtT51VrLGCjRXllh_SScLyEWt0GSQPmlepAQJB4h2VNIXJZUsnzmKNlVrN7U3O9RhujspvfgdsOpvTZsxUxiMGtSdaqvtr1rWZO8UH1ZhGWcQRgV8l5R3i8SxUZQS816l0XlHd7GPePH36m8qQy62ET490lj5tZYuzNC20yp6cn6wLAHN0LF972EIFdHidhp4vf2LA-61PasCZlOG8svF229xi2TGprtrOasCR4DRqBBW5xNvBIAoG07KMv162DCSAQSFNvKM9zIlCujEa7rdVwRXlOg0rZmbTzUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-5ZNdoouDpvTXvtsWTDewsVGfYQvGZw67tKl_tyeBtmWrwhpCiO0ggQpwxbSpa8xYi8xcYj_y4w-ciO1A_oyD7d_DpVeBwL3EHAYHLDH2f-0ZErIaXcEBb3Oru2qntvSHf17n5W6TArJ10HLDXnTelJHGz8cD5uvc9S2Kq8Lsz9SZ4_HTPyoQ9EeA8anMP58M0ujKkP7B1Naais57aZ9jDJghzV-MNhewt0xgXcjytFIUxs_B4T6hzYS0Pv_oMWeff7IdI6azeHmxMqOcNM542nnNf05StSf2gyCJ6NZKxw22qZTkSjcHP7GAjx5NV0oWTEnse2II5JcvzDz0Iz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=GEQuX3ER8b79vlP8vHZMW_c-GK5nwP0b3UiflEihdJBf_FxpZVB7DUqdtYNToDbezMkamASGI5s5C6Tw6VNlC8jL1jNrb00y93CBPQRXh1uVldFpGDFy_3K0nfd1jDGeXrAzukECOBrhGDt73ecAQQ3YPUNA__JpqTStA-3lim7HDnJwIBrjZaQFki0xrfvRpXfhsN_W4zZzY0bzEu-sFZvasuSCkVqsCUe7fMl3PAnzyfklAQkrjxW3iABbAStb82cZU29f3smAPEWcKjbaKpZFzfwebiYQ7W5dYnquhZ8ct_AIDqpC9YeiUIuyOV4NmKvra_GF7c1B6eA5hAQ19k5jzR3aID8NxNgU2naHjQCvrQ_-OUwkdCro4VYIHB23Q1NAjReVm0lJLCc7PtO3T2XjP5-wuyyFuejh32WUDMCqgzUhn5cgS0Zm-ZNmc3enmOoBjoW4qOEV065UH8sRmyjjty_tcRhoH3fkJ_9ixmGTxlhsjOpmDmlaPqQKmXD7-JGhts17fsLEZx5DpaW-uryKuCPOejZG5MrXU0tH37RmKbQtONld4S1iQ1oCuLT9PtV3e6dcMvIYUM4T329n2V3OIy4hhbNYBgEjfCLU_CJ1AALHBq352vFjk69Ybvcq2orBpUUPhPERM0dNBNteLQoe1lr7WWjskj4bNqf7p2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=GEQuX3ER8b79vlP8vHZMW_c-GK5nwP0b3UiflEihdJBf_FxpZVB7DUqdtYNToDbezMkamASGI5s5C6Tw6VNlC8jL1jNrb00y93CBPQRXh1uVldFpGDFy_3K0nfd1jDGeXrAzukECOBrhGDt73ecAQQ3YPUNA__JpqTStA-3lim7HDnJwIBrjZaQFki0xrfvRpXfhsN_W4zZzY0bzEu-sFZvasuSCkVqsCUe7fMl3PAnzyfklAQkrjxW3iABbAStb82cZU29f3smAPEWcKjbaKpZFzfwebiYQ7W5dYnquhZ8ct_AIDqpC9YeiUIuyOV4NmKvra_GF7c1B6eA5hAQ19k5jzR3aID8NxNgU2naHjQCvrQ_-OUwkdCro4VYIHB23Q1NAjReVm0lJLCc7PtO3T2XjP5-wuyyFuejh32WUDMCqgzUhn5cgS0Zm-ZNmc3enmOoBjoW4qOEV065UH8sRmyjjty_tcRhoH3fkJ_9ixmGTxlhsjOpmDmlaPqQKmXD7-JGhts17fsLEZx5DpaW-uryKuCPOejZG5MrXU0tH37RmKbQtONld4S1iQ1oCuLT9PtV3e6dcMvIYUM4T329n2V3OIy4hhbNYBgEjfCLU_CJ1AALHBq352vFjk69Ybvcq2orBpUUPhPERM0dNBNteLQoe1lr7WWjskj4bNqf7p2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pjLQOYb6l6dGwvuAHHPOLVPJ8V4tIkLIyi2MTvB2G_p0x9GvqMT7j4rIzWF8pvoGggG66bIuZlGxUBuvB9hxHI8pxeEomTSI9Q2JLuecoHYz1rSjdjhhu5-itZn-TIKslNmgYutqNgvmp_JnhNHdzwJqJhc_mZakbZSgVXX5KtKcq6_F-3gsW1HgsmjbElEQMGpPtjhnJFG7vqnbBEKlAyE9SjwI1m7c2MPO9BI0dR2Fh-va6-lffYPr5acqr-FHGZVGaJUtpnMtigAo1dwVKDQP7-JntQuE2JXIN29ChaTdNgJxyw8j-blFa9AG6t1vBqIMAPpc5cJksecp7xhnGjhyHfMS9fLu0LNRvmlRMC2YOrBizKNK3DkXYgwMVr45S2joONyrsuej27jkfeis3Oqkw1QcowzM2LIoBygW702tsUz4_7ym90BYS5bZTc0EetJ9xrhdTJpf13xsT4foGOpG4bbCwEqF59NkJ3dtVQSE9S4TOvxIn73Irutwh6dIgLaE9XZBK4ygHeLU4z9pDaXVLqA3hUjbMqqoaJuIlTXLawfpoa4307k567oY_EyBnpVDHhckTC57yOxxi6ITu_GCVK4HYCc_74TmxEqLbTboVRstJr7_dcBFgJTd11BDXwrKAKFR23v0pe3yNeFfvOcZd55TqEtNLATrSM12MRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pjLQOYb6l6dGwvuAHHPOLVPJ8V4tIkLIyi2MTvB2G_p0x9GvqMT7j4rIzWF8pvoGggG66bIuZlGxUBuvB9hxHI8pxeEomTSI9Q2JLuecoHYz1rSjdjhhu5-itZn-TIKslNmgYutqNgvmp_JnhNHdzwJqJhc_mZakbZSgVXX5KtKcq6_F-3gsW1HgsmjbElEQMGpPtjhnJFG7vqnbBEKlAyE9SjwI1m7c2MPO9BI0dR2Fh-va6-lffYPr5acqr-FHGZVGaJUtpnMtigAo1dwVKDQP7-JntQuE2JXIN29ChaTdNgJxyw8j-blFa9AG6t1vBqIMAPpc5cJksecp7xhnGjhyHfMS9fLu0LNRvmlRMC2YOrBizKNK3DkXYgwMVr45S2joONyrsuej27jkfeis3Oqkw1QcowzM2LIoBygW702tsUz4_7ym90BYS5bZTc0EetJ9xrhdTJpf13xsT4foGOpG4bbCwEqF59NkJ3dtVQSE9S4TOvxIn73Irutwh6dIgLaE9XZBK4ygHeLU4z9pDaXVLqA3hUjbMqqoaJuIlTXLawfpoa4307k567oY_EyBnpVDHhckTC57yOxxi6ITu_GCVK4HYCc_74TmxEqLbTboVRstJr7_dcBFgJTd11BDXwrKAKFR23v0pe3yNeFfvOcZd55TqEtNLATrSM12MRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=oHCbytpFd9cL6trOoKnJSVH44aE9PdysqFb4oRPRJKscrKW5Fui8mgTX2eN52L8_OJB14-BpqFLSij9dKgaltx1IumwSleYgVjMWLgtRLFTXFBq8_7D1GL8iOUcJun0D-wFS6nOAYJfs9kcGy9mFitZ30UmSq0pe_NuangM0GcNActGABvhzrythJM_cFJ1Fc_CN9Qw8Bv_6t5bDG6bq_4YKM-PhuXrBH1jSlW36NekvtsHySbB3AvLjEVvULOdxaAgpBPNDDqJk1vQLn6M2k35IBErq2auy68jR4v0_pXzqugQd1KYhP8Rg5b-aQNrc_gXyZxrGgHJjK2I8ap_C0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=oHCbytpFd9cL6trOoKnJSVH44aE9PdysqFb4oRPRJKscrKW5Fui8mgTX2eN52L8_OJB14-BpqFLSij9dKgaltx1IumwSleYgVjMWLgtRLFTXFBq8_7D1GL8iOUcJun0D-wFS6nOAYJfs9kcGy9mFitZ30UmSq0pe_NuangM0GcNActGABvhzrythJM_cFJ1Fc_CN9Qw8Bv_6t5bDG6bq_4YKM-PhuXrBH1jSlW36NekvtsHySbB3AvLjEVvULOdxaAgpBPNDDqJk1vQLn6M2k35IBErq2auy68jR4v0_pXzqugQd1KYhP8Rg5b-aQNrc_gXyZxrGgHJjK2I8ap_C0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=YKeBRk6dr9f0czALxHQJQ23L-qB6a_eZN3TG5MzB8bEz4hEc6g9fDNneHHcq3a9CBh8ZBOz5YjjzCkApDVXAG3N9MolQCjGpYJlMG6ADw0hQsU_Q6EerjF0I9BhcH44LkIDTVWtOiVLHhFbaAkJYATLG7nq5A9VTfb9ihbDIwiIRU_hSNV-IUPCyeZaw5Pxq9WJoRcFRFcJP4nOxBr-BL5LbKV5WRpJem1Xp_LwWyi_PakQahGGjarXP-kvZag1sjzJEJG_1UyUhCn5mmXa57z2USfjVrG1gYNPXrVhZdGHt6lJYDH0pJBboPM0k_ql9xqBL261EhM8igHw0BoBa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=YKeBRk6dr9f0czALxHQJQ23L-qB6a_eZN3TG5MzB8bEz4hEc6g9fDNneHHcq3a9CBh8ZBOz5YjjzCkApDVXAG3N9MolQCjGpYJlMG6ADw0hQsU_Q6EerjF0I9BhcH44LkIDTVWtOiVLHhFbaAkJYATLG7nq5A9VTfb9ihbDIwiIRU_hSNV-IUPCyeZaw5Pxq9WJoRcFRFcJP4nOxBr-BL5LbKV5WRpJem1Xp_LwWyi_PakQahGGjarXP-kvZag1sjzJEJG_1UyUhCn5mmXa57z2USfjVrG1gYNPXrVhZdGHt6lJYDH0pJBboPM0k_ql9xqBL261EhM8igHw0BoBa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Omp8WkIv6btO6is4X90OS1g8xZq8ZghpVYqZL_ZuC3CFehIILNQlPlbSjLXFZTkgSTKNiw-keBaI6AeyKYpLSe8a_GSA6Y86q0Qyl3edaHfEB0qOO-1nFSkSmk2YImw0frXAXi87AKFqaHtQZu3FJfOFCre5QTeLF4HvvMjjbb1hti5177_1z6m_aMKLIly-MxY3o31boK4yYkbFm5o25PYq0mAG9tat0_GWRPmJp_x17aaGsyhSZ-dke4tgHFW_hn0lP7HhBcv8i7jVkjfYZpYQbARhUGzwhfIDF05m-7pOwiJAKmgxgk_AiC7vCIVYEULTa1eS2aQns4HfIJQJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Omp8WkIv6btO6is4X90OS1g8xZq8ZghpVYqZL_ZuC3CFehIILNQlPlbSjLXFZTkgSTKNiw-keBaI6AeyKYpLSe8a_GSA6Y86q0Qyl3edaHfEB0qOO-1nFSkSmk2YImw0frXAXi87AKFqaHtQZu3FJfOFCre5QTeLF4HvvMjjbb1hti5177_1z6m_aMKLIly-MxY3o31boK4yYkbFm5o25PYq0mAG9tat0_GWRPmJp_x17aaGsyhSZ-dke4tgHFW_hn0lP7HhBcv8i7jVkjfYZpYQbARhUGzwhfIDF05m-7pOwiJAKmgxgk_AiC7vCIVYEULTa1eS2aQns4HfIJQJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WazHi592Ka0WbrhxFiRLymeKf0fIFaWU-AcD_0Yk8NgzbchxpiXJo8b_KHjp0gcMMMXm3iUfLq3bQ2zBLuf1VXpWncB3iYFHsSg1by_HQDy57GdGLhHiP5JKhe8moIIInRAasWzmj8kdIwxQKUnIJnUWqy_tRXvlmWTKl_DN6jACQeK0Jk5t2s_PRZb-4Z9nA0XtSYYzTEJy_5vZPDlTYkvMx-6X4vGQTAekc2CbhJkIspqWyHrc2uRvRH8yN2KYSoUZ7_MJSs3lVuwSPtIFLzYZGfYY4Mb6nHprMMwVGcoRwVo_o_TA7EqDobK0l8hLjOcKmMsDtY86ySeQgSyfbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WazHi592Ka0WbrhxFiRLymeKf0fIFaWU-AcD_0Yk8NgzbchxpiXJo8b_KHjp0gcMMMXm3iUfLq3bQ2zBLuf1VXpWncB3iYFHsSg1by_HQDy57GdGLhHiP5JKhe8moIIInRAasWzmj8kdIwxQKUnIJnUWqy_tRXvlmWTKl_DN6jACQeK0Jk5t2s_PRZb-4Z9nA0XtSYYzTEJy_5vZPDlTYkvMx-6X4vGQTAekc2CbhJkIspqWyHrc2uRvRH8yN2KYSoUZ7_MJSs3lVuwSPtIFLzYZGfYY4Mb6nHprMMwVGcoRwVo_o_TA7EqDobK0l8hLjOcKmMsDtY86ySeQgSyfbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Bmn0MQGepYHgAdcZU2YgCFvvw-PYhynIwpLtohLXLUdFNQjDOmwwUeEFIGC2SHvEcwytq4hlLbmWjBRWXRmaj5AEsdsTjz20bppD7X9nhpeJ5GauG0zI7XKZPQobeicZbYPcQZASgIAtvnsCo7IU8r0-PmWPmU4C0QLggU7P1PieqfwhHJdAzjhdH9BiIKMUXUC_brvaZ1k5N90MIuCcp_RwohVax5bZ9xt1-HaP1I3KYvqDEf-VjMVTFVJ6vJzKDuAcgZ8AaNk2igLPzgUmENl2yMQld0J9AWyff-1pztEYl3sVIosVC5INeEb-ZRTJqp8QaeOd9oQGeGqncdhchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Bmn0MQGepYHgAdcZU2YgCFvvw-PYhynIwpLtohLXLUdFNQjDOmwwUeEFIGC2SHvEcwytq4hlLbmWjBRWXRmaj5AEsdsTjz20bppD7X9nhpeJ5GauG0zI7XKZPQobeicZbYPcQZASgIAtvnsCo7IU8r0-PmWPmU4C0QLggU7P1PieqfwhHJdAzjhdH9BiIKMUXUC_brvaZ1k5N90MIuCcp_RwohVax5bZ9xt1-HaP1I3KYvqDEf-VjMVTFVJ6vJzKDuAcgZ8AaNk2igLPzgUmENl2yMQld0J9AWyff-1pztEYl3sVIosVC5INeEb-ZRTJqp8QaeOd9oQGeGqncdhchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=HYbxRMkaY__5koXDH3sNGZjtAYUDQI5x2ElmjBmmvo9i4yomv6uZ0Ids2-8lAIVb_qMr1nrhL6kzadNo9pfWnX0p-g1sEquCbisXsSXMKLuaq5O4aqnb5Puc9I9YYE29kdE0lAVkMBQWERv01rKmekRBMWqVtdQUAtA2B9NvaZHyYR3Dqio7HKc4sxoAa0vrm2ne00bxbkHUQ6qqqBSUFpok3mwSjyWGnXz90uBxE9OsMH97d9fE7_e9AO5XaCheti0DOl806lR3Ul2KwyenKikva_Kr2ibKFxmNk8Ski0yNQ8Oq5HjrVdVCVg7_E9zwpc4Hl1i4wWy6YYtK9MYucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=HYbxRMkaY__5koXDH3sNGZjtAYUDQI5x2ElmjBmmvo9i4yomv6uZ0Ids2-8lAIVb_qMr1nrhL6kzadNo9pfWnX0p-g1sEquCbisXsSXMKLuaq5O4aqnb5Puc9I9YYE29kdE0lAVkMBQWERv01rKmekRBMWqVtdQUAtA2B9NvaZHyYR3Dqio7HKc4sxoAa0vrm2ne00bxbkHUQ6qqqBSUFpok3mwSjyWGnXz90uBxE9OsMH97d9fE7_e9AO5XaCheti0DOl806lR3Ul2KwyenKikva_Kr2ibKFxmNk8Ski0yNQ8Oq5HjrVdVCVg7_E9zwpc4Hl1i4wWy6YYtK9MYucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FVBd-pDSmBoJjFk7ja8OOZozbH6lrXIRuSexcPTySltLHrirZE36WAZhdAt7pp777uebqm7RmAPBuBNzIU02xqDlrUDRGzADpMlqAK7rpYFA_xmYlh_Kuw9Cwk9YreQqy02yJLjZkCjE-WGRLepprZ5kytT7R2XP36Ey96lhsz-z7GFi3uFFTv1Z1jedYDSBvFNN5Qq9E0B6caTfwgYAbXfgG7VNaNJBncI2ufRsjZjpyZGSVAU5yyuP_kXNKe3q05txUhHwN9M8QhfBWgGeWdWY58IrY_0cvBylzthu36EyuakikvP0rTuqIsnHSZd40VWqFh2HAmlcCeIf7ZCb7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FVBd-pDSmBoJjFk7ja8OOZozbH6lrXIRuSexcPTySltLHrirZE36WAZhdAt7pp777uebqm7RmAPBuBNzIU02xqDlrUDRGzADpMlqAK7rpYFA_xmYlh_Kuw9Cwk9YreQqy02yJLjZkCjE-WGRLepprZ5kytT7R2XP36Ey96lhsz-z7GFi3uFFTv1Z1jedYDSBvFNN5Qq9E0B6caTfwgYAbXfgG7VNaNJBncI2ufRsjZjpyZGSVAU5yyuP_kXNKe3q05txUhHwN9M8QhfBWgGeWdWY58IrY_0cvBylzthu36EyuakikvP0rTuqIsnHSZd40VWqFh2HAmlcCeIf7ZCb7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5bPcnBrfuhU-IyuYvDph-j2BTjQde4_Y_nsPUulhfoN8lYGmYRd43_Fxk0RQyvRZX9hgKmh8y6eNL3nj1XTJ7BgX2s2yq8jcYw2sVL1tB8vkFQkKb2VJ1HTj39w2SxEfExmDd4Jazz-H3HJ9_GWRcBZdocQyyBui7sxUPoFLDj9Um2eyV57eC8UpER3bi0KpVmIIakoroe033cSWxlkADfJDZ6-egwiSlHQBwqL27pfJmwSSudnCj9qM2e6BjZ-VoyoxSULa4pQbsLcMajDJdg5SKA4Vb7KZr4njsxu3bGGLAOI-vTLJCN0-_hI3EnPgJnvorD1pF4nm19iZ8EVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BAMBxCQNcWBkTLFz-Fxf8LqtlVRSxxNFZ12lpmRyUNSfBHW6YJaFzuP_TUHZATtNUZ9cY6AX8BY7EpdzU_9SMkRxx2pqAjSwVUg3FJWMO-sBOC6A2Rh-WvhmEgbO8IUKjqR706MQtMlhT9mt8BFnNIQek9OtVb4Bed5uh7aj1ZYJUo4s6oF86yQey-UJAH_ZHWvFd0fUKG_zGF9SYTcGmx7VipUKpKMckrTZhf3ht9ijmH2-QZlK_zy_RU-Nx6-RBXMqZ-BqDs-He5XPceiRUvJUaxR8f8UCdslHDs7B10k-WzH5jKFwTQ1zEIEj9DMOJk95k30hTa1nJhkVWQgJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BAMBxCQNcWBkTLFz-Fxf8LqtlVRSxxNFZ12lpmRyUNSfBHW6YJaFzuP_TUHZATtNUZ9cY6AX8BY7EpdzU_9SMkRxx2pqAjSwVUg3FJWMO-sBOC6A2Rh-WvhmEgbO8IUKjqR706MQtMlhT9mt8BFnNIQek9OtVb4Bed5uh7aj1ZYJUo4s6oF86yQey-UJAH_ZHWvFd0fUKG_zGF9SYTcGmx7VipUKpKMckrTZhf3ht9ijmH2-QZlK_zy_RU-Nx6-RBXMqZ-BqDs-He5XPceiRUvJUaxR8f8UCdslHDs7B10k-WzH5jKFwTQ1zEIEj9DMOJk95k30hTa1nJhkVWQgJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=J-8tvJ9JqCb_leqw6VSv49BJO9KeGwjS3KOdOZSroYby4jE-cEqyvndspkZXPD-6mgVAaUkmB7aROxHdmTeeVttdC1aVNyVOk77TZBpmnqDRd_roAjbyf1KgkvmHEwVOxX4A1B_ozx1iXuYTUBspG6vKn4tnKQcNAuLKdB4Q1KxjOPUKkT3SEcoO0lUVLEZ3Ga2RQxRFX_xdVQGV92J_7lopzGTCkTQSvWwB8bXO86cNyDEUkaAKdZ0GD26CKx4NYDxjwrq5o6m8K17PYYGIgn3G-VQ0CAFtZRux_1Il0MqDbDnPVEy0jD0WccUofmlHvxLpWR-0xqLDUVs5tR408Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=J-8tvJ9JqCb_leqw6VSv49BJO9KeGwjS3KOdOZSroYby4jE-cEqyvndspkZXPD-6mgVAaUkmB7aROxHdmTeeVttdC1aVNyVOk77TZBpmnqDRd_roAjbyf1KgkvmHEwVOxX4A1B_ozx1iXuYTUBspG6vKn4tnKQcNAuLKdB4Q1KxjOPUKkT3SEcoO0lUVLEZ3Ga2RQxRFX_xdVQGV92J_7lopzGTCkTQSvWwB8bXO86cNyDEUkaAKdZ0GD26CKx4NYDxjwrq5o6m8K17PYYGIgn3G-VQ0CAFtZRux_1Il0MqDbDnPVEy0jD0WccUofmlHvxLpWR-0xqLDUVs5tR408Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=G3EyUtyxYt9StKWjxIm5CDsSh4BEtgSPCj8rSq4eGSp9r-KQjDqBPI2bpaDe_zAC0Eg9o7Mndh1damQFcNbKi5p2tohpvsjS632oiH_UdXp5O4i6Zs6h-b00cr8sQjsJxwxn0XH9TXu2ZJmQ4T5z5DVNVqQNd9wop3NStzimwRU2Z-FZA_wGgr3NoPSuf67jzfKaFPIqmXZ1tTEPEsV_pE7_kxr1MOG131c4GXMnaLAlfquXwIzlH46-PkYY-o81Odc9U5ec0uYc3dmzAo96nNlqfFIPWoB8zuOpEfLBzaupQ46wIH9QmRIRfZBxRgKpS2D34Z71Qg_GIiWwLRVUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=G3EyUtyxYt9StKWjxIm5CDsSh4BEtgSPCj8rSq4eGSp9r-KQjDqBPI2bpaDe_zAC0Eg9o7Mndh1damQFcNbKi5p2tohpvsjS632oiH_UdXp5O4i6Zs6h-b00cr8sQjsJxwxn0XH9TXu2ZJmQ4T5z5DVNVqQNd9wop3NStzimwRU2Z-FZA_wGgr3NoPSuf67jzfKaFPIqmXZ1tTEPEsV_pE7_kxr1MOG131c4GXMnaLAlfquXwIzlH46-PkYY-o81Odc9U5ec0uYc3dmzAo96nNlqfFIPWoB8zuOpEfLBzaupQ46wIH9QmRIRfZBxRgKpS2D34Z71Qg_GIiWwLRVUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Lc38d0iERvizNsTMMeMDkli_NxjTaIZpaRfWqk2iiOamq8L_QpkJmEDA-8RCx16u_Xh2FIexEmjUBvtigDWtpU3pE9Tj-THXgjGBlgsghfLpDXk49jGKvs99-q8AbNSQQLvvYwCXrC-gF18i_lMBaSyRh_t77r_5uF_xCxShN7gfLQ2lZFY--FZOb-gfKZMrS7zhW6mXaWj-n-W46eAOeGB72V1xC1DW5FvMcMdxRXV1renhwwKVtcAbLvUt3ZDAAkailIdSH17gYVsk6Na2q5giiT9hTEn5HN7wxfbsmD9De9_f_X3wLeMQnGk5dKsv7b0It1j34_4xWAZLl7FkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Lc38d0iERvizNsTMMeMDkli_NxjTaIZpaRfWqk2iiOamq8L_QpkJmEDA-8RCx16u_Xh2FIexEmjUBvtigDWtpU3pE9Tj-THXgjGBlgsghfLpDXk49jGKvs99-q8AbNSQQLvvYwCXrC-gF18i_lMBaSyRh_t77r_5uF_xCxShN7gfLQ2lZFY--FZOb-gfKZMrS7zhW6mXaWj-n-W46eAOeGB72V1xC1DW5FvMcMdxRXV1renhwwKVtcAbLvUt3ZDAAkailIdSH17gYVsk6Na2q5giiT9hTEn5HN7wxfbsmD9De9_f_X3wLeMQnGk5dKsv7b0It1j34_4xWAZLl7FkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgIFXqGmsLt0TfInF0GDA0pIuaY8KYVdpuYI2XLzoDDp4da2Z_aIVdUZEC3GB9BaP0-z6jGjfPmJHcGbBsiW295rbUpGVicJvA9QX2MbMqwMlwluTRkwRmP5BQNofOdqMWbgF_dRpiryfAmGVG90T7YxEUNCDngb7h4504BgvaXBh3gS_KiYNIO_c_ryOYDRJFb1BxnMzEAsfaL_ambX4vnVOmy_ppLkm_BCwhWX2jnR-eErUaSqYVfpu71HFgxD-eC4m203KpgpzE_83ryvgpEblLHqgnpLpW5k65lxbC5I2vr5IDhn_hH1wi0KV6M6RBeWbBApkkbkctxtu3vk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jX2TWqvWF-DUznj1m3jZtPsftlqCCb-y6p0KAftfJRvHtvoicSI3Ez10_njKAuVl06HA-QgtrNE_S0NUC-1bPOw1NhWgB5sYFBv0YwqZjve4_5KYRSyBE_sSlpvFD421_DbBQ3TqVoRgZC0AccoI3dl2h8gpM7EKcdgXCtOoeCN3A8s1SA7_cVf0zsKhd88ji3Fb0ptg6BH9-4RmSK1B0af8ZdxwuzZpts-wmxBmYr2OOg-NSqGI0mh6eb7uhwPYlwI7DSR0zYF2x4B00rM22X2z1mjFkWAqQhtY2UP_CZr-tBh-G-YsYFfSCtobCjmymZ73Xl3LtP49trI3WLJ9pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jX2TWqvWF-DUznj1m3jZtPsftlqCCb-y6p0KAftfJRvHtvoicSI3Ez10_njKAuVl06HA-QgtrNE_S0NUC-1bPOw1NhWgB5sYFBv0YwqZjve4_5KYRSyBE_sSlpvFD421_DbBQ3TqVoRgZC0AccoI3dl2h8gpM7EKcdgXCtOoeCN3A8s1SA7_cVf0zsKhd88ji3Fb0ptg6BH9-4RmSK1B0af8ZdxwuzZpts-wmxBmYr2OOg-NSqGI0mh6eb7uhwPYlwI7DSR0zYF2x4B00rM22X2z1mjFkWAqQhtY2UP_CZr-tBh-G-YsYFfSCtobCjmymZ73Xl3LtP49trI3WLJ9pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=HLjYmwahz27liOgYUDH4-JVUhW2SPTOQ6szjHB_f3oIzCzprNrIbwC097kYrj0M6UtMMDCiLx9A3XL7WBkmjH7nYosShCm2G0Ru6-U9cy1My-g0qyOfs7Vgs2g9PBa87dFGXgmbIGEQBvmZPrvjUBPTXKvtRIJa2e0JT76HjzlyW9ptzEfBSatS_hMuNYl4EG5KW2LLjXRmDCnLoL5zMHRSqUSP28u3CnSa6LF1DIIU00yoEHMCwlS_HPejh069Qv5FVCEcFkw2XWy62F6w4nuwDdAiG93tHIvjBOUGqbCveKSu_IQmWrzY1VmV8w31TkVXWpYXbSY9HXnk1UEcSjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=HLjYmwahz27liOgYUDH4-JVUhW2SPTOQ6szjHB_f3oIzCzprNrIbwC097kYrj0M6UtMMDCiLx9A3XL7WBkmjH7nYosShCm2G0Ru6-U9cy1My-g0qyOfs7Vgs2g9PBa87dFGXgmbIGEQBvmZPrvjUBPTXKvtRIJa2e0JT76HjzlyW9ptzEfBSatS_hMuNYl4EG5KW2LLjXRmDCnLoL5zMHRSqUSP28u3CnSa6LF1DIIU00yoEHMCwlS_HPejh069Qv5FVCEcFkw2XWy62F6w4nuwDdAiG93tHIvjBOUGqbCveKSu_IQmWrzY1VmV8w31TkVXWpYXbSY9HXnk1UEcSjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nstCf8Kos10RJEQz0Y1VIp4Ex1PsEXA7hRh4-4-faZBMKGQFsj4kqEYEJdMx6eTPzIpDRm9_aOGKev4y3tl_tG3yxtFhYlLXiuK0qWtcSgWElw3eKkWPMV8TDYmGYkuz7vGcw0Wknl7yoyfHc4fDVtlnwNVQR2mDV7F8FqStj2k9GpTDBLulWXDb3JjK3X45zdMW6e-g7Cjoh7kwWiQtMvhsH3uBpJOC5FljuAerhNw3BSoePRy901-e_HikLbit62v-FGoC4RnV_5998Urvp0-zonZw9yZVEpAbd-iVNE6QaJO39z9h3_rCGkDjN64J66ScTNFxeui4yDee_09c8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVOthE22Ljag1qbSpo90vBGZRQpf98RwLu_q9vMi5H_aDqaUgJKxbdMUXGw9BGkv6b3QZmg0ES1KHYd04eFVY85o-ShA-HpI2_31IIWf9ip62WyUe3QzkZj9ER7pKfTFY_IYxco-9gG6vLUi4aHzz3vbr-_Tnxdxz8HkNHzs7253ARe_WjtcrSllbAPWCK7BVa-inKVgV_MJWTDi03_JjFq9gyX9K5vRteiyXW4mty8xpsofBul-7xAY788GiOen94PA51GJqwcmWsfAOPHi3X82wYrZlsfoHmzF9H162SLNYxzW1BK5CzHWoh3Xb7wiOeWRzzw2q7HNRV2bXQDvMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Lukfsm6J_E_DfLb2Zw6b_8xkq7gtO1DK9hK2kG3hn4zHYiprbK7UzJRq7vmED4H9H4k555FQdmqD6-IOB6leEAJ2dxKuiKHS1znEfM6y5DvwExYJcolul4TuuN-XSfBHMz5RIQm9PEBQAnRsG0tnq4zrUUr7mit_lN5KqqTf43AMz2M8lKrYepwnQb92OMibfIVqwbuXxUdPaO3lhmAz32TBARwq9x4zqktZRm_6YUkldu5ZaiuFo-n5kxoZjeARt_v4j93PpqlaPG1FIC4_Z2QLLEyrb1QdR5ShYqopUpR5UChJy4XCNPYWg7ROmbWYXQzJA3d-LfrQ654G7JtDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Lukfsm6J_E_DfLb2Zw6b_8xkq7gtO1DK9hK2kG3hn4zHYiprbK7UzJRq7vmED4H9H4k555FQdmqD6-IOB6leEAJ2dxKuiKHS1znEfM6y5DvwExYJcolul4TuuN-XSfBHMz5RIQm9PEBQAnRsG0tnq4zrUUr7mit_lN5KqqTf43AMz2M8lKrYepwnQb92OMibfIVqwbuXxUdPaO3lhmAz32TBARwq9x4zqktZRm_6YUkldu5ZaiuFo-n5kxoZjeARt_v4j93PpqlaPG1FIC4_Z2QLLEyrb1QdR5ShYqopUpR5UChJy4XCNPYWg7ROmbWYXQzJA3d-LfrQ654G7JtDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3LJODdE9YJJuSeaJFV_MnoTKgtXuoaLeEy4WwrJj8iv0S7V5JNcVwh7C5pMH1568p1EvccnFPaJUtVaZyhdOv0-xJScTmnvPXU1gMksQnBrnNIS82hmv04-DMttWae8HKixV3q8XJPOfH9581DGgtY-vBwHrmzPm1IzqHcPjE3FZOQxBb8W8nXpsexGhxT9ZS9Jg1s1CWuiDWsp7S7d9eOBKFkXRfd3XhSbRM-SVzRaQqvdvtMYWvi9zlYTn6sem2FZdibPy4Z_umPZKXJkWU986srWPmRyd8gZ0JJ9tkN0VYlkxZhENglNFJVuZR0VHJ1IndLi9mIC93cU9EaQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Q3d7jt4Nqmlnw2NCT4WpV7qb-5UNIneo0PbsDsnjWh_4u101ApDkT7IX1Ra95a13kfRy_7BsMBWidoW80NSTCGcKSBXw8bY4ukQ71fb-NUDcXOSSPm7EFsfmP6L-Wt1hjTs75nx49h-3AxMMmAsZmbSnQ5NBh0G8ulVxVhd3BfQ0NF4E1bSufYIG8RwEWdZzelbYpJX8Qw5PbJJHvlngSsLr1EhGu266xp3lnNm3pIozHHVUukMOKzlbdSNH-3BY4bluMlVcWuP5csM1T03iqWIY8GSlGdO0P02Goa7gdzUtJloHPFWNvLL0KbIb-m0qZj5PjIDZa2qsjzudvPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfhpG8CPmFfy-EFqTmWbP6X1nc3Y1qZhep6X8145sJBF2gW1C-X2BbffiUms06tFAoTbREUCSqN9ZhOWUSZk17oKarsoYuzbdaRQGqHX0AyaZoSrDt_p_8xVe_vFOqUdGtN9vgYrw6-K6KHm_AQTiafOfv-swEvipxOjeT3N8Yk1z_9cRkAWl4LNArNI4eNBTvTC4z3KS78z0LZ9BlwhGxqwYZTsQXxVIdR9QCAsSnD1-Xrmq1xt1APmlnR8daL6gt95YOSsY6GJj8ntae3wROt4eNffjMCRmRAw93V-kcPw2D7XCd728hvgnZx8hLiETGgoZJ08cXtj3Ogf5oGiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=f3C3CPvdvmuq2oiDOm0YjkH4CWQJvRJgSyzm82DDWwhIrSugl0bQXX6DbVggtWuuXjDlx5xe1yg8ktxnxarBH9MicVU5gwX79NpSvjbAkBPhL-V1dQMkiQI3CWLazeNvndzsEWfqn9kDyCPV3dFX6wdnCPXqFM3829GjSyLehYRq58ehelQoxVYvxSV73ydXfxeVnxnSCY21XF6ZjWI16T_HI0Ef3pQVCUs6oDIQxw6hmzEDGwb-ZMWgU4C40MEo9ecuaxVrrunBQ7wG_OdDMnizEjWr8aiGN8x256-vr_qX5ViEFTidTt20dz6t5vhpXXa_D2tiza4PQ1HTp28cng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=f3C3CPvdvmuq2oiDOm0YjkH4CWQJvRJgSyzm82DDWwhIrSugl0bQXX6DbVggtWuuXjDlx5xe1yg8ktxnxarBH9MicVU5gwX79NpSvjbAkBPhL-V1dQMkiQI3CWLazeNvndzsEWfqn9kDyCPV3dFX6wdnCPXqFM3829GjSyLehYRq58ehelQoxVYvxSV73ydXfxeVnxnSCY21XF6ZjWI16T_HI0Ef3pQVCUs6oDIQxw6hmzEDGwb-ZMWgU4C40MEo9ecuaxVrrunBQ7wG_OdDMnizEjWr8aiGN8x256-vr_qX5ViEFTidTt20dz6t5vhpXXa_D2tiza4PQ1HTp28cng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=HFTDTMCb9J4-OuBBSRCwCJkwDXnX6mt5OCnk4zkTgXa37WyXZw3Pyej3QsT7bw9XGmOgl9Crn5-y7WKQ_u9X67mOBXiP4FF4EOrJnE1mLwLVUHu6LiPG_WLvZFhpGlMZTRN6aTaCWAIaM6K0foflfK6g1uV5r7jPUuwpuKteF6oyPdbKRt9Hy_Y-EzQds6Ko2afsF2nhItBLEYKUYR71IxmpZFsR2_obS06WpRNsHE1Wg92uFcdd_-kdiWjUbO_pFoqEoSO9JCJZ6sSN9RuT7laYhAqfXEn_G1x7G7uEC2oHVh9Tra7ah8bb_kd1MeXHsXitlEDFaHfDlvLcrLcNwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=HFTDTMCb9J4-OuBBSRCwCJkwDXnX6mt5OCnk4zkTgXa37WyXZw3Pyej3QsT7bw9XGmOgl9Crn5-y7WKQ_u9X67mOBXiP4FF4EOrJnE1mLwLVUHu6LiPG_WLvZFhpGlMZTRN6aTaCWAIaM6K0foflfK6g1uV5r7jPUuwpuKteF6oyPdbKRt9Hy_Y-EzQds6Ko2afsF2nhItBLEYKUYR71IxmpZFsR2_obS06WpRNsHE1Wg92uFcdd_-kdiWjUbO_pFoqEoSO9JCJZ6sSN9RuT7laYhAqfXEn_G1x7G7uEC2oHVh9Tra7ah8bb_kd1MeXHsXitlEDFaHfDlvLcrLcNwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GQrQe2gmJyokJ6sEBehdZ8eH3cxLXe_WzplIup_SOb_40-PovSGymMlt21eWQLPODThpgr_LGkduJmsaw03qeJ6Y1-vzyF6Lv022ZcDAw6Iyl-gjPQq1B3agyaOYj4I4a9iu_46GMaHb7mmuDBj-tLKus_iHD8N9XbtQyOdDKQiMzx566XtFYQbPXFaPT27IIDDRi6sAxbCRiRn4LXgq5KJLp2IE5q8d2G6kN0EFgs0Uo-ta6OGUBk1bySGWUwf9fp0P0rwowZaCSyyIB4uihD-7X8S9yEMcNEokRJuuZKqw0cV2jX3o3PjTFg-DQc3tpfIVX-MBHJHQc7DlKWnN20_G9cY6RCnokx6US8a2m7qjSnNVgDxTKz-J_b-GwnIbKliGjZ5_6aycFyDtipGmQNfpya4uDJ64I3PyONjK4-V3SCFqMZOaCZ3XtnCXz10RXuBU9BxIfgWZkaF7smHob8-AtPL4cgjxOSlJCp2qbd1gAlApCXDUkWgm-ZRLhp2GxVZ1WhsmlMTizULx87P2mMsd9-8FkgJCW_gVf3kMbOjJt7cKK2UoGUhEru-xl4mfwjmnE-1IkqNPtfT1BOeSMkDEW7MICIQg9JzK1O7k1rs7dcaJJYhIqOA1iPWIjnWwPy0k4toDbhLZWA8AhhRhQJDQd7bqXjbLtCMEZcJnC0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GQrQe2gmJyokJ6sEBehdZ8eH3cxLXe_WzplIup_SOb_40-PovSGymMlt21eWQLPODThpgr_LGkduJmsaw03qeJ6Y1-vzyF6Lv022ZcDAw6Iyl-gjPQq1B3agyaOYj4I4a9iu_46GMaHb7mmuDBj-tLKus_iHD8N9XbtQyOdDKQiMzx566XtFYQbPXFaPT27IIDDRi6sAxbCRiRn4LXgq5KJLp2IE5q8d2G6kN0EFgs0Uo-ta6OGUBk1bySGWUwf9fp0P0rwowZaCSyyIB4uihD-7X8S9yEMcNEokRJuuZKqw0cV2jX3o3PjTFg-DQc3tpfIVX-MBHJHQc7DlKWnN20_G9cY6RCnokx6US8a2m7qjSnNVgDxTKz-J_b-GwnIbKliGjZ5_6aycFyDtipGmQNfpya4uDJ64I3PyONjK4-V3SCFqMZOaCZ3XtnCXz10RXuBU9BxIfgWZkaF7smHob8-AtPL4cgjxOSlJCp2qbd1gAlApCXDUkWgm-ZRLhp2GxVZ1WhsmlMTizULx87P2mMsd9-8FkgJCW_gVf3kMbOjJt7cKK2UoGUhEru-xl4mfwjmnE-1IkqNPtfT1BOeSMkDEW7MICIQg9JzK1O7k1rs7dcaJJYhIqOA1iPWIjnWwPy0k4toDbhLZWA8AhhRhQJDQd7bqXjbLtCMEZcJnC0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nm-YFYIJDlxov0WaSfLlKHdrl0D4iEigesSr1QjxxgUy2Up6mPw6iA51S0hFBrN3B2_oIyqQ8Rc-ExWrdIAXqF4WmrT19036a3AY1dy8L2AszzORyXfMZeaHHVlxT2OA6urD1KgavDCy9vvOLM8VswVulpas8qDrU7CrTcykQSQqLYvInYBv338XgniRx6bbUtpW-vbKezaHMGClMnTdnEI1i5kwxsXuisiq_25MECzojQVGrpi8rOZejDAmb81d4FwS8ngQej0E_y7ZJ2-f5bRliVOnm3NbMVCRvY6g97mJHB0Fp_XzILZSapPyguB8TRRk9Omr9TVbJ_pQT1gZKiTgLhPLoFcwXeVzH5Wwdlq3RjvSKQfqwIPJAzSayynBgiOfBr4bdDs9qV4qMU5KeeWC9L1c8N9qbFtdPuRE2K8tGfi7WusVnm1Nwbe_efwK5jfK5WVAGKVDc-vMVMbEYueiSsGQJE-tBY0ZTtoeH9ekQKq2uqs0pALPEjCSi9rhmf5yveXK1GWqkaBJv_rDwke7IpfQJXNl95Vi-WlAxxukmrlvM4L4ijvBM7-cLoY4G3OqnvQU2n0DrCp5foN3nDI0482tfiLvCteWRfjJ-QaWuzrk3RuB5jTf7KnfD7POGMClwnPaWaLaXuVH4UysyxyJ4EWxXKPUNRLx3DVwZpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nm-YFYIJDlxov0WaSfLlKHdrl0D4iEigesSr1QjxxgUy2Up6mPw6iA51S0hFBrN3B2_oIyqQ8Rc-ExWrdIAXqF4WmrT19036a3AY1dy8L2AszzORyXfMZeaHHVlxT2OA6urD1KgavDCy9vvOLM8VswVulpas8qDrU7CrTcykQSQqLYvInYBv338XgniRx6bbUtpW-vbKezaHMGClMnTdnEI1i5kwxsXuisiq_25MECzojQVGrpi8rOZejDAmb81d4FwS8ngQej0E_y7ZJ2-f5bRliVOnm3NbMVCRvY6g97mJHB0Fp_XzILZSapPyguB8TRRk9Omr9TVbJ_pQT1gZKiTgLhPLoFcwXeVzH5Wwdlq3RjvSKQfqwIPJAzSayynBgiOfBr4bdDs9qV4qMU5KeeWC9L1c8N9qbFtdPuRE2K8tGfi7WusVnm1Nwbe_efwK5jfK5WVAGKVDc-vMVMbEYueiSsGQJE-tBY0ZTtoeH9ekQKq2uqs0pALPEjCSi9rhmf5yveXK1GWqkaBJv_rDwke7IpfQJXNl95Vi-WlAxxukmrlvM4L4ijvBM7-cLoY4G3OqnvQU2n0DrCp5foN3nDI0482tfiLvCteWRfjJ-QaWuzrk3RuB5jTf7KnfD7POGMClwnPaWaLaXuVH4UysyxyJ4EWxXKPUNRLx3DVwZpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=G7jefkq0USNIuR4NWdBzetezrfaMqoUBpEtdHIWQSHntkNqsh6vT-kxd13vj0WJ7Lw_RAjv93USHfJ5jcj8d0gjPqbPq3R2Jh310GZ3govamr-a6ovJsVyuW7XluV3JrPtX_wFDkANrxZ-q1VxoOlYhTjf8YqMdmVde9ET9axp29FxIKSUNALAZ_wyjBEB9W9-TmX_FrJNi9_858bWquhtOsYmGeNZvCNuz9ReCfEMsGLaSKiZxBr8NHALGTe011tCtbgmQZ35IfjwzeBFGOESz89BM7spNsqpCH12sLT-SQuVOUzMkPxlyDlJjY0ePP8gQkIy3MLYmgHsxGLDDr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=G7jefkq0USNIuR4NWdBzetezrfaMqoUBpEtdHIWQSHntkNqsh6vT-kxd13vj0WJ7Lw_RAjv93USHfJ5jcj8d0gjPqbPq3R2Jh310GZ3govamr-a6ovJsVyuW7XluV3JrPtX_wFDkANrxZ-q1VxoOlYhTjf8YqMdmVde9ET9axp29FxIKSUNALAZ_wyjBEB9W9-TmX_FrJNi9_858bWquhtOsYmGeNZvCNuz9ReCfEMsGLaSKiZxBr8NHALGTe011tCtbgmQZ35IfjwzeBFGOESz89BM7spNsqpCH12sLT-SQuVOUzMkPxlyDlJjY0ePP8gQkIy3MLYmgHsxGLDDr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdrONJAVljT5uAis5RfjvQpDlUvruuMVdmNLzx4kaU2n3PJuA9gQQ-GlnO4NYcoV5rn_C3pOe3c6IRhrH6Obnv4Im1NsRzV_VKVDi61rvyO-T5KkaemJODR9GmD-PIdb8dwiE6KaUUCREbwf4cCF78kXd97tQ44N4kS8MU-2_FH7vllNkWz9VMcEHxyTMt1otpgC1UievVaCAiHlsrBo8ejsaBI4MzkTSQcTLxIWL0A4-q4TJxt5dPGjxCDuBG-pE45jCr9qrbq2zS3lTnfupknS7nlaLEONROEukSBNjl6kPUpOtQxQGslzBd1FJPcXRPiF1soVMbDDoyZa4FrQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=XJ93wMOlsO76eW_ZanMAH5_LTGnZMDx00qN08za4G2PQBOQF-Szd3Tb9yoaMrHkBNjbX8UXz4ez7g171LJAvX7m64Li8MJ-w4ZUg5mvfHdwFJxA7Pyz0aeuTCXl7jWljN9lxiMIIuXhi_5P5qoVz1KSACub_ZsaMlGIWsmRLIhCfxHokjQMLhQQZCIB2a4DTFysNrl_xJuOtrZs4htc3xP7xw0CUFeWe7wFqryXfyE0sU2P3hYblC3C0uqR-U6PZAMLhDV1IDyEtB-ybx2jh1DrWzg4bEoYryzajlXK5ZhMGdfj5Pg22IubFdz0uHOmCZ71h0DkqpGQ4v0aP9zbDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=XJ93wMOlsO76eW_ZanMAH5_LTGnZMDx00qN08za4G2PQBOQF-Szd3Tb9yoaMrHkBNjbX8UXz4ez7g171LJAvX7m64Li8MJ-w4ZUg5mvfHdwFJxA7Pyz0aeuTCXl7jWljN9lxiMIIuXhi_5P5qoVz1KSACub_ZsaMlGIWsmRLIhCfxHokjQMLhQQZCIB2a4DTFysNrl_xJuOtrZs4htc3xP7xw0CUFeWe7wFqryXfyE0sU2P3hYblC3C0uqR-U6PZAMLhDV1IDyEtB-ybx2jh1DrWzg4bEoYryzajlXK5ZhMGdfj5Pg22IubFdz0uHOmCZ71h0DkqpGQ4v0aP9zbDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ICKALY2b8vUmrsOn7UzTm292_1GV_kn4F88TnW4hGT4DqP5Hu7HKRoAzodqTa8NbXzWc9uLW15wT-fK9LSXpLWRO7dXhCsmNyXF3owfvXV1J_fwiYhHmlWIv-p3LR0bO-WQdSGysymJ9-k6F3oiJtQJDEtclo2zUm8ENeT8IL5-BnhvOeqZUdJvWTl4nXDCqdPeLkzvtHQ70XuyZXtcWuB6aJ158zIbNan6MCSvskaYkwsPGb9qvF-eAZB-LgkA_sLFcPG0kAGZtaj7xu7H9G9e_H9pInY4YMFcKc533z2dBm-yY4N0GqVf9VEk3hfdA_d3ro0Q6PogBI0cj64PMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ICKALY2b8vUmrsOn7UzTm292_1GV_kn4F88TnW4hGT4DqP5Hu7HKRoAzodqTa8NbXzWc9uLW15wT-fK9LSXpLWRO7dXhCsmNyXF3owfvXV1J_fwiYhHmlWIv-p3LR0bO-WQdSGysymJ9-k6F3oiJtQJDEtclo2zUm8ENeT8IL5-BnhvOeqZUdJvWTl4nXDCqdPeLkzvtHQ70XuyZXtcWuB6aJ158zIbNan6MCSvskaYkwsPGb9qvF-eAZB-LgkA_sLFcPG0kAGZtaj7xu7H9G9e_H9pInY4YMFcKc533z2dBm-yY4N0GqVf9VEk3hfdA_d3ro0Q6PogBI0cj64PMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJpS-evNtjcq8c_RMMDvX5ya3RxSqUSveeBWf2kXEvjYQf0W55DmggN_vaxKhNnQiyTAYy3E8fkY1gQ62K3GWiCL6BBdHTARYsXm4QHpbkgZgv0qMNUho1KozqAxXBtAkvdzAQTftR05isZmwfBpSAHjI6eu5igK7dG1HFZHFLEXIXKmVvxx1nyzPvdqhF7t8A5h80epXJJKD6uKkhYezKTZkm8cdUftI0371HFAzXQgAFKRGgwVSJyWGoqNgF-CBxEkCKL7uivsMrXi8xrUkEL4Q99GQpq66rJu9uVbt-KGY6ROcB9aCfoRjbKEwP1suTiLOzpQhHomwBlyi3u1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGs-RP5T54Q6YdhfDQe_yP59tPYlfTpP7bPQE2uwvtGuqjkstGDAuAES6gyY4oC_LuzjzfH7IJuguI5_ghf748ywtRghsAgwluai6fBYIlwUu1a6-MZRxmlZggsL4E4-ub1QI679O8fIwItO3QQMnwU_yzRYEB1a0FJcKzjG1K5Cn-OFP8sMdPO-WffjiRYcqVXJ7GhbDVp8DM2aYPpGBo827pJCUVH8DpYunfdjzpCxM0r6KJpOyrPWXrD8E34a2ppNKk6CHergr4cLY_Dqgp9JGira1rN8S8bAfKCQ8d1PvbTf5eySnM2_-4yBpnHHQxQs7q7vdWMVIk6m5gsqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy1fvKzvekK5DgrDTn2JcwfhpHRd5dTnEjClmPC1Tcgrjsog3OOPkDoPCJGjnqZ2BbNjj4kU9RKyrC4LsfjtZogPMwBU4t7eAQSTDno7kJiIF0m4RFxUhUxBsMNI0cwoA15PK0z00DhEkpuEmJS8mkJnSlWFruDW_5mrQOy_zsUgm71oeoKQC6qMbPgkWDqFBsLfvWd5xsw3bMiIXGS0HfJMoSj7uEYF18ustbpnVKc2AyjydFxEamZKy6rnQDtbFs7PWfhDt9BPbMKdx6qQECc8IvzxarJ8zVaRCNsZRzONpTWbvWBuYffNRtk0DdG32aQ4lTi39DM0i9QowwMKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUgMGPtB06HgCYDcLJEpuZkq0zWD_-QUqDKXQ-iF96fdElXFZ5bEKbV59NAfi0W-AhxqRJXDSd5EfUZgh1VuykYDzrYaNZKyA2D_ciXc3Qe7B5gr8CMVHfhcNeWd5CASuzmhYBZpPgPDOfpNlppqDIvjAXJNIt_jivGz5sG8wthaxxyj-mFXFbwPEWcScefaZ8auG0Y0I0oEGRGf51XbuIJWq3jOwLjKSjynRNZE5-MObWh93qJpyKRFdaFLOuF4fcb2Lb0ZnYn45nv5QTlJCxLcTgIMHDCe_wABPyNtv7rxIuEsrCvuvIrdaQYXAkDpXd1SUBDqVUROEygrs2QltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVwN0XqRbF2qgJXK1hooy1t9OFcSVWfeNG8cR5YDthQboAGfXZVhYoltn3RLm_fZsLlngqO9R3G9UU1NwhDLxL2R-FteMbjCRONJ_Ew5juVPgJhWbbdtL-RI8moS-B6b5b3HtYuHgZjd0yNyX2dLuMD4_TQU43FjPVzs37Wdx0hynyBqjJ4pTuOmDCnv12sWzK_u5kyLhCvgn4jwft_Kyd72AxUWNSqsPRlEt3RvevgsfwF8t16HJRqQeIvOs8XxT2gxP-DnWTscGSwxGX351dCgKVuXfb904kKXPHREnjn8r0oQAMUA7JH2b1fgEQm9F9X4lWP6WNnwrw8UPe3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab-Squ6nEo8lnPuAt9erXsnfKnh0U1dw0Vm4KUYsO_Yimjf8qCh1fQa4Emm_x2EnEbFaSX1ydj7bl1kYIuxiKA6r3BFD1AGc0yEHZIzMkqXnM3ark84j4Ilrs5zwGy8p77XSks8eCkunIbx2DzJx7m4uSFhgviNkOSXbm5CQwPcjAuUq4CxSzMfAk6ENg6le0Qp1k5dpX1kLuTSqFc1wzcCIKhwo3KRiWQyv29WOJ6wi2DM9PDMAFp5BfIEJUkQXZ-wCMqkbzyPusbtb0GaXrGCfcuEkSvsaPpgfeg7IB62hkTWcKH0yiEO0xFVk5RWoQOY4qPLTKAbC2XGc8BhPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buSXcA1fOzNBOS0RBzg4oId9M2xos6aWMQNP8aRwyHgVOhJCq0Q-42ywS6kPgEFTUNuyxcQkFa07630YzYNVbgiQ_eDIP2ebWU5vZUOyrn97UCjvTD1CSn9RSD5CCcJwDtWAx-AaTPD9foNrsBkthttLLn_sLT7JIndmJqxcVlBuUw-RK_Xv36JzSI28-E-yvi3gUSAn9kay3NsDjHpm_8kvh8ECSJhgatduOCIyakoIr3FVv2Pbm7KlXR4mQM2NBH8thrSwNXjhOxdVkRx4llC-bQ-7SmFtVtLsJ8mu9f_DFlJ3zErMAsqeCc1RVI4EHL4Ubc8ezlR1x0lKrIALjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
