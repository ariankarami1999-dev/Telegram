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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCeY_I6ZeHmowhf6WSFQldHus8QaITXuVMBt7wfR7KyhMcmpiKL-TitEfrUgO_IX-BJPAOXc8wvaXh45EKEb4bj-hFM3PGn4YvMAGB6j2EF4UKe9Tq2GfjwKD-5QlfQ-xgaRfOx_u9cF7172-TESNyt_q-k8sFXiVYDxsVmlchmb3EcJNA_nDWgz5iYf83Iffd0xN_sG55o-rwC6SvZQCqCvAaZ96Bx45sIZmrafFC-0XVk7fq2kADWqk88buDahgu2qsrBzvjeZflgMEljUwotb-KjehHgw0cH9WTCsg0Xbh0otsftgWo7_9c557dvjF1DgTerIrvqZICjWVLVzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzOsHTYpo_JOqRS_pLj7DSlT-gcBF7nS2c61U5AH0GK4N4AmG99UFkk4ESWwTADBVDB5XfYDCQ4L70jw9w_gFGwosxzQK_9l6Ya5UoccO09OPZOvw3acR9Ben0MDTgJrDxMT-Wb9tZ0TyvJRWFCrYJH-dESYua3D5s8ZWT8fjJifoREVe2prTnz0JhJekHSoaRSb4p_IDVCHUmLmS6r-_I2zCn_d6s9XHhykbs8fpfu5dfZfvOlym5_382Dhl1yX5ZHdCdUrE550XMKobp-0LttMabgsHIYSiuPV8xPgn_TKR7LeW1MqC2DVAs1XIilxzMovRoqUuPyzZK7EHwHImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4F_6F5Aa2Zvx1bf6wMEbKIfsbubOSZ46j1fmUr0dASQPfltrhG8UR--PfE2Hd-HF4DFo0uw4QQmJ7SzY5-XB2-u1frziVWW9IUu2TSdTlHTcpcCD1gbuQT1PfzEbqShX3lDD3SKHKHQ0qdTseRxA6tQkuVh6vvcMUDejLamnqcaXmn1Z8AJZDdUZ6yfSZtD9ZKzhjEgoip6liCjhmt0UbJ0-x2jWXjZUyNVnM1QcsKiHvI3f5XPeg0z5RxPq9omv0fQubvDBgT147u9NzDgrGxw-9YZNvrWWJMZW7zaHPO5UgGzwQkyKnH1YZJwxPMLgaHVcU41GTNITZW1aqKG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6O6I1KeX6NbbXk9akso76C05rdaw9_jsnyzfse0ZjYLOSikD46nUKu5zA7YiXFtLUaQ_duoXXIDrmOcY2uGmMsgIMuYngjUzP_ptm3C_hxNua2SNeFchdyWEgf_ghs-O4xGfhT6fQCRZxddI0OVyU2f_AvSTQRe1gJUoPHJyNEE7O_O0MNssF3LMHHceKh2FPE2zTq2TjTtvoVymAY7VFUrSeGKA0PuOErEIs6YVMsPQZbN0LMymHNfs1QuckvsnosuBLbaLIpFP-XRKWCpocMTOCnWLys_t2EvvNVQm9gZc40leEiyh-lGFMy0P6ua9N5paF2_jWYs_a5pUleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-thAneT0i8IHfFu9t72fBzz4_Gcp3Lj7pfjP774Kf-5Y_GzT_DhK_Wotra5h4YfY6uejTQZQkb1tmo85wphu_oz-R4rbDRACJDgWHl0swkVvebHQcsl9vzt6NFsyzV7Xi9gR8pfMw_tuvHmyrmEtutIoZfYkxiYfHWfCmjTiDrQoeFZT7f7iWPdmN200ctEfmOtc2bKLxggSJ6uSlUcyhEL7g4mmYVKJDAVFZzfyOd-Yi9lz0QS5GbJxnw3-uJY2qOT2f9ioNhWATHwYhhAQq15PgBDm6KaAJsrdo96ToNBrAfQwyipWxVPfqgRk5ZdsBmXPbG_0ptHd_37y2YeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mVibPBw0eTr1gRTGNQb3XRCfny3Oz-uh82TwTsV3xvMGClyO5fmI6shvbZpKO3XEey5XidRloasQiHdbrALRSFQZAnisgoaRceVWlI4CTKNGoB00Ghe5CNX0baKLelkuhdT_iQQYC6R1cKSkDT-QdKb7xG2HyJeYdTcbpNYQfJF62EvT2qREMpgg72uID-BgYQXRuufpMUEYKXaIsoR98w56qi5eDOPV31uMsOMUmdiiJb3ba9oX6hVb9z63MOK-DUDfFC5X88bAtLXs62907JLlWfcpIy_lhoy1aIlLLZEMtLoo-fdn5qg5ppozUDL6y7ocXanJeMU1m4OJcOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcTQKFWjSocS4SiURLk0QU8VKDJbJ3ZvZtIoL1Zdd7eIdtMnINUgw_suDMlRPq4xhGD6J0PnZxqPoF66wOX4C7WEz7hxwOOClopXQsFYYRzQ0iSzd5ABJrz437HPxBx0YWK0hyDfctCvoXwczBiCZzg44nk6rzxYvTAjNM2AsjA1-Gu_tKcPl-ZJbe9q7JOx3vxoA0dF-I65tgvlGG5qEwDNrXnq6GzmjAM46MEgTuG-sFna2fqwyqIHoaSs1ui2EUXCQTR0oDJ54xGuHn6N3KV6NA2eOQm9L9KpxbkaOOEH4_SwYp1Oq8c-x-6GbqfdkzYgSTAkeGhAnpkk7K8MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M03B7noW6qpfJyjjTW-RS8nZ6WmvQ946LYKNhoR89xFn8Pioz_m_X40n1XPxopGpcFsgNQX175DEJGJ4j2KU0SeyZ5h7xF_bx8uFFXuOX8jj1ZxQkWABP-WtxtoHjpyJNGAQkekDxOnGPAH1Dc4nsWeQNjC7piquw7uP4VkEoNkJj_vdCVhb5jME70-wLWtILzqnDgZvFCqL8j1DaVojrX-LtGBO8_AJ5E04m28SdEptNzefVeiUfOPIakWAed0UayHGisY8nw44lJvykCkczegOQWAp3xKgNwwqEVajXHvLYzDQcYdimzSqiKalqFAgY8VkfN1i5b3fRIsnDuIILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOn4FVtZPOksup3-ez1BI-nJRPNbncnyMtzk_w2mxk2zdrfkjyvjCYVakTgR3emLPgN94hYGWl0OR5dM7sJ46NkZAX5kOaamDdM9R5PQY_JBtqabf-degEFgvTp3kg2LRSgTSwkXJPTe_j1yqmGYhsEe86vER959rrWNbTHY8tGvl2Fu6MrhbNilanJOY5-gkPKs9gKE8q4wyHVwu6zpp6XDj-M24_iZ0NMCp0tCZjCm-bgvrGTx5ibw5XBlbuWLz98gCFip2GNMX056rBbnst2HqkPadUl8O3Tzwz-D7U3B8zMXQ-o7KhWI3f0vmWKV6NvSk3Of-Kn0CMfr2vCY9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3ovK2gFu3IHn9pRMDb22vr0N3y-g6Y3JcS3_4rqzChkiuz1zu_J8b9DR2DOeRZ78uCqJ8por6s8lbA82QbvgQms9EcXYxu94FHC2wTLTpIMsWY4si8P_h2v36IjH5J65bWjKTJoJHEsr98zhg7_tJSUnf9EnC3rt772PS26Kn8z-zeHIKeSYU9by6fKuCxVbbBEbNK4yN2LVnrHSoKKU2mLtpDzI3Dch1OeFy6YJ2IEcLSlzasDvRju_gWS6WxSQCHvIt9TE5jrM3i9S0Cmgltib-YBosS1QhcYcs_Oz4V630Xk4-pezbOJKvzsIBhHeLTzH19PFEWnN78LXhVwCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujevZMJT2vtJKRfh5ub7vF4No6pSZ-QaQqsxY53grROpcnySFy6Bz5AwitYBEgpTNsKfJMesgSCeUuIh5NckB4ePUut7S7UzZdKRVGJbqJvVLb45XPBLdd7hancqNYe67WDMsgCuEIOu9TekbD_LRSNgq23XXj4gAakc3N3T1PR4mf-_Ehd4yvV2sySKpJ7oxi2bxVExIPrjUKvr3_6XihEXauUMnQQnAyLvwVU2Wm9WFWBLsawi40gnyoRdhmUer3vVIi-tOXbzzuiHVWqWgEN4X6xIZULM4pD4yNk_q0KN-Rf13jiFupKix1PtoJ8lALtd2MTc0AO_TKecnS5WFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=fc1HzTm8fZJeXBqN4SxnUBSAqpTVIq4bBbss7l11UMK5PG76f7XM81pwFc8Aa1h-UCu7ScbTjDHInF_0K3bqZH6_qnpVmIuGkPNHGYeQlbgee6H7KsS1GactNGbEVC6TufjL49_gdFtYC22HA_an88HSisECQkTiLgCOKcCUxi3h_8aEW5b3iUD0-zQwWgXE2-zi7EEQymnPSm7kvwXLFJ9n8oBvQ0-ERXd73JqLWVj-Ift2ZJz3d2JmzYpLunoScGuno6UvomcxS9H_WKJTWXSgjAj-nxKGsbEmgUV8sAufK3JXA6NuorTk-qlVPbumZLLfT_WmG7QgtqMUGSe04A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=fc1HzTm8fZJeXBqN4SxnUBSAqpTVIq4bBbss7l11UMK5PG76f7XM81pwFc8Aa1h-UCu7ScbTjDHInF_0K3bqZH6_qnpVmIuGkPNHGYeQlbgee6H7KsS1GactNGbEVC6TufjL49_gdFtYC22HA_an88HSisECQkTiLgCOKcCUxi3h_8aEW5b3iUD0-zQwWgXE2-zi7EEQymnPSm7kvwXLFJ9n8oBvQ0-ERXd73JqLWVj-Ift2ZJz3d2JmzYpLunoScGuno6UvomcxS9H_WKJTWXSgjAj-nxKGsbEmgUV8sAufK3JXA6NuorTk-qlVPbumZLLfT_WmG7QgtqMUGSe04A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=K4ogsnmQtcvtKwbt_Bs5uMg_QFy1F4Pg30h2Gmvm3VJlBCAQo4ex3dA0z0QvaylYHa-OB7XiH_vbKaXCtxIWTKqZBtw7IeI1AYnZ6tT7oVjcYUXoVcwIn0G_R87--hv25cOjaz9oS_NoK3RhEVfEpjJLAZSmNPuvMmZhG5AjZc-HAmLRt1UClGDVTD-vVsegvrmG9oxTdROTk_FlxBJuT58NVWN0_lj2hPSFbRCrBq0f5uaqFG3ylWeTLyZJITE56soeRFAb-F0pWJtNWFODhAR6yFVbLfPQEMpHKMfIOGiJ_C5ZaDs4dLkTIBldfKykIjMBD_lfH4yD1dnbXQwiRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=K4ogsnmQtcvtKwbt_Bs5uMg_QFy1F4Pg30h2Gmvm3VJlBCAQo4ex3dA0z0QvaylYHa-OB7XiH_vbKaXCtxIWTKqZBtw7IeI1AYnZ6tT7oVjcYUXoVcwIn0G_R87--hv25cOjaz9oS_NoK3RhEVfEpjJLAZSmNPuvMmZhG5AjZc-HAmLRt1UClGDVTD-vVsegvrmG9oxTdROTk_FlxBJuT58NVWN0_lj2hPSFbRCrBq0f5uaqFG3ylWeTLyZJITE56soeRFAb-F0pWJtNWFODhAR6yFVbLfPQEMpHKMfIOGiJ_C5ZaDs4dLkTIBldfKykIjMBD_lfH4yD1dnbXQwiRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=r6iFlOLraCcFj_-uQ-s078XHG4V4Dxdd4U1h8M1lcGloed82Z0X399A3Nq84ldM7_pzsdnffnWRMbymio9UJX_oLg9QK2fkNvmNG4RnOJ2RKx2PFbkesEI-W-N5xH6Gfq_x_rzbexB2WpqmvWp4OWXF1RRvYtbkyVrtR7LZKxghXNN2wy6ASLQf0oLnCdzxMLd0EFRPEbcAgpiNBvQc9Usvpa8No7J9g5HGqOYRY2ceurYxaT-vnyiOKmwc8dazIJ2wPFpTmnAoQ7j4_loyxvqXHz7dwhFaiNb_3eR0PNFP4BCGofXj1NGPkbM4hZhrN4jFeQC4Ipg1Lftx3I6Lp-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=r6iFlOLraCcFj_-uQ-s078XHG4V4Dxdd4U1h8M1lcGloed82Z0X399A3Nq84ldM7_pzsdnffnWRMbymio9UJX_oLg9QK2fkNvmNG4RnOJ2RKx2PFbkesEI-W-N5xH6Gfq_x_rzbexB2WpqmvWp4OWXF1RRvYtbkyVrtR7LZKxghXNN2wy6ASLQf0oLnCdzxMLd0EFRPEbcAgpiNBvQc9Usvpa8No7J9g5HGqOYRY2ceurYxaT-vnyiOKmwc8dazIJ2wPFpTmnAoQ7j4_loyxvqXHz7dwhFaiNb_3eR0PNFP4BCGofXj1NGPkbM4hZhrN4jFeQC4Ipg1Lftx3I6Lp-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=UJzU175EV2sjtQ-yVntLON6JAuHpLcOWjDPfKCBbJ7W2l2_m9DH2j3TfvnuOFtCPpi4a4t-CHepiHKfJQd0w5rJ25LOyj6_I2uhh6FzVBcHXNL41OZnhya7ubUASxvyc2uwc3JHaxow9Dr6mgeu6ycf-THghQx5zbIY2V5WAmF3qn7aX3pe8-mj3B5dvZi-XsdZW5SfwLboeoREnjUeV9ki4muxQjcEf17kHJoIbool2vFXmfwrEglHjS1niKhXZee3BaOBclUTNrep8a6kULGCg2BtXS-V3uFeQRqCDhShrZCBOtEVQOlqiKk6r3FoTdkZywtkJrT1iR42Ew4jZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=UJzU175EV2sjtQ-yVntLON6JAuHpLcOWjDPfKCBbJ7W2l2_m9DH2j3TfvnuOFtCPpi4a4t-CHepiHKfJQd0w5rJ25LOyj6_I2uhh6FzVBcHXNL41OZnhya7ubUASxvyc2uwc3JHaxow9Dr6mgeu6ycf-THghQx5zbIY2V5WAmF3qn7aX3pe8-mj3B5dvZi-XsdZW5SfwLboeoREnjUeV9ki4muxQjcEf17kHJoIbool2vFXmfwrEglHjS1niKhXZee3BaOBclUTNrep8a6kULGCg2BtXS-V3uFeQRqCDhShrZCBOtEVQOlqiKk6r3FoTdkZywtkJrT1iR42Ew4jZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=nNpaKn5wKRaE3KG_Vu61q0sFMkWLBaBSYh7XEjvq7ObXh4zifcPezImIqUneEXUnv2VHZo-4VOZKD44s1TUQt2uPAbzKEvj9kUz9a01_upLvDhOHLw-GjGPoC-OfaT2XzhoP8Blp91-GOefQIcJfS5V2SQ5_LBjlRvacKm9tZsxzOa215ClQXZTxbHqnbsHp8CT-dTRoerYKVxCBKe1DH9vAH7mppfWa6UHInpajHfDlvUciOKBcC3AcaOb9vsZDnsypqf54ctKVsS9j4c_BkBUcv8bQ9ZLHuv5lt0j8AsryKXs7c3aHg7eQKj9I4qIq9l7ob9xFsN4vvICt-kKOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=nNpaKn5wKRaE3KG_Vu61q0sFMkWLBaBSYh7XEjvq7ObXh4zifcPezImIqUneEXUnv2VHZo-4VOZKD44s1TUQt2uPAbzKEvj9kUz9a01_upLvDhOHLw-GjGPoC-OfaT2XzhoP8Blp91-GOefQIcJfS5V2SQ5_LBjlRvacKm9tZsxzOa215ClQXZTxbHqnbsHp8CT-dTRoerYKVxCBKe1DH9vAH7mppfWa6UHInpajHfDlvUciOKBcC3AcaOb9vsZDnsypqf54ctKVsS9j4c_BkBUcv8bQ9ZLHuv5lt0j8AsryKXs7c3aHg7eQKj9I4qIq9l7ob9xFsN4vvICt-kKOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=MhG2gmBS94NwYZ5lUBMRWap4C6SukmPZFSJX5bIABK0_q5J25eVQZbxj2V5z164r3FRfqkKBF7gmqusvl0efTxDy_C3vcNcHTf3QnRGYRyaVaqsUNbbQ2cj5bNGGdCudwXjlPGHIb8kRdQWL7QF285G9fUqDSYoTSB2OccmK0cxzdOEppVllitHwDaUvc6NDT3azgC-1Rk4QcE0nrZSelZv23AFwrqCEv8nkpUIfJXU6RAwmJa9I3BV9ur4BdY6ZbImBvY9RcyEhL2sj7HNKaz63xwselfL4UQiWc_vfcTHHttRPuCuAAlbsklj2l-ikSu0x4Feg-aEFG9oJutddhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=MhG2gmBS94NwYZ5lUBMRWap4C6SukmPZFSJX5bIABK0_q5J25eVQZbxj2V5z164r3FRfqkKBF7gmqusvl0efTxDy_C3vcNcHTf3QnRGYRyaVaqsUNbbQ2cj5bNGGdCudwXjlPGHIb8kRdQWL7QF285G9fUqDSYoTSB2OccmK0cxzdOEppVllitHwDaUvc6NDT3azgC-1Rk4QcE0nrZSelZv23AFwrqCEv8nkpUIfJXU6RAwmJa9I3BV9ur4BdY6ZbImBvY9RcyEhL2sj7HNKaz63xwselfL4UQiWc_vfcTHHttRPuCuAAlbsklj2l-ikSu0x4Feg-aEFG9oJutddhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO94XZQztmrbUyV4NNXbClndosYWFep7AC6nj2XJbmcanpNlnY0L0UmHR0UQfTFPH4M3PPEjTSFHRrmZ59kGdizIpQMXoDekSU2P9POU3N0mViJYU7G2kGZZvReHaMnTYLgf98_ghXASjt6UeysolarBVGHXishYZisaMj9sfVAp7a9Jy9KWGpRLC21SIoDFkoflKMjwoylJG1mRSrqHJmqlwfIPFXl7a1jqQAbHRVGjRsnPYA2CsDsbjvc71ErmNJqAFpy7CQIUIlMcg7DcfRdkKeY-mgyyGoQDiFI7KrLAn4-BVe0gt2Q4Xcgoac0OKvcJdglkp7m_DsvpH9diFN_I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO94XZQztmrbUyV4NNXbClndosYWFep7AC6nj2XJbmcanpNlnY0L0UmHR0UQfTFPH4M3PPEjTSFHRrmZ59kGdizIpQMXoDekSU2P9POU3N0mViJYU7G2kGZZvReHaMnTYLgf98_ghXASjt6UeysolarBVGHXishYZisaMj9sfVAp7a9Jy9KWGpRLC21SIoDFkoflKMjwoylJG1mRSrqHJmqlwfIPFXl7a1jqQAbHRVGjRsnPYA2CsDsbjvc71ErmNJqAFpy7CQIUIlMcg7DcfRdkKeY-mgyyGoQDiFI7KrLAn4-BVe0gt2Q4Xcgoac0OKvcJdglkp7m_DsvpH9diFN_I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8cc6vZdLwnD8noEDwbNuzqKphbBy6otRHOxr7bWoIpdXT1z5roD4olHZQCJq33bfFg8Q63mQXYnMR0Fq5rwyADyI1Z2E2D4VZcKzYTY667Fjx0Jdwszo2IC3uczoDhPSrwQas7ewZV_tKyfIqEyyBHWuEpLKttVi70w8wjxJ0tnwVryULajqAU7jZFPkpe1KQwTcRM1MXHnboUyiLzHsuFv1goTmD-Eap4_w2mG3iVGyHg0rXNKvmTRBFtB_mYYn_O59OoqS60WXRlMZt3xWvbTlPxrK-ctkVvHlZX-K4ww6583yWcYnIGwJIn-EqrKp--zOwPi8HXov8g1JRrMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=p2n84CpZD8WsdVz2o7dq23wLS5gzBQq9J3bu4rWlSJRiArxoyMFH6i1kOMYBUb7qcb3rtoM2ZVdqOFxoHEj9tH9i5K_KtwiYMAmqTyPLFGVXBYEBVQJVg3Ua1aLkrB1tNcof8Dstou0dFoz6P9U3AswPPg-nmDR2uY1yK-Rh4sCjlS0_LiPY9VnxqsPF3PICYRjC4SSfzqU_1iovwsAeZmQYZB1w9hh0iUFPlUqx5jv88yY54GaxW9tie3zhZq61_M00SFQY7RMJmopkTHrvvgrsIKaJxgJ-j9x8xemd92xLIlrXS---wpxBv8GOXMsETl-U0AhkYy9VPi8k75v06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=p2n84CpZD8WsdVz2o7dq23wLS5gzBQq9J3bu4rWlSJRiArxoyMFH6i1kOMYBUb7qcb3rtoM2ZVdqOFxoHEj9tH9i5K_KtwiYMAmqTyPLFGVXBYEBVQJVg3Ua1aLkrB1tNcof8Dstou0dFoz6P9U3AswPPg-nmDR2uY1yK-Rh4sCjlS0_LiPY9VnxqsPF3PICYRjC4SSfzqU_1iovwsAeZmQYZB1w9hh0iUFPlUqx5jv88yY54GaxW9tie3zhZq61_M00SFQY7RMJmopkTHrvvgrsIKaJxgJ-j9x8xemd92xLIlrXS---wpxBv8GOXMsETl-U0AhkYy9VPi8k75v06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxjNHa_wlEtQ188P_OGpQSvOcfwKk_K0xLNCoXvj_j37aRk-UE5kNPMpygEvqwaRewDj0FgMWptR_Tt8iIMAKvza0w2bish3eO-KGE_jEzGuxZ5bm8R5YeDaN8FR-rAEuVFCIvS8zykqZK5zfcPi7TSooK46Yi87g6wIIdVLAC65w3M9DBm5ADh7K0GMQNBZ2XqhKvOMlv5KE2iYH3uujTMRvIblxOSnQa36u6NJaP0sUMhSHmVeIUMiaHbNMbVpPKgqP4rkvduC11UuC2L9pE9D3OHehDb6fOmIYPJLDOhwcoMN4MXUkgbTvepXuUTGCuFHkSmKDvuLZLQ-9gACTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeoDOOa0fdIOAJtBaVVvjj8yNxz5zRH11VvdpcbnrdZ2bTCi37nXb99MtoX28kKaICeQbtesNCkBUPj32mNnIcJtZZHupryxOqBbHNcpJYtklnJg8fblCtRzYzCUdwhTpMmPHYe6uYSXDAJeOXAaX_SuNKY9hsyZY4_xE2AI6G5vSlnNNvJVPHLR687LM1R92n2MbHKbxpdvmaW2lbMheJI4_O8sbtOqCiAp7F7saeDvMCFrdTr_QNL0keAZR0cG2QOqJ-E_XvyQpsHyDtriPmNxx1vOAnhxWj-E7DHWMv-cTZ67dO698IbNcsKH6M-19_v3MeV48Z0ANRh31-HU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUIX0ZIPNdGH4ndI3KALXXoTss7nEpjnkZJYi5LXYHIUgFp4LgZkSv4z_v-uQ6HDgM0jEE5XbHBQhyNNR8TahK1KFOjSLj2iCbxLdE0KlKnztqkrUVYtxHUF2A6ggF-WpJPYY81n_fsuby7VmDOVy7EjlwjPuz2gClCsgqC_D3ybA9JYzEsHNB7BE06hRBwZ1YVxefYYTitVLDrBXFb88UydVKSTz7PAru_UaQBAojUSbzBE3KCdyEZUfYGhbd51MslwqyjkRhRgClC41kSkcABpiLVSsy0rDaerzeGE4n0AhTa2xz11v_h2m58oseamv48IwYXFMQCUptei8QvYzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=jPEJpMzEjVV8IW-wwXvEaVUxmXpoWWRd8lflmPM9S7nIs_gkIl4e07HWTVN45Y2PdtRenELC37UHJ0rIbwqMFVf1DKT5NVCiFVPOaWN6WQJ0uKJDhviaL-fm5gUK0hb4kYOyaCpNkrpSHWfU5tXZJYxGMRY2KCYQL2gLF4ZvIfmKZk5QKEhn-Dc8GjQafpfPbM8W7RslHWHTbjByWtx2tmDtyCdCAIYsbT87liz_gWEBxoEOnVYfJLDOaLs5AoTxZvNqYs82lg3wYCBuGLwkFpGHiWLLiexBwhGHIQNbtuj1Bfms5ed408fOWmOiXmSibYRW5v7P6kgVBKO-YQJkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=jPEJpMzEjVV8IW-wwXvEaVUxmXpoWWRd8lflmPM9S7nIs_gkIl4e07HWTVN45Y2PdtRenELC37UHJ0rIbwqMFVf1DKT5NVCiFVPOaWN6WQJ0uKJDhviaL-fm5gUK0hb4kYOyaCpNkrpSHWfU5tXZJYxGMRY2KCYQL2gLF4ZvIfmKZk5QKEhn-Dc8GjQafpfPbM8W7RslHWHTbjByWtx2tmDtyCdCAIYsbT87liz_gWEBxoEOnVYfJLDOaLs5AoTxZvNqYs82lg3wYCBuGLwkFpGHiWLLiexBwhGHIQNbtuj1Bfms5ed408fOWmOiXmSibYRW5v7P6kgVBKO-YQJkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw73cWFoajj5jMRmUL79KlTz35Puqbmq9o9Ci8JkXM21KVq6TC7P5A6qvEcLLBqE1aRiQ0RHxYYnfWcqUYqYg7OxF0gSorEbRh56fQcwRDmTl0wKMnojntS86xAFfOHX2Vc8ajECOEhHmWCTe1XqFQLzPZVNFkqsPTn9mUu84aW410DlbFJkkpy6NR9U0oMcZm6WkbSzymTYZNXhOHQFVGQ4pJyx1FXzrwp8CnPPd7GkA6zWErmBZ75AQXJKzppTLRqZxugpl5-tBT8Fj2DKLzZgWZ7p7aMzT0PkqsQf6qr-_z-OnybV37ztMDMuKPWgA41kZqvLlDcBmtaT6h69bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGT7Jv8jVEGfcl90rEvFMDQk8WpDEn1ppLEewCXWEp9jwvrpKlDUKxSW2KCIlXvj5SXy-YTTIhGmgIYfJrAeVCgyCELUAh0JE3Kdc5emuNYLTByqmNdfO4kw-DP6txf-IOhRVv76hxFcAB3v5z081FBFYIBPnT7JwlPz4foCIcp8Mx1-ro8RVEZaqtmiU_8TRFwJdIXB73KrR76kxxDaEWXCaqz2BaYPpmf8u4aYi7H_LN3wLtzEwfJYCv2rZJnaV-CufYvMJix3BmSwb9hpcd8We64jEDYW8nxsqOVsH3E6q_SgqRVe9lfYdfeVLDTpPPTmgVPEZLIoEZVu1p6qIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-ifiyv8vuBC87CTIc_pPo3dXSRsfHIg8sIewYu_Ll7nu6cWX5s4VcJhOMKg-vUZteqlISivXngnCmc_zxjSTujzogFXlYxezMRS_BFVoq2z6MQk-KP7ZmQDGu167FajBD6uda6jc6Jr4uyUDHyNetQX7r_1N3SVO7LDDNUWWIEUsbOMQNl3-1eYggq4dS4Ai95IDkNER2A3Ky4VhXxZW-CC-9ZWWci9ALZdd8QDU2wQs3PYaN8Rv8yvOxHZs0X4aeL-e31fn6_bGLDkMlLhpm3oTuao0StWCNuDFSYjcyEoK7w-PR8oGIym7-4vsYEryKT8zfxy-7J07fgzvn5ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na5LgtDmjpjyaDL-c-LsRTlOrAZ_YeB3Vt78GVbOaCpOKoX5yM___yzzzP3K5UzIKh5yhgY9yDNZaMRgmI2xD-iTGDu5aDxKZvrDtFnKhIuEsR5pKWIUkbfw-8dEHk4YuTx_-K0ifsCJNihld9WYm_4CGkq83rAyhorJNREB-HynQbHS338555fnE2072prcghRNafbpxieq4P88wzgu4aPbE5-MRjiZU9kWGhcBtMKsT0Fvfcv3NEBi-vi7--m_FlCqznNNnxbOPWJvDtXsuhRniO6m1UYCz7TN1aORUF4AoGrBbRfvBYIE-Uls7L1PUM7t5yjLU-rSQTwE05HFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=OA6gL2TJHdYXKRAhJAdR0SAIzG3w7np9Lg9x7t_ayopdcXegavEQY1_-eXpRMpHGQhT3AwlVkG0QrfPcjsDEq-7OBp2kxufgXEoCpZpNx7RgtxRXKj_X_4SB-DAziAxJYbj02Iw-0MfOa8pvpTVaBmXLSgei0jz3kKy-cY8_DaMAhxB__VPc28rYmz8mSVqgBDHzARmxBvRIuWk_NQk-QR6ekpFOr4WkNb97XFWDctxircMj6xAKxTcGRkQzUslFRoGxYs-29ZWymZiRCRwG3E6t_b8Gie8FpCTFXiQ2qn3mUqtmuTe27UjR0w6Qyj6VYZv7_Nrd-gypq_SJQyqYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=OA6gL2TJHdYXKRAhJAdR0SAIzG3w7np9Lg9x7t_ayopdcXegavEQY1_-eXpRMpHGQhT3AwlVkG0QrfPcjsDEq-7OBp2kxufgXEoCpZpNx7RgtxRXKj_X_4SB-DAziAxJYbj02Iw-0MfOa8pvpTVaBmXLSgei0jz3kKy-cY8_DaMAhxB__VPc28rYmz8mSVqgBDHzARmxBvRIuWk_NQk-QR6ekpFOr4WkNb97XFWDctxircMj6xAKxTcGRkQzUslFRoGxYs-29ZWymZiRCRwG3E6t_b8Gie8FpCTFXiQ2qn3mUqtmuTe27UjR0w6Qyj6VYZv7_Nrd-gypq_SJQyqYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViixAmNRwuJzKW2cVy8Fog5ugdCzoFNs5q4bxQAm8_HtQYColxujEJc-SRHDXgaRRk2GvWrXtL-c3FI150k-WJNAzzX5-N5nzsPGOiYMl3yhCEoyIkJVcMAWBRvx9jY5JchsWrj9-GZqqKcB5zZDwfown6j2bllpnVXr9CZeT9TJArhbhSxgyc3jnmZ83PcZTcgQVCvOc3PnRoN31EjhJ2-x11-mPLNH5UAJ-2h5ys0BlHCOr5HN5pNNqLxrPTYM6hsTEY_nDfv_5LTQCcgNo8sg3EyzAWLi4d1R6b3M8K2Q-PHXgBcRNEU6SA10e_X6nGdLcfBB1Fhh0XroUR8IBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVoVcH2PXN1QZCx8ocsyIgMGdIA5G5CgThA4ysvyExyQV98nTKSIUzuH1CuCia_FrtCQ8uKH4Dns4GV_OgP0ZliGWEzoW6yjIuvOI_HTjtv61P0dikvKHkafBJXsKZ3Gto3l31e9VGulrfO2QolXBkpxt-RRym_e1298GiFUlR3fw7lvNNE6T73FAz-HOPKvjgYlQ-pffd8KD1oBWPkaPx2x-vx4G5rDy3EcCxcj6UDeTaOOJvsWbj6Qp2bcuZjUXLd0JqHW50ivOMsEGPTVk-OQiBaEUrLCnnl8YBtrDF_Xnb85OFrtEs-iV_AZIjRM8hh48_I61MmuB72pC_65Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=eUx7qRm8gzPjV_pqijOqZi3xtgObSV-H19-vq_Z3WvmP8IE8ssWHPSUxeEuLqvF8Kz2alNzs3HKReGaMpInnP_0sqGfF2nN5--ObhyDMVrTz5SEbWwiDXFKEv6LHSk5T_GD0CwWe2GshiZUe4EJHr6jLT18II8uub--xzADMmGMe_V2Pv5E2sTn06NA2g78TpiwEG8mdeUYirUg2yjRKkekDxzSsyEfFKkmuzW9pn6JN_ZQM0JNS5pCHlhjYXlMm3WefPCMU3t-KdRyfg03dn8KKXPBFXso5f7kyIbKJRxxZSepZvhfvPLAhIETBCzxqPrtEP9FEaG_308iRETvUfpXThUTajjEz_-daEVM0MhdtQDEYlYPkvs900XyTqR78Aj7xGcQWh8I-4Yo5doAOO4lvULnp6pmkGHeYSGRhf8YE3DK6bQe3NhKDwb7y81eK90OQJAP4AG2JzfwBDPOa45fyaBdr7mJs8AVnxQVqa3rAcxU-IgKUYRBHj0hHT6xOW-FVQ_kE7dXQR6s7xKzirFCTioXm0r33Y-_syN5uF0_vbryDT0FE406ZQQn_t0Y2ygrJAXZjR5n7RiZO-BS7ejgSBadqQQEB5Lc_qWwRDWOmVCQz8-OuJMJhScnp2vlRWyZbFtml4kDoJYGrWmjGsgXUjpZtu1TYkZvwIu_VO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=eUx7qRm8gzPjV_pqijOqZi3xtgObSV-H19-vq_Z3WvmP8IE8ssWHPSUxeEuLqvF8Kz2alNzs3HKReGaMpInnP_0sqGfF2nN5--ObhyDMVrTz5SEbWwiDXFKEv6LHSk5T_GD0CwWe2GshiZUe4EJHr6jLT18II8uub--xzADMmGMe_V2Pv5E2sTn06NA2g78TpiwEG8mdeUYirUg2yjRKkekDxzSsyEfFKkmuzW9pn6JN_ZQM0JNS5pCHlhjYXlMm3WefPCMU3t-KdRyfg03dn8KKXPBFXso5f7kyIbKJRxxZSepZvhfvPLAhIETBCzxqPrtEP9FEaG_308iRETvUfpXThUTajjEz_-daEVM0MhdtQDEYlYPkvs900XyTqR78Aj7xGcQWh8I-4Yo5doAOO4lvULnp6pmkGHeYSGRhf8YE3DK6bQe3NhKDwb7y81eK90OQJAP4AG2JzfwBDPOa45fyaBdr7mJs8AVnxQVqa3rAcxU-IgKUYRBHj0hHT6xOW-FVQ_kE7dXQR6s7xKzirFCTioXm0r33Y-_syN5uF0_vbryDT0FE406ZQQn_t0Y2ygrJAXZjR5n7RiZO-BS7ejgSBadqQQEB5Lc_qWwRDWOmVCQz8-OuJMJhScnp2vlRWyZbFtml4kDoJYGrWmjGsgXUjpZtu1TYkZvwIu_VO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ACyPWKRK7B_hgvFTzw8aQjKs8JUG0guLpsG-qtZgBANQKpEuXat9lvLVbqiFR3DZgHgHvHJoam9iog-lI9YpEoLdR96H0dcuFQCEqkuhFUwVFMJ7ucVSvDor3SdYOusabLbEG1HccJuCL2EdI1X0jkMCa_E48PZNKxNtDNYFlEu0jhxu0cuPEVe9K1ycRp54vaciKTDC44P2LvrHuO_FeoRnNyKQBN-lsSRppBkaEuPKQGgAyiBd8Y8oeRGF_B0bz7dOQNCX5m8hMtkqn_oztamzWAQf3GhS3EQXMbC6ME7VOtDOrLsOCHzNs-aT5K1xEo8RahOnJvT0LOnb7JZmOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ACyPWKRK7B_hgvFTzw8aQjKs8JUG0guLpsG-qtZgBANQKpEuXat9lvLVbqiFR3DZgHgHvHJoam9iog-lI9YpEoLdR96H0dcuFQCEqkuhFUwVFMJ7ucVSvDor3SdYOusabLbEG1HccJuCL2EdI1X0jkMCa_E48PZNKxNtDNYFlEu0jhxu0cuPEVe9K1ycRp54vaciKTDC44P2LvrHuO_FeoRnNyKQBN-lsSRppBkaEuPKQGgAyiBd8Y8oeRGF_B0bz7dOQNCX5m8hMtkqn_oztamzWAQf3GhS3EQXMbC6ME7VOtDOrLsOCHzNs-aT5K1xEo8RahOnJvT0LOnb7JZmOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WobI-yZ4JmTTM12jOSYyOJnrNzH6hIktVy3jc_uFNdha6VznhWcW36VLe_7RMauCUJgjzb0uDS2BB9MQJci_m6Tv6N-9OLx6gJbuHfD0NfjlBmwPHHOjjv2r9CFC3FmnaF-aSq4VH7RI-xnkuut8dHZTLf9YfiqcF8VZ3rZi6MzwYZnPBaB2haRvIi9E9gaBecunVodUbilpF2Im6dGBkJh8XSFY8UiQDs0xyhQumfW9e9E65vh4xT3bR7HN-dMSNlIHbzwfEjINclccn5wJR2RtcAzWkuDZh2Is2-M6eDc0FhCdL_kuK-ANIC7BpDlbazWoOod13xvANR0M08XhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=F8UL5aQusr60peR2tm8xwKD8wOhvdRk_4zEqhU2fgcTVg0B9LkNUZuXbSHh4m5lA5CDEGQdET00N2Crdx3_rxYayogd8kIgmiNz-_EVVeJ2-AWc_F-BzA4e-F4UsCt7lWkelz6DZ22UKuSDPbyOLfAa0sR0jS4nSFo-DNngeLzhqeNzgd5gT_vL8n4GR0Hh_PukTMRmRbNymGGKqxPHSjojx1J3rwJZ6tnDOQbLRuVOj1ebmJcMdGGTcrKV3Qg9sFpDksSA4oNqXPU9VUhth8up6-vR8TyGr9XC1dhzY60JEjAeiecRuchANZB4eNhzPmocTNe3mytHJRroHYoZS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=F8UL5aQusr60peR2tm8xwKD8wOhvdRk_4zEqhU2fgcTVg0B9LkNUZuXbSHh4m5lA5CDEGQdET00N2Crdx3_rxYayogd8kIgmiNz-_EVVeJ2-AWc_F-BzA4e-F4UsCt7lWkelz6DZ22UKuSDPbyOLfAa0sR0jS4nSFo-DNngeLzhqeNzgd5gT_vL8n4GR0Hh_PukTMRmRbNymGGKqxPHSjojx1J3rwJZ6tnDOQbLRuVOj1ebmJcMdGGTcrKV3Qg9sFpDksSA4oNqXPU9VUhth8up6-vR8TyGr9XC1dhzY60JEjAeiecRuchANZB4eNhzPmocTNe3mytHJRroHYoZS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9fJDN9V8M3-XWWKyyOVtw4mBlyKkye8fnIGtj9pHodqS223hMwELAtKwIvQ-sC38KsfduX2URTSmXJljT-2yJi5aP20zIDQQ7GxseLxpD5ADDL6bY21z7CySa4O0cGh9TNyz9jkF3i8OaOMiTWcGh_DiqYBe8ygr-fnO-XE8tQ-bbdbQMX2jj7Omzuk80ZOHDPWAtl2Kv7Ev6_ShIkdcfG-Gy9HEppOcYtPwuFYKhltJ9hmu0WRnABjcFsYL-YZd9k6BMvlUdWNkZPMbUUP989Ihy4nttOckdggk6rZ6V3DYDGPLZ1QrpbqlBWrljkbJduc_sJA80i9beAx92Dl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=R0PquceLzWltjsqAPuUE_RPe8vGssbbuOoRjH2WC-2LBLDrwgLXClMqygSQnYwDj7KjMe4LPncnuDg_c_M4eZI40a4SXTmYcJiZBzkyqhbf6CpfUgzfxNn3E-GpvmjtH8yAA-R7lvkhIyDwreYxzzUPqtYfDVvq6aCvFz4v71ElyZIwocuTj9Ni4MSIyyXpTk6aqfjVj1B3UcXmDnZmy-TX0wMjd18nP7QniFSjsLjaPgocqMqitldh9joQj1PDG91B3KjozKBYD5ne4KSAfHLxu5wdJE4ees14ALz3ygCDY-owggvUpjFHfH9_GWbdnDxccyJ9UdAzSuefjSNKRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=R0PquceLzWltjsqAPuUE_RPe8vGssbbuOoRjH2WC-2LBLDrwgLXClMqygSQnYwDj7KjMe4LPncnuDg_c_M4eZI40a4SXTmYcJiZBzkyqhbf6CpfUgzfxNn3E-GpvmjtH8yAA-R7lvkhIyDwreYxzzUPqtYfDVvq6aCvFz4v71ElyZIwocuTj9Ni4MSIyyXpTk6aqfjVj1B3UcXmDnZmy-TX0wMjd18nP7QniFSjsLjaPgocqMqitldh9joQj1PDG91B3KjozKBYD5ne4KSAfHLxu5wdJE4ees14ALz3ygCDY-owggvUpjFHfH9_GWbdnDxccyJ9UdAzSuefjSNKRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=DzoFmRBY-D392ciyVzhDJbecDSFoEMt101gUW_F478DfeNRfxQ0bN7-q8XLUVvhZgR0xAfbxNsMCUZGIK-eerahbZT1AJvs5Ku8XBTjFOGDM_25ymlp04Fj9YI4uh0KsvmONozt7qOfhNLE_AlkyGq7mO1MtyHk_V9WyTT4G150DvDD8jptfr0YiP0sUxF0Mljv6jaaOEKdOUnfnBG-7IkH6nKD5yhU6EtvgcS6DSSTp3nwTmWN7Ew68IXkuL-Dn6TBWcAFjmVbSkp78CZ5wmpGHeqMHeBKqndzO6fXljUbJhssNp-kQ3hmr-XRYuOGdHBgfipRBxzyypyViPPbS7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=DzoFmRBY-D392ciyVzhDJbecDSFoEMt101gUW_F478DfeNRfxQ0bN7-q8XLUVvhZgR0xAfbxNsMCUZGIK-eerahbZT1AJvs5Ku8XBTjFOGDM_25ymlp04Fj9YI4uh0KsvmONozt7qOfhNLE_AlkyGq7mO1MtyHk_V9WyTT4G150DvDD8jptfr0YiP0sUxF0Mljv6jaaOEKdOUnfnBG-7IkH6nKD5yhU6EtvgcS6DSSTp3nwTmWN7Ew68IXkuL-Dn6TBWcAFjmVbSkp78CZ5wmpGHeqMHeBKqndzO6fXljUbJhssNp-kQ3hmr-XRYuOGdHBgfipRBxzyypyViPPbS7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HakRX19chjKaeXGQ6MQ2N2qij4xJaFSm4JRiMgjULOXYgow_PvTCcjRpfLtBk6fmfhEy1NXPZk9_DswBeyK1RkHw28nqpRgIH2m9VfbCESpWhANz3r6g9iRCIbjsSZOnjqVOKeBXYKDZCPL8hnLWUcu42Iy-lP6OCgbWQKhW54E6xeP_ZAGF4U-JzmdN-1Q3ncNjogEVcVvvJxJMlo3hga5m4g15DMPk4UL_BHJsJuZVDS2ZYDxSIhxpt-TSuc3SNLG-yFG5i4h-gVvDqQhemeiSil1CdXAphTnq864VDc7P6JxxXa_mSIsDuHodVOAJtwZiXRMEMMzz4ivvujJuXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=NUXFttpQbQ9nqfGi_9-hB7RgbXeN2-FcnW62dJThM3VQXHvW9qIp02s5FZCNuN97-Hv_G8S749SceppnR6-D67btrXqlK99F1ixiD8KTRe7Er5ccUmCvfYKJyF6P1-xz2QGAakLUfYKyFSqnNZ5UxvSzDr_p_7c7uFOL7CZajkzasERBiO1S3829RoO0YvYRoIkVR1ostze1mZTKr2kM4TBBgvA_gQ__alG3pAIKHeB4TVRXHIb__tphpNTFZOoG8n9PF7CqNeUQAZ-_La3Uosthgq8axiTJZwqWIVhY8wcD-PHcnyJJENjgbMUUjBymjRKgLj5eY_0xEe8MfVAwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=NUXFttpQbQ9nqfGi_9-hB7RgbXeN2-FcnW62dJThM3VQXHvW9qIp02s5FZCNuN97-Hv_G8S749SceppnR6-D67btrXqlK99F1ixiD8KTRe7Er5ccUmCvfYKJyF6P1-xz2QGAakLUfYKyFSqnNZ5UxvSzDr_p_7c7uFOL7CZajkzasERBiO1S3829RoO0YvYRoIkVR1ostze1mZTKr2kM4TBBgvA_gQ__alG3pAIKHeB4TVRXHIb__tphpNTFZOoG8n9PF7CqNeUQAZ-_La3Uosthgq8axiTJZwqWIVhY8wcD-PHcnyJJENjgbMUUjBymjRKgLj5eY_0xEe8MfVAwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfgbYzdlzRLnievpNMJQFCsmrcoHR1Y5QlViDBVMA9CzoO9jJPZZUvr1phmyAECXJy4rgcgyGbn9mFN9zPMQbY2u0n6nzJS0yIK4-MAsqVskxY78bgcBy2SbWkyy12MQf4YNl2-QJQZyWau3tUvEsFepZiXkB1tyJ1xXvlpUYw1-LXfezaKlyHrVUkWlGVz21mx5VaIW6xV0RcQqGawtdpx2QvS9aubShib-JVnNI_miU1CExin81OIzgpxPnwgafrwhVzyvQsytAP3cVCN7lGtRQdB6h7UIUKn2m0uNUrgXiNa-aPHOYENVA2El2W1boyLmpaUBLUwYCSSs7fEwcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnTU4G_xEDmhEOyLtpyOMq2_8zH-6ndE0-HuBw02D8bNVNfTOIpcotVqEZ3jtaZgilWLxJmqHbTLd9dJBdnAwH9VpHw2ccBnGOlYW_IJjqPuQMyzrKPaABp66FBdxpHuHq9alBUeh5o2lENEq6xw3bw-Ubq6Cfj0PhVMts9AZ1WX_qhe3Z_0ovbfmZ-k3anCHSxe5Ufpcf4FUMcUHndl4HCHjTV31U1BlUnjoemuY9mhOTFRdpLErXFLsrDaRiiscVpIhgfg1O4sCmj_XH0-3I5Z1ljQp2OSgEXkuBLnnLPi6K4wG6iMUy5fIvn-8kw4oq7cn5ut6APtmbpROYGW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVcTE4xD02AXQ_E6-zHzYod1solvom0CSVuHoYF4N_el6iJtT9oijKkFAo0l3EWYN1j30RTb1DI2vlpPeOGpA2MMA48WB1EikhlRrX6hjvqCM2JHG4jHuJwqQStrr5mY-Sw4_xZVufRmCrbDSOmYXvEgdfAtWVjwzd1UUwtSq4id_MIp4bZ1sAoYrz76BH8Eal71L1pVZm0SpHI4vGu071GbgB9uEzKJJzT52wR3KFOUqSk6bK4_h0Vk5Z5jYIM4KfTREFv8poAQFwqM14gbLvPaWkaIJ7Gc8A_9xTmVTDJmDUT6Jssuvey1v5QaULMMrdfPtj_n224V5Mg0tH10dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSUT04DGTgpPseezbU3i8M4ElVSPpA4gkiKY4I4u3KzBjsEYC1dn9n996gmOmQ7mZo9lHZuQ-1ox3Ioyo43rKjI6Yh35KtFQ-aI6mHgslZnlVZQ4uKg67mS_nFy9N9P0euFp40zjRa1cf8UPs1zJ2wPJmK7phYQzCWb-7Gxu2OPfrgrGCrREniKsveaRhFIscdtYChIRUVG3wpjarP9sDMSdjVV_dOWLjJApV1iWCawRgr8tSbGWgLu6hTT0qL7Ep_OpD5NNGcv6haLy8VB00KIBZsm9MxsO1dKZokfLxk25HgSOSSIUp8YZ9ZeQlIsL-4xRfbIPWYgk5wqqSGPetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcsbLSikWEHWmZ16no6OtqaOHBRuoCkvsFOJAf-B-ymiQhB1EKMsv8ojPWEJVB0ktN3abFXO20ZcEZ6jEWXCN6eZUEHKl-KkMtHl5PKjiP2c9vjWvSWZ8BxDQR7ynM35MK7z2R5--_Wmo73mrMTVnu_Ewt9tUR7VL6I1_-xAzrQ3pkeu9O3L_MmgVezOvzaYgX8ZJ4cD8e02r6Beaw9-C5mWohUUugG6mLLpPvNlTs0ZntF00BhNC1adhIqLO1ZRnNfPWKSIrcBtARmccA-Fts3VTTYzjW7nVbSfW4dndjq6EcJF469D1qABKU1An8esQP37jz_txzvFmj6HQPMcFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElxUQW-C0oj8Hs8sv12VBsO2pROIGe4kX0HDOuvIRYBgXWielh9CwRAyD8d9EAvJwJJSLrEAZkHiiyfrixW2j10wEK2bwDC4sDeHQOFKKxHY_3wwnQ6aETn0LaE2oxdRGfuj-x5rGaK-y8iUX0cFZ1KbrA2xHRjUOqxQmA799DOB0875CUCJV_P2ECZjC_4eUN8U97mNQ6coi0mSgt8qOJKH0W2FjuWIQUWRm-bx0VoJ6LNSouhKIun9laDP6UvfLlketMbOy21yc6QUkvsEyuCYDbab9VPswmvKyHB4l5V0fWKkNoC_Q6fLxfXILneChWRJQc5mTTSz7ablZxhTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=tefwonKOWp9y8Z2EoLHU8lvF2HuTLLYPH9vGjntzakidOp56s9tj47gRw2bX-kLJnudSyOhYvnfS-7OmQmUvtDDeYXasCLq6OxLSgUuQf8S7QPh94pG3HS0-NGYExDA6UkDruxVN_zK59DPz8ZA0F8fMAHtYAOt3NLKhBoyOpgXUEcUg0ffoHwtiWyl4hA7agwvHmUh89w2vDnkLBjkNWcnmTwMlWTNqemtkmYHq3WrqcZRPD-0Zxjgmdz-8VoqSEKTqCr51m6JvDoPywLFwJ6SMFUKT8CU__ZkR5beRENd26-l-s0moCe9E_obxTfbKH4bYrUaQzBFuJHA3Y_-iJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=tefwonKOWp9y8Z2EoLHU8lvF2HuTLLYPH9vGjntzakidOp56s9tj47gRw2bX-kLJnudSyOhYvnfS-7OmQmUvtDDeYXasCLq6OxLSgUuQf8S7QPh94pG3HS0-NGYExDA6UkDruxVN_zK59DPz8ZA0F8fMAHtYAOt3NLKhBoyOpgXUEcUg0ffoHwtiWyl4hA7agwvHmUh89w2vDnkLBjkNWcnmTwMlWTNqemtkmYHq3WrqcZRPD-0Zxjgmdz-8VoqSEKTqCr51m6JvDoPywLFwJ6SMFUKT8CU__ZkR5beRENd26-l-s0moCe9E_obxTfbKH4bYrUaQzBFuJHA3Y_-iJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrGPzWt3DORod7JyNGtTcOXwrwg5zoTYwlz5p6N-0P7dQ3RQXmIKzQwZ14j5VORyrHqgMAEji_1vSWoR-frxMHHsSHXenW8YcoQnxAD6_d0_78b7iSpPuOORtAeV08EsU7B9OSYMK5DhG1MJJlSzNOn2XIi12D8yxTj-LHI8W7_bG2WL2ubqnO805DbHs-HwToO5k5pPClWEpVOTZmdBnpqFMoMRdz5pQlHkL2TiP4rkm99Ik4-8SYU7wIkgHokT4yr_ArDKemk2UVr98UN_VRnuZr1C84GZ_tpg3FODrBxwHnTZ_X5InTSsGLKp3pBHICVlUkXOoYfB2A2H0Irn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQoW5w5GWqjrYQonhHzfUS3dozhu-JMBXpnMHHq8re5U5KEf82EB6qLnpkhGV7qrFJR48qVasJ57RHv-2V0m146H21LQmTLT3IMrpqaYS7lwuMaGtPqudjwZSw4QKS_LPMSNpc0OtuaS3J6fld7L1kONthbgQ29OrW6rVTga4Cp7p_b71mLKMweLegjTcd64mx2Z2PNvk2HjSyuZBRWwuhRPnrKWPMwt-niuAjkvz01YfwYGeIdOiuXhBuC5DpX1wTxeAtHHJTLfHQAOJ4VgRqxr3fA5zO6g1jZXvzILKvMI8HJrfv5isXd1vyvB89jAW3Dd9tQNtecSQllLvykYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abkN7twS93WVsGlKYRYbvsBDx35FeWlrje8h3Ibk9LH1vtHukbbvJydMKq7aHxpj-bspWuJu5h0zhdzlea4hoQoD6QwJnaDpOAiA6cptBKqQzBeaCERL_oL3vRB6rbRRLIO7UA15CrZKyry53bRuJbf-7rrNi569m4yW_qOBCddEwUH4absJNlZWpjb-95HwjL260B3p6pIOyUmDJHmnxJlK53inBsxj3II2O6UyoQLONNi82ycZyl8pDV1oTeXi0x8yzzV0GoYVVgOfptmbv3WDi1bKJ0uwZgTCoVCGEglNtotFcgUclm4r_OUEK4GNQiui1ilRIk_QUxBZUKyXJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLd53I7lhOPzaeeVkwt91ZBCqIiRC4qLVjcHvVlwP7GyV6CJmLa99fl9MgXlj-j5q5HDC6Fb3rzx3I7ybzriz9UMiqC5pMlnf172CG4IaDXaQGXDpIZRzLgyo8RLip0NT3khxov8VwSzJZWNKqzpSEeOF1W1OjLxUio9aP9G6N1tP3eKNk8v15-vBhBpbeCJ0kCe5_ACgTZmfTXSjMttAx7mxrV2npVkPK8fdzNZ8XsMFY6yad60WbtsDArlITYhsrGk249APWY1D29rw3jcpAIFPKpg90b8DLj52XQNpIMnVGDcj6aJbx5g9voCJDWdoOwFsUjdwVihKznnS3iGvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=uiQTYKeHFnCb4ve49sQooXPWoAPaQe2e_y2H0VLnMHIwzQOKxFsFD5qK9PIEozgFZvlBc3oawUAO8vizMSLd3jjRzhixn2H-OoaJBBJAwNMBsr4XaWNjrcH8OgdaJx-7gM-tGE9exmV4J7UagiPG2DhCNa55MPiWcMoh4lmc5koLCIdkOKGjnBnEkumHJg8kqBCJRGBL2ZCb00URMmhaUIDcUJOmH6RZMLg7iXGKdkX3lZBEEMNvS_GaUexAODpYsYBUIVeH6uUd5t5x9WjsXmeaSIDZLvs8tgICDIblqzUAAAxxWq7xXKgZXGUI8Z2Jx3kcxPRlqAI4Qy5gY8ZAsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=uiQTYKeHFnCb4ve49sQooXPWoAPaQe2e_y2H0VLnMHIwzQOKxFsFD5qK9PIEozgFZvlBc3oawUAO8vizMSLd3jjRzhixn2H-OoaJBBJAwNMBsr4XaWNjrcH8OgdaJx-7gM-tGE9exmV4J7UagiPG2DhCNa55MPiWcMoh4lmc5koLCIdkOKGjnBnEkumHJg8kqBCJRGBL2ZCb00URMmhaUIDcUJOmH6RZMLg7iXGKdkX3lZBEEMNvS_GaUexAODpYsYBUIVeH6uUd5t5x9WjsXmeaSIDZLvs8tgICDIblqzUAAAxxWq7xXKgZXGUI8Z2Jx3kcxPRlqAI4Qy5gY8ZAsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESG6ZupeKLsR4KKtOCDGIxqvLITC-gn-ZhLwrqiS95HHOjmfkqJ-f2Z2QEMpvZbBRWkecBppW5Fe7HrM2ZTCBe_dpNBxG7FpwF6fVc97IelbnEAhxOPiDUGpN5buGsjrUdPEde-aw-6aUiKYD5mw76TBzc6Rmw1t5bHyxw_1wIAObY2HtwCWvrhA7x8OCEb3LuMzLLSBtziXf7G19q2s2woZ8tASqEYJqCdDC_m7YkqjNjgKojFvJyOhG3IjKO66On6Y-XFe1I3YJCbT6RITIGDphlATDZncj_1yx9eKdQJC-h7eN3I1e_9-ZKd9RUAFpU-KSt81V7yPew-jhDCNjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLa1oRPxpeoIB2Xp1XN7QemnYYXl4cefA7v14Z0Bar7n_aA23l4wmuhis3pIjxDl6iWb1VAna3e9aUqXyPdx2_W7E3Q4BldgfBUwwdqaFQ26hJHf92IuOC53nl2JwTAGEhXumI6vpByk1kb4TKLjJ4Y3kh9_B0IQMiKojd5HOcIioqZ4cu7-8PFVBDXvTW04Naxk9SOt-GpUW94bEDx1GCQdvNloRQ3VlYwXgx0Fy1Ec0QfMl-GwBn7l2Phdghzc0uUU6N4RHZJk7cgF0X-v2AVduvUi4DlPuBBYTFg3j27dHKQSMfrtx2BGaNfnaY1S6Z4hnG0q8obiYgn-gwbaCA.jpg" alt="photo" loading="lazy"/></div>
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
