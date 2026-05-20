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
<img src="https://cdn4.telesco.pe/file/SxKk7R39wYfjwZ54pVylyL9corcp1W6vez6l5Hetd4SH-sTpDgH1RMqihucdgTCFrokAFjTJOV95BPh8sdg7LGplRMc2wRNTlj456rW_pkVKjE5gyZylSGVNPwxxBUPxe65iTfjILCFOweeXQilJMuwnmeBI_KOQG9DzR6Np2nXDvQetYTNoa7hkgbsW90kfCRU5ourEt8mxvDbPGD7wiDP7L7_6dvTmLP-SIT6CqD-7amtmoXAlFMReQurHDRw410nwAV1pHOfy2CNh4yyoR9sKgSAY5Gy_EDYRxHFCSYBUrg6dQ6_gAQGTaj7rXShPuzioJsks04K5npUh8-yhvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE2fAIBXlERRIxNP_ypVuEEMAophK4T00pmS5UhHJ5SWaAQkEf5PnCf9I_JaSvom7uNgagvUUFe0vyHTYylmaigLYTLSEd38cuvXzzMbOy27wFXhVzT-dsjSXGONvViacKZwoZs9NkwRPTcqppoP4aZ-hqZiKBlDWJgBa-TOFYU84625e2YgtD3NS0s0gq1COFfDln7175bUGvjPxLdFI7-rxjcPD8r0DD0eGGuaQNxgf-dO8XkEJ9CsCmc-OhD5VS4Qo9b6p_okRtYYOfhub1Cy77PFQskboIuInms8Iic-wYv58ywA0a9gQlypYRZTvJ8XB5DlOMq-L6X0gEPltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPCc1yKpVOmap01bOdccSEt0yVfbg1tALUPbROUeOmpgJpCH2yF5kKdEmyyYfztD5Hw0XTP-fEnfePF0Ryj0PW5bEVRVawaHa6p725-mKVaL4zsE3f50WVMHhVhYgba-RrgclWsSRTf0e6Z3My2242Ro3wRbnuKDZUrOO8Lpmw3M6Lip2Fqkpano79cCl0oERfEN4G-QA_CDL_N9F7qItHNH6BlIDJigN_3m8J8-lFWEHU1UG7IQ7wSFPPmYA-BDFk2Fy9SpVW2_Upodk8SSZGv08GKA1gpQv6PacEm42q04TGaJFxeh0xt1t2W1fUKg-5b_q3BMwfQaxFLSxGDTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNl5Tfjqilj9PGtk6OD44yOZJq9-PfqplTRmvWxnTsZnkNc4hS--vT87v8cXMNRvFzDMaHORt2kUBPQLoSimcl2D8pupwiq0dHeGAJFbU4xszlQbfSXvGK2TIbV5PL1p3JmS3yJP57vDYo8NIkEM_e3e_gTmfOAJDczEqlagAnmpLypKQPPnJYeoTdg3NYw7UUU3V71srp2dONY-VOZlZBFpaCLnzoKFg2ORT3rL1S_Pg3_obdTI7PH6-GeHIhmtMWErqarfNr9UnD5jPR2ynKY8XH9HmDT6ogScqql45DIFv79x9wFD9JsY_vVPMPCAzj4e8pQviUmiJqQKOyU5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuJ_odOrLtzR7yQCI0BGLislu4h3tvQZiz-fENELOLcbjl8JwNS6uk2ruMvNg3QmZYW-5PvrrMaXwnKESkrRbJECKPGPRUfXTghfrrSxKGJFya0WMno1uC5AY73-LinCnMCHNernYjjhSvWVWJjYGmlAANBdoyGIwuBKHus8H20cwAO1OBYYxCMmJ2-qyElYkO5cnYek1Ojfr7a7BnY4PSBlbhgxI_XVy92kisIz9ha7EdX9obSWiINFpdJ5BD2cENDCUTmI43MDEM-wxAvj9hIbT4odP_tTZ6ps_iDLKACCjEvTtEyU6qRrzH_1zpNvW555qKa9nSA0jhpLjxzQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEQbB47J2zhG2hWTCRpLCQeJ6XaJ4fg166JIiyPyTJvz1LS4rsSAaCgLebPuB7tXCQa6QGE4I0IiDIZt1vW-CIZgjNO4W4-0Uz2yVSdgfzxQL6QELKqPaN0v0oOj3vW0QRNhaO8PE4I-ZHzAHafwCqmfGSdwe19R8ICcouWSr1KW0N4tjMFV2jpzoH-Ch9xLOzfdM_cXChkeTOdZDFtrErF0ySIqlq8d7yIsh_kESgZnU2U94x9HwQBuFRajCF80zUoaRjSYPUEjQqgX7BdDHFws5ykAL5dhPQoU3n8W_G_EUvxOzjAH9dFJxJkm07vR7mSwR8c-VyMJWPy7KFCFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_Etzn-dRanSaUEc7zrD5_LRqA1-IAMW-wv0El6NjJ2C0NY9Ti-WOvswmAiwalvw975gOvo4AmikpcOyPO6TMWr3edIQu88UWaUXSHLLcC_2CcxHczWkrGU3YiCKAUjRo_TzLJjQoUcejQm9XGbWxPjjLXi0JO4oa9StDX3HYVO1T_wpq9gkyWz-j_nnLTZfq1fc9XeFkPefpSgmbGlU9ejtvJxaMiR7L6J7eTawEFTPIc9EgGm2oZHlR2R_0k3GYf0XtGby-YdnrhDWakCg0Sr1xOPv8UmPRK2QXtS3JN5ZlEE1vSrCt2ofhqYKKyijPT9mwaQv5QibwQFYmYafUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=U2GizNJvDOt-yHNdQe2ajo-RYSOpF6DBElEZ_axcUGzKKgB8IGRpuGb5UiZDwZeK15DULmJAsghyKMHOLUjCqdX9aiA383-q9iJYwPNiZRM2CZNlkZxoRthsUYsD_s8d5PxVytDPQuoyTGtOcxm9ZosXv8py1Aqvag9SnVEFh5tWsVgqNMbPWlLdUZNqM2pRSnWb7-NSFliDYVA4rqOacF_sjXLo3-PNkhoXHZFB92Cc5XfGutxjCDIYzMnaMkgTrSBXd3DCga0fiGSAxwyZ9-UB-8dFZhTSVW0qGSs8XvWmGVQyr2cXOeqnkspvCVv0OGdAXwerMyVngfhk17FmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=U2GizNJvDOt-yHNdQe2ajo-RYSOpF6DBElEZ_axcUGzKKgB8IGRpuGb5UiZDwZeK15DULmJAsghyKMHOLUjCqdX9aiA383-q9iJYwPNiZRM2CZNlkZxoRthsUYsD_s8d5PxVytDPQuoyTGtOcxm9ZosXv8py1Aqvag9SnVEFh5tWsVgqNMbPWlLdUZNqM2pRSnWb7-NSFliDYVA4rqOacF_sjXLo3-PNkhoXHZFB92Cc5XfGutxjCDIYzMnaMkgTrSBXd3DCga0fiGSAxwyZ9-UB-8dFZhTSVW0qGSs8XvWmGVQyr2cXOeqnkspvCVv0OGdAXwerMyVngfhk17FmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivlYWsWE8pxcKQ4MkAuOtlN1HCsKhq0xtMu6Lob2-6d9gE-gReQCYgW6UsNYtEiuScrQGzY9nrccwXOE2d_dzR0zp6_-SKv0MiYZlSPnOmMwqf6MIt3JbViD4DL2EOeLlZrDS3vNGk0w8xY7f46xJF3Rdj1vyHmPlbe6iizQWJNGqPcagjVqdbEcAGeoMqGgCVDxNV4wZ4lJ2AciRfpZX4ULzCQwEI9PJyT84JKH4sZiJhUHBvkdJEtWRbXybZP4qdY_wJ_jUe58WNsyZ8HQtzMnSg-IVWJDUZJDzgRv5CvRaZovBAwfSEDuNgk6-yMI26SCWiVjg74nZIFV0TVPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7F2PfQ3YfF3n5lZ1UZtqtc-F7bbC76XY8XbPcxn2Gwr-KdSTsSvftmVqmaXojq8WG6-pCQFFKRasS3Sptvio1uDzKAm9Od_PVVORbgCNeHxO5CjX8wjWWsHz_UeA7yFptZKDPLvmugEWdVKTvKAtOOPFF0iNR4CytpPrHi-Fr6H6ywV-dHkj7M8M5tyWI2voy3Agm4zKWt4UWgK6kQ86rGIQZVnQEYGqbFA0q2gPcSMFteB2yHK8OYt-WDZsgjsWJGN20QxZdYhXGpUOtBC95fuOi7D0iBWUDAmMPZFo5cqo3WOsMhHnzlH2lQXcqmrg-S5fKvh4H9Sy0csE4fJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALGu3oyk29BmNLzUGIn1v7a1SUPn7cjDgawhmzcVGkBYaiKYq10WiRWyOOwELXhO9gmYVgyd2uuJRr90NTDcD7jHqrWI1E1JLFkTFIkqQV5F-87qvpsQ_lP9XrnX76_Fu7pMjst1aXOS4VggjaChBM3TxG0jDxRTdQF6r_NLVuxFkF-K1FbskiCWqqfppLJwA3H5OisQoPQeTNNb6b6hBhDXqsSdFjjNzwL2S9EtD_8UlH_HJfjhxiRomI6fColleBxxq9tHZuSj-_0EYbW927NA1y_jsdnsyq3T3w2NCHX7U5oTb7VxOuC9cpwpod_5Wploh3QCukiw7NeUVGAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACUGh3arGkX-E5PEp314WG_cWS_qQ0Lk0SZHzMg1-yP8NnyXzmzBbWaDvvzonpSksaS7kFUwzZ2tyNxbGKMUiOXcWugUL2aCPrOQfEr18iEvge9E-uZThd5I-U86AQaIe-SMufPHv5zDX53etpVpqov2byNECVDiuIVh8lhLDz8xTG2yq-6yNLR-jj_w3B03ZOUoZbOgqSzHtPamuXEeG_CNdOYO0B-0V2kTpxA7adWcgNvpTF9ftL2LKn6eZuGLWZ4gIutKBSP620pTtl7nyoYcA9yviEPMGTLyt1dHLnyRz6pz4yd6PHOYCIXe-766nBpy7q5zN3TLKwfYrM6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LRmi1VhZMsNR0q-QCqms-nWNprtyYlL2Tk3vy7U6bQ70Jj5HJ-44RKG7XIzqcwfDWxkeNwPgx3UndC7AbBJBcT8dX5jwank7z5KPxdWFX3RDQOyVN0YT9CEZdP2u3KpVyriH4-m7A1r-O-dK2CnALHFEm4itMoyTVqkYXltQG_Qtz_6M-83EtQCRG4D88eRSL1Ml74OonRYOrkTBAJ1JxCCZTohg9NHIxUX7T_oexYgggFEFZu_lLWE59w4kGxSKX-3i9IS3fdVFslXiuRsysuD9fftdquNOvxQVFEtE0lHYywj1hOIQAXWsnELrRL8C1unNx_WjN5dU1ixl0CsWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LRmi1VhZMsNR0q-QCqms-nWNprtyYlL2Tk3vy7U6bQ70Jj5HJ-44RKG7XIzqcwfDWxkeNwPgx3UndC7AbBJBcT8dX5jwank7z5KPxdWFX3RDQOyVN0YT9CEZdP2u3KpVyriH4-m7A1r-O-dK2CnALHFEm4itMoyTVqkYXltQG_Qtz_6M-83EtQCRG4D88eRSL1Ml74OonRYOrkTBAJ1JxCCZTohg9NHIxUX7T_oexYgggFEFZu_lLWE59w4kGxSKX-3i9IS3fdVFslXiuRsysuD9fftdquNOvxQVFEtE0lHYywj1hOIQAXWsnELrRL8C1unNx_WjN5dU1ixl0CsWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJHLMYQprHSuOFZ0Da-ORJDMfcZI2e6ZJtkzaamZIowh4SU3uqPy0VjwG_dHGmRJ9DBCNbCm9vx70mU3vjvRKW9Ma4XMpCswYeBQICwhJ2e-5wPzHDFO5pv_XPoUQmNgZr7SQ_xmaKVAZOF5M8xK_JW24LSWuEpg4o_rY6geN8zaxHr1hYdKRCxdzJq5ayQvTLg8WZCnV9FQOHxtR5ovflsDDlelEntxLlrUC6gKfo9Z4pIlj4ufl2TLsXVvMzB2bklIrvwLmpNURvQ6yWB8KS7of97poCaNUaxXe0ciWsldx1tV0pxDr0HNETJ43dY-BPAtE2SyqU_V0Da62UtNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIL-c0G2IN5nMqgvuktU_0eDqNZ-LlWiR2qpJkjs-8drMNnG6BMe9MH4iQTlXhk-mDeZuZjHVyIMQtEgzSYg8aUT_EafXeE-9GefqZQ8Jdf8kIiz5teFk4livqRV4G-WktjJIV7BFPMJ1G1xm-r_v45zw4lc_8FWeJKKAl19D_x5JTosWLEtV01roX-SQsy0JEtofhqgZgq4r6gugQaoU5bJ7xCRDCdYmhfeqsY7dwwSqjcDuc0rVpxx-5Q57QSeBi1mLcJ3Vh7wgNctE1Cc7LgE5bR1RhHqTorsbPI-8rmG9qXo11U500jeRDCkT3Y6AyiIpUy0wm4J5kGXfnz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAcAvClTwIZuhhMQBvP8uWKQ4tSAy5Fzj2BcA_r22pm9at1FCe0l3UnmksDEiZgPfKo0bC_k2lX6bKeCe3GPbB13J8Vs4pPPhtxBgXvibA0fJy9EhP_RwJarGTvsj6ioqpdiooyd3Pc5FXEqdQvzo-F1Girpir8bre2KVTbkjbLqeZ1R9i3mb9fXMRUq5h_mfDAwpUV7qExgKrrhbEsPE8ZXAjV6QHxxFxGRQkB3AknbD7-k-2x2JLsPuV756Juff_9u7tRZArIKzZ-VTmukw0cblxr4ito4kjEus2RbaiKsPamUf1ukn5-XDtAU6eKDigCgihr6jBjeZAly41LnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD4udp5iSkvy9A9EKf4Gw7HCyHwJnvFsSoTjhwx2SDXGpXoynkJahq4H0__udsGT7GwrfAtSUwyf3k7n8N1BLgZmJzy0UC6rUE3rol-Vm2LnSg7T_DcxY3ahoUGgZvzIQq_crw0fJTIiCZWEiosLrOEf1PIdyn_oCMCZeZ_CjeQGQRPVWcKGxgMY9QckoDYxCvLF-spRJf-6iT8U-7ox_35savb6-B-_Xk7zlhLRyyFbUyGJ_g9PS2r1WTo0Vz8_0M9-LfLmk6Gi7M4D0uReaYJw1hFWywqFoVRLdd2q0q3HVReILiD6ClHsvbU_CkKr9oR7EyYeW8Xxcn2uU0aYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8KkduL4yQLbwAdXmqBZncsQw3iZfJYD7HXTXVd8xt_x9-RiA6wXvcLYeguZzqMoAx5-sjscvkUPH4pDo9ZY5PArDRqCQJCXeyCfiRHSsTe2nB4gwRkzeBHBk65l4tfYlOPc7RVIzlxk3V_39-7W4efzJJVi-0dbznIowvN9PAvKIk3p-P5SKo_dMHxtyCJn18_nQRvGU3CPKFr7h_NcraZ88Owv3acE9j6mMxJVxqyf5KXp6nmFwcYHeHZR4TSjRiMvd-iiJobzT9MW09CQwrqUxkV99q9vjyUILIUAunsMaJdqxFf1V77Vcg1Oeq8NkRxesJih22fNg2iIW0ZqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=cfnCovzdqeJc4dQiucLz30A1nQgnW2OinWTBUAb-hh9Ne1y74a86EZ_bUdsFuWPD7sBgigvYKz27PXk1pIsURs89t04PZRVzJfysrk8hUWIjlg_x5ZJ6w2RDBSUJpdQnA2cjM3rObT9sFAkXQxVfL6E2Y_0hMB8j7xAt81H1omz-JnVWVwqMWUsQjqbtaBSWnA2bhY37KLsNnitlzSenxtkzmwgrHAxh_c4eAbnCJMys_sJfyjdREYDhp5NhJnI-xXlu5vNmeKCviPM_qNI5ln1ndiI45_6IDkdY-AbxVErNduteISmUII-gLF-UI2g52efNocc7Wx_aqhTLkSISHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=cfnCovzdqeJc4dQiucLz30A1nQgnW2OinWTBUAb-hh9Ne1y74a86EZ_bUdsFuWPD7sBgigvYKz27PXk1pIsURs89t04PZRVzJfysrk8hUWIjlg_x5ZJ6w2RDBSUJpdQnA2cjM3rObT9sFAkXQxVfL6E2Y_0hMB8j7xAt81H1omz-JnVWVwqMWUsQjqbtaBSWnA2bhY37KLsNnitlzSenxtkzmwgrHAxh_c4eAbnCJMys_sJfyjdREYDhp5NhJnI-xXlu5vNmeKCviPM_qNI5ln1ndiI45_6IDkdY-AbxVErNduteISmUII-gLF-UI2g52efNocc7Wx_aqhTLkSISHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-fcd4eE4SKgTDl7o60SZjSYsKWDvGIL6AtKehN8xLMj47uVjrwtOLmhoV4bGUdLwLdF6LDi3GxnDN9EinGplq6XyX8QKWEzqYExVCH5MgFiPxrRyatsOQxO1OcOw1ebxXzrCbKQnNqhZURDQpA17-YkAWzQopwy61wFAnZ-Gi-vqT6kTOmo-aFMPdGutWJT71ft639LVqErHhHRz9_ugDqhoHN9Wgqz9s_zBew3DbC1MT1WFUR1RXfDmCeqA8UbPi-u9WOuzZNtkTNzQ0JB8rUSWi0rNBsuqMCvF8ISvZqfpt7EG-BZYZoYQl7-hONXKvWnJsjnmTVBoI55zZGsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKi1ajhD05WrLiTkbNH8uD0nBSu0-ZJ8KerWLb4ROG7yLtLd6qZ5gV0qZPgdopU4HHftiWdYVQDWfqQnO6KWblEUqLziqnFDS0aRSsxDO1tMme1nHg4g3LnhmwtBu5N_iYD8G07A8EbFFsXuO5yBCHoMnPZAEb1VWvy08zdRNr_aMa98ynHKFDq331rg0svwJbzkqRSP9KAdxUaIx-zUCE1XkLgzIVIk_ckwp7QLbeUwwMIYEdG6eHUO1WgMNP_Eqlj9sDCI3QYKVgksedpNByTMmkxPRdd8a0pfv_b7hvlK_CtEpy57gql0GDvsYT8WZqBUlN_TiUOtcL1Pm2pjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5CA1KcIRCtcbGCW4ZP9u2RvWt_bUA2OweQkM3wiGY8KeW581Zh0z67dCvsh_avB0pdNDt-xKvmTtgdAQjj-fCFw5GBykWe8XzxBPHxhpNUQsZEbxfkw0em9WdCe_GeZGAP-vHX0ps7cTh9PZzHAr1s_E3t-NdYGP6V3Ttrr8Vuflzi3wuo4vphqjH_Q-eB9kUaaHRw132wyMxFq6ChuBu51OBmZVc09XAfXhlq8nOG0zYOVQbse2AtECQba-SSq-PMz_ERo8wBd4VDbTteFEgBZZT2vCZJchlJybiilMMUhfMRrz22K4PjUvV3hLKqUrLhzLk3fjNbo7overxtYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBKqb8D2zo5jw6zX6BxebtZV53t2HSqBulDUcGj_6iqEz7YYPrajQl_XtbnUpivqZAeIoBOpVSW9Xt675KPqDTRxnKz0n6CYSryD8m3p48WrRAvAz95GWPXqNtWstfmaory-32MGDrQkF5dnd0PECO7WDIoXcf9OysSr7_R9-Hs_F_irZbMkb9FaVx3AVwJnza9jas_yQwiP2SlCgYOd2DH3XWkTxLS2ztUx-N8gxEY5LRoLkxYrZBnDZKAgoqdmwDooKQkwKc6c_SoXbcF2fdVrIFT9-1mkeTeB4F04Th6zTSWof7Sabs6vrx-Zrem0nde--V3KAA9zpnjkO-kwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=eez40R53icFlDJlRSuW2UeuGSGGmqcIb5TEleeeRHVQPa5LTrmCYgCMO1i2vTPofilSZutb__aSc1Mqbg_bZ2QrcZj_F-mylaUN7TYh732yGZUVWe2geneCqOpf_TqwayZP-YPMYLbqfvGVvBGX5Hq_bDeXqh2UHYzNd9bNhKncmTAeRMFx6KpRL9G7woZgsRWjteaXGmw3tvPKEkDZlw3h1ETcCldMu30VR94uiux9ClM6obFbfbLnS3i-a5X1Dwynh_ELcGRur3cizS-44LNlMwupV3VCE9iaMQ50R2c7-RGZH0J0K5vS9ztXCceQK6m4vdIuQtSJ_N2FUBeVMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=eez40R53icFlDJlRSuW2UeuGSGGmqcIb5TEleeeRHVQPa5LTrmCYgCMO1i2vTPofilSZutb__aSc1Mqbg_bZ2QrcZj_F-mylaUN7TYh732yGZUVWe2geneCqOpf_TqwayZP-YPMYLbqfvGVvBGX5Hq_bDeXqh2UHYzNd9bNhKncmTAeRMFx6KpRL9G7woZgsRWjteaXGmw3tvPKEkDZlw3h1ETcCldMu30VR94uiux9ClM6obFbfbLnS3i-a5X1Dwynh_ELcGRur3cizS-44LNlMwupV3VCE9iaMQ50R2c7-RGZH0J0K5vS9ztXCceQK6m4vdIuQtSJ_N2FUBeVMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=FlyIN-xAxOJD1GG9E2mrp4cRzaLuMVuqj23CIzWM7yr0pIeX-6oXC4UGi9S_0MfieD7VZjUfOKip0-XHTROonPMOfW4NOY0_w5TV4ITEbTudbilGnVsJkQJPdi7TW6aT9lTdxNJcm98GL8k8dni8vQDgHBv-qpi7beNVln30TpQjnkjfRNfWo8xjwJ8YHgtuUVpechb8JhpxK9MurRAjTbjXTfuyyNNmaSKDLSJu-0Gj7Qfwh6skXiL2h8ksZDDPlH-90Qk_sIJKWN5Ao4wE36jfc_03D8xXrf1jL29mcj4Y4nrGOCuUgu6iixSU2_0juuJmukM6eC-uOsSOdIXHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=FlyIN-xAxOJD1GG9E2mrp4cRzaLuMVuqj23CIzWM7yr0pIeX-6oXC4UGi9S_0MfieD7VZjUfOKip0-XHTROonPMOfW4NOY0_w5TV4ITEbTudbilGnVsJkQJPdi7TW6aT9lTdxNJcm98GL8k8dni8vQDgHBv-qpi7beNVln30TpQjnkjfRNfWo8xjwJ8YHgtuUVpechb8JhpxK9MurRAjTbjXTfuyyNNmaSKDLSJu-0Gj7Qfwh6skXiL2h8ksZDDPlH-90Qk_sIJKWN5Ao4wE36jfc_03D8xXrf1jL29mcj4Y4nrGOCuUgu6iixSU2_0juuJmukM6eC-uOsSOdIXHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8-sAhw2jTnOZaC67Q2cawF2wJTY_DJm0EguvXukrSaJGZqXDiaLr39jPW03o_KoadGw6KXSP6cDREEfTHHjh6ffyubnBcXbwcLxOM4ATmpQDpktCHpKILVGIwE_zdSQ-gSYPN2URSuqkYFOg6keoDDmsDnfhjc7iHEzP3Q5EZNOrs-eqOOhBCJnYVU-EdcMmpad7aF7XsXgIxHhvjpkBrn9K9wTxeWmPUGJFLr3hSXH4AJDVGI0wU6ljJWwou1kpgstaZQJe_mQjdu1U8o6KizR37ZBJ0jFnVVFCYtG7RH79uVpzccA3FJnVaFtBPZ_iqNOzckMIWRUB4UM_iSMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb7jDxx1orhsTiCtZS_XSlASHCqHPtgf-SYvzIc-zYo6sVU0Bk7XCMU6sIvnXVOzU7DNjuwkXFDDCV1cH2uauDUydPEdm-C-rBLTvF4RkH4JNc8Bt7MWEFfB5q8Jhl9QvuuE7rwYbDZGS0eXCBb-n4vPbAmd43VnrtGC2eo2vd-ZQcDN4LsX933qwOB_ae4asksRLExoF3YAu0pwFUQPAt833d8kqnXom2Z0traJ_lpdS1k3JFKdfwopLJDHM-x0SzBBarGhtBFhEnape-xOYfsV9v2KcwrYYsXcOYE99pDNAA48utV8Hsd-fjPLTFMY96IOIby0q4fNXmUCKEpoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucbtaw9P3bDcQaEOCMnn8crStvCAUx-FsM1R7dPTsQH61GuISuRQD4Ek72DiE5a2jqsIOzy7zOxnsLz6mOiEZL7xGE37NTLByuQiVHVkFJra8hsZjsJGlRnF_HsNENMPs5BHvWGH2yeEFutR9cPz-7Sd1grv60FgHhatrgx5PP7oaTCBplVBOIq8QV2jHgWUaWs5bt6Vbw5kHanYgE5NNOeLBWit_zN_mDkqRZPS-PoS0vHq3RwJclkAcVLvwpVn615EuQLlxDKHRg2u3ESBp3cdqiRkLMKpf2XJq0vKhj5PJsTosVIjoiHXzWMlvOEZK6ikBeVABeYWBG5FW_yeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn2fGd7VXopg0_eGxVvV1FkVrDXQgmWz_W2z0bXVRQDn34wrB-K95xSKB4Ff-OHhbF8WyL4xHsvq8Ve5kbE-tDWF2HiWxoVnD9FyExsSErD4lKS2lueuiTZ-PJElQI8j0es2C_VxIBa4g5oDCOvypTHW0npI-a4krtYVqK14khLGnIrHY7-aEqzUHQcNAjiCAsi0lk8qN3-5AZ92a0r0WAOjxq6xFwQaAtVFSxn61zvDflzYtVAFWp7whsvgkff1ld6GPwAM0Gp-gvGTl9c_ZBE2f3ogwkXjPsvq-BhjhMFy96RfAkMaaAkNV_RW72MUp7mskUpApJySxGjnxtf9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=dbY6K6rJFcj-w2fwzyvjfxzVHpAoD4zDWFXfoNVgtik1TveB7_2PJgJbQTbyKrUp0aB3JDKjGoPmnyrAImj76krDfUCttaDeelqu6F3W0ANUI9ejDXFMaeZAnXhNAncdR-TtJ9h08bT6WIqf4v-zYvkuK-250kgRnDpsp7iSl0fyhdiI2g6aYi7IE9N_U6lRONCveiJpVsWI3Sqq80TbgmTCtvdWBLFdeeed_2jlWkJE1ImkTPOczrVlEMJqF0fiZm_q0PXiEbaf8PaQJaACoH-ys_E3ZYS0_490Co_ulBiXjJSNN-5-533JaEo27tppH9e5EH6YDzOoaXqsn9oIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=dbY6K6rJFcj-w2fwzyvjfxzVHpAoD4zDWFXfoNVgtik1TveB7_2PJgJbQTbyKrUp0aB3JDKjGoPmnyrAImj76krDfUCttaDeelqu6F3W0ANUI9ejDXFMaeZAnXhNAncdR-TtJ9h08bT6WIqf4v-zYvkuK-250kgRnDpsp7iSl0fyhdiI2g6aYi7IE9N_U6lRONCveiJpVsWI3Sqq80TbgmTCtvdWBLFdeeed_2jlWkJE1ImkTPOczrVlEMJqF0fiZm_q0PXiEbaf8PaQJaACoH-ys_E3ZYS0_490Co_ulBiXjJSNN-5-533JaEo27tppH9e5EH6YDzOoaXqsn9oIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIQk6kPinwwRtyIKA5FtzZ_u8OfucNSmChCG3yvk3KbT-UoDn_34lPHKLj8f5T5SKAomqk9w1mzlOMg8wsnXl-iDwNb4E6AruEB4b9cUroJKkYwUB5ESCNlA8nbANvzVjJ_gdHfz2DxGrqQ7_4S9x1KsBsBpmmUi7RJ7Fx_8EZdnUHHEO8K1iE9V3rJsbPWNqB-f5zPJpEEqUmyEv_zjKJ1OJSx_SuHIwsx8MDant2HJTjeRLglMPQOcoLgy0S3EVbwK51zY0HhiiP3ORbTbF_xTvo6oxlV0MBz2gyXs5MTdynLFIP3g3bb6njp2rXWQwWl7mqxf1OaugN6lQot-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm7qX5jgq3qaXImSUo6Ghjyrbs9LfHF3lLUcm0Jme-mPexkLZMDIHXQvqu_yWvh1JZ3W9A7LHgDsmbupuvxBi4ZdIfnDxHkrhECxy_QIdd8W4WsckBRo59lDpx56Ubfuq2Eeh1DHZrp3_PrSH8hGD-usTgUxh06_E36SIFOVMONqIEqadTHxiMdjqbZuedCvCpvcsgYHllBd1lkWo08M0gN6rILSBNvh55zOqgPxTW0QPPpbkzFxK8SEkJDhVeYvMJOky2GROBgnH469ceqScUIffLLpn_HQjUgnR-JIOwUAlDoytInrKa_3VdrinBWFlJT4wTk-oTsHQX55QyfnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=hGdqQoF7mUiD3VvnHGGs6DZ2-lBjUFVxweI_EFMIoB9i2k68K73a-soKNrogd91Ko4LuYRhMGQYLtWRdwpLCsjL6I5I7sL4zqJzabtsea3qfb_nmviLKBanMpQ8c-56UyOSyTE8Y6t7lbI5T_Ydy3jgknycZGZMaKulO1HhX921EnVblvzyJ3czvwsdICMMhLGYOZFPsn-Zzi3gNiFjBcinvFXk92JP6CMGqS9KuoBWZee0Jx0C_8ENfyGupjrwtfL0rEeGq6pWBpTcuCGLHR9TeSEKeftHZMP8J8XCxJsa5QmWkuEGIU5Ab2ibPpRZZBZhcWmt1bgVkfc28OARJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=hGdqQoF7mUiD3VvnHGGs6DZ2-lBjUFVxweI_EFMIoB9i2k68K73a-soKNrogd91Ko4LuYRhMGQYLtWRdwpLCsjL6I5I7sL4zqJzabtsea3qfb_nmviLKBanMpQ8c-56UyOSyTE8Y6t7lbI5T_Ydy3jgknycZGZMaKulO1HhX921EnVblvzyJ3czvwsdICMMhLGYOZFPsn-Zzi3gNiFjBcinvFXk92JP6CMGqS9KuoBWZee0Jx0C_8ENfyGupjrwtfL0rEeGq6pWBpTcuCGLHR9TeSEKeftHZMP8J8XCxJsa5QmWkuEGIU5Ab2ibPpRZZBZhcWmt1bgVkfc28OARJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhcxgPBaeBQsqaSlZAizer5_SUkf6cDf5vKewXE9hNAuzTGAYc1E4W3itekoe8nTP0TN8M122TZRyhgisQHtHRNgtsdwMBtAQBUuETyUdaz-L-rxifPaC7Iq7JqplJisJHK4QBse2_SNqTRFmeq0ovlPi3ET_KeG8fuxeiXulfma46l_efT2wbcMy9uGA5_Xy1HisbhQh8Mapv2FNyxL_vJInGKe6WB7mqoXhybRypPJFkDqlcpaJlqi1x2NzuPB4qeQ2_vWjZLyGFgizWHwpbmTrjqgFwDJpRgf0R7wulhKrqD8g0qj9stY7JmsNrB9heMRdenaMISaXFNUoh-L6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=NPzc7g-fcuk6oLqF13V48LxjMgoj7ZjyidjBZdScjlSDCjbUsrYmkitYfe9ozQ-UKAz_fLMkgwyzNbl6O3rZGN7YcccSHRC8loZPbbp2bVeIpkDgdvSLfJi5jC13ujFSkuK_Sv2vgg-3HY7nwQB3rFGJhaIcTN0x2Fqw6hhbK31r2MtcupRIfT64-BxjW-v6x-3HgLXI2zRlvg1MPD9LUe6WnVL3_GQLh69EJhVQdkfXwtf-kB9B9WLt_7XBbfJ506cQrleaCew_yAfE5gNafsga9YQcStlR0RCI3oEuySe_N194djmuIiPaTU64e18q6Cs8t3IvJBOu_f27CAxiUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=NPzc7g-fcuk6oLqF13V48LxjMgoj7ZjyidjBZdScjlSDCjbUsrYmkitYfe9ozQ-UKAz_fLMkgwyzNbl6O3rZGN7YcccSHRC8loZPbbp2bVeIpkDgdvSLfJi5jC13ujFSkuK_Sv2vgg-3HY7nwQB3rFGJhaIcTN0x2Fqw6hhbK31r2MtcupRIfT64-BxjW-v6x-3HgLXI2zRlvg1MPD9LUe6WnVL3_GQLh69EJhVQdkfXwtf-kB9B9WLt_7XBbfJ506cQrleaCew_yAfE5gNafsga9YQcStlR0RCI3oEuySe_N194djmuIiPaTU64e18q6Cs8t3IvJBOu_f27CAxiUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=YvXXeK4zYdR6J6rdbwsca2nwgOaUJe-6RAGfRJ6m1eq-uJMnhvJvwHEOcRMyoGLLaJ5oia3i3jMCHMyQJ1DSxVMnJ_vHvZIndeuG6QrXhI9qBFGwX_vGi4e48FZN2o2DB0Jb4S42bvEoGj3ynsK4Adc0S_7-CxfTL243MGPyOCaEVkIN40AUHlgoyIscG1VxrpudNiSWQrjMhY_iwR6Ah5082xC6F2Kioj67I3Cnk1iccakAtq0C9dymotxDcdle17TZagVvVFPjlEJ2m9D8Xn3tEdTNkelct_bJfD1ix2PgAe9aYuZzy3vCINgPLj6MdhcumRDDZuop48gY0OBCUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=YvXXeK4zYdR6J6rdbwsca2nwgOaUJe-6RAGfRJ6m1eq-uJMnhvJvwHEOcRMyoGLLaJ5oia3i3jMCHMyQJ1DSxVMnJ_vHvZIndeuG6QrXhI9qBFGwX_vGi4e48FZN2o2DB0Jb4S42bvEoGj3ynsK4Adc0S_7-CxfTL243MGPyOCaEVkIN40AUHlgoyIscG1VxrpudNiSWQrjMhY_iwR6Ah5082xC6F2Kioj67I3Cnk1iccakAtq0C9dymotxDcdle17TZagVvVFPjlEJ2m9D8Xn3tEdTNkelct_bJfD1ix2PgAe9aYuZzy3vCINgPLj6MdhcumRDDZuop48gY0OBCUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=SjmA4B7quxRq7yezlOEc7pfahNOdkY3LeHDPzPDTt78Bf2LYeFDiV5GrtMU4Rm77b7_LC4FonyDmaRzH3shuV1i_3koh1M_xOzZfv7yERWErtVjFKR87SPTQDLYtFzZS3PZP_ZB8S_KRQK527Jd6FbMKqLRT6lAVJxBGky_wqEs5Hv83A6LTD7bWBNzh0nFzjmDyEVL9DK17KvvfRuYVA-a2mt_YSXrj_xDrAfSt-9-DL2zrBrE6usomWNWrnTn3JF0ro0L1XLIOZrk-MjTKg_iJ29DbWgZM2-svJ0-YzEE4670OOIMFMHkJbmSKf97hAuTsQye6PKIaxp40j7WYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=SjmA4B7quxRq7yezlOEc7pfahNOdkY3LeHDPzPDTt78Bf2LYeFDiV5GrtMU4Rm77b7_LC4FonyDmaRzH3shuV1i_3koh1M_xOzZfv7yERWErtVjFKR87SPTQDLYtFzZS3PZP_ZB8S_KRQK527Jd6FbMKqLRT6lAVJxBGky_wqEs5Hv83A6LTD7bWBNzh0nFzjmDyEVL9DK17KvvfRuYVA-a2mt_YSXrj_xDrAfSt-9-DL2zrBrE6usomWNWrnTn3JF0ro0L1XLIOZrk-MjTKg_iJ29DbWgZM2-svJ0-YzEE4670OOIMFMHkJbmSKf97hAuTsQye6PKIaxp40j7WYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=DBpz55Mf2cFR5sTWA74rjxofsochKdb12LpAEfD0f2pXkCEt-sYLpFHuabB7V0O309KgfjFJvmJ8EcCgged9h09H6IzvFjdLWCNX4FIlxUUWKTKefAJJXFEM9LXoE4kXZBccFWZPVB1baB_Sd6FP_2u_2DrDhgt_4NAkdvqxQ3NLHy9HGUvmH39ae5L8V8tC331ybTAPA7ej6NlXi2OBItYCO-cds5aJ1ZjQTxzeOcr0gIir8PkOSQfCnG4FMzOqIRFDtSp2XWljy8yAHrn__a7BTtFM3trtskJ98X6HbP56IKE6N_6CT0xo3IxUMCdPDHnV5Ww5D-rwtwpKrK_xVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=DBpz55Mf2cFR5sTWA74rjxofsochKdb12LpAEfD0f2pXkCEt-sYLpFHuabB7V0O309KgfjFJvmJ8EcCgged9h09H6IzvFjdLWCNX4FIlxUUWKTKefAJJXFEM9LXoE4kXZBccFWZPVB1baB_Sd6FP_2u_2DrDhgt_4NAkdvqxQ3NLHy9HGUvmH39ae5L8V8tC331ybTAPA7ej6NlXi2OBItYCO-cds5aJ1ZjQTxzeOcr0gIir8PkOSQfCnG4FMzOqIRFDtSp2XWljy8yAHrn__a7BTtFM3trtskJ98X6HbP56IKE6N_6CT0xo3IxUMCdPDHnV5Ww5D-rwtwpKrK_xVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=Ab_ksBmlcqCl5BBbYwqhUf_32UjDMUCfs4LumgywOotSNFJy0olZQaOOeBih2eC7gC_3bqnVhdtxRukBhVlZUEIE0cb5Nff0gjzCvHKY-gJkySXBuA3oR9cH6fvtUGqR-YOu_4yWP7tOantqOsV1PaQ1sfqBRsbytcQ4zIm9EWlAJnM9bIQUVaxLmoYYqDx2NfCxCS5MdYPttrthvEgZd2-JFq4YCYlLRsBPNRRzbQfdLr5yWlf62WziS8Qg7TjNShOkNDEBXXsJUxor1umQ87KbGNx-MYFUdoYhfehKN-J0VMNHEQyNMOAQCmVTBuRG9RJPgDpBhfR0Tge8ldzqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=Ab_ksBmlcqCl5BBbYwqhUf_32UjDMUCfs4LumgywOotSNFJy0olZQaOOeBih2eC7gC_3bqnVhdtxRukBhVlZUEIE0cb5Nff0gjzCvHKY-gJkySXBuA3oR9cH6fvtUGqR-YOu_4yWP7tOantqOsV1PaQ1sfqBRsbytcQ4zIm9EWlAJnM9bIQUVaxLmoYYqDx2NfCxCS5MdYPttrthvEgZd2-JFq4YCYlLRsBPNRRzbQfdLr5yWlf62WziS8Qg7TjNShOkNDEBXXsJUxor1umQ87KbGNx-MYFUdoYhfehKN-J0VMNHEQyNMOAQCmVTBuRG9RJPgDpBhfR0Tge8ldzqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNMFhDbD5g98rEhy2fm7UiY01l_b2YIDfWNqS9IvjqQfzoh47HfAwgz6q7UpDPpLbv7EpCSg_-G5BxW2ehgz_dONHEJKhNu60ovWbYZTHHQNUMQFC4-9zPGi7GsJFZ_1UTO5jVgW1PGrxIEQ8l9cQuwk3d8oxXzuxqvm1_BMY8I1x6SjLQBHb8OThEHUKlluXh-ZvA7ug-j-vtMAAB3dx4vtkV49kRWL6hGU0joRbmmTW69OOV16wOgxMyCm76aPG5Ya6VN00SZdAbhDuFdSNp-tlFgmDiBsy9Dyx5sbJUIOlayMhjb-T24rZfBAtlAbEJ8P0uvWm23Q4Zjix_frmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZ9J4xWPjgJpZ6ViMMOXxCEwnl8ZOzHXq90Ug8XcjbNjgtqwwOKeh4cXOMXGx21hUWuIvo8Mw8aNI3HbyqBfG-Mo_MiL3fgjJJSf9P_Xzm5H5bAmlhSNO-GnWmREz0wk0kyeUyCiSmzDOcTGnJSm9tvuCWQ2gZjaNer-maVEV32LhL5iyC0Mrcwg7O37GmvarNp2GcUFZmTkkne1EAs4gRnH_WDf1-PtFuOUeKEpxKveFqn201HKd_9atJZRQS6ICKgquMG-A2G-VZ1t7PjOAwM2jQWxXbn3Sc3z0KcZE5Hdv33DAeIENcKIfBmpCpuxlEB-6HPlGOEl4stiW7QNkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLO-kA-0Wsm9pLuLf-CwNqFKT_UOIbqopVwxgyIAsIbmvVlOoQ_GDbtfY-pKhJ5mthyrP9S-HEBPx694R1uKH7bRc4l7EAkMIyQnGTQQP1NewZyg-n8S2etuMRGBGzzWWHnByZkCQAVP8DZCEVjlmEVAuH70XESxqy3AQsuvW2lMCT3-jB75FqcWbyJk_BKI6UltNKb9ta78gX085fc5v4VoxyRbvj95y6d3hRC0k4XeoUjFyURVgfIqT4A7oQt-tXAYeeDWaZXpRymUqEV_IKspB9wNe9f53lT85mPyPC6M03wQe9ajNQilF7kyCBAI8OByt7yOQo5DalOO14AGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUl0wTadyuFnC-bfFkC4nIFulUoguaRyH_pBX5r2TvSxcGy1NpvIa0bo4uw4f88-YeHum_p9Hz8jjdmk-hwJy-BStKUWkZu_dRiDsh5JHIuHTufuDIus-psoiPxD_lwsRfgVOWPcJTBhd_yOXDdpyoEsXfpP1moAKOjDRtRpWkLNKdPLy2OwIVHb45wi3uFloqXubEbQheVua0gjsdi_smiUzAKb-v7DGl0A9t3sFkJxesBcgVb1Icyi_mJLTm7NbqtfoTTJH-kVBpBkPgId4hcNfRjqp_QjyceA0_QLWNxURtroekBP66oe7reT8QX4kof43FMkMpehE0h3ZnrFEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=AWbMQ6pQEo-zJVeWxTDDQhUP4Pp3L-7IsnCuo3j5uox-gD34Rb1Js8r6O4_9g1K74UfacVLjMZcPNJDVxaeom7mmSLrrSnHl_6Og8hnH1jhnkoM1Imcp9CVtF4l9q8MM4Gz5AxMVJC6Vo41h5k0XeVa2GMXnWqkZyQi874w0Kf5hX30uTow6Uwshk7S8PFAA1VxnLydiiW7xZHkuuCQibgxkTzZNJaLMY2AEpoVyxD_TpQBAEhjXtnVPHTF6HTbOEsNtSfHpWaUD_fbvOrdmTpPwAsFw0CKjtSLkZRClivN_L8u3gCgPNTJb-aLw3JW9R79x4PWx_8FlASu86DBitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=AWbMQ6pQEo-zJVeWxTDDQhUP4Pp3L-7IsnCuo3j5uox-gD34Rb1Js8r6O4_9g1K74UfacVLjMZcPNJDVxaeom7mmSLrrSnHl_6Og8hnH1jhnkoM1Imcp9CVtF4l9q8MM4Gz5AxMVJC6Vo41h5k0XeVa2GMXnWqkZyQi874w0Kf5hX30uTow6Uwshk7S8PFAA1VxnLydiiW7xZHkuuCQibgxkTzZNJaLMY2AEpoVyxD_TpQBAEhjXtnVPHTF6HTbOEsNtSfHpWaUD_fbvOrdmTpPwAsFw0CKjtSLkZRClivN_L8u3gCgPNTJb-aLw3JW9R79x4PWx_8FlASu86DBitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=IQF3bTMJf4xd5GN_q4fPq7vzlOlheMG0S-R0AY6wgqIQQi25SuhsMBaglY4_Iw1cM56LCdgLDBLWewMUIVKbZ6GbYq-ZN4YE0CuSbbi6lGGSODK0fKJsS1kISXr-M-_l1RQQWkfSAAWWKPGM-yN51V-WNOlKKRHpgXlHpo1p2J-7NbMJpJUtMFp90WExgjmtZaNFXfJLMfmcz2S3Q3YHZKhTHOpJDUQ2iF17EwPYvj7Qg828mryYjeAxMJAwOugxFCY6yqUXW0ny_tsZBq28XaYw1QQWI_PuVJ3O8e0kSfAqW-I1fPn1Q5CW9rTZqbduwsUtjCJvButJHR1-tO4xbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=IQF3bTMJf4xd5GN_q4fPq7vzlOlheMG0S-R0AY6wgqIQQi25SuhsMBaglY4_Iw1cM56LCdgLDBLWewMUIVKbZ6GbYq-ZN4YE0CuSbbi6lGGSODK0fKJsS1kISXr-M-_l1RQQWkfSAAWWKPGM-yN51V-WNOlKKRHpgXlHpo1p2J-7NbMJpJUtMFp90WExgjmtZaNFXfJLMfmcz2S3Q3YHZKhTHOpJDUQ2iF17EwPYvj7Qg828mryYjeAxMJAwOugxFCY6yqUXW0ny_tsZBq28XaYw1QQWI_PuVJ3O8e0kSfAqW-I1fPn1Q5CW9rTZqbduwsUtjCJvButJHR1-tO4xbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Q98c56fVq2kZWg17-fF9H5rkkxcSUDZ16PYFmgkxXUCcgjk0-ebhZSMTz9_4O49u8vaijGl_F4fO3VdGJ_b6euTtONUp8CB8RqBeCtXV3vpvjiUR8zH1iNdMEOMSDNDxVfUvbrs-f93lc75saXvu_O_5SEAs0eFZwAfAt56jlvfRjFIZJGHOErdAejaxjFV_WZ5W2J38t5zeZMi8xKxnugsbaRBQJkFGG_rECfNztkq990EZpliF6iFRRUGV4n3ZwYjzyeZ_51V1jBB7i7sk3CHs2LHPeUQEEERoHfka4UU4-iA174MK-VsyVbJUM1wQcYkeifsercEwRxyC0KuEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Q98c56fVq2kZWg17-fF9H5rkkxcSUDZ16PYFmgkxXUCcgjk0-ebhZSMTz9_4O49u8vaijGl_F4fO3VdGJ_b6euTtONUp8CB8RqBeCtXV3vpvjiUR8zH1iNdMEOMSDNDxVfUvbrs-f93lc75saXvu_O_5SEAs0eFZwAfAt56jlvfRjFIZJGHOErdAejaxjFV_WZ5W2J38t5zeZMi8xKxnugsbaRBQJkFGG_rECfNztkq990EZpliF6iFRRUGV4n3ZwYjzyeZ_51V1jBB7i7sk3CHs2LHPeUQEEERoHfka4UU4-iA174MK-VsyVbJUM1wQcYkeifsercEwRxyC0KuEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXx3za1kcL04Jy0vocygFxjqFNzhNl6npJScgcOuY1337MsvjYiKzPNn1aanfPNF20fDHx5cZz_JR3l3Hxyn9sHP4JkS1YEuLOo6qHSFxbUl74TBU3A0xCepB41HL9O5jUYltnq5wm0IIMe-BFEfyXyaLwV37Cq4zHG9qbyKHj7Vgvbz1d7ir0X6kHVrWgnGqxKBerwqIIkXH7T6EGG_8UmSxffaEP1wAyQlYM2qwfGtIIMDt3Z46WDuDE7uj4Or7SyzJ1tgwhVKHchRozodByj3yT2fWeZr10bpP3mNSZqeJQi9ExwCBdrWPOpIAF8ErtmRpqGreN5VL86DId3zCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=TeiJrsoXqYEMQjJP-rgM2seGWUeskJ7wCXn11nMmk8XQyC28rw60ok-VSz9os5258Jinxi1ptvn3ZBzudV_C5OH7W2gbKtR7rtdSAGSTm3z_ZCJlJIhQRUpwKbnDV6-ZsjEFEBeJguHjDcjRH7rbqZBNa5HPPO0S_tfK_TbLVwWc34jFYE5hEFdyv7GhS6szAud2c0lSpFRKe_YiB00Rtidtce1D-2-GD5NHYjufzwcIEcybVtVQVjg7H6uN-9H1FW8EhIyk1i2QNJ3ecTVNrhJVdfHFEMThwD6uNSXEDY72ipriIlHivsKDii0W1dXsCB1ocfz-EUIsfKGjKo31rBYOtLsKzrmoOFgnfPi5KloldbdgAyAnf9k6fMkPfdMuHGAULCG4D3tuItQpMS-1ZH8CXGwrrBuHf6jRSfeFgET-zM7nedaQ-Y1iywpbhv5JVp8r7_bn0Sezn5JzzkvyQNJgx7eTm_pv2Dgzkv0rzf4i2m0qLUFRSD7S-0lHZtEHJJe1lAlNWyr2LbNQwXG_xnDeA3fkLvsQj8cdJvMss_v_bF1eVGsKAbF7pt-RNytMsxFMu-jBgAGED6Gtk_e99EryPw3ZYHEbHzoVRZzJKAoEuF9gwJXMF9mAjtnbmTrRCeS1jQ5hwMS6RkoaIJpCx02Y4J5KtJFP6OwcqbSBikk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=TeiJrsoXqYEMQjJP-rgM2seGWUeskJ7wCXn11nMmk8XQyC28rw60ok-VSz9os5258Jinxi1ptvn3ZBzudV_C5OH7W2gbKtR7rtdSAGSTm3z_ZCJlJIhQRUpwKbnDV6-ZsjEFEBeJguHjDcjRH7rbqZBNa5HPPO0S_tfK_TbLVwWc34jFYE5hEFdyv7GhS6szAud2c0lSpFRKe_YiB00Rtidtce1D-2-GD5NHYjufzwcIEcybVtVQVjg7H6uN-9H1FW8EhIyk1i2QNJ3ecTVNrhJVdfHFEMThwD6uNSXEDY72ipriIlHivsKDii0W1dXsCB1ocfz-EUIsfKGjKo31rBYOtLsKzrmoOFgnfPi5KloldbdgAyAnf9k6fMkPfdMuHGAULCG4D3tuItQpMS-1ZH8CXGwrrBuHf6jRSfeFgET-zM7nedaQ-Y1iywpbhv5JVp8r7_bn0Sezn5JzzkvyQNJgx7eTm_pv2Dgzkv0rzf4i2m0qLUFRSD7S-0lHZtEHJJe1lAlNWyr2LbNQwXG_xnDeA3fkLvsQj8cdJvMss_v_bF1eVGsKAbF7pt-RNytMsxFMu-jBgAGED6Gtk_e99EryPw3ZYHEbHzoVRZzJKAoEuF9gwJXMF9mAjtnbmTrRCeS1jQ5hwMS6RkoaIJpCx02Y4J5KtJFP6OwcqbSBikk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg4Rgavj69wpX69bc8wg_wlBwdUXKq2JUV3WaRojkf66p0vNjYLW7yz_lzegq3mfmvy-6mVs5wF2GGHpdTk1fbuA0SyXIMra_CLJwupJLycMr_tnwsOPDA2h-3K78bga01GcyevQRVdOpJALi_FHOlTa-3ct384Jsh9WMGiSpE3qtaGi0Ut_o0iz_P5atVqTSFKwKFQcqYloiQViwoD0HwktLsWTCTqN5GaHMTrLYBCqDXVFeUJrJXGPszsfkdB4xrNQs_YygRgd81xqcJIXNjSw7tr5_oQX-wC8QqOZyx9N7FkNeLjka0hMq-3jnQCkytToTP8uu7QD6eIlqvJ-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=mdQrkGnG2Hgpa-pXoMs81T0w94iYQvq84HIYpIHd4wytFn3xjNEIYAydNzdHlJTeXbNEFlyjVaDbsnp3h940AJO5HGfeZue3rNnZ40fFoGhkIt5d4ZOH2oxGMOKEqNbtL9Jy3D9avEkjxp2iq8xwF3knX7f4toeAYpmMM6WJW7pivHl26gptEIYcQPreit7RdDsWThGAF-5RH2Ok3FiyLTp8L60_YO5JfMQP_T3NNmThdccuqLtndZACwdBX5hvJYhkqliDS8wXS-hI58bhfZz9-wYd0lWg8UqLLWxFJcHNEAI7j14CyT7Gcpn8RP9NdPQvJuiYn3E7ACEHiFOvplA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=mdQrkGnG2Hgpa-pXoMs81T0w94iYQvq84HIYpIHd4wytFn3xjNEIYAydNzdHlJTeXbNEFlyjVaDbsnp3h940AJO5HGfeZue3rNnZ40fFoGhkIt5d4ZOH2oxGMOKEqNbtL9Jy3D9avEkjxp2iq8xwF3knX7f4toeAYpmMM6WJW7pivHl26gptEIYcQPreit7RdDsWThGAF-5RH2Ok3FiyLTp8L60_YO5JfMQP_T3NNmThdccuqLtndZACwdBX5hvJYhkqliDS8wXS-hI58bhfZz9-wYd0lWg8UqLLWxFJcHNEAI7j14CyT7Gcpn8RP9NdPQvJuiYn3E7ACEHiFOvplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_SVbk2dK9mHxSr6VsRVZ7Gm8Dxag-T_3ZGLQit8UcIgzg9SEVzBMzzGSK_4Baq4Dg_uahJVj92DH9KUwtWOsbWujM26khz93H_DUE1rtUsdpqAvfHVvp5oGTeo6LBttq9gmo-bh89R6vcCqBmP960uouiLSODB7t_lE5qzmkvp_nT6MMc0TQoJVMV4NqGb3N16ArEI1VXAboTHKF47SYW23FJyjKRgL8zN_zF8CFyIuNZAnsDDmOj9HBWBQ_LWf-k_F6D72VM4Sbdf__cBUm1ZKNQzAJMZ8_GH0w4eFq1UIj5_gsyjjLb2-VzE8jWFH95t_EdPYyyRWiZROjgrffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5iV7hoNegb76wAMa84ggGD57PaGclI1sDgOpiSe7TakQTyPJujZ_EJHPLhluu-lV4usJWCeD0JVFGGFqsSmqEiYcDFG3zXOKEa96MNB9-jReFzWL0Qcmb0_4YJ1bVbi1bw1PNNREUbF3HcoE7H3_oIYmv81-bBkP3J-cIO8_d25D03etrZ5o4AnNwtUhPVuUUnt0LRvmsk65ZyyaQlfYWjmoBdVjUgvAmqhslqMIGSjABmwXyN5X3bWm-fPP-j_b0eLZx2bbNh4YREFz3IHw4r97nCqDXCDMpWFkR-yNSzsw6OiN9EaM7L5LSdyR2bk_Ak7oUs_PDFTEvk6ZUp_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq4NdjL-Ud4iU75EM5SxZboMT_B0No5EFUK55RvBzI5w4-Q1lCaNRTFhLwfj7q_qdn0CHCUFw0lbYU2Chj3ctXiISUlNfWfwsprhB3QUGfG05rYSZr8ZFqJo3DmWfMVRgu-uKCN42fsIXUrpON8cavpGLQXjr8LnSKiPwFA7_zzsvVBcFKY_MWjozZgCVBO7D91dx328lDPmHyEBDLOjzsjroFIgcf8VVtWa85ZCqsZRUlE-A9j0yelsKllbpSCQBjIt0EJKKOJWjeslMr2M0J8NWZvSxdbpcgB62DflFBrk92cCpurFus3pqoaNaSfRJtLKLx9U3DvxpHEFJMfmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8kkrE-R7lCir5gz-ftYJUvsKkD5BCBOzSrkpQBWGnkJFPaLRhwElC9LiBMF1gZWWfK25UPZoCj_rzMRVzvsnmIxUnv2h8K73su-BZ1caZhVLu5EZeD1Il1lSaeK8ZhZ7Ys6769gAJj8eJ6fAStoWyLhoHR-nClDn3jjkcetXM2PdgDjJrpkMmL9tiudESY2xctYP6-scDIwPM4ShxmD7u3uuRabJZwEU2wk2537SWpJdZB_m5KG4wSUm_rw02m5Oe2Zl99s-aC29kIaPIGHuxdobIgApvSI1BfsBXEaMtOgNFQhLj7eHW6bjnAwkfp6pICJuJeTNEbTH8s9C3fpAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRxMgq2NDS22XBQU5a9viTZ4kEkmujosCH7z9Xor1BFqQrXAFDtCu4wCQ508r2c0Ln_LegqeLypxUdl4pek9gaYW4_WvgM_MOtEWzRY4Fdojw3i1Vx43n6eWm0z94IfpCookCCYoYso5RnGeHiyaINYwPYaTMr2hkmf7eGzZjIe5WhsEw1G26Swc9TpnR8IlALJSnJZdOX9WpgdXPze4oqSTltupxkHHU4vyiWZHu1vdm5opjCSKpum3SysMiqZEd7Sd36g7DKe2TSw5Uth8ygVHf_kQBkBWh21lCAeRkq7i6hSgTq2w-HFpIn59SrE2FYrL59R3O1p1nsDOxZSoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM8O3wkaZehMkh9U4hm6vAsOlPIYk0pEHHJSXTPygJ01nkkZYBMnxQmRzMx4Dg8GSBir7TaBI3U06nlatMWMS5lRqqLX38LsFCZLpKaQib1_1m72Kc3N4GHiyUMJgYIE9q0YFqAC1gWJzU6A8yQ-igTD4RCjAksgWsmnrFurXTiG8ckiI112-uz-KCYHM8j1WwBhuUFQTFLiMvgs5_k365E2tQVzElCZnhByalKqh0mY3IONE0Ab7PWvrMgJ91N1vm23D02IVjr1-TEQ8NwC3DfBy9M_LTjka9Lxy8UBXMN79HMq4asfnViv8JVTmDUYCZePdIVM9G1_QT2dU1iRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evlL5_Ca1f-IXXpZQlK1uFSSIuOoR6jpOih-UUv-HyB2nupEYWf28UgjUyPb8T3l5jTbr4KM3QCVWhOXKfZBn7kR4chRdZQhpqE2B5J_LY-VhiZRLcc0hWUNZNDf8Lj1dQzQTu9ZbUVVKC69e0CK2ohyGnGd9EzScr-CmmQgv0tHJK4Eoy792a3ZZKJOanm7oYlYeFupc4QyUTYnaP7mKr_oLox9PfzvpD_B-SeQRNC8Mb4g_lJTIm9XGFcjBqqW2pSsMYlfA7QLHhtDydOU7mCaQUCebfBM4qmlnuF3xDh55c3dos1HuJobc6NTDoAPkOLjNIm6--38qQpdNp2Gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=Z48MoWyZWPjmYxtHOOPMxzbnaY7VkhZsZMPBiQAAHqzSvPi60XS7it_yF1pcbqTQd9A8Q23-NunI2MFycC6kEPb3nN0cYjiqQvJ3xW4MPQhuexXRc-8A9Rcac694yppkzkSaDRAC0veH8tJJfGp48zWJ872rPr7dZINn8-vrXfia4OftTF5MVclc6HwvZ8ygoIUr_rdInfymlKFepPxxC0sM1Fk4yKSFxYtGJv-biQs3MNMEWZztTpcvpEtpWaKlRQgq5Fs-132xMaxW2tQUrxLnk1ahJqRZYnqXZr8AgGYKdRwQIT08nnknEWVUq06hJ5-IKFGaHokjqtMY-aseSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=Z48MoWyZWPjmYxtHOOPMxzbnaY7VkhZsZMPBiQAAHqzSvPi60XS7it_yF1pcbqTQd9A8Q23-NunI2MFycC6kEPb3nN0cYjiqQvJ3xW4MPQhuexXRc-8A9Rcac694yppkzkSaDRAC0veH8tJJfGp48zWJ872rPr7dZINn8-vrXfia4OftTF5MVclc6HwvZ8ygoIUr_rdInfymlKFepPxxC0sM1Fk4yKSFxYtGJv-biQs3MNMEWZztTpcvpEtpWaKlRQgq5Fs-132xMaxW2tQUrxLnk1ahJqRZYnqXZr8AgGYKdRwQIT08nnknEWVUq06hJ5-IKFGaHokjqtMY-aseSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv8gLJ3hu5qmd2x_lJIFyHLsMtf_r9PdxA1-ouUslKgfLJBDVNelZjWW9m0_JZYt8FhL486ha3fEPBTM7jDo5ZqC-OZKg0DuipgSdDupDuBbisAjmx4Pu8nOjsyebik_1gV-SOUmZdU_Q5Zpyy8HNyks347LSUYHgpwU_mtw4V9_huwohgyTGF-2lp8KM0-cHdHCLEIZgTSkZybzlWriSzjOVXY0mz92JA4l0MwjkFYxtbQ4wFbyEgcsr7Cf2Ho9khPKN3LpmstaT4NswNljAY4B4b4O7Rk0mULkeG5D6mmoNlvf8O_SlYgHyfNVJfFpgmkgiN3KrL8-JZL8JvPQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q15Z20fzUO_Xh29ghlZ-EtAG-2gyp8nm3q1POiePb4lnN7ZEL7OxEXILjNMrbaob7PjvlxVt2xp-JiRv9IfJODFh5x-nlcFbjR5hgNlf2q-b1X39-ajmigaO3EC5refSiqIOghGKJjGcCM0nxQ4pjDGrJr18HTrMp4e1-MLUzfEngnrnkKUGr0MbOKk1LYJWckQANqsPLUwouKP61NJZVZ8V6CPVHwBsTCQ8tgnFFiAlHO3n5HpNGmmyKU8xL8L9wE5KpCaEZiCbZiMuyPemYfqJsItOK_IrLam_pzxD1X5L6BMLMe6SlskGtJpx3o3wPrmEVUP-kmm8edGYr6edtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=vgmkQwO-PDchSlskS6SEduArErIH1tw626c-4A32v2_ftitC-v06b0p7nsKUxvRnnCS2F8DOvFRg7uo9XG6XIHkuVH4FhM0JNXNQon-ftuvmzxMqSGgY5FZYNKrMqfTA74wOGVdKKgzngy1yLc230AoRvMOB97nzDfzn8R5rYeLF9Nr9g3_bhek0dTbiLikVuike6Ja9fZSY87VOlpG0hUNLM8PoyvAJCUW_RF2-DKOkNSH8bGfJ_BCDrPKNY7E2vQw1reRcRW93dF6m3IPpPZi00K69uIMTvGssPnKtdwOj8BODu1pGQutQUC711ZAmacLP4R-Vb4YxbB0JbEYIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=vgmkQwO-PDchSlskS6SEduArErIH1tw626c-4A32v2_ftitC-v06b0p7nsKUxvRnnCS2F8DOvFRg7uo9XG6XIHkuVH4FhM0JNXNQon-ftuvmzxMqSGgY5FZYNKrMqfTA74wOGVdKKgzngy1yLc230AoRvMOB97nzDfzn8R5rYeLF9Nr9g3_bhek0dTbiLikVuike6Ja9fZSY87VOlpG0hUNLM8PoyvAJCUW_RF2-DKOkNSH8bGfJ_BCDrPKNY7E2vQw1reRcRW93dF6m3IPpPZi00K69uIMTvGssPnKtdwOj8BODu1pGQutQUC711ZAmacLP4R-Vb4YxbB0JbEYIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=nuBcx6NUz0TNjBQX6o9GnjKo2Gtfx81JCZWiq5hu5LWtfYZObUCHtIXIj3nKvj_L1AwvMiQzciKKvLymHc3Qo0_U2Kjkadj_pjOdu0D9LAFTKvm3xh06kW5u4-PajTnFE-_OPOQNAg45Kjd8hC7djDh3QF4iWUReCLOkNjgsj8xroBADf2yc-vavoU2f9jxe5W_5wJM9z0wWTMz6N-geM46B802g-p0x-dB9FmmpK1_NOENxnVr7pIuOZKMyi8B5bKiAUE-zqRteRXpnCHvAHGlWO647yOEJ-WQLglL9Amd50nrfGQHSGJvP98v6gbQZ7ArouqC2L22B_HZmiIcgnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=nuBcx6NUz0TNjBQX6o9GnjKo2Gtfx81JCZWiq5hu5LWtfYZObUCHtIXIj3nKvj_L1AwvMiQzciKKvLymHc3Qo0_U2Kjkadj_pjOdu0D9LAFTKvm3xh06kW5u4-PajTnFE-_OPOQNAg45Kjd8hC7djDh3QF4iWUReCLOkNjgsj8xroBADf2yc-vavoU2f9jxe5W_5wJM9z0wWTMz6N-geM46B802g-p0x-dB9FmmpK1_NOENxnVr7pIuOZKMyi8B5bKiAUE-zqRteRXpnCHvAHGlWO647yOEJ-WQLglL9Amd50nrfGQHSGJvP98v6gbQZ7ArouqC2L22B_HZmiIcgnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AephO5Kz3T9lfXGtF5vEgeIo_D9zrfc--Tq_Ht_H7JZZLIPHf7sZ5D0SxwLJCNcyNTEpaYw-5BaPGL55bn1mkjw0gFtkevJ7GVGKSpzvRtfGC1ivL6einEgr3Jh2RR6U1__68VHQfl3lb3GQB3IaEjUfUgwCNYPE9loIszKYpliDiN9RXi14O_kvgU1eh5rwj1yMXvRdKXNvH3qlJGUPDlkCTP__S4rx-cU4HHiV6nVCNclE_7xxr9kimNhRnOmj50shjj2RwS58vAUy1MuD5z8JpvUsdqrgucLpQm5zUuz9XEGzuAcSypJbGywDMPeDfRV3Zwh5m65cGo5eyH5cNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=E6aCE6t4ogtFqNb1jt433W2wEM3hsVeRUBgPAU907x13pzq9RchAevXP3pcbZcUDrk51tAkO0xqF2CQjRvLwEtHZIKR8tOh9QrqXMXGIIRTOEFN8mzBPG1drPgWaBcXNhigg0QpO39V1k7VHcOliQ3R8K-KtA3k58D6PwSvvTlnP2kVPNhJzLhQtZDkv-SdcZUb1YeFKZNIIN-oh6myyg_SvuQXoITbPX7obL7LRMZDbQhoz9T6x1bcAaQwiJgyApGPw8VYEQD8m-XE4NC9m7GMP9VGiKdA9bWfsqQYCmdPlkUKzjXp7pemn_Wpi7d6EvZYnoyvqgNTAcVUx8f4sYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=E6aCE6t4ogtFqNb1jt433W2wEM3hsVeRUBgPAU907x13pzq9RchAevXP3pcbZcUDrk51tAkO0xqF2CQjRvLwEtHZIKR8tOh9QrqXMXGIIRTOEFN8mzBPG1drPgWaBcXNhigg0QpO39V1k7VHcOliQ3R8K-KtA3k58D6PwSvvTlnP2kVPNhJzLhQtZDkv-SdcZUb1YeFKZNIIN-oh6myyg_SvuQXoITbPX7obL7LRMZDbQhoz9T6x1bcAaQwiJgyApGPw8VYEQD8m-XE4NC9m7GMP9VGiKdA9bWfsqQYCmdPlkUKzjXp7pemn_Wpi7d6EvZYnoyvqgNTAcVUx8f4sYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=aprH3XRy4R-AlILeVuShZ0x6s50zWHURr9HEur3n970AtP5UzLaOn2iuQ30nMPiRnqWaOH8KY9eaWbJpO7d27moJ2xJzS0gC4X9-dqfbcfy3yLoiJhUosR4xGestp5uMn1drbGK7v5bGvP1EtW6PL_sz-1PXjzaon8BNN7QEN1oKCI4th_ukqbWYe0QoMqdUeReb5J-GhOUcPktwbYXQdgx5rpKNGYF6f3zzCSCxydeAu3iPO4YjK_Ju2_9ZwL69L8Z7Bm19bz53-oHCfEoSGOYDTdm2bZGXXu3p08HSvNOPqeAMCYDP3wMWejPoOWilZp5dxgaHwxzWlKIVvJBfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=aprH3XRy4R-AlILeVuShZ0x6s50zWHURr9HEur3n970AtP5UzLaOn2iuQ30nMPiRnqWaOH8KY9eaWbJpO7d27moJ2xJzS0gC4X9-dqfbcfy3yLoiJhUosR4xGestp5uMn1drbGK7v5bGvP1EtW6PL_sz-1PXjzaon8BNN7QEN1oKCI4th_ukqbWYe0QoMqdUeReb5J-GhOUcPktwbYXQdgx5rpKNGYF6f3zzCSCxydeAu3iPO4YjK_Ju2_9ZwL69L8Z7Bm19bz53-oHCfEoSGOYDTdm2bZGXXu3p08HSvNOPqeAMCYDP3wMWejPoOWilZp5dxgaHwxzWlKIVvJBfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvEo6nX4DKtf8x_vsCya30KwzO7GwulsLrcnFmCrg4gK6UZ04bJqHWzm7Qgp53Kke1XaEpnaq5hO5ghtL_woMUgJfxabo79UdZYW2xhqM_ztH0qjeJKUuSN8Qi3I6IVArNV8fnxaig1ATwDyMi2mTE9CMMWLk_1w1Jqv40hBxryjCGdn4EgPlcw6Gl0D0oRVYk4C_PUMc2uQol70GBaoukx8ZbmuNnEUHJOimc_aBgR_PyyJI2c_fVyHpOLLVEY8eokrOT08p-CECMiqI_pVJt0NpjFqLVXMSsINS8woN-VAop9OzYoCk7o7l01eyDnrrUz6r0SNrfsmWsfE3LAMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6asR6YoAn7rQOTIce_8njoIbHtB8WHXPTqbsblQKwRH0vzivFYZRx46Kk68FefB2ELXfkEi7_Oti51BCdaJiVji6uifXolpSRFSt-uU_8XQlk7PwEsKl-xn4ody2K-QvKmLXmuNX03VvrNxK8hl_pY7BbPxwNPn1jvfhK_cXNbC8rIV4fcCfy03KHZz3wFybljgRC93uKRhso3ehrCigxW9A7hoD6wLhH1qzLhOB1DewLxZuy9cFXEmMoYwnvWPOC2IZLPdZDMyPCuUTD0zuJN36udRyTYrYZUrkoGxkceSYfS3Tz30Ge1fD7nNGjooRYt_lslx23uWiBuG-piJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4BXMvexfZPaHOUZfqsyeAkyD7-HB_x8DzGhULrdLf1t4hgRyiOKKULxoBc_Zz8wkA0WBmbFHv-BhwjF6yOYxn6RV6YmHQuGtFAPsgRl9wA1zwW7ajLTS-yRW5HFwW8QkoaY1n-rOg8WeH0H-MzFwBWRcOlabXxORp04wWxoeyKnqupyBVJXWLKOnXV-ClCvnANZcAatjlJnAWsotAmyjmv-jsBlIjsxeBo8VGK5aBDdJiHpDEeD6vk5lXHr223d3XAefQU321F5Q3A85LQq4tZd54zv6bFxn38sjfCm8TuxMwcpdGo9fO_a6K4QFG6JJwJrcUmgFeGhFdzr-2YPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzWi8iHW4OSOppPEpsdBJXttrfGdppDBFTxrqG4niQhdcQGyhELVRxHRX2F9Td-wPlLTYkCIqASEDRRsvZauYoJeW0p_8NBfEqpUDx2jlWXMeKSJuP-9P6R2YxOpJ7DeoCBcK-RUV3-4v5qkP5fzG4QfL7rrFqoGD_w6we5HpaEEo_xbe_1JYGxnxKnS3wC130gCwiPTowEDq5pNZBTScaI0Bh_K7b1IqPiZ3n81v8M1bitxPmVsosX2xD8qP-u94-euzWfVvxYP5eld3pXaWKXnaHzLCVr-C90FReTLtWpSjG98dzEIepUgT1Wb-O2rGDyeMzdbgcfmi6rA7YrJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=Uzvfi-GGvC9uSjfEgAcq3ErUj21iIgj21Njomxdk9gwzwSIdRbnLr0nbzwxCX7974M4aMCjhP5bTru0a4fjNYVpKLF4NW5u4FZHwCxWHqCEu6oUPILOP9hbEi0grX01sYYoKA0KXe2ZE4s2Fe8CCEAv5MtGAK2I6-h9hWTNtwFDo6dYxgh5tALFkbY6N6cjPQNd6-WQ0j09eRPCmvG8M9ODuRVUvYalQ_mNiylYBCZrSR8mizG-8qRB9vIwSp4ZwVyfNi0re6uMwrSRVYDWS_0U5hl-F1i3toqxpXeJIR1n4k4WGa0majgRZLx8kvVWhgRpSm4BAIUtqS-5ZcAxueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=Uzvfi-GGvC9uSjfEgAcq3ErUj21iIgj21Njomxdk9gwzwSIdRbnLr0nbzwxCX7974M4aMCjhP5bTru0a4fjNYVpKLF4NW5u4FZHwCxWHqCEu6oUPILOP9hbEi0grX01sYYoKA0KXe2ZE4s2Fe8CCEAv5MtGAK2I6-h9hWTNtwFDo6dYxgh5tALFkbY6N6cjPQNd6-WQ0j09eRPCmvG8M9ODuRVUvYalQ_mNiylYBCZrSR8mizG-8qRB9vIwSp4ZwVyfNi0re6uMwrSRVYDWS_0U5hl-F1i3toqxpXeJIR1n4k4WGa0majgRZLx8kvVWhgRpSm4BAIUtqS-5ZcAxueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei0do-XWbflePx7GEqu6wjDgwTwGe5Sr736x5FEwHlJXU8nVcm7JIPvYFt_wo-awTmV-0N8VjGMs4N4-UKEH_ZshaeZ6GsSkHpgom69eyDHMLcclVJvSmMoiixQPGQBZG-w1jKjk02z7naWDHQr8i0VKaf15dZdpcL9I-hsKn3gH9V5xSwCz2J8Cq5WHoFuRAKoiL8WqhSoiSOzERf5YA2VARcCcWIxHE2OOodFOC1bbSlJzZqTp6g6DpXZvLdco2g7rW26M5QEqJzQMD2HB112DXnHptINnqlRJNb6lRlPMovyOP8KPQgicgA0d7bpr6-NZTEp-2uEFHPAVHRU2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXUI9XRepSgITwQjhyED-H-NFIq0015SiAc-BeE_HpEozqooTRMCShd-z5lXLpvTNmJ-IBG9Y4z1fTA63iBis15lnE4NBQXzyPmaPh9Ys84maPypcA_-GXPHAv6n_yRmWUEPPTdXfHZq3Lk5L_sAi5BaWPwn0OoyjjJhOYcaHpXo7fd1j5cvjL6Z9Bl-epTqAJl57Za22EEAD8Ep4FL9nYsnyX7GlXciGrolXOm748dbpM7resDZJpRVlYa1x0HQPtZScpJDyS2B_YFf6VNXrxFnev-5OcG66drdTIOHQjDYEz3mtoKUPV--chYqPdFXV8rwhjrxmDcZM-KdmYJkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwfxAUur-xLchQtW8BMcLXXhbj9VBBjmVgtz6gHkLpxwuZXdnZjLCaW7zpUrCT4-LDjiYt-ZrvO5doq1O80jfqWd07r-thdnKKXCIbNyJN3T7NMDJItAQR9DVY1NWXlBd9SSHNyWf5G1S8ANe8pFWrEEAIgTEnBcsrrAX-kZy5vQCsWanQGd7X-6pGLIbqo5tL_ZOlUfpyvDGf3Y32ufN47F2-Ai-eq586hR7hBDNNedpK1TbckcYrEru_l8t2mYVZvXFGNDPz9jknVsaFU4-QVlrE8kQ4poX2vQoayR4WX96PtTBY7BDxGle5Y6rCWybEeDTma1S9rBgW7RLXYrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=eH7VGGvtdAGe_N_kNSZ_L4kPmA5_42TgVUZI57Mw5r-rP3PJ3gPXhhN_8aaGzt41SIWqOqHBKIit-YsZRnHBZkpnqaqM-IdoD_FLtt1PPXBTz3hapvsKzEXfl59qC0uxreLUo4p4oIL8HYiUKp7KgsTZvi2mtsOaa9D5sa5aUsqPcfqnsSyMqQgX-mgt9gKoP6nxlcXZGXcua9mAlSLSZKHzvcivr2_HFtI-tzTjyONCERVj-HBvBaYtpJird0js3Ycogdj6kVl6j3G4-_AZXscHW6aB2IrrGWniHouJOh7AMdThhTpE1XoJfTRQZRzRwp9_cpqyafT-1RsgyxGR4781zYnQI90rdrKzfSA5i66NTKt8jvx1aGAjvs_lAk_8UP0hje79S9IiqfzWmNA92j5DUOU8zo4vIupNL4VtX4yMmfnfy8fk-YpS_1Cl5lcEwZwX0szk6FgGHfwGgNgATlp5ZBb3dYz4m8qAhCDS5U6Jofr_g3y_RlLMVrXeAyZNP-1Qdh-OAKvbxpQ_cfhOdDUhK1Rbl171XG7wQ_qZJqiDyKo1iNKksIHzQ5z84wymjdBy_3X0-s9e_4Ce7Sa7LHkLY2vXtQVo7F1s-qlsXHDUJ4QR4qgu4JVY1ZV3IPuP9CYmhNYqtWfrZ9Ap33NIIz8gR9YTdcDURwWQpFAYETI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=eH7VGGvtdAGe_N_kNSZ_L4kPmA5_42TgVUZI57Mw5r-rP3PJ3gPXhhN_8aaGzt41SIWqOqHBKIit-YsZRnHBZkpnqaqM-IdoD_FLtt1PPXBTz3hapvsKzEXfl59qC0uxreLUo4p4oIL8HYiUKp7KgsTZvi2mtsOaa9D5sa5aUsqPcfqnsSyMqQgX-mgt9gKoP6nxlcXZGXcua9mAlSLSZKHzvcivr2_HFtI-tzTjyONCERVj-HBvBaYtpJird0js3Ycogdj6kVl6j3G4-_AZXscHW6aB2IrrGWniHouJOh7AMdThhTpE1XoJfTRQZRzRwp9_cpqyafT-1RsgyxGR4781zYnQI90rdrKzfSA5i66NTKt8jvx1aGAjvs_lAk_8UP0hje79S9IiqfzWmNA92j5DUOU8zo4vIupNL4VtX4yMmfnfy8fk-YpS_1Cl5lcEwZwX0szk6FgGHfwGgNgATlp5ZBb3dYz4m8qAhCDS5U6Jofr_g3y_RlLMVrXeAyZNP-1Qdh-OAKvbxpQ_cfhOdDUhK1Rbl171XG7wQ_qZJqiDyKo1iNKksIHzQ5z84wymjdBy_3X0-s9e_4Ce7Sa7LHkLY2vXtQVo7F1s-qlsXHDUJ4QR4qgu4JVY1ZV3IPuP9CYmhNYqtWfrZ9Ap33NIIz8gR9YTdcDURwWQpFAYETI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=vDZ3vUHABdFAi-pPeGWgpUw4XjiAvQLBDsYGbOBNfCafKYn7PP3jB_7gJFRwDNOWVcP0CZ5Yjv1IG-TxFosUZo11Zxtu6BTmYJD9qpIhy_EKX9i0271uDMLD1JuaV7RIjq2sSWF_sVNxQBH38st9-ewwBReSEJrI98JC3yINEL3fQyLkzo-n2D9d1FQKW6KrBco3rV7NCIW0hYaKgLYvriQ27roy0WHF9NynXzoMZ9QnJh7dOHwcJ_jL9IZOe_A4ycmgKXD5efty_GJaNvnIl3xhHqSuSbyj8AcE7Z7yKHCEr7s6I14ZSg0KEDFuA7TKtbWxa26WBg0w19tEe41waw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=vDZ3vUHABdFAi-pPeGWgpUw4XjiAvQLBDsYGbOBNfCafKYn7PP3jB_7gJFRwDNOWVcP0CZ5Yjv1IG-TxFosUZo11Zxtu6BTmYJD9qpIhy_EKX9i0271uDMLD1JuaV7RIjq2sSWF_sVNxQBH38st9-ewwBReSEJrI98JC3yINEL3fQyLkzo-n2D9d1FQKW6KrBco3rV7NCIW0hYaKgLYvriQ27roy0WHF9NynXzoMZ9QnJh7dOHwcJ_jL9IZOe_A4ycmgKXD5efty_GJaNvnIl3xhHqSuSbyj8AcE7Z7yKHCEr7s6I14ZSg0KEDFuA7TKtbWxa26WBg0w19tEe41waw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=i8tAhHkBeISsLzvkHslzEriQgc-VDqO4T8e9ZNtJqRc7-X6p84UruDpeeZ67GGpAn5QltCpXZaUW6fodntyhStF-SvuwQhVVQNNsO_4si87TVWxWFAW12Tb2ynSlOCMOWUqBmiwzQBqWlKgLZVhwyRagOsR79-Sql3kPIkiTguQ3ruUcHO6nty7vjgE9U--4FJcAvExCHH5pQxafiMb-7Kq0i5zPBwvWFOtlBrjwyx6mz-3Z1p9B0Xc01iP9fTTkZ9Q8dfH1PxNUSLb0r8Zd-fWol75xcSZxCI3Ca882a6hPj0YJM-75-w9PqHzA9D3Fzb-_SqN2Vjazh2oyafTrTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=i8tAhHkBeISsLzvkHslzEriQgc-VDqO4T8e9ZNtJqRc7-X6p84UruDpeeZ67GGpAn5QltCpXZaUW6fodntyhStF-SvuwQhVVQNNsO_4si87TVWxWFAW12Tb2ynSlOCMOWUqBmiwzQBqWlKgLZVhwyRagOsR79-Sql3kPIkiTguQ3ruUcHO6nty7vjgE9U--4FJcAvExCHH5pQxafiMb-7Kq0i5zPBwvWFOtlBrjwyx6mz-3Z1p9B0Xc01iP9fTTkZ9Q8dfH1PxNUSLb0r8Zd-fWol75xcSZxCI3Ca882a6hPj0YJM-75-w9PqHzA9D3Fzb-_SqN2Vjazh2oyafTrTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=uPB764-umhfSCe-2fiep8uIoyvg9YZl2MlsdmlsfoZosv9ZMWFLUXNm-S1oceq7e7J59tyJYSytVH6UKopp1J-dS5Z5KICtWomysi_2UuI9NTEQyWA6sikTSWDPbSf3CLFveE3j8gTz5PCQKY1SyMXA8iEaNS2PZvgKHGvh_ZCZ6jnBOM-LKexx2AxiIS5FzR82fmoG2Acd8dyyo7jr6r9HCrTByr_N0zGa-OCWDUGygmG9oTnv2J5-6PMSQvIkL5cMmVEHiIm7kie-QaNqtnSOEt-h_qbXKNEwit6kgCjG1bWHQ1yxZ8XrvcW5my9XtAK0Vqc3OUWd19iQ8GREGFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=uPB764-umhfSCe-2fiep8uIoyvg9YZl2MlsdmlsfoZosv9ZMWFLUXNm-S1oceq7e7J59tyJYSytVH6UKopp1J-dS5Z5KICtWomysi_2UuI9NTEQyWA6sikTSWDPbSf3CLFveE3j8gTz5PCQKY1SyMXA8iEaNS2PZvgKHGvh_ZCZ6jnBOM-LKexx2AxiIS5FzR82fmoG2Acd8dyyo7jr6r9HCrTByr_N0zGa-OCWDUGygmG9oTnv2J5-6PMSQvIkL5cMmVEHiIm7kie-QaNqtnSOEt-h_qbXKNEwit6kgCjG1bWHQ1yxZ8XrvcW5my9XtAK0Vqc3OUWd19iQ8GREGFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
