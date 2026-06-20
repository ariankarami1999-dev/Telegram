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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 21:22:25</div>
<hr>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbITLjdkx_DVx6bJXnd3yGjyTADU_TcT7UQwugSreL_yCntP3fuse-pjyjq5Jo9WIdJTKFGIIH98rOyOi8-Ghwbx4zHPjx3r86uFaSRn-mABub0oQoPgoJIBWAozexjEhGJ3Ew7MlDD3YD5eX1D9a_hizvDqNeHHEGqFVEzk6sHS7zHnRwkiNYySFqfgFVLswUtlC3U8J8g4YJKv9AbGJqu-urbOeGS3oQitvOulF20s22DBJKIqahMQXcY3FIbqAIQcYkEmQ5Ix55jDqTc7QhTPbvWM1lzCGTnN5VYrRr7Of6Z7GGwSPkzqlr4xkw_JpfI6siLvMxoKGK6BHcARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nas3tovWomn-FAMyso71GqdoDDIQPqwR6C7kZj3ns7BpdNNjcof6kF7Wrzum1-4-EzKujOhtoI5tM1tF26eugEY0wrbEPr0DyGW_GVXVNRzgYwP6cgMKTTNZU0_DbB-8Qex8CKf8gZxN1xaWV9YACIMtr1cfZYaRcxs2V6V1EMzUaKQhg5xQUjgYNRwMhGeJuQIjD1FZCRZ-7915lYNrRq4HpVGqzkrlJ2BQUfpyQlnIMDJNwitWH4j2PR0zE_6FFJrInNnpZWSIXwUGlmoWt_7rBAhkXaTIPsW8R-Kz4Zepvwt7lREgHThCvGGss84u1UUd3ZTY_AncAXJg0XjQMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=F8eOyhdUg0lbVWEb0yJlqnhofTvfPbiaVBJOXgZSnwHJZohNCdVg5QggnL_659fJISIEEYIV0nemNTSdB4tZGtRmLOeF5CGlLR5v9dM5OXIerPSC8tVnIzhprSHENq_GpaxMkNuyWwpsXMJr1FSh0bn_3Nkx6Ijb6epo1fY6bhbqNhYIXzFcDaUg63gCyn73mpa_7XLxccnUNNtyWMSgyX696oqFk7Rs6vIG_cDR3lWTlA9hbnLWxeHdKQeHESw0PTZ4UMffVx2VGg6usMUyFqyxdmkeAYmBJmbenmoNGXrf4ztOmsIooXUkuxf0KefiJWkVZZFZTqLn1hEdMDE1Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=F8eOyhdUg0lbVWEb0yJlqnhofTvfPbiaVBJOXgZSnwHJZohNCdVg5QggnL_659fJISIEEYIV0nemNTSdB4tZGtRmLOeF5CGlLR5v9dM5OXIerPSC8tVnIzhprSHENq_GpaxMkNuyWwpsXMJr1FSh0bn_3Nkx6Ijb6epo1fY6bhbqNhYIXzFcDaUg63gCyn73mpa_7XLxccnUNNtyWMSgyX696oqFk7Rs6vIG_cDR3lWTlA9hbnLWxeHdKQeHESw0PTZ4UMffVx2VGg6usMUyFqyxdmkeAYmBJmbenmoNGXrf4ztOmsIooXUkuxf0KefiJWkVZZFZTqLn1hEdMDE1Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_PF19z_Wc-nBTz66N5hrq45nZQN4HjIJTvIcdAcx4fhlKbWDpTTJwsHbkpyv2_Di6CWA6cg1pOR12_l8U2Bm91fb2vzY0ErujPmGUwTs7av4noQDVbmd-SmqVnCQd3XmqSjBripsnnZnataIFxNuyC365yYCpmENA1oMWEM3gqay513TLXg40p6QNFj7R16Yr0YDxiEG2Fc3rsLEzhdbFMevCBlb0jqKGnMC_DldSsvKmfoKgKsMsx5awBnvzlzaMMnrrSy4t4PmbjbWYRAkioDaIHiab7-CyFyybucoJHu-JtA6Q-XpZJYAxUmdauFQyCVh9sM6WV7FMH7BLy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCky_KPctwQaiqZUONhx5pUbQI7fMH23rwbG4uHOb2Msn3WiV8nUihVt8rdOrhx46CquMVU5hnaq6F1KKr5Ce6q3Q89GIn7FsIrMEpncpnHDUpCOY01Jzwy0UN6Qn3LyY-PPGuPlvZjgkRPwwG-QqV9gHISwDEzTC1bGC5yljBpqm12mUr698xwC6MMkceOkv9NGEmm0yhsAxlpAzGNKCK-5_PO_JhvXON0RN-h9A7gfxLHiviTFHpNqEOiSYKIyLQdBVRYSFhPSqV9E5MUtgK5PzrnwTZ0mzWXlckO3zw5AN2bXaEFdlf0ANmyvN3Fd2N4reB4W3MdaJ5fFmdW8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtcEZq8Xh6tAQx5DQ7_ZfV9cOp8L0kzKC79xmtviYumimxOAlWLe7Pmxb9tLJz_XQ0jFBuQnd-GaCwb5k8zKlArsiVzvWHbKFy_ehtLjB_CklymLq81CzuroCuhshgCM4VxUy5hj9zFYmqULEZHrcASKwD9uTKWz8bJwZ5w_vUIuzXq4YHUk0PlyaxAdGJ1EBtg8wbcgB5qaeDJqWysBpQ4cyQv6w9ih0xJsdDXK0mtoyy29kSv8u8LWpQ9seCpQ6DcxHwyVWFkB519ZW3Gt8GQvJeRizVwYyuINS5QFM7N1gGEo4fKfEUYTFjyVh1IDegRLnxK21PqpWzJIkEDbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGomyDpPAwo1UyNP9O_E4xmVOdCpWe7DhnCZdWp9EooUBmVxTl3WVq-JyFcDRt2mAuWPDKKtOS_Ah90eAp0b2IAyEJkmCYdY_kcBLZ12aZ_8Fc1eSVjLKc_VfSJCheVCOETK6HXzq_iDrLmWJ2lE0a_ngaRa2la2Cg3lMaZavroJTCqbtEyCQ6PBPfVSVT2DT87rzAROq-GNQGbun1Wwm6pApfM5yKxCBZ0HvAabOuPTxw_h1aPwppVAnvlz8zYztwUMVJrN6TJXLoXCeBl1zv9nPCDptuotDtWfjVtNrT1THlq7DZgbkxhOlhetDddD_i0_Kl9FN9Pp36TDtSErtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu83dMZRyisEthGg8zycNAYR9hKxZGtmjCrruQaTM_-vMwEB_BbV3ekugPnUQTLsi_y--Fc2H-sxKlxGcCaTPHOgo3obWJvXgohzPFhFmB5pP6bs3hkxXyckXoDY2ppUveUtXeOgwijqMOau3U0g9kI_pt3vBWI-8x8sr227-vimrcMoDysS-Qlu-Cpcz_AEenoq7Xre-Lb3NjRzeHgpkvxVWSl4Gy2jYZ3BZ0CyHpEC5ztlRYYnu8rrS2l1UI81LVsorBDQuFuK-KxnHqq3ptJM4i2o3n5bgV7xhPD0kNg4WlB5QJmee6grNcG95ieQX2MHRgwMK6NBAv12Qry6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=u3RE04RXV8tg-mf_-lgYfE7YkGWdGvVBOkFbFF7oz2dyP9ZmK7KhD0zvamttqFYTBU-bRI95kBpxtVPDLv2VStrVnEGxcxOmY1Wp4oR5JC-tfdAgjcP6-BJpGmQ_5b1Wf-g8pXaIhje3_8upBM3GKXbg8y5TkrsI7awVWjKm2gHgAihTARWAwUDrwHPG2AbvpKA4M5XpllrrRJdZaDns7Vy6IXIFQXzcfvxWHDiYUfUb4jE4CKZ7JaRigmsI9t64-WDXYFtbsArjBbca8G1sA-BKir2VGzil7aP3r-YtHsI_ieUZHdgfsiJ61wVeAH3VQjWPsrw7Yg6t98sc7DQj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=u3RE04RXV8tg-mf_-lgYfE7YkGWdGvVBOkFbFF7oz2dyP9ZmK7KhD0zvamttqFYTBU-bRI95kBpxtVPDLv2VStrVnEGxcxOmY1Wp4oR5JC-tfdAgjcP6-BJpGmQ_5b1Wf-g8pXaIhje3_8upBM3GKXbg8y5TkrsI7awVWjKm2gHgAihTARWAwUDrwHPG2AbvpKA4M5XpllrrRJdZaDns7Vy6IXIFQXzcfvxWHDiYUfUb4jE4CKZ7JaRigmsI9t64-WDXYFtbsArjBbca8G1sA-BKir2VGzil7aP3r-YtHsI_ieUZHdgfsiJ61wVeAH3VQjWPsrw7Yg6t98sc7DQj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=WAVNJb4DdT157ovddA4pszhxdjMAwkc81eMkkeDrpgytwgqxb28ixwH6gjs9-BHSWX24mD9Au-3tX4WljfAKZulEbueNv4yy7Iz4-zJHmx6py26NEH0Nl-kRTrg8DkFzdyR0AHMJzrXiub3sbeo_lOxxlDTVun2jse42GEo6n5fFUdADpJFTd9SeReeP5ZOoIdsGgf0A5I2p2s0KaHh3FT3S9ThUtzEAoLCpXNEnmbzQ4cRWvB4_5Haj217dMReJOPKCSRZKjc3HjJ8zEWor9wgFO_rKhX8ype0BKJtw5AtR-dxq2fdsNPvqiTndw3CXCjrtMuJCc6QUK9h1YOPm0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=WAVNJb4DdT157ovddA4pszhxdjMAwkc81eMkkeDrpgytwgqxb28ixwH6gjs9-BHSWX24mD9Au-3tX4WljfAKZulEbueNv4yy7Iz4-zJHmx6py26NEH0Nl-kRTrg8DkFzdyR0AHMJzrXiub3sbeo_lOxxlDTVun2jse42GEo6n5fFUdADpJFTd9SeReeP5ZOoIdsGgf0A5I2p2s0KaHh3FT3S9ThUtzEAoLCpXNEnmbzQ4cRWvB4_5Haj217dMReJOPKCSRZKjc3HjJ8zEWor9wgFO_rKhX8ype0BKJtw5AtR-dxq2fdsNPvqiTndw3CXCjrtMuJCc6QUK9h1YOPm0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mauclhFMSZjPso97qRu0Wb8dIzhqJ6FMBnGFzvshitGoIRrz_yuMviZlE7TkwIIUlHP1W590v_Y7vdOMIkSp830_4nfehNfxWcFxrly1CkDwNMRVv_Ho88WRlJ3CDsVDtk-XqQzbQirgbJN4hKpElqEUQGQ5VqEID1ygZpZUfQaw5hbrctIsdUVm-W0PLEq84NZNhEIrV-6jN0LBt7k71pbtsLDxfhwtKq0W-DmVUQ8rtV6-2-kqRD0PkgIOKWsSIJq5qyto2uizSPgJ02fvrK8REWCZi0QydfvZrd4QvzbSGnEGsWb6IPZiWmNdN0xmf5lEdI2Gym0tdg35wst-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpm783EnfBkGyrUcGBAAz6wwIkFBYtSdJxs4lC5iH3-4e0k7Pn40ID_J_YS0vWGczdntupgPJMeJLi1AHROmrJf6qpLXJa4Bs9vUt4KfscpsyGEoIA7sdlzB-vLvo-to14s7nSR55YQ2MfHgwGDjqqulybUG-kCXlMT3yi7jPwNaxLzR-Wz5r1kNaefn9R0-mp44cr4_VAneXFt8fvx03EsvVw-Bhxw218CjXiExZ0YpfEjCWELK-CcVhg8li3oqyObn53V4oE0ZCt47D4Rq0rvITtG4vrPQNg4PzVQyW8Y4dYu7WnJUWMRWqjtbM2tirQ4lmv85TaNs0ac4VfFQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=A0mLOYzKMZBpKySfmorLZ3N9r-NQrzW-uB6_YNSxWhquJ-b-HHxwmlBK-1vwrQqxSbdojojyq2dlXUaxCpdkSypXAMktYP446rkBrO35iQminMKi3zrbCkSNUAUa5XXX1ldvxlb5-K0B3KZLBUMRJ9BAXlnxy4VEKMsN4sZaMBUYoZOE-iEoKNENEZE-kvyQpsuZ_3XUCw4xuXBTo_07DwHWRE4U6BQg6yjpRwoe6SA1blTjoL6I9IOsOPoUJdiDTrjKIv36FjAlW5XiMA5ouwhXN-NvyykOqY-eOFpqBa-vlyvv98NiNEXjslwK2Z9uYmY7WVDV3UOk-3Lrg0h6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=A0mLOYzKMZBpKySfmorLZ3N9r-NQrzW-uB6_YNSxWhquJ-b-HHxwmlBK-1vwrQqxSbdojojyq2dlXUaxCpdkSypXAMktYP446rkBrO35iQminMKi3zrbCkSNUAUa5XXX1ldvxlb5-K0B3KZLBUMRJ9BAXlnxy4VEKMsN4sZaMBUYoZOE-iEoKNENEZE-kvyQpsuZ_3XUCw4xuXBTo_07DwHWRE4U6BQg6yjpRwoe6SA1blTjoL6I9IOsOPoUJdiDTrjKIv36FjAlW5XiMA5ouwhXN-NvyykOqY-eOFpqBa-vlyvv98NiNEXjslwK2Z9uYmY7WVDV3UOk-3Lrg0h6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5Y8z_FQ3upKlK941vmmP93OShl7AZJjieAYAh9Vas2QvtZsfceIIDmeSQbuKcJbLMnOdK5WaA5kCnWz9dJ12Y84bnwTr19lnShgkQCOAXQxJHydve8PZYDmY06r6svlUS8TcDdzU-t_Orcv8yKoMu0LFTjmJdrGwNH5LtzDkj64vG5ZE4T7HUnxVFS3kz7M8WQQsXPUrpSfIU1Srmg6JlrasrSKs3seZN0IElbRtKf2oPX1aXZcAOTbKoWh8AbzypSH-kfkFpP35FYSsqH5gFTKf2rn6vuPQCcOLhkpGsZfV8Ejl9ZIj9AJM7LTEcjPEbb5VkFzQT1a1S837oYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=I-HFBDleIuAYFswSHZb9RqxPLgCgpqyRv06kjKMOx8l0OTry7DD-Ck1NXf5xu0ZyNmY09LdeC4pr6Vk5xlseNTo5q6zJ7q22JDpPNy25IRX8G9Y3CCgNWGDbMcU2PDrpOPIHsV7pAKEiRDpNDKEpZd1TJZ6FjObx6hW8NvJFqez1UaZSxJPiiVEX0NIH1XygVxe6R0rgnSBXbgw2ZHG-c2rFEENmD2i3FU_1ydhZJO_P3uZWY2Vj9PbWpBEz7mGaDUMqLnuabn7fNapjpfLSijFJyNxigGaymqTFcyyBSyBMVSDlJojbeXo_x1FMZ8Zf-uYPl5rPz__JyBd392SOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=I-HFBDleIuAYFswSHZb9RqxPLgCgpqyRv06kjKMOx8l0OTry7DD-Ck1NXf5xu0ZyNmY09LdeC4pr6Vk5xlseNTo5q6zJ7q22JDpPNy25IRX8G9Y3CCgNWGDbMcU2PDrpOPIHsV7pAKEiRDpNDKEpZd1TJZ6FjObx6hW8NvJFqez1UaZSxJPiiVEX0NIH1XygVxe6R0rgnSBXbgw2ZHG-c2rFEENmD2i3FU_1ydhZJO_P3uZWY2Vj9PbWpBEz7mGaDUMqLnuabn7fNapjpfLSijFJyNxigGaymqTFcyyBSyBMVSDlJojbeXo_x1FMZ8Zf-uYPl5rPz__JyBd392SOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYN389qYljR9qDtKkl0MaBVHu95o1oJOLiO9K9Qnqi-HMn58Y19srcgAk10epFkmnvFXT_TsUTv_n9FvhZQBjzA18kErcyZ9Hk2dAqZw5MVkd51roP9wB0nTdMtFhBHU83Nh_ApYI39pgNkMXk1ODV8VPXHn6WxrBs08U9GDP8emugI-TB-LXYJ-4atnGWLK8U5d2HrqKv8NgOGUwS8D31OrPfNb6ojDgDD7n1bj-aWfLHC2WYSzfboP-HXc9mNrBE08ZZUEejDWKfzUL3WONwi_pNpqHxsP_qh1e1HS2HzOQ5zmReWaw8UGOkEApHdmV-Xq7e4X7J6d8Y6rFGu_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN0apv8irFCYHmP7g40GLjdvOOvmOK-H9uubh3d_oA9wr59CF-FFCd8aLFN5E4yl3nMhcnPFFsZ7b20Q7uzpXlPebIrBJR-DKAHD4IWDfesIsPIBT4W6f73aHcl1tOnPJKE7bW6XtDWmtjjzLp12Hnc2CzKj6mBCxJe7Z_yIFq3XJIH1L-lqhw0SC_eRl4otaY5IjMMT-bm67h9XnWrPKk8T4EROlUBnIvJ-WY4Svw9kpgikV95TU1SqycWMhudF-18F-XQGTMuN0ljsWlwbGz1GP3RfVOJno1Sq_Kx8uSTwbDrbIhh7TFdv99Kj0PDTcmEQLu-twVZRseJAk2ikDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DcfgPCO4L2sUIGi_R5_HfMYAjUeFYqbCw3GDFifjQ5UjbNo4KWkg1fr7Sudax5q0j7byH1uGyQOBqeOV5TgZPzctPJQW4CYRshtqZMFoUW_aDFOc4SzIxadVnEihHokUWVitUaYTC9PBZCVdEElKc_lyhQkH4unqJR7pwykTadsaqaL3pj7TO6szsfgolFFKJl6ZioWVzIog1ABgtVlHtXANkwwerZq-etqMdUIeaDTOkLnHpl0D0gKJHR64_o5GDAEpOWRtwYDSleOyyzSqz-jNwoIsVDLYCfc7VpZOBX0F0HtTPgbEDGzrCgHoyAkG9VfHfsLZjZ9gowRj3fA17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DcfgPCO4L2sUIGi_R5_HfMYAjUeFYqbCw3GDFifjQ5UjbNo4KWkg1fr7Sudax5q0j7byH1uGyQOBqeOV5TgZPzctPJQW4CYRshtqZMFoUW_aDFOc4SzIxadVnEihHokUWVitUaYTC9PBZCVdEElKc_lyhQkH4unqJR7pwykTadsaqaL3pj7TO6szsfgolFFKJl6ZioWVzIog1ABgtVlHtXANkwwerZq-etqMdUIeaDTOkLnHpl0D0gKJHR64_o5GDAEpOWRtwYDSleOyyzSqz-jNwoIsVDLYCfc7VpZOBX0F0HtTPgbEDGzrCgHoyAkG9VfHfsLZjZ9gowRj3fA17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=aR27suJ9gtencuT-F8a6v2o6npAYTsMdJ-bw0tJ75RCLUqkmyaiR4x05mqKujzT5N-le9pnvMXnTapZQaLyGVsIg7jIilstmffgSlU8kA82SbL49IBK6Do0G8ISwQ47DPs6gMsYAr8sBEMVbci6fJvvaXWEE7kQhc3Xk_n0lRh5C-jqFd7zL_CNkOdqAjykHe2pGfkNQuD6lhzCHx0pNCaQGA0j5HxP9EdYbDmivNkFyL_auwndMw5lkcvNg2YLkpcCUhtnJfkvUSk_NX8J0GiIhCQ7sOXip9Zx48vIf6wSLWIJpVvWAGOznCBSBWsGfdLryXOuVt0fdiIOyeLo-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=aR27suJ9gtencuT-F8a6v2o6npAYTsMdJ-bw0tJ75RCLUqkmyaiR4x05mqKujzT5N-le9pnvMXnTapZQaLyGVsIg7jIilstmffgSlU8kA82SbL49IBK6Do0G8ISwQ47DPs6gMsYAr8sBEMVbci6fJvvaXWEE7kQhc3Xk_n0lRh5C-jqFd7zL_CNkOdqAjykHe2pGfkNQuD6lhzCHx0pNCaQGA0j5HxP9EdYbDmivNkFyL_auwndMw5lkcvNg2YLkpcCUhtnJfkvUSk_NX8J0GiIhCQ7sOXip9Zx48vIf6wSLWIJpVvWAGOznCBSBWsGfdLryXOuVt0fdiIOyeLo-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozKf5qb57GWdJ_4O1FwR2U-fFBF4QyxHTlD7Z685QtSvaWDy0rB3RoeFyV0eAmt4lt_kb6RiWvDQJF66bmZiRUUpe95VQXtIC9CAka5wfXk5JK7n6a96a9LAgaMhJ6H0klMq-CPKYxrZvgebYC-BDRrFs5lu8oUuvCpUrebOwNKVgsUHT-7m_5-AWfthIQgAlmWLjxxuhU5YbtfaI5UACk0kNDlTayv27TuIeYGXqt84_e03C3h3T9wN0boxzUZA8pUGbodCYj0eubVDOUiN6sHNTg8giSzaSSQwnpnAfcx2opbIovczkvdGPZlQObAJFz8prEtqKu5m0ZYpVBMitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAxSgVR5P1H7XeeY4NIJ9AP84BWuY_YsyEGHyeKGIRpNjghTMwMkhN8wIydp035xVBxL4ZUArlqfh78tOYeczN5DeYbmZTtRvjPJ8I1xre4iy7OGuD4JJ0KDoib63Uy2MlXEmYsaYOSO_oAmC3hj08DeeR9mCVkTzgbIAu9ZRnowwvDZCw0jQADgNJmn22XDh_i3zdRZv_p-mlOtvWY_CFNCIZ0jnGtfLskTo8ZOZc6EpTqgQaNKbWYEyEtdaxiIyKPr3lqoRQOl27V7lbtQBM1qNsWh2CMIVUiYbr08g_ltwlgMmAjtvSx2wv0wm4DEgvWcN7A83qjMVlWM1faHWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6xH7PdwxisTdCxyXhzHrf3PjQqTq-UtcPrOcfBbnM5peHTol9ZfpJvwDxwcLsCEMyax4xbYhy0vtL7QJRq9zpTXumCZEAHWv5hhC_eSOVaHtxDL_jY3g34y-HBjFtj-Km1HRYO2ZoOnAXXNzFNmSty8uFOd9NkRrNrTOwaz85NGac1--UP3IVS1jDj-PaYJB6O3b5pUwyX8ZOYuIClXTzxBYfxLa3Xnh4nUpmJ-rrbeo30KFCNY5QWZUmdY9eaHb9IRuehNo_BxMyHBXTBEaL4Oham1UBO_cJyrYDyeLqgMgCBNUM65tDZPPrL2QWIvW3FlEhCEYnoLQmkm2xFx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=tx_9UL3IXppqMIu51HTExzOpHOvre_gUOO8ed8LvKn5mH0_bFHDHyo228Q4wV6-_fBeskTijFUOFrwMWMcxmYAQzQADTEE0nP2XLN5AzjLSPAAPU8qxdD5b6Gnata0aQe4WkZCbGXJZ4TNQhCXBnRFhmUgfm2HBf2ErqEwLlzoH9fYb7yEqd65zG1GK5Vyg8xGVxG1pGRQ2cbIqQPql8VybADrCBVIgEXkqnUJkxZMqyzlN8nedz-ZNwv_HA5aM7VCwBS77zIR6fJheBnxUHYqCV-zIon7M1cKCDLXA_z5kUn5bUQTH0yzWNGNjCjjhGB-0mfO4Orm3FaBL0FB9vlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=tx_9UL3IXppqMIu51HTExzOpHOvre_gUOO8ed8LvKn5mH0_bFHDHyo228Q4wV6-_fBeskTijFUOFrwMWMcxmYAQzQADTEE0nP2XLN5AzjLSPAAPU8qxdD5b6Gnata0aQe4WkZCbGXJZ4TNQhCXBnRFhmUgfm2HBf2ErqEwLlzoH9fYb7yEqd65zG1GK5Vyg8xGVxG1pGRQ2cbIqQPql8VybADrCBVIgEXkqnUJkxZMqyzlN8nedz-ZNwv_HA5aM7VCwBS77zIR6fJheBnxUHYqCV-zIon7M1cKCDLXA_z5kUn5bUQTH0yzWNGNjCjjhGB-0mfO4Orm3FaBL0FB9vlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyT4V7n2VfytK_SPcBgnTGuoT0p3Pbky9x1SfPFxAjCabFSIUre7uJ4t-8Gggr7Y7d4Yz7xAgSBzsQL5eCPGF6vvC3Kx4KUKER1wlBTkR5wIFsPR24WabuYouDRwVhdWtAgLOtql8-m1AB4UDYw-T3WFElBKhXEneBvTVA4QuFmusc7QWawFSvY1vaJLjB1jtkfKnv25tqGyr8NZ3C8fqxWGE3dOeLTo2sUX7QHaCk3c7AgkgEqOYTwFc_-Ga8SRjfepXezhaY3IZSSnumaPKzJmtvPn6_iTkFpBrnRKJNUK1N4tX8m-g1sag0I86iusaBDme_GSBDjnw1AaeiRw0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCNHJfDjdOJlWLdMfvLVKgSHlafTY8OMl5mB4IoHl2_MVMIAmb_sVXPf_YSK0LcRo25sAhmVnYJxXWtitjGEZwFbKwTE-hyExKS6_YXIh6TtB9pk7JwfLxPmsei4b2vHofrifYKCEhZjzr5cc_9RLTubWqLZbRwZdVTcC8ZCpD4Ot99DZ6d5Qlc71rD1zY8qyNMHnitROEUn_ALy9GTI6PAmRdBATmr5zSmHSfhPBeHyoa5uP5O6x3wv--8jnJ2EjJdKI5Mb5IdfBj8Ka_F7LT-MkLh2_43h5lxG1A2HhMYc1uD0FGY_yVghwPgzibllDwbWkfVPobj3YhHkwkGdRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOAY-d1MdhnUskjY0YK8jHTDkfMl3M0oamWRDyZCYZTtDPNm1EdHmIywVIkr3WfOgCTU5yqECKPDFkqii3JVIGQZurSlpiYsQpoNrRpqPU4cj6wI6vTGeH0cPu-7rBBFgY9J-U_P58O8RtW-ErpAudEC12VaGzPLnD5VQ7RMInbUhxU3jwxeePC3FgSuP4vb_8Q1iQSM1SI3GZavNy8enK284BWaucvdi3E9Srn3We_DNHj5Td6QCx5sbAenBaRTErPI0UtyagLApwcOKeOhaMtcTaISDER8kUN5e_3IvWUsh3d2PVyG-boDwVZbXJv0Y9U8qGi86QeQUxiPZFkErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no7nVfXOPMz6PWJl8EdY2omh9RjKFgvSXO6E6gplIdS3qicWKd3ovKVVk5zzGJmgoQlz7FR6Y_lGqU_Q_6EGf-S3ns1jxH64SCDnGQSs3zxczdGxa8po2UVbqhzeKg0g3Q8a5POz_igv6tfYtasNntAd6Bzz_2s5H9GZV3gZEwC6kb8UqD5G3qlCZyH6ZPMeE15jTKfn9c9S7bb8SqpgXQMnwSBn2vd5Y_17TljGT_9Gox3E52dBQCICDmBy1oJrNvDPl20NfaTMSnGy5cWE9LizdIx_rfe0AjPcPw7JAtMfrF2n-iRYxqD36KKJv_VheJAV4O5cnVSQGZGQ_rXxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=cKRdLU5pkEFltx1t7Mm6IkM0crSPIV6sNZcNskEURPSrX2gBSiU5GO2nqf6iFiqroLXbPxoaLRq9eemkdidwG9dlwDWtGLZL6gCkdxtyEkT5W_OBAje4fImv6l5SijGPDvEuMbOM-egfYGh_S4JPZJ81evhijH15GMqOpM1X1T_uxxfR86_mbRizDvXp5YOpcqtHut3BO4IfFian2r_867YhAKX4K5I9eo4VLbUp8rKaKSeblYzcJQ_KKfIzFiLpKiRfRkyqz9VUB538IbhnEbgExkZH70txDeVltoBIHwpfUQFgLEjZBR4DIgFarukKDBixc45crH7OmBI5KNk7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=cKRdLU5pkEFltx1t7Mm6IkM0crSPIV6sNZcNskEURPSrX2gBSiU5GO2nqf6iFiqroLXbPxoaLRq9eemkdidwG9dlwDWtGLZL6gCkdxtyEkT5W_OBAje4fImv6l5SijGPDvEuMbOM-egfYGh_S4JPZJ81evhijH15GMqOpM1X1T_uxxfR86_mbRizDvXp5YOpcqtHut3BO4IfFian2r_867YhAKX4K5I9eo4VLbUp8rKaKSeblYzcJQ_KKfIzFiLpKiRfRkyqz9VUB538IbhnEbgExkZH70txDeVltoBIHwpfUQFgLEjZBR4DIgFarukKDBixc45crH7OmBI5KNk7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_PIUgbpjAPQaP8lGnk-7QnAW6Lv_S2RkBUYOPsytwjgk5dpKddHr-_IfXF-4LdKrXg7PFw2WC9IjNSOqarc4rbeRPmcDxMBtm_tVlNp1ua4Hj2VqCLF8II4OuEUmvroW12DkiQ6XNXBcSvcglUoahjhS5vrcpnpBbcFQcH7_bbaPDxr62QzYJCCGW4MREYwYg12xUJ5KfUzeCid3YXP2wySu7Jwq51RNfAOEWnEW9pIGqARgrnZp-osbDtULfLFVb2OZLEJhxQe7eDom8lfzB12nGlia5K8aEKC0AlNZe7IMQAg9J35t-AfHepX6SWRlpgnMGCSFyq2SWT6qgkv9A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=FVWKnXLwxFajQEJ6N6uvPz5HtkUZ6x_LgQio2YiuhHsGuJ9Lx-qCJL-59ZTxEzRN7gx-Cp7x2zH55J7SWAA4NDNaLBCPzNO870jb5oI2mxYVKMxzMQvwPuv9xGYk038rzyOyrgMKe61vAaQ7dfCvzN7RK4T_GCUqwfayEnzdMQYS-fFDvtBR5Y9UuZvWdp8ipGm43DpMDJrDqzPxXYob9eSoBfQfcPM7I_OJQcYUp55Kc_HZDtD8lQU-pefNbSlUOfUHEc4gigKG8hwg0VDIbigiuMgVfWIqolN7ZC7hXyFRK4EUTQ4zjzP-VtA9sP2utron5AVmOoFdlTD2-preJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=FVWKnXLwxFajQEJ6N6uvPz5HtkUZ6x_LgQio2YiuhHsGuJ9Lx-qCJL-59ZTxEzRN7gx-Cp7x2zH55J7SWAA4NDNaLBCPzNO870jb5oI2mxYVKMxzMQvwPuv9xGYk038rzyOyrgMKe61vAaQ7dfCvzN7RK4T_GCUqwfayEnzdMQYS-fFDvtBR5Y9UuZvWdp8ipGm43DpMDJrDqzPxXYob9eSoBfQfcPM7I_OJQcYUp55Kc_HZDtD8lQU-pefNbSlUOfUHEc4gigKG8hwg0VDIbigiuMgVfWIqolN7ZC7hXyFRK4EUTQ4zjzP-VtA9sP2utron5AVmOoFdlTD2-preJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY5OZzqDyxuOyt_48cJJN9FVY7Z_jIh8rHfV5A2vKNJbBxtZVb2WA_D9DblC23L8MI_OEPPtTStBGILQA9c3KKTBM2xttVGANHXB1mYVgbEzx-CDnIMjmubzHVZYpQdSLEheox9MqPfwC0Nr-IeQ5ASCDEXTeM8mqWR9huHk2TR5bvxH7aLrOs6a8OtADo6KDZvRb9RVN33pD_6u5OBViyGC2BQPjtQrCfkINI8DBL6E7Op98MMY20BYTdafH79cpPyXUYABpfnBBxxMHBlGJa_SybgIIqW6DoklmR0OOkjTmP53tjf-xdbTVuBy2d7Fcmmb5EmjOXKBH4rEms5wgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=nQk2lK3GISB3ZcKn-rcC2w9N6n_J_H_XJWyHgKCYqSF58gQszN1_fWL2GvYs5_e3c4bP23Xqj4dbLFHVdyGUbUHMagETgD1xdDEw411oPSZkZpEftHiENWIDt2s2bvMtaIdPlZ-RNPiCN8Q1chSHmNcKieU3pfBNTgz2pAB-b_mjYRTJzVDn1cXA1eKsHSHA20HjFXx3JmNM6p4N1hp71nzkhM8vneKskJEA2rVp3AxuSji6D8CVP7Aua7vnSUjkQGfsmtXSlVFz3D6PJWQzoqkHRZ_MDplM9BFGN6J5cBqkAAkEVDiCJaaQ_eiGqkHUcZSIT8m-gsrBRZe_IDBiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=nQk2lK3GISB3ZcKn-rcC2w9N6n_J_H_XJWyHgKCYqSF58gQszN1_fWL2GvYs5_e3c4bP23Xqj4dbLFHVdyGUbUHMagETgD1xdDEw411oPSZkZpEftHiENWIDt2s2bvMtaIdPlZ-RNPiCN8Q1chSHmNcKieU3pfBNTgz2pAB-b_mjYRTJzVDn1cXA1eKsHSHA20HjFXx3JmNM6p4N1hp71nzkhM8vneKskJEA2rVp3AxuSji6D8CVP7Aua7vnSUjkQGfsmtXSlVFz3D6PJWQzoqkHRZ_MDplM9BFGN6J5cBqkAAkEVDiCJaaQ_eiGqkHUcZSIT8m-gsrBRZe_IDBiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Sn-xGPMBGS-pjK8otLmLN1D_eHnvUxOybrjP0Gk7S81OkX74tiHnBhuRkjCZ0eipaMpykELZ8PAP4KGtNfjhOXmFamGNHgLFbGi4rji9f02xvTyu9Ohcr289d6wpDZ7BSC7duEj97ChSY-J-u1PQJmE5lCv7vufbgiLkei8kYlNw_6Ofu7eSn2ErcONFYDZfyn3CNHbXBlUgNw5tnvBxTWUUk6xRLiTxt22m3yXzvpzajcsy0JHsKte6Tafz3Ruu8xkDP5HKhv8PPNo_Z-OXTFE0ez_RAK1vtUUwykRlV_nZgE2qYtf2xqWJqX7f0I-0Mw4pnSilkm0qK4Wud7wfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Sn-xGPMBGS-pjK8otLmLN1D_eHnvUxOybrjP0Gk7S81OkX74tiHnBhuRkjCZ0eipaMpykELZ8PAP4KGtNfjhOXmFamGNHgLFbGi4rji9f02xvTyu9Ohcr289d6wpDZ7BSC7duEj97ChSY-J-u1PQJmE5lCv7vufbgiLkei8kYlNw_6Ofu7eSn2ErcONFYDZfyn3CNHbXBlUgNw5tnvBxTWUUk6xRLiTxt22m3yXzvpzajcsy0JHsKte6Tafz3Ruu8xkDP5HKhv8PPNo_Z-OXTFE0ez_RAK1vtUUwykRlV_nZgE2qYtf2xqWJqX7f0I-0Mw4pnSilkm0qK4Wud7wfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iii6R9WJ6Au8xmDFN8wGjNENLUe5ytxZ4fksE7OHTJnwVla_QwPKnz8EDevupOpKlCf4AGHbRM9fEihcGaadFvq4x_wasCt5jYe4HbQA_oYlAi3kZJcIIlT9GXncIpDLc0cpzrFvN_DuD9xfauszQYhv7Z65QEP17qjg2hrMjKa9xEv04YLeWy8oKRdsZJdIkbyas3U9BLYlRnotQodEL3hQG0SHgJEVr4bjYwYiTizUM3blQJcGDIiEOlIS5tY9uAqsO7bQU0iquAWZCAWu1h-5AlRVdxx5F664Uod6CSzufehPZmfYJez9eXXzcvnnD19PlfZClzYqs3ed18zk7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_kdGfcfTfSN5uqZoEoPAaoic3GH5cp8rA8p22F4glrtGhr_JBaV6JZEq3uE71Jm9AOJc8-N3WbjcJURtbOqGhiEHa02FLjLNgM_CRsQIdvC6BvjhzXBCb38Fhvmr7YQaCA2ocoQjLIFPNgs7FeGbPfYI0evNyxPvxC6vGed45ApeA3T_bT44MACr5B_WX0JOVBm4aSgqgiHAv_89dPawl-YoUVBI0WdSFMrcvnzXKJPvXLfzIGrdzLp31vIO1yEis538ztc9O2FqCoBjw0Y-0eHuuDcAH3Uogad27qVYhssfw7bM6aj3x5jks7nfC2D7rpw-1XI0ZcwV9eqBpgerA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNepHWiBIDjeNFv1xDHr1yBgVh4VYQtTCTbrbsVXfUZoicZmvCRj_CewzTQsNqgvAHnSwpcgqnwX5YrCxon7MOUaI7z7WQJhbCDgMw0hDjQgNYoZjU0EvDXeGajYRP3U7O0M1Tu318e5Qb3qYEOMYTGvuwZCPtCgKlSdOUeEkk8oi6Tdc_idMtzJY1z8Re2rgPYeemLvb61hhw8-O9oPqh9e4YRItY9W2YNtUVtLUH1qBStiAtV9XdFQ6s9WqDF8lLBBPA4YgS3iDkV_jgqnl6aVN0HzsVZfIaXqJXapVn90oug8d6-XuF5-Qod67IBeZtydoiM78QAADlxcvoDBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G239bEKVIzqsgp0aU1-iDA6ZBI8YzJqB5QFF7X9uaY9w3dQHJAxXKuzTn5Ii65awQ6h4022mQxzM86oDXKPK3KZeavT8egSLg51VJgBoNJ-jqINfDF6VSBYjzohXmEK5BG62RM4SqksMSg0-XgsIm11NJIVGMH4l4bv85Zik824NZN6ydV9hVeVurdk_x5CHFZ__y5kEs_dQ2_lwETzI9bTC-XvlPny-EQ0hrtTw7jzNleH7o4kyjfJx2YBIZLMkdV9Ej-y_UC-g4FAgASVnXu0EnMqqjDC9JXyftqhBKhPvYxh-3BFxB9g02d3-oMPSJ1OWmp6LeBkTqhGar1tVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=GVnycF3vy5r-f8JVsyw3bU8-gacKd2HyMVOZ_dxZIpMr_v9Fy6nr05qxPd2EDyMjk1Attf9BGep5ue50CLFdT1yukWYfisDGvhiRrl5Xp_bD1E2mgWpZKP1EdnOi1z6QiBJ_1AM-C2m8uPnhl2uzK9OC7SKasLuI9NQCDTl-lshZeUcV9NG1wBhbVh7EoHFhiuHQ-7sfjVJ2EAkmwwrRJ1tmNf1xXRxmwCdllethrx3PEoYHMlKEvaAU2p9gT70F0GphcZJHOTWR8ALAOnOVXs8vCmmLflA-0jp4uzK4GHp9bMkxhHbTUlI2PJdlXQbLNEaTxlsedgNBNsCY8bUCrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=GVnycF3vy5r-f8JVsyw3bU8-gacKd2HyMVOZ_dxZIpMr_v9Fy6nr05qxPd2EDyMjk1Attf9BGep5ue50CLFdT1yukWYfisDGvhiRrl5Xp_bD1E2mgWpZKP1EdnOi1z6QiBJ_1AM-C2m8uPnhl2uzK9OC7SKasLuI9NQCDTl-lshZeUcV9NG1wBhbVh7EoHFhiuHQ-7sfjVJ2EAkmwwrRJ1tmNf1xXRxmwCdllethrx3PEoYHMlKEvaAU2p9gT70F0GphcZJHOTWR8ALAOnOVXs8vCmmLflA-0jp4uzK4GHp9bMkxhHbTUlI2PJdlXQbLNEaTxlsedgNBNsCY8bUCrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftao_lmkRWkCBSXhvqgFlFtJCl2BhGEA5z1JE0gcviBsoJ_vmigihi7jeILjLK7SbxSRpRgHJwDrGZi86J_PGcge7sDC-A3ZXyRROwpaH2kw9tBbpKGg5bnCUl_c9RR9fZT_AcDI-EuV0BIAxzJ14q9BwOvDKvmciqPq3VnLA4cBLPBqtii0JIIEGrjj6sRmqS0ZckUlAKJKmP85EDD_kmgsg6B8GJpSOYPzABVY3SqGjnIMmw3tRDN3B3UHQxeOUQM4sJaAZkYjythF7VFcbK-VRzlQc2MF2w8nNmDnEi2ef0gp-Ijuap8BH1cmYViwHWGIiVGBf2_ZMESa83CHmdcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftao_lmkRWkCBSXhvqgFlFtJCl2BhGEA5z1JE0gcviBsoJ_vmigihi7jeILjLK7SbxSRpRgHJwDrGZi86J_PGcge7sDC-A3ZXyRROwpaH2kw9tBbpKGg5bnCUl_c9RR9fZT_AcDI-EuV0BIAxzJ14q9BwOvDKvmciqPq3VnLA4cBLPBqtii0JIIEGrjj6sRmqS0ZckUlAKJKmP85EDD_kmgsg6B8GJpSOYPzABVY3SqGjnIMmw3tRDN3B3UHQxeOUQM4sJaAZkYjythF7VFcbK-VRzlQc2MF2w8nNmDnEi2ef0gp-Ijuap8BH1cmYViwHWGIiVGBf2_ZMESa83CHmdcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsvfQqtKXCUU2wZtoC0OExBm-F8fQ0U-hCBRFAL6MHk4sRMknVrt-hOF3PXhww_sqBmfKG9AIxLkg_tIGdi8WvQs6nzVzd5PTgv6LpKf2pRF6EEBz85RXedGeuu7gN6ha3ijz_aNbHRZlYQQgtvos-GeAD5o3W4CdzZZfQMpWFVhNw7ezX2cp4TYdYZnQ60niK66lXQ8H8queiJwXPvbK9vM3KJLkPtWGQe9Hz_91-0BuAtSdjEtAwSlzRONA73CfgOzXMolqsx8rOGRepQfbAmn-VjKGhXcukzmizjBB0EbSsRC12Ja3QNNGPFjpEdQnVjNB8kmVYYjb0kJQgYkBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kchuG3_vnjWuVrfL_mZ6qPwqwVuWilrts8-WJ9Vtnnm1qpsPnaLmRxFqRuZ9mkNMd9svAJvoOYfyCVBdZhzDp2djw-yX05J5Rpvr91XJxLiL1CGqDzBdC4MGP-vgX5W_Xf4w1ykXGAgdwhLOau0seKk5cnfaMwgVye6cK2XB3Z-hsP4aasKcXMEP2jK3B2QsLpTwlr1GB_KJ1ZVoD-OxFlCzMj3Qwv6th5xUQcYfQRuyjM3elftWdu9ppqDipHw6eQ7CnMmnsk8rhHC3HUrpejMRAG5kimrslxpkuXyr8rvvjNlb6TZqgcmjHLqWokiMtZ4FOrkKk7xDXnV1ks4uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K24ThtPnsUWLAA9XbDqj38G19n3vExfI9UvVTOfnuKtvOtUcw2EOaoFHicprvezbxi-xjdJILZchPLNlvFwvyUB6whGhcnObpx6Q7KNXgDRMFM-Q0yOGs5JZJmqoVhN512XAOf85LbiUqQlcI1TgePhvU6NPV__MyTng8ZU7vCyeVSD9vTJCORg1_2lklrWZwtdOlrb5696LW0if_0464fLEVAWzI_K9WVTiOGlyQmy8TGDTjeG3N_9wpWqruMajkxXarDOCd5kZG_X-fbZFPEs6xtmYaPYp678p22qwMRxJVUtV6dLY_9FAjwLJXLQ4ZhEOpu61DPzw-VCo0DDhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlgBxgzU4rKbWxTA287Ujgb8-ZJhRwY5cPBuvNIMBR048lnvAhu0htHyNhP_BRPgiFIKS65-qN137MxrpKyKNpFPq673_15RP3xmOthJYaIq3cXdyD-EeQ-0PaX7LSwO1wA1QFSGvTQ4sqU92ADvK8drfrwBjx2J37yC3s-nI9ZdMjq5RoFJMzFEzA4EKLerHIXkARHvPHDosN65bpBm-UZE9XEsjk6wurJvmKi50w0rW3fdn9HHf1JLQID0lxYU1R0h93mcDUHD4wT-SY9iMTAz0CEpNYADRAwRr0o9Z4E7BCYuRCvKdPGM-Reb4xPyfsQkeRdsQdAt1rVL1ua-nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz8B0Do9DSN45xh5JEiunCskoOA1_6-anHyQGJmiHqs8UvrEEu6vpkwhFBRLzDYnc4I78V8as9u6My91fPuPPRFPp2Vn3RcFQCOr9cYn3Y8gMPYXJg-UhJfntEQfkeppZ4psZXcBDnz6EeCWu9h1-iRm6q5of3TNuU1JKyG6DxNbL0ON3guuEZAwL3rILnwI2dxzWWbEUw4WREUntnILoxjsf7KqlOp33s2E5AjwuHVEqxdWCjlbjC68jHbM3SPKYr7h6ty9l3z93zYmbwkjE2zHvc2DvZu73kSpaKV9wN3ZeW-PanVZNejcA3hp4l_DTTnZtSkiSLBiwN2B9mDtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=ekfK9_9M_NPW8kyQsOp0n5gksTp3sYAuGPNi9nkHF6wyO32jcH-oEWjlEaDYj6s_Ic875VJOdb0QHzCnZETGASoX7Bvx3ekgt6NR2t-kb9oZDsFYuQxS2CkMvwgEjXygxYLdCbJo_EIN5kaRYotHPSQbokG4Qqgm4KzLI-8AKERWpGE8koM6fiN_aMQXDKLlnvnb4KAYJ0WVa-ujcFs6N6FkZ-3lbyLlZjXXr6ICDu0Yz-1_Re4TtSwotjd3u7-6RiyfC4FEJWhFb-z4YKmXMcW2l01Vc2-XP-_u_NesmMb3-aXiXHx8XR-8lq9T6Z8pDBsAG-jTdjSb8FIWiXa12Yzqr9fsGpmdokv6As9z_TSY0t_DoLHar5Q3lMwZxzEwO8lvmfzXIZdUKV97cKAHayrW1lQR7NgBX587RGT5gVEAg9aqkWTQZNZRlNVqmUyn0pLBshgmjyLCk0OEDosIkxbJZFlWNuHD6YsgztdSWV3YKWtf-UptrvZ1iKXSlK26Sgy1VvRlBVT8LgqJcikoCwnhbskEIfqiXtv_wZDgcreCPELMi6tIZkaQO-D3qOaIoIlFpkFVzT2wejITCrpl6zZLdNagvR38CmBrFXSMT16Lm_R95Skz_53rvSzsgY9HsaB0X9Vp3FWl49GXEArC8UgGh6W6YxcZ0GpVDqYN7t0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=ekfK9_9M_NPW8kyQsOp0n5gksTp3sYAuGPNi9nkHF6wyO32jcH-oEWjlEaDYj6s_Ic875VJOdb0QHzCnZETGASoX7Bvx3ekgt6NR2t-kb9oZDsFYuQxS2CkMvwgEjXygxYLdCbJo_EIN5kaRYotHPSQbokG4Qqgm4KzLI-8AKERWpGE8koM6fiN_aMQXDKLlnvnb4KAYJ0WVa-ujcFs6N6FkZ-3lbyLlZjXXr6ICDu0Yz-1_Re4TtSwotjd3u7-6RiyfC4FEJWhFb-z4YKmXMcW2l01Vc2-XP-_u_NesmMb3-aXiXHx8XR-8lq9T6Z8pDBsAG-jTdjSb8FIWiXa12Yzqr9fsGpmdokv6As9z_TSY0t_DoLHar5Q3lMwZxzEwO8lvmfzXIZdUKV97cKAHayrW1lQR7NgBX587RGT5gVEAg9aqkWTQZNZRlNVqmUyn0pLBshgmjyLCk0OEDosIkxbJZFlWNuHD6YsgztdSWV3YKWtf-UptrvZ1iKXSlK26Sgy1VvRlBVT8LgqJcikoCwnhbskEIfqiXtv_wZDgcreCPELMi6tIZkaQO-D3qOaIoIlFpkFVzT2wejITCrpl6zZLdNagvR38CmBrFXSMT16Lm_R95Skz_53rvSzsgY9HsaB0X9Vp3FWl49GXEArC8UgGh6W6YxcZ0GpVDqYN7t0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBDWo-g8AalMkJ2SUSJ0vOP-Dwk_ZmqI5uEWhA1ONQf9LKhsVDVwu6E_Kn0Y_h7rWWJTfjxKfqtmOq8VYlwC8KIZYkiM5ZwAmBRnvuYInsqyiBuWODnQbrEL1vcVOHCtUVYZS-ZBnGvQIDYgYpDenPy_SjKdUoxkwjWmpbD6v7OipXI2gwLQtBBYvKJu8O3qjzm5TJ_fwrOEslwMVjYvaWujbj8265pmsOR6S3AaLdT8kEeKRHQolImeueCnORnvsIVBNC9QJtBHXedxFI5XeyMAwOiPfhW8Ahdnd1j8MDAtKAMb2R9ucwSDHJN4n2TcoR_G-7Wj1U2GQI2uuYnQWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=JDtqAnqCbEryhV9JLU601t7grm57rT8J_9MkG2zqjfqOlfJY5YvNqSSuwkRRhIq-bb5EhIjHbtl3W-FMjraKUyfS1Dkl0lWm0IIgUBv77FY2o6hKZDDrUcGBXEPG5Jrp2paEkE5nFYqx4GlbqOuNgIBboTBVunGeDKwl-mT9e2XwXxtkm42U58EbF4IMaCxVq96Bm9dXuxXtkkrd_cwwbAoYP5CSNTrYoXT-FS0-M5lt3aS8qahUPZ9koE9vmSUAOhLy3sDMzgxhAG3q2t06r83NSzVkTkT2lOWND6RHFHip3RvK7CvLGAt5lpu1lSYb5nJd9wFV4nRAaoE1UTDyxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=JDtqAnqCbEryhV9JLU601t7grm57rT8J_9MkG2zqjfqOlfJY5YvNqSSuwkRRhIq-bb5EhIjHbtl3W-FMjraKUyfS1Dkl0lWm0IIgUBv77FY2o6hKZDDrUcGBXEPG5Jrp2paEkE5nFYqx4GlbqOuNgIBboTBVunGeDKwl-mT9e2XwXxtkm42U58EbF4IMaCxVq96Bm9dXuxXtkkrd_cwwbAoYP5CSNTrYoXT-FS0-M5lt3aS8qahUPZ9koE9vmSUAOhLy3sDMzgxhAG3q2t06r83NSzVkTkT2lOWND6RHFHip3RvK7CvLGAt5lpu1lSYb5nJd9wFV4nRAaoE1UTDyxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=AJjTBZwELiP06X5H_Y60PmhW3yVOv1dT996clIVeAl2mylYbUhani_PRyJiAK5NrWY0LCQtkpRr4FPVj-rOD2FOeoJVfH1eHKEYEsPWq274CG8YlWVn2trIvcYDDqIBBMYdKXrr1J986wd8AmoiHQgssS6Ra0leIximixZsteklcY7GLgRkal4GCy79iPZ-loNM6DIytGZs6Lkp85CeaogTM2EOzX2DtrPTVeGLqH1A4I3ReuC0Id-3Tx1gGbSeHysj9YpSY2NhBx9ZMfhT1hgVVIMAkReMjmOJLolXLlaQ_ridC1CVAuD_vBoxCqQ5oYxl9FmTxz7x-jkefR9OjXaNWtPvBrKkWeEh0etpk561OxMkl06Dm3RkVUqTDeWbhHn1mqVw6yOpHdYmSwHLuLi7PPdh87NHuQHES3W0-SXJHSO00eC011h8k7XqDd9crRDcW6qJfNjPbr6222LUMIg172ydRXIzfkp5Jj5bsu4uTlEmiVuTlr4l7TszbOI7QJwqyMW-yjsSOSxJP8jyI83CWLOzsbnrwggJxV8BXbEVlFr6BbUnKjsfLlXFXUK6SIifmdmY9qQgzgxvfrK254N6J1bSL72RRwto9Q4ZslgTlhynNK0OEzxUjcL5MLG54626hleXv3qMz4IZy9Z3Ey1cA5wpYI_KfdalHvDnwurU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=AJjTBZwELiP06X5H_Y60PmhW3yVOv1dT996clIVeAl2mylYbUhani_PRyJiAK5NrWY0LCQtkpRr4FPVj-rOD2FOeoJVfH1eHKEYEsPWq274CG8YlWVn2trIvcYDDqIBBMYdKXrr1J986wd8AmoiHQgssS6Ra0leIximixZsteklcY7GLgRkal4GCy79iPZ-loNM6DIytGZs6Lkp85CeaogTM2EOzX2DtrPTVeGLqH1A4I3ReuC0Id-3Tx1gGbSeHysj9YpSY2NhBx9ZMfhT1hgVVIMAkReMjmOJLolXLlaQ_ridC1CVAuD_vBoxCqQ5oYxl9FmTxz7x-jkefR9OjXaNWtPvBrKkWeEh0etpk561OxMkl06Dm3RkVUqTDeWbhHn1mqVw6yOpHdYmSwHLuLi7PPdh87NHuQHES3W0-SXJHSO00eC011h8k7XqDd9crRDcW6qJfNjPbr6222LUMIg172ydRXIzfkp5Jj5bsu4uTlEmiVuTlr4l7TszbOI7QJwqyMW-yjsSOSxJP8jyI83CWLOzsbnrwggJxV8BXbEVlFr6BbUnKjsfLlXFXUK6SIifmdmY9qQgzgxvfrK254N6J1bSL72RRwto9Q4ZslgTlhynNK0OEzxUjcL5MLG54626hleXv3qMz4IZy9Z3Ey1cA5wpYI_KfdalHvDnwurU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=CkA-isDXlt5-oCLsBmLFPSaS8i2SmToyPWFipKcUcVZO_nI0oFzA4i_ZHP9chGmfbJid0QZNf2gCeTeLaY-KKPj2RrHn5QlKdhjh0NRuTQmPsQPkHGfcMVyNkwV2y5IRjjzunQuHiRXpFOwvKc16GzRfdv6W_hkRNj0MYcBtHgLUxB81GvTH7pKo_72bA-RVBniXJSbErUbC6HPSM3r24eREOfUck9owYVay43KFhmOZ59kh76WS0VIUWeY7IrakTprU8ydV7bM01dxbLgNw-zVpfrOX_M9e7uMJHzNypklPHUH3D0K7XTB0HYUMf3th3O3Ol15ibkgLtRmaSDnUgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=CkA-isDXlt5-oCLsBmLFPSaS8i2SmToyPWFipKcUcVZO_nI0oFzA4i_ZHP9chGmfbJid0QZNf2gCeTeLaY-KKPj2RrHn5QlKdhjh0NRuTQmPsQPkHGfcMVyNkwV2y5IRjjzunQuHiRXpFOwvKc16GzRfdv6W_hkRNj0MYcBtHgLUxB81GvTH7pKo_72bA-RVBniXJSbErUbC6HPSM3r24eREOfUck9owYVay43KFhmOZ59kh76WS0VIUWeY7IrakTprU8ydV7bM01dxbLgNw-zVpfrOX_M9e7uMJHzNypklPHUH3D0K7XTB0HYUMf3th3O3Ol15ibkgLtRmaSDnUgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZeWHkMIV6nqX0CWhHSFJIi_Pqlfg8r3xTUIvlMusshxRzksH-opYnVioZA_mzieD8KyF194FfjLG0lGbyvUOe4JfMOiNxQGI5nRLSdVXTexWNLjHh18_iq3V0Ogoy5ADdYYVHs_CSTilWVnyeFLAb6uvEHG14t5vR3c8nO9aqNsXcNbR8uRTHRk6FxuUQGg8PkpB9Wmfa_AQn7i3yLHNBJbbXdwGM4yQbPPyAKd7Ph68NAxyd2lrcKUciq00i9NnK0tmjOMFeKKNHllEpOFt6bOzLZTJ9BSgdEz20oL9lMRGSLnYoaBolphDXHRwosDFrVMo0e0biA3PByE6XGielA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsKnoYksT_Tvwa6LnCJK0gn2kbhu4uobKHHEg3jaEN5xUt-ja38Fb_NE62-gNyeLL14wi7qqEbwEvOFCuixarPAntUrhs3ShYjysTbJqhSnBjJuWXzMTCyTSuw6hKiPQealAADn4hsSOdLZc9XRMwXXnpceMEQOn7gtPHmQg3kMsiFTDe2jbCIoMEFXF8AJD-Dq5wJDWYvyu8XHQPo17gMGIIT1NrL9M66y4mzB_Wwus-staqhju1EsQ-AHGFZ8qO3od3KIjLo-3pZto-70UE5F8AWXInvLgiFjIzCykJ2zfCHwLLHsEQB4ZobCzFF1TjuuCVMFeXctbptAtxXebGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl9Uf0LaxjLau06IhPiXh1ugXe94_VVJmkd90mPFg_YwYXL0OA6AtpP0qp_RBcGzkhtbaBRmNHUNsVV82eJp8cyFuHKZ_Rk9pIjiBQ0Wq7nG9ktua8cJ8SFcF7hunf94G0XMn91-Slsh3JQDcXlHJgPNIq81YySRL5envFtcDJp9PezXrBC-wn-yQcPGxHdKO1icZxe2PyxCZNuLPtAG7Mvv6XM8Jd5SpdwCWJuXk-1kO6Ioc2gIC8Q_97jJKtDFUSTAgOHkLGXKyNB4QpnsC0wY7kkPVzS6Cz8bo6ScCPrxzC1DbPA7YS7z3j_zgPfcfXmyXO77dyXDNc7bn6pb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDqUf9dcgLpPmGKLw37PlPBDPCrN8rTCrA7k9xQEXQTPULEyt8aO-O4tMpeWV1eE6bCACIOspDWgJngxWr6zd90BR4KpS1YVbuBawClyKoHFg-L_KyZJsbBbNtwqEUR-MP7sWQNEPms1JlXFkPCGnO_p97D0J63UV2ddsZnyJr8GDuWr9yZQRJ_cuELkTjeR-CP8QU_nLWx7SGjYVzjW66RLbha8tXQKh6vx5U6rTYYS-pIxxLjE98V2QGCeUuc7QIRhrZI6I2Vx_WpKOcn_pAlSGM1m03zKIXQ99WuJ7tCTEM9MfgRwVsa9EAqWsGk6MCGm9J_LCi5QqT4mxF2hFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4gItbf33TePmL3WxWgWo9yuNISeIn9_hohk0fwDIFGkbPo70FP7V8WRDYxdUbFK_X_blo2mBRuRQt4BuqvouU2M65-0CSyhkP6TY5P-C0pqFWVHWyZPdSPG9TobukMpczkhE1nuJeZz7rIFuNbgDEowG9n75iulgo0KYDBr6NrAd8lV9ppOZhkzfZANMNf2aOf3Pu-bia9z-EwJISvM-cdaIIdOcwJUMp3s9OaAJHVUApTsU0PiM1jxp4bLYJZxd9H3o1v_M_7L8WC51xniW_FwbWDlnl9yjkBKJLfAf9CvPmWi1fLWvR4V_8YP6VnIve4YedfZ_ZeuJcEbn6pHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=uWA4cJZ5ARj8aI4U5FdKnjUfnWApDX-3oaMjcp4GeD1oNJwTV3CO52QIKU03SNDG4D5K8fLnwDR1ZKRTyPAAqnuXctWYkGedIRDVQrIgR9VgFTTj5qKdDX32gvIEXp-0wOx9E6XbU4BvOKxIc9XitDKIxHEm7FDrmqdmip49oAcZSFomCubtTpr5lkt6hy6Qu5cgVbHaJJztZMqza8qLuvRbB3CDQZW8tXuvRMl3UenDLtJmV_Xa9aOFz2aqWYG-mQj_0TeMJ9Nofx_4_wFW8OqNOZEK0NlAn2L_kkD3wE2cihXuB4TNDbGI-Jng1e8enyzV5IAXeFJ6gIp4pKoz_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=uWA4cJZ5ARj8aI4U5FdKnjUfnWApDX-3oaMjcp4GeD1oNJwTV3CO52QIKU03SNDG4D5K8fLnwDR1ZKRTyPAAqnuXctWYkGedIRDVQrIgR9VgFTTj5qKdDX32gvIEXp-0wOx9E6XbU4BvOKxIc9XitDKIxHEm7FDrmqdmip49oAcZSFomCubtTpr5lkt6hy6Qu5cgVbHaJJztZMqza8qLuvRbB3CDQZW8tXuvRMl3UenDLtJmV_Xa9aOFz2aqWYG-mQj_0TeMJ9Nofx_4_wFW8OqNOZEK0NlAn2L_kkD3wE2cihXuB4TNDbGI-Jng1e8enyzV5IAXeFJ6gIp4pKoz_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLJGWKGZYX4HRsjeEC79QJeTCTZMYRX33h-Qt_e2wcmh2IGXPpxuaTXbox5DRVshu5jospen_6pmXrxnTKmqwKpyFKvGU3w1XwlZ_UGXMhKxWewJqyzi4KaHMKmvVwXfqAjNZYw2UC7rYIDprJiBGngx0Keoy1XUlLpmzYgjFOeRMmSANbFyJPE0YitY6k_KVCkCTKr_S_VlixnTDYaXWwbTZe9uVeYdnLHZfGI3TwTGvjdst5Jhb2WPcTMDr2NgwY_Xz_2tH2K-7t8GZd7RIRbglmmpE1BP54-Dx4T1FyGtl9PBWsV1nuJFfpGlkVxcMQ8l7QI0b2gkM9abJa7pVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqtiC08eSwvEYg48QXJ4YprPbpoTRFL7NhsLRkjkx6XA2VrlxGDE4cukR3dIyH0Iu-V6yTLRbk-tHNhCRQJ53WfpdM_QBKWnflEb3iPFsniH_e4VvtVQjzDLVfg6Bxe6EnwbLVdI7gAF1TEZefxV3ZK5_Apk70HlO_12GepCTnbtXL21eXkbwDNP6dx7kAcfCc6aHvv4pVIczgiLWOtgzOZsQKkmjF5OWy-NScRjqBSKwj8U18oVR31US0btyQWNitjMzNHMJeELpmaTHTwVa8XXkMruZONLuCPajiQi-5KRlANeC6Kpl7ln9u5RUNMBNsEyQIEJO83-OfrlHnnPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNSG81lGF4AWDZxtRnImxydUQydVVT4ud0QDLLCxLkFEBBBUpVQJlHuTC0UwD03BsU2NzqMThKyi14wuvzBZP-l5_-PwKCtWHr9GKIqefAribqmVpTG0fjtEOjCXMxlHU2BUq4I5JM6kP1C9FbiB86-Y9YRcsmTkRNzCU8nogi37zM2wRFzgxbi0zWsX74cjfnDTXvXTyvJHblgFExGFBjcpdx8s8NkybyE2i1Z0AEBuyFTRJh52J7fEdPkobYSUbFmQMMDP6tQQ_Re38lCs9Vcui9kccZmhCjLY2yYykYl2fCAkddWrs4hNTO9EdCD-WrxbRpQSoT4VfzRRhm5T9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byqobkDEK0UH88MNgSdHEMsmozsq_lRISK0l7s1kNYBBH6DVAy3MCCHs5BjzL-1nzSYV6bLJp3LWgM0C_JGUnqTTZyY9FV8I_U0Ay-Rpfa0jgBLHQKOt34AY0quK-fEoQw_GLTSATIUoldhlTwFJPRr5pCQUgInCh2QUCwqul3vEl8402lybQ1nJ49gFyo87NdRxsg3U9g8H0lsZ6j0lsMpTKDp-W9s_S4KfRUvH89BRzGRKPdg9rsGwYCwJ4bzOubZF-Q886LQd5yGmMBqf2kqZn-Y5RkZBEd1VVOXBARG8-haGUXRgEeH8YS3l0ufnfqoR7MnpTwAhH2vqk3_zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUeUdlKsrMaIgjIiLVfPw_Many9pat0oPIQOUQ_uVgQpHBv5th1bgUJDLx10Tv4rvDLBfIMVyXfIKA-DRS4qIGB2M7RPfWNZgDLlKIIm6u2iNJ3qKE1iTfxJ1F8Bdul7V3DKZNNhXuhV0QkE_lygLzyGeEykl1Y1v0ibb21zPhoSc94gih_g90RtWTL_Ymyvvf2mFU298V-rhTNcwiSooFnpsVBHF_6Dv6mqP46rrW5K7pWu77UTkV25GqFrxWkmUNu79LqEXHiEzU2-XKJNpb_h4MBn_om6CcLMtmPEA69AJOS5WjEq2KysPNKFSp6xjmGZP1X2MgC1DA5PdKOpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtjvLwj0Z4leh2AQhbxNGlRSSzpKi21Ac3MJ0gNRvVwHeIWp8TUnYUAOfiVqdsLwK1DL4a2f8YCcpHDLpClUQVkgmD2GMpngV_O11ekzacph7JCT1rONuhHUgNVcahRv4ZZJfyygd2BnmNdvsU5XfTU6hoZl1Ic28SeWQkRODqEZ7IrS6RO5G1m92iQ4NwnqVofTXKhMg3LXPK3zPAXdWYOmcNn4VWIzyFMJaJaX-BSm5yEMOXQLP2p_Gc1F1Zq5MdfmGbHH1pVnZVZBYkqOYW4YMQ2pAgLwjrEj3ZXybUnhu0GSE-ZUsJtHmND5Ror0U8Yx85LGyfqN6UfDDupv8Q.jpg" alt="photo" loading="lazy"/></div>
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
