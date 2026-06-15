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
<img src="https://cdn4.telesco.pe/file/S9peqB7avsPA_Ca37i3PZ5VcdK1h5ou3Mf9zIIHOeyp-3Dwnz-sRBxuDYjhLgA4WNLdeTYf1NCa5vg28x6Xuu4xsl_FQfwLXRCs39k0-HzZQgCObm98tyvjHBv1cnfijj61PJZtF6Kl0XIp1OpUcqfs1yrCxisGNj50t0YOnCJpkxcyTeqkFeYwkNAD5VCnmJLoqN2U5tLwWyDMp8oWzgS_-sRTOctiF2CoMeqfG2pvF1RhGQwWW7yUHYuPa60bTwGzWSH0EMUNAZUiL9bsbOFgRCG9NZ3osg4AR9ODUbq31uw5j3PPuZIg1QCZkEi70soXCztaNoMN1wPBBCzZCQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCeY_I6ZeHmowhf6WSFQldHus8QaITXuVMBt7wfR7KyhMcmpiKL-TitEfrUgO_IX-BJPAOXc8wvaXh45EKEb4bj-hFM3PGn4YvMAGB6j2EF4UKe9Tq2GfjwKD-5QlfQ-xgaRfOx_u9cF7172-TESNyt_q-k8sFXiVYDxsVmlchmb3EcJNA_nDWgz5iYf83Iffd0xN_sG55o-rwC6SvZQCqCvAaZ96Bx45sIZmrafFC-0XVk7fq2kADWqk88buDahgu2qsrBzvjeZflgMEljUwotb-KjehHgw0cH9WTCsg0Xbh0otsftgWo7_9c557dvjF1DgTerIrvqZICjWVLVzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzOsHTYpo_JOqRS_pLj7DSlT-gcBF7nS2c61U5AH0GK4N4AmG99UFkk4ESWwTADBVDB5XfYDCQ4L70jw9w_gFGwosxzQK_9l6Ya5UoccO09OPZOvw3acR9Ben0MDTgJrDxMT-Wb9tZ0TyvJRWFCrYJH-dESYua3D5s8ZWT8fjJifoREVe2prTnz0JhJekHSoaRSb4p_IDVCHUmLmS6r-_I2zCn_d6s9XHhykbs8fpfu5dfZfvOlym5_382Dhl1yX5ZHdCdUrE550XMKobp-0LttMabgsHIYSiuPV8xPgn_TKR7LeW1MqC2DVAs1XIilxzMovRoqUuPyzZK7EHwHImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4F_6F5Aa2Zvx1bf6wMEbKIfsbubOSZ46j1fmUr0dASQPfltrhG8UR--PfE2Hd-HF4DFo0uw4QQmJ7SzY5-XB2-u1frziVWW9IUu2TSdTlHTcpcCD1gbuQT1PfzEbqShX3lDD3SKHKHQ0qdTseRxA6tQkuVh6vvcMUDejLamnqcaXmn1Z8AJZDdUZ6yfSZtD9ZKzhjEgoip6liCjhmt0UbJ0-x2jWXjZUyNVnM1QcsKiHvI3f5XPeg0z5RxPq9omv0fQubvDBgT147u9NzDgrGxw-9YZNvrWWJMZW7zaHPO5UgGzwQkyKnH1YZJwxPMLgaHVcU41GTNITZW1aqKG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6O6I1KeX6NbbXk9akso76C05rdaw9_jsnyzfse0ZjYLOSikD46nUKu5zA7YiXFtLUaQ_duoXXIDrmOcY2uGmMsgIMuYngjUzP_ptm3C_hxNua2SNeFchdyWEgf_ghs-O4xGfhT6fQCRZxddI0OVyU2f_AvSTQRe1gJUoPHJyNEE7O_O0MNssF3LMHHceKh2FPE2zTq2TjTtvoVymAY7VFUrSeGKA0PuOErEIs6YVMsPQZbN0LMymHNfs1QuckvsnosuBLbaLIpFP-XRKWCpocMTOCnWLys_t2EvvNVQm9gZc40leEiyh-lGFMy0P6ua9N5paF2_jWYs_a5pUleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd8n2E54zJ8YhoaiObz1oEyyyKdT4EljHv5C-oa4YphBW4e2PYCt-fTfOzgimFWexppyieUUXbU2PR0Vcym-WEXEXw62WlMzAsURgvkxWbzViMTGBevPVKqgoMcyRStRQaRXs_G3xXC6epTo8byI6NG0KDMzU81LhfNrcXdBuFemT5xUZvqXcqq-P2Z5nBbWlC_wXjU09FXDqBhftj3v-hafODV9wt9g8Qq_fP1DwB3_PhzEXEsmOfeIrsPaYjfWD6dDVtVULey8wk4gfYcA2HGNIibG9DOyQhw21SCvX9CeGLFJ_SIvEV-Rxa0ZPkAh1ATUxYeOeZ4S-g4-KO_MGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-thAneT0i8IHfFu9t72fBzz4_Gcp3Lj7pfjP774Kf-5Y_GzT_DhK_Wotra5h4YfY6uejTQZQkb1tmo85wphu_oz-R4rbDRACJDgWHl0swkVvebHQcsl9vzt6NFsyzV7Xi9gR8pfMw_tuvHmyrmEtutIoZfYkxiYfHWfCmjTiDrQoeFZT7f7iWPdmN200ctEfmOtc2bKLxggSJ6uSlUcyhEL7g4mmYVKJDAVFZzfyOd-Yi9lz0QS5GbJxnw3-uJY2qOT2f9ioNhWATHwYhhAQq15PgBDm6KaAJsrdo96ToNBrAfQwyipWxVPfqgRk5ZdsBmXPbG_0ptHd_37y2YeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mVibPBw0eTr1gRTGNQb3XRCfny3Oz-uh82TwTsV3xvMGClyO5fmI6shvbZpKO3XEey5XidRloasQiHdbrALRSFQZAnisgoaRceVWlI4CTKNGoB00Ghe5CNX0baKLelkuhdT_iQQYC6R1cKSkDT-QdKb7xG2HyJeYdTcbpNYQfJF62EvT2qREMpgg72uID-BgYQXRuufpMUEYKXaIsoR98w56qi5eDOPV31uMsOMUmdiiJb3ba9oX6hVb9z63MOK-DUDfFC5X88bAtLXs62907JLlWfcpIy_lhoy1aIlLLZEMtLoo-fdn5qg5ppozUDL6y7ocXanJeMU1m4OJcOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-BzrRHeVQ2UMm9WuY2JtXe5_pV9kg1-2rfhdVquGkw9j4gBVXeCkCYZX9ziQVOvFIRyqp8V1y-tWNRHg1ZT3Qi4YSYoGJg9u_mfGwmYRfXI8GPV46QIGw8lIB6L0TVCJ5w2H7L3rSzMGrExDF_-AcQ3xu_A4nWAQvLNnT_XWD46MObcGK0sMN92FPYG41BH19LRgq4YK7iFXK1hFIQst-2BPIqEap-5D50stkDm2Uu8sIsONpqrr3W5D0TeMYCmBz-im5D8ZfEcn0oY_RxM17mfofIocWayViApPRhL2dO9OPVKKn_ZeXKtZkpT4ulXU4d7I8BhGiAA1sBFivemXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmvdHAO4pU_4f06Fr68SJteJeDlEdNBymYvXLWssp7krHRzwaeU7OfdCmnaVjHicsfBavaIEm2EZ59K5beqOIJKjU4WwRgIA6XAHg3pmvBbw5xte2MItPLeEzeRxN_RCL6Q7-mWw9yfeoj5SgpbEjjWtUDFd3hbTmHhuCWPdvEfB2EGojAhrrCeVKgGfmcmYKSDdIavnVjhgKtFpCdR-a-FPQ4hrELlvvhreMPlb9IJG_N9X2YF0NSa5v_tmoQGj2ATL960BcrbKjsXSrW3_saHdcfkYH3wp_22ysy8V-EB2xOKmQIg9gdUda-5PcSDin942Yig-G8ZbMp1uUSycJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL8KzmqA8alOx_-hKTNHGWqia5p5hzmV_es-yNxI_f4HJdd8sImbr_m9lHfROteHvfmY1aGz7Uruc2kqCr7IwiLuejf2M33I_mYi1y5pnO5RFpdPQaBFVNT2R3AG4mLgux0epC5kQUWUDJ1kWIabl73ioXi6xiJTI5nEYLZUd0AhKVjk3AM8KlF-sOIV54zJXjid2nE10bLE5bJYQigE4aHDhG-wtaRsiBRWZ7T1TeGA0SAf7YwZAzNCu-slnrCSuYoyx1rFOpZ6jgrZbHmb76NPimZksxVHiDPQ2HDvZT1CBb1fe9VDUtRdkFsn15iW6cpqBYiS19VhiROaqRnxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcptLHubu-tLQS39d_Oab8L7RLOTNwSwKXE-Yt8pX14TNQFYCz2u9sDTtYanQHOCLVC8s0dJFmCbj1eAu80RmZ8B1p8FsWM6qAvn9oGB1I7OP6wrLLnrWzK_chobBHnyRRZ_qezP2cCx1AoWCF5M7ndDMX0jCwzjLhGR_ivUyqi5yjbpNdEgjqkP4-pwK-n5MraIumiKmX7mGvEbzAisOUvD7qmDUnRuyfoly2AfiWdxzdPwLEPHzUfUC72WR8xTSJImPpCAlx_FbPtVTPyN897daOG0Fb2tnQHZasjXxGo1qHUocMByrbYyK-v6UO8zHLltU48dFh46Smwj9VOpQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL5AVJ05pw2JRXZs2msntKA5wBTmOHfBsc7QcrPU4HcVuQwxA-8y2oBJvBVCO_oKEM04JlXGsLoEpnDaJ_WEDTGv4NASbk95Rgr2yTTxPwxS1AVhsDgj_hvuDuv9-HqL-i8c9QlpQFNs0iVc5wpKf4oimZ6us3RZcboM9tqA7U6ICo3fQqPMax08WVSG4hnoiMVspYLLEHLWZQRED_-HAe9ReI9k4QFKTUf7IXUKOJ9bZjrXrVBxR6EqtPltDNNPc1cpXMNt4WNLJFx69VqPftyIPpz9IDu5B1njj-EJWJhPhAh6xal8kcfVdL61vnsMsgz6P7TynGdMZEBRJGw2og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIPRV0-fgFD2L2PQU0XVCv8lZwmRaYM-wxqjcK43rIl87iO1sHVrqv8ipoV5HYvFKX-hKckiuYr1GP2ZMrJxz2z6J9eaEtWPbgxJuAdH0nJXJCZBGxYZE4ky3PTGbUR6Px_WDptl6GwpyKsi4A7CM1rxg0E6IT-JPFtWUvfJW4u0ofE6DPyAQvxzPAqazLSdavH9C4FzQ6GljIuv8q62-wS1zXiO7vGwhQAIVmRFF44nPcHCHWKS5TorgHsny1DR5QUN-7RlTuAFWxABaI5Tf14g-oz5C7prTyxGuqvg03K9xX7cMD0lYfCEFvp25Jcq-qtKCaJ21jtZCNn1osyD1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=GbSh0A2oHFCyhACAaIzwqa4ZSrn4f6N3dJM73hSRpo4nY7MhIw6L-F5QS_6DrRp9sH8cTHoD2rc-yLzOjsVMD30BsWBMc-Q-bncHh-yXZhRfDSrDcqg-K_MuEk0nB-lEY7Z_qBF2uTJ8w7_j_QkBQz_AWAFhnGQbrzPlcZZIfu1hyLtZN_xFHjQxC3vxF9M-Cr6nlDv1avNTVbEwt_-3tXap0ffpCnApOjcFui7Cy1PSz0aofYZ7RcQey8-GdZwIxTolgfAauPbP48kr9p7zfg0S8TOJI0za4DWR4pUs52WKEl4ofSf0ZOP0VuqV-UmX91Z_GDXcEV0Y6hlmzCCCTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=GbSh0A2oHFCyhACAaIzwqa4ZSrn4f6N3dJM73hSRpo4nY7MhIw6L-F5QS_6DrRp9sH8cTHoD2rc-yLzOjsVMD30BsWBMc-Q-bncHh-yXZhRfDSrDcqg-K_MuEk0nB-lEY7Z_qBF2uTJ8w7_j_QkBQz_AWAFhnGQbrzPlcZZIfu1hyLtZN_xFHjQxC3vxF9M-Cr6nlDv1avNTVbEwt_-3tXap0ffpCnApOjcFui7Cy1PSz0aofYZ7RcQey8-GdZwIxTolgfAauPbP48kr9p7zfg0S8TOJI0za4DWR4pUs52WKEl4ofSf0ZOP0VuqV-UmX91Z_GDXcEV0Y6hlmzCCCTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Wx1slMmnIBXBXbegCFkWPOWYOC0kQy2I29LmHKJSR4GSJr0vtzSeZmNTgcms7hKWKoHCHQvsYXa-zk4849FxZMxg1D9DKkv1oVpMuZPrGBJtUMJQHF3Tou3Om1whuoYasEk6YVEqnjiQp9OYbbzdGz-ijDDah1YG-NR8w4xS07itwXrbgqZKz_H59fY--NEg9H_VSIwepY0qoPHglcLuKaSB-spbzbTHpuO-PRupI1rO38hJ79PzBYmlPfQ57eP3r0-e0OWxIZYVl-5mkduhJQrw9FIgJ2CmmAyZqP0_7qr1PCHW0PouOX8zK76uc86M--xbqvTRuYdgvGTjfweRzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Wx1slMmnIBXBXbegCFkWPOWYOC0kQy2I29LmHKJSR4GSJr0vtzSeZmNTgcms7hKWKoHCHQvsYXa-zk4849FxZMxg1D9DKkv1oVpMuZPrGBJtUMJQHF3Tou3Om1whuoYasEk6YVEqnjiQp9OYbbzdGz-ijDDah1YG-NR8w4xS07itwXrbgqZKz_H59fY--NEg9H_VSIwepY0qoPHglcLuKaSB-spbzbTHpuO-PRupI1rO38hJ79PzBYmlPfQ57eP3r0-e0OWxIZYVl-5mkduhJQrw9FIgJ2CmmAyZqP0_7qr1PCHW0PouOX8zK76uc86M--xbqvTRuYdgvGTjfweRzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=CJ4Rkj7aXBRWlSy39YmTxV1w36i2Io-Rxs_uspUu6h_B0s33qp4P61PQj_QuUktR-GOKbiEzjilTPczPDw9898cBCtgoRwKRHcROkl60GRbWH2WIGq0E6LGq0DSM1Munb9bWltTWQ2cVQ_DFx9PH7TSRvV7GCWfRc-_Ziv5cign5W1lQtACLL585hnbXOr-USqvmZUGN8Vi3GFOu4ykEieaOksIOdjJwpuJera1AMo3RaqbgnKJwBvuQy37OBVCjvIGegsUqxE2O-4lYvkOSJK1F0WsWH57JyWyffOcJ5YEQTfaQnohWOSMleTefCWGWRvaVfSWfoxsS8DWjTmd_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=CJ4Rkj7aXBRWlSy39YmTxV1w36i2Io-Rxs_uspUu6h_B0s33qp4P61PQj_QuUktR-GOKbiEzjilTPczPDw9898cBCtgoRwKRHcROkl60GRbWH2WIGq0E6LGq0DSM1Munb9bWltTWQ2cVQ_DFx9PH7TSRvV7GCWfRc-_Ziv5cign5W1lQtACLL585hnbXOr-USqvmZUGN8Vi3GFOu4ykEieaOksIOdjJwpuJera1AMo3RaqbgnKJwBvuQy37OBVCjvIGegsUqxE2O-4lYvkOSJK1F0WsWH57JyWyffOcJ5YEQTfaQnohWOSMleTefCWGWRvaVfSWfoxsS8DWjTmd_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=tCmqArvQ0lFDdn-posz3KXQQm-P-FN-r5GVDm-jWVMkOTBkI8uLY7tje6X_3ku8Zht9vu1phITw6mm0sNiBK2Bx63F1dYgj_eZfjteQ0BIuN_TOKRy3Til2d3nBR1IXQAOV25vmBNvXlnV6K4VF4tNlrck0jv44m9WG9GDGIedH80_kzCPNKVFj0GWNyBkgvyxV8Za8vAxlKhYSOSwu2Qfh_f7nHjeUm2cu6W2_Pd2CXX-6pdmY0KqKaDhOkrIyEXCtF-9k4MXaZHI2qKuoCgZG1AUNdi2z_L8kU7e8fGMjZlejfoUg2hoxtNB7NqE4Y6q1vIhcn0evrpfAp6iOTzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=tCmqArvQ0lFDdn-posz3KXQQm-P-FN-r5GVDm-jWVMkOTBkI8uLY7tje6X_3ku8Zht9vu1phITw6mm0sNiBK2Bx63F1dYgj_eZfjteQ0BIuN_TOKRy3Til2d3nBR1IXQAOV25vmBNvXlnV6K4VF4tNlrck0jv44m9WG9GDGIedH80_kzCPNKVFj0GWNyBkgvyxV8Za8vAxlKhYSOSwu2Qfh_f7nHjeUm2cu6W2_Pd2CXX-6pdmY0KqKaDhOkrIyEXCtF-9k4MXaZHI2qKuoCgZG1AUNdi2z_L8kU7e8fGMjZlejfoUg2hoxtNB7NqE4Y6q1vIhcn0evrpfAp6iOTzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=BS4lwNmJrU4tx_ExaFn4lpW3wSnGXQ2DhXqVITiPjZjF_YtvsFrqHO_DDNgN98moa-nz-sbR837MXf92mqh7NUi3L6oA2DKSyujOBUh-nmr01V8-NFpWUtiv0fVQVu6-UXiNbo0l3OT5E5CTzC1OUiWJqyIRuhpKAZA52WJdhPn-3DQt7KmwjSnnfAQNra8-0QJELlhhC6D02KbambeBuIbVKwR1ZsD5xnReFAC4ip-hk5nOrUmw2RL-UQ8-kmV0vC2xqMORdkmH0uxoxjM4IKe_F_rK6HjHbKxuF14hsNiZdWUxad9ICeX9CotwV5Ond052VUpLojBiJ0Pg-UTzXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=BS4lwNmJrU4tx_ExaFn4lpW3wSnGXQ2DhXqVITiPjZjF_YtvsFrqHO_DDNgN98moa-nz-sbR837MXf92mqh7NUi3L6oA2DKSyujOBUh-nmr01V8-NFpWUtiv0fVQVu6-UXiNbo0l3OT5E5CTzC1OUiWJqyIRuhpKAZA52WJdhPn-3DQt7KmwjSnnfAQNra8-0QJELlhhC6D02KbambeBuIbVKwR1ZsD5xnReFAC4ip-hk5nOrUmw2RL-UQ8-kmV0vC2xqMORdkmH0uxoxjM4IKe_F_rK6HjHbKxuF14hsNiZdWUxad9ICeX9CotwV5Ond052VUpLojBiJ0Pg-UTzXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=T1Bi1wrppWbqrAjQ63CIZip7FvIV0daj1vxXWvxDj5it1-4DqpR6gtPLKJ_wjoKvlbn50OBSsZ1wSQjvTa-uy_5vSjE3n3MMH8LHX8kqrfgoG7JYrgvSg944WmhXRXGMV7Hv0hwJ1TIOCsNTFohFnOzM-8mH2ffc4BBVDYtHi52zt5X6CuRGksd2Tv2P-swGw6RA03SQEJKVTq1U-rZEsVPC3umoLJE7bemC272RbHN9NtWjksmTILp2Mr73ZXHecQrR96hmPywDiyHcmkO4I5UMTwbE-bo9dV2bvm1SxLaSahvhdUqQCRUNn3oTgW2UmoaziOJGnHRV9KHcGjzjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=T1Bi1wrppWbqrAjQ63CIZip7FvIV0daj1vxXWvxDj5it1-4DqpR6gtPLKJ_wjoKvlbn50OBSsZ1wSQjvTa-uy_5vSjE3n3MMH8LHX8kqrfgoG7JYrgvSg944WmhXRXGMV7Hv0hwJ1TIOCsNTFohFnOzM-8mH2ffc4BBVDYtHi52zt5X6CuRGksd2Tv2P-swGw6RA03SQEJKVTq1U-rZEsVPC3umoLJE7bemC272RbHN9NtWjksmTILp2Mr73ZXHecQrR96hmPywDiyHcmkO4I5UMTwbE-bo9dV2bvm1SxLaSahvhdUqQCRUNn3oTgW2UmoaziOJGnHRV9KHcGjzjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO93w-LVLHrbbOrQA2mM_odCECpJmvMzOSNpypyz-ffcYZus-Uvx1ylkOyc7UEQqtxJ-IY3VYNueHu2UeNiJ5mF05_VPVE1M2648g4pxN8Eq5wohbe0C8VWWTFUT5cj82Sk0h4VkS1ocHJ4tTX5B76VMX45frANjKmKhcqXr0J7-tLKf9S9AKRxa6Sw46N1LKG1rEOZC-ZxpoEOp3YXJhWBurVrYNsf8Ju4v-LSNAFA1sdT1A90TzuAzcVqBiSdQv4ORBzsOYuX1ZDTxIGbZMviYdAa5NdXhCD7hEbUs8WMo_SHlh5eoBw0aWwEPaRNw7Em7vyJ1fwGglKvLdAtbu9as0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO93w-LVLHrbbOrQA2mM_odCECpJmvMzOSNpypyz-ffcYZus-Uvx1ylkOyc7UEQqtxJ-IY3VYNueHu2UeNiJ5mF05_VPVE1M2648g4pxN8Eq5wohbe0C8VWWTFUT5cj82Sk0h4VkS1ocHJ4tTX5B76VMX45frANjKmKhcqXr0J7-tLKf9S9AKRxa6Sw46N1LKG1rEOZC-ZxpoEOp3YXJhWBurVrYNsf8Ju4v-LSNAFA1sdT1A90TzuAzcVqBiSdQv4ORBzsOYuX1ZDTxIGbZMviYdAa5NdXhCD7hEbUs8WMo_SHlh5eoBw0aWwEPaRNw7Em7vyJ1fwGglKvLdAtbu9as0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud5GqAUuM0YutY82O4WIWVZi1N61YrpuEuydUNvHqElJPu3SCKYJ1iYjK4Qga3hajxE5Jp6FuNOif_VNWr_I6mJlthKr0bWu5375WB4MBW3SM7k0rLpsrxQMw8VpYytk-MXaBZ-SiVtB8qFErVGize1xI5BOxNU8PEjLUaqGHza-kh3JnBgJrVwNyThTXSB7FT_6ChwAm3GEG1xc1IqcXcK1D5Ibe2WljAupmmYkafjKA6ou9EmDLo1MhUe1bn5og7p_GgTZUCPBt-vb_goJyBWJ4iLXuAEZwoMMeTqXxC1wXkhMweI6H0x75JQWSzA5qzChz39vMyz0i7PyLTKnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=sQgdb_6ijuQNv46d6je1e-vblh1wOgL5o2JyMTUvOzaFigW2bqSMR1haWFyozEmefp1dd7HUL7Z-FVm5omMA3G7s6HSQz2OdaaEwbF0lkQDxqMlp4x-uRQCl7guyxVdqVCVD_ApJGQRjvuMKP6WCsK7r9zjcMKpf0Aid3-MS4M-49tepkrQrpGmRZlZ2UwJ6vtn4g_MCNW0eR6NKuC4VH_ZidELS58dl_dhL1Ihk-MNpWTbD24fZh0ZfIiNGKgu8UcOC9lUtBFZWLpVO4pGCr-cZoVaZ-kzmU6X_eRpzQroQD2i-4dhunnkRXDP1EYjxmKzLmbWYgadIc6JdBHUzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=sQgdb_6ijuQNv46d6je1e-vblh1wOgL5o2JyMTUvOzaFigW2bqSMR1haWFyozEmefp1dd7HUL7Z-FVm5omMA3G7s6HSQz2OdaaEwbF0lkQDxqMlp4x-uRQCl7guyxVdqVCVD_ApJGQRjvuMKP6WCsK7r9zjcMKpf0Aid3-MS4M-49tepkrQrpGmRZlZ2UwJ6vtn4g_MCNW0eR6NKuC4VH_ZidELS58dl_dhL1Ihk-MNpWTbD24fZh0ZfIiNGKgu8UcOC9lUtBFZWLpVO4pGCr-cZoVaZ-kzmU6X_eRpzQroQD2i-4dhunnkRXDP1EYjxmKzLmbWYgadIc6JdBHUzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9beRogp33KL0w3aj9NvoTmNRdwi5m4rO5hUw6ySfxGOejN594vmdbhWyP-YyeT8J0sUgVVDTQim-WXoeUEFvAS-VK-FDKljKitZvSK5LTXLgXMSJc19X4Iu3i5GueZBUsPsXFHukGIL4daobtI0eLx3i7RD5VCIWw_WDcYFuiF9Ipd6C5EBE-qG35_siFih0q861U4XKOSUEhCUDDFG4RdmzuuCLUvS1AhEbcqzHwjnCTa-B5pQ4XihpVpxO4uWfKlln9c7uEgX0LnhIW3PZ4RbZoLgSIBpxfApbZvbPUqSYhIKuOILb1c5M7x6iQNGGSX_dKrZeUaM3ooo0qICdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fserCVzxBFrDTXu_5Sv91Broi1q9jq1UOlBSdYYwm4Y3WpTBeukLdE12hAgwAjXhkRYLcoNf4U5CmeNTlY0Yi2d7syiY49WXOltLpcdYLPjyuUqHKWf_W6zbaIukUh9xLKUAzRsQTB00qJeKbRabvbwylbKBiPcDRV2Ynol6XxWdIc2WBLBMF-neZvkwE4Sekt3HJTJQF9MzwdvilSr8iRU358zNHoLL846AFVtSZ5hEEkRUk0dwnz6TQ8eXqh5jzkO75ht-UiGs_BENaot6890L8IdKlwC1B-uRziFqjMKeodX9kW7DNSR12iJcwmN_p0lrDebjbLJkDX_9mnjHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKpUyahkzXkjbhKmB_9vvH-9OzSghRaSouS315Bjj1B-C5RbxKZ9L0ZY_xz6aWBQG-SG7PUXRaRXYCyCE5vqjTGqbnNoOugwfQgKLVX3w6rTVyXyT3nd_LGllwc4gs-tC7rInOXPmT6bmcaTDR_P4UQoW24DoKCzZEdwvFucx_MQ6RKMRK_cBPEyrgsDN8iDd3Mn0uDXa83H3ifklgibIN8b-0MR3QHffHfJnNQIigdKIvO_hTBiwlOLqEGXRsEM8Ilk1ZsbVUWVl_1YnOS1bMLO60QVn75A_PZ8OEYpdGRgpen45vjsRYjvDAEGkIpA1PeXvmDS9K4v2OmiIHPOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=j-eRC2qPkxqwgcGXUTnS2T1qdiB1FqneHMp-QTAB7tH-bLc1NmMW3HZucI4t6uKAPzxVJ1MNCbrmZ1gzX2ZWq92dcIDv0-EzasZZ7-yIbf645xn2vYAPNy4iVFBqGVLXczBhZSYuzUUaiJ5QH8CE29hE-QrPDZnh_08zpMGeP2tlvfn65u4f6bmcdT4lLgpcPMslBqMOMmXWUojJGLmnWAPQ73-kDnrDO_tLCCY4c_oNxs9XxsCkJSYDosCb6nCS-YMeH548gZjmLvdnwarT6rzRWIcIMhUS09YHYwgCvX21sc3dtLqS2MH5Yw8VQWAW1qVoz2NlMs4ej-NXyIhd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=j-eRC2qPkxqwgcGXUTnS2T1qdiB1FqneHMp-QTAB7tH-bLc1NmMW3HZucI4t6uKAPzxVJ1MNCbrmZ1gzX2ZWq92dcIDv0-EzasZZ7-yIbf645xn2vYAPNy4iVFBqGVLXczBhZSYuzUUaiJ5QH8CE29hE-QrPDZnh_08zpMGeP2tlvfn65u4f6bmcdT4lLgpcPMslBqMOMmXWUojJGLmnWAPQ73-kDnrDO_tLCCY4c_oNxs9XxsCkJSYDosCb6nCS-YMeH548gZjmLvdnwarT6rzRWIcIMhUS09YHYwgCvX21sc3dtLqS2MH5Yw8VQWAW1qVoz2NlMs4ej-NXyIhd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U10So8ElXp-B3CSxb06IGpHi80t7prCLHbTb1mGt2J-UNnHAIxvQ2EVxorDVA0_-qSYkBrgBg5U1ia3pieS9eDNpcjaqjrK0YU9hmWQ23MRHMItPdBt_sCDACBKbg4e5elCCeLuwg3LLGVjoCBN3sW1JfvtGhhWEt-fOqQwHxI901j3XEH33jhGGd1bNgeEAWqevdqo4yUlKR2UHRuSVTO39HksBYIrUnFPFFtRIwj-bsTQJWn46Bo1d9JzkCxZF5EQlA99ACDzmxE1Sq2mAmZMMQQKJ1fnCY6lSnLH2B2NUQ-hIRnadozMeGssBin-28wu0B3FCNb-lyFrYm9T26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHQqmSl5ISdUHuHRN7xdz3ylJ0RxK7WKRgD1o_ZnNQ8oH5fVHZv6if9bsqrbyr_UkffTnOPAAJkLLt7-xzK7qGQAw-pYV9IwHSaOtWyV_QbGWjwqL1SQWJxVXFnAUABZslpTA0B8agSUoYz1lU8GkSlOy2CXDYkim2Ndf-5SD7luFW25Ttd2miNDamAbzr_RysuZwNZeJJ6GKIhHqTCEWOlgYvF9UAVSiSV-rUAT16Kuv53Brv-j90drG24MeiLo8AnqJ-__AuSoLRiwzRRF9htjZtoUYt4jnRjcFmJPQx0yHorn4SWRQp3VA5otKGRK8Ywkd3X8V2LBOfm3YPnRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVUu6UvuITGwvfwDQ_baGQenDaCsEt0O57aMtdUwP85iZsgjhBMt7JRWmzhG48AjHIQf6QijwwV_t-lSU3pKQFJFsL8ylR2qtx6fCucVlOjDG4Ri04HOrCzAHsC8FMXrd2TUYXlj0cYAsMxw9iS6gRTyQa8akvtgWE0-mWCBsyHIKEIhPVLhNJu2C8BXdTBD8-CTHzA1DITP5LmU3UVeC1d9ZbodF47fhjEA8eXleY8V5MDw61UG0-wk7GRFtCkBLPCcYXcgY889MHtqXuMfb-omh3k8f1tN4ucDDEQgEtnHGG4Ld5Ni8Nh5WjjLZEKNMp6Lf8IZ7XU8VkNK_sE9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgbd1lBy9codchMiMu-z6ZJkFVVW0iNczNukel6BRKxBjnf7eYWxAxCxAu6Zo_6dWRwVYQPt7htm7jgf-ScUny1HdyoQ8rsN8ZYlJ2vymHL0i2aH7GNuzJD8NkJCsGELiN0Zmdbj1NNxRgHKDNlQy3e7ScEJxc0PS7PUMElx7fnxu6NRzp_ahmKLVfrM1CyePDNw73b1In_7GGRV-uKxVddgbAeka9MalZnmQBcTUDQnuwSEhcIVj_lQasPShWtOKrL3_lanl7RNxh4I0Uv0Zxp4x1n3poTyyXjcR7EYS-WZ3URAdNlN1vOBvGHLFax3lZwkhmrlvCf8eKVD3eSk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=K7Qn9l0Y06Z3_ez45TnBpHqXr2QCkwSZUZfSGUIRhtFyUd0eBOYGQXwUFBHBr0CE1zJLbG-r71EVj3dG95rRA6uZz9LWy8ENiQ1qGNSn38RGVA16EfVcEnp9iPiphMGmwoPPSyewxR1RJpKSZAGNvFvPADvrX1SZ8zdN02_pzzyMIAi37ooQw_Dx1-_4DKWNtIb4L1f1u2UjBIbDmgOG0cu3HQr9IMxUIMSmP19LETms9kFnvQTxb5RiGa39kvmAuKBkhbxEtBuT4JCkzFFylgAQhQ7atlDRAX2RUeZ88zYcJrb-lymdFcQrCWm2TXWrn8pDZcBQSPZrRjcieLKYzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=K7Qn9l0Y06Z3_ez45TnBpHqXr2QCkwSZUZfSGUIRhtFyUd0eBOYGQXwUFBHBr0CE1zJLbG-r71EVj3dG95rRA6uZz9LWy8ENiQ1qGNSn38RGVA16EfVcEnp9iPiphMGmwoPPSyewxR1RJpKSZAGNvFvPADvrX1SZ8zdN02_pzzyMIAi37ooQw_Dx1-_4DKWNtIb4L1f1u2UjBIbDmgOG0cu3HQr9IMxUIMSmP19LETms9kFnvQTxb5RiGa39kvmAuKBkhbxEtBuT4JCkzFFylgAQhQ7atlDRAX2RUeZ88zYcJrb-lymdFcQrCWm2TXWrn8pDZcBQSPZrRjcieLKYzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-HneFlSGBHsoLcBmEUZLI2AiTh4AQDRXfDTeAiCkD56mzs3n9muzDQvrxaOD80bEnpmG88IA_sptgMEwzTy5f1k1HKZz5EyQ3VWBstME5jCVoi9GFE1qPZv-v7jVdHTqT-9NbD5D33laav8ndQsIrR5JlEZmI872d7qIEPQGJJfyXpQvBsXLOowsYupZDRxGZ74cBcde_g9VAdNwC8iYwPrx83Wk7Aqd1j7RsZPqfLsjlRPQdKXYFyg3KrNLb5DoDTVNd4PvWVhz0lijF91uKacw0QYMYEH8unkOmzZRQL33mxgL-qs54RLhP_xzuD7a3Bd8trEmL0vNZKZKxfWxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmSqjd0aYNCqiXN9YHw81ZXdLSrGDKPKrfe4FZQeJgNad9CnScNqpgy6a3w-2HJgrsLYh_-ZzqTzO6QXGFRI5FA_HDZb9GNpVDl5iQ8p21CW3STidYYdS2Drwjldy1oL4vIysnTV_O6RvecxSwU4A8-E8WiuobK9EispJHXXmsuAZ9P6VG2trJGkkyVjo2mHrKSBfFJuxvMZ7-8-LR3cEaHxBGUgmlQYPHqb1V18XCs5b3E7FsRwT7FkAgieMDCbDbDNkdumPsXD5muGPACVXZsEmdmwDpgpmWM_A0uMaEkvdbZLVcUjW2Fpy4hFbWATkn3A-ggQWI-QzLSn-6pDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=ZUS9SfH9USS_vbY6XI9K6jhB58HjX7v_Iwh-cNdBnIhS9mtW0eugCJzY5m622QN5Ai6lAIRHUmT3lGvlVp-T5GvdmY42XLZkCGLgkiaqDO34iEd-XM6dkmaidB_Jn3yKWquollSwxKxD0FBeCs0dLYBrb6NwUjjcaJ1N-iJfroDkS5Bcp38hDK3KC4XQs5o_BRqeMofl0spHAbUXHbBtw5VyECdCrrT8CgmpjmNyLrt3AO4_CHoWDmEEF_k08J-DfKLlYvfqd2iSg0_MqFTUhd-DcGreuLezD__AsGK1RkaJb97NIj-ZG-iwAOdOCeJhPvQK7C5OIvnwhSMvfiEqSBWOjpfN37oev8uBy6D5XdhPEqDRGvia-DkdVdUIXxPY2DJok5Qnhsbg02kqWHgBKWOU4vDEoOcrrvZuRUVF33mYrioHTxx9KDMq5nEU8mkcahkNnzn_uY3ThIVJArUMfxjQS80jJsaIpzo5fcWn6_qrwcCMnsws7dGlkn1tTYtdu74IeXFtRCmG_rRpPOdpG3WA3RPXB_LZdby5hKXOL8oRmopLtDpmiKwJBoxS7vX-ONWatwBhQsNQh3r4e7-IQBXzqjgvD8IhB-g3IxFzwRvUz_mb45eUal0BhQ7pt-4w6sbtlgwClWZdXrg34UL_jImeLSaeKJRcdKDHBBWs9uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=ZUS9SfH9USS_vbY6XI9K6jhB58HjX7v_Iwh-cNdBnIhS9mtW0eugCJzY5m622QN5Ai6lAIRHUmT3lGvlVp-T5GvdmY42XLZkCGLgkiaqDO34iEd-XM6dkmaidB_Jn3yKWquollSwxKxD0FBeCs0dLYBrb6NwUjjcaJ1N-iJfroDkS5Bcp38hDK3KC4XQs5o_BRqeMofl0spHAbUXHbBtw5VyECdCrrT8CgmpjmNyLrt3AO4_CHoWDmEEF_k08J-DfKLlYvfqd2iSg0_MqFTUhd-DcGreuLezD__AsGK1RkaJb97NIj-ZG-iwAOdOCeJhPvQK7C5OIvnwhSMvfiEqSBWOjpfN37oev8uBy6D5XdhPEqDRGvia-DkdVdUIXxPY2DJok5Qnhsbg02kqWHgBKWOU4vDEoOcrrvZuRUVF33mYrioHTxx9KDMq5nEU8mkcahkNnzn_uY3ThIVJArUMfxjQS80jJsaIpzo5fcWn6_qrwcCMnsws7dGlkn1tTYtdu74IeXFtRCmG_rRpPOdpG3WA3RPXB_LZdby5hKXOL8oRmopLtDpmiKwJBoxS7vX-ONWatwBhQsNQh3r4e7-IQBXzqjgvD8IhB-g3IxFzwRvUz_mb45eUal0BhQ7pt-4w6sbtlgwClWZdXrg34UL_jImeLSaeKJRcdKDHBBWs9uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=gT7bmnfuLO2AyMZiUWsK8ZdHBmcndJWdegubsykVzlkSS5iam1lH9g_afJf5XZVZXG_ro3LgxtpgVpDWNQKqDqgi2P_uchw_yu2P33Dnu0SYT58XnV6LLe7IdBuztg4jG2GgxNO7lHz1oKlsCQQWSRAYdOaJAS07JtjFyZmRMQzei4ehw8jmXXofQaEeViGFe-ggWAZ-5g9ILjhIPyIJsQX-r7qyiyi2MeoIbyzGIZd5rIN5gmHGTDRtTLkPD3tuTeNnMJTAcZ-4pcHPzHfjLpzhhvMiQP3s6XrbY9zMU3LBPz-Sa2sLmZxJdt9XfbPUiOO7hEA2MjicJ61zlfACHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=gT7bmnfuLO2AyMZiUWsK8ZdHBmcndJWdegubsykVzlkSS5iam1lH9g_afJf5XZVZXG_ro3LgxtpgVpDWNQKqDqgi2P_uchw_yu2P33Dnu0SYT58XnV6LLe7IdBuztg4jG2GgxNO7lHz1oKlsCQQWSRAYdOaJAS07JtjFyZmRMQzei4ehw8jmXXofQaEeViGFe-ggWAZ-5g9ILjhIPyIJsQX-r7qyiyi2MeoIbyzGIZd5rIN5gmHGTDRtTLkPD3tuTeNnMJTAcZ-4pcHPzHfjLpzhhvMiQP3s6XrbY9zMU3LBPz-Sa2sLmZxJdt9XfbPUiOO7hEA2MjicJ61zlfACHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyx8XY7-8PwkqYEB7ueL7AGO1rnYlMoXKYWmnYLVWOwDLOW-eMz2l7AsHABE5TIk6hVClax6yyLZL_speIspOy8uGilma0jwwAfYMhNE3tez7Kl-nJ6UblDNJAyEi7QFC2pW8l7zDuBWuPBJo2kOykmVZsTdUxwaS2SwWMKrr_ZYruBWFPOXUMIiHPnhR8GX3FBsaFR4qo_Ea2CeNlki1-6fzVkg4goXmDBY8dW-6H3pRHQqriB534-4s_mCGdBm2GLR02KPfVwKwj2Pt3raBYeqxaLzS-ExyVf3dPfNNpP1QqwuypohNBo4GIip6OgnQwa0misnTq0BnfcQtep7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=NVTNX7GJrKdDQz60ok3C9yB_YfffhvIpuElOh6AYqgJRTtHIaUIecDXMSEdDOR_CweXIP-KeX8dY7I5reoZAFHAh3eIwcuNcYA8r09vdETP2T4kqH0KiSxUXSywzbHnA8wGIWRCPdYSYXQvUvjFDgLy9XCtFwDxnYX_nesM842MISS3bldtWqvS-TvEak3xmSYSzmCRrMupSWphptyz-GsYVdJ8zLtyXcEAN26FxzMzZCCAoE7ZW16yQT4fUBn75VNw7dcy5yBnFl_sGO7XulerK8ePQPBT5_YIHvC8t-PVmr6vl_b-tqL3amd_PusqHsgDi8DlceF5tg8IsKP50Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=NVTNX7GJrKdDQz60ok3C9yB_YfffhvIpuElOh6AYqgJRTtHIaUIecDXMSEdDOR_CweXIP-KeX8dY7I5reoZAFHAh3eIwcuNcYA8r09vdETP2T4kqH0KiSxUXSywzbHnA8wGIWRCPdYSYXQvUvjFDgLy9XCtFwDxnYX_nesM842MISS3bldtWqvS-TvEak3xmSYSzmCRrMupSWphptyz-GsYVdJ8zLtyXcEAN26FxzMzZCCAoE7ZW16yQT4fUBn75VNw7dcy5yBnFl_sGO7XulerK8ePQPBT5_YIHvC8t-PVmr6vl_b-tqL3amd_PusqHsgDi8DlceF5tg8IsKP50Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S85Wvg84xVPhVN71uQK1462rnv-m_cMxWO16-cFNbNSYgnSkSQ6Ux_hGvVsfbnQWaKYveqyckG8q4cIuXOe6UZbgjAZhxzojPjhsTUClawLiIpyArNVazxKD98QAVgrMq6vaP5r4N5wg5symTGAmE92u3pJ2unuswo5G6g6V8kVplwkfhnt-2FPPs0UOZUnqu0u-cUtjKODaTqXMVchXnG5RSvLTOqolKCfBi-hutqfpb5kdY1IN8QJ48hkw9PDeiKjQoYv859ohkrLjPa9d5QmNg5GV0cb_e4nAA-IqxO8vJz0n2Y1qJvJo-iIgI9Xp8063IXWvHw7sZlNMWykI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=hEXFw2Hh5Bjl5NrBz9Q98OAcLibyw_Vk8T9XpgKc4H3b4nVWgCHgaz11V6dlsUSIu9rHZWCnbdNZAFmLi-bZ8lLcjPnYOVY0_ft0aU1USSz_2d5LJK2B6CHOVzZmS3WOYK3--sJYYq6KnCUI4enwBgfR3i75LaPevUIv-wFhnwm4xvyiEi-sJeAz8IPK6UumsTAFTusTMbZ_50NbxmJcgn8RcvyFWG1qseqhJU6AICIPyJZWv69UjMMjlq5igKnVJIShcyolrmHvCmc4wygIad-XxhPr5GdnH-EwcB0BD1oVZ16d0qZ5RiJR9gn6g4XvOT5mU9ay1skUel8WPbabpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=hEXFw2Hh5Bjl5NrBz9Q98OAcLibyw_Vk8T9XpgKc4H3b4nVWgCHgaz11V6dlsUSIu9rHZWCnbdNZAFmLi-bZ8lLcjPnYOVY0_ft0aU1USSz_2d5LJK2B6CHOVzZmS3WOYK3--sJYYq6KnCUI4enwBgfR3i75LaPevUIv-wFhnwm4xvyiEi-sJeAz8IPK6UumsTAFTusTMbZ_50NbxmJcgn8RcvyFWG1qseqhJU6AICIPyJZWv69UjMMjlq5igKnVJIShcyolrmHvCmc4wygIad-XxhPr5GdnH-EwcB0BD1oVZ16d0qZ5RiJR9gn6g4XvOT5mU9ay1skUel8WPbabpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=XFU8DHfzfYnoXBNFiDogUqK3aHUs2SUuCeW-nQVOK4nuwYSnGfLStOxPbzA4hOTKDOqPrBsjiL03lcNbIGWy-1a-v-PWqlSvOuoITWYKSbEXdYVnsIEReWbD3a2Rlz4QscRZ46_4Gpk1jvxnYF_HPAb7TKlndi39J9iAWkZh38dTYSN9rGalCjbJTlaElbHNUi5caI1ae1L04Sx42F_1vaxNGqYug6RKlXcAY-P8eeVgrqlQ_2oyNNQxUclf43OGA6Hfe4bUOwiNwV9UdSvDRPE4HEXKgJaIpE9jJSFAMjpKHc82yKukW7kLPoSME73diuXyIGMwEedx766JSr8AVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=XFU8DHfzfYnoXBNFiDogUqK3aHUs2SUuCeW-nQVOK4nuwYSnGfLStOxPbzA4hOTKDOqPrBsjiL03lcNbIGWy-1a-v-PWqlSvOuoITWYKSbEXdYVnsIEReWbD3a2Rlz4QscRZ46_4Gpk1jvxnYF_HPAb7TKlndi39J9iAWkZh38dTYSN9rGalCjbJTlaElbHNUi5caI1ae1L04Sx42F_1vaxNGqYug6RKlXcAY-P8eeVgrqlQ_2oyNNQxUclf43OGA6Hfe4bUOwiNwV9UdSvDRPE4HEXKgJaIpE9jJSFAMjpKHc82yKukW7kLPoSME73diuXyIGMwEedx766JSr8AVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q11yKojJPDul-UhM911zheZrJ6Xqaa310CYCVrRWHGgDzBkUQMtzGDj6tjj0VXXqjX8lg-W4n1zDJ5779Fgq93P7ketGA4URskz_6Ts2sfDLkr52kpwgi67_jnZVtIgK4VzOwP5XzNmzW3IE9ySTStb5jrseYU1FTsCtuAQztM8OYAsaUJuoogAARlM-HmnBGTbq2UxD1eaitAd6lGGEsWrfvD0tq-TjbC3s1ue8fAdVDgWie3jSixsKW81eyq0Whxm-h46qsKeTvPgiGUG8cGNqWUIIjwnaPxS-6NEsmkuP81CkflAy3_VMJXrJv0yuv6zeXuqxr-uDgPaL9Ll5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Iavdu4GeEG6vpu6T-quwdFaeco2J7c1m4Ka60qKbpkznhn4LQRsUvdkkCkm3ff0ErEa_9ZaPoAfxxt0z9weZqap8VOeIBMUtRBMUP263pVqZxzW6fZh6zKnyN-0ZHsvP7J9hTGSRfsp25vPuReXYzCG12W6pa8Ysal4x8Y0lU938BzfqiznPHwkOlwQLwCSHnonJu_wTqSoS-AWT7eNAqNM1biQISK1TnwLE2JcSkuDwQ0HOtuEQd2g8_rKhMVVyI-aSt9JK_EtMtJB081HIpe0DTaKYNWgxaHccV_oKtAcBSQrFO7oWKLTErxXisPRpTvb2kXSxP8nzt0Exka-9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Iavdu4GeEG6vpu6T-quwdFaeco2J7c1m4Ka60qKbpkznhn4LQRsUvdkkCkm3ff0ErEa_9ZaPoAfxxt0z9weZqap8VOeIBMUtRBMUP263pVqZxzW6fZh6zKnyN-0ZHsvP7J9hTGSRfsp25vPuReXYzCG12W6pa8Ysal4x8Y0lU938BzfqiznPHwkOlwQLwCSHnonJu_wTqSoS-AWT7eNAqNM1biQISK1TnwLE2JcSkuDwQ0HOtuEQd2g8_rKhMVVyI-aSt9JK_EtMtJB081HIpe0DTaKYNWgxaHccV_oKtAcBSQrFO7oWKLTErxXisPRpTvb2kXSxP8nzt0Exka-9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZprecgH-NAgwdpSAR6TvGOnsmmFEBYV338WIQTD5MkxNBGAkRE8COtjFZRHPSbHjWe9u3XeQL_BO9kC-wjUSWuTW_VtKNogX7HpXaxmb9ADFy8ygSVkPQcfNga9vGvZUdrKluJy0D71lL_y7ZL5baIorArlF7PLC_ooTRwBCvB3PJjNfJiLOW_cWLueXrMVtGhN9qPKtBybPkn7MDG9JX9hZAJQ8ZcexhwBFLAgQ31ayzGaNUNO7EWbHZrjWmHK6QXTWd7gLw-WW2epj4hBJ_eqYzhNBCuGDpzPzqQxkPygyl3zukRYBz3YSnTNlwxbdqGUQhRSXYEX8-W5zN_p0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YfeEc9HMZOFeEekziOITVCtxBWbUgBSt200k7KSL1U_WpsQD7H2yL_2Ao7xymyUHl7MwYA3oBR1BXoUxf0FjpVLt3wFp2Khbj70wr9WujGJ2z1_yXif0-j66tCZ-NYqc7wOOQE9QbaI97l__D1R3QSAA2wKNtGmN_XTJmySHt724y6-rIsr_S2Tbkewvtc10doNLApfhEKKnQ6KKYmmy4UnHY6qcVbOW-WBDXigRDaj0DXjALu20WcLJ0IuhFeWCgWFswpmoZF_ps1B5RL6pMnjR3GPmfLWkNUJBRV5YbjlaBkJM_zekPVfv7VtbJBBlZmKVsZzXrGXYC82oYbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL7K-ISzx6JduLMI18agw4j0i3x0Z27WSeFzuj6gNcaTNaUZygac0yrTQqb7suLlT-luyLP9woXlcMd92PVABn8bSVyfeRiIBgUpD96CXR9r1dB6Popz54GILa8cpMD95dCmnk-izxNYXe6an6qREy6Jwqo1UYfFxS4mts8LWmJfZC9h96G3dlzDX6xBc-MkZCwqEQU08ePpuNA6suOeCsDmeLdXV9eVcgJz60KeBsoa8AIbmzq7XAdd2EY460eH60P7yNLCGWuPlmZCyTX2OdyaTyz610m5t9pOyahGA-uz4tJjSucW3T9BMkFhDFd0fbFb8b95e_jxgpMdVl5u-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcwTJTiJPX8F-qAF4NwZUMqUT9eJwTv4mTaPfkBFctmqZs3F1WQhdbwDWE5veazndwCK2TfICvQjPGcnHGiYyHKuHZ2do_uSaVFcnG7X4wdpoRwlRrORvsS8S7bOekXuaZ4poPdf8mAusc_evZ9tYYwGW2qTywsGUYZUrB8EHN_bf7R2lqHSIJ0j3UhEs5dwKUPp0EZbNCZM55FNy8zxTGBJ6lhTmgGc2raX_e52xjVGsm61xTLSfgl8NYBxZ9DPDVZxmJaARA2pm1j2oGs88ReyaHKfMpva95YOFHfyF8rz6C0PYWD_y1lXgPOqytuEkqb82sn4FG7eX51Rrl0Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_6cdY9P7rnHRWl18i4Ccd5n87LMyhGYvgQss33g_CsctaxCgLiz4gNpsuX7Q-wthMALRpfAgvOYgvH-j22MBltNdY0p4A05AmmS4PoEJZ1HDlYt6EW6UGSzCWarPydrUDE9VhkcqxJXPhN_SVJmHBr9IXnnzYQueTqyLbISuB63Fe35vghC4cOgjuvcFIa9VPcTNr5l_8L3TyZQpdsT9Xofv1kr4It3FUBrirDe_rkcMKdV2qOsReOvYdPMMCOWeiGLK9Aq_wJbwrwHrrfFgp9ys8XUFawftb1kR1EHXQWVze9vpYUU7AgqXicCXQ8USP7dSJVjq8Uq0lwh3ZuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghUoewmjyp1kn-zZLaZpLxfSjjqRInyu-a1k07-d40gz4E3nC92DfLUuAJeqx4Drk5VJs0tAMIVQ4wrYoyKBvtSPXpjNI0Qh8kVt92HmHlz0EZ6nTDUYIwVW7y3d5eVHm4ty27l9A2y-mNaNGDT4VdOFfMrbH-dL9yRRfHbZF5PDqeoA85zHK-zW_Lq0COO22V2RBe5izFb66D0_Isi5Auu4vVWZSIUcZdZXJqXEy0KkJyyqGWib8Pc_0D8O3dsgAqVUIgRWDveoJ5MbUNp8w_W3KuCtTabbMOhfSlAl-O0nkXR6OxR9wykO_w_EsVYL7dW-GT5hHcWGXQi0uiBIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=MleZmHb906t39nmKOfrqy3rm7mRykOx9-PTDaa01iQJVJQ2HI3QzwT2I14Y8TyObuZFgZ_Iun3OVbi_MI1kKfvDW3b1pe2diAbko-ZMzuGQfME7kogdB_Zh-DIXDVPSpoVlrdTeLrkfuTbpl5cF0hcwWZKbix_09u1w6bcrFBAtJPPQfMZ_W6-UK31E8a4mSEtTugN0C-mJheP9l_P5dZVLEcSZYNDh4Kg34U9RmndnX9Brh4BezZbUiVU7G-daUuGx3VsKdtnAaSs8jjXEYQprO1EazkTkKga8isMu7h37yLhl2ADYRZg8U27eKn8_KcNbcGVIXH8S2RAMMTExZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=MleZmHb906t39nmKOfrqy3rm7mRykOx9-PTDaa01iQJVJQ2HI3QzwT2I14Y8TyObuZFgZ_Iun3OVbi_MI1kKfvDW3b1pe2diAbko-ZMzuGQfME7kogdB_Zh-DIXDVPSpoVlrdTeLrkfuTbpl5cF0hcwWZKbix_09u1w6bcrFBAtJPPQfMZ_W6-UK31E8a4mSEtTugN0C-mJheP9l_P5dZVLEcSZYNDh4Kg34U9RmndnX9Brh4BezZbUiVU7G-daUuGx3VsKdtnAaSs8jjXEYQprO1EazkTkKga8isMu7h37yLhl2ADYRZg8U27eKn8_KcNbcGVIXH8S2RAMMTExZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUXreCb_Rc6sUvSHORr09eRTBbI3tSOzGC4aj0TdNdZ8nl6llmI609LYOwmibKYU7abH5rmZSWv4uBzGGmvc2MEK-Mw_qUq0Jp7nhQGBX1xGabfQRFHsbahzd1bzIuhTZQWVdFaMXycAmTY-SyXAfAcetAK1XlfnAHyE25OB8o-ZhBZF9VepdoYDhdOtKaQQzY_1aplY77Q2HBeNeZ-8Z_6eCimrxBT0DuMNOgUOq09gZwc_42s6YCb_B8hiIWPYBIhLlDn7TRNZ9v61vvlQwSoDMGoxi_PLd8ejmzIXuvLNheoDdQhrRVvoWlESAVVwmGo-TWIUQcIObaBJLNH7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SihXldnTqQk29pIJ132rKX8pqIr8Plc4Wb-XCAJIkI7CI9h6k6Hrr9g4diqTrkwdRg-peZ43RBjK53igrwJpXTuBJrz3L40ouCROBvr6D2Xoo61KS3pcyjTyNc2tskKk_3zZyoLCWWSxswqj8Jk8ehsHUN7DrmMyzv1vkj0xy1bOiAr5WkJY41OPOslrAoTgK37uXfmn7DI1TOtHFAN19k2p-4e1NPWHdKclycaoQOhssxxid6Vu57rpBPfy6HLsQwrU1ovRozdRY1T2_yR5Azavh_bcCJRTdkH2V3oMPt1lNxsRLa15YJLpLgQ-AzX3VWH4txwsgopglaKa97vlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba1a4T7QBaB2-0Pq0aZQZKqqCSkIw5X29PUDof9AFIb3LuB9ksgF_RynUK9kxVQs6f7q2HK_OL0ln73TF4xNz02GxiHzzwWtfs9yOD0BuhCU2rb_n9YUoYoCl45hTBoaXXOdVyjx96ryRjGXjDh2y0Cr7XDPU0kVtIGxv7BmqtTEctYks5Ca6f0zKicmn-1wRreyMz2EdL2MhDseJuoXMrt3CrQksDUEdenMEWBlpxcaTti8NWMCRNWaq0LwBwnwShd2H_OD3BcSe4wtnQFMuJ7OgU_2I3sgZadgFLLbAegei31P_QjJdXsE0LUGAHuvW0l6N8-obn-j0hp4NvDLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfZ1Ek1bds2kxTK2Tj2v20b_25bnEK_EdU_rkhJaVX6xna6anQnoTIjWhohYczfImgvUB10XeIMFQo3yqh6Yo64vJD9nI_R8BGTrtOut4FcQdXGA9JWEognuB-i1-_Y14q4_tKXtDVDxnnEh4XO1y4WP53wxZ3UAlVpBAqKo-oq6KekfWyjCyuqN4EdfMi4knjJUxgSuJ1R53eOkpmRS0E_tTUiwK-ztjuvRd_n-6l-kT2heZjTBPCyGwoIt0BO-OjEIJ36pBf6hv6Nj9igvca_UW6yAH1sCq-uzhiqG5_0rKqB5ZXTa-C_zO3QGtUDsAY9I19D1dbRfohGmFwUiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=aeAQgC2otYodgXvTKTnSfB71CS07y-J2m9FJX-4RgYWO3MF7EepSiP2GXYkbD2orWBeEVRdD13CB5VGSGEkMdJHSwhy0k3argKXqLD1h9goFOcGZJ7S1JShQSwPJqQC4hVAc85_ybowrOdlEr2pEx2bG54JroW9vUEmlsTgQB2ncbCZoPdLCbPsD8IUJLGnRekcG3zrk7M0WMuACOTS7oXycx7NUDYqVcnhp-mtZO0obnqWC0jKgcgdc-aPt4yqJ-zADUniKw6l1Hzp4lPsmXFcMeOltywEJwFMITCWPAKwb9aLJL9S9PbbzWLcCyg0qWceiRCpK97PIWCFsnhrpTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=aeAQgC2otYodgXvTKTnSfB71CS07y-J2m9FJX-4RgYWO3MF7EepSiP2GXYkbD2orWBeEVRdD13CB5VGSGEkMdJHSwhy0k3argKXqLD1h9goFOcGZJ7S1JShQSwPJqQC4hVAc85_ybowrOdlEr2pEx2bG54JroW9vUEmlsTgQB2ncbCZoPdLCbPsD8IUJLGnRekcG3zrk7M0WMuACOTS7oXycx7NUDYqVcnhp-mtZO0obnqWC0jKgcgdc-aPt4yqJ-zADUniKw6l1Hzp4lPsmXFcMeOltywEJwFMITCWPAKwb9aLJL9S9PbbzWLcCyg0qWceiRCpK97PIWCFsnhrpTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oclZpWFpZyo9MMC-ZhIgWZ5dC_3ypo2VEGn7W_pLz79XM1FLdZZn7P89X0iHa_5KpzxYJu9XjeHGwz6_CdkVvHpDQB149Ztc_oR3d-Cmy347fKNM4xqTXoszp3NQR3eGwLJDeA4Y3pJilwcBDBXRXLSCi3Gwzl9-qTEEJIn2meM6k7_s_P6B_-V7rRyNosOCBkv30dur3kUMyeFMwA8axZWa8H1a3zIh8tLooVofJEf26sbb-gIOfiT6tIWDVWjJPnn4-HmrkLvNMO_A10QRlYIXxgsVWOZpNekdAt-iwRoi7rgXL8pia2CZWUUX0pcQQtdA7xAfWr1Xj0dAuyZtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfStYPkz78b17c1CnnCgavql-bwGYVlykYZcws8xBAmo9JmXGbHvFA1Vq5CBEGMlvKXMIukyyBTh7T8o7SOw_w2-o4QFWw6LfBihUmUpl7udFiUkOA6uM1T25sQkU7c8JCPvhMFy7QJDML9EJ2_0DQFj5u4YChqfBpH9NkSXm1swNJMMfbUsvc0uYM8CBuLcnMI7Fw7SxXGvwZ4ckiOz5Y3hsw8ByxvdOG_eYow1E0ccqPHWmtAUjDTn8_p-Gsz1HTWncjv2skdmAoS2MS1aPBcsuMGYj1J361M6W_8AcRVDCFJbUTQmtoyLwWlkJhKYH88jM5RtALEoZYlUmhr_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
