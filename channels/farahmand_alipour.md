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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHNFJyYEqpVwLM2egaouiUL1TyFuE7Y_47qqX7R0wyXgkVJSKHAZpcr7nhJ19UdVCLtHkfl5YfWdS4guk2Ux0ZEHeeHD4_Jc6KxAgfWUifs9enb8hK8sCWwCebrTYvqL_gv-auNTDvQ0c9Y54QyYmU2qXGOv5k5frqP8gB4bX-GKH45846raNxl4KSv-mfz1ocgQuI7PCNRDu9wxEb9QJcZzmXb5T0SYYQ9AOvY0g6KULqyvTUcoURKEUCkMAvdTGU7wbOnQ9svq_nwNJELuRKDcUmo4E00_FZHA5wkOC1lLVAfhyAG_4tMP6d-sncbMbRMvGtgeg4QDdVUb71DpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMrD2T0gpjUArt4MbfC2ITM9eIT0I6PMVpl4Ch34-2VBrxmRC1xU4pxWi3TQ5zGeYpPgxYIXwZqhIUgTF31pmaLuz9PGszENveY4Iqq0B_QtP3pjGcqNyX-g8-zSqyD0Zq_Xtsjtwwu81CCwGf20proS-RgvdkVLbhcL4fVQ85lAJbV575EEqLmIpmFwB5ablR-Xe90rZeQhD8Quf1unI0lbIgSm1DDmlt2DJckFIZIfk0CBPYARFIg4EfrpOaPitMOSoT0kYRi3CfbWd40dCBMPF8vZBOXNVEa0MtB3fos-4SAgczlkZoQQ0AGV4Zs7n-GAzlMljTll7NO0w3pS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxwKw9u1wKVi0le3sqPFXJ3CxsF1knfLf6mNDFc0QMEfDEnyoTWDWIcxmug7nrVAoG0YilGx548apFZ-Zj41EHFoTSW35j3jTyHyHTh_TShFp_IrNO7oqMxOgnInCivZqCMVJj2JHL71X9Q2ZN0n2NAyZwl7Yg-dFW9zpebWRNciy9cHlGdkVfrDgFVNRa0eCqk0QNhJxmA2TgITHvL9zof5OHPL4HglFUgbeNJIifrwDbPu38jqHL6PVnnJIwEw9yOCZIqhJCxLgLKIH0lBRgXa6naMBzoTF2dddu0otKs7BgQR8GS6Y2Lp6v18q3ExCve41eW8y9yXUgz8payoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Pyr6DFICdFfZoYth6e6DNKaFPLBHl4LHj7dlDfKT5ac28kD7k1Vr8W0XlBw8zit9kaKj7OZFrOvpBtkN10nr_kNIrci75ufQYuXja_pIfO4XwTo3Ap5k8OqMSf0JfvCkzJTVuIPQxReovxFyMYqqPQlorDxXhPSwbs4-wEa0VlYbbl73tibtmR2Lhk5CqXZZzl2vNS98Z4Jfv0BeyJXE9QsiY-uW-N6-6h9T-9pTA6TVIh1ae2a9lnp-Dtjd1KGuM9rrJJ1DuL6OTd8Fjy_Q_R5j7az3eterRIBpFCP4dsVyGd4hQ0oIEe2VYziFQHBGOHESa2KDB1IGDtrlnIs4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Pyr6DFICdFfZoYth6e6DNKaFPLBHl4LHj7dlDfKT5ac28kD7k1Vr8W0XlBw8zit9kaKj7OZFrOvpBtkN10nr_kNIrci75ufQYuXja_pIfO4XwTo3Ap5k8OqMSf0JfvCkzJTVuIPQxReovxFyMYqqPQlorDxXhPSwbs4-wEa0VlYbbl73tibtmR2Lhk5CqXZZzl2vNS98Z4Jfv0BeyJXE9QsiY-uW-N6-6h9T-9pTA6TVIh1ae2a9lnp-Dtjd1KGuM9rrJJ1DuL6OTd8Fjy_Q_R5j7az3eterRIBpFCP4dsVyGd4hQ0oIEe2VYziFQHBGOHESa2KDB1IGDtrlnIs4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwLtWHw5_hISQChZ86HTRxpxZGRid_ZPq-UZWWIeyZqHhmq4Ip7g5wtxbAjGOcy6knJEQCYhER2Wj_wJdNDrDJ3p0VX09GVfKwwH4DJKtWnGXzT7ZdVLOYX6-_85n34BZJX_lrX_R07EHZMvKOPhNQNe7smnwyVlEQL3AeDOlnARMtUurKcVaqKgPdqarR5EOjBpzkd9qtG5hMIX7CgTbHFODB6qc8bgHveZmvHsaziXB5SH4Dt_jWqvP9AkUBdxSGoQPvlUfFqBJCIyNOGvrd7KR-u5p6V7cZ_dvxWEW-UDq7GEJsQmafYa8uGIdRfLiROaUDKXx7zD1iBixbuw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ho7hnYm6kDVplrqEp7oPygSWhfb6kHqEVS5omqQCg5pwQv2J2MUJ9cJ_zjJPI50cwvpm9dLdwVxglFxBXNR2b7wJZwWvBGDlxj0Lc7Bz683wCAeGNY92U87ORooK-A6GKUMv0Bkex09fV4BD-WFGSyy1YawwiJ-q6TCtcTjxWr_CUInacuH_pPvaNTC3RKXpry6Cq1cYrBR4gLBySm5iLZaO5ODihnvIlBI3Sn5cP61BvrAnY0kydGi8vavdBK9pnw0_TVxWT6c4qWr9CTb9_RdPdeEgYBvZhhpzhFQQKh8YJQ3wmzXOVvBofwcRxg57b-BUz9r8E1EitB0LdivmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ho7hnYm6kDVplrqEp7oPygSWhfb6kHqEVS5omqQCg5pwQv2J2MUJ9cJ_zjJPI50cwvpm9dLdwVxglFxBXNR2b7wJZwWvBGDlxj0Lc7Bz683wCAeGNY92U87ORooK-A6GKUMv0Bkex09fV4BD-WFGSyy1YawwiJ-q6TCtcTjxWr_CUInacuH_pPvaNTC3RKXpry6Cq1cYrBR4gLBySm5iLZaO5ODihnvIlBI3Sn5cP61BvrAnY0kydGi8vavdBK9pnw0_TVxWT6c4qWr9CTb9_RdPdeEgYBvZhhpzhFQQKh8YJQ3wmzXOVvBofwcRxg57b-BUz9r8E1EitB0LdivmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5l21qnWUuE0ubqbRoE9QWPC3YWMesYusFHAB1JZltgZK61tZsweRAQLzi9Ve6Yg-yTBCIL97xDRZA8Zs2dX3B-rEECDcC87AfpVcSKmqZB_ZhFh6TGa5ntu7NGPmAjT5quNWiXVbTm7o78ybOMN3JHFPoTxmuqV3aP9SUWmNRxbVmuglAof4BeLyzjoqKPz82BJ8ecvak3Gl5GGOyEpSW9PxI9oePJCgoogNNuFDaNoTMPF0Yivpnyyi9QQi4YusxsF12S48y1HwGWbMXKqaf_TL3FoBoQkicH_4evOHTfGm8mrvXNIzDvi3ZOZ-ORLraT3B-95CSXaFMayRlsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ323fh_ZI4goosekrbUeky_cTExGCNCfpicV5PFuNxmipKcPA3EFwOyyFfGIxEJspPlMmvmU-Jwl9Ac3Trst-ALK2AuSOW5svsZfq0u8Mj4Ejl69gUeThPdA2i9wvYiyq-qTqWQ18ePS2WJIEwDID2hzNkX92k1o-M1v7V_yDBkBpTvBozoe_GgjLe4pMTBf-wB1-AmqFBl0T8oTQDVMtt_WiVFHahQd2WRMxHo1Utv5ugLyEpt004AEu6xfsvmPTxBkPBF2eSfcadSik-NI_wRdJOwdGjsGl7fdqyBt5CmQLjbl3oeM6Cix9VFEln1zx2gmTWrrMXGZIV45AWlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcxI0EEZ6AhqXI4ueTpVCvQbv4RP0WqZ-_8dWQX8bjy21ErK61Z00-huT-bmiYiBd099FfE88kKK0nyfS9pDG9OWrSm-LjOtzvNNb7ystnl-t-TQWxU3MKkmbQVsrbqMFYtsmsqkNLOowQSyvkt6w9Bs8jv7cyxMM3UQ12WbX9L2n7eH9af8m3BSlSXcd9xh5sKdQCwnciRdSUUCofKbT6rQ5OULzTqwm1p7yXNhx6pfeh4dJDpgIY9oyL5zkzaxUnbArlCMnEaG2K8aEeL0v_HQg5p-zT1ESXJ81yZW3tnuyCVPZ427l0V0V2GxZ-ncW4aKX_yDXz3KjNfaRcnTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFRvNqbTy3pzJkzuhbg_0c-odcwHCLWScwtJ5W-2yMv5ha5tC7lS_1R5rSfp6jPpMAEKK2elN5xcjUV8U0ussS-cQ0yXrBw6r7hMM6H4g4VflZzR6b-f16qJgyC_J8DT6N0wtF6_wee6HvELU28PpCy8yEdj2bxnx7-oqANbGi028NzVEUNU0FlJV7dBiPtjL9GiezhrofYH9xDHiJyL9WhDa5G7WUTBYpzVjtRGKMxw2vZ_7yedV36AxMk0066kA93f57-mcoUMR5P0mMQgcTedV2fMJBgeP9vdLkqWOhK5SYciG7yN3BwEVwaFlJP97OTHJGM9bnyStR0ZmGF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=B51b8eMjtX5Zov9JhuRbLf1NOLPBneY5f1eSqhEnnIOaSh7VJit6w00xzdENtrXiVwjx5IEuD5iQiVnZXPrOIuiPILelQS2LCL0w8BfffXdeDdhQ2s9XRRT64MFLDg3oVlA09ZTIDpZjXA5fLp5gB3TsK8RrdYrWCcWvOVu6LyLzyUmE78lhYMlZyJKoIn3BLKwliYi4ZV1RWJM51vQfRreSUNWzbr3Hp39uR3RWybS5gsFJYZb1oLbF8zj8WgtqBTJ0KjiL1QjZVau8GX-uzUHVawGm40evWCuq5IAxPO0BpmfHwDMH4yJuLaMNtKGXb_suM4sEdRBpNk0Sne2S_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=B51b8eMjtX5Zov9JhuRbLf1NOLPBneY5f1eSqhEnnIOaSh7VJit6w00xzdENtrXiVwjx5IEuD5iQiVnZXPrOIuiPILelQS2LCL0w8BfffXdeDdhQ2s9XRRT64MFLDg3oVlA09ZTIDpZjXA5fLp5gB3TsK8RrdYrWCcWvOVu6LyLzyUmE78lhYMlZyJKoIn3BLKwliYi4ZV1RWJM51vQfRreSUNWzbr3Hp39uR3RWybS5gsFJYZb1oLbF8zj8WgtqBTJ0KjiL1QjZVau8GX-uzUHVawGm40evWCuq5IAxPO0BpmfHwDMH4yJuLaMNtKGXb_suM4sEdRBpNk0Sne2S_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=kxqwKRONDcBvLoXIVkyzC2CANIoSfRuNyFru4VWsPQNOb5JIzIaSZMtJSQz02WkSd1vlBELTaM0vF8mGd2yxyDulZwxz9M7tIXc5dArteC3h1AX_uUC9IejxHxhh7Xbs9FPmA93nEPZgs-dXH1JTxefX5lNxjlbVcEHLsPywXtIxfSVLYLiQd-K33izT3NupK6kJtletFftN846egUUBfZpAj9uK_emv8TWf-Go77vks8FX8LAvxGWxqsWV-geXqsuVO69OyKSjeqU24M085CSB9KtJqRhGiuiydhrwWLMO8LXlxjNzyIn_r6jGSFE93ROFlLJAoZkfH_G0iLK1fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=kxqwKRONDcBvLoXIVkyzC2CANIoSfRuNyFru4VWsPQNOb5JIzIaSZMtJSQz02WkSd1vlBELTaM0vF8mGd2yxyDulZwxz9M7tIXc5dArteC3h1AX_uUC9IejxHxhh7Xbs9FPmA93nEPZgs-dXH1JTxefX5lNxjlbVcEHLsPywXtIxfSVLYLiQd-K33izT3NupK6kJtletFftN846egUUBfZpAj9uK_emv8TWf-Go77vks8FX8LAvxGWxqsWV-geXqsuVO69OyKSjeqU24M085CSB9KtJqRhGiuiydhrwWLMO8LXlxjNzyIn_r6jGSFE93ROFlLJAoZkfH_G0iLK1fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQPY6V5ZGxGXtRmHJHELUi2qyx42lWwt64xDvRjA_ocZAIrjxYtIfdguNcpOt1GzwsEFVIAMBmTs81EpTOJCeqSRRpicd3lQeXPVpdnDkf7CA8bHExydATl3rqeaWoMEN4CcepF11EPkFeyW0KwtI51nSEgi32icMyYa08d3S--DdNMiu5EEd1_ARdYfvTEdTKPnj6AUVga93c2QqmKNbW-MlP4sUvEBPDfeX3EULW9aZS6Tm8EwlbsMq_ImUWSsp8YlAzGdT38GCesWx2vaIHn1s3pcKgmDZxy-7QTVMuGMd2QhLl5Z4NmSdrloNsXLHLSxHShBOggmjJds-qxJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Ij3V0UvnOseGZnxQmpvy69kXl6MjQnqk-9uiWfi8xXyk2BDuuHtnEAN6g8XcsPnSYILmfyZNwVzlm_hsoMzFOMVrw3nuq1e6-ACFPOz8Lf0KtmqwygwQWTKXtTp-tVDm5LYy8Uv6HBQA5Vdou1IT8bg5QxSgZFRU_9-xtyBv4X1HNGHRB1o5-B7PmVNkHJtz0RGe-EkzVvQUPFfV3Fyj1fTV_rmoeYO_LVPnB9cag7611L7FCAW3Ha0Zcpu4adJQlEEJf2vDl1BktObCAS0NumVeonKJFlSPLad3AcWddBnyj7pDd7CJThUZ6K4MJWCxn2hKG8isNtbMNo9kRH6rHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Ij3V0UvnOseGZnxQmpvy69kXl6MjQnqk-9uiWfi8xXyk2BDuuHtnEAN6g8XcsPnSYILmfyZNwVzlm_hsoMzFOMVrw3nuq1e6-ACFPOz8Lf0KtmqwygwQWTKXtTp-tVDm5LYy8Uv6HBQA5Vdou1IT8bg5QxSgZFRU_9-xtyBv4X1HNGHRB1o5-B7PmVNkHJtz0RGe-EkzVvQUPFfV3Fyj1fTV_rmoeYO_LVPnB9cag7611L7FCAW3Ha0Zcpu4adJQlEEJf2vDl1BktObCAS0NumVeonKJFlSPLad3AcWddBnyj7pDd7CJThUZ6K4MJWCxn2hKG8isNtbMNo9kRH6rHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=bh87r7mdxXgM0T1fnwvIiKR9Bw8jX6oBirN1tEGnz3Ku3rtVn2chXsyld3o5QrwSU8XRJP1x5IE2SupkSyx1k4D4BR26_Oh3CYp_6qUNoEJRcDD-d-iIEM04xWgVV_m1NTmV-BtfWhs6EJbjCFPVlO8ccBcujtGXRPm_210dfU8ZDzzo-P4BvrvLokp3gRhDWuktItLWesKsK3wDsx3k87e7EATZsYHj88TWC2EgsO4ktP8S8_YbqpSXBwlwNKLwsYIPPws2EHqct9gtekvBaaRaSYFsTBZswHL9MhNZO_38LNZQhbvh2cngnijaVgKU0Qmi0MI0PXYxuZn9ZLo14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=bh87r7mdxXgM0T1fnwvIiKR9Bw8jX6oBirN1tEGnz3Ku3rtVn2chXsyld3o5QrwSU8XRJP1x5IE2SupkSyx1k4D4BR26_Oh3CYp_6qUNoEJRcDD-d-iIEM04xWgVV_m1NTmV-BtfWhs6EJbjCFPVlO8ccBcujtGXRPm_210dfU8ZDzzo-P4BvrvLokp3gRhDWuktItLWesKsK3wDsx3k87e7EATZsYHj88TWC2EgsO4ktP8S8_YbqpSXBwlwNKLwsYIPPws2EHqct9gtekvBaaRaSYFsTBZswHL9MhNZO_38LNZQhbvh2cngnijaVgKU0Qmi0MI0PXYxuZn9ZLo14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_zPQz4_o1MOfl9Pj0WpjQSqSNb8nagccZnKQGamWNQU3MH6i7WPeLaGUgP-fAhtPdvSfi8ZxbayKe80AYiu47u727rsWiUCvVgghxrcaGWoB5V8L1EHuFjKYzI5JYa5kWkojvrr-27bLh4zhEp6n4iYazrKoIUKmvxqcMulepK1XAwgbM08HoYJpFQhr5apcP9o8Vzg0L_vyxnxrVkZOmx-okpIkrBpD-Xywp6wYlFLQPqL4ERYHnc9ZCNuZcjgCDh0UUQ1SZ_alauuVcAdtCKIQuzSfGiFL7rdlm_CkSVYmrs_ocEqyeIqSAWFrZHk1qPdZwsqhHqOKi2u4uqHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=EOqjHKTe492FS9bM5fb-BNkuHnMBB5a-A-RWn6HoU-dF7mmOk7e3XAOP_01KXqDnTKN00x7DWH7JKo-gQYt28CpgVlVmoYk4RpHn4DkqOxqjlyJzSALIBdiu7zWeximgNCGS81z-XCfQze6PmPwef6pejFIO2n_0NSA87vVLPxukqTGlDlEfTO1wdlB3Q6l0f3LSqUeAKec5hh-tEm2oDPtlhzHGwTtDu76APRDDjMZ2s29-I5Ko7oJIGv6DrwTGoKCU6HZDymODw_eNo3QZFxhCL1o5XI6cpSkdEj_74-oHY5FDeGvEirtFevQ3DAHwCm7LIvwSf-uJJkCLZnQUvX66sZxmI5i7KR35t94V9kDQ6e3J8wsVfIt-RmInDYzxq9vqrebp1I33atRyl0oUqHJrVicsWbvpZQn2QVJtK7ewxvtpqK8Ya-szUM8iM9TOF6C7OjruZdWYBfsn2pKRNcTXBBtnrtd9y2gGQopxKFuCy-JPMrrc1445vSstra9RC7mxckOIkAUtMZ3hRVe7CAdQPx0sFgNfN0WRjWkYtfEJZNsndCK21XuLf5wn-o-Ku1qUd9PfTUSQ0R9BdHwi5pMpNVNvyTeiouciNlUJcA0J0eZonlMOYsE14v2uOU9EgWO9bKA-Fcwmz06BXZJgtdgYCktD_oseQdHXU6STP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=EOqjHKTe492FS9bM5fb-BNkuHnMBB5a-A-RWn6HoU-dF7mmOk7e3XAOP_01KXqDnTKN00x7DWH7JKo-gQYt28CpgVlVmoYk4RpHn4DkqOxqjlyJzSALIBdiu7zWeximgNCGS81z-XCfQze6PmPwef6pejFIO2n_0NSA87vVLPxukqTGlDlEfTO1wdlB3Q6l0f3LSqUeAKec5hh-tEm2oDPtlhzHGwTtDu76APRDDjMZ2s29-I5Ko7oJIGv6DrwTGoKCU6HZDymODw_eNo3QZFxhCL1o5XI6cpSkdEj_74-oHY5FDeGvEirtFevQ3DAHwCm7LIvwSf-uJJkCLZnQUvX66sZxmI5i7KR35t94V9kDQ6e3J8wsVfIt-RmInDYzxq9vqrebp1I33atRyl0oUqHJrVicsWbvpZQn2QVJtK7ewxvtpqK8Ya-szUM8iM9TOF6C7OjruZdWYBfsn2pKRNcTXBBtnrtd9y2gGQopxKFuCy-JPMrrc1445vSstra9RC7mxckOIkAUtMZ3hRVe7CAdQPx0sFgNfN0WRjWkYtfEJZNsndCK21XuLf5wn-o-Ku1qUd9PfTUSQ0R9BdHwi5pMpNVNvyTeiouciNlUJcA0J0eZonlMOYsE14v2uOU9EgWO9bKA-Fcwmz06BXZJgtdgYCktD_oseQdHXU6STP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUgrhpDt6Ps9zvEmlD_WvMdDlPl4kD-fIe3dnrqf7a7FTNz5VxGN6UNDX04Cq9XzOVAjtK9hJyb-5vJjtHxYaO6mO5W8mxQrr7rdW3J8IUhLEX_7zUohbxV84ma73xSMrd4gPXwLjXDpE35x6rR_w8IOyIZd69JlXsFB_7N8Iy49O4TJs_Wn2x_LC-fbuAjDlBgwMhq7UYkE9N72URHhiG0CAHBXwv3U6ri30Q5UteMAXB6dt0gL0gY91qaWiIAG4f5VVVcwORO0guVeFOswd-TccVqw8Ro40ylYNqDBAF0fkvhBSMa4rxrHbwOl0E40RbZJ_NnIufx9TkqmRxCdWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=btw2iG3pnS8UUMW9uJx31S33cZypiAGGg7LbkTlifdJWWQ9NJFPQZT9SuSwXMLwcticQCeXuk9VvMj1AYR3aALBL-UX3xsL9FCHKslcExdIP4rXVF5RrqyzP-3YoCPVskJuvEeI7jdj0to9tlqj6BRN4dKJ0wGxPhtZ-yxfKxmrCL2jvC7siih7_jpX2Kan-vrnUBtwtKsJqIS32XOSQpCMt_8D1VRITQw_C4scshzqlEXoM4gfmiuhQDaYDaj7UwEfb7-BWFDS8CeGREYbvdVrFkrWs-Ic-1-hzBPSjQtUT4ovEbx2hz2ssk-T9_mQv0P5Qx49tFrlqE2jvpAYj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=btw2iG3pnS8UUMW9uJx31S33cZypiAGGg7LbkTlifdJWWQ9NJFPQZT9SuSwXMLwcticQCeXuk9VvMj1AYR3aALBL-UX3xsL9FCHKslcExdIP4rXVF5RrqyzP-3YoCPVskJuvEeI7jdj0to9tlqj6BRN4dKJ0wGxPhtZ-yxfKxmrCL2jvC7siih7_jpX2Kan-vrnUBtwtKsJqIS32XOSQpCMt_8D1VRITQw_C4scshzqlEXoM4gfmiuhQDaYDaj7UwEfb7-BWFDS8CeGREYbvdVrFkrWs-Ic-1-hzBPSjQtUT4ovEbx2hz2ssk-T9_mQv0P5Qx49tFrlqE2jvpAYj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yuks_w24p75ZaKpBmQW9tvACsHmPQIcfaf662Mrev6T16aWkgfCgTlZTNmvHtTQRzsEy29f-KjsziWwfUpC5ld5vpxZmJgj0lZQUAZ2sdMce_Wjgk1WIGOqKMppGDBMMCIgOjnQ7I9_BdYtdDlGS2JpmVZCjCEedIiAyzjrNScdyTWenijZkXki5Bx4_nWJgmxMq1HCff0TCMWPOQ-F_xbY9B6YeQsdt3359M299Q6ZaHE8z5WeNc7X_FwZLRATFCklt33SDkomv4yV_VZtbGNNK-xJQtyQiNfseL5u969D3yAUOKWlnKaRd3vaGOdAT0eTUC02wK1_PcGdpFCbdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUW11cOLzWWnfEtJYiNzOHB9DxnveDVeN-ID4Qhk8jSYQZESxtJJKl98bv6nc4sXj43MawvRW13J--j3yPGBOp18cpR65IRMxsC43yFbU9B_GR_9kgBaU8uYyzk4S60Kzhi_CF2ZfX8vlzUH8tQmWeGvHpDfpXyZtjrCLbrJhTjfiUILqTx2n9GtD0W08mz8p1RKXuIhQDNt_jDFz6gtvvqgh8xhKXAw8B_n7wtPDlTlgN5FTykz24hpBLphBYqftGxwI-Rl7m830FbnhiqGZ6GpM3x8p4wYITX8UpPWqcnj3oKQVHQli9R3CMp5aaRmCn5LFAii_46OLcbeeHd6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biNyV2VPR6BqPoShzo2aVBfOuFR5YC-6im6lkI_pRB04k8lLysa8JlvM5Wc7-H-uHClpZiQpvF5jL64xmWD_U1oPJWLISoTuGJOy2Luy4pLwgKx-IjTltpTus-gjcJm8l3tB58IgG0hQ0Vw3uuYTLhaNF3hkqP0dwOkiIHdbpNuTaCIHuSnO7nstLmQVFBjwjxUNYC3VBsM2JtBnIQZZEaWXFdIAJkx3nSEVMeBc8brJjlNV5MsYZpihjG7cH-GdrgsZSGcFwtdnyqYA_tQd-LOs_0Kt3mgPWgmRT9fRfLhPquzMIiUz_DcPaxWzzeNVu0sljIExAhsDGjhWtEk9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=csl8o3zLyYC7V_PZZUEcOQ62wQD-eSQPHIQbJeX-8Uu1qzNs2vKRyXrmX-fJY1JAytCLQcWM4hUsPonogLc5uZY2gKqQuGmBDAr1hZ24_W1YpU1vpdIDD7yG-asXbLVWafDenGXAfOdvFyuF2mm1oftdr6hgaBf5QpSjfnZyA6sZtVyRgd1xBVCH-onPQX2naHeXFDjnJkpcrY1y1JPFP7TSQdc2mpPLQQIRYD3iMyK1qr9FdA_zzLUBkLDtHGWVV0PdhHoba0vOrRcTsU5jLAgCTXA0Ude0LggbwYcFEbNLmsFzPLMxXCEaJAo64wvwIaZvkYmALqRRTV-Q3aXBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=csl8o3zLyYC7V_PZZUEcOQ62wQD-eSQPHIQbJeX-8Uu1qzNs2vKRyXrmX-fJY1JAytCLQcWM4hUsPonogLc5uZY2gKqQuGmBDAr1hZ24_W1YpU1vpdIDD7yG-asXbLVWafDenGXAfOdvFyuF2mm1oftdr6hgaBf5QpSjfnZyA6sZtVyRgd1xBVCH-onPQX2naHeXFDjnJkpcrY1y1JPFP7TSQdc2mpPLQQIRYD3iMyK1qr9FdA_zzLUBkLDtHGWVV0PdhHoba0vOrRcTsU5jLAgCTXA0Ude0LggbwYcFEbNLmsFzPLMxXCEaJAo64wvwIaZvkYmALqRRTV-Q3aXBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFQRJ4RyGVHTr5wxL47ulRHCXxsDGNJbrMZO65aZXwsdT9CWQBgi6QCwbnWC8FFJI1ublD-Qmz2MhmAha9d6WzD2qMnMQSqxMo-9xEnVVmysKMbTPMbo2C6rKuPeSzTawKRkFjyaTHSgtMLH4TFzs0N77z4R5hVmwuxqWGVi7YzKoMYZfBhQPVaheL3g9Bkvz3GKBh7G_HvGb9QYYMz0WkDrFHs17bSpZTGVsFsCrHhEoTaMMjhJ4Xl2jPceebdIGfXopgUuqnLf09F2RTn8Izyl0CycMOtfmNjrKwa3mvRrI1dZ_l2k5MzSJbRl1dmau3yaCRScJbpmI5s6zL-Utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3_w9_9c0utT5zB_8mjbuO2libFgQEz_QHhbjz7FRNtk1uYhrMLjnA2uyaDABu2tpjMfx-P1lNxCKobBoN8uKu-tpzUgvGr8z1_P7eBTto3s48uEpIm86eDUS4WRW9-fXQ3aQyLGQgE2DGPeJH0sVhlbpxL7qXTFm9BXZNlzPGy84Ol_XtgI2sephrJ7esMQuA1NWjODJeFsgjQaHoI8TOsqQAKBv5ejzQod3SXqWGqb1LK8yq2qV2jxrhOcYVlCjk9fkH46vrq_yALnXUbUw69CDUPiSxgdEhCw3JN9IL_e68QB3GpRFTffClkdzNLOANIFzTwn4ac2vq4K25Zv5Ds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3_w9_9c0utT5zB_8mjbuO2libFgQEz_QHhbjz7FRNtk1uYhrMLjnA2uyaDABu2tpjMfx-P1lNxCKobBoN8uKu-tpzUgvGr8z1_P7eBTto3s48uEpIm86eDUS4WRW9-fXQ3aQyLGQgE2DGPeJH0sVhlbpxL7qXTFm9BXZNlzPGy84Ol_XtgI2sephrJ7esMQuA1NWjODJeFsgjQaHoI8TOsqQAKBv5ejzQod3SXqWGqb1LK8yq2qV2jxrhOcYVlCjk9fkH46vrq_yALnXUbUw69CDUPiSxgdEhCw3JN9IL_e68QB3GpRFTffClkdzNLOANIFzTwn4ac2vq4K25Zv5Ds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=AddzoGUDhu-dqhhdxU9y6uukt3EnLTCnUYasBq8O9D78d3wSLD6Bv32pNW06kZA0DLwdKz_yNOiVakbTdyx4fIsYHxju2H2_5CkbIWo4iLn-lwjIZmY7jUjYhiLqIneqwFZTRcA-ggLnTyCq1i3p3mwI2XajMle-rusnanvg33zydVqTYk_NosTAZ6H2vmawE1O7g4TLL6_npb7pUSXYsjG76gqGhFlPC-MrQ36zjltOsUEc6-Wu2bXxMi2eiQb6Hg8jE3gWr0XgWzPIXXsjA_4g09-VE6_S7HxemKCisFl_jzNlBv0ON7rIaTGoiQrEob2xx_UfKXoxPgv2lXC3tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=AddzoGUDhu-dqhhdxU9y6uukt3EnLTCnUYasBq8O9D78d3wSLD6Bv32pNW06kZA0DLwdKz_yNOiVakbTdyx4fIsYHxju2H2_5CkbIWo4iLn-lwjIZmY7jUjYhiLqIneqwFZTRcA-ggLnTyCq1i3p3mwI2XajMle-rusnanvg33zydVqTYk_NosTAZ6H2vmawE1O7g4TLL6_npb7pUSXYsjG76gqGhFlPC-MrQ36zjltOsUEc6-Wu2bXxMi2eiQb6Hg8jE3gWr0XgWzPIXXsjA_4g09-VE6_S7HxemKCisFl_jzNlBv0ON7rIaTGoiQrEob2xx_UfKXoxPgv2lXC3tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=heoa92C7uidgo7Rdxb1wkngxktILs8kF8wdJusVG4kL1ucn0ohwuwTXN6AxUBCvQ08QgqdIphIfTqeT7CA2-fRWdoFFv88QSZjpdm2Ch1lUlP9kMmMytoNRxH7wutDxABSatxGff4-JJlJYoWcnRzyJGvLAhjPucrOY2Mspw2376WCtFKDcGA1ltL06nNca-gbYjJp9I6KwsOUjH57c7yOz4b0_tGzxv3bqtz-DguQiaFEZtI46zPgitrbH82m1NXKBE7dH3gGfGoV3WLvqSSRxoENdKX-rdCydEj9jyUown2ZZY32tpuv2jrp133xcuw6VEpuez8HoKpGP2laz2o1U0YyTtSOK_WGydeGwTwh69pG1pzSX8wqdDSYPklRQ3HTiGKX7e1HzCxE1a9VUee6FtqHWWVLOVSc9C2VkXp_yqYq0P958uM9qbShqZcZXuo9s9zna5SBxDf07vZmLmNZv63B7JudhMEEqQvu6HyeGDxvOHLzMtcShgYD5SrlCTV79ptgtbGfQzDwgAMjRmzrOcCfOC-NDK6HdiwwLhyAFqWkDjlEZ6izG2qAtwlQ6-5eSfRzt6xgyi1pKawCYuUz0n4JW9lUMfMNcxQPArIamAhZT8KW0PHRlQ6D0TMAvyYNUJJIpNRFNxo1aREr-2KV77MCkda4MsxHkPGdaO-sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=heoa92C7uidgo7Rdxb1wkngxktILs8kF8wdJusVG4kL1ucn0ohwuwTXN6AxUBCvQ08QgqdIphIfTqeT7CA2-fRWdoFFv88QSZjpdm2Ch1lUlP9kMmMytoNRxH7wutDxABSatxGff4-JJlJYoWcnRzyJGvLAhjPucrOY2Mspw2376WCtFKDcGA1ltL06nNca-gbYjJp9I6KwsOUjH57c7yOz4b0_tGzxv3bqtz-DguQiaFEZtI46zPgitrbH82m1NXKBE7dH3gGfGoV3WLvqSSRxoENdKX-rdCydEj9jyUown2ZZY32tpuv2jrp133xcuw6VEpuez8HoKpGP2laz2o1U0YyTtSOK_WGydeGwTwh69pG1pzSX8wqdDSYPklRQ3HTiGKX7e1HzCxE1a9VUee6FtqHWWVLOVSc9C2VkXp_yqYq0P958uM9qbShqZcZXuo9s9zna5SBxDf07vZmLmNZv63B7JudhMEEqQvu6HyeGDxvOHLzMtcShgYD5SrlCTV79ptgtbGfQzDwgAMjRmzrOcCfOC-NDK6HdiwwLhyAFqWkDjlEZ6izG2qAtwlQ6-5eSfRzt6xgyi1pKawCYuUz0n4JW9lUMfMNcxQPArIamAhZT8KW0PHRlQ6D0TMAvyYNUJJIpNRFNxo1aREr-2KV77MCkda4MsxHkPGdaO-sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=YN89Wt3gjyhQNz7ApRqV1easD_qPxGX-dqt1XvwXlzjXPbDuIn8_rHyoV5N2-ZgvIPbN2JeUllpkplKUuPk0VsF3QlESZkRFLFy_etQ7PaQ88PUQOw9FiMV-yHZ7C-TXG8oQwiRUuh9yXeBxF_HhbFUJMxNb5sAgw-lHIaDZl7D73TiSQ2E5hBfhrcyh5q2X73OemHUQ9UoTlQ6TxDwXCtO1PqDYKB8BRZz_FjTxq7CGAXiaSkZYymZr-uK6mZe4q_6HpRVo6IcsFMYzYnC52dNQaFf9qw8DGmgM66sqsuYhwtDoX3PT-3yndVlLqFMJncaraQWByTwYKngO7WI2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=YN89Wt3gjyhQNz7ApRqV1easD_qPxGX-dqt1XvwXlzjXPbDuIn8_rHyoV5N2-ZgvIPbN2JeUllpkplKUuPk0VsF3QlESZkRFLFy_etQ7PaQ88PUQOw9FiMV-yHZ7C-TXG8oQwiRUuh9yXeBxF_HhbFUJMxNb5sAgw-lHIaDZl7D73TiSQ2E5hBfhrcyh5q2X73OemHUQ9UoTlQ6TxDwXCtO1PqDYKB8BRZz_FjTxq7CGAXiaSkZYymZr-uK6mZe4q_6HpRVo6IcsFMYzYnC52dNQaFf9qw8DGmgM66sqsuYhwtDoX3PT-3yndVlLqFMJncaraQWByTwYKngO7WI2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcTgeb9YWVykIIwaoDqbkmeTUoB2JhUxadlsDy4OrnFve2nMsKoridA6wLAyn2jqbhEuCipK3Qp4bduf_0TQ0cuDkTBRigqe5YxurN87KdwIkBN-3MzkJkZOqNJQHnXJ3dgIE4ZUfkL4tQwZUat2r9KQ4FQFE0dC-9xoc7iHHrBir2O2qEC-ToCszSzXBdhuVcsmJZDuSdi7Yu4rQkbh-TiQX6LrYC9nocmxcDpEM-cshHfM9kFkTjJbdh4X5dNGIVA41Et7buZUug5g-lrqy7UKiJ2U7qB_irA9g8mWOuie91PKGtbNDjNkOClUVEq0X0TKY-GnIS8cO0rmpkRkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=G1P-3WGXqxVDTrCLV4PAZd19bgDVvTtFJ90Ejj46ZdnIm8zBuVEzYcy4ps2vBhE4Bgi2Pkr5uL28IUT-sxpzmer6Rt6Dnbj5XjcH4X6Z6rEvd004sZsDsqt_sspXWjeje4tvkHjq43mMp6kwA8Dxro7lmi3YdJ5nlORsisFMmxeF6JnoAv4ygQrKhZjV5BaQlkEVgl-rkDFcDA6mnmNnkDlRVA-6MaaJJ6r78WPr-xISq27UmQAqbdus0xTHFiMtrAWvR7394dt1PafLsYD_5KFJJ2tNh8DdIvrFgCUWWwLTnX_sie32GxVQdwEXNvvfpkwvIGCfpJfPH33F2QcaPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=G1P-3WGXqxVDTrCLV4PAZd19bgDVvTtFJ90Ejj46ZdnIm8zBuVEzYcy4ps2vBhE4Bgi2Pkr5uL28IUT-sxpzmer6Rt6Dnbj5XjcH4X6Z6rEvd004sZsDsqt_sspXWjeje4tvkHjq43mMp6kwA8Dxro7lmi3YdJ5nlORsisFMmxeF6JnoAv4ygQrKhZjV5BaQlkEVgl-rkDFcDA6mnmNnkDlRVA-6MaaJJ6r78WPr-xISq27UmQAqbdus0xTHFiMtrAWvR7394dt1PafLsYD_5KFJJ2tNh8DdIvrFgCUWWwLTnX_sie32GxVQdwEXNvvfpkwvIGCfpJfPH33F2QcaPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=O6XIK-8XDpYmrcYEL7LXtDsk_oVpNz20f6ideA7B5n0--BtJ0Z6CKJok_EAf9S9Iqyhm84npWb2tcApeIxr8ect_4D_dwaXR6RejD4Wt4kImgJXMGUffGJnl7FnnZL4ktM8yPHjp1bjneEaHSp8HIFmbVOh_U0XYm04lpMKHJKYgQ3A40weSrA7KFr9cDOjlVDaPltwl--U4WSfzCYrhOmpI8xzAY0i6v_3GaRB6qV7R3Rb_jpECw7-JBC72pn_hAkDbjcrdqHMtJgkeo8--INMCCN18PhknqrGgJv3bUAC94plJh41vSZa_HHBEhNwpnkm3V8cgk5d9GUOlJ93Q6q-w3l6BruAQSQAmKSEMLTQEbwUYYWPzPs-E2FGQxTyjNvbLy3J2SHo94KQLcjA8cVAEfqUdhSUgihNzpNVjI4Fg59wZYsQmlzwIfmUa0lpB_MV1XfrRzaXb7tcyVszlyKcm3hyJAMYXXnAotNKkVL8pzjeCxQFdXIgENiLuv5VJQdax8wcVgRwkrGg9OB1l44wkTv6gPhXLJ-lpxpXrzyPAtCdcOHsYMdnP0zC6E3JN6Mkhyms6oA-x4mulkwqmt9iOXNrmozEvuzzCqNTm084u1zZcNw5FkQ0wgFlH2dmCezn4Blais25ZqvKKl_8QtkL7fqzbTk-_42Rb3XX0flI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=O6XIK-8XDpYmrcYEL7LXtDsk_oVpNz20f6ideA7B5n0--BtJ0Z6CKJok_EAf9S9Iqyhm84npWb2tcApeIxr8ect_4D_dwaXR6RejD4Wt4kImgJXMGUffGJnl7FnnZL4ktM8yPHjp1bjneEaHSp8HIFmbVOh_U0XYm04lpMKHJKYgQ3A40weSrA7KFr9cDOjlVDaPltwl--U4WSfzCYrhOmpI8xzAY0i6v_3GaRB6qV7R3Rb_jpECw7-JBC72pn_hAkDbjcrdqHMtJgkeo8--INMCCN18PhknqrGgJv3bUAC94plJh41vSZa_HHBEhNwpnkm3V8cgk5d9GUOlJ93Q6q-w3l6BruAQSQAmKSEMLTQEbwUYYWPzPs-E2FGQxTyjNvbLy3J2SHo94KQLcjA8cVAEfqUdhSUgihNzpNVjI4Fg59wZYsQmlzwIfmUa0lpB_MV1XfrRzaXb7tcyVszlyKcm3hyJAMYXXnAotNKkVL8pzjeCxQFdXIgENiLuv5VJQdax8wcVgRwkrGg9OB1l44wkTv6gPhXLJ-lpxpXrzyPAtCdcOHsYMdnP0zC6E3JN6Mkhyms6oA-x4mulkwqmt9iOXNrmozEvuzzCqNTm084u1zZcNw5FkQ0wgFlH2dmCezn4Blais25ZqvKKl_8QtkL7fqzbTk-_42Rb3XX0flI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujOjyt45k3lK76MzvAQnmFxDmF8VNMPV0aKbQrbYl0o9Z3eLKBY8iWfbS102yCGz8Ju9gnsN8xE1FMAD6gPJTAL4rqyMUvxbkerpv66hXSyKSPTlTd-tRgUlZI04TJ3jcf88Oq8wCeyZsWqSsWRuJwQqYfm11mx1IHw_BvJWa1qp4g_L2ogAYuT7DHRoBb2fZUumkcVWxIcYpm68bsYi_J6P3wjnvRqlaKPVNq5A_ZYC6HPqZuj2TuqcnisRFk-HDgnfBaq4IvDdqcBYe360V68gq7cGSH3jPJba7ns-ladgKY82MzxOJimeVz0gxYSshh0IeOCfqTN0x-lvTTLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=RO0RHG54VLAijTMF8IR5hv0izrz829kNUUIzuPkd4VQnHTWUawRX7sq5NRWtOEUqoTvQh8cHP3wbR2DXLqp03fN_-O2fjp850axTkEworWzO8EEm4oEvX6cKzlm-qK-XJx8JHfnr0z4cuS8XlvxNkFrSm7Gnb65ZoNge3f417RnOV49P0T3FKzqVnU65KNvosDQtp5wIjwLXDyMt3ytpNLqO2LfHf1VhNqLoNb6n5f27xeD0qSfFUz0kHrDgzUD7CdrhDjvKEShArFadeulcN20rWFTwM-WV8DLPgrcrvSdY6iAVfGivyVJ92ApHWAscafhfJhdeGS9RqPe4KZwUAWsFTYihap8YhYXZ21Lm3GESZe0rm-8QIcRgjqDmk-S8-YLFneA8wvPsgvde8QbEfGDl4gpCVSkCRfVFOrYctGnTtm8QvC3m---aLKObr8EM4k8psF9FaqS0xQHGik3PnVdk5XyIvgmUWxcep8dEdADmyEG6kFOJrlcRTTslH1i_MdTSVz3baUBhu_RoEUd3kqBI93mpj2JYDIcy3gW4SVH_yTKr2W5yDll87kOfqtduy8O0zVwCY8j5ihpcajyJiOk59H03K2pmtDMdEted9XnJJcB2PLbYfCgQeILsm0eeeeVsLDPdNIVKeIeQBgdXKWZjQfA9J3f485F8BMNcTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=RO0RHG54VLAijTMF8IR5hv0izrz829kNUUIzuPkd4VQnHTWUawRX7sq5NRWtOEUqoTvQh8cHP3wbR2DXLqp03fN_-O2fjp850axTkEworWzO8EEm4oEvX6cKzlm-qK-XJx8JHfnr0z4cuS8XlvxNkFrSm7Gnb65ZoNge3f417RnOV49P0T3FKzqVnU65KNvosDQtp5wIjwLXDyMt3ytpNLqO2LfHf1VhNqLoNb6n5f27xeD0qSfFUz0kHrDgzUD7CdrhDjvKEShArFadeulcN20rWFTwM-WV8DLPgrcrvSdY6iAVfGivyVJ92ApHWAscafhfJhdeGS9RqPe4KZwUAWsFTYihap8YhYXZ21Lm3GESZe0rm-8QIcRgjqDmk-S8-YLFneA8wvPsgvde8QbEfGDl4gpCVSkCRfVFOrYctGnTtm8QvC3m---aLKObr8EM4k8psF9FaqS0xQHGik3PnVdk5XyIvgmUWxcep8dEdADmyEG6kFOJrlcRTTslH1i_MdTSVz3baUBhu_RoEUd3kqBI93mpj2JYDIcy3gW4SVH_yTKr2W5yDll87kOfqtduy8O0zVwCY8j5ihpcajyJiOk59H03K2pmtDMdEted9XnJJcB2PLbYfCgQeILsm0eeeeVsLDPdNIVKeIeQBgdXKWZjQfA9J3f485F8BMNcTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=X6Jrw4dnfkNG7p3qp5NrVpMOWN_tAXEeACjAAhyZ-lgRHuo7Cw-k7Uq_9DTLPXs5_SK4eYDLPQ7_ZEzro8FtVe-AauNrX0ruGwSQF7M5sFSP7JoP6sZCNrRi-7gg5dRgPiqbnfL3IFNuWJt5VUB7BdQPQCmhbDpyofNU51bPN1LJk6SWMN7JMcPL1cQpYfftRin7fkSs3mCqY6yU6ubMSU_0_GknqWT3fWmQBAFC4DekmN2z_eY5WwEyn0fQVTB3tgkSu7WH4Hn2hEC31BMR_kAN69XMpAw2Iuxb1rho_QVQ-VlW018PyKuPX3VbbRFKnLDyS_Bkatce7KgrqnVu34GAySrHm8xE2owrPWxVo-dVVjMt0K-KXRRPMLlZxK5ChbR7y6vnQEfB-Q7ZbuN2zp3Tgu5hOTVkqyWs12Suf3TOgqEJV8ZBCwr6m5nut8UBrpf5qhSzcdcacordFrBQFRBWOcoRUT-SqQnnTxYt1sb_HGVol8axAS5_ZtjxYNCcRUKOxMaucddrP_zv5AMExfEu0-8G1mt9jaN8R9qBA8rud8FULSeDfp_eprX8DQLQWDMvJWOloIKYUSq-AH-tNNfw6a6gdLALncMCeEjmF7uTmhnz3EQBthU0dJSS5qqgrfnRHHo_GsKyvy2d4z271RXSkeY_2njlZga0k_LT4Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=X6Jrw4dnfkNG7p3qp5NrVpMOWN_tAXEeACjAAhyZ-lgRHuo7Cw-k7Uq_9DTLPXs5_SK4eYDLPQ7_ZEzro8FtVe-AauNrX0ruGwSQF7M5sFSP7JoP6sZCNrRi-7gg5dRgPiqbnfL3IFNuWJt5VUB7BdQPQCmhbDpyofNU51bPN1LJk6SWMN7JMcPL1cQpYfftRin7fkSs3mCqY6yU6ubMSU_0_GknqWT3fWmQBAFC4DekmN2z_eY5WwEyn0fQVTB3tgkSu7WH4Hn2hEC31BMR_kAN69XMpAw2Iuxb1rho_QVQ-VlW018PyKuPX3VbbRFKnLDyS_Bkatce7KgrqnVu34GAySrHm8xE2owrPWxVo-dVVjMt0K-KXRRPMLlZxK5ChbR7y6vnQEfB-Q7ZbuN2zp3Tgu5hOTVkqyWs12Suf3TOgqEJV8ZBCwr6m5nut8UBrpf5qhSzcdcacordFrBQFRBWOcoRUT-SqQnnTxYt1sb_HGVol8axAS5_ZtjxYNCcRUKOxMaucddrP_zv5AMExfEu0-8G1mt9jaN8R9qBA8rud8FULSeDfp_eprX8DQLQWDMvJWOloIKYUSq-AH-tNNfw6a6gdLALncMCeEjmF7uTmhnz3EQBthU0dJSS5qqgrfnRHHo_GsKyvy2d4z271RXSkeY_2njlZga0k_LT4Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=jeo4JL4NePrgRB9R3y2UpQQKkgmotIfL4f8O4d7m4iaZS2Y7kdqtz7Oune4bj81MUE0RWLSTWl--Ii6zLmEGd34XmGKxq5BPuKc9lwvNT_UU2k1xyRi-U52aas_FM99h9OOdhEcHYv0e6net527exwuSmPUuJ7OjAzDzOwMpaVyKkc1hIVRCXb4_m2jYbqIrHNecMBHnsLFZj0vMPTHEwEj3hbUmGz33gxRWH6drzcsrC42Fn6H_bMBTsHimsD3k-PL-J5Pq3gJwi_jDf2_pvI17Mx5C1aeIm0mN7U7JOjk0x2FOLw8DJJp2ct4ka-WQbX9x9AbRduNW_vizJKTrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=jeo4JL4NePrgRB9R3y2UpQQKkgmotIfL4f8O4d7m4iaZS2Y7kdqtz7Oune4bj81MUE0RWLSTWl--Ii6zLmEGd34XmGKxq5BPuKc9lwvNT_UU2k1xyRi-U52aas_FM99h9OOdhEcHYv0e6net527exwuSmPUuJ7OjAzDzOwMpaVyKkc1hIVRCXb4_m2jYbqIrHNecMBHnsLFZj0vMPTHEwEj3hbUmGz33gxRWH6drzcsrC42Fn6H_bMBTsHimsD3k-PL-J5Pq3gJwi_jDf2_pvI17Mx5C1aeIm0mN7U7JOjk0x2FOLw8DJJp2ct4ka-WQbX9x9AbRduNW_vizJKTrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=T7dMzUk9VjplCzghIuCp__M4THdMTZ12ku8NLMI_PrQ-UShM6X_vyZr_clTuPMPZ2mPAD2P5wJ3um8vkfSm1M01h1iRbgspk2_bfr2YIGJIS6KLcFuye4gXQxVtwEntxHlz5PwnVMyqxsCkgVTIrH8VE8cdHiTycUPbhgW2Vl2ppzonIejBfvS084lvhu8JYJC_Iyn8wgLbIKVfiHSriWEKOXR1TgaVWMc88Al63tnAGXqKz-gehq-s2nnvB3D1mZG1VCNCd1pfx-ccy8YZlGAWcKiRhnO685LRuNInhkLuSzQg9DOSVwVGSO4RuHA7RwmCCOEMJ9kTXb2z6Ljp3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=T7dMzUk9VjplCzghIuCp__M4THdMTZ12ku8NLMI_PrQ-UShM6X_vyZr_clTuPMPZ2mPAD2P5wJ3um8vkfSm1M01h1iRbgspk2_bfr2YIGJIS6KLcFuye4gXQxVtwEntxHlz5PwnVMyqxsCkgVTIrH8VE8cdHiTycUPbhgW2Vl2ppzonIejBfvS084lvhu8JYJC_Iyn8wgLbIKVfiHSriWEKOXR1TgaVWMc88Al63tnAGXqKz-gehq-s2nnvB3D1mZG1VCNCd1pfx-ccy8YZlGAWcKiRhnO685LRuNInhkLuSzQg9DOSVwVGSO4RuHA7RwmCCOEMJ9kTXb2z6Ljp3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lgpSCj9zWwQG9PJ8D-qOx0rf8qJObaABSlkkUg320JCxV9Wbr-J_sUCeyqv4uODm7_HbPLjn3AEcemP8_JhMvNnQ1hSVzoh6MyCxsjocaRABeCqZ7pz-FbS1jkWSfCh_pmQcQ2wVw_Ge5CavattuWDOJU15e_KoLMv0jUJec-b1j7wR2Hz-AzUn_EqEvxLTIhEH5-zXjNkbrdXZb_iTvKXhcKCCJo0RbylHKu5nf8jCR0QTg1TApW81j-_n6zsu1LePihBNPBWGTN13TGt0EGlmOygcFIY5OiRUHclWkyQ5n7MorLJbnJMFEficgfQEVypsJ0UM8f6H4TOTrYh1tjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lgpSCj9zWwQG9PJ8D-qOx0rf8qJObaABSlkkUg320JCxV9Wbr-J_sUCeyqv4uODm7_HbPLjn3AEcemP8_JhMvNnQ1hSVzoh6MyCxsjocaRABeCqZ7pz-FbS1jkWSfCh_pmQcQ2wVw_Ge5CavattuWDOJU15e_KoLMv0jUJec-b1j7wR2Hz-AzUn_EqEvxLTIhEH5-zXjNkbrdXZb_iTvKXhcKCCJo0RbylHKu5nf8jCR0QTg1TApW81j-_n6zsu1LePihBNPBWGTN13TGt0EGlmOygcFIY5OiRUHclWkyQ5n7MorLJbnJMFEficgfQEVypsJ0UM8f6H4TOTrYh1tjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hYiWKW83i5ybG9oMV91pozpF7X-m2hrge2Cfq_Xk-clVMMdEskbmAUy2YL7xegC4TnHgkcBvipLUqLQopRYX0_mwRyksJ7RT5hO0JOh5euJ5_Aq78G-k7Gg_7_HXp1PZu3a1V52DM-1OZeBv5cMWcrrb2gh5_hPiL4719GrcFu6k3CkzcSTEZwmiQOBC1UPQ2QCOuco0cOFQLcswJ8FHhnZ1AwxiWlz12lwDcCIJpcjy-tYztgrTI3mMma90pvrNo1xJLGI2ozG-8iEnQXkq_V6FEAaPXDi_Q5Razluoc31GXHyZEF9ckjN3uPf4xorkHFrgU-iBgRdJYeudUoCbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hYiWKW83i5ybG9oMV91pozpF7X-m2hrge2Cfq_Xk-clVMMdEskbmAUy2YL7xegC4TnHgkcBvipLUqLQopRYX0_mwRyksJ7RT5hO0JOh5euJ5_Aq78G-k7Gg_7_HXp1PZu3a1V52DM-1OZeBv5cMWcrrb2gh5_hPiL4719GrcFu6k3CkzcSTEZwmiQOBC1UPQ2QCOuco0cOFQLcswJ8FHhnZ1AwxiWlz12lwDcCIJpcjy-tYztgrTI3mMma90pvrNo1xJLGI2ozG-8iEnQXkq_V6FEAaPXDi_Q5Razluoc31GXHyZEF9ckjN3uPf4xorkHFrgU-iBgRdJYeudUoCbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=i-z0w3UmHaFo_05wGQ9f5HjmP1CoZMdwujE0EezaKm0J0ZPyojZALfrExbnYGxqLxPElWUWwGNsLTqV8Iaurx-G41SG1Whp9lfsol0pTh-NPxeRDu5JXQjn55hUyQgFeQz48DM0qE4mSLvzcyFdKps2NdZhPUOk_mNh7M8BjrNX7blgeRHN0-mlKjUlFYsOmkYNBxsBQTawqu4p8TJiRwvTS8mS_Aj1kAVPxYd3pLQAOrJaUrExrOZV_6rsRoXvmKKcntzB0_-uKTSkMgLciyroQuYhIcgEyz-wtIM8ns3PshQNc9iUuitPJ_akOdo1J3sBAVgN4NByN9PkGncW9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=i-z0w3UmHaFo_05wGQ9f5HjmP1CoZMdwujE0EezaKm0J0ZPyojZALfrExbnYGxqLxPElWUWwGNsLTqV8Iaurx-G41SG1Whp9lfsol0pTh-NPxeRDu5JXQjn55hUyQgFeQz48DM0qE4mSLvzcyFdKps2NdZhPUOk_mNh7M8BjrNX7blgeRHN0-mlKjUlFYsOmkYNBxsBQTawqu4p8TJiRwvTS8mS_Aj1kAVPxYd3pLQAOrJaUrExrOZV_6rsRoXvmKKcntzB0_-uKTSkMgLciyroQuYhIcgEyz-wtIM8ns3PshQNc9iUuitPJ_akOdo1J3sBAVgN4NByN9PkGncW9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IwCmpzxz-tV_bpcydiviibd5equARvUzTVFUhM0SbuW51N-RVJ0Bkyk_mF8o8Anv-YHMDGpJSqFnvnu7pVBr5-Btt7LioilH1TmANkq4Jy6qR0MZAMedaGlShkSAXYkau-OopVBho1Lo23cFFB9f0OFnQaILlBgMg3DkeSSFxXNVuqFHeKHB20nQ4cNMtmRdC0R71BlniY944GcSIrHAmpJlc5GNjMBJLymheUlsrQSFRd7lJvvHMROZIBK7WoooERypkAc4kZXfaSubCR-bPay922p8yQ6GkrBAcVPMPWERJsOls9-J3fY9ueJQUe1jK_ssb9F4ytCz08dlQVZuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IwCmpzxz-tV_bpcydiviibd5equARvUzTVFUhM0SbuW51N-RVJ0Bkyk_mF8o8Anv-YHMDGpJSqFnvnu7pVBr5-Btt7LioilH1TmANkq4Jy6qR0MZAMedaGlShkSAXYkau-OopVBho1Lo23cFFB9f0OFnQaILlBgMg3DkeSSFxXNVuqFHeKHB20nQ4cNMtmRdC0R71BlniY944GcSIrHAmpJlc5GNjMBJLymheUlsrQSFRd7lJvvHMROZIBK7WoooERypkAc4kZXfaSubCR-bPay922p8yQ6GkrBAcVPMPWERJsOls9-J3fY9ueJQUe1jK_ssb9F4ytCz08dlQVZuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ahoUDMOhLd6IfbtKxcHRBY4F1mVJjabPbGaFCiP72jsy4tj2bv3-nuWPx2FQY1_5Fm3NnvstavJzeBMXVosoYyVWWtsAVk1MyY5p5pnYW8uRDLxpCpNaZv1W4_7B36daesZAS_PuqRvkKBxRHMhHSOzycmrRpa_Ks3i4rBQkyntPIyECP9vpX2WneuMX5ApgFvFXNisYZ90PTg533K9poSpx-HShu_kXLa0iWF2PQdPQytf8t0lPgavFiPbEc5DN9OJHVDQ3ufkozQOPcSzM1MfjohpemUU9wG795pFmKtfLLbSAV395i5llxrDdHpFn4kh_b_Viuu4hiszBGGq0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ahoUDMOhLd6IfbtKxcHRBY4F1mVJjabPbGaFCiP72jsy4tj2bv3-nuWPx2FQY1_5Fm3NnvstavJzeBMXVosoYyVWWtsAVk1MyY5p5pnYW8uRDLxpCpNaZv1W4_7B36daesZAS_PuqRvkKBxRHMhHSOzycmrRpa_Ks3i4rBQkyntPIyECP9vpX2WneuMX5ApgFvFXNisYZ90PTg533K9poSpx-HShu_kXLa0iWF2PQdPQytf8t0lPgavFiPbEc5DN9OJHVDQ3ufkozQOPcSzM1MfjohpemUU9wG795pFmKtfLLbSAV395i5llxrDdHpFn4kh_b_Viuu4hiszBGGq0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDkeRi_curWJgUnjrzkGOzSz2b8_Z_Ein1wg6JEn6fDhk-f7RLw8dHKoy1jwQV-fewmDNhe8MFi3193rXhEmshvi7g-m-_dyQ1KJFKv3ixS13DyOT13N5vANrshlfkI_6Qx8PJgiExuXwZYJF0vFpoBs_lpgR9TbU2bnIjNI4pIqq4pIigstUGuJcWUu9dKX6sb3WgJxSD_2QtD-oH2PbH_wGhn8eB1XP-d7cDL4xPjf5Mgdjhltwv1XWm9WATaLTwFnlKdswPGkPMuCpA3RVXFrLA9LHkMMLRNzQEysqz245Kp_ki0tPk2pGlEv57BunBeWQOifLLYtLonF-fw8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZtSwaWNxtS39d5uoie80xrrSTYTPwfOz-jYpOKQl5Blo4Uux7WTEcBoK8IuVM6643o4YGOQF8xxGBtfN4YXGS7G-FLN9ACXetAsbM4qCP17BB_oX4iTuZys2PKghwqiBcTEItqbSbZXnYzeDkH8wet9wpgWHrssMf7LyPZFSNsQX5hyRHp00AuO1SsdjWeumlO7YMATbYDgHEyhmcyVmg8xCvBdEi2JoKGE_7ZuRsfxhfheiVQ-UP5cF0Z523UjStxAbAdV6Ueae4bMuxPCAo39v-u2ImySeNYpPIjZn7_US0gTugBJNUCt5RBevb5YQLcbthwmrWki3reAk8ROY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZtSwaWNxtS39d5uoie80xrrSTYTPwfOz-jYpOKQl5Blo4Uux7WTEcBoK8IuVM6643o4YGOQF8xxGBtfN4YXGS7G-FLN9ACXetAsbM4qCP17BB_oX4iTuZys2PKghwqiBcTEItqbSbZXnYzeDkH8wet9wpgWHrssMf7LyPZFSNsQX5hyRHp00AuO1SsdjWeumlO7YMATbYDgHEyhmcyVmg8xCvBdEi2JoKGE_7ZuRsfxhfheiVQ-UP5cF0Z523UjStxAbAdV6Ueae4bMuxPCAo39v-u2ImySeNYpPIjZn7_US0gTugBJNUCt5RBevb5YQLcbthwmrWki3reAk8ROY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aBbhwJp9mWIyUfvzksjG7Uf-x-QxqfmpHSYKk04Fu0yxY0k0kdIZ8IB3W2FPAIlFZCtQtuAOIlSshbhElgDJnHcXOnrgsdD5HNh8dCEwd-6976ckPOSWW6VmDTtCA9iNb4_m4KPyGPcQM9QdZsyccGpsobhJdpNfUHEDcwFk0J71jyyYSeqsrKLdbcJQEMc-NW6mxHMwpMwlcnjA6uu4GOtEL0Eoncc3aHhgBAynDJi2mSsPPSs4hPfmpbm_JB-j0H24Xf2YRwMxjHUpE7FH3mkOIzozXRZhs9p4CYTSQ29N54Kuhp1ot4yQEL7nuXo5UWnQaf04Ybt1rsHf60SlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aBbhwJp9mWIyUfvzksjG7Uf-x-QxqfmpHSYKk04Fu0yxY0k0kdIZ8IB3W2FPAIlFZCtQtuAOIlSshbhElgDJnHcXOnrgsdD5HNh8dCEwd-6976ckPOSWW6VmDTtCA9iNb4_m4KPyGPcQM9QdZsyccGpsobhJdpNfUHEDcwFk0J71jyyYSeqsrKLdbcJQEMc-NW6mxHMwpMwlcnjA6uu4GOtEL0Eoncc3aHhgBAynDJi2mSsPPSs4hPfmpbm_JB-j0H24Xf2YRwMxjHUpE7FH3mkOIzozXRZhs9p4CYTSQ29N54Kuhp1ot4yQEL7nuXo5UWnQaf04Ybt1rsHf60SlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Fu9tj4wfGnt37VygaBGtYc1ut9hGm6s-nsvvUrx5LwHJbcz5qFfEq-tkZfAbGaGrkQwpH8FSJvB6zT6JJLosthG6HfEaNM7Cfq0HBwQ7A85_01kkQbbfdvyFybNIAri-yhaT8ryJjt1V1yWwHmGCnVpq97luDLQ8BQVD14-gBXj3s5akONPl6ERsmH2FDAvmKeNjYD60fwEvPd6-Rh077UEH5pxYD77WuvrtPWTQC4vehUNIaCCD2HpUrUJByXr7ZBtwGDycOrc7fdq7RJCpFVN0QwzZxWDNeGdYbxIF-0mgEdB-2E8CXMmgFyc-M2ENsO6VyGrjny5Vju3HdzvjkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Fu9tj4wfGnt37VygaBGtYc1ut9hGm6s-nsvvUrx5LwHJbcz5qFfEq-tkZfAbGaGrkQwpH8FSJvB6zT6JJLosthG6HfEaNM7Cfq0HBwQ7A85_01kkQbbfdvyFybNIAri-yhaT8ryJjt1V1yWwHmGCnVpq97luDLQ8BQVD14-gBXj3s5akONPl6ERsmH2FDAvmKeNjYD60fwEvPd6-Rh077UEH5pxYD77WuvrtPWTQC4vehUNIaCCD2HpUrUJByXr7ZBtwGDycOrc7fdq7RJCpFVN0QwzZxWDNeGdYbxIF-0mgEdB-2E8CXMmgFyc-M2ENsO6VyGrjny5Vju3HdzvjkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=LVIK5BVOtlzrmWqG6Pd9wmOlSmxZn8hcADjGGr7eZZP1t3J19IKjeJWzthte60PMpRhHxVCUWvxp7paQRQBDNkeqd3ZkP3SLOv-GY8hv_epnW6ypXdCWYj8Eh4wYDllskCk9BMnzv5Js7uX5jn1xy4utbiHE6ZhxG8Kg4WDaeR80vPEXe7T7-qEoBHj1NIlCBm8cYWef47-qWHqpfbvp0Loy5hXAWxGN2eWmpiXe6J0XI_-vpD9KxImmgnL2slohxjG8a2Qhsq3A5FUtagKnAORUl4hyN6rVL14_bNRk1tyzDpzxVrR0EP0YWcdHRE236Y37ujn5GNVku2KWLPvE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=LVIK5BVOtlzrmWqG6Pd9wmOlSmxZn8hcADjGGr7eZZP1t3J19IKjeJWzthte60PMpRhHxVCUWvxp7paQRQBDNkeqd3ZkP3SLOv-GY8hv_epnW6ypXdCWYj8Eh4wYDllskCk9BMnzv5Js7uX5jn1xy4utbiHE6ZhxG8Kg4WDaeR80vPEXe7T7-qEoBHj1NIlCBm8cYWef47-qWHqpfbvp0Loy5hXAWxGN2eWmpiXe6J0XI_-vpD9KxImmgnL2slohxjG8a2Qhsq3A5FUtagKnAORUl4hyN6rVL14_bNRk1tyzDpzxVrR0EP0YWcdHRE236Y37ujn5GNVku2KWLPvE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIdEnwwKj4ic9S1uV_cVWU4lpJB_GnXaWfoHhacS0WR-lQp6EHYOgkN1AfzDNKpMw5fD9EtrzA221H3-kg25y0W7447KjYuigYWViPu-YigjdLCswO4yfQznPHaPYSWZKDBGGIrPPDaHIv-l-FHb4p-fDP0mTMop4OtspuUV0ilFTSLQb6vginGf0P5gHZq5ZPhFdjBwrf51moOwy1fVOzPHIMsGoTgkImyp7o3BstBcE07GUqIi2T7S0eMb8VB8kwxZkIyMQi_u1YQQGO5SQiPVnxzq1lbq1S5ePB40RwBeC86afBVKTJRQh89UmzzIF0xFctAegx8NsAYP1Ao2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=RaWgbDdWA4fRoPoHpm9OQ2_UWbXSk9eaI-WY2M_rTWfYZ1iDY0Xx7lO_IXkfO_4axnNUxXa8QhXCMbQnD0HCP3bKlVSY5aIJG1slpW1BCyA4UwgRbSl1VNpQaXQyD13CInR-h6rl8plCIexOwgBKHH8JbJOlariCo2tHKB7G6g-vIOgzT9cg8XViTgvYeww-To-s-iaBSzRRp-PfZBzYVugH8XLLc90ZowfTZjbtKVnJ5tR2MtLVXAOfyfPh4Uqne6FcJ7MMq2fGPoZvmBbQklkKKBuvCZ845wUGeEirXhNGaAuG32lwAgRgylRn-juLuaUnRRuDPgJ8RP3Qetq41jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=RaWgbDdWA4fRoPoHpm9OQ2_UWbXSk9eaI-WY2M_rTWfYZ1iDY0Xx7lO_IXkfO_4axnNUxXa8QhXCMbQnD0HCP3bKlVSY5aIJG1slpW1BCyA4UwgRbSl1VNpQaXQyD13CInR-h6rl8plCIexOwgBKHH8JbJOlariCo2tHKB7G6g-vIOgzT9cg8XViTgvYeww-To-s-iaBSzRRp-PfZBzYVugH8XLLc90ZowfTZjbtKVnJ5tR2MtLVXAOfyfPh4Uqne6FcJ7MMq2fGPoZvmBbQklkKKBuvCZ845wUGeEirXhNGaAuG32lwAgRgylRn-juLuaUnRRuDPgJ8RP3Qetq41jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mWZ3ASHjH9zKG-srISeoR-nqzvn5S4tTIXVrhVLljbJC8xHApwp1TO3OpqZ1FPDt1IrZr-Bhp4P-JiSGCurKuRwqwYyBuyuvO2pLrQAeWN_W3ar0KvToI9ZAJ2hiBwD2_5MKZX8QC5ivAD9do0tqjrRRyynEJ4tSG8oxksBTjwUO6-sQBAm3-ZUI3uGhzAkq2NpMdLubNM0_DnKRxOaATm1Y3KdchtFimmvVomSHzN9NdSCT7xhWY_L1tCdlB03ZCX--WboQBTu-9XFKG99RPnmdmt0Pex69Y-D75hSGqKhbn9j6IIGUweiVd8_FeIkIMMJ9BkY-WTk_NjAmHx1yLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mWZ3ASHjH9zKG-srISeoR-nqzvn5S4tTIXVrhVLljbJC8xHApwp1TO3OpqZ1FPDt1IrZr-Bhp4P-JiSGCurKuRwqwYyBuyuvO2pLrQAeWN_W3ar0KvToI9ZAJ2hiBwD2_5MKZX8QC5ivAD9do0tqjrRRyynEJ4tSG8oxksBTjwUO6-sQBAm3-ZUI3uGhzAkq2NpMdLubNM0_DnKRxOaATm1Y3KdchtFimmvVomSHzN9NdSCT7xhWY_L1tCdlB03ZCX--WboQBTu-9XFKG99RPnmdmt0Pex69Y-D75hSGqKhbn9j6IIGUweiVd8_FeIkIMMJ9BkY-WTk_NjAmHx1yLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aql5s_L6aPTLMoThKdIqsxexlFWuUVcjYs6cLnJzhehbLtMw7lm3udEfx7sT2E00ZfDR4AIQXqta3DGDm4fhZ-1Iwv2nvxNmjELOuQV_WNBcn2ozYA4Lia_rdV93sH4FGwz_012GWqZPGh5sZf9HtdK9aAsDLn23Jev8a8YvM87Oi64UhG_iq6Evxg310-Caeyyrc4qHn6kr-ZHR7yPPcc5_4-FxY_xRzkGbWZU97t15bcnUxzTKgkxl1BR4ObRBsLgy7ldfPaDVnolcjLB6RHQlZuBoL0HDaPKtPkjFTaWz1OH0EXMii-ZDwZBkG1ajO0FLIApuLXJvPOVSL9bRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qz485UYuDzX2QnzRf8rhj5DeAi8r_WC5Kl9znqhi4qQzNjZpacNxc_FmZ8P-LPqrpD4PaFdsl6tQFif_5iRLG1IYOya-TPQq9Bm5XQRS9fal5rkOs6AYwZu99SYdwgKCfRCBpSdF2GMVxJbRtcRA-Y5urlxXGJSQ1FS-Z0iV3Ju3W2_DQrEbQVohQsO8nQziBMMoZU__nCGBGfWjHRpsV4cao6WxmlXYk0NPdIe7oV2GnJ6Ig7w2zb-nXk4cGFOtsHXDU_2fjQogUltF5EohaEqEldwmHAz0u6S0jwbshHG_DHKyUVRr2EJSLzyAMVs6IKdJqbNyh-vM_Q2lGpFnfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dHrLEhp4Lh2_v54yMPAhMb-MYwSrD9IhNO6QPZ29ph7PVOg_jDrHIoLeOnwr5-Inobanw50TGNy-YikycB4IGpvnQFLI6hCIyHbAtlNNqyEzfy2azGs81pjmzC8gxU0HkOhfuFIuYiNcxNMXakhZdrZJGWkiJjOW2xLLXsTvoEFNzS4MQW6tXCN7XcI-AD7PsTS24Y_AwuiinlTGKufCl2QquuFitaxzh93yFzi_IB9ZAzHUoP9t9tQSeS37rzsUHeFFF_NojNMBPimTTeGfjwm039-eXSsvl2G6lztWBE3Z8R5XVQJC_NPvqJ0XyaInzzcGQoyA4PQ0_hdZhrxoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dHrLEhp4Lh2_v54yMPAhMb-MYwSrD9IhNO6QPZ29ph7PVOg_jDrHIoLeOnwr5-Inobanw50TGNy-YikycB4IGpvnQFLI6hCIyHbAtlNNqyEzfy2azGs81pjmzC8gxU0HkOhfuFIuYiNcxNMXakhZdrZJGWkiJjOW2xLLXsTvoEFNzS4MQW6tXCN7XcI-AD7PsTS24Y_AwuiinlTGKufCl2QquuFitaxzh93yFzi_IB9ZAzHUoP9t9tQSeS37rzsUHeFFF_NojNMBPimTTeGfjwm039-eXSsvl2G6lztWBE3Z8R5XVQJC_NPvqJ0XyaInzzcGQoyA4PQ0_hdZhrxoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPdqMGPy9c8ECjm-uuQK-Soj8-tSQAL_xixr1WpQMfjEsqQgj7rYy5KDXr5FoHXKqkmbc9bKrHfPUEqopRHpanEbaRThvADlxjSuauML3t3aUaWMd4EOS1rAQYk_YVu4JvbuD2emF3sPVgMkeWyDFSCDS6SRj8pak4j9XFM4IieL-gUCJkdmBx90hQ60Btnsxjq_57G7vINRaPBm2bB4_pgoNTA2Gcqe9HhTvcG4uyVD-XJQi1_n2js8_VD6LGTHGrjrbJtBSFUgzwUd2dC2Ow7zX-8SG76DJWyCQ1V_h-FENtDQihsRpdQw7teqLLJCCFw22xYHtLhWSwh45kTlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0dcuYIxiJo5WlUwWc8Kfowgp_8WmOWy_jhCgCEUDVZmFIIsg-j7PWkiksELMSHGk6FqYSig5pMhFIhqZMK8p8xf31wc1jlI3K_wpuXqJWJeTSClpl_i_Z2xO5jxC4ortEWw2VhHrKz8nzTMJa-mI0JPPq9Wt--HHSvmaf-oarJJ4v3Yk28fg-1KR32DraBK2rQL2E6a9LkYJN4WMbCwLhds1swdwM-dPNA6LwIFGRLLI_scwEpqbHWbLq45cxlXz5yABYkcDHesKDo-APNGhJhUIShtiDEmWirvqGUuHVlD2ya853Ev08o70Ai3btaFNbCYSm3eofgSjo_H631wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_2Y2vld8TGYU99Cj8YZSbaiLPl9I15PFz2K-ELVGfpRsOWnqpo4U-DIr1xBy9gkOE-I9DLEtUcXrP4-QBvhuMDYkZdvYBr_t8qJfSp0Ia0s-jXuiyzCtaheBHcguzqZPuKvyjdU6mChQPsMLQY82H0uGta4ZS2QPn6mx88tIX_-TgW3kI1aiH8OzBdngNFO3i-bI0di7Zj1ZcsGA6wJMG2UVc27tjODG8Y2mzAGdCtgpYX69tHlvdQagpbzVSKPLfPNpe2qj91Tdbj9kv2mnM3_FdKd8r_H4HHbv3FL3R4sdZNHSdIpn0kf7fX7fS_BeWfqEYgSWF4FYbJn9UUzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=jOuYKBtCT5GWL2qHboxVDBTS8nhwEjlNPobOGEBu8spoVlbEkqyk91smyxXA_VGulYcV7CzgHPauX-c4WdSmK7ggDOyaSeXOlYDP1v3-vSyRcYxq9kQsRIZRqp5Ls6wj0IdgVjT7SmM_I5shc5PUmcZ2m27f1kO2urIQS3XjSMT2nFX83tZdYJkkqaJNL3Rrg-JllBOR2c48eFHW8HY30AfSKFb7XpXGo2aYe3Ms0qcDw-d7UD56XAIQEvfoU8x1wyg6Rwy05oi9NAnLgo-TN5JvmqMr2YF8329nZqjtW5ZIqqeLM1FfuW_qR4czbOpSs7lBbCN82vIfGu7Du2tJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=jOuYKBtCT5GWL2qHboxVDBTS8nhwEjlNPobOGEBu8spoVlbEkqyk91smyxXA_VGulYcV7CzgHPauX-c4WdSmK7ggDOyaSeXOlYDP1v3-vSyRcYxq9kQsRIZRqp5Ls6wj0IdgVjT7SmM_I5shc5PUmcZ2m27f1kO2urIQS3XjSMT2nFX83tZdYJkkqaJNL3Rrg-JllBOR2c48eFHW8HY30AfSKFb7XpXGo2aYe3Ms0qcDw-d7UD56XAIQEvfoU8x1wyg6Rwy05oi9NAnLgo-TN5JvmqMr2YF8329nZqjtW5ZIqqeLM1FfuW_qR4czbOpSs7lBbCN82vIfGu7Du2tJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FfmeUPXgs_nsqTI8dYKWc8P-taMW5QHh0hYj0sftcK_7enXFR_OE2pyrOmY6Vb9ZUUb6YTSFEcYtNtJ0H7jNlXnFOzbiYV9rWqtGBSX4TKpmJHzSaxLzht0Y6F9k8RL7E3JaO2r2fPF4ZFHqUTdoz3XFLT685WVYgcpd9H2AUeYVdjr_iYxodSfAeHOMclI362xwPgPT7pW2byWtjniIQxjaXxqyw8t2_pXQ8WAeBeZFnrW_nfSUhJS5A5A74ganWhv5cqS6HHW_faDx3hzEUpy_Jf8dfqOwK64frUrdgkJZppvM-4-k61ldXU-YOhGcGUXIgOn63LnA84ymP2dJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FfmeUPXgs_nsqTI8dYKWc8P-taMW5QHh0hYj0sftcK_7enXFR_OE2pyrOmY6Vb9ZUUb6YTSFEcYtNtJ0H7jNlXnFOzbiYV9rWqtGBSX4TKpmJHzSaxLzht0Y6F9k8RL7E3JaO2r2fPF4ZFHqUTdoz3XFLT685WVYgcpd9H2AUeYVdjr_iYxodSfAeHOMclI362xwPgPT7pW2byWtjniIQxjaXxqyw8t2_pXQ8WAeBeZFnrW_nfSUhJS5A5A74ganWhv5cqS6HHW_faDx3hzEUpy_Jf8dfqOwK64frUrdgkJZppvM-4-k61ldXU-YOhGcGUXIgOn63LnA84ymP2dJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=QyEdQWZ-CcZ3otF49gZO5HpPddgE8olCPuBR8hJBUpKtWMyPLKPd6ieSNGrLzUHTxI8ZTTMgULEwc2Of90TemYJQKKprmog_ClqiFx15JfASVqfHoQKq8-6AQUFnG1zZaDOzfUIrCILKwEFSKjrwhFuE6nL2t4LeI6jbLHBp2YXA1iC5DHJ319mARdkm97lQBOD_4D0gF9BuIFeJOmbLkOVCOa4Du9fZKa05V_c32yuA6gD945YcfJa4Zvnr4V71MjKr81QWuCVnpZwjruEPEFAJ4O50IpAmDlOy8_IZ0000dj_-C6RkKSc7KS67UaBgKwmLWsbE0WYk0YrsKBPWX6S1w0J3PKFT6TsIUiXuiYAEagCxNWd9yBEITJETj4pImUf1-d0305MLpuCwpYFPaMjrvzVzImJZdCYX4ONiWT4djhZiYbhCdkvY_-szf25MejE6xDi7ztW6uR83DmCYM7_nzjeakEyBgzd6NrsKbmoN_K6mw4DyI2RrR8OdV2vzUoKsB5plUW2el1Fl7MY-TcsxqBlVEJZK4Nv_yW5cYUt_IgNwTTGgMpqsng5SWGfZ71cDyQDRkHVL91mUHjLjf9G5zvYsntLp9yKBkZgI9vxHPXxnmzeLBADRM12TyhemnHpV-myCOGFjyeP-Hr0JFjdx6_T5bKICjTr0EUgjbWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=QyEdQWZ-CcZ3otF49gZO5HpPddgE8olCPuBR8hJBUpKtWMyPLKPd6ieSNGrLzUHTxI8ZTTMgULEwc2Of90TemYJQKKprmog_ClqiFx15JfASVqfHoQKq8-6AQUFnG1zZaDOzfUIrCILKwEFSKjrwhFuE6nL2t4LeI6jbLHBp2YXA1iC5DHJ319mARdkm97lQBOD_4D0gF9BuIFeJOmbLkOVCOa4Du9fZKa05V_c32yuA6gD945YcfJa4Zvnr4V71MjKr81QWuCVnpZwjruEPEFAJ4O50IpAmDlOy8_IZ0000dj_-C6RkKSc7KS67UaBgKwmLWsbE0WYk0YrsKBPWX6S1w0J3PKFT6TsIUiXuiYAEagCxNWd9yBEITJETj4pImUf1-d0305MLpuCwpYFPaMjrvzVzImJZdCYX4ONiWT4djhZiYbhCdkvY_-szf25MejE6xDi7ztW6uR83DmCYM7_nzjeakEyBgzd6NrsKbmoN_K6mw4DyI2RrR8OdV2vzUoKsB5plUW2el1Fl7MY-TcsxqBlVEJZK4Nv_yW5cYUt_IgNwTTGgMpqsng5SWGfZ71cDyQDRkHVL91mUHjLjf9G5zvYsntLp9yKBkZgI9vxHPXxnmzeLBADRM12TyhemnHpV-myCOGFjyeP-Hr0JFjdx6_T5bKICjTr0EUgjbWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=o1Q1m7Vaefp79S9fhynVNotlK5D8Oy7wehrkEVsgd0Ede7clbdM5sHWvQo0chSL-hOEInxG1X76KeYZyMUvIpVE_RitYSuifgGcxf9yB_6kuvHD1iuVYPfBKP-UoWOFUCSiGlKiFKlkyZwno22SdnHC5BcaqPkj6O-wmmoJpOqLkTPICxaVBqL0Rz9CPhjXPtMQTJXKgPYWQh3mtubrLb5E6dDaqyIG9CcJSw7q7xxPL5HbWlsiPvRZq9ZZCqOmoA4LRQRHwCm1L1XtrTeW8JT2NidLEHYyyhir2Yo6-3BJIl4mPxacl2NAoUfi4IKTsQF4lI5OMa5TPhrNimY44KoMjuei0ugOrGXaGHJkKD_6lblvQLW68XmDNV_iBu58O2r2VpLzn8udEpaGjDZtvS5RpcjT_0xt_GfxqRmpEll-M2AbjR42LrggF0vPdG3fsT-EDoulsnTGKAbfv3wXWwqAdZS6bohJkMWoH9oXzSB007wFyqFSfPXxGjp23B9uClzNulJCPZs-gJOKrnxUxL2xh-0MVQq_IaZmZx7yPOWiKgcZxdRTb7DLSR118vc5BcXDd2YI9SC95-VVwH7oGSULkQ7qcfIzi2HJrtY_vdiCHbZPNV7iyJAY9KTqQT9rV8xO0nONcJfX4e5gjhXn1tLxdGIEzFKfEQ-WE_x9ugdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=o1Q1m7Vaefp79S9fhynVNotlK5D8Oy7wehrkEVsgd0Ede7clbdM5sHWvQo0chSL-hOEInxG1X76KeYZyMUvIpVE_RitYSuifgGcxf9yB_6kuvHD1iuVYPfBKP-UoWOFUCSiGlKiFKlkyZwno22SdnHC5BcaqPkj6O-wmmoJpOqLkTPICxaVBqL0Rz9CPhjXPtMQTJXKgPYWQh3mtubrLb5E6dDaqyIG9CcJSw7q7xxPL5HbWlsiPvRZq9ZZCqOmoA4LRQRHwCm1L1XtrTeW8JT2NidLEHYyyhir2Yo6-3BJIl4mPxacl2NAoUfi4IKTsQF4lI5OMa5TPhrNimY44KoMjuei0ugOrGXaGHJkKD_6lblvQLW68XmDNV_iBu58O2r2VpLzn8udEpaGjDZtvS5RpcjT_0xt_GfxqRmpEll-M2AbjR42LrggF0vPdG3fsT-EDoulsnTGKAbfv3wXWwqAdZS6bohJkMWoH9oXzSB007wFyqFSfPXxGjp23B9uClzNulJCPZs-gJOKrnxUxL2xh-0MVQq_IaZmZx7yPOWiKgcZxdRTb7DLSR118vc5BcXDd2YI9SC95-VVwH7oGSULkQ7qcfIzi2HJrtY_vdiCHbZPNV7iyJAY9KTqQT9rV8xO0nONcJfX4e5gjhXn1tLxdGIEzFKfEQ-WE_x9ugdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=N8Qr0t-iX4T_gKn0nvNuZBZg4BuShaISqGp3braWEHRHAnWDtIwB3nVXs9oOKHE3dIYb59cgZv8DBMqvoEn_pObr8eqsZMEYVHQWKYXoKpxCoeh6h4Ly7t3I5ASP7YTgbrl_6yV_TF0l3yAJq9tG6kin70ngNLT7-0Ukt0ie7jqhNLP69YiJt5sBAH9xReUbHCVbQ5Lt0hNUirHfY745c81kDOWtIsV0ds8hmzZR6k8O6jO5lb46paH3xXmCMCN5wIIrM_HuFvr0703bLtxMUR4ar6NBR6OlYcr0q5yoo5JawkUC6z8bBM2TCWHVuDZKbJDrVQMfV5dSXxufA2cqTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=N8Qr0t-iX4T_gKn0nvNuZBZg4BuShaISqGp3braWEHRHAnWDtIwB3nVXs9oOKHE3dIYb59cgZv8DBMqvoEn_pObr8eqsZMEYVHQWKYXoKpxCoeh6h4Ly7t3I5ASP7YTgbrl_6yV_TF0l3yAJq9tG6kin70ngNLT7-0Ukt0ie7jqhNLP69YiJt5sBAH9xReUbHCVbQ5Lt0hNUirHfY745c81kDOWtIsV0ds8hmzZR6k8O6jO5lb46paH3xXmCMCN5wIIrM_HuFvr0703bLtxMUR4ar6NBR6OlYcr0q5yoo5JawkUC6z8bBM2TCWHVuDZKbJDrVQMfV5dSXxufA2cqTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cid35weMMpyavZELII1daRCuECF1KZSGu9uEWXizJvbZKumpDeAg2Khoc4C39Xcgw3E36MFv8xmhrCqxBizY0WESX6GeinM95jHH74h6UwVOE6tNJRpjwUPm3UStgXF9XhWXS4alWpd7XG2DFiYymwBMMjySrbKlL0hU0DoOlX_pu2h6CEBNaf67Q-wtCenwtdP0GiJQfHfh7PGNTlHhfbzbyVZadov2bzcpMQhD8ez8He4bIVQD5mfSkKtZrAXf8U9huU4LvJGi07jwC0SUE1siden85N-nM8nKmQloFrR7aXbTYyK353QutTQbcrLCVLm5vPko7DTuLNunfK42YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Rnin9z1YKkrvYFiB9x1FNf10O0UdK9UjA9sLf_SbzzOib-2SIxXgScT25k_bXGAS2VsDvcwUh0gyZ48Ne1mgbMYPy9ImZ4cPWWOxynO63jd7yNI7UjqizdMTP1DtY8D42VM9vl3Ku62YEDFRLT3Kw5VW2X5Tsuv2nv5ZMTLkGJ66RBZWzq--RA-I9mndS427s3ss71Kc97M-9KwTw7n2bGcIFwifC2DttA3DtmCeajlrtraNZHWyJx2HQdSQfGCaiRN8oqtG_SLSJtQbQwJYgjoPIZwzum1KjAiudRmbDXGdvV3Qp1KfRY9OuZ1W1kSh_kwrJyvpT8f0VLWSkBqP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Rnin9z1YKkrvYFiB9x1FNf10O0UdK9UjA9sLf_SbzzOib-2SIxXgScT25k_bXGAS2VsDvcwUh0gyZ48Ne1mgbMYPy9ImZ4cPWWOxynO63jd7yNI7UjqizdMTP1DtY8D42VM9vl3Ku62YEDFRLT3Kw5VW2X5Tsuv2nv5ZMTLkGJ66RBZWzq--RA-I9mndS427s3ss71Kc97M-9KwTw7n2bGcIFwifC2DttA3DtmCeajlrtraNZHWyJx2HQdSQfGCaiRN8oqtG_SLSJtQbQwJYgjoPIZwzum1KjAiudRmbDXGdvV3Qp1KfRY9OuZ1W1kSh_kwrJyvpT8f0VLWSkBqP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E1Ihley382V6Nu2fQgqRy3j0xSMy4ta0PQ-2UcPmgDTJDaacm8qj5c6j2XE1YS-x3Hr9rASKawMRC-bjBTbTiGiIssJxMFqdeBfmFYemb6LrEJs5jrTFZvwKgk6OuuhaIoAQirQu9WCHOAOc1U9oTA6hvs-6naCR9rr881AzvPuJQiQ7_wLIm37LJcQXK0HkZ50evR-8ZXAxamT4D1Cfi6qBWWMVvIOdqyWcpqPrX24Jm4aEhzktVzrt8iPAhFbCDxTHBoN93euGs05hriyHnE4qijnb4qU64ukVSzdkRszjfdl0eyxuWPrDg9_b6BqWFwLSlpKy73CJdByaqE-fEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E1Ihley382V6Nu2fQgqRy3j0xSMy4ta0PQ-2UcPmgDTJDaacm8qj5c6j2XE1YS-x3Hr9rASKawMRC-bjBTbTiGiIssJxMFqdeBfmFYemb6LrEJs5jrTFZvwKgk6OuuhaIoAQirQu9WCHOAOc1U9oTA6hvs-6naCR9rr881AzvPuJQiQ7_wLIm37LJcQXK0HkZ50evR-8ZXAxamT4D1Cfi6qBWWMVvIOdqyWcpqPrX24Jm4aEhzktVzrt8iPAhFbCDxTHBoN93euGs05hriyHnE4qijnb4qU64ukVSzdkRszjfdl0eyxuWPrDg9_b6BqWFwLSlpKy73CJdByaqE-fEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKmk5WfvFjriSD8gZ9aefQmPQ5_mshxt5oTFffsIYIyHLQrewc-t-YgPvRPjhkf-kf1q-MOOmOrS91wF-pxBvllKyQulzSKWRlq006TXIlq5Iu3STuSA7UO69RaNiqThpYbHIx3HsdMeBfMo67Ey-tFAQIO6gmXJlvFt-u4A-SaUThc95dFbjdgXoUvaWViur9XT7o036wigPemT_LjEKi6jT0WzGwly3gl4LMjqOUGRGgLT5OjjJ-y16HQ8YwC6j4OJm6EiHsALZ3MKCK13k7uklfVIC-GTlX6uRX3Z8d39sJNG2lc0brMEDFwQ5VvPMwfWAm5g2GrTDAZXEpYpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNsmbLT7DYStClgwDRxZ0QKFTN05euakOPseQbZS4RU75POGGRnCg_Kug84M0wA6xMduGXYQ7k8uDEGOiGnR2AP_EBQnUu2FNOdt8s7ogJDFdOKHF2PoKptb8JVJAe-cRGdLE8xcrOoAlI6MCKh47zagyrTZdI7VqK9JmdB-OLwdRF8qdzl8s-sQpGj8LvUE9BVz8B0PJmfWIZsXmw1mxllGBpIxeLwsd5OnsK2zZl33rNpno2S5FYVz75AhHmR1hnKv7peuarAUEyHslP5eT_-Sfzj97M-A7GpmXkWNV1OvBbFmAlkqWpoFOaE_VrwyuawsbKj0aWvlSxnklFS2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOiDPNd6zaKRDMztDmGwH4rYxrvPAVPVwSt3meDQeCV95wsG0sdMowazL1AqO7wkaoAfJppKlzCWjYYV5hh8T_1f9OCWGTm2CKxDi__-Si3aDFfmITE0BR3pdsgayF0COPorN7L_IP_YSXg0posGnCj8LF-EhFMGl3jahmY0X9H0kHJbjSxOTihEgzURBKsSjgXQjBQ593SlCPt9FkxSehhC5z4cm2KDWY0x2jGnc3IQKWkvq0oBzPJXuQ9hUB3mIEw1fg0_xPLFWdkmQR4wiqkaiX0pvXMCgRdGt2atLFwnLLuqve6g9U9kzSavAmaKsFBidDXDwEdyKw8VLaBwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgojbhsFDUvHnJnCTBTKpQpQ1BXkGTd18kAqBaigpYdzEYWfOfliFTz1sHayf3tM_frtWk9rQ_lgOUrNHwEvIXptwV-rHDgKPzzlXs9XXDAkpwe2CJQgq3IDDQRu0_pcJje09S0QU7xzO_8R9IdBkpRZRihtMFGRQPzX2fRZJbiPMFWOXCRecDcrWCMBZB01lNxCw9YJAIrbR0Y_PdiS-PtGjUVIu4wkQhRJG3KaQMb_pAANQWtw3Dhdq50GChFtRDHPJE_zdVb6nf6Y51z3lAmnIWcq4FJqxGT9qyqt0PmnkVeY0mjMtnFTGjm9FTcGrDtuPPHM8DOh3VkEJ4YkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb3_v9Nbj2Dtse6sEPE_a8_RhMg_N0Is7LMfI6bdvUdghS6wyKngGLP5ipsqdhU8iFABXtfL8Ex7iARUT3lilyzlLhdioy7iDXpu9ZLXoXpCJhNwc1lhCRiCuM1osTdGbC31z7hjSXVq0VKxRy0iaBxPFu14ukDih9CsEC0WCrUjCBzJY-_Tlwvh3niGiDuayMRY1-yuWlO6T7QjWmupapvQhUCpdgdSbl6wZF1eioxw3mjazHnve2hPCiIxQp9woGw_FcZuWlM9lsVqWjXZ6LqYtb2Hk2K40iIlpH-PHFkGSzXOLVLf7k1pq2n9L8jsuDv50ZxrhDB86uqcIfgD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN6a1x_kJBShP2XCM75lLUbmZjawJprnr5jc2OvN7tXzrPIgcypTshnsGWm7ujfk-4KGW5PZDrJT-VOQZlHXMpaDC1Fma3sivFuvvQyIZKdUBn3ocJ6yqecKJiEHWPr3rJchCRmfNbEVI0uTl8rZT2TkD2DFXxHBq4qr0eOjwUiEdM5Gl1PajDh5dPvnZ57cTZhK-kuadOsQUeJg2_fw8fxgChpkojpEHl4ah2Qx6lGrP9shPX19-VbFfg_Sz1H2DS22VH5hIDw0wiVZ5mVl8lGFU_AAN7MO-QuYCre49ftKZtXI-V5OYEw1gNOkqhkzApCBzakADJOywh488EsGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKQdV6xAAmsjyIjpc9_6ezXFKiTMhm_U2kLdMlfFHtI_SPrGLHSb4ojhetmgWnZkBtQmogOTY8AcOXFP82QlS9oUPs9GmeYQcP2wffRaHY6YxAnU5rFNv5e4aK3xzYTD1op-FYtehVcxQPq_G9-LqB20_2MM9TSX6RPxb5ViL7ZES7cY8XWKW8KwVqaIgYPyJkPEpvjvn5344Jc-zYXw7K2n6RijfJ3wyzCIhy5bZMQlBL-pzRRxd73zk4AbxcyCG9HRpjKR2Rb-xUpzFvv-LwvevPUYzIYlO65vw-1b0DZFCicg0718UQRJXQkqvrVmRmcarQEdeBRtEGVP51VKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hr2tGtQFAxBMO1MmXCHuwYbu1QAPh7rJMV1ZNOeqLChrL4ply92TpNK0WXDk2n_ihuOAAkaBz0kLhYMQgRbPG4I0w9FcLZ_X3NDiyjmEfFJUQ1Kf-7RsnKZjniAp4lO3oz51Hy0pADlicGCThd7TBvWogOvJZMFqk3PhAwbnnriEq0cF0Kdzf_WBm5oS7mWIab-Gnr9zoX-dhJscfURKED5ROIHe5V8O8s9S7a8CB8wQPXO-YX8agiH_LLG-RNYWKc4mi8V9uewyBAm3YC4NnCR4KoB8pyNwU9OwA6AM7CJl3l18mkv_eNu7AnwGj4ENUsDkxM-5JX0rhxz73d5FKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbZ0ijJqMuvGCYzZwYdakAdPw5yCTC2KBd2FW_-Za-l03NiiesbPMGW9Dt0DtBd7kotpECcMT6o5vmzWydnrgUnGpjs-vT09LeUXFvteVVTfS56wE68_R0whGrlieH7VUEFkp5snbaaQLF7PFmwlEn1tzfNCJw-UGt9_fK2-xqYcmrbZEJl_LDZE_ITZ6ypx1FIjnWTasxUqw6Xr8Uh1OUgDOGlccPf_FcHVxgTLFZfh0ioVp5kxLVnm0TwzKs7YlWU3drbRLE7gK1r8mRJaVYZ1nSi4Q4hCIdhtUKTS3Gje-n-FjuPip6LJLDamAOts_GdU8BEu-s9pTtx_QFKxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCDF1CCexKMG8NZZMRWIcsvHbSYlhIWt_oKtYzRNHT9pyVL66VU_ZMviFssGB3ngYn82E5bLxoLzh9tIgx7nzkcpg1AC4mO72PN_6fuNqdoasXCsHRaFrc6xJLh7_NK62r-tZtLk-i-wSyvxXjnDpHAjyxLCO1CxvSDkL4eAFv8oqBPJjPhPdAPG4KHeOu0km7LJZ4Z1TyBuHHk7iAeT3ttsyznvuWqDIkI093NNV9Y2S0tHQjf-ovZtQdNiZpmhuMMXykbvWdc530ccdSvqfUVW1C1_i5Y0z7EdET-z7CiwcKyD8sr7wp32DN6QFd6Kqvfy2vnN2ny-giNWIwi-gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
