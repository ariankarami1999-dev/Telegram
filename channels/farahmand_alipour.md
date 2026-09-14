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
<img src="https://cdn4.telesco.pe/file/FyqkbHXTB7hEcEEh7q1Bfyjd5vurG1-U2CcRrw7cwtSYn0TTprKlSPCL70ZChMuGU5HPO7SneWYrO8_2U4TI7FsEeDT8rSiJkAkZw_kXu1ZoIZs-RTDbtRC24ug5t_L_eGvhDUWZwUVzdh1hTtblE-_V5LNz0bF9mZ4nlcTH4XoxH6zyQaVvRjzpJE-60XIvq5xCaPWN4E6ND1ob7AVUC1fyoSxkVAk1WG2nJTjMss51lVVLW13I-w67W4PwBQx8tEJ-7OMH9MiMeA2QEpqsfFA7IbXfehTBXEHgqS97zTbJ207ip0w7j8MBy-_sFnofHE0uIgZhmGNLp-KhORE9RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3QjYtf3tYBrORlobdb-ztDs9fnKGhEbE1FzIB1d-8LMWccHBg02ePQK1pvmHujKgs6wDmaf9SJsR4ywUlXsXskOZMUktFEj_jaISqiTk2lmYFiMYOoyL6uUESmw9-4gCZen1ubK8IaI-p-6Ydo_LCGSh_JK3UoZVDHih3eqJxEhtgQGQHa0k-Wd3zuC-20fpSwWjjkWUKncuB3p3tsHgFyBoekpoNuT-Qu4ZGq4djbcmx6zexLJogV5jO5RUfFWrekOLoARVxnKGVL6-MQbik5p38LDXjD-ms8LzJ58CaC5pVGUGfAoMU2eRuZyT80ZC6uRx9FIxrboLh_sFcqn-qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3QjYtf3tYBrORlobdb-ztDs9fnKGhEbE1FzIB1d-8LMWccHBg02ePQK1pvmHujKgs6wDmaf9SJsR4ywUlXsXskOZMUktFEj_jaISqiTk2lmYFiMYOoyL6uUESmw9-4gCZen1ubK8IaI-p-6Ydo_LCGSh_JK3UoZVDHih3eqJxEhtgQGQHa0k-Wd3zuC-20fpSwWjjkWUKncuB3p3tsHgFyBoekpoNuT-Qu4ZGq4djbcmx6zexLJogV5jO5RUfFWrekOLoARVxnKGVL6-MQbik5p38LDXjD-ms8LzJ58CaC5pVGUGfAoMU2eRuZyT80ZC6uRx9FIxrboLh_sFcqn-qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=PFNFRB6ZKc5xu-_vF_fwMH5gFZ8kFBR5rCeFWwf5slyD-7oanm0AhiYK3wV_5IuXqhZv8qpacu80Iqp2rvl0rGTl-7QGpzCzIGZcDuJEljzydi1OMLwj8TpB3VsprZCAtmtAd-cehFIv3LxULvLmFXkQw8CdvLMURLWWgR16_z2BUDFyeT4YilaWanXkTpA4dlic186uc2Ta8jHvsAAYhVT3YWC-AfYCCnndt7qma24q76ptGIIDbniHwUmBTJ4H5ifdW-0NPNamvOSNm_H0WQCp6X5EQ4f0Dkbv6Rc8PJJw0tWBsV7lN7yMtVc4i8t1hy1BVEtqVT94Futz13jSJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=PFNFRB6ZKc5xu-_vF_fwMH5gFZ8kFBR5rCeFWwf5slyD-7oanm0AhiYK3wV_5IuXqhZv8qpacu80Iqp2rvl0rGTl-7QGpzCzIGZcDuJEljzydi1OMLwj8TpB3VsprZCAtmtAd-cehFIv3LxULvLmFXkQw8CdvLMURLWWgR16_z2BUDFyeT4YilaWanXkTpA4dlic186uc2Ta8jHvsAAYhVT3YWC-AfYCCnndt7qma24q76ptGIIDbniHwUmBTJ4H5ifdW-0NPNamvOSNm_H0WQCp6X5EQ4f0Dkbv6Rc8PJJw0tWBsV7lN7yMtVc4i8t1hy1BVEtqVT94Futz13jSJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Ox0_88JZvlmyAgDRiLwaMqoJSuYcR1VmlUkvspZk9abDueD_HYToY_souJeJr6ViwBtTtwOxQFX1FZWIgVEXis-cspovsb-GnmWxX6VmpDW_Mn4p6XxFFm45RJoOZvQbgE0xKjngF79zygHaz7oKa1fqTk_x38wOrr7YzMhtAFAY35UK6Sm05zt49SRwunTwfvj7BxRpA44uY07dvTacQi6XwWS7QbILJj5T003RMwStUU00EayDNuJQH5XtFqe-WRyU0b3VTXGQPNFXPdaCCvw7IRWKhlsUpMgXs491DjHQOuMbAcdrJ7EEsWuY-9jbG0wPSeCNxyRVTZNEglsXULmN72kmVk7rgP5b5hCMZ6x52DUljwuo8L0JcqVgmODWPQ0mBvBH9Y_m3XyRpXvkrRkL2HkZ0U5hvT8qZscBk6zTyN8bZOFYN5kSqkKcaTKMcLJXzAyi1u-6cXtn3qPHEqfpumPAcS2eWhbYzsAreUkqk7H-P6uGulWNmcy8qVFu50P1VyGx-1QWJSD3RRZDJjvFyS61eGnyYaSF4sMBbvKHHSy1denpsZG1CuYlEh34T7-eRug96iAOwkOQJdFpj0caKm0NNRbUHmZtxOag6aLoHdgdiNVxnpEiLbhmXdu1wUbjIw61e07c0xoXj74rXhRCE0o4OpesRqQpgXQqyFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Ox0_88JZvlmyAgDRiLwaMqoJSuYcR1VmlUkvspZk9abDueD_HYToY_souJeJr6ViwBtTtwOxQFX1FZWIgVEXis-cspovsb-GnmWxX6VmpDW_Mn4p6XxFFm45RJoOZvQbgE0xKjngF79zygHaz7oKa1fqTk_x38wOrr7YzMhtAFAY35UK6Sm05zt49SRwunTwfvj7BxRpA44uY07dvTacQi6XwWS7QbILJj5T003RMwStUU00EayDNuJQH5XtFqe-WRyU0b3VTXGQPNFXPdaCCvw7IRWKhlsUpMgXs491DjHQOuMbAcdrJ7EEsWuY-9jbG0wPSeCNxyRVTZNEglsXULmN72kmVk7rgP5b5hCMZ6x52DUljwuo8L0JcqVgmODWPQ0mBvBH9Y_m3XyRpXvkrRkL2HkZ0U5hvT8qZscBk6zTyN8bZOFYN5kSqkKcaTKMcLJXzAyi1u-6cXtn3qPHEqfpumPAcS2eWhbYzsAreUkqk7H-P6uGulWNmcy8qVFu50P1VyGx-1QWJSD3RRZDJjvFyS61eGnyYaSF4sMBbvKHHSy1denpsZG1CuYlEh34T7-eRug96iAOwkOQJdFpj0caKm0NNRbUHmZtxOag6aLoHdgdiNVxnpEiLbhmXdu1wUbjIw61e07c0xoXj74rXhRCE0o4OpesRqQpgXQqyFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=QNOzv4lEOIQAVcabo1_AznbYoMOjF_aHjfzQaxObD3nnNLRXIzk7Wki1Y_CW2Vopj_iB9KpQWhy8LqaNshUChGp9YgTfLTxYDbF95cKcpQn5FPQiLqsMObQRsAw-qyrJkvvq449Tm8h6ys5Cut_HGcG0pbzpydO674whTJRSgQPM851RtcgndTiMR6RYSGA_1jin-J70YK74CjwNeNYMUvSga_klNw6DGyipjxsh6_uhV820lHUGj6e2Fvn6EtM9VROKcUQT1wpO5ZD7GlKVCdnVDRCpiG7Z0rch0EA8TqLy2SUDpk20I_JjfVORcNamIYLs4l40j_9rCKao2UidYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=QNOzv4lEOIQAVcabo1_AznbYoMOjF_aHjfzQaxObD3nnNLRXIzk7Wki1Y_CW2Vopj_iB9KpQWhy8LqaNshUChGp9YgTfLTxYDbF95cKcpQn5FPQiLqsMObQRsAw-qyrJkvvq449Tm8h6ys5Cut_HGcG0pbzpydO674whTJRSgQPM851RtcgndTiMR6RYSGA_1jin-J70YK74CjwNeNYMUvSga_klNw6DGyipjxsh6_uhV820lHUGj6e2Fvn6EtM9VROKcUQT1wpO5ZD7GlKVCdnVDRCpiG7Z0rch0EA8TqLy2SUDpk20I_JjfVORcNamIYLs4l40j_9rCKao2UidYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZbPSwhfBGMKxVmmllj5ywROGon3ZEERk8sYrDxF4_U8blpSwsNlcSDy-oza1SMNyZNzR44yopzrdJC54gc77TY2WvSbBOoxgJCoKdDlkP8v3yHQxd6IdGiSfDwnUKq7OBe0XlSKsxAhn2fJRtpfroMhyZgtV9hGHkOhM0ujRxF96AGYt76VJnu4Nihn2ICVkXUNYjs2wVmsay6AWuxAYC9jdSeOjiAZW-WyO8EH-vm_A0iAy5danmSPGsfZFBgdtnN1uoyxlc7LYSDJSJmcCkAti_Oa-_bsHpyRcd4nFJJ2K-P47nX5cDbSz3yEGtZOw6KxZ5jKgUnZgd6y8Ubhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jDn4zd-nSGvjb5rLcen7s1KazvaVk_QrQco3M7Hj9u_TqG0fujVdivpEBvImzZfGHjAIHC3PyAKJdD-FurhJaRzK5X_V6u2I2aua_nv7Kcti0eQF240xZaizhmpChNcxhIaGqihACWUM3jT4yVYQTx5JcoGam5r8mt3Pu-jfw49tOYuOHO6Dj8JxQoe9ND2eshutHgKMF33Kv3ZNrjWrdqJk86UGw2L7jhUOgkD0HQ0SFOxmrNCgaOkxsVztWFWF3oTjBUkLZ269dNqBrLI-9BX-nqu6Aanum_sq6yQdG4Owp-OezhNNIQwB64dkbZAMY5KTuyac6XZtK7TUP98hyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jDn4zd-nSGvjb5rLcen7s1KazvaVk_QrQco3M7Hj9u_TqG0fujVdivpEBvImzZfGHjAIHC3PyAKJdD-FurhJaRzK5X_V6u2I2aua_nv7Kcti0eQF240xZaizhmpChNcxhIaGqihACWUM3jT4yVYQTx5JcoGam5r8mt3Pu-jfw49tOYuOHO6Dj8JxQoe9ND2eshutHgKMF33Kv3ZNrjWrdqJk86UGw2L7jhUOgkD0HQ0SFOxmrNCgaOkxsVztWFWF3oTjBUkLZ269dNqBrLI-9BX-nqu6Aanum_sq6yQdG4Owp-OezhNNIQwB64dkbZAMY5KTuyac6XZtK7TUP98hyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hbeYist_PTUQZtjB7byoztcM7d5Ney4II0OfxU3Zir2IGCCyl4SSlL6smFjqaBXNCGvPYTJXfjonFD3BX4kTVxPURNUJO29aLBaMwWlNEi6WxBe2KXxjOpsmyO1g9-qLxeqoIRvmLOyATgk7JPHn4zJH_rLQXNGAmbqt3ElKkgjwd8rKEaC5HbXvYpHlYfWo25pxNLJkufKi0Q1AhsWes74HRvNqOOEgbYZvF-NP4msMWkNdzewM6AwyYNDoe3bMXhQo3_TQTBTtfE_onca18mWuHX4P6XMj16MW44xxLJhhFURuhSTl3og2yfKi_hSC8u1g_YTMkd6c7TykG3srZpQdGyVffSwgUTZ4sqiqXXd0lhoeDkJ2ypbE4vk8X2so-unAcTCsKs_P-xEDVn120DUaVQyQ6t6jLvYIK6b-x8wVmIzYKgaaHhyCfKZQjOI1v6496GqRcBy9LnNsqID_ORHjKu5W48bsaGwGgcO4HJ3z-1KD9mZZtjMYJb9zU5uGhYixCVqo3dfs3ZVrw6hRSaTBoVDh-nthVDNq-3SLaR9RrFp9sSRdzaxdD9wNyQ3kALUwqP1ZD3PREt4RAEmwL00oTrlYEGmW4oheIlI5-hfOuhKqgRb2yWnZRbXHW0yPKvwzRHGHgj7Kg8YRDQph-jp27W0EQX0ErKYUhZ3H_sk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hbeYist_PTUQZtjB7byoztcM7d5Ney4II0OfxU3Zir2IGCCyl4SSlL6smFjqaBXNCGvPYTJXfjonFD3BX4kTVxPURNUJO29aLBaMwWlNEi6WxBe2KXxjOpsmyO1g9-qLxeqoIRvmLOyATgk7JPHn4zJH_rLQXNGAmbqt3ElKkgjwd8rKEaC5HbXvYpHlYfWo25pxNLJkufKi0Q1AhsWes74HRvNqOOEgbYZvF-NP4msMWkNdzewM6AwyYNDoe3bMXhQo3_TQTBTtfE_onca18mWuHX4P6XMj16MW44xxLJhhFURuhSTl3og2yfKi_hSC8u1g_YTMkd6c7TykG3srZpQdGyVffSwgUTZ4sqiqXXd0lhoeDkJ2ypbE4vk8X2so-unAcTCsKs_P-xEDVn120DUaVQyQ6t6jLvYIK6b-x8wVmIzYKgaaHhyCfKZQjOI1v6496GqRcBy9LnNsqID_ORHjKu5W48bsaGwGgcO4HJ3z-1KD9mZZtjMYJb9zU5uGhYixCVqo3dfs3ZVrw6hRSaTBoVDh-nthVDNq-3SLaR9RrFp9sSRdzaxdD9wNyQ3kALUwqP1ZD3PREt4RAEmwL00oTrlYEGmW4oheIlI5-hfOuhKqgRb2yWnZRbXHW0yPKvwzRHGHgj7Kg8YRDQph-jp27W0EQX0ErKYUhZ3H_sk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL0sBMXVei0b2yfK9ciEkmF8V23met0IVVrY4GP_UyPeWzbjYXzTomXEPt0hhqF5frE7TB-NjtLzt1hIoJgyBGJpEW1fzJxGoNfbyogeEdg_ezRDxVexM1G8bjhobMM-Dy7GqVXuGpajP7nclZb_emb5a55k6f3iauLpfUjxkPIpDiwJPDvOeAD4wDf83GyZS0A1qxuawSIHuT7Dc__iY_CXdkbx8Oi9zwYnJkJmVMt_FRA1WIQiWjZwgA23lRstjrKoq70izsL_F9nyfgDByULrSchDfUUdRWeaFP3Tly2ZOlr-tdePHmNlg44Z-xWAXdt1OKfcnBkuKE8ZTvRVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kb9OehnaLTpbEyXzxOJZEQ-BLH12RjoKOyXdTLfHg8zpX8mI3gBkhUWajjtIw6zjbEZfoDEJnbeLMIElZuejJ5EhaMPpZF2A5Azyc4CooaozVm4wQbJ_DpIYEPSnpppJHd-6WMu6ZgiOIFs4tyQGi9elIxGqxJdJ07IFwn2mcQPoRSG_jq_e3FxPicSjBzemWTHYBJC30fQYfYUFBXUXkIUgIjcgpHPN89Yzu9nMUpv8KVDqtuR1nRee4dihNMeCLdbIbDcXOzLaX_0iuR4hNOntFiItcQJKeyBZx5wjZkikmQnlqcTW7N3A8KsNWwLk704f0Fr9ShWfsnX2jeF0FDd5gj23RKP-dCnhd_4MDzUWyyiYDxsxijTStAlRXCmmeadM93EUJXxBclL_PRXhauEL_cMmnMNMZVqcQL3GwkP40D8DGrxH1rDSpUDTNZF6LTfA-fk6tozOicdoYGUYyd_qAL_wzEZgXr_R3ob0igAG7Bp9MU0w-rsDHiqrRGHScmpsxdJiys7MmpAvTylehGcHtIfNuMcFmNLwNphA1IS1VdFCvvj_PdtOtzhNaFO2ZrM3QJIN6O3ZirAfWAV_6GVx2hxrPK5jNTY-NfxwH9hm5rPL44A2oiEVcnBLPjC5c7j9XaP_c_Zuh9CJ4cTjgZ015WbcuvepOjx664FaJYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kb9OehnaLTpbEyXzxOJZEQ-BLH12RjoKOyXdTLfHg8zpX8mI3gBkhUWajjtIw6zjbEZfoDEJnbeLMIElZuejJ5EhaMPpZF2A5Azyc4CooaozVm4wQbJ_DpIYEPSnpppJHd-6WMu6ZgiOIFs4tyQGi9elIxGqxJdJ07IFwn2mcQPoRSG_jq_e3FxPicSjBzemWTHYBJC30fQYfYUFBXUXkIUgIjcgpHPN89Yzu9nMUpv8KVDqtuR1nRee4dihNMeCLdbIbDcXOzLaX_0iuR4hNOntFiItcQJKeyBZx5wjZkikmQnlqcTW7N3A8KsNWwLk704f0Fr9ShWfsnX2jeF0FDd5gj23RKP-dCnhd_4MDzUWyyiYDxsxijTStAlRXCmmeadM93EUJXxBclL_PRXhauEL_cMmnMNMZVqcQL3GwkP40D8DGrxH1rDSpUDTNZF6LTfA-fk6tozOicdoYGUYyd_qAL_wzEZgXr_R3ob0igAG7Bp9MU0w-rsDHiqrRGHScmpsxdJiys7MmpAvTylehGcHtIfNuMcFmNLwNphA1IS1VdFCvvj_PdtOtzhNaFO2ZrM3QJIN6O3ZirAfWAV_6GVx2hxrPK5jNTY-NfxwH9hm5rPL44A2oiEVcnBLPjC5c7j9XaP_c_Zuh9CJ4cTjgZ015WbcuvepOjx664FaJYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lbXdhSjAf5Mb68r8uaEekxNlXLmQuOZ7HP3fzfr5cVpvTDb5lVB2IcvRtYlIoTBk12LIgvm7KIyTpExt-MVOXu0h5DLOEtrb0ugTQEJ8Q9S2zdM1bjqH7qEl8r1Jk_6srhRTQt5FCXAscLE40qaQRrvtxuclIxWTGUeXXxWCX9xR6QQQdCsm3Ms2LgM-t5i-2wR2NXBlRtiRf4JANPMGgf9sTuomNiyeA2u9BYSnLY2p-C8lx1wTFAQxQpObPAduV9xNSJfAW49PrlXMJFyC853941XT8r_Ef0X-S4bhUQcNpP0nRVF3mLn1wp1pNpP7sL_54R6qXyWUoCayA_Ci2XZHYO0jJJNCXtwRjf-wfcwmTpFmmL8oHtHSO2NDT4_7ziRdME3VGRnZy5MVmxlQX5WP3VAqBEaWMIzEOq1vzNpgX09g9Z1cxhJXYDeaF2oIjNccp94hJWSA-4WvNknoC3V1KQpMQMJjdje_9j34nJe0dYq-KRcQ4FLshIP_177bVMto83fqE6kN-LMRzISvn4qntDEE7Wd1rgu-n3-lclzxOepS0eQMsYPDgyv8Ltdy08_4JYRCDgsR5fThBfn5uj3sirzt2pxNdmlwyL7z0zqV4LPyFFywVzpciWh-AcFCt49qLp8GFYqQm_kPwZyhKxE91JJQj-qehiCN9TdrXUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lbXdhSjAf5Mb68r8uaEekxNlXLmQuOZ7HP3fzfr5cVpvTDb5lVB2IcvRtYlIoTBk12LIgvm7KIyTpExt-MVOXu0h5DLOEtrb0ugTQEJ8Q9S2zdM1bjqH7qEl8r1Jk_6srhRTQt5FCXAscLE40qaQRrvtxuclIxWTGUeXXxWCX9xR6QQQdCsm3Ms2LgM-t5i-2wR2NXBlRtiRf4JANPMGgf9sTuomNiyeA2u9BYSnLY2p-C8lx1wTFAQxQpObPAduV9xNSJfAW49PrlXMJFyC853941XT8r_Ef0X-S4bhUQcNpP0nRVF3mLn1wp1pNpP7sL_54R6qXyWUoCayA_Ci2XZHYO0jJJNCXtwRjf-wfcwmTpFmmL8oHtHSO2NDT4_7ziRdME3VGRnZy5MVmxlQX5WP3VAqBEaWMIzEOq1vzNpgX09g9Z1cxhJXYDeaF2oIjNccp94hJWSA-4WvNknoC3V1KQpMQMJjdje_9j34nJe0dYq-KRcQ4FLshIP_177bVMto83fqE6kN-LMRzISvn4qntDEE7Wd1rgu-n3-lclzxOepS0eQMsYPDgyv8Ltdy08_4JYRCDgsR5fThBfn5uj3sirzt2pxNdmlwyL7z0zqV4LPyFFywVzpciWh-AcFCt49qLp8GFYqQm_kPwZyhKxE91JJQj-qehiCN9TdrXUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Oh-n3onhmDIXjnQ3_BSqtwN1qXCRZ3A0IE52bEQ8zIUlXvpyMAd-Vlc0RUOmeuQcwS4_6SmQRnjqZgUFiSQP9CxrgvZ3YOGFmEduaqDg9aRLwAsa0ZBdLsbJrw9v4r_-7fjiyBEErsn47E0e3cO8xt_Yik6NGdr80uzH9rrkietDdSBEcDTzWXRZbfj1iqWvn8EExOgF1k3kDQCDH-_d8FLaxg7gUEM90H-usjzdJtwjRWUSHzN21ZriOxZtLXj2moE773o8S6NgOQAZZKFAwBboLlUYp1S7hVNMNjY7WNf0NSBr2ff_Dx15GsU-5n_10hDskcq68hm0Tx6-GYgjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Oh-n3onhmDIXjnQ3_BSqtwN1qXCRZ3A0IE52bEQ8zIUlXvpyMAd-Vlc0RUOmeuQcwS4_6SmQRnjqZgUFiSQP9CxrgvZ3YOGFmEduaqDg9aRLwAsa0ZBdLsbJrw9v4r_-7fjiyBEErsn47E0e3cO8xt_Yik6NGdr80uzH9rrkietDdSBEcDTzWXRZbfj1iqWvn8EExOgF1k3kDQCDH-_d8FLaxg7gUEM90H-usjzdJtwjRWUSHzN21ZriOxZtLXj2moE773o8S6NgOQAZZKFAwBboLlUYp1S7hVNMNjY7WNf0NSBr2ff_Dx15GsU-5n_10hDskcq68hm0Tx6-GYgjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Tv6fwBEzxPG5kNMQ5gNS3ZGetJD71HTqvgB5SZ2SmW-DGL9BUD2fgw_RpOWccfatKKTgzdfQeYBE7fpOs_7xCIA_hUDVYivz_vuxWKjuLPbFwFMO8iQKP7wAJ2Ji_lR6HTAfyWwOyH8vjF9NmyfRc-yudX9_NC6qFgz548CogySNwDbGCsxiciMyST9aIxUyLZvRQ1HdnCxpQwmDnQGl53ctX2smJEpN3FN6FWGAgjv3FeSfZhDKq8khjXA_vk4SvXdwmQom-eRPVzwyWR1XdnygS1FNahz-EWOl39E4z9IB1OuRbXn89m1yd3bawXNZ-h8DqbLLbzNxeOLhXgWCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Tv6fwBEzxPG5kNMQ5gNS3ZGetJD71HTqvgB5SZ2SmW-DGL9BUD2fgw_RpOWccfatKKTgzdfQeYBE7fpOs_7xCIA_hUDVYivz_vuxWKjuLPbFwFMO8iQKP7wAJ2Ji_lR6HTAfyWwOyH8vjF9NmyfRc-yudX9_NC6qFgz548CogySNwDbGCsxiciMyST9aIxUyLZvRQ1HdnCxpQwmDnQGl53ctX2smJEpN3FN6FWGAgjv3FeSfZhDKq8khjXA_vk4SvXdwmQom-eRPVzwyWR1XdnygS1FNahz-EWOl39E4z9IB1OuRbXn89m1yd3bawXNZ-h8DqbLLbzNxeOLhXgWCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=m7_UkV5ATY4uheoRrSsp0J9XchjiMU1JRAONKEqrgIRfPw4DbdbHZCGBPcCPQFjknOCPCKnlExFoNdK6CLIqPJzAHGJrQeNu7MnDeKgYzZFAP_IjSt_jUwNStvhi_SvX3wxO1OdvktaB2MZdQqQczwZBMshzafMwvrZbDc1yZPSxKPQCYCMh_ZtnnHTkEicAkGR3XZqwuFcxgceJDyP17cXwP_NkdyiF4oy7lc7bZT6Z43cjdbR3yuzm1JbBIV-XA5KUV7sLALTqVKQv--dkT1mlaPojnA-reptzgjA5QcKSpJDudV9VJENZpZrf95vt5EXjCgV_p4S8n919qX7lTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=m7_UkV5ATY4uheoRrSsp0J9XchjiMU1JRAONKEqrgIRfPw4DbdbHZCGBPcCPQFjknOCPCKnlExFoNdK6CLIqPJzAHGJrQeNu7MnDeKgYzZFAP_IjSt_jUwNStvhi_SvX3wxO1OdvktaB2MZdQqQczwZBMshzafMwvrZbDc1yZPSxKPQCYCMh_ZtnnHTkEicAkGR3XZqwuFcxgceJDyP17cXwP_NkdyiF4oy7lc7bZT6Z43cjdbR3yuzm1JbBIV-XA5KUV7sLALTqVKQv--dkT1mlaPojnA-reptzgjA5QcKSpJDudV9VJENZpZrf95vt5EXjCgV_p4S8n919qX7lTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KP2waT-tNlRjZGh4jAG7AJUClsNVJxorRhM5dyU0xAtHGB6fDTy4uiSo6fk7nuaY0TUIKN0aC1WyE-b74xymn3AgqBaGkygJ7bH3q3X881rj1VTdNybaH8XG-0MHnFiac3ujJ28H_hRVcmWbjWj5dmfuGC0KWA6EGum_eerkyRQkCcsPRWglSdcJUTM9EZnswu9Vcn4SYI_XmQRmiswQIchgGUtZgrM4MIY3pHfPtC2rOdiTO-ViYlSmvcWKgwCv3WJtIGgLaG4bMtbhgKcTYROS7Y4gll_h_iIK5hRshxwI7Qe5Y2ZDUKo1Pyn6bY0Ejn0ksMGLHG-pKI6fqWbrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KP2waT-tNlRjZGh4jAG7AJUClsNVJxorRhM5dyU0xAtHGB6fDTy4uiSo6fk7nuaY0TUIKN0aC1WyE-b74xymn3AgqBaGkygJ7bH3q3X881rj1VTdNybaH8XG-0MHnFiac3ujJ28H_hRVcmWbjWj5dmfuGC0KWA6EGum_eerkyRQkCcsPRWglSdcJUTM9EZnswu9Vcn4SYI_XmQRmiswQIchgGUtZgrM4MIY3pHfPtC2rOdiTO-ViYlSmvcWKgwCv3WJtIGgLaG4bMtbhgKcTYROS7Y4gll_h_iIK5hRshxwI7Qe5Y2ZDUKo1Pyn6bY0Ejn0ksMGLHG-pKI6fqWbrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=nidr1BRm1lJXDF0q-WKCUeI4ALJlZEtVZTQtewSoLdknjEvXo6O_7XUb4Z5JYVf0wC6YjGlx5-J-51PyEG-P_f8qj-RAdEQa4XQXuL5t7J4z7qi4FBOwS0c5l3_onlACKJ9rocs8NxJsXEuk2v8G1SF7nN6riFuz5UbS-rmF0quGrfHA0icHjuspt2hRYwzGs8kDlTW5kVIxZwdu4v1sPkMJ97yW08mI18z0LquMYaQjtPDc0Y0c5BEKsVJnd04IDfZN7XffMhDrnlyMO1fnlc028pOjHTn3wPci2Wis26oY1JcCn_SprCSR9bQqFITKIrCpMMJaby8GchTVO_WPKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=nidr1BRm1lJXDF0q-WKCUeI4ALJlZEtVZTQtewSoLdknjEvXo6O_7XUb4Z5JYVf0wC6YjGlx5-J-51PyEG-P_f8qj-RAdEQa4XQXuL5t7J4z7qi4FBOwS0c5l3_onlACKJ9rocs8NxJsXEuk2v8G1SF7nN6riFuz5UbS-rmF0quGrfHA0icHjuspt2hRYwzGs8kDlTW5kVIxZwdu4v1sPkMJ97yW08mI18z0LquMYaQjtPDc0Y0c5BEKsVJnd04IDfZN7XffMhDrnlyMO1fnlc028pOjHTn3wPci2Wis26oY1JcCn_SprCSR9bQqFITKIrCpMMJaby8GchTVO_WPKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NwgMWpJBYJt1yfSw0r_fJGw2eGzpOhAS9Yoh3s_TOMyJKPQfkd2Gu2Mjiego-dJI8krQsT8IKKjpJj8auarwi-XgdFK3vecTe5X1GIiFndJu9-kM3lH_Ti5_FPnkKL0FrERwu2F91uuvjIos0KmSfGf-WAhHzwfz4_c6uTlrGngftiaVCjz6UkgI4HgBnTlU6GO2miyCLSrWpc8qXkOZYojG5w9N4ZsrZpc_CE8pcKLEp9IIc64k7U0t2RS4-YQavguc8K1bk8QvibeFSirlxVqaal1PdTYU2KhkAOcJbQLpVv81anBoI_g2JdMGF1EseIgDjTBUpe4kCqDQjcDBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NwgMWpJBYJt1yfSw0r_fJGw2eGzpOhAS9Yoh3s_TOMyJKPQfkd2Gu2Mjiego-dJI8krQsT8IKKjpJj8auarwi-XgdFK3vecTe5X1GIiFndJu9-kM3lH_Ti5_FPnkKL0FrERwu2F91uuvjIos0KmSfGf-WAhHzwfz4_c6uTlrGngftiaVCjz6UkgI4HgBnTlU6GO2miyCLSrWpc8qXkOZYojG5w9N4ZsrZpc_CE8pcKLEp9IIc64k7U0t2RS4-YQavguc8K1bk8QvibeFSirlxVqaal1PdTYU2KhkAOcJbQLpVv81anBoI_g2JdMGF1EseIgDjTBUpe4kCqDQjcDBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fuDmV2C0ch4RWX_iqzk-cgBUUD5UYaII9h4gvZwBt_5fkxhnUA0biKS7YA_N7y9FB6O3qJjJNEUogE4m0biSC2XE7qDnetWovVEuu6Z7R8DQls0xsz7HRuW-6fr9rhUT1v6Lr9BXQzbOiGjZg7-iNEQcGp00DMZTOpsDaWMYPQe-Y_Lc_v6HkbQmkr-BIPfi7U3uwYQn4izF6HDsETk5t2OVC_qkc6VhFFBF_EN7yru7YW6j5ZHjIx_8cnjfFf9JZ5Yr8gUoqeLyGBr_xvNJApd2B6AYkaIpiAAoqEHe-p1f373RrRd_IZ67XdTtKztGoPwsCSLvd7-wQfiuS3omtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fuDmV2C0ch4RWX_iqzk-cgBUUD5UYaII9h4gvZwBt_5fkxhnUA0biKS7YA_N7y9FB6O3qJjJNEUogE4m0biSC2XE7qDnetWovVEuu6Z7R8DQls0xsz7HRuW-6fr9rhUT1v6Lr9BXQzbOiGjZg7-iNEQcGp00DMZTOpsDaWMYPQe-Y_Lc_v6HkbQmkr-BIPfi7U3uwYQn4izF6HDsETk5t2OVC_qkc6VhFFBF_EN7yru7YW6j5ZHjIx_8cnjfFf9JZ5Yr8gUoqeLyGBr_xvNJApd2B6AYkaIpiAAoqEHe-p1f373RrRd_IZ67XdTtKztGoPwsCSLvd7-wQfiuS3omtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3HGQontMUMlkdrPxn6gmsIhUoAivrT1tdYJ0TBO3L6qezFQpldC4CNnSR45pB9LZ1aenuIYFzchL02vcwKKE3L-jf31-gJkOrrW4WD285CO1k6Af7gOjNk2WtEv8bRnzJ26o6CZO0BHl51yyicLNnUVXy8pctgfK6asCgMZNUDJPWR2nyz4RRtQaHNc5N5eEm5CHS450-lynTdUg66eTUnhTI1CYWfLVYDQTcVDYM7pcurGLTax3hlRKv1YNQQy6CvhWzsFvHGIoEN8qUFEZnbBbCVUI0SbsUfmzCHF3F5NPHRTuG1cQHByT7Qok080_X6cmyrIkfbOTIUWs2xfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dg3XyPGhzPfGZZSysnarlDS1Q7g2XBkWt2yC5h-gSs5UlcnqkRG0EKI2Oy1kffW3-i6CAZyYcp06t_d6EU1Jr_nYseYYOCfE-_FSfmRg0D-Z7FDqIvR6WIKKTN39LRZbTFGA3zC5QPJ8EUNP_7AHPYEjvLeZUFOf4SRkYITaXBgKe33mDFEtTBlr1QriHj2ThbFH9QgI8LheYF8G2AN8YYA-UvATNqBCuiwWC35N7bS9Q4FgG3_zcA-b9UDlaJ31BFw9ap3TrokWtrvGv0P6xWQfh5vrbwO-DkAmSLhuzUo1kqquS4eJ7aHAGEZRjO7TxKh0jsdlUPFY6FGYQtFGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dg3XyPGhzPfGZZSysnarlDS1Q7g2XBkWt2yC5h-gSs5UlcnqkRG0EKI2Oy1kffW3-i6CAZyYcp06t_d6EU1Jr_nYseYYOCfE-_FSfmRg0D-Z7FDqIvR6WIKKTN39LRZbTFGA3zC5QPJ8EUNP_7AHPYEjvLeZUFOf4SRkYITaXBgKe33mDFEtTBlr1QriHj2ThbFH9QgI8LheYF8G2AN8YYA-UvATNqBCuiwWC35N7bS9Q4FgG3_zcA-b9UDlaJ31BFw9ap3TrokWtrvGv0P6xWQfh5vrbwO-DkAmSLhuzUo1kqquS4eJ7aHAGEZRjO7TxKh0jsdlUPFY6FGYQtFGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=MfwJpxn5cja7SSr24E0cYnzq-MVhBS4Yc6M1N47zDHSnUIcE5cxzh2c1XAUagurb6RnD2-wEUx6nj4P63748321IRf8k8KxQlyimHjnjxk-zcps9zHMpTdPLrv6UFfJblABgwm5pfJj0waawxx-d_Vk3XaIJ3Z1688_ihklhWS4e3w3MrZkPNFS9hFdbB_mIvSHQ2dvjrXvWiWY7mW4h7tzCUM4FIhXUyehPpiqJX7w7H2MA8HSe5fodrBvb8stxQFEVi82SOD1yX7XmcHdvL6XiWW4XwpDxLi6AP1oiYgBGI3fX1hrnz1ZIdmRvtazT8pgvuR8W9hGztdiDjnATbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=MfwJpxn5cja7SSr24E0cYnzq-MVhBS4Yc6M1N47zDHSnUIcE5cxzh2c1XAUagurb6RnD2-wEUx6nj4P63748321IRf8k8KxQlyimHjnjxk-zcps9zHMpTdPLrv6UFfJblABgwm5pfJj0waawxx-d_Vk3XaIJ3Z1688_ihklhWS4e3w3MrZkPNFS9hFdbB_mIvSHQ2dvjrXvWiWY7mW4h7tzCUM4FIhXUyehPpiqJX7w7H2MA8HSe5fodrBvb8stxQFEVi82SOD1yX7XmcHdvL6XiWW4XwpDxLi6AP1oiYgBGI3fX1hrnz1ZIdmRvtazT8pgvuR8W9hGztdiDjnATbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=B31ha7FPEaLnJsbrqf1rxrYZK8EgrTzCffAbA1AktVy97fKmKCCpGd5nYoP8Yp7xYIWlf7wakGhTU9oDcu-ffrAyHR8eemHJWcTx3FktNgOZFgflu8pYkVilVRQRDnrzxN9lYAyEKi9ve5yabKBMVv1vlCs56z4HRF8IdJiTCsYddRofkm3cnvLoOtk7MUDwNcssnwTvnKFd4A2MQ6RdUG-svZqAoZxb7Q01J3I8s7F1XD-QoxIBMTsGqnDR4xbWneVWv-MA2Dr4iyDNfR7xjicKtiYWU0ui_YcB2BLn-5d-FyAcu1mp0VK5txnOh3dUaGU0NsFKveHow31ui2VeNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=B31ha7FPEaLnJsbrqf1rxrYZK8EgrTzCffAbA1AktVy97fKmKCCpGd5nYoP8Yp7xYIWlf7wakGhTU9oDcu-ffrAyHR8eemHJWcTx3FktNgOZFgflu8pYkVilVRQRDnrzxN9lYAyEKi9ve5yabKBMVv1vlCs56z4HRF8IdJiTCsYddRofkm3cnvLoOtk7MUDwNcssnwTvnKFd4A2MQ6RdUG-svZqAoZxb7Q01J3I8s7F1XD-QoxIBMTsGqnDR4xbWneVWv-MA2Dr4iyDNfR7xjicKtiYWU0ui_YcB2BLn-5d-FyAcu1mp0VK5txnOh3dUaGU0NsFKveHow31ui2VeNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=o2uqjxLQZ21GJzMdwnzVzN8sHHaAn1UvrDrXF_RCOMLBUNq-OZtgoxOh1qawUG2GRZeHzfii7MkXXGMfqO25KXGOxOwU16HWIAV4fAYf35uXZK949lpyCdaSY7O15_MQ5bJnfeWarBeN5_jte9Oxhan5qNZeAmVTTRFEl3TvaRuzTrC07m-FbErDYWpWojkHb6SP5PM6VL3bC_QDI-FnxgTGaRpknpYm33wx7LnJCJiawVqvlDYwYJojjxmMINvrffbfBhKcMiwr4ecLxEgD6m2ZKFLHWVea6spk6efoihrE5qUcWY363_ddN1XsZmLDY0GzAzvuCp1_-dgyMO6vJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=o2uqjxLQZ21GJzMdwnzVzN8sHHaAn1UvrDrXF_RCOMLBUNq-OZtgoxOh1qawUG2GRZeHzfii7MkXXGMfqO25KXGOxOwU16HWIAV4fAYf35uXZK949lpyCdaSY7O15_MQ5bJnfeWarBeN5_jte9Oxhan5qNZeAmVTTRFEl3TvaRuzTrC07m-FbErDYWpWojkHb6SP5PM6VL3bC_QDI-FnxgTGaRpknpYm33wx7LnJCJiawVqvlDYwYJojjxmMINvrffbfBhKcMiwr4ecLxEgD6m2ZKFLHWVea6spk6efoihrE5qUcWY363_ddN1XsZmLDY0GzAzvuCp1_-dgyMO6vJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJQNFxEQQAY35s-8__EfnwNzXPw-9tkSTOrC5EGUSO7bVvATOcoL1YZyIriIqjpTkpzyuCLaIqL05XH5K8BdmlcbWvymJ2S8VtwlzNEMX97XA0Kyw-TsDYNe5MCf0knGef3suU6HSynyCzkhFwjBWItG91KSzCDEUYCOzUtrJBo4rPC99HoDI4NxORkcWPVvKCinlBfFZYUQG30EG4UFE6eqGjKOUzIU18-BxFBkMZqB2I-Lb1GGuH_5y-B-YDaO3upefK1Q2e3BlEI2UtoPuTCbX-NWZIQJlh8AnK-6eZiGPqsnORHC29i8oU-ZiCyGYVgj4ymAwgVhbPrIFnvYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=EdanpYgbUv7i6MQXPXax-0pcNAU8Do7Bo86SjRto39jYWbnNokAlSGVoz_tPcjuQZwVXTJwHsKgU1Xij5qFzP8MWtYklAadFuhGXDk4tE1tKxLfHgOihDFrEJ7gLsbfhxal4dgSBcyxCvpNNmTq8qN76ELcINrw3jiZPkRGGybdT4u_7tdVLd4cHC3mQWrtV-PwlQqsMR-NhTQH_1YCj-oQfZ7HvmpyM-6nYplUmDlg5KAGkF3ppUafuSVKmwUtJLqyaYBeUM0qOt6A92euLq0Fosr_QKz9u6P2rlVRYBxEF87yPKYhk9kNuY3B_khkQNbsP7BoXDhrS8JVbPS_QNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=EdanpYgbUv7i6MQXPXax-0pcNAU8Do7Bo86SjRto39jYWbnNokAlSGVoz_tPcjuQZwVXTJwHsKgU1Xij5qFzP8MWtYklAadFuhGXDk4tE1tKxLfHgOihDFrEJ7gLsbfhxal4dgSBcyxCvpNNmTq8qN76ELcINrw3jiZPkRGGybdT4u_7tdVLd4cHC3mQWrtV-PwlQqsMR-NhTQH_1YCj-oQfZ7HvmpyM-6nYplUmDlg5KAGkF3ppUafuSVKmwUtJLqyaYBeUM0qOt6A92euLq0Fosr_QKz9u6P2rlVRYBxEF87yPKYhk9kNuY3B_khkQNbsP7BoXDhrS8JVbPS_QNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aKPaetRUfxyKJRZHzUmg7dji1u0JFRxjTXsB3lc7sJRgpARCV_beswt_v87_mP2MI906s76yEjhfJELtLLLL65ebVKimw2Dj2k-dF3hxGA89TSY_m9WGraWyoNPpbysr-BfcIEc2Z2xLdoJlUKDa5njn0-yOpK6jeK2YWNx3W3s1iGec059eS0FTvNocesl-mrivfKcuuiQJlMSv1mRQaa-jmcMxbxOwgkdcaF_Co6T9dP7PE_J49M10UR66CezUlTejPi4XhgY-sTu5gYleTX6M9A9RAbx_mCpHLp9Enj1mjrn5vwmBpCQsb5GxYH5kj440jiMwGCg8ax_5dvK5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aKPaetRUfxyKJRZHzUmg7dji1u0JFRxjTXsB3lc7sJRgpARCV_beswt_v87_mP2MI906s76yEjhfJELtLLLL65ebVKimw2Dj2k-dF3hxGA89TSY_m9WGraWyoNPpbysr-BfcIEc2Z2xLdoJlUKDa5njn0-yOpK6jeK2YWNx3W3s1iGec059eS0FTvNocesl-mrivfKcuuiQJlMSv1mRQaa-jmcMxbxOwgkdcaF_Co6T9dP7PE_J49M10UR66CezUlTejPi4XhgY-sTu5gYleTX6M9A9RAbx_mCpHLp9Enj1mjrn5vwmBpCQsb5GxYH5kj440jiMwGCg8ax_5dvK5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOb2wXUJTiKub6H8xPe6I2bslUbLcHtEmpkUxBIaqpgTktHleoZJaLsV7CY6zb4cPw6Wj0x0q-6awQJrUK-RxI1g4yB2dZ4Yj1FHHh5Kx3GwBIRyJCLJjjK7NrHFpWbT3RbYZ50GT35zThT8r6ovVnUqvguBsZl7ULsmo4SwCXrzOv4w6oo_LXyxa9EShYX5Z_JvJRlPD3emhm0qnQDGmTjrqQVlSbamHRt_Y3NKdJDft0BU83AyGfkriwiIEIoy9nsfiBPXq7G3z7GfYBhTYmltxz-0RUvbEVuM_B_aPylrFDPP2ehhIf_8s09ncXH7c1-IxUuM8Ovb-K5_oTT2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIAVfVVRf-HJGNdMu5H-eWLAsAu2kLNloG17kV-C-D14X6lG4ZjCscFzZ2UjG2yT9VKXKAfwZED3HLePG0eSQLQNeKCVQz52E3bxBhOiGbPKnHP84YAJlniX82RqP9NGt8S3FnTEQXN4DYtctGJlBMTKoFX7EvvIdEMnqwZfaF_5-4186lbq4Gfb0OFy_umRqMTNCgV_yJjxKaScsrl8B5wSeoWFsPwuaQzU8NK9gBkzXtvl7S5hxku_nt_iTAuER89ARUnM34PkhSDv_z1sVF13pdnxsypBMboF_PXWLKoWe0RF9eErGbovld9bZPFBjbS9TU4XA6PHAz6glDdKgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=t8IdIR7DUag_N3gYlg1xN6znpwJSNIZ58KdwsDfLzWENmcIs2jFNuuvdh6c5FZqUi2-D6LjwaOqkGVTIgYPFxRLzFs3cIr1BRT5NwZTcZrPYXS84dd6jH4mPtrGP07mKUC3jMix47HtnS6qt-yOgM3aPvnOpyNYnNxFgFBK5yR7sIHoXaEb5YOYZyZBXcV5mBoU1p5Yh-96RxAFSpMyHIVE2KXWV-w4X3ylite2MQnjU-VX05cV2BxdZAEvNydRzkCF_g4C0WC3OpWW-kMaLy3ghmkA5qzLgzDNRGq7PQe492rMJN1PoLA3SSLA-PXu9gpGKl9JzMMKIcFFKizjj7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=t8IdIR7DUag_N3gYlg1xN6znpwJSNIZ58KdwsDfLzWENmcIs2jFNuuvdh6c5FZqUi2-D6LjwaOqkGVTIgYPFxRLzFs3cIr1BRT5NwZTcZrPYXS84dd6jH4mPtrGP07mKUC3jMix47HtnS6qt-yOgM3aPvnOpyNYnNxFgFBK5yR7sIHoXaEb5YOYZyZBXcV5mBoU1p5Yh-96RxAFSpMyHIVE2KXWV-w4X3ylite2MQnjU-VX05cV2BxdZAEvNydRzkCF_g4C0WC3OpWW-kMaLy3ghmkA5qzLgzDNRGq7PQe492rMJN1PoLA3SSLA-PXu9gpGKl9JzMMKIcFFKizjj7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyoS7NxBgbIvrWglkD6YbU9kv9udW4mR5SqN2vBx-9A-SZA6lEbsk4buKtJc4BR9eMS2-MJV9jjs396Nod9E_2-srjdD8mNBd2wLAoMqx6ftZPalcP1XCFfbOrQtNbD5xRJvStv6FvTJRmtlus9-9I-yDnvk6Jyall3vwGwnO4OxglILzNcg9YhtD_DJf0AlUINr9In4aCEIxsErLMxiJhgot6VJcgmbx3mVLAzxGycIDmBEO3W6U05XAm7BOcUMOw-LQUTLXNkUuYOzJbDMPD3W9p4s3BDwyiSfoGTJ7PtJM8pWrzGfoL4-UkO6bbiQIXt1UamDWvG-AB0p82KL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4lMV6mQcFAvUi7vvSTIxUZMOJqXryvNisnN5nDOA28SntaVpIgLvNMFkKWVF-nNOZ3VHKWz1mNUH-n297HbgJciRpLOyOW19PpecHAkq8aV6sjZpsdoD9AEdSphQg6aVvuwpGWlODu17Z3fg1uwfm94UjrHeZHmn9K4Fy1ETo_pRYfuHNIDKbmAYJXbHBuYO50WJ11mMaViynNVPgbDqdRK3zVgc8LQGGR8g7I7fvIEkqr1GwKGUI2RbvaFStqYGLzy0naJhHuXgqp4TQjhTSmsBmNkHPJDw0saUHAWfKDFR_gtu3cBSAwbjljkCAQkOZ7I62B2E2BINTBr7MPHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUBv5dlgC3hpTOgujt-grq_eaW6N28e-ntjLTN9fMLdjT1czAPKx_kJPHeTxdqSvNyOqbl-4nHV74qD0f24NB9RL6vc1hDJnJwe093bx0qq0Es-nqk67Qo2L5SeoE7xb2aGzIA7X7QBsjzByFzVvs9CF4cCl6zVipPS1yqngM9ixesB3zDJdka9hojHn5iBj0rShChA58IvP74LBn5RPaSSbh5WKHG_L6dKcHpqTR-pNdRkzLriYxmpJxJREonZAeCHTv4mLKkUIwKnbUxK4ilSi5bOAcUTVio1eZmf8iN5adACRgCqM5y76bVyTo98Jtc7w8ucQf04VOYQXLYjJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kx7iyuHqPWlX46cgksVMkfMDMgWjgfxEhCo1iacFopxJlMORbXmyD88dk81dIP1cqbxHf4BvRqLJNOKC1yvwzk4F5PVcTEMW9nwzGcfifeyLE2B636UHjM0RQgLbR-yQweOsSVjM_JabsFF4-pdQrnGXRez7EbJuGEpu6gSUm3-xGAx35xC555e-UJgBwhSVbpeRfC6byr7swKQU2et3oux7cd1_sZ6I0ly_VA8giRfYfv6R71rh03z8DmI9X0ROYGoS8zLm5iPFzFQJw__NAwmOZ6NcC92cucFzeZUeQlb6qg820yMGi9PPwjM6i9hUjEm-PFKNLzhjFyWh3QR47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kx7iyuHqPWlX46cgksVMkfMDMgWjgfxEhCo1iacFopxJlMORbXmyD88dk81dIP1cqbxHf4BvRqLJNOKC1yvwzk4F5PVcTEMW9nwzGcfifeyLE2B636UHjM0RQgLbR-yQweOsSVjM_JabsFF4-pdQrnGXRez7EbJuGEpu6gSUm3-xGAx35xC555e-UJgBwhSVbpeRfC6byr7swKQU2et3oux7cd1_sZ6I0ly_VA8giRfYfv6R71rh03z8DmI9X0ROYGoS8zLm5iPFzFQJw__NAwmOZ6NcC92cucFzeZUeQlb6qg820yMGi9PPwjM6i9hUjEm-PFKNLzhjFyWh3QR47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sKUi797kcceJOz2SwmbpPJga9BTd-4ZDRL8QJIOhL-gdzeb818WdMHJUB0S8aD9PP03TySHDr4soTgPL_GG1cfd_Xxk_cIODHa_xPgLQ22aWpFaFBxPQsb3FtYUnPb18G6OXt-mxANXmlTEu_VsC9VqjmObA9MutLBaL3P8ENV8clL5hWf2d_8RJjQCm3cPYXFVJ2ifSp2DyVjltOJ_JFd_79ma_5_UFUWOMb3R-vtaIa4mYGBeMRm99K8R_HAAPgwt3jjRYbgqlBHMK-6KfTeBKWlb5po-tTzuBkUHDfycFDpYLxn7fP_3dwxVBK9ovqPrnyb4dt0JEU7ML2L8i8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sKUi797kcceJOz2SwmbpPJga9BTd-4ZDRL8QJIOhL-gdzeb818WdMHJUB0S8aD9PP03TySHDr4soTgPL_GG1cfd_Xxk_cIODHa_xPgLQ22aWpFaFBxPQsb3FtYUnPb18G6OXt-mxANXmlTEu_VsC9VqjmObA9MutLBaL3P8ENV8clL5hWf2d_8RJjQCm3cPYXFVJ2ifSp2DyVjltOJ_JFd_79ma_5_UFUWOMb3R-vtaIa4mYGBeMRm99K8R_HAAPgwt3jjRYbgqlBHMK-6KfTeBKWlb5po-tTzuBkUHDfycFDpYLxn7fP_3dwxVBK9ovqPrnyb4dt0JEU7ML2L8i8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=k0RG299q9-WwIY8-kJV0--CxpxB5uE029h_PGcsvv1dGH_7kLzpGFUWf2hwoexth0R6PbEDkEEEgs9Ai2Ln0proMjXGSfZBUZwan4jQBGC4hHHE7Pp2gbnHeRZezrIKUoyKayIrOZVBUC9lwdsy-bpzjY4ebRfqQnV9FbtKieG2QHIOOMg-ME4CX-uCdiKy1IchQ0D8E9Q4tFz5SnYHTcDP5Ywc0qzgSvi8zhuZ_3FXE5zCidoTdJ_8NhNJH9rLbbItdIhpKDrKTD73IJ_e1f0631UhMjGJ24xSXCtLSsnKYxVuEEndF8HmsTxWuaAYOjNl5ucaUmV1SPEXmQfyC5w8_0dsxFoeUAIO8qZZ1Sqi8Cqmi8b8t6o7gzFZjPL6qHZgxyKess_TMhApVpAub2U0bnMtLaPPEVvxsB4UjandOjNkDZc0Y6EnZpES0ne8gM_JqAbJ9v4g4iItSfjC4zDw6wuuZ1iffBqOAw_fOlv4Kscv4OAtguYE4ew_b3M1gZFRmLEotZX7vn-hQIB92INrqrNS3ZuoMn6Vl4Y0SSBHbTUbdlze_szJ0ze03o45_5KQB9dDRHkEhbpDTrIl9u4w8AUnRMrPuQ7IrxCUZIOnxHD_SAbZiaAN8v-Hr-9DKCw6h88mMnNWGiuU9FABF1S4G8q7umztbzxaQVZqEyog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=k0RG299q9-WwIY8-kJV0--CxpxB5uE029h_PGcsvv1dGH_7kLzpGFUWf2hwoexth0R6PbEDkEEEgs9Ai2Ln0proMjXGSfZBUZwan4jQBGC4hHHE7Pp2gbnHeRZezrIKUoyKayIrOZVBUC9lwdsy-bpzjY4ebRfqQnV9FbtKieG2QHIOOMg-ME4CX-uCdiKy1IchQ0D8E9Q4tFz5SnYHTcDP5Ywc0qzgSvi8zhuZ_3FXE5zCidoTdJ_8NhNJH9rLbbItdIhpKDrKTD73IJ_e1f0631UhMjGJ24xSXCtLSsnKYxVuEEndF8HmsTxWuaAYOjNl5ucaUmV1SPEXmQfyC5w8_0dsxFoeUAIO8qZZ1Sqi8Cqmi8b8t6o7gzFZjPL6qHZgxyKess_TMhApVpAub2U0bnMtLaPPEVvxsB4UjandOjNkDZc0Y6EnZpES0ne8gM_JqAbJ9v4g4iItSfjC4zDw6wuuZ1iffBqOAw_fOlv4Kscv4OAtguYE4ew_b3M1gZFRmLEotZX7vn-hQIB92INrqrNS3ZuoMn6Vl4Y0SSBHbTUbdlze_szJ0ze03o45_5KQB9dDRHkEhbpDTrIl9u4w8AUnRMrPuQ7IrxCUZIOnxHD_SAbZiaAN8v-Hr-9DKCw6h88mMnNWGiuU9FABF1S4G8q7umztbzxaQVZqEyog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=BnojNEEkfzgBB8vqCdQYtc157viLpKNTyMuY94dlRV8PyznGrYV1UJgpzkGvmIHOXhk17VLNsVF2ma-F1HXFmecgkHF7A-70aM6epCFUHBe7_bRG3-7XLHETswkaxdVpzE85SymdYHMf88MoANzGkoEEsVf88FUa0OdJU6SZklFj9X8cyEqG340sZCPfKw0fFHTw7PEKFnTwEUMf9vOzMTvo5BwOXEuHYurPFOaVSOBG1hfioubpiYrnHPgYmysjv1CgAU9PeMy6fk7eZz9PBtI3vFUF5tweGVtjtY4npZZCOR7FsOx9uqqKjJng6womZfGKNA9c3lV4RjNAlC9uswBn2XLRyoVMbRBSY__y0H9i5nlVnbtvYslPjVYGdGRYOYKXF2rRyfpl5W7y7rfTsqufAUz5Qrm2YRK7zhdXgTK9te-jLsU1hZTiLfFkQ9c_rfPczDPHbHT41aMi7XzKnNDU-8WgVe21wsO8c78LflLpTEVqvLGLZnbzNZXuoAi-PwWsVeKNi_44ewCzFmomoiWOH3Kdqj93fytN8vZ1BGrHXhqA7_cQkpyT_SsMotC-q6l6idpAj4u0iTOjW6ll0emR3bk_xpz-_HJA48x3bFV_9UjherdcNUkIDuEUu6wMvKm2hbapPFvt12ZbzVgisqGvaM971S-8pPkyJGWlhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=BnojNEEkfzgBB8vqCdQYtc157viLpKNTyMuY94dlRV8PyznGrYV1UJgpzkGvmIHOXhk17VLNsVF2ma-F1HXFmecgkHF7A-70aM6epCFUHBe7_bRG3-7XLHETswkaxdVpzE85SymdYHMf88MoANzGkoEEsVf88FUa0OdJU6SZklFj9X8cyEqG340sZCPfKw0fFHTw7PEKFnTwEUMf9vOzMTvo5BwOXEuHYurPFOaVSOBG1hfioubpiYrnHPgYmysjv1CgAU9PeMy6fk7eZz9PBtI3vFUF5tweGVtjtY4npZZCOR7FsOx9uqqKjJng6womZfGKNA9c3lV4RjNAlC9uswBn2XLRyoVMbRBSY__y0H9i5nlVnbtvYslPjVYGdGRYOYKXF2rRyfpl5W7y7rfTsqufAUz5Qrm2YRK7zhdXgTK9te-jLsU1hZTiLfFkQ9c_rfPczDPHbHT41aMi7XzKnNDU-8WgVe21wsO8c78LflLpTEVqvLGLZnbzNZXuoAi-PwWsVeKNi_44ewCzFmomoiWOH3Kdqj93fytN8vZ1BGrHXhqA7_cQkpyT_SsMotC-q6l6idpAj4u0iTOjW6ll0emR3bk_xpz-_HJA48x3bFV_9UjherdcNUkIDuEUu6wMvKm2hbapPFvt12ZbzVgisqGvaM971S-8pPkyJGWlhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HCvGwYt6f7oHNXZq0DFPoRFDTwNYN0Nz7Xi58vUSg0QeWXIDlbrG0b2U80cJvAuW3PlyZ1vssLAnduMs-rVVfYYz6H_NF5FJ65x_CIfn9Iu-xI_eEMxa6Qcey_Nz-B_j4QLGQNceq07wXRSHD7bAfgaU2RffjAxnKno5KJPgEqCCBNzmArbVZERntIdcswI9ha3gP0VSzWFVoDjuFZfWFDR5hg-72lJ35Mfk6SFMi0IsePd2AeKAyr58aO8YRucVls1xnoUptMTee5BTAYDo5I_4KR55UuDBSK0RooJHhx_lbylTXEtUbTU1E1U3Lxl28ejdy5uHy9w7mbSzY5yDxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HCvGwYt6f7oHNXZq0DFPoRFDTwNYN0Nz7Xi58vUSg0QeWXIDlbrG0b2U80cJvAuW3PlyZ1vssLAnduMs-rVVfYYz6H_NF5FJ65x_CIfn9Iu-xI_eEMxa6Qcey_Nz-B_j4QLGQNceq07wXRSHD7bAfgaU2RffjAxnKno5KJPgEqCCBNzmArbVZERntIdcswI9ha3gP0VSzWFVoDjuFZfWFDR5hg-72lJ35Mfk6SFMi0IsePd2AeKAyr58aO8YRucVls1xnoUptMTee5BTAYDo5I_4KR55UuDBSK0RooJHhx_lbylTXEtUbTU1E1U3Lxl28ejdy5uHy9w7mbSzY5yDxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDlhoFKUtkuzXPWwWKbMN4cVBypgYICaigevrJxLkfHoMUUCRX76Jy0dB5yUB4wtEz-jp7mA_sK8cOLaEmUJn0CMKD0PEiaDDJnaLvdYVy5m2-6UC4XS98x_oj87WX3hHoRO1Ga1SqM0koiJqtcTVVffoSltJcjv-6AeY-Vaz03Pv5IPLb13PcfsV-3OqKW_kdJAwv15jakYH5op-oKimjqMFm_c8ENZ5uykGwqg7ZnFInH4qccbjRGHv5FHqXAnelPtagtoFnOtK5nY8ELxeLtQ1e8keFH_lPIogwsYUAIdMIFCAZZ0K2q7I-_N9E0VndkgvBpRE4X9US0M0zz_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Gli6bDKX3iA_Eh3bmAny42JA7-3q-wWCOWud7nZzJG9um0W380sz0aQ90P70G2Fs8BpK7IdoWMS8udt6AK9SFhAubE3Jw5uIZbykAAo8wdEL6aqzmO4l_q_UCQOVZoyT1rc60Bnfx1Lu1QELwOkdGG8ofWznMO_5_i7bYhjSshBooETuNMm-d6f47SgMSY-uMNPthlCmZRVTO7Xam1RkuVaGDTklW4jzIuiCxyFxQ94iEW-eSKLFtOPSx9ldhjPx_rZRexowRN_agA96HvfJUxGGIgMLcWDbey_EHN2FxadLBoc8Sv-joRGqZv4XY0bGURoDiqu4dLbVkpSxAY5iAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Gli6bDKX3iA_Eh3bmAny42JA7-3q-wWCOWud7nZzJG9um0W380sz0aQ90P70G2Fs8BpK7IdoWMS8udt6AK9SFhAubE3Jw5uIZbykAAo8wdEL6aqzmO4l_q_UCQOVZoyT1rc60Bnfx1Lu1QELwOkdGG8ofWznMO_5_i7bYhjSshBooETuNMm-d6f47SgMSY-uMNPthlCmZRVTO7Xam1RkuVaGDTklW4jzIuiCxyFxQ94iEW-eSKLFtOPSx9ldhjPx_rZRexowRN_agA96HvfJUxGGIgMLcWDbey_EHN2FxadLBoc8Sv-joRGqZv4XY0bGURoDiqu4dLbVkpSxAY5iAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=VVklUNcEb7teAGfoYGiC2p-_1AJ2Mzh3CI1y8dIU6WhnzhlWnLLYLXbFVCkxu6MeqXHGsVIZXKmHJJmPGWcKjHhkAgqNErc7JFNSsIZVsC1t6Mhu7Tug2DtOF5cPE8T2bupj4oZ2qmU0-ta6I8mwx64EajylEXToPoVflf9E-6yG1hNpimqGCNG0s2R326nPbqL9miZJ6GRmhZY-Gvaa7TmPdu5SjnyrNEY0FaSxkqp7iHyagx-sTG48YXrsxVnCdcvDAH0d7lFNkstbZduNlzh18jTPN-tRvPsgMruIfpYu-T8g1tICw04f1k8W9RZuadvZgTJZ3iFREMANApH3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=VVklUNcEb7teAGfoYGiC2p-_1AJ2Mzh3CI1y8dIU6WhnzhlWnLLYLXbFVCkxu6MeqXHGsVIZXKmHJJmPGWcKjHhkAgqNErc7JFNSsIZVsC1t6Mhu7Tug2DtOF5cPE8T2bupj4oZ2qmU0-ta6I8mwx64EajylEXToPoVflf9E-6yG1hNpimqGCNG0s2R326nPbqL9miZJ6GRmhZY-Gvaa7TmPdu5SjnyrNEY0FaSxkqp7iHyagx-sTG48YXrsxVnCdcvDAH0d7lFNkstbZduNlzh18jTPN-tRvPsgMruIfpYu-T8g1tICw04f1k8W9RZuadvZgTJZ3iFREMANApH3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZsquNdxQ_1zTjlSPXF_6bPueLAHBa2y-WEMnKURe92uoa3A-Q57Iu1c9GmJWuH3MR57C-uQQ6PCv2wtcmbx5HVxQhH2g1AfUXL6_2HLlrCr_w4XHS3QlwWgp-p-VBBkJ8xvI13aWLBXpAuzrRlPcNaOUPTkw7m8qLqsJERspKqAx0Q4JHdTKiHnP3g6zt8EwOm6S6jagPyTYDNzONDEKFB0lZojSJNRi6qwhUL0dwU9TE2ldOUvHbnoTJRQF1CgQ2f5ut3sVNG3n2mqvhXrJ2IPsbfxjeft7gQh9aBhu3NFM9dL_JfQ-C4WG324TJryVN4hAv-4oW6h2zRdHG_-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfLdkw1EMgL2lwmtdewxQJsPlpq_wGvrtLDo2UC9yF8e5q90eEh4LYuMb0M9IFak6bsr0hniNlD2A0HJ2Qxq627fJGTnzSCIWiBGbO_pLZNmy7ZLpHAhkDAHQbJl47E0wb_xnOLgoqreda3FHuiKA0U_MHKNuHWGaEyOIk1PjNNlmWmrmbL4Z1yL2ahCUuydLLU36D8n-Wfiub2768yHEEU1ir2zct29QP_Z4PjwufME4xdiD5QJUBCSOIgesPO-eErNBV3C2UHGjgI2-tngzIUTafwZ4rhJwSfdgSTy2Vb9-GxltR1bkZBwiwyqguELu8cZG3K5A72DQCfqgw909A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndWk_MiNRsbNT24dvqKHDMPrHNJAHehU4-KY5d-jrZ3-fnCPWOytHUqBUTzBLnsoAQRp3wIkpNLh1o2TnxHqoLvXI2lToyDbOwAGRsWBRVl6uH8_vkYNPhd9ChOpWfby75prbqUyZZkwAjssza72-VcZ--58pXw0MAz-QlEc3lBNEtbpqdEMOCGLCxsY6dxOhE3eSLe4L0w4Crxx9tsYwf6CJvocJSEGioEPbj3X_X51mSzMAnDffwTFT5zpZbANMk7laEJPea_FGqspkttR6b3VAXfvi8N24h9V814uCmWOhA124DucYxlVfEX2QWEYJZVyM6-oOSY9fBFKXC3Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSXu7NauTP8ibzUrLLqZsLAWZgMObcIc3GV4B8kDmDUQHHyCpNghibJ_4iWbiXSqOYVEZhKAb2NpnwO_U5pwFPxXSy71_MtR4eVI5J0ESenIot-ZqSwA6V1GcqskTmjTqHKzj6aTkjckO0BkK9kvjAHDLQtaMKhSSBhGQg0NWvxSzRKQB3Zdjcf_rW8Qmy8tran5JMCvYzzGBlTmGS5FDmCVznyp3N4VBIloMF6qMnp4LdRAjpOV5-iv3J5bkmsixYkQ-4mlwvDSSUI60a31Z1LicBUFL_yzpmRjdy9a6hXSgJDAJR91Jqtnh_yLOL6c7zS_m93JFirJnPDW6_NztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvcfUkSpCYWmg9dxr33Mjm61N-NWmJI0GCBBvrmljLAN33JrX1BtVkZHKlJJoF4g0M4dCUlSHYr1nx1vpyf2BTwz-JrIe-5YmN0tmuimmtfRohaAT47_YEQ7XAbiyGp1J7WYF3s4vP3VL1chv6Uuc9GWhKwXQWBxMEr53N7M3Ch0bOBoQmKggtr3itFXblM5B1-ni8aVbs8p0h_45WocJwaHeUwqn3v3zyKSqOizfkLDiFDuhBGCU9FbWkmxqBEV5KzPKFB8eYqwMP2AFYpujwcYm9SJfaHrTdydunFTNEgSD-b4GlPPJ3-3IJsiMJVydUaUIfHR2qV-h9SFtBcp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJWAUcTQWOJoUB2cHHQa0ZUnMkJDxFmGGjUtNqbYH47l-FgnsT5MukY2FKB-pnmDVx0xZasiCcRuwNVpJbVzBimoINm13kR69XSih8OFGNB9t1D8kD0Z5wbwpXhAR75HFY2eAsJnQ7tHYkJsyWCRpJZ18P5VwvuUmDcBt3PwzOuGz_zcncVSUaAW3gq8iK1ubKxjvj3pnxU_nkH01lA4BfZcxktF_HPfdtgsjSiWx2oPUtGHy9N9juI7m1AfhTovnP487myo8xxu1QaPnEIQPstxKvvab6GOgeTTyRKA14Zz3-lx0GD7R_osAgdTj9FLowOb_NOfaQeres0Iix0jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZuapNvESK53dHmyg6LOAmUwUOICdX5I4isA8l0cN1T1pBUPbIfQIdQpJj0hqag912OzCQ6a7hpUE5hwFN6I2iaJX6MbaVFHhWmdvcUQmXex3U3YZ9krBkKdBtM49pusFx7LV2CyOaD-8pH5W6Q0VayeujHGm3IiXv__iWm--XjM4TQKt9hwx0vcJYPXNYtB3bJKHvbRTw1UpPprFlLUaAjnOPIQklhLNXgNZkCWLalswR8cQX8pokHc8oPNfqfbDDZG3LbMnjAEOASZHtUXC6qRRZJxADZt6ae1IXF18iK9vRTVo7wnlzXHMUUrLLU3Tt7V1Itgt7cqyKZAF0Q7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOT9JN_jYqZOpUczUorDsffEIh2KK3evu4zxiJJ24xlmMZ9PxocKIWm3hYVnvFHLuzgZmtu_c5_Bco3qazj2-dJTqVQH_gLuOXTNThIDSmgD5Hez3adG3ko6UpR6XLQ3BiVxGX-_u2Jt9QwCFRN7o_l7TOTDLJwLljLPfmeXcENPX2GrHyqkyD6EUxJb2w3i5JiP1Esy1TR6BDjyCNGSP-vE7iDj2stbyvT2XAeY6EufAgIHf60phA62zVhqVWTS9JQYe6WKl1J8xx0tCToy9rOljrnJ4KaxzYb4hhn8-OlKJBHGrb15XIezLL9piVBC6Oj3bz6daO18LHgoDySMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbGEO1gxw5NamxRKa4CEtV3oSJVfG7Lt2iG8WiawDEQDlYn7Sx5kfNPCm21gx0ZDT3H8TcbDdXunsYBa8qYsPw6aZqbwYsg0IG739LSq0EjFXqr9O-cpaLyQ-E3wXbsPqmkQ3SXp7IsZ-mwgaX-gRF1rXkU94-UjDELAGm08piabK6k4XOXrpTzrUOHg75qwL26IsiRse2mN7qxiHBQJR0Bau6yz7ZFCUzPVk2qp6jTTVWRloPU5GGdvIwiKwo5hotlxglsawik78I7r7xxfh4FGaUSh7y692jOxY-mWkH_-Y8ErSZS_eQKNHMEs1DbNHhwS3ge6m6Fi3UZfecdQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZXiXFJUM0_TdASvkx3I_shs7N7pWvASbOOZpaDEx4csvTvxynvVUuMcceBm43Bt6Kh3KUGMWzNjehDIL8U-f0K6bNYMxWc6EoMuGJObll0PHlEPIlC_13WAoJjiGKnZuodfebZJadgU6MsJz5UqP1SMLMZMiUGZPZQuTdSM9Z8tRJRxcizB9FyRa1JRuPIcUkDb9PAZOr-mss0e7am6HMevuEnsVEvcdyUdT7brf_4UZ3F8MvG2y8gfO5U_AyrAHfjXPCXDmbfnBhz5bphm_7Yw2KuAD8V2EGqZP2EfqWY8OwY6-HJrEX10NW82C3RD0hLExo7rei25xzo_ffL5Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=jZU1xHpACaEhrU8nl24I7iVa0gAilufNxr4lazXuMlQ0Zm0CWTXw9RldIt9x7wFV7ld8WnIKrJa36pmradt-uxkL4c-QBDaUk-H49hRYsl9U14RIA_9GU9Rc_Su3hfnZWcjRXWqfPQiotRK-B-SsMFIHY8fnoCgsjrTEqaULNNo1SQgqI7_5a1W08pApqKQDJQ0SRgfaSj_OHZXtGmWZkYCPEKaoovGd9ThcmxaNMS62u7riyO61couQQuD-lRl1xgs5BF31I1-bj5d_QSLnxHZ9KkZacPMi9WLQI7XiJr_1-NTx9-0APHCBqrRpkiYMVXfUpVkW1JcuhXzYpRE8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=jZU1xHpACaEhrU8nl24I7iVa0gAilufNxr4lazXuMlQ0Zm0CWTXw9RldIt9x7wFV7ld8WnIKrJa36pmradt-uxkL4c-QBDaUk-H49hRYsl9U14RIA_9GU9Rc_Su3hfnZWcjRXWqfPQiotRK-B-SsMFIHY8fnoCgsjrTEqaULNNo1SQgqI7_5a1W08pApqKQDJQ0SRgfaSj_OHZXtGmWZkYCPEKaoovGd9ThcmxaNMS62u7riyO61couQQuD-lRl1xgs5BF31I1-bj5d_QSLnxHZ9KkZacPMi9WLQI7XiJr_1-NTx9-0APHCBqrRpkiYMVXfUpVkW1JcuhXzYpRE8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKFMl4dFIRhY3CYkR2KLc6p_jkfKQKEXS8AyRyT4a3z0y6XBEXNtvxQIABMKBiKxpcdN6j1ufC7csa9IjA49M2qn-uKaZ2sKAVN-pKAN-SboG7IKLt9eaERmEUR8KYSO_sgAgVn2BtYW6tkDFbUFQvv7W8AFN6QdD6p9QV-pKA3o6Nnq4drjSlwU3w0yXBOkuk9MufwPyDwv5ZY7XKGo52HSkDaKKEKcnb3J2BGfK8_M0KWumqeDJzVs5LvUWavhDIXwB-I7_Q-m7cjVccgbewnZFyjyJGZY8eQ_jCvvFouig1_e2twX3Yt0Npeyq08nrrMoyuR576qqowycb5K_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3AJQZckYYumLH1hIs4jZ4OLvneKYn4GPBbq_UdO70gpMO46RMHrmNlxwnGxb6z8DHIG4659HNZOpXoRJYfecmd8ZWlrUwvrS_ufBZYp6TvnZjIsFuU91Bh_b8A9_ZNo-zNSs9wZq57u6miyi7o_2aQODvZTNSN9X7tWXJKwZnm-6fBtp9u1KQugH7SX68OGQuoF-nP2fu8hgEUfJp8ABl7u7-oF7tO_kZ5PDwU6b6V84izNEWyAOINbSJOoozsMalWaTExbqEZE9FMfbLjMLeby8LO9EEYpirJJ_xt0H8mlBS8Wt49bf18nnPcBk3mSU01BOSpkT9RQPZfaE_9gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=o7KTY2jaUhzGyMKIXjiWpdbUptYYIhfEmkKJYGT26sku1L2LKydjml_cnMk2gj67JA2Fx9U3Aijj8clAgmDcrA8a4F6J-73Oij8apAEi-9xtZXqC4Q-6IkHv6-qyc6KOE2NilijNlnfungysbxrwS_sgIDxU0bGyxZSIKrZaEcQlivYE536mTmqn4irj80JzzFVGdb18oCh3D1_8MJQtBD_yuMl-aW4beZvD84KiScJPNWMiwj4YguX2NB-PMnnj7DPElXaQvwaSTE_YPA6Ip5EHJ3dBPcFmAO1V-pdf5YhdaBxFAOJHkiQ_8pQWOuA3CbSc7dpbIZJVIdSsE9vNSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=o7KTY2jaUhzGyMKIXjiWpdbUptYYIhfEmkKJYGT26sku1L2LKydjml_cnMk2gj67JA2Fx9U3Aijj8clAgmDcrA8a4F6J-73Oij8apAEi-9xtZXqC4Q-6IkHv6-qyc6KOE2NilijNlnfungysbxrwS_sgIDxU0bGyxZSIKrZaEcQlivYE536mTmqn4irj80JzzFVGdb18oCh3D1_8MJQtBD_yuMl-aW4beZvD84KiScJPNWMiwj4YguX2NB-PMnnj7DPElXaQvwaSTE_YPA6Ip5EHJ3dBPcFmAO1V-pdf5YhdaBxFAOJHkiQ_8pQWOuA3CbSc7dpbIZJVIdSsE9vNSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=g5V-Oyb3XngicC2P3Teh3DU_5S4RWVhp6DI_6qy-MW1R6dOpHGCeg7fG5KPJspu2q3JvipS1NFTkDxAyJNR8r0rVY-Z0hMhzSwVvk8XNGf4yyW4dGWLeU-8klLLtNLFcccv2dk0mbQ7g3P3_suvLz81lMLbTn0xCvrR4QYw-nMV5Koznbn19s_Q-5BYT-72o3jcowMImwy97k9Jk8ehgaOR_VCh3m-lIlW0EjH73nBbEvL_cMn843ExYV-vEQL3yrO6PnnrF4Fm0w102-tqpnrCjzNRVauwSJgVKTNbGVSrT7GNQyLmqeR4nC1IJXJvvofIwCY-fXIMWYrftK8MNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=g5V-Oyb3XngicC2P3Teh3DU_5S4RWVhp6DI_6qy-MW1R6dOpHGCeg7fG5KPJspu2q3JvipS1NFTkDxAyJNR8r0rVY-Z0hMhzSwVvk8XNGf4yyW4dGWLeU-8klLLtNLFcccv2dk0mbQ7g3P3_suvLz81lMLbTn0xCvrR4QYw-nMV5Koznbn19s_Q-5BYT-72o3jcowMImwy97k9Jk8ehgaOR_VCh3m-lIlW0EjH73nBbEvL_cMn843ExYV-vEQL3yrO6PnnrF4Fm0w102-tqpnrCjzNRVauwSJgVKTNbGVSrT7GNQyLmqeR4nC1IJXJvvofIwCY-fXIMWYrftK8MNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Od-B4VFaEPWDZDU-Y8F-xk32YUe2eDqGXJ8e7NUZSFq_1Pw3kXLvLWM-llRt4O_L0rnUrzKu3dEpCXKJ_gKi8dXHt99GDBHZGKnbh_PSaWMC6j3UFNXbUvwjCUOCipTwI7D1XxIQN8XW3SyzSg3q0XvvK9hwSyEbp-P51N2Svow70J4l_cqTL_-HHLBD4gWzBrl9Zg8JEw3fOBwXXJ2TrSHh0tdhkfy20yUZDi22hcDhr_FRu5p_mEZyQ_9isLQY1Qp5SSs5GrMQsDw9eCaxaLaA9ZtPVoqYR2pSV7SKNk7-qPA0_dXo8AFhWvdXaUpt0v_0kZIYCItgXIL09XeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY46GSGnZL_E4QIsyOC9cZ5orsR9XpXXyllbpFsSLzMYr5ujReFtbngjXyO3WIIOOsc6158JPe5Llbgk_a75rfADH-uqwL_-NnTXUvgQlx86Susp7_UCRsVJWBUouEE414QunGN8kMBQTsHyvjjzt-EMv53wMzlqOeEn44B4TExOhvymgRBaBGp2YhLgIk7kU3q_AP6-g5UtzPd1GevcAuOeFRSLTnR_hGalUZnBdfyHhi51o8PTyvMOFxNO98mjfpDVodleF8LM1LF_PFpdOIpgcGgd1af_aDlTGnFWtM39pGzwEJyAB0iv91C_6KYZie4X2J1yA4rReZukvsB2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAn5U6p2WUS_KJg1t1z6tAbJn5Gl6md-3aRG5AK3iohm65-uy792FppIgDEI2DoAj5zXqUyXLFzvMjLzytNLp40Y0NxYxPWCGfkJg10Ec_bLdQiwI_MX2mWdaMGMfEplq4-TSNj2QPHhWT3qfUwZNgDWxISbrc1PZ0RU4azj4aKFA1c8LR1Tft2wV4pcFtYhlK8i1KZWeHiT7z_4BuMqBUDlW04_7mHIZvV43B1AIjYWKZLkuw6IdPflVAuP1_cklvFdVKNyIyfM_UwmnN_XLe7MX2ZKbtKGMzxUO1wNe6TKsU3Mj4kT5QlDYY-BfgrrLwRvnO7WPNyl5-SIjnZU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEOEuxv6T9hvMXKGOBeDGy4Nds8rJrlQx0SKGVDyPnNkUYE9I8cuZmD4qMtNj-NxKTlcF-7-Py5J9zUiakMES_dS2JyZdAbMLhhxBXfMBnoIHjTxNQCHgOUdD37M6X3t6Iul9cC3DP5eQl626TbkI0yt0SjSPKLV-GGqVWcqFZiZLxsfH60aUe5IcTIDvg3yYcJHoF1UQNyja4iKNv8CCj0adCfth_G-GZsNoshbbAbmmlfkehDyVYNABvVWwG7VliGxyeP-dcZrqz4k_N94Fsg_i8wbIc0HRQ6Yy4Y6yApugLae4mvCtMj3IKEMMm7bbkyNq6l6T_nK11u1WMzPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOjQ1XS-g4pEmWUWvCd1iBkC3KwPyxcfAB1hOGw1iuOi5Iv2aVxcVWza-L8_q_Hpnevh8vx6iphh0tpI3ufPTGXqecojZn14HIudx3NxXnCnc5mchkvhvaCN0cbSxfQojLJ4AUIc7rsMeFv2Qf768BTQPtuK9SlCWirXbqELEWL2g_IdtyFbI1ls1OLlYteqWGtyqNwu4KayNhRx-E_51QiRu7A0K0-1iw6P5hoU8H_LQ6IVANVgNQ1XU4M8HE79Y4JUR3QQ31CyJYJBgfWezSSc7L430BPOaUbspr24sPM9ptx2JYc4p3eEHo30mCCRKz1NShRsHubW825RagFIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqSNltimbb_F8FM65AOuZLnhy6DyphZ1aHtYZk6FKHK_p-PnQve_2CIhajuvcz3KwNtuUTmVV19LufcUGLqZK8FnWfWFpEJK6V9ECO6oJ-ErwywN2x-rIaPMwntJmLnuO-BoLxG6biRpW_IaNIOyEz1O83_uG1VMWVtymquD6qs-APE3BomAUOUj6S7nTEKR3wXgCEBJCqQJEWUcs1oF59TouHj4oghQUIjw0egaETZjP9pgKfC6bE2aCrYYC1h8n3mpPXR0_CJxem_cs18p0-coaXAXQKj9kjx8zqJ99Ac1ULSya_payR0kpKoSVg6xfNGhUTA4DMDQ2UjkJqVd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1VJS_3w0aG7S2mfctl_I5rsM5og9OCAXEximdu0kqkYkVx_1l-Z1SA6O5lNrzOa6qNMwLO6MUG1VfHH2MDdE_NnLxgdSykyR8Ig6qXPr9LD090CwO16mng3xfcEXc7fqVnHn3CjXatP_JsINE7CC4LKummsHBY-P-lt13g1x3uC5oXJHJr00zfse0rzeMY6D8PRpCUSqpJx2GCkw5kLagWdlerrv59Bhbs7eG7nNBJmMfIQyQXuzznvhMjScazxuu8Ywd_ppbxjuc9-49DlqC1jA3Nm5QxDqbcyVa_p_z5DU-GQHMszkE7kx4tZiujvpuiJBjyScypN-V8_qEkdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STPyPtVeSnrlqDfoPBmbrfThbrnpv_6IV1vrmype-ctdrLpdCNMbNcFzOq_SiO1DLprqOZNfH5tDZTKJoq671xMjjNWY40v5dDebatx7bifOw9rBqGg8draKXOehT4oBc-Iq2kgmmcU6yEyAfM_R0ydU1X5ZECzcoThj-GaWT6JCWlf1yn0PV5RAM51cl3kKNk4TZFzuwlFN_efm5vr9ApfeYHwWUSbXYWbm9riB3IKoov491FvxjIWTitqKewi34m627n9JWZi24_m0umuxR1aGc443UWk6s1nVoC7kiYiKq_xWOD02TQ19UEZf_C7T7H2JGNJmZrJ0kV94rY45QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=N8ClFEQ7YV5CMgA0B5XsQtyYGRG13haM69z8eTJz3xY8jqFzTOBIzd3Fy3svdD0bw7f-khzvt2XMKH9HxIj0jb4qRVRpmyGvXzn9XG8UuCthUq1zZAXSj57pYzEYb5lYvyVKxCwapCS29JyUcjl4cFYCo7u0QOrzOk_6hQmE7ewPKzxkaePYymznob0cnFi88ibGQhrUAtT4EA7xc20QdKLbqA_T2PSQsjqT3p8mFHBhtVpo25Jg8FLYwEjf1xcqsN0ejsK_3SJ_cEpZshpNTMA3D-GD07Vp0Oo1J7-o7Zs6sGmamHYRMg35R3BOeIj93cohBxtKVS703S-VqjwtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=N8ClFEQ7YV5CMgA0B5XsQtyYGRG13haM69z8eTJz3xY8jqFzTOBIzd3Fy3svdD0bw7f-khzvt2XMKH9HxIj0jb4qRVRpmyGvXzn9XG8UuCthUq1zZAXSj57pYzEYb5lYvyVKxCwapCS29JyUcjl4cFYCo7u0QOrzOk_6hQmE7ewPKzxkaePYymznob0cnFi88ibGQhrUAtT4EA7xc20QdKLbqA_T2PSQsjqT3p8mFHBhtVpo25Jg8FLYwEjf1xcqsN0ejsK_3SJ_cEpZshpNTMA3D-GD07Vp0Oo1J7-o7Zs6sGmamHYRMg35R3BOeIj93cohBxtKVS703S-VqjwtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWfMnDj1FRbP-2f7NKxhbJhxTPGtmhtDWHmUHqQLynfiOSAtrt77gvsGXeb6O81Z4PLvk-Cd_ljYCiiUpFM8XrJpKYI5jv8-weBEwFCKzcYuCbEoqEbPpjMMhNILeUw15hfW7RJEy6vhcQl8D1jfBSYvgONa-Wnm4D4Zdc5QjIz7gYG2RLP6Dd4Nxw8GtC2nyhf7-OLytwBKKzWZjOWthYGH5xCqBjbQFCmttbry2195d7BQK3211y4dKY86J5bSSZuQrKEk5l2rj333huFsmZq4USjvFHJlMDjN4-XxQ2MxBVzHKxNxjUL-SQmiMqJSEQEtCtLDfHVn2aIUGp7iUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mQmsNfZZyVrTRKyBcFFpDKLg_4t80I8Ahjt01YNd3M8AEM8sp4MxdKZGDDTTmfRSsEgkTO4yedrLNF4YRRqaXHwwHDvi7RhnQdN5GJiE0TpgARIJbJgtI-0udhcb_8NYHqFgTuDz-jRVHGsHP9d7E5KXKkmbc0Ja6LZOSixP1Ae6KJ9s_AeFNoOHnomIAxX9jgdOvOju1TJHukyQBkTdwq_t0fY3aGCAbRdhuRTLB9H6MK-SQBy_j9tr4MZngAlNPb2P2g1M-bz5RyCb1_WffIyjYi1glfh80U1cgnuTjYRQvImeMtm9t5kag0AG3d8vjdGSOgizn6qOr7ubO7GBug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mQmsNfZZyVrTRKyBcFFpDKLg_4t80I8Ahjt01YNd3M8AEM8sp4MxdKZGDDTTmfRSsEgkTO4yedrLNF4YRRqaXHwwHDvi7RhnQdN5GJiE0TpgARIJbJgtI-0udhcb_8NYHqFgTuDz-jRVHGsHP9d7E5KXKkmbc0Ja6LZOSixP1Ae6KJ9s_AeFNoOHnomIAxX9jgdOvOju1TJHukyQBkTdwq_t0fY3aGCAbRdhuRTLB9H6MK-SQBy_j9tr4MZngAlNPb2P2g1M-bz5RyCb1_WffIyjYi1glfh80U1cgnuTjYRQvImeMtm9t5kag0AG3d8vjdGSOgizn6qOr7ubO7GBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Dr4hstiOSkc1EKfBzv6n13saaAAfuQhPd6Q9OkyU_i7BUuHH6Uea7H9rct4YhQpKm2EUN1TCot5RT0bGa8RPXN9Ifj5jz9mrUIjthDmdAGkPDZhUXlPLV4h8WUXAs-3FhqkgMmIoru8ephh633TqxzScvKjRviaGz56efccXH1fJ8Iv4NWCdf0jTc6MG7l95Q0M93r61Wt3zfng_xWGaaids5er1g2l8oJ4axuJJCsPX5CkjV4tipYTMT0YX7RZF6pQ_xkLLaOPpQAkh9vCgpVvi1DpEgFiTLMcNMrq71zej-Fdxi1aSiXbyh3yqBGq-fQLqIVVhdV8QQnxKG5QsbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Dr4hstiOSkc1EKfBzv6n13saaAAfuQhPd6Q9OkyU_i7BUuHH6Uea7H9rct4YhQpKm2EUN1TCot5RT0bGa8RPXN9Ifj5jz9mrUIjthDmdAGkPDZhUXlPLV4h8WUXAs-3FhqkgMmIoru8ephh633TqxzScvKjRviaGz56efccXH1fJ8Iv4NWCdf0jTc6MG7l95Q0M93r61Wt3zfng_xWGaaids5er1g2l8oJ4axuJJCsPX5CkjV4tipYTMT0YX7RZF6pQ_xkLLaOPpQAkh9vCgpVvi1DpEgFiTLMcNMrq71zej-Fdxi1aSiXbyh3yqBGq-fQLqIVVhdV8QQnxKG5QsbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUNziX1wkUh4d8lbw-E_qY4TWxumILbeciEgdcmgbb61JepiuZAaQvEJTvQnyNHcyX10lSDmb4EZXUZz3O44HqrS_i2Xo78NoH5TfvSqdhTgdxkPF68qg62ID6u80_TSqi3DliE-sQRrvG6xEc18n9uuV3yl1RVSp7s2jky1nPXzwXsDLtkBBGVcLSqNLWQZ6c88myoloWAIIcCNpbVBWA7kMnothjPCm8Hj4VNoZ_kse5WjhthjNakZO27aN34Kz1jjqD-HyyM40iXcdThk9zcIfZjmCclHd1vkR_oQ-uzdpVcL6nABDracm-UsBAJjYH3zAOdzg7AOwFa6UbgqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDdwZXQ0J8bjgmbBOhXdpxiNfQACr4nmamzbQ3VQjFFq3i7PRP4UnbzRBUAFdrsPh-ZQrQtPlJE1TaK23g6DM157jTjjhuGR16owWcs9abLnrD7gdyIfiaOQ5phoLKycxQKX2FXJ2-cjRZz0-Nme0_KMyiGDQCRFQuLPVFG8uAeqEXbLJ1Vx6-aPg_vG7J0A2A89ioRoKiyRdxmWn3UnXRiDWemivSpWYKwAyjWu2YGMq83x5aAW0xX5YyhY0myiTLe-vrOfxZCmKvTEDlmFE0dXVS8D8xnH4TrMT4hbFHU3GbsE8Ops_hjjjJTMBtdkNj6susmz0nf_L06lM0Hoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Tz_U8WtzPbReBicXvOe7HRyb76f7An_IhogbeF4YZbRRnUN5RZEIqnqv4pKW8iQw3CabAJYYzShbRFGv5Uumf_gcm0Gj3hGfUQxuPjnHlEzQ37ZFxVF6cCLYcl6Ze01g-ZpnCLiyz1GWcZpXUwZ53rgBHU2GQbbXfl7kii6g6Iij2EjLGiOGIJbmAVaI5-BXFRt0PTBVeZz6hHb2cjPhYGiqBh4ufXhE9KczUzb89muXeDJcpMN_GNaGtfHGDRg48adSLjnHnM0BMvRmJn0BwjvxbN19qyboZ14LDTBnQWNNzynSva8DXwI8kZ4y0SiwNXell0tyLwR2oCe1Y7DSP36_267Lf-3V9j0_7694qdY1B1_4BTNZ_uvJx5E_4HRmXDckWYTWDu0mzRxFeuEofzvHHz4t_8TqCquOAj1Ntsq78Ywer3Ehb8apxbkLFs_J3ZWHMXX_S55BS2Db1F82anWSzQls3uC_9F75y6OoVTeJtExCrm0VSE_dOj3jRDS_U0s8Im3Y8T0g3VObTskm8IoNsUdq3QWTpd_hTw7RiCZAs4MsS-t9XqP3zeXSJtqlndORw0xybGR_DzonFziNDBMj2xtsMVlkqTNoCVDZYEXbc59S6c1cfBJiVXR8HQAjS-tvAlvhIitFBlY890jy8WX9-j1KaMZmO3IvpxvD8w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Tz_U8WtzPbReBicXvOe7HRyb76f7An_IhogbeF4YZbRRnUN5RZEIqnqv4pKW8iQw3CabAJYYzShbRFGv5Uumf_gcm0Gj3hGfUQxuPjnHlEzQ37ZFxVF6cCLYcl6Ze01g-ZpnCLiyz1GWcZpXUwZ53rgBHU2GQbbXfl7kii6g6Iij2EjLGiOGIJbmAVaI5-BXFRt0PTBVeZz6hHb2cjPhYGiqBh4ufXhE9KczUzb89muXeDJcpMN_GNaGtfHGDRg48adSLjnHnM0BMvRmJn0BwjvxbN19qyboZ14LDTBnQWNNzynSva8DXwI8kZ4y0SiwNXell0tyLwR2oCe1Y7DSP36_267Lf-3V9j0_7694qdY1B1_4BTNZ_uvJx5E_4HRmXDckWYTWDu0mzRxFeuEofzvHHz4t_8TqCquOAj1Ntsq78Ywer3Ehb8apxbkLFs_J3ZWHMXX_S55BS2Db1F82anWSzQls3uC_9F75y6OoVTeJtExCrm0VSE_dOj3jRDS_U0s8Im3Y8T0g3VObTskm8IoNsUdq3QWTpd_hTw7RiCZAs4MsS-t9XqP3zeXSJtqlndORw0xybGR_DzonFziNDBMj2xtsMVlkqTNoCVDZYEXbc59S6c1cfBJiVXR8HQAjS-tvAlvhIitFBlY890jy8WX9-j1KaMZmO3IvpxvD8w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUqjn2u8I2L7PbSQ2X5noTepmntZ4mPOCDp-OPEqhWZLQMTqS0fb16VaMfLpJJQpBoIG3lrMvIYjgHzz7rMLNcslD70n78_G0T98A_DXELOIh15qbsH3dKdtqVcNhf1rFoFwunxrPpxv6giPV9Ur3XZ1cs5Njx1wXfxVxHxS49MjTpWQMkvbEgXf0f4g8k3mTeZ6pyp1rlecD2AWoGoMAiZQW9_Ooe7SRCmH8Tx7ofojIUn_2AVx62KBf2lEFjsAQZW4FsQcx6KmM2l_FuN_DcrHLBX0vPy22EacEJ759yBrZKdpacHhY8WexxXa-IKVfz4vKcgrvdt8wucFreREMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=fjobVxL3MmBgzWtMwZBwacNWLy8uhVg49kOWRJRTHa9X5sxE3UxteBxlf0K7afxpGrXaxDbv-7aMbsQf2xnvDSz8YyK5BMlR2ipdh8HEvJr08NCdFKRCEYIMyGG3xTEYV2NGDoyNoVC1CHmMH3R0feBSf-uOZ9l_vrIFJyM22kT3xn5z0v723BwzgSNV9eE2W_wEHHJV5LF4TdzbqtVhi8uX5NS1MK4rJ9vRhwRHip_0uJ9wXa9ujHp80cjQVXFXmj1c_ietqOQZ1IGGjZcsS8hf6PRRIqZEkwZGUhf6JADoAkmCPcAXmsTo0vy32atB_jm9PwoSf0D6hbDPKO5_8r54KcYt0KSnOYzEgSeSO7KFQGTe99IlajiP0BCqEu0wwfH1Pd1MQCSpqpNdJtjizywhIq92K3q_x0JqtLe5ddh72nR0xyetLM4XkmPoYAEEJc6feujP7pAr4OeurKrbUPG4x8O8JWUbc8iOEnKw-yIz14obszQoSWm3_980sAusfUppxcdYqbzw4hMTrb2aY0Q99xAxHs6VBKSz5YmR4FThPSjm3dFe2m29bKqu8WW3SJLSuaFRHTxD3Mc7N4_evBtaI2Nk967JQkQm72mdVHbs5Lji8m_k1IJX7y-piDie3abxQOIRYJkE9ZHTcbw-smCkpAPHdi0NyR6ph2lqEFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=fjobVxL3MmBgzWtMwZBwacNWLy8uhVg49kOWRJRTHa9X5sxE3UxteBxlf0K7afxpGrXaxDbv-7aMbsQf2xnvDSz8YyK5BMlR2ipdh8HEvJr08NCdFKRCEYIMyGG3xTEYV2NGDoyNoVC1CHmMH3R0feBSf-uOZ9l_vrIFJyM22kT3xn5z0v723BwzgSNV9eE2W_wEHHJV5LF4TdzbqtVhi8uX5NS1MK4rJ9vRhwRHip_0uJ9wXa9ujHp80cjQVXFXmj1c_ietqOQZ1IGGjZcsS8hf6PRRIqZEkwZGUhf6JADoAkmCPcAXmsTo0vy32atB_jm9PwoSf0D6hbDPKO5_8r54KcYt0KSnOYzEgSeSO7KFQGTe99IlajiP0BCqEu0wwfH1Pd1MQCSpqpNdJtjizywhIq92K3q_x0JqtLe5ddh72nR0xyetLM4XkmPoYAEEJc6feujP7pAr4OeurKrbUPG4x8O8JWUbc8iOEnKw-yIz14obszQoSWm3_980sAusfUppxcdYqbzw4hMTrb2aY0Q99xAxHs6VBKSz5YmR4FThPSjm3dFe2m29bKqu8WW3SJLSuaFRHTxD3Mc7N4_evBtaI2Nk967JQkQm72mdVHbs5Lji8m_k1IJX7y-piDie3abxQOIRYJkE9ZHTcbw-smCkpAPHdi0NyR6ph2lqEFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQwjsawj78dCVS73LgEgcpC-ThDrxDKX1qBgwe3l0ukGIQJxJez2jnLH3Zw9ch7dR5nVhq0jyqLhh7Szy7mNJZc6Xc1tZ_YuZvghzDfoZ3uIuRuOu3AGjwt580EksyzdW_wBy5xs7GC5-rJgCXo6Eg-027_fxcFA5eqBB_eoOLsg0CUFhTBSeLooGFsGoXMDzy6m6QM6dSUq_u9uMWzlDaao_JBlcxz5b5-ph71JjyQS_GOjxUZGsLxCaZe2vBvh6ZsxDdNL-Ot3CLdMyW3J9r66jFVjs5QkUOwJQYjgYIcUrjIIUq7BtBHcPyLHis7SSVd-YQcgWsyCBJ68nOjQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHnLIese0RHtntVH7YGMea7hpgVniEoVGoa6tWByyz8nWtwWTgCQlcRtVODnXJjgaVIt4m-C4n4FPBgBmQBCaApHYEEzMIxyrZxoGV-ofrk9m5Gtzh4IFbQoQvm4X1PVtGF__hQCYCoANcvIPlymTucSmJAePFqHXvHV_6TxwTTgpNSU1sZE79-VQf5mGrwIW04Wa7AC3XWHvqXQMAbciIf51EyvD58gIq2_F9N6eWfnHm_7uE9LZN8zyO6fWvIXBa4TVW2Ks7qD3U6NAFY66cn31EC55XyoIbMbLkolkpSdRQDkELcaxwqGzNJTKcLvXd2N-fP4QE0IDR0N9TmjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
