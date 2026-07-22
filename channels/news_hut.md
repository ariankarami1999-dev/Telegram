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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRKDgQG7yrNvq8T61GwBwB1PXd8qJOO3WF0LFMvDLDIp9rfEHt2JL16p_h-nagSWYbyVNnkhDLUt2oSRfQRKFI-8hG3UaUQCmnR4X1A0S3BVzoP9MsYxrZhtjwXFLk8WP8QfHob-sbRxAafKtjRmHBg4VPMrSxp5_l5Zy3MUDZsdt_-07NbJhEimXZ5VTnQoD_jMEI9DkTD3_9owLDf5wxg0cgmS0-28vCxzZ9PtKy9CjjWE8-isBOV5vtLJFzrOop0EsydEkxdnWfzuoPvhBF_nk7MyVGC6uzB8A9YSYdAQ3rJroIra0gsNHd6kUUk44uVp9pu5_LNoat0ZIlAQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyYem9zgZQJE0NwiXY__CFPfgyn17MvcolECKZJQrwXxl-bV6BEBARPhMJUJ-_Ie_lR11U9B0nn4UdqrdnlV3kUwJDGUwe7NDIewDEgX7lEqwWO5FIaqz9YeHiSfS2wHBB-AvIpsH0D1I9mlTdwf_yYNxaEWTjjYiCTlvghdmZfVlFL4OHUaYPH3rxR0la6RmGf5xni2DN_em0PNkgVD0zCVa7fupkN53n3MAiquTrGvJmqZYffC08wfMsgBjouCD_1i-enE3ODY-xyvjKCt8qtoMSTBANHAlFo2B_lsEbla_Z45LSISK7BsQorQIXecdBSnSqT7ADqAauynpoTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=bM6YgE60k6qbm-kDBRM6wgaqiyn6xv2pWrniGGI2UfDb4Jkl-1dDul_1rZyTVYeOMtgfI41lOKxfQV3RYQhE90MFn93k88Mp04sPK77YXurm5uHDS3OmPIAJTie7Oio_oR_xI9Pt5UCXWtjPOXJqP0MjIHSPD-1a0wQ-6gUaq_kVbpDDkBD44FJXZg4-OM11hFXaSnfOvm_9KUrdKKbORYx0Gga3VLXPV1k2UXr8DTMm2wqdx2L9wL-yffXWxsWd4LJoJYZkzCGfNmmhpedB2fUDId6byHyYZjHBXHvhOKd0HiOcUYsyycm5LFVbQOpLqjKs91nGUYffYNxv1zFFNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=bM6YgE60k6qbm-kDBRM6wgaqiyn6xv2pWrniGGI2UfDb4Jkl-1dDul_1rZyTVYeOMtgfI41lOKxfQV3RYQhE90MFn93k88Mp04sPK77YXurm5uHDS3OmPIAJTie7Oio_oR_xI9Pt5UCXWtjPOXJqP0MjIHSPD-1a0wQ-6gUaq_kVbpDDkBD44FJXZg4-OM11hFXaSnfOvm_9KUrdKKbORYx0Gga3VLXPV1k2UXr8DTMm2wqdx2L9wL-yffXWxsWd4LJoJYZkzCGfNmmhpedB2fUDId6byHyYZjHBXHvhOKd0HiOcUYsyycm5LFVbQOpLqjKs91nGUYffYNxv1zFFNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfPi8-2vHXL_Hy1Rx8B2gR4Annc3Q9geBA1CONXFF1eakcGpp4sXfnLgQpMCH58MtrH1J8clR752c7WTIS7IgjzSTvqWaWr3XOWdB8RiH8EYaTUq9uL54rrVgKnuAYn8R_x0WO4ID0JA6Q7vm7MFB3eSmVBTcBJ7y1TkTSikt2N1QcermAs9usLRntcibi7QAMQh459uiF1mfiDi4yLDZzhmK4dLc6N2BZj16LvEoIfyldPpe5xaYZPt43uMprIlChBSTV6GZDFazg3NGLAQmJwUNY7AvKCmyjqjuAIZF8sraiSxRyd-ubamCVe-OFXdwXGP8WHqlGI_pEo3xBLOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA-RRtN9TwBOVJgKDXGyPG0jeDcz6XTBjKSeknden88zlzA66LtuAkcrdQH1TxGZC-rbdVAETqH9SjrseGXyaf4VV8MKZ1ej3tALsdu9jsPaY4LfOAV_i8KrqQMSOV5GUt9v4b-nInb1MNGPsA-LFDtbuA7pZTQfTgOf5vB_3nHBcFBD9xBLxQtTOiF3XvlTq01d6Jz3tWkdjd9QVxadUwJGTnjoWCPyKU0Ay39Nz0k-vweSQjr6H4C8u_mhIF309QiCh7ImzwPUikT9c0zxloWCHPCoWT9ZcSYOPHd404FN9D24eYFkiNQ4gKko1Uv_w21SHYQfZUWpzQGxIBYSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxCw4tMQs0tT0yuoDn7xuMCG1w1uPoQbqre3ZN2-z0vrat87QBW6IQgK4DAi-W13WKv5zZ4O-IJ5Uy3V3U5e8W6l8m5GXzy3lCS__Io3mQFP2iql_wX2w6vlj8IsjZpvFyby_zazFsQ1q91AFg9zV0r2d3Si65nX49H2_5WY-ILuCvQLZBDN4AYUEnIf1JHoJwlBYReZz-5OSKsLMOoCuV3IvsJnUtSB-280DZMOl5CeXfGpEC2ucC6fTR-l8_HrQ0Hm7pSegCi6BCMi_m0Fm6Ojk0Ea5t4V55tSOdYsPZjJnjcZSDPFYPGo_0pNL4wbtcRdzZf8uT_MtmFd8vWPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=AeN-pTInMgEZCcY2IooI_xCimuF_KuV_vyEkISQTx2MOHkTQN0lnMiLA8EAoBIt5ub6A6wmqDafvnmXoQk6w3XcwKBvXuMd7gepcGRQ0FFa8qGqRhoLoyrBZdIZO3oRMKxR65bfVqTamGeSki30d51GPbC3CK2wfUlcu1aqsDbTk-PKp2arXEfjpYfUUqdBvga-k-FJkYX35a7zCzNSIpI-LwRNux5XJonblqoQs3hgld0LWDOyiFhLZ2BWiNjftTWP1z7rhNZzInWPS7j1MehFDPzW-rCIW9yZ_sDRJLMsMkcf0Nifh2AC2enZixR_u7glBny-i36CgiPWAWTnlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=AeN-pTInMgEZCcY2IooI_xCimuF_KuV_vyEkISQTx2MOHkTQN0lnMiLA8EAoBIt5ub6A6wmqDafvnmXoQk6w3XcwKBvXuMd7gepcGRQ0FFa8qGqRhoLoyrBZdIZO3oRMKxR65bfVqTamGeSki30d51GPbC3CK2wfUlcu1aqsDbTk-PKp2arXEfjpYfUUqdBvga-k-FJkYX35a7zCzNSIpI-LwRNux5XJonblqoQs3hgld0LWDOyiFhLZ2BWiNjftTWP1z7rhNZzInWPS7j1MehFDPzW-rCIW9yZ_sDRJLMsMkcf0Nifh2AC2enZixR_u7glBny-i36CgiPWAWTnlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=gdtoUG861JdgvRn59sKiY8Lkf2iaazGp-9Asq2kjncvsCTNtFd2B2N4x9TaOGmAhK9ch91Kt5TPUSA45A1QhwHv9FZN4nQPvqSZorus4Wak7r0y67bI5Lrx7p3rh9ofX73iu0Pg59sFYceUGyLfeGg3-RtfWNlKqaecRgpOPw1TivUIBZqe1JhmrBwwyFP9LcBiWRQw0zpzDKuNXMLUsD4yYW51ib4iiluXpcTt_85GUlrMEg3vv4d66Fgb84_vT5apV_ER3sWNent6kv2NPBR9O4tya8w_vJB4RN3hzDCNnFIYV_y5K9KpRdXRdoeO4K-bPccQctT9OpzgzS8r2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=gdtoUG861JdgvRn59sKiY8Lkf2iaazGp-9Asq2kjncvsCTNtFd2B2N4x9TaOGmAhK9ch91Kt5TPUSA45A1QhwHv9FZN4nQPvqSZorus4Wak7r0y67bI5Lrx7p3rh9ofX73iu0Pg59sFYceUGyLfeGg3-RtfWNlKqaecRgpOPw1TivUIBZqe1JhmrBwwyFP9LcBiWRQw0zpzDKuNXMLUsD4yYW51ib4iiluXpcTt_85GUlrMEg3vv4d66Fgb84_vT5apV_ER3sWNent6kv2NPBR9O4tya8w_vJB4RN3hzDCNnFIYV_y5K9KpRdXRdoeO4K-bPccQctT9OpzgzS8r2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=qr9I6PFKndnPxis62smCQXIXnpDf6Myv4b6F7-o0ZTqI0QJHvdONbrQSfC_oYCoOkvhVn5ib5wvlkEURSuOJc-p-xqEb5T-YWAxH8stOzaJceeLa64d_w02JRKefcCRExxbFlJV9IdhrrRf-qPu4G46bLFxV9kNisUPRDEMtcGSYLKR1i0tQQpDnQlPswym5q3TWAX64XrVlzLsUivT9IwFsnuITsv6ondCCBB1FTxEX4LebRzRUu-SlYdbuG-7uFDp57V_frSzCqnwqvFpqy2PSs-KtMFjCAVLgbo1ZOu1a9S8vrprYfzcfMNd-SgPw4qw3hgFrDBAj2MvNKEeKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=qr9I6PFKndnPxis62smCQXIXnpDf6Myv4b6F7-o0ZTqI0QJHvdONbrQSfC_oYCoOkvhVn5ib5wvlkEURSuOJc-p-xqEb5T-YWAxH8stOzaJceeLa64d_w02JRKefcCRExxbFlJV9IdhrrRf-qPu4G46bLFxV9kNisUPRDEMtcGSYLKR1i0tQQpDnQlPswym5q3TWAX64XrVlzLsUivT9IwFsnuITsv6ondCCBB1FTxEX4LebRzRUu-SlYdbuG-7uFDp57V_frSzCqnwqvFpqy2PSs-KtMFjCAVLgbo1ZOu1a9S8vrprYfzcfMNd-SgPw4qw3hgFrDBAj2MvNKEeKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=ZRuPFT5u8854V8L4RmDLljr5y3nT9zNulnFIqO7RB3arxQCLSLOy3g1v-TKi4qXeBoCbuEkpiv3ErfWA8t1dc_YprNeoo5mg7IAFmWVCe99ze_SAKrjlsqydQ0hu1MUb7QEyFiosdpYA5nv-7ViCKkOJnz9dCd5qyZxMCfOOhwe4VzAVd1cRuCSXEN4_xoCvMf4H1j0eBqPB4BcjlaAsnnNHbuT9yeO6BBINAA2ThgxoYzorzaKf1pVS2pQe0H1_CvQvVMIk6oz_wOhY8iFKQiCCRK1fHn7MgsvGFBEqmm9qhh-XClTPmWRjX6uaM25fAFiu4PTy8GHhueS_nrKxrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=ZRuPFT5u8854V8L4RmDLljr5y3nT9zNulnFIqO7RB3arxQCLSLOy3g1v-TKi4qXeBoCbuEkpiv3ErfWA8t1dc_YprNeoo5mg7IAFmWVCe99ze_SAKrjlsqydQ0hu1MUb7QEyFiosdpYA5nv-7ViCKkOJnz9dCd5qyZxMCfOOhwe4VzAVd1cRuCSXEN4_xoCvMf4H1j0eBqPB4BcjlaAsnnNHbuT9yeO6BBINAA2ThgxoYzorzaKf1pVS2pQe0H1_CvQvVMIk6oz_wOhY8iFKQiCCRK1fHn7MgsvGFBEqmm9qhh-XClTPmWRjX6uaM25fAFiu4PTy8GHhueS_nrKxrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=vSeWusnKiSrr315VGnboIJLtmrYiijgbVo67kbwy4cLq3o2qiotQoEIhvqu4SdhsvRjmvgEMmqoMN16Ytz4kAQPKqajaS4_55QDX37uRQ32NMP282_QIf5lfmjzRDPlyFXJbF2cBKFiTu-6e3590MeQROnDFWaUqOUH-uH7EpFxK1uk-VGaVwZILxtuVltxaWGKo347uT4jsrpaU6_Q_y1o1waZtKtxltmNMOZtjkKDRV41g0EsKJ-YFTyMohnXRoCXY1vlZRmblOA_iNH7f_hobBNRzZAMxg1DUTD4EqyW8uh8vx6IOiR1EfeT-8g_PkQVf8y3azL9xxf5VJDJ6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=vSeWusnKiSrr315VGnboIJLtmrYiijgbVo67kbwy4cLq3o2qiotQoEIhvqu4SdhsvRjmvgEMmqoMN16Ytz4kAQPKqajaS4_55QDX37uRQ32NMP282_QIf5lfmjzRDPlyFXJbF2cBKFiTu-6e3590MeQROnDFWaUqOUH-uH7EpFxK1uk-VGaVwZILxtuVltxaWGKo347uT4jsrpaU6_Q_y1o1waZtKtxltmNMOZtjkKDRV41g0EsKJ-YFTyMohnXRoCXY1vlZRmblOA_iNH7f_hobBNRzZAMxg1DUTD4EqyW8uh8vx6IOiR1EfeT-8g_PkQVf8y3azL9xxf5VJDJ6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL6VLriQsX_DuNudAm38DpIXjEaaU0FM3r7-DmvBDRRAlZo4VTQ1alQ87Tai4pMeJDFa-gzFvDY9Q9Y3OByFQNXlrmkhiT12ZKX7Ho5OOtIKmM4AU6s1TZrlpVLvX569P9AiGT3dUAcKE3pLJwism8zxfpXAmhvl8UgBykvp_14QuH4_EGGZntFx7p8ATLvE2k8urjCAjKO4gcogLymIZLG6KBD3MFDQ4ZUfgRUJr5jelTZo3lTbv_fpnCNiWaKxfmVfQDO6Rx_ON76FBjl6rv6PqEseGk7R68LrrVHgc9Iv0PtdmJOooOfXqfTlLrnThsiU6WE4PambJ3R_AdLT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYGnF-q4bgMd3NeOV1unJoHkNrYOoILXELuF0epnUpxyPXu1LF8HH2Nk5NE10NuSR8nsHI8KIxyvcoAp3pGJeVI8B5Y-HjcbaNMP2-0h1Ftnib7zrI321134JfDfRPkClbI1SvKCMsw8zdvKhrVcepAH--jBRdM7HoiTgkQV1jsIrRkYpksdmATjco2-AvX3H-nlHVy-VH7oTCilsN3eXQC9xX7b6fVENoqGok6NnYJ77bSQzBfH48oN5jCyOuu6bFd2TuCYNz32RB9b8ewhRPlx1NfmF5BWUE8LKeppDmWat_5G1cmRiMlKD2doNq0Y8z0WtUAnYQNX6rUr_0fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=EZn0sm6LfsEkh1iHV3JmQMhtpqkeluMf7JHyRjUIpLxHruyJghfDmFcrF3paGc2QO6qeSOsITxox2LXcmJswOWrVYuSE6hy6Gp9Cjbr6RKArxSiyJbMNcv601UKBGclyednuKfvic41RRymKaqkOVPA8zjpep09EVFv2N8Ybb5Q5GhmoASuz2stVUIvEDYQ9cgREG0Ludf8YJAq6qHHkcCzg8h2HB_ItITcYz6zPvsrUJLQ5eQBJ2Qt_LVIs2qZvDBLLr-eEhpycpkVn4mycJacZOAKfVdh8z5z_wdyrv8KaSK5rvRbQHTZcikQzaoB5tCBpSSE4o6k6OUqRDDdnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=EZn0sm6LfsEkh1iHV3JmQMhtpqkeluMf7JHyRjUIpLxHruyJghfDmFcrF3paGc2QO6qeSOsITxox2LXcmJswOWrVYuSE6hy6Gp9Cjbr6RKArxSiyJbMNcv601UKBGclyednuKfvic41RRymKaqkOVPA8zjpep09EVFv2N8Ybb5Q5GhmoASuz2stVUIvEDYQ9cgREG0Ludf8YJAq6qHHkcCzg8h2HB_ItITcYz6zPvsrUJLQ5eQBJ2Qt_LVIs2qZvDBLLr-eEhpycpkVn4mycJacZOAKfVdh8z5z_wdyrv8KaSK5rvRbQHTZcikQzaoB5tCBpSSE4o6k6OUqRDDdnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=q1c05QqEcoA4VVfLAYhSh9M0JSZkJtkuHWwN1uWFRjoUidGIA2XrS9uZU2faGU-WQv-SiUof6TCCixcZe1Nh-LMF6s4f7hFwIOt7g6jqc6rNfqrcUvDy-PcvF3of8Z_J5Y-Ksf6zKa6XBZQ7JZPmjAWkAubZEKlneLm4cWhhr9OeUkAYT7t9Td6-MPUq6oxCR6ZEqNp9-fX8uBnk7y2hoS8Pf-q6BSZvdAf69kl5XSrtUyXaw6q71uzJaMFYO2siKV5YN9C44c4r-1jRPmFUcRid73mXomDKAiAqqj6yESV_Eg2V8VBqxAJG5USMaBeR-KY-v6pT_pn8nigFpb_NnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=q1c05QqEcoA4VVfLAYhSh9M0JSZkJtkuHWwN1uWFRjoUidGIA2XrS9uZU2faGU-WQv-SiUof6TCCixcZe1Nh-LMF6s4f7hFwIOt7g6jqc6rNfqrcUvDy-PcvF3of8Z_J5Y-Ksf6zKa6XBZQ7JZPmjAWkAubZEKlneLm4cWhhr9OeUkAYT7t9Td6-MPUq6oxCR6ZEqNp9-fX8uBnk7y2hoS8Pf-q6BSZvdAf69kl5XSrtUyXaw6q71uzJaMFYO2siKV5YN9C44c4r-1jRPmFUcRid73mXomDKAiAqqj6yESV_Eg2V8VBqxAJG5USMaBeR-KY-v6pT_pn8nigFpb_NnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=WGHqzRNHvflGP1DdHo8h2hdG6sOqmD7vi-Nlk1HbRlRIXv-1HmK667P7JrEgtWGw2o2915S6wxtt3Dkw4i5OXqRl9p5UIurCNvxTsugbg0G-4cV5_0zYBuXZobtnHZ1B9UcP64xgg7cuMNZ0Jqb1YMJApQVtaVG4qpAMnF16LERB25z34qFHc6lGoHOaMYASqh5YzRc7LY_pQ1aJAHgcyzIjuTrR-eo7Gm5tK_FS0lqk4XIVNHNweuocViT6RdtLuaWXajFsrLff1ST0e8uYoRBRX92RPB9S5g9-yiAj0madOC3VbYNYS0Ki8H2DPx4FPYBIanE5uSkSXYUOTg83HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=WGHqzRNHvflGP1DdHo8h2hdG6sOqmD7vi-Nlk1HbRlRIXv-1HmK667P7JrEgtWGw2o2915S6wxtt3Dkw4i5OXqRl9p5UIurCNvxTsugbg0G-4cV5_0zYBuXZobtnHZ1B9UcP64xgg7cuMNZ0Jqb1YMJApQVtaVG4qpAMnF16LERB25z34qFHc6lGoHOaMYASqh5YzRc7LY_pQ1aJAHgcyzIjuTrR-eo7Gm5tK_FS0lqk4XIVNHNweuocViT6RdtLuaWXajFsrLff1ST0e8uYoRBRX92RPB9S5g9-yiAj0madOC3VbYNYS0Ki8H2DPx4FPYBIanE5uSkSXYUOTg83HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEiFZcmpWrge8QbPIOjV3Sz9S-9O9XnlABEf9RzOHjAPb2bf4VED5MSTADL_oSmKpYjycEsk98kX3g7cujMfy9pYzewn83jDkefrGRrgBmM5nD2b6ULqM2nM6OV3GJ1uNtecD1E7vC8zg7f33d-lb-W1l70F5V7FmVit591E37kWUs4BZPdbmSbyOY2L_KFeJ005gO3oSy8pF4hrQsAFDHfJs8EJHWckd_ccTyLzQThl1YmFQv6v5X3pFQbgONI1pRiGV5EqOPYVMDN5ZwoNWkNoMb821z2x7eES9bH4RoiL-WLVtOKkWpuS-6rxYgRt3XlOAoWQfEsI1Bzay1z_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=I2iB3lgGbI52DTBFVuylad761Di8bY1NqYf-BGqWiNU5kh5HiVPHLOxU1MYIxgcfRfsys8Ylo2avSRXu1LZNgcElvTKrWvC9eBFQYhXE61B9cH0LuwrgUxFz5xuFVIAo8-HkvzQxyXnjy1EYOYNoc5qKvhfmFn92X0WCEh2G4UNaQrAVwKsQ9gvnUMP4rwKG-kxeXZhUtIFpD650ZECJBB4Hvld08lP7MDQhTgD6YTJ8EfyAgPXWlAyes1RjPzk66r9ZZGoaLPvPxsy7QtH4zygQznvuPstp6fpbsgkhOmkF4oRxCwKqIb0sHf46_9Sakd2BlCXB5h3Y8SHqFodM5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=I2iB3lgGbI52DTBFVuylad761Di8bY1NqYf-BGqWiNU5kh5HiVPHLOxU1MYIxgcfRfsys8Ylo2avSRXu1LZNgcElvTKrWvC9eBFQYhXE61B9cH0LuwrgUxFz5xuFVIAo8-HkvzQxyXnjy1EYOYNoc5qKvhfmFn92X0WCEh2G4UNaQrAVwKsQ9gvnUMP4rwKG-kxeXZhUtIFpD650ZECJBB4Hvld08lP7MDQhTgD6YTJ8EfyAgPXWlAyes1RjPzk66r9ZZGoaLPvPxsy7QtH4zygQznvuPstp6fpbsgkhOmkF4oRxCwKqIb0sHf46_9Sakd2BlCXB5h3Y8SHqFodM5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=os1JR1mZsontjLr96cTW74RtcEEezUeNkAz8v2WXjndbvLf7-QWY9iG7amjDer7-1iL7krO-KAK8OXQwZrF0q6rkfI2A6RfOIWO5P-PyNqHjf3SiZhJmiQFe1aRGyWXWs8gbN16lhO9Dr6LvyvfqG1G50dOwfDobNkAwQI3wcy20ZtVM_sr3WtDk3Lj6x26TaVgugi4zR0IgX_r8X4F2oYm9JI7uZlj7P1oLNEswZx2oH3bd-1kixSrmy5Mf49bvsC52MSYNfpFn4le-iZSjD8jNaa51RHEp2g8Uj8gTYnd6umo130phihv_CUnHlZf4r1IXrWzhvtUmFtoNP55BWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=os1JR1mZsontjLr96cTW74RtcEEezUeNkAz8v2WXjndbvLf7-QWY9iG7amjDer7-1iL7krO-KAK8OXQwZrF0q6rkfI2A6RfOIWO5P-PyNqHjf3SiZhJmiQFe1aRGyWXWs8gbN16lhO9Dr6LvyvfqG1G50dOwfDobNkAwQI3wcy20ZtVM_sr3WtDk3Lj6x26TaVgugi4zR0IgX_r8X4F2oYm9JI7uZlj7P1oLNEswZx2oH3bd-1kixSrmy5Mf49bvsC52MSYNfpFn4le-iZSjD8jNaa51RHEp2g8Uj8gTYnd6umo130phihv_CUnHlZf4r1IXrWzhvtUmFtoNP55BWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=Z8fzL3UccWY7bNCRnM-9b7Qfb4rW2fvs8xoOtjPBA5m3bEfFt0DfjEOcDTDgwnbZXCBlTXkJNmHm2d5UhIVI8J0KHwjUjCgv0Fw7OKRJV7KT0KwonUe9-n5rUjoauQ6zuXjb0uJ_yRcXbnOahBwJi6CUFqvV9CKGLR0ZntR3y3iV_EDLlvB49xR6g82oDsoTIANj-8_ed9wmveF2H1ZTkBvokZIKnPo3v6ZCZIyDhFTIdTdpyVjMB9nOGcwHfrP_ZncjjiUq2OI2y1Librf9d0t9-stACczdx8EJGn8y6wrMizu7o_y-Rbz3IJG6taW96KSd8W9IMAtArgLBat85iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=Z8fzL3UccWY7bNCRnM-9b7Qfb4rW2fvs8xoOtjPBA5m3bEfFt0DfjEOcDTDgwnbZXCBlTXkJNmHm2d5UhIVI8J0KHwjUjCgv0Fw7OKRJV7KT0KwonUe9-n5rUjoauQ6zuXjb0uJ_yRcXbnOahBwJi6CUFqvV9CKGLR0ZntR3y3iV_EDLlvB49xR6g82oDsoTIANj-8_ed9wmveF2H1ZTkBvokZIKnPo3v6ZCZIyDhFTIdTdpyVjMB9nOGcwHfrP_ZncjjiUq2OI2y1Librf9d0t9-stACczdx8EJGn8y6wrMizu7o_y-Rbz3IJG6taW96KSd8W9IMAtArgLBat85iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=jbF1BH-jJ6i4USA3x4B1z8bLn8fw4PARX_x907GyIVYsPdiG1Qn438pd5sOLWFsElsVLzEfojJLRA0YAmwNRos8tOsvDropKjyVX9cL4WGLbxF9ddku57bf6NkquLVrI5o-V7Bfte5xw5_2-1w_ze_s2L3ZBKx240NyjvQGU0ackY4nNLECQEmH2StCEiBtRZQUWk64UggnVpviEYSHnEaMarhYcGX-ZvIdlCWsJUBBktrFa__lxd8BDbuKqheX1zIP1U-0J-q0g58qZvsz5Jsp4-e6AjezB-l58SKTGDDFXML26S_kAQwzZx-ZDVh9TDGjgxJ4CQ44ePAgCX2o3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=jbF1BH-jJ6i4USA3x4B1z8bLn8fw4PARX_x907GyIVYsPdiG1Qn438pd5sOLWFsElsVLzEfojJLRA0YAmwNRos8tOsvDropKjyVX9cL4WGLbxF9ddku57bf6NkquLVrI5o-V7Bfte5xw5_2-1w_ze_s2L3ZBKx240NyjvQGU0ackY4nNLECQEmH2StCEiBtRZQUWk64UggnVpviEYSHnEaMarhYcGX-ZvIdlCWsJUBBktrFa__lxd8BDbuKqheX1zIP1U-0J-q0g58qZvsz5Jsp4-e6AjezB-l58SKTGDDFXML26S_kAQwzZx-ZDVh9TDGjgxJ4CQ44ePAgCX2o3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=BIdHFiNtcaO3jV7v6oCRxCONIHlvUXEuVr9fwwKSuYbY5nInnOC0pRg0yjltzdRXe09HC4HaJFrA3TJ_pW0ViJriVC4NT3D2K0FOscRxSjI01Mt7Y0fyUwZenmo-U-qzmLXYaXac215YAkACIntPKE-t-TRj_sPduwgiFPGO1IcX3pKtDd1nDQusp6_XhCyLqQPV3xEsvXb9ENvdW89UUPLyze-KI-EdlQa1Y7wtkMtVIR0qeDaUEnskg4Cv9UCMWreX5bxdGWiGZdVmJ9mbDxz2Qdz_8FlZe5i9HydwvCPntADglPRoGq961bV_H2DWhcWuK9KlY1eH3TwQtStgYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=BIdHFiNtcaO3jV7v6oCRxCONIHlvUXEuVr9fwwKSuYbY5nInnOC0pRg0yjltzdRXe09HC4HaJFrA3TJ_pW0ViJriVC4NT3D2K0FOscRxSjI01Mt7Y0fyUwZenmo-U-qzmLXYaXac215YAkACIntPKE-t-TRj_sPduwgiFPGO1IcX3pKtDd1nDQusp6_XhCyLqQPV3xEsvXb9ENvdW89UUPLyze-KI-EdlQa1Y7wtkMtVIR0qeDaUEnskg4Cv9UCMWreX5bxdGWiGZdVmJ9mbDxz2Qdz_8FlZe5i9HydwvCPntADglPRoGq961bV_H2DWhcWuK9KlY1eH3TwQtStgYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0LK-jGlpH0fJw9hxHo6L38u3EK76wGS_ETTVzcsrkFgHtkDeISJWMCy9RUAbjaOoOnq7vz3xp4aOQJYtEFkG6lHdeW80AvApTw_LY6ODwy2qqGcWKS3C6fpZI-80zSqMglnWPDNklrOReV38DGpkP3OInGEufYNKwqBT5d3oAMdK1iyYC483_mwnUUZJO23hWN3L1JpfebUPWW963fUKzDkK4RZrzMjYhEbh3jTDhu2Z3Xekk8TIZ5YNtaunRlmlT9y2aXyzytZ_W1Qub3pMoS0lY9CCjl8jGq8PnuOB8qFzDSdTYBQPNMJiRD7setErMI_waFvuaAZko4qoS1XxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdiPyFJt9DlYzxM_xmRfLAumL3rDPGd-0cneXf5drX_kzDrcgCumGhU2_Ib8Ta58vCP54F6ZzjONlkqtZ7XxwVwhvuzW9_vZAXtZi7hvEhzEhAuHNtv2927qpMETdJiNplAvtjLuZmf1q2n4ZMhFQAjoxIqdqs0V2DKphPm556Lx71GNBo-KvJpexR5ecMzj-UPx2RiKBjvk3-j83Awwu7t5Lq7SZZzJqfJgWGviEGy333Al1COU9jh9picN4NrjCstFZvZBGmrUp765YE2fjhA_canwsif-SFgu1pHjd3i4HQNp4poaxaDx9UcVfvGH44NyylKuuCn3p257MoUaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=cw6BsUsTo9Ayj0zxscQSUe4KGbCXrx7Vu5K_Z0iOJkc2r07VxsCEvPKBLZPo39q-vjbckhHndCxHWvpfbeNIsjm_HsHA3xwKpwloztHR0nnO7xAHDnBnIr4K6dsWKaqSP4DnDysaclgsnSBbA4PnVqaWSSCMBaKbxFlr2XaheMV1mQS9gtZcsQQwMCACpJ5B0s39D_H4XW1Vak60gYA0_pc7GoUsvgQ30AP171jbm0do3ljsAP_4116Ejvb4Nm-CjvOy35Nc_Yy9dQUuPCD0w3eGYjXrCrKTbGsRisDu9ULZGI3VGogw0jSt1_vegieqGvUyWJk5XtVGGoJJmwbf9Fp-tGlJShMlzPWsncoqXOkTIssZIL5knDq-Qd1xxNzo1zU_oxEotoZwteJaKCw8lAz7oARaXFTp5vD0Syj3T_oJ-Gys1BdT3BP0nqr5iC1z9GsBCu3Ch3zooVRvPchgkhi2WK5v5-uncjjPhhzHd4Mn7OuMohWhcuZ5kavBWMOGnH5azUW5mc-b6xveRmmhsRLauNBnkeCXcifV7Zg1ke9xpBP0TZmQRopKigCNRuh2zbI6XBDafzzjWkqD45KdMrcUE2IIfEbcuzqntpveY9-5hNs7GO6JvixrX17mmBgVEMdmKC-hV-rCQsBND1phkCzn2in_HZ7upM50TMjAJio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=cw6BsUsTo9Ayj0zxscQSUe4KGbCXrx7Vu5K_Z0iOJkc2r07VxsCEvPKBLZPo39q-vjbckhHndCxHWvpfbeNIsjm_HsHA3xwKpwloztHR0nnO7xAHDnBnIr4K6dsWKaqSP4DnDysaclgsnSBbA4PnVqaWSSCMBaKbxFlr2XaheMV1mQS9gtZcsQQwMCACpJ5B0s39D_H4XW1Vak60gYA0_pc7GoUsvgQ30AP171jbm0do3ljsAP_4116Ejvb4Nm-CjvOy35Nc_Yy9dQUuPCD0w3eGYjXrCrKTbGsRisDu9ULZGI3VGogw0jSt1_vegieqGvUyWJk5XtVGGoJJmwbf9Fp-tGlJShMlzPWsncoqXOkTIssZIL5knDq-Qd1xxNzo1zU_oxEotoZwteJaKCw8lAz7oARaXFTp5vD0Syj3T_oJ-Gys1BdT3BP0nqr5iC1z9GsBCu3Ch3zooVRvPchgkhi2WK5v5-uncjjPhhzHd4Mn7OuMohWhcuZ5kavBWMOGnH5azUW5mc-b6xveRmmhsRLauNBnkeCXcifV7Zg1ke9xpBP0TZmQRopKigCNRuh2zbI6XBDafzzjWkqD45KdMrcUE2IIfEbcuzqntpveY9-5hNs7GO6JvixrX17mmBgVEMdmKC-hV-rCQsBND1phkCzn2in_HZ7upM50TMjAJio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=Y3-C4VeKxLPdzT4Uqmb0iNMMW-o9dY78G4C0vhwy8Gignx2AmQiOYl-vyJ6htShbQMQLaU8vDy1_IwhTsoVPJFF8vsy937nOm0FSDUEJoez50hgb771DwvAsgTsvOMbaZl1NOQY-WmjH_70SG71syKEYg5Zei57PO5R2Wx0Ft9PSq4LU26LpWEKgtXyCO_GckL0dsOx-fFyakyh0yNc1UTU7aa67dorP4kidG4vJqz2E1C3W1d-Qwki2xsu0UoV1qRYvbcC2-aMRvLueflDh5Bm91IgQRprlTaTFNNnXlaJ8UOhGuudfo0oN3YxyzIIeyZMqxXGx54vukklSsh4E5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=Y3-C4VeKxLPdzT4Uqmb0iNMMW-o9dY78G4C0vhwy8Gignx2AmQiOYl-vyJ6htShbQMQLaU8vDy1_IwhTsoVPJFF8vsy937nOm0FSDUEJoez50hgb771DwvAsgTsvOMbaZl1NOQY-WmjH_70SG71syKEYg5Zei57PO5R2Wx0Ft9PSq4LU26LpWEKgtXyCO_GckL0dsOx-fFyakyh0yNc1UTU7aa67dorP4kidG4vJqz2E1C3W1d-Qwki2xsu0UoV1qRYvbcC2-aMRvLueflDh5Bm91IgQRprlTaTFNNnXlaJ8UOhGuudfo0oN3YxyzIIeyZMqxXGx54vukklSsh4E5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=pn2XvyTuizPr0hXwfhBw9cdq9eGlxNZqQOY3P28aVb7RO-g_6Xu2iS60CxuUrOvo3LIVlBOiSnainuFbqrQzYMfx4vXm-kJN3KPkJqt0vDyVmuC0weI6Fyq1Z8H8GAoU-WNwRqRpzsWHGjh3nWIXJqWKsuohqHze38Ts1cjkRULQc5H6VlyQINGCwEwzS7jZViDwSTq0ZMWmDuvetvM-KwQV0ueJ-lkwMxPG6ciPmQ_61CeyIwm5OObnZAaSrOYr6z5AIU7cxR3uqP9K6dAaSkPTwWTZ2_J8rYAiJHcJP75Ss4ngXOCRejog3-AQwpfMqExjRy90xq1iFZ9OOsGQOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=pn2XvyTuizPr0hXwfhBw9cdq9eGlxNZqQOY3P28aVb7RO-g_6Xu2iS60CxuUrOvo3LIVlBOiSnainuFbqrQzYMfx4vXm-kJN3KPkJqt0vDyVmuC0weI6Fyq1Z8H8GAoU-WNwRqRpzsWHGjh3nWIXJqWKsuohqHze38Ts1cjkRULQc5H6VlyQINGCwEwzS7jZViDwSTq0ZMWmDuvetvM-KwQV0ueJ-lkwMxPG6ciPmQ_61CeyIwm5OObnZAaSrOYr6z5AIU7cxR3uqP9K6dAaSkPTwWTZ2_J8rYAiJHcJP75Ss4ngXOCRejog3-AQwpfMqExjRy90xq1iFZ9OOsGQOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=r7vgehxuUMtalsNqtGhQFUlsCS3VzmhdNzUgXySoruMXfnrGQ3kzXj3b_4jVJUVHRDHzwQyQAuc-wjTh_ue3oPDeD-zge-9VT-0H25B3aqqvHM1EDhm7bvG2UbcLJ94Q3cBdvYLrePht7gUG19_CeMkpMoZgMDXUeELfS2ss7eQO51PolxXSqWbNtiCqclCEF3B36QDcP6WtYp4Qr9Zj_vqVkF66pdMgmN-dtP8fbIr3xfNm6UQHi9ywsLzCikpjAvKsavUYRcEfI2Iz1grjSBN7-nj4jMeELf_nXE7w7Id6hanqiY1L--I1MTHgpYmYhcLyYN_js-YOAUuNN6ajqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=r7vgehxuUMtalsNqtGhQFUlsCS3VzmhdNzUgXySoruMXfnrGQ3kzXj3b_4jVJUVHRDHzwQyQAuc-wjTh_ue3oPDeD-zge-9VT-0H25B3aqqvHM1EDhm7bvG2UbcLJ94Q3cBdvYLrePht7gUG19_CeMkpMoZgMDXUeELfS2ss7eQO51PolxXSqWbNtiCqclCEF3B36QDcP6WtYp4Qr9Zj_vqVkF66pdMgmN-dtP8fbIr3xfNm6UQHi9ywsLzCikpjAvKsavUYRcEfI2Iz1grjSBN7-nj4jMeELf_nXE7w7Id6hanqiY1L--I1MTHgpYmYhcLyYN_js-YOAUuNN6ajqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhIChtd6mwQ-5RZGDdrOFDrvWpvmDKqK69YM4Kxpnwdc7iHg0L2ZkXBbRHOY-MAkxOSMdM5jCfX38RQt7VKLR1lJAYzMyJ4y9q6BQbif3-wLKg_qf8tT7WXr9INWU6SS-tZyI4kbI3V3dx1oHrNVm0vvVpLSRrhu5zXFz-z1tlllmmsxsYF-883ajTCkUbu-8T0a_9hTRz3-bURvrxvMzNjTdFa3YJowNw1AUGdSZntI-HWiN9-EFnhf7ZfPO2z-b6J8M8CHBEjXboDMPvqKYhDi-L_WuPFTR5dVMvU86W-n3-IHPIzj7Tvq309n81zP2YKb9yUq2qo3v5hN6u4T6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDfL-6jk9VrrOH4kATZhm93mWBAx_UqwrNEJTtfpxduWMLbvQLKcjcmWDW-5Fl0IbtcFnXMpeSJWR-aNeNQrUOR-vq6C2l1xYJjiLQDh1WMAMw5YNjDpoBD-EUYEVfImrBUYQBgKi7QYXEQ83c4KBiD1-9wrFc8AgdYvCXsZ6FVQaqElvu1vE2pm1g05xu8LU_StEifw4H43-rXmBvPGNbIYWpdmD7qk9JSFS8RK_MpbqV9C229FaWr8ucfQBYlN3rzRD5FpFMeU0uLQFglKxaepWr-s8_3nAe-vM_W7cLHkY-UNQmNwxl16q3txNg60eY1F0qM-yTWikwSAvnho5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFXa7vWX0TSGrjvFn7cBDnja5LVkJudPqVLuK4JeMENvz9UsEkIPSe5XA_xoFDNE8Z0_0w5qlpNgfXSdlFIsKdDyWU5lcnxIEg7lmETgEcuvNxiKAqgiFxoyc6ykEWhGI6Ko2vJarvzBk-rPqFtJbYhVk0rHV-AwPGI836FUNLxI-XkAj4Lg_J5tGawHPJxtHwUjSCMFlNNfuUTq36loIRbPfeIhwru82K84McAD-7XxFnITptHHHGOG8tx_4lRVlFNnPLNGar1lj8YdQQHGr065w1JxqW-bqDYJgmccNzz6_EUveL14Tlz2-_RtuYDZPMcnW4JfIF5sJ_9y2Iavjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcYaD5cWD-o1RlQ1Jewet3-aBijDctw7zigePjAatF3TaoReEzjBgI8jj8t94eowkIR2I7CSrWz307NK1YA_nhwXTGsBW9D62mND6JvFZayoSiEuIt-uXiKlliOcmsxRJ3aQ22JJ0URTYr8_kb89WknR27gEsbR0PsSRhuE3sOHMTZY6Ae4c1HrzLzd82Bn9KJlOZGrV8l7iGSDLGhoEsV-hbiW4s6GxjBaDnwvA6VD4hNMj6mPkgFpMDWIiVwJeBOYXOgGXV68fEUGl9JZjHSuBVaEHaDiT1s-pxCS3PFqdfLduthV2W4cI-B0GvKzQWr4UF8ZEj1XK_yiq4V16dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=PaL1uaTPyr1UaqjBEzu32PgW8uM5YemuAet7RHe_mI-mxJ6YdxYr954D4q2mLz2pcSugZnX9xX4J_If1LKRa-pi5fuPecy0zzakH4dH6iKTUNYv-qS91CqyphwhQ9Tc4Xkr06YUVtWUdEvuZ5XOHy97P5mM7wT4wuWLjuGBPNUWmgBbq_36ZeFPXpu878tVUzR5JQyftkH-eEuyos2KS3xevE4tVz8c-hunOzk4HvWOrx-6GXotip2n1J7aH-9Y0C6xXfIIvosBCo1uz5FmKCfxqUQOjtS03aXMbgxcH2rBXE-K202l1--NhalxVfoUwEsDfCBsVPWPDulrvqSf2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=PaL1uaTPyr1UaqjBEzu32PgW8uM5YemuAet7RHe_mI-mxJ6YdxYr954D4q2mLz2pcSugZnX9xX4J_If1LKRa-pi5fuPecy0zzakH4dH6iKTUNYv-qS91CqyphwhQ9Tc4Xkr06YUVtWUdEvuZ5XOHy97P5mM7wT4wuWLjuGBPNUWmgBbq_36ZeFPXpu878tVUzR5JQyftkH-eEuyos2KS3xevE4tVz8c-hunOzk4HvWOrx-6GXotip2n1J7aH-9Y0C6xXfIIvosBCo1uz5FmKCfxqUQOjtS03aXMbgxcH2rBXE-K202l1--NhalxVfoUwEsDfCBsVPWPDulrvqSf2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=schU_e3TAkILn6xM_pBbOPYlhDUW1YrLhWu_ZHdVDlyghzR6Kde1YgbGc4USRmL06keuwf0Xlz6UUGn486_KSSnd0qXsJgSeab6OOASC1ZFlq5e8W9po-4WL1j93IKGPrj6O32lHojc51ysAP7YucA0qeTnRGkOJnS8ttnLn0iW7OcFIhrwqu_WHrEWVFz-Qsk4A4qmrtlrFotFjwcYtyd8vZeWpNYiXIl5w_8urBYhleqT4xkyRvWaHaJ5wvmO8ket7vyF9KX8LGsHmTeVkXAd8BajYy3eta04zE4rEeUhODmutvRDPwtLfoLxPZn6ChnoZ37GbjqyO29L9PgCAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=schU_e3TAkILn6xM_pBbOPYlhDUW1YrLhWu_ZHdVDlyghzR6Kde1YgbGc4USRmL06keuwf0Xlz6UUGn486_KSSnd0qXsJgSeab6OOASC1ZFlq5e8W9po-4WL1j93IKGPrj6O32lHojc51ysAP7YucA0qeTnRGkOJnS8ttnLn0iW7OcFIhrwqu_WHrEWVFz-Qsk4A4qmrtlrFotFjwcYtyd8vZeWpNYiXIl5w_8urBYhleqT4xkyRvWaHaJ5wvmO8ket7vyF9KX8LGsHmTeVkXAd8BajYy3eta04zE4rEeUhODmutvRDPwtLfoLxPZn6ChnoZ37GbjqyO29L9PgCAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=G1BVASW5SlXx_UjYqGvVnwekBrfHKMlxE1Nhp2RUZFtuCFpsPbpD2e73Vm7N48U22kHz3gcoLCYVwZ57Tym4BhGGHmLHkCQtXU9Xfmd8ONXYxSMwbPdl7SRky2kJ_w3ioYxI0_Ss9iV_feiLWuwDuxYobrvHUPV1Isc30X3mhGTmXJxDVluD2unpPKy1fAvHsAmCxNv0nkcIfgj6_R4DYkFLyr0Hj4feW0tqZ_Qodba578uihEVmL9rvGQHHVXzYIWEqMI_avwyx1CZvzqQUSxuxLaIb-kHsgAgW2n1gH97Q2aXC-R_urU4tNq2a748JWKpgMd1WaH20BbBWc3Hj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=G1BVASW5SlXx_UjYqGvVnwekBrfHKMlxE1Nhp2RUZFtuCFpsPbpD2e73Vm7N48U22kHz3gcoLCYVwZ57Tym4BhGGHmLHkCQtXU9Xfmd8ONXYxSMwbPdl7SRky2kJ_w3ioYxI0_Ss9iV_feiLWuwDuxYobrvHUPV1Isc30X3mhGTmXJxDVluD2unpPKy1fAvHsAmCxNv0nkcIfgj6_R4DYkFLyr0Hj4feW0tqZ_Qodba578uihEVmL9rvGQHHVXzYIWEqMI_avwyx1CZvzqQUSxuxLaIb-kHsgAgW2n1gH97Q2aXC-R_urU4tNq2a748JWKpgMd1WaH20BbBWc3Hj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=YkY876XgDpXSwNsROhbsEAyoe922DFM3uGm0sblX-6q4jmUX-QDVnTXH-yvUaWoVkvPV0fKG2LRGwLSP9G_d9PmSQpgYxuo6eG2Cz_5CbVAt_4-cjRDkGOzAU-MH_Gadwq1ye0Wsgm5AjFbOC9v2ClRcBmwybSWjEQOFcXi9J43cQnW0jobVFAQ9_zttvjk0XNeBqybP-itJ47BwJBxUiwiC_5NN2UMdir2Y9G4EiNrnHrNrMESPpcSqvvxle9enEBBWz_qKWzLkiPJ_r8_qUb_n8BVlz8OUq3fdN1nlB2W3w4GpgjmUgGTEUujMFRVjzEyJCgA5paEGDOA-XlLc8pWB8xf4WH80EtiPBR3avDN52ZvCl_aBnrqDzWkTTMeCC7itkY5Qh9ME9-W7AExkzT47ey7DuMS4XG0MuCu6YTRNgVJck9CYvVMzq_69J_nhgsGQR1AGyz1EA1A1Bpm_YXK26OgMoorgeLGS-Ppz43J5sLHlDZHVeHQB-CIF2zJbs7zLQ0JtK3bTN7dspEZjhl6m72x7oMYJCv3UODTlzOCuIdI-pces054scV1JKLZP9hyfc5wxZ1b5N3b53pBpjCqzXxdB-zTwnjKOLikDbbx0lXOay84PIVjme7c_fEoR8CYeNQGjwIMNlrXG3Hit7DbPhLuudSqx46q_HIoRpio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=YkY876XgDpXSwNsROhbsEAyoe922DFM3uGm0sblX-6q4jmUX-QDVnTXH-yvUaWoVkvPV0fKG2LRGwLSP9G_d9PmSQpgYxuo6eG2Cz_5CbVAt_4-cjRDkGOzAU-MH_Gadwq1ye0Wsgm5AjFbOC9v2ClRcBmwybSWjEQOFcXi9J43cQnW0jobVFAQ9_zttvjk0XNeBqybP-itJ47BwJBxUiwiC_5NN2UMdir2Y9G4EiNrnHrNrMESPpcSqvvxle9enEBBWz_qKWzLkiPJ_r8_qUb_n8BVlz8OUq3fdN1nlB2W3w4GpgjmUgGTEUujMFRVjzEyJCgA5paEGDOA-XlLc8pWB8xf4WH80EtiPBR3avDN52ZvCl_aBnrqDzWkTTMeCC7itkY5Qh9ME9-W7AExkzT47ey7DuMS4XG0MuCu6YTRNgVJck9CYvVMzq_69J_nhgsGQR1AGyz1EA1A1Bpm_YXK26OgMoorgeLGS-Ppz43J5sLHlDZHVeHQB-CIF2zJbs7zLQ0JtK3bTN7dspEZjhl6m72x7oMYJCv3UODTlzOCuIdI-pces054scV1JKLZP9hyfc5wxZ1b5N3b53pBpjCqzXxdB-zTwnjKOLikDbbx0lXOay84PIVjme7c_fEoR8CYeNQGjwIMNlrXG3Hit7DbPhLuudSqx46q_HIoRpio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=b53ECa4GztADbJoc3s_XbaAV3HzbLbR-KJpRpthp7S-Oi_dRfgsv8xuy2GHxPrZBpfK-jbgsVn2vk7-V5K7Su9tvNhJVU1G2B2wprmCi4FnlKo-rGSX3CtwE4QSQHo85Zh-dCISkJL4vsOIGyDnwQAPZ0Dw5HBTOcyH-u8HifHJgjVl_uw-jvBM3GMB4O6OwVmU_IbYZ4nsh9S-dzxHGyi-izejQkWXPCq8S1Rkwy8Rqef2fF5yxjZ-BEKKmgGdPBw3whSbCOZRPSqK5LkzNs75L2dnS_jcLDP9I3o2qbuJtuPdP0nMS9MsrC_TBblKo5fryduyreQUGJNBXlDvOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=b53ECa4GztADbJoc3s_XbaAV3HzbLbR-KJpRpthp7S-Oi_dRfgsv8xuy2GHxPrZBpfK-jbgsVn2vk7-V5K7Su9tvNhJVU1G2B2wprmCi4FnlKo-rGSX3CtwE4QSQHo85Zh-dCISkJL4vsOIGyDnwQAPZ0Dw5HBTOcyH-u8HifHJgjVl_uw-jvBM3GMB4O6OwVmU_IbYZ4nsh9S-dzxHGyi-izejQkWXPCq8S1Rkwy8Rqef2fF5yxjZ-BEKKmgGdPBw3whSbCOZRPSqK5LkzNs75L2dnS_jcLDP9I3o2qbuJtuPdP0nMS9MsrC_TBblKo5fryduyreQUGJNBXlDvOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=scN9a4AFxK4r5Wgaw35yDe7XuS_EDBEpu3yZ5zPf5vkPHsWmBjLa6nwMxAlHbVmTUtD_eCVwQFMr33QTRYc5cnIUd_b86R4PhomAfz_7xnPALDOQRtBscIAXUNgcIeGWB0rWOs-x_upZv0NHdjxVf4cMMP9k_MLLudEsbzQusluZaCx3imhHoh_qBCOwwRdcGfILa3FbEgthKSHK8Us8N5M1UTqo7g0oFIlwBqL7xv5icT4TKHkmbIh-_fbt4mN4Vn0NTl3PyHN3qeXmM8ypSrXaWAEaIU6K9BhQacQAyFb-aT9_l5NRarx8W3YbAf-vQTAS90iGjIhOGgaYGVGaVJp_U73rqrIn8TmyV2-V3AWYsLw8U_MnYT8x4APoToCAI3ss8l5jPMYb4EZBaR71oBgbxnbo9uDvbZ4TCqHAWvx08XecQI9iQnlgs6yTVH8kFgeZT4oaJMjpNcB6Sq8ZbqBjFlZ7CWDIvQS7pbBNbzfd8soEydrLw7Yik2YzZgRwG72g9lZgKPwStadtDNnqBpQ1relWvbcEOfmmAzvqmTWE8ReDlcxR0_uZCM_a26Z-w5THsqV_4B71padVRUVOaz0GCedCdhhJIEBxOluWsvonCXwuIDqqv_avwzG9SqajfjUsd3J_gsdaxmHhpvuXSR8j_ae2AGZxgNcor2muvv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=scN9a4AFxK4r5Wgaw35yDe7XuS_EDBEpu3yZ5zPf5vkPHsWmBjLa6nwMxAlHbVmTUtD_eCVwQFMr33QTRYc5cnIUd_b86R4PhomAfz_7xnPALDOQRtBscIAXUNgcIeGWB0rWOs-x_upZv0NHdjxVf4cMMP9k_MLLudEsbzQusluZaCx3imhHoh_qBCOwwRdcGfILa3FbEgthKSHK8Us8N5M1UTqo7g0oFIlwBqL7xv5icT4TKHkmbIh-_fbt4mN4Vn0NTl3PyHN3qeXmM8ypSrXaWAEaIU6K9BhQacQAyFb-aT9_l5NRarx8W3YbAf-vQTAS90iGjIhOGgaYGVGaVJp_U73rqrIn8TmyV2-V3AWYsLw8U_MnYT8x4APoToCAI3ss8l5jPMYb4EZBaR71oBgbxnbo9uDvbZ4TCqHAWvx08XecQI9iQnlgs6yTVH8kFgeZT4oaJMjpNcB6Sq8ZbqBjFlZ7CWDIvQS7pbBNbzfd8soEydrLw7Yik2YzZgRwG72g9lZgKPwStadtDNnqBpQ1relWvbcEOfmmAzvqmTWE8ReDlcxR0_uZCM_a26Z-w5THsqV_4B71padVRUVOaz0GCedCdhhJIEBxOluWsvonCXwuIDqqv_avwzG9SqajfjUsd3J_gsdaxmHhpvuXSR8j_ae2AGZxgNcor2muvv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiknNsGkxMhDwR9kvtWMoFmQ6597M0HNJdCtI4NnR_J_6LLWDoxPuGux5M1pT_EIJbqMMuCaYRjEJzqta0Hf2yigo6v-GWLQeF557AHkKrdKvD8y5Fw-sMbSP71WvTlzlT_J55dE_60reHwVLFGtALXqXLZrP_KpugUD3lZunwaXcPQkcktSfckUQeUrW0gG95bhNqleO5W7o1nvgo_8jx79yRKOKxJY5FpvBhg4OnlfBB0uel_eTyxD5gGYDZ7sgesHMRbkcB_eVSynmEgPIiNRqoMLAyqY7d9Sc-arv3wHJr57UGNB_Lz0I01KpJWZwkS6sYmjAagCfpJn52nsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwSxcp4cvWetg-WfGNHJOgPZGPhRLyjdtI6nZiqfAdqogUGzQaxrCmFqo4w4kXQ-Ve0YFVoeX3omrBWWJv35egElnRFCp3sgqK3jfjrQmpPqZk5_Us--GkAF2VDZOlIphD2CG6JjzpuU_2wU22qyp7xKJdCr8Xfs9pflx9Ffp156S8mM1mCB3Dd9br0yUmt-ktsbn8YNzgUXcpkZPFGKIqfniVz5j3vDMKuXKRZb0ih14kwjHxHHDmGjsOYmmkNGjkBOX2k2KlsywQ803gOCAqGwyPljviHTx4jvUS4EpfWobUznppEuVoFL-7p5Iqfr5VPidM3lxWSZBtA1jWncKdaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwSxcp4cvWetg-WfGNHJOgPZGPhRLyjdtI6nZiqfAdqogUGzQaxrCmFqo4w4kXQ-Ve0YFVoeX3omrBWWJv35egElnRFCp3sgqK3jfjrQmpPqZk5_Us--GkAF2VDZOlIphD2CG6JjzpuU_2wU22qyp7xKJdCr8Xfs9pflx9Ffp156S8mM1mCB3Dd9br0yUmt-ktsbn8YNzgUXcpkZPFGKIqfniVz5j3vDMKuXKRZb0ih14kwjHxHHDmGjsOYmmkNGjkBOX2k2KlsywQ803gOCAqGwyPljviHTx4jvUS4EpfWobUznppEuVoFL-7p5Iqfr5VPidM3lxWSZBtA1jWncKdaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjGHK_JhqVXkALZdaRq5WbNL_wZibMnohbidmJg6eSTLw0Z3BzJZXVUus9CGA6uFkQa7quakh5dazkrBuT7Xc3ywmtSEW_YIAFleCvw2G5y1RtIIbuYhsSa5XugDuvQxvGUolUZbHfN7EhA0HheM99HIGJnep9IHZy49BBBbAGr_9QoCHiThMmVM8UroccXW0KYP2bJg-2JqLEkfZy05SD0fDOXECzHUM6e_oXgzk1kizL-CT8nLhIWCeD50XudzKQmj6u_eTTWhE1NiaK-AUnUlaBZcYu1O9FBr-mlS6K-qwcVTL8IS7-f_pHEdnMTkjQ04PUv308u1B3Lup0rnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/V-gsHQGo0D_DPxrX5hHBpMFVZ_WJCvNF1eMaTKr5ZF5oBqhIj_lA-uETI244l1uO3umDRiqJzOzuF08URwNrrPvmo4Eb0RQcLGHiZAFFwrw6IDdHoWvL7xtXpZYg28HZ_KKbSsUp9OLHxRBYvaBvU2lfh0JP2VlbJtaOnktir1mBhLpsLybN5C8FRH10D0uVvQZUYqJsZLaric52e9CiW4xGBeq4qD4xL2SUtyZrfEWPtYgH23E0muqdTOjqyg51MdrCywX7Vmy0LlDFRhPr7vF4PTCmi2tO7hTijpenPTNOsbwrAT57wTRifjHnS_Ffho0ZzDzxikX4PxsBVZIGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/SUoJHpe7yi7sJp0_g9_IWmY8PP6M0dNBf33RfmzpQesD-vcIY9N2oBvBZl62rMfHKF4KZklDrZN6uDaZMPJfbauje-g2JdbC9qwTFgddlEBtvxQWSGeRWWoCPG5jhNj8JFIPOwwcJmzI6CRNeO0hlr6epdPxCkUm9Qcdabdrh9q80PfxG23VBU_ITRzdKIjOXiPt407WRQqVFi1vgAKLgZasuGePmbqEQWEH-YHuI4Sq17vpFR8gqrgW2X_PAs1rp5TeCJ85Fvj2XFJpIF1w5stKYboN1XUvEgZI36AUtBoEHlFstaHKPq86iKGX4oph8iD31nrSEb1IEqivfc3_gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=WfDbfQXH_0uZcBW-k3MeTc3BrFlwx90Dh7pjwXfsz6sP0W6BrgPdl_-YMEjsL3fT9cjj1cO0rSPe8EefO0dV8KY-K6j_XnWi5Loe2bYcERrnipYxTz19XOKktCvh7Opv_G0ZqNMGmZoZEN_7fXdT8Iol79AFCL1myB4So6dgTKVxnqWt2ae_OslBjEf8iD-z8UjVTRLp_BIVzpRmbQYcSi8gZDc0pDwvyQrHBGwnqyoD2IleVrreRBT3JuRB6MsVyB2itnuiMc4KtDavqEQE8xUsWLPYMSsDwsWzgMs39S8cAWOCQv9mj8gILdKPi0Y6YijD5UFWJfn9F2yQIOn48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=WfDbfQXH_0uZcBW-k3MeTc3BrFlwx90Dh7pjwXfsz6sP0W6BrgPdl_-YMEjsL3fT9cjj1cO0rSPe8EefO0dV8KY-K6j_XnWi5Loe2bYcERrnipYxTz19XOKktCvh7Opv_G0ZqNMGmZoZEN_7fXdT8Iol79AFCL1myB4So6dgTKVxnqWt2ae_OslBjEf8iD-z8UjVTRLp_BIVzpRmbQYcSi8gZDc0pDwvyQrHBGwnqyoD2IleVrreRBT3JuRB6MsVyB2itnuiMc4KtDavqEQE8xUsWLPYMSsDwsWzgMs39S8cAWOCQv9mj8gILdKPi0Y6YijD5UFWJfn9F2yQIOn48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVS0zW9jNksn_T35RQi7CR0mvIOcNOisFim0l8WihQDcBli3AMOoOnIbzaa3ItUF2LTpwEGsp_TmKpcGdyDN2A7RGvZ62K18mowlNlVmraypKFRSZfBGzp_bXEGTKc8pG8NjyJqpcj9UNKiUYAqaYFD-3ZgfJS4j8sThbn3jj1weBvAMVTwxLAw2-XsGubFMROfNCuHWIgyBqA95qBJXQToBs1ZC6kAxiAUNko-Jr-k8TK25KZYgAcnP7FNJFiNRDRfTmXlUxGeboxz2XnXcgZ2bVjhpPxSynWLc3JTPdNz35L-AzmcYCFQCkR1_XLHLRNIGLL2dw7XNmtE5Zw1YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=b6XgHFxR4ElLD06qCsMtYoQukM_7v43VPhyPO7bO8IUuoGMWMsecN_v9IuEeYbOxHLFC2zeW1qApbNO1Hgs31Cl7tulNMOBpLbZiYF7ECpYJIPowErHhFwb0Qs2lkxb7aV_b5pOI6tdUZDmPRKCK0xnsXHTHaOtIqYYNwfU9tOYHGndGfB_7lW9wnYMs1Bz3qJllGYJp60A9ZM7NxHiLXVKCH-6-QkTf0W4BK1lU9674-ilQdx5pNHAZT0MrKs7jR4byZw4CsYze2uaT-jAds-GqeD-b9claxIKXG4SwMPWlZUR5D0I7cWICyZh4mImGv-LOU_ajUriEWS6yBdYF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=b6XgHFxR4ElLD06qCsMtYoQukM_7v43VPhyPO7bO8IUuoGMWMsecN_v9IuEeYbOxHLFC2zeW1qApbNO1Hgs31Cl7tulNMOBpLbZiYF7ECpYJIPowErHhFwb0Qs2lkxb7aV_b5pOI6tdUZDmPRKCK0xnsXHTHaOtIqYYNwfU9tOYHGndGfB_7lW9wnYMs1Bz3qJllGYJp60A9ZM7NxHiLXVKCH-6-QkTf0W4BK1lU9674-ilQdx5pNHAZT0MrKs7jR4byZw4CsYze2uaT-jAds-GqeD-b9claxIKXG4SwMPWlZUR5D0I7cWICyZh4mImGv-LOU_ajUriEWS6yBdYF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWJA-BjwTDjRs_k2d2aZnQWuIFl9Xu2qyfkTHOK09ws-fHPCyd3UzgbtyAYe1gjnbaANm8hrNH4EvdUOkdEprcJ1xxXGvrQsvE7S8aoxmrl7l18EAaVrElj8L_Jszajus-1DquhJNzM_vrv1ZzH-hH5Repeyjcq0pwlqjwtBOXhVJKz5eTeAgmpv89HydBa13w08BPYmuKtOC8sgIKlz19sdNfS6I4C0Rv4E6_noXNHVOvqD0OCWJ1j5XAHQ8B2P0zGpu9G0qP9aHk4ugrdFz9we7uAA7lJj7SLBNgyBCEPMg_YUyCUBvrWCht47vuPbx43iZwy-7kFcBER7VwayDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVsAUMGK_n3EkHXTaFHGJommzfYwGU1ZbsJNsBBuM1wSA1vQBMH8Ks5ZxAA9oCxtj9j7ZxcZDGoQ9hsLD4jTf53fGLUWYqKUk4ZjC-WQio7wBQiaM2bncwFfxvyDnO59HEpMJR-Hm2WlPhnHiuLr9J2wsYSrD0BYRX1y5FpYQoLWw3vn4JinKNWRbggl5HDpJhD-S7mbvEbScQUReuQcg6a2zFzd1AHu3CkRX025dhCnw11xNrTlV4FY3qTMYngSNeCoGa4Zzv1wXK6rykUCOqcmvh4743hTmCppjIvqBITmgKdsIAYBmzBzH1NmCY8OX5JW1rhDjl6GAGt2tuG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=nKb0Xu_nulZHhjTeYtGos8FVHOfqCQSzWAkcF-pN8OH7g6bdyH0H2wPnnafgZ1vyi1yxxi4Kmy9dynNlUXYmoWEH7Zcro7dL3wd3E9MAKgaqmT0Bir_PmqKwj0vUiXGeyTSJKD_8CdrfpGTKgsJQaWncToGzv2EjIOKK41gbMijCm_ej94Ho7rXaoV7bJ2yqQgFoXTGXAKgdMrMfMrk73MBUrSPd59QrrlnD5aggz-ZLYMR-TmEcdd8d3n0QDXnDYhlRpj8VOK-QqsP2w072z2x2idhGh_fB5msIW6CvSg4yTsCdO9uBorDntyDBr4PToZoiq7nq_a4plsJesYy3dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=nKb0Xu_nulZHhjTeYtGos8FVHOfqCQSzWAkcF-pN8OH7g6bdyH0H2wPnnafgZ1vyi1yxxi4Kmy9dynNlUXYmoWEH7Zcro7dL3wd3E9MAKgaqmT0Bir_PmqKwj0vUiXGeyTSJKD_8CdrfpGTKgsJQaWncToGzv2EjIOKK41gbMijCm_ej94Ho7rXaoV7bJ2yqQgFoXTGXAKgdMrMfMrk73MBUrSPd59QrrlnD5aggz-ZLYMR-TmEcdd8d3n0QDXnDYhlRpj8VOK-QqsP2w072z2x2idhGh_fB5msIW6CvSg4yTsCdO9uBorDntyDBr4PToZoiq7nq_a4plsJesYy3dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6Gp4L6iLRFCYVNuR9mH24k9UsN-yOkmREcG2oNYmkKanaMgwytk55cVIj9VA85osQlIzmQS38Tghmpys1e5RiQv-fBR-DDGXvyPs6UtDwgSul7OcgOqFoAwFaWQgjFzjXrGht5STQU9R5mYCtKYElSh6rkluFX49mtaS77DLzSU5dOcamnIsuVOC1_QhMO7HcWt2Ypo78FVsHQcU9HOwwgx4xnneosZbhW35U1J4mEY-nLjIbHMURW-hw7IZsTvaEWf-hwXHZYst1NmNdQN_GyS8I98EJHtFuosy8T8N9U6JthQ5_HgWmLLCkp49efIFQjvgBJc1JXwuV2yVpygpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=bFcr0EhS6rFFkGaXXJ5fwS32zyVx37hSgA6Ezx4aETAbhcHlnWP8jV6rwCwZ-mwfLmPOyrbtHqhTDRPU77nXCuqRKcSet6TfG1jqX10YWO10mvQMQ8NAdpHGXSrodJsqjRKDBqIqjrCtxiVjAtfrCwqQhVF1xw7u1ueAX15inSYnap8zDagl-KVPfy2kgwjoJ4rTkV68ZYpwlcCgF4ri3eUUnDxLpEoYlb3UVenAAjZKH1zrnxsQ1E-9WkdG2mwpaUt5O5fXt47Qi9hzE1gul_41lWiXnrKwcTpYCKEctZ2EQ0j9_pE0_JdTHD0A7TX9AiKNG_WIiSDrQtZeBIdy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=bFcr0EhS6rFFkGaXXJ5fwS32zyVx37hSgA6Ezx4aETAbhcHlnWP8jV6rwCwZ-mwfLmPOyrbtHqhTDRPU77nXCuqRKcSet6TfG1jqX10YWO10mvQMQ8NAdpHGXSrodJsqjRKDBqIqjrCtxiVjAtfrCwqQhVF1xw7u1ueAX15inSYnap8zDagl-KVPfy2kgwjoJ4rTkV68ZYpwlcCgF4ri3eUUnDxLpEoYlb3UVenAAjZKH1zrnxsQ1E-9WkdG2mwpaUt5O5fXt47Qi9hzE1gul_41lWiXnrKwcTpYCKEctZ2EQ0j9_pE0_JdTHD0A7TX9AiKNG_WIiSDrQtZeBIdy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=qidp88f9CSn3RGPfF_4wZPk7wy_czMgNYjpjaxxJr3n3gbXGwTXh3omBA4q6uXMLqCXcnh9eTI3y7KhzP2tGRESCm6XfHE7At5cRNJF5SEO-y9Z0E30Af02jYavWjaW8DJsCzgDoIUqmsdW6ZEouvEqyMPUO8v_DVf6ryHfodhMCMCqaX-k1Hiz3NLscXOx410rbEiZldpabeWtMXOQFSrfaWafq7eqKu5zMN7YEKGSjg7VNmFMeylOO-d-mDGpRUrZX1NOHoW_y0u4OZh0zbqfMcCciz0POq1lFTkf--aWxX0kRFuhTVEGwLeSBPh8gf9u6dhYGynUB0_GwrsuXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=qidp88f9CSn3RGPfF_4wZPk7wy_czMgNYjpjaxxJr3n3gbXGwTXh3omBA4q6uXMLqCXcnh9eTI3y7KhzP2tGRESCm6XfHE7At5cRNJF5SEO-y9Z0E30Af02jYavWjaW8DJsCzgDoIUqmsdW6ZEouvEqyMPUO8v_DVf6ryHfodhMCMCqaX-k1Hiz3NLscXOx410rbEiZldpabeWtMXOQFSrfaWafq7eqKu5zMN7YEKGSjg7VNmFMeylOO-d-mDGpRUrZX1NOHoW_y0u4OZh0zbqfMcCciz0POq1lFTkf--aWxX0kRFuhTVEGwLeSBPh8gf9u6dhYGynUB0_GwrsuXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=QXH56SqiKrG9NAtp7hbr64_UKYrORXdZh3sTMKIAt2wyInH5CmzomFwi8groER-z3RobQE3S96M1dVsbws3HkOcMZxmqCx3s_CaWd-qb-y0bfNwMhzR64ME0VDeYCl5JN5_4jK_7liw2C8ldfJPQRrp9Yl7xP4jv7SzBzizgqAZMzmECB3WY8WK-IXfXHorM_p57vZ9zNgIJIcik7mke0MGGFNLfgIrOFF-E3w7-9mcAnMUDwTgQ6DJC3x9XwKDpwIU7Oyj-lL928LBkWzUPAi4_i1NJDWX-xES3gO0jgK0HA4QtbtP2cKdcLv8zB_4ctc1BASlWUTYuHSPaCtq3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=QXH56SqiKrG9NAtp7hbr64_UKYrORXdZh3sTMKIAt2wyInH5CmzomFwi8groER-z3RobQE3S96M1dVsbws3HkOcMZxmqCx3s_CaWd-qb-y0bfNwMhzR64ME0VDeYCl5JN5_4jK_7liw2C8ldfJPQRrp9Yl7xP4jv7SzBzizgqAZMzmECB3WY8WK-IXfXHorM_p57vZ9zNgIJIcik7mke0MGGFNLfgIrOFF-E3w7-9mcAnMUDwTgQ6DJC3x9XwKDpwIU7Oyj-lL928LBkWzUPAi4_i1NJDWX-xES3gO0jgK0HA4QtbtP2cKdcLv8zB_4ctc1BASlWUTYuHSPaCtq3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXFcUp9sksQ2RF7n6OERU7B2NyaBUYtklNrm6OpnyJmdXBEycqR1NzThFpDHqXkd0vr3KPPY4R-8A8xbL70WvQ7J40G20EyAma2Jwdyu5mcfm6gIXN0W3wauhrFrSRUYNx0uhuWlLD_BEyrhRiGHiXO94RYEF2E-9W-lBFmbRZMfDcEIs82lkIIOPCxEsVbURWknnhNTVTOyb9y8oIJIdNYMIBRnfzafUeRYyeSQ9tFY6NicgJj-EnWH04aR2lz9zHsQkoOucUd4tg0aWpAFIga5b12vXfv8On7Vlz98-xrdx4FUM1FBd1RxkUINCAP_iqbEaE8JqWvenoGPMP1uhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqG_dB6KLQjhI37gxYswOOfT8jsulQZHONlxiqCklUPEYFSiKZqI0jjmj9nKrbKlNOzNqj8q_yOb2GXGlIj96Ii9oYtSf4ryDkJtuJ0X2ZDQOcDpAXmMh9ulDPxp1m9iKoOLSpnpSpPIlQKqPdAElU5cMKkySmCTnhY_XCDy_Amk2aTOaiFoku6gH7Z2tGfoA_26-nZucHPorbYxrMs0Mm_G5q12Yw6XBVkTWExdt5kQfQIdlEdR3tHIIhzS1-2BUFcGXCOtBf5rBxKk3Cu5nzlg_4CytUN9EnSm-1bRRi7mKeg0yCBdP3QnQmn33gews8GdEhBkGr8RK3djetmwNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5cALy5Hb7CGBv7FGgD8VE8M_xZ0Rpy3BYRbSi83sZcP2DCTmJefr5R8Cn64ifYrZvmlmYrZS8siyr7gLodr-V1jVq7HhQmNoJTDfrOwK_d4fV5g3V-uqWnLtYDBjUo3ycca2nxNjC6pFF6DajqG4JGapP0L_oF7YiV0Gs2rfZT9wxatG61E6W1__zYrp5FLfJ6xONTFi4XMi0R9wjETsUWfugye3jU4geEiDv2tfiLhCV8di5T6NLdr2xVuTL4NUloOEa8eYgTkya8cYqmwf2YSCxlLd11LfVefxSn10mXlWj6grfpF7ZC1Cy12Xslq5L8k_LfVErcZpYQcPBVKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
