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
<img src="https://cdn4.telesco.pe/file/Dw1AilgJ_FRxENPIlB6tVWroH28sAouOItMFS3iYOqXJvQy63Nz04bxQLTw6Wceif1q36LCnvqU_A1rGYDKVqsf5D5vB8hDrpBrYgVFlOxpYC_tvlhsc0c_CoEvh9olg5WvX6DRoCDvOD6GPPRFlkiinXnPz2TXK-hc0fagi6n63JKfdVDiiVtRLEEdrCjQan6JBa_sPyAFFqJZohq2-6rrkcH0ckR5W5nhWAFnqOcQgU48kmdq6YZ05jylW8P0Nzf-z7DcQoYVkkq54JDsduY5uh_MUyD6OZjI1SmiXuW7Ra5_zQP6neqJewkL-yfBepjjp9VD_fWBOWGELQKLd8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJWZjkkt8Ja_Q_tVAl1qUhDS-Vg_HFuotmZFcdypKGNJND8dT1FV-RkY-oC8zMT9cebb6CB-OmLwD1RSHLlng7jG3ABcIRbWXCtSDBiphpd1UuW2Agl_m5ZWIOvhMQ_pOmK6Z_R2Ad_RH0ydtXiSq4ckxmrsiFgEJn1MYoXi0xrVIRL2JrLM17kDSgrB4PwaTCBwKP28eEi2JHU-adfc2w-QUB6SfliYHgvt5AbTt_KjG0-MuDBMlwWQEw4e3orVV_MCFzgzNjwfXHIK_n6REprdFr6F0R614vnZt50PWxxYOO1BDD9-Wc7k22Y869qDogeCMxv1s3fHhOY9p54u3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWOuI-5iTFC5hZ4CN0HX6UAg6Vc41eGg9VDE0WsDxzMBHa_-QEOi3XYHf2bZG4KLCPG6vaJUNoBQyRfClIU7Q3SvDTLAKrCY4eu5f4kU_MJJ9NYHMU8meVxYE-y4UACri5QjeTt-AEd5pi6nGGvFLb0N3qd_aDI9emEySbrC7LT4zbOAUhstodqKzqPABp_ITMrdk-eZjl2w9PVSde3UW9yboD3v_bUuAjmTYRq2XRX2gCiJGJE98c2X9yJo-FF2FsUibTJMPznIwpJymyWe-IclXIIyw3noRm9OrTx5z9lvC-SzEJgwQ6Cju4t1Yx4u6CEkF5yDzjFvPRW8wAqN4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vPSguEY9_VSGpVzOwPZWDS_AykLAVPdFRHab8drA4cBje8z4gZm7yLmdsjg4lR8zOFsvpqGvjlkpqZ2-_nIp81p9Gr7MrZFrHSrRMHA4HD-xzttwJ2EApcpTccDYECroF3b9bI2Z5RPsRHqD9BHnq-BJ6Nbe3fTIPLaPR4cUlJkYlFgAzwsCQCIYtizcUDC5oRAEnnAy9yeWUxqQWPoIknAY6fGXMU5XqGn2pQpb2IQXrG52vbvwCyrxIFZhlnk-uEq-wFMjYoQaItXrihoOD_neRs9q-LOSYc674KzbQCTKjSy7rMMn_346Or63KTSDwxXbMID3ckmXeioEeTYfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vPSguEY9_VSGpVzOwPZWDS_AykLAVPdFRHab8drA4cBje8z4gZm7yLmdsjg4lR8zOFsvpqGvjlkpqZ2-_nIp81p9Gr7MrZFrHSrRMHA4HD-xzttwJ2EApcpTccDYECroF3b9bI2Z5RPsRHqD9BHnq-BJ6Nbe3fTIPLaPR4cUlJkYlFgAzwsCQCIYtizcUDC5oRAEnnAy9yeWUxqQWPoIknAY6fGXMU5XqGn2pQpb2IQXrG52vbvwCyrxIFZhlnk-uEq-wFMjYoQaItXrihoOD_neRs9q-LOSYc674KzbQCTKjSy7rMMn_346Or63KTSDwxXbMID3ckmXeioEeTYfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=CcPq70_klJv4o6OJND2XOs5kN1lRxb_6VkxHN34ZrGUH8wvrOWC0CE5QA7rEJB8FXuVR2Qv1KIIqo9bkQpN8mLNdt1uvXVfEFYUexWbdqV4ILyqW_ooAZBlRnylle84aNgPU14j3gxzFHAlkZvE23q1G79hPVbuJZmpiaIJLVlaPXTTrGrg_M5PsycC9lhaI9gKSrzwqBkfjMqlYLVCJCwuOCF72aZFcJFUCa8gozKvhQkHnrh7Fz9vf3ygaO9lHbN8X0djQw56hMKeixvTSA1YDI4_OSWH0B92XUZ_XM2MTtavs-czhRE8YL2CeZ7SPJn4cFpuKCDM-Ak3hnboHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=CcPq70_klJv4o6OJND2XOs5kN1lRxb_6VkxHN34ZrGUH8wvrOWC0CE5QA7rEJB8FXuVR2Qv1KIIqo9bkQpN8mLNdt1uvXVfEFYUexWbdqV4ILyqW_ooAZBlRnylle84aNgPU14j3gxzFHAlkZvE23q1G79hPVbuJZmpiaIJLVlaPXTTrGrg_M5PsycC9lhaI9gKSrzwqBkfjMqlYLVCJCwuOCF72aZFcJFUCa8gozKvhQkHnrh7Fz9vf3ygaO9lHbN8X0djQw56hMKeixvTSA1YDI4_OSWH0B92XUZ_XM2MTtavs-czhRE8YL2CeZ7SPJn4cFpuKCDM-Ak3hnboHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6tfQKPhuKL7CdW31KComUIyBaa7bJ8OwiMMfQqAZbcyhq6cCsH5TrSZ0Sgt8lGa3iS0jBR03XbzCHz5PavNHdLIL25nYQMLKIoTfFD7-VOxvxzc7t3RS2ogkJZIg3OVuc43VZluIBIjDn9Tsn8E7RuifBlIrYoY_tv1PqHSWEU_RemvhLV_2VDsfYs_Hq7KbMXMovpeZDnfXT_rDndSKS7PQexYHSZ5UrIDkaeiPAoRdmumOgjDx7h4vvzrz0XJZsbqWxPpBQhuGLKiAUZeLQ2Z0ir2VKf1fBwSDVIi0-wUrbiYhENqwBySZu-04y9oZJqPesSgIppFZoUGmMN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ieDvUzXc23lKRmLJtLKYIhGNbt4QY4X4yAe2oOD0yzCWlVeojdB5hagbMYs4nU4ZoTzOWdyeZYCBKKoCx3V0Fo_q9ia57kZap-MUpqTs-Y9dXz6n6Du8FXV5is5l9ghNFA7thnYMtK43ParbW8bJ2JxiZq0FFl9z4cefwYvip2xI8qhKapUFld5ncoIgQradKtq1isdEUdcw2JxM6k1YGNSealtZZLAalhd34kG-Kd8Lkr3O7GULmzhv_ILWBW29ISQV2s9unP3VFX1FPRpZNJMnA-6H9fb-cbVVwA0nQ-toKT6BFIstherGq_N458fNNu0wD8xQCs2bYeHrnxi6hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ieDvUzXc23lKRmLJtLKYIhGNbt4QY4X4yAe2oOD0yzCWlVeojdB5hagbMYs4nU4ZoTzOWdyeZYCBKKoCx3V0Fo_q9ia57kZap-MUpqTs-Y9dXz6n6Du8FXV5is5l9ghNFA7thnYMtK43ParbW8bJ2JxiZq0FFl9z4cefwYvip2xI8qhKapUFld5ncoIgQradKtq1isdEUdcw2JxM6k1YGNSealtZZLAalhd34kG-Kd8Lkr3O7GULmzhv_ILWBW29ISQV2s9unP3VFX1FPRpZNJMnA-6H9fb-cbVVwA0nQ-toKT6BFIstherGq_N458fNNu0wD8xQCs2bYeHrnxi6hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=A-wg9iGdavXIKXH-GzzucsFrjgg06Jjpx8mBzToC_oL4F3V01tkNXNWl9dnLwgJoXXA6ChLvj6fLqf5n5ll47EclryC61O6m0hCBcIB8hvAl4r8lQ_stEmIvLQONvudJGzBxKUlacArDGDcpcKS5-3R63_Gr6gBFibEQYi1VBU5vJgWDf5WCCvoXAFklod9qc6blzwxU34_dN2q4nKfbHuDwn0MCjr-RRN6rFoNh9bPxDpfqbbe6s3cwYhbXpPJrJOpugK96QxkU7ACGmeUi4iI0Txnk18VV9mYlIQmbngwWSC_zD36HZpyHO__aWOzwbe671lDv7DPP4DIm_vTzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=YoRJfa8-hh6enTJNW6Fpl9pzZtq_eLNTGXM7DM6KU3SEjM3W6M0XsFxfa0KO9a_b5jl-gMoydEPzffjhkiDd5eTmN0GGocrv1hUJCF5T-4CUDDteDn_0e4Co0Cdq5lPN1n8NAf0C1wDxgeluFYjTKCq9f7OsDuxrRcxeQxVQmLGEJiWLoOkJjCdVoXyqZ_T7lvK_VzuPVtaGLeX_0H57nyXAip_SH67bGqiM4xowtP0H3wjlkDEgBMz9i35dsIOdObWyB95JPlBo-f4m4IfT-_WPriMWAj8FA0TIaf6rNeapAHgMfx7MEk0KGCoN5AJHJU8_pa8VitJ6XG__B_ynIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=YoRJfa8-hh6enTJNW6Fpl9pzZtq_eLNTGXM7DM6KU3SEjM3W6M0XsFxfa0KO9a_b5jl-gMoydEPzffjhkiDd5eTmN0GGocrv1hUJCF5T-4CUDDteDn_0e4Co0Cdq5lPN1n8NAf0C1wDxgeluFYjTKCq9f7OsDuxrRcxeQxVQmLGEJiWLoOkJjCdVoXyqZ_T7lvK_VzuPVtaGLeX_0H57nyXAip_SH67bGqiM4xowtP0H3wjlkDEgBMz9i35dsIOdObWyB95JPlBo-f4m4IfT-_WPriMWAj8FA0TIaf6rNeapAHgMfx7MEk0KGCoN5AJHJU8_pa8VitJ6XG__B_ynIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=vGy21I5eWikfRf7Cexx_1tzN_1pLESg7P4gb3hTPuDvSAhmdsvODwrMy0RraXQG581daWIc0Vv-3OlhDJ3_SOVbO35a7lZF0MW-rST8w3v-A2j3zERCIqx-U5l_6qRv0uWObuIXuwhwzfW-HH5jtCpqYfFnSQq8TvkLxiWMs4QDnHbhg7oWjNSf_GA1nLU2xb1RKyRTFpy_PrhadUl0iZFm3ITNZHqS7_yji4F4fbhthKUdijHDWf-0qRk8xZcb5FDNwUNSoxTxbn-oZMKii5263QvnEJmRP5dTubl_80hta6FLeetLrny5TRhYtTuC-ooQIUQzg8KXN542L4JS7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=vGy21I5eWikfRf7Cexx_1tzN_1pLESg7P4gb3hTPuDvSAhmdsvODwrMy0RraXQG581daWIc0Vv-3OlhDJ3_SOVbO35a7lZF0MW-rST8w3v-A2j3zERCIqx-U5l_6qRv0uWObuIXuwhwzfW-HH5jtCpqYfFnSQq8TvkLxiWMs4QDnHbhg7oWjNSf_GA1nLU2xb1RKyRTFpy_PrhadUl0iZFm3ITNZHqS7_yji4F4fbhthKUdijHDWf-0qRk8xZcb5FDNwUNSoxTxbn-oZMKii5263QvnEJmRP5dTubl_80hta6FLeetLrny5TRhYtTuC-ooQIUQzg8KXN542L4JS7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSNj2xC14Pzq0zvnhcM21jp0LDkh8E7MTWOeBsL5YfZ5kBBmcNmj8GHeYbQwC2SxH8MYWt6XhmInot51UsO0MFtqzkjHNGevOc0XmAVewGu3_pUJsid4jczD2XREzpFfaB2VmI1Mhsou40sf75oiO04baByG9nlndLZBjqVElWUc5gCHwnP6BQBWeKuKDxWoUrhlv3WWp3cq0sBlinH4H3Knl7IV6vZv-0IIuw3agBpzv061aazAjlJ6Jz-1XL3Ii3ZuFQ_kg_RyGeulSi-eqwj14KILeDUlNI4ChBByQHBT0GrUElGCrP1pvdP84nViSqzce_HkEJs3sYGIgR7e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=YT0aEoghVRXlPp-HMX68ytL_tSwyxGJjpF6-9sK0blRfLwy3fzQw2aqaM5jrOenjW9MBOTO4TCTWjuxfJxVzbQi714edaboVJspsoQ0SR2ejf2NmtRfUJ9yH7lTuYjsunU-ATysccg1_KI7JFmrcstUDMqElPg_YrY_XQZtpzUPBWqwq89Xhhv6yZhSK8vTKNX0hWu-plPteo1AXh7sxLxL-qphYEyle6c-5R44Wurc4LlxztNOXaKAZx-iUed2I4U2Va3dn44Y6lOfToOBKUDM0QjTT-Z8t9qXGsAKXl_Tcm6O9xMqjYMZzbH3Cdk2QzOLp1dRXxeKagvHNqCPZig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=YT0aEoghVRXlPp-HMX68ytL_tSwyxGJjpF6-9sK0blRfLwy3fzQw2aqaM5jrOenjW9MBOTO4TCTWjuxfJxVzbQi714edaboVJspsoQ0SR2ejf2NmtRfUJ9yH7lTuYjsunU-ATysccg1_KI7JFmrcstUDMqElPg_YrY_XQZtpzUPBWqwq89Xhhv6yZhSK8vTKNX0hWu-plPteo1AXh7sxLxL-qphYEyle6c-5R44Wurc4LlxztNOXaKAZx-iUed2I4U2Va3dn44Y6lOfToOBKUDM0QjTT-Z8t9qXGsAKXl_Tcm6O9xMqjYMZzbH3Cdk2QzOLp1dRXxeKagvHNqCPZig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuBEblN740rBznwLme7TsjwgDl1QoOUhrrqfpPTWvockOAc0t-P2z0QkJ9z_k-HEGeBWUIOT7lUYDhg5UPN_C9h5Fw6LewmYKBx8Pj9QuYyfMC71_i2GpyAl6QWx6J9cN1D2c3Zlhd0pVRKj5ahnFoDrm0-z-akAE9Gkez62_5TYFEZJetjGIOLxqS7OOSmEztlg816BvkegUbCXN6IQWBI4iKzCKWtyrQiGK684FP6pWHwOocZWl2XErxZEriZEnrV9E4u2k_2ELXgaCDZ0-djuu7T2JcU_HaLLNoe_7-8sGgda4CJSIbuSwsLYlNwxEx5sawNmyKrraE3JZaHtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=pVvhBi3teXwiO9ZsvA6UuG1BJHPAdMeLki-wYhOyR1HsYmksqUYlY9-qXPIkcjqAyEGSmT3sahBv6F-R2pTORtC8D_2J-sLgPau5KmH-bqBDltxi1KRnDA-puFZNU1eR67D0_IcelmlEVFQIG85GQ8hnEuQNyUxVQSbWo_-QEFJXi2pbDrFhqJMFvF2T75i0-7w8PZw43vhulYEaUA76SQSNi6Laxg4MvLOODJzfqiO4-qMWzYAYgpg8SD9ctVjsWe4rlCBMj1uyD0HylMK3kpYCjmCPInWnTOq0Wc46p2IdqbxNMWozB3o68g4_-DnLr1-fSxa3-_ziUpFDnAoD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=pVvhBi3teXwiO9ZsvA6UuG1BJHPAdMeLki-wYhOyR1HsYmksqUYlY9-qXPIkcjqAyEGSmT3sahBv6F-R2pTORtC8D_2J-sLgPau5KmH-bqBDltxi1KRnDA-puFZNU1eR67D0_IcelmlEVFQIG85GQ8hnEuQNyUxVQSbWo_-QEFJXi2pbDrFhqJMFvF2T75i0-7w8PZw43vhulYEaUA76SQSNi6Laxg4MvLOODJzfqiO4-qMWzYAYgpg8SD9ctVjsWe4rlCBMj1uyD0HylMK3kpYCjmCPInWnTOq0Wc46p2IdqbxNMWozB3o68g4_-DnLr1-fSxa3-_ziUpFDnAoD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTT9buKXehTeBTfdNhdPDkbAMDxKMFUGiSKh0AzaO0zbX2bV_3fh9EpfpFsbf-hIfCVz7W5TqPFg5gppwEJKzTHWjWABcV1tgPZfXJUGBxCVNLQyelI4MT5PeT1slQoshg6JmKT-j_SgNGe_ugjcU325LTCDd94AimNnDNmyeqW3cgVcuNnh1zQU3h-hfTeBhRnXXNZjDEiJ-KHTJ2dDLjDS4MuvzJBGc_QRzy4FLNvyFEfn8G-uTmlUK_5nBH1zUDODUHF9OgvBS2F4QP3aDo5aZU_lWDZ4xhyRYnWtPEZw8id2uDSheVxVMJmE0tzhHBSPQlb88bxnIMK8sJ37pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-PdQNzgGDXGaC_aHcwcrgfZAGJvbHJu2eGMHY-LVi9QMOHMtTx-c127nyBgJPYg9WASmUuNHPiMvR5AZJduJgKNOYUzsoG43uve9Ho-WnBD-ouoOpPJTFP-1DayS3FLdc_2qcsN_bfsF1y8vHNl3AEXNDcOvF9i7ofGtf0TFTO4P2sgCqXwe8r6BfVCb1gXMZCshvWt91W3pQn2N_p7ziVbpgJzDngqhvoknMXGwINpYHjGhg5ytIaMZ2YB8rxk_YzCe3AmmODHeQ2me5miWdylXmCp1kLU30SgLjuD4DzWBTtHe4g7VS3TFYBTXgEkb5q2w-tRpSMzb1MIDl96JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRBk47WbH2VV5CCbJYp-iIow2ai5D6MvrjXS9YB5YK5Ax4AWKDDldsYv16s1JdOo50-I7v8v_qQIISj0pNYQlmoZOGvWpB2vSrkc2EBJ19sEy-SgFD2mXRT9Is1zlyIarRfFdR2GmWq4yuCwVv43Zz9tl67pB_mtc8414oI3ntQyzLxV3B1sXWmYm5_rR6nzB2TSDRZokAGT5K_D3OEUDyMPmpkoh1h7S66EpK89BrckFYsZuAYe_2lpYlPoxYTXozziMBIoAGBnSesj80pp_TWbWqspF25GUT9waqBqpHuaxSgch_Hq1LYNNGnh-zwqCbLW6XNTjonjFhkvbS0ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6HY8FlP8mUcAwUpOZAxNImXX_HNfHuQLGLxdw__bjKxp3CWGdVWETAZ6G9ZqwmQDfjgcIbdYKcjKP_6IS3uv67kYCyxAFAG8WQUTX8mEzkGJFxAI4zJpr98hCaDkUge22T8xqafDD8suQh5h3U9k9p8a03LI_6pzobYctlPan3RzwBFrOEiKWuKSMvRnqntMXLq8s0nHd-BltgZX0-PReXxSITjbLPmuXN3eZvywfYGEhMJSCjXuwr77db2svL53mGUq3KWwQ_cVF3P9vWTEj5wJSt-DFWooYJRwE4JCEhiu63K5B54bae9ykcrMmt2O7zJ0ZylDpDzeXNXFYoXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrImxtwiCSJDLgsAuH189wA4kmIb4hjxqEEqiSgI-2dDqWSr256wvyspTgosovJs-mJl5lrgwrsmdFtaQ3b8eKLbdF4UIxZoQv5Fwi3J_yEPdEdKjcjlzwv3BcX6cCmSxjBT5l0U32-ke10GEWPCXfR04M-E1GTnEkmxb-QeeIMW3bKphH8yfLmpgZ6-b44VNFAueteEbp3pKIy8iKX-CRDX143-rAnxiBwKBD6ZwAGWmpyoMBogGcQSagEn49DQlSvo89zHv0zaZPt_ydzuav2kHE2aNgUMq7yxD_V2gTEc1w9IWmldR-vWlm46essf9O3Cpz2TiDHMRI4mihiISg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tynDbFAumzgxFsEIOK1pJ2po0TRzcI53FPaBGsXKZNx3eJbG8YCcI2E6WLXWN5-SO3mcNb_CXLeLhztbkJ0FeSGPPt_1s3DZU3sdsBrGdK0nqtyZ5G27L9V55pIkLEPeqt8LNJqnagYArsXS0BogyXQjAdkIX5e0uoUni2gTvYRtRmH0vVG2czliXNndFxJ-bXC-wgLa71yERBDa4xBky0d7Ry3__Ijq1Q59ChZ-plvp2Y1yhNDh94Ozexjbinu2AOHh6d9C-f_thNXe4C3b_2csAGUrKRRS3xWI_xWV0ZvorENS8GX1tfkNb24R9vRA4PYZWWvAxIkwwa_KzOJeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFgfiaeChvd5w369iBl-nkzsfSRRZbSx3Y09dZWyET0LGdD5dCujrKZ_KdebpdRunTeVUKtNco4HMmOBrrGQ3X8jathNd5Lrhpg3IgWf1tSwWvlrwFDpFduVtHkv6tO_PbGWE1ZBazYmcjJvI4tSv9fFIfki_pkVwvzeIZat2b0JNs0GsMJV3yy6CPDGu9UY3vO7MqUodzidm-DejNx1-zbPYcugK9HrsV69e1Upw-S_sxLNSANwntmOG4yG_6e2Bat1EmY-LHcJK_uQA55RgcyD1FQBzpz9oPYJ15BTEtX4lIi5bmUiH7pP9GpBGT3mc2GYdgeEofkpLPtCIiThZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVUpOIwfGCvOHwvEnLMchqARIao8DZ1ltjovxgSM8kx5P1My3Yyd6VypJOPwfG1XdeVD7K6HNA5bewhrGhOQisiw-ttiEJWW_3934mkR9z6KyK2hhtkCOtaK7dufj9c-8d81U-huNuCtSk7WTyG72I7uGtCV9uBdYmzICa3OXlSpLQwcz52iViDpDsPdMe_FS26zXOOScDUK1G3ocwbHNC5rRgx5HwdPrBq8qNVW5NJi3b1Zp-TyktFLLokFr29BCU0WHzvQIYjRK4rSXP2CO-SVFjY2G4o755bnJwiL49JPW_Ex6wkkYPTW_7NnfpEBBLweMO8HVPKuq_EizKpY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=LjzfeOJ0z2BOVzscfAlmdYj_CSbO2h3yqKfRHNV-FV-nlaZDbvvxOZ4uVYedeIIn1IZxBZAaPD4q75eK1-to-HsAjRQokJDS-yOHAi6xpLsr2Q0A46P5m6F_hA7NZ1OHrJZg5-w-zDCWXQrcCmSYTLv9pMocAPUu-MKtuI1wZgQU638M7zK2x4hgJ7hdFNIfDBYZ5RHGtPwDdwcHI51VfIO1nDY6X8_xFNZzcV0NnycmY9sdLWgi4Kt-M_QrHgHpl_QzHDY1AdCjaDJxmlUiI2KRjQU8k8vucpWbmLfUlrV68_U7C5e3zeP0QHrA3eLFmhTLrXs5feD__VNIXPhPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=LjzfeOJ0z2BOVzscfAlmdYj_CSbO2h3yqKfRHNV-FV-nlaZDbvvxOZ4uVYedeIIn1IZxBZAaPD4q75eK1-to-HsAjRQokJDS-yOHAi6xpLsr2Q0A46P5m6F_hA7NZ1OHrJZg5-w-zDCWXQrcCmSYTLv9pMocAPUu-MKtuI1wZgQU638M7zK2x4hgJ7hdFNIfDBYZ5RHGtPwDdwcHI51VfIO1nDY6X8_xFNZzcV0NnycmY9sdLWgi4Kt-M_QrHgHpl_QzHDY1AdCjaDJxmlUiI2KRjQU8k8vucpWbmLfUlrV68_U7C5e3zeP0QHrA3eLFmhTLrXs5feD__VNIXPhPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiN83OTn7XXLtpqwJrNtaYRKfNS33-ruH2isT2QQ5UjyML6j8qPDrmaOqi_xgI4OyRoV3ffm-ifvS3gW6ULpdiDJPe19vqm9DGHFINESkvLGFMQ85jzlD1hE6-WSSgJBVHiquLVw_dteZ5nCwhaXdhnAMZRuRTV-ltbqZQ8PhWU7FH16ftVyJL5C-NB2kvFgJj-jn07S5tRZVzWIChr6rcdtNkfB9Jh44lW-Tr6w3Kn25Piu9an0efvp30Bd9-R_CfM84bMkR3ETorWgjKtsj02yzjMba0gKnzl5NGrJcepPxW8son7Oyzf8xnnUa_xYhjF8KIRF6qxmbPR2Xb0Zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2RkraEHa9iDtLluVC9ZoxyItZ85yH13KhiOeQO6J7XAUQS0eVko6hfaAUtPw5FyqptrHhWbp4nQnF7ntcY9DwyUf7CGBvWaHy6KN5t1tOxAeyTDeuO_yRbzchuxziQ2tIsCZTFihT-J__-6GZ67HwCMnzCQQdmRezcuowpRfjS6ht-2XHSpHIcVJQcsWYEnwp1szVe9wNJsl6vs2VbG3w5oQf0miUlopeW3u1MaaH-TyFWcRn3Gfu14cY6HkPqyDAoa31Y620rtmmaeJk24GSjxubLaozcbNEo9rt50z0cXuO3jLorjc_AlGHIbmNMt2dOh7HzAnF_48isGoLxCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsqyhi4lp3lWW8LpoMMUt6Ht9i8ModppMgZk3GfiWZ7WQuPtFzz-_3kc6DO8Rq3Jz9M4HLnwJCUJcSooIYh7853UWb43vIHlO2T4nFUhZ9o3k1GJZ0MiOCAYpwle5kI2hPe43AwdihmrHFgHH_i4eYi_c0ooFOg4ma9HRsAoxM9fuZncrt8jiAyM_1sQmQ6IkADZl8KnGqKQr5Kc1oOLlu44X6UCOsrl-nYtGyeWrZoXags6QBFTjyLLh1KwmOt8k-OiEDuDErIx85o9diXTQb-BmI7cqDXMhMGtHFpkW6838AA_N77eIBk9U4fAyU0SaAUzLrvqTDVKshSdbjr6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLbuWivbWY-ixL4azW-3HwmKMquL9tKdwrC303CtdB5eqSG3HD-QuTI77mUTN1fpzumpQVFjS-lXGbXh3r_uI6CtcbEhGpkg5HkWPnVI1v-sm7NSQsZVcaZKvXY8ZW4Ui9esQbZHceyvs5xUjvXjyg7sS_qXvDEZLVdzh6jV-TWW0mPOK5bu6zPtQh0iQlP3bBnvPd_frdq8HAqCAkUjORKx7IAqTw-TEA7yt9ZJ_Wfh2I6ffuSgmIuB0RJnSzVqAlV7sQ8j5TNHPv3qxzYpNjMxLMHHpVYd1EWf2w717JWeKm_0G4hAxldX7iUj9PNNRX6DMifYHmCF0GNQWBrlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0Vca8gdDbpAnw3KgySL_t_U5tvefmzVSW3XhzQ6kgAIdjRDc08pf5xDZzsXJmyDld75PxZyw31xIu2LOOjif-i8miEKYDLpoajYHjFK2XG9VZ1HD2EWZmNTpbDzZdmtR0YPTNkisY7nISfhlXHD0cZw_udGEhWwo5XcWtuAdB9V8PbJRtAG6QNQcpAwZ5v6cCPisJgnlFEN7hlHqNzJFag7WDHksx2ZIZhehQHpw65CdMDxztD23W8xlb1RKPgBdAMcpLX_RUJzVlRNoihRu7GgT01gaffHJB2WwdbmcxsHq-tvlA7wpqg2STHxD5g9z1RcLy3DhsZuORj2r0fSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=kvtZOXIvSElTYRAD0WBiM0mxNtFjLhIIRrYCXdfBWtDxEN3sP5RPvAbAvZQp_55lWa0ozrE0FItqzd-KE1uGr9vnM210n8uNX14EKL_usWcADFd8b6ccJSYzEEv9QIH44KUduwZg5e1aw6MVwphmgS_ELmi8WIqVNjQ7uOd-Na_H1BkcFII5x-1B9BOIKLTovdF27SDz-XAH4xB4JKoCQgfOnlm0u9mcKr4pKRknX-W1F1uHfBhqz2WEegYMZk4QzCJmMxIVsZj7VuRDqmIgiaDj-zEm_DlvZLmXDV2jyFiGRQ0xUr0968hcefUgD_XhH902IciZsmKtiUyoUsONcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=kvtZOXIvSElTYRAD0WBiM0mxNtFjLhIIRrYCXdfBWtDxEN3sP5RPvAbAvZQp_55lWa0ozrE0FItqzd-KE1uGr9vnM210n8uNX14EKL_usWcADFd8b6ccJSYzEEv9QIH44KUduwZg5e1aw6MVwphmgS_ELmi8WIqVNjQ7uOd-Na_H1BkcFII5x-1B9BOIKLTovdF27SDz-XAH4xB4JKoCQgfOnlm0u9mcKr4pKRknX-W1F1uHfBhqz2WEegYMZk4QzCJmMxIVsZj7VuRDqmIgiaDj-zEm_DlvZLmXDV2jyFiGRQ0xUr0968hcefUgD_XhH902IciZsmKtiUyoUsONcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbSzlBnog35GM0Apk1tNNqgFCSOfAESQ3jQ9cXRM0YSyBgUbfqTGZ-gIjNndYRF9bmywaxfdH6OyUoqGRQt4e-J1wxkqjd1-P7ac0XBDF6CncVsLgMnA5b_Nbr7SC_VbQaS9FGX1bdyIrPOBPJ-UPUOU5kEEcKW7dyZKSOdsvbBcYN0wlu2oiFo6vWUGG-G7asmhLHu3_VmJm4-9Vqtvo_wwRKYEqalYw5NbGR8mWsgtDBwHd9QDPyrA8Qo4-A1A5rBkBR5JsdfhUQBeGFGl2r060L1fzPboW0-0iCATVJ0rFF_AFfj-sRR4Izxv7L3E4cssHIiTfYMWPNwqo5JlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=kXxwZcOaHc5SOszYQNm7MDcP8xCiYmQ3GRQIa4MrhmEgUq90wXS59j-6dFkHMHFkJAKzMbam3CkOOLXd3lwYfgJxdr6OeToQVGbZIXBzUlFCagfV9pYfAhpZfsG18PnfTpoTr5QPOqP0tSH_L9RWhr1U_WEEA_-6CYxrfhl9G5FizmvBmS0pgmvR4q9uOhkCo3rSALJhixZOa8qygks9r-yauzDKpwSsGvwTm1IlA_58EwEVnwVhc2JgTa8bBzSQKxNLimMQOyIn7xrdNAf1SufvbskhDGifm_K7BrWTndkUSHGVqqfBTGBLwVVjIKI-fDmubWp63B8xDJ5hdfXOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=kXxwZcOaHc5SOszYQNm7MDcP8xCiYmQ3GRQIa4MrhmEgUq90wXS59j-6dFkHMHFkJAKzMbam3CkOOLXd3lwYfgJxdr6OeToQVGbZIXBzUlFCagfV9pYfAhpZfsG18PnfTpoTr5QPOqP0tSH_L9RWhr1U_WEEA_-6CYxrfhl9G5FizmvBmS0pgmvR4q9uOhkCo3rSALJhixZOa8qygks9r-yauzDKpwSsGvwTm1IlA_58EwEVnwVhc2JgTa8bBzSQKxNLimMQOyIn7xrdNAf1SufvbskhDGifm_K7BrWTndkUSHGVqqfBTGBLwVVjIKI-fDmubWp63B8xDJ5hdfXOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=U601-6QoTHm6NzeqhbjXNp3OAxmAXYW_g4vujcE7V5qqQQfVVp1kFbThmu03M1vjFIzgnlu3qcAecjs2xODLjvCBAfS5vbUzKO7joRAjJ291joEl_9EhM4kyw-OPLVhybzF-7QkS-BM4PYPvWYOVo5UvdKiIo9iMgLhfdZbU9vzkR427L_J22-vJyG_Lhuefjh9bCln8LepaGYxmeKjDYyc5UnrrlxHdH_AFABwJ0R1toEZN0FGkhLVGUI01Yl3f3_ZykePpUkMs7qEe6AZsgagO3syZKCgZDLHhGtqu4hO3buUqGZQVauhFAMQOA6IRtYGC5ewrqhazJz5UzM310g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=U601-6QoTHm6NzeqhbjXNp3OAxmAXYW_g4vujcE7V5qqQQfVVp1kFbThmu03M1vjFIzgnlu3qcAecjs2xODLjvCBAfS5vbUzKO7joRAjJ291joEl_9EhM4kyw-OPLVhybzF-7QkS-BM4PYPvWYOVo5UvdKiIo9iMgLhfdZbU9vzkR427L_J22-vJyG_Lhuefjh9bCln8LepaGYxmeKjDYyc5UnrrlxHdH_AFABwJ0R1toEZN0FGkhLVGUI01Yl3f3_ZykePpUkMs7qEe6AZsgagO3syZKCgZDLHhGtqu4hO3buUqGZQVauhFAMQOA6IRtYGC5ewrqhazJz5UzM310g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX0qDB3xcFarynpc_UiL9O1xCKDv9XweXGug5LEKqF7_IyJWDUWNefa8wzhZYcQmfAu68AV41hWR5z_z_CQ5Xdsw5eQbdjI_amKNnBvc9-5mb8RWTYjzC-86SovY1ExIcNmDfTD2GoUct4eZ_9chgRDek_LTQMHx4zP3ywYGthdg9pQVl35YsyZl9jmWYPFJuC03piyb4Kv9QEoOUCvOlv0MQzEgqlLaCcO6Kt1RMfgLgfhVeC5CHpkkeiMbyIdso1wEak5xfX8Qgc4Wvz1at6bGnYjnGo4eu_KKATU-u-0ij2mRxHuyG3qb9HaJTVaJ-PprPtCjaCcFR73lZVD_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty8aWOROpOWgRasmppvfLTRNiPLDsNGNSyWLTBN0AtC-T8maPk3QLZ7rJKo_-Tdh-3ACdxVanQmk_Tqx-_1g4ZsWAyhLaY4OqF9T3ePijBaTCyqNI2PAsWfbR5CTQzb1wSa3LC_Wjr2SvOORhnr4iIWCcUCxiMpxubRZOy5ITjB-twG212QGb_ZNNHY2DyQ4TqVjcHpDrR9hLR_g66UnTH7oorcfawit_soYHLkDBUp4nnYSKOGLNj906W72sgWu_Vg550ggazg773iw0iiQG-aksR9wFHOrp8eCLWAp1hgUyiyDTxnnx6apsD4lVHTOjJNfc0Czp0TMHUpaQ7jNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=Ip69FNMAy-_HpPoUA5xWprTgkKfLNMrsb-nyfYeF8-2lW-Ov7oQoyF6dSizKEca4SPDYbGjRxje3PsUjY3r-ZriQekyHLts4qDObMmzI45vpESBLhnuTccPCtIrcaowWP54XBPfHWqaVEveqclAOUYNrHUE9PfTD8x_jB7woHfUR4G8iIWBQNOs6oYhmWLbCLyhxAridhK7uknho86tZgLlK7WK7vfnu_5majSOUjFPoKf7CXJiZtj7rUDW2iTdZNzDhKHDgwgqfA3A8iWShdI-YxivcWhMM9DDREGO-a_RfH07VwzPB4DhlXv5EOi0zMXE9jakePCCNcqUXwHlnXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=Ip69FNMAy-_HpPoUA5xWprTgkKfLNMrsb-nyfYeF8-2lW-Ov7oQoyF6dSizKEca4SPDYbGjRxje3PsUjY3r-ZriQekyHLts4qDObMmzI45vpESBLhnuTccPCtIrcaowWP54XBPfHWqaVEveqclAOUYNrHUE9PfTD8x_jB7woHfUR4G8iIWBQNOs6oYhmWLbCLyhxAridhK7uknho86tZgLlK7WK7vfnu_5majSOUjFPoKf7CXJiZtj7rUDW2iTdZNzDhKHDgwgqfA3A8iWShdI-YxivcWhMM9DDREGO-a_RfH07VwzPB4DhlXv5EOi0zMXE9jakePCCNcqUXwHlnXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_a1KYVP0f4SZR3IUzSO1OSBZIdOcD8puH_UDJ6rMDvErSXcjrp_RX7i7GgmQT9IrqGk3r9k-Ih1Se1FPkQU-uHi0mVzYuHuz3wlVUzElgpmaC2ovBeBAwGZmjeCOY9vKoZXarVKbYJf68d9C7fjXzNp1wS1OeQ4iy431i2iyejG-wSVxge59GO7w3KBmm_gUHXYkJjB6UbMXy9G5RSzVgj1UaoRbZm2hx_q4yLUH9BId7ySar43UoNSrEwer55pxqVWEHxuDEjBhPlfBne73FYeDQbAO-pObHDDqhceLyqBtO4ityuU5sfD84bFdRxGmzn9WJcgKAuZtEZpuEe5yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwB5AK-duD7ZRwzb-2o_J07xshhJn2SLOYpNU2G8rXcfIx6R7bW7gxdQkKo4YxL2n0_bx3hQSCT01kV7ZSCn1ArVvW8vekVWnMbEwxBDFdCrQPBjp8lrCIDjCJFQ4Hvy4a0kNoreW1kgBYoD7-yFlhlD9YrC9O8cdXXsaS98xnNQPWg3iDySUxKd5SkOBy1i--aNzNxPdw8vE7GNKQ6MhXGqlbcpMIsvO_6Ub_ZLNsu147UtlPXbb64heKIqX8EZGCSbk5nDVvmGgQPZl7XgTHExUW9J1ATrZbPd_Ixf7vntlkQdp2_UHAXTm7k9CtfseTx5gADbGuoHA8XD_YiNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDpdUqjGh0ehMw5OWjxphZKKb8QTk1eXttAgjvnF1YnqHAKfdLpX3hau216cN2LnbbFN8aqwgagVZr5p0q075_dV-oli4wxkyRliiJmUkljOe75AwNE1eXLJOz9Vnr83buAgj8b1-_4EGt6U2LnTaQYUJAxyLog9cIPnsglfPONo9897ij0DTXnGK-InzSifHnxFi9cdl83Jw5ptLFWZ5TqW_VlfoGrjgKKJIcM2UPNV6_mNoBKFMuR3dFBSI63v4nTXk8PS631brUt5e_aTuV8xKMPy-rz6btL_RnxqWlnXbPQFK_Di2XXDWfXSRKQJsAJSxwyjX2UhpmXm2SldYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bod_ZMmkCo98_tOUisNtKCV-dxX1d7a4nZ5GPebVq-FWtfFO5XWZzZvvStKlQVTTwAfsfPjYG10QK1NWmTWtRURE7NOPD20yjDMrJcjdUJFo513bThGVxDus5kiDdzrOHaeijJV2H2KEOlKx81F6fl1qfG2vtRLRLoOjCv8MGFFIw82zcBa5McCuseoc8koPVu_yWfoTWBNLUPL2aiTEJBl2N8PUY3vWdfzq0k228if5dPFGWgp3OxGrzl4ykHli2l_Z3t_GOxvfzr_oYMwS6mjFvkzY3i0tjjgCXSCbqFl2iQDG6P47Z4YeHFjOeLjit90PyAyEIP0Ebm8tv9ooQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3wtssKCME_stkdz7ngvvdigmJHmwSrP7n9yaXwfuN9ijdt_QL4gurLk-cDvaHoPa1NM0jK1XZFCeykTzDMaV-30VRQ4m00JtcOBh5J9e8uNCvkY_P06F3mzV2B4LLLn6xEpLf3hA6sEaWk2i9Z292M5pUWs5_kZofbWc-OEAjPRLwXwL_MnrKK_rdsI9lUcKSD_4vFDSrwH0CQodjYpZLMsW_JdjS2D87x1RrLLfHcnHpGtWTfj1et8rFEmmINmXVQJlMPRhjefPEjY4YlNPRwzRJaHBAUhDBrq5d9zSyHeWLzU51RNzc8CVDdHekxQxhcUjBx5WXz_nERP6cTUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7Owp_-tnzMGgtqKvr66MGJmdBZckurROKbAl3vOjTyPbar65jzYVGZ4-kbD4P1_TXhansXZlfoP8JyCMGxuxBMqAJ6aPSR6DTLTl5jRdJHMycY-jx0eQ64EtGf5hslENLkHuD6QRHxTpy_QHWD9dJqZ0mEwtrEzIIOdeuSgjVBXQZht9Q0LHtejO2cLxS5w3htouDgl4BX9IL3GLOlGCH-X1-5qhagDBNSdyXtbJbvS7wEftMq8cgYATKO48Ytsxk0lrq1GA117ViKXQ9JJ6SaqoGSH94b7mXSsnSv11NpbBuSHnzzj8IKJEAf4M-Bvb2RVJwoWf_pmV8iAiA28CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3JtLk_VitLhAHoeH8_TYFcSBPlTE4N3uHOU-gDdHCcE5kWJ1-kqnN_Bt9eNWYAM0lTQPChTi_BnBC3WN50gZjv5XaG2UIqCenCu5k7DxU32gHObqMB0HNpav0aVLIvZy3aLauzajUtLd5--LYCBU5GRH05CA20dtHgtmy6_R14lK3vvKkR9PcS67K8Xu7B4QRYltUqcA3HIwvJLVKh6LsJwNUgb5n308ns1ayt6LPb9BvWvYXFv_uFqSKAY6gwHLjdbjfQbr4UJwsS764IPfR7RlBX3Sq-vMjAB3nd6lgCBKNouY8ZUDlHoEiQetl9me-YqAFnHbpM_kiUSNjCB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4c45cSS8MkIy2RxBt1LaTCcRyUvuIUuZcEM4hmUGWsNKG8V2Hfj9DBQHIlurTlt5X5sY4wl8hi_6JQkmwcJ2-VbsrWmBo4fqqAt9LtW23S3l2Hz_vx-KyHgTXpkF-gJkqTytxx7lA5N0HvUpmAkCHLEQIxtDL4ieXSS7bJJNs2bGwoBLmrS0N5xWQgvST6bnsnTawS4GFiqW1Lmfj1zzxfiuCCDAudNfk4kNODxxMU-f6dt3fCyzbQpsUeSdNo1htgvRWmNcNcQFtTmynIxOLTTqaiDJf_XTdGSt2d4u6ypsd7qjRlk-rFwG8GIdoRA5C77eByVc47-yq02v-Z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH1h0Cs7RcB9Z6ktEkkQ0wCQZaOexdd0jViyLjxwEorEzOqvUpARIHMvdPM3jxlzqk0Zg233QKJmoUs4E7lgbzvPcHOQAYRC6jaRjJvqLLQ1JDIurNyA_VuJtvRsKWOVaFwKmlaex4E7lgDWQIcxBmXq7tShoF6R3fdPr6Hb1UGWANh-y_TguDJbwRW0OIvp80RPJ73JS27AZb91WwJvTPwZpoKuV6hw8H8l9-QE2gk7940g2Op-YZ89yBi9ruU7N9vnXYv-DsDoHzZffskz304asQuHxVlwiVyhYhdxwCcubIVS2YDh471FKc3qFJZVYd5Fys-wOfmtizbIYuPYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgWVcelOfkKTgnROWh1iV-xcx4U1eQFUDziZtty1vZ8lcnI9KyCNSAteBVkQQ1T0Vi9P-d_r8JbfYNekqvTnqAvJLGlTc6i8eYWEKdI4sTJSvFcukiE3QCWHa9L44_ns9TCP4lyMqSshqpXCcJBbAuNs6pbNnPQu6vAm5LD75hv7AZtSit93CX2jE7ZtFpLw-R_mQuOCzG9xGUE5oV5BxDIATpJ9MmztQIDLwOLgx1TXcWNTzwFzIlPFdOTT8B64GifaEXcLu9_eN1bKEWL0T20kCLl-gMNHFjDu9KqaVKzrMElrWCny73-M3g1HRQnSq5QGT5izmQsNb_yPkzgSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuMmy89Dfj1k7nHJpHM2nrdtUJexQPCtfUbQxEwI9ckcCJgrTUSp2PuNjzubAEqiexk0-u0VbyDEtKWvheJwUi83-_I8bT79Kf6wwVsZ5U2-2mw8KORY6uEJuTSTftU5do2aEPzH2AiFa_Yey3sIncPiZ06DNFjBadDaLR4uaU6WyPtX-9xbsgeXC2DTX52cDRcgyPjDL9v63eRun0jny45qiYZyhCCilmyK8jSZXNhhJutpfetJ-Q4F1bH9fMMxg67twTe0J_O0MHXyQaeFe8RZ04cvkzsXpBb0bsI0-L03CC6Pm_luk5emYb3Lck24PRYiVRHff0c5DJovZlOquQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=MVBT35F8ZqrtR7Q675c0qSTjG4Dzh-_b-p3KNkqrzb_bLmAbpbdO0JUQXBVTbMsfBmcmMBK04ugmDM50VQDEhr63X2tGiIpzhWeOCMJ3bFQ1go03vohdf3MHbPNlcgncsouVIvi-L-C9gLQSiEes2v7GtCBnG-NKXWyqctWFcGAMqr4eXgO-y_VYUE-OmU7PgK1k6bP3ysvbmH40gxVqc0JsHhuHnsOSsILpn-Xn8mStZdgyTKhab1eXQ-bNpLU_Oq2BP6ZQWHzw8RgbL1QtcKAnHur8fspwsWDpKU7-zFxXbOACYRbsirokRJyehzZRI6cJnf3_2KifWka5AZlTIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=MVBT35F8ZqrtR7Q675c0qSTjG4Dzh-_b-p3KNkqrzb_bLmAbpbdO0JUQXBVTbMsfBmcmMBK04ugmDM50VQDEhr63X2tGiIpzhWeOCMJ3bFQ1go03vohdf3MHbPNlcgncsouVIvi-L-C9gLQSiEes2v7GtCBnG-NKXWyqctWFcGAMqr4eXgO-y_VYUE-OmU7PgK1k6bP3ysvbmH40gxVqc0JsHhuHnsOSsILpn-Xn8mStZdgyTKhab1eXQ-bNpLU_Oq2BP6ZQWHzw8RgbL1QtcKAnHur8fspwsWDpKU7-zFxXbOACYRbsirokRJyehzZRI6cJnf3_2KifWka5AZlTIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=YqJymdKsoElKQpEN-vlLYYjLqr_GJxEBXgZQdA1UB3aG8jM8cz0QaSkbRzf9PXh0-Sl--wAG_3RAP98EjqgWQ4_JqlcZ2JPCLwOWEtXuJ9KuA8X9AJ43XGP8QCpm8Tb35r3Rqfrcz6JcnLsIW4PDqx1ba6X3Cc8QeE0RmGaXLDfpl5vNQWJd5-fQDYG6J4OPJu4tcUCjOjMH0OYr5NA3c51OMc04S7VwCBDBRj3dHszd_UzEA-igKpipT29JgOgx-619xEBLJ29dpLpFS0If0gTnV7Eac9RCkopX5qvUX_jCazKS70yh98XlNGLFLKd-secU2w6WlxGRNMwfwciGnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=YqJymdKsoElKQpEN-vlLYYjLqr_GJxEBXgZQdA1UB3aG8jM8cz0QaSkbRzf9PXh0-Sl--wAG_3RAP98EjqgWQ4_JqlcZ2JPCLwOWEtXuJ9KuA8X9AJ43XGP8QCpm8Tb35r3Rqfrcz6JcnLsIW4PDqx1ba6X3Cc8QeE0RmGaXLDfpl5vNQWJd5-fQDYG6J4OPJu4tcUCjOjMH0OYr5NA3c51OMc04S7VwCBDBRj3dHszd_UzEA-igKpipT29JgOgx-619xEBLJ29dpLpFS0If0gTnV7Eac9RCkopX5qvUX_jCazKS70yh98XlNGLFLKd-secU2w6WlxGRNMwfwciGnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g39QnEdwqdraw-Nzswux1c1MPoio3re5GQrGYJxIOvKMnkPe2LbArCjYV_sBtH5YCUMm4xpiAbU7tOafCGL_ujaIwfa4RURMfxvTAodY90UAx8ENDFP_x0EoilK2HUZmXnSsbaZSgGwumgDVgmzL_lhTlRqwiFruFSW-cWwy9OabL-J9W5xtS_ouFf0JCzLSiLhJXTZtg0f3kE4x1-EIV-EskVoBxhhvra50bBnEm6UYAUOe_g-arY2jqHPmm30-Y-hvFVTirssykoSPCOdeh--IQOew9gCD_h-W1w_GyyWjEn3WdG9aM4q4_8JXcQ0QF9nFRbMzRvcV-Z98SEZAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcqKBGvLRd_EFzvzg0W2EKdC-n5T7PvcawIYuN83XH5anJiznMQcrvOKdnrBjGUTmauuPXYz_jRcdDx71KqgeMZzv_Oh1J6RpnsZ8Uc_YsJtBDjHH4Uqpoaqt5TKF00vLZKdXkfFqPazk1rqMEqRmIvElx0isYEpCyg-wwOEmJgzxcU3zuu7UTzNK0u_-6yjcwUwd1Ft8xeMTSgZC9CRkLwr-TY4Kczj45UqzHM4ss9e_wFGl8jJ0QzN5PVnqFFBd_TpVTxPiv4nchJBuDxhiAOImcLADTJcfSMkD8ymyTXPTdquek7KebxXN0Fhy2_viVWfwHPbODqdQTD9esOGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6tzSry20STlU7R8l5KUrIjdQmJi-VGNl4rgNwh7GeC3xV0PNa0zVl7MibRvPdyAFfYE-J-2oeo7uIyuGoR_3NVm7E5Q4mvPU5bPj8GzB772bjf1uo4VK4P6ZY7xgPcZ-E9GffPxmlSkBAs44GV3ktHO_qJVIAgPfRquJ58yvD5iqA4NPPTKM_5pSpkvxNzr0qZ3ljG5CCPImMA1ZkpD28MvcykC7a3hQQBGt66oi4t9MrVAkiP7chIsLWd6MkTRRxT_sqnOA2IiE3mhPs6D55hsrSQhQ0-GfJVrynLOFtBdB_IPWqD0ja_djQ3O3Y8iifHzldHcQPRmKyB7fxhZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=niRtYNgmPLoJab5dpoLm92ZlerXi24Md9XnWNCmOyCGu47taqdWkGSsGGvo6tKJKwL6b_kxceOjGJpjPTGKJtG-LrsuoFd1n4XychIhlqUgXJmvaj3TLwdRt33emgCE7x4lba-gE8ha2rUzILfHvaX5K1oEO3VDuV6m1lO8eileI24xXO3gQtzi3w8iranlEocSCB0uXjL056nxibI_rS6HFtSEqDC1HRlkM9N644xXM-OXKW8xRvvrOIAIBotGWQyXzNX9Pvgt6uTTMs6MNt8QWkn92FTttyXETO4x-LgMeV6kVRVkg_Ys2HoKNarqjJz63TS-pcHKXKm-Repsbdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=niRtYNgmPLoJab5dpoLm92ZlerXi24Md9XnWNCmOyCGu47taqdWkGSsGGvo6tKJKwL6b_kxceOjGJpjPTGKJtG-LrsuoFd1n4XychIhlqUgXJmvaj3TLwdRt33emgCE7x4lba-gE8ha2rUzILfHvaX5K1oEO3VDuV6m1lO8eileI24xXO3gQtzi3w8iranlEocSCB0uXjL056nxibI_rS6HFtSEqDC1HRlkM9N644xXM-OXKW8xRvvrOIAIBotGWQyXzNX9Pvgt6uTTMs6MNt8QWkn92FTttyXETO4x-LgMeV6kVRVkg_Ys2HoKNarqjJz63TS-pcHKXKm-Repsbdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkMX2BAFgmvicxvCnKWMHm96DhZ-YIf1zudoO2CDhjMfw9d-uC2Ul7TX6gdglz5w52bmmRS5_JspHBFgNppbIo0qLNYjstU0jTJkOiRrRi_K_M2tVHpW55aoh7oEcFnV-_5xEQvuczCBoTmnIIGgCtEgyWNisxhEwoYX9TVpRvaXAhUp21VXVO35xBf0gcFjREwIrsmBSJpe7KF2Lo6TVI8N1xOjwAS-wVR6Ltu2AqWGLSsQa0ltAlxg3Gd3_rtaGyil7O2HUI3y201juDOl2GfRyWHPIIKLHy2ui3z5PZefCKLWSrrJCB9MGmd1LldtwGFVFxAHVN2c_JOh1xGDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZgJERV82BKjGom_cVxefmlu7H83UBWZqV_G7yvHjFoEEYsqVTLitJO3FFuJSJLfxCoT57Z0Xoc5hWMzO1PyIyA_895tUyGIIpUyemPW7kS8781Lup5W7NQunx3n9naPOEcY2hUw_18cd0-DvU_9b2T3THY-oCkSyJqOZlieQJBCD7WB_vml7Yr3F9kK6z7_v8xychMeSnnMiSaQu65Lak93s-yvrJZe82czEatZSkqgDR9qwtQGx7kB6rIs_c9X9uu3e3kVw0hT5KujA-OQARjEWqd02rrtH9rYYsKJ5_7-rJAqqEkxPWwWnk4k6N6Q6zyMCg1-cNtI9KyaR_9J_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
