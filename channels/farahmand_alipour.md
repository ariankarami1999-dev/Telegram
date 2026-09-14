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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
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
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpWCayyCDAcWeSRoAR-75XxigAGnv03rHykX05dJFvbJ6GNXLc-pYVME54ma_1VlicHZ0AwQc4gxuCMxFIN_YrZHninfH00q0QP1j_DRdD0rVoTmx1Ktx8gQJXnRT4Ez98XV70YgIjeKw8jpAfteTUR_HgdrWozt41aDh0lMRMZin_Y93Sxg2h8Yb-Wj9zd6PPz3oSuYWBtn9ICgJyx3cKIFW9QGmEjnaoBYLzWxv388PsgoQEJ2nI8-I1Pc3xHsHeav0-QtBK3Qq8OjeKv5MLcqO9MllLnadsnyXD0P6TbiRqZ0TUTPzRTEM6NwtarJlxZ9EtASKKbDCenqGkHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL0sBMXVei0b2yfK9ciEkmF8V23met0IVVrY4GP_UyPeWzbjYXzTomXEPt0hhqF5frE7TB-NjtLzt1hIoJgyBGJpEW1fzJxGoNfbyogeEdg_ezRDxVexM1G8bjhobMM-Dy7GqVXuGpajP7nclZb_emb5a55k6f3iauLpfUjxkPIpDiwJPDvOeAD4wDf83GyZS0A1qxuawSIHuT7Dc__iY_CXdkbx8Oi9zwYnJkJmVMt_FRA1WIQiWjZwgA23lRstjrKoq70izsL_F9nyfgDByULrSchDfUUdRWeaFP3Tly2ZOlr-tdePHmNlg44Z-xWAXdt1OKfcnBkuKE8ZTvRVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KIjaQgH_-ZMO4y6bbrnL66ccnNcL39GDZ5NnAgT4oLQlOe3_DT8buPXWyYaeNvU_63sawmDt-bOqEmLTF-5Yg1K9Xp_JhI7b8nuL-8vJb_1hzKoOE6AKayQ6biPY5Bl1ou1wjqoEFXIImneQUF1vZed0EvAJov__8eeFcdrN_T76suCajIQf6LkUM2V2JrloMj-536i3Tewz3wUkIatCgo0w12Z470ST3gM0zxW62OCRx7yUMvgLZJufBktS9MifUvQjZqV660YBeGqdfoLQTZM0y8QnGdgRoIZeftQW_j3IGAdr2rrAF-1axktdvoAQ-OpV19nx_NP3u5qJzpgKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KIjaQgH_-ZMO4y6bbrnL66ccnNcL39GDZ5NnAgT4oLQlOe3_DT8buPXWyYaeNvU_63sawmDt-bOqEmLTF-5Yg1K9Xp_JhI7b8nuL-8vJb_1hzKoOE6AKayQ6biPY5Bl1ou1wjqoEFXIImneQUF1vZed0EvAJov__8eeFcdrN_T76suCajIQf6LkUM2V2JrloMj-536i3Tewz3wUkIatCgo0w12Z470ST3gM0zxW62OCRx7yUMvgLZJufBktS9MifUvQjZqV660YBeGqdfoLQTZM0y8QnGdgRoIZeftQW_j3IGAdr2rrAF-1axktdvoAQ-OpV19nx_NP3u5qJzpgKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP7VO6RdBJ9OxLlg-59rkfY8SRB88j2_IoYISTco_qZpJMXHBykjn6gVqNUaJtNpLkPk574xHefMb5e9Z5m2u16ffQ3F2n8RKylF7DVl_2QXUz-TS46bxk2kN6iDjljREUrPM6DwgrljTutYlAeiVFTYw6iHUjREVYFWRD5dzrMhJIoKJiixH-Cbtm8HNYFS-xuQTFWaJnoGkTQ0oOaDytYZLOD5Hhr_-_EVw53s-CRLCPtQREazGfkgfQjjBsGm2G2d8ADIjYtJk1X1YwMXds7h9T95UtQq11iiv7sn373fNubci-P3tPGG4KmPNlZQJzx6hyOoo9OUn3XpMW0Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YnWBJORLFUxQhdwkHbKrqbzPtG8Eaefn91ENiDs61TelVuLY9otztuOn0ZQa4UBUpOqax3grrdFmt9rcC1F1_Zk1pe-9vGg9oavcXMdghr06QGAtw7-R7QT_NYCJGYnflX4UiueFkM559-YU5gmsmpGsZ-SHLP1PtaUukyL1LKAXFkIrFhZaCgY3lbWk-pllJGSv8hUh7H5R2Pd3KmC9sAzhNOFIj604OTA2v_7AGeKtNAbkBZ4QW7dKaNm7wSroqBQlxXO8-wYOkcUSpVHdPTf20jqpu1_cjOIil7JVNyRnhuPMoux_c4BMLhs1tGZQ11luvZ00NzHnV1f4PjXovA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YnWBJORLFUxQhdwkHbKrqbzPtG8Eaefn91ENiDs61TelVuLY9otztuOn0ZQa4UBUpOqax3grrdFmt9rcC1F1_Zk1pe-9vGg9oavcXMdghr06QGAtw7-R7QT_NYCJGYnflX4UiueFkM559-YU5gmsmpGsZ-SHLP1PtaUukyL1LKAXFkIrFhZaCgY3lbWk-pllJGSv8hUh7H5R2Pd3KmC9sAzhNOFIj604OTA2v_7AGeKtNAbkBZ4QW7dKaNm7wSroqBQlxXO8-wYOkcUSpVHdPTf20jqpu1_cjOIil7JVNyRnhuPMoux_c4BMLhs1tGZQ11luvZ00NzHnV1f4PjXovA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=qg1B6lg603bh1Mb7YHDQjwgOBpPkQ1YPPUszAkJJ5YmPRDMbuVH304fuLwj7S8RhL0YcaHttLuu_lZny7jze0ApBaFez54PMzXx8YRmYeTrBSTpBNjeYP-IF_TGnmLGzPRORYaV9xsWvlbwoxgunsYZAipYxn9UHEo6n2Bsn7DJJ12q86qOyxU7CN68RpbMMCtBkwdP7SeH9tmVPQJmvAbWlDND1fMoBedo7eqk7h7foVgQ1_XkQ5kteIM8AfaKYFxJJkzU9yeiMGYUH7O0d-DyXY_JfR9HCIMrRRYIJBnR1ykHKWmQ2ARnbhrokKULOegNL2TSMHRDMvj5dW8baWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=qg1B6lg603bh1Mb7YHDQjwgOBpPkQ1YPPUszAkJJ5YmPRDMbuVH304fuLwj7S8RhL0YcaHttLuu_lZny7jze0ApBaFez54PMzXx8YRmYeTrBSTpBNjeYP-IF_TGnmLGzPRORYaV9xsWvlbwoxgunsYZAipYxn9UHEo6n2Bsn7DJJ12q86qOyxU7CN68RpbMMCtBkwdP7SeH9tmVPQJmvAbWlDND1fMoBedo7eqk7h7foVgQ1_XkQ5kteIM8AfaKYFxJJkzU9yeiMGYUH7O0d-DyXY_JfR9HCIMrRRYIJBnR1ykHKWmQ2ARnbhrokKULOegNL2TSMHRDMvj5dW8baWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gqOs92qYqCtwzZ5t17jk-Uq5gZs1F9bbtLfvm6sndpuIrjXjVToWq3UnUjrw7lhGyQ2zbqSDW-qWn-CjvxWAs4aMUywirMMyNOohgMBS0Ge6zey75ViJL89ByTmb166w9hui8i1uzM1FKl6aXByqnVRp9W_ubQQ07OTTOGfvSALcbEWxqk2pqUqRIvIowex_D0dwB_oN5A4L8Il1-eTM94_EHNzetYGYrLNeBSDY2RrB7VnGr_Ip0mrka7Jhn_9HJYMj6X-5yaMVfpmWEcxBmlvdGy4JkID1qQvTGQyiOWfnwp2tbHTIHx6DHYNLgzsjhKWDP7jaQws4-NXExdSrfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gqOs92qYqCtwzZ5t17jk-Uq5gZs1F9bbtLfvm6sndpuIrjXjVToWq3UnUjrw7lhGyQ2zbqSDW-qWn-CjvxWAs4aMUywirMMyNOohgMBS0Ge6zey75ViJL89ByTmb166w9hui8i1uzM1FKl6aXByqnVRp9W_ubQQ07OTTOGfvSALcbEWxqk2pqUqRIvIowex_D0dwB_oN5A4L8Il1-eTM94_EHNzetYGYrLNeBSDY2RrB7VnGr_Ip0mrka7Jhn_9HJYMj6X-5yaMVfpmWEcxBmlvdGy4JkID1qQvTGQyiOWfnwp2tbHTIHx6DHYNLgzsjhKWDP7jaQws4-NXExdSrfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=DyfFScvI88Y4KF-U5TcKRpDvOHSEiL3yksjBmAK266duxJAKLT3i4m_7DkKJvS4dC4ExWN5YjDUVqa_6ne00XBuMVxtO8Yzj0U8LgjcaFPCYzeAFInPlQFcY-v21aRNSYwauLAXyrZ1IolPGQ_m4EreXIxcDoFJ6E2KL6uZt2KLjEy9pIW9hUlwGveX9QTBY6ardcMA2A0zRWW_gs10zRF971jO_tsAVXEk6FtO1kEsgrhnSbNlJNuJSF_3kE1HOi7hdJt2N0_Cw7dug7ln0tWt_Hy5Q7wLSydgY_AljxFPFF1Fukgr3TAZFDNMlTLHzMHeNgK58mmk-UBBQCmbIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=DyfFScvI88Y4KF-U5TcKRpDvOHSEiL3yksjBmAK266duxJAKLT3i4m_7DkKJvS4dC4ExWN5YjDUVqa_6ne00XBuMVxtO8Yzj0U8LgjcaFPCYzeAFInPlQFcY-v21aRNSYwauLAXyrZ1IolPGQ_m4EreXIxcDoFJ6E2KL6uZt2KLjEy9pIW9hUlwGveX9QTBY6ardcMA2A0zRWW_gs10zRF971jO_tsAVXEk6FtO1kEsgrhnSbNlJNuJSF_3kE1HOi7hdJt2N0_Cw7dug7ln0tWt_Hy5Q7wLSydgY_AljxFPFF1Fukgr3TAZFDNMlTLHzMHeNgK58mmk-UBBQCmbIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9zvXSXeaPNfX5cwk4H5Z6BRwQF8_kUhHGMHnzwsIupfdBcknRyc02cb9kSKZ3AWgKubnhjr5dyVOjpV3SCS-YRIpCMTCevnUF1ZMiU1O2pekREpJwqQIXqbEGmM4_0sxVp49BvKXu3m2oWbA0eK5Usr1tkyqo70i5fy4uRYHR1EVjw0ML4B5XKHYfG94zqfkuBFYzygGSElwN55aMnV4RmrHby6WJG0WOAfu56-yB0_KTJ3QZvUDTTcMoIUlt_7_Ojx5-wEn_flJDspJqDx5Hdy5kZc62rNnrkKKesXMiuRRK6RG9ICHkHyNRaH-taXnFKDBBmMRr8VlyT79SKhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=F_z3nJ0XkK0Mtx7_BHiKQd2Vv_PxpgeYuL5e5g__64DobJn0zKvdvHYwehHVBUcjDjSAmfFmpSlPplMYBdNL9a5VH2LCeYCSKeX3-VR_xA4bDeoGxFDj7FQ7vYiCwT6bowNw1eyKYrNG9U1JzRpzFUMt5a4HORmC1XhXN35rNZeUccCkE-hdi00ehMGEPSRECNX0_G2c4Q2ZgeGrFEwzDkE14g2zkHeRWgU9FQQq0XoM0rJg-OTDw86DYifcO2ZgFe0096zZO7HRUkvOozpZvk2X_0H-DGoAraISH-gbuRuEWxF_yyKqKrVBxJPiAOKk1d5rxM2vSiYHOoW5eSk1hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=F_z3nJ0XkK0Mtx7_BHiKQd2Vv_PxpgeYuL5e5g__64DobJn0zKvdvHYwehHVBUcjDjSAmfFmpSlPplMYBdNL9a5VH2LCeYCSKeX3-VR_xA4bDeoGxFDj7FQ7vYiCwT6bowNw1eyKYrNG9U1JzRpzFUMt5a4HORmC1XhXN35rNZeUccCkE-hdi00ehMGEPSRECNX0_G2c4Q2ZgeGrFEwzDkE14g2zkHeRWgU9FQQq0XoM0rJg-OTDw86DYifcO2ZgFe0096zZO7HRUkvOozpZvk2X_0H-DGoAraISH-gbuRuEWxF_yyKqKrVBxJPiAOKk1d5rxM2vSiYHOoW5eSk1hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oGK-ulEBPYheAXcm69RLlFnnFy9XiH-O2yq57ovsQ8PZkSh1N1ViB1fgT5ZEoPR_iHYJeoAwEHCmgDSBvFCPVBn3prPJMUC7473dH9e1N8P_s_HuX8QMn5ub0hUCx7UJz7QERNZ8SBEpZIdZlPlewFK55LOEh9re-0B1O5zdy2HUNGPH2Vg_Ki_kkqT-ShmEb8gHWPB_D3cKna42di1zsrkHn6hphU1T4JODTg8S69lF5pNTk02HxSl3jbsLmX2052zz-VjkAqtgEmGgALiM-A3uppQcUtr_Y7sM1d1hiuQl_lbQ6T6XqxTvevjY329G4YatSsnqsCKqxQHfGi6Pbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oGK-ulEBPYheAXcm69RLlFnnFy9XiH-O2yq57ovsQ8PZkSh1N1ViB1fgT5ZEoPR_iHYJeoAwEHCmgDSBvFCPVBn3prPJMUC7473dH9e1N8P_s_HuX8QMn5ub0hUCx7UJz7QERNZ8SBEpZIdZlPlewFK55LOEh9re-0B1O5zdy2HUNGPH2Vg_Ki_kkqT-ShmEb8gHWPB_D3cKna42di1zsrkHn6hphU1T4JODTg8S69lF5pNTk02HxSl3jbsLmX2052zz-VjkAqtgEmGgALiM-A3uppQcUtr_Y7sM1d1hiuQl_lbQ6T6XqxTvevjY329G4YatSsnqsCKqxQHfGi6Pbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3Xu38PaM0w9g02Igg36oNzzBkww6IIqM4FrZgbJ0qi7pu2hyvkHSwjgrnX60HOuUZRtjmW9PPNaS86HhJagXlgYu2yQy5tB5qRsND7IKjt8SxwM62OdV7w7igvFxJ6xZvLB84GN5Opc20MZTatO7d5P6u6_KYZzR-oVufKpng-9X3ypIv97KVzoVVQ9_YwH-VNI82O6fipU3UQiMCdNwRtd3Zl99zBEdXryP230aw0H8MPsEz1GEep66eVwwNiUP_oTGbVgz_IGkmUA3vfGbpQ-eE1-BIPjsAGvaYIaLk-N2cbWHBS2mtmgJiDlOPJ1Gf83-tSD9n4nq1UMHIvFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3iAlwXM7JDvQXi-tzRMOk0jNyDoY6oA535atH5OsiKdcbNrxtTVWGYv1AoUsoDoVXBN3ACg3-o9FbTaPyjV8ApzUd8upjHA9WzyExU1oCTV5q4GIpL0Wjn41Po5r6VwrHa8_J5jCrR7LXYDohnKH4iWd2h9BJ8qWDiEnfgwuruHr7DYZ-2HCviiJs_q7nFTCscQcG-JIrx-zqeJgJSVxgPMby4CsIlnKXpdzyxNv44ggpTr873WVyQTsgg77JvKkWc4Awpnh2WjY_09pC_LlRppUlaRYUd1-_Z2XK-1uI1B7TGLAomlpSQWOQPIu5FI78R_x8uqTGwzCoiFCwllOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fg1l3Vm9Ov3WmIoQufnHW9aVDZl4tGPohQ0GNgC-EmZNOUS4fjPY6OskO79WgcUJ0keF6d0nzN6SzYGSrLp-oR2FsdMMn3AmVogLaI8a-vMh9hUI_8oCULqrPWOkV00KwOCUYsv7BNg7qQcTR0tIx8ivhw-APPg_fczIF3Z41w9mT6mzLzzRDnFqED5isaSw5W-kAkG4811aIQk1swW7Bz-vdoik6Ffam6Aw9ucYThch-YvWjOjqadlmtTO7wbaNpanoVzQ2FEwakmR65aDIFWhQS_NJbQz4GTd3O1fEq8s7t2-JfiBFj2TfHCfwmDaLfCe5VPlJuW33AHrRPNG9qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fg1l3Vm9Ov3WmIoQufnHW9aVDZl4tGPohQ0GNgC-EmZNOUS4fjPY6OskO79WgcUJ0keF6d0nzN6SzYGSrLp-oR2FsdMMn3AmVogLaI8a-vMh9hUI_8oCULqrPWOkV00KwOCUYsv7BNg7qQcTR0tIx8ivhw-APPg_fczIF3Z41w9mT6mzLzzRDnFqED5isaSw5W-kAkG4811aIQk1swW7Bz-vdoik6Ffam6Aw9ucYThch-YvWjOjqadlmtTO7wbaNpanoVzQ2FEwakmR65aDIFWhQS_NJbQz4GTd3O1fEq8s7t2-JfiBFj2TfHCfwmDaLfCe5VPlJuW33AHrRPNG9qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdh2z480PppeI7MQIL124ldtEuYAcifL31nNc4iAowbnFCqmp2m8nfoJ4UHmNkuJqIH9FtrZ_onRxW7xGa2yTteO9sZinT3holYrvdZGhLH9wTuTH5U30A8ZaLtyC3i0XJx6JCjWqRbug1dkwMugEZehcUWT4NqelYA-8eqeGCPAQJpY3uloFT-291PEGlsABDK0NoeWWN-qcvff_YSGzUxH5qTFom_Ge-30JyoHZf1ocM1BZDkBSOzJB2S6lLXtE_SP9zVj0DKz0boooVTf56VfR1wrduQr06wqP7qRaAGJ62BfaW3-P98anNzGJ5dbhvYWeYUlEi9VzSRS1ludqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVjnzcJtVkfbadj8w-m9Rdvsd-MGMCFXoVX-S9-khJbaXhHK_pOfM0xP7fyvXCoee_yiVWhUyzOg8iSPC_CRSX1jRGv2MNFmVmzDrL4wBQ1qiIfcqgZN6AzwZDygg83zzLAdDfJUQZ0igaAQHOMvTC5zwrlqTqJOyjbNA0OgotiO8Mu8teS8diFaGi7g6EKKOyEaiVxyr89gP9hf6WEltxlstc-VBkFfRN1hmONqVFN2Viu33ETNtm3mdYHf4o1AFWIwFHEzwshLtyu3RxfkxszW2kk436GNJhrqmtKIUY4gklLOQu1JABCxMYTB8vgR72zVP3K0eWpppI_0mVT5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTqnV8hEJgraMBO62kI9935MyXQ_HNZ0iGPDDeCh-0VrQNWl1NphVG_itL_wU6bAo3TcrjMBX0-NMDTdM3QDEFAYqnDJbDdZJbOKxLAkcyfo_fh4lThZLfmQ5lfFIFbv2tDhWkMgNiEBJ6Ei99TQp36IxiZqKj0EbSVfAQ6z8HEMmP3TD88urcIZ5Kc-78NpirNz7lW4oLb3tl_D1fzDT618cQBEZsleQnMpbAw_Up7-ZQK2w9GcFAYYPjYEsFkQMgJr2XQkbFMxUyzXBhbQRi57u9sGMT2iZF75AibMEE7WdXgxypPbHWqu766JVI9YXKQzjgehg_rKcrOx7WFHcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JJPXeqjZr2psj9PoczMmAs6pRcdoxhyfXGh1YlqQLSn1L5Lt14dkmbDlwM_Fdqth863VnTgu817xS6UnICiSwEMnLXdE1OBK4gFZK7j6MUGK9oaqjJL6ymUzCHnxQW7C_f6gZjLacUlUuup1NWpSIFzFD-dMJ6_uUKEfdKwyJbQhH3Gmwyc1S9_M6H3Ynp7iebjV0M25zBHWR2hLoqxh1HE_vI_902nRkTub6kEq4vRHC4YHceT_3Pxx391tcDEN0m86XuFu6NfL7jE15emcUtBwB8sKMhiHuClhBe2JOBq0cy9SH_IcOm-hxtf6NiNIqjkcNZLrhyb0KIqhPszW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JJPXeqjZr2psj9PoczMmAs6pRcdoxhyfXGh1YlqQLSn1L5Lt14dkmbDlwM_Fdqth863VnTgu817xS6UnICiSwEMnLXdE1OBK4gFZK7j6MUGK9oaqjJL6ymUzCHnxQW7C_f6gZjLacUlUuup1NWpSIFzFD-dMJ6_uUKEfdKwyJbQhH3Gmwyc1S9_M6H3Ynp7iebjV0M25zBHWR2hLoqxh1HE_vI_902nRkTub6kEq4vRHC4YHceT_3Pxx391tcDEN0m86XuFu6NfL7jE15emcUtBwB8sKMhiHuClhBe2JOBq0cy9SH_IcOm-hxtf6NiNIqjkcNZLrhyb0KIqhPszW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RJM0DpvVFXQg-BGVCwqNlCAa61GnicGK9JI9yZDIrnh_rDYqpMBnodQoU89fH6G5LcMeGDZTnuKHly2zG7ze4q83hNvrBZjDYZE1qIcykVgwMQGO4GNX4HIcDICRB6AC8Rfvx69EO-MHuuTUV5zQCHWKTgNxoFHVG9DxvxDMEBDklOJbZNXvRs0TBVaUqENO7TByHSqP-7JRyKh4kdGOP-a35N8NgQYQODedwRbNX0HuaM9xVMEZDRJiZ-g4LXgx5_bkWtaeHfjI3VlSjhQu7oT1M3Om0eNMOyjRFQzD1H-rScDwMhFIuVyLjjG1gddVFQOGrF3WWEnDvzsiRHMjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RJM0DpvVFXQg-BGVCwqNlCAa61GnicGK9JI9yZDIrnh_rDYqpMBnodQoU89fH6G5LcMeGDZTnuKHly2zG7ze4q83hNvrBZjDYZE1qIcykVgwMQGO4GNX4HIcDICRB6AC8Rfvx69EO-MHuuTUV5zQCHWKTgNxoFHVG9DxvxDMEBDklOJbZNXvRs0TBVaUqENO7TByHSqP-7JRyKh4kdGOP-a35N8NgQYQODedwRbNX0HuaM9xVMEZDRJiZ-g4LXgx5_bkWtaeHfjI3VlSjhQu7oT1M3Om0eNMOyjRFQzD1H-rScDwMhFIuVyLjjG1gddVFQOGrF3WWEnDvzsiRHMjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=kMkC-pvEOO-uUEEZlVJePku6GadR19_eoQs2mTYfolOwXdGKwbW-C0nt35G5_9iqrt9zjyETNwk9wRU4FfvhPsVt_L8GHvnBbiofAZysqGmM6aoJalkYPYcMBJIdWQfDcUTkNV5u_BcSc_BJBuRqwQLSd-UxAmL02d-gI_rNRSHS_DaYkEWPwsKg3S0Xw5UB2oMqME7r3ba60mOeYDNMPlgPl9wGyvdJGeBgY75C76LDC8CX2_W6SsfBkruaKDstcJRxD-1CaPtwCgrIxBHBNRMfhdL8FYRBehKNqthxCYCJ2UPbWMV5fZ0dTDxBOgcba8VVx4fVWRhcQ2aKEzj2UZ_CsDv0wBs0AFQ__NFF8XQAa-XIlVoTxhADWLfkJVdezuPxh-xw8jaXbcMgtsrNlBIdWOPVhpU4_i9u81s3JGSLxU4Eg2PaY2vQEzA9eNZWXTXlZL7JSba8IaNPMENOtgtcVyJ58fITEqBE3HdED8IkO5IMUqzo9faq-uU1_i4yscUI7H1nLA1bgdQ7svx7tP-XHQSzgJ9ihm3YPm0Vsq9XO8abbZP1IhHLTJoeTXs0uefGchMHf7t7MNDnHQ7APnmB_de1UrpJxKPVdRdLbnDPaKKGbJ3zrpXhF92pvdAzOcBgiZ5IpthQnZeVAVxQG9gtvEwvMoUQcxy6O60E1qI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=kMkC-pvEOO-uUEEZlVJePku6GadR19_eoQs2mTYfolOwXdGKwbW-C0nt35G5_9iqrt9zjyETNwk9wRU4FfvhPsVt_L8GHvnBbiofAZysqGmM6aoJalkYPYcMBJIdWQfDcUTkNV5u_BcSc_BJBuRqwQLSd-UxAmL02d-gI_rNRSHS_DaYkEWPwsKg3S0Xw5UB2oMqME7r3ba60mOeYDNMPlgPl9wGyvdJGeBgY75C76LDC8CX2_W6SsfBkruaKDstcJRxD-1CaPtwCgrIxBHBNRMfhdL8FYRBehKNqthxCYCJ2UPbWMV5fZ0dTDxBOgcba8VVx4fVWRhcQ2aKEzj2UZ_CsDv0wBs0AFQ__NFF8XQAa-XIlVoTxhADWLfkJVdezuPxh-xw8jaXbcMgtsrNlBIdWOPVhpU4_i9u81s3JGSLxU4Eg2PaY2vQEzA9eNZWXTXlZL7JSba8IaNPMENOtgtcVyJ58fITEqBE3HdED8IkO5IMUqzo9faq-uU1_i4yscUI7H1nLA1bgdQ7svx7tP-XHQSzgJ9ihm3YPm0Vsq9XO8abbZP1IhHLTJoeTXs0uefGchMHf7t7MNDnHQ7APnmB_de1UrpJxKPVdRdLbnDPaKKGbJ3zrpXhF92pvdAzOcBgiZ5IpthQnZeVAVxQG9gtvEwvMoUQcxy6O60E1qI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=VYG564Nj7A2dFY-GAaCn_f0KuMCFOFF2P0V8mfY4lo7ACZqUUTm7Fuug1u49DW70rc67OgG2Dh_Gmt5ptBCaNPRbEJvQuOizYkHCCIpv3IJJ0Quno6l4kwg7fDxdWo3KgBqa3_tNkukksU8cy_j9O1YTXpmHflYfn3hh43UE0XBxbrPOBbeFriliHTndW-RyYNj-Prs1QhpV7b5pSbhKknK3jxPbO0ijtMm_2HjewzN54uJ4GkqGbNNkInXCffF1wzRx7K3LEVhe16ESqrn39KuUqyRBopZCyYvfHpepytW-Z-7rtLxy6-YGCwQ0QpMfPecJB0Mns86hO3VDjp5rw4sGX8P7YizbHxCmqT_5IaYfPATeD0PxJkije-ZnqqVeq04wXf-bpKYjmKImL1QsH1rSU7f4kVo2AzLVnExqIHkNMQPXKiP9R3IqdHgNOCkAtysw6pRiGqh5KpTP3OymPaxcQ8Z7A_yxYhN7sa6IVZuXxiqQ0ki1B5ySO4OrNvzEWb46u6JlPiDW-vELwdccGfzJ8ZFRePKE4rzLPuBM9CDmNDWktbZGdFWVhjOHFrO4NHqGEzQI_FFpdyOXCarSv56wzjVtDdl0Jx0odROouGlFfg0MipvBYebc7lBuN4q6oRchlZEAKQH_IAxXt0KZTc6VPt5cbWwfd64Md7uihG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=VYG564Nj7A2dFY-GAaCn_f0KuMCFOFF2P0V8mfY4lo7ACZqUUTm7Fuug1u49DW70rc67OgG2Dh_Gmt5ptBCaNPRbEJvQuOizYkHCCIpv3IJJ0Quno6l4kwg7fDxdWo3KgBqa3_tNkukksU8cy_j9O1YTXpmHflYfn3hh43UE0XBxbrPOBbeFriliHTndW-RyYNj-Prs1QhpV7b5pSbhKknK3jxPbO0ijtMm_2HjewzN54uJ4GkqGbNNkInXCffF1wzRx7K3LEVhe16ESqrn39KuUqyRBopZCyYvfHpepytW-Z-7rtLxy6-YGCwQ0QpMfPecJB0Mns86hO3VDjp5rw4sGX8P7YizbHxCmqT_5IaYfPATeD0PxJkije-ZnqqVeq04wXf-bpKYjmKImL1QsH1rSU7f4kVo2AzLVnExqIHkNMQPXKiP9R3IqdHgNOCkAtysw6pRiGqh5KpTP3OymPaxcQ8Z7A_yxYhN7sa6IVZuXxiqQ0ki1B5ySO4OrNvzEWb46u6JlPiDW-vELwdccGfzJ8ZFRePKE4rzLPuBM9CDmNDWktbZGdFWVhjOHFrO4NHqGEzQI_FFpdyOXCarSv56wzjVtDdl0Jx0odROouGlFfg0MipvBYebc7lBuN4q6oRchlZEAKQH_IAxXt0KZTc6VPt5cbWwfd64Md7uihG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=AK_XgS8dU3AQTtQyAb8PCAiG1r6hBdDQzb9ub-zkbFqClc8GC1EYXGwcFpF77Fg_Aa2ILCLrY6iNXJM8nija16auCWNVbt1QMVsqnzDNkh3Ig_s-uxAvEENetUXYGqOFExac4fY0TkUiHk9AZKIi27A-GgbIMBpDcWtmKuwnfOVlHg8lXF05wYcqSc7-naJ3pM_As3GSZRJdbWisx0YBFEBd_7IACp2Mu0WsEmnsVv3L1B8KW1dB5frQqSoSEcyMceo_YLsB6llX1ulN4BVDUS1dhle6N22sZJAcCYnfV6GpsSILLG-b1witF11gJjQsvnHdQ8EwNYwyjAKPw2w7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=AK_XgS8dU3AQTtQyAb8PCAiG1r6hBdDQzb9ub-zkbFqClc8GC1EYXGwcFpF77Fg_Aa2ILCLrY6iNXJM8nija16auCWNVbt1QMVsqnzDNkh3Ig_s-uxAvEENetUXYGqOFExac4fY0TkUiHk9AZKIi27A-GgbIMBpDcWtmKuwnfOVlHg8lXF05wYcqSc7-naJ3pM_As3GSZRJdbWisx0YBFEBd_7IACp2Mu0WsEmnsVv3L1B8KW1dB5frQqSoSEcyMceo_YLsB6llX1ulN4BVDUS1dhle6N22sZJAcCYnfV6GpsSILLG-b1witF11gJjQsvnHdQ8EwNYwyjAKPw2w7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsb9wFl4gb0yxUDeddtrRC6nMyVrw-adJ2WVy9tGgEwqeJFloh4AfZyNjTWFCN3ZVJICnT-ka9XCLX0wjj4TNq_uXFotAU_EkCI3zis3p0xoYITSNzFwQpzq0HM-qaYKbv25LIP4lcfCuiZVduHNIRcMbgE-J7ur39tLFgGnA4qfJINER5hyJSknCfqbEICy6-kiYAK444pWAZbutPiujRQj7wTYaeh0LxpMbu7X8iDTc2OI_RxrWlNeJ4YaGnv4ELeVpIK_wwERI8BBiHXngzyw3aK-I_d5sEpQRw8G-IkElc4eeTjyCr5hfSTBrJWy-4Z424zof2BxQbZBMVlU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Vbhbv5rpH7BkSjeL7N1_BmPYjN0QNgQrrrrzwALVd3qtj3KzApkwmjAcvt3yMm6zB2WIl_cPzxTD64srNrhs_nFMQf4Am08KPfOs5zCR-nEUeLAc8IJIfpDUZ_ILiijrw_9DZsXWG0Mfvdw-u2ydoz6kL-ihsdB9BZCrYmlJoZ0tqY3N8QBCKNYXRHlVKgY1H9VTXVZIcQ79h0Ms6vitZngCabck2m32JQzjrRbh3Y4MrTLZ5O6NkYJASVBMdU09IDyovNi1kM2hd2rsRsLww_fotWNN7I1j3fWNeOIfBqbOcm_tMIdpev_rvw1g_LgZsqwYIhF8PmFJ9bJUTWreCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Vbhbv5rpH7BkSjeL7N1_BmPYjN0QNgQrrrrzwALVd3qtj3KzApkwmjAcvt3yMm6zB2WIl_cPzxTD64srNrhs_nFMQf4Am08KPfOs5zCR-nEUeLAc8IJIfpDUZ_ILiijrw_9DZsXWG0Mfvdw-u2ydoz6kL-ihsdB9BZCrYmlJoZ0tqY3N8QBCKNYXRHlVKgY1H9VTXVZIcQ79h0Ms6vitZngCabck2m32JQzjrRbh3Y4MrTLZ5O6NkYJASVBMdU09IDyovNi1kM2hd2rsRsLww_fotWNN7I1j3fWNeOIfBqbOcm_tMIdpev_rvw1g_LgZsqwYIhF8PmFJ9bJUTWreCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=n3v-H-1Hqh9U3jKL9WEToOb7ekYLjvJ6vDhw9v15XZsBhL3_uThBRyBIpZnFRcYxUWftCaO8FceC0wsZPmds6r1KWK3FEoYCzkX3CvgQuiVsEULGb6BDN7iGVnp5Xa6kdzoybsXloPZBA4tW46YV5U87fqxztKkTmvs1VgtfMrw5A8T2IwmChP4QWhl9i5CY3KM8VpMGqlH9L1jWQGl7fYvf2zcZflqPAJD6t0fIagzHsOWw9LRfECfjep1NH1h5veTYizwPAPirsiZJikhbgzFSBnYSEXyAHtVulrRmswqEBlEoM3AtVmdKgoikNybpeNsGZt1KLdiEz2p2aSFTpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=n3v-H-1Hqh9U3jKL9WEToOb7ekYLjvJ6vDhw9v15XZsBhL3_uThBRyBIpZnFRcYxUWftCaO8FceC0wsZPmds6r1KWK3FEoYCzkX3CvgQuiVsEULGb6BDN7iGVnp5Xa6kdzoybsXloPZBA4tW46YV5U87fqxztKkTmvs1VgtfMrw5A8T2IwmChP4QWhl9i5CY3KM8VpMGqlH9L1jWQGl7fYvf2zcZflqPAJD6t0fIagzHsOWw9LRfECfjep1NH1h5veTYizwPAPirsiZJikhbgzFSBnYSEXyAHtVulrRmswqEBlEoM3AtVmdKgoikNybpeNsGZt1KLdiEz2p2aSFTpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD8i6Dg0CbBHQZOci9kocG5fD1EcHOIJXkiy4oT3vTY-XFw1_AN8WjhRS-28vYzDX3uBsIaKa6KcS3YfD0jrW7gw0s3cKpyGfugqvsE_4QLSS7hkTM-lzaEkA1fVvTGKyLZD0oWAYa0Eoi6HMcKqROhs_w0y0fPFn03I-AJRNAkz6X5OIZgggKtxpLLcDS_Qsg7-SaD2ZCqy3yke7vzVp7z7kL4YFnhAhf1CBid2E4Wd4cCcG8lkc2unAfYhiLuPCpVqMDkMb3IY6KCyKJDcNxzOHrOnoALeB5N_0tDdI8-oVRA72A8dCKykz3Qj822j6J4u3ZiyjzrJlEfoOqpv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ViwE5u5t2reZBDzKJG9MOTJGgXvpAjsfAmTPxo1p36GqRKGay4rL6OCiKQMnf1MmJjiDdvt5E1v80foLz43lc2x-Xa6z-xrECKWBikofyQeQCa8nnEmGtQQef_4f8FzPP1BcEu67QANFELy47DR6VV91RucGWQ3bRIX4UY1elMWuAzKrSb-9pC-p-Ez6vpHfRCuY0bLPOevHJK2O9794yqUe-VC3r4CjHHYm7aZc7Gwz4POpQ4pUEn2rbFR2Kv7nAhP6nSDvQ3K1LSoC3P8QJwm4NOk42VxkSLqIIvLuq7NhhznFQXXmBf63syMB7ZOgF-6bbBuO9_J2m9yRbMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXbofFoIUElEgtjVgXIBFm4dN355Y33WflMji6IaRxBbEU8Kmv0ks6M_3EUaiZgWiEJ3gR_Jaf21LnOhFxZkH0zTOwz87jwmyaLbC7e8HP6PYBuHcuGSHnwxZrhsKVfYn5MqxoJaQ5M6TB7zA1nOzCqe5CiaEXlCjTAROy1F8mSgyuNrHqWEzRwn114DLYF6RfSqwYVETdiw3tfHV62mypqxNXqvNvVgOhb1BE1upjrkqvEdb7I_R4mYT3VxWOR103zSZvQK5DKOXqXH2gZDqdoFP52rD1r7-ai_Z-gKbKj_2M_s9IoKZ4YjYzaK438AUB3-uung2grXpJ2kGPGlrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8Sj7VpretVfLFNZRl_2_2BkKLDdcsElOGrnUBMnVuRrJhAVe9hKIExQ7klnDAJdx8J-rH68_iJYg-RizRXS2giShkYUOJmU1MMyysrDJiNEcNSLGLEgurg2U71k6N03m8LyuiPhhSVfqahDMlvBeRSIMCgddosPfoyxDHjbWXGJEP7o94oRi_4mxvL8rnLfl2Ys_FSHvP9qywbIaJBNUYgFPc7RdAWYgmVmKKW7UCfQz7DzIQTANUH_fPun7otyxUzn4Rvv0zLKNQ-AYIuOHsU1uwwx8wmzhvCpX_NwhIRnq6Zu8_6zulhYpVcL4nWmIoDo7jnj6UdVSPJ31Yd5Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3yvV0FBisk_RcrrI6aiBwFqdT5jZhn65MGOaLgJXsk1Hou-buDSsoMldLMK8hOavElueWb0e8K-oIEMgBGTMqYkBXvmOJIKhZchUJ53VUart5oVtOdbT5rvc5A0Xxhbpa-_P7e_F_9SatL3IPkqx6AeBROenk7bX7iYRNTYmhNQy0d8k-4ScWaxD4SYkhV0JveLxujF2M3HIlvSCReCheewyPfhweeVN71Mv_en7v4lxfSe3KeaBs2GeHBCPcQCPv8aEzyT7MCNqCyFmBi6f4WwhFAV2SoYpBit-_N2iW4mpPBYhXfBHho7WQ2Q8cDYqEIc9VD5wo0WzJp8MtRaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAAldEVMEFaU3ItZu259afFs5apxAfLx1aVZNVcpdmuqz2eYopGdrNFiME9gCQhh4UYwPeb_5xzAyM3oDI_zw48rTYOtVABfDZ7OjjXDpq7u-X5V-WkJoEb5CSMUDiaL-_8qJqmJgSjFjJh4uHBZIZRl360Q6RUx3hjjpysTwoW2_-BJeeRri3cw5Uw2C-yIta16Mv0zCKHBf3HRn6dCtpb_HP3FuYmeZnTMDVAOLxobmS6XR2kDm_NsWgD98_dME5MGYfp3591K9l9HBBvR3GZaqsxwdIvUBeyzaJbypbAipr82Y61Vz5hAziV08dyNHCYndNy_0DrDKDEr7LUUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc2eSXuy4os57BxhGLwAdMmFieFzL2qtLRk6d6V65RrF_C87kAeyftDLRTf55k8_ROJlSJt_xKWvBjzta81HHZ5E7v4L1UAdWW_UHLTG6BIczLyG94yWf0k7irfuTIzGm_qqME28bmbvX9HkKwBLBG1T5NqkQCnzVLPUMIt_O9O_9zMOfSbfu9RGib4jCWpC7Fk6hdYYCuc3WUgckZU7fqyJ0IJeZ3k_M827Zv86DVriNgyAG5vY8TwlZ3tnDpGuYZJ5Ityy5DIadk4j_5c9ca4jQZE16VgZEjfARN9aSVSw5v0cRXDwFEGfgTATMt9Uy936u7wl-wNi4tpP9urzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upEca1z7D-EKyCwWR1Ra_NID60Gaj12_Tu-CRT_bPOWdnxaF_p0jsA04OaGHRk-HwKNZH97GP7Oj1HCdgY2dAfL2G6Z7BpXXjkkMkpEKM-lpwyPaTuNG8fMtmVR7mYz712OHcp_L5_wZ-8Xc2O7PJcJwgLcszKTX2RB-T26umkKYVpXnLUswgCLjhbbsJeXiXygMO8FyV33SnH1OA0jeVnA1bUmp6NSo6VNPPbFE3Cvkr7BzoKyJCBaLmYMsvZwlMVp4K57QKr1EbdqiBOQgZ7-mxT3A4YqvQhWcBzoQp2mkKWLTSbAO7rTYFvuAXdx8g06czA3gioNjFalKid9k0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqrLyXN96cCr1DPKEcT2ZdnQ9mUNJQ2xCpK88zVc4n4vG4m_-dNDeYdOinxrIRmY9FNPiJEYau841qMBkMEkFSqKMVia2kth_XehmeNR8_M7Y_dyH1JW6LWJs70mtr_hvQ0BV3rhPjFQm_VvJxrc9qQ595Hyq2GRQQ7Q-CjRcD5HP1YI7OfClmQVi3Bi_FDLO4MepGgOx2N6oe25F3X-ztWskzX_eQU0J4nWV8pVmqjzDAGmoiN_kTNMkXKyLN9fPpwehwX8r8JvVkEeyGDVa6CGuFSfLHSPIq1tyU115BhW9jqG4rQ9I-eQAWYDRTTyO7nH8rA5g6HkHyznmNlxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUa0bs3Rchd8uUpjhXgiw1-fMipkP2USNopxerj4JiFSApXc1zi8GLNcA7e1PY4KVyXT7YMhrdbmSuedQqiUHS9xUMxSzoljckQa8eyZ5tQJDlNUDHOmHrOFcn7J_rHa-LpuOUuNQLGqpED8IkJ0JJV4gxmqcD9xSnpsnraCf2Vnuo1p-e5aLiZBi91IbqHKbb1N96vArUdCrsn9lwuvHPOWnsm8i5i0ZmFg20L3pvGSY9Q21VNmqiP0ipamC0NhJfzUh5X9Y5HbPoEEnXrDuioiMpPDJB2Zdu6jVtpoHXjTdhIQIJV-f8JohxFSXpq_HErx5WxF4tnraiVvm_wLDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r6oPoXDpZ9jP8zxAYZpeZde17w61jzdmYMhU1_hWwpsKRN5FWjdUfwcfVZ-EdZ1zxp7IUspcSau-e8q98bY6glHClThHnQNE7fXF5h0C1roZQo7tgFiiqs4XQxMpTCjx4HSTs1mDl9Uunpi_synxDaAm0ODLWciLxjzgTv01tE7xEtko-Wwz29rjXoFD5-hb6nilU3u4ypW4AvODElULR621clMFPDp0McADkqTeGdozP6NIZ5w997jZQujxrXVRSEj6ricnRdgysoBh6O41uK6f5h48HPb3ovhaeVRozKwV0tS3LyY1qsW0Wpmgxe1gRYVamAK1lA94R6pkPiihnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r6oPoXDpZ9jP8zxAYZpeZde17w61jzdmYMhU1_hWwpsKRN5FWjdUfwcfVZ-EdZ1zxp7IUspcSau-e8q98bY6glHClThHnQNE7fXF5h0C1roZQo7tgFiiqs4XQxMpTCjx4HSTs1mDl9Uunpi_synxDaAm0ODLWciLxjzgTv01tE7xEtko-Wwz29rjXoFD5-hb6nilU3u4ypW4AvODElULR621clMFPDp0McADkqTeGdozP6NIZ5w997jZQujxrXVRSEj6ricnRdgysoBh6O41uK6f5h48HPb3ovhaeVRozKwV0tS3LyY1qsW0Wpmgxe1gRYVamAK1lA94R6pkPiihnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTeCoPZLXgWdvllutcSMg5JD0HFBgKifpWLr7wyoatSq9pZvvUuX2S1IxohFAneA7LixtgDXRl9pGlPvu_QVpPh9uUkuteEj7XuSwcquzAn6Q7KyV8OOF4jtBewnjb_CxkHa6V4o8Uc4mfAnDUwg-DCZDCJM8UaECw9kFrYiWQbkPVnMBIVlYeTmyAL56mrgg45P5Kjk6CJXl5v-bM-35kRTKfTPvR4NA7iZh0qhe_lqZG-J09diVPwuDSjMcVPC83CfskGMZ_sw2h1vl4V0Vh9RHTOJGynGuqU-5OqPym2lnzqoPz60uo73Il7IROSz34g6gwHpm3WEbDv1fM9reg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWIJ5QUF1mnovP3BqdaD6_1vxd5rrhU8gE4MecJWsPzUaQM4CuJFnyW_sdMt8bEQJn0IICjC18o-a38Bk-Zhwl2xoI1toqL3v1qIb-Do-l5K9TPvQh1w8Zq_-CEv9kUoqmHY0p9HV65ow-7t-NgvRlRDuwS5L5L8OROHHRf5gjWQ9GdF5o5cN4QcH9nNG-nIEi_9qkhPz5YRscwKtNWVLO_gelPU4TmFzY0gIE__7a27mi-APkBwClEL0U6mFC2taUADEoJKNz_ahG2q1qxRKfR3HD1xYJSDTWz9VInigwR2ofjEkYdbh9ZwuN8d6UXRufTqunPNpp62WqLtLVIfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=RccB9unXd-C4r9BRKadLfcs44ooB4FyuLntgxTWcDovafhRawUS6QlueDV9cDDLPXdJvKA9_fism0ZtAc0Emo3gpQvGi3q67IIXEstDry_tuAQML0fD9gxCgLraAEVqmAe-JkReLWsBaWh7DqUgcxS944VauquaPbOstC2JqSMvkrRASdcKpTmW6L_onUvWZqnpGcXaUH4gajcCzerP6vsqDywkMvCoByeCypIF5yhBwqX943kbMDeqWgngrEgNbfMKcGVx4eagiOFLpodKupp0BRYpzsYxCMeiGc0HprvbjeaKu6zQ4vm6L46mh_D8D_9CCy3ihQQvfNJ8YRXyD1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=RccB9unXd-C4r9BRKadLfcs44ooB4FyuLntgxTWcDovafhRawUS6QlueDV9cDDLPXdJvKA9_fism0ZtAc0Emo3gpQvGi3q67IIXEstDry_tuAQML0fD9gxCgLraAEVqmAe-JkReLWsBaWh7DqUgcxS944VauquaPbOstC2JqSMvkrRASdcKpTmW6L_onUvWZqnpGcXaUH4gajcCzerP6vsqDywkMvCoByeCypIF5yhBwqX943kbMDeqWgngrEgNbfMKcGVx4eagiOFLpodKupp0BRYpzsYxCMeiGc0HprvbjeaKu6zQ4vm6L46mh_D8D_9CCy3ihQQvfNJ8YRXyD1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=I4aAFDQHyNeQHEesUxFtffhE0xJI9HJF0kRVCSXLww3VJjSpIXEgQH-gI7kiRowZkVu79lWg0PvhfG4XTupwm9ySWpVxzJ3QuTEsQBBpVOksGZ2V5-Bgv6HqTxWRSFT6wL62Kcrq3w6v8c34huJ8DKFxjIwkKc7aYBgfVo0jZrop98wbDE_riMqIsbAoFJpUAQZt-mLNYhnikYvbfN9DqpbWornnrnZzhBG6cxse4sNBF9I9Bu5-TOxgEXXX9AY_ZRoJ0JKj7lA7-6vB-CwriB1rHwAbkgJ0FFA3TpdsiRmr3lEep3FqI_Xhn-7JuzpQm5WpNkWlIzWqqI5ndy2A7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=I4aAFDQHyNeQHEesUxFtffhE0xJI9HJF0kRVCSXLww3VJjSpIXEgQH-gI7kiRowZkVu79lWg0PvhfG4XTupwm9ySWpVxzJ3QuTEsQBBpVOksGZ2V5-Bgv6HqTxWRSFT6wL62Kcrq3w6v8c34huJ8DKFxjIwkKc7aYBgfVo0jZrop98wbDE_riMqIsbAoFJpUAQZt-mLNYhnikYvbfN9DqpbWornnrnZzhBG6cxse4sNBF9I9Bu5-TOxgEXXX9AY_ZRoJ0JKj7lA7-6vB-CwriB1rHwAbkgJ0FFA3TpdsiRmr3lEep3FqI_Xhn-7JuzpQm5WpNkWlIzWqqI5ndy2A7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXEBlXvpuubmO46bk1hHFob3dPC9_YbJ-BzlIL86PT24NMgY42PqU0HbFEcrG6AQGybvPDvHiSbHH4OHkIQ_6qGWcFIOF9IJM6KnxlLjGaGsxT26Voz3hOhcBoRcc1zikJHVjvwy7B7DGnI1c5RARasTgC0Idt5fFZNR1oRMdzbtkmduZAsJrMcEPmuTYmZ-1Z-FNZnUomtZvHuiUW9XtPIhLaNW0ykpgMEebOjVJZQgPvWQSFKWFaGInE3izH-yqdpMRGTPZoltxqXCwVVBllqe2Jud0L39Ck9hYg9cuKGzheWb9F6ya91zvgGtvQvrebgfUs7auAXIMyZOnRRajw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL2T4eGV_ei0ZxVg7RrviJ111z_yN3EkF_V53vZtSUHoYkTmruyspPsmmkg860ngVicFu4XXlEODLHmsK68nUXjMEUoPGrMdVZ-FdSH8d-1_ix_ovzUsOXsJJSjy3591Cq8BvTPfPEiJwB7saU6GZhhBaUV6PoldAfVzEwvMAIOuePurrEoUPvPIOK94E1AvavyWOlFaIcLEE-hfqHRbq0RVWcZGBFMMet1eH9WiKEwSnhHwlOvz69WqPGZSWo8OFKJI7aJFbvrmduEWJfRcvC4dztRz5wnYm-DuepuqwK_zJcBO3HVNVJ6Pkvh1VMDGblHPs_Zpus8BzIDOobTUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeHhXTnFtFXMxcD27cqDSw3RBIS9959LzwAy0qTTvjhKhgp_wjRrIXreFCls-l7jQAmxa4XTec0mparhv25yYlvpTqV5nI4mLrqgwjo6Stq2uBrpNFoCs-ooVnYD6hMP9nzDjEs889F1q2oe30PUdIISSSd9sRaHV10joJRLF-npXne3Rj5I137xOGg3SlTqjF3cI35OYaoDxENdFa3_4aML0euhqBccd9WKSA4ytwW2I-4V2wKJQH2zqQR9xhcefRybhQELpUSfoxcndY8PG4F9rvk0h6xooJxT7QtIr-aJ-nU8PmACbXgeDxVwBxfcNI6DazGw6PWpqoucCBYEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtKewi1F7syOBuOIFRKn9ZabxkV4XTTGomFR38SfK52kC1n49vCT7w-LBuQg0dXFIidalL1TU4g3VNqcoMt7n1aUP724UCvLg8RGau1Habj96Gti0NEGuCXm3lHdzkS4Hk8Eg4omqPJ6woPvrT1m9t1BFGlac4OtF47bEKKuH9K5-6ivsGo0KBZOcN47-GCoUV62QODgZRl51lqnFjwjKv7cuOOxuH2nd2ZUlT0aB3Kg9asONq9UJIPpZH8YPLkSybgSfO4L9TdP_hENtWHNU3FbGVys8WrUoMGhZpTv4-XADnDL-S0dS3IXyuFaGjTZvnK1xtNibsGBjawmoZPQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Yovo_89p6Y6uYnSs6w6l-foOZc2meQmJ-X-wMgv_LhubFAeNE_YQweFQouwDX_-NkwVJFXGRPN2jg-cES8lvDWYYjjOnyCMDlRjrUjedOQAlzkMiZFu2qeBJJ149ec7l47MnANfWLwKVW-5P1IRTfqHleLZJlc5OhkMljx3khVbwsdSt63C07D6GZLAAHy5FO6VuEOmr0FpyLAUHtioyvm3PqLhsv01vbqFmztICESWNV_jGa1MjRAgYlDeA8sKcD8jnsire2LgKcUUy_upQVoz6bQcqGA-4MjzCSN0jUD86nVhZAMAjAE8NjhYJYVBt3TBMGPV7Oyj8Uq6Uyq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfCSNv46vk6OiDFUwr99QPCd35RV2r63C9ymAnkHYWDKI9e-KNpZ0PR6usHdzhMuxaUG2PJOeFz-9MvDbRkiIVXzmK6y_elR9K0ZQsvdp8EWEJNrqUh4YZgdwYWsGbpXm7drScT0z5XArE4J6G02LxnddNcPNX8gvqC8AmncxKYILpaxwILqVhgvRDDm2xDkzkp_cvtULQWTkt4IoZqzhh-7-raJQmt0BX1bDgpna54KmlaC1QSiMxikG7Pl4dX0xAjjowotIn2-0GGQBWrZyF6vgMVoDGd_rRTIrVVM1W0OCa84ekrXCT6OdOszv6fp2GXOHsSARNqetkLEian5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXg8AeguJCCqObpOMYSd8gNKtwViS3-KxnZB_i_3QJF2uwbZMTWU5O2tCdUcxCVcjzkiblksO0by_XgIddZMnIBuzXY7Q7LR-UXmJspfsUgZykshxHsC5-RudbEm1ZfR8FyB7tlzroxdmiVayMm9_Dc2QaW19vr17z43q3uasyyojqvaGy8Tp45OVMb-5g6Ti3ofQw1tjZJ7cyrPe3OBRpL-MJfzgHlwlu4QAQU5vBVdbUar4qMfj3N9SwVM9o99INOIpC3rRleW7exeRiltfbGEEFU7-zul8m78jKPuILBh7FcZqfe-mM_2XS0Lt1U8OeKMXy_XiilE0tY9QzmuZA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=BC53p_Pi2NsNUNsxs8McRe9NCCelc6Bn5Aihxhn-oCYG3A4MlxJCAf9wEFbNMO93c0iw_GG-QzBQ3vZi7OSFkyumNPQLRlX9hLmAn6n5ULu9S0i1LE_F1dFvBYxXuUfLSNBSy4NOUcNeG7NsE6zgsdP-0oI3YUATTjx1d2LK66C7nkkuIliKrtid5Z34xQfsue_WUvqN1qHfyjTYGYFoc1ez-ixH2fAMxZR0vA8oIRQ1oGE2TYVEK7jJgskGGPe5QlORtExFLDy0NtXuCHatUmwhV0bNwRc9abDFZODjPnQX4du0yVz4hrafRZ74TAqrCGm9vzJsKgwc3H6IPPs-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=BC53p_Pi2NsNUNsxs8McRe9NCCelc6Bn5Aihxhn-oCYG3A4MlxJCAf9wEFbNMO93c0iw_GG-QzBQ3vZi7OSFkyumNPQLRlX9hLmAn6n5ULu9S0i1LE_F1dFvBYxXuUfLSNBSy4NOUcNeG7NsE6zgsdP-0oI3YUATTjx1d2LK66C7nkkuIliKrtid5Z34xQfsue_WUvqN1qHfyjTYGYFoc1ez-ixH2fAMxZR0vA8oIRQ1oGE2TYVEK7jJgskGGPe5QlORtExFLDy0NtXuCHatUmwhV0bNwRc9abDFZODjPnQX4du0yVz4hrafRZ74TAqrCGm9vzJsKgwc3H6IPPs-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpK64EvBNNmlBJPG27iVF6LCb3tLj9moKlgJMaQ0Ja_JiT8ZROWKhzPCCCcpUYUX2e_5G325LlEodn7qtgn95xjCKL1gHkat7ZzsBipLNwa1v7ZGqhsQxVAQe8Za1BAYeJpuaT36uUzg5qHr10GA6BHn01OBjA56Ni-Lc3QRwyARz0rugN75CwzsLvyJxsCI-3CoVJP7rr5K9kkjZsgbw0TeAhm3CqI2RjEnpxz2DhvRZGYFwYF_2ShYcqhd0qHGtusqwvY4_XIaHFfLmTh6USeVet29LzxDkvKbLvgkV4YO-1qS8P7yaYWnVoLhnONok6tfjmO2OpYlrGWp3ukiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=c1ZK62kpPRSJIDuhQbsEpcY02R0ShQVrIUnA6Fti-m7DyqFMRBJ4tSkDdXMl4aXKHBL3iDk8F1LTC1iluE5THdjQjwQhVeRyD9xStpuffNtbz71Ct4g1p-j_baX4q5pHODQLUqO5Dz4aVx8nbKkMBb9ZBBju38IAD_ocO29Em1zL6VAiuQy7abu39CoNoryJx0i10WoXLodQ1hKuoPrY_i-2JBLo-8RiK6W6qgeSPg-uteDBiikDSW0D-5GDWqjeNdWphoatpmAvsm4WhJG5rsxhVak6tPuz7bYp7D1D_GHuyp79RM5wcHVGBKpF5ek8fhPjtv5rr-EO-cgZ2UUM3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=c1ZK62kpPRSJIDuhQbsEpcY02R0ShQVrIUnA6Fti-m7DyqFMRBJ4tSkDdXMl4aXKHBL3iDk8F1LTC1iluE5THdjQjwQhVeRyD9xStpuffNtbz71Ct4g1p-j_baX4q5pHODQLUqO5Dz4aVx8nbKkMBb9ZBBju38IAD_ocO29Em1zL6VAiuQy7abu39CoNoryJx0i10WoXLodQ1hKuoPrY_i-2JBLo-8RiK6W6qgeSPg-uteDBiikDSW0D-5GDWqjeNdWphoatpmAvsm4WhJG5rsxhVak6tPuz7bYp7D1D_GHuyp79RM5wcHVGBKpF5ek8fhPjtv5rr-EO-cgZ2UUM3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=BqcQfSHyRTivO9Twk9NWwGjO_X7fGIP5osbOL8PS1UFV4IzZ_UQH7Fyu-45UjZwGDrstSRJRWW4cTFhsK1rwot8FaUO8yx9xZbyjMKYiXZVs_Z-0i-C16F6iEBZTiG_P3ZZPJvh1TQKKnnUImEISAAlyOnKkPlw4tk-9c5iMnOAN59cQHEMdDmJwBU6Uh3F_CdrM9JDnlcylDcVOH9-hX_2K5-WjVfsN4_IhrZqghZg2mrJsljKI_9t3lN2_b-sBzu0KhbuDWDUvry2NLJ9JDeUD3FPQ0FN8sgnuT3tI8LyfLy3nmeZQq_ajgDVFbZ6Pm5tGeFVFfXtk1vj05KSoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=BqcQfSHyRTivO9Twk9NWwGjO_X7fGIP5osbOL8PS1UFV4IzZ_UQH7Fyu-45UjZwGDrstSRJRWW4cTFhsK1rwot8FaUO8yx9xZbyjMKYiXZVs_Z-0i-C16F6iEBZTiG_P3ZZPJvh1TQKKnnUImEISAAlyOnKkPlw4tk-9c5iMnOAN59cQHEMdDmJwBU6Uh3F_CdrM9JDnlcylDcVOH9-hX_2K5-WjVfsN4_IhrZqghZg2mrJsljKI_9t3lN2_b-sBzu0KhbuDWDUvry2NLJ9JDeUD3FPQ0FN8sgnuT3tI8LyfLy3nmeZQq_ajgDVFbZ6Pm5tGeFVFfXtk1vj05KSoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLDnBVZdoynrJCDFZJe8WDB1EYDi_HcdLbcKV8v9AmuFkC5zjDKmoX5-k0YdR4NipQXcuOmQEjqV01LYOPwl2E1mZlNVIWWotlx9HUPk41j1R11ytz9jJCoARQE007l35BeZb9Y1QCAJ9USuS5JEaWBcC3t9ZCbdppB9L3ODvB14rOq_dWfBPPnVsFVSJF6UDnBk_OlY9ZLKPQMusgpENuuNgj3TZ1-c0kV1Nf2AD0rIRuKlxudNxfPMYXV10NFkxKnwZ0tXXGp7aVy6AJSkT1ShGfAet_7NzzYZiqM2Bbyzm_abPktlp9vTwFlsjGKSjvTCZA5EelSZE9X2Yg3gag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVrWO-1gOHy9EpPVn_owV6z_0_1A_XWPht6NSeQrrxB85xKSEfv81IK3YKpwcyjmsfOk5aadj-ndo1RZwHQ6hGCgHu0q8INcldojUiDsXwYBCuRGjw2V2pG5j_Sq8NYIMZHAUZKxBwBurhd8l87-aAO2Rkl6BEdgExY4rejRiP_FARLipZTg-_wJDwby3fFj1coEfGQcNFGqv4qAwbAznjIVSAvJQV7DYMilrIHjr0HuMLK_2VIEFhq2hB8f1o9C36VFUIoDpCY7VabDpV4L5synXXX3GfnBQyYrG9ggEaoyDgCQwruWXA26Lwtn5XxmO27b8GztiYb1Vk6zpgkaSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=WXyhYzfpGs41UsMXyN6NVo3h9t6ddqP8szULAiBDtTjvYyvuzNSxeiMjfhG74_2CyoKg2zCZp2S8aWL4Sf5LTJUsrhtd67u7iAsLBtoqgPLtvP68AUiQB7mDXLk1sF0ONUpnUStGoNVF2rFKLaTMhxoZ5o2fB6dDGTROfcXi90VR6W9IAmx2su73ceBKIL3Iin8fpurVixMw89ODErR5Mo6tbiKfuFbFzIzdOo4rOCHefDCHNe2tvXp3EjqImSSbCvYCOg5fhr11tTiKOeSMmSMAM3RhcnHDOyzS_3Ou0l1QCjB0bzTi3Eo40PbZICQ3NnU27k3vFegfW8CDGvDH-BMN55hdKvKgowWYFdHCZM79vVTwVfe2vipR8_AYbWtva9zhGTD9czaf71gk8wRfm5IyGtTJ2LOeH2fXoiN8fIGdZbfcogFb3SQQ06VvzreuewuuepTo6dxFM_jIWk333Yo7IZ8ap3_R36SV312h4epns2qK3N1Zouaa9sLWhXJWSqph0RnxvLCkYq5Dusf2k1CQAJjjepNH9PIUBgC0IIwRBhSW94VKEnAKJFW-jxM5sap922WchVm8-fg_3tnpWFOjhLSD1yEdF3EloNUMb367sHAhwhhpVf2y9f1Lc-z3h5VBdhVc8zbatOe3u7mS65n8fjMw0mGW7syV6mnNRps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=WXyhYzfpGs41UsMXyN6NVo3h9t6ddqP8szULAiBDtTjvYyvuzNSxeiMjfhG74_2CyoKg2zCZp2S8aWL4Sf5LTJUsrhtd67u7iAsLBtoqgPLtvP68AUiQB7mDXLk1sF0ONUpnUStGoNVF2rFKLaTMhxoZ5o2fB6dDGTROfcXi90VR6W9IAmx2su73ceBKIL3Iin8fpurVixMw89ODErR5Mo6tbiKfuFbFzIzdOo4rOCHefDCHNe2tvXp3EjqImSSbCvYCOg5fhr11tTiKOeSMmSMAM3RhcnHDOyzS_3Ou0l1QCjB0bzTi3Eo40PbZICQ3NnU27k3vFegfW8CDGvDH-BMN55hdKvKgowWYFdHCZM79vVTwVfe2vipR8_AYbWtva9zhGTD9czaf71gk8wRfm5IyGtTJ2LOeH2fXoiN8fIGdZbfcogFb3SQQ06VvzreuewuuepTo6dxFM_jIWk333Yo7IZ8ap3_R36SV312h4epns2qK3N1Zouaa9sLWhXJWSqph0RnxvLCkYq5Dusf2k1CQAJjjepNH9PIUBgC0IIwRBhSW94VKEnAKJFW-jxM5sap922WchVm8-fg_3tnpWFOjhLSD1yEdF3EloNUMb367sHAhwhhpVf2y9f1Lc-z3h5VBdhVc8zbatOe3u7mS65n8fjMw0mGW7syV6mnNRps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkEozfP2EHj_2qwn3vUjRB-WusNbXCAkVXI7NB6hdmIjdDU5hYYx4UCNGi8ax5r9DexjOeiD72JL_lza-Wlytle0HjkXdPj3w0f-byJjNlzDzedy9ulJNVHk1tVs5FZUfGNmejiM59fJBx6t7kJP28UTZzkE-8D-bu8KxilfymGvVovJ5Wtx6Fb4jUZfeJ2sPhVX6iI7glNZvRMDlQvoRMrWe-ApeJcXe6XLQfn2GQK__KhJizlNseEstLSItAHOVAaaRZq3fNDs9phIaw27_c0iAw8UxQcRFADRlpqrgHt2H3xILay6J364t7Xo8MYpp8Uv6_C3N_uCjiGM-G2dLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=e9ztVIlN8tSm-UPEQ5Pf0rDUyN9YWbaVzMLEW-dL8VRt9-jOeII55IO7Zc0H_RrC71NuYVNs_D0aUbw0EBcNx850r2_nHrm2Mccl12YLyNo9qO0MJNG_Ldu8_SHqJWNbX-yhXMrxZzLQ6AR5fKND_JRZGkGAs_GxFejElHY5pUm034mvsVUZNyfgSI_o06-EJWqYHZEsLzKRyrHZkFN3XNtM2Qu9uEdxusAnyWX0_ybxHdvMJwLnR5OvKnheqPMSkOLY0yPA1V3ZTMJZ0bIgu_leoQ6cZxMToZIYo1QaLnnNNUA5YtCIvalX6Z2q_NRJtL4uvpDMVzbM47AJqlsRgRFv2KfQAdDK-TyaIUxlVozj6M-2hL9TrER2jbKCylbWbX7lqZqN74YpIb40EvqDXBueNYMIG4puw2pCWgPsTzjYJCFlDMg2Sx-_S73zzh3WBQtZyC5nBEhTjpaT9TBgW2Dytc9pknk4dLKolfnQQcIIn5qRY6hGAWlcTqc8933BXv31cRG05w12ERYxSp7NE4HA7n0jFmEkNollCK__uHtAtJIyr4T_QUG2TtzHcobMe1-Et4QAaNMyxjjWFZ4KjkVT9vSulU9_RBGvA2go2bor746rS0YnBtSkoTsY_Fc1QSRx4dHO49Ej4P2vthp9HbAAgDsnFNKJza5TvVl_b1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=e9ztVIlN8tSm-UPEQ5Pf0rDUyN9YWbaVzMLEW-dL8VRt9-jOeII55IO7Zc0H_RrC71NuYVNs_D0aUbw0EBcNx850r2_nHrm2Mccl12YLyNo9qO0MJNG_Ldu8_SHqJWNbX-yhXMrxZzLQ6AR5fKND_JRZGkGAs_GxFejElHY5pUm034mvsVUZNyfgSI_o06-EJWqYHZEsLzKRyrHZkFN3XNtM2Qu9uEdxusAnyWX0_ybxHdvMJwLnR5OvKnheqPMSkOLY0yPA1V3ZTMJZ0bIgu_leoQ6cZxMToZIYo1QaLnnNNUA5YtCIvalX6Z2q_NRJtL4uvpDMVzbM47AJqlsRgRFv2KfQAdDK-TyaIUxlVozj6M-2hL9TrER2jbKCylbWbX7lqZqN74YpIb40EvqDXBueNYMIG4puw2pCWgPsTzjYJCFlDMg2Sx-_S73zzh3WBQtZyC5nBEhTjpaT9TBgW2Dytc9pknk4dLKolfnQQcIIn5qRY6hGAWlcTqc8933BXv31cRG05w12ERYxSp7NE4HA7n0jFmEkNollCK__uHtAtJIyr4T_QUG2TtzHcobMe1-Et4QAaNMyxjjWFZ4KjkVT9vSulU9_RBGvA2go2bor746rS0YnBtSkoTsY_Fc1QSRx4dHO49Ej4P2vthp9HbAAgDsnFNKJza5TvVl_b1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5c7oIf2khebL2SoRjhcZCFFMynPbaqiKPCDCRoXeKLBJOcJMe1s4duxLGBYXahr3Mb_-Vb4GVp8dEIRSIToeWqloQ6zAnmro4BxH6egr9KArNjz9cq-AMzj16d6bxr7Xyyi0MFRAiFRueXVnrQoqQKG80Ir_g_sKkhiqYnuDS2a6NsvwdAWxouqgzd627xu-_XfQ6SzHVEyjQ8P2lY9Mo8J5w-RYN-iqzT9gb18tLaKAO56M6-8JcYExhNypJ0-kU_CxiORRKc7rmLvt6ilHorY43kLozv5peh7Raz6EBcvA7kigd2Di5aWUAfVC01nUmM2wYwHjCrBa3k_QnWVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXW2KAMGGrOeKtVaMWGgPNL4drlVkpkv27n6G-S0JZVCgF3KTgoeT_-4dAkxcE8XUioizm4TFHJ8VJjiI8g7UKZ9IaQKtgzUthVyIZsGVF6xMxZSL8BXKYHw2MjkuS4YlTBIn25g59NrGwi250bu4jAF2vkNqKzLkOdQRB9U0dMmpEB95R6KcORECllc4c2oSK2htwjP3di4DG_g8jh7d3FXLCIX0BwsRVztDYc12_wrQ6Dc6SGpNzAHyHQ69ytds48tvsb2vWbsoRZaf44OPSxNnN6JMVIGP3t7D-O3yG0a4AQAqq2xpfap3KDaEovSr2v1nBHUGFviXpJFIjmxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
