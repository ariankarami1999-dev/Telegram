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
<p>@farahmand_alipour • 👥 61.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6tfQKPhuKL7CdW31KComUIyBaa7bJ8OwiMMfQqAZbcyhq6cCsH5TrSZ0Sgt8lGa3iS0jBR03XbzCHz5PavNHdLIL25nYQMLKIoTfFD7-VOxvxzc7t3RS2ogkJZIg3OVuc43VZluIBIjDn9Tsn8E7RuifBlIrYoY_tv1PqHSWEU_RemvhLV_2VDsfYs_Hq7KbMXMovpeZDnfXT_rDndSKS7PQexYHSZ5UrIDkaeiPAoRdmumOgjDx7h4vvzrz0XJZsbqWxPpBQhuGLKiAUZeLQ2Z0ir2VKf1fBwSDVIi0-wUrbiYhENqwBySZu-04y9oZJqPesSgIppFZoUGmMN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=oT9QEJDJnfpOmPsIwuNTYWc7moBMqcZX9_3i1O7xnuo6Ef_NTWnUUFF2tPRS0uqvB4faJWH9b4yW67oKmgkBNtFdH2ZAgQ52k1JsE_ceuhwIiFxUEYfVBHWqkgY4iTjKtDbXwmG7lpwiyNl1Xxpz1NMkobpSH2Tzs9-VeB5GOIXclA9ojeTaNlPaNby-w-t_0m8JRZz0aVPlJAHaciKrxE9o_c7hY6KEh0EE-yxigJ7SXZQHoxwMowuaB269xX4-74p_S_rEfb1sA7qMurCv0KEPVp3QaasJzsoiCOgvYlEpp-zN8EdDvG7aLixmEDLw_02-XJoPWervBiBVS3lsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=oT9QEJDJnfpOmPsIwuNTYWc7moBMqcZX9_3i1O7xnuo6Ef_NTWnUUFF2tPRS0uqvB4faJWH9b4yW67oKmgkBNtFdH2ZAgQ52k1JsE_ceuhwIiFxUEYfVBHWqkgY4iTjKtDbXwmG7lpwiyNl1Xxpz1NMkobpSH2Tzs9-VeB5GOIXclA9ojeTaNlPaNby-w-t_0m8JRZz0aVPlJAHaciKrxE9o_c7hY6KEh0EE-yxigJ7SXZQHoxwMowuaB269xX4-74p_S_rEfb1sA7qMurCv0KEPVp3QaasJzsoiCOgvYlEpp-zN8EdDvG7aLixmEDLw_02-XJoPWervBiBVS3lsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=ltQjT853LBuWONDabHwQ3sJqRo1bySuAns4RjSrAY6Hnglm7csImulUBw40ks7ZsSpPjQzg3Wz17W6rgWnXiPHCNvmuJBN3sMMV2KLmsBxyE92fRV8TJnCAbjw8eyV3Ob1nTyIK0p7HVIs270rjr3_6sojkd3ACV0DX3aoSJnB7CPKKZEv0eXKx0b63osPNH7U3iQHr97HaKVJGFXL-VtlhlTxMNt-5XWkRm_cfWKDZnpW3hsX_dzmWPBhDTHCmNW4MPYYochnaYgSOj44QCJ3rbckHV0HCwjrI2D8J98GFclcdF8mO_mjf2Zvtg13i3zErOdOz21IDWOAnpUWk24w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=ltQjT853LBuWONDabHwQ3sJqRo1bySuAns4RjSrAY6Hnglm7csImulUBw40ks7ZsSpPjQzg3Wz17W6rgWnXiPHCNvmuJBN3sMMV2KLmsBxyE92fRV8TJnCAbjw8eyV3Ob1nTyIK0p7HVIs270rjr3_6sojkd3ACV0DX3aoSJnB7CPKKZEv0eXKx0b63osPNH7U3iQHr97HaKVJGFXL-VtlhlTxMNt-5XWkRm_cfWKDZnpW3hsX_dzmWPBhDTHCmNW4MPYYochnaYgSOj44QCJ3rbckHV0HCwjrI2D8J98GFclcdF8mO_mjf2Zvtg13i3zErOdOz21IDWOAnpUWk24w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=HJHyeWQ5Wxb-zXk5Afv0Xu8LVGu99oaLtYsM_7s9wIu3Q_0p2dmS8lppHSM6jcP7BsrQHaqEHnlq-QZKjMhwSg6M6d4tm1qW7zx8Kl3c73Dq0B-_rax9PHE1qFQgLRSYwkdp-ndLqMrvQ-MgMw8phesF8_vfkTo1LQdZphOSiZHo4D2lXQFm7uth9MgLefVs-ppEly9-6bWV0cwYVqqEq8iKw-TJDOSZFLVwpFLsm8YQnIGULyWtlfHRucIfELJRJXpBPLJvkEo7yKAzgzKMGX-pM9gNr_xMk6VGitXGM6bfbxvbYVbxO_EtgT-sEqzRjZXnjXunpzUswA9QPjYNBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=HJHyeWQ5Wxb-zXk5Afv0Xu8LVGu99oaLtYsM_7s9wIu3Q_0p2dmS8lppHSM6jcP7BsrQHaqEHnlq-QZKjMhwSg6M6d4tm1qW7zx8Kl3c73Dq0B-_rax9PHE1qFQgLRSYwkdp-ndLqMrvQ-MgMw8phesF8_vfkTo1LQdZphOSiZHo4D2lXQFm7uth9MgLefVs-ppEly9-6bWV0cwYVqqEq8iKw-TJDOSZFLVwpFLsm8YQnIGULyWtlfHRucIfELJRJXpBPLJvkEo7yKAzgzKMGX-pM9gNr_xMk6VGitXGM6bfbxvbYVbxO_EtgT-sEqzRjZXnjXunpzUswA9QPjYNBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vP5tpTb8fMmLV-PsEib4kyXMYH3EqKgtEf3acWWLWBjEGT4psyucrv1BPSAZeZvrSGnANG4zLiY7dvyFP1dP7q8Szzpf-Xb2ztSCBwPn_UBHHyg-BiTf3MYnwLKTe9mjHrAL5RfOnHdAVqPpaz5WpWK4BTyGLxfxiACKQI2QsPAGqa9JK25qSdzJx707BECBEXO3q5kB83lbFTtI8RL-as8am5ONlGS6YULZ_cUzPlLP0Cis40jQ92CkofX0c7Ow-1w2kYbKxJMIDbkPpVAHdSRHIk7V73FvHyQPQyjd25ceniTPaD-1bPrn9EPyLIBjHaE_Dx9l-hDkMYQx0aVN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vP5tpTb8fMmLV-PsEib4kyXMYH3EqKgtEf3acWWLWBjEGT4psyucrv1BPSAZeZvrSGnANG4zLiY7dvyFP1dP7q8Szzpf-Xb2ztSCBwPn_UBHHyg-BiTf3MYnwLKTe9mjHrAL5RfOnHdAVqPpaz5WpWK4BTyGLxfxiACKQI2QsPAGqa9JK25qSdzJx707BECBEXO3q5kB83lbFTtI8RL-as8am5ONlGS6YULZ_cUzPlLP0Cis40jQ92CkofX0c7Ow-1w2kYbKxJMIDbkPpVAHdSRHIk7V73FvHyQPQyjd25ceniTPaD-1bPrn9EPyLIBjHaE_Dx9l-hDkMYQx0aVN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=l1h5sazuFNfnOoLu49V2AMfXdl8hHEwqxJp_KSTJhs-LO_bjHXRPXFg6lNJ7gJ_qxnUTAj-SzJjudv0ufx0uauOlE68_mijOQ7ffKLJT9Kj3YD6T_DN349KZCbOFC9e_FqxOTR3TIMun_8M8R2_fB3UUp5F6cerFHZtJKcxFZt26ZYWNCt0v7L_bgloYMEe5qi-8n35lxTpgzNE0JEcZrV1tgWYS1bOO273xcusxKWC6yEmOnmaV8CY3a_EDJwORbP77BbIz5uSspXQyfudB1pP4vUGdejje4E0tqE6k0yWDvo5s_J2ntIod8pa3ANhzrBCCQOHsNoHHkHL1wO4cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=l1h5sazuFNfnOoLu49V2AMfXdl8hHEwqxJp_KSTJhs-LO_bjHXRPXFg6lNJ7gJ_qxnUTAj-SzJjudv0ufx0uauOlE68_mijOQ7ffKLJT9Kj3YD6T_DN349KZCbOFC9e_FqxOTR3TIMun_8M8R2_fB3UUp5F6cerFHZtJKcxFZt26ZYWNCt0v7L_bgloYMEe5qi-8n35lxTpgzNE0JEcZrV1tgWYS1bOO273xcusxKWC6yEmOnmaV8CY3a_EDJwORbP77BbIz5uSspXQyfudB1pP4vUGdejje4E0tqE6k0yWDvo5s_J2ntIod8pa3ANhzrBCCQOHsNoHHkHL1wO4cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojNf5I7ZKF7nIMQz-AYjyK78gA8WoEkv2ZGVq-kaUEPFBlUUGNiIMm5crcF_j4wsrgOoOabhmx1dP2XkUqTI06wQv9r6XVqgXVMDHe-HQ-xk-sSxqfcD9p3osbaCtDf5LbmtUxRRuH3sGGN3mU-O96Bu6Ibq2uvgPOu4VLWM8u4EKojCZC4b0xnsLzgi1GSFU-D055O6gq3Y0ThdZdKreTqrdfxTz2QZ3J2UcAngVYncjTs7a11lYI2BaMBaaNor5LMR_NbkFpYmuqFo3pYsnq8AigrRikWVGGCEbP3LVnwuCo7rk6zYWjDroAK30ZKGt0J9VI8CVthNKDovPoU3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=jgTpKJYn_rW5qtgYVoGUkt49R6vhgMM9nkKxVsTaB9jpO02cGXbGL2gcjeSBv1PLZFciOa2ThQvzpfhEpGWx_PuHzGiuZlI_ijQCVPSpAMwvoiH3GJrn4a7MGrTjtxJS8w8wOKcdBqCuexmBt0X0oPVnQcn0dhwkCNVb0cdsB-iTr3HruwmDprBpQzevGvEwXr-1x5PPmjUoVW7yX9-7BCwTJiMtYpQt3hv-GYCBQKvGy1FRxEtZ8jP2OgyqSrDZdthApXaayd31KC6aYsbPAVEH2N7uxDaIpHIbZ5U96Cb72VDExkcSW4r420fdxzV-FXYqav_MXJQ5gquL92LATg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=jgTpKJYn_rW5qtgYVoGUkt49R6vhgMM9nkKxVsTaB9jpO02cGXbGL2gcjeSBv1PLZFciOa2ThQvzpfhEpGWx_PuHzGiuZlI_ijQCVPSpAMwvoiH3GJrn4a7MGrTjtxJS8w8wOKcdBqCuexmBt0X0oPVnQcn0dhwkCNVb0cdsB-iTr3HruwmDprBpQzevGvEwXr-1x5PPmjUoVW7yX9-7BCwTJiMtYpQt3hv-GYCBQKvGy1FRxEtZ8jP2OgyqSrDZdthApXaayd31KC6aYsbPAVEH2N7uxDaIpHIbZ5U96Cb72VDExkcSW4r420fdxzV-FXYqav_MXJQ5gquL92LATg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K121sQaLmCH9zrrS8ydu9CQ53mJXOwwyii6GU1LW_Epdii00_VSEvW7LuEdGrJWg4FtfCpX5SwJnBHPRzi7chm2N7936BXM3FlezVz7jJOOpo8mb2TY9U7dYey4YK3C-ecafExacnAgR1lnu_StNsIgcrzwvZL5vVpPDyecP1cmEmS3oSNRQMBStqjKDsXQ9X403rN-MPc-oR5nvS6YgvccS9Bs6UAkXOusTOfycCS45fwr8j6Sw4YPMhWbKFFIOjfgdbRu0fRtoYxeYbrO8rA7Roje0gjijHkXWbvZLcwuGl27gwBRMFHqE-M38Crt0ZHrwFearyPuQeG_cPpxOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=lJdemnxAGH71EGOCfC3LcFa4djtiKmZ8d43RwRfh7q4Q5fIZUUTOG2Dkhnz817dx_TrFq_tH0Vy6Bii8ZmKLipa3nbMN43Ik5BgvUQsLGurKYUGWvDJkLLO8riFlu2pxmXPSFyVw6lEFu5jlt2otx9ZweBzsoiSsHRbNy0xG6FJSYo-8z3ZtW5l6Mrpgl2RJjEIpRXBCDRW6t11f1QRADpDaUILP7_HRi4Uu31p-JKZnFaPkH7KZ7YTXbck5fM5uJel5_qahPY0Uc0InMcsW7F0q6s2J2MLXvY-GGMdRuQ539LW-6wFTuPSsEmX5-e-I3W5nTE2fknLE3jHCWyPG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=lJdemnxAGH71EGOCfC3LcFa4djtiKmZ8d43RwRfh7q4Q5fIZUUTOG2Dkhnz817dx_TrFq_tH0Vy6Bii8ZmKLipa3nbMN43Ik5BgvUQsLGurKYUGWvDJkLLO8riFlu2pxmXPSFyVw6lEFu5jlt2otx9ZweBzsoiSsHRbNy0xG6FJSYo-8z3ZtW5l6Mrpgl2RJjEIpRXBCDRW6t11f1QRADpDaUILP7_HRi4Uu31p-JKZnFaPkH7KZ7YTXbck5fM5uJel5_qahPY0Uc0InMcsW7F0q6s2J2MLXvY-GGMdRuQ539LW-6wFTuPSsEmX5-e-I3W5nTE2fknLE3jHCWyPG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgRCjBQi8chbv40s5KqFCBdsGeDqeRmpOb6OVqtC7uL0PfAihQ-Ec6X44oRpcavgiXYaGnZ84MjBm64BQWsyM_Eh1FjUWLGn_eV2fSWaxl9Lz-XQ0HAfc1-RGB8R-zXG2JVQmftvvQCrKGsA1a0bHhj_cdSnmm3oIz8LJcJKdq8gMDJiEumGOKqBYqHLjifBluc-Zlw6QAU170M8UQUIQApUtp8bID3prLeDcq9OmLOKeu5AQSwLAjBpj2J30thnwuYdn6dmm3ZBCz_cvJw0Fh1joqqU_EhepjEebMHixIS1auU6LkbJ6_4q2LVxMItQKc0eA5g0qBRBRJNLsi25Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-PdQNzgGDXGaC_aHcwcrgfZAGJvbHJu2eGMHY-LVi9QMOHMtTx-c127nyBgJPYg9WASmUuNHPiMvR5AZJduJgKNOYUzsoG43uve9Ho-WnBD-ouoOpPJTFP-1DayS3FLdc_2qcsN_bfsF1y8vHNl3AEXNDcOvF9i7ofGtf0TFTO4P2sgCqXwe8r6BfVCb1gXMZCshvWt91W3pQn2N_p7ziVbpgJzDngqhvoknMXGwINpYHjGhg5ytIaMZ2YB8rxk_YzCe3AmmODHeQ2me5miWdylXmCp1kLU30SgLjuD4DzWBTtHe4g7VS3TFYBTXgEkb5q2w-tRpSMzb1MIDl96JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFRP_al04B__utSLl39bu_A7USz9K5Ge20siNvWYXjC81tSIlLxVHPy5niWUyP3iqcWWy56yfONzbHzCV9XA7r-urhtCjKCus6vOEHgNdO53zfQijAxc3v6mXfsyEO-_2H0-NMdZRtmbT4ASOUzE2Fmq9i2Z9wsVkxkuZMYLQeN2gmvQ-KQp2ZG9un1eUeL1bHw4rxz-vxvTykmGpemZ7YOPML4lY6T3_3NkPRhEwse2qpHBbkAtRmEjpgBFXL8r2xE9iSwrn3vDZLsb1yInEjQ6OrUiVrmDVSQ_OY-cMr3E9qUujwDJocILVPN5Jjd6jx-E6yYylljeEMkGFVgDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5HtCcl9PeaVMEwmXZ24zQ0odQG_KIjgB84w03AsXzayJZBATQMIUXzVCXhwcZLQGqn-drNR_4xfzdCwB4tFPo0etc_iUlsmuaL95WeMOe4RVHhU79l6fbFrTPhYBi8JqrMjUpAau4uRNLs1CH9Kj6203XES0ZMIxg09qkQEkGX4TpqrWauzH_ioM7geNRRNIt-ck4PluYk9lTEatw0u08gJ_a_Cd5xBj9wlsdOOVZQEPTLtiOdgV9c_A8gLfkIvm1sX5ZGau2slfpB2mdyIcotf58-x4zZ7nq-wqflkD-G63jU3MyOslNL4BdtjzYnnfqaTFgLBJ4X_TdEifhOChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a855SWMxoxtc6DyiBDzs3s5KP8HWxYFOtLB3sY26Db2DCKvbZUqyJshfs8ouVsh28XQp_4ZOXwQPCLEhgeLy0trvFcaC_zsOjr3xMNA4oDRg9ZHh7CP53oSw1ytljfj3pK82DzrM98eD6sSWwLmDfciaPN1f6HbpOl_y87FthJmJFa_BolrQDTJgK02un6R6gCLFrKNAilhfPEJ4j9dcWIOMMTR0ui6yNz5xgPlUdA0GDmBTSnvQOHTUQpoyOYe4nofEHDOiflWyAwAF6_PtSGr1Sjc4o78xgqUt-RJhupb7_yfGL_WJ_Ldta9IgrtFErjU9BizmRoWNZ1mutURF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tynDbFAumzgxFsEIOK1pJ2po0TRzcI53FPaBGsXKZNx3eJbG8YCcI2E6WLXWN5-SO3mcNb_CXLeLhztbkJ0FeSGPPt_1s3DZU3sdsBrGdK0nqtyZ5G27L9V55pIkLEPeqt8LNJqnagYArsXS0BogyXQjAdkIX5e0uoUni2gTvYRtRmH0vVG2czliXNndFxJ-bXC-wgLa71yERBDa4xBky0d7Ry3__Ijq1Q59ChZ-plvp2Y1yhNDh94Ozexjbinu2AOHh6d9C-f_thNXe4C3b_2csAGUrKRRS3xWI_xWV0ZvorENS8GX1tfkNb24R9vRA4PYZWWvAxIkwwa_KzOJeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNKhvvp8n-Qt3Zn06wknz9_D8gkdQr5foS-joMwRCm6WhsNSrGfylr-2gYq-vlwfBG694j9UddMhiFQHJcDDUhzoJnEWkviGIWhANVMZ8ab0Bt9eILxmiPN3gsZhHLxPx75jZ3mM0S4E0Dxi8LmzzceWDGU4pX53rdRNJR9EcZJQu-D9k5ywx_OaB1gAzWsFz-J7vjKxsYpIaIBQpdhPve0UbAQSCjUbzdNr1FHYFN49iUch8OxQaD22IpiOsELLvicw0Q-y_tkIAblpmKw5xvNVyLlVFnmwZ47yg4rRxTUByggykR2Bae9LPg3UB5a2ZKJgSotfa9-A9TcomIxvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXoWwWfKl0vswbzoQ9QSO6mP_C2uhxk8HGLJqQ0Ehf2dwVF8FDP6xFMShfANwgJY4glvkty3F8UqQQzPaB_cHKFUJ34ydxwg98KMCDAmBYrxGZstOsSuFv90WOJwmfNOaKPzdC-PmTegr7hu-EZmTlS3bdCM1D8sXPaIoXgiSeN6w-qcGy345P_EnalsQZHCDk3g05TyuPJABfhRdG3IVT6jHVrznHinEFb96tTbVYPjSUWQAN0b4LXTU2pkabG6kuMv7y_p69OgSvvV552JvYpeAA7GeYOz5Mu-SfLhMdfblCSXby2AdY4CcpQTxS5GAXvnH6ssGfMszzFhmEsI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=IVC722QuHUT8AE50cMTcBi1at_OXZLLbyEjxpFYtI96jmYGI-qLBpluLPhjAr4ZS1YybVPyuvPsoKhE9pMWnkqMlgeyzwcxtGOuVfiLJGGmu0yZaLkwjDhZNF1JlB9p7rqM_Ux_Jwby7-HrS7iXvvSkOQLiC-bUoXEuHS590EQsxjAuOs6a6ewapy-yT-2kE9FnrBqEqOuVoxsFYpvnoLiuYWklG73JndVTkOBgjsQn6SoY6u8pNTXn838aqH7Q2bScD1ReahP9zKo7co6ZrV4hHyca4_kgxUQbBpk94B_MdkwN13HrjG89qmbIx7bDa9hHWHY7ob-cUxKUMIiONhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=IVC722QuHUT8AE50cMTcBi1at_OXZLLbyEjxpFYtI96jmYGI-qLBpluLPhjAr4ZS1YybVPyuvPsoKhE9pMWnkqMlgeyzwcxtGOuVfiLJGGmu0yZaLkwjDhZNF1JlB9p7rqM_Ux_Jwby7-HrS7iXvvSkOQLiC-bUoXEuHS590EQsxjAuOs6a6ewapy-yT-2kE9FnrBqEqOuVoxsFYpvnoLiuYWklG73JndVTkOBgjsQn6SoY6u8pNTXn838aqH7Q2bScD1ReahP9zKo7co6ZrV4hHyca4_kgxUQbBpk94B_MdkwN13HrjG89qmbIx7bDa9hHWHY7ob-cUxKUMIiONhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YExFTap8ebSwyXAiFUPEmNHWXZeNF6rb47Na-MrrRZk8LIwcl3yQ9g3U29_I47DTm2fpnemYYDMobqity0k6mGAB8oV5EXgqObLFbLrfpqzwU-0sF0y6cOCdIV5pHRveAp5L4Vuy2pRFJJAjS_A_U5uPIocH-dk9G1eDoP4hJYdyTEDFOHRYfD1rm0wk65fb27YhTFAVJ9TeD1RqUbysvmzphoKAx-UzPsoLesUFp74L2cuaZGGyNWGLKNPnjIXVE-LO-y68P7Zfk5WVOJvdeUTCgKnjg-UiimZ8Pje68CLuGJCsPpSuhRrulGnfyKzDDRC2ebIX0oseR6LYp0cEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8f6HNGrPFzHqARyLjaL3EioFilJj8ueH8Ix7BGT6ip_3W1AOj2C8TCEbpdOcG1FAya0QG3rsFXbiOrFvsOJyG1AUbCDR_2crwRKsSj67WAujV5jL8gy-0dwpwl46uG7KsviNOVpbtMIwClFKOIJogReLR5bI7GQpbRmBcCXQlY4zFJF-lvrB5CeStmmdG5h_MOGekJNyVJdgf4ZO0BgiwEgZC1Cv7HJNpkD0h8NED1aK3Yj1BGE5Cu3z-dJAqUZ8Gvng0ZMT7q5bn5u46WpRWpFMdXMeQ8VXtJuYjQE7EvIY8cNEN3hAEykgo6xbeWxN4eD70-3qSobWA14r58Ybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKCpey-GIRH0FUfYRJOOTAn7g-X0Wh10_cGD1BxxVGVEPCGsMkAOvS1R9PfK6PJQZevVBpoArJF0u43nosc9pgrUSf02nabD1kZfeePUqYc0Nn8M73FkdU_D2GAxRJme5Nh44zV9Mxj5HJnPvka1sv-l2oEtTeiPmVFfHpOg7PwjY_fU1dPVlEVrYC0i5hU0ceT-eGIcorsgQMgpL18eiRfpkSzWSRuayYE-ajuaTZYzgPepOZofZ91NVvUZsJFSwuPuzO00wjQ2VTsgkpehUKyN3UWUNHbCjRu-9UMPUbRFEAYLPyHlQM67r7lKA8SYGk-r0HpLsin4AtV0E0VaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPeJHIbyavXlhOy181SCHshP9x6ny3N506Paus4iN6FK_0tnwT07OCc3YpIeGO3E484U9095i_v2NotvoTMrYYWQT0cIKomjtjUqhEHGR7TkrBYNiHYsvi4bPG1lzCCQP__tjpVofj11-wuJMPQ0FMJn6gmnyUZ8trB4nmBzg805a_TgCzGXmIiOS9vArPG_Tc1cwoFFxMsP-Uzx7jgCkbepPI9jALC2jwYOj0yEZt9rrpgYm_M05sc2rj1HMRDr1pW3I4M-daYmuV_f9zw0ytUknkAX3DsvmqGw6cdw3F5gKukbiJp5knS6SJwabb4OX-5lllxp3jTn4oP6rfwZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oy0p3bnyyBsp4R8-xTKH3XIyxeshPPluwrq1z1NJmmdP94l77jJU05fw3pOaZAPR7SAM3G03Vb212rUxdjRExzhiFnR1QUsAat-Y6WG9mHOAReuJocbO1E1UcSn13Fk6QdUYlKkbE01cwKsITGem5gnX5pIYvofwe7Pxtm9y2Jr9IESU1XNtYUNuqbxXasq7GV0HlOnMYxmTw1N_wbxzbOHiFz7bzPjrSVUFVAwCXGHyl-Ef-UyD7wraENA99R6OscyTIMWO--ymrW84a1TzmhiNJDrlxgdevcxuyuUQqHI9bGfcu430Vjf4VGAZCrDFwmGLqEPtCoLBvDGB1OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=BkFDzDsSH2ePWqJD4ruGgqkuFH6uM2TvOR0SdGk37niTybpqXMSYpkpck6nFXg3pOmbpBrVWGOP34t_EafR0avlv__kji40S-k0xL6UW4OoZsYPSXuXWe7JfPFU-G5AIVH9IeZ-gaow5nq4FfgMZeOVCd81XOqpEIOVbwdKNHygrVV5B_ANdfyaIwobeZ-9rCdP_FQ2TjKN-JEWhudcO1Uz6dA_fVZQte689z314D3g9GPmueXvO147S5EL_-cgvioHSPSUt-cFehK_nLfnJUsuJLa5s8FMuuHUnam5dO1WFuL5QxluqCEJXiB2uerLT8OZ6v9pytqcZ7udiPrJwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=BkFDzDsSH2ePWqJD4ruGgqkuFH6uM2TvOR0SdGk37niTybpqXMSYpkpck6nFXg3pOmbpBrVWGOP34t_EafR0avlv__kji40S-k0xL6UW4OoZsYPSXuXWe7JfPFU-G5AIVH9IeZ-gaow5nq4FfgMZeOVCd81XOqpEIOVbwdKNHygrVV5B_ANdfyaIwobeZ-9rCdP_FQ2TjKN-JEWhudcO1Uz6dA_fVZQte689z314D3g9GPmueXvO147S5EL_-cgvioHSPSUt-cFehK_nLfnJUsuJLa5s8FMuuHUnam5dO1WFuL5QxluqCEJXiB2uerLT8OZ6v9pytqcZ7udiPrJwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shZUL26yurRQSDGL4tNFSfSKnjpBtZEWSgrE7g1LSomuOOByGj9bTXSB4z2xv6DrryCl3NDQpxMPTg4gT40IoRtF6UCNt4AimA_6Bv1oTg4yqKsQUZM6qUu-F8vWV7NIle7L1KMDhuk_TycOuPsot5Kvk11LXgt9MEjHkhlgmFi9WAgO6FvSjCi7cfJ18QaJ0qJDPw8U_OaOtkKMLUfubMlSKXwvOwpJ9dDC2AGn78cDgdM3mEv4V8Mgu5wG89BP0Q9YMuGcu5ExRaRzOL8Jl-5mQh0TFyFqQxTWOfHZ9nA8l4WfZCqbo0dFT-mRG2EAJja4XTR5tU7JjyDPJPY53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Xm-B2P3skRfnrevcqqAZUCnGmHArbgf2cvmzwTGjN2bDBWM9xlc1n1KAmf439MSD8hi_j9iMnJjA4eMy9wKh9GlX0Qs0qRyOf3VgfRXWmflDDzlnrpOmK3tcJSPpVPS5COREJ56YyYYFo3_PklSsO3Xybm2aX9y0ZGGvbap325WFzc0jn_IT9olWgxxJ8aNgyK-exq2v3hODxyoa1dYBJV7TQTXukf4xLNyC7AoQeQTjI4y3wJrszLFytugbtVr9JGtdqzoULzmROtEsckOU5zTi48qi2bxdCed4ULEE5e02wNHyZ8HjtKCoj-8Ki6RmBXvQzXFWLnb6hcXrFrKcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Xm-B2P3skRfnrevcqqAZUCnGmHArbgf2cvmzwTGjN2bDBWM9xlc1n1KAmf439MSD8hi_j9iMnJjA4eMy9wKh9GlX0Qs0qRyOf3VgfRXWmflDDzlnrpOmK3tcJSPpVPS5COREJ56YyYYFo3_PklSsO3Xybm2aX9y0ZGGvbap325WFzc0jn_IT9olWgxxJ8aNgyK-exq2v3hODxyoa1dYBJV7TQTXukf4xLNyC7AoQeQTjI4y3wJrszLFytugbtVr9JGtdqzoULzmROtEsckOU5zTi48qi2bxdCed4ULEE5e02wNHyZ8HjtKCoj-8Ki6RmBXvQzXFWLnb6hcXrFrKcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=EAbltGv31b1E5VFFINoJMuzJOqymqsWTQ6dPmEvoeb_pN4hQWsWNSBrziv3dRuntKZBzkrpWA-sKU8r3EaUI41GXZFFO24MqI4t_1h27255bDwgDXch1htUg_m_f2_NZ0T7EM4HYWwrVPryE_QxuenaceSA72QENEzXsEVtP90l0R8aQkaOGkqc_nLgNf0gGTcH-rIsRPrjq6-lpQyF5t9Wsuw55feprSYISjWnjonBOaS00jtFxcNesT5MRjlm07AG9Y4MyygZoVjPUhwIK1lNV-Bp4kjyjGu2_3CozuWbOO2fPaM5Dov8IqxyGZwSAIunupm9MZorYv7BN23F25g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=EAbltGv31b1E5VFFINoJMuzJOqymqsWTQ6dPmEvoeb_pN4hQWsWNSBrziv3dRuntKZBzkrpWA-sKU8r3EaUI41GXZFFO24MqI4t_1h27255bDwgDXch1htUg_m_f2_NZ0T7EM4HYWwrVPryE_QxuenaceSA72QENEzXsEVtP90l0R8aQkaOGkqc_nLgNf0gGTcH-rIsRPrjq6-lpQyF5t9Wsuw55feprSYISjWnjonBOaS00jtFxcNesT5MRjlm07AG9Y4MyygZoVjPUhwIK1lNV-Bp4kjyjGu2_3CozuWbOO2fPaM5Dov8IqxyGZwSAIunupm9MZorYv7BN23F25g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnGzQaN9Miidjyh2oVOwT4OLVZv7qztwPRPW-Jj1wSP4s0zzyTjLXPF2Ti2QjhYayQQ6gd4uvUSa9LtL3wJEfdpNqYHaA1GDctEa2BELzrWACQI3WgJF-lO1pbMVL1MJq_IXWmuuxDgQktW3tnOzJzy8p2bCXpZA7Kd1lkgQaKXwnzVDAdI8TD0Tk9VbYMW44gjgqKjHKAJ6n7WKRNkho6iZQRkjAzz3CyqRHYA4ZSR1MBjdGAvNi1u3weL1wlSO8jhCQ9QUYxBPRAwnfqRzxFrYTlTxbNaRupYUFXv8MA7ONN5E0tBcEJjgdZ91Ti9_q05-XzCgqDsEblW9Epyx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjqt2ixlqXfdG0TAFMFdO79w9DCTeaYvOhClNm-TuGR7eh0KI_voO-U2IJ9jUCh4sQkdRPpN6kwei7ghjYSW63zfd8lhecsPMaTb5S8QGb6Vcx4u5XpHUQYtHHAkLPLDpuKAIXQiiunoJVF8SixYA5i1h8_RXLQwM5McRsu-CxHGsQNu_ab5f4rX5fI2KnTiW9WJuO3r9p2KOmduVOha-iJz1pVyxXwdh8VTPL8_TJGpgtYGKaOBShGXWlbi677CPBigqWdWDgTvQC2NXtXCRutL9qZj9HI4vdwlB5ZDNpu7CCIqLyaqVQ61Gd9jtlJTD_xXAmb5Nv9n8u86ysmt_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=rg1F4FKnTC9-7SPHqmSd-BHpTPtSc2LcTh2NNUokV33o3Wbodfk9ltaaPHjp32bXaa8nh_5_xhTNJGbpISJ10GXHJsq2i_2GepYiHfdMaF9ClBaEGmg64idVofVkTMfKpGosX7nFotZlPARWCHO4KaJ-wSchN7tXSUrgsszrRv46B_c-SqQ1-tbLYwOhp-0WBGQwNt6m_LYLKgUdyKMNtMFuPxGbwdgpOyAvWCeWPzDCAaw9n_bP1B_4rDCvd1nPmPuIxjbVImAf5sL3F7uveUQZo-pPwyeUYEcpmhO3cdVdt2se-5F3_4qs7QukaRuAxSU2LdpgAtn7HwHDhj1HhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=rg1F4FKnTC9-7SPHqmSd-BHpTPtSc2LcTh2NNUokV33o3Wbodfk9ltaaPHjp32bXaa8nh_5_xhTNJGbpISJ10GXHJsq2i_2GepYiHfdMaF9ClBaEGmg64idVofVkTMfKpGosX7nFotZlPARWCHO4KaJ-wSchN7tXSUrgsszrRv46B_c-SqQ1-tbLYwOhp-0WBGQwNt6m_LYLKgUdyKMNtMFuPxGbwdgpOyAvWCeWPzDCAaw9n_bP1B_4rDCvd1nPmPuIxjbVImAf5sL3F7uveUQZo-pPwyeUYEcpmhO3cdVdt2se-5F3_4qs7QukaRuAxSU2LdpgAtn7HwHDhj1HhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmvymQNwjMuFbwmT0E2H5PSnOeG5q7FcoSA2hxbog0TM3aL8ZCQgR0FUduDwVtEj5H9phH9iG7VqqrbTl0hPyv_pRSram6ZDfWMMPXU63kdOCaFbKdKiii0Rc_AIbXh7Gx1ya6DiufPRftVo2Ir-guuPMYxe2Qa5fdSIMdHg2k-s1OUXKsfES_d6lKN9wKcnBaAKu09i97pGvxxqKphJC3GCyb3huBFbS2dwE_06fOBG7EfDlt_T4RCpM1CD3uBpk93R_ioEQKJ-PORcT2edOjc9R91vMAnVBTbeBRcvVf-O3hd_6-_w8RdK1Y7gpHgJuOd4I3a-MbcC5jVeejO_Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV1oI6-zXf-tRL72gLbY62KfEsX7Ug9H25EwKyhic__izn3I0JGLj6sNWZB1Ah3Q0Zn4MG3DILfkNGpijGhn1I02W8fTiJ1yHeJT7DyrRGARi7ePHCAE8SrPjzK_9aTJYXmGx1EXGjHqTl0IUPxDKwEMtp86t4KmsHQB7m8ukCwvp_Cs9R_0C9Z5UoFUysGLkkT-Pw3Jey0BwPmfzcGZ7oO3hyw-BlOxDNSvuqV8NfHTNlLTLQNnMjqEZ3K3TWkc_u4cUfLpPzjxWyAmKGgrvdwHYnXPtQI4gNQDUfW9RN5iFJ2btfwg2S_knhNRsuxy8rPA98CBr_WaoywtoWLMjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVflJ5X-0D4yqFKu2LkbJ_AYCnqjwBSKlNobxOIBTMMkiR5_9jAlVumGipt04cyD9Eqoop83J-08nnyfpB68p-jYfUQ5Q5iyrRAcjipK_LLeMEE4EM-IPpPrp6ArSapgnNxnlq2zgbr_M5L1gzuNjCVEMZXlBKYotZnF-due4wxuVXDZN3Kn4z9U731dYVa2gqsOk05uM7mSJBf3SvfKIsGxB5UxY0zUXE1efTJvpmDDODiZtMs-IGVzt-Cj1l2Pz1_vUeDKGyWbUwSz-k2zPa_Bl_-tAXRluJz9aIwj2zOaMX_Rg1_qpnKan8gCYcDnQnBiKeexlJhCBO1kceLY-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVC0z7eYpRIudMPvBK_MSECdj7d4A6OFvwWY81IRZHtBM_W58U3i2kKKBdF24WiJVH16kmq6UExzxWHC82GJgrSzcYp09hEZpIdqofW0mDhRpYpIgSnukMOqwS51bMI3Hl-hC5JOg_DbYWPXeAsQ5Tu5OoDBOJAHiZ2RYiDwkteQU1rDyi1A3-cmRuhej_3XOmDR6qE_WUEPAQjjg8iN87o8EQSLaonNIUkTElBfaX-EPaeKkVSAz-fEpmAJWvQahm4S00FPGgkkkkXaiwYc54ak4ZsafaC00r_XRvASiWuluUqnkcs8ZtoRoKjOjBPeUDDsCE_uq27rMHTi_3G4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw8bGYZeFZAhFpCuesQMjFvcpJX_xHi1lUcNMwlj3Od7DZQ5SU8e9PRTLyBHvE2Jm1Y7svjMfZlhzfU1mdgLBKy2j-uNXqO1LfdNpoZNLSQ9UBtbe2boQThzOvD15WyAQHeIdP4iCLHeOfhx7O_ZmAg8QcsrlrX4vlGPYyGsRvE787arme0-HMpAJKxvqtZzoFQzILMijN1IsI2PyGPLhfoKkR-rwIaGy74atFh1QMGr9MQq-cskrjkKBvkyJ0xBPkMrp5SqP3qu9JTy2WORdy5X0im0TDjK9pznuUnJcdqWwks-scU1U14GXL9mTcHUDuhtaumG9XaEDrqvZI1pYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC4WItHwpUng6_lrjTd1HZzkF1lCmKa2ady3bEf1AUtDYRhSmjnshluZZAUq8slkPV3l_CDCMJ-Lh87gyQbjxQmT0HgOutCr590fEtBNqOjP3nJVorWwWSZ6GyTojzvN83IQhJTQaqCEY7y_GnjlnBad3TPTHOv7mj0_0GdJeGhBJ6lwOXOHsiuG9gtppPKm02GWBqMMqW0RfK7YADaRxwE_HxLxab-kwYJpn2JBXcUR0KLk77IfDcllynUY2rdyO8Hvw31wyXtz79xDD4UZFCVIP9X8p16ZKrVw1xrfj6oLys7VCEsZ-Dx_dQsMJVX22E9xNqm5JPPl9i-HL99dOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZjPFr0sqTmHfEsiw83LnVELi1VtQO6NRscdiky7WBGjdUiRASaLVY-lmA99i_Iz6udLjSVZbCNqEPeVOyE-2kIwvx3o6Tji7AwhE6GvvEu_fGsNENROzTMI2ZVy1TUXQyLcRwN9E8WmvP0j4E5VIT4v4xhp69Gy_pwG_rYyYpEfI8GW9vtp8POYdXkt9kEihddEH8FH1TAfOK_KIxvRp_7FLHyEvrrM-kaBBNM499abp4KZJELkpPJdoneHPkabUcWr3PmApfXpaaTCd4f5pppekRYjuzNYvPWLajSbhrfGB8dbzW8o9lBlKJWhZ42yqiZBnuU15cY5vxoRNhv-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCCdS5gYLfBAwbX2-0nvpUbU3a2eVxAE_29sY36BmlSHfpWEy7W6rL3I9GPiPNJZoPDz0FsBht4EQUE5-Lk9wPGi1toXJDvDia0x0iufRbKn8H-62pUtJ3Iq8gBB4IZHdsM8uIKYL5SBdbnbJ8VK9akrlUMb_GAiFlOn20ZfWORfEL-t8UH1sBHyTEED5fLVjVCE9XGCsSdS9ru1dQ4dYAEwDjukN9Cb1dcCc-9VqD2aLOMnI2RFsVy2dJ3wYRtUz9oGWt8CiPRQYtPjWr77b8sc47jPKSZkO4Uwln5jTVCaLUG5aBTaXoJTiqORhi7SomN8p6NGR-6nzy3W-_9oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr74qoH1x7DbKTwflE796qRFRgByfpiOrV_jgghzOzuIny7GemtD70jpfTqwPq-2yzrajBhzUNxB_pZ6lQiMMXbRT9VXt2cE-u5NIrXYXXUDwhhsgAbO7m-TaFljxO6ESrtdzBw7ARb_dGovoiurq9CEKDuTimwTD420gJKpx568eO8qQsRUhdMb6SukKYL9PTxUIkFzTsX5QP7GwfIivM50WLX2X96A8pdRBBduJK2mSKE8HM1ssDUrBBB6FEXeJcryMRZi-_Gpq_7XGwEa2k84Otv64k5Z7P9XGiHj_zfTaaPNuuxyWKTOSMAp06sRDPqmKRZYTGDYzivGT9-jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoiUqsFXmVTB3u51yiUsRdL5OF8diI8v8Odmhv3_b--Nl_2Slk-EgT7BiTX-aH1SK6q4ThgWG3jUs70hwAOGhplwWUgsRzHaA_5C0HMxPWTLTzBZjnucerOoLe25qf8yMwxqfpU18fDEzivlaolTQaQfFCXDr8wzgrGBsf5M1S7CG_WU6JS3dxGLrOT5WLgUDiyNPPo_e-fQTx49Mj0_iHDJfw3RwfXooB81Qz1ddSGoh3JjNWRcxgH5KR4uTxiL8fOdZbrLYmhQsGvcPWBeKuXpVlq0PtQmImle2dQYy0Yh6JXt6l7MdnIuIYqFR8JwjcknZolUNUxur2eRSHESig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n90IGNKmd6Ah9uPhFQncNT3zV67QD3Uht-kYBWqtSuLHqOYBn1JGO-vei8ro5njJkJjli2vF3remsNBkbkI8stwq4tHDuuBQzOrTPbkXRhMsRM1sYsGbLgFoEaZgoQAZvIsqoN2iSWsRB6tmebtcM-rnijgTAOv9S5hBp3uhu8tGyzG5XtnnueyO50jB-4XOrz7TLVuTjktzUxE2zGw4ZOmCYCmf0q3AR0_gYE45J8Wk3BJwOKF1vJJjwTQN-lC9ZZSK_d5uhZDXlGo01L9ATIZlFtilKTt5GXYkL-uVDHaBh7Wp4rNrPlfWYrsHiQKG2klX01w4LTF5T5IJjEX5mg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=SloJgrezGjG_GwuWLMgoR9uaK3zui8JWLzcFNprq4Th3RFqNrHyecqrsyeqjQfBDnQlTvDJEIhP9F0kraweX8pozwIIsNoaQXWcnbJCW4DG6W_wEAnT99-iXLysNdVvJzQRfOqDNbgQkYU0nFH4nmVimJJRmZ7OMLnO862_-WjRM8UAvugrMPHKi28UN_-m2Ndbt4-zGvFzGSAFEQHb8URRs8b9pgy3Bq2kPGHXL4aEc2xBrPZgh7E2-J86EFMgSYiAi1mTG0H2wMHTvCZImO5h0PbvpImFIOezX0Exr9bOgNF27PpoCcaGtxZOmKStneOPA8taZjIyaW-y8IYN5fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=SloJgrezGjG_GwuWLMgoR9uaK3zui8JWLzcFNprq4Th3RFqNrHyecqrsyeqjQfBDnQlTvDJEIhP9F0kraweX8pozwIIsNoaQXWcnbJCW4DG6W_wEAnT99-iXLysNdVvJzQRfOqDNbgQkYU0nFH4nmVimJJRmZ7OMLnO862_-WjRM8UAvugrMPHKi28UN_-m2Ndbt4-zGvFzGSAFEQHb8URRs8b9pgy3Bq2kPGHXL4aEc2xBrPZgh7E2-J86EFMgSYiAi1mTG0H2wMHTvCZImO5h0PbvpImFIOezX0Exr9bOgNF27PpoCcaGtxZOmKStneOPA8taZjIyaW-y8IYN5fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ZLQ0JDhwx0r5MILAISqg2i01gKUKHHTJ6f2ChB346E47vGL0fA7J3GI_k3zvVUX0LK-R4cegH4rb8Y6TwSogM9xVfmlMArvruGOIrvffm8gh9EfAqHAeyrnBOqm3AVv5jic4jLFWtlrOMfZprDHMDDuJMKZgIdvJJ56pap_o05wlUGev4DPXoLycatrs6MMHZwzdKf_D8bmzRvwpL_XOL1U1Bxo8izJaUadBJjY2w2jE6pZiZHVwk2jlwtaHRuZsNhdZTNc5GcE-NgT0Rbl548qM8YmCaSnMls6c7VTP_UQlXV7tqxWLzAf5GXSgwCueIhDQDHBkPaEMvijI8KaYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ZLQ0JDhwx0r5MILAISqg2i01gKUKHHTJ6f2ChB346E47vGL0fA7J3GI_k3zvVUX0LK-R4cegH4rb8Y6TwSogM9xVfmlMArvruGOIrvffm8gh9EfAqHAeyrnBOqm3AVv5jic4jLFWtlrOMfZprDHMDDuJMKZgIdvJJ56pap_o05wlUGev4DPXoLycatrs6MMHZwzdKf_D8bmzRvwpL_XOL1U1Bxo8izJaUadBJjY2w2jE6pZiZHVwk2jlwtaHRuZsNhdZTNc5GcE-NgT0Rbl548qM8YmCaSnMls6c7VTP_UQlXV7tqxWLzAf5GXSgwCueIhDQDHBkPaEMvijI8KaYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNjABxS0FuVJrFi6czzjD0IxDA9PZ8OdOK4kM1J7BVf-xr1Irh_60zE8550e1QMwYCet2oe0xj3jIRM5tisSukCZ1oeh1npMLSohCG9YWhw_nH9UtosoxHgxik38OgIvdZFxLkhQXULeha01rBuWTSETQ8OL2vOtEDUYHbvTd5uW3stmNrKi0tWCx7posKJE7jynBAMpsiViBwnF0kaP9EgMot5l_Bc7IG4Q4jRnIQ13SRQChxFv9giUH5fBRxUEaT3hUkrXY0d9ExQn3FXs6L7edWJy7VKFpZcZB6dU85UU0BOU6WIG5yxHDF2XFamT9sQinRZTbG0aDyblixqc_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c24VjsnpWD65n2yozfOQ-taIxeNiCCCL13NP-xkvWji8gODakigIwI_2qy4bO_pUJ2GM1XOrgCEt5FfN9KUS_yD6AyiKO7xxxaGSe1slksZpJhRNcG6_20p2HwZ87KiF4Rb8Kfm0hsnowV0-XZ_g7jfblqLamTGvewTTMmMrLp5ZV-myiDd3eMlelt7mcZTENhEu9frFieab18hUFqKAZCyTF_n--YhUNP40bIGPV4qin3Ohx5cVxULxoD5s5ndP0nDFBeKXavvjcQYUW5bsrSqsZMii0hPFEp9vIquxsX6J7W19iSt5sxCt1mMENM8I5U-hKdkJGI4hyjhWxUIzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivNUWcCFzX0ZWFaYnxtznlwn27lwp1LRnD7pfs7BLWB2ctqEqsyLmBxTmmHEomvzDb-CJ104O-3PQgsdOJ1jz9e5CQyJZKKkFxN0lo7R2_D9iq5tN3A6UAwFfkCpUlLvZF37OHjGdzW_I5Gy-xXZB8HpjM-zweP_K7z3QIQ-_ZoAFcQhn_NM5JQxzO0dHc2AvwYUamCV9sYpGm3O174B_k8C40wyCUURBbBHh0eOjbyRkzRZx_0FTTk3AxjRv1DoAOR3QqUXoBFlh1DDx8zdNnMB8x7Pu6tpeXV9pR7WJLby981Jdf0WyT1IUYyGoeEE0N3xrnEnC0UyNkrkKMAunQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=AfJ8mHzMMJ8igYSsS6-bMUeEcVbwVmroiSm3000ZxF36g9shbA9ZsEpBgPBI1A_78ULdMkfLwHa8SvnTvWAfS0TmwCT7fISlO9ek67a3Y3-tntrnydXTx3qvQYanHHhyQTWMjWbjHNWnPaAVaEogrTWyQIgDOhJIaMftCunrgajOM70gJdMpFC33pzxv0HPngjYXhe6eFBGnx1LfnU6O2CS57JRXVsi-YP1G6pVyh681nd-aeP9HP1_wVa3phxZci4LvzrfiTNCTqoKur0681bqnmdZ5MC59hZFa_aQEcjoneLrOjtCVD_nGugKhfogFsO3nshwZotUN4PctRlWknQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=AfJ8mHzMMJ8igYSsS6-bMUeEcVbwVmroiSm3000ZxF36g9shbA9ZsEpBgPBI1A_78ULdMkfLwHa8SvnTvWAfS0TmwCT7fISlO9ek67a3Y3-tntrnydXTx3qvQYanHHhyQTWMjWbjHNWnPaAVaEogrTWyQIgDOhJIaMftCunrgajOM70gJdMpFC33pzxv0HPngjYXhe6eFBGnx1LfnU6O2CS57JRXVsi-YP1G6pVyh681nd-aeP9HP1_wVa3phxZci4LvzrfiTNCTqoKur0681bqnmdZ5MC59hZFa_aQEcjoneLrOjtCVD_nGugKhfogFsO3nshwZotUN4PctRlWknQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsoWpiu9BjpgRMx-fehCysjBj4Qdt425Rnh3bdj9gHNuAIIu7JqYbF2NsZ_oxyP36LvczYnEEMG2imwUVbgbYagPV7C9KaCOMpRXC8VLBBNDEL_2nCUbdDQ-ucaX3RFPgYs_3CvzHDTbDFzcTq3Y8mDrLOA0mPPMHtLBjM4EnQ979cOaAenpWmoZpuGn4u64YCKZX98uUjlmEtxIL6bTvXjRWipZSRlD6LdokC-fOZESS0lMRG7RKybmV9J_HC9vClcJ5FAzMzaQllklSuPDh69dqZeG21PVweAWYcU4YoSQnOF6UTspm5aeq9RUbzfjacvzWGftGMmFiNhpMDWQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQnMFxOMIv4hTmd6KzsrS1yxseYF1gyhOg7ptQVgbYkTBEI4B8V1dn4l12sPvhkUDCLKRMYKIu4Zz1gO1ydCEwZ_ZVc-n3-9HKa7tHwq9Zfat7dxdQctGTQR67x58Dmbdso5Ni5EHun2E446VQY1rzSz5hb2BrBmfgfThJ214YciudWzklDEIVcNXK7OI91XDUUjk7dS1lLwqMz9MooYD4b5i7dXoHIKrPvSE9LUJe8YMmqVzIPEpzYgdLOi5p978Za-b77Evaor6tjGOM6gYnw7j_AI4LbBmY-dDj0XDX-wTr9bBPQ2UMrmyf_r9sOdZNWEiQxzKdGlY6C2SOC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
