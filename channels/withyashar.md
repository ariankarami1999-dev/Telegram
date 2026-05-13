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
<img src="https://cdn4.telesco.pe/file/Bv7gP7nZvNVUGBF8tmi-E1IxSO3qas54juQxOWZOnSP8-SiaVyI52ZfAfcSi0hKKxhbgnDzOKNb4fdv41qmcj_QPVht46KermKP9y42I7vR37Vd50jTFYA2qafbqgqIKOIoV6xgE9HUVziWOpkoFnJCaDvADeuG8sSbsYKglIRWlcoupKMEfvVFgyVzdgC1VZeuQzS_jYBNTW_zzdeKY-zf2kz1xwpkjFj_KUL-JrTPwf4rCREgUyiEKxybnLVGlztSmg3qW3qZ9JsCOh9Gi2fNrJhNzpNG0vJGbzyT9ug1_RSKb2qGiB_M590_2kVn-vBSzlQokPHEXfSwjbd-JxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 259K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 20:07:55</div>
<hr>

<div class="tg-post" id="msg-11157">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=cQmqRKmYVcpmd67zVuJFEbds8vTM59Y48CPtZ6eedt-hqc6AWLjbifJUBeJi2fQWNqs2PlWW3vi8nJfQboLCGiMqEOPxhnxZxxkqAJJfC935W3dTiPqu8MS48DGhU8fGztANo6tyTf7JSdL8BxaySLinxzVg30dnRiRHZlBfVybg5bBgnkR2b1jc7GN7RZkhGCiOaKUC7Xi4B0uPhOQQx2mzVQ66c678EF5DRoCqGAP5FEKseFq__sSAbl4xUa1Aq8gbCxFciHPUboSAMSG6ylaT7q01eNosmTRGaCuJyvyNCVjWIee_VNZv5Y5MyGqy9mgyHK6sSBfP6wMyjCnepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=cQmqRKmYVcpmd67zVuJFEbds8vTM59Y48CPtZ6eedt-hqc6AWLjbifJUBeJi2fQWNqs2PlWW3vi8nJfQboLCGiMqEOPxhnxZxxkqAJJfC935W3dTiPqu8MS48DGhU8fGztANo6tyTf7JSdL8BxaySLinxzVg30dnRiRHZlBfVybg5bBgnkR2b1jc7GN7RZkhGCiOaKUC7Xi4B0uPhOQQx2mzVQ66c678EF5DRoCqGAP5FEKseFq__sSAbl4xUa1Aq8gbCxFciHPUboSAMSG6ylaT7q01eNosmTRGaCuJyvyNCVjWIee_VNZv5Y5MyGqy9mgyHK6sSBfP6wMyjCnepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همراهان ترامپ در چین
@withyashar</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/withyashar/11157" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11156">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سد عباس چپقچی وارد هند شد
@withyashar</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/11156" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11155">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/11155" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11154">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=WRCzjAimrpgONLygF_cvG4zhK7WCXMsG3vDRlzQuPBY_tbPLXCQObk3i3QjilV1zGwx94Vg7rJc0tVMIPIdrW_Iu6VMbHfioTznNF7SZ6EeFY1EeoYlVbNYSuGcJ9wC9M5XwqKU5iiGeWU3PnWDwr4Fq6xIh-vU5lGRubT5KPhdROffhxBfdmND7ViNsgiHnM9EW7gwB-tbbWnChD7aPMOs_AJhlURFuvd4G2kGDiwqmB9Yqs5wzGCclm_jF1LMmkAs7sJ7anfrhe4bVVPBvYzPELr5_XlURjb6sFzB7chGd4DV_vx1ME3FAlPNZ9ghv_DA9IO-E36mLjHOVnC_dMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=WRCzjAimrpgONLygF_cvG4zhK7WCXMsG3vDRlzQuPBY_tbPLXCQObk3i3QjilV1zGwx94Vg7rJc0tVMIPIdrW_Iu6VMbHfioTznNF7SZ6EeFY1EeoYlVbNYSuGcJ9wC9M5XwqKU5iiGeWU3PnWDwr4Fq6xIh-vU5lGRubT5KPhdROffhxBfdmND7ViNsgiHnM9EW7gwB-tbbWnChD7aPMOs_AJhlURFuvd4G2kGDiwqmB9Yqs5wzGCclm_jF1LMmkAs7sJ7anfrhe4bVVPBvYzPELr5_XlURjb6sFzB7chGd4DV_vx1ME3FAlPNZ9ghv_DA9IO-E36mLjHOVnC_dMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌حرکت ایستادن کامل افسر چینی هنگام عبور هواپیمای رئیس جمهور آمریکا (ایر فورس وان) در چند متری او، توجه بسیاری از رسانه‌ها را به خود جلب کرد
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/11154" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11153">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک مقام ارشد کُرد در گفتگو با کانال۱۳ اسرائیل:
در واقع خود پرزیدنت ترامپ مانع از طرح اقدام ما علیه حکومت ایران شد و اتهامات او در مورد ضبط سلاح های معترضین در ایران توسط کُردها، ناعادلانه و غیرمنطقی است
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/11153" target="_blank">📅 17:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11152">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با شما : گزارش از جنگنده های ناشناس پرواز در ارتفاع پایین در‌ ارومیه و انفجار در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/11152" target="_blank">📅 17:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایال زامیر ، رئیس ستاد ارتش اسرائیل:
نبرد تمام نشده است، ارتش اسرائیل آماده از سرگیری نبرد در صورت نیاز از کرانه باختری تا تهران است
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/11151" target="_blank">📅 17:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH02efNYZXF5gHa4Usa_Qyp4XOOTgJ7SkXWMcDQ-mkMzKSVprCrF5QJxVV_aEony0tC7502VYL0JxwvVEoQk4H9RywYRT8v3qcYoH7sniXrEMWKI53F2lT_-W7mL1HHglJ3bCc0QcX5wUQEnfnnUD5pfGYm2oDqbZ4RJS8S-Cm1v1w3dXLLCvUmZPJu_iiSlgg-q2R4-tOKnak4DqzROApYI6vy4GBmlTkdDSLOP62cjjQBhoJxZu8aLkT1jqHHthR8q93lXMU53cxpLITefQDXFe_4twXJNITEHZWmDWqKCJ5u23Ird59Ow-6sUlSUVLLI2U5z6AdkMonehL56i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه های ترامپ با حاکم چین به این ترتیبه : مراسم استقبال تو تالار بزرگ خلق
چهارشنبه رسیدن به پکن ، استقرار و استراحت
پنج شنبه ۱۴ مه
- ملاقات با شی - ضیافت دولتی با شی
جمعه تاریخ ۱۵ مه
- جلسه عکس با شی- چای با شی
- ناهار با شی و حرکت از پکن به آمریکا،
@withyashar</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/withyashar/11150" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5924e9f0d5.mp4?token=aTG5RYHXqyxmUVp2Pdt897MduAOq3i7LR1-a_H8wOcyXWcDwOJ8Bh-LofHFPcqYPQwIZokwkikndmoW3bvo1wjG1SEI2-Hk7z_R_jqJdsUWKx9kwihGH16RszZDrxs9FXgoMuCjHMd9nk53rn5Pmn6O9vkpe4L__lnHV4tSoAaaguF47sEbLtTsljivFnAFN8ADy5OFDK2glTUvhI0V7PereE32xbIinwPsDUHY9KAWonqXyLR8wRBSliwOvhrsjxAbf8urHmizyQJvbKeTCEzi0EBasUy1blK1ZrqCGSxJotjmCg3xpOqwGEL6Jh7boPC4Rp7g8SWOA7TgWgZsSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5924e9f0d5.mp4?token=aTG5RYHXqyxmUVp2Pdt897MduAOq3i7LR1-a_H8wOcyXWcDwOJ8Bh-LofHFPcqYPQwIZokwkikndmoW3bvo1wjG1SEI2-Hk7z_R_jqJdsUWKx9kwihGH16RszZDrxs9FXgoMuCjHMd9nk53rn5Pmn6O9vkpe4L__lnHV4tSoAaaguF47sEbLtTsljivFnAFN8ADy5OFDK2glTUvhI0V7PereE32xbIinwPsDUHY9KAWonqXyLR8wRBSliwOvhrsjxAbf8urHmizyQJvbKeTCEzi0EBasUy1blK1ZrqCGSxJotjmCg3xpOqwGEL6Jh7boPC4Rp7g8SWOA7TgWgZsSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ورود ترامپ به چین-پکن همراه ایلان ماسک و همراهان
@withyashar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/11149" target="_blank">📅 16:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بلومبرگ: صادرات نفت ایران از جزیره خارک برای اولین بار از زمان شروع جنگ متوقف شده است و تصاویر ماهواره‌ای نشان می‌دهد که مخازن ذخیره‌سازی نفت تقریباً به ظرفیت کامل خود رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/11148" target="_blank">📅 15:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDp85xdhEDXq5wB10-H2ukXWGCBuK7UvJClliKe6oLPs1z2skhCgt19WqSrNpXEbYcA7OEEG-RtDrbi-QTjwNKHHZ318qkvSLpsXIbQfpPZMkeLNHhICzQrdALSTGCyk_ks491gO4UxoW48hYb6KseDLITfCpjP8tb_fvDVnGsleObxnON30lsV-MzfbJ1AiUQmjGz2QOOUu4R8-W04ZPcgfm9GpVE73lJ-RKP1Y6SB8Ai5OR1zc03O96HGuIOCRKTypzghrpDQlnfFWkWGLacJ8iJ4Ljt3bXAZ48h_AW9bJgYHhL8C1-OEUcOVYf6bVJIGsDfaqqHeBu0R7Tv4Tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به پکن رسید
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/11147" target="_blank">📅 15:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0Nf2vw4nHtFaRYZArWBX5fQPpBllv99uprP1J8SIagb2UjM7Lnv3iGZizfZ53nyQX1nyiBamRYXluPeJyCEPCqnFD2uhyAplXn46rWcqjqShl_HLyTlBw1algUJiKRcb2Tk9Qgd2ZEXqrF1yDUhZHhNp-yaZvd3uoAI_1QerG6msCc-uTyP7xl2TolubYx-kD2VgFvPvvBI_MFdkPeZuJrHAMykkFLA5BL1deMk1y5sb5A_meiuvNO5U7nsDQ3DQktQp2SJ18UU7U1istKlrId25TAxzw5WaCjewYfuDwkzkoptbsi28tgVO7M-Gy8qIbnlsab8MFa9I0G3DHXDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون ظاهراً برای چندین ماه با بازیگر ایرانی گلشیفته فراهانی رابطه‌ای داشته که شامل «پیام‌هایی بوده که گفته می‌شود تا حد زیادی پیش رفته بودند». این موضوع ظاهراً باعث تنش در زندگی مشترک زوج ریاست‌جمهوری فرانسه شده …گفته می‌شود سیلی‌ای که سال گذشته بریژیت به امانوئل مکرون زد، به پیامی مربوط بوده که در تلفن رئیس‌جمهور پیدا شده بود. بانوی اول فرانسه ظاهراً گفت‌وگویی با
یک بازیگر ایرانی دیده که در آن، امانوئل مکرون نوشته بوده: «تو خیلی زیبا هستی.
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/11146" target="_blank">📅 15:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این پیری رئیس باند medea benjamin از باند نایاک و از مهره های ماله کش ظریف هستش شخصی هم که به سخنان شاهزاده حمله کرده اسمش «بیتا» هست  … اطلاعات تکمیلی به زودی … @withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/11145" target="_blank">📅 15:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B37wSO7S8XJvHaxDO2CyMV8JFvUXQZoynRxPnvhlG37KcA5cxH3gJFmtDrDagnDvV6Qh3JoBiwqHeXfyi0kMjRcFthQX52FGda2lZjG_G1w53TiyJwr5HzUJ-2rAHcQfqlmEpZXi6hhVkg_4BGs2Hpk6289qojKN8EO20PMFfqAavbfTrq3rttNFocAQvDD6xvP-NxnhOY_bNaamJH4nEd3p_u9TTJBSCX3Xd-5iwl0JsZ1kxl7Fq4QDmq7s6rZax_8vXYLu9zb9RPobiGd33uWybZqDjrMOveUjcCVHiM2-7IIBXyvL-4gIxxl9n5hrFmGmK9bMm9Q6Bj-KzaJy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیری رئیس باند medea benjamin از باند نایاک و از مهره های ماله کش ظریف هستش شخصی هم که به سخنان شاهزاده حمله کرده اسمش «بیتا» هست  … اطلاعات تکمیلی به زودی …
@withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/11144" target="_blank">📅 15:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/691ecb2a9a.mp4?token=nAVR_ISsnFWa_xeiPu60IGlhJnApXeYy0JFLvA5e9azyXb1mpaHL15JsIIIe5XwTqto3u_FBEjzJGumX-hWLBWdJXQVDiuNpIIQQFBKPJP949g4lD9mXsbF0NExr6LORpxcvzX1FlyW8xQeHGYtaemsrqmW1pa6yEO5U6VlKTcT6GyIeFEOotnBjBJGmtH8SKzj1hFyoBtFHfw2B3qqBSpV1ohmqFsioSWudJ3F-k50Fa7-frN5f5vsF2EP0GC2zknczk4frhPptp0UXelhimIM3bw9gTjMHf7LBTaH9gaVY0QRpaNtXob-Eg2rUDCe9AjqQIm1qXMEWKhubxv4pVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/691ecb2a9a.mp4?token=nAVR_ISsnFWa_xeiPu60IGlhJnApXeYy0JFLvA5e9azyXb1mpaHL15JsIIIe5XwTqto3u_FBEjzJGumX-hWLBWdJXQVDiuNpIIQQFBKPJP949g4lD9mXsbF0NExr6LORpxcvzX1FlyW8xQeHGYtaemsrqmW1pa6yEO5U6VlKTcT6GyIeFEOotnBjBJGmtH8SKzj1hFyoBtFHfw2B3qqBSpV1ohmqFsioSWudJ3F-k50Fa7-frN5f5vsF2EP0GC2zknczk4frhPptp0UXelhimIM3bw9gTjMHf7LBTaH9gaVY0QRpaNtXob-Eg2rUDCe9AjqQIm1qXMEWKhubxv4pVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیروز گروه «کد پینک» به سخنرانی شاهزاده رضا پهلوی و وزیر جنگ هگست
@withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/11142" target="_blank">📅 15:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN9FvDjLWukIt5AhQZogxCQe9Ph0D2xxCgMzidMhqIsf03sRheBshA8voXPu5M4yWUqJyyTdLhfw0LrafSYgWVEPVluP3GPxlIcIk7ql_WxMIeCjcZGHb3GL82RNlUzFUIstiSHy6sRsOUlA-jApHu5-SYaLTj_SLRrPU8ffmT21v21C7AMXjHC7CXzOVNG6yxCzApIhrXhjcBtfVbzzTIaYVOZrDX1B_e8pnTb6Jf53SlZMqLra1pmFl_M-eyVdyebSC26nUwrY0OthkRmpvcPA8r88C98U90dDH0dpdjaGqMcvZ_UwVFLGh2ZbmLrUB-nnU1-Dl5aZYReCljZmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گروهی اومده بنام « کد پینگ » سر دسته شونم این پیری هست
Medea Bejamin
حمله کردن به سخنرانی شاهزاده و وزیر جنگ
@withyashar</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/11141" target="_blank">📅 14:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایتالیا اعلام کرد که کشتی‌های مین‌روب خود را به نزدیکی آب‌های خلیج فارس اعزام خواهند کرد ولی شروع مین‌روبی‌ ، به دستیابی به یک آتش‌بس دائم و پایدار بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/11140" target="_blank">📅 14:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام یاشار جان خسته نباشی
❤️
تو یه اتفاق جالب با همکلاسیم نشسته بودیم تو سلف دانشگاه غذا میخوردیم،دوستم پرسید اخبار چک میکنی گفتم اره،بعد نشون هم دادیم گوشیامونو
😅
چند روز پیش کانالتو براش فرستادم،البته از اینستا میشناختت ولی کانالتو نداشت،و پیجتم دنبال نمیکرد…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/11139" target="_blank">📅 14:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Dh05-0PFQ7XHX4t3CVaalw1-uwlX7sUetu93D3722dCCeSWJn8CbWD8f2D78MVWYgD3YEE4urMALktBLsBbQkixARLOKHFwwYbffgZUpW_IsQtOjUas81oIa81WoME_Tk8wOxFoWzLgPuh4vodltb9xuCO_aSYGujYg0czHADbQBPFNgpqqZG8-qK4QAqgRNKz4jftx-aHh0aQ8UyN-qd-o-HaVhdaXby8kxHp5satxmm2YR4MLgXwkrg-b8W6lysh2ZWzV_Hze9cu3Fhme2vveebzKlumtcU_VeFfa0YHQssgtL1xxIcLu4bXwpKL-MmCaS8t02WiLSpNazvlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام یاشار جان خسته نباشی
❤️
تو یه اتفاق جالب با همکلاسیم نشسته بودیم تو سلف دانشگاه غذا میخوردیم،دوستم پرسید اخبار چک میکنی گفتم اره،بعد نشون هم دادیم گوشیامونو
😅
چند روز پیش کانالتو براش فرستادم،البته از اینستا میشناختت ولی کانالتو نداشت،و پیجتم دنبال نمیکرد فقط چندبار دیده بود.
دوستم‌گفت بهت بگم‌ همش اخبارو چک میکنیم و منتظر اخبار بعدی میمونیم
😅</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/11138" target="_blank">📅 14:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adfgznRVh8JTey0GeNnSMX0jgWetN9Ew9wbCmC5nIV92Q-pS5XUAFTnZ35c1xNmA83ni5SanvjqSn7XB_m4gA4DWIm3QbZxdISQHdHCra5AwzD-Puc5PJv7OxjpM47HaCFM-Pi8OH0JCopSzTj0vAby6U4q4fQfbTbLMwwbXQ_LChHsmWE2xPQnDj5gnKpmJW5yyhlj6RSnL94QgYlDF0ckWMQhVDlCnmVG4bFjlJ-Vg2AzoNdBLZlGLpcN5EZ_9-EQ1rsruLCNZZWQC7l2uUIPMyO_dLhhZUmULfVxxVGax3InSb3HExx-KMP2cLzmE7J3eI42rBp3dbuGX99tM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین «نمایندگی رسمی مجاز اپل» یا Apple Authorized Reseller در افغانستان افتتاح شد
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/11137" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیو دی‌کمپ، روزنامه نگار آمریکایی: شاید ظرف یک هفته آینده شاهد بازگشت به عملیات نظامی بزرگ آمریکا علیه ایران باشیم
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11136" target="_blank">📅 13:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند @withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/11135" target="_blank">📅 13:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی وزارت خارجه: ما عملاً در یک آتش‌بس اسمی قرار داریم، اما طبق حقوق بین‌الملل، خودِ محاصره یک اقدام جنگی محسوب می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11134" target="_blank">📅 12:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب جلسه امنیتی ویژه در مورد ایران برگزار خواهد کر‌د
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/11133" target="_blank">📅 12:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbiQo6rjbSexTHLanMHlkCi2etLfvfmNcYjFqMepf0lgz4G3UCnvU61ySHv1wUxbaQ2Kk0OzmF8rOx0VwXOibhPHCNO_-ABPCbLTBeBwy1cUTmK9q-2utL4OD7fWqVfXTvS-IG4Trh7BGkUH0QvgRAVGaB765rkD1eM6N696pFv8RLt292yezHS8UF93VmLMw36bx6mTPJQHDdgwozjfmfxnVmpBCpO3KZAqDuHPbrAcVRC_CFMfa4hbi45zSMT4qk9RHBVnjD6RCAmgO536M9capV5hsYcdrkkGFi_nVyCMI1FUdfvZ_fiIcnMIgkqOLObUBOQ1IbWFVZteIY2Kxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11132" target="_blank">📅 12:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فدراسیون فوتبال: امشب مراسم بدرقه تیم ملی فوتبال به جام جهانی، در میان تجمع حامیان حکومت در میدان انقلاب تهران برگزار می‌شود و قرار است در این مراسم از پیراهن تیم نیز رونمایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/11131" target="_blank">📅 12:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عبور ابرنفتکش چینی از تنگه هرمز همزمان با سفر ترامپ به این کشور
داده‌های مارین ترافیک نشان می‌دهد که کشتی
یوان هوآ هو
صبح چهارشنبه در حال حرکت به سمت شرق از طریق تنگه دیده شده است.
برخی بر این باور هستند که عبور این کشتی نوعی اقدام مبتنی بر حسن نیت از سوی ترامپ برای جلب نظر شی جین پینگ است.
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/11130" target="_blank">📅 12:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک مقام ارشد سابق موساد: ایران ممکن است ظرف چند ماه از نظر اقتصادی سقوط کند اگر محاصره ادامه یابد
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/11129" target="_blank">📅 12:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/11128" target="_blank">📅 12:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پروژه هارپ یه پروژه برای تغییر در آب و هوا بود طوفان میتونست درست کنه ولی زلزله نظر اکثر کارشناسان بر این بوده که امکانشرو نداشته و فقط تغیید در لایه های جو بوده به هر حال دهه نود ساخته شد و ۲۰۱۴ امریکا گفت پروژه کنسل شده ، ولی تئوری توطئه زیاد هست درباره این پروژه
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/11127" target="_blank">📅 12:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">سلام مرسی از همه زحمت هات
زلزله میتونه پروژه هارپ باشه؟</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/11126" target="_blank">📅 12:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11125">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">درود یاشار جان، خسته نباشی. مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی. داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟! قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/11125" target="_blank">📅 12:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11124">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadegh</strong></div>
<div class="tg-text">درود یاشار جان، خسته نباشی.
مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی.
داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟!
قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل ۴۰۱ بود فک کنم.
بنظرت میتونه چیزی بجز گسل و دلایل طبیعی باشه؟</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/11124" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11123">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlS5Yj9zjnBT--WF8p4yUwgW0gkRaEIJ3E-gFhbeICypbY-yjDtxSSyGEAIvxa5iFVqcdR4ASXts5EfJBgXTJcW9RUt7uSNgAR-7yk6-8yQuwcHbtp7qk3rapDhOnTcID8wSP5I1vS82YNAPNAXeocGtCfJJ2jYi4WgSR3HQ_mSFc5mOK4vHeKAf1-fbhv8nEQym919WYzm1ZAga0d0zuyN1HlEj1vwACpIBOVDfRBwPcERzA2o51Mfe32CEYdCdr57tb9k6hAYY8krkOio05eM2j_FJiyuxuCb-93m_uNP1WX1QKBQBsp6xu3_fc_mQOu79_zk0HuZ-EZGxcV5HTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهندس ارتباطات حزب‌الله که متخصص فیبرنوری بوده و پشت توسعه پهپادهای انفجاری این سازمان بود،   توسط ارتش اسرائیل به هلاکت رسید.
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/11123" target="_blank">📅 12:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند
@withyashar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/11122" target="_blank">📅 11:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش مرکز ژئوفیزیک از شدت ۹ زمین‌لرزه بالای ۲.۵ ریشتر در پردیس از روز گذشته تاکنون
ساعت ۲۰:۴۱ — بزرگی ۳.۴ ریشتر
ساعت ۲۳:۴۶ — بزرگی ۴.۶ ریشتر
ساعت ۲۳:۵۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۶ — بزرگی ۴ ریشتر
ساعت ۰۰:۳۲ — بزرگی ۳.۴ ریشتر
ساعت ۰۰:۵۴ — بزرگی ۲.۶ ریشتر
ساعت ۰۳:۲۹ — بزرگی ۳.۱ ریشتر
ساعت ۰۵:۵۷ — بزرگی ۳.۳ ریشتر
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/11121" target="_blank">📅 11:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">غضنفری:شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/11120" target="_blank">📅 11:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62701b581.mp4?token=isLMB9sxZVznQHj52Mq71SpDYWzgtYv3KltmhqOgzQAwwnlv2n_2Gq8pi0oM3duu_cqQODiZthwpr9N925pzzfz8fuiyolDKe3oKaTwvp4Xf3UzJ-HXmzbV7TSd1c5HDdwnpHXniD-N41M0LT3IOi4aD5A-doYBWnMA3dFD_66z9qebBknAcUA7pChS_5fRk_b-RSgMreDDOzq9kR7uITiRYZklq89ML7HUQvM8fVqTiPhXQkc5_4k9GbEmp_Z5Gv10HN3AML4pl4MaANftY7WLWHQROlzWiIVjdh0mJirlRp8go6uZUY7-DqKvhbz53i7R1z-pEz47aTKU26RmS3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62701b581.mp4?token=isLMB9sxZVznQHj52Mq71SpDYWzgtYv3KltmhqOgzQAwwnlv2n_2Gq8pi0oM3duu_cqQODiZthwpr9N925pzzfz8fuiyolDKe3oKaTwvp4Xf3UzJ-HXmzbV7TSd1c5HDdwnpHXniD-N41M0LT3IOi4aD5A-doYBWnMA3dFD_66z9qebBknAcUA7pChS_5fRk_b-RSgMreDDOzq9kR7uITiRYZklq89ML7HUQvM8fVqTiPhXQkc5_4k9GbEmp_Z5Gv10HN3AML4pl4MaANftY7WLWHQROlzWiIVjdh0mJirlRp8go6uZUY7-DqKvhbz53i7R1z-pEz47aTKU26RmS3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور 53 جنگنده F-16 آمریکایی در پایگاه شاهزاده سلطان عربستان  هواپیما جاسوسی آواکس هم که دیشب نشون دادم از این پایگاه نظامی بلند شده بود
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/11119" target="_blank">📅 11:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/11118" target="_blank">📅 11:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPSd6ysrg05bPQ6kc_I9mDPVx3rSCh8zhptgXTV25SiAf8_O7wTDlqvdU8AwijEsQToHEv7P3UCe_Eo9E4hucmQzjjmNfGBIoa094BN10FU3SOw4BMS2EETvJVrGq4swwD5XM9BwFBu1P9hNvX7fka8lpXJ9h0iHRt-uxI_uUyaZoapiaj1_p8nchZLQHas17p9JB0lGONARyr_i65fmd1duwq6w7VxObXFFhGBcrn9sybkPF85wFW_FOoGyHxCFHZsEdpJM1P779U0ANrDOE0PJHxEwTZ1an_EEt5IT2-TZFxk9us9CZZ4IwYe_G0wCoV9rlyxi4Y1vFN3mrLOE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس وایرال شده مارک روبیو در هواپیمای ایرفورس وان که همون ست گرمکن مادارو را پوشیده. نکته ای که کسی به آن توجه نکرده کفشهایش است که مارک آدیداس هست.
@withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11116" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpACFgndmeGEpC6OCKdy0muwGveJ8OHwvjlV3Qkh3eieLRzFPNmey9iLoB0EAJK7t2sWlhlm2pA8Amq1w3t_khzP1ylxkzrr-MyOlBb_zFEKcDQpdIJuqh4WYa4lgK0tyXieWUrsGoCUQe5g_5uE0nb3nohf0bx7uHVRGJHsll-7lYL_7oykr6EH2CXbUXsoR9BfRu7SlqwcgqPVkUd75UD6Utua1A1rUpav1psJjvs4fAFETwQVFz9CZLlk-CrG_JA05Lsh7lws9J1vliF3DFNxT2keWpZkpcN9Ci7iy8H1yKJf7Sm5QnEBeEzBM0ugIp2nhRyqb0fHg9bDBgz5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11114" target="_blank">📅 10:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBJEqu47qk50WSTtOx4q67O6Rzy9gN_GvaijCx0sx3cDyZtDAnPJpl97UOlWzjr5DqtETjkEGg8FxeGoeZu3OztoGhUEJ2kkXpWl8zVLq2v2Rt-QTIq-sxi0kOLJMNvahRkKgIEroqHzJashYsmeBenbwe7DqxpLaiEkQZXEgUPvNYEKpZaR-ltWs2pjVE7wEO180T68pfbwh3FKqMvncw45wRI70D1obLQfmJza45s9PibzA3A2738XiTJlmsYwDEWOvUlJRcRXWoS9j3IhglwRntOnd0a96JMUGAO9km1hv71K6EuiT9Dns_CEjIzzt3TNZ72oS1EASuaXV_WwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهد که یک هواپیمای باری جمهوری اسلامی مدل C-130 در پایگاه‌ هوایی نور خان پاکستان پناه گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11112" target="_blank">📅 10:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الجزیره: منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11111" target="_blank">📅 09:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کیهان: اگر مذاکره کنیم جنگ می‌شود؛ مذاکره نکنیم جنگ نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11110" target="_blank">📅 09:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ویزای ۵ ستاره عراق برای جام جهانی رد شد!
آمریکا در تازه‌ترین اقدام خود در آستانه جام‌جهانی ۲۰۲۶ ویزای ۵ بازیکن کلیدی تیم ملی عراق از جمله علی الحمادی (ستاره لوتون تاون)، مهند علی و حیدر عبدالکریم را رد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11109" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ در تروث : شبکه سی‌ان‌بی‌سی به‌اشتباه گزارش داد که جنسن هوانگِ بزرگ از شرکت انویدیا به گردهمایی شگفت‌انگیز بزرگ‌ترین زنان و مردان دنیای تجارت که با افتخار راهی چین هستند دعوت نشده است. در حقیقت، جنسن همین حالا در هواپیمای ریاست‌جمهوری آمریکا حضور دارد و مگر اینکه من از او بخواهم آنجا را ترک کند که بسیار بعید است گزارش سی‌ان‌بی‌سی اشتباه است یا همان‌طور که در سیاست می‌گویند: اخبار جعلی!
مایه افتخار است که جنسن، ایلان ماسک ، تیم کوک، لری فینک، استیون شوارتزمن، کلی اورتبرگ از بوئینگ، برایان سایکس از کارگیل، جین فریزر از سیتی، لری کالپ از جی‌ای ایرواسپیس، دیوید سولومون از گلدمن ساکس، سانجای مهروترا از مایکرون، کریستیانو آمون از کوالکام و بسیاری دیگر، در این سفر به کشور بزرگ چین همراه هستند؛ جایی که من از رئیس‌جمهور شی، رهبری با جایگاهی برجسته و استثنایی، خواهم خواست که چین را «بازتر» کند تا این افراد درخشان بتوانند توانایی‌های خارق‌العاده خود را به کار بگیرند و به جمهوری خلق چین کمک کنند به سطحی حتی بالاتر برسد!
در واقع، قول می‌دهم وقتی تا چند ساعت دیگر کنار هم باشیم، این نخستین درخواست من خواهد بود. هرگز ایده‌ای ندیده یا نشنیده‌ام که برای کشورهای فوق‌العاده ما از این سودمندتر باشد!
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11108" target="_blank">📅 07:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhEODDLs8pq8xXmgzKopEhjGfdoYPnUIteemBzpC5VPanUzZos7zC8X_HAfzgC9hUivmo90a2IGCEFekD9ToxmFZCO68-QkVgfPRnLDqrUnS2LLa10NTSzc4iY0nKj-3F1y7ZzWCldQaiddGDjL6wnAVVoaL-f_UMsT2iIqXB5bGtAseZOh2L5fNE1guaam_OGasIDypwCJdiNlc2sGAwgqi-XHJ9yEtIs7MhLZ68gzhs2LPpU1hjvoyEFpxDxsmAZxzEmkb9-6U4NQ1oy3KYV2QvDl_JKuY_eJeprGnUSm5odGQK9l0kotu5eZ8AqwwocD51iTMZN1aGi9ykq3tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پستی گزاشته که ونزوئلا رو به عنوان ایالت ۵١ ام آمریکا نشون میده
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11107" target="_blank">📅 07:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/11106" target="_blank">📅 01:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجان فدای میهن</strong></div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/11105" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه  بزرگی: ۴.۶ ریشتر  محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس  تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07  عمق زمین‌لرزه: 10 کیلومتر   @withyashar همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11104" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=tPfj6YJocm-mabANp2K-tYQ3UCbwIuqrV7FXst1g8FgJAlJSG7ASjJu1b0rkvIqfvmguLKo0OXPnovwQ4QRszgLBKSYvpccFnJDjiF-2a856qs9TDL9YU7zxr6OvM8z5jdb5OhyyulcqZbg7HP3ir-6iQtGy6gF20_07GWF_SCCrvpkwqbsR4AwiFH6fDPxBojRKMIK4CVkESMi6tl9CAUAUl-88qbahiWnMtJqvM4SwLJgWfwg9xUkMcByN-cQ7zo40_IXP3IFYf86FRGelYlpoODlnKGcqQS_LoXoWpo-0GslV-HY_08j71YN1Gh9rf0jlIaC1WkIDLGExnZkQjCcXfh_Od2ZxN0mzgpzMoQQ4ChQVeRE_HxwXXjHdQ5ZxNJ51tIK5MN980y-iqOHK0zUYhQn1Lgh8fGZbjl1gZJBsdB7jmej97IQyfjv4upEMKCqavjuJD8mk5CfLX3Yjz_lDN0xkVCMMy6MCgYHZhoevp7xx9kRzHFCyAgQNk2Dq-DiGJzXQC-lLoF07MDXfE1P3mn0TzPV1060WeZEuGkLmdN30aTWqKxdoG3MZmMCPCarCf_PchGy3lPZjZecU3a_xPq9vf5XRywoDDR1cdTy_hjJGrtxkw3_Xg6mSWJFvK6uhAE0SUTbriSK2Xm0kYfG8qcypMNAuSfnbdTWhZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=tPfj6YJocm-mabANp2K-tYQ3UCbwIuqrV7FXst1g8FgJAlJSG7ASjJu1b0rkvIqfvmguLKo0OXPnovwQ4QRszgLBKSYvpccFnJDjiF-2a856qs9TDL9YU7zxr6OvM8z5jdb5OhyyulcqZbg7HP3ir-6iQtGy6gF20_07GWF_SCCrvpkwqbsR4AwiFH6fDPxBojRKMIK4CVkESMi6tl9CAUAUl-88qbahiWnMtJqvM4SwLJgWfwg9xUkMcByN-cQ7zo40_IXP3IFYf86FRGelYlpoODlnKGcqQS_LoXoWpo-0GslV-HY_08j71YN1Gh9rf0jlIaC1WkIDLGExnZkQjCcXfh_Od2ZxN0mzgpzMoQQ4ChQVeRE_HxwXXjHdQ5ZxNJ51tIK5MN980y-iqOHK0zUYhQn1Lgh8fGZbjl1gZJBsdB7jmej97IQyfjv4upEMKCqavjuJD8mk5CfLX3Yjz_lDN0xkVCMMy6MCgYHZhoevp7xx9kRzHFCyAgQNk2Dq-DiGJzXQC-lLoF07MDXfE1P3mn0TzPV1060WeZEuGkLmdN30aTWqKxdoG3MZmMCPCarCf_PchGy3lPZjZecU3a_xPq9vf5XRywoDDR1cdTy_hjJGrtxkw3_Xg6mSWJFvK6uhAE0SUTbriSK2Xm0kYfG8qcypMNAuSfnbdTWhZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بلرزونش ، هواپیمای جاسوسی آواکس و زلزله… حجم کم
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/11103" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز: دو تانکر حامل ال‌ان‌جی قطر، به دنبال توافق دوجانبه جداگانه بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11102" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه
بزرگی: ۴.۶ ریشتر
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
عمق زمین‌لرزه: 10 کیلومتر
@withyashar
همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵ کیلومتر در تهران تاکنون ۱۱ حادثه به این سازمان امدادی گزارش شده است.
سخنگوی اورژانس تهران نوشته تاکنون ۷ مصدوم که ۵ نفر آنها سرپایی درمان شده‌اند، در ماموریت‌های امدادگران ثبت شده‌اند اما ممکن است آمار مصدومان بیشتر شود.
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/11101" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/11100" target="_blank">📅 00:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nciKUkw_vs3zyyeU8x3WojP_TSy9IZfiY7BVSRvyXpHw-FTjs327qgb5L0rFg2irVY3yidmZX7H3MjfwtRaoL2X7ryyTndEgno4xLvlPDuUAqjQOnOveR2yz-uUKC4EB-fzDwpREunCFofM5r8ErvFRUgwDR1OxUmBC_WECGOv2422UCPfsdiVGya4rC1QsZ6h0zx5VKqCg0qxDSh_Mq0FeNuTP14C32RIDkkTVHrkeUhLE3MTq20NaPr84H4Qwl2d32iJr3QynGhbYIfLsG-LytCr7v5fInUNgQhKEcwS5jBqX7-0K8_j5HBhWqjxk-1So5RsH0rDCltGSrK8fhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
وقتی رسانه‌های دروغ‌پراکن می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً نوعی خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آنها دارند به دشمن کمک و همراهی می‌کنند!
تنها کاری که این حرف‌ها می‌کند این است که به ایران امید واهی می‌دهد، در حالی که هیچ امیدی نباید وجود داشته باشد. اینها ترسوهای آمریکایی هستند که علیه کشور خودشان طرفداری می‌کنند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت — اکنون تک‌تک آن‌ها در کف دریا قرار دارند. آنها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان نابود شده، تمام فناوری‌شان از بین رفته، «رهبرانشان» دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلال کنند!
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/11099" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت خارجه آمریکا: با چین توافق کرده‌ایم اجازه اعمال عوارض بر عبور کشتی‌ها از تنگه هرمز داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11098" target="_blank">📅 23:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : جابجای‌های غول آسا دو شماره یک «AirForce1» هواپیمای ویژه ریاست جمهوری و «B1 »بمب افکن اسطورهی آمریکا و خبر ویژه از داخل ایران
https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==
کارای اداریش رو انجام بدید تا بعدش بریم برای سوال جوای</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/11097" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BABKmF4Hhfp7HU_ppN4uXrm2Oy0gnB89vramXcMFDjdqQ5nCpsCmQgpcw4lIO4xY7uNik3Rw_fu4p2hA0ZQuXNQZSl3WklR-alCNYbQP1cZd8-YcdpTHLywqrSwqzam5jMJ9cv5Uqdv-QDFW9epDIdG2LFQM7RjKtZHU1eMULZF2ZPbp-2nXWCBjmsX7_cTD3cBwHltLtu9cLoVJdtfiHf3LnfrDS00qDwo_Es_JnskSH5kLX6uMnHD4-yXwUtFHJYOfTT25VUNkDUIJy4oHmD8Id2GtQzLQiOsYMbPdmTK7h-iwwTfmFiahqKfL8FvfjIO4wKMeGZZZHaQgdC5uGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/11096" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11095" target="_blank">📅 22:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=ceVg8hnzuZw_NTvqzYc4hxGztFeF7BocZS6CR1rpEj83gRT5YqhTOsWxK46uMijAs11i3Qucn3etrcmIJxcU6UYCn-Qr5sGKWWI3Yc16G3v99BLyy-u__vKxYhwpOka2p61lvJUzyp_7fxVCRMOtko1QctU1ZERAKCpT-Xi4DmxCR9HbOrBgMGudQStvI8EJFmFhD2Czk9h9KRaIA-b5lMBZepOqrslN_JTVNOnqFoBGkXdUI7nvJZ0YedgaDssxfyC1mhD3_YpcfSS95oQZqhy4p4h3Z-DFm8aKq9nfWyHX14qP_JIvKnpqD-gtUjGYs7fWQFqY4U5_hHT2gj5Spw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=ceVg8hnzuZw_NTvqzYc4hxGztFeF7BocZS6CR1rpEj83gRT5YqhTOsWxK46uMijAs11i3Qucn3etrcmIJxcU6UYCn-Qr5sGKWWI3Yc16G3v99BLyy-u__vKxYhwpOka2p61lvJUzyp_7fxVCRMOtko1QctU1ZERAKCpT-Xi4DmxCR9HbOrBgMGudQStvI8EJFmFhD2Czk9h9KRaIA-b5lMBZepOqrslN_JTVNOnqFoBGkXdUI7nvJZ0YedgaDssxfyC1mhD3_YpcfSS95oQZqhy4p4h3Z-DFm8aKq9nfWyHX14qP_JIvKnpqD-gtUjGYs7fWQFqY4U5_hHT2gj5Spw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سوار ایرفرس وان شد و رفت به سمت چین
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11094" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوباره ترامپ یک خبرنگار دیگرو هم فیتیله پیچ میکنه اعصاب نداره امشب این بازیکن
خبرنگار: تورم الان تو بالاترین سطح خودش توی ۳ سال گذشته هست. آیا سیاست‌های شما کار نمی‌کنن؟
ترامپ: سیاست‌های من به طرز شگفت‌انگیزی کار می‌کنن! اگه به قبل از جنگ برگردین، تورم ۱.۷٪ بود. اگه می‌خوای این دیوانه‌ها سلاح هسته‌ای داشته باشن، پس تو آدم احمقی هستی و من تو رو خیلی خوب می‌شناسم!
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11093" target="_blank">📅 22:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ یک خبرنگار رو به توپ بست
ترامپ: ما یک سالن رقص داریم که هزینه ساختش کمتر از بودجه هست. اینجا ساخته می‌شه. من اندازه‌اش رو دو برابر میکنم چون مشخصه که بهش نیاز داریم.
خبرنگار: هزینه‌ش دو برابر شده
ترامپ: من اندازه‌اش رو دو برابر کردم، آدم احمق! تو آدم باهوشی نیستی
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11092" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11091" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoni Ami</strong></div>
<div class="tg-text">Yashar jan, Chera enghadr faaliat kam shode top Paget? Aghaaaa enghad zahmat mikeshe Like konid</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11090" target="_blank">📅 21:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به سیم آخر زد و برای با ‌چهار هزارم گفت :
من به وضعیت مالی آمریکایی‌ها فکر نمی‌کنم.کلا به هیچ‌کس فکر نمی‌کنم!
فقط به یک چیز فکر می‌کنم: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. همین
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11089" target="_blank">📅 21:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار: فکر می‌کنید شی جین‌پینگ باید اصلاً در موضوع ایران دخالت کند؟ یا می‌تواند به نوعی کمک کند؟
ترامپ: فکر نمی‌کنم ما نیازی به هیچ کمکی درباره ایران داشته باشیم. ما این موضوع را یک‌طور یا به‌هرحال حل خواهیم کرد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری. تمام ماشین جنگی آن‌ها از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11088" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: درباره جنگ ایران گفت‌وگوی طولانی با شی خواهم داشت
ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11087" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">همراه با ترامپ قرار است یک تیم اقتصادی بزرگ از روسای برخی از شرکت‌های بزرگ آمریکا و جهان به چین سفر کنند تا روابط تجاری میان واشنگتن و پکن را تقویت ببخشند،این تجارت‌های کلان اگر موافقت شود برای هردو کشور سودمند‌ است.پیت هگست نیز امروز گفت ترامپ می‌خواهد از…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11086" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOSv-zKYxx7tAjbMjvocVoNHbbt7HCOetusL0Ar1ABTenWJ2dje6eglsRQYHe4I8lgQlm27grMK0aUBm9s1UJMKlDka49qReKNsEffflcuI5LDu9fnEudvg5HJ-FwlJJ7F-bNAXR6-8EWMF4Dua8uVeFpIXC_eER301P9mzHL9-TcXA6hpap8hUusqlf3V2ynZI0Y2cXrbo3GHzjxyIDL9gFP5eseBSt9kwAzciLufRbWRGq5TxtQEIB7kSkJWabiPQviUce_Lq0qQWTV-guab12Tcf-E_ZdlNPrz0hrdpn10pcSin8lhDgHa8IkKzmfMkAOhErC3bFEZTp2bnOEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه با ترامپ قرار است یک تیم اقتصادی بزرگ از روسای برخی از شرکت‌های بزرگ آمریکا و جهان به چین سفر کنند تا روابط تجاری میان واشنگتن و پکن را تقویت ببخشند،این تجارت‌های کلان اگر موافقت شود برای هردو کشور سودمند‌ است.پیت هگست نیز امروز گفت ترامپ می‌خواهد از نفوذ چین در برخی از نقاط جهان(ایران)
برای اهداف مشترک استفاده کند.
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11085" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چهار نیرو سپاه تروریستی توسط کویت دستگیر شدند.
سرهنگ امیرحسین عبدمحمد زارعی (سرهنگ نیروی دریایی)
سرهنگ عبدالصمد یدالله کنواتی (سرهنگ نیروی دریایی)
سرگرد احمد جمشید غلامرضا ذوالفقاری (کاپیتان نیروی دریایی)
ستوان محمدحسین سهراب فروغی راد (ستوان یکم نیروی دریایی)
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/11084" target="_blank">📅 20:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست امنیتی سالانه پولیتیکو:
سیاست مماشات با رژیم جمهوری اسلامی که راهبرد بسیاری از دولت‌ها بود، شکست خورده.
با یک جانور زخمی روبه‌رو هستیم، این فرصتیه که نباید از دست بره
بلکه باید کار رو یک‌بار برای همیشه تموم کرد؛ موضوعی که نه‌تنها میلیون‌ها ایرانی، بلکه خیلی از کشورهای منطقه هم انتظارشو دارن
مردم به‌اندازه کافی هوشمند هستن که تفاوت بین حمله به یک ملت و حمله به یک رژیم رو تشخیص بدن و اون کارزار، حمله‌ای علیه ملت ایران نبود، بلکه علیه رژیم بود.
ما فقط زمانی می‌تونیم مردم رو به بازگشت به خیابان‌ها فرا بخونیم که اونا از سطحی از برابری در توان مقابله برخوردار باشن.
نه زمانی که رژیم بتونه اوباش و نیروهای سرکوبگرشو برای کشتن مردم در خیابان‌ها اعزام کنن.
اما برای رسیدن به اون نقطه، باید پیام روشنی وجود داشته باشه. باید راهبردی شفاف برای پایان دادن به این رژیم وجود داشته باشه.
فراخوانی روشن برای قیام مردم، و همچنین پیامی برای نیروهای نظامی و امنیتی از حکومت جدا بشن و به مردم بپیوندن
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11083" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس جلسه: آقای وزیر، اجازه بدهید به سؤال سناتور کونز پاسخ دهید. سؤال ساده‌ای است: چطور قرار است تنگه را باز کنیم؟ در جلسات محرمانه، افرادی از تیم شما به ما گفته‌اند که راه‌حل نظامی برای بازگشایی تنگه وجود ندارد و در نهایت این یک تصمیم سیاسی از سوی ایران خواهد بود. شما هم ظاهراً همین را می‌گویید؛ اینکه فشار اقتصادی، تهران را مجبور به باز کردن تنگه می‌کند.
پس آیا تأیید می‌کنید که راه‌حل نهایی دیپلماتیک و اقتصادی است، نه نظامی؟»
وزیر جنگ : من می‌گویم قطعاً ابزارهای نظامی برای باز کردن تنگه وجود دارد؛ چه از طریق اهداف زمینی، چه توان دریایی ما و چه محاصرهٔ دریایی.»
رئیس جلسه:
اگر این درست است، چرا تا حالا انجامش نداده‌اید؟»
وزیر جنگ:چون راه‌حل بلندمدت و ترجیحی این است که توافقی حاصل شود که ایران تنگه را باز کند و دست از دزدی دریایی بردارد. این فقط کشتی‌های آمریکا نیستند که متوقف شده‌اند؛ کشتی‌های سراسر جهان درگیرند و این فشار بیشتری بر دیگر کشورها وارد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11082" target="_blank">📅 20:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سناتور : من هیچ‌وقت از رئیس‌جمهور نشنیدم که بگوید هدفش تغییر رژیم در ایران است یا می‌خواهد همهٔ مواد شکافت‌پذیر آن‌ها را تصاحب کند. چیزی که من شنیدم این بود که هدف ما فلج کردن توان آن‌ها برای باج‌گیری از جهان است.حالا شاید دوستان دموکرات من بخواهند بگویند ما شکست خورده‌ایم. ولی من نمی‌فهمم چطور شکست خورده‌ایم. آیا تنگه بسته شده؟ بله. اما اگر این محاصره ادامه پیدا کند و هیچ‌چیز وارد یا خارج نشود، در نهایت مجبور می‌شوند چاه‌های نفتشان را تعطیل کنند. نیمی از میادین نفتی‌شان وابسته به فشار طبیعی است؛ اگر خاموش شوند، دوباره راه‌اندازی‌شان بسیار سخت خواهد بود. چیزی را اشتباه متوجه شده‌ام؟»
وزیر جنگ:
نه، به همین دلیل است که رئیس‌جمهور می‌گوید همهٔ کارت‌ها دست ماست. و ما بهترین معامله‌گر دنیا را داریم که می‌تواند بهترین توافق را برای آمریکا رقم بزند. و اگر لازم باشد دوباره وارد عمل نظامی شویم، وزارت جنگ هم آماده است
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11081" target="_blank">📅 20:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سناتور کونز:
حالا دربارهٔ ایران امروز صحبت کنیم. آیا موافقید که ایران چه در بخش دولتی و چه خصوصی الان عملاً با تف و چسب نواری سرِ پا نگه داشته شده؟
وزیر جنگ پیت هگست:
اصطلاح “تف و چسب نواری” اصطلاح دکترین نظامی نیست، سناتور، ولی در کل با این توصیف موافقم
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/11080" target="_blank">📅 20:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سناتور کونز : دستگاه اطلاعاتی ما مدتی پیش کشف کرد که رژیم ایران یک طرح جدید برای برنامهٔ تسلیحات هسته‌ای‌اش یک نقشهٔ بازی تازه طراحی کرده بود.
طرحشان این بود که تولید موشک‌های بالستیک، موشک‌های کروز و پهپادها را به‌شدت افزایش دهند و یک انبار عظیم از موشک و پهپاد بسازند. بعد از آن به آمریکا، اسرائیل و بقیهٔ دنیا بگویند: اگر دوباره مثل ژوئن(جنگ ۱۲ روزه) ما را بمباران کنید، برنامهٔ تسلیحات هسته‌ای را از سر می‌گیریم و خاورمیانه را نابود خواهیم کرد؛ و ضمناً موشک‌های ما حالا می‌توانند به برلین، لندن و پاریس برسند.
آیا برداشت من درست است که یکی از دلایل اصلی حملهٔ ما به ایران همین بود؟»
وزیر جنگ پیت هگست :
«فکر می‌کنم این موضوع را خیلی خوب بیان کردید، سناتور. آن‌ها تلاش می‌کردند با تکیه بر زرادخانهٔ متعارف خود، جهان را برای رسیدن به سلاح هسته‌ای باج‌گیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11079" target="_blank">📅 20:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سازمان اطلاعات سپاه اعلام کرد که پنج شبکه قاچاق سلاح مرتبط با اسرائیل را خنثی کرده است.
۲۰ فرد مرتبط با آنچه آن را شبکه‌های سازمان‌یافته «بی‌امنی» مرتبط با «گروه‌های تروریستی و قاچاقچیان سلاح» توصیف کرد، شناسایی و دستگیر شدند؛ این اقدام پس از اقدامات اطلاعاتی و عملیاتی نظارت بر محموله‌های غیرمجاز سلاح انجام شد.
بیش از ۵۰ سلاح گرم، ۷۰ کیلوگرم مواد منفجره، حدود ۲۰۰۰ فشنگ و مهمات اضافی در جریان این عملیات توقیف شدند
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11078" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هدف جنگ از زبان روبیو: بازگشت به زمان قبل از جنگ
مارکو روبیو گفت: «ترجیح ما این است که تنگه هرمز باز باشد، به همان شکلی که قرار است باز باشد و به همان شکلی برگردد که قبلاً بود.»
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11077" target="_blank">📅 19:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد. @withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11076" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وعده سر خرمن پزشکیان درباره اینترنت :
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11075" target="_blank">📅 18:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">️عراقچی: هر کسی که فکر می‌کند ایران به دونالد ترامپ توافقی می‌دهد که می‌تواند به آن ببالد، در خیال‌پردازی زندگی می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11074" target="_blank">📅 18:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو
: پاکستان از ربات‌هایی استفاده می‌کند که خود را آمریکایی جا می‌زنند تا شبکه‌های اجتماعی را علیه اسرائیل دستکاری کنند
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11073" target="_blank">📅 18:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به گزارش ایرنا، ایران و عمان اوایل امروز یک نشست فنی و حقوقی با محوریت تنگه هرمز و عبور ایمن کشتی‌ها در مسقط برگزار کردند.
از سوی طرف ایرانی توسط عباس باقرپور، مدیرکل امور حقوق بین‌الملل وزارت امور خارجه، به همراه نمایندگانی از چندین سازمان دولتی هدایت شد.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11072" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا
نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11071" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با شما : به کارمندان دادگستری گفتن فردا نیایین تعطیله ،احتمال شروع جنگ رو دادن
یاشار : تایید میکنید ؟ اگه خبری دارید بفرستید
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11070" target="_blank">📅 17:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عبور نفتکش قطری از تنگه هرمز
در حالی که روز گذشته اعلام شده بود نفتکش قطری MIHZEM  توسط ایران از تنگه هرمز برگردانده شده است. این نفتکش دقایقی پیش موقعیت خود را در دریای عمان ثبت کرده و از مسیر تعیین شده ایران از تنگه هرمز عبور کرده است.
دقایقی پیش بلومبرگ هم خبر عبور دومین نفتکش قطری که حامل گاز طبیعی قطر است از مسیر  تعیین شده ایران را تأیید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11069" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: من رابطه خیلی خوبی با بی‌بی نتانیاهو دارم. ما واقعاً مثل دو شریک واقعی کنار هم بودیم؛ اگه ما دوتا نبودیم، اسرائیلی هم وجود نداشت؛ مخصوصاً بدون من قطعاً چنین چیزی ممکن نبود.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11068" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
چین قوی است، اما ما از چین قوی‌تر هستیم. ما از هر کشور دیگری از نظر نظامی قوی‌تر هستیم.
شما این را در ونزوئلا دیدید. این کار برای اکثر کشورهای دیگر سخت بود. ما آن را در یک روز انجام دادیم، و حالا به آن نگاه کنید.
به ایران نگاه کنید... آنها همه چیز بزرگی داشتند، و حالا همه چیزشان رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11067" target="_blank">📅 17:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itgaT6KuSjvMWEdxoHOPw19eYdsZyXDEnhydFn746DSFLfiqoMnRt9A6Z4qTwMh9s6jPfOh9SnmH8eMeirVZN25QxrCDG3X_CePpo9LXUKSmCN-ELkyKmKhw25zuvEYsbuFZJQBTSIa5dFb_FuxvhP_x1xxy3eHLbOHJpLT9mv9bjc72meEmR_9gWFRA04Y9i4xXxbrTp55gIBc-ChjAln-FbJH0Hp4mVua56bpLMcq1Cyy-weSjXL5LhogZg-I_3Nl1ISKHHbwmv3k240HIZRU9lpkYKKgwlQZ5F78cP4CAnyUQL6lUccr3kb60eeVIpOklsV5B76grf4cP9Fp14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدعباس عراقچی وزیر امور خارجه برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
😅
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11066" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: آمریکا در تماس مستقیم با مقامات ایرانی است و عجله ای برای رسیدن به توافق نداریم
@withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11065" target="_blank">📅 17:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر جنگ آمریکا: ما مهمات و قابلیت‌های کافی برای تضمین دستیابی به آنچه می‌خواهیم در ایران به دست آوریم، داریم.
وزارت جنگ در آمادگی کامل است و در صورت لزوم آماده اقدام علیه ایران است
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11064" target="_blank">📅 17:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ : انتظار داریم اقتصاد ایران تحت فشار ناشی از محاصره بنادرش فرو بپاشد.
مناقشه با ایران بدون نیاز به عجله کردن، حل و فصل خواهد شد و ایران با انزوایی مواجه است که آن را از منابع درآمدش محروم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11063" target="_blank">📅 16:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ در مصاحبه‌ای با برنامه‌‌ای از شبکه‌ی WABC در پاسخ به این سوال که آیا معتقد است می‌توان از غنی‌سازی اورانیوم و توسعه‌ی بمب توسط ایران جلوگیری کرد، گفت:
«صد در صد آنها متوقف خواهند شد.»
ترامپ همچنین مدعی شد که در طول مذاکرات مستقیماً با مقامات ایرانی در ارتباط بوده است.
ترامپ گفت: «من با آنها تعامل دارم. و آنها گفتند که ما قرار است گرد و غبار را به دست آوریم. من آن را گرد و غبار هسته‌ای می‌نامم زیرا نام مناسب‌تری است و ما قرار است آن را به دست آوریم.»
ترامپ همچنین مدعی شد که ایالات متحده نیازی به حرکت سریع به سمت توافق ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11062" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر جنگ آمریکا پیت هگسث درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11061" target="_blank">📅 16:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سنتکام
:
ناو هواپیمابر آبراهام لینکلن به عملیات خود در دریای عرب ادامه می‌دهد و تحریم‌ها علیه ایران را اجرا می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11060" target="_blank">📅 16:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شکایت ایران از آمریکا به دیوان داوری لاهه
این دادخواست بر اساس مفاد بیانیه‌های۱۹۸۱ الجزایر و به دلیل نقض تعهدات بین‌المللی آمریکا در جنگ ۱۲ روزه علیه ایران، اسفندماه سال ۱۴۰۴ در دیوان داوری دعاوی ایران و ایالات متحده ثبت شده است.
جمهوری اسلامی ایران در دادخواست خود که تحت عنوان پرونده الف-34 در دیوان داوری به ثبت رسیده است، با استناد به بند اول بیانیه الجزایر، ضمن تبیین و تشریح مصادیق نقض تعهد آمریکا در جریان جنگ تحمیلی ۱۲ روزه و همچنین اعمال تحریم‌های اقتصادی و تهدید توسل به زور، از دیوان درخواست نموده است ایالات متحده آمریکا را به نقض بند اول بیانیه محکوم نماید و آن دولت را ملزم نماید فوراً به مداخلات مستقیم و غیر مستقیم خود در امور داخلی ایران پایان دهد؛ و ضمن ارائه تضمین عدم تکرار اعمال متخلفانه مزبور، خسارات وارده به ایران را نیز به طور کامل جبران نماید.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11059" target="_blank">📅 16:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ در تروث :هیچ جمهوری‌خواهی تاکنون درباره کوبا با من صحبت نکرده است، کشوری شکست‌خورده که فقط در یک جهت حرکت می‌کند به سمت پایین
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11058" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwUeW0xanw6YIP-f2Fv8It9DsrLyuKAjZ_lxuaG5suJHgqko9Wr69w7YR5RBx1HOAO3cjBlMKBe2H02HrRCIXuqjr_XH4YOH43OlIPbYVj7F0azI65Bstbb5Y_80F2AhWhz7ojVtC2_mLuq_EX4lHepbL3_mC5ctzZU8FhphEZ_4ekyriB8mtQKgFLVFdrCpQo5dKfWmhdczQ76pvF6hka4CHcIOym-cf_6htAaEpYMPvUOiYGdFvI7k_BRXdwSw-FWIflRx-1VnfHFdvBxYr2g1Kofe6X_XYrdZsYwFu26kDdvW2gYMGXMvl8Ax1d_fKpC0mWKa_ZlZ9j-BQvEicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ قایق‌های تندرو
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11057" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoVQkSWKDmkN52l-S0NrnKoDf2A5uCJsKUS4-8RNgmgL2a1koQlNzJNxTjU47MFM93heIiYswtijrOLxa009k9ry4f4bOxPEf_UrzFbowdphJqLurm7LJaEaLK0s48bL9cDjNPHvH28kh2U0t5H5kQwgtt9Qzt6KrW_k4sJsFohp7iQiWRb-EDWCSZDxCFXPPNYeAWmu6iEK-2prmbgEtmR0VQ1kdEawDH6SkqOoMBd5MxT6VRfmTpcisJ_RFdpKjwaH_PId6yVPj-XEuiXdSX-obsVmiCmwlOhWZkLm3bhUPeJe8NHR6HgCmipWtLd0ILXV79eJgo6x7URC8VUuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : دموکرات ها عاشق فاضلابن
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11056" target="_blank">📅 15:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ در تروث  لیزرها: بوم بوم… رفت هوا!!! @withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11055" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در پست جدید تروث، ترامپ طول جنگ‌های بزرگ آمریکا را مقایسه کرده:  * جنگ افغانستان: ۵۴۳ هفته * جنگ عراق: ۴۵۷ هفته * جنگ ویتنام: ۴۳۹ هفته * جنگ جهانی دوم: ۱۹۶ هفته *  گشت و گذار در ایران
😂
: ۶ هفته @withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11054" target="_blank">📅 15:27 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
