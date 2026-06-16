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
<img src="https://cdn4.telesco.pe/file/kKowCpNPJWYoPs0AGJhnEIXmHNELLZlPiz0xaPkmljxdzBYOsJWZAQuSXVHvxEwxB9wKZYLUeSr0V9ZIsonXBhW96qZcUiQdWExkajDCU-GHlZjD2orpfmOLfXTJdd7Q1vQQetV_UDt2XTbHLVGOsPOCXSWPOhC77x028mFdEFnau39T8j5xtxiLJjAyL28nGMbZ5Pfv9S73fcFkl5UnfyZMYzoXLJob1uPLm9E_lU0uS986M23m6Ezn6icD0YSlf3nYCo_t9y4quvIx81VAm5c3WiaLR7DQ8NO9FyVCHNDNA4ksRSzHjEgS9HOOsy4djnDTRkiwxsypqA89N3MUaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ki0DX59vR3XXe9trvVz-SmBlgOCcT761CXZ_v41DmwCEgmpjwbxWL-GvKBoMRBS7ZUCKiml_OUUz8FhhwyJ5q1eizjqMgngQiILn_3kvn4M9fyXMOmgFOUsWgM7sEH8Y5Kh6iC8N1DLYCjTpTd7f40jssx52AvdBlsC_nW8sJOQJpZKwlUomb1Yy5trtQRTvhANTapL2yOvYwlldJ8g079VBPPs-ULr5Plo02AQZjCVziId10p_AO6AeP8Fc3HpIJ62zA2PlLAMXNudE-k_pK1WwYpN1D5Ydvs-0EaODL03-SFZCU1mXP3iLXbyJbqU0a4nSG06n3OrKNepb7jfA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxYhek32LuzjOVTsrgGIOAOTBucu6as_bMr8gDenQ2PFcglQD1gj1tEZ5K-kKnM3dG824AqeP041zK6OSF6h2a7ZRz874USewEc754M3PqRLYDCnP6P3gXKkdb92JqTZ2H82PTOE9MGLKsT2xEQ3gQs_AYkGjBvcr8wjkZJP6cpS6WwsLH3lB1cFyLBunB_REwgptx7qnip77vespE-S48oRndl1w5v45YUosn9lKDORqqggRj2zxaJesnS8gxlBG3_gBhk4COHHSpGRXKqFqZLQ28HyTB_BNmIuVIaTylKc2M0k8doBc7Z2NTgFh8atNfx2pJEzB3El0j-1IMyxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycVQmRxGkXKm7CXg7Ca1gmICLCTB8uNctC0KJ1Ml7U2aW1mK2fNtBHY9aSXsczk0UqfRDt3xoV1Mo06JsSuUocBtCukYyhBUsA7oOpPLRjEjR4BAW8nR2StrM3fQJXjLEWf1-qQ96dUl7gejRFxvriNCD02cJ2ImlEKOERkKtzpyiGNZkOw9oBtOxXjRBZsIwzVIWWO7ZQgp9m-GMwArZyEsdBgBgC82HZzOXiKqubar87ENuOg-BdDj6mVI_euqVBccqBt1FCgvPPni-FX1Nxg2ygy-PXCRH9cNGxex7-DOJVuvqNRTlsWBynxWoPPqOqDLkB6K9zarMB3njp7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsmEHCExZLsXGLDrE0khscKMLpGasy69wRUZDq7LL5dTsN3GlvUyBzdf3Q_Ok-HcD2_KG2zG13E_AHMxJd_r6zen5D0itHEYje8_6glw5FdjlSaB23I7pZzCDN7Q1cpO0voTL8XLSvyaP3AdkSleFwM3wWycDWRI3A8G4TgLsU7kp9VlKyCUf09G-QjXl99eDP6l2H_0ZPUWc5i92hR2hCckiveUMPLasB230Hyr5stBAGfMAqUFWFxJof3auTpvf2zasjoz-NSncI_g74JwZnNo5agRF_IRBHimOWy8yFX6XOfqi4F3kspzG3hOOJa1IrEfeaZBaPm6md66AQJfkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واقعا حق اسپانیا تو بازی اول خورده شد باید ۱۶ تا به کیپ ورد میزدن   @sammfoott</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/66294" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbQtTD_5Qu1IuNNk9oST6flS-WWgPKeNXz-1V27Xq8DljaGVVarz-IMFb3QHOO1MzqEuybeiKVwN52U_likmpXUpAl9PU8d09Gn1WqomHLaI03yg7ncbHTM_SbAWHgJYKQOnfwVvUDdYL8Ujv5pkXSJWPB6USPoONu46GO49k6-Hrxif0w008y_JypDLFrFxB79Pcq1VKfXoA8WikWeBKOnRYeplpI0GMLshZhqkKQfBeATWVOV_y1lO5Tbws_-hsDnBnov_88H1K_wLZuc71D6RvveuANDeN2DpSWjBKJo948G73xOgP3Bi01AJtBKvW2pi3QZ1n8NN5k_YPyZinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=Bmf-CqEzDFYSj18f1h4m48od-YUgx-PYb_qQtuqL5v_pSxjlTBDfQPmEMoWPEsFkxi-hZ4_NysGplYUSm8J74guQRRy8MA6zeqf8UnEIseSIEfSptY-OVY5yrCv9pT69JkglNIJ203k7SdntgzOmymfU0A8fk2MX6JmidLw8F2zjNAzCxVC-At5WjIbr1q7Cdig-Ln7PqIOSdOBhRLvj1yLmR1-0tRNgFDiFKGFRLXBtTYoLMzJ3ZNcxxe_jrP6JNBl5b5DJDjrpoFE26W8Jzt6QY1inIu3sgihhBA-RdV7-GfzFSqhgVT06gnFpfnjj6KJWzd9neIXur5nEdxwWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=Bmf-CqEzDFYSj18f1h4m48od-YUgx-PYb_qQtuqL5v_pSxjlTBDfQPmEMoWPEsFkxi-hZ4_NysGplYUSm8J74guQRRy8MA6zeqf8UnEIseSIEfSptY-OVY5yrCv9pT69JkglNIJ203k7SdntgzOmymfU0A8fk2MX6JmidLw8F2zjNAzCxVC-At5WjIbr1q7Cdig-Ln7PqIOSdOBhRLvj1yLmR1-0tRNgFDiFKGFRLXBtTYoLMzJ3ZNcxxe_jrP6JNBl5b5DJDjrpoFE26W8Jzt6QY1inIu3sgihhBA-RdV7-GfzFSqhgVT06gnFpfnjj6KJWzd9neIXur5nEdxwWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=NhRRD8fCY6YM7U7x-CRycnIswAA5DU_oUBAsk-FwF4w2nuoWO1Q2CNxTCTsAjaXh_6a8ZtrbxHi2dx2jjA9iXxSebmH7xVzBuZsFt76LtDXIhZ7TFi4fSD9n66wzu7eenq8hNVMfYH889yJSpQhV7J4HJ6Cg3dLvyl8MsVon3GTTcQczrP3qcF99i3ajlJyAwB5hRsjxQk9vsKWbdiPZAL_CSvYn8IjwehcYHTxViOecpF9VknvBe6KfLRwf1_tD6Fa1XF6Kk-EDinUdBKlGXkRGYEHLQbDH_72TFAuGD1k_4aValDbN9BpV8xqJhcdy74ZzKryl5okLCt5iERADbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=NhRRD8fCY6YM7U7x-CRycnIswAA5DU_oUBAsk-FwF4w2nuoWO1Q2CNxTCTsAjaXh_6a8ZtrbxHi2dx2jjA9iXxSebmH7xVzBuZsFt76LtDXIhZ7TFi4fSD9n66wzu7eenq8hNVMfYH889yJSpQhV7J4HJ6Cg3dLvyl8MsVon3GTTcQczrP3qcF99i3ajlJyAwB5hRsjxQk9vsKWbdiPZAL_CSvYn8IjwehcYHTxViOecpF9VknvBe6KfLRwf1_tD6Fa1XF6Kk-EDinUdBKlGXkRGYEHLQbDH_72TFAuGD1k_4aValDbN9BpV8xqJhcdy74ZzKryl5okLCt5iERADbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=nAO_APLNxx1goAgxcybZnTJTX9QoGhG9CeStTz1Y2IL8D4haCGIJByCeLiMzqFMy2OFRx1iP5dP7864QTsyzZMrucAA45lWGEYjhlJZCrgtabW_IwBLvzck5PyZ_0ueSckIbeuKYSVU6tW3khsRmUIuldQ-lCFCsDl-IszKtuJReOKGvY3yJGEJkV5Dnvod0IBYFq7qatiQQovnbMp_gDL3VkHR3_JbKtyxKFOLK84BMH35dJdqTjBk66QOT6-YeXx1MXqM_VoEjjO8ddVLwfs0Sob3HVSkoE9DXLeBj97T5b5TsDI3Uww93ryVSc4A59amkGjHUDYZSDkP0gkdbYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=nAO_APLNxx1goAgxcybZnTJTX9QoGhG9CeStTz1Y2IL8D4haCGIJByCeLiMzqFMy2OFRx1iP5dP7864QTsyzZMrucAA45lWGEYjhlJZCrgtabW_IwBLvzck5PyZ_0ueSckIbeuKYSVU6tW3khsRmUIuldQ-lCFCsDl-IszKtuJReOKGvY3yJGEJkV5Dnvod0IBYFq7qatiQQovnbMp_gDL3VkHR3_JbKtyxKFOLK84BMH35dJdqTjBk66QOT6-YeXx1MXqM_VoEjjO8ddVLwfs0Sob3HVSkoE9DXLeBj97T5b5TsDI3Uww93ryVSc4A59amkGjHUDYZSDkP0gkdbYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=PPFdh0gL2t_5GPvqXMN544Q5sRB4d1rctVwT8R-qXmJqUIiuq9UMb2rWyprT4U5TaGmJSMXrQdNA4MoUNmoOQo7xQ911VVi6bzLm_9MAzBq3oP5YM8_PljmpZvIDdcB2V0Eh-J4s5YEVpzWbWL07vNjNcjXTdrAA4Mem1PbDMshh0_Iy8GXixtV5mGdPv_dzk-X_Uea6XK_Elm1eo3OVYMLiqSCcMVih173fu4dIz43Kod7Hmfo0y4rlcrv0QtmlL6CgMOfxkPm5fT6gQ7PU3mhxvgqnnBAi-xlQslKqLMICyS-glLas6tFoV2vmpCfo-FZv4rN7M9NcrJM9XecCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=PPFdh0gL2t_5GPvqXMN544Q5sRB4d1rctVwT8R-qXmJqUIiuq9UMb2rWyprT4U5TaGmJSMXrQdNA4MoUNmoOQo7xQ911VVi6bzLm_9MAzBq3oP5YM8_PljmpZvIDdcB2V0Eh-J4s5YEVpzWbWL07vNjNcjXTdrAA4Mem1PbDMshh0_Iy8GXixtV5mGdPv_dzk-X_Uea6XK_Elm1eo3OVYMLiqSCcMVih173fu4dIz43Kod7Hmfo0y4rlcrv0QtmlL6CgMOfxkPm5fT6gQ7PU3mhxvgqnnBAi-xlQslKqLMICyS-glLas6tFoV2vmpCfo-FZv4rN7M9NcrJM9XecCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=op4kyQ_ee3JdmMQ55Nn-dTe2EO1gLq7CCfEa7GTNIriCHr9KALgsj79eml-tDvlKXxy8p5lW3NR--AecGYebzC5pW1omvJvOoLOFTKaiyFFpzgMLwHLBwu3bwapKoiD03BeaDt3BIGud3UqXGLjWXwRPnCmJxwUqITh5dDYA0MO6NuGpAxVgHY_GxLfBO9deXEOvaMOZmqQyysSfVsVw-6_Zsu_9Vy6n1oRGf6xYTTstDyolrbh_5H2W5M3xqahYuRkUtqXZq7Uw48oqc3aMtSkBRb3qcMyJPbfwndbrpYvACczLSoWrT2cn9BFxfKTEsJoTH9QCWxw-pIrqeyME8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=op4kyQ_ee3JdmMQ55Nn-dTe2EO1gLq7CCfEa7GTNIriCHr9KALgsj79eml-tDvlKXxy8p5lW3NR--AecGYebzC5pW1omvJvOoLOFTKaiyFFpzgMLwHLBwu3bwapKoiD03BeaDt3BIGud3UqXGLjWXwRPnCmJxwUqITh5dDYA0MO6NuGpAxVgHY_GxLfBO9deXEOvaMOZmqQyysSfVsVw-6_Zsu_9Vy6n1oRGf6xYTTstDyolrbh_5H2W5M3xqahYuRkUtqXZq7Uw48oqc3aMtSkBRb3qcMyJPbfwndbrpYvACczLSoWrT2cn9BFxfKTEsJoTH9QCWxw-pIrqeyME8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=uBkfbFyChHhMoLyCbUmyFETG4-zEGtL7gsqPMi3DynuLGs_EWasYIF7PyMZkVtFXK_zsAucDhVFnj2ySPHiMSA5vj4NC_ZeihnM7L8_lZtVTcOopFa9qSZekcdsb3Rr6A6iwhidzu330cpKeFEo2hDKa99rP-6KbnTovNwYdTfaFUWCwctgVXWNe3D8wB12O5R5uVq5-EzELCBDUG0SUVz0Xak_bvdZ7QTgNeBSAxI8sY97nvFkU5NQ5UNGmO0xOHC_TWqBuZXai4WZZbo-RQp6SFZAeCCnHncZ6--2AcmVY5g6MBoQ7PuynOOjYfTthvu7NQrJanCi1e8vslb3D9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=uBkfbFyChHhMoLyCbUmyFETG4-zEGtL7gsqPMi3DynuLGs_EWasYIF7PyMZkVtFXK_zsAucDhVFnj2ySPHiMSA5vj4NC_ZeihnM7L8_lZtVTcOopFa9qSZekcdsb3Rr6A6iwhidzu330cpKeFEo2hDKa99rP-6KbnTovNwYdTfaFUWCwctgVXWNe3D8wB12O5R5uVq5-EzELCBDUG0SUVz0Xak_bvdZ7QTgNeBSAxI8sY97nvFkU5NQ5UNGmO0xOHC_TWqBuZXai4WZZbo-RQp6SFZAeCCnHncZ6--2AcmVY5g6MBoQ7PuynOOjYfTthvu7NQrJanCi1e8vslb3D9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgFKDwsxKiVsm-Ye-9O6AI-yGaXN4O2AQxj8Y6gF5ssb_aSg1xEL33dt4ApTCOh9OdprRNYzRZiYckKqxuZXt46fVaPeMILIbldpBfDVAU3ZEC4HB-o5eBCSTD9UBhwRUUKbqhEXArRtszLaD87_UZAysCvSfuBUGqjvzwR54_qRki-Iww22hPv_WhHb8YznB9rSo0WT5scvkH23Dgd3axb0tR40MQ3oCfUQ4sfOPEqcNSRXE4-LLpf3N3LjyZlfLUlUyS20L2ckfJRfvUlPeIogDPC8u4rX5Z9v2Lb8clRvTvkcS-pizqWvJcZ8yzHhOCx_2SpU3R7oYrs1h6aNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAieEg1Em0II0mymWZZUtCCX3gJRhWxdbT3RYr9wKKH3TijsuJAUHAwKM3ZlLl-n0pVJn7_RtWFSh3NgzfCUMuE7X-F8PYUC8zNYAZ9aCBvFb6BgXExqfBjxm_DWWthZxMTBjEme5otVj-EyPxmRtLLcR-0qPhKriIsbyEl5DhtQ3SPOqU-PqSd7DYkmy0kET0PV48g6KPBqrR4a2HhVv6M7ajRAkkQizmXBda4DjBzgsVQLOw9szuoTNpW20O3zeAMFLOFfg6MPgncQA9gH0uQVvlmbeOjFiNpqvO3vWyFI2Bu1qPe6wOG_XiUQfnqLLIvTIFzy_Xx9RXmY1pMSiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=JSsR_PZ-Md3cm7HUThf5mFUDF6j-bafEMtTrDJ49Mgw2nTamzAT0xYf1o2WWmWovCYAu63qFtbrKGJvyAFpjS6rkXsadUMBvD7Mdk7muwmznhdrDnm1MEfiXAQrMutaVCRnrUl-YYyzt5DzsFQ02K9W51hZxFauOPwfZZ5LCQx5iIJrYWcAHMg_zVMcPa9AsB8Hgr_4j6c8G5JK6M8FwFN6ubaFygxXuulZnM9VJf6VuA2kVWv-6sEBpXmMqGcILHRPONEsIe49X3QeSBrwJ4Ov7xZTzkV2L_3MJG2-7LyTXxEVPoBltQAzgktgxxq5iiEWF5MGEDqIVvPFLnslJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=JSsR_PZ-Md3cm7HUThf5mFUDF6j-bafEMtTrDJ49Mgw2nTamzAT0xYf1o2WWmWovCYAu63qFtbrKGJvyAFpjS6rkXsadUMBvD7Mdk7muwmznhdrDnm1MEfiXAQrMutaVCRnrUl-YYyzt5DzsFQ02K9W51hZxFauOPwfZZ5LCQx5iIJrYWcAHMg_zVMcPa9AsB8Hgr_4j6c8G5JK6M8FwFN6ubaFygxXuulZnM9VJf6VuA2kVWv-6sEBpXmMqGcILHRPONEsIe49X3QeSBrwJ4Ov7xZTzkV2L_3MJG2-7LyTXxEVPoBltQAzgktgxxq5iiEWF5MGEDqIVvPFLnslJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=hRHC3fG06Pcswzd5Y5Fmn89ObOD8HFDVYKkK5XvVcyxehSmahwLnPL5SG9WdZUtJSLu9Vdp9Ess8xGghzC-pU0892BcJR-Hwc-4hR9lqDnhO2S6UVFgd_bv57W18dv5wnLm7l9n0imuQL90QKeGkTXL0Bf8gsBhIk3aqkDydWc2uZlx9iqz1QyzjX78OzuxVqWtwesnm8P2rmhx5DVnjgGIXr4SR0Du4EyGN_KV66XORc01UNiKA2gX3EzjYEjP3Is8_Dp4D8nI8klUQL0BbpEk8fijzfIYhhcRJTg9425U4uAo8U57IdM1qubcCLFdceaSwnZtuie5A8bLvUZodFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=hRHC3fG06Pcswzd5Y5Fmn89ObOD8HFDVYKkK5XvVcyxehSmahwLnPL5SG9WdZUtJSLu9Vdp9Ess8xGghzC-pU0892BcJR-Hwc-4hR9lqDnhO2S6UVFgd_bv57W18dv5wnLm7l9n0imuQL90QKeGkTXL0Bf8gsBhIk3aqkDydWc2uZlx9iqz1QyzjX78OzuxVqWtwesnm8P2rmhx5DVnjgGIXr4SR0Du4EyGN_KV66XORc01UNiKA2gX3EzjYEjP3Is8_Dp4D8nI8klUQL0BbpEk8fijzfIYhhcRJTg9425U4uAo8U57IdM1qubcCLFdceaSwnZtuie5A8bLvUZodFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=uaMnEDLyFA2TE2NUJF4CQweqOKdBq0_oCt3Tu2jgCsEriQrzI0t6V6xL7YBRga_VvUO1fPrDSm6sGzVd7zaXR52FtQG5kgLB34z8u_2PnGLDUYLA6Um_cwfQibSLaufRFWOj-7Be05gwkK8hkGOPyM6Ql9vouSHGtanEVGSIxlivmv2jkEV4UnE4IZyGhBLUNqnvUfgnVQnDeNM1br6w3XZ3y0wJvLQSknPDjxhAo6BvInYQRPC3TwmLRQtH_8bzLWC2NHicZ_H-_BorevMHFZEir6y_EbDRpAPi7XZSxtjpLfKIbtYZ5xc9MOe3EZNDtA-jZdg24OqjyR0PKuqZvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=uaMnEDLyFA2TE2NUJF4CQweqOKdBq0_oCt3Tu2jgCsEriQrzI0t6V6xL7YBRga_VvUO1fPrDSm6sGzVd7zaXR52FtQG5kgLB34z8u_2PnGLDUYLA6Um_cwfQibSLaufRFWOj-7Be05gwkK8hkGOPyM6Ql9vouSHGtanEVGSIxlivmv2jkEV4UnE4IZyGhBLUNqnvUfgnVQnDeNM1br6w3XZ3y0wJvLQSknPDjxhAo6BvInYQRPC3TwmLRQtH_8bzLWC2NHicZ_H-_BorevMHFZEir6y_EbDRpAPi7XZSxtjpLfKIbtYZ5xc9MOe3EZNDtA-jZdg24OqjyR0PKuqZvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=I0D4yI8qp3xJP1wcIh0GvWfsyMgmGAqaseF9kjRtCaW6PohNi4qOGjLZdtO4SM-DmK8a39rZFMHVUNbtqfAQoqMWSWMY7Q1ZbhcPDfVQ5SaJ_EB5Nu0OZz2sBXinkU2qHfJClfoATkS7AhV2xDbZIBnuWWXv7MgMJxOjSkqc7wxC5piEudHMIUvHma41NRDV2YNKKJVYGt_A1zRgauGMkmI4e78MIY5CDFGRyeEzGZGYUSNnJ_gnK54YkUUqHIjPDlQ2UhDFNVTc8pL8j2H14ZTwgW3n-hwX6uxerz_ZtJlfLvPaiFp2aFWIEwcFbir1jnVpcJd3ZEcvA67Dvn4qeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=I0D4yI8qp3xJP1wcIh0GvWfsyMgmGAqaseF9kjRtCaW6PohNi4qOGjLZdtO4SM-DmK8a39rZFMHVUNbtqfAQoqMWSWMY7Q1ZbhcPDfVQ5SaJ_EB5Nu0OZz2sBXinkU2qHfJClfoATkS7AhV2xDbZIBnuWWXv7MgMJxOjSkqc7wxC5piEudHMIUvHma41NRDV2YNKKJVYGt_A1zRgauGMkmI4e78MIY5CDFGRyeEzGZGYUSNnJ_gnK54YkUUqHIjPDlQ2UhDFNVTc8pL8j2H14ZTwgW3n-hwX6uxerz_ZtJlfLvPaiFp2aFWIEwcFbir1jnVpcJd3ZEcvA67Dvn4qeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=OYUHcBZdx5obrgNIl9jOcoLcBHD7rWdvQ5gqEy8Xwd4mnuBI9whkGVAMXPVV9W5hg9RlmppiD9pnr4mcn5yITR3qNxaGSv1nLFSnQppMNLHLVYUr0ghJGJyGgz9sOa3y69NfvlPGOy9Kis6JCla4rYJZva1sj_AoVuEqwgJbLzWTL3PFYTw0T1gB-KVA7XG0NdmBRZe809w2L5MAU1wWJfFI8L2SPRBEFwUk0qLorALyKVcNNP7MlwTJoDEMpQhTEuURHBK2RHfU-N-y4l3dXMrmawoKQB3c5bvBhRO-uNky_x6fRUOFN6SdN7wMFVVP15FWhCyDEiNxWuGTV4JefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=OYUHcBZdx5obrgNIl9jOcoLcBHD7rWdvQ5gqEy8Xwd4mnuBI9whkGVAMXPVV9W5hg9RlmppiD9pnr4mcn5yITR3qNxaGSv1nLFSnQppMNLHLVYUr0ghJGJyGgz9sOa3y69NfvlPGOy9Kis6JCla4rYJZva1sj_AoVuEqwgJbLzWTL3PFYTw0T1gB-KVA7XG0NdmBRZe809w2L5MAU1wWJfFI8L2SPRBEFwUk0qLorALyKVcNNP7MlwTJoDEMpQhTEuURHBK2RHfU-N-y4l3dXMrmawoKQB3c5bvBhRO-uNky_x6fRUOFN6SdN7wMFVVP15FWhCyDEiNxWuGTV4JefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=IGwXKiunaLt8egegqeXFNEkymOfkpaWWBq_qGVbdU45fPjjWA8Ct2kx4BkSMs_pOKqMmyxE_xGRZt3f_01I1dpG361If0ckoBEajxTLZWuVDWT2neikHBh9R4n3G-zVC6aSc6lFa10OVQN4y1jTDTJHBvFoJyRkbZBMo_ctfqqCVzHzNZO3r1qgzlVrLtiGbVTwzLDeLMcQnsTrHFfPRhUuQNRW_UOznLHGP3jjsC2Ex97JPrS9-4F3plE_qlc934ab3fFsw_hVdOYDCh2PA4yACwHa8glaxbFg4Q2B80qtnmEGGbi2hLxtcRr96nSd93hNPiQ5ttlKWN5LHYi5DYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=IGwXKiunaLt8egegqeXFNEkymOfkpaWWBq_qGVbdU45fPjjWA8Ct2kx4BkSMs_pOKqMmyxE_xGRZt3f_01I1dpG361If0ckoBEajxTLZWuVDWT2neikHBh9R4n3G-zVC6aSc6lFa10OVQN4y1jTDTJHBvFoJyRkbZBMo_ctfqqCVzHzNZO3r1qgzlVrLtiGbVTwzLDeLMcQnsTrHFfPRhUuQNRW_UOznLHGP3jjsC2Ex97JPrS9-4F3plE_qlc934ab3fFsw_hVdOYDCh2PA4yACwHa8glaxbFg4Q2B80qtnmEGGbi2hLxtcRr96nSd93hNPiQ5ttlKWN5LHYi5DYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWeYWhsk020aTnvipDsL3K8BdUE6Yd5ODW3x_mfNgMs6Hn-xWgbliQvbTG1s7GIs5fc6bPa7Zn3pGLDfZ3k09DzwemKdpWjvAxlJmiWHKi31SMxyLvrk8a_fkzimyQ21c2KwNUZlo_fBkXb-mojglkaN8nmlZX6CO8d0mHnJ-bDk2VREXH_4rlhFSvFTpp66aAyxrGAwfC9V62J-YWc23BKoEzpXoCaauvFJXJ3YImBGUtOvFraIBWTPX1XmwSosIzZoi3Z-c2nUaI5rBmu2qNXHEOtnTcLNAdVLKjJurYHV2dHdoSonejQOY1CAxLHEMdp8IdkqRtrqgsWTVP4tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njDHnPrK7fMTOzwJJXrDBkpZfBR9Vt79Ha-pxFH-0qw2IFEf9du4Q1EyG97sosnPBmHrxVLAKbORmrmeVukHjI7D3PrfpvHeSb7EmtasbQmCa2Z8Idal8V8uZIKyoH8P3RvPbZaMq8PXDEWo6z3epymUQIKI-RZrhMUFZWls6PN5_LZWkEc3ctDND9opFl7H7auEqrkwjc4DzkeySLWNy26XD-w2iwXNUqSJhj68Gkuz5Grh2mslXyD4H5xszc7oW5QFvl7TSYZ8s1lhDNfJfANGwTMt6RMbzzKbUY7Hgps5HRNwqnhiwEvvAaQOhHClTeswHSewtugvTQ6QxCQPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws_UFREdlUNXjm4CmATS1hFtYpIgNiCh2N00A-tC39MaXbJjUM4kTjC88tLEM7JRUvxzYixuq-AGCIDWgm7frNglVauPBs8GgxJ3y25ZLYLODj0jcTCJWGmnfG3tuUawBlX0Y_kASeBIN8Ws3i-fl2SzAa3b9vBpT8-bvJYxJamQHdGdQqA02hJ2x_F_uoDTTAEkCAZNRk7CD6r6gHxFrLYv_OctHvsXIVzEIGsEdmPHOClRqKs5kQU7naIgQe91W2MYsXEYkl7-FZ3OBrG2pwDrPYGTrJNhBMbE653P59DWkgASfdGjElJ9P-V0X_-eLMaJoltDTwDeSYQr1ki8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmJtFiImjnfWesMFao-i_WwO2NIvqwAYqeVAshtYYYwYAbZimbTmJWenPAod9lv0idZlQdxRu4K50PODL7Hgzr53x6GUbPIC08WyLFL__b0RJ35lNlJnH7aCmjB0BktwIZ6hDgAQ4J23UbJXcUYg94PPDcPao0qzKqkZfrUPJqsFwmYPt-ANFVMP00Fp1b233W3y8L47dTX0FC5qTkxnwl4cVfs2F8VycwJDmMj5olo-edk0p7Qo0Osz6-xbHHuHo-nhB2Xsm9EuF9Xx0mgNwEIAmeA1RAVLeJhorisme58a10EEj2X54Er6KZsuqqPXphnMjgFcWviqcUYOsYluig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqRb21--e-IrAwPaz9qoab5-ImYl9jC5NCxpwLxQP_dX3qjltxhc6rzl1cz4QiG5XoM4Qqhe3FA7qIvcCJf3kK2n9PuzY74tOXnwqt9vxQPVKW-82GQ_5W3DBfJlvIDnvGsrYIJ8vCUcKTIZSlP_VoW3Gg9SWdKBZ2n2kvudlGDXArMryUkJbIKkw3zcoggF8l--2AmzdN2_OmShOgQNLyaxOCDJkJbiwOLF7Gqk_p1JQSpTS0A5uSQdNJVEyTO6S9AWbgEMIgM-WlZm3siMJkHBn2CBewwErQwkyR3KkQWu43FntGynU1w37xHmsfy6bHXmzyF362IJAGuG9BrhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=X9jvXhmnEMEhGgntbZ3ut-L2H64bC4vTvw2xZFCkMHSbwdbwWEAYixWEAheZGw7OglZJ_9oJYYwK_N5KfFtyXBsaEE7-3f62qce__7OE3WyRQ9p9RrPTWOCUgw2JFsxxCivdBflf9iu51nCW_60I2Zm0vgLMAzbAWh3CjXs7D--hONf_U-dejauJ1fFwJVRDggmSFwIlWTqeRL_q6DQXxS0hOEsOvn1_6DChgbUh-9jOeVPYEXIZPMgalC1tmeU_J3WmeTtRmvjMfnjbhTmV81OtFGjypGaduBI3lSbLRFnbjJsCKrFytg8pTKSl4OKy2xrVYyX1itCIE7GGfe17jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=X9jvXhmnEMEhGgntbZ3ut-L2H64bC4vTvw2xZFCkMHSbwdbwWEAYixWEAheZGw7OglZJ_9oJYYwK_N5KfFtyXBsaEE7-3f62qce__7OE3WyRQ9p9RrPTWOCUgw2JFsxxCivdBflf9iu51nCW_60I2Zm0vgLMAzbAWh3CjXs7D--hONf_U-dejauJ1fFwJVRDggmSFwIlWTqeRL_q6DQXxS0hOEsOvn1_6DChgbUh-9jOeVPYEXIZPMgalC1tmeU_J3WmeTtRmvjMfnjbhTmV81OtFGjypGaduBI3lSbLRFnbjJsCKrFytg8pTKSl4OKy2xrVYyX1itCIE7GGfe17jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwdNGTX6oyfpfrE4E2wDvEEj8gN9y0rZNBEDQSyszBgIiHM7Am-oA93ucnTf-_bOOw4-qHh5egVXROI8n07qG-FtW_sC1NvpkkH5-URhfWuI9O9waI28kz3t6NoXnZF5wV5Kpa_Y2ijxwJAezI5oxf8Srxuln7kNgvxyogib2RLEVWmY8XpQgHnLIQEBxy1EqGmtKGVCkxdO7S0mL44UjSRmTdN7LipAHjcUDyPlC2zI8kBvtcFSctMi5b7-hNUiSzEuFvpEi4qalkQvd-kQJMFdI2DL3R6vQYl4Amb6_oRuVf6aPP7dAH-qOE_oce10yP1Ei5vMc7hlqPZTQwI-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=j27KFHLgOQM2sJ35WUkuX4oZPI77NybTa3Usm9mTh53BDqqRNFlwtPyhLUhzXNt8EuYcVlwU6QMhTOFWQubZmob-11_-1GCBKhkgC3q5GMTjkcM7EFYYl7Lmg4Qaqj3-sBnz6umo_jsq3h-1KLMO43NPbcExTwUzB0Cpska3u8EtY6DXmIec9J0oOqrjgjVw78vJJwESolhK5Bjnk0ovLcU9L73GG_iDq9fozo5hlv7iRbTiEADHe4otXjNRlt5IIg1BPnb4wzvwteNZbLfEyxMScGAoJ-1fDOsb1ojxysfKksZm-GpBf27HJJU4aIOVpWdEB9cMul0Nclq8QdzQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=j27KFHLgOQM2sJ35WUkuX4oZPI77NybTa3Usm9mTh53BDqqRNFlwtPyhLUhzXNt8EuYcVlwU6QMhTOFWQubZmob-11_-1GCBKhkgC3q5GMTjkcM7EFYYl7Lmg4Qaqj3-sBnz6umo_jsq3h-1KLMO43NPbcExTwUzB0Cpska3u8EtY6DXmIec9J0oOqrjgjVw78vJJwESolhK5Bjnk0ovLcU9L73GG_iDq9fozo5hlv7iRbTiEADHe4otXjNRlt5IIg1BPnb4wzvwteNZbLfEyxMScGAoJ-1fDOsb1ojxysfKksZm-GpBf27HJJU4aIOVpWdEB9cMul0Nclq8QdzQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmUzqfZNKHQnaDeE3MJsJefLv3fae8FkN20ALUE1sE2hUVNyVHF_Ihs-ZFWdCK1BZZp259jGfiJmnEnC0Wyv9FEWua3pMhxMA9nJgc_-dzsS5zvA7TUlhn2Rt9WLSv9B3Vx02wvaNPEUUp5-9_Exd_FquZzKzX1wRYd7dR-7faec6bIUe44BQ6bkqsBnusKRWH07rlShtY_LjDOr675YPP-MA2uZl8nW5rkDisRaIppzBGs8NpfZnEX35CBCdPWD8RBNKXqgG4hMO4jcaN6PdkvMVMjJKdW3ScDDHvISvfscX2u85z1bSRz__zvYXFy50J4G4Cf0M6g_gdRlagq7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSJc2ivvF_T31QjzWNSUqiZcu3MN8CJmFwNRZdIt6mHKZC22Z8wSmgB8FQEJjbY3VAmeKQN0utcs_ECTGB0B8u7nrxbaAi9uZds0reMXIjwGDNHXW-rfS4tErAHW_HtITdf0C55GuIk9vuOiY7nVE0Xe7JYlryEfE3DXf6qFCJbjhfx6p4WD7ek9zfmdZ6o3rV-V6RkIsyXuxl6V1BuuOtgr4hWP4PuyTZtPM2dxT3LE2n2q2r9YhBdeoxaJtuVnCs-V-eFq9LsgYj36a6-uG0yNTWxy3Jvev5-caGhnt7LL8fR5Ayo33h6qr5U7F5YOuSD-MLpbGkm16C9NqaDgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=Hfjs3YfCCZLzTB4s5PxlS6JXZAEfbfFz7Uss8ex0a5fllrFjKpOfQO8SgrYsztWUOM-MwQu41k1o2cLKhzlqNXnNTIA39XIRnBFXc-OVG6DgHzqTbtwWwGWgFkzq9i_cRMo2tRx3EARN_jcysDBJ1mfUEN7k5T7pruT5Oxg5ECRcl8WbjW97DNCup303bkWorfN7D05cArWKiKBX2w_nMTRoF9U9QTBsfEwEi1cxxMrYKFRiNQgO-ElPzX2y4hR49xpV4Mrvdtsvbu-XRu8vCGkoaaTpRVKi8sQK_D9phcqY-Fg_ox1GAWBow0pQhZN5NrWM0rBVmtB3vyqADTHjuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=Hfjs3YfCCZLzTB4s5PxlS6JXZAEfbfFz7Uss8ex0a5fllrFjKpOfQO8SgrYsztWUOM-MwQu41k1o2cLKhzlqNXnNTIA39XIRnBFXc-OVG6DgHzqTbtwWwGWgFkzq9i_cRMo2tRx3EARN_jcysDBJ1mfUEN7k5T7pruT5Oxg5ECRcl8WbjW97DNCup303bkWorfN7D05cArWKiKBX2w_nMTRoF9U9QTBsfEwEi1cxxMrYKFRiNQgO-ElPzX2y4hR49xpV4Mrvdtsvbu-XRu8vCGkoaaTpRVKi8sQK_D9phcqY-Fg_ox1GAWBow0pQhZN5NrWM0rBVmtB3vyqADTHjuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=qbQgM0pEOCWlsS3LEK9kVIpvl19Q1avpCOj6gck8H_Ldgne1aRWes5bE6rlmcVor_KX4-TFCLqnQlfvp0ox3Y5yxc0_0Qna6hi87qeXTgEshoXpBbzpXG3CorkCeXvuiW-Rjb4L2qwrUS09smuP5-1RyU06G9zEydFE1bF0UdiV2POMM7ufJdpIv2lU6q7d_JQoEmxqtvoK91JJDfog78rqIE0fSY662XD8rD8cLRu7bQeHTOTF2pljK37EnJ4VBnPsszbo8CIER0BN7aftKXc90Nx_aM7bHt1nPDkdFR571w5lq_kgB8O47LdHsG_ROaNHURNkmN6802k74hCK49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=qbQgM0pEOCWlsS3LEK9kVIpvl19Q1avpCOj6gck8H_Ldgne1aRWes5bE6rlmcVor_KX4-TFCLqnQlfvp0ox3Y5yxc0_0Qna6hi87qeXTgEshoXpBbzpXG3CorkCeXvuiW-Rjb4L2qwrUS09smuP5-1RyU06G9zEydFE1bF0UdiV2POMM7ufJdpIv2lU6q7d_JQoEmxqtvoK91JJDfog78rqIE0fSY662XD8rD8cLRu7bQeHTOTF2pljK37EnJ4VBnPsszbo8CIER0BN7aftKXc90Nx_aM7bHt1nPDkdFR571w5lq_kgB8O47LdHsG_ROaNHURNkmN6802k74hCK49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=CIzMgf0qdkpdygLoSqOsBcoeq5hNh-hkq8JsEff8VaMDk3PTcXFSOeLI-RVKXpkoo64ODNbLb5ebMfpvxmTkw4z1ihQ3rCG021WxA5A8-rS9ns5GAFG5zzh56nz1a0aKuWiknk2jrFwxQjnmFe3yb1cV7DWaIgBjOOwOE4-I3Duy6DlqL0N9bwgZOFV-Lrx1JfKCDlfPRYfam1vrlIa4OAyEWgW8NXe9oyji3W4zvDP_oCqcNd7pKdZh4RvkvJCwBSnMfyFBYENkFHMGuolq7BdVmB9hwSt0m4FeZR3KVS40rRdFnHfJaJUAPiVrVT0hsFEMqO_4fTkf1DNVt31FIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=CIzMgf0qdkpdygLoSqOsBcoeq5hNh-hkq8JsEff8VaMDk3PTcXFSOeLI-RVKXpkoo64ODNbLb5ebMfpvxmTkw4z1ihQ3rCG021WxA5A8-rS9ns5GAFG5zzh56nz1a0aKuWiknk2jrFwxQjnmFe3yb1cV7DWaIgBjOOwOE4-I3Duy6DlqL0N9bwgZOFV-Lrx1JfKCDlfPRYfam1vrlIa4OAyEWgW8NXe9oyji3W4zvDP_oCqcNd7pKdZh4RvkvJCwBSnMfyFBYENkFHMGuolq7BdVmB9hwSt0m4FeZR3KVS40rRdFnHfJaJUAPiVrVT0hsFEMqO_4fTkf1DNVt31FIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=HeE_-nKIwkKfAVjbaB2EDpp1Buj8HRrQ1_AweF0UFn44VsiA4bhAef01reqI8UQFclBdfFeNpvdfFiO5K628pk8dvfYhljfCM-4AUl4RvKhSd7nIA60rPVTLg7gh0TuhDHrUd5oX9zQ6FMYnXHk4-9rgmogxHjYGYVOaSC3A6sU_r6NM7dVmdJHxEytsEH0HF64jBRoTLGu-LlPTo58QtBkcnfElbhi2K9V59qVntCAbR86xahLUeKZOL2iNbraCPHwBYco3G3bPMu1gkBLpoluVRRDAIMu9hO-m2MGDITFLVYrt7ky4VYBmQ5SNKwRdvP0-ji-fBdG0jP0zkK_6eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=HeE_-nKIwkKfAVjbaB2EDpp1Buj8HRrQ1_AweF0UFn44VsiA4bhAef01reqI8UQFclBdfFeNpvdfFiO5K628pk8dvfYhljfCM-4AUl4RvKhSd7nIA60rPVTLg7gh0TuhDHrUd5oX9zQ6FMYnXHk4-9rgmogxHjYGYVOaSC3A6sU_r6NM7dVmdJHxEytsEH0HF64jBRoTLGu-LlPTo58QtBkcnfElbhi2K9V59qVntCAbR86xahLUeKZOL2iNbraCPHwBYco3G3bPMu1gkBLpoluVRRDAIMu9hO-m2MGDITFLVYrt7ky4VYBmQ5SNKwRdvP0-ji-fBdG0jP0zkK_6eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhRiC3uISd4bX3kvwriTUFGQ3SFqQ28gaEWtSWAI7O6bs3OYQNTLW8n03uhlP2VauBx5OcIWFs532gyxLk7S1keRzNwHMxrsp4ItHGc2GFr_UCQESkdikYIZhLE0oA246RNPfF6PP61GLAm7F20YG-Qlc-I2HKw3NuxKoBvmkUvol0TGaJVDo7A85va_A2r9Dsegw2UwmhJ2Z0d1WBMyFAkBnt9HxFkDyy0et8tPn-S0gM50ZgDARCtsYFe1fQs1hbEXnVB6J8ezbbyq6T-zg-mBSg6re0-mhDAeu2kl_zKV079luPp-pdhAvGyE4uCm1ymYLSDE0cQN4f3rSc9hHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRF3ptagmwJLR2Pqc3WtBBMeuk9NTf-DExIR99_543BwDZnVLyh8QEop2CWUB3IpnrtrmffI4Hh31SsJ-2yEkGIb-GKi4z4b64vlU1hqdUqR-0j0js73QrkVn8r5rXGpAUqVv2ChuYFNtNgF3vb0IELqafOLej8ljjnf0zY0aXSvWnKL-1c-MP7lQdMmidYb10HX6z68gZUvPb06D7oTV0ls9ldRjn-cSHLRQzkwyxFypN4Es0dV2tuP1_XYyVtpRp4iMaLDsiKmQCUheh1GGautoI_8cEeOcwsjKqh1vi8ktoJCOapqMx5tE2JOP04Gt7JUZytfO5aNFh0dUxK3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiP0JQhX8nY7xAIEhBozzeGbnNzqMGCAIPlXIWtAW7CMeNXDWZsMX83yYcKHt_swl5y5a0gIq8XGhUmdGlOH3_vwsWgc6Xl9NcsiDrgspaliZMS8NYH5WdTzuhwRfHTbEi7UWSEN4n9hpen9fWkyX6yL8tS7gtWXJCQfDW6hPLL_aM7UaYELKqh_DvJjjvMfSudx5AQwxs04QFKh6ncwsQmgLTUoEgxARfDwoTvYL_PVr63-xYZxflWtHjEeH8RkcEPut26MELJtgvOgoNRVex23C2mIO_qkgwOGJuPEnw6nr_7jQl3lFtvtWcRjyFRnC9UQCemiZlv5wuKQMwrDhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=pfW0J-bc0hV6dnx-IGSgvSJ_la2OKDsflKL8wB5-zlHgnleB_sBOGhfe4tM9DTgZTTv_8yyIANvx1cjuA2QkhMEznhJE525sY-43moOrilhqFSqM0DrZWF5BL6C1IUf1ik8HLXgji3k7397z1rRygU4Rb675ERMs7W9cEbV03yDObNbI7iCb2bq47c8DuGHsPYr94UbCKJFLA0PflsLahMV14M_gRn477OfZOfbhrkF6XINHComOL89jdlbNS7AqQgVM9veetjTbeyQqAihky7JxDzhxMYbriq1l6_DkCf8DizpC7H_Apk18oVuI8IT5EBwJZpyS-tkkATkTQke6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=pfW0J-bc0hV6dnx-IGSgvSJ_la2OKDsflKL8wB5-zlHgnleB_sBOGhfe4tM9DTgZTTv_8yyIANvx1cjuA2QkhMEznhJE525sY-43moOrilhqFSqM0DrZWF5BL6C1IUf1ik8HLXgji3k7397z1rRygU4Rb675ERMs7W9cEbV03yDObNbI7iCb2bq47c8DuGHsPYr94UbCKJFLA0PflsLahMV14M_gRn477OfZOfbhrkF6XINHComOL89jdlbNS7AqQgVM9veetjTbeyQqAihky7JxDzhxMYbriq1l6_DkCf8DizpC7H_Apk18oVuI8IT5EBwJZpyS-tkkATkTQke6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyKKEjEtQXRpRxjPTo_NkrXkOjxWNr-6c6qjGtuMt5BkJp3HdhbmneYVBLkCIi5MdDdaRft8xiIgfnEVX_FEzu6kJ2FZ20Bc1dfMp3y-iQA9p67Jbiq8M9KUVjKdcIq8oRT1Dg13CWEbg39ieEnQRUz3WQ-x4hUeJn0Wahbd8e2Wr9Gh53Llqw0QK5m44rX5Wagltb-bvygN72J_fAMgYNCQGi2DUGbTBj7NI_rBu_Rt8CN3PfZi_YYjAlABRa7jmNcl7meAimwzjmkLpdX4S1nfvVvv8ovaiMDX52D612wiavI78EEwanmzclgC0Nt_WiAsg5STB0FdZ6md4IvXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=kyTl2LoTFWwWcv3YiwgMS2cNkQGlVCSEKKCYBsiUxMkykISZu0dIut0GJQru-lh6pb5la9zXNittCPmmyXlcvxnbgPa8GgZoIPvaV84_D-8n1HQibdQiwFHqWr5YgSpJtiswnFIhP32F9yIoESkrhxG8tLJEjbu2Zt90Chdd6sfDIDE2smtdbAUJGGRx14JTs29ur9M7apEPYVV-v8MWrBy4T4RcK1QVpRUhQ-YD5x887V5t4LX1tnSgNMDBogTWSazPwWToHw59YA7TXM59hEqCXKMQBBaqUjX_NuKGao6H7xHHIa03_w-OT3szM-x_ab1xLe70bAb6KJhD_UKlg0FiFM4GcKsmGYqnGqSRcMMrWNA5goKGfzeBjg8dCdJ09lrFS5l8xcfm9AnJJA9XEk52HlYlMlh5RQhfP97di4YzPZkNLPcpKailbZBMFm7rW1zp4pi42ic66wArNumZnMukOwUo2q57t1wln7kqhWj9sDgPiIYMMHXZrkZgDIw6w96bHaFuHoNpMZU4iTWMFJfMlZvUss3W70X3jrV_bRFjVkMXyUf__IgVXrVBIGMFISQfohT3mTLielg1jllICM5gdjt-mGfKUwjULvUIeOu4q5hG2BZlEXUk3TjcwHsVtxt0b57QSJytjYmdcBpiXrPToEbnv1rIXTPn4BLJyjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=kyTl2LoTFWwWcv3YiwgMS2cNkQGlVCSEKKCYBsiUxMkykISZu0dIut0GJQru-lh6pb5la9zXNittCPmmyXlcvxnbgPa8GgZoIPvaV84_D-8n1HQibdQiwFHqWr5YgSpJtiswnFIhP32F9yIoESkrhxG8tLJEjbu2Zt90Chdd6sfDIDE2smtdbAUJGGRx14JTs29ur9M7apEPYVV-v8MWrBy4T4RcK1QVpRUhQ-YD5x887V5t4LX1tnSgNMDBogTWSazPwWToHw59YA7TXM59hEqCXKMQBBaqUjX_NuKGao6H7xHHIa03_w-OT3szM-x_ab1xLe70bAb6KJhD_UKlg0FiFM4GcKsmGYqnGqSRcMMrWNA5goKGfzeBjg8dCdJ09lrFS5l8xcfm9AnJJA9XEk52HlYlMlh5RQhfP97di4YzPZkNLPcpKailbZBMFm7rW1zp4pi42ic66wArNumZnMukOwUo2q57t1wln7kqhWj9sDgPiIYMMHXZrkZgDIw6w96bHaFuHoNpMZU4iTWMFJfMlZvUss3W70X3jrV_bRFjVkMXyUf__IgVXrVBIGMFISQfohT3mTLielg1jllICM5gdjt-mGfKUwjULvUIeOu4q5hG2BZlEXUk3TjcwHsVtxt0b57QSJytjYmdcBpiXrPToEbnv1rIXTPn4BLJyjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=t7yO0JaZfT-iJph2qa3BXO2vu0f1Dbtlacvt6jZZN8kzI94PNpvFnpmNyHHtAHwxyftlXe22p4Iapgodtv7ksAo58VCuw9Ms2xGYw0i8zhcDAqiYZGr5qaUprYInrl8EUBzDoqeQvR6JINXOoJVtoahooT3jNBQ_yuP3sEwT93G9-CJZSj7lHDNHG9LGcjOugZoE1aOayo2Zw1o3qpDieu7PPP7XbLgfJbiVT7tR8zrxCT3RjznPZluuLnQziUXjlfBYRCMHDbvTGwNITs1JZQ9P7Ce3xI9wqL-DMggukx1crD8eE8skouRR6DUfbkmOgsSQQc1TWVYw5TKsA7ORJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=t7yO0JaZfT-iJph2qa3BXO2vu0f1Dbtlacvt6jZZN8kzI94PNpvFnpmNyHHtAHwxyftlXe22p4Iapgodtv7ksAo58VCuw9Ms2xGYw0i8zhcDAqiYZGr5qaUprYInrl8EUBzDoqeQvR6JINXOoJVtoahooT3jNBQ_yuP3sEwT93G9-CJZSj7lHDNHG9LGcjOugZoE1aOayo2Zw1o3qpDieu7PPP7XbLgfJbiVT7tR8zrxCT3RjznPZluuLnQziUXjlfBYRCMHDbvTGwNITs1JZQ9P7Ce3xI9wqL-DMggukx1crD8eE8skouRR6DUfbkmOgsSQQc1TWVYw5TKsA7ORJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=lEwvYNr_4BubeNKqmJ6eY0HdDXod1IckcxQ1IBX43XbXLm0l8ombPSu9ZZf3w1KdEqmiGglsWoqusFwsbdgQZY2lofXE35YVAavoQcKcbTJ-NRA2euZlxHst382jWcMu6PY_zXQwHNLcVPASsT_xZZPPRvF6LrayDaN-SOAOPzlgOWp320u1I2FLZEWacFz8m-eCLD3xNS6uG4U4sgFDA4Aj-a9wg8eBLgX22xWjwUanj1GhS6rKVzxKti9eicCXiFmovKHZ5uH-Mq4b83g58RBPZPuA80gVus2qmpuWaE5ZGFG6SEzIhb9KtNS8niCCXZhA5Gm-u-kCPsrAKVTqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=lEwvYNr_4BubeNKqmJ6eY0HdDXod1IckcxQ1IBX43XbXLm0l8ombPSu9ZZf3w1KdEqmiGglsWoqusFwsbdgQZY2lofXE35YVAavoQcKcbTJ-NRA2euZlxHst382jWcMu6PY_zXQwHNLcVPASsT_xZZPPRvF6LrayDaN-SOAOPzlgOWp320u1I2FLZEWacFz8m-eCLD3xNS6uG4U4sgFDA4Aj-a9wg8eBLgX22xWjwUanj1GhS6rKVzxKti9eicCXiFmovKHZ5uH-Mq4b83g58RBPZPuA80gVus2qmpuWaE5ZGFG6SEzIhb9KtNS8niCCXZhA5Gm-u-kCPsrAKVTqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZe7o4fLs2pvw2Bi8Zah8dz8sBAg-v2wGZ4Bq9ef62W_4r-RtWBkR3gjljiBtODyoAXdjVpjco2icz99w6WvF0Wqy9YV8PSvnlf1_pQ6zEwxjNkPAMbHoW4bElIi6DEA59-MRRyom1y1RuG5dzE_-p8JQiF7VD-HrMH54FhjmHYQ9ndEf4CVcwCm72S1TXjcUVaysWyVnEaGPh_8xLMdMyWSpIkVzBjrluQB_NYfPo586SE9Hdr9FBi8MFLLUvpPMSSOFKVg-Tzt_EQMLtgvFVOwUpGpu4oeFTGm9PwdhZO6XEEp3I9daS5micZU956yIkVTLeePNDB3clnvFnaz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇳
سنگال
🏆
جام جهانی ۲۰۲۶ - گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📝
نگاهی به آمار دو تیم:
- فرانسه برای
هفدهمین
بار در جام جهانی حاضر می‌شود و
دو عنوان قهرمانی
در سال‌های ۱۹۹۸ و ۲۰۱۸ در کارنامه خود  دارد.
- فرانسه در جام جهانی
۲۰۲۲
در یک فینال دراماتیک از مسی و یارانش شکست خورد و
نایب قهرمان
شد.
- سنگال پیش از این در
۳ دوره
جام جهانی حضور داشته است.
- سنگال در جام جهانی ۲۰۰۲ موفق شد به جمع
۸ تیم برتر
صعود کند اما در جام جهانی ۲۰۲۲ در مرحله گروهی
حذف
شد.
🧠
تصمیمی که برای جلبِ توجه گرفته می‌شود، خوب نیست.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=dWEKO32qlFJZ5eAqt4RlR916npG3vk0fiFExPiKTAF7QA2cGWVJbeae3eyPlAycB2QargwMHehc6gmckFU8nBpujYUSPTlEnY2JpCQcug35CjVlE6Inb3YxGUbBNXx0qCrnbsnHReHjH0OitJSBUe7G9_Py78XY3K1ZQJsrtaqSk41zgB3ZFkj0VwfbicD2Stz3_l4LHC2kiwvgj0sjWCrPmo3XOBi1ng_RNAgTLjDjU_58xvBOounj5jc6YYqcF2s1FDBNHxiGbsEs38_9F6ukJysXzeOkkPGODWysb4WrJs3CY32lg_VkKJyEP56Op6aM2iF2zxe6EDWiXhtIDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=dWEKO32qlFJZ5eAqt4RlR916npG3vk0fiFExPiKTAF7QA2cGWVJbeae3eyPlAycB2QargwMHehc6gmckFU8nBpujYUSPTlEnY2JpCQcug35CjVlE6Inb3YxGUbBNXx0qCrnbsnHReHjH0OitJSBUe7G9_Py78XY3K1ZQJsrtaqSk41zgB3ZFkj0VwfbicD2Stz3_l4LHC2kiwvgj0sjWCrPmo3XOBi1ng_RNAgTLjDjU_58xvBOounj5jc6YYqcF2s1FDBNHxiGbsEs38_9F6ukJysXzeOkkPGODWysb4WrJs3CY32lg_VkKJyEP56Op6aM2iF2zxe6EDWiXhtIDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=jjL-aJkPLqm0hejdZYPJx92l-mmJvW1jCGjMeVMd26YERCrIxhujX7I0mJ3NH3LvrRlQXbwYoOsYyMZX4PFHlkJEnbBfJcgM_2YTSDdQnCNHg_SGAIz2wf82zC-IMDB6N2c4ECS0sPycCTA2O34pi8Ac0HEo6HL7T1htKv7eAGcy-m0Ag5C86Z6EbRenNSsiPsoHiIWkPzgvner6_CkrYwNhpu6P03juM48AbkGqOS41SMSpcsDAuK0Ue2vM59YNKvs1Zmx2W8WCYfVlC7iCkw07k9S1KBb4kPtihgfx8f3PoVCQSaIN6sRrd57s-RLd6cVhbxtZ04rWtnmb7t52PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=jjL-aJkPLqm0hejdZYPJx92l-mmJvW1jCGjMeVMd26YERCrIxhujX7I0mJ3NH3LvrRlQXbwYoOsYyMZX4PFHlkJEnbBfJcgM_2YTSDdQnCNHg_SGAIz2wf82zC-IMDB6N2c4ECS0sPycCTA2O34pi8Ac0HEo6HL7T1htKv7eAGcy-m0Ag5C86Z6EbRenNSsiPsoHiIWkPzgvner6_CkrYwNhpu6P03juM48AbkGqOS41SMSpcsDAuK0Ue2vM59YNKvs1Zmx2W8WCYfVlC7iCkw07k9S1KBb4kPtihgfx8f3PoVCQSaIN6sRrd57s-RLd6cVhbxtZ04rWtnmb7t52PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=sqq25xOPwLdIyRgo10HfUvsD8WgPT_1xhdFoVQaJAXF6jif-s0LsxrwbCdD5iivBZV2-6rtmcfUkJdhwmtYo513sPJ9g9PPegjw02uSMyqI0WiymNU2zdhg9w6Xir0w1--4pawyI9KlZlIPnz0Ij2xq82I8UUy8KnA3GH0nT0Hp-0ZsDy2YZKsJwTEwt1rboJpACPRSf70dJ_56UG0kcUmCMFItrqby0P44lZQC12_drKKCtwcxWNyGCopJGsGSS93d-L0RAv-etJAG3_Abj-dc1MCizXKj4H5tFb3yLlydulll9jx1OE69SzQniMuAkM4ILRBXIH6dMMYqfd3f2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=sqq25xOPwLdIyRgo10HfUvsD8WgPT_1xhdFoVQaJAXF6jif-s0LsxrwbCdD5iivBZV2-6rtmcfUkJdhwmtYo513sPJ9g9PPegjw02uSMyqI0WiymNU2zdhg9w6Xir0w1--4pawyI9KlZlIPnz0Ij2xq82I8UUy8KnA3GH0nT0Hp-0ZsDy2YZKsJwTEwt1rboJpACPRSf70dJ_56UG0kcUmCMFItrqby0P44lZQC12_drKKCtwcxWNyGCopJGsGSS93d-L0RAv-etJAG3_Abj-dc1MCizXKj4H5tFb3yLlydulll9jx1OE69SzQniMuAkM4ILRBXIH6dMMYqfd3f2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=Ylt8DSgT11oGc0lBeWWBpqdn6ivBH2sqM3Q6wMNxNKFQnr9BBP028rmjJ7HNsPBsHPsa6e4fmA-O1nLX51ab65KSILblIEZTq0dJ94Ts6B7dTxuoQjExM7ZAywQ4oif0Kkl_mkKaNZUAKVn4lvPpTOJYhIDSHa7-mj_9p9GO5C89szNHDXV8xbE9qm7VVhbaPX4MiJR9-ysqIOSC5ua5t_9FJdAavNAnhCSe4uhSJ6QoroqDMXvE4sdTihU_rp9bNik817FaLW5fnB8yrMAuqZ-_pFBCQyZ5DvJDtTG0d-Rw3JvjXG_NtWrUte1xkEeqaAUwejOfWmL06W4gqOi3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=Ylt8DSgT11oGc0lBeWWBpqdn6ivBH2sqM3Q6wMNxNKFQnr9BBP028rmjJ7HNsPBsHPsa6e4fmA-O1nLX51ab65KSILblIEZTq0dJ94Ts6B7dTxuoQjExM7ZAywQ4oif0Kkl_mkKaNZUAKVn4lvPpTOJYhIDSHa7-mj_9p9GO5C89szNHDXV8xbE9qm7VVhbaPX4MiJR9-ysqIOSC5ua5t_9FJdAavNAnhCSe4uhSJ6QoroqDMXvE4sdTihU_rp9bNik817FaLW5fnB8yrMAuqZ-_pFBCQyZ5DvJDtTG0d-Rw3JvjXG_NtWrUte1xkEeqaAUwejOfWmL06W4gqOi3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQJ2OIo7yAQaiygocpuCC3Cg82aZ8lfy2cJMd_bxv9KTRoAEm5a_Qf5tgRG_yTEm8K9yit-XVievBm_91MJ1U5TMwea_WsN95gDvSlWGUcPcLeESIQQCVs8-ofCn-93Q3Sj02Mu09Qt8osQmlM1b5dt_mS_oLi1KwqZFLlYFEF68LQGODCNJscW1Y0Yz16XlywhaTQeMlYbc7wBYvLSBt6-y-0iByDm-f6BrO41cvz2ippeyEyoM0Ecqlv4CyDTZXh721sdVfPsHb5uaG0FFg4f9OlZA4oKj9ayUQxnD1I3LkKZaMOHghlsk6qloWsBQ3TTmggDFzmfo_cgfpCs73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=FrWUDfVXz1UqwClHsGp4YI8Z_qzBXuK1ukpZNWSlg_IZbYlBBCxNlxn8kOuzBQ86ea-P2-L2zqui8dOrfB0W21o8CpOzhGzqFH-8FPExAZ4wZTIz3bSnaVhoA5YFw4nQa82LlimhQSy7YUQU7W-ApkzOB_j1b0ieTn91pGl8_AwTrtHzZgei0EAD8Zin8P2lIEk4aD9GlNcMODiflKH9tVpuDu1Vu3K0deBgClsr0HiwApUlgXV1li_9f_U1BL9AcUgZvbDOJRdd1taAyUeiu-5zhUAR1crrAHRz6eJZHlshdtcdJKYWOv78OWf67doQ1_OGXlFUIkvI1N3EDN8Vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=FrWUDfVXz1UqwClHsGp4YI8Z_qzBXuK1ukpZNWSlg_IZbYlBBCxNlxn8kOuzBQ86ea-P2-L2zqui8dOrfB0W21o8CpOzhGzqFH-8FPExAZ4wZTIz3bSnaVhoA5YFw4nQa82LlimhQSy7YUQU7W-ApkzOB_j1b0ieTn91pGl8_AwTrtHzZgei0EAD8Zin8P2lIEk4aD9GlNcMODiflKH9tVpuDu1Vu3K0deBgClsr0HiwApUlgXV1li_9f_U1BL9AcUgZvbDOJRdd1taAyUeiu-5zhUAR1crrAHRz6eJZHlshdtcdJKYWOv78OWf67doQ1_OGXlFUIkvI1N3EDN8Vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=DZqCbLzYWRq0KoMZV_Y5S5fVLsGMVld2ZUcFEaM6WGX-t0G9bfEMr9QNANBeCLwOMINyOJHKTPTXh717guNO4RXPRtqCkfiVEyHIoRpzCoA6vOS6urjrwEk1s5He5MWGm86KbaIBvjBjvCD2DM_eD0tsN2dvVctS7WMN2Hm1x1_RxlF7gAvgg-3N9FrmW3JRZaUPCQaun5PFVycibYFMUQdw8lsLJjxnNBgFUSOnIYxJAhMbvv2qhg9VwwfI8w0ax-n31ZwPo4sZhjRhOOACLpIE_JslPxdwVTbAekoZjk9_lqDETYGMZqlrDvdHrHZtam86Vx69V7C4_pD00o4rIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=DZqCbLzYWRq0KoMZV_Y5S5fVLsGMVld2ZUcFEaM6WGX-t0G9bfEMr9QNANBeCLwOMINyOJHKTPTXh717guNO4RXPRtqCkfiVEyHIoRpzCoA6vOS6urjrwEk1s5He5MWGm86KbaIBvjBjvCD2DM_eD0tsN2dvVctS7WMN2Hm1x1_RxlF7gAvgg-3N9FrmW3JRZaUPCQaun5PFVycibYFMUQdw8lsLJjxnNBgFUSOnIYxJAhMbvv2qhg9VwwfI8w0ax-n31ZwPo4sZhjRhOOACLpIE_JslPxdwVTbAekoZjk9_lqDETYGMZqlrDvdHrHZtam86Vx69V7C4_pD00o4rIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QM0lAdANN3HaTQs8jyOeWQL4Ete51SRYvcIOT8CQdXAZJaFeoYTFIJ0hVX4lfZYDFAxwIKb7uIPr7kZD0WAaydvaLyuWhWgVcfZ5mcI1hsdhKekokNJnT6zTxWO2ERbXG18C7Ce5nqTxqoQo2MgyUh08-KAT3GbDR0uludSrCuRezRKyWwaie_2MXXf-joHH8r1ILqUyB0aNBZzq_J92CicKsZUsY1mcmJZVO8dw-7-8BCcAGGLZGi1c1h-IaZRa13LoG64fAdeW8dkGf0Ni2huW3ofIS_VFfpTt7wTw3zzVUXNFVBvD6KupHHFb75T2RoIiYjWmRgYDzmElcQle0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=q9byGA0Z_rVmnq_KAZaO8HMtNPi0N-hWofbVhENe73Ju5NhKFOsiVhnGkypi85oWZzbZvyJ0G7Gd6BrUOAWvfOEcHXZFkf64HkkwXVxrOAfl1afYfAFHUuyb0CMqIXopkq6EMPXIZ4B5Pf1xz2rrUavE5jyLFM1DLVhvqhsYiXYF2piN3zbwueE5G6aIbDI4-pTVRSqHPvctT8aM7Kbk4p9tyrrKHROZjEjfakJcwgkvQvuK66U40YJll-WKFqhfUIDUkerf3jW-nikore8qrdUcZr2p0duBkNkELf1z27ZEItAL-_7UMCigF6K1ECrVXCpoSEj3m4A79cyXa3KQ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=q9byGA0Z_rVmnq_KAZaO8HMtNPi0N-hWofbVhENe73Ju5NhKFOsiVhnGkypi85oWZzbZvyJ0G7Gd6BrUOAWvfOEcHXZFkf64HkkwXVxrOAfl1afYfAFHUuyb0CMqIXopkq6EMPXIZ4B5Pf1xz2rrUavE5jyLFM1DLVhvqhsYiXYF2piN3zbwueE5G6aIbDI4-pTVRSqHPvctT8aM7Kbk4p9tyrrKHROZjEjfakJcwgkvQvuK66U40YJll-WKFqhfUIDUkerf3jW-nikore8qrdUcZr2p0duBkNkELf1z27ZEItAL-_7UMCigF6K1ECrVXCpoSEj3m4A79cyXa3KQ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
متن تفاهم‌نامه به زودی منتشر خواهد شد و سندی بسیار قدرتمند است
ترامپ در پاسخ به پرسشی درباره زمان انتشار متن تفاهم‌نامه گفت این سند احتمالاً خیلی زود منتشر می‌شود، زیرا مایل است افکار عمومی آن را مشاهده کنند. او همچنین تأکید کرد این تفاهم‌نامه سندی بسیار قدرتمند است و آن را با توافق دولت اوباما مقایسه کرد که به گفته او سندی بسیار بد بود. پرزیدنت ترامپ افزود انتشار متن احتمالاً در مقطعی پس از روز جمعه انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66187" target="_blank">📅 20:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=skTiPMVHmWpF1Y7X3tsnmvkylggapSl4JvNiv1Lr7KsMD_D0dlJ1KQJ16zz5jcbZWh0B3hmMRs_dQpf-mdrGsp5n47HigJYDjAiMFt031QVuLxdhBUB0BtYZ_1X6nf4l29MWR3zzyhluywZ0lr_mZx1sUcSY7nM7DnzuXyeW82KGAYlyszR34gS59FU9S4d-Tu_p7gGZ52xu0y7exGVixYC5UJrNkZbx4GZpuYJvGjmBgYf3FYap5q03eIjrC50H_a3wFVdrjtW2p0n3coTFwLda9eRNPXb0YdwKimFEeG3Xd4R0btLLjZAiw2rAkI4jYnIu2cVBbJbCQyftPh9fWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=skTiPMVHmWpF1Y7X3tsnmvkylggapSl4JvNiv1Lr7KsMD_D0dlJ1KQJ16zz5jcbZWh0B3hmMRs_dQpf-mdrGsp5n47HigJYDjAiMFt031QVuLxdhBUB0BtYZ_1X6nf4l29MWR3zzyhluywZ0lr_mZx1sUcSY7nM7DnzuXyeW82KGAYlyszR34gS59FU9S4d-Tu_p7gGZ52xu0y7exGVixYC5UJrNkZbx4GZpuYJvGjmBgYf3FYap5q03eIjrC50H_a3wFVdrjtW2p0n3coTFwLda9eRNPXb0YdwKimFEeG3Xd4R0btLLjZAiw2rAkI4jYnIu2cVBbJbCQyftPh9fWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: می‌خواهیم مسئله لبنان را حل کنیم.
آمریکا به دنبال آن است که ببیند آیا می‌تواند مسئله لبنان را سامان دهد، زیرا این بحران به نظر می‌رسد هرگز پایان نمی‌یابد. او افزود این موضوع در مقایسه با سایر پرونده‌ها نباید دشوار باشد و درباره گروه تروریستی حزب‌الله نیز گفت باید گفت‌وگوهایی در این خصوص انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66186" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=gXFl1PJwTtcI23LA7kHF3IQCRiD8G7GNPf5ciCd0nmVh8y6tqwiMzOOEBcTK3JhrNBKzvpn5ByyFQXW9v-tZd_LSp6_prgRsjAddW-a_0qip6vn285oq_BhuKsanWTt3TUpMveF1AbrQ2ES26fUVxz1OV1wJ4rnStoSh50jK5_Gm0Np12DoP8lIZEEStMgEBbaCZHnAPhZZcFf3FUOJoCccPALFK8VY11BHDET9nMvG3lovs3pHpHIEZTs6OCDSpxrS4UGJHwBbcVuhHpNf-GbUHIbNPcr5CKYHHy8pAR7OFm6B4j7ucBjiPVcMwKK3ImGUbBd7BPenc4iS4C_O76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=gXFl1PJwTtcI23LA7kHF3IQCRiD8G7GNPf5ciCd0nmVh8y6tqwiMzOOEBcTK3JhrNBKzvpn5ByyFQXW9v-tZd_LSp6_prgRsjAddW-a_0qip6vn285oq_BhuKsanWTt3TUpMveF1AbrQ2ES26fUVxz1OV1wJ4rnStoSh50jK5_Gm0Np12DoP8lIZEEStMgEBbaCZHnAPhZZcFf3FUOJoCccPALFK8VY11BHDET9nMvG3lovs3pHpHIEZTs6OCDSpxrS4UGJHwBbcVuhHpNf-GbUHIbNPcr5CKYHHy8pAR7OFm6B4j7ucBjiPVcMwKK3ImGUbBd7BPenc4iS4C_O76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
درباره باز بودن تنگه هرمز اختلاف‌نظرهایی وجود داشت، اما در نهایت عبور و مرور از این گذرگاه راهبردی بدون دریافت عوارض انجام خواهد شد. او افزود آمریکا احتمالاً به کمک زیادی نیاز نخواهد داشت، اما حضور یک یا دو کشتی از چند کشور دیگر می‌تواند مفید باشد و فرانسه نیز یکی از گزینه‌های مناسب برای مشارکت در این مأموریت است. پرزیدنت ترامپ همچنین تأکید کرد هیچ‌گاه نمی‌توان از تحولات آینده کاملاً مطمئن بود، اما به باور او تنگه هرمز باز خواهد ماند و رفت‌وآمد دریایی در آن آزادانه ادامه پیدا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66185" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=La11oN13e0irxm_Syh1Xe_lITN2y46Bsx-lzfOw4nMezn8PxBDhJy9yUAx6VgBRhiOBBqpufUEgfjLBylj90Nrv8x28hGXCHeilr7YgCbyrs6osv-n4DEMUJolHvGvTO1Gw1NiPa0dU5rRVs7t4LLp9dQiju8MsFtvUG2GBy1MUguTh1BURBsaw6BNulEGW_G2RpgtXSduOwffBGWbu_eEAue6M5GuTy9P1pAZtKyqn97IZtRONV9KoepiJMnvmWylUOJcvDzxiPqpSkBmtQ_15LhY7x80kXqi0CagNzXBWXEDZG4jJA0Z0OPMNYLnXH763E3kVfYdKFZn2ZCdDELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=La11oN13e0irxm_Syh1Xe_lITN2y46Bsx-lzfOw4nMezn8PxBDhJy9yUAx6VgBRhiOBBqpufUEgfjLBylj90Nrv8x28hGXCHeilr7YgCbyrs6osv-n4DEMUJolHvGvTO1Gw1NiPa0dU5rRVs7t4LLp9dQiju8MsFtvUG2GBy1MUguTh1BURBsaw6BNulEGW_G2RpgtXSduOwffBGWbu_eEAue6M5GuTy9P1pAZtKyqn97IZtRONV9KoepiJMnvmWylUOJcvDzxiPqpSkBmtQ_15LhY7x80kXqi0CagNzXBWXEDZG4jJA0Z0OPMNYLnXH763E3kVfYdKFZn2ZCdDELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره حضور در مراسم امضای روز جمعه:
پرزیدنت ترامپ در پاسخ به پرسشی درباره حضورش در مراسم امضای روز جمعه گفت این موضوع به شرایط بستگی دارد و در ابتدا قرار بود جی دی ونس این مسئولیت را بر عهده بگیرد. او افزود ممکن است تا آن زمان برنامه‌های دیگری داشته باشد، زیرا قرار است تا دیروقت مشغول باشد و هنوز تصمیم نهایی درباره حضورش گرفته نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66184" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=PgluYt2plhAMw9CHTP9QxpMeMxS26MBPl9sjyNveb9KSurz6G2Xt3KpRS4Ysp2mPhLM0XhdTbCcjBX9eIGc-EIJpD3GKtdBZHHs8qWLKg_cteEo8rt_g1xZwvpBhqxqKduw3qS61tFJwzbKOIkSdohNmkwom6s9HrSlMJOBtIIeJoCi9x5luhb3TN5eazH22DYv366Uo9vK0EftPs0Gu1undCg6bXs4e4KzlM4mDmik03_wyJXWpzZxfwtFJikxfh7vyU_SieCJv0VqoAEOor1w42WPgS6ONx8PfQ4gZt-hA4JA1CiMa439hqGOrVfwEdroX99M4Lsx90vh68O_QGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=PgluYt2plhAMw9CHTP9QxpMeMxS26MBPl9sjyNveb9KSurz6G2Xt3KpRS4Ysp2mPhLM0XhdTbCcjBX9eIGc-EIJpD3GKtdBZHHs8qWLKg_cteEo8rt_g1xZwvpBhqxqKduw3qS61tFJwzbKOIkSdohNmkwom6s9HrSlMJOBtIIeJoCi9x5luhb3TN5eazH22DYv366Uo9vK0EftPs0Gu1undCg6bXs4e4KzlM4mDmik03_wyJXWpzZxfwtFJikxfh7vyU_SieCJv0VqoAEOor1w42WPgS6ONx8PfQ4gZt-hA4JA1CiMa439hqGOrVfwEdroX99M4Lsx90vh68O_QGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
پرزیدنت ترامپ گفت آمریکا کار بزرگی انجام داده و امیدوار است روابط خوبی با رژیم تروریستی جمهوری اسلامی شکل بگیرد و دو طرف بتوانند با یکدیگر کنار بیایند. او افزود اگر این روند موفق نباشد، شرایط به نقطه شروع بازخواهد گشت، اما معتقد است نیازی به چنین سناریویی نخواهد بود. پرزیدنت ترامپ همچنین تأکید کرد توافق انجام‌شده با رژیم تروریستی جمهوری اسلامی می‌تواند دستاورد بزرگی برای جهان به همراه داشته باشد، زیرا برای مدتی جریان نفت در منطقه با محدودیت و اختلال مواجه شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66183" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66182">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz5J2vxMsWU-4uIplK5hfMoOnF7_wTbwEzHhZXklYf86l6yR057ZHfHHhq7phRZg9rbVXx-suJ8qDGcdUy9YabRSkeIL4Vnua6vnujR3zuTjOFWc4iBGIW6sHeLjSHMC8Y_N4HWIjBwSC-iaWsbtS2GDfjLGn_QjSbEaal9tOogWY5uPKK7i58yOwNlopWMoEIUGs2-XeH0ASCfKA12dt7KNm91HbzMqLL-uk9hS4aVDDYhKSMJXHaNwGKA_7TS_drYHoo82Z3sk49ZruTMnYDoTBrrPMEqwfnH9K9_PPsuZDgMQh7Q54i0DaJVZQcZYL2Uol6-5UiY4R6gRjj0n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
ملت دوست‌داشتنی و سروقامت ایران! با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.
ایستاده‌ایم و در نهایت ‎
#ایران_ما
پیروز خواهد شد، به لطف خدا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66182" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=FDNqQUTYuUibK2zERGvi59zWpAkwOy5qkgPcrmVRgind0zl2wCa4J8IQ_Rtny17jPj48ohVViHij9KjJvl06ehDojMKU6vgP9Sb7QQ-jXeDJ-UwWbd-YflmNAIwlwprPfaF4DdNTiWMAjU7I9IdV6oXOEvSW-FPdYFh9161r2GPQUmwU4Ox4oGE24zFMA1OV8SZcfo2Ssm-tFBgXGVaSB8TgW5tkxNLNeILrERhJSxVCwIrYNC6SX-AUgAdd8BQSEIEwvDHPw2K4wO4NYhvWdmjqfomyD3SUJ6aTz-NdD7d-2Aae_U7tfKpw3VXSsFGM2QW28myf5u8cIy2PcqvrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=FDNqQUTYuUibK2zERGvi59zWpAkwOy5qkgPcrmVRgind0zl2wCa4J8IQ_Rtny17jPj48ohVViHij9KjJvl06ehDojMKU6vgP9Sb7QQ-jXeDJ-UwWbd-YflmNAIwlwprPfaF4DdNTiWMAjU7I9IdV6oXOEvSW-FPdYFh9161r2GPQUmwU4Ox4oGE24zFMA1OV8SZcfo2Ssm-tFBgXGVaSB8TgW5tkxNLNeILrERhJSxVCwIrYNC6SX-AUgAdd8BQSEIEwvDHPw2K4wO4NYhvWdmjqfomyD3SUJ6aTz-NdD7d-2Aae_U7tfKpw3VXSsFGM2QW28myf5u8cIy2PcqvrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف بعد تعطیل کردن مجلس و انجام هر کاری که دلش میخواد
😂
:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66181" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66180" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66179" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66174">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQfpv8Ortapvo4_ZQVu-PCAq4XerVHetLN5w7t-lTjJSVWLhdbZVR9WcQM9GaI4iOLkIsnsPGWyol0EdQM35DvwYXJVbeeVYZDfyjBf0njzCGAs7Vs0eJpopdSwW4vp8x6czPH7zYGHJBf8ZkOOOVochudUXPsrbRufh0YWIXl7E7yIOGdMe9zRnPqJNoaYcQQpCrQKsSONW9nZJ4itnsMMA2Mc2-nHitaAhFLsAKZ6C-RaHSJOIlJ1U8zanpVUNYAXeUn82rDUlLSXDngfehi-1JYWKyxb_728yeDJcir6DF8wrFTZMkh9fFeKU2W5jQQVrrI8C2dFcOdmfIvql1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIGUxBQmWe0W-28fxnuwyY4tmxTLVee03jGLMeUwykr6oZON0_wspWHmCD1lWDs6wijej7m8iHKTUMHdIC3ktES3Ubb_UQ7DdOHliIdlVIuAizbgWB4U76rzl07XeXjG99P_3EUWel0rmBAVqykWEoNlDHYLc7FMUXXOWKIilfZEDtEOo3XJ81znvFeGgMALHjfkQiF8eD2pXTpmLHw3eQ_xLYTYDAyr2nOd8OCkropk0r9-dfdYxs243cYAUC2Nu8ZN7ShG_Cc07ibCJmGoKZHM51TwnwKBbEBcPlGWkliR4fLuNNrfUlwL2BgqRcMR1FIT8FWysjhBmTdMghFqow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=At6CagyaBob-fcQ29Pf3YrJ_fbaPxCZMcOWC79S2Nc4wqLduDoy5RUR1bdldscm-ae4o8ZviRI-ISeiGuSVRv-FoFpziZ1uO2hT57WeBls1jXGxE18ydvlxkeJT4ko97xjKFAaYPKY9nGwDQ9xBzfq2RC61oscRQYm0obA69gfDEoBKOrzt3XrkayBAM29VNXUjjwvzAnusbHN81warNJ2FvrBR_0pZcrrB2_HJ0AjJ13fm_ng-fQpx5eFp3IkvaV0KvKWXyr_loOGPTVYR3qHN_JwtT3L2w4eUhsMQHVfYWScfByDJL-Cs2VY0DLT-CquBZvKTlGcLW6RiQb-eUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=At6CagyaBob-fcQ29Pf3YrJ_fbaPxCZMcOWC79S2Nc4wqLduDoy5RUR1bdldscm-ae4o8ZviRI-ISeiGuSVRv-FoFpziZ1uO2hT57WeBls1jXGxE18ydvlxkeJT4ko97xjKFAaYPKY9nGwDQ9xBzfq2RC61oscRQYm0obA69gfDEoBKOrzt3XrkayBAM29VNXUjjwvzAnusbHN81warNJ2FvrBR_0pZcrrB2_HJ0AjJ13fm_ng-fQpx5eFp3IkvaV0KvKWXyr_loOGPTVYR3qHN_JwtT3L2w4eUhsMQHVfYWScfByDJL-Cs2VY0DLT-CquBZvKTlGcLW6RiQb-eUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از آتش سوزی گسترده، میدان تجریش تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66174" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66173">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
نتانیاهو قراره تا چند ساعت دیگه سخنرانی کنه و این اولین واکنش اون نسبت به توافق هست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66173" target="_blank">📅 18:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66172">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66172" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66171">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66171" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Dxc2N_SOSMN9JhjaCY7R8qOTyhBXg0NScpVlNdFodRxZF-J9rSeXe_evG8BGtLVq40zYEv05b7cI7k969yzPfgkn5CG4itSyQN8lFzW5bhwcAd5bQkiWsB_pHMqDKFfUnTwYsWI7vR6estCwGDmipRi-Sk1Sr6vqafo1fcZArQUufs0TcTsyuV8AV38jHd4FvaK9sqHtDKB8L_xVgSodL7hBic3pl9Dgq42kMX1zRVUEHLNf5ruW5_o8187ChufeqOSeJ5i1yIpsh2X2gyOnzCJaWganZjbg0ggPLbf0LBI_tHSMcOgN-E21CwGJ-PPrwZa8Sheow5OC_uxUUMR2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Dxc2N_SOSMN9JhjaCY7R8qOTyhBXg0NScpVlNdFodRxZF-J9rSeXe_evG8BGtLVq40zYEv05b7cI7k969yzPfgkn5CG4itSyQN8lFzW5bhwcAd5bQkiWsB_pHMqDKFfUnTwYsWI7vR6estCwGDmipRi-Sk1Sr6vqafo1fcZArQUufs0TcTsyuV8AV38jHd4FvaK9sqHtDKB8L_xVgSodL7hBic3pl9Dgq42kMX1zRVUEHLNf5ruW5_o8187ChufeqOSeJ5i1yIpsh2X2gyOnzCJaWganZjbg0ggPLbf0LBI_tHSMcOgN-E21CwGJ-PPrwZa8Sheow5OC_uxUUMR2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=VRzi7eNEoNCZgCIVN8rfs5NvfrskuYU2nhTeP3bRlC1LicBDMPXngDQ72Sc1cDQQHbuAbAdMiAt14HLj_k3R_EZEC9qJdu7lbRcSpbVs88ZQVxAoCVX4ikaf1QACwlaXbwTVP5MErTvQja1pUBEu43ZOKQ00PWJtGwhSdS-Jx4hX0hGAQ-89V7uKoz2x0IXYRSSz2tAAaY_ydA82L8S1afjDin3I6Lk_aNZwzncdFMGzxeADwARqK32KdufZSm59U1Ka3vBDtfwq2pP29qF1RuUsXVXkvEvwwtYTshWOoolM71v31z5iE7cVSBCevLMnegNB8zdRJc2DgyBdksz7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=VRzi7eNEoNCZgCIVN8rfs5NvfrskuYU2nhTeP3bRlC1LicBDMPXngDQ72Sc1cDQQHbuAbAdMiAt14HLj_k3R_EZEC9qJdu7lbRcSpbVs88ZQVxAoCVX4ikaf1QACwlaXbwTVP5MErTvQja1pUBEu43ZOKQ00PWJtGwhSdS-Jx4hX0hGAQ-89V7uKoz2x0IXYRSSz2tAAaY_ydA82L8S1afjDin3I6Lk_aNZwzncdFMGzxeADwARqK32KdufZSm59U1Ka3vBDtfwq2pP29qF1RuUsXVXkvEvwwtYTshWOoolM71v31z5iE7cVSBCevLMnegNB8zdRJc2DgyBdksz7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=h2X8ddmfkbSV-QbtgUK8_pw460_fSuwD6V1_mLQ697ozWdS6CfgGFWE_SsTW8BW94C8gWt1viMTNNpR4DL8nRi_LuflXtjok7V5kUsxsJOF0aFTPX__VWlUpRVU3rePUENTXZVh3QIZtxRLZvP7wxYcxWmP_Qr4xGQb6SOw3yczNMGfSg2LqLxGCLaMxkliaSyt1E4lZg1hKtbatImkK98gr4mVc0VgUKmbEyLY9a-doSIqkSGwmvQ3wghuE3MYzggNQPq6IsimZcqKxpxVrhvrNm-MbVz4WokmW-wXCheEdBLPbJJwHcdvxFfsjIvvB77pkRfyJdHLnoGgKnsbOqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=h2X8ddmfkbSV-QbtgUK8_pw460_fSuwD6V1_mLQ697ozWdS6CfgGFWE_SsTW8BW94C8gWt1viMTNNpR4DL8nRi_LuflXtjok7V5kUsxsJOF0aFTPX__VWlUpRVU3rePUENTXZVh3QIZtxRLZvP7wxYcxWmP_Qr4xGQb6SOw3yczNMGfSg2LqLxGCLaMxkliaSyt1E4lZg1hKtbatImkK98gr4mVc0VgUKmbEyLY9a-doSIqkSGwmvQ3wghuE3MYzggNQPq6IsimZcqKxpxVrhvrNm-MbVz4WokmW-wXCheEdBLPbJJwHcdvxFfsjIvvB77pkRfyJdHLnoGgKnsbOqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=vLAshzHs5fAiaW2goq94e0JeMJkAce8Fen6E5K4wlKNjK6bkTg6o8Zv6O2GIofORF77Vpi5UxQ-F1lktLBoMXoQZc4XS7WUyazOQMy_jvjmewHvfB3GRGrD8Er3XCGFQM2suU8foCaGIai_0kgWeOpcXdwiZnIMSVw-tEknVJXfb_OG5vftGsucpGNuCmseGTuEGeN47IZMSrU8N6XOqjC-QAbeRsOUL9QNd-vhHtIjF55po6g3aAroiTLxgCY2PinJ7CiVJBrRERo-0aca48xG9lZVWi_D5JVeJoOodhS2pW6XQWLTG2Tao48eakF6-TbEd7tkZiGMHRl8lh8XqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=vLAshzHs5fAiaW2goq94e0JeMJkAce8Fen6E5K4wlKNjK6bkTg6o8Zv6O2GIofORF77Vpi5UxQ-F1lktLBoMXoQZc4XS7WUyazOQMy_jvjmewHvfB3GRGrD8Er3XCGFQM2suU8foCaGIai_0kgWeOpcXdwiZnIMSVw-tEknVJXfb_OG5vftGsucpGNuCmseGTuEGeN47IZMSrU8N6XOqjC-QAbeRsOUL9QNd-vhHtIjF55po6g3aAroiTLxgCY2PinJ7CiVJBrRERo-0aca48xG9lZVWi_D5JVeJoOodhS2pW6XQWLTG2Tao48eakF6-TbEd7tkZiGMHRl8lh8XqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
