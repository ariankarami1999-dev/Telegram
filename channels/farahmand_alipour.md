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
<img src="https://cdn4.telesco.pe/file/MZjgOL25P0HOGAEBcLlVYWff9nmbgMEZOOpGAEYk9gKGt8L3dmezX8cBUK3TZ_bVOOUgFppyWrLMDxf_LmISi-ZsJfKhvjCemG9U0j105bCPkDjbmKrl1uZbkERGfy5L-SGYZOYzCD5NC6aDz9HvHZnx4eUqQhRkcLIQ_6r7QvOjiT_cEtNFhlv_NXRmFxPBbeMbYfVVKMK4VG9t8JrucgYc5AjmJiG1sqS31GMco86TVjX8qEcyC17H4huo0sbGZY7owxgqzQXnRW-qtBwHLCx8IQsg8YduFgAILwVUIv0jwbufW1RlOT-4nfKjw5MwYAdPlgMD058JZy1_8XPzhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 06:32:46</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1IpHgUQbCuvlKDh3wit_xSm5kxt-_bt41xzna8DfsLYs2iKX79o3dGsiSYBX2eXU5x8MzGHjImdtnsSIez-_fwTNwkKKtCXT8b5PAmdob-MriBoNikrysTQ0P0FpQgNehhKzP8v6IM7g30nPWXfIH-3kJm7xpn5v2pBBRg5meeIOBQ36_unB4VLXVh6Kri-MCTW9-eFi8Biq1MYH1j1r9Iv4ZFsubaiZzYC0rY3t5JYJ4FSbBbtMmSbUx3ZzI2D6_ywcJw5rZjQ6LB5edGBwjpFXGRdiYy2KFogcivwkF0JrC6g_72r9dOxeVv45k437HPrOTkVUVzlNmDJEruEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcu8bFEAr5fJqC1-vXwVdBotP9ZK6_01Aw61sODGzzCEwyNeQwjRcwFCw6OMcMI4tpmVQsml-ui3XCm38X_KgyW7AKp73Lg-dik25Miqh6TSycO02jkjGbRLDsiNxHgWslvF78WQIBRHDDqddBPEoKxrk5zWQufTOIgB9bInj9BsdNaZyM8O3dBI-fCYo2gqUD-jRhWo0fSayMv146X6A7frgZ_oSZGeC_Kwr0Erj6vje7oz5TBb-WgRRl-PNfaFEjAg7QqVZAhSkwUs2DHu5sjpg1fREI-VWxTxx8VkAYokS_QTuoyzWrf_mHFml5IFiIrlqdaHX8bRVq4TuLRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP86bIVtPi9mAqOG0Xt1I131-Jv5xxUB3v3L1UZKSs7v-Q7q-o3rNe0DqxS-5h3Kn4T6M1H44wjXGh5BJdgUUzVe6c18GXm3_l1AQN4z9AVgH0iM0oR0QyMSHBP6-Cbu-663k7JhSy10CfyHh6rW4WxBLxK5EDW4tbkJpprVLuoVTz_dIcfMDcEB2dzBRewJ1lF5AnITdi_uQ49vjaMJiWWHefbCagbWxbX89P1wNaudNzfpVI2DELn54iC7GZtc6weIK0d3t9DYiKk3RIvVDrskjOUdtL6ZoFYXAJW32VACP0YRqk5r97NYnJK2DYH2o5KdtbWlWeYDiFUPNoWuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoQTpAGTsk1aVZdKV134P4FrAT2JK-xdGol5qGhIfZunmQohz66Cdm1eTB39BzQkL4EOWnj7IoxpT96g2NUUxCt0VvyURAUX8GnbIrB004art3rI-ZMELq-WdsTdVzaLtTIphwtZcLlAkbbrisvcalD3kWZi5Dk7qAxBP1Mo3W-ZKkIiJsCzQlLCA29r7_yeoIFnzweqtjqbN4UHahD9EJUNyk8ePFTNRtp9B--o0jGyJ9KivK6KEjaVpeC_Cj2ZXFuJg7YHYjqGiBNItPHwFg3lBA9mYqZB4uaKi8phkPO1kwiVPZAOBphm7H6sz4AEQJcMzrmIRPHKqefZjalI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ud-J6X683q5jaiJSnS0HigJIU7QiXM5qljyLKGYedXnRYDS-ozDZtjIKXeu-0PvGFIwFlgXc0sVvdyGIeWM_VhUdoBKCgbSdFnHd7o3fMPvqIJcL17WtrSXGn26Z0dMbH7j6P57kPKvDdCMK9LpnXMjkYuhBaBU6cVygs1oMg8oTmAcSUnp4q2WHmf7r5ZYxylcxkGnLPKlAXtq5ND4SQg6bU6IXwOOXTv7m-Ve6ny-xmWDXjz5spA5_CuqjnVFKqHQaLwU5D_Q8Pvwv0F9q4yekUDbKe7vkU3PrNsZ6SdLY0NkIiwp7IE40MWjxU82tHH652tVwW8lh_tf89TuhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ud-J6X683q5jaiJSnS0HigJIU7QiXM5qljyLKGYedXnRYDS-ozDZtjIKXeu-0PvGFIwFlgXc0sVvdyGIeWM_VhUdoBKCgbSdFnHd7o3fMPvqIJcL17WtrSXGn26Z0dMbH7j6P57kPKvDdCMK9LpnXMjkYuhBaBU6cVygs1oMg8oTmAcSUnp4q2WHmf7r5ZYxylcxkGnLPKlAXtq5ND4SQg6bU6IXwOOXTv7m-Ve6ny-xmWDXjz5spA5_CuqjnVFKqHQaLwU5D_Q8Pvwv0F9q4yekUDbKe7vkU3PrNsZ6SdLY0NkIiwp7IE40MWjxU82tHH652tVwW8lh_tf89TuhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=tWCWS47kGO4zHS7ahIgbadPz8GfMicaSw2K0DQZsRqbHGWAluXf38UUC0CLDz0ZMay5_JTz30Jx7alwWsMYXleEU4XzcEAg-77B6ktjYF6yoMmK7lwo0f5GV7hvImC00xdpkxNVETPo9xYNRSXCKCNyFOKSK5XWxuB4pQmZjANtq0Rk2E-Im9svDhFugZo4hlhaUpH9JIi5AfsqvleNHJqRU7uHjXv9TooCvlGIMapvHpde8VIA2nUOrenkp6trYywg4mXPXnPxaHwWeUDockv7arYLpMfbcx8kk73fhd2hppG1RzT1KW6lccsmJiYftwUqD3ENGreqGuPtldz-cRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=tWCWS47kGO4zHS7ahIgbadPz8GfMicaSw2K0DQZsRqbHGWAluXf38UUC0CLDz0ZMay5_JTz30Jx7alwWsMYXleEU4XzcEAg-77B6ktjYF6yoMmK7lwo0f5GV7hvImC00xdpkxNVETPo9xYNRSXCKCNyFOKSK5XWxuB4pQmZjANtq0Rk2E-Im9svDhFugZo4hlhaUpH9JIi5AfsqvleNHJqRU7uHjXv9TooCvlGIMapvHpde8VIA2nUOrenkp6trYywg4mXPXnPxaHwWeUDockv7arYLpMfbcx8kk73fhd2hppG1RzT1KW6lccsmJiYftwUqD3ENGreqGuPtldz-cRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KOdXofPiCz73PvdqYSpznko0DPYnz6rnyDuffVjIkKiNAzO26n4ytnnIN5LhDjamlGEZ2Qp_ibr8OMNiMCWSOpEAcULzpj4brCTKxJy-ZgD7Ez0ID64nWXj0MfP2GkwxRkPUvVQLXSnRj3uVXUuNHX2VfkuqtjO46p8befR2XU6ZoGDqPfhRu570hbAT9Z-PwOIm5bKHfgvGA5bQYAQAu0zoXNrO2HM8nCtFyWvb9qCdfUsG7W81lSpMn0U1Ul2T9HGZ4vOp0iHvxhganwWIEcAm2TR6mdQq7QBdDjDzku4lYzJRvnNZrDb3R_SoRywhP3AaeS3rPfaSzavfJjfpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KOdXofPiCz73PvdqYSpznko0DPYnz6rnyDuffVjIkKiNAzO26n4ytnnIN5LhDjamlGEZ2Qp_ibr8OMNiMCWSOpEAcULzpj4brCTKxJy-ZgD7Ez0ID64nWXj0MfP2GkwxRkPUvVQLXSnRj3uVXUuNHX2VfkuqtjO46p8befR2XU6ZoGDqPfhRu570hbAT9Z-PwOIm5bKHfgvGA5bQYAQAu0zoXNrO2HM8nCtFyWvb9qCdfUsG7W81lSpMn0U1Ul2T9HGZ4vOp0iHvxhganwWIEcAm2TR6mdQq7QBdDjDzku4lYzJRvnNZrDb3R_SoRywhP3AaeS3rPfaSzavfJjfpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMhhtFDPs_5Pya1GBMs2rYb4VZSVE72NoaFGSRAEg9Q8iPTLFi9MwRdryW0ms6Ejn1xPAEcs8D-cwZsqonVud-MfCm4zsq7x7UQwPkYLOo_iFoytulQqzR4NcDeszsKgXN4B_frmqC1MGanmMyoMbC0ldWUdAgzpumcbDOo_e5F2wSpIIBmTWxym41sWc62HACSX0caZUgdtubBsgkxD04tvEt_8zJhKeg69LWckrkD4Z-pKACon26DePf2b-NuGLnSsd3pHquQBL1zs7VK6x69V_abKJ1sBUsckA0jTduWPw5Eo391RYa57GFtxNfboYayoU3VXSt616oRQySAw6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KQWrm_w0OQ4Su82bhoOoYTuNBrJVF0NFgJ6LteflnLT9dHywyhaVxW19-lEuCZEZidnJhAeekE0ZDpNGJo4dlFJ0cZVjiOj19oOgn9y33-Uxm2_hYL1Hr4AvkZa2cXOBqQZZiWO5E0lpoIsLCaYxRjB4nP--OMdf33CXSTmqAAFyNrAcaClBdea1FxGiWLmfjDgDysgKCQuCO1iBLkoeI6Dqk8yp98k1azBwPXUnAl8Hju_Lt1YfYLWb002tOUps60jwWtxVcFwuyvesKbOza5DimclCwWE7PHQZOyU3D3rwPVqY_92s0LlZQ8zsuNiVsKQ_stAdzPIvGmAiQX-X2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KQWrm_w0OQ4Su82bhoOoYTuNBrJVF0NFgJ6LteflnLT9dHywyhaVxW19-lEuCZEZidnJhAeekE0ZDpNGJo4dlFJ0cZVjiOj19oOgn9y33-Uxm2_hYL1Hr4AvkZa2cXOBqQZZiWO5E0lpoIsLCaYxRjB4nP--OMdf33CXSTmqAAFyNrAcaClBdea1FxGiWLmfjDgDysgKCQuCO1iBLkoeI6Dqk8yp98k1azBwPXUnAl8Hju_Lt1YfYLWb002tOUps60jwWtxVcFwuyvesKbOza5DimclCwWE7PHQZOyU3D3rwPVqY_92s0LlZQ8zsuNiVsKQ_stAdzPIvGmAiQX-X2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QEMTH72gOwHZfPoxE7EPX1P0T2wVDdBe8HbxqAG4038vZyudh-uTydT8B_j14qc0v0OExC0eCRQkBQ8YGYkjVmhYB6zyIh4_6oSHA_6OXscKUQXZPFWpZdpKIxYrHbmMFDYXk-l7VLA_w8-UAvSCMNILBzoSaLPCvqDdxk3rCkKVlfNfUPmHHQ9GrLx2ITNlME-CQNHjKKrc_j16kpI2pD6a5NoiFe_a6xlUnyHMcDbsLELMlC11IXsWiKpPusfUfVviYba6TaUNhiqk01iLs7cSkzLbEh6XR2c3Gy1EnjlcT9dFPYiah2fnhsaE8LyvKlWAZiB8GIZR0Le48hbnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QEMTH72gOwHZfPoxE7EPX1P0T2wVDdBe8HbxqAG4038vZyudh-uTydT8B_j14qc0v0OExC0eCRQkBQ8YGYkjVmhYB6zyIh4_6oSHA_6OXscKUQXZPFWpZdpKIxYrHbmMFDYXk-l7VLA_w8-UAvSCMNILBzoSaLPCvqDdxk3rCkKVlfNfUPmHHQ9GrLx2ITNlME-CQNHjKKrc_j16kpI2pD6a5NoiFe_a6xlUnyHMcDbsLELMlC11IXsWiKpPusfUfVviYba6TaUNhiqk01iLs7cSkzLbEh6XR2c3Gy1EnjlcT9dFPYiah2fnhsaE8LyvKlWAZiB8GIZR0Le48hbnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAiGyK_72FzKHKYNcdMeJdA2bWvI3QE8BpIW7OvnEzdEBWY0hL5m_ANvuw_dt71a4fNQ3qd8A33814x-Ft0xRFmz_Gu7b5fP-rAu-JqKGx3vLd8nt5heI57Jiw7GQHECyqxZVsY1cfB6tMYZ5DQdnCPb8-Ue2Wgcqw1HfE5pc1ilRaq2ChDD_SZEpcRmN4ilke7i8zwFmEgh70GCNFos18ju1SAFvceHDxFU8keXklZw32IhtoFgJglZ8tk1kAzfjuSPkDq8SN4cNjfd5xLtJdZKA5fG55jRhIGOKjm4dbCxsALuNJY72Vr0YHGLbiOMqp2iIxLmDLLp68TRnXN95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pg_wMFWXM3MZ8VwA0CG4GKjko4K9H3WwgFqPMvmmVzCV7HQtctkoUsdtBMU0dWDJALt6fGq8qXiCBslA8-P6CtVAeom8ed-O5PY_ldf4oufOLTWkgXL8Cqh-dNHRQkSrNFo_zNZlB6u-PA_dyZEHUXxJzzuya5MgJvbRvUpVs1cbamZBlPxqdHCEyv0ECAiRkRd4EA1p0keW4BlfJS4WsS7fiRQLUo5tIs3xC-RLgK6GdQVBnv2j6gGEs3XdTcNT0ix3-gN3cTBQBd6MkuY7g6wOCFkaKUHyWnp4ZuVlrqCx7utWujF4EXCrkbxAEv47ZgCxK3UddBm9DX-OavNo4acyjw4dVTEJHMRLD-UAlvznz8mKoRZfX5DetZc4fNl6kXoMuAvu6zW4orBRXvwxxxyEfT2O31hcEA_St97MzDHuuzyfJ_pwFONbQsyWUA-SNFiBZwLPQ0q4c1XRHkLLZGsDFsUAi6XMny95F2EYBghyaXNLWl_2ONzzbG-0blRa1wcOe9Ez_7EDJhv9QK0r16eCc3dpIVp3vVxp1MEmcuoU7KKTVIBYojwhtMEJr3AZKpOHDkvxKHTTnzCMzzBmsfB_AzbzcFfUOo_vnbYXUv2h8FZNOaW6NwJpP_fsfsB1uXyKuK0JHXafoM92DF1FJ0r5BoHxzNvXg4esd9dRbeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pg_wMFWXM3MZ8VwA0CG4GKjko4K9H3WwgFqPMvmmVzCV7HQtctkoUsdtBMU0dWDJALt6fGq8qXiCBslA8-P6CtVAeom8ed-O5PY_ldf4oufOLTWkgXL8Cqh-dNHRQkSrNFo_zNZlB6u-PA_dyZEHUXxJzzuya5MgJvbRvUpVs1cbamZBlPxqdHCEyv0ECAiRkRd4EA1p0keW4BlfJS4WsS7fiRQLUo5tIs3xC-RLgK6GdQVBnv2j6gGEs3XdTcNT0ix3-gN3cTBQBd6MkuY7g6wOCFkaKUHyWnp4ZuVlrqCx7utWujF4EXCrkbxAEv47ZgCxK3UddBm9DX-OavNo4acyjw4dVTEJHMRLD-UAlvznz8mKoRZfX5DetZc4fNl6kXoMuAvu6zW4orBRXvwxxxyEfT2O31hcEA_St97MzDHuuzyfJ_pwFONbQsyWUA-SNFiBZwLPQ0q4c1XRHkLLZGsDFsUAi6XMny95F2EYBghyaXNLWl_2ONzzbG-0blRa1wcOe9Ez_7EDJhv9QK0r16eCc3dpIVp3vVxp1MEmcuoU7KKTVIBYojwhtMEJr3AZKpOHDkvxKHTTnzCMzzBmsfB_AzbzcFfUOo_vnbYXUv2h8FZNOaW6NwJpP_fsfsB1uXyKuK0JHXafoM92DF1FJ0r5BoHxzNvXg4esd9dRbeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVkSEquvuGg9RqWZSOY_BDSIrqzlmYvbZIdrSrJ_tNt-hjBhndw0CX7SY3_9U6a5MfWK3YOX7Mx9ParQnq2HZ6Pb8djQF7QsB8kOtx50Nwn5bsOABF1CRAoQAXEQfdrmf_jatptiO_giOkymDwMVBCIdvT_vOwdibL3nR_eS3AOqcpCQVsNKlzQHkGpb1tTin_GyYAuLb70bM6yFNi2nmNwmmVWVMyIKyZ7cVfR_uf4MYIfWnRf2ZdKiwCXObGNaiEq3bv0Wygsby-TlumnPa53JdWucCeSWQvSIf0ySSqvUX4jjVBJLt7O_1hE-6wp_-Sh6stEx80sxZBW2bekR9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IjeIyjYfvW-k1Rt1J0TGds0CK6SBeIn5gNYo5ZgVy2fCRPjG0s8hUB9bh6oR06O1gV3BLqnncET1jw4El02rwgrrf8m8zdX92LvHHyMUmcahjN49i2y3LWJoxHcdEYyCTS_pPHNvcyou3D_TkggylRDg1qzwAWkZ7VTRkaNj7eulQtN5_O7Kz1O4LVaP-HhoxrW5XY9jIoy5hzSYZWJwdUEi3Gi95e2G8_E12y6Er5Un3V4XrYNKh_al3xH8Sq2mM3LxSMQ9UC6-MH-bW_queqoNRurjuwkOYm1L4_hdkiqLjJRNQIKJh6mURNhFq6vu0f2qTItWpUUR5sZULO46GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IjeIyjYfvW-k1Rt1J0TGds0CK6SBeIn5gNYo5ZgVy2fCRPjG0s8hUB9bh6oR06O1gV3BLqnncET1jw4El02rwgrrf8m8zdX92LvHHyMUmcahjN49i2y3LWJoxHcdEYyCTS_pPHNvcyou3D_TkggylRDg1qzwAWkZ7VTRkaNj7eulQtN5_O7Kz1O4LVaP-HhoxrW5XY9jIoy5hzSYZWJwdUEi3Gi95e2G8_E12y6Er5Un3V4XrYNKh_al3xH8Sq2mM3LxSMQ9UC6-MH-bW_queqoNRurjuwkOYm1L4_hdkiqLjJRNQIKJh6mURNhFq6vu0f2qTItWpUUR5sZULO46GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MObrJIR15DD_Pzdp-PeWcaTZ2YRu8TU5rpIHY2t2jiVOnkw6B8Vbek0EtiRRgLGme89nptsaiPo4rQzWtgfEMCEr9Kf--alviNfBk1vg7qBspbpvhLi_VCJ5ojGOA0_rbc-nTKTbhkkBU6L902Yv0Ok57pnCAhwGKuwY3iHw1UU4U0ypMydDwIqmjea_-qsl3uXVxpFC6lXQRQ-8Oe20BUxPaGM-TK7rnXuZNY36uy-yM8ZlfoUxSNYlDErZYntqz2FXxz07Yn4-jqu9iyS8s5aL7ktaEncPnUP3eE3giCDPR26RdsWbcmOygTDYwrdwxBweuv4fZvdKHuN7wsSPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa56vuTCBXD4FoLuRviKLPkE5CehID__PGN0DiZQGPCafJXWXgx54DbO-J0x1HAd_jhBjsXSElRFtPtmw1hZHFqDWpa7cxbujWkyxRpUZoH4JjSnM0okCdUtvWRHwMJSHFwEBqGF2IhFI_VlrnugKw-OTvLQRfzhIbrD14WqAg7QgcEZWepkv9a7Cd0mTaGJDepZAiJUyMzRKdATgywwA1D8ePfhd3DnmVDt2kad0mpncpRFm-GsYpH5KBLY-oqkLNBscM7RVKUBKwmX_McS5WdhtdYwJ3DMAyjZA7QGI7ocSkyMGNVC13IiELUEZJ-_nSk6o0yWL2oBrw-IGyw9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZozjIh_wapOsLIQxBl24kjsTQSx1YIf5NhOv6fKBrx7TU5GxJJNB55OG2fl1LtqPYeCB4XDAkVWfbBZPaSH9SkY_poq4Ds4ENJHdzBxDAqoOVw4MdGHyYyiJdpbPZDUJUr5hPMLQKj9_RvnBsrm9eiqgnOiJmvW-v7ThcJdkIWI8QG5UqxrRXphhCxzw5T57KN2TssvfLf6n9P1cxxjckDpsGBdRzDPSi_E1p4HuKLvImCQwamv6PtL3p7u-_Ocg7_yrwkWKaiOHqUF9H4fkfyfRn7Sbws9vQotX9dZzO-se1KbZ-UsrPxnwrl4yLu0xotC4ok-SIOUoJdRmxZKC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sKh8xz7uHdzqiRgKpxhRH3KI_wLlLIOvp5ZunJN-aNCgCvGEhSxBpjXzxvMAbLAwFbK0jSXJDxnKU2InxX2DScBv1o_st3ssr1FRwc-W4PUSADJLlbQlsgnTbNIej6M9-Z2kfxJSe8kvhAD9Q8TxcrRO07J85Ubj9EAfjYtaK0nlVZAYersBJnFUhGPc0G9QwFGle0eXuzFSU1CHUrxozqr-_Huia7Ss1jLUlMJ3zjb-MILmpEyZBxWVdKnV8FJGScUveBKudBm2a56KodbOHqsOp3gy8GBYXrzAD2uAALVJ2A6G5P6rSPTXAD7juJ91-WAz6rI24VE0V6MgQFBwyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sKh8xz7uHdzqiRgKpxhRH3KI_wLlLIOvp5ZunJN-aNCgCvGEhSxBpjXzxvMAbLAwFbK0jSXJDxnKU2InxX2DScBv1o_st3ssr1FRwc-W4PUSADJLlbQlsgnTbNIej6M9-Z2kfxJSe8kvhAD9Q8TxcrRO07J85Ubj9EAfjYtaK0nlVZAYersBJnFUhGPc0G9QwFGle0eXuzFSU1CHUrxozqr-_Huia7Ss1jLUlMJ3zjb-MILmpEyZBxWVdKnV8FJGScUveBKudBm2a56KodbOHqsOp3gy8GBYXrzAD2uAALVJ2A6G5P6rSPTXAD7juJ91-WAz6rI24VE0V6MgQFBwyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwqpOdKSD--4LS1s1ns8PkOJCs2gtgomPJuTOoqv-SrFwEWTnRXypvk6ZGlcpO4kDr6qA8-8RG7ToTtqGFiHmp6VLA8bohiYLFZNx3qie8tWKnFOurxMYz2-Y9v94IUz46JPTP8NPwP12ALKs11fU9Tzc9RLoqV2wXhtk8mQE2rsyB1fcz7qEAt-23pMNLJaSkCMY6S2COD5Tr_jouWlCsvs9uQSk9SSBteVI-57a_WZGe-8Q5pTamqbYXE82EO0V5mpfchO3Zd8u6BSOC_hNGdIu9FbQCwkUuwz5yQuCfdUL0nqkf2a3X9Dd-oePtmpaf8KqMQoK5PYOz1qmrvhvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4jbkVfnuFlfj-LXw9AJ1zMA7ahB8Sh7Tn06q2xtO4cIS3KlM4kYyM3GLZJUSLWA6CIfPKN1ULzHz_GUxV11T2t9rW8W3-os3ejLWBJKV3ojmHIuS2YeBegMQDEYrCzFK4mEpQMkUdNEAWW5ujtAMSsX7i6FvID29Q1yWQkHu01r1CyTX2-72s3Yjp3hHWg-h6v2fNDWjD3dM-r14WoeyEbndIOE38QaOz6vAskFnGc_8jUy08O49Qg0jO1exoGFzdBm_DuCFdQ7u40DYmZeFuQqu0V2jJAfc31IdWXp_SQF2Qpb0kyPbjuKRRmyvClBWaaZW3Gdj8WR2z2JIn0fvg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4jbkVfnuFlfj-LXw9AJ1zMA7ahB8Sh7Tn06q2xtO4cIS3KlM4kYyM3GLZJUSLWA6CIfPKN1ULzHz_GUxV11T2t9rW8W3-os3ejLWBJKV3ojmHIuS2YeBegMQDEYrCzFK4mEpQMkUdNEAWW5ujtAMSsX7i6FvID29Q1yWQkHu01r1CyTX2-72s3Yjp3hHWg-h6v2fNDWjD3dM-r14WoeyEbndIOE38QaOz6vAskFnGc_8jUy08O49Qg0jO1exoGFzdBm_DuCFdQ7u40DYmZeFuQqu0V2jJAfc31IdWXp_SQF2Qpb0kyPbjuKRRmyvClBWaaZW3Gdj8WR2z2JIn0fvg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=f72INzuPI2q2LaKMBBJe-r_05cSmttoglSkj1Nug3yefLCtWI99rf5QklOiRKClIDgbbYj7-LSs1QYJ-PwKNvFQ6kU813F1S9vUxbqXVTDtlj9B092PXkrj4d_oqSwEHCu4A7LUHW5REJ6eZzgRB-TcXBP_8JOjN4y3979Lq4mUkcDSeWNJ0ECrjUPUyAgYQZsVF9yZMfK8keh6DPzQCC4I8NTaGGzomMgQAtQrj5Hc-Q4WAMG2MkXhubRPCvFGGYvXc9yzWZyhEJx3ugm7Wi_T3vivhf6b9aAy2zk4PovOeSIu4XbFrMB3SAnMGVyC6U4iHrlfLDTfKn4-yzfnYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=f72INzuPI2q2LaKMBBJe-r_05cSmttoglSkj1Nug3yefLCtWI99rf5QklOiRKClIDgbbYj7-LSs1QYJ-PwKNvFQ6kU813F1S9vUxbqXVTDtlj9B092PXkrj4d_oqSwEHCu4A7LUHW5REJ6eZzgRB-TcXBP_8JOjN4y3979Lq4mUkcDSeWNJ0ECrjUPUyAgYQZsVF9yZMfK8keh6DPzQCC4I8NTaGGzomMgQAtQrj5Hc-Q4WAMG2MkXhubRPCvFGGYvXc9yzWZyhEJx3ugm7Wi_T3vivhf6b9aAy2zk4PovOeSIu4XbFrMB3SAnMGVyC6U4iHrlfLDTfKn4-yzfnYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=pd_-vYYMFDgwKq7gWWZQ-K-eK-FOSSn1RG6pJ2u0taL7at_0hK3UTD9ho9hmJQsLA4-bfpt046EYOdIUlolhV_QWhpZ7Hc3vG7HjlZE1QGX-8VMeN-RDg-FvWjDhYdLg-OpFpQKHN4Jv0MIXAXsuxgJqABI2cgpdY8-ex-w--3SkxMUDXNrtCNfymz3p66-ER8KAu3S6joPGulmd8Ns89hA59lvZ-uJwl17CUmkr37L8x4SdC4-oMP5dtC-PcBtrMyYrhVHYF6bcbk4mxijmFk7BlFoqidncbA-t0Oy3Y82t2rtYeSDQy2Ww-5p1R4OrRcsNU26qTzFHO0ee_TwG0j7gkPG6vsptgJrHU55sSUDiKiMkVU9WN4DS_4DBGeYhoFZ-towFvtPvzKjPSc8LcdbQwXDmcF6WfwXvLtXrN5duDtNL8Vr5p83LZGTQkyltVjUMnliLkUaGIiFhZ4-VUH6TG1_7QD4B98ID-VhutMdSgWSC16OYcUfJmAFaQ4UZuIqD6y-ONuxypab155PdcqjN7PQuSaN-hb4qtKiDmAvD6rQ0z35C-oNZDKVLazgJ8ompyw-655rKB1rxSPKw3uYq5F9UYj2Wf_WlLwZRjwNiRC_280IAz36tvs3OWMv5cvgJYpDuR9YYA87e1RmnmFmMwa0-a_6A3NJjn0kXbfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=pd_-vYYMFDgwKq7gWWZQ-K-eK-FOSSn1RG6pJ2u0taL7at_0hK3UTD9ho9hmJQsLA4-bfpt046EYOdIUlolhV_QWhpZ7Hc3vG7HjlZE1QGX-8VMeN-RDg-FvWjDhYdLg-OpFpQKHN4Jv0MIXAXsuxgJqABI2cgpdY8-ex-w--3SkxMUDXNrtCNfymz3p66-ER8KAu3S6joPGulmd8Ns89hA59lvZ-uJwl17CUmkr37L8x4SdC4-oMP5dtC-PcBtrMyYrhVHYF6bcbk4mxijmFk7BlFoqidncbA-t0Oy3Y82t2rtYeSDQy2Ww-5p1R4OrRcsNU26qTzFHO0ee_TwG0j7gkPG6vsptgJrHU55sSUDiKiMkVU9WN4DS_4DBGeYhoFZ-towFvtPvzKjPSc8LcdbQwXDmcF6WfwXvLtXrN5duDtNL8Vr5p83LZGTQkyltVjUMnliLkUaGIiFhZ4-VUH6TG1_7QD4B98ID-VhutMdSgWSC16OYcUfJmAFaQ4UZuIqD6y-ONuxypab155PdcqjN7PQuSaN-hb4qtKiDmAvD6rQ0z35C-oNZDKVLazgJ8ompyw-655rKB1rxSPKw3uYq5F9UYj2Wf_WlLwZRjwNiRC_280IAz36tvs3OWMv5cvgJYpDuR9YYA87e1RmnmFmMwa0-a_6A3NJjn0kXbfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=oT9EFpy1t0HnYfCSFhFAu98Rmt-K9-fa83zJRSNli-k2t37iYQiWMRxR0XC_vuqeowS8a-oqZG8tYw-kRoNWB_VyR_04_6Yxtes96fdiV8hbmlKFBkafre1tPMeYiyLk2QuDK0nRHXO6x9lW27W4q7yY5fb1ZQ5h9gOmhnXJ1lJslrKLrI5F9VLVi7TTIkqAvdL_jjyov21sCkt6XuqFPh4nzcBVS1Drsp7lSanuLq8KlLOvvs2kPsbNAil3S2HFhB94lyqikO1hV-m-gHmlVlwY_pJOkfE_rXJHF_BWDsQOA3LciA3V0mdU5p5eEpFltpgthPMTzxX-W_lHo4us0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=oT9EFpy1t0HnYfCSFhFAu98Rmt-K9-fa83zJRSNli-k2t37iYQiWMRxR0XC_vuqeowS8a-oqZG8tYw-kRoNWB_VyR_04_6Yxtes96fdiV8hbmlKFBkafre1tPMeYiyLk2QuDK0nRHXO6x9lW27W4q7yY5fb1ZQ5h9gOmhnXJ1lJslrKLrI5F9VLVi7TTIkqAvdL_jjyov21sCkt6XuqFPh4nzcBVS1Drsp7lSanuLq8KlLOvvs2kPsbNAil3S2HFhB94lyqikO1hV-m-gHmlVlwY_pJOkfE_rXJHF_BWDsQOA3LciA3V0mdU5p5eEpFltpgthPMTzxX-W_lHo4us0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkExwxRoZFl0zmdoz8ukytiR0WrJZGvOdaPvdKg_jwc0-f-e95NCyKVBpTc9nXzeS3FuNjDJNAoX22CsHMty1hSZ2j-S8j2ovInqjsLekpT1ZCZWI_gqeSemb1PB0Ln-C92VWTDU2O1ng0zLutiMIFipAQ5Ka-nr1G5DvzAUOABJ8ptj1rDsJCS06T80HaYVH_rDfPorYATrVWAzESmk5uwVn2A2LbRo-WqHYPq7OfJINZStrysKf-gVXBgcGsMXemm7oqpDQIDEzaz1Pcvz_X3zRt1P4g9ipLJnqC3OabmIikNgVLbU5I2qPzqfMkbtZnZu8iZR6VSo10OrPASPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Croyu3OQ6NHD_-XW0kpxCzsqdYWRnZcRtCrtUB_7PkenzLpLr5z-sKeGl4FV1VRqbkxCrVwEemcHDwjTCA1Iv8XDndizZXNLAAAcJHE-fAQ8OLe8q55UTRlTXkj27XMPlY0FcDAcMabETsAKpElTrKSxLKdGCFJBKsaqrZeZaYfabzLqwaHKTrIH9ubmQYuLfqxJop_6niESnuzvRRhwLQtx2BofUXhkCjYW1EXrunF-DELqDnFEL-408RErLYxBQXL5n3Spub6YehSx7Ml-q8xR8AobP8dJukjyfy74_eEYRIlKkXh_CkiDc10cDKoThzW7gCYUt0xx3iUOdjwUIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Croyu3OQ6NHD_-XW0kpxCzsqdYWRnZcRtCrtUB_7PkenzLpLr5z-sKeGl4FV1VRqbkxCrVwEemcHDwjTCA1Iv8XDndizZXNLAAAcJHE-fAQ8OLe8q55UTRlTXkj27XMPlY0FcDAcMabETsAKpElTrKSxLKdGCFJBKsaqrZeZaYfabzLqwaHKTrIH9ubmQYuLfqxJop_6niESnuzvRRhwLQtx2BofUXhkCjYW1EXrunF-DELqDnFEL-408RErLYxBQXL5n3Spub6YehSx7Ml-q8xR8AobP8dJukjyfy74_eEYRIlKkXh_CkiDc10cDKoThzW7gCYUt0xx3iUOdjwUIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=iZpMf2-6oi1bOfk2yNpD2sud9U2bVniaGCdlGBzeZwqpGmh6mFvWbJmJIcKPump9uhZ-U0vLqC76CjyNc-WqOa8NUBVlSyyNs-ygLV3mqWwoMssrLnnynIpaFjgs73cLs0kwMV9fJHPmxupbrslOiOGzYJEf1SiMhl5PidknQbxLM70P7_icHRFTjs3bASILLqhCrsOzYl6_PCKVi8c6BfgbSh4cfvvoU0qdNg6FwMtPoQIbgsgeyYB3IStlV5eBO5cMjMboDXKLGpyuspLdzizO-2l8IRg9vGZr74YOZEa0LNvPp6iJMvu1IBe08p0de7Jx4Aev4Xf7y4oXN-z0ZoQhP32nH9jJuOgNwShL2-0E785zfc2i-1YSiKEZzNkrgpmX9XFKUcuIh4OWJOdUKIcoriOZUad5e-Xj-LXHz2eNy2I1wMKcjK3soHXCcrJvZZu1XCP5M1wQDP8iUhvK0nTX3IbsdjuTRQdiXL-mmy6LGENeGYWK23eMYuNLRNsr7dyVDuJyTekXwzAHaVzDo1Q7PkZPM6v5An_ARv7zAwDLh3qqTETyEBfCq6A2bzUwn8-dBc1Xw6VKap3HKPaug8gz820u0ajFeXpeZ2sqoH5VYw4F8oAlGhIsuoffRqscRfNWh3BUNdPjAFKg2FYIBH6NmdBK5CSrP96-3EuRs1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=iZpMf2-6oi1bOfk2yNpD2sud9U2bVniaGCdlGBzeZwqpGmh6mFvWbJmJIcKPump9uhZ-U0vLqC76CjyNc-WqOa8NUBVlSyyNs-ygLV3mqWwoMssrLnnynIpaFjgs73cLs0kwMV9fJHPmxupbrslOiOGzYJEf1SiMhl5PidknQbxLM70P7_icHRFTjs3bASILLqhCrsOzYl6_PCKVi8c6BfgbSh4cfvvoU0qdNg6FwMtPoQIbgsgeyYB3IStlV5eBO5cMjMboDXKLGpyuspLdzizO-2l8IRg9vGZr74YOZEa0LNvPp6iJMvu1IBe08p0de7Jx4Aev4Xf7y4oXN-z0ZoQhP32nH9jJuOgNwShL2-0E785zfc2i-1YSiKEZzNkrgpmX9XFKUcuIh4OWJOdUKIcoriOZUad5e-Xj-LXHz2eNy2I1wMKcjK3soHXCcrJvZZu1XCP5M1wQDP8iUhvK0nTX3IbsdjuTRQdiXL-mmy6LGENeGYWK23eMYuNLRNsr7dyVDuJyTekXwzAHaVzDo1Q7PkZPM6v5An_ARv7zAwDLh3qqTETyEBfCq6A2bzUwn8-dBc1Xw6VKap3HKPaug8gz820u0ajFeXpeZ2sqoH5VYw4F8oAlGhIsuoffRqscRfNWh3BUNdPjAFKg2FYIBH6NmdBK5CSrP96-3EuRs1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0k2-dbABb9OLM5CdOb9EVOsnWpJ_lT-qIgjJOgFzPbmYLvzmospFbWZ7_CulNRQ928DnO1kbbTvXspYjEbn2AFVBji4e3a0XsL-d-Vs8Ew4Pd739zO5cuGlYPAUVVBmisT13c9YOkOVduf5khuc4I5hUu7T6ev_cwA5HHhJhO95i8qnZNhu8BT_5FC30sVGM-CgRqSdvqBMuJ7iHu0I0htmOf-FAkLP43ys7we5p3nXTHsIuW_nLwNq9MoUU99SoUc6-moAaxrQ5kA8IpuUDjDkzJ9_Lhf5rMpEyquk34uDMxxS70wm0GUtZ4ZmtQuivUG3MZf0P5xyr-4UHph1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dUBi1KU8IBI7yYsbAOTKtgpNC-lieu_eY06BBxWx2w0vCcuO-UibtYZspphyXgEv4Jaojn9Uk-G3VPaqeFUnaPcK_8UDmd4P-tbo5N7fRJrOlTHsqrE_22AknkALuqASJu-E1jiGL5RvlL_lv_5o1KqyrWO2Ty8O-jIwn5dHw9b-UUKzpzAg_v_c41hIFZsnta-pbzEIh2qrLXEJEghmd6pNUdtswyYnbWEF3C6tbS585Yx8abZP1eUi8VKSjuyzIOUzXU4qo7Gx5fqvYy3vFLpMMn5i0Ij33XPi0MPPJ4aujfKz0oEYfXyG2rbkeB-96uupC3LEAZWmY_ag0kcjJXZSovD23iJbLfSS-roUDzgU3Qbow67Sx-GqacgVxNV02x_WMOZ9i9dH8Qfm4svBqJZfLuFkQ1nJ44Ejok8zNyqS5EqALKa_O2cgLEJ77do2dQswR52K9lYMluQPrbo1R8gWyZOjEo5Ye5xdomlVwPpEiUJgySVpGFq4my-e0pf4lP7C-qQwHGm84heqAfX6bBoqzz4ZXLQWZuIpbr9SHNGHUewfD6fcPra7tjuDoJ7AzBlSSyL4K8Ae9FqufpjPV05kxDPwI1reoYa9vk1C1LLIkjcPFBV6IDRDex4QvxItx6IkfkD2X8w2Q7XfcVVL--tjFTKu6ssTwTHPIT4TfJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dUBi1KU8IBI7yYsbAOTKtgpNC-lieu_eY06BBxWx2w0vCcuO-UibtYZspphyXgEv4Jaojn9Uk-G3VPaqeFUnaPcK_8UDmd4P-tbo5N7fRJrOlTHsqrE_22AknkALuqASJu-E1jiGL5RvlL_lv_5o1KqyrWO2Ty8O-jIwn5dHw9b-UUKzpzAg_v_c41hIFZsnta-pbzEIh2qrLXEJEghmd6pNUdtswyYnbWEF3C6tbS585Yx8abZP1eUi8VKSjuyzIOUzXU4qo7Gx5fqvYy3vFLpMMn5i0Ij33XPi0MPPJ4aujfKz0oEYfXyG2rbkeB-96uupC3LEAZWmY_ag0kcjJXZSovD23iJbLfSS-roUDzgU3Qbow67Sx-GqacgVxNV02x_WMOZ9i9dH8Qfm4svBqJZfLuFkQ1nJ44Ejok8zNyqS5EqALKa_O2cgLEJ77do2dQswR52K9lYMluQPrbo1R8gWyZOjEo5Ye5xdomlVwPpEiUJgySVpGFq4my-e0pf4lP7C-qQwHGm84heqAfX6bBoqzz4ZXLQWZuIpbr9SHNGHUewfD6fcPra7tjuDoJ7AzBlSSyL4K8Ae9FqufpjPV05kxDPwI1reoYa9vk1C1LLIkjcPFBV6IDRDex4QvxItx6IkfkD2X8w2Q7XfcVVL--tjFTKu6ssTwTHPIT4TfJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gARidWs5g8sACAOpxu4KksG8Id28Ot0DwQg7TAHsOnf7w5R2JfuVOGbeBIHcHeq0bwoXmMKDxLubW_F6DpPv3TXxIoO5JrA7S4bSIe-4QxT6Z_LSG4kSwzKk_gFWOxS5RIRknzY6nWC7V1T0ytbG_saR7g7nALWo9MKROuhXYmjKTGQNPLeDqQ3OR3u6OIxsBoDIWVS0eI7rho2UAdZTn0iVser88zvylzQKypBledHzJsjQU89u5VgfMtgibOaDLf2GbdWKkqaCN_j5aSPE88gVpUMRSzxzHoxWlO0TzsbMJ68hB8nOLijtDCn_BSvk_NlTbcYG7NYXTixEw8q96TGkG-FgpPWgEX2pxzr1UZrTaISeO7A3841-lgw6jQhYTjv287OxYUsgUF9AriIfFmbcQqKI6FQCyK6fXDQJTsNmjzno0SFr7XTwgjZ5g973byrXaAcAGDZ3QC-1_XCFNKJuxmF6GAhPQEoPAqxAJscMK47pEPK_UNCARfjCBpGoYRV3Wiyhb2bp6oHRVwA65VHZf-RALJFRaHN19SD8n3l7tETwVTGMHsEEzSGHBHvN9mga7XWHwx-z7PQJZsbEc6arqPJQZtYXW-cBuqgHLoKIuzuUe4V2tcxX5-lHMYPss9nn_t3peF145Mmd8LJJTqDJsfBY_EG29-D2Us9wUX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gARidWs5g8sACAOpxu4KksG8Id28Ot0DwQg7TAHsOnf7w5R2JfuVOGbeBIHcHeq0bwoXmMKDxLubW_F6DpPv3TXxIoO5JrA7S4bSIe-4QxT6Z_LSG4kSwzKk_gFWOxS5RIRknzY6nWC7V1T0ytbG_saR7g7nALWo9MKROuhXYmjKTGQNPLeDqQ3OR3u6OIxsBoDIWVS0eI7rho2UAdZTn0iVser88zvylzQKypBledHzJsjQU89u5VgfMtgibOaDLf2GbdWKkqaCN_j5aSPE88gVpUMRSzxzHoxWlO0TzsbMJ68hB8nOLijtDCn_BSvk_NlTbcYG7NYXTixEw8q96TGkG-FgpPWgEX2pxzr1UZrTaISeO7A3841-lgw6jQhYTjv287OxYUsgUF9AriIfFmbcQqKI6FQCyK6fXDQJTsNmjzno0SFr7XTwgjZ5g973byrXaAcAGDZ3QC-1_XCFNKJuxmF6GAhPQEoPAqxAJscMK47pEPK_UNCARfjCBpGoYRV3Wiyhb2bp6oHRVwA65VHZf-RALJFRaHN19SD8n3l7tETwVTGMHsEEzSGHBHvN9mga7XWHwx-z7PQJZsbEc6arqPJQZtYXW-cBuqgHLoKIuzuUe4V2tcxX5-lHMYPss9nn_t3peF145Mmd8LJJTqDJsfBY_EG29-D2Us9wUX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dL6e9FlD4yKAxiHDHc778BhyVwXy39n9DJEfybO-_56k2QXLacOhEo-6X8AYG66zgBFxDGkEfVINnTG0pTBfcnaBANfs592afpmPyulNnTqwTsDiwx0LQmzRWiN1WasbYJf-48SSUstgMmA1OHfSjr03HzofZbQmKuwfktYRWnrB3x9wgC1EMMfn7TIX-16UK1lr7T_dBnZ76eZmKtCSL_N24I8RmL8M5jC9EsAOGJBHqDWdUz5p1dSGBCcry_5k1MckjodBKsamLFbRPoIIuWjSQzlUGan883lQcvHW-imnqcHIqwFXaPuFbtP1-BSOzCm6tC3-mxhLw3nGPZ8jYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dL6e9FlD4yKAxiHDHc778BhyVwXy39n9DJEfybO-_56k2QXLacOhEo-6X8AYG66zgBFxDGkEfVINnTG0pTBfcnaBANfs592afpmPyulNnTqwTsDiwx0LQmzRWiN1WasbYJf-48SSUstgMmA1OHfSjr03HzofZbQmKuwfktYRWnrB3x9wgC1EMMfn7TIX-16UK1lr7T_dBnZ76eZmKtCSL_N24I8RmL8M5jC9EsAOGJBHqDWdUz5p1dSGBCcry_5k1MckjodBKsamLFbRPoIIuWjSQzlUGan883lQcvHW-imnqcHIqwFXaPuFbtP1-BSOzCm6tC3-mxhLw3nGPZ8jYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ILF3iOFkopy9Gir8TYFQsZyAgJ236Obqd9blndrI2VZMlK7XsJKT1ECHqCnydB2ujMmIqFpIVl2eBbyNQF53UHCmPoRfbO-1aYXIGSCKXoCJHsEhEa-RnWqj9dc7MAq5c9sjfKyqh9qjcgzryAjPtc-jUkZw5dNwFYu6trq2gUDQ9rVsv_hAx9B772FsQmHq33_OSBh_Itwv0HPW0i5yFtYqWhxnivPynGeghEBpNBj0xhnmg0HabNZc76Dn_Xfl7ZzID20wYNQgX7jn3uz5hhDEeRUJ6C3FY8Bcqw8myJooyQJZtAvJq9kwkvB_dm-mBKLGXpo_scgGCMH0GDa0GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ILF3iOFkopy9Gir8TYFQsZyAgJ236Obqd9blndrI2VZMlK7XsJKT1ECHqCnydB2ujMmIqFpIVl2eBbyNQF53UHCmPoRfbO-1aYXIGSCKXoCJHsEhEa-RnWqj9dc7MAq5c9sjfKyqh9qjcgzryAjPtc-jUkZw5dNwFYu6trq2gUDQ9rVsv_hAx9B772FsQmHq33_OSBh_Itwv0HPW0i5yFtYqWhxnivPynGeghEBpNBj0xhnmg0HabNZc76Dn_Xfl7ZzID20wYNQgX7jn3uz5hhDEeRUJ6C3FY8Bcqw8myJooyQJZtAvJq9kwkvB_dm-mBKLGXpo_scgGCMH0GDa0GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Bnw9ResFkQSBnhx964IZGhlKGIyAk_UoFdlZS7e5kyg-vEaMQaCxjmRbwy7QtnN_TjhcK9oHnkuX95VtmQxtMOv6cxtRve57RF03w1XoPRn9fCu70fPA0mIC35VMW2SRrlMy9ttvzn_lkH8lj4W_A8zccO3WzWB-xnSxNPhnoW8rWbdbkG9O6bweg9hFY-35S9GYWUfjV__VMW1eH-Dgy3qiaCx7ea-zcNBdEn-jpSXJKuYbia2NKG7GpE3FaQzoFEemTxke4Q7sdo3HYHSQ1cIt2kW-e-Hrnl11SjvufzO36SUw4fTaR3JjVTES3xEygQAiz1fM3GUoF-b0niEyXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Bnw9ResFkQSBnhx964IZGhlKGIyAk_UoFdlZS7e5kyg-vEaMQaCxjmRbwy7QtnN_TjhcK9oHnkuX95VtmQxtMOv6cxtRve57RF03w1XoPRn9fCu70fPA0mIC35VMW2SRrlMy9ttvzn_lkH8lj4W_A8zccO3WzWB-xnSxNPhnoW8rWbdbkG9O6bweg9hFY-35S9GYWUfjV__VMW1eH-Dgy3qiaCx7ea-zcNBdEn-jpSXJKuYbia2NKG7GpE3FaQzoFEemTxke4Q7sdo3HYHSQ1cIt2kW-e-Hrnl11SjvufzO36SUw4fTaR3JjVTES3xEygQAiz1fM3GUoF-b0niEyXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hMwwZkEO5-QtGJVguQgsxMrwCg0WrzTmpIM1d4h40mU2ReTomm2mgmQBMLXr79sl9RUzlCrVRoT86Rg5jo0mGZbbPFauJ8bH4xdeQxT4KJXPAfkjntyoI7DGbo3fdHWpFmBT_k0g5FRzDWeGMoGXc91q5QW0pZd2Ldx1pJfxDRSvvIundAk36nppc5tC-aitmmaQdoFZB8ClyNVS8vgyZ1okdfuWNqzU0qXGAwJtJWxGrD6AQqxGoiArjtdS-n521s-Ajbwa-MSJ7Fu08kp-wFMlu7UuMK9UfAl_bnXXbCkGnqOxo9TisfPDnEGvjvx_rVPwXaiL3rkTe0TQJKtWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hMwwZkEO5-QtGJVguQgsxMrwCg0WrzTmpIM1d4h40mU2ReTomm2mgmQBMLXr79sl9RUzlCrVRoT86Rg5jo0mGZbbPFauJ8bH4xdeQxT4KJXPAfkjntyoI7DGbo3fdHWpFmBT_k0g5FRzDWeGMoGXc91q5QW0pZd2Ldx1pJfxDRSvvIundAk36nppc5tC-aitmmaQdoFZB8ClyNVS8vgyZ1okdfuWNqzU0qXGAwJtJWxGrD6AQqxGoiArjtdS-n521s-Ajbwa-MSJ7Fu08kp-wFMlu7UuMK9UfAl_bnXXbCkGnqOxo9TisfPDnEGvjvx_rVPwXaiL3rkTe0TQJKtWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LzusNH6vhC4hgRtqXAnEn9R01tqJlb_bytslwI4ImPO-GDb325bC76P7LUtnxGezHDK7mROlXajbxR3rlrZBJ93F6HCQBg_nyQYzhz7VKqhnLqboJeZHgeRXc9GU0UscJSJqkFn9Bz6xQVmIYwMLiFvr7i1zR7CL8Ox4UtCxzC4yiIvhey8mquxvw3hbjK9GavOuRg_vAa6fDtt8zcdN0q3sSLBIJ3PAsAMmyC3RMl6WIXJfTrjO0PsqghvulKhUHDPVbTWiq8CK9noSw67z-hDOM-mLLcJ2MTVIgdHvOUjqy23RsZq0-fn8LTtQ7_nCeULabNqJW6ZQGC25OxjBlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LzusNH6vhC4hgRtqXAnEn9R01tqJlb_bytslwI4ImPO-GDb325bC76P7LUtnxGezHDK7mROlXajbxR3rlrZBJ93F6HCQBg_nyQYzhz7VKqhnLqboJeZHgeRXc9GU0UscJSJqkFn9Bz6xQVmIYwMLiFvr7i1zR7CL8Ox4UtCxzC4yiIvhey8mquxvw3hbjK9GavOuRg_vAa6fDtt8zcdN0q3sSLBIJ3PAsAMmyC3RMl6WIXJfTrjO0PsqghvulKhUHDPVbTWiq8CK9noSw67z-hDOM-mLLcJ2MTVIgdHvOUjqy23RsZq0-fn8LTtQ7_nCeULabNqJW6ZQGC25OxjBlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EVTPEt1-cxesoyDPokonE75XkMnWat-YMbK0fZZxFvyxL5opPDleTsl0m0K_iKPZ6DsOVasmfvUujZyT9qb_ya689GzhnCviC5acH8C3ddBeVIsznfZuy0ey7V8gvjHO060FtIubTPp4EtsYkES4kQOjNz22yCRJF1HZVWVHsaOwtZCz7C1sblPGuodw3Ex8OblYGWJGsRqLkBfGebMUgt4qR9y4417ysB4GoUdlQd1SdjIUjAsql3ti9ZhFUdCazTlMQ5eFa6w-U4DdukJT7tUp4EPYzB61sYhQTF2cFaFBOcM5_1kBg7p7CNEZvbL8l7AATbVbHYd-foD7f-TxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EVTPEt1-cxesoyDPokonE75XkMnWat-YMbK0fZZxFvyxL5opPDleTsl0m0K_iKPZ6DsOVasmfvUujZyT9qb_ya689GzhnCviC5acH8C3ddBeVIsznfZuy0ey7V8gvjHO060FtIubTPp4EtsYkES4kQOjNz22yCRJF1HZVWVHsaOwtZCz7C1sblPGuodw3Ex8OblYGWJGsRqLkBfGebMUgt4qR9y4417ysB4GoUdlQd1SdjIUjAsql3ti9ZhFUdCazTlMQ5eFa6w-U4DdukJT7tUp4EPYzB61sYhQTF2cFaFBOcM5_1kBg7p7CNEZvbL8l7AATbVbHYd-foD7f-TxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=NcdT4SQtgZTxL75v4gkgWl7ztv3lqvIw62qGii5S6VU8mBZ1Rh9PFRmo4MQk7mVRSmGscrdj0KKsyjt_qhbvM1qbmeYkNKt98WzTZfs0XLzWq2jFHSWBkSdC8HOtADvqGSArnOCu4RyfO8qr5XTXrn4i0PsNGUlWmrmvbY-3T1o36KWrO8MPI83PXCMQ6OZgPp65PT1hyd56ZrhbrL5lYq6z-q7Es908dwp3_QKmFqrXJIc6ggUVfRdemykYN8mdEUdy-Vr_nmr5qccsAL2JeITC0h_gxxuLMo1N_ge_T3Mj-GcELUJHLEjdHz-27OkCotoXZKrdYkweo-Ec8I3TuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=NcdT4SQtgZTxL75v4gkgWl7ztv3lqvIw62qGii5S6VU8mBZ1Rh9PFRmo4MQk7mVRSmGscrdj0KKsyjt_qhbvM1qbmeYkNKt98WzTZfs0XLzWq2jFHSWBkSdC8HOtADvqGSArnOCu4RyfO8qr5XTXrn4i0PsNGUlWmrmvbY-3T1o36KWrO8MPI83PXCMQ6OZgPp65PT1hyd56ZrhbrL5lYq6z-q7Es908dwp3_QKmFqrXJIc6ggUVfRdemykYN8mdEUdy-Vr_nmr5qccsAL2JeITC0h_gxxuLMo1N_ge_T3Mj-GcELUJHLEjdHz-27OkCotoXZKrdYkweo-Ec8I3TuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCi13XE4TaFZaePEp92AHH9n7XT_BByB1E8HpXs-aKGDuWK8uhWE31u2Go0-7CfVEX1KmpA7XhmrRbDxT2z-3eTkG2wbyft_OH99oiZc9FJ4PZlJSIm887s7eGeUuOa4ojCokBi2XDPsSYH9aRGM_HTIvbJjMmXp5VQ67Bb_IyLu_3tzjUuOn-OOIMRdwzVFlkamCb6uqVTOtzCoRSeyGWq3fdx1WoBhw68u0G3zxnyLihFJ3gPP2SdEJhFSbSXn3WQiQ3gT8Oz2gUCAnhpCOp_12q1iiPSI_076Iczc2osHdfmNH1Bu8wQhXEsrjcbWsnJDdjAA42DInpOm2_C-jQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WTfLHU7a0ee5CUfOpZhZ1ZTIMZ6P4ZPI-ELAJvRZd1Wxhb3ng2PzgE9daeVhTPaxxdj2k-fOT_lYaT5fCwgqDUXvsJsdxV7_mooLsR42NH2lIWoF88NA4lPXg83O1R9yvsxpWV4Numhg63ukSmwea9v6ecTTxsYVRvgK979WaT_qmNZQizwb_SwFQdoqdKPATAp6p_3egdIC_vp8_UyKwgA95Lu-AfpxmWcdUbO5IuOIsx98gE7kHDdWyEcdSDu7G98ItFAG6Cv-X8u-MorfaSjVw5x5e1Z99hhihHocPpkPo7aLRUSf7v8R6hehGZDcUAR7RZAMFNf2qOcscoj1rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WTfLHU7a0ee5CUfOpZhZ1ZTIMZ6P4ZPI-ELAJvRZd1Wxhb3ng2PzgE9daeVhTPaxxdj2k-fOT_lYaT5fCwgqDUXvsJsdxV7_mooLsR42NH2lIWoF88NA4lPXg83O1R9yvsxpWV4Numhg63ukSmwea9v6ecTTxsYVRvgK979WaT_qmNZQizwb_SwFQdoqdKPATAp6p_3egdIC_vp8_UyKwgA95Lu-AfpxmWcdUbO5IuOIsx98gE7kHDdWyEcdSDu7G98ItFAG6Cv-X8u-MorfaSjVw5x5e1Z99hhihHocPpkPo7aLRUSf7v8R6hehGZDcUAR7RZAMFNf2qOcscoj1rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HEbAZ81DrexaheeY1jxQFN-j4-gI9MwaHoAOTqRJjGL20qxMN1QM1diICZFEOjKqld0phxFvr90e3GtAV34n8OuauDghiBtpAPLDO93swW-NhT4dOQ6mHLQGxJIsYveLG-7yCFRgjOjgroeywVyTxaSHTfU_y65Ny3SJV_AtBSX_rW6NByyXZj2ht-Z6S3Ki2GGoOvo7vI__nKHyy_oj5G-vXHsuYS6IaSF9g27Dn7SyKw5YPVNCm6owB1M30xuiGjtvMrrgwy8qF4vUEC5lY547UIjxMYwE4FlfgZ1s1qGQrlf0clx6jAfJor94ZsSFDTyLKa-TG87YmgWcBRbj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HEbAZ81DrexaheeY1jxQFN-j4-gI9MwaHoAOTqRJjGL20qxMN1QM1diICZFEOjKqld0phxFvr90e3GtAV34n8OuauDghiBtpAPLDO93swW-NhT4dOQ6mHLQGxJIsYveLG-7yCFRgjOjgroeywVyTxaSHTfU_y65Ny3SJV_AtBSX_rW6NByyXZj2ht-Z6S3Ki2GGoOvo7vI__nKHyy_oj5G-vXHsuYS6IaSF9g27Dn7SyKw5YPVNCm6owB1M30xuiGjtvMrrgwy8qF4vUEC5lY547UIjxMYwE4FlfgZ1s1qGQrlf0clx6jAfJor94ZsSFDTyLKa-TG87YmgWcBRbj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=CxiLh-oswW5vnp6GmL3g16PlfIQ59LuD7HBqlAeFV_XTxfMXpcmjtDH9leTs-oepDWMoVHl83Osxy2hY36awS8hTMdjREetVeW_LSuiErDm_yqbT_1gl_YoCb04lnKDZ4Iy8OhsQiDyHqd1OmwyBBhOS3R875Hp_-7YpIYIbDNC0cCsF-w6x4S_Db9n041rOBIAZ_zoguOr15CWAANdTPq9gfpSHYiGKCZaKUpkDCmQ7rl5qlK6TSsQSIbuaPoqbba2x0oyMNLX1_UpLpR-TcN5IFKhvSd_Fo8LClbz2pEitc9Zp0cK6zUA97hEytGq1sUc-U285tGhdt79aVKDytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=CxiLh-oswW5vnp6GmL3g16PlfIQ59LuD7HBqlAeFV_XTxfMXpcmjtDH9leTs-oepDWMoVHl83Osxy2hY36awS8hTMdjREetVeW_LSuiErDm_yqbT_1gl_YoCb04lnKDZ4Iy8OhsQiDyHqd1OmwyBBhOS3R875Hp_-7YpIYIbDNC0cCsF-w6x4S_Db9n041rOBIAZ_zoguOr15CWAANdTPq9gfpSHYiGKCZaKUpkDCmQ7rl5qlK6TSsQSIbuaPoqbba2x0oyMNLX1_UpLpR-TcN5IFKhvSd_Fo8LClbz2pEitc9Zp0cK6zUA97hEytGq1sUc-U285tGhdt79aVKDytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=APTsziwOopcqQhiOdix4GqlU-lrog6V8cmxumY_D69TpOwH_MunrXcQNkNAyPVPIkzpna05CmQZ5uRUTu1LutuPIeA-hZbgBOgL-P6prB1kLeUbWZ6KTnT4quZRXY5FpmZWbCpAMs_k7xd1gNLbQwV1L7oBrHAn1-IMF9WXapbkKHRU7bQq3NiCSjkj9KzABnr9IV0l0fI9QPZMBE-KJfEN6n6pPL3mba_1zQsmdwrQGaHbIRZ0x3fnz6O2EfWaWIE6pCvHSf2mluh2PG9z5JC-FCL8TniJ0CNMd4ivASgY6opiJXmQOnvedSErgMdFe_8VdyX0XBkeBWxX9U-YEJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=APTsziwOopcqQhiOdix4GqlU-lrog6V8cmxumY_D69TpOwH_MunrXcQNkNAyPVPIkzpna05CmQZ5uRUTu1LutuPIeA-hZbgBOgL-P6prB1kLeUbWZ6KTnT4quZRXY5FpmZWbCpAMs_k7xd1gNLbQwV1L7oBrHAn1-IMF9WXapbkKHRU7bQq3NiCSjkj9KzABnr9IV0l0fI9QPZMBE-KJfEN6n6pPL3mba_1zQsmdwrQGaHbIRZ0x3fnz6O2EfWaWIE6pCvHSf2mluh2PG9z5JC-FCL8TniJ0CNMd4ivASgY6opiJXmQOnvedSErgMdFe_8VdyX0XBkeBWxX9U-YEJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix7jcFhhPO29G8KYJIjrd2isVkRsfF2yTYe_-FyKkpsaqEwkP7Ppe7bdJn7xCrhA3fNqBLryE6DHuQRYce_OMP0k3rCU7rlU4mgbqeGh3P2L1LHUWkwshdpSeLIM6lyscCjo1toPCZYrM3hCf3UjTWHBimlskzwPgge3TNAEHiCp7qfcP1ZL_qdCKSNfGKTqp-PO9eP3bP84Co1SQsnEb2d6SfRvq11Wnnxrc7qs1ZBodD7cseBKsZUESXaiujZGkSxxpw6mW7bWY40tJNWVYe1chA_LBlxJ9yZkheQnJoRwQzgoPCqbGsUamW7zZLhDeiUNETotKLDRZ6RIiMRiXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OCaNow_sHVydlERA6VaiHPNu7z4-M6L4hJqzn16bXrXhGRFSd6Nl1JYCpy5RYRoHYbYylhT12R90o9QHvPcGP4PkJAPtab5GbjuuXKfX4-2MNKld6If1x6_O_CVuGXoHDJ6hsJPJge7DV7o1My9LrWkO-UCfyaBqLcOgXSM7ujwHUqDngNLGpt9gVawCrMy_atwqZcIV7zOzmlr-eoE2SXWHxHp91LKIOQfjKiVJ4dQiMJQuTmafW9y_Zxse05AJt20zfzOKqdMsjtZc3Y75x1SaCthJ3b4U50MxCZSDZszi2rcZeWgC4I2ijPazl-7vHVF6mpmXJdl_hzljKdJY0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OCaNow_sHVydlERA6VaiHPNu7z4-M6L4hJqzn16bXrXhGRFSd6Nl1JYCpy5RYRoHYbYylhT12R90o9QHvPcGP4PkJAPtab5GbjuuXKfX4-2MNKld6If1x6_O_CVuGXoHDJ6hsJPJge7DV7o1My9LrWkO-UCfyaBqLcOgXSM7ujwHUqDngNLGpt9gVawCrMy_atwqZcIV7zOzmlr-eoE2SXWHxHp91LKIOQfjKiVJ4dQiMJQuTmafW9y_Zxse05AJt20zfzOKqdMsjtZc3Y75x1SaCthJ3b4U50MxCZSDZszi2rcZeWgC4I2ijPazl-7vHVF6mpmXJdl_hzljKdJY0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=pFpDq57PfEIHI8eG5rDQbgvQUg_2EST7WjXs57DkIUUGuqgoopdoe8el0Otz6wUoOsWsvkohLew80FLPiFpDqw7-OCsO_T6N-PvqyGWxXmpssiPUL5rSblq_1MGNFGggLThcjP8ZF32zee0qwo1SoEJv2cCMXRp8FQ33IuKiNL5-PRohyVAUDcQN8ps1J5-ea44fVFWKDz9Ubtf3LN8SfbuwwI94CoWFYTvmqrbhrdcQzhV7cU0oSwKbnsgVYoIXVM1qrLqLtDdDrS573HY1-k_VT2iP_mHrB9yofBYoTpxbqnQTCyJmBDydH5iL7sJjPHaHp4H0og3vYOGnoukPFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=pFpDq57PfEIHI8eG5rDQbgvQUg_2EST7WjXs57DkIUUGuqgoopdoe8el0Otz6wUoOsWsvkohLew80FLPiFpDqw7-OCsO_T6N-PvqyGWxXmpssiPUL5rSblq_1MGNFGggLThcjP8ZF32zee0qwo1SoEJv2cCMXRp8FQ33IuKiNL5-PRohyVAUDcQN8ps1J5-ea44fVFWKDz9Ubtf3LN8SfbuwwI94CoWFYTvmqrbhrdcQzhV7cU0oSwKbnsgVYoIXVM1qrLqLtDdDrS573HY1-k_VT2iP_mHrB9yofBYoTpxbqnQTCyJmBDydH5iL7sJjPHaHp4H0og3vYOGnoukPFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryNxuOPM9AE2luvODwoq-MrR4UOFwSAk7KcWVdXvTOowyouEAUG91oOM4az2EkSpc8K6B5tXkPNgHcmZuHsTLX5E0bwQAsBlRQStVBL5Mq6pDrQ-lVFJVYaxNrAxgqohNUeBirZOm-fc8DGj6iYMvNBGIG901Mkj-mqv1SAI9-p2tgsu3tqmfQf6GNmx3b0C0MHplTHKm16xZ5fSxWn3c5p6Go2IHatFxQO8fS2Nk0H-Tbo_iOhDgsLGJF74kudlDdXG1f8Gmifhcl8H1fVibrmk1N3VD4jsj7vjQ05IkMYr1efFpx119zRIW0UjHIdVKTkfsy3TiW2fBi5eJRUqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_cYoP6w2frE2PL4Foyy8nIf_nhR3yan3mCZ76YUvjJvP_-dZlRbU7KUJeDXEx1BGmAHCErwuGz1x8Xky3_RhdHX_SEy8OIAMFbNZhy86PaYftgjo0n9V33odcIWmV_wfqztin2unodpkh5qZH5D2lJgnhq9emp_wV71rRP7x2zIAt3a8F1bnlFV0kgje4dDfSPlYDfQ-n1ytXiG9jrqZXVm4b60f0S6aPO5qUrDL_Ds1S5Z4OHJ_vWqVqCMM0oJGNiWunDrzZ_PK_2RqRVEyFrHPLYpJbhsYSSCS0kj9pa4f3QVpnA9Ts2PEL8jVDsCK_FLFwKPOf9nMsJqtT016w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=tJxtJ1PxdcF7uv8UDQYl3Bd-fSzEEe1anJ1t4lrxzTmkmiAYZIG0rZaHFo-8vlp4vDhZ7JMPMqpjeUeeXRj3j0ATVSij9u7GanPFqXR37ZmIJpVj0QjaRkcGjAEGWvRRgiRhAesIU44U-wkyzi8kSH-lg1k11d9dcjvWgXds9fFGcmqI5EeLS-hvY6ssUnqtKeU2gxcBfPhkB3m23mvk88avCvBFCASEOsRGQmkXkOHMV9cXs9sZiA7Jnz9ezcfVOJ4HWztFGA9V5gGObR6_ZMelhXUYbzw9L7rTFK-40hmlb0iGQgI3riBDxG6v5ZoYlxBYlq0Ux5cWIEoxSriXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=tJxtJ1PxdcF7uv8UDQYl3Bd-fSzEEe1anJ1t4lrxzTmkmiAYZIG0rZaHFo-8vlp4vDhZ7JMPMqpjeUeeXRj3j0ATVSij9u7GanPFqXR37ZmIJpVj0QjaRkcGjAEGWvRRgiRhAesIU44U-wkyzi8kSH-lg1k11d9dcjvWgXds9fFGcmqI5EeLS-hvY6ssUnqtKeU2gxcBfPhkB3m23mvk88avCvBFCASEOsRGQmkXkOHMV9cXs9sZiA7Jnz9ezcfVOJ4HWztFGA9V5gGObR6_ZMelhXUYbzw9L7rTFK-40hmlb0iGQgI3riBDxG6v5ZoYlxBYlq0Ux5cWIEoxSriXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW-C1lDB4R0NX3BO3PBIsAzV6XBoF916SRj-tpydrmHRwXUlGj7JkkZmG8Ua3u594T0kgNcGX3q98vkPEZ7e16Rdif4RfrSDkaqkZ0siN-H7YEmRc7h911t7qkUwtB5yqNY90aSRlzw-jZvn-N2IEIkaKv4zMzm8D74dQz_2FpR-LEcNY9-hLhTnVyiONnwKCMWpIz6eoyVlGpxypP9SXl8wXzImHoxAYG5nxWPiUU9LFKGODRCq4b6tyd-s977pWSq2N3xZOIXJn8TczKoipll4V5pSWVyVlMA9xUOE2m1pXTPOCZG91HT77tisnJb6UxO6g5Qj8Sels2CwpNn1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC5Vk2IHU8hQK8aAdJfSg0EuhPxhCU0rudz5X-yufmBd5d-JrEw_OVB9bh1LKsShx3Yq4BPKJN3uGk_OVJ93cBjLKLeEHJlObquyHsa1IZYBiB8oF83n-F3xXX9z_Ot3OGTlK5diSwHbTZvDvFyvSQTWom3yea74vdTBQCHeGUXo9WCyKb_AkTgoyVMgHWVLEz4z7m_TEQc9j98hFLKxgNnM0mpcK7znznm_29yOoPoL0OFpSWP2FPU5rX6WoA5SdkDPGOiecN3T_6gxmsufyN7bAS1DeTh5u6Daom-q_BnKnqQehOkdjcZlVFuAjj-IjEEfjzceioJR4QVpmagx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O61NZv3y3vtncTxLVqWs0c7NjwrqWWuEmoo6hBEPpTjA-qdKvaxkQ-_PJF5aPj1-ofi0WHbVoVOs9MUekH4bDku8_D7WVfzCoO41-2hJ7gqiRYumH-BTwMtpHRyvMjoppT3WJ0yY9gcTZaj7sx1rU4tCFhJ92fHSlWL7kW4i5j1I6gxbwy_uoUFMWWtiVPCLFy9WXX-7zaora9Es2wQjjkfmlg-wW6kCW8-jZr9A0W1KhPbLSDQfStXMaJYQNqOfUcmbNoMLW2pUiNqfZjdPy46NfXL-it6qeh1DZRdA1_4_4JsCCw01-CVkMjSMcbgRVWj8I9Gl9Ei1QdQyCd-Buw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DYHtXD-S6yAR-H7ZsuXLXILYjIWx1HYC7q5fIaaAmXvUAdaoQ194IWUPkGzYUd_f87cLBIpty4jnI4FwNj6lswkXWhQ-3KeX8uKJhG_xAScwIGwK0XbpJY90nVfUXMI8m6cFdoarJkBTdbaLyV1aQ9Tzq_uubXNyPEkFIsWam7Qz2kxxkE3aWlv4Nk64D4BbHDcO2D-3Qy7sXNgxABuSyM2PI6txLNgxUnmvEKi7wQ8eOtY17wixhbN0vGYSUD_DDrWHqV_KeX3HSTowC7CxcnhN3mucjafEsdhiJYh-CkKW_eIPKOFCA64rFCf25W6DlCk69FiDM5lLZjbukanZyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DYHtXD-S6yAR-H7ZsuXLXILYjIWx1HYC7q5fIaaAmXvUAdaoQ194IWUPkGzYUd_f87cLBIpty4jnI4FwNj6lswkXWhQ-3KeX8uKJhG_xAScwIGwK0XbpJY90nVfUXMI8m6cFdoarJkBTdbaLyV1aQ9Tzq_uubXNyPEkFIsWam7Qz2kxxkE3aWlv4Nk64D4BbHDcO2D-3Qy7sXNgxABuSyM2PI6txLNgxUnmvEKi7wQ8eOtY17wixhbN0vGYSUD_DDrWHqV_KeX3HSTowC7CxcnhN3mucjafEsdhiJYh-CkKW_eIPKOFCA64rFCf25W6DlCk69FiDM5lLZjbukanZyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=h8aYumLZxFjkldLzP_Gp9SA5YDIFqLYuthn1yrMYgQKFQlA33_mkimAJ2fp_5dN7jjOd1cFAUjmM1ld0zokYeSpoVIP-Td27frMHwHp9cRzixtn8qCRWhznuMbedoanNaLNuGlyge4THVxGuksAP4jdWX2w8-fXdmVDaHSAvNnhpeahRjHqJmwwPPE2-45Cfe2XVWL9Cv_tLSuSX41Ju3ucILZgTV3XSsANqtyZVM3fzrQ1i5bplL0zna_55Vf_l4WkeWHrJTVfKuGiDLdqJBQX5TmsYeeSRx6YD2uT1PrJxQD2rjvpyhcg-5e9UmcyLjpES9iDvy-m2bE7bZ0PX4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=h8aYumLZxFjkldLzP_Gp9SA5YDIFqLYuthn1yrMYgQKFQlA33_mkimAJ2fp_5dN7jjOd1cFAUjmM1ld0zokYeSpoVIP-Td27frMHwHp9cRzixtn8qCRWhznuMbedoanNaLNuGlyge4THVxGuksAP4jdWX2w8-fXdmVDaHSAvNnhpeahRjHqJmwwPPE2-45Cfe2XVWL9Cv_tLSuSX41Ju3ucILZgTV3XSsANqtyZVM3fzrQ1i5bplL0zna_55Vf_l4WkeWHrJTVfKuGiDLdqJBQX5TmsYeeSRx6YD2uT1PrJxQD2rjvpyhcg-5e9UmcyLjpES9iDvy-m2bE7bZ0PX4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Nu6wsiZFfnIw_GV_QUJYm2qsgQLVr-q6X-GFNnqYMpe4b-ZzZRnV5tcqkrgHRUVRzI0d3g-biDAbTfI9uolj8qX5QNwX-Uznt4Nuu98AepTdbjXkLNPBA-3VeKL2_tCDvHUALNlYQSZmDsnBtxx4Hh3vh7UdUO4bnsRcK-0zYhN9LivHAmnCDFiCJJkN-6toZceUfVZLasG5S1fsKuLZ_dq7NY6AN2ppUmcod7hTe-YFGVGcP2S1MPDKK6Y7F_SS0M-uqsXwYzs2PrKeGCa5iLG2K81qdP5iZEkTRQPYKb-IWdPCWmy-zcfc7dsH2qNU2s4TygkYDHdH-WjvzLEj4KbblAaRCARKNjpcC4TrnftSzZIhzekoV--UGiGKgrl-eSV3L3NbMGde1AToTFFIlKBG8ykMAbrpTHCHcruMFVkjqAC6MgImAjSgumFfi1QJKRcF1Ug_MSDqso27A8gTlTHEMt5dC9fJ4h9jQg-ZGHil82NNcSrI2e8YUAmdIToeHxITCsBndHEx2QjwQdK5SlZ2XcsckivgNyLXwfxgQW2pPeMBM0R9crIxbZTLB0po9CoU1_1uEl-iw8kKB2IqSRoTkg1v-QWB8wfc6nPo2H0PmVX3c4RUmwJ82FZiYJsDGWBlk1iAcWckSAm8WJDUdoIS4Z-RiLdkaoYyen6Fn5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Nu6wsiZFfnIw_GV_QUJYm2qsgQLVr-q6X-GFNnqYMpe4b-ZzZRnV5tcqkrgHRUVRzI0d3g-biDAbTfI9uolj8qX5QNwX-Uznt4Nuu98AepTdbjXkLNPBA-3VeKL2_tCDvHUALNlYQSZmDsnBtxx4Hh3vh7UdUO4bnsRcK-0zYhN9LivHAmnCDFiCJJkN-6toZceUfVZLasG5S1fsKuLZ_dq7NY6AN2ppUmcod7hTe-YFGVGcP2S1MPDKK6Y7F_SS0M-uqsXwYzs2PrKeGCa5iLG2K81qdP5iZEkTRQPYKb-IWdPCWmy-zcfc7dsH2qNU2s4TygkYDHdH-WjvzLEj4KbblAaRCARKNjpcC4TrnftSzZIhzekoV--UGiGKgrl-eSV3L3NbMGde1AToTFFIlKBG8ykMAbrpTHCHcruMFVkjqAC6MgImAjSgumFfi1QJKRcF1Ug_MSDqso27A8gTlTHEMt5dC9fJ4h9jQg-ZGHil82NNcSrI2e8YUAmdIToeHxITCsBndHEx2QjwQdK5SlZ2XcsckivgNyLXwfxgQW2pPeMBM0R9crIxbZTLB0po9CoU1_1uEl-iw8kKB2IqSRoTkg1v-QWB8wfc6nPo2H0PmVX3c4RUmwJ82FZiYJsDGWBlk1iAcWckSAm8WJDUdoIS4Z-RiLdkaoYyen6Fn5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=l0jA8OIkkeipXULDVzBUR06giSa7a97QWuHWSaEQNImcEV0kf8koH3rBPP2V5ro1xwEiDuZRsSEbMJzV-P8hK-_IKwbM_dn84ch31ZGwAzLyJ1aVbTUv0jFjo2wF4NfswvmKps-2dK5uqNX9kWkEFjk8XbVWyS95EU1qbSr6JWs6Ygbyx8S9aoC7Jl7c7r06_TvNA1nYzeJhPe3oCVUv09OmwwB_ETTLvi18xTPfntqfOoq1E1Xdf-s-_FjpVf-DmO3h1M-20e31fMhnLLbTegle7VP7KZQpDFJBML38nNY7U0JLS3SBLJyOeYWND2uZrLKaIeKgwFnQNG0zb2fjpVmuL7pum8hF2M7yQyeaWzra6vizCV9U0gK-tUo5buRCVeHEkQKRX8gAsWOBrLfJjJBUKd7q0S8r_KGU-Gm2J3Mwh-zwHbhMG5Uu8cu9vhLlLADY5rRFDsHTkgao5kwwGN5RobTBDG9EoFiKMSmU0KNaRezuEfRB2DGjZKlvwNxWm_bk-Y0RwKiWJa8vjFu4cUJC2046Eq_LeuiZXzbMM7BcIH9PrPhBw-4W3CuhBm09aQSeLQaK3oJV7Tin4YmxdOvYDYSxB0ajUF1E4ol1Suk3xSFwhv6lY3OfKHSnS23krrP1y5-MrZ7k2-neiM0JLpYNc2g_F2VAgtWfK4AHmX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=l0jA8OIkkeipXULDVzBUR06giSa7a97QWuHWSaEQNImcEV0kf8koH3rBPP2V5ro1xwEiDuZRsSEbMJzV-P8hK-_IKwbM_dn84ch31ZGwAzLyJ1aVbTUv0jFjo2wF4NfswvmKps-2dK5uqNX9kWkEFjk8XbVWyS95EU1qbSr6JWs6Ygbyx8S9aoC7Jl7c7r06_TvNA1nYzeJhPe3oCVUv09OmwwB_ETTLvi18xTPfntqfOoq1E1Xdf-s-_FjpVf-DmO3h1M-20e31fMhnLLbTegle7VP7KZQpDFJBML38nNY7U0JLS3SBLJyOeYWND2uZrLKaIeKgwFnQNG0zb2fjpVmuL7pum8hF2M7yQyeaWzra6vizCV9U0gK-tUo5buRCVeHEkQKRX8gAsWOBrLfJjJBUKd7q0S8r_KGU-Gm2J3Mwh-zwHbhMG5Uu8cu9vhLlLADY5rRFDsHTkgao5kwwGN5RobTBDG9EoFiKMSmU0KNaRezuEfRB2DGjZKlvwNxWm_bk-Y0RwKiWJa8vjFu4cUJC2046Eq_LeuiZXzbMM7BcIH9PrPhBw-4W3CuhBm09aQSeLQaK3oJV7Tin4YmxdOvYDYSxB0ajUF1E4ol1Suk3xSFwhv6lY3OfKHSnS23krrP1y5-MrZ7k2-neiM0JLpYNc2g_F2VAgtWfK4AHmX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=OpQ3sMnMmzUEvbdL1mwD-CwSgrsnKpR9MagkLNFTdycBUUERTjlDYwHC9RwjTPtJ7SG7GvPf_B2PKnzpgyVn9Zp0HLtNOqVYrCWe-tkivMWWcQoTfe_Ni-pD7Jofwhdg1vn_jnVCqAyBDnmir-R69yN6Y_Si_ehaxBsy8n4w2DZFczjUsGD9JjCF5ZZlDoTIANEe_VycpeBLi_wUvN51xvjcd2AqDMV-rJ5RdEYjdx45NCw63M5Ct4X5Z1I0tq2NSPO9hZg3l4gsxnMd2hBicYQystiT4XQ2YJI8GMlao8wP8lbChzLvvSZbICTdl7JZoPaLtPqgiTbqsPv2pVPxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=OpQ3sMnMmzUEvbdL1mwD-CwSgrsnKpR9MagkLNFTdycBUUERTjlDYwHC9RwjTPtJ7SG7GvPf_B2PKnzpgyVn9Zp0HLtNOqVYrCWe-tkivMWWcQoTfe_Ni-pD7Jofwhdg1vn_jnVCqAyBDnmir-R69yN6Y_Si_ehaxBsy8n4w2DZFczjUsGD9JjCF5ZZlDoTIANEe_VycpeBLi_wUvN51xvjcd2AqDMV-rJ5RdEYjdx45NCw63M5Ct4X5Z1I0tq2NSPO9hZg3l4gsxnMd2hBicYQystiT4XQ2YJI8GMlao8wP8lbChzLvvSZbICTdl7JZoPaLtPqgiTbqsPv2pVPxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLpB2wL5Oe4jsfA0ZRU6DqR-bivR2cgPADqB_4u-Mx_eDCE9j34hmCY9wmlnYHoax65A0UDGlvd6KY2TrKU1pAj417KsncMHS4VWXumi6os97nTvTE6MgNKSGGvvg4ieH9zd2b6VNI5JNCJy4NOBGX0i06BT9Xxxg928BWnegsUS0ybSrJsxXHeZe68LVnVDNdsUZbe02zAU93JbPW78ypSPlyt5cMH-KF_vwqCmilZp0PXMpokyuy6Mg27LPfxEwldd8y1QsJbabQ7eUQd0dLlBge090poKAoZqN3KHdKvVg8VtfK2VQ0RA4hSYlzvBr2Px5tXJfJXtxa5wUkwC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TsXvPVhoCWaVIvRX8HdQNXsmxiC2-RBaS7jGxxAJx87Q6Nf9Y60wpsY24sWlu8K8TyDu9il1HdZ1VqXYNejdm2hHJUCYeSUg5XpikvyMON1T12ZM4zXiGGJvwTLOKhG0YEtGkq7Vrj4ecK0eTe2EeikjqVU7Tbkig0mXVCR7T1kEwvFikr3n3MRbElgWGo9bneXR38xaKj3sWQFXfgs-NcTYZVVZr_MFwREUbowQVP_nS5jb5FCHfJbOYrlL2YJQjH_-qLCxa3kJ5UfuGjFX9AVwqUCLJsieL9_tsIewPXqmVDW3SfxTF4KhgiB8e6mYPxxRDLhOuyELRWsU-9dFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TsXvPVhoCWaVIvRX8HdQNXsmxiC2-RBaS7jGxxAJx87Q6Nf9Y60wpsY24sWlu8K8TyDu9il1HdZ1VqXYNejdm2hHJUCYeSUg5XpikvyMON1T12ZM4zXiGGJvwTLOKhG0YEtGkq7Vrj4ecK0eTe2EeikjqVU7Tbkig0mXVCR7T1kEwvFikr3n3MRbElgWGo9bneXR38xaKj3sWQFXfgs-NcTYZVVZr_MFwREUbowQVP_nS5jb5FCHfJbOYrlL2YJQjH_-qLCxa3kJ5UfuGjFX9AVwqUCLJsieL9_tsIewPXqmVDW3SfxTF4KhgiB8e6mYPxxRDLhOuyELRWsU-9dFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RL9LcmwJfgsY_TQEiRBcxcwnlbUbxCv6koDRNGhdP5Wsw9Vcq_WvJNpUcabTr3XyUQxpTUpyeAL1SV_0QpuzN1sHJS2-DpMz5pl6eJXjB_jbqHd2v3X1I0pQNXIwCFMfVbHZ0h-T4KnkCaobBlHeZ2wWPbpbzlpkU7MHBScqh07reSDS4zwSP20FcPkKtFu4Z_CNwSeEP8Di-9t59ZxKZ_pmljIVgskHaHvigsO72NcrZOKaXq3MIKsxD04PvcsgRP-9YsjFKoaYTqQOdQh-bHBVtPHcn3PlYj0HANiojVZKuOhRtZuJ4ee_4c6SYrV1CXumEbgR_UHZL70dI08mLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RL9LcmwJfgsY_TQEiRBcxcwnlbUbxCv6koDRNGhdP5Wsw9Vcq_WvJNpUcabTr3XyUQxpTUpyeAL1SV_0QpuzN1sHJS2-DpMz5pl6eJXjB_jbqHd2v3X1I0pQNXIwCFMfVbHZ0h-T4KnkCaobBlHeZ2wWPbpbzlpkU7MHBScqh07reSDS4zwSP20FcPkKtFu4Z_CNwSeEP8Di-9t59ZxKZ_pmljIVgskHaHvigsO72NcrZOKaXq3MIKsxD04PvcsgRP-9YsjFKoaYTqQOdQh-bHBVtPHcn3PlYj0HANiojVZKuOhRtZuJ4ee_4c6SYrV1CXumEbgR_UHZL70dI08mLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyC1rZZWc9fASOtn8m2GB89TRJ_5g6DLiIFkK6YkyRju457LSRBRzy0w3IbGU79iLWFhd1r0taTNaxt4ogGGoaHSRF_C6KwuuiGYswo1OCALxnaTTh1Y5_IdhjKT26WlPkcQrH2_5Jq_Vlk2vEqY4fSMANwl80IL2DrWVKtWaLyHiDyKIk01vkvsZBxXJG8VVKfiYjST1bkmzXCi9jjn5uOSuKiS7_Bst2IR-nJU68dXpAgCIaZKmKscnz4n_escJ37jwQ3UyHGX99lSchggyIi3JKmCl1H6SCq0tKnaszNDOYiTnMOaXhYd42wiiLcBGz4osRJUZZwdULB0dUa3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxDmukZHZ7nOaYj5kTXxuePiTFcmSMZzk5rgRXh4pslUSmpC5Wdd_k4REv0X6fZxotkT7HPgKiClXg0YrQmt0dUdboy3buwRoFaIeVWsR5tPxnNwlHccKR_LHGvoTryxBroYP8VsZ4SajZuGUo1K3FL_b_YLKrh_PtMUFU1dnfwBLpUVOrRRtCLPDL6Ill5pMAGCShwBaG1jkZOeq7vlr0efEGjfH1kzPeHbxQIbUskdm6PKvj1pMoA07gDNdTVyFr88z25lNForqv6mwPh1LCJLUCp_hGKSomM1TH2aOeVpy-NcfrvHKzmujViSnpmDCj1XxwWmv1TTED2_3y-qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqWZYlPaMuZflDWQJ5ZFNAzo_VQ5CpZqqIvFmJ47iiM6QU_w-dMyKbCpK_WtstVyi4_SB_ZYflPLPxUN2PRY4lv6u2mcrymFfRWixo54QJW-HlkxDeXp06zpY1478DPSerpSQfY22fcVrl3e9OADJlgyD5L6AxSWQsnXSwFxZq0oV7p0JNEVzty53Te_eXeF6VDql3owboVE5j8wIQgTzLWy1Ys8OLMXxiVKlTgcumpSKOhpZhWOUfRrgqeQSM_mqp__JNfDIV8OLxccEEMIJBsfnp8rdigFHq3EHNkAPiaUc2vOOA8VFf7CFTLIev5k5NhLb0M0l1TA3Rdch17jgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjdpSq5O58gXZRQgE-U_kQl81S1Ck2FgVe6qdWMS6ygeu01xhEtk9fUcbWd4DiJPlYl5J0gIWf7XgXkSWODQ0uxkW6rchc9LTtu8fzzT0Ixy4p1HqNIjo4F91Gkx5yUYZblDXg5naYOHZEoSv411evFeocIoa7ZbLLoF5b1kA2j4pc3SDgE_waVkrOft5Qq9bdhX3kpc8ThER81MABX_QObl32wQQCuYk9LqXggUHdVv9m90LmNScMhkRkuEx_IBu1GouI-r8w0Ao7GHCnfJgPHnrDoI-cO4mglihg1EFUr1rH06D_PFS7Qt9uieJey5hKTTzbA7JkUhSNImGM8VDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3rpTOPzkhoFpguJuvREebtqrqExVzuoF9sugYfQ0183x3AP-T6O9HyY1cx2RJ_9dalJl7lEVJjM9P_yQWd1j5kmDaODNeKMoexd-6wroC2Cb7gpmWrTPv92NTqH2Fum1kRtPI6D5XhISLOMFMOfQu3_WHjWtG2ptL4dc3W141DjSXnMwl5VclmwvXXJjPGjsdNBEzxp6SqZ1qgnhpBiuNIsrWCfrZRkQE2CI2raE1pNwdXX_hQ_KWFxtQXTmif2g5feKS5Tk-eCkupgtdelT_Of6cLRcQ6MdP2q3RKumK_tIx9__Y0CKTzjA6zeRbEjbdLHbIyJxRgAa2pIfh3Kkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtLHVtb-zfJCUCGzxGa19nJORQiW0dYV8cx8doZosuOPvJMyqdxxeh5FiAehUT5BSyoemXH77poaafZ07FgQd5nyW9Uttqg80HJZaWJOWkC11_bE7_EQD9S0Cz2IdUnxJh2rk1djmQfb3Cc2mabL6TurofsiakGy2ZWlbkZhYR6LCI1v49WtRC_b4YYS4okuuffUBdOrcr-1Ko7QXk4_uSUU01dDNAJbMaPv_FpQ5lxP0dvms1EUPEy5_dcQ79KCCjz32awTsohedIg5x5flHw7fJwrfSRXF3ugaCVorkknRS5uKQgMRM9DoWjYBFmw8bqbVsl0iWhA5KmvGuS0Vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnQqOZQRxu5_6Xt1UEMSxqV546TE8L_PBndBGfbQjwElEvKS9DBl3_-zaYOCC-s6hcDv5sMKbXsLemqLqvnfFsr2LkWksZQTI3O1CNHuJeTpeSLXCOxRb282mI7RMTRNH4e5WJMKjjayQpVIwA4iRlm9veTMduwi0wjdPzTK-peyX5gSI5EibCps5UUOVieNtW-5SuowTgcirzCjDNVmyKi0u5pUBXQqgkkcA63nx6IBlI3fP1Bu4pNGepLSxph4C3oORgQNpfNnJR5h90iovqdMU5GGPFAqwkdGtNSdyQEz_Lf9wsdltWY7A_GmRsdXej-zRawvqj55q-WNVPSASw.jpg" alt="photo" loading="lazy"/></div>
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
