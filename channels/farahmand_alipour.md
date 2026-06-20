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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 00:17:24</div>
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
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=FSnCX5FrLPBRDerdK0a8D-gTvwO-kwfSb9sVF2egDZL9_RxEbQd6QwUTlv2kQaJwh7_AnAc96NwJmvPLk2cAHxJJRa1d-wL7PMKM2n0g_1uoVDiz67OUNO_M7EYDa4-1TnBZR43agpfpoFI9oJrybzN8mdDCuADxlc-dVxbDXkPX2z0Nt-Q95KjM7jWW2C14SWMro9tdbubkO3y0IJFamrsSV6EMO79PuEEzAsaFQX2mpuR7JLiWHChrti4t9NnW_mHNR_R-ydJ3yu12JHT45KOnSRprMKq6pA2MweS_ZBKLDP2Undy2wTj8c1UrC875qmRagg8wpi3bRDpxVNJJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=FSnCX5FrLPBRDerdK0a8D-gTvwO-kwfSb9sVF2egDZL9_RxEbQd6QwUTlv2kQaJwh7_AnAc96NwJmvPLk2cAHxJJRa1d-wL7PMKM2n0g_1uoVDiz67OUNO_M7EYDa4-1TnBZR43agpfpoFI9oJrybzN8mdDCuADxlc-dVxbDXkPX2z0Nt-Q95KjM7jWW2C14SWMro9tdbubkO3y0IJFamrsSV6EMO79PuEEzAsaFQX2mpuR7JLiWHChrti4t9NnW_mHNR_R-ydJ3yu12JHT45KOnSRprMKq6pA2MweS_ZBKLDP2Undy2wTj8c1UrC875qmRagg8wpi3bRDpxVNJJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbITLjdkx_DVx6bJXnd3yGjyTADU_TcT7UQwugSreL_yCntP3fuse-pjyjq5Jo9WIdJTKFGIIH98rOyOi8-Ghwbx4zHPjx3r86uFaSRn-mABub0oQoPgoJIBWAozexjEhGJ3Ew7MlDD3YD5eX1D9a_hizvDqNeHHEGqFVEzk6sHS7zHnRwkiNYySFqfgFVLswUtlC3U8J8g4YJKv9AbGJqu-urbOeGS3oQitvOulF20s22DBJKIqahMQXcY3FIbqAIQcYkEmQ5Ix55jDqTc7QhTPbvWM1lzCGTnN5VYrRr7Of6Z7GGwSPkzqlr4xkw_JpfI6siLvMxoKGK6BHcARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ar-QtGilzzGAWM8c3e53A2UMT57PXmK0jbSkOD-iuw1kgZwG2ObZayAO0yFFOzLie1gVW5ojK8uf4XOssXTpAs3ytbaYN2ENwVIBhcum36Lb7_lVTBiP4Zmd1FC5Tmro6CKNwfuKilwCBwx-jOT7FpvpRYuau5Jcari9gJYxjMgvriz1TlzujRw70xILd1qxF6nJuDVy7I9nhVBMA0WttU9NIRfN_Bp07aI9C8f6Xp6byxIJPItcM76gDzYp_gdXjGOwLaW97PrGFurMZYCQ5SWglFizFrHc8XEYkCuDk6mc9O-UD88Mb4xdDgV0c-5KWr7H_MdAk2wKs2BX2SALOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoXoH70txj-IYADuLy7ZUaOPHHSrweX-GfD_PQgUS9lA4j_UuYhjDSjBszwoi25ToVjivEb505KLvmx6xsGUi3KBgL3TVvuglMDCjppiC4Ap-O7RJ-kXWIM8coF0Md7IVE581aOm_rdEvZVO8sVDtYqtMESZbeh9F3ZVWVdYpHz65zDGSKCwYhEn2r3BxwzVMh5to1IIz1kKBYJrorjYL7GUguwp9nGJw4PLJM-UKEs7f1p52N0eTcrIcD3nICbe6UMNeglwEc8iVvkXld0korVhlJvnx-4uax3rDKC_stmGfUD_qsRbj_jJQ6o2a_0dwd3TO6CfFHR5T0W9nQSKKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCky_KPctwQaiqZUONhx5pUbQI7fMH23rwbG4uHOb2Msn3WiV8nUihVt8rdOrhx46CquMVU5hnaq6F1KKr5Ce6q3Q89GIn7FsIrMEpncpnHDUpCOY01Jzwy0UN6Qn3LyY-PPGuPlvZjgkRPwwG-QqV9gHISwDEzTC1bGC5yljBpqm12mUr698xwC6MMkceOkv9NGEmm0yhsAxlpAzGNKCK-5_PO_JhvXON0RN-h9A7gfxLHiviTFHpNqEOiSYKIyLQdBVRYSFhPSqV9E5MUtgK5PzrnwTZ0mzWXlckO3zw5AN2bXaEFdlf0ANmyvN3Fd2N4reB4W3MdaJ5fFmdW8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-ZBH5QfofuMnFuYi2NNQbTBRlK3Y6CmC-WZZo4AasuWKPXvSNap2lNRMzMOCBZ1WvxDguqCeVRn2qr7rjevs_PvJQLDN3s4RRZP7foTERNb99y-EN_7xvbF3v2T677My8m2jhH3OGt2_mko5uH_jbz-BdBBai9YlgPmrdVTAwFX1MDDRcaz28RXyHesEj60H52PxQm6Ll8IsGa8snHB1F_1CilRBjJPSq_vq31j3NhhHEV5dfmapMtbFTkUagmGI7g2NBCI5xJI9ZO7IkPT2u5VJxpFuKneNMHvH68bz04ubwp9DlOweJPvvdZNs0boT6dHII6ZyqMoGzGluuAy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXXxh0RsvIf9FjQueKenUtsvpI4szV1CQKQypXP-yjoHftTLEIfuDrQxQPoKsHJ6lxGBiYwIbAuv6kLxK6QXYSURfedKrmRpkcS2LlupWmadPicSdIDNAVNNeJfbxE3BuRv8USXt-6G9ZFapOSResYtz---L2APoWbULbYebU_NS5gejBN67iYekMXTmHMuPTYaPbGbmTlzUMouv67_LFfbCViY_xd857ryeDGGyWv1G1X5E8MBMi7C9rb_7IKYOX_aVVKt7NmiqNjV5CH62VnG20s4Hm_IRW1yhmcyny3qoeeIlnRRnQsSV1Kv_KXgLDo4V3n8-tpGnW_F5MB4Wqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu83dMZRyisEthGg8zycNAYR9hKxZGtmjCrruQaTM_-vMwEB_BbV3ekugPnUQTLsi_y--Fc2H-sxKlxGcCaTPHOgo3obWJvXgohzPFhFmB5pP6bs3hkxXyckXoDY2ppUveUtXeOgwijqMOau3U0g9kI_pt3vBWI-8x8sr227-vimrcMoDysS-Qlu-Cpcz_AEenoq7Xre-Lb3NjRzeHgpkvxVWSl4Gy2jYZ3BZ0CyHpEC5ztlRYYnu8rrS2l1UI81LVsorBDQuFuK-KxnHqq3ptJM4i2o3n5bgV7xhPD0kNg4WlB5QJmee6grNcG95ieQX2MHRgwMK6NBAv12Qry6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ZHypnNKdAeh2-LliL9zhv3j0HuNbji8eiMOMZT7yt40CbHcHuNaUqVjINTeCXcBkUIx4gCSv9uhpn1o9yWxpTzezCoaSNzXPLD9ZwBY2ek_GV4jr9U1fizA8uai3zPUBlQDdbSgtgupWEzfLIJUtk4oE6xEjWkIqLxuFpD_o2-Wtt4C0QjGcOSgfcj1sQr3Dh1agHOkJoI8_ecwO55BZrmkDQJug5zCls_kieLKhm9HJCDDzC9oOqURvcdZ4zEHyMi5EEpXe9LwbEUgMuIkWTQS1MPI_4kqYZEZSK0DQmfp5seS-cKgrBkdFt1RrgGlx2WCFVH2sCQRqO4-w4YX-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ZHypnNKdAeh2-LliL9zhv3j0HuNbji8eiMOMZT7yt40CbHcHuNaUqVjINTeCXcBkUIx4gCSv9uhpn1o9yWxpTzezCoaSNzXPLD9ZwBY2ek_GV4jr9U1fizA8uai3zPUBlQDdbSgtgupWEzfLIJUtk4oE6xEjWkIqLxuFpD_o2-Wtt4C0QjGcOSgfcj1sQr3Dh1agHOkJoI8_ecwO55BZrmkDQJug5zCls_kieLKhm9HJCDDzC9oOqURvcdZ4zEHyMi5EEpXe9LwbEUgMuIkWTQS1MPI_4kqYZEZSK0DQmfp5seS-cKgrBkdFt1RrgGlx2WCFVH2sCQRqO4-w4YX-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=nVMV5hs985G3atoEW6lcBc5ssLpQ7PN972HsfZqQwa4nhSauRvkd1l3YACiKgmo7lSFAYCfHSHpJ-FFt39P-c1hc0Nir3Zn_BbEQE-idNvv-53E1wjcg9CLmYYNIRUD948ktCDTrEYQ30YnonnVoi_7eCXmtTGk0lshuWdp0wzSX8kMYTgGGnIXYKX8Fz9dUDWGLdhq3XiTyFyte4JrOUyGbCCn3I0W31gC6nCyVgSrE7pgoqFJG_FW_GQs1vFEJAuUlKNDGN8W4Dd-qoq50ezq2ey1-4b-uqvriA0xJt1-b0MCI5Ajke90yRVuEHxZmqnDdkad5KDUwT_ohzcyIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trS_ktgyMkMqkFn3X0nT3sFd9Z0WWSTtEaUfzD5omOU8PeEcOYK_bw9m4LhMK-oIB4Zbc7jT6jMZmMvQiKGQb-BP1HPB-pUGydwcEfia6h250CHIFX27W91h80JxC1Uu75_PdgKthnA6LinkMm81LJqXsD5lIO-XOIt-3KeoIwh0QI2uSWt39xDGy70CIV8yylVsfAEc9i5PbBZBJnQw2sw16zX9SM7XSqRXdrlJb1Oy0yiAVESBftBo6FPEnh0LF5JRdyVYsWatB89DE09HvWy7pvu3ozcdiScAb1ChnYJ36Hrr8z9uQB8T8wQvjs_DYLt1QeVtiZMGOcBQzrQJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVdms9y4_JqFhLz1oBGg7RjqipchHGxNDTKZ7tHJZN0nx9l6ZlN0Hju3k32Cghb9y3vpHhMfds79rCYB3wcMN4rfr-av5usTm5RkSbC40p05vOSqn6ifbV0PsGB2ZikOIOLbPJnAitIBND-4SHsEp03aVefV7YAQw2KS2JG14QJNMt0trNKL8gkdtTWlzrMN49jOA7fTjC7agNhGTHiFBD0bdJPj1hSYAvoJu9VQnZJ85vA3r-B4ds4xv0isVz4nOePLWCzKNdexpFZa_dZiZ4UaFDMUpegiSi2Fe-0Sne88THKQqbp9VafKpE2poV31jZCxzB8cffvMj0YJBsjQFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=A0mLOYzKMZBpKySfmorLZ3N9r-NQrzW-uB6_YNSxWhquJ-b-HHxwmlBK-1vwrQqxSbdojojyq2dlXUaxCpdkSypXAMktYP446rkBrO35iQminMKi3zrbCkSNUAUa5XXX1ldvxlb5-K0B3KZLBUMRJ9BAXlnxy4VEKMsN4sZaMBUYoZOE-iEoKNENEZE-kvyQpsuZ_3XUCw4xuXBTo_07DwHWRE4U6BQg6yjpRwoe6SA1blTjoL6I9IOsOPoUJdiDTrjKIv36FjAlW5XiMA5ouwhXN-NvyykOqY-eOFpqBa-vlyvv98NiNEXjslwK2Z9uYmY7WVDV3UOk-3Lrg0h6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=A0mLOYzKMZBpKySfmorLZ3N9r-NQrzW-uB6_YNSxWhquJ-b-HHxwmlBK-1vwrQqxSbdojojyq2dlXUaxCpdkSypXAMktYP446rkBrO35iQminMKi3zrbCkSNUAUa5XXX1ldvxlb5-K0B3KZLBUMRJ9BAXlnxy4VEKMsN4sZaMBUYoZOE-iEoKNENEZE-kvyQpsuZ_3XUCw4xuXBTo_07DwHWRE4U6BQg6yjpRwoe6SA1blTjoL6I9IOsOPoUJdiDTrjKIv36FjAlW5XiMA5ouwhXN-NvyykOqY-eOFpqBa-vlyvv98NiNEXjslwK2Z9uYmY7WVDV3UOk-3Lrg0h6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5Y8z_FQ3upKlK941vmmP93OShl7AZJjieAYAh9Vas2QvtZsfceIIDmeSQbuKcJbLMnOdK5WaA5kCnWz9dJ12Y84bnwTr19lnShgkQCOAXQxJHydve8PZYDmY06r6svlUS8TcDdzU-t_Orcv8yKoMu0LFTjmJdrGwNH5LtzDkj64vG5ZE4T7HUnxVFS3kz7M8WQQsXPUrpSfIU1Srmg6JlrasrSKs3seZN0IElbRtKf2oPX1aXZcAOTbKoWh8AbzypSH-kfkFpP35FYSsqH5gFTKf2rn6vuPQCcOLhkpGsZfV8Ejl9ZIj9AJM7LTEcjPEbb5VkFzQT1a1S837oYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=ixf23Q32ArgGEWkalRxFB6SqpMqUfYt4386OSWJOV2HvKyeNIuAVtk069TlL7ts7IRmgw9rz_SCwQ3uZ4-4Rdrj1p6gk2JUuL1XMZncG45iMjzliy9KL-S1toXA0eJtMtOPM0RGVnCf3jKmYeNWSgyN59NIAA4k4idQ1tUptqxLQeAoOnE4LmuQfengciHGbmR8ty6qERuo1Ma4wZOR_JOK-C8OiiCZK3qlhykyVEsLLO_q0ulnVL0qQ2RdXFmzpGgbM5Ph2ldkuXoMLz6Ae15H2Gn592Jxqk_lVmZ8hpMLnHuTWtTa3OHdRkUGUx9QZ6flIqeieLsjeFiR23O7axQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=ixf23Q32ArgGEWkalRxFB6SqpMqUfYt4386OSWJOV2HvKyeNIuAVtk069TlL7ts7IRmgw9rz_SCwQ3uZ4-4Rdrj1p6gk2JUuL1XMZncG45iMjzliy9KL-S1toXA0eJtMtOPM0RGVnCf3jKmYeNWSgyN59NIAA4k4idQ1tUptqxLQeAoOnE4LmuQfengciHGbmR8ty6qERuo1Ma4wZOR_JOK-C8OiiCZK3qlhykyVEsLLO_q0ulnVL0qQ2RdXFmzpGgbM5Ph2ldkuXoMLz6Ae15H2Gn592Jxqk_lVmZ8hpMLnHuTWtTa3OHdRkUGUx9QZ6flIqeieLsjeFiR23O7axQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI-KBPL34OxedMFfd3fEDdvsKs6BUdH6qXoS5CASvdTSdAQW_J4zQVi-xyON7K_jA38lUw624B_BvZwnEOR7K4Fcch6l0r30SJFIH9mCyjSU9ejGHTcSU4iPgV4QtjLBqN-tySpfLq_RkojYjF2Oni6CtW7kvk5NbVjkFFHPtxw7SQx5khxc0_m1335uhT46TICCK5na0oxnIsVwMYo0vBuC8rxRTMjoHS712yD0olZxp5dnAJESow7KD-LGUXMgh1bviXUeLcYGIlZaGjq-fo_8B9q2T58A73n-zbiTKXjcF7vVNtCVSuJer6FQItRRhsCaoecGRnoftSNaVDpKaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRT0C1b6ly5QrYNObYJgT9JsGdJ2g8GUJUFxDKrRjk-e6urS1wB7u9Ucw5sgoeiyjlKRfjBiUeQNMlEs0pV-r2ROlIeIjmi3laJC6xBkA6uMFGzG9iWe4W4_ElU78wMUXYOwqEck20VcGtzgN9FZoToev2YIXp8Wtd9UkEBaDdTwX5k5LDIIH54Po_ssTU9z9Hw5zEYnyWQF82lGAekrKCFVRRyr4ZOhD4Ukas9d42hKCbSQlbiPDZSkKrW9lryBcXFbMUz9WFmpzbwAr3lHCtJbngt_vZ4XTgJ6_4k1v4FGCTpzhec1N4vBHScnRqijX0PYyk9I6XlfO571eaAJRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=C0On1eU2tnb6vYpmnJwy_f-y4PIbmyuwDEjPpzLT2RyA2jDTNs_dXj7Sg3GEIsyZFwtY5kH_Ni-ikVvBtD6QMQQlSIOpasyDCUBr4xdg-a-7xMhRos1YScAe_bEFBwNzMA-9Nq7yi3s90fdNuRIh0hdbXqyYHQ9F8tqc4vE6sYRBHQIMgYl5WzJIy2lMMS_nyNoc5ohxqdZjDD2qaEXxa8k1DQhN2fM7tcpNM9MldafSfCEQAu4xTH0RpdLtqaN8XkujliUZxmGT85VOrLelR3B1CBYIdXllfDuW0z4sJEil-xGarmF2BT-FMJp6koIcUWr41YLuIcUrG5wGBL-l5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=C0On1eU2tnb6vYpmnJwy_f-y4PIbmyuwDEjPpzLT2RyA2jDTNs_dXj7Sg3GEIsyZFwtY5kH_Ni-ikVvBtD6QMQQlSIOpasyDCUBr4xdg-a-7xMhRos1YScAe_bEFBwNzMA-9Nq7yi3s90fdNuRIh0hdbXqyYHQ9F8tqc4vE6sYRBHQIMgYl5WzJIy2lMMS_nyNoc5ohxqdZjDD2qaEXxa8k1DQhN2fM7tcpNM9MldafSfCEQAu4xTH0RpdLtqaN8XkujliUZxmGT85VOrLelR3B1CBYIdXllfDuW0z4sJEil-xGarmF2BT-FMJp6koIcUWr41YLuIcUrG5wGBL-l5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=IuQPF4mmp1Pf2ZY9lbP0Q5SpGOAydO_6c-oT79fTHV285n-JpIl5h54fzCJn4cG3kwS9ZxXthvnJkHx8brJGdFHQRd7Q-YZMYgYgpyXFn_30eefVToFIfVgW4V_tQAW2lKqHR3BqifDCrwk16dUoWenDAomCn3R3G2QX-7PVLpyngLHusS4Z9enawyOQjueJPNfBHI-CaVNDYZgBFBeEDJBLVlUJOO98F8Whh4tM7U1cqI0eEzNDmw-WVojHt0GetvcL1PXeajSMxvlG7s3Rqzoip1kYwmObgJbtmFIvO2yC3i6UY2Dd58vq8ENdI_qj52IWPCCWmlIXSFy-1X0-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=IuQPF4mmp1Pf2ZY9lbP0Q5SpGOAydO_6c-oT79fTHV285n-JpIl5h54fzCJn4cG3kwS9ZxXthvnJkHx8brJGdFHQRd7Q-YZMYgYgpyXFn_30eefVToFIfVgW4V_tQAW2lKqHR3BqifDCrwk16dUoWenDAomCn3R3G2QX-7PVLpyngLHusS4Z9enawyOQjueJPNfBHI-CaVNDYZgBFBeEDJBLVlUJOO98F8Whh4tM7U1cqI0eEzNDmw-WVojHt0GetvcL1PXeajSMxvlG7s3Rqzoip1kYwmObgJbtmFIvO2yC3i6UY2Dd58vq8ENdI_qj52IWPCCWmlIXSFy-1X0-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s80Fp7XIjms3bosWVYCoNRmsnVOa22l6lLVda8ll8ZdZceI0DrN88jj37nBG6oAkjLykdkbCbv0dHLD4tsdGWQwb-eCYOv6y3g9s0FTQvTwmGIsBcgPEGD2Rn3W6D35nh4A_GBZkJDHfzYUgY7KOAX4cJuube-fmSkXTF4mGHZw2wD0WY9ST-NLwKXVHPE2-GUzwCBho1a-wGMDafRSr2NaFi932-wGBfrf3lPZy98UgLfiB7Uyk9wHp1tbquH54hm4t91X5GkTpDXwFEOpwQX6S_C3OuzlEyT7tpU7sXfCpdGlTthmSXt8F1lCX47rCIkxNnghWf1C94YWwF3jCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orQndsj81esSFqqejTogM3pv7xk8J8O5_yueL9JapIp8ZGSdgm11GaltnItc3y9z4KfDHHX58XblP3rIVn8Q_stRa49mbFJ_LzEuNP-o8utyiUF6i3vU-mMwGGefZx3Iu7lIsjIOjYpheospbRo0cvizgVRKOUbEldHAVJy4cqxVsswJRKaNOTdT0LPWcA-sE1gnUhoLUU2HjJNfRC65lz0BTrNgdd-LoHG1NiUI5s2T3lXO6JcEUIDM5N2eE6-KL0rsShB5pGFCVc-9Cwb4MQTo4MvM5rEaSXPQaMo-LhF2dQ1XOZDnH7-b4F3IaPIEPt8QE3O2Ex_PxKfVgxUxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iag4QaoPCeH52xAlM3qXcd-1MLckcngP4s3YJ6UaP85DQ_sRl47GIb9ah805_v8y0gmTAEU4oyDonjUGhmKFzi9_zeEub2jX91_vdDHbZitli4MKU6XizCMmCy77jYc4pSpvruKtuOmJDL7y5aBYt5XKjlFbitlvoWQJaaQjrLGIazmDqCVsejFzemayNwdvxsooss778EAvmBd1qVmgC1hChA-ItCftDDlrgXCq3HNGxaA5_I7CAZaNrk3ynrjJeXa98jQA4jJKkZncBc93MTu4hOeXFG82NnH77K2hZfQtEp8OfGZCh2Jmaens-ILKOlxU4q-jR65cm3kf29RtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=ACRsvWa4jSVS9-WxEmjJQZk9xR40oOl-jSd7hIUs2XcTb2Kur3yo6pbsogAwcC7kK8BAl37sAszwSict3YwpYLmr5hu6bzFwnmduMpRMLiIcxvERRQWS5gjZFJG-mBosBoWiPlaKQDA6n-LMMM0z1TYB9Ij8eXTdauKe95ae3Sb-1596BFPP6XGwzb-m2ycdiZMSUUCvwUpIRZu8Wg3x7QNoJuL-dqVcQI0kKeRyhUz4lykFO9maEYX42DDhI5fWDRy5ps6kDB1aVHEkWaBGa4D8kY5AoZpNFxzpF35y9VzavIAPSO0AhnWwplUDb4CciuX38MgVofQqyWDHx7Dhgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=ACRsvWa4jSVS9-WxEmjJQZk9xR40oOl-jSd7hIUs2XcTb2Kur3yo6pbsogAwcC7kK8BAl37sAszwSict3YwpYLmr5hu6bzFwnmduMpRMLiIcxvERRQWS5gjZFJG-mBosBoWiPlaKQDA6n-LMMM0z1TYB9Ij8eXTdauKe95ae3Sb-1596BFPP6XGwzb-m2ycdiZMSUUCvwUpIRZu8Wg3x7QNoJuL-dqVcQI0kKeRyhUz4lykFO9maEYX42DDhI5fWDRy5ps6kDB1aVHEkWaBGa4D8kY5AoZpNFxzpF35y9VzavIAPSO0AhnWwplUDb4CciuX38MgVofQqyWDHx7Dhgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwvowAhfgFGtJYpC5FCyEvbwVYeUkpIObUlQjxqxPHDQMu9YW2QZ2Tnd1P9d9KBrx-YIXrRnEKSCpm95WrO9Us2LXuge7wkNb2goJUiXtaWnnkREsjKYmOaadGV6HMZLxXKarZGAGY9aO5IcO6EIGx2_ZO8NkmpgOHi-YZRRrSGMgNlnTp7xCRlUBE8C1ChOaYASoiZQ9kAf37W-OAXXp4Fe9PvX_TqMm8NUSNhZ0Ck0H-ki4grBybjg8SKVejMCw6g0XC-ZuNbcToTPwDOaH02eDVUF7IHeQD1F6ExWs4qXHlbP2OswM11k-E1S0z567XhEgFirVkrXG_3DqL6LVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_k_TB_jfu6-HUmwB95Q98tManzCx3Ngt6NDBFl5RbVQygdBRvp4KPxDlOs0tVQfbazupXtQLdy8iOuKJ6l1ALkgfWMnnGnNVLeAV-Eew8bgoF2K7wknzka1T0rnemTLCe64W8k0iL-ntlcHu8qLdaPO-pK3rXdCPp39fp65He25nkNpSD61_K7ZqzA7rGEkWP4ucdja0zAZtUwMbS6-slO_HfAkW7JbiOfA0JxPFyskZ0S50B_Vc7ssAvLRWPhXxESD3ziA6jh-9mzJXG9CB75hemqXsxY6mSKforOIBSOQ6OyiM769-FYz8o36deLUThCPTjLl2VSybPoe0sj5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDG_kPtDeSFB0RAoe_8EEMm4Q_FJkDyZOID7Za26G3tzuRey3-vU6kweU5s9VLcGwC4A6EvzZi0Hn7rzrW3v9NjkmkroyyiDHkIOHH-U9Mq6gllQsKdtXczM2qHmx51VRlwpQXCKw30vLTSOWm0LDC1HzyhltCIB20aHB1M6Sdtf2K-iA54rL6L_6WgYFkBGemwwIMDRt_CET7BE7Tp7QfEpGPkOmBzPc_PSlS3M0-oQBhLNmM3Lvi4-OIekynVsqll-JKrhhEbJ8aF3ZOu43UtEEoallO67UISoF-QIgwycYdRga3ZhDb3E8sPbTK2o41tF1RTzuv_aeWPoR2U6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAlBR0THow4tOp4rkLSr-D5G7NGzpncLnYrvZZRpvXySJdpHtNOD8Hy2GYPe5LjzngdWHOsdPbHI9TdhLrktD_zJDaQWdNytxKKsMja_LuJfuc0zP9STKH55G5BIrTsplc5GXQ4tlJD5Q9vsTTKcmYH2uzEGFBCE292hvINkack4LJqSKGao2AErDm0Dd-fh1UrksFsveW1qSRFiQe78MZov0zr3TMkgzEdX6Ggn0v5n2ERznKYOAgx2CHrDOtMImHm8nuacgciOGRJDyt3qbsd28EBAsYm8fh4iy8WweZRHT5RoJTNydjk5h4_DH01mA59cZmmr0EBXsofJlWAeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ApwREKgiixpCalBirliJ_-bV-LAslFehHjsze2I0UB32jRAzZ28l3v0nTTEY2gLD9MrLlPS-qMxnk840nStQYULI54NGwDpoLOEQbF4FG3fqyVj9I277T56lyjAXHFTC7TvXD8dxas9cWUdbC5bmUURAhl2H76b0y8DwKSpRzTbLf16T9Z371Ezxp9Gtq_1MZjCXX_63s7cyIS2c-CcLE_Omm6sX3DOMsEQR_Y0kIbpTK0h37SL_cOoPvnT96kVXd7jCPAOq9cFbiTk2yv6g6L1hiqrsmK0Q8v9WqQxlZn_iwdgwUmRBR-zZA6jq0-mt5Eh5FQQTV83sHmVzO1CTmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ApwREKgiixpCalBirliJ_-bV-LAslFehHjsze2I0UB32jRAzZ28l3v0nTTEY2gLD9MrLlPS-qMxnk840nStQYULI54NGwDpoLOEQbF4FG3fqyVj9I277T56lyjAXHFTC7TvXD8dxas9cWUdbC5bmUURAhl2H76b0y8DwKSpRzTbLf16T9Z371Ezxp9Gtq_1MZjCXX_63s7cyIS2c-CcLE_Omm6sX3DOMsEQR_Y0kIbpTK0h37SL_cOoPvnT96kVXd7jCPAOq9cFbiTk2yv6g6L1hiqrsmK0Q8v9WqQxlZn_iwdgwUmRBR-zZA6jq0-mt5Eh5FQQTV83sHmVzO1CTmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLjKG5iqBnI5yxRkUVYaC5j0jfU_oHlNUlnzRwQNfxx0rn_M4uujEfYh0BfsQdgq2ffc8_aW0X1Vmq5maMcq9rWO4SvFqu7oA4mvvX58pQTgi6qLm_0UkWQk6lDQ7poi2P_q5_zoo9tGagbJfFwBevelx0bpnbS7WIfI_3l3gtsAOYJOnXY-OQHnKMU3hA7PtzbRbNr1iKfirdY5n48s_Xj15xpXacDm6ruKLnoV__0OgIFnxjPRAf9duVwCKaAKfQ0drvEZr-J-DzqaoXm_SA5GLiJJXdoeCOie2g4MG6KzvREM2yXRqaxi7w2ozrv1t4W9lp_GOveo3fnH6Adp5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXKk335fm_5OhoZTUTrtA73S-5wcNNXfn4vU60056wmwtNzYjKZBtFZRlS5DtO7MyGGhhGrk3BjaXK0Ed4JNjCgo3J3YQ_TgEaXIYLNdrR9qd8zqmR3AoDvXYlnoXFY9_gLxVDaW-ljgE3oPWZo6H82SIFm89D8DP-LGAC0qgl_oVfNhVulT76pFZdoI0yPUNIQ_phHemAjwh8baKa--aC4e39NcJ8aGmhr-K6mKo0QUmFlV62VrC7-t0tXlLLtWIP1afqknhiYNlWsAgWAdD-DEWySltNwu9-Wuynp9YAYdLow7Tg53N6OkP1dc1XcMmuKvDi001rN355aGuNiVCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LIpctTwzvl7Om9JQ9124WKB6ZTdMpAsGJlbyupf-JgU0UrlVZeO_wgo-kOsYDdvZMFs5GnHyJkSzZhjAudbdoi3HjCEw9B0OyXfdpjXAEjSa3abxZXfjZIVHj1MRYnF6bj76fTPNiutAf9flBwM7w6-m-8ySKQkiZr68EQKdcnYdpcxHlV6sLQu1P1Hg_cMTfLRvD10XrPLFgOB5pJKZBrwKRYzbcawIf9FaBxxgANho5OfHknfRjtyhrHAH7HbFDOqk4HNE8wMmNoyD1KrpHBMoHHoGM4C4ZHy9052ZLc6ml1RMEYvIxBoC_devlj-eqMiuuAQnI2wvbRxZwXAISQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LIpctTwzvl7Om9JQ9124WKB6ZTdMpAsGJlbyupf-JgU0UrlVZeO_wgo-kOsYDdvZMFs5GnHyJkSzZhjAudbdoi3HjCEw9B0OyXfdpjXAEjSa3abxZXfjZIVHj1MRYnF6bj76fTPNiutAf9flBwM7w6-m-8ySKQkiZr68EQKdcnYdpcxHlV6sLQu1P1Hg_cMTfLRvD10XrPLFgOB5pJKZBrwKRYzbcawIf9FaBxxgANho5OfHknfRjtyhrHAH7HbFDOqk4HNE8wMmNoyD1KrpHBMoHHoGM4C4ZHy9052ZLc6ml1RMEYvIxBoC_devlj-eqMiuuAQnI2wvbRxZwXAISQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AcZMNPNBQ0Wat0XuRMCJSLCcHSUGGYKBVJu59nbGDGs8DLV26f8rZX3r45jo7RRTmEaYS-3xJxd3kDj3VMR5LeC6LtT040JdmCQdwxMwpN14vEuna37IGhvMU5GdTOyefrwiIcDrJbZjZUOVASctiSGJmyhBPlIyGlArOzO0VbojvxrwNV4ykPWTFcIqAmOE59G8vPsXP4QAQC8x_6i5IhymDwAZq1za1S_NztM4aGAI_8snAh6kO1eDfvZ1Xvk3IcIPFiZGaND6156Wt9oPQCULdi4u2Mnw-kbuA4D5ExjkydJ7F_Vxz-z-wpt4yd777Xab_aQ8PtQH_6SOMXTqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AcZMNPNBQ0Wat0XuRMCJSLCcHSUGGYKBVJu59nbGDGs8DLV26f8rZX3r45jo7RRTmEaYS-3xJxd3kDj3VMR5LeC6LtT040JdmCQdwxMwpN14vEuna37IGhvMU5GdTOyefrwiIcDrJbZjZUOVASctiSGJmyhBPlIyGlArOzO0VbojvxrwNV4ykPWTFcIqAmOE59G8vPsXP4QAQC8x_6i5IhymDwAZq1za1S_NztM4aGAI_8snAh6kO1eDfvZ1Xvk3IcIPFiZGaND6156Wt9oPQCULdi4u2Mnw-kbuA4D5ExjkydJ7F_Vxz-z-wpt4yd777Xab_aQ8PtQH_6SOMXTqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3Kf_eP5uX55fwrL9Wz6dZEvFjqpjTxPVoXTX4Ayu2tyejBVm0Gn5oThhSc7np7tDx7dyDaNCFIzTq-YaFQv4H_Ic4FmZd_muTYwJAoqITIWlobEqkeQbJdWQbc5Kd83YG45E6WOU_g-D3Ch_446rQZIlf4ChrgXc5kSFakDJXzFXUw6wtVKrSQfhO2Ygrp-wh2_PMrN32pWg67n9wtlGbTjLezLXgK8aQq9B1y64kuW2vi-Vm4CG0zxvo4d9sfkb8LLl-XcQq85twIKJ-Nb_g0Rod_y2Mc6BVHNQ0DmiXnVrT6iHrgK4W8bUDSysSnIp32p7jUzcJ-ZHQwa35psyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjW6dbau38HgAIo3Oor7t2O4quNtviSaVRmt69u92pSLXL_gQutGMXiYuNBNdY06D805u2dpUWVGkaHIqCFLBmZEMvfmLoPvo-HemOmS3adjoAvqKyBUccX1FLgdCFmoe1Op2hofLgsAxAVCEUEYkG9vEtAQ5Wn-nMUQT4VB5taJbFZ2H7NYO1f-OyMGUkkEwjr2Saj0pRL-bJ6-p82XepnmL-Zjqiez-CM2wMx1QIZoMastTY9tdceS0LUGlRb_b9yAyq7U_oIRv6yzIb7K-fbd88MyHXAngKPqWVuxipEb-FuQskLWdPM1xzDzpScs63Qv07D9XAslJ9uFe9Lc0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQaVub3hvLdmXAN9Z8vFY9teMMpffZi01teHGf7bQAsf8bABWAjTuYyFWfN16FSs78jaKuPeNlJqfKP7IZmxXM29C4phFiQ6I2zGvqv7vkNJ3YVgHVSUCsb-eT5piOrExg8WA0en0DXGoO8_lxvJc7DCShrreRFlumKazXpww7GqMxsTAymth6NhtvL-gaRfh8_CvZCUPm1gOpQg0GRzvuWxu0usHgRa3JyW1Ak3P471vsXZ4LHfby8sPtdZVJVC3qzo-cTpHdBR8BFzoS_OiMB8kvse5zDAXi5Vr5Mq5Esc4IIItXa_xH-VPblOCaoEgRqq2e4J3XVLLpv9He0CYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXoyHi_48UsmmtjiqVoyzT5lOYPg21K8DIieDF-zm3wx9hdItqYHIY-5xiS_1cwlZhq_ik7FZiNYkmY7o5OoTAJaqAZsKWa_fFdJUbNTEkbzFQyWii2kt6-FLCelHK1AaQ_QO269LeQNxxAFW4PWLI7vEe0B7vAeE0erDXlDSj95rcDMQ2sb0Ub-dSBgAJEkv6MDRfSRJRefWMgQTnx75rrxg0JfFuVo_slR4hfpbgS1OPw61rQz2c8My4E6HM15GmnfJzDePMGz1muJUcEvNc5N8KceE-uvPOLsRTduGZBe1wdewV-YdYs60p6neRKtvlECe_ZbsmPXpEkzp-2NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=WNbyAXppbs7VZXMxM5Zp7B3mtPvBueBD06rLIqknqY6rqJ5KNlY_RAHFwRbhZATcyWSK4iGpfj3EwmTs9kRonne072XJBoxjjq1fQ_KAc_QqCrgjKJUkfB8bcfTRFSyjhYjP_dHBuHURoCrbw-ebyeppicgKmU7d_oQiuGwlYMApGHYc4fovV_dnJYp6hcFs0bTfMlJa9TAVcOm_M0YbwCbRotZjs2ESLpPhVSDFbMyRAeXEAGM6q6mZx9o0XP66Fw9F8xG_qTW7F2lXivuPbVPpa1yZgLrPRHqnZvcfi0MNugJnJg7x8lfeeTVsX1v00baisAV_2dCg5PWstUexhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=WNbyAXppbs7VZXMxM5Zp7B3mtPvBueBD06rLIqknqY6rqJ5KNlY_RAHFwRbhZATcyWSK4iGpfj3EwmTs9kRonne072XJBoxjjq1fQ_KAc_QqCrgjKJUkfB8bcfTRFSyjhYjP_dHBuHURoCrbw-ebyeppicgKmU7d_oQiuGwlYMApGHYc4fovV_dnJYp6hcFs0bTfMlJa9TAVcOm_M0YbwCbRotZjs2ESLpPhVSDFbMyRAeXEAGM6q6mZx9o0XP66Fw9F8xG_qTW7F2lXivuPbVPpa1yZgLrPRHqnZvcfi0MNugJnJg7x8lfeeTVsX1v00baisAV_2dCg5PWstUexhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHwYhxCD2G2-Y6lx0I1SAFbSCjZV-mgbTqBDXCFNsws4F3AClHUpHdNS73C0KQXF4Y93W8yMd3nFmLOeGX8SnYsF6v_IliIwIz6bW2zI1zTP7myBxSH2ILMvgDyeiALsIScjY3IZ11Kq3Q45903WO2ZuWynukZbYXIRdRGjzE5Jvg_Bcv6h5p4rG4LjVKE7QQeiBBiCgls2Ffn9MGDomsKIsR5o1eqT0neqyW9GtWFH4y-NynVROKvIKJpXjqzh-pq_yvS0du-6-XzJnMTq5-Tl1IQmto-_tKwJQsHlUP10W1tRYNjFJtz6JtFcMjcQSVK54f9jClIhWP-27k167qSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHwYhxCD2G2-Y6lx0I1SAFbSCjZV-mgbTqBDXCFNsws4F3AClHUpHdNS73C0KQXF4Y93W8yMd3nFmLOeGX8SnYsF6v_IliIwIz6bW2zI1zTP7myBxSH2ILMvgDyeiALsIScjY3IZ11Kq3Q45903WO2ZuWynukZbYXIRdRGjzE5Jvg_Bcv6h5p4rG4LjVKE7QQeiBBiCgls2Ffn9MGDomsKIsR5o1eqT0neqyW9GtWFH4y-NynVROKvIKJpXjqzh-pq_yvS0du-6-XzJnMTq5-Tl1IQmto-_tKwJQsHlUP10W1tRYNjFJtz6JtFcMjcQSVK54f9jClIhWP-27k167qSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhT01jvssEkdOT1X0jNZKukQEDknkWBdL5WpAtPphlzy7UWQI7udPVVNW9ewnTHom5cVFKyBElBK7A0CwD5s4AUbLEynYIDrrtZjH_9rVTeiS2A5M6wnBobbdnxcRvtEKUXW87yRE3J8chRImxF76SCPzUL-WDlXP8yi1T9CLwubvfwdwc0Vjkr5wsRODoLYoT5brinUv9326vUzykl_Zk8JXnFuZhYtAuDD7sZ9vGjtBVLkvTBA-GxPTWCVg0SN_XO0rwGzKFJjXMtYBLVR1uolrnYlj27fcViPf7MjHskknRFbjVFhgukXmikYnQG0GnR11A_GV5V7YcfP8LmG4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCOPyxP-PQVOVGdXt6fclOoIjwJYU_D-51Jlgdiq5it18XSpsRjbS18hCiqQfKhtRMIUvotGGdJugoNdKAYFysnWSttizgzdqFTNdiyOID6WTK_yg-FuzVBHxNcKAq1MJYAzi3qwT9TAjgdqAy1NJvJbggtr8mWiwQRxceKTsrff7oC1UIw2Z_7HRIa2iMZE41WINrYFpU6-Jarw9kbvvi4W2SSkLupKiZEeo5tncC1F-U0eKtWzy6gdTJWR8LkVG95RUGmZUDDuN99J9p1q6DSr5wuKRTEP0tFowKLxAnk83O9Y7-lcu3SXvTfFXjUnD0XBdn_Ip3Vg6AkFAyAPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTqqVwe55bK4wd1DZNfbP_Et6i8Ggyuoyc584X-FF05akH8bN9cCR8LaEXAl7GAKxgDYNQU-IYKpIJsCoM3RCsSUXVqlj30HRh36979MmBdx1CkUw-xJTpuQDVopzfQn7uSc9JMetpIlU3cIH-d4CsAZ2DlYpORk579yI2ENCT8O-hppRJhd7p3qYyBeCrzl-A5fwG1ogrq6eTELKBQndnkCZMqWKi1hbzGNFkzFcGU-QCUuIE9TZK5R5cyBnSbftyLgU_yFP4CiDZRP7dzlaVWkxSxHYTijBF8Bbm3TX2Xa3DhUaGk8hGajaS9btAFme-2HIjk5E7X8cpfiiXrQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jkzc2ZjzQ5IxYb_FKjjRt2ZbhclVw6-f7iD_lfcbA4As8YVqEvkFiR1n1_9VDr1Zoqw5KM57pP2lL6A1WZ5gCCWMiTUuLJyIpFS7kIbzhDQmp6n-97xC-EK_f8k2cnrFxoxMscvc0gOQIiPBeJVTj2CawItPKOnR6GmS1rD5fLDguC_z0j-sJSOsvhLUcMH0fxD3f2dJjVHMjptC9JM88d1ZrBD0NreFJqPnrb27qwWNp18DJc1TpmvURfiFw5NjI45mTUe0WsB_Xt14HjoyquXJ7H0ewx8QMqCZckGq_StWTmVVVCNxe2jPQtzkN67CuPy_MjQJEGvA2_J5UVxfCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rswGudUU1SjLpGv-U7i_CixV992fGs_NFMUMPrGaIkoGnJvYRnf9D9TozopWOwIvGsZ3l7VNRFShvLvF8RLKNWa_bnboF09jB8CFpjn6WLvGGrduPthACSLABGD8251QIers5RYMAsAk6uDx6ddWKfnI2qQsIkwS9w7okH25EnFGhgBMnumx3MdXwxrWj-lxxQlP1Yn2mqwyg7CDSS6VG_v0SYGjWuTBN-nH4YYfj8zRYUobTVjBnYmE9rQ7mjVaI7DAdsQNyJKEYTr08WsKuyvV4357mOff4LQ76VU7wMuFWaGj8B0QiCpqQ7QOcktm49B06ZI6FaZQ-tZ_euTkFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZUcMSQCs-zZcKmY03_GDsRBeltGbFKrehvsy46hGYAH_B6Z0QetZhJANcNmq64ycHx61kKOQJ2Ei1sBTjbpMaPkh3q4JJdNvWKy2D1QTdRQLldb8uZCKTyDmlrQlsdSrsR6ZcETH2irZld_nHKNg4H6AkzyLrUaCpgemYtOQXLpfSwBcpYD6LrJ8czUUG5aaLjNIk7O2AVFf5f43tWOR--6rZEFP68MoLDMhfWMhx0W7fygXTl1w2IT6OVJoi-fqW40-w9QjhkatM6dq4XBXl609k7hlN2FBkG_lCsTpHKnJTDloLVsqTIJjZRbQLf49RvApns4PhAQf4bIG-Mf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=asNmTsui9L4F4BvntQyP4cMuLUE-nX-oDvHXp3a0Xek-5ysO7AuAKNpYUX_CIjMjIHc7yUlZHK-5wn2kCoVt8kaIRTPEuiJYYngTyG157g4MpU8YFcQO969m6VmJsr1JkkgVTZhkZDbDaJ_tZ85lFMa9YjR2VaaKEcBlSQxioqOiwscZtimDTj2L9Lce_2LMwf7WybtDeVJl8fc4fKBvr8mQoQxA4iuJPEu7rIv7rVjR1_ETrEGdRkC2Y7hIv7TvCQT60ptbyi5a_B6wLYD6wI7YeCA0vDB9Z-GT2jRLD--z6edLQQ9VjOlxRqEr1WLfcpitkNZ5EIyzbG7XC4K3ZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=asNmTsui9L4F4BvntQyP4cMuLUE-nX-oDvHXp3a0Xek-5ysO7AuAKNpYUX_CIjMjIHc7yUlZHK-5wn2kCoVt8kaIRTPEuiJYYngTyG157g4MpU8YFcQO969m6VmJsr1JkkgVTZhkZDbDaJ_tZ85lFMa9YjR2VaaKEcBlSQxioqOiwscZtimDTj2L9Lce_2LMwf7WybtDeVJl8fc4fKBvr8mQoQxA4iuJPEu7rIv7rVjR1_ETrEGdRkC2Y7hIv7TvCQT60ptbyi5a_B6wLYD6wI7YeCA0vDB9Z-GT2jRLD--z6edLQQ9VjOlxRqEr1WLfcpitkNZ5EIyzbG7XC4K3ZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=G0hpdJYDCJKmpzMCF0vWZmb13ZhhHKppss-V1L7lPJ_Tz7tncTsKkJGqZpl_eqI7kNwZqf2wWEPpdZWY1Ef8QoCfph6wR7l-tc8nyt6Oz3JQEAPG8b9piODudwBrDi_YgkkXFI5nXWvW42eTnAWDdGizEqqeleSFbcQ-q3LdceDo0BNaWD4nbCGjmVp75DQNu1ah3q8f9NJAXfmrWm9KDo54L4OpHlugL5osMKv_G0KuwT8I-KVNOwJTSa87n3eYxpUC5ANGisDhebM-SCEaeP9QvgEjh1c4rvk7QhHoVEc1no2V01kmteMxNjwBtTXOsETxT-tws5BIH2COtSdLs16yOBfHAooXXUiGM2DckrRsYwCDtj2mION59x0KQMonz5GcK4kZqQ-xELUMHgs2e1HFVveWd68w2ulKZQTHeUZ84hNGQexbCEJcmkTf5jlh1cDxGtVZZu5rz0igdRDfVEr9XsG-v9Bh0s87Kcm3z5LDY78FH4jVnLz5OQQ6suNx3giLn2rPX7LHmF-VfMXrm2YdC9-9TdwNKVjVWDreFF73JUV9m-HsDcElAKTKvjpdjqHpn8igJs-E2bmFBAjONz7JXB9T44AbBoVY_vV1_OaA1E3bf7u3roTcbzmPICpbxE9As0Gy6nistPr0U5g904ulLBGz6i2LOEYfWFy2lv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=G0hpdJYDCJKmpzMCF0vWZmb13ZhhHKppss-V1L7lPJ_Tz7tncTsKkJGqZpl_eqI7kNwZqf2wWEPpdZWY1Ef8QoCfph6wR7l-tc8nyt6Oz3JQEAPG8b9piODudwBrDi_YgkkXFI5nXWvW42eTnAWDdGizEqqeleSFbcQ-q3LdceDo0BNaWD4nbCGjmVp75DQNu1ah3q8f9NJAXfmrWm9KDo54L4OpHlugL5osMKv_G0KuwT8I-KVNOwJTSa87n3eYxpUC5ANGisDhebM-SCEaeP9QvgEjh1c4rvk7QhHoVEc1no2V01kmteMxNjwBtTXOsETxT-tws5BIH2COtSdLs16yOBfHAooXXUiGM2DckrRsYwCDtj2mION59x0KQMonz5GcK4kZqQ-xELUMHgs2e1HFVveWd68w2ulKZQTHeUZ84hNGQexbCEJcmkTf5jlh1cDxGtVZZu5rz0igdRDfVEr9XsG-v9Bh0s87Kcm3z5LDY78FH4jVnLz5OQQ6suNx3giLn2rPX7LHmF-VfMXrm2YdC9-9TdwNKVjVWDreFF73JUV9m-HsDcElAKTKvjpdjqHpn8igJs-E2bmFBAjONz7JXB9T44AbBoVY_vV1_OaA1E3bf7u3roTcbzmPICpbxE9As0Gy6nistPr0U5g904ulLBGz6i2LOEYfWFy2lv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=CRdfpSs3G2iCJDHbelwNppcp9YQ9Y_eCLNmEkuN3XRtQT3Vk9F3V5G1AM71X_uJl4BcxkB_OtZ0lLcNnTcZ9p4P9Z5gnS-eaG82FjHpJk49WHOkeJTp5Vg7BFUh6mPJ7RDIoupU1rK8OD-4Dq7hSaJrTsGoMaa6hO2XcDKdpe_D6B7ZHdKdxZL87KfdRhGIg9xtPfbpMfz3ESBipF3AmaIW_rpIcdie3Y3syu-MZHD8fqGvnKoVBAAOPR3hWBJc6da5Eo5hjBCSKUWNx_36vvuq1ZQH5u6aaqEUCI2WYUJzT6D5MfPtU-AlL6di8w7pDSTnp7fuxAo-t2Q2VLrblG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=CRdfpSs3G2iCJDHbelwNppcp9YQ9Y_eCLNmEkuN3XRtQT3Vk9F3V5G1AM71X_uJl4BcxkB_OtZ0lLcNnTcZ9p4P9Z5gnS-eaG82FjHpJk49WHOkeJTp5Vg7BFUh6mPJ7RDIoupU1rK8OD-4Dq7hSaJrTsGoMaa6hO2XcDKdpe_D6B7ZHdKdxZL87KfdRhGIg9xtPfbpMfz3ESBipF3AmaIW_rpIcdie3Y3syu-MZHD8fqGvnKoVBAAOPR3hWBJc6da5Eo5hjBCSKUWNx_36vvuq1ZQH5u6aaqEUCI2WYUJzT6D5MfPtU-AlL6di8w7pDSTnp7fuxAo-t2Q2VLrblG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/checOF0Pk_W-2kYjQ4Fr8moKgSPKLM-sY61NdNfvI4Fi2Zgf0H5XDOILq3-LqLEYEAlIl55fxSK0jDvRlYiPW8HqeKU6G8fO4DGVm6OiYzCwTni9l4Q59mDAkEfyjiR3blyPGXXEumJ3ri01vOgTZjPP6D_5ri3Bofjh4FdUa5FOrW-nIL-HI00-V_RJjsChMaMcH1vOL97DbNEAZ8beToH91pvOVVyIxQomsBa3MaOkQ8q_OyCZX0NwILXSCMTneufmrKyvXPTCoEEpBkJZlkP115G4mz1yeoixLjQ-n7XspjQwevoySLiBKfyOJXynzIEZGej9EaAnnTg4Wn-e0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbtLt34RTl8-RsS6uPYDng_gvA5ZR1xW4QVDvR4nFa3tvEJdTZxdsvn3YQ6nXg8uUwkdOKL56T8-EUjfqodSAWbUbajD3vYhriY9MX0GJAfz9_9N2eS68lgqdTHvQIwNRrmuoWamQqA8XriNI51dXw9ry6fR5tvq2YrZPlSKHvUMAQi61kXy2M_gxynsQArgKBuSew-QtCV6KZjE7aWsWpB-0ulnlVr33NvHtxA1MMTcNvs0bCXL_pyJ1V8Z0hZedecJfWlR0PbGpCGpNGWrUOFxaAZvMurdi3EnVYUHO2sWlfkTVskPuWAeZ0jeFOxBWtEF_mh2d5-m9kgtXds0tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6Rz3sDY4iw_6NUqyes7opJ4XZlihi-xE-JVcXwLVdA59Fa36hcIjA1HwJkwrKtzCw8LQo6O-ubrEUssAP5vWnpeGk-GUWBT-ab6vRszdrlG-ran5if2ZnECtZjDKsJHJxQuWzOlzGJ98vPDFk2chGXm1HU-52QbQccqSomtI3APpWUCKpJ5MIbfH004Gu25_Faomc-l9GMmU-X2I2zMZdyAObKQJybzO7-W84JYbBjzNePQr1Yd47n5XmKAVoByCk9Quc97_KfYo4XjIqeeD78Eqx-R5M-JL_FdrfjrOyeFA47bYeAciaSSdJxQIgz2g9BzYiCmxJJiaR80dpurXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajUbdQ7lIM_cOJaa307wdC4xsszU9PzeiiiwqrThJ7bFcCgPuQFOjnixmokB3h0KhHlvDdYw8apohQ4v6qRCJoScArTNJk_fUNlES4OiXGXwMv0wbHb7TInuUF-4fv6Wv8SbMIASNxOIeVIeKGe_T4T4xamNGz16_EwQpQPt1RieLcczlE79yVIFsLC0TCKw0_AaKM_l9vdCc5ZKPEuy9qQLzfkJWcgAO2HSizzBALhSsesfq-ls8e5wtk_yF8IjLhmpez0qBppC9Td75QFeOiimxo4Q94lMzmYBDHhYm5yoYGn9Ccg8uCgIATcOdaxqIODpEd8lhG5yZenR7VSMiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ottg48coHMid4Z3Ne75XI_kSb4dEIsDYOg2Z3goN0MVwCvkmuO68bvvB-gJbq5diiv9troOkmpMFjcH8ADFWiZ09OaStM9DTP0_DxD0PnOWMBXiE5uHtmEyshxDffNR9RXOT3G9YPRkgfurvuttmJ3MFhn0RHT6OInZ6mHuva-tZoJiLzacVw3R6Jbmaz00GD9sgz00rxN6D3odeJB2Er0KQTv3rdOvbNVHV-jcYV7PzDX1njewqCKT7bcKVqZ_007nn_0fa2WIga-hCwcARarq4_H0RiUq4kgPTdSnJ9x6MsXdmAx7J-kKX0wFGfXPE-LKM_78bEFrf7_pVwciN3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=P1Ngm5p5UCjRczbl9GDkkgHIalFvXDjGesRr6qKjy9BeB0bqjis1MlNl4ZvUedR01lGXB2jHlzvPkN_NMZpN2CYk-Xboi98IKHlTEU7sGD65Apc2y7JWk1MvPzMp2aQjQefiC0QgfHGfT96KvWbyAvk92ZKhw2s8xZoW_swM0UOk2cFretf0TNCuV5I6uMIp0nudHHhXxaBVMSiKfogup8Q3tZ7XMKxMdlyqETbXl-Vyw_XtlVvu4ckpMpC3S6bP-6IzpIr9_iR7_WdG2CuyqavqmYYELIwEq0dWmoqnX_Wolb5ALpFfm4alnCCq_kg_HFHcCbL8_CfGzKX368UPvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=P1Ngm5p5UCjRczbl9GDkkgHIalFvXDjGesRr6qKjy9BeB0bqjis1MlNl4ZvUedR01lGXB2jHlzvPkN_NMZpN2CYk-Xboi98IKHlTEU7sGD65Apc2y7JWk1MvPzMp2aQjQefiC0QgfHGfT96KvWbyAvk92ZKhw2s8xZoW_swM0UOk2cFretf0TNCuV5I6uMIp0nudHHhXxaBVMSiKfogup8Q3tZ7XMKxMdlyqETbXl-Vyw_XtlVvu4ckpMpC3S6bP-6IzpIr9_iR7_WdG2CuyqavqmYYELIwEq0dWmoqnX_Wolb5ALpFfm4alnCCq_kg_HFHcCbL8_CfGzKX368UPvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V80ntCerse-WEnLob9GW2KOtc-AM2mX_p4K80KqHgTxwE9IrQi5jyP-xx_tqqGusy5XRFDi-iyJdXBEIWQVsdNn1acNJNdYXfTpp-ehDUukZTH47kYOlAKa4C3mCbCzJmSeWZRi4-MqTXehw7fqJp47ENzuDU3XCWcr_s5srbTUzBGsl7MHtZZ3hAjGpVuWd0W_vJMgc4BaXLA1Fbnhxh7xEZIa6RFUzQ4KVfZJXuMth0e4vgRpW0Y1LcjWHpzjge9K2y6TEvU8c5uFYl75BE5o1Hy4CnT6P_fHwtX_LPAnW-Z9zw3uwI9T4I5RuzyvM_UZcCkgbOPhBfmFyZuH4uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3l4oZaJNfF_lQKxfcnPWS9skAivup2cDlIOOg8jva0Uya0BaHcZtUIw2tQ-LEgSYqbVg9XnePcTHRhWg6PLiM2TcPd_Qpk5or0AtTKnN16n8SUvTNtHFoeXJxqp8ooZpvimu0bVbNAccgynocYFbTyACZUd_O2g8tzxh5dYErTFxXwJOplMKeT7WmZFonlcml9M0jaWNsqIj0DMXs7GWiTxX-v77C1NQJo3bzoqMS-fNTGyDsNHYXOeaZOEExtop8rz3snv9nZV4YPyNo6ydXyJ3zj4AwZlvJdahAKK9_h4mXkIpGoHkr38X3PD6tagiS5Hvn9nZ0wI3wC5lsX4mQ.jpg" alt="photo" loading="lazy"/></div>
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
