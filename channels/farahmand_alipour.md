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
<img src="https://cdn4.telesco.pe/file/n6-fUugsXe0iKAIfJ9iPtpahB8taKUpwUVnF2fYKqi5Ku3vWkeNov9CFwjcQgORACVpqXt9fUFveex2qi9ptp1_ngEp_Y4FufNulLouPgE8GxVNmqhTv2wBwc6HEyBYpi2OehvKGVVYQNybObnJLZGBVQg8-RI0LJk2JZQswSnUjaYHWn8NGWFtJZe4I_x0Ggs6B9sY8xEP4MNFBUn8sTs6maQ4t7IRPDEks5J8O3DRX6EtZrbNtqk5gQdCjB5_i6jjuQDi1TpDt5fLnhkWMWQfpWM1KdobjoDT9n6iULEEwEJIpPPm8YOmDpO1cKRjMhO5TJdbSgSoKnQJt8AQEqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxwKw9u1wKVi0le3sqPFXJ3CxsF1knfLf6mNDFc0QMEfDEnyoTWDWIcxmug7nrVAoG0YilGx548apFZ-Zj41EHFoTSW35j3jTyHyHTh_TShFp_IrNO7oqMxOgnInCivZqCMVJj2JHL71X9Q2ZN0n2NAyZwl7Yg-dFW9zpebWRNciy9cHlGdkVfrDgFVNRa0eCqk0QNhJxmA2TgITHvL9zof5OHPL4HglFUgbeNJIifrwDbPu38jqHL6PVnnJIwEw9yOCZIqhJCxLgLKIH0lBRgXa6naMBzoTF2dddu0otKs7BgQR8GS6Y2Lp6v18q3ExCve41eW8y9yXUgz8payoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwLtWHw5_hISQChZ86HTRxpxZGRid_ZPq-UZWWIeyZqHhmq4Ip7g5wtxbAjGOcy6knJEQCYhER2Wj_wJdNDrDJ3p0VX09GVfKwwH4DJKtWnGXzT7ZdVLOYX6-_85n34BZJX_lrX_R07EHZMvKOPhNQNe7smnwyVlEQL3AeDOlnARMtUurKcVaqKgPdqarR5EOjBpzkd9qtG5hMIX7CgTbHFODB6qc8bgHveZmvHsaziXB5SH4Dt_jWqvP9AkUBdxSGoQPvlUfFqBJCIyNOGvrd7KR-u5p6V7cZ_dvxWEW-UDq7GEJsQmafYa8uGIdRfLiROaUDKXx7zD1iBixbuw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5l21qnWUuE0ubqbRoE9QWPC3YWMesYusFHAB1JZltgZK61tZsweRAQLzi9Ve6Yg-yTBCIL97xDRZA8Zs2dX3B-rEECDcC87AfpVcSKmqZB_ZhFh6TGa5ntu7NGPmAjT5quNWiXVbTm7o78ybOMN3JHFPoTxmuqV3aP9SUWmNRxbVmuglAof4BeLyzjoqKPz82BJ8ecvak3Gl5GGOyEpSW9PxI9oePJCgoogNNuFDaNoTMPF0Yivpnyyi9QQi4YusxsF12S48y1HwGWbMXKqaf_TL3FoBoQkicH_4evOHTfGm8mrvXNIzDvi3ZOZ-ORLraT3B-95CSXaFMayRlsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ323fh_ZI4goosekrbUeky_cTExGCNCfpicV5PFuNxmipKcPA3EFwOyyFfGIxEJspPlMmvmU-Jwl9Ac3Trst-ALK2AuSOW5svsZfq0u8Mj4Ejl69gUeThPdA2i9wvYiyq-qTqWQ18ePS2WJIEwDID2hzNkX92k1o-M1v7V_yDBkBpTvBozoe_GgjLe4pMTBf-wB1-AmqFBl0T8oTQDVMtt_WiVFHahQd2WRMxHo1Utv5ugLyEpt004AEu6xfsvmPTxBkPBF2eSfcadSik-NI_wRdJOwdGjsGl7fdqyBt5CmQLjbl3oeM6Cix9VFEln1zx2gmTWrrMXGZIV45AWlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r84fnfGD3w7SypFeQRutIuRQETNMjatl43OKsKUsla9jXZXLPNJpznxv1KQr8pnLn6zPQGKyJ2TP2hf0HbsWkJiIMJIC0H7RfOo-xTBpmTFhPbiEEx0oxSP-DijgUcZ0kppL1ByOOJ-GVUet5KELHQhMvBrR_aMGxPKU0y6tICy8OtnSoiI3K3L_AX2IfyAYHHJPMA2ipC0SuK2IrP4ccuS7lQxHfcIpYEYZRLFCFylrEasTwloq-MthqkG0cVXoE4wbwRhJeAe3fDcnICJpzIqrTrPJIHXanz83djYoQGWCDBdEvunEFY6Nefp4-KD2bqNP9Lz3i31W7Sm6PqyFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSQCxqMjY2v41OcrWsNunGe38UdtxzFGgF3rjyB70Q16QdZVOoJYnEXiXd_tYxwNhT6Rl4wodZuPBq9uypRsj5OKj3_LFbvhif56OSIhDCEjgRj_wlpe6ycDmLg620zWhof_tgbI2y0pFutOHWdOHs03dDJnNEGGEvOzqsM8lD8KIqw-zxtEPl6UYAtp2ix4NmSqPBnp_nIAV4-4zdTLabnDj2tWhtPNBEzFnqHFjlhjwVfLcFpYB5_nFFM01uCHfnSCfrDEY45hVLR5qvQuzUqvwQHSySepmUu8EQKyl8YXkaAdHKM4vDEaWRxOug4X82iic2NMN1Du6Iwnzdiaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=gFVFDlsau8p3gK1XwazWPyT_RroYisBG8RmL8LB-EDnYmfkyd2fsaCAl_TbowJ_IGrrbT5HBWkIC3-O_9xdjSfFiHWfTgZQVFDQwh2CkTsFVfkwJOGCVeghZwX3FQ4zKBWO3v5AitUNhk6wNTdHdJcL7ORXTBSMbyPOEpp7bkvHOhsmQIhiCC6SGlMUbel-MZzOyACxt3JAAmtL9_0ZbsZD6V_zLuXbunTqHCFW4UTvU3xzxIYYS7KCWlh5CA5VP4bEfSwalCOneLkQ-nI5_urLEqACbEORSNC1uTsr7GQrCpo1Mz0b87KSvqf9AxduWMBVbKgcgQbdOSuOGFN02Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=gFVFDlsau8p3gK1XwazWPyT_RroYisBG8RmL8LB-EDnYmfkyd2fsaCAl_TbowJ_IGrrbT5HBWkIC3-O_9xdjSfFiHWfTgZQVFDQwh2CkTsFVfkwJOGCVeghZwX3FQ4zKBWO3v5AitUNhk6wNTdHdJcL7ORXTBSMbyPOEpp7bkvHOhsmQIhiCC6SGlMUbel-MZzOyACxt3JAAmtL9_0ZbsZD6V_zLuXbunTqHCFW4UTvU3xzxIYYS7KCWlh5CA5VP4bEfSwalCOneLkQ-nI5_urLEqACbEORSNC1uTsr7GQrCpo1Mz0b87KSvqf9AxduWMBVbKgcgQbdOSuOGFN02Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=E5rX-hmCYl7CwcBBSdt1ylPHNuudpYouCTMyGhQR56z71Kfr5duqC0v7lMddQjkQLFulsqw7YpCEZCPRB8SFUPssdrx2YepaJMaeTjtRG03p1hGcRCfleEpFz6SreZ2QVfRfsqhFCNF-WH_ichbrLUWPw_vVdGjdfQuKw2QZWc5BLnkouh9MQd_1CbmhHhOyWkJDH8_aDAeYYsGdVE6CKPkApEpOL012WvYoqBWLm1cCXXmLRbGkWQjbdC_awoKvvxzbegLTha2B5HgzZT6p2xFwpa44iUKr80-_rPwedPex_MQSDf3esGzHzEsuRepFWOjgf1WU_Jl8JmRNGCiT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=E5rX-hmCYl7CwcBBSdt1ylPHNuudpYouCTMyGhQR56z71Kfr5duqC0v7lMddQjkQLFulsqw7YpCEZCPRB8SFUPssdrx2YepaJMaeTjtRG03p1hGcRCfleEpFz6SreZ2QVfRfsqhFCNF-WH_ichbrLUWPw_vVdGjdfQuKw2QZWc5BLnkouh9MQd_1CbmhHhOyWkJDH8_aDAeYYsGdVE6CKPkApEpOL012WvYoqBWLm1cCXXmLRbGkWQjbdC_awoKvvxzbegLTha2B5HgzZT6p2xFwpa44iUKr80-_rPwedPex_MQSDf3esGzHzEsuRepFWOjgf1WU_Jl8JmRNGCiT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=F8WnLYhh-6yZneQ6NeZ9QM2csfJooXK5uQ1O45PNuUjYdQlta23Jt-A-V29Q4zol4vKANJkeoFYHhsg4OQRSNWL1H9xr3MiG4jDbKfCVyf0JUTWDdGpKZAeKaBj0h_slMe1Gvs4s2SEnmS43AIPO-PSRT0AIRtlkkOsZB2QtSfTNDJv_Dl_sIQAUROVR6qFeW5dsIKTFDLnSfnamo-uRGLM1XgEwHU5v46uoTWKrxghJiBY9WJ1YH_o9UMingH30VmNgrImKa_tRVrOqUIXYPDSqmmkLymTaRwD26h_3Sr4tqUb-cID0mHVQGRELY4KdA-6qRrb7qe4N3TMzWELhwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=F8WnLYhh-6yZneQ6NeZ9QM2csfJooXK5uQ1O45PNuUjYdQlta23Jt-A-V29Q4zol4vKANJkeoFYHhsg4OQRSNWL1H9xr3MiG4jDbKfCVyf0JUTWDdGpKZAeKaBj0h_slMe1Gvs4s2SEnmS43AIPO-PSRT0AIRtlkkOsZB2QtSfTNDJv_Dl_sIQAUROVR6qFeW5dsIKTFDLnSfnamo-uRGLM1XgEwHU5v46uoTWKrxghJiBY9WJ1YH_o9UMingH30VmNgrImKa_tRVrOqUIXYPDSqmmkLymTaRwD26h_3Sr4tqUb-cID0mHVQGRELY4KdA-6qRrb7qe4N3TMzWELhwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU4PdTUvrhUZQmoWSMNUosgws0KD5MpHyfbqWbT_W3KDMjXwidqVWf0GvaWvthL9-fP59KevzWmwM-e6iFjXBEzGxkT0K9jkqSxxhuBvx7ha6OtK2oUEstgEpFmhgYUjKE9F1cc8ZvtWKRKwJGW0LUK6TamHsVeMZxIyJGDoKbXXh1Ts3R8L9y_t1s0BVJWbU9uMwEdmgSvFU0Q1QpKV8KZ5tLF7DjZuG2rkyUTKlK2BhHBseqg-SJ-h8lwVhl5xoiV-plZFLyKYA33iia5tKiVNOSDtZb5w2fQZXuCIWXoW0T_QMqvA9UAIfx_hD6gK7wojUSGlhlupIxxYgjI5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JVlG2l4EtaA4a2HgDoCoOqck3Gc2CImZwQfIhA-0P8jR8CitSCg5woGeSTruT6KAwnAPbQ_mYJdEQI-dN7LQmE-vcLHqTn7puQvjqGkFiR4b92wcBs8Chd0OS0BJunpa-Z5iOzA-jFzfhPcOFGSq1CMxFZJ2_hbsh9ysxsCygdoCo6NMnlHfhN_QGgSvabltproMJBwqnA2EJllPhIWQO-PLDO-SL1RLdYuoi1XLDR0yliSrHnUgWhiF9B-3XyCtXy49E51e4rbSM-VBMmt1bV5ylFbWzWOWXj7o4R_1tPQFsHw6xREphbzV_J88dbBiXwWrH27eyVD3FkshNxmNzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JVlG2l4EtaA4a2HgDoCoOqck3Gc2CImZwQfIhA-0P8jR8CitSCg5woGeSTruT6KAwnAPbQ_mYJdEQI-dN7LQmE-vcLHqTn7puQvjqGkFiR4b92wcBs8Chd0OS0BJunpa-Z5iOzA-jFzfhPcOFGSq1CMxFZJ2_hbsh9ysxsCygdoCo6NMnlHfhN_QGgSvabltproMJBwqnA2EJllPhIWQO-PLDO-SL1RLdYuoi1XLDR0yliSrHnUgWhiF9B-3XyCtXy49E51e4rbSM-VBMmt1bV5ylFbWzWOWXj7o4R_1tPQFsHw6xREphbzV_J88dbBiXwWrH27eyVD3FkshNxmNzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=kbAbnygfRaIrBolGkIjLgkYsWHoyhG6_99LyCUuXmE6_l2QbK8eu-LEGoypd8Bk7iIzR03jQGMikgkaRF33RWre788GY0OjEZW4VzM_O7MQl0edkzZ0fWKaHs0tl3DBD2udXniMgbsYlekMAetKkDpbIErvt8Nw3kRLXyEbbiUJO0Uttvm_fAZ5nPC5sJaqzLFYLhdfQwpRURsOVl3m-I-Trrq2QOBHFymDvYG-GaHTBWWbaRx6ilQxLzNUlDOS1NiuqTGn2kGk2uZutpLwQKZih17jANprNmBPPBkn3fX9pGXq6Sc0ksPWsSiqIJhJ0_70XCm3CneZNHoBoz-e8og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=kbAbnygfRaIrBolGkIjLgkYsWHoyhG6_99LyCUuXmE6_l2QbK8eu-LEGoypd8Bk7iIzR03jQGMikgkaRF33RWre788GY0OjEZW4VzM_O7MQl0edkzZ0fWKaHs0tl3DBD2udXniMgbsYlekMAetKkDpbIErvt8Nw3kRLXyEbbiUJO0Uttvm_fAZ5nPC5sJaqzLFYLhdfQwpRURsOVl3m-I-Trrq2QOBHFymDvYG-GaHTBWWbaRx6ilQxLzNUlDOS1NiuqTGn2kGk2uZutpLwQKZih17jANprNmBPPBkn3fX9pGXq6Sc0ksPWsSiqIJhJ0_70XCm3CneZNHoBoz-e8og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2-LUQoFQIXChTQVw2hhHhGsZn5f7njH1aGaRVpvcUx0CX7ObdNrhhIuSnA0GJniskYeMYwBXCwB9QAxuATFzq080R4P0DO15rLOpKG6FPpvO28HFGCV0cFrPIq7ugzRPq9u2YcDSESJMlToG-SpleM7e9oXpDstxDicx9w6S5dKYWWoGsmLAE1ZTcJFzOBim65IIsrQXLE-c2_JLU4ylOztuip_xvdfVvSL9n9PeOv9OpqsWYcD0lYs2vepQ0nloRcd7OF2QjHjVO6i3aCG0Ti4c-AE9HexiyUBpVqBfWMUabIi4x4NhUklvkmbmdYYAGYVYqAjisTG_TmnhhEwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=p6Y-cNiRSdih1JOFjlGW3q12JU0GR7c7uZiJLuwoKVa6CXl5gWU5DjKrKCGS1jlwAIgUvE1URHtWcGSIusQC_0ZaQUhUncdAtaNX0VBlwUrjbR72AK24RPP674cOBPJaXDugXH4UHRRVhaNFKMlzaLFQT4WONTXxQSCG7-Y1daYvkgPdEPkP1mGPNSrYYyMOraO4kIVK1g6B1AB6y8OLzK-dlgha1UyDp88keWoRrFsPUBMKfly9Yr228E6VVhxYa7ICfa780OxYAsI8K25uHoXoCGz0Q4tYNooSmjs-HV232G8yCG8g73c6Ue18xzdAWjHGwwhlBwY8Du00ouIJ5EfBwkN1nW3jpaDg-zzXK23xa7IK46eOYkZ2okhAnYAcBl-A7BZN48CwLK7IUqaQgZs_PJN6uXbRDhq40HoHst4NEoCrQGtgb10tbdxylB9w7BlXiI8WMLFPT6MjD29mm6EPwxxlS1lHJBIhqIt2EmPNtZ26OsrdAl8w1wximslmlBSgPhAmchTvUM_3VPSEoh1cXfVYO48LDnYB04Vn1bap1gOws1Mu_NcXKaY1B94ScMjHZVxR92NRSQIeBqBmvG_-C2O8zAPOdse9_teLFIgLiUe4HvJCiSEsdVEAFIdG2vyNM7yPu-YHPlz7gEfnTChYg7kWAw0GJCreaje0_v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=p6Y-cNiRSdih1JOFjlGW3q12JU0GR7c7uZiJLuwoKVa6CXl5gWU5DjKrKCGS1jlwAIgUvE1URHtWcGSIusQC_0ZaQUhUncdAtaNX0VBlwUrjbR72AK24RPP674cOBPJaXDugXH4UHRRVhaNFKMlzaLFQT4WONTXxQSCG7-Y1daYvkgPdEPkP1mGPNSrYYyMOraO4kIVK1g6B1AB6y8OLzK-dlgha1UyDp88keWoRrFsPUBMKfly9Yr228E6VVhxYa7ICfa780OxYAsI8K25uHoXoCGz0Q4tYNooSmjs-HV232G8yCG8g73c6Ue18xzdAWjHGwwhlBwY8Du00ouIJ5EfBwkN1nW3jpaDg-zzXK23xa7IK46eOYkZ2okhAnYAcBl-A7BZN48CwLK7IUqaQgZs_PJN6uXbRDhq40HoHst4NEoCrQGtgb10tbdxylB9w7BlXiI8WMLFPT6MjD29mm6EPwxxlS1lHJBIhqIt2EmPNtZ26OsrdAl8w1wximslmlBSgPhAmchTvUM_3VPSEoh1cXfVYO48LDnYB04Vn1bap1gOws1Mu_NcXKaY1B94ScMjHZVxR92NRSQIeBqBmvG_-C2O8zAPOdse9_teLFIgLiUe4HvJCiSEsdVEAFIdG2vyNM7yPu-YHPlz7gEfnTChYg7kWAw0GJCreaje0_v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYeRUVkzx4BQlGlAhJIAHcFhz25Y1mZ3vc7PhT3Nj6OKrZPvtKVHWYoFyn2XcBknrW6bhGJpjwo-vlIyrsVyM-IaTTQRBqGPB1dNLkPQaZ-2LTyaCTTcMssBqgNUmU7VX3663khueH4mxICcjoyRZxhQ7ubrGqPZhlahezGUSP3vLhoUzSSVdz6uiPB1ZR9LKIWKFmVoI1Ro2xJrzU2pVk66uL_6JjhheQAIiJK-Fji_qV-GlYT4UC0C4ltp_YczzzyNiHkxsuJRh99E92tExkESBUbjIyOFluNnTDLvW9Zr9NvRFgBL1sOYfagb4ZT810Jd0F4-PVwv6AiwXB60pQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UicK97YMLcBQJuvaFIszHE6QeVQyvwDrdSa09Frp04t36AEC-kjA9rqqijVsfC4-T4qvVj0j_VaTknqV4SwRlxc-ta6I86R7hNWJk52pEIr-1ki4oEHueZsvMqDltNmiR9lr33rGL0jk-6wiomDYyx4dEE597RpY1_172v08OlOT0N3htHvrF2ClPpwj2K-yDY3n4m_F3YIizLcw0ibO-Lx-FQsJUmi_XwvJXejMJ1n02A0qKXxR_e3uU5wHuct7yCofdPOuC7BqW25isegAV5ipNuUo8sFXi2RyvNgWfQDvNChGmhGoE7LWM3hxpOkvMIF2cGaKlqB2_IkaLdIHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UicK97YMLcBQJuvaFIszHE6QeVQyvwDrdSa09Frp04t36AEC-kjA9rqqijVsfC4-T4qvVj0j_VaTknqV4SwRlxc-ta6I86R7hNWJk52pEIr-1ki4oEHueZsvMqDltNmiR9lr33rGL0jk-6wiomDYyx4dEE597RpY1_172v08OlOT0N3htHvrF2ClPpwj2K-yDY3n4m_F3YIizLcw0ibO-Lx-FQsJUmi_XwvJXejMJ1n02A0qKXxR_e3uU5wHuct7yCofdPOuC7BqW25isegAV5ipNuUo8sFXi2RyvNgWfQDvNChGmhGoE7LWM3hxpOkvMIF2cGaKlqB2_IkaLdIHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI0KecqLNYD-FdORWiDLGon6W7nDqN44VclNW8nrkkOUoGt4Bx4KOpOD8Vy1MJHeOq0C8mtedUp-jPNU--k2r5CzpuxjM0cRS9jk3v9AfxvL1SJPy4vwTNJ-k5TDlBqNX0Iqsi7c2R5ppg1isD4sx-20LQirSE4pNe5aYeXzn-an788SMs3FkEGfx6xAJCL6LDV6R5HHKPpRBEcD2JeO_TR8ocIgM3EpYWVG_EKAp6QDWNcN1YsyflKDx04soxPKEUv4NactALGg7HcXKIB70OXERHbEeTTboCi0fZ0EhnBsP01o-9GK9hD7H3qNQmY-SqmVjwcvQRLFDoJP3mGxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA-k133QbpbzCLDWCHIMhMTUzmKOS-aVeMsk5hkRwOPSYwF4yplCug1MDL2-hWuHQrlJON9TwijcxBJyamQvGVNL0I_Z4NeT8Jvcd9tfIPUM__8oTHOS10Z_Mx5GiFprbQr2md88uGDsKLLdxPUEckfAOdBF2NsExXiUTB7VgqZ6ti3890Q1qLMhZcBVNmZHNFoAjS1-3StTLPp9ssgeNcRqYxO_jr0nclfgnv-QmZaKwcfrbJ_0RJFuBqZaIJR5qXFrLSyZUcLldKvbb19WTSov5UWsuhEuVgzUV2qf1O3jZx7xM9tEmZ3A2bA9XTb1nu5jvHMb8G-5RRvJKYhKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dARnPD0FxFpUHkZ2Y5wX8j9PQZBlefjTF4cjFjWAUpWXQy__-K-AudoWBv8CqKEFQPMB2ue4N1ZbEKqv_5lVnBRXOlZNv8w7GwXiENdm-jyh45RhLeyUV3WPABgEJjZ3JR1JqlYlfc4lmN-jErxGsGvdodAzoW4FuDmP3OkSc1N5oGSmsVD_AsjPEWPRFSnnjqoAp0oG_LwHhz_YOeM5ydExeDRqvaaURQPjsyBh0IaqjAAjgmgj5Nw8pTn0TNeLgeoL2d3_9bbYdPx2Az8yOaSQ3dgI7IbB_dytSkDuwzY4XSsQ0Joy_ea8yLfXTQwh8mUI7193csL0SlxHuVnQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTjzSymzAiBz3glVtbumLdbouxPg6d5WZcKsPUyXXE7iWLuILWo-SThFmUHELzNqrdpBem9gPam3WBcpBj-RKwDzXjnKgUUE4auHMld1Np4Kl7PMxVrVe_On6cf9Oja98AUK5qospZZuhGjRDhiobJf5SierMcx-xLouE-rzlYekv2SSH2PJchJJmIYVVJPndD8sM3-741JbQOdruICFWbmr-nFDoQjoiDXMzvsy_Fyu3DJxlLWWjw8klboiLmz7Ju57fLx2jY2qi3tj9weqTWRBjwbrg_fVLlNZmelvTSxqA5cMrm0Px1z2TZxD_k1HVuWgfHRUKsqwq1Q5Bxnb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0JMhdcfd2uuyEenWGkVBFg3Kv00p9vPpK85PBwXUL_BGiSvZmUKM_jFbw-yPBdv3mIaaH2P0pS1k4euwzW2_VhXYI3u8QXWnFKqs49IAT3HcwKNOCFWWQfB4XgzEScIvzEjgYSPEq2CEL6HudmJm287fTMv03OXgWVsIWzBZfGlUjdz2RtQ5Mhwxd1prpJPSN_MXJmo6fVVM-aDMDDdjOjXkFn7QboukPtS0H79VICCyLM-76lCiH9PuLVtXqxF3bRtpDzqLY9lWiaWCw9anyQRBL_s5hnypvXDIxXIGBkcjho7ln09vVZOybW1Itnq12TSMwTJsrxQiZMUMsS7qX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0JMhdcfd2uuyEenWGkVBFg3Kv00p9vPpK85PBwXUL_BGiSvZmUKM_jFbw-yPBdv3mIaaH2P0pS1k4euwzW2_VhXYI3u8QXWnFKqs49IAT3HcwKNOCFWWQfB4XgzEScIvzEjgYSPEq2CEL6HudmJm287fTMv03OXgWVsIWzBZfGlUjdz2RtQ5Mhwxd1prpJPSN_MXJmo6fVVM-aDMDDdjOjXkFn7QboukPtS0H79VICCyLM-76lCiH9PuLVtXqxF3bRtpDzqLY9lWiaWCw9anyQRBL_s5hnypvXDIxXIGBkcjho7ln09vVZOybW1Itnq12TSMwTJsrxQiZMUMsS7qX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=o8QDh3qlV8h84tgQCRzykbRfEXJMg0jrP8SNgT2vcx_MknmFQz3ny6nxt655TCERsNJwiKNANRGOnVXad4Sw_QnRjO6B55ur-ihTMxbmxi7QBhWYHXPHfHpwoP6kGGCxufO5KXoxsns5bxXGYLLD4i1pBAl8VYbQfqJL-xpkTU7Kpm4lfhcRO2RxlSS8ExPGYp05eLNh8Fz6YinPgaYqyzD1-OLSiml5I00PxRGs76mQx542C_eplPYGJwxN_BjEbmTpvmIWw9MjI5ICT834q1MzOSFrB5Q7IklwdtOdHLeQecuxE2UnfcaTod1O_7D_pwvDUVi2tS8revusadpSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=o8QDh3qlV8h84tgQCRzykbRfEXJMg0jrP8SNgT2vcx_MknmFQz3ny6nxt655TCERsNJwiKNANRGOnVXad4Sw_QnRjO6B55ur-ihTMxbmxi7QBhWYHXPHfHpwoP6kGGCxufO5KXoxsns5bxXGYLLD4i1pBAl8VYbQfqJL-xpkTU7Kpm4lfhcRO2RxlSS8ExPGYp05eLNh8Fz6YinPgaYqyzD1-OLSiml5I00PxRGs76mQx542C_eplPYGJwxN_BjEbmTpvmIWw9MjI5ICT834q1MzOSFrB5Q7IklwdtOdHLeQecuxE2UnfcaTod1O_7D_pwvDUVi2tS8revusadpSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=I_88gGRdSYacV2tMhLGvLbzXfHwocR5otcrhQV6O4k8wR-ViHMd8z2qR-EToBVxlIaFRew-n7lEa0DOvoYvXokVdyjXFd-PxBqOW3CbNIbTm1o4TsEKFPcHynFa7MytgVXVL1hHhin1ClveB-TzqF6UHgiAHu1AT_kwKBAzaAiezPhZr5CtR1QXFPr5xJklTyhSSEWg2QJdmJLAD_8Ae-uzUMRor5j7SIesveW6LR4k-5UE2TMLhFtNwhULRS7g6BHIyz10wJ6if3gIWmBx5BSF1drwv829NqnyX2d_mHs8e-4i2cd4ifP4l8dCWvAF86ZYjSpYR_RiMLtf8SiR2Sl87YrVbBrM_CivbqE3QiBhB8cBwP_ivE68gmW5tO8S7rImDWggwx0Sott7ONhJQMEtEqWvGQdzpT6BPdNBpcn6OWrpDaNnVV7XqCSJonTOe5fzPYD9ZGFUWknywQEXs3CMI8B0Z31zdXbQwEotVg9GdC-SaBUiT3EkPPgEXfPYP0qqfetEO-wtbpda9rTurxLbkaZk1P_9WNCnM2l1ycwwTF5OUobFNYRP5MlVY92X-AkoStvgXwes8Aq9BPKAKoHHuIzcdNOTowLhitD1lru_6YfXCQu6iiBz5T__FcMcFvryb5o4JZgX__jkJmjndzEtL7lnOjttsxwMFM243EUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=I_88gGRdSYacV2tMhLGvLbzXfHwocR5otcrhQV6O4k8wR-ViHMd8z2qR-EToBVxlIaFRew-n7lEa0DOvoYvXokVdyjXFd-PxBqOW3CbNIbTm1o4TsEKFPcHynFa7MytgVXVL1hHhin1ClveB-TzqF6UHgiAHu1AT_kwKBAzaAiezPhZr5CtR1QXFPr5xJklTyhSSEWg2QJdmJLAD_8Ae-uzUMRor5j7SIesveW6LR4k-5UE2TMLhFtNwhULRS7g6BHIyz10wJ6if3gIWmBx5BSF1drwv829NqnyX2d_mHs8e-4i2cd4ifP4l8dCWvAF86ZYjSpYR_RiMLtf8SiR2Sl87YrVbBrM_CivbqE3QiBhB8cBwP_ivE68gmW5tO8S7rImDWggwx0Sott7ONhJQMEtEqWvGQdzpT6BPdNBpcn6OWrpDaNnVV7XqCSJonTOe5fzPYD9ZGFUWknywQEXs3CMI8B0Z31zdXbQwEotVg9GdC-SaBUiT3EkPPgEXfPYP0qqfetEO-wtbpda9rTurxLbkaZk1P_9WNCnM2l1ycwwTF5OUobFNYRP5MlVY92X-AkoStvgXwes8Aq9BPKAKoHHuIzcdNOTowLhitD1lru_6YfXCQu6iiBz5T__FcMcFvryb5o4JZgX__jkJmjndzEtL7lnOjttsxwMFM243EUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=j1rV6Bnho6Ao0ljNphzKZocA2j_wGj23VuAXdBTkJygRG59tl7mQhAKQJq1WjSpbkYO855NOTiOC-IWR_XKsxaAhUjAzm_ilnSot7OuMpmZr4Ujk6nN-XB0Uo8wWQh8c3WOcVswtfXI93I8Ie6hdQ5-of7fdhNw0VlEuDhyGbrGY-6sJe6MNZDILtc7WNN668Uz8YJFfVMFwT7qkRT2COO0LUEoprba1d7wl9O9L07ibBPhTST_0QvKLpN_3S3I0Epc-aGqPdjMtVo76Tz9fxW9WlYSI8oJ6WtT8Sy-oMVgSRqOhxWILHoYZQgXLsNFjOc9jOgCPxPNldUFhPNM1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=j1rV6Bnho6Ao0ljNphzKZocA2j_wGj23VuAXdBTkJygRG59tl7mQhAKQJq1WjSpbkYO855NOTiOC-IWR_XKsxaAhUjAzm_ilnSot7OuMpmZr4Ujk6nN-XB0Uo8wWQh8c3WOcVswtfXI93I8Ie6hdQ5-of7fdhNw0VlEuDhyGbrGY-6sJe6MNZDILtc7WNN668Uz8YJFfVMFwT7qkRT2COO0LUEoprba1d7wl9O9L07ibBPhTST_0QvKLpN_3S3I0Epc-aGqPdjMtVo76Tz9fxW9WlYSI8oJ6WtT8Sy-oMVgSRqOhxWILHoYZQgXLsNFjOc9jOgCPxPNldUFhPNM1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtcOaOUyuvFSuL2Bq856JSnJ5f94AV8I8T9T8q2PK5djkkK3kaHoJh3QQWOcrthoejuQgpfIVKzKKB0tg9d93FuJwgTZLCzFVznAkp-YwH8zwB2Ak9vlZzmIAqjNvvBBEqUkbRzyYRZSjdcIxzb0tu5Q5UN5oT80dDvmD8eilBhIvv-lBp7byFpftsBM4iHq9Ust7mGLLK_NJGDEfbvQgWh4BTSfoYoUiNMxaRpblmxHTksICjPWeRy14AEtQNGNbK3_y4R-f12xpxLffSMeqhSIeqTZRXNVYdB7M6ci5V0ij7lQc2lksAmfEfps-MLZPHYleL7wkkHFCrp0LP_Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=kPDAUuMErraBnlY7H8D3i5WHjAn4pAoS2nQDwrpYh5tshTTSzFOxLLUutLAU9NMJtHsovWN1SEfVJ7GxaNsZXQtg2Uf7Bkddg82JlVRplWhIwtdKQ57CQ0IUAQiVbNJ-R4cJKCgwr8b1y9cl-mJb98nPkHAsD93ZE0rhIxa-3-uxUb-pceOFdXM9a_6Z4YuW9mBIyvgjO-RhZYZS4iJ1t8ZRc2mw7J8QLWsbAfDCJeKsPQQWkWjmplbaxd_Y9KCv_-uOQwYiPf7-4-ukDYoRrVRDL9tXzHtE3Lrev2YLU-vsJt3NTfc04DW80qbRg19xwTIDI3lbYJiRt7o4fRi2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=kPDAUuMErraBnlY7H8D3i5WHjAn4pAoS2nQDwrpYh5tshTTSzFOxLLUutLAU9NMJtHsovWN1SEfVJ7GxaNsZXQtg2Uf7Bkddg82JlVRplWhIwtdKQ57CQ0IUAQiVbNJ-R4cJKCgwr8b1y9cl-mJb98nPkHAsD93ZE0rhIxa-3-uxUb-pceOFdXM9a_6Z4YuW9mBIyvgjO-RhZYZS4iJ1t8ZRc2mw7J8QLWsbAfDCJeKsPQQWkWjmplbaxd_Y9KCv_-uOQwYiPf7-4-ukDYoRrVRDL9tXzHtE3Lrev2YLU-vsJt3NTfc04DW80qbRg19xwTIDI3lbYJiRt7o4fRi2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kYi6cJPvJAgvE2Lz0nRdF6uE9DvmQ4AihdgskFrZFZYXBooEnu2RTINK4ajOomUh8va6sHXdhBe1wu16DpoKGFLoOEFqb8sITjK4Z2l3GlARj4wfr6hH9I1E_a1X4WJqPG2hpjWCGP4FLXWd4fpyG9jLWYNuNcGNAhGRvJF_ThhkBq_H4iMtwzvrfnIjmt-cu-Ybrj_kWn_mGblA24snf4XGkKPw9zCnY7TpmT-FMDor5vgXqRZiQSVrOEvie17vDfF9oxeH6zNg4Mdc9AhwlX1lrNy7_dSPchDLbxqQOdGRmZvfyAsbCPm1fIkNFBk_MJMUtNV72lqypWKPSob7ua_t4zvFeM71XS5XmRDRa9ZrS7h3sG3FnvClmIEKBP6gRJrk6Zh4fzSwBQqvLijh9XlJE8YbvivoqPGmcmHUreZPG7Apcoor7y16ZLgaemuZwxBfTCIok465td3oK9ab9a_tVIzOT0KsWqTv_8IIyYABYkmnJsSoTe1qyZ_AIXc18mw08TUNzVau1u5RuKstXvPQSVmTBB8rZZWBfO6txFouKoDN40ZVxJcBXZ38HsU-1w69QJjB_In2aP20BDIVfi2f6v2HIIolvox3e39pHqGhbSVToWfxan-MjrQ1pAglYfyUhgLZrGa5O_Lv6ORhwfgmJN-qUpa7hXwIDgIG5zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kYi6cJPvJAgvE2Lz0nRdF6uE9DvmQ4AihdgskFrZFZYXBooEnu2RTINK4ajOomUh8va6sHXdhBe1wu16DpoKGFLoOEFqb8sITjK4Z2l3GlARj4wfr6hH9I1E_a1X4WJqPG2hpjWCGP4FLXWd4fpyG9jLWYNuNcGNAhGRvJF_ThhkBq_H4iMtwzvrfnIjmt-cu-Ybrj_kWn_mGblA24snf4XGkKPw9zCnY7TpmT-FMDor5vgXqRZiQSVrOEvie17vDfF9oxeH6zNg4Mdc9AhwlX1lrNy7_dSPchDLbxqQOdGRmZvfyAsbCPm1fIkNFBk_MJMUtNV72lqypWKPSob7ua_t4zvFeM71XS5XmRDRa9ZrS7h3sG3FnvClmIEKBP6gRJrk6Zh4fzSwBQqvLijh9XlJE8YbvivoqPGmcmHUreZPG7Apcoor7y16ZLgaemuZwxBfTCIok465td3oK9ab9a_tVIzOT0KsWqTv_8IIyYABYkmnJsSoTe1qyZ_AIXc18mw08TUNzVau1u5RuKstXvPQSVmTBB8rZZWBfO6txFouKoDN40ZVxJcBXZ38HsU-1w69QJjB_In2aP20BDIVfi2f6v2HIIolvox3e39pHqGhbSVToWfxan-MjrQ1pAglYfyUhgLZrGa5O_Lv6ORhwfgmJN-qUpa7hXwIDgIG5zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjLlmlwQQACUrNq-d_9ALpvmmOtQFoXRhre9R-M0yeHXQtoh6x4GguEgXEM5gzPXYN4Doz4VsxaEjyvBUGSWynwypJlYmsLNN_eTQKzlj7R4HPswu06lGc_TLSdD0VKRbjmSrCyGfDF3E3znOrqF2RYoEn0GEyUvYTBQKZIQPmGOUfKwpEZ-698Yu7x5mbjrtXiAi8EDRRE-0ilwcaj1IVDTI0JQOWagjP3JGkthrpFfBvdrLpY0Wu3JR9VG37K0LYeNDet5ZdONV6Nija8qXLgrYY-ju3bZofk09Jphzu1zd5mh5CuGa0vQGg16-DAu4MwyJvrqMavYbSGhKeLzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NO3QBJ5wl7tsRGHw-S_xecGGxCaaKitWXpw_TvIjo7JZfG93QS1_OGc2FFT2Go_gcVDmf8IEVVF5Bl-V9FrWIi-YOhvTCN8ItTfAm1umVROoREhpNV18etQ6RjPncqRHKsttF6L8WuOXdKTvPNHu-PeLjz-5dhh1kq_7v2YfIvk18RLTLdnJt50tC6yWQR0uUjwqNkPRdjFyoZq_AySbu8Gafr5czFnj3tS8pa1XiEgoYRspSeQQJZk4BXi7JVadU8NyI6cCcfw3DIoZf5H5IXQJDL0_ioa3uaWVlqtyvg8zrBI9f0tHVxV06o-ECvvXm90CCXaxNYvolupmclr3Z5l5WWTZcGQ4pt-aK1kpeePApEgQWbUjFWkU2W4PSV54awJYhPRTTpOZU5Fh7ISjb0lUHsEu3byXL6h5bEN7l4dY5JFeuiXO5IX43mA_FWTYlKoL2P0fCzFA05Cya1bGvBKUwqJWrYXNNhw63eb0rhUei-PoHeR-kvjDTtZRheAcxxoVlfmDFYedcqFsCGrugmw4xRQDVGuOKLuRCBPwVpqhDUw-hS4sRfC5fnD4ZMNJU-DnNsuFWHrMYAXoo0L2spz8icoHGbNzzXzOf3AUVR0G4PRSuCvvqdu4fa38v9aS-zbcPJ_NGZV_xmC5MWbhn37p9llPT_YnY9lUo6vZqGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NO3QBJ5wl7tsRGHw-S_xecGGxCaaKitWXpw_TvIjo7JZfG93QS1_OGc2FFT2Go_gcVDmf8IEVVF5Bl-V9FrWIi-YOhvTCN8ItTfAm1umVROoREhpNV18etQ6RjPncqRHKsttF6L8WuOXdKTvPNHu-PeLjz-5dhh1kq_7v2YfIvk18RLTLdnJt50tC6yWQR0uUjwqNkPRdjFyoZq_AySbu8Gafr5czFnj3tS8pa1XiEgoYRspSeQQJZk4BXi7JVadU8NyI6cCcfw3DIoZf5H5IXQJDL0_ioa3uaWVlqtyvg8zrBI9f0tHVxV06o-ECvvXm90CCXaxNYvolupmclr3Z5l5WWTZcGQ4pt-aK1kpeePApEgQWbUjFWkU2W4PSV54awJYhPRTTpOZU5Fh7ISjb0lUHsEu3byXL6h5bEN7l4dY5JFeuiXO5IX43mA_FWTYlKoL2P0fCzFA05Cya1bGvBKUwqJWrYXNNhw63eb0rhUei-PoHeR-kvjDTtZRheAcxxoVlfmDFYedcqFsCGrugmw4xRQDVGuOKLuRCBPwVpqhDUw-hS4sRfC5fnD4ZMNJU-DnNsuFWHrMYAXoo0L2spz8icoHGbNzzXzOf3AUVR0G4PRSuCvvqdu4fa38v9aS-zbcPJ_NGZV_xmC5MWbhn37p9llPT_YnY9lUo6vZqGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=KZ41iDI_XE4qUlQTwOXqjIDXTP97811G-1MpJCCL8Ev0NJTY4PMK6qv3hsqnKMrRRVPoJNEvLmiND20UmN-Ncz8zu4OnQScdZzBemQcH-WzXUbcYWJfgTFajcV32s8b4hpa-79XrW8aK6bwSgv86MTY-iL7ugK0drqfmzFvupJ-qmagx4u4NBhzeGXS4odp3kYTTIfQsQ8wyu7dyjh_LJa5D5WwMFmaPmvf0wTBFsuoI8v66fykVU393w_duVQAdS6rT_O3oCQhAQudkV8XKRNBX5cdLOH-H7r3bVedm4UXV5iDp0_3l8aIBigDi1__qQARJFq6RsiTSekxBlIfaf1hq-Zz4jXQlkPZyxbIpEDNsIvPipVkC_L5RXHeGQg11skmblPjFKPGzo92r3WvV0KHXo9XcoT4Dp8zhG8Si3QgijZSOFKaDkbVUKZAL2YKH984qFWOUDX_oP4sL4hTBwwtTjZ1aeukj0ufzuF_hUmKpGC1B_PQGjyBLYICWHzXWG4lMdt0uCYW7ZwRt55W8rMH5zwM9IUuvEFZRZ9xp4nyQjyqCzEDX8Q9GXgaX-pI2wQWHZ4X2nT0WGqnJ-DOsnPzpZBqZYeqpx2LJcU358TwtB0nHCtwakMmOzZ-Xg0ACMZr82gKqPhOWXmLUxPrbLYu1yr97GV3vYzNtTodqnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=KZ41iDI_XE4qUlQTwOXqjIDXTP97811G-1MpJCCL8Ev0NJTY4PMK6qv3hsqnKMrRRVPoJNEvLmiND20UmN-Ncz8zu4OnQScdZzBemQcH-WzXUbcYWJfgTFajcV32s8b4hpa-79XrW8aK6bwSgv86MTY-iL7ugK0drqfmzFvupJ-qmagx4u4NBhzeGXS4odp3kYTTIfQsQ8wyu7dyjh_LJa5D5WwMFmaPmvf0wTBFsuoI8v66fykVU393w_duVQAdS6rT_O3oCQhAQudkV8XKRNBX5cdLOH-H7r3bVedm4UXV5iDp0_3l8aIBigDi1__qQARJFq6RsiTSekxBlIfaf1hq-Zz4jXQlkPZyxbIpEDNsIvPipVkC_L5RXHeGQg11skmblPjFKPGzo92r3WvV0KHXo9XcoT4Dp8zhG8Si3QgijZSOFKaDkbVUKZAL2YKH984qFWOUDX_oP4sL4hTBwwtTjZ1aeukj0ufzuF_hUmKpGC1B_PQGjyBLYICWHzXWG4lMdt0uCYW7ZwRt55W8rMH5zwM9IUuvEFZRZ9xp4nyQjyqCzEDX8Q9GXgaX-pI2wQWHZ4X2nT0WGqnJ-DOsnPzpZBqZYeqpx2LJcU358TwtB0nHCtwakMmOzZ-Xg0ACMZr82gKqPhOWXmLUxPrbLYu1yr97GV3vYzNtTodqnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=aRSRok5s6qiBs_mia2flFX43GxXU6oH0k-RzShfKNdd0OtSSSH_BnKTn37aNamkP16eXni6MJ76otv5PE3MeonuLnQeTNoPo75JZyzMoKr2rAdnfzMeY7GcJ84vcOEKThxckOI_kfeRCJnhmYOy2liF80ohMiZUZcY_ZBI4eNKVIkkwRUvTlVtmWcpByWFyrQDLfKRIQm27vKH8Iqn3kcG4POgHEXq8mUUWgr_i4cs9zjQD5et4A-faEntlyr4FzZmfuXeQ8kB9Z1iEBCmdlTOZC8BoKQaa4BzKaMufheN_7wLEyXRLZ8Z75hUuMY2EoXI_VeDB2acAoGnkfwCqtPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=aRSRok5s6qiBs_mia2flFX43GxXU6oH0k-RzShfKNdd0OtSSSH_BnKTn37aNamkP16eXni6MJ76otv5PE3MeonuLnQeTNoPo75JZyzMoKr2rAdnfzMeY7GcJ84vcOEKThxckOI_kfeRCJnhmYOy2liF80ohMiZUZcY_ZBI4eNKVIkkwRUvTlVtmWcpByWFyrQDLfKRIQm27vKH8Iqn3kcG4POgHEXq8mUUWgr_i4cs9zjQD5et4A-faEntlyr4FzZmfuXeQ8kB9Z1iEBCmdlTOZC8BoKQaa4BzKaMufheN_7wLEyXRLZ8Z75hUuMY2EoXI_VeDB2acAoGnkfwCqtPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=M7jRiHGho8szZwqQEdQ4fKLvgU-NmYh12UnmCLyP3H_FIscC-HW8XsPJ0CgHNv62tmpXPyYiqOER5_oSDw-DngSV0bg5paQ1IUpI_JZpXfwx-jaRMJSDNxTNDLAR9DBe4lPrkaUD7s2PzXvzfa_4HVhoRGprLda9XU98pYlmM8AMcDdgf-Sgg-YPhnqgX-ItCtGmFiCmQdHK9laHnwRl8u85XhT0Ea_tXFyfr7kTw7ChugSbgne_wOolTwpUt_PFCBw9dFbz0sjLCEMiyi74dqWILxLAvP_H46HR3k5RKHzb9N04IiHo41mAfAkWdIvBtWsZ_x6U3Ix4NHYPBbeu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=M7jRiHGho8szZwqQEdQ4fKLvgU-NmYh12UnmCLyP3H_FIscC-HW8XsPJ0CgHNv62tmpXPyYiqOER5_oSDw-DngSV0bg5paQ1IUpI_JZpXfwx-jaRMJSDNxTNDLAR9DBe4lPrkaUD7s2PzXvzfa_4HVhoRGprLda9XU98pYlmM8AMcDdgf-Sgg-YPhnqgX-ItCtGmFiCmQdHK9laHnwRl8u85XhT0Ea_tXFyfr7kTw7ChugSbgne_wOolTwpUt_PFCBw9dFbz0sjLCEMiyi74dqWILxLAvP_H46HR3k5RKHzb9N04IiHo41mAfAkWdIvBtWsZ_x6U3Ix4NHYPBbeu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=CTKZT2E2gRgJBU1JwpRk9zPA1UZMRy-N0JEahJkNnA8BcaEqiC0Erl0Q9AmHFLmQ2XZpe_QlJshlYMB5ZTB5Jy3tCA_ApzQE6MwVlRnBWrWDerp2tsZdQKAAkubBlw2yO9aXYx9ExKc1iqRS2iDQvG5sn5Q1UPuO1RCMno-UEgvI6ZHKJ4pF5wb9L6iUMW4kClGGnTblMfCflqtLJy_MZWMUZ9Bm6Sq-_muz3XEgfM6mXBObTKkIbApLEgxj7rw-sQS2l3SOcOe58MytaG8jZHuG27lvl-7ptgoAr2u0rUCu0ZXiBaIrN0HfKFkuZetiN3wlvuLrYmeN7CUrneAmMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=CTKZT2E2gRgJBU1JwpRk9zPA1UZMRy-N0JEahJkNnA8BcaEqiC0Erl0Q9AmHFLmQ2XZpe_QlJshlYMB5ZTB5Jy3tCA_ApzQE6MwVlRnBWrWDerp2tsZdQKAAkubBlw2yO9aXYx9ExKc1iqRS2iDQvG5sn5Q1UPuO1RCMno-UEgvI6ZHKJ4pF5wb9L6iUMW4kClGGnTblMfCflqtLJy_MZWMUZ9Bm6Sq-_muz3XEgfM6mXBObTKkIbApLEgxj7rw-sQS2l3SOcOe58MytaG8jZHuG27lvl-7ptgoAr2u0rUCu0ZXiBaIrN0HfKFkuZetiN3wlvuLrYmeN7CUrneAmMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7xkmNStBIx5aXFsc1-WCuGB36mEsjWRlp8mg4CqDBkuOjSYy_uQk86yvqfU3k-Kd8qN4FLE3BF9RbMTmqARwLKtb7MC7MoenW4X-egJGLZLWiv--xv7IxmU_desEsiSdMe2s8bP7l-S-noLj3ysBi6mg-csqu_kL8h8GfK1-7j7U9ejCb1dZFMHIWS3P9nHn_6gQTzaF_7qPUgmK93VfmjzENcuhxw-8jEzMo4fNCRiccXGFX7o8Y_IIR0fjzcvL8fdI57aZZuBbwalS-5bhspEGQQpNqGJXvxAD-svqodctr_TiJOWzG5K_GwnQYliFbJ6pLwIXl5VP9cTvCBG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7xkmNStBIx5aXFsc1-WCuGB36mEsjWRlp8mg4CqDBkuOjSYy_uQk86yvqfU3k-Kd8qN4FLE3BF9RbMTmqARwLKtb7MC7MoenW4X-egJGLZLWiv--xv7IxmU_desEsiSdMe2s8bP7l-S-noLj3ysBi6mg-csqu_kL8h8GfK1-7j7U9ejCb1dZFMHIWS3P9nHn_6gQTzaF_7qPUgmK93VfmjzENcuhxw-8jEzMo4fNCRiccXGFX7o8Y_IIR0fjzcvL8fdI57aZZuBbwalS-5bhspEGQQpNqGJXvxAD-svqodctr_TiJOWzG5K_GwnQYliFbJ6pLwIXl5VP9cTvCBG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=kw2JPo5hXeger2qDV0XOdDf3WpffCOTCnfhttErk88IV9F88oGTF1UWMvTkQYQ023Ys69egmTcANQKSJWrarok4OJTjC_mI-C7RnSKnARImeyt1HCwQkmeGZ9zgI6tFiahSTN7Na5aO4ZhZgRFqcDR-PPzgsoOQoLEBEIfzvgDEZ7qponkg5M85ewY4AKf4dR2ZZpmjDobV3EjGjo_lVmP4oOaPIaxDuc7eFO_7Nk2y7M_iz7LsImvxS5-GyaC1o9bitGYnoTVCI0AcSXmyQu-eSTfIKW5TC5A9_suS1odriMcmAuyKroujH6pIG3ePWYYezi_Nc0qaxKkbQ12TprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=kw2JPo5hXeger2qDV0XOdDf3WpffCOTCnfhttErk88IV9F88oGTF1UWMvTkQYQ023Ys69egmTcANQKSJWrarok4OJTjC_mI-C7RnSKnARImeyt1HCwQkmeGZ9zgI6tFiahSTN7Na5aO4ZhZgRFqcDR-PPzgsoOQoLEBEIfzvgDEZ7qponkg5M85ewY4AKf4dR2ZZpmjDobV3EjGjo_lVmP4oOaPIaxDuc7eFO_7Nk2y7M_iz7LsImvxS5-GyaC1o9bitGYnoTVCI0AcSXmyQu-eSTfIKW5TC5A9_suS1odriMcmAuyKroujH6pIG3ePWYYezi_Nc0qaxKkbQ12TprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=aJ__NYRq_I7uv7iEFuO6LSst0rFhsA5MlWL4XLyyZqekfnxFAIxRuYU624_2ksb3ist2hTFVMDv_gkCXBlQmNCDIxcVnZ5XZFLbZIzU8GZ9jCHpz-CiVMzciCUfeDTOlQHBzp14J9JQOHK13od-8c7anpOhKZ7bxDYRTFhZMCVR3B6zc9c21c1YlwezIIyFv5jCn-thFMSkzIKWGxfPOLuGBwqu4Kn-z6PsuY1988ya6bSiA9SjI9my8KAch_jl7fCbr0Q9LeZe-fZrvpDOv8VVpHVwgxBj-o4H4PhIX5HcK-vAKLqbbVnr0LukhfL3TYTxgo-Hz7XWaCokwr8ZF4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=aJ__NYRq_I7uv7iEFuO6LSst0rFhsA5MlWL4XLyyZqekfnxFAIxRuYU624_2ksb3ist2hTFVMDv_gkCXBlQmNCDIxcVnZ5XZFLbZIzU8GZ9jCHpz-CiVMzciCUfeDTOlQHBzp14J9JQOHK13od-8c7anpOhKZ7bxDYRTFhZMCVR3B6zc9c21c1YlwezIIyFv5jCn-thFMSkzIKWGxfPOLuGBwqu4Kn-z6PsuY1988ya6bSiA9SjI9my8KAch_jl7fCbr0Q9LeZe-fZrvpDOv8VVpHVwgxBj-o4H4PhIX5HcK-vAKLqbbVnr0LukhfL3TYTxgo-Hz7XWaCokwr8ZF4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IYaSF0K6_64B26KUOU4ZUASiblKoL7WBZD4hAblxnixn2TvX-MYRKCMXBnarSd4DN83tASc5s2POkDbkwXeQxoXf6locPughYV82Y982MK-vqUZZm969oOl0mOU6D958mINo0PK_2Wqcd47ZmocOz2bwa5TXD3wzeSrZ7Xv3ILvwaLTcciKYbvMXpYWvY4GrHlc4dE4UiDDW0oyPfdbZF5592Yxim8ret5yw-kd6ecwmjEMamzq43Zv3aiYH6NWaBN7SwTo0yfg1R5hRD1VXK-gyJ-4R8ahZKnztpeb19s0yJUBl_f-BhstoTg5EzzLN280Q11L_TqotxHBn0G49Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IYaSF0K6_64B26KUOU4ZUASiblKoL7WBZD4hAblxnixn2TvX-MYRKCMXBnarSd4DN83tASc5s2POkDbkwXeQxoXf6locPughYV82Y982MK-vqUZZm969oOl0mOU6D958mINo0PK_2Wqcd47ZmocOz2bwa5TXD3wzeSrZ7Xv3ILvwaLTcciKYbvMXpYWvY4GrHlc4dE4UiDDW0oyPfdbZF5592Yxim8ret5yw-kd6ecwmjEMamzq43Zv3aiYH6NWaBN7SwTo0yfg1R5hRD1VXK-gyJ-4R8ahZKnztpeb19s0yJUBl_f-BhstoTg5EzzLN280Q11L_TqotxHBn0G49Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5pEdmfdwdhNVXfvRGc89m9-8-FHEC6lyNwUPe4MfVrx6QG0I8EFSW4azSrrHQ8VwZDN1BBs5S0QU59N6veqQgBUhwZc-YEG3AYpsRsdQzVfaVHXcMubUBBitASHZIXbr9pAiVx39F_yAvywpicJjg3nE2aedsS0ID-K0FjTm3OhajsF0EI42G79YhhVE5hz8ln8hOQCS-ghoGu7DrkTmnQUV_li-trn_Bk2fB8pEEEVSy27e3ffqYWsZHwpLuvky8dzinwiLH4uJVe0k0rK08Svl3opjfbGrDkjxYL3lmaPKx7aiKRK__7pA7OA5N0Owyb25VJIIWLR2L0LYrH7g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RzgFPHEZvG8i1QrokkJXGGahh7q1nMzsY5QQkSu_VGKkYk0-ssSu8RvaYWrhdwBxRUtkF8kREZMUoz_37DOAQQt9AWLhJyrgmR0v5U94k9YaRqeNb-_R7Vu7VsSDgUvgZeMWW60o3m8GEKZzOEmCASVSqtZx_jyDSF7OfU3Mxs0NtO5vxOEHjNoXGruJfYlAMg_79N-dT7Z_VBBDJooewkusn0syCip8K6C2n_IJ38dEYBxS7_uaUdwtLNpoWTvn4hfZMuIE2mICbsmXz2m-fuPso4qMJVoSuET4na_WTHkAVq-mzHkFu1edpX_FNclbXNCKQO4pPRBmRmltUrjyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RzgFPHEZvG8i1QrokkJXGGahh7q1nMzsY5QQkSu_VGKkYk0-ssSu8RvaYWrhdwBxRUtkF8kREZMUoz_37DOAQQt9AWLhJyrgmR0v5U94k9YaRqeNb-_R7Vu7VsSDgUvgZeMWW60o3m8GEKZzOEmCASVSqtZx_jyDSF7OfU3Mxs0NtO5vxOEHjNoXGruJfYlAMg_79N-dT7Z_VBBDJooewkusn0syCip8K6C2n_IJ38dEYBxS7_uaUdwtLNpoWTvn4hfZMuIE2mICbsmXz2m-fuPso4qMJVoSuET4na_WTHkAVq-mzHkFu1edpX_FNclbXNCKQO4pPRBmRmltUrjyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=c5aloAYC58EddTN3_gA7f4sTZkcriN8qGziMDpqF76dJ6KRid5sf2bSh-px3iqAcs4jBOjKktykoY9VjGDrV2TETNcwnAbl3AoPHd6uPuKOvkjRQkb-Llzv1iCKw0msMvT3IlGsEuE_OMik7Pj5-6G_-neAluWdKReLKlXWd1JA27KKxe2LcSeTRyMTXOae0DofeOr4_VOndiqzqy5dWce05Us7_no9kD9qqmP6fBJHcudi35mouwK9eLbKz_txCce_ABLC_vnjlR1NtW5pc5eDZtL27HJV8MGbI9628JcK6Kdc9u_ft9v6-NJ1NWZaAz34Tr7pembBhVlOUOoA4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=c5aloAYC58EddTN3_gA7f4sTZkcriN8qGziMDpqF76dJ6KRid5sf2bSh-px3iqAcs4jBOjKktykoY9VjGDrV2TETNcwnAbl3AoPHd6uPuKOvkjRQkb-Llzv1iCKw0msMvT3IlGsEuE_OMik7Pj5-6G_-neAluWdKReLKlXWd1JA27KKxe2LcSeTRyMTXOae0DofeOr4_VOndiqzqy5dWce05Us7_no9kD9qqmP6fBJHcudi35mouwK9eLbKz_txCce_ABLC_vnjlR1NtW5pc5eDZtL27HJV8MGbI9628JcK6Kdc9u_ft9v6-NJ1NWZaAz34Tr7pembBhVlOUOoA4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nGKoj-p7ZP2s67kN6NeE9pDrC51G1JG18uZhSTAuWJBi785SDFj0-g47BJOxnvO8JFpP1Q0iinjvcfZDU2lvJE-ZUrQkUfRw-yK_uPRcJ3qG6DqeWpeRVFgJMlzAnVyMcAS7IxUYYEcpewMlNPIRB1YUJW4RTI_YbRj_LFB1da6tjui9V34LIT0hYAobZtTsfMknLVvrLF8lT7aZ-Ar9LrJXh0GHnwFg3ZxqQmWG2zvJjEOsHpWHQzPWnOOG_RDiLylliQwj5-mW4yVONd0fmUhJoybh-LXmX-b-HDn7LkqD9gYSOSE9FD6mUNZwYoC_OzY3Wuyk73Cqc3fw_j9QeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nGKoj-p7ZP2s67kN6NeE9pDrC51G1JG18uZhSTAuWJBi785SDFj0-g47BJOxnvO8JFpP1Q0iinjvcfZDU2lvJE-ZUrQkUfRw-yK_uPRcJ3qG6DqeWpeRVFgJMlzAnVyMcAS7IxUYYEcpewMlNPIRB1YUJW4RTI_YbRj_LFB1da6tjui9V34LIT0hYAobZtTsfMknLVvrLF8lT7aZ-Ar9LrJXh0GHnwFg3ZxqQmWG2zvJjEOsHpWHQzPWnOOG_RDiLylliQwj5-mW4yVONd0fmUhJoybh-LXmX-b-HDn7LkqD9gYSOSE9FD6mUNZwYoC_OzY3Wuyk73Cqc3fw_j9QeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=awHxCHnBayQkE4f1p42gkq5X3Vh30e4fRhcTLMmeoC6nuHrsG2hZ_NA1T9Y9nFx7s1DkEXfjc5Bnm-2hol34zOWE4Oj5xv5MDCthkO7f77ylotOz18w6naS1VnLjcEuEqPX6lllNGJWvkYDsgE31YGESiRhU0MiWXXUph0pYkAz4TI3EMWavf2dKLyrzGFZOU0yWPjerPaX_NsyNktB-7OdMM7B3oQYnynYebpRguGIKcDVITDxC70LKRg6x8oBVHWpjQrroPn6UV55hpAJ89tOPlbYUZl3iWu3T3fPyT5lACg4yPmvSYG_DLFbIF6Zc-RYgCMVQ_XqHYkVU2PMomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=awHxCHnBayQkE4f1p42gkq5X3Vh30e4fRhcTLMmeoC6nuHrsG2hZ_NA1T9Y9nFx7s1DkEXfjc5Bnm-2hol34zOWE4Oj5xv5MDCthkO7f77ylotOz18w6naS1VnLjcEuEqPX6lllNGJWvkYDsgE31YGESiRhU0MiWXXUph0pYkAz4TI3EMWavf2dKLyrzGFZOU0yWPjerPaX_NsyNktB-7OdMM7B3oQYnynYebpRguGIKcDVITDxC70LKRg6x8oBVHWpjQrroPn6UV55hpAJ89tOPlbYUZl3iWu3T3fPyT5lACg4yPmvSYG_DLFbIF6Zc-RYgCMVQ_XqHYkVU2PMomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_E2M5xtasEQ7-o9p1wxxJ-2Uq73P4qz4kf7V-D0MURNM5uxAV1DcqjW1t4ra6w3LddM9dGJ5qQm0SkJxPusisjstXL7xCiCCY7dM9B3VJg4YMQI5eitw2mrPuBTHq9TcUKS2ATODnvDAI-nd73r--XcTeeZaHCEf6IOuDRTgr7GIFIy1vS4ugC58KHa0O6eVHGY9sl-2QYWFLtsteu3Mj_8SVt2unE19W8SYtsK_WTMD1tWMgkpXZIOeRMOrhbg24KxYWPYDY7z1TMyjVG-DuweCvFVAxHEtRuL25nPIA5V30f6bsCTYXDJ-2tRJUSBYUe3T5seeod93tEo71KbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mBkU0EaHzAk4YH9VKPyKlrQQMQzb-hcVL8BKVcKPCCzfubsZacqU9Y8AB6ux0SceIk_DxceTygQntBhSjgCaBWY9kLxjOfSLOtbsvAQL5_QctqDKUFyfFvaGhcT7Pp9MldZYUUPLB7R-dUJ-e2B98xiK9NT8S7VzZUo2-PiEHS7uSIWvGeFfE00P71E5rGoKau7FQB7qnbaUaKO6uyn8OIV1rugfd2dKs7ajE5OEPKCDJpGVbVSvTbXtDeTCG9EGu6a4d-zmjkHZZIFTv8omuPjF48L_LP9FyeIh3fjAAnJsxzfxLgQKSl7ZtoA2Erkddf9oSlLDkEf2-m26E0sWUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mBkU0EaHzAk4YH9VKPyKlrQQMQzb-hcVL8BKVcKPCCzfubsZacqU9Y8AB6ux0SceIk_DxceTygQntBhSjgCaBWY9kLxjOfSLOtbsvAQL5_QctqDKUFyfFvaGhcT7Pp9MldZYUUPLB7R-dUJ-e2B98xiK9NT8S7VzZUo2-PiEHS7uSIWvGeFfE00P71E5rGoKau7FQB7qnbaUaKO6uyn8OIV1rugfd2dKs7ajE5OEPKCDJpGVbVSvTbXtDeTCG9EGu6a4d-zmjkHZZIFTv8omuPjF48L_LP9FyeIh3fjAAnJsxzfxLgQKSl7ZtoA2Erkddf9oSlLDkEf2-m26E0sWUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Ne9sY8F0AdGo0a50bBcxyP5OwNQHalIqeOckdqPKh0elra4iS1-T4NUOaRcT9XoySjbwLpmTo6hi56WQBrmnxJr8J174s0O_6SLyFp0UuZPGDmnoVAKqXh3X0L8LsXcUzZyikt7RAjn-2p0ZZiUrEwcTygQqGUAO-YtD2myuniji2kBSkhHlAWNgGKeQanN25z0MNrMaNdQQw22DixR51Zmq_PXhmBufUUXyiRJ8Cb-mjahwGTWwbpXxDHYyaY_JxJVkIYoJNBbrfxCzwocHTGFsBfyPPFRkWbqmFTtEyZFmmhjulgGwCVYZ8YKC7Z9_MbDdHJBki8RAja8yOaxSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Ne9sY8F0AdGo0a50bBcxyP5OwNQHalIqeOckdqPKh0elra4iS1-T4NUOaRcT9XoySjbwLpmTo6hi56WQBrmnxJr8J174s0O_6SLyFp0UuZPGDmnoVAKqXh3X0L8LsXcUzZyikt7RAjn-2p0ZZiUrEwcTygQqGUAO-YtD2myuniji2kBSkhHlAWNgGKeQanN25z0MNrMaNdQQw22DixR51Zmq_PXhmBufUUXyiRJ8Cb-mjahwGTWwbpXxDHYyaY_JxJVkIYoJNBbrfxCzwocHTGFsBfyPPFRkWbqmFTtEyZFmmhjulgGwCVYZ8YKC7Z9_MbDdHJBki8RAja8yOaxSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egSD71QKEwfijXFT3YKNsglSXaxIlasTkf8mHo6_U-5Qj0uBEhp3uL_qTap19JaHv8xgxyKcaV12bWYBbnkRYA2ZwOYtPdQLfuq5R72DpRnL8dbFrWrWutmjz9Oq2v9egtWnOw6xzHkuZqqev-X7Wpw2yPvr3MbAs1tEQROlsdVL19I1Fq_lhE1NJVreGg3PPNaGmzdPT85G_BuKTHd8DBmy8GwO98lDftxBrc1pI_jPyrHuc8-NvTs9J_L6q4qTVIXIcDdSve2gaEVqAo27gZ_mmbi0KDnX4-vGJqC_es7b9VBpG2vMGnIYMlEwLKPCGtr8EaVvJi3ue-Zetp1wiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6pPBJhjxaaaV-1SUFsa7Tsa8fq3NCPQT6GOujOcuKmMYnjtIXH4z3O8rVqHuJMJectvIeI-yumwcd14KlPUjjTmqLTViipauxKXQMznQdv-x7mL4JLUKufIVOUF1VR-IrAgAedrat3KWaNueDIs0f3dh8wDrmEpLQBDPlH5rD_59Cn-H2CssJdHLrbm3LpgHyaoZpVqUCh1mFaidprWaU4PiEZTXo7BwA8hjFAZ7dmjXiM-RMNfpQqgGqNPutpzZ-_qZDpemf8Pvcdd0zri1lcupCU90wmvZnx-phQgyTsdl6QXi-vuTkxYUJtwctMp1rywf-Z3fudP88HQjhzuag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pA4ECq0oy5u7rd062snh41I8Q2T1MqLiLSuORqPd2PxE5EGKWK4JdZsS4FTh8RI1T3eR8P4QA6BobW3cQtFffaJavtYxkqUwLaIJ08tzw98D-S0rO_KnnkOirW7U7j6hajTMJ5rpz-_OzivLTZ6Q5Oyet7o5_eOiBh6u0QnQgMvSR8Bk136BW7RW_SxvCf1bJwnChOC-H-qKWHQm5syHn49UxSiaZumER89NkVUcFYsR6rvBBmJVfuMpCtEgaL-eFBNFRCXhB8GFm9DwxO1svrZ7ub8v6tz5hOlKZrFjwLSJdDg8BHkbsc-Uw65B71yHTsgfN6P5j2coG_qjg7futg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pA4ECq0oy5u7rd062snh41I8Q2T1MqLiLSuORqPd2PxE5EGKWK4JdZsS4FTh8RI1T3eR8P4QA6BobW3cQtFffaJavtYxkqUwLaIJ08tzw98D-S0rO_KnnkOirW7U7j6hajTMJ5rpz-_OzivLTZ6Q5Oyet7o5_eOiBh6u0QnQgMvSR8Bk136BW7RW_SxvCf1bJwnChOC-H-qKWHQm5syHn49UxSiaZumER89NkVUcFYsR6rvBBmJVfuMpCtEgaL-eFBNFRCXhB8GFm9DwxO1svrZ7ub8v6tz5hOlKZrFjwLSJdDg8BHkbsc-Uw65B71yHTsgfN6P5j2coG_qjg7futg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3QHxSMH6PwRyCKB1BSMui-jhmAylTTIX2FmuCdUx952DV0JoEYh-Ry8UEibP_vW49hu-Beow9Fhb6fgFoVTMbgp58fEjFb7JC5_ZfEj-WpZhsPdxl_Zc1U6EO6Xp3OX7ENbvg7gFMOHJRLF9nOOOGgHRmND-vqvFc21-xXbABZDyDewpNvmXvpy9wWVauij4Wle4CWVF16EDrqm_a1D0aeh0iYgeMqMwkwCim-5MIIFL1lLkhFXLUf098hjngBogWM7SDF96uh624B5c-V2Ckuz4eEvtOPUGWW5dJ6xcZ3FozlkEpJFmZW0GcrYebH0Lx8wX1jJU4faAHKPRnHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMj-qHnCkfpOp3UBk0nKhX0wVoyKzBlBQQWZZeQvu2hKSN99L9SaQ44LgKfQ4gXEyB2ZaFWuCfKm8Mz8LPjN9Yt8VlnXlK2dCFN2QIwG8nsIHoHn8drp8Tqbp_oQq_e1y89MGuV6kOWONyCbMxbOTIglgOlD7cvRe3L0KHU3qFpqkpUR0o3CQ5tdM81blmNqFnSZbG_dO0PRyCF5aYUwT-UE8_Ja_p7jRDitYc0-OBLiQ-mLYvfIkHhBW-OPcNNy7SWlccXQWKqQGRSTzIylPDYysKc9rWMtIh20ST7-z54CJRgyPM-DdgJG4isyFwoDDRulnWPXJEqo4e0q9MUmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byFC_xJbYKAXHCzeZ2tlELGjh-d1_6qNaEN2tkB1q1dwAoEkH_-zxpdiSbWTiO5pZUitj4nYJty9iS8ROl78epKJDiQ414RtUUGEGLDeWzjS401Za29_2l1ERw0kTfcvYwT43Zr27Ny1NLBPAZY_jbgn4tISO299qrivJnOd8E6HnLOI3R8kPfhVM3MfgofIyjclas0Y1UKvOhLVPfIY_ICwAdf_eXnzZinEhUHnIRBjr49hPy1oC37rMFq-GokO6Xeh51Eym0acTEfPf_qcsqDy4Yin7jJDuyV0WUpX8TbsdCzJmR0m6cFVj3WGb-2umGOnkoDzTWTNxdpM4Kji-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=nd8598qqQl7pnDbJx0ZdTUSuXuRN9P7ZEoqoBOezPZNnLkjJqDqoa9zKNi4tqNk9W3Ru7WvrDrRjLfc5kivKbQi1qzM-UYdHNdNYUiTERyopVxKBYDLFA2yQpT899M9vMmI8g2i3kb-l533PJUTzVo3nwdGL5ee7KetR5tSi2YMjl1ATYqEcD_g8hOsX3BTTpVBVI4gXZJ6GuU8PHwKzGPEYt33GD4g3rN2HxeUPSX4NTjUr9k2drnWYzt0RVsjIHtYxokAgBT8GOhVJAP3K2ECmTthZBxvXQmKGF-41l3L7HBXIItUvLn57-05Mw45rP-juTICfmxn9IeMcNw92Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=nd8598qqQl7pnDbJx0ZdTUSuXuRN9P7ZEoqoBOezPZNnLkjJqDqoa9zKNi4tqNk9W3Ru7WvrDrRjLfc5kivKbQi1qzM-UYdHNdNYUiTERyopVxKBYDLFA2yQpT899M9vMmI8g2i3kb-l533PJUTzVo3nwdGL5ee7KetR5tSi2YMjl1ATYqEcD_g8hOsX3BTTpVBVI4gXZJ6GuU8PHwKzGPEYt33GD4g3rN2HxeUPSX4NTjUr9k2drnWYzt0RVsjIHtYxokAgBT8GOhVJAP3K2ECmTthZBxvXQmKGF-41l3L7HBXIItUvLn57-05Mw45rP-juTICfmxn9IeMcNw92Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lVFmbKd6d5qLnJRJIblE2SulenMzx8PMH7GEW7SwnopSi4AG4xtL4rbkBj9ZOY3lkHecm1iqnLq1MB9Ogx1wP5KuYy4WIhYUWoxGpO9BIjnjoBVzFBbeGiLMoDPSJzTIPLoJGECUcPWU6RuI_I3EUEozTmyIOlZKoSHywFcJnC91CVTh6ulo5wUTFAihmnQ-GmtaGn15LvRhYSHvzPlXNKZP3vVeyUKwcdlY4PkZUznwtPuZwkF_mqMEwtIZAIwqGWr1_kuEbnzd9naMNxZlLNfjUguxIoOhcdz9dk54XSlhaZr-C0cNT5zO9xsxJ_KRrS3Gjg8YQAgMF3c6Q5K5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lVFmbKd6d5qLnJRJIblE2SulenMzx8PMH7GEW7SwnopSi4AG4xtL4rbkBj9ZOY3lkHecm1iqnLq1MB9Ogx1wP5KuYy4WIhYUWoxGpO9BIjnjoBVzFBbeGiLMoDPSJzTIPLoJGECUcPWU6RuI_I3EUEozTmyIOlZKoSHywFcJnC91CVTh6ulo5wUTFAihmnQ-GmtaGn15LvRhYSHvzPlXNKZP3vVeyUKwcdlY4PkZUznwtPuZwkF_mqMEwtIZAIwqGWr1_kuEbnzd9naMNxZlLNfjUguxIoOhcdz9dk54XSlhaZr-C0cNT5zO9xsxJ_KRrS3Gjg8YQAgMF3c6Q5K5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GPAWSlsgyDRmkpqrqy8ac5dVL055qRTF-Q9HHDMO3P-9AsVMxAMaRUxQVTmYml3oW3FfayCyJNERfCogBEFYvxU7TiCrPvoRCKB-VfreGCOmq3aUt3CH1YOUzXT3dZFp8DvbIQDi-NAAz1_eOPPA7ZzJhxUBT0yX__SzHQaWc1Od3KMWyXky5SUe_70fep5e1IfY_Wv3fvRpwxlk3kHuUEtty22vIVo53P5vl-Gia0Jw9PPF8AHv_h11fx5e-nuhYC-y3VxAgpc_nOO5T9sWxHpho18enA-RjwXCUY9fDDt40edkxihjjBRMcQj_jzYelULOZseP-S1h6w-WftthslDJ10DBMmg0JUcGvgf--I32fh0-ZAOnIghk4WaHIyN257ykdMkmGWLZHsWLtuCyJyvQjHRZibgCHt6xMxFd7psVx7dnakZeUNd4GnAJkZ6jg3XCy4KK5a2ks6bUKgTanmxS-a3NMGOU-DCdAxvZ4NWJpdpDtp8HqUTZAJ17_INpbVBJVJ2EnArgzkKMPggKSeRCn7z5PJ2kw_sxQfWDAbbRF674HuZKXAs2psKgWo076-IBgi-Uxot9LAsBjlXhsIuGoNva7Den6Ae9mYsFaIxNOO7E9cYzgqDX11tgItdRoqjwlQC269TE_edG9ewMojwASDO7xfFDCJPFouYB3k8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GPAWSlsgyDRmkpqrqy8ac5dVL055qRTF-Q9HHDMO3P-9AsVMxAMaRUxQVTmYml3oW3FfayCyJNERfCogBEFYvxU7TiCrPvoRCKB-VfreGCOmq3aUt3CH1YOUzXT3dZFp8DvbIQDi-NAAz1_eOPPA7ZzJhxUBT0yX__SzHQaWc1Od3KMWyXky5SUe_70fep5e1IfY_Wv3fvRpwxlk3kHuUEtty22vIVo53P5vl-Gia0Jw9PPF8AHv_h11fx5e-nuhYC-y3VxAgpc_nOO5T9sWxHpho18enA-RjwXCUY9fDDt40edkxihjjBRMcQj_jzYelULOZseP-S1h6w-WftthslDJ10DBMmg0JUcGvgf--I32fh0-ZAOnIghk4WaHIyN257ykdMkmGWLZHsWLtuCyJyvQjHRZibgCHt6xMxFd7psVx7dnakZeUNd4GnAJkZ6jg3XCy4KK5a2ks6bUKgTanmxS-a3NMGOU-DCdAxvZ4NWJpdpDtp8HqUTZAJ17_INpbVBJVJ2EnArgzkKMPggKSeRCn7z5PJ2kw_sxQfWDAbbRF674HuZKXAs2psKgWo076-IBgi-Uxot9LAsBjlXhsIuGoNva7Den6Ae9mYsFaIxNOO7E9cYzgqDX11tgItdRoqjwlQC269TE_edG9ewMojwASDO7xfFDCJPFouYB3k8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q9g-Du4GXT5LbXsjAolpgAlSMbg_ZPu0G719bFx1Yj9J-cqxQZio5kwcyn1uRWQw1MbC8Bn1c2Fhpq4q0ZfHl4u0BhhatNMNt6KID6pSkT0nuattgmoY245_STBRyj_D3nMLP2CaXgm7e0OK6wYZivZ4rv23HVHlRWYT0m_eiSzOKlcNLZwDY-9pw8CnKwjyZq7cSB7SC4gCYoU_aTH_V-91qZyVAFJZ-3fHJvUHrkggyr8YKXQYcamil5SLjuP4eQW-n8ts8ElU4QqKPGM5wwljSsVJZLrubF6kGwMdf2Z452VpyeTH_zwXcxhwTRJJD5PPYZHtZmAAYaT0hxvUq2Xhqr8ye0e7LZ3EVGlYfr5hxA_4oa4UwfGOApuzleeZV22fxJBLhhJf7GiEvytvl5YNZEbdcHlesrB7LWr11JIU7Fnuw_4WkGJqZzld4yi606a2tbC9hEGK23IlI04scHLlu3vc9thd8Rry-fcFqaXX5aBzZyBTN-czQtzYEwCzVtoU6-2yTsQbCys9efEf3DG-5WCiv7X4Biw8zi0CE2Ihh-pGIa6fN8Pfelk8hUAyvxplNBT6Ma96Vtr0UTj7wDvpgHkPmjm-QUYS4O182IMIfyb7QbpQSVEp9aK1351j1IO_UY2W5LqEK20jyARZGGLTIsBvt4_QgrAxpkI7bsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q9g-Du4GXT5LbXsjAolpgAlSMbg_ZPu0G719bFx1Yj9J-cqxQZio5kwcyn1uRWQw1MbC8Bn1c2Fhpq4q0ZfHl4u0BhhatNMNt6KID6pSkT0nuattgmoY245_STBRyj_D3nMLP2CaXgm7e0OK6wYZivZ4rv23HVHlRWYT0m_eiSzOKlcNLZwDY-9pw8CnKwjyZq7cSB7SC4gCYoU_aTH_V-91qZyVAFJZ-3fHJvUHrkggyr8YKXQYcamil5SLjuP4eQW-n8ts8ElU4QqKPGM5wwljSsVJZLrubF6kGwMdf2Z452VpyeTH_zwXcxhwTRJJD5PPYZHtZmAAYaT0hxvUq2Xhqr8ye0e7LZ3EVGlYfr5hxA_4oa4UwfGOApuzleeZV22fxJBLhhJf7GiEvytvl5YNZEbdcHlesrB7LWr11JIU7Fnuw_4WkGJqZzld4yi606a2tbC9hEGK23IlI04scHLlu3vc9thd8Rry-fcFqaXX5aBzZyBTN-czQtzYEwCzVtoU6-2yTsQbCys9efEf3DG-5WCiv7X4Biw8zi0CE2Ihh-pGIa6fN8Pfelk8hUAyvxplNBT6Ma96Vtr0UTj7wDvpgHkPmjm-QUYS4O182IMIfyb7QbpQSVEp9aK1351j1IO_UY2W5LqEK20jyARZGGLTIsBvt4_QgrAxpkI7bsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=GjrqiiwfXjs5u0RCi4Oiq6I51KwfdeVRU0iZvc3-TjWmHA85HJYS5_vSa75SMEhd1gPKvnhI1SAh2WwL8Y-AbvPu0F0V2MXe4qWAY8i7SOgSt7aWx9OiuEneTyxSwR1Y-Tzn6SB-oKWZs4mcddx4Spz7jOJvBbRxUyFIoY2X_F-Et5foG_y-3KiHGatHkHUdS9P9mQ6EQ1lHpC0Yht8OislohWt04MNk86odF5Z8vKiPOHKY_8bWoaioR5XJLPWfIwTXhBJ7V0n54A2f9ag57-YyyWKS7Xd5xl7eIdmDIUFNF5svfmJGxlT4kg4sKsLSNIuQLyvKm5lVek6vmdGQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=GjrqiiwfXjs5u0RCi4Oiq6I51KwfdeVRU0iZvc3-TjWmHA85HJYS5_vSa75SMEhd1gPKvnhI1SAh2WwL8Y-AbvPu0F0V2MXe4qWAY8i7SOgSt7aWx9OiuEneTyxSwR1Y-Tzn6SB-oKWZs4mcddx4Spz7jOJvBbRxUyFIoY2X_F-Et5foG_y-3KiHGatHkHUdS9P9mQ6EQ1lHpC0Yht8OislohWt04MNk86odF5Z8vKiPOHKY_8bWoaioR5XJLPWfIwTXhBJ7V0n54A2f9ag57-YyyWKS7Xd5xl7eIdmDIUFNF5svfmJGxlT4kg4sKsLSNIuQLyvKm5lVek6vmdGQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLGAjLEJMoObayKlVFS7Kxw3K5yI_Lu8r0ArzxTbmzOr_WVD8BpRKgOuZDX4ErxhCZ9waEI12jXoE5iz9FPtMa4VOPggTGPnHlR_PEp-9AS6BkzmQaSrhCBIBXFVnhCi_IKKB7ofMdw4-SMnXwzukfwF9FM5JjiBnubK1g_WTtfM35nuGUqlMVkdA6koSL-F4cn1DXtSgJv6ryIq43kPJkzn7HazOJh6tSFN1oGwjlrkEZGzZY6xdpJBK4tVQKs1VJJ2A2PIRx1g6m61uPcSYZoqey2PT3354MfpFGoAMhhDlTPyVHJRyZheFcOYVPINCS0RZHuBUS4fUv9HZt1AeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lDntnIk824TethV1FxH-Nvw01RIrn-xVEWa8AAF8cavfnXeEXFWSMhgM5IhVSgORwr7ntmmU82Rdx3dfQE2vL3Trqjz_kizYdJr_pQ_tBHwyCXQ_RCBdDphdwqXwR9YVyOzhqk258t0foNp_m6jMUzHaWcZAaAtsm6gnzg_o96KuKvR0PX3UiccelTYjaoovQBl5vnG-jnYSTEGXhJCGilYceNAdDOWqB07q9mzhxFz7ZsyQmLUossCxlsyRemXWDJOnVN7A86Az3shZd9YYyMg5LJQplbOqOzYbi8tPnT71VdlpjlnS0Ra4HTOq0aXZBbFwVwe5GgvHk6XmLN7ngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lDntnIk824TethV1FxH-Nvw01RIrn-xVEWa8AAF8cavfnXeEXFWSMhgM5IhVSgORwr7ntmmU82Rdx3dfQE2vL3Trqjz_kizYdJr_pQ_tBHwyCXQ_RCBdDphdwqXwR9YVyOzhqk258t0foNp_m6jMUzHaWcZAaAtsm6gnzg_o96KuKvR0PX3UiccelTYjaoovQBl5vnG-jnYSTEGXhJCGilYceNAdDOWqB07q9mzhxFz7ZsyQmLUossCxlsyRemXWDJOnVN7A86Az3shZd9YYyMg5LJQplbOqOzYbi8tPnT71VdlpjlnS0Ra4HTOq0aXZBbFwVwe5GgvHk6XmLN7ngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oGbc5LNjUDKxkBu-YquVSV1qvjpbRCZpWVNe5sz8jQxjEOMJ2Z1RIjVUbiOwHzacb9tuHUorMB-zdkwam-2RHc1QHLryVmLfeDiBBVa7SJM3PG7_SPgDgqXBYleRWv2HPXg0Tvf8Ds9Fb98sOT4B5LnwijuK3CwgX8LHEs2ENAD7rGe27zF_Gi-ATYRY2X00hDoYIcSkhlfD0NKbVLUu24bCyGkzvKuv-liBzR3kgAq7NjGWYfl_vnYSvYoqBHZgDp3dXV8trF4k7Wijko0fIdtqPNp1zMibqtCHrvQdZAzDOSkKk_WgN2-9j619QEyGHQxjlmNJ_L08BOZOt0IMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oGbc5LNjUDKxkBu-YquVSV1qvjpbRCZpWVNe5sz8jQxjEOMJ2Z1RIjVUbiOwHzacb9tuHUorMB-zdkwam-2RHc1QHLryVmLfeDiBBVa7SJM3PG7_SPgDgqXBYleRWv2HPXg0Tvf8Ds9Fb98sOT4B5LnwijuK3CwgX8LHEs2ENAD7rGe27zF_Gi-ATYRY2X00hDoYIcSkhlfD0NKbVLUu24bCyGkzvKuv-liBzR3kgAq7NjGWYfl_vnYSvYoqBHZgDp3dXV8trF4k7Wijko0fIdtqPNp1zMibqtCHrvQdZAzDOSkKk_WgN2-9j619QEyGHQxjlmNJ_L08BOZOt0IMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSrdwLyPhp1yHt6yGvYO9Py8QmwRLMheKBcBQPFzpJulzKJu0aIhreunSgmkou9ikajG6nhTSpP4ak0Nl5LDuoJrc-3a6f3L9TIUt7wK9pb028sLJfSe-9ndSSfILcMgDBdq7vE-oEFRSWPJ5hVs-C67doTUtBBsikZQ3mUegeeWfILEUKQIrYAkVkk2hKcmoLTSiKJnQBRf_x8BK171YVnf7jrFi1yZ1qgdqbowURRsTTqvAzPMx_cye93NTAcMk13EN00YqwRdD117jD10KKIFAwH5ybnkhWpvsJYfE4fBBX8ALDIl3Ailp6cn71UoheWPZCFpsuoB7hciNXQ8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No4MePtAXpJWlxG3BRmO32BNoc9Jd83N0MrYRAE7TTmhO6qUet7MHjxUeREt_-Rin4IvAFvqPgjID0Kjo6dRaTWTjEx1FFMTb9eMrRp4PZH6wig4PpEENcAyRzZNAiNdtTL8ZhzB1kxBAiDYFlU3piiDj3dfjOJukZi6b2Ugkexjh_MBIEi07H8O4ms4vOKLtuevCEDzqhNBWDzUZKeoM-w-Km6Is1ifbmpiooISbDrsl0nXk3OHerGDw3-n_s3o9a-tlWOVujV3Fy-p5-J35n72dJC_4t8NBvcOqbb0uyJaX1h3nKE61uyp73yp13O9i2OeCAOfwg_xCnJE_A_9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czTLPCr-01uuPmAw2I1EQ4OQmenOAACjcrbEeh3Lu4XRf6vul_mvqQmWzuD5olgBNjRt8SV0KNDbIAk-K-LqZeHgy3-aWNgK1awLq4N7hJICxTISSBu8sr2D_HBNWTJMkCZnYa3WFa0095KyFdfLFNLhdZo0LcFSlMZ_SpbSgDvGX7tfiukA16Bd6s13dcIZE5zCh6mvzidraQAA5fAf0VY7w_PEVfaRQtVIPfemzeTPpwSIv0syWhTsWxTQnLDTNUj2HvXKX4DNWpgKthtrw1THTk9ZoQq8ECLyitHK_57ASSYCGKQzSIYnR8wROfOnRHnVCK7z2bG3nBOO3sIY-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdfdYPa1wl8MVYFcW9Q5MVt_uQT_lcdokeVbR0dp0lPEswf8ugomNFVtm86mGXOuw22DPdNtVcDxrceUcbNxaR02YmPhGPkTIfg8uBNC99295eiEiloMHWbT9ZEUAAvavB3-ysV5wxroOfDvGCHhbIdNr6XYBypkWR6aAnrOtnAgn8t8RW9uICemNwq6KSzW5e5KRFd_LmM8cd9_5Q1YCVEZXYanYVHbO8kgKIu2dSg2mmVCwQMIgolZkka1-pUM1ipJ5XzfMJ1VFQyfr_gVgNxiT9Y-a53LI3yNRI_5ElTLRT2U_5Jy9ngXnQ3ZiEV2z4ruAQvl5NmQr-MdWI0dLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfKiTQAUliz7QIIg-49wcMqyl9_aAByOFUA75DwwpwAwWtjIuDR7OY2O1h0_-cvYKMjDzW_jDzYFK8QYEXFjKzS2egLPIzV2HtFHFfCl5JuRCFKx-I3lnCzrkystTqf6_nyHAw8xD0EMfZepZexGZMQf3UrjMwJ7zFqdxqMe_pFWcI9eiH54C9PnczpcldUerVwgUSV6-0HMHAmWez2__YoxqgtgjCZ_xOxZ6KFKJgVe0QHZMhwGR7BsBI0h71jT2IWCugR31VwE4gIcPc-4aKPEIW1nNWj8TxJ4l_genhQX_NJVSNh11fC0xqdAWBq92NpY_m4OsOBx3Z-ipoQdjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUkyxrjuNaDu1wYpw6ImcOKso9lwOQ1TmmQmMDvrf5rIGl3zreuvMsr3XSfP4HZF36qcMvy-JUPzDSIMeN84ztt5v45o_IH0dtUS3ofdUFxQefpqa4NGiEEwD9MeT6CV-ub5w3CliQBKqWPYg0XJUAE1CoSTud6lwbOgDfN4fn4P9povGdJvWAqGOfqRBN7849dN28OatabXM07XN2l6Kr5Jbzbv_ZiL2wHp3eihnWwAMNLdfnfMvN2tkO6GWeGtGxXQuSy_OpqLEpGobUz2Xp2i47UpDWjlTPrCTWfY9FNYB4sRet6d4gAO5_m3AOyTx2GlBtzmTpvWQ9iEgfZG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn1J3cziaJRuwEPhASa3zFGdLn6EdEOhExGp5cZkI1Xq1LRNiL7TL4oSLMgRDJtnnI1fK_XWeb0gJu_oDEwf1lLFybM2cIzOtzCBQAGV32L44zzCq10bnFKe_bssviKIDaXOsBRnrOomA6w_nlungay3kH8fCdPDscU2OA4Cm6FaIRwio1u98V24eNBUIBEd8UNJjR05R60fEjX-ATwIKuZVmX3d_OQG0CB8kozPOaLUikMduXsqaClFeJnAJr0xG00Ee7V1Ulct4bhoVNoik72ZXN-NcQ34QD6a1UL9ysgssyxWUfpkpyM4-dg-EQHkXQQvjqvVX0vXNwIs7-oA4g.jpg" alt="photo" loading="lazy"/></div>
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
