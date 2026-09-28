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
<img src="https://cdn4.telesco.pe/file/TnPraY2FCYOGaAWYQVVPuKAdO4LnYxurvatDaHwk85tOlUhKTrNuV3qIxV6m0BQO1umIh6zrTOnNshR0Ugr2Z1wDtc3YB1L5nN3_c20m3WEt4wuIwCEC-hMKbOHrCDY1Y6kirqBI9ZsEF8NpeIe33mDfpnekPWmooPyvT2pEU5AaF3P1G9VIWVcmRT6R4pDf1Rjco0Gxkq2IwPOQC8tSkEWMotzPL55mlFVahU02yQs6QI-FA5HaeWBzpwNoFl-6vC4dPhjjgqmX8Ke6NJZ7LXy6vDdwc5icge0ZyN4NV3MCX5f6drbCKIDRljTAv9QFoFYsy3-1Bzf3se9ZQIlabA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRfqPP-OFb2FkeT4WVYAWqS-6ymgO0ppSlGMzs_tlZPqqmCfYkX8bDHqpnwGXNHdUkd_VQGUV9SrS9z1-OmvTJrsLkx3jEoKLq0Tiw3XcKUCk1fFCjfQppjQPVLhcZPWvTxf-5467fwb13nDZcLzeiTlKNIr32NB3nS25xIQOzi6iCIlXwKf6BcYEpPq7sw-ob5f1RO33OH0woBPmFVuCrMXBAg2OlRfYWqy1UOsMzvJX8VSW03MSyT0ueKNY7K7B90VvNsZoIocVCf-9RXMAxKrolfoGTz_Ua8EJp6excTrx3tD30WsagW3MbpvFxfBnceTFmeEnx-nMoY-nJnhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLr6PtJKMNyuB49FEOCfaLPbaMoZzHNPPUa5AfdMCRmla30ryaQqm3lDiEpHLlK0Enr6pfSdyi4We8qy-AmptUi_n6Bolx6PI_oiiALcWHcQ70n0ByDsLB0ydB5rGM2YzyujjgY3VuI2jmG8VLRjG1-oC7etNLtfYteuWN5xuV3QCbe7pNEthPQYoQwFzbl2YXX9BefTacykTFitimKkOVVckLpM7DMHgvx11sA6pl1gTt9fyjA-RvUo0saiFlTj2obLnjhYsPcQ1JBtmGi-kwhMuFnON9YB79qVc4z_VTIGqzns0Lo8nVyP9CBLvLCsqAEldUErkeQYFaCRF34gFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=ahFLedcwVzS5YryEku8pAEPU8bFwhp_mYg1uH8TOwBNI82kCqfcC3IPKVveAaHjm2OnuJEqk6EUZay4HOnakxpEfhMVq0zTlDLD7je64zknQ29DOo962AkmnDPaepuWswRzaOkHjKo4bK0FR8UxSSmwSYufWoqaQ_EeRekzgNx-_CtZLoHf8aM12U2y4r4zJXuVwm6AmIq2XbPIu6S7S4_VNnILiMVtBmwCIryOm9SWTtSncqTuh1I8dbUKPwrRdv9sKA6JWasgBNS7PvDX5wy0fcPFgxBX07xENAjJbfkP8U0xvvDH2XupkvrKy-bmypnRThM6yqmS679djjs6Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=ahFLedcwVzS5YryEku8pAEPU8bFwhp_mYg1uH8TOwBNI82kCqfcC3IPKVveAaHjm2OnuJEqk6EUZay4HOnakxpEfhMVq0zTlDLD7je64zknQ29DOo962AkmnDPaepuWswRzaOkHjKo4bK0FR8UxSSmwSYufWoqaQ_EeRekzgNx-_CtZLoHf8aM12U2y4r4zJXuVwm6AmIq2XbPIu6S7S4_VNnILiMVtBmwCIryOm9SWTtSncqTuh1I8dbUKPwrRdv9sKA6JWasgBNS7PvDX5wy0fcPFgxBX07xENAjJbfkP8U0xvvDH2XupkvrKy-bmypnRThM6yqmS679djjs6Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=UgsTrndmpljjO_A4Uq3l70U_0-3poavg_ta6u8unf84JkZfd03oaF-Ol2_9uj28-O391NfxT90ZGGvaDK98W0c6z2kTmOG6UVv1am2JsjL6kudGGNStwPmrkb1Z5prRe2zTdV4uYaUmPS3kp8ns8m1bXCq4-X4XrJajrvkgG4zli7-mNjla_BlQ6YNKGlq3d_xbp_pcYB25RvxflCArZwEM_X-nTZt-_XBpdBU7xP1hPLw8BOdDYvXolQcYt5ON0Vpe6TyMbQ0aFknKbym9_pwm-aTBxRupPQJd9PR7_PEho1xcJrg0WLxDM0QcKHllZuVOteENlmxQrT91-589pbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=UgsTrndmpljjO_A4Uq3l70U_0-3poavg_ta6u8unf84JkZfd03oaF-Ol2_9uj28-O391NfxT90ZGGvaDK98W0c6z2kTmOG6UVv1am2JsjL6kudGGNStwPmrkb1Z5prRe2zTdV4uYaUmPS3kp8ns8m1bXCq4-X4XrJajrvkgG4zli7-mNjla_BlQ6YNKGlq3d_xbp_pcYB25RvxflCArZwEM_X-nTZt-_XBpdBU7xP1hPLw8BOdDYvXolQcYt5ON0Vpe6TyMbQ0aFknKbym9_pwm-aTBxRupPQJd9PR7_PEho1xcJrg0WLxDM0QcKHllZuVOteENlmxQrT91-589pbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jZuzhUaXNFFtM47QKe-Gx_hmBDjhGhnNJW-gdmiJ2hMsxk0CLGxHdPSWi4JB597q-p58dXIPL53CP6EBE-YiGq6Cggo9VxipBiZKCTLg4YvmzVQpnccH_lM_aQXm32mlXutmuUkUW-MyCcrzsfqDqBEKz5tMuVq18Y_y78l1VP7gg5mhkcbkQl614BAuXjapBOwWrNxhouZdkAjHksMClPojX4oewz5hjmRClDDZF_fEQh3jyf3Wjb3NxyLrVengFqiVgXbWjGE9AlGZrOW4-V6RhpcBJCUDyW07le6dHfzcaqjkF4spqxZh4sE-1XPQRbaEBngIzXCWN6ub9eFpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jZuzhUaXNFFtM47QKe-Gx_hmBDjhGhnNJW-gdmiJ2hMsxk0CLGxHdPSWi4JB597q-p58dXIPL53CP6EBE-YiGq6Cggo9VxipBiZKCTLg4YvmzVQpnccH_lM_aQXm32mlXutmuUkUW-MyCcrzsfqDqBEKz5tMuVq18Y_y78l1VP7gg5mhkcbkQl614BAuXjapBOwWrNxhouZdkAjHksMClPojX4oewz5hjmRClDDZF_fEQh3jyf3Wjb3NxyLrVengFqiVgXbWjGE9AlGZrOW4-V6RhpcBJCUDyW07le6dHfzcaqjkF4spqxZh4sE-1XPQRbaEBngIzXCWN6ub9eFpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=FlI6QPD5OIjc3DBpn-OQpPP102oPA1rLM_9j8izDV9s8-HoTzCBIlrkcI9ZuLILShXmG1getqItR6erLTOZqcf9ASgA3PAtj41mkOcI3uoP0QPYlyC1WqcRGMgPOyIxhfnQQtmdG5EDhaVfFBlN3TjfLS7AsfwEymwk-O71P7xbtEsiMLQzt20aEDSRtYpL7EyZ0QLkhtK6_seBCop_8Wt6B3lpwDzettCGdqimxk2WzdYVUUXke-gNGANrKK5Vf5Dz2rDJCL9UPSeOhfZHdNXbtA0SE-l9bnvl-UPigY04OMhk5pQMyAQFs72OgCGPYtJi8K1auTUyhe8nS3Rrh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=FlI6QPD5OIjc3DBpn-OQpPP102oPA1rLM_9j8izDV9s8-HoTzCBIlrkcI9ZuLILShXmG1getqItR6erLTOZqcf9ASgA3PAtj41mkOcI3uoP0QPYlyC1WqcRGMgPOyIxhfnQQtmdG5EDhaVfFBlN3TjfLS7AsfwEymwk-O71P7xbtEsiMLQzt20aEDSRtYpL7EyZ0QLkhtK6_seBCop_8Wt6B3lpwDzettCGdqimxk2WzdYVUUXke-gNGANrKK5Vf5Dz2rDJCL9UPSeOhfZHdNXbtA0SE-l9bnvl-UPigY04OMhk5pQMyAQFs72OgCGPYtJi8K1auTUyhe8nS3Rrh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=JBKI3ELqpQ4DNKmMbgcbebpuFSkk4LG8giTdF6ZB29Y7e9_00z5jr7FOHCj6Njf7F2LUEQsc8pom4lhA2IK7hONr64s9vlHCi771KexxT_dKVmB-OmVFT3x078oHoo1UYHyq6QmgyVR5w_2Lp-8hMfFEWxIbKWnGscBwjasLl8-D8Rws-vkOTWy6e0XzV0pG6DXfHwve__0ohzzutA-dwEyq0swJpqY-SxkzEwrbzGB8mQB3NAULFG7iWqWMsBCxsBIhkVHeIsUgo1xFHiT2nmMjJPK4UMQQYRt4j7wMTzF5K8PD4Pu-YYhpJsT3s9ZxonPaBw965zUNrFGSnAwckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=JBKI3ELqpQ4DNKmMbgcbebpuFSkk4LG8giTdF6ZB29Y7e9_00z5jr7FOHCj6Njf7F2LUEQsc8pom4lhA2IK7hONr64s9vlHCi771KexxT_dKVmB-OmVFT3x078oHoo1UYHyq6QmgyVR5w_2Lp-8hMfFEWxIbKWnGscBwjasLl8-D8Rws-vkOTWy6e0XzV0pG6DXfHwve__0ohzzutA-dwEyq0swJpqY-SxkzEwrbzGB8mQB3NAULFG7iWqWMsBCxsBIhkVHeIsUgo1xFHiT2nmMjJPK4UMQQYRt4j7wMTzF5K8PD4Pu-YYhpJsT3s9ZxonPaBw965zUNrFGSnAwckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=aWgkFLSPEuTK-zLnY5G8-iNEXLcef8wB9r7DWVuQWL0XHjQorYWUrb6jkYlvgbGcbktdeqdxt-Lpvc4RtK91qxC2F1SDt3g1AocfE98SMfPOKDPsFKB9YUpnjOmj_5vf1TTCca7QzuX0FwWV--GxcrlL7TTRJNyv2hNCXiF3rQTZOK1h4wncOJH-LebKgvL3DIi2HgEH4b-TZEWbJfBlxwgwjDYtPNp7lyrKAzbNToeINgYEFldBNUef98vH1oLYYwVpCzN86cbFf9gBi45_o_2xtnbjJqFF9XwWpqvVkPG5NsT32cEwaE1p3t7OZlXjhgpoSlDleGmBmvDRTwVUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=aWgkFLSPEuTK-zLnY5G8-iNEXLcef8wB9r7DWVuQWL0XHjQorYWUrb6jkYlvgbGcbktdeqdxt-Lpvc4RtK91qxC2F1SDt3g1AocfE98SMfPOKDPsFKB9YUpnjOmj_5vf1TTCca7QzuX0FwWV--GxcrlL7TTRJNyv2hNCXiF3rQTZOK1h4wncOJH-LebKgvL3DIi2HgEH4b-TZEWbJfBlxwgwjDYtPNp7lyrKAzbNToeINgYEFldBNUef98vH1oLYYwVpCzN86cbFf9gBi45_o_2xtnbjJqFF9XwWpqvVkPG5NsT32cEwaE1p3t7OZlXjhgpoSlDleGmBmvDRTwVUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLbV8WX7CrQDm-GkboSWJBrimaQ4r1dPQmmxstmj97hplDgmDxQluwKim_TgT3CkV5_RVRwaPUClzmsR5XoGsGQplVMcEsO-vSY5Qj4nolfm90o_qZmWbyzKFDhiuYQUCno8ddpk6dEksNokLWsXoWyg_cOulyaPe0yxwzWvLm__bYAkNVm7XBZQTD95Wkpb2JkipbUR3DGG6tfSuJ2TziTfjVjKXIAXn7ZeV_1A9RaT6vDw2NRFlHih3u1m4KWL-D50Z0RHMzplp1Qk74dgneinUV6utvEjNdjaMzB9zeKdvjQbJ5UIGkz35C8ZdRBW_lSQALwY4cYsgxHU93ODZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heTpWD5H-YvquWoVYxwE6K_TdCJ1SmlWVV1hA1tOEDnkqa9mU77hA4mtLldsFVbHjvEsdCpYe0n7lAZsR5Uu5VEMcniaj6e6lowX6kY4Hn5kt1xsx4kuyHx8FKxGl6JAQ2toF-m6vm_uTSi5fjqedWyVayQVJ9WaIUeXUbKqmJaFgSs9BlSG0v-OZ9KlnkuzC6_axkSJMO84m7YueGXa6jMIXN0uGx0LDji_k5-LuJ0pExrIpzpkJFWD_jEPK2d1zgq_sLgSiamGR4vCelOFnGt4o5IYvIrXWpkIHW0214qMZsHoy4uUVX6k3Uk0xc-VruCuu2DYrJ2f_Ptmo_i1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwi15ds9jGud7dqj7PeA7U5HF4Nvsl9bvBcRyaHDvLwfbF3N5-h2L1HRzDZ_vQVN6ATeMx8pUOB-Yv1kZJLoJIa6dL7ct4ZTtmlTFbPTfuk0k8VtcK3hSdZfxMaHHFGQt1V4Yh9gLmw2YBuRm9bqQu-wl_IxTQ48QRr0usE9m17cWxGwW-C4axb_BVlVxNjsu-r-zYln0k3fiUSmAMFrrqwxRejU2a9bHAiKDy--aEAs9OGqZroc5uTnh0bMVQl1d0revh0eW230ig0a4tpkKMMQ8d1SQ8ZUziC8xCdJYLmq4DvdgIPGZKh7waLu5RuF7l_GQ48n79Jxds9JNFUECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfSCzyHogaR6TOj6w26aN50H3bAJu8w_d84JH_3_ISkD_FdhIjVQlm0m8BETCwxRiuWDN4T96Ym7wtbePtcn1U-Fv-wwWCJtSlkpQj7WvemjGN9uR5CeI8_0ChLHpnfCop1TKeNq6fDhBB5xK815-KccnDkkKaC3hfw8iOFWpast0-ud0cDUQI2QshUKuG-7M3_lBaTCNMk-ewB8Re2uVP0CNhUF2ulIHH2UXzgtX2ZBbQYb9H-Fz704-mCWGEgbOhJ-tfTJf2u4zudnm3-bZAY2-bJi_iK9FzCY83g2IkFrQQvcsTvXHrIno_6gKjNIbe5ZIUorqzgJjw9uVNB6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCpPN75qewa55-ilUPG0SjeRRFl_wBrBAtjrjURwbP68lVb69fDLm31AsZkyAA2C0YYQzWSFLFtGlHID-4I6v9zARkPvjP-yRBdKiBRCL5et6_X2XaagmE-B9TlkUNJMeaiIClgsZlX9EfDpZNM-TE0N8wT2oXN2A5VG-pSht0HgNv7YvCvgsLr4NZf_6PwmuqGrph53z1t24v3dIg1bkRRX5_ZTewbf2J4xaudSNYk1o0xvXIwIFQch21ASY9be2C0cGAwoF2KRbQtetgYth6UKD79B-2s50qQM32z9_ntqjGDkkqtPj7kulFlt_aMbo-CD6pQeu-rPYAtT7mRluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLtRuj0cIeja9XDfSCyXlU-SjFXymLafLVnZW71FudimNNW3LtObY1Tf0quW37Yvia5Ue7GHtuA7DEwVobURBIMx_dbb_AHQlovVNRrbPtMVDS1W2GLsYt1ihSS-rPpESyD4Pu5OorzQNIFLt2qyNoxPcaTPfIQ80K-NBDlTWxaipB4CYWJgLWyao6YvJzeYGzqCTqZfv9JCICyKo1u675xEsZZA5Mhft1ADMhGY4b6bXbjeVMIUVgOjx8PsX_T-gdBhc5nr_u6991tFykht7NC8Wu2RkvzP6l9CUvS-IGQNnqtGs_L3YE8wsQfScKPYDHpr67SXWt_qa_VPchd9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=f7TU_N8elK02hDGa0ULhSd0_jILcPhvkb9InxIf3ZeW7AFynIUwG4zfekDrZiiHJyaXtYZrupwloPqlDq3u0UKawaa25R9a8CsWJta0xEpbu1LP_5rJMDFygRnfTkGQEYcRJfifLFbSIKfM3aKeHZzTThXGJcEcBGJ3iHhKRBzvD_ONiKRi3FzZo0n8s2My93LG9MvEPoQCo9qFWZPWp7UpV3HrzWjb1iCB01U1faDg-FC3u27KpSeKRkDzLSzh7ZzZn_ia-uJFVveL6ntp-9BQKjAeraE_AoyvtgtceGrQo_G3oaued7H1BvWMYA4CkC-KK_ETf73mSbcWs4s5WqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=f7TU_N8elK02hDGa0ULhSd0_jILcPhvkb9InxIf3ZeW7AFynIUwG4zfekDrZiiHJyaXtYZrupwloPqlDq3u0UKawaa25R9a8CsWJta0xEpbu1LP_5rJMDFygRnfTkGQEYcRJfifLFbSIKfM3aKeHZzTThXGJcEcBGJ3iHhKRBzvD_ONiKRi3FzZo0n8s2My93LG9MvEPoQCo9qFWZPWp7UpV3HrzWjb1iCB01U1faDg-FC3u27KpSeKRkDzLSzh7ZzZn_ia-uJFVveL6ntp-9BQKjAeraE_AoyvtgtceGrQo_G3oaued7H1BvWMYA4CkC-KK_ETf73mSbcWs4s5WqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c2QjDoNO1GHQkTkGqQwm89fnQ732OO5Uzf_x7l_tm0JnYmnS4mQYvqXSiiyYVaZmDDFMle5cCRpbgPrJdeD1aVqd2oHZc5T0qaxAtFOm8oz_-sHmAmVm7E5JcuBEiyFYGRJ6ZFZnmgmfFfJWlmILt1bxlEZYUpCWWlYWSABJBtm4jG5k-PvfFsPMZ7dX-MEpnb7e0GfOUOZoIGeW_xrFqLQfSWplRWIsYcGjpzckGc0roqdAQiAIfFcfskdiOFG4f42XDEM6N5tUOhnCwqrl9_RGHx_eAXS0LFWb0yJLoBnkokkgpfByrg1K_O1VHlK_74eBsuuLmPdzuvxpXC8Klg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c2QjDoNO1GHQkTkGqQwm89fnQ732OO5Uzf_x7l_tm0JnYmnS4mQYvqXSiiyYVaZmDDFMle5cCRpbgPrJdeD1aVqd2oHZc5T0qaxAtFOm8oz_-sHmAmVm7E5JcuBEiyFYGRJ6ZFZnmgmfFfJWlmILt1bxlEZYUpCWWlYWSABJBtm4jG5k-PvfFsPMZ7dX-MEpnb7e0GfOUOZoIGeW_xrFqLQfSWplRWIsYcGjpzckGc0roqdAQiAIfFcfskdiOFG4f42XDEM6N5tUOhnCwqrl9_RGHx_eAXS0LFWb0yJLoBnkokkgpfByrg1K_O1VHlK_74eBsuuLmPdzuvxpXC8Klg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=BH3VHWzz-K9kZvMdcGcFfbFb6VAx4PzFIkhIn_oTXi7eGgJMbKLnMqODKRpZKqYrHrLTbNT7k7esEHmr-bY-CY6b7gOoFgbAbQEdIjNdiEG3fcDXJnSIXwuodrYB1HqZwEuCVypg6v1-25rFYwfnELKd60YuKVb8klFSEGIYfwmHiYqtWWfVnzryD1JSpidwNoK2Q639POwZEwsTx7Ldol0eoAHjIcUPHz7WoC1UAAy7V-innz5KzA_kD0KHoYKO-UGdB17hvqYMBVaDxR6C1njJ5J-i5KK9SbbuK-yFMimCoWPzAKH4pOwSP0tMOyvwc-USLg1rnNsDOu5URfUTjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=BH3VHWzz-K9kZvMdcGcFfbFb6VAx4PzFIkhIn_oTXi7eGgJMbKLnMqODKRpZKqYrHrLTbNT7k7esEHmr-bY-CY6b7gOoFgbAbQEdIjNdiEG3fcDXJnSIXwuodrYB1HqZwEuCVypg6v1-25rFYwfnELKd60YuKVb8klFSEGIYfwmHiYqtWWfVnzryD1JSpidwNoK2Q639POwZEwsTx7Ldol0eoAHjIcUPHz7WoC1UAAy7V-innz5KzA_kD0KHoYKO-UGdB17hvqYMBVaDxR6C1njJ5J-i5KK9SbbuK-yFMimCoWPzAKH4pOwSP0tMOyvwc-USLg1rnNsDOu5URfUTjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=ZW597dbRzQhZcF5T02dtEWnyoo2rB2W1FPrawASKBhq84_DEpyvt9JrWwx0NRxqG2MgEDlDWO306LnxqoDVyG7ynL9nlBwFtIEFH6THs3spd0JPKfOz0X4q_YecLsu8f5ws6a2jQCDkDD2j9JcEbw4b2mtG_QeH559rh1BAyTojbrwj6XIZQrccwhsM8rVi0aTYjM7fRdyszt7qgSxUnjtqLOkzvBYfSiX7GEJXcXb9rRWb7H62P3YtrJMnJmM44rQDuFYeDIYzoeTwU2A3j5IkyMAI0k2PgyK2A_mDkG4NyCYycNWCRPR0JU-wOvTUn2zx_qSVD7Mhxy25vmPYIdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=ZW597dbRzQhZcF5T02dtEWnyoo2rB2W1FPrawASKBhq84_DEpyvt9JrWwx0NRxqG2MgEDlDWO306LnxqoDVyG7ynL9nlBwFtIEFH6THs3spd0JPKfOz0X4q_YecLsu8f5ws6a2jQCDkDD2j9JcEbw4b2mtG_QeH559rh1BAyTojbrwj6XIZQrccwhsM8rVi0aTYjM7fRdyszt7qgSxUnjtqLOkzvBYfSiX7GEJXcXb9rRWb7H62P3YtrJMnJmM44rQDuFYeDIYzoeTwU2A3j5IkyMAI0k2PgyK2A_mDkG4NyCYycNWCRPR0JU-wOvTUn2zx_qSVD7Mhxy25vmPYIdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=eGPcsw1FvD3evnEaCjGqP9piKYHvX-qO5zJPHqd9pLsGwkBE8BRO0ms2KG506i88e3aI617jAJ1Xws6Sh_JI3HCyEwQ4zNeA4gY6-nKGKOCki8HHntz_MGxSL2K-3A4Rtw9_mGvM9Hx6zrsL7dGEahy_332GQ8U8gEBBjRiMT0e5Gqa5uYGOjO9Knwz22Pb3FtmKbxny2zKSlBM8gqOx9a7AabKxEPvw4Hu5YjSxa4fFsQ_4Jafcnq9SIaxHk3VgAw4QYEhi4VYCxMlI6iOyePuPV6Vn14mIWA7ye5OImvp-TyU6mfBw1Juy6_84SbT8zDOZX4cLXDrH-DLMJp2IEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=eGPcsw1FvD3evnEaCjGqP9piKYHvX-qO5zJPHqd9pLsGwkBE8BRO0ms2KG506i88e3aI617jAJ1Xws6Sh_JI3HCyEwQ4zNeA4gY6-nKGKOCki8HHntz_MGxSL2K-3A4Rtw9_mGvM9Hx6zrsL7dGEahy_332GQ8U8gEBBjRiMT0e5Gqa5uYGOjO9Knwz22Pb3FtmKbxny2zKSlBM8gqOx9a7AabKxEPvw4Hu5YjSxa4fFsQ_4Jafcnq9SIaxHk3VgAw4QYEhi4VYCxMlI6iOyePuPV6Vn14mIWA7ye5OImvp-TyU6mfBw1Juy6_84SbT8zDOZX4cLXDrH-DLMJp2IEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRRFGaboAL3mNT8sSXpuN9NAsvtOjuqqhfqmCr14bDvTglNiZI6z141cW12vsImbcJnqJ4SQQBOVliSGHB3187D4RLXDwi5GO5q69kzFYdbo2XUx7gi_Syk9kD4Cbwg825twfPEXE9e_EyAMnVjwq-5aqOOSYtzqRxk4DvIHM3V9-7_YQK9pH9i1K3X8yr1gbeEzYpKN2rOIEpEpzyTB97-LPdybEsMjJ2T9Hs9wZv9f2zsnS4oPR8G-zy-EdBRJHKRmseany-DBXP_apY4jh3JRtejFM8oMqg2MKbAaYlrH14QmYl9L84sumbMOAwCpbQTHloi3cSDbNAq6kAwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=I2c8ymcaEn1wseZFePzf0l5YuTgm1ZaGlTJE3Ad2Qys12B24AQ1C0DKRb9mQ6DV2fuBeKGz_D994UfMRRWc9nVW4Ss8xRSbKg4xayOJw96RzWXrZYkLdGIV8IroFNFt0kKlIgW056covGBZl1RAc7hMC6AR6nU71v_NUDrfjZzlZHrItje16OuCGNv92-bbnwdVsJ8tvGLdMWNdoh2_MdgBGJYJJk9YcVxgyoHWXZowV-G8HKrwqHBXp9rHXmF_M5PqNNnxOeIMBe3yUdjaKprNb_vs15pfct4j_fDmLskPuIP2gLeUIXMlrVKwjvme996SMDzPQKu3jVDT_dCLmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=I2c8ymcaEn1wseZFePzf0l5YuTgm1ZaGlTJE3Ad2Qys12B24AQ1C0DKRb9mQ6DV2fuBeKGz_D994UfMRRWc9nVW4Ss8xRSbKg4xayOJw96RzWXrZYkLdGIV8IroFNFt0kKlIgW056covGBZl1RAc7hMC6AR6nU71v_NUDrfjZzlZHrItje16OuCGNv92-bbnwdVsJ8tvGLdMWNdoh2_MdgBGJYJJk9YcVxgyoHWXZowV-G8HKrwqHBXp9rHXmF_M5PqNNnxOeIMBe3yUdjaKprNb_vs15pfct4j_fDmLskPuIP2gLeUIXMlrVKwjvme996SMDzPQKu3jVDT_dCLmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7BVjC4JpGi3LOlJ4-JcTfOImxIuxoRiC8t9UfAx468DHld7IYMJykVm3VPFnyT13bkVwB8g5NwS_Gp6CggFOIF-gC4OfrihMmTZqv_uVkOYZ1Ur58dKycuA2ZMkCI9w6u8ae5-JdB3qMBm4qOIG2XwDXjWVjc4j_PW7rbadm1bGkt2_sdUZ3QAJiMaYgQrW_vIMGUwH3zQbKTeCYeJJRyTORtSCm74MSGx8onpTZj6FvSHB7KPxFVpxZB1spc8bG9lJT3QVdR2bhIX8MHhXAJswpW9Rmr4c-BIg1rINhLhHr5HiWKbuXwR-7E77EOagPXXRNe5ERJnubUQSvO4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCWmKfLgAnPn76J_sPqZo5J3aFVNqZFsd2-UWUq9MiUmQV0Oa0db_ksh-4rekdhj1cfjPrgZ0xJAeXv0lQ0SlV2VzI9y_MbTzUfOrfyE607srjA8uGfPAcBBoqg9hCJmN2s1gOFy2alo5jYFJw0qv-iruliFsbu1EGqyrvC7AwYj-i-AUqFC82iE2H4BGtmqzi6f3ntY8xmFtmnlHOc9hYeIDe73gm9Fz3Hc-JWp4a1KKViODnIeMv1zztb2v_Qh9JjsD7Yi4mvo-mq7GJvWyP9TFRfu0F3aeHFKfR_XDvPz_5MFcWGDYjQHGZO1hudtLL7FalLquEOHeXPh_m7AaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=iLZ6slQbXtTq0BJgt0JrbVkR7oWWlIdZ01iFw0W96Qrd7bl6tlmLg86DrEaldOIzO6nLmKELoIIFv0kJIARmgO12iX2Md1FHiVtKfYJuVTVr4Jh2SZIIKPdXSFOjX0j28dvMn2NHj5qdo2Zm13vx26_EHtgiamFEUTXPX6PoWSiq8SsBdN2ZVe0VpVhJrKs-d1EbH7RoFQWmRVikSsA3NdafU8UdDZqakESWcbyPiA_o2hIb5xt8uZI1uRqc1NB6t5F_G2_cMEWB8VvSRezfog-dASoui1POcwZqxPe7jmDqoR5PwfeRuJLgcxjD6GXOeMIYqIg2FdHCfQ7B8nPnMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=iLZ6slQbXtTq0BJgt0JrbVkR7oWWlIdZ01iFw0W96Qrd7bl6tlmLg86DrEaldOIzO6nLmKELoIIFv0kJIARmgO12iX2Md1FHiVtKfYJuVTVr4Jh2SZIIKPdXSFOjX0j28dvMn2NHj5qdo2Zm13vx26_EHtgiamFEUTXPX6PoWSiq8SsBdN2ZVe0VpVhJrKs-d1EbH7RoFQWmRVikSsA3NdafU8UdDZqakESWcbyPiA_o2hIb5xt8uZI1uRqc1NB6t5F_G2_cMEWB8VvSRezfog-dASoui1POcwZqxPe7jmDqoR5PwfeRuJLgcxjD6GXOeMIYqIg2FdHCfQ7B8nPnMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=E__SxBLEmkyWY-64CBaUwk45z3zbvvLOYxmVFgU8WdJfIwYFhaJX7ZLOhmfx7DR0KoqceYmIFB0Cft8tnTs7GruoBjBY7rFsJFj84qjCDplcUABQt7reaVkoDZ6qdCPGGszNy3nx2KuzgvqZkSd8rXDJd2fOQv8sFArjMVumCG3eunwn-BnHjIsVROfNuHPnZbqCwXpWBo2OMDq3DF5iIerK2ahzkQdIq5pBDAREHzbnSQ4YeCgsGQbCK1kQj03Y7lj0QPXkCphI3IzsFX8Jso79H3H39EK4T18YQLgyLqUrj0GQJuWZ2Xx1lJT7HD_ys8jW7GtzIQH9wP-vKMFQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=E__SxBLEmkyWY-64CBaUwk45z3zbvvLOYxmVFgU8WdJfIwYFhaJX7ZLOhmfx7DR0KoqceYmIFB0Cft8tnTs7GruoBjBY7rFsJFj84qjCDplcUABQt7reaVkoDZ6qdCPGGszNy3nx2KuzgvqZkSd8rXDJd2fOQv8sFArjMVumCG3eunwn-BnHjIsVROfNuHPnZbqCwXpWBo2OMDq3DF5iIerK2ahzkQdIq5pBDAREHzbnSQ4YeCgsGQbCK1kQj03Y7lj0QPXkCphI3IzsFX8Jso79H3H39EK4T18YQLgyLqUrj0GQJuWZ2Xx1lJT7HD_ys8jW7GtzIQH9wP-vKMFQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=kKS77gdBTbudxARoku9o-gGgZtKZ7B0F85XX-hsI1RnCmrEBufL0j_ogb2RLdv-qqQxHaGG_GTvbGbayyHrHxky189sg0Dy546SMYSx5mbaTVaVR0YR-hGozFqiOse3ip5I6r23LeCQ8X7T_8cdZIWdxquuXdy60IHGWOHI89a0NAQoKuT_WuDbmOcPwcvJPPyRohvkDC4VhNsntfF35iGONVeivM52FF7_6HDb6O9n8Wg96pyqtPHFsYjhIRZyUEJragm4zINO-g-zmQaaroPKGQOCi7E1Yrj4GDy8E4gWzxUuvX2ISYm_axuFF-uS7Gx_xfZHLGh_R3ghZugORYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=kKS77gdBTbudxARoku9o-gGgZtKZ7B0F85XX-hsI1RnCmrEBufL0j_ogb2RLdv-qqQxHaGG_GTvbGbayyHrHxky189sg0Dy546SMYSx5mbaTVaVR0YR-hGozFqiOse3ip5I6r23LeCQ8X7T_8cdZIWdxquuXdy60IHGWOHI89a0NAQoKuT_WuDbmOcPwcvJPPyRohvkDC4VhNsntfF35iGONVeivM52FF7_6HDb6O9n8Wg96pyqtPHFsYjhIRZyUEJragm4zINO-g-zmQaaroPKGQOCi7E1Yrj4GDy8E4gWzxUuvX2ISYm_axuFF-uS7Gx_xfZHLGh_R3ghZugORYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=NFIFSZ7Df-XIrPpmPbq2qoC87y7VnKFpTrp_LUh3ntDhb_arEfsLYjor3MFkV2VgU5a80FWAnfuNLX-x-G1jXgb3iBKKIRZDmjNZ6oqVFVg5gDWCJkGVsGQTnMnte2K4TM1LhKhu8-VykRJMmUYRYuIShz9_ogdITPx2QLTY2kpYRqc8Y8Vs2HxN8wmLeIq5j4DA1ZUyghgrAaCrqaU35COp6RFgwSBstC4lms1qMnVIPB4IT45kFihTZHHsaScz7qkR__CRsTtIxxqKyUi8ntZr482dNdaMhHZDz4oEVcXVpTecDEUTGTATcHA2pEj1AWexcXP9eqbntXLEdsmvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=NFIFSZ7Df-XIrPpmPbq2qoC87y7VnKFpTrp_LUh3ntDhb_arEfsLYjor3MFkV2VgU5a80FWAnfuNLX-x-G1jXgb3iBKKIRZDmjNZ6oqVFVg5gDWCJkGVsGQTnMnte2K4TM1LhKhu8-VykRJMmUYRYuIShz9_ogdITPx2QLTY2kpYRqc8Y8Vs2HxN8wmLeIq5j4DA1ZUyghgrAaCrqaU35COp6RFgwSBstC4lms1qMnVIPB4IT45kFihTZHHsaScz7qkR__CRsTtIxxqKyUi8ntZr482dNdaMhHZDz4oEVcXVpTecDEUTGTATcHA2pEj1AWexcXP9eqbntXLEdsmvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=My9AuQOureYgd0S5PxkYX_8sGnqwSrIOECNxKs0WCRd_kc4sPFKVsCdlyHEaJiX1FOVjpTk2gC9NEKLMDYsPiU6a03FwJzJ6s6HUyUpYsSwrn4pka2GUIAej-9e1J-Pg4s1FyTC2MAvAFdRVVpuC6IQYl2_1Qi3d-VaU4ksO342gY8IL5Z1wZxLsC2FNsuXEAVfoQQDdbkbK1RjrnPPuNCEe3oJPX2aq0aFoNixU9VkGliM0KT1tsGy0beaPyeEgy2UIdPf2axuf1w6oUpHmQ0ns_vJZmmlxaZjnYobn_asOs9yysjDWx29eSSrwlxNKcKvyhITIsZx7mo_lRHXapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=My9AuQOureYgd0S5PxkYX_8sGnqwSrIOECNxKs0WCRd_kc4sPFKVsCdlyHEaJiX1FOVjpTk2gC9NEKLMDYsPiU6a03FwJzJ6s6HUyUpYsSwrn4pka2GUIAej-9e1J-Pg4s1FyTC2MAvAFdRVVpuC6IQYl2_1Qi3d-VaU4ksO342gY8IL5Z1wZxLsC2FNsuXEAVfoQQDdbkbK1RjrnPPuNCEe3oJPX2aq0aFoNixU9VkGliM0KT1tsGy0beaPyeEgy2UIdPf2axuf1w6oUpHmQ0ns_vJZmmlxaZjnYobn_asOs9yysjDWx29eSSrwlxNKcKvyhITIsZx7mo_lRHXapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_vpSPpRU4Zi1UTVFKXaXQzaMys2zdgmBllmZxN80e0bQ06FC_dLpZLAfnpSqu5A3H5euIAVYohxehQWHLhqfUCWgEXjhfVrTQeS94HUBghAFGlx13zhf6Bii1-eeb3Z_IN-AXAgz5kY5jsL-IOKDQtxWiQL8DEdB4cG5G2bV7uwKi0F0v6gpw9cKKJQlcO53jOFSz-7iA2vgD1a9XFSI6tt2lAXXwKiHTOn0UcPTvzlqKcbdA7k7kwbTRFTi1Z29ZRC1HarjrOu4P48mly6rMafEzWvxocQPVkfzOX0rTUExdB2nQpSmoFzheQ5B3JKeBdeAylgyzoimLiBEC4elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=QzMiiKcQHAI0uYba3vVw_am95Nc6qm0ghZsnHejB5PIbrndR_OQhaYmkL7LaBTOCCaUMc4jLWTG9tid2UD-eLiE2Lojg9Xq2syBdtQTb38QfeL2vKgM4MRWOhOcv9IWgeef9ofVHI4NIVcYO6cegUGMWQK72pDBSV1c5HauwQ_BsqbeaKFodTk3cdtH7HYIgWkYBL1IKMLyl1poWG-ivnrJ2Yw1FtsxrMTc5ZP8Rj0_BUzPP5aseHkPwENPgYIhYNx1Yh5NWM1065BkcimNpXYnW-9tUCwNW-bfhfYPUMrMvKW39pfTeJCME60_wQdXJtZzTPuMbC9LzeOsrcGsjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=QzMiiKcQHAI0uYba3vVw_am95Nc6qm0ghZsnHejB5PIbrndR_OQhaYmkL7LaBTOCCaUMc4jLWTG9tid2UD-eLiE2Lojg9Xq2syBdtQTb38QfeL2vKgM4MRWOhOcv9IWgeef9ofVHI4NIVcYO6cegUGMWQK72pDBSV1c5HauwQ_BsqbeaKFodTk3cdtH7HYIgWkYBL1IKMLyl1poWG-ivnrJ2Yw1FtsxrMTc5ZP8Rj0_BUzPP5aseHkPwENPgYIhYNx1Yh5NWM1065BkcimNpXYnW-9tUCwNW-bfhfYPUMrMvKW39pfTeJCME60_wQdXJtZzTPuMbC9LzeOsrcGsjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=T7MkeJ5iwsJWe98sZ8vU50RI_ljMBcLqlqgq0TE-bxUI8NA4-B4RPReyECBabIicxUIx98TD8mG-5_k0yCtAA7XsdRGAHfllFUvtfuQPOPOxynr6JaP-JWbXtwDycKWHnqoY0A5DEeNO8SV6OvzqPJdfXVn6Su-5C4gHRWpRlpqG72AtdAB7nE4KCZXBh63n_ex24a3QpWzR8msW9FUuU_EbB1btdiJWHnW8Ibu0QWfoEk5gtY_COX9I-uma7djiiu0Z9mma4hyz-mwEeI-iQbUatcClqa93iYH_qaMXSkQaRgC3g8pFE7RUYJsA6Ra2GiV7YfH5HQ689GE6surp3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=T7MkeJ5iwsJWe98sZ8vU50RI_ljMBcLqlqgq0TE-bxUI8NA4-B4RPReyECBabIicxUIx98TD8mG-5_k0yCtAA7XsdRGAHfllFUvtfuQPOPOxynr6JaP-JWbXtwDycKWHnqoY0A5DEeNO8SV6OvzqPJdfXVn6Su-5C4gHRWpRlpqG72AtdAB7nE4KCZXBh63n_ex24a3QpWzR8msW9FUuU_EbB1btdiJWHnW8Ibu0QWfoEk5gtY_COX9I-uma7djiiu0Z9mma4hyz-mwEeI-iQbUatcClqa93iYH_qaMXSkQaRgC3g8pFE7RUYJsA6Ra2GiV7YfH5HQ689GE6surp3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=cxOE6J0PP4IIQ6Iwx19bzLU9rpf1udHkUZwA_LkLEFjWUQadg9ADMTEdsSghtR-GwoJYlRfoh4U__RUMou9l6H742-G8hXi_gWwZ5YvVaAJEqNu4jbLJKTMnpx4uMU0-BFTt7kFZNQJRKQP9_MeM8ICS26CSOlHVIfiIKfeqWqR514yIYkljCLb7Tag1RbzHZDBJlh8Si9OhND5Aqu7sF_LG83W5GpUyZVMVHOVkUCfNs1SKeeSu5GhKnL9nQhWadYWMnpD-QJlwgUmEmwbEana3T3C48OHL7PBiEcpmNK7kgRQllUBgNAOaBzSy7-Llbkok7jvs1vJeIUfD-Lmzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=cxOE6J0PP4IIQ6Iwx19bzLU9rpf1udHkUZwA_LkLEFjWUQadg9ADMTEdsSghtR-GwoJYlRfoh4U__RUMou9l6H742-G8hXi_gWwZ5YvVaAJEqNu4jbLJKTMnpx4uMU0-BFTt7kFZNQJRKQP9_MeM8ICS26CSOlHVIfiIKfeqWqR514yIYkljCLb7Tag1RbzHZDBJlh8Si9OhND5Aqu7sF_LG83W5GpUyZVMVHOVkUCfNs1SKeeSu5GhKnL9nQhWadYWMnpD-QJlwgUmEmwbEana3T3C48OHL7PBiEcpmNK7kgRQllUBgNAOaBzSy7-Llbkok7jvs1vJeIUfD-Lmzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=rgbTr3e9kG3Z2husKErll13mpoEVdpzgBVpHMXC6KBOLkr2DAHb_drHow8bzSlfvAEcATBeJxz6mlIvZyQKmfDDS9YRIR_ZylgtqBZfk75LeL9xWl49h8c3jedr0ph48AfnR4BjyjPOejdS99-N3ph3Krr39GDsrC_TplC1YpQ8lmpxNmC7SZsIBJjFgvWB2-h1DqQSOMWidiaZj4xcwt2DNwpLbtnOOMUiVi7YEusOilHHq3kD9b6H-Fd42_iTt_4z048Cb4tBHN5YWAvpAEqepgVo75glWsUm9_ozgxUz3AEpLocEHICWW07HvHANIY4eMGR4CgEdzm190sO-jnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=rgbTr3e9kG3Z2husKErll13mpoEVdpzgBVpHMXC6KBOLkr2DAHb_drHow8bzSlfvAEcATBeJxz6mlIvZyQKmfDDS9YRIR_ZylgtqBZfk75LeL9xWl49h8c3jedr0ph48AfnR4BjyjPOejdS99-N3ph3Krr39GDsrC_TplC1YpQ8lmpxNmC7SZsIBJjFgvWB2-h1DqQSOMWidiaZj4xcwt2DNwpLbtnOOMUiVi7YEusOilHHq3kD9b6H-Fd42_iTt_4z048Cb4tBHN5YWAvpAEqepgVo75glWsUm9_ozgxUz3AEpLocEHICWW07HvHANIY4eMGR4CgEdzm190sO-jnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiP26E9tm8iXyl1l2OSF_26XRRlnou0rGLnhDUWr89fDWeSE4HUAxHSpS3IDKIRbDDXYTu28UG6v9R7cXt0YoDckidmlyi88jBDMBaSm_MlZ7xHp2agGcVbIy-gtz94hKwCRmRcpPYOl__uK6jtS6kRj5LNn8IfaJWb_1_gKRTFXCLqtaNVcoPvo-iohEbJofdZUPusgJ8w_2ggqR99qjxZgNtNApeRg2Gii9HF-v5wL1kaIbc55iCK3IW1C1dTMi3-7S7SI2_YJ4lclzSO4iBrEJN63tF_uIKoCjNl_KGyGM4G9MwxUgTzDZsxc4Vr_1gCWcU1hYXOkmUKDQCJ-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBt-IF2T3B90vU2b4MQ4uHorcSf_cBBv2kuEbpn0PYtsNamvnEkg4qiFYRoYKdTjMqyyLjm8NnLHSTqBO7cCv-MuNrkXDJL3Yflvx03Eu6dwjC06zD_UJMg2BVWbdR7WQOQ6jjBQdqvr3bg7XtTyg2hSI7PbO_5G_aZJgEzAcRpZqwd0Rbdq2KF0-YTDFcQ-gcUh1UuZanqB3CEl-lNUe9cr9TWZDc_-1DVn5kCQPbPEtRIlJk8zPNXwjC0alv3GfsCUmXTaC9-niwG0R2GG9GwmPGA8a0R5hK8_FKv_Hh4m3nT2t3NRK_z2tklfprEPc0I2TtLkizk8rXL7XJFiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=Jzw50RoLcKjhQRs8JILHJAsluNhZjCxDku5KTzN9WHr1y52C1FFPdx6W2b5ebWQhItsXqtR_46jGdRK53NbU5CPJjdo_XYmRwJyLhEpurEDy7Z0jYZpFuswghyqBjH5dLfFMdkW-XehbgKFZZlsqyBrzzKKm6FTBbcdkWhdk08QhhOqcjKKDoWfV6u6PZfbs1e7xENDF9h_BG_k5w52c7YphLk0lEmJdZ_qZ020iylA1-bqYDmmHT0DymyYDTra-GwpLRCotQ5khYKML334vmxEhqLLXUzp1-5T1vEggPP1znuz0tzECq6hi3q1cvCBwXRNhvdEpdN8tc20GDF_qOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=Jzw50RoLcKjhQRs8JILHJAsluNhZjCxDku5KTzN9WHr1y52C1FFPdx6W2b5ebWQhItsXqtR_46jGdRK53NbU5CPJjdo_XYmRwJyLhEpurEDy7Z0jYZpFuswghyqBjH5dLfFMdkW-XehbgKFZZlsqyBrzzKKm6FTBbcdkWhdk08QhhOqcjKKDoWfV6u6PZfbs1e7xENDF9h_BG_k5w52c7YphLk0lEmJdZ_qZ020iylA1-bqYDmmHT0DymyYDTra-GwpLRCotQ5khYKML334vmxEhqLLXUzp1-5T1vEggPP1znuz0tzECq6hi3q1cvCBwXRNhvdEpdN8tc20GDF_qOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=ca9IMkNanCOqYl8QAH8zUtWnuQuVEgMXAdvU0YRsmsWVme3ws7E7CPdigZ504KX9uQLq8w09jndMK1RjQV-qIS7pIdjwLlUQ5KJ1Q4PCvWx0ZuIl6IULASvklZEpLQQRrsN6ih0jMOlGXKwfpJJ_xtKc-qFI4af1WeoesDU1eVy3Fvw7asQ48P9wZALvFo_F_SVxiiRnzOU64IyL7pLNdmC2RsZYaDCwmE9tefv451tpBxCYevfJFjSjYpc5GWc-FOKWv4qof4V7-eAE-yREMGAKDKmd0pA1eD_KaeJorYOfcTr3RnoRTi8Hwz7UBjq1ypYqA1q_IkdFmzuf7k-Yj7OPbIQUdCvbK_XNPf7NnwSgbH4majlPOLCCsgomVF7JLx8REi97-jZfn0YibpZMP5VRGhNKggJMeuZMy8Hg2zJLm54jd3b1nAQ31SxVCJypfpWwFQzoclZ0dJ9w3EaN2wPNfrnE-mB1UnbbZpk48qlTsgwJuoxH1Y77czmm-pyXp7sjIhF8a9vVCVpFr_M_ij22NmtZiIojDtga_IxSzpN2WKgg_Zvzo1dFNTIdypSAJGabqIhGt-DikHa6dmQoC6dzyFHoCj2iyfRqlly27fUxJ1Br2RI5mYr_GIretAka31gChQeldVfzLwMQ46d1f12BpKehklIvQdu7nVM-Y8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=ca9IMkNanCOqYl8QAH8zUtWnuQuVEgMXAdvU0YRsmsWVme3ws7E7CPdigZ504KX9uQLq8w09jndMK1RjQV-qIS7pIdjwLlUQ5KJ1Q4PCvWx0ZuIl6IULASvklZEpLQQRrsN6ih0jMOlGXKwfpJJ_xtKc-qFI4af1WeoesDU1eVy3Fvw7asQ48P9wZALvFo_F_SVxiiRnzOU64IyL7pLNdmC2RsZYaDCwmE9tefv451tpBxCYevfJFjSjYpc5GWc-FOKWv4qof4V7-eAE-yREMGAKDKmd0pA1eD_KaeJorYOfcTr3RnoRTi8Hwz7UBjq1ypYqA1q_IkdFmzuf7k-Yj7OPbIQUdCvbK_XNPf7NnwSgbH4majlPOLCCsgomVF7JLx8REi97-jZfn0YibpZMP5VRGhNKggJMeuZMy8Hg2zJLm54jd3b1nAQ31SxVCJypfpWwFQzoclZ0dJ9w3EaN2wPNfrnE-mB1UnbbZpk48qlTsgwJuoxH1Y77czmm-pyXp7sjIhF8a9vVCVpFr_M_ij22NmtZiIojDtga_IxSzpN2WKgg_Zvzo1dFNTIdypSAJGabqIhGt-DikHa6dmQoC6dzyFHoCj2iyfRqlly27fUxJ1Br2RI5mYr_GIretAka31gChQeldVfzLwMQ46d1f12BpKehklIvQdu7nVM-Y8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-V3Ied0Yxq4_8JfGcPR8-wI0ivEmQXOmbrT1T-ubcI135CrcSdgQU4ueAFangGqLXGRPYfFcgxj1T9hKUUU3HoR9kH9r3tqDIuePRNCOcSpKS2v7SfKANW3jjxvXDqAGox8h-gwe-C9gZfcMaoE5Y2C1sIA6iOvOBLscxaLcgGpywKZeM98Y5j9fMUVAEvoj9ubTqZGiKlZ1RNjg15kmsO9JumP4e5NG7_7MTKpXsIKD3FxVptpM0aUijerVFWD5c_9SXAtpPQcPvFKuFonJ5NEMTw_Y-znNsyuGGOxphVovYx_kW-m4EIWvIw4JaQdtktRpbCcpFYwXaTQq6R2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggP0ew3xSQRzzERWBDa8u5gIN-oDqJTUa2CVGZGwEM6QWsA5qnxZFuBoyo_IBHSeeh01_MLdsz5naSqSu0GpEqPiOc9NiIdRGINo3gaEMwIAqHC3SW93kwd87AW3EkO_k760fLfGGa56tcdtX2Q8FRDgtZ7WBPJSNczTrNd6Jy6tVWSFjGaR49RK3YGYMWyoT4x3xKhprpFEVvghMjPGX3jTE9xBjKozGsJ_Kmv2BBeeITeFbkUST8X8aiALujZVXMfGrDfv2pptkvk7T17u-Zp4_rh895Uj4TJqZ6xp-SYQQeaQVSeqjsGw1d04SMdKGofSpVuacRHT_uBXxCdo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwJm9eHlJmQLCxNhV3pPFGLB508sLHy7KaezcoVyN4j0zTT8t80r-1u48OzkXcOnh2yTPVJYn3Ja9kXbHHZkk_B8WStyCE9iLN_IROWLj6lIBVQKruyqwQmmG-fIRuoDhR0cGRIOBdbiAEK9hSvo9dM5Fs9GiplfVjzizQDBfBcQ2hmQDXXjGeCS0CuBr_VFrqG0byWslfrud6W7AwpD9saAPBsAgCS7VmWmU70tYMhvxwF79Goz1M-oFTwyKkFxwYwoGJgfiJ5QRY0Kt2D5T_CWnwQF-N-nPdswKRMll45v2wWb0nVvOofxOxBj2t842wPMV0LKnPwJlpvWSk4bmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=UH5cxK_eUOPd6yBSYb-HLgKNDBU6DEhLYewaAg_clOriEC60ewUuj1wz7nqvtBbv2MqDvaRyaCkXsmqgXG8e9kAZ7jtSaFsM-N_Cm_K-KkePNIJbcnd1doa5mp9JQKgL4dQnxfDRizIE07FF-9g-f_QwxHZ9NlmhdobTcqoA_9eAXVLGJ5M_RXD13rsTMOBoGlB2w88ZzIierCMpcg0oBfgVX-gSBK72AIBO7kK6VGD9GRf3c3JNNubi5PfuFfq3lqwpNQ43EqpsnRUOgKDAVBwHPf59FjZ-gssyi2HEsl961YURRPJzUP9_XnRYx69KtWAnpi4vWQtYIlJezReOxYw8fY-bANTk2ab6kG-GFEe_K5G1Kv3hg3noUsHRTHZer55E2OzZAvyrU6pzQyyCKIeDCmksokoR8zFtq_iYnTgibrNOTZ5tojjBxoqtqGy6j4L_BZlaO6-VVyvzbgHJa07NQPyip2ONM71ThYNUvWbIZFwMn9Pwa5vJBm_4bgqBqbfVUZTrm7FRBs9xkyxqj3vhty8drKtPTGyT5TgaKJghLIRKHCBhs0fnp1PXDRmqYXY9Ah6gPNfiWkRx4XLCipIeA_Nbl8fOyWA7IDuP3we8eWtXVTGkwX_RqB5t1x-DbZXHvhdfKo5tQh85WGXnxAbloD6_f-tv66vpLQOxf5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=UH5cxK_eUOPd6yBSYb-HLgKNDBU6DEhLYewaAg_clOriEC60ewUuj1wz7nqvtBbv2MqDvaRyaCkXsmqgXG8e9kAZ7jtSaFsM-N_Cm_K-KkePNIJbcnd1doa5mp9JQKgL4dQnxfDRizIE07FF-9g-f_QwxHZ9NlmhdobTcqoA_9eAXVLGJ5M_RXD13rsTMOBoGlB2w88ZzIierCMpcg0oBfgVX-gSBK72AIBO7kK6VGD9GRf3c3JNNubi5PfuFfq3lqwpNQ43EqpsnRUOgKDAVBwHPf59FjZ-gssyi2HEsl961YURRPJzUP9_XnRYx69KtWAnpi4vWQtYIlJezReOxYw8fY-bANTk2ab6kG-GFEe_K5G1Kv3hg3noUsHRTHZer55E2OzZAvyrU6pzQyyCKIeDCmksokoR8zFtq_iYnTgibrNOTZ5tojjBxoqtqGy6j4L_BZlaO6-VVyvzbgHJa07NQPyip2ONM71ThYNUvWbIZFwMn9Pwa5vJBm_4bgqBqbfVUZTrm7FRBs9xkyxqj3vhty8drKtPTGyT5TgaKJghLIRKHCBhs0fnp1PXDRmqYXY9Ah6gPNfiWkRx4XLCipIeA_Nbl8fOyWA7IDuP3we8eWtXVTGkwX_RqB5t1x-DbZXHvhdfKo5tQh85WGXnxAbloD6_f-tv66vpLQOxf5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nBFvozRbkanK5oSu_b5oO7OoFNDJEPTEw2GlJhi5aGrqtNeRpQoBT9QXeEa6jdgT066hnDmvPB66dRa123cgO_6b4w8ung50eDT0p7ZTQfnqmfj8yj64b9bNAjVjr09BIDp7kN1lHVVlgRaUcgJGELQv1r5casiM7lN0F3t7lg_f5BEGtXw4atlxiyOkUCRVHxbMO4Z9AXQDCeJENH6jVcqIoz829YTRZZRuZ48AVhBNfTue-QBLWFdspn4icpY8V3-v4OpQ37AM7VurvYtShG24vcAuM5KtkgoMXFj2RT95SB_jeT8QjcxMWjVykm3rnkQpyuVK0Ne2sOEW_a4gD-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nBFvozRbkanK5oSu_b5oO7OoFNDJEPTEw2GlJhi5aGrqtNeRpQoBT9QXeEa6jdgT066hnDmvPB66dRa123cgO_6b4w8ung50eDT0p7ZTQfnqmfj8yj64b9bNAjVjr09BIDp7kN1lHVVlgRaUcgJGELQv1r5casiM7lN0F3t7lg_f5BEGtXw4atlxiyOkUCRVHxbMO4Z9AXQDCeJENH6jVcqIoz829YTRZZRuZ48AVhBNfTue-QBLWFdspn4icpY8V3-v4OpQ37AM7VurvYtShG24vcAuM5KtkgoMXFj2RT95SB_jeT8QjcxMWjVykm3rnkQpyuVK0Ne2sOEW_a4gD-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=n6qOIsN5W-8hFjiccP-DENPlzD8qBO9dOiD7cCC7MGxPobN_Ex_2EsZtg4Fp-Z43BmlQi0klFP7FgkPMHY3SI1U5q7qtbXGPRgkZ9OYAtaUZC0ej7igUCcy1uCRmRYz7jrLWNpLhXUGPZkUt9wQwxtajy9vgl6Q2zhSWAH6jsCfBEXHOOjqxuo4Ajbj5CuH3K3k84r8nPeLH6XdPtD9cVmudDEgKflMmg2hCQjoDvHVfMQ20YLgHqiG6JarUnPg2hr6CsZixoAy7qytOo6w71xT14zwzM74U0sC1hlRxgeq4Wd5t7sQWJ_xRoSXQTN5FjzbWOzice2yi2k9Lac-eHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=n6qOIsN5W-8hFjiccP-DENPlzD8qBO9dOiD7cCC7MGxPobN_Ex_2EsZtg4Fp-Z43BmlQi0klFP7FgkPMHY3SI1U5q7qtbXGPRgkZ9OYAtaUZC0ej7igUCcy1uCRmRYz7jrLWNpLhXUGPZkUt9wQwxtajy9vgl6Q2zhSWAH6jsCfBEXHOOjqxuo4Ajbj5CuH3K3k84r8nPeLH6XdPtD9cVmudDEgKflMmg2hCQjoDvHVfMQ20YLgHqiG6JarUnPg2hr6CsZixoAy7qytOo6w71xT14zwzM74U0sC1hlRxgeq4Wd5t7sQWJ_xRoSXQTN5FjzbWOzice2yi2k9Lac-eHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpR2Wu0gYYKOjjtrM71PQNdcK4XhejHDZX2tOJg1EdBRJYX0ScobqPGpkn7vey2yrdRU3He49kwYku73tZ4KxX2J_KtLytpMPOQRPdVI1QKnVrWLgkTa342Wm0qjAFk9kUu7UIAkp3NkIWiVG_TcX8IHrt-xzE4Lgv_MCStCCh79ImYuSMLfHgbapV-Zk44rvl0v2LcHNEodlCQEIDjwbV0Vgmhsqt0pafelbAtw4gr8FyrYk15yTzZAzIUplTLe_XQV7q-xoLseNXVBi_gHJRnPzAMbTAEoaWkAqNgyBiNk2eU1KW3z5sF8pYeejsutjnIV5DzjaeGlgGfngBYyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=MFsU8uoaLNP6EAfT2hOcCFfyEcZuLXWysEz_6V51h68UNEoiYzgKNsac9f2Ov-Y0DIwdiS55MqWXxsxp8FOIs_tudqU-DNJCepu3G8_pEfMVx1xqQs1amlGUIlKeIjWFI4rLrGAtmILyvYN1vGkF2Q8mc5r0WUb8s4PCI0DJ9gFS-FGuk-GdGlPglazuOCwtiiCL6mvF-fJjzwvlxAJiobhVMgsKrsvWWhrpZonjzvQpgnqy5pC3boNvDRvfSMR7Qj3LxNYz_GFzWhOUK1HJl8YLEYDX-IhJYOoDNLVAcv15boRMWD-0vHOzkgnvHsTHDiu-NDwMragxH0Vtg3s-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=MFsU8uoaLNP6EAfT2hOcCFfyEcZuLXWysEz_6V51h68UNEoiYzgKNsac9f2Ov-Y0DIwdiS55MqWXxsxp8FOIs_tudqU-DNJCepu3G8_pEfMVx1xqQs1amlGUIlKeIjWFI4rLrGAtmILyvYN1vGkF2Q8mc5r0WUb8s4PCI0DJ9gFS-FGuk-GdGlPglazuOCwtiiCL6mvF-fJjzwvlxAJiobhVMgsKrsvWWhrpZonjzvQpgnqy5pC3boNvDRvfSMR7Qj3LxNYz_GFzWhOUK1HJl8YLEYDX-IhJYOoDNLVAcv15boRMWD-0vHOzkgnvHsTHDiu-NDwMragxH0Vtg3s-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vLrOH7tSu53amicjr29jBt1vsTAxgAjsECB3dujaH2kXFim3bpy-4XH18hrD08envwAgHa5XuFLI7ln3d_6GdzBHyVMt6q6wODk2u0ufsMJYA181FUbEJmY-ZCu_uBoh4HBswGozmBHuNvbHcr9_9aeH9Zx-MTRIx7_0oMtVy0X0gTS03h6-O_nn723b4ncG_Zj6auCIZ25oq7U65CuKRw1_yzJOXbxyzIQu_CocpBE3Hacekflu12yJAlcoaLSL2CfpbllnJdbYO4CTBEHwKBqPNWc87dSiCUD47p6o9v_AM9tqGW0OpPzjFcLS_rAkzQkvlqyZDeInj8Xhlr8nUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72367" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=G3hNNhq_RXvzY1XXn8ms6e9qsoxe_DXL6L27SAPAsZt5IbV0IbjMLsBpSG4oAE4gTcFvq4lpCOmq_7Ra7pxwYiqG7tyIcHk0DeS_Yii3CQtuj-A01buKn5ZGJzp6SpILZmu7fvYlePh02zuzdcf6WZsfO776Fjy2HBcpXbMhSoQKo8LbN87T0Q4YY9dpUTkcuefCSpIwxxiaeF1tcdJw3tWoEJcwldXNRCgZfqRHou3TaDBgXaUCRnpCJDTA0NhWliALvn5CU_2swxAg_YENuJDGLMutNHQHWYKJk1yvaA49X1L7bxMWFSF6gJG0_hwzv2tko8sNeM-HxmpW4GbrQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=G3hNNhq_RXvzY1XXn8ms6e9qsoxe_DXL6L27SAPAsZt5IbV0IbjMLsBpSG4oAE4gTcFvq4lpCOmq_7Ra7pxwYiqG7tyIcHk0DeS_Yii3CQtuj-A01buKn5ZGJzp6SpILZmu7fvYlePh02zuzdcf6WZsfO776Fjy2HBcpXbMhSoQKo8LbN87T0Q4YY9dpUTkcuefCSpIwxxiaeF1tcdJw3tWoEJcwldXNRCgZfqRHou3TaDBgXaUCRnpCJDTA0NhWliALvn5CU_2swxAg_YENuJDGLMutNHQHWYKJk1yvaA49X1L7bxMWFSF6gJG0_hwzv2tko8sNeM-HxmpW4GbrQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به‌محض اینکه ایران تسلیم شود و جنگ پایان یابد — که به‌زودی هم چنین خواهد شد — قیمت نفت به‌شدت کاهش خواهد یافت.
قیمت نفت سقوط خواهد کرد و قیمت همه کالاها پایین می‌آید؛ البته قیمت مواد غذایی هم نسبت به دوران بایدن بسیار کاهش یافته است. تقریباً قیمت همه چیز پایین آمده است.
قیمت نفت اکنون نسبت به دوران دولت بایدن کمتر است.
ما مقادیر عظیمی نفت استخراج و عرضه می‌کنیم؛ دیشب رکورد جدیدی در انتقال نفت از تنگه هرمز ثبت کردیم؛ مقداری بیش از آنچه پیش از آغاز جنگ از آنجا عبور می‌دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72366" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=vGvsCYMFiVY8xbk2W9-t2wjPstS__Tgyef8RzeupO-cwIcZf_Uk8YvOgXklAPQ_QZhGpcQKFYlslUkgWicHFjE4P67Gc3H65q_el73eVX8B3W-mUoj1cmEHqASjpVP-LxxloZdeNmgLrX8m2UDnoFpMXkcQ-CXXv38l3Rq8wqlVvH_EFIvpsda8WCbgyi1An5YKm6eBuCzaMF78MQh0z_0s9rl40XtnX-hX4mQQUEochtQZUem6XznSWojdwp8PGy3mfGaXsE7J-zI3AyqNbfD8MtcqHht9rHD0NjvKVseps9smt14-TSkRSddOGZBEJO_-2VyV8R1GUT-kdWQC5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=vGvsCYMFiVY8xbk2W9-t2wjPstS__Tgyef8RzeupO-cwIcZf_Uk8YvOgXklAPQ_QZhGpcQKFYlslUkgWicHFjE4P67Gc3H65q_el73eVX8B3W-mUoj1cmEHqASjpVP-LxxloZdeNmgLrX8m2UDnoFpMXkcQ-CXXv38l3Rq8wqlVvH_EFIvpsda8WCbgyi1An5YKm6eBuCzaMF78MQh0z_0s9rl40XtnX-hX4mQQUEochtQZUem6XznSWojdwp8PGy3mfGaXsE7J-zI3AyqNbfD8MtcqHht9rHD0NjvKVseps9smt14-TSkRSddOGZBEJO_-2VyV8R1GUT-kdWQC5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود کریمی، مداح حکومتی، در مراسمی برای علی خامنه‌ای نوحه‌ای به زبان انگلیسی خواند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72365" target="_blank">📅 16:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=FEAGWQCmc6Kf0RmyjSWzlyb_z-QoViONwlo1NGA69ZmJY-20CwMjmPdWGVE89McIVbMNKOeIgHNLdEVFHmLfg-UqtmFBXRN6w4k9XsX-vEDl43dSWxYvNJUi8ZXTW1-Neczkb4rG-9-u1DTdwm1zyiKxLZmpyzRyeaVS6g8hMiqsghBQMCqG6Kcy_a-sv5g44tVC-vAAxKrzElwvpAIgAcbbDDff6afhQ4WV1p-RI5fUZwbhuSmpZwwDAXC_VzlIoZjSNsGX2Gb0Hkk-tEd4EBS1XFM9WaJdnJKAstHKQWq2pg5W_JXOdExHFXB_M7Vpeg429tNdKEGU3R5asNmrWnKWGz1uhreCYatrwgNyhR0466DPD72eT59jYT2d-EgNjQS_ZmafKsBExrJI7Os7kqanyDI2PgvH6l-7GVVH1BE4Tstt-J79hqJGVJaY0EFdp_7gd2Ktjn5N5GjAoW05nsUggKdek6mXGphru3NbkbPoyu21XY3w2APerKAym6G6CbXFpPBmt68ksz3x-F2CLRvAc_n0A4w4emqdTExLOkKOxKQIg4vnKdPlfZt8WWT8YrlAn62sNTPBWk607U25SfZ1WUJPZk5M5AaoxHtjuN3PCTMPM_z6zHQKpi75NLBxfCntUsXgK2l69_Yoj1UkaiShmRoCwyU7HNQZNBzdsWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=FEAGWQCmc6Kf0RmyjSWzlyb_z-QoViONwlo1NGA69ZmJY-20CwMjmPdWGVE89McIVbMNKOeIgHNLdEVFHmLfg-UqtmFBXRN6w4k9XsX-vEDl43dSWxYvNJUi8ZXTW1-Neczkb4rG-9-u1DTdwm1zyiKxLZmpyzRyeaVS6g8hMiqsghBQMCqG6Kcy_a-sv5g44tVC-vAAxKrzElwvpAIgAcbbDDff6afhQ4WV1p-RI5fUZwbhuSmpZwwDAXC_VzlIoZjSNsGX2Gb0Hkk-tEd4EBS1XFM9WaJdnJKAstHKQWq2pg5W_JXOdExHFXB_M7Vpeg429tNdKEGU3R5asNmrWnKWGz1uhreCYatrwgNyhR0466DPD72eT59jYT2d-EgNjQS_ZmafKsBExrJI7Os7kqanyDI2PgvH6l-7GVVH1BE4Tstt-J79hqJGVJaY0EFdp_7gd2Ktjn5N5GjAoW05nsUggKdek6mXGphru3NbkbPoyu21XY3w2APerKAym6G6CbXFpPBmt68ksz3x-F2CLRvAc_n0A4w4emqdTExLOkKOxKQIg4vnKdPlfZt8WWT8YrlAn62sNTPBWk607U25SfZ1WUJPZk5M5AaoxHtjuN3PCTMPM_z6zHQKpi75NLBxfCntUsXgK2l69_Yoj1UkaiShmRoCwyU7HNQZNBzdsWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwXJFOgC69TOjs1tNnYjkwVE5v9shnKEJ57ZBCL_UnZmNESCBJCD5Xbonf04QZ1nrczoXDTaPxmuvItU2C6jIOZ17p4MPz40v7lgNo71m60FhO3q3sw_wWgX0mJu6Y-_evShSOj7z3GFhvzxdt4rcfnA5R_nNTJ_dLtN6lu5fQAg4Ft69W-rSw66yh0pq7e3Yy8UvaJi1iMpUcztackuxidx902yuVRW0I9o7RPR9yBkd2ToylkQD46XBugRwVdLUUW46jZqRfrslbHzv8mbEO2Z_jHsCmxJjiNtfEDslBCT4d1jGXl5SWIK3YYDwQaWxvyGsop3JQtwRvNyVYn1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=s3ylVaboH0x1vUGDD_Y7-TGKMsaeOVN4cqA1rN8WMGDMt2zQFCifipiVEzjV8neRs9IR8xzGLBsNaisMtLSpEiEQTRN-t0usDmvcIGmA9wAUtR-W6x6AFALX28POLgIsUbIUL5haQqQ5VsALbsAp174i_t9ba_AHlyH7u5W4L5rkTbw7GqeaeqJ5IufCv8IcvZ7yeU2-eMZg-YFMX-abPnbSyygG80516spSRm1R2dHC5kDUMksl7I7gfxqOxxMiXS7eqK08VNMJOJfvm5za5GNT85z9OYtoasH2NlnRz3zrSwIrp4dU6R6263Hb2p-2Mf5y3bouwYvwCRFlhYjPpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=s3ylVaboH0x1vUGDD_Y7-TGKMsaeOVN4cqA1rN8WMGDMt2zQFCifipiVEzjV8neRs9IR8xzGLBsNaisMtLSpEiEQTRN-t0usDmvcIGmA9wAUtR-W6x6AFALX28POLgIsUbIUL5haQqQ5VsALbsAp174i_t9ba_AHlyH7u5W4L5rkTbw7GqeaeqJ5IufCv8IcvZ7yeU2-eMZg-YFMX-abPnbSyygG80516spSRm1R2dHC5kDUMksl7I7gfxqOxxMiXS7eqK08VNMJOJfvm5za5GNT85z9OYtoasH2NlnRz3zrSwIrp4dU6R6263Hb2p-2Mf5y3bouwYvwCRFlhYjPpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjC3LyqvMWxGEajL3cSc4POMRdpTmaBdSWSpBhlsLrkeH1S1YliM8vVmsjibxqr5zp0XqLtHoySg6pIkZzQaKEHXppiBkqjuTYlvjMl9PFhNc1ZoG4tHQ7Ph3S2IEIREpZo6PJNFmjVRZLXavnacMT0AsI_HM8a5ihYhyNg4ZB3ZDNO9Ytr-xdrAPChQbn3iqHCLyQQSHzbOftwx2lZ0l8vVTtuBC-b49uFtj2bYfuNdDCsZURRXX2dBo9KmTX2M9ia-wyGqEz8dQmI2iCfl1pyBSvBtwW61aZT1JwKcYrONU0yaEiap2kG4HM9TWN7V-RDXfsSNa2zX04s2g-XH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=UhVMAJKzaKty3dMN0YywqEcLVuDpd0LluQcUGde1L_aOOYcnexGajBx9R3B1cm-aX7VY1zwURj-mGWIw5x_Tu52HaGaoAWYZpz4tSMtY198YmfvXjFir5zh06Lm626SHCR7vxMLTgFnerEVFXlAtiNENphLDWu8bYgkolUHhuVOKdhXx2l-WxrhxRhQ1Q_qIAGE36gh0GNwiRFtT17oFW42bn6MjJj3anxyaJ2rLq8eCB1WiD11ubbEHdzE25pzRBv8tDwIehAP6XhJofQsNRKuQMW4paW9pnqQFtgVPUAEyOp68xUff8irO10Ht4jAO5JVTdgkb8mYlW2VVlnPcXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=UhVMAJKzaKty3dMN0YywqEcLVuDpd0LluQcUGde1L_aOOYcnexGajBx9R3B1cm-aX7VY1zwURj-mGWIw5x_Tu52HaGaoAWYZpz4tSMtY198YmfvXjFir5zh06Lm626SHCR7vxMLTgFnerEVFXlAtiNENphLDWu8bYgkolUHhuVOKdhXx2l-WxrhxRhQ1Q_qIAGE36gh0GNwiRFtT17oFW42bn6MjJj3anxyaJ2rLq8eCB1WiD11ubbEHdzE25pzRBv8tDwIehAP6XhJofQsNRKuQMW4paW9pnqQFtgVPUAEyOp68xUff8irO10Ht4jAO5JVTdgkb8mYlW2VVlnPcXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=Kk5VjOeTvzn8ZXplyoYNNpSoDUNeK9CfBD07rlY2QUJa8xfZjzD4IUc6kHAV5eYXii1KgrZZGUCJkMG7Kh9AQzkBAlfbnHvqC5O34uprbzJYQsiSCV9904XK6FCCLGOcf46JKT4asuyLkEyJIIP6V1aurpeDSvz05WFlGv7qYoHGgG5Iza9KCrCUwHQEYXHHJgjbhnXVzbia4mVL7FaWAa7RQQlGdZ1YvYKT8tjJxPRncWiq2zNTstRBPoHparMevqF2V8JVjxIkGPrf9GJyFm93RFG2XOEkR79QgBKdZyQYEN72Bt_q6FafJdO5iBvosRuS2WH2PgJb77TgfwLZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=Kk5VjOeTvzn8ZXplyoYNNpSoDUNeK9CfBD07rlY2QUJa8xfZjzD4IUc6kHAV5eYXii1KgrZZGUCJkMG7Kh9AQzkBAlfbnHvqC5O34uprbzJYQsiSCV9904XK6FCCLGOcf46JKT4asuyLkEyJIIP6V1aurpeDSvz05WFlGv7qYoHGgG5Iza9KCrCUwHQEYXHHJgjbhnXVzbia4mVL7FaWAa7RQQlGdZ1YvYKT8tjJxPRncWiq2zNTstRBPoHparMevqF2V8JVjxIkGPrf9GJyFm93RFG2XOEkR79QgBKdZyQYEN72Bt_q6FafJdO5iBvosRuS2WH2PgJb77TgfwLZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=iJ0KX7dgIl3KE7AGJ5vPzqmarHA0Qw0PpP-lM37NFOHU9oHN2ufkwbqfXbfUc8hBk_qkZG9LdQIHknVYSs9zkusTSDOWZcWKRGKIIXhX2Rg0XBZEKdV5hbKr--q2lDhDX_Z-F2j-GUW0FLOz6DUk0gLW2lppRTvIHC-SmgtYV5T7HXKBn5nFtTTakmpC2TA8VK8OpZV1cwZV2nXODxGz0O2BwzswTgKiCz9Y6nr_35rc5aleVgyHuNZgQaYwhChZOfA2vLOFdvl-3jRAKeuGkbBM7U-iwlcVKqjwdDGGKfamjHgwT4X_5lBQqlo19zbqM-GlSajcmrewAa749pliIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=iJ0KX7dgIl3KE7AGJ5vPzqmarHA0Qw0PpP-lM37NFOHU9oHN2ufkwbqfXbfUc8hBk_qkZG9LdQIHknVYSs9zkusTSDOWZcWKRGKIIXhX2Rg0XBZEKdV5hbKr--q2lDhDX_Z-F2j-GUW0FLOz6DUk0gLW2lppRTvIHC-SmgtYV5T7HXKBn5nFtTTakmpC2TA8VK8OpZV1cwZV2nXODxGz0O2BwzswTgKiCz9Y6nr_35rc5aleVgyHuNZgQaYwhChZOfA2vLOFdvl-3jRAKeuGkbBM7U-iwlcVKqjwdDGGKfamjHgwT4X_5lBQqlo19zbqM-GlSajcmrewAa749pliIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayvip1UYX-Y_s7F8hr9GfpDkS5fRimNpFkPBQi2fuM9eXgn2l8-FUA3LGfWK0xQwSHq3AXTOLCvQl9M4nT7mLN8rNQmuSySG7eo5AF4Xw9_TG0LMlhMzWJlCcq6IwpQywhpMjfYDj-_-8UDiMhtqnCCyLl-UCzLfLB7Wyb4KOy27Pav6WZlb_cu2ERwJSslNx4hZKW9u31Vkj4Gbn3PmJaMcsuuQY26HdoY6LzZv0KSvYvfawXwbLgUZUgMLoBz6UO45x_lwgT4SEnGkzjPgxVroxQiGOYcPAWxH-Xf94IXW78nDiOd2a0tacsynE6p63TkZzM5H1m9BT2xeL7qtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVjt6FVSEZNoRWvBjrzxd6-ZqgdJmWx2ntNE3C5E6i5gumqUQeWFscrWMxvyBRzlME5SN7A-tFy0RwiEVkBhBTwsf_6QCxAShd4T5nBjEnnQSocWAjxVnv581ZYpNRwbGzOUKW4snqT7gpK-o74qPyTcPPfiVJDy3b8oC6Bp4TTCKp3ONe2ezJBiSIyAbBLrCS5gIpm0J3KMswc-3xmUhqo0rQ7EZdxpZ8WkrDzXGMkQmqa9VJhbywVnRN_yBmkoz30CKuPFlDuc1n1nDOaj-21PobDGWEq4zVzlXOsqZqNEYWX_0_zPQla_VWuP6JObAi98Ce-mj_vE2qHb7cvJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gmwi01B_rg1Tl5Da_xgV1Q4ofH0Nkkj58K88AehLQTy0Aon73r38FLn4o-cNGQnnLkAIKql3Deq9DXEtwwS2xVehb56fao_1MyKdYtFAitxkVCvvl2nUN7cO7JKKejjCa6Uqw_vUDXhb4c2O8hTPS425uckK0LDUeRRa-_hNKx2i1Z2ynk8Gi0t3RXih9sD0H-u7qUkPMoXE60ZYJdm80QumZkWT2zz2ZAEjtluNVYhB83yiiruyYc_FlzSp_2NO_c-yg4L5MObRaqAvnMjAT8H7t7BEekq3lnH9RPvRHAcJowuGM2cJsn_r6JhuHnTU0XX0i1htAmuFOG_R3afg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR2Di_IXLZaaG9c8yRJmHRouUjtiZwHMANSiq4cqYF80ibnbvgXEdlGlhxL7mh7Meiuy4lCg5CGbvgNz2enQHsTafvwExk-VF8SCtMwcqWW3Rt--GTnidqIa-P4yEa52WyFau-ecuVJH3En4vx4-Lg6YBeuSmEt5n9ESMymISSfuAW62kcTCnKZarF-HeYxQUsnsZnsmjm93JZCHfnXOERtv9hssJlOT63Ykh0QmGgEehK68a1PsZcBG9yNI3x8H4SKXU_AOgeiCFBkJnVg_SVCXsG_D2dNOq_L0qycdadiH_LaOYQEzXsB1lAvHo_GcbkcZdBYeqE8rdeFC_SMz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwQiZyLd2XV9Lw3V7xs8yRqhZpavFjeo5rbZfpLA6uF3NQcmi0QFEibXY_s7eu5DtZLzt-n85xsdP4NAX-v9eGNH7kY5Y4eqOfmf2AKtMJqokujQtNFPGOV3hPV-vaASzjBmbaeXlPQhfhw1HfZU8nZWJI8SNg8WNJTNZrBnX4ITrkfQke2E64YTwC7-YkYH4FB6LkCb7APwhVITeVEOcLkbyr4bopjOt5_1-8MaZmJM_8EWZPe_nCNnxgAsBnCwPt-O7OT9g_TEU9U4KKpBYuozqUYv6uYov6H_E7CE6V1_My2a7nEWKeffEZp5Xr1ekv9P5tgp053j8fkf8N3-8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=Qh2kOcV3puTW67hAfpq5eYBddviqRwzcCuc0-AhCeY7FPDPhSgHnzGbMhpxDS9681-ycwUb0-_fyEftohXnFdAHkFPbadgkBy6-G--EbWSaKBPEu8OxiGozQa06y16ikUaPm7zZyFPPq49mRR8WHIIT8lNyUu10ZeQ5zP1X_jleT9SHtxjiNKAr75pAkGX7SMGtiK5yd-pszfC8WJ3p0MG-2GfhGs2cOoHEhDDWNFboGDSFLvBKPYqLkkzf7HSQunO-yOh3JNbNUYtMXFRfJGUtoeBRTwxHeQ3xh_UhcLNyH0bctFQgDx64KIrEui2x1XUOooyLzfXkzNdMaLsgmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=Qh2kOcV3puTW67hAfpq5eYBddviqRwzcCuc0-AhCeY7FPDPhSgHnzGbMhpxDS9681-ycwUb0-_fyEftohXnFdAHkFPbadgkBy6-G--EbWSaKBPEu8OxiGozQa06y16ikUaPm7zZyFPPq49mRR8WHIIT8lNyUu10ZeQ5zP1X_jleT9SHtxjiNKAr75pAkGX7SMGtiK5yd-pszfC8WJ3p0MG-2GfhGs2cOoHEhDDWNFboGDSFLvBKPYqLkkzf7HSQunO-yOh3JNbNUYtMXFRfJGUtoeBRTwxHeQ3xh_UhcLNyH0bctFQgDx64KIrEui2x1XUOooyLzfXkzNdMaLsgmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=s9PChEEimX3HJYIbQh7_GR7yeNj_87JbqPcTc_J16JLUAWA8Wz3LWQhkL7VwCrx8B9-3omVcos7tYl0z7fyHeAjHxPXqxztw4Di3pM54uXr94W3CrMXZ3HOSvalLUtQfMmsRXV8gGEv__rY1QBKap8nKtmUHsggj1yffpDOo8f0iN7ll59A_wgPtlm5PiZiHGx7z-7AcuqV0QBFPvHTZCUwMyZO57r6Kfp3IAXL7lTSGUXtoyI7CBJ9IgcfQHDvdBHmVyJoxflnzNbLDBTkxErpGrb601cDHhGHuvKnUqHOHHZtqr5Rk5gVpsDITjoc1LqYFAf5sK1lU6ZM_fyLJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=s9PChEEimX3HJYIbQh7_GR7yeNj_87JbqPcTc_J16JLUAWA8Wz3LWQhkL7VwCrx8B9-3omVcos7tYl0z7fyHeAjHxPXqxztw4Di3pM54uXr94W3CrMXZ3HOSvalLUtQfMmsRXV8gGEv__rY1QBKap8nKtmUHsggj1yffpDOo8f0iN7ll59A_wgPtlm5PiZiHGx7z-7AcuqV0QBFPvHTZCUwMyZO57r6Kfp3IAXL7lTSGUXtoyI7CBJ9IgcfQHDvdBHmVyJoxflnzNbLDBTkxErpGrb601cDHhGHuvKnUqHOHHZtqr5Rk5gVpsDITjoc1LqYFAf5sK1lU6ZM_fyLJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1T7OZpyjIvnkwYIKK0LuXWVyTTuWCrGt5C80KOSUcReSP6WRRl1VQXXwem2IEKULsEwNp6aVZMRAq-nor0MYu0QVzwqWTY8sNYQ399CDdrlOP7T6i8o2J2EosFAN0TdRnfzMTVcUp6hWYlB76goT6ctUTPZsAR1J-IhmJ8KkwlBEVWCHq121dYhVg5Jhj_wRNrCphertOVKNzOf7SMUrCbRMNgjyF9_yah3CXZfUuP3NY2BWgvgZcJANnH-MyStUGONOd_jAFvJqOZxggkpuW50Zbwr6bR95mWpGnxAZDZ0mv2nL6jCWu3GbvDMUSvzrSF3ouzo52fGeZr8_1CbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jrBqqmJIeQBlMYpTFpj0MHXAdIItx9MGWJxuTDshPhfvu8qQ5mrO0Ae1p4wSx26lhznkdHGn-rJcHjWdHQHj2b1EzYwYzXYrjfJ-L1UWhM38L4iKsSBSMxzyXU7UGO8MRj-wnhka03Y7x4qPMRLXtLC1LUCeTEr44ZObF-CttG51luL0J8nuibxHF039dYRkSJMH4B913DQMv418XN_B5Md5H8caF5ggEeH13WR4LOKLMQB_J8dEjmwj1GotScFJVrnpunoq3hbYQs2T6dblQTr9gJ_jJ-OB1n4-PIVPc4hF-jN-on9hUr5VzRiUw3jn6uQG-3Eps7TOdSwtIf8Gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jrBqqmJIeQBlMYpTFpj0MHXAdIItx9MGWJxuTDshPhfvu8qQ5mrO0Ae1p4wSx26lhznkdHGn-rJcHjWdHQHj2b1EzYwYzXYrjfJ-L1UWhM38L4iKsSBSMxzyXU7UGO8MRj-wnhka03Y7x4qPMRLXtLC1LUCeTEr44ZObF-CttG51luL0J8nuibxHF039dYRkSJMH4B913DQMv418XN_B5Md5H8caF5ggEeH13WR4LOKLMQB_J8dEjmwj1GotScFJVrnpunoq3hbYQs2T6dblQTr9gJ_jJ-OB1n4-PIVPc4hF-jN-on9hUr5VzRiUw3jn6uQG-3Eps7TOdSwtIf8Gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzx6TX3842Znj9v1C4vG6e3yBK6ogXS2a_lj1_HH12KEBMHMi4M1sBTvsR7syXgEtGjq7aFSQ2OaZbwbxFy-P2rs0CdDqaDEMjssorI_YlgQwXJEQOhQAd7K9Ogy4PjHeeq8-YX1-A-tZSrnc6wHnE9jCSJaX2rzcCC5Sg3m4GSNDrAYHxxU8Rk0iDAQgvqIOJTdn065HmvgY5y5n_36KLaYjFs0kMHXzztts3TMQpn1QsydEl4XI8IJ3mwgNAg8YCUlr7bEfraBTdsKZRqNhSaqbP8vTXaYld_EZ1tMNxQDs0obLXch-PoXeVt1PeufLgjsiWgGjFC0Lpg-MNAMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHX9EFTatjMsRuClii6AjmMIxqjXi8BOVQkUkD9gj7lIIRs9qLx50ymUMzmV2ETF4WCNc1NJH1yb8DcYBWgfGAegevrwWVkLhXm-Dranil7bqU6MR0CjGNzyJyyneL89V0INSICZmHde-bblLFcget61Lv2fBKRvhrtqsky4aENFoi6Xw60NkQ07pvMyBGVzZrFJOWNOTnzBBjb2K_cPAbPZi2Ibwe9tHMICEvUnX3VSowRb0LBCyrYC_e0rJz9UviBPIQEq9953F8yEKFqqOzxRdU9RJdfim_IYqMccW-pwc-InXDtNI7ucAKhAshGvSlBFfyQdNmUiBbId950NMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=QS306t7mUVcpNXlVuQS9osKucWlgPWCq3PF3_OBnrZPreNhk1OLDblCX7ssbHtHWACyO7R9VNC49Ocqs05xk8iSM2PY9nTIi0Vl5n25skPPp_KpApO1zBWQAtFPFoMjBdxTc-dqRDFo6Ms1G0NIkaRrOuuxgrvuIKJMsKWLppJn6vCIkie9Hf9jSYAzg1GixDQFs_8Udz20mvemT65oa4BmmVHzNEQRGDDKvrlVc0fdBzeu_lV0a9kxdlxt0uLUZYBzXJhyJeV4jqGCQqY9ihq6iuKeO51RaMwC8jahfDwbM0_J0SxGgHqGRaRaeCAYCB6Qwcu1uSUTyQk0WVtECgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=QS306t7mUVcpNXlVuQS9osKucWlgPWCq3PF3_OBnrZPreNhk1OLDblCX7ssbHtHWACyO7R9VNC49Ocqs05xk8iSM2PY9nTIi0Vl5n25skPPp_KpApO1zBWQAtFPFoMjBdxTc-dqRDFo6Ms1G0NIkaRrOuuxgrvuIKJMsKWLppJn6vCIkie9Hf9jSYAzg1GixDQFs_8Udz20mvemT65oa4BmmVHzNEQRGDDKvrlVc0fdBzeu_lV0a9kxdlxt0uLUZYBzXJhyJeV4jqGCQqY9ihq6iuKeO51RaMwC8jahfDwbM0_J0SxGgHqGRaRaeCAYCB6Qwcu1uSUTyQk0WVtECgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ZOrYzJWYxfer9aQpQcenFQDy1lQO3ViYrzkYc6xkNizcFsMdDe8NFnzcRKJvvCFZ3NdWt6zJ5ZyFeJXPPzR2vq8D0guL5WF5QPMxgdz-vB-kmMrdWg5j4LIqZrjacnlrEV64mgv0zgjzxm95167i3PlUTHGonSn0IDdem99r7JsehlCnnHbHkYNGg_rxoSJG9RmHRiFq8CB4CC8E877WQwpydWAJrgSN9ixFgdXzWImlC4PXkRi--GbeF-Ysoi1TAcUamuDSc5fQul0x63dZ4VLwa-1l7LhnSqkau3ocCbfuhgu2qA6Hs148SwoW_LHdORDZuQ8dPpU_V6Qt5w63Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ZOrYzJWYxfer9aQpQcenFQDy1lQO3ViYrzkYc6xkNizcFsMdDe8NFnzcRKJvvCFZ3NdWt6zJ5ZyFeJXPPzR2vq8D0guL5WF5QPMxgdz-vB-kmMrdWg5j4LIqZrjacnlrEV64mgv0zgjzxm95167i3PlUTHGonSn0IDdem99r7JsehlCnnHbHkYNGg_rxoSJG9RmHRiFq8CB4CC8E877WQwpydWAJrgSN9ixFgdXzWImlC4PXkRi--GbeF-Ysoi1TAcUamuDSc5fQul0x63dZ4VLwa-1l7LhnSqkau3ocCbfuhgu2qA6Hs148SwoW_LHdORDZuQ8dPpU_V6Qt5w63Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=D-VJw6svpoXZzFL7G2cHVuU8LhXgNwpg4ojgwi6aV6wkwKlp3DoBo7S6l61-z8qNJscH3WAQVAJ7ezHf02zcGZNybRG2n9U7_A1Tmm14nqW-kfQXsvrEsxH6hWZdsR4Jo0pr6qYdUaTXf4NKfeo9PKjzJr_kk7FyhMptR4nlse-bvrohOLVBk6QwDLNntfCq8VNwmb6TTQXHa6KzQjJ86H0weJRz7Nix5NEFSV4Mj2at2Mg3y0v-mlHJ3GINB0FfmTeVGiwimB8XjtxoTYv95sEXBZ73iloO4iz2jvbQieEJD2UhsHgSN9bCEaM22xhMdA8C7CTE-99VbovJ1d5Wuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=D-VJw6svpoXZzFL7G2cHVuU8LhXgNwpg4ojgwi6aV6wkwKlp3DoBo7S6l61-z8qNJscH3WAQVAJ7ezHf02zcGZNybRG2n9U7_A1Tmm14nqW-kfQXsvrEsxH6hWZdsR4Jo0pr6qYdUaTXf4NKfeo9PKjzJr_kk7FyhMptR4nlse-bvrohOLVBk6QwDLNntfCq8VNwmb6TTQXHa6KzQjJ86H0weJRz7Nix5NEFSV4Mj2at2Mg3y0v-mlHJ3GINB0FfmTeVGiwimB8XjtxoTYv95sEXBZ73iloO4iz2jvbQieEJD2UhsHgSN9bCEaM22xhMdA8C7CTE-99VbovJ1d5Wuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFvG8EYXVx0wST3e5QLizDmcBzslhnFyXh1a3rXoQlCFkQCgou4TO0KU6Ss1LR_PbyJWlY8LrBPghayS7kW5MQ9MzXytYpKS6u_Y6yse0i_-eGz7HomwEgIheaxNpdOotFgA15_uBY9gIgf6wBtA2qEC1TuihwpRYJP-Shm_6-7GhF32km5xhB-fdFn05zKeh_Ipa1pVQoZAt0g3OY93obQG4_-DiWqFbRfs1Y25n06n-_Bl_LpteCmyL6xedzj3csycNo72Usrej9g55Uv_1fHayiJshk9-YU1Dlv8NeT9m0W_6ZgPetO6ed4X1DCOCrUn937PCvPh865Kwbms5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=TcMEvj-wmNyv36S7yG9rLP24x1JGU1SeT6uGc8vVyocWLj3rlgo5gb_-4ZiQzgjQCRF7cQhjyiw1vhqwcOUsliTKz-zPxZL42XhmS5wBlOIu4rP4gUAGR2BeiOI4CujLP79Mqds1r3C8wiz_Tu4t5PkgC8NBtF5-fx1c05OOeJWVZlYodeHk84v09h1jKVQGtMxaOMBIcpM5sh92v-Dd_qKZY-LvfxFOH5dL9Rxfc4gYExMKyg6KrR4139TXUQn7c8NBB6nCqS10fpKyOvWRA5jA-38uIyBnBiqiFIEZZ-Q53IcNEwQmevsAJ86vXdSn4ySqIb0b-qlAeyK700t_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=TcMEvj-wmNyv36S7yG9rLP24x1JGU1SeT6uGc8vVyocWLj3rlgo5gb_-4ZiQzgjQCRF7cQhjyiw1vhqwcOUsliTKz-zPxZL42XhmS5wBlOIu4rP4gUAGR2BeiOI4CujLP79Mqds1r3C8wiz_Tu4t5PkgC8NBtF5-fx1c05OOeJWVZlYodeHk84v09h1jKVQGtMxaOMBIcpM5sh92v-Dd_qKZY-LvfxFOH5dL9Rxfc4gYExMKyg6KrR4139TXUQn7c8NBB6nCqS10fpKyOvWRA5jA-38uIyBnBiqiFIEZZ-Q53IcNEwQmevsAJ86vXdSn4ySqIb0b-qlAeyK700t_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=MSqhLLvMIG9SGJ4cC3AyKLa9vpq9lgPh2qSjrxpCiQ6yI0P_NF73LOCMkSUdHWIF11FzjB6DXhwx0l8GpkQDlhJaPcBDdn-utxyD_EH5BzrN1Du1H7WhjT3MMBFMlgy2QpilLE-IATz_eX4zKCTRCoTB7qycs1zX6_kwd98dJ1P-lUeTYeZNWFT0iou7bweUDKk5cm_e6zhNrdqEm0Scla3zgebcGlOpVOaZ987U8NDWXGg1Gc6RXTh2h68EidjMQIextyjTdW8xH4mhbAtoBy9gvwg_30rylM4ECpHULEIrjGUtwVYIXy65_0JH1azPTQiq103cPw9JU7F8wipUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=MSqhLLvMIG9SGJ4cC3AyKLa9vpq9lgPh2qSjrxpCiQ6yI0P_NF73LOCMkSUdHWIF11FzjB6DXhwx0l8GpkQDlhJaPcBDdn-utxyD_EH5BzrN1Du1H7WhjT3MMBFMlgy2QpilLE-IATz_eX4zKCTRCoTB7qycs1zX6_kwd98dJ1P-lUeTYeZNWFT0iou7bweUDKk5cm_e6zhNrdqEm0Scla3zgebcGlOpVOaZ987U8NDWXGg1Gc6RXTh2h68EidjMQIextyjTdW8xH4mhbAtoBy9gvwg_30rylM4ECpHULEIrjGUtwVYIXy65_0JH1azPTQiq103cPw9JU7F8wipUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
