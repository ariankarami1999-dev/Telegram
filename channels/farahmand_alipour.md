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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbITLjdkx_DVx6bJXnd3yGjyTADU_TcT7UQwugSreL_yCntP3fuse-pjyjq5Jo9WIdJTKFGIIH98rOyOi8-Ghwbx4zHPjx3r86uFaSRn-mABub0oQoPgoJIBWAozexjEhGJ3Ew7MlDD3YD5eX1D9a_hizvDqNeHHEGqFVEzk6sHS7zHnRwkiNYySFqfgFVLswUtlC3U8J8g4YJKv9AbGJqu-urbOeGS3oQitvOulF20s22DBJKIqahMQXcY3FIbqAIQcYkEmQ5Ix55jDqTc7QhTPbvWM1lzCGTnN5VYrRr7Of6Z7GGwSPkzqlr4xkw_JpfI6siLvMxoKGK6BHcARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nas3tovWomn-FAMyso71GqdoDDIQPqwR6C7kZj3ns7BpdNNjcof6kF7Wrzum1-4-EzKujOhtoI5tM1tF26eugEY0wrbEPr0DyGW_GVXVNRzgYwP6cgMKTTNZU0_DbB-8Qex8CKf8gZxN1xaWV9YACIMtr1cfZYaRcxs2V6V1EMzUaKQhg5xQUjgYNRwMhGeJuQIjD1FZCRZ-7915lYNrRq4HpVGqzkrlJ2BQUfpyQlnIMDJNwitWH4j2PR0zE_6FFJrInNnpZWSIXwUGlmoWt_7rBAhkXaTIPsW8R-Kz4Zepvwt7lREgHThCvGGss84u1UUd3ZTY_AncAXJg0XjQMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_PF19z_Wc-nBTz66N5hrq45nZQN4HjIJTvIcdAcx4fhlKbWDpTTJwsHbkpyv2_Di6CWA6cg1pOR12_l8U2Bm91fb2vzY0ErujPmGUwTs7av4noQDVbmd-SmqVnCQd3XmqSjBripsnnZnataIFxNuyC365yYCpmENA1oMWEM3gqay513TLXg40p6QNFj7R16Yr0YDxiEG2Fc3rsLEzhdbFMevCBlb0jqKGnMC_DldSsvKmfoKgKsMsx5awBnvzlzaMMnrrSy4t4PmbjbWYRAkioDaIHiab7-CyFyybucoJHu-JtA6Q-XpZJYAxUmdauFQyCVh9sM6WV7FMH7BLy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCky_KPctwQaiqZUONhx5pUbQI7fMH23rwbG4uHOb2Msn3WiV8nUihVt8rdOrhx46CquMVU5hnaq6F1KKr5Ce6q3Q89GIn7FsIrMEpncpnHDUpCOY01Jzwy0UN6Qn3LyY-PPGuPlvZjgkRPwwG-QqV9gHISwDEzTC1bGC5yljBpqm12mUr698xwC6MMkceOkv9NGEmm0yhsAxlpAzGNKCK-5_PO_JhvXON0RN-h9A7gfxLHiviTFHpNqEOiSYKIyLQdBVRYSFhPSqV9E5MUtgK5PzrnwTZ0mzWXlckO3zw5AN2bXaEFdlf0ANmyvN3Fd2N4reB4W3MdaJ5fFmdW8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtcEZq8Xh6tAQx5DQ7_ZfV9cOp8L0kzKC79xmtviYumimxOAlWLe7Pmxb9tLJz_XQ0jFBuQnd-GaCwb5k8zKlArsiVzvWHbKFy_ehtLjB_CklymLq81CzuroCuhshgCM4VxUy5hj9zFYmqULEZHrcASKwD9uTKWz8bJwZ5w_vUIuzXq4YHUk0PlyaxAdGJ1EBtg8wbcgB5qaeDJqWysBpQ4cyQv6w9ih0xJsdDXK0mtoyy29kSv8u8LWpQ9seCpQ6DcxHwyVWFkB519ZW3Gt8GQvJeRizVwYyuINS5QFM7N1gGEo4fKfEUYTFjyVh1IDegRLnxK21PqpWzJIkEDbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGomyDpPAwo1UyNP9O_E4xmVOdCpWe7DhnCZdWp9EooUBmVxTl3WVq-JyFcDRt2mAuWPDKKtOS_Ah90eAp0b2IAyEJkmCYdY_kcBLZ12aZ_8Fc1eSVjLKc_VfSJCheVCOETK6HXzq_iDrLmWJ2lE0a_ngaRa2la2Cg3lMaZavroJTCqbtEyCQ6PBPfVSVT2DT87rzAROq-GNQGbun1Wwm6pApfM5yKxCBZ0HvAabOuPTxw_h1aPwppVAnvlz8zYztwUMVJrN6TJXLoXCeBl1zv9nPCDptuotDtWfjVtNrT1THlq7DZgbkxhOlhetDddD_i0_Kl9FN9Pp36TDtSErtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu83dMZRyisEthGg8zycNAYR9hKxZGtmjCrruQaTM_-vMwEB_BbV3ekugPnUQTLsi_y--Fc2H-sxKlxGcCaTPHOgo3obWJvXgohzPFhFmB5pP6bs3hkxXyckXoDY2ppUveUtXeOgwijqMOau3U0g9kI_pt3vBWI-8x8sr227-vimrcMoDysS-Qlu-Cpcz_AEenoq7Xre-Lb3NjRzeHgpkvxVWSl4Gy2jYZ3BZ0CyHpEC5ztlRYYnu8rrS2l1UI81LVsorBDQuFuK-KxnHqq3ptJM4i2o3n5bgV7xhPD0kNg4WlB5QJmee6grNcG95ieQX2MHRgwMK6NBAv12Qry6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mauclhFMSZjPso97qRu0Wb8dIzhqJ6FMBnGFzvshitGoIRrz_yuMviZlE7TkwIIUlHP1W590v_Y7vdOMIkSp830_4nfehNfxWcFxrly1CkDwNMRVv_Ho88WRlJ3CDsVDtk-XqQzbQirgbJN4hKpElqEUQGQ5VqEID1ygZpZUfQaw5hbrctIsdUVm-W0PLEq84NZNhEIrV-6jN0LBt7k71pbtsLDxfhwtKq0W-DmVUQ8rtV6-2-kqRD0PkgIOKWsSIJq5qyto2uizSPgJ02fvrK8REWCZi0QydfvZrd4QvzbSGnEGsWb6IPZiWmNdN0xmf5lEdI2Gym0tdg35wst-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpm783EnfBkGyrUcGBAAz6wwIkFBYtSdJxs4lC5iH3-4e0k7Pn40ID_J_YS0vWGczdntupgPJMeJLi1AHROmrJf6qpLXJa4Bs9vUt4KfscpsyGEoIA7sdlzB-vLvo-to14s7nSR55YQ2MfHgwGDjqqulybUG-kCXlMT3yi7jPwNaxLzR-Wz5r1kNaefn9R0-mp44cr4_VAneXFt8fvx03EsvVw-Bhxw218CjXiExZ0YpfEjCWELK-CcVhg8li3oqyObn53V4oE0ZCt47D4Rq0rvITtG4vrPQNg4PzVQyW8Y4dYu7WnJUWMRWqjtbM2tirQ4lmv85TaNs0ac4VfFQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5Y8z_FQ3upKlK941vmmP93OShl7AZJjieAYAh9Vas2QvtZsfceIIDmeSQbuKcJbLMnOdK5WaA5kCnWz9dJ12Y84bnwTr19lnShgkQCOAXQxJHydve8PZYDmY06r6svlUS8TcDdzU-t_Orcv8yKoMu0LFTjmJdrGwNH5LtzDkj64vG5ZE4T7HUnxVFS3kz7M8WQQsXPUrpSfIU1Srmg6JlrasrSKs3seZN0IElbRtKf2oPX1aXZcAOTbKoWh8AbzypSH-kfkFpP35FYSsqH5gFTKf2rn6vuPQCcOLhkpGsZfV8Ejl9ZIj9AJM7LTEcjPEbb5VkFzQT1a1S837oYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYN389qYljR9qDtKkl0MaBVHu95o1oJOLiO9K9Qnqi-HMn58Y19srcgAk10epFkmnvFXT_TsUTv_n9FvhZQBjzA18kErcyZ9Hk2dAqZw5MVkd51roP9wB0nTdMtFhBHU83Nh_ApYI39pgNkMXk1ODV8VPXHn6WxrBs08U9GDP8emugI-TB-LXYJ-4atnGWLK8U5d2HrqKv8NgOGUwS8D31OrPfNb6ojDgDD7n1bj-aWfLHC2WYSzfboP-HXc9mNrBE08ZZUEejDWKfzUL3WONwi_pNpqHxsP_qh1e1HS2HzOQ5zmReWaw8UGOkEApHdmV-Xq7e4X7J6d8Y6rFGu_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN0apv8irFCYHmP7g40GLjdvOOvmOK-H9uubh3d_oA9wr59CF-FFCd8aLFN5E4yl3nMhcnPFFsZ7b20Q7uzpXlPebIrBJR-DKAHD4IWDfesIsPIBT4W6f73aHcl1tOnPJKE7bW6XtDWmtjjzLp12Hnc2CzKj6mBCxJe7Z_yIFq3XJIH1L-lqhw0SC_eRl4otaY5IjMMT-bm67h9XnWrPKk8T4EROlUBnIvJ-WY4Svw9kpgikV95TU1SqycWMhudF-18F-XQGTMuN0ljsWlwbGz1GP3RfVOJno1Sq_Kx8uSTwbDrbIhh7TFdv99Kj0PDTcmEQLu-twVZRseJAk2ikDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=smyoOmI15irlywpknn2-XhlS36dd8GhGBCDxDiYWK47oSyvgX_59N-_wwswsy1wnVoxhy2LUcveyeAQXZXKYJFrIVVFVOu82somREGMtGgEQ_PMXN2sqk4IgKIQyzqgC4YCtK-Sl7RKAi6HS-_irFdHoVQp-iHqhdQSAMDgqLa-_iX3aA6G2A7WD2w--r2aGb5T6AdyfQonDOgR68bcVnq1XUN9dqmfeZSwV8cIJaxzC09GuJUiICTwoY3qPMvL_sy-BcFxuf0yZhDpaOB_DMniZ_jZzzeHgPNr4ZcL373z--XlD8Xj73u-tS7g-NbW1KXpLcXH0dmOuCxd61FN_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=smyoOmI15irlywpknn2-XhlS36dd8GhGBCDxDiYWK47oSyvgX_59N-_wwswsy1wnVoxhy2LUcveyeAQXZXKYJFrIVVFVOu82somREGMtGgEQ_PMXN2sqk4IgKIQyzqgC4YCtK-Sl7RKAi6HS-_irFdHoVQp-iHqhdQSAMDgqLa-_iX3aA6G2A7WD2w--r2aGb5T6AdyfQonDOgR68bcVnq1XUN9dqmfeZSwV8cIJaxzC09GuJUiICTwoY3qPMvL_sy-BcFxuf0yZhDpaOB_DMniZ_jZzzeHgPNr4ZcL373z--XlD8Xj73u-tS7g-NbW1KXpLcXH0dmOuCxd61FN_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=WTs905RksGYcLSkeJUZvl4E_EGooMdOpQEb5yd3E8EaOvfYNYzO5QNETi_p1CiRMG06BIsKksy3RqLw4cu4mhfSUbfdbrifJao2IYwlfpPmSgCiyZOXVIkUi4sc8mMxhFAeYNmF1d0eHBCMa-pUODQ2_b3rgtb1jqLEmSBKuG9QOxvXinU0r-3u_Y4SX1k9O84akQAJURdxb-AXW-FFizKqA8PUpvgizbd7QrW0CD4ZRxjpuzcDh9XmJeKXiSYysuFdxoi0Cp9nGgmQ0Fm9MuCgPrnw2ypTYShWm5bjeJVwJCDz4UOhB6Va5eO06gyuItGyhqB9yzWnQvVZ6yXxB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=WTs905RksGYcLSkeJUZvl4E_EGooMdOpQEb5yd3E8EaOvfYNYzO5QNETi_p1CiRMG06BIsKksy3RqLw4cu4mhfSUbfdbrifJao2IYwlfpPmSgCiyZOXVIkUi4sc8mMxhFAeYNmF1d0eHBCMa-pUODQ2_b3rgtb1jqLEmSBKuG9QOxvXinU0r-3u_Y4SX1k9O84akQAJURdxb-AXW-FFizKqA8PUpvgizbd7QrW0CD4ZRxjpuzcDh9XmJeKXiSYysuFdxoi0Cp9nGgmQ0Fm9MuCgPrnw2ypTYShWm5bjeJVwJCDz4UOhB6Va5eO06gyuItGyhqB9yzWnQvVZ6yXxB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA12pIAbtXZuyobt0L25UexhE1E1mMUSZ47h5nPpcTBNMVbsBymvcjrnvevQ30RBxmUWza_dK2HjfOvAjWr3AMGMJOY9gNQ20sRTao9YFre6cAoenVwUgxEf3CTIvLwjdwvZPmeqJLfwkG02p4z7paFwA6lSofNgrdhda8oy2Za6tuHgLGkEJhtzWVGP9oMtqq-kTgYDBizj4xZWf6MCKmKL5tLnA_fAneLK-l3-_a0BaxMhuDdnMlpouScnvMabFcu3CDTtOWrgb12l2E8Ke9RuC0K6QrbdYkEw1JnYOD4wpCb5CVQKcfssz2Hx68LdPYbCv_cX3od0SNoEank4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTUXZQ-lMNRsoNExUwurnKQ0VuoT5nb2jmimoKiy_Nw_Dbr37AfoUOIdk78VXB-0IxA3vd2NNqacBDOLtd4qjlRsj28wupTFSgROIJomdtPsAfW55-3e1e2AtUxWYlUFg3cF5-eh3_Vdoh4cPcGkuO5Pd5rYANWFh94wdyMUZeLCLqOrwdFToKD4cyP0SjJGOLTtG8n18a8fwGOI8Cl5V94RFGE-jG6KEwL9sH4fIUrS8hIBc3gcv0da3pJUAvQBgC58CiKV4GtCJIfTnp-MqsuwRyBcay-KjCEM4NHjeChZKR1xggBTLV1HdUDqlG1QkPwdfEeWCf3EdRb6m1PYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpWIX27rZIvifJ6000Dw61CfFxVtYRllcUFW83D9rGF8NzZp6jyYLUxinV-h5FbYh6kTEH4ZM0bERWOQGUhLcvB0qTeYFzSdkZiSw_VG6dlcBTMmpp4SZE2aa36jqQvuzT2pc3BW0dtQua3cRgJpgUCB9REzDvSwzTHpdCvXdtpnzah9R2slzpmfxpDywFDs7V-IAPBzHH6LJg2Znhe0QFRtXVM9DYmXWZ_wI_F1xWQgfHvHUHDiSgAOBYeLEA25kQGa2lOyq74aJBSKkHHu8ToJInBnvaMwCpBHDIgvW6G6vWJkxZ3lFxss_U5xH00m_D1XKjUPDC4JzYbmy5jvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=MaujCDNPjTc7iAQXA8oG4jqrrLXsnricsmBlzsjvPvaUhm1k_6Svg489SM-PucpBTIIkA06_Re4bV4x3pFdx1TK1xqwAOOCgw5p5YMvy8mX2ecdudU5ILRoAkwVhzGGvuv9H2agYBgUIC09TwaEriFlurA_cVUEJHA24FflvY9jbxP4JoahbN17bMSP__9onEj4hr_cwTdQ5SOB092rPjuJlhiYPkjJ4kmYGXq9_-XWBuzTc3irp3Bst0NF34ZMG9LQqo9FnTiCPUfBdJ7IsnindS2enPYz9WllHLr-YsqLx78p4gSIC7CccuMiEz5ODNoJjcF6QuQId3QU7mPzPxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=MaujCDNPjTc7iAQXA8oG4jqrrLXsnricsmBlzsjvPvaUhm1k_6Svg489SM-PucpBTIIkA06_Re4bV4x3pFdx1TK1xqwAOOCgw5p5YMvy8mX2ecdudU5ILRoAkwVhzGGvuv9H2agYBgUIC09TwaEriFlurA_cVUEJHA24FflvY9jbxP4JoahbN17bMSP__9onEj4hr_cwTdQ5SOB092rPjuJlhiYPkjJ4kmYGXq9_-XWBuzTc3irp3Bst0NF34ZMG9LQqo9FnTiCPUfBdJ7IsnindS2enPYz9WllHLr-YsqLx78p4gSIC7CccuMiEz5ODNoJjcF6QuQId3QU7mPzPxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG39dZnCyMaG8IXBTdWP_DluUBv-33QC1OEt_oKyMfhodyGQzWsYsYw8KGv09PXQws0gPXQlDqrpNYxIOaGyiNdaUOuyRda3laGYWay0Tip2HuJikNg15jHN6FJcMRNxojfpmHk1hbYziJJf8uANCJ-Ih3OdLSmLUXfwT6byAzmql9jvwK3R77OdBAOKEex_QmumnYK5Gn11nsi4oAtSCPSBtNeZkAEs6BLVnM7qAToAP34MnhAJ4W-lgvYFhTPQBIgXR5wdV4lMJmZwtvJqlTLFoq0kkKOUUC6pi_Wfw8CgT0eeK16nbQfIk2IsftMfSU-MdGqJ5Q9DMOrflDcrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6Sw0Ygu-nniqXyawxifFnDyPBgayW5BPeq3pRfJmuoj9pm9Cmt44uDpSibThS8VZ_XtVv6NnjnP27T-nH-8BQkJE_KRYmNyj5SDUWVxPFYgSh1L1rOYfUXH2roZjVC5M1ChXVGT0UX6ek-RKtkBjQcB_6nOvLh6-dhING3HX9CUd2EK_BGXgpK_xLqtQd6RdDNZt4UYXgJxhgEOEv7fHEEhLK58lgFzf2veow30JNlKWkyES3vTnA-xG2P7SKARsjTkq_mY77G7LXMOFv5-t3-TPoA4-dDZj51uhPnHgyutOO1Gi8PvUZVtspxZUCRzJ28uHchFzns7R5VS7AZ2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy4-5pzfTDtPF4ZM3c2-NqKHnZIofjvTSSthhRT3g6ekTzkVFue7GFguSczuW9q-M11YzjP3FIuAu25omBzpD0si0GqKKkCEMTTHFogLrkq0JayeSEYLbkPnge9h0b6e9fr5lAHYAwbWfYQjbsXFV9FKqyw0p66RJicmhSBAV0zTPbGRlIdbH74qb8LsSfAVJ_f1D0UDxQHZVIgzYtDWcDc67YzJ3vom1WLJjyB2808KRqhJ_D9Ziz5R3d0DkgohDGFFna3TumYizsZJPJgTytlBn-ji1CdzCt9CL5Deaf9Y7WaujvUz1Z4OOSvl9G7rxv_x7nXgelhSthi9RLIabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9IJ0rbS71sFd37vYrGNSGGBoy3IikpBet_3tVbYOTCKJ1uNO6nzpgcBV-mhOF3HyIeVQn64_XbXdPfyCFUtwO4uOY4yJpzVdgsVLsnqYOlwQUup5nTZhS2aOxykGr9PYIb6nGib7BbNQxwVF1GbVj5GGG-9pUQYHvetzHH1wdD_2WnooTGP2sWv0LBZQ0NzLD9fcMg6It8bSAVqDZpUBCuJoTIbA-mRzykY24NQbfxXJ5tcYgvB7rPweY41qQ785Fl0AGf9qWFWz-MrvPOQlKLfrsETA99EmvWgrLrvrLMuJmkRVCZgdJfivHm1evfRP2f1V3czMGwUcpZ9sB-fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=HwTG268URVcnNXH7ChWvqnnGAz5YbgOjNxfea1YJGZuAYL2E_2mixTBTPYw8_ydP_KcRHI-6IDkhdPVyioFvudvRHVdAjRUlhQ27CRNbNEJUSrhXODdgtjvGPc7NB6bfoP9LnCa72gHo_z4bi5hNixfMAbAnppBZjbVc6cSkgVo08B9zGNL6H3dfEzVrW4iALPitELY36jglB22FlTVhInKVXvv-D69tfwb8L_OeU1WiE2YI6iGikFau5vJpw5qZfiXbktAoPSNcmzY4sYPoZTROP0PmmbiR-Gl5WvBCFF6limywd2CAHs77acr0d8_kJfdVJBOdq5noavP9m8WFfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=HwTG268URVcnNXH7ChWvqnnGAz5YbgOjNxfea1YJGZuAYL2E_2mixTBTPYw8_ydP_KcRHI-6IDkhdPVyioFvudvRHVdAjRUlhQ27CRNbNEJUSrhXODdgtjvGPc7NB6bfoP9LnCa72gHo_z4bi5hNixfMAbAnppBZjbVc6cSkgVo08B9zGNL6H3dfEzVrW4iALPitELY36jglB22FlTVhInKVXvv-D69tfwb8L_OeU1WiE2YI6iGikFau5vJpw5qZfiXbktAoPSNcmzY4sYPoZTROP0PmmbiR-Gl5WvBCFF6limywd2CAHs77acr0d8_kJfdVJBOdq5noavP9m8WFfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_AGmk0qXab7dTIC3hb_vtD7Dllw27g4TljiQcwb--y4WIcAOUkHvMtiN3HfKrP0oLxo1cf5UPBDsIDfsAGoWLShpo01PwD_G8PltWcQ7bEMYVdkXtJNUEJ1M6-_Utv1-eAhkvYdzL9nu_JssiG8PYUQQf5c4-InTM4VOlNh_iO6uUzLDtPIp4vUi4Ng8HfsfO7Cakva0OmpBI-dwj0XDlbO76bq-fg2hmpFTFG3wH7QwsfHAXT6XIFl6XdXGnOWupSJgQ64n6OPS_vQFP19xV9qMuQOSzo2GeZW0k6Hmm6C4AGx6CdSCnb5er1ZDxtLXWbtbuGlQWbswUQMyb5KmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=X8zGX2Vjb7KXfrOfGD8QnepAD-sf-RFOR4cGLxcfI7ZMdtdN8q_zuTIMDwA0GQ41cSOtjV9ujfjYLSaYIKZ-zQFsUR9b9jlYkX_PFrTe3MUFf1OY7Svpi9SWtYA5RNcoea0qqdFPX7DseXZBBcmE5YXloywcG_HPCWuFYQqun--JRq6mP5QAES4yRhWR_yA6e5OEV4H-Nnk3u19PK0pOb2TrNQjI9_QyP0qyf8pRlPq2wy687GpXKJYjGtxs--9gwouv8wP-1Z04qRqGFlenNAGM9wXV7aXwLzRIbYdmJVt7i_19XdKd_grJmdALjgQaxdSKRj8fwmgsqoRIBy6I_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=X8zGX2Vjb7KXfrOfGD8QnepAD-sf-RFOR4cGLxcfI7ZMdtdN8q_zuTIMDwA0GQ41cSOtjV9ujfjYLSaYIKZ-zQFsUR9b9jlYkX_PFrTe3MUFf1OY7Svpi9SWtYA5RNcoea0qqdFPX7DseXZBBcmE5YXloywcG_HPCWuFYQqun--JRq6mP5QAES4yRhWR_yA6e5OEV4H-Nnk3u19PK0pOb2TrNQjI9_QyP0qyf8pRlPq2wy687GpXKJYjGtxs--9gwouv8wP-1Z04qRqGFlenNAGM9wXV7aXwLzRIbYdmJVt7i_19XdKd_grJmdALjgQaxdSKRj8fwmgsqoRIBy6I_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEMbfOOyw3Mv1GJtmDdajsAppgYjiCTg6VUN6hx1yG9EMzadg8jNGBMMsYqToD4GNUGEZ3mQV-99BLHOldl2gzS64CwqRZ-c1mWtdr1jBrBwdoxRnlHv9q74IcyHXp5hencFHJDmjs_IXtdfnZFAB4DMye1vBPxu2FXXnEfDcrwHolplCkmjqsBGtlhMdz00PWQwqMDTzf4noqvvliEgGklyPh-G96x6jKT4PtV0eNmqbRqIGzZKHcezSTBYN1t7sSO5VdJpcb2br1XhIDJ12BXvYQbPxY-Mj78RgZsNmMPZwih-lXya_xqXv8WbowqmU66fQGpIGwoDMpQtooG3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=r9_TrliKnmOEd2cPqXg_dOjLo3_df2Og1lnf_fRqOxQcZLLcdeNp1-W8xKfyfYnqssRul7qXhS1Y_KJmSbLIIDQcE1w1UtmovvaFaIs9d2rq9dwkWCm1vQoQ5rlFX6Mo_JD6Rg9iL5m5U2XOQGEV5RsoKYyNOAfHVAG5Cz_bwzmUz0FCWVQUZqcowfIyH4_T1gVVlAG4MpZTLtYkbyuVsDrlQJQATWUZcueJ0502nH_yIblI9i-6cki_IDIySFZ8UVPXuEpa6tf0rU0lathOcHcj4NwcuuxfOdyA215-cA2CDrKUVItRA6fOHqsQSk_YltgPE8O1OPH2N_4zQvEhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=r9_TrliKnmOEd2cPqXg_dOjLo3_df2Og1lnf_fRqOxQcZLLcdeNp1-W8xKfyfYnqssRul7qXhS1Y_KJmSbLIIDQcE1w1UtmovvaFaIs9d2rq9dwkWCm1vQoQ5rlFX6Mo_JD6Rg9iL5m5U2XOQGEV5RsoKYyNOAfHVAG5Cz_bwzmUz0FCWVQUZqcowfIyH4_T1gVVlAG4MpZTLtYkbyuVsDrlQJQATWUZcueJ0502nH_yIblI9i-6cki_IDIySFZ8UVPXuEpa6tf0rU0lathOcHcj4NwcuuxfOdyA215-cA2CDrKUVItRA6fOHqsQSk_YltgPE8O1OPH2N_4zQvEhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=sbnpy62clY88NdZk3sO3e6_a2uTurvCypEaMdJl32U4pF0fBtNobWw4CwxWHkaLOr90ZCENos7gdEbXjo_KMzKsnAHcIXG4Ce_FWsOfabifu3McwKWL0a7TIrwBKYfLFbQ7LuWcLteaR_5Kvd11aO0kJ-KtTC9KC8QVqRI7ljhdeJV_B_wwJtl0m3mfA8171TfUNDlBckO2OX_2pPJ5CCxW15k7kzbv55sfw_e-vQRaG9luaX46Us4HZGzMefbycWTXeq-xTG1OWM5EOf1NOGBE99hOZ95J7_0fOVWVQrpMJ4Pvr_IFZJIFK3GSvZ5VDAlSrX07fzT5-DH_9F4wAEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=sbnpy62clY88NdZk3sO3e6_a2uTurvCypEaMdJl32U4pF0fBtNobWw4CwxWHkaLOr90ZCENos7gdEbXjo_KMzKsnAHcIXG4Ce_FWsOfabifu3McwKWL0a7TIrwBKYfLFbQ7LuWcLteaR_5Kvd11aO0kJ-KtTC9KC8QVqRI7ljhdeJV_B_wwJtl0m3mfA8171TfUNDlBckO2OX_2pPJ5CCxW15k7kzbv55sfw_e-vQRaG9luaX46Us4HZGzMefbycWTXeq-xTG1OWM5EOf1NOGBE99hOZ95J7_0fOVWVQrpMJ4Pvr_IFZJIFK3GSvZ5VDAlSrX07fzT5-DH_9F4wAEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEpjYxwD44heZBZZYiAb35E6qC_FJ0YYx6-gOXXPFyKg_MIqiyPcZbhHeBocg89COhidlB_J59kH0mqhGW0JHarEDgcPj0rKTC9rOLUixQ9k17wQmqmGAw9JpzAxAEjWMhRZmSuq04lK0ili0jVTdklt1sHsBYbpaGoIQ4DOxe39YhZM0f69pM47phJ0wrgrVpsAnVQ7Xmy-w-NNCbGQeCOljkjewR5JoAAPvxyxWHotSCQZYlE6MZh3W1yfJyG9Z9UCA9MeSbOC6c2uZCbsI94SgiC2m_xAkozJhsqlxd2E6IXIO0fN4OYZ7QNfvl1tGXaxDa4xFAKu58qv28NFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_H33sosKnR5v_ZfKtVXTVFJf7C4ppJqTogWCRa_xcGjvxSopr67JScbhH_5i5G9hdwtaJZHudPCNyIFpbN5wXraBj-Crtc_vGVAdEXmt7fjJH_pZ_NQysayfRsGX1vJHBPiOkQkpJIw8lWbXED0TQZ8h1fv0Ms_RuBHs_b80XAxAwSsaqBhRlu36RFElocH0iL_pix31OMlywJnn05FgYooZTS4iBSTJtgx_f_a8Ty_ORtz3lz69Q_RROySaYH_jkke7-2s0HuSyOlBwwkP1ZPk9ELDm_Y9npLa-rm_36VuDtmrkVXfvR-Bn5xwOFN_ze7mwjyIO2QL19FW9fdEZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luA0UbCaSdntH74iKbyBIjnG6ZX9k3fT0x59TFU5YLtyaHCEGpMEBfWtnuTSvVuFxjdFIrZ2_QY2Z0AO_S7mJqKh27qZIfHmJ7HFUHuhq_l5BubqDz_6zTm3tpqf2PIUMAwUM1uCioma8lpV1JEwsfXhnHbktkA6fl4EMp4_KO0CJZX5ytJA3JDLITRXxn4lu3_JGLPEq1n0Y_21qs-5j9zosaW_Jgm7DTO4uu-snvt77q6T5K-juywrGW153ngiC1W9lMHxOVrAPOdITbq72VGVvhnDpSowsBW41QePv9xEBeoAuUr00nUOrA5BYds0hY3FhIN7ZcclMjgw006v7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6aohan1n6nBqzwHN5xks1AhaDWtLMsnO_k4cEfkdxhj14bAqSAgH2UXEvXGlh9Qd0bHDVcwBP0HDkxtzRyCIplVwxWzChOX2Fe2N39dqiIxedQGB5Ww2YNde4BsY751jgvMq9fn_f6jMgjbcwkhzhv2gJp9la8uj7Q4BG-yA7MLBiyGi6ixoKq8fiCRwQrhuOyYQJV1lilJuQ86F9SHFkFIja5Daz3uGuJEyzy-S3Bx1o9q5ANYn9RTjyJksQrvHmn3904GQzDmqFgSpL6BFQXjTTzO7pordi9UEWCfZFmhx00U15G7nblzd-5f5XJsicykw4Md4qD8_NHkBEoI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=bWsgJrME8NgnYPVadUY5dCq4iwztQHqJPTq8FMGpQ7Z5uUi_BHA9MuvEY9RXcgcvJ9sgKDe7z6UIr_9IxfDhVYp17WizLqZGNY02rLbfu7XDmFsgPh3ErChgOUyXLNFoETTykxhGWg6kh2uOcEBgm8UM7WYQ50IMQv_tHjuOEw0ytUmDS_P_zGK_LfPvGPF6LZ4Yq8n3vHkj11XLez2V4K949TnsnyFFYSHsMmBXxFDgFxz3e2v6-Z2LN40B1vuOJmXgHsTEhJGA5VyT2awYb_ffqtSxP6miarh9hiVcde3Wfb-HLXP3SjGbrIF6PN5s4OTdu8I6egeJMonFmHSd0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=bWsgJrME8NgnYPVadUY5dCq4iwztQHqJPTq8FMGpQ7Z5uUi_BHA9MuvEY9RXcgcvJ9sgKDe7z6UIr_9IxfDhVYp17WizLqZGNY02rLbfu7XDmFsgPh3ErChgOUyXLNFoETTykxhGWg6kh2uOcEBgm8UM7WYQ50IMQv_tHjuOEw0ytUmDS_P_zGK_LfPvGPF6LZ4Yq8n3vHkj11XLez2V4K949TnsnyFFYSHsMmBXxFDgFxz3e2v6-Z2LN40B1vuOJmXgHsTEhJGA5VyT2awYb_ffqtSxP6miarh9hiVcde3Wfb-HLXP3SjGbrIF6PN5s4OTdu8I6egeJMonFmHSd0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftVyzC3Ry9UiHcClE1nV-cIS0ZlCDAygwIUjvebFhtZy_5k1h3DnUoBx7qYCRrMSYXP0A9Kxk4moDzSDs1tzrRszJUcmg79A4199VuqprLEVVWtRQNUyMja5gmTn06IB1a8dFjAJVkFThNQJBAfdldxEIHFqE9ZDafKSA8rNdjKe_peZbVhobOjv8K9XLtuz3rrWOxnltvtdNBMi6xQIZwl3_yd565lhI2OQdI3o5fZDWQYuANM6tX4fz1_B2SJca8P8ZXczAO_TRBBD5VA5IkrFaVrnjKwGBeXJIpSWRg41hJfBiSgeGbCx9ZFnOyzVUMWtZRTy1VJ0KgYRriumB8rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftVyzC3Ry9UiHcClE1nV-cIS0ZlCDAygwIUjvebFhtZy_5k1h3DnUoBx7qYCRrMSYXP0A9Kxk4moDzSDs1tzrRszJUcmg79A4199VuqprLEVVWtRQNUyMja5gmTn06IB1a8dFjAJVkFThNQJBAfdldxEIHFqE9ZDafKSA8rNdjKe_peZbVhobOjv8K9XLtuz3rrWOxnltvtdNBMi6xQIZwl3_yd565lhI2OQdI3o5fZDWQYuANM6tX4fz1_B2SJca8P8ZXczAO_TRBBD5VA5IkrFaVrnjKwGBeXJIpSWRg41hJfBiSgeGbCx9ZFnOyzVUMWtZRTy1VJ0KgYRriumB8rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijrK6GzhbKCfC9y1ff24QgzLIGJlFSP_M2d_YcD8-bpNhJBTutg9YlRqqrS3sYHU7nZE-Cx_MgPBlqBTcgC1bB8lsVlYo9QEZuttDL24HCON_nnOHkq_QnONiZzp9ObV0yYeu0A17GrYmagOUzfZ6PVNEFytSpINpNKoNIbfXLXH0Txnawi9zV8r8B_3YrqVEenhtl9WabJHUAjtZj0r7USLOVD0eJoJjBKlKAi8w1uiSPDILQuZKgHJJDiPzLI2jGy6xBYf0C-NbBctk-hI5peEyjStSieUB3daT8OnbVd4kpOJCjZAOJX8SkxV425jYvdp9IUYC7EdJMD_VGEWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPrIBeH5uY-L8M6wlNPi7ibkKO-6rDFf8KXigGiP6yxajJ-t9FFmDrZIb3t7Hn_Odq8_bq93nzH-YO1BczAltt-wgvkIivP34wgUrKK0mOC5PimXOjO4WeLKfnivDp4fBTXkCloketMzqpcnCANBSnDXtt15z0laHEcHeyXH0l_EebHCRZezAEMJrTY03qNwlpwi5H8BFMDB2ltju55iVEh0psliin7QLwryTzzRfMGUaJIUXuG9PmrBgJ-xNlXG4YR4uie-6TL1PDsnKJuW5eb1C-eCq5zjAQoFIdeaTBG3RCFxPVJnWIa0kHrHn9oJKguixFd-XUW4tZOqcIuAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urVZkdKdwJGhfKNHeKGgbBTGLDQx_GaClthBjO1xBLPxa_acHZywed1AQC5MmCHMssaSijTXNT0N1G0_CVK9e4uM7ybDF8SDHMeXA3gvh9q7224gwcmZQxrsQNbZTdPp-zToKqIrXajUDklRgQiizmu2jCl0dxLDAEHFXfoK5pjBwmQ6lqvvE16QkSFpSVi163eH3HvLWMThn77Z7CYbHA0-1VBHdQt7mkPmL2UfzvYsa2CTOEoYplKn0VxqJUQHGWhxofNOBZUwpfCQBb8LUgSQobUfXejPfqYVxoL0F_QFT183wVO_vcvrXjiakAbbYfAwXcmX5l2-JhHWAT4AmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhQiZOlAjze--QzLZ0hnUxUH8FzB_jvkiRWABQwCCc32AZHocoT2Zt87CESN_pb12idxdhV9k7tpsEn0FU6U9x2AYTvFf3nMGXMFmkpyu1W39D6wzxIpMPEfUbpmbW9tzSEqig02GIgbQ-9nhK6zRX9crBPVy9KH9ptpggXgQmgn1HLLwCIYPMkbexA9dMn792nmWqxzB6HjPoFFE6Lkpk7ESH_L9b-AO2Ct8l-JxHnniuyir66AS-o6Mj2M7YZkPOiYlOcIoavr8TMzzGX884NWH1Sw2ozQsdtt-pBcoNj_zXMu0AxNIXBTbt8k0iGHh5mHYWw0x5fPWn7d-NMhUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exm2nAhhxl-XS1kJJevB3EDh6Hjjk697NYFRM5V1VrGC9e7bbCCMftmPmeepXfgoYYIFcoEZ84zUGg6OO_aHWEmlCNwZvBA_NJ2IG9vtaDZWxj6XDjurXyYdEARtZzs_rcYORatA6CRtHUn1CuDVv_O5KS_urPJqUnTytTFUlLsB5bg3zQ6LT_0_chBXezYOJtFe9Z9Ioj9FPhPV4qJBRWYTW7pRWMSIChBhg90wP1EozCa1T4NErkQd2ijWp9o1rVwClycsXmaXciNnzt5DAeAg6O6WUyuUzJxvGzFHphBGleDpXqolGqp9mQ-wcdS_3Y9gjRcjWUxK_9y11ZWuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=As3J_N3z3WmkSjehGlYxnIKfyrCBM4zYD2ZGgo8tmUyXEpAZESyxzqPB2Cgxj1ONuERq87BtQbpzTiA3-DNkivNa3bt9pKCGHXO_1KKSQQNf6MqcjD-f9-Hu7wywHeDhd2Fh0dk_XwxvK4fbvREDDd0cPFQKSXKKUCyr4ui35gtS9jkMB0NHdGgQWhdi9HF4Ipu171rKNqgDY-x1uiYVWw240VEPOiy-hnc3BflfEPUL1t4ed6w2RSDiFzu5ixPdzCoRvsyQaapo3ghYAXjjusviltYO3AwwBtd7Uea_ZMBzPj-qpc6RCX4M4O87PXgHzQJvwD8gHGU4V_6qvXTIl632vcQhDLZj4-BzhD8i9vr4LxYrobLDBnfMzI9Fl27gWwOa2mvccQ-GmUA2Mmq5jWzrhcig5edgNkKhM87qBD-vSJHdlL3vMHwq817pyXsXeMZEwjNjHBL9dp6YbodxzCZGDe617p_gRvrmzkI3D5Vm4Nxgsdr_eUpRHLBefWAYHAbm64AqDIOnrUefg2sko1s3nYLlsGHcVS4IzGv-Y0Xp4qhgEyAjg2EUFGTUVz1eZGdwQCTPEl_hSEkpK_nUBSBAL049ww2CiZV72uD-9Ad0LRgTaSYc5zNkDsLBad1ICnarrhhjwm_qrJ35Camj60WAPKmTMCfdMBVgHLP-1LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=As3J_N3z3WmkSjehGlYxnIKfyrCBM4zYD2ZGgo8tmUyXEpAZESyxzqPB2Cgxj1ONuERq87BtQbpzTiA3-DNkivNa3bt9pKCGHXO_1KKSQQNf6MqcjD-f9-Hu7wywHeDhd2Fh0dk_XwxvK4fbvREDDd0cPFQKSXKKUCyr4ui35gtS9jkMB0NHdGgQWhdi9HF4Ipu171rKNqgDY-x1uiYVWw240VEPOiy-hnc3BflfEPUL1t4ed6w2RSDiFzu5ixPdzCoRvsyQaapo3ghYAXjjusviltYO3AwwBtd7Uea_ZMBzPj-qpc6RCX4M4O87PXgHzQJvwD8gHGU4V_6qvXTIl632vcQhDLZj4-BzhD8i9vr4LxYrobLDBnfMzI9Fl27gWwOa2mvccQ-GmUA2Mmq5jWzrhcig5edgNkKhM87qBD-vSJHdlL3vMHwq817pyXsXeMZEwjNjHBL9dp6YbodxzCZGDe617p_gRvrmzkI3D5Vm4Nxgsdr_eUpRHLBefWAYHAbm64AqDIOnrUefg2sko1s3nYLlsGHcVS4IzGv-Y0Xp4qhgEyAjg2EUFGTUVz1eZGdwQCTPEl_hSEkpK_nUBSBAL049ww2CiZV72uD-9Ad0LRgTaSYc5zNkDsLBad1ICnarrhhjwm_qrJ35Camj60WAPKmTMCfdMBVgHLP-1LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASHGXHcSKN9yu28xW9lPQdDGAwhUyn0XYrtLCi1lBnXxNLMNQ5tljAq0bmVNoQ1vE0HJYUIIyAdlszxAIz9Aht25o_2_jWtym9PbU5yWp4iElMEbPNbbGqLCvYC4nvZlL0EDSmi4lBclv0x-MrlTKOp658Yapi5u2en-OorLxfc74inqbIcgy74r5VrZVytkCV3u7a1DyABgDhPRGtEQG7SYHmT9ipIAhWWgn5n4DIRaaeoIStSAFgTRCZOo0c30tkWjfNY6mcmhSt-An7-fwB4O5466h7A_qtjPGxmKv0J3SuqCREfTOQeIfbJwWqYh5J3vuQwWvRUlNJYaQnVZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=Ajg847dC9nQe9j1ovM16EVJKFy_kfPYTRXy8EF1XIrToTMEoP6sdgS-QEAVxBFyr95EcCbO1Ao1yIYXJ_W6WXZxXqmIz6Cz7J7qEw6BkgzlLV4iqr3VasDSok5i42-o9v9nkG4xRmNalv921WIUCZQ8ySOJorcChCN76gBWoOFu5dMAWnyBU2NONxzFXQvp04cE4fAOzyEMBzx6Tw15mCHCHnLEXyrf7GlxJBY85gZCYx2BIQLQZO0o8uKpOWo4B5Di9eVFMzIRvhgKXotuojRBlVnFJUcVeGkWBeK6DnhXI0W7mXditLONDgrn10CLLkMH37eNny0iyB0jZe8EDr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=Ajg847dC9nQe9j1ovM16EVJKFy_kfPYTRXy8EF1XIrToTMEoP6sdgS-QEAVxBFyr95EcCbO1Ao1yIYXJ_W6WXZxXqmIz6Cz7J7qEw6BkgzlLV4iqr3VasDSok5i42-o9v9nkG4xRmNalv921WIUCZQ8ySOJorcChCN76gBWoOFu5dMAWnyBU2NONxzFXQvp04cE4fAOzyEMBzx6Tw15mCHCHnLEXyrf7GlxJBY85gZCYx2BIQLQZO0o8uKpOWo4B5Di9eVFMzIRvhgKXotuojRBlVnFJUcVeGkWBeK6DnhXI0W7mXditLONDgrn10CLLkMH37eNny0iyB0jZe8EDr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=RqKtq5rG4wPns3Ew1_MWmHfXRg-AO7KpgC8iaFFQ1_zR252ZkTx1Y5loQF3_ry8ImzE_0fWHTyeIAbFPCN44hkIgqIpOlkYXMrlsszumISEJtIiW4mNoE9skIBgcF4i3NRgi73WKzkPSw6YD5xS6GhB_MV0HXXIZ-CGrfzXgkFkoSpeEWSsAzUtzLKzMxe33JxGBND_6CcgcImDJL4pUaCrRn-dd8283R--aaYhDiAWhd0xK9AZ-ZoEkZ4HyJZwBvMP5RrmgMgOmwgHngL5CNBbwvs5Am_wknowJnO-OSNawOe6KJYuYYcWNujVt4CmMiRLiY7ELYRq9CrBrFgcWqUzVctyM6Nf4v2EiVXT1aZwNlUu37sf5e-YiFtvfy9RVnqK12daUkVHU_KAEfjopHRiEBmLur5ZXirnTx79aINKcyj6u5dDAFO4wRlnDrlC_o3L4vh3iXXKYJgg7QdfZ9I2HlLXyZ5PvGzokv6PCr9_gXL0rofy2DXrCNqT-Ri1NOXESAuBM7bA10NFKS3jFP4HHj4ERHTeX3tB6dHJS0jMJZZZlxPfkowZMrvYyffdfHZykkbRyUQiumWUjtGMneeZ3lt_Kca9OkcQUchdy9bQnb4UvqFm6c-TLOMwh4K15-cfUQ2vQ5P6_WpP20o7TshE8fOsnrpUxGz_68YnpBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=RqKtq5rG4wPns3Ew1_MWmHfXRg-AO7KpgC8iaFFQ1_zR252ZkTx1Y5loQF3_ry8ImzE_0fWHTyeIAbFPCN44hkIgqIpOlkYXMrlsszumISEJtIiW4mNoE9skIBgcF4i3NRgi73WKzkPSw6YD5xS6GhB_MV0HXXIZ-CGrfzXgkFkoSpeEWSsAzUtzLKzMxe33JxGBND_6CcgcImDJL4pUaCrRn-dd8283R--aaYhDiAWhd0xK9AZ-ZoEkZ4HyJZwBvMP5RrmgMgOmwgHngL5CNBbwvs5Am_wknowJnO-OSNawOe6KJYuYYcWNujVt4CmMiRLiY7ELYRq9CrBrFgcWqUzVctyM6Nf4v2EiVXT1aZwNlUu37sf5e-YiFtvfy9RVnqK12daUkVHU_KAEfjopHRiEBmLur5ZXirnTx79aINKcyj6u5dDAFO4wRlnDrlC_o3L4vh3iXXKYJgg7QdfZ9I2HlLXyZ5PvGzokv6PCr9_gXL0rofy2DXrCNqT-Ri1NOXESAuBM7bA10NFKS3jFP4HHj4ERHTeX3tB6dHJS0jMJZZZlxPfkowZMrvYyffdfHZykkbRyUQiumWUjtGMneeZ3lt_Kca9OkcQUchdy9bQnb4UvqFm6c-TLOMwh4K15-cfUQ2vQ5P6_WpP20o7TshE8fOsnrpUxGz_68YnpBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=skPZ7DWrqfJbbgwP9O0bQOhfJ-8i18MR8sX9Ry3Uw_tg8oyjLngnNFxwdYQoT2ty48AnS9sFXdWWro8YAWKtbhaAfy0WcXwDFMLwkdtpytvBhG3lbo5bPuVJETNziuySvexzbLSEepIK6A2m4Yk4I6IbWsYEUCbMdL-JrncClwyYFKwilmC_pCciHt4SG8B0WscoCkxtqN23WNizt4o19rCABkayraj-_8UNMCe-CIAO6JhuIkJGEeYDx_ddfEAXpzqlSmqs-TAwT0-w5Ph2I_dGT0FJZyjeTbm35F1sOWvjonlLJQ_6qsp91fyLoJ5kRaIf0k4-FanDm4H4Lqhy5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=skPZ7DWrqfJbbgwP9O0bQOhfJ-8i18MR8sX9Ry3Uw_tg8oyjLngnNFxwdYQoT2ty48AnS9sFXdWWro8YAWKtbhaAfy0WcXwDFMLwkdtpytvBhG3lbo5bPuVJETNziuySvexzbLSEepIK6A2m4Yk4I6IbWsYEUCbMdL-JrncClwyYFKwilmC_pCciHt4SG8B0WscoCkxtqN23WNizt4o19rCABkayraj-_8UNMCe-CIAO6JhuIkJGEeYDx_ddfEAXpzqlSmqs-TAwT0-w5Ph2I_dGT0FJZyjeTbm35F1sOWvjonlLJQ_6qsp91fyLoJ5kRaIf0k4-FanDm4H4Lqhy5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSYixB79tC64QqNLNlobEP44m_9i8CS4py3P18_otsIa9195ut9tV5hIHZKH58DuIFjn6vvBXgDV11wCV07Yr2O3x_wQjlquSktMPkChdCc_Dw6vl02DiYCl_wUmzngBYxYis8EuzO2CCSJtNN60h-m70EC7f-lHELpXJkICH6RSrx1sqMwk1hx-6EcBcpUtXwA8O5pQkqAyqHa-Y3XxOlGsrBsHurfpTHnv313TVLZPdVBO5aqgE42cVtazRMpOQsDajUgkaJLv0_BjxSSNqAQTxELRhFr1TOtvPq6ji0-U_uVAiiNSimozWZ4Y62J2WFD2BxRD1eb9UAhJgQUenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLlLNfIfCSlpz0lHOoLgDUFdQT95E8PyneHefNhdydWUKe8y1oBul_Uj4lho95FgOObqBhJYEUcMfpmDi-cS-6mS8pGvuCsUzUhRBSiUnzuTpPKWednOtqLXBrIR60VozwDgG9-4jcNmi7ON6o2-4egb6F-JDd6PL9VZL9fRmJXDjAUdCqh58SEQI7gff6WhsU7zXgTdXbtnWHEHzhhMVKWht-ATZ8ZUw-DdQzDSXsurPN73UYTAAZmpoeCg6HZbxF9r5LRcIrN3ZYuJ2HuBmqzIFUlMFiS9Q6MS20Y5iGtcj_ivVuA-Z4GUmd0U4SLlNYa3LgiNFFJnpK2TLU1SJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLZcYCBfnohT1AzqOMtNGygG4RprRs0DwzYVwnVVoOJqy3llKM3wE0GjU7MzP5BFvJrPLJ4wsCG7EGtLsfQylxOZJxQ-_RBr1RcKMygoP9RZ3Pn7MvIeNnAp9StVol1kwtPzHC0gEokbeVQx8YAjBzJTT2hakUpJoz3pEBduLeHxWs9EsgacOSeQd3UMMsUgc0ihlY7xWluqZCmaWgsoYlApiShm241MnntBuRe5zSe-ZB6tnxf7M6MxmJrzBSeh8vNIA-H5xy3Zv8mft1hFi3tJ9Fdewl1naY0ft0_oXIt0236LI17GcNWBTYcBoONsUlM9ULzYK3xGdGUYdpZbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADobzyIIIdBW8UPlrbpWnheyPuvONvFw1TmxEZvOVHyh6JdR2ihKfivJIAZ9-eCRIG4RfwkxgqbG-kVtGyDSfcIUXE_dZCoxiHPaLtUiVN5KMDlASEYV2BGynifPL8cZabMevVzMGYndweImwDtHtcLi7CJ7rAOapQFLD2K_7kdmbYSzALNvDjBJWWvkNWmFWwjG2-vwXcSquQtFviide1ng4cJLPSABeuuXyFPU86A_S_4809ZZBdbjSIRwlON44nsQTjciQKtaXax4lZbt1ETjkrAMH6si6HRPsbrQb-N-ErGvri6NHUeWalK0gLliwEhXU7hE4LkI9oa2dIXA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUU3IHQYa1xhonJ_bPVZqv8_WxSZtKvffpOO0T0xzuyidfohvKLw-A6fNbVXauX53QA1vKShC0oSYv8XeUu5ZBIj_6MTFT_k_-f38gKPMq2fgNOqthyYPIu1pWHzdGlmOIyRfaWcYkic0qmeypRkgV-j6vn-3PD1OchsbuDOAVgwVd1oXO0sefwba3pj9hp45VXLNpPgNRtr3grS80GnzfkMVvtDL7OMOf1bFIqL-SJ2rkad7zSxfyIHI-80Q-gxIzM4Mb7S9If5Ky0PLv1ZcGljdEa71iy1-nmWKg6IPxuGdLV4m9Jna9XoAcBRGTIaZGdh_pYu9EEioQF6XxGoxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Gb6qvKrjVWu-cK5iRkuNN4lXju0TxHIA4k8b7cc8dRo3T1QLUl53SOOpUNUvRnfcJ8JbuyGFAGdR1Ngr-TRrKmGPRgXeJkiYdKdQlDXSDgaEEykknx8DnN_UrWJh0ooHdLeCYs_m3zQcaD7rl8mRwVGTzXjXznEjJzdhUM51l46NEdjDLoE4FcxYInkhd316LUHfYpSPFMNMnbCQi7YZF7So5XD1DCm7xNrwjd7dFDW0JF8GHk_JaF4P7hN8LZOn2wuipObv4W1maSf-ETkbAJIm2yr7y9zQzoKQfEXDVk6owrFJoaCqSrMqe2-IqiWBYI2ZecH4Wq_S2uRMApUJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Gb6qvKrjVWu-cK5iRkuNN4lXju0TxHIA4k8b7cc8dRo3T1QLUl53SOOpUNUvRnfcJ8JbuyGFAGdR1Ngr-TRrKmGPRgXeJkiYdKdQlDXSDgaEEykknx8DnN_UrWJh0ooHdLeCYs_m3zQcaD7rl8mRwVGTzXjXznEjJzdhUM51l46NEdjDLoE4FcxYInkhd316LUHfYpSPFMNMnbCQi7YZF7So5XD1DCm7xNrwjd7dFDW0JF8GHk_JaF4P7hN8LZOn2wuipObv4W1maSf-ETkbAJIm2yr7y9zQzoKQfEXDVk6owrFJoaCqSrMqe2-IqiWBYI2ZecH4Wq_S2uRMApUJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaCa48nWvyPe43KwpYNSDvL7sphJBt6jiCRMUgLQ5dw5M8uF-Lwpd4Hitpkeju3EdUsb3parfKUHIe30g8mZ9ZbjGJZ0W293Kq6UwHOm4jX5kCPweEjZg3fhprQ9p9PgZZYYkUgvBZD5VemeMILmnztgdWqrB2pLSjA_4zDoUBEDkCYLCUefvk0oltBD-ASpf56ec8-JenAZcppHpOG9iw-Wl8CRZRm1vKxSGJSNio-KwMNkvIVLKhCNMblz_YeQY98ZgL7ddl1KsF4Wo5BfGZCwcRfnp9zYH_WAZ1kE5o7abClW3afIOtjLFYSdCT2uaxl_IrEcfcff7WQRhGwg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLS0nCzejs6_leUwPIy44UGKcG2RHWpcrr0_uIWiiRTVP_ExQGDMzxbHQYm2_GYJKOsAyBqlJHMVrItvP0uXCS5N0Z330yQQUHoYK6dvdnAbvRqDL_q2YJ2OU9ETWsWe8F0XS2eohRO6lB_ddHOQWHO0D4EiJC0u-AV4iyIQx0vvgFmz7_wYT7Z9KJb2nJ6a59uy5vlyanQJlWRQ2NuLOUUCjWTd0VBmaEibUK6lvhmA7XlWvTFdDPf0YKVcMW7dzYSEXgtnnM2S1O_tKZ0XMg6KzQYAMBMN5q1BlGI0zt_MY8TRNP34OXt-lXF_hQPgD92VkwdXKr1cz2J3XtXC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7nhnY6bTEQAx-Wfb6WTZHO6NgkDQU06vOk50kehzG5WEtETzYFMZQcz1Fgvz7_wUEYOAW8w6JuGGLzIfpvg5xP_x1DXcmNc1ifPsz6xnfWpYRdpbNbpixif7ZPz88kE76Y9TzI0iCZ-NwwO-3gajAJSy2zldfIMSohhBhkiRGQq9Ozc9lCrWCgOEQrpO4693FQSVWLLxiZdo1YugV47azxeP4jWwrhmaKY8aGgm1uBOhr-7Ho6glVtC3U8muHfFJKc_7GAaMP6pQCPIKSkJoX097AGS5UH-0YOp22jf-HbDrEl1Hx8Qx-PGhs7ytgR68L3fJNa14jzlE844HSpBJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-n7xd1pXNO-8j4cpc0RH8n81phs1JFr6lD6Dq4KLnxBz5jTJhWEOrI7JbyB3LB0eVgdfrPQ5B26QmLp3tfNZHP4-wGZLuhCiXG-vn7bVVmXJQFFZAU6FuWPhmJ4V-gZXC3beVS9-4NMlKJTzaLOsmwtK-bP6yf9RKbTYNn7SpAeoc91WCIz7zS8HT9MrOCM0hdl7i3FNofTTgBL3jh2ZgQfFS624kkXGq0jRMpjT3QJruMsxa31dgw-6pjrtgiHEhVet0Q7co8tPafFcaSTFIRvAQh0cwraXwGrqlrvGjejiPPxRdkZHjpS4Pwvo8OEg0tCHJ5BjMf5IUiGHw_TFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfOzHyT-w-6AXy2NN-oU1eFeeT3XlrRzkDLao9xUwwyk4JpGvUF3R2hOXlG34cXVdmKQgtL8RvUCrC9LS6KwO52oUHbcySdGLjybwNJEAkpVNduBn1f9Z1RQshl0ji83sSVRP_TeBuqc1Io3t_700WSmoC49aN_olRxSOwYbSllSE7It6WuiIjCKQsN93ZCM3BloeKfSwBjP_XHC8XRKQ03r9ECgc_14LeX_AAFTZ-A0-V-GcOTUoP97ejY8yFK9eUv3lxq5Ip5RpWspAAp4dgBqXWcdsTk6wuZUHuiGkkjYwehaWPOJLpGYwBC2ejq-bDcVlMEyKZ-lbgtagTTMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/isHcYhLTusapY088IaYBV0T9bxRLz3jSyng_VBeCWJWJLxb8sahlHvqyUInEC9Kn3DBpq21xY7Rnc22b7kw6ayrd_G4dlZ6iX1qiYMOV8rIiKXCi0q7DBGeF5OqTM64_7qgf0wWpysX0myvUetQXc8A94Zp2XMGUKm_2gdvy9dVLoswbzb_uBoEX_IvNA945AiHDrYhrZGFWcDtkXvxYC8N5jN6qDyCT3BQShIqhu0co7drRytqy4ThGC5FR-BydfIyxndHnPnSOs1iThZ3yX_BkFUgSLSisCxg7-M3vNQdEJ1aGjiCkVXPBu1a96WNIeeKNQXQi2vcDNs9XRHRKGA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
