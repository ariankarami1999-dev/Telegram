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
<img src="https://cdn4.telesco.pe/file/LKw2Rrp86RoJRNZXzxC_qK7bF_T8LSccWPwEygA2huMj-hdF_lmbUuQIlQD8c-C9a6MyHK0JqEgPPFQJWPl2Q5N7CNYIjMOLkf57N3UQWDmndBc4pkTzFuuQ-dwdB6teseAT37GL0KrSn4kH7GWInaoFdu2XrgwogA9LxNfBsSDZAUSL6SLFkP7iWKBS_-xsxZLbpiUaoFcukyNFHjtO_BSgak-8C_WTeJ4AhPNuORUgLEFIoRJUVBURfER9xI3TAr3IL465btl_9A6XRi1SPmcqnfbIC1vehyc-yM4FSIE1NQKHBj8z6Ile3xPnN69g3gsG3XZVqtsCatp0EoJ-wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=KoeCSgVYTmaY20OqFKGozP9C7ZiCvMr9GOAVMdovKvtauyzUoDdY9tgrXoxVzI1xtnwoGpPzRAplVimglaQmWVa9ekjZ4V8DqH1VXCnCRlQL4gFHbJ9tuKITHXvKnyjncY2mI44a-1oELjv8If5lHSpQ5wi9Xqa4ZTFSK5S679WyyRE1V8oQpFI4XvBxbr_wQkcZT_19MSDEosUioHUZ4VrmI0PTyQF6HSJ-HE7mTGBhrYIOdcbQV4edjYi1KqnMh6BYiwJMNhTym-xhgqGZD2DzXEw1cRkLfQNuiRjsvyX_EJ92OqToallW42L9VUfbfpXqAeuHUbDJ-WdFximUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=KoeCSgVYTmaY20OqFKGozP9C7ZiCvMr9GOAVMdovKvtauyzUoDdY9tgrXoxVzI1xtnwoGpPzRAplVimglaQmWVa9ekjZ4V8DqH1VXCnCRlQL4gFHbJ9tuKITHXvKnyjncY2mI44a-1oELjv8If5lHSpQ5wi9Xqa4ZTFSK5S679WyyRE1V8oQpFI4XvBxbr_wQkcZT_19MSDEosUioHUZ4VrmI0PTyQF6HSJ-HE7mTGBhrYIOdcbQV4edjYi1KqnMh6BYiwJMNhTym-xhgqGZD2DzXEw1cRkLfQNuiRjsvyX_EJ92OqToallW42L9VUfbfpXqAeuHUbDJ-WdFximUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=noiKo1joVIa1LcucPtvWpTmZtJ2LxtuWLWMI1NmBY8VhM_ISdiSe1aNbqOozPEaqvN-3PKByGQac4kKB-q1H9p7t-qPuPYDltwOT0VqzUX7M8lnYBh_hMfUQOunFKWeRRwLolYJqj929xRHeLSlF8NrqHd19uT1s0QOjTdc-1GkYPRnXSga9xLwmM-Jk3fJmbIY67eIvaLOT6G-bz_hHa3fbEsW9__TvlNJaVjHUUiX-lYCQ_wxklxFJ3Qq28nXVRAUD1MbGy8aUvSMUTzIg8McveJubKGkNQVU1VaABRbZkJ_ebvX38Pgx2aRnJKnTiRr0wAfgPm2C0pm-vOd78Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=noiKo1joVIa1LcucPtvWpTmZtJ2LxtuWLWMI1NmBY8VhM_ISdiSe1aNbqOozPEaqvN-3PKByGQac4kKB-q1H9p7t-qPuPYDltwOT0VqzUX7M8lnYBh_hMfUQOunFKWeRRwLolYJqj929xRHeLSlF8NrqHd19uT1s0QOjTdc-1GkYPRnXSga9xLwmM-Jk3fJmbIY67eIvaLOT6G-bz_hHa3fbEsW9__TvlNJaVjHUUiX-lYCQ_wxklxFJ3Qq28nXVRAUD1MbGy8aUvSMUTzIg8McveJubKGkNQVU1VaABRbZkJ_ebvX38Pgx2aRnJKnTiRr0wAfgPm2C0pm-vOd78Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=TDS2DpRWzVFJy5pmhY2Qs5ek5xEeJOK9UCnizS-9qVobuFTjRPtL9jnjKvNY6jOKtL5Ep_o3aRpTkbG48qWD54PatXXvAb57tzqn48SDsjMQOqfukQI0CvjOY0ftf5qbcUnCtHP-U6qMpmdADNdgakM8DH67V-o_bp6nNwX_xw5S3uZ7AutZH7HFCA-vgAqVfrPzzRqP9C8q-dUdfAPfaxqIVqAxGTDdosL8eTrB-NU4RRSqOZ_Abl_c3y1iBMLFWklHj9ki2E7huMtEgvAhcU9OwbjrgCVTOBkjzkKHc_5DJD06tItbwxKWQkIUJ6sftjuTDgHIYY1DSto5jpX1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=TDS2DpRWzVFJy5pmhY2Qs5ek5xEeJOK9UCnizS-9qVobuFTjRPtL9jnjKvNY6jOKtL5Ep_o3aRpTkbG48qWD54PatXXvAb57tzqn48SDsjMQOqfukQI0CvjOY0ftf5qbcUnCtHP-U6qMpmdADNdgakM8DH67V-o_bp6nNwX_xw5S3uZ7AutZH7HFCA-vgAqVfrPzzRqP9C8q-dUdfAPfaxqIVqAxGTDdosL8eTrB-NU4RRSqOZ_Abl_c3y1iBMLFWklHj9ki2E7huMtEgvAhcU9OwbjrgCVTOBkjzkKHc_5DJD06tItbwxKWQkIUJ6sftjuTDgHIYY1DSto5jpX1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7Bar7z-6BMUnPpEwd4GqW1pELGV8GT4lpagUPhNXZngGLdrkxr_wNWTXSBpPnUb0RpDaUkDOheTD4YDiyxpnBZD-pJ8xf0w6gWjUpoBq0j9eI6SAKxY26qkS6k4pjQ2V84STNXpjK8Z-3dnV7TBWAJZz-vqvhT6-A-7YOahWg5AILo1K4hr4K5BBhYq2d17jdogpJJU5hrkk1cqHjNbRJ_4BQaVnb83kP9ZDqFJn9iDuTS6PCLWpUana7wlzch340ry-soxuJAk4MKg2JcI2a0aIw_XZDIFKZC9BJsXP7aFjNEWJupb_QTFkfwSDi-IsJ-nBzSTeWZIkAxn-dTamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=K7ZHTc_aoXX9xebGvZgvQd_87z3sUmoBeOW6_WjpgPOlGlQIx1ZD9WswPnXu8xTWQhOUicZlgZI-ImjupyD7p8E4auw6q5InAXU3pjeO67xNEy-Xe0ISliwZpxDOuAH7_ydgM9EaJ3ixLixHuglAEKsdiHw0U8a6-vX3SwCYeB6Ju2I640mXxuRZLSxEugIGBQfactI3VW_XxJVvm1cEL6SEx5cy6N1XJATDEOjeh-o2-H1yoFVO9WAgQNdsuys3LH3lh1L88w5TLzHIBRL6fLBHGtLAzMLnJebzpJIohbCba8EK6bI41pTDFrJ0t772stzADRysO-cdXh_O652Hfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=K7ZHTc_aoXX9xebGvZgvQd_87z3sUmoBeOW6_WjpgPOlGlQIx1ZD9WswPnXu8xTWQhOUicZlgZI-ImjupyD7p8E4auw6q5InAXU3pjeO67xNEy-Xe0ISliwZpxDOuAH7_ydgM9EaJ3ixLixHuglAEKsdiHw0U8a6-vX3SwCYeB6Ju2I640mXxuRZLSxEugIGBQfactI3VW_XxJVvm1cEL6SEx5cy6N1XJATDEOjeh-o2-H1yoFVO9WAgQNdsuys3LH3lh1L88w5TLzHIBRL6fLBHGtLAzMLnJebzpJIohbCba8EK6bI41pTDFrJ0t772stzADRysO-cdXh_O652Hfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-ZIxJXvUFjR2IbLA-xJ-YwWCQ9PZ3e6aySEA-7VUf_UaPeuhZ-66586ZWaVi5jktBUCoeh5yP7fShzMQM52Kp2G0MwVeoRuAkZe2mTOlkz635p0-_79LE3FqF_jfMf9S7gg6LrJ4zpIakkf5Q46z1KMx3Llnx_LDk6z5zUbiSNqFM4YuvbBktBsQXoXBskWCeqCpLVCwqmIWNRm24n93l9SO2h2BU_obJDn10Ycri9ng7o8U84J9JlLyJh1KG0YgPAG8h6wMbqR77j_1Vqg6rTblOMxD9-5q_R-1OzErSunbKlATNMsCDH_18b4U4ZlTrkXu9PWmciGL_W__aaXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KJFc2c1BF2LPYRz4qrjGlFlH-U9zCeLy7kz1sL2HGSHf72jcKB0VYCgR7Vmhs54wqdtNnR8JWG8VDhCwH3bspTAMSCKKvxUeKwWuSNAJ8_6CFlhHNvlBjoP4oNQ0erB9bRTzdIB8Hp-dZy39JyI0MXCMHYoM9eyH-Xz-E4mPDVL8Cq-DlHKcHggd_lonm8V9LDEkq_33-7Q7LRgl61tqP411nC0UJxZ4c6TlLz_wvCtb0UTPF0_GByiD0bDdU-4m8pzbnZX-bfYEa4qkG__-UftnjspyfEb9ohpZhOfVHFW76No1KMjenzCC1Dlg4r1Q7kV4Qkylmb6gQLhbJCOibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KJFc2c1BF2LPYRz4qrjGlFlH-U9zCeLy7kz1sL2HGSHf72jcKB0VYCgR7Vmhs54wqdtNnR8JWG8VDhCwH3bspTAMSCKKvxUeKwWuSNAJ8_6CFlhHNvlBjoP4oNQ0erB9bRTzdIB8Hp-dZy39JyI0MXCMHYoM9eyH-Xz-E4mPDVL8Cq-DlHKcHggd_lonm8V9LDEkq_33-7Q7LRgl61tqP411nC0UJxZ4c6TlLz_wvCtb0UTPF0_GByiD0bDdU-4m8pzbnZX-bfYEa4qkG__-UftnjspyfEb9ohpZhOfVHFW76No1KMjenzCC1Dlg4r1Q7kV4Qkylmb6gQLhbJCOibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3LYbBSCxBfE4yU4lSfSPnRiYrGgmC0kl1ek2pozHlTbJjo31P_u1oBnLp17qISw2cEyKfuGYH6S2O2-azr5_aDvN4uzZRrJN0yHdqwuInkJgmPqwgWyFwfRezyCZ4g_YEc3HnZUe4xggt8MWC441EBTcZzTZf_lQOHd7zN2AYN_5QvlrbKh3w6UGMKq9BFn7Na1KHTbEmnowGV2AsoGZMV84zvEvH9rZPGl2Zlb01LPdLZdKJggaRScFSivLk99JzFdhyp7xJm6YZa_UccdfmWnnbIE0pRVYipo9xxGC4wszyhyV_ylsZfIlxCUuCbZvbr3ns_BB42dOhGkSVufiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anDXrE4z3jZV1Kb9Rw0ytqdBT0n4oE6v1LERK2lSBW-a4nyRZm2_7qmgk8UW1NwsfsjZor1iYPUcs6b_yxghpVmvJ7GpSLS1fLO3WKGohQqkcHQM_JOv0LTIan9SzBYXyHwEEvqIbXYKD3EItToxQ9y7v2J5B3Rp30Rn7HAsBKOjvOPmig4BOBukYqhNO5lAePUmNsjJjxxvvlUK97VrqL56aCOz2plmN-lrXi_oBwKV3iKvuv9OwbPhjeh2QI1UXKXI-aG0sNmAS68XLmNkkBZidfA6cHVqGHGj1gdvdoOW2cPjxiEZYW6f0at-hpRrZf_mzoBEhGxcA6GzNt6BRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AakxK_3gqpJGNRYk0v3m82oZbiS73HrNqZrhQeUYX01Xwq-KHiYj4FqxOLyan9f82maFaLDe0nRSwZzbbYjk_DPaOyD4VIqoo5aP5Uxn93XH7UYheMBUX77o7TbKaP_79e-pFg1WYRL-tHTcojoGwAefPKNhwCXW62fSde3l8iivfZuSM7AwRiwpcCJOxKN_wwkTn-liNXTrgumiKTvGpSC2aO2R8u4qhQoHRacHL69RYunoXGrTdPV8HIY741AJxkgA5Hs6KIL6i34_DbFTAhwtNSp3ztXKgftVdUeteVoiVG6X22Sf_Sh26vCDQ02R-zOhjNiYSkdYDwMHBs9ZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePTWKuUcLKZhe-gE4mGHKzyqUGP8v_aCFQcrFM6ceOdbTSfqlZy8-1XU1ibA0_mJO325_RmJpeA4CzihUY6akwFT4onyrm97JqXqrfXwjSAf7eupaIdgnGAA78eMQrciC2sGKzUJKMCoe64EkpNm8P8aIwwULRvT7s2W3Xzb3k6i9vFTc7DeZRpa6oCm3-Z_Hj36dH-RT0RUSwpK8NFMDjkItR0H5N0uxCD-2I3hEcwUqG6nh6Qdz0jZnH_ST6pCWH66CrMjWGjTlKJyH5onXES3EZY21YNYt3WPWL3eDQ7OhRo80Rt89foS2KO7PxWLecu4vbBrIu4BIpfr8KT-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOXBK7jDEPtL39ZHsM0bSeXDMcIgb_643z4pH0Q2-sZea_U4GxMHgZFKeWY0p2f2_ple1jlIm4jkrrKm9TR3KYFLV-n1u-rDLP7RjLHgLiI3h44WwxO_kP81a_KmSHOpy5IAutjak7vGux_VXbBKoJt2Yml-tSMkf0DjnWRhzkD-u27Dehnx7dehTSnWkAVPz0pnzlhymR4Ux8GHF8t1ZX7vYQoiMxKhhuNcgwu1IpTwndCVMLRVj8VPjVeo0VTylwoSOTufNgPipyg0EUHzO4oh05wd4gW_UJ_2m06ltb40gwkqqwVnYKlbM1SijqyP8BjTheToEuiLGt1RkCk88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=HtbWwOHmZGBisN6ajmbB-3vBIVgLJSw0bUfg0sC1H1dkGHmfkjgWxbP4203BQBMPOkHvc9_sGwnjktyzdzWqM54ki9DYDrLZiyMSuk3IBE9ab27SvjhGzRPsXXHFBDyIC2dC4_GhqUR_KuCJsXodZreg-Vo6ojnP8pYp5S7qIPAzjIhu_iC41aWHKy47jaXTWJ3mPz0cZSl8tizKg2-TyPPseHeFdFOIqIhmfLWRmjjrziZrGWpNjTIOgGMAGTNjcC9fy6YBxdLVtwm7bqq7B8gvwyhqqzjJtqquYalV9JrFd3uvfioRA4mcCUtGlpGYBznG9VKD_XRaPFTDScKsMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=HtbWwOHmZGBisN6ajmbB-3vBIVgLJSw0bUfg0sC1H1dkGHmfkjgWxbP4203BQBMPOkHvc9_sGwnjktyzdzWqM54ki9DYDrLZiyMSuk3IBE9ab27SvjhGzRPsXXHFBDyIC2dC4_GhqUR_KuCJsXodZreg-Vo6ojnP8pYp5S7qIPAzjIhu_iC41aWHKy47jaXTWJ3mPz0cZSl8tizKg2-TyPPseHeFdFOIqIhmfLWRmjjrziZrGWpNjTIOgGMAGTNjcC9fy6YBxdLVtwm7bqq7B8gvwyhqqzjJtqquYalV9JrFd3uvfioRA4mcCUtGlpGYBznG9VKD_XRaPFTDScKsMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ah8B57JcI_fq0s-Yd6W0H6PViNp0TXJVyWU43jL6W98k1GJl-FEddc-vm1SbEUAUbw6VfAXA5DeW5CepJUCsW-tRKPHM3DCD2IHyv7kXjCw3lMcj2HgGhdLyX81LsiBx7-dAtW5UU3i8qxaBbjaBCaliSsPBXz-ru7AdGH7OwR5AhvvFkw5yF-J8N0cDF8QW0BgxcA0iNyeodFtTe340rQFwULe080Rp0rU7btTifDQriUwAyoFiSAKFJg1ffis9q2YaGVl8skqw8dURfW6MpRxjpH1gelxFBHmE1jq8F03uBM84ZmkDTB0IwnXMpJJC0SCfuh9B3fA8KybbGiv-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ah8B57JcI_fq0s-Yd6W0H6PViNp0TXJVyWU43jL6W98k1GJl-FEddc-vm1SbEUAUbw6VfAXA5DeW5CepJUCsW-tRKPHM3DCD2IHyv7kXjCw3lMcj2HgGhdLyX81LsiBx7-dAtW5UU3i8qxaBbjaBCaliSsPBXz-ru7AdGH7OwR5AhvvFkw5yF-J8N0cDF8QW0BgxcA0iNyeodFtTe340rQFwULe080Rp0rU7btTifDQriUwAyoFiSAKFJg1ffis9q2YaGVl8skqw8dURfW6MpRxjpH1gelxFBHmE1jq8F03uBM84ZmkDTB0IwnXMpJJC0SCfuh9B3fA8KybbGiv-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=LfGwajZiRdxRm22gKbg65dXyQjcjLi2Y6YdMG_s2x_3SKwfXhxLhUnSYDj9-wEVSScHRsV4zLfkGW7-rdGmp4I1m-B0aR10xqCHpGVg8UzKB3hBfHX8nPo7ZqhA1A_p5o5BrmSw9ax5BKNB4i82y1QJjOqoz9FNcZ-IQ_7PeuugVk-CiE_daA4mEQ0l1NiHkjwnk0a7FBVQrYBNGQKkoUN6bYFXxRC6rrl28eTsK-l8IlJDv0h5yOlo4E9A5WSQofRujH7_a24KPQDyh5U2igDIhwYrI4SdCQjP_BCy4jatetB5PaNhzuimWvI6qMNhkPrHaNphXjsB1iRVpDVno9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=LfGwajZiRdxRm22gKbg65dXyQjcjLi2Y6YdMG_s2x_3SKwfXhxLhUnSYDj9-wEVSScHRsV4zLfkGW7-rdGmp4I1m-B0aR10xqCHpGVg8UzKB3hBfHX8nPo7ZqhA1A_p5o5BrmSw9ax5BKNB4i82y1QJjOqoz9FNcZ-IQ_7PeuugVk-CiE_daA4mEQ0l1NiHkjwnk0a7FBVQrYBNGQKkoUN6bYFXxRC6rrl28eTsK-l8IlJDv0h5yOlo4E9A5WSQofRujH7_a24KPQDyh5U2igDIhwYrI4SdCQjP_BCy4jatetB5PaNhzuimWvI6qMNhkPrHaNphXjsB1iRVpDVno9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=QbhMLfvaZGwpByjEtIB1lWlqnBZCUUiVpYyRv_ZIZ2ab4JGpv-4qlQ1AFPpJj3DwWDdGFDINyXInSbfQo_L9I9pXA9sxVc_W8_lNztqU4aJ4Y2KBsAzR8YAY5yHHpyyGrvVXdgXSqg-uRUw8Y0gwHTwWlsHcPyD2ZViHhn_dFo9tSr-nQvTu-0GYKqMxHXm5CuzVUz9WL6rpqqxxwsjeAARGzxeHLfSft9CsAwESYvtGAwggDyacF9K924-ZWUH_uQpEouDgiOqXpIqaEYmSdLf-3As9fw4IbCknZEmUayILC-XpbSzD-zU7az8cEhnLNWcbf3u-H_gMkl3uD8_ZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=QbhMLfvaZGwpByjEtIB1lWlqnBZCUUiVpYyRv_ZIZ2ab4JGpv-4qlQ1AFPpJj3DwWDdGFDINyXInSbfQo_L9I9pXA9sxVc_W8_lNztqU4aJ4Y2KBsAzR8YAY5yHHpyyGrvVXdgXSqg-uRUw8Y0gwHTwWlsHcPyD2ZViHhn_dFo9tSr-nQvTu-0GYKqMxHXm5CuzVUz9WL6rpqqxxwsjeAARGzxeHLfSft9CsAwESYvtGAwggDyacF9K924-ZWUH_uQpEouDgiOqXpIqaEYmSdLf-3As9fw4IbCknZEmUayILC-XpbSzD-zU7az8cEhnLNWcbf3u-H_gMkl3uD8_ZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlxmejmduMljCpoeBrdOTGTSUEpCWKx2Li6gB_MpPkYeOn37kCQ8ZPWhchoSzZ-jxuE2tLfeZSx35UUJmjY3VNG1UU4hgjESWqK343K3QVH7tk-8y1RCEQ9YId0tHB4BnJVj5GGoR8BmgVegpRgfjhlFE0WVPSrwPuWhdTEDVVq3r9OnywlmXozfnDlPBRnZgPhsJQRsewuj70AlwimnErQNQ-UUSdXBBTvjvMxMTVugQ6pLVzG8hn7NGPAsZUnKm5P7PRqU9wLTYdhCUooKYpmTR63E-XaDFAbsNde5XjgU8fOp1uk9Hp9ib3w6TblSuIlDpUHA8IcV_FV-1vQQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5W9ggORE-Wl_whefatxB4ESciQC6PytqJjZHD1z7pS-CJLsPrQ2_Znp2Yilq1qozixWsxK1IyAZCGMt-hqP4oDkHp_IQOPfgpHh8pU4t4iS5v_sqWVefYmX049vy-rIYHjLcT7RPCDy00N9z8Cr5PLjd1VPBWIGgX6KFFS_M-IUX7BDgBHwSFcWwHIg9hZnxQtlagDIS62EIVpy_4d0uVe8hzXiMWg_nG6wLLbg0770K7f8S5Ifh3_oAsNn0cDYy_ic0eAHJPC-Jj5ydQ3ptGuXaeUqkFGGdGClcoil1j8NTFmQ2Sjl7tHqQFU0nwYFWvzudxyLihvPe8VuXPh7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=gkryIT7Xzwuovp-SUcZAysh14Zeg_PYHqEcd-IPlsIZCB6ziw9y_H2tnkcxXA-NzgBHmHuU45w86eSTbipE8-i3pEijkN7RBFL5ukX62IhW91i4cpCvU_rC-cFM5W_rd8UG-l3FzwH9laLKR2GROqb9qA86kftts7unyI99VWerRnqVfw5s2EjJ_Wy07r7fyx1LMrJeJMg4WRV08KVCwiNN4rCy34rYwaxVRf2nNf5rCNo5-IMZv94wioE6VnsrUleaMl_O5Gx0grfNvTkzTSBW4t10QSnf2gNJ8dhCVI04H5y3DBPgCXmOxJC4U6gp8zm5b2xArAs-njbVuVTTZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=gkryIT7Xzwuovp-SUcZAysh14Zeg_PYHqEcd-IPlsIZCB6ziw9y_H2tnkcxXA-NzgBHmHuU45w86eSTbipE8-i3pEijkN7RBFL5ukX62IhW91i4cpCvU_rC-cFM5W_rd8UG-l3FzwH9laLKR2GROqb9qA86kftts7unyI99VWerRnqVfw5s2EjJ_Wy07r7fyx1LMrJeJMg4WRV08KVCwiNN4rCy34rYwaxVRf2nNf5rCNo5-IMZv94wioE6VnsrUleaMl_O5Gx0grfNvTkzTSBW4t10QSnf2gNJ8dhCVI04H5y3DBPgCXmOxJC4U6gp8zm5b2xArAs-njbVuVTTZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DweQNUb1_m9VhkbrwD5Rc_IcwVhPFQ_bphK7gXAw4t1scDznIkjzsujTAa0pU8R1E9FMrGO6npA7LEHFXP7lFjM9ndjUIlET7Rd_vhEsz0n1jrM0tpnoltyz3lKT5bcAj0GgOWkr5AjGOslgIEZABsPQcWEswY19FsMbiYUU8nAFgUKYNDeviWGz-F4CYO_KaQPTvE4qiEajzrdswVQcvaRgTumWuJDhsPmqUeJqcf0_zYRcrztj8UnIsJnMe5DXKvCC_a6w3XpbgZal6dP2LVZK9OMUhK2wvZQVZXTGUzM1HLJ3xLe5cF2FGwA4yJ3erSIci1TJg5eSq9np6EjzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=ej-FI3UP_QLoTve7Odteqhf1CdIlEsFZzoC5LbW-duoFSWwZt-nije6y1J05Aun3LiYB8elw8dVCYWj9_2yAOnOxn5rItWYGFUUs-0pMPBpmy4vK1dPtZGSQG9O8aVv6kQ_FW0jSZi_ekLVl5-_Qr8btvxf3W38GKHaFgLpAcJoRD3vMu3o4s5BhYxmDStGMZ6zq5OPEZMN8qzbGvnRVU82txu4hXiKXO7DUWGsLT7rmSDqPTsJ3R2_qliuITyDI1mmc8_2RNpLxFHWoo_qkl8Zmqhi4CHoGNuazW4HK2b_t1PfZr7-laQyAwekqw6kayQfP_YxNilsUgHH9WDeteA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=ej-FI3UP_QLoTve7Odteqhf1CdIlEsFZzoC5LbW-duoFSWwZt-nije6y1J05Aun3LiYB8elw8dVCYWj9_2yAOnOxn5rItWYGFUUs-0pMPBpmy4vK1dPtZGSQG9O8aVv6kQ_FW0jSZi_ekLVl5-_Qr8btvxf3W38GKHaFgLpAcJoRD3vMu3o4s5BhYxmDStGMZ6zq5OPEZMN8qzbGvnRVU82txu4hXiKXO7DUWGsLT7rmSDqPTsJ3R2_qliuITyDI1mmc8_2RNpLxFHWoo_qkl8Zmqhi4CHoGNuazW4HK2b_t1PfZr7-laQyAwekqw6kayQfP_YxNilsUgHH9WDeteA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or9jh83MeBipDLR4jP8hZkdUu79GkZiUYTy-paR3Wjm078foggnvKWW_07alaDlDgHzRO7YFIxIBqmGOzoJJ2082_wbMFOUynRlTmgMasiyJAQr9iP3aaorLzJTw5sk1qvAWvQeXTNNoA5zzTL2RhhU7V0D1aZHG6pkwD5g-BTpl2bFskZ0b-fC5toEVV4xttR5jJud2O0nDycuz_Rc2G9urnzx8MEEt2lv534zMPkFfCJVkABfI8NsQiZkZLD5fTgFBV_IlhKsk3pSqrfcqXqNJN9vpfIdzKevV-QpaMdlgTJURpholFd4fsx7ACn1G5xgcpmpovzXjOUQCHTqQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrAz7TNLh-j45s-aznEr8jqe2gJZa_HKVca62WxuT8aCm-yifVH-B7CniHCadBekjWQnpC6Az_31PiSVgGg5s82FtNnC1TzzwjaZ8-t007MSmSl4EZgJFLHvd_NV3ajnNAHcRnhZPeLb3H1mSF-4MriwRaY16j4sxFDTpE5LUPegpDh3CkJBrYoXH6Nfy91OfRJMmGKun-9fIZ6d8oKfpStdvXwu7yWnyDY4MVSHI1K1OPeLJ7qRxZYjrqbQmGT1TT3-JN_xJKsSF7I01_nWRa1uDzE6meJtZX4ToCJihHU9yZtR8mmMGkg8FNOscgApgWeTESB9NBoo3aTiiP9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HPrDbAnEZgQ7ivutsX02ZqYP5doAzkA46NJr3R_JrRT3IC_UPmMC89dJEQH5Qqy0kuWZYPNQAn1QlEc52tYPdJT7-rrUYk1TbrIk9a2mxjZlSbSp-xQkldoWjdmwo1yoLcMS3di4UthTgK6rGHxCs4gLh7Pywf1hsrIDZVccXZNFnV2ZRx_vGCfhp6d6grE9jLyJpwVbSZZYTZQCLIMj_TifqFyfpn2BzOVFfA4clNPpit83rLQJeZfA6_zAioVJLKXMqIc-_NxMcJSPN1uPCJkMe7OSSPN3jT2xb6QdQgG67kiKDItVy1i6wtay4rKn8CVkCqEs-ja1vh0Fg53ByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HPrDbAnEZgQ7ivutsX02ZqYP5doAzkA46NJr3R_JrRT3IC_UPmMC89dJEQH5Qqy0kuWZYPNQAn1QlEc52tYPdJT7-rrUYk1TbrIk9a2mxjZlSbSp-xQkldoWjdmwo1yoLcMS3di4UthTgK6rGHxCs4gLh7Pywf1hsrIDZVccXZNFnV2ZRx_vGCfhp6d6grE9jLyJpwVbSZZYTZQCLIMj_TifqFyfpn2BzOVFfA4clNPpit83rLQJeZfA6_zAioVJLKXMqIc-_NxMcJSPN1uPCJkMe7OSSPN3jT2xb6QdQgG67kiKDItVy1i6wtay4rKn8CVkCqEs-ja1vh0Fg53ByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FYmypVXY3nn6kfbq1miX6vjLBrvOo9W7E8KZB6v_jFY0Bdb-O59hzij6GBOu1wr8f-57v6DdJQXGvNwivgtuuijl_N5OxFQfsQ0zU2_BtFzgwxI-ePf4a67tn-H5ZsX2tS1qdWgXWWlIeUX7kufX2nUBk8bcqGAqWutc7QmmsQp0Jz6_nn0PtAWRtrD_KOfUjJPVPdoLKzFjFiU67LKp5s-etjxdpc0tS95cxdx8H8x06pqU4wNisUo96L-eH4v6bPbKZlHjOgryo2fP9WtxDemXmoTeMevFr19T9nFSF0uuc9AeU7jSBMwT-SSE8IxQrhKGT3-wplB6EaGNHdkGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FYmypVXY3nn6kfbq1miX6vjLBrvOo9W7E8KZB6v_jFY0Bdb-O59hzij6GBOu1wr8f-57v6DdJQXGvNwivgtuuijl_N5OxFQfsQ0zU2_BtFzgwxI-ePf4a67tn-H5ZsX2tS1qdWgXWWlIeUX7kufX2nUBk8bcqGAqWutc7QmmsQp0Jz6_nn0PtAWRtrD_KOfUjJPVPdoLKzFjFiU67LKp5s-etjxdpc0tS95cxdx8H8x06pqU4wNisUo96L-eH4v6bPbKZlHjOgryo2fP9WtxDemXmoTeMevFr19T9nFSF0uuc9AeU7jSBMwT-SSE8IxQrhKGT3-wplB6EaGNHdkGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAiCsJXaOfYMym2sHHAI96uEcvn2a2DwC4ToUJJue7itw27HSTt15UXFgtCENCINj2aWNTAdpUhJ7nHzbb6uHursEuQEWHtCsKDxYRorzlxWlAmXC0rJBovvx36hIqsHa-2R6Ebmecl71VB4Ax6zqgVf8PVQiD9KUERl3eRyizElf8r8DTGj-olj22rzttfBfEDwuiQMx1ZXR8Ua4U_yD3ODLQmcGCkfxoGmPh3eTXh34Z8qrd3hI6ezbvFpuVMuW0dHqqA_8bkSZYazmvDt_eho9L4QhHaoMF-AswbH7PMJbHIVQ2OieVntKU8_HGvZRMcEVcQyNyupYSYSzEHxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFDO_p3OvEXMCS7FfunDQU42K0aZcAYP9x9685OhpwG9a6A7CPLHVjWURA5H2Rhmbc2MKiPpusekDaKrugLATjNPDlkinb4gibCXIjHYeINg6jKUYWxUmvmrPQRzoigTtmYbhTJyo42pVGk05_z64jST-ZWoB9vI-H6GzLVVxNBe4Y53KZDXuAnRpwfjJy0oOtwLK-0L3GeMqPiMSKptu4Pc0evrsGwzIKqpf3Tko3qhlQx-B3LL-782fjBv9R2_dJK8Ai9X43R19oQ71ccexhHyW9IYeFV5IIu2tLkBd6RT94ZIcUI3GSK4HaF7zu9ki4BXjceQcRc2hMq9c5YE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gi4ryHUwIpcezc4FpU4S1X2_MPbS-lUXSf3BsqQJvgdMxfjAns0DYrwGJKO-z8OQ1QF_WO5HQ3xGqAB5GsKTgu_kdTA4CcVoaMpfJjzn8yrrGrrfnI62zAwSivnU05hl5DCtykks52rCsoGsMa4cjqe1bTe2N2wvQIOZAG15gLoKMzJjM9uC04o_BRSoMUmTqHvENqer6TQB93_AOx-n4XN5nLw8opugYHrX57gDXd-d4HINC-M9xDwrxX8Jysq6yGJBMZKNX11zxAJQoTCZUlKLDejATq9bW26YhmFZdKlFo0PAZKrgXchEfggtCZQZeZ_fC82H-NlYw5ltgI0gDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=hUjpDubvaq-Ov1beSfXNr7upr40dQPubf71katdp6YZ7cH4bVTkebDKJCxFEL-26WsxqClYjk0sYukH-8Mmrg78HW7bwEjmTbsXiU8p_av2M4uA97nEOZmy5mlUfy7dbML6iRomQ6-3WM0VHfZQ3I4cQCQ--I2I-oxXXF1RgXK2IYQfAp90QsFtRQfRVN96kgwTTMIrnS1E1ZWZ8cSAzLSOuHb-JheVk-NQVeIz0p1cibHh-yyNziVyGQcTkrhZojL9VYdC6z4wtL1O7ivpl3CDsw4pcoJAapTH61eTFsEgUT_Q9VFxDwQm2Jg5KaIN9HX-2OykyptHictQeFidEdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=hUjpDubvaq-Ov1beSfXNr7upr40dQPubf71katdp6YZ7cH4bVTkebDKJCxFEL-26WsxqClYjk0sYukH-8Mmrg78HW7bwEjmTbsXiU8p_av2M4uA97nEOZmy5mlUfy7dbML6iRomQ6-3WM0VHfZQ3I4cQCQ--I2I-oxXXF1RgXK2IYQfAp90QsFtRQfRVN96kgwTTMIrnS1E1ZWZ8cSAzLSOuHb-JheVk-NQVeIz0p1cibHh-yyNziVyGQcTkrhZojL9VYdC6z4wtL1O7ivpl3CDsw4pcoJAapTH61eTFsEgUT_Q9VFxDwQm2Jg5KaIN9HX-2OykyptHictQeFidEdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNNechRRs8BkC7pO3yeCwQRxZgQM9djV6IFiqI87r_Afea0FBgQGBhntb61NWOpRaHM_7vQEXbjQsicRzS6T_4UTN1WzPOnXt4VyioQ7TZ38rers5Hz34F1pDqQHMulXPIxN5WCFUxh2SDE_TAlp9GZB5NbCBtf4s_Wck2xZq3_esyII4kDvS1RYWgu7gDQt9i_VJRHCEs6N0wTgyzbOQHj-28zQ3_sVIa6jUk7kvSRRglHOZnZVQLxOppZmV9XZ2VxZlrSbzV5___eif9IPIPyZ_Dq68j398T7ZbUvLEijS0KlPmLqrT0ZsDod_l65G3iLcRa52N6gpZNJJwA4X0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAAnbVn5CYat7riS7GyhlBE8dbnY0xiiFj2FYbnULa6NrOu5EZClliKpLjGrdtUWF2XM1WqYxnsbVARwIIRBSJYvOUm3oEcaL_bIOSy6wiA0vSfwGS-YRj-F4MX1qHnnYr86DdrlIPVOiWo4D96t1sXLCRP0agc3wGSlnY9iePgM_ng_3NaX7zDepBxB_mbkZaaaN7wkNE10k8WprM1uOvvPEzGU9m8I90jHXtRQYYY5mq7ELVUUliLKQ_TGnZmQWPpKb2Gc3Dy8tG4WuNlzpIRIf4xHcNf9Mx-4rRzIf1Wa1deoxGzC5j6EcLtDvDktKVxegrnqLEH2oqMaVVR0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvp1_ybid5ntdb_tNTsrJDVU06H3m5JWyfkPMiV6hnpaajjmyVbNMLih3vVgw9RDs5YBeuJataDr9gBly5OQ8C4U8IeK8atPunB24baOKGtG9XfEywGAWh7FItAjcJHbGHswz51IOOhw-V6Iy1FRaECC1mOndOj0omokflsqnqp2rIBuUUfb3TMjbG6jD8IkN_45c3U-E9Q8-_f9G8cNhFU-IBriH22zuz3KnuoF3zq_6OJLz7AIiFqXSCknr0IEadbPEkkbQXCjwb8puMrp_8J9pQ3UNrL2NigdjbmmO5jn4OUyH3lsR6IZvFRz6lThL1SGsIdxWk7w2atJsh66UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA0qla-NcYeK_lpatcEbtEOKMuX8BmWqZzDjcMS-4L65QdUjNI2CsDNJhiP8SOJkOgKzJ91Ae3W4WYJr1BsQt0zNUgS2LW7yt_rUtAaqBGr0QyxkG1cbCPHVQOpEd19sadcXMM4SEpEu7tIfFkaVlWO8Uasjjf46tV9G3yUKp3GMeBnoAl3MgFiruAg1Wz4HbuHcYBB7z_kJVcICJ4opvvujk70IzEdTC4Z33roOnf0LwNHr4sDNAZMmU6ruGdGyPvrbnMXuI3NFboCLrkDAplKyxf0xXmKF-4XDPvYw-q6htukTuBtQL-Uwu5e6_nq-MyhsgtV0ukjwa3btEYDJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XNJnl9-uh9SQseAS5zmusEKT4hbhR2fGLgi3TKEf0X4-6GHAD9ZU1jlRoBAX3ntAHvCbyHKOBnbeJzA_SEGxLvDLqy6HdrXMgsM5B78JMolY2ueZ9bM7rkzEZq6ewJnW9QlcponXEkBqIUQfh7_tIgbcabcsWXisR5QiKdxFrKOLHx9dZOgKjlOpqn4Sjjl5FCc_zuNTmqw9ly1qU9ETY14ZpNuhXSvBu0nCP8OKUt4FGir4uGL49y45ujgSziJtzHLGtx3y_NNc7BvHClONBz-44mP7XFG60fT2YMzt1PEmWm75VCk4DquO74WS-nD7XdPAqM8qn8xZ6Z4P9zcd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XNJnl9-uh9SQseAS5zmusEKT4hbhR2fGLgi3TKEf0X4-6GHAD9ZU1jlRoBAX3ntAHvCbyHKOBnbeJzA_SEGxLvDLqy6HdrXMgsM5B78JMolY2ueZ9bM7rkzEZq6ewJnW9QlcponXEkBqIUQfh7_tIgbcabcsWXisR5QiKdxFrKOLHx9dZOgKjlOpqn4Sjjl5FCc_zuNTmqw9ly1qU9ETY14ZpNuhXSvBu0nCP8OKUt4FGir4uGL49y45ujgSziJtzHLGtx3y_NNc7BvHClONBz-44mP7XFG60fT2YMzt1PEmWm75VCk4DquO74WS-nD7XdPAqM8qn8xZ6Z4P9zcd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms2Cc74Xqn0N0_o1yA3zK14_ZBdZyA7LMx36UO4BGuFqL4cAHSLto_Erbd4vO16GcaARFCrAmHewLcEK4_Gl1mE5SDuhLQTqC_9-XTXwtt6V_u9Rqgpf6r-1BF6LzemMpLdNKU6a53No9S-7clUNKpSZ3gPxFELzcjWf7g1JyY9r6FdkaerBYxEmozalr02QvTFvR_B0n8-ZbPDO86yC6-1NVf-kx_u7pcMeR507uX2JkvdBpcHHi4k1lolNlggQ5VukRuqtBE8pPKtGtWVGfW4QPOOH33epTvluo1rEZlX-dr4lcw5cx49O52rlbY6fu3r6LkfjJ1_BszcUlnk9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=jlhh9Zy3J1N7OfVFhjPbYUwu9oc18FjYaFyjGXRoKj_WhlBbMEP0T5XN5oga_QGhIZKJtiKj-fd5AJgBJd7hdH-JIqHmCIGkNuPxO7Ww3TtC9P41YbRVpDLGm7ybeZQmsnzLOME3RbhEVOga37MxVZVH0UomLxOzc-Gpc_30wlbZVtRd936A6oaWJdjufE29Z4KFRYQ8_JniaK4lcsL2yVMgkZhT96TBGISM2q07r76rAzJr7M7yD5iLZJMEho6-ePJvj3VMSEt4aE-kLSijvBvksMr3wkmc5uFK_RHURAsnW_rqrvaB7mhgpxQkOvYK5k7NRtzbCYzG10BKqoIM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=jlhh9Zy3J1N7OfVFhjPbYUwu9oc18FjYaFyjGXRoKj_WhlBbMEP0T5XN5oga_QGhIZKJtiKj-fd5AJgBJd7hdH-JIqHmCIGkNuPxO7Ww3TtC9P41YbRVpDLGm7ybeZQmsnzLOME3RbhEVOga37MxVZVH0UomLxOzc-Gpc_30wlbZVtRd936A6oaWJdjufE29Z4KFRYQ8_JniaK4lcsL2yVMgkZhT96TBGISM2q07r76rAzJr7M7yD5iLZJMEho6-ePJvj3VMSEt4aE-kLSijvBvksMr3wkmc5uFK_RHURAsnW_rqrvaB7mhgpxQkOvYK5k7NRtzbCYzG10BKqoIM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkBR5YAhUlXqqDxGmsvJBTJB1SptZpgZyrusYvwLJZiHp5Ial1Hz8pThBlaOnhG25WR9ftn4PA_ejjlIqFyQUUjgmzaorO5wi6i33S-_ZNCtDvPqvCdQKtzgwO-aVubjbz_mDJ6_0sahqw2TBVOTc8mYjz5cByOotzOZsbVTWQp3EoyHM7jjiNo4jGgpi4pkSxUyxibvufua74mFhvWFHZPAN95abpGeZBNsoFvHhb1Qi90uQJ8CTjX6-tTLw5WDbOGPAB2uvR2KKzlEA3oPdRAjvs5ftjMAGkFvUBtG5of9kMB2rtxrkgfbKTEPmI5uOCl1m1DKwaIgZlDkRKcfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=nA18b5iJEyDmPru1m3iyzhCOKddhzfbHImUapfHzKsJG2qs-lO6ceMFYkZUV7j2hdDMmRjqiIgUEdPvFJ82WOQCCkUpm2RKMUOv88fKNMVRkkccV2wIxxUTvFSfQ3YXlJbrjtnAhKFaa-5XHkuZVXB3HQNIDx531LIb_YDWG8M_Sv3zLbbSOQxj_T2hD0BmxbXDfK4Y35BhHwlTc7Ixg20CadRhzU70UnLBZiPbFw4Yx-Vfob3tHOKuKHOhDn-5NE6S7V5jPLa3xx8D1IVTPHb7sQwJsAItPw3QNMJHAvUex6hAX8rBHCE3gVKLkScA5bZBHpYVAkOkGn978fzI7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=nA18b5iJEyDmPru1m3iyzhCOKddhzfbHImUapfHzKsJG2qs-lO6ceMFYkZUV7j2hdDMmRjqiIgUEdPvFJ82WOQCCkUpm2RKMUOv88fKNMVRkkccV2wIxxUTvFSfQ3YXlJbrjtnAhKFaa-5XHkuZVXB3HQNIDx531LIb_YDWG8M_Sv3zLbbSOQxj_T2hD0BmxbXDfK4Y35BhHwlTc7Ixg20CadRhzU70UnLBZiPbFw4Yx-Vfob3tHOKuKHOhDn-5NE6S7V5jPLa3xx8D1IVTPHb7sQwJsAItPw3QNMJHAvUex6hAX8rBHCE3gVKLkScA5bZBHpYVAkOkGn978fzI7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=owa9Aw51Uv9gSpf0qFAOMXMQgKi8ZuXGDUAGKJuJ4CE2RA0ISib08zzz5DialPe89OPB7QeCmlLCN-mjOXHNI7dF4wDWTr-ZbExl98mSPE_U84bkc8ciJq0XUjEItK68pssCd2LNo1QtVheZ4p3L7eBmciMvip0QmwJE8_0PmGbq1anoMusNl6J3ZSEuDwbl07EoXYj6I3bR9bE6-wW8qvMn_a95-JX_mn2O3TCxVDwp6nmE84dQuB16fl5VhS8Xcz09AfGLpY4mf30xPW-4-x1N8y5MwGyH2qzXx5Lat5GEh2AKLRvx36YbykmcfdTSzbg6FJ-5C3yxR3Za6rpYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=owa9Aw51Uv9gSpf0qFAOMXMQgKi8ZuXGDUAGKJuJ4CE2RA0ISib08zzz5DialPe89OPB7QeCmlLCN-mjOXHNI7dF4wDWTr-ZbExl98mSPE_U84bkc8ciJq0XUjEItK68pssCd2LNo1QtVheZ4p3L7eBmciMvip0QmwJE8_0PmGbq1anoMusNl6J3ZSEuDwbl07EoXYj6I3bR9bE6-wW8qvMn_a95-JX_mn2O3TCxVDwp6nmE84dQuB16fl5VhS8Xcz09AfGLpY4mf30xPW-4-x1N8y5MwGyH2qzXx5Lat5GEh2AKLRvx36YbykmcfdTSzbg6FJ-5C3yxR3Za6rpYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgIBbmDLTWgzoHcPb-XJQGzi3s_FlHg1gAJrp5GmWGsE55w9dZiLkg7pUoUZiGGC4g8sL-MLkQyKEFZyZrOEJJMmJD9cb2pvMYTLFBZ1hCvAS-HsAu_0b19mCU_PcgPVgN8gd2gRHN-szjZWj3JTXE64lLtNkV9wnwq5LhpEgOIWPs9ToGILBQ9bEOn_nQPfzjb5gtFdGaa8GftCcRNWRL4B4c0JpdPd99AiS1X-6yKoCpzNLP-ZqNrxMKFr_hyuK2SZwTj85WzhQg1A9dmNUbjnYrdamtxzdCHcPmM8Ky2e3lXj88dv9S7lxsGLY2ODYCZoWZy9ZWGD7CxvtYU_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBx_FGq26Jfe1T6sAcjlWCFTa9lNpjF18sudkaySe95qt9I2l-OSYoZowxRAOlST_5vI1K-juf4hHZeEM57cNC2JfTH92rMdFKqjV2HWn-oIvevUTFk257-K95HzwL4JiL53MlMOWSCGBMXRRU82DyQkMNTWq0mCEZ8i1FBxpoVSA87rJaMFz1dwbRh1jBFIniE02FbFbpBv0E1XJqkAh3vlQbnVm6O4tOGKvH4d6yR592oSCXEiatf5ogIrvbFf1A_kMOa-md4UM-PP8jaJ6FU_cryd0ZWzJTmPLN7cZlkGrNS87ttPT9vcR9VWWJ93JOjbasyoYLbC8hKBbfWYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJN-OdaEA1qXboGjiz0X9IlCZkoqBFmxVuL0mSfyGT7li-aQ7fci_P13FTb-k8GJtF4bg2vGdTx4d1jITBX9ckdnBb6XSGuARKrb2EGJwRaPGKUZkY5b85TBBKnnY997YFdPu4xgUOIsc5QdCLI1tVH0WYx30sSySJzC4Bpz1drV-sFv5MrPe0I4T-wKUtmGjCu8-XjwQeublcYlordbiaOYg1GwdgrBzLBSUoaNtBErCnlpQsu4WqJIvEyBI7GdcBIoaK712TuNc5Iemjs-rVB8JryIu_Mx4i5_v8qQwbUcVivqQnvo49SrivI11KEI6lRZBvO2RmmzcL2GR6cElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvmmQtpYq9z7DWwrZR7FNW15F-lvKgY731HDCaUWSHi5X3q7rKfoWyGuAkiX4p5xkk53gBAWhr0nxG8VJ1YYQj74WJwmlALFGLWupNIuSvqGY-4UDU7uCEZkj7ksNJ5G2LRw8arKQOvJonOKUFZ-578VhtNmMsQNleo7gPzzw8VLkkDxwxwQ1kZHuX7Z77Mi_-uzBAr41Leov941n79sFiwprDvUuicOfn_3ZOy7yfI2nKalDrLKPFehON9-pmbG7ZAF9Gc-_BJegcJNyDEhLByMfIHpBOgrA6yScy6ziKb08zRHgocj0NTH-MdhlFoz3leF1bnWMaC-4nUaeR1spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=bsM1yEsrhc7d_BmcUPULqYCD0rOZGmVq6SMVLALxPjWf_xlV_2xQbxEP3f7jtDxRDOM-NTIj2DaK2g_mVbE78MyQWWN8uSpZukDoFxDb-RU4xy5qsuBvI1my3jMeg3TG504HJXKzMQ17cFpvj00TCsFe67ZHgFQUgLmBMLfgUD6b6GATGiHM4S6qLWiLDKtdiU11P45RPMqTVmZ23CztXzWKoNlbkBCnClvQc4ATqHk3tCuhw5oCVA3QXxRkvOdj6ueFlgqOj_ug_dsSXUgSyEWAWK9LPaE2Ps39EGCZymgLgJFl7I8lSvKyMrXZcuc_rDVapSIvlDMlGzRmuQy4tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=bsM1yEsrhc7d_BmcUPULqYCD0rOZGmVq6SMVLALxPjWf_xlV_2xQbxEP3f7jtDxRDOM-NTIj2DaK2g_mVbE78MyQWWN8uSpZukDoFxDb-RU4xy5qsuBvI1my3jMeg3TG504HJXKzMQ17cFpvj00TCsFe67ZHgFQUgLmBMLfgUD6b6GATGiHM4S6qLWiLDKtdiU11P45RPMqTVmZ23CztXzWKoNlbkBCnClvQc4ATqHk3tCuhw5oCVA3QXxRkvOdj6ueFlgqOj_ug_dsSXUgSyEWAWK9LPaE2Ps39EGCZymgLgJFl7I8lSvKyMrXZcuc_rDVapSIvlDMlGzRmuQy4tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=ejvpprFVo42brV5hbWBOcKI6m1d3Bm0s-yeVlGMo90kaZYnvDrQWTBfNvuUwCv0acVezKcoBurk8PRLpHPvXiTTrhVlWU5Tc5u2chfxJmgeCbCbVfmB_WDxkVmJ26r2mGRuzfYjeb7B70b9FGYdHZc7ETnb-X72ei_2B6FVyY6-EMd_Td8MQrL_Vzin-4BgRfD0c_j2C6Mvf4albJKrNobc4kcjgkMN0cui_pk0mYWour3ISvnMwfT1Bif01l9x6azYHezz6I6dX_f6_7_TMKmF9DJfUhw4YPrp6L2f5Z0raAllTM5uNGsWzCNaLDC8J2pXr2hgjcpcSYfKwP6U7fTe-3rTn_lMlMggWj1AYtXtjC-uiVAOM-ZSSH9o_R0llQMGE0j7jeMbCWiDwXgJFJw9raSWlmAXAMxG-DQFzRfmVYSDUpBccCk74dgu0kcNyCadMxCYs6ImENWXoJ5416RkhRha8BbKSy2oMolAxEsYgzxtTpqVmTY0Amfaz03ia-k4T6jFxQ6PZqZ7XjFr8JJb1lNFkwY2WEakmz1zVoHiLMUKTYF2ZY6gDPCVm822vQmizkcHBnQwm_tF2nhAinBoELaH4n3sHVB-arvYRuUyn9jF3AyZw_nlINDbY6oscI7acyciVISg2lTJg-8YdGLoOwne_s2kR5wTm_4IORpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=ejvpprFVo42brV5hbWBOcKI6m1d3Bm0s-yeVlGMo90kaZYnvDrQWTBfNvuUwCv0acVezKcoBurk8PRLpHPvXiTTrhVlWU5Tc5u2chfxJmgeCbCbVfmB_WDxkVmJ26r2mGRuzfYjeb7B70b9FGYdHZc7ETnb-X72ei_2B6FVyY6-EMd_Td8MQrL_Vzin-4BgRfD0c_j2C6Mvf4albJKrNobc4kcjgkMN0cui_pk0mYWour3ISvnMwfT1Bif01l9x6azYHezz6I6dX_f6_7_TMKmF9DJfUhw4YPrp6L2f5Z0raAllTM5uNGsWzCNaLDC8J2pXr2hgjcpcSYfKwP6U7fTe-3rTn_lMlMggWj1AYtXtjC-uiVAOM-ZSSH9o_R0llQMGE0j7jeMbCWiDwXgJFJw9raSWlmAXAMxG-DQFzRfmVYSDUpBccCk74dgu0kcNyCadMxCYs6ImENWXoJ5416RkhRha8BbKSy2oMolAxEsYgzxtTpqVmTY0Amfaz03ia-k4T6jFxQ6PZqZ7XjFr8JJb1lNFkwY2WEakmz1zVoHiLMUKTYF2ZY6gDPCVm822vQmizkcHBnQwm_tF2nhAinBoELaH4n3sHVB-arvYRuUyn9jF3AyZw_nlINDbY6oscI7acyciVISg2lTJg-8YdGLoOwne_s2kR5wTm_4IORpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsVbZFEo2-OVrACZtVcOgoWTzK7p5ngTE8LZtqi-x26PbDScqeNm0_F9QkHDjvfMO9bgaKhMOcv4hf2GtHPzZnyaFZfsq-vzWBBpGxvNzmlsahRiX_u34bz4S6m3ZL-oCU0KFTfzJm3o6nYS0YUeKJwGA1G2DjUVqU5mY9SZNZHXuv8Sc_ZIbSRvNw3SLkflvWuPpT7K_ikzWsECv1MwapiiuiNQRm676RRR1KETr5qpXNbt9nBLvX9l7WTmgvs69f5Dr8rc8NuNTiENNyFm-o82NoJMtqJWQh3G9aCRlXyRwDMiLLpONlgECwGlOu5CcANr7oE5_cgsi5CwmqbbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDiXLXS5XDRC1szPO_ttRmZB7O0ppL5O1BlGVJHK0b5W2Hkt_vOEWwGC6f94aeFmPkEWYrp0EIPCNrSqBKb8n8r38s39l_OTmRkI88MsX2-yib7EFGlYWyVCNgCPgnLcHEWBMibTfe_Ld0lyw5y6ZAUxsz5zLOMMfvfoJn16pJvywSmcP6VO47CwKiP9cHKuDSU2B-49pvQ0b2Dq6hkrWaiSDsw8YNQnAADvlE-lzw_8xptsUyxk-0UCCQHzqDVr921Dji4-6-sHaFwwbFtMR8mHMcdkldgcLtKZUSiyz63jbbXsJTizQWAzYKlZ4Qpuvbpkn1M4GbXtlMTGryMBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N74xdFDuIWxd-KEiVe-y1qtlrdZIJvoHs2HqmDkcoROWvtoV3iAR__uF01Br-4UA1osd-RY6EimWA--DIOcdWXAhO_pvxvQZdzIgG4WZeN848J81hWHwufgtbGHVQo11uukB5XOVG-k3Wn-dNUPVc7nEidbkaeR2D5zrarw7qJfNu3xNRnUMY17sHcD58TMSxlmM5Obuvart-fRp0m2bCba-aNntqHX6Lx3NPRUGgYRMJYiowZez5vw3GJqD2ZYxu5lBLlauoAZ7DPAtiBhF8bHYyFKLGoSph0AzKh12gOikhr4GTCHvdXLvw0f7sjuswpkby9dcWjNoUf1i4DY0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c26YPCbV7-MkpRUCbborUmS_FRgRHIMW80VL-caUrIRs9lvtvIHFaF-_45k5SbcEzGkRKNE5lLLNmCffswhiJ6UQNVNwmGO5Sb__fV4YU8PcW-MZR6c16mh9efyKnEA51Lul-jMfOJ5JHM95Yrq2jbm8fyD2rCX10y9miwkagQjfPVaQWcOAuFfu6u8CrcYi6MyU_KkUusQ-yeS-F20w4-IudxvcB5wWbWnL_mohAKkzEVmJ6z4YbgG3x9dW1wLKTrk2Q5nSF-sXS9hKhYfFPa88Bfqv1d8lT6oYldFTSkwlLzqmV4gld3BaOfvZd5pAgLqkvi1gwFjewWRGnouMwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdG5IpbSOGKAuh2ME1HY-RnCfz9qHSlpufjo-sU45Ro10GE9tcuERf6cXpjFKs7ClUXuXjnTw1uoIIiJQH36rFAeFQTm-3SbbmbozrrtzkDDIMbU51TUeq_Kv8tqTDKiP3kHGIrokJ9LLQtVtkEkdESkCl3PheOhuJx_XUfs8Wv7e3Yc8iHPF5IfLYCymPfXHgg48gA2J5FQzlPvLoMglOkE-EMlsJqz7PrrjJC7oOQfkwTYmLq-URGZ0Rid-WNIGUQq7EXL0zU3xWDJ5fbjTysbUHai9YBAwR9AQQD-JiPeaNfVSdtRi351gr4MEKVImoGKYWBgiq4z-7BMfbNY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=fIwfOJlPDPE62Lm3g0icOnZy2W7i_6ib5qfnLQOiPvmtEz5zYyJD7_dg7IJnYyT3mUv2EbjBCCSJVk1zw0ztgBmzhekPuq1slCMWBbV0yLRcGAOZGcE3iZ4OVJE9cuk0hUJOclPLJM1qhY9VOWp6Wsa0pbnciw5zV6aJK1OUTUvXig0SJHW-kTIj-cTXyarKlmp5zdwVSqp3tP-dqznHGuEgPSz9p7ZQNCS8akPgPT__1wUmg968JTdpLUHLS8E5FSJ0b6w8SdE0fYOohmpLfxj1h8JvnYSwaD-PDSKfOPKqvs7LPoKbu3i9XcizCGeAkIu8WhQiQ0KkXaMMDHxexVaeK83YVoZ8O4ZbaeVcvEuFdIaMMarKxw4u_jGSPkG6kvPGUEjMwTJDG4eyqMHpGY1D7wdTGp6KZwY6gc8vyWWo9Kk-zTssnHRGGWTnUCPR4nnI6ERMD954XDBxk4gabOG33eSSg3kdGqqWp-78cWxmq9k-ySgjJ59la978YA-QpDnXtyyjrdqrj7GwsAi0NeFcCzYqTi_Y_gFfoeyW7WBPUg22WWhMB2KxRA0Fa-_aUSsv1rW0IdBq-W8zUI4vl_qz9Ked-uBkceS4t2t9FhyqT5xYwlvLy0mcYCDLfJo3zMXtpTwwnfK0fMpS1syl5tegGy9apDl0t-UxDSIi8D0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=fIwfOJlPDPE62Lm3g0icOnZy2W7i_6ib5qfnLQOiPvmtEz5zYyJD7_dg7IJnYyT3mUv2EbjBCCSJVk1zw0ztgBmzhekPuq1slCMWBbV0yLRcGAOZGcE3iZ4OVJE9cuk0hUJOclPLJM1qhY9VOWp6Wsa0pbnciw5zV6aJK1OUTUvXig0SJHW-kTIj-cTXyarKlmp5zdwVSqp3tP-dqznHGuEgPSz9p7ZQNCS8akPgPT__1wUmg968JTdpLUHLS8E5FSJ0b6w8SdE0fYOohmpLfxj1h8JvnYSwaD-PDSKfOPKqvs7LPoKbu3i9XcizCGeAkIu8WhQiQ0KkXaMMDHxexVaeK83YVoZ8O4ZbaeVcvEuFdIaMMarKxw4u_jGSPkG6kvPGUEjMwTJDG4eyqMHpGY1D7wdTGp6KZwY6gc8vyWWo9Kk-zTssnHRGGWTnUCPR4nnI6ERMD954XDBxk4gabOG33eSSg3kdGqqWp-78cWxmq9k-ySgjJ59la978YA-QpDnXtyyjrdqrj7GwsAi0NeFcCzYqTi_Y_gFfoeyW7WBPUg22WWhMB2KxRA0Fa-_aUSsv1rW0IdBq-W8zUI4vl_qz9Ked-uBkceS4t2t9FhyqT5xYwlvLy0mcYCDLfJo3zMXtpTwwnfK0fMpS1syl5tegGy9apDl0t-UxDSIi8D0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzE2gSmaGd0fBkc_UvEDMy2oMMVWoMKeAdQh1MJCxoCMq3B2cAARhAtNrgz46JcxK0mfqhBHmY7UIHY9GBP7cM-Wc-ct4usskHyQ8PmWwm6EGrvfgb-d2Pa_wb-rWI5gntPah9TEOZjEPp2BGsF9IQsPOhmdP92hspYfjBsueZ6X6jnennXC-KvdyBaGgwI-2jTVtCdYqaoOuWqUV-ehEs1FJAEgbDJ3pHDqs8c9QbGtSOhk4nHHc9vJWlhG4dCw54knwP_L39DhTqStAFJs3hUB7UMIgpDtRqJConV5ojwYMzwzz6Ozx90S6CBaQfeHe5PYtpHkoN66tzgOhWCLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=Rco2s4xp6d7ygoZK8aNMqY_DhVeNRhjzkT8PqNWUkz5BNsuckz-J6aMfZ5FQKqUuF92kQMCx9ZLVttzDJO3RwHENTamNAfEkBhbBDbf47XChOKxQRyoAcIKvs2aVNz71f3x7vqP6b6lAnsd0RPhfoeTak8GKPvtIs_EZ-Tp82BrbKtEKt63H32N7Tf4YpVTFt5QEJcycDDNJC2wSyCvBbVLoN4YIXs7FsB-Y01bH230y5sLUag4O7fH70gNWHLDc0weQJsdQfG6jRF6e6QXCwyJJwicP6VrALZgxhxvS6vOM0w0PfWYRMDSJjYn4YVAWjjv6GGKBdYDFaB8faOG154i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=Rco2s4xp6d7ygoZK8aNMqY_DhVeNRhjzkT8PqNWUkz5BNsuckz-J6aMfZ5FQKqUuF92kQMCx9ZLVttzDJO3RwHENTamNAfEkBhbBDbf47XChOKxQRyoAcIKvs2aVNz71f3x7vqP6b6lAnsd0RPhfoeTak8GKPvtIs_EZ-Tp82BrbKtEKt63H32N7Tf4YpVTFt5QEJcycDDNJC2wSyCvBbVLoN4YIXs7FsB-Y01bH230y5sLUag4O7fH70gNWHLDc0weQJsdQfG6jRF6e6QXCwyJJwicP6VrALZgxhxvS6vOM0w0PfWYRMDSJjYn4YVAWjjv6GGKBdYDFaB8faOG154i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=OJwP79f5jZjeQKH4-_0KKGDkFxaY9lgVm7uqXgTCmELjx_t3jCkGuPOUalLeSlTXVv-zf4cYV5ab1kNgc8Vfz3xc5rLERfERioltMgM7OecW93yZe32MKooTgm2Q0aom9qSoqlHCKLGhLcyAv6ezdYmLJscUrS1xx4npVYTpbSk2SWq6Xi22cNhyA4U5z0i3q6fK7t_VBXZMBxppT4oX91qr0VL_UZsB6rNxGfwTU74SJEmuM1laLGtMypwEK4mCu0ugBSgp-lOxuhKL_jnA-6r0AJxc91R1HN7aHNFKH2q-1FbUfg5PqWGnmKuwFj8DBYn1khCbzkqTX1kCm0pJvR7Kg0mBcvG0ZfdXbXwQEqPPOpP7Rl5chpy6NCkCIWWOtNkr4onnle6cnGjmVsRyBy0oUrvIMDI_rie6ESegz-DnxdD3RLAJT0gDZTffme3MAZwDFMaFaH0bVOMqbOVpuyXDiuESRngjvHCXwkyangRHK9gt7gXp5Lwwh14Gut0Z3ry41yGED949lgYP05wxFUemrzUOGN5_qNNQVjg_5uJqifpLxbbJJy-GuEl1wjh9wSrxswOtswSmjxEsoUodEsOuY98ZZa5wMCz5nEIqEcavccPC5vSC3rzwCXlOSFI2mzn0B_6Y9WYpYJkNVDmrsEoBQWlTywyS1D5htSEaCm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=OJwP79f5jZjeQKH4-_0KKGDkFxaY9lgVm7uqXgTCmELjx_t3jCkGuPOUalLeSlTXVv-zf4cYV5ab1kNgc8Vfz3xc5rLERfERioltMgM7OecW93yZe32MKooTgm2Q0aom9qSoqlHCKLGhLcyAv6ezdYmLJscUrS1xx4npVYTpbSk2SWq6Xi22cNhyA4U5z0i3q6fK7t_VBXZMBxppT4oX91qr0VL_UZsB6rNxGfwTU74SJEmuM1laLGtMypwEK4mCu0ugBSgp-lOxuhKL_jnA-6r0AJxc91R1HN7aHNFKH2q-1FbUfg5PqWGnmKuwFj8DBYn1khCbzkqTX1kCm0pJvR7Kg0mBcvG0ZfdXbXwQEqPPOpP7Rl5chpy6NCkCIWWOtNkr4onnle6cnGjmVsRyBy0oUrvIMDI_rie6ESegz-DnxdD3RLAJT0gDZTffme3MAZwDFMaFaH0bVOMqbOVpuyXDiuESRngjvHCXwkyangRHK9gt7gXp5Lwwh14Gut0Z3ry41yGED949lgYP05wxFUemrzUOGN5_qNNQVjg_5uJqifpLxbbJJy-GuEl1wjh9wSrxswOtswSmjxEsoUodEsOuY98ZZa5wMCz5nEIqEcavccPC5vSC3rzwCXlOSFI2mzn0B_6Y9WYpYJkNVDmrsEoBQWlTywyS1D5htSEaCm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=clVncXIjy3zqi66j-lQfL-TDvgw50WjHHJ6q8NBaoXmuLbShRTZmIOOHVsTxUn6h1EP94eomZC-z7HG-JPC-Yk49FH63TWVGkJ9fqP_d88_enEt2JoNtIleKBT49z0SH3AAYx7KWE9knT426xf9HR9g9ph0lwPM2K6nUhPn1XqrzrvDTIlV6wrKgxGJDaSIh6PMY2olsP0hJGt6C1Ss3gJK19Wr3kuCTNHQabbh95pXzJXchw8epoUB6W8bs3kQcmvrHCMOVdzbTAtdc8TEPWF7ZAtHnTwYOXMZEOvbBNEWhrZvc4oqh7se2KwJUvQs9iN4_q8EGTvdhmJdhPFF1VYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=clVncXIjy3zqi66j-lQfL-TDvgw50WjHHJ6q8NBaoXmuLbShRTZmIOOHVsTxUn6h1EP94eomZC-z7HG-JPC-Yk49FH63TWVGkJ9fqP_d88_enEt2JoNtIleKBT49z0SH3AAYx7KWE9knT426xf9HR9g9ph0lwPM2K6nUhPn1XqrzrvDTIlV6wrKgxGJDaSIh6PMY2olsP0hJGt6C1Ss3gJK19Wr3kuCTNHQabbh95pXzJXchw8epoUB6W8bs3kQcmvrHCMOVdzbTAtdc8TEPWF7ZAtHnTwYOXMZEOvbBNEWhrZvc4oqh7se2KwJUvQs9iN4_q8EGTvdhmJdhPFF1VYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VioUGcI3mr-FYWfVpnt6_lTtqkoV48BXGKc_ODPtJtogy0K2IMxBjBuMiwOeHQizruilWVfmj3KP9Ku45dODXJJpHRJS7Bc_cWnPHL1htBGLdC_6cVXbB_4BklQ_8n7LujJmrp22dCYDz4gQnDfN3cx91X4ByXf8tXNFNO0PcHvwE8Z2NJepHuXom78v0qv0TDc4Vjf9DG1dKpObF_0EiJUWz_KpYe9-i0fucUDHxe5jgcIAfDCDx7hfIsk2nBaMJUejhdPnI-zlbDSsaD49TCtrXDWSrG57nNPVAzcqrZLmKdDXOz4yFUJF6Q6VQMjiwSHJpjiAth0DBDDM0XfWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9LI_W20AutVeRC2FmGLE_HM6rhs3cHmUumq4lXXL2ENYzHMljpG0UhtxgsgTZzCxqvDklo1c6QEMIiCkrO1yairJUD5YtkSKZIFifW38WsxKbv2bnNOKXAC5FnXUxvyRQyX0ufzrhs0Tu_mQtO6p5YsxmkyU5JnX4u3vV_F489LsM04kMnht6BHqNfww3QIZ0J8d7RQzlZuxf5oaMv9uCDkX4gMbEfZqARHvHWC_ZgFMNtJOYZlUtZtck2vc3JVF2Wl1NWNXj2-FVzyJPPpDBdxdomH2C1svDreGV6Sp_Kz0g_wKtx8IKkTKqPeM2yVYn8wh_O852_0IFPaiu13jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvxFpdZWq8Tlrs8SmwC10JZ6FHJrlI75f8aPSxz7VO20a6xeKhiWNxREzxoiWcdHEE2EyiWxKAlU6qytbSPDx1S5Qy4R-h0b6H85goKmt2qpIaUu1GGCWM4w1TzmyJlyE9jvj6zdcgeD4AsnuQcuFiVCKgJcJRI-NEIkahlsHZXq78n9aUQtyM_ePna82EYn6YXJRWuchTwXAmbd-naKN0QaHpfFRw3VRwpw7pgcex58zaA0gfN9FVp_tolp8ubiQxRmofEULvPzmcP-tvVd2eqOLhVD45nfZWCAw6UO8Ihl5yw61Shi0E-sAN-Zb1PQuj_NyhH6uA_D47PbJ9s-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml8Fvm6KfPAlTYOSEuS2nQDjVVEzHdTZ9FajEjFl73aQxf_HwaXD6GM55MaB6FPhn5TNvjdAq3pJhi3g4HoJhpFMV8LduCauVN5JmcWPSsoaAom-Vo005PiIt7d2D8lNi_wD4bRJ_GsUe1V054I8hA4i8JsKZ0hTrIVckiNdeRsMUneYTEkFZ-iOhryRCsgsZ7M8Lbqot0xl5G1L-eFsXvhJ00sIUAXfrcIjJ95nzxGn_fJg3hG-mz4TfKixiKTzyOC1p9n_bhJGHq-iiIRpaB-21YGH5cqb6Ciem9U6h-RhphdauMQv5cKfEASw4LCXFy76jnWFjqdLtpqLz4ks0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq-Cu3E09kJOh9uY9RjyDSJPOb7Z02HKDykt1GDF1GoGNmA3lTTOlyMi7681QT39Jf-pWqoGwEndcIkdM--bA4yLpyDacMEyfHrF6l1Ot0LQE4Y4UTrU5CO-TGVgOjx874lfg5Ib3vImE3O0ags4CRlKSCo08uWPvd7UzY80Q3nPVz3mlei5p64f_KjUjl0FtY29hRXh4rMDj9OeYdoot68hiMn63sZHOY3A4xQqLNXfaRGbEq_Z6XCeu2Xt0osoD2YZxj0rx8JvfLC1D7UbUsHerhzLpN17zJHswhXh5dYnpxhNDPHYsYM5Mo9eXF4byBHktKb-8wvbystaxuVl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=jAWkXUYaRoA1yH-vsXtUsVMozzutzQwUhcv8yVHgExj72RI16JeiHtxNtiN4YeywXAo2VXMGUDh1hU4ZPYx6wIhEIpaUkNkV5GC-msApMD4qAQMMjmBnJ8l0BqaNa2_ZQyARdBnF0DZwnvECp7CQXZJC8ncsUngXgJPBjat2pDrGk9-YYATj8SEDdaPjJKALxB_kCQ6N8vbP6YjT34iRcOAHQ4-o3RCGdPrxlqE0ESJRJyK0UfehwKhGPl4wzWZS-VdkoRQKJSKjMv-RHEgj943K8r6sPVAViSrn5OfKB7aaBjYTYKf_qNNzGjPWu_Qb68WDKOsqdgFKWHXNf9ViAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=jAWkXUYaRoA1yH-vsXtUsVMozzutzQwUhcv8yVHgExj72RI16JeiHtxNtiN4YeywXAo2VXMGUDh1hU4ZPYx6wIhEIpaUkNkV5GC-msApMD4qAQMMjmBnJ8l0BqaNa2_ZQyARdBnF0DZwnvECp7CQXZJC8ncsUngXgJPBjat2pDrGk9-YYATj8SEDdaPjJKALxB_kCQ6N8vbP6YjT34iRcOAHQ4-o3RCGdPrxlqE0ESJRJyK0UfehwKhGPl4wzWZS-VdkoRQKJSKjMv-RHEgj943K8r6sPVAViSrn5OfKB7aaBjYTYKf_qNNzGjPWu_Qb68WDKOsqdgFKWHXNf9ViAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlhtXv2PGmRo9yM2UBMzCFWw8-t46eDwTA3QdhiBunIgDh7grvOkt6TmaRtRiKa9wueIMxBjnRHfIE5ZLN7_ii3ynb89683OEbzGvwWpZhKQbNAHKUPg6XWK2FyBZFdWe6d_JYM4E_T-UAn_o3mAWDuQXfDn7SfItQr3Q6QaP3C-KQ6dgpJXsTHDWUxy_NVF2SYKAipMGGOW-2khS-4UaKkZs4obm1NqSjZPHw8fiBcA3rveOzdifKuXSlL8A7-E6bc8zAkrGPHwTKZrK87-2gz9LhybtymWuksywiRmNbv3oSpvreU-L_QCFa1LDdLQ3pBy5ylYALNax124cKPJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrkjoMLvGBBMRQvhBi7sSMVgHE3X3H5nV6m-ml5QUaoMKw9iJVOnlhHm-6DbDbpFFvSv5sgfVpwrOGIzDs97AyYHPqnscMgzETf4Tg1ofEahpkD-5KMg2jvbs7vpoqJQce2VkaRHiPXE6s_nyV4Hqs6ib5ZjVTIaaeRKp8NeEn-sk8Gb2nhtSZTNzU8esIMbJ98AWIAEMle3wPT9ak6F-_o2qsdXGkuc_TKqzpPM65SlXOpH4yehHwA0RO5-PbCfDTJO4gzsEXTd7OAoN5gwGT0ODFsW8AOMYC33tZ0Wuc_ZF60CBM9cG2_4GzcpDnx6F4X2c_pNfO5VD-8b4j0vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNGGTX1zHA_Vm4X1e2KaMeS_-q7b8ub8R-F5Okohwz_fTz0NDSmOyHF_hzhBYKSD1ZDE5bGIc8VHpBzdkEwhCroDmhAw_Z7vTJ9XDkqJvIh-E4qq3h7TPv7I6T730aINFG99R2z74pn7tYvnit1r3jz3ANboVa0Fb4V22S07cTTaeu-x5BoplS-NKCMLB8jPkOidIfn-12NrY3KU_vhEKTCNRcLJ-xjimu-VvDaxHBkJ_y_1YC7tU4W9OfDzUPgRRpzNNVIuRPFrhS3jMmMOunIJ9oiUTD-aqN9fNcklY_TsQy87WPAFOgjZ44Rd5o87rZr45VLe7tVpZmcorS-0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqd8fNXm4AcNonLP0xtdNDrtwzhB1B_PZocMbjW3HjzRy6YbtXWOoQ7jTt0BvN5ytfM1DgHOJZPpoDaoiltLojNrOJphHiJQKBS4FxDyv3D9Y4aRLsasnPtEPb-URGp_hQ7oKWNbr--Quxe4HVVs5cBarQ3i2FUn61Wn9O3juNWzWAalfKNLMumU8dh1Lz-6TjYBuu_0qegYAcQl95lADmFVHGJD_pdeXIEXd5LvpB1y76wRUEK9PPdbXIHlcnZJHrd3OPHZvuH-c6elFYvxw_WAFStI9tDyXA1023dLilbFfKQ8_848clHIbkEnAZ3PdAQI2wYtn4c9_dtJqdTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWoo7YUIhGEa7tsgwf_ztXC_JCE-lUvtvodyTLg9HaiO8v1FwStLt81sFZQMl3v9fh_agk1fb8YR2dv7EeWZGvYhX1OtS9BLuQlqgLc3EVqWGDCayFNsHMoijBkIj7fCRlDs5azXSs5tQ81s0I2MlyCQBZ0R7An2GklZ8RMItKeaR1YZEuYm5cdUxD4XsGgWKzF6QgU70xeCldGCZHo4vJDFCsmuHmNurmYYjwHYbMVYzwV14rBmJveCaK9g3bhJ212O2lXMacalsxZ_Mv62s3Ei5Jwmbv224Yq7E2-0dN2BYmU4GNdP_RGZ-XpuVTeom0to8RTFURV1XSZo1Jw1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn5cpE71zIWSDBH2KXqTSv-Bc35TZuuWmg8BLOCG6eMzH_vaHB8K-WROzMzS2y3aHtjd1WoFLDnHVf93OZbgNq7hKQaXZw_tl_7EgrMWt2bUQQbn2vyHjao6CJzVhCEzdxcdp0gR4oC9TPiV1tMoCicKmTw0fdbgLjb7PTNCvLFOmtHXBWHPsa5nn94dW_FzXgpNAagHVQCgex0THTWmkaHrsFD-1Cpzs4VFv6RtNVP5XrgdCFn6BiuNbR42X_F714xyBZ6AofkVYH6Kt9kxihBPJpo3i_Svq_G6Lgi00f3U89G8L-3RRSMSvhA70IfLy3hQdlVKtNUsjA0k25uCVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
