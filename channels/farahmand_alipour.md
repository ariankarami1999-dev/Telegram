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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 05:52:28</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHNFJyYEqpVwLM2egaouiUL1TyFuE7Y_47qqX7R0wyXgkVJSKHAZpcr7nhJ19UdVCLtHkfl5YfWdS4guk2Ux0ZEHeeHD4_Jc6KxAgfWUifs9enb8hK8sCWwCebrTYvqL_gv-auNTDvQ0c9Y54QyYmU2qXGOv5k5frqP8gB4bX-GKH45846raNxl4KSv-mfz1ocgQuI7PCNRDu9wxEb9QJcZzmXb5T0SYYQ9AOvY0g6KULqyvTUcoURKEUCkMAvdTGU7wbOnQ9svq_nwNJELuRKDcUmo4E00_FZHA5wkOC1lLVAfhyAG_4tMP6d-sncbMbRMvGtgeg4QDdVUb71DpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMrD2T0gpjUArt4MbfC2ITM9eIT0I6PMVpl4Ch34-2VBrxmRC1xU4pxWi3TQ5zGeYpPgxYIXwZqhIUgTF31pmaLuz9PGszENveY4Iqq0B_QtP3pjGcqNyX-g8-zSqyD0Zq_Xtsjtwwu81CCwGf20proS-RgvdkVLbhcL4fVQ85lAJbV575EEqLmIpmFwB5ablR-Xe90rZeQhD8Quf1unI0lbIgSm1DDmlt2DJckFIZIfk0CBPYARFIg4EfrpOaPitMOSoT0kYRi3CfbWd40dCBMPF8vZBOXNVEa0MtB3fos-4SAgczlkZoQQ0AGV4Zs7n-GAzlMljTll7NO0w3pS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=T7HLoJm1ztJsMbbRIDYJ8sV9EDDA_uRgTJjnGTzxTOfuVHFgikzRAal1YYWs1f6wEgJzkxZkxnJ7bDQjAg7jrUlW8MRG71gl2FTK5ebOMsWDG4M0HDukyrcHPwbUdFGSwpvAJWEvYFVSK_uUUhMWKP7nHQL0E0ivQvFWzU77Ltx5Erb7oWWx1VlidmNTDPpUxVxuPjqT4xRlHiKcplKG8ci7dyIwN5wLgEaijAconDqly74bgmexWMGimjelIeNNIQ0jrM3htVi53iB2n3uzBZ_zCwExlDcKoC-aiN2hg_hNuYAW1N7YVZUn9uB2bbzZ8G8HbQeTL25UwqAd8puxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=T7HLoJm1ztJsMbbRIDYJ8sV9EDDA_uRgTJjnGTzxTOfuVHFgikzRAal1YYWs1f6wEgJzkxZkxnJ7bDQjAg7jrUlW8MRG71gl2FTK5ebOMsWDG4M0HDukyrcHPwbUdFGSwpvAJWEvYFVSK_uUUhMWKP7nHQL0E0ivQvFWzU77Ltx5Erb7oWWx1VlidmNTDPpUxVxuPjqT4xRlHiKcplKG8ci7dyIwN5wLgEaijAconDqly74bgmexWMGimjelIeNNIQ0jrM3htVi53iB2n3uzBZ_zCwExlDcKoC-aiN2hg_hNuYAW1N7YVZUn9uB2bbzZ8G8HbQeTL25UwqAd8puxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=ucztXmP6gewLUdyJHsAOLMa4IsawTyI-wFvrgrfCeFCGRMhY-FOxZXD3Fgw8zS03MzdglpPaeiyPMOmQbW2ipYVaHHPavIHR2VZdgm-MM2JemVyZyd0JHIRkxumQeV8eWcvCrAWBvDwqwFl1JxdUPVKMzBMRTGvKRpldT74W0y9moMM8h1wxxxjHHqJ6X8g1o4It1H6_JTcv5yfDg-2dsZLBnnHmemM3a7OaPAHd-Jjvja6Wu6HdXzwwnu9GOVihKVhRQgH7Eg4l6HGwkpxOgcQuxbBb5RVfLYkE_aCVmvA4-OXWmOJ04c5KbTBzJFiCfUHR55N0gPZGOEtoO27X4T9G0YIDe9qDkF_whbGd1YHG3BhWo7euPkIjCdr_Saf6Fsjuh_j-Mlt9UymB9upZgdpR_IIL4N87nQ8-Oqu5V2rQpDV8U1MrG_kqjaRifLgnmtXg_SSThpMIeZI4mTVG-wW_b42PuRa9xQmpT3IPW73y9w_Qn4CTSW-yZJaUlUSBWrRP_TxBGvM1wgUQcu0VYQwWrpM_IGAOuZJ-YclJREK934M6zs8uOVK6pZtkcDsrycEZy8nzzZPB3RqysPvC-SFhQRBDY_tHdX_SDuuysfu2IVUFdKpWwTaWI4VH0oFpUKDyp0H4wbHr6YpsmvhQlgrTp_qKU7C4lw7UtKddhpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=ucztXmP6gewLUdyJHsAOLMa4IsawTyI-wFvrgrfCeFCGRMhY-FOxZXD3Fgw8zS03MzdglpPaeiyPMOmQbW2ipYVaHHPavIHR2VZdgm-MM2JemVyZyd0JHIRkxumQeV8eWcvCrAWBvDwqwFl1JxdUPVKMzBMRTGvKRpldT74W0y9moMM8h1wxxxjHHqJ6X8g1o4It1H6_JTcv5yfDg-2dsZLBnnHmemM3a7OaPAHd-Jjvja6Wu6HdXzwwnu9GOVihKVhRQgH7Eg4l6HGwkpxOgcQuxbBb5RVfLYkE_aCVmvA4-OXWmOJ04c5KbTBzJFiCfUHR55N0gPZGOEtoO27X4T9G0YIDe9qDkF_whbGd1YHG3BhWo7euPkIjCdr_Saf6Fsjuh_j-Mlt9UymB9upZgdpR_IIL4N87nQ8-Oqu5V2rQpDV8U1MrG_kqjaRifLgnmtXg_SSThpMIeZI4mTVG-wW_b42PuRa9xQmpT3IPW73y9w_Qn4CTSW-yZJaUlUSBWrRP_TxBGvM1wgUQcu0VYQwWrpM_IGAOuZJ-YclJREK934M6zs8uOVK6pZtkcDsrycEZy8nzzZPB3RqysPvC-SFhQRBDY_tHdX_SDuuysfu2IVUFdKpWwTaWI4VH0oFpUKDyp0H4wbHr6YpsmvhQlgrTp_qKU7C4lw7UtKddhpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDkJ5C5C5ybZ0LxvQH15TP0XsJ7PlFO68O2dXvi-b7TAN2aRPI0PUrPQ60bALacq5Kea5LMA4-EzpiGdLT8pJZavGOoasd4GUuSoWmsS48Y2L1SfAxm8r2u37SQg6VRFcReivbPZJIxqvLx7Rr53BFsbhRWKf9L27XjSKozZkfjowmAf0irwYIPd8_kJFJTnw0JM-BPFSFVqSkkn3fFGAj-_dzfoj8ijH_JFnMhvYVq2LB0Y23KkeYE_cjgfra7zKfIVfHbgsOmiV4AY-qTWFaX2QFNd0UqzOkT83Mf7y5fF-wwPGqHv8-GdUqyOPbioJhYXU5xu928RAz7BiEiO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXbben7ZxyMfsLKU-U0FzbBIhqiJ2NRbFUO1L2uJeTkHLM32Xt41cAj5SpeQyIRnekvqUG15eULeh_Ck8yrTAVfoYJo_jah3te8Uqv0HST1AkHsgecZO1irzdrai2veDv2L3m6Nw7tGaHJUSdahVJ1wWqqV_rHO4t75CCW5uogQWPeeq_r1zqWjUtGcIanCxwXer0A_uIzJb5JjLrg89q0yYb0wdYyzSs7SszyIPQ1Aw7a-u5u5DD8pQ2reGSNwnLFZlXy0dwjSRGR8TGwLJ78b8x2520Ab7GcIm5xrN3hxwj2vGGsnjm-Ntlo1rzptSIM7ENMvrG7H8eDFRKViyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKsCt8Jl_kfcl7ji9Pocked_kOGhXANKaE_KAeFfrLNTMgGydqXqzt18aP2N39bIjOqzIC6vxgyteyxEsKd16y9Xg9Q6FctJEUkPFwdUv0DLweLxEqQiAXH6Emd4Da3cKihk8kzVoN0ltpqdLfqxuXurSf_Szo7utwiKgp8o5Xj6P6UHwfNRyPxiv1CI6MWwQ-YFGiWMHr7HKpUUjyB1RoqMmWmpZGbe9jM5LKwgWNBaUD24gkYqkZ1ATAmtoM5hjdndJliShYWP98y-Y7fYfj4ktS2Mc0zdbLETObTY_aJpLQBQEeVv2CthtM2lrBeZ-7Im1XWaB95HD4bpfdOuaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=icirUPp7EnFh5VEfgVACiYv0DIEPVGrPhcM7h8JMzJ15Q1E-3DvAIeOBGNhNVuqu5hApAVSY2VODmcImj9z9O9bnL9Na-Pc-6nS2CPINjeIePja-XXRwlg47lgzUL_DmWiHcME3_yr01-rk0gmGv9qJ743t0WbJUMjE0Wpj3xzVNS36hBeUWx9XzEPEJIZJ6Oro0fZEAV391zooYOYREfzA-7ejMWpcDJBtsbZahk7iSbJJaMnXdi_Ji5fmtfkzDF2JmSpV_QB0T6eKHJHZLPsXHGQXBRHsdp88ukFKzh3aiWBJMLMwaDn3bcxohmzZ3obVVF4gRPyEp82-VxQ6LhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=icirUPp7EnFh5VEfgVACiYv0DIEPVGrPhcM7h8JMzJ15Q1E-3DvAIeOBGNhNVuqu5hApAVSY2VODmcImj9z9O9bnL9Na-Pc-6nS2CPINjeIePja-XXRwlg47lgzUL_DmWiHcME3_yr01-rk0gmGv9qJ743t0WbJUMjE0Wpj3xzVNS36hBeUWx9XzEPEJIZJ6Oro0fZEAV391zooYOYREfzA-7ejMWpcDJBtsbZahk7iSbJJaMnXdi_Ji5fmtfkzDF2JmSpV_QB0T6eKHJHZLPsXHGQXBRHsdp88ukFKzh3aiWBJMLMwaDn3bcxohmzZ3obVVF4gRPyEp82-VxQ6LhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Pyr6DFICdFfZoYth6e6DNKaFPLBHl4LHj7dlDfKT5ac28kD7k1Vr8W0XlBw8zit9kaKj7OZFrOvpBtkN10nr_kNIrci75ufQYuXja_pIfO4XwTo3Ap5k8OqMSf0JfvCkzJTVuIPQxReovxFyMYqqPQlorDxXhPSwbs4-wEa0VlYbbl73tibtmR2Lhk5CqXZZzl2vNS98Z4Jfv0BeyJXE9QsiY-uW-N6-6h9T-9pTA6TVIh1ae2a9lnp-Dtjd1KGuM9rrJJ1DuL6OTd8Fjy_Q_R5j7az3eterRIBpFCP4dsVyGd4hQ0oIEe2VYziFQHBGOHESa2KDB1IGDtrlnIs4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Pyr6DFICdFfZoYth6e6DNKaFPLBHl4LHj7dlDfKT5ac28kD7k1Vr8W0XlBw8zit9kaKj7OZFrOvpBtkN10nr_kNIrci75ufQYuXja_pIfO4XwTo3Ap5k8OqMSf0JfvCkzJTVuIPQxReovxFyMYqqPQlorDxXhPSwbs4-wEa0VlYbbl73tibtmR2Lhk5CqXZZzl2vNS98Z4Jfv0BeyJXE9QsiY-uW-N6-6h9T-9pTA6TVIh1ae2a9lnp-Dtjd1KGuM9rrJJ1DuL6OTd8Fjy_Q_R5j7az3eterRIBpFCP4dsVyGd4hQ0oIEe2VYziFQHBGOHESa2KDB1IGDtrlnIs4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwLtWHw5_hISQChZ86HTRxpxZGRid_ZPq-UZWWIeyZqHhmq4Ip7g5wtxbAjGOcy6knJEQCYhER2Wj_wJdNDrDJ3p0VX09GVfKwwH4DJKtWnGXzT7ZdVLOYX6-_85n34BZJX_lrX_R07EHZMvKOPhNQNe7smnwyVlEQL3AeDOlnARMtUurKcVaqKgPdqarR5EOjBpzkd9qtG5hMIX7CgTbHFODB6qc8bgHveZmvHsaziXB5SH4Dt_jWqvP9AkUBdxSGoQPvlUfFqBJCIyNOGvrd7KR-u5p6V7cZ_dvxWEW-UDq7GEJsQmafYa8uGIdRfLiROaUDKXx7zD1iBixbuw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=QZH7S6oi7H86-cXYSSqhS47zzn0q4hDESZG2BqJsP7hsAoCNZIC-4YOKxZo3Xgmhalt37XLyxD5tD6fI2msMz2mXwKOUHsJJ32ZIKYyxiljYFnfrNl9cDFLGWRJ78HSHVMtG0qvRSXTZAg9ZVKN-WdOJMT2v1UgjrTkCNtbsm2xIF9xayq8NiE7Xgli-Kr4s-LxLp7-NDLey1ObE76ERwZ7aVO2IYntTtnZE3B2CTAeSLdQaXmrX6T-ncBuNi_2LnCTTesNkJvkfXAOVVgj4A0v2B-KN5cjKGgASisDKN4Wl12j8ZdJOKEk6iTO_C50D9bPsJQxDTtsBlNaMviTUizxRTlQWVWs5kZ-gHM8DCgW3C3LoCu6eo1r-oGD8-xdLNCBC4YESBUr_1pljfyfQzmJlRE1IJ25Zuv7tJGZW5dlePk0qqKpBh5YlzFjHkU_vCj32RzhD9Mhoj1cs_RMrEEBADbbN_CPlQyVb_exxEdSjUHiOj2CDMOZpE791bOWb1rJineQH5_G4DpRgzUEyl2eHmqfJmIeDmIsSJc21ON7JcyTRmEXigepnkOQIsgTyJQeX3cItVoRDcCnADRZ-Dej4l1PHXmOBGWPMOOaF5hKznej0GNz2aDgdwQhco0FYxGtMMvLjbW98dXxWH5uYVTQO00ArX2HwJ4fggPbBrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=QZH7S6oi7H86-cXYSSqhS47zzn0q4hDESZG2BqJsP7hsAoCNZIC-4YOKxZo3Xgmhalt37XLyxD5tD6fI2msMz2mXwKOUHsJJ32ZIKYyxiljYFnfrNl9cDFLGWRJ78HSHVMtG0qvRSXTZAg9ZVKN-WdOJMT2v1UgjrTkCNtbsm2xIF9xayq8NiE7Xgli-Kr4s-LxLp7-NDLey1ObE76ERwZ7aVO2IYntTtnZE3B2CTAeSLdQaXmrX6T-ncBuNi_2LnCTTesNkJvkfXAOVVgj4A0v2B-KN5cjKGgASisDKN4Wl12j8ZdJOKEk6iTO_C50D9bPsJQxDTtsBlNaMviTUizxRTlQWVWs5kZ-gHM8DCgW3C3LoCu6eo1r-oGD8-xdLNCBC4YESBUr_1pljfyfQzmJlRE1IJ25Zuv7tJGZW5dlePk0qqKpBh5YlzFjHkU_vCj32RzhD9Mhoj1cs_RMrEEBADbbN_CPlQyVb_exxEdSjUHiOj2CDMOZpE791bOWb1rJineQH5_G4DpRgzUEyl2eHmqfJmIeDmIsSJc21ON7JcyTRmEXigepnkOQIsgTyJQeX3cItVoRDcCnADRZ-Dej4l1PHXmOBGWPMOOaF5hKznej0GNz2aDgdwQhco0FYxGtMMvLjbW98dXxWH5uYVTQO00ArX2HwJ4fggPbBrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5l21qnWUuE0ubqbRoE9QWPC3YWMesYusFHAB1JZltgZK61tZsweRAQLzi9Ve6Yg-yTBCIL97xDRZA8Zs2dX3B-rEECDcC87AfpVcSKmqZB_ZhFh6TGa5ntu7NGPmAjT5quNWiXVbTm7o78ybOMN3JHFPoTxmuqV3aP9SUWmNRxbVmuglAof4BeLyzjoqKPz82BJ8ecvak3Gl5GGOyEpSW9PxI9oePJCgoogNNuFDaNoTMPF0Yivpnyyi9QQi4YusxsF12S48y1HwGWbMXKqaf_TL3FoBoQkicH_4evOHTfGm8mrvXNIzDvi3ZOZ-ORLraT3B-95CSXaFMayRlsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ323fh_ZI4goosekrbUeky_cTExGCNCfpicV5PFuNxmipKcPA3EFwOyyFfGIxEJspPlMmvmU-Jwl9Ac3Trst-ALK2AuSOW5svsZfq0u8Mj4Ejl69gUeThPdA2i9wvYiyq-qTqWQ18ePS2WJIEwDID2hzNkX92k1o-M1v7V_yDBkBpTvBozoe_GgjLe4pMTBf-wB1-AmqFBl0T8oTQDVMtt_WiVFHahQd2WRMxHo1Utv5ugLyEpt004AEu6xfsvmPTxBkPBF2eSfcadSik-NI_wRdJOwdGjsGl7fdqyBt5CmQLjbl3oeM6Cix9VFEln1zx2gmTWrrMXGZIV45AWlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=fukLE18mK7h54loKRH2uu2h88W_dxhoSj1yo6VimHi-7dTnIk5FSIPz0zDkH4atfKBfkAHAii1k2BxsT6iwjHn-rHJ4GCV8fuJsfyGv-FSLlHR11Y7KRnLTfNfwQHe9W-Y2tI0QOJLbEHvA8OgdIIIhWNMRG7zIDSE_qgGsmfyNMoOwjsrQt6-d6FtlAYEL_U0iBY7DhmSeAv4P1MC8UQnMjL1bd5W7eO6ysfDSUNwrdD1McLoXGJ4jI-Q7LOsFUFpD6oAhnAu2Qd6BdBhcZ5_ajlz6gr6-7zhIEnY9GPMSm9bD8aSnNAy-o2zrVoQvtPH6a0_BZli5iTRSHv4EUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=fukLE18mK7h54loKRH2uu2h88W_dxhoSj1yo6VimHi-7dTnIk5FSIPz0zDkH4atfKBfkAHAii1k2BxsT6iwjHn-rHJ4GCV8fuJsfyGv-FSLlHR11Y7KRnLTfNfwQHe9W-Y2tI0QOJLbEHvA8OgdIIIhWNMRG7zIDSE_qgGsmfyNMoOwjsrQt6-d6FtlAYEL_U0iBY7DhmSeAv4P1MC8UQnMjL1bd5W7eO6ysfDSUNwrdD1McLoXGJ4jI-Q7LOsFUFpD6oAhnAu2Qd6BdBhcZ5_ajlz6gr6-7zhIEnY9GPMSm9bD8aSnNAy-o2zrVoQvtPH6a0_BZli5iTRSHv4EUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DTTLAuOwYTVO7W_Vw8qW49X9QC008BgfX5fx0hTzrnn18a_6fuPwyRiMshaiDDQTAw6p0Tv-me4lyK9BbDjuaU3GhdXthJF4qvQM73MDsKYNLdqJ8HTRMKGJCRo81ARUAYxN2SE92_rhqDSrMfvHKMZSHqs5DccJQYqgbPVay8c48zzYVpApc0e3YGu89wSX92ikeJhkeCC4PLrSnsiyPoWDDsqsUw4c6F3GYuLWnb2S5A7yx_srIp28bbHZ_jRTZv0HHgCLHZltSBe9Q6MWKRb22kpk2uDmuvtgRDW8ryNjiktQUkBM2UlFKLH9TL2D9Sq_lAZDuabHPH8Y1H-VsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DTTLAuOwYTVO7W_Vw8qW49X9QC008BgfX5fx0hTzrnn18a_6fuPwyRiMshaiDDQTAw6p0Tv-me4lyK9BbDjuaU3GhdXthJF4qvQM73MDsKYNLdqJ8HTRMKGJCRo81ARUAYxN2SE92_rhqDSrMfvHKMZSHqs5DccJQYqgbPVay8c48zzYVpApc0e3YGu89wSX92ikeJhkeCC4PLrSnsiyPoWDDsqsUw4c6F3GYuLWnb2S5A7yx_srIp28bbHZ_jRTZv0HHgCLHZltSBe9Q6MWKRb22kpk2uDmuvtgRDW8ryNjiktQUkBM2UlFKLH9TL2D9Sq_lAZDuabHPH8Y1H-VsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=XaypYNnkFQG12niUAh4EV7pIWvt_Qzx5MpsSThq9VjfutGTH5sh7Yf8nWnGQmks4gNDkwD7gHQpMSaau0wLgQyz6e4s7gGVAKMzLrzfEtvH7NkHq709kN8prHHr2JaIOU_V-uFHiuKykGEgGGVnUJ9frwEsSRSnR9cCGYHawhXKfep9MTgIHHXq3muFNTZk-nS81eKPPqkofcnamrtZxw6pG65-ftzRoJ6y6zJGDbSRos5x61IAKdjRSH1Cuc6NNYGAnV01XW-CD6DcJTRk-lLPAufVAU57-tGw3pp15eiOTvnZsP2DrYWKVLorP6KStrBWomaG23SHzTClCe_1Pxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=XaypYNnkFQG12niUAh4EV7pIWvt_Qzx5MpsSThq9VjfutGTH5sh7Yf8nWnGQmks4gNDkwD7gHQpMSaau0wLgQyz6e4s7gGVAKMzLrzfEtvH7NkHq709kN8prHHr2JaIOU_V-uFHiuKykGEgGGVnUJ9frwEsSRSnR9cCGYHawhXKfep9MTgIHHXq3muFNTZk-nS81eKPPqkofcnamrtZxw6pG65-ftzRoJ6y6zJGDbSRos5x61IAKdjRSH1Cuc6NNYGAnV01XW-CD6DcJTRk-lLPAufVAU57-tGw3pp15eiOTvnZsP2DrYWKVLorP6KStrBWomaG23SHzTClCe_1Pxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEWJMTnE6R0Di9znNjcymDvtp-qo7xhRfQ_xyZPtfHQi8bNg9rcRQBzbyu7mb49WYSVgxtBXV8SzxiGspoTQYTT28b2lOo47nYT9b2pLCwKbvhpFS3H2dscgvJE1JGhEszFls5JtJlSmiONhgbBB372WNyQlreZaaNmIc2M9H0HNZ_rDewjQUzoXCBwUC85oGsd-3KbIMTM8i4SCGGw0tQwgsuDav0MW6ntvmV0K1vkBPmdB6hxS3GjXl-LyBBHHTndJrvdx6DPpV2mT4W4x796OQInsIPJVxYZXii1k8s2c0R34CHjWpBlfZHq_egb52Aarze4_B0-KpZGmiOOpCw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro3ADEoiAq-CahAfxQBXsyUQ8qN7O5jDxdHh9ywQj2rScJkhO9LMA0x5Tm_kme9cTaFTgAYEZDGiOFuDyz48BWKGvthqvhoUSwxMneEtapA1wU5b_BVckvyqNkQSH4izDm56K4-wW9eryZw_Vv0VvZ2IWG3J_0YRr1SB0w84IyYtFUi7EtEyxQCjqtG_vBz2NWYe2XCEnNEZUyR1Id5a_Z98L4_VwrnHShJ4iJ844TgnMdrrQLdzQjUeB3WL29HKe2da22L4AmcmV_HP8hktiJCceyAsLJ7I8DNzFlcRb-hqH8Wd1aiBwH3m-z-C-gV-gFFcE0DZNfRNeBBN_RVccCLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro3ADEoiAq-CahAfxQBXsyUQ8qN7O5jDxdHh9ywQj2rScJkhO9LMA0x5Tm_kme9cTaFTgAYEZDGiOFuDyz48BWKGvthqvhoUSwxMneEtapA1wU5b_BVckvyqNkQSH4izDm56K4-wW9eryZw_Vv0VvZ2IWG3J_0YRr1SB0w84IyYtFUi7EtEyxQCjqtG_vBz2NWYe2XCEnNEZUyR1Id5a_Z98L4_VwrnHShJ4iJ844TgnMdrrQLdzQjUeB3WL29HKe2da22L4AmcmV_HP8hktiJCceyAsLJ7I8DNzFlcRb-hqH8Wd1aiBwH3m-z-C-gV-gFFcE0DZNfRNeBBN_RVccCLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=II7gsbOER8nZtohZwdk1b_Qo8Pf7vsbMlW0dBor1eJzwzdglYp7JtwZ94eeI9TH4mBfwjzg6pnTqDIQtTRfLnrtFEecgtDy1zd7AAw8AygWAlWkQbOVSIraqt3dxq9uQpYyBYOyqIthM8djyC95DW_LOJAt51ZGDbKFKSGdPFoU4VFN_yNzBzdPAEaJQq-wmRSb-DUpghSMwLeDrCX_EFgr-15F_aCvuvnfQdDLCGn5PemazvGVm7MFiofLsqDSop-5Ff-59gc-pMjngu_VZy5SYjTz3i9CsJYIyk6sDzBuy7rRipEAROTH53eWpwzkHOL985qKz853XO2VZngaq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=II7gsbOER8nZtohZwdk1b_Qo8Pf7vsbMlW0dBor1eJzwzdglYp7JtwZ94eeI9TH4mBfwjzg6pnTqDIQtTRfLnrtFEecgtDy1zd7AAw8AygWAlWkQbOVSIraqt3dxq9uQpYyBYOyqIthM8djyC95DW_LOJAt51ZGDbKFKSGdPFoU4VFN_yNzBzdPAEaJQq-wmRSb-DUpghSMwLeDrCX_EFgr-15F_aCvuvnfQdDLCGn5PemazvGVm7MFiofLsqDSop-5Ff-59gc-pMjngu_VZy5SYjTz3i9CsJYIyk6sDzBuy7rRipEAROTH53eWpwzkHOL985qKz853XO2VZngaq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYng0H2VdiMk4cpNqnUi5e_5jnBz6Rc3Ilj4HEj2jqGluEj_OryajVrcP9vgvf9c_y52i1MZt5jKxxx1rsU6NJlklVSKX-Lh6GKue0-R7CmAutiHbZsaAMLDessZggoxVTyBvUMEn0AFX8ujdcniEt0TGSec6n-y8ei-HbyH8EqmC3fb8n742T_9dDJCh0jKpanBowkN8bP73Yac6_ZjgDb2sC7lU9jxc7-U9fT6gk9_K_tNyg2tHur5sPNFmqwXwSZfxqi2XX3gDNBjkZcs7rMrrqy8CUdWhgoa4Rgbr9_1Kg4vc3MK8KMexs45A2DBbk13SQCbjz3BgIH6n1HJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rQ-1DPrNSPWpTgc-khgwv2jberwEFCqrGEpSt4PnC-qUJyeSRiAsVMF3QjXzp1ecRKea-hkbEzh2vCZ-q2VjOPMBcOBP2uTyZiHV4W_IRNwHmgCZ4DplWmxy0tSfhDWVFZEPzoiA7YUosy867m56f5Tf0IVa31GxnEjQJelSusapDDl7qLTSXT1Iv1c_inNLX1bM4E8fBfDtCGHn4NCzi95pTuQt30-l2eg7rZJR-teyCPquE-ukDa6PP3o0xQCGjC0NQmullPzKdGV8QUEWMEj88MopotR0wyVDtBRTqhkwxnIOOT-CB_E81t-wkSMjqhbTSs0oMPFTaV3VQ3GspRDrnG1anTM0o6eYKjwuCNfLniVIud37VuP_KyA1k_MmO_hMjdr8yOz-ekFpsYayyvFyGYV16wosi5H2M-jPGbYunRhmMhdx8s5ENuhnJkr2U1r9dnPtmWhPTy6Epl9u-uwk6nsDHvRa4isqYU9UayUDChA6XYOr2RvXwOdzw5hWSunVqMIWn5ePYPX5rh4p5SFjyCfScSdDH49TKpkyR739vL_bgNmuZ2Zp6lCf2ShXKTOIf405opM1L5_EImaCXMrD_0du-z0TWs7aFCnxoOKOnlkbnBgavb4tFG61sG6YSJTRBYkHO3cwrbq9pmlBYnB-Gh_czdfucunuKbvMJpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rQ-1DPrNSPWpTgc-khgwv2jberwEFCqrGEpSt4PnC-qUJyeSRiAsVMF3QjXzp1ecRKea-hkbEzh2vCZ-q2VjOPMBcOBP2uTyZiHV4W_IRNwHmgCZ4DplWmxy0tSfhDWVFZEPzoiA7YUosy867m56f5Tf0IVa31GxnEjQJelSusapDDl7qLTSXT1Iv1c_inNLX1bM4E8fBfDtCGHn4NCzi95pTuQt30-l2eg7rZJR-teyCPquE-ukDa6PP3o0xQCGjC0NQmullPzKdGV8QUEWMEj88MopotR0wyVDtBRTqhkwxnIOOT-CB_E81t-wkSMjqhbTSs0oMPFTaV3VQ3GspRDrnG1anTM0o6eYKjwuCNfLniVIud37VuP_KyA1k_MmO_hMjdr8yOz-ekFpsYayyvFyGYV16wosi5H2M-jPGbYunRhmMhdx8s5ENuhnJkr2U1r9dnPtmWhPTy6Epl9u-uwk6nsDHvRa4isqYU9UayUDChA6XYOr2RvXwOdzw5hWSunVqMIWn5ePYPX5rh4p5SFjyCfScSdDH49TKpkyR739vL_bgNmuZ2Zp6lCf2ShXKTOIf405opM1L5_EImaCXMrD_0du-z0TWs7aFCnxoOKOnlkbnBgavb4tFG61sG6YSJTRBYkHO3cwrbq9pmlBYnB-Gh_czdfucunuKbvMJpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWXL7ju8cP16wJepLKbh-Qqzd0pHATJYgRdpG5NgLO_JjtouumgU3b39VflThanydkWPc3IAyhJkYP-qgjOQLQ3cBkzG4-h4g5ATZCcH9inmL7ZxCwCxGBVTFuzfJJitHixazT6_hah2K5HtrVM5JQpDfGppUv0PCgTlIln5adg6eteyLBExF3CRFU5qYiUFV8BkL8fX0cWZI6rELp4iclDNKzQ2Fa7i-bN3pzTfvNmCSUDy49Rl83f5GUm48r-ZqO-N0D1wyxb4hnrx4d7jnsets3oGDhjkGupDUY0ztZr4Zt93QcFRA3rXaqyiSP1_bozgJWW5Kx9P5apmuptTvw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=PkPApz8g6M_Uq5U-495x4I5MFUtiwX9JGf6RVkMcDkfYlPkgQrYxgoHC3HSdYBW9aYYlCJ12kQe5P18jWq_8UG7LNxwi77zCwY-Aq3nPNy8qRMCdm72V6crte6khPm-0o4H3D3Zhh7S3-_lTlFL-RIgUmZ32yrSEclPIG1LQOemmSoXVqqxEOYWHnanuN6U8riFzQjQLlhrsIGDRSuBMNltedgJpcK3LsyJ2CPcPRt7pkQ2gQ3gZxswN9lpbYzAxTb_o8ptLF4M6ZMwp06eols_yxZ2LUjSOGFl6G66f556mngvrV3ZX310odwdRahPROck6R0iZPCWHvjT5Y-hJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=PkPApz8g6M_Uq5U-495x4I5MFUtiwX9JGf6RVkMcDkfYlPkgQrYxgoHC3HSdYBW9aYYlCJ12kQe5P18jWq_8UG7LNxwi77zCwY-Aq3nPNy8qRMCdm72V6crte6khPm-0o4H3D3Zhh7S3-_lTlFL-RIgUmZ32yrSEclPIG1LQOemmSoXVqqxEOYWHnanuN6U8riFzQjQLlhrsIGDRSuBMNltedgJpcK3LsyJ2CPcPRt7pkQ2gQ3gZxswN9lpbYzAxTb_o8ptLF4M6ZMwp06eols_yxZ2LUjSOGFl6G66f556mngvrV3ZX310odwdRahPROck6R0iZPCWHvjT5Y-hJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUMgu1qUkB1foDbG8Soa7C3VztL6Xb7rFyG7NZYz1HtkwV6FqQBNZjUTI7N09OfIm3H_puQxsvFgs1SUhx6T4dNC-zK0wDMmM74XpowAz4K-nKehcm5eP5RFKt7CEIl4DDEi8QWNHy8wu1xEOd13w4o0eAsxPBEksUQgReWabwSRyvXLRjGZOcKVWd5pCsBJ6R9MQvOOKR12u1PHDO-YOy3KMLAaZv8tWuK1BhZPNjxYk62PrhWaPSCVloZ524Z8TdRCI0dr4cXQ_SO8SHJ5ZBtCpH6WNrhfdA0wHHhlLYgPivij5ivhw4kPpKX_AyiwMye9GPOk-c0xP1qhfjDAjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU8ix4drWf3yCAx6m7PsePzWe2qlLwO1-tVcJ5pDJzJpqhE9HysgsRV4pW6S677GKJlGAPLhVrOVDz23QAS0__ykaZQ6-VV3P-ML3GWVUqWmou3lk8bbQCiu-xkL7dcTHs9N8VLTeb0GzkdTa57DHoIA4NTSgkI5HIeXTQfH9HgVL4uzuURnBNRQj1qXiB35JJr2pREqIc5eS2HKJ0VU8tnHXquYcE932nm8cMkNALwBZjZSlxB7AAZkaTMZ9aoTwqHHeNNQ4oEv7i78PvwrcjSU61T0qEmZs5Dh2MYarYCeu_CXtU28avg8T-nizkdaHFYDAENq_XTtUBVMAYk91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEAenMcyWa6g5uSypFWUUV47w1onsdBbgF7qVzvGsT0poQ2x02zKi_pWrdM1s7sB6upmVhohUVqIQLtnkMAHTLHnyNsZB2YVgZuLa_6YkAti1awpnVCYdJePGNbGVn0GXbz4gzyYMwwIVP4qNZJTC41mdUD-apu5nJDowUwXvYK_UulxySfq13wQ7yT31PqIzcVKW25KUk5EFo-C8eZTBjMNPpl8FgXMI-G_7rROLeQqzHV1djDcpwKEjufSVhxxn1SjQvBOyosTmS1g8dueiv4tqoPwweEORBN9y_hLm3fJUXTGGjukwfMNHwwMwowX4gpZEfXfFc80KG0cXetsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=t-0P1ApvJxJlNyEUNCm1Kgz_PbA6aEDzhlM1oeK0MpK3XW_HJTifpO3zzg7PGJhToQ5Id2YJ2QR4jmCBK5UgBuGbiZT4bDJAJpw2qs9FXjkxxmxeFnhNmzNziauBZ6WgZGEOJG3db0zuqatAjYo9-omP1g0cJuxbvpu5jwwGIV1xVLcPgBibJVsuWUlocLvENVEE2eT3GRPAu-8PG9toQ7wsnFXKkcQFVQJU1MaOSdrmvIeJ0YHGRFo8O88I4vbfCtpxIwuFoyQ7Lum1pnCOV08z4Ulfql9jdDRdUmXxnuvaMXbf943s4pOgHjGkH8zik3QTZRacsF-Oc8S9pUrJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=t-0P1ApvJxJlNyEUNCm1Kgz_PbA6aEDzhlM1oeK0MpK3XW_HJTifpO3zzg7PGJhToQ5Id2YJ2QR4jmCBK5UgBuGbiZT4bDJAJpw2qs9FXjkxxmxeFnhNmzNziauBZ6WgZGEOJG3db0zuqatAjYo9-omP1g0cJuxbvpu5jwwGIV1xVLcPgBibJVsuWUlocLvENVEE2eT3GRPAu-8PG9toQ7wsnFXKkcQFVQJU1MaOSdrmvIeJ0YHGRFo8O88I4vbfCtpxIwuFoyQ7Lum1pnCOV08z4Ulfql9jdDRdUmXxnuvaMXbf943s4pOgHjGkH8zik3QTZRacsF-Oc8S9pUrJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-9-3c6f9ODvfayZiHBPrlONWK6aEZS1xK4BUYLwdWymEkwnl5r2Dnb0ipIZkSJLHGeeLjqXEuMYRwKKgQVrE9N50UBynaMWSl5XCWo9Z2EPqpxQLktxi6zNcZ6Q7h6XmUqXP_nQWxnUC7vCjLC9WWuIqMlObZRuLzmIGQmxDobqDTWxBGf6idbHBcIYd4eDQ-QaW4EMBENU4XA7yEGNGBp3td1DuUV45ORQ94kdED3Gw_bqXaYPQuh4zzu8dHZMpDwvjF6fQlQqpxYBJ7IcHi3QUiF0vS5LialOffkKs6-nqTeGYYVejGmC-s0wtfOz3ML8obLGwtMFHZUFkkUpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5YWOwzwowWkgzsA14_L9VMyEwaE0gASo2jsEBpgd1picZMF4ZxujoCyWo9wwzV-bgBilNoXHpYwu7Fg7OTndz0zjxI2rB7VKbt_ixzGIXKFx-ksOl0Q6th-FLgUAH6PCQR8xboK_5o8WkFiXaMCi4c_bR6LhUTDBuvVswkHcgtURw_PZTKqkGPezFNQY1PGSbZ17kqu861IIFmLDtGHFlMEcEI5IueSJf6OO7RIIDOnWCzmvSuLscK3OEaplctc18eRA8jCqzYVKQTkcArxPTm4CjsEFfl0SRjACqhYdKHYvrWrBHr6vt9A6BfZvck3OnKAUoyxOLqxZIn9EWEBLNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5YWOwzwowWkgzsA14_L9VMyEwaE0gASo2jsEBpgd1picZMF4ZxujoCyWo9wwzV-bgBilNoXHpYwu7Fg7OTndz0zjxI2rB7VKbt_ixzGIXKFx-ksOl0Q6th-FLgUAH6PCQR8xboK_5o8WkFiXaMCi4c_bR6LhUTDBuvVswkHcgtURw_PZTKqkGPezFNQY1PGSbZ17kqu861IIFmLDtGHFlMEcEI5IueSJf6OO7RIIDOnWCzmvSuLscK3OEaplctc18eRA8jCqzYVKQTkcArxPTm4CjsEFfl0SRjACqhYdKHYvrWrBHr6vt9A6BfZvck3OnKAUoyxOLqxZIn9EWEBLNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=BxBrpG7OB95_7ts0rrvL9-139QQMFsAENwA4sPrCYtWNLBmsrq3DJ5lcdbwmwqp1enDIN_cf4q-dKxaPohd3W8UAmcB7MhO8mWAiQ7MDaLn2cs48Iy2nl_Lobem55gUkmCHYxbuqJyb7CmJNspSKQna0HScEntCqKM_YLSLVL-v5ncG0TzlRxM7BdfLBw0zMZyKv8Qh1QFuN-bO1purj7OcFIDulpDdsJYrM1s5wEIUYuD2p3D1i0zRbgwYjT4JlyhXJ6AXPwQu2bL7Kc57mwYSXNyj0THb8C4N8SSwHYfSTnLBWI5llqU4ZIRAZRh1BIfuoHPaWI1WqeF5vt-dhdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=BxBrpG7OB95_7ts0rrvL9-139QQMFsAENwA4sPrCYtWNLBmsrq3DJ5lcdbwmwqp1enDIN_cf4q-dKxaPohd3W8UAmcB7MhO8mWAiQ7MDaLn2cs48Iy2nl_Lobem55gUkmCHYxbuqJyb7CmJNspSKQna0HScEntCqKM_YLSLVL-v5ncG0TzlRxM7BdfLBw0zMZyKv8Qh1QFuN-bO1purj7OcFIDulpDdsJYrM1s5wEIUYuD2p3D1i0zRbgwYjT4JlyhXJ6AXPwQu2bL7Kc57mwYSXNyj0THb8C4N8SSwHYfSTnLBWI5llqU4ZIRAZRh1BIfuoHPaWI1WqeF5vt-dhdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=XRt4XXCegTJLhNS53pKLEiJF4r5q_3-pdY4fSHvBzGULajjSXCbUhMfVTF1N0HWFm1WksGoEVORAwRNW3RN836AAPg8wxRk8hOtq9yvdypy762SUo6i9nnSRW9iOa1SM06fMYO_AIFOnFBBqn2-m-4nmdnoBx-Znpx2JG6I-M07shZ0slOAPQZH04gFtTLnAz8xZt7OksOwhxIpASryImCt89sxqY806RFUx8xACycNPQZJ5Ii31XhSfq-T0RgRzNO4nQ8cl74oOpsK7PmW7i_g8oJCCQUrSQ2c8JW5Ri0uBu4gMNV2egAS215jAAdJwQvi63I-3uqU-YZwVVxruZbF0qskfcTRxnpaJSBy4pN3U-CIfKNoha7oyofbiGuCyTq4AjCAhDPJQj8MpuIvq70KGAeco9maMCjVgkXzkUa4Lr3qC0X3OW-hoc1orBlkM5QfKtYrTAQxXrKWllHFSfuS4tLDt1enXA49Pat7U7wyVEDCk9jzzwH_0_zmhbcewE1BxTv84db0rj_kXPFe1gK_Hod28CCWkM40E1_X5rxSsu2SqZ3yWJej9S7QOJNFiHVbboyTkDQKj41wXkiwv46YQX6ym6WB6ERvRgCBPQhzaAMMVGJ1GQ3qudQfftbdTiVhNfDeKO8KzeV5T1xCHiMipia9DbQKS21WEnuISY-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=XRt4XXCegTJLhNS53pKLEiJF4r5q_3-pdY4fSHvBzGULajjSXCbUhMfVTF1N0HWFm1WksGoEVORAwRNW3RN836AAPg8wxRk8hOtq9yvdypy762SUo6i9nnSRW9iOa1SM06fMYO_AIFOnFBBqn2-m-4nmdnoBx-Znpx2JG6I-M07shZ0slOAPQZH04gFtTLnAz8xZt7OksOwhxIpASryImCt89sxqY806RFUx8xACycNPQZJ5Ii31XhSfq-T0RgRzNO4nQ8cl74oOpsK7PmW7i_g8oJCCQUrSQ2c8JW5Ri0uBu4gMNV2egAS215jAAdJwQvi63I-3uqU-YZwVVxruZbF0qskfcTRxnpaJSBy4pN3U-CIfKNoha7oyofbiGuCyTq4AjCAhDPJQj8MpuIvq70KGAeco9maMCjVgkXzkUa4Lr3qC0X3OW-hoc1orBlkM5QfKtYrTAQxXrKWllHFSfuS4tLDt1enXA49Pat7U7wyVEDCk9jzzwH_0_zmhbcewE1BxTv84db0rj_kXPFe1gK_Hod28CCWkM40E1_X5rxSsu2SqZ3yWJej9S7QOJNFiHVbboyTkDQKj41wXkiwv46YQX6ym6WB6ERvRgCBPQhzaAMMVGJ1GQ3qudQfftbdTiVhNfDeKO8KzeV5T1xCHiMipia9DbQKS21WEnuISY-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=gmIV-Ylu64EkYfIgEgiIDjUcVWD6P-pWJNO8ICHSqV9a06lr3NFZaF4yPuPlBDaMm3_MLDRScUIER_E50MoxdAAta1T0tLRgUGahlJqzztyr-BquM0IcO5EdGayQl3vU7PZSxPfClmPWPnePilZrewPyyKjxRMeXspVjPAA06z4B8vq0ZwRoOyIzMT9CpZ6IWI_qGRjk5tojfm80iMOFctpWIQK7GiEXlYAEYoegQXKWKBfZy32omoaTKRwHcUnTr7ewrhY4fByAHz89i4U8pKEA7p6QXRXP9QQadRvnw9w9449osJtNs-_8b1cMAhLZHNImKw020QT8gCMAyNl8CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=gmIV-Ylu64EkYfIgEgiIDjUcVWD6P-pWJNO8ICHSqV9a06lr3NFZaF4yPuPlBDaMm3_MLDRScUIER_E50MoxdAAta1T0tLRgUGahlJqzztyr-BquM0IcO5EdGayQl3vU7PZSxPfClmPWPnePilZrewPyyKjxRMeXspVjPAA06z4B8vq0ZwRoOyIzMT9CpZ6IWI_qGRjk5tojfm80iMOFctpWIQK7GiEXlYAEYoegQXKWKBfZy32omoaTKRwHcUnTr7ewrhY4fByAHz89i4U8pKEA7p6QXRXP9QQadRvnw9w9449osJtNs-_8b1cMAhLZHNImKw020QT8gCMAyNl8CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoQ3YGpHSWTb_eXMPgXuUTQzAbG_QaNtqV7WKMYYZcnejFMlYrLIy4Ax3HpYhfKIOcSO4T-8sGoH5TU5PACxji7QqM93WqXjc1XhNxy-mI3YjKvKjRx0fLKX6URVkPZhh906Amj6BtIHxKD5-i4YZkAIpC_0B8CdWPX_-KCOfpZDj4O4xxnRlf-N1_Qm7EX59v3UWX0Zu6Os7XUs1CSSaEUrIr5H-qUh_wP6UcHTDHPk-9Ipkol94NWCUsfqT6SsO17l9FoUKrn0SVpxwzKeHQlkNxEHyygoR8O39ywc4FWf2M3_DjM06q6hEesbUYDmOMR9RyJVxJPNntfj6mp0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=f8UDjRD6PCd81GxHcqxozUWwuLvRh5KvwdujSflpt5WxyGWdnmRuxUW7YUdwFSVCYbmprWQA8S0zWdqxeibswzdP9EVTfEJhUNaobKr8t5Vp5KEGSqxzOGUH6RCwlTbpugY-_QwN4Vp4oVmIzKWgX8dRV_C31JJVve3PAqMPO6UqYizwfijEYcVeiV6s-R22D8YjwAe0q0jRuPqUyS3vSp5xXSV5Iz7ZZQdtI3v-B5hXtS8lqaaQen-bSh3ekic6Mo32GSsygo0KelpNZ6wXPkpS4L4a7Aim73D8wGjLHq8UxDQfHcScSiEMvhmF3WujX-QUhl2JK7SI9ooXq39nlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=f8UDjRD6PCd81GxHcqxozUWwuLvRh5KvwdujSflpt5WxyGWdnmRuxUW7YUdwFSVCYbmprWQA8S0zWdqxeibswzdP9EVTfEJhUNaobKr8t5Vp5KEGSqxzOGUH6RCwlTbpugY-_QwN4Vp4oVmIzKWgX8dRV_C31JJVve3PAqMPO6UqYizwfijEYcVeiV6s-R22D8YjwAe0q0jRuPqUyS3vSp5xXSV5Iz7ZZQdtI3v-B5hXtS8lqaaQen-bSh3ekic6Mo32GSsygo0KelpNZ6wXPkpS4L4a7Aim73D8wGjLHq8UxDQfHcScSiEMvhmF3WujX-QUhl2JK7SI9ooXq39nlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=QPKaUmuLSzL0f39M7gajyaynZ1Ts3CAoAik6c3q7Ux94i2DrhAUtwGWKQNWkOmYIeV-PNgZxCPLT7tqTcpsXtpzHpdhu6eeFzDGUqpas4wE3XBkFOtjDCc96iVn-7mj_0V5bP7RGotzrWwEl-c6dN9kkkeTTPabmCPAQaWQR9pfdlOIC8txKKnPTpDtrear5iJkT2PexWJGgL5mb1HRtb5EU7tYv4-5jKUr5Cqf6DSaCwIq2B2PQf3MJ2wLefKvUPfmbSr8bUjhN-bfD1jpuU8BDciVMkKRBueq72llC2Wmw-bpFySDxhjSu3axYclBDS0Pj3Xc6H8WWBcRTVOYoHrmJ-FcI59a5UGOr_WSkSi7GGsUsDFxi7zsXwPVeHp3raeqN8zMrwmRTW-IDl1GtMclILOD09vyKVakmUiSTFRbF3R7rDsR_YubddNIxzvd0TbqxGVhKPKzWfuv7q5-e3UKMimgnPwno-LCW2XspC-Ot-dOIw1BJ7P8XVno4bxv-ImZ060sw2ZgY9anUHqWh8DDowRQv0OH3iYhw5wPp7hSqhZJ-3GTWaidmfROMtJ0EDEhP3R5weLXAVl-M8LosYQaAQgJyxznaFkMJUlKs9uKHwGuHXiGguW-L5vyB4MXIFTLgS4cnQdCyBlij2QXFNjEslbcg3QkEWxS8QBXbkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=QPKaUmuLSzL0f39M7gajyaynZ1Ts3CAoAik6c3q7Ux94i2DrhAUtwGWKQNWkOmYIeV-PNgZxCPLT7tqTcpsXtpzHpdhu6eeFzDGUqpas4wE3XBkFOtjDCc96iVn-7mj_0V5bP7RGotzrWwEl-c6dN9kkkeTTPabmCPAQaWQR9pfdlOIC8txKKnPTpDtrear5iJkT2PexWJGgL5mb1HRtb5EU7tYv4-5jKUr5Cqf6DSaCwIq2B2PQf3MJ2wLefKvUPfmbSr8bUjhN-bfD1jpuU8BDciVMkKRBueq72llC2Wmw-bpFySDxhjSu3axYclBDS0Pj3Xc6H8WWBcRTVOYoHrmJ-FcI59a5UGOr_WSkSi7GGsUsDFxi7zsXwPVeHp3raeqN8zMrwmRTW-IDl1GtMclILOD09vyKVakmUiSTFRbF3R7rDsR_YubddNIxzvd0TbqxGVhKPKzWfuv7q5-e3UKMimgnPwno-LCW2XspC-Ot-dOIw1BJ7P8XVno4bxv-ImZ060sw2ZgY9anUHqWh8DDowRQv0OH3iYhw5wPp7hSqhZJ-3GTWaidmfROMtJ0EDEhP3R5weLXAVl-M8LosYQaAQgJyxznaFkMJUlKs9uKHwGuHXiGguW-L5vyB4MXIFTLgS4cnQdCyBlij2QXFNjEslbcg3QkEWxS8QBXbkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7s7Kzs4RG7O9-Z4USflrSda6b-lQvl3b35IoR9CfNFlSY_rar086wrL8WUX064Y8xj6n8pnQjeX9U-6oslyKgovZYusydxnzJ8Sg_fZJWivuRfs0dEmuzpqPdGUV7W61RdlroGbN6boFAGZFrl7dM0JqtbczUfVFzLElIMo421rAIeB6Q8ddAFGcdgZxTepqGL49SgDt9UDIUG068Ujy9nntKv97rWcQj9DGfoYWYDC-vY_9CT_Wuo_Elhw5xohpJzPTIOYz7g3wIhhfrR2YmxphS4XNPt8ygL3M4NmjAGSC430nQmpLwOsMps4jv4K6cdn7m3N29x0BcsXYH5Wgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jeGBQivJG00yFTWYbGhcMnYq0oylwfRJP5y476jgGTNu4ipZemcALypTBXSYRJNh1cGjCvEI_OrZmxdCyJAn1w-Z8ccBl-rsi-t42oYVaf2eD-dJHLwsn4cFsxpqBc6w6EiWn4lbifxYZMMCUCjeHZY5jIAL8ezwQMkyhojyc7CzQomrqXTj-lwqG3jK1fDlZK_Is-Sabj2zHNymAHvcXA37fee8cx9vIGxxFakuDVsND73Ny05a1-yIOhpz_Kf4-Rk7G_vavKx_YAn3iOkQ-DI7uPEagiOLCVuVRTcedzEVP5y8mKyXIU7KEqxyBSSqCCcAR7ubqPb-p9z8R0Jyd0DRcGkpNb3u5xDywOB9rcK4hzoZ7-jqTUiiwkdUg0yyHqfMmAshX5olTkvbcA45hPMZ4-4e9U1nuuOL9bHDe3fG0GgbKfIKrUQLdxgzaVtQ1ymrRdPhaKBXBBI1QypX_Uf05aswMILDhfrGBNcOWJL8IeCmeR9vET7g_8JoaNIoGcDJ6HVlP0XfG6CIuAZuQnWdhIY1fK8KAAINBYTvl005K_M-HIARyL_s7JLceDmf5SY2k2PufIe7TswhAiq_qFUA2La6oycuPUPTFjbmxRE672llksPzE9ZXh8F2xZDMnGASmGyfXZVdZCfbyoTesZMXvXj92XM0ttl7vrXgR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jeGBQivJG00yFTWYbGhcMnYq0oylwfRJP5y476jgGTNu4ipZemcALypTBXSYRJNh1cGjCvEI_OrZmxdCyJAn1w-Z8ccBl-rsi-t42oYVaf2eD-dJHLwsn4cFsxpqBc6w6EiWn4lbifxYZMMCUCjeHZY5jIAL8ezwQMkyhojyc7CzQomrqXTj-lwqG3jK1fDlZK_Is-Sabj2zHNymAHvcXA37fee8cx9vIGxxFakuDVsND73Ny05a1-yIOhpz_Kf4-Rk7G_vavKx_YAn3iOkQ-DI7uPEagiOLCVuVRTcedzEVP5y8mKyXIU7KEqxyBSSqCCcAR7ubqPb-p9z8R0Jyd0DRcGkpNb3u5xDywOB9rcK4hzoZ7-jqTUiiwkdUg0yyHqfMmAshX5olTkvbcA45hPMZ4-4e9U1nuuOL9bHDe3fG0GgbKfIKrUQLdxgzaVtQ1ymrRdPhaKBXBBI1QypX_Uf05aswMILDhfrGBNcOWJL8IeCmeR9vET7g_8JoaNIoGcDJ6HVlP0XfG6CIuAZuQnWdhIY1fK8KAAINBYTvl005K_M-HIARyL_s7JLceDmf5SY2k2PufIe7TswhAiq_qFUA2La6oycuPUPTFjbmxRE672llksPzE9ZXh8F2xZDMnGASmGyfXZVdZCfbyoTesZMXvXj92XM0ttl7vrXgR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rn9u_Q4ysVcJ-Nzy-IF2V_HmJtWq2QTb-h4faw4B2nyANaeGIDEzgY2FVYtOS48mGgcALRCCO9ycKY91YTimAv9mo0a2DvzaDeqMOsTzxKuYYdfAlLnCfbvGfIeePW99kuEU30cUuIDO08E5er3xi-0jj2LVtzi60LQoOYCVSaFUGT3sENCW_hdDxfoGzT6j3xD9LeGngro5DohUWXJlWdOJiFvDVchAUffnXPZfEa8reSsgcvjoQ8sxm50Rb6eCs06g0QcWbWotYEbE5az5HSraOtBdj4KCr1y40TMfy1UpOhILPf9_RY9ZLYCxFIBQ8lCp7SToDfptM8H_eNwsH4f9SYFU45sHKYHIEg0rZ0hKHefWJcR1JQt5V0qXO9TrHZrNySfSrTrKR8n-TAwgElhPh2c1JN36wCumqNOq6bCNwOiDxTEZStn6YLNGEfL3DJt7tZyE_2EFlC2TgK-gjlQpWpwOuJNBzNKfn0WAlvzmhYS6K28t95rjv6obNod_HM5tyzlUYh5Arvzk3VNxmnbcO5mNUyn47R50rwMF0IlHParEZOldcq5od1BmH_5s2yp6kfUvXCCeJMQ5uNRI-DVkPM26nHvIaf38PlseJlTNQQsT1QwSIfyFlev_I2xA_k3XQmiV2E7Ny5sYY9RUeb1wP2hjAsNVnsyALOkHMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rn9u_Q4ysVcJ-Nzy-IF2V_HmJtWq2QTb-h4faw4B2nyANaeGIDEzgY2FVYtOS48mGgcALRCCO9ycKY91YTimAv9mo0a2DvzaDeqMOsTzxKuYYdfAlLnCfbvGfIeePW99kuEU30cUuIDO08E5er3xi-0jj2LVtzi60LQoOYCVSaFUGT3sENCW_hdDxfoGzT6j3xD9LeGngro5DohUWXJlWdOJiFvDVchAUffnXPZfEa8reSsgcvjoQ8sxm50Rb6eCs06g0QcWbWotYEbE5az5HSraOtBdj4KCr1y40TMfy1UpOhILPf9_RY9ZLYCxFIBQ8lCp7SToDfptM8H_eNwsH4f9SYFU45sHKYHIEg0rZ0hKHefWJcR1JQt5V0qXO9TrHZrNySfSrTrKR8n-TAwgElhPh2c1JN36wCumqNOq6bCNwOiDxTEZStn6YLNGEfL3DJt7tZyE_2EFlC2TgK-gjlQpWpwOuJNBzNKfn0WAlvzmhYS6K28t95rjv6obNod_HM5tyzlUYh5Arvzk3VNxmnbcO5mNUyn47R50rwMF0IlHParEZOldcq5od1BmH_5s2yp6kfUvXCCeJMQ5uNRI-DVkPM26nHvIaf38PlseJlTNQQsT1QwSIfyFlev_I2xA_k3XQmiV2E7Ny5sYY9RUeb1wP2hjAsNVnsyALOkHMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Jtvx2T5dCIr3cJ1FAxpDfBhuAA8mmzQiW9pk6yBju2E3wNCTeDQPwQ2RWafcwIVpvCKwEb0AhSz1H3lP1nJMj-frGVpVGckOiqlNmys_khFa__tOxT-hMXixH1M40979Wmuxur3ZazJJ6dnLx2oTmrixvEumN-JEH4T--fDm6JH8LkiIwjtwNk4tw3Ed6MDMvJcOUYaZqXJAkqE6y-bjuQlxgcawCKhE6TglCdv9uuvW7vupdZJ1UudxxXCQCMBSbJOEhs8ydpq4hpiNTPw0ZSd5hqL_zjTBLgkNVyGwzCi0zlk0KRHuJ4_UyShVyuab74iCL_tRDmdBNlldV-iXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Jtvx2T5dCIr3cJ1FAxpDfBhuAA8mmzQiW9pk6yBju2E3wNCTeDQPwQ2RWafcwIVpvCKwEb0AhSz1H3lP1nJMj-frGVpVGckOiqlNmys_khFa__tOxT-hMXixH1M40979Wmuxur3ZazJJ6dnLx2oTmrixvEumN-JEH4T--fDm6JH8LkiIwjtwNk4tw3Ed6MDMvJcOUYaZqXJAkqE6y-bjuQlxgcawCKhE6TglCdv9uuvW7vupdZJ1UudxxXCQCMBSbJOEhs8ydpq4hpiNTPw0ZSd5hqL_zjTBLgkNVyGwzCi0zlk0KRHuJ4_UyShVyuab74iCL_tRDmdBNlldV-iXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=s_P07qj5N9apXQkLFlXFlray4UVbY0vwSoPq641rdFHXgg2Bab414RgukVdZhkKwh1DRLuDMMCK357aqde6nuPVB9XsUtZPPkaMRdApFeJ6aJG9Mb81pvzkib4IOG0MhQgjVZJ__SAlSBfCgd2S7pLFLM1u1avr1rIBwId72hlYfgUxFWuPThBHMtMrYZ72OqeuII3k4xd16oL5zDBuiufeybDmr0lL_-ymaw2rJoNHTpuJNZGufXyBvexnz4jxzXRZ6hlIUL_hiXAx1PWeoIyMINg-xiE4kcHSq5PiIW3Kb0z1YjOaMBP41tCpxOX5cla2lYGumHU-0NMOQun8h1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=s_P07qj5N9apXQkLFlXFlray4UVbY0vwSoPq641rdFHXgg2Bab414RgukVdZhkKwh1DRLuDMMCK357aqde6nuPVB9XsUtZPPkaMRdApFeJ6aJG9Mb81pvzkib4IOG0MhQgjVZJ__SAlSBfCgd2S7pLFLM1u1avr1rIBwId72hlYfgUxFWuPThBHMtMrYZ72OqeuII3k4xd16oL5zDBuiufeybDmr0lL_-ymaw2rJoNHTpuJNZGufXyBvexnz4jxzXRZ6hlIUL_hiXAx1PWeoIyMINg-xiE4kcHSq5PiIW3Kb0z1YjOaMBP41tCpxOX5cla2lYGumHU-0NMOQun8h1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GbZa7XQ5Z_eNYVdLhs45w-kgyiUPGdppOqyk_49uctY8drU1CcH2G0ZmVyWLpsxdDDs0zZIBUG7LAYp5_fFOVkoP2ySN1QnshW-hLYQoIk_LCseWqpZI4ZxsyjMqd88mrdDUzqMhCzv1u3gF9mjEnsASS95tYYUzVzZEi52QJJxT7CTVsizYfMhjTquQ66g1vfOvuxPNJBhvc4NYn2of4GGx1oNXbx93PDRt9fs7OwEAB-_q5w4F5gNY4MOmwVzDVvkuafq8LlUwEKs9nk9_N1xHi0IMEpfl1xG1iFXE9nu9Fsb3OnWfn6kE8iYfCLOLG58pcw5blrMUSt-l8qt04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GbZa7XQ5Z_eNYVdLhs45w-kgyiUPGdppOqyk_49uctY8drU1CcH2G0ZmVyWLpsxdDDs0zZIBUG7LAYp5_fFOVkoP2ySN1QnshW-hLYQoIk_LCseWqpZI4ZxsyjMqd88mrdDUzqMhCzv1u3gF9mjEnsASS95tYYUzVzZEi52QJJxT7CTVsizYfMhjTquQ66g1vfOvuxPNJBhvc4NYn2of4GGx1oNXbx93PDRt9fs7OwEAB-_q5w4F5gNY4MOmwVzDVvkuafq8LlUwEKs9nk9_N1xHi0IMEpfl1xG1iFXE9nu9Fsb3OnWfn6kE8iYfCLOLG58pcw5blrMUSt-l8qt04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Q1UAUgslOL-gaznbRhw6Xo2Bd1pb0jZ7m5QdW4VLDU8LOlqu0lLICl_RtXORBidgytMf1abI7vJCmEl6-KNFBZD9RgbgzqA3gIsyScEjQMT-05Id_UJhe-sG_oBqq8ZkVM9zu3B7dLGhYLkCUOQsjYH5ft1oAp9Gwkxs-yvMKauMe4Va72VLqfvMeRtUKNWi52-T-UfISaWYJELZo2smB_nijXe2NJruqRIP5zLzmCPT7l2J6o3f1zEikk1GwwieZ3KfM94K1XlXAaVQqUZAh_4sapuAsCRWv1Dq6KHaX4f-O1GtAs0UcI_Zkxf-XkpGzSPtppx6NL_NupK_id7oPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Q1UAUgslOL-gaznbRhw6Xo2Bd1pb0jZ7m5QdW4VLDU8LOlqu0lLICl_RtXORBidgytMf1abI7vJCmEl6-KNFBZD9RgbgzqA3gIsyScEjQMT-05Id_UJhe-sG_oBqq8ZkVM9zu3B7dLGhYLkCUOQsjYH5ft1oAp9Gwkxs-yvMKauMe4Va72VLqfvMeRtUKNWi52-T-UfISaWYJELZo2smB_nijXe2NJruqRIP5zLzmCPT7l2J6o3f1zEikk1GwwieZ3KfM94K1XlXAaVQqUZAh_4sapuAsCRWv1Dq6KHaX4f-O1GtAs0UcI_Zkxf-XkpGzSPtppx6NL_NupK_id7oPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qTaWZ2ntOI1FDbseMqohxTje61S_Bq5tmEsTaqAlWpip2jG5wUkdCpuZ9_0teKuGkEyORUfgID6Fr9DgLLtl2w9jJaOyCngEpbjnAbhGK0iptPLfa2Vyuon9_VMxHtJt2JaCVQRmGV9jQkynvGeIUxEIOLkcqXqzZ0XA8f3Tir7mbIby13ZiJC9fMM40-nXHdQXy8E0o1X8uWfnd9PaM4y5LMtndi9DKnfRSEIdQ3_6kroWOxQWmd6AJ5i8R65Exq9_oo-u6uyicRKNQPDmOFeUorxXFhmyuaR2TfxnA7aPInhYOVNH6esi54vxBxm9ILG9h_t58j8VuGgP3WZsRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qTaWZ2ntOI1FDbseMqohxTje61S_Bq5tmEsTaqAlWpip2jG5wUkdCpuZ9_0teKuGkEyORUfgID6Fr9DgLLtl2w9jJaOyCngEpbjnAbhGK0iptPLfa2Vyuon9_VMxHtJt2JaCVQRmGV9jQkynvGeIUxEIOLkcqXqzZ0XA8f3Tir7mbIby13ZiJC9fMM40-nXHdQXy8E0o1X8uWfnd9PaM4y5LMtndi9DKnfRSEIdQ3_6kroWOxQWmd6AJ5i8R65Exq9_oo-u6uyicRKNQPDmOFeUorxXFhmyuaR2TfxnA7aPInhYOVNH6esi54vxBxm9ILG9h_t58j8VuGgP3WZsRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=e3f8n-uFI9G-DLEX64zQ5MEjE-Jtee--bUZtez8LmVcb3ezZqJzdNl4_aLYNfT2p6VGtdKu6il1Hq7rViUzTgtyUE27TFFhvZ0d63eUDoW-U83_VdmthEsnCaEyliFA6-vxLywFth6_5O_CZQogfMts0Fy1GpYJQvrtLYhTipB8uG1KOqVb7V7YU0hwtXyHo9vaei-3ERmM7gQG4pWbr8iTc_hjyOrF9Ihu_6piVYAUUp-QXO7XnDxF8P96e37Sdz_qmZK-CepVfXWWtGyVPrKD3O9gwOZxvyLvJlKAL-3ebsIOvJ4H4ujQ_1LlopHje0bWdgwMm6ChTO2smGRqjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=e3f8n-uFI9G-DLEX64zQ5MEjE-Jtee--bUZtez8LmVcb3ezZqJzdNl4_aLYNfT2p6VGtdKu6il1Hq7rViUzTgtyUE27TFFhvZ0d63eUDoW-U83_VdmthEsnCaEyliFA6-vxLywFth6_5O_CZQogfMts0Fy1GpYJQvrtLYhTipB8uG1KOqVb7V7YU0hwtXyHo9vaei-3ERmM7gQG4pWbr8iTc_hjyOrF9Ihu_6piVYAUUp-QXO7XnDxF8P96e37Sdz_qmZK-CepVfXWWtGyVPrKD3O9gwOZxvyLvJlKAL-3ebsIOvJ4H4ujQ_1LlopHje0bWdgwMm6ChTO2smGRqjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=P7fmKwHg7fJM6EyAZtmWnQDIlf3oO_hGnfjBLnWVamdamjekwF_9BRry68MJLaAib7uCfa-03B4V4PPdKq4-2ov4JSuWdlmt5AGVQHGR7YvwBnLhR8d1eJ6wYvYwnV4PhDYffq2YvnGEuAVl-fiDxjIdEXinQM1zlrP0uqoBNPs6holY04W6pol3pOJG6gRoulOcSVaxldkZkKj-6qpXMhjVoeoQg8RN8bLim_qeuwA94h6Dj932bLZuvkTneKYDCiGBNaq-4el9UplRG2XHZyLy16PF2rSvTFQKTdi1scPPs8NQ2oYU7qBS5sdJZT3qcdHwreGrSj5hMuuLqRB4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=P7fmKwHg7fJM6EyAZtmWnQDIlf3oO_hGnfjBLnWVamdamjekwF_9BRry68MJLaAib7uCfa-03B4V4PPdKq4-2ov4JSuWdlmt5AGVQHGR7YvwBnLhR8d1eJ6wYvYwnV4PhDYffq2YvnGEuAVl-fiDxjIdEXinQM1zlrP0uqoBNPs6holY04W6pol3pOJG6gRoulOcSVaxldkZkKj-6qpXMhjVoeoQg8RN8bLim_qeuwA94h6Dj932bLZuvkTneKYDCiGBNaq-4el9UplRG2XHZyLy16PF2rSvTFQKTdi1scPPs8NQ2oYU7qBS5sdJZT3qcdHwreGrSj5hMuuLqRB4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXqPMv1E1bwGABFMaOOrw9daZJuwZl0kj27PqkcA8z_x4VQUvOtALSmsDdfKMghXSMr-v7USV-m2h0TnxINkorYJJu5Gvv8lEBTMi2LWcUWJ1Z9weovuDkBA3uG0PQbptyezkA1UXNJVqEuGWao_eSM_L2OAcA2rY9ZAjs7yUUMdtqWCO-yUejkfFhhukF7TGb-Dx_ExX9ya9536N38XSwv-5mzj2cq30keN8I_ijYyIZSaQZaoYPiXC3_SVBR3rOAB5nyfCpFSsZ9R-D1Izn8rw5Y80OHYXSP8xd61Mu9C2JmAeVywYKKyoyRWI8V9usLtvjlIOJPe_JqNBAwKR7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RwGbYxcnPLwyRAqR549ZKke_LS68fuO6F5NcRplvINJOAQywIlwxRoVj2ojjlUrIJYEHHIX6CfyoPbpALxbzu17wwmB1JOsE6_tyZAhQ8kTWgLutBZWqO1e8o5TxtTga-Ojn7n0HEA18MZGJM_I6Zl8gvXIl8mFPT1w5rkyThrLjuM1R73S4vArlLkkFv1ElbV8mIUT3FfXqtHxfKGK-xlQxrhcrP5thR-KQjyxEal1reFk2mM2ptypskQ7t5opSvY2TKvE8Takk9CljkRfQ6Fw26PuYvYNGoE7HKDkgffGN6sKRbVrk3kUutG9-k-7SB4w_U0aBriM8F7cP2329Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RwGbYxcnPLwyRAqR549ZKke_LS68fuO6F5NcRplvINJOAQywIlwxRoVj2ojjlUrIJYEHHIX6CfyoPbpALxbzu17wwmB1JOsE6_tyZAhQ8kTWgLutBZWqO1e8o5TxtTga-Ojn7n0HEA18MZGJM_I6Zl8gvXIl8mFPT1w5rkyThrLjuM1R73S4vArlLkkFv1ElbV8mIUT3FfXqtHxfKGK-xlQxrhcrP5thR-KQjyxEal1reFk2mM2ptypskQ7t5opSvY2TKvE8Takk9CljkRfQ6Fw26PuYvYNGoE7HKDkgffGN6sKRbVrk3kUutG9-k-7SB4w_U0aBriM8F7cP2329Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=hESZTEfi6x5jkissdJS7-qtfH-O0syNPruqibw9NnEP3kGuTfmj6RTU-KPiWZtLm8l5UfnUq4ieAx7U1EKIRPcvU2Ns9v6GEaZ7Ixw-0VJPKx3iJsr_MId2vfiImuljAko2kd4YIfe_SS6QPNLwwFI4yuEj4GOqcQ3C6RdRaCfG7WmcEPZ54h_C5l-JQBD5j5RP9YFCKZjiIZC-6uhBVNAdoQp_sJsgC-0sUZTZHDsS3z0SFTriYkhNJzqPrVtWG4-QHkj6ocOODV1WmXwiaIt1yKnHIr0arahShUGyoPggsrzhGLoj_fASMmUunvvpkiBlovmvU_6mU--Aw4o8Ckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=hESZTEfi6x5jkissdJS7-qtfH-O0syNPruqibw9NnEP3kGuTfmj6RTU-KPiWZtLm8l5UfnUq4ieAx7U1EKIRPcvU2Ns9v6GEaZ7Ixw-0VJPKx3iJsr_MId2vfiImuljAko2kd4YIfe_SS6QPNLwwFI4yuEj4GOqcQ3C6RdRaCfG7WmcEPZ54h_C5l-JQBD5j5RP9YFCKZjiIZC-6uhBVNAdoQp_sJsgC-0sUZTZHDsS3z0SFTriYkhNJzqPrVtWG4-QHkj6ocOODV1WmXwiaIt1yKnHIr0arahShUGyoPggsrzhGLoj_fASMmUunvvpkiBlovmvU_6mU--Aw4o8Ckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=K5HNAxOHCI2hC-qpGwRvfu2KhG5pMNWgQPexSiLH9nmWDGdwou0ykAk9R8zddVLkanl93MgzhGz1eJrzxN-6KLPRcV9s4VZ1E2YOa-rYujLQ-AOfV6KFcCYCRZsf81NN4yhYEXLPt5PXzTqWGwMU37ezTdSkj0Wl91RIlccMhfdLABAoMnucLO9D00R6OdXo68TjuA2TfcXsuoMDYtURdGCOCySWGxh1jB9V4NuxEH3Kbq5Wdj-ZK7g36fBF6WAHjZ89ELH38VRHCKLNJxne46PP4DCmaleHb7zCAshsR3nD2XGRpu5wokcefX5FTUEbJhpH2VgfFNOlO2GB7LzPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=K5HNAxOHCI2hC-qpGwRvfu2KhG5pMNWgQPexSiLH9nmWDGdwou0ykAk9R8zddVLkanl93MgzhGz1eJrzxN-6KLPRcV9s4VZ1E2YOa-rYujLQ-AOfV6KFcCYCRZsf81NN4yhYEXLPt5PXzTqWGwMU37ezTdSkj0Wl91RIlccMhfdLABAoMnucLO9D00R6OdXo68TjuA2TfcXsuoMDYtURdGCOCySWGxh1jB9V4NuxEH3Kbq5Wdj-ZK7g36fBF6WAHjZ89ELH38VRHCKLNJxne46PP4DCmaleHb7zCAshsR3nD2XGRpu5wokcefX5FTUEbJhpH2VgfFNOlO2GB7LzPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=bGBbcQDnP5hHyPdpk4f5w7N3XcBbtGV4l8MOh_my-sqdJjsW3bVrR1i32mI-GhASzJmuwIey7d7K5CHtgnvjKyHj0HJq1bhuSsNOzqxw9fmbsJamFUap2mV524sO_UgDDmj603BCgsQp2iWpHGLAwGdPgeP1FmDOIjXVlKf3qaJQLp8o5UFFUVrDkURfyVTeMcHSsX8-xHJJFv2TKT1fgdY_G2qyuHPnZO68FJH4a9LRG1NYSXrdYpopbCXJYDlzE43nSRqpTS9u2FC6Pl9EhxF4DVq8zITdlTdJYMjI-odXMkEyUYYwUTkWzEOy4Bsni94Q0qzr3UsL0T3nfd2AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=bGBbcQDnP5hHyPdpk4f5w7N3XcBbtGV4l8MOh_my-sqdJjsW3bVrR1i32mI-GhASzJmuwIey7d7K5CHtgnvjKyHj0HJq1bhuSsNOzqxw9fmbsJamFUap2mV524sO_UgDDmj603BCgsQp2iWpHGLAwGdPgeP1FmDOIjXVlKf3qaJQLp8o5UFFUVrDkURfyVTeMcHSsX8-xHJJFv2TKT1fgdY_G2qyuHPnZO68FJH4a9LRG1NYSXrdYpopbCXJYDlzE43nSRqpTS9u2FC6Pl9EhxF4DVq8zITdlTdJYMjI-odXMkEyUYYwUTkWzEOy4Bsni94Q0qzr3UsL0T3nfd2AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKUvSvkBnYG4RPn_6KbDdFZ6XLVG4wCSyyIRPBcDdeJ60m94VpxUlLQ9GsLp5coCP0K53NKpqL0s_thgiRu3x9zmlyFuKM9qWKpO1OYKDLSQErzjwQCheoO3KweOmdihbhCX7XaHCUL4Hi0AIGFOBYfNTnuDzr6cid0iMa7VAr-jkWZmC132lRRMVtaBgdy1u6FBcM8BET6P4rEHEslp4yTwdHt6W6rNjeAYKjd11FZUV7YRsRRynETpFVjOJ_-5_Z8ri_8tnTBCY2-5KOFT_j54PyIbfQfT4CL32CIkoez5D03allYHTO4rXRRus0nzgA-r0460ioc4QZ7mneTpew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=PVnUZeFARRP2VXd8dN9vUudvvx1BI2ShI-ETr4fG_J6uudBXitn46mleqPG-oqwpoYxFTFZNbK1Q34meDvpUPz98LgbnwYkEVQxhUxJw6408GteGnFMdd8Ken6KeIVJ5o0M4c0eCPsi-tBjZYIjXpCvhC6PXyIKTgA929SO1Y-0QSoToyNiNHvRvRfjtMhjT--AoMnCOxUe-_BettuV4yHpXcWneqgXWT9Q3EkgTGSvnaFD-QOPTt8Fc109-0qgMOybWfah2ettJoLN_eApTfrbaY6C8Q-dYGqkEXCGmb6A-CyfccsHOvGhN-ts8y17975wO4790JeNS53UH2paGkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=PVnUZeFARRP2VXd8dN9vUudvvx1BI2ShI-ETr4fG_J6uudBXitn46mleqPG-oqwpoYxFTFZNbK1Q34meDvpUPz98LgbnwYkEVQxhUxJw6408GteGnFMdd8Ken6KeIVJ5o0M4c0eCPsi-tBjZYIjXpCvhC6PXyIKTgA929SO1Y-0QSoToyNiNHvRvRfjtMhjT--AoMnCOxUe-_BettuV4yHpXcWneqgXWT9Q3EkgTGSvnaFD-QOPTt8Fc109-0qgMOybWfah2ettJoLN_eApTfrbaY6C8Q-dYGqkEXCGmb6A-CyfccsHOvGhN-ts8y17975wO4790JeNS53UH2paGkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sTMbp99VRhvrdd6gq2vI0CdHUHev4lubc2HP6xii7BeUZOPDmhbXBZDHGJo1ivEhbHP2FrPEghQopeRgZ9ID0SSSmP0hNgMCHpIsUjoARjj-D3J_7GJHCrRIjtnYmCwWD5hGZz0yxdyfGQJuTruIuKy4AUxs8a7AF41AW6YLNhf6Cd4Vf3iCkkHnyYAf4RWtwgr1hiRJ_SIvfPTrDYhHrgf9RgyB6OqIlhG9ZAxNxP7aonC49mTOUy1zup2UMSTBGob6pFaLOX8jfyX_VgHrjRyge1CXwXI1nHQFw_umHgh4LeWMejCwU_9fwP5aFnUrkpAbFVcenYe75BvIo-o_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sTMbp99VRhvrdd6gq2vI0CdHUHev4lubc2HP6xii7BeUZOPDmhbXBZDHGJo1ivEhbHP2FrPEghQopeRgZ9ID0SSSmP0hNgMCHpIsUjoARjj-D3J_7GJHCrRIjtnYmCwWD5hGZz0yxdyfGQJuTruIuKy4AUxs8a7AF41AW6YLNhf6Cd4Vf3iCkkHnyYAf4RWtwgr1hiRJ_SIvfPTrDYhHrgf9RgyB6OqIlhG9ZAxNxP7aonC49mTOUy1zup2UMSTBGob6pFaLOX8jfyX_VgHrjRyge1CXwXI1nHQFw_umHgh4LeWMejCwU_9fwP5aFnUrkpAbFVcenYe75BvIo-o_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVqk31V1I-v711RvkDCE63gYwuPvmqfzg7VKM6f6oc-CPjThYqx5zjDkO3x7q3wYBZbm4y7TUwdcQ3NK0zfzTT7ngNzpNx5QN7vYv7yehM_jt1ksWQo-hdKsJRcT9H0yfG9JCJk57y8mePs0Ztca5BweTbuZmhVOI2Dtp63Oz5IesFF1rLKT_DXYj7hLSeoJYAlJpCySrCzJbJKTjnG4OWEjL9hMeUTq0OD0k2fx3qR0BPY2IPzjMXM6Rn8ZyuubNCcsvSBOcHqsS43rJ13LFHgfFdKWoHEyYDRKffn0-fyd4pvGn5UC_qlu-BM_RQ9QSY8VbtM7k9rMZos9h0TpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9sxIYr7hUmwwH-G141Ocz8VYhGgnSHuIpsD1auYQhV-PqxJPMAzCAN3-vZ1AkMQWdKHmBwTF7VHRa2fKjzer7gCbwvvOyilPNBxrZotJ4Fvd2qLZXhiEBuCrRPfM-ilayPIeuZ3MifQ33cksZ5NuZwTrp9xA6udLNUAnCkecv3yKKL5icDL5tNc1E9BRHEejfYpB0AbSaG3Dmg0lniSAOgxeJS4VAWim-1Vpe_LVii8LAekGxkqa4uYElQLmwlJflfxscmLAnA3jNORDRFCEq7ggscCopYkpydn_vp3LrA_T458TFEd2t9TPaFPVcIzaLyRuHfZKykWhtrfEgzXsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lFv-247aI6m7fUzDj1rpnno-UwYIyGTD5kCLpzhAjn280FXGqoF2amXa3WdjjSgaldwTsuC5BCJTNKqQNL2_fdfeVd4KngpjKYQCz-iFspN4me08xvLEXw4NA5pb4rTZrFaKbkc3Ia7s3ks7EyqM6yWy7-oWwmMuj0cmIBSNBIpUOpKuN2Jil3E-WQ0cJzcy4e246MbIAKuauqYC3uj3MO64ppjHfGZRT2gpvze2083H02ur1nHx0Tw9w1GuMn1KNsTOaICzVSVEbfBZ3pKOT5FJHucPD02ruiDSwbfTuv07yM4Bd_Ahv2pGtDB7y1wKlN6WjqVnd4iSmp2e0wUXlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lFv-247aI6m7fUzDj1rpnno-UwYIyGTD5kCLpzhAjn280FXGqoF2amXa3WdjjSgaldwTsuC5BCJTNKqQNL2_fdfeVd4KngpjKYQCz-iFspN4me08xvLEXw4NA5pb4rTZrFaKbkc3Ia7s3ks7EyqM6yWy7-oWwmMuj0cmIBSNBIpUOpKuN2Jil3E-WQ0cJzcy4e246MbIAKuauqYC3uj3MO64ppjHfGZRT2gpvze2083H02ur1nHx0Tw9w1GuMn1KNsTOaICzVSVEbfBZ3pKOT5FJHucPD02ruiDSwbfTuv07yM4Bd_Ahv2pGtDB7y1wKlN6WjqVnd4iSmp2e0wUXlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClpAlpuG4-f2XFsDjwnj0MtMhg7PSOxY1jNg3Pb-S7vnjSjB99W5p5_rc9zjCc1nmxkwuNPLVDKWOSI6MVo-R0qyFL13oIieSAhnP8MlIAKGX5sZFu6HrAjOr4mkQ-IkbCSLyhVYRzdtFTcX2sl5WXrneQasBzDXKWtSbNxEp0iB0m_5jWzIvAfhh9-7A0jqpdp5Hpn_ZBXuFdbK-3uAPVxlosiSiidnvbxhTvTm_683AgHAsu2ED86U46rK0IvO0Ezb1MeTxjJCp54cTpC3b6xphKcIpi4iqLvcaDPA8JjNsr1aEeQH5tKS5eOwy-twglrToh6wAfoosjLbitl0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmkIkR8pecls4yuLOcG1QIBdsxzT9dNLd3Nz3XGKeRKC0Uzuq-EW9uzMs9mkWut3_Nw3OGsxru3X08qBKqVdxIfZ0CuVfhtZqaAM453J3ePr0PuIM3g3WRrZNsPtrAq1_mLXoeno9t7PKbgJKIERNbCaHCZ_NuRo0KmryihXyDmoeKzO5QCuCdIkrd5-Q2M7FF1-BGoWT-cyjudj_Hz-Cl7xDsZ7DVOjqMyb9Bt2oyBWB00-yYKizq2Z6aOT8iPjV7cJSBgengM12p1ZcRjykIRAHx4Bk0S0w0-ahKaZItAGJmy0f-OU4qSjE3jgrk2tYPSNDr5tTQluxaD3c6hnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9VK6mLuPFo-9pR4fY8UNhOeD9otFo_-6OideQf7FQesBTEbbffs9RKCrFgm33hzxzQ3f3to9nU19Vn2U8VHtE1po2MC2N6PHwXE2LEoJC39MiZMo1C47DF4WK4YM24uaCtcgCGbbT5AJ8kjp1ZLk6bXAfN17WKEAXQ4X6mficsOxK5KULHdRvmkE5lCHMvIAWHuWpWYKJ6w76NUV3-kehKFNhxYun_iwvqs7n9Z74GowsA9eDSZwkbA51bQZp3hdw7EF0B8Ccf4qwf4PQcf_3chjkt4mDcWdZiBWL5AzMRTtFTU0zplLcDOITDmVwmYWY8Bh9Rp9PfX47UbTfQMuw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EkG6RlDLH3IJG5rBdwbZO4-ChtQ_0V9EGkKj2gEsE3GFaRuHi6FaMMba8AQTcW8jBM5YOL84GEA4zm-16eiS0jO6-sIOSzRVOQyJvYzmBG1xk_9TsAwaI-HT-BV_bndprkBtsfbEkZq7EohqzrqTU6pwKAswPOtwid7uLL9hJ2vrG0LxRa-eskGMlNtakvVerNKQdl3TowP2wbX_650DthBSm7rhIpe3wtQutPF1OSEcqHwIn38UeXZjHW486JwcU8N2ENT7Dask2-9CMnyhHmyuc7edYfnzG-tHZXi1S9LuJ8FVUWsD7Uq8fFJQJzSctKPF376FX_1LN0hrWr9pJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EkG6RlDLH3IJG5rBdwbZO4-ChtQ_0V9EGkKj2gEsE3GFaRuHi6FaMMba8AQTcW8jBM5YOL84GEA4zm-16eiS0jO6-sIOSzRVOQyJvYzmBG1xk_9TsAwaI-HT-BV_bndprkBtsfbEkZq7EohqzrqTU6pwKAswPOtwid7uLL9hJ2vrG0LxRa-eskGMlNtakvVerNKQdl3TowP2wbX_650DthBSm7rhIpe3wtQutPF1OSEcqHwIn38UeXZjHW486JwcU8N2ENT7Dask2-9CMnyhHmyuc7edYfnzG-tHZXi1S9LuJ8FVUWsD7Uq8fFJQJzSctKPF376FX_1LN0hrWr9pJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=kM7wVAePb-sCiQlqvqHvhtV8ShdgvdnNft1WWMa3Gxz2m9udNZ7MRw_uenKj9cpzcnntB25Zs6kTrfjOeUuxf-bRrkzPampYtB28jzuuNJ8NFLxZ8xwIuyLgEmIxHuf6bJ1o9qI_JGDAtc3WgmmaAhdLaG4Jsc1gWEBaRLv0hEB7xZYTI0hayR87fvkCV7a_bR4I9sUx7Qj-sLmgm0j5ECHufN-B-czd6c6B6zKWnovaRNnMlpHm_A2LgqXGUERAJCaXwXVCXr9MeD9kBkbFMTvTLL14VDfohScU1J2NWTED3zaOxKJB-EXjx4FF5SYsi5gqfoWbgCzbQ6mob2BGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=kM7wVAePb-sCiQlqvqHvhtV8ShdgvdnNft1WWMa3Gxz2m9udNZ7MRw_uenKj9cpzcnntB25Zs6kTrfjOeUuxf-bRrkzPampYtB28jzuuNJ8NFLxZ8xwIuyLgEmIxHuf6bJ1o9qI_JGDAtc3WgmmaAhdLaG4Jsc1gWEBaRLv0hEB7xZYTI0hayR87fvkCV7a_bR4I9sUx7Qj-sLmgm0j5ECHufN-B-czd6c6B6zKWnovaRNnMlpHm_A2LgqXGUERAJCaXwXVCXr9MeD9kBkbFMTvTLL14VDfohScU1J2NWTED3zaOxKJB-EXjx4FF5SYsi5gqfoWbgCzbQ6mob2BGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lT0y6vWoocxx6mX-fBLjfCj9txqiSP38824BFeWkgL8d2ZMmhar8xy_mZyTLhBZiBFqRdDDwglktbFnXnYecbDKgv3bjlnKizCmJvaB0l-wd8sAVbzD3Z-L-4aLLanlkddeyQ4IGGz7phfTIsNOIW7bXvVpP3KgBfL_T3IZc6NHLRGAAbWdYkvZ4YerzW4aOs2i9e2vwK842zZbuNygpyPQn9qxzaqLq7oQJvTe7WNe1NzzvlLw6Nbv5227N5Zq8H_ywEKzI51cD5OP8DINgFsd0dhEPV7kLlc5c3x0cWPPAIEtLlKp3CCATQ2TaHRHxIQLctHp2ofHIIUMcEMEdE5YwrRoMDnoVKNWpeWSKCdMMnlzTdZtFyLFYyA8nhawwowdnlXpSwLfa1R6wBixcJuvAPgpEDblHBEBu9OWIXlGYM04RdNGNaDedXRwDI94sjeuYQTXzROr9lOhJzCwRzUKaU9UEKfK4JmWzLYuG4W1a2uc_CMikc21_YydfY5bquRIW4xbTpYT6tqgld6JCg9Z7fL3wz7IAfXZQzdadTufq5sA2mmW2S4mgpRDMYrBGVWv1zTFJbxFvoXVuAiPow_AhvsUzue4l-EDBnnwgzNjBzqD5AChGr18dk0Y-T4HxAS0YfbepwpH-9mlqD8SkZH3IEhHnFvzCm34mr2hunag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lT0y6vWoocxx6mX-fBLjfCj9txqiSP38824BFeWkgL8d2ZMmhar8xy_mZyTLhBZiBFqRdDDwglktbFnXnYecbDKgv3bjlnKizCmJvaB0l-wd8sAVbzD3Z-L-4aLLanlkddeyQ4IGGz7phfTIsNOIW7bXvVpP3KgBfL_T3IZc6NHLRGAAbWdYkvZ4YerzW4aOs2i9e2vwK842zZbuNygpyPQn9qxzaqLq7oQJvTe7WNe1NzzvlLw6Nbv5227N5Zq8H_ywEKzI51cD5OP8DINgFsd0dhEPV7kLlc5c3x0cWPPAIEtLlKp3CCATQ2TaHRHxIQLctHp2ofHIIUMcEMEdE5YwrRoMDnoVKNWpeWSKCdMMnlzTdZtFyLFYyA8nhawwowdnlXpSwLfa1R6wBixcJuvAPgpEDblHBEBu9OWIXlGYM04RdNGNaDedXRwDI94sjeuYQTXzROr9lOhJzCwRzUKaU9UEKfK4JmWzLYuG4W1a2uc_CMikc21_YydfY5bquRIW4xbTpYT6tqgld6JCg9Z7fL3wz7IAfXZQzdadTufq5sA2mmW2S4mgpRDMYrBGVWv1zTFJbxFvoXVuAiPow_AhvsUzue4l-EDBnnwgzNjBzqD5AChGr18dk0Y-T4HxAS0YfbepwpH-9mlqD8SkZH3IEhHnFvzCm34mr2hunag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=gvBiFVmvUx8KXuZvBScB4dDp24d2_eUDI-oI2jZVviqZlo37IZDoKaDfHI6DGjoE69gL0ZE8DPp2jaTwd_BGL875YnzHEC2_3ifjm83K7VUOJYL8bOURv2glxEo3v5H_2dayIkPvXRi_j8tYK2V6U-nYK4G7pGP5ynqcUg0BJthDNlZN4aFif0uxK_OJRqXx3m1-mxE-HyiyjejW0Ghin3LiI0lkG4Zt20JQh9aC0EKofD9uZN475HlsZfuRriAcVbOciOHIkNj8OpbvQOjLFbqZTfTi4onra8i8vtp2Vw2-FaJizcBw5Pkm4jz74tg3DKkU09fKpZIs42mhnOMS6AZAPSL3InvGAZxjql2a9zW6OcMxwIck89LbR9YbzdQqA61YfbTnKirSxPVkKGh7cGI_1Fk8p7EGFpWmytHJ5y8aFoFiq1Lm_XsHygCrjNke3eufNinowpU7dqBJOwf4AV4jaa4m0dHxbVYs3IKLLA1kOTDM_S6qz8GQQY46B9-QasuwKkTSM2QV08eXKGXdD_CtKV0_ebJf9nD-V1qpzWgXhM7UCmjgdVBlZYigUC4mHGq8Sryz5-wJuCYhRTs7scxe1OgvGeJhAJt64AgJYPpyVI28Y3gSJy9PFEWcPkJPQ25poQRkljXTEux5iDYsPkvl5oXyonE5ofY9-pGDCr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=gvBiFVmvUx8KXuZvBScB4dDp24d2_eUDI-oI2jZVviqZlo37IZDoKaDfHI6DGjoE69gL0ZE8DPp2jaTwd_BGL875YnzHEC2_3ifjm83K7VUOJYL8bOURv2glxEo3v5H_2dayIkPvXRi_j8tYK2V6U-nYK4G7pGP5ynqcUg0BJthDNlZN4aFif0uxK_OJRqXx3m1-mxE-HyiyjejW0Ghin3LiI0lkG4Zt20JQh9aC0EKofD9uZN475HlsZfuRriAcVbOciOHIkNj8OpbvQOjLFbqZTfTi4onra8i8vtp2Vw2-FaJizcBw5Pkm4jz74tg3DKkU09fKpZIs42mhnOMS6AZAPSL3InvGAZxjql2a9zW6OcMxwIck89LbR9YbzdQqA61YfbTnKirSxPVkKGh7cGI_1Fk8p7EGFpWmytHJ5y8aFoFiq1Lm_XsHygCrjNke3eufNinowpU7dqBJOwf4AV4jaa4m0dHxbVYs3IKLLA1kOTDM_S6qz8GQQY46B9-QasuwKkTSM2QV08eXKGXdD_CtKV0_ebJf9nD-V1qpzWgXhM7UCmjgdVBlZYigUC4mHGq8Sryz5-wJuCYhRTs7scxe1OgvGeJhAJt64AgJYPpyVI28Y3gSJy9PFEWcPkJPQ25poQRkljXTEux5iDYsPkvl5oXyonE5ofY9-pGDCr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FxgDHz59HoxPGfZgw7VDZg0WJKqCSLqRhyxzi2zcx7VSmbF7cIxPx-8HenGYzILsxPB2qwIT2j0YZbhC-8T7c2_Z1WpqioEiI6CvI-AURypVRZwBae262SROi33hdeZsj7NvWUYJRK5BTP91giMyJz3IIxn5PUSH8EUBCjcBm5KPIXa4Uf5AEIOA0oA4-_x14YmT4lv5Zz4XCwkB6BkynyW1SBIdljTiyID1-eP5m-hz9vHlhquNXlRc5xGo95XvTkyEblrAfBtmywGIoV4k3CL5_HlJHQcUwl7mUYYddbCHUZhcZlcbll6cpzBBTRkDrj9w_AGJaVokYRnEY9hPww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FxgDHz59HoxPGfZgw7VDZg0WJKqCSLqRhyxzi2zcx7VSmbF7cIxPx-8HenGYzILsxPB2qwIT2j0YZbhC-8T7c2_Z1WpqioEiI6CvI-AURypVRZwBae262SROi33hdeZsj7NvWUYJRK5BTP91giMyJz3IIxn5PUSH8EUBCjcBm5KPIXa4Uf5AEIOA0oA4-_x14YmT4lv5Zz4XCwkB6BkynyW1SBIdljTiyID1-eP5m-hz9vHlhquNXlRc5xGo95XvTkyEblrAfBtmywGIoV4k3CL5_HlJHQcUwl7mUYYddbCHUZhcZlcbll6cpzBBTRkDrj9w_AGJaVokYRnEY9hPww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TopTTai1oYZ-BtmgtMuYQb-nyL2qhoNqFqkYkkCpvS65COIoC_om0dEZJmaVxrgjCo7fCbofTv3tBzYbR_ffLvM7kcYUKwa_ISzn8QZkZWfcO_dKAU91sAqqL6Ig6dHgy0KZZGtE1k4NjPFmMiskuCfqbuSguxQJArYXuX_Lq9WntaeEOBWSdGxSI5QkJEp1QCjcmNKRtL5z63sEEArZ7cOMpeXpfsaJFAaY4bgksF6EGc8p2mYdDZmwojlkbkV7NRtw8KH3TFrlNWwE2lOK7Ef9Fs0bAJtRyKWC-c6rCY1tn44xJ3zhLWgkXfKPfbtXhFF_rgZfNqBVeSfLxccF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gmXWeallXNRNRlk0IxRekP5jX-nFag36J1REY-gzcZtNDvIR3K1Ky3MZRYkBBIBede6rMPa49hY18ZYe7Fer1Q9OC98q8ugZC0V8Wp98r-2xAi1-e3a6GxRmgok6JQGGnJRK_GWO-cPN0pEpF52redbKzFHntaqQF53kRLq2o7QI2VgyvmTGjJwAPYCc4TLKRHRoya1DDqbFFGDNUfFSpZlu4jR61ZUXVtq5H_ZEGUydKA8EgyAlkJda1OkeqiSROapZkgj8OVroLayY06Llq1PYsdmBQszLp9_ShET4MawAM9wAWVTeefWxhcZsnpMv_VelDnGo0xIbzhp4E0NuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gmXWeallXNRNRlk0IxRekP5jX-nFag36J1REY-gzcZtNDvIR3K1Ky3MZRYkBBIBede6rMPa49hY18ZYe7Fer1Q9OC98q8ugZC0V8Wp98r-2xAi1-e3a6GxRmgok6JQGGnJRK_GWO-cPN0pEpF52redbKzFHntaqQF53kRLq2o7QI2VgyvmTGjJwAPYCc4TLKRHRoya1DDqbFFGDNUfFSpZlu4jR61ZUXVtq5H_ZEGUydKA8EgyAlkJda1OkeqiSROapZkgj8OVroLayY06Llq1PYsdmBQszLp9_ShET4MawAM9wAWVTeefWxhcZsnpMv_VelDnGo0xIbzhp4E0NuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E2fhyJeNJvkmbQfL0TNP84JGVAIqjyiQlOiP9lRKCJu5I7YjWxSXMOsLWiniRgKJask7Za-QgYq6VvolOnaybAl02UwLOQ_fJqOLMBqCd4BLbqUXyfK0iaL88kTvRo97_8Q7McQgrH9p8XTmfyyipS5BEg5sAzEFs6AqdoF6FAnem4mmR2lmPUlqwEPKXDXmMEKjeomovAxZapj4sSGBqqWeYH6CAta3CcA3yDd1e3f8IdYPhuT52a-OGZtsuiWC3MNUaWafmJJYUPPxDH0JfX6Um2DfuM9v0Ezpw2ymzmSI1PvdbhNZgNLiJ9KXSD523zWunSALJWj1Kry6xC41xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E2fhyJeNJvkmbQfL0TNP84JGVAIqjyiQlOiP9lRKCJu5I7YjWxSXMOsLWiniRgKJask7Za-QgYq6VvolOnaybAl02UwLOQ_fJqOLMBqCd4BLbqUXyfK0iaL88kTvRo97_8Q7McQgrH9p8XTmfyyipS5BEg5sAzEFs6AqdoF6FAnem4mmR2lmPUlqwEPKXDXmMEKjeomovAxZapj4sSGBqqWeYH6CAta3CcA3yDd1e3f8IdYPhuT52a-OGZtsuiWC3MNUaWafmJJYUPPxDH0JfX6Um2DfuM9v0Ezpw2ymzmSI1PvdbhNZgNLiJ9KXSD523zWunSALJWj1Kry6xC41xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XifRodSLsu4LwQyKRNsbKm5BSGM4Xxrr0OgzkXzImJVmIfbHqF5iherwiPMxJ-4CQEI7gJ00W841xzJOwf52THKxOt4ZXShC0O6uhiB6eXzFzbHE_hb9LRImae5ajpi17ZOGinDL1114gQ9M4_74bX7Nn04b--sKaCCrEaYgCIa8DdJEAqgLzzm5hKKcrZkunCEceSvzxCsUe0c4gG20YC3NCcciCs_8WjuTXig6MGInxM9CmpRfAGn58ogYndTCYg6bfILnGhRDrA3jM7cJwwwx4Uw2H4sS9aO1wwSw09qxkEveM7ELWerkfs6J-JsKenaGJPhC3wjrhrdxH8CWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU9j_ndqCba21IzYP4t7ef1K5meOJs89e6eHs6FmxWR-T_9nHqB6SOY-4bIcTO-8tcs-oMUfG7z-nkue9OqYrovvpJBOqsZT_xpIFya8fluGLGFomiIA-UZKgF8lvpDo8-j8NR0XVP6gseyiCR3tk_TVOF_vxhQubolNlX9pU00KEUsNRbGQ1688LAxEdR3L7Sh7koULxMzPeZYH32lnNRnXoIUwrFUjkULZiscGVGsiETgHb6PgsW8OpTqDGL28Sk9Qbz3lTkhOqQ5zq5Yx7voEjaggU4beTRJi61hi6GZTsdSXU_V6pMoLJMH5jxnc_Q_DIT4gN0Lopan77rzpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eByjY9f0ISky4RTz1ntnX5a5BlKsGaaBxByByqA50aH0WJPA061g_wZO3sgD73LI15vAxNVKOKC1Q6Nd3pDVrsY6Hun6cYZl5cNUY7VsjoA3dc_mGPacb_zUoO2D8I3kUo9Sp1g14x7dJS8X1Zgz3yXl8ky-gKwiuwredZS5Pq65uw110f8V_la7eUrriIz6OZ1qkOMiVFVUnbyrxC31sXRqGw0zXhF5_Ri5qoy96BRMmDFsJfckxV3oRHrUsgHa1mDcQ78T9mNaj7kFoGLkf_qfkl0u1HynyHBRLK84vmcFEPTUa_JSkLzr9fMOegzZ-crAXXmtQQneXgPuvyWopg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stXcVb5MnfuKOs3mpn2RPayVDjOY2CN_ILa9f3H6HVLVCTn5qi_qNvFgCc796foyAad-yIEzKmtSqPIa9DezQMwmrS6ToIWgWREYy9V2afeCaZe2ZsCa4xeGv5O1X8-ASzwCZId4pyOZ3nBM5OeUr9uqVnO7emb53vPj9sqwtxoI9gXXvuL-puONeZ0BIaFBhMWiYrNpJqpO08ALM7qIFVaEdIds8RX7YKrJituBPPI1mg7ar3NUsjZP9XIFU_tdS0ImX1lbJ1rcQRCMTRxvOD-4qpDioY12iWCRDU3tw3ghV-I1nfnOlJtfbYOQ-rCuo7IXt-oE15Hpd8_xyee5Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBIaHy7vfkyb2NkDZso-TAKaGzRf2I0pn2jbziWfabc2PedwuxFdfHT_ue1txL2MlWV9n_5-Ijcztv4Krw4QYYGgloz-HgCZVsHj4_TOcUIN0DRgrjmHG0AvE6KUPi9yAL7ECd5_Qk1pvO5mCyMMDJp1ehrWTr-O4yutGcwddLlevqMI3JMsStgpDEkghLa37SRbKX_jjRzYwBe1W7QIFsvbtW2xUsmFsLfSFT_BNan8bkJ3sEU-UyuuQ5sOlMZ0emTN53-22SVaMKgauM2_Pf0LWRzQ5T7wG93WN_BOdvj7TRYQaWNJROzOrpI-YCQv4qWgrC2R3Ib8-Kr2pzOYCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxC9SOVBA_YtFDIn7a0Jb2xEhcknjq4eTRlvEZUH1CEcEObu4MiXsdJbNUu2-obczz3cWGfW3BZjllyhBgvZdEUGNrVRkVbgHtjxY3UvQktVciCZbQuhHAW-GUv5-Qu3oR8rorZ-o0_HYruFmBFDoKmAvEn8U9irO6kXF9Vc0VT9aoYWoisZQO9yB4CoP6jeh8Zo8c14lqWfvnym9mU8e8PPFkAH-ZAw8Rg3ktZie9wjSBlxRvsNrkaVGTkoUu0_fXqBxT2OnijKHpfCI-IE8ZbNFAIQ6HWPGKLPEHXwxG1s7eBMmd4Xb_sWUySUg6h-fQvS5bCbMqrebck4EfXlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIVMB_k670YwPwXxihYF-seoIvhrar0OYsI51ULOPlmYQxKR5CDpBRD5KDZU5uPgQXanvyikvls-RDIES-AS_1OsvPyUSyBIYq4_no84mgNfCU70I2xVvE21TOMLaNVsUmFSjTRy13a0LAAIaV2X_TsHJhgbJ6CdU-QmHdl44kGHq3VfXVRebYUyaIJGm2yLcp9ha_XZCI1KZbjiOa2FbLLtlqJ_Jc9nzr63pFt3i6pYLl_smoUR2spL7nPjYWkuJHpW9riCFI8znwZVQpxro9WrLRs4T5yIa4EhYQ_IkoOTU78wqA7kBAXsUfBJX58eQorkKJp2hCwgwtyfDQfMQQ.jpg" alt="photo" loading="lazy"/></div>
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
