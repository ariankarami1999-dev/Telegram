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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePTWKuUcLKZhe-gE4mGHKzyqUGP8v_aCFQcrFM6ceOdbTSfqlZy8-1XU1ibA0_mJO325_RmJpeA4CzihUY6akwFT4onyrm97JqXqrfXwjSAf7eupaIdgnGAA78eMQrciC2sGKzUJKMCoe64EkpNm8P8aIwwULRvT7s2W3Xzb3k6i9vFTc7DeZRpa6oCm3-Z_Hj36dH-RT0RUSwpK8NFMDjkItR0H5N0uxCD-2I3hEcwUqG6nh6Qdz0jZnH_ST6pCWH66CrMjWGjTlKJyH5onXES3EZY21YNYt3WPWL3eDQ7OhRo80Rt89foS2KO7PxWLecu4vbBrIu4BIpfr8KT-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOXBK7jDEPtL39ZHsM0bSeXDMcIgb_643z4pH0Q2-sZea_U4GxMHgZFKeWY0p2f2_ple1jlIm4jkrrKm9TR3KYFLV-n1u-rDLP7RjLHgLiI3h44WwxO_kP81a_KmSHOpy5IAutjak7vGux_VXbBKoJt2Yml-tSMkf0DjnWRhzkD-u27Dehnx7dehTSnWkAVPz0pnzlhymR4Ux8GHF8t1ZX7vYQoiMxKhhuNcgwu1IpTwndCVMLRVj8VPjVeo0VTylwoSOTufNgPipyg0EUHzO4oh05wd4gW_UJ_2m06ltb40gwkqqwVnYKlbM1SijqyP8BjTheToEuiLGt1RkCk88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ah8B57JcI_fq0s-Yd6W0H6PViNp0TXJVyWU43jL6W98k1GJl-FEddc-vm1SbEUAUbw6VfAXA5DeW5CepJUCsW-tRKPHM3DCD2IHyv7kXjCw3lMcj2HgGhdLyX81LsiBx7-dAtW5UU3i8qxaBbjaBCaliSsPBXz-ru7AdGH7OwR5AhvvFkw5yF-J8N0cDF8QW0BgxcA0iNyeodFtTe340rQFwULe080Rp0rU7btTifDQriUwAyoFiSAKFJg1ffis9q2YaGVl8skqw8dURfW6MpRxjpH1gelxFBHmE1jq8F03uBM84ZmkDTB0IwnXMpJJC0SCfuh9B3fA8KybbGiv-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ah8B57JcI_fq0s-Yd6W0H6PViNp0TXJVyWU43jL6W98k1GJl-FEddc-vm1SbEUAUbw6VfAXA5DeW5CepJUCsW-tRKPHM3DCD2IHyv7kXjCw3lMcj2HgGhdLyX81LsiBx7-dAtW5UU3i8qxaBbjaBCaliSsPBXz-ru7AdGH7OwR5AhvvFkw5yF-J8N0cDF8QW0BgxcA0iNyeodFtTe340rQFwULe080Rp0rU7btTifDQriUwAyoFiSAKFJg1ffis9q2YaGVl8skqw8dURfW6MpRxjpH1gelxFBHmE1jq8F03uBM84ZmkDTB0IwnXMpJJC0SCfuh9B3fA8KybbGiv-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=QbhMLfvaZGwpByjEtIB1lWlqnBZCUUiVpYyRv_ZIZ2ab4JGpv-4qlQ1AFPpJj3DwWDdGFDINyXInSbfQo_L9I9pXA9sxVc_W8_lNztqU4aJ4Y2KBsAzR8YAY5yHHpyyGrvVXdgXSqg-uRUw8Y0gwHTwWlsHcPyD2ZViHhn_dFo9tSr-nQvTu-0GYKqMxHXm5CuzVUz9WL6rpqqxxwsjeAARGzxeHLfSft9CsAwESYvtGAwggDyacF9K924-ZWUH_uQpEouDgiOqXpIqaEYmSdLf-3As9fw4IbCknZEmUayILC-XpbSzD-zU7az8cEhnLNWcbf3u-H_gMkl3uD8_ZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=QbhMLfvaZGwpByjEtIB1lWlqnBZCUUiVpYyRv_ZIZ2ab4JGpv-4qlQ1AFPpJj3DwWDdGFDINyXInSbfQo_L9I9pXA9sxVc_W8_lNztqU4aJ4Y2KBsAzR8YAY5yHHpyyGrvVXdgXSqg-uRUw8Y0gwHTwWlsHcPyD2ZViHhn_dFo9tSr-nQvTu-0GYKqMxHXm5CuzVUz9WL6rpqqxxwsjeAARGzxeHLfSft9CsAwESYvtGAwggDyacF9K924-ZWUH_uQpEouDgiOqXpIqaEYmSdLf-3As9fw4IbCknZEmUayILC-XpbSzD-zU7az8cEhnLNWcbf3u-H_gMkl3uD8_ZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlxmejmduMljCpoeBrdOTGTSUEpCWKx2Li6gB_MpPkYeOn37kCQ8ZPWhchoSzZ-jxuE2tLfeZSx35UUJmjY3VNG1UU4hgjESWqK343K3QVH7tk-8y1RCEQ9YId0tHB4BnJVj5GGoR8BmgVegpRgfjhlFE0WVPSrwPuWhdTEDVVq3r9OnywlmXozfnDlPBRnZgPhsJQRsewuj70AlwimnErQNQ-UUSdXBBTvjvMxMTVugQ6pLVzG8hn7NGPAsZUnKm5P7PRqU9wLTYdhCUooKYpmTR63E-XaDFAbsNde5XjgU8fOp1uk9Hp9ib3w6TblSuIlDpUHA8IcV_FV-1vQQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5W9ggORE-Wl_whefatxB4ESciQC6PytqJjZHD1z7pS-CJLsPrQ2_Znp2Yilq1qozixWsxK1IyAZCGMt-hqP4oDkHp_IQOPfgpHh8pU4t4iS5v_sqWVefYmX049vy-rIYHjLcT7RPCDy00N9z8Cr5PLjd1VPBWIGgX6KFFS_M-IUX7BDgBHwSFcWwHIg9hZnxQtlagDIS62EIVpy_4d0uVe8hzXiMWg_nG6wLLbg0770K7f8S5Ifh3_oAsNn0cDYy_ic0eAHJPC-Jj5ydQ3ptGuXaeUqkFGGdGClcoil1j8NTFmQ2Sjl7tHqQFU0nwYFWvzudxyLihvPe8VuXPh7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DweQNUb1_m9VhkbrwD5Rc_IcwVhPFQ_bphK7gXAw4t1scDznIkjzsujTAa0pU8R1E9FMrGO6npA7LEHFXP7lFjM9ndjUIlET7Rd_vhEsz0n1jrM0tpnoltyz3lKT5bcAj0GgOWkr5AjGOslgIEZABsPQcWEswY19FsMbiYUU8nAFgUKYNDeviWGz-F4CYO_KaQPTvE4qiEajzrdswVQcvaRgTumWuJDhsPmqUeJqcf0_zYRcrztj8UnIsJnMe5DXKvCC_a6w3XpbgZal6dP2LVZK9OMUhK2wvZQVZXTGUzM1HLJ3xLe5cF2FGwA4yJ3erSIci1TJg5eSq9np6EjzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or9jh83MeBipDLR4jP8hZkdUu79GkZiUYTy-paR3Wjm078foggnvKWW_07alaDlDgHzRO7YFIxIBqmGOzoJJ2082_wbMFOUynRlTmgMasiyJAQr9iP3aaorLzJTw5sk1qvAWvQeXTNNoA5zzTL2RhhU7V0D1aZHG6pkwD5g-BTpl2bFskZ0b-fC5toEVV4xttR5jJud2O0nDycuz_Rc2G9urnzx8MEEt2lv534zMPkFfCJVkABfI8NsQiZkZLD5fTgFBV_IlhKsk3pSqrfcqXqNJN9vpfIdzKevV-QpaMdlgTJURpholFd4fsx7ACn1G5xgcpmpovzXjOUQCHTqQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrAz7TNLh-j45s-aznEr8jqe2gJZa_HKVca62WxuT8aCm-yifVH-B7CniHCadBekjWQnpC6Az_31PiSVgGg5s82FtNnC1TzzwjaZ8-t007MSmSl4EZgJFLHvd_NV3ajnNAHcRnhZPeLb3H1mSF-4MriwRaY16j4sxFDTpE5LUPegpDh3CkJBrYoXH6Nfy91OfRJMmGKun-9fIZ6d8oKfpStdvXwu7yWnyDY4MVSHI1K1OPeLJ7qRxZYjrqbQmGT1TT3-JN_xJKsSF7I01_nWRa1uDzE6meJtZX4ToCJihHU9yZtR8mmMGkg8FNOscgApgWeTESB9NBoo3aTiiP9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=QVz3KE4Xol-P6oxgfb_rYwS6Ht_a-CFfzWDmBwM-lfnRQ2GxIReEXH7vTIou-wqN1ro8MUFjiyCI6aM5nAtWwcAyzwkOcK3N5SXcn31IwlqLr0CM-2KWMcPicUJCXnpaaW8JqqioVHyHq6Qi_HwRoH3CevD6Cm3dlkv14_TcDiweMkxjNVOvsIniBnUWfu-GmG92FNmWbWKztgSeCg-YNZneG2Y07rKg_m48CvHgonx4VKAHBrPwxaXJflDwwRST8oawTN6pi7Hds0hMoWmICV1CswSpK0qXWeReVneFiMtyFx9j_8Vo_ojhzCvIGXDwYJU7Yj5Nm3jqOV8xAUMCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=QVz3KE4Xol-P6oxgfb_rYwS6Ht_a-CFfzWDmBwM-lfnRQ2GxIReEXH7vTIou-wqN1ro8MUFjiyCI6aM5nAtWwcAyzwkOcK3N5SXcn31IwlqLr0CM-2KWMcPicUJCXnpaaW8JqqioVHyHq6Qi_HwRoH3CevD6Cm3dlkv14_TcDiweMkxjNVOvsIniBnUWfu-GmG92FNmWbWKztgSeCg-YNZneG2Y07rKg_m48CvHgonx4VKAHBrPwxaXJflDwwRST8oawTN6pi7Hds0hMoWmICV1CswSpK0qXWeReVneFiMtyFx9j_8Vo_ojhzCvIGXDwYJU7Yj5Nm3jqOV8xAUMCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bafd0-kIqv3Uy-_Qe6IsJR0hmjWY9YKZsCd4MrZ4rzh1pGiBs5SeUFd22ecj9fXjIvBnT6Hu-iG1jSCFv1CagD7Y8AB8DptXmx_RWUOe40208IiKdvYil3WYhuqu871sk3gKCXEib4QeOvsG_t622w7S0P0gqbrv6pWkSeDs-YzTknXbuCuH5syQtBKWHVyb9oRuVIgutjCPGlHdbrgUk0IefvPJZI5IZUcW1ZFQ1Inci-Yjkwi0w5NPoKtn2RK7V5o8vUTSb76BckxTF5oebWcm-F9s60FmeK8RrHoKU2CrBT3rYMIuePmjVtzGsbMQGkyoquEsJNOHuJQ4IvTjbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bafd0-kIqv3Uy-_Qe6IsJR0hmjWY9YKZsCd4MrZ4rzh1pGiBs5SeUFd22ecj9fXjIvBnT6Hu-iG1jSCFv1CagD7Y8AB8DptXmx_RWUOe40208IiKdvYil3WYhuqu871sk3gKCXEib4QeOvsG_t622w7S0P0gqbrv6pWkSeDs-YzTknXbuCuH5syQtBKWHVyb9oRuVIgutjCPGlHdbrgUk0IefvPJZI5IZUcW1ZFQ1Inci-Yjkwi0w5NPoKtn2RK7V5o8vUTSb76BckxTF5oebWcm-F9s60FmeK8RrHoKU2CrBT3rYMIuePmjVtzGsbMQGkyoquEsJNOHuJQ4IvTjbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqzJiYJ-R1X_hvrGPhUvALxslTJF834CodaJGiUY9rJettDXKFS7mXlLhjc_75NUBFFs0B8ioarF91bG2C28BsyPmlVMRFJgoF3D-ahd0kHpCEVsSpHzCZ6fdToFxuMf5RviTqMHTWxNZOG61dWiHzJhY6ql8NHfik0lrHXM0oW6iCxX-HVUL2BXnu5md3pzQBrGC00QF89X7OHoVPCBd1Gp9Yy18FdMPNqh-9GvoedgutYemUm1t1jVEXB9S740po5hDQwfVeKrYGG-8UIiBqq2f27jlywugUc8AhVtGzombfK30RL36o8xf9RIgyTDk4X1IJYvhV4Sd-3uZ8NLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl8t0Rm8L7hdPuqjcALYB9udd1leQpDaIDrEf7wqykSxlQe_A2lUJqt4AOrmRsde29aIYzbR_lXc6B3aGARysvyK0HloUFdfd7yKclEpn-tNZkEZP6dK44FWSMa-d2ZsgFij_D2ylS03T8X6qWDlCOQO9srVuIykyu-b056ozynPbaOsGb-e_txP_pnjsHTzinXd9BV7co1JPs99HsbyFAxehl5-kHaAoNsZ8opemwys7zAdb0RuCwbEEGaRpGd4pFXEXE52QIIrMduhkWslwUYM00SlxBdX1G06AItgLty9olt6ogZ-NHZINxzkXCVkIZaKhTKAsOj77mA3Zg0fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apDHq8XzJwoJsg1gd24Hedwhiht_IUvaV7t9oVV3yi7STuAzhMVNd5PHTB_UX9KBwUlNNt88mo_tPsqTL54DTpBZeJ6NXzwqFOPmFnl4l9I6v0VgcKIiSo73-zEc463BsHOtlo-d6p9jjyZDe0HwRcRSlZ0gUTVQBEe9sTHJ_OdOz0C46D-qlkticdOYW2a4Hnt0xxsz5dZ1bMmxzdeSlYOhZXeUA7lb-E1XDYInjNOK-C6uYYLcxrVCisvWj-BFCEp3755RwEe2707a-T6l8ZwehtH1_dKMOHa149LlR0ZZQlRfmgqT0OZvFhQe1VENDcq2pGiE54eJoWzgkUktJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=tuFwMd5yXNJDJK_KTG6DMdYOEwfYlvbjcFtBWczhpWc-ctLcN395eXIDFMGgaZ1Z-duPe85VVHsGhMa7jzegCNI5KAVZLB8E20uXOnWGdnOh4l1FF1r_WdDWV_4Pbacswrs4eznvR3voJZHEhG_YMmcP7pM0KHR6IohYicDjQBPAmHBU6jC6q8otmzzQD_B-WdjId17kZUPGmBqO3CA_bi9fcV2gpiYoDqEbvw6xGgdvOcMIakozasqV5tgahv-9-ZvgSYaX4-obtvDHz7574RIqLa_5KmIo1nyICaBF_5x_TuHeIliyIJXRoYqfZ61xjMoB0q2vdHnRR4GBCbdZ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=tuFwMd5yXNJDJK_KTG6DMdYOEwfYlvbjcFtBWczhpWc-ctLcN395eXIDFMGgaZ1Z-duPe85VVHsGhMa7jzegCNI5KAVZLB8E20uXOnWGdnOh4l1FF1r_WdDWV_4Pbacswrs4eznvR3voJZHEhG_YMmcP7pM0KHR6IohYicDjQBPAmHBU6jC6q8otmzzQD_B-WdjId17kZUPGmBqO3CA_bi9fcV2gpiYoDqEbvw6xGgdvOcMIakozasqV5tgahv-9-ZvgSYaX4-obtvDHz7574RIqLa_5KmIo1nyICaBF_5x_TuHeIliyIJXRoYqfZ61xjMoB0q2vdHnRR4GBCbdZ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-fsaC3GtqikNgc9m7yPxvmFLp1xOt0plMAAHPFyZ7fUeFhI_XKRY1n3inAFfwRHVqyt6rdYH2CCGdn7cBQROQa7wTH1S6CkeS288LKCXQzW8l7cX56vw8CS0TlNmzevk4mcZiZQpv5zN71ICULG0TUXk1b_aSUGYt7mZ2AlsXdCuVKETOEIVWQsxWiR7BKnw86LuXNy54g5u9P6zjcj3enMz39b-1gFOdG85WZV-T0xV1wAkvuIZfBThDlKOS2LV1dHP6-BVDYP1JRTE4uLhPspFhP2bLE7pwVyQsu-0O14k-vmJ0sGP6G_Yh7jelco9deiODEzKcOftOHATh9hWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG1-3AKxFsQFdLV0hwA9s20x83y5Cza2OtusQIyGy-rcn4ldvEY_x5VGz5znBV8wnqrSZOZYQ0LWTV9Rac57fntnEsM4pmV73id65MUhuURF6vOMUByfsIUZWCFYm-sEaKhwtHzRDpDUO19HkOloebXQ70QRVKOMBpwTxvM37cEBAQS5QTaVVrDfRoMCAZuutNKh6suM_sOuHQOIhaANnr-wl8iw-CyjQ1UqywwnUqDtpJ_08jISBlszcY57WvqLc8Ev_sAC-4N3eGy8Ple_vd3NWzpqHwcsjIxtPFhx2bHI9uwbL3MmqrRJeMTfYt57Yi7tVXFrwUJGt71fvpZ6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvp1_ybid5ntdb_tNTsrJDVU06H3m5JWyfkPMiV6hnpaajjmyVbNMLih3vVgw9RDs5YBeuJataDr9gBly5OQ8C4U8IeK8atPunB24baOKGtG9XfEywGAWh7FItAjcJHbGHswz51IOOhw-V6Iy1FRaECC1mOndOj0omokflsqnqp2rIBuUUfb3TMjbG6jD8IkN_45c3U-E9Q8-_f9G8cNhFU-IBriH22zuz3KnuoF3zq_6OJLz7AIiFqXSCknr0IEadbPEkkbQXCjwb8puMrp_8J9pQ3UNrL2NigdjbmmO5jn4OUyH3lsR6IZvFRz6lThL1SGsIdxWk7w2atJsh66UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA0qla-NcYeK_lpatcEbtEOKMuX8BmWqZzDjcMS-4L65QdUjNI2CsDNJhiP8SOJkOgKzJ91Ae3W4WYJr1BsQt0zNUgS2LW7yt_rUtAaqBGr0QyxkG1cbCPHVQOpEd19sadcXMM4SEpEu7tIfFkaVlWO8Uasjjf46tV9G3yUKp3GMeBnoAl3MgFiruAg1Wz4HbuHcYBB7z_kJVcICJ4opvvujk70IzEdTC4Z33roOnf0LwNHr4sDNAZMmU6ruGdGyPvrbnMXuI3NFboCLrkDAplKyxf0xXmKF-4XDPvYw-q6htukTuBtQL-Uwu5e6_nq-MyhsgtV0ukjwa3btEYDJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=cnjhSoj-McNY-TfA9nPCVJQBRYwyYZczYQ9EYgYPrO-yrz2pbRdoYx6UCYpCvvR-JEfu9OoAAoH4FD53tm74K2snu_E0AnT7Q39t-1H3i__u_qDJ1UAMu0zV4cxrotaONFRWA9Qt8MeIm6Dl93FKPT0JzMC4Naoh2Hv6gbC9faL1K8fpTJ9qJQCAqtTR-gHU3tv3_q-E1oMHznFWLeVYJWZVAlQitJnXvwLjiKmGtgJEqoIWMvA13CUg1RpFGG9xabyjsUntoEKiJt9xydo-REZLucMTPOZ22NGB1izKqJ6wdhX2j-xgx72hPfXnY27BZ0l0QEHbQ0xDq9twE67qlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=cnjhSoj-McNY-TfA9nPCVJQBRYwyYZczYQ9EYgYPrO-yrz2pbRdoYx6UCYpCvvR-JEfu9OoAAoH4FD53tm74K2snu_E0AnT7Q39t-1H3i__u_qDJ1UAMu0zV4cxrotaONFRWA9Qt8MeIm6Dl93FKPT0JzMC4Naoh2Hv6gbC9faL1K8fpTJ9qJQCAqtTR-gHU3tv3_q-E1oMHznFWLeVYJWZVAlQitJnXvwLjiKmGtgJEqoIWMvA13CUg1RpFGG9xabyjsUntoEKiJt9xydo-REZLucMTPOZ22NGB1izKqJ6wdhX2j-xgx72hPfXnY27BZ0l0QEHbQ0xDq9twE67qlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bby-8FOAd535Tmmkp8cDqyOsQQ-mHWEnwZX0SfMAh9i6mCwOQn12nQOsf1ILdYItX8S8eSGBu392x1VoU0kcNQ8UmccwQTwO5DjadgwjrTHun8e6AEIV94vJAvyliIUjdmEZlEX3iWodR6v1kutRy3Vksrwy2yfMGzcVqjOhILhI53EJvlwqdGhrt0lMJYEwEEfBlfVTD00W55QsWAjcf1fyWuezJrCk_EQJpowQYvSksjYsBJy0SlC_IvI34SSj460xdi5oHhtsvDKbKjn48dMpAvfzGchzME_6F-j-sTHJLhmRF0hqmdzHS81n9tGJYzDtNfWj9UPLTY5FnIuthA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=a0jUgj0Li8tB1Rw0_BNzCiHsdcOU556o5zKNBq3yfkkWBl4iH7igZ-OfuYC9zA_Qt4AUWeaF540jLMJqxmN7oOp2f174JJsLeJhKv0QpbLnaAZyHnnosNkalII9b1Ka08LnXpRXEU8ejQFe3vqvZGQcgmgDs_8MJjF0ZCmmn89Yba0ROjaampFuXBnCXOwp_rzy7yWiYQnShy9dwbafRsjAyUoO-OzUckVFi3F9Ub3CAzViMVOU231aQ7NG8bC-OlP-KixFma4OGqZKQprt9vv5Grz0VHW0Pge87rIj78fSbhpjK2BIAVOzyh3tmwPArVQ3CnvODFoeUdjL-wCvp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=a0jUgj0Li8tB1Rw0_BNzCiHsdcOU556o5zKNBq3yfkkWBl4iH7igZ-OfuYC9zA_Qt4AUWeaF540jLMJqxmN7oOp2f174JJsLeJhKv0QpbLnaAZyHnnosNkalII9b1Ka08LnXpRXEU8ejQFe3vqvZGQcgmgDs_8MJjF0ZCmmn89Yba0ROjaampFuXBnCXOwp_rzy7yWiYQnShy9dwbafRsjAyUoO-OzUckVFi3F9Ub3CAzViMVOU231aQ7NG8bC-OlP-KixFma4OGqZKQprt9vv5Grz0VHW0Pge87rIj78fSbhpjK2BIAVOzyh3tmwPArVQ3CnvODFoeUdjL-wCvp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpbIUMzNxubbvBJIfgQwSBhTkj8z4tVdCNsXzriwK2h2465oj1wwQ4hx5bfXa0G_5jygZrU0gapPVoDq7F4w6RAHwNFBUaVpR2D4HSnQkNtjRTIfOJiMb7_-CrspFMcFT_kQ-eI1EbkuTj5sNlrgsCRPJiB3r6blv4Fqu4PuyivUPX6S7x8YG_3_7HC1aoNr7DtK6gRgiilvaTy-KedEMQV6VUcu6CW_M5rwXwHrxKAi1l40ImoSodPdJIyH04ZBagZzEFHhX85M_DEPe4c3SGt3cZeW0mSS7_MdJYdYzmBNIeGrFiq6oQ-cLy6S3HiHazwPAFFwqkHk52PP1TO82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=KuDNtOTx5_A7mCQC9bAmMlff0W2FHYk0kGS9S5mMm_tUn-yxwaQdr-Uxj1PQ3QkXXP9hAVABK3UfPqPizcohPni0b0VpNoW8UexWNHObJ36Unl3fwKCJdPbz7Nzp8rj3aDxdbEIm-uqN-cMzUE0p4LGp1nDdHUqKCP1LN7UihO7brCnPC3IdkC2LR2Lp1Tzq2eiKCsCF4fE1PrEk2vZ75aNCRc4liplj3pUebzsmB7ZFp-ygVzbCR2QF5mBHGid1COH0XwhzBPNw1_U8cuBaQAFItbPeK9_sLu-2q6Lw85P_PtRK6FbgYe9vmKNzZLa1jcp1wfAZG0tjh2zvA9MSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=KuDNtOTx5_A7mCQC9bAmMlff0W2FHYk0kGS9S5mMm_tUn-yxwaQdr-Uxj1PQ3QkXXP9hAVABK3UfPqPizcohPni0b0VpNoW8UexWNHObJ36Unl3fwKCJdPbz7Nzp8rj3aDxdbEIm-uqN-cMzUE0p4LGp1nDdHUqKCP1LN7UihO7brCnPC3IdkC2LR2Lp1Tzq2eiKCsCF4fE1PrEk2vZ75aNCRc4liplj3pUebzsmB7ZFp-ygVzbCR2QF5mBHGid1COH0XwhzBPNw1_U8cuBaQAFItbPeK9_sLu-2q6Lw85P_PtRK6FbgYe9vmKNzZLa1jcp1wfAZG0tjh2zvA9MSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=dfgbbiyd_XIZVBX35QEzxgZgn3kfHQVI1iLNbSHellcHQg5NqqhjNnmUm8d6f5H_LOk2gbRK-3MTBBpOXt5tPU0rU_jSPm3EQM5pQ-taJSEGsA_Ni5cAJnil_VmGLkfqDDuwpkvn3_bOH48GWB8Wl59tofcTrMWmN2yktGkIhzV-fVFBj-hnOF-tuxI10UvSndzo7cE4LzSzU-mVefWA7D0c0bFDa7JUrfUK-OKEuUX8pwsR7T70DOMa09_kgLRjmI4VEhQAoRXY2LfWF0VwqA4qmaa6mljrAZDkmd9O0rz6Kup8i9fNZlGTjNsF3qhaie6jpVgwt1WrwaIbFNtvaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=dfgbbiyd_XIZVBX35QEzxgZgn3kfHQVI1iLNbSHellcHQg5NqqhjNnmUm8d6f5H_LOk2gbRK-3MTBBpOXt5tPU0rU_jSPm3EQM5pQ-taJSEGsA_Ni5cAJnil_VmGLkfqDDuwpkvn3_bOH48GWB8Wl59tofcTrMWmN2yktGkIhzV-fVFBj-hnOF-tuxI10UvSndzo7cE4LzSzU-mVefWA7D0c0bFDa7JUrfUK-OKEuUX8pwsR7T70DOMa09_kgLRjmI4VEhQAoRXY2LfWF0VwqA4qmaa6mljrAZDkmd9O0rz6Kup8i9fNZlGTjNsF3qhaie6jpVgwt1WrwaIbFNtvaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNRAjI9CaUwyAf7qLJCt2rI4JCM5p9FY5w41HuCJ0XMkc_-3ggMVOSfUgSVdZCIn8wztvRKpyH7jxlaRG8y13xDHFmE_pyZxBUcLYypytECdxvbNmvHoPAqzhsz-TVYDPl3lDoHJqXX_4aPPsQMmmOu_4Zkuz_qmXd7l-2KlB-5awAUJmFrI88ZS_C7XngWvrLu5sJxSbvuNAJ8FbLN-Ar0_whEanQdeAficCOLxQOPUEfYASCsDOhNU9uFExDQ-WW09219-Kie3CiXwoYik8I8jEItGTbaYsG6C1TPZmSHpEZuAN0MAiNq4hRhKFq2X9PTP6Bn2sS5gJMH_p428YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIpIprE9vYxOocdWjiHhnZizNv--59fWqsBLsl8HmLiBAjBk7WE2UBJXVvDBtwGhykWOMFp8ziAL2QuVLN5d9HioEn0vNb2XLKYVY4SiCfsDzIiMmN8LeKsWkn7Fpk-ZW0X9PKo6rvMhNTIRg3cl-lO74ou-7vvGynJem3llqAN_YF9M4vY-3GV7XIHx7aZqPBbnOgESDPd-AxUqvkY-1O847Y3XXbsRHodZBr4hxQDIfMIcY6S4b1wlBkAyH1wzC-w4IDkuvxhQVfQJfDIuW60TqH4l-ABdpdtwp5V425KwlkRje8Q-N1kg02a8b_Tuq4ArKOWAEAcVObfjSJ8kXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irVlPC1m0r6mUY-nAq2WvTz9KpEbono9UOy3vj8ceAjnTOyF_RqeJHZT31kMMPn06laEj-nrlwcY5OM17NgJ-CBo86dJe4enPM7nVWR8-dDhdNN6IGN1X8ddN5DHHTiKI_2J0GM5Q25-WafSbz8N8A_pUzfl5VmL_lQsHp64Bgx_0ELkmxlBUh0NP4f9dkrc21HYGN6fiAYWyEUUhBpfeB9ZaKfNRc--PM7k4rU4myWn8quYG8emNmVxHHlq8HdIm8B5VaGaN7euJOmEkqv4fALjrOOIXdp90RtbeHew2sUmNtxrYU_s6VU6YiQaxt6ewekJ2xPpcPpKNCJfNcG9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJuMaU8T3OWCbUcmgPulqn1m5S14kC0WESMMNnfkWTogLmmFwxnlIrGPCDiCbCXPjkF18RXZpUSZ6QsCibUnGPu7u3shRKZTyLuUXZuEmOv7WX4wKvkfxo7_q_iLo9Uj0fDSYxG93X55gIB8w--0txrmNOuWu9Uw4HrHHBsV6b_LiExy6cpHlWqAG4CAUE6x_oKkqubkUirHH2cOxrK6_j5JWebzot_CxG88n3rxZyfWMzDNG-M2F9EZwc8xikJKjHrb-6CcamVD6AjyK-xCDbGdg0hCUIWYY2Fnx1hBJoa_UBXb4Q9qJiJospN6a3ybHR8xgHpI-RghjWxw3xmYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=PkGn2xDb8h1ugUM8ayUdqWlyPBUwMo7vOlDD1QZ_jLyqVSndM3ry9evG6lVOdoth537Se2INSIr0na-KdEzlWiHXobeN3XSUn9uZ4vPffPEmNMi1mcntLcce8T5xPmI9eOXfrSbgoI676RHA5sc_5FMIiZmrzPuQe9RD4yZfmfucKutenW6gSwO65yvXmPC3SJ-spHNmEZJ287fDeNA18SsIp40y99oM4erqtkM1Wqdm-yTuwlSS_nkk2jlJVQ9f5WF75vcH0RJMKz1hlbuDCyxVArfItd-KxUbrizvT7oSThKbZYVwkZo7pId-ogF3ju0iIpiQocPE6-xPh0PmfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=PkGn2xDb8h1ugUM8ayUdqWlyPBUwMo7vOlDD1QZ_jLyqVSndM3ry9evG6lVOdoth537Se2INSIr0na-KdEzlWiHXobeN3XSUn9uZ4vPffPEmNMi1mcntLcce8T5xPmI9eOXfrSbgoI676RHA5sc_5FMIiZmrzPuQe9RD4yZfmfucKutenW6gSwO65yvXmPC3SJ-spHNmEZJ287fDeNA18SsIp40y99oM4erqtkM1Wqdm-yTuwlSS_nkk2jlJVQ9f5WF75vcH0RJMKz1hlbuDCyxVArfItd-KxUbrizvT7oSThKbZYVwkZo7pId-ogF3ju0iIpiQocPE6-xPh0PmfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieCSlV4dNTjtCmmIFHjXeIy7Cfx1zxXuJW4IXmJpiSW0pdFALgq_kmbILbiBOEkgerl1Ety7sDsbS4IPEi81KCR4IbSy4LFeK-cxbnay9pMrzo3vH844aA9iMtoOHonZHzC-CYUglgGdffc019yDrBF2M1GUQTyDYVEmtY46mwI7ml5ovgH2T6h0T9H3U4cZNraoLMshadkxONeFesuurXTMg36KqlqzuPGxiVGaj1zFGx-V74-CTyb2DI0jH70l8t7LKy2jTIdFYpTaXtpp_LGrFwtrA7F1olK2prBqK-BofHFM1G3eXoFeuJPhtkKu8dI3m81zxtSIq8aJfUto6Fps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieCSlV4dNTjtCmmIFHjXeIy7Cfx1zxXuJW4IXmJpiSW0pdFALgq_kmbILbiBOEkgerl1Ety7sDsbS4IPEi81KCR4IbSy4LFeK-cxbnay9pMrzo3vH844aA9iMtoOHonZHzC-CYUglgGdffc019yDrBF2M1GUQTyDYVEmtY46mwI7ml5ovgH2T6h0T9H3U4cZNraoLMshadkxONeFesuurXTMg36KqlqzuPGxiVGaj1zFGx-V74-CTyb2DI0jH70l8t7LKy2jTIdFYpTaXtpp_LGrFwtrA7F1olK2prBqK-BofHFM1G3eXoFeuJPhtkKu8dI3m81zxtSIq8aJfUto6Fps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmA-FRhXaEB4LDvUFcfZaDSil0kq_SwNRIDvyBvvrzcDUOggUUrWkfapB85BbLslipsZly0YUkBWSKm9oMPvQJ2-yvz5Ex2rukfb9BJn_5rhzF_yclEjKNT--1wOn4xeg_pev7BTe3HYBcNsbdCQnWjzuuxpiGCmnCXd_zYxOY9wMZyVQxq71enAP96wu1NrkSna29SlBsrxsKxhvszspr0xmpdp0THKVlaHuIx-JHs1zPxOfSUXZKBFD7cQXF9LsliCpoyA0kKx8kRl4W9VrWVgROp5Vw2fe8I2ps6vd8_3MFvnHGOLgA8DSDTC77wg_16KjLCwYTTWnMshkrVjCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg3D1iG382ywBY_h18-jysgKg6l4NAec7Z1k7eMk49ua-_KNdri0zWNYphUc8BdcZjH5OWCb2u2AXgJztPe9wEvqjhClYdgGh1ntmMQQbfujbMVCVvK9pnILpo2p3pPIkxoBipcmc79ZMCO8QvHuz2JkJTiYY78ZsyQZbdMD97nSkvbRt9iQri7BJXf3L8ruF7OPc3Wd5lIiNWjkY1Rz4_ASLr76hLn6ktAjf-7zJPHlZyroKRH1RHZ9dcBtFKfW9YYfvGDlRL9FT-ZlhX-XPCt7W6qhQzvrnkGzyI1O8HIzeOvT1n66cMh7ZcrlSkZQMfM3Su2AvH_6XEsRkXzG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTxE2T4Kw-JUsl5HClztquvCED3PhacosbRUliprAcgzawL4D9SOZvYK1oW10QuafFyVOtR60F9nA7so1aH5fBcwaMDKAJjpy-o9ojRcasi7D_y6IoDAoiPU_gjNVNJ7Hy9cMiqWz7D88LKM6BqfriKF4KjS-4QCTDLYrtk97RlO6fXlfX4qM2cjXr54eNe0aVctNIQxm5rtn2W67yQHoNkYHbHye1N2E_IPkomoEXEIMzm31vJtClTcSdWLtr8rQ1hQDhmIMgkHyUEauxzfHsf41hjID3NsDje_AjdP3z712u4J_PZJmm5PXiRpH0UyZSPtEyc0GM3ILss2KYkaww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiZeUe3GlP25iuakgWH4sBrfdMW7JWBnk2qv4JYrcv3StexPJ9RDKR9ItUrQTTmshpLMN3qCTtNFbJNtiK1SQTEoFh8vavzsbn4sO91G4oMgA9_kic_HD44pgDYyke0HpleujPWMCYAuGo81g3BsvX-q9VhmAQgTL1ImLA1XBsBfXjq1Ots7UY-tz8RIBn6A4yh79j_inAKSMmVmsYSrxKV4FIxffWiRg32S9RaQKXnV8R-cqpHZKgkN_1ZH7RNGHaE9dUe6JJ2EnSfBHFH-o-IP5mbGXF_Cj0ZU9bUOye93863nOLg6YT8aDbXn7rbsyQitpdhWqonD9s6sGqxCDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLZgnC5gVDNPz-7ps7D7pU8Kjg6I4KZsS_iMp97IKgMPQ2mS8omhBI-W89thUpK3buO4OLPNO3pjBFY4qcLeGjpPNo93bTsaLhLCGxdmU8FsTGhCWfPAHT83fgQG-mn4bwhxP3aDLplf6J-HGPyeDA7hHE1IMIDvzB6SlTOYy4RWtIBh8tJnfjWco_nFJ5pdl68BPMar5fPpRUn2qZWvRrCmLbPwet-8y2GpdD4YvgE18Rx3yBzRsTpJf3wtnqas7SYhktrLoRoQenwrH-40G-jrFgy7PxffkJCISlGeEX7aoCd2SQxM6ErYdWL9GZ_r7l8ddgKK6obZnavCagnbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=C-QawlDmQwKLAauxwFHkowwJDhUXJBFlQ66uTarGabSu73Sx5pGuuWliHHqM_97gObEqnRoF7m1QOL5l2is2gQkCflW5qVXWbs7rfmdVM1xkXo2_I3RZXXKiumeSvtSoqRjrh3_oVTQY6to-LWaNcRdylETg5g_ZwtM9hdokf4KvzWhl6m3oN68LgLAyucVEnArvMF6ZQmUbhM4x2eFwAcQWdm10J-3mE7cubkGTQ_n5sSB_tIh-L-BFWqanOKBA5N8rJKDbehII5T-llPG7IpONhqP-hq2MIp-w8duS7fZviXPCKeRUT1CvGLYifV4SmKAAIDSVqKIZyLqAPSiqBTHujFo6R94r7SB6_o1u4GYrVpn_DT47NNjrAibbCBK3aVBccTGhjB4jmdDjdwVllR5oIy9pUFPdtfomPGWl-rrS3X3IYGrh9aT2IzYxyWJouJEjHAQDggB0AKiCgrn91TWBAQQimio7ApJDd52fwIf0drte17dsR7KQ6LBALpk7Y0RB0Jsvctn5isusRoBd6L1w3BDIyXKBciGB93nWHf57KksJ2YKj947dynAQcvPqRf7YgXjPzdf7GGedmBWeSgBa0AgqGbEoYdOvhHxCOCep7WL0LfC_tazoDsaZfxZ4s2umX0ItMg5WBRQ1ORa59KGZhhz1M8o9ds00gVkshMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=C-QawlDmQwKLAauxwFHkowwJDhUXJBFlQ66uTarGabSu73Sx5pGuuWliHHqM_97gObEqnRoF7m1QOL5l2is2gQkCflW5qVXWbs7rfmdVM1xkXo2_I3RZXXKiumeSvtSoqRjrh3_oVTQY6to-LWaNcRdylETg5g_ZwtM9hdokf4KvzWhl6m3oN68LgLAyucVEnArvMF6ZQmUbhM4x2eFwAcQWdm10J-3mE7cubkGTQ_n5sSB_tIh-L-BFWqanOKBA5N8rJKDbehII5T-llPG7IpONhqP-hq2MIp-w8duS7fZviXPCKeRUT1CvGLYifV4SmKAAIDSVqKIZyLqAPSiqBTHujFo6R94r7SB6_o1u4GYrVpn_DT47NNjrAibbCBK3aVBccTGhjB4jmdDjdwVllR5oIy9pUFPdtfomPGWl-rrS3X3IYGrh9aT2IzYxyWJouJEjHAQDggB0AKiCgrn91TWBAQQimio7ApJDd52fwIf0drte17dsR7KQ6LBALpk7Y0RB0Jsvctn5isusRoBd6L1w3BDIyXKBciGB93nWHf57KksJ2YKj947dynAQcvPqRf7YgXjPzdf7GGedmBWeSgBa0AgqGbEoYdOvhHxCOCep7WL0LfC_tazoDsaZfxZ4s2umX0ItMg5WBRQ1ORa59KGZhhz1M8o9ds00gVkshMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IekCGJjyGVSKhoI0vYi-mkrcO-7pkxEdkyIBkksk2m9S48kki_KLLOJWbUKOgvD223P8AA1TB3siZtszryfh2if2U7UIlk69ivBkkdch7ri-Z4xYdtmQE0HFPop6IqcRB6SvQgsek-AmLj42-mH_ChbQ40Yhf3RUxiiyoLsZCeNTMViCjtM6S-HcjIl4G0FpO4RdXxSVANjIFrtiLWGmGg4KSer9O3kQCCqv6JMp-kdjIdJRqtD0bP_5ijrgQ7ioe1Bnayum-zkW8bMEmVXj-LsH0MSjsNfGoPEvsuk-L5Nf-q8FEFgiXMeY4Nh4AUsVNXhod78z5zLsOIBiR8uXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=TmLdo1DH8zknHeP9G1gsS6vz3BrcsLqKhfxDAeBRVQGeSMd8ti3dnokiQYjDaybXVF5Wm8bW0bwSAG_j04dv2U9STYfAaYCWKz3XZw6YVq_72a-O1aMcXpgE9B82uoc-7EGPGBCSG5mW39lBdA0nfp3SMkbBOxOL4PvW23twI9Hd3ZZmZ2VVP9ly8-d7OiEXaks-S7Zk79xGlip7upN5aPYTZ4TYIxxPSCCv_5Jfx_CgZadg-coL5tMZCqX03i1-HiN915VW6A2alIOmVdFWUQFEzM7Y0iTnoxnSWQwCjB7DXEWypQlx_Uzn2a7LeqPxQzAVNe8LhCfGa9fjFq2pnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=TmLdo1DH8zknHeP9G1gsS6vz3BrcsLqKhfxDAeBRVQGeSMd8ti3dnokiQYjDaybXVF5Wm8bW0bwSAG_j04dv2U9STYfAaYCWKz3XZw6YVq_72a-O1aMcXpgE9B82uoc-7EGPGBCSG5mW39lBdA0nfp3SMkbBOxOL4PvW23twI9Hd3ZZmZ2VVP9ly8-d7OiEXaks-S7Zk79xGlip7upN5aPYTZ4TYIxxPSCCv_5Jfx_CgZadg-coL5tMZCqX03i1-HiN915VW6A2alIOmVdFWUQFEzM7Y0iTnoxnSWQwCjB7DXEWypQlx_Uzn2a7LeqPxQzAVNe8LhCfGa9fjFq2pnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=pU8OOJ1shFz_aRkDqyrmbQetc7_v9MN63lkrUHOcZB7Xmw_DqsHysbF69bwoh4ImEF9dpg5kBZAFJ_zBfT6B3O-rSXllQA86Kv-u9S2nhmFuNd8cGE0KTqyAcUs_eUlviaajriu5e8Ox0RZw9MTAOmLzpDQvgbedbr-vfYx7vCE1MmAIHW_hFI1A1EgUBvoU4KQ9WT1gA3yHbxSIkZEXWs6PEf-Ylg0tsJP0vfieGez6htXF4Ny_pkc4_Jaqt7O07tgV6GV4b2qCfVZXao2LpZS5oobrzP7ucEJm9k-0AAsGrSOXJNiQe-28DeZ-4lL3okVpZx_hZZw0bK1fAiryvJW9ujPmsPrsgHbcIF0OGuCNAPTis_L3dGvuehkFVUh9NxhqCU1h37NcgJ11ysEnxGI_69Z2Ze3A-MSnmAYPKhd5js5HylO6xIiTtz3tvHmRtd5z5Md99HAzNaQJ6OiLSgBM2G629tC4JPO8U34JBmH72upHdxYOdF2_5kct4ns6VXzKLzYIDa9oul77K6soCkACv9drXW-pcDGtr2CEF6_LNatcEw1c43GnDMpzgLRC3m5rE9M5PIClRtS8ih7CGDXULhRAomMvnlfhfePsIxS7sTycgaddpXHrRuKCHygEb42iyGWu-ljse-ZxSO-uPnHdDX0ER3J3D7jclwOYRuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=pU8OOJ1shFz_aRkDqyrmbQetc7_v9MN63lkrUHOcZB7Xmw_DqsHysbF69bwoh4ImEF9dpg5kBZAFJ_zBfT6B3O-rSXllQA86Kv-u9S2nhmFuNd8cGE0KTqyAcUs_eUlviaajriu5e8Ox0RZw9MTAOmLzpDQvgbedbr-vfYx7vCE1MmAIHW_hFI1A1EgUBvoU4KQ9WT1gA3yHbxSIkZEXWs6PEf-Ylg0tsJP0vfieGez6htXF4Ny_pkc4_Jaqt7O07tgV6GV4b2qCfVZXao2LpZS5oobrzP7ucEJm9k-0AAsGrSOXJNiQe-28DeZ-4lL3okVpZx_hZZw0bK1fAiryvJW9ujPmsPrsgHbcIF0OGuCNAPTis_L3dGvuehkFVUh9NxhqCU1h37NcgJ11ysEnxGI_69Z2Ze3A-MSnmAYPKhd5js5HylO6xIiTtz3tvHmRtd5z5Md99HAzNaQJ6OiLSgBM2G629tC4JPO8U34JBmH72upHdxYOdF2_5kct4ns6VXzKLzYIDa9oul77K6soCkACv9drXW-pcDGtr2CEF6_LNatcEw1c43GnDMpzgLRC3m5rE9M5PIClRtS8ih7CGDXULhRAomMvnlfhfePsIxS7sTycgaddpXHrRuKCHygEb42iyGWu-ljse-ZxSO-uPnHdDX0ER3J3D7jclwOYRuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=pqFCO-GnprOf-XJiAdjiF9Dsa-8oEBzhoXPSXfRUbGrY1nXdrK8F9vyitKDRN5mQUB2OPj8DqdgFY2agB6Je6yL0cPJQ-3t_fbsFFdYZ4kxLR7Io8js89zlLgy-jMWwkOAtrxweKA3ErVvGR10-Cqp_UxXDsOpypFBaT5N_7DCRWgjRy4ut6CRdqSxK2F__qv-CymABWzj2pjIQog93bF8ePUzJqWTt8F4PYcNJ6sExxMSR_Q6xojPb_ZmjrIcF7_md493zIFUMGwZlvBWEvC2X6mMrLYidvxE3pm-5CZpyK5Dp8HW3HQz0HFy6bocrIRxnDb4wLL23nCrdDd6nRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=pqFCO-GnprOf-XJiAdjiF9Dsa-8oEBzhoXPSXfRUbGrY1nXdrK8F9vyitKDRN5mQUB2OPj8DqdgFY2agB6Je6yL0cPJQ-3t_fbsFFdYZ4kxLR7Io8js89zlLgy-jMWwkOAtrxweKA3ErVvGR10-Cqp_UxXDsOpypFBaT5N_7DCRWgjRy4ut6CRdqSxK2F__qv-CymABWzj2pjIQog93bF8ePUzJqWTt8F4PYcNJ6sExxMSR_Q6xojPb_ZmjrIcF7_md493zIFUMGwZlvBWEvC2X6mMrLYidvxE3pm-5CZpyK5Dp8HW3HQz0HFy6bocrIRxnDb4wLL23nCrdDd6nRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I82riOM-2zjtfmglOcC-XFRSuBTgJb5UCilVyAEHDwGkPssDV6XvQWOFvAWgRiDb2vkyR_B4-SuNPjiVkfoF5RBwQc7Do41nweyaOZSWIAaPnjnSZ4ruFCVQRuWhl2bmbvhkbzPppeGZXhXXFeEoKcrbeYB3avMtIPzb-Tr3VanjoMyPf28oSV7hiW8G4Q1tCT43RZYbUTTVwNkVw92tAPFfRq0NLf5mivymcEgDdhWHMQPnPa2O3xabEs07aG6Eq3xCKtZWQldj61vYfxcsbFrI4LGQBMWCnreHtgMEg_TdkQ-3mIePU83J1kduX3kp02QZ8-Np-jWDHBL-rciBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFvotagXK3Lq5oGbkhkmt2AUnedRSitKcUo1hsx-70q9_HzsOgXMpRYHvDRIujvANjzSA79pZhgbT27gpVPni1Hcf69AkvTHQKR9yxY8ZHDyLwhnoCibIFkabEEzPLPOkIcqJn41d96nQEaagpkUgYyW4-P8JtORGPyWkWE1bhJWWWyVz4K3BPKS5c7PSyMz18nYtl7v53CBfCc7C6zAQw7X0M2Ixa9IB0VU7J2ruSj9_b-EfRXvO44EJg4d0PDANrbEytuDyH3zoZ0boynOfgpSvQsNowVoyW6jsvzRaKD1frqlxKZ_raZdlp9GcXFoCLDwLR2aaxToEmICRvEXWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISYVSxwDNhqUs3eGGcr7oLvVpcJXYFiJb6yuSg0DtlT5fercV8qEC30qh1MTQ4Kz4nhiT0L-R61P2Pgkmm0OsftTtX2fVBKf5OMhg9k9-M72PEW0kl_YCQl6x_1i-mtvnjKGAxqx37Lr1c7b1weTa80iLey_vCWp7Ng7nzwZhbZjIa3kj51TMnNuS12X5qB5KQ7jxQOqL-OoTXSTQy7HoAOoIJqF2gLFWN_iTuE69bpnFez5PnKKzcoDvyMEYGjSWGgnRGkHAWGF3pmW3cVC8b5xf1h8BXLivHScPl9JeW_rSl7SEmeb1VSuEhN4f3AckBDbJpVXvAUuDnNmFXXhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLXbaZc6VPVk9vg1zpJLrHrtnVW9nP7Vnv1SogFi3Y8Dm67RssBtlG5qtS0etlzil353ZROiotbO2vZgjDw5oWNx6f1tX190dAk9jgnj_BS1vnbk3q6JwjqKwTyAmxllQeSlbiwISvgwYGeLSXJizlk_bRWHOG6nzJeos4B0XDaWediufUhbQaHPkbPZFkLMVDKkf30RPEUpixnPIkHqDD2fPjpdOf_PhlhtbTJd_3GJbIWi_Ho0tSwgYFj1tffl-wApw2zExkn5Xq_-htKYw-38kzVF4sOyn1VqGMm3PwhXNu8OsN3FVjSdE6uKtAhzM8hYWmEGXPaCgvI0bGjviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD3VeAmzVwaZA4UD86X_YQTY7LK2VgrPIqFk43HYYPGL56BCdlhgeyTQFQ34L_PYv5hUZhNlAXG40AIYBmAypPhEixcHMA4lOBRv_r2UPlatUeq3mtUi_ZKkazmqUzqLMY4p-ZMYiqOV0ueinESfffPMubpbwB7NTGgV1NdpG60T96Yu3f-4caybfTWCxHZc4ixQWnqq8oGBbPV2aUph7BVrSqQWPZ0dtnzvJ2JaBQpos9N9-KEZstAFHdBcylTybw5kjSuHZ63ezvqP3vWl-WJ2_A4uMf0jm77H9vwXlACa-pZ6kwjRaNoWTXh2Wh9S9eT_Ad9KH3NHylvnTlfYMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=F-zF8KknPs3jqfT4Ex75XRcKclUEjrNhwDBaPJm8ESXDqf9vfSK11cALLOkecFepSLkvVVj816U_swxkiotvXYqGF1kRP4AgEstOXKSrdo9lcYhskEbEn_DZDMeA0OLUpU6VhK7Bc4-R8vd1zZSoURk2XkK4ODt3tvYjOezc8MQX8DuaeCQruImxr_O5s__kSJjM8HfjpVp0dQt0_YzTR58Z6IcOskEcGxGC45ORPtqjKmo5pMbzm6fOX1IU3WexRkjaSvqLg4BxhDCNx_kZRH6i4QwN1ytQPankTjv3dG8tFwhrDKe4W_EnvKta4EnJsLg9s59I1C72xZm22Ffn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=F-zF8KknPs3jqfT4Ex75XRcKclUEjrNhwDBaPJm8ESXDqf9vfSK11cALLOkecFepSLkvVVj816U_swxkiotvXYqGF1kRP4AgEstOXKSrdo9lcYhskEbEn_DZDMeA0OLUpU6VhK7Bc4-R8vd1zZSoURk2XkK4ODt3tvYjOezc8MQX8DuaeCQruImxr_O5s__kSJjM8HfjpVp0dQt0_YzTR58Z6IcOskEcGxGC45ORPtqjKmo5pMbzm6fOX1IU3WexRkjaSvqLg4BxhDCNx_kZRH6i4QwN1ytQPankTjv3dG8tFwhrDKe4W_EnvKta4EnJsLg9s59I1C72xZm22Ffn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrpW_9jBz5YoBt6d33NE6W2YI8yBYQT58LKuveq2woypN3Hc6_z7mZ0lQR_ZcLt2pwLtTcTOYsTuu4UmrofRnsLHKToRwpt1cX8IW5x4-xMPcpvjyyUAIN12egwndds268k67XWOCbdSnC7NF09-CfKp5BLza2VNUYJb3CXNkwqxbB10I54fEJFWWZeoxJS_6mVHi_Uv_oCbXgFldl2918Vek6CMhAiRu3AT-HoSXSd_YtZ3Iyfk3ImZ4g511mP4MhCQBDYusxzkmvVaWEapX2jp2PHzw84kgCwe8T701QMGvQLV4O2eepq0w0FDKkMci4HL87jtRHRxpg4W1OlvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgCNQggcVKeKLh_W9rRIZOaBeoi7PISwxFV6MdMjjV-FItiHpT_-Icqp5fIPBhgZxCVxC8F0W2s0S914C-qxZo6xUJSKUrvKqJU-72lsQpOiGudLWoUnvMlDx3sv019WYN0HOawPPSCANHvPkDiw9MHxUqUWBakP6RAbkyFLZhJJBthcjM5ebTW0DUcg7D2_dsMOPj_cv7s3aHIW4C8Z6l64G0A6vER8ha1CxKMQ_GXqwk4EC_j5Ujl1g6-CZrA5EHDpNuAEWpZ0f_YMgyGatWJrdLIHWAIu0wFd1G130tiZrDCpYFmMhWC3o352VJ7YnVfFMyosnvMD_k8vBvBqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsMX9Gf-q0m5a6u6d7dRSJEPMTv2s5pGzXSYPdeQW3Wm288s5sq2gd4nLPnKaVO8j9CccalvHaCL3sc3p8RECMd-cab4GR2GdYt2LtZ2sqvK7q9uCq4DdlL_yvswprej3vD_1Y4QpgMvpGpFftS1uur8ND4SiKXtaizQbOlfYdEcK8roBhJfRIrnBHeI7z1BYGrpNSGXTZy1gZuYVpkeRKN4NwFtTmTWSapRqAzSZd-87MOGsP5aXU2Zf-1qvoNoNvwCF83eYcJsh0I8dsl7rfbAhOeeRC1plHGHzXAvkPO6VnmO7zwg4F2rx5w4DBy4bhwmYwhSYvo6fRU3hNLtOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIM7V9tz-4TvUQRwRZ5csGpeogl5t_tAlyU_5KGrgmd-4h0-b2yTqkN5bhPRzwgVsE6BfMd2G8uBIWaXZAmhZrmnNarmGxLAoWqawBivR8Cgg_FnUQ7siLVxZd43Xm3pdZFkZMdmO67NAyv0Q-IBLNS_L8G4-orVfSPnN8MzR-rRcq2w1uXtNCrlaZZgNl5yYgk6wC3FUlKGxRLpx-_AessRMNAe8FRq1Kj10PZqpWI12xiOZXqbW_gO2tv59CcswYzH5Vo2XlAtYmxy-wlBH8APK9AOapRtgopBYzdZ_4JO5fOuq3j0bzTHDxteJKvoLyeMJMlzsEDad_wjPGlfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rq2qkvtWM3Q4Vo2GvvGAj1vpodYiz3N8NXBSEIlwlnTRSgtqxz3kWktl4RLlPDQYfqc0YTDHT3xWandnDj4znLDeo9hY6PVwBobXjnJCw-lp7n-H1z5LC3EOhVl95HdaZ8FPdTkISIZDC8GXswvdlBV23yWfbKFI1jsRinuV4tnKm0KWQ2uLSbGtG0E9-f0Yt5PTgyRFZFd8m-4oU-pnrn0cRHNmeQU9CGtskO_QbHv6wHIv3-S3CWR7IyJ1Pw69GApFtFfiQ_7pjSfQhcTZITH1pYoA_PpY72cgYcly9s8zK5MJe4Ir6bznvO9DmgYaGE5VrQRpNFdUzdpTjsrFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCeX3h47V874EPlvbcgrvCiXN6_-G8XD0MlBayfzLCyg7dsA1PWeEs3go_uORix1hj-2W4IrB_VTjdXQxbA4n9sd8Rl6c5EdVIhCnRt4rfsKanXemuf4ytrspyLJDmymSNBVzzUOhs7n8_ZeiNxyGpxFRzwJFnVLknEA6Ua-KHuCGFCR_if01lg1m2DREKoukV-X1vOPOv0WPH75SuhHvshbcBJ-tGvoEQFUEV8xa6dIGiUEng4sY0qnl3irig8ArC0UZ51mxE0rLTHYEFXMPy-MkY9PGYgoEGY1Xc-c_Ua331CeKEqLlPxJM_QYRVd1Hrf4yHjn7Hx5676n6e_LrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTuSoLwWNDc7sq_Cy1IZkP1fFPdKX2moIm3sx8t9Or4gPN8kKua4qU8KNSDbEmL32VvlRTvyIKNxSGe5Inu1UEsandJ_6O2CpBDtgbLqYhB_0bYh4zySpcAK_0MeLbQTtKcWhXkocc7EHOpcDGBQdB4R4YvLcWVx6Mp-GDQB77gVs_XpHnFgt8YCioBkU4Kj-qL_JQVbsc1bGgNGp8T7z9B3Tv-wl-CH_vYqBsiKINEEj-1si1wLeE0p_8QY3VzMlT83LsXrYWbsnubTSZ0cDT1fMyzXMx1CNmf8gtxTbpIJQWQdBV6FJ5aTHbCMUzprEs6oaNpSdtwqXpcbibBnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
