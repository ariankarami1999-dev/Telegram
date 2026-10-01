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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u47RjGutzISdVwJwkmb8-d0S-QEAEpI--UQUJ8s0L3gMfJpc7qBlK4nZBDRl8Oy1ubwlR_f9vB--huX-YRAqZLhGrKvB3Wk207kw0hNipE14njVmZr4R1lRvS1kCLGZPoOxuxCXI_aVTIqeHrvrVSCn6Nj23cyJeiKg5KPIVVOhCcVZ0KBgk-b8BjrYbKLfbsKh1X9aYbDBG1gwrUJWNvPDhy7nhWcCOyTQBG9nedSRyPDUU1a8bb6eXp2kBD_gCxoBIFohg1K2_JAbbg6KyGnJ5KiEEkm6Fg7mC5RURH2H1zWZDCaaOcrVU_9EES3wVPWDNEXnk6poJgFY4UNufMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u47RjGutzISdVwJwkmb8-d0S-QEAEpI--UQUJ8s0L3gMfJpc7qBlK4nZBDRl8Oy1ubwlR_f9vB--huX-YRAqZLhGrKvB3Wk207kw0hNipE14njVmZr4R1lRvS1kCLGZPoOxuxCXI_aVTIqeHrvrVSCn6Nj23cyJeiKg5KPIVVOhCcVZ0KBgk-b8BjrYbKLfbsKh1X9aYbDBG1gwrUJWNvPDhy7nhWcCOyTQBG9nedSRyPDUU1a8bb6eXp2kBD_gCxoBIFohg1K2_JAbbg6KyGnJ5KiEEkm6Fg7mC5RURH2H1zWZDCaaOcrVU_9EES3wVPWDNEXnk6poJgFY4UNufMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxwKw9u1wKVi0le3sqPFXJ3CxsF1knfLf6mNDFc0QMEfDEnyoTWDWIcxmug7nrVAoG0YilGx548apFZ-Zj41EHFoTSW35j3jTyHyHTh_TShFp_IrNO7oqMxOgnInCivZqCMVJj2JHL71X9Q2ZN0n2NAyZwl7Yg-dFW9zpebWRNciy9cHlGdkVfrDgFVNRa0eCqk0QNhJxmA2TgITHvL9zof5OHPL4HglFUgbeNJIifrwDbPu38jqHL6PVnnJIwEw9yOCZIqhJCxLgLKIH0lBRgXa6naMBzoTF2dddu0otKs7BgQR8GS6Y2Lp6v18q3ExCve41eW8y9yXUgz8payoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUCuLTF1ky5S1NKzLdt_8yhlFL-NCcTGTXzgzJ3fcAixrdQg0rUx_lGX4bsFubvcH3SLVaVJdEZUWSlMMr4-Zs16H3pPQZKdR8f69tAkrfrKKY1liSkJheJdILvZikinRbQ3sKI1x49zcE8U2klM-yMtkXdLfEkwUxB4lW4zUMhDXT2K2xJNXd6T5P81U_yaBvQyv4lX72N3KL49jJJTLTmvi9iVyzw3Iprwi3TJs16OOQqPe7xbyZ3_TFz3sIOhgmPlTeiusCxbs5SvXFd9lRZsvzbjQr21t8jHG3OQN1ICWVfdO0ztNq77YBY7QJiLlQugJvMtvlBe9FAknLNUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYOevLWCoTMtE5K8XzPY7LPgpiL915mzOLv9pUmpaBF0eoFwiFNUtpQFeHNJhx0z4UF3oTRjlFoR4-xfXVTXpQ6pe9L6r9zWm7eADOAPKu820f86_Hwm-kwve23d6CJux-Zr4dA4gbMO-ZPEZdKQUM_2G8KB3Fr542qoa5sj2PRzFc6w7rldSl-9Nite74LWzPrKqc7Ose--4x468eULgKvxc0IGHZ6hCRPImSiJWiPP-uohp4BVQxqk3kYcWIbs9pB5u3ot3SdbPiE651t69sI78ouUA9UUanHTkgTaK9QGCvPBKjqW5JoLNEnQaNlcQMBCwBIx1jAcPQ6DbydTvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=B2tHj07MxDvFQcTVft9a5zpxqPypwRpd91L3VBEcsF9zn3vU3Vd7vKgJF5PCWjr-mBVQOGHwiF17ua_7PopPQw0BvRwPeM_36iAexAUihXX1m2JhspHvPGXiWYtPI6hi2nNEkznOAReJ7EUTlceavdhpZLuxoAhrX8IGjVjrTI6sW-Png6XbuyK2OWu7EjQ61v22neawTit3YOSyTCqe4r6q4r8OEsboOcXyTrJvd9zUgNAG6UoLZPz5jH5zzpgR9aiidNimtiOz-Zkxfo1T9krcGOln8fvQF-vDj-3i40ZpDL567hD8Z4Yu9WSXZn8Je1YyROLagH9pzT5qp1oEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=B2tHj07MxDvFQcTVft9a5zpxqPypwRpd91L3VBEcsF9zn3vU3Vd7vKgJF5PCWjr-mBVQOGHwiF17ua_7PopPQw0BvRwPeM_36iAexAUihXX1m2JhspHvPGXiWYtPI6hi2nNEkznOAReJ7EUTlceavdhpZLuxoAhrX8IGjVjrTI6sW-Png6XbuyK2OWu7EjQ61v22neawTit3YOSyTCqe4r6q4r8OEsboOcXyTrJvd9zUgNAG6UoLZPz5jH5zzpgR9aiidNimtiOz-Zkxfo1T9krcGOln8fvQF-vDj-3i40ZpDL567hD8Z4Yu9WSXZn8Je1YyROLagH9pzT5qp1oEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDXZGP56DfcskABrCZq7mOK9f1Fbr2DhwliEJyti2rKVQjkl6Nt3p1SvMwwZ5_xs2wpp_VilU7WnbOPScApLX10QQAlqDbmlRGjYB493khkmsPK5chlrV2RX7C5_VnNIShHt7ERiWL6sRtcLzjfWfgX8qndILJQJGRyJz9z3hWkccSEWQHkHMIOjDLeGZ7rO-yG8XQbs5UNYeD200ElRzYZNH3iIqK3T_Ud9mviZr1u5FiEYgZSULuA0hdVs9G-sc1-J-xWIAYe_0wqz9WmhXOIqmU2ZuwYshTpn4MHhHMFeQzmd4HTRrYY_ju9dDoBU52b3MFIFn3O3GfsP1iGnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDXZGP56DfcskABrCZq7mOK9f1Fbr2DhwliEJyti2rKVQjkl6Nt3p1SvMwwZ5_xs2wpp_VilU7WnbOPScApLX10QQAlqDbmlRGjYB493khkmsPK5chlrV2RX7C5_VnNIShHt7ERiWL6sRtcLzjfWfgX8qndILJQJGRyJz9z3hWkccSEWQHkHMIOjDLeGZ7rO-yG8XQbs5UNYeD200ElRzYZNH3iIqK3T_Ud9mviZr1u5FiEYgZSULuA0hdVs9G-sc1-J-xWIAYe_0wqz9WmhXOIqmU2ZuwYshTpn4MHhHMFeQzmd4HTRrYY_ju9dDoBU52b3MFIFn3O3GfsP1iGnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RklkcfQFscNLvTRMtxfQDpX7HmsafMqDKZaOfl3bPp-2rEagjGovguMYT_RRgjX923HhxgveBTaPjtkafB54pI0XFnNvILVekEBd6T7bC6_iPFAG0X-N3IQN-8vjtcaMOZ1pC-yUgeodJozJGCxUZE6iq1-Y2sSdqwaliYu1sEXEu2-mFNKQnynOZYujDL5sLol7-JBT9iFUhRFmeHdJ0ROXN1YWLVUD1LjN_zNHWAltrvqyo2OXehiRoYkzguWuOahwbWVYBvrrrQQGoZ4s40BluHBkvrg6vf1-5_LGQ3vwvAS-IyzVdLUEOgAHgxLmv9xBRTxCOUafAetxsjk6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UFsQ0OidagncQGlC4OPq6L11xfzpgz9Oo1rX1jGNtMIjCH8_iV0CNaa4bs6NpEil7JscZ2gV0USWA7utwRgg_INg7HNaoA63qh4CYTIWhczAdFuWcHZhtHMinKZlZ328ifesveeORwWwv_NyTR0JSTm7n_qnvsyOldWY2C8pFyZ2tXsTOu2RH3rxqLisaI3kTQWYdwR1xfuZ9pNKF57UXNmrfvrhNmhQhx-rMAuJbnkOCgp6l5jvh7syy5jxfuzwp_uEtEbMCaJv8NUlFAyd6SkIRJ6jfJtjNcNgFDKi7-j5gq_e1Dx7U9urvUi5wJRQE_kWbpwTDp1qrec6vnARJ6OpqXTgUVj10LYQrwC8P7eGsX7YFONk7btopTvKwYq-hhraSvE_fmsbMT7QCjf0g1Z3FklkWsDSzOy5O4DNx07yn-XW8t5zlE0UxIvLh0xQIE-q3AVRlpSyComgCDAFDQWr8cN7-jSuNHFP8nXFSnUJPYB3Apd0z0shk5XjTjAe_SobLME3Eq25kr9GsMWxKoZRGBHMzBFYYVlchI1Cq0He_NYxWri-L72L2u-RLa0POxpr8kOIXkuQhckAyVCBvABVl5l3NHsfQVwVpV-l4MuRNgLeSJnd02-kZk7Hlh0bacXBX0ICsiqZNlea9MehYhdGJrL-Y4GfU_JIUkaglXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UFsQ0OidagncQGlC4OPq6L11xfzpgz9Oo1rX1jGNtMIjCH8_iV0CNaa4bs6NpEil7JscZ2gV0USWA7utwRgg_INg7HNaoA63qh4CYTIWhczAdFuWcHZhtHMinKZlZ328ifesveeORwWwv_NyTR0JSTm7n_qnvsyOldWY2C8pFyZ2tXsTOu2RH3rxqLisaI3kTQWYdwR1xfuZ9pNKF57UXNmrfvrhNmhQhx-rMAuJbnkOCgp6l5jvh7syy5jxfuzwp_uEtEbMCaJv8NUlFAyd6SkIRJ6jfJtjNcNgFDKi7-j5gq_e1Dx7U9urvUi5wJRQE_kWbpwTDp1qrec6vnARJ6OpqXTgUVj10LYQrwC8P7eGsX7YFONk7btopTvKwYq-hhraSvE_fmsbMT7QCjf0g1Z3FklkWsDSzOy5O4DNx07yn-XW8t5zlE0UxIvLh0xQIE-q3AVRlpSyComgCDAFDQWr8cN7-jSuNHFP8nXFSnUJPYB3Apd0z0shk5XjTjAe_SobLME3Eq25kr9GsMWxKoZRGBHMzBFYYVlchI1Cq0He_NYxWri-L72L2u-RLa0POxpr8kOIXkuQhckAyVCBvABVl5l3NHsfQVwVpV-l4MuRNgLeSJnd02-kZk7Hlh0bacXBX0ICsiqZNlea9MehYhdGJrL-Y4GfU_JIUkaglXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DtKrZAywixEMLCnVJ3jQRmHpfzXn57OA4ayiQmfbW-1m58Ac6U1N6CbMEGksTxKTL_IaxeiCYRs2OMh-j_NG2TwrosmyyJwImoCAzw6K4akwlFivZHJAyhmUssq8Rsqg8ajTnwlviuEwBYmydvL28YfxQvaFmmAkAiR2SGi61KhrUFLGf59Z99arqlzu9w_utpOGzJwfTp427ehprk5n8e-WpxC9D-z8tRvuRGnPpURkg8ohdxdF1z3d8vyM2u6rkf8DhexAz1zk4eMppbAT7uNHT7hvTPckBJdInlq5wP-7MIbz5XwrAmHfCMlCtk0wjDpV6SMx9vfTplLSx7RaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DtKrZAywixEMLCnVJ3jQRmHpfzXn57OA4ayiQmfbW-1m58Ac6U1N6CbMEGksTxKTL_IaxeiCYRs2OMh-j_NG2TwrosmyyJwImoCAzw6K4akwlFivZHJAyhmUssq8Rsqg8ajTnwlviuEwBYmydvL28YfxQvaFmmAkAiR2SGi61KhrUFLGf59Z99arqlzu9w_utpOGzJwfTp427ehprk5n8e-WpxC9D-z8tRvuRGnPpURkg8ohdxdF1z3d8vyM2u6rkf8DhexAz1zk4eMppbAT7uNHT7hvTPckBJdInlq5wP-7MIbz5XwrAmHfCMlCtk0wjDpV6SMx9vfTplLSx7RaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHNpc1P7GHBgG0nR2QHt7CKmyP9kp7vcmaTBoBcitY0Q2eMs_r6h54kueQTGgGl2RdQVJtRGsymQDCqqllc1HMcnYvX8N-j7922cVI8BQnBaAC16In49N_cA1M9QGPHM2ahSWYLdbWbnFDRW_oi-GN_VY-clsUWo-563-8cEO021zePcygMqm7t485lmiI9oWyQ3caQsyC-a6AM5ot1boDYaqmonmgibTgU_RreaqjWy9VVd65R9MjU11UX1LUmkUGYCpDP9iP_QHK8LTkn0giBvwEADwbQvo1nxBE_jW68fatjS8ygovF0syXRga6irbqS4tFSOGZdldJqv0vHUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SjIdX94_OXXl_08uvTHqLo95Uii97JdR06J-0xwghAQ8_TYM2t_fGQx8Q3z7SzzkLj5huKW_7ySszX0EUZSRrIIfVy1aVEeHS5d5Kl3nLNvIM1l5MzzDdKCV2HCxG23A9-rcnJJ0baFLYKz4tIxARnRMKLodkc3eLREcdX_LNS0a0zs5wbsLBuy3T7f8dy7uI23e6CMtFGKD2hrQedrJmN4z4waK_l74LzFStF6xOeQWhfYB3o9-JkB29IhJuQqu7H22Ja7rUCN6QAFjqwQAq_sJ7kuppr8lp9cUdd4eo6kocsYw9-dzwkQ8LlBdHHDY-O4wMetMQDYNrTtCMfoYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SjIdX94_OXXl_08uvTHqLo95Uii97JdR06J-0xwghAQ8_TYM2t_fGQx8Q3z7SzzkLj5huKW_7ySszX0EUZSRrIIfVy1aVEeHS5d5Kl3nLNvIM1l5MzzDdKCV2HCxG23A9-rcnJJ0baFLYKz4tIxARnRMKLodkc3eLREcdX_LNS0a0zs5wbsLBuy3T7f8dy7uI23e6CMtFGKD2hrQedrJmN4z4waK_l74LzFStF6xOeQWhfYB3o9-JkB29IhJuQqu7H22Ja7rUCN6QAFjqwQAq_sJ7kuppr8lp9cUdd4eo6kocsYw9-dzwkQ8LlBdHHDY-O4wMetMQDYNrTtCMfoYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRPQv5xDhns-4YvXiy0gr8mJ7MKvVdGzc8IOMEWkaSlQgqXU7aImd1l5XNAWoH2ynQYB4ouWN_p_wOtiPrs2-wCpEnNhDGYHSjYKoTX9j3qWINOzZNJtA9jhxx6sXzsrhzLz7ybjv_ZXgnHQC4ByE_PSLSjfyQyMCBEFC0O-BEotzyFFW2aCeOiB9zJTe2tmii2fk9Bla6ejvjIvYgAYbnb8LA9X4zIp2FsMfKXSnRUS-2q0lr6LqoR_JIaEuec8jIyFC1t6oENLqv_6KdOijultHywpk7OYiNO_kMH78vcMQl7zdyS_8HVZnDKXQg6cdlcolc3s8HX1Xt84O_oWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMql1NspM8lT3550nkb1cNNloGu4N65KYsrQWHarKwNB0YPC9Hcp0vckjnOskQsgW4omdHPEtvbRpiLErxPxSAxr6s1z9O0E6Xj0UDgvGsYTfFNstRDeRYkQ3VIS7O2o9QKbD6f1hK-HhbjCUQ6VfWDTmaDFxVxHIWUTsNFLqRoS1qhaYu_Dao0-YKfFNtvlf8kCgaBuu5Naxvl2mG2TZP2OyZb7siUAFj33-5e_xIQ4uYS8IidLSpH9K2_96SnwLGqqU2oMobcQdcNPE3KygEaLTVF675LfcIC-iHkDFu_BlS7BCdYUA9EeRRy6YZ9SlHBfTzpNcTnu3ztpNyaY3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tB6nNWVhVZDDPG705m2_pW-qoDIoXnIpVvbGW62eDvw409A3zwiPmzyj3AZOVOk3gFRzgNP7fcee69QAmd7gY2dHKFO7OyTOByZHYks6sXWtwMFubicDn8kKVg30CvgEHEBiKnOYh3JloswoaQWPJsTxE4sZ96cWrV89kTD_p85aOwF6FuYkdKzrXXY7TXRYRWNpB4k0ucpWct5xtnDOCE7ljN5uBW1WrMCnIyZANlqQ4DiAIrRqTD5WvmhwY991WPOTKV_hdfQwD-2GxDklRL_jb3ZAq9z6N9M4Ex0dT2L-JLxGV2dC06ftECw4CWA6_39LlguX22hsN50pGzbJ4AmExEDhooDONpFB3XTFmau26A9R84gFHrc4_lDgZOnaN1O9mMN3zMJKFCoXko8SBAQChB-1OGiVoysQzx71jhHCd_7kx2yS-xd2onREG2fNFEcCKnIi4WKulj-a98K-Mq01hcRztO1O_MZ4OlLwJz5qwRxG1S0VU4ds2wIF-FtX05tRxvL7btEeT8J4KlI4oLyE5MRUYluYxNRq8vMEmYdvgG-LvhdHHDtU7YPStNIW90invmpYCKgWFQTym4x3jnl8IUi30ufCSekYAiMA1t4NZ8hTTGaqS-DidJKaegvXDqAcu4YYyfKJ8_VnrlAdXjp6iXSSW6S1GZ4wvyYqvK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tB6nNWVhVZDDPG705m2_pW-qoDIoXnIpVvbGW62eDvw409A3zwiPmzyj3AZOVOk3gFRzgNP7fcee69QAmd7gY2dHKFO7OyTOByZHYks6sXWtwMFubicDn8kKVg30CvgEHEBiKnOYh3JloswoaQWPJsTxE4sZ96cWrV89kTD_p85aOwF6FuYkdKzrXXY7TXRYRWNpB4k0ucpWct5xtnDOCE7ljN5uBW1WrMCnIyZANlqQ4DiAIrRqTD5WvmhwY991WPOTKV_hdfQwD-2GxDklRL_jb3ZAq9z6N9M4Ex0dT2L-JLxGV2dC06ftECw4CWA6_39LlguX22hsN50pGzbJ4AmExEDhooDONpFB3XTFmau26A9R84gFHrc4_lDgZOnaN1O9mMN3zMJKFCoXko8SBAQChB-1OGiVoysQzx71jhHCd_7kx2yS-xd2onREG2fNFEcCKnIi4WKulj-a98K-Mq01hcRztO1O_MZ4OlLwJz5qwRxG1S0VU4ds2wIF-FtX05tRxvL7btEeT8J4KlI4oLyE5MRUYluYxNRq8vMEmYdvgG-LvhdHHDtU7YPStNIW90invmpYCKgWFQTym4x3jnl8IUi30ufCSekYAiMA1t4NZ8hTTGaqS-DidJKaegvXDqAcu4YYyfKJ8_VnrlAdXjp6iXSSW6S1GZ4wvyYqvK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R8tUScCWPOPvrQaRZGjbpzyukmBLar765CvbSadmOmX6k4Wcmjd2J_vC5bQFLxgndPbAOmYmbjYb10h9bFJz8k5Rl4braheBgTEK6XvhXGr4CfkxS0DfIFhIHRY0_xOSL1R-thzUdxJlzUSoaJzl6XzTGibifSDAJNHJMf_hcxNdlrbgfM-JEejY0h-wPMydDMy4roIdzq_sbhUUxXh0CIM7LddJvdzp_93uAkzbc7RI-YIdB1pp7UyCjkvus8itNYEVyaeC0eCYP3u045AasiBGQOSrk-GKaHpWYb-egGx_zlhFEuvhEvMonFSkU7vlvEoN8d2eMWejc-IUov1KLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R8tUScCWPOPvrQaRZGjbpzyukmBLar765CvbSadmOmX6k4Wcmjd2J_vC5bQFLxgndPbAOmYmbjYb10h9bFJz8k5Rl4braheBgTEK6XvhXGr4CfkxS0DfIFhIHRY0_xOSL1R-thzUdxJlzUSoaJzl6XzTGibifSDAJNHJMf_hcxNdlrbgfM-JEejY0h-wPMydDMy4roIdzq_sbhUUxXh0CIM7LddJvdzp_93uAkzbc7RI-YIdB1pp7UyCjkvus8itNYEVyaeC0eCYP3u045AasiBGQOSrk-GKaHpWYb-egGx_zlhFEuvhEvMonFSkU7vlvEoN8d2eMWejc-IUov1KLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=AyaJGAZPjD27CnLmJyvxnSqlgt9KsrSRTWSutjsTsV7Axow5Bkc8W16IPiAYQ-rGa6-9e1-wVOv-OWkJXGcJclxVwNkY63ZkWHQhxhhzSKyNwPCitZm1lZnuK4DsVQHaq8t6yLeZnlZgJAhq772B-MfjBTdzexs3or4k72lhLBLohnomLZXIzWgZClhNthBEpg22xwnjjBi9RaCKXwDUNVXCpjfq1HVGE8XKf97WTwCkxBHIG1ysTzFd_nR2rXXX--KQdqhy0fesVWz5sMEoJVOWuOrE7cxp4PfG6udqkAzFg5PHhZOavxeLo5eU1WTORS3OXyYC-yxbwHKENUI0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=AyaJGAZPjD27CnLmJyvxnSqlgt9KsrSRTWSutjsTsV7Axow5Bkc8W16IPiAYQ-rGa6-9e1-wVOv-OWkJXGcJclxVwNkY63ZkWHQhxhhzSKyNwPCitZm1lZnuK4DsVQHaq8t6yLeZnlZgJAhq772B-MfjBTdzexs3or4k72lhLBLohnomLZXIzWgZClhNthBEpg22xwnjjBi9RaCKXwDUNVXCpjfq1HVGE8XKf97WTwCkxBHIG1ysTzFd_nR2rXXX--KQdqhy0fesVWz5sMEoJVOWuOrE7cxp4PfG6udqkAzFg5PHhZOavxeLo5eU1WTORS3OXyYC-yxbwHKENUI0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=j34WtrrRNp4icCPJRTmoe6LGfx8s0Z3UYqZwX87ieogRGS3AHgGUWv3r2IyQt652tbw4SCLFdfHGFbKBPz6GecdLSSlGPXZn3ZxKZ55wYyUm28IJdB_efYp6kw7KJFkaszdksB6aEbNBut8pzqLaoE3yrp5z54giFsXeXBIfAGrkTETU9GEwPxad2n-aKI0hnmD6Sv8ehANHSFmQNV51FnrkiGUk4j6oUa9OXRftfwsCMQL_KBqkFc4oI89draW_JgWt9E_BFhn51mqOjReabQlWZq-Fk8Udzd3yeM1Ujj_1ErgmJhiNQ68MFU5S4Az008aB0M7pjqu_TMRl_y38Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=j34WtrrRNp4icCPJRTmoe6LGfx8s0Z3UYqZwX87ieogRGS3AHgGUWv3r2IyQt652tbw4SCLFdfHGFbKBPz6GecdLSSlGPXZn3ZxKZ55wYyUm28IJdB_efYp6kw7KJFkaszdksB6aEbNBut8pzqLaoE3yrp5z54giFsXeXBIfAGrkTETU9GEwPxad2n-aKI0hnmD6Sv8ehANHSFmQNV51FnrkiGUk4j6oUa9OXRftfwsCMQL_KBqkFc4oI89draW_JgWt9E_BFhn51mqOjReabQlWZq-Fk8Udzd3yeM1Ujj_1ErgmJhiNQ68MFU5S4Az008aB0M7pjqu_TMRl_y38Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHgcAyygJ16G7emMsREE7Lla6gd_Zh2503qAM5JJ3KkhbTb_w3bwcCINwRjx_8PLnoGlg0lhVhNNVDHqp2oIQ0esyKQIhYnLyjq2TWdyT65j8bjyrki5Oj1s5U2PTxbJWRIencjvu8XC5S62xfErItUvbMp2tC-76jdG9oFYD5YE5b81icCgfJN7O5Ux-CiTRcdRY7VdrZ_rqEFfpH7B402wfHnyN4Ns_b6gG_HelLON2z697CmI6OHNIj10sR10oaYNrpNQT64rEaomVAUxAdb7g0apnmDamxhM5n_N5uqfUPtwBy2LAm-Xk1-HSA0qNSu-mN6-1nXob9TEae7Tww.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8G_d2RJcnXX8ugg1TUD-zSX7aJr2GY-dSsL7hpAD_ubjnxzqjPkg-cKj62YIVi0PnrGnpW6WOAMUnCtzkYHmOELlpVSyuLMWLPL5qkddx4PQNLb0PeJIVLHuAjx-AfhqD-jaV-K0NTS_63RUk9HihJQgTduR_EY3fs4Ijo5-e-IHut0QJ3uaV9DIy3bWVU_RP3NB9l-2nxF4Npu7hSKL5seuN3e5ZA4CCLv8GgL8sYEKmi1h9ZCAd16gBXOrhEOonPQJ8deRk_fYutokgbBC9MZVjf2hH7GEnD0WcmML1eTRS8Pceh_QTEwSB0Yc0vxw62_RmItgnSpjUUGD6ISHkM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8G_d2RJcnXX8ugg1TUD-zSX7aJr2GY-dSsL7hpAD_ubjnxzqjPkg-cKj62YIVi0PnrGnpW6WOAMUnCtzkYHmOELlpVSyuLMWLPL5qkddx4PQNLb0PeJIVLHuAjx-AfhqD-jaV-K0NTS_63RUk9HihJQgTduR_EY3fs4Ijo5-e-IHut0QJ3uaV9DIy3bWVU_RP3NB9l-2nxF4Npu7hSKL5seuN3e5ZA4CCLv8GgL8sYEKmi1h9ZCAd16gBXOrhEOonPQJ8deRk_fYutokgbBC9MZVjf2hH7GEnD0WcmML1eTRS8Pceh_QTEwSB0Yc0vxw62_RmItgnSpjUUGD6ISHkM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ErrNa_-p6q84XNGE-IUV19t2dfztNnbX2qh9QZ8014iW5oBDR3wnDMBjpO2hOs4oeyljRfhQ2lN9VqIDCZmyLKVNZUzCqmNbghxuXp29mp-Pvjm0YuH6SmidYOUmXVuPzm93RV9pXvu4emEBErKOCF4jK_TYKuxupjl48nlUBI8htdhEm36bn2sXOHiOzY_k8UBe2VUdiNhE0aVX27pAc5fdDe3QyUWlPczUEQH8pI_gKS3qGIINJkdJ5G6m1t6lwNqS0fE6k4NJt29oqRuyQ0PXJyXQZ7o2hKR9WrAKo6ahJ78PkzFKEBASmTtzxODG_qVFosPT3jgHCBHXVeQthA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ErrNa_-p6q84XNGE-IUV19t2dfztNnbX2qh9QZ8014iW5oBDR3wnDMBjpO2hOs4oeyljRfhQ2lN9VqIDCZmyLKVNZUzCqmNbghxuXp29mp-Pvjm0YuH6SmidYOUmXVuPzm93RV9pXvu4emEBErKOCF4jK_TYKuxupjl48nlUBI8htdhEm36bn2sXOHiOzY_k8UBe2VUdiNhE0aVX27pAc5fdDe3QyUWlPczUEQH8pI_gKS3qGIINJkdJ5G6m1t6lwNqS0fE6k4NJt29oqRuyQ0PXJyXQZ7o2hKR9WrAKo6ahJ78PkzFKEBASmTtzxODG_qVFosPT3jgHCBHXVeQthA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZNe_TLa5WOM86DHZIVPAqg8KzyQcsQxSaaW4ggXGdbP2s8jTX7wKmQU3cHtHohlv-67Xlhpy6c6doPkuHKL_kmnvWRzrTEro6IkILrHopA2XhgUByHiWnWg4k-9hG_tS7Axtdtsey0miawZf_K__Qt2VDkQcV7ReXIEa0V0XGXPoTezL-HttzEreObUTFA5j2qjB2UwrCHFnmkf3Ys8klUD1bIm157zSuFwbaYcBRewTxiYSkjbvTEYFsVSfj6lq69MfLBrZAPBg7yFjNzE1exh8q7Qd6vlp400ANm9Hp2P192Ae34B1l378SeYQVDN9IH4zarREBkMPa_ao0EaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=sfxBdPf9UNmnFnjN801c00sPmvM84cC9rfJ3HeDaIZpvqcw61p7LIDN8kmhKOcM049JN3dwxn-SXAxhI3Vy_G5Lrwc2xr8kyxWB74q7_KoSwHvrTqbnsfm40uw1XWCGAIv0n-nDaMHSO7eydUlmY_RA0odVchEEcLdLz2MbAUU6yiuAsv-BoL-K-T21hvxUfasl7iBUjRMSC-H8SsnYf0USG2AYQx7DrCOmTqzRpNtRy3IKuMoivFWAIMgOs1ew0kx-Io7QKe5ZLRqPBSw5I872o3fbu0UH5vI48kwNNAI1Ci01i8vbvwcMmg8MCR_vWu8wPYuJF-mWVOwdEMgI0VqXrqeivCDn-t_sUiQ-tcpS-q1R7f5x9zcgEdf1rKgZVzjEz4--lcI-22WfGTLgEwfHSQQ9okiedTQUs3PUBN7KveBhhSerOTY4MhvucSdGJk5ljtnxPYXOd4Tx0tcvWBZ5h-UokIoxjS7bnuRm98p5pgdZ9Z6UbgJjlzsASlVearGlza-3fwNqJULDJPY4HvnxQ0W9PwLi3EuAivnt4uZvM2CoovGvS_76OY7JGRWk8NF77n9QD42bxo8S1lfC3nQ0sj5R_2Rr86dXlsGUTOhbjXek8F57AemfWde-j610duZFTRvklnP4CzA2DhtLFjTjSBZwDjwM2ytMts9w5dsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=sfxBdPf9UNmnFnjN801c00sPmvM84cC9rfJ3HeDaIZpvqcw61p7LIDN8kmhKOcM049JN3dwxn-SXAxhI3Vy_G5Lrwc2xr8kyxWB74q7_KoSwHvrTqbnsfm40uw1XWCGAIv0n-nDaMHSO7eydUlmY_RA0odVchEEcLdLz2MbAUU6yiuAsv-BoL-K-T21hvxUfasl7iBUjRMSC-H8SsnYf0USG2AYQx7DrCOmTqzRpNtRy3IKuMoivFWAIMgOs1ew0kx-Io7QKe5ZLRqPBSw5I872o3fbu0UH5vI48kwNNAI1Ci01i8vbvwcMmg8MCR_vWu8wPYuJF-mWVOwdEMgI0VqXrqeivCDn-t_sUiQ-tcpS-q1R7f5x9zcgEdf1rKgZVzjEz4--lcI-22WfGTLgEwfHSQQ9okiedTQUs3PUBN7KveBhhSerOTY4MhvucSdGJk5ljtnxPYXOd4Tx0tcvWBZ5h-UokIoxjS7bnuRm98p5pgdZ9Z6UbgJjlzsASlVearGlza-3fwNqJULDJPY4HvnxQ0W9PwLi3EuAivnt4uZvM2CoovGvS_76OY7JGRWk8NF77n9QD42bxo8S1lfC3nQ0sj5R_2Rr86dXlsGUTOhbjXek8F57AemfWde-j610duZFTRvklnP4CzA2DhtLFjTjSBZwDjwM2ytMts9w5dsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1989A67YSbXE15212sTfaN6bqPc_17hsKPy7X-265H9CClzbN9Mz1lyw0Lh4ljeqruDX8Wsmnukpl5G5gmaEWcz215dDpMTkE7eYlHGp9ti_kHIIYCwZuyZNRJPQK9V8mMGFib56i7PGKb69Sr2-5VZ_gEIqRPrhG-IYTMsy8EyHAajYEwKMp1tdnn9w6jOL5sVPyeLrj49IJCEWkWYLFD9_6AdpWCqpIjEDwP6jVaCXQNlXrwZTCIoWzeywqi11oxgUDvIirzbN6eiyhxqGBYNQq1vs45-vVjaUAcjn69dlM6D9T9UcQJ0378ynNMyeQQLBJtVl593K7hFmiDWmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=On27MbdpnjsSRrbwPGBe4v9NwleLPaqBrKB3583ZBTtRzqJI3tCA_izyZJ9re_1Vwfs9vsqYR33whSbaOEg1qLD5DV1kZp1NTD9gbRZESRMpXdJ1kzG6HI-d9Zk7br5WpWyuXwQWc1Q3fzlKrZsuvY6_yRzth9cOuGekhfmLtmwPSKpJqWy7SZYE_Z74q0UGvsKaieQXoUgNLTGfiC8cni6t6cRo_qyn3nZT5RqegJuEqP7I35KdMQLE57SD9GSEbD5InonDbjq_l1h03CBUqZa3l1ezukwNT1MWZzBcwTVNhWkNL2GhhaleamDWmsqT5hbWrQI02fltlRxnEepQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=On27MbdpnjsSRrbwPGBe4v9NwleLPaqBrKB3583ZBTtRzqJI3tCA_izyZJ9re_1Vwfs9vsqYR33whSbaOEg1qLD5DV1kZp1NTD9gbRZESRMpXdJ1kzG6HI-d9Zk7br5WpWyuXwQWc1Q3fzlKrZsuvY6_yRzth9cOuGekhfmLtmwPSKpJqWy7SZYE_Z74q0UGvsKaieQXoUgNLTGfiC8cni6t6cRo_qyn3nZT5RqegJuEqP7I35KdMQLE57SD9GSEbD5InonDbjq_l1h03CBUqZa3l1ezukwNT1MWZzBcwTVNhWkNL2GhhaleamDWmsqT5hbWrQI02fltlRxnEepQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6SOgZVVrEUeUV0nIy8ssjuGy7OFlmuyL8tliWFiG0nJnLSz80zUcXF-MhdRclh8Fxpqd8nOfPN7g9D46c8ezrw7lu2xO64xqnElBaEh0kpEq9ApQVpIwmDXIwdmRNGW0ItfQDzxqcpMVcI5rmHBvozKJ8a50NoRKKrUUnH3NWP9H2fHiHcGUqCQQWfIo90kTF-Wpn4n3Rii8epSkQWr0XG6gudXmfFqsjJGlFRrZaeEkx6ZXBDIRGx9dlkdL1VHuV_LBQg6tLmoqRZNkmAP8jORjasQRjVAsygjlJ33255F5Vp3mq9iwh2ZdFLsdIAx-FXzhb-tS_pxYUVUT06QMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlRECUzsfwQf3BwwVGcPNuwa97_I68GZIl9xMYXUw5bnmt91Mm-TncizPGVAHM80CoNwNUwErvvywTL6gIm_TrjjKlAYV7qAkW30QfBllk7iGgEf5Yh9895WLgYQu_OXgWCi-oLPrmFhJHwdVdZU1_TNXDKCzZEV0B91XBjemXUvbtGTazpW03hav0436Zyo2bv9nYOKvkCrMPCATzBEISj1qNC7U-EVtfdV34Kvr9IZGPxCdM3LYTEBPjetzDSvlJM0oUwJpuU1a1ksACmmKTdjJRWAMap_fzRUeKR8M_h1JMeRUFPi_XErJlbKZkUpf0fz-Ce2eYNiSDcb3ASu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZv_rK757Q8MVvI3Y5gGKOh7NvQAaQMniqKuXf8lERx7WIumaKnE2F4zJx-BJrmbVCDJ2HhqhY_IU3RJ-iUVUnwlmoExrfJhSH3GXtuDDLRuntDAtwqCbKmfwPRNtSRF48l2FeqJt8YTAMCq7awhXIbEuVtdEb2viEI1x53qBjOkVpY-c36fcoYP1E0vo2E_E18EOP0tIH5EJOYL7lv_8Je6ro2MsdNmPcZqvsmvFHvhoiw5t-pzcH9Zdztbxb2c1Io8Kh0D_naaOS-VKVuX6tois-hM9xONwdXuwEM9tkjUo5bgRLlE_hawfz9Gujvaacr22DcZtYfK6c0LKfi_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sfJcgG4BR0_kjshpYpcrY7oWV3tjHqzDYRYnGHtdD8f7tX7bues0uvZAUtiCz49VeFT-gqZp3Cv40cEcoFmS2Z2m8UU8-eoBdwwKJpu7rsqcOh0QH3_dm96FYxowOj_X9JstEgu5qddsgxV7Xz2v1V1nPmCiUwT7nbf6ZPCvbBLyRTKAqQfshM_831wq3ZhXaZrQuuTpx2E4W66g8KDqzO7b0gXFPYAQTMNjjdC8cgelhypSm3oukYzH-DHgqcr4cVLedZ5FOeC9BoDHKr3sKYTmfVVmkJZW7EIXFv7mv-df-w6z2PIZps6Ria9d0ahV6dBOnc_PtmEillQqWQd6NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sfJcgG4BR0_kjshpYpcrY7oWV3tjHqzDYRYnGHtdD8f7tX7bues0uvZAUtiCz49VeFT-gqZp3Cv40cEcoFmS2Z2m8UU8-eoBdwwKJpu7rsqcOh0QH3_dm96FYxowOj_X9JstEgu5qddsgxV7Xz2v1V1nPmCiUwT7nbf6ZPCvbBLyRTKAqQfshM_831wq3ZhXaZrQuuTpx2E4W66g8KDqzO7b0gXFPYAQTMNjjdC8cgelhypSm3oukYzH-DHgqcr4cVLedZ5FOeC9BoDHKr3sKYTmfVVmkJZW7EIXFv7mv-df-w6z2PIZps6Ria9d0ahV6dBOnc_PtmEillQqWQd6NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0_G9iIaxShrbA7T6GSZmKl3TVGQPQ4kr8kWh3PeHG0_98Sgu9PgJoJu6CvFw_u7t4KA6VLV3ZbRLNijHFMJhSnosX67FI9M8LmPx3gwtErGjZEcSdCAt5s2320FbSqwqBvtGelYVoCya4wSUGJAKtQ7AHtb5UFncdWrS2FeLp3u0Iuxrn-9cOuRNO2RTfgXaBxr244tbUPwlQnnLjvdEeBUBJQxKVWo8jI6oOBhGiZwHgRz7922KYFGfCdtKcE3n8DpmwVnSqesi2l4k99uJQan3l0LjleeplKGRzXmdyygpTMi1TBQJJ6UeUmUhK1DpWvFi4sQWqjzX2RbUcxnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFHkgCC-56gznWtpOYdUq2T5C59_DiaKLD3dAPbbE9iMktcRvlfdE7_-9YSVjS8OD_GuJb1-Ui2OooWctJ8SN2qExlgIcKzUkIs3Rc3rnvxQaB4B_7fbkZoX3ErZoXQe-NRUffXJRiXpMZxcSkOUTehePPRAx221RVFdLAFYyXAk43FEctAiOFrlue73dwi3yGl_pFM41PB-Ja43lKIbo4jca_404I5dMAgN33FerCGz8MTZmBXl0fFXu9rzusxV3fij8h12Rd3pknbIFyVgn9bW-iIsDk1BtYAJr3K-wCGyo8D-mckkErxjyxbYBT-ZIcJsMWqm-IaIQcmCzrOF2acM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFHkgCC-56gznWtpOYdUq2T5C59_DiaKLD3dAPbbE9iMktcRvlfdE7_-9YSVjS8OD_GuJb1-Ui2OooWctJ8SN2qExlgIcKzUkIs3Rc3rnvxQaB4B_7fbkZoX3ErZoXQe-NRUffXJRiXpMZxcSkOUTehePPRAx221RVFdLAFYyXAk43FEctAiOFrlue73dwi3yGl_pFM41PB-Ja43lKIbo4jca_404I5dMAgN33FerCGz8MTZmBXl0fFXu9rzusxV3fij8h12Rd3pknbIFyVgn9bW-iIsDk1BtYAJr3K-wCGyo8D-mckkErxjyxbYBT-ZIcJsMWqm-IaIQcmCzrOF2acM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CAuszgXzk9_snzDvEkaJr1MTA55Nh_h5PlLUJz_wUflx8PYj87nE-OHC3KLTRfyPQ5IgV2xXnF0DVSi5lL57Aqh81Xmv9GzjMFKSpFHoWmoCBWQqw0gUIxxQwyouhGUWsbaqzjSS2yLih8-3a4g4cFr3Mk1gS2a9sLsAK3Pa9RtD-mHWEJYb4IdSbOEkCaTvllxOuTG0JkFfoxQKbeNlex0uRtdY9AMAT6S_glmieAhOsopBQlOnNnx6zYMsHrGexeL5qijLIvdDuvlF1Xu74rcNbHpqHH0eMre559Hjn-7NI0aw5p3VU6oQJZhxkHq1orhvDUzSNJ8n6HS-fMaOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CAuszgXzk9_snzDvEkaJr1MTA55Nh_h5PlLUJz_wUflx8PYj87nE-OHC3KLTRfyPQ5IgV2xXnF0DVSi5lL57Aqh81Xmv9GzjMFKSpFHoWmoCBWQqw0gUIxxQwyouhGUWsbaqzjSS2yLih8-3a4g4cFr3Mk1gS2a9sLsAK3Pa9RtD-mHWEJYb4IdSbOEkCaTvllxOuTG0JkFfoxQKbeNlex0uRtdY9AMAT6S_glmieAhOsopBQlOnNnx6zYMsHrGexeL5qijLIvdDuvlF1Xu74rcNbHpqHH0eMre559Hjn-7NI0aw5p3VU6oQJZhxkHq1orhvDUzSNJ8n6HS-fMaOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZOqtbF-rJihvZtBnz6wJ8FqG5lRyfcKp0GDB0xCQz-XlcPzmYJyDy14kw2ItnL8a_qis6QHqywTpddEKtgWx_BsAQLZjhHdxiXMrNsJsywdsji-L0Mgk64-q6jLf1iqkVKydIsbJSyAcXOwfJonXJ2-TMmFsFeXeZLkCqkt131Xt_2cAreJ1l9mt7u3hWIVXsO-eYUzo0PG4q77MxCDQZ4xfERYrpzDtp1SI8l0h1CxgY3rSU-BEhm51rZQOFzXT5G3x9oIJncU5sqBcVinMc3UyYwK9yN-GLcVA4ukE5GAqaKY7ytBAFrXsr4sTy_Dep7QV3tCl93Rx97SU1ep8_LnGoEhbhSJHw78jSYQD2EeDYQbhZMQCV6hwbz74PEjKFVlNbNprWtw1BvWaydJQr2CqEIiMNuXC1-o6PAM9QWx2KSZcE0WNtgbPI1KZya_4o2jHv9U0W_WAVhGTNoB6Pld6sdFHkiqiV3rl72McXicH1BN1ucJzNTLShb5ZzmEtgfBS8daIU7zO8G-9fcAJu00dn_2rDxl065iZsZ6WElTy9PvgSc3xFkv2jcpY5CYqTOenjI__z23DKdLS44FaqVgsoAg7Iz4naY6AYonLAJ80oBDLqXMfPQE_bJv9M9vbCxLlCIKB4KynuB0k220WYFd9JXLNeHdcROMBMTsalas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZOqtbF-rJihvZtBnz6wJ8FqG5lRyfcKp0GDB0xCQz-XlcPzmYJyDy14kw2ItnL8a_qis6QHqywTpddEKtgWx_BsAQLZjhHdxiXMrNsJsywdsji-L0Mgk64-q6jLf1iqkVKydIsbJSyAcXOwfJonXJ2-TMmFsFeXeZLkCqkt131Xt_2cAreJ1l9mt7u3hWIVXsO-eYUzo0PG4q77MxCDQZ4xfERYrpzDtp1SI8l0h1CxgY3rSU-BEhm51rZQOFzXT5G3x9oIJncU5sqBcVinMc3UyYwK9yN-GLcVA4ukE5GAqaKY7ytBAFrXsr4sTy_Dep7QV3tCl93Rx97SU1ep8_LnGoEhbhSJHw78jSYQD2EeDYQbhZMQCV6hwbz74PEjKFVlNbNprWtw1BvWaydJQr2CqEIiMNuXC1-o6PAM9QWx2KSZcE0WNtgbPI1KZya_4o2jHv9U0W_WAVhGTNoB6Pld6sdFHkiqiV3rl72McXicH1BN1ucJzNTLShb5ZzmEtgfBS8daIU7zO8G-9fcAJu00dn_2rDxl065iZsZ6WElTy9PvgSc3xFkv2jcpY5CYqTOenjI__z23DKdLS44FaqVgsoAg7Iz4naY6AYonLAJ80oBDLqXMfPQE_bJv9M9vbCxLlCIKB4KynuB0k220WYFd9JXLNeHdcROMBMTsalas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iCgqbMP2RXaxZJzInzxqcFYfiqIs74YG7GH9Uc9oLWOapTTR1n7Y8PL3tk0XSPCCKzcALxhOhUUttutQnoE2YJPRTHpH1F6udb63MiRpRCVnCHoZ1SbfIVcbvS4llWjJU3RAIALrPejvdcDYAHerF4g-V5oV-F8IXlKIQEDs4mCpl9_zuLMPRExUJWx-d5qMNjGcCnlBrkYyaIrLQnLfP5LjlovK3DExqi2eSxkEwH11EbHdnFuOj8pdgz1cwzp8EhpAA0T2StdJhgc-uSaDiFsXE8MBJmBkbB2dd65dHzAA6jbj_4dwyf0d-P2A7qA-eM5MRsS-tIZ3IgBM3knsNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iCgqbMP2RXaxZJzInzxqcFYfiqIs74YG7GH9Uc9oLWOapTTR1n7Y8PL3tk0XSPCCKzcALxhOhUUttutQnoE2YJPRTHpH1F6udb63MiRpRCVnCHoZ1SbfIVcbvS4llWjJU3RAIALrPejvdcDYAHerF4g-V5oV-F8IXlKIQEDs4mCpl9_zuLMPRExUJWx-d5qMNjGcCnlBrkYyaIrLQnLfP5LjlovK3DExqi2eSxkEwH11EbHdnFuOj8pdgz1cwzp8EhpAA0T2StdJhgc-uSaDiFsXE8MBJmBkbB2dd65dHzAA6jbj_4dwyf0d-P2A7qA-eM5MRsS-tIZ3IgBM3knsNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9hSnHE0twGqGLuuJq6Md5wZ_elcEi520Qrr4uOGXtFhui1p8Iv1ZnHpdkfqVbMBLbyFw3NKayhvYvQWu7jkjEGBE7WaJmubaGtLqLo3QKDW3o9zp9pygewLULgrkWcbBcqDXUOL5h5nDJRw08HoL_W1UqXN21MlsoUmTp54vkFso9I3M0QMt9HuhUPVQqZKdfJVIb1fLYCMevTRvaR5SJHMT2qN-tfp6N7-3vb_roVW-1Gon4Q72gDKTR0Jiufnsf56DG-4mOiEYZMgGnvdCCOdvhcOU9o3TQmDt-68RSz6ZNgt0ybd46D51DEnMOGWoMv5Y9N1TwoWKLJp4N1EWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=PvABcl-GWXnRd2d-BZKuZQ3nvBDNJTE3HCTY5WJhtdsYb-i0Umyq5jrdeh_1qOY--gXwR6IIat4ZQgbA_63z2VUF1uRxmDbGDf0MYc33sXJkXWhdexTip5ca9ZBknYN8YocGxodi2Wig8ObAAFFMxrUa6VUe-b-d4WlE5n_JmgVNYBgJ0ep-GIUGyHPVwNYiq-lO4_qWM94adQd4Zt5LE5mMTnVIL3O-jWCjMsN1y9VrGG6wNtccgpdhUk5UF05RqCgFgqkvBgtLJyMFgCdojC1C1pngBfG8yukDDVR4O5OspDjmvXALNPMnRarzqliZ05jQs-u0i4KvygNi-joPMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=PvABcl-GWXnRd2d-BZKuZQ3nvBDNJTE3HCTY5WJhtdsYb-i0Umyq5jrdeh_1qOY--gXwR6IIat4ZQgbA_63z2VUF1uRxmDbGDf0MYc33sXJkXWhdexTip5ca9ZBknYN8YocGxodi2Wig8ObAAFFMxrUa6VUe-b-d4WlE5n_JmgVNYBgJ0ep-GIUGyHPVwNYiq-lO4_qWM94adQd4Zt5LE5mMTnVIL3O-jWCjMsN1y9VrGG6wNtccgpdhUk5UF05RqCgFgqkvBgtLJyMFgCdojC1C1pngBfG8yukDDVR4O5OspDjmvXALNPMnRarzqliZ05jQs-u0i4KvygNi-joPMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=NLTCy1jOvvUFzmU4BBwwqnm1s-Z5q8mneUIX0A8U8QjoEzYkY-K7HieMYr4duxz1USjPZ2EmZgdTEQRXlr7xQAT4ls9LeTEYrAYTNxawIM3wQQwUlLv4MR0S4idmC9Bt3UO757fmsbEqDwVHzaP2swxsEVdC7t6_LKLkdOwBUGp-NqDnlUJPtdtRK5BQNHwPUN0RTkFLWMBjBbVUC13NlrCANhp6-b0M-YEp3MT89_XhRyB4wjZkx5lcBxKK5xC13SFl_NykED8QCuwyAAuO58jCDx5qzIgomkdfhQJqRAd1-DmOVircW7NyUtApO5VzV3hTARcXrGlbR4uO8KZ51zbLd6c-ajjP4MHKXRjkGwiwIO9EAUdBL91tZYelJbxNt0tB4OcJmxhEeE3Iu8YyhlDPeH_gW8SS31AhrFDmNnAVSGVDrQXXcK-I7X7AfrzqavtepH-_4qxrHlXCGriXg1ekej0_ZdifcjoiywjFOJM_d0QhtW6kBXjkJ6Gx7lw5SoTCNsbmIjAeTeP2quwWy174S--_sy3ks9Qp-ae8pbhw0MrBBpeJZ1N9gxqAwAW_qvm064FxLE3Fcv2CzyBu8RjF32X8ItglRZQP90b3JFOAJh1eGnrpUc_LplKLl1sxJlPdm1miA8s1zdofJEc3uBLFfRt5hJzU6gEEJkblrEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=NLTCy1jOvvUFzmU4BBwwqnm1s-Z5q8mneUIX0A8U8QjoEzYkY-K7HieMYr4duxz1USjPZ2EmZgdTEQRXlr7xQAT4ls9LeTEYrAYTNxawIM3wQQwUlLv4MR0S4idmC9Bt3UO757fmsbEqDwVHzaP2swxsEVdC7t6_LKLkdOwBUGp-NqDnlUJPtdtRK5BQNHwPUN0RTkFLWMBjBbVUC13NlrCANhp6-b0M-YEp3MT89_XhRyB4wjZkx5lcBxKK5xC13SFl_NykED8QCuwyAAuO58jCDx5qzIgomkdfhQJqRAd1-DmOVircW7NyUtApO5VzV3hTARcXrGlbR4uO8KZ51zbLd6c-ajjP4MHKXRjkGwiwIO9EAUdBL91tZYelJbxNt0tB4OcJmxhEeE3Iu8YyhlDPeH_gW8SS31AhrFDmNnAVSGVDrQXXcK-I7X7AfrzqavtepH-_4qxrHlXCGriXg1ekej0_ZdifcjoiywjFOJM_d0QhtW6kBXjkJ6Gx7lw5SoTCNsbmIjAeTeP2quwWy174S--_sy3ks9Qp-ae8pbhw0MrBBpeJZ1N9gxqAwAW_qvm064FxLE3Fcv2CzyBu8RjF32X8ItglRZQP90b3JFOAJh1eGnrpUc_LplKLl1sxJlPdm1miA8s1zdofJEc3uBLFfRt5hJzU6gEEJkblrEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfmDFPFN9Y-QuBj7I00UL7vU-Iwmvak3ipUYoAR0TZEguH3woXnOHaJZfGN1UER9QHHdzLQcpI9Rnrhznz38WzgLToLOXoOHoDayvH8ZMWNdR0H5AZ96JcKSj7HSfen22tL8oIPcG9_Vd5rvmsTKAdgmMURlxZ-8tafYTyR811EbS8QRigkzt34Mnk0q7q3cc1akWxhEr8JKxSaz_KiOpy6g8uNGBlBcD-XZl4-i7CT3ffiLMpR9RTRKM6vnHKlmtgv0VCK6mRyxNEApPbF38abxnzrjVRfHub_vBTVp2X2oHTs9eL6hPYBzEF95D_rJU_i4S-PZHY8rnB5lvJ6_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XXTQmrKGtOmsg2UTQDLN4HjrvN-L-7sSjS5MEYrhg1K_lfd9MJAQlCT4_Ly92aX5zGn6HV7zjfqQV_PuZU28xwE9ei9_LfVZ3EanwHIiCbnJVhQPqsxncaWkg1_NRSU-oaEpI4ErQHf6IrzTnWt_HZkqKcJMePcmhXQhO3_VmRqyUllzx-Xj8_jiGP7OejNZVeSRmz44Wi9w0yOZarj1GNLMYVacGSshrYXuSTgtq52b_1BWUa1qA2rdU2xVKQTUbfpsy1uOsCN48sZJE0d7rfn0kWqBVNizYmrJKP1lzdPdahGureyqmaT-0u5z2sFjaTQL2KbvDG2KLZArslkCwbqXrMOdpAlABhDcq-DP-SOJWpo4I9cRZHzLyV6b-nSm1_9uWJ20pwhh_S2NxEcAkYGe12J7eYq5teJzt961NBg3ZVMC-7opub3O4z7B2a6fuGkgCFkJVxvWjMX3xuiM50L1mwFn5MogEeAmv0g1nQpviF8jx4UyMY6zH54PzEalGaoAlD6FuJtnARqPLcnaD66uA_BQoY9C6LTnuUfsg_XNC0RBZVt8qezFVI2QTv2oFN09HuDw1UZmnmyHS-uVv_fe2b--QYVToTx6akCpwHo4fOo-TT5eDTr_UykgIO9EID7wWASMDp4pheDg9sFeIbHnz6dbUApT-oG6FX_1GZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XXTQmrKGtOmsg2UTQDLN4HjrvN-L-7sSjS5MEYrhg1K_lfd9MJAQlCT4_Ly92aX5zGn6HV7zjfqQV_PuZU28xwE9ei9_LfVZ3EanwHIiCbnJVhQPqsxncaWkg1_NRSU-oaEpI4ErQHf6IrzTnWt_HZkqKcJMePcmhXQhO3_VmRqyUllzx-Xj8_jiGP7OejNZVeSRmz44Wi9w0yOZarj1GNLMYVacGSshrYXuSTgtq52b_1BWUa1qA2rdU2xVKQTUbfpsy1uOsCN48sZJE0d7rfn0kWqBVNizYmrJKP1lzdPdahGureyqmaT-0u5z2sFjaTQL2KbvDG2KLZArslkCwbqXrMOdpAlABhDcq-DP-SOJWpo4I9cRZHzLyV6b-nSm1_9uWJ20pwhh_S2NxEcAkYGe12J7eYq5teJzt961NBg3ZVMC-7opub3O4z7B2a6fuGkgCFkJVxvWjMX3xuiM50L1mwFn5MogEeAmv0g1nQpviF8jx4UyMY6zH54PzEalGaoAlD6FuJtnARqPLcnaD66uA_BQoY9C6LTnuUfsg_XNC0RBZVt8qezFVI2QTv2oFN09HuDw1UZmnmyHS-uVv_fe2b--QYVToTx6akCpwHo4fOo-TT5eDTr_UykgIO9EID7wWASMDp4pheDg9sFeIbHnz6dbUApT-oG6FX_1GZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=is7ldvOqy2ktxORfApvRuO4A2STr55jA6XJm06Ntgmq3IuDNuzAoFTGlrXVVddUzn5EfQPhtXkWTnpNeVIH1hJifAXn8AXm6p5VK0LnPV30jJMwhWexBamumMPRqEkgWCvvamErkuM63fikY3XEqzUAZjyhyGkRm_TXm0sl1InVfD_1W03tLcLudlgKiqT8UOkAtFKCqFgr9PHEeuS0yVFAmkkY6zgY7kt3xqtY49YDFVYq5XgA9NdjedVJT7nfRAPhGn92X4Byza8gq6a19BrYuQOcmASuLgkbnF-2ajodnqlOZoHE7SRUqqTkgVQWQ0wy-GQlXSwsxpAjQzevs6yCv9IJZvp_KOBzQ1jko9VjfyXgxr8PPeAIFq0VsI3mfqpFh9twfKequN1QLmR3F4EfcrBbsEBRMsgXzMuxFhzi_Gxd_HsH6IFqiWYNcgYm2F50-Yvr-YnT1Xg1TEwLo-ZcllEsdGhf4hqhgOngOT2swFPPh5bdShx5moPa-uxi0betRTa1kCemVpcTBUNW3mLJvSGKaMdYR9sN7V4CgUEdwplFe15VqO9OIwdeEvTEiPYoBSykuYQHRzqUiY_SIigfVJ_TcZJhdQyreeDvQipmWnPPvhqQPkW0BamNkkVfDriaS4dubbQCgOrXiDzfjipLaue1ZPW72hiEPcM_8cvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=is7ldvOqy2ktxORfApvRuO4A2STr55jA6XJm06Ntgmq3IuDNuzAoFTGlrXVVddUzn5EfQPhtXkWTnpNeVIH1hJifAXn8AXm6p5VK0LnPV30jJMwhWexBamumMPRqEkgWCvvamErkuM63fikY3XEqzUAZjyhyGkRm_TXm0sl1InVfD_1W03tLcLudlgKiqT8UOkAtFKCqFgr9PHEeuS0yVFAmkkY6zgY7kt3xqtY49YDFVYq5XgA9NdjedVJT7nfRAPhGn92X4Byza8gq6a19BrYuQOcmASuLgkbnF-2ajodnqlOZoHE7SRUqqTkgVQWQ0wy-GQlXSwsxpAjQzevs6yCv9IJZvp_KOBzQ1jko9VjfyXgxr8PPeAIFq0VsI3mfqpFh9twfKequN1QLmR3F4EfcrBbsEBRMsgXzMuxFhzi_Gxd_HsH6IFqiWYNcgYm2F50-Yvr-YnT1Xg1TEwLo-ZcllEsdGhf4hqhgOngOT2swFPPh5bdShx5moPa-uxi0betRTa1kCemVpcTBUNW3mLJvSGKaMdYR9sN7V4CgUEdwplFe15VqO9OIwdeEvTEiPYoBSykuYQHRzqUiY_SIigfVJ_TcZJhdQyreeDvQipmWnPPvhqQPkW0BamNkkVfDriaS4dubbQCgOrXiDzfjipLaue1ZPW72hiEPcM_8cvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RbjRkWuaA7ODzOdj9faXGS97pRVGTTaFOXPKAeKavE3G68Fqu_qSQCBfD55rIqd2jARq1LCfM3B5xkXwzUjz4Kdg6rhJjnIFU5uMAW8-qGDdoA8tM9PXEHhTEksDg5Xwt_bvZkZkTpMTFVfH3NG3A88PDoOjHaCZlvsDL1N9mXcbX2eHXQ2WCWktbpnPs6lc_XX5PMBZrplNbsg2WKfjK8YWsVfzn391rIQzVMAwEUyTOaxmPTKZ48Da6i3zcmW2eM1o0p4nTMLy2W4QTCnHgCTYXjlFvqmEhL3tTA5p7G2MlrB5rzgBix-C6O69uaSbb7my3Ltx6GtJsNROB30eKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RbjRkWuaA7ODzOdj9faXGS97pRVGTTaFOXPKAeKavE3G68Fqu_qSQCBfD55rIqd2jARq1LCfM3B5xkXwzUjz4Kdg6rhJjnIFU5uMAW8-qGDdoA8tM9PXEHhTEksDg5Xwt_bvZkZkTpMTFVfH3NG3A88PDoOjHaCZlvsDL1N9mXcbX2eHXQ2WCWktbpnPs6lc_XX5PMBZrplNbsg2WKfjK8YWsVfzn391rIQzVMAwEUyTOaxmPTKZ48Da6i3zcmW2eM1o0p4nTMLy2W4QTCnHgCTYXjlFvqmEhL3tTA5p7G2MlrB5rzgBix-C6O69uaSbb7my3Ltx6GtJsNROB30eKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=d6u2_s55gdzj3OpGfHZL6dHS0EnyAqfXOceRLFwN8HX5-CpjM-1EYH2cDIWlxrPnjFwMPu6bK1ECBsnZodoI-OdXUFteFWXX9mxf0W0tYRGBSr-5wc1Tfnb5pQkvjNBQu0eXAUA3kxIr6v5k5epmmvlWhDNxzYgt-Xo2H6q6HmJdtLQ0EnbcKHvGcO34NUsel-FOrFBOGcDe0FIl9ZC0YStGtw46UUxblDGc8gYwws060rluj4cJueJtt337yW0A9yd0r5L9-wvVqyTrnBvBnQyqBNdLnI38dH4gt6B33PAXxbumzrBT5hfrgVCOLEziiB74D6PEwfDbd_Vfn5LG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=d6u2_s55gdzj3OpGfHZL6dHS0EnyAqfXOceRLFwN8HX5-CpjM-1EYH2cDIWlxrPnjFwMPu6bK1ECBsnZodoI-OdXUFteFWXX9mxf0W0tYRGBSr-5wc1Tfnb5pQkvjNBQu0eXAUA3kxIr6v5k5epmmvlWhDNxzYgt-Xo2H6q6HmJdtLQ0EnbcKHvGcO34NUsel-FOrFBOGcDe0FIl9ZC0YStGtw46UUxblDGc8gYwws060rluj4cJueJtt337yW0A9yd0r5L9-wvVqyTrnBvBnQyqBNdLnI38dH4gt6B33PAXxbumzrBT5hfrgVCOLEziiB74D6PEwfDbd_Vfn5LG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sG3T34EMf7-qzLAq8E-5yd4z-C3VSGlKtUaI_CY1GMGlj-DkOQB1jzvu_8J4yiBxGB0DRhv96Jw5s9rYUsCgAQ5GdXS7cSmeulso1FwO9dpdPeoJxrkN-N0-zrIymsG1mvDmAGZdiAub1g06mNc_l1qEqhQdyk5h486NnRjjuKTb_okU5EBhrZbH3lZwYmXsYoLSQbHdOCt9BCIF9t8Vbc-Y-TuTYEQRa5Jsf2Aw4WJfpoW9Ezx8idQhWnYveXfnMbE6XeSvmSo1Zu-J8MXsr1QGA3vS0g9ckLUIxBJ-uf2thBRTslYjvDEM9V6nD3SGLqv5ZgphjEbGjNZQ_HhW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sG3T34EMf7-qzLAq8E-5yd4z-C3VSGlKtUaI_CY1GMGlj-DkOQB1jzvu_8J4yiBxGB0DRhv96Jw5s9rYUsCgAQ5GdXS7cSmeulso1FwO9dpdPeoJxrkN-N0-zrIymsG1mvDmAGZdiAub1g06mNc_l1qEqhQdyk5h486NnRjjuKTb_okU5EBhrZbH3lZwYmXsYoLSQbHdOCt9BCIF9t8Vbc-Y-TuTYEQRa5Jsf2Aw4WJfpoW9Ezx8idQhWnYveXfnMbE6XeSvmSo1Zu-J8MXsr1QGA3vS0g9ckLUIxBJ-uf2thBRTslYjvDEM9V6nD3SGLqv5ZgphjEbGjNZQ_HhW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=sEJgU4Q0f5atswx8BxUErtRBaurU65FSjPKabXbgapBeX7birYGuX0pdT9pjpGLGbLN7BJYybk2SLVGCcUtXgBgv6vO5aY36U1J-RMV0DgEVxbpdtGK9OPIXclPsMUMf79rOZkQ5Gg249QsTs5BTG0eqXb4aKWPFjIWUD4lAkhs7bsimS6te6LZExEhlQeLmJMASNR_9AdzI6RPCV5RuWNDxXtFqbzpejvUr0y270Lqh3kPJU54pZHG1uPwGEmhFzQpYVtxh8KPeYcWOsOu5Y5bm9rtNHswlYASOpxS3VY9yk1O0DqeCk1-uJucMyVL43bNSFlcHYC-ucc3-B_j_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=sEJgU4Q0f5atswx8BxUErtRBaurU65FSjPKabXbgapBeX7birYGuX0pdT9pjpGLGbLN7BJYybk2SLVGCcUtXgBgv6vO5aY36U1J-RMV0DgEVxbpdtGK9OPIXclPsMUMf79rOZkQ5Gg249QsTs5BTG0eqXb4aKWPFjIWUD4lAkhs7bsimS6te6LZExEhlQeLmJMASNR_9AdzI6RPCV5RuWNDxXtFqbzpejvUr0y270Lqh3kPJU54pZHG1uPwGEmhFzQpYVtxh8KPeYcWOsOu5Y5bm9rtNHswlYASOpxS3VY9yk1O0DqeCk1-uJucMyVL43bNSFlcHYC-ucc3-B_j_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=DGUPjPf8bBZmHarPmZl3WRmInGt4fLuNnWptOxuqTFc9mre6lWXGoedZ7LJ-WKJio-iuLpw6TYYs5AeZmIBCOc79BMJVWkTqcuaRIYdZk1BH0gBWd_iagGuUr3PW2Rm5KbgX3iHG1dUMeAU_9hWo_4-hSnja0Pzp6B24wL604UFLkSB5M8TvpW7fSVSImSFhKNHkajM_GD_rbF1tTYijX4rdb0L89bozgV0BEVYqPsODzfv-y0m9t_lYIIrlpCSkuJntRELggceb4QGaZxi2iswtnMEq4O4ZtFSxEYTTahbEyIBkX6jcsJtK5BNMojwXf7O-pILqe47Sg7LqIjSh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=DGUPjPf8bBZmHarPmZl3WRmInGt4fLuNnWptOxuqTFc9mre6lWXGoedZ7LJ-WKJio-iuLpw6TYYs5AeZmIBCOc79BMJVWkTqcuaRIYdZk1BH0gBWd_iagGuUr3PW2Rm5KbgX3iHG1dUMeAU_9hWo_4-hSnja0Pzp6B24wL604UFLkSB5M8TvpW7fSVSImSFhKNHkajM_GD_rbF1tTYijX4rdb0L89bozgV0BEVYqPsODzfv-y0m9t_lYIIrlpCSkuJntRELggceb4QGaZxi2iswtnMEq4O4ZtFSxEYTTahbEyIBkX6jcsJtK5BNMojwXf7O-pILqe47Sg7LqIjSh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=QM6Ugy_hUdGFCwekoKcScJx2uFoW0AOmOR7gv77tkZnr2vDQSaSyESL-eoqfxtH888VRUKrtN9y9UWPll3NUWAan-hgcqUKlpq7DOOWEtQ8Qufbly_oHe6vxFPrkGh3qxj_Zw2CUsQzy5cWgwm7dVn79N1GEKakP_hFzWUUP7ifmC-c_Hdx1r5ycp-5UvQsgkcB1GDxH4g1hrfSAINP6q7lAnz-mNcTjlKjrW9BiGZ6Vq8xjOuS7wC3g_xchrr1gmelaqkvNaLokaOLbybrTYTjxb1EbwO5Ndm5HRsm8nvTGujg1j9C6wm_djruc1PIlTsVQuBiBGKNNCQ2qGQHFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=QM6Ugy_hUdGFCwekoKcScJx2uFoW0AOmOR7gv77tkZnr2vDQSaSyESL-eoqfxtH888VRUKrtN9y9UWPll3NUWAan-hgcqUKlpq7DOOWEtQ8Qufbly_oHe6vxFPrkGh3qxj_Zw2CUsQzy5cWgwm7dVn79N1GEKakP_hFzWUUP7ifmC-c_Hdx1r5ycp-5UvQsgkcB1GDxH4g1hrfSAINP6q7lAnz-mNcTjlKjrW9BiGZ6Vq8xjOuS7wC3g_xchrr1gmelaqkvNaLokaOLbybrTYTjxb1EbwO5Ndm5HRsm8nvTGujg1j9C6wm_djruc1PIlTsVQuBiBGKNNCQ2qGQHFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=s4PPxeZy7IN0ixLIt3ZIdO3Ir4uf9QyT8vnoWdGzX3yPgON6PQy-2Brkfr636X-neK2fjxayJukKbU095r-fqWQR7rK0PV-_S8FHgopMndNsgpiF0DRNw1Aud2H3Kb0b608MVtlaNKKTAtXF4DISM0jBMN98iO0v9G_eMhUUoyE6qZgWqkyH_jfNqerj7ZYvaq0lt7wBZudk-RGAEZc2lOul05fFSNDT4CS0mmS8k5XRg-Vt8uUWUuDfzdrj-JG-aHp-528ZI8hF1GfIwNKHNLM3cA1O-LcmGcoaL8k4a0U6qkWJumynWAgwF6ocCixn3_MyjLCpsyzFDtWR6YjeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=s4PPxeZy7IN0ixLIt3ZIdO3Ir4uf9QyT8vnoWdGzX3yPgON6PQy-2Brkfr636X-neK2fjxayJukKbU095r-fqWQR7rK0PV-_S8FHgopMndNsgpiF0DRNw1Aud2H3Kb0b608MVtlaNKKTAtXF4DISM0jBMN98iO0v9G_eMhUUoyE6qZgWqkyH_jfNqerj7ZYvaq0lt7wBZudk-RGAEZc2lOul05fFSNDT4CS0mmS8k5XRg-Vt8uUWUuDfzdrj-JG-aHp-528ZI8hF1GfIwNKHNLM3cA1O-LcmGcoaL8k4a0U6qkWJumynWAgwF6ocCixn3_MyjLCpsyzFDtWR6YjeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLcc77mlo0mtiRsUZhBeXD2hqxGC5P6pC8WqMgHg6qtC49lr3vlWIbfn-pem9wf-ymzq5C1sDM-QQrNWobPm2t5yfeoY4604Jd-x4rCcuBQzod-Da53agUL13fNsuqq0CqV59vEAW3JUcxA_RPf5W_ADquvMA2vmRQrormT5xkxHLZf6z41n9Zukvy1NogjdkdWxtihG_P1GX-fl9mHMoTkakanAczbnyf_MuZK4YeZrr66-x-ROXrAf4a8vk78G_289L5FpDdW2_xQLlV1B4YNZNaZThYB_6CV61w5R750X-NtgbyCxo8pETADLyd-XRtJcCBRWT1YaaazR2O6VFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=IOD4Esl962-yRaEQG7GvDyOC5pNOWqNif7YP8ohlY1kRrqLkvZM9i4y3F9cZSw5tbM45PKjOWRPfpHyMRNkk4NSk6Ur99oWGnPoqslSvRn4_AYTRYyhCFhHw5Zj6yrkAzDkyqwdzP35vJakpCcgGGhSWhCl9TADEr1aRigsdZjX72QUSoBCEdbuZK7muMyWI8O2Hpta--f1rr8QulP28KMWottRnZn_Oj4VRU35RToxm_fCH69kf81K-nki4OWaNBST5ymiPYLkE9NmLHXncBGQ7HeO4SzhBPlCTDlB2S6HRjaeQzhjYRQOJE3p89udGW8v4mKOA_cuxnE8qiL0pEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=IOD4Esl962-yRaEQG7GvDyOC5pNOWqNif7YP8ohlY1kRrqLkvZM9i4y3F9cZSw5tbM45PKjOWRPfpHyMRNkk4NSk6Ur99oWGnPoqslSvRn4_AYTRYyhCFhHw5Zj6yrkAzDkyqwdzP35vJakpCcgGGhSWhCl9TADEr1aRigsdZjX72QUSoBCEdbuZK7muMyWI8O2Hpta--f1rr8QulP28KMWottRnZn_Oj4VRU35RToxm_fCH69kf81K-nki4OWaNBST5ymiPYLkE9NmLHXncBGQ7HeO4SzhBPlCTDlB2S6HRjaeQzhjYRQOJE3p89udGW8v4mKOA_cuxnE8qiL0pEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=r_ZZGZwItrFoyT1bCaQQZuRPulJ09-oVIGcKij-7U_yeAB-N9qwOmN9zI7KWaswSjQy_sSYfOAYVUQwAPyziNJ2vL4aBJ1OmL32MEu3_nRpO2WY7EGOg8hXOJ5sPh6U84kX8ZHU7kPc4sTRJvAJkBVP2JOIwfycnXSg6DrwnSVgAxdFCEJiPc5dFtx9mEvd2_KT5mIRIiLbLCPrlJDWZDI-Tq9Qu05c_NApEBYYC3CaNQjQ5kWU0PwPsi2PaBAsE8mRrejmDz9pl9N30TDrsYR739JN6kIoOXXi0xRYnilZ_UP4K4A_cX9YM9xXhzelizLgjej8LCQ4TCdioCXzOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=r_ZZGZwItrFoyT1bCaQQZuRPulJ09-oVIGcKij-7U_yeAB-N9qwOmN9zI7KWaswSjQy_sSYfOAYVUQwAPyziNJ2vL4aBJ1OmL32MEu3_nRpO2WY7EGOg8hXOJ5sPh6U84kX8ZHU7kPc4sTRJvAJkBVP2JOIwfycnXSg6DrwnSVgAxdFCEJiPc5dFtx9mEvd2_KT5mIRIiLbLCPrlJDWZDI-Tq9Qu05c_NApEBYYC3CaNQjQ5kWU0PwPsi2PaBAsE8mRrejmDz9pl9N30TDrsYR739JN6kIoOXXi0xRYnilZ_UP4K4A_cX9YM9xXhzelizLgjej8LCQ4TCdioCXzOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=N2vOR3lctxFWJyrN7IclopPm9bsiHSOwzBZUcp55f87j5CSWs2mY1tDixjaizIpMrsebL6fXGI6N3-k90-IvGcL0O13dbA5FMgmQM0Z74crCzuMvJE4NdKhO06kGhgeXJAFZTroPzxdQhiFrwf7y1jOxoVRYhOiKxDkSKpMCywv8WkuEGS1GRaA0YzSSfKXEhDhf6MsL8qe3GhXTRVqUy8duaH-lWTUO1NiC1__bqgaa9jcITXTdsqDKbgpwP5lKoffy102R8kCyss4DxMYQic72gtmD6qGdwR4Hy-guOT8nvdQ8hksx3SJziQVDqul9YK-4Rld09T-1BtBhlCwJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=N2vOR3lctxFWJyrN7IclopPm9bsiHSOwzBZUcp55f87j5CSWs2mY1tDixjaizIpMrsebL6fXGI6N3-k90-IvGcL0O13dbA5FMgmQM0Z74crCzuMvJE4NdKhO06kGhgeXJAFZTroPzxdQhiFrwf7y1jOxoVRYhOiKxDkSKpMCywv8WkuEGS1GRaA0YzSSfKXEhDhf6MsL8qe3GhXTRVqUy8duaH-lWTUO1NiC1__bqgaa9jcITXTdsqDKbgpwP5lKoffy102R8kCyss4DxMYQic72gtmD6qGdwR4Hy-guOT8nvdQ8hksx3SJziQVDqul9YK-4Rld09T-1BtBhlCwJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VN_ZG4pnt_GPrAhV4j6f1ti2Qky0z0bpXC6cl_D1aKzXsqEwVxOrAZ156dE5omhRE-qfbsk39MEpcQ2tk5f3ooretG58PrnaanSd-YE6f4CBGKQH2uoPOtclC3ORTUWyxzptKF0ZGbwK5GWmXXJm4E-xh0w-VzG1q84F8nymkoRFzK3_x02Lp-tl8gIkSfGLRmg-GC8yMkVZFImtJYFBT0600eVZxAAbGpCmohLxXUfYP9MvkJZrrk8Tbb9yskkuJWdiNXS72mr2qR-fen8yiwBluD2myFodzsFlInXzZ5UgC9Hq_-IjMHF_7bwZXj6s8FDesib7HzoD9suOw6gIsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VN_ZG4pnt_GPrAhV4j6f1ti2Qky0z0bpXC6cl_D1aKzXsqEwVxOrAZ156dE5omhRE-qfbsk39MEpcQ2tk5f3ooretG58PrnaanSd-YE6f4CBGKQH2uoPOtclC3ORTUWyxzptKF0ZGbwK5GWmXXJm4E-xh0w-VzG1q84F8nymkoRFzK3_x02Lp-tl8gIkSfGLRmg-GC8yMkVZFImtJYFBT0600eVZxAAbGpCmohLxXUfYP9MvkJZrrk8Tbb9yskkuJWdiNXS72mr2qR-fen8yiwBluD2myFodzsFlInXzZ5UgC9Hq_-IjMHF_7bwZXj6s8FDesib7HzoD9suOw6gIsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSZnOPKmwe4n-dqUfKhQzbziUntzeF3_ALFBOeEHsCTs8kaXuykC4cW_0vtaAAYx59mzuDNLq6PXtYTtKHemKI04_rYNLd9fh2py1k97xfdlVVDl4R71Td6k3zkihRvLmFDzlpOgiOKPWYV-FRaCA0NFVFkWVVAnV3XpsCzX06HnwE2mPs5fpTG6OPx6hqe4CQd4c10cwMxvfg4c8Pa1XWbrJG-xXQwsFG_k7rnlqR-tGJH7Ji4h4fUgr7aGjlM9-tg3lQuxYalq2r6ZU2DvaKT-BSvKz6bXsK4HehaI9ZdFmY14Bx9KyEYhlz3927LeLQ6NfDckNPEfI2tWBnFXOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ig2HIz81vLNJ5L4ixj_9wyBIYQNe9UT75LX5R8hA5fM-xIqzKGuM5AZm8kIHfqLVVO0aMLTCUwvAheHViuxxhU6n9wIl4yGJL1yXbOOCelbaJ8sk6M7F917fdJOfdUsYJpV3m3Vokjmz6LjoTDhWonvyncR3KLDtg-7CJDD3-PkS1Wp9hfSarmxyA5SCnSxgb2iavnXDbjPVdzwY_WU4WBvNiX-BBf-WYgPexfoq2ipCzrdWKGyPP2GtsZ2LU0YuIRe4Et3B7Ray5acR6JNImpDvO3kOP_UbQs5aEvnvD_talrqPZBGdxy5yx6PPPGJlQFvLrMM9SbeLquMkMaGBiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ig2HIz81vLNJ5L4ixj_9wyBIYQNe9UT75LX5R8hA5fM-xIqzKGuM5AZm8kIHfqLVVO0aMLTCUwvAheHViuxxhU6n9wIl4yGJL1yXbOOCelbaJ8sk6M7F917fdJOfdUsYJpV3m3Vokjmz6LjoTDhWonvyncR3KLDtg-7CJDD3-PkS1Wp9hfSarmxyA5SCnSxgb2iavnXDbjPVdzwY_WU4WBvNiX-BBf-WYgPexfoq2ipCzrdWKGyPP2GtsZ2LU0YuIRe4Et3B7Ray5acR6JNImpDvO3kOP_UbQs5aEvnvD_talrqPZBGdxy5yx6PPPGJlQFvLrMM9SbeLquMkMaGBiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=MXg7W6jNdQar9exdqUKEE5N5xZAjCiayBtCkWrR-n8KG_s4tDOKatsmeG167tNKEBNxFnfRFog1DEl5VfJ98U2kMWDpXTKDhiH_vx-nIuP2FfydxIuze64GG-s3gJw9WaDk3fw-z3a4P20sKfmDsyYoteHvcszZYUu8EbSN9skBoMhI_P7ROgu8L-twbJTVCWh9vBqPAYmSvOoiK1sA3NoasRwMKZ8on64AEk8AU82LEClyERX2JrgDAkio988R2yNj-M7MbqtKRM4AFb8TCIOnwR900tctli_Py4ddcUNhGd29z2vI3sqCit1DrPeso9FOyae3JfVtLeG_nuXDbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=MXg7W6jNdQar9exdqUKEE5N5xZAjCiayBtCkWrR-n8KG_s4tDOKatsmeG167tNKEBNxFnfRFog1DEl5VfJ98U2kMWDpXTKDhiH_vx-nIuP2FfydxIuze64GG-s3gJw9WaDk3fw-z3a4P20sKfmDsyYoteHvcszZYUu8EbSN9skBoMhI_P7ROgu8L-twbJTVCWh9vBqPAYmSvOoiK1sA3NoasRwMKZ8on64AEk8AU82LEClyERX2JrgDAkio988R2yNj-M7MbqtKRM4AFb8TCIOnwR900tctli_Py4ddcUNhGd29z2vI3sqCit1DrPeso9FOyae3JfVtLeG_nuXDbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDlHE7orMB3GAKTN8EaWtPqzNlB2hHigtvPs7VDzxE9YL6JcXbgseSmaQ4QVGQZJGzRRhO7Pdi-jYC1iYuV2Nc2dWLgt0nBD326d0vFhI1Qsk1zc9uXMKZ8VkGVytuaRlGgQh98_vd3x7kxOF2mg5JK6kn7mmCrJn-q3_TaQCCiPYB8Exjy-aW1VB-GTJftuufM1kjHGgl6hvvDR_2_amaBOQdBmy7CjWn7vIYr5FI7hBQ6Ob2N3kseDIliJ6VV-MIwp_iAvuTrQ2i3uqIHZPx6pVdAEOjlARz0W3K6rs6zlDK5kOBCsoFfMlXNLkwU9NNbNACmqJuj8Cb86AlH_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7oAzsJRu6kiWK2fBv2az0j3B9zd4OUGmnCAl470OO0vVVPMc7-1Yt5halXEEdKN16_kQzlgRcjC1yfy-RW6LFmUhdARuiE1sSVjTAi7hAGEyzUAl8bmPw86-HNNRukjP2UaYq1iGlN-qvNi8zahBghWBQDlntDIBQGWpYSZpGESl5LUTYj0b6ji1R65HNG5FRPS1sVPSwv3nz9M4xHd47rI3UElx6_JLIsXIvxSTC0unx8FctBQigZKWc1e2nKecHNG0FfP9Rkus_uyh0e5yxY6eAQfV7ewkm5u9SOjbSCU7LoUWFhTSS0ugGqjESc_wKklRfjqSHiJ5jUq_cy41Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ut_denekcKXYeBamQkc4a6d8TRKZWPmZ00WkdMLoMkMp0skZO-gm8RjqsidnqnGfIm08ARmp6TbONi-m6I6NeSHQRkv0sJn9w7WmifojvqjZ1FqqMenQll8U8VXtpyrq7tVtvTHQ3fLCM4i8aeE6OQNg-gxPf4sZaXutoauUXlFcFtBr5fdyOyvEIrj0pgeiZBPeUf62k09TyekffLn1s1xESM1TEmDfhjBg88KozKzT_KHdbfVqLpc5inDrp99NiIhvAVDij2Ext02p4OD08GdpgtfjXTYM5VtboCGzrGIz7okFAZsc9vQ5ikVMacFXgH0OOgENXvr1dH7ZX-J8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ut_denekcKXYeBamQkc4a6d8TRKZWPmZ00WkdMLoMkMp0skZO-gm8RjqsidnqnGfIm08ARmp6TbONi-m6I6NeSHQRkv0sJn9w7WmifojvqjZ1FqqMenQll8U8VXtpyrq7tVtvTHQ3fLCM4i8aeE6OQNg-gxPf4sZaXutoauUXlFcFtBr5fdyOyvEIrj0pgeiZBPeUf62k09TyekffLn1s1xESM1TEmDfhjBg88KozKzT_KHdbfVqLpc5inDrp99NiIhvAVDij2Ext02p4OD08GdpgtfjXTYM5VtboCGzrGIz7okFAZsc9vQ5ikVMacFXgH0OOgENXvr1dH7ZX-J8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm0VijEQ-h8USwe4k4KbXASBd_MQ3DF7ZVIobqnhSdcEume_cgoy8fdZSl1pnA87cJ78VVu5VZQYeURf88624EW24jgxD0mJdz_6dSqyvPWuZKqFnKff6bLf7iC5OoVzqTAN3GcWCgG5YhvzNYzQ9ZsEz7ACQfo026_IMbKlL9ZktDmDL-yZbZl9jyZH2_dALUX88khwBP2opJ-s-HPX4MYcjtvh1nTagx9UKzxl-D9eQ38VqYrqtlB-i9FZRA0JN0tDvlIsWdcEy18EQpoINv5NreWlRts-MMzkhYOX7BAGj849TCDV8aOJmnpOZgPSpa_U_oe8tt3Icf6uK1ts3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShqsjvdNK4AO18dZKJXsAcAkHgq6mz9z_OqAzD4DqVEWDadI7WzpRX6J6ygoso0n3KzZmHWwEQiNx1WtaiWPp5mcL_LmUdeYv9TdBd0Cqi0DkCC2Xk-12aB3J1TtuwVjRLPG6bxwW5nvEn7wwp55OZdp1VTtSdmtOHtBLGX34GCeJhfS4hoFlRgACkw6sR2sNyLVcOyBRJuXyblU2ChusXLHKp8JCDXTqvBuNOW3MszlkpJgW_98CzH-z0UP0nO7N5XskRlfB2R9HdmC7dYyFligI-YLxB8u5Adt7icm9idkubQZ5ITjilEWTL-A38LsjmLJQ9jzQyqS587lxvoNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlj7Mcr_oCnejW1TJgAQAo2jODAT1cJa8jodt8zM5QTv_H6mt4yg9GLmTKHi4JoydxlTxcH6z6ZMylruSIAOjFfZaJzRTZI7WYwhVf4H0_XpXfeAIzEJFXIqVL1oTHEgorGPO0KkchaLN7ff5z8brx0dH_M2vHt_vaqHHRKENHMMDl7JhJcZkW-GI0T25A9uglP_Xk2LatMGW7FDHL2RC15DfXjwsr7FjzeAwFbmNPe_7T76SgQrBwjKUukqk35dQBciFtK3Lj-tQ3DQcYNV6X8-emHCPb7FgzNh1umgZiOzMA4xm3CoDw1acGsJUbGztsMbcktOzIBeofvRlw4WJA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=LefY5O3DqgbnxkC8zPYW41YxgloZ3YUA46Q7JBpArhBQqco6DtkdzSbnBsZ00MS-KglQKwQAH2k6RAYvHsWN2Pz4ZPJLXo6AxXAgagwXEqoofYLH0T2VfFuFnXt52qD3jDIgVyCfaWGhOf6Ab0ePgSZQZOkZMaYfTq1EFneqUe5RSlh5p28nlUK-scm3zSyg6RkDPNxvsmQ6R-A8GdCblt4qub6c-c0plomuTkkJSXfUFeEk6ZP-NfCOU_q-av4dexb53ePyR05dGW4KvS5GUZKT7ALEvOLzxDNUteTKDXxGUWB9bPKAT4UVoq17nMoU0iIYmpwBuUhoLyzSMNxWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=LefY5O3DqgbnxkC8zPYW41YxgloZ3YUA46Q7JBpArhBQqco6DtkdzSbnBsZ00MS-KglQKwQAH2k6RAYvHsWN2Pz4ZPJLXo6AxXAgagwXEqoofYLH0T2VfFuFnXt52qD3jDIgVyCfaWGhOf6Ab0ePgSZQZOkZMaYfTq1EFneqUe5RSlh5p28nlUK-scm3zSyg6RkDPNxvsmQ6R-A8GdCblt4qub6c-c0plomuTkkJSXfUFeEk6ZP-NfCOU_q-av4dexb53ePyR05dGW4KvS5GUZKT7ALEvOLzxDNUteTKDXxGUWB9bPKAT4UVoq17nMoU0iIYmpwBuUhoLyzSMNxWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ICHZElKeoNYCP9qRQdP9SZZx9LImKte3ldA16xfFTR0svllBkBJbI-2gMUjen-8IdAk1oeeetI4Xnp-ohoWKsUtwW4YGLeVk5-UYE3KtV-EP_hj_2RRirG8NFzOvKSpCVkCi_7Hg1LqDmNFi75so2MvvbykdYqQSUsw40RD6rTO72v4UcGzf3WxSs7go0BFYnfzDF8gMpvkdgWas3OuUIaAG5qjbxBbdg-8AKrBpdZT3bucAeCefJXeVeRVCoCF65ZRNY5c69Z79l-9NO2WI5dFcL5TTBWTVsWw6Q8EM5Ph48YD_kwmMPM0ryj478_UgC4yzuYo9KukEhOe2S28a6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ICHZElKeoNYCP9qRQdP9SZZx9LImKte3ldA16xfFTR0svllBkBJbI-2gMUjen-8IdAk1oeeetI4Xnp-ohoWKsUtwW4YGLeVk5-UYE3KtV-EP_hj_2RRirG8NFzOvKSpCVkCi_7Hg1LqDmNFi75so2MvvbykdYqQSUsw40RD6rTO72v4UcGzf3WxSs7go0BFYnfzDF8gMpvkdgWas3OuUIaAG5qjbxBbdg-8AKrBpdZT3bucAeCefJXeVeRVCoCF65ZRNY5c69Z79l-9NO2WI5dFcL5TTBWTVsWw6Q8EM5Ph48YD_kwmMPM0ryj478_UgC4yzuYo9KukEhOe2S28a6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fDz6Z5bF8zNXnqT0rOailWFtUsZDsVcQZenj-kS45fuSroERSSFpdSRNRzQxpfw-SJX83AIB56n5tdRXrft9yXHVTAdw_afv859TkQUEBORKu1nv8CKjI8JWy69NvE3PctC7IcFk_I5qhe8M-jAuVRvcYAsPAO1dJc2ScPlpXXcjcdFAfK5uPyzlHtoG71L4kLBj48ihu62slOTngY27aeRxQhzAKJq0VgCjziNqGBz1YC9YuaO_fZOhOLKHdDcQTUOlW70snjgXySKfwaQUIidKiHrkPQTqP_2HySJOJZvFj65NXcrIcLffc_70vNxztretMXOZVZWrMzv8VFbFKTpL3fCNtk8mJ_EunWkBAtD2T-4R1c8kOneQ6mOQDuN29Gf3v7hi03D2ZXiMWmZO4MrXgbm4pN99vaznRjSfl4G_5FZBViE3K7vtLx1frd-bOT0a7zcWNvZGFMdbgL9b90Qh8dz07MfBTR8jg9jK4crBp1vJ8eDvWE3scM7NA_737fOxHMeGH6KdgDSLOQ5FqtCN6OC08rVJLjSLQn-2OPMkjUFo77UfkROT_5XzFPUBC1-N-ZQanPqC39G9cBzPdMMdIwvGh0kSMIiiKYH4i89omaimoJ6QUWJ8GZ_nF3m_uwE3yoEzmoWMcVohp4QdxRYPOVrSsBbUW0V8EKoQb4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fDz6Z5bF8zNXnqT0rOailWFtUsZDsVcQZenj-kS45fuSroERSSFpdSRNRzQxpfw-SJX83AIB56n5tdRXrft9yXHVTAdw_afv859TkQUEBORKu1nv8CKjI8JWy69NvE3PctC7IcFk_I5qhe8M-jAuVRvcYAsPAO1dJc2ScPlpXXcjcdFAfK5uPyzlHtoG71L4kLBj48ihu62slOTngY27aeRxQhzAKJq0VgCjziNqGBz1YC9YuaO_fZOhOLKHdDcQTUOlW70snjgXySKfwaQUIidKiHrkPQTqP_2HySJOJZvFj65NXcrIcLffc_70vNxztretMXOZVZWrMzv8VFbFKTpL3fCNtk8mJ_EunWkBAtD2T-4R1c8kOneQ6mOQDuN29Gf3v7hi03D2ZXiMWmZO4MrXgbm4pN99vaznRjSfl4G_5FZBViE3K7vtLx1frd-bOT0a7zcWNvZGFMdbgL9b90Qh8dz07MfBTR8jg9jK4crBp1vJ8eDvWE3scM7NA_737fOxHMeGH6KdgDSLOQ5FqtCN6OC08rVJLjSLQn-2OPMkjUFo77UfkROT_5XzFPUBC1-N-ZQanPqC39G9cBzPdMMdIwvGh0kSMIiiKYH4i89omaimoJ6QUWJ8GZ_nF3m_uwE3yoEzmoWMcVohp4QdxRYPOVrSsBbUW0V8EKoQb4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=uFe5tIneo5vxIQrzdqqNXarZ7agOpwt75RETZMEJzKLxIdlIk0Rm2hRgXmISMe0PCWPb8S01jZDzCPBNkjFLbdZ96CO2qqnjLIYTyNEVGTdKHCgFHV4Uo9N4s3fo6pd1D46wkYQA8W712CofDcvTsyRYZX9fyNHVBXnelci9vOWOrIJ6S5MuSMbLwhGFF6dZZclCgpexkNDjjVXW6Z5YK46Kp87fw4d79Yzv1gyc_ZKkAgl5pbtweXlkksAQOjcIbsTo1BI0VM7IkQRfNNFjp6lgIQ2RJRzpqP8ULIGkJBEMQXWTRUAWYWRHyosb6mewzQRJ_aHahNpVVQVPXUDiEANuKoTjLcPvfFbsaTMidACmjzSP9TWgICaLsZOZVXG1f0-H6O5nXZiKY35a7DUUOwE1RxYybskUwTREDmm4Ay-ofwAgWX1Zm3tyFybPa4noEfw8plzWLhZ3wmyma4KO-399-LgsWzlTJgbmnPlC_XO3LW31VezbAnoyczzSQ9WF0TsYjtvhw_zbUw0h0Gu6k9vRaekSqDaeR9TBJfbLI9MROTh4soNywE2kLEr2RSYP3goQUOTjItNn8x8mGQNd2UTQU6HnuqVYA_Y2CDfvg4GXYqxk6F064_JyOOJu9VtDcEpa8lmeOSmTjqWx49pkcjZc-Wr9dpYCVbo8btCnR4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=uFe5tIneo5vxIQrzdqqNXarZ7agOpwt75RETZMEJzKLxIdlIk0Rm2hRgXmISMe0PCWPb8S01jZDzCPBNkjFLbdZ96CO2qqnjLIYTyNEVGTdKHCgFHV4Uo9N4s3fo6pd1D46wkYQA8W712CofDcvTsyRYZX9fyNHVBXnelci9vOWOrIJ6S5MuSMbLwhGFF6dZZclCgpexkNDjjVXW6Z5YK46Kp87fw4d79Yzv1gyc_ZKkAgl5pbtweXlkksAQOjcIbsTo1BI0VM7IkQRfNNFjp6lgIQ2RJRzpqP8ULIGkJBEMQXWTRUAWYWRHyosb6mewzQRJ_aHahNpVVQVPXUDiEANuKoTjLcPvfFbsaTMidACmjzSP9TWgICaLsZOZVXG1f0-H6O5nXZiKY35a7DUUOwE1RxYybskUwTREDmm4Ay-ofwAgWX1Zm3tyFybPa4noEfw8plzWLhZ3wmyma4KO-399-LgsWzlTJgbmnPlC_XO3LW31VezbAnoyczzSQ9WF0TsYjtvhw_zbUw0h0Gu6k9vRaekSqDaeR9TBJfbLI9MROTh4soNywE2kLEr2RSYP3goQUOTjItNn8x8mGQNd2UTQU6HnuqVYA_Y2CDfvg4GXYqxk6F064_JyOOJu9VtDcEpa8lmeOSmTjqWx49pkcjZc-Wr9dpYCVbo8btCnR4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tqTWenc305X7ldbDDBCoANKtotgrCcbw-SJ3nbjH_GVCYLTo6jacx64JQ1QQLqRwebOJc2YXvwyYx01blLRkkn7A5QfzV6qx9i_heJOHZLJGG4BcH1-93H1okO5es56qd47gnTmgfPTJVDkUW6duOK28beOWBfLBmNZpy7js5nGRd9dU0hgTxAR-V7_OO6QOfZ4PVP1nLv8dMVQOyFca3dPZs84boFaIAGqzSYHYOeENJeVIcJ-za8BdKSmvDT8ndxl3t5v4wZsszWhkFQBaUdzIZoQgk6nSvOiEX5C4cKFiGLTHQZ7FlESqTYM83mPofZqdwpTUELwaS3ga-mHalA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tqTWenc305X7ldbDDBCoANKtotgrCcbw-SJ3nbjH_GVCYLTo6jacx64JQ1QQLqRwebOJc2YXvwyYx01blLRkkn7A5QfzV6qx9i_heJOHZLJGG4BcH1-93H1okO5es56qd47gnTmgfPTJVDkUW6duOK28beOWBfLBmNZpy7js5nGRd9dU0hgTxAR-V7_OO6QOfZ4PVP1nLv8dMVQOyFca3dPZs84boFaIAGqzSYHYOeENJeVIcJ-za8BdKSmvDT8ndxl3t5v4wZsszWhkFQBaUdzIZoQgk6nSvOiEX5C4cKFiGLTHQZ7FlESqTYM83mPofZqdwpTUELwaS3ga-mHalA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjxcCu4SoK9uroSWzCW7o8RG0LN0-9C_v_wyhqILfrywNY3mAVQSB6URlZC5XHRHq8gV5HhBdYZNei-54vY-0SLQLX0pQVeIGBmUmLTSrJUyGoPRN7Wa_JPS3DdQI2IPaZ4hYDMvseeVmzm4OqMwClDJgapp0avQcx_BDI-6CRLl55OnpxLSTasd9aZxr6CUBtLK8v-W4-mAAuONUoDNQxiF7_G84R2-whwScftD1dmn4Xsr2yUxKP6t4GzcuSUxv4kxk2bfk5_qTu3Cl3X5hI_obkb2ITNQtq9z7-sP83ffhHC51T_7rL7gYHOUqVWSxXR14-OJoatvrZSRD7cEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=SpzZslKNR31u58K4SKSKnxjOww3_IRzNXQWEm3zPFQCex0GjKNxe_A0RzeFzAc1cBUrOVif3WKXv_tVE46mHdEiRSBDOFWd-yCjb-WBmn5DfLYMXpAP_dyPqapI6Ijwf1HthlpOusrpuqVdG993Ip-T829GkW3ZXjDq0URJ-nCQDrwU4LPWPmuTBglyqdUmX8oJhQtF8Cxa6VIlAg2i99nmvGEpo3SItjx4QcaOSQqPC9im2eXgr8Ht9Yy7X6qiKDKZ5Y-kPq2yTGMnDArWcg3ZfL03hRMK0oBWKbhEIA5TdA6Oo5GY0EtgHOLme0aXtGCXDuUL08EOV-mqJh7B8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=SpzZslKNR31u58K4SKSKnxjOww3_IRzNXQWEm3zPFQCex0GjKNxe_A0RzeFzAc1cBUrOVif3WKXv_tVE46mHdEiRSBDOFWd-yCjb-WBmn5DfLYMXpAP_dyPqapI6Ijwf1HthlpOusrpuqVdG993Ip-T829GkW3ZXjDq0URJ-nCQDrwU4LPWPmuTBglyqdUmX8oJhQtF8Cxa6VIlAg2i99nmvGEpo3SItjx4QcaOSQqPC9im2eXgr8Ht9Yy7X6qiKDKZ5Y-kPq2yTGMnDArWcg3ZfL03hRMK0oBWKbhEIA5TdA6Oo5GY0EtgHOLme0aXtGCXDuUL08EOV-mqJh7B8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=v6BzQ8ir068gDG-0KfZr80l3MFyiQSVLQicOCnNxNHsIjVBfNheNN57SnfJwNIVrmKVp6qQwEDj5tre9dC7OnbGbibrQccKGcspszGjRhThHRqp8wEB6m63sbg3GaEaX2Y43Qn-tfVK39FcSCWRTTfZmVl4_wA3JIShfQxW7MoaAcWT2S-W70J9arKnaZ2Ara0_dclSZ5eNh6FSwG19_YzZHknIWnXlhYAr_TGtYy7eUCuR5H2PExIAb8UaM7UIH2u6Rt_vH85dVp6iSzY6EK5K4C3gDiLMVHdLfZhM-2uKYpJ3W3RBU2q02gzYSOQFRKZfagLS9QIf9Kt5i_98AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=v6BzQ8ir068gDG-0KfZr80l3MFyiQSVLQicOCnNxNHsIjVBfNheNN57SnfJwNIVrmKVp6qQwEDj5tre9dC7OnbGbibrQccKGcspszGjRhThHRqp8wEB6m63sbg3GaEaX2Y43Qn-tfVK39FcSCWRTTfZmVl4_wA3JIShfQxW7MoaAcWT2S-W70J9arKnaZ2Ara0_dclSZ5eNh6FSwG19_YzZHknIWnXlhYAr_TGtYy7eUCuR5H2PExIAb8UaM7UIH2u6Rt_vH85dVp6iSzY6EK5K4C3gDiLMVHdLfZhM-2uKYpJ3W3RBU2q02gzYSOQFRKZfagLS9QIf9Kt5i_98AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2xBb6_cDbsMo99qmnwF8gnL9qkRZUxS-7tOoTK7q2DPKY8Xf1FwXc1JzJiD_k8ByDC_zzqIBN9HEZmnDjn9yMqjH-SVqUI85oGCDljJdbwe1iBlsGjPeVUf4c4PlyljXoCpUFBamXZeJwXoWtgZCUlhclcdU8NbZpalSAgjqfpn31laHtgfONQk2BzvjGcTm53rAemgA_8AuKdJTBbMqx6zYn1ka-Gzsv40bZGeYMryhjMRmoBqcRdZn0iQ4hPfrGVdKD_ZeuKmJxdnwgePN1wQ4a2O_pvqlH6Wah5bOGdjO78cF2-aYQqfjBpan6XbmxSiAtpCAOp1ihvn3Dk1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhCnv9OnOPmnR5PmLxKv8944jvRLQIZEAfe6BHJ0V-rzshZs80upaf4uiVoIWm-lF_Na9yBHRDW-CVEY_xt5RS1n6q42CjEiEGQd7l84fD-1h2cNK9gcHOxI_3mAdaGfCmo0hDcsEPZPmdn8-IBhmuogNJN8xc-k9S-B0pvhQiFIzL414UFwImZ4gkq1tbVbIx6lZa2h1VpF4RsZI4ozeG9R43kSZO4e24ZGwwmZ1QK5ruKCHJypGQoYps3UDDmIjfjFJyRmm7lVF5ZubIaABOB9iH9AMKrnrpPQBzUvLAEq4UkkvMMTaS6ibwYnGOsOAqzAHdq1_QLDVXqe1iY1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm6rykHEezu5okBYhrTJSq3gRF_v_l_Yy431C2bxq3hI5F07RwTVDHfqHjTRIiHuiZHBOehXw0p8lWC0W-Qk2Ry_M_I8HMpQLlfGg_MDX7N1WAth-ZuMOpPAGrpTCpgtxRaSTttpHQl8V9dnIEuZ4nsnIMFWJ_8ybD7yF9HNzDS7T6DLpqmQpgWtZm9ypDPYkqQg0tfqQ77h9aRE4WdluZLBK9h3hFIpm0zWVgvunl5dSGapIpGaTUyCF0Nz8ez356tdvcRuCZJ-yB-SB9iR040C_aOZyIyzEDRSwq0FrksG_CQz8BbuHNoQsKypUmlEsRmZTiE6BdMlzFw1aZAwXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixZJkLY_GYdPMzYy-HXXTAutPllC2c-gad1nuczT0Hi4GOyMeEN3giGQwTYlh4XXaEY9X8bmVrjhTH1-KVXFzYzRxw7Lv5UKwVQl3Msy-Rce-ZrTYhOQQ6dgwzZlJgyQjF10yr41Vi9nLEtasr0-yzuQLZvJ3ASqkxGCJHknhRKFKBKOhsmi9lXE_0mohOKFzlVhaJlc5-ULgjaM2AAkfpsmgN8f2M-Mva3RpPqok8O1RJ2uy4J5tdsVZ-q42S06GfjkRP7Lfrhz3wXlkTu7rnMmyiaXH6tSA1xG-eKE2KtpWDRnIN5WhwK_dkQbH-h2PBZtHn5sd779_jU-r5Cgqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0-NISbdF-IO7ffoKq0Iq8gsus8AuBKqA9DjJgqmVF1mdLFeaoTMhDU6drneesHIaIFnzfh7OfaLw4sxATDUGjz5NOY9hF9slgEW7bcwlWlkiv7nlYe8ERI0vCVuYOsd7XENPJL5yqUMC9x8h48KXa2weqtPLq3n23oG2flHAwBC__mwfTocGakxyAa322qsZS6FOLL6k5f_YhTxuXOsQzRSDVYxmGL95vsVZaNURucMwe3Z9ltVleqqor4ekoLlDSs84n7JQKU7XrMHJ-i83KtB24IDNHTpA7Aee080IBu35uXRWXMc1EFLTzPbcno508VZM1L3RHy5JdLZtvfuGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fga8iOaB-wDSq-aAn_bgBN99CO3jOCRhRs_TQx7cdPUmS0AuWldogbRYMeG_arGf3LOkONc8yJB3mZhsLiXhquUN-TreJAxRPC2rgJp8z0yOrk0KT0Gkh4FpuOHOsNvKiZieiIieFlRiubTRySgzr1QDDk0VJIe-WyWvnREOSA6F_3QB5gmvA6rXOe1PRocm4aArjc9L8omwDPjZ7w7f21Kpu1NmOoqnACtwVtSMebvOEj2nacxWgAKdAi1PFt57xcuCXpg5pyRCtffznM9LvHlCgfn-f8pSM80xUklROpUa1BPcQ8NLjxjcYFBAom5GqPEO9orIzM-ieN0qIV0g4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1AMdpqL43bcaKduNACFM3YjQAybVPFIXdHbBXJi8UEfDSfiV-ngHgoAoX3FwBVnJfIQob-EaI8oZ2AQyjOE5HfjapuByDKCiZ7JZGt19OKsppXVJJpprUD-AiKWvMypEwAiXE7QpThzj-80iHYReWCJCwrd2Q01Cm02CmKBxpgNTmP0pbQDvSWr6Ind_Xr7UDLVgmcvjdoOswC7XNmfF3_xXeH7FoKRydnG3WAknguxrjmjApWllZ9aWrE4V2prWQ-BzDEdTvBB8NDoIkuQgk5wjogIocffReWqBGDZ_7a98DRlUqaI_1_GlZCGhUw-cFdN8Kzpbj3l_JfGjEI6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7aaqIZtXEUbDX1mBygmVUK9a5QJTMH4ETtmHQxbjFrlJji0LLF5hbsJeua8DYGtBTYHZqfiLPVfejwAaAy12HWkgeCMyPBvC1WeplJq6cBGcYrtJEjlFirQq3KOl9xt_BS1owFGuEJuLVzxpfacAriJLcREDQcr9jBBTweQXgJdCT9yZVwmLmLWJmKluRJa7hqzAiGDdWvwYNMPszvnJ93EtS97qvjdENlD7G_x6Wsn4YY5KQS2Z30FjjFHQw_8HEZ026lFFyMGNE_t3kBm9xCetvz4yEWrIBZ8lqnQH0GrG4fFQwh2-VS82hHB4dmMcPCg9nJVyk3fdz3dJMOqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElCjzgcNn1_aC8J5Rs4eWnfctVPrgxdaPoJdCZGRo50BVVbDNkUQq-bBWgjkQgW72xzCl1gyqUpLPbvLoG-TzUWwrHiiqiepahIm0AB7spRrgVMUtK4_dPsfFPRAeKuV9PXWDK1V7zuxEmjI3kCoao6ZJzD0TA2HmY_3ZOVGXDKWv8U4VKyxBqHbdxtFToNFiblcC4rOwU0Unp5urKu3asR3n52l0gCrNTpv1fHy-UXQ7OcxIZS-JBfd7LIAvbQhOvIQ_TVumEiQllVLb6zCmRd1uuhIkw8PfpOAFLyNBoiNtq9aoiGjC6pGKY0x96PXJm8NJ8xoCP1bs5ZIl785iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrgR6G13g3pZWWKoetBsQqDuD0kJYU0S-uP3aHbNGfEz2bFfRtsFLVlEFpLmy-w8y2DJEi-bwCvv9u1aqWVJwrVaXA8GVfOW8WirHoWOak9_hSGGQKdh9AQ0VTNfDqOJku4Sd1VsG9NEEzskXDD6wrzBUcE1nIe9JVGGIeubaUckbpapdClYl05yg7D34agS7I4dbNuAxtflqbkVj0oxTysa-pWP300zIBEF2Y6oP98LBG6Mo7e1mx9aNcyc-2NCNpZw-o_sB0DLaEMBvFLsMc679SB-60U-5Co-W6P3FzT77ZBUO4UP9xReUPvYTxMbY5actY4jpETYZPfmggdVaw.jpg" alt="photo" loading="lazy"/></div>
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
