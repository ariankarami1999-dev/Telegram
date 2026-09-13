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
<img src="https://cdn4.telesco.pe/file/hJBRH9lDJyOGbC8Is5ZAGJ_QGXwnkWVkOleCh9R574s3MBNs1gNTq85WNP5SqWFMuhVzkzuCP283ERNJtgwgU_zixbaq66ifZSaXY8mD9vFMiDERmB2Rzfbsxk9gc5mUIUU9mKW8NLLENO0dZACWcDiQpfA5E28gakk86J96Y2Hh1abZM2rtVH1Nja35BtJ2-GiADNTHluZiVqFxZNh1lS8_RFcp0lvFWdlWY0vf1rvIrv_VT2KgljvbIyrxQEoXKfr1VWJ4c45KAR42PyQtuyBL_hxhO4nmk7ds7pnwn5HfSxB3gQGiuhfEo1-PXZXsE83ahS6V5DsD4mpJUqOwHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-461752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 354 · <a href="https://t.me/farsna/461752" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbV7wU7E5cNscHfckWfq7jUsnkveQg2FJPatWsTQCah1gTCe5oRN7EogU1sNodwGtieFqAZBkAVtj1PwPWCZWorcMcVYz6VYdtvHGRGj5C-SE6OrJETKxzvOF1tAmivCyGixwO-fDqHlUFkj-C3f9aMXiQf3ZJ1pqfD5gHH1nn4fDXfjVuTAwFO3LLwDvZbu7KxG_dzJTKjFSfZB0ZUxUOLl_QhvXp2QftlQ_Nyn2vhP9YO-iTtn_rcHIZ_YwqqRG0CTIgu3nHPqEedFM0vTJ0ku6xD0xsVj0xAbMzjggnbJS1eeczW9A9_88FwV624cXbR2TDlFH8W01ilDCtqnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: حاضرم در آمریکا با پوتین دیدار کنم
🔹
رئیس‌جمهور اوکراین در مصاحبه با دویچه‌وله از دیدار با همتای روس در حاشیه نشست سران گروه ۲۰ که قرار است دسامبر در میامی آمریکا برگزار شود، استقبال کرد و گفت: در صورت حضور پوتین، من هم حتماً شرکت خواهم کرد. باید باهم…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/461751" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما گردان‌های سازمان یافتهٔ ۷۲ نفره از باشگاه‌های ورزشی و مجموعه‌های هنری و مذهبی و تمام اصناف داریم که برای شرکت در رزمایش ۳۱۳ هزارنفری ثبت‌نام کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/461750" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تا به امروز بیش‌از ۴۰۰ هزار نفر برای رزمایش ۳۱۳ هزارنفری جان‌فدای ایران ثبت‌نام کرده‌اند.
🔹
این رزمایش جمعه از ساعت ۸ صبح از میدان امام‌حسین(ع) و تقاطع نواب تا میدان انقلاب آغاز می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/461749" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/461748" target="_blank">📅 10:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب به ۲۰۰ شب در میادین حضور پیدا کرده‌اند و بزرگترین مولفهٔ ملی را رقم زده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/461747" target="_blank">📅 10:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ صیاد مفقودشدهٔ هرمزگانی به خانه بازگشتند
🔹
مسئول دفتر وزارت خارجه در بندرعباس: ۱۰ صیاد هرمزگانی که در امارات مفقود شده بودند، روز گذشته وارد تهران و امروز از طریق پرواز به هرمزگان بازگشتند.
🔹
این افراد قرار بود ۱۶ شهریور به کشور برگردند؛ اما به‌دلیل اینکه…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/461746" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳:۳۰ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/461745" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شهردار تهران: قیمت گوشت و برنج ۶ ماه ثابت می‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/461744" target="_blank">📅 10:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNORXxGGZC-nQuMrcwEG4wMHsAucHwMFUDsf7mJwNJGxUiSLJynZdawEkLzHt1GlFxtoxC4h47HfN10MUKDNa5bROWBp-0iXZjlfi3tfBy_r56txsbLNldMAc9FLr2GqLlMTJS9C4DzoBKSkpQoQwdelFQmWLXW0EdTRfcBDKF__zqNmqfWLx10i00HHX8rbOgjq5DAkVWHYsphN5gWHgF0EiEIB76D6-Sz9e_u_ZdSrfX1eeBa9RlE3V2DtuK4hTNyZIi3sXi51WDcl9JxYwj5HzlaahyoGrurZfyvdjy6Jyaifw4RVfcegMS79dpp1ZNg0yJl_FJJl9ORahh6iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
بازدید رئیس‌جمهوری از جدیدترین دستاوردها و راهکارهای ارتباطی ایرانسل
🔸
ایرانسل، در جریان آیین «یک ایران متصل»، جدیدترین دستاوردها و راهکارهای ارتباطی و دیجیتال خود را به دکتر مسعود پزشکیان معرفی کرد و همزمان ۹۴۶ پروژه ارتباطی ایرانسل در ۲۱ استان کشور با حضور رئیس‌جمهوری، به بهره‌برداری رسید.
🔸
این مراسم، با حضور رئیس‌جمهوری، وزیر ارتباطات و معاونان وی، مدیرعامل ایرانسل، جمعی از مدیران حوزه ارتباطات و خبرنگاران، در قالب «خانواده ارتباطات»، ۱۶ شهریور، در سالن اجلاس سران برگزار شد.
🔸
در جریان این مراسم، رئیس‌جمهوری از محصولات و راهکارهای فناورانه ایرانسل، از جمله سرویس eSIM، سامانه فوریت‌های اداری «فواد۱۲۸» و سامانه مدیریت هوشمند ناوگان حمل‌ونقل و قفل هوشمند، بازدید کرد و در جریان جزئیات این راهکارها قرار گرفت.
🔸
در این رویداد که با هدف معرفی و بهره‌برداری از مجموعه پروژه‌های توسعه‌ای حوزه ارتباطات برگزار شد، در بخش پروژه‌های ایرانسل، ۹۴۶ پروژه ارتباطی در ۲۱ استان کشور، به نمایندگی از مجموعه اقدامات ارتباطی ایرانسل، به طور رسمی توسط رئیس جمهوری به بهره‌برداری رسید.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/461743" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdYGW3p9n2_rhSG5nfx2kiu3Ki7KfGffIEXflTQktVIOzzHEO15iCWsBjhu5mdEHcLnAstZVrxAV_ToJ_TK87SKusfCtGVnTz7o-pm7FvRhvVz4S0hi_05YAxcIWh6IwZkPbz6haLTOADQ_ry592iJeg8P75pRO1UQRMc5LF-FyJKMT2IRVl7jgVac5fvPWxI-y4Aeq1JrhEsd3CfE4jh4hsUxPGH_3TzQqT0fOGVpi7e2UrQcw99pLheXtQfDU9riT3oC3e_PHz9y0XjwUo8bwDF9re6RChxurh0tgHygcGCqWvfFb0Y9korGf6qKY4uhLTD9da2MNm9QjBuxeowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همزمان با ثبت رکورد ۹۹٫۷ درصدی تراکنش‌های موفق
سهم بانک کشاورزی از تراکنش‌های شتاب در سال ۱۴۰۴ به ۸ درصد رسید
🔻
بررسی عملکرد بانک کشاورزی در شبکه پرداخت الکترونیکی کشور طی سال ۱۴۰۴ نشان می‌دهد ۹۹٫۶۸ درصد از تراکنش‌های ثبت‌شده بانک با موفقیت انجام شده است. این امر در شرایطی محقق شده که در همین بازه زمانی، بانک کشاورزی ۷٫۷۸ درصد از مجموع تعداد تراکنش‌های شتاب را به خود اختصاص داده است.
🔻
جایگاه بانک کشاورزی در شاخص تعداد تراکنش‌های شتاب که بیانگر مقیاس فعالیت در شبکه تراکنش‌های بین‌بانکی است، نسبت به سال ۱۴۰۳ یک پله ارتقا یافته تا نشاندهنده روند بهبود موقعیت این بانک در شبکه پرداخت باشد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/461742" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/461741" target="_blank">📅 10:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNpIspWXy49V79tOGsWJgkj5zZZfCcxRiBkJyB5_9ZoIloVcGG0FiE3BT130z6LFAGAfNuOAdLwIUTmXaaligJSRqXY8Xg5ZNCPTHqzPb59UU5JNXDQE_d3VYFuJelg5T1m3gR0hCtEhim5-QCgsLgnjGL31CDyHvndr1q-Zp1v0arP6VH1x9tXcM2F_4BJn_RFJJbX4joVHlRfSe5aGZouPCkEZHigpuPMT6IvJgwnRivynEuEIjQt6Bf1gxSD81RpcFEc3tJroYsjv8gC_SYSyMXIbq9Q5vhx-xlyK0eqwWPcrFxeZeTNkQizkY4c6rs1E9X9deB9cZ8Geriz4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم
🔹
رئیس‌جمهور در گفت‌گو با شبکۀ خبری ایندیا تودی هند: روابط ایران با همسایگان از جمله امارات، عربستان، پاکستان، قطر، روسیه و چین دوستانه است؛ مشکل اصلی پایگاه‌های آمریکا در منطقه است.
🔹
ایران آغازگر هیچ جنگی نبوده و تنها در برابر تجاوز آمریکا و اسرائیل از خود دفاع کرده است.
🔹
ایران به ان‌پی‌تی پایبند است و دنبال ساخت سلاح هسته‌ای نیست و برای گفت‌وگو در چارچوب قوانین بین‌المللی آماده است.
🔹
ایران به‌دنبال جنگ نیست، اما با تحریم، بستن راه‌های دارو و غذا و فشار بر مردم تسلیم نخواهد شد و تنها راه، توقف تجاوز و یک‌جانبه‌گرایی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/461740" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی اصابت کرده، مشخص نشده است؛ بررسی‌ها دربارهٔ جزئیات این حادثه ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/461739" target="_blank">📅 10:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/461738" target="_blank">📅 10:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
مرزهای چذابه و شلمچه در چه وضعیتی هستند
🔹
ساعتی پیش مرز چذابه برای اتباع عراقی بازگشایی شده، اما هنوز خبری از بازگشایی پایانهٔ عراق به‌سمت ایران اعلام نشده است.
🔹
با اعلام استانداری خوزستان مردم فعلا برای تردد در بخش تجاری و مسافری به مرزهای چذابه و شلمچه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/461737" target="_blank">📅 09:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uELaHKmOoUGPo68gWKdXNpgEflsqI5bIV85AaPyCjGbGCDOkN5Mh1HdpXdGtFxyHPMNtMqt8bJU-7Yi-F_hfvdjZXXM9YySxXDeoYxwIZPZ1TDPn2-w7GJxlYCUy5akLBlmS0VG0tNqJnlNTCWwxTBOk9UtlMV2qV_twsVRwSBhqQJDbmQTpL2baGtJaelm4w_R55bB1jxjcacFUVvxcMzF9HhBgBUSlHQD7XFB7kAOTaHJC29WWFts9T0Vxfmh9jwgexAB4mxS5KvpEeme5dlx-kDAu7t9wo05pcPmcUuGsoTJhCR6URcXwR_ccq1FdGA4mFpycbo-8lWtnubq0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصویب طرح ملی توسعۀ هوش مصنوعی در شورای نگهبان
🔹
سخنگوی شورای نگهبان: طرح ملی توسعۀ هوش مصنوعی که در مراحل قبل اشکالاتی داشت، با بررسی مجدد شورا تأیید شد و قانون ملی توسعۀ هوش مصنوعی تصویب شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/461736" target="_blank">📅 09:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67371947d.mp4?token=bGQfO6nn4Bo97G29tj3FF5_AtQXOB6UjQM32_IfKeMXKvujKKxXTHqjobM2HgWahkBJqHI1cbdRXNS-0NgrG-JDqJkYel0y7eGJq6mGVFGjbvTPcHch1denIh-dWsWDy9WzMgZz_aWMDR-6ges1mQBJ5VZgQPlj0u4QCQxYyc-nk0UkpHvNfzrOWk6aQ2CHNN28yV4vTzwnGpBzbpuRI9bgtWxNkJe-lIaNoo5RBr01ohqToSI-Ox-u7Gngaxo0s3x8kzUQ-vS8vQfocZ9MkuL4wx8wQ0eaFh1jngOTxe64Yx26Ya_5s1WVGOFJ2jX7hvTHflTIrdSU1rcdapONV8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67371947d.mp4?token=bGQfO6nn4Bo97G29tj3FF5_AtQXOB6UjQM32_IfKeMXKvujKKxXTHqjobM2HgWahkBJqHI1cbdRXNS-0NgrG-JDqJkYel0y7eGJq6mGVFGjbvTPcHch1denIh-dWsWDy9WzMgZz_aWMDR-6ges1mQBJ5VZgQPlj0u4QCQxYyc-nk0UkpHvNfzrOWk6aQ2CHNN28yV4vTzwnGpBzbpuRI9bgtWxNkJe-lIaNoo5RBr01ohqToSI-Ox-u7Gngaxo0s3x8kzUQ-vS8vQfocZ9MkuL4wx8wQ0eaFh1jngOTxe64Yx26Ya_5s1WVGOFJ2jX7hvTHflTIrdSU1rcdapONV8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/461735" target="_blank">📅 09:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWIr4mQbqPF8ClHq-EFMrxz71G-gjiJs9Vlk0jk-y2kuQYZfzuZjG02iun09UIbiqj6OXoOEN6cJg4z7yBEUfqmjYZ1oaA_zrXIvH4lz5YmHJKdPWd2C3mYusl7cdbNaA5e0BAsS8tDG-S9qaVpFYdmkYks89zAU6ht7PlGUilO2jB4fJ5L6UvK0iTGN_6IifjGHorZ2QIBo7PtZVBb9I4xwTgNq9NOs40x8UUiO1QP3l-P4rRd1liD7HhdOQyHysOpcPHJeKfqJ2LUqckKg4P7wXMNf6Yl7F-YkbLf2YIA0MiXlIECsriXNFbeo5DQT3aFYBddl9vqgT41sZKMjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fff5ddec2.mp4?token=BzC51TYHhm-nkeL88iJMFdB9hkPuv-p9T9x7gstsvKJ3wZAJPB46qHVFnTEr-29nNrAAGyPeQPwgCGrXzbOL_wQvphTpJs894pn6OeMQnTVn8lGV5z7SCZcsZ8mwG_ibcEOXXtP3R3WJIi9LypO4VSSQbmSKJYNgpQ-bfQRBymXKM4Q2KeCKBPAedne38wryvrbM3wksT6UYp_rMlLplL8Vs7IujrfWO_j58qygUgsrlV0gP3RndlhxLyHeCbA3HxkxCwmmbkUd1l6emTyajdrde49FywEHCYwyxqGEGxZQSk1BMQZQatUTHzlcIJpiE1X7Th16DSXqJGdQhB7WgpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fff5ddec2.mp4?token=BzC51TYHhm-nkeL88iJMFdB9hkPuv-p9T9x7gstsvKJ3wZAJPB46qHVFnTEr-29nNrAAGyPeQPwgCGrXzbOL_wQvphTpJs894pn6OeMQnTVn8lGV5z7SCZcsZ8mwG_ibcEOXXtP3R3WJIi9LypO4VSSQbmSKJYNgpQ-bfQRBymXKM4Q2KeCKBPAedne38wryvrbM3wksT6UYp_rMlLplL8Vs7IujrfWO_j58qygUgsrlV0gP3RndlhxLyHeCbA3HxkxCwmmbkUd1l6emTyajdrde49FywEHCYwyxqGEGxZQSk1BMQZQatUTHzlcIJpiE1X7Th16DSXqJGdQhB7WgpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ امارات مانع خروج صیادان بازداشت‌شدهٔ هرمزگانی شد
🔹
نمایندگی وزارت خارجه در هرمزگان: اجازهٔ خروج و آزادی ۱۰ صیاد هرمزگانی که از اواخر مرداد امسال در امارات بازداشت شده بودند، دقایقی پیش لغو شد.
🔸
قرار بود این صیادان ساعت ۱۳:۳۰ امروز از فرودگاه دبی به میهن…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/461733" target="_blank">📅 09:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461732">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozab2T8nnYABcQqbIEE4fvzHWaGULHiLC_HLjtyjzhEj5ZBKZXxaDTO-YJXycHs8JAT-6C5YPt7zmi6RMH5eREb9qBkkjt-O2hG8Riqq8Lz0WWgCAh8Q2dVvkSiY-_PfKCxvRZD4QQtJ0_nGGx7j4IGJEOkuyBmRX5bW3SJZg8kN0d7gcuW6ESuLjjRzJ1yx7auKxbtppoydMN2w_CNCkn3xZwDQ7aQhjvSS-weXENTvksP-kClbu1q6AsDEBQTYWRfoNFe1JsUCbFeSKPBVT5BYVfp-Pj1kNGfZTMYPY1e9pasYh0AmRCnt46114DxFYQlCSGXREFxmOAZaybZE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/461732" target="_blank">📅 09:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461731">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b558ee41.mp4?token=hxt_r8jYq23CXTYgJA2aiQG8bkI-byLZ2WcXROQ3Bg2TaMUysY7DFaDlY1dZCvOVW9ekTavZoBXd5getq-NWDBMpYjFafJMCwXt5i2mzCx9hYkkUy6wbuFJQeGyk--m9sX5uL6k97lYzXhnc-RncId2MQUsMjOg7qRUkTe7IvMl76ZzW00-nBFdQ9MnhV4Dzoy5EvJOVuSpIBucfn73Tl8iIzbpyE-8femWCaPv9jc58IYE1_tUpKltBsYd_74Hxf9aKnL99ANOY0I7qgjfqmfE532gmitOld7N8fLv0tE92XbbHB8H0HiTzdn4WflVG9NOCj2Dde0DLf3vicNbzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b558ee41.mp4?token=hxt_r8jYq23CXTYgJA2aiQG8bkI-byLZ2WcXROQ3Bg2TaMUysY7DFaDlY1dZCvOVW9ekTavZoBXd5getq-NWDBMpYjFafJMCwXt5i2mzCx9hYkkUy6wbuFJQeGyk--m9sX5uL6k97lYzXhnc-RncId2MQUsMjOg7qRUkTe7IvMl76ZzW00-nBFdQ9MnhV4Dzoy5EvJOVuSpIBucfn73Tl8iIzbpyE-8femWCaPv9jc58IYE1_tUpKltBsYd_74Hxf9aKnL99ANOY0I7qgjfqmfE532gmitOld7N8fLv0tE92XbbHB8H0HiTzdn4WflVG9NOCj2Dde0DLf3vicNbzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبار سوخت روسیه در آتش سوخت
🔹
درپی حملهٔ شبانهٔ پهپادهای اوکراینی، مخازن سوخت پایگاه هوایی تاگانروگ روسیه دچار آتش‌سوزی گسترده شد.
🔹
منابع اوکراینی همچنین از هدف قرار گرفتن تأسیسات مرتبط با تولید و نگهداری پهپاد در تاگانروگ خبر داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/461731" target="_blank">📅 09:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461730">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2WZGDcVtLL7o0IQ9UPsRnv33pLIOE0x91IInSCICbfw2h7_xSryxJGsoxRFtRxJjThNXvSiB11y9YFtgy4ijlaYfgt2E3tTZMhopqLf_jcGBtVFn4nWSZrUsihc6xjDSfrhV3lKZy32NcwgL2VC46ISGe4m8me2b9tzgyGpKHeTPhH3Lx1aB5SOE14W0ohOE0UBnCsBQt3DVj91slLDLMak-xnOEfEhbBNTw78cTG0UEyBjZu7st40khL_tn2SUvkmJ-Z4GiFSfvgdarvHMjYvxKkEmgwX3Wyb5qw7bALAEjqGKvUqxjuJH6k32E8H-ahcEHS7iLsmk2yCbPiGqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلبریتی‌های اجاره‌ای دشمن
🔹
یادداشت مهدیه شادمانی، فعال رسانه‌ای: «تازه به دوران رسیده‌های هنری» تا پاهایشان به خاک بیگانه می‌رسد، به‌جای همدردی با این همه مظلومیت و آگاه‌سازی افکار عمومی نسبت به جنایات رهبران باطل، برای «آزادی پوشالی» اربابانشان دم تکان می‌دهند!
🔹
وقتی پای منافع اربابان غربی‌شان وسط می‌آید، برای «حقوق زن» یقه می‌درند و بغض می‌کنند؛ اما وقتی نوبت به دختران مینابی و قربانیان بمب‌های آمریکایی می‌رسد، لال می‌شوند! این استاندارد دوگانه، «هنر» نیست؛ خیانت است.
🔹
این‌ها هنرمند نیستند؛ بلکه سربازان پیاده‌نظام جنگ نرم دشمن‌اند که در شرایط جنگی، مشغول عملیات روانی علیه ملت خودشان هستند.
🔹
ای کاش مسئولان قضایی و فرهنگی کشور پاسخ دهند تا کی باید نظاره‌گر باشیم که امنیت روانی جامعه با خنجر این وطن‌فروشان «سلبریتی‌نما» ذبح شود؟ و دشمن را نیز به اجماع علیه ایران تحریک کنند!
🔹
آقایان مسئول! قانون مواجهه با «سربازان فرهنگی دشمن» کجاست؟ بهترین راهکار، مطالبۀ عمومی برای مواجهه قضایی با این افراد در زمرۀ وطن‌فروش است.
🔹
وقت آن رسیده که قانون، «سلبریتی‌های اجاره‌ای دشمن» را سر جایشان بنشاند. سکوت در برابر این خیانت، شریک جرم بودن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/461730" target="_blank">📅 09:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461729">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حساب شهریور ایران از دلار نفتی سرریز شد
🔹
درآمد نفتی شهریورماه ایران از ۲.۵ میلیارد دلار گذر کرد. پیش از این در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از فروش نفت وارد کشور شده بود.
🔹
با درآمد وصولی شهریورماه، دست دولت برای اقدام اقتصادی نظیر افزایش مبلغ کالابرگ باز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/461729" target="_blank">📅 09:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461728">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obc3LHq_HzKwCqL_X-sD9wkof4-tKo4pT15ZmTF3EEDrlDt0ao7Ri9aUdDlsDH5mt_P-Fdunq5Fn9maXBOtOC5iOJ3DC1XXEtDurqspkg14iQTCRPbq_y-d-ZWKC3xi5ZwLB_SCKyFMCmIPAK4QVQo3MgnGhEhJvQ0GVKA2TvQOzU4pNHLdKL94YAICRBPZuQTYwUkuMl2d_r6gTsR-8yaJpFmKe4sMM5hUsqQjJEHamSnpXyvIy0LRJVZ1XdXzr2PKfNd1Wk-rz9gQu8tuzN7_uaDMepYmu8-6hJzvYxeBlU-wi3JIb65obJ6KxlwtuPcZURr5inbmsUTqtPdVirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/461728" target="_blank">📅 09:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461727">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4298f547.mp4?token=kTkfuW5li93l0OdFaakYj1J6xLvf_CgOrxURXXEvyqkTZ3Q2KF1vgZY-Haaw5ft_HCedNv-21yNCH_W6uDf4hHnnDV-s3E5OR2BSTOpTirqnoX0huEeW3ukzoi0GszwcEAcNHnSHWevrJFyV8UW296w6-j9zgbu5Qwo13z_Kt7NQrOSBjptceUoMa507X9UJvpYL2rQemO4AC0RF8lwbZsdyALQQuZH5ujtsRQ_0lRId-UEhdA4oMXXTd3-9_qbZ_AZYu8qhnhcstoXX15eKHbFUIwEnfx24DPmGHjq9ZFYqGfbeTSxEP9DG9cAqQq3dn1eHmdrLRLl5BODcfeSrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4298f547.mp4?token=kTkfuW5li93l0OdFaakYj1J6xLvf_CgOrxURXXEvyqkTZ3Q2KF1vgZY-Haaw5ft_HCedNv-21yNCH_W6uDf4hHnnDV-s3E5OR2BSTOpTirqnoX0huEeW3ukzoi0GszwcEAcNHnSHWevrJFyV8UW296w6-j9zgbu5Qwo13z_Kt7NQrOSBjptceUoMa507X9UJvpYL2rQemO4AC0RF8lwbZsdyALQQuZH5ujtsRQ_0lRId-UEhdA4oMXXTd3-9_qbZ_AZYu8qhnhcstoXX15eKHbFUIwEnfx24DPmGHjq9ZFYqGfbeTSxEP9DG9cAqQq3dn1eHmdrLRLl5BODcfeSrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی برای نیمۀ شمالی کشور
🔹
هواشناسی: طی ۲ روز آینده همچنان بارش‌ها در نوار شمالی کشور ادامه دارد.
🔹
امروز در آذربایجان‌غربی، شرقی، اردبیل، گیلان، مازندران، گلستان و بخش‎هایی از زنجان، قزوین، تهران و سمنان بارندگی داریم. به‌سبب شدت بارش‌ها هشدار سطح نارنجی شده.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/461727" target="_blank">📅 08:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461726">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPCtkw6WDMZo_k_tCgQyWBCLQB3P77NGmuRWnWZapk2lhMmRojluHYtYKnogUqKWCATMslZaSUYChQG-jY2WXAPOLjBxjCJ2eupFeKfnXaOBSpIY_j8LbXjnv3_3hoIOOYsaCQClKaqyk3TuDO-FZPxBOWi_dQr6rmX3X05jnDOwitsuEO5D3V3itu-ivDCyeKTNHBsIy67hw6i0RQ5L6aNIys06o0SwCiEURs_O59x1Z0p5igz6OtwtkpoTab4--na_kTeQSaRIO488RrCWuKpJvAlprXlT6MYrgMUQngDZ4FA-_DF0994qW4N8oAUja6GLZNZ9G3Z34nQMq18Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوان ورزشکار شازندی زندگی‌بخش ‌شد
🔹
اعضای بدن[قلب، قرنیه، کبد و ریه‌ها] عرفان عسگری، بوکسور اهل آستانه از توابع شهرستان شازند، پس از وقوع حادثه و تأیید مرگ مغزی از سوی تیم پزشکی، با رضایت خانواده به بیماران نیازمند پیوند عضو اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/461726" target="_blank">📅 08:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هوای تهران در مرز آلودگی است
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۶ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/461725" target="_blank">📅 08:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461724">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کشتی مسافربری با ۲۴۰ سرنشین در آب‌های اندونزی ناپدید شد
🔹
یک کشتی مسافربری اندونزیایی با حدود ۲۴۰ سرنشین پس از مواجهه با شرایط نامساعد جوی در دریای جاوه ارتباط خود را از دست داده و عملیات جست‌وجو و نجات برای یافتن آن آغاز شده است.
🔹
تا این لحظه گزارشی دربارۀ تلفات یا زخمی شدن سرنشینان منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/461724" target="_blank">📅 08:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیشب که خواب بودید چه گذشت؟
🔸
ستاد راهبری تحول دولت سیزدهم اعلام کرد ادعای یک بلاگر دربارۀ شهید رئیسی کذب بوده و او هیچ‌گونه سابقۀ همکاری رسمی و غیررسمی در این ستاد نداشته است.
🔹
یک نفتکش هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفت.
🔸
نیروهای یمنی تنها در یک‌هفته ۵۴۰۰ کیلومتر مربع از خاک یمن را آزاد، و در این عملیات ۹ فروند هواپیمای سعودی را سرنگون کردند.
🔹
«طارق صالح» سرکردۀ مزدوران سعودی در یمن در پی شکست سنگین در سواحل غربی، به ریاض فرار کرد.
🔸
تیم‌ملی بسکتبال کشورمان با شکست ۸۱ بر ۶۸ اردن در ناگویا، راهی مرحلۀ یک‌چهارم نهایی شد.
🔹
سخنگوی هیئت‌رئیسۀ مجلس گفت خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای سهل‌الوصول است. در برابر آمریکا صرفاً زبان قدرت جواب می‌دهد.
🔸
معاون سیاسی نیروی دریایی سپاه دربارۀ ادعای ترامپ که می‌گوید تنگۀ هرمز در اختیار آمریکاست، گفت: بسم‌الله! یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنند تا با پاسخ رزمندگان ایران مواجه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/461722" target="_blank">📅 08:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461721">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLaLYz1Vz5pm4IogJABgp8ACHx6x2vUvOPo18qPdzA6eUWbQMVCfmtX3k6Z_mzho1bVJgo--rvyALYOLO03b_7gwMvXZ8wD76yP-rmHbinGiGSyeNJlT9jj1A2gqvjJzla8mwaZ3V251WMqEdq1bS8R8RKNihrMlTsc6EpKfVp45CrGN1ffRi83RBvUOKz3WeOD7KJ7jHlbpu83PXZP0mi-KoIExS9qG9tQLUnv3ppUu1ZjkIIvevmcO-JU8uiXCztzMAHH3PtYUniPgkGV9UKpX2bjxe7VU5zVp6SccQFTEV-jFMOLx0k_-bBIzJUj8lLveDZDPWDoPQ5AXMPng2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای سهل‌الوصول است
🔹
کسانی که از صلح با آمریکا دم می‌زنند دنبال تجویز و تحمیل نسخۀ تسلیم‌اند.
🔹
اعتماد به آمریکا به معنای پذیرش فریب و حرکت به دامن هلاکت و نابودی است. در برابر آمریکا صرفاً زبان قدرت جواب می‌دهد.
🔹
خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای، آمریکا و اذنابش را تنظیم می‌کند و سر جایشان می‌نشاند و این امر کاملا دست‌یافتنی و سهل‌الوصول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/461721" target="_blank">📅 07:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461720">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d29d2c80c3.mp4?token=KeXHJ4mPx7BJ-hQbkG-IakwqZdMnyxh-r_0kkufA77grVf0mmxHwoVw4jOZ6hNE-ZrqJxgL_jRAwuA3aJI984bkDrM1tdeaSeMd-GkvrsQgfjFuKi4eNPGlfOLl_RPilHiSKkF1-V1zsqs4mD9d0e23NDJjOlXuvMttg6XIjRYQvdoYfRUEa46ArtA2uDjNmpay2URbac49cgISgpgr-__EhoXCWN6ovU_6XrlYYB-cLleV_PUJJ884yZ8LoAbaVAIZDBbqRRMjDLyKHwNJFazKRG25tTiW-TwOWvg4oJXGq2q6ka7SRm9KmZo9rdqXBBhKZ_ZpjL6UUAWhcLHwB6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d29d2c80c3.mp4?token=KeXHJ4mPx7BJ-hQbkG-IakwqZdMnyxh-r_0kkufA77grVf0mmxHwoVw4jOZ6hNE-ZrqJxgL_jRAwuA3aJI984bkDrM1tdeaSeMd-GkvrsQgfjFuKi4eNPGlfOLl_RPilHiSKkF1-V1zsqs4mD9d0e23NDJjOlXuvMttg6XIjRYQvdoYfRUEa46ArtA2uDjNmpay2URbac49cgISgpgr-__EhoXCWN6ovU_6XrlYYB-cLleV_PUJJ884yZ8LoAbaVAIZDBbqRRMjDLyKHwNJFazKRG25tTiW-TwOWvg4oJXGq2q6ka7SRm9KmZo9rdqXBBhKZ_ZpjL6UUAWhcLHwB6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم آمریکا در ایرلند به آتش کشیده شد
🔹
همزمان با برگزاری تظاهرات گسترده در دوبلین در اعتراض به سفر ترامپ به ایرلند، گروهی از معترضان در دوبلین پرچم آمریکا را به آتش کشیدند.
🔹
معترضان در این تجمع شعارهایی با مضامین مختلف از جمله حمایت از فلسطین و ایران و اعتراض به سیاست‌های آمریکا سر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/461720" target="_blank">📅 07:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461719">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیرو دریایی سپاه: اگر تنگۀ هرمز در اختیار آمریکاست، بسم‌الله!
🔹
معاون سیاسی نیروی دریایی سپاه: ترامپ در فضاسازی رسانه‌ای خود مدعی شده که تنگۀ هرمز در اختیار آمریکاست؛ اگر چنین است، بسم‌الله. یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنید.
🔹
آمریکایی‌ها می‌دانند که اگر شناورهای آنها نزدیک شوند، با پاسخ رزمندگان ایران مواجه خواهند شد که نمونۀ آن نیز در روزهای گذشته اتفاق افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/461719" target="_blank">📅 07:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q01QJwwopNJK0_zNH4qUVqpIKqQEGFP7hqQJb0vJg-TcyuoHeHYrWxY-vrrmLStV9AzKQ1MyRoPTZH0p54OY14-DcMWwjyZUI62YQDKOM95P0BWgXI0GIDb6ZKRw21WfKy27GtRm46nAO4CsMBfO6ydxVmZkgvXrRia1lFkCP5ZCoJOeYTid_ee98-J-9VgFNYgKlfUH1XovxdoTMbdc1FJiiBmEUDDWYYqXR0NVo6Ipgb1hp9VuprzFj61aEY-6pfflDmaYt6AShpeWNEJegF8h5QxexYHIZ1MScGbcdXtgNH7jz9nvdXV49ttLgdYDB3jdQsUVZiGm3_hsjJLXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OULf7WUtt3ePvYGUhrXCyD7pFz8c6njK4zTrQXmQNFkuXt1WHo1NSi8QVP63r7dL5nT-7Aqz7Akdf-ZUmm4fnJ9fDVLtUvZyZYlqdFQEH1nBv_Abq2be_HstCJ1TEVAZe0Jbi9pcCUubyKpTyGUltYTo1Jf4CtJ4yw64g6e849bnWbGFBhVd5EqbzFy9x_Vc3v0oV8Z-hAk-6aAoKVZ-buql_bX4KiF08vgXehrsJj7J-pjqhVJhhjY2YJKYstKBK8DQq9iGDW1AM0iK9ulHR7Zo-kSX-e5M8Ttu2bOD4L4CopASH3XbPX4Fpv5QfO2ueUPBObJ5ndXyfvGrQqkAIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عراقچی با جمعی از علما و شخصیت‌های دینی هند در حاشیۀ اجلاس بریکس
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/461717" target="_blank">📅 07:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b76ddaac.mp4?token=kyOkkz4mYPJX5Z8V3-M-B7COxAXsVFTW_nbQVNGURACXxyHeodnLQTfrhpbelbc37g4YLvc7UCa5n-eZJWdO732y6wkm3CNY0T5gHyduDFuBLY3DygAgrhEMZoFxhPPGOmG3TVeW4PvyK7n9ZAEk5KQik3cj2UeAAMoWgHZVrQebUrO2ibJCJ_TAcLSc9yBSJeqDhgBYoIi--jlvAN_huqHkrP_PuyxHitftJ1kxK_A6r0_ppR25g52dK8KlD2vK_gXHIOdNBbm2hJDbYh_HaL-fAFmUe8oRHESmuUOxCuqYYMQfSfma_EiSzXOC6ZuYgFGmYj2jJS8pIEwTQDu9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b76ddaac.mp4?token=kyOkkz4mYPJX5Z8V3-M-B7COxAXsVFTW_nbQVNGURACXxyHeodnLQTfrhpbelbc37g4YLvc7UCa5n-eZJWdO732y6wkm3CNY0T5gHyduDFuBLY3DygAgrhEMZoFxhPPGOmG3TVeW4PvyK7n9ZAEk5KQik3cj2UeAAMoWgHZVrQebUrO2ibJCJ_TAcLSc9yBSJeqDhgBYoIi--jlvAN_huqHkrP_PuyxHitftJ1kxK_A6r0_ppR25g52dK8KlD2vK_gXHIOdNBbm2hJDbYh_HaL-fAFmUe8oRHESmuUOxCuqYYMQfSfma_EiSzXOC6ZuYgFGmYj2jJS8pIEwTQDu9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازهم تیراندازی خونین در آمریکا؛ ۲ نفر کشته شدند
🔹
در پی تیراندازی در یک زمین بازی در منطقۀ بروکلین نیویورک، ۲ مرد ۳۳ و ۳۵ ساله جان باختند و عامل تیراندازی پس از ارتکاب جنایت از محل فرار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/461716" target="_blank">📅 07:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzB_BKS3nmoZ_hy_ij9_UbTALz271IlTiZEf3NZgxOcjrtZT9V55R6KotyP0TBNCRKLMeBHprbcfBwP7NyNmpWT7RVjf8CqzrMRyIu-XL5B_ETIK4ivOqFxJmN7gdDKc747UPBroyDMR5HpE-N7pOCMCbG5VqAaVDsBPm47oZk98alB99tjmz3Olr2UCZuTutdJYUqqZrMDpy6rQgn1eDl_LUmT8bZswIP44LWR1x44UOAnPKpyMLUDXyVTC9PcF0F6p-TRodB0aZ925ytYYyHbS7dAvsgFzQ9tSjhINIxaygg6IDfPI_oJ5K6BoTo0HcFp3y8sSq5-Y6us_ISNcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار قربانیان آتش‌سوزی کشتی در فیلیپین به ۷۶ نفر رسید
🔹
در پی آتش‌سوزی مهیب یک کشتی مسافربری در آب‌های فیلیپین، عملیات جست‌وجو و خارج کردن اجساد ادامه دارد و شمار قربانیان این حادثه به ۷۶ نفر رسیده است؛ ۱۳ نفر نیز همچنان مفقود هستند.
🔹
هنوز علت دقیق آتش‌سوزی اعلام نشده است. با این حال، سخنگوی گارد ساحلی فیلیپین به نقل از یکی از بازماندگان گفت که احتمال دارد آتش از محل نگهداری بار کشتی آغاز شده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/461715" target="_blank">📅 07:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461714">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lasuZ7BhiPyGrKTk8c6nfAIgnPS5JaPjPqcE3NA-cRhH1drQlxyTZTX2bke-7A-cYd6-5xoMRgTAGBgECIW-Z-_iQbmBYTYjtpeZoucO4TtFLx3CQdqRB745kesFI6GYIKAaQ1YTkMPGz-KJc1Dgo9CqNIkBPa7fgHm_pLqupJTN7kK4YI1Z2NEXQFblIAcakVNBhvtdQnlErA5FKQ6gm7M9dzCOL0AIuu3TcTIbguLeFXgC5Eh5N_SfuIbz3R6NMvJZo7TeL9SC0knderv2CcQLO0UQkPIP3TnAJPs4ogg1jJiBXPcO1AZ__rXfcecc0Luri-EpO02YWdVRFAKbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تیم‌ملی بسکتبال با شکست اردن در ناگویا
🔹
تیم ملی بسکتبال ایران در سومین دیدار خود در مرحلۀ گروهی بازی‌های آسیایی ناگویا، بامداد امروز برابر اردن به میدان رفت و با نتیجۀ ۸۱ بر ۶۸ به پیروزی رسید تا راهی مرحلۀ یک‌چهارم نهایی این رقابت‌ها شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/461714" target="_blank">📅 06:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461713">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9Vif6YkZiZC0fsSXUEgSe78oJD5CZqBItTHpa0Wvys-PrVNX7mwOOWlM6IZg6MoWmKTz7Gvej1gdbNmgUa5_B61O0JZN4mMAlBrnf_Uq07YLJRpsvb1W3fkNzckLUTH_Cz9ZS1bDNaDgy-dZ8zRtIkzYpAw67dNCc59Ir63vCgB7uLfYTUSt3GGUgfJfrpNhNyCaNfga-Ps48HOv8h7BTS02_leYkGW_BUAe70FUK_6l4WYTCT4AdhP8yCXFmuicMjQNf1ixpgX716CC8xvYtZjtBV6G6eYVd5PsA2PDCYq9CKNu62nUrum_8FMhdGN1fzuLG_Ihml9qdoLRo8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن زمان سفر کشتی‌های سعودی را ۹ برابر کرد
🔹
یمن در ادامۀ محاصرۀ دریایی عربستان سعودی در دریای سرخ، کشتی‌های سعودی را ناچار به تغییر مسیر و دور زدن قارۀ آفریقا کرده‌؛ اقدامی که زمان سفر را از ۴ روز به ۳۴ روز افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/461713" target="_blank">📅 06:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461712">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce80ed84b.mp4?token=hoMxDQ6FLE7Yxt2I3eqIPSIESJyMm6eDufIWMQOi2ixCrOEd5S45apt9hLRiJPL4kYDibK43X_xntsVYI8CPsLBFVlt4sUv4kV77qYrJQb-FbowbyuIp6c-gJ3grm7ofL0f6L0j3TbxYyMgbMC_F9wgA42UoO4pjEgxZZIShra7DaxOOTKZgMdSWS0kFdRxyzG7xOVQ2mnvzUs2774ndgpA7dxyyix6mD-VhofK21ERIZwGWdIG_3neQt_w_8hAJRKY79gLj1GA9YhYDF5EQlhLDjxRpXDZfh_VBkGXkZ-csD3XENpt8n7kv2uARwcqDxukhFuJ3Dp6y2IZ-wbDZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce80ed84b.mp4?token=hoMxDQ6FLE7Yxt2I3eqIPSIESJyMm6eDufIWMQOi2ixCrOEd5S45apt9hLRiJPL4kYDibK43X_xntsVYI8CPsLBFVlt4sUv4kV77qYrJQb-FbowbyuIp6c-gJ3grm7ofL0f6L0j3TbxYyMgbMC_F9wgA42UoO4pjEgxZZIShra7DaxOOTKZgMdSWS0kFdRxyzG7xOVQ2mnvzUs2774ndgpA7dxyyix6mD-VhofK21ERIZwGWdIG_3neQt_w_8hAJRKY79gLj1GA9YhYDF5EQlhLDjxRpXDZfh_VBkGXkZ-csD3XENpt8n7kv2uARwcqDxukhFuJ3Dp6y2IZ-wbDZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لگو انیمیشن جدید از شلیک موشک ضدکشتی ایران به دشمن آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/461712" target="_blank">📅 06:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461711">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIreMnlNtUt_wWDMj2J3vFttzBRymh62Hs3__fkOgQCHOxNaxqIOQ-k0da3xiqS6JbJHcb2Y9k025rb8goiSuAi0zFpMJZ-LLaq6R4BPVe7s5Scj2N55HzSJm2z_PjjNHySPSjsFgYMLYuJf7YABSK2ryI1o7rpsHY4wxLoq3SASE-uMEEA7rmCurB0hAyMJ8QtvF4szcDSgL4AwuzKK2-_Eu8BxXw6ODCV4GqfH0Q0SQBHDBVEUdram5Q_gyI0iaYCqfxa8HHbc26EfPBamdm4AUqHNMBvbELZqKQQnqkktDHKZNQ2GUOb0wnQN319UwPlc4bZbEYAUv3eFJ1LefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کم‌تیم‌ترین لیگ یک با قوانین جدید فیفا
🔹
مسابقات فصل جدید لیگ یک با حضور ۱۶ تیم و با قوانین جدید فیفا از روز سه‌شنبه آغاز می‌شود.
🔹
بیست‌وششمین دورۀ مسابقات لیگ دسته اول، کم تعدادترین تیم لیگ در تاریخ این رقابت‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/461711" target="_blank">📅 05:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461710">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icaGpSU9GoC3Qn26xftHdopgvrdiwsTzrQsx5mgb6-Ldgqbv7ZDzB941MyqL7Owo_eJVFTVLTpcLmhuMWe0NcTFecXT_izaaxBTzRRkJUXi4_YI77mBWE03joSZCyU_Zw_yttVztZ2KF-BoUSrUrqx92-zJrvVDZSZEbR4NSkB5l0c-c4qbcK2odgnzKBeQZYHLdZEzbBo4V_0blN462-fSj1Z7twm4vHwB0WrdxJRnpO9wtJ6SA9AQrBhs42tAvM8pKpLDQSdZX_3Tadi-A02ZCXpcJjuDEW8pmzU5KH6ZUaXmZ3I44qy4QWZBI7PuVjT4IuC96WQ_ZNiIv8PZVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرکردۀ مزدوران سعودی در یمن به ریاض فرار کرد
🔹
یک منبع دولت عدن (همسو با عربستان سعودی) خبر داد که طارق صالح، برادرزادۀ رئیس‌جمهور معدوم یمن به ریاض فرار کرده است.
🔹
طارق صالح، فرماندۀ شبه‌نظامیان موسوم به «مقاومت ملی» است که سال‌ها سواحل غربی در جنوب استان الحدیده و استان تعز و در واقع کنترل باب‌المندب را در اختیار داشت.
🔹
این منبع گفت که شکست سنگین طارق صالح در سواحل غربی او را مجبور کرده تا به ریاض برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/461710" target="_blank">📅 05:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461709">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5w4Tsyz3d0mpcXtIE-Q-vl5vTzuK2TpOcg7wBtEteufwQvUwhGTAcsqJKogoE-YfBGI74vRQfLzXpObW_GArGjoEAey7p5uxGJyOuUMCroQM9jWKZp0bdmoHt9g7_eI6IhnARExDsfSI3LaWuMNarCwMiBXgnx4DZBid1EpD0LIQ1Hnne7z-VVwhqzbfNZXWGDliTCuidwmY5Q-Pbc_Jp4ceiDzlX9fFTwGfjvZqFNHgaGoAksFI1vpqJBEh09raEGqW5OG5V4VZAStC0arQ6XoIfqJ8nmPYSnGiIsFjcs2ViHWxNx_gRsfa-IYFpmsm70P3OnTDoywM162yGIQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از جاده و آب تا فناوری؛ چند گام تازه برای ساختن ایران
🔹
هر روز، بخشی از مسیر توسعه کشور جلو می‌رود؛ گاهی با ساخت یک جاده و ایجاد شغل، گاهی با مدیریت هوشمند آب و گاهی با فناوری‌هایی که تا همین چند سال پیش دور از دسترس به نظر می‌رسیدند. این‌ها بخشی از خبرهای…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/461709" target="_blank">📅 05:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461708">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اخبار غیررسمی از سرنگونی پهپاد سعودی در آسمان یمن
🔹
برخی منابع غیررسمی از انهدام یک پهپاد عربستان سعودی در آسمان استان الجوف در شمال یمن گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/461708" target="_blank">📅 05:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461707">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e663193587.mp4?token=B4MmJAFgcMeArRAr0ZscEf54lppVJbHsGRDjGZoaMMXnGbc6Qi7_uCoCu1CNal2GafuoJt39Ig9UU5y_sr0jJtieo8YvwRFFNWOUlfiChmNmVS0cDfIN4hZ0lBQ4NdeFAz_ddxgy392vIeJUazV7USY8IEfDebVVJjl2Dqq8NhKkwEwXeHaDMzZQ00D1fSiFvbWrWYczHCW5ClaFK-LQX_kkWXgr_VIveyG_jZbkYrNPDK332fQJChrAhLagAxAYKYxAWfUwT3J7auxTZywloRM-BjX3wNXJoe4LnsIUgqhc3OMYzr_OXPva81d2TqiTBXUTyut86NGa44PuSqt3rDFg0mxk_u0XDLATscXHyrT17oHnTGY3Z2q8lHG92x2YEVEYBt5eJh_3QM77pftM21zzQoIaaVe2rucWzuYlFmi0b74-pfjbqmGTQxqaHjEowqk8HJ02j_YkytD_KFDKZU7j3PtBKImM_Y07g2NPuYOO6NQw-ZCqi4AL38zfPkaEeht6b0bA4mbXYGmWH2Fc3m9PWYzkPTUBE8a7bew4PPBO3JD5rJbaSJpwPxy4dJm0SIKBFTqRT6wqknzDCASEDFN0MrPKu0XFnI6rC8d3nB2Whe9topvMKVkXMWX-6dm3d60FiEtUPeEp_OXoAKpbEye3uqlIVOAN6lqaJQ2ns74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e663193587.mp4?token=B4MmJAFgcMeArRAr0ZscEf54lppVJbHsGRDjGZoaMMXnGbc6Qi7_uCoCu1CNal2GafuoJt39Ig9UU5y_sr0jJtieo8YvwRFFNWOUlfiChmNmVS0cDfIN4hZ0lBQ4NdeFAz_ddxgy392vIeJUazV7USY8IEfDebVVJjl2Dqq8NhKkwEwXeHaDMzZQ00D1fSiFvbWrWYczHCW5ClaFK-LQX_kkWXgr_VIveyG_jZbkYrNPDK332fQJChrAhLagAxAYKYxAWfUwT3J7auxTZywloRM-BjX3wNXJoe4LnsIUgqhc3OMYzr_OXPva81d2TqiTBXUTyut86NGa44PuSqt3rDFg0mxk_u0XDLATscXHyrT17oHnTGY3Z2q8lHG92x2YEVEYBt5eJh_3QM77pftM21zzQoIaaVe2rucWzuYlFmi0b74-pfjbqmGTQxqaHjEowqk8HJ02j_YkytD_KFDKZU7j3PtBKImM_Y07g2NPuYOO6NQw-ZCqi4AL38zfPkaEeht6b0bA4mbXYGmWH2Fc3m9PWYzkPTUBE8a7bew4PPBO3JD5rJbaSJpwPxy4dJm0SIKBFTqRT6wqknzDCASEDFN0MrPKu0XFnI6rC8d3nB2Whe9topvMKVkXMWX-6dm3d60FiEtUPeEp_OXoAKpbEye3uqlIVOAN6lqaJQ2ns74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با فرزندتان درست وقت بگذرانید
🎙
هادی زینالی
#تربیت_فرزند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/461707" target="_blank">📅 04:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تصاویر الاعلام الحربی یمن از عملیات بزرگ آزادسازی مناطق ساحلی یمن
🔹
الاعلام الحربی یمن تصاویری از عملیات بزرگ «والله أشد بأساً وأشد تنکیلاً» در مناطق ساحلی استان‌های الحدیده و تعز منتشر کرد؛ عملیاتی که به گفته نیروهای مسلح یمن موجب آزادسازی ۵۴۰۰ کیلومتر مربع…</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/461706" target="_blank">📅 03:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اصابت موشک به یک نفتکش در تنگۀ هرمز
🔹
سازمان امنیت دریانوردی انگلیس خبر داد که یک نفتکش با پرچم پاناما به هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفته و از کار افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461705" target="_blank">📅 03:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCcKLbiMjr_uSZVqRGUWGckW2dpj4z2jejrO5MgrIu216rZ8fXWtpDX6grX07hM8SpMQbMNkKlsmpyVM7Xp8IwgqxzQrJ88_U7iOGj9n5jbfNC-m3Tujg9B-09Pf6A1kz3-d9wVA8izI6kAdOYp4XKW7hY6W4BrqL3k2csu22iDFPzSni2QRD9NLIjL8h8yOHgh5bPsVPoFu6ZDH3lCRTAcBu_67GAm8F-N_r3NiJ69CdTUTt5Se0sh8UzmFK_IMzYaZWQtzaaEMk4ofN97Z7FPow4BV3Cszi9Oowa13-9m9qYtQycK1qhZnXSTsfBOQD0-oWJYHdFjDoHUd5BrU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقق پیش‌بینی رهبر شهید؛ وقتی ریاض برای صنعا سلاح می‌خرید
🔹
این روزها که فضای مجازی مملو از تصاویر غنائمی است که به دست رزمندگان یمنی افتاده، پیش‌بینی چند سال پیش رهبر شهید انقلاب از آیندۀ جنگ تحمیل شده به مردم یمن محقق شده است.
🔹
فروردین سال ۱۳۹۸ که چهارسال از حملات همه‌جانبۀ ائتلاف سعودی به پشتیبانی آمریکا به یمن می‌گذشت و نشانه‌ای از پایان جنگ دیده نمی‌شد، رهبر شهید انقلاب جمله‌ای گفتند که اکنون تحقق آن برای همگان ثابت شده است: «من از تجهیزات و امکاناتی که غرب در اختیار عربستان قرار می‌دهد، نگران نیستم، چون اینها ان‌شاءالله به دست مجاهدان اسلام خواهد افتاد».
🔹
و حالا تصاویر غنائم یمنی‌ها خصوصا تصاحب قطاری از ماشین‌های زرهی که این روزها در فضای مجازی دست به دست می‌شود، تحقق وعدۀ الهی را نوید می‌دهد که رهبر شهید انقلاب بیش از هفت سال پیش آن را پیش‌بینی کرده بودند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461703" target="_blank">📅 03:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRc3nkqjuwC5IRCWdzcltNoKFjNfUrYX7EvallTMkZlAorUOHyOoiMTLTSsM-JPp5puuC-NzhbXoFf73FOzi8uvz80LWS2zJDwpptggTWkCIPidUV-g3pujGdkXLUonGIezRsOd4gMKBylVoaJbjXR2k1y94VwH79COjundeNGolxwvxfQXUAnhpM20HjitW4BamqDk3D2ua-9mZvfnMx50iTFQSqxdjMYph5yT_yoqSE51j7LBA5KTwXFSozETDnaT0z8lLMh-puYDBUvsZwcWhf8NBkt8kEFRO04JHIUyo1GyxobCOYr12DSsPEERXms3lOOfAZFK-jTiy28ijuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QYHSDSEcFQGgbA2Bevp52btpxZvFQP_OfFfxMjeyVyTt8DATTVXKduipqfbIytOKT5dDKXEtFlbGOAaMO1WW5iUhYonLem2hmhzkHoEpSM0XVaqy7TvjjJsiriU5GJ0fy5VREaMCk3he4v_lc95ttiaPOfB_B0zOJ6HK9vB7-Cwz938dq1I1GTJe5X2zl0l-jvE-SzuZa7DZ4zcTnythP142qhG4kAkCgQkJw1Tj7PRPvk6mIHqOfjCU1PGp1yww2UthVfHPdKoIU8TAiPTGawbz-8kEWvOrUWTWx2jQ6X9L1bqTCcicsc40C7HtEqRnu-bevIid0xoLKCGkcY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEFwL6iWHq0qeXofEJcaqGlqKxySXFIzN9v92lA6C1urHcBMqY-wYedqWHwLAVLO1EHmNB0wg-2boGh6nJgGujbEe2BXY0dVeNqE0DgPlG1ZgoJhpL-LkCKrfZNvqwQpHAjLEpxfr9KgWw53eU6HUEN1h6VfP2MURyvvG6T4l5BW5FBw6RtJuBg0-BXz-WYQ8OZ811gYEMqCuFG5L1nZcmMSw4NPVc02Rr5Jts4DvxMIvHeaEDUb2ZTgdyJ35ARWa3jP81W0r9x69bO53SXR8BmtEO0q6I8tDyx90YM5QQrv0Pi7xMwilvqXTKX5kd13GUj0oj3abiTQBI43FZ-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJ35hr1DccCK6C-HH5HxX4j4jUtfehYkGqFEKD1wqlCJdOAtjjoTB0BV-Ioy8YAvJCsPGJbRcNypEpcS1r0XkeLCqbHGQjXjeqf_3WCRdtJWOf3L7HC0wm83GqznlrLTRGo2ggvHSNymhl56KJO5yCVkcjtQz_kwfDwWYc5GkWaenfgpKcqClKBiqGhnjMzmuCA0puLPTuyiC-dvYq4j8cfNd8LhRnYsYBlAkt99nUe0Au0ZEKE0dL0oYiK0AY8xCezpv5xJy3AU4I6GZRaDNIBUtX11ZSwSX6uuYtJmNT5v0gWMxRkwJgA1M3St0LVDjEecY1BQD42mIsZyX4n6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU064D0-IEldX2Ry7ncPny4_CPTJC1d0L3jaVLFZYpTnqy2Y-o5K5ZQkfs6ECtucVld8_391WFqkMOYHZMrN6ONEkwqjBQTmXZZagQ7DnJ1DwMWmfqP6K8pmmwEDsB_FcrOKu1mo8qIAREwOTXNG7jW5voejNBZoNMhckdmvbKol-FHaqjry0442Yj4Ucb9U-NvImLwNPSDnAH1tcCYvaU8MMUtgLhtk3qoOBnTTpPg-_nbMiZAqjTr6hQUuWdfx4s6tCblEoTJ4ATZRyoK4bS9E2wvSfTgUOmIr892dapH4Cr1sHoags9bEf3mNnBjCedcJj-8fNGjsDq_kmcGQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIGsUb4DQcSKUc-adYhJPdNQrr75Ny1G7CfScYs_wvoXwz2PDEjX7PJ2spyRN_6Is43GOiheDMrVfrots_kP_5Uq5fBD3rCC_a6EvZZU2yTMNHqWbZHegmkZcT45snpbHkRVSjFg4I4HUlJVuouZo-QBKsDez0epIdlfNdbm74einNaor9I4yZzYijBJd94OHqzbhgaaMz5VUO9Sv__FbXyxFNIbzNHZRLOrQ545egL_jF6HwSzCZM4QGzQNdRY9vAeKg4AGh6aTE96lziA0epcXxF9Ee8jLuFa4Hg6u6d1UdCKNSt_0ab-32ZY82VE4-6tunn86p-2xdjwXCdWFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_dsohs5ASXYiQQkMjy9kRqM2S8C-M20INMMhm0mkqMVw40k-nXxFpC4b3PQUMJKwbn1MjTfkKx7eni_oTCSPKdeRUSVGnLBpYnM1EWYgYLdYJ-R97xmIvZnqU1CW_9E1-Hlib2lxgo-8lFdENVdBM_s5kOlBM3r8KRJs5FC7TZ1PK3N5hCwxBg0qDDC9AiKSnBPZYfOAe4cghLP8NKlplVJ_sSF015RhqkNXm-mzNEZ3mWlreExAZh45AjcqCfz0ltMckO-E8Th0feqbayt_nH6pVdb5x6qRFmd6831YAxbpwF6xUFiI4pozdszZz-DsAecAsk-PbWkBCdli6Ngjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=om7uGzMs0P5HiCohTmFZTAotBtpwApf05Xh7BqCLsgfpl9LPw3ENKwRIfvnFILIjvkZqd9VXaM7z0AYcJBFOkAavRKYltdJvLpAC0McNYUA7azW1-jJyv84uePdFL2bBsfLfxQj9PjGWxsZbk6pwTOR5eYFnzYe3K73fbqwFTHOWXzviDRj8TmJCCJUiJHMbKllPzkhAAQ5hWpAWjLvX1zW4LiiSiP_KSEKpkb8Uj5n8UI-8ZKdBSl2DY-pIbVPMchoz7W6bNJCyei_wvm8jqY2fg7OBOp6tgvIQ4POKQmlifbIK6vMSAtj0oSrGpFejQE0WgSR8af1S4H3e60jAuC4bfp0CEdJLaqr04yMispLjMj8Oy-AOVEY2YfFteo3Fkjlxs2jdxhs6kRbYg196yaLXb8jLxkUSfJmN26wQqLNed0caf-7PkyBdBWiOwRxZp51bc1wvm1TizOHIPztLuQaf1LTgS1iuvYmk9t4_UR8NY1zWKX05MbOj4AR3VEj4JPEymltnwk3DKzanvWTFiTGkAtA2lE_xTY1n8yVP610Z88qOGBTKxwnXnFOaZt_gfs0nE-7lCjrdroaxMKxBfnQ-_oZBghQRp6Aev8Iutq4Vgd_JEzR5_aJkA8QJCvwXSsm1z2TRWo9-nXHxNUgUtv3CRhXnvt-IL4F5XpNn9t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=om7uGzMs0P5HiCohTmFZTAotBtpwApf05Xh7BqCLsgfpl9LPw3ENKwRIfvnFILIjvkZqd9VXaM7z0AYcJBFOkAavRKYltdJvLpAC0McNYUA7azW1-jJyv84uePdFL2bBsfLfxQj9PjGWxsZbk6pwTOR5eYFnzYe3K73fbqwFTHOWXzviDRj8TmJCCJUiJHMbKllPzkhAAQ5hWpAWjLvX1zW4LiiSiP_KSEKpkb8Uj5n8UI-8ZKdBSl2DY-pIbVPMchoz7W6bNJCyei_wvm8jqY2fg7OBOp6tgvIQ4POKQmlifbIK6vMSAtj0oSrGpFejQE0WgSR8af1S4H3e60jAuC4bfp0CEdJLaqr04yMispLjMj8Oy-AOVEY2YfFteo3Fkjlxs2jdxhs6kRbYg196yaLXb8jLxkUSfJmN26wQqLNed0caf-7PkyBdBWiOwRxZp51bc1wvm1TizOHIPztLuQaf1LTgS1iuvYmk9t4_UR8NY1zWKX05MbOj4AR3VEj4JPEymltnwk3DKzanvWTFiTGkAtA2lE_xTY1n8yVP610Z88qOGBTKxwnXnFOaZt_gfs0nE-7lCjrdroaxMKxBfnQ-_oZBghQRp6Aev8Iutq4Vgd_JEzR5_aJkA8QJCvwXSsm1z2TRWo9-nXHxNUgUtv3CRhXnvt-IL4F5XpNn9t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر الاعلام الحربی یمن از عملیات بزرگ آزادسازی مناطق ساحلی یمن
🔹
الاعلام الحربی یمن تصاویری از عملیات بزرگ «والله أشد بأساً وأشد تنکیلاً» در مناطق ساحلی استان‌های الحدیده و تعز منتشر کرد؛ عملیاتی که به گفته نیروهای مسلح یمن موجب آزادسازی ۵۴۰۰ کیلومتر مربع از خاک یمن (۶ منطقه در استان‌های تعز و الحدیده) شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/461695" target="_blank">📅 02:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce86fb43d2.mp4?token=TBXdvSxc7QhDcUxaO1v3AQCrSWBMuaiXURf3kxjJfg36j1SC8BFAukDtjD1Fb697n1-tkADaaqafsE7XDFllQ6lvidYoE1ZbGbQRZ2eWfOPjyWMvHYn_7_lnkHVdZwb7c_LmpfpQXJN8HNm4D16OgfUgBBX3IpT1uuNWk1xcTf31CSYG-fq_3aBUEOvilt6zId_pT5JiGSckaJlznB1tXkguGthPNrLLnCEK3XIdtif4RLRjilxg4RaEPy1TwJDXQnW98Xhle6vtNUlO4_QOXPPW2R_cx88CGvcuhjtBjlcHmJS0JaHP5itfLsGQTK-d0eN7Gts-clx2Cp85gQTbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce86fb43d2.mp4?token=TBXdvSxc7QhDcUxaO1v3AQCrSWBMuaiXURf3kxjJfg36j1SC8BFAukDtjD1Fb697n1-tkADaaqafsE7XDFllQ6lvidYoE1ZbGbQRZ2eWfOPjyWMvHYn_7_lnkHVdZwb7c_LmpfpQXJN8HNm4D16OgfUgBBX3IpT1uuNWk1xcTf31CSYG-fq_3aBUEOvilt6zId_pT5JiGSckaJlznB1tXkguGthPNrLLnCEK3XIdtif4RLRjilxg4RaEPy1TwJDXQnW98Xhle6vtNUlO4_QOXPPW2R_cx88CGvcuhjtBjlcHmJS0JaHP5itfLsGQTK-d0eN7Gts-clx2Cp85gQTbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ هوایی جنگنده‌های سعودی به غرب تعز
🔹
در شرایطی که مزدوران وابسته به ریاض کنترل ۴۲۰۰ کیلومتر از خاک یمن را به ارتش و انصارالله یمن واگذار کرده‌اند، اما حملات هوایی سعودی همچنان ادامه دارد.
🔹
منابع یمنی خبر می‌دهند که جنگنده‌های سعودی بامداد امروز، پنج مرتبه منطقۀ «الربیعی» در غرب استان تعز را هدف حملات هوایی قرار داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461694" target="_blank">📅 02:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461688">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2R5unbNoiQojECNtTN6iCjhmF6kUuyETtFl5jNwNjNFp47kGMMtLLBCT0_pqxEcq7MtyQgEQB3DKfxs0jD3Uh0SsaWoiQyerTXd5DUjRc6uDEyhLQtrwLAptD5cOB0TtbN38IzR2TPm0ZF-A2MxaTH1e1aqWZ0j5LyZZgQTSnihrriY60arrw9L97nbZ2sDj7kBvfthPY0Zo8Wfnvnuo5Qu9jkCRliZGhtS65zx1vyk5nlxYmeF2WLcedefZDb73TD_jivL3z7Zrrnc7ExWKoAM_3w6xb2bLaAVSBgPhEhPQpHpJXUOaaoe6T94wkvpeBxag94kAbQ9sWspkCsl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS4e8-RspsYUMH6ZJTiSSM_-AV199aIjKeUNtEqIMjSJ2R0f2qJJ9p8PaKX7mGFxVNM9-DSQELY98zkTGobe2An4S7f27FELc0UNEUqQvyYUnBGZGGRFVxnuSpHHiRvQ0mHr15XI5LLuBu5-nmaxGFmWfy4F_Vb3cKQ6b5WFz4NdCWHzJu4EmQsZVuFx3s2cQxWx3lTe64fP0M-kqEX7iUWenuZPDXYf6eEd95tCHd_dae-Lv6uyaF8fCpe5pL-hnIF28wOvDOoXCmcjL3a_l4sWKD4vMvFa-1RkP6o8l86nZrrcgT9TXNDKvVndyUL8dg5CA-rmHub4o4TENJcNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMcpd8gFGFETJ33TMt5RTqD3JZ1lqMdGS4eMM5sokKTYR7-Os0SPmk4t0Ilnt8LPbV66gWsaePy2yz2nxij3yn38qKuH4T5dIkf3vHwWol18OvhhmfPh93nn9ozyYUVZWwziElF5hgczsYbsJQHygKk0Yj_W55cznjE2ijX1XT2UqmmBAuv4xDOZo3y1enrrzAweBIay8Nundg3UnQawEu-Q7OuaUHlbNWOvy5WbwCCcxhVyQhDC0_IrRdsL00Kyyp57uO6Yw7GBPnmTWULXMrstZhZ-EqwWBr2CAGejxVs9gnlPkb_ZCGfhAZGbDLQbjNj0_UYzMShh53IfWoZl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMG5Xkg5edMh49AClSyFFEYoEgJRYMMHl5qmIuJzPRT1hcFaDXsQaAMpmhmrr386iP09nPOifPW-IscWAWOaiz5SXmoVhCJtg220UZagxcHX0gmzEqU_5BNujVRPITahm0tMLqitIz_SKKhSTq08g-0zRsppCNymwwgYi5_deU_s0QXQi44OvlRbG33rCVldakgO1QKY7svMWDo-9aFgzFs79_bhtC-faJmJqhIsuc5xD2o0CwLZZpZKhRKsNVObFrh4Z6miyTpfq9pTA_JWZFiQ1zIwWvUtzewDXuWR5T2bS4qf2JJXUZVi93yvBm6crY0MSVxymZcBvs2eRv0onw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scHiX-tCvTTNxxBESlcNCZl3N5YCwBHOBPY1PnbrEHu6u-au4n9280pDXWt-OaA3F8af_Dw0PQ9DNkBNj6wQst0mo2EC6qcNOxqYyNuzWLKWpzYZqriSicwrUv5bhBEXFzvumdR28N_8SELBHaHgAbnsdjTPJnWUwGrx7zS0yZqrBd3IyScvv907NCzquDSrPNQb8hYNtw8R2Zpu-BRA6miHWP4j4ZpcylVqiR47KVMvxVgVsd7VItgNf7tRZx91GPpDI9ktTdUsck_CdWq8zw08DA3wRFIL0ndm7sSk_Qq5zlpBfJy4l2usOQju0Gt51TeQoU3LtQFlHS4fmzmugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHhuYmQDC2Bxye19JBAdrei5hoK9G-ajYybrUG1qEVOU-NsJfuApvFwwdTwqVFfNYGYu1iKpNLzWSMK9BaLPHrWuZ8GLD7TE8CNuILLlPANKV5LRKTdiL9lXHB6xp2FNd1DP8ngMZwrBgeAlcrajJbZiuf399JNDKUJrlj3nimneuaGUdFjtz2O2NyguEor7scrkvaHL39NXgQuzX04ipzSve86v7cad8uVqniZZBkQDzBiHKirUkEDvnYKrmAf7_Oh0W9sU94k8R0Tbpka85xVd2QO1V7sG5puo3hktA7EYTa-vFmmc8EA6PEkN2Ck2rEHADJrz6x_1C4zbV6Hx4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۲۲ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461688" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnrGG7gto7lIG8VpZ4V7zMFfERCGFzBe-CkvETLEd8SIRMSHmpRhbs-zQ6Hk5jSczFQi7S0fPPV2lQ9OcJAAFUTbB5ROXvH8q7Bokr48NKtA68W6gJCNI36yXDzNGX5ZKkAKi7uH8bLxw5nCNCIIrOmt_7QUd7FDhS53cMpv0jPqwLiE0hcUewaEs6vZzBSeFQ3pGNSUMfaMQfzzlxYbA8o-fynQRLSSKTJGEhHOL_cOmPIQW6gABes_4dr95uJHXOJ6cKjWpWjBGpOUsPfNDcKl4FRYzlH4Jn7VZy4jiCA5rIACrp6LUx1qqiNlZ0dDWB9ozIG-NLDt-D63F4ixzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_fpO9DVOJGaYnbuoEWhiHHcrgbGmrAKFWSPELbWc_Ro9DYrukUGJW02yRWFQaQC15F4aNhOVz3kBeO2VFZiGPFUTs2UxTIFufWJlRQ8BuFEk7iLPvya55xGH92yyatBJFw4X9Z5cdv0Lahkfjblyf3W1CvNWhK-BgNhItgyoKHH9b_rhE_vWBZ_28n_l4k160f9N-yWoX7W7ADDn2B3kUcPq1jz9fK9y2-yaVTwWq1Fpu8QNFt315IXLVyqWMqAeSJw50BnBUdyMWEq3QGrA3_aCDtg7PGdmjGylVskpq-IcC230_RwWSgy19E9C9q5yK3E_ZRak1VgCu9US3e2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRKgEgzur1G_qLbrqp3c5YsbqgURNLavuweYzx-pQo1G_cIKQssElkzvqMn-PQxv3ELs38aXr97QOf44yKxw95iE9u8ncuzKHYX1e6R2jGonGK4eANtH4fmKjAY5BQP4V5pLDMxH2GxrMJpKOBSLeshYt0W91fE1knGES2xUNk_Jf5AoPhk5mSg4KROTlanai2aYykdUIjsWJK9Vo4o1stT2X827AG2SLQTzRYdATyqregcFsPij_fSsq26NVnyQ7WJDn58N8qdM1_MRb6dQ0ghiaiFQUGZFhJBCA03eEeJ_FWXqlrjDtdhBibmrv3xDlTcTQjOuuHAFtduX4l79nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFfKA5na8MUUefUFiO4PFwSfI6aUiXNdvpTkHcfFk85uz_HZWOPYVkEumnbFraEdH05D0FHcd553VeDzeYHPCwT1KIdKoEgk9HVoyaasH2NM_ZeLLwAN199H0GABQfyAD9stcEDtQF51KNmjxxMo4-et2rBNJslFa208byylfXj_GaX-s6qgH6PGDl0DRdxBENTcQLGxU2AKmTo8znXc20CKYBgoZxw8PD8h_2jnlVT1su9U_HaQMlOVm0Zl1RK14WICDeS9u0gDL8AVp91QmarEKXxelKKQar_rmT9gS7xPbrP8vvUA0F_g3cKshMcNTiRfs4AAuMpOesKh33D1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osVgEL7mLUl_Hn5jZBlz-ag2WVUW9KNmuPGeeh9nlai25Jc6kUyJtZoja50s8bcOgVN3OfxvZ-l-UYmzeyOPrDTR_HW5jwB5H9vfb1p_ZjUCri2fcHtRwqTxZWcGFCsTZoZYpxqZTdItM4jTHDGvYwK-PJcgWu8OD17tHkbm8fUCyJYei84o68yC0avJYqPm5SjX7Jlm6sz9Zta3tXLerPzlwCNlrbnkXhF3rPnWkY7bRVBo5cf_-Q8MAFCwJc5IqkPTIcM0cJNFAKVKlXKCqHLeCRPNLVNjbVbsq0gMzfjWazhVS9i4_Ds7OGbKnxFjFrAt7qfGq8yGfYL4EcTd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBZVDeenjiiIwd1BGPFdPSB4stO6QDfx9hU0rmZf70hBBGS5t16wCfL0ZlHxt3Bf910XVm2mUkfxDEXJ80R8N9lvNJAca52uYgAYKeQ0odKeyaKp1IEf0zl8iMkDM9GS1lTIbmDshmTJbxgNW5vX6T_I9IkqVzUX06giRRoLm1UJT76p1pyPB5HEHtmrHX9ocMVlAjUcsokTEe05JzvXHf_xk0z2UU6xRdGLIgVvJlid-LSR1fv1o2CQxUp0XcZLnT-pcc4IFPqPiEGlt6jOXCTOEPqM1iu7VlmFe_baXyT3Bddvc0BqZLlU3r6tt0TEMNsdzk4F7gCRVCLNEQgIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vh-OzCVQq9z5TrD2rsT0ajByxVTgtdXUkSBIM-fg4prj3sEcW4f0GGvJUoUbwRrjug1k9HQUfy6-1oz6BKILNow0JLcQdg1ad124cEweFC9LCD3IipoxaQiRhnizPyxJpsLeP0yaivUkB_oIGywSa4OBOLgCab3FCJGyH4y2ujxjmYrTbjXUKfflTvEmU0NX35PHu23hBP5zse7raUInaRCWkUehVZsdjX3BcEw4qPJANdrJQNTvZmlsczg-2OblXUmnoGEAM_gwO2zKne3dmPZPI_6ipgi2y0UId7ER5p2PZ7TJzfddBwjITcJ-OcGD1aZh8Gd6GogwrknvsyGbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmsVsojDF0_yD23whImTaq7jCtEEYgEozg5lnsj6lk8DoAhB9pf0PhpMyL8h7kCZwp5UMm_6XoWo_tLhl6fbz9K3ueEjDFfiWiEjdXWRnZ_HeayYRG_FyKPlhooSGaD2p2IKEogEbnT_wg0_pou0sKJMEGFUZ5ctbWQXfnAcMCFeRBDuWVKv_ehyI841vO41VtPt6BiMQq9G060sEccmiF2IfOgbDFCRyT3d2KEQT9DRo3cT4iI3ZLbXMC5OlAZ-Wg6zO6mS8dSxYSrfHnmAm_Tx-NsQSDGTkx29NuTQIDCf9HAzvZhux5DouOZtvw503gqv3uRi8p-DeAWsuhEakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCIfoHXQGNHy0BS9vXBVN0-spSlgbsSFDf25IEvib2mKMF89fS-Rb-ct8s-KW3yCwqd9aSZ0dSpTlVlT_3vY1uhwXtc-y6rDYTgpRx9XxLraXK4oH8zIpviZBFTG9mw2s0fEHpXyh6Dof0ATf0M7c1XiIUMrn6DxGtMgWjrVnfM7HMo0qHVwYmWQm9U9a2cmk0_nBqAM4A5nOYKFjVOHFGSFgeypV8yJbwCXc8Sd_o4OE8vMxZO5eVBPUVZZv50I0cOYMC6NoyAJSMVUGxjLF-GoFLMHPavHVnscGSdgAPCOsyS1Jwt1SU8lmXMEVSdgiSLETSIt4Ldv95Ahad3J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skytA-Pc_Lx1EsC5ByBzeJVohskqpUGllIpySUQG0GWpVTf6oOAKyRyEqUZ1RVMn1JSOGVHNtCdlzy2NNwIFr8EK4I5cIuMoSPUEayqerVXr9z4IlnshgRTxa8MoykVQbF9cFrn0RUC5Uem7nW5WR4LiSevh9t_v8m80poIIvHqLFMDjVC3JNOd3I2Ym6V03Qrykph3nAYfHLGK1ynfuGumxgChgyd8THiZzd3ouGm2keiAE0MukRw3YTz2x0bXzkMNUi-si5aavUf9TrUQmzxITOvzZshWmqFr4iD14DrVXV41VgsPnf___BBaeccbrWZICKPRBduIOLfmigZHpcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461678" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به پایگاه نظامی عربستان سعودی
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که ارتش یمن انبارهای تسلیحات و اتاق‌های فرماندهی و کنترل مرتبط با تهاجم علیه یمن را در یک پایگاه نظامی در منطقه شروره عربستان سعودی هدف قرار داده‌ است.
🔹
این عملیات با شلیک شمار زیادی از موشک‌های بالستیک و پرتاب پهپادها انجام شده و اهداف مورد نظر با دقت و به‌صورت مستقیم مورد اصابت قرار گرفته‌اند.
🔹
این عملیات در واکنش به تداوم حملات و تجاوزات عربستان سعودی علیه یمن انجام شده است.
🔸
یحیی سریع تأکید کرد، به دشمن سعودی جنایتکار اعلام می‌کنیم که ادامۀ تجاوزاتش علیه مردم ما، با عملیات‌های قوی‌تر و گسترده‌تری در اعماق خاک آن کشور مواجه خواهد شد و عواقب وخیمی را برای او به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461677" target="_blank">📅 01:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2y4gaTwbiusGPl1w1b0zeofzm5qDIhqUYve3Ept7gGR_KWN7EYIgEOS1qYVvGplVDSrf8eBJ2pbL_EZDCFkEmtzkVNDDHIcjkTRD9LN9WNIU1hFhWpCMDOYGjQ4yKhFMyAt_QYfVxE68rl5amCxIZUnxjU_mmHGl2XbUKDTYX5ynUCOPb2cxjahclKuGwneBITzhuNMmRAI0nFAEE1kTMZn6ZDXeZmWvbIwKioO6hIGJX0pGwylKZ9NDgeAe0BETycjB-gkJX742_7KtcR9g_Cqq9tqW8hyFJ7SDC5XtoRyE5FG9na0T9Q-QqySJVomH5EqampZfJ86jaMTUzQ-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: مردم ما را نمی‌توان با زور و تهدید وادار به تسلیم کرد؛ ایران تسلیم نخواهد شد
🔹
اگر آمریکایی‌ها جنگ‌طلب هستند، باید با نیروهای نظامی شجاع ما روبرو شوند؛ چرا علیه زیرساخت‌های غیرنظامی، منابع غذایی و معیشت مردم جنگ به راه انداخته‌اند؟
🔹
اگر آنها انسان هستند، چرا مردم را از دسترسی به آب، غذا و دارو محروم می‌کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461676" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461675" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c398ca191.mp4?token=Ej6CwXDKXYSbxYZDMIFqx2ggZqVnlzGIwM5OxzTpo8mOYzgEfKPAGqz6BWPsAR0ces3j2_uVvxdF2z3RZBalY-biI1AGCkAk11qoH7bQxO3YkjhHX1r9fXXVXNXKuN9MipEDqGvSyna9-aMYzKLsurDwIfukruRRB3dLkTHFG11WDp-ZEofxON4Udkzxy0sm-XZZMgeKCyOCPU1e-vC_gH-Oah3hImhwD_LyHFkWXKbIRZGLqVXEzzqeK4iMPFNXKOy6ThB3oc00iFXkY305EHIr-i6mYy3IthSkvjr5HAtx6FvDTsuHvGprLW-zrI9rx04KjyvSjxOv8Fe2gQmplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c398ca191.mp4?token=Ej6CwXDKXYSbxYZDMIFqx2ggZqVnlzGIwM5OxzTpo8mOYzgEfKPAGqz6BWPsAR0ces3j2_uVvxdF2z3RZBalY-biI1AGCkAk11qoH7bQxO3YkjhHX1r9fXXVXNXKuN9MipEDqGvSyna9-aMYzKLsurDwIfukruRRB3dLkTHFG11WDp-ZEofxON4Udkzxy0sm-XZZMgeKCyOCPU1e-vC_gH-Oah3hImhwD_LyHFkWXKbIRZGLqVXEzzqeK4iMPFNXKOy6ThB3oc00iFXkY305EHIr-i6mYy3IthSkvjr5HAtx6FvDTsuHvGprLW-zrI9rx04KjyvSjxOv8Fe2gQmplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال اهالی صنعاء از ۲۱۰ اسیری که سال‌ها در زندان المخا در اسارت بودند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461674" target="_blank">📅 00:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt2CGFZauX0tpX6pdzzIfD_2W4fCBfcP8JJ-y_VY6awQ7nSzTJA-3iWTaBHjQEHOrN5amjI6AycKD89thm4uxq26GczKVVe1S3SaLrFhHgvatzWPmnqJ3Ylm-UngW54Scx6oqRQ2GhR2xfl8O4AInUtgVQw1OKVDf6K3__N7N1MWFdSWPvl3qOnunKdbSFYRcpHdYoUobVfNsKxWk1Cnsh3wvEHxgThbreahdRBqEBaE2qb5yPQvIHm3vQl1DGxtBJz7yGrycVjWNGfVuLPIHrPEKKuyz_V2v31_B3g5tb166qzlV3L1sReGdaEat0VEa4SolBUevd-mN2qe6WXKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نخستین روز ماه ربیع‌الثانی است
🔹
بر اساس گزارش ستاد استهلال دفتر مقام معظم رهبری، ماه ربیع‌الاول ۳۰ روزه بوده و یکشنبه ۲۲ شهریور آغاز ماه ربیع‌الثانی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461673" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31de2b1af9.mp4?token=LWkxNuB8lI9VokRsHuv-lV5GCmtTO7BDOL7Vl94M0tcBW0GFe_w0KZLad3KtTuZqvsmCRmc-ApfojvQBHQB-2CO1XNg4LMIkkH7EZCID6iPSUrMPTM65-Fbwwu-0PaatzTIhEyLghKmjT0F9qpXprvTNbQHzQ5q1Ef7VBEz_d4Gl4SOKGFP67QqqfM_oQuP5EAENVdfQ8w97ud8PBPLF641uDBJIlWJ0fW_2Cp8SV3OHyfrrZNu2PjNJieCTINPwpOpBACm3ESO8S0E3Y4UqhIxtOocBBPTdrf_3Rk7jMCVeXeQ32jC36_M2U7L4dw9k4RoDm9H7hreXKNBgecqxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31de2b1af9.mp4?token=LWkxNuB8lI9VokRsHuv-lV5GCmtTO7BDOL7Vl94M0tcBW0GFe_w0KZLad3KtTuZqvsmCRmc-ApfojvQBHQB-2CO1XNg4LMIkkH7EZCID6iPSUrMPTM65-Fbwwu-0PaatzTIhEyLghKmjT0F9qpXprvTNbQHzQ5q1Ef7VBEz_d4Gl4SOKGFP67QqqfM_oQuP5EAENVdfQ8w97ud8PBPLF641uDBJIlWJ0fW_2Cp8SV3OHyfrrZNu2PjNJieCTINPwpOpBACm3ESO8S0E3Y4UqhIxtOocBBPTdrf_3Rk7jMCVeXeQ32jC36_M2U7L4dw9k4RoDm9H7hreXKNBgecqxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر رضوی و مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461672" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acLBkcMC77YXFleZz5-R8LKKvf6-wCddMLrGwtBS7VxKMvqyid7gJnGDteNf2BvDRGJE7liJfQTaV7vu8sm2nSsl93fKuTSZXIQE5jBtm416Wyhflc2NI9xyW0NIZgUHqGI25e3290ZJyCFgwHEnCZAT_mtBhsfmnJW9PbiIgNgIhfnRsEe7_dXWaoYAhKuqsvEal6LIdm7IeBeXyx8EF0UMrGz5611IHWkAxP2E3781az03P12tASG8I2dlDPOVg2-c5MVO-a5C2S9OUYryE6zdHR4dm4MHQ77ubwtiv3s0NDtm6FDCjxUnm071YGD24pVcUCAAzsal9WsVnLXNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی درباره مرزها با وزیر خارجه عراق گفت‌وگو کرد
🔹
طرفین در این تماس با اشاره به مهم‌ترین موضوعات در روابط ایران و عراق، در خصوص وضعیت ثبات و امنیت در مرزهای ۲ کشور تاکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461663" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ypdOZ3MdsV_bVdZ9nwTsj_8mcE-37jnhPVlzJRiIv2jLSq1k6mrUJ6b0ZxY92b9O8lf5wQKPTLysVHeciPzGLLO0N3r70FrPJrtzQapD_XwxFkSaVYJWaKI36PJg87PEV91oJSflHMWzXi_lCVteOL3yRaFIQJRCej15yU9eVhA-zVZND65sKKq9HKNUuVP6B3hzj186qUMpuwxawaS8S2bjgCroQzypEEu77Asx0w9q3HilKm0ne_S-UkAjmEn9EMiUIafzdgteiltVZMo5h8V5pWYBc8e-JyDwg9jO4MjrOVnnXDZXV6EGEhdekoqkgh-oe9R2WGxHG0mqwKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دولت از خانه‌های خالی مالیات نمی‌گیرد؟
🔹
با وجود شناسایی حدود ۲ میلیون خانه خالی، درآمد مالیات بر خانه‌های خالی در سال ۱۴۰۴ کمتر از ۱۰ میلیارد تومان بوده و وصولی این مالیات در ۴ ماه نخست ۱۴۰۵ صفر اعلام شده است.
🔹
کاربران با ثبت پویشی در فارس‌من خواستار شفاف‌سازی درباره تعداد خانه‌های شناسایی‌شده، مالیات تعیین‌شده و میزان وصولی و بررسی علت ضعف اجرای این قانون هستند.
🔗
اگر شما هم خواهان اجرای جدی قانون مالیات بر خانه‌های خالی هستید، با
حمایت از این پویش
به این مطالبه بپیوندید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461662" target="_blank">📅 23:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apLxGNyYM_X0wXpe1g2IhxE1Yxcw1HsRVMajziG4zeueMkrPKNso1RAuaPXkiCVofysh-6YyZl3fg1UnaqZUJX5nxO27iLt4Hic3tcoBWfcrElpMseywsd10x1b30TxSnESmPW5n1ekE08_4oTeO5aHvvI_RrQ0bm-Mk5DNp9sGQlXKfT8Q5nfMtQMn__MgVaa1INWpRSQyuJBBWaGu-o2p4YkvYvh7fkfOFEMDIno5_p5TebmkBHoTf0w9yzSV93ynTWjukJqJXUvXvgl54vy8wNTQDiiJ3M9Bwy84uYU1n_ITJmCCa5uXEqO_VVKOdsKNsjK31pLvvlYACNnKJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۷۷۰۰ بار توافق با دولت لبنان را نقض کرده است
🔹
ارتش لبنان: نظامیان صهیونیست از زمان امضای توافق آتش‌بس با دولت لبنان حدودا ۷۷۰۰ بار آن را نقض کرده‌اند.
🔹
هدف نهایی اسرائیل، ضربه زدن به اعتبار ارتش در داخل لبنان و در برابر جامعۀ بین‌المللی است. @Farsna…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461661" target="_blank">📅 23:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yg-XhDORugdKVHCG8q5uo0e0yU8Nh-8uss1q2vzRWdKyFpCdKMG3cg6lzPvLpvgkPrUYS8lPx7lsk8JTCiFV3DsPXfAacKo1sFMqpYkC9RFIvZvbAysu1NBZa0JOGUGvWBlLWwAPbDsR7umY2DK0s_ZjxTh3SfvnVqfy86WBM4mIcQ2po5uZAcD7IVqZO1JAgQHbJ76qdoOl_m-JoqQVglQs7znZp1kf4z6PJb7wwbztiFw__5mY25cs7WtdcCbzjfyXm6eCJn39ozslDsiEdX8_QTHJic3ppyOJc6EIL13dFSHWA0Pn_b_mNq_LLBmcmiWXN8-msp7ucHzdXZXM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-qdswPXjaiNjOTNZjmcmQCdPpYP9tp_I6WCJrSiA9pbnfIoceraUhKCQ0q4EVzlUtgzE3ssu4Zp293kVk3z9xcV_qU4NdqxQcarrgwLKd6H--an_HCVEsc55sQUCvVYCIpV6iZxh2oCxU3XGdm-GJnEOUq72rcrvjKhGBAev6ZpnEwA1bkYZyS8RfQNH193YLnM979hL9HuwsiUWPGseKRBeZt7bmMMp_D_pd7et2euuO5XmZEybG3lT7Qe1tjkHBEA9ZDG9lm4fnyII7gG4frEWSSgqZhkoi3mzfogLoi9v3eQWRqMq5hSSve1irvmJevBhB57hjANexg5iGqWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doamqdxB5W885ZPXm3xzO5jmLDYkLjySgLJUs-mYEv-gV3eEjeHvfwf_OcFg5icTY5LqB6jxt9vtT8JTOo3QMyfEPq16EjY7zzaTzw6rbu7w-AwJdZ3mOz6PSl-1Kc_tVpfVXxD2vXdnB8mKp6P2uFQ1j_Jd7HJ4Vdtud4GeOT469I1hX7RC-1t3RBoQQt2uN2QXL9yj4Io1X44SEmeG73GLmy9pQA90TZkec6o9pNaU2h-lCYp6SWzBExyOkiaeIDrwq451ws-nNkxvZ_5a3SZkKN7fu_Ojgk_09wOIDkmoBJ-1lRGNfc1FN3VXRAn5IRcZQ6XLaSQjZyvaKBA2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEphxkwnfAPhFq7_F0eLGPYkGyA_lpAbLhEZtG8HZQttj6Aq0G--EdenXSzEPjsGQXMiubuC22Pevc24vI9TKmkDv2RWeS9tkOaFD7buhH75p_WtfXkjGzcpK5qip6j2eKV9xeSjSkwUzzhWWjmjoejB_mWnXsCHYeo5eg_5TYsYJDo0AnSG4nYy8W4WN1QsKpGZ7jOZDYLnRP-JXDkeVsLRCqqka8rZxA7ZEIVeoNyxjKjg0POmzIROUH8-iwgadFWYxxGfJfgAVKF_VMPeTeQY4ikrVhl_qqIZr0A8dk8Btm2q0QgqZrPvlwUl1QdG980OFII8ogmg4TKya2au4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdbYjxrguhssHcbZFa85hGSnI0nGccxkAR_NdoCJ6x2AKFcmB5lBcMMpNiah4MYNiwX52Fr6W_T_JoyWUKABexuEftdll-MmK6z7uiVryqR0RgMOndDia4Ce5AST4IJ67YfoU2cJumQJnGHCvx058I1qZYuQu2udivbdlNHSAUpEfNfxSaBEYr8q3A-QED2u86YTMoEJQ-oY0vr139BfIogXdh8mLLba3f5hL4p6z8N4no0YeO5Y8pvzGfxksLQ12EdB9a-1YV8EpZQzEXkg5AZdJgCbMTTjqTVSJLxIW5I0szVBQWA48Unfi7pfiwnQ6Z4tKQAL4TneXzkGzBUmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvfJUjFK0V9u2vI0tPfrT8nDCg4HXR6bRMOlcMZcM4UIMc5aD2AxXpAN_Ir14YUUxOj2vv8UG0zSXMyg8ScxJ0L8EvHyg4gid5oXkvfeu-jyCUe-oD3XDVsT56BPRwycSojmkGAA4mnBVb-V_DlB0fI749D4AxaIpsJqOdFi_CBLy8jG7CKBia5gncMLAz7AV1uBokRjr-zO0k9cHABvbhGDIf7MfCQJ-XkN-g9vLGqDFm-r2tS-E9hOC-osatO_I0MztOiv0q-sq8qNIyXUxjDnBPbgOyXLyuX9_qK1xQDr-meImHMeM1k_peeFIbUQCJoFW8R3aRcH35JeXK497Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lC7mYw6mPX44ZgImqRi7hbqDNZAd5luCY81bxKFv-2mNGKST0LnctB9VabkS_PPicfoiPPAIfOeFtAUwv7R9arfbF4EGzu5HmYCL5YPFYC-h_CB3oA0q4O4nSAcuek_kk-4fRYkX1KLFKZAdcUlwwDVKLVrOK_d2RPukWyI3beO1PXFMS0zIRWaNg03opc-Wi85hmBp45CGSF0R6FRk0fxEFMPOhGaFonZLVRtGhmugFK3jvGLScv77GXUgF7dxPCcHq5nHj2VfjiePZS-uBPD16UaCWuXL1tTOKAxnh3PVxgOA3OMdbcZ7aWntxnKyVEIMNsxoR2gFBgERwpe4s7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری بقایی در محل شهادت شهدای لامرد
عکس: ا
حمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461654" target="_blank">📅 23:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5460e8a8d.mp4?token=sWHfHZgkzSjyDt8ShKGyFnUbdcq7-f5oKu-DzJ7PgEvFxR_RFls7QDkTwp0R82IheUxegH3qQyw9cgdxrv_mco9cChqD0cKsLf6rE6vwPwiZMOVGkOw90WAz6XBNNxJfgR-1MjexNoYDHZi7stTeY-Ml1iHU8r1cnOtRI_bWFd0G2PiYbj_57QXBTv6qq4dn_dX1qZKfh81zLj62uO0gHpFjz2s1ZZNQIJ9AaIgrkWF7IDVkXXj7apfXo3C8_IDG1oVKzCxrljfqWpEmDu96DcEnDdRZC5raZjXllUA_eiXnGRMiAau9pcG3KaBmc7LxtgBPieYvImCDt6F5imIj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5460e8a8d.mp4?token=sWHfHZgkzSjyDt8ShKGyFnUbdcq7-f5oKu-DzJ7PgEvFxR_RFls7QDkTwp0R82IheUxegH3qQyw9cgdxrv_mco9cChqD0cKsLf6rE6vwPwiZMOVGkOw90WAz6XBNNxJfgR-1MjexNoYDHZi7stTeY-Ml1iHU8r1cnOtRI_bWFd0G2PiYbj_57QXBTv6qq4dn_dX1qZKfh81zLj62uO0gHpFjz2s1ZZNQIJ9AaIgrkWF7IDVkXXj7apfXo3C8_IDG1oVKzCxrljfqWpEmDu96DcEnDdRZC5raZjXllUA_eiXnGRMiAau9pcG3KaBmc7LxtgBPieYvImCDt6F5imIj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سست‌ترین پادشاه ایران در کلام سپهبد شهید غلامعلی رشید
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461653" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd72072398.mp4?token=O-WOEz5NDH3yAzFxAzmW1qS5th39JTN_XwS7jAVTogKGr2eB73YIcTQ90KEAQT9AIGAQtLzDoxF2tPu09538uljS4LZnGQ1JT_V9-XqayCGiiMbM-gT_UQmvL_obteG_E0mNxSH6ollv_7zFGGmSAcq11_7jBDYz3ZS4rAsnYMdezSFVV_Vq-UybBrrjxULx1hABotNocy5p2ajYgqb1SkpFAL3SF47L4rLwGl3vufYMeFPTYD5pLBMfTnxAiv9LLWDp3oNDxbUVBIYzFgHcQAkcLIeuoahDiNXUtM7k_lhgB8JB6Q66mtFIKG4wC1AvckEkl4Z4_v6liDoHZ819Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd72072398.mp4?token=O-WOEz5NDH3yAzFxAzmW1qS5th39JTN_XwS7jAVTogKGr2eB73YIcTQ90KEAQT9AIGAQtLzDoxF2tPu09538uljS4LZnGQ1JT_V9-XqayCGiiMbM-gT_UQmvL_obteG_E0mNxSH6ollv_7zFGGmSAcq11_7jBDYz3ZS4rAsnYMdezSFVV_Vq-UybBrrjxULx1hABotNocy5p2ajYgqb1SkpFAL3SF47L4rLwGl3vufYMeFPTYD5pLBMfTnxAiv9LLWDp3oNDxbUVBIYzFgHcQAkcLIeuoahDiNXUtM7k_lhgB8JB6Q66mtFIKG4wC1AvckEkl4Z4_v6liDoHZ819Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهمیۀ مازاد سوخت تاکسی‌های اینترنتی تا ۳۰۰ لیتر افزایش می‌یابد
🔹
مدیرعامل شرکت پالایش و پخش فرآورده‌های نفتی: تا سقف ۳۰۰ لیتر سهمیۀ مازاد سوخت با نرخ سوم بر مبنای پیمایش به ناوگان فعال در سکوهای اینترنتی اختصاص داده می‌شود.
🔹
این تاکسی‌ها با اولویت‌دهی مبتنی…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461652" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYPlPsrFfeSRYK19REnhn8wt0Fr066R-AlHXNqWUFQtLyE4-GQcaP79OLSZUPMu-3ikFYHvkPU6yiSlzjqtUrW2r3QaL3OQ_ag87sGuYlrAdFlyVZBbOH3OrEShWnuAId0vFRvWPriGfWW5jlHiknYONwufD7lZT7syOpFqZC2GhwrEKsUEFzFKmTAuLlxomXTig9hftT_ZQHwr9NL40wqribQDu-sLUbT6ArvFds9_Xov2WfY2X6GI4fAXlsCslNVZu0vyesKU53aEkicsfEkVH6L5uhVlf3iNi3uby7GOzUJ740vNgj7aa-0zQgQOT9cJIT2EdVhtu5EfLnEkzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گوشه‌ای از دیدار و نشست صمیمی فرماندهان ارتش و سپاه برای بررسی آخرین وضعیت میادین نبرد   @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461651" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8051b458.mp4?token=JwLn_A2zTHrrJhgFKJ8nBUNRY9dJfneNg2FpR3ztma97oM2frbg3bwMA6utsjUMdpm4AidkVQM5Hb5fJzBuaE1oUN94miDmRoFwos5eofi8Tj0o7Ic20CU2-Jf_Y96-KHtHQFJB5lw2rSDd2DBxKS3VBZYAPOV513qBCKvw3VxksDnL1PlTYRD0eCqDYwtrZz4amYoearC3gHC7ke2yi-7pp2FVIW3X5vX7yRBOpvG4nqfkzFm7vSXNbXmVMH_88cImtfQCFGl3Lm57TuXIZzkSJ07l3zPrlehxGJXJRQJVkzlmYPd8dZoWWhWe1upwJCrlRyjCiG2IvxJILVE3M3YPVwybYPBiXiZc-fnfreHC_AkCm-9qv8P34wAkXgys_WGHOC4PECW_9SeSfE5yYXoPFRtAOScf2cMOLPYJsrL8LIqQZeQlpFUyvyeTtBPtmzDikalnuP6CfKn8JWr9SwLDN2ZqiUA2Ypez-pEOrupjv2pIYJGftmWeNlJLMovihscLv5kkLHm51ziyyXC6L1UXzWD3wgeP781wrxPomLwthjGXIJVRS-iYo2uDdqKxOhvYelqhpKjRk57KuQoOvfzzsRw8aI9mxzAQRVJvQl9xBtDmJyRu3_pOVHosjJMI5_GyFMPi-51plvJn-hzfqYEhoSgIbh0fPSZ1Himc40hE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8051b458.mp4?token=JwLn_A2zTHrrJhgFKJ8nBUNRY9dJfneNg2FpR3ztma97oM2frbg3bwMA6utsjUMdpm4AidkVQM5Hb5fJzBuaE1oUN94miDmRoFwos5eofi8Tj0o7Ic20CU2-Jf_Y96-KHtHQFJB5lw2rSDd2DBxKS3VBZYAPOV513qBCKvw3VxksDnL1PlTYRD0eCqDYwtrZz4amYoearC3gHC7ke2yi-7pp2FVIW3X5vX7yRBOpvG4nqfkzFm7vSXNbXmVMH_88cImtfQCFGl3Lm57TuXIZzkSJ07l3zPrlehxGJXJRQJVkzlmYPd8dZoWWhWe1upwJCrlRyjCiG2IvxJILVE3M3YPVwybYPBiXiZc-fnfreHC_AkCm-9qv8P34wAkXgys_WGHOC4PECW_9SeSfE5yYXoPFRtAOScf2cMOLPYJsrL8LIqQZeQlpFUyvyeTtBPtmzDikalnuP6CfKn8JWr9SwLDN2ZqiUA2Ypez-pEOrupjv2pIYJGftmWeNlJLMovihscLv5kkLHm51ziyyXC6L1UXzWD3wgeP781wrxPomLwthjGXIJVRS-iYo2uDdqKxOhvYelqhpKjRk57KuQoOvfzzsRw8aI9mxzAQRVJvQl9xBtDmJyRu3_pOVHosjJMI5_GyFMPi-51plvJn-hzfqYEhoSgIbh0fPSZ1Himc40hE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها امشب گود زورخانه را به خیابان آوردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461650" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2366b049.mp4?token=UYfeoFFY4X43Ji8mc5h9r-P9104MWcphSJXw7xf4OgKfFDsBFIUINi-liPPmWNa7AGfDxwqhWxLF_1da_fYNxoyVolLwC4u7JKu4AZVP5bmbJFnimSH-QEeesDi5T_Btxfs_oJQ72BsshGlQIVODzaayANpujsqO4G00hAUlSzIatz0eHVg5kkL7gqVnMN6LSNv8QhCbrvc7wQ-WqatbmPvTLUaD6I7gdEy6YzLjzYDtPBMVwG9XPrb0Sn5JRXlcRcx-QOJffhY8eeOloWY36DNrHi8gmpweFOujJsrTPri2s9yWDrlHcFbFO1nmTXwFGROsTwaL61JY04QiUCTIEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2366b049.mp4?token=UYfeoFFY4X43Ji8mc5h9r-P9104MWcphSJXw7xf4OgKfFDsBFIUINi-liPPmWNa7AGfDxwqhWxLF_1da_fYNxoyVolLwC4u7JKu4AZVP5bmbJFnimSH-QEeesDi5T_Btxfs_oJQ72BsshGlQIVODzaayANpujsqO4G00hAUlSzIatz0eHVg5kkL7gqVnMN6LSNv8QhCbrvc7wQ-WqatbmPvTLUaD6I7gdEy6YzLjzYDtPBMVwG9XPrb0Sn5JRXlcRcx-QOJffhY8eeOloWY36DNrHi8gmpweFOujJsrTPri2s9yWDrlHcFbFO1nmTXwFGROsTwaL61JY04QiUCTIEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند شهید دهه هشتادی جنگ رمضان متولد شد
🔹
دختر شهید جوان پاسدار امیرحسین کاویانی‌نیا امروز در اندیمشک متولد شد.
🔸
شهید کاویانی‌نیا در عملیات پهپادی ارتش تروریستی آمریکا و رژیم صهیونیستی در جنگ رمضان مجروح و بعداز گذشت بیست روز تحمل جراحت در چهارم فروردین امسال به درجه رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461649" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c12ee2739.mp4?token=patmc5_3xJbC12zMer_nKi7bwi_CqrrkNDdTY__Bl7Qpn4-o-J2uEX-Mfk-64OknAwbuJWTr7sPYWCvEVqSoEVAw847ThDQ6eBIdFFhgi9Sb2HuxM-D_jkM2U5JI0AJipchE6euCalaCD8CPGxC_RF3P5AcLpPy_USfb3atYJ1o081uGYtDVPysO7wPQANatXXKge0tdBQBsiVwEK5EUYUxFjurNWXwZ6bexwiGNx8KhMHYhyoBMO7H_lJG82gCgLh0F0Nd1wYB6takng-Lg2ZVFpMcMc51K2-8I5eMaELT5lAAHo8IV0b7dAB_havQTg_ectZ6bGNqPYSaYjp7KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c12ee2739.mp4?token=patmc5_3xJbC12zMer_nKi7bwi_CqrrkNDdTY__Bl7Qpn4-o-J2uEX-Mfk-64OknAwbuJWTr7sPYWCvEVqSoEVAw847ThDQ6eBIdFFhgi9Sb2HuxM-D_jkM2U5JI0AJipchE6euCalaCD8CPGxC_RF3P5AcLpPy_USfb3atYJ1o081uGYtDVPysO7wPQANatXXKge0tdBQBsiVwEK5EUYUxFjurNWXwZ6bexwiGNx8KhMHYhyoBMO7H_lJG82gCgLh0F0Nd1wYB6takng-Lg2ZVFpMcMc51K2-8I5eMaELT5lAAHo8IV0b7dAB_havQTg_ectZ6bGNqPYSaYjp7KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرستان ولایتمدار زرند در ایستگاه ۱۹۶ دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461648" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461647">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازگشایی موقت مرزهای شلمچه و چذابه تا ساعت ۲۴ امشب
🔹
معاون امنیتی استانداری خوزستان: مرزهای زمینی شلمچه و چذابه تا ساعت ۲۴ امشب صرفاً برای تعیین‌تکلیف و عبور مسافرانی که پشت پایانه‌ها مانده‌اند بازگشایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461647" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCJ5eYuUrfdhF-0mw_MB1D2R8A2JH_LYgyYVAVsOznaSCIVLr4VvPQr5Q6GBlkaWw7-3wNHKbZVYg1yPysnSNlou3iHDg4ibSNfVi218aQzyma7fxKu8f_ytHygRfn-FVFue7U1V0WIPxt1vKGoDT07RA3T757lPTgcqEUmUvAwChzNjH6DHuaEONPKPSmLgRWfxBYfivlgZgIlDNAeh7T8Q-4FBjOO24_Kpx5RTn5Wih7KthKtZ1iT57lndEhpM3SKAwc7GPv8K5-aTEtW84lbf1I0Oi3VB1FR_cOsqVl7GP9yanDgAuMDgWCiLlIUx-7tA5PLHrAft7G2JVpV6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/virkHb_2EhOi8e_HNfuLK4MiO5i1bXdw6fZJMCqqokr0lsyXKj0ZsMf3Ng0I65-DEwE_uhaA5RcfZpB2O_a3NhphInSb_1oGD3e2L67xsbApF3EuU-YvY9FQYL5GdTWf5Kk08dmoorkI5QhjoTuGK6FiPSO45JB0S-A8ox9rtTLq5fZfNHm4r4rYhCagLwyq18Fb8Zwfu2QSNQ_nKSBXmP42NounSP_mMHJSQlvO1VrkAsLbgmNHfxe3am0Q_XSzAtKuaB7PYb7g3Oq5I-JHRvtf_vhLNxzLYpUFo_ETRpj_-EKVEGgz0cJzzUOfgwoAQwrhsC15VPHSR9nfEKd-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9NeiBaul_DpnkjmcVO9HmArIQl5Oa0YWcym2BRoO4CIAYToeuq7jIE4_AMGl8LohB9SiEymgZC0QMWEfMu31DV_dRqqy93AYECXDSzJXZA88BT-AYE7i2xeNEZpSC4V4Mrm6hXSQgiRWnQqoRkfM8ocLCCtaiqIa53Cw6gHhDX4otrc53SRedFgrNQV9hZ4IrjeEWhEWV1s6EQZQdT7l-IYiIZPBvGCJadCt_lDIh7nIZggXIRaqvnUDdxoKHV2jT40dTyJkX5W5PQoW8xfnhgQo2o4dNm_HyMMR5h_V41TczKDo9HYeH7eNaGbEG1K6aWywwSVupx9ZWlgEj41Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zceye5EiV5SVpUEukhsewzsbSb2XLcbBW00fLKXMFeHSVYCM-0efBCvlNKqrojGVqJAnSw6iUz90mLL6e3PkadbhKrBMju67un0_DdOzbnMgV8XG4QX5nVO6nX5e8YAqcsEZWnGrflvQdYs5fneAFvUFpfyna4Zj5WMLxdVK6c7656W4NUre64F_sklnBxx6MfDxa4xdnjN87jrta5flW-SVsqiUSXG-vkHW3sNnFeOv-7VWmNioQAxGBY1DY78t0u7ljmvXvwk2BCO7akIxzhnJnXTwTxtXH0Jbxxu4bmOvoPtKqzjAUoyyFMTP4VNjw0XFnDDgq2pl7ro9mKfnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spTooW0ZxsIcE6tqej9uJSLtbiX-7EaJwbe-M1tA_GpaOIY_tgqbyEsmp_8G1Dz40UmgabGxqgQGJkRHZymBer-zgL6ZyOqbpxACGaRxsSCAtNsF8n-nzoIE6p6rx64RI37BLSliQ5tGmbvTuMjPHhUj_QCkVKUyzLcSDdBs_epOQjro5ydyvBs0OgCPlV5xkAiRDfjG26O7vMdDBTRjFdgT9ax73UB2QjP1W0a65-p496_hxKCqabkQ2DbGm91JNCKkI8AUUJ3boZHPIJhW2yWSgoHdrB4oZ4My1zQ7B5p6xwjLU35VbQRlawGrRsEzjbOEtfLs67klYVmSPNKG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG90aid4kYYokbPAB4Cbk9RF7pN8AZlNjL7vz8nTRXxjGTcu2c8u5eJp1Q1zIu4P0JwPNkg4geLxp_6vdmBpgIW6OArlmApk_ORxhVvy3C0QKCPDmJ4w0GUUKIKJD2_jwGcF2qJXoPzUgV-UPBClqGNDxSBoXtKjhNTvzm5U-6mDmnnEOO4vvl9_KOQ3lUrXEsd9tGTSIu65gyxuQ_qxt03QM7RHFQZy5e7LACVAM-ZXSnm0nBDSEeJ5RNj18e3AlAEFkr4bGpyvdXE3ZpS1cer44bRV4boolNprYrWYmuPJ_AJGPPOVWaoP6lDcnzFKZVArQgJpbVMu827Is405wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2_zl23_4GagA2QClpv8RGtAOBChbX5RamvUNwsYaK-N41y35OaZlmXK9W8JlRu-SaYRqOYtrqboqiuvTFQEa1rMOYkm5ceUBAXxOfmMipAzFu51m99pxDnOWazK7wSjxjlW63HVApDZWOXxBIdR8UW0OxI_7_r3agoyNNOOpFoEtMauTEOtx3sn1BV1bwkqHC9FeXHNLIF8iNFCbKUzAAayL7tIopnwC-uJdtsbg1H0R9aSH4imNcJbRAtybuMGaw4YMPhnhB5MsT5xCxtU1y4Z7-YjMD9qx5oWBI_iufyJDIlTl1VZvP8tAhtB8cYdK20VUi2iD3hQN2yb6vE9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9skPXt9q43HDNoeF7HsaDts1lClUcIIbXUg1kNz460WGnNLeHM_bYq6BWj6IaYNRU1AlJBy7-7KjRRxLmbFpXqNmX0N7G8n0K8kLu9b5h4f68ofIcusbgj45wFLx3jb7TBaVEeuSzuktuZC6DGjcdWoGng0LgNsCzCmgAeAozxZ2kEwezpukNJihnFoMaFRhNTDrTLRN1PHdWdbwqYudWSCLXxMQsx20xLNy-gBlCyvYReGa6Ed6Tm27Lx6AT2HMj6O84ZBKgSDTovNP0_Xyzw-MURvFFO-NAt_LZY-eUjr8aiSQ3SRjTCCgpf4jdCRLqP0YK3izy7pjZ5X16_pJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از عملیات گستردۀ زمینی جدید یمنی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461639" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملۀ موشکی یمن به عربستان
🔹
سازمان دفاع مدنی عربستان از به‌صدادرآمدن آژیرهای هشدار در أبها و‌ خمیس المشیط خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461638" target="_blank">📅 22:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حملۀ عناصر داعش به ارتش عراق در کرکوک
🔹
برخی منابع خبری گزارش دادند تروریست‌های داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند.
🔸
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461637" target="_blank">📅 22:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b31d3b847.mp4?token=pgNHyE5BCg47YsP0x1ihqQYlTz6s9eneAC135y2X3dgmpoeF3PTI4lc61aIhbD3yC-5hTFPu3mwEFEVCbQREGktCjeMqBp5P-o8YiWMvlbpKrUCpQf0dv4r2B7AkmzOSBqotjBaATMUW0ZQRKvBi0O6jkmWAXVFCO5Jm2QlbfCDVGiqts0pWTNchHsDNqg-KqS7az7ObtLqiISgGlZxxCHFYKwIcZXeShRBh8RbYjm8eZ7VnrOjX0eqCSZN2mwmq3a87HqV9TdXn6DFB2tDL7i1rUKMi4bfM6gn09Z4dXqtb6HIxGCGG2Re9ZCQ2ivX5XJwZtqYXyWDqEGUexd2Umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b31d3b847.mp4?token=pgNHyE5BCg47YsP0x1ihqQYlTz6s9eneAC135y2X3dgmpoeF3PTI4lc61aIhbD3yC-5hTFPu3mwEFEVCbQREGktCjeMqBp5P-o8YiWMvlbpKrUCpQf0dv4r2B7AkmzOSBqotjBaATMUW0ZQRKvBi0O6jkmWAXVFCO5Jm2QlbfCDVGiqts0pWTNchHsDNqg-KqS7az7ObtLqiISgGlZxxCHFYKwIcZXeShRBh8RbYjm8eZ7VnrOjX0eqCSZN2mwmq3a87HqV9TdXn6DFB2tDL7i1rUKMi4bfM6gn09Z4dXqtb6HIxGCGG2Re9ZCQ2ivX5XJwZtqYXyWDqEGUexd2Umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۶ شب حضور و ایستادگی مردم خمینی‌شهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461636" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8732cfd1f.mp4?token=iUiQ4TJxc1VnAEBzJ2Y2vx4_nwFKayoOTEkCX7YRYs4pXRpgyShVHzoMdvShG_M2e9n9XmhavPztmIWhF8GwKWn0kv58Ar0vzcIhXuyXIxc9N54z-TWDk1DPvZCZMOP6OH9HxtqKYKtpLdjLK7y81sulkAw1Wwtzu6c2vbCWK-BS929ajlxryeWcvn2O9j-kJCjbVmXuaL95asi1PWbVuT4gSEilosmH63EQepOvLO2I1bHGjjyqOF8I2NS3B-2cJO_R9M7jKnebbOT0X8dmvQ2xHuoO1kEGx27YY9ao251vlmdqBcgHppmH4RGWZQV99TyWV2H7oyPS2TfAV7mthg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8732cfd1f.mp4?token=iUiQ4TJxc1VnAEBzJ2Y2vx4_nwFKayoOTEkCX7YRYs4pXRpgyShVHzoMdvShG_M2e9n9XmhavPztmIWhF8GwKWn0kv58Ar0vzcIhXuyXIxc9N54z-TWDk1DPvZCZMOP6OH9HxtqKYKtpLdjLK7y81sulkAw1Wwtzu6c2vbCWK-BS929ajlxryeWcvn2O9j-kJCjbVmXuaL95asi1PWbVuT4gSEilosmH63EQepOvLO2I1bHGjjyqOF8I2NS3B-2cJO_R9M7jKnebbOT0X8dmvQ2xHuoO1kEGx27YY9ao251vlmdqBcgHppmH4RGWZQV99TyWV2H7oyPS2TfAV7mthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت صادق محصولی از تلاش سپاه برای ساخت موشک ضدناوشکن
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461635" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac454eaaeb.mp4?token=H_bmNNqxhjUbIJQV51Xfkj_i3770602T2PwDW8Q-1siBDhS3SEiwl5KzaPicfn3ImZxi_iltAd3k_6JyB6A_0bgFRLFs3ncucJBKjHQE26wlTS5I_RjVpwkY_vIxiIXx7wtNE9lj1Z0T36akIAwk_nRPuIAS7Y6MBoUnwy2Gwjl3Dr4mhGLd8HOAi5LSSUDsVI-PemmLrJOqo3Z0bsQByatJwyV-gBteddHNFFLq4THgcbbfkvARdn4y6FlZm2qIhvt_OvJrZ9Kbn4tabdQuozlFL0_BJeyGh_1QTUdbPNXilYQtiQAdvqcH2c3StdlWO7_AKnVZViX0qgO2BS2irQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac454eaaeb.mp4?token=H_bmNNqxhjUbIJQV51Xfkj_i3770602T2PwDW8Q-1siBDhS3SEiwl5KzaPicfn3ImZxi_iltAd3k_6JyB6A_0bgFRLFs3ncucJBKjHQE26wlTS5I_RjVpwkY_vIxiIXx7wtNE9lj1Z0T36akIAwk_nRPuIAS7Y6MBoUnwy2Gwjl3Dr4mhGLd8HOAi5LSSUDsVI-PemmLrJOqo3Z0bsQByatJwyV-gBteddHNFFLq4THgcbbfkvARdn4y6FlZm2qIhvt_OvJrZ9Kbn4tabdQuozlFL0_BJeyGh_1QTUdbPNXilYQtiQAdvqcH2c3StdlWO7_AKnVZViX0qgO2BS2irQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش تگرگ در بشاگرد
🔹
شدت بارندگی در برخی نقاط شهرستان بشاگرد موجب جاری شدن روان‌آب و سیلاب در مسیرهای جاده‌ای شد و تردد در بعضی مسیرها را تحت تأثیر قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461634" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
نزدیک ۱۲۰۰ تن ذرت علوفه‌ای روی زمین با بهترین کیفیت دارم اما خریدار نیست و دولت پیگیر
واردات نهاده
به قیمت بالاتر است. چرا کسی به داد ما نمی‌رسه؟
🔹
لطفاً پیگیر
افزایش مداوم قیمت پوشک
و افت کیفیت آن‌ها باشید. علاوه بر گرانی، گاهی در یک بسته از یک برند و یک سایز، اندازه برخی پوشک‌ها متفاوت است که مصداق کم‌فروشی و تضییع حق مصرف‌کننده است.
🔹
لطفا به
وزیر نیرو
اطلاع بدهید در استان ‌ما در کلیه شهرهایش همچنان
‌قطعی برنامه‌ریزی شده برق
از ۱۰ صبح تا ۱۲ شب داریم. سامانه ۱۲۱ هم اعلام می‌کند برای کنترل پیک بار هست.
🔹
در بحث
کالابرگ
، اعتبار مردادماه خانواده‌هایی که کد ملی سرپرستشان به ۷، ۸ و ۹ ختم می‌شود به‌دلیل فاصله در زمان فعال‌شدن، عملاً با تأخیر ۱۰روزه و در شهریورماه شارژ شد. چرا باید سهم این خانواده‌ها بی‌سروصدا با تأخیر پرداخت شود؟ از طرفی
افزایش مبلغ کالابرگ
برای دهک‌های پایین نیز همچنان در حد وعده و «امروز و فردا» مانده است.
🔹
مدیر مدرسۀ دخترم دریافت خدمات آموزشی مانند کارنامه یا تحویل پرونده برای ثبت‌نام در مدرسه دیگر را منوط به پرداخت شهریه کرده و برخورد نامناسبی هم با والدین دارد. کاش
آموزش‌وپرورش
یک
راه ارتباطی مشخص و پاسخ‌گو برای ثبت و پیگیری تخلفات
معرفی می‌کرد تا خانواده‌ها بتوانند موارد مشابه را گزارش کنند.
🔹
در طرح
جایگزینی خودروهای فرسوده ایران‌خودرو
برنده شدم و خودرو و مدارک خودروی فرسوده را تحویل دادم اما با گذشت حدود ۱۰ ماه هنوز اطلاعات خودروی من به ایران‌خودرو ارسال نشده است. پس از پیگیری‌های فراوان مشخص شده گواهی اسقاط من اشتباهاً برای سایپا شارژ شده، در حالی که در طرح سایپا برنده نشده بودم. این بی‌نظمی و عدم هماهنگی بین سازمان نوسازی و خودروسازان علاوه بر خسارت مالی باعث سردرگمی و خستگی ما از پیگیری‌های بی‌نتیجه شده است.
🔹
وزارت آموزش‌وپرورش با افتخار اعلام کرده
معوقات بازنشستگان
سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ پرداخت شده است؛ اما آیا
ارزش پول
آن سال‌ها با امروز یکی است؟ چرا باید مطالبات فرهنگیان پس از چند سال و بدون جبران کاهش ارزش پول پرداخت شود؟ چه کسی پاسخگوی این بی‌عدالتی در حق بازنشستگان فرهنگی است؟ آیا در بانک‌ها و سایر دستگاه‌های دولتی نیز با مطالبات مردم چنین برخوردی می‌شود؟
🔹
متأسفانه بسیاری از
مدارس دولتی
برای ثبت‌نام از خانواده‌ها
پول دریافت می‌کنند
و تا زمانی که وجه پرداخت نشود، ثبت‌نام دانش‌آموز را انجام نمی‌دهند.
🔹
چرا خدمات حمایتی و پوشش‌های درمانی بیماران روزبه‌روز کمتر می‌شود؟ مادرم سال‌هاست با
سرطان
مبارزه می‌کند و در کرمانشاه بسیاری از آزمایش‌ها و خدمات درمانی که قبلاً با تعرفه دولتی انجام می‌شد، حالا آزاد حساب می‌شود.
هزینه‌های شیمی‌درمانی، پرتودرمانی، آزمایش
و بیمارستان برای خانواده‌ها بسیار سنگین است. بسیاری از بیماران توان پرداخت ندارند و حتی از ادامه درمان ناامید می‌شوند.
🔹
لطفاً پیگیر
مطالبات گندم‌کاران لرستان
باشید. تاکنون فقط ۳۰ درصد پول گندم پرداخت شده و بقیه مطالبات همچنان بلاتکلیف است. کشاورزان یک سال زحمت کشیده‌اند و بسیاری برای کشت و برداشت گندم قرض کرده‌اند. حالا با رسیدن فصل کشت جدید، پول محصولمان را هم دریافت نکرده‌ایم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461633" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de67b0b2ed.mp4?token=EVhSI3PZl0yBZqfhkLm_LghOcWsSDgPzXTXZQpdk0an2EXbWMw751EodsrqeX7PxXbDp1--KV83L_UZL4Ex21JFOVnZsXJzS0K2GvS74yjjjWelOCss_LND8XWFpacXjPqcgyhK7Vp5R1iGVRmOUyAbwC5z8DHvqEN4g943fYo36BoCqWdUHiS75jjS6e3g84BiX-GNJij1lZEIMQ_eM_tXq3xdr1_uF4-R9S3cc85-NPTzFyUnqzwfY02RiBCEUmNELZQh3tS916IoVEHeHCqBOMjj37dxjypaWetGlIPcTrW7hUODnpAvQEnazRjCIebLsCUeZNEASLTcXqsBrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de67b0b2ed.mp4?token=EVhSI3PZl0yBZqfhkLm_LghOcWsSDgPzXTXZQpdk0an2EXbWMw751EodsrqeX7PxXbDp1--KV83L_UZL4Ex21JFOVnZsXJzS0K2GvS74yjjjWelOCss_LND8XWFpacXjPqcgyhK7Vp5R1iGVRmOUyAbwC5z8DHvqEN4g943fYo36BoCqWdUHiS75jjS6e3g84BiX-GNJij1lZEIMQ_eM_tXq3xdr1_uF4-R9S3cc85-NPTzFyUnqzwfY02RiBCEUmNELZQh3tS916IoVEHeHCqBOMjj37dxjypaWetGlIPcTrW7hUODnpAvQEnazRjCIebLsCUeZNEASLTcXqsBrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز ایران و ترکیه برخلاف شایعات جریان دارد
🔹
پیگیری خبرنگار فارس از پایانه مرزی بازرگان در آذربایجان غربی حاکی از تردد روان در این مرز بین‌المللی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461632" target="_blank">📅 22:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4lT3iUeL7TT14jVvu5e4UGXnxRJmLuC-mVe-u_5B7XQe0vzNKi03n3TGbdfTTQjpV8Hx1pQx6cFHo5IAFaervuY2KKcLpiHGYEi_4ry_DERyIT4hthFfp_dQTNwZXigFlzKXuk4vr90RYq8CJBNJgsXPnFQuGCNvcg4b8gE-eprAaHJl6pdFeY9CrohH3Qte9xzQpo3cC1JrPE_VmhV332PoGzBFiUWKCGMQck4RGRaubWAur9PFYsAhARqqFre50lBxoLSBb6KPhb7P_ItujlBGXc4iRu4ELekRxN96RzytfL-lhaNM7r4LMKnpkRtNcuUDybhIIdfYLmLmGj_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو: تاجرنیا به من گفت فتاحی می‌تواند کاری کند که داوران با استقلال مهربان‌تر باشند
⚽️
سرمربی سابق استقلال در گفت‌وگو با فارس: تابه‌حال مدیری به شهرت‌طلبی علی تاجرنیا ندیده‌ام.
⚽️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461631" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcc-DJHmKEB-8W9N6YSwo_MgqAGCxjGVcS161ORL_UV4f5eW5xWS5HNRE3zl-JE9eSsB_Vl-mYCCEcr9XqDubnT5QdMNce8XAVTL0kF2CtXbhSb-KaxSUudadrrZbcHtoOBpJq_NAnxzEcjzX6zemy9wAYaX7NvnzeRmzcWj5uXuZXwDrluaf0_CogFEJuOxDJs_zzqHhA1Q1U76m-kd_WSGKVsNxPUhStU90kpP8adEwNUsexlQIdnBvkNs8UeXrEuESgcJ6ZFYrTqfMnEbbzhHsVfEYmVgQ_SJHO54atJlnrTSqIs-9bRzdNCExWiiGxN33vXUMOGgk5_pD7F6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئله من و ساپینتو ربطی به رفتنم به رختکن نداشت فکر می‌کرد نمی‌توانم اخراجش کنم، همانجا عوضش کردم  سرپرست مدیرعاملی استقلال:
🎙
ساپینتو احساس می‌کرد خیلی جای پایش محکم است و آن نقطه‌ای است که می‌تواند مدیریت باشگاه را به چالش بکشد. من خیلی در قبالش صبور بودم.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461630" target="_blank">📅 21:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در امیدیه
🔹
فرمانداری امیدیه: فردا از ساعت ۹  تا ۱۲ظهر انفجارات کنترل‌شده برای امحای مهمات برجامانده از جنگ در برخی نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461629" target="_blank">📅 21:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K06vVCD6NafBdToWGrzqVV_NU1rJFkXlDDiOAuntqJ1G_ovPdNKesCQBf6mbF0RFjabSfxtaO4Sa4KxA2TcycIYsEytBV5UukvNlC09aHMjSWKB9LyL7Mxy5NDJHoOTAvV4aiuZw-sDWLfsKWtQi8RViVQ5A_YTgBuu-xvVKgfZMpCyl78tZFp1p5wcaEbPi11DW2yiXMqHaLrMBgjA_hp1OtJ-w6v9YuyJUNnQxyy2B_fijbUDQSP8cBoGrp0z6SVSmAQzGG3PmLOSZZ-A3ED5Yh3vG81BSRXcXSe1MPp2d9g-1eLeb_3QlmCF6ZQnUGmfpI0YuQ-B8GPpFZ8WPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای عالی سیاسی یمن: هرگونه اقدام احمقانه علیه یمن با پاسخ مواجه خواهد شد؛ حتی اگر پیامدهای آن به سطح جهانی کشیده شود
🔹
محمدعلی الحوثی: منطقه در وضعیت بسیار متشنجی قرار دارد. هرکس بخواهد آتش جنگ را شعله‌ور کند، باید پیامدهای آن را نیز بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461628" target="_blank">📅 21:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حملۀ موشکی یمن به عربستان
🔹
سازمان دفاع مدنی عربستان از به‌صدادرآمدن آژیرهای هشدار در أبها و‌ خمیس المشیط خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461627" target="_blank">📅 21:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY40_pAMEiwAIeulmQHX4oJ03GPcw0fhSjrmENJB4DED69VzG6fwAOcTXuUNTYYWha374CgY2AzgNxOB00NOrdi9WbdVp0rg7Pfdq6txyE9zFqOyRhBlfOYlDehi0HXch9-z0OQCnH-ZqBLqdNl9rqSKje_rfbP78g83Df0IdC2kWD734rEmNaxT6rSMGCoCx5Nwx8EayUCYQPI8e-ucAjEZfEgS_9Znw7Kd6X5jlfbsFRK0yVcA0hyNgfjRvduccAwylxZNUQRVHUUWRnM9KZXWn0hoIB5uPqN4O-uYJ1veRN-q9TVtBqsdWNL9r6HujjQ64-VJqeVj5GgOiS-aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متفکرآزاد: دست برتر ایران در بازار انرژی نباید با پالس غلط دیپلماتیک تضعیف شود
🔹
عضو هیئت‌رئیسۀ مجلس: دشمن قصد دارد با فشار اقتصادی بر کشور، ثبات داخلی، امنیت عمومی و آرامش روانی جامعه ما را هدف قرار دهد، اما در مقابل، ما توانسته‌ایم با راهبردهای خود، دشمن…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461626" target="_blank">📅 21:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf93b046.mp4?token=P2OQM9RAP4Nh2jw021AJPETMeA-JNVljN9FNqkd8SaRmlJuxES20zwg4YnFaef0WG5KgpKVeri1rrjUxNhzaZV-XRMLfMzqLm41gRlYkeFjcSiFgPKyo_YL_BcP5NH9Zy11XTheiqhKmORi4VsEewQWWV-tiCsJRTn5JKnfs6h-EQ7UQmt584BWeJOa-4ouU3RnJLd9iQAOElFiLvwat1W-PVLMSdwmKTG_gVj0iDCXXDXHCc0Sn1iTJM6Y5F5OST28kXsSDrQzyaoD0HTdKeVEoguRjAgr5lOcw1W6PfE5akm0o27R73hNlJP5R4U-Z0Z6wd1GpZ_aXc7mgh3W7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf93b046.mp4?token=P2OQM9RAP4Nh2jw021AJPETMeA-JNVljN9FNqkd8SaRmlJuxES20zwg4YnFaef0WG5KgpKVeri1rrjUxNhzaZV-XRMLfMzqLm41gRlYkeFjcSiFgPKyo_YL_BcP5NH9Zy11XTheiqhKmORi4VsEewQWWV-tiCsJRTn5JKnfs6h-EQ7UQmt584BWeJOa-4ouU3RnJLd9iQAOElFiLvwat1W-PVLMSdwmKTG_gVj0iDCXXDXHCc0Sn1iTJM6Y5F5OST28kXsSDrQzyaoD0HTdKeVEoguRjAgr5lOcw1W6PfE5akm0o27R73hNlJP5R4U-Z0Z6wd1GpZ_aXc7mgh3W7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد امام و شهدا در شب ۱۹۶ ایستادگی مردم شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461625" target="_blank">📅 21:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73b822623.mp4?token=L0-OC0_FfuscB_p5fREgsnre78zr4yex-HibGKWIUMePUjh-dzC5eo1GLUOPZsd4gi2Zh30_CEMbL_Z65UzcFUlVGIzqZtLIggKRHrYYGKY8_aNc7XrfLglTHr-Mv3Nn7-hIwV_SXfdJAI9HvTF3HcbyHVp8MZHJ8HYJUQTCW2kBx4GwXSe3VAb-8HLacLaSaVJ5iueJEMRUfaKtX5x9L-110StH1La27ld5x5FhMjCrxDEeQYE14AsD7ls-8xfYFemaNZSW4BC3AukFS7GOEM4rVbkgkVSn0wqnaatNolgK6Gbz8TL9o_-lHLVLh0aXPuYkGiQAaPgP9otNd6H-ulQpm3GO7bsNqrqANfOGTudHArthQoAOLTuTVNXIDlUiywmH8pa_laogiv6JlDHEowhrd8_JpaFsAUZ46bl96KsYtvUYN0duKO0V4q0y3zaBtJ0piZl9N6DrxEP3LGNgN4aHdXFq7TU_20Qkn-Zs5557YN2s-qgepwl8f_XEovrfwN7qbEejlB-wxveAixRbq0cvv-QDdbeTD_F9D89T9PMlQjIHWByI6W83aBXcjaJnJdBPM-QKpa-mDSOmYCFgzhrpfZNLb5yTENSioX_JtAz-hWPewucAdx4mfpJn6Bhs7Ia23Xio95Br0lJ73Xqy-MKKUaRbdHXXi6lT9IGLT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73b822623.mp4?token=L0-OC0_FfuscB_p5fREgsnre78zr4yex-HibGKWIUMePUjh-dzC5eo1GLUOPZsd4gi2Zh30_CEMbL_Z65UzcFUlVGIzqZtLIggKRHrYYGKY8_aNc7XrfLglTHr-Mv3Nn7-hIwV_SXfdJAI9HvTF3HcbyHVp8MZHJ8HYJUQTCW2kBx4GwXSe3VAb-8HLacLaSaVJ5iueJEMRUfaKtX5x9L-110StH1La27ld5x5FhMjCrxDEeQYE14AsD7ls-8xfYFemaNZSW4BC3AukFS7GOEM4rVbkgkVSn0wqnaatNolgK6Gbz8TL9o_-lHLVLh0aXPuYkGiQAaPgP9otNd6H-ulQpm3GO7bsNqrqANfOGTudHArthQoAOLTuTVNXIDlUiywmH8pa_laogiv6JlDHEowhrd8_JpaFsAUZ46bl96KsYtvUYN0duKO0V4q0y3zaBtJ0piZl9N6DrxEP3LGNgN4aHdXFq7TU_20Qkn-Zs5557YN2s-qgepwl8f_XEovrfwN7qbEejlB-wxveAixRbq0cvv-QDdbeTD_F9D89T9PMlQjIHWByI6W83aBXcjaJnJdBPM-QKpa-mDSOmYCFgzhrpfZNLb5yTENSioX_JtAz-hWPewucAdx4mfpJn6Bhs7Ia23Xio95Br0lJ73Xqy-MKKUaRbdHXXi6lT9IGLT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی‌ها پیروزی یمن را جشن گرفتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461624" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45167d880.mp4?token=czU-EnCfmT7NEKfL2oxsi36jBhEqaWd8XGCQBny8RVdfdRxbgmhNYVBdd-Urpt2DDrF9JInTcMX6XhtEGwcRRm7yRnXDgViy3fbolApstiZED-SOpw9d3Xh5inyM7uNjGXR52pQPtFJHlkFhQsWF_asTxC96HJc2o44BKgCZ2gcHwQSwgy-TGUZMiWr-W9_sIbN_Qm2cgHj4WkQj6sFyBMLgLA9FmvcdfXcKF-d0XJ24_ZHrTd0gkZ0Xwt8uDdVW-O8W1f65avMWunDM_LBcKRAvQ7sDfIWzuQXVtmVt0myROue2HqKDlGJMA3N9grOSUOVTwhKCGG-7Xl87DUxKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45167d880.mp4?token=czU-EnCfmT7NEKfL2oxsi36jBhEqaWd8XGCQBny8RVdfdRxbgmhNYVBdd-Urpt2DDrF9JInTcMX6XhtEGwcRRm7yRnXDgViy3fbolApstiZED-SOpw9d3Xh5inyM7uNjGXR52pQPtFJHlkFhQsWF_asTxC96HJc2o44BKgCZ2gcHwQSwgy-TGUZMiWr-W9_sIbN_Qm2cgHj4WkQj6sFyBMLgLA9FmvcdfXcKF-d0XJ24_ZHrTd0gkZ0Xwt8uDdVW-O8W1f65avMWunDM_LBcKRAvQ7sDfIWzuQXVtmVt0myROue2HqKDlGJMA3N9grOSUOVTwhKCGG-7Xl87DUxKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: برای تخریب پادگان روس‌ها شکایت قضایی انجام شده و تاکید ما این است که این بنای تاریخی به همان شکل سابق بازسازی شود
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461623" target="_blank">📅 21:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b024849e91.mp4?token=USGQqln0gJ0frjMbf0BVGGhLAs3GE4PEd4JXCnurPLyi-t-QmNXEVWwReEZwjOSotW3HkdEiGPIDnSEf32VzPdqGENfd8Rfvkc2VwlS2xn2_9P9J_XN2uLKj4kVl7VhpR7xZWRh0ANFjA6l5xaPJp7UBHF90Ddv3ZAQn1YI4a7EYU0gQzGO3VdbQs2hyRNz7hoM6MSMcGBGDEgTbXEEn9UaVJbW7v6ZmqpiM2BHfYKSsqLxrT2bGbtHw3JTtTOq68Nv2_VfZiYBiIEqJyQog0_xxObv077_CoWD6OfUZ1ZNpEytqOIX9znhKNzMzgSqm7SdyEYoNK1dYUXkXiIuY8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b024849e91.mp4?token=USGQqln0gJ0frjMbf0BVGGhLAs3GE4PEd4JXCnurPLyi-t-QmNXEVWwReEZwjOSotW3HkdEiGPIDnSEf32VzPdqGENfd8Rfvkc2VwlS2xn2_9P9J_XN2uLKj4kVl7VhpR7xZWRh0ANFjA6l5xaPJp7UBHF90Ddv3ZAQn1YI4a7EYU0gQzGO3VdbQs2hyRNz7hoM6MSMcGBGDEgTbXEEn9UaVJbW7v6ZmqpiM2BHfYKSsqLxrT2bGbtHw3JTtTOq68Nv2_VfZiYBiIEqJyQog0_xxObv077_CoWD6OfUZ1ZNpEytqOIX9znhKNzMzgSqm7SdyEYoNK1dYUXkXiIuY8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدۀ «هلیا» یوزپلنگ آسیایی و توله‌هایش در حیات‌وحش خراسان‌شمالی  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461622" target="_blank">📅 21:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=RDD3qry2T8TOHkBN1yJIDODyFCjph2rz_4KCiwv4wlO2nRwmsfG68cFml2Cm-1LoTFLSmoG4AR-59VkCnoxKIBADo8P0NUfwy52XWSEYS4Ltg2dcANJDP6tZVm8DOf-9GwN7vfKN0g-Hw92k-FcTZpJDSUA1BrKNHlpMzkgcYLhyd7cO6h4H7eAN9pRSdDuB7XbMLU4v3wpqhBqaYgQF3XdZ6-5pwptO61Zbt2rMLiVDfF5GjwDOUiU5wQeGEE9NGI0_nItGlvQE3-8CLxNx3GeIZa_HwKIsbV_HTJHl0cuCkOordHH7hdHWAIsGxGQkW397MCdd2wGzas0YeUDuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=RDD3qry2T8TOHkBN1yJIDODyFCjph2rz_4KCiwv4wlO2nRwmsfG68cFml2Cm-1LoTFLSmoG4AR-59VkCnoxKIBADo8P0NUfwy52XWSEYS4Ltg2dcANJDP6tZVm8DOf-9GwN7vfKN0g-Hw92k-FcTZpJDSUA1BrKNHlpMzkgcYLhyd7cO6h4H7eAN9pRSdDuB7XbMLU4v3wpqhBqaYgQF3XdZ6-5pwptO61Zbt2rMLiVDfF5GjwDOUiU5wQeGEE9NGI0_nItGlvQE3-8CLxNx3GeIZa_HwKIsbV_HTJHl0cuCkOordHH7hdHWAIsGxGQkW397MCdd2wGzas0YeUDuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش تابستانی در ماهنشان استان زنجان سیلاب به‌راه انداخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461621" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=H37B6HZgaT2d3lilYMBothajmgzMYz3YdRRarWLn501Jue_B7YSJcu4Z-H5NJ8aLEJN8mY0Mv6Kx4LwYLVdcA6M_TbrmbIrRj7vbU3PzE0TMW74Bkp5_KdbygbozUYlVpKppKzuTpQL3aP-5kfYokMXEVnBLY4VoiTw_dHyarxenN9GAdlEaGBjDkBNLxPP_teWIroCjiX2F2kRFKFEMApcuThWnGbViD36MXzaatPJ2vWUL5zLp4oxaCmQZWaAlWquY9AX3ENVQzWsfVRdr1Vuuu_XHl7SUfU3-HKD2y5eA7p7fpPpwDHigghSGTheSWzfCbQBV5NyqKfKCYyG2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=H37B6HZgaT2d3lilYMBothajmgzMYz3YdRRarWLn501Jue_B7YSJcu4Z-H5NJ8aLEJN8mY0Mv6Kx4LwYLVdcA6M_TbrmbIrRj7vbU3PzE0TMW74Bkp5_KdbygbozUYlVpKppKzuTpQL3aP-5kfYokMXEVnBLY4VoiTw_dHyarxenN9GAdlEaGBjDkBNLxPP_teWIroCjiX2F2kRFKFEMApcuThWnGbViD36MXzaatPJ2vWUL5zLp4oxaCmQZWaAlWquY9AX3ENVQzWsfVRdr1Vuuu_XHl7SUfU3-HKD2y5eA7p7fpPpwDHigghSGTheSWzfCbQBV5NyqKfKCYyG2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوخی ۱۸+ «شفرونی» و کنسرت «شادمهر» در تهران!
🔸
در فصل جدید «پشت صحنه» گپ‌وگفتی دوستانه داشتیم درباره خبرهای ترند روز؛ مثل کنسرت شادمهر عقیلی در تهران، شوخی جنسی و توقیف «شفرونی»، فحاشی خداداد عزیزی، قیمت بنزین و تنگه هرمز و...
🔗
نسخهٔ باکیفیت را در یوتیوب…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461620" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: پیام‌هایی که سعودی‌ها برای مذاکره می‌فرستند ارزشی ندارد
🔹
رژیم سعودی چون بردۀ آمریکاست خوی پیمان‌شکنی پیدا کرده وهیچ توافقی با او ارزش ندارد.
🔹
ما تجربۀ زیادی دربارۀ مذاکره و وقت‌کشی در مذاکرات داریم.
🔹
تنها چیزی که می‌تواند…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461619" target="_blank">📅 20:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ابراهیم حاتمی‌کیا از جلسه سینماگران با حاج قاسم
🔹
حاتمی‌کیا: فیلم موسی(ع) را بعد از دیدن حاج‌قاسم قبول کردم؛ حاج قاسم سلیمانی نفس من را باز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461618" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYlDJd6vwoAgG36-udSuFfw1zyS3szdbHYo4Udwe8mmTKqEFkYPjUAL_S_pCmjqMiq3mkl58tP4G5bwPglpp0eeORkNF1gzN4uVxTy6GsQExF0the4mAQazMqWSgDDNyw2bes6XuOdaCu6Xpipd10Im8IfzQKnfKcz2-zU-AJQJfSpbLHHLby0bBNwABlUPSWk6emepfxmm2hTVo-eIzMTxvcG78A1JOl_jg2Q4EdoM8xC41_lqO6Kz5svn4AF1tFLNfqANY66hOg6iqYei64Lt5iJnxj76XLJWR_RWCMJnCKoHnDSdRcbow9GNFVPo4yl1nD338JXSduEWMYagd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۲ تن از شهدای عملیات پاکسازی یک خانه تیمی در سراوان
🔹
میثاق ثانی و مهدی سرحدی در درگیری امروز با یک تیم تروریستی در سراوان به شهادت رسیدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461617" target="_blank">📅 20:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای خسارات وارده به پالایشگاه جیزان شرکت آرامکوی عربستان در اثر حملات یمن را نشان می‌دهد  @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/461616" target="_blank">📅 20:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drd4gD5K6L3ybcfeO5u3SgBPBuaBt2JVP2EWaZlwJBdtihZxSVQgBEx-WPL8MHKi7C7Axe2toUHzYGPIkINdNX5csDPT6Zf3urCbDCeMlmzKVHG7POzvT4EL115GBwI3lSsAuPWi2Qndy_-AcMUZjAn4P0WPZZ8MDpwWjYHekkjFc5XLCK3dsEXzqEBUme6-GBqXdm9bjgTG4sJsWRhaWRKCmN7YTjUc8tdtAlWD-TPbP6ZUnc0Htti4ML9eXRFO3TiS1ba9uq1Fszd3cFoH3GLLkYlwSvnXxw5zP3CSe9L_CnF6wJ0t8bai2JJa0m_mZCAmvMgwNsO-nnm8ZpbAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461615" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: برای همۀ جبهه‌ها در یمن برنامه داریم
🔹
هر شیطنت دوبارۀ عربستان در یمن باعث تصرف جبهه‌های دیگر در یمن به دست ما می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461614" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/461613" target="_blank">📅 20:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bbpq0uPmrHUpUVgAn4LfhnNRDnmNX-0BbSyGhzkIybZvA1KXqT25PJe8bQkne1Am0isBgctJKByyEzZkbV_DtBD_R3NYmNR9skjTRtwipTl1I121QYZK_awjLARssbQ2VY7RaTwq6SpO-JOlUPziKgAd53cH6Xegb5FWZo00XXkc-gyXBaqdtub8dwsGnGdJSQoXuOvHIl3OkhmBHlyiEYkexAXRDOFj1yF9qDR2b-9StXob4p-Sfh75r93sD4pppwrzDkvyju0mQYGI93btVN4aAC_DYfLgkAA1BKKhoTFrF8rmzrpO9k5mm_-H5Fk7ei8zMR5wGhgeNt45KmTqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با…</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/461612" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس علیه ما اقدامی کند به سمت باخت می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/461611" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIJCWd40pAmvmprhTABsALsCTNfMXjisSB3dWmq8fEkFaWoOynffgTzFE28kVN0Ob6a3jhHktBdKHG9NhCVynR33Sr3Djb0paCBU-pxvGkDmIk56AJ7hL1EpujDjQMW0fMqdrqfV_pAJFQwuxncbe20nysttCdl0Am-28DY_coZQPhq6bzXj-7_Slu0llFfq4_QYztGmOm3tdZDhuqyN_44dAVh84hW05QHXUZOw7sDkS_V2T0Ix43nAA7jlR_PCbxB7m94sxYWh26btJFksClLEAIWa8_19p_YhWlCzNGidlpm_NGp7VRMy91SqKlWeewnYYaq-wjRPb8-BQSpGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6BM4C_WKJT8iALR51ZIydxcicwBonjdjEqsFBKrhS_sDD5NMYWjHPIXBRk8luWzrf6-i0lCvWSkuLGc3CJJH-KQGMLP-Mv8oLhjWeAaStuGor_woXY-RrGDR_2LXBJRdSsa53c1l0jU3vfzR1WrqEinhuYKWicGudIXkG8qbwHybsGyV10HkIj7HiqNQKA2Yh93Rr7yiJ2xHiycntG_TRHdZ_UbtpDZU4Z94TP-5aSPgCSzt7RlOPtcyl_VQS6A329cQ7rLx7piYuZUp58YPO-j-7uD2AtSDjgluxC_r7QULdLMmXP2GfBtIRVBnpyVtZN_VUAoUKcbLJmT6Wdpkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تنها یک کشتی چینی از تنگۀ هرمز عبور کرد
🔹
اکانت رهیابی‌های دریایی، منچ اوسینت می‌گوید امروز فقط نفتکش چینی لیسا با سامانۀ ردیابی روشن در حال عبور از تنگۀ هرمز دیده شده است.
🔹
ساعاتی پیش ترامپ باز هم تکرار کرده بود که «ما تنگه را کنترل می‌کنیم و مین‌های دریایی را از آن خارج کردیم».
🔸
اوایل شهریورماه یک هفته بود که ترامپ و سنتکام از مین‌روبی کامل تنگه هرمز می‌گفتند و هشتم شهریور ماه آمریکا با حمله به لارک مدعی منهدم کردن راکت‌های پرتاب مین ایران شد اما فردای همان روز سپاه پاسداران از برخورد یک نفتکش با مین در کریدور جنوبی خبر داد.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/461609" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTwnX0HgfPd2YvW2Nmz8R_RMTVMPWZ2E7O-gdU9-m_d4-shgRZANew3M04RZ55nUqbotqQWANLoia0LIqEjO6euxPo4zPyvjmn_i6pJgZ1eOwRHJB8X0pXqrdCZaZvLMQSbM9nfkCoSrI9c3gpTWWpJExfi-rabr-OAXw9q_pwoSpLUPicAQlkJMBePM3J5S1e8PjNwDRtprgVxqYgtMeTBpdcoyRDZcTcdaku1Dg-FIX1-gjj67_GF0dcfdmZr-az5AaM-6Zb0_Zwrc9fhHwgs3aeKFczkbCuquI6w6Vna1l8WbE1tkzUiGnBP8ZKLBP2nEA6Xyy90mQbAn4NYtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان صهیونیست‌ها به کمبود موشک‌های رهگیر دربرابر ایران
🔹
رئیس هیئت مدیره صنایع هوایی رژیم صهیونیستی اذعان کرد که در جنگ نامتقارن با ایران و شلیک انبوه موشک‌های بالستیک، این رژیم همواره با کمبود موشک‌های رهگیر مواجه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/461606" target="_blank">📅 19:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا خانۀ ۸ گونه گربه‌سان وحشی ایران است
🔹
از دل کویر تا دامنه‌های جنگلی شاهرود زیستگاه‌هایی گسترده شکل گرفته که یوزپلنگ ایرانی، پلنگ ایرانی،گربه پالاس، کاراکال یا سیاه‌گوش، لینکس یا همان گربه دم کوتاه، گربه وحشی، گربه جنگلی و گربه شنی را در خود جای داده‌اند.
🔹
این تنوع کم‌نظیر، شاهرود را به یکی از مهم‌ترین پناهگاه‌های گربه‌سانان کشور تبدیل کرده است اما در این میان یوزپلنگ آسیایی به دلیل وضعیت بحرانی جمعیت، جایگاه ویژه‌ای در برنامه‌های حفاظتی دارد.
🔹
این گربه‌سان چابک بیشتر در دشت‌ها و مناطق باز زندگی می‌کند و کاهش زیستگاه، کمبود طعمه و تهدیدهای انسانی، بقای آن را با چالش روبه‌رو کرده است.
🔗
برای حفاظت پایدار از این گنجینۀ زیست‌محیطی چه باید کرد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/461605" target="_blank">📅 19:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/461604" target="_blank">📅 19:43 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
