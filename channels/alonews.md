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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 00:38:51</div>
<hr>

<div class="tg-post" id="msg-125186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:  اگر اسرائیل به سمت جنوب بیروت می رفت، موشک باران را شروع می کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/125186" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ایالات متحده رئیس‌جمهور کوبا، میگل دیاز-کانل و خانواده‌اش را تحریم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/125185" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThbcSuV0YEfBTTURtPDhmghi44y7wJRzYXGvuEYpCToxxUHV8qd9Aykga6FfGLNVWgGKvtbOglZ5c4KaLQBDDM3Uu7bBKUxunRiJEKea1pvjhnTIgIhMORcePSLREsdmirghtzr7XYXg3p6sCYujUd6DVbz8mHit7kh98OqPcLahlwO_1sQndokQZVSRQT6Xrh4FcIYBdIeAjfPkY70qqML_cblUWcSh_Wd0FETxS8gL90_RxdDX2Xis-Kt9f7EDmCrduivv5ppSFBCxj8EVuU5_H2hjloZNzlAsJSVDIVj97h-E22j_mk1-3oAocPasBXchrFv2LlDvO2BLE15xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه منتشر کرد: عکس وزیر کشور پاکستان محسن نقوی در دیدار با وزیر کشور ایران در تهران، در چارچوب تلاش‌های اسلام‌آباد برای پیشبرد مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/125184" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: باعث افتخارمه با آیت الله مجتبی خامنه ای دیدار داشته باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125183" target="_blank">📅 00:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKAFZPGBRdELZZkYf22cdvP2lpMa-DY7wQs-YN3gAK-25MDQ9gDr6-5Z3QL1ithf6EMSkwTtklRFwm4WWGi2KmIx72yQOrHcJ9QZemhZCDn7G_rEThbswuOsVZlSpCOkPOC3Uvzpme0tkG8dF2JvQWSccJSLK82NrpuBwn1d4iVGcEF01CDoz40mMTFCq96p1IollvTq853k8Vr2367wOn9vBHyEqf2BXW4xL_vdEdolq7t4HDD1m0eew37L5pg8jk-8tfGZ_ICJhgCwEeNMQ4hcfIz-KUI-eUaVZrdwXgMg5-1mysnpU68AMT1uebaB9iyNQMTrtUcuDJLujGm6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم قابل توجهی از ترابری های آمریکا در حال خروج از خاورمیانه و حرکت به سمت اروپا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125182" target="_blank">📅 00:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125181" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3651e966b.mp4?token=M9jBbQMB__wY48ZODt0D6p4oitgfDI5dG9oVcT9pKwGzowZp-sXYv6cR6zJCma_QLaAehMsjYCmkQuu1_7RWlsiNc265DIEKaureQleK4PnJFGSXV2kdgXnkGbotXVfCJGJqK2BLEKvh4jDHZ2q20uNJoqg9fNeQORhd65Cw43Szj_hfTcCYcQur_9FR1IXfjacQqMj3m61T8nzKmso0uxcz0Rngj66FUzsoC0pbcPATPU-HbbYyELTR0HYoQD4cQOgyd3PliRnfs6-s3EdiOvnvSZhpyLrm7NDCURFZfPPYeCtOiqB6jfrya1CAgshdEXxOec2bxOCxmK0HjXd0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3651e966b.mp4?token=M9jBbQMB__wY48ZODt0D6p4oitgfDI5dG9oVcT9pKwGzowZp-sXYv6cR6zJCma_QLaAehMsjYCmkQuu1_7RWlsiNc265DIEKaureQleK4PnJFGSXV2kdgXnkGbotXVfCJGJqK2BLEKvh4jDHZ2q20uNJoqg9fNeQORhd65Cw43Szj_hfTcCYcQur_9FR1IXfjacQqMj3m61T8nzKmso0uxcz0Rngj66FUzsoC0pbcPATPU-HbbYyELTR0HYoQD4cQOgyd3PliRnfs6-s3EdiOvnvSZhpyLrm7NDCURFZfPPYeCtOiqB6jfrya1CAgshdEXxOec2bxOCxmK0HjXd0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا تحریم‌های شما علیه کوبا با هدف تسریع فروپاشی این کشور اعمال شده‌اند؟
🔴
دونالد ترامپ: نه. ما فقط می‌خواهیم کوبا کشوری باشد که به‌خوبی اداره شود و بتواند مردمش را تأمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125180" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991275c480.mp4?token=Rfxw4s7guAqRvOr9tQ1I2wDTm4pS_vxek0V6jEFlLY0IEZZmzXTSGirwx1tVDOFN0CnM6DQplSIXMx-3Cm6F989UrpGk4AX8cmbYSd9Wlwa-c5ohtoPls8BW0QFgFesXmpZWuNienEvdxYJm7W1pJH2nwPcsuBmRaXtvHkh85bLHHylDR9JrZV_bfxzQR8bw_fWOP3RUiR2rq2s6StoK6vWAOJYwTxlUg86lfwmsrrHsJvZyCFGrJFV6D7uDSJMAge8z_gSApzMAz0xf8aHUtPnFsfph1tBH9gM2gCkKtSRfpfy5fkJuBNjO37uAJJJv5jjW7BTpC9_3ft4qoF_D2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991275c480.mp4?token=Rfxw4s7guAqRvOr9tQ1I2wDTm4pS_vxek0V6jEFlLY0IEZZmzXTSGirwx1tVDOFN0CnM6DQplSIXMx-3Cm6F989UrpGk4AX8cmbYSd9Wlwa-c5ohtoPls8BW0QFgFesXmpZWuNienEvdxYJm7W1pJH2nwPcsuBmRaXtvHkh85bLHHylDR9JrZV_bfxzQR8bw_fWOP3RUiR2rq2s6StoK6vWAOJYwTxlUg86lfwmsrrHsJvZyCFGrJFV6D7uDSJMAge8z_gSApzMAz0xf8aHUtPnFsfph1tBH9gM2gCkKtSRfpfy5fkJuBNjO37uAJJJv5jjW7BTpC9_3ft4qoF_D2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مجتبی خامنه‌ای: او در برخی محافل شهرت بسیار خوبی دارد.
🔴
خیلی‌هاشون درباره من بد می‌گویند. البته این کاملاً نادرست است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125179" target="_blank">📅 00:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره کوبا: ما بعد از ایران به کوبا رسیدگی خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/125178" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: ما در جنگ یا از طریق مذاکره با ایران یا از طریق دیگری پیروز خواهیم شد، اما قطعاً پیروز خواهیم شد.
🔴
مهمترین نکته توافق این است که تنگه هرمز فوراً باز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/125177" target="_blank">📅 00:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ در پاسخ به سؤالی درباره اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران:
🔴
«من نمی‌خواهم جیمی کارتر باشم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125176" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سؤال: آیا کشته شدن نیروهای آمریکایی، خط قرمز شما برای پایان دادن به آتش‌بس است؟
🔴
ترامپ: اگر آن‌ها کسی را بکشند؟
🔴
سؤال: نیروهای آمریکایی را.
🔴
ترامپ: منظورتان چیست؟
🔴
سوال: اینکه اگر نیروهای آمریکایی را بکشند، شما جنگ با ایران را از سر خواهید گرفت؟
🔴
ترامپ: خب، این می‌تواند دلیل خوبی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125175" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125174" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=diq3itqFz7JZueNQ-k1WbHgEjR7-k4zNqJ_x1dOkb8FVWm0C-RwG8X4GZgmNcKYsy3O9s4S85L4dl6-1_OlP_5TrF0G0fC3NZ-UYgS0ZYEo2IEgb31DZoDiRD6clYa3a5q6mpz-7MLL-W9DAhIj02V7JLZ6O0_AkKPfHZm4uPXsx6YINHkRIPI27myNBKBoNBEOOuBA41VsgWpV9VLDmHDG498jfp0yjsf9GRilfXDzLwnggCIOrp0mGmVYqkgVMbrCsseZTFAvnWmnXcPpUBFu_WTmgG951sLmgyzeTqEw4rLtFEUCqLBqVnlL2jRHATkffPyMiKn8XNTk-Htp-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=diq3itqFz7JZueNQ-k1WbHgEjR7-k4zNqJ_x1dOkb8FVWm0C-RwG8X4GZgmNcKYsy3O9s4S85L4dl6-1_OlP_5TrF0G0fC3NZ-UYgS0ZYEo2IEgb31DZoDiRD6clYa3a5q6mpz-7MLL-W9DAhIj02V7JLZ6O0_AkKPfHZm4uPXsx6YINHkRIPI27myNBKBoNBEOOuBA41VsgWpV9VLDmHDG498jfp0yjsf9GRilfXDzLwnggCIOrp0mGmVYqkgVMbrCsseZTFAvnWmnXcPpUBFu_WTmgG951sLmgyzeTqEw4rLtFEUCqLBqVnlL2jRHATkffPyMiKn8XNTk-Htp-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم.
با احترام رفتار می‌کردم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125173" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f44b60c6.mp4?token=Dc3pqRB8bvjFqzhtLYUlROD6IXrsQb5kVqWmOTkj3m1oQTn8KWKsi2FfInfMM28LzRlQrfQBpJOBFowu8cjuvy0A1_vwZVPr3AAKm0kmxr37x6GKH12kYrAG-lFKkpaYgSDrJvlhwIgcU72OeE5IEGGl1uU9RID7yyWK-nk0eCQLSWAdSiOJHYxnxAgzZ8rqSYTyHrDS1L-rvH84alIxkZGbKvH0Ct9XmtPJvD-ccXJkY1Bh_esizUue8WfsmT_UDKcdmcL6oI3AYiuGCi-vIZ36MwmymZbKd2WILSCYSBd96S8-zGDdGP-0SjzW3tXqEgjtuNS1P1MnSk0geODDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f44b60c6.mp4?token=Dc3pqRB8bvjFqzhtLYUlROD6IXrsQb5kVqWmOTkj3m1oQTn8KWKsi2FfInfMM28LzRlQrfQBpJOBFowu8cjuvy0A1_vwZVPr3AAKm0kmxr37x6GKH12kYrAG-lFKkpaYgSDrJvlhwIgcU72OeE5IEGGl1uU9RID7yyWK-nk0eCQLSWAdSiOJHYxnxAgzZ8rqSYTyHrDS1L-rvH84alIxkZGbKvH0Ct9XmtPJvD-ccXJkY1Bh_esizUue8WfsmT_UDKcdmcL6oI3AYiuGCi-vIZ36MwmymZbKd2WILSCYSBd96S8-zGDdGP-0SjzW3tXqEgjtuNS1P1MnSk0geODDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی ایالات متحده:
سیاست‌های انرژی سبز دموکراتیک، قیمت انرژی را بسیار بیشتر از درگیری در ایران افزایش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125172" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: بایدن و اوباما ایران را به داشتن سلاح هسته‌ای ترغیب کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125171" target="_blank">📅 23:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1215f2431.mp4?token=hF8hTjUqZcSW_wBygtjRZgPkdPhBb0-SO3ZSVAqx5YtFBa3Ao-t3zc01JdIqzzF7hubmRGdA-bIhm7_8ZewfSeXm48FY8ZgLKcRwc5Pn0UIqTqk2rRjq5OuA2xYWF-RHHesK-3SiCn1mUBZle9fFxuqpe5HHMZa5HFRhnVsaZp0SJjZ1OsdQV1kAPX0MKtVn3D5OSfwJrveNL69Y5lhaX4a4Ci1VYo8czqqNVefnU0NbDogYNBv0SrfP4dt53wvRcVxGdzAFdxbEIWMdnmP393HI_7lcI01nD0HQJO90XFjjwSvP33Yfaj4iW1zdCKzWufWjEcLUtK6AwwdwsFJXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1215f2431.mp4?token=hF8hTjUqZcSW_wBygtjRZgPkdPhBb0-SO3ZSVAqx5YtFBa3Ao-t3zc01JdIqzzF7hubmRGdA-bIhm7_8ZewfSeXm48FY8ZgLKcRwc5Pn0UIqTqk2rRjq5OuA2xYWF-RHHesK-3SiCn1mUBZle9fFxuqpe5HHMZa5HFRhnVsaZp0SJjZ1OsdQV1kAPX0MKtVn3D5OSfwJrveNL69Y5lhaX4a4Ci1VYo8czqqNVefnU0NbDogYNBv0SrfP4dt53wvRcVxGdzAFdxbEIWMdnmP393HI_7lcI01nD0HQJO90XFjjwSvP33Yfaj4iW1zdCKzWufWjEcLUtK6AwwdwsFJXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  روابط ما با ونزوئلا فوق‌العاده‌ست. کلی نفت، میلیون‌ها بشکه نفت از ونزوئلا خارج کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125170" target="_blank">📅 23:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: چند موشک در ایران باقی مانده است، اما بسیار کم.
🔴
مذاکرات با ایران خوب پیش می‌رود.
🔴
مسئله لبنان تا حدودی متفاوت است، اما به ایران مرتبط است.
🔴
آمریکا می‌تواند اورانیوم غنی‌شده ایران را با یا بدون توافق مصادره کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125169" target="_blank">📅 23:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=SPCzicfqg3m_fno-KhgbKJOZ8vK0aWRyGN-9nBswftDZHo4oJ_f5nLYAIW_MJ56GlFFtwhdpxIXOB2kHtrgmNoVETqhQJRyFg69zYkSgDRSIGL-Pv6xDCdulVinb_NphAeqt7bC3qSIvR4jodpc2ujLKoGDxsYOCEiv8M84ryxigkzc_jj89_M-RvM7sskfNa3bKxrw8piJNgJ_F1peWw0WULz48wLwBW8eCGTpW9JJLiLSE5NpXOgiDnFNmRk924fEz1E8MWlIHSKEP06QsHdMOwzAe3zx4B--psvt5sT3kffme6MdPLlYDfpyjbADXWC0T4fQWAHPS4SD2uhb7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=SPCzicfqg3m_fno-KhgbKJOZ8vK0aWRyGN-9nBswftDZHo4oJ_f5nLYAIW_MJ56GlFFtwhdpxIXOB2kHtrgmNoVETqhQJRyFg69zYkSgDRSIGL-Pv6xDCdulVinb_NphAeqt7bC3qSIvR4jodpc2ujLKoGDxsYOCEiv8M84ryxigkzc_jj89_M-RvM7sskfNa3bKxrw8piJNgJ_F1peWw0WULz48wLwBW8eCGTpW9JJLiLSE5NpXOgiDnFNmRk924fEz1E8MWlIHSKEP06QsHdMOwzAe3zx4B--psvt5sT3kffme6MdPLlYDfpyjbADXWC0T4fQWAHPS4SD2uhb7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/125168" target="_blank">📅 23:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=t_6nPEvDV0cy67oMED2pTq9YIGV8QJIwB7kHBEewz4hwSzDClRE8c_2oY-zjboi1OzfW9MIJC9_PM1mFVQeCr0qzQWmjuvQ-pmOJ9sNGmn3Y3N6cnlUqVtaqMvvrGaBstY1IhFy0vPjqeldyg-lqq5tiKRQhWVO6m4ou2np4b4qhM4-AH7YJlo_wbukyM2_mhiqKPHUqVLo7WLNkAiQlIY9JUns8DWSx7heylWLUmb8gB7H-XHyJmBXWePPTwAD8s9RhLLlQ47m1NOhb-7DKif1OfZrcISwDgg8lQErYsgCBHsSzZPl2-SAm_2uL7hBitGw_Ocaciblgb5Dz7R1mZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=t_6nPEvDV0cy67oMED2pTq9YIGV8QJIwB7kHBEewz4hwSzDClRE8c_2oY-zjboi1OzfW9MIJC9_PM1mFVQeCr0qzQWmjuvQ-pmOJ9sNGmn3Y3N6cnlUqVtaqMvvrGaBstY1IhFy0vPjqeldyg-lqq5tiKRQhWVO6m4ou2np4b4qhM4-AH7YJlo_wbukyM2_mhiqKPHUqVLo7WLNkAiQlIY9JUns8DWSx7heylWLUmb8gB7H-XHyJmBXWePPTwAD8s9RhLLlQ47m1NOhb-7DKif1OfZrcISwDgg8lQErYsgCBHsSzZPl2-SAm_2uL7hBitGw_Ocaciblgb5Dz7R1mZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125167" target="_blank">📅 23:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ پوتین و زلنسکی را «دو ادم بسیار خوب» نامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125166" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e28cd9a1.mp4?token=E_6oMz4904O_SW29hWUhBuQ1xbd_VNsR0fr11BcgDt-6WLVIStpZSKPSTNFASFj-v3-4ctSGs1vT_zL8_Zwk-d5_I4jAwgvhN4NDGA5NPbtD47JHlH1xTgOUU1rYmiJcLY-xPfZijX3zxPc4_IgyOrchCnQMZep4vDV67caxvinM2U5NZZ4jcfJ6Zk3Xwl2sh3JEVjcR_dDXTLcFPtz2at2nyzUCo-Q9bpVHy9EUrrB4NSsJSjciqWv-Rmfx7yK20WggNT8IzOedhpbnRG4KR9pHmMXZeQG7d5kc0GARGygvybWfZPAqXXvA_E-E-qP5APWhVP-U-4oTWoIqrUwT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e28cd9a1.mp4?token=E_6oMz4904O_SW29hWUhBuQ1xbd_VNsR0fr11BcgDt-6WLVIStpZSKPSTNFASFj-v3-4ctSGs1vT_zL8_Zwk-d5_I4jAwgvhN4NDGA5NPbtD47JHlH1xTgOUU1rYmiJcLY-xPfZijX3zxPc4_IgyOrchCnQMZep4vDV67caxvinM2U5NZZ4jcfJ6Zk3Xwl2sh3JEVjcR_dDXTLcFPtz2at2nyzUCo-Q9bpVHy9EUrrB4NSsJSjciqWv-Rmfx7yK20WggNT8IzOedhpbnRG4KR9pHmMXZeQG7d5kc0GARGygvybWfZPAqXXvA_E-E-qP5APWhVP-U-4oTWoIqrUwT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : پوتین گفته اگه اوکراین هم کوتاه بیاد، اونم برای صلح حاضر به مصالحه‌ست. شما دقیقاً چی خواسته بودید؟
🔴
ترامپ : راستش فعلاً نمی‌خوام بگم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/125165" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=sumLE82HOn5YMjtWDrcoi76f_lQ_yTcRThXR1-BzJk91uMR0tscYw6xJmLwCcnZxJV2ogaVD-EOXsWaVpjRk0t2GabnU3c8TnEnK-wRLJtTm_LDjdvnvuom0f1HgJ8i11I_YaUVCLm27ewvjEktsdg12h4nTUsQH-7LurkrCiJN2DSsExAq76M90ZZYtpz9rvGMkAe9Vt8zN-k_rlKd-3_m5KuzZSzwvy61pFXC41m8vuBu8zNt9LRzbUe4lxhUpEVEtB6e1ppEZBhTLR1w-89zXmlXQa8v-Ub_du_w0FRoyBdgU6uuJvj91T__UHdswo6Kc3TPTOuAMteEkl6CkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=sumLE82HOn5YMjtWDrcoi76f_lQ_yTcRThXR1-BzJk91uMR0tscYw6xJmLwCcnZxJV2ogaVD-EOXsWaVpjRk0t2GabnU3c8TnEnK-wRLJtTm_LDjdvnvuom0f1HgJ8i11I_YaUVCLm27ewvjEktsdg12h4nTUsQH-7LurkrCiJN2DSsExAq76M90ZZYtpz9rvGMkAe9Vt8zN-k_rlKd-3_m5KuzZSzwvy61pFXC41m8vuBu8zNt9LRzbUe4lxhUpEVEtB6e1ppEZBhTLR1w-89zXmlXQa8v-Ub_du_w0FRoyBdgU6uuJvj91T__UHdswo6Kc3TPTOuAMteEkl6CkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
🔴
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125164" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کاخ کرملین اعلام کرد: نامه زلنسکی به دست پوتین رسیده است.
🔴
اگر زلنسکی می‌خواهد با پوتین ملاقات کند، می‌تواند به مسکو بیاید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/125163" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: اگر شمارش صداها صادقانه انجام می‌شد، احتمالاً در هر ۵۰ ایالت پیروز می‌شدم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125162" target="_blank">📅 23:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW9VktXN7OCnDgfsdOkcxJ6VimberHL8Ym-s52ydJNTGHLyHtw2UZ7wPFr2GqSvtfACTcJ643KxwoWfppyoR77L96HjYgLFrO4K6b9PFogmEyvoWUV8DXKIHRZ2bYYPiIEKj--G58M-rcoqF9tbuRFZP3P_fNRTIqRw-7g3m-s8yF8hI0YvTipgJDigdrIGRwOCPqSKyPHnW_7rHxfggLqWi_J35bp3e7VSQZulXsxgkasWnTZEbO30lzANNM3PWA_Vc1_fwDl3wtl3qUXV2kJuC1EEFtxnfllXV9T4I-52CXkXSj4Mfa7C5vkLBUmEub-7eiKb66C05hzcrkrzLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5HukcN2uThT0zu33g0OdWco33QY5v3BiBlRxRBkjd-83cEWsxVOrCZKk7EnRy_x4p6rRt24huZl3vMIYoSA01AbGWcqhlaNBawv7lH8EHS25AEOSlj9rofCCyEd9ZZE47dmiqUWO1fj2WB8zm9SOVDNk7S9Ce3sbRwSSZglVBpMdX2NNj7wf5zAnggxOcGwyWCiAXxolLJKdRvcXdSEIns9AxMqzPbs67Xb6z2z6DLDRxPU5wxGCCg40v-5baHkBxnvyMrb-tQRGJ7201kiZuLAbJyOvvy3zq-rFG4wHgoAdKO6q6Dht7Cj5fxtNTH3hoep8mckAtFR5ESSVfHghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFBwo3kGokFkNcQb1aaghBILIJnKwVwUGQa2vkpjV-ah4TgLUoXQ-DcjbTzxULL_WcIDmJLjfnQlX27IX2jKeL_dT6Z1D4j14-6kgRT2baWrnRA_z3Yfe4uNWsrV993ht9frEutRjhfh5w_LfKo0igVI9kRGYI-wjGT2W6H2rt5LbL75zzs7diY-rCdlcDow77Hh9Fyz0rMtXwLQ5vwz5DlehSj1zr48Wl0vDakXMzUu263EtktnWKxZ2qp2Gws-D3GL8kusNlDS26Yyg7YWqo3t-1_bC8oIGHnCAcOae1xukew7IDJCMiKIipv_jtTL1kRrwfh4aURHrd1KdzESTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2ba44a48.mp4?token=o4-tYWfPwPEH4TIP96KtHau0lZj_Xwfm6ujJUnHYTNWCR1cBApM2vGjLF0NL1iFUdQM9CnSwwoP2I2xZPLtd438qyZSJgHcQIJVS2UbgevCng0n8seowv2mjBLanTYpshVV_r0_5t_ZvtwwtXHzZlTsfSCXpm5rgP5yqy9o2g-CUWBgx9foVHGb_SkeAXb1gpZ2ADowoaeOC-BLdCVQHoH_0X3U9572ViDfSoAU031yuKviCVJ-Yj1lKlhASPihYpnX6_r5XVJjKUSbrKMv1eSFCx0RRzT_6NKBX-K_BWyMPHj5odSva13kGLZOKycWyOnswcNjLqt2ERJCmJlJQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2ba44a48.mp4?token=o4-tYWfPwPEH4TIP96KtHau0lZj_Xwfm6ujJUnHYTNWCR1cBApM2vGjLF0NL1iFUdQM9CnSwwoP2I2xZPLtd438qyZSJgHcQIJVS2UbgevCng0n8seowv2mjBLanTYpshVV_r0_5t_ZvtwwtXHzZlTsfSCXpm5rgP5yqy9o2g-CUWBgx9foVHGb_SkeAXb1gpZ2ADowoaeOC-BLdCVQHoH_0X3U9572ViDfSoAU031yuKviCVJ-Yj1lKlhASPihYpnX6_r5XVJjKUSbrKMv1eSFCx0RRzT_6NKBX-K_BWyMPHj5odSva13kGLZOKycWyOnswcNjLqt2ERJCmJlJQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/125158" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: باراک حوسِین اوباما، آیا درباره‌ش شنیده‌اید؟ باراک حوسِین اوباما، یکی دیگر. او نیز یک زیبایی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/125157" target="_blank">📅 23:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8Mq24n47lxUf-RmO7An0uBO1f_Sg6aDNbPx5TTTCJOq_DpRqNXibUFruJnT2VMmKN4kTLPie78E2Lz8VJ1c5p_9CumYDc36MJha4CJQvp0fftcS2LSmXmXq_9hPIf7V04nN0GO4eOYdQyf3rtejJLcw3Yyx7M-kz5j-Y3yrKTJvYcsbJflbP8w-h2ag2jjg89zHy1nYxh4yTL6Tp1nbDhq_8n3ju4gs28n7ij-3Zebfq5WJfdIkxp4epWebfwd8E0MDz0fWk3ysFwVFnVPCSE-LQavwiaqRfU1IjyuYduUz2-rzNUrZCOkJ942m3OlOnQIkHodAl8prZVweR5rWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پولتیکو: انتظار می‌رود پنتاگون برنامه‌های خود برای تأمین موشک‌های تامهاوک برای آلمان را لغو کند و به نگرانی‌هایی اشاره کند که روسیه ممکن است این استقرار را به عنوان تشدید درگیری تلقی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/125156" target="_blank">📅 23:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VINb-LEqDrU9oGizWFAGST2eoGB-2OM6rG8dv_IYJk76-ARmWTndZ3373V_v26aSxLcoOn7t4pbV816zCZIGVSAz20tlei3p_BuIFgyekvoo3M6ux-SahVIcgGF768FL87nHNmPajAuCQfWmDrQ_SHEd-jgmiz6xV5vk0DYGAtcCIV4nO3QSvNPKrgPvLGxpYPvCcoHnOB2jNzXuUhM0a8nObH37iRfmzqsocdyFzpFPGCJH_ZuCvdQqFbOXioshhdVURHyPsA7riS4iM4z9WiKoiyWPoY4KCGop_dsk4jBWc5e6j1cIQ_-nvN1j8oov_7ZpzetRTvXv2tdLDs2Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هفت فروند هواپیمای ترابری نیروی هوایی آمریکا در حال ترک منطقه غرب آسیا به سمت اروپا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125155" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / دقایقی قبل وزارت امور خارجه آمریکا هشدار امنیتی برای سفر به امارات متحده عربی، عربستان سعودی، بحرین، عراق، قطر، عمان و اردن صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125154" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125153">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: آن‌ها در حال تقلب در انتخابات کالیفرنیا هستند. شاید نتوانند از این کار فرار کنند.
🔴
این بهترینِ [کار] ترامپ است: بدون جراحی "تخفیف" ترنس‌جندر برای فرزندان ما.
🔴
اگر به چین و بسیاری از کشورهای موفق نگاه کنید، آن‌ها از زغال‌سنگ استفاده می‌کنند.
🔴
اگر به برخی از کشورهای واقعاً شکست‌خورده نگاه کنید، آن‌ها از باد استفاده می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125153" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bed311657.mp4?token=TDrFgiFx3KIgQzlartg2JR-p23fvigF1q8ptApH3BppOXilRu0RYRYE5bxoDysdHynTi1yUdA3yjFEA-fWHEVZu7rXADyRNu3f2iqxlVSLN-biUQc3I3FZzildNusPArLoULRJuyuzRw0r_gHslEoBLkbwDoCcGeDnqtaFmfWIJzmVD8L7lPeX53Cp0QGKUe80CNLOKfaMdpoHrKksSAcU6KZXkoNrXsqgEkpxF_gy5m1JUpOPX594GjfDR-47rlqpLfis-dlUekk7V8TCqgewuJJbOgv6leCCMv2BVTsWGQIoajcAQjkRLzJBDkKuWL9gg6HlcAwXGHh4KeZxV0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bed311657.mp4?token=TDrFgiFx3KIgQzlartg2JR-p23fvigF1q8ptApH3BppOXilRu0RYRYE5bxoDysdHynTi1yUdA3yjFEA-fWHEVZu7rXADyRNu3f2iqxlVSLN-biUQc3I3FZzildNusPArLoULRJuyuzRw0r_gHslEoBLkbwDoCcGeDnqtaFmfWIJzmVD8L7lPeX53Cp0QGKUe80CNLOKfaMdpoHrKksSAcU6KZXkoNrXsqgEkpxF_gy5m1JUpOPX594GjfDR-47rlqpLfis-dlUekk7V8TCqgewuJJbOgv6leCCMv2BVTsWGQIoajcAQjkRLzJBDkKuWL9gg6HlcAwXGHh4KeZxV0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125152" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/125151" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6SdA_lTNrx4INmLpSF3DiPhSOS3ZedRS3qZlxMSWiYP6xzuE4sSWlZB9BvLRohNWjfLok19D_oY7wZSumls11yYd6qKQOnXoEjt6fdSsH-aYQbsrPDNZEVbclYEnxYgcbxZ5aSeMLIKtSAcFe25p2FWRgeMZibZwQtb_5Se_ZII4Y6wL609Q0PNrCHiR13q7_DvXe0jmOZddHnNjKUOYJYnQOOe_m3NVsXJC2do62ht2PvZIY7GRiWbjHr9o3xTZjmnVLTzRVvMq5cMaUATsCdmyu5K4KjD0jj0ikUTi77qZ_-CO2RfcXk8WvxceF9RvwvZ4BqBU8xrrBeklqKP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/125150" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عراقچی: اینکه ۴۰ روز در برابر بزرگ‌ترین قدرت آشکار جهان که مجهز به سلاح هسته‌ای است ایستادگی کنی، شوخی‌بردار نیست
🔴
جهان به میزان قدرت واقعی ملت ایران، دولت ایران و به طور کلی جمهوری اسلامی ایران پی برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125149" target="_blank">📅 22:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره مدعی شد: آتش‌بس با ایران برقرار است، اما ما به حفاظت از نیروهای خود و اعمال محاصره بر بنادر آن ادامه خواهیم داد.
🔴
یک مسیر کشتیرانی آزاد از طریق تنگه هرمز وجود دارد، اما این به کشتی‌ها بستگی دارد که تصمیم بگیرند آیا عبور کنند یا خیر.
🔴
از زمان اجرای آتش‌بس با ایران در ۸ آوریل، تقریباً ۱۰۰۰ کشتی از تنگه هرمز عبور کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/125148" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125147">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات نظامی آمریکا: مناقشه جاری با ایران همچنان حل نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125147" target="_blank">📅 22:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125146">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراقچی: ما اسناد و مدارک بسیار زیادی داریم که نشان می‌دهد از آسمان کویت به‌طور منظم علیه ایران استفاده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125146" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125145">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LzUjTLVIywwbm3Rz4KRkGz5TiF6lg2m6EaHdy-TjY2pmQdOdvVUsOeaUMl2CxhHIxxns67fR9_W8oeLvf7TuPFCYzDAinbI8Fodg8E35lYGshkzMcYOadEeYTL2MflhMp71k54_3QcSzcH5TQvOD5FBdRWnip_zHRFF86Bc4ZM7a3TsEIxBtBfSV2sKaK_n05lO3HmDPcXFnX66hKo5p0rTImK7f7K7pE9r1tJkvffmdvDJhgM5dPoEaiBHH9tHll1c7iiCpiKkfggXg_DN15gWK5on297oU4Q0qslKcbtGFK25IdFIibUw9wWyunZj62tVFC-xjTNg8DAnICrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که سربازی در لبنان کشته شد: سرهنگ عیتان شمئول لمبرگ، ۲۱ ساله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125145" target="_blank">📅 22:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125144">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ادمیرال محسن رضایی:
معنی خروج از NPT میدونید یعنی چی؟
بهتره هرچه زود تر محاصره رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125144" target="_blank">📅 22:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125143">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ8V4dLGiW8GT4KWsNjS3-x13qb_lJxS2Kis5-QPPHwExB6rQoEh7q3zR_eNJ-rimodBf1mVGFT6M5jHNPSVBSXHJPPJlzP9_P1-xzZh39__GQYANbplwR2FmtdzIxlVejp0WnOVSY64GJ_VRHU9EG9Tj7EWfEBxhviEZxuIdhP5yP0aTiUp4X5HG3dSjVCJ_gbXYUjjGjlQclErDBgofgyqeVAz4cnxb7fcr1TaM4v__itzn221uLQeSMfYY8pKPGfe44UYpgatJbRnKU-Bw7vjgbRqbw6vVmvMwZeWmEHk1dju60ZS6Mwrih7Nzm9a33-1ah-_s6mHxiAsccbRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز:
حزب‌الله طرح آتش‌بس پیشنهادی بین اسرائیل و لبنان رو رد کرده؛ طرحی که می‌تونست روی مذاکرات گسترده‌تر بین آمریکا، ایران و کل خاورمیانه اثر بذاره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125143" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125142">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZlCjn47dfgwRRZ4KVBIjYyJ4wkfP6zmylpjl5iAvwXUIBF9yAK_AdbBtD9R_4nysAmzqIr6vrZysDK2-HFl1B3uTtc-bzQU_7Ki1xjZLfF8YkvICQ8J5z7Yjs8q8o32UNV99V37nBFsMFRhHC8N31_dhdbYSFt64ZFDmGgtGKfe7FYWlMPcWVK--EGYt6_QVbYr_hjgELI_k7vIt6R8JxKFDJisf36ZLFKaXVwxj-NTrxDt6e_2BjJLzdvlqw0nNOBn5j5yR_p0agZ-d59MZrSkionQlliBmUuncvDZqZ6FplOE2HQh88jiqgh8_lNhAFgkCGKtowll1Ey30z7tVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یغما فشخامی، خبرنگار: قضیه تجاوز گروپ به شهبازی بو داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125142" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125141">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عراقچی: رابطه ما با سلطان نشین عمان بسیار دوستانه و برادرانه است و شما شاهد بوده اید که در جنگ اخیر هیچ آسیبی به آن وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125141" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0bm4x8FRWqYPaJIN_1pdNfl7wGXTO4t2BG7qiwKmn699rx2PLVEchEXqXzMTOI91veNZjp9q_CHAli4axgRnDNV8i9mg47bEN3scbTqSQyQg6v6b9SUrdZK3mc6Taw9Qb4LQtSQTBVwFphJmQXl-cfznV7oeCgx57vkcmpDIzzrhAQmFZWqhToeZ9gVhrp8KpMdTgn4KlC_oqfDVmePPU9-u_yDcRUNR6lHzbQKNISfuh1X5p3Ry38ITAhjjt3CXzKYK6FyLo7yQnhAT7NaHg5jQIIFiJ8pxc9m9Zeci4oZIlWva1L6mcnRHvv0xbmDjWOSPOXi0JvpRrS4tmkihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125140" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پوتین: ایران یک کشور دوست است و کاملاً به ما اعتماد دارد؛ از اورانیوم غنی‌شده پس از کاهش سطح غنی‌سازی، برای انرژی هسته‌ای صلح‌آمیز ایران تحت نظارت آژانس استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/125138" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125136">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین در مورد اروپا: آن‌ها به سادگی مایل به گفتگو با روسیه به عنوان یک شریک برابر نیستند، اما مجبور خواهند شد که این کار را انجام دهند. ما عجله‌ای نداریم.
🔴
حتی اگر نه زن باردار را با هم بگذارید، نه زن نمی‌توانند در یک ماه به یک کودک زایمان کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/125136" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125135">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8hb8Q-fZCd3cgGjGWz8WL67iBRD5YvrZpBkX4XqpQuS6yt3UffLXJ9e5XpXFJMYoJITXNDvenu1jOKFQ9P8pQo-Mgq_ck3-XPsrYOJBnOybUS_rrx-XvT32wTX5HzX3Ms4KZt0gBsj8ValI_KjVULZNADwFewsAnjTWspFnSF3pC8CMUq7lw-sCjOhgwaeZnhMO1Rzez5MuDTwJHnWpnlHG6J2j3KZh1ad7MmVZXFRdVsdiM0Q_mdRTlwGDu53-qjCDmiVw4l1gPbcM18kt8vk4jdPpM5dQv7-naaGNi4iAAbwlc8m0xoSXW8SnxKAw3wmm4_Vpi-DnG0n4aj_Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایالات متحده در اورشلیم هشدار سفر جدیدی برای اسرائیل منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/125135" target="_blank">📅 22:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XqDAUNlkCsq77_S1kY3XhGiz9g0y7nOHhUchGYL9KTRp03xjpKjRrQcIMOMb1NHFcwcRgeWwYzG7oVjyeOslnXa_8tGGWaxh8OXZD_UbbEfysGh4kVELsHhg4M5vQ7L8ZQfldBaUWY4Ml6fZ0sQCM2rxUGFhmia2JyMlLAPH0kVpFfmviFilRYIdOFRawbAuMwCQij0LzuPNDngHIPQY8kOpOHA9EKhrN7ZS9o7xBuxQyGf-qbnLQk9WvlB7px_uuCt1FqU0ZBTsjwkimp7BvL0NX7BC7Ho1w_9akIuumQ2nk2p8aqpfLrgBGNeBWPv6AkTQslmGtU-bTaRdik8-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5YQSgV2LZ-HqtATi6B_zMioOAPpSkrLxRGCEangZVRoYb09yBviM_wPri_eP4bdl_EQpTh1HEiARM-4DxAuBLzRE6w1ojcSa18e5Q7uz5VbHIUvjkgHBP55tixeHw_6Y9KQ4BNYQl0Er7CeoJdj8KflkWotX6keSuUkTEmMlqt5-NHTc3cIeQSGtB_OqAIgpU_5rWdsvqmYb09Q1qX3tMrxKMg75jQX7cpkBfRXggir4tt5t4CJpOcrreVBJgP__ynBq4Jcw2cZ0JTKdQDHSU-by2pNmdbBP1pvL4Fi396PY3AcUwsGmm7Kh0p8QRVbDK6abllavd-0Ak2fu2tqwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
طبق تصاویر جدید ماهواره ایی، ایران علاوه بر تعمیر پایگاه های فعلیش، داره به طور فعال پایگاه های موشکی جدید حفاری میکنه و قبلی هارو هم گسترش میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/125132" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ_f6jRIss3XnLjfkfH8H2gLpCJHslc1BTF0xRaT36uvYPcObfo45w5VrAd4jhliZmboQ9VJoT4ShXFdTvfV7xsnMsa-fot4qq-ABw3p2YyTQJejPkmJ3svEHFJrBk4HsBPFu4T_pGkRdl8pKmLttNVR3F9qEYvfuzzwwbjeN5ecTyuLY377zKb_KPKqig7Fln2DPRW7isxGy-AizO9Eczl65PDIZKdG9rxJhzasUSO9OB5_HUGFG_2KV_sfFHMIbMKGwoPTH10siTXlVVpssFeAgZ0iB9H3pnAmrm_WLAi8hi3xQThzDafz-lZz-pjfoi4IDfoxVCY4rkIDsSpC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏هواپیمای تهاجمی عمود پرواز AV-8B Harrier II  بعد از نزدیک به 40 سال خدمت از سپاه تفنگداران دریایی آمریکا بازنشسته شد. جایگزین این هواپیما F-35 در مدل B خواهد بود
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125131" target="_blank">📅 22:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب زاینده‌رود به اصفهان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/125130" target="_blank">📅 22:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🔻
بیست سال گذشت و حالا رسیدیم به ششمین و آخرین جام جهانیِ مسی و رونالدو. این آخرین تورنمنت مشترک اوناست.
💔
🫡
🙌
@AloSport</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125129" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125128">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام علیرضا سلمانی 28ساله
🔴
شامگاه پنج‌شنبه 18 دی‌ماه حوالی ساعت 21، با شلیک مستقیم چهار گلوله توسط حرام زاده های جمهوری تروریستی اسلامی پرپر شد. چه نازنین جوانانی!
🤔
عرزشی حرام زاده، به وقتش مردم شما را پاکسازی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125128" target="_blank">📅 22:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai8iHohtBVIQhPkSd459rXRaPvnWxWls03F5XVEjPT5NUgSDiHZSGAcYQd2uAbCM8f73x1GVHM_uJoXJnNXZNuYrKxWxsGmsMYr_p02FgkDpmgfDgUPYFzTVomdSNKdK5AnFEo0rvC_DeaH5gSt0mwgAg6QS14bWFGC8aNftnqVUdrmMhzDjipapRNCmpU27KIg4j6_71k-A08u1KrR7Z8pge8w8DpynyD4SuEa4E4o5wuu6vKCgg18DNjvV5O8lzwb6-BVf5gWB4LhwXiRlpUQq4DnUGI6NakwHjlPF5zkZJ2zJFF0iLHsm24W5XDmBxLZsnMH7WZ4TUDJDlae8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال حاج محسن رضایی:
اگر آمریکا غلطی کنه آنچنان تو دهنش میزاریم تا درس عبرت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125127" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVeOt0MlM042XTFwHjEJwT73gbfS6d-jnx0Hzg-YinzD8UUjsOr-fu80DOQMAEbbn-VcicOz8VkpyIog9vsQHMDVKhdZWV2AzN8srNoCQbq9ZsgPhtqwdbUGnmG5RTjBJAS36a5EQsdvkkiDFbfxn-IbZDjFpfIeXP29lthESg0lk4kIKj5EsdGBMBsbQR_joAO8uqGaPqxbcOtqoSK88z8cwWbJEYZB-V9l5Y72EaBy9I-yYzHA0qEaVupwn0f1YaHYqQ7jIEMvf36GKKSGLgCCl6xKqYld5IiHvlsf8--bwRweDaIPRRwnUrbfPbrZYas9yHf541YUj1r_ny6EmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
🔴
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
🔴
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125126" target="_blank">📅 21:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125125">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پوتین درباره فلسطین: اکنون باتوجه به رویدادهای جاری در ایران و تنگه هرمز، ما فاجعه فلسطین را فراموش کرده‌ایم، اما این مسئله هنوز وجود دارد.
🔴
روسیه معتقد است که راه‌حل اساسی این موضوع، تأسیس کشور فلسطین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125125" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125124">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر تماس تلفنی از وزیر خارجه مصر دریافت کرد و آن دو درباره میانجی‌گری بین واشنگتن و تهران گفت‌وگو کردند.
🔴
وزیر امور خارجه قطر بر ضرورت پاسخگویی همه طرف‌ها به تلاش‌های میانجی‌گری جاری تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125124" target="_blank">📅 21:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125123">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پوتین : روسیه می‌خواد با اوکراین از راه مسالمت‌آمیز به توافق برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125123" target="_blank">📅 21:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125122">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125122" target="_blank">📅 21:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125120">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQTos46FXPHuvvEGmRpT57i6IWuhkJe18eoP5XFFQnQklr2UpVcCu129GkMM5xVyZZDcY__oikd-KrCULgoGdx3HtRGEbN9o6z0YCaJLv1oqEBaOeiXp7EabVNvSUU-17AZnEl7Sl3Ty-XsIYX01D8LbtuzF-CfotZ-0sIsySPosZgeE2l31Gkon4r14d-U3fObq7u1iCAq7mCZEvceVCAUjZ7QSgayx4496VeCS2lkZhVIIuz3LeGAgw-rxFIFf7tNtos08tGDlsfkH0Nfw2uCzw_F90Nm4zCmc9v0q6SMO0aYplgqoUd0nIojO0MV8DMdIWb2al8BofnB9_Lvzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8938050d74.mp4?token=siMszbgTsG7eskZaL_DiSi36MpuLRdQGiVdjS8WxdikxLL9D1MtdxBL0qroc3SetEbv0WTrPlBUn3HJzbqCRHDuhJPROZQrDAx-npojASkzwYTVMdrDJJrMSqxwFnkqZhf7a4nKHikPj820FFQ1xQIFykknTWC3YhyiRW0LpYrfClWMCoagPE0NIf0NNSG4ayBtEjl_-ZwdJd_F-oW1ege3Q_OGGQe9fsnlNSBp_UbwZDWIucJUY_jH3lZoG7ynIyLwU9xTNI2ZD2yXqZ67BeIx4_ggJxDfovtEWERx0_tzo68sHRxaVBIdTBtNnyu3tOWxDepC0jb5vRqMFcZ3_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8938050d74.mp4?token=siMszbgTsG7eskZaL_DiSi36MpuLRdQGiVdjS8WxdikxLL9D1MtdxBL0qroc3SetEbv0WTrPlBUn3HJzbqCRHDuhJPROZQrDAx-npojASkzwYTVMdrDJJrMSqxwFnkqZhf7a4nKHikPj820FFQ1xQIFykknTWC3YhyiRW0LpYrfClWMCoagPE0NIf0NNSG4ayBtEjl_-ZwdJd_F-oW1ege3Q_OGGQe9fsnlNSBp_UbwZDWIucJUY_jH3lZoG7ynIyLwU9xTNI2ZD2yXqZ67BeIx4_ggJxDfovtEWERx0_tzo68sHRxaVBIdTBtNnyu3tOWxDepC0jb5vRqMFcZ3_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125120" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125119">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqRG2Sgiwj58IRiK7b0J3OKaIm0MRglcJDY_E0uxbhsHo2g_Nxs6ySGLpSGbX93M6nnAhN4-z1l1hAvAKS8eAxSbgBgjlWU8EqDqJXUzOXCUmv7UAtUP-Z51K-a3LJMAf7UHUBP_naWRzQaba5sisLKuBdOgCtAUey-JMSg5MYq8PRft_rTfnPHYkduGoSq0w-XfPQMY__kD6cjvvAIVtUfw4Vu6GL2kpnDh4yPkc-Et6qWF4Ih-kuKsA7VqFwce8zGC_zi3_DSvOd-jZ5uvmv_3hyBbFY-2Cxpo8T_uMrQZgTIRX2cW2hP8CUSt0mFgvKxOrcN_MERqm1Pa8e2caw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند وقت دیگه همزمان با محرم:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125119" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125118">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/125118" target="_blank">📅 21:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125117">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJtzl8hYdxMeFc_D-UoxyEMfUS5u9NcKOaJ6y1lmlSFyk6qqBe4vBnJCZT7u3OLKABRGQaRi8q6gGzBcXL2y8KUj6r7yHznOPmDdykHgEw16hy1buVR_o6qBhyWhlxtypd2ZXJgAmbqJO2lN2sp_lh7LAKwAcb0mFB6ta5YnCEsCpl07-XuVSBBdkWv2jmh5jZvt0VVB9XpBEAC6gQ6vGGcO7PqjM5-89YkWqBwYEq9AhBJJTjn9J4Zi00c-jl3fZ_EFQ8Kyl9ZMF9KMPF9ipB53DlYv2i_fuq4jT4bruQsZDgY0PJQqBoF-nMMbZJ_XjDSpAXjCJvndqnkOxjOhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/125117" target="_blank">📅 21:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125116" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پوتین : روسیه می‌خواد با اوکراین از راه مسالمت‌آمیز به توافق برسه
🔴
ارتباطات بین روسیه و اروپا از طریق سرویس‌های اطلاعاتی همچنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125115" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125114">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff210baa61.mp4?token=NrmKlJDjTWVcIuudesUT0xzG8ewXMXUmwvRSh_BQmqYizbc76G9ghoZdfVjKvYnjM4MH1eAn4zwpuqNX6HJmy_DcFTDbXmsS3Fmelv2-HMvFW4JQq3xNRbidnJAzL0x9arCN8kgx-Dq2iCJ4-2wefh2eIVa3UY6MGd8EF6yoVcoVlD4kap7TAI-fq3qaNGWRFQaxzTENIsOy6ctDsleMdoIlLVkAJsxT67gupoFPT7xbXGb47-mPgI0JTtBs2THcmA8jhbeQgfCONO7KHABW97_xY4QTEslzIJ7a-npDbcBWLxGuE8QxpNcc1Mjg8HTmm9xIcCZRJOKX0gzOomqGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff210baa61.mp4?token=NrmKlJDjTWVcIuudesUT0xzG8ewXMXUmwvRSh_BQmqYizbc76G9ghoZdfVjKvYnjM4MH1eAn4zwpuqNX6HJmy_DcFTDbXmsS3Fmelv2-HMvFW4JQq3xNRbidnJAzL0x9arCN8kgx-Dq2iCJ4-2wefh2eIVa3UY6MGd8EF6yoVcoVlD4kap7TAI-fq3qaNGWRFQaxzTENIsOy6ctDsleMdoIlLVkAJsxT67gupoFPT7xbXGb47-mPgI0JTtBs2THcmA8jhbeQgfCONO7KHABW97_xY4QTEslzIJ7a-npDbcBWLxGuE8QxpNcc1Mjg8HTmm9xIcCZRJOKX0gzOomqGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر روسی کیرل دمتریف گفت که روسیه فردا برای پیشبرد کارهای طراحی مهندسی یک تونل پیشنهادی زیر تنگه برینگ که چوکوتکا و آلاسکا را به هم متصل می‌کند، توافق‌نامه‌ای را امضا خواهد کرد.
🔴
او بعداً شفاف‌سازی کرد که امضا با یک شرکت مهندسی خصوصی است، نه مقامات آمریکایی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125114" target="_blank">📅 21:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125113">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پوتین: ما می‌توانیم منطقه دونباس را کنترل کنیم و می‌توانیم به توافق بپردازیم.
🔴
یک چیز با چیز دیگر منافات ندارد. چرا فکر می کنید که این کار را می کند؟
🔴
ما بر ۸۰ درصد زاپوریژیا، بیش از ۸۵ درصد دونتسک و تمامی لوهانسک کنترل داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125113" target="_blank">📅 21:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125112">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: پیشرفتی در مذاکرات بین ایران و ایالات متحده حاصل نشده است
🔴
واشنگتن از تهران خواسته پاسخ خود را قبل از پایان هفته تحویل دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125112" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125111">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پوتین: هند یکی از اقتصادهای پیشرو در جهان است که بالاترین رشد اقتصادی را نشان می‌دهد. این نتیجه کار سخت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125111" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125110">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پوتین : تلفات ماهانه نیروهای اوکراینی حدود ۴۰ هزار نفره
🔴
روس‌ها تقریباً تو همه جبهه‌ها پیشروی داشتن؛
🔴
نیروهای اوکراین هم تو این مدت حدود ۱۰۰ هزار نفر کمتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125110" target="_blank">📅 20:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125109">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شرکت ردیابی دریایی کپلر: چهار نفتکش ایرانی با مجموع ۷ میلیون بشکه نفت، روز دوشنبه از تنگه هرمز عبور کردند که اولین مورد از ۱۷ آوریل در جریان محاصره آمریکاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125109" target="_blank">📅 20:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پوتین: رابطه دوستانه ما با چین علیه کسی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125108" target="_blank">📅 20:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125107">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYe82tconC7oZnG5qXuWFT1cDCZ5hwtKvw9rTTE-hsIg1u7c2OmGQegCOg1rp4END5MrRC4G1M8yVGpnhS55asAkKzPmcQyextxs6ksaBzjM5BumXkd9VSFqGrb9dYFvlPdngdioSzjYTcleAIG3Pqu83qPTDN7ILbnCeCpkuw4SZvr0T62u1Jt-AfcAeoYGK1tAQhc7BbBqjON9QUf8PtKt8Cb0eh5C5xDZTmPl_uur_BGxHDo267lHmC-unbrttU8QU962zQgYCppUlG4LN6uIN9X7FleQ-zDyQpLtfpaxCxBgWCd-B3lqb_CZOrt_3srkMNTD5Vlgl6gnt0QYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.  توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره. دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125107" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125106">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وضعیت آب سد کرج ، امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125106" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea73f38f1.mp4?token=XTbA4RoTI4PKd8xDmkP1C_VI8sY72gQOm0m-WKslme5c092YARM3eZrM049K_yzgCurRpa9VNQ6nUb1ePwzyNHUcIKLJoKYDcsLt--_II24sWd4IbsWbrSaOnOxfemqDdJwq7Z5rRZB0QR_pck22zdUosRqK3eTqeqoWo1aU-RRHbuESg9_muzMvTf3mzue_S8LpE1PxyWYc5r0fiM1zROBjR1ZFtf117jE8lasQUssYgqGEcQkHFi55742KLIcc0v8WAcJm-2C-Gp9RAN2jqZY3OXKBZWhFAvyXjTM4GVMtIp-CoOpPH3katrsHLEzgQKLtb4yIbyI73LpJRCTcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea73f38f1.mp4?token=XTbA4RoTI4PKd8xDmkP1C_VI8sY72gQOm0m-WKslme5c092YARM3eZrM049K_yzgCurRpa9VNQ6nUb1ePwzyNHUcIKLJoKYDcsLt--_II24sWd4IbsWbrSaOnOxfemqDdJwq7Z5rRZB0QR_pck22zdUosRqK3eTqeqoWo1aU-RRHbuESg9_muzMvTf3mzue_S8LpE1PxyWYc5r0fiM1zROBjR1ZFtf117jE8lasQUssYgqGEcQkHFi55742KLIcc0v8WAcJm-2C-Gp9RAN2jqZY3OXKBZWhFAvyXjTM4GVMtIp-CoOpPH3katrsHLEzgQKLtb4yIbyI73LpJRCTcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش خبرگزاری فرانسه، حزب الله توافق صلح میان بیروت و تل آویو را رد کرده است.
🔴
دقایقی بعد، گروه شبه‌نظامی شیعه شروع به پرتاب موشک به سمت کریات شمونا و شلومی کرد که ظاهراً این خبر را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125104" target="_blank">📅 20:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgNW-0Yx112hP_k7NvL7tYyoTjy8aj1o9YHmZXRMIYVEmw61UbmrVRY7UrPd_7ehOMS3Vk9g2_Idam9u0Bs09oI9FznWGzcdILSpdJposF2ep2xlOorqK44saJaJtDIEcokySa_ID_l8T70RWL4oPsPtp2M6MSNk39FPHDhQbCIFuQZPpParjxzaBDv1WWSR9lFhkz6GXUOrG_JLawe8fph0rM2LbZ9mQa9wfiZ81MZ-C1KOEGZasGskLhdBItvyxl-4ESINn8_Tbfv3iV_2KjPQCK-11FdJiR-OlnU5sAg2XizhPFT_WRj8_NFOyXG7kawadDMBQzAwA3KbalskLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بسته بندی رایگان هم پولی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125103" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رویترز: روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته
🔴
این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده
🔴
آژانس بین‌المللی انرژی تخمین زده که تولید نفت خام روسیه در ماه آوریل نسبت به سال گذشته حدود ۴۶۰ هزار بشکه در روز کاهش یافته و به حدود ۸.۸ میلیون بشکه در روز رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125102" target="_blank">📅 20:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=vDwSqnVBpVuolHUdhf-xXjcFrVNmWZ5xlT8UyGQDwtktYY8DkfW7o_gKkbToxneYnp5IWCfcTLv4b5txt9ggfoo9qAk1UW_f2dD4RWrk-i0iqqk1Pw9nSbuoMBgKoG03SI18AJeqoMGuU5XebiqOXxTJh8_hDhhV7Bm-CTJrjHODsVMdG2bzLR9opBQtDfMg_CFnjhMzkknZOHpUqfJRt4RxMUmG8sdY6FkrUCP8fIOKMsGK42UBLJ5RXs_NJ7roAdjgC8Am5Hlhhc45EfQwB5qwMZ3mL6m9jWBDI4anlPfdCCcnkPXwnz-7P0iThu1syVWWptJlt0fc2lOMdEdTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=vDwSqnVBpVuolHUdhf-xXjcFrVNmWZ5xlT8UyGQDwtktYY8DkfW7o_gKkbToxneYnp5IWCfcTLv4b5txt9ggfoo9qAk1UW_f2dD4RWrk-i0iqqk1Pw9nSbuoMBgKoG03SI18AJeqoMGuU5XebiqOXxTJh8_hDhhV7Bm-CTJrjHODsVMdG2bzLR9opBQtDfMg_CFnjhMzkknZOHpUqfJRt4RxMUmG8sdY6FkrUCP8fIOKMsGK42UBLJ5RXs_NJ7roAdjgC8Am5Hlhhc45EfQwB5qwMZ3mL6m9jWBDI4anlPfdCCcnkPXwnz-7P0iThu1syVWWptJlt0fc2lOMdEdTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران شهر بزرگ صور در جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125101" target="_blank">📅 20:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125100">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc6a353f1c.mp4?token=rbNfMphflAnHgS3IwJltj_19uPRaZ5MA87auwSyZisedrUge58bWqZvnJ2tz4EmCN6UFnoG2c0nmcYp__KK5jDBlsOvGe1R1oFIyUlLu6xHpBT7WeqmepEM33V9rX_rzIfK5uhk1NsD5Rpq3kXwUVsI0HW1Pgmhx8_rDtL8CFSFMN1M4LFcMRbRlq7ZQt0F_Q74N3WOuN6C7A9tWmDbvKLeDwqbx7a1H2T5DOkAjFAVdPaRGCrfMi0mjGQuc85bkjUB2HPlwuaSrx2I81dq7qDgMpLssOlIUBLQ4k1SfHrbtaJmnUmLLxtLLaztQgZXLwN6EhCWGYNLxx4phjlYT8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc6a353f1c.mp4?token=rbNfMphflAnHgS3IwJltj_19uPRaZ5MA87auwSyZisedrUge58bWqZvnJ2tz4EmCN6UFnoG2c0nmcYp__KK5jDBlsOvGe1R1oFIyUlLu6xHpBT7WeqmepEM33V9rX_rzIfK5uhk1NsD5Rpq3kXwUVsI0HW1Pgmhx8_rDtL8CFSFMN1M4LFcMRbRlq7ZQt0F_Q74N3WOuN6C7A9tWmDbvKLeDwqbx7a1H2T5DOkAjFAVdPaRGCrfMi0mjGQuc85bkjUB2HPlwuaSrx2I81dq7qDgMpLssOlIUBLQ4k1SfHrbtaJmnUmLLxtLLaztQgZXLwN6EhCWGYNLxx4phjlYT8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها حاکی است سامانه‌های پدافندی اسرائیل دست‌کم ۷ بار برای رهگیری اهداف هوایی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125100" target="_blank">📅 20:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV37qTBNhKQLTQvtnwXjpj1rOVg0fDEIPeDGx4Ywh2zfPhfUGhqrZen9qOeyTzTAgxKAGbEvSmGAbD-3jIwVrUEjKid7r6pZGSY7AzO75ru4CY34A8mfH3sUmx_LiUioMhq77gwFHZ84ofA9_qa2TUbuzYkB8jmxx7fAyiJWPWS_BoZl8MbUyJ_Bg3Ir9Kzwq0oHIoYkCGYk2XbWOKeYgrD6eWcTpoJbLKjGQty6KEs7dPyVEyGkbj19VreIVhBctXPgE4FFRgCGChyp8sYPh3bjmt7E63cvVDsPOmUAX_lkiJGRGZPAUA9MWaAE7bWfk3qogllHG54V_N9shfhciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9e03683c.mp4?token=WLDtGgKq4_iZaBAjgVE3cVx9FyoLtH6N0bycbm2DC48N9u8shTAcv_BPtzIEeYJBwaDZcYY3AbRWxeHSkw10TTAA0-cC5O3ldV7pLbGP8MC2t9GnbkbipCwa6LKjbWF73z7EJqYIfuD3E43aJz2NHTi8Ig7Up9hpqhM01ONqI5uMtR1n2UuQqWjUSLCa_R2xyAkZ6_Kvgea_70x84u8mohwwfeTUijWrNqZ1hDqKVo_RZgo3V9wExSpGzbx9RR-LRkc6lPlXaetBgftQgq3ogkCJ87B-6bsrb5xzycUBmhbCtTber64yDiAB9vFiUD37FDifP9cmGkHrRs0aCJiE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9e03683c.mp4?token=WLDtGgKq4_iZaBAjgVE3cVx9FyoLtH6N0bycbm2DC48N9u8shTAcv_BPtzIEeYJBwaDZcYY3AbRWxeHSkw10TTAA0-cC5O3ldV7pLbGP8MC2t9GnbkbipCwa6LKjbWF73z7EJqYIfuD3E43aJz2NHTi8Ig7Up9hpqhM01ONqI5uMtR1n2UuQqWjUSLCa_R2xyAkZ6_Kvgea_70x84u8mohwwfeTUijWrNqZ1hDqKVo_RZgo3V9wExSpGzbx9RR-LRkc6lPlXaetBgftQgq3ogkCJ87B-6bsrb5xzycUBmhbCtTber64yDiAB9vFiUD37FDifP9cmGkHrRs0aCJiE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تو حمله به غزه چند تا از مسئولین ارشد امنیتی حماس رو ترور کردیم
🔴
عملیات دقیق بوده و قبلش هم سعی کردیم به غیرنظامی‌ها آسیب نرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125097" target="_blank">📅 20:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل به کوثریات الروز، صفاد البطیخ و عین قنا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125096" target="_blank">📅 20:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اکونومیست: حکام خلیج فارس پس از جنگ می‌خواهند نشان دهند که در خانه همچنان قدرتمند هستند
🔴
آنها تدابیری شبیه حکومت نظامی را اعمال کرده‌اند؛ ده‌ها هزار نفر اخراج شده‌اند و بیش از هزار نفر بازداشت شده‌اند
🔴
امارات، که میزبان صدها هزار ایرانی است، بیمارستان‌ها، مدارس و باشگاه‌های ایرانی را تعطیل کرده
🔴
فشار بر شیعیان و ساکنان ایرانی، احساسات فرقه‌ای که پیش‌تر در حال کاهش بود را دوباره زنده کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125095" target="_blank">📅 20:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n33LvChy57v9UUJzbbsCn1onQmrrP2B9iuThqauFg7IiwsVqlFsW3F8dFpqHDl_MMTT8uO0QoFYPHOP_tguhyWRI0FkLBaYDDM6d6YRCI3qQNfBBmT0UYEzO6RlN0VkN3P2QzBBLW04E_B8j36jHA2JjmqlzKJaDihCP0gksfJ-RX9wCO6q47_zFTgyW2K-UWpz0jY4rKvCAQSJbrlNX2FNRYAC2mx0Jld78n67UjAeQS6hd-Z2KKyHiFbIghld5VzdN3Eyj-QKqFcajVk6H6lN40Q_QYbHWaS2nD7s1bTFi9oZEye61QzPzUtWNQvbHZjTRXBWLWfZU4BRjbk0PNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان بولتون، مشاور اسبق امنیت ملی دونالد ترامپ و یکی از منتقدان سرسخت او، با وزارت دادگستری آمریکا به توافق رسیده است که به یک فقره اتهام نگهداری غیرقانونی اطلاعات طبقه‌بندی‌شده اعتراف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125094" target="_blank">📅 19:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر خارجه روسیه : غرب تو تلاشه تا روسیه رو نابود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125093" target="_blank">📅 19:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فارس : آمریکا برای تبعه خود در کویت هشدار امنیتی صادر کرد
🔴
سفارت ایالات متحده در کویت از شهروندان خود خواست که احتیاط کرده و دستورالعمل‌های مقامات محلی را دنبال کنند.
🔴
علاوه بر این، سفارت ایالات متحده در کویت سیتی تمام خدمات کنسولی را به حالت تعلیق درآورده است.
🔴
واشنگتن همچنین از تبعه خود خواست که از اعتراضات و تظاهرات در این کشور دوری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125092" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
واشنگتن: ارتباط با ایران از طریق میانجی‌ها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125091" target="_blank">📅 19:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد، زودتر از آنچه فکر می‌کنیم، سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125090" target="_blank">📅 19:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مدیرعامل مایکروسافت: دیتاسنترهای هوش مصنوعی جدید ما به‌اندازه یک رستوران آب مصرف می‌کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125089" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwCWC3pgGZVcV3Lvjd2_VPlB2_GcpyioSP6jD7xrUFoGeoY64d2257VCYgFuNhAMD9dHIzPGfOQPJGtHlyrz9u3qeRWuAGexuPtjvERiyNqoviIrCVbwEOZ0xjG6wOMhQGtRZlTRJXOVEIIYxc2DmnAQUAnuH9pE_DA0kLSL1QXS06q8QwRxgCINEOAiEQCLhN7FiprHtn5_cF7OA11mqI6B9FA1jdn7PoyYSviJzEDuqvlQ91PN3fhZ_2T1qbTq8bPsC7R0w2rWK43gAO9wz3sw-i-TCOU9nKgQmX9sje80QY7L4-NkKcgeETfa5THoW4TL9hOH2cQgO1hfndWnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۵.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125088" target="_blank">📅 19:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سنتکام:۶ تا کشتی رو از کار انداختیم، ۱۲۷ تا کشتی تجاری رو مسیرشون رو، عوض کردیم
🔴
۳۶ تا کشتی هم که کمک‌های انسانی داشتن رو اجازه دادیم رد بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125087" target="_blank">📅 19:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/125086" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sd6iIwEIzbtKX5L8jvI0kADv7UFEiV-Ajkm2IGniiuAzVya0jw8Cai5uwV2Hb1o3z_Dc1pRb17pszKBQQylhEYt85EOONiP1GziSSLBwiwHwdWhF0vI0Ry5zWmjg9xEQCMGPY-gXmX0xFs_fCgCvjRDe-p6-_gNk_lO7RbUQ-M3kubAcxWXOr8g50em-c3sXxmi9z5N_Ho_2Z3mX_xwaQczAgfX7EjwvE2jTWml8LDTsBJvMzcApvmHGPA0z35BMsyBzdA9yVS_q9FBG845gKYzzQIUPSw7cFPlSE0LuS5iuc3Pq8ytCYTR7887GkIaT941LulLR3aFkOr3oB7OryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/125085" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=a0T5AvLS5eYlF2P_ssbb5l3MjxoBYK-FHWQqeTw_q8yl8TWca_9YDLfObFAmKnoDqLTZ7n7du3azZzntO8l79rMmlHCV_esxNOK_go1ZKq5tboUmWRJvRtBSqX4Ve4e00ju5QOhnReSCaQsgYX6_pMMsYjxWPsEanivQnfgp_REyytbonwthx5ySUYOZ-22o0QniHzM0tKUe1Jg6tgQBFJjwp0VS6ck4gCfdkNdiaPYIvyAMmpI32I9OkxcLDBCpQImEtqH4o1RHzjlQEvLSoW-Wy6h-nrQT6JVVMs9unPv7tNArMPWxayEBanMniHUrc4qnm6NMPyKLyYU32XPz5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=a0T5AvLS5eYlF2P_ssbb5l3MjxoBYK-FHWQqeTw_q8yl8TWca_9YDLfObFAmKnoDqLTZ7n7du3azZzntO8l79rMmlHCV_esxNOK_go1ZKq5tboUmWRJvRtBSqX4Ve4e00ju5QOhnReSCaQsgYX6_pMMsYjxWPsEanivQnfgp_REyytbonwthx5ySUYOZ-22o0QniHzM0tKUe1Jg6tgQBFJjwp0VS6ck4gCfdkNdiaPYIvyAMmpI32I9OkxcLDBCpQImEtqH4o1RHzjlQEvLSoW-Wy6h-nrQT6JVVMs9unPv7tNArMPWxayEBanMniHUrc4qnm6NMPyKLyYU32XPz5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی: برای ترامپ ویلچر ببرید!
🔴
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتواند آمریکا را اداره کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125084" target="_blank">📅 19:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
حزب‌الله به دولت لبنان اعلام کرده که توافق صلح لبنان و اسرائیل که با میانجی‌گری آمریکا انجام شده رو قبول نداره- AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125083" target="_blank">📅 19:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بلومبرگ، به نقل از منابع: بریتانیا و فرانسه برنامه‌هایی را برای یک مأموریت مین‌روبی چندملیتی در تنگه هرمز نهایی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125082" target="_blank">📅 19:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125081">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش گروسی به شورای حکام: آژانس نه اطلاعاتی از ایران درباره وضعیت مواد هسته‌ای اعلام‌شده دریافت کرده و نه به هیچ‌یک از این تأسیسات و مکان‌ها برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی داشته
🔴
حملات نظامی به تأسیسات هسته‌ای ایران وضعیتی بی‌سابقه ایجاد کرده
🔴
انجام بی‌درنگ فعالیت‌های راستی‌آزمایی آژانس در ایران مطابق با توافقنامه پادمانی ان‌پی‌تی ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125081" target="_blank">📅 19:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125080">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=vhejOR6mLoinDDNY8byXnqGQV8Sg7Mhd63oJrdUvbtZeD8Ior8widRmBoOavcXClgcmEAdA8cplyNW7WXBMCkeMNfjfK7wGvQIhf8YVt5sfvLVpyAPvDElv0wDfo31--YJ2wCJoV1VvMMeikrttv77BBpHGUyWgtq5NzzOgCvBZ9LEUBToDCgtCilT09y2PKZU2mRCLWN73YtUcQcvEBPOTvvJNp98mvbKprUTESACQGskGin2gW9Kc4UltM7bcQD-SdeBa_hlaUU9uAhyg9XD5YE6hQNTO7s49CRLqci6Hjpy5bY0HGT8KBtgv2neSRrwRagf3N_YBZVjqiEh0Q6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=vhejOR6mLoinDDNY8byXnqGQV8Sg7Mhd63oJrdUvbtZeD8Ior8widRmBoOavcXClgcmEAdA8cplyNW7WXBMCkeMNfjfK7wGvQIhf8YVt5sfvLVpyAPvDElv0wDfo31--YJ2wCJoV1VvMMeikrttv77BBpHGUyWgtq5NzzOgCvBZ9LEUBToDCgtCilT09y2PKZU2mRCLWN73YtUcQcvEBPOTvvJNp98mvbKprUTESACQGskGin2gW9Kc4UltM7bcQD-SdeBa_hlaUU9uAhyg9XD5YE6hQNTO7s49CRLqci6Hjpy5bY0HGT8KBtgv2neSRrwRagf3N_YBZVjqiEh0Q6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که از لحظهٔ بمباران مقر سپاه پاسداران تو نسیم‌شهر تهران درجریان جنگ ۴۰ روزه منتشر شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125080" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125079">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzgAupNYC49OaXwvPG22Lv5fYf8YrIv36SyC3cc9NF-EtS83jQ5VXfAdZsXtRNgehlCfinPE-EwlNOksdBGhZRv__224uovM8XRGyDhiVduIBemo0YjBlXEnktowROoPjWeDO3La6jXbOaWUB3sa97Rijou1ygQAn4p-JtaPL0bnHMHrt0lmAyCV706gBWlhbcnlHTPd1CQMY_m6zRzDNUMbIyOTGj-No7ixtL-062EX_S7o6xR8Al0pWGO9FOqQUFzcHflL2-mAegjlip8kzgEseSrkYlEhAXMTfVzk-HkJt4JTIWT1lu5KxmTgAQjMba3QSn7s7a4Eo0Vz_HL_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125079" target="_blank">📅 18:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125078">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار وال‌استریت ژورنال: یک منبع نزدیک به آژانس بین‌المللی انرژی اتمی می‌گوید هیچ فعالیت قابل مشاهده‌ای (از طریق تصاویر ماهواره‌ای، یعنی در سطح زمین) در سایت‌های هسته‌ای ایران که سال گذشته بمباران شدند، در ماه‌های اخیر مشاهده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125078" target="_blank">📅 18:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh1CJfaUEvdRAFvCGTQZb7GPAf7qtLtCfK5oRukG7WhErRl8NE9BCVvbfCQadkCEFH05A6e6IVQZ24MTy2_uaKAfsmNGlR5N4hb13LCxTSLubELWmiNpCsT-fA8sO_93ymfnyIn-bShIgxicTjK4AWGlvypNnsUyIACopmOHbzzc2pZGSqWfMZd33nOFbkiN8phDAldHxdrHmKvClZbq-5gF-3vpt87eIzkk72m_-DuGvpakYIkmRTaHsNK1HvsNtRJTuyJIgOljgpDqLGK0DVustBgrnD0rEMZ1AsA-DWjeoj4q9-lR6vxdPW90pTg9sm7WxMRt8Kv5gVFYHtifGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید از آقای قدیم سختگیر تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125077" target="_blank">📅 18:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFlO8i4wbE3PopY1VYjsE2of6fbaoNCyEYWQYELc8esxpTm4xPeo_bwJ0Mm1Ytb6UlQx2DkBG61qYpAuw_WnjAaoN5qWVJx3B7RVGgi3bNspVInIkvYsJz-mgN6yg0kEsZf_6UabmN2Hc4K5ZDoEC2ckwJ70psbvRk6JG5YwoYHDMJh2O6jqQdCwUpkXs9TyYD7Ay0goHLR7CwXZJC8y44nfcS0TgMBGHLef3oZFtTaIjjSWGnHxhwKxhdHxQxbQZUJ6Nu7OEBZvlmXnR_akuz_qC_V50ri5xVnN8g_UBt2HYXiFKhPw2tnScA4ExYWeV6wTMuyvXzW2vSbOzIjRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس صداوسیما: به نظرم جنگ تموم شده و دشمنان دیگه جرأت حمله ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125076" target="_blank">📅 18:28 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
