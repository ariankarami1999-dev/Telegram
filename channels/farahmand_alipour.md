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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDkJ5C5C5ybZ0LxvQH15TP0XsJ7PlFO68O2dXvi-b7TAN2aRPI0PUrPQ60bALacq5Kea5LMA4-EzpiGdLT8pJZavGOoasd4GUuSoWmsS48Y2L1SfAxm8r2u37SQg6VRFcReivbPZJIxqvLx7Rr53BFsbhRWKf9L27XjSKozZkfjowmAf0irwYIPd8_kJFJTnw0JM-BPFSFVqSkkn3fFGAj-_dzfoj8ijH_JFnMhvYVq2LB0Y23KkeYE_cjgfra7zKfIVfHbgsOmiV4AY-qTWFaX2QFNd0UqzOkT83Mf7y5fF-wwPGqHv8-GdUqyOPbioJhYXU5xu928RAz7BiEiO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcu8bFEAr5fJqC1-vXwVdBotP9ZK6_01Aw61sODGzzCEwyNeQwjRcwFCw6OMcMI4tpmVQsml-ui3XCm38X_KgyW7AKp73Lg-dik25Miqh6TSycO02jkjGbRLDsiNxHgWslvF78WQIBRHDDqddBPEoKxrk5zWQufTOIgB9bInj9BsdNaZyM8O3dBI-fCYo2gqUD-jRhWo0fSayMv146X6A7frgZ_oSZGeC_Kwr0Erj6vje7oz5TBb-WgRRl-PNfaFEjAg7QqVZAhSkwUs2DHu5sjpg1fREI-VWxTxx8VkAYokS_QTuoyzWrf_mHFml5IFiIrlqdaHX8bRVq4TuLRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ho7hnYm6kDVplrqEp7oPygSWhfb6kHqEVS5omqQCg5pwQv2J2MUJ9cJ_zjJPI50cwvpm9dLdwVxglFxBXNR2b7wJZwWvBGDlxj0Lc7Bz683wCAeGNY92U87ORooK-A6GKUMv0Bkex09fV4BD-WFGSyy1YawwiJ-q6TCtcTjxWr_CUInacuH_pPvaNTC3RKXpry6Cq1cYrBR4gLBySm5iLZaO5ODihnvIlBI3Sn5cP61BvrAnY0kydGi8vavdBK9pnw0_TVxWT6c4qWr9CTb9_RdPdeEgYBvZhhpzhFQQKh8YJQ3wmzXOVvBofwcRxg57b-BUz9r8E1EitB0LdivmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ho7hnYm6kDVplrqEp7oPygSWhfb6kHqEVS5omqQCg5pwQv2J2MUJ9cJ_zjJPI50cwvpm9dLdwVxglFxBXNR2b7wJZwWvBGDlxj0Lc7Bz683wCAeGNY92U87ORooK-A6GKUMv0Bkex09fV4BD-WFGSyy1YawwiJ-q6TCtcTjxWr_CUInacuH_pPvaNTC3RKXpry6Cq1cYrBR4gLBySm5iLZaO5ODihnvIlBI3Sn5cP61BvrAnY0kydGi8vavdBK9pnw0_TVxWT6c4qWr9CTb9_RdPdeEgYBvZhhpzhFQQKh8YJQ3wmzXOVvBofwcRxg57b-BUz9r8E1EitB0LdivmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5l21qnWUuE0ubqbRoE9QWPC3YWMesYusFHAB1JZltgZK61tZsweRAQLzi9Ve6Yg-yTBCIL97xDRZA8Zs2dX3B-rEECDcC87AfpVcSKmqZB_ZhFh6TGa5ntu7NGPmAjT5quNWiXVbTm7o78ybOMN3JHFPoTxmuqV3aP9SUWmNRxbVmuglAof4BeLyzjoqKPz82BJ8ecvak3Gl5GGOyEpSW9PxI9oePJCgoogNNuFDaNoTMPF0Yivpnyyi9QQi4YusxsF12S48y1HwGWbMXKqaf_TL3FoBoQkicH_4evOHTfGm8mrvXNIzDvi3ZOZ-ORLraT3B-95CSXaFMayRlsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OZeTQ4LOwbuesbjhxFDQopgJERPYlrlfWVf8PYN42erbQAhdPNIUcP3Mvp_V--2XftjxBcWbABsTXxyNtak8aT9ZKye__-sq1c6Q5Oy2Pbv3MmZoVOpvwb9qa_dfb3PD7Us2qZqGta4HEyG6NrY-ILEDvDkY9VBqV_68rM6HIu-AcffH0aPOVr9HzPDrikqOO2QjOJjOFAh_y_q7fD2Ho_1pOCHNjvc_LMVuTZ2c6pVsHgg3nf-YYEBaMjV91ZiptN6vRmceIx7NGG9smWdhRdA0uzn3Ilp9CuXaxtUX9son8yi5GEgCvv-QIZzF3YqVIjTRxwfNH3S9NXghnXE7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OZeTQ4LOwbuesbjhxFDQopgJERPYlrlfWVf8PYN42erbQAhdPNIUcP3Mvp_V--2XftjxBcWbABsTXxyNtak8aT9ZKye__-sq1c6Q5Oy2Pbv3MmZoVOpvwb9qa_dfb3PD7Us2qZqGta4HEyG6NrY-ILEDvDkY9VBqV_68rM6HIu-AcffH0aPOVr9HzPDrikqOO2QjOJjOFAh_y_q7fD2Ho_1pOCHNjvc_LMVuTZ2c6pVsHgg3nf-YYEBaMjV91ZiptN6vRmceIx7NGG9smWdhRdA0uzn3Ilp9CuXaxtUX9son8yi5GEgCvv-QIZzF3YqVIjTRxwfNH3S9NXghnXE7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ323fh_ZI4goosekrbUeky_cTExGCNCfpicV5PFuNxmipKcPA3EFwOyyFfGIxEJspPlMmvmU-Jwl9Ac3Trst-ALK2AuSOW5svsZfq0u8Mj4Ejl69gUeThPdA2i9wvYiyq-qTqWQ18ePS2WJIEwDID2hzNkX92k1o-M1v7V_yDBkBpTvBozoe_GgjLe4pMTBf-wB1-AmqFBl0T8oTQDVMtt_WiVFHahQd2WRMxHo1Utv5ugLyEpt004AEu6xfsvmPTxBkPBF2eSfcadSik-NI_wRdJOwdGjsGl7fdqyBt5CmQLjbl3oeM6Cix9VFEln1zx2gmTWrrMXGZIV45AWlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzo4gQ2mGFpUAU_4EvPYtGzt22gwRpEX0g5bz2SuwNrg-xdpfRrO-SwmsXP_AKOtEFFDWZWt9vxz3U99Ikm40dE0dgtUG-8V8i2aabpWaG9HrpKTfmEOqVO2R2oPmYU7v4pF5t22G0Cd0mqMC5hYX79m0llFdUhnAUaxfgOfRpbLoLy74v5ISTWS3gEYMjarPrIa3jGV7SDgMeak3lXgyuhG0tI81VAwnPb4vT8RHVwHhvAZHVE3N09b35oJI6YPdwOx4HM--9p-oZr__d45GKeChEyjr3uvOX7zah0Gd0Ec3i7jd_KPHjZ7VOC3ojTGuxDoQz8zBGOoZhDGs-Miaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tYX7135SX5apgVzT1E4PWr6bs5uDo5hYCZ1uTAk-3hYWPIof40H2pd-0aAXhLQVSAFdKREj_ktR1ZiIHRPltikeJTvu6MD9LXFVPo1a0KfVJIQfeSPKys0DdAGiOab1UFCSUW_wn0odnjsLhfSMrmGjvXOh9w5aTLb9eDnF07wTCpjmIELkxJRCC_0LY13QOLbDqW9NSp2TnMq9W_h3MhjbZXDCjyA1NKLWkneA3txTt-HT_lj3F1il5GnCXGV3FNkusIWw9AEUcIAMlzyxzHqAuo51c_0jq56-zH9UgjdcUSX7EWz4ZM34tg5pc_6B_XGoSvNbXcvIvCt-gCJ965JoayHK51wrJViBVHLyFT0LprJPwxGAyBwAavfsA_5qRpVYQvJI66k2sajApz8EUu7X6XwxwqpP9YE3TIMzzksLZuYWpKBDU_nRwtPj1j8Xv6cmKpXtb4ExLzj84RKsLh7ET8q5G7NQKoFxFW52kEl7JmwtsFK3nFnjmB_e88OlpgpcgjozZ2fswj02TRM5sR1U5B5aRwA0Pxc_il186HzeyjMTCUt8urQcqXDZ0RFQSQvPaZhh3Q5N1kxVybaRUOLKiJ5TKdzjlykwlDr6uWoIw-VpRcfjGjDDFx26mdsohBWBWLgVFpq7xVGXOTkaVtFx9FRnnAmT4-3P1sr6zkr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tYX7135SX5apgVzT1E4PWr6bs5uDo5hYCZ1uTAk-3hYWPIof40H2pd-0aAXhLQVSAFdKREj_ktR1ZiIHRPltikeJTvu6MD9LXFVPo1a0KfVJIQfeSPKys0DdAGiOab1UFCSUW_wn0odnjsLhfSMrmGjvXOh9w5aTLb9eDnF07wTCpjmIELkxJRCC_0LY13QOLbDqW9NSp2TnMq9W_h3MhjbZXDCjyA1NKLWkneA3txTt-HT_lj3F1il5GnCXGV3FNkusIWw9AEUcIAMlzyxzHqAuo51c_0jq56-zH9UgjdcUSX7EWz4ZM34tg5pc_6B_XGoSvNbXcvIvCt-gCJ965JoayHK51wrJViBVHLyFT0LprJPwxGAyBwAavfsA_5qRpVYQvJI66k2sajApz8EUu7X6XwxwqpP9YE3TIMzzksLZuYWpKBDU_nRwtPj1j8Xv6cmKpXtb4ExLzj84RKsLh7ET8q5G7NQKoFxFW52kEl7JmwtsFK3nFnjmB_e88OlpgpcgjozZ2fswj02TRM5sR1U5B5aRwA0Pxc_il186HzeyjMTCUt8urQcqXDZ0RFQSQvPaZhh3Q5N1kxVybaRUOLKiJ5TKdzjlykwlDr6uWoIw-VpRcfjGjDDFx26mdsohBWBWLgVFpq7xVGXOTkaVtFx9FRnnAmT4-3P1sr6zkr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r84fnfGD3w7SypFeQRutIuRQETNMjatl43OKsKUsla9jXZXLPNJpznxv1KQr8pnLn6zPQGKyJ2TP2hf0HbsWkJiIMJIC0H7RfOo-xTBpmTFhPbiEEx0oxSP-DijgUcZ0kppL1ByOOJ-GVUet5KELHQhMvBrR_aMGxPKU0y6tICy8OtnSoiI3K3L_AX2IfyAYHHJPMA2ipC0SuK2IrP4ccuS7lQxHfcIpYEYZRLFCFylrEasTwloq-MthqkG0cVXoE4wbwRhJeAe3fDcnICJpzIqrTrPJIHXanz83djYoQGWCDBdEvunEFY6Nefp4-KD2bqNP9Lz3i31W7Sm6PqyFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSQCxqMjY2v41OcrWsNunGe38UdtxzFGgF3rjyB70Q16QdZVOoJYnEXiXd_tYxwNhT6Rl4wodZuPBq9uypRsj5OKj3_LFbvhif56OSIhDCEjgRj_wlpe6ycDmLg620zWhof_tgbI2y0pFutOHWdOHs03dDJnNEGGEvOzqsM8lD8KIqw-zxtEPl6UYAtp2ix4NmSqPBnp_nIAV4-4zdTLabnDj2tWhtPNBEzFnqHFjlhjwVfLcFpYB5_nFFM01uCHfnSCfrDEY45hVLR5qvQuzUqvwQHSySepmUu8EQKyl8YXkaAdHKM4vDEaWRxOug4X82iic2NMN1Du6Iwnzdiaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=SdviTa_5weCtbndInr4W9jGe5_ZCQMoJi128yZFRIdZMb9rJW3k83WggLMNoitC-2_4HJAdP7dzKN_xppyzbNPCJxaJolpddck30zG-krpMmq7J65LpTvea517r33kOfrhH19c8P3WMcqyywW8e-j4kGNnk1qRPrywh0FQLgjyq66sD3-E8Bfe2kc_Dx50PDHfnkhWiO8SbE0GkATRvJzFFaUuxV6q12c8OhJx1qUWuufkRWtqnA4eiK8HYkZOzHARLLkNfDQbEU1qFGoP9VcfjeBYUdPiT3xhHwR6Gx7e1xKE_vTEniGiQFJUbsnOmqyPO5bK4XGBmAj5YwQBZsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=SdviTa_5weCtbndInr4W9jGe5_ZCQMoJi128yZFRIdZMb9rJW3k83WggLMNoitC-2_4HJAdP7dzKN_xppyzbNPCJxaJolpddck30zG-krpMmq7J65LpTvea517r33kOfrhH19c8P3WMcqyywW8e-j4kGNnk1qRPrywh0FQLgjyq66sD3-E8Bfe2kc_Dx50PDHfnkhWiO8SbE0GkATRvJzFFaUuxV6q12c8OhJx1qUWuufkRWtqnA4eiK8HYkZOzHARLLkNfDQbEU1qFGoP9VcfjeBYUdPiT3xhHwR6Gx7e1xKE_vTEniGiQFJUbsnOmqyPO5bK4XGBmAj5YwQBZsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UqH59SrVvY_3i0bYUy_0hHACZVBNFglZmdE6gVmkvJ-HC6oB8oKJbjuE77W3MGvgtDpaKR0cVyOLR83v4Yyutyb2dBfs8BywXblgpvMrootWIa1X5QMCcxQcmFNIMFFp78clTOUEkON8g7sAQvcaJoofPrpgydEfU5zpT0SQn_glTLZvN9Hws1_4Ko89dgovXZ-RE1lrHxOHUWepMbhmUZSC5dcttKeW9bnGQWJyprQ6GW2Ttw2NDaAKvCyO2foqgPOpe590SujqYD1xnQz0jU5QbhNX9LZYEN6Tv769ifzqJCStfSKTXfqcEY7qwT2IKtYvqnPfm1FJy56Kvpf5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UqH59SrVvY_3i0bYUy_0hHACZVBNFglZmdE6gVmkvJ-HC6oB8oKJbjuE77W3MGvgtDpaKR0cVyOLR83v4Yyutyb2dBfs8BywXblgpvMrootWIa1X5QMCcxQcmFNIMFFp78clTOUEkON8g7sAQvcaJoofPrpgydEfU5zpT0SQn_glTLZvN9Hws1_4Ko89dgovXZ-RE1lrHxOHUWepMbhmUZSC5dcttKeW9bnGQWJyprQ6GW2Ttw2NDaAKvCyO2foqgPOpe590SujqYD1xnQz0jU5QbhNX9LZYEN6Tv769ifzqJCStfSKTXfqcEY7qwT2IKtYvqnPfm1FJy56Kvpf5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=jTzRbFxkju358NfjVT1A3qhlIWBCYEeSgNV4Drayu7r6xXE9-p7H8B8ywaJt16ONLM9Su9ymg3GkLe_MlON1rITAzMttf3NY5-vLl6qz5FSlC3Nl8pYRG7Ofe8jU_0YMgh8S-OEwovtADJ_KByjWBxdRFAlrcIhm1c0nXL9vK6yUB93dHdmaUj5MAaUso4-CWgiAGcs1p4CEZdPXng6u_M8hksC1kzL9248ZUuhgthG_yVUu1zsloQRDAZ7_qKGQEsfmRsRlJ6FOKTbJyCLk_tw058PgVJEFHS4GVLR59x37SRHkNL3bds3OJLYHJ2YdW1AFEvjt_IuTgc6H7yy6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=jTzRbFxkju358NfjVT1A3qhlIWBCYEeSgNV4Drayu7r6xXE9-p7H8B8ywaJt16ONLM9Su9ymg3GkLe_MlON1rITAzMttf3NY5-vLl6qz5FSlC3Nl8pYRG7Ofe8jU_0YMgh8S-OEwovtADJ_KByjWBxdRFAlrcIhm1c0nXL9vK6yUB93dHdmaUj5MAaUso4-CWgiAGcs1p4CEZdPXng6u_M8hksC1kzL9248ZUuhgthG_yVUu1zsloQRDAZ7_qKGQEsfmRsRlJ6FOKTbJyCLk_tw058PgVJEFHS4GVLR59x37SRHkNL3bds3OJLYHJ2YdW1AFEvjt_IuTgc6H7yy6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6jIllHrAKjQqKP-QG9WM6_0Wr3ecW4oFEv7gFXGdoRd7wYaykhoJRTE5dP32o4CI4sq-EH4io5Fnw7c5sW82tTBY12pFBPFXlbmbR-aUSWE6CqgDvxcAW2Cck6YUs4Jxxgd1ZHqLx1Yz42KhuH8nRh21YZv620AHlrBEru3c_mWb381wUb3ET0zo43UaRbiJuonP2kElCPDtnNOOHWHU8QBpSVx2p64hoISGJhF8PDYmej28vDxTp_HP4if3Qp3tvIDcGC-AsSHC7mB1V4BZireeCUiPGYUqxJbqcbVKdhmDeT8E9LG9gSn6OsSHf9GAOz--aj0QiVCktQBmiVlNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBrozB4MR8GQXrLHP5UqKIevuPVwUMqHzzh5o2dAvIC4sho8rms3VmrX7kX1Gvy44Z8Dqq_I7mVJAyCAQEvJ59iKrGeZ_6xWWnsf2SCBKIGqVgJealOTeEkPG6xvK87Yy8v1f99CH4lHkWj1m_eADovNNAWfkdlZ5B6yfY-mDpbks6fxE0eO1OHIF1peMiI9-APnkH2btQquLGmGqCKu8E1KPpSVE42oS-WkyyHihSPe5zN58C8NLPRXcKga9H7cGkNIfGDcHS6fKG66xnr_2krJCgbO_J7g1LBOu_kP-JCWsm68HqufHKDPzPM2VetPQVZG5KYYZj2TmE98NqQA5f6BaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBrozB4MR8GQXrLHP5UqKIevuPVwUMqHzzh5o2dAvIC4sho8rms3VmrX7kX1Gvy44Z8Dqq_I7mVJAyCAQEvJ59iKrGeZ_6xWWnsf2SCBKIGqVgJealOTeEkPG6xvK87Yy8v1f99CH4lHkWj1m_eADovNNAWfkdlZ5B6yfY-mDpbks6fxE0eO1OHIF1peMiI9-APnkH2btQquLGmGqCKu8E1KPpSVE42oS-WkyyHihSPe5zN58C8NLPRXcKga9H7cGkNIfGDcHS6fKG66xnr_2krJCgbO_J7g1LBOu_kP-JCWsm68HqufHKDPzPM2VetPQVZG5KYYZj2TmE98NqQA5f6BaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ZVaKgMRJOMxXUq-tL8M25LVJPot2uujwOVSG9fGiTAKcbQUrfXtimpZ-p-3Lb73RRnjccQh2eeKeRBV_V1gp5PZ-XS_NKOTivP7ZjbiHif_O1Esn_dYH5Yznrye5s2pA9mme93grIAgvXZct87r8wI0znaAtZrySBqC2bVngMW7GGNa2xo5MVsUnnsB1YDvYpuaFqkvtGKWz34kExtRaAuUKd6HMTgTjYBURouRGb9xhlo0j4AulnmRwVXBZvJOLcIrdjKw0_ZAwcIl32F_XzbpEB8lynFLsy44TvQNXnkwVXEobdqQvgVP68W2dLxaQuWkbyjeiKQJ4Q4aEWwyRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ZVaKgMRJOMxXUq-tL8M25LVJPot2uujwOVSG9fGiTAKcbQUrfXtimpZ-p-3Lb73RRnjccQh2eeKeRBV_V1gp5PZ-XS_NKOTivP7ZjbiHif_O1Esn_dYH5Yznrye5s2pA9mme93grIAgvXZct87r8wI0znaAtZrySBqC2bVngMW7GGNa2xo5MVsUnnsB1YDvYpuaFqkvtGKWz34kExtRaAuUKd6HMTgTjYBURouRGb9xhlo0j4AulnmRwVXBZvJOLcIrdjKw0_ZAwcIl32F_XzbpEB8lynFLsy44TvQNXnkwVXEobdqQvgVP68W2dLxaQuWkbyjeiKQJ4Q4aEWwyRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqLQ6jxuQaUk3qT3cHpvTcQVuFKAH19Nl-SwY9u8lbo8tf4UCovxCNi36ZfZeVZ2W0v6vkFD_RvE7S4HmYOnFFrAn1fKsP24E8Jzs-nGk_bBA7owTylaqbM0wo0hT6ZjVdMf0-SrZVZ0LYfuuWzhBiLJ-Y98EKTmrRi0jBMVEJMtr2fGpzYpVCzmW6-DR2P9ZzJ6wPTvO5LHDuqg2prKRQsgP7am6OF_KbJk38rK0hMJQT-NlQbaNKhhZGCMZXVYqEc1XXauoNFOE1gLz7EQOO7iwsmSjZ7j0_d4NBare0oI5_LLH35FEOUnKgoms1VuDU-vJTo-43xUYs9bz7JV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=llAueiX6CmC_hNy8N6_wjLm0hq6xY-cblRc89kODgQeZHs6lGBT9wilRNDoXO9u3nIx5T-U6F7WEjvyjB_kXiWh_Ry5YXwFDN4tFwWU3QMsRXGLaI6hG9HQgnwzD9W7_EuzuByDyNymW_f9eHs7D0OajX0WTw0e21E4uTmp_9fYmuwvCh_5oQAoK0obu2qwFFPFJJ-7ClG6vRPOMJIWZ2g94zbCYoL3ZnQ8zWjXpytDYD60WzQmTsbJ8dfoHqDCFY_-z8t4cWF-6q-Gr3uAAeF-Jx4AZhoNDuWTyPDPe3m-tG3YEFGeo2vLh7hjg-SNPs8M7HfcDw2eJqCFkBH7Ja0itbI-VelLsbrVjLT9BEuV75UrlNiOt4q96KZFIdObHTEtKX7QXECbIL1Z2P4mEYKNldbIxYwcfMNNBX9DgYi7XHZQKukjV4VS8CPasoCaHIxSNCfTjTduIKxfeRErtdHy6kfKs2QABoK4wBbMlzcGTCyWWrlNSowDS9UZh0RjVD2qw4yyjkFzih5-zUceJFHOvvT-cgZE8iWCGxdVjmozK_fYywrPBk2QXdr4egEUA_qu3Fr3g2jwmPr2jn3Qk910fihNptOsbKk8zUBJaIA65p-ZLp4pK5OTQOVqkf7uxLKb8sLe5-am9iwyrw0DIlStRS6t9mzcqN8B9f4CkVm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=llAueiX6CmC_hNy8N6_wjLm0hq6xY-cblRc89kODgQeZHs6lGBT9wilRNDoXO9u3nIx5T-U6F7WEjvyjB_kXiWh_Ry5YXwFDN4tFwWU3QMsRXGLaI6hG9HQgnwzD9W7_EuzuByDyNymW_f9eHs7D0OajX0WTw0e21E4uTmp_9fYmuwvCh_5oQAoK0obu2qwFFPFJJ-7ClG6vRPOMJIWZ2g94zbCYoL3ZnQ8zWjXpytDYD60WzQmTsbJ8dfoHqDCFY_-z8t4cWF-6q-Gr3uAAeF-Jx4AZhoNDuWTyPDPe3m-tG3YEFGeo2vLh7hjg-SNPs8M7HfcDw2eJqCFkBH7Ja0itbI-VelLsbrVjLT9BEuV75UrlNiOt4q96KZFIdObHTEtKX7QXECbIL1Z2P4mEYKNldbIxYwcfMNNBX9DgYi7XHZQKukjV4VS8CPasoCaHIxSNCfTjTduIKxfeRErtdHy6kfKs2QABoK4wBbMlzcGTCyWWrlNSowDS9UZh0RjVD2qw4yyjkFzih5-zUceJFHOvvT-cgZE8iWCGxdVjmozK_fYywrPBk2QXdr4egEUA_qu3Fr3g2jwmPr2jn3Qk910fihNptOsbKk8zUBJaIA65p-ZLp4pK5OTQOVqkf7uxLKb8sLe5-am9iwyrw0DIlStRS6t9mzcqN8B9f4CkVm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjDpalD5Yn6DK5ItH5eZicDACbYkzAKmTHxYYKowlONM-ls6aisEuhAiGGkY8vSbRNMBiN0CLxof289gsAVbRChdkgqrVWNQ85SvpbXjSyco-LRSAk2du2eV7r1YCLy74I2ZGReFHQZLjsrYdoihEUhxRmy26sH4se-6ihqtTmUBi7Ne1lr9PESfa_BYQyOYwQyeghzQZUU_wMqI39oyYprqPueB95u4aDWBOUZPy9ZbxD3NCtx6IK0tgnhtOSqBue97Nm2ujpWTu9Nxxngiz8nd4j11Wm4leRCzBD3kKB-2GouQLGws2vCNZCTJXWUFeIxsBuawtiSy5J2fIQ0VRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=FBeyCLzIPH6tRfY916ZOe81eQnj8qaVnyaBHh13lYBh4Yhuz4Nu3YLgGZBGPc9QXgZy_oKWOj7bbks06zJykm4-sABwLY97OjXcBlk09_5XINw-ielxXpHE3CIHJXLsX9ntZ8qwtKpQYYQBKORrqfH9_WY2wNzjd1IywjrBOUZfmU6yXjZuCz_f8thXzzF9tE4HY65DKyvBgvLGtFM7QOM7cvHq2UWoYDoUkOOgrwrvrG7gGVptbWg3lR2wsk4QNsS09kp-n7zrrAjg7TfiGr24JEnaaKLFVTy-zPTBRYdFaSQ5TzQlMFbv8sMA32q2ZqRTCcsyr0l1xQD-rXO6Bqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=FBeyCLzIPH6tRfY916ZOe81eQnj8qaVnyaBHh13lYBh4Yhuz4Nu3YLgGZBGPc9QXgZy_oKWOj7bbks06zJykm4-sABwLY97OjXcBlk09_5XINw-ielxXpHE3CIHJXLsX9ntZ8qwtKpQYYQBKORrqfH9_WY2wNzjd1IywjrBOUZfmU6yXjZuCz_f8thXzzF9tE4HY65DKyvBgvLGtFM7QOM7cvHq2UWoYDoUkOOgrwrvrG7gGVptbWg3lR2wsk4QNsS09kp-n7zrrAjg7TfiGr24JEnaaKLFVTy-zPTBRYdFaSQ5TzQlMFbv8sMA32q2ZqRTCcsyr0l1xQD-rXO6Bqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_gzmDMcdvHL-RRzTxkluluQx5xLlXaP__B2q0WDe5KUqO7XAtSrDizgKgZwsUCaEc1CSVTnVFc-jTw8JkqjvUD1w6JoZaF8BEBVQHuh9Sz5SYl_xlocucUzl60D8YgqLVKBKjy_RUNlLBvr0EtMtAkhgJsGYlsX8mSMIXeFGNwhvmQ0euzuihdtvSjKS7BVT8oN9G4iaW7jUicxr9bKy-aE38NTc1L8yckeqcPx_dRF3ecKae5097s2v4MJsEFiUlzlXsIxo6U4DbrWDhhcCYtrcqr-qsHicv4zJ_aAZa0GzVWOsPhzGxdCZp-Y8xzsP4uYNE8Q5wBqF4tEZBp6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXj4UjNDZMdV-Bye-yBWl3REbsgiIxO8WEaBfAV9tNOzbPVexenaG1zdXoRWNKx_SjFYL6J2v5vrt7DJP4mztE5ZlH2scFtHmjMpOoqvTl9HGVFEc-vcq8iwQH0zVfyfGi84-VuSN_X7XQjDO4CoFPdwFnIeUPlFbcHKYExNCMZqMaeZ5UYCGbSJzilIYq-xAZm8yApjfVtNZYm0cBDx_hUL92lRoRb9cACY1cgKbqJ4W5h3vTibx1voQ-mz6goVt_u6_VrqkYu-XekD81EKGOChv_cBbRlsIG5nO_uC1OLTIzZyAXVOYedhs-hTQPo6cDGEKxN2vlI3gnSP4svsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHlr2h_yCffkMg9WXleJtgzLOsGsVaZk_-yp5PKhyISYO92JTdwBRUCEShcV8TGeY72AE9XM6yRqXWbQ8rgdrN5aZgjgrp_D0khWxsOYCXaTxtJlhADVPEB7-vpauS3d7t0vrCthFM7N7VLzRUOuzfVoTUHm-CCDpkN_4SGzxz-b6L4HEp-SoZ6aD3ihi1hSm_JN3L1mRc2JM2wIvlMYtOMZPTmI8cPDqyNIFPZ3gkRcV1p0c4U9ruBUaGVk5tpNW5UzegKLeUrUd3j54vA1QIlaxBm1klonUeusIRABEaTiD7t4VzdIhz7_JqaybS-4pVHPvQb0KB1CC_E5-JYMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=amIu960x3vJeCqIWWJrp7hldVKWDU38fJxkNXy0sTz08G0w-gCeZgoqktWJr_yJtvVshurVhd45QXRvQ4qpJMbykMh3HEkKOMkP4wWT2D7EQ7UkeB-dgbvFQ70wmnEKAQ8J4Zmf8xfeOX5nOJPO2zg5HKOh6-kq2a29gPDSFRarY6YyG6QTjTPimAC_f4oHWq8vU4g1by_NkDXy6EZgM6CqBi8wP0wfGFKXyo5O2Fonkd5O1YdyVlIitl25WHP_NwEeJFkhicVlGGFz57QKU5_BXfx4R-1tmz8Jh8Nl2O881o7nima6sGLYl6worKhVad_L3kpKVEPlPo_YVWROl7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=amIu960x3vJeCqIWWJrp7hldVKWDU38fJxkNXy0sTz08G0w-gCeZgoqktWJr_yJtvVshurVhd45QXRvQ4qpJMbykMh3HEkKOMkP4wWT2D7EQ7UkeB-dgbvFQ70wmnEKAQ8J4Zmf8xfeOX5nOJPO2zg5HKOh6-kq2a29gPDSFRarY6YyG6QTjTPimAC_f4oHWq8vU4g1by_NkDXy6EZgM6CqBi8wP0wfGFKXyo5O2Fonkd5O1YdyVlIitl25WHP_NwEeJFkhicVlGGFz57QKU5_BXfx4R-1tmz8Jh8Nl2O881o7nima6sGLYl6worKhVad_L3kpKVEPlPo_YVWROl7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el8jC-vgbAFKg3uyiGMLzGVdori0dWTQDGA1G3OqLT1d2HUumi5AoJFueCVybEnqw5Tvj4oPbQ5u-FCpBESQFm53oRHS4nB-xgrcnLtPc0yUHRuTNP5P2XXRa8MJL5y1diVWN0ipQS_GAfaSDQubdJVgvs6h3vulbvfzWiPJ3zGOt72-OPyviFblvjNxLC6rFVOozp6bQmMfjFcgP5MduJh4kTD8Qb6Udp5_Z-FaPvXPwQWPyihIjC_cIINBP6gxuJDCtuPnlLDMJJhwdNjVXpEg038D7MBzBlycWNZdVxNzRcXDB0giMczMdRf0--_l8FBv7SmzPXmPsTz8hkUxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6bSL8hazYNUIbHHZ-yEm1byM1UBpoYdC5R9je58sgllEp8fMyJErylq_Yq4GnkqLz9_aZpW5pfmCttaZ4bibc6jDeJ8ysfZ3QUYgjNOO0773BMnnejmotX-wSan4WFAk5tTIarPX29V9y4HZXywm5_F59OxyW97x_dApd22aXipwGhfw7ephzuiuFosC6hCub6wr8sYtn8axwJirWQCjqI51saBs0UeOWhUmmMSqsNN7NXzq2_7uXvzjyfd8p053zvWXD3Ct24xaKONaKVjLT7HcZd09pSVzYqBFsJQscU-7DYbo7lqypV4tiJ8SEBlWK6QB36hvY9kTNIfwXr4kDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6bSL8hazYNUIbHHZ-yEm1byM1UBpoYdC5R9je58sgllEp8fMyJErylq_Yq4GnkqLz9_aZpW5pfmCttaZ4bibc6jDeJ8ysfZ3QUYgjNOO0773BMnnejmotX-wSan4WFAk5tTIarPX29V9y4HZXywm5_F59OxyW97x_dApd22aXipwGhfw7ephzuiuFosC6hCub6wr8sYtn8axwJirWQCjqI51saBs0UeOWhUmmMSqsNN7NXzq2_7uXvzjyfd8p053zvWXD3Ct24xaKONaKVjLT7HcZd09pSVzYqBFsJQscU-7DYbo7lqypV4tiJ8SEBlWK6QB36hvY9kTNIfwXr4kDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=cvj4jxg6xvDb2u6M3_fG_YwHfwRDw0wBIRV6a6V62lUaqOYB_GdLWkMXyREOlAcxU-e9LPcy6dgwV28La4Cz1Cny0I2X-FNm1J0S1C9gubVuxwsq83eBwcjI1KXX4jVBlx1rcEk4qqRde9ljUTVqiZ8X_Htrmij1DjjFueICyk5ZpiGxD7wstQhR9q5ZY-7We_9HNSTbDQH_QY2sj9nEMzt-vs13oAUPtNiGYFVa1gNHOk22BwXMXR29fVQeUHtMxhP3SCpsHWVkRKuYqTQk2zK7ixDqbGb20klG0fILt9XHDLqvVxYF8zXcastVTBioFZTQYcavruTyhIfSzYLThg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=cvj4jxg6xvDb2u6M3_fG_YwHfwRDw0wBIRV6a6V62lUaqOYB_GdLWkMXyREOlAcxU-e9LPcy6dgwV28La4Cz1Cny0I2X-FNm1J0S1C9gubVuxwsq83eBwcjI1KXX4jVBlx1rcEk4qqRde9ljUTVqiZ8X_Htrmij1DjjFueICyk5ZpiGxD7wstQhR9q5ZY-7We_9HNSTbDQH_QY2sj9nEMzt-vs13oAUPtNiGYFVa1gNHOk22BwXMXR29fVQeUHtMxhP3SCpsHWVkRKuYqTQk2zK7ixDqbGb20klG0fILt9XHDLqvVxYF8zXcastVTBioFZTQYcavruTyhIfSzYLThg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=cMkG2HbKu8opGwjglHGlzL6ihMCLBdL1Pj7YyCgHmYEFqwUmC1aLVCcS4MlBivN5VLFmT_J_lc1cnXYwRsaGd7xmW1Jx1PP3zUPrXCSOk0S_k5sSWaY9XFBsYmGy0ouGWL9CMsS9NneU1LKGLdMgD2cMblA6Ovk8KLltQXOzusRi8faARl-2NoSvd1Ptlde9HkfcBxsscnJ44jWZg_ic8Hce4hNBmHRMf6z6AsucMC05djJL1xBib0xfRtEdP6UZUq4Us7SBjggb6SB9MEBTypkefYW-R3SvYvbEYLRlKyE0E4RyxmSMXq99qAig-5KfFY5RM2RAOxLwEYYczAOnHhmD-pd6jPpt8GIRYbZ99aaDmbimiXKg1ShGxuGfdbgOVflxDj-D7Q5Roz_eGsZn2sxNV_sRS4nKb4MCsQRDm0jIEMecn66joQMAr5LCIOJDUSbSjmqAlxODxvmjnWeH-6nAEcepDLMvYL3iZze-FnKMpUoMPpxAFEd3S97Md646rJsOHsQBmzHrKMsCnZbZ13d4v4-glhcNU3vC4xc-eW2nJyF9t27JSW1cCudLnuVAoGl5IruHLY5_SoYInyVCVK7CqZ-X2d7xsz9-P_Wqem7rYsyLZfjOfe1Cvx1aLHexDVWtb5HNyVr2Ii06DbzGWhRnzKlpyjOHDp5FBwEG_xU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=cMkG2HbKu8opGwjglHGlzL6ihMCLBdL1Pj7YyCgHmYEFqwUmC1aLVCcS4MlBivN5VLFmT_J_lc1cnXYwRsaGd7xmW1Jx1PP3zUPrXCSOk0S_k5sSWaY9XFBsYmGy0ouGWL9CMsS9NneU1LKGLdMgD2cMblA6Ovk8KLltQXOzusRi8faARl-2NoSvd1Ptlde9HkfcBxsscnJ44jWZg_ic8Hce4hNBmHRMf6z6AsucMC05djJL1xBib0xfRtEdP6UZUq4Us7SBjggb6SB9MEBTypkefYW-R3SvYvbEYLRlKyE0E4RyxmSMXq99qAig-5KfFY5RM2RAOxLwEYYczAOnHhmD-pd6jPpt8GIRYbZ99aaDmbimiXKg1ShGxuGfdbgOVflxDj-D7Q5Roz_eGsZn2sxNV_sRS4nKb4MCsQRDm0jIEMecn66joQMAr5LCIOJDUSbSjmqAlxODxvmjnWeH-6nAEcepDLMvYL3iZze-FnKMpUoMPpxAFEd3S97Md646rJsOHsQBmzHrKMsCnZbZ13d4v4-glhcNU3vC4xc-eW2nJyF9t27JSW1cCudLnuVAoGl5IruHLY5_SoYInyVCVK7CqZ-X2d7xsz9-P_Wqem7rYsyLZfjOfe1Cvx1aLHexDVWtb5HNyVr2Ii06DbzGWhRnzKlpyjOHDp5FBwEG_xU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bWCV-07qU3UdfScVvZt3cHu8pJUVrK-gAqCM5zHvUZJcWJLUxmYfu43PC6cpb3-Vw_PVLXv97_OMehJwU3oA6aAm3be8v6mm18uULZ7CN6DhLGIiaeIauXR6lBzfschA1TuOXNB12jSn-OtkXfWohKgot2Ub0wyo1nrIxiolgBu1c7ieV5cgucKMI19ryMq_H3-yJ6tPUT7N1OypOSCvllyofLVRyl6fk1E2scjNty4YcGPcNSS530BxfVmF73uYS5tAf3Yvz_DTGTuSy1RIadipdUIvvm5d48CWteOtzmCPnvtyVYRsSJRKQusTQ8pGcrkeou8ixyRgFaKVI-P2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bWCV-07qU3UdfScVvZt3cHu8pJUVrK-gAqCM5zHvUZJcWJLUxmYfu43PC6cpb3-Vw_PVLXv97_OMehJwU3oA6aAm3be8v6mm18uULZ7CN6DhLGIiaeIauXR6lBzfschA1TuOXNB12jSn-OtkXfWohKgot2Ub0wyo1nrIxiolgBu1c7ieV5cgucKMI19ryMq_H3-yJ6tPUT7N1OypOSCvllyofLVRyl6fk1E2scjNty4YcGPcNSS530BxfVmF73uYS5tAf3Yvz_DTGTuSy1RIadipdUIvvm5d48CWteOtzmCPnvtyVYRsSJRKQusTQ8pGcrkeou8ixyRgFaKVI-P2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC2zuxLiBWK_3BCbTRBogt3Wfe0mChjBzkvrWQJXIGT5ib9xGDkTatDuTBu655NmVcjVXrk8BwLLdK2VlticaKEXiVNRWEi5bn0OJUH1fRc2uFjp3-vXmvLfQhPK8yXvppdFMLM-PxoD5wFCL8BjQC6PvHwi9Fy743YCw8DaICek0VQsPEK7uFV-xpKZP3VhyS4boFmFDClVBjWE-2x4jDgpyCbJ7A4gnEXtGBh96KXtx3Kezib6kEfpqkqtde0I_oEhc7QDzIZK6eE0scorC6aQBMRxccHHuJMkT7Q_i1YCTlMc6aT0UPv_qfaD82uUXN9eQ2pWwJI0kPZBzEnboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=FIFNHDiirnSfCrXtb3UDyN_8XuG2GcUzmGNXLMqgjMG4OrX9wkk9dmaJC6iquc_bmP0CeNQWpwN4aympufhpYSvhDSQdriP4T6NCWb2OBb3EmMZSNvKjr3lutfgFvHlhDXxmAgZlQuQzK7jMWB8RF2E6ZBDboXwy84eGuWOqIVsLlnqqdvG4zCEM7E-IYeBZ8lyXWgBKZefoQ7ufcVZBwpcoQPj997NJbdZhkrgzQEBIi0XYLXcR_LDih9zk0CYJW7WTMt4KQLasb9q9JlLdujGEXFCY9tJM7MsfcAHMeZ3jyu_99DZfWARh0PgaF5s7V94ODdNEnEg7Yy7yRXHYIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=FIFNHDiirnSfCrXtb3UDyN_8XuG2GcUzmGNXLMqgjMG4OrX9wkk9dmaJC6iquc_bmP0CeNQWpwN4aympufhpYSvhDSQdriP4T6NCWb2OBb3EmMZSNvKjr3lutfgFvHlhDXxmAgZlQuQzK7jMWB8RF2E6ZBDboXwy84eGuWOqIVsLlnqqdvG4zCEM7E-IYeBZ8lyXWgBKZefoQ7ufcVZBwpcoQPj997NJbdZhkrgzQEBIi0XYLXcR_LDih9zk0CYJW7WTMt4KQLasb9q9JlLdujGEXFCY9tJM7MsfcAHMeZ3jyu_99DZfWARh0PgaF5s7V94ODdNEnEg7Yy7yRXHYIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=E7eLVDSK4qJIqfkLSB5P0xorWJytnUcMsH-0w8FZD-X7eLSirkmABlWHkEhRwMNuS0L18XzpUPpdJG_XGFlCxfY3LZP8w1AidLsryYCw4Ma4mziNxDc4HA2p48YudxLrU9sQdQ86ixJE2C0fXzTz7ersQrQPSIeaiua4oTe4DNIcLUDKqVy87jD_9tIaMmDgfOH-dHINigJ_-NIJBHOGBm_irWK7Xshl6zxLkrAP17pVzT6KpGpcfmKT6HOXZopJe9uyLtmVGO0VYLpSG4RURr3yAfh698DTGsX51kJNpMO7Q-TRax9fVbSXtBoIltkLnu7xQ0YkcqDhWV-AF7D-PgHBwsbu0lKT9HEG0VeFx4Gq1sMKFmdv2yQe570ZIiD4RNfSfmor4rKyilxaqi6m-AUIrI09Oao4Xjx1wpV2XUM002WARzDvd9EdkgqdCNmh79F9lsbMwH8dq_DEKAcfcD_QwzGdZ9bK_baWaW_5qgwN453ayQjSGKMnNUThBPiF4pSNqYbF_ZsO0hIgKTVIg_jwJQ0Erks8Z1ArNd2dPHYyryaIeTDdepDXguH0_1_svve3kYB04zh7thtXMzJUxJ0TBtZjZMb_mjltJCJ1qxQLMtF2hl59cvK2puZnEOXWw3FvHLCWEk9FdbFUuVjH5DsjEpe96ujhtIbfM2cLlLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=E7eLVDSK4qJIqfkLSB5P0xorWJytnUcMsH-0w8FZD-X7eLSirkmABlWHkEhRwMNuS0L18XzpUPpdJG_XGFlCxfY3LZP8w1AidLsryYCw4Ma4mziNxDc4HA2p48YudxLrU9sQdQ86ixJE2C0fXzTz7ersQrQPSIeaiua4oTe4DNIcLUDKqVy87jD_9tIaMmDgfOH-dHINigJ_-NIJBHOGBm_irWK7Xshl6zxLkrAP17pVzT6KpGpcfmKT6HOXZopJe9uyLtmVGO0VYLpSG4RURr3yAfh698DTGsX51kJNpMO7Q-TRax9fVbSXtBoIltkLnu7xQ0YkcqDhWV-AF7D-PgHBwsbu0lKT9HEG0VeFx4Gq1sMKFmdv2yQe570ZIiD4RNfSfmor4rKyilxaqi6m-AUIrI09Oao4Xjx1wpV2XUM002WARzDvd9EdkgqdCNmh79F9lsbMwH8dq_DEKAcfcD_QwzGdZ9bK_baWaW_5qgwN453ayQjSGKMnNUThBPiF4pSNqYbF_ZsO0hIgKTVIg_jwJQ0Erks8Z1ArNd2dPHYyryaIeTDdepDXguH0_1_svve3kYB04zh7thtXMzJUxJ0TBtZjZMb_mjltJCJ1qxQLMtF2hl59cvK2puZnEOXWw3FvHLCWEk9FdbFUuVjH5DsjEpe96ujhtIbfM2cLlLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMsGtJlN72b5cM3j6Nzm_wWA0EpCTvTWsJ5SGGix2nfnuGefViOq95u8gZgrDoZvaiUBqYjboV6_Aaa339qFirPhrpfLYahDC41E_i5Ek8cTB0v0GdabeoplZmmRRu9tcbDrEWr-5zmRHrVfZe2gCV0XdRD35hnAnMiwF4J2BzNtzFJ7VtbVBTwnbFfdMucyJpI-66L0K_tUKwSEjbLmjvyrgznc0UynCeWTP3J_dIFMBMU6z0cfbcF_EaCBAZmFkRG3QtaSq-iPSmvEEEHCO5es53sOJP8b2GuEKPh0THPRwui_7vpHIWQwxOoLsxGsyqX1GEiD1Z8-5NWaYTBaCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BJM-IJtfGCaTmDJVI8smdgvRvjLWr2Ad1Fxjodz_jKeLGk4X7eoDqjG_SlC4QFtiuqwjVGVf4PuhzFt1p8nhkNCfCNGjVoD6Jq55yULGUbYblOEM8Mgt4MUd5pVjMKAAk23gz4PBzwFV7edIWuIRsw8HL_WEq6T6ZabGIf1mJjj5DtAl7O7h65yU3cLzSiU5iRqEPAigrauWbK1_CNP3utesM0CxrO2ZbWdVFRGKUrWN6UfpYdPOOyMfna_FvXfm4BSFm0_EsAELCJ5bsQLloJ3mJl5SLS8_ZZLK23oTyGIlJVgPH8h8_tATttXzmuFyVxM_Y2-uYEBKyQiHDh4miT6xaT-lc292KOAROxHaqaHB5LIapzfZ5sBG0aT2r5CNfskbmKlvqihR71s4QMp6L0d8mQPd_FNx9JqYg2y0r6tA10nXCeL10XVbBGut8mJCNKVVbCRPcmVDFZ_-Sr-1vHZsc96Zj4yiwfNnFdZjnbREWEBsdYE5v0I6wkMKO1A3Zl67AeOibnJn2RNvRHd2r7yPAj03OTzr5OBe6FY0b5wtr-O_XPAqokZcQd4vV0rAk7FkVpsWUmfnSE9rAhdfNjwDxAtwxZHgUX3r2Nwr9ZC6s5ZsdycirhKWY0Lyi3DYAyjg-Ia-1Gzd4hPs9ri9NPRsxp3q2_zG-i6VJu__zaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BJM-IJtfGCaTmDJVI8smdgvRvjLWr2Ad1Fxjodz_jKeLGk4X7eoDqjG_SlC4QFtiuqwjVGVf4PuhzFt1p8nhkNCfCNGjVoD6Jq55yULGUbYblOEM8Mgt4MUd5pVjMKAAk23gz4PBzwFV7edIWuIRsw8HL_WEq6T6ZabGIf1mJjj5DtAl7O7h65yU3cLzSiU5iRqEPAigrauWbK1_CNP3utesM0CxrO2ZbWdVFRGKUrWN6UfpYdPOOyMfna_FvXfm4BSFm0_EsAELCJ5bsQLloJ3mJl5SLS8_ZZLK23oTyGIlJVgPH8h8_tATttXzmuFyVxM_Y2-uYEBKyQiHDh4miT6xaT-lc292KOAROxHaqaHB5LIapzfZ5sBG0aT2r5CNfskbmKlvqihR71s4QMp6L0d8mQPd_FNx9JqYg2y0r6tA10nXCeL10XVbBGut8mJCNKVVbCRPcmVDFZ_-Sr-1vHZsc96Zj4yiwfNnFdZjnbREWEBsdYE5v0I6wkMKO1A3Zl67AeOibnJn2RNvRHd2r7yPAj03OTzr5OBe6FY0b5wtr-O_XPAqokZcQd4vV0rAk7FkVpsWUmfnSE9rAhdfNjwDxAtwxZHgUX3r2Nwr9ZC6s5ZsdycirhKWY0Lyi3DYAyjg-Ia-1Gzd4hPs9ri9NPRsxp3q2_zG-i6VJu__zaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vmcpXMEQoaKji3rXgjNVKV3lYwGaAuzl0cyPwXMjHYN5qFcQt2AJSQNPDcdjptMchBl13NbxvJDKgK8MqtPRfeCW4EUMidOY4I12d-qKEXN-6rICAKw0FYdG4iPl4WcgGqWcC0URo3a0oVf9q7zBjAH9NtysXLd3MUiEgIsitFpbHFe5Ldna-GFfDkdOE8cnEFsT1cbf1So6aMbUOJQtmeVgCXei2gne6ZO4bttwRSf4GuXWXwrwJRHAzpZB0dtYb4r9fvQht0YEA9028NQP26PgcabT9H9q4nVq0gYFoLqmG31u4P3agZOev8q9mrCKIYzwfNr4AfYG4fdymV4TFVFES_cBv5Cu_WDMbOl1pwy_Sqa0ZqtU9HgHIjxDlo1GWn30KOqUI9PUzr5d_webJ-D_iMxDp0j0YcQQq9QjblNzVR-gvzBZQSXYYzFWrou4XM-3mqw1_9nBwsBRiEgoHZR5FKCcAvud6006bqgUSv0OGXwIw00W8EBeQDLOTAwyNETMZv1cHyuYfKPZKf2zq2G6Ts90e06dwJM4mFnwxBTJgetXFua3m2-xppHAb9hpy3GdmFE9Dyx3er2c5Bgwg6On9Ez0F3gUC2kOifEY05XoWppyQK5GzrJaF2mI5_OWeITYMOonmiZLa9vOH_zA-3Py9IlzOUeS0E0TOgtTGrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vmcpXMEQoaKji3rXgjNVKV3lYwGaAuzl0cyPwXMjHYN5qFcQt2AJSQNPDcdjptMchBl13NbxvJDKgK8MqtPRfeCW4EUMidOY4I12d-qKEXN-6rICAKw0FYdG4iPl4WcgGqWcC0URo3a0oVf9q7zBjAH9NtysXLd3MUiEgIsitFpbHFe5Ldna-GFfDkdOE8cnEFsT1cbf1So6aMbUOJQtmeVgCXei2gne6ZO4bttwRSf4GuXWXwrwJRHAzpZB0dtYb4r9fvQht0YEA9028NQP26PgcabT9H9q4nVq0gYFoLqmG31u4P3agZOev8q9mrCKIYzwfNr4AfYG4fdymV4TFVFES_cBv5Cu_WDMbOl1pwy_Sqa0ZqtU9HgHIjxDlo1GWn30KOqUI9PUzr5d_webJ-D_iMxDp0j0YcQQq9QjblNzVR-gvzBZQSXYYzFWrou4XM-3mqw1_9nBwsBRiEgoHZR5FKCcAvud6006bqgUSv0OGXwIw00W8EBeQDLOTAwyNETMZv1cHyuYfKPZKf2zq2G6Ts90e06dwJM4mFnwxBTJgetXFua3m2-xppHAb9hpy3GdmFE9Dyx3er2c5Bgwg6On9Ez0F3gUC2kOifEY05XoWppyQK5GzrJaF2mI5_OWeITYMOonmiZLa9vOH_zA-3Py9IlzOUeS0E0TOgtTGrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OVn6909swx_DWwCRAhtPCHyVC81QWplwyJLvBp8iJ62s8Q_uuC0QfRPa5dV0A2HUBX_CRDaK5AL-f55gHrsXYhnfOGsqYg6usbyP0zMF4N9Y_ShBbqCT9PuTpPAdC4SDJzQhlvyethS9WHiVSfcAFfxHI7tuJEJZN5hd2C3LBJXKUid3itT4z6Wn7w-96wA57mzStTNpSVT_W3HKjXUfC5l_uLi6WsLGJg8m2PuaSAzMa4PGmpnFxb9uwzpXXQsoBnFLfi0E400aC3aQGqMLuTufP9vbRh47w3Tqf1DU0UVL9Dv9zmoKhOATOBf-p7oJOzkl5qQTW5bArXTgqkMe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OVn6909swx_DWwCRAhtPCHyVC81QWplwyJLvBp8iJ62s8Q_uuC0QfRPa5dV0A2HUBX_CRDaK5AL-f55gHrsXYhnfOGsqYg6usbyP0zMF4N9Y_ShBbqCT9PuTpPAdC4SDJzQhlvyethS9WHiVSfcAFfxHI7tuJEJZN5hd2C3LBJXKUid3itT4z6Wn7w-96wA57mzStTNpSVT_W3HKjXUfC5l_uLi6WsLGJg8m2PuaSAzMa4PGmpnFxb9uwzpXXQsoBnFLfi0E400aC3aQGqMLuTufP9vbRh47w3Tqf1DU0UVL9Dv9zmoKhOATOBf-p7oJOzkl5qQTW5bArXTgqkMe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UISSjhD2z7F4WMxzuSYqsDUx5fG8xyP-f9yfU0qZub7fWrtUzxh3yIZwaKASjYIDgunPim79jKoLQR7f4M1VVtDiXqbVq9t2ysPj68hrbU8QSh9HjYtC-acJi7XGF0N-Cuy88-Zs3wdHdkFg2XtpJGEfaOvBzu2vutmgmUB3prSvT3EMGKjC5NSPhTMlcK8lyyM42Zopm9l-TuVgubTzOhhfOpYqnknGpc1gpayJJhhH1MxuqtWSXJrsjW2y1VI4-nDTbbFKUxVmx7e6sKibWeDhFjrAnjgkEVKrcMECxMWX2BjQsg4PKMQfzzO2drZngWqY6LYUG3Ij9e9HnEBozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UISSjhD2z7F4WMxzuSYqsDUx5fG8xyP-f9yfU0qZub7fWrtUzxh3yIZwaKASjYIDgunPim79jKoLQR7f4M1VVtDiXqbVq9t2ysPj68hrbU8QSh9HjYtC-acJi7XGF0N-Cuy88-Zs3wdHdkFg2XtpJGEfaOvBzu2vutmgmUB3prSvT3EMGKjC5NSPhTMlcK8lyyM42Zopm9l-TuVgubTzOhhfOpYqnknGpc1gpayJJhhH1MxuqtWSXJrsjW2y1VI4-nDTbbFKUxVmx7e6sKibWeDhFjrAnjgkEVKrcMECxMWX2BjQsg4PKMQfzzO2drZngWqY6LYUG3Ij9e9HnEBozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TzG_XYVUChv5RJo3hwiRU7jfDOUOpQ1tyieWVdeyWEXusWwr-PNIkM3yjvmDYmOOyMSPvnKLak0uex_zOE6Wv5OstDSjpfuH_JsDHYPXvgWtFsAWeqKkvPAscGznHC149m34aDuEgJzcZkB5-s1u8ke_z0TKutfvaUUZIwS5-2SwKUOBUI0fOLFHxLIXIA8hKDHazHeJd8CUb5W6Ki83f4d6yRXSTXZA86cels3uxQxWhhzeio8PPP2Fsigqao81mdOSXDHf4P8o6nGyvpOZYcRCMr2oFPQYvbzKRhqhcJKZQlAY9KqbqLbLckQXKnCudzP2CO2iO3WNvUxNgkTH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TzG_XYVUChv5RJo3hwiRU7jfDOUOpQ1tyieWVdeyWEXusWwr-PNIkM3yjvmDYmOOyMSPvnKLak0uex_zOE6Wv5OstDSjpfuH_JsDHYPXvgWtFsAWeqKkvPAscGznHC149m34aDuEgJzcZkB5-s1u8ke_z0TKutfvaUUZIwS5-2SwKUOBUI0fOLFHxLIXIA8hKDHazHeJd8CUb5W6Ki83f4d6yRXSTXZA86cels3uxQxWhhzeio8PPP2Fsigqao81mdOSXDHf4P8o6nGyvpOZYcRCMr2oFPQYvbzKRhqhcJKZQlAY9KqbqLbLckQXKnCudzP2CO2iO3WNvUxNgkTH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DPkOwKEn5HB5uBGVdZertC7-RImmTaDVwX5IfvXKvmkE1dUfO1h3g_atkD4lQc6F5jKMAcHE2gHCpSlpKpDl1Ww3r0bpbV_yB1xsWXzEgC7fGBGskoMPoS8NSpqbJVdpvdlIbSgyBMq91JjyGXeoO39O94QOgBgQRzc6ofOr41CsP0UAycr86-452Hh9oA4_Nhks4NZXcQVpcqW66smgZ0HidCVdTZPt1pFNVtt6y4w3_C82YLW4UBEtvOBH0RI3ClJW27oJHWUz45bcJ2eELE8Y-3xUekSAMLjxZN4SePRNkq3JgHzohSbtUGonVmwENQciJarPjLVO7SFQl1F5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DPkOwKEn5HB5uBGVdZertC7-RImmTaDVwX5IfvXKvmkE1dUfO1h3g_atkD4lQc6F5jKMAcHE2gHCpSlpKpDl1Ww3r0bpbV_yB1xsWXzEgC7fGBGskoMPoS8NSpqbJVdpvdlIbSgyBMq91JjyGXeoO39O94QOgBgQRzc6ofOr41CsP0UAycr86-452Hh9oA4_Nhks4NZXcQVpcqW66smgZ0HidCVdTZPt1pFNVtt6y4w3_C82YLW4UBEtvOBH0RI3ClJW27oJHWUz45bcJ2eELE8Y-3xUekSAMLjxZN4SePRNkq3JgHzohSbtUGonVmwENQciJarPjLVO7SFQl1F5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=imdqqXr4PJeU2QX1BE4LstSVJJNQyBGNTIL8kL5ioJ9Klj4xYTpjHwTasg4YRkKEmAU8pSOoXqeOTs88LNIOcynM4xxZGFSDHJIALnWGwp61G5X_OVu3NFopvMJMylBQ7iGaQOlVDSf5Hxo2roVWdPXG6_YRS77B3upkspKT84SOGqQSnbM_zaR28HwjrFXK5wfFMy6vP8Sfuw6pBNKT9PSrx-Qw3yfxME4q8DuYIYI44t-2w9R9iy72quV5LlAW4M1jhaTIkP7c6lCruzMEiON8HmFewWU179CO76ykmOkQCWF7O9GlZcOFDW8ay-akaBydA6XKNNHVY8wLmCx1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=imdqqXr4PJeU2QX1BE4LstSVJJNQyBGNTIL8kL5ioJ9Klj4xYTpjHwTasg4YRkKEmAU8pSOoXqeOTs88LNIOcynM4xxZGFSDHJIALnWGwp61G5X_OVu3NFopvMJMylBQ7iGaQOlVDSf5Hxo2roVWdPXG6_YRS77B3upkspKT84SOGqQSnbM_zaR28HwjrFXK5wfFMy6vP8Sfuw6pBNKT9PSrx-Qw3yfxME4q8DuYIYI44t-2w9R9iy72quV5LlAW4M1jhaTIkP7c6lCruzMEiON8HmFewWU179CO76ykmOkQCWF7O9GlZcOFDW8ay-akaBydA6XKNNHVY8wLmCx1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ko7Hefmanskw-AnKCLeNidwrXqS9LwalQkK9FEnquGtSKKWzpsXeu8pTcFYRTUuTe1rPVwpOu9MWxRXr62f8wlasdgY-kbgB46jTLIv1mX0fNY4MHklortr1szGVNQJI2pZHWAG7fsyQQEwDlJ0xmgtOQ8gHSft92mEaqJq8oQO3BsaW5QHCL2NLu-m-s2UDQE-rlMVtQ5HyQr3cX0ZGWbQaOEch-ogR-JBLUlTjqVAF-EgZE2GYwLUCNlv9-U3QHB-5NlSNIUn3xVwZZnbz3hKhv1FnZp9NsmNlvNhbr927uenKUCgX-R8PqnFRT9HwrJ7HSGJ6AdIfLrvM5U_eDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ko7Hefmanskw-AnKCLeNidwrXqS9LwalQkK9FEnquGtSKKWzpsXeu8pTcFYRTUuTe1rPVwpOu9MWxRXr62f8wlasdgY-kbgB46jTLIv1mX0fNY4MHklortr1szGVNQJI2pZHWAG7fsyQQEwDlJ0xmgtOQ8gHSft92mEaqJq8oQO3BsaW5QHCL2NLu-m-s2UDQE-rlMVtQ5HyQr3cX0ZGWbQaOEch-ogR-JBLUlTjqVAF-EgZE2GYwLUCNlv9-U3QHB-5NlSNIUn3xVwZZnbz3hKhv1FnZp9NsmNlvNhbr927uenKUCgX-R8PqnFRT9HwrJ7HSGJ6AdIfLrvM5U_eDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aqe7fvUvkVO9jNT1Pghx2oRIpTVkq3ai69Y7cS0tMwEb1Zma3ez6t8KPHfb58HmxqUTDEZfsx6f7zMt_qmFGpUBdx02mXjy-me6zEbpHGd_3TZhnXaUU7n57H6uCSmRtUDcI_rfzuVX22MNEomAUXq_gNMoCD-Jd74VL9hU30KDVnEePu4l0kJkf7DPCDyykHsJzh77yOCDujC1I6h-yNzOAdnEeqjUQiCkkfnBxXye7zxxY68_WVklIvJhS5UkkfNjw7HwWGATK7fwa4eqYvwD9DHmpJvj1OYrHWK5NQkQxOo3uMadKfXkXlCoWeTLqX_tpiAehDoJxkWfqNv2UEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aqe7fvUvkVO9jNT1Pghx2oRIpTVkq3ai69Y7cS0tMwEb1Zma3ez6t8KPHfb58HmxqUTDEZfsx6f7zMt_qmFGpUBdx02mXjy-me6zEbpHGd_3TZhnXaUU7n57H6uCSmRtUDcI_rfzuVX22MNEomAUXq_gNMoCD-Jd74VL9hU30KDVnEePu4l0kJkf7DPCDyykHsJzh77yOCDujC1I6h-yNzOAdnEeqjUQiCkkfnBxXye7zxxY68_WVklIvJhS5UkkfNjw7HwWGATK7fwa4eqYvwD9DHmpJvj1OYrHWK5NQkQxOo3uMadKfXkXlCoWeTLqX_tpiAehDoJxkWfqNv2UEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeXuZdVBtgG7JMiptTVbeO5trS0qR1Lsox0sGl3NekuMi-ylC3pVPNzTJ-t8ArbwSQifOeFCa8qJWWHawnGkUN9YZ_ctlrnxrGghdrO8YKmyZIb2l5_sXP11LP5RFjD8flPtn1kqrWG7gFxuIR4I2VEej1XFtR45PH6v6KBbr0UkAZM6zHaVj8d1yaPMwLqI3Tn06MrnOAzmwkUwq5qLW9HW2lJmoSuoNOOK7A2g3i7oArWguOQ698CsEs6DHg4FdRwDIcQ9bIXMBOyUp00AjaXdFIzgwlFqPHzfSFtffkRD9nEARbKelIIbkF-y4sY1tz33bS50dkxNqm4xDcxqIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DwZnUuk4iMJ62n153VrNbd0FsfTm4zwagWI02N3Kn9nzk13aRTRqvvSQrdIc50j_pqDOUd9b_kFtuKak9RRYzwggS6YcCWcq5gsgdyDcwKXfu-JtjR6V5gnvycadQaXTpmaojIHHReE80w5MqIKmbtDwjDMasObh-wWOrBXAKDxDz9fk4p7eTqgtZtxv15lHVmFQmfI15sRbqPTEL10wILN7BNqpFZvAjndsBNIayq1xCQkfzfegF-VnzN4KmYwIUIieVhvc3J44cIPW77QHEO_zbDg_E69FtU8KYi3Tm4bT6aRj4zQI9kXcsKW2cd-0nocw3iPtMfxPFsWyltwAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DwZnUuk4iMJ62n153VrNbd0FsfTm4zwagWI02N3Kn9nzk13aRTRqvvSQrdIc50j_pqDOUd9b_kFtuKak9RRYzwggS6YcCWcq5gsgdyDcwKXfu-JtjR6V5gnvycadQaXTpmaojIHHReE80w5MqIKmbtDwjDMasObh-wWOrBXAKDxDz9fk4p7eTqgtZtxv15lHVmFQmfI15sRbqPTEL10wILN7BNqpFZvAjndsBNIayq1xCQkfzfegF-VnzN4KmYwIUIieVhvc3J44cIPW77QHEO_zbDg_E69FtU8KYi3Tm4bT6aRj4zQI9kXcsKW2cd-0nocw3iPtMfxPFsWyltwAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=efLEA6K5Oupd4pXnVeIjPCH_XH_CSF4zV0vdhyQw3_eTUtrz3nhCqVrqgF8J2nVxQ09PoQW5g8DGRBdQnQgSieTW8i-sj2MigxGwT2yGEKqvXoj6jDdc3st49x95Od1olA5KuVyOht0cIhwCV4zsJlG3KbSaY4sDE4jpuBRvLCJOMKX4CXbhPdFnqE_3iQfobU0KYsllY_NPCvFvJ9HKSAa357dM4KPwuDhOaUpD428s1taHxQm9Zw6N-wezH5Xjbh2tOU3w6SLtWG68RQMPUcbI0ufoMPFxXWlyMKvrYgacOqyhghwnRpTzmIUtPFkfepGV2pG4k8mxB2Z6XmJRcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=efLEA6K5Oupd4pXnVeIjPCH_XH_CSF4zV0vdhyQw3_eTUtrz3nhCqVrqgF8J2nVxQ09PoQW5g8DGRBdQnQgSieTW8i-sj2MigxGwT2yGEKqvXoj6jDdc3st49x95Od1olA5KuVyOht0cIhwCV4zsJlG3KbSaY4sDE4jpuBRvLCJOMKX4CXbhPdFnqE_3iQfobU0KYsllY_NPCvFvJ9HKSAa357dM4KPwuDhOaUpD428s1taHxQm9Zw6N-wezH5Xjbh2tOU3w6SLtWG68RQMPUcbI0ufoMPFxXWlyMKvrYgacOqyhghwnRpTzmIUtPFkfepGV2pG4k8mxB2Z6XmJRcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=a7X8yc9E3vC336QhV3_3SOnWBqsL1bfAFg5A1W_24JuaGh3mlLhjm0Xo7TfrC-00l4WQn6rz4LFZDlPBGZCmVrYvwNst9X8DKR62FWYh3V3N3r0S61suPZw-VaE64fxmHskPMF6K-G36HYOzRtHzOeC45vf6TPpoc7Gz7GrgQOB9AjsLKCRS4r6gMn1xss6tTrUw46Awo3rnsjpqERcbvlzCrsML3mY-UG7j0R4T0n50y_m1P8sLXmeMFHiKjeLQ63vBmWxbjZXopogUYUZsDn_YPJ9HRTQk4U2b0Go7jb-xJSnfHBPm_b-dA_-uR2J8AfA-6IfV8B59JmC9sO1mbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=a7X8yc9E3vC336QhV3_3SOnWBqsL1bfAFg5A1W_24JuaGh3mlLhjm0Xo7TfrC-00l4WQn6rz4LFZDlPBGZCmVrYvwNst9X8DKR62FWYh3V3N3r0S61suPZw-VaE64fxmHskPMF6K-G36HYOzRtHzOeC45vf6TPpoc7Gz7GrgQOB9AjsLKCRS4r6gMn1xss6tTrUw46Awo3rnsjpqERcbvlzCrsML3mY-UG7j0R4T0n50y_m1P8sLXmeMFHiKjeLQ63vBmWxbjZXopogUYUZsDn_YPJ9HRTQk4U2b0Go7jb-xJSnfHBPm_b-dA_-uR2J8AfA-6IfV8B59JmC9sO1mbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ahWqOLqf0V3aqUbxNN0WVvUaH6Fap03QMgOjlYpheBIB4DXDSUWFc4s3HsMCuTkRyuweQqf4dx06MPQVjjpcbCURQIokXoikmFBLRiJmVLlntmOQcAEWr9d-zLCCSy9KqvfE3V2My-MkjIoaws_zBweqzY66pIz8NfpLIZzrdbLYgx56-BFgP8R6CJFUVSXF-DbyYm0fZYx84mu-qtdriga9ZAE7GQ3EDUZvqZZQeSDL-fIkmqCKfsCfBOchrM1yKJXH_Fw4mBnhU7TuuK5l1eQBmstaA4vqvPkqFbjsUe2bKOuK6APV4J6Yj18fmhsv8RYKaPB42ABwyH7eE2I41g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ahWqOLqf0V3aqUbxNN0WVvUaH6Fap03QMgOjlYpheBIB4DXDSUWFc4s3HsMCuTkRyuweQqf4dx06MPQVjjpcbCURQIokXoikmFBLRiJmVLlntmOQcAEWr9d-zLCCSy9KqvfE3V2My-MkjIoaws_zBweqzY66pIz8NfpLIZzrdbLYgx56-BFgP8R6CJFUVSXF-DbyYm0fZYx84mu-qtdriga9ZAE7GQ3EDUZvqZZQeSDL-fIkmqCKfsCfBOchrM1yKJXH_Fw4mBnhU7TuuK5l1eQBmstaA4vqvPkqFbjsUe2bKOuK6APV4J6Yj18fmhsv8RYKaPB42ABwyH7eE2I41g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIMv0D2wxv5-tmgHKEmRpRVBTuwNe-U_KXuvZnAX6BMJ79VraYwJ6onh7ksHttQ64Zp4zGCsjeHpo1oeKaUjwSZ_cpWmQWUypCOotvyTWrRWwFh6Nxnvk-vPf0LU9yGb-ubgI3aSfTU41xNoSpXK4ToYxoWFNl9IUvOAKK_75TtNcX3H2lbBfQDA36v3aCEwvuT_xF6-Hdzs5ONHX5XSWoO4Bt_suOWQpYpvzqgN3v6f0yT3BVpTRnzdG5AN2ycrC0k_rbG8iI2WH9oENVMXG2qxm9itbvKMiTkzpkgk5wvg9BuZ13ZxtqAS2KIeVWwGisnOJUqzMuA_5-MTVRtwgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=AD2Z7D0EiwVoJ8DRuAg_embu_pzDv6F5zsfZIVuqwvtozNeYUXVb0v96Y0uMZ5iIBz2eGo6YfVNvH3K_qu5XUFZBWyAy_Ef1Dvbcty2gea3xkMG22CbDMVGQtDtXGY694UwLrbt7x2fkxZqjTFm43kw5kcP6UpOpcCL76ae23deEvXlLChz9nXuqCgsuyfs0doWWjsuOnUY6TNVvuXVA4zmHN9SfiaQ7V3hsKhRAchGMJ5t3C5lTF3ORT289Mbj5ucIidrdwPBLY7sgun-LxA6vjzAxOgGjn_mrTJzZ_peOsqDnyUjIPk4rXSZMJIWSMIb_MLZAQ9zpszGW79r8JqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=AD2Z7D0EiwVoJ8DRuAg_embu_pzDv6F5zsfZIVuqwvtozNeYUXVb0v96Y0uMZ5iIBz2eGo6YfVNvH3K_qu5XUFZBWyAy_Ef1Dvbcty2gea3xkMG22CbDMVGQtDtXGY694UwLrbt7x2fkxZqjTFm43kw5kcP6UpOpcCL76ae23deEvXlLChz9nXuqCgsuyfs0doWWjsuOnUY6TNVvuXVA4zmHN9SfiaQ7V3hsKhRAchGMJ5t3C5lTF3ORT289Mbj5ucIidrdwPBLY7sgun-LxA6vjzAxOgGjn_mrTJzZ_peOsqDnyUjIPk4rXSZMJIWSMIb_MLZAQ9zpszGW79r8JqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jfSTJ5kBRUgxEiRf6W9TnRxaxqeiRWpdkeKpb97YmUo-Sz9yLRZoANOpWYLtKzkZR5HKGtqHWGzIIUekjgJFkqvkdgbnT9OfTBTnblvyewGknZ-v8g2fET69iVKiIBdb2nNeHf6cZ8lPv4Bc7CANnineR0y5UJxmhOLOq27D5Tya_IIAPhipyiVpEVEAsTKiY3DGQT352QkqAPWFF3HJdovlhMk5Vv6mhJuLNQp90IWaSJ4NrRstxbEjp7epVgFrHIsro4iDqzmZNSGiXpmKfTbEqov9CHQSvkzmaZNz04ylzP4b0JicbF8pjjwkVkS0LZvrO6xyvXqJHEkU7FNoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jfSTJ5kBRUgxEiRf6W9TnRxaxqeiRWpdkeKpb97YmUo-Sz9yLRZoANOpWYLtKzkZR5HKGtqHWGzIIUekjgJFkqvkdgbnT9OfTBTnblvyewGknZ-v8g2fET69iVKiIBdb2nNeHf6cZ8lPv4Bc7CANnineR0y5UJxmhOLOq27D5Tya_IIAPhipyiVpEVEAsTKiY3DGQT352QkqAPWFF3HJdovlhMk5Vv6mhJuLNQp90IWaSJ4NrRstxbEjp7epVgFrHIsro4iDqzmZNSGiXpmKfTbEqov9CHQSvkzmaZNz04ylzP4b0JicbF8pjjwkVkS0LZvrO6xyvXqJHEkU7FNoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsei41UN5VVE_F0AusBRx4vxJ4DIJ3RrFu3QWvvc2i7USO9X2oSlS2ark0mKXYR5lTu5TqaWyGHYQiNPIzU-Em4fY-Gz6xyx3rK9XVJFw4-knsBYbtFsqNf5A7aFuvt2tjtXHMSvOfse5A4BrGVt801PTpygN-pyQXjaOW6Juz3gZ9ifzPOA5qlfqgqEoVytJaHEnDL6TLEQHG9sXDfY1QoV9B2Xj4W8P0nAVvkHTyoZl3ZI_Rw0Ek5obFB6_Yzmn8ReG-dnwZe8Nb-3za37mtESg-OiJIqnaKASybaUJqjFSScTA8XXvrP9zEiPAYFDoPH7yXoi5VIoaZSr6WaNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ff2WgInygFVjPWfIuo0-mXc0FoWa-wNTzbE7fVFkt1-OgjERM38VEusDgnNzV5u72Xu8dyFYKXSWI1YSv_x7_fuTeZ68Nm_87xJmsVCilZt7umkfkZBEKEa-tJqCcV8WV2e8pD6slWg3sQbLmhJLRkeh_uskGX3FBhbPGkh_eczcq0H8EZ5_M72D-Dx22kIWMv3uuQtiQmLXtjgHo8_9ZvctX7zxO2kuyj_VWJYcY4knEJXSy1Q9shRDmBX24s5368BAde6Y9uXhz-JxicWxgXDpFqGmD4lgiM-AlJ7AlDMnPjlHI1CmM5pAwQngNPwvEJKvsdzwHLyWxNixj5F5qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YTSQa7EeN121Y1teXJIwq3XaeOtok1sLhn0ttQdYbgdrHQIlxRbQA7jdUvLiMZ1t0D0VNhS9jHkFKxjjFP6et6C3VV7XbnRJrXQxGweu4ivI81q7uU4qGvZUNkJcMEmcPkDadTJG8_YsR9CzVGwHj4Tufpt3uPLtviKwqWRLb30rBFKWQHf4oLfHIBWZdWcqs_4TnE0BsRdZg7lkTt3CjsMjdnbT8fagYe3cxvWH89szsp21FQniXl2L2xZzr-UzMPY4MExOv7uwa9Lg2_iR7BdYu1DOv557pNLghfnVSKOtusSt84Fb4jTbwOF-_JkC11cQbigLhFo_-_BbUiR_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YTSQa7EeN121Y1teXJIwq3XaeOtok1sLhn0ttQdYbgdrHQIlxRbQA7jdUvLiMZ1t0D0VNhS9jHkFKxjjFP6et6C3VV7XbnRJrXQxGweu4ivI81q7uU4qGvZUNkJcMEmcPkDadTJG8_YsR9CzVGwHj4Tufpt3uPLtviKwqWRLb30rBFKWQHf4oLfHIBWZdWcqs_4TnE0BsRdZg7lkTt3CjsMjdnbT8fagYe3cxvWH89szsp21FQniXl2L2xZzr-UzMPY4MExOv7uwa9Lg2_iR7BdYu1DOv557pNLghfnVSKOtusSt84Fb4jTbwOF-_JkC11cQbigLhFo_-_BbUiR_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FweDwIEzaWlZEZ9x-YzgvkzkGTOmNF4q8dKAlpPCkmGvZRvDO4toFekExNcoyWvujvUnkxly8TP4q91ircopsm7V1PsFXXrsGZNTkLXxIJM1FvwJATCn7Dm0ACkY7vevNX4FoQxCqPXixXbU4BU5QHBBdERuYwpVOM5kyayDLrLTkFw3Q941s7nB0j14ybfpt4iEZrlaVw60I-ZTv-MlwTvzaTWPUVhRA1mQReFlcQxmowFopTFebImz1UE6TLbF51B8kuvQqvJgp1_9SmFwdV-Fg8JrsQcLcTr1qaEoPa1e_6WypSRWE2xAZmLbA3PoB19AMXVifda0xkW4YRHr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZLlaqgiKx88xYCalUSy_GvO4biz4u2qA2Bg_VGTZeR4qkDP1yy9YqsdXTXMFfte-XC1UhJ3Cka4rEY93qVwyl_Np2HNbTKIIugW9933J3hVzP5J8ocSlVSK7H5AEZSFZTMexfZAey0iHOtGOFUVKXeR-QDrneSlyXZqXwWn1B3p4D7fNMfShSqqAM9z5SpVILnlpWdHV8DgKlz3SiO-UrDWw023e3TzYidYhHjN0lUf9bYN4Fie3_qjq0ilYNmcfmU8Vd6BnfjdP9TS4WAo8joWLkyraoNJEVdrjMzX_HHEbWXuIUftJ9MDth1eci0bwJ7KwxBov-V9Aa3AcYLAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G36dsPSMhKQvUN6zM4OpALvHKUxRf-Gv55BhZgP7y3G6nElYeA3i2xNSmmdkMERykfEmBUgJOxB_msPq6FIheWzLiBE7bslddvE_flIMymsq_AhDnpWck2b-bl5uxzOXX_NVgkoz6ZPzsSjFfy7eoVlEfAVkjoQlHlbVozbomftQYWGes2qR_F7H5MeRBkjewlRATWarpaR5qg7Va5hE-716RVIrMkpAgtiSiuyYbc9oFOj3lUfONhl4lKh-BmGqOjqADsSdZuFFPJ20NVDBzSaDpIoA8mgiIvNN-Izn9kbL2Io2enMEirDeRQJwDwIJkIOHC0i66etlFu77vhbjMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HUbkPmO63HkuVpukFQNOo1ormgsLXNd-KNcNw8KGNOZmOgge64KyHFOOZLY3r1tv5E4PjCFwqf06xbyV9O5bKm56oQ5QCTFqmyMoYZ3Q-DkT5pIdT-lcd1Q1aAL8Pr0x__TQwW-yoAynLou3MfyASUSo8Ys9vEAQeaG_x8unPL6NWQzMbPI333n1yp-bRQlPlhcHMhLSKVZIcde-9towMMK4CiCEh3svRrxZC3TiO4ye8oo9eF0TmQ8FNJrhJiN4zLN1BS77NWpjZWldFZYfKvUqiW9nHVr8c0ESHg8YIOakHlxp4XcD1qOe7mlnwJYsBJep9Czo15s2BEl3xhKqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HUbkPmO63HkuVpukFQNOo1ormgsLXNd-KNcNw8KGNOZmOgge64KyHFOOZLY3r1tv5E4PjCFwqf06xbyV9O5bKm56oQ5QCTFqmyMoYZ3Q-DkT5pIdT-lcd1Q1aAL8Pr0x__TQwW-yoAynLou3MfyASUSo8Ys9vEAQeaG_x8unPL6NWQzMbPI333n1yp-bRQlPlhcHMhLSKVZIcde-9towMMK4CiCEh3svRrxZC3TiO4ye8oo9eF0TmQ8FNJrhJiN4zLN1BS77NWpjZWldFZYfKvUqiW9nHVr8c0ESHg8YIOakHlxp4XcD1qOe7mlnwJYsBJep9Czo15s2BEl3xhKqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=OLv0_NEHxFpfBUqWVAwxJSqlzt59rq58RkrchJO6u-ZUDOE6sJemzPiNRIlvB_2oSJbAoV_W-t_x5iOomFmHy96XzrYXBWNMtBy2uLcl1mM7VQcUZfsOif2buTAnQ9nxeCZM2ggcPxq-TYHezP1c40oHKVA9mqCzLsgX-gPTCBnv05mrER9RejkJNr8l6cx3WAJygWwmbt_qpFUT4IbJirXwKQDYzQPj2R2kwis3Mfojkz7q8BOjYy6__F2d1kEH8tmcadRSSmjg4WK6kFbhR-F6HQvW5sZbeJLEXlGMG8kObVq5V4KQj9GH6aKN6wsFqgLOfskNHjEH_Q-1MrHTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=OLv0_NEHxFpfBUqWVAwxJSqlzt59rq58RkrchJO6u-ZUDOE6sJemzPiNRIlvB_2oSJbAoV_W-t_x5iOomFmHy96XzrYXBWNMtBy2uLcl1mM7VQcUZfsOif2buTAnQ9nxeCZM2ggcPxq-TYHezP1c40oHKVA9mqCzLsgX-gPTCBnv05mrER9RejkJNr8l6cx3WAJygWwmbt_qpFUT4IbJirXwKQDYzQPj2R2kwis3Mfojkz7q8BOjYy6__F2d1kEH8tmcadRSSmjg4WK6kFbhR-F6HQvW5sZbeJLEXlGMG8kObVq5V4KQj9GH6aKN6wsFqgLOfskNHjEH_Q-1MrHTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AsDfk9ZZ2qlpRXxaWnDAQQtohbhS0Sb9lofU2NYIv71nIgQbTlWdcbp828InY0KBR-29--EWCau4zGiTEaZ0hm6HYSou_hYrFe0HIzBFKxr3cstkmEedDTdfSzYkn4zs4lT7SmfRKfk-CDdGeGA2A0C52sYmS3NcZreYjwLf5sxd_pQawQVv_cmrqx_B2pk-fO6LPyvcNREJDibEzspiGin0eq3s-lX-atKiEKEoeP5vMvJQL2wFVJjG3_uNcIhOeaK3wHSjn8urV5PggciHdTRAVVKNAAnuUWrOt_abh62utrdJXIaJ1NV54V77Ly01xoPjOVUWKIUcT7hMd5cxpL6pKDBpURYU9WDF48a16d7j0jL0KEzkTBQSZrkwjWQsGy5Wvvd5Atk7jW_bK-Lxd6gkT4UWD6treC09W_mdFmk3r5R-nabPqjUU4Rhj_GhXVdZnzN45-IHbWzREPC6A6LUZ9XrEmOaK4gNVLRLVYu0M2w4337Q_houTV0o8brdPaOyfopzcIGwKKU2DPAA48rONwAgfyaeC85hqC3yFqLDchpYShXijTnK4DDf3tBcK0zQthyvVDTb2T_HYyjE-eTUHhKYIcgxNeBmX2_C7qlL4WiSgibLbF2S7Z5599Eyg3sGe6Feh7kOQPn1X694iE5zQ5oJPEV3ORk_ON4v-91I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AsDfk9ZZ2qlpRXxaWnDAQQtohbhS0Sb9lofU2NYIv71nIgQbTlWdcbp828InY0KBR-29--EWCau4zGiTEaZ0hm6HYSou_hYrFe0HIzBFKxr3cstkmEedDTdfSzYkn4zs4lT7SmfRKfk-CDdGeGA2A0C52sYmS3NcZreYjwLf5sxd_pQawQVv_cmrqx_B2pk-fO6LPyvcNREJDibEzspiGin0eq3s-lX-atKiEKEoeP5vMvJQL2wFVJjG3_uNcIhOeaK3wHSjn8urV5PggciHdTRAVVKNAAnuUWrOt_abh62utrdJXIaJ1NV54V77Ly01xoPjOVUWKIUcT7hMd5cxpL6pKDBpURYU9WDF48a16d7j0jL0KEzkTBQSZrkwjWQsGy5Wvvd5Atk7jW_bK-Lxd6gkT4UWD6treC09W_mdFmk3r5R-nabPqjUU4Rhj_GhXVdZnzN45-IHbWzREPC6A6LUZ9XrEmOaK4gNVLRLVYu0M2w4337Q_houTV0o8brdPaOyfopzcIGwKKU2DPAA48rONwAgfyaeC85hqC3yFqLDchpYShXijTnK4DDf3tBcK0zQthyvVDTb2T_HYyjE-eTUHhKYIcgxNeBmX2_C7qlL4WiSgibLbF2S7Z5599Eyg3sGe6Feh7kOQPn1X694iE5zQ5oJPEV3ORk_ON4v-91I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ae3nPCcKNQtLgrKyLTmb7Pj74MW91ryld9xJl2xJQu8nI-BxXTC5x6dfjddtrohrO0vVrk5b40XNBAsTy_cVBDMmQ8H1YfO5uUDkW6roVzsF7xgIlFCkvGZpcU8K6mn1x01BRfc2u87B1GrX_Uh-7nU_6FrpEY0yGqjxzsREiQZ9tSYRHcl05dCl71LJNP3egn7ii_vpphG3FAbSDI-CzO_11FJmJKe_MiYHnS3k-RtFB2-_ZwRtlUP2wvxSANp66cGNtrWh1I__z9TcHFAfLvqVne_kXSVsf27cNoKP3HTvwBDivoZW3ABMY0eYvkv_RntCWNfawajXuqc-wFS7o0128VjzVD3iqdrbUCQs8jzK9Hj7T3ZmSYitPBCVf1Wq63d9A_qDwAUukyuGxnGF9zhzWWMCQgcyJdBxLIj4u-I2Qc6arqsqNcnNVY5M0l_9xg44UptB2WDvly0SF-Qvf8_pgjFYYL3VV00SNXWRAZpYQnlXF5I6b02_AvU-iqYXVJwGXDnx50f9MV997U5PQXd6zCByhidK1oxq0vCJf6nhgSqEaTQCrjLj4EkaMGmOf6AuF6UpOcf9mX0ysGP-n5DnJKfTwAsVjfCksxbU1nhvSjaJx1xniXS5skCRTZ15CtrzcDUHtxWs3fFzoVMvy227O66_gkIiaHQ_FILV10E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ae3nPCcKNQtLgrKyLTmb7Pj74MW91ryld9xJl2xJQu8nI-BxXTC5x6dfjddtrohrO0vVrk5b40XNBAsTy_cVBDMmQ8H1YfO5uUDkW6roVzsF7xgIlFCkvGZpcU8K6mn1x01BRfc2u87B1GrX_Uh-7nU_6FrpEY0yGqjxzsREiQZ9tSYRHcl05dCl71LJNP3egn7ii_vpphG3FAbSDI-CzO_11FJmJKe_MiYHnS3k-RtFB2-_ZwRtlUP2wvxSANp66cGNtrWh1I__z9TcHFAfLvqVne_kXSVsf27cNoKP3HTvwBDivoZW3ABMY0eYvkv_RntCWNfawajXuqc-wFS7o0128VjzVD3iqdrbUCQs8jzK9Hj7T3ZmSYitPBCVf1Wq63d9A_qDwAUukyuGxnGF9zhzWWMCQgcyJdBxLIj4u-I2Qc6arqsqNcnNVY5M0l_9xg44UptB2WDvly0SF-Qvf8_pgjFYYL3VV00SNXWRAZpYQnlXF5I6b02_AvU-iqYXVJwGXDnx50f9MV997U5PQXd6zCByhidK1oxq0vCJf6nhgSqEaTQCrjLj4EkaMGmOf6AuF6UpOcf9mX0ysGP-n5DnJKfTwAsVjfCksxbU1nhvSjaJx1xniXS5skCRTZ15CtrzcDUHtxWs3fFzoVMvy227O66_gkIiaHQ_FILV10E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jEcw_17MofPrNajALyGAvIHlrMn3tScI5NBIRc2nRGMmndoXhXjPYOO-6ez9VyMn0EHyFP6eOAlBvoPdGYJ12r4IjW0L1gzpek6eKORlPETrQO7PRvcWmqmJAawRXAI9rzf7UM-WyADkEpOymqSGWmAOxx5yuKJBZLxnpyyD4k1rf2l26mY3vnINUfU2CWyTzfMn1xJ2tcB7nZCwq01Oj5IwqrVqDEASm9e6zDCyj8X1W8uraJ1bPzxEU2svtZaSb3sngAeCbDVUO33k8JJ4xKsT5VbgCJFpTh-U-1-2YviOEnP2Hb7hdrc-EX9bBzB6vIS8kybfEQ73J5cj-E8GGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jEcw_17MofPrNajALyGAvIHlrMn3tScI5NBIRc2nRGMmndoXhXjPYOO-6ez9VyMn0EHyFP6eOAlBvoPdGYJ12r4IjW0L1gzpek6eKORlPETrQO7PRvcWmqmJAawRXAI9rzf7UM-WyADkEpOymqSGWmAOxx5yuKJBZLxnpyyD4k1rf2l26mY3vnINUfU2CWyTzfMn1xJ2tcB7nZCwq01Oj5IwqrVqDEASm9e6zDCyj8X1W8uraJ1bPzxEU2svtZaSb3sngAeCbDVUO33k8JJ4xKsT5VbgCJFpTh-U-1-2YviOEnP2Hb7hdrc-EX9bBzB6vIS8kybfEQ73J5cj-E8GGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3y99RctPCAd59VwNoe3yXyzfgsgdzVfP3L2ncS5Y9sKD1ihDX9YiLaoOKRK6f6e8QQSE7FX_JCoss1xX0foIRWvTaL3fIRe9jD0cIEmpPzc-LJVSbkP_Qa2qJyzjkC4Vij5RC2oSKByw575UhXfeDYA5wxriCEHP2oyCrfKhbrV-T0hgaF9typ0bjhLAMdjB-BTpNf91zOu2_4SL_spZPr9DiVbbQkHF3BSFHFMgABC193udHO3tX-qzLHtSCnjiTk1fa6qSJLmFansNl6g_eIQPqJXu4g9mC3wfvZuhrBMdFusN3Tm5MfEB35V9kbumd38l4xHrc9l0Tn0c_sC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=cJY3ftRznHkIc4ks6efEnwMLgKqJuuEm6rA3GUbZG_D3EXhAj0pgEQ_aDgseSYEsIrZTrfeMC_CofTl1cOW1NUGds--ECRqN_fcc8laLG92xZ9dcNlsVRVKJKUCI5OTYKEyuoEVMCnVItdb6sCAxnH5A9NQZV1YgcoW_Rn22SezhC_02QGPTjwIRD8FoEBAlCOgwU0og6P9fAPpDN22gZl-NS9LfZ1EYJ_XVwFa-_yQ3nxWjhEjaZlQRNR_FtjWnNV7Mzm-vUQ_XxPhO1oB-TQiSLkzNkdJ7IMpt2utcsV2ggS4YEjrVn0EKoYTgLkPxqh0SJUP0v8-YVII-ESNXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=cJY3ftRznHkIc4ks6efEnwMLgKqJuuEm6rA3GUbZG_D3EXhAj0pgEQ_aDgseSYEsIrZTrfeMC_CofTl1cOW1NUGds--ECRqN_fcc8laLG92xZ9dcNlsVRVKJKUCI5OTYKEyuoEVMCnVItdb6sCAxnH5A9NQZV1YgcoW_Rn22SezhC_02QGPTjwIRD8FoEBAlCOgwU0og6P9fAPpDN22gZl-NS9LfZ1EYJ_XVwFa-_yQ3nxWjhEjaZlQRNR_FtjWnNV7Mzm-vUQ_XxPhO1oB-TQiSLkzNkdJ7IMpt2utcsV2ggS4YEjrVn0EKoYTgLkPxqh0SJUP0v8-YVII-ESNXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nSJpSUFtm1H82nGaduk5gyCJYoGS_7AL80q6CnRRoxR8Lb3SnCRILCdqXUGmVYRPpfv1Srj5a5-i0pBHPFmefl4yVT1brsWNID8Uyw7Z4zkzhVn4caM8DGhagJvEmyN6YWGQg7MUOFMCoQU2dUKrAhB7owdVE0_ffOcKgCZNApAZs0rwH--a9kCM2a7ZbEc13Tk6el1f1pVCUqAAuBVW-bV5Io6jMrRwvjZtTCN5VtjfUDN1frvOkewGrF-gWDr7cggqarfK2XUfD_J96sUMDCMoTtYvrwRsLKXf_b-OXsJ0bPFpi2K12HcJLNp4YBlqsHjQuZL_slbE5kQBHIwX9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nSJpSUFtm1H82nGaduk5gyCJYoGS_7AL80q6CnRRoxR8Lb3SnCRILCdqXUGmVYRPpfv1Srj5a5-i0pBHPFmefl4yVT1brsWNID8Uyw7Z4zkzhVn4caM8DGhagJvEmyN6YWGQg7MUOFMCoQU2dUKrAhB7owdVE0_ffOcKgCZNApAZs0rwH--a9kCM2a7ZbEc13Tk6el1f1pVCUqAAuBVW-bV5Io6jMrRwvjZtTCN5VtjfUDN1frvOkewGrF-gWDr7cggqarfK2XUfD_J96sUMDCMoTtYvrwRsLKXf_b-OXsJ0bPFpi2K12HcJLNp4YBlqsHjQuZL_slbE5kQBHIwX9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isfJCF5TvRbauJIPYfPucCxbHWM_yhH6KFEm8O8IQmOOv7iosZXbiY1_-yMuIKVeGerfAz-mlmJKixS1mfGUnbj8jvhKrjreIMWqNBnF0-B9Lpp_c9uYyotiHCgseE9ESUb3VvgnHU08S6F61DBShOku4ao8o7dfBwVJESr6yvSJuENvSnEFRQyMi-m8sfdgExVmDZmIiwaauPhgr05B-iiEAwBRSuq8h6WPh3iE7MS-WGBSDI8Gs2Du1BW7PDPnAi3U5cxu24QLvqo8ryQJrSEgepGwgq14QFvkW4paKnQ9hOr7U_lk6Or_i06XY9MuPaFOAXpfcotThsaNkOfjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixA0ZtqVlGb_-BlCtdS5XsMeO-bQkF9ASmGuhNytThf8x1beasCgKoMC-eLj2lMKyVpVJpjjDIvaaLHOvKjG78_U1B7tRJQYLXnXXXl8_ZV94h9W4aq0o7FAEPUp2KqOCZ3ldRt-EofaKt1UYWDokivi906qOEmRSRn0IxWYlFkfyAK8_-st-kBoREGC1bqk-iNpdiPFt1AMNo2lB77OKSqglaXgX0b60A5Nbbu4RthLjgikpeXASmEvGVryJQXjvYn8JN0tBVYFHUW2ZTS01SFYChdRWnwsQ7dezKsxWb13RfJtfOrW8hNU36CKhdnbswzdVpIYNKPpus5Xohe3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttZR6HIfERRXJtFSYqNx1pqHKGcQP9MjLyJ__l3SrSz9p94h0p7rYFM0peP2VFkkdfOd3ezuLsKdux3gs6dAA33J_d9akDvlFftxGKks62G5kPpbMcK0kE2GEQ7oIAzOVPkpLm8QlLW8doL_ojxgF0b7cA3a77r3KcFQDpL0gK4CwyATf5cpA_S1aZRYDpU4WBaFauRqLf5m2f-17QseigV8g6IXvWVtGMPi-b1U_CAbyJ7OmvMPHEF-cyIT5JZK3fgsN-ITiigXHPC3Iy00ezv1vOlYjGm4o3LdvHAx-DXEhxrM1TLrs8dWydBx5Iz5GAwXw8UtlTD9ZsFS0KRt0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnaJb7cUpbv_EyXHTa4PG8elkMMY3PnFfJGfoGDyvFogGg1HfVh2Cq5Eozf5jZIguQFSBzRQaFDnOoD_EKYlQIWp0YjB00in-DAbxis4Zi78jnApPSxmBUMYhhNsjN7J8rJ7wKi3Q07-3mzfVsrZXrLe52ezcnk46xopx5HVJmfAKqervh1dR18gb7BRo9l_7ziZ2ofuDTwY7DhFEI6OoCM5vj5NkDYdDknjoDOc2VAT4LABpe-x4FJb2IbGXZEsqTlb3Om762yEcPPmBj-wWpVZ0Nz30XSh0Kx6zcv24XiUz6bgfpSIuLB-OvgMk7ogN21jPNtWFhFlVUsv1Flgmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV2x7g_6CGMzRHacJBmLWeFVEV6rSRmQ0Ba5kAaX19AN6e5Pwph1dLkGirPmkEm5Es_Csmq_6OZoeMH10JPshXieFzweWPV6-WVYdBebF5nnWY_qmzGihfDGQ8qTteoo_4c1YOQvOdB-bFrj5xdA4o6MviPAaDllzXmd8oDL-W9bQSG9ANdiu0mbTGx-ZQCpyBOw24tBKratELy-eBRgiEpIS4RqtYeF23WxdEVcwRYMySgXgLdvaFLEC0n11AkHdYHkGfz2_o4rJKuEtgaznCMvX_0yEdrCY05TmKLKNKIseO-ScL6dIdU6nHmZ0r0E0DARv8u2r772i-MpRa4ZaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty77dTusAIktYdWKj5IXeYSz4rDOvyMPVooXzl91QRbbZgYzt2IIAo7el_21-D2JMZqE3yjE1ANttKKlY_6X7SE57D2s9_DzQq-IUKWIEf2CWvFC3vah3Xu7sc9QiaKGnitex_tWmBj7YHrs9e2MefBiEboIhdpfemV6ZeouzNCqIcyctW33Urnk8Plw7ZM0LRuMyaZAaKkXYKkv-oze_ioB67a_Ht1xxufXmZUwxjcmD7OAbViBTSC2qoXV5J83SZcKEvQeJa8mFRwBvRklfyIIb4QZd8YLhNgk4X4Rh9fZAbnnsW1mAUnLzPb-TI9KZh0Z87HCmxG1axVI7p_N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0rF317OihFLODIgP685GhKfgpJpqYdwr55Y_Gr7kM1NWmcExTH6fA1pgaZ9NIghC48m3gYd9Yd7DzO3QX-eqO_JpLDe5zlIz8-6kv9bCVvJSnkRPxrjRyECDdoPlQgMvIeJ4qP_LRU52h-fifahLCQBQHKQ4rVixRxljBZ0mstbZH8Gvv4Gixh8Qp4ztHCZbu6f4TMRgpUEbss2wHqXEDd2lSW7UhgEMPLRXHoiqH0obODCj6jhbpNqB6OIJ5kXXtwuha-QckDGaGVrs_i4ZzaQOp1ET0m4GhjXAiR_ADChWAIaOPlCQLDT5K1EWH96bfOyEq5xWKW1cGSq6S0oaQ.jpg" alt="photo" loading="lazy"/></div>
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
