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
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMJ81dEvikS6WGYwQclpY9Q3kQJUcfWn0QuKUSHgBkuFhuRXVdM8lMJTar1Cjjw8mSv34KqH61d2f5jdeuxpAylCuwkDE2RHTAGdQYw-Z_rrOINAqK546GD3tTkhEafCXhHaZO9q7gUpWIVVCwppUwLMwbZspaLUPdXu3W3q5FnJLimKlCLEtwwNtqfKnc0Y7XRNT4xsq9a4gtA_FifYlJLEJWjRtU7ICqtIrVe_sbMJY7K2iU53er8e1LQ0eeAwZUpDKNBwjOV2qDHX7kgwuaigf42L3GRKPS6n_pJ6JdaMj5VlQI3L13zOZQlkDmQ34dHDkbMsft0TDSg1GN2MeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9M7T_Az68rxXqB4Jw9gRFRW8UMkIrB-JQ3_Tvq3U1WNAhXYipNn2CNNOjjxZaqX_mWnLhEE-LRBwKJkILOMs-7pyukeRFSnL17flZIzh3jiPEHTLw_Yl29STDHeDiHtoN45je80E9YqS2PFL_G8Mnj4Fu10UALV1nkOPjU2dkNt49_Gc8qiZXUHdhMiMAmpCuzb2aKUxisWNTd9635lze_Nxx6hg1YECLmHs2yHGQJZ_WxmXbtNERItb5NcGfW99IO0TAoedPOl_WerAAf3ty3KhzgLc9pHG1Ebz_aIcfdKdzVim_jewh5XldDuY6ji6-CFiRnykN-AUwW4TdD22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=GgDx_muLgyGl4O7aLq_XqTUPDU_XkUsxH2SU4UM2_NFVGYyDm85WTIJemfoH0v-8MPBKAKOBCCuV9FX5wN8sQVY89TAETJ3OcCFQqCQ9OaMNP_0DnNZCDmyHZ5wUmZDk0NAnzrFcNlEc3AhhzjGMtSaynIwQsocuK-7GVN-D_JbtbO2L5fpBebooGcu05QMeilE3WgyKfwSWUHOHEeis6-KkVfWevgV9OUETQhFzXlXoTjapA3wNVT06-Xbt-8uaoxQDrKmd2g2LfnTSIeOefxTGiHI64ckxevYAdzgnXe_x5AAlahw0bHE_dwEtUzqum4jWSWlfBaCA1r5iJvezQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=GgDx_muLgyGl4O7aLq_XqTUPDU_XkUsxH2SU4UM2_NFVGYyDm85WTIJemfoH0v-8MPBKAKOBCCuV9FX5wN8sQVY89TAETJ3OcCFQqCQ9OaMNP_0DnNZCDmyHZ5wUmZDk0NAnzrFcNlEc3AhhzjGMtSaynIwQsocuK-7GVN-D_JbtbO2L5fpBebooGcu05QMeilE3WgyKfwSWUHOHEeis6-KkVfWevgV9OUETQhFzXlXoTjapA3wNVT06-Xbt-8uaoxQDrKmd2g2LfnTSIeOefxTGiHI64ckxevYAdzgnXe_x5AAlahw0bHE_dwEtUzqum4jWSWlfBaCA1r5iJvezQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR0VQhgAK65nrtXSUhqc9IFkXHh73zknmcrcPhIs70I1AiCm5b2XCx3B7DsoYrCLWKJUQ9aReKTzp25v7oidrlXsoZeCW18FslCvgtpLLm7CBUaJCJH7-VpQrrdWGyW2rXrrVXcqU-y9XmrLUVc_Ltx--bE8MyPvDhrWIXRQ6Y0y6-1uIml8Tw8nL5mgjnD3UR5ybVK2cHMyjgmo3Mk2Ea1dJ0-gkR8I9r2fS2WbxpBlYO9e6Pw4QSYUBE_6BZ07I4uIqOIFyXC8I-37QpsvgyDCWhGpsgby6hQbfp6mshxfqOk9sL0ddF5TUWuzUAIQi5mkSQQ9E-0wIyqAsxLK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=V4TAJ0tYh-X6dDssW3aeYK0Mn1_mT2dWul148veTkXbflypV6jyJvVHkQjhGeqvedUdbsm3oVzukU0bivbz2KwwtsZAiiImZ2W2Ts238V_ckHQ7cAqds63jv4WGmqr670cDpahls7vISXaP8tOsTL9lzgC5gOiaIiAZVCEkdhoePQDTOB1t5f0xUvcvZbxBDgQidkz1bsduu66uC88aHzaDK8aN1-Q7X47npTfGrd-9y9kQ-2lfpvObJdcDq613xApkDbKdRUVQaeCb_snkH5Y3RwV9bz3A9Ry_U58L1NKWWQq_d1NOpqR76daOVf6VcRZylov84PT81IMVUsp-nmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=V4TAJ0tYh-X6dDssW3aeYK0Mn1_mT2dWul148veTkXbflypV6jyJvVHkQjhGeqvedUdbsm3oVzukU0bivbz2KwwtsZAiiImZ2W2Ts238V_ckHQ7cAqds63jv4WGmqr670cDpahls7vISXaP8tOsTL9lzgC5gOiaIiAZVCEkdhoePQDTOB1t5f0xUvcvZbxBDgQidkz1bsduu66uC88aHzaDK8aN1-Q7X47npTfGrd-9y9kQ-2lfpvObJdcDq613xApkDbKdRUVQaeCb_snkH5Y3RwV9bz3A9Ry_U58L1NKWWQq_d1NOpqR76daOVf6VcRZylov84PT81IMVUsp-nmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7c2BRyigPmDJk52i80KENR0Dp3AJmctYteEx6d_NBlGN-lwdW5ZOEf_QNxZeemUfBVmpsadeRNrNMSfz8_TYgnSv4Cwf8tVwCAaunS2vtmk-bHxEggGR5xqrIQ3TdlUiNKlcTOQZB76s-qs_uBAlBMvtg0cAErhBbsH9JAgMtpzRPbx5qgqrc8-3TaA6XGAXbtQR90Jn7MsX2eEuogn_SRWlMDTZFOVnkWCTQkZfWVED1KlKRAXJNhC1vA7GIZv12XDe62krawBs7ORcgVF6PCVa8hwepGxJYZV6t1HEHxsXNKi4OZxTdpo6fOZbG4nNp6CkuGHS1rt13fEBkX1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEkH8RJ3nv8aX6LgFcSHz9LKUVJ5niwC3-I_gNPnwhCGacScFDp5Li97cD6mojXudD1lkZUv-gOI3To3faXUbba4zq3HKuMOlAxuoVNVEmmzRprlimZlOZejOFZP1PjCMy9WdyAEI8tNKwfl2hWmpVdVhk8Nqu0pzod-j4XQ-KPff09hXuZwje1pUOhMrSIdBFw1j5wwXsw0i7PPifCJ64yr0cFbme7oZvwRmjWTMppaEXxFdUNnqFsVW0tUJDTGrqNUB9h-p4agrcK8GEbS31wQ0CaTWm2SZoN8-IYgMMHYt8MemsRNUveNFo2-IWC9JO9F7sklbM-AWPKNdflLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=JMZFTxmB6CP9xNTi8r1ruxHeyYzB2cAr20it0HencoirlJeormGQAluJ1UY9TQnIutg3sWdgFl4RmlrzaAFwW34rM0zq2ONDhs8OkbF_uTLX7pnHRcQ5eCqc_PW2HkJhjTWZd5uJopVeGyvtXYHR1zMps2YGpW2kCM7gb65cD2UF7kRDjTjod7xo0oW-xo_Awm_Er46FlfDjHefGBMVEm28QfK4mh4PZJ1rxYU1063Y8tNIU6VNra3FOn5aIY7T4eNjOBhHBCMmW1gq43zGF_kCzbh-38mnKB321OLTy4JhJ2mJSUoUdduHe0fhERQXDeUwM1bsohksK15uw0Azwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=JMZFTxmB6CP9xNTi8r1ruxHeyYzB2cAr20it0HencoirlJeormGQAluJ1UY9TQnIutg3sWdgFl4RmlrzaAFwW34rM0zq2ONDhs8OkbF_uTLX7pnHRcQ5eCqc_PW2HkJhjTWZd5uJopVeGyvtXYHR1zMps2YGpW2kCM7gb65cD2UF7kRDjTjod7xo0oW-xo_Awm_Er46FlfDjHefGBMVEm28QfK4mh4PZJ1rxYU1063Y8tNIU6VNra3FOn5aIY7T4eNjOBhHBCMmW1gq43zGF_kCzbh-38mnKB321OLTy4JhJ2mJSUoUdduHe0fhERQXDeUwM1bsohksK15uw0Azwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=vfg4FCBVOtRcc9Ptep_5Wri6N-K7P6ydGxqIv7bpKl3w3ezvHzgwAItNPFMNIdNTw6FQZ4_VWNEVfzKg35L1VmoaJlEPUt0-idevTDUnZYKRnSpzGX4WqsXsFoKWv7L8Ic6GF4OzgjGN3GhjuVMfCEfPR8rrhsAU9RKrLX_n5OLvib1beuKLcSHweky21NhsnFuBFVHAkmZ68DK2CjxU_YzJHEarUQ_Kn57sSRrzTUreu_o7q8K3AILrE-YQGbUqcXfEIgYECaZUm8HZGuTInr3oVJEaF919rQkI2VMtYoEB_76MPYEugyMXh0XHkTaEAGzrTFNXTAa1RBWhBgRhLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=vfg4FCBVOtRcc9Ptep_5Wri6N-K7P6ydGxqIv7bpKl3w3ezvHzgwAItNPFMNIdNTw6FQZ4_VWNEVfzKg35L1VmoaJlEPUt0-idevTDUnZYKRnSpzGX4WqsXsFoKWv7L8Ic6GF4OzgjGN3GhjuVMfCEfPR8rrhsAU9RKrLX_n5OLvib1beuKLcSHweky21NhsnFuBFVHAkmZ68DK2CjxU_YzJHEarUQ_Kn57sSRrzTUreu_o7q8K3AILrE-YQGbUqcXfEIgYECaZUm8HZGuTInr3oVJEaF919rQkI2VMtYoEB_76MPYEugyMXh0XHkTaEAGzrTFNXTAa1RBWhBgRhLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDg1YjW232Uh1-7dtGMr-sq6mrmyNUoe_W7dRb_NRzlcivDsfMdpLcE08YVGbw1-8Vp0YEjnG5QJ8BFz6yvzYe6uVawpiV0e2RrCb-wvq_Ee39tANeJkLXWf7LiDXm4ipHUU0vathDhDqP0NHe59-MGvUvsLE0t8ljkgI-MoQYdKKWcB325AULlFwG8GxhXb6Pq_udPeIpB62L1BnWDknk_MnWSK9JYp3YlrCKddARWp-bChKIucd-FBvRcXTMxFlNepzA9zSNGpeeU6D8NDwKzCKJKAKZE95y8Gq4rrHSQ5tsSFQ2ia11DDlXRAaiOSpUpAs7YPBT5y_xQV6TnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlHgKzVfYQSw0MTs1Ld4IuQtgZogOm9DtvSTVNnTKEZijlkmPYVWKSNl6XAn8VkzCvNYZS0lHY3YLtJ2R2awjl8N5qeUhz0gPt3h25U1zSW9pxG9j0A_Qx28WHIPpaOBMVB_tcMsBss63FJ5P4Yd5Of8xoO4VmtMTp7caTY3TiaYXVJ8rqIRNModRwBdashwFtmKOBk76t-yCG62DKu5V3ONihpO0vQg-H67rM6eB8WE0bCg7Z4FhjZdtc9vrYI2fh-2gxCxul-nda5TUmj2MsZmtYIv8hZZNB8ncfdgUZ-tK7LDAMUNSjjQ208mkfMlXL-iXmwNpjR0HU56VEtGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMPVOKnfShuQgyE6Z7R51sWx1Od8pu7dmLfvMSFGnp3frHAqI4xouaGOo1WE8BFRKakIrpFtAM2zKZclpSXXjv9-HkxfSlxZgBko8RAGEh3jiao67h6whWAQJZD-EI1rk_Rsc1_bh0OVZtPuZRY2bJsQkkNVA_Tl7H0JU-SnpA6RFNrZO1OCt4V-scltpkSL0ZzL2v5mvQAPs8CevK1YBnXWYimNRDHZodI0wWN4gAHTvAKk3JQrqpUejD9Rk9ILlnjLnrqw8RThbEa0tl83wzY6g4cL4yFfxZuPhT_vvkW1keDyOHHHxDSnmO9mCpm_fgKthUD6m2amS_nt6UtsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=ujeNsVfuna0gvXDDSgMqlKsHH2Q08lYsanDTkhQHGAvri8j0gaCM07h9DMEyQ-YMY85DkoB7Z_HCN4b98Vp5_RWZKwCN9gksRfJCOQEHP0KC81eS_bJ5xfazHgiNT07j9gDRj_nlHP_MykS7UZprn69gHM-_QHgbn_dHEz9SkPyviXw3af_y-K1kailLyXvB66B8RIEOEadzOwywlxFl929ATutWNP1zf6j3IH6MQXXeOx8erkRAwDoaC8Arjp0G8tBmOhKNqYsbGjiG2S4Mhl1Q1kp6X4BtyEk_Dlv5CEyKpHiaHwByvn87O7CGVDtPhtyZfSTEFdHEA3bF2w8ZKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=ujeNsVfuna0gvXDDSgMqlKsHH2Q08lYsanDTkhQHGAvri8j0gaCM07h9DMEyQ-YMY85DkoB7Z_HCN4b98Vp5_RWZKwCN9gksRfJCOQEHP0KC81eS_bJ5xfazHgiNT07j9gDRj_nlHP_MykS7UZprn69gHM-_QHgbn_dHEz9SkPyviXw3af_y-K1kailLyXvB66B8RIEOEadzOwywlxFl929ATutWNP1zf6j3IH6MQXXeOx8erkRAwDoaC8Arjp0G8tBmOhKNqYsbGjiG2S4Mhl1Q1kp6X4BtyEk_Dlv5CEyKpHiaHwByvn87O7CGVDtPhtyZfSTEFdHEA3bF2w8ZKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atUK3im0T12K2rEchu0DMzOmGP8AMQd4rUYpFw-oyVQ_sqC-bSGmu2RV6jkyDXuF-2FBTIxdTip2j4ArNAZvSkBw2p_JIqo3zTn5Ptpvm6ZpUvcREEKmhaUuIRR4hITZ4REo7r6OfT7hpXuvgltLFdozLAagBzXXI-KvkVfhaNLhbakK2ay70J3UHKrXNEJNN-SQrul53IlYZWsqw4xjzpu8mDUrVx6y2KTLfHb49VDQp3_t4LYwhwA-6EL6f1jGsyKkG5jRHJrlVwxRNL3IkhTToitvtgy4mxNoiBWqK5btMIzKEnCc4nYf046Z1-993mqEohXwZkSsgoUXNDCxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilPkukllXkXyiPApCnHUm6kiQQq6_Fps_iFiKfL7ChFBe-wiUe6n8z5FMyVTWfQQ6jRkR1k8uu-T0jxv9SPBAkGNmHbKUbkwfBnQOT0iVdavNo1RnSuoEH13lfw67828E2Hss8izFBzwL_uD1CWHkGDJzmSCgGlicTDsuiRRem_eWimSc4kQW2YUgbUDLYiRMcVWFQIwzZmwv1upFq5j25pPLBVlB2rosw2O2UCcGcBtZvLpW6dYfA53wT5aLOmIUshU_2mQqtKdRZTkLq_ldJtwofhAD_NTK2VZbMc_sYWKP13h6Iz1nywxvFaLuVPSvlyWHZT_UH6Ud4Fbu3Wz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6jrkLR2SUieGejOyDmFcdjdfBUzuItZnzyCMWNbHPP7sKwpB7XXLXxmcNV-cvSQ2Do6N30eEa_nuuaZtTfgqvr29VeFIRVTrrQiek21ScirzJEIYOcRRLMm507MUn0oMFHS1kIETCfMKZu4FMau2Atyzdk9Ezoa1OewCplWXsYwzi0TKXMu5CFfqn7vs8yCerC5VsphE_0IaKTf1D_xYF6DnqLC1wCuPm5IN7ASmiKR80VeOgIf_n1MK07l5bOzNHmnEfwDS1b0C22Rg06GBlGGksAJooslyMEBOtHvdUfBAyvHFJL1zhONRsLKoiz75_7ktjoKXdworEx7Hl6W3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncQuOjERjlTEXxdEdk8n7h2YQNTL3su7DKVQ310dgd4D85_xgOx0wrPxVuTLT7QdfnZfKpIEa8mjABCH1Eh0dJCawiNQDQhz2cTdNgcGxFWYtqSOwgWu52nIS6KrONL0zyLwNFfBxLCe3TKo2LV8KeNHYpcHmdL18u_FiDtX4UiK5QpLpXarwqivJ39qHDQTzl5i_r2ShOMmlQYhQIQ-lDa4zJANjsBs0ByiCq7ROoX7PmrNhCxzubcuQzQKAtYcfMq91izORKTF-en0hX4yVwrXZmbuC0rzGbucPKXCu6HGpvm-IVi2DtqFUQmmi_0570-DVnjQFD-ToFg279jEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DB8J2cYn9ZaVv80DlWG3QhdPVxwxsoZpnXHe1QX41k650Zm_w0iRfFDci0RilVs7Cpa3AlU74hq4DBEM80XIj4ptrjwd67At4M2S6ax3-7UKOgwylK_sP8qKs8IPmrUKXVV5V6-DJl-i9Cu5HGvC5SzqGidICglK7Ceb4E3uPMP61G2kXc7sVqLBDorGQfLM5mkTm5r7hbA1GDQeWB4McXN89TI4MVeQMQo2S3KpEdEdZ4TbqpXA-MjMrcuzcu3Wb78z-XQ4e7YRZEl2C13N6R8KqzzSf3jpBcanQwJZSCdDyt0LfqQ9c67naAHzLIKACorW5Ocj_6VFTvm50NWQEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DB8J2cYn9ZaVv80DlWG3QhdPVxwxsoZpnXHe1QX41k650Zm_w0iRfFDci0RilVs7Cpa3AlU74hq4DBEM80XIj4ptrjwd67At4M2S6ax3-7UKOgwylK_sP8qKs8IPmrUKXVV5V6-DJl-i9Cu5HGvC5SzqGidICglK7Ceb4E3uPMP61G2kXc7sVqLBDorGQfLM5mkTm5r7hbA1GDQeWB4McXN89TI4MVeQMQo2S3KpEdEdZ4TbqpXA-MjMrcuzcu3Wb78z-XQ4e7YRZEl2C13N6R8KqzzSf3jpBcanQwJZSCdDyt0LfqQ9c67naAHzLIKACorW5Ocj_6VFTvm50NWQEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1kgz9Osz2_F9le7ZdtzLvhvgudViNmfnemK2SSWR-N7jdEyF1dVa_u2TFaI3Je6Xo_4pBjXfhWR0Ic-fq0_vxQfgn_Tk9n04AhSJi8qd9qbUN2Ks_3CD9Z4k9z7Ob3QhhjoDPQF2hSeRdMGU7l4e9_N-xkdoudNyLKSq4uCv3hxeA7TeoqTCfn6oS0Pw2ZmsEaGGGakMKYAgcoMYJPmut0j477yi1h4mNGLyqBAlNcKIcYwcDq84VzOYFt8uWldEjHsZKIChX-cmIBbkBpRBG3eXcmN8pkjVX0m7MHd4y8uk8dE1hGCcwdSexYIE3IWjIZMc10pcswEyt6kj5xkHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=a0jUgj0Li8tB1Rw0_BNzCiHsdcOU556o5zKNBq3yfkkWBl4iH7igZ-OfuYC9zA_Qt4AUWeaF540jLMJqxmN7oOp2f174JJsLeJhKv0QpbLnaAZyHnnosNkalII9b1Ka08LnXpRXEU8ejQFe3vqvZGQcgmgDs_8MJjF0ZCmmn89Yba0ROjaampFuXBnCXOwp_rzy7yWiYQnShy9dwbafRsjAyUoO-OzUckVFi3F9Ub3CAzViMVOU231aQ7NG8bC-OlP-KixFma4OGqZKQprt9vv5Grz0VHW0Pge87rIj78fSbhpjK2BIAVOzyh3tmwPArVQ3CnvODFoeUdjL-wCvp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=a0jUgj0Li8tB1Rw0_BNzCiHsdcOU556o5zKNBq3yfkkWBl4iH7igZ-OfuYC9zA_Qt4AUWeaF540jLMJqxmN7oOp2f174JJsLeJhKv0QpbLnaAZyHnnosNkalII9b1Ka08LnXpRXEU8ejQFe3vqvZGQcgmgDs_8MJjF0ZCmmn89Yba0ROjaampFuXBnCXOwp_rzy7yWiYQnShy9dwbafRsjAyUoO-OzUckVFi3F9Ub3CAzViMVOU231aQ7NG8bC-OlP-KixFma4OGqZKQprt9vv5Grz0VHW0Pge87rIj78fSbhpjK2BIAVOzyh3tmwPArVQ3CnvODFoeUdjL-wCvp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0inmWpvEOT_pMoL8776yrJ3TngRLV9mWUwWJydc5diEKmGbk_Eh976K-Q2QqefXY1Aoxy5H6YDXtLyDE13op89FlF9ToG909JRj9LmdiTEszlkS7BnKURARkSu-4vNEGitG8xKLhZtsErIyGap2pl4JLS36TxjpCrTpFnyFe66gMGnNnW66aLQeT3MIsp-zX-QGOfH7G_rKgg7OHqBt3V5Pvl7hpJuryoCqOxun1Z4J0MqYN86R11Ug1QqviYlIoKRjhZhSUu2y8YKm-ZWJCRTaUl1XFUDziZPqnZ99KIhoS45DA9rzCsJ5VEv97JHF-7_Nujb76J_g7FM3fMrdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=QlwbYcsBLxhsRESoLX7xY-eu-CuT8N1A8CMlQIy7BbIUcqzDGOMopV_wrkmRUGZpJnx_fbtl2wBNgj0D6qBrwYjax8tQCGSVsOc_vm6U_RYW8rEFySfIiS72gzWuDnXaRRRzpE54mKegCOMrUDp3qp5hhYqRDAFbe8BOo2Z_58MdfVA8k47FYCqVOwy0GWPmpbv_UpzAugqtfiAN8uZ9mOiRxyHeQohRGMPWIx6m1bf3XLijMc3hjrbDKWmJtgSlGErWOyIGRvKqFyiL_FXT4cnMcumY3lrn35MwHs-659NC8oqBUW6VvNrJm51ut6pR5qKbscNWuSz6Kzvtpsmgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=QlwbYcsBLxhsRESoLX7xY-eu-CuT8N1A8CMlQIy7BbIUcqzDGOMopV_wrkmRUGZpJnx_fbtl2wBNgj0D6qBrwYjax8tQCGSVsOc_vm6U_RYW8rEFySfIiS72gzWuDnXaRRRzpE54mKegCOMrUDp3qp5hhYqRDAFbe8BOo2Z_58MdfVA8k47FYCqVOwy0GWPmpbv_UpzAugqtfiAN8uZ9mOiRxyHeQohRGMPWIx6m1bf3XLijMc3hjrbDKWmJtgSlGErWOyIGRvKqFyiL_FXT4cnMcumY3lrn35MwHs-659NC8oqBUW6VvNrJm51ut6pR5qKbscNWuSz6Kzvtpsmgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=X28Axd_CY-PUadBg9riZPxLXjXQKW8fx-nukYsaBPfoY4oVYeK0BX8pGq_yZo0CS0uwWTq4I0ILcBUdOUmhvd1aVf-I25tB3gOGbRWWZflPwAToaDvuOpPAd2sCnKBU_tpXAHnHtvR5hopKZaEVUC0DDf5RnD8-da8m3TK0xkKrXSe_ObFUn6BZ0QUE7KY3YV9-C5NqyjpJi8rWetNN1kHnC2p3Kjmjj3zNJSZ3bFufQBa9Rz_igUbwNy1oaR7UH0_RJNchD773Bg02DHgzJqJDYmyDU7NFsCZHyxZ7Tz_Kb81iqMkrMo7MExD22saDT8-ruZHDj0TfqZEiFCHHrag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=X28Axd_CY-PUadBg9riZPxLXjXQKW8fx-nukYsaBPfoY4oVYeK0BX8pGq_yZo0CS0uwWTq4I0ILcBUdOUmhvd1aVf-I25tB3gOGbRWWZflPwAToaDvuOpPAd2sCnKBU_tpXAHnHtvR5hopKZaEVUC0DDf5RnD8-da8m3TK0xkKrXSe_ObFUn6BZ0QUE7KY3YV9-C5NqyjpJi8rWetNN1kHnC2p3Kjmjj3zNJSZ3bFufQBa9Rz_igUbwNy1oaR7UH0_RJNchD773Bg02DHgzJqJDYmyDU7NFsCZHyxZ7Tz_Kb81iqMkrMo7MExD22saDT8-ruZHDj0TfqZEiFCHHrag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUjO--GQypyL4fZ6ToWGQvk1ZUwBVG4C55NksxidheoBzK04vbUFA77Q3J_NbNlDYsqboaecsBwlfYH1e685xTXLHLqqAJyDkqfP4ITfzSfxqjalEQIGLLF5nPg2CDeyDca3IRySw99rdtKVpiaYg61IBn6ruVGqO1svPGai28decmQ0ujBQVRAkwooRqusrT5KWBqC6fJY8oAXUaOsGPzlvcszqQgTHTPSViQPeg673HFLHcqRqOXmcYD-7KHu37-CA-2WN3tD1Bs0GKrPD3rKQqOlANbSndBJnmFm4bz6GmMvflXMzG_CJcwn037my25bLm3S6yBnfRsY2vepfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWfHdwgZ2V5ioCLfMB3_vQhU8f3aF1oIil6IBIsA6EzYnqJL7piQH1h6jCbMvCBFRln_Ko8EizWlIW5h27oDFWsUXHMx0ju990I0SZMw7ourpgmIPF1LcoexJ46n2_mnka0duCNFv2JzsxvlLMsmnMm_4uk7-ANQ9hwCuJaWdIZFxHNF-LEtD_yJ9F-D99c_XCMIBFAjizWgGEwaIH9FGk1LmEhvsdAAj1KxHK_KbhCrVz1W_Lyf8dIPp2DfQQ9HOjNvAAubs_lbDtMzS-eO5zemYuUb0Ow-1k60apNOWp5gKZ7piJtDBEopXp-cCSvHvB18sIWN0WJD4lW3crItqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ8x1q0zwTjNn2KlzxxDdMFJPn5h2SKR2qSoEtHuZ5FtZ-vwN634GUCCkdvazsFxvJwtie-tkeiv4jWDe1eNHz_gCGESmMiHE-EBS5DrSZp6PkB2knig_B32I-hVFtTXp7kL0holeJ4uO4E53C-uMTV5we0OiOIjqREaj2Y7uNNOP3kic7gGwusLAxjt4k6PyCHG12rSJHNNvql77GDB__L-0MW_WEDCIU1bDSJLC8XQziwUYpj3LFH_j1yWGkkLg1_ENbmURfN9mQOCNPGgzEyeM-AuLXAhhAwt9NSQwSn1vqRpLU9tAgnb_yCKavxx4DbERbOZ7Ip6ZjWkXalKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkm4gd3mz6zWfEfx4NQBKdZBl8qr9MQz9Wq0WpHJ6I0-dXO6nf1q7cPdzdMzXWtFxBGIsQjdzef0QNbSx4L9G9Kq06G2knKo133qAe2Q-DE6FrwxLnsvLZlqvIxZgMGMCt90NwM5aKu1CEqTzuzmMVOVVDMiS5F_39Eb6psHW5lBeuTZy16b9Qr0f1824oUR2eh8QN9HLqDtv3v1JsnsgDuT0091yqAIgRMucWPau6j8bbyfpt6I_ACYaS4tn4JZru_o2A-EENoO2H5_xouBT5--gn14gi9V_YBywCmYmSl47yxl7tCMI9aOVa_tkHB8zBg9dHf_3kshpWQFWeL8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=A9SIELXwzUXeockhlf5jYMBnlyCUka4EIS03A06cFuCIQ2JMNFe9qNRLe7PicUx2urQvgV21uR9S7AwemFTiM1zBIq1cpzmcF-zFDhIVQ4lWmuXunXU0D7S3xEJmDvk2Sj2IlJSITXlH9k0mQH4GoOXHTjegfnU9i_jneTyzANV11xLqpX3e495-Nxu3eCeMviraa2k7ChbaVrMBq4jVer-6Itx8Le47zyXy2QFJ-KFwM2iwVO0ePy8vUdkl33UUsOa5_RzKOGqP-qLUJXDezyq4P_gLxtZOKo32uIEy9edwVnASfJKbZjYy_SVCbjn0F6moAGjIoXwnbe8Wzn5S2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=A9SIELXwzUXeockhlf5jYMBnlyCUka4EIS03A06cFuCIQ2JMNFe9qNRLe7PicUx2urQvgV21uR9S7AwemFTiM1zBIq1cpzmcF-zFDhIVQ4lWmuXunXU0D7S3xEJmDvk2Sj2IlJSITXlH9k0mQH4GoOXHTjegfnU9i_jneTyzANV11xLqpX3e495-Nxu3eCeMviraa2k7ChbaVrMBq4jVer-6Itx8Le47zyXy2QFJ-KFwM2iwVO0ePy8vUdkl33UUsOa5_RzKOGqP-qLUJXDezyq4P_gLxtZOKo32uIEy9edwVnASfJKbZjYy_SVCbjn0F6moAGjIoXwnbe8Wzn5S2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieLzCFEaxbg93XPQdmfa8ZDAm3sAHvrwIWdUSBGxvgnDOJO6qE5dXEPlgcJt6zQRbmpfWh_vORTkS-cY063u-GHo-chZgK1kI4jn7MGU8MALgtXry0CfMesimW-aljOZKXKyMHl0xoJ34bWPMKo40_AicmUwbDlVlIngTlT4Nqmk6jncsDcURMq4qmuWIeMBEoNspV8UomyCGpGVmACqZwlmY5WbKnYrazo8o_0fJNe_2GcS6JQPULBLR5RAUR3_f5kSciMK-qp_8a_d15Fl0Xtser_enHvW0Vjzr7mjHKZClYGFnI0Wx8xSCAt4hqt8qFxGagU2TcMN6NuUPOfON9mU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieLzCFEaxbg93XPQdmfa8ZDAm3sAHvrwIWdUSBGxvgnDOJO6qE5dXEPlgcJt6zQRbmpfWh_vORTkS-cY063u-GHo-chZgK1kI4jn7MGU8MALgtXry0CfMesimW-aljOZKXKyMHl0xoJ34bWPMKo40_AicmUwbDlVlIngTlT4Nqmk6jncsDcURMq4qmuWIeMBEoNspV8UomyCGpGVmACqZwlmY5WbKnYrazo8o_0fJNe_2GcS6JQPULBLR5RAUR3_f5kSciMK-qp_8a_d15Fl0Xtser_enHvW0Vjzr7mjHKZClYGFnI0Wx8xSCAt4hqt8qFxGagU2TcMN6NuUPOfON9mU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMwdnoXl1JTw-aAo-L70YnIQHLGCoq_wXuPUjKgDdNoRdmcPitdjqv3aqghwHDULVAQNU0OUG8TW-LDRxruEwk9giAAsXjZzZALBRngUmd4vX76xYdD-q8hfGNgYeufSj2J8zFRZa8tiH9QLYIcy8u35Ii5Kg4LPAawpKpyidoYsh_FWMwLAAqA-StMwsGQn69fDofSd-aVcXd4IL1zVsMdXFBk6I8Zi_MBMvJDqU0Ecw3Auw7x_BQG03jAoXMWu-SDslnXo9tp-YqBqwh81sILW7XbgnAhIYoXW44ZfUdyhjAgMGtn1b03Yfa6sLBsSlQ1Fzh72b-xIEeTyoUROXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A55Qc5B3r0HXTkfjMN9J3us4huSK3oF-3Hd7uVaarLrmJ2kRbWVKZ_rjKvWGbH5bJrsJdjsNiMcTZiNtw3xzt3asugRbbdij8tYuthA1NVUid1nNaD5PFuiSJWUSspJbY_mMSPUB6ZT--FXHdlFwQXR0Xd9Kmx5zFAzz8TJOhqjCuDkCuO06yAke8nXuB2gwmZDZ9qsqPZS7GO6xxxAHQvb0mritDC0bo-ev8H6aKe-E6BV0R40E3rTyKvw5msSp6dCruwDg_AvbgO5kvyYF8osQR3vrWj-7IN3JQbgMWNS-HNRNTdc9pEZ3fyVBxE4kr1I17ZTOpIcX41zMd6B9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhAqKP2CYYFAiJjSzmJuzW8QG7A3XVZjTb-Fs6QWTy_NN32qfo9q5AOBz_eKmvmuDAG40jiytkYyCZddNlMOvCzJsfgOpzJbWcpVnzTo4dwjw2irkPhMpUVcXdWvzVyyAR1_6hH-v8x-ARz0X0RnDhhxyjt0mTxe1V0JDnisxuhufCGH6GUkmiJCmNSVPfImqszB_TJCYv41Z6tATAum0sixRg6zg3b1wOdGgMGTWiTrySwJR3dUC6w8-3VYIYhLv0U0JitLUVeZwn6woTw-ZMsvybEcW593rvdSI_UJSJs4gP3fhR3aASp8B9F_gNKmtiaGU04_tVcO0tgK1VvxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9AbAnNYWEIjuBpbw12lIWZGzupK74W-YeazalrR1HPYxD70bkQC7nQlxS-PG7T-JB-R1GIgf9yigQ8NaOmswj8zxukSuf2N8kSyKrD0HnGX88092RRwOUD7N02JzEkkOZymdOmt9LRuKaoVtegd6Y2nT87vKAHQZytyJpgVKsEJTmD7cGaAVLNSLqj_dFvwMiQwoC045XQrakXZ_JnlBd3-wxCjV8inolaIckEJbBxtW3LsrbbUQTQACry5oTOtXdzLfwsNtaUBLjTj8yzsnhzNcItF824H11X16WkPFGY6j0EE-zwmYtTXzJ-n-tK9Wpt43GnFSCUi_lxP3FUCAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voLNj-DJaTy9Hcxv06hwYHetO9zvCEu3NaZpUxlYSOaPtjap3MnNpHWrQH0J7A9U1om0_yGfaMl-X94tQ1g11gyFpSTK4LEzzz_Qe48W6wMh_8u2rVGOEplWcAZbyvLBgveIq8v1mCZ8i5eykEo2moIxlU37MFsxsy_4DlltjXzyl10nh1NEGotueif1gusDZ7eup1JDDGJZOTYvDME3od0QYzBk2Fm_LFgyU6UJQl0aUdLqAGZ_rUy4Y0tVpwdvJPR-zcc1tD5lBhE1b0EG15n_0ln2pDXcguz9ZUuFFMEF5ZdIVAbQLqowoBcabBdgDfdWHB0snRCsoV5P8z0wVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=O66OP-c52mWMyCSbadcBu04-5KxpGYyBWFrjLpEBPVt--ShyzUJiL4np2qi96NCheHypsHNdh-9TnYnCf1u6WndMZZeifHQdVdd4g8vqkEGNvs7FLkmg2YUeY6LH4gZSxYjaZ3FuWHUZegHIVXtQIWTdP5-xdg-HpKv4P6JcoeEfJ6vgSRfkl3teePxunue-nybANRVJvx6kusiZ-qrGmiYyHr80Z3L9TgcF_nBmX6zQlgc_jfKivEb6dMxLIhXdK40EzDGS2KjCWvxq1NqDFIadwV3En_IHYozOmKceCqj5uM1TVVrjtXSF1aqizV-3QoRV74hd63lYJam9YcYp6aKCcyGwqRG0BZNvrl4GU9HNz0AvoxWwWFxZIpCCOsqr8QUmwTTgFZlZpV1X02cwd_r2qBL6aWXIykPZRhBkNFE6MpDBWsLfjPF4YK4nj7PuSe8H1QwOEIhOf6EfIjuk0vs8tN5aC-6IEZFxfgT15TUSA8oXFk7u76oLs_SLRxEBSxKvMk_f8zx4mm80HzaVTcLhPANYJsaBxLa_4AJvVfYPxcIqklV8mtnYeuYXjri590vSLNikj6Lb_8_ezjp8tM8fSJkarwubyay-Ct9afrBI1gQU6DEgmIFPV05JH0nhXfuYsKoMWVFsA9SuTy6IZX8jfc7VqeQgdU59MC3XcrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=O66OP-c52mWMyCSbadcBu04-5KxpGYyBWFrjLpEBPVt--ShyzUJiL4np2qi96NCheHypsHNdh-9TnYnCf1u6WndMZZeifHQdVdd4g8vqkEGNvs7FLkmg2YUeY6LH4gZSxYjaZ3FuWHUZegHIVXtQIWTdP5-xdg-HpKv4P6JcoeEfJ6vgSRfkl3teePxunue-nybANRVJvx6kusiZ-qrGmiYyHr80Z3L9TgcF_nBmX6zQlgc_jfKivEb6dMxLIhXdK40EzDGS2KjCWvxq1NqDFIadwV3En_IHYozOmKceCqj5uM1TVVrjtXSF1aqizV-3QoRV74hd63lYJam9YcYp6aKCcyGwqRG0BZNvrl4GU9HNz0AvoxWwWFxZIpCCOsqr8QUmwTTgFZlZpV1X02cwd_r2qBL6aWXIykPZRhBkNFE6MpDBWsLfjPF4YK4nj7PuSe8H1QwOEIhOf6EfIjuk0vs8tN5aC-6IEZFxfgT15TUSA8oXFk7u76oLs_SLRxEBSxKvMk_f8zx4mm80HzaVTcLhPANYJsaBxLa_4AJvVfYPxcIqklV8mtnYeuYXjri590vSLNikj6Lb_8_ezjp8tM8fSJkarwubyay-Ct9afrBI1gQU6DEgmIFPV05JH0nhXfuYsKoMWVFsA9SuTy6IZX8jfc7VqeQgdU59MC3XcrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Havd9S9ljK5KMMEnf5J5bWbVCDwmkYVIrJ398dvXkGL5quwQH0GmdeQ3xye9wERsIAQ_GAwUFL_U1TiVU0z3_k-uVcB9BuoqAjrpfvqIJ3y60_bynersL-0puT6xqJ3GFZqvGw_VTpT6l1nEZIea-1UP7Hj1lrs1vXnXbJZwfXKkj2KhsTpqNFRi1WzKMb0gsPmJkpw3-RNKN9dS8M_bq-S0-jCCdpThYqZzbc8Qp-Hmz5DgGkA3gLSspEnvqiyZ3tFtZ2ldkFKxS5ho2ikj2xmpu234foB3jWF_fiTwvJlw1RB6wM-gPb5bolMoY3WNG3sZ6Tw-KZiItjQIEQlDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=eJYIiCvuyk6PXsTisR-5oFx9-KCZk0NzsShqSmw5l4l5o9xNTLutv8WBGVzrEhHTIgjpx88pqy6uVC7D-bY6IsLe077noTtFPbnudiNfDBAeFmS04zIPLGL01r8IBql8O7yEvwqaD08NxL9lRKXS6HVVAehtVdivyGtpXZ4Cg46tIlFmZ0tQ1Jwbe1t-HtmnDT3EmXDUL_zwkb4fO0p1oJh2Jv0NVEyapzmI7USCQAsWFT2hxO_NWFlPPE0m9fW3XxZMAEdD---Jtb_XAfqdsyinfEEfwKw63IcyQ9oBegIM0fx9VvGAdTeLyORHkwRL3TuFI4Dl5WN01X_xEZnVsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=eJYIiCvuyk6PXsTisR-5oFx9-KCZk0NzsShqSmw5l4l5o9xNTLutv8WBGVzrEhHTIgjpx88pqy6uVC7D-bY6IsLe077noTtFPbnudiNfDBAeFmS04zIPLGL01r8IBql8O7yEvwqaD08NxL9lRKXS6HVVAehtVdivyGtpXZ4Cg46tIlFmZ0tQ1Jwbe1t-HtmnDT3EmXDUL_zwkb4fO0p1oJh2Jv0NVEyapzmI7USCQAsWFT2hxO_NWFlPPE0m9fW3XxZMAEdD---Jtb_XAfqdsyinfEEfwKw63IcyQ9oBegIM0fx9VvGAdTeLyORHkwRL3TuFI4Dl5WN01X_xEZnVsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=n_njODUCUqlVdV0KBHQYWQXV4tFuvdZbCn9T5YTnnUE1BWwEbL8X13fOhveQT8cpzgCOng-ZpGkE5WduxqURXixBhguXdgl_Pw20uYpkPfLbcKWVU3ckjQYFSXndshBsZy0M3RCx9DNzwTtQmO-uEc6STxvT7_joUPbjr7qKqmycCIjIO8xUSqJJKNiYdCTJ2uTgHTdIqJq3H4M-kZ_zOY6oWGTErG6Yy9PlNDSXSxZFZ66HzP3JVHT5-grC8CHUnVlQc_Z98BHdgaBZlE7YSqN8JMHc8VFNaUrLPiKEK4r2OweLFnWLDuFMHFkXrVq6yB41lR5eBXyf5ZYB3B2ldLCJKhMBQxrnS8TYy8RBf6y75iFTA3v0N6v0FaHd71334atuAIUcskC1GPScJCV4n4cgFRM2ZAVxd8IzrOJTmt6coeC12UEDEUYS2rot9MrEH9kgr4fEkLFY4-KgZE6satwN8uIVZyt58HOcPGE_t5WsPZ31Z6S8Tjk3QkwV8VvoqUBEzwWgq1MMmoLJJJK_zpOsLEwF3rwiWyLam1vTMKwTuTGcvBH8S1wGC4ZYVeW3LbgEJiry2ak80ceEdy7oESM_pLUDyb_ycg53APrF53yVtK_dVlhUI32kx-THpS9Qq-pOGxip2c1ggMEbwM9Vdnznw7F9rAEAS-emlw9u2e0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=n_njODUCUqlVdV0KBHQYWQXV4tFuvdZbCn9T5YTnnUE1BWwEbL8X13fOhveQT8cpzgCOng-ZpGkE5WduxqURXixBhguXdgl_Pw20uYpkPfLbcKWVU3ckjQYFSXndshBsZy0M3RCx9DNzwTtQmO-uEc6STxvT7_joUPbjr7qKqmycCIjIO8xUSqJJKNiYdCTJ2uTgHTdIqJq3H4M-kZ_zOY6oWGTErG6Yy9PlNDSXSxZFZ66HzP3JVHT5-grC8CHUnVlQc_Z98BHdgaBZlE7YSqN8JMHc8VFNaUrLPiKEK4r2OweLFnWLDuFMHFkXrVq6yB41lR5eBXyf5ZYB3B2ldLCJKhMBQxrnS8TYy8RBf6y75iFTA3v0N6v0FaHd71334atuAIUcskC1GPScJCV4n4cgFRM2ZAVxd8IzrOJTmt6coeC12UEDEUYS2rot9MrEH9kgr4fEkLFY4-KgZE6satwN8uIVZyt58HOcPGE_t5WsPZ31Z6S8Tjk3QkwV8VvoqUBEzwWgq1MMmoLJJJK_zpOsLEwF3rwiWyLam1vTMKwTuTGcvBH8S1wGC4ZYVeW3LbgEJiry2ak80ceEdy7oESM_pLUDyb_ycg53APrF53yVtK_dVlhUI32kx-THpS9Qq-pOGxip2c1ggMEbwM9Vdnznw7F9rAEAS-emlw9u2e0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=PNrWqdfy01ChjDetHoKv8l5nrX2TlyOhraF8b-BlTeTaO3r16YP542LRXSZfAsxPafHMYs2wVq1gWvi7TKCV8ZuAT0cHpIgy9WAIREAdfp2HYjR774g01vFDVfuvkGEzWfpCLquK6m2ZXXVqccEqrdTgiGiyfwLwUI5VR_cIs_Dv5Nch0MS6sXEklCYDhja1QB_UNnlxMTK3QiTZ2g6GptCNqhQ9_pqEzaQ1XzRsN7de1nlLL9o88tcJYpw1pSCIasnve6XzntjTYizb2LqYIZjNYyDBki-SG4i9JoCCo9leZwWfJlAW1v8TmS6e7U_aLaZfpyrbx0m0xVi5JGVkToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=PNrWqdfy01ChjDetHoKv8l5nrX2TlyOhraF8b-BlTeTaO3r16YP542LRXSZfAsxPafHMYs2wVq1gWvi7TKCV8ZuAT0cHpIgy9WAIREAdfp2HYjR774g01vFDVfuvkGEzWfpCLquK6m2ZXXVqccEqrdTgiGiyfwLwUI5VR_cIs_Dv5Nch0MS6sXEklCYDhja1QB_UNnlxMTK3QiTZ2g6GptCNqhQ9_pqEzaQ1XzRsN7de1nlLL9o88tcJYpw1pSCIasnve6XzntjTYizb2LqYIZjNYyDBki-SG4i9JoCCo9leZwWfJlAW1v8TmS6e7U_aLaZfpyrbx0m0xVi5JGVkToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eix_akK0_shuVJF6S5qlfPDNJUvVCUo5SR1qpcJFUW2agbC5OhIZbsuxKa1k_F19dMMzMQii5AI-Ccw7KDBlwxkHQ03TVxcR60CyxYzCjg7PwI-WU6j-ZPeVYEOeZ5c-rBEf7eReTbdnkBJOEoF-semYiuzWEtIblMtSPbqKfC_68BVatMbC118hW1sSR22fzOFLZsJH2mT9gdEv0FtYNFU9FC9itvc1sRqHUB1V0dAkXU7KGtOyIvSUlrBhTcedOooEuixL9eZqNqvndN3ugSgALvi57bc99RfG9Be1wmHzoXi61aAW0xssP_0ndQjZcI38p_yw7DQkBqwCtM0tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRadOmq3JgkmeWnnWJACNTDxPyQwCI6XBRBKzRaBYXtjnLxE2xrJHD1a4NPg3cmZrkL_V8XiHqWP3hx5Iu6mBiVTuuHhAAuGefrJ3Uljv0Xf6WEWBT5cX3ajbhXjNPFYdJdY5wYMlK_qU5AtYAYfjE9rVgP5o_CjtpufkpONlmQGPY_Qb374MpDwIqFY916XyyUwa_dh2EBKtdsbkUCwcdZakv7W_19kZaIdoY0ICMAhgax5V6QqpPSGeY0BTuGIxU3x2PxQyEIFhff-JAgA-4rErZgGkhtNqH6wvfiFBU6gKZNcocX_Vz_PUx9Pwxkr8AyHDnzjPhbWzWgcaTNLLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkKBxqb7T-0CMukmexGmooP6NW-ADBOfX8Urj8jn_8EOl6WWM_gYdFtZzBz45ak_oFGUpbyHICzTDoDwqySRh8oYf4FUT6qPRoNJtz2Nm_5eu1Piw9Q5tcfLvb4m5njWnchwYmzuKYJCZOwrXEKN8P3Co4V5G1iYobOJr3OC22R6ccTgTWcHdXSLRr5Hf48WrHkrUDz21cljJRy_jxmLFd0jvL5HAeaGpt0OBqwFrBAtdOrDilqYwo6HTqyLKc_UG2Ip9R3POLWknb_gWY_fGds1ZJyI0xJY860y18g2hZmiioH2BV7os5vdz-0_1-4zfhHtNpJrMi7MqW-IHVXS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNHbt5qBGr-QR-A5W-9vua-C-yhfGIOU5I3a7MvKVzJTxcHd-2f56L7jW-eYMCz3f0obGyQ0nv05uxKCEVdKLALhKIP_sNwFO11ZUB2ei7h8A1SReONPkZVaag6k_ulOObNsv3Q8NqrZJluNjHRqgP0Xaukx05KoJAiUJF5TVVUIpvzmSyaoKjWzERSyJTuVrWj-a8E0VF5BZqm5UeqoOHcPFZnNwUQLLkhJcbZi0dfiSmzyOO-vTu17UKHe_04sRMTpT7jRo4KwOtKREZ7-gHe5V5JelcTuw6Xm9PFCcx2XIV0P01EEPihZF9QpyeB0QPTlhSz1zdvx-E_r17BJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQPlZailMfq7IaJljFj-nUA2iZnZoP0axtPNt9rS-dD7hyRyC5QyvBJOalOrkjfBeww6XRmP0pSxd8o8usZy7H1Q6iDSzPLMIftHyqwjtf-zeEpVvQ2eAbrr2k1sPU27OCY652D7gRTVFdoS5TTAMPPrSuiItUChecbdv-u47wSYR_tGwjCPauo_lBi7homyo8MFM2691d1pBBXmk2gMpCXNz6USzmtfDeoaRcOqUhVKomz9w-TtA-1H4OKEbG2uJ5kPZqiHZ5FHYQeNmB0C0VhzvwZc9PjDaxdnH8aa4wj1QsmKTYhCoMcIuxZQHEoq9Vt5uyEbd0PmYMPvmoXfSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IGleWglThK0x1Rxedz3nX7uPry4b0N5JJHUIWPfEq_lgfjc7iNmgifa81gfYP3w_amb5JPW8sB0ieUkdf3zYXHnoq_8mGrDl3A0rwumKtFys7atT_KfQiykY3REjZsMqRtFDB5nhWFtX0k_kDC0tjrRWwni5QA2GwhWvg458bsx7pvlNGsXw6oHv8ICaZnaur-ydJsuUZW5SskcQoNlBN1Iupg79nIamwZRi2VNV7WkvOZM-GwvZFEiX6BKu88CnZtsxFySh9ePYY2wnyn2XFgBWSr-0tJGYPYBGOT97A6lMvNyc71kIwI4dJhw4lUNWgaHolScFQ1AaviQg7mXyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=IGleWglThK0x1Rxedz3nX7uPry4b0N5JJHUIWPfEq_lgfjc7iNmgifa81gfYP3w_amb5JPW8sB0ieUkdf3zYXHnoq_8mGrDl3A0rwumKtFys7atT_KfQiykY3REjZsMqRtFDB5nhWFtX0k_kDC0tjrRWwni5QA2GwhWvg458bsx7pvlNGsXw6oHv8ICaZnaur-ydJsuUZW5SskcQoNlBN1Iupg79nIamwZRi2VNV7WkvOZM-GwvZFEiX6BKu88CnZtsxFySh9ePYY2wnyn2XFgBWSr-0tJGYPYBGOT97A6lMvNyc71kIwI4dJhw4lUNWgaHolScFQ1AaviQg7mXyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5htVkbFglC5x7upCBv7LPMY2ZSVhhzmvFcz66YzA_xB7YFudcU-lAIuZGviejOjIiK6q2ukSvnaYYkTm2yH4uwx4QvApw4E2wGOgvHOGL2mg150LVu79BrRmhKmy_oyIYstNtAjW6K68adGFeQECG9wKeMPVoNCFDrlWHOqX71-KQlphCtzJnOCKG5Svrdg6i46Ki35FN8WHRVFL_FxSQv7u5TthIs4YEkISgNZKH_-RQIjQJaOxS3ZjNrJohDkXEWy0VZTcXwlUnBafVCjhH708h6WcYzK-icTp6Z6OIlafbQ3Z_lBVa28nBDg_zvW_pKKruH6zOgzVDOfPk2ZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT2JMhS5aQroJC5ECx832qT7uG7cMUgtIo-TUbDfir9WzIDv649iUd9dhqGE1JHqiPmwrJtIwVibfo2tuOHp6Um3jODz66foK_bhlWpeQYV_-7Vw94qANLLHYruxvTFiFgrZI4PUdQsfNlzU-d0IDqdLGsGxtYnMpFnyLruPpqAcXUoQ80WprOUW5O4rMLbxafb5XYabnfAicIPLZ1NbLiJjZrs2CgNE-0yJiTk_Nfap0yHCi7Ktn4_43__9vzNTtYoNhuSnB-fdJNgyJAku_M0nfWM8ZvHqFB2tQfHS4zZenSj5_J7FJl4Cd6Pr8LsX2Puf0qGZNeSkhsqhdyGHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwuhZyiSyLE5aHt67lba2Avrz_dji5PGig1ApaNjZJ9D4eAemshHtGRQSX5zFr88b3jDuMzZZjUQx7HovNsAcCnCobVpvYiYOPmuRtXgPFbTEYcrh68c0hQrMSiMOs6xouXbZX-FirYXP9HNqmwjTUiL_v69OmG-6-wM3pmSrujTSsqaAzEs6W5rMkyPGZrUxNOWjuCkpJkr4JEs9vYpQl5QDvicW_jLCAW8CDkeBzyQkGssnYP6HftlTbK2iEZPPAUsJAkc7dOIhQbFFo0n3HaEdAZMrJenUsLM5pMekf1WZ8mShIufErgji0Z6kKMLyxKzI8ey7tKhPpeRY0W0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJg8ABz3XtqHDo4NjH92b7O7FDBGjaNcFB1CEoVKxK2GWc3_9WUZZ25iAauGiorT2bpCNbiXZflGgMzgy15xSFRT9da4PfSnE941R0AUQ2i3MshOf0dP5nS_NABiomfqnx-2XNqBghKVLNEcsNFUBTKAQZnq4xYGOyoAzEcUA_SwPCXsaWqFAssZV6nXiEBmtKcspvXw0Bp0kOb5BLVS2lHDiIDMZdIMij7_GxpJN7ObrgWZ2QjksTvSbrkuq2jB5O07l18BMqjFRyxhdj7Ldq7uVekwlltZ-5D7hdE5s8XUJC96N5yEdCfGU0ytwyKFj75lnhzD_yPghXlurtQyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uppOfQ8-FmFQ25Fok52Vz7_LH6bTHmsS2z8CPFHEr0Pe2L_UgVOdoiM-8Lrt2xAqkg6vpyeXMD-xRt7cFBed8y-d2SVnLMKxZz7eiclOdvrZZfu7kF31b1EzWhkzFj-c5vAeV_fKKSQu2pUcwUKMjoyNYLZ43KKjPxkgGO6qXl2YgPrFhl-1uVHESZNLbhHNsJ-lFir9zMsz56sFVg7t4MdoUeN4pE2rmIBSLmqxASI32vGywF6VSGgqIMJK6oEG7MoqM23AvrvHpy6wPlWXh6gELLzauplRgJoKKzvQWVHqEVA8LDK30Te07_5wSta3tqIsX0xji8d3j4xy5s21dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrBudp8Jar0HQ_ua9Q1PRs3M1qXdC0lDXCFFlEBxdMvkA3PWXndF7tHeZ_9gKTmeyRUIMooPmoh1a36oeV24tSFbquL7VbpZoBfFtt_yoicEt_9TkxSkZhwBaeZIaLmWoNruXGjz7xpQaKII6FQjDTd71zmXrxPD97qfuwuMxlhCZ36OQghWCAEm3_MnKO-_4QbxfzsVlcTj80pi-o0PzYeShVL0SEmYdAVNnRQS3YvirDDlapRkSRiYz7ye3Ko1yNU5jBl2gxSCXLANxiW-pfPWp0f_6djEjXImY0PukpfT2cHcO8kvAyd3g7xMeqpDB3KZaCEqWzjsmBP8k6rkRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmuemOU-KK6FP52z4SKLjDvrV8oJYI1zDKlV15hqHCeasEMDtP64yB3Y-bMj_OZnPDMf9e6Sji9E8erWgdZnJsdowqrdKnD6XJC_0qKFDh8mzcmJuVXVYUT8xN_iR99B04SFFONjw8xejQeWqCQmRCmo7T6CAFhrTMELY2UK6kW0ijDl56yVNYASq94iW_WdE_u6A2zFoOuZ7L4B802vDycIMPWY4AixJ0DlsXFE9kSQzzygGSVQ2zsETdgK9ntVzzHy1BTtHLtNfyRVJqfbOnMV-Ns30siJSePHwUxI-x65FUqgk40RFWfOl4TvfdZSODCWYi8cCHrEF5BhzryHCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
