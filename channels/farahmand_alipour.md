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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDkJ5C5C5ybZ0LxvQH15TP0XsJ7PlFO68O2dXvi-b7TAN2aRPI0PUrPQ60bALacq5Kea5LMA4-EzpiGdLT8pJZavGOoasd4GUuSoWmsS48Y2L1SfAxm8r2u37SQg6VRFcReivbPZJIxqvLx7Rr53BFsbhRWKf9L27XjSKozZkfjowmAf0irwYIPd8_kJFJTnw0JM-BPFSFVqSkkn3fFGAj-_dzfoj8ijH_JFnMhvYVq2LB0Y23KkeYE_cjgfra7zKfIVfHbgsOmiV4AY-qTWFaX2QFNd0UqzOkT83Mf7y5fF-wwPGqHv8-GdUqyOPbioJhYXU5xu928RAz7BiEiO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcu8bFEAr5fJqC1-vXwVdBotP9ZK6_01Aw61sODGzzCEwyNeQwjRcwFCw6OMcMI4tpmVQsml-ui3XCm38X_KgyW7AKp73Lg-dik25Miqh6TSycO02jkjGbRLDsiNxHgWslvF78WQIBRHDDqddBPEoKxrk5zWQufTOIgB9bInj9BsdNaZyM8O3dBI-fCYo2gqUD-jRhWo0fSayMv146X6A7frgZ_oSZGeC_Kwr0Erj6vje7oz5TBb-WgRRl-PNfaFEjAg7QqVZAhSkwUs2DHu5sjpg1fREI-VWxTxx8VkAYokS_QTuoyzWrf_mHFml5IFiIrlqdaHX8bRVq4TuLRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP86bIVtPi9mAqOG0Xt1I131-Jv5xxUB3v3L1UZKSs7v-Q7q-o3rNe0DqxS-5h3Kn4T6M1H44wjXGh5BJdgUUzVe6c18GXm3_l1AQN4z9AVgH0iM0oR0QyMSHBP6-Cbu-663k7JhSy10CfyHh6rW4WxBLxK5EDW4tbkJpprVLuoVTz_dIcfMDcEB2dzBRewJ1lF5AnITdi_uQ49vjaMJiWWHefbCagbWxbX89P1wNaudNzfpVI2DELn54iC7GZtc6weIK0d3t9DYiKk3RIvVDrskjOUdtL6ZoFYXAJW32VACP0YRqk5r97NYnJK2DYH2o5KdtbWlWeYDiFUPNoWuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO3-dvaN-lix2hN-LK0anig0k7MXhFylvwL5RFfH9yYbSY7kV_rXaZLzkdnUo4MoovMB3A2RtSccpMjxFoqgZTHLlkTm-_1jSFSLgN1jSE-5tMr0s-0YcvTlDq99lmxosS-4F3fECwxVPMr4U7MfpQgF-Y7gkhN76Dh3ZWyUJs5tKdkyuXZ0tiNbNgdk-McFlFGbZHdyFceNfbOJdyKva3iXIBZ_EelbFr36UYTeQV-JjdWKFViowa5J5nSn6P-4B-i6p65chMg40szpA_3BUbG6BSOiQT20K0UMx-LmA2weXI6O94l6NZhvuuad38AF3rsG1QIxLoy-kF2GzgCsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r84fnfGD3w7SypFeQRutIuRQETNMjatl43OKsKUsla9jXZXLPNJpznxv1KQr8pnLn6zPQGKyJ2TP2hf0HbsWkJiIMJIC0H7RfOo-xTBpmTFhPbiEEx0oxSP-DijgUcZ0kppL1ByOOJ-GVUet5KELHQhMvBrR_aMGxPKU0y6tICy8OtnSoiI3K3L_AX2IfyAYHHJPMA2ipC0SuK2IrP4ccuS7lQxHfcIpYEYZRLFCFylrEasTwloq-MthqkG0cVXoE4wbwRhJeAe3fDcnICJpzIqrTrPJIHXanz83djYoQGWCDBdEvunEFY6Nefp4-KD2bqNP9Lz3i31W7Sm6PqyFjQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PM9ULs2Cf5N72SDROLkN5izutd7DcOa0ii299UTTRsxUNI6qScntk55xgmvYNzRUxQIyMmGPwavwR2GE4uHakYMv8y2yKvIhxkCgeLHm27cYQ0EABGGHWBEDB3NDGZlqN6I99Cc3nzxbekJhm9fIWc9ezp2Kfhaa3YnzpK6zNpkJwzfHGEDEvZRdVfOrojN9_aBpUqGpo2uzDj3HiTxdsuxjoTtPyLbsaUErqq5VwIXhzALurdicTSUYWubaI84EEvyIt4atjbmL6dHE_nkiirJUpTFhrDFDN6kd8H3KUmdP9IntP0dLpR0o94tEz61XxWDA-XQGpa7TE3Nmls-FCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PM9ULs2Cf5N72SDROLkN5izutd7DcOa0ii299UTTRsxUNI6qScntk55xgmvYNzRUxQIyMmGPwavwR2GE4uHakYMv8y2yKvIhxkCgeLHm27cYQ0EABGGHWBEDB3NDGZlqN6I99Cc3nzxbekJhm9fIWc9ezp2Kfhaa3YnzpK6zNpkJwzfHGEDEvZRdVfOrojN9_aBpUqGpo2uzDj3HiTxdsuxjoTtPyLbsaUErqq5VwIXhzALurdicTSUYWubaI84EEvyIt4atjbmL6dHE_nkiirJUpTFhrDFDN6kd8H3KUmdP9IntP0dLpR0o94tEz61XxWDA-XQGpa7TE3Nmls-FCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UGuNby0bxBfKYzHNxEIpDfUznX_ObLr5qnpDMVwVgySOD1SbYYuOWl--ihOZkJHgKGyrGS7bgZeYcFqCVm_FBjcPROCOD3BpGeDWa9Kh_yy2SufSizWR2Wdw4O8AMSd6HKQM9LEsvS-gg-WZxUxcRGqQxKkDsDLInA7DSzQte9bW7XCYGk48vreTNCT3DrP5abhpYR_Q13eKVfcNAiqh1uRsKWi7JUlLdV3r5jwO_6buffwPEqJazGpf8beJn7ffFPEejD5bomVYm8oMy5S4BnSAkpFc7CnETwT1-cP9wbf_BH75rwoCgheMuONsqpc-fdhT8pS-6zCuP1wbN_N4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UGuNby0bxBfKYzHNxEIpDfUznX_ObLr5qnpDMVwVgySOD1SbYYuOWl--ihOZkJHgKGyrGS7bgZeYcFqCVm_FBjcPROCOD3BpGeDWa9Kh_yy2SufSizWR2Wdw4O8AMSd6HKQM9LEsvS-gg-WZxUxcRGqQxKkDsDLInA7DSzQte9bW7XCYGk48vreTNCT3DrP5abhpYR_Q13eKVfcNAiqh1uRsKWi7JUlLdV3r5jwO_6buffwPEqJazGpf8beJn7ffFPEejD5bomVYm8oMy5S4BnSAkpFc7CnETwT1-cP9wbf_BH75rwoCgheMuONsqpc-fdhT8pS-6zCuP1wbN_N4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=V1MEwAdV0K6ivleSE7wrymzP9F8JSh-yOtDrlxLrqp3MQ_CNIAUM3Ro06bS0zj8q1JSZqdmJ6x_MAMDhoD3XTcwK-DEC8YvLcmW7uZJ6XTGtPGftwhSbtpR_BW9seI1X4hIi3CCgiY7A6jBM7GlzFc7NDYhWLcHLioKLBZTRWYUWKuXalZwIV5fGx9wPkQSrKoy_0MCQFWrn1gLG12349Y_KP7qGjrvvd0rQIa2SeiduAvGoiyhsxrpjVX3P1fVk7ntFC6rWrvUV2l6I24bBfu1JrcZf-o4mKqLbEy9Odx3uWfjw8dR1C6zCrhb6Bi57R1ob0K7hqTNG3KhGn6Baqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=V1MEwAdV0K6ivleSE7wrymzP9F8JSh-yOtDrlxLrqp3MQ_CNIAUM3Ro06bS0zj8q1JSZqdmJ6x_MAMDhoD3XTcwK-DEC8YvLcmW7uZJ6XTGtPGftwhSbtpR_BW9seI1X4hIi3CCgiY7A6jBM7GlzFc7NDYhWLcHLioKLBZTRWYUWKuXalZwIV5fGx9wPkQSrKoy_0MCQFWrn1gLG12349Y_KP7qGjrvvd0rQIa2SeiduAvGoiyhsxrpjVX3P1fVk7ntFC6rWrvUV2l6I24bBfu1JrcZf-o4mKqLbEy9Odx3uWfjw8dR1C6zCrhb6Bi57R1ob0K7hqTNG3KhGn6Baqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAQtO9md2N8J3QGoKKhh38qpx2C8EZ_jMfTvi1MeZ3NQxE1Y0ARey_fc_M231E6r1BoxrGqEro8hLknptwpI3-G9w7O56viOb9CvpFA8B0VW_afYSpKsvtprGAgKW36505nbeaKFuwKVMxNrF6E6Dtv4MosmNbBP_2MNX4AFkMkrTH9ZoOwxhlsS_v48BjTmyfFOrYh9Y56DieYvozxhpWQDQ_GZkOdrsNlZ6nG7Awy4b_-fcgYfk5hSBnrblHM4_3u7xUHSxAJ2yK-r8eB-T2vuo2A6re3mrRk22GQtI2YNzcRGG8ISQr1cOZfpfltnLS9l8g9NT74__zuoCCIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Btr6D57yNqrGOjy06bLa0WUcrCbOqD7Zd-ViO8vlHwjRHED3_HRS_Qoi-eHGZ0rnad105DgWLAGw2JH7OJj-WmOkSE4gTbAcaZ9f2_ta2lSCRYU_uCjHnZxITgSQbpgz3nhQSCSUKkwuNkQ1CpynHXpn3rsKoA53dSkej0VKbATs3ZXcmr070i4313_r3BL9NVmiRq1n7pX8gJrgft7qpM5QslSOzoYiChWZzYNC_pnanFWMPd_c1AlPnCtgyCpiUEDBmWn9t9gf7IFxpBZwqzwjERGKf2D7Zpd5aUSSaEGEWXWN27yhJvut9K6OqvwBeVrqj9WkoPUHo9eROwWjGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Btr6D57yNqrGOjy06bLa0WUcrCbOqD7Zd-ViO8vlHwjRHED3_HRS_Qoi-eHGZ0rnad105DgWLAGw2JH7OJj-WmOkSE4gTbAcaZ9f2_ta2lSCRYU_uCjHnZxITgSQbpgz3nhQSCSUKkwuNkQ1CpynHXpn3rsKoA53dSkej0VKbATs3ZXcmr070i4313_r3BL9NVmiRq1n7pX8gJrgft7qpM5QslSOzoYiChWZzYNC_pnanFWMPd_c1AlPnCtgyCpiUEDBmWn9t9gf7IFxpBZwqzwjERGKf2D7Zpd5aUSSaEGEWXWN27yhJvut9K6OqvwBeVrqj9WkoPUHo9eROwWjGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=XpeV2b1RIG-v5X2_YEl-udwBj-hSNKssQ08-WaEbUs7WrJQyOmWP7fM_9Pqj9i5XVw2Exh2EBbl8c8_izE1UDqyoqkB7NpolW4LEcGHNJngcC8kGQ-D5vdnF6nV8as_urvCfhJr1Vu5Ww7PB0_EHgSwJzSVa-S8O9aIzu55nczOOSzCDsLx-DMbvXAwShIUtMOQYavUNKynREC9BwHtnj9s86uon_3E-Icm_lHgIyx1fVp2xKHBK8o35jpIiL0yJ_GrSNYakK9u6PPhc8UxcTbaW_X-ynrEL9xXmr98RWN9LIE8cs8hnolfCUmEuSUBjBBO28srPqZ22A_S_dZ_aUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=XpeV2b1RIG-v5X2_YEl-udwBj-hSNKssQ08-WaEbUs7WrJQyOmWP7fM_9Pqj9i5XVw2Exh2EBbl8c8_izE1UDqyoqkB7NpolW4LEcGHNJngcC8kGQ-D5vdnF6nV8as_urvCfhJr1Vu5Ww7PB0_EHgSwJzSVa-S8O9aIzu55nczOOSzCDsLx-DMbvXAwShIUtMOQYavUNKynREC9BwHtnj9s86uon_3E-Icm_lHgIyx1fVp2xKHBK8o35jpIiL0yJ_GrSNYakK9u6PPhc8UxcTbaW_X-ynrEL9xXmr98RWN9LIE8cs8hnolfCUmEuSUBjBBO28srPqZ22A_S_dZ_aUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpdJHotYqgZu6wfcJUVbdzScNcmCVvUowe5-_FuPbJ3PMakjKWazeUNRBdvSXaj7VdbGR4kBlmnz7Ki5G-t5zWAi8VxRIHOVrnpHKsJ6CAViDd1BCso4DhBSifJGHqdltjyVt9nBAn4FjxuKVdKQGkxZDh2Pns9OCqY9zjiloNE9wiIU18Sdoy_wduNKOxxeyE8skp7hb7NCNev5ae_T3a3zeH67b9KeeNLGLikujPtUfsHN2l0EubzqxPJmuQLxmwjaD_gbyEHx4m_1sq5gtfDSLYyizl0ibqHPQd5Keo2V64_AwstOHf13wPVhIOb239BU3N1XKhsaqmIgfKhx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=T_NN71KtVd084tMoy3sz3I1R2lVUkF1ISaZUonCo-rOXhbRlPozSlBTR1AyLFH7V997kRZrmPqDPu_5UJQNo-Qa9IcDKs9gqwMwMK_Xu-kdgH-cNQEehmt9nt-oFo_8rS4z1PfTc0j7cX3742WUr70ZO9FMKvZ1w1SVN7ryRlXaQpH1DldDsSzRb5huV2NgVP53nJtMFcqZU7Utfc4nahB1ce_XhACKp54fIgf3USPUMvUi6K-6d19lM-i_DzVv5jDCszoq4yQwBV1HM0T0lemtkRBTknyfttN1wMaxBkIoCseejluCu-a9IV72SjE9xzoHjyAl4NDVXFBAV2VigDlpzWK7uCh_txA46qcr6m1deNqUiq9TIhDjw6BDkbTr84D4BYYnrvcpi09ke7AEZMw05Q36JK_9DvS19H8wbCn6lHdz7Udja6KN_70G83yYw61dv285nWoG6MUWZmtoaoaaOU_4GgD2ofSIBJFBGZ9HLq_EWTndpilBzfP9_OfbjRTbEUbrL0m65-fIJ01VCbu72Z64X6kEp9nWsO6rjDSMxXLLGlah9f9rYn0dd00n47hK2zZdidk0EQvExed9rhP-CK5dxTEpef41Q42pOShmTfQUp1fOJgxwWeEJtiGtfLUTZS9X92JDVMvRV0MpAJLuJP-JG_Z62eXUp2NakqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=T_NN71KtVd084tMoy3sz3I1R2lVUkF1ISaZUonCo-rOXhbRlPozSlBTR1AyLFH7V997kRZrmPqDPu_5UJQNo-Qa9IcDKs9gqwMwMK_Xu-kdgH-cNQEehmt9nt-oFo_8rS4z1PfTc0j7cX3742WUr70ZO9FMKvZ1w1SVN7ryRlXaQpH1DldDsSzRb5huV2NgVP53nJtMFcqZU7Utfc4nahB1ce_XhACKp54fIgf3USPUMvUi6K-6d19lM-i_DzVv5jDCszoq4yQwBV1HM0T0lemtkRBTknyfttN1wMaxBkIoCseejluCu-a9IV72SjE9xzoHjyAl4NDVXFBAV2VigDlpzWK7uCh_txA46qcr6m1deNqUiq9TIhDjw6BDkbTr84D4BYYnrvcpi09ke7AEZMw05Q36JK_9DvS19H8wbCn6lHdz7Udja6KN_70G83yYw61dv285nWoG6MUWZmtoaoaaOU_4GgD2ofSIBJFBGZ9HLq_EWTndpilBzfP9_OfbjRTbEUbrL0m65-fIJ01VCbu72Z64X6kEp9nWsO6rjDSMxXLLGlah9f9rYn0dd00n47hK2zZdidk0EQvExed9rhP-CK5dxTEpef41Q42pOShmTfQUp1fOJgxwWeEJtiGtfLUTZS9X92JDVMvRV0MpAJLuJP-JG_Z62eXUp2NakqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mocy0e2Y1XDptOfsvgbOb15qnEs-D5ucMQywa-p1SkarLodUFtGXdCYSkwL7rGMIjULsuuCA3IhrsiJVmjL8N5ggXlceGIa4ySK3OaDlb7xqWXgwctn8_iBxxYjzJ1OwTUTRhHJGI6a3aVO7RId4cvgyaww1FwI6iiFMJokijIp2VRByMOf3_5-wJmFN5eBm9u5Id4AelZI5UF3cP5w2VT9yubB8xiZFtmTPqKKbi9vsiBi_RZg_Z5KwISG5u-3njOrISxFWms2pWy9FATjnYnjSN1ZLzEQT_6ATRszE9GzzQ_5aTj0-Eh374pfOhRzyAOj3P2NpiytHBll9YvUMxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JhFmXy9OkD8ullDP-vA_YBnzZ_KQk9PuXByurpzznzgxFfemg66elQGTxLqyXDqV2bMvvnTSLiJ_0BRcrooAASaQp231LH30Zbw7E-g5ScvVfP9sxewVouytVkY0uaTE2Wd4BdUYI00PPyuvNdAihg-uG4RMCZh8fb379tKKbGoa8PWQRPpM0uWzBSUvuvTCFKb71yC698_1tN4ZUzvCt6Z5xrtTJrdnMhJOLmoj58_F0PVni-p7uLvNjYZ6j48r0E_bVn71smLmyZjEJvpf_GMBcgV4w3A5Njy2zM3I-n4s82KTPnZSqhU0V2lJE9J7wxAMzXc6idOyPQQJm9HtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JhFmXy9OkD8ullDP-vA_YBnzZ_KQk9PuXByurpzznzgxFfemg66elQGTxLqyXDqV2bMvvnTSLiJ_0BRcrooAASaQp231LH30Zbw7E-g5ScvVfP9sxewVouytVkY0uaTE2Wd4BdUYI00PPyuvNdAihg-uG4RMCZh8fb379tKKbGoa8PWQRPpM0uWzBSUvuvTCFKb71yC698_1tN4ZUzvCt6Z5xrtTJrdnMhJOLmoj58_F0PVni-p7uLvNjYZ6j48r0E_bVn71smLmyZjEJvpf_GMBcgV4w3A5Njy2zM3I-n4s82KTPnZSqhU0V2lJE9J7wxAMzXc6idOyPQQJm9HtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwEkb65r3szB4Lokkta_KQb7vQzt3iOo34289oPvFoZfbs2oXE3Q1WwoovloRjrm1AQ2FMjSWOsZVYj9_LvWcEw9NS-EJpDZl6zEK1wFnDQYDBTVIbDrNL9KMbYzhJdBfQ_4mBgnWca7ZBn7vyWP0d8zO6YGQYrcHBOyRU0LjNl8ri60WgpcB11x2N73x4YTBEw9LNzK71wkbeSMemSB2Zn3sFWjTxv3wgV4u-Jd4TgyMO-gntjAw9TMlw7TOm3iM-IvhNCxQi1xTwBUMvrGCsaLxGSUl-lz4yEp5-zX_3gC9rCNazOlNsz3mwE9OzTdunk_vHpU9R7YzUhbc5QzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKYK-Kdru2lEP9UsMvfcjW160XCQUBVDcjrtah0pTbB9wm4obhq2OA2DytSMlTq9whNNVQGzP1XcXQvH3l-I8sZrB8ghk5WtD_N0orIGf2HzhhBlrgBfghg5rh6KIc9IMo4TQzgI6b_To3FTFHWgnmNOu9x0wB3uaTzvOBuT8Bt9rjr_kruHvNpxM1PPj_2hsSibB7PyILTWgaJGaEoDpF1lslplMbUb09GpleOkdIaU_qWT5AUqRnuG1UAzlgy7ral_rxSY1pjaxIaOaTrW1Xyal935eSBDD2w4-AwCkQwy1Pq3M8ipwQ3dF094wGXN0F_-2ec53_q9uto_IEy8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGASEVVPZDHfUAgZ8g6VZ_5nmfWhkeyJ6n8OMmu9Tctu8bonfe_tQBEgvJ_jt52LpAtXS0ShcgOkN2GB0uvQGfGw-0353fAPxUrmHgffP2iFGdCXcALvEAh1P4NejmQPp5QR2276tTSr4n1rUD0jAeVSX3VCu8dKQSvOtIxHSdbjPWc8ddjeiqYs6VqMTfVlWFiC6q0_fvICsWF5k0U86ULQLtJLqxuGXl2o-SOIwHcMtTtpNnmRrTojbxDkV6ALRqwSc9m4ZKb1QmEzIUx9TOxgLd_u4wwmQyKOKkCeCtxQX7s-qFsLV8KhGU7l3hSJ2PEtR7mU_IMPm1TEWpM9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ioWfxYQ3IA7io0akaROvVlRGrbqUiKb6UbAO7n0GrMQdLiA_8IL5aG5E3_PBIQZdd5oPwFRHQ2YAlrwsWUnv2wEg9MGNb7icQSA8pEHWFGe1xTKAWbnx2TDIpGhgqlIVaLBDRkW6yKldjkqnQ9rMfBD1rO-7MhWYkui1NK30ToSWGMShsrq1zqrL5JHgG8nSNYHOYEbYRRfzJPRRSowCtkPBl6HxxoEgow8CM5smi6T96ZblhJhouw57j1hffqcINxhP-AS29UVuYjcwq9D8a1Z-Ma_BZcYENFceqY6BvbbfioQR2wk9FbXT1I80PQzn1DnvZTV9PnXte309pLiN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ioWfxYQ3IA7io0akaROvVlRGrbqUiKb6UbAO7n0GrMQdLiA_8IL5aG5E3_PBIQZdd5oPwFRHQ2YAlrwsWUnv2wEg9MGNb7icQSA8pEHWFGe1xTKAWbnx2TDIpGhgqlIVaLBDRkW6yKldjkqnQ9rMfBD1rO-7MhWYkui1NK30ToSWGMShsrq1zqrL5JHgG8nSNYHOYEbYRRfzJPRRSowCtkPBl6HxxoEgow8CM5smi6T96ZblhJhouw57j1hffqcINxhP-AS29UVuYjcwq9D8a1Z-Ma_BZcYENFceqY6BvbbfioQR2wk9FbXT1I80PQzn1DnvZTV9PnXte309pLiN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7bVe3FZb5AYye-dx0DViglpYF3hJ66Lo28s_6Yow7O62O-XvR9xQCKO88bpxBaYtczUyagkoRadgOCnqvoU3Iee5a6_f_ws-sxmnXJj5wmpnTwaNvxwmtc-z5VmfLvibOrV3RwpcDnvvMUHMKVTS8yBC8c8D3ekjSCrwP1UJSqn6yOmefL-PyyWjjY7bZqZ_eC-FJc03awPzfla5r_VUSJ9mVIFvYbGOWlFDlUmkIVGxM7OlPpHJSPpgWwoqVrg5XcDowQprdgu7e0zIfPN4VrO2Tv8Cp_dZZUqpKvP2sGcvNBg3vIOsVDWCKOg2cDIKT0Hqjkq2Y0R0tWhKfCluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7fg9C2wUsb71u7iuSGfYoiz7nV-ksacpD8CFUXZA7EnE-Cdwtu8TFyCbzGPcDUEagMiU3lyOahtG29T_O9_pO7-f66gAGd6rIPRJACDQMYcndK7zzDG5XpOkd7cFioHtLV49pllfzfDw7V2ItoAxtKd812H7gUmK0vtUTH2akHWU5Xr0wRbiYzKffoTG0nKkqHDH5avmOMbx5RV4UaQ56UaxDo5FdxP0tr7FwMgTME_jvWP7YU96sPWV1I0dMy-qoquCoovAP-o2YUEmizutfCDpfCacIxutSx6uJDRn9-HzyL4JD2OXDSfwK0XGDoZMylLBAWcbJYHeZAeX22I5kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7fg9C2wUsb71u7iuSGfYoiz7nV-ksacpD8CFUXZA7EnE-Cdwtu8TFyCbzGPcDUEagMiU3lyOahtG29T_O9_pO7-f66gAGd6rIPRJACDQMYcndK7zzDG5XpOkd7cFioHtLV49pllfzfDw7V2ItoAxtKd812H7gUmK0vtUTH2akHWU5Xr0wRbiYzKffoTG0nKkqHDH5avmOMbx5RV4UaQ56UaxDo5FdxP0tr7FwMgTME_jvWP7YU96sPWV1I0dMy-qoquCoovAP-o2YUEmizutfCDpfCacIxutSx6uJDRn9-HzyL4JD2OXDSfwK0XGDoZMylLBAWcbJYHeZAeX22I5kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=InZfKfHmAHBWsFWShN_BtsfzBDSStSSnidImHWzUmGJbZu8n5Y3pWI6jFfoIkTtgsfQVY9OHB2q8CQiR-5IprchOlbI8eqOmiURu1zFXyqbTiU_hfwoI2QuSrtCHVV43B0h2lDxhZnweVTQGf89yj6tePV0sd90oh1wq136HqDv8wS-Qp1TbHWawznT98a0AnO8NcliFf1xXfqHmgWYlV2zLx0LpXDViI4-BmN_-tegf5Ux4UwHKAEkeYhcZmCUCA1PRSkLh2ElraQ3N3Ghkyqwtd4iUDZg0AZUiEPLYqWrZ93niSuKpeflTEX7zcdidvPkn4XJhDO9mUfyVcfhNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=InZfKfHmAHBWsFWShN_BtsfzBDSStSSnidImHWzUmGJbZu8n5Y3pWI6jFfoIkTtgsfQVY9OHB2q8CQiR-5IprchOlbI8eqOmiURu1zFXyqbTiU_hfwoI2QuSrtCHVV43B0h2lDxhZnweVTQGf89yj6tePV0sd90oh1wq136HqDv8wS-Qp1TbHWawznT98a0AnO8NcliFf1xXfqHmgWYlV2zLx0LpXDViI4-BmN_-tegf5Ux4UwHKAEkeYhcZmCUCA1PRSkLh2ElraQ3N3Ghkyqwtd4iUDZg0AZUiEPLYqWrZ93niSuKpeflTEX7zcdidvPkn4XJhDO9mUfyVcfhNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=O-VAG1dqqhvgUsdU1LnnbzQkPumKBs9wvJiW2Xyz8_CBezJd9Gez4AAz0qIMGm6PdUhyfEDwokX5kcGXNdMCGW1ShYH8QE8V_mAGc0dM9Hd6S9cObKS6PDpT1T56PDmg34Irfmsj87wnITZ_pv54GYe-3qOKSOe8WWyi2LCjgpiCpdAtGg28b7ps-gSv_qvYbuoNNHiocfxPDkXLRi7bt2T7rgjxBIRcEvep4DVg5TX_TlVuFjqZbK42K6X8__roey47-nLkjmz9NafQDXJLwYk5k6llem2SLi0v4_T97uc6rRQHYvGecpPRRiBN1F-LsaRVXinYR32FFwr4XNcMvDyISv4eFDVlp1jB82w7CpIiB3zBk-F6O8V4qIcEaetb0GxTPzXFMVxCfSywfnBzwbRHsKeR5jGdqX84yfBF4hxw7PWSaCik4NaxDVjKGaVbQZMoJPPGcxp_8FO8uHMahUgQkZmHl3r-bHl1wyiI30hg66LlJW17lJixn-A0J0Z56l2_4-9P1y564PjNaFIh12tHDX02zZ3eTid3Gl7_X4vsjAZVe4m5Ftmq3G8aXZAruix9YqJTJoyZF2FFcmB6g88av_KJu9AWyCm4Nf7bI_59oGXdSIhUxKRWk-dkfBRkCeKg6Nl65EFlA79LRKuuQsoB6ocJCcS_HtOsV_PguoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=O-VAG1dqqhvgUsdU1LnnbzQkPumKBs9wvJiW2Xyz8_CBezJd9Gez4AAz0qIMGm6PdUhyfEDwokX5kcGXNdMCGW1ShYH8QE8V_mAGc0dM9Hd6S9cObKS6PDpT1T56PDmg34Irfmsj87wnITZ_pv54GYe-3qOKSOe8WWyi2LCjgpiCpdAtGg28b7ps-gSv_qvYbuoNNHiocfxPDkXLRi7bt2T7rgjxBIRcEvep4DVg5TX_TlVuFjqZbK42K6X8__roey47-nLkjmz9NafQDXJLwYk5k6llem2SLi0v4_T97uc6rRQHYvGecpPRRiBN1F-LsaRVXinYR32FFwr4XNcMvDyISv4eFDVlp1jB82w7CpIiB3zBk-F6O8V4qIcEaetb0GxTPzXFMVxCfSywfnBzwbRHsKeR5jGdqX84yfBF4hxw7PWSaCik4NaxDVjKGaVbQZMoJPPGcxp_8FO8uHMahUgQkZmHl3r-bHl1wyiI30hg66LlJW17lJixn-A0J0Z56l2_4-9P1y564PjNaFIh12tHDX02zZ3eTid3Gl7_X4vsjAZVe4m5Ftmq3G8aXZAruix9YqJTJoyZF2FFcmB6g88av_KJu9AWyCm4Nf7bI_59oGXdSIhUxKRWk-dkfBRkCeKg6Nl65EFlA79LRKuuQsoB6ocJCcS_HtOsV_PguoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=pf-j2n2oipMej5F9vvm_Uq2tI1Qwlj8_GYjMS6gUg87qz9mqM_hriH8hO7pTxNxCkvQj3O7KPNJwR1sgMlYAP-8yATXHP5cOXiokSiWrf2vQDAdY4l7KVZ-ThNZhWK9QLUkUcTbj8o-YMKUoUPk-Tx-1bhKkubdn1B11EeORM6yZsUKk4VgrYOfCY6vh2RP7cu8NvI6J77T1S-1SlGwswb0v5_eGYyLq9-Bt5yCodLlJcRqMa5Dahetq3yTEELDxenqlemLjSyUMrBCUWoEYh8o4JOplyAcvRBjoc0VhAjqiZJwtdUBHqoknYbMv5njdKxEf0frItTo_R8EmJTVZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=pf-j2n2oipMej5F9vvm_Uq2tI1Qwlj8_GYjMS6gUg87qz9mqM_hriH8hO7pTxNxCkvQj3O7KPNJwR1sgMlYAP-8yATXHP5cOXiokSiWrf2vQDAdY4l7KVZ-ThNZhWK9QLUkUcTbj8o-YMKUoUPk-Tx-1bhKkubdn1B11EeORM6yZsUKk4VgrYOfCY6vh2RP7cu8NvI6J77T1S-1SlGwswb0v5_eGYyLq9-Bt5yCodLlJcRqMa5Dahetq3yTEELDxenqlemLjSyUMrBCUWoEYh8o4JOplyAcvRBjoc0VhAjqiZJwtdUBHqoknYbMv5njdKxEf0frItTo_R8EmJTVZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT50QisneLGmb8UZfx2NhYuzJl86QWpSDWBcJRldbzPdz446iSJApwRUERLlPDRst7MGGr1_8Y6pyZBRc_dwbK8j3Raqvc_EZnlzuy9EuehxJRBF2DhMdSOBsWfg20M3nhUbvzlLLUCqqKu2tDAQ9Xs3kOC4-El65J08zWv6yO-aAyExnFhF8YR98nb6GpnPvfmZJ6rLTg3H0LRRoZ770PtrMePsgveX8EzkmCNK1Kujo5HQ6rPO4UDMAAXvU7wJxvGYHM1TE7cqeD2TBN0VjX3tLHr9twhrTDujjJ4UhlbFgPoxJVFQp4WXpbqvJyAkYIzONWN5aAi-cYIunPfaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Zi7i3jETSp67ke8BIdwtzVn0eHUcjjJPEip16YSZCctxql6-B12mgYoa20CnbPV8p7MWDjCaE2ndjxR7Y9kQzhiKm0VBIk3sBlSfrF8OPlwA30km-ue99T1R6sDONTAkuH-9pLh0BaQe4BEgSEWVXiEvn_O1f3D_lwqT66jzemEEQsaCzrCDPe6jOvH9Sd0sN7A3lBC62-Hc2yia6EE5D4ajm19mnG-74D4sSXVsJlaGRoC4NRJoHCloE-IU9CFh3SH7ARiautJiEae-8W1Wdpew2J8_wjVfAN03uSRYA3CZ1uEeirrC4SVOkWdabmkE4G6QC2UImc9kvCQ3ZhUYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Zi7i3jETSp67ke8BIdwtzVn0eHUcjjJPEip16YSZCctxql6-B12mgYoa20CnbPV8p7MWDjCaE2ndjxR7Y9kQzhiKm0VBIk3sBlSfrF8OPlwA30km-ue99T1R6sDONTAkuH-9pLh0BaQe4BEgSEWVXiEvn_O1f3D_lwqT66jzemEEQsaCzrCDPe6jOvH9Sd0sN7A3lBC62-Hc2yia6EE5D4ajm19mnG-74D4sSXVsJlaGRoC4NRJoHCloE-IU9CFh3SH7ARiautJiEae-8W1Wdpew2J8_wjVfAN03uSRYA3CZ1uEeirrC4SVOkWdabmkE4G6QC2UImc9kvCQ3ZhUYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vqjPq-dn0Foui2Foy5AFi0F-iLVQ_e51akOBtvR-zbVXttEXkF2PeV49s0U-irKxk1E9JHumGtIhq6IVA7Rfp66KEnXSkNRfkQroiTDOPAmZlHI0RTLi3YaWkJtVkV8AXZscvGrcTlSr--udy2gXzGiN-gBnEolA_17g9RC26yEC-tjuasTJV4epxzt8_85CHXiSMleojaRLInP--IEgdDgL81aHwoBrFqSe0g5Yfl1fzM8psAtkMvfHSqTgehUUDb7Fd_i7wfj_Aqbm5yp42efozuOLW-uvQ_XFbyJNOxt-_IoR4N0R4kTgAYJ7CPA-iHdY7Jr06CxPNoR5GwsqR63vzw6f4_SsCm67rdnG8Mtvj_imXCCLr4_zekMIs-dws6T8NIl1SXc6ttk63q9Gk4k-Dwxxihdilxzll0mD1iUazaYjRE3OXj2sm5axkphkdKuhRehD2T4q8eUQyM8Nb14rr2cAyJodoNUXP6hBHS7OwG6aDAbIbi3elaKISlEmVEDKXdHjCBsD_DcMMFlQqXmWR6m9sVKC7D4cFnx-nps6qZJpZZtAFvw-QgowcUGpoX28raLfXnkw6d9Zyx9rAd6M4eG3lCPnUnW4FLjunVn78mGJIXYC_KHxCyJ6WJnAfIR4NwygTuo5OTlWabmBGN9-5GJJphPCKoVhWiLNNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vqjPq-dn0Foui2Foy5AFi0F-iLVQ_e51akOBtvR-zbVXttEXkF2PeV49s0U-irKxk1E9JHumGtIhq6IVA7Rfp66KEnXSkNRfkQroiTDOPAmZlHI0RTLi3YaWkJtVkV8AXZscvGrcTlSr--udy2gXzGiN-gBnEolA_17g9RC26yEC-tjuasTJV4epxzt8_85CHXiSMleojaRLInP--IEgdDgL81aHwoBrFqSe0g5Yfl1fzM8psAtkMvfHSqTgehUUDb7Fd_i7wfj_Aqbm5yp42efozuOLW-uvQ_XFbyJNOxt-_IoR4N0R4kTgAYJ7CPA-iHdY7Jr06CxPNoR5GwsqR63vzw6f4_SsCm67rdnG8Mtvj_imXCCLr4_zekMIs-dws6T8NIl1SXc6ttk63q9Gk4k-Dwxxihdilxzll0mD1iUazaYjRE3OXj2sm5axkphkdKuhRehD2T4q8eUQyM8Nb14rr2cAyJodoNUXP6hBHS7OwG6aDAbIbi3elaKISlEmVEDKXdHjCBsD_DcMMFlQqXmWR6m9sVKC7D4cFnx-nps6qZJpZZtAFvw-QgowcUGpoX28raLfXnkw6d9Zyx9rAd6M4eG3lCPnUnW4FLjunVn78mGJIXYC_KHxCyJ6WJnAfIR4NwygTuo5OTlWabmBGN9-5GJJphPCKoVhWiLNNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGxWou2xCGLIT2ZWN-6N4KywCnGNrexoufyATF465yIcKYq2LmlBc-bnHskrueUAnFAySOT3pIl1HxU4NskY_Z6jxCQCUFIlgum9FkzTSv07r6yKKBpOD1AtvAkUH9msMKPXTlSTImJjS1Ty6YiBWHACv78MkaIvOQQCyKhkRNLfIjpcc_FRL_aQ3e2m4U2WbDxxPMy38N3vO3Ve8-7Mp_tlDxF4O6KNOaz3yz8SUWRuM87ys9C1rWAoMv2FapnLSsstlrDGbqru8Ga-ZMfHks2-0Stl3zkd9GzqTJ2XZ3DHYhYTJQDmH9jxaDETcoBUAsteM3wlJvlUQF6s66_K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NWl_QAt7vXVQeg7jXgveGsjs9EXhLqmnM2yCFZymtC2iUfZXO6Wb9CnfedsKoE5DBwf91lFCa3fZRMVeAWs2ECLnmliQDMgZ_Pu9bQIf2dcCNj8p3tfE0CsHPqwCcRceCjh6LeS0do0C5bqyTKlOG23S32xzVMdChgKs0CxwBSgyI_XBqw7dHOCMEKw583qBBs7yo_38lbZ2DOmFKBW3GovcMUdA9-H86Fs4CVt3sSLkYn5mV6k5AykDyzNWIf-o0q0LhVBQCcMHHwKZyuQELggvNAyVS20zIIw9HzdzLn3QOOfVE42IOtdBuMy0-CTC4PiSAY1VQfoHvoY0WjT2Ar8bFIDO7UtldC8Q2xZUd8W_n_VbHgoJcsWO7wNcqkkO8m8OjIsN26t6JfB4tC4gWnMkFpU6FYkO80qE7zyNgk3YT3apWaxAULNW7JzHYUUmzWWC6aDA1xbuCGUjyveSOALFA6YfSnlN4y-lsT3mWo2GmY2qjMJgGIbYYzW218LIzgdXzXuEX-a3Gq1uX9w6bIamvtHvIR-sYc4qw4INPbgStJsWsMlCJ-BlDE1kWa3PSXPM3rCQgt6JfxY0FOJ8qAeMkneBZlIQjdQ2pcoypg3-tQNCkBSHqU-T6tFq9FhOFxUOnbfdceuwchUS7jMQawG9KQhdGduazwRr61c6f1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NWl_QAt7vXVQeg7jXgveGsjs9EXhLqmnM2yCFZymtC2iUfZXO6Wb9CnfedsKoE5DBwf91lFCa3fZRMVeAWs2ECLnmliQDMgZ_Pu9bQIf2dcCNj8p3tfE0CsHPqwCcRceCjh6LeS0do0C5bqyTKlOG23S32xzVMdChgKs0CxwBSgyI_XBqw7dHOCMEKw583qBBs7yo_38lbZ2DOmFKBW3GovcMUdA9-H86Fs4CVt3sSLkYn5mV6k5AykDyzNWIf-o0q0LhVBQCcMHHwKZyuQELggvNAyVS20zIIw9HzdzLn3QOOfVE42IOtdBuMy0-CTC4PiSAY1VQfoHvoY0WjT2Ar8bFIDO7UtldC8Q2xZUd8W_n_VbHgoJcsWO7wNcqkkO8m8OjIsN26t6JfB4tC4gWnMkFpU6FYkO80qE7zyNgk3YT3apWaxAULNW7JzHYUUmzWWC6aDA1xbuCGUjyveSOALFA6YfSnlN4y-lsT3mWo2GmY2qjMJgGIbYYzW218LIzgdXzXuEX-a3Gq1uX9w6bIamvtHvIR-sYc4qw4INPbgStJsWsMlCJ-BlDE1kWa3PSXPM3rCQgt6JfxY0FOJ8qAeMkneBZlIQjdQ2pcoypg3-tQNCkBSHqU-T6tFq9FhOFxUOnbfdceuwchUS7jMQawG9KQhdGduazwRr61c6f1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=D3E6Dsv-4C5-iMNBMQQfMWBooo9dIdgENtYOqgyE1qQWl0EEJpTGRIMhw6hP0eYob0NrhOIstfdfLqLrq3_gWVDdd1BJT7e1kZU087e9f5ZgCCcEDIeFFbWYd6dN_0jLrtUD8vpvECtw3mFdQZWqdiJ4dwmmfy5njPGLXS5dguT7Vr868oOcQcRa_JC8fLCUn-_1NKaroh6CxLzFuw6Ig1LMqbJ_8PSN0ZcAnLUZ54OYniyDslRWF78HIS76iat0XPNkor408_WRgswD_yF6_atfD2T0CQc7ZsoW80sJhfKABJUgwyOqlKmsAKOWPNFJIlePEJZN3tk5sE2KrHGu91fDmzChzZ0IjtsYlsBAUfRp_SixntKGAaLxgtWQenqpyHUBzDjX8189HaLiRZxw5-JOyET626wIgu5Tt0sRSsvKMjG2YmPPtZGN6d-366DvVV3FCgYXnKX0bIF3GmiY7MPdrFeyclsYQvKQwELaXSJxnW_1MaU2WzaR-CDEQnaoI5JLuVWH2UpNURk161koPRcKYaGDZmRlW_AKaBcTgBPQokOLBgt2tiFB5bwVoR0e_DzLVQl0UiMwrdek-loAwwb68A8dj5c4frplP7KSo3-Qkicu4XIpXq_EB1YsZkuDIXtRpt67gq5yCVeCisDnYvMYXMiJtM69k5gLlpgkRTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=D3E6Dsv-4C5-iMNBMQQfMWBooo9dIdgENtYOqgyE1qQWl0EEJpTGRIMhw6hP0eYob0NrhOIstfdfLqLrq3_gWVDdd1BJT7e1kZU087e9f5ZgCCcEDIeFFbWYd6dN_0jLrtUD8vpvECtw3mFdQZWqdiJ4dwmmfy5njPGLXS5dguT7Vr868oOcQcRa_JC8fLCUn-_1NKaroh6CxLzFuw6Ig1LMqbJ_8PSN0ZcAnLUZ54OYniyDslRWF78HIS76iat0XPNkor408_WRgswD_yF6_atfD2T0CQc7ZsoW80sJhfKABJUgwyOqlKmsAKOWPNFJIlePEJZN3tk5sE2KrHGu91fDmzChzZ0IjtsYlsBAUfRp_SixntKGAaLxgtWQenqpyHUBzDjX8189HaLiRZxw5-JOyET626wIgu5Tt0sRSsvKMjG2YmPPtZGN6d-366DvVV3FCgYXnKX0bIF3GmiY7MPdrFeyclsYQvKQwELaXSJxnW_1MaU2WzaR-CDEQnaoI5JLuVWH2UpNURk161koPRcKYaGDZmRlW_AKaBcTgBPQokOLBgt2tiFB5bwVoR0e_DzLVQl0UiMwrdek-loAwwb68A8dj5c4frplP7KSo3-Qkicu4XIpXq_EB1YsZkuDIXtRpt67gq5yCVeCisDnYvMYXMiJtM69k5gLlpgkRTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=kKnKnkMwwjBRVEO0vzoqh16-PbLRrbCPgxCLhbspV-rOt_o7w1f1aa9EKdIaFcbXY5hE8xMRxc8BCLWuexj4_ythwHAOUVC-XfYl_RLZoaB1w-BH9RyKDtX3qV-Asq3OKBn8Cnp5vOrtLro3peVbSRQR8jKkruLpgbXbBa_kDJM3xmRgzZ0LRmyOm3t_No6-LyTPQEbU4VWHS78BjncqeHzZ5_pjCNH9-BGORbeUaFwpv1EDipH_OeURZ6YACdAp4sk4iTP-Uuel3n2ebofjeArMvYj5V4_mUrq4fiePEu3c1i9Cj6KZ2PEMnihxdstLn1LEZKU52irlogPfx4He6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=kKnKnkMwwjBRVEO0vzoqh16-PbLRrbCPgxCLhbspV-rOt_o7w1f1aa9EKdIaFcbXY5hE8xMRxc8BCLWuexj4_ythwHAOUVC-XfYl_RLZoaB1w-BH9RyKDtX3qV-Asq3OKBn8Cnp5vOrtLro3peVbSRQR8jKkruLpgbXbBa_kDJM3xmRgzZ0LRmyOm3t_No6-LyTPQEbU4VWHS78BjncqeHzZ5_pjCNH9-BGORbeUaFwpv1EDipH_OeURZ6YACdAp4sk4iTP-Uuel3n2ebofjeArMvYj5V4_mUrq4fiePEu3c1i9Cj6KZ2PEMnihxdstLn1LEZKU52irlogPfx4He6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=R4HrCYwTL466r6gNCmvr0xRP0NhJDFkYQqYke3-iDibRgXXRkEuNEM8OrkosM-x-jKFTH-FsHPqJDUm_aA05ikPYGZ8Hi8i8oVzFs-ol_AM5lCd8Xwf7KMl7vWqNPdp1Vxntv1FkPsT99EvZpGqUAmlRM0E8G4kQiAe0omLybF1Zldf7haJlGiTiICFmOxRcz16xef9ywAX3eRtse3a0MKallX1HXvJLWrhg3SXe1Ac1KgFONugDLNFSbUdS8f6YyDglepSf2izVD9YZPK_kse-VGoNS8P-iveEDa-xU4LD6mcLQyirnO1CtK1Vs2i-oZHUUpo9Fh3A5GF4Aezchig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=R4HrCYwTL466r6gNCmvr0xRP0NhJDFkYQqYke3-iDibRgXXRkEuNEM8OrkosM-x-jKFTH-FsHPqJDUm_aA05ikPYGZ8Hi8i8oVzFs-ol_AM5lCd8Xwf7KMl7vWqNPdp1Vxntv1FkPsT99EvZpGqUAmlRM0E8G4kQiAe0omLybF1Zldf7haJlGiTiICFmOxRcz16xef9ywAX3eRtse3a0MKallX1HXvJLWrhg3SXe1Ac1KgFONugDLNFSbUdS8f6YyDglepSf2izVD9YZPK_kse-VGoNS8P-iveEDa-xU4LD6mcLQyirnO1CtK1Vs2i-oZHUUpo9Fh3A5GF4Aezchig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=px6qkPFd2890FKq7mv_LsaXbDv5w8ZpKubAO5qQ0B5YHeCN5WS2TYeWMKRIc1PCNu457de0zQ9bdFO4YtFVBzTs4HnFRHfEcX3ABpWfNlxCHrjRYZTb3THY7JHN8VV-yMoiH4DoPoEMFE4tyvxhE5FcLSvte19iaLXPLbFv2_z8MORHwD9n0T-W3zYOEXqjC7GqJ3-YC4bZk4q04d5dEiEVGx2PleDkCY6e2J5kmah86R5Iw2v8IAu78azYHDzbaVcuZV0CxLt2G6T1DQ_io9Nrkth6c3cMty469Z-UT2tP_B5N-5n0ui8CvvMkWlmRnOn5JMi26U4rpHCiiC7ExqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=px6qkPFd2890FKq7mv_LsaXbDv5w8ZpKubAO5qQ0B5YHeCN5WS2TYeWMKRIc1PCNu457de0zQ9bdFO4YtFVBzTs4HnFRHfEcX3ABpWfNlxCHrjRYZTb3THY7JHN8VV-yMoiH4DoPoEMFE4tyvxhE5FcLSvte19iaLXPLbFv2_z8MORHwD9n0T-W3zYOEXqjC7GqJ3-YC4bZk4q04d5dEiEVGx2PleDkCY6e2J5kmah86R5Iw2v8IAu78azYHDzbaVcuZV0CxLt2G6T1DQ_io9Nrkth6c3cMty469Z-UT2tP_B5N-5n0ui8CvvMkWlmRnOn5JMi26U4rpHCiiC7ExqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=m9ES_M7BqzpJ6FzqWjKhSl7nalzRqjSwUsVFpXohPD1dKW5KGRiTldrJfNCHD1-sy_apyJBf8jJ3JoMWgxZ77gfYr-PoIO_dh_ag80TbLuwRMHvkb4Lia7JlQhALbO6W2kF5vm5lBr2UCqVqIE1o5sINOB6-RTOiIaq9SkcLDeuB1quQ9nhoroBCvbe0OMzo2TsSF9EFOxFCsdWFZFVXvud2ZltKJ5cBM-vKuXxSnFipZaoKQoRtvB-p36SzQR2PptQRkLU98edndSIswinbzlCHPpj-PSspwkoybaADcs3txCfOlIDLhtF1XQZh6OneUsQsPD8OzC9G9KGx3tbSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=m9ES_M7BqzpJ6FzqWjKhSl7nalzRqjSwUsVFpXohPD1dKW5KGRiTldrJfNCHD1-sy_apyJBf8jJ3JoMWgxZ77gfYr-PoIO_dh_ag80TbLuwRMHvkb4Lia7JlQhALbO6W2kF5vm5lBr2UCqVqIE1o5sINOB6-RTOiIaq9SkcLDeuB1quQ9nhoroBCvbe0OMzo2TsSF9EFOxFCsdWFZFVXvud2ZltKJ5cBM-vKuXxSnFipZaoKQoRtvB-p36SzQR2PptQRkLU98edndSIswinbzlCHPpj-PSspwkoybaADcs3txCfOlIDLhtF1XQZh6OneUsQsPD8OzC9G9KGx3tbSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=XD-5u0xUv373vVwtsPaQNrOhJIAu28kRkJ-hEqvmVH_-kdUCBKMP1Md9KxSd7n8Un6r3gjz3UJpBJMM6Hlej78EDrRvOcu0HLgb0h0heh29cfOZm5KUtT0MPQH5IPXwtR0aP4bAUzFHu63umE5uoXTA4S7QkvpOyIHfJTF4q3CSAWiLQu9xD4Z5MYij3n3K0zfbjwZtF8bAsz5StQN5q6_ATDsyCMpYgOwIOQxCz9t-qCCx5JoT1urhcYtSJhYRZwYG60y7nIbSa6zaPBN3o6A5eOhkvyYXABFC_U43Mr1YuGlY9cl9g_g21cVZFCAEKvL_Ldar2P-MgzPaiuSG-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=XD-5u0xUv373vVwtsPaQNrOhJIAu28kRkJ-hEqvmVH_-kdUCBKMP1Md9KxSd7n8Un6r3gjz3UJpBJMM6Hlej78EDrRvOcu0HLgb0h0heh29cfOZm5KUtT0MPQH5IPXwtR0aP4bAUzFHu63umE5uoXTA4S7QkvpOyIHfJTF4q3CSAWiLQu9xD4Z5MYij3n3K0zfbjwZtF8bAsz5StQN5q6_ATDsyCMpYgOwIOQxCz9t-qCCx5JoT1urhcYtSJhYRZwYG60y7nIbSa6zaPBN3o6A5eOhkvyYXABFC_U43Mr1YuGlY9cl9g_g21cVZFCAEKvL_Ldar2P-MgzPaiuSG-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LtzqT0Lr08edAuXU7X-03the9XMezXoku4NxPshZp9qJBETn6aVoR_IaodebAI2tgfFvs2xxqn59AIfjbDCqVHZw0NysxQFWrRNzTqgKkpESQcYV0w6-4hup2NkBDnNWwgncVPOs-Z8eL5rtf4RwvRbrO5mZgVB3zGUV9dj4suXg--DrI_rlUbgxU8efAUcxrh5tTHO9SJyO4lAWyMnLsGTN_fU43Ksnm8z1a_kGr8e8p3SYnL2DO3jEFc3gIqhsR9j3jvr7R1y_ZtPberkkKLc290FQS8kISHjtcFkLr1jMWZFq9nyMTswm98n3T9Xvpv8glg-XOCWDQX9oJROgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LtzqT0Lr08edAuXU7X-03the9XMezXoku4NxPshZp9qJBETn6aVoR_IaodebAI2tgfFvs2xxqn59AIfjbDCqVHZw0NysxQFWrRNzTqgKkpESQcYV0w6-4hup2NkBDnNWwgncVPOs-Z8eL5rtf4RwvRbrO5mZgVB3zGUV9dj4suXg--DrI_rlUbgxU8efAUcxrh5tTHO9SJyO4lAWyMnLsGTN_fU43Ksnm8z1a_kGr8e8p3SYnL2DO3jEFc3gIqhsR9j3jvr7R1y_ZtPberkkKLc290FQS8kISHjtcFkLr1jMWZFq9nyMTswm98n3T9Xvpv8glg-XOCWDQX9oJROgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=PFMjU-IYeX4RZbSB1sDjzVClwJxchgW78tTX5_kE2KVIFbU8T67MJoxV_jDPRT_HmkLXVZ5haBr7tr2t2_-U-Eyz5UolSxizLcU14_Ep3Fu-oQ8Kl0pfvWD_IG_QYIY_YSaM3OpK_qHC1R8fg-79s3Uw1ZqBkUV7hfGHd4nGiM1W-BUamFB3GQfDtXnlMy8_JcZealzS7x7eFSPxxb5cTKOdWGnXQKPsXuxOXpNVMIPuWiYoVONYgis8Mvfx-PuJn8XVYGZSbAJ2aQVE6eemOz-XzhzSo0pvCXBZ2p3B6r_BmAlGGTVRND99OYHWEpQhII5zybDWYCuVEgyBY3W1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=PFMjU-IYeX4RZbSB1sDjzVClwJxchgW78tTX5_kE2KVIFbU8T67MJoxV_jDPRT_HmkLXVZ5haBr7tr2t2_-U-Eyz5UolSxizLcU14_Ep3Fu-oQ8Kl0pfvWD_IG_QYIY_YSaM3OpK_qHC1R8fg-79s3Uw1ZqBkUV7hfGHd4nGiM1W-BUamFB3GQfDtXnlMy8_JcZealzS7x7eFSPxxb5cTKOdWGnXQKPsXuxOXpNVMIPuWiYoVONYgis8Mvfx-PuJn8XVYGZSbAJ2aQVE6eemOz-XzhzSo0pvCXBZ2p3B6r_BmAlGGTVRND99OYHWEpQhII5zybDWYCuVEgyBY3W1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOFlKEqlSdPEXaygK5KGFzh-NpVW3IPQH08Wa0MmxnFPGot_eiTssuce88ckwok9MtozUgP5zmVTOQkpqDT9JQ7foVkEWC9CdRIJmf0n20Ylcnuf1MqN4rqSxbjMIePL5q3Ur4YcV_zk8JCiJem33mRDobS0Kzay8FF2ABOX-ov4hgYpZg2jAp4wJRJLnUjFiVsfHXfF4zcSy1an9iWPIuhsohZz6x3Zu0ELoPtR86qrIJeHjZcL-mRNtS-xwgbi1IbBrMeCTCPgG9d4CRlJeCVX7H3x4pG_KOwK0uINlM71ePVeWkoKoJWemkjPiH1ghcHIdCBFHBvbTDi7Mclt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=nrIbvIMmf0_MqbqXuEqu3ad-3nkvfcywv4oGq_tqJ8E0K0wNcm6KjraUEQxIQYnC1e346KNBDV5nl0fd4JvPij5OJGjz3yN2nTU17aHLTL_SflvDuB74RmKyl16-PicTlaWLwI7BPH7VIK5a_A6yY_lf1hSWSzEcsAnCkIOCZCmWr1Bot_lwjBaMUOD1DYSuI59FcFxFVz1PFUSqgq3Wa7EdCZ-5faTTUxWcuTYpVYoZUKyHS1sidWgtrfy7_9yicZ0ex9RdUcpTWV8Nt5-ZJCkTsRIQVz7iFbleae0JiBfu323IrflApRRGmddFTJ2d2vwaDraZ7mDqtLzbR-xYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=nrIbvIMmf0_MqbqXuEqu3ad-3nkvfcywv4oGq_tqJ8E0K0wNcm6KjraUEQxIQYnC1e346KNBDV5nl0fd4JvPij5OJGjz3yN2nTU17aHLTL_SflvDuB74RmKyl16-PicTlaWLwI7BPH7VIK5a_A6yY_lf1hSWSzEcsAnCkIOCZCmWr1Bot_lwjBaMUOD1DYSuI59FcFxFVz1PFUSqgq3Wa7EdCZ-5faTTUxWcuTYpVYoZUKyHS1sidWgtrfy7_9yicZ0ex9RdUcpTWV8Nt5-ZJCkTsRIQVz7iFbleae0JiBfu323IrflApRRGmddFTJ2d2vwaDraZ7mDqtLzbR-xYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=oae7DEgDikx-6m1hrLYZ5Da4XieMaDKnH9kTlyjOFQl_-Q9y2qb59VMrCbnd6Rs-Ng7LSOhe0U4SBOUCQ3q3SKo-FkjRZA2u0Pg3ygIyVP6yUzeTS6q3YRFUGqXomIKoT_fls7olDyzGAMnExQN8Pp7D-L7cwM6JXrBo43iSQSl7P2cPL8XmirYgcJA_QID3KALqPjPupQVRW6uG7FQXJi2tP-f15U3p_sgvvxnNmgYEyniJKJkblKbkxBQfWQKipqzVHel8QgjGvNRZSw-R0iKFcHqFzpHcWEK4a1mCnwOCi--95JRxVWUbmGp0HN8NTVHOMJnyedfGwwDNY02jhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=oae7DEgDikx-6m1hrLYZ5Da4XieMaDKnH9kTlyjOFQl_-Q9y2qb59VMrCbnd6Rs-Ng7LSOhe0U4SBOUCQ3q3SKo-FkjRZA2u0Pg3ygIyVP6yUzeTS6q3YRFUGqXomIKoT_fls7olDyzGAMnExQN8Pp7D-L7cwM6JXrBo43iSQSl7P2cPL8XmirYgcJA_QID3KALqPjPupQVRW6uG7FQXJi2tP-f15U3p_sgvvxnNmgYEyniJKJkblKbkxBQfWQKipqzVHel8QgjGvNRZSw-R0iKFcHqFzpHcWEK4a1mCnwOCi--95JRxVWUbmGp0HN8NTVHOMJnyedfGwwDNY02jhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=RjbCN94LEfhrc3FHGSPKdHHzuoiIwl8o7mh9SZOBSzPUbuJRSPIU3fY6GAmgnDNsJ972_xSLueMeTWKhmk-RKha4R3JDifhBTNZvkTBDt92Arp-HX721nVWh2pvOhf5Vh0rVKJPB1_9SikNwlB1xOCRCqtxabYX1IZ8D0yNa5po5yA82Z9_mYhFAXHgihyUhTxvYperBg8MwrutnQIK4NtAdPYoZF6xklbkrUfexi8RlIKJ2ba40WrnJKyS8dYAKOrBSrEy4nP2-7WE68xUiaUiaz1WMYT47ghW5rqlOKETTZIuo064cV2YS4CDEzC2COydICH5lPTNdOFt2g_eK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=RjbCN94LEfhrc3FHGSPKdHHzuoiIwl8o7mh9SZOBSzPUbuJRSPIU3fY6GAmgnDNsJ972_xSLueMeTWKhmk-RKha4R3JDifhBTNZvkTBDt92Arp-HX721nVWh2pvOhf5Vh0rVKJPB1_9SikNwlB1xOCRCqtxabYX1IZ8D0yNa5po5yA82Z9_mYhFAXHgihyUhTxvYperBg8MwrutnQIK4NtAdPYoZF6xklbkrUfexi8RlIKJ2ba40WrnJKyS8dYAKOrBSrEy4nP2-7WE68xUiaUiaz1WMYT47ghW5rqlOKETTZIuo064cV2YS4CDEzC2COydICH5lPTNdOFt2g_eK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ETdkNM5Ac_wIkECeN6LdtOC9MgH5vln-xw5BHF43N7YYPKTX54DQVitYbvQXi4c_-Z49TJAhqDrMeE-8eQ6dUHL_ZybZwZhI5F-QK4W-yHVpZzzRV0UEXCvVI9dKNItfgoSLXGbIz2X8OvfHYlHgoxcplVv3q0R4ZDpTv0_EoKHJzvQYVVUJS5gNeVLiZh8H1MbFbLxxvmq11M_VlVk9UFMYZokokd9hrPIToG0mFWbxlwNjFpSjLjSkKM4Uecmh3UysFH9c2TPHvZzc6DgQ6c8OqU79ITivb3kpTKTpz6F-9zhtGg3CTm5Vtkupc0VIhYV1g0C5lcum8JL3ZK4brw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ETdkNM5Ac_wIkECeN6LdtOC9MgH5vln-xw5BHF43N7YYPKTX54DQVitYbvQXi4c_-Z49TJAhqDrMeE-8eQ6dUHL_ZybZwZhI5F-QK4W-yHVpZzzRV0UEXCvVI9dKNItfgoSLXGbIz2X8OvfHYlHgoxcplVv3q0R4ZDpTv0_EoKHJzvQYVVUJS5gNeVLiZh8H1MbFbLxxvmq11M_VlVk9UFMYZokokd9hrPIToG0mFWbxlwNjFpSjLjSkKM4Uecmh3UysFH9c2TPHvZzc6DgQ6c8OqU79ITivb3kpTKTpz6F-9zhtGg3CTm5Vtkupc0VIhYV1g0C5lcum8JL3ZK4brw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4HYYl5ZcbmcUybQHbszsXDUmW8viEpgya2fRKXpyr07xZrbkeh64AHHNtwNHairPO1qvnYpX3MU_1WnnfF1ntfAnitacXv7BKxZ0h51oX5YA8p58VLpqamFyBfrWJkUN9DdWXuFIUbCh14DXIk-Dj6UNqW_tiuXpE1Czd7KGa80PzOJca-vgw0tlXgKPH-CnUgGOaF96dedAzaBQvnN9ZpORgshR8RNJotiqWYqXrvI2ZPtJXi3kpCxuYA0c5_DYmaRh-NHpXJ3E9femmJFOudUJsZrScW0NyLyuEUArKxftRWhLFotCd9lxi854Tgbg9MbN10prgoonNWNtX1vtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ANk_sFtY0j0XJRlwwuyclrjM7g6eHe0K2EtmxWrQM6Fzgv7QnQ28WjzCD6MgvgFJMP8vChVifh4oqr3gx3KR3NOoCKlclogj4AAEcUiFUUSs87aKDYT4-fD2dt_o7rGT8W_1XHM8SoQ9GyVqVhf50wxOvc74fR5DKRCYL98IEQ73JVP8B4q_qYYS9cfz1P4wAGxPKhg8Wf78sFp2lJEtv6Mi-BnEZbOGlUQQLEbKckeQF9MsRca-r2d-5XSjqp5UjkYSbDGjfWymyb5TZO3Me3Ys_72gNpz9n4I4B9iGXg104TGjHSsCGw34awT2iu7n4XcuuVJ6eGtzGUipu7dEsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ANk_sFtY0j0XJRlwwuyclrjM7g6eHe0K2EtmxWrQM6Fzgv7QnQ28WjzCD6MgvgFJMP8vChVifh4oqr3gx3KR3NOoCKlclogj4AAEcUiFUUSs87aKDYT4-fD2dt_o7rGT8W_1XHM8SoQ9GyVqVhf50wxOvc74fR5DKRCYL98IEQ73JVP8B4q_qYYS9cfz1P4wAGxPKhg8Wf78sFp2lJEtv6Mi-BnEZbOGlUQQLEbKckeQF9MsRca-r2d-5XSjqp5UjkYSbDGjfWymyb5TZO3Me3Ys_72gNpz9n4I4B9iGXg104TGjHSsCGw34awT2iu7n4XcuuVJ6eGtzGUipu7dEsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=naIqm-GcYD1NUmN6gF2R3aY-BZVUjaiALretyC5AsHj_g0y6ziU058ruTTXumy4UUAqccoFj0-i00_Xxjp5xeYiQleeQKrXL-SEOiS3igUSnbrZXZcKNG0zncMg1RNA_nNBd0MhfxhqNTGImLCe5SDn1XJsoL75yMuJkvFZUEsYTpHTCoP3LkFWb0_Nvv8WpXJK8Bv5-M5SRF-4lYVcNyGdKcX6OZaDHDEkoAHloWtLIqLhif5bIu_EhNusNz7n5X0h30IfYQHhWBjdQaHoI4wg26P9mALb885sbU4PxYPowJq2N88VFzZLIcLwYcgqdmdXlZ6XXdgHG6x6vxVbQNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=naIqm-GcYD1NUmN6gF2R3aY-BZVUjaiALretyC5AsHj_g0y6ziU058ruTTXumy4UUAqccoFj0-i00_Xxjp5xeYiQleeQKrXL-SEOiS3igUSnbrZXZcKNG0zncMg1RNA_nNBd0MhfxhqNTGImLCe5SDn1XJsoL75yMuJkvFZUEsYTpHTCoP3LkFWb0_Nvv8WpXJK8Bv5-M5SRF-4lYVcNyGdKcX6OZaDHDEkoAHloWtLIqLhif5bIu_EhNusNz7n5X0h30IfYQHhWBjdQaHoI4wg26P9mALb885sbU4PxYPowJq2N88VFzZLIcLwYcgqdmdXlZ6XXdgHG6x6vxVbQNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKPzRHVK9dhk_7p3yinTcoyIi713JyCTppSl-C6vooSuSIB0aYOxqD6s-IR4mEKjBkXHZsJQMexUOLYHxKnCjGEROdcS5xfxkg7zsqfuzuxRIhLlphjfZW0UkK-gZk6B2mgBGVmGgw6x_-rw4ID8uIztLAGexDzAnw0VgancaIxWg5ogcHa4guImZhVd9gEEUx-50z9JlpHAV-1hPpL3GSBWA12AaMvQRqY8kv5NCb7DJ6hk5oiiU0T3yowP2r6jHfHjXwBmoMzaD1rNIo4g9XX2pqY6sJ4p1PWg5I-hSan6kgkwXvLiTMtJ2_VvSPNRHrPsV2-q4n-Qrs0w1zw7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9asvv1Rl_8V2sQSJiV5BVzndeoyOv-fjwLYL5O-pEApu8iOxFpgzSFfV8hpmhV8jlUQNSkxtaio-FcWVQymeLfgt3bNMHoHE6ws9sTxWXV3omkx2fTQAXhFuExo05j6h5r86KZthrZGS6_NdV6lCV2zTZvM8scC548EPcQS6cu92NumMQZBTSmifpVao0DyVu0_DzAOmE79OYb_Z57ctE2MSsPPgVqZ9brwm3A1uzzlj8CC5UURA5iM1RDJ_rYW1Zy5HjLEe5M4L3zL6e7Wm7OIaa7LNXmnp5IqxtA6TKnRhoaTp23nhS7gH5OZXUlr1HD8P6Jsn_bhLw59b7cIdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=p8ruRrvBrLJ68PaWiGTBmalj1htaQZkoUdAh_roJx_ybrOYpRgbQxauWyGcKye03lGl5GIBhGRv681gE-2_zsQgpyKvGypwdI-sIC2kLorHSC-6uo62AgR5B5DXmj5k09jfEMVxXb6uy0teNPKzG6fqNpPLCpsnQX1_tM4uCPTP6dqGB9jPQHsN7vV-3t68XkPWWaS9pNHiG6UUEjY-9V-mKdP9SMXY6GVsIIapR4hp1yNAFuopzQwRY8P745GAycIkDttilUNyew8MyXPnbv8FJtRluVmunxtVSZ6k6x3vXG5wlUuNLp3R6Ki_ESeVM9yYbbNX2uRAkx5XaPmPmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=p8ruRrvBrLJ68PaWiGTBmalj1htaQZkoUdAh_roJx_ybrOYpRgbQxauWyGcKye03lGl5GIBhGRv681gE-2_zsQgpyKvGypwdI-sIC2kLorHSC-6uo62AgR5B5DXmj5k09jfEMVxXb6uy0teNPKzG6fqNpPLCpsnQX1_tM4uCPTP6dqGB9jPQHsN7vV-3t68XkPWWaS9pNHiG6UUEjY-9V-mKdP9SMXY6GVsIIapR4hp1yNAFuopzQwRY8P745GAycIkDttilUNyew8MyXPnbv8FJtRluVmunxtVSZ6k6x3vXG5wlUuNLp3R6Ki_ESeVM9yYbbNX2uRAkx5XaPmPmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj9IGWD_0D__rYBoWY7BwJoDZLaEn_q1ImGnu41vZ5d5qsTtNdWnapb0o3CahazHkUY4xHigOwxLLbMilaY3IhmUzEkCH7YmMxb7rvZj0e-7rcBaINyZyqD-hL_QDZfTasSh1ezf93grwVVk4SdzQzVZcSXLbTUEk-nXFhS0k357oVDOXqVneB9TUcsb1Df2WcOSYMs8bI3ogxSMV2rbzV5s6YlhoGIZAoembsLe4F_JJn6N_mTqH2fKDcpT64QUv9jfN5I3kH34LPggobcV27o-IvXgdiCOG8m8EEEh-y-PIHLLjmjXqtJ9K6bs_NNno1vJGbqfwfmDPMoJX_p-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr7K42DPdyX6hMi28EosZGXR9lGRbgwPiVvcfFFsOPwfmUqpLlXn__nCl_Aw0Qq3463yuN6TjzBS96bHtejhGScfxJ0tf4IG7q_Aj5VfFmXs18FNXblspG0trxqAomEekDm5QmbdK6rdv5sgATtBfas_940wxCAEJ7vsXKV9420Syhbp3Yl8Up4m_60qS0z-t342F3ndXhM1OO35S0upqsmOUa9lPBPfgwz51S4gQDA2GzVe8JT_aUavkbfIkEAOjp_a4IWhAIcr7JlU9kZE_ZgI0_0X3gjCm7qLsNE_ctjtFhxy_8rdPyqirIcUduccDYRBnEqtdVgjsYAJvnO1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlibKtUfqqfR-HG9AASOZy4cqofBIenfE5SE8DF-tcst5v4wHvj74DkOsdJFa-dxeOTIhBfW4fBugmyrTqh-4Xpq0c9zTSLP77IpUePuxq61u2Je7NIAiZ3BUEQTF-FyrMNkY9zwDIH_bFttzx2mt3m0mKmws8IEbIuL55WJIv7W9eBd5S7smUbZpPeySVQAOE4R3njAZEUrG5DsuOKsxTLmRzyr7ZcOBkKPpe8dn1Jhf-8l-xvNjyaUtHuMJj8GgbO7jL8N-aT7_0R6FeJQOMfcl2q-NxH3JXLjzY1nelICiAJ7f0vBYtdZ0xDfV1W-ckTIlvwfcwn7fPqTi1kpwA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=p0g4B-jao2FIX32rdL4eI4FG8cMcpuOFeVVTdTvIWT_85xl1-95ZwiPUpLioPrJwyu4I_9PQ1wcmcLXFdU_hxOXnPNkD03b3HC1_KndX9GL9l54H0Bih1KJ61BZAfdRxxjZR6tBIRyj48EPIcrM6hOo5yxKR90MBEQzcs8mbVT1Fv2kdDXuoeEzlhtXLGEiGVQ_fESg1jyCsVoqPGhdBS5hWDbe8XvPPg5pxbVX4djPYKf9BKJHNkrT4CPDvQJlYFGkP129iwniuDTp_qI8yqkuc6YUmKQHrUPF9-AMvS0aSRuZfpU-2Md_aHROn8j7BRVv5onCwr_mVBvtzCcVl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=p0g4B-jao2FIX32rdL4eI4FG8cMcpuOFeVVTdTvIWT_85xl1-95ZwiPUpLioPrJwyu4I_9PQ1wcmcLXFdU_hxOXnPNkD03b3HC1_KndX9GL9l54H0Bih1KJ61BZAfdRxxjZR6tBIRyj48EPIcrM6hOo5yxKR90MBEQzcs8mbVT1Fv2kdDXuoeEzlhtXLGEiGVQ_fESg1jyCsVoqPGhdBS5hWDbe8XvPPg5pxbVX4djPYKf9BKJHNkrT4CPDvQJlYFGkP129iwniuDTp_qI8yqkuc6YUmKQHrUPF9-AMvS0aSRuZfpU-2Md_aHROn8j7BRVv5onCwr_mVBvtzCcVl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=m48x14eNyN6eft4Jv5w0qaIq82daRkkWTBWamo5mU_ndwfGGhF3L_XFjsz7R9SV41C9WmIF3UWiNuTz7T3O8OuV49p_uGS8vb_jk6hB0l0mhNj7FprXJJ_-H3OECcwSSSYrH77wxxBz1y0F1n3xtxqDptasmban9Zk9C7RdeBkqFI2tFtsh8sBfB0PqHxIqfpFen0a-glCDbo1LGncUD6FuX7037YEx120InlYln5CR_KvuEZXaG_wNfvZ8Wxfv7S7D5tKd0WFoNpz4zgfVU9T35VfENaQSjM0fmZDlL9BYoSvl_pnbsWmEjCRpA12bghddqmyux6d7y8nwqBLfoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=m48x14eNyN6eft4Jv5w0qaIq82daRkkWTBWamo5mU_ndwfGGhF3L_XFjsz7R9SV41C9WmIF3UWiNuTz7T3O8OuV49p_uGS8vb_jk6hB0l0mhNj7FprXJJ_-H3OECcwSSSYrH77wxxBz1y0F1n3xtxqDptasmban9Zk9C7RdeBkqFI2tFtsh8sBfB0PqHxIqfpFen0a-glCDbo1LGncUD6FuX7037YEx120InlYln5CR_KvuEZXaG_wNfvZ8Wxfv7S7D5tKd0WFoNpz4zgfVU9T35VfENaQSjM0fmZDlL9BYoSvl_pnbsWmEjCRpA12bghddqmyux6d7y8nwqBLfoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=eRA24aQpl7KRMlz30GvftpESCM7iaUhMNAlAlnfs5AvhRMyVWaQmNimXZ7isIAwhvkVuXoohpv08NMJ7VzRHl9UAGD9zMB38WF6GegSNfnz1bVJPECysmjWhrdQoehTiktDL93C37ihycchL0gprBUaAgURWuJb1c-AU9gd7XzZ9NFTiFkKMABcHneX5p3CpZQWgBjOLmvskfEzHng06MAp4Mc3ht6oH7xf3eC1-0kiIknVA-bdpH5IDkqKboxcW34hBpgbDYHi1P2R1WmEaW9lVEZeow9rt9t2YRv2-safpenlokyoJlswTX6-ztTWNLWHu0nrtvGULgWat-Cpz0Tt1a0TYyqjFYMmkn5O0NvvOgL9t2b7PfaYm11fFiO-WFViYNUJ3ojemZ9mtD6Zc6vJpMi8I5PfEhEEG1GlA95JrUpzzwp7A-FNhNKTc18emQLkZfbQitTWlO_Fe1LnKpRKrxz7ZWn_OTniGxy-Ly-Fo7ZR0N5praqD62oBdp2YvYeW7MDAZ88LKoWLvilTl1_h37y8-ZcXsNub8zM2n9m_wF6yQ6jIfeOzCtKwfs2xO1KYtx469zxFOt8EmH9qiPhnTBp_PpnPdW1s5yfHeePGrBjpLCBZF4FsqCjUHg7e51-jozNXRrZzut4ks1uP7Wl6p_DwATcp56psSYWul0ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=eRA24aQpl7KRMlz30GvftpESCM7iaUhMNAlAlnfs5AvhRMyVWaQmNimXZ7isIAwhvkVuXoohpv08NMJ7VzRHl9UAGD9zMB38WF6GegSNfnz1bVJPECysmjWhrdQoehTiktDL93C37ihycchL0gprBUaAgURWuJb1c-AU9gd7XzZ9NFTiFkKMABcHneX5p3CpZQWgBjOLmvskfEzHng06MAp4Mc3ht6oH7xf3eC1-0kiIknVA-bdpH5IDkqKboxcW34hBpgbDYHi1P2R1WmEaW9lVEZeow9rt9t2YRv2-safpenlokyoJlswTX6-ztTWNLWHu0nrtvGULgWat-Cpz0Tt1a0TYyqjFYMmkn5O0NvvOgL9t2b7PfaYm11fFiO-WFViYNUJ3ojemZ9mtD6Zc6vJpMi8I5PfEhEEG1GlA95JrUpzzwp7A-FNhNKTc18emQLkZfbQitTWlO_Fe1LnKpRKrxz7ZWn_OTniGxy-Ly-Fo7ZR0N5praqD62oBdp2YvYeW7MDAZ88LKoWLvilTl1_h37y8-ZcXsNub8zM2n9m_wF6yQ6jIfeOzCtKwfs2xO1KYtx469zxFOt8EmH9qiPhnTBp_PpnPdW1s5yfHeePGrBjpLCBZF4FsqCjUHg7e51-jozNXRrZzut4ks1uP7Wl6p_DwATcp56psSYWul0ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=fyVZg6fCfylEnGJ5zEhXRRzsBpAJHR8UIO8sKdKfT0-il1FsZhxbKerYz7-WW6BPT637gWdNMPag7f7mEFDOi6IXxTO-y6I0YvoQ0AYKc7m-qq-vQ-sAI-7VAg0xXMJd-8MQ2-txFKOIEKEyLIm73EPgcGOU1016YPSxAWG_NH7mcd8rwWcoRuKnj1ujuX5VyoZafSZyz491Kl-frezWCxLlGWiSRF8FWapb8tN-pHlGJyvvc98yMrfmMRnvQBB-v9gSlKx1quPCgWScjf2EbTOA2QNUEk5JuDpYH3NbKrZcEh26l1e4s4zeYyCjKB4wI_LVEQYrP8vz2D0MmVoZTq1DqKsX4eg7xLSagI3UlZBDY5dghuQDkJa8-T3sUQDAvauZN5JwWIIsT8x6TWcDmqbYoBkHGNzmXmP7vsfWTY9PfDcQexnBTGbMthvkKbJXyQ7-c3a1_am3uP3ouIlm45v8LUP1bwJlKiH5wIGfV8-7273v0_61w4VI_pfUKp7I8ZoAGbIog4nYOk-vb8vLx160aHa8ZFQHPf_j031DLpPosGts2CmIvylVNKXy7MX60ANWLmAYMKKbtdYpwdr6Jv8mR3s8PjvtROy1czwXgX-YMIM6BbE20TUSVahwTsOY0vdSt7LJG6KN7lJ-r6TMqnjxvnRNFDLdzkJX-RLS13Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=fyVZg6fCfylEnGJ5zEhXRRzsBpAJHR8UIO8sKdKfT0-il1FsZhxbKerYz7-WW6BPT637gWdNMPag7f7mEFDOi6IXxTO-y6I0YvoQ0AYKc7m-qq-vQ-sAI-7VAg0xXMJd-8MQ2-txFKOIEKEyLIm73EPgcGOU1016YPSxAWG_NH7mcd8rwWcoRuKnj1ujuX5VyoZafSZyz491Kl-frezWCxLlGWiSRF8FWapb8tN-pHlGJyvvc98yMrfmMRnvQBB-v9gSlKx1quPCgWScjf2EbTOA2QNUEk5JuDpYH3NbKrZcEh26l1e4s4zeYyCjKB4wI_LVEQYrP8vz2D0MmVoZTq1DqKsX4eg7xLSagI3UlZBDY5dghuQDkJa8-T3sUQDAvauZN5JwWIIsT8x6TWcDmqbYoBkHGNzmXmP7vsfWTY9PfDcQexnBTGbMthvkKbJXyQ7-c3a1_am3uP3ouIlm45v8LUP1bwJlKiH5wIGfV8-7273v0_61w4VI_pfUKp7I8ZoAGbIog4nYOk-vb8vLx160aHa8ZFQHPf_j031DLpPosGts2CmIvylVNKXy7MX60ANWLmAYMKKbtdYpwdr6Jv8mR3s8PjvtROy1czwXgX-YMIM6BbE20TUSVahwTsOY0vdSt7LJG6KN7lJ-r6TMqnjxvnRNFDLdzkJX-RLS13Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=gppdbsvNA7Uu3dJV0TvAdpYK4pR_O3nXSjbE_ILd55h209vojUeSb3CjpmTX761GBWoz3eFIteEPXcJKoqUKIgtbU9h84P-uJMUijf1Dx8YIfy-GoeaG-SS8Kvo4rXA7bfdsKZnd0pk3xvLeBqAl468oA1Yh5jYKFrov5_BruGivxyORSz1k_q1-DUdrxZhogxeQVe6ck6lNzY49jDyZT-OAkEsLrgBElxed7tfS8gcclKTX98K6iLJuDWzD6uBcLr26Ems6mlM96u_tC7wPTUxonhpDy5XzUNgE0rIAiUr0bXTCIGUllb61SeTBBNWjPw5xa-UPvoL3-mO1bYS9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=gppdbsvNA7Uu3dJV0TvAdpYK4pR_O3nXSjbE_ILd55h209vojUeSb3CjpmTX761GBWoz3eFIteEPXcJKoqUKIgtbU9h84P-uJMUijf1Dx8YIfy-GoeaG-SS8Kvo4rXA7bfdsKZnd0pk3xvLeBqAl468oA1Yh5jYKFrov5_BruGivxyORSz1k_q1-DUdrxZhogxeQVe6ck6lNzY49jDyZT-OAkEsLrgBElxed7tfS8gcclKTX98K6iLJuDWzD6uBcLr26Ems6mlM96u_tC7wPTUxonhpDy5XzUNgE0rIAiUr0bXTCIGUllb61SeTBBNWjPw5xa-UPvoL3-mO1bYS9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjvznrDbr_0qu63sjCFNWwivJwq_PsXH051XkeZxokA6TxDGWeXbWw0mu3-FmdPjsXmqxN6w-ccm8JVHXsVP9fYVHWa-83dwdAH6MuIGctttUNPHSefQhcVxwajrevYhxNvO1_W9jEmjDjhN9bh0psMIA5wTQVdIHeoOWdfVL1ztBQKZ4EtjGQvHu8U70KSxwYnZxaaShPXfHfLk753KWu14fazBrzSBb1A-yI62zHiaY8RGLoNryRo4I9X6Tf1jHGYg1K71g84k_Jz0v8E3u5UZJOV9J7bP1Lqb3dTCG5kMJ2s8SHxPqOUypqVjv4DEGim3t_YcyD3jAnE-B883Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Fvu6lzseQ9JMh26uhMxgFpncMF3lGb-_MAV-_8jDmvt54k8eZoKQzGTlJZEb7JdgENGxJAHjunHy3XYBIzh2wmzMhK_vYVUlCUMjhMDYcabX9mBXBYFOOYpceTFx0M5clDQcNQxxJhiDMILPOC97U1tA3uwKob3ZrjRHTL-Y5lcQA-I_LjupMAwfwAYTBE5V4qbLcSDQTHchQ0dWFo9evXVt3wlnAThgI3kcKCpwzCbARnvVhBY4SwSleJA2RYlECMoh7QHo2gm_-3u1DhKv1HQN9ruEIQaPgGKXuGazqmxxsF2uk_v34B0WhlgaGRQflo6PYPRyDZOBqlT5qggVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Fvu6lzseQ9JMh26uhMxgFpncMF3lGb-_MAV-_8jDmvt54k8eZoKQzGTlJZEb7JdgENGxJAHjunHy3XYBIzh2wmzMhK_vYVUlCUMjhMDYcabX9mBXBYFOOYpceTFx0M5clDQcNQxxJhiDMILPOC97U1tA3uwKob3ZrjRHTL-Y5lcQA-I_LjupMAwfwAYTBE5V4qbLcSDQTHchQ0dWFo9evXVt3wlnAThgI3kcKCpwzCbARnvVhBY4SwSleJA2RYlECMoh7QHo2gm_-3u1DhKv1HQN9ruEIQaPgGKXuGazqmxxsF2uk_v34B0WhlgaGRQflo6PYPRyDZOBqlT5qggVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=n-JCJs3vUKJs8tnZ1K_sduK-eqtmIt25Gu5kOCXxbR_Ckp3HCAL8pkL-CH1ptcuZ0fvoVDvwuVdr1OioB-FRiea18baKV-cQVamffN6SG5lYtXGxad_JcfOrYyYanWQUhIidDssytGvT5ldmpZSOxr4OrGSL5K22oDF9kzll7hP4rBqfmVjAiY14MdbeQJB2yqYMVPNpU3TrTYPVGp3mYTQM_7emxsj-XN4rgJDoHDgigDG0tOpOP0OKWleDYAKx_AeEMMwBVhz3_5AmKj7eqRaPmUQJolioHkz8tNpl4fYRHbBksDi-9eUvojugJDSUoXGkL_30To9An3TjGrgDnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=n-JCJs3vUKJs8tnZ1K_sduK-eqtmIt25Gu5kOCXxbR_Ckp3HCAL8pkL-CH1ptcuZ0fvoVDvwuVdr1OioB-FRiea18baKV-cQVamffN6SG5lYtXGxad_JcfOrYyYanWQUhIidDssytGvT5ldmpZSOxr4OrGSL5K22oDF9kzll7hP4rBqfmVjAiY14MdbeQJB2yqYMVPNpU3TrTYPVGp3mYTQM_7emxsj-XN4rgJDoHDgigDG0tOpOP0OKWleDYAKx_AeEMMwBVhz3_5AmKj7eqRaPmUQJolioHkz8tNpl4fYRHbBksDi-9eUvojugJDSUoXGkL_30To9An3TjGrgDnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frAsZf9Le9dGRNVCeVNSkT75rG5ZxJFHL3MvnRPqWLsoQHTNGRXhLDsjmbxRLdfgeMD_RFd70uaUpUF82mSnOZJIFAQEMIxlxo7pBQG5MNGTDYnW3E214BF3vsPm91mC7VLwKOQaDgpNa59dOWPP-15tPqpUO4Cu1wYc6Fqm_vN_Ury7zUiNH1DH-3plagrwsRergk0t59-wAcXGgd63413pHnmV93VahxzDFQadgJTJhFVq83nBc4zowyKlHtPVYqReN9V32LilQTZb7VbpxQ6UEGpgIns9CiQS5P1Ni-jkel0yaCnHSLV4Ri74qRyFW_tTJ6JgXS25kpbUolqp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIkuqj4qmMP8xdAdHuFu1piVfj6RDKsPRcDFbeBsNZzbinS99u5ZA1-ntVYksIA6g47ZTfpX99CSob92s_mdOGSY4psMUHvGlEhiI5Q6Fhvl4PsqrR0jx9rhxiNpRvL93BsFsAjvydX9AeDGOYDemgPlWrhYDpcvL0V_cgvjGNixKIz6PO1pdEX7sJ-RqvDztFt0aBVX--5EfIktRzLQsIZzKCrEJW_6SdoSQVDluDSmtNhhSgaW9_gFSBoGmDgzzAJcrUzsCY-hI9TT0-AuHsJGKrfyAY3KmP9Gv8btHw2e_pcvgDvbFgiGyjaNBXBV711opnFYhcVwVWlN5Yio0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrdBUeaDddHo_dsvQxT96Mf3Znva6tevqdQpnG44gRGQnMlJi6qGeQyYOyNfJa9dBH4XjmFYxFEERmevoUm8O73nTRvAs7ITWecC40nTnoPrNklXQIgnjoZJ1uFMZAhbee0MMovf9Rt15usPfF9BKnuP_Wp9dOuutcMtJUm5agmGi_OiqVPK2WmUM3gxEPCIZlkclbEzlB-fGsBCkT5hNkrgLU146ucPG5rX5VefEmfq0dzlxa1_BSQVxFnBZLxVbjgZWWzfrbLxHojYT9Gso2s_GrDggwA9QniylvetzybHUsZVuNS0qSR0PQSjQjALCURbbVUbBtDuwoS5IKgMbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioJsoUwzr3IdrI34FgjMrF9R0IgyNogNnqLl8liZsaPvSivNfA4m4VqWzpc8qJmNUHD6i0UFCdlG2rJFUwLvSkPiKFJ-PKihwLl7itr_JYck0Z9S-x7mB8l_u112Y4ITO-iIWi84tHAF5Q1x2fil0ALFVDVi42lMZD6bv68HP0VSXD-mynZ73xzOYToXwbcBS3ctKs7l3cZvUeckgLFJlULYzybmPVP6R_thlWSP35dS7ngRfKyjRLPBRcblyY1rjAzY6fZLWsZP1pUxpHbP65F5K8926GT7NBAyIe0MrFDD5DqbalSegexC8ftkMnDOUQmAm3qMU6_l2319mSVmqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8_La4SOISeQ8QHqPntYthdKzOfe5prOxL_vGhb3CPcP3f6FMK7VaKo2UbwKYrhBEYN7t7ReKT5VIZV43mLywDIqSJwIKEDdhjMZ7cC1v86lGzzfEhprET7nbYO4so4tDiiZIIBGg3UZycJ-m7JXqHL0EUKp6iVmiDQZOGLomqXXi2r37bjw12yZPpKNGFXorjkwOjrbveGqfbxAvQkI4V1dBdTQvuezwLDj9gFve6rHvFOc-zTVicJV7QuoCcZpL2KsUbTeE_U-DUQ7fpi8iOayoh0vJO-_ssVQB-uPq36FL_KsOfnOFiYy8i0P7x6VjKEJCZQcWv4L4_6aL5N-xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGRDiN-GMxyuLJvfrvhwTcSNH6KlbUxEgYXihsDG4wQWaux5GI7B0gG5osCdt4cYpvK9GPWiXiKa2kO28rX7pOnpUeYfCVSIvj6M1KgePPPy8boG76LPwtGC9zOIMi4gd78iD3fLb8FEuP3yTSR6UnrSKSDMgyhHoGMQ9ZxRkCxtwZ7GSsTJZ9D6LuC5AR4mPudjO1W-UxYF-SXawx06Xu3xkg73Hs2ZRNYUrtUtYwtuZorAWgj_ySbff1ylytKppqTXXvEMEdz3g80JryQOEDKEoh73VVgR2nPtyV6d7SRmwUM3aqiJhMULv9-a0pcIjJKVKg5O1nE4HuJ7ozfYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ6YaNPZjlXuyPGSX12iG3VKe7GvGI9eikODNcTP3aOGbuklkZFi0x3UGKgraptv0AY_GUC4TOOTNO-8jSSvZ3ECcx1b8vbc2G9xKP09nL1oYFeO6hiRJ0zYRFNbYuHq1M1wve9f5YEuklhZZCPlGTY6thHM1Y7_ZSjyZB4x9pIRrqbwe7XphJSqNEyDS_2iN0oSR0AZyq_J0Jy51GmEdJTTtw9DnXzEejo1GRg_5Ck9Oo0vJNBs44I6rXuwrYCwLAtTegpMLNqsE2a3jJFuto9jqjGRMkUzwLNB0ia1JlCGoYyir1MJpcSL-Zu_wD8MsUWoPLj9zdH7LBVIfBIWEg.jpg" alt="photo" loading="lazy"/></div>
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
