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
<img src="https://cdn4.telesco.pe/file/Ei2kjxsPx73bAWGtPL7ObjXUjndd30NzswBKv_fF3Ey88Z3SRHpF7V_QUtSNZvufbiAMwW7zizIXOtdtQqfSdvf7wqJgaM2IaGQwQJDm2aajJBZXZ7Nq3Y1suLJaomKSIa-mz5ruunCVQZ4CslCDMVwNg2MAVTMd3AN0rxdoGfUhHrl7Qsxybe5hK12J2gYCReJjt_UlSV6i15H2TSKWW8n9NIu-LPnwKUsarwoUCBc9wiYQ1WIhVqSpokPOQXCNoK2xU7Pus1EJYIu9k484xAwc-Tg695wGR5J9aoOE-U3cDe8X6mAefvkWppzdHZmsZOGPhUAPx_H54sOJKVs5-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 615K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg57VC2dl6MDdldvXFnUME54tg5EPOCjAcPXiSa903HPfqYmKNdVrusgyeVz5wBFrvEKuasSfL42Iqy_OstvKHPQZ1-DgVLjTAPEDskmisGyGz4BtgkNlrQuSrahMU2pmWtpM0sn54aJSdL-IdcxcJDbB9gM1HPuXJ9BG1-v4fWKKSOfyFXjZpK08KBMgkyYCBpxxEYDgoBJvM873Ar_8NdyDCwyv9bH3efUr-g4H-ILNJvbBzKivAkji_btzL6isMVuxdeUfTQQMnyFTd7ubdQ4HIJYzhAxT723uXjaGX627RxEkr_y0GewZf7ZE9iek2hjIRA6kBd6K7Rb093oEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYbAmjL4sNKBornsB6Fh5S_Gwp7qnwMRSLtzuaZv2LsrlncxzF_ety4gFFeUdHYBaaroLKCZdABp0J2BQbHfgDi-j9ZPfThXCj1RLf21ioOyEz3-HJzvLdX_5dFjP502fjCBLTs4cG48XakK7tFoSehsOSuClGw27j6Iv5N8FOPHITl2jLuymYRvgUHjP3qHFbVT3SuMoXhxCoszTC-LpBcTir9AJIaoAd43dH0wVvwK-c33pQE-LlPINEe1p_d6p1dP-Dk04jGJ5O_EaR4OpQv9pQi8nWmCkc5EYcCOjbFzfZZPNSfQ_HX32G53pzz0gtLARKce8H1CT7emdBaKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOmYQLjhilLCFm6eghSEkm-I_970Ah4LNnMs_Hsn39bbQcQyHhwrU7wcxglVJ9mxUcAiyiiljL_lqmZ4DtHvBicvqZ8SxnIRmo22xNuAt2zPRT-VzebVo25P_fbbiZm30qvQBVqG1W_wIX31LM4tOOilDbdRy22S24j8EI49wlweNrjvlV5YGTZKuU92JvaVDtIz1oW6YCQ84ggMhj-PH65ALRvhWwAEVkbeBnLhM19Vjnqu7rkKIc6bl1Y9uyP7EplCicB9hSHdnNlihm_I-CIUhatuxJxqFHe8tW9Jg9M8-V7-UfjgaVNurKihRtnThLu4DpN8bsEFAVvuaP2nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYIRMWM_kHJcRZJ1Z88sriSTGIp0UMWE9gq7ji47Q_TzdxWZBa8YIniYKsF_XFZypJu_G6qlluhtjzmp-V3aoXKZq9J8Ev8fKMdJgnnBFALpxFOALd-NqzAnqkJ3vyczJtWp8LHn21yKgXn4mP1jpgM8j3s3BZUO7ev6qbp8cy0Yeot_jMR5RhLlhphM5Yl168mFQ8vIlEkfswD8FgH2p2-EBopBC0n7vBGkr7w8QV3jlUEKByut9sW9xHm07tjEteRVhFy0-pS5VsgfBJrZ11DJZzq_wjF5imNVyY_JDqUg2T_YDNKVatNLMMt5-y_kxibewsGkwEZolDdiOhbkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال‌سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت‌استفاده‌از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/28809" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW8VcLzZCFpHKb-HSLIkR_y3a-q3OQ0LRNg6plybqBOalU-wdR5n-GAcNkCf9xxGGIslomlVaTmF1EEnt4aogaQMYzqgKIXYbqTekvDpdiKaVV8Dp20NMktPNUgzFsUFWx9VGXfqwVOoF0DCE8Adt9FVLfWZYv33ql-Rjh0ZMSNDcizMbP7Tq2zD4cIIcBPOB8ilD2kRlDktuVmPDPsn-cf7sxqgzS-KOVmcYuO81cJKdFMxGgTtXxH1ZDiMXyMQcQpmM8xf1u2qz0pPAKoccIMxbpOJBwv39GcGCyEQ3lhk94pMnVFuKl1tAFsPu8Yh2ju1No9bQSapZKSNLUlshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXFexPfyszIisonRZmTB5grUmmM4V3LaUXYgFbBJZ8C8cDIfkttQuXqULf67QOqnp6QIN-vKngQoXqdk5yRRddJ20l72hfNJ4PtkD_q5DVkTpEGLU4l9is-xDE0ANsIENlMvqCWFmUZSJj8pdI3TS_HFdM4ncKoe6vY6bQ9AmVcK1uszRaS7KGlnKR83RpmSoaLZOSg-ZbcFfr0J7ParAFSqAnXHw4DdUvgoyy2nGeYinz1k_ks6eB1nMGXcFXvRBAHyzfdVqDxBOYUlEpMaHuoiHW0ltjYoI7HfS2Os-Z3Dmwczp6x5drWcgHWhGGuta-ItYNN8-RGDzp7xpMjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTDdB5Dc-w1-X3eMGHS_mSVBEzwdOyj70FJAMEaf6csCz8tmNoqhcVARbNgxLDjdXORaotlIxphe1IM8-dPcSUo8cvK9ppnxjTiI_iKE0ZxSY-xgkqdmFwH6GXXZ1HQVHxK5XbhANvbYCI5pe2yobE7_KnKtCdm3kfucCKZkLF_C3FdSGtoNQhW1-5wgo_YmYOW6Jv-Cu8So6ncgIB-3tcj-WI6Z3AASbcTwsodoJbbdJyHpabFy6ZTbeUHwxlaAdjqWmQmVPyJGjcO-OZmep6vpvUhKYO9QKkIeqDKk-hXMBlUiTZ8q_RGHwHnMuIfxq8nTCN7Kll6D4suk7m8Szw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5joGjoYFkE-vO8cK_WLYvSDarCKqD7THQ9UM_iGOzTTrCAiibK08kLbkwQJcEbDi_30G7iUvv6sNTYkfP4rOyMU2q6SEDi6glQLeKtXijnJ1gkhqZJtNjAeyyWpi2Glat23IPHpCVuXn9nOPYVRGeZ79-TillczDWye6db_UGHHQ0tkEBGSPUn902n_ejMAqe34YIyp9K5e3Bh0Dc7i_M65OpOB5nYotnRR3M8jLNcZMygxDyUGl3KALNX4Or1XLAD-e7LFWeR1LvqLuf78VlNmlm1lOXBZdbSklRAZzE9XBYMQwForMp3f97eUZhwJoLhVxFdZWWTwtYhN8F399g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Zrem8i5oBQrfsP52HTY1BX3hL3VWcIv8SbcTLVADiY8tbBrNnwHdinxgJ_DhZcoEHzM0o99UFbMGOn28YTkqxvkVfGjdK2PtKCOtUi_SrhKkMJ5ZnCWCtjKD3Ss3snvGZnpTfIQP0avXrUX4RN_fhFOn-wPV95bxzIllXekq7NCRVo6hVEfVRv0Yz4D8G3qjRPiipIBb8ccUmY1cHqluvDTzzN0xBUiEoPcjkaXlBzQy81htSZUe_dSg6IV1dHYCVZx5L4tNGIFCefIGGKj998p96EgwsJXFALp3cb46GfHsDFuN6qpQwwpJOuSz_s5JPA3SiPNEmOAGpseWu5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiE_CleKzn93ZChQXjAW3DYoKCnt0poB_GV7vs9AOHl3wRiD1FurBVilS0fXCtvBLNZi8smYtnyKV4avwCNbCXMhOhP_dOhITMTIPp927kzY-gkmzV6rZV8VxVRNCBqRBnVFsLaRh4eD4PiTqr7mR-5UiqUTbEC1BCcELdpJQJ5TRpYDkg983mNvNSgLImwMOha3guqfJbMNdjmgz11T2c9NZipq-ibQH-e157P8ob7bISYhy11wK3cPYxk7WxXMlaM8jv_9y_BZZ8u3zgje6eVfltpnYimnM6HUXzg1utkLUslfE1NAWJqLXAtVLuSgt89c3PwxST749r9892Cw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlnvYBHV28krSJ93fF8Eo32VxGyAuJ7N3jUUu1YwWe0AfDAfOWQYeIGBJhxwcXzGqP8T7IVzWp0r3SiqOGFlB1cGW9hpwc6eu-btL1HXlPuAFaSk6-pWMKqjD4-MwPmoXqEsWg8lokYaLu80fhlRa7DR0uf7W9nhVicmAK23gng_m2mUHLoWSaCBGRu5PFscInTZoSE-W0KFQcSHG4zdMVh-hBzX13igaRPR2ru4KGjNrIxPzP6iIRBtt_U7L6J9OmL6ErxdKw88A3X4q__OLdCANQmj3l9b2HeNseMyze8Tm6uAr8UkiXPvI52fHkVj_DY6QGWXoZmixmIyACwTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEVnewy415aCTKgIuNy4kKYVqYT4VjQKe_RvVDoNNRaJOQ1qwAb_9RGmutOT0gKTU0zmybgcGiTq-l-9XYEtFfBJsI6o3ATlBPK_6nxNaXB1u5lqJiijMtHkEhkw7WPjWg6YZmbauu5hLsDmhn0gsR9JdmGGDyql2E110VVbIKNNX1m1ZqYjgaE0JfR6MieBd_NztgC8xNMG6y1zNSicNzPN_ry1iRUV6JXjd9qgjIOkWTIurDr4YVsOh2I_DmwtLXApT_wmQjXiWyp-QD6xxtc-A92lBqa1EuIf_yQum2xt7JIL_o0ZZFD4S5TmeC_q7ukKW7Ng_SzdJ8PlxF-MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVSFt838olAQsWaX3YpisNwxiKfWi1Y9wJHXIXLAKQgrTbCt-qgbyqYfXqqWmsdHT9tx_4Zgf23j7u99B9ac_9zw-8iS1I62JQXlbmppVTvcU_xlpyG9FVJWEWhzia-yPa_hzS3nunuvh7zLhyCdUkv_eYsJsDpCr6Zjcjg5dI_xgNrAYekz8LnPGkgHoKtRbmFRoc0mXSdvlsekk35DOvFfPQrhPY8IM5KydmbcWz_sFc6A4OeDBun2heZW-4EdfpeBuPn6XN3NlDzR93K9vZKlzE5pEC-V3p23LG0NQoKO33TcV4NKa3A3nifa4quegNs8eUfdvOQwa7lbQOmlyNqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVSFt838olAQsWaX3YpisNwxiKfWi1Y9wJHXIXLAKQgrTbCt-qgbyqYfXqqWmsdHT9tx_4Zgf23j7u99B9ac_9zw-8iS1I62JQXlbmppVTvcU_xlpyG9FVJWEWhzia-yPa_hzS3nunuvh7zLhyCdUkv_eYsJsDpCr6Zjcjg5dI_xgNrAYekz8LnPGkgHoKtRbmFRoc0mXSdvlsekk35DOvFfPQrhPY8IM5KydmbcWz_sFc6A4OeDBun2heZW-4EdfpeBuPn6XN3NlDzR93K9vZKlzE5pEC-V3p23LG0NQoKO33TcV4NKa3A3nifa4quegNs8eUfdvOQwa7lbQOmlyNqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGpSWvtq5KXFNdhysuERKVPzQg1Qvx4GJpxB6jZx7LpCQnSCT7UVQG9cN9wf3EfDq7aor00MbPYfujffOCZ1PiIUEECT_9MD-XtF3pWn_unknfldC5xjQ8QCg-Riq-fru7MmrlbFid7f7TiNuID0xoyyfDK_FMlhbqBQzxYxlS61EqGgZYHXrjCmJOdXUXsOZhFVSxru_bM0pIWL8OOupPkjBGXc1MYJvmHqGEjT7jFnD2xnXbSRYU5Me9vbZ0edK0Luv9cZnYldY-4gyFctsPoGkrtLfGOxWDF8O-e_MaDiSEDLjMgOWu8Adv-OcEO8kELxLOLh3LyMmwYYvBzi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKrRO8S-gDsLpiVYn3fXhKAZjOg89GZXgv8uqCBJbZjGTlSrBRNQc4CD0000KW01BEX4vQf7iNXDst9m9WRLuRuReCuqg256PhpvkNnj9_CfyK5yqTG7CexMnMO2jhLE6xcE4WCSPgwfCMYjlP6MRVPwcwHxT052tBNLEiOoqc_rVF-tyri7lgqZcdRUHe5rGQdVi_bnn4OaiUs9XE78J2p5vDdwwcgHU4WtI8OtX13xJ1u65MUDJfyz6IqIXYKttzFW8K96gS1NC32Rk3Rucr-e8mefdE3dhsvHq2nGWyvLr7ez77Yc0wa_t5W3zID5vSsvPsiU7kCrMgmLk0WajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icXvjE16i58vRO2a1Bzq2AorUzNpGS9o3NPU5IQYPgukKRUd5UGdUPehp7GnEm4BJJRcuT6JNBgPY3hekjePc6K0ohSxcI8XVbjc7QiO8u_6sScQYeC6ug6eSmpCJ09eII8SwukVAQQTJeHHv_0pXirhm-jcqVFyxOR2fOI_k-eX8hbOtlaytzwJaaBA8vhGoXWgPJ_BhQO56md8YPkGnk5pjTv-R69L1jPvYgTzPO5X6k5l0u1G9YXsJuyyio8rjQG_o3EZRoHb80GLvQ4EEO_QfQt3d_NjmoTjSz4iI7HCb8_f7elS4_kuvwyGXuMVfmrn4P6RW5FYZ7Tmc3cwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HT2LaGlrYPbAwcGB9G5TjqFyR93dWLJ10z6uPQclaTFFEVg8gdyl_dfkGGUXwy1Gu66eS4mQa1gCjOI0ppui7sjcPl_lP2dYU9NC6uGiD_97vfXqlVZGkxDoiDoVxLB0B5d-Tdxrvy_5TYltGF4I84E4LZP8n881GOxkMLW8BVBAHmLv12OliPK0c_MnBvQp1L4GnZO80m_KiK-cLoeQMAGrNJmCUihVBOHvIFW_2C0YbifCqMT2T-e_Y97GwDAMcpirE9H3bAWZ_80jIL04Ww6z9pMhNJPlrPrHqHv0ZuXvtZ8XbyPpP0ftvDE1kGb2F47d6rXaAPm8dR3t6nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0K9KPZNrTZO4OyfhVqDzj7SzIYBK_f_XyUTfXg1fwZSQvg5957uB1OjdLeO8obPKzDL4JD8E6ThXSBamtoXzb-vbUNwRkIUxkJcfKfMKUW-awfAlstSED2RPUmo-R2uhleHq95OWwvgxKZ07jmBzvd9dDRYenkWrINWN6AuJcTzPU2JVLjeVpmzoV8zW7XO3ARHPE_XuqpYOOSdsDUOd7cz8RV3voNtoNIDinyZQaRE6-WBJPxXgU4oIjegyR10KCBbgYOVFyLX_pz7c567l73YSqhZV-6CBf4na95LmFLLWfFlyW8ZL1HSuJ_YRFdC2geka3SxA7rhT6QNaIsHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=e_LU3pecPzGbXjR0_3fxVvJlyWcpesotzkmsxWgw4RwdexBZamWMCuqfYaaNVa-PzJKpoBX1C9huMHxI1n5WPnlf51-llR5KvYrCi0eEptRIVrA1akOOEqZ3LdlDnOVZUiKHafXS8FzwoRMVZN90GUn8pdThGN147duupBArtBGw_Pxh9MRdJlU9BsrLctyivH9YaI8GQgZokHyYJgY6XJeeftBGbsh2nozz1SYWGsZZysbmc2IWJF-SPTr3SXOJ1-_T6-7YCH-KhqAI40DvTM7ygm-d9IzcjYNl5ljT9ZIp17-HCuR2km3v95HO0_23qBb20IklKREwbkZQM5MJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=e_LU3pecPzGbXjR0_3fxVvJlyWcpesotzkmsxWgw4RwdexBZamWMCuqfYaaNVa-PzJKpoBX1C9huMHxI1n5WPnlf51-llR5KvYrCi0eEptRIVrA1akOOEqZ3LdlDnOVZUiKHafXS8FzwoRMVZN90GUn8pdThGN147duupBArtBGw_Pxh9MRdJlU9BsrLctyivH9YaI8GQgZokHyYJgY6XJeeftBGbsh2nozz1SYWGsZZysbmc2IWJF-SPTr3SXOJ1-_T6-7YCH-KhqAI40DvTM7ygm-d9IzcjYNl5ljT9ZIp17-HCuR2km3v95HO0_23qBb20IklKREwbkZQM5MJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZb6Eeq8-M6vlzK1p6g_GEk5hwYkZ0Z9Yz2Cv_diBwiEcWOn_ljMxI_WMsfTd8_Cfy32YQtPzH6gAueNJE7qLNNSL-ZaxWWWK3HgpixdGrU2EZOcI-lqaS2iAWw7-TYHsDPPHIR56d5eFXyJ9XjaqvaVT2Tdap2OEozO_zKsxh4WViERvOglW3p0xKYL16Bptkj5YD4l-MRg3aqhgxBO56zZ5O7ngEjuedbWbfQjkni6NxXcOXi794TvBGSJgIQ_asBVUmPE8RKXbsW6NTbt3nFN_fyXEWFISPWXzr_ny06Yi0gHVVkiQNz6FApBoX7mYstbZFA47MHnMlgLlazUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXJSoBrsmszdoVzI8ZT7Lo5sLGGHKvKL0XqqGgQNoHbbAZdfFIvY1-GT07rR_eIQQ7os6VdfReHXFVKZsQnoPdBbAVfpiLhp1-sMXkTUfiEZrxHt0Q-1btKQDZCJiCJXp0hDYd_Gdt5a6q8SIsE37dPemh9zW9_GF_bS4Us2mArrCTZPCsV7W_B-BKKbNaJfSRGvCMHbTbovHjis171gqe_Lz1E2sdYl4668LEhxLzeQBcGxv4j6B88LcX5Ke1FOy4PKakIfZ1nQdBHgq2EMyPxUl2mozij60C1KZikQrKnuJ9axEybkk6gsFtbiKkX0spnsV_dnQL4QL-IgkfabxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqxZWBc8W2PPBYv1r_RD2PQ0O4FRQinjcSOtw5uCREeG-ZO4cg7Htuakw2dh8IeTZViRWvTCQ0GUgHrXniDs7HW6ut_9a6aJir9jBgzD7Ik0A2InFvUB3gcEYfaH6_yIv8vG1UV0sas0ep35CcejXcs9OHhWcYQAFLVf13AefZEmwtJee6ASXlH_924a4qE9Bg73JcgfCOjSuHrJIdZm2suDWb30W0FUTNbkUp-jaB8HDAzM2m2AQ-yHAfWKL0UAVdpvTDReeWH3h03WKs0itBPgAiAyfhEGnEIgt--cImbZ1VbjQmCPYn9jz_661CvKdFVUyGvli9ZFub7v5rLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-sODR8ETopMqa89Aqz5SCDWAko1_ezVjrbln30TFayQuM3A1-KiUFy2P1WN30bkXfwdLR2ueYModry33sY0xNqgJ9QBnbBDYFjHVw9cDgDPJAEtiRWypB47HtVAfPGzR88DzJB6hoWaqkXHOSKCs-rcFY3fiF0Lkx-2wzctXP2QFuIvuCjz8wxtl0epNcUImEESGYcOAULckacKNi_NyHWC89ZjnYc-Bwux-TAn0UWriZu-XQ9G-2tKXKUsIAkqoY6GdKZezrX6GKk_sr2XpE3_KQD5z_6stqzTIR51sHThJWsAc77CFIve1UJWUXwAmyl64cAL3Occ-zeNu-8o1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqYycztowjz-UV5T3EUQmg08CkDKAtNwuFP78fyxQdK_4qtAzwuGQeZXCUhiGQRoOawmhKD4h1J0CYS-PaLERNZZCYunEJnXkjGeSvwDZSjmoTxgI3C9Nk13bfY4h00zQSGWpPYrzqfVv6v72ReJuNoBwJP-wRwp5cEInuR6PDOMUu96Eynic759zfTe9_eyYnm130YH5nRM9R6uDdoHUslnsLeIsojHoAZnjFeHEGapFwwZ4z_9oieojFFLxcdjxWKnw76SIrMBL_cv0YimyTPbHrE2aY8NnSZPqIyM9FbratVzN4QNeHXC5MRnbkMco_cuNCNUlf5sLX5TXP-7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRXVna7QKwHekkX3uumDSr-b8vmo7U90nWAdgD51AlnHbdwn1tP_wMxBUQ2OlfO0IlNEDSc7IQUAwzUfB1kO0uYVKy4Pq8at6rT0q36oUVqGCVLnlZAQPQvQlAhmJFGkZDClatWulEiosK-HZtEH78Kp0XkauuTin7DWgvoZlR9nVdAZX81FFKXMyB1pmyxGiMrllaQ4fgoS5XARr0yuq7cFCCYgYqNSTkmvnV2VDOTDRFIV6iViSou1CSDKdS9QJFJ3twDBMYIUnnNNnBzPgsqXUksrK1BsGED841RtUwKIR8Rj0BvvXYgAqs4I6zoXq99GAS5EGxXxVJA6kqLynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28784">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD7eMuLz62hgUbQi1iEbvA5V9B6aRzuW43WKBj_A52D8MhAxCytQw6YBRot1X0GRNZiiLzws3ncCyrz_av-zZHWYJ3xP-G7xaqpzyeuwwYo16aTNlfaJtJntyzVLKBx0Xc726Pgvnt-VFPbRwABuPRMINFOHKisLHqT_xofG3XEctzm4fiIvJTeyULqdHzXIZqit74-_L1Ms_LAEOABxtb4x25oxXkL9eorv-sCWrf8kS4IbccZAny24bK42KJaNWqC0kcSwKzCbgNlVWYrPDeBp3H2Acz3bzcmrQmmmzE1r65L7FnGnGMTdbjxPqBvpWla9gCbVyohk3qHd-ZDKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28784" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZNOi11T1lvhnrZwFV5sqeg8Rwkjsncjb_1TMb5aaJwOBb92A5g29eJ1Kx3O-T_hn6vUuJgHomL9luedIA33pFLMeyZGmrPYaIad4XcTJ2N5TM3DRfZ_V83Nh017kDguRLFjeOk9JE13th21Ur-vzGUwdeKvB2pPGu_toeDE3YN_S_H8Q-4bldenMpcfgmoF5F6F_xbAoIyjdITegPZeXTB1q6sTLP7SER-BF_ZLexT7yTjFu6L0TU18hBv5NGR0iNSSyLF8LNeR1XCAwZpw4ZUdo9R09qLAx1iNfwZD-Xgib59UDb5SBwdJLEgW7dizDuP-2JuzFfXcSA-H-1bgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=Lu83kZMu3JYG6VlCPxcymR69Z9nO6qcliW4Yq06DtUUGkbB9Y3VCmLEhYqIqhe2iKfrD51zJt2fU_pzu30S6X-LWzGec_Qrm9Ix0DujhU3mFL6T2u4X-uNe3y7dOYVQBfNwByutKifU6moKFCIAEL8kUGlBV1ppM9aPg6o40HYy4_hkz3AC6gU9qN7a7n_NMMd1uqCOqoO76wlqbrcIUVtr8zgW4CWlYfY2TAZifkQVEBQEH3fLqf9m1yTlPfD4KVDB03M9F0TOfZCllmfNdeJ0m9uOfuXj-L-hdfDtT0raunXhGEsYHjNunE29iOGUPX2xBP1Y3WjcfFf6H74gw6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=Lu83kZMu3JYG6VlCPxcymR69Z9nO6qcliW4Yq06DtUUGkbB9Y3VCmLEhYqIqhe2iKfrD51zJt2fU_pzu30S6X-LWzGec_Qrm9Ix0DujhU3mFL6T2u4X-uNe3y7dOYVQBfNwByutKifU6moKFCIAEL8kUGlBV1ppM9aPg6o40HYy4_hkz3AC6gU9qN7a7n_NMMd1uqCOqoO76wlqbrcIUVtr8zgW4CWlYfY2TAZifkQVEBQEH3fLqf9m1yTlPfD4KVDB03M9F0TOfZCllmfNdeJ0m9uOfuXj-L-hdfDtT0raunXhGEsYHjNunE29iOGUPX2xBP1Y3WjcfFf6H74gw6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV7KEjGe79Xy_LdSWosC0tXtHQemej962xR2mAPxBYn_DTUNaApnWq0dUmGsaJ8PP0SFchgAdr5DHrDN7DoAIwaWVy9Er2KBFkIGVMTm_O9Mb9o42CDD3gVmWMtnKcpEMoFwZ0NIEp2NZU8Tp883h5juI2KxwqfDY-id9uppia2PdpFAlKmo46FKknW9PhojuXivfyz2E6E7Ug7gQWPkO4X6JNLhctCdrLAZu8-eFh-bJjqvzj4wPY37uEHiOxiy9tYPrTRad_ZEvvxjeMylNAMkjZv9UxbzhwMXlbysHU9MqZgLC-D2QIGtMC6dNRPKEC253bsXHJt-3vsrNRCIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc559k8gMYUsRPVJg1hh2Hlsz0uylS6WSg3XhgKQlrg_lMVouGvkrSqjDky_UOoComtVbrnYu6r2R_1oYl8zXM27Y7LyOd4J6bXOnHOjNVBorzxdM4GcGSagG4U1KmKf7OmcfO3BaaF0EmDf4zTLYF_fFb5Mpsr8Kc9W8gR7T6rPAaHuFMKf2DhyiFax7f-LLsDGsdGo_LovVtJ1EpZQOQnTNsV5q-L43f31PUiPBneahoybJ6FZ7Zzq46molPqsYZ59ENBhqcTgAvaZmghNFVNzCeECLPhoar8KovUU8HVU7h38DwjaIb_yGtJs1gyK4U1xgLX-3Ry1sZ6KhVnu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA-r0dwY1xv4THZRrgzVzmtWHfPpJSXTSjlH5v2wrgLRi_jip4HsDFu1-rSUOW5e0TweBv8UITXsVI0IloA7Dv1Kz1MkGj0WZUwRywAg6uvLsTHtVPhFgu6iTE_GOxERILZEqOem3YgeD1TBc3jyvyKbPCMfanIsdDnHzUvmn0xWyP9gYUEzxzjatsh2IgBSNFPrkTHYq1da3DUdUtA2vNcS7_Hy6ABvIPi5XcNkimy8l_uRl1K_zGFfgjyYGNzlqRGmg4AkMAG3Q3c9wZGRP9KscrtpEKkIO_lybLUFZOW4IlRPgcnsno1StyXgP3wKYXJihcBiBpYhzWwCkbAvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNgMu_rvyCwf-6sbUxtEJh--h6OSToF2tb5DHAsuKG-jBRYl4U9ve6S3_65_rXjWBCIGNaw--cv_H4eowA2xgkFfVAOcXdVXTaRRh1K6PrC1vTv8CM8lVPDeH7zp4Cn8-yD0uYSI9XAQRs1TMyXXCRiowa2_pvIvMLEPWcPQjCqZ0bw4bXzHb1BAuB7tjtVkBhJJE8OoxGHxCJWzs1EbhcQO7GxZftmZ6uSZAldoCi6CiVq--JHlVjhQmaMTbtZwN0IhbuNaOKTDP1zEqVH-LZ3FfCPMhYv_ZT8kpafHfmyru238iYWU1nBPHZG9yiPSxlOE_B0fxe2BxO67PE_sNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3fcjE_WCco4htmU1BJCrTUhCpxJxbBiAJTC5bx4Qehbmo-IzxGdP_70vEZFWWsnd7IvMrRG4O32BdIPst9vLgyDSzOZXB-iNCpPxObGSCPdjJJDiW53XmyDKnkgHSVPH2tnAtI4XKZcM_DaihDvisuD6g1DqowGrShNaJsE9bN9CTL_XP3l6nSrPkgMpJkbafTDD4a1UfG1qrnsUIBSkcQctadzafXrtzbh6-t-lVUmJGQsYLIPcRM1YGqOFFobw_4QW11n3Pq3cizAc9xjitwlfoxgEx78a5J_vn0aQxTZzka8RlISQN_gPrTHGtTDyLkEf3d_3e_xd3xPVk9lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT8BzmYXX1Zw_D-1OI8iqGtpULm9CQJrny4YiPwqCV_FcplqGucp94ogIM3T_pp7VZNPy5wJP0XIPxys9CQBP2oMLSB2M6RW0OHEpEnKBUwqzTo7w-p1p5p6OefpqjzwbhNC1LYxFQkc5-0miNsk9frs00HWmbgeWgUal9oK7h93h00e1vVcgRFMWOb28fj-jef_4im0Vuq9b0EHCfBY8INV9IwhiZIlUHmwgqHTAIuDOf-6ZlZvbCkgsrXpCUekeMZMvgJU3Mw60qvqym6ewcrC2o3kZ8MYP-yqsiD9tcp4PQ5uxc9dJcc1NXse7dMcIouKxV1nYiNa9cuXDUqfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0iCcYbX2C9Y5W11vrVIrFjKGDAG9fGgph4N3SYl5JqxhB_HxVB3QbzBaqo8U6NcICTWtCo-poznLDdhdMIMWjii8y0-SHud6Mveyt3pNmmCBjR5Ts33mp_FKXAwKHe5QoE7dJCHmzVWF7cRzoNj1_TArlqJIZlfLASjcQXs7WXieHqOTF-BSfy1RCgje17wy2Mbp-M7biGh27UDGsukh1M_0arNiukPMvB_nWoxP65FuC04IJycqLEZK9oG0_hPYqgLkwXXR8yOe8_oqQpAEKSASyh-82zfnSTj8I17c2aboa-1zjSWAlwXZbWH1x_XHIPu_lgDw-ce_u6IAR6VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcO3EWTVkuDe8nn4Vc3dBudm1cIqQXRubH45fJ2Fp1qwqCnRiZEGGsMx17KkIJt39o49LHYZn5X5_WnIDX0nexRSiGNMmEobkN_ZkDIiDcqP_eXsSvAZKe6e5wDybvuHBStPvpJrl-Cqsa1BCqtAX1iOiM1qLGj9fIeHCij41zL39p-OVRN3HFqu49KxGi1oENeLG3TPzxt1ekOaTyQo3UYC3C7d9T02Aj628RyeffVohw_69cJDh7cEVXnBO47vPSHJ_zP1ucaA6Bmi46CrBQbRU_o2ZTmuPurrhsjUGoZJmBq5iwSTnM-E7gqNhJnM6zR4QRolkjSmqA8RujWX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Tk2c_nMJFKforT4LZFsgqb7iDYhMNWbeLlDNVr_4ljrWJ8_KzZfg6V4s-5oSvm0pqhKdTOHdERI3wtk8J26dFBcDjQ_GZkSSZJaUnXqO258gKnaUDCn11GsDsLZr1Ywjy3KGGTeYQXKH_CgWoNITKMUVL5LCx6asDfVQvUw95LmW55DJoIcT3x1zMCQdDZhLdEpat84mfhGZPB-3eEZ6FgYrl81xD2G01stLca1fVrUpQCHsZ0CDi0afiVEu2FWui_O0uUWw4KRlTELLRWQ1cN1sV8VDyAR_7qCdR9iif59ODf7LbfHwmDhhmA3vKSJqO0ncDJXBXi0-osLcO9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxiyQtnhMi5YgsR759pLK3azxWQXUXb2R9Nkd-iNaX7nYMfCelVaZUkJ47sozfq4uEGyv-qGuf50ZJ7XoP5ZvDj37srK4c4G1PbM8tTBHEz5SnCOhh8BUMY9Nm6MhzS35QAdtA1qizkBefkdU-E6FADbTBhDWIKbq-j4FnKI-hY1QXbp_Pnmzb4bRE-BGQ2ZrLNqSVNqYgl13ghhMj4vP5nZQh84xz4LmAVOfVi9S2q7VNKcXSgjUzRHlNCmAvlgW-o_Kq5H_0WnQoyunV73wKM5lX8JMG1uJxMtVtQVlcOrglXQM4b-ZxMWgo6Nrcw9mZQqLoChbmjxzXY1-_P6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB-akIyuqV7LpON6cgipLFvlnX1-r-y3ibjlWqClgDTUvC8BoEFHUkwn5N2w1j_EARV6kUoWl_qxIAGQ21iQHNcwyAGarUVad-HypnBLy6WVIiCtKJdVAUx7ibBNIZfSereZ9yWqi74pOqTjvjpcEkCd0JYJ5LlZ5Sa6kkVndWf964ZsjUB7uRM5hFJNSsh9PGHrnrGN-_RckR3pd5H5O0mLAU-pQ5ERVI7Z3wLU_fRWmYDHd-CbIueTfmalvg0TZGCfUV0T5s0YQdFFDCMB_RveEeG6B5j7s7pWtXydJhZmza9cDQYqGxLrExGcEDT01umGvAeBmrWsrI-smVMUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=F02ElhdNkgUQljBbaA0yQwKxy5vnlFxT92GwELGJsd__-BsvLX0OOOmQTI_lhhVoXqA7ndb-DtVm4PSLUWkaCKdWKm_JvHq_I0dDc3El5RmSTOYn0nZcMjTQ8wHA2LHI7cEW9bNIslhUq8jAxxBRKqUnROxSb2RWvvgAxkMP4kpUVY1ycQMHkno-t4JjYsQSQ6dz8bPLIf3loqNdgFM6zsKZ9-BXeHVNOW7BP5tPYEq1oMCtJKm787cV4wjk37uin4gXi4X8P9h65joAkec_dfcoXy6QB_yHn1Ep845pWuTgtD3pf0gekzhLOgknAE_xqR3CZLawPAqgbxej9U_2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=F02ElhdNkgUQljBbaA0yQwKxy5vnlFxT92GwELGJsd__-BsvLX0OOOmQTI_lhhVoXqA7ndb-DtVm4PSLUWkaCKdWKm_JvHq_I0dDc3El5RmSTOYn0nZcMjTQ8wHA2LHI7cEW9bNIslhUq8jAxxBRKqUnROxSb2RWvvgAxkMP4kpUVY1ycQMHkno-t4JjYsQSQ6dz8bPLIf3loqNdgFM6zsKZ9-BXeHVNOW7BP5tPYEq1oMCtJKm787cV4wjk37uin4gXi4X8P9h65joAkec_dfcoXy6QB_yHn1Ep845pWuTgtD3pf0gekzhLOgknAE_xqR3CZLawPAqgbxej9U_2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTVsLdnZu_z3XuO8RbhUaLwWPygws_bLp6UE5vTewAEdet1xbCyc6AfQvTSIvxu7MrpQ1KsLY4pO82m_UfZOL65em1_kV4mGMEozi-QrYqNhkmW-g_AEJtUQkibun5XatMe3pW4oZuPtDp_0P_4uJE-pvVoIMMnjdar9jsWkQ2Fs56Qmt7arDa2NWtoxw-VXxvU1dl8_fxJEEyjzTpPCBWPihuZRP0jZ0mnOjRxD9pVDcnU4h5YHmVg6LSghwVYZ7s3CCu5gVhg2ZRFb8krEdVFRzDZTtGmaZWS9B3Jvkx-Dm7jcy8ixeb1fEvv37xST1yHPvcoI43Zycw5Ym1IQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw-gQzDellV99Z2oML1iasawoiqTmBhjB4GtomxvwQWqfFbx6SSNSS2o1tkXN4bZXoJpI0b8_qTvE4RpCeJOqcl6mRLxKRN7YB9YzQMI7KDUGDCJ50dpJnwTC8G7aRclGA_ngZ9SZfWAacB8jh4DBBIc1QHB55CDDzd1fcK7WgsVofgYBmUcOFS83rSapoIlJ3So-ATbPAk_hCD6EgLxW_o0XurIhz1I-ffIYJmD023hTg2OuJIUF9qJppZfxE-lFkn_bUB7fkdqilgVNaidO47Yr_bXjrTPYXi_XjLqVNzU1RsBvxq-033q4RJw-zu05Uw8Z6YBHeIib-e8vTfB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=lPsGE3GR1URjt6AH3PeI-xwZTga1YdJOhAROwPquhXwet3il5rhQso2y1aAJ8AXaEnfQvidpYEKYRJ7WjqYWho0o8mIVUHXRCqqbpCdweTse6fZXhJIUy8afozAoyOowLqkUvHpH4OJWk-9SA_-BLOr1sNHllezEjy4r40tXaSpWYNPFVskc39TpMOO1WBFzk25IZ4Ni63LLKGcyM_9uKSTYoUHWM_84t9rosXPVQolZ3CkY0EAc4K0sH0IiDA24PJaBGUVpKeuHJmg5QytEmGtg-nm-jEu2Ywc3bllV5l0MC54wbtrBm8GsrJQOes876git4rlAl7hUyx_YDQP_nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=lPsGE3GR1URjt6AH3PeI-xwZTga1YdJOhAROwPquhXwet3il5rhQso2y1aAJ8AXaEnfQvidpYEKYRJ7WjqYWho0o8mIVUHXRCqqbpCdweTse6fZXhJIUy8afozAoyOowLqkUvHpH4OJWk-9SA_-BLOr1sNHllezEjy4r40tXaSpWYNPFVskc39TpMOO1WBFzk25IZ4Ni63LLKGcyM_9uKSTYoUHWM_84t9rosXPVQolZ3CkY0EAc4K0sH0IiDA24PJaBGUVpKeuHJmg5QytEmGtg-nm-jEu2Ywc3bllV5l0MC54wbtrBm8GsrJQOes876git4rlAl7hUyx_YDQP_nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H220WF4pf65vRqd-fdYvQYp1sBM-Uheb-xcM18i5WVLz-it6OQw-x73oE8Qpm6PlI9yNIYrKalCeUZIt_lnheBqnkaSguhCAgPi_dBzN2fzLpjP9JgskhqNwsyDaS7qM4Bg06mp_WzghYO9F1gFFfW9ACgARxcZN3AbB3GWWsbQsntRbXBs05f6x-WRExvf6H-aBbgd3GIkMKJE86UCNa1sYXG6KmYkbp7oAkF3ykv3LaJqYswwoqukkgDSMrMR3nUmGpRaHdmnu0ZFUfLVijl-kt0wS4A4ISOSt_YFQRxXcbF_oxf3GXd8KbAfH2KEBwEwXyangHxizaNuR2W7ItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ljpQmG0PmcjJg1EWUUFdTEyhBsz-tJ7Irwy1veeNWcwyOgQb_wgqc3pNRmhgYwH6uyLHnu8kGU7pFvjN9X-oMhWHgTJtkt0MPyjUgT1FaP4_4Z_JEqEc-VQS0JQ0r4nr0znnRG4uAiLhfjcPB7aI6wKbSAzRDXnubOZGCzugydzHZeCViVJgYFvK1iQ9bpjc6SPRkHya2kS0QCvsj5nxcQYoFs-Bnaa2CL_rEuxLWe4B3wxMAhNbNOh1ZI6MnGPO-a6ZnRp3xIN4QSGHBH4hqFcmJaREwQVM-hTWXB5ASDn0GjIAKAPeikyAIulOyB97DyibaSJCKbXB9IMnY_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=Tn9lUY8pc2UJXVeAmKZO2b6eufJCaGt7sctFUInObU_ANNeFc02UiHFJ1Hm1fJbaqA9sTalRrLwlSqNs2PbDQudlpsRIwn2O-k91Jl2VGkXkZ2slMtSgeYccTR3xAiMfwbOPCjHlej8HZ3zhieqzZvvQ5AAXSSy59uXLw79hMVSfpkDCUCgMwiDNo6wUnPk58UH7Eu47rHUXjGc4JU_EofA2zOlCNqPwhvSVQTWoKgitOLmEAL0j36NdJBDppThP7TXQcodm86Ryozk-BuuhFqdVQO3D4lvDN4PBpsvD7yEEzGSckf8ukem9heucbrczul9Rd63f4Sb05WPUtG-or2SV4y-cOeTUDbHDIwIdfE7hGIUxRTsdsDxFs9c0UB4Flnx1xySfZV-4Rm13XTTP-jU56fV10m1NmCdpJJ2mBBYEjqb3KytbOSSFMhwIbLLrusABdFFMKWpbP0Xa-2OR5I_YcpvxKUG8ZD3zJsRsMJy6g0fEtjku_BCE2k3ERCO4DPFTopp9aLoRhmr3NNjRgLqohIEqdY2jdKd8YB6VMR1UUZegBV2xec9FsCj_eslXU3Zz_GIbKLPtN06SPLCXtWyCVqEAyEkMj6yYP-wpAYRchjT4cVV6x74hOk8q7kM9x867d6aWx9ceqXdn30U5_Qr4ahi3FbRb3Zs51K4bFuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=Tn9lUY8pc2UJXVeAmKZO2b6eufJCaGt7sctFUInObU_ANNeFc02UiHFJ1Hm1fJbaqA9sTalRrLwlSqNs2PbDQudlpsRIwn2O-k91Jl2VGkXkZ2slMtSgeYccTR3xAiMfwbOPCjHlej8HZ3zhieqzZvvQ5AAXSSy59uXLw79hMVSfpkDCUCgMwiDNo6wUnPk58UH7Eu47rHUXjGc4JU_EofA2zOlCNqPwhvSVQTWoKgitOLmEAL0j36NdJBDppThP7TXQcodm86Ryozk-BuuhFqdVQO3D4lvDN4PBpsvD7yEEzGSckf8ukem9heucbrczul9Rd63f4Sb05WPUtG-or2SV4y-cOeTUDbHDIwIdfE7hGIUxRTsdsDxFs9c0UB4Flnx1xySfZV-4Rm13XTTP-jU56fV10m1NmCdpJJ2mBBYEjqb3KytbOSSFMhwIbLLrusABdFFMKWpbP0Xa-2OR5I_YcpvxKUG8ZD3zJsRsMJy6g0fEtjku_BCE2k3ERCO4DPFTopp9aLoRhmr3NNjRgLqohIEqdY2jdKd8YB6VMR1UUZegBV2xec9FsCj_eslXU3Zz_GIbKLPtN06SPLCXtWyCVqEAyEkMj6yYP-wpAYRchjT4cVV6x74hOk8q7kM9x867d6aWx9ceqXdn30U5_Qr4ahi3FbRb3Zs51K4bFuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3DohfwV6KImW-oAubsKmrAu7ThqQoXGhj4yYx8oGX9rvRQ50TlYo3f_pwhY5MK8h2DEpVrKURo3WaJSaLN_Pr2tZSTTSXUZhCJ-K4ToHd9hQ-EJyTFqEk91I6WB0hLbePjhrl0hfHk0jx4jtHGbbgxfrej30lTK7AhuDugQv7UwhnDQX2EQqIGThSCXPvJucEURuvZrbMkGBfh46ARGz9MvmwK1SjUooS9gUPtsaTSQXPFwqPHgO098MSf09R2TGFLgyPKI8iJUfZmWeW7mGEZd5McpaTQ2_z0k8w4neZD9_1Dp5rZUfhF28je0MVy-ss7G_GI_5aREmrsNhMpKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=PxFL0jUnRp8-f5rnLKxNRwbnF14pHacDmkBz7Y2myKrxMR3vrl6ao2vbn8392Y_TtmPcLBenHJV_x21OYRKm7KZuIrKi5auHyMI5viplSUQLEi3j3fehtOcaoJpr1Xi2uWhnlTtUc-TzGAXPA465Qqq1q2R9TPOBJ2N3KG58XsMngrP5C_ICIeAK2fqCaM_h2p1szmBIumk72QqDJANwqiZ7veEPQoA66so6qGt0gw7iV76Zfnw728a84070qkF4yqJ_W66q-PB6ciMJjZyDdN34sk3gq0DPL3tTs429V-Rwk_j-JM1Wl1YtYMlfG_D8puhfESEJFs2bhbFKZQSt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=PxFL0jUnRp8-f5rnLKxNRwbnF14pHacDmkBz7Y2myKrxMR3vrl6ao2vbn8392Y_TtmPcLBenHJV_x21OYRKm7KZuIrKi5auHyMI5viplSUQLEi3j3fehtOcaoJpr1Xi2uWhnlTtUc-TzGAXPA465Qqq1q2R9TPOBJ2N3KG58XsMngrP5C_ICIeAK2fqCaM_h2p1szmBIumk72QqDJANwqiZ7veEPQoA66so6qGt0gw7iV76Zfnw728a84070qkF4yqJ_W66q-PB6ciMJjZyDdN34sk3gq0DPL3tTs429V-Rwk_j-JM1Wl1YtYMlfG_D8puhfESEJFs2bhbFKZQSt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egHM9oHDfXCxzl-qTkSLINAn9q7iUNPdLGc155gL1-oQSZQI5rjJN7DD-vZ51mZd03rgukeD6LBDs-LGBwsATaCE1jkdwQA06EUhhoSdyCtTQtLHbC2EtcfQjhDp0oshYJm6esFuq3v9x74lE7qAJGz3kLD23uJE73rF8UwurCrGNTPvwdcvJy6XAPKSZmLn438AkcnoSo8fxAlOvzY2NveTzwxc3fuyFuj2iAcIqpLmKH2DKdMi1B74oDjy0q9utU_Xy5AXVz7YZx279crDuxFaWNVQP_lzBMpRyE4qn0vzvGW4zRnAV-S7OYCUSlKQSaoOcVBlNpDJDJwfin8Pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQh_nLzumRkPc4bKW4JlJ2CRukaIjUCgT2Itcmt_V5KDuU9sXxHiejRk4bYiIARFhSKM5egPNx8gLTEJ9HiCbtBM2qeFuibuogPw7EqFdvDj46m_x5UXh_llhBxtmQhMXXxhat-CQHO2grtU_TCKKMQ7njWFp_tfg1wzNMo64EAeYGkXbmHKRgxC0WfEUTpMfs_hH-0wYoVqknCHOgQ0HH5OacrGiuasPn6TtNGon5A-kVnN22tv-cvgW8XlBWsrpKBwV-IopmBMWAIFtWodGY6tlpRKCpDZTWnLOkopODCWzLOZPLZScQ-xu9vNfjVnmywc0v6YiHGTKuV79UKsew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPV8SjeKn5pJeEj-LMscnkwaaH7QQWB8ehnuQHdPDILQs9zhWWWFDzz5voLuE3JIN1I2R6W5AnLBeBo1NFQxQqSDbZ5NM2_fT43sH41J4vmwLqL0XFnDnqc4IvPagv2bIFqqqKnTBd5ZrPya3L3cO7L06mpQM811R9FmoLuVhB6VjR0C3ICZ9ecgITpXCrM6_5LoALE29HVyYGiySg3Vu3LD5Jq6n3LsewKeTAsb9uawY8FtdEBctTb5lbj20o1DRwPMRSuSNZ1mrApDf-Qd7_4rYC1EG3s8RAiIvPAIwMAk6hNnV2_CVmJwbfIeVbXEOFOFif32REl_BwHrv-Sxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pteXvijvTr2e2RWnBSWwdAONrqldXC7x363_Za1e0F7vYiEXkXTUh2K_c4ToLolGcUplSmqE3oCH6sVXnzCfSqRz3QveyzDpMRO8HR3WU3B37GlBxxNTSEXluNxQkfhpDa3eivCrxGSPE2BnmCwYebKKaa3IbYbYOmVLNatkg6hfERUHaMUvMfflsuWKlA0wyORhDkbdkdftc6xNQ0vtgwP1Ez4IEDjhVi1L7H2LCrEFPLQU3H_BmLVgaoBsCraTwfqtN0lmgR6EnFyuzLoW6zZvalJJ3rkR-5xHuHwCU7EcRjDD08Dy0OLaz14pUbZt51s0JXdM6pV5cMVWdOvRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=I9UvHh7IGUf43T6Ru1zBWrp7-0PRFHLY6VlMZNu-whE2mRmy-M8vRNEd_ZFAR0sgJw68y-ksnbNJwZnhRJNgh5oGddecxODWI3oSUrmoJYWl9h9Gl_F0gWlZBXcHqpNQnMWaQ_FG5QgU17eYEA-Rb3wiPf6VV5isW_Md3131qG5jc24orTaXa6_kjhJzwNnYT6rsOjYp_iQnoyXNbxRR33flAfvt4VmQmxE9ZpeEVoE_0-RZX-ViS_1MIqso8u4yr25fyNRwHb1bXOa32d2Yoker7_tGrp4z4RrKTODVERiDHiKmSw8jC_NsHFh1COEsjD8nxX9b8rzlo0CYEeitEUJ3Kb-eY0ZqbMdnFOrLrdOcaANRMtJ-sKCQVFKBJqzla5IwlIlMSv-O7El7ZHIzEE0YwjcPTna3h0ldwzfKyf5bqdFUmnIIbYK5Id-dcIYYO6VI69yhTITWpq9F8Cs4gkuWc7GUgTEbphhtkkpof15ATVTLZkG2eUjOWWXo3cab3_UNJLWC8KXwp8xsFpgwLcQ1xYdyHHuZg9cwTCoSRf1qvt-Wc1vJG9ql0M8qHBensbhVIsPQJAX5-n0pCl0w4nVRR6dZKFERhaw1LyQFSAi2qvXYb7vgeb09nGGaR8oMIkJDahIl2vn9XBxrDK_hwSK2fQX5ws5dj0Aj0eWYxag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=I9UvHh7IGUf43T6Ru1zBWrp7-0PRFHLY6VlMZNu-whE2mRmy-M8vRNEd_ZFAR0sgJw68y-ksnbNJwZnhRJNgh5oGddecxODWI3oSUrmoJYWl9h9Gl_F0gWlZBXcHqpNQnMWaQ_FG5QgU17eYEA-Rb3wiPf6VV5isW_Md3131qG5jc24orTaXa6_kjhJzwNnYT6rsOjYp_iQnoyXNbxRR33flAfvt4VmQmxE9ZpeEVoE_0-RZX-ViS_1MIqso8u4yr25fyNRwHb1bXOa32d2Yoker7_tGrp4z4RrKTODVERiDHiKmSw8jC_NsHFh1COEsjD8nxX9b8rzlo0CYEeitEUJ3Kb-eY0ZqbMdnFOrLrdOcaANRMtJ-sKCQVFKBJqzla5IwlIlMSv-O7El7ZHIzEE0YwjcPTna3h0ldwzfKyf5bqdFUmnIIbYK5Id-dcIYYO6VI69yhTITWpq9F8Cs4gkuWc7GUgTEbphhtkkpof15ATVTLZkG2eUjOWWXo3cab3_UNJLWC8KXwp8xsFpgwLcQ1xYdyHHuZg9cwTCoSRf1qvt-Wc1vJG9ql0M8qHBensbhVIsPQJAX5-n0pCl0w4nVRR6dZKFERhaw1LyQFSAi2qvXYb7vgeb09nGGaR8oMIkJDahIl2vn9XBxrDK_hwSK2fQX5ws5dj0Aj0eWYxag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQf1hs923peoVkdd-0LUs5FBHXERxI2N4MUYKmBFkdHg0KoVzWwo5NoXjike2NX_Y6nJUCUHyL_ik_vq23etrcl_e6miHqY3KerYhnhj6GT6PRTMM2jEJVXtmgOaqCHT2mfvFj1z8gVIt9I7nMrru8ZovZQQzQ22bi8Id_hT7tyBpUGXTsS-qAk4YxifULuBvgJmd0XDBAg1fAZ6svGSw9Upfh1-4vfA5WKFnysCF-zuT393OhdUMatCadbgkEwN8ZIbn9MvfntqXigAo6sKI6qBiFHqogPbhAnfHvlZYEAdKRoSR-jq-DhHWn2k8ilAZFyN1OyCttYI4JDRDMo-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru16hKJGQJwdz1hQ8uoKmTbXxmhNAdaNXmtcHnMZcxqy5_TR9UXKfIMqNCku6vKUkL_vuecE8e2axLj71Vq2bZodsDZ5Ba0lsrc2lqhJdvg94RBMFmvD0gHXzbK7iRPzJiulg4iPKMThB1fZtjnFkWp6gbf6zrtqEmU7FDCXI_UdkuNyUpWtTzDtWsBRI-aVvsvL-NfwgVUjT5sOpo_ljZAm_MkQz4pMlC0TD28vEo1tdXMvUojx9vz9OZOZy8BC_huSLpqKfu2RnTjww7OWB4Rk6Eqa2TyLLoMMg79-owr8pv_I7su3HY9FXMvVm6fKtKlm6POv_egVGGeRmlWK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Moed3DwzHXQeIZ5PCg3ZPmH5q3ICq2aQK9psdVXYYSoadm0lYjYko7_PefEe0mEVO9QcBQxgVG7BuiCOVslgNxnB2vrD92puTN4sdrnlFNlTH0oJfhNItQT6fwFDvTktLt18a8DZqVsL98Qp0L0wZxoL9uApq6hOPMFW-yJXckOfxv7gweaF_XTNHCxF3wlAVciDeAYs5r_3XxzBT4GuWbb69XjIJasIoIoCsV1o2-YWJJrmfgjkrzoEk8mjhSGT0Koj8M0TjIsiUpYQGj91hjTDWfXfBrr402OPE7kYVlkSO6ENquyKbIUXXLTX-vtoKrYjE4yOEZwLUUn9LNznZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=sPmbhNabvubHSEJpuqCZu7n7uUm5t3smISuVO7HKjjy7xP8-LwZX03gCxuAWM1CFtdCt0dS0aC4XivnniLPl0cfN-OcmZ_e8hhmdr--q283RUXwufX2ySZru95YlfMh522_tnWwm-Tzd0pLfWSLYJ3U_QHRz-LBdDRAUsWkl1mKvszr9MsQ-sRrWONikIO1z-aPnc9OA9OkaakZ7ReSLyq4EhJVFKuU2MR8VCSlSdVDjOMIJORF_JLF2IIS9uOpIRsTGVoQA4Hq2NtQnRSB9CC--18OHaXSSlOPS1Sff02YMEaiKSxXlfoC2smtseyoDMkeOLdUdb9JPt0JO6o1-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=sPmbhNabvubHSEJpuqCZu7n7uUm5t3smISuVO7HKjjy7xP8-LwZX03gCxuAWM1CFtdCt0dS0aC4XivnniLPl0cfN-OcmZ_e8hhmdr--q283RUXwufX2ySZru95YlfMh522_tnWwm-Tzd0pLfWSLYJ3U_QHRz-LBdDRAUsWkl1mKvszr9MsQ-sRrWONikIO1z-aPnc9OA9OkaakZ7ReSLyq4EhJVFKuU2MR8VCSlSdVDjOMIJORF_JLF2IIS9uOpIRsTGVoQA4Hq2NtQnRSB9CC--18OHaXSSlOPS1Sff02YMEaiKSxXlfoC2smtseyoDMkeOLdUdb9JPt0JO6o1-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2PrSFhdz0vXtWvue8Nat6NC23iy4J49wzxGW4P49GSyacMv_GbowtWciXn3lhOyBEdTdRrxsqDH9nB0Zz2_bhAH-z7In-fIHSQ-uGci0xYawsqOyBK-kPRrRYx4jbIo8Hj1xebaJJl9l1uIYgRX-6rufBh1qnw0o7QAf24vrCX4Syo4O0rC3lUHW3NtJf-x3eHDl7uTJPrZBd6OwVyXkLHqXWmQ_pvgTSErVb53rCiXbSRJdkgaHKzmJfMeYXTmUHEIsZqFU51RMVOMqmMY4IiX9rlgHwCdsi_JTAYdtbXm-DGYf2_IKSU-mkGlAbyNfFlRzq2v1Y_tfHFXNKZ45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEMVFKCF2YvjfxMXurjrBf2rKeOmNkwkl9IXkyx2dclBSlgbwkKBxdwK3DlAOC1dkrGJpF2GraPITxh4cZtMiCroDjwcd4fvagzs3aULWVhGTKpYrLZUHRHIxHxqFYFvyfBOP-5ZTY0GMW79KnPEOKVFNfI79DQKb99Uy5oGBqFVhDEzUg6hofX0dXrweRjmqMjwcQUdksOCw_mjVkBX0caLhejxkeud1lpmanJAUwdNT25jNCyUccVgBAG20vtTCQiKPkWB4nXCbZVUmFDa2kNHfVS0RZSxLi6-GjpN4qH_s-3r-IBCQqUoCpqqj9dB1kfpqx-SAwVbUQZwXhAAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hrBJCY_HMPQ2oh9yGbGHsz4aA9MAiDm5i5gRFjW-lEuoIGrJ2y5KqP6GXedALRrPHVPlcZgZNITvgf3EH9ba6K_PtCrsd26tClsbv7ftqNm7XXvFzgVNpkyEYELhjsn7Cz9zdPd5e23TSfd6Nyrd54KAXLKbbWJFb9n1eIbDKloRc6fU-rXaxJ1Zwp-ZETYNQOcXaXim6ZhCDCtbPNBbXK1nBr6k5ljJcaEkZl-wSF9QVzM2NR32wuxN0g4p1vxgFUZI5zfXijjKJKD5VcUHam6E5TbG-oL8UudRElw64GdsyKaeCibrBaK1Wl3ClH4MuDYFRqiNZUXwEKAdLLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXhY1jXvZjFkjXer8MMMSoQbOX-GAMvK8F-f9m0IrvsZ2cvk7E19SpNLZdaHcxcuepp1ct_yGZulXHZ2uPEhoo-szxM3wzmLgP334FcCikKMIb-3otja2ifh8IphWQXwiIU0hvLlmh-9je31Gx4KYH5U-rfS4O4vOptHz4O2yFfrxfZaHJu7fAxgiqqBGoYuMM951AVQu6oGdcv9kOo0hxAsXB98gmdULsKqA3VsXxUuIucqhcXw7puwy-axLE6rTmUIXt1ThI-u3Mj4SQqIo_iK8yOpQPd267EKOGlCiIhDDb4OGlRZzmfiIJhZhomAJ4Y81uAJDz1yWvvDXqNRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFxQczDZ2EymRgbwJhxx-vZZWJYRCScbXLsAkq44HqsBmtYLKZTj-iEmphUSGE_0wBdzJCbAFTgZCI2_Tu715BNgBMjEWDiUJqmic4DhlyGlc90SpGWmoudxdb7Led9zPbmF268FmcAw2CgbVfKVa3LMvawccOlJbTONCSNRH7d3wkm-IDx2KJ1fHFZV9ueKmRwQKCgXXzutnbXxiSbIercEYh56ctUp7hi5d7qGc9lcyBdik-SalF_VJjOrDwKle-n-32Kd9-3nbhFvP5t4vHJk-e7FE6FWO4Ip9OQ4hCzHogDmWHEYv7wIRSD80sEU6AIjjMdJG7mAK5bVj9vv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAUZahybTsmqiFQGlsrmfBXZX05ZApRbWqlvD60M-zZwgePkmznx4ikJ4j6m_ibUMXwA5srRBbgfDC9jZFCO35WMpTPHHfvBTIKtgHZgF0eMqnBKDmTw6WPd9pFwo0AY_RUN4HoxCZBLben5bCw_kgS7WmiDLQvnwc6hB5EwcSP34q-ZpK9TtptL4h9C4Ce6VePjKwPy88brJ61ObrSsktDYHtO8ZWDFYXnDJeSqHxLA35yQQgF13A3fEet4oTQpHgjLle8sVgYg0Sk_yhYtVIRFie4ASbwwwDgrHT6SwKBeMffEGRYTaOqvTNiGbQJpsxajDS6PhSGz7A8HNtG6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOvOHobMkVbGUy01S7pQZsOYYR5cOmz5DXAA7KXJbPHLEjUPqFhK6lHxP3wKWAvLSFfTxtfgryJEolPZxY4_cXEAPr6NDWgnuKXWuxPAweH5p-8dekhtwzC3QCloIoFJF7c0MwwGLLTK9sWT17qGfk_eCJCxQYn-JifZaZQreDzWl08Q8FNBJs360wdQHBmBBLEil7z5kJDYPM7baEo68ucfvpa5mNo4klh8GfgnJPYG2t3mA7yoeXdOUHB1nRCYw7O8hpV1e3D2v2CgM55y4ChfVGo36Ln6qJUJcBjqA-MSe1DII3cmAI895q56JYWXQ1XnR9sNwwmEBiy0TcLJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGW6R3IQAf1D-E4AIEuhcUQ2_ALa9-1NM21aBy-2DZsJj2Xb_IMdZO2HpdTovFA9Q-XpwzypJIkqOkVGjOIaTH9YHDfetyaX8j3OS1ZgqHS-SEtw7RAN0AY1LR2nOzcTpiRTeL9hPJJfzBAgfeL_XQXqubYYSMgxfqrMEcbOdB4TJE8zn1Wr_nvjOLw7pC00oDhwYVVCz2wX9Q_g7khjk-XihELvamkgHVLiya4TH91QTqIKug56JExsx4pGJWLXaDcqTPo0i9eTqonOMFJWiqMfKAUjPCfdeu4PctkJjXhDtAJ9risz6T-mOLXuJ7ylKSJ3Nh3tNcNjEYL5g_2ttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvIhShhEO3FfPNG48tXT5cMeenVtDy6-Oh48_OXoj7-YTkrM4rXxL6eM29IfJlo6b0zVfEdnej2asR8xnpDI-uwREWnIGUw3ek_-27Ei-K3KP4rvQ4z7kr6Zyx4pJts9R5sYitbFJHewJzUQ5zpirRvwWN0TSxgZiVT7hyACees1wcIu7x9gLWNSH3MVwKz4CEAVCVw8kXstHPxexQ-adcEErTG0u5ulCSJExs5AjTaBrYv59dLe7eYth0ghcBMqvcUtFaLnDdp9YB1GfMj-51sTVI7WlwqJNmzvI20MPfCfGq5PZaGkEDYs1rP1CHHvU6Kabve4wHs56l7pERjhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpVudZ11FTr7hwRkMGAfwZffJopny9RBkruAufNo_HMIPo9RspciylaAqDaB6PZmTm5fObKy1ncPR3HH2NKtsucy2mwbQsRSTdtjyCIRFDANbhLrA5gbnuxb-lG_r3luCMciQbmivZi4x8SkzD1Cms7gCHUKaKIYWw_kpdYClhVqcBZNOOxCH-7nGv6DfchrmyCpLHDzByOBGMxMwqO_FpG8kDNaVlX14tP8fK5IC_YQbEuysCjUM9LArsDPpyctshvXkokTXrAgGrtgl9JvZsc71CdGuN7t_h9e9EbIZ5n34XovJGuuxZgd-4F7RSR9qzeDjpuZ_1pzPiGcv4lWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLRaN36on7FgAxHxLzH3Z7X9XhdUOU1YiQtGXt1_C58aGYsv7LWdZgDvtUCcYArrTTpu4fkgIh59n7fDGPyLisQe1A1gtULnQoQTsuYc6mYMsHCuaEBwa3oeDDYosd2xsbcYOTZfh1Ov0bZBBYZYFz9_-T0bemlVpXay7vNgQY_ZpEt41yWSBgMRFUS2TJTgbUx7W8UXPHwB3C1SwHZC3TRXKYpCiLgZipjzgvY2YwpOgF8TYSOnulQqIpRi84BZyx6ikRnl2syYRr7zFN2s5vUlglwfp6dAP6A02RC9Wv_miHxYuagiCdap97CrAi4PQrYXH6EnKOodUNBa_ijsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YK2MO5VwarB6m-D0NGgkZQ0Cw6q0vrbylnLN7Ok9j2B4N6frHTkYmrko2R9T6Vgj01CnEixCg0uYeDdPGUDkmpOFjUGhcEZYm1o8iw7BVfFuPBEAw8aZAWCX7flOBnCPPbK1gTlpDuxzGyD5Rxud-QfMb0U4g-IPgnC64rlNLUg3bzPbxy7kLJG8bF9IBIM8pJFLKeRFBbUuYqB4YYHmk5S_bxVyAsFHBiDXTmH7blc9XSOO9wwNXSDDSJMNGsp3Towfq_JU8Z4uzJiY1anPkL6W0zM4ih2ODe10JdFLqpmubsreSNkWCbpD4WmNmlnmOArPLbC4ko7bg-xBLFs7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLV9sXSMLwL2tEJtH8VGs2_zrmF_REgWQo0cIZkiErGUNYaGmDB4VJr-Vm1kCRYrmeyPVmn4MNQBPh67muZqNii7inMJr_Fs0NVchf-pb49yiklhHFSKRfdhklE3MJGTGr7lCsL2Xru1dE_BeTTodfUq_iMSQJ2fgssTIXvbVp6FMaL3T3eusgXKMt5lGBq2JDPNzHSwt7RKaU9aQr35mKUMx9lIco8GD3DqnGf6Ju44LwlyKF5z0_H77EfbetG2SsdT72Dv1kadjDE0gOEd_XJWzKX8qEged6t6dKQx81trv0GFk33ickxedvOGIK4FSJhjjoNUhmGv6XO2juUOhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSz26Y5y5Cx3JuWwjrFpI2HQxFXXKlIJoq2YE0kn9Nhu22qbjorhKGf5U7zxFXJoSGdM8R_qWOjX2GdvZ21husZLm0FyYq3WXRMsyKxzeG6BgkIPqa7t4XaC9qcrTgGBVizgjnh0634ms81Ps9P-n9nMSMC7ul8hcGCkqwrpDf6LJQBVQmQe2BQA_WhOoLK3glSGLBkd2dlz8YaZRc1mZJJHLeR88m-mXnerVmcfIRqcoRAlLJAqmGd85yMor0ai1Lf0NRaUf5KehuTY4X2VcCX-NrwCXmzgWRHNGAv5fwT4WhS2bzcAYB5nLe2NK2fhdTOb88x5X1s0tfNQ8oPI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgSsLJV2-wj2x2A8MK_arGKW4UxtMHbok6fc20jO4MDgFKzTmIAvuvqbTtTB4hcHPGxIwAYgpzzzNhL1vuGKOxEkBsbIJasPXcN1Yop1DEk_FnFaCPYAO4COQSAYwhAt5FFRCutHJi4IphUm2hGyGWA6K7-o-n-2_PTOMtPWaFOj_zcztw6b41PJQffzGAzDadLudmvrF3K61w_SgdhCOojzwRFcNRFQoIj48-BvyfUZXNe5EdHr6ru89DEakHD7pIK8i29LUwq7C1sctv72nsYS-iYyzaeKYMbsqd0gNh3zV5PC5scGblRMa5UE5wi2NeLXbX1BDOfuU1AH91ALRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOZApKMnvWFhJgMJiiC2Wrng4mwrgAzvLBpA4bL57eFgtaT48FnMxExosePWj2csrcEKcviV_O86deA782NAmwMto-XXk7-Gfy641TXKS3F8YokHvCWefg-nSuGuTAXW4Wvxme-oJ56FnUhqYQ63p6KVIpENtFNvFfdEwqj1ANws65Wg8Np_1l_B7xT8rk40jZ_CrTHSnEer2C2q5rDVdv9EEE2nvqD_3PLngUkd306Tk9Mwvs3v5eIzk3aRPAC-TNP7d0P-SDVua89LAksR1x9VMUyPDs9axYmx198dcWZaowws4nLxIeyE3nRSDoHweICPtZc2SPbfCjIi0zsKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=gif_dzuHbxpUR1BoRNfJymBAaaLs4v81QrZWGIJV68MOa-6G1xSWGRBzEimhLU9iI9sJ_zCw-8TSP1Izy5veKNPJuqgol4g3XCH9LCv-d7-6Bs6sm79eEahYh7aVTblW2BJPWEox9cPajNqVlcP5XPSZ9yWr4iT34Cg5oe0f_uZvfJdV_dKyDQJsJTruUg-SO73GK49SY2b0vZAMz-3Flc-K-6txslAIDZUCfWGKrgYHDyCZDqpQ1wJwZf8tXxyL8pIxLvY3OfJyzVJUuAMW59-PFwfhLJi25d1afZfgEK4Lh-wksqM7nWAijcX51Qvs_hdKqjhAjXQR-s8NHnhclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=gif_dzuHbxpUR1BoRNfJymBAaaLs4v81QrZWGIJV68MOa-6G1xSWGRBzEimhLU9iI9sJ_zCw-8TSP1Izy5veKNPJuqgol4g3XCH9LCv-d7-6Bs6sm79eEahYh7aVTblW2BJPWEox9cPajNqVlcP5XPSZ9yWr4iT34Cg5oe0f_uZvfJdV_dKyDQJsJTruUg-SO73GK49SY2b0vZAMz-3Flc-K-6txslAIDZUCfWGKrgYHDyCZDqpQ1wJwZf8tXxyL8pIxLvY3OfJyzVJUuAMW59-PFwfhLJi25d1afZfgEK4Lh-wksqM7nWAijcX51Qvs_hdKqjhAjXQR-s8NHnhclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXXooD2auGDsGnyt7p1aeSh_HXkZpVj_SIwdszMIEK0A_EwQ9gnb9jzgS_DHogQaV9ysJmuGO-osxt8-wOApvK92LO-na4QPm-vAdHSe0vCroRLZ9D0HUpEKUImbZPR1Ll_4cRjXiIeN04oykIX0xrSwV_b-AVCde9af-SxJBTWhCtKCDrhni6-qP-8xsaxbuvF27MjLTUf_SmQ1vACqe7vK2B5SQmOw4t0dFfcQD3O31Ccj9k-fmgt_cmzJobed_Ab6LxSvNoDBvMBUoz7YcQoC3M_27G2CfiLfDiZnNCXPV54yI148BiAIISZn-5tEPKlNrkFh1yq0dioqCKUT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA5WifPrZafT0vSTLExMlwxd8BFSVki7asybvwDHE0f7oAoQ8KFvHkJ_mS5FpooIy9rA_frFYiME8w9gOuNWSRMhjOpzxxDxhiaGSpBXzIe93DZuwrjMSH318R7kExZSpXWLyedos9J-I11CCwtksOtdfZqlwPX03bTlJz7u0w9q8w6j6ZZT2kAdLvgz7J2NKxssOyUMfAXaG_60_391wPYdNfrQ8QRsAH2wGHD2SrQPizKELKI4KC27tJ1Bj2iP1ETYPTVYU1T__4FBk-AqUfD8X6UXf_gezYx7CAlAoTdeD3IgPEHbDTpi6QKqlyrlrxPd5IKRkntSrI6AU6Unrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Mi6ZmzcQWPRa0vVxkU2oPvSuk3qWsyi3GDVrdUPwck55XX4mOOdLOSwpuqkEPb9WzV6YGQ_3rCVQejRkXzZF7YRFPLk04TGXaESz1z1sqpbUa32fLANCIqj4G3OAR-BhYmznxULQefItR4h3q2ajP02is-jHygJGlgbIYTDvdpp3oxOhaxYr0FX1Q9ouXu8N8Gl4-lz8Ek1japIwYINHE8ciRGTtEc9lbEFNS_V5tDcruKDVRqgr3eGlwC3RQ_aCFjru3of9vKIVWWsh6F928in9HgF6ARq96Dd1PTWhFZgVK2zM5sVB3ARTjCWhpu0wSeziQ475FKwja8X0t6nHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Mi6ZmzcQWPRa0vVxkU2oPvSuk3qWsyi3GDVrdUPwck55XX4mOOdLOSwpuqkEPb9WzV6YGQ_3rCVQejRkXzZF7YRFPLk04TGXaESz1z1sqpbUa32fLANCIqj4G3OAR-BhYmznxULQefItR4h3q2ajP02is-jHygJGlgbIYTDvdpp3oxOhaxYr0FX1Q9ouXu8N8Gl4-lz8Ek1japIwYINHE8ciRGTtEc9lbEFNS_V5tDcruKDVRqgr3eGlwC3RQ_aCFjru3of9vKIVWWsh6F928in9HgF6ARq96Dd1PTWhFZgVK2zM5sVB3ARTjCWhpu0wSeziQ475FKwja8X0t6nHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATxNEnphuVhvoHeWGsDYKO1UBBMYWFPFivPZlZS3GkUHvKFxHkUAB4qOHdaSe0eVzaHWbV1ZtCsV1o3Jfdw_nj2CXzuj9aRxJcRwOT9jsdG0vVQfNv0wHROtu8cHvhl2wuJabSF-cvxQkheqcg0WdRrGl21Cr-_hMc1VtHakE3NRHNQvtDnQZXuv1iVd2mj45bMxlp2-zMfwtz8GRZ9qY2KuH86u8BQDrU0owr7oSn0Wm9HTG1mC3yy7AUtAlw3nhDqY8fgiNrHobkD4IabnJAdP7Cye4z6j231EiO5HyumJfXwGR4Dp3LjDj7TOgKlOGsr1GM0JtGo37V6fVlpr3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrYk7FkMy8bW_4DA6Gs7PZx9AXLXKmgytGWxzbUcbqZDVv83LusqNfb5y73XEtOMIQCFZSdmT_AO8VLAIlr8XGTk1rdLiJEAhfBTr8hqJqE9NXnWMEUGQhJZp0LwV1R3gczfk3JRJn9UVifSNeb5WnOhPg8hO46__SiNQvH5GoqMKGD4z4UNxkSRZprXvNb8LwJvlN6fFH4Gp5ngpOrikZ-qah8AFSoI79wehZ5NI5vW6HVP7GLwPoHXQFM3i0kXF1n2oMrjUBxHkgX8duRShyujC12NiodPMQpGulTuJepUlhj-T-cYJiNQVzrrbkiNuXNT-kXXCrjE2IEzlUvLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsIVYeFUDhP3XBuQolyHJPtYU51GG9oyxMinzbHSYm1X6jMgxZycW8e0s5W_X2NmmhHqLYts65yG4UrXgQTKPtMdv-5LGpRIGyuOSVG-w3UdfwPfYcFafFewQYyvfE-uJEIIgDODd5gJRcNhbGtXjTJosElldnObrnLDKtOoZno1ZAmLyFTpGeV6y32mF2qDGqfDRuWYTwStAKiQyFGAZt2bvNSZ0b0Hy1YREn7XmsP8fPSAYWKZFRexY7Vl3iOw-HF8241jw9QJKiO1VdSTVybmul-Wc0ItPzIkXcpO8MmFx-z5xfirwy7mXD5AzESUN3bneIHDrGmFkIAHIynHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAtIx9b-QP-_N1AySSNME945EsMrGhKYEcuEuH-NgGgDwsUkMDs2XwBVDZe3UEWcfNquRcbiLeP28n7IdU0_zNSdnfBz8R5wrQmE6TpXoofL3w4lL5TY_OCuGhl6pXBEdZMn5g5G-tDVwnsz4UcvjbjpzFQT_8Qk3Mqv1LC577_825Dk33UuUD1lr41XDtYzSJylCY1PrXKOD8oOTm0GqxyH2K5H31zi8Reu_jdnRO5QLrEeKrcjpTOAR1WhOdAhdU9w1jf77-NJA_EP_v73nixqieWukjbr2tFSyTlM-U4B4R9BL3i4VBm7bQZ0kIkNO187CqemGKhMrx5hVhJjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=h7bXNKzHL40_ntn6cw6ogViyrsL93z_YLdy_BknGMHRgSedg4BslrjY4RmGDFK_SirQmEFibeG4kno5aUi_F2lMjFjvV5IKXFss72gcd-Xr5iPevu9Et1EU1i6xCV9laAMeC7c0MPmAQi26VdTFQaSjyos_Uvm7Crmjlp43cGDhT-SZ-MU29qiY54bua_MFbTgjd3Zi3EsIELCKl6n37FNkSAZdldV4VQF65o6-VnIHFZNqVZQxtmQomB-6g6OzbtydpuBqZrdwlb6EdC_kQr75lJ5JcNLNHGfcRv8xfo40ys7ksJTweQT-sdPK4Y5KYBFKJH2jwQKg_1lLQ6HK7-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=h7bXNKzHL40_ntn6cw6ogViyrsL93z_YLdy_BknGMHRgSedg4BslrjY4RmGDFK_SirQmEFibeG4kno5aUi_F2lMjFjvV5IKXFss72gcd-Xr5iPevu9Et1EU1i6xCV9laAMeC7c0MPmAQi26VdTFQaSjyos_Uvm7Crmjlp43cGDhT-SZ-MU29qiY54bua_MFbTgjd3Zi3EsIELCKl6n37FNkSAZdldV4VQF65o6-VnIHFZNqVZQxtmQomB-6g6OzbtydpuBqZrdwlb6EdC_kQr75lJ5JcNLNHGfcRv8xfo40ys7ksJTweQT-sdPK4Y5KYBFKJH2jwQKg_1lLQ6HK7-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAvOxFrY3SuhrdtXKU4tidN524JDAUx4W--djkRor71GtR21AIetawxfdCb-TS0ERdnh21Pi0LB9y-RDF0l11l_7rqyA-1J78FNZeujuWr_56Gu-n5zko9BEa_rQudpY99PWNbFVC5z8WKu1yWsXkRpc2vpu9xdDrvl1MLsGjxlKz29KWKDM_PDtq1WeUg1e7Z7QND-Vy9U9ip82NGtYhKPWdCZQb_px7rOfACXTGcjAvic8nb_isAEs_cfLbzVA1fps3GVihl26BFAj3hj5XLTR76p6oI-85G1fZ5laEiViX5ulo025me6bF9ChXCH2yxhmZnVtZXkuIkUPLDiGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907216599.mp4?token=AT1rpxp3xfMNNmyS3h7LEfQRGXairIrS3DKAbIilQOta4fdSSIFuzxc0hW4OzjbNieT_indfjWjYysi5vhj6O1wtKxsdAKnJNFJmWeH-Bfc8dd1ITL3b-zxQAm7JS2VsSvwxditv6OX-BTwbD3HdqgpL5oazlfnLKSeMxDt3fw20BGifYMWcZJU2D9ppt0Q-s_yN_ZFL_M0qFdgumKqyrYdrWR9I9aOZ49CuoZQ7kG5t1oJxkEWDkXsTJzlELrY6pNHCFwCXz076h9S0YR5I-DlKbJOIh6ZVW8n_2NAzYvaXpd5xdsJ1LbYGOYcpNVBsEfBaWHSckVUISY98V2bJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907216599.mp4?token=AT1rpxp3xfMNNmyS3h7LEfQRGXairIrS3DKAbIilQOta4fdSSIFuzxc0hW4OzjbNieT_indfjWjYysi5vhj6O1wtKxsdAKnJNFJmWeH-Bfc8dd1ITL3b-zxQAm7JS2VsSvwxditv6OX-BTwbD3HdqgpL5oazlfnLKSeMxDt3fw20BGifYMWcZJU2D9ppt0Q-s_yN_ZFL_M0qFdgumKqyrYdrWR9I9aOZ49CuoZQ7kG5t1oJxkEWDkXsTJzlELrY6pNHCFwCXz076h9S0YR5I-DlKbJOIh6ZVW8n_2NAzYvaXpd5xdsJ1LbYGOYcpNVBsEfBaWHSckVUISY98V2bJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد گلزنی لیونل مسی، رابرت لواندوفسکی و کریستیانو رونالدو در پنج لیگ معتبر اروپایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IY0QL_q6JBBSwilOE4dRXs8POYaoeQxhuL-ZEp5iPUGW4suyPQL_O_O7iBMqzmqjw4wQih-mJlRC1NznTcQGuQgPR5ZBXBLEWBfr_qKxbgfAlwFUmBYBQDcYfpTI-8ihtM7vu3cjEcFDKlSyBI50IHTvs2IM0G73moy5dOD5q-Esmrv9iFKwSmgZMwqo3GUnGNerICK0-gfZtXoJ-rJfy0b9H31EBvtKOiNMEcxaLZPyPkPxSfglWoDBVvIt2iuf7PwGbJQbdj26QkloBBwaL4S6Bt79xRYl00uRUpm8b6ftficmRFye4WGCAOy9AIc8KnAeaJW10hNIM_YOCCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3foooDA-TZYmZP4szzz4TeaWItogOv5cZkHMDDogZ5yKbIGlq4Z-48XaKQjxU73_h-d_zNEyxzKSfHxdFezaofm_uC9FLB7XFlVaQKpPnhsGe2cqPO3lLbR_oM-kb3zL-AnIQIPIpkN_ObcwgVImc5GrcWWwtu1HBIBiWcORjjf-TsMr5EfbLKwMQzh0pqQbf67sNtv6DVNReVKOGi2Rx-mgaU7FNF6Gmf9casZhh2785NeJQ5GuaZ_3cRzq8KlkAPv5kqsz7iw8WtQnFPiDMlBxBrmhcWDO6Yj3IQ-7ENc7TzJojoOfz0iFErgL9ozrJXtIwnOd9gsMig5gGt_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJQ2igQcfsMkRa7d3vggDrUQ-Sc7iG1vFfwNYUq-dl1ngOZRln7W_IoLMG7s8qlTneL8xj-hW2C6qGrHrQxG7GxXTs18Yr3vvzHbN5-9K0I1f_0mDJvysOrVkxrTMN3Xgeez7l2knj5HX1LadwhT97gX1WHArZe-wRv1cHeld6oHGuK29eHN4h8xCSZw-z-CzihWWyRRI4VHLp_rxspJeBtMjDqSXuJSkyIycFg3vNAhelYd8QwfXo5Yncb8TeTV0GLxP3tbaPsQUhxYWObbO9QJ6l0hD7N7QZ4PZ3Vx7a45MHf-RzMmfu0E52E_-h2tHfyIf9VX5JsgZ_lBSQ1wCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0v2FdQGtGAnszPnX_OTkhmstg_rYvxciqE3Rq6lkb7aPdJqPCzG5GJkZxORmkAWGsjrWzm5Airi47KIgmJMGYZLB6qYxg1yjqFuzkGsUghD0fnCcX7YqCYd_p7y2TSyJJTXGgZVtrPKHGKtI74kmCIQJdNYrmsMuMNijjM1kFAfEX0TbSRjYaQ4l7qH2KNRtnI7Hc-AawDInzoWMP7QZe_yhWpW-bBvIXTw7QuejxOSbRGKsanH_A2uk_n8ebixHrRHAMLDVv-Atosf94LnoqbqH9wCB6J5CiU-v2rKhwT-P0HyKHoyqlGYkSH5nzM9mY6LyQNnGUIVp8oduuG3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u39UZr_flC4VbH6Ol83l_HJ-56KqCIkgV5ImWWrkyoNc33uODFFGqH0QLNLdWziFZVibsScrGuamKhn9kp8IxyBIKUjEEE6-SPT6A_GK4_or1Xveo5Qy3TiV7wKoZVdBf4URCXBYQmJ_NjPxQuc05c-2pczZPlo2UvXOeqBnLM0l-2NvWvorWo7L7_zc3HN65nEBa3mZzr4OKN2ef8VaEYy84zh3zdf1wMEU18LySzlB8prwfz_Q6WrtQD4ue2uRSKgFBbPtbDwESGAmHhfE1fSANTrrKL2tKPjzP2cuvefxsiWzKWj7z-UqpRZhxe4iroglJW6Mu_YmpyXfr03TFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyu8AYC_FcZjcIfm_Xow8GxeyXnxUax1sohc_9EXUAd0fIRiTbgb1zxiok1mA0KHy0YrDUi8Wh5IM0ng_xy10maInMlzSRPf8Q1bQ6dJRONoa56JrdKdYgW_Pru1iDLWOP00S1h0tZ8b7rXIx1r_0NB0Xg4MGKp8dc-HsNzWB2rAF8PMUWxQWa36jr6D5YAhLReMZdl7c_422pE1e1URIIWDqqq0LbPsXV3ZO-e-Jz2h4HHQzVdGvBE_TEFVCdaSjp8sK_6rGzrEG664spTcoKb6xMok6NkdCOGsKs5eN4HIK7BWT5bdycrCRL_qWEAFmA-K3-NimOnzgojP4tKSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbX_tucThSY1q4IR_hM2DTi-QV_1-vGJR0Mo3iUMHkV327eWu5dGgY1-5OyAI8qoM3jlDdE1bnj-0wR0faAZZ132Kyh2MEdTjAFCW4Lt40FI-fZl5CXs1DOA912H3RKllcK7BxSlCIJvfvv-cNtMdnpAVBV3EgMk3hQzzj7OZZtTDMiBvNShVKgw8yVzXwTLMse0B8yy4MX-SAeTzKsmZCO5hnvIAkpVlz4fFR7we3fsxIRpcL_3UXSGCbNm6eSikXuKZk3SE4PqJg02RFjDxHjTBcHZYorS1eFuEf00kiZrYzkKhLLtCJjsJAwcztbA2NbId7-Z26a4akxQLkoVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em1nPWJRLo2WYVOC5lDXBcZoCqch5jRXLS0ImUKQnm9L-9kVYjwzJpQ2FzJ5btjLHCDoM_hc9ZRw6nmZcUfX6oR-uH7teVU9VrQbCHXlZdayjdpXScEzdvlwcoj1QJWTQA2X-e2uxMqibc2j_kyWZcKNJYsjAGvr80ll2U5Arnb_CLLjWARNEOM8t1o5MieGofcwjta7BXKUTOddJ9L0hmA11WXBGzU5IYX4VgVmZTpaXw9oRjZBI6nnxjbkmYNqjkAaekJzY9zh3n0neZovjwPa8PbB9XLXykkfYT13y-wFoqTNQ9DcZIpwljMWmvPp48cRNQhW7_kW0tLBR5Sp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX_uJOBO79iOiDII_qBVxLe0DhQGzCWqV9Lj9i0EsMdwPCr3qWYZhemn67StfX25eW_JpO2ECM5NkSoQFxM3_lvod3kxY9mr0BZfS0qj9DNNpBhfGW74epzYjmHK4F8TP8zgMx6AWg8RD8FJthKGsQwZGvA5ZUPCzxYmUbdOPdZDEBYVg8OKe7HkZSSekA5ZL4TEGNKqmGBzy1lKWJcC8RvxqqQPqrUVMNoQJwCzkRc3fIN8nKSlUHj20q9l4tqQUlzdTkttdtDBqWdSeXFgJL667WgyVtZs6BMNgQes71QnE2p1EeTG_PpZyOPGcpep3pBJM8T2pfPXu7i_pARNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
