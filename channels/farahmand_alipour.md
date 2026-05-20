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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkVkzyC_uRz7k4O9z7HFCLYPdU8GRwMxGMq71CuV2Mq1FMMpneLMpqm8pIJ5rFeugE5Y0RsPBuGr1EtR8Pto9BDB18r4lStNGhDuOcklYiI7qVnEQ5BG7XXFcUabOdYK1z625KXo-jabWy0VpSUxfqC8asJtthCwWRDYQSVBwZ8CxfAQlnYwkxFu5aamDZzgy3B6425krwk9waSE9b0C4euubzDrRPbNM8YobE_-gH-r9Lrb2cENUfyHB6oOrSxt2ZIl_ajYKyTN_XlYGzQUsGA9pC4s8PI1zoyLfzfVceSyn0z1T2K_wwu91lGBUuKjXZzgzOw46gj9iplJp187Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 401 · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE2fAIBXlERRIxNP_ypVuEEMAophK4T00pmS5UhHJ5SWaAQkEf5PnCf9I_JaSvom7uNgagvUUFe0vyHTYylmaigLYTLSEd38cuvXzzMbOy27wFXhVzT-dsjSXGONvViacKZwoZs9NkwRPTcqppoP4aZ-hqZiKBlDWJgBa-TOFYU84625e2YgtD3NS0s0gq1COFfDln7175bUGvjPxLdFI7-rxjcPD8r0DD0eGGuaQNxgf-dO8XkEJ9CsCmc-OhD5VS4Qo9b6p_okRtYYOfhub1Cy77PFQskboIuInms8Iic-wYv58ywA0a9gQlypYRZTvJ8XB5DlOMq-L6X0gEPltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPCc1yKpVOmap01bOdccSEt0yVfbg1tALUPbROUeOmpgJpCH2yF5kKdEmyyYfztD5Hw0XTP-fEnfePF0Ryj0PW5bEVRVawaHa6p725-mKVaL4zsE3f50WVMHhVhYgba-RrgclWsSRTf0e6Z3My2242Ro3wRbnuKDZUrOO8Lpmw3M6Lip2Fqkpano79cCl0oERfEN4G-QA_CDL_N9F7qItHNH6BlIDJigN_3m8J8-lFWEHU1UG7IQ7wSFPPmYA-BDFk2Fy9SpVW2_Upodk8SSZGv08GKA1gpQv6PacEm42q04TGaJFxeh0xt1t2W1fUKg-5b_q3BMwfQaxFLSxGDTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNl5Tfjqilj9PGtk6OD44yOZJq9-PfqplTRmvWxnTsZnkNc4hS--vT87v8cXMNRvFzDMaHORt2kUBPQLoSimcl2D8pupwiq0dHeGAJFbU4xszlQbfSXvGK2TIbV5PL1p3JmS3yJP57vDYo8NIkEM_e3e_gTmfOAJDczEqlagAnmpLypKQPPnJYeoTdg3NYw7UUU3V71srp2dONY-VOZlZBFpaCLnzoKFg2ORT3rL1S_Pg3_obdTI7PH6-GeHIhmtMWErqarfNr9UnD5jPR2ynKY8XH9HmDT6ogScqql45DIFv79x9wFD9JsY_vVPMPCAzj4e8pQviUmiJqQKOyU5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuJ_odOrLtzR7yQCI0BGLislu4h3tvQZiz-fENELOLcbjl8JwNS6uk2ruMvNg3QmZYW-5PvrrMaXwnKESkrRbJECKPGPRUfXTghfrrSxKGJFya0WMno1uC5AY73-LinCnMCHNernYjjhSvWVWJjYGmlAANBdoyGIwuBKHus8H20cwAO1OBYYxCMmJ2-qyElYkO5cnYek1Ojfr7a7BnY4PSBlbhgxI_XVy92kisIz9ha7EdX9obSWiINFpdJ5BD2cENDCUTmI43MDEM-wxAvj9hIbT4odP_tTZ6ps_iDLKACCjEvTtEyU6qRrzH_1zpNvW555qKa9nSA0jhpLjxzQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEQbB47J2zhG2hWTCRpLCQeJ6XaJ4fg166JIiyPyTJvz1LS4rsSAaCgLebPuB7tXCQa6QGE4I0IiDIZt1vW-CIZgjNO4W4-0Uz2yVSdgfzxQL6QELKqPaN0v0oOj3vW0QRNhaO8PE4I-ZHzAHafwCqmfGSdwe19R8ICcouWSr1KW0N4tjMFV2jpzoH-Ch9xLOzfdM_cXChkeTOdZDFtrErF0ySIqlq8d7yIsh_kESgZnU2U94x9HwQBuFRajCF80zUoaRjSYPUEjQqgX7BdDHFws5ykAL5dhPQoU3n8W_G_EUvxOzjAH9dFJxJkm07vR7mSwR8c-VyMJWPy7KFCFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_Etzn-dRanSaUEc7zrD5_LRqA1-IAMW-wv0El6NjJ2C0NY9Ti-WOvswmAiwalvw975gOvo4AmikpcOyPO6TMWr3edIQu88UWaUXSHLLcC_2CcxHczWkrGU3YiCKAUjRo_TzLJjQoUcejQm9XGbWxPjjLXi0JO4oa9StDX3HYVO1T_wpq9gkyWz-j_nnLTZfq1fc9XeFkPefpSgmbGlU9ejtvJxaMiR7L6J7eTawEFTPIc9EgGm2oZHlR2R_0k3GYf0XtGby-YdnrhDWakCg0Sr1xOPv8UmPRK2QXtS3JN5ZlEE1vSrCt2ofhqYKKyijPT9mwaQv5QibwQFYmYafUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivlYWsWE8pxcKQ4MkAuOtlN1HCsKhq0xtMu6Lob2-6d9gE-gReQCYgW6UsNYtEiuScrQGzY9nrccwXOE2d_dzR0zp6_-SKv0MiYZlSPnOmMwqf6MIt3JbViD4DL2EOeLlZrDS3vNGk0w8xY7f46xJF3Rdj1vyHmPlbe6iizQWJNGqPcagjVqdbEcAGeoMqGgCVDxNV4wZ4lJ2AciRfpZX4ULzCQwEI9PJyT84JKH4sZiJhUHBvkdJEtWRbXybZP4qdY_wJ_jUe58WNsyZ8HQtzMnSg-IVWJDUZJDzgRv5CvRaZovBAwfSEDuNgk6-yMI26SCWiVjg74nZIFV0TVPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7F2PfQ3YfF3n5lZ1UZtqtc-F7bbC76XY8XbPcxn2Gwr-KdSTsSvftmVqmaXojq8WG6-pCQFFKRasS3Sptvio1uDzKAm9Od_PVVORbgCNeHxO5CjX8wjWWsHz_UeA7yFptZKDPLvmugEWdVKTvKAtOOPFF0iNR4CytpPrHi-Fr6H6ywV-dHkj7M8M5tyWI2voy3Agm4zKWt4UWgK6kQ86rGIQZVnQEYGqbFA0q2gPcSMFteB2yHK8OYt-WDZsgjsWJGN20QxZdYhXGpUOtBC95fuOi7D0iBWUDAmMPZFo5cqo3WOsMhHnzlH2lQXcqmrg-S5fKvh4H9Sy0csE4fJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALGu3oyk29BmNLzUGIn1v7a1SUPn7cjDgawhmzcVGkBYaiKYq10WiRWyOOwELXhO9gmYVgyd2uuJRr90NTDcD7jHqrWI1E1JLFkTFIkqQV5F-87qvpsQ_lP9XrnX76_Fu7pMjst1aXOS4VggjaChBM3TxG0jDxRTdQF6r_NLVuxFkF-K1FbskiCWqqfppLJwA3H5OisQoPQeTNNb6b6hBhDXqsSdFjjNzwL2S9EtD_8UlH_HJfjhxiRomI6fColleBxxq9tHZuSj-_0EYbW927NA1y_jsdnsyq3T3w2NCHX7U5oTb7VxOuC9cpwpod_5Wploh3QCukiw7NeUVGAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACUGh3arGkX-E5PEp314WG_cWS_qQ0Lk0SZHzMg1-yP8NnyXzmzBbWaDvvzonpSksaS7kFUwzZ2tyNxbGKMUiOXcWugUL2aCPrOQfEr18iEvge9E-uZThd5I-U86AQaIe-SMufPHv5zDX53etpVpqov2byNECVDiuIVh8lhLDz8xTG2yq-6yNLR-jj_w3B03ZOUoZbOgqSzHtPamuXEeG_CNdOYO0B-0V2kTpxA7adWcgNvpTF9ftL2LKn6eZuGLWZ4gIutKBSP620pTtl7nyoYcA9yviEPMGTLyt1dHLnyRz6pz4yd6PHOYCIXe-766nBpy7q5zN3TLKwfYrM6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRa9adj3QeciuAGjCBqiHJvTeTMLE99Crz4elijt3Fhlbj1-oGVTRlvVvYSG7LDR7F5xIqIcEFVga6eWGSB2cfuPNmc1TG0UsoWVzTCE3yjZKHw9_9Un9_9a-Wcyt6JyHB1qeXXA4VJ2_PZVme2OyI8IcpCNQ48tpGPcHtMYeZeo3CR4dZ7MRTuax5o7hyV8yrlx-74CutQdD7Ruwgio7sE0OILqIF2GloS736mO751RD5lGYUBlk2MU1vib8mVbe6lA7jG0u_08nEEj4viYeyy-2Pul785bx18NWmc70s51fs7VWp3xbyINgrbq6tYXb2CyHiXQUBT_atmyCcVsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIL-c0G2IN5nMqgvuktU_0eDqNZ-LlWiR2qpJkjs-8drMNnG6BMe9MH4iQTlXhk-mDeZuZjHVyIMQtEgzSYg8aUT_EafXeE-9GefqZQ8Jdf8kIiz5teFk4livqRV4G-WktjJIV7BFPMJ1G1xm-r_v45zw4lc_8FWeJKKAl19D_x5JTosWLEtV01roX-SQsy0JEtofhqgZgq4r6gugQaoU5bJ7xCRDCdYmhfeqsY7dwwSqjcDuc0rVpxx-5Q57QSeBi1mLcJ3Vh7wgNctE1Cc7LgE5bR1RhHqTorsbPI-8rmG9qXo11U500jeRDCkT3Y6AyiIpUy0wm4J5kGXfnz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAcAvClTwIZuhhMQBvP8uWKQ4tSAy5Fzj2BcA_r22pm9at1FCe0l3UnmksDEiZgPfKo0bC_k2lX6bKeCe3GPbB13J8Vs4pPPhtxBgXvibA0fJy9EhP_RwJarGTvsj6ioqpdiooyd3Pc5FXEqdQvzo-F1Girpir8bre2KVTbkjbLqeZ1R9i3mb9fXMRUq5h_mfDAwpUV7qExgKrrhbEsPE8ZXAjV6QHxxFxGRQkB3AknbD7-k-2x2JLsPuV756Juff_9u7tRZArIKzZ-VTmukw0cblxr4ito4kjEus2RbaiKsPamUf1ukn5-XDtAU6eKDigCgihr6jBjeZAly41LnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USdMiBqtxv1o2devQUgOAspG-om6YBYkkOeLo_p6EU4741FHtsytr2NTjqtkcYgyPrjeRJQ4h-SLvI00giO5ecvgnK38v6LR7ivWzm9Yaeg1X-og0U61mcJOYUD1IGmjZbiAEsz7tE4Ea7X7wdJ8fpcPR5jbJuW8qrl8B-7dl7GB98sFC9qA7ha-lYDwfOuVf7eW2l10QOJHTADxqjis0hGWOzdAR2DFll_KifCzNTw4mv6IubGVc3yRV6hauj2am-wgoHzuZPZfob5pGNcK0_gGnGsuFoKHqH96lJL_iVRXktprah9VTto1E6oiN8te9PlOinZ724z28oglKpb24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugV7DplWWqPW2MbXrmZSQK3LfRVCdLjNypxgzpKffksPrul5vTjz5vdGoH7JzzPGon2s12ZXnRAnoECHEDVeA957l8jGlmy_odMGodSJ_Qrzh4d6yD5vwM5ZCb-9UuUN_OKKW6ZZ-cxbXLJaM5YUS8t52Okixtg3S4sKdX2UmNzPUJpcyTGSPQHgW7uG7VhBAUyRWA1x9LK77V93AgjCSlV5rqLJMxr-ADc0QgmHClyh1BYuskiLA6B6yLXw0j_hKZSzzNDL4CnM3MC3ZoW0_F6iKLYZRtxGjF4Y1HtGgg1VekRt4J6kBxFezUIYxKUsLPjRmJPCOekiA2PrUzEhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=aqCJCBd4D50QvzJgDC_uoGj-D6PTP-KAz31DEAWcOluvJKyzxyFBuTlZJQpYBkKioUm0EkRQi0Hn84p_O4wHm3CsPNjv6YtH65lwYGwIo2jyj2DKbQX8yRy9bbNqVESyLPG0s07u9g-9Djn2wTwURtrYAYe7VmC8W7shRJY2qkDk0E4GEK6fyS8Sb7jOOuWYPac513x41PyIRj_PBHAmV08VFu29ELU9pM8aKJdKQX0FCX4ihlYENkL5gdaEizcGE_ZpL7_tN_7E9i2u9ZD53uggj30Bu68L22DVBuQkyalgswqALr7IO85i7ql8DOjM2GvizADy1RxpKr-lOj5WCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=aqCJCBd4D50QvzJgDC_uoGj-D6PTP-KAz31DEAWcOluvJKyzxyFBuTlZJQpYBkKioUm0EkRQi0Hn84p_O4wHm3CsPNjv6YtH65lwYGwIo2jyj2DKbQX8yRy9bbNqVESyLPG0s07u9g-9Djn2wTwURtrYAYe7VmC8W7shRJY2qkDk0E4GEK6fyS8Sb7jOOuWYPac513x41PyIRj_PBHAmV08VFu29ELU9pM8aKJdKQX0FCX4ihlYENkL5gdaEizcGE_ZpL7_tN_7E9i2u9ZD53uggj30Bu68L22DVBuQkyalgswqALr7IO85i7ql8DOjM2GvizADy1RxpKr-lOj5WCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHmt5hDPTgASZ9BQex1RCSp8qTm6kOSr3ACYyoz0B2ZG5gVri8zRhvnzhNRUfY-0Vaz7hr9AMLbSt5GNosAaLXoeR_I23XC3kTjFZYpq4hyvF1ecC8_7uXpCtNuPMzjbue5XH1SBNerONXK7eXhx7HcaX3Iyp1TDI4IUHiY35Y4c_op3heK_2MoETGsWyXNViNbA4J0DTVqVEmU-zejFuurxTqTQlvrsejHuouAPA5hVel0VGZcyjoQOg_cczMjc74HXiShsa055azVsVUEYzqI3YAnykheiGStBg27LqKDDoodqkvSg8-zyxdqCFXTuaJ4D4IT_T__BzQQYOhwWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ3rCfiIiELSjDHNbDX6qGisaS3cC3GljlKIm1276nkVg1jy8pHep1HaF7-b-9WvTn45w87NLhgZD3a7RWJRw7b0oJ1jzuK5iYSBVUOitRbJqesV0vdjp1qlfr_68t1-4CwcYaHC3GFskz_NmqsvM-a1zo85yMdlOag1E8kvUph8TXCIUmF1fkEexSLC04sT8Q9jXmXugo7Fs8wPkUqFJBSb6BC6heuzLwlV1jaLW0qUX0iIalgqb95CFOsMC0I9JTrVPWpMcistj5iGuH4RKwtutn51nsQfOz_Ji_muFiOWu52z2RZ76BGLWuZCypw09cHDxjdgWuqkGk66pFI_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDDHB1baNCGtXk1S7SiLzBD1rIDavuIAzoKbOz6XJQFtiJA5Dyw4axNuPU6Ojdbv498FTIdg94BKPM6-HBw4qSt1M2Ho-RoogwHybzUFHkyJOpVG_HUb5BmJ2tAk-lT26eSxFsPfkHXdt2Ij6qI3DNEB43Tp8PYUuS11fD7IybBSKVRfcFUtgMfA-z-Oruwf2oQCUpXwbxSD7uBNtygQJG22sgc9n1WUKV-zqD6pZcPyGKvGTFy4IELn9M3mnSOxne5Oy9siv7o8-_dkA_H4lPcVPQLsf6WGlbulmMStkQOBPiQrltIrHzshbuxr7y6F8A4Ey3YqZ86lFEMgOs6v1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq3k-G6CRP1JiVtpNJs_Jote4P6zBp6wU9P5_v1lH7D6weN9GJzW9s2HP5GXrw0MO5HQDCSTAtll6TEXPijgC2qxKRZpfgFbxl_oZANAtyotL5LhHqM4W5YINpNzRGH8j76Gliz20UuTG7JSJgH59j5HtraZiLBHV8t-TFd3H6bt_8vflTa18sbZYIN30ikVFNM_y-eMEmLIoZp-VDGw2EnsKJ8T3MERqm4QQrIKyshwMKfKY7zi41p0bZf7H1wZ7m8X-yGtCf3LYNwXNY6CZRYEWVk-0noK4HRK4legBl6CskpKwFJL2ueiMFQ6OcTJIJ52m1sLPP_3_aDG9ezkwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=Hq4z_tAO_-MTQAFRkaFtQWZXst-hzRRVjoylvU33iUMdgYofRrUfkX9_SyTiTd6zMqdI4ytS-mqjFlKTyDsUJwWNln02RAa7ukl5-meIfGsw0J_lKnKvAj-geN_WThVRnV5LsZK9II8xdtR6ZLa6RwRaMTUBK-ZtbKTx4P_OELjM3JkGhdX8KDPlbgDqY6iL2Up3Xa9mWRJ2X24W3q-OUqTAMAZgnOvkew-rXw7qqg5Zjqm5q2UdbMl2QPYuCvZf7-nd8yO58H_y8Dao4n8udtBjQ-qkMWV5g3AghpWcHlAKsy4L2YbQTx5vdxhD6QMNp8C2MNXWIyxgfYdQC9i72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=Hq4z_tAO_-MTQAFRkaFtQWZXst-hzRRVjoylvU33iUMdgYofRrUfkX9_SyTiTd6zMqdI4ytS-mqjFlKTyDsUJwWNln02RAa7ukl5-meIfGsw0J_lKnKvAj-geN_WThVRnV5LsZK9II8xdtR6ZLa6RwRaMTUBK-ZtbKTx4P_OELjM3JkGhdX8KDPlbgDqY6iL2Up3Xa9mWRJ2X24W3q-OUqTAMAZgnOvkew-rXw7qqg5Zjqm5q2UdbMl2QPYuCvZf7-nd8yO58H_y8Dao4n8udtBjQ-qkMWV5g3AghpWcHlAKsy4L2YbQTx5vdxhD6QMNp8C2MNXWIyxgfYdQC9i72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rw-p_xe047ATfjuylWpX1qjtUDhLIwmMaqN6XEr3ii2iV8QGd7Dat9_yc980nS-1AYQefOBvud4PrzO0hAtVwfuEOPq2rxMkzmTd5rgiZFxT35y0mIiqr_-CHOTsVGRyRivTHIp0fbVHAUQMfaQDKIflf-YhhGTnM-KJ5Akl-rBxyO_r6xXlDmE-6l21-LCRHPJWDG0O3qUticN7Hw4m5nY4unLP5sriNd-atteUpcwGjdY-j9OTDWuQl34po2K2Ri0bRuwLCWJOEI2O0x825WxXoBdsTzcOcYE2g7l3BFCd9ounzXODnwByxPzHbpKYeOci-KeQIwVrbgBddXzl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rw-p_xe047ATfjuylWpX1qjtUDhLIwmMaqN6XEr3ii2iV8QGd7Dat9_yc980nS-1AYQefOBvud4PrzO0hAtVwfuEOPq2rxMkzmTd5rgiZFxT35y0mIiqr_-CHOTsVGRyRivTHIp0fbVHAUQMfaQDKIflf-YhhGTnM-KJ5Akl-rBxyO_r6xXlDmE-6l21-LCRHPJWDG0O3qUticN7Hw4m5nY4unLP5sriNd-atteUpcwGjdY-j9OTDWuQl34po2K2Ri0bRuwLCWJOEI2O0x825WxXoBdsTzcOcYE2g7l3BFCd9ounzXODnwByxPzHbpKYeOci-KeQIwVrbgBddXzl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7r0S9UvsyZf7xA1NYpI1kVXB89nKCWGfY4k3G5HCODJO1R5vCERKJ1C7tyXqPTNDbXE5No0h4kJODTCaRB_VBXK4UMpE-vBKHdzXRnRmePH_sMPF-s5KjAksnYXFsG1x-Oxy1Cpz7CTnZReEleU0T9MB_gBMvGQay30hQ2UNcNa3Dy5ByPp-UxZll0N_7Sf8PT_0HMOljfhVCwqXPhXvXymQeEZ-QW_ZvgMDA5WmZTAqOu2RWYdx9gjVefSHM1fXUJ9AD9lfDhsAgS08L1DVouJKnJ55W54uGBOR2vKaRuxBTiQiivJIxY4BR9Bo5mh124eQFzZ-Q2XlCWhD8m_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb7jDxx1orhsTiCtZS_XSlASHCqHPtgf-SYvzIc-zYo6sVU0Bk7XCMU6sIvnXVOzU7DNjuwkXFDDCV1cH2uauDUydPEdm-C-rBLTvF4RkH4JNc8Bt7MWEFfB5q8Jhl9QvuuE7rwYbDZGS0eXCBb-n4vPbAmd43VnrtGC2eo2vd-ZQcDN4LsX933qwOB_ae4asksRLExoF3YAu0pwFUQPAt833d8kqnXom2Z0traJ_lpdS1k3JFKdfwopLJDHM-x0SzBBarGhtBFhEnape-xOYfsV9v2KcwrYYsXcOYE99pDNAA48utV8Hsd-fjPLTFMY96IOIby0q4fNXmUCKEpoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPeT7fqor8YgCOyxxStUf-RlK0Y1Zt182hZOYOQxdd3nKTbP6uDD_4SB_nIVTfadcxIBz10vCV6PqDoI8yTMdSEXBni6qCcGxBd1AXTiZAtFzK7H-1nHp-jVMmcuOZH-OFl5s7hjVnEqzCOPpGzkb8UA8rEc9qHMU_lZT8ED5M-wcFch-xbcqvkEZ9sDmDADGG8T6FlhGskHDSHGdGXsfQKHjHC63NQAGPFxevNPgQyub3th-d9cs7luWqHy1fHE_ca2XpAFppNx4OuN_zB4GzLW0fZuvX58GZ59Ujudz0pVmELwSEqaWOeNADsXpCjSwJkRyJFYQjzYVeM_1gvzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8mBr2ywKOjQ7TAYc3YckIOP9nmbXyDxYfFUvMu83sfS_HA9zHHmvaQrlM2M8J1sJ2XDkgdf5I48mvnoFGyAOn4UtjbH8nW7JUgk_5gLN3o8IHCf-0QJPrZ12pjXx34kq6wv2ZJxF30b5Y_ESi_Xgi40WUvTow8ESoH7OwiwOFjSga2zq-z6loBBFSjia9Q3Y6xeOeH57Vvn0Kx0nSvUgy0U7D75FsuSpHf1V7pD87nft1vDJuapTx1mTmMlF_Z4SZE9PoxSGraVegHoq6cf1qJePmBoFSAwJyrg-8maDFINnEU1GdDcNaYbopROFdfW4tDsUQ18fJMidXqHlLE9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=t7ZwFt8c3KY7CR8WeKi2xDg6SoaiMxDGvlMamhDRLY1jVBUKkFEitnqwHJAMY6qgvDhe5Mkag6HHq9a0As3KdFkFxR7QFAgjG8iT88sqGwQwJrHPNhtnaOZzWHuquhQrU90VF9h2lhV8c611LlSl_Z_SXAQwE1f9J7uOlvNs_10J_paxD98XbA_kRe3yLwFJxmawnwvJYg0cdnMxsCYTnrrfvCY8Jm8wkbgsaVCMD92aQGXQNh-sz3D5rzxAT8Ppj6vCBLr7bNomfHHDDIc0X-WYhuL8q9yJZPubu6VLjfLtNyiUQhYZoW8McSI9U-d93sUfVY4VxF6meyjhWWKU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=t7ZwFt8c3KY7CR8WeKi2xDg6SoaiMxDGvlMamhDRLY1jVBUKkFEitnqwHJAMY6qgvDhe5Mkag6HHq9a0As3KdFkFxR7QFAgjG8iT88sqGwQwJrHPNhtnaOZzWHuquhQrU90VF9h2lhV8c611LlSl_Z_SXAQwE1f9J7uOlvNs_10J_paxD98XbA_kRe3yLwFJxmawnwvJYg0cdnMxsCYTnrrfvCY8Jm8wkbgsaVCMD92aQGXQNh-sz3D5rzxAT8Ppj6vCBLr7bNomfHHDDIc0X-WYhuL8q9yJZPubu6VLjfLtNyiUQhYZoW8McSI9U-d93sUfVY4VxF6meyjhWWKU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utRPaqayEF5E-4LsY6Lj3QLQxmpBSxefyEi4BUkm3FzF39Vp4G6Wl1F5En41HIlH3qN8-ckNs5wPTRmxZBERRet58pf9sloLhYDGt2jKvbb4f7KgPxlKegCf3_DnQjeWxvsK_UgiZkCFbWOrZ-OzWxvrhuiXf6Cc4vg7Vag5uPGo9yk17DlZtFlSn64ImKdiMagEP7W0L0UsONwMFyQWZr0tsdsrYHFuFU7WrO7bkBdZBmyKV-y5Ikz3UHJdTMJsxQMY6_MrZgb9gtadtckVIGCEb42rhw_46mhioF-vYPFIx_V8bIpXkHXKR6DJGKYmSWkyTJU4rng8yhnFDSndSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs_uiAceRbjfS8gu27D8HsGdBrHZA1iNG6FmYsOkDSGpmaxv7LPD0Ib7JvC45kOv7nBm9McwuQ8S3LMzxwqgpXk0mAvB3Ux0T0ATWXuMjXOs_whsk-Y_xlkCsXU5X60EGijLCO0laKSPDkQXW6qnwAXi7KNBDiWj3b6GwyUVbC714QpcEH66DO6X-Vl_z2I--ZRxVO_0hnSIDfaQT95AkkQR4GfpPyt63SvOG0LtO9inDpSxzgVR87qgfbfFFu0XQKUGL8PcMPbgN22n4kYDIE5LhD4cmlWB3YImJaFVzNu18IISDUhFoORPn9wx4OZK5_mgbdqbgCRtdftMk4lB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=fuk8eV8hk6BnPWwVyBXHIwaEI81NBJDYef0gtojs545fTE2Ifxon9usx0WVlytE4528r4s9KgxP9Zg-t4qA55FHGqKYtsWa4-_GDiozC-FHgzkGzb19g69W5_ajoAa8OvRkO_kYSgqmf4WJV1mubgEGTDRKSx6TY37ROIZOPekDPfaBVmHjrwRUc7aryYc75ltDaESQOepWv0e7bVdMYRH5zLmc9g7DGmuVaHaBndDzIXy7Vm6UIEoR6if71fzg-ZRzgKZpKBzfAisGKyA7XGSATHmVqtmKQdDjf3S367XQn-HQ4JUhKsrXLOJJ6rXKGQN1NG6qY2udDHtLoNTszEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=fuk8eV8hk6BnPWwVyBXHIwaEI81NBJDYef0gtojs545fTE2Ifxon9usx0WVlytE4528r4s9KgxP9Zg-t4qA55FHGqKYtsWa4-_GDiozC-FHgzkGzb19g69W5_ajoAa8OvRkO_kYSgqmf4WJV1mubgEGTDRKSx6TY37ROIZOPekDPfaBVmHjrwRUc7aryYc75ltDaESQOepWv0e7bVdMYRH5zLmc9g7DGmuVaHaBndDzIXy7Vm6UIEoR6if71fzg-ZRzgKZpKBzfAisGKyA7XGSATHmVqtmKQdDjf3S367XQn-HQ4JUhKsrXLOJJ6rXKGQN1NG6qY2udDHtLoNTszEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1otoQ9l_8-2YITccyADSZPL1WIZYEktZINmnsVQKYcfJdxPWgDRxKcgelaXugtbv-9lcRLPUNdhgYBtRHJF70VLZDO8SxnAZuxgzU16gusuV8rJN8DGHsetppd4WftzeBK6sHZ9Ault6QI9ZNoKnLOxuLRAhy2mAZnu34O9YgUZPlw4OpT0NNnESyJOtPTbJVQynsrJl5w7eE0iMm2air_ky5Qo8pZlR3X369ctLXWFxq4jJPA6FRcbRwCCQQzR1vczOMOK5ClJhsEv0Rf36N9psZksFZadlj-zJ1MMYnJnqX8NNXc4ZNuvH8O6GxNTC0Ue0InNwB-KiS95pSfyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=l4KGUJFnx4DA806SDGvhKNr3Tr3b9TpGqpYtSVTOp4ncAThbTZ50co-gFc-gpdrVkDVgpBByUw3uFESPSPShB5YmcAyaio6-Jccxua4srHQSfV-g28XmtO8BCyCsUYFLSA_AXPxZQcbH30PYeqgBVA3r4rWKEiFeuKL-yhzQKkxj8UK560zZJnkt_JMnlqIc-RjAFQ2lxgLqpAyLm65OxT6VD0E7oKCum04DRTWqmNYQqSL2s2yceB0X-yTnxob7p_4wkk5cHSgj2m20MLuKeN34LezLeukUsighjC7YS3KY8CRNsvepVi3CtZhYx1vkve45-Tj_TtUp-KqG2qNPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=l4KGUJFnx4DA806SDGvhKNr3Tr3b9TpGqpYtSVTOp4ncAThbTZ50co-gFc-gpdrVkDVgpBByUw3uFESPSPShB5YmcAyaio6-Jccxua4srHQSfV-g28XmtO8BCyCsUYFLSA_AXPxZQcbH30PYeqgBVA3r4rWKEiFeuKL-yhzQKkxj8UK560zZJnkt_JMnlqIc-RjAFQ2lxgLqpAyLm65OxT6VD0E7oKCum04DRTWqmNYQqSL2s2yceB0X-yTnxob7p_4wkk5cHSgj2m20MLuKeN34LezLeukUsighjC7YS3KY8CRNsvepVi3CtZhYx1vkve45-Tj_TtUp-KqG2qNPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=b2x4anMOb4zeAKWDDaQptMeTgiSRRaNtZuGgbU2cCB7tyXhJND6nxvQe3iF4mK17PaQwRutawOZIMS-uWxltIXTnEF3VNzVR-oK-BwmmYAvN87RsAeylZQbnkwQKgCZSz3aJBHF6f90WDqRC9VhNxQlJQ5CwDj1SsctGChjuYrCpO9qDGQrHScpXSz_F6SrrGo7AQzgdQcvqSbs7pZLGyOfUJcRYS8tXRm1-TpGiFL6KZNB954ztxdrxbhWWoUnOfZ1U_eVBvH4r3jzKJjO0yaLaymiqd5Ii1y1NRXfArxwj2NLyRLYbUpuXgj5eROyH3iWrwXEzNZdYDEQeBAP82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=b2x4anMOb4zeAKWDDaQptMeTgiSRRaNtZuGgbU2cCB7tyXhJND6nxvQe3iF4mK17PaQwRutawOZIMS-uWxltIXTnEF3VNzVR-oK-BwmmYAvN87RsAeylZQbnkwQKgCZSz3aJBHF6f90WDqRC9VhNxQlJQ5CwDj1SsctGChjuYrCpO9qDGQrHScpXSz_F6SrrGo7AQzgdQcvqSbs7pZLGyOfUJcRYS8tXRm1-TpGiFL6KZNB954ztxdrxbhWWoUnOfZ1U_eVBvH4r3jzKJjO0yaLaymiqd5Ii1y1NRXfArxwj2NLyRLYbUpuXgj5eROyH3iWrwXEzNZdYDEQeBAP82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=c2yE7pPnJ2N8qumvuvMK-FfMGx799Tl4oY7ENJLMusuD0LQYp4EnR3COefF_x6gJSoXq_2LUx12KaAjDtZ6P-akE57rI9oRL1yo2ko-u_DryGi1cTxBh1apewWbetpFGgxEOgBwgb8ZxX9MeEWH_fkPx1XIo02z5lnJ0cfXzHbPiLmDp6kh1Lx7PEAtQMhkv3xhIng7_UmvFm68nwmYHq1qOJz8vgv_7snp8ZqOIrrIye5X9coB7caG-MsGnTCiXIov-u9uT4y7ptJGFpOLpfvSkYkgHrpX900v9vCc0PXqjacPnPjyPRajx2XgkC3sy1EQnnW-S6DD3k3chaJwCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=c2yE7pPnJ2N8qumvuvMK-FfMGx799Tl4oY7ENJLMusuD0LQYp4EnR3COefF_x6gJSoXq_2LUx12KaAjDtZ6P-akE57rI9oRL1yo2ko-u_DryGi1cTxBh1apewWbetpFGgxEOgBwgb8ZxX9MeEWH_fkPx1XIo02z5lnJ0cfXzHbPiLmDp6kh1Lx7PEAtQMhkv3xhIng7_UmvFm68nwmYHq1qOJz8vgv_7snp8ZqOIrrIye5X9coB7caG-MsGnTCiXIov-u9uT4y7ptJGFpOLpfvSkYkgHrpX900v9vCc0PXqjacPnPjyPRajx2XgkC3sy1EQnnW-S6DD3k3chaJwCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=GcqZfkc6bo2wtvt56-aPsqRTmgH4JaKODCt1dNJJw6IoAef7iTVnGJH5y7XtVDqdOkTnuznfjutbN4UTM386z6i691owCM8mBMc98ZoyrNZBW94JKZ6y53AeTnoL6cl1UCVSyvVZQuWdt5MVNInmE3XOPbZ9MgJkQOvllz80ZTjofDHsh6ka5MfXRrJcFI7Ma7WzeHsENYeoOggIvCM6lSu3XAi8RhZsKvjujuzvbI58JgDoh83Gq1uPxIyd9mue4J2cBNnG2vhX6CP25cuQe-7n5tj5O2y16K7EoZAaTvSyuXF5LBQ-re7rw_U41dV2Fbhtuad-MA24fzHLd6m0uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=GcqZfkc6bo2wtvt56-aPsqRTmgH4JaKODCt1dNJJw6IoAef7iTVnGJH5y7XtVDqdOkTnuznfjutbN4UTM386z6i691owCM8mBMc98ZoyrNZBW94JKZ6y53AeTnoL6cl1UCVSyvVZQuWdt5MVNInmE3XOPbZ9MgJkQOvllz80ZTjofDHsh6ka5MfXRrJcFI7Ma7WzeHsENYeoOggIvCM6lSu3XAi8RhZsKvjujuzvbI58JgDoh83Gq1uPxIyd9mue4J2cBNnG2vhX6CP25cuQe-7n5tj5O2y16K7EoZAaTvSyuXF5LBQ-re7rw_U41dV2Fbhtuad-MA24fzHLd6m0uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNMFhDbD5g98rEhy2fm7UiY01l_b2YIDfWNqS9IvjqQfzoh47HfAwgz6q7UpDPpLbv7EpCSg_-G5BxW2ehgz_dONHEJKhNu60ovWbYZTHHQNUMQFC4-9zPGi7GsJFZ_1UTO5jVgW1PGrxIEQ8l9cQuwk3d8oxXzuxqvm1_BMY8I1x6SjLQBHb8OThEHUKlluXh-ZvA7ug-j-vtMAAB3dx4vtkV49kRWL6hGU0joRbmmTW69OOV16wOgxMyCm76aPG5Ya6VN00SZdAbhDuFdSNp-tlFgmDiBsy9Dyx5sbJUIOlayMhjb-T24rZfBAtlAbEJ8P0uvWm23Q4Zjix_frmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3SqC3fqJOuOY71SVzHDHX3pFaGsEAt76p807pQy0EzgMzHxx8TUzSaYBQfI8in1zHqvZHXg07gtHC7habfX4AgFQsTNGOjHx6r_PFrdXdo_fz6gwfpFwX2AxtPqMymjvxDcWZAp3EIMNydFEA6_prU0J3lMaNyQNbMe7hxwQeCXOpg_wjWJMVQCzO3CROzLcQh2j9jMlreR32Nk-rgYBFbIZHhbUNblzMbKe44HvMi_ToHC_wHhVTEe8QexavU3JJd7RdsA2EcF8XhjxD3P6j_SM4I5Zc2ZHdzebJ3ijHAPiITsHici8RgCcdP_GwNRvTAIiv00bTm1-CX7OPbxsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfKd2Yo1ITf7J1ZPkadpROG1uMbuSo3AhN0aEm-PGLNnGqPIZTevdIvcqv4IKPyYmWXCE58T6F2t871EgvL625eerxyKxW-Kd2KbdNcnN2NLqG_n75bEphWdUw2MmySxFkpn10xlBr_4Q7DYTyviqYTVKgODl34iBL1qf1gylk9vJ0i8DVsUfFFgBPfpdq4t3Jwg8YY7MJraJSwwVve-8qacEvLSHgt1sKfUpIC5wHozMrjbl9IVrdf7qfABE23a_DU0R_2m50bF_JSGNnSYAAzlAUKzHiGjvxNxQqloeV0MjVT-qn-eQ2wI24FfWofMaDT4sC3nTmv6uMFHZJ4bAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NokZ8ht7BljJQw8Irhj6seZInU0puWnfvv2wuuXQbZfFxY9Z6mMUBkheTEGO0-7MmNEL4MrMerHWcifIlYyAOssOr-CBgY8HuOlLQK_17vKX8owy4Tgb0ZLPeGytdebR5mgoYB1-0x3FlCiGSm6EtjxyXgIXeopU-UvTa7sKoO5HXP1LKyMRxHMiPK7g0AkeatrRyTYKsYrOnJaMCjBNS1bo-1A3BL3oHAPyplKd-l5pm8yOEc3yMZHQMddXiCsfzBSIDlg7QCQSjqj7y3mCIPOdUwx2YD2FQseM4PcPuzbeaFpmzFOq9k5HpOohCR2hp9enZ-WMpRNQJHcRXouP2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=KsTNDeuYxOjdSiz-Ivp4-tUxpgNl2yg-_L4oGlMLPvp82gDxj4S2ttrMV7vbTFkT8ryFwKPaZ_6vlK6cpP-0uaqDyHKeAkKAevUVgAxPu7m4zkZquMlfLM0RQkR180KuOHV8HGILd990cx3tkEjwiHIMvryEgnzrL5xaCHoqwrODle-wRVdHlLaHgp3HGVpLIIH1PBJBbWsf7XigmpEq_ReKf4zmnSmzcE8LM58M2lRQDxHgpVcoCIw1bF0gxskkNF_BJmZuZfcquNHFLGKCuUWJQeDHc8WGbsVldsQPyCgobTowcmkfCnnmzydG04b31Jtyb6yGYZ7GJ-MAUdPwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=KsTNDeuYxOjdSiz-Ivp4-tUxpgNl2yg-_L4oGlMLPvp82gDxj4S2ttrMV7vbTFkT8ryFwKPaZ_6vlK6cpP-0uaqDyHKeAkKAevUVgAxPu7m4zkZquMlfLM0RQkR180KuOHV8HGILd990cx3tkEjwiHIMvryEgnzrL5xaCHoqwrODle-wRVdHlLaHgp3HGVpLIIH1PBJBbWsf7XigmpEq_ReKf4zmnSmzcE8LM58M2lRQDxHgpVcoCIw1bF0gxskkNF_BJmZuZfcquNHFLGKCuUWJQeDHc8WGbsVldsQPyCgobTowcmkfCnnmzydG04b31Jtyb6yGYZ7GJ-MAUdPwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=KFbSXhNz___sZmwUo7g1Ekn14YWnvizX_x0sUDHem7rkdC65fIe9XTYRO6SrZw-ZkN7TQZPwxqmjPEf6yFYcmZY6kt87nV6q8Lhyqrk7npHb9W1_9PoUGW6nvlCYHGCc_6qOkp3qDJwyG6VcSCwpW0JiR2y2rLXz0lFgF7ka34dEtzhonlQexFk4N-z5qm7wNY5xnLe9Xqiblzm6H_sqTbaEq-hhC_7L9hHQ1mR8EBiCDl7glu6fGXmfsvTEMNgp5b7_lNLp9iyPgjYABUeVIdoUkNeribKXW2OHim32oBtIFWbI9C5bWlXx5yJjWKobIxcdnckLrYwcQETvkfTLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=KFbSXhNz___sZmwUo7g1Ekn14YWnvizX_x0sUDHem7rkdC65fIe9XTYRO6SrZw-ZkN7TQZPwxqmjPEf6yFYcmZY6kt87nV6q8Lhyqrk7npHb9W1_9PoUGW6nvlCYHGCc_6qOkp3qDJwyG6VcSCwpW0JiR2y2rLXz0lFgF7ka34dEtzhonlQexFk4N-z5qm7wNY5xnLe9Xqiblzm6H_sqTbaEq-hhC_7L9hHQ1mR8EBiCDl7glu6fGXmfsvTEMNgp5b7_lNLp9iyPgjYABUeVIdoUkNeribKXW2OHim32oBtIFWbI9C5bWlXx5yJjWKobIxcdnckLrYwcQETvkfTLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=iWDFgawgYZqvi88fOZd0R7vXWD7oTZHijIqrRBkfWvEaOwe13iG8I8Dh0apU5L_fbEPZujuc2eV0_QUG9G3B9Ph7dlBDc-5heLWcbySVfPri0QebeTz6p3s2hC4wI_5nTwuqHdmgyHNngxTt04Aanl0leQ0u164_7Pnc-7ZdlWcJlLw6IuxfoWXIYa9ZBReISVuKRTK9MLNGb_iJ0fCGBHQtx9DR0srHbOFZSBECrXJyoFN7NjHw68Ty1rNkHCOyG8S70yH4TrerjwX7Gk3S8KIb3RQ2REhyiULJTD2x-FQaL9cmMNvBeibDX1eGic6TpH5drrgICVTW8vmOxrtBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=iWDFgawgYZqvi88fOZd0R7vXWD7oTZHijIqrRBkfWvEaOwe13iG8I8Dh0apU5L_fbEPZujuc2eV0_QUG9G3B9Ph7dlBDc-5heLWcbySVfPri0QebeTz6p3s2hC4wI_5nTwuqHdmgyHNngxTt04Aanl0leQ0u164_7Pnc-7ZdlWcJlLw6IuxfoWXIYa9ZBReISVuKRTK9MLNGb_iJ0fCGBHQtx9DR0srHbOFZSBECrXJyoFN7NjHw68Ty1rNkHCOyG8S70yH4TrerjwX7Gk3S8KIb3RQ2REhyiULJTD2x-FQaL9cmMNvBeibDX1eGic6TpH5drrgICVTW8vmOxrtBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEumC3HKoyU-_Lq0InD3MNY90QZ8r7o2KMDEeIDReZMpefSdN3xyBIWHe85bejTyhguEhqDaMl48e3J19-TpeiWoODlICyYWPvrSJIkPyKHCDF0X0bDJ2b6YJkafkmjsDFZaRJQKraiwonPGkFsKzh7BLf3qxj8ddg7xu1uGDMOT9v50w1gZL_aN5fS-5vNy5be5ZxESyVgf0vJs6keN_NjKO4WCZ_6D4fhShEhD0J0K0kxteixrduODIaLf6T0DhLXhb6JlbCce_G3EH7NEZUzWUuuZTlTqOnqvzy1TUQke6iFxFCLo4aadXUW97BQE5WM1Igpenf7cge4hmjqzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=STLPZS55Xvj9mQalTofZTuV5OBrE2gEMbibN8ps9-qva84y4YObqngMk0MapsnGpDuaxwquB6fut6HwCdIde7RSKB3CsiL1FZ2dqH1S_oHbExoajqsQ2wc2O1CtR7KwE3VeA4Z5t5cvk16UAOiayC4WQuamaS72aKbUo3jvqHJG4roBMUW_MZG5C92Kv406hfGSJJoJsAcKXuBIspkUZ4PCLKqALUL4t3xySNxLIb58avN53YULPAKAzzk2L-OWXirGaLA7SEgwhTAAT8_pIJju5qpCK_UTsgwW4OoIu6reTnpPTs2TnN-eM7EJamMWfDovaN8qLc8kVfKL9Bih4d05aafIpGzAO4-1QdMoThtQ5SSqECUeluOdRZzFspZPmKkqk42S0XqsdCDYypx7ljxLSzLfIciO6FleQblkKnC_kFe-2GIYPEd7p4fORgarh8iz5zEwG0vjSF1r02uAKuQrfumzpkp_o3NBa7Ur5XWhPyzuQp-hJQSe_UwBSWeDn5OK4jWSaqzfNn4FRC7UIp6UW1lwwRufsQpygynyifjdZD-oPJ1-glOI-JzasIRRNJYmm7UC4VxBvhUzRCT71xBl5y-EdXr_6mdm2BRHvdPSvtLi1nTP4m6aIk2_eemSOOsDTJuPxLKv5hiodWIeIYD0qqLvLFOVqQD9jZ_MfUdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=STLPZS55Xvj9mQalTofZTuV5OBrE2gEMbibN8ps9-qva84y4YObqngMk0MapsnGpDuaxwquB6fut6HwCdIde7RSKB3CsiL1FZ2dqH1S_oHbExoajqsQ2wc2O1CtR7KwE3VeA4Z5t5cvk16UAOiayC4WQuamaS72aKbUo3jvqHJG4roBMUW_MZG5C92Kv406hfGSJJoJsAcKXuBIspkUZ4PCLKqALUL4t3xySNxLIb58avN53YULPAKAzzk2L-OWXirGaLA7SEgwhTAAT8_pIJju5qpCK_UTsgwW4OoIu6reTnpPTs2TnN-eM7EJamMWfDovaN8qLc8kVfKL9Bih4d05aafIpGzAO4-1QdMoThtQ5SSqECUeluOdRZzFspZPmKkqk42S0XqsdCDYypx7ljxLSzLfIciO6FleQblkKnC_kFe-2GIYPEd7p4fORgarh8iz5zEwG0vjSF1r02uAKuQrfumzpkp_o3NBa7Ur5XWhPyzuQp-hJQSe_UwBSWeDn5OK4jWSaqzfNn4FRC7UIp6UW1lwwRufsQpygynyifjdZD-oPJ1-glOI-JzasIRRNJYmm7UC4VxBvhUzRCT71xBl5y-EdXr_6mdm2BRHvdPSvtLi1nTP4m6aIk2_eemSOOsDTJuPxLKv5hiodWIeIYD0qqLvLFOVqQD9jZ_MfUdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5mRzhGe7vJg10O_AsdpKqNv_xiv5DepE6lAM929ViFxnwmGJ66L7pp8PHvc2gqqycOdY7_UD8MaWIxyOB2dfPx6qnVH1GsrdU8k5WZef-isvOyyKwUC2DM9oLRO9nAUJmXF0fW4JZmXVilGkx3q5do446w4DvTMbfbZwXvvabuHy3zXr5iRJYrU98Md5uY2tDcge1hO7dSVACgNv1QIk2F43Dloxz40Y3huuCO7ZFv_7iPa4sndKs_siE5cB7ppB7_jrGK0jIXN0NuZ3Q46Gr3Y18bq9GU0m0DbYZiaLYZ-oquiMrBY1RZhnHz3Tq43BGgxnYUVw6V83oZqqUZ9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=NTwLH-4gxvIg3Dd4fO5RzoVgdTXQP6XHSKJpZyCYDKYEiMB5ZC9QhQ33ESvw6QOs_JxmnrvUEA6RS6gS-tLijhiACguBPFAdpuegcvQ8E5bLx7BmUzpQKWFUmbMAv0jxUpK04KzhRtJiI19dXwEy1xgO_-3RlnyC8X-WivOCSFFV77h_YDqM5ytIVaAfoiBANQZbrhV29MZa9OimCt5W-FPlGGeYbfCOS3vRyYEBV_Yk6eCfX54cqTBHfcAcpM4fZVVCJiapwpn9cd_H0yM-F4duXjndjT4yp-8LrlIkxrsTxRPpSOvG9wLnalLlRKm9n4_G8gZ3KbJuoQkBsVLBfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=NTwLH-4gxvIg3Dd4fO5RzoVgdTXQP6XHSKJpZyCYDKYEiMB5ZC9QhQ33ESvw6QOs_JxmnrvUEA6RS6gS-tLijhiACguBPFAdpuegcvQ8E5bLx7BmUzpQKWFUmbMAv0jxUpK04KzhRtJiI19dXwEy1xgO_-3RlnyC8X-WivOCSFFV77h_YDqM5ytIVaAfoiBANQZbrhV29MZa9OimCt5W-FPlGGeYbfCOS3vRyYEBV_Yk6eCfX54cqTBHfcAcpM4fZVVCJiapwpn9cd_H0yM-F4duXjndjT4yp-8LrlIkxrsTxRPpSOvG9wLnalLlRKm9n4_G8gZ3KbJuoQkBsVLBfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orXNfSeUeriN5aRoap42yVR4QKSdHVHY0nAaTTEAZIVSx4_BpupKsMk-uc-pGElibUrusfbmlFLSN1g4ala1D70ijwJq_aMerUlK1UpNq9V7eVwmMP3yH4kGjGS48OFGsZnbZH9G0igVpdJZovoaDv-ulMh63yWHGYKu5Q46rP4lgkKhT21PBNJra8tOJxYebgpUTYfvDuGlMOqmPaC8NfTmgzuqTSI5rqLZZ7KZlbeuISEYC9Z1soTXI2-g3oiCIAflm7AtshF7U_CES2Pav7X4DRus1Y2XPrWTW9zPYiPBkyNmr-k6sgg_gpegI8tEQZCGfqOQcI8YZ5CEuCNKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzDYJoBKBGc2XxizGq1Dwyb3nE6RpN1Q-3Cbik3W2wYlbmJO3L0a5w46cytUY6JFoX4oxJZ7RmOJo0oyjhhNilkMQsSgCzsMN7xdwTX5WOB2LT42rxWC0rOmnnN6wx9zKjeLgDTIiAE5u-9IGoTeXUlcnUgaJO53PeyIkgUUkGzAYHAxo_bXy-TNbjKdoz5qeaPI4Wl7Fpj_xVVIuQy8s79fJAnrIvhi5tBTcuYRI6v_agQHTqK2R-YcfSSJAezuuwSicQTiWaVM9Usdxds7VMWK6SjYbyCd48gUA2--_gnyjpUO7A1hCGT2inv43vDcxqUf619D1qGVDtcriXoimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNqZwROUKnImhpM45mFQftOmxac9vBX3QYfbCb96XdDBBkeItsgjkeaq2ekCS4-0OUS2W6tMe1OTcWLVEeKSoFgOkeGWrWUFeKLr4kjrAwvOaQM4JXXnRduWzRsTe2DzQN-9Vi6hWDc-7OYtwMxjyJrrhEVWJ6WxrUOV5Rw8RA1DNY87EGxv2ZlR69sYM28-nIk3UlcCesc-2EzkRGZXP-Qrtnm2qJbOUewChFH_IOoSAufyuCAmMQhDOGDlaQLGmuK44bPeKLiRc7vufHm4zyp6y0Wp4H4kzdC3Y4UtUh93tBGshRHBxpnlPw1nxMHjf0sEj0gYFeAEWyAdUgR3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEKYKqxSlRivaSQKvi0wlhFb5MFuQDzTGMmIZPYTsjdYoBuVZGBrmOWISq8C_uP4WwehkRHuvFsikIFOys45SgfqmwGHwiO3049h_m6qASiVaE0RemB1LF6MPTyU4KNLUqcnmw1TNKnJdS-IwwO_LkmI71kODaNzuuTDY4WkSeeV--JlQXuTcr15sOEV6-wrjzUhSb9Sb3yXU3tNKuoibguAMQO3pqGaZ6ThW9sCIbVYT_UCovhxI6b3yuQgu3kc0NfFh0PTZri_LlBHi90F2fW9NILwqCUn7-qm-oeUffwbxJZuPKcJ9TkA0PU3Ji0vMaqMVgq6ipIQgDaZehedSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teSbCP7_HKAK8k9EoI0hivl9hxh0y2MDacLdIwreWNMlVJIK-I8cSJ9HFaJZccW3DPZPgl1JSI13ma4azvXaF7hsHHOLzqlV7Fv6fZ6-w77b4yD3AzCA53WJib4aV8zztSDrLI0H4_DqhKLdoFhjZrYuEoKoQfiMgCWyqdr5fTFqY7o2fG4ZSKmCiHhiNuw85A64EXTMk6tkTxigEaQz1j64q42rjyT47V9YWCKQou0OSfA60hb_JIXY0vSBViKUj9TSajiFhGXa2blPZI1hcZ40Nb4tegVWahh1KcGUG7D2RBvT-XXYoISGe1uOXybqL-VOZYu1RtkhAjnDVpdyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpdblah89Sa9WLM29mi2KftnNTb6Psn5fzwDUBekT_NeXmRWWrUYzlIQkLqeUHuGpNcc6AiFQ3grkXZ4PH-Wq4oimTRyekUkux9-srDHV4TrKMg83cdRYyefVxfSv6V19voJys_J1HBChV28Xgd49jJSzyweCpkpovEOwokSVa9_IS6EUq_UZgbAocVhm53u3IAGifWIkmFeIW2BP54Td_T_MMhkl25YE5lqzyzLDXj2ElSiZbxQAfxFapKD6ic07ljnG56brouRXb6qAZ4Fq4F_gVL9HbAz8Nrwh4qiM68HeWyBbMnhRn5n2wEOjkSe1m1vbJ2CpjzxhyHC02NJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_HjRpYQYp6xLtk6Tnlb42XxKeqON6-CMcS4B1zA8a6jUN8ErcLYW-6UkvpAG0R74nx4ethlQbNi2PkFKIN69GGWFHk-gBs-YVzNv61vE1g7V0qvi58hVoyOxOav8CRbKwsTjhcgt5HDeGcQryyGypBk156Tx81u7lpKWORZ1L6ixtHnHJbERvGoP8stvikZc8fAVj2S78b5XcCO7iXXcJVO3sydjrS4EUa-_kC61VXeo4jdH6H7Pkw6HltPh35dmVG2pT9wH0K8ztPxqfjTN7tIMH7-DaIWqcBlfOjZa2LmilwP1D6hZLBnksoCGXI1i2No1IrqpxEO1TitAMP7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=VnzXkkKGrbkCNErZ8r0W-1GSVwfDYaPy8a50ZxP5t9YWpeb6EMEM-c9P0ceiryYwq1u_DcPsURagVDipo4miOY92XmYOGUJrTV9TLuH1pkM6bJTwJ9AQOBR7XWUkSFd_ARFRT1AJv8JoTVRLy3gH8D-JOJ2bHFjdGTlddCVgLA22ignBIRITHlEzIZ222fQ_tcOIGgcToFzy6LNigYmwmHsl5DHfqc4X9bpFmsYbcdU5RoiuzJLFeAgGF4Q5JnWP3fjUoNqgM7RWb0v4k0rxx6Dz6EZN-ThM79qbGz2M-XU_fcOq5I6fbFE45V3t6rvs_HD-l9wStBoDc2A5syNroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=VnzXkkKGrbkCNErZ8r0W-1GSVwfDYaPy8a50ZxP5t9YWpeb6EMEM-c9P0ceiryYwq1u_DcPsURagVDipo4miOY92XmYOGUJrTV9TLuH1pkM6bJTwJ9AQOBR7XWUkSFd_ARFRT1AJv8JoTVRLy3gH8D-JOJ2bHFjdGTlddCVgLA22ignBIRITHlEzIZ222fQ_tcOIGgcToFzy6LNigYmwmHsl5DHfqc4X9bpFmsYbcdU5RoiuzJLFeAgGF4Q5JnWP3fjUoNqgM7RWb0v4k0rxx6Dz6EZN-ThM79qbGz2M-XU_fcOq5I6fbFE45V3t6rvs_HD-l9wStBoDc2A5syNroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBynWlicIDVCfyAqMVoDYV5oyqDvIuDlKbJ0qcBXmH1Aa4Y_QJPe8m3_-DH57ZUk0zpAt818xZrr5hiN3qJCtSxjpuDb6IhAz44H3U-njzkgW8pn86ELcqeZb369bcGH_u4i0ArMeIWh6j5ZtBUWYuEsT4SqIgqno_QbVuWTAxtlR3I_nrmmHRz8UNA4COXHJeBcSdzCN3XMnhOyk3Jme9IzTiuBYu4EKlffhmTML61mmbQOikZ9uPyZQQ6mNcGCmo7T0Q_ckNmgp_Ex8_onhY0V6_nF5JzeLchL6wTbrtG6Ooi3WkJXUBiQZAKHrnrgc5TIjR0HuS8Qtt7SAWAoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Feexc_0of4K6zdX6RbDcbcI-NXhl_OVyVOYp0IuEWfi1zNMIxtKvG2vHu99Bas1CZfxEjilNleDhb0d9YpWIGGRCZhm1z6dWwVXEtgyIdje2WhzeLP9DLmoGYTgVOYSVbfyYwkz7LWmtNGXGgbcy3iN3QYa3dklcRf-c0o2Xd6QusQlae9cyu3NPXK_uEF5orNynQfmOHjThFFteNiz27WcqvjUdSj6nEsTszvMWW1tRka-lQ9BPFUSmkJrwkLiRdtzymv82FddV0SKQA2y3n3kSiNWvh6JGb6bCEk9UI5eZvlkWl4x2X90rJgL6Z_i9IRcbx6cUnqxWUAJmBBE3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=ODzvNxVM2IPWM7mgSXWtMXOF3PQuLy8k_nb638EM0Bc__hZgPZBSvlBqWcgg6iOREeMenmC7Hjn36SWzx3Ouiz-9689hhhrOSktp1ITYIPAS6umLUKW5xbEo3SIUYIZRbB-bpsYExPoVTc4kWfmIdODjwSmoet3O-W-mNb7lNeQ4r_yzzQRA_mllGQe-k5jdgktmdDNHWWxDHmarQcbruoyA9T2T0QVq0FftxlqLRTCL__y_Mk_XWDoy6yNfiLD_gB69xLGzG2RxznathNoWBFzquSmVcejNC5x5PlOHY4YUOQlgCt3NaPydd5slG2AZKDDx4aBlF9itUP26qKyu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=ODzvNxVM2IPWM7mgSXWtMXOF3PQuLy8k_nb638EM0Bc__hZgPZBSvlBqWcgg6iOREeMenmC7Hjn36SWzx3Ouiz-9689hhhrOSktp1ITYIPAS6umLUKW5xbEo3SIUYIZRbB-bpsYExPoVTc4kWfmIdODjwSmoet3O-W-mNb7lNeQ4r_yzzQRA_mllGQe-k5jdgktmdDNHWWxDHmarQcbruoyA9T2T0QVq0FftxlqLRTCL__y_Mk_XWDoy6yNfiLD_gB69xLGzG2RxznathNoWBFzquSmVcejNC5x5PlOHY4YUOQlgCt3NaPydd5slG2AZKDDx4aBlF9itUP26qKyu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=oSS0h5dK4elPm-j8JW0SC9BLyroOKWyhWVRziZ5O7WJerTUi3TkFDUrR0waAkMCxz_thfarGpKtYtZSkNxnODmu3W-X1NT8ZrFX_KXnwfBsSe6KtqoVqunUpoexhk89cFCFs8oE7-8BVS87sdHGy6yj5VWg5NlwMpStzECMo_WT7zALcDZ0Uk-g22BvO7vsWZP1NYmA6NNkteZ5cGRFL801R5Rurrf05SSqVmK9WrLU4Z5zbS8Eg73twi1d8qm_ldw7ifeJbCAiRblR4kpkrLO9vNIEvvpHlfExw-6lsWkj4t82zvGPos_uka9uvpOc3g4x1azNyqZefsgSq74tRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=oSS0h5dK4elPm-j8JW0SC9BLyroOKWyhWVRziZ5O7WJerTUi3TkFDUrR0waAkMCxz_thfarGpKtYtZSkNxnODmu3W-X1NT8ZrFX_KXnwfBsSe6KtqoVqunUpoexhk89cFCFs8oE7-8BVS87sdHGy6yj5VWg5NlwMpStzECMo_WT7zALcDZ0Uk-g22BvO7vsWZP1NYmA6NNkteZ5cGRFL801R5Rurrf05SSqVmK9WrLU4Z5zbS8Eg73twi1d8qm_ldw7ifeJbCAiRblR4kpkrLO9vNIEvvpHlfExw-6lsWkj4t82zvGPos_uka9uvpOc3g4x1azNyqZefsgSq74tRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhkq_YVxt8L7_6u9uSa82OpGUzSP8sLb9UebcaOX4BbO5OwBqmD9YHz2n6mZfZIQOfm87yA_O3ys-Vb5HDl2zK1GVQuimlVEhPbtPNMdWqkWCGXLAVyA4gBvmkewC0-ObXs6zBdgdjhEsqX7-x9z48zr4nYXbaM7EuwhOUy8EYMvtwrI_HZDJXuU_0m1kNkdDCGE041w9v-49bkbmxWuAmJLSz7bC5xVUPIUNAOVdfYDNATNGVi7bhxktbQFGyu5V5xZ3I-_JuwS4hV_aOsRqwVozbHUMkeAD2dMHGIRU2V97fl6WeGieZIfBJrHLZ8P1IEKu1bmt_z7qbzps9niwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=iQVecuZiehhsSzq6-YaCv_q2-gS59BwQUTV1y_GMPF3wCzvyQtHxzG2ta182UAmmYNxTPpOeWBTDgmivBuSDSAb5rLxn_7n9h7rvthg5EwWeRbpVqDH4KCbVbp2okbxaOi4kT54KJAOtmyQJFgl2R4MoqKRTuXJi6Z_cIfE3o-cGRh_FuXLWAs9LY-wuBvrpI7IjbvfWuSHBuRxvUatSZhrs-xPN1dWhkRuYs2qwtgLG1Wz_LyatlHI2EfdmD2vvxRTSSP_1lbkHO5K8RWNWPheNbEemFAITrP_wOCB8MHNlMca2LsBVGZZAPqahlPRidvRqwKUxJTca0V69AtdbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=iQVecuZiehhsSzq6-YaCv_q2-gS59BwQUTV1y_GMPF3wCzvyQtHxzG2ta182UAmmYNxTPpOeWBTDgmivBuSDSAb5rLxn_7n9h7rvthg5EwWeRbpVqDH4KCbVbp2okbxaOi4kT54KJAOtmyQJFgl2R4MoqKRTuXJi6Z_cIfE3o-cGRh_FuXLWAs9LY-wuBvrpI7IjbvfWuSHBuRxvUatSZhrs-xPN1dWhkRuYs2qwtgLG1Wz_LyatlHI2EfdmD2vvxRTSSP_1lbkHO5K8RWNWPheNbEemFAITrP_wOCB8MHNlMca2LsBVGZZAPqahlPRidvRqwKUxJTca0V69AtdbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=L0EZokD-43KJXUOaw8fbnJLjQPvD-QRl0F638IUvokufe2yZgD4n3hW9MIG_AlpjZ3LUSuEieq3hplx5tcJH_mtr5-WivlkdRnlfnXQwSTJNaPDRyCOpjNqY5ZtRDXDOEjRrk33_laNqRNH5HoTBs9Ku-YcIRLuIRYiodYRO7Ebzvmtwy3MGEpNL6pO2PULj0kO0IhoDWkBunqI6UlQOVlKTTd6Bxffve8wxEVCrbBsyVM13kcV1zP_kwuNxqUIHnuas7_aRBfyAabkiKLD-u5hx15f5RB7FP4QeP4NZVleQlJMMhPISdHN1Uv_wGSQijn3tA2xpkrnenqTwWBc9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=L0EZokD-43KJXUOaw8fbnJLjQPvD-QRl0F638IUvokufe2yZgD4n3hW9MIG_AlpjZ3LUSuEieq3hplx5tcJH_mtr5-WivlkdRnlfnXQwSTJNaPDRyCOpjNqY5ZtRDXDOEjRrk33_laNqRNH5HoTBs9Ku-YcIRLuIRYiodYRO7Ebzvmtwy3MGEpNL6pO2PULj0kO0IhoDWkBunqI6UlQOVlKTTd6Bxffve8wxEVCrbBsyVM13kcV1zP_kwuNxqUIHnuas7_aRBfyAabkiKLD-u5hx15f5RB7FP4QeP4NZVleQlJMMhPISdHN1Uv_wGSQijn3tA2xpkrnenqTwWBc9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-wAC3hMoNim64WygVRmVSE2HreGTHkmp34o5xZSuKiWiozG7ZUBwHAYkHiZh5SsG3pFObbqaPrm6ggz4iRByob757suukhVDWYX3FHPW_GO7-GQ2IroClqUz43ygRuDHPxyKCvUEp-TjVJZ6Btwv8LiSLjPccKmYH2Vrx-pFfigE-s6mpkQEG-7IZwRHIPnZ3zghq07HMDfkbdxd4-8z0ac3hHsDB54mS7EOFAq3lfqjLCKyKmSsISg1unpazXIf_CxjMBR-s-nuf7mlp09gdFm7RuKed-wzHEPpqE3Wvq2r_gR6OX2KsmUzz0Lmcuwl_qTjaMZQI-E7hDnjKSQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7qFiFhxCxw-krUG-HzWog2bA9aTj2xy7WKcVWhIMgEqB16QCq6Uh1qJeJDy1U2yZcL_oX__HMxitIx_z7ggp0ftqGysUeAHCiSi-v2iCvFuuAwsf5Lp1vJCemxjrtuBxVXZX7UDSN5NzGFnoCe04GZpWUNPoNIK1cr0zYYlGUVG7_iKYIb_o3Rg8LZ7-ySFmDrA5HSq-HYEXzIegsRw39MkOqpO6_tlnwlO-ws5LBGJ24VHtvAIKfcXy0OqM5W0WD8Tk7o0PjLSH48vCNFvtgxmLxnwH25e3eY6Mc-7QaX3DSQV37gjVYHJvoc4EVxx_GG4oytymtJGiCswhprFvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR0WdtJ5VgSx5LMKCqb3PX50Oi4eaDVwdCYr5N-EFzGOOm6LwBZ-8HPwDY37yAvZflMpOIO33cN_oh4FM_74O9joCJvs878wHHExIDw_7HzjxWdmU6bUyEJb2lTSBrgDUFNYaL83uLarCx7eHKcNbcqI__oNqXzEDX-UXOfv5BibYU31exIYZPwgsUOBd_ejiitc9utodIRcz2Luwf2vTSAZJ6-5kuW5SpSkkhSPfLLrJTqYyArS7ybmZsIB5r8CZMug7zoUzQ6QOiyrrwEKBldoEOVhg-GFAUiF2O1ZACY92lrVaY4iJjH0CQSOv7sufr8eVKeueb2MdxhvFxjKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVSIK6SWUCDG4oSE53uOQYpRbq1rehco5BPDo76YAUtIzYpNIGVzSwxDy-fKdyDPzFi59aLVike0G-a7K9NB-J51Jw9X9wVMNOF1AyEYosh8WTD1TQT9lDOJig6btA8MHO5wQAeDlb9Cqvge3hvRXAHzhWFyTlq7dy6vsRxDWEb1lPRSbDdv-76VpRnmQ1lHnaSAGOpavXF0OZxvOsb5xAYsfceMWX-6FxKMwPXfMHFnKQm_DOlsKLd0NyTct9ZOO7rHjoo0eZSlB8CsQoTMnbRATI_Bn1ijwI2HmDTkUqUb0Bc_GvKtVEf5Y5GEbi3TRpRPbLLuRq3muOv_C7bfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=BmwVBoZmNlOKI8tcWxapWPOxbHjdN6az_0mjPmmm-3fcI-BLV0YPv9f2vca2CE-T_967XMgmytWlWd3Gsz0YDW-Oho1ZvJqynC0lsy9DHvIYOWW-hU_TJZO4Wv0q_1lA57sTvH3zMSpfgBAqNkcdK4MP6ezaETYn05mR0B3N0lkQzU-QPa2_VnseBRBGx988EOWZPozhlpE1FsUGsVWOFeRmqjtO3uL3OnsvzHD1JL3RdFvRHRxJTRuLhnmNzsF7JnnsNzGw5HQYlxzT_liF22ylTp1gLXdyEcl-r3dBLWW8uuApqX4OrrjB-tM-EQPx4kcPyRrrYLLFjVxu8JVfbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=BmwVBoZmNlOKI8tcWxapWPOxbHjdN6az_0mjPmmm-3fcI-BLV0YPv9f2vca2CE-T_967XMgmytWlWd3Gsz0YDW-Oho1ZvJqynC0lsy9DHvIYOWW-hU_TJZO4Wv0q_1lA57sTvH3zMSpfgBAqNkcdK4MP6ezaETYn05mR0B3N0lkQzU-QPa2_VnseBRBGx988EOWZPozhlpE1FsUGsVWOFeRmqjtO3uL3OnsvzHD1JL3RdFvRHRxJTRuLhnmNzsF7JnnsNzGw5HQYlxzT_liF22ylTp1gLXdyEcl-r3dBLWW8uuApqX4OrrjB-tM-EQPx4kcPyRrrYLLFjVxu8JVfbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkblSTfN4HKsJShkZIRfLTcbyCqjAX1PcYNK0Z5Xbjlc5rNaqEPKwtrmz2KUyekKPwizegx6UlOfKk_N-GkZ4nOJ7olFu_u_KuJvsS5mbVARAQ4CUpdz8PP025MwJHG602KM6n4JmfHZO_LQunuJra2k_SSFYNjYzbq7H_FL6w9nXXtd0q5uj6ZL7Stn8SPuN5uQrKOEO6oPPvOGHhLx6VghMSVQPZ44v_8I-fwKU9gJSAX26_xrfeNbBeBXVIbSpcI6Rn0rjq8U8FLRnnz8F39sLlT8EzrJ9ETed5-QhSHN5F8QdDrFTF6q0DgfmFxqvgYdrR9tA_48TL8yHbimpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXUI9XRepSgITwQjhyED-H-NFIq0015SiAc-BeE_HpEozqooTRMCShd-z5lXLpvTNmJ-IBG9Y4z1fTA63iBis15lnE4NBQXzyPmaPh9Ys84maPypcA_-GXPHAv6n_yRmWUEPPTdXfHZq3Lk5L_sAi5BaWPwn0OoyjjJhOYcaHpXo7fd1j5cvjL6Z9Bl-epTqAJl57Za22EEAD8Ep4FL9nYsnyX7GlXciGrolXOm748dbpM7resDZJpRVlYa1x0HQPtZScpJDyS2B_YFf6VNXrxFnev-5OcG66drdTIOHQjDYEz3mtoKUPV--chYqPdFXV8rwhjrxmDcZM-KdmYJkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI4OExq--UWZji3qAoZlz0k4yvFNOT9_A_TJIowPyKOdIyq5dw2O0Ri9l0s76ae0jpi_0OuenzWrdTSSPkzP4rQqSFb8Gepf2RVb4rDeoa4mDTv3k6O3nobb4iKe0iIzCfKxZ_ET3ujXDNO7sypGlNaR06Tqey99aTbn5nBxN0V2JW_t09rCHDHCJoqn0wxM9n63OsX6Jw1rizXr3ymcf5Yb0rXkzcJtjsjRckRFdtvFrayLigMaQzBQq_mCnA5O2vMq-OqqW12cmbxrTXyZO4__owLG3xx5_Q2pPI779k8ilyyv1OZdZiUSKqUdzUNGvGX1FA05g9CBIAiVm6ki4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=UoqZ86wbCZ0deISf7LEAOum9vEbDzoJG_NV_PzM0rMWvxEBZ6RiM9LII_V0Ww_wREZ_91s-5YIyNs-KaPsZoNkNsKZN81RmrpE6_B2rppTEznT-ObCAyMT9oi8CEmFCGPbaPBCr8iNo0MyiFrKEyukMlc-x4U4zLX74U-O5TnaEwYta8w0LiEPS2SGd5Y5F_f3OiVLg3hf7HNL5Tuc3OZxnn7BI3Wla5ujXfSvS_qEyTAR44Buu_13DbdVFz76e6tsbTNT9PZcuuV5jKcCn95lOQlb0UTzpE3a3Z4_lN8bKfEuzzd_2YyVt-ey2hng8tHUenzIqqt2tG1SDqoXh_HBbKBeQlZNq4ZC8t8jhB8uFhJFHQupylibbAy2gmuekPWDA3qLAtLQuFTFuNZY2tMsm-zYol8k-wyy1E0SM1j5jk2JDTkXCmjZoA6hbZHeVWkL1-kfuoVFHr-klOXqi8CELC3FJojSN-tWyl9XYfDf82ULWX41lPSGR8Sy7VWUs-ZsLaWOcYjsGaRT2bGDtMwHSCZ5KNRUrozv4iYMJYTeoJhsHOnmwQMua3mCbLDeMAExLWMqDDmJp44jk__MuS2OEg8N-TW5UPHjIiMZuIoD46cKx6Oylp1eMj6s7djfKu1YSfRBuiobaR5xpCkwYZYXmDBAAw8pQxyUqr0PZcqDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=UoqZ86wbCZ0deISf7LEAOum9vEbDzoJG_NV_PzM0rMWvxEBZ6RiM9LII_V0Ww_wREZ_91s-5YIyNs-KaPsZoNkNsKZN81RmrpE6_B2rppTEznT-ObCAyMT9oi8CEmFCGPbaPBCr8iNo0MyiFrKEyukMlc-x4U4zLX74U-O5TnaEwYta8w0LiEPS2SGd5Y5F_f3OiVLg3hf7HNL5Tuc3OZxnn7BI3Wla5ujXfSvS_qEyTAR44Buu_13DbdVFz76e6tsbTNT9PZcuuV5jKcCn95lOQlb0UTzpE3a3Z4_lN8bKfEuzzd_2YyVt-ey2hng8tHUenzIqqt2tG1SDqoXh_HBbKBeQlZNq4ZC8t8jhB8uFhJFHQupylibbAy2gmuekPWDA3qLAtLQuFTFuNZY2tMsm-zYol8k-wyy1E0SM1j5jk2JDTkXCmjZoA6hbZHeVWkL1-kfuoVFHr-klOXqi8CELC3FJojSN-tWyl9XYfDf82ULWX41lPSGR8Sy7VWUs-ZsLaWOcYjsGaRT2bGDtMwHSCZ5KNRUrozv4iYMJYTeoJhsHOnmwQMua3mCbLDeMAExLWMqDDmJp44jk__MuS2OEg8N-TW5UPHjIiMZuIoD46cKx6Oylp1eMj6s7djfKu1YSfRBuiobaR5xpCkwYZYXmDBAAw8pQxyUqr0PZcqDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=fYqSpjWOYIgcWMT-rJXIOf98saksbT8pOJmcy2A0xcK7oG0fpfHbGqxgpJDZqFKce0aI8j4IlqtSsv_fDT6CGCfKsOxSnUk9VdjVc3WnPL8xHPGVzCOjYN9LwoUQzi6KNvMxKj6lrs-Sl_wiAhbmU7OduSDFn67lD_f5kB2qZc4lxuNB6ZN6d_MW_1RhaWYzXvyqw3eo2I0UPVGhIkSp2ETZO9XftdZrLNBIZoMNjszIsu9O2sAmHzaUsZtQtCD2n33JA4TVTNBToS0_zs1Df7CikuSnZHm68JbHy9pd5Wh5K6h8qcZFSsqzsaM2eJqF7p7D7xHKJEveER1QPmbgBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=fYqSpjWOYIgcWMT-rJXIOf98saksbT8pOJmcy2A0xcK7oG0fpfHbGqxgpJDZqFKce0aI8j4IlqtSsv_fDT6CGCfKsOxSnUk9VdjVc3WnPL8xHPGVzCOjYN9LwoUQzi6KNvMxKj6lrs-Sl_wiAhbmU7OduSDFn67lD_f5kB2qZc4lxuNB6ZN6d_MW_1RhaWYzXvyqw3eo2I0UPVGhIkSp2ETZO9XftdZrLNBIZoMNjszIsu9O2sAmHzaUsZtQtCD2n33JA4TVTNBToS0_zs1Df7CikuSnZHm68JbHy9pd5Wh5K6h8qcZFSsqzsaM2eJqF7p7D7xHKJEveER1QPmbgBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=ElrcfJirRxIrxaClQltadK3mbLwT-DLsT-1cVLlxXHaesM6o6pG7YdrVnCbl1WjAxAV8yE0YUUPSMbfpRmhljytJ0MyYXGGsuO4U8H7XliboMV-mGUEGxPr_POGvmrW5_w0MRffxJX4YSy02Ri-VXhilGwiBJ12NV99d4dSzIYlb1MUVOWemO_tieAEUF7Abn3E0qhgUt9Oc8S3zldchIzxr5SMj4bNJiwNXAn3ata3flkyI5p5bHGQ-7FO27fF0OCODVLgAdj5m-sM1VtXn4AYGuOuCwO0XKN5PK8tqVOpjSkjTyl9bXypUyYRvn1tYIkvtOQQta6IPH1AlEKkPTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=ElrcfJirRxIrxaClQltadK3mbLwT-DLsT-1cVLlxXHaesM6o6pG7YdrVnCbl1WjAxAV8yE0YUUPSMbfpRmhljytJ0MyYXGGsuO4U8H7XliboMV-mGUEGxPr_POGvmrW5_w0MRffxJX4YSy02Ri-VXhilGwiBJ12NV99d4dSzIYlb1MUVOWemO_tieAEUF7Abn3E0qhgUt9Oc8S3zldchIzxr5SMj4bNJiwNXAn3ata3flkyI5p5bHGQ-7FO27fF0OCODVLgAdj5m-sM1VtXn4AYGuOuCwO0XKN5PK8tqVOpjSkjTyl9bXypUyYRvn1tYIkvtOQQta6IPH1AlEKkPTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
