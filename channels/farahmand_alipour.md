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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Qejb3Ih3ntqESpzYYlUpSS15y7uuKpzrGXwk3IFL27X3H16GopIQM438c__xQeJRzhTblWNEwHMSS9e4twyJsapwxIWAkvZh6jBdn5dG_JHFq8wD5DX0ZaAEMjJtCN_koppbdWpPVvpu9uUQoGV8LfL1FXtmCY21joDsoLWrYv8m0bFjjwJLiKC8LTLTMTCzP5ckMjooQZ4OgHCOh6VfzWm6FckCAZRIyT09aQ88ohsl_i5PQBkAB8RuUK39S3uJd8l3XuONLI72V7l3AlrEJ_TiyAkl_6DhrR4n3iwMkKKxCZ7KAp3J0SkgTJQbCLN9mLmYaEW2HSsEHYLhpzpxhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Qejb3Ih3ntqESpzYYlUpSS15y7uuKpzrGXwk3IFL27X3H16GopIQM438c__xQeJRzhTblWNEwHMSS9e4twyJsapwxIWAkvZh6jBdn5dG_JHFq8wD5DX0ZaAEMjJtCN_koppbdWpPVvpu9uUQoGV8LfL1FXtmCY21joDsoLWrYv8m0bFjjwJLiKC8LTLTMTCzP5ckMjooQZ4OgHCOh6VfzWm6FckCAZRIyT09aQ88ohsl_i5PQBkAB8RuUK39S3uJd8l3XuONLI72V7l3AlrEJ_TiyAkl_6DhrR4n3iwMkKKxCZ7KAp3J0SkgTJQbCLN9mLmYaEW2HSsEHYLhpzpxhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCICPfj_hrk9R34bePOMR8VtGLbkJdVzZpB9lvZgoNgBzG0QQTGDjyCpOrGMWeK6FY4zYdQSNPbm8ZQNjfuTwhkamEL6V0fmc_qRC8MADft63IVBwUaMuva2UKqHpfQs_TOwjwZ2Ygaw6WMAWRi0MXJXsMSWGzMmGDbp4rj7x3UY0FsxNG9FyracLyL0MEkGVXAX6UH-y2zLeD2jQcxbLgtY6uC2fCWMMq6JLLh73Paf6jt0foWaDc-Bd75gDzcMg_MAHpMlNqr3Q6gFCltxQ22Ni70O44mcz0JbylJpg12FGK0-t0ZbIEwH3zS7WfAGDq2WYVEmJyHjfX2IsqomdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFuAIgq3Lu1vDs4UmWRmI21OLGPjKu879u7cBM4Ntz2ECGFuXbr8XTMHtCLUjgyu5KB2POT34O0rciSetUKQjHhm1j5uiI7x4lEzbFyaWfCFPKHHduZNu0ldiCSUet4_IB9aQIQpIkTremNWMOpKpSQNXOa9jtx7_FtoX8lu4o4cvSrqsEEq90viRKfkVvLhXzmzonBwews1grgaXHhCHo0rOMAp_sW62fBeZQaLwpPzHsuN1Kc1YjeQlXYtjeF21eb7qotLi6_Z4_pCCssqn090yyZPIlWpsZTy1MMS8VO5i46-A8MSJgpAFNHZMkBNF6SgPPk9Nd8kDQWls_7Lsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=VelNgcpQ8JHMXp6y0KK91sGe7cp7svno7rD87UJ9BHgtmL-3VtoDoFp7rEc0qEPO0QR94hWsNIPdBZy6vrdfDw6eRrrKoocqeXcKMY_bWNLLTKXfSDejInCUDHy8Ze4mDAVuQq3Y8y5z6RVho2tGRTPsvpj-t8neA5I28yXy0ggLrkW1SLNLvVcYyHATYnE7gVhq2HcraHysAGJRHhZnxYR_gmyhXThdMZjjjYsHRbHFV2-mgK5ALqqe6kvY9SjNSB-AWjnnA0q3n_JqNkqX6QRjdQEQVtUn73PhNAYeivs2JKkxEGuViy6LVviPt728LSVAMelrcTv4rKZ0P1jiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=VelNgcpQ8JHMXp6y0KK91sGe7cp7svno7rD87UJ9BHgtmL-3VtoDoFp7rEc0qEPO0QR94hWsNIPdBZy6vrdfDw6eRrrKoocqeXcKMY_bWNLLTKXfSDejInCUDHy8Ze4mDAVuQq3Y8y5z6RVho2tGRTPsvpj-t8neA5I28yXy0ggLrkW1SLNLvVcYyHATYnE7gVhq2HcraHysAGJRHhZnxYR_gmyhXThdMZjjjYsHRbHFV2-mgK5ALqqe6kvY9SjNSB-AWjnnA0q3n_JqNkqX6QRjdQEQVtUn73PhNAYeivs2JKkxEGuViy6LVviPt728LSVAMelrcTv4rKZ0P1jiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud4PDjgo1oaNF9K_sR-JEQEDri0aCocYAGlT856Wp5HuxQtt9k0DEZqnikm6zZ7vRXsIBz0Hq0GJO7j2Nqk5_rXyajaapeIkfCWFm6-escJBfcWNeDsSG6mNfEBCHdTF-Kp4PG1ULdtxmtQjWxc3m2XquMFqn810t_deDVTel1E6tWqh51xG-ujj03O_3POkFwmLERnkXVI8YDHnFJ5PwNeGK0_Fn3NhrphOnhKM29Z_YTjoTIgImi2fP5CGH4RtubQxxZ_1eWSvW_Yzk0KwLjhBPzLgWd0xBPRVXPDWgAgFiamkiyaT9eoMoSODdJVM-FTGxN1vvRTQIv7bLvB7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCky_KPctwQaiqZUONhx5pUbQI7fMH23rwbG4uHOb2Msn3WiV8nUihVt8rdOrhx46CquMVU5hnaq6F1KKr5Ce6q3Q89GIn7FsIrMEpncpnHDUpCOY01Jzwy0UN6Qn3LyY-PPGuPlvZjgkRPwwG-QqV9gHISwDEzTC1bGC5yljBpqm12mUr698xwC6MMkceOkv9NGEmm0yhsAxlpAzGNKCK-5_PO_JhvXON0RN-h9A7gfxLHiviTFHpNqEOiSYKIyLQdBVRYSFhPSqV9E5MUtgK5PzrnwTZ0mzWXlckO3zw5AN2bXaEFdlf0ANmyvN3Fd2N4reB4W3MdaJ5fFmdW8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqhfsMitQaCAED0Q7Dp3Lu9aM6zfU1rZDVQoJu0CNjggbcxR9ThztFMJL8f5zaKlcqT0i_nUkoAXFbovAvCmjt0e05CotNJtwtJy8Kyy3NypLlGmQOVtgWKppXOuyPd9Qwy93-RvdFfmRxlnGAKINrWgb-VvBVvWSDJ79wQvDvVNeJp9M4nYzG1Vy0ZrrAtW3m2LWOu_qm7J_VRJ0XDfgGx063_lwkRsuqUzv8HdYJgzJZRVk7jUR7GEYURw9TjiiWIYbk9r8QxjxhtJKYAN0g_fQe1B27d7jDDUDdnefiAg8CsPg_TUFdPaITmX85nlfmaasBYxLkfw3hI1UpQXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zuu2Nhd1UmviWhBmn0j50e1dsb1IPRA0H9D10hcFvXD1q4D2qGwiVvDlGYbys63yuIDLTPV6RzR1bwh8ER65NjJNdGpsPu15G3F-zRORJO0Y6fcjEvCOub_1t_SnPgc6PWALCEuYRfnmDUcCodjWmntQkDorYhZAOwc7JOpKEKCs4HtDV2taJIpbJUJRc6zyaz2xOhKuaOwDOlwjXQVr7iAylOgV-jtLbhvEPIn8Passfdm__yw9TTlnnikVmQNe6yENKLgd4BzWjFJPMY0bHHlzhc0ndbMRR7vkxlNdS_aOJ0jwPHKtZQ1M57YyBXx3seDSSw6jGIFPhCIoWEIXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTOganI_vbVlIyUzJFqnwho0b7-vxUiqV94_ZEBjfEb3OsNTthe4adBxnr7R0Fb_8ciBZ_ugvM2QgV47kRan65JozL0R09LKMBrS4UfU91xCLG3gGyy0HW1gFW3PUuEWyvHdjzXqKZ0UVeHCNVCdEGYpcEOTRKUdtP3mJrl9J_iJxYYU9iJFe7NQSSSXYYvWwCwEnspx2KCSbONxdquq2j9Ftn3GCrcT36P6JYj0f8sGDVK2BU1wal6z-9fn9-CQNcBQaluk20_TmUdMKW2T9QL1QF4Y0OegeBoUhKAZEOdNKusn5-SUB-BlKsAhkZBuqjeI2jFXFSHNu7smrHfEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=bZDDxvtqb2eMr-w2PhOF-Wv9iRb8HTFJDpPNOFcp1gRNmZ_He0jcbeJlggfh4eDv7SesYrGC7bYlKgpxAqKHTbESvdD6CM2C0Qx1JtMFEp7VXToOzvu969cHFZW9Mw4rcqS7MKVcQv_Z7EzW-cZ6iqXnJr3DcFZpI6rCQknfFtzIJJxWX9iMgKJyDDRPL4z9cdViKzDy1DJyb95pQzyUwNRbOLCpu4uHSzeFBaaK-IWfyhWd6nIF3Gw8tbIkgYwI241zCeZfbJqeJmPv5ihZyXgR2I3zoTqqmJZfT5ysoFrjO4IIdKpDikK0_gonwMvYsl0rwr_lO3hU1Z7-6BqcWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=bZDDxvtqb2eMr-w2PhOF-Wv9iRb8HTFJDpPNOFcp1gRNmZ_He0jcbeJlggfh4eDv7SesYrGC7bYlKgpxAqKHTbESvdD6CM2C0Qx1JtMFEp7VXToOzvu969cHFZW9Mw4rcqS7MKVcQv_Z7EzW-cZ6iqXnJr3DcFZpI6rCQknfFtzIJJxWX9iMgKJyDDRPL4z9cdViKzDy1DJyb95pQzyUwNRbOLCpu4uHSzeFBaaK-IWfyhWd6nIF3Gw8tbIkgYwI241zCeZfbJqeJmPv5ihZyXgR2I3zoTqqmJZfT5ysoFrjO4IIdKpDikK0_gonwMvYsl0rwr_lO3hU1Z7-6BqcWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VvcQ6lkLUh92nHNwpG8oDoZz5nv4forX_VGft7kbrQ-EbjNXQbAKqQ_Bqi2L45Q4_89P3p7Hjx_P34Wk-zOqI57_aianvWaZkAbwQjE_zKFxYwA948kZX9kqJuX_jyo6uTooFeFHigNCC4uxxv4sDmYD9O0k2B5l-a20hLE34rN1jIJblhLZE52tq9GgOM-gY-PjS96_SMc6UVlQ2wRzie2_DgRmj4Go9ZX2lNu7xmjDeLrKb11PNeMiVFDgZb-H-_IK2tyrQSYXcs1C_q3wyW9EsWCJAn3x-HDJJJxdTOEChvBGmnnIhAuD4pgn_FRXtIm7msZVK2neWVBYr0bEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mBYKYV3n6E0jg3Gl8lZs44T1FXJkvDv_Vu0ycvQaPEekPpQb1ouT5jZmK-fwECVzuza6sQm--0HYxhCV_maB5PX80G_fJY82CF482G7x1gjC9DckidRuMvekIYycoASGjfMWn5-w3x5PrA29ZXFBbo1bW6mnTPtBlTSZSTgr_TuoRNyINIbf8b5qjwFGZgLVtw1PAE33B0vlSNGaIWwNGoAjPjZoxiYeBDf2Tma3RqR4moaEmW4q6_0itlGgOaa2c3S8XD_9J_sNKSD6oKnEWruYVXbffQbMQGGtnb01JMbIiQnwQn5o85t3-g5QJHuf-3DfrIb9yCgmN4rJSGNz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mBYKYV3n6E0jg3Gl8lZs44T1FXJkvDv_Vu0ycvQaPEekPpQb1ouT5jZmK-fwECVzuza6sQm--0HYxhCV_maB5PX80G_fJY82CF482G7x1gjC9DckidRuMvekIYycoASGjfMWn5-w3x5PrA29ZXFBbo1bW6mnTPtBlTSZSTgr_TuoRNyINIbf8b5qjwFGZgLVtw1PAE33B0vlSNGaIWwNGoAjPjZoxiYeBDf2Tma3RqR4moaEmW4q6_0itlGgOaa2c3S8XD_9J_sNKSD6oKnEWruYVXbffQbMQGGtnb01JMbIiQnwQn5o85t3-g5QJHuf-3DfrIb9yCgmN4rJSGNz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=cjvxV4rn4wdyDLFdGsfqaxWkcL8-VplLj0Q2IvI74panAYi7S5qwAENbhcI7BfNBgOK0IZHLVqRjTNa1ZuQrsAud6qWHJg9lGrzXODXZfvh-PrOrsrqRQuG5BK43uWGJ6JVudS0kpiFwuhUU7-8rB8imIZp3kCwkr0n9EyOAxRpBim966ThSuKuUiG3szcw3ogFDtH--nv2fdCfQZS3-rB0RNXNbaLvmzA1Olk1-cOb3CvhgBU0j67n4us0i-fzFUJu0Ua5Oihb8WUhMd-7ySCcF5FB6wYOu0p-CPLUJ_Ju_AYLNN-qIw51m1EP7kzA7RAkSAVsiq7XGNePT5XESSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=cjvxV4rn4wdyDLFdGsfqaxWkcL8-VplLj0Q2IvI74panAYi7S5qwAENbhcI7BfNBgOK0IZHLVqRjTNa1ZuQrsAud6qWHJg9lGrzXODXZfvh-PrOrsrqRQuG5BK43uWGJ6JVudS0kpiFwuhUU7-8rB8imIZp3kCwkr0n9EyOAxRpBim966ThSuKuUiG3szcw3ogFDtH--nv2fdCfQZS3-rB0RNXNbaLvmzA1Olk1-cOb3CvhgBU0j67n4us0i-fzFUJu0Ua5Oihb8WUhMd-7ySCcF5FB6wYOu0p-CPLUJ_Ju_AYLNN-qIw51m1EP7kzA7RAkSAVsiq7XGNePT5XESSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6-lfUoQSTysTz0IiojmVmdHJBvwEimz5v1Au9zjAopawr42dbr2QirDmTV-XUJXNsBKtxpAMoM5Bf6bjNTlUGoWKX9yxB4lrLvdidFoGzxaXVY1T_AeY-E-sIRgaLSNtznHDmGS_-OpWXSMATtNC7XmDX1Y052jeDeHjVIEYN7UguHOTbKxCQThTw5uLo-vPELqjSwKdlzXZ7VkkphorebVvZKCGcF9cCrpP620PnAe8et5uVhIK7lhStD3iOL7mwayXkxhvimy03illzCPj-Umv9Kpkg0Wz80wj0F2AumkbNCu769fPB0cFUNXtttFVmDBlujvQqNQquUmAO3g_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgbOsCbGKrwqbIFZcX1HEMZmEaqTXXtEsquzXnDr-_CA0ox0oFh94qB1K8o-ROH62jdFDXzKNM2gKaJtTUQkfL8nKdhUMniK0ipvrYh1ho-j0evbA7atls9XrOBWWAiNUpQfpV9NuvaM5snuDHrh2PkruRsLet8svLTm809yXUaSLDJFN7TQBdC2AO21zTK00ykcaCABq2vS7nZwQcn_UYc2Y41BbIaCq7x2DAVxYK_xTCpU6TgUYC5EQ-1y9nBYySzFj3etTljZElLkPGMycdzsYFpECupZUdAcZ-tOiziCHRCccpJUAeUNuvnabCoG6tUeKce_N5muKB15ewP9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=crIc_38yyc1W3Ij9pw4tYteawTN1k-ONwaWZ_j91Hb9NWp5VQ-XuTxKfPTm8xo81AQN2Ena6vY_CJXgurOUkvRd90w7r9BB5Ta4jGNCMxsUL09vsJpng3dvXafJb1LYQUnZrQo6DHqKTsNrGOspDe9duQIHPBkG6Ocnre3nSCPxLQaS-QVszIohlMdIICIB-_-fn8ZzX-U88M-t_2C-HcdWyFKW6pjcXHw2nI5l94_aZb9pPPwJI6n-ETNLTCzJUMuIbzb4wpkaL9AFrlg1lsGmmTZ1Bw2OZwlaU8_MD8uvA_S-TSwjOt0XyUKySMttaxwaCU2ZTI9AC7RVG2v1BXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=crIc_38yyc1W3Ij9pw4tYteawTN1k-ONwaWZ_j91Hb9NWp5VQ-XuTxKfPTm8xo81AQN2Ena6vY_CJXgurOUkvRd90w7r9BB5Ta4jGNCMxsUL09vsJpng3dvXafJb1LYQUnZrQo6DHqKTsNrGOspDe9duQIHPBkG6Ocnre3nSCPxLQaS-QVszIohlMdIICIB-_-fn8ZzX-U88M-t_2C-HcdWyFKW6pjcXHw2nI5l94_aZb9pPPwJI6n-ETNLTCzJUMuIbzb4wpkaL9AFrlg1lsGmmTZ1Bw2OZwlaU8_MD8uvA_S-TSwjOt0XyUKySMttaxwaCU2ZTI9AC7RVG2v1BXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0GIDEkFLaq7FhPHwjdjE0-ggRKSKfXxxTdPt3oZYbX4bWpzGcq5jXLeXLiW7H3edELgHaRkCuBoCb0uiN1mIElge1RPM9U4rRqX-8s9CN70QDEJCFXsap2ReGcn1V75AtK239Yj3iB8BHIzMhzsWjtHH4NGPTC2_ktGxSLhs9L98HfzXf2xiukz24DQfGJiaADoiZhgCVOIDsMIYrZWVchT3YKQvYTbcQN7IOofyiYNLJx6wOM4ZWE7daIQW_3fmKXGIGHF541Fx0jjaGeaUeu9AE0eEyNwYSeh_yayBc2_tMnxrlpl_W8Js7ljWcTKG10eZdfVCX1RdTUdIbvv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=S9iPchHFiUUvdCbeBt0fcOaSM28Rv06q4iOBIGtccvpoN__Fhjwxl-0IHKXCp05MnPvi_JLkVX-A4fTE28L4qYUT15nsKqCdvuNsaWma9pE1GArHL_QjYv7L5l3WTcneK03rCaQ5USg2wqJeZaC48hBoibhWZRy1oVYSwZS5TS2xaCSKtjN1S-bw7YsZG5As7cwS_csBeK2tQUOITZEUVRKrJp5d76_Lbb4ln1gaGRICnaKyaThg1WNmUp6wSapZrh1rRveLb1yZAT39dthDnPBisiBFCIpwala9tLNPdY9MndhMNYUGVW2QWoDmtrrFwh7udtmSnkk53eXcsth-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=S9iPchHFiUUvdCbeBt0fcOaSM28Rv06q4iOBIGtccvpoN__Fhjwxl-0IHKXCp05MnPvi_JLkVX-A4fTE28L4qYUT15nsKqCdvuNsaWma9pE1GArHL_QjYv7L5l3WTcneK03rCaQ5USg2wqJeZaC48hBoibhWZRy1oVYSwZS5TS2xaCSKtjN1S-bw7YsZG5As7cwS_csBeK2tQUOITZEUVRKrJp5d76_Lbb4ln1gaGRICnaKyaThg1WNmUp6wSapZrh1rRveLb1yZAT39dthDnPBisiBFCIpwala9tLNPdY9MndhMNYUGVW2QWoDmtrrFwh7udtmSnkk53eXcsth-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6ce_c0TJL2aKGi2AicEK0hlq9wmpkL5rKsuKo8OWseLNGyE4h_Sa0RwpKR2-0l_6XD8oiOO8dG-HZonDnsnOKaEkG1Z3hcu2No1kXQYMIrYgS5OMLC8KzQDDxPGWdOnHc6OnVMUo8cbm5n98zxxhfBwSn_OIMEvwm2kQeroCfYR4YO76gYyuDB_ECXJZ6hwWFKWyzXjPmAzOUbmlvP8Hdx5Bum-NWAqrgfyDaiMW-581ojCikRzQXhEVse2-5zNQ2ZEXKIMC3k9gMrxcPR7jmLHBYS2-yh4GM9WhCnNkbjrmY37nfAoi6R2hhpcImRkRE8l9SA_QmPw5T7KXx23lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUUiMLV7JvgNq6mHMq5lkLX_9mr_D40-IouwwcRY1heaQV3IawRiOspX7Hg-LlmhYAN2lEsWukeII-9EWUobjmbum9s2kXuNGggC28wWJeS_c_7fVfiwmsjWRDD4fuovcQSGsyIjNNp7DSxaIf-xktVwwxKKMehHGeijnZ-JcBH8SE7mZVxYHJEBspTVa_FGvufhCm2SDtkQ5KFM7KpL8k63dZa5_e8L3hiQh8r9ID1y9HKk89pcDX1Y9eR3rzlxDjuVPCA9X4_irwEcRibARbrtk4av8JIBXM-w2Os8EiMpJVct062dEUtBPHoK4OjbwTP8M94ymWY6GvlCFVFAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DZbzTgcpu3Su5H9rde7iy6JdTyhE43RH_otRnGxeAuOiKZad6MC2GNubSQtYGihkIczNr5EyrwLfiEuxMoJzqud2ZQDTBBvPLK3lNUpe9T8eACW9gVieU_OM_6DtwjpnC7p8tpIryGlAuXwxs7DDXPdkGsxv0jTzp-oMszKpqE1Dqj6Cw-zEcorcrHZ8whAHKKCyROoiFHWR_L0yJ9XnFDmyr0-De6AXPfJIemU_HuqKMU2tDyzSHTmOntOqDLZnAbOlMGVay2g70-lGi6VOOtAvsYlzrd2u-Yv2WrwsEqJlC_EJyeAoXGb6ke9naBpBUaizFS306xNI_1wcmb216A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DZbzTgcpu3Su5H9rde7iy6JdTyhE43RH_otRnGxeAuOiKZad6MC2GNubSQtYGihkIczNr5EyrwLfiEuxMoJzqud2ZQDTBBvPLK3lNUpe9T8eACW9gVieU_OM_6DtwjpnC7p8tpIryGlAuXwxs7DDXPdkGsxv0jTzp-oMszKpqE1Dqj6Cw-zEcorcrHZ8whAHKKCyROoiFHWR_L0yJ9XnFDmyr0-De6AXPfJIemU_HuqKMU2tDyzSHTmOntOqDLZnAbOlMGVay2g70-lGi6VOOtAvsYlzrd2u-Yv2WrwsEqJlC_EJyeAoXGb6ke9naBpBUaizFS306xNI_1wcmb216A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=VQyEDVLj6U2emgwgSSY_Le57Gdn9nO_wQxU9r4B5P_L_5qkJ-8VKLHryGf5UTHoWUq24YRkVjWC383bgX14-TrrgvfWDgN5sLoQpTuVnIB1Z7iMMeTXb-d81ggheGuDn71vHdmaS1XDLY9EMr9PYYRd1Vqnx0vKTlL47uRSI4iCa4Nk0941vT6hFPw52MQcY0de5AMfxagEy0qppxTU4JyE2Vb76ySgBMEkgihnZcmxKoaPzJQAbxmz7qtoccdjMSBkBl2BMnKPV1wO4cyFaVV1RpEIOmjtOKjzlygzN5cedunaJZMqKI-i0z-cjBotg4uuIxMSJcqFSEaC-gqrfsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=VQyEDVLj6U2emgwgSSY_Le57Gdn9nO_wQxU9r4B5P_L_5qkJ-8VKLHryGf5UTHoWUq24YRkVjWC383bgX14-TrrgvfWDgN5sLoQpTuVnIB1Z7iMMeTXb-d81ggheGuDn71vHdmaS1XDLY9EMr9PYYRd1Vqnx0vKTlL47uRSI4iCa4Nk0941vT6hFPw52MQcY0de5AMfxagEy0qppxTU4JyE2Vb76ySgBMEkgihnZcmxKoaPzJQAbxmz7qtoccdjMSBkBl2BMnKPV1wO4cyFaVV1RpEIOmjtOKjzlygzN5cedunaJZMqKI-i0z-cjBotg4uuIxMSJcqFSEaC-gqrfsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXboKQYDYoNwEEkUINqIpwlP93YnLLcMqgqqrrdcskgNH4GeuP3n6K4WBcFrnvz2Gmoe9ABKP_zHdnYnMdqpWZ9oagDdFf4aNDE15_aOcENcpACz3eE0nCoYlkfbOyrARAynvJ-Le1XXvV95SyGhlEusEOkeRFkm58CqMw75Rx5FZJyqjdtcNxCDG2oAUrKCMYNZSHLsNCimG758mjnaaypdusMSwj6WQATcE7kzC-m2ikuRsYW2QyGrSblNMU4CKOLPSHN8dVxqFn4qbtgbCiP6nCOSGQB2LS-OEQIjIA9c-LklkS36u-dIFhw1yxd6I5kgTAj-ThR8d-LISCKaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUk2q6jgSetWokVXGs_O1YBx4ziH0Qc6kG4gAcgY1qatBB83k9ocBJSDD3EFrNkMmzTGcuqV7fsMH_Ht61I-OCw8m6XsIyrsH0Bwnpy5PHA9vr35Fs0VLbpBJ_ZsUPAB4W67Dp79R7-prDOZZU-Orw6LdpQqRzzqH7NCd0Vre2OZFKIMarmI6cyiQeQO2xJts2JghGUFb8tqfp0tuhnkEBJXHJhmwaXqu-WsS9yYlRSJbyGtxegBaW5nB3B0fbcAqMvTxQXhci57c3knAMk-dNLUbni7ZTnoj-Q0SfS0foiEb_fIS186C83WqQTzVJWOCQfJVMcOLgEi6VvdxeBBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auVwO1Dk1nkV2xA2HpN2tTHJQIfRKCan7c2lsEbxHu73aYRWrsKHKGciksPYrzXRcOGtH6K3jvXKbdjM3ewXGxFB76epyctXan3ispK14YEU02O7Xndj3NW8_PXuUxTJm_SYPkUQAiE8RsqzOy2b89H_ArVBXjSB9Rh9ZCKP3mb5zXxNvWI7kbCAr9En1xkwf8zEI1Rr7buuiJliSBSCSpwgs8jJeZWk9KeHBgusxndjzwf1efnp6B8hvOeI9rXKwm517wBsde5qPkNnfBQdC0hEvfKeXqCP0bME7iyqBv0k4_xbFotKfDf4Dyz5BMdOirYN2Z9-39pOonHsTDzKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=S0Di8uXu1DLgOk1vy006LOM2T1E1cesQpT8lvpks3O2hv1_pVl78bSxC4G8bn9qg7jJrOnjJahiXeugSzL0FawBtQBCfNXmGF8JSzuODRCxk1JH839PcPG0GzwTNDp-61Lh_DcxsnDPAwit-0nq08GPYgwKZOErqicryTvzOmK7SXhkYOQuOd9lXKXMi2zgNCFQMRbq2pKaiARhj9FxFWGNZKoWC1Niva67OfLF-twa4JflIcZ0KWnjXdezU8xAdJH1pDhMwShorV_KVmkcQeVOCVR0RGTFR-_kRh-jdPOdXa6AA2Hauu5Xqs1ruAYsGTsTX-gJhLQXp54fXha0Kog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=S0Di8uXu1DLgOk1vy006LOM2T1E1cesQpT8lvpks3O2hv1_pVl78bSxC4G8bn9qg7jJrOnjJahiXeugSzL0FawBtQBCfNXmGF8JSzuODRCxk1JH839PcPG0GzwTNDp-61Lh_DcxsnDPAwit-0nq08GPYgwKZOErqicryTvzOmK7SXhkYOQuOd9lXKXMi2zgNCFQMRbq2pKaiARhj9FxFWGNZKoWC1Niva67OfLF-twa4JflIcZ0KWnjXdezU8xAdJH1pDhMwShorV_KVmkcQeVOCVR0RGTFR-_kRh-jdPOdXa6AA2Hauu5Xqs1ruAYsGTsTX-gJhLQXp54fXha0Kog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIbc2ahx45WjcyP5ZLbSW3ozaOXH4aUZnLws5XrOb25CnzbA7qrsP6enHqb0yRfYFuCdC8KOl1g7YT5rRzvlh1cuWyWDeiADAg7V99p3TTcbP3h2C3TlbOCHu74DJUTLFzuq10A_Grd7zz3YlWmWuG1fWuc64z8aPswRnROUiT-V8iH2gpV-bBJDRAn27SvrwW1vpwznjqxXySIP0ZWoKVTJSGKjFNIQU9r6YFUTSpSbm9woD4n0dwc674wCoBBRVL6seCm7YNwghDvkE565fcNPWWV4CO3wYOpxQGUkH5lIF3LFv4l6kfXhhcPzVmVm2eYLIPlU_bD5hX-VUQWj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG_YnTlBMsk3tnVMgfLB4sye082S0YrIfEez5hI2pdWKznIEdXp7CWJouKpqtA7UhtHMLOwx4XvPBoMZmfJSg-8B68UAMX53dOgd1luzmYBqhdZU124ZVWheTBfbAcnEuCIPqxOB-cgre5K_N8godO9Sf4sBVk4s-xHjGKQ8g5Vu8ugWUW2ocdHSTFnrkxA1fIijuRsC3IpQjeUWYHV311YQFjaoLRkH2it6j20Ax_3s--GcsS6L3NYleIpi9V8O5-0s2BD3EkDFqwPrVkRxKdCm2KFYnbq5GEAOxoOkXgjOUwUgcxuhALze5HDP-pJxyu1WG7Z4W2CYzFeXzkrjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfv2UfjZ5kv60-Z1a4kzckVM2uNwyJ8NGJ08zi-OEZJHlPaVyl8dhM-HG2IBto-VGPGA-_Y9aZPDBZ93IBHabfC4RZlkldfpjCzS5CHM4gWgyPUHkQ6RDk7JZpPZCn6bRHBpBclZPAY3sPWWcdWBbimqBWzWowA-W4iqPYnAlgXcK_41XVpt3MThOJk_2TXAXkYtysAxIY7qfTorvgKncOYUwm6xvCyZ5M0XYN15WQ04fhuInxYNSUrxihxNp2ldWBR5SjKbM776jpSUaFcwEXvHJx20kY_BjSd1donRtGkrL4AqxsYozFct4KoijvceLUc0q5_gXDOkAPJJ_PItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7tIXM7rmIXsWwwXt3HiFKxrYots6PBM4yfYmFsz2fwlZZ5mjVqjv1lTnK7r25-r8k7R4n7F2vNVxsf010WjnUiq0pwFH34Szn8Jy1ek1zpmiUrF6JeafgY5iouJeNMDEM0-XZFcUX6ozAmPIM1vfok-Qxzeklt8QFqXRSRBlwazuMadnAnSqxreswMJISMcT3Ui7iuheBd2_4diwKZWUrL4yzk1-X6aJKGdj8MfP_76Zl_BCQrfuatxbx5O7mTe_Aq6Xs5_2cVbE0nFQ1hVd74AwSl_iV0nKM8VVynaJX7HVygjha13FJ8K4hPVDPr6dkSaFHDdvb0r9iOsGc77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DO9la3QFKS2I2OdS8O1LRv338BgkqH56ekmQMIX1n0lfVIyVtjzbBR89FkCyadOi80otwh3711NimT6xJMl8BNpxpwKcnO2y41ddvpDOKZAuQZ5ntNiOQU6XTAGsrVAGeAlwLQD33XhdVqBrIIUH-mtwR7lpsD_joi-voe9kHEr-emGBOFRjQ51FxIwXaMmOAtEIJ3Sp7P4de0LgfUR_UFYZ-DmxCu4aFARjN5C3eOiGL-eUieo1rXrNDQM8lMTdPyjm7WVzZQX-6wY5tm6aWKds2h2M9PYprpxesoBKkhVkhi6_Ae46KJNWtrrtBY5Y-OzPnMLmLqnysQV0r5PtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DO9la3QFKS2I2OdS8O1LRv338BgkqH56ekmQMIX1n0lfVIyVtjzbBR89FkCyadOi80otwh3711NimT6xJMl8BNpxpwKcnO2y41ddvpDOKZAuQZ5ntNiOQU6XTAGsrVAGeAlwLQD33XhdVqBrIIUH-mtwR7lpsD_joi-voe9kHEr-emGBOFRjQ51FxIwXaMmOAtEIJ3Sp7P4de0LgfUR_UFYZ-DmxCu4aFARjN5C3eOiGL-eUieo1rXrNDQM8lMTdPyjm7WVzZQX-6wY5tm6aWKds2h2M9PYprpxesoBKkhVkhi6_Ae46KJNWtrrtBY5Y-OzPnMLmLqnysQV0r5PtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xds40aBXmVh28nimyTklLVJWDk8qarnYgov0M0ghMH1U0BWT2Jh8zCWHqJDfpVAkmV0_k3OoyyZf3yUjNAVPO5V3zQOmMashGMN8pzJI46M1mkb8K8u-qV2pWldUxJc802oLzB9tcfEcWNB-xBtVcWkD5pHyIELB-YmMiij94RBEWEeDaHCSZWviO_7rgdhvfQ5UKUXgneZG5iKZ1Ff1ul6-FKLs5MMAJBLfEeZkKbi2vJDabFkxzgibIP6cH2ixlYzliTVq-Hf9Cs3g5Eycbo5mrenYlJaqyVE-nlvsqsP01UNW6tePKMv18n4CCifrYBthE2fCw7b40ptk3owAgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=L2arzF7Q0fDwX0uLwYWvfavtScCFmPJeNkAlAFoJA-tKKceSVuic64ZXjmbMLRiqp6UiVNIH6qEGzpfFolSrf1aDPxzk6NV6LJgHtLdurtr1iryGmXXqFjTRez5OJNhIBEgQSQgmiiW7uFaMszFQgpfxyzD8g4PgxPw7Cl3edNV6Jln-Ozg0GFlviZ8M8DyG02Tdw0_t4r0WMJ3sreKY4Dvtmy9qHA-zCk1E8ZwPmisTQMNz6KsxFL6o4GFYfy5PL6I7RmGuNPf51596HfZZKuX5lTDPBvI_ge0gytnzkWoq_H4LKVAWrZnnWg78VHwZhYWvhdy_uN0BKdJ42GvJGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=L2arzF7Q0fDwX0uLwYWvfavtScCFmPJeNkAlAFoJA-tKKceSVuic64ZXjmbMLRiqp6UiVNIH6qEGzpfFolSrf1aDPxzk6NV6LJgHtLdurtr1iryGmXXqFjTRez5OJNhIBEgQSQgmiiW7uFaMszFQgpfxyzD8g4PgxPw7Cl3edNV6Jln-Ozg0GFlviZ8M8DyG02Tdw0_t4r0WMJ3sreKY4Dvtmy9qHA-zCk1E8ZwPmisTQMNz6KsxFL6o4GFYfy5PL6I7RmGuNPf51596HfZZKuX5lTDPBvI_ge0gytnzkWoq_H4LKVAWrZnnWg78VHwZhYWvhdy_uN0BKdJ42GvJGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=UOWDNydFrel-MVX2KGq3wfrSE8TjDDekxKWF4xfMq0mxCQuwn_SVrvxLAEM_IYo0NtsAdnxc0Cq10HThrr6Uyw4HnEWfbwg3pppIPEi4n3rpL1g8Gu4Ptw15b_l8jx472TFtUaYlrXkNLDazidnfSbcaD0cTx1BQO50U-vj5-gi15-wDFxuk3JvELusPRazjAzgNs5Cg2GFg1Y0E3FSlv4gWzIKY8L7rtUUdNpz_sTI-fUdeHbMW6jDuL6ZF5AVoeERBH4Kj55kXn-8zy-zh-XeoA4IvdmOzf2kJiBnl1xxigtk-GGnWIgDLazfnSTGUBsHohehTEVL9_kEjknnHpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=UOWDNydFrel-MVX2KGq3wfrSE8TjDDekxKWF4xfMq0mxCQuwn_SVrvxLAEM_IYo0NtsAdnxc0Cq10HThrr6Uyw4HnEWfbwg3pppIPEi4n3rpL1g8Gu4Ptw15b_l8jx472TFtUaYlrXkNLDazidnfSbcaD0cTx1BQO50U-vj5-gi15-wDFxuk3JvELusPRazjAzgNs5Cg2GFg1Y0E3FSlv4gWzIKY8L7rtUUdNpz_sTI-fUdeHbMW6jDuL6ZF5AVoeERBH4Kj55kXn-8zy-zh-XeoA4IvdmOzf2kJiBnl1xxigtk-GGnWIgDLazfnSTGUBsHohehTEVL9_kEjknnHpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtdgQ_FLajg_7UmYXuIBU5rawcdkNNaWDC59Cy8qgXwx0hb9qxbYPAXNQi9-yLAnfu2MAbD1hDshYgXBbUO_ijaszyO6rb12M3sRE8mxAaqs4niIkCaIZvHZsWnOdzC01dWlme6vq88xLMNuxr3VXI2KoKTI7vS0o6-dhXT0fHSJxVKQK2YqIxseg0P4OgF2C51P15XSD-XB9Enyemodtgew-NrUKSvabk7AHAsq1BzkLBgWqBX7VE2LfwvniVBV6r7Am8M4njaM25moiAPtFrrbjmh2mHPuUn0K2VU7Ez_ekyivK-vymLf7aPcPmbyilFGNu6ha9IGInGtoSsRB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=sczI3Q2KFN9P6txCr6O3J8QYfjAoh5qqrc0HxGP2eSvQczxFClgrRkXO0tiLo3R2jqB20PrR_xkbhvMtSFXe4xjpiHnLK2tuzti2zmuIMq4v8PxqBlnBtcXIW1OzGxeul3pH5Wp5O_K9xTHr2OwDZZUYUWQ38dW6x3Bdayi_S4ret_1WaNPNp9g8ezSjwFqio0vg-FM-ebU2xJB9re6lxa4gxe-bZlzWcT1eN7eTSpZEoHll1hJQMTMHuc3vIYImerOaUwPdVsRrwTN8sn4Kicr1kdD1rFvI4OIZtZL8fKw3IAkhs7ws69VAVAVBA_pHd6MYxEaPxv8xT-Z1inEk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=sczI3Q2KFN9P6txCr6O3J8QYfjAoh5qqrc0HxGP2eSvQczxFClgrRkXO0tiLo3R2jqB20PrR_xkbhvMtSFXe4xjpiHnLK2tuzti2zmuIMq4v8PxqBlnBtcXIW1OzGxeul3pH5Wp5O_K9xTHr2OwDZZUYUWQ38dW6x3Bdayi_S4ret_1WaNPNp9g8ezSjwFqio0vg-FM-ebU2xJB9re6lxa4gxe-bZlzWcT1eN7eTSpZEoHll1hJQMTMHuc3vIYImerOaUwPdVsRrwTN8sn4Kicr1kdD1rFvI4OIZtZL8fKw3IAkhs7ws69VAVAVBA_pHd6MYxEaPxv8xT-Z1inEk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=g_tiN1cw3SbOlORDsWUu3UzJ4Qv2C4HgaNG4Ob5ZHtqkLoQvTpTt97PsAk5PWeokqtpx7cFYlR2AGv1ATo8AH6sc6lzRNOqOU86Zkn-Nb8A9sp4jmvkooL03De0ndL0jH0YMlFBZPeIlfHq8B6thjOZq8hrHzZEouiMu9W7m3Y1L3fDhor6xxrMR13Ph5k7RWvqrYWqlQwIp_xZC1eVjGxHCzJezqSc6P4dtBqFfgOzRqFZ1qqkLTajeqUv0n-h59oESGCxg3tllGIFGUG3Swdsn2sP8j5BiV7s2PD1uO2f9CtbChMxpyA7c7qy5aSFqz4TNZlRTsBgYBBloIRl8BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=g_tiN1cw3SbOlORDsWUu3UzJ4Qv2C4HgaNG4Ob5ZHtqkLoQvTpTt97PsAk5PWeokqtpx7cFYlR2AGv1ATo8AH6sc6lzRNOqOU86Zkn-Nb8A9sp4jmvkooL03De0ndL0jH0YMlFBZPeIlfHq8B6thjOZq8hrHzZEouiMu9W7m3Y1L3fDhor6xxrMR13Ph5k7RWvqrYWqlQwIp_xZC1eVjGxHCzJezqSc6P4dtBqFfgOzRqFZ1qqkLTajeqUv0n-h59oESGCxg3tllGIFGUG3Swdsn2sP8j5BiV7s2PD1uO2f9CtbChMxpyA7c7qy5aSFqz4TNZlRTsBgYBBloIRl8BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4mDP5v2AgeV9SFdpkEpTLnRFfOdN5oOY8FtBbCid8pUCz529k346MxXOJZ3HM7SsieaHLCYovm5AOq2DOST4ocYDf7d4IZ4mhsbNROYY0srOrdYE4wtwkT8QLczXJ_4V-cPCXBCztvGWqtGPJmbWWrLk_7FcD3RDfLoRbdtlaztvHstp7eHSUgEFoqXzsfndcVPAgFb409KkzZ_-Fx4VJ_-no7W68BtAGXiIXGDRfyxFiMx-qSU78yt8MZQ2Gz3ToRPi7vYNXCqiLQMJ5oDVLMMXCaA1N2vP_A42i2LQVrwMtEasDoTzbvwmXmhwTbvpBvyabFbVF2Arv3wmRneIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZpzBP0cbl-qAB_fbMLJY0426_RD5500vREy7wR6NgGSvZo2VovanR_k4m8RzflJ89jgtB49czQgsRpaxNg0CYHq8LM57ST3BF4GGEmQJ5eNTN8un9WV-6-IBgk-MPsLc9eMjUmTvBYvRXqXn3Kn3YrywTlsa-MEunQNHmou6mr4tSR0YTotdRJn2ccIIcpOzcETXFcAu4rtoWM6fMvKYJ3f_bxYZAbcspFfAliAO3zomMXsN1kyVh2eHoDUJhAG2atfaCac-fGV4sS-ztIcWhoLd3xuYBexdFiKbTXOKGSIEOmWyYpeVWGpd7WQFe59_B2QCFOui9dC688fJljFBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq28XBoeVBM2KPbe30AbcdWT-2l1en1_FI3EFiAKDB4E5W3S-bDwBzhuQ9kQkK302-JF2eHz2lC5ND5Nei9TFVxXbuXXdDjHhHL4xiI56CN-E40TiHhnqfTL8JgVGJGq0NvOs80n0szgi6tD6ETCipfPQCJi53i-8frb4JrF79cuF-60rTOm2kUBVmiXk8wRs--EDUCWGR3gPFSahosNiawGAAE224X2WqfyVweGUSQqAiN-xydjvIX9USz3IylwcQrS6MSV-nQF1CRpjTxuiLKVpHIUFUXvKArxUoUNaLRRDYmu927EeElfnobuDdmWgCWjOEq2jOTG1aGFskbPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spKTTSQ2xRMDYmttIy06ZKuywrA0p6VRaRKtetWq-GWb3zXSwgp_AgYOZaiugSWNgnqkh-LJ5qbrKul7tk5q97oHw45XXh36T1B1slnywphK_TUUQ9hEQEODmjNgSWve_ZCKH2QrQeZy48Zs6psugfGX-FgKqYtIXDV548KzhhaEn0G2s6mNkt0w8PIcsB6i4TD8_HRrxFfHMH7QIYPPEHmuP4Wzf0q5ycYbMOjxxhpvfRXm41OgTcPN81ol1IMKhtmH0OOsNDxJb6DKImqOruKUe74JTkdDwLc40v3MjLfuIz9YpeA2xmJ1KctkNju2jWjTx5nFN5jeCZq3Q6vyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=hudIEeVgnrgYika9msIZkL9zDkGoZOnpuvw5cTktNcrFBkL1pX9m-RSqNGDd5CP2_yZc3KQ9k0T1Cf6QeTgGSnGmvA2cOAoTlIlwG3No4S849VMuVvbozGwnqoP_EZqUYrfKwPBVKRg9kaeK3hAqBQPMBIZBcpSMG5Erq0XAKCJq0WHG-yg8YYh1nEuK61osKRJlN08qIAdAsUc0b5uFD63Iul7mInkVGlzcK-6pEhbze682SE-qUKzQ_aZRHI2z53E9N2Yk2WwgXaEhEX9FMzoMykCIc3M-x5B0yOCFwxSbFVhRuQrnGOTiktTgHwRFiwqT-pc6Y8_tXr-2rjjf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=hudIEeVgnrgYika9msIZkL9zDkGoZOnpuvw5cTktNcrFBkL1pX9m-RSqNGDd5CP2_yZc3KQ9k0T1Cf6QeTgGSnGmvA2cOAoTlIlwG3No4S849VMuVvbozGwnqoP_EZqUYrfKwPBVKRg9kaeK3hAqBQPMBIZBcpSMG5Erq0XAKCJq0WHG-yg8YYh1nEuK61osKRJlN08qIAdAsUc0b5uFD63Iul7mInkVGlzcK-6pEhbze682SE-qUKzQ_aZRHI2z53E9N2Yk2WwgXaEhEX9FMzoMykCIc3M-x5B0yOCFwxSbFVhRuQrnGOTiktTgHwRFiwqT-pc6Y8_tXr-2rjjf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieJ_8QwrfvHE1dlFSMS2fbUNOXKK3KsysNRLuISMTW_Li0KGQJuLPbUlVpEA0a4Refqw45qnmmoUjud8ytQ9Eg_n-gmJ8NL7laiQQhwfUAlEdwVoqnLNWF1du0c8rKcm2W3elFlGtSrvkwNcRVCnIXZsPZURLEukipoyVFkI8cuB5mtwG9kdj6wrT4yKzaKDYnkETN5d6luw8PDUSVq99_CXvf0CONj7DVTlTpCc_vNJsHOZ3Nkk5jss2b2ntaetTXjqKe6XpG-UdK8jTvrMfjIA-omZ6J_8GZ2MJd5ClN4TSMz8l1ASXfZCK_ltce1EEJ-xhDo6T3K5K2hyenyqmoto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieJ_8QwrfvHE1dlFSMS2fbUNOXKK3KsysNRLuISMTW_Li0KGQJuLPbUlVpEA0a4Refqw45qnmmoUjud8ytQ9Eg_n-gmJ8NL7laiQQhwfUAlEdwVoqnLNWF1du0c8rKcm2W3elFlGtSrvkwNcRVCnIXZsPZURLEukipoyVFkI8cuB5mtwG9kdj6wrT4yKzaKDYnkETN5d6luw8PDUSVq99_CXvf0CONj7DVTlTpCc_vNJsHOZ3Nkk5jss2b2ntaetTXjqKe6XpG-UdK8jTvrMfjIA-omZ6J_8GZ2MJd5ClN4TSMz8l1ASXfZCK_ltce1EEJ-xhDo6T3K5K2hyenyqmoto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoiF2ygpLlvFxKNjeZMrnVtI1pyfMM0JVuAnZMazBXSEMPPQlp6eiFnombG2mdWCuPOsiHS6QjBn6deg2kCZ_Zom7OxZN_w33tk3Ik7W6Jvo7Bd1WSw-KzOt9u63PiFvjRdAZGR_3huAO3PhaVSZ67JzmRRfANe0TmNBCd6ELLjP0hUSMylZ1whXsYEP75aOw-MVC-gWXncdq898awuBwRKW1odBWeIKNqbZIpofnPE0-tC_Jf0Ona2kPzVObBC8oVcUoY2Us03qMdYJvC2MNjVOMqhQ9LB8jsLBxwF6XGgrrTvJJD4rHdkR1tmnH7AVd2nGMVJ8koe1xmTKHvNMIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMZmczhw_DMk_6dWQqm9K09gTLqozfXXK5IRifWLKor-1MaVVhAfM9rR9n2bWzbja0VgsHwgMO0_Jxl1rM1gUl6J8-Z9VRBsvopkygBowM2KBFV9PAy3Wc5tlbewZhql4-UyjDlymuZ98gYYePhPK9xUFFr9K1CVgeC6QngfHzZfaj4J9uJ5fA4tgtLB-kb3njhXVmSycEo8d55Fpxw15X9chLJinW5ml1RIasTxcdJ2AJiTqYyOGpn3nxy2pFT3a5p6KYKCaunDEAjLXKeDGqNvvIP-QDqecmCLCnVfpb5kLNR_R3lYyj9_JRuF83WV14cYi9VXXZ4hr4dYUX037Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9vsQ-JfSzB2798gw-wRl_uaGn3vv9uQwjIef8hyfoXpQWoLDE7nNjbNAuYUtaPKbW9uqpbOOIhuXNcVp_F_-6NebXUA7zGCQ51mUcz76ioQLvbZYbDp9zKi-IPbeMJQdGhRuyefs69PnsAzFFP4I553E-e0HgEmEbQyNyAviuax-wiSHrSCEN0Wonve86YZbxCy3s-4h-_M5AFLdwEdNOeRt5L0ESNTcqe9YP6lHIit-vQWKwacmFBbKnbAITOKWmIv6JHHPMoTIVjVhfwcDIuffndVQWZ52_Dq70orHM33bIUYt9Ff62pG-1vSecl-pID14zUIX1pHB8zVBiU8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jkzc2ZjzQ5IxYb_FKjjRt2ZbhclVw6-f7iD_lfcbA4As8YVqEvkFiR1n1_9VDr1Zoqw5KM57pP2lL6A1WZ5gCCWMiTUuLJyIpFS7kIbzhDQmp6n-97xC-EK_f8k2cnrFxoxMscvc0gOQIiPBeJVTj2CawItPKOnR6GmS1rD5fLDguC_z0j-sJSOsvhLUcMH0fxD3f2dJjVHMjptC9JM88d1ZrBD0NreFJqPnrb27qwWNp18DJc1TpmvURfiFw5NjI45mTUe0WsB_Xt14HjoyquXJ7H0ewx8QMqCZckGq_StWTmVVVCNxe2jPQtzkN67CuPy_MjQJEGvA2_J5UVxfCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6h_DiBxKK5Nc6GLeOeVMjWHxO1_y10VwEUgKgKljxvX5JKz5R8c6k8rbqJHjcQuhF5e_1MPnHbVZ80stpC7u5UR-j3wppqlmNygZ4GLwGIgfoJ7MPcrXOU7bYqrS2zHTzvkbdr3TMx0KabmKO2K6cNcYdzM98S5hjv_K9h6iZgaXHm_jGKjmlvLkTDLgr7Gq73X3x06cF2fi0cE5idvfMbOUraipnI6j_7HNxuxt9p1b8fAK9zQNA452boY5i37yKVRwPV58FXIE63_8yOhnFVHjnjUv75Gzdyx-5WH117CZFYqLIK_9KtsoWnfGfgUMwb7XT19n6dcmMn62tWH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=i0jn5-j8t6PlBmM-QBKYRyG6xx05O4DoJoZtoc-zec-6P6LVkhw5LWzlphRcQh_LwAcDs35R3w7CCgBSc5JTzz8RXoOuFtg03Qz1bwEJI8AaYBFgeqBoRggx9hezeXokfBfKBzUvOOPbD6-TR269zXFP5L8ThD5e0K5bgl5zwNjswTRlStQN63ueNsm8nihWvEYvMRJiMjF3HLHzkwqic3UmWmcModQLc04g3xZbZYbzbI2DzWK47tkKkBVlS5G2ySA2Lm4Lc2pYasV3hQIl00eqewIR1mVIvFgTMPRQ7L_svWlw1J8A7I0I44lCOGXC1E7pl54T1gdP1qKctRLuELma3fRRn3Q9IbApUhmfKPbN70ugwcga5NFPKXDOYdx-R3AmslQ_euIDKlv-dC3Y_zy_VP2VeaIC6yr4wX_sZQKp7HuFyiuj9dKp42NvpN7bV48tzfcVjyNb2lySmHlOsoIZ2NLpcyek32xkOy-4u7e0Fg_geE7rxYZiqnZZKI1SJOfv_JbT_bhnv0wIiahcfprNji9ZCtsCxxgC-3EIQY_x6AjNfqB3HFb4pN2DsJtqIT7NTTk-iCa082J0E5sZlfhZmNhjKqa1s84ohLCc_6z4OA5RMbh1ihSGdNdi8yn2XEmRr8VbdwBI3ZwlDZ0FPoq33rT-82PKQHktUCopjcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=i0jn5-j8t6PlBmM-QBKYRyG6xx05O4DoJoZtoc-zec-6P6LVkhw5LWzlphRcQh_LwAcDs35R3w7CCgBSc5JTzz8RXoOuFtg03Qz1bwEJI8AaYBFgeqBoRggx9hezeXokfBfKBzUvOOPbD6-TR269zXFP5L8ThD5e0K5bgl5zwNjswTRlStQN63ueNsm8nihWvEYvMRJiMjF3HLHzkwqic3UmWmcModQLc04g3xZbZYbzbI2DzWK47tkKkBVlS5G2ySA2Lm4Lc2pYasV3hQIl00eqewIR1mVIvFgTMPRQ7L_svWlw1J8A7I0I44lCOGXC1E7pl54T1gdP1qKctRLuELma3fRRn3Q9IbApUhmfKPbN70ugwcga5NFPKXDOYdx-R3AmslQ_euIDKlv-dC3Y_zy_VP2VeaIC6yr4wX_sZQKp7HuFyiuj9dKp42NvpN7bV48tzfcVjyNb2lySmHlOsoIZ2NLpcyek32xkOy-4u7e0Fg_geE7rxYZiqnZZKI1SJOfv_JbT_bhnv0wIiahcfprNji9ZCtsCxxgC-3EIQY_x6AjNfqB3HFb4pN2DsJtqIT7NTTk-iCa082J0E5sZlfhZmNhjKqa1s84ohLCc_6z4OA5RMbh1ihSGdNdi8yn2XEmRr8VbdwBI3ZwlDZ0FPoq33rT-82PKQHktUCopjcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcWjxk-y4LBfPaUnvWD5lxhKpdtq6D0lIKaP83lf4SSYro6vQJgtz6hNFw9REBCb2HhW6yjcHx9mbDHeUi6JsgIToLUwGGvR2Cu3J5ec1RTw60G6ORtxpJSsApv4TAv4x3TGcWhOHVrnpgDMH-iC8NIplVBifr_e9KS4DcyKyHnK6WPpZM-ZMR7QvTNwuopkFtY_0eHBLZrlczD17KzFrl6vk2firOlcoWx-vb_mHOi7HZ2mwqbOOaY9qWnKZKBuRncxE7dYjqf-JDtv1mc5kAbX6OUel0Fe43MQsaKJ6O0oy9ML8OydNPz232mDX92nRq70ZXUJt4Nn4_wY_vJd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=EXakP-amVy6BVWN_CuTXlWGZKMDZ_bm5uMEakelplnFXWsQgxSDkbrrbzD5ywmIzIfpgVCb6BJitC8Xo_D6A1qKzlmqG_5wc1HnjWZfiXGthRVbajmOkoUjkGWARMDh2Yc_3og6t22Zc4UMuCN78Z1RG6y5CY_KmUauXeZU5wNaHkqRhyrqBS6Unj8yC1yFWWRE8YYi87coH6sn4QuG-xoOuWbDAz5fLrF22L5uviCzY1eFiTFJ4aTT4lX7Loy8sxFZewZYlnMVhwtMBY77KmsQVqHBymbrCbzIgnS6zI0B-KA0WnfEIcqt-_7tZpdz4a3P_BbkgvQmNzfCS35Pc8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=EXakP-amVy6BVWN_CuTXlWGZKMDZ_bm5uMEakelplnFXWsQgxSDkbrrbzD5ywmIzIfpgVCb6BJitC8Xo_D6A1qKzlmqG_5wc1HnjWZfiXGthRVbajmOkoUjkGWARMDh2Yc_3og6t22Zc4UMuCN78Z1RG6y5CY_KmUauXeZU5wNaHkqRhyrqBS6Unj8yC1yFWWRE8YYi87coH6sn4QuG-xoOuWbDAz5fLrF22L5uviCzY1eFiTFJ4aTT4lX7Loy8sxFZewZYlnMVhwtMBY77KmsQVqHBymbrCbzIgnS6zI0B-KA0WnfEIcqt-_7tZpdz4a3P_BbkgvQmNzfCS35Pc8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=IYBGiXttZIAGvuOlm97p_0T_XQpqf5dU5IYK_SYg1ioE8cXFhSczgVcBMkANYKOc5e-uPekj-iOh8pxhnauVNFBYFNdwbVjaSl6UsMdttV7CpapC1xkJ0hQwkNccpo2jTCHwtM4Q2BKEzpzitgcdTEVcypddzrv_mz-s3q2Pb1vFzMxIEJGrCfXbIA8EpQ1k8rouepvjdy4w7qug8lw6RP8kWDepyChyurJg63ZREdOPolFTkXTEnWAgEkSzy03OqavMvUlUxDOlwfsqw4SJISZ7g1vE9JvYcUwajj2bBBKKlh0HUA4CiGbtFmZniIaDWhFpKlLahTqS4FFlvPRNR5BN1Xwys2xQcw5wADOgCeRQ0m-QZFGIVRBuxA00Yxlvsehjv9QCEV-8pL2-umZmeEJzAN2PDOASSi5l3IrI0PlNGSJN9GP0JubJVNAQH8E6IoxOwuThNycuvsO1YRnOw6071snyJ0sHORFZSJSEehcw-fk5zJ1TGpPS6TE-LeL4uQcwo7PR6HTelPt2fzP0a2lpX6bx27cKh0NDvWxxWdehHMtupAerK92hQcJ7Tc6m8W855eSTjsXvlHBc0Oac4U3sXPOhFe9qzvy_oNWOmuLtQPOfdQgyIcfTx_jzxzP-7D8sTu8bp-tswhHmFz3iW7hgn9mZqbCeLANC83hAt-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=IYBGiXttZIAGvuOlm97p_0T_XQpqf5dU5IYK_SYg1ioE8cXFhSczgVcBMkANYKOc5e-uPekj-iOh8pxhnauVNFBYFNdwbVjaSl6UsMdttV7CpapC1xkJ0hQwkNccpo2jTCHwtM4Q2BKEzpzitgcdTEVcypddzrv_mz-s3q2Pb1vFzMxIEJGrCfXbIA8EpQ1k8rouepvjdy4w7qug8lw6RP8kWDepyChyurJg63ZREdOPolFTkXTEnWAgEkSzy03OqavMvUlUxDOlwfsqw4SJISZ7g1vE9JvYcUwajj2bBBKKlh0HUA4CiGbtFmZniIaDWhFpKlLahTqS4FFlvPRNR5BN1Xwys2xQcw5wADOgCeRQ0m-QZFGIVRBuxA00Yxlvsehjv9QCEV-8pL2-umZmeEJzAN2PDOASSi5l3IrI0PlNGSJN9GP0JubJVNAQH8E6IoxOwuThNycuvsO1YRnOw6071snyJ0sHORFZSJSEehcw-fk5zJ1TGpPS6TE-LeL4uQcwo7PR6HTelPt2fzP0a2lpX6bx27cKh0NDvWxxWdehHMtupAerK92hQcJ7Tc6m8W855eSTjsXvlHBc0Oac4U3sXPOhFe9qzvy_oNWOmuLtQPOfdQgyIcfTx_jzxzP-7D8sTu8bp-tswhHmFz3iW7hgn9mZqbCeLANC83hAt-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=pcp07XxOICES0VkOrTEhotD4BfNmB-8UnU_PFUJE4SOf7HGlVGpFHMj3jTJtmc7EV--RQyxI7tX3-lFdRYeqBlY4JavhW-xrwsxI1PQCPC-g3wGqPpQw1-sAkdPeHXCcBYC086C4m3eQ0JzXARsfhWxRSS5cM1cAoMvaVuarG07U-UIiodPpX2lN5pnB_v-HiuHJ7ptDq76oM_3XoosJuXRHI4DsW316KW7A6hrblLVXroJs6oKzssHvKrfZqesZOuwnDOgm_KqEsv2LLK6-6NkVdi_cSJjVv6dRjEIVi4qhNSFwkcrJHINe-vmPXniHAoSSRsY9HOt1jHRKHfmcz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=pcp07XxOICES0VkOrTEhotD4BfNmB-8UnU_PFUJE4SOf7HGlVGpFHMj3jTJtmc7EV--RQyxI7tX3-lFdRYeqBlY4JavhW-xrwsxI1PQCPC-g3wGqPpQw1-sAkdPeHXCcBYC086C4m3eQ0JzXARsfhWxRSS5cM1cAoMvaVuarG07U-UIiodPpX2lN5pnB_v-HiuHJ7ptDq76oM_3XoosJuXRHI4DsW316KW7A6hrblLVXroJs6oKzssHvKrfZqesZOuwnDOgm_KqEsv2LLK6-6NkVdi_cSJjVv6dRjEIVi4qhNSFwkcrJHINe-vmPXniHAoSSRsY9HOt1jHRKHfmcz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfy44Cgd69txH-4XagUy8KVtHrHupbKu2RCwAWFxHSnxXV5tOR_Usud1_niMKgvyOmiW5YYNYbLOjztzHJhz8Ob_BKwJkp4BgjLdAAzcZV-XAfLMZZWs8CugAWWjfHpRiCCRXJ7jZxa0LoukN_XQ0sVxTDtVwoHJTt87ZNKhgXkYh7WU0zg8zbAS_R2m6wqkDAhQG60ZQb5DCGVZ2N5yW1vtaZeuEknYLjVPQSHVgOXMkBIKTwBm6A2Ha_cDlxJYW4udIXgon0EHGxGxppNj608Hoy1ZkePcMgctBwycVQEGBsy5CoiCZZbqKWdO3PEMwiyu_-T5q74hguRP09tV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbtLt34RTl8-RsS6uPYDng_gvA5ZR1xW4QVDvR4nFa3tvEJdTZxdsvn3YQ6nXg8uUwkdOKL56T8-EUjfqodSAWbUbajD3vYhriY9MX0GJAfz9_9N2eS68lgqdTHvQIwNRrmuoWamQqA8XriNI51dXw9ry6fR5tvq2YrZPlSKHvUMAQi61kXy2M_gxynsQArgKBuSew-QtCV6KZjE7aWsWpB-0ulnlVr33NvHtxA1MMTcNvs0bCXL_pyJ1V8Z0hZedecJfWlR0PbGpCGpNGWrUOFxaAZvMurdi3EnVYUHO2sWlfkTVskPuWAeZ0jeFOxBWtEF_mh2d5-m9kgtXds0tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v90pKYbgWM-Ug-CB3bmLKAmanw6q3t-9GkH9KvgbA3Zdd72VV2do3V6YtA4JDATvkc9xrbBWWoUPHRlxWXRhauIZ3UxdcRT6MgsYRq_CghxAWzvk5zhFE9E4xqOgTOetYd7ibz6PaSEV0RmPzuFSl3P24oQZwlv9ms7BZi7Ao4TQkMAWeM9OIN2D1SU59XfhCTS_UZFZ5aoHMA_q5tuIFWRrUwKkHTZOfavz9MeXJingxSM5jrLWcjlVWOwZfXlOgHJ65f2-CmziAcDY1LUib7BkNZQ7dj6wh8dW9N-gOc5Q9tW2O8m3jB27wHDWUTBkvGmG-l_mylfPBvvvxQSQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrNdJC8BV06m1rLpxHSUYzb-k3Vm0l36Gsc02eoyfvOukdtAULKDgyW7DSmAfR7aUgGMBUo76YXmDVzK2L5x6oA8_VG-yjngOY5BnSlVL4kzs6Mx2BSowMJ9xkjxDjL_zmHFtmc0YV0XVjnKoDmXBftoSo-9xzlyXlWfU78dn7jZqvPosmC6hRCKBd3F0Ph45GiVXOpp8jXxwVtiwk_gkH9PMLYgtnoY2QHmOfFL9Dbx6uGe42MUv2nYy5i6CeRnCdX2CFntJVuPcL-PGmKu7OpFe0dofkZd7DeR76MgLiPqwC7U0dGnktOXAdOt09saiEGosU3bnSJxTMt4pd-Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvwY959Kcdl9kxEPxkmBjewKlvyMSVTHjvqA8sBqr179GtG9tSirPfymhHehYqXp97IkYRQpv_A-6IMZh_CRDHmcIANeGJiQP129wXwInBTKQdTlVwI_IosOylLFZmZAtVjOe7VkDiCz_jsAcGkpGPHjps9FzTw24zeGTKU9R0dRtVH-uS2eoP7ctGaVPbjGVD2l8vWSS88ymh6KjcbtjKvQ_WVLHxj59eEiTK1HXQReSTiizF2sXFathw_z38cDhuafpmP14kA6OT9KNW7VlQT5CpXEkQEu8sWdywOzXoL3tDNNFAJUcmDMe7lM-T8b_34fDdpdD_RNc204mKKFmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IXiS9gXRqZRz7LMYK11VkGqz5eJuUueQTxHQHSRN_XY2B3HBnK0x7Y27SIh2O8mQo4514xulE07LUUJo8wbz6Hs_oi3NjoLs0NIFCOUWqFfuckQYu34yHyQnNcPRNRwYykK5ILmenAJ7awzuNVwYJGPaJ3j2AU7jqv9T4GOrfw9M-aNmmUCUawjX1Odj0IpVIOy_eCmgzfcyJZi7CIIEdJv0HGc-RqZvHzCQYWGjwOYbxn602MVKuT7SmUjVt7cVQyva4quy92VFKdGr9_2njM_yUFGICwy6V3nZCTrfaGS0gt-2A1YrbLGzBARBF330uA6rU65_6DsLhlvswigDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IXiS9gXRqZRz7LMYK11VkGqz5eJuUueQTxHQHSRN_XY2B3HBnK0x7Y27SIh2O8mQo4514xulE07LUUJo8wbz6Hs_oi3NjoLs0NIFCOUWqFfuckQYu34yHyQnNcPRNRwYykK5ILmenAJ7awzuNVwYJGPaJ3j2AU7jqv9T4GOrfw9M-aNmmUCUawjX1Odj0IpVIOy_eCmgzfcyJZi7CIIEdJv0HGc-RqZvHzCQYWGjwOYbxn602MVKuT7SmUjVt7cVQyva4quy92VFKdGr9_2njM_yUFGICwy6V3nZCTrfaGS0gt-2A1YrbLGzBARBF330uA6rU65_6DsLhlvswigDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beqGjDTtYVQUwLbA8CXccaGPBaIusoNp4nv9Obh6mIN2jBW8S76rKGVnXvaB3DXvWiS5n5akLFwvjImRyx49m3XwmfYMho34jVGzKLOrhFjLvUvpXRyfG9kYKu0UCaYIvIX6LNuFG92nLXUaritpysYe2euLZsASO6t7xl4en2YoLZMV1RXqJEf4U0wkcP71_h4PpnHvnx5f7qhQxrfH8S-TzcbRpUKRzrW42hvTeKTJQP2SVk9Ld0hpHumzKXpaP8kp9EcZzZKAIp7-ixvvdZWHjhbnUmXLf9M-uZpGU3Ynv439ChJJqO5l9Y7rps3M58WmeJ0skLFw5484WwBwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqDng7Z5aAzbD17N05hSGcSagc-Y7LlFRBcsecC2ZXrwXf7V_eH6H4_ZQ-v8jEufAqOhDszkOEnSkNyBjacDFgw97FwPYxCQaSMWpLoDMEXaBgFScctZi4DVPYTxAgyS73SKejSceYq88QHIsoBsCe9CPCiicz_f6zNx0P-tuyVMjA4u_KHLpYHUWeM6MUiaqjJncIf4IRSAD_r31f6TbY_TjXV-YqUHFNnMAfJZ89ZKHe1Yy72AN6HcWTp1T3JmnTbGrKibHfnVVpyMPnTtJeL2Gf5V3GPW8RVCcewFQYqj8Ymb_9FkhGhO--PDf5I7kBlTkhcrew6akd6rB9idIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiY7tqLDgla6BbktajrEMmJ55dubaPHn-gXRwzSymN5zKNwOJpB24FiKFl-zRD6wNoRH6CFc5dhYbcdyJpqs0-5ZU2BUBp9DU9mx3P3jK2o4n1I1ANvVYG3aw0kkociQAkhhLbis06UcfI066dz-YWP_FcZgHDUiw4bcY8FY5nR4xzSjszNg_gOykTK3xQTjYAEQeTB1vAcbMS88f3qxZcSI_eEoI_eeNulWlydVeo0c7_RHM8TpAh_URxP-WGezMnJDx1Zxbc_RkJrYH8190I4weicWR5JvrTQlf-9GB_dpyRVCta7U8igJPSbcU80IETM2eOn4iElFqrX4DH4EHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
