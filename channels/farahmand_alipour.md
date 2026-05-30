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
<img src="https://cdn4.telesco.pe/file/AXlvdrAnLa_Bmc-Mz2IUu5H4FAG_D6rgD4SHpQPszXh6uYBQrLQG2LZmWouIVEDdkZj_t4-_78HbiBaeZbSUH4MAuEilOAQHsvYyZ8kZtLDbshw_BLfDMpaeAuRU-VXoFIeC7pEbKSSc9ab6fIAwfj0_FQNO1yKkfl_tu3kguyTYqWZm4PSlcX3NOOSLQGLszxspklEMvI0SoIg4tNeuK1ir98lgf2fK7iC1y0gjituSoVzbHnZq-zd-zRVJaIAfitbL6Dl0C8YksHTSRXCPiMFEYAQUCcSb-YFw3e--1maLCgSd1bDv6QFPaZZ6Mm4_QPT05QNCpz1V--VCpGTr-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 08:36:32</div>
<hr>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyvzrqol1jfG0LMkc_tnkyeD56cY09VswK7gySi62alPzQy3_i4yheTZm5oCYTIKcRGtwIWoOYAVYjIDMuZ7VAqAQO8ipx2IOEAeGWeJCugmip2XAQNKt2IgHbg8hOcM8GZQPhKtzzHQ2gC6nud10zHBOYOgI6xRIREPDKUWaWSMLXZ6O-syZ83M27E_sDNmgjFnyVYLb3TENvu2g3qqB9ALdxAr-bWu-Y-Ke8_1mMaXtLxvEPg8pYnvQK3knmv79KADMQ3jQoaK9Y8ApWMLdAvfklmeb0FOj9VoqQr5ObxjehAzHZiTviNKdiLh2fLPNnRrQAgN2oLk94QaCcMCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX46z-Zl_bUQ96FCDfakt8VmPjUTxZc-gqaMVdTXF0XYwicLx-KBp9-MAAV_o5hBRB0Cm2-WxyNM3OcWANCZYCvpWNHGuTRMy8abB_JMQ54EVIG68YHt-BXD09Sw1c_ZQbFc490EtJaKwQ8okJPOITPdQKbalQDda_DMof-UTSZ-H5w9VHSBjRHfhknn-pBg3XxMlw26nUTWhoI852z5DzRCgeBukEDG-kCpuqxnHVrN0qaV63JNveb1P_eS993dn1ZfDoc_FAcoE1y4zCe4khOXxVip4VAHRK4AGiT5FaiJ7lbt4QxqmJMn0zZFL5RE0RM3cFQzCAsNKzuZDXI-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6FfAkHOJVdA2HJC1hXZ97SoBO6uRKXbfY2UzvFWnlMInEJ5h4wnwcqeIZQSGhoM_FM4X2fK9dgAnwGxwrcFgmx6T-bynjERrc3c5YjPeqeRMIpJyUNHBjIRuVBsJNOkSHGMgKOQXBGZP6IlTdxFO5W3n4mroiWXVhMniu3La79ldfTgML9Xf-SShv2ZSXALjvuTBpiwoNwO6GvZaGyML_6Ztb9-6Fpd4dkWpaJ3xg7DEGKgdZceFOw1YPQ4DLQHDFFDhJUdbNAR-IlRnwZg7CRU47CBszHE35kU4favY2Q7sRTdYN-z0WaxYzPm0NvHkAiwJch4kMbf-H4Qq74LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E97e-ybw3Pw5Xg235io7lCb1LKIB-_C7LMim_K7iGiPKtygGnOYX97zUMIm4_DoeWsLiCGYcV5Jl0zruXHFnzlyOZvFkfjiOUtxwljCtVAKxUibqNnhIyKRo_ExBKDpIF4w7S_VPdafshn01e6Xx90GtCCVLcg-uzxToMUruPZls3g25YKCX9yW9YbRTsK21s9qz6jS8biEI5wJbpMNPmzizgk4o6LNtnyGU6mOcDOpAP-7E2FiX45HgnbO-9WSc9JRtNm7cQUXBX84iys3b-o2bMXaP8JDv1qc0txs1-49sNlXxvG67aNkwKeehuFTpW2hU5PStjuYqr3aYW7Uc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz20MFN_mcpc3Y152zaxEj2ybeGeave3YdTTTO4hGKLki2_QGE0o6kmot9aHzQ8Qw8JT8jvCK30XA_XgQXAqPp9g8LI121X2Mzu9VX3lf5jeEqYjI--pdQkCydcveAoUc0mN0uNdHQkggJ9BApXUnFvL53CHdgQ7vjGMw9k3fKZl9QmBNp78e7gqX2EQioNzSnycs7CvsNK0o2w1CrNdbkZFIyZZYv6q1M6zwv6Y0ec6AkSM1G6kmvmW_RHwnhaOaexxTofCi8O6Pmn-bh6Wygq2uj2tBBxT8s8quOHdGKPmESVaWP6w3ocjIGHMnBmUvPl_Gql-z48hVtgUU1UsQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJWZjkkt8Ja_Q_tVAl1qUhDS-Vg_HFuotmZFcdypKGNJND8dT1FV-RkY-oC8zMT9cebb6CB-OmLwD1RSHLlng7jG3ABcIRbWXCtSDBiphpd1UuW2Agl_m5ZWIOvhMQ_pOmK6Z_R2Ad_RH0ydtXiSq4ckxmrsiFgEJn1MYoXi0xrVIRL2JrLM17kDSgrB4PwaTCBwKP28eEi2JHU-adfc2w-QUB6SfliYHgvt5AbTt_KjG0-MuDBMlwWQEw4e3orVV_MCFzgzNjwfXHIK_n6REprdFr6F0R614vnZt50PWxxYOO1BDD9-Wc7k22Y869qDogeCMxv1s3fHhOY9p54u3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWOuI-5iTFC5hZ4CN0HX6UAg6Vc41eGg9VDE0WsDxzMBHa_-QEOi3XYHf2bZG4KLCPG6vaJUNoBQyRfClIU7Q3SvDTLAKrCY4eu5f4kU_MJJ9NYHMU8meVxYE-y4UACri5QjeTt-AEd5pi6nGGvFLb0N3qd_aDI9emEySbrC7LT4zbOAUhstodqKzqPABp_ITMrdk-eZjl2w9PVSde3UW9yboD3v_bUuAjmTYRq2XRX2gCiJGJE98c2X9yJo-FF2FsUibTJMPznIwpJymyWe-IclXIIyw3noRm9OrTx5z9lvC-SzEJgwQ6Cju4t1Yx4u6CEkF5yDzjFvPRW8wAqN4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vPSguEY9_VSGpVzOwPZWDS_AykLAVPdFRHab8drA4cBje8z4gZm7yLmdsjg4lR8zOFsvpqGvjlkpqZ2-_nIp81p9Gr7MrZFrHSrRMHA4HD-xzttwJ2EApcpTccDYECroF3b9bI2Z5RPsRHqD9BHnq-BJ6Nbe3fTIPLaPR4cUlJkYlFgAzwsCQCIYtizcUDC5oRAEnnAy9yeWUxqQWPoIknAY6fGXMU5XqGn2pQpb2IQXrG52vbvwCyrxIFZhlnk-uEq-wFMjYoQaItXrihoOD_neRs9q-LOSYc674KzbQCTKjSy7rMMn_346Or63KTSDwxXbMID3ckmXeioEeTYfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vPSguEY9_VSGpVzOwPZWDS_AykLAVPdFRHab8drA4cBje8z4gZm7yLmdsjg4lR8zOFsvpqGvjlkpqZ2-_nIp81p9Gr7MrZFrHSrRMHA4HD-xzttwJ2EApcpTccDYECroF3b9bI2Z5RPsRHqD9BHnq-BJ6Nbe3fTIPLaPR4cUlJkYlFgAzwsCQCIYtizcUDC5oRAEnnAy9yeWUxqQWPoIknAY6fGXMU5XqGn2pQpb2IQXrG52vbvwCyrxIFZhlnk-uEq-wFMjYoQaItXrihoOD_neRs9q-LOSYc674KzbQCTKjSy7rMMn_346Or63KTSDwxXbMID3ckmXeioEeTYfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Fumcn5fV3NhWg-QNtKh9ELKCjXObyqoL7dLXXPwsXtAxp-mDNNFhZcdHcTZUN6iTFtwV78iKCELnYdLrtNjepeuuCwZe-m1yvSBT82ufQdtYYOiF-utAsKgYiAbTHEqivXAS7jZIqc_lizlrxMqN5TkzXUnG8GDAxoyrYKx4vMpyF7ILwINuA5Ct1O8cvfOV58sIFUVGCuolDH6cTDqy8ZZDN5cXAACD4b5V2xbP2yGYANbpOKArjIbxlsQWDL8pyjZky5omA8yj3E5rwMMF6F7uW5dFxgpw9I5800YiS2kxKVVcPaShSDDuG8snjPs8qVa5_T5Ba8eymi5NKXCngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Fumcn5fV3NhWg-QNtKh9ELKCjXObyqoL7dLXXPwsXtAxp-mDNNFhZcdHcTZUN6iTFtwV78iKCELnYdLrtNjepeuuCwZe-m1yvSBT82ufQdtYYOiF-utAsKgYiAbTHEqivXAS7jZIqc_lizlrxMqN5TkzXUnG8GDAxoyrYKx4vMpyF7ILwINuA5Ct1O8cvfOV58sIFUVGCuolDH6cTDqy8ZZDN5cXAACD4b5V2xbP2yGYANbpOKArjIbxlsQWDL8pyjZky5omA8yj3E5rwMMF6F7uW5dFxgpw9I5800YiS2kxKVVcPaShSDDuG8snjPs8qVa5_T5Ba8eymi5NKXCngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQV5pYZ-_Bmqtoi3VKXa038p-Qnw2GOa1Z1qT3vR5Sy0uJw8bvtbScOUkXP5e3FxuDM54moQBWxvA5Xvs9W0E92sjp8PLziazsO17PdedTFVyIDe2OsnH-Ckm3cMAbSOLXVtUv7aDGNtLnSCmjh_8SVPwuZb2DkWJNzvG1ntc7mRbrmqgDh5MMTw58ChHHFO7XNeY1pZyXJOfa8quwzeGzCy9RNTrFI4_y7nzI1SaLwiB07qz3Mjv-3lMgOUJvncsL_X6Mod7E64mevZvfV3oBDf2ERswAe2JxefrdNDf_GpC4_wzBmld5SXhmS-uOApJNmVrwT8TwFMeAtd0piepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dz3-P688I73tsQqIpX8he-oFARwsxYmGYUmbqExeyy7X-K4eRrolVm6HnHUMzfqripH8RDeWJqG2g--TMO498oKZ2nkOQu2pYv60WbZvBtJFW-H0ZjrMRXetJaKeAdvaDUFLQUBcFJ1lzlLBYEH1Cg-tWS2U6wF6SXT5eqVLxYJgDmIMJNozCHiAeps5qr4Ywf_3sMvhIMYSBYob8B83WIK36crGGOIj5dYP53-Q-2kAxlvtTBWOrLZUyAQrwDHx85XqtO49u0ryi-6LChWM1vwm-NCJtlSOu8mGBChwU6aQ4MCxblPP8VnTMjJ9V8-3WymaTaZPJdYVhAdDNpkJBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=CcPq70_klJv4o6OJND2XOs5kN1lRxb_6VkxHN34ZrGUH8wvrOWC0CE5QA7rEJB8FXuVR2Qv1KIIqo9bkQpN8mLNdt1uvXVfEFYUexWbdqV4ILyqW_ooAZBlRnylle84aNgPU14j3gxzFHAlkZvE23q1G79hPVbuJZmpiaIJLVlaPXTTrGrg_M5PsycC9lhaI9gKSrzwqBkfjMqlYLVCJCwuOCF72aZFcJFUCa8gozKvhQkHnrh7Fz9vf3ygaO9lHbN8X0djQw56hMKeixvTSA1YDI4_OSWH0B92XUZ_XM2MTtavs-czhRE8YL2CeZ7SPJn4cFpuKCDM-Ak3hnboHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=CcPq70_klJv4o6OJND2XOs5kN1lRxb_6VkxHN34ZrGUH8wvrOWC0CE5QA7rEJB8FXuVR2Qv1KIIqo9bkQpN8mLNdt1uvXVfEFYUexWbdqV4ILyqW_ooAZBlRnylle84aNgPU14j3gxzFHAlkZvE23q1G79hPVbuJZmpiaIJLVlaPXTTrGrg_M5PsycC9lhaI9gKSrzwqBkfjMqlYLVCJCwuOCF72aZFcJFUCa8gozKvhQkHnrh7Fz9vf3ygaO9lHbN8X0djQw56hMKeixvTSA1YDI4_OSWH0B92XUZ_XM2MTtavs-czhRE8YL2CeZ7SPJn4cFpuKCDM-Ak3hnboHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6tfQKPhuKL7CdW31KComUIyBaa7bJ8OwiMMfQqAZbcyhq6cCsH5TrSZ0Sgt8lGa3iS0jBR03XbzCHz5PavNHdLIL25nYQMLKIoTfFD7-VOxvxzc7t3RS2ogkJZIg3OVuc43VZluIBIjDn9Tsn8E7RuifBlIrYoY_tv1PqHSWEU_RemvhLV_2VDsfYs_Hq7KbMXMovpeZDnfXT_rDndSKS7PQexYHSZ5UrIDkaeiPAoRdmumOgjDx7h4vvzrz0XJZsbqWxPpBQhuGLKiAUZeLQ2Z0ir2VKf1fBwSDVIi0-wUrbiYhENqwBySZu-04y9oZJqPesSgIppFZoUGmMN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=jPydOvkLkupz_0isLZMHNpKAKvxCzHlz0nTtWN6tpBe9-CKP8g7gIXNwXK6-OrWhGBwJ9L6a9JooNyZNiw1_26oNCgYJIE9DNCMjrHTCG_sd948q8ARx74bRd0n0USJyFIffw0R2Z7x_pfG2Eya3srOHSkBU1juCNMZnsboEBvzxmfYviku-ZhuLBXeREmOx0QR9cMgPJ_yLlcURAq5NOoGy3bf2sqa3tFZIGIMM0efwZg_PkOXyLx0Id0jmy9oK3hpBHkid9BAHU2GKhZv21S-2Vwe4fvU8WsLvZZy0G6vREiW1_lge9fcySBdnEtc9deZrzGd5n4T7rL3fhooUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=jPydOvkLkupz_0isLZMHNpKAKvxCzHlz0nTtWN6tpBe9-CKP8g7gIXNwXK6-OrWhGBwJ9L6a9JooNyZNiw1_26oNCgYJIE9DNCMjrHTCG_sd948q8ARx74bRd0n0USJyFIffw0R2Z7x_pfG2Eya3srOHSkBU1juCNMZnsboEBvzxmfYviku-ZhuLBXeREmOx0QR9cMgPJ_yLlcURAq5NOoGy3bf2sqa3tFZIGIMM0efwZg_PkOXyLx0Id0jmy9oK3hpBHkid9BAHU2GKhZv21S-2Vwe4fvU8WsLvZZy0G6vREiW1_lge9fcySBdnEtc9deZrzGd5n4T7rL3fhooUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=GWV_WWhiY0rITqomdnygpw0uQhN2oWPku46O1EpmeS7Hqnce1w6vbYjrSEdtWxGQLxAOtYiyDwG22E8wtjg36XlfvLvcN1tOJyXqvVzYntJoi1P1eNIfVQ0-13yUdUvACCjaOhs22wa3iV-WtrbJ4Gqiflw8OqFNV09pyNM0hMeq3etjeeJZ6xLRtV6Goj1MzxLegCjbT5bjrSanUTsPBi_pyEhcp_sqslY9TkIr9-l2ggKNHjHn-jzbkBVDXHbk_b0-l_Py0bc4zn6ZcBfH4pZZbzSMh5SGD_Ju7372E3Q_Et4pGLVbc2v0US7rsf2-IYxwvv9UoBuc2seCZk-yow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=GWV_WWhiY0rITqomdnygpw0uQhN2oWPku46O1EpmeS7Hqnce1w6vbYjrSEdtWxGQLxAOtYiyDwG22E8wtjg36XlfvLvcN1tOJyXqvVzYntJoi1P1eNIfVQ0-13yUdUvACCjaOhs22wa3iV-WtrbJ4Gqiflw8OqFNV09pyNM0hMeq3etjeeJZ6xLRtV6Goj1MzxLegCjbT5bjrSanUTsPBi_pyEhcp_sqslY9TkIr9-l2ggKNHjHn-jzbkBVDXHbk_b0-l_Py0bc4zn6ZcBfH4pZZbzSMh5SGD_Ju7372E3Q_Et4pGLVbc2v0US7rsf2-IYxwvv9UoBuc2seCZk-yow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=G4D3TnvvxHzYQsu-7DU4sWxNit0Rm5c883NP8R3LZwm40AHwHlrqJOIL5ccr41icPBPu5cPirgQ4mreVibAY8HZGwqGXiyf4fvzeUgL3F1zbmHJ8tFwsZbkcjCUk7suh74cGd-Cx7AX5PzHNcmjJ64TTkjWPKJXpXOvqsNKELTj4d1hB0tTGZEfS2sKaYBNniBrqA66djx6sobLyiB-MVECiQry_sCaIoLyqBEEfsUnsjG2NobW7n_ZSL67KQTQSoQORr8qWEDYCrq1Jp7Y7pPkh4htmuD5Vmoa7EZu1MXiPbucOHCU1FVYas53vfh8ME3EK7GQcii2BD2uU2sygkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=G4D3TnvvxHzYQsu-7DU4sWxNit0Rm5c883NP8R3LZwm40AHwHlrqJOIL5ccr41icPBPu5cPirgQ4mreVibAY8HZGwqGXiyf4fvzeUgL3F1zbmHJ8tFwsZbkcjCUk7suh74cGd-Cx7AX5PzHNcmjJ64TTkjWPKJXpXOvqsNKELTj4d1hB0tTGZEfS2sKaYBNniBrqA66djx6sobLyiB-MVECiQry_sCaIoLyqBEEfsUnsjG2NobW7n_ZSL67KQTQSoQORr8qWEDYCrq1Jp7Y7pPkh4htmuD5Vmoa7EZu1MXiPbucOHCU1FVYas53vfh8ME3EK7GQcii2BD2uU2sygkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=U9K3PJqs4OiMvEfiWlLheGKONnjpRRo3BY_tAC1uU7qXyJpWLLS3v64v9zzEyhD9lOT1tOQuapUHaq4aNb_GFsr_uaHGYBPYxya7XimMd93BoPgbXc0Kw4pDomEGnjpyjVAkjK47o6rV0eILDajYszEyaUDreRsgxFh6wHY6mIhhZiZAPs9ZB_86founTqPykMQirXJXrwOVhN0QpjIdN6nC6GvyvC5Y9m47IQ6Bs-11b--GjKfrUcwYkttpnjBmVAEvhe8v4FaGmiUMwWvQwOjugJhnV_x0XKCzwmHYoP8c3b8B_jo14n_MwkGwDwC94ZjiVzHNxoh3jR1qkZ_b6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=U9K3PJqs4OiMvEfiWlLheGKONnjpRRo3BY_tAC1uU7qXyJpWLLS3v64v9zzEyhD9lOT1tOQuapUHaq4aNb_GFsr_uaHGYBPYxya7XimMd93BoPgbXc0Kw4pDomEGnjpyjVAkjK47o6rV0eILDajYszEyaUDreRsgxFh6wHY6mIhhZiZAPs9ZB_86founTqPykMQirXJXrwOVhN0QpjIdN6nC6GvyvC5Y9m47IQ6Bs-11b--GjKfrUcwYkttpnjBmVAEvhe8v4FaGmiUMwWvQwOjugJhnV_x0XKCzwmHYoP8c3b8B_jo14n_MwkGwDwC94ZjiVzHNxoh3jR1qkZ_b6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=v3yklp-vUU-hNDsO79UfuntZg5UWijI9lGBuFIF5k0Dnwo6Nq0_eUHyRyewZHk-zyvk4tNhk-LJml6xEsF8-BH48dauhnFvP7KkWN2eX6GEEGfNP126d4XFiDJqkiOdiszu3VQly--FNxgeMekA3wtnTbgSo3De1bfKhGRSO1RA5HfYC3WNOP7fvoIOybg1AVbGx5YZ-idZJUU8oq8MYg0mZdwG7HWlxfPSxeHqqzOsD7mCgRRKxHNF1r9ySkuxPBAyHcSj-ZwEjqhaT0HdQNzN0xV9-kQUK3tBtrMUbiZyU1wJGWpQfV7qMPgXI8FuUwLNVgmF140LUleSXoftmZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=v3yklp-vUU-hNDsO79UfuntZg5UWijI9lGBuFIF5k0Dnwo6Nq0_eUHyRyewZHk-zyvk4tNhk-LJml6xEsF8-BH48dauhnFvP7KkWN2eX6GEEGfNP126d4XFiDJqkiOdiszu3VQly--FNxgeMekA3wtnTbgSo3De1bfKhGRSO1RA5HfYC3WNOP7fvoIOybg1AVbGx5YZ-idZJUU8oq8MYg0mZdwG7HWlxfPSxeHqqzOsD7mCgRRKxHNF1r9ySkuxPBAyHcSj-ZwEjqhaT0HdQNzN0xV9-kQUK3tBtrMUbiZyU1wJGWpQfV7qMPgXI8FuUwLNVgmF140LUleSXoftmZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=O104_7LSjZm-GFOCG72qDWpG-nPs3JMvQWf1hdmHnfqqSzyxl6wKvp-ZiWeR4k7RmYLpd4xUtdqBAvmuHxM9w5dVlsj-DJibzHHdB4VRP4tmG49r4y2Qce-FA909K4fQydan4pWUJGhepYyjJ-SCUZCU9fJjwdbQeV0_kFVpLGPfKfXCtb12yGseROJrmEiYPEvgexAG9yAh6XN9-WmCzaxKQMsvNHcHXuJWmxOpuh4IjHOqYMdLukC0w9CN_x6W_oeCiLWOTZZj4-utnNom23iDQJToH-U62y2LfSe6phkkcIxQ4Jk-Rz2SvYgpTiH0ssytfl0amZxTOhSx1U3_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=O104_7LSjZm-GFOCG72qDWpG-nPs3JMvQWf1hdmHnfqqSzyxl6wKvp-ZiWeR4k7RmYLpd4xUtdqBAvmuHxM9w5dVlsj-DJibzHHdB4VRP4tmG49r4y2Qce-FA909K4fQydan4pWUJGhepYyjJ-SCUZCU9fJjwdbQeV0_kFVpLGPfKfXCtb12yGseROJrmEiYPEvgexAG9yAh6XN9-WmCzaxKQMsvNHcHXuJWmxOpuh4IjHOqYMdLukC0w9CN_x6W_oeCiLWOTZZj4-utnNom23iDQJToH-U62y2LfSe6phkkcIxQ4Jk-Rz2SvYgpTiH0ssytfl0amZxTOhSx1U3_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNsx0tdoYwNP-JhB-FX3OLWL79YVcFaiiQmGvZcVl1hDg4GtaQZiyBaIMr02ETe0EKzakp3W51-OFAtqtxXGfbc3A1HVOz_mZLHq4lazMMaRL3z7zKHOhGYDskiwN0QW6y377WtmTcmvrHXAP_g_3qDSV7IIAQoxK_KX1dA1sjjsVAdyxOGZDoTkQEt8GcGvuUv6vYdlqMKM32UarIanRND45x7cm_bt8NBeL8QT0pbn5zPKgDrdnT6_ELWHPtc6f-ylhj2cPc7ZcOkTQuezH54NbYe8Eh1-HQ7t4mZB1lC9Rups3uR3REIMs8BlfwxdKipjjEBiTTEbjlFpyAldcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Ea6gPW87c19bykm0Z3F-abM7vM3Omr33HbDDgZtLDaGc-RvZVFwX_ajPpkKw-_ZrMl5tUJLxD3JlRKpPhX9kUQECuvQPUg63qBqZ2XPTV0_jdhQznuHLxbBjpthLO3pQ6H00FM1H7zdq_4fiME7RWyVD9PP5cjpRkarKtj_iKlzUBmtLhHy_oD63s0uS42wvWXCho5ej_PHL5SM26tmir34fv42GnajDC2HO0Z09JikfHJ1IN1_IsByrBam_GiyxO2WtlFmyRm8J-rTWCJ9sdRERKYO7lIZ0PyD4qhVs-i0gy4-qBuvIak79R8nYu2QIJcCuiYnRq_73kyhCwLDA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Ea6gPW87c19bykm0Z3F-abM7vM3Omr33HbDDgZtLDaGc-RvZVFwX_ajPpkKw-_ZrMl5tUJLxD3JlRKpPhX9kUQECuvQPUg63qBqZ2XPTV0_jdhQznuHLxbBjpthLO3pQ6H00FM1H7zdq_4fiME7RWyVD9PP5cjpRkarKtj_iKlzUBmtLhHy_oD63s0uS42wvWXCho5ej_PHL5SM26tmir34fv42GnajDC2HO0Z09JikfHJ1IN1_IsByrBam_GiyxO2WtlFmyRm8J-rTWCJ9sdRERKYO7lIZ0PyD4qhVs-i0gy4-qBuvIak79R8nYu2QIJcCuiYnRq_73kyhCwLDA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8McUDPF2BNcSu21fgUD3d-3QF43VIFa2lAQR-L17m10JYVEaza3zSqivM9pQ_qak3HmN7W6vAGrOlGL9tpxtsvWDsXJo0UMOZDCHHveJrApS8gL8l4CpkxlbjNsQudE-yAHRxFb-q-XWFikJGfvf2vZuZtK-u6mtJRykSDyOyF5Jkuo__lYOR6tgFiXGaw_A0BQ524WB7p3vmuk_PF0cHHleldP6Jbm7XebVDAas8OhU6Sabknp_4bP-pF4NGrclBx73ml7ifR7I8f1IKADKSktD2C4Um6BE4lJP5sLt0OfHuPtPxb93Zqg57hPgFS6H0et4JXsvd8aRjRvGOUjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=iBiXpU1tPgUc5V2riq6cuAv_AR3DTw7IcGgDCNvx13LptD5pddnHvybKDcRv3J6ac58q3GK5TfWYS7w1whw18FnxZuhVBOBuJsolMjdoZcLGnDcj4nfU8sqxuGf_yGE6QUwUPoWuQmKDyEncziw-ov0bzZ18infAQnB6r2fMCI3WX86b9QAX31B6uuraiusQfdV6y8M5S61_osGYqnKnnCUbVlJP-7Hixt7szyNDPjVX33VjX-cEAuVZJ1V9OzMRgcup_bLgbnO3vqwWTNDeisPbf1SW-3eipgv0YrPjdx3GmT2epzULEOIuL076-7tciDFlDBaxHlNJqCIOThQEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=iBiXpU1tPgUc5V2riq6cuAv_AR3DTw7IcGgDCNvx13LptD5pddnHvybKDcRv3J6ac58q3GK5TfWYS7w1whw18FnxZuhVBOBuJsolMjdoZcLGnDcj4nfU8sqxuGf_yGE6QUwUPoWuQmKDyEncziw-ov0bzZ18infAQnB6r2fMCI3WX86b9QAX31B6uuraiusQfdV6y8M5S61_osGYqnKnnCUbVlJP-7Hixt7szyNDPjVX33VjX-cEAuVZJ1V9OzMRgcup_bLgbnO3vqwWTNDeisPbf1SW-3eipgv0YrPjdx3GmT2epzULEOIuL076-7tciDFlDBaxHlNJqCIOThQEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGswZHqeqckMZiNo_-iOknZcUT3_B_F34C4YI08an048icXZxP3ZLz0BeTdoqHhvEiZXWraSUAhTzgBHf6P3fNHwBRnPiSioM0HhFMEicvhnjyFzQD1Qljlx58BGtCOa5eBzS-bGuD2jwCZybzCEXHoVTo9AAlLKmr4-hnuHksibKr4HThmIYJflrAoqrFAkm8yucgsT5E_KO-F1GvGFeWv0NMv8Tud9dVtmgSIL96beGeFQAThzFfnpWtU4DNquIBSRdrMLWgYMSUbsehfapQ-guuDD_gPhBd9kTVBXEI3bpVwtHkglfSQiWSJaneD7QJ6uD4ptvuipnDRo2LHEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiMAeUPGzXy5KNeCydxoIEK8N8kr5jSlJtnEBwOjtFxeYgw8mIDwXNl3s8zWHpKuZuVYPoXNY56IgvZ5Y-zsChojeqc3Ly-bhgiOn2v_ReOph6MSpxqJtEWOMU4FxJvGpa5ixQGA-VVfL_Bo0WbKckewKfgReJKeCUA6tpyqB3BHwDIfQNkiLUIOJW6eBclII7pPZUIDy-YnESDgf-7_Hr2rU6OPmtIvY8v-Rq8cVqmynY_1y4nlbOL2qVk5gK3IxUArAr0JvgpWk9KrWR_Td1Li49Vbt4ELW-Nn_GBPqB4A-ubYS9ZW-dDt4UTZHPERlMDHq1NTBMzqROSwrb8cLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAK22wtbuq3f_yHeyva9GwkPSdEToMtNbPcg-HM_ieCU1U_CiaiZNdN6-Cx6O2jrw4G2GmQe3xGONh3FLdrY3jX7rwETLZvOreOTEFzvPO78umwfeNdwydptcIuVEOlZ8GnFrPiyI1NxlRNRpbUVOhJMVufdX9y2ewWQXEp0liILI8Hk7fQzLgtz7qkpOwx0bkhrqRhDM0DaxJS2hbXMziuIkPp1Q_tyjIMlBlrE9Qtu5ydAtmNzGhny91-QpZr6OczpyqEnvdzYcp-VL0QsZNOF4448K_KC8BOki5ln9kRuTiwqpERGF5ZxiiuUu6YdziZ955guHXzZmXyixa1yLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2zC8nUUnrjK5dsAF1uupdg76o0k1zyzRq-fWqrzywzaxU6Pl_t0bdsl-220-HpTU0UjQ19pLuPnj2KxMs9eYdCvhEOmUqGwfJlp0PUUUFIOf4_oqlWD7BA0hjsHolvvw8Ive6ylZaKp_tGyHb-KgJwNjHqhorl_VwvZtbICP7wZE8wmwwdSo1yx35SlugBjXcYKrcs0soIiRqwPJn0F3EyfYKoAwsm4RzEwgfAg3L7AssIKgmjdCQEe0DoD72hHtiX5CPpUq1fJCRuSQP1Ru3IOjWp7gf1l3dt9e_1_khxjLs4sc49TA-O9BBPbBDxlTBVPThaPFbP4fGNYrg34RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2PRUvkPV6xbJTJwiSPeRGiMhTz617DdUlbrQyqDl3wS2o4E6t2i8bCamWJfS4jaI-1kk-_rDj4qoBvYWRaJY_1loF1Vb_pnErl_2LbAs3IphwyaHD_0pYNzXZlLSAToMnH4RT18-EdUxkMZ-GgMR6_BkG1Ywun6OvTGwwMDYTv3PK0B2X7JOkLRj97V0gJ8NbiN_-pq-naUn6MTRNY44jO9CztxQacwpK1UGuPMYlOHq5DsPSbtjuDJUCWiyAsiZp4ueKEsXP2wStGVbuvRTPxkpHqEZLgtdWh8YldFLaLeFv9eHkVyAX3i48g6GaEMGWQ60njwZKQRErSviK4Cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEQbKzDp5rb-S7Wj8J_YP6CvklSKXWgH72nnV4m5ndN3hVnANjF-XkcqIhilWzAr3k7KbPOXpvMboGXT7fZLs-JeG8deIzlk-mKXlvl4oHDWgso9235dQf6MrRmYv3EKXr8fxPWUSz7bCz0XG1t-BwdgFeyLIOsZEavIvzJXjV038faxcf2-fEgaLzYEf-PCdUoCs0Gy4j6RjHGlC62UNzdHwJTHZhaZzGt1L_EwG_7AVqI_F7gNSvA0jxAJUtmpUhxCSUjb5kCc2S4-dm6meH-4RMdAyZv_hfZMGSrO7Z1d32GeXb5smEt5Ng4Vz_04TGxT_pCWC7kEE1-CIM3qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBHHvMCsj1Yon0KMNbUNjPHDswnwgQPIuPFhZ5jn6NmjWjxcd1yCBoswi794H3UalVe74ZkO48r-cTz1ZmfC8u1WGCn4rY76Xg9FwdAcCVCPt1fPiyGUmp9Vvsw90uJjooh-cVHmbF1FAq-Nj4YcW8VD46hVoKPdFiYCq1uzUGmnfBqqfatiKU1cenhZIuE9NTJG2OGQYz-vfoVg-uN_gyQXd8SIRErJtF4Bpnf3dQChnRt5ZHBAL-wA4v6nXBd0YE8NLs2L5xcqhd9KOA9OaSYI59RxtgOzg_5897e6M2VbL4jLdSaS3HfpVTvpV16VGrwXLli5KphLohNdSVd5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rsr6fqXVERqXpEQX_W5kpu88V-lImj9pndc76oF31F-IcGhMMQMVOe4foasl8P0kGwXpHbwBjMBSf0uTJhtqdqN_9U0wUlWp796tXGl0N4gu1RBSfoWx9uuAcK3Zw5RRZYgRsBRl0CWEFbX6l-9PH0t7e37ij1gUtufOXzK1_O8QSwXOCelvr9xpIRg5F0l3YRQTP9vzRMAXbb_hMI6fuac3NhETsmWoudA6z8OJsiEqF7F-yVjUg_7BdiQJhLQDoFgO9a9aIVSMY1hgXSYDa8bqM_klQZbI9CCknIGfPLwygUjh8ZbxM937EjMw2q62p6XKS3O3qsXOlfgl9BSQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=eeK0I1EiQoZDynsW1eUVQGMDJdOdcrHK3REahagzdjj9KtCDmeG4x6n_HG9DUCjHEQLhZt9XoMdd1hq3qFWlxScKCjbZUzRARCwmFSaTuA6e-U5U_OfvneNvjPvN36e7tf_vtrcJZaTuOmnLCJBSD8fWfcgmUhcdTRd7LT5V1MNW3Z84CEVQBAOTjxhqmvfhvQb5uiE3Yq8xjrLk0gFRzZzOPweuQGRcZ_gr0ZVZJKcaYs4kqDCQMLkU5nko70wZWGSelTyeDRu5gC6m7fdi4T3k3r_bAOvpFlzPViwH8BmRpNnYWEqJekVXptkPSzFUpU7a3QeiOotlR72fvbVC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=eeK0I1EiQoZDynsW1eUVQGMDJdOdcrHK3REahagzdjj9KtCDmeG4x6n_HG9DUCjHEQLhZt9XoMdd1hq3qFWlxScKCjbZUzRARCwmFSaTuA6e-U5U_OfvneNvjPvN36e7tf_vtrcJZaTuOmnLCJBSD8fWfcgmUhcdTRd7LT5V1MNW3Z84CEVQBAOTjxhqmvfhvQb5uiE3Yq8xjrLk0gFRzZzOPweuQGRcZ_gr0ZVZJKcaYs4kqDCQMLkU5nko70wZWGSelTyeDRu5gC6m7fdi4T3k3r_bAOvpFlzPViwH8BmRpNnYWEqJekVXptkPSzFUpU7a3QeiOotlR72fvbVC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtqY-5p0nE3h44xdTkHyGmCZ0ZQdpUlNS68gwIe7B9uO3ahvrOi7Tw9QOOl9uekprT-QLgbP_s2RrK-3ZLtHqg09Ffn3c-A-M05J6XjHjG1Aqv4Ninslcw2GTNdm2N6WOcoImyVdnAXlsc8NXp_1ogh4j6aTMizHCm1tOyH7jeXll5404vcYNmZb8iWadKMCByVLXr4zNiMj24iDqnVSjUm1oG2eT5G721A8WF1oXqVCz50xp0kxHxuikwkCp4n88ij-bXTDOQfoiakV6S9tfqcMO5eAnvp8DFmCCZCTbpUr06A3kl9G9YaiBQU2OWOeHICtS11AFJIqQ-r8684sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj8UDXEvCRbSinysbxftPD8FDZft4je3G77lWV4E39nL82pTbe_hCkTaYVzGtSP3H8cGV6lv-_VORW1_csl4XdiL0y9-yoqLwHQdbcT7-c6xxlBw2jKvf9fta2Lu-l3WEs4V623ziQC_CLaa-_eaLYmkbvyjr0XB8I7WFUVRs_El8Yy44J1wIj887UDDNX7aiyEmuc2i2G0jwh5dW_wamt160S_3dR9daoB1QtVcc7vzzE2ZtBRG2rMGBFIxYqSFIE9_Gav5I86_A9Hlogieo5dfsAV0Gj0_5afT0lp1B2iZwzE8IjEyCfgU8MWfDPPPWZHgi36GEyVQ-F1XK594QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIUFZz_s74XOyuowfOnc6Pcds6beHOKp5NuKCDhwsDGTediKAhuKzk1YjCfrVxDbYV1Fl-Mhwmu0Ar9_0IolCyOepPn6qBW9EeqkV5rqum3W84GX7L-kCPLWgjscE_qxoJ7ZOx_tYbEWEnttGPfClzuAT7yjhnRujhKyrW3i7nEXkEpcbQmIPqnzN_yY51DYdKNC6G15NUZ9Wu2MmLx-1ukhSgBtr9sEFR-5oTkLh45sxkc8L0z96BM1Tw4KOHGpijP_Y-AiWeji0tDRrQzm_kaV3q2vyos8hf1gjcuuJ0jwo-KChovFcAjMSOlhhbQ--baFv--VgChhnzSBQASbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXhj1dOyVaJk2rix2A24crX6Wj1Y0YrF7h7NMHzTX0-LKJNsmNX_u_9I84ngMu3qoNTvXGp0h9U4VvBWwvTY9pnExBArUXWbDigQKPw-70Dxq8AtphRTkRWW_orIivkFIs_Yqu7-_5RAA39hqS3mPYgxbKFL-uk-c_hamUrMtTrfu45HqOi8N6FouH9hPUsydqJSC3fFEvGp9CCyRHM02ivgbYpYOH6jZAnuhKDYAZSZXfFP2Q_zeG2OG8WQGlliHgjE1Vkz1o7cPeKQOB3W6LTr2oiwCtRFJWMrkooM7rLmbTVgPF68fc2jz4ju9lGjXOqywu47-f9PlRi1N0j7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMq6cIyvlvj7FUNTWEdie4Ncx1TLKxk_MpraNumpeKsitZ9v05v65eyC-KyIYzUJdvAX9ZmJEW3AiwyAAZ09c9pB9OkAg_IFxU_PVSkhWv7LjRyvHeDosZZeZ-1VK7EQGTyiNG35m9mHRdAp2OaJtK3A5kCd-mFt4-wOEDEVcyr0vLllf4MPAJe511PCuNR459yRvgNE2TZ11wFDnnVl-OEkiMiN_PrPI5yZqgf5SWH8dm4lv9XOgOWtULRnNy0xuHj2nZacObaXoKwkve7IEdqr7gAhijI71LGxV363yJ5C_GA-G6-X_mCgpGG8sCFf6Yz7pCV2hK8vkkm8fn8JUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=jncP7rUUBKKKJsUe237gO1xxoJx6yz8ur6vIxYIfbSAs0asVmpLWIQtIwlse7Is5wWs2j94u0FBi-zNLRmNoC2EFrwX6zX5X_Uz6EN3HATcXXDXX1rgYoncr_-72KMCNnETvMdIFQ-opAlApy0VMDPl3Zq7tc9nmYAyzUb_8xQ0eSKj6Uis9GkFXWOdPZ32m_g29iXfSJezMjoyVQ8Bu9DIcxdWGO1VwwJh1sl9MhnYQeUlUqPhIgerHQfBpyuBRinHnDJS1Y-dPU782C0cGyEKU7yPnwCnxVW77dCuK-UDpZgGW9kswSMDAl0CRKSK1ZtkjajDLMomPH6oU5RouXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=jncP7rUUBKKKJsUe237gO1xxoJx6yz8ur6vIxYIfbSAs0asVmpLWIQtIwlse7Is5wWs2j94u0FBi-zNLRmNoC2EFrwX6zX5X_Uz6EN3HATcXXDXX1rgYoncr_-72KMCNnETvMdIFQ-opAlApy0VMDPl3Zq7tc9nmYAyzUb_8xQ0eSKj6Uis9GkFXWOdPZ32m_g29iXfSJezMjoyVQ8Bu9DIcxdWGO1VwwJh1sl9MhnYQeUlUqPhIgerHQfBpyuBRinHnDJS1Y-dPU782C0cGyEKU7yPnwCnxVW77dCuK-UDpZgGW9kswSMDAl0CRKSK1ZtkjajDLMomPH6oU5RouXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWEN2y8d8lRlvgBFORTcE0MJwGz8NfwXMZGNKSiPXp6u6MsgwAAn0DdhBiilVbHg95uPkCq6W7u6AvWeBcR5FZJeo7GChQg64yh_cerWeNXFJp8PgkKFdOezlHErMA1wWc2ItxjqyfzWEgDuk162g7mcwW6likPkKrcbI4BMehQ8j59XspilgruH3McKYtDIvsK5AVPxlX7TMJjOLrsDyOOTMPm3Dxsx4M-9fRAcKPsO4TNK5697Ht9cgSBwOUDcBsHrDI8h4w_8u8HchJblunAvM4dKo4IRFEHjyJaFZL5Np2gsSq2dEk_Ta2KrBA5Ags13J0nzOOu5pP1FBc5TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Hsz7BazVLTHUv7p2a-CzYGj9j2j32In9nQnAgTThkFY-Eq2kDbUE1cT8hO9x-bmXsUjLRfRwbvSE4EcUkudt6HCO54jJRD298NhXsf56FKHtSbJhY2u_xklvo8iNdKSQzqQvVU1iYHM_WH3EPrZdXbadX2fKPkd_tQghqjwzw7tQYZ88AUFy98r1yaTkt-c5_HBxoAiDV9cNg1MNECI0fzk6F7cwsZ6P5kavAFZaumC5CBwzuFD14oUr7Di39qcu4tCtNkm9r30IZ8S7uedlcidsVwh4i6FBV5b4y-unzwZhmS8XrKCWR4yakHH3e0CyTUaQI-0In5_G3rxXQlrUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Hsz7BazVLTHUv7p2a-CzYGj9j2j32In9nQnAgTThkFY-Eq2kDbUE1cT8hO9x-bmXsUjLRfRwbvSE4EcUkudt6HCO54jJRD298NhXsf56FKHtSbJhY2u_xklvo8iNdKSQzqQvVU1iYHM_WH3EPrZdXbadX2fKPkd_tQghqjwzw7tQYZ88AUFy98r1yaTkt-c5_HBxoAiDV9cNg1MNECI0fzk6F7cwsZ6P5kavAFZaumC5CBwzuFD14oUr7Di39qcu4tCtNkm9r30IZ8S7uedlcidsVwh4i6FBV5b4y-unzwZhmS8XrKCWR4yakHH3e0CyTUaQI-0In5_G3rxXQlrUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=oBc3hDTrXyz3VJLZNQn9lemv5_OizcBcUeVSDXHFRsU0btFzrfE_GxDfgliJPL_Z6ONFK5Ta4ifF7G9YqyBxBWobygPjklDwvjjSOcpw02k9vCJ3lz5q8abCHaxt9_BeXV1mGHcGnjxNJXK6WssaGSJVaFz8c-LC3433iHtgzIW9EGKhRxa16JsEf24nw9ry2cEmsdrlHBBnyR_EYDyJUTVNqy_GIXKu_ceKTVMU0b-9Y5lvGz4YOJnW9RVx4ajyvncgiRtIJiouoF-o3itV94v7gOGy3Qd7wP_IedcrO1djgucV3IhEEF4qDt6ApHtcGpvwBcp8aF_qG9U8gDBlTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=oBc3hDTrXyz3VJLZNQn9lemv5_OizcBcUeVSDXHFRsU0btFzrfE_GxDfgliJPL_Z6ONFK5Ta4ifF7G9YqyBxBWobygPjklDwvjjSOcpw02k9vCJ3lz5q8abCHaxt9_BeXV1mGHcGnjxNJXK6WssaGSJVaFz8c-LC3433iHtgzIW9EGKhRxa16JsEf24nw9ry2cEmsdrlHBBnyR_EYDyJUTVNqy_GIXKu_ceKTVMU0b-9Y5lvGz4YOJnW9RVx4ajyvncgiRtIJiouoF-o3itV94v7gOGy3Qd7wP_IedcrO1djgucV3IhEEF4qDt6ApHtcGpvwBcp8aF_qG9U8gDBlTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmcZbyGhsrYKwQRF-xW43ygUKLtvIqF3Xnjiuj5bX5wXnNOLvvKZJDnDWr75RdQjpreU43_usDWcnH0mK7dFJe1EVzyrzuYv0gOTjwtrAZBEwbgSYMW82h9eUZjooYWp2mATIquEDnmxHpu8HaKsn0AUCW-U_x3QDVQTEqtdSrFx0mofWpkmE3iUv40UDSoj5NQCXb2OZhvlAzBURUSd5xTj4yuhwFzzOkFR8W6_BWjT5lkcllBs-oRjalHaCi8uEzC1tf_1h4BjVPVCOV7T951qx6PSjEeKJGwIt-yIqMVN5CEdl23lIiYw6nvaTvN4eI5QG_3WWpdRnc_RYD5S8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIwR9W1C415L-NQGyVaEkHn9EAnnXd2ULLsF_vN_S8IhIrIg_dslMqCTzt1JBUEnj7VILpbNF3EYTJS8s0bwBmWZ4e-OOTK4atWTjPORYMWahu65lEYKEFBA3xF_IfGysK-ddZnQlhb-x3d3jUYpGai2kV-BWOTu18veKKlhzyh_MmYVaeXmhFuFEmFzRP9MiteKB8FQaZKwyP665_7HVxfbWgLx2W41VXecGvx-Z-MVqpbJ3si0BFhUDXJPGPsdea1zNKD7rf6eKL_ELQtTzwaqpeXXThgGdxtLsLX-dQNP8LDfzs37bqT9BLGkAmHnjyvYqBu2UKgh-IkkYdvIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ORXzdzQM9oTxe_CkhWPs0E6HOEfE9mhSnwL-vxP9Kg9hgup1-P_bCaQgh9THRYbENjo0UrCD_0dcwhKE44L2x5p7TmWYZ_hURac9tBCBivFCOV0bmhP46K4wyiCLT_cjwPQxBhV8tzxOn4Vf44IlXoWJrSiiKFM0aHrYHZLhMQkbt8HQmtNds_SHWv8eTlxuf7fsWy5MABKlZ3ZmGseVkOEf2POtg073zLnTNPK5C3DYdJVKp9av_2hDRB2ugiqGgPT98KWiQMWCHWqBhcvhmD3AvG2W_yYjuFbiYirHeEgs1TvtBSjBw5uoyxdXOo2tB0NP3nCV6xdYWcJUdQt37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ORXzdzQM9oTxe_CkhWPs0E6HOEfE9mhSnwL-vxP9Kg9hgup1-P_bCaQgh9THRYbENjo0UrCD_0dcwhKE44L2x5p7TmWYZ_hURac9tBCBivFCOV0bmhP46K4wyiCLT_cjwPQxBhV8tzxOn4Vf44IlXoWJrSiiKFM0aHrYHZLhMQkbt8HQmtNds_SHWv8eTlxuf7fsWy5MABKlZ3ZmGseVkOEf2POtg073zLnTNPK5C3DYdJVKp9av_2hDRB2ugiqGgPT98KWiQMWCHWqBhcvhmD3AvG2W_yYjuFbiYirHeEgs1TvtBSjBw5uoyxdXOo2tB0NP3nCV6xdYWcJUdQt37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMR_Yd1BfoARqap7MMzUFiA0u1WS0gb1cQADwVVRpe_H9IJTH270WaGB6oKc4MpQS-5lRuYuZEsUSqSOgN8eBFDvRa9rX2Sr9Q4RlxmQDdhKKIhq3_PpPwoRH2ofPiINAv8_egsEhzWdf3ogYzxKmAQbccPfvocRUORd-MiIbLtgewSeQImPzFrwOKpN7aoDUQriVl_kYKrRq3kFsltj969CiR5A0eZ4IGWiLv5rp6bRhEEY6pIiMoU8m_4R-741Y3RJ9XHZkqTZVLLDlJF0naXuacOY8Bi_H9IAEr_VS448-TdCzLp-WOUYy_1qn0RdO7JdRXAkjFoxtKtfHBa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObED2XDfIDVCZze_bMDp_MDHXq-mjX-hAh88fm-QXdwS3Fe40fYPHewEOe2NMZxoceK9blZ87DkiU1Tg-xt2e0zzfoJ_sAXDR6Ii5DQTVwrsrvXgJuu_6x7w0pDORM5-n9oXeHd5gb2_KP--tiXPxRbO9dkLrTRQ9lEAzLMX4i2-NikRubkqyN3DrFJen8N3ij2yaGqXdd-8XqD_9jfxlRL7mqfQa-PqW7_RZXoEFu9lKU3BNwhHqjcn7tPC70oS-hVaNjmdoJNWM66Bv2hrkbR-gicwsZC_EdHi9txB05azCycUM1D0f1JPqQE4M3r7evaESqdCoGFls8pxhn7kyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF3p-9dBEJwQVKs-d57je-n8io6qCZ1FZQ7H5pN8ajG_xLTuvyQLY50A3eYvsFNGQMIakwBrGobL1VZPOdmLxLw_Kzd7AhKOGVPMwUyS1ZIdM-k9mlpR7xxpV5QLVSjiII9V2no6SjIW_GNyFjSqQ0UYuJ8rIX4EidClCMrQj6Cq5s7keDHZmH0hYdq02D5YjRW4VFO_3-TjMN1lPamRhu1C_1EjKbrqYfptmD95K5FbXT-VzsiZ89rMyjXpkLUHxNHY2-Qt4303fyfpyeCNsv3upTpKYeUzirEdXl8sdt3YCoe8-xfdD83eu1Pr51101LMoHKHwTScbJmb9LkoTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgSot8j2vwvxxESeaBrGxgIsRyRbAXuIBHnX4AJZFH4N-TY4e27RkMf_5Vz0XF8W72k5o0hZF2TzqZE0-HVD-Cl16TG94pTGadQb9ZcwMH6kkVrvNru8Mdf1mscSZurMWfDh1GkgbHzOCrL8haLkqsGbRJacWj7f_za4_1IsF6-yLgsCyFfRA97vSyDybVy0vMmHswgNpH_t3nDFbnX8B614iWd4BsgFkQUqO_oTnBXwS8nFGi1WMNVxnMuvTSbnpBJX2gOVn7SGU03kUAztF2fcDtXxQWUL6fJ0uWQbFU0kF5cwuA0ac-PtaJ0_a8dZg5-zL6XX7NoS6OGmYQXE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDybIs4tVJDiMSxT-V5X4YJ_b0eBDNAbWeWtGfyHMSRhWWwI1rVvNHm3f4eeAlnI1jap27lADtg_Rt0Gs1EW9dIgKzPEKnW4TgiqIyqiI132qV_Sxi6k991DDXJInjt61cfDpjP6OHPJ-zlJ22zGcW_K0uBS4ebv611vhGe7kDWmeW9g-pZukSBqT-1SjzWMdpQCPTnzN63eUuyAoK7YLQJseVhHTsPZO1W1M04k5ggovseMJ4z2tSYoHwmiU33MBXB2tAj1iikvZnacdVO5TsMPnKcWQIPqB2fZpfjVu-lcE5QUTbsoUh3oshy5Q8yolBnqINVHRf6TNTmA_2bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNw3QpWOAjqKwcXpzdai1gw9ckuc48a_z6y-ttvnuF-duziTYePudkzYpiiX19_DTjiCQAdHkqsm-UtuhwdKjw_27At1HAG5zk5SdWG9fGcKKSxrFMSYA_BkwIYxAuXVARXwb4QhCyuLIfSoacqS_3rzfgvNrwHEU0G19ncC7_NfYXjSo35Ef5t5dEEQ1UEWeVHn48qDec2YfDb84Yyr9PJdg1lmwewjQ6cj0U4N3L3RQv8LSXkOPQb5FVorLYTn-acFxm-bxZGlaJCLZ2_SlwB5Gs4CdD43KoXGyW6Jzo_g147oQ6_O97ZxyV6mEDHDz8NdVGcvVZ0E0Q_UHTiBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZjPFr0sqTmHfEsiw83LnVELi1VtQO6NRscdiky7WBGjdUiRASaLVY-lmA99i_Iz6udLjSVZbCNqEPeVOyE-2kIwvx3o6Tji7AwhE6GvvEu_fGsNENROzTMI2ZVy1TUXQyLcRwN9E8WmvP0j4E5VIT4v4xhp69Gy_pwG_rYyYpEfI8GW9vtp8POYdXkt9kEihddEH8FH1TAfOK_KIxvRp_7FLHyEvrrM-kaBBNM499abp4KZJELkpPJdoneHPkabUcWr3PmApfXpaaTCd4f5pppekRYjuzNYvPWLajSbhrfGB8dbzW8o9lBlKJWhZ42yqiZBnuU15cY5vxoRNhv-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJNWyTr1XpTBNC4GSmKrtLk8A3JiTM3Rr-3eYuYPAYkoTZw5qXwX_YJ_0jKI991RIvddLl-qmis6iukILMDMeoOVhkh-ylY0itviXWvCgUA74HIE9C_7m7GoNkZWvV31rY45hHne8MN5VOfnaadfa8AZswLXBB6JsFeXCSQzfgAvV4qbAjBgXR-hek8n09uEzgeaG4gkVlBmGnT0apnsHNCrtHzwJITYy4hZghXKknMmMD9puKkmwdwQo9sbvdwaaocCC3fVQ6NGRF6vDIXD4xzbxyuNui-sXxVBbG6FG_5EdJksY7ifuE9KvyTuHBDqb9LKTy5_5juJjNEyEELs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDsuvI_9q31wXr-hC7mTJxRQq4DFm5vukKhz15hnir1Xk2gdAZDnqliz7WclfoBXuRCd4k4Hsx2yHbQIG7WnYZzFU10X6nHUr3QHjflBDdb0pQ-7WygPPLOTqW27JOgdyqEGDvHxAhqEqQsuF5-orGPQqdozSXJ98PdcEfCirxflwleGQebiFWv7d__oMf61p86xxrNpfHPbsCf7IYGnQMij8mFh6vApVNQ2ekh9VnldYSmr8iJEO2cYOtdjot_tULmVulqvVeDDJqsnERVRRm9_AX8j2z-7cpVWnJkJVTqjh-SQbA-v8f7AmtWhR4gSN8FfWc3UjglUT7HRiRNVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppxWZsDB9CrSQISWrKAAiRyBjJNwGkEcywHpFjmLWe4i9RTyHJno1XQbskuUGoyfVkALUsyqFbt5vFP2k9MPvK07S4cj7mPIrQxC__0smbv4aYaB3sv7iz_DgIzZB2MuPNV5yQxg77-Sf10t7Rr4-Puxu_iawzBHjQiFOi5jxqQzyZYF571OcT_Jjmy6p-Jx1HgazoiQDfrmdTNckOAN7eqMdUPxZo6Tf7wbPcPmWGBLNQASScEc6C01qyCgeHoVgaAliTKih9K2BIQtjkw-gl0ridFaCrKCKSs_5_FFMGpaioUS9a0Xynl4O-LFHZF_iIesWNTkglXWpGWtWDtpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNdmF287jDWs4c3-NZ30KC8thekOdpWkDRmZhnS_2k1UFaNa-zWXWdySMiD_rrK3oxJVlrySBM4qSDBZUlbbH9TfcNmg6DJ7XnRFVC7Tf_fix0umCjcVC1FWFkkvzeA9_OCU--k_3LITHYPlFfTW5R06PJqNHWho75oiIMvpS8qOMhjC0EWcuFbsxeXAtylO23OBI31IY30OjklGBGjSfVELTmLDw1KkOiIflGAz0OuuPdk4w2MJrCcsaPw8R_K8weBgpqV-A9B0uNSteItQv3QNLjlqtV05GJ9GB8pcSVb4pQFZpmzP9W9C8opvmTRYD-BuM5HF9dOE2byVHPwyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=p6kM3JibR-8TwJ_ZGymQNMiQ1yviTaUXhvRilptLKU16VyLUiG0kbbpOY_f3N2paGH2YwBIw0CVN6xAubS0F3vjW7-lzeGW1A6HJYGqx9kzPHbUtRXxN_Ewoe0Xq2H5PQaVBbdUU9ePxz-BPOm89HK7KibQROTfbDc41TC3OOOZLNm3j3gta4NKNrmB8h-3LklcXjRteKwooI7jC6pHaAU2q_cqu98GrKBqd-vLQUAocKdbyepwhXD6lsVFpBG6XxYvtVjHUleEZ09npa-eoUV0DgZ14hHZOm3ni-A0-233sxFh7cKBpKE8TPzFOXI2MP8pNmopSzTZZ6p6ox0xnxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=p6kM3JibR-8TwJ_ZGymQNMiQ1yviTaUXhvRilptLKU16VyLUiG0kbbpOY_f3N2paGH2YwBIw0CVN6xAubS0F3vjW7-lzeGW1A6HJYGqx9kzPHbUtRXxN_Ewoe0Xq2H5PQaVBbdUU9ePxz-BPOm89HK7KibQROTfbDc41TC3OOOZLNm3j3gta4NKNrmB8h-3LklcXjRteKwooI7jC6pHaAU2q_cqu98GrKBqd-vLQUAocKdbyepwhXD6lsVFpBG6XxYvtVjHUleEZ09npa-eoUV0DgZ14hHZOm3ni-A0-233sxFh7cKBpKE8TPzFOXI2MP8pNmopSzTZZ6p6ox0xnxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ISBFle9onoAaNBRF3lYBnIgxqfp7s7pAGtKl8kbFD_seojBrGH_BDsMjD82IJvXC87nZWIbNr1rEEvFjjcOHgf_2vBoK5BJta5tn_8YYO2RerCB15PbjrG_NYZS0yUckM050HpPoAp-Dl1l1yro9eSVKRT6vG6q4gnwupCF88fFfuGUeGlWyWi1aL_Z6ps9rgNW9k2KFhgbbdnM4MHNdnVO7sh2Ro9nqelSHvxJtIGOrd1rAf92zp5sgUa2vwiaq9kqq2xcSdzQYivPgKQAPnRaKWhhGsDxnxXff0_O7ntHDG0IcH6EGQ2J00tJdkr8ULQBcCsooRxiz-j3sJ-7new" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ISBFle9onoAaNBRF3lYBnIgxqfp7s7pAGtKl8kbFD_seojBrGH_BDsMjD82IJvXC87nZWIbNr1rEEvFjjcOHgf_2vBoK5BJta5tn_8YYO2RerCB15PbjrG_NYZS0yUckM050HpPoAp-Dl1l1yro9eSVKRT6vG6q4gnwupCF88fFfuGUeGlWyWi1aL_Z6ps9rgNW9k2KFhgbbdnM4MHNdnVO7sh2Ro9nqelSHvxJtIGOrd1rAf92zp5sgUa2vwiaq9kqq2xcSdzQYivPgKQAPnRaKWhhGsDxnxXff0_O7ntHDG0IcH6EGQ2J00tJdkr8ULQBcCsooRxiz-j3sJ-7new" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DukIZS9gAg0AkjCA_rLe-q_hh-9cdcy_m6EzlYFFsRHG0O-d-yPJTg2q8l3V7gkO9_h0dHMYrFDx9XDOZUBural445J_fVYk8tVZbqOGmUg5RYXbL1yGcdS6tacmKj14XKsYLhMnJKZKINPw7BZBKedTHkariaXZKBs1yDpgvHvHNciw1Y-w4v6YYzuVxzbx2fFgglSrk24iis2Y0jyzYzV2BZXZsgP81sGOq3AP1d8-C1DvQgwPSl6zXO3EanD-SlOM3Zn4kUNIKWb2dNAQTPp7TmzBg0sn1gktOSjIv4yK53GWRZTFLJt0zbMYoPacBVaDy1ItOSEOF0dgbu0ByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPawUYdobh-f9ixXMGnPUyrpz092LcogKjeZ7hH1QsrtTKS3zN7ZWrbDHqUBeRomS_8uBnsk7OxkX0RQe3NYzEDB9_cUI0wuQyBtGcnZjZKgNXjcUROktkmwG5vjytCDcVn7AwcXs_xPhF21aVBkkmyc346VMbG3jvIw4URlHKDLlkV8DZf4eai8ln6Q1gI60aXlPL0HOAP4UWWjJ3f6TN4lF1sc4l8DtUB4Cl3R0jTlb1aIirNm4wNa_8ZlarF8rqTR9Vtf3mftWbrhsc4Fj8sjrNiUUiwo8UECRT3mqCIE7sgWpCAEe_532Pv4qs-KylAOQNfP6nL17Ct84V3Ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdl1F3CMrivsTHoDI0cI1vMGz_rDA3XPtvJBi_RhQZ6HhKJYI_yjVepVsZNr9BP2cCGWqJ4ZkLBNPG7bX1b5AA_vsgLthzd-JOer-j8OpgyrxJDeOdCCB_i-gQZ1vS-4vSPy29pxyb8ro6cFsVwp-tdIm7w9JsQXMz4e97KiuLYr3VrV1V-nDD1Q6KtHQcjz_By9x5apjrk5D-blJsZBpXlsuHdISZ2B9_AtUFsyuRiJirAWlTX7Cb4JjJpF8sghkED6TJvIMLYeMu1mpx8TGmILM-X3Sr7_erTKvtVyb-jmzLdAwsRkpdCfdjhvRK1_OYCORyrbNLRGHomduNwKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
