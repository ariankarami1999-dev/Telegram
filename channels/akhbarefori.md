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
<img src="https://cdn4.telesco.pe/file/O9LKj1Nmkh2fkDLMfdNxOlU_C0KkNVDgd85j-_4C_s2nLcreJANANuxd_vx-_kEb9vSA0_j4KocvTmmZJnHEB7SCxpycY_CfEFy6dtpgvcXpegT5HdnMSapQDvXVxKxa3jvqVaN0yQsrjOvalTilxbYCBMeHY7vuZLSl6iHlo9Nuo8c9-3mxTZEKetnU2I59psxegz4931VMLAHmMx-MfRy77CUNhmzy_rhmw-RNP_aW19tSVXxd9xMn57uak-uyIcr270EgNFElnIvKZ4UsP7QRdWHFdSjnSUuIX6lNIf77EySW1gJkChw6BxlM9j2_0u7u_hOwK49hIx2jWsoGaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-695511">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148e4ff4cb.mp4?token=GUipMB5gQ-qBMwIHLmIXB07PSF0ksVqnAe_vVZIqILEYITPFMfDLiCjGZJ6fNCMKThVRerGSkvkGp5YPD29isjzvb8U3QxJnQ-Akif8jKy0FqAmSDQL-8ghpvCbGvoLuQZTjca4dtR91FvLCfK9VJssA0QWAF6wErDaZ6YQZM2ThzC9pdHhFYVg2KrCKtvJ0w6gzNZNwM9B59eEC55SsxEML0F_ykfPW3hIq7coxFdWreMloQCS9JFczQKubEEzwS5Rl20XxFE69vZbCR0cXLRWI92ppaJF_KFZE3Cljx979lJi9DLiSp82l-P-9Qx7rbw-VZoh9TgVTXf1Wn5qSxC96i5gQdKvNLjjFHvAjC4Sr87hoh5I31bKwOmS4DWR6yetepIMVn91rL7r4bRCz9hCDDFp6uIoskXzKqIld3gpULectacg8owZHWExsly1d9USGuKSt_8OfdCNTOIn-K6sfPoJWqVmvCEH5b9JifuwKmQLK6S_hxS3jQP9-ed8HSL8lxWddaFw0W1LD9MRTmcMs_9OTnk7jTK7PPLo6IiwscuhzxQv1IgbpMCj5BjVWgoUWz5B_cPDoo4P7u0nN_3bBHIvAuaad5BE_2Q6M7afASmUx7vH5D7xk1Ru5w3TmVQxo3mLJB0GtzOa9urxYyvpB8ptHfMTdyuT060BKECk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148e4ff4cb.mp4?token=GUipMB5gQ-qBMwIHLmIXB07PSF0ksVqnAe_vVZIqILEYITPFMfDLiCjGZJ6fNCMKThVRerGSkvkGp5YPD29isjzvb8U3QxJnQ-Akif8jKy0FqAmSDQL-8ghpvCbGvoLuQZTjca4dtR91FvLCfK9VJssA0QWAF6wErDaZ6YQZM2ThzC9pdHhFYVg2KrCKtvJ0w6gzNZNwM9B59eEC55SsxEML0F_ykfPW3hIq7coxFdWreMloQCS9JFczQKubEEzwS5Rl20XxFE69vZbCR0cXLRWI92ppaJF_KFZE3Cljx979lJi9DLiSp82l-P-9Qx7rbw-VZoh9TgVTXf1Wn5qSxC96i5gQdKvNLjjFHvAjC4Sr87hoh5I31bKwOmS4DWR6yetepIMVn91rL7r4bRCz9hCDDFp6uIoskXzKqIld3gpULectacg8owZHWExsly1d9USGuKSt_8OfdCNTOIn-K6sfPoJWqVmvCEH5b9JifuwKmQLK6S_hxS3jQP9-ed8HSL8lxWddaFw0W1LD9MRTmcMs_9OTnk7jTK7PPLo6IiwscuhzxQv1IgbpMCj5BjVWgoUWz5B_cPDoo4P7u0nN_3bBHIvAuaad5BE_2Q6M7afASmUx7vH5D7xk1Ru5w3TmVQxo3mLJB0GtzOa9urxYyvpB8ptHfMTdyuT060BKECk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی کوچک‌زاده: به خدا اگر از جهنم نمی‌ترسیدم خودم را جلوی بانک مرکزی آتش میزدم، اینها دارند کشور را به آمریکا می‌فروشند
نماینده تهران در جلسه امروز مجلس:
🔹
چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
🔹
برای چه در اوج کمبود ارز بانک مرکزی گفته به هر بالای ۱۸ سال ۱۰ هزار دلار می‌دهد؟ اینها پول بیماران پروانه‌ای و مردم گرفتار است که در جیب سرمایه‌دارها می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/695511" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695510">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COq4BEzvAxZ4meqLlXNzAljqUPsMEYN3q5u1epexV-YdrxtsgHPfNimU0Vdypd8YteP9y_OLa54ixkikpmPcA1_tKN1JZcNkD3La19UjhEDYVBwOC12HtufJ8zcn-mhU-kFPrb4PivIEC-OinHk4DxT4K6DKQdRVJL9yn8_B5_uTIapim4KfrEOMYqktNTDsQKIXnhI81UOHKS3h66wzKi1JOdN-9_8mZvqcAhmpsCsL9rn2mP-PjnfY496HNg5qYBd6B-WDlMTsB1Vhfh1Jtj5suty1QHmoQW-GJQ157mvZ1dxUGFOQC7nmyU2x4zP1LkqEZMT1-P3bk8Xf3mRWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز یکشنبه ۱۲ مهر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/695510" target="_blank">📅 16:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695509">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=upeK5X4miYkc5-1PEOfiuC1cMhOJZUh8lCjY4wyqVEq5EllMiDhTc9Q-m00pcaNn4V3eishMIRmAy9_iBDAP8036A2KBjxqvjw7lsOwj09bPcvCYl9tgvsQB_de_pXOvo56WzT1wp38iChNTSWyOleMvuRZ68jPah8XjJ6jMIKBhD4rIW9NmsElvdumoJaduVLOjeiLLV2vcYsd6Ey6b6fjUTQzBbQMZ08qOASVAm__oawXDM_wyDHTtY4a83aS9e5EXvppxfZVrlYJ35tOryMwGOabdMnJ_tb45-Pq4qOHqQOWzEmgOaWvIkB0nn5t8gd6xPTY44xp0sCRjL2tlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=upeK5X4miYkc5-1PEOfiuC1cMhOJZUh8lCjY4wyqVEq5EllMiDhTc9Q-m00pcaNn4V3eishMIRmAy9_iBDAP8036A2KBjxqvjw7lsOwj09bPcvCYl9tgvsQB_de_pXOvo56WzT1wp38iChNTSWyOleMvuRZ68jPah8XjJ6jMIKBhD4rIW9NmsElvdumoJaduVLOjeiLLV2vcYsd6Ey6b6fjUTQzBbQMZ08qOASVAm__oawXDM_wyDHTtY4a83aS9e5EXvppxfZVrlYJ35tOryMwGOabdMnJ_tb45-Pq4qOHqQOWzEmgOaWvIkB0nn5t8gd6xPTY44xp0sCRjL2tlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
شهروند عراقی: حاضرم تمام فرزندانم را فدای جمهوری اسلامی ایران کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/695509" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695508">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اولین پرواز در مسیر مشهد - نجف پس از اعمال محدودیت‌های دولت عراق، امروز ساعت ۱۸:۴۰ انجام می‌شود
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/695508" target="_blank">📅 15:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695507">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQOgp7_Ruq-voT7tZG2m9cQADMZIhxi3q4_U2hQzhwAsEj26suQTNJlSH7cmexUSJGSCkAz37TFhRz4NSpACEtt5RHBJpXmUy2SW5bvGAB0U5bJSWlseUafl1Z2nn0eO4ISpfsA2Neld8Psszav_mPj2f4EAofwRuU3E5t82z1gQ3rR4l7JgxGWgldYmFyNl-cx6YK9p6iA_qob0Fw94rNsitmDqwJte1P1vXDphq_dFtxygw2lNf7YKNDsEmN9-4SZVoQJvkTHuEfem08kiZIKRt9DyDKjVW51JjZ0cCDORgFHZdPyhQYH3zKTkzJUsA4IhY-uToXCbDprUj4i8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: هزینه اجاره یک سوپر نفتکش برای حمل نفت از خلیج فارس به خاور دور به حدود ۱.۳ میلیون دلار در روز رسیده است
🔹
پیش از آغاز جنگ، این رقم کمتر از ۵۰ هزار دلار در روز بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/695507" target="_blank">📅 15:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695506">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24488e9f1.mp4?token=l_e-SOVTyH15QpYnkpXVJ0WpuBgdwXDJrtDs4yukm1U8mu3xgKi0Ra8WNkffqsgqNUIJdZ6ur1Sy7VcPXRcyrSbbHFLoA2uwyH2zYOCbVmUgF8CbnTYJ45aDWKhS6m95apklrmqCXrXjXTN7Z7Pu9ciccWOUGfcGvDzM3l3A2lT80O6yv_r48GJFUD-74b-JrT3cv5WZhaKhriQtBQ6N9oXAawi-qN6v7jp0NCvCfNaf9DLHIZF_R5rjcXw54fgc4OuWF8YKVwb0MjbmozoYzW5ei5yp4Om5L2xMB2Pc1csaa595YjW0kktwoF1-oj1h4446rePzezczshu7Koz9-VV0CA4X-uviKdSnrhTkxehJQ-abcbAjs53GM5yiXMIb60F_poWVal7PuMZZJCg3A5PuSNERAeux4afBRbRmOhaHCcSWuDuWq1sjELCBstaC_3JYVJZ_hodJSSdqGJkLjLhLEBEotGE7lCDu6ivmRQWkM8AcCEAh6vKg0fyAQ4Hmayo6YaP8r8IpPCthf_otqc6t9SP4QPMgks6H0E_IUYZwLQkjXMsi9VZmqa4R-DC8ZVsnwjcNdjVhl6BLUEk9OZ3GfaK1ME5GQTZBKPpDV6re_BBq8DsxOn4I34AGA_xVo9nYemmuRIxk05JLBFHTAkLDVGkAMX3cIVrWvHyy2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24488e9f1.mp4?token=l_e-SOVTyH15QpYnkpXVJ0WpuBgdwXDJrtDs4yukm1U8mu3xgKi0Ra8WNkffqsgqNUIJdZ6ur1Sy7VcPXRcyrSbbHFLoA2uwyH2zYOCbVmUgF8CbnTYJ45aDWKhS6m95apklrmqCXrXjXTN7Z7Pu9ciccWOUGfcGvDzM3l3A2lT80O6yv_r48GJFUD-74b-JrT3cv5WZhaKhriQtBQ6N9oXAawi-qN6v7jp0NCvCfNaf9DLHIZF_R5rjcXw54fgc4OuWF8YKVwb0MjbmozoYzW5ei5yp4Om5L2xMB2Pc1csaa595YjW0kktwoF1-oj1h4446rePzezczshu7Koz9-VV0CA4X-uviKdSnrhTkxehJQ-abcbAjs53GM5yiXMIb60F_poWVal7PuMZZJCg3A5PuSNERAeux4afBRbRmOhaHCcSWuDuWq1sjELCBstaC_3JYVJZ_hodJSSdqGJkLjLhLEBEotGE7lCDu6ivmRQWkM8AcCEAh6vKg0fyAQ4Hmayo6YaP8r8IpPCthf_otqc6t9SP4QPMgks6H0E_IUYZwLQkjXMsi9VZmqa4R-DC8ZVsnwjcNdjVhl6BLUEk9OZ3GfaK1ME5GQTZBKPpDV6re_BBq8DsxOn4I34AGA_xVo9nYemmuRIxk05JLBFHTAkLDVGkAMX3cIVrWvHyy2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواسمان به دریای خزر باشد!
🔹
دریای خزر فقط آب و نفت و گاز نیست، بلکه پای پول، مرز، انرژی و منافع ۵ کشور وسطه و نکته اینجاست که منابع خزر بین ۵ کشور، به طور یک اندازه، پخش نشده. حالا یک سوال، چه کسی همین الان از خزر پول در میاره؟
🔹
جزئیات را  در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/695506" target="_blank">📅 15:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695505">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b53b1e6c.mp4?token=ETZc9tg86rH2IY9tWxRkVOrhUJ1VjiCb6kvFiHkNrvSKTytk2mDpwrGNA6PK7hsA0D7QsxPfH-bBZ6tfQ4eKe4W4atzeKFs66kRzrjCGp3jtrM7mXL0sOzgfsI2qrzfeGmTB0g1u_5vduI9U5fG4GdoNI4cuVk_SZNWtQy3oqpupNbbab1c_L06YvvkFXjJvr70nn5jBgsMhoxNdAQMuPeipZ_2mf0Lne46JFuJ2oXVN36J8jLHkLjPtio8Bzj1XpnMU6UzlXk9-sgQHIvRL_54jYQTLchhXR1YA1b8GhW-Jrbn0y_Z5wpo9mmn9iaVpCdG1hKhZsXwFyJMmk2WvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b53b1e6c.mp4?token=ETZc9tg86rH2IY9tWxRkVOrhUJ1VjiCb6kvFiHkNrvSKTytk2mDpwrGNA6PK7hsA0D7QsxPfH-bBZ6tfQ4eKe4W4atzeKFs66kRzrjCGp3jtrM7mXL0sOzgfsI2qrzfeGmTB0g1u_5vduI9U5fG4GdoNI4cuVk_SZNWtQy3oqpupNbbab1c_L06YvvkFXjJvr70nn5jBgsMhoxNdAQMuPeipZ_2mf0Lne46JFuJ2oXVN36J8jLHkLjPtio8Bzj1XpnMU6UzlXk9-sgQHIvRL_54jYQTLchhXR1YA1b8GhW-Jrbn0y_Z5wpo9mmn9iaVpCdG1hKhZsXwFyJMmk2WvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهین تسلیمی: شوهرم خوشگل و شیطون بود، دخترا ولش نمیکردن
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/695505" target="_blank">📅 15:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695504">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZjYwDDF9jLuDFu4cmSvDUZHOTzwO51dnQDDIxvuXCy5iLLQPNOeboyaSRL6NfeUu6qjq3N_j7BvgVXPYb8sRYqZPRnPmaoqau39tzcrPkxo63_5eoSILH2tgThoRjUS6cgoX3XcL_VK1r8-pm6PdPFRlPGtvpNURG60eFKdvVtUvhCD5i0YVnlstv4e33PfeMR8jwWUWikliJqSiZGeigAeyPZccuywCmUBdNJtmihxNMwx_2Id8XbiXCQP8BvyRmbh74voa7zGrM0w6gANoY8LJUF2rRukvIr5msiAtP9UsZgiss6I2RRYD3Mj5VcEhE46xplozRblrqETAzSVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کاوان» در راه بورس تهران
شرکت مس کاوان نماد با نماد «کاوان»، از ۷ مهرماه ۱۴۰۵ به‌عنوان ششصد و چهل‌ودومین شرکت پذیرفته‌شده در بورس تهران، در فهرست نرخ‌های تابلو اصلی بازار دوم درج شد.
ورود «کاوان» به بورس، مسیر تازه‌ای برای تأمین مالی، توسعه پروژه‌های معدنی و صنعتی، افزایش شفافیت و تقویت حضور این مجموعه خصوصی در صنعت مس کشور ایجاد می‌کند.
سید حجت زینلی، مدیرعامل مس کاوان نماد:
مس یکی از فلزات راهبردی اقتصاد آینده جهان است و توسعه انرژی‌های تجدیدپذیر، خودروهای برقی، شبکه‌های برق و زیرساخت‌های دیجیتال، تقاضا برای این فلز را افزایش می‌دهد. ایران نیز ظرفیت بالایی در صنعت مس دارد و با توسعه اکتشاف، سرمایه‌گذاری، فناوری و فرآوری می‌تواند سهم بیشتری در اقتصاد و صادرات غیرنفتی داشته باشد.
▫️
مشروح خبر
titrtejarat.com/fa/tiny/news-11141
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/695504" target="_blank">📅 15:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695503">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سید ستار هاشمی، وزیر ارتباطات: اینترنت ماهواره‌ای جایگزین اینترنت زمینی نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/695503" target="_blank">📅 15:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695502">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=IBKo6xfRBnEBpD3fV9PZHdzVB-Qu4kf5eTTOSmubSUL72kjbS13BtfYYMnNuREDvkU5eD_l3GctFVpvbqIr4zCka5ok2bTEJ8ae-S10n-RTBIMWBizsER9W_Xb0N2cKs0jYX7L37SALLNuZ4SVQQ1mfS-wkY33YIDXa-zhuZLFDkaK8f14FAqZTHr-iS5pJ-cCLkhZMgRcXIaeqeJ3Pp9-0xxgED8O6T_KhKw0vgMrdHOxnapzXQQdk5NErTrqmGC-A35CHZno6x0-3cgkoLPcvvcfADQYPXx12h67-eTS_TTUF3YUWKlO9qTnGx0cZD1ASzaj7EQHxsKocJch7gAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=IBKo6xfRBnEBpD3fV9PZHdzVB-Qu4kf5eTTOSmubSUL72kjbS13BtfYYMnNuREDvkU5eD_l3GctFVpvbqIr4zCka5ok2bTEJ8ae-S10n-RTBIMWBizsER9W_Xb0N2cKs0jYX7L37SALLNuZ4SVQQ1mfS-wkY33YIDXa-zhuZLFDkaK8f14FAqZTHr-iS5pJ-cCLkhZMgRcXIaeqeJ3Pp9-0xxgED8O6T_KhKw0vgMrdHOxnapzXQQdk5NErTrqmGC-A35CHZno6x0-3cgkoLPcvvcfADQYPXx12h67-eTS_TTUF3YUWKlO9qTnGx0cZD1ASzaj7EQHxsKocJch7gAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه بخاطر رتبه ۳۰۰ تجربی؛ وقتی یک کنکوری رتبه دو رقمی میخواست اما رتبه ۳۰۰ کنکور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/695502" target="_blank">📅 15:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت مرغ به ثبات رسید
افضل ملکی، رئیس اتحادیه فروشندگان گوشت و مرغ در
#گفتگو
با خبرفوری:
🔹
کاهش قیمت مرغ به دلیل افزایش عرضه و رسیدن نهاده‌های مورد نیاز تولیدکنندگان است.
🔹
جوجه‌ریزی و تأمین نهاده به میزان کافی انجام شده و عرضه مرغ در بازار افزایش یافته است.
🔹
قیمت مرغ به ثبات رسیده و پیش‌بینی می‌شود برای آینده مشکلی در بازار وجود نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/695500" target="_blank">📅 15:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e758b833ff.mp4?token=rLYyDIpBQ549NTJxbdeWhWbaGojNsIzXS6GImDYyBnzyV4E74x-M1vgq4OABuks7E_fnGkDTVocYSyqdxScertgArf-vR835DSM_8tjGeocVPq1brCuRBueS2FZSHLxzLLYTu7PoGHhzKJyJGCP-rIKnX71QXCvTJzO8h7cLRZxs4A29ZKN0YKvAICbpHjT-qrtxx_AhaphOxhnBgPTZn_FJi0amMv6BIigCer78steIDsTfc2OJreJatB0lbV4vtmjtEBJ5bCM9AjtEIxJJJ7mg_v5dSZ4LPdi-_8aME9IxVQw2ksEWV0v8IjLG5XnNrlW3etOxGIzYsWSubh9-7i_9B1JpQdj7we31BtLqEIqe5jDb1s-j6CvLvIOMXDgohd9rbcajOakI2v5VXDZbiSQwulwu4qZGj-R7c4AMNXdk4t-4xh_NK4J6jYiwoMX6_pLXkMYrldrS4hEVUhSWFhxsl1pbte25bEFFgoJQjbPjlrijyq4XsJM7Enlua2bwiK1PawndHonhqGFmn4mK15CeY_9lW7CyuGM8fzR31uH00YXoQxzNAh3cBgchUvyduEYEo88ClwHUa8REuu8j4OQDnW6b_lyO-IlyKXl8lFcUx-7bi__tHniQK8ccscI5dnlMNhQo0DAsYjeNYPvHxPVp-aPb9wKVZbymctzg9Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e758b833ff.mp4?token=rLYyDIpBQ549NTJxbdeWhWbaGojNsIzXS6GImDYyBnzyV4E74x-M1vgq4OABuks7E_fnGkDTVocYSyqdxScertgArf-vR835DSM_8tjGeocVPq1brCuRBueS2FZSHLxzLLYTu7PoGHhzKJyJGCP-rIKnX71QXCvTJzO8h7cLRZxs4A29ZKN0YKvAICbpHjT-qrtxx_AhaphOxhnBgPTZn_FJi0amMv6BIigCer78steIDsTfc2OJreJatB0lbV4vtmjtEBJ5bCM9AjtEIxJJJ7mg_v5dSZ4LPdi-_8aME9IxVQw2ksEWV0v8IjLG5XnNrlW3etOxGIzYsWSubh9-7i_9B1JpQdj7we31BtLqEIqe5jDb1s-j6CvLvIOMXDgohd9rbcajOakI2v5VXDZbiSQwulwu4qZGj-R7c4AMNXdk4t-4xh_NK4J6jYiwoMX6_pLXkMYrldrS4hEVUhSWFhxsl1pbte25bEFFgoJQjbPjlrijyq4XsJM7Enlua2bwiK1PawndHonhqGFmn4mK15CeY_9lW7CyuGM8fzR31uH00YXoQxzNAh3cBgchUvyduEYEo88ClwHUa8REuu8j4OQDnW6b_lyO-IlyKXl8lFcUx-7bi__tHniQK8ccscI5dnlMNhQo0DAsYjeNYPvHxPVp-aPb9wKVZbymctzg9Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
چطور وسط دریا یه سکوی نفتی میسازن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/695499" target="_blank">📅 15:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695498">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جزئیات قتل عام خانوادگی در اصفهان به خاطر سگ‌های خانگی
🔹
دو خواهرزاده که پیش‌تر بر سر نگهداری سگ‌های خانگی با دایی خود درگیر شده و او را با چاقو مجروح کرده بودند، این بار با ادعای گرفتن رضایت وارد خانه او شدند و دایی، همسر و دو کودک ۶ و ۱۲ ساله‌اش را به قتل رساندند.
🔹
پس از ناپدید شدن خانواده، بستگان با مشاهده گم‌شدن یکی از فرش‌های مقابل خانه مشکوک شدند و اجساد چهار نفر را زیر زباله و آهک در پشت‌بام پیدا کردند. دو متهم ۲۹ و ۳۵ ساله بازداشت و به قتل اعتراف کردند؛ مادر آنها نیز به‌عنوان مظنون بازداشت شده است./رکنا
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/695498" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیام الیاس کردی | Payam Elyaskordi</strong></div>
<div class="tg-text">امروز یه اتفاق زیر پوستی تو بازار طلا داره میوفته
.
طلا گرمی 26,606,700 معامله میشه اما هنوز 1.8% حباب منفی داره
یعنی 468 هزارتومن زیر قیمته
یه نکته فنی بهتون بگم
، سکه‌ها حباب مثبت گرفتن تو این چند روز اما طلا 18 عیار حباب مثبت نگرفته هر وقت سکه حباب مثبت میگیره ولی طلای 18 عیار حباب نمیگیره یعنی نوسان گیرا تو بازار هستن نه سرمایه گذارها (احتمال نوسانات زیاد هست)، حواستون به بازار باشه برای دوستاتون هم که این روزها میخوان معامله کنن این پست بفرستین حواسشون باشه.
@payamelyaskordi
✅</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/695496" target="_blank">📅 15:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4eb0b1e68.mp4?token=BQNuPO3af87Mpql-PMCa1aZtNAKmO0bUIU-ts5-O6fahauPmn9VGD8K-QkXLrNH89W8ti_faiCxSJBDQBPAQvCRxh8scqBx7AkpiHF3GXhsO2HECPQKdpsWcfzbjXwT1lcrTiP989CxKpID1K7oP9JCmrGEx0M8aCevKsk0Vw7OEbxwmfV30YcBXRnJCK8MwonQWFWUiqfAHxVXzk-x3pJHUrZmXQREsn_zCRa76_L3sqCX3FTFqzwdpE2koY-mJ8GjpQB_eN_g2tTQ_p_BpMnyPa5MAr89vrQ-cX6RaBnK76Q6GB3_MEHDYDOMbUGTDhU_a1mnnLNTrQnQfclLbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4eb0b1e68.mp4?token=BQNuPO3af87Mpql-PMCa1aZtNAKmO0bUIU-ts5-O6fahauPmn9VGD8K-QkXLrNH89W8ti_faiCxSJBDQBPAQvCRxh8scqBx7AkpiHF3GXhsO2HECPQKdpsWcfzbjXwT1lcrTiP989CxKpID1K7oP9JCmrGEx0M8aCevKsk0Vw7OEbxwmfV30YcBXRnJCK8MwonQWFWUiqfAHxVXzk-x3pJHUrZmXQREsn_zCRa76_L3sqCX3FTFqzwdpE2koY-mJ8GjpQB_eN_g2tTQ_p_BpMnyPa5MAr89vrQ-cX6RaBnK76Q6GB3_MEHDYDOMbUGTDhU_a1mnnLNTrQnQfclLbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا شیشه‌های امروزی با شیشه‌های نوستالژی قدیمی فرق دارند؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/695494" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbae2c93ef.mp4?token=K8gUonmLm0UqIU1Be3aQbPQD1CxDqcRn8HrcZILZVmMHwTnZZ7Id12YfPKJz8NSsIE-kZGv2pR8XxrkBmZPj20icUN4_LuRqWK4cImbLUNzGZfT7tho8l8SVfmqRHqPDsWsOOJ-T3v6yTeULW9uge6FsALfT0OYlZ62SvoWbdQzHwSBcE7VRvOVDdPrROQx1SrgNrKNXqO81DXarbfkDtnFkM_jSQhxmCYB9jaDlxSpOCdI8wr1rvkxgwqUwepePLY4QDL024aNOKq0ixQJ6COgTq4rcDXmtZJJBIZm7uY5E367rmOAM0aVxY5jIao8wIHgO2Iw6FVjtKVXcDCUcJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbae2c93ef.mp4?token=K8gUonmLm0UqIU1Be3aQbPQD1CxDqcRn8HrcZILZVmMHwTnZZ7Id12YfPKJz8NSsIE-kZGv2pR8XxrkBmZPj20icUN4_LuRqWK4cImbLUNzGZfT7tho8l8SVfmqRHqPDsWsOOJ-T3v6yTeULW9uge6FsALfT0OYlZ62SvoWbdQzHwSBcE7VRvOVDdPrROQx1SrgNrKNXqO81DXarbfkDtnFkM_jSQhxmCYB9jaDlxSpOCdI8wr1rvkxgwqUwepePLY4QDL024aNOKq0ixQJ6COgTq4rcDXmtZJJBIZm7uY5E367rmOAM0aVxY5jIao8wIHgO2Iw6FVjtKVXcDCUcJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: استان‌های شمالی و برخی استان‌های شمال‌غرب، غرب و جنوب امروز هم شاهد بارش خواهند بود
🔹
همچنین فردا در بخش‌هایی از استان‌های گیلان، مازندران، کرمانشاه، ایلام، اصفهان، استان مرکزی و لرستان باران می‌بارد؛ موج جدید از بارش‌ها پس‌فردا وارد کشور می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/695493" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88dcc5c70.mp4?token=kk7O94o1oPbK1rATJiUOUHeWLe6Q1XC735MY6_uQ--3Ewo7AT6J_vFutXukfYDdRjxr5H33w0I_xZRO7BlHNFk7_k_qh0aQuDiahvgq3aZo-JSFu6YfqmCoty0P_By8EjHk2fXSL7IGQOcrvsmX7B8RUk2bhfdbgyFn0ZzaISnpn_n1IS4e-duRA50bPYYToVlZXPrUNOrNBcwrB6K2GFGxhNYzElbB2eljhkx6anNEQ_Zv62jyPQ3MkR2GkSEASJxLe_DjGnfSHliXOVquDBzoOQC84L8Y4QRaid9V7D0TjfzuOg_dgp-gi6SEBtYMJfgGBDkFyzWlVNqi5nICawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88dcc5c70.mp4?token=kk7O94o1oPbK1rATJiUOUHeWLe6Q1XC735MY6_uQ--3Ewo7AT6J_vFutXukfYDdRjxr5H33w0I_xZRO7BlHNFk7_k_qh0aQuDiahvgq3aZo-JSFu6YfqmCoty0P_By8EjHk2fXSL7IGQOcrvsmX7B8RUk2bhfdbgyFn0ZzaISnpn_n1IS4e-duRA50bPYYToVlZXPrUNOrNBcwrB6K2GFGxhNYzElbB2eljhkx6anNEQ_Zv62jyPQ3MkR2GkSEASJxLe_DjGnfSHliXOVquDBzoOQC84L8Y4QRaid9V7D0TjfzuOg_dgp-gi6SEBtYMJfgGBDkFyzWlVNqi5nICawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاهش اعتماد به آمریکا؛ چرا کشورهای خلیج فارس به سمت چین می‌روند؟
آلن گرش، روزنامه‌نگار فرانسوی و تحلیلگر مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
کاهش اعتماد به تضمین‌های امنیتی آمریکا، کشورهای منطقه را به سمت ایجاد روابط گسترده‌تر با چین و دیگر قدرت‌ها سوق داده است؛ اما خروج کامل از مدار واشینگتن همچنان دشوار است. جهان در میانه یک دوره گذار ژئوپلیتیکی قرار دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695491" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUVwj7eW9k7q0_i-Y2_JZyexcQKsgbCm1b04dvnyQPJlXoMzCt1oUNUMlAk94J06UeGBmTSFeaIvui_Vmbsfj7egiW8c6prcsJyVaD3NdD8MuXzDRrbo6uYe6xIsOjpuTP4xeadCgu2g1Cwh4H9GGQPzATzfJ3MD4M0ALj5c8SD4Xz56Bm5GsezhnKiWuc9h6R70Nl9T11ehHwcpGxW7ngMiUyF9s8EoL_viYaqppKDXLVR-8J0ANY3maJL9UokLVEJRocsUUM4feUlqMX3JgetqxgLfsGcu_3LgPir0lon_DuhSkValsGIBfrZFJ1GKtRAga9dxpCAanYcjiEyoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/695490" target="_blank">📅 15:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in7fnOUl3XLWtoPIO11_qUJGsG6o5DpjiZdK9Vg7dRBsFRXokDK8BvCMcSTvzC1SC86XKUJMpjaIyCUm_vSSp19j0gWl8j1mpguh-PjewBxW5oc8KecVLF_mo168gTut7ttGeYUGRDiz-Gz-HgQ8FyzX50qws_1pa7dDntI2EE4D5CCEmSNXqj3nLiHHwQnzqKfhNWQiF_7mDCz3aqfI6xpnoP8sVkW_I7gp1qG0E_8W0-j0U7ADifFU1r5L_DlVcT_pQ45U0N4DDZfzdmPS4MBaBlQZZfXEu7hCgqF-SsqwrOuZjbTrHLPs0wd6cXArS_sYFIe3oIvAfxmIF-nRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی از آسمان غبار آلود شهر بافق، لحظاتی پیش
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695489" target="_blank">📅 14:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd93505e25.mp4?token=WREekaGl5F7AZibv2UtweNWj9m_Mt_S7rHjkuwbHpD0m9JmUEqNtCjxBu8En0VLe09gSjjFJ3xGkxTumGKb1JXMtxsFQBdqjyefK02yDfY2B7_bBEnIVeQ3F0kNuYaZFIzVxBjW65X1Lcwe1fT0eOH37fiYVLPjjpmiBboXsVN14fEHKsqNctqWdeYnj44O7Qd9Gdp3GzJGZaaWIDm41liRK7qLTEdhFA7JIsRICSwdqcpO_A6eJAd_SRwPPaRptfYy-2yq5b8HyMZCQNLbCf5GY5wdlimiiRabCPUr9NGH8tfYjLtnNhLnR17a40sF5H20dmjbBgiBKBfpzeIv-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd93505e25.mp4?token=WREekaGl5F7AZibv2UtweNWj9m_Mt_S7rHjkuwbHpD0m9JmUEqNtCjxBu8En0VLe09gSjjFJ3xGkxTumGKb1JXMtxsFQBdqjyefK02yDfY2B7_bBEnIVeQ3F0kNuYaZFIzVxBjW65X1Lcwe1fT0eOH37fiYVLPjjpmiBboXsVN14fEHKsqNctqWdeYnj44O7Qd9Gdp3GzJGZaaWIDm41liRK7qLTEdhFA7JIsRICSwdqcpO_A6eJAd_SRwPPaRptfYy-2yq5b8HyMZCQNLbCf5GY5wdlimiiRabCPUr9NGH8tfYjLtnNhLnR17a40sF5H20dmjbBgiBKBfpzeIv-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین زمان آبیاری گلها و گیاهان را بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695488" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9ORT01id1rZHVQkIPSpH72URim9r06aV0GrKdxeKNaZV2CwaDiwJc_dAvDRjvM2N_6ZEu0P4XQkrski0WNbCVb0m-Dh6aQV1NQlTbHSc7c58gItkOH8PYjKcM4sVscElzSZr5RKE4i4hdnfMaE59Df6j3TdleF4Oqze21bEmwhwMmCyY8tnuO99jLiHffTFD5iKQJUfxEp3Tk0QGHg5Ur2aWLuIYzRuXYvrLYvE2kg1QlX53MsOLqqcHhYeNuwHz62d1spR76YRLXblmh_1a5xqeETIsPJu6eACelRyVBhDGq4Uu0C5De4UGE37GhRAsUEzRhj4hmUd027uT00j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وبینار "
راهکارهای حفظ سرمایه در برابر تورم؛ مقایسه فرصت‌های سرمایه‌گذاری
"
در
شرایط تورمی
امروز، یکی از مهم‌ترین پرسش‌ها این است که برای
حفظ ارزش سرمایه
کدام گزینه مناسب‌تر است؛
طلا، دلار، بورس یا مسکن؟
در این وبینار با حضور
پوریا بختیاری، پژوهشگر اقتصادی، بنیان‌گذار و روایتگر پادکست اکوتوپیا
، وضعیت اقتصاد ایران و جهان و مهم‌ترین متغیرهای اثرگذار بر بازارهای سرمایه‌گذاری را بررسی می‌کنیم تا تصویر روشن‌تری از
فرصت‌ها و ریسک‌های پیش‌رو
داشته باشیم.
🗓
۱۴ مهر ۱۴۰۵
🕖
ساعت ۲۰ تا ۲۲
مدرس: پوریا بختیاری
✅
شرکت در این وبینار رایگان است
👈
ثبت‌نام رایگان در وبینار
👉
❤️
@talasea_mag</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/695487" target="_blank">📅 14:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWGTxZbQKQxLv96BzdE-IYKLUBcraOjDnopLkNRIXlBz7WFyj20hpCjo1A9LN8WS0nC6y70T4OgmxZWLsW1dQT-S7utQ27ad-Fn6IX17TypradGovUv07Ze6UrzgjpPuCLclr92xJUU4w0tiFKA8uQpWRFU54k1EELzWJ0xIRpnpydMlkf4UuzQkkhoot-xv430t_FpruS-vWa0bqmjhklpCz-28gADF8y17ehTJTaH1-qDtduxGL4HK7JFD-A6HbYoUnhWfxInYnaNmsn6ycf7OsqvRCa71k8cmVyFBz3gUTnO1cHB_O-kyshVFbvgTkTLOExhTnNRFiqi_LVCOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین برف پاییزی بر دماوند نشست
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695486" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بیشترین گلایه مردم از پلیس به‌خاطر چیست؟
سردار عباسعلی محمدیان، فرمانده انتظامی تهران بزرگ:
🔹
غفلت، حواس پرتی و دقت نکردن به محیط اطراف و رعایت نکردن توصیه‌های پلیسی عامل اصلی بسیاری از جرایم است.
🔹
حتی همکاران ما با شهروندی که غفلت کرد و با گوشی در خیابان صحبت می‌کرد همراه شدند و گوشی را گرفتند و آخر سر به شهروند گفتند مامور هستم نگران نباشید، ولی غافل از محیط اطراف نباشید.
🔹
بیشترین گله‌مندی مردم از پلیس به‌خاطر نوع پاسخگویی و شاید همکاران ما نتوانند نظر همه را جلب کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695485" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c27a68aef.mp4?token=OBXrWcPpTVar_aNu4vhd2JzdMFyaI0t4MJMyD2__Ghia7JTpkC5oeQEVohqrpwQmAuFfdnllgLgK-Oj_MFrX8sFFQ4pUunowXjo4-TxuXSCIHR4qwcG7DWTx89DtomQUz1j8P6xcHPbQEZA--uJ7-96lSl0VrmPhka_MrDTsdfWH8wq_TiK0TglblZIIukVJscLzHDu5z9TKoaxKAxOPjDFksxyCDA3aVApsX2MKHUG0-lq-PcCpFq3hYHZpcZ2c9uSC0lh-IYyE6A5Uh5EKZIWgTSo1vGFbZloOYToTb6V23mPQQgZG7AeG7zfUy6mF-dRbS7zvMwDJEQDehljHmBJ80G7voNxhvaCKY2HSZonYzAmg9sOfTCyvullu9AVOm89PzVc0q-2Q_9AgxLF7M9WrcRVt4YmX0fT3LMntEJZRonUkP0mAtOvNBAlVoSKAO3Btw8FJ1IotrRFkgAdqx7mZ9clnpvI-jUbbqWQ41GqmiGQ0oeIsde_LA2K_E0TnvMFSKjZOJ9YGq0WsS6T5YitGTlwMVx_qnGgLQ6t4hpngFrBRnPrN9SL1NWH9ssRriyIzWdP5SKUvtyeiJhbkERyGSCm73jfj0cICK6xp3oK_YlAnb5gxvZ_TXSnm0_pHScAhbwxikZxehEuvtb0sk_7ApkOngXnJpcYP-_SJ9fY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c27a68aef.mp4?token=OBXrWcPpTVar_aNu4vhd2JzdMFyaI0t4MJMyD2__Ghia7JTpkC5oeQEVohqrpwQmAuFfdnllgLgK-Oj_MFrX8sFFQ4pUunowXjo4-TxuXSCIHR4qwcG7DWTx89DtomQUz1j8P6xcHPbQEZA--uJ7-96lSl0VrmPhka_MrDTsdfWH8wq_TiK0TglblZIIukVJscLzHDu5z9TKoaxKAxOPjDFksxyCDA3aVApsX2MKHUG0-lq-PcCpFq3hYHZpcZ2c9uSC0lh-IYyE6A5Uh5EKZIWgTSo1vGFbZloOYToTb6V23mPQQgZG7AeG7zfUy6mF-dRbS7zvMwDJEQDehljHmBJ80G7voNxhvaCKY2HSZonYzAmg9sOfTCyvullu9AVOm89PzVc0q-2Q_9AgxLF7M9WrcRVt4YmX0fT3LMntEJZRonUkP0mAtOvNBAlVoSKAO3Btw8FJ1IotrRFkgAdqx7mZ9clnpvI-jUbbqWQ41GqmiGQ0oeIsde_LA2K_E0TnvMFSKjZOJ9YGq0WsS6T5YitGTlwMVx_qnGgLQ6t4hpngFrBRnPrN9SL1NWH9ssRriyIzWdP5SKUvtyeiJhbkERyGSCm73jfj0cICK6xp3oK_YlAnb5gxvZ_TXSnm0_pHScAhbwxikZxehEuvtb0sk_7ApkOngXnJpcYP-_SJ9fY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مچ آستین لباس‌های بافتنی گشاد می‌شود، این روش به رفع آن کمک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695482" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0IaBAFYyIJ7c1Ub5uNhCXTj0DUGJ60xkf_s0j0QZTZWDP16Nk11QmvL7JrC6bG7PJSGNhOSPSCJn83F1CYj1IpMB9KGH_QpuUABoirFKdBCCXVORROoNuq0As2QLzTLoK1I3oufBU3BIVMi9NrTULNT1_H1pvI7En5U4sK6YiubA1F_z6uUJBPRMxtFdQEx4lvNihPVuo8VUu-nDsoj5T_ngDAFoeVSG844cHAIcJi558slMQ11SDelAOu1yFKuhQiB6YwtpqDH6D95L7hLwEXAlgS1EaPtvqFRfe-CUTHPItxpKIWAZlazj3cVV04ivc89c1AiwpAxNK2-ZH_BWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عرضه اسکناس دلار با کارت ملی در شعب منتخب بانک ملی ایران آغاز شد
🔹
عرضه اسکناس دلار با کارت ملی در چارچوب دستورالعمل بانک مرکزی از دیروز در شعب منتخب بانک ملی ایران آغاز شده و افراد بالای ۱۸ سال می‌توانند تا سقف
۱۰ هزار دلار
برای خرید ارز اقدام کنند.
🔹
متقاضیان علاوه بر مراجعه حضوری، می‌توانند درخواست خرید ارز را از طریق پیام‌رسان
«بله»
و بخش «خدمات» و «بازوی مدیریت بازار ارز» ثبت کنند.
🔹
ارز خریداری‌شده با نرخ فروش اسکناس در سامانه ارزی ملی (سام) محاسبه و پس از طی فرآیندهای تعیین‌شده، از شعب منتخب تحویل داده می‌شود؛ دریافت ارز در روش غیرحضوری نیز منوط به ثبت اطلاعات در سامانه «سنا» و ارائه شناسه فروش است. /
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695481" target="_blank">📅 14:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695477">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fscDeIHIagBmsP0uXgKre2xKqJ0oQ8dqkbbuSwz6jvxUiE6_61BGQlSKTR62LvYssXQrLXHsw8gjcHXOXB2JudFXL2qE9vDswfxKJ_RCDWbjwYxasiBgxleoflt7M6h4lCWlBrGDP0I_3MHEM4_sbG0YO2yLF-3fwrThK-9XQ579ewJmBaKyemHMbPawCwS5jSOLk9IymQOpmT_uqVNCoLJwPljzNi0-xfkJNmmkQPXjCkp6qR2C9sb3xgL2mgNM61zNR16AtWJ0x82OnBMfih2v6GEoLn-kMys0YG4bC21kwTMN1stqQssx74TpDlKMTgll6doADa0h0LcnuF5pVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAB27p6CEq760wJvkGKFZTWpAl6PhgmMxYCQm_U8VzPqavUAHg3ZAktl-b4MceoqBjEBVpYYJ-bS5uICK2oSf86RYbeuNnbAUKFmXHUjMHiaBC1hUK7H0woZCe_ySdFxbSMbNjKHSSyAWoh-5AkyCzfDmf04wOeSpmnzeC1qubp51jEOsP9w4EYnJNpm3WB0TZsH917ZlYIJ-jI7zqpsrEV46c0G8QwuXtVdmDM_4wRqFZr4Gvl8HpWgSm1q1wI-Xtaailh_64jUi5vyfAE6tYybLaWgGY5eDNuq-V3CqENjwgSbZJQmHriWy17E9_3LlOnPgyyuleYvZZY_DEC6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD3HquXZYkHPzVEIQDzz03LRixtw2M0obTN3dEQbrsKYiXKw_oOry_LOOXR8xNlYbUV2iPIRjow3VdSWNVqXZ4E-P9oVYqI9ipuc7qTOXd7kDSV6EGHjq0SsP_zISFLcofkNa3mcKYnBRLxLATsoHJmAc-98HhfuIwZOIb-UexzoI9kTDuK_WeIDmg71S8ujULRf5TunHEWN7HAKEFJOBdWcsPywyWoX6zHREJ2qf4geubuxJ2TDqwn6e98xZhZQywn7PbsOWPWGqkPcpaF7sX1YeeEDX86FyDm4vqRELj4RGYoNnSAxvLCWFui77gb7ROSeaneLs3QdQsNIQOKUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAzKanCR93yl8i5lY3IK3Mk3AsDgWGwkc_XTxuqCl67FIukbzORNsTT6a-BaiMphLwcl9i6EH9-W10ApW8P1DUkjMpAPXbp_AsswC6ghn1X5qF4XwWvx0d4KlUMObc5gWuv7wm0LbwtmAvRgiVZ13WgCxrb-1lMI7dTMOkRby-qFXefWjDuU33YFTBHF8dk63zfFGwTWuwZ62CWdmCFJ1VR0jV2GSw1rwFayODbbeOk9LUe-41-jmtZh4YhPdmjitJf5mn1P864_bNuGc5cht7kZHKkp7zLj-iZ-oPbyE8tx9bOBJDHdMfwscw8cbzTpsIoDeIwXuN9OFVVHlEIdxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از اینکه سال تحصیلی جدید شروع بشه، این اپلیکیشن‌ها رو بشناس
📖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695477" target="_blank">📅 14:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۹۵ درصد کالاهای آرایشی تقلبی هستند
مسعود تهرانی، نایب‌رئیس اتحادیه لوازم آرایشی و عطریات در
#گفتگو
با خبرفوری:
🔹
فروش لوازم‌آرایشی نسبت به سال گذشته حداقل ۷۰ درصد کاهش پیدا کرده و مصرف‌کنندگان به دلیل گرانی خرید خود را به حداقل رسانده‌اند.
🔹
یک محصول که در سال ۱۴۰۴ حدود یک میلیون تومان فروخته می‌شد، اکنون به حدود ۲ میلیون و ۸۰۰ هزار تومان رسیده است.
🔹
بر اساس اعلام مسئولان غذا و دارو و سازمان صمت، ۸۰ تا ۸۵ درصد خریدها کاهش یافته و همچنین حدود ۹۵ درصد کالاهای آرایشی موجود در کشور تقلبی هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/695476" target="_blank">📅 14:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
صدای انفجار در بندرخمیر مربوط به عملیات شرکت گچ خمیر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/695475" target="_blank">📅 14:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb41196e9.mp4?token=PVHbDOcpe-DBUeca1lLE1NbdNL61F43M3Y6i0n_zMY3u8Vm8XONbftWkO6QV3dNwJnSYyHRRUCWU7efNN1JPBWUcS5sOFrnM_ZoUabLISaE1umL_seq93rh7p9AXs_R9bv2rdX80EihWWm8jjWS399usoiH9e8aVeMZsyjuueGcMTWJ3i9buA39lev5PXk6FTPZrgbl_HQUh0ZjqmoxnCQidwChPhkoCcNPGmdMFLEVzpFvTca1dNfhCTSum1h2mhJ190lrciaGkyNG8j_VlX-uQxM1u1fkbnrC0gd0aNoHxUcaylqdCQyI28m9xZ_dpRsfavDRjvUTSSkfxrmRtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb41196e9.mp4?token=PVHbDOcpe-DBUeca1lLE1NbdNL61F43M3Y6i0n_zMY3u8Vm8XONbftWkO6QV3dNwJnSYyHRRUCWU7efNN1JPBWUcS5sOFrnM_ZoUabLISaE1umL_seq93rh7p9AXs_R9bv2rdX80EihWWm8jjWS399usoiH9e8aVeMZsyjuueGcMTWJ3i9buA39lev5PXk6FTPZrgbl_HQUh0ZjqmoxnCQidwChPhkoCcNPGmdMFLEVzpFvTca1dNfhCTSum1h2mhJ190lrciaGkyNG8j_VlX-uQxM1u1fkbnrC0gd0aNoHxUcaylqdCQyI28m9xZ_dpRsfavDRjvUTSSkfxrmRtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار جین، یه استایل متفاوت پاییزی داشته باش
🍂
🤎
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/695474" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-GqayUn1G8MzXfAyzhClDDs6Uhxyp4z1zuUA5zL1oFcn3HRT9sDpbVIp4DbSr52pdCgs3OMvKgnG98qzrVl1YEZ0NR4X1aK_tjv4_u5WNV_MIFaTWvzxy1UutKbfQJR1QBQyrz4Kkri4ejaR_jSJ-8ClEBteqTXuErJowuVZNbO2ev1XCpuryg_QLTN2qFCwnlvvPBSQOsxsXIH5lfiMXdT4S9ygUSM2AbXaHKl5xCWLqHFNqidmxNwhqvhU-HvUEZVtsw8n2-dy-qKGVWkjEMVuWMphfW6QCpwoxaLLwuL7lnKL0jA9pChRIm_XiBMltcel1OsRohA_3MYX5ZXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس اتحادیه طلا یا سخنگوی بازار اجرت‌بگیرها؟
🔹
شفائی، رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلا می‌گوید ورود افراد غیرمتخصص، «شأن آب‌شده‌فروشی» را زیر سؤال برده است. اما شاید مسئله چیز دیگری باشد: مردم دیگر حاضر نیستند برای خرید طلا، هزینه‌هایی بدهند که در سرمایه‌گذاری‌شان نقشی ندارد.
🔹
طلای آب‌شده، بدون اجرت ساخت، سال‌هاست انتخاب بخشی از مردم برای حفظ ارزش پول است و پلتفرم‌های آنلاین این انتخاب را ساده‌تر کرده‌اند. پس سؤال اصلی اینجاست: نکند آنچه «آسیب به شأن بازار» نامیده می‌شود، در واقع آسیب به یک مدل قدیمی درآمدی باشد؟
🔹
شفائی به‌جای اینکه توضیح دهد چرا مردم باید هزینه‌های اضافی بپردازند، از «شأن بازار» می‌گوید. سؤال ساده است: رئیس اتحادیه قرار است مدافع منافع مردم باشد یا مدافع مدلی از طلافروشی که با اجرت گرفتن معنا پیدا می‌کند؟
🔹
حالا باید پرسید: پشت این همه حمله به پلتفرم‌های آنلاین طلا، واقعاً دغدغه مردم و اعتبار بازار است یا دفاع از بازاری که مشتری‌اش را به‌تدریج از دست می‌دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/695473" target="_blank">📅 14:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا آمریکا ول‌کن تنگه هرمز نیست؟
🔹
فکر می‌کنید اگه تنگه هرمز دچار اختلال بشه، فقط قیمت نفت بالا میره؟ نه! اهمیت هرمز فقط به حجم بالای جریان انرژی محدود نمی‌‏شه، بلکه مشکل اصلی، اینه که مسیر جایگزین برای جبران کامل اختلال در تنگه هرمز وجود نداره.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/695472" target="_blank">📅 13:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35225b91.mp4?token=drnja5I4kersWeWXWzJD93-xLzgni4eEJVdT5vE_a9WfU-GF2KCEqN_EPJDoYwUTKAzedr47A1nNXtl71AwoUX5qqkdTsCNf8JxYgQ3aNIKM7niKffdHhdxblhf0jfRTP1xlUgAFbeMKGpefQxxLCDfbD4wxmeKb5DnThA-3qwSaGNIVBjeMnHKvAOp9wlfRV_tq0tTz6vD0-AF2TsIIf4XDihtSdQWCbZJM6cOPAI3bLvxLvC-YjEKIYE92CuRcq9HEulyppnp1hD8UNvwiBGQmkG2UdlQg4XPGKyMU5OG2ESQRVOU4_N7STw-n8RpsBRJGKCQ7yt25FfR9aXnHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35225b91.mp4?token=drnja5I4kersWeWXWzJD93-xLzgni4eEJVdT5vE_a9WfU-GF2KCEqN_EPJDoYwUTKAzedr47A1nNXtl71AwoUX5qqkdTsCNf8JxYgQ3aNIKM7niKffdHhdxblhf0jfRTP1xlUgAFbeMKGpefQxxLCDfbD4wxmeKb5DnThA-3qwSaGNIVBjeMnHKvAOp9wlfRV_tq0tTz6vD0-AF2TsIIf4XDihtSdQWCbZJM6cOPAI3bLvxLvC-YjEKIYE92CuRcq9HEulyppnp1hD8UNvwiBGQmkG2UdlQg4XPGKyMU5OG2ESQRVOU4_N7STw-n8RpsBRJGKCQ7yt25FfR9aXnHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهین تسلیمی: تمام اتفاقاتی که داره میوفته بخاطر آخر الزمانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/695470" target="_blank">📅 13:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تیم ملی المپیاد نجوم و اخترفیزیک ایران با کسب ۵ مدال طلا، برای سومین سال پیاپی قهرمان جهان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/695469" target="_blank">📅 13:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXI3rD9JUk-NEaCMK02u75TB0FsV4cEt-fJf-a5yBp-MX8tmZ2fZ2i4QpENGnqmKOimf0P8CrMyaBet_M7qH48_NTFUHD1hAdEFRbX4o6TBVexiMnD_gkuXlZj3jzE59xHnRCcSd4jEY89fHSUmveIZJPY10JZADJk2VSAJnd-hwRZSbIvBaY3VZ4sZaCh9fKxtEBOF4bO-GvR_viGIFraA9S4O2w8bxnsg5wE8_TiTmr273ozydN1sqJCHm3lWd5SoKZM6mmW4P_fZXE0yLaPtlCqxZsdbbqBR7viEa6zpIwU1mpIZP8K4IinAohyKzXtjqlcOwIM2Pwy-NqX-LUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ سکه، طلا و دلار امروز/ دلار وارد کانال ۲۷۰ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/695468" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPS8fTxfjEFYTnEQJxeINqlmtO8D3psgN4ACDsT9jGRdVijtWwNSht68SzSF3bOXDM05YTFaNz58lPwC8iXuIHFj3RjEYuo0x9U7MPg5OlzEGB4theB-4hFJHwTa2l5sFRPM34PPBlRVWoSaxxwf2cM_Jzt9cVlXazRTka0YJmy6fyejRj6gpfk2Yt9JzuM_FMdp4pVG-FQ70h1ipVmRowvAZkLOQqGRtJiMSasJjMaP3dqc-A2RBzyWJblSdUZ0CbzD_yAi9W1vj0NfnO3exwI7yNxgrWmGwbh4aoE4mSOBO-0DGo0ywj0QEWVdqV0W-P3kPlHu2_4VDBtcF5kI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
اصلاح تدریجی به جای انتحار و انفعال، افزایش قدم‌به‌قدم ارز
⚠️
ثابت نگه‌داشتنِ طولانی‌مدت نرخ ارز، همواره
مقدمه جهش‌های بزرگ
است. سیاست تثبیت با ایجاد شکاف میان نرخ رسمی و آزاد،
تقاضای ارز را به‌شدت افزایش
داده و دارندگان آن را برای عرضه در بازار رسمی بی‌رغبت می‌کند.
📉
در نتیجه، بانک مرکزی ناچار است ذخایر خود را برای
حفظ قیمتِ دستوری
خرج کند. اما با رسیدن این ذخایر به مرز بحرانی، سیاست‌گذار
چاره‌ای جز تحمیل شوکی شدید
به قیمت ارز رسمی و هدررفتِ سرمایه‌های ملی ندارد.
✅
درحال حاضر بانک مرکزی، در حال
تعدیل تدریجی نرخ ارز در بازار رسمی
است. این کار، بهترین راه برای پیشگیری از شوک‌های قیمتیِ ناگهانی و عبور از فضای سفته‌بازی است.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/695467" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی ارتش: در این جنگ به این نتیجه رسیدیم که حتما باید برد موشک‌هایمان‌ را ارتقا دهیم و الان به این سمت رفته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/695466" target="_blank">📅 13:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695464">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d003a8c0.mp4?token=AwBKgdpOPom6MU35sglozv_K1L81EXSZ-Tf78Z4ZW4v7YNRq2w1SZ4PPJFAzQLpB4Ur1TZfxaUrAOLhs3eAKuHkgT-ag5CTQJtRtLz-r-6NbO5KxohvymggwsHkp9qB3RI_hk_Oyy_Qf8hzqpshXiJqmYAfNt99xicDMlujPsr1NRByz6PVJiUJmBDsN9IZ_3aQfec1yq90oNRo3gFY3HltPrlCUkwNJKIOoqlB59ulF40ico9sUmj8ls5BGTa0Dav_V_hpcOyvXVgD8OgETSh8S9I1k8VwPbBcq2qXrP18qFrZlVX_0xtaz8oWm8A2vIJOS6hHtcm6vg68QZsO6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d003a8c0.mp4?token=AwBKgdpOPom6MU35sglozv_K1L81EXSZ-Tf78Z4ZW4v7YNRq2w1SZ4PPJFAzQLpB4Ur1TZfxaUrAOLhs3eAKuHkgT-ag5CTQJtRtLz-r-6NbO5KxohvymggwsHkp9qB3RI_hk_Oyy_Qf8hzqpshXiJqmYAfNt99xicDMlujPsr1NRByz6PVJiUJmBDsN9IZ_3aQfec1yq90oNRo3gFY3HltPrlCUkwNJKIOoqlB59ulF40ico9sUmj8ls5BGTa0Dav_V_hpcOyvXVgD8OgETSh8S9I1k8VwPbBcq2qXrP18qFrZlVX_0xtaz8oWm8A2vIJOS6hHtcm6vg68QZsO6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از سر دادن شعار در رواق دارالذکر و در کنار مزار رهبر شهید که در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/695464" target="_blank">📅 13:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695463">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حادثه‌ برای هواپیمای اماراتی در پرواز دبی-استانبول
🔹
حین یک پرواز شرکت هواپیمایی امارات از دبی به استانبول، ناگهان آب از سقف هواپیما سرازیر شد.
🔹
وجود این حادثه پرواز توانست پس از حدود چهار ساعت به مقصد برسد./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/695463" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آمریکا و اروپا بیشتر از ما تحت فشار هستند/کشاورزی آمریکا دچار بحران شده است
حسن قشقاوی، عضو کمیسیون امنیت ملی
مجلس در
#گفتگو
با خبرفوری:
🔹
از طریق میانجی قطری پیام هایی بین ما و آمریکا ردوبدل شد؛ همان پیشنهاد هفت روزه را دادیم. در واقع نسبت به اسلام آباد فقط پیشنهاد کاهش زمان مطرح است وگرنه هیچگونه تغییری در محتوا ایجاد نشده است.
🔹
در حال‌حاضر زمان مذاکره نیست و زمان تصمیم است. آمریکا باید اعلام کند که آیا اراده‌ای بر انجام همان ۱۴ ماده‌ای که دو رییس‌جمهور امضا کردند، وجود دارد یا خیر.
🔹
همه‌ما و جهان تحت فشار هستیم؛ اخباری که از وضع اقتصاد اروپا دارم فرایند تورم در آنجا عجیب و غریب است. از نظر زمانی به‌خاطر انتخاباتی که در آمریکا و رژیم صهیونیستی است، آنها تحت فشار بیشتری از ما هستند.
🔹
با گرانی گازوییل سیستم کشاورزی آمریکا دچار بحران شده است. ما کاهش منابع و کالاهای اساسی در ایران نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/695462" target="_blank">📅 13:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75b756a6a.mp4?token=secSSzPgdKAv4wY70-TIQuCfc1aX5a91N_bv6eTdCsO-w3bjhl1diGJzasA6nQmZYnjvfKcGeyd5KBUIlDBdd1x2Ma9KBQU5eaJCqML1Pz8TJVa3NsKYUPB2lEGOYL4zb0aoWN8GKR9HEvv7VYRICPpevKzokQ_TDimRVjuKUpMDWbO7Nhm0j8Z0iUaIoTFjUHL1yevZB9kZHSlqBp8sJeg6jhTS2C_TSJmRPsaX8m6UQic5BSxsywPM-aQoVhKd6kGdVOMtqXM3XwttZ75aTo8Jlxx7fstx6YpJTAOrr4rJTQlZY7_wW7-bHAyqgeJDMdHZDxhBSydnT0V1qNwm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75b756a6a.mp4?token=secSSzPgdKAv4wY70-TIQuCfc1aX5a91N_bv6eTdCsO-w3bjhl1diGJzasA6nQmZYnjvfKcGeyd5KBUIlDBdd1x2Ma9KBQU5eaJCqML1Pz8TJVa3NsKYUPB2lEGOYL4zb0aoWN8GKR9HEvv7VYRICPpevKzokQ_TDimRVjuKUpMDWbO7Nhm0j8Z0iUaIoTFjUHL1yevZB9kZHSlqBp8sJeg6jhTS2C_TSJmRPsaX8m6UQic5BSxsywPM-aQoVhKd6kGdVOMtqXM3XwttZ75aTo8Jlxx7fstx6YpJTAOrr4rJTQlZY7_wW7-bHAyqgeJDMdHZDxhBSydnT0V1qNwm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصرهای پاییز یه چایی متفاوت درست کن
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/695461" target="_blank">📅 13:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695460">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
مجری شبکه ۱۴ عبری: ما او (شهید خامنه‌ای) را کشتیم اما هزینه خاصی پرداخت نکردیم او که مرکز رنج ما بود، درست وسط تهران ترور شد در حالی که فکر می‌کردیم ایران کار دیوانه واری کند تنها ۴۰ روز جنگید و سپس به توقف جنگ رضایت داد. ۲ دهه ترس از پاسخ ایران در صورت ترور آیت‌الله خامنه‌ای اشتباه بود، ایران اراده لازم برای انجام کارهای دیوانه‌وار ندارد فکر می‌کردیم حداقل کاری که ایران کند خروج از NPT باشد اما این کار را نکرد به هر حال باید از نخست وزیر شجاع خود بی‌بی نتانیاهو تشکرکنیم، زیرا او بود که ریسک کرد و پیروز شد، نصرالله، خامنه ای، فرماندهان نظامی ایرانی و دانشمندان آنها را کشتیم و پاسخ تنها چند موشک بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/695460" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e7a2bd39.mp4?token=RnzZwCGAw-mY6VUIqTATRRt2iXO1ukR_6Tmw31Y0OQrJIdWjzzbh1x6q871SksEeKeEJHLznzKp5MBCOQ8NEcb3LBoeV0NJy2IpERE3VJs42gtClC5wivGginAIsZyN6QruUz9PY3EvUob4mR4A2qkhvPhMsmDK_-52amQhf9MNnsh11FwG6HSbEzh-4YzhlDn8hnRIYKlSY2HWJCha-Y6TSjsHc8iavp-5-0Dv1Ia10r1E01BrD6m8bVC4SQiy-zCGbEcb46dMO6NtnbwjevcsLe8EKF5LddZsJ8c-ZZnsC3y52vYfweyvMXoXUj1pqIWtF8awxQwpkdibWFh2HogWgOQ7gSIqMbEsPmO9gvYKZfhOwUcnLQqRMv6l_r6PltTLVcQjxJeq02fwpDfKeHFlolN3xxGEo9fJnaJFNwpDOQQRSsqVA8b-WKtfZoFYaa5uZy9kiHxR_oNUn-Bv48w6Cq8w-c28n69B8HynrZOxMMmdbqLoduoE3Ynhn0xOqC_ATVV91B-MQsUFeNaGlSloYhsRMgSZ9GbaNTU-SdQE7__AkglWkpqi03IvWtew7WyV8fOPnA07_HwSbG7xrSnjV2f6hCwyZvnvdkSzzvt3zcnCeVgdxti9cmZyRHyh9pRRnbzbR_1GMoBTGwKGwlHg8cSOVJHtWZNiBcqRKDXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e7a2bd39.mp4?token=RnzZwCGAw-mY6VUIqTATRRt2iXO1ukR_6Tmw31Y0OQrJIdWjzzbh1x6q871SksEeKeEJHLznzKp5MBCOQ8NEcb3LBoeV0NJy2IpERE3VJs42gtClC5wivGginAIsZyN6QruUz9PY3EvUob4mR4A2qkhvPhMsmDK_-52amQhf9MNnsh11FwG6HSbEzh-4YzhlDn8hnRIYKlSY2HWJCha-Y6TSjsHc8iavp-5-0Dv1Ia10r1E01BrD6m8bVC4SQiy-zCGbEcb46dMO6NtnbwjevcsLe8EKF5LddZsJ8c-ZZnsC3y52vYfweyvMXoXUj1pqIWtF8awxQwpkdibWFh2HogWgOQ7gSIqMbEsPmO9gvYKZfhOwUcnLQqRMv6l_r6PltTLVcQjxJeq02fwpDfKeHFlolN3xxGEo9fJnaJFNwpDOQQRSsqVA8b-WKtfZoFYaa5uZy9kiHxR_oNUn-Bv48w6Cq8w-c28n69B8HynrZOxMMmdbqLoduoE3Ynhn0xOqC_ATVV91B-MQsUFeNaGlSloYhsRMgSZ9GbaNTU-SdQE7__AkglWkpqi03IvWtew7WyV8fOPnA07_HwSbG7xrSnjV2f6hCwyZvnvdkSzzvt3zcnCeVgdxti9cmZyRHyh9pRRnbzbR_1GMoBTGwKGwlHg8cSOVJHtWZNiBcqRKDXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به خاطر لشکرکشی‌های جدید احتمال جنگ وجود دارد/ مقابل آمریکا آمادگی کامل داریم/ شرایط به‌نفع آمریکا نیست
حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
از لشکرکشی‌های جدید بعید نیست که شاید جنگی صورت بگیرد. ترامپ و تیمش در آستانه انتخابات مطابق  نظرسنجی‌ها وضعیتشان رو به نزول است.
🔹
ممکن است ترامپ بخواهد فیلی را هوا کند و طی ده تا بیست روز باقیمانده به انتخابات فضا را برگرداند.
🔹
خارج از بحث ایران موضوع انصارالله و یمن مطرح است و حلقه محاصره باب‌المندب بیشتر می‌شود؛ شرایط به نفع آمریکا نیست.
🔹
برخی تحلیلشان این است برای از بین رفتن این شرایط آمریکا می‌تواند از طریق نظامی، دیپلماتیک و یا فشار روانی و اقتصادی اقدام کند؛ ما هر سه مورد را دیده‌ایم و آب از سر ما گذشته است. ما مقابل آمریکا  کاملا آمادگی داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/695459" target="_blank">📅 13:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo3vItGgm7DluGGgvlp36k_BRk0_JgMghPZyCVvvkz2kOgYBslF2o0vsHUTKqcvb-XDETlVKvfoE_zDSI8VDmh_X4ozdU3V25L5XO2AiCrWqld6A5SqMIK1bNucvLn-WEd6yBwiOVMgm7pZnl5AmGQFKtEwgjfhs6rZp3pGsXWeN5lJpeAlORfNvgz4dFiz3mPnZO1OzgIvh__vLKYkZ--wYb_4K3iEPgb4PBvdb1xIv1aoS3WnTSsCLFKZt8E0c9SRmMms0H1AwpkW4oguiSKIpqWzTE2yiqctPxXYjCzaaf9QhjOPj69tOICBXuUSvLfRdJcabiGx9QmY2gcz-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس جنجالی از بنایی در ترکیه؛ شباهت عجیب به آرامگاه خیام در نیشابور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/695458" target="_blank">📅 12:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بقایی در پاسخ به خبرفوری: کشورهای عضو ناتو مشارکت مستقیم در تجاوز علیه ایران داشتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/695457" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/695456" target="_blank">📅 12:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695455">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d9fbe693.mp4?token=OEr6NmHY4XquZ0yYjgADxUdzOmZCQUDPRitRTD0E6iFX1vss-gDElDfVuoBKphq9d31c7EMM2N6VU6Hu5ExngWexXSmBGR7WPhWi43mH2WqKFSo1pIQMiHqIvxO7C1zAfP8skryMcRHAUNHqtZAYWtKvlx_7DnvqfEYV2q0d9JINeAI-jdDY8EPDrKOVzoIzk_DdF75B_bVfLGC66yyXn2Cw9BsldcJTBSF52sTJ4roi4PRCsLw1HuHJ7WzgH-OhijBstAVzk53EwoIYpARK4wxWp4Nlbm6LbHG_nZa1TsxTXv2wBM7EZAiQHuLZNN-xlXxnbSQ6omQzEWFQCWjbiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d9fbe693.mp4?token=OEr6NmHY4XquZ0yYjgADxUdzOmZCQUDPRitRTD0E6iFX1vss-gDElDfVuoBKphq9d31c7EMM2N6VU6Hu5ExngWexXSmBGR7WPhWi43mH2WqKFSo1pIQMiHqIvxO7C1zAfP8skryMcRHAUNHqtZAYWtKvlx_7DnvqfEYV2q0d9JINeAI-jdDY8EPDrKOVzoIzk_DdF75B_bVfLGC66yyXn2Cw9BsldcJTBSF52sTJ4roi4PRCsLw1HuHJ7WzgH-OhijBstAVzk53EwoIYpARK4wxWp4Nlbm6LbHG_nZa1TsxTXv2wBM7EZAiQHuLZNN-xlXxnbSQ6omQzEWFQCWjbiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقریبا هیچ؛ سهم مدارس دولتی از رتبه‌های برتر کنکور
🔹
تنها یک نفر از رتبه‌های اول تا سوم گروه‌های مختلف کنکور سراسری امسال در مدرسه دولتی درس خوانده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/695455" target="_blank">📅 12:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695454">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfdc8ac57.mp4?token=A0sgp3mjPZexkZmmUfIaN2kMLJzy2OMsWXAEIcLgy04KHPRuoCCiBNRYWjYrcUUa3lWCUpCRUe4JFzhUunIIieii46vzcGs_YwRnbExT5mcUbRa1sEXGIaIgxe5TMPxAFzUBxqPLyEawNbvn7UynHW0QLuHQZFL5P_gcymAtzrUUM32oKBT7j08zhfsVcmq9e9IVwERzawalz6RGWu02LVq8iDkzEmb0pfyzPJ2-8wXyOwACJzJOpCPJECIumi_4pLgeiO03rdPmKVdMzPdkqOEBdi_Du_ICs5NG7SWPzQJQpUWwhj4HwtaLqOpsaJM03oZk4mGGbAS3Jx52lQw2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfdc8ac57.mp4?token=A0sgp3mjPZexkZmmUfIaN2kMLJzy2OMsWXAEIcLgy04KHPRuoCCiBNRYWjYrcUUa3lWCUpCRUe4JFzhUunIIieii46vzcGs_YwRnbExT5mcUbRa1sEXGIaIgxe5TMPxAFzUBxqPLyEawNbvn7UynHW0QLuHQZFL5P_gcymAtzrUUM32oKBT7j08zhfsVcmq9e9IVwERzawalz6RGWu02LVq8iDkzEmb0pfyzPJ2-8wXyOwACJzJOpCPJECIumi_4pLgeiO03rdPmKVdMzPdkqOEBdi_Du_ICs5NG7SWPzQJQpUWwhj4HwtaLqOpsaJM03oZk4mGGbAS3Jx52lQw2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهرانه مهین‌ترابی بازیگر: ایرانی جماعت همیشه فکر می‌کنه مرغ همسایه غازه/ ایرانی‌ها میرن اونور ۱۶ ساعت کار میکنن ولی غر نمیزنن؛ ولی تو ایران که هستن به راحتی غر میزنن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/695454" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695453">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsHovgG3IVSVqXHUFWvJV-WqJ-9ZCrVmS8-6eBEkzi96evTba7fr2c2YC0uUnD7qGoJGY8RmNn90FTbrxBxp-hEWJCluPJV5efNHFN7dqbDwbccrlFZxL53OWMmhbntMXq7TNvK0hXDaue2QY14byYHCkf_BzcW-fQ3zF2FAzeTp6QMDr0QqIAfH-jFfpGAbWC7_tLk47lSHtyWo9ZEgTJTlyFH_yq98S2Y8zS-wA2jHBwcrOy18gcdifwZCectnxdh-CGz6deQkQeTQ1tHbFJfUVjsxADS1bMziMyJ5i9LbjJMYGaCS0om9asdSE8wHSSjdvxjl6kxsPLiQ71rStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن برهانی به جرم افترا محکوم شد
🔹
برهانی پیش‌تر درباره نحوه ورود بهادری جهرمی و برادرش به دوره دکتری و عضویت هیئت علمی، ادعاهایی مطرح کرده بود.
🔹
پس از شکایت بهادری جهرمی، دادگاه پس از بررسی و استعلام از مراجع ذی‌صلاح، اظهارات شاکی را تأیید و برهانی را…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/695453" target="_blank">📅 12:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695452">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d910a9a84.mp4?token=QsJUqV3Vj52caaXdZSeTqC-WcbwqVQzNtMwpmURhmeArS7jSgsll916A810dSkCiRxD6yFue9yk4qhVy35jKJNCYmuxUQicxdLsY8wCwbC7HWwhw9L1oyq8NBFiCCfjh-28aQmzjDaya_Lrs3GmS2PuX4hTaZkpfWWHERzQMeF0du2Vvqne0qi1tWL0llMvrfsrhOFLNFSrvblZDTliNQ6-66KledYYiiUPpTAwuR5kiaBGkVxNOPRwFY5H9DNg_oSQ_SDhTudyOFA11ODtkG73dQEw3QgoPKndpOvk_pJRF6lLwMdkkYW6HHvbl1sv_ww0woddOlHayq6V4I3-ApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d910a9a84.mp4?token=QsJUqV3Vj52caaXdZSeTqC-WcbwqVQzNtMwpmURhmeArS7jSgsll916A810dSkCiRxD6yFue9yk4qhVy35jKJNCYmuxUQicxdLsY8wCwbC7HWwhw9L1oyq8NBFiCCfjh-28aQmzjDaya_Lrs3GmS2PuX4hTaZkpfWWHERzQMeF0du2Vvqne0qi1tWL0llMvrfsrhOFLNFSrvblZDTliNQ6-66KledYYiiUPpTAwuR5kiaBGkVxNOPRwFY5H9DNg_oSQ_SDhTudyOFA11ODtkG73dQEw3QgoPKndpOvk_pJRF6lLwMdkkYW6HHvbl1sv_ww0woddOlHayq6V4I3-ApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی با اشاره به اعزام ناوهای جدید آمریکایی به منطقه: دست آمریکا نیست که به راحتی بتواند جنگی را شروع و تمام کند. تجربه نشان داده ایران با سرسختی از خود دفاع می‌کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695452" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695451">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwM7_QNrg3RlKDduf25YzdshEiv7QqCzkW7uM1hcatePPFnbZMNkBmMz_jC6xHYH-WUIEMZVEsFbG4VXYTJfxGl_N2rMrH4_JnzfO5QTiGMSH-7pHZnd9ijk6Aiao7ISWu0yx2i9M5TIzOCQVhwMIYiHJVbg0KIS0-I-mHE7uukYPOkzuY1CGIAK2Qnr2-Sr4967h2NjwjRvRMNGb5wWa9OIAJu-rqKFr9HaI0wS9Km_zm6P-7kdvd4jxLIa4bgOCEcUIaSQohK-FKqYSiEnPEVnNHZ-slzWr9TVX-WmBwIH8UlpV2UbuhwFsELungf5TAOIPB1aiVzFChonCnB9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنجلینا جولی تصاویری از «قبل و بعد» غزه منتشر کرد که ویرانی گسترده محله‌ها را نشان می‌دهد. او با استناد به آمار سازمان ملل از آسیب‌دیدن ۸۲٪ سازه‌ها و نیاز ۹۴٪ جمعیت غزه به سرپناه خبر داد، اما نامی از اسرائیل نبرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/695451" target="_blank">📅 12:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سنتکام: ناوهای هواپیمابر آمریکا همچنان در منطقه در حال عملیات هستند   فرماندهی مرکزی آمریکا:
🔹
دو ناو هواپیمابر از جمله «یواس‌اس جورج اچ. دبلیو. بوش» در منطقه به فعالیت و حضور فعال خود ادامه می‌دهند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/695449" target="_blank">📅 12:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بقایی با اشاره به اعزام ناوهای جدید آمریکایی به منطقه: دست آمریکا نیست که به راحتی بتواند جنگی را شروع و تمام کند. تجربه نشان داده ایران با سرسختی از خود دفاع می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/695447" target="_blank">📅 12:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس فراکسیون زنان مجلس: برای گواهینامه موتور زنان نیازی به قانون جدید نیست/ با اصلاح آئین‌نامه می‌توان مشکل را حل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/695446" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695445">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رئیس هیات مدیره سندیکای صنعت برق: احتمال خاموشی در زمستان به سبب کمبود گاز وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/695445" target="_blank">📅 12:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e5b6b430.mp4?token=cw_FxBdQj7WlaD8l6Im3XM7hQeIyZRg4jwgvjTXN0rAGbbWmo4x_NmPWM0N9YNbyZm4USWQEgBdOHbiIOgnNlRXAa9yPjTZthHGdYEUQAsW8tf0-0dnXgfDn2pB9tsaj6SVccWJa6JRLuxLaZHPs56-5wYKAn2jCB6GI21vpoYJ3AMB8AjrmS8SIcon1O_oHOBQEOyN9bglbMby1S9WQPoY0CNXTE7FSpeo6UUsIc1Z8pDn2B-9pbPtQhvrwLe6sFb5DkyMgsyomHlWaAMcmsOdkDvnOXwGSWTxSSUJ06XbhUV0DK3xGv3n6Febfi5Wgd87d4SXPmdpQCG45QBslOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e5b6b430.mp4?token=cw_FxBdQj7WlaD8l6Im3XM7hQeIyZRg4jwgvjTXN0rAGbbWmo4x_NmPWM0N9YNbyZm4USWQEgBdOHbiIOgnNlRXAa9yPjTZthHGdYEUQAsW8tf0-0dnXgfDn2pB9tsaj6SVccWJa6JRLuxLaZHPs56-5wYKAn2jCB6GI21vpoYJ3AMB8AjrmS8SIcon1O_oHOBQEOyN9bglbMby1S9WQPoY0CNXTE7FSpeo6UUsIc1Z8pDn2B-9pbPtQhvrwLe6sFb5DkyMgsyomHlWaAMcmsOdkDvnOXwGSWTxSSUJ06XbhUV0DK3xGv3n6Febfi5Wgd87d4SXPmdpQCG45QBslOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیروز بارش باران و تگرگ‌های بسیار درشت و غیرمعمول در دزفول، توجه‌ها را به خود جلب کرد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/695443" target="_blank">📅 12:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw1nMRNgsqrylGvW9L9MFt3UnO9Gbo9in-k855osvhfy8j5UkM_fzC2MyFnCrVKr7kZc03QjHm1ehqeBr3r-pZ6VMkT7rQLhvRfzMLREAGijA_gD3XSI9kRJWRntmi6Oe1XeZccPtuIVcm8K5MehaAF5ZIPS0RA7ML9Tme-Ar-FDndDiZIQsZezSyl38c4K4gp0tuQexsNrjxndVGQ3YsiZj6d7C_G5ZKqZlHv6K3KNnFK75OuQZtUrvAKNwe7tlLw6v0bJxmYT3n9yiAf7vkP6_K1AvHrRCW9eqSupvud4KwsK6uRQXk6Qsxb_Ko3Y3fkma64FXECHmv-S0tow5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت کوییک به عدد باورنکردنی دو میلیارد تومان نزدیک شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695441" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSs75KQLwWlLBoxLossMR88Chmass-ZlCqer355VeKL9qC_jS6ZrB8Y1QqmgVmdL9Wjvqts0dt5K5NZJ1J2sGy4-fA-FX7IdOSE5132NWFu42Z67rOEaRKH2BQB1DkdQjy9ZoNTVPSHd45v6MmjnK0JPb0931-ybDuXYJ6Ox2uZ7mDfttEMdacoOunoBYCguozZ3mJDKl1ZHaFAL-X4jxb4spatodzgDu7bHOSx3-8uhXPbwDxdSzSiooio894og7zXnMFryGqwkd6VzafrvRkI6QI9FMVlvlBoangIMggzudOBWZd637SsbEZKCnbugmOh2gbFnfdofkD0jGoprVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMKJ_oDW6CB8_yvmEpAD8sGWOH5_E4bn0Lp488SzBAheI5qHOg3Zne58Y6TL51YMhq1MPGf-vpLaoI5bcRR5JIbrJS0QUtUjrm9njJYdTnKZdTDbPoTt7jkga-zXSifJQcqXUXTQUcZSRwZP7_RDjwQG5_QhXhhZnBxWDwMSNsBxnqoomABP9TukxKFvVx6HF48zRCrbjKIFDtc2T2ZKQrllk68OPSzEppP7hN4-QAHYhm568iF8a0f1Rij-YwlH4pAknl_HXfIzoS0u1CoAzsQgUzEzA7pxEh9k8LM1UTPMkWdpKc-aEXGvDWRJr7pm3XRV7XOG0JVFY4Ao09_OFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1vrQcYo1IQOytm7F3PoQx6xdOdJ6sb3gVB9nezHC7tIaOjoDPRa6XENLoHAoetowm5KfncUbk7NlguKiaOKJBnXFlzGnJY2FmwNsFu4OoTqxVyNvWAdJoB2Uf0ONEbV0M81poD9b2HKrZ8PqkHchCy7FrUbr3pEtDytyYG1ui1LoFyMzLceZ9f9iLCLSe8soYQq7U98VfCtwK3QJ4kJHXxx97GwyW1uaXF8xv5K6AhqFVgILh2QTBK57ZJvMlXmfwcLic2D5Z8ZO1VykADkmqMdQs8umbWUoIrmpwoOpuyx87p7CdzwDIAs3batvIVO8SMcpIEJ3iTVcTtv887MVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JG-_hQGxRQIjFLj6W1hPy0LUGipq00eKftQstWUTwTGMr8f08fA6MMHxEzt5wtEbi7YuhL2uxyvZiQZFpp1xqnrpu1LEN2Xi5evak4Xq8gHJPWnDYWiNI84TruAvQ3E1eMF_CubKWhIK8oNeB7UBVK4Fac-Ct3jyBm9CppD4SHDZka8FNkFojbRDXePj2tEKLX9NTDybc-YudhUNAim72D86OV-Hoq4X_6JGNNOxj5OG_dA67H9WC5rimGRZdS4Bl3KM9AZV-WfPIAAe1rq3Zc4gB7z4bF3QC0sqgVh2K4l2WYXdouBOehC73nedBInk5UEIVTCmdU75P4WYTfN5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYSkV8_rkP4BaIUwqFhn7oGpIH8XcNq2pWOl9WSEzM80O-ZlMqTBME4M0JjUwWbk4jHXieaLB_uUngiTOJtDOrePTB1fiu2VCaFuUWLdm4sU6eYA-ZBBIV01VbZEdGuAqWW55gSegosgc2ad9-GH5FOf0jwo-nrBDrMIGfvtvEtmW4Gk7G3mQeF11dW6n58Jo2ZrZTVTB0D4wXFFkAe3n56LiTo2EdMb82wvzGkhdnlHoK0LtwOpXmaX-CYAstLlEvD-fFWe0IEBWBl7H5rMOPgqhfUkpRPrwHSnKLCJ3iTZIC1I0GvKD8a15bC-CKngWc9gL3lvTo2eveM22r7_SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گاهی رها کردن راه رسیدن به آن چیزی که می‌خواهی‌ را هموار می‌کند... #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695436" target="_blank">📅 12:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قالیباف: امروز در خصوص استیضاح وزیر کار تصمیم‌گیری می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/695435" target="_blank">📅 12:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZaU6Uv8DrnJLSwaj4nNZE7xNj5k7OuxuG6cAGqvyKVpwB6jMulrsMB1dV5d7TQLeUIZY4V7fcu_5n22tGyVfsoLmDhwBKiBwfKuTq4Lgf49ed9dLs0RjuCLUIKAK_ar3Y4-wyClaQ1EN9XRsDwcaQ1To4Hr3n45k7xG8dP12lWMNfNOVFuT9SH5M1Us-1mtCh7jYJJejeOYlx1swiPdy5MGRsMD6v2cqtY-Dte5d7XxrZ79heYHrf416XLYSKvyCfeoZWQ6Hn-HacxUMDZFi1G0sFG-AFEJ0enhX-cFNf4q1j1OLL47cGXXMMYaiI1A0C2oBO7rk8tBOSc8gwpT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
🛑
دوبلکس مدرن 4 میلیاردی
🛑
🛑
👈
منطقه ای بیا بازدید ویلا موجوده همین عکس همین قیمت
👉
❌
مالک چک داره و فوری به 4 میلیارد پول نیاز داره
❌
09393291641
09393291641
💚
روف گاردن با ویو جنگل و دریاچه
💚
200متر زمین 200 متر بنا
داخل شهرک با نگهبانی ۲۴ ساعته
دارای سند تکبرگ و کنتور اختصاصی
@vilariahi
@vilariahi
🛑
🛑
قیمت تمام شده 10 میلیارد ،،، شرایط پرداخت 4 میلیارد نقد و مابقی اقساطی بی بهره ،، معاوضه
🛑
🛑</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/695433" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCk5lh95DqnUArOckVq_5p-IIVhFKfkRAoHWgX2hWYd5aU2rfmoAYh-jz2AEXulUsDxoZsplSXMCXKCP-c0quAJi9Z0BgtJp_litdvJZ_RaxoV3MZmHxVac1_d-r8_BVg61rB99vEIJ07ylm6fmSiLbC6PXFSDA2LNEscyPQk6wqL1WAZdPwzPEvokLmpsIToDJUVaC8_KDaoxklReIfT9R7Lp7hsq5f1WQ3VD7W0GbkCDDVHr8hKSjh_LwzRj7ZgGvDlocXbaSbKah68ffFEGx3Qmpgklp0vMC5w99b4bMv_QabIvO5BfTDzgpcofppk8bWwi5JOj-bpGTq4MVjzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم و کابل، بخشی از زیرساخت زندگی و کسب‌وکار است؛ محصولی که شاید دیده نشود، اما کیفیت و عملکرد آن اهمیت دارد.
در ایوان، اعتماد از ادعا نمی‌آید؛ از کیفیت، دقت و عملکرد قابل اتکا ساخته می‌شود.
سیم و کابل ایوان؛ زیرساختی مطمئن.
استعلام قیمت
https://a1cable.com/jryn</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/695432" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بقایی با کنایه به ادعای عملکرد مستقل گروسی برای دبیرکلی سازمان ملل: بعید است چنین اتفاقی بیفتد؛ ترک عادت موجب مرض است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/695431" target="_blank">📅 12:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نخستین تصویر از کمک‌خلبان فلای‌دبی پس از مهار او منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695430" target="_blank">📅 12:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piXm1lslC1ABT7l_xrwv7OqMIv9fSNWYQxWEoq1GOysMVQOZ96-yUGhgnNdNWV5UrUrLw3oVp4JyBqwN_EOAvSS_L7yijkjd0hYNKR1asjdS4EDgsqMWWuyqwP-Ojvdr5ieqDiQakZJipjsv20NRBy4rJKsdZtfjwvzWX9lVQHiLK9GhwsVtRVFwmq5vRYWT9e-XYzuRJ9vz_71mt1GsCz2bD6BTpGz90w-MYxCU9UU8d4Hn1IJbFv7sgAjT7YLALGj7uPtdDfXdev_BoaeFlYRDnRXVdi7WuIPO0mfLtjXFxLNm-PEcgn666zEJokGthBJQSRCuM7clh_Y4Te_Q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سید عباس عراقچی به خبر دروغین اخراج دیپلمات های ایرانی؛ چنین رویکردی بیش از هر چیز نشان‌دهنده استیصال و شکست است
🔹
تمام دیپلمات‌های ایرانی که برای شرکت در نشست مجمع عمومی سازمان ملل متحد به نیویورک سفر کرده بودند، به استثنای یک نفر که زودتر از موعد بازگشت، طبق برنامه نیویورک را ترک کردند.
🔹
با این حال، افتخار کردن
به خبر کذب «اخراج» دیپلمات‌ها
، برای رئیس هر دستگاه دیپلماسی اقدامی نامناسب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/695429" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تورم یعنی چی؟
🔹
این بار به جای مسئولین از شما مردم در مورد تورم پرسیدیم، هرکسی نظر خاص خودش رو داد و جواب‌ها متفاوت بود؛ اما واقعا تورم یعنی چی؟
🔹
نظرات مردم را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/695428" target="_blank">📅 11:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e207e91f3a.mp4?token=vs-VUpBbpHW9hHDDghFcRz0LQTd1xpovTapu6s1C_irefFuKUS7ze0TOTC6r7HUqWGwrHxHwaWG8IqeH-5LMfLciQSnOlx84tiOV5wqvhGh-46METufqpeLXZ51G9HVTDU-HWby8oQZGsked7ItJej-ijjB0LR0fSqFOYa6F_CddimTLjS2bTOcYBBzZUPaOdQRgR4P1N2dnALncK1CY8gIkVIr9KFl0wiMvqkWFDx0BI1K8Q86hWnujEw3v_WwySNi47PaAfW6urVFSh3rISYbCyx3_uWfJgzeeEKTnWHdSfmZNIm9bBsLiurHE_jG0367C7P34qodQ-WpAVpTJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e207e91f3a.mp4?token=vs-VUpBbpHW9hHDDghFcRz0LQTd1xpovTapu6s1C_irefFuKUS7ze0TOTC6r7HUqWGwrHxHwaWG8IqeH-5LMfLciQSnOlx84tiOV5wqvhGh-46METufqpeLXZ51G9HVTDU-HWby8oQZGsked7ItJej-ijjB0LR0fSqFOYa6F_CddimTLjS2bTOcYBBzZUPaOdQRgR4P1N2dnALncK1CY8gIkVIr9KFl0wiMvqkWFDx0BI1K8Q86hWnujEw3v_WwySNi47PaAfW6urVFSh3rISYbCyx3_uWfJgzeeEKTnWHdSfmZNIm9bBsLiurHE_jG0367C7P34qodQ-WpAVpTJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز لپه‌های نرم و وا نرفته در قیمه؛ این فوت‌وفن ساده را بدانید
🍲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/695427" target="_blank">📅 11:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قتل مادر بر سر یک بشقاب قورمه سبزی
🔹
مردی ۳۴ ساله پس از درگیری با مادر ۵۵ ساله بر سر اختلافی مرتبط با غذای گوشتی، او را با ضربات چاقو به قتل رساند. متهم پس از حادثه مدتی در پارک چیتگر و کوه‌های غرب تهران مخفی شده بود و حدود یک ماه بعد در یک مسافرخانه در مرکز تهران شناسایی و بازداشت شد.
🔹
او در بازجویی‌ها مدعی شده سال‌ها گیاه‌خوار بوده و اختلاف‌های قدیمی خانوادگی نیز در شکل‌گیری درگیری نقش داشته است./ همشهری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695425" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf00b80493.mp4?token=gR8D-8D8x8fBv39A91zo4sTarmCQY3XzasMsYpESSUnAHfxxkcA0MhpCO-8F1fFpfCPm6qwz7eSD6CU7bNNwEougjvOHA0fAQSrIjE3LV1Pkb-6kQ89vjRLFknduFcPLu4Ha7Yft6is79xTBZsgu9qHe0YS1qdscLa_nl7JUngUmQxh-DRwQi9E8pQKCzc9xrxK73SLwRck45vEbJ3P3b4aBHDBJYTMopDH4ZMmQRgcvUgl_kM7LhgraK33U6wsar43GtwCiaY3vcjR-Y9sp_m4BvAe4MbIfb2E9sNYGWN4OWeGPT48ruTYKBiE9hB9SW62szqG3-h6R5PAeC0Qcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf00b80493.mp4?token=gR8D-8D8x8fBv39A91zo4sTarmCQY3XzasMsYpESSUnAHfxxkcA0MhpCO-8F1fFpfCPm6qwz7eSD6CU7bNNwEougjvOHA0fAQSrIjE3LV1Pkb-6kQ89vjRLFknduFcPLu4Ha7Yft6is79xTBZsgu9qHe0YS1qdscLa_nl7JUngUmQxh-DRwQi9E8pQKCzc9xrxK73SLwRck45vEbJ3P3b4aBHDBJYTMopDH4ZMmQRgcvUgl_kM7LhgraK33U6wsar43GtwCiaY3vcjR-Y9sp_m4BvAe4MbIfb2E9sNYGWN4OWeGPT48ruTYKBiE9hB9SW62szqG3-h6R5PAeC0Qcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: موضوع بازرسی آژانس از سایت‌های هسته‌ای ما در ازای رفع تحریم‌ها در گفتگوها مطرح نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/695424" target="_blank">📅 11:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بقائی: عراقچی، وزیر امورخارجه عضو کمیته ۶ نفره‌ای است که زیر نظر شورای عالی امنیت ملی فعالیت می‌کنند
🔹
کمیته ۶ نفره شورای عالی امنیت ملی پرونده مذاکرات را هدایت می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695423" target="_blank">📅 11:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62707a79ab.mp4?token=j24eZu5zjjfnraufRkIwL3Wa4UYb2ASRTXRcnIbU_06SJ2jKwPfZO5H-Z3EVn_gkc_D_zU30tRHCGCAU6w7_YkAYlCutbOE1rDIzdyVrwvDePEBnXSK_9DFsgLvMZWcHg_YF_oOGq1dZkip0cfJW9ZoU6YdK4BQFgngNKGLWlu425KGeno4teAZQ-WjWpj7LlsQinzRXbvh96U_ABfakEz59_cn9b5x0YqThl9yY5brcKmh6GPRb8Z04HhxX6nX7XbYy1YVz0Zi9UVL6vRujhXjwC27_H-hGwtKGyZuhgcVQzTnJXJK_CYiOhYBc226AlRzyC0BTSqLNSCz2xCtNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62707a79ab.mp4?token=j24eZu5zjjfnraufRkIwL3Wa4UYb2ASRTXRcnIbU_06SJ2jKwPfZO5H-Z3EVn_gkc_D_zU30tRHCGCAU6w7_YkAYlCutbOE1rDIzdyVrwvDePEBnXSK_9DFsgLvMZWcHg_YF_oOGq1dZkip0cfJW9ZoU6YdK4BQFgngNKGLWlu425KGeno4teAZQ-WjWpj7LlsQinzRXbvh96U_ABfakEz59_cn9b5x0YqThl9yY5brcKmh6GPRb8Z04HhxX6nX7XbYy1YVz0Zi9UVL6vRujhXjwC27_H-hGwtKGyZuhgcVQzTnJXJK_CYiOhYBc226AlRzyC0BTSqLNSCz2xCtNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در پاساژ خرید عسلویه
مدیرکل مدیریت بحران استانداری بوشهر:
🔹
از ساعت ۵ صبح امروز، مجتمع تجاری در شهرستان عسلویه دچار حریق شده است. بررسی‌های اولیه حاکی از آن است که اتصال سیم‌ برق عامل شروع این آتش‌سوزی بوده و شدت حریق به دلیل سرایت شعله‌ها افزایش یافته است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/695422" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بقایی سخنگوی وزارت خارجه: در حاشیه سازمان ملل با تقریباً همه کشورهای حاشیه جنوبی خلیج فارس دیدار و گفتگوهای خوبی انجام شد/ آزادی تعدادی از هموطنانمان که دیشب انجام شد برای ما ارزشمند است؛ از مقامات اماراتی تشکر می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695421" target="_blank">📅 11:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
با تصویب مجلس، دریافت هرگونه مال، وجه یا امتیاز از کارگزار بیگانه برای هزینه در انتخابات سراسری ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/695420" target="_blank">📅 11:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ee58f931.mp4?token=fsQpEYDpSxHKpWQyoGR_5nRQ-6wgQVgbOFQ5qwqO3Li1cYwGYCSkqAfWE9h6iERqs5w_0LDj6-jwIIZ64UMZQ6rIAJOks6kjUZwFCL4k6ZynsKyG30Jj-uksO3lWvyRyoJP-NmGNtP47-rATkB50iSh4a_xuew100jMQdjQGztVetYSrGAxSbkMo7jU7bcakbKhe1LwHOfFM8RLdJqK_wGF5Es1CzM8nRzpATKm9dzu0jZEXt-ftR0DzP4RJ4aLAbh1fobjUVAlm5591pyyOiTCdW080YhNFKYcqhi5dUh6bb7nB4hcwF4ggB1V0j0pvK_OdM3X5_l_8iOSSIrllMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ee58f931.mp4?token=fsQpEYDpSxHKpWQyoGR_5nRQ-6wgQVgbOFQ5qwqO3Li1cYwGYCSkqAfWE9h6iERqs5w_0LDj6-jwIIZ64UMZQ6rIAJOks6kjUZwFCL4k6ZynsKyG30Jj-uksO3lWvyRyoJP-NmGNtP47-rATkB50iSh4a_xuew100jMQdjQGztVetYSrGAxSbkMo7jU7bcakbKhe1LwHOfFM8RLdJqK_wGF5Es1CzM8nRzpATKm9dzu0jZEXt-ftR0DzP4RJ4aLAbh1fobjUVAlm5591pyyOiTCdW080YhNFKYcqhi5dUh6bb7nB4hcwF4ggB1V0j0pvK_OdM3X5_l_8iOSSIrllMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی سخنگوی وزارت خارجه: در حاشیه سازمان ملل با تقریباً همه کشورهای حاشیه جنوبی خلیج فارس دیدار و گفتگوهای خوبی انجام شد/ آزادی تعدادی از هموطنانمان که دیشب انجام شد برای ما ارزشمند است؛ از مقامات اماراتی تشکر می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/695419" target="_blank">📅 11:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حادثه دریایی در تنگه هرمز
🔹
سازمان دریانوردی انگلیس اعلام کرد یک نفتکش گزارش داده است که در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و این اصابت به موتورخانه کشتی آسیب وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695418" target="_blank">📅 11:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: کشورهای عضو، ۳۲۵ میلیون بشکه نفت را از ذخایر استراتژیک خود آزاد کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695417" target="_blank">📅 11:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عباس گودرزی سخنگوی هیئت رئیسه:
جلسات مجلس از هفته آینده در محل دائمی صحن برگزار می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/695416" target="_blank">📅 11:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFlhu5fzaFCJIiLwYQQRqcKLXIi7iR65RZAB_9cPE7jWmPyo2sBLLp9Mg1Pkt7Toy6nVKysgCy-KHURqLhVt8dbM_IlWhGfmsvHXojssVWuPkwYLTxvqpPXxxBwHLzo39LC7_818UKZieScNDHa__4UxMs99_9Ykj6Q8KwAMYXQ70Sv60nyk_oJGgbejAlGLAkZK1uE1V-ztOkxek-MxFyaZYuHa3jWhDqm9rs8EQtfGIcSIn7-g3DeAVJUMCdLGRmeYOQhuWKopFiMX29ZJjwtYbX5LeoRgQxSR8LMonvpYcYZWK4-oZ118XvPOLfr0Ai6WtdRvyAMWxZwoRIVzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2vF-0SBYO-0Hdj5m3KO36rSzFr-H7gl1TL6VzdOyae_M_PuA2W0zuURLbcxLIyRbusuREmTI2SAGf4BOD1J7sgLKXni1w6ksSocQcQhqD8u16fTWkfz91Sr_F7K2nKn4z8Aaqpksb8HJbv1AFhC_7pMOou9P7Te9PfIlqusPvUYV3D-OOdLfD3lMEp_p00lukMmTI5RqMGK6RhD6fS03xkNOlv4gf70A2NcLmKsenjJo4RrgkTLZ1TPB7aUfRZ0QWXMTXWhz78E57c3iVWF30Oz-KgzuQv_vKGkCJWnCSuz3rhrqIN8BxQAB5SvJYX6iymNooubDe-1h7renUdsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqfgtCnhh3kq4pYChiP_6joodDNWtgp9yvKNThpLEGjgE64PvcvmjgtgA7inP9JHNkk8BETDR406UyZxuFSJx4fBljzKCAIwHHou0GIbI2ltYBTpotBI3q5XtpucBnMpgIbfoIMFAKenVv1eJQXq1cZl0scvNtJUAqQSVHNwVMOLz5mxS0_cqI7ZQas4AuogVylf4CBxtZgAvAy8EF0xPG9pHSjLF49LtfcDOL0Q3PJM8ViCcnK9BPn3xxUCuEVK2JO6Do5gtPSwwgZ1wsDsq3REhTds3a39__Gqc9HjCBEHJ-SipOoY7WgqDPL3d2myai0Fyk82tNCsPbLcTda8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp744YdACpTtF8ct2mAN9P5glztkN1pkxwFGPI3zdu4II3cjVj2vBy8pXRrGP_sHLROY0Gl2uJwdHXighJX-3TCfUKM4e6xOOlBPgQg29GVMgA7zpoZVj60x1IpdM4lTZBUe4hBcD6Rg6lNfEqsgrifGpxJuPiAHcfy9ucC0rHjfzlp_UGqN1le_v-443tbI8MM2jLzq7rkxQlypZBSaWFPwQD6Psb--z6GDXOcujESBZ3ZxP63-Q0APV7iHPcoJk5LN2H-VM-_VO4u8JorWbFRN8jjomHfY0vk_t392EVZqQ-tVyp-HQBlAM7vVigwa24yzz9BcJ4YJ9pjHp8Ffzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته
🔹
این هفته بازارها چه مسیری را در پیش دارند؟
🔹
از بورس و سهام تا طلا، دلار و دیگر بازارهای سرمایه‌ای؛ کارشناسان، روند بازارها را بررسی کرده‌ و از چشم‌انداز روزهای پیش‌رو می‌گویند.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/695412" target="_blank">📅 11:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عراقچی: بیش از ۵۰۰۰ جنگنده آمریکایی برای حمله به ایران از پایگاه‌های اروپایی بلند شدند اما پیشنهاد ما به آنها برقراری گفت‌وگو با ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/695411" target="_blank">📅 11:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695406">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76063a6d36.mp4?token=hBIs-G8y7c0-cFUCGAi8UI1YjouZmGB83fEG4bJfDdYMSX-LPUGu1Cn1-TgSBb4d-MPl8gi45cjksbba6n0cTBZP1qwoT4wSF2oSyH6AG89ff8G5BvrVEMkX4KV7wGHuHsAzNS0_HmiW4VsHMvsIeWamMtnKIwDYO-_hQa3BRrvHo7yXwjDF0pcj8VJX_zGfDioXk_-zeFqtDuuowidYLtymreTl2AAV1FIkP7qcuZ5yjx3LvnPgudaNYS1rWrPs4_MoMGWClzToB1KwUJXDwvJHvv8ZWg2ZnF-prINCSJ1FRbtOFeZP2s8-kCMjZQtoNHZO6sdhf9HLO7vqSuzDsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76063a6d36.mp4?token=hBIs-G8y7c0-cFUCGAi8UI1YjouZmGB83fEG4bJfDdYMSX-LPUGu1Cn1-TgSBb4d-MPl8gi45cjksbba6n0cTBZP1qwoT4wSF2oSyH6AG89ff8G5BvrVEMkX4KV7wGHuHsAzNS0_HmiW4VsHMvsIeWamMtnKIwDYO-_hQa3BRrvHo7yXwjDF0pcj8VJX_zGfDioXk_-zeFqtDuuowidYLtymreTl2AAV1FIkP7qcuZ5yjx3LvnPgudaNYS1rWrPs4_MoMGWClzToB1KwUJXDwvJHvv8ZWg2ZnF-prINCSJ1FRbtOFeZP2s8-kCMjZQtoNHZO6sdhf9HLO7vqSuzDsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات گسترده در فرانسه به اعتصاب و تعطیلی ایستگاه‌های قطار رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/695406" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695405">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عراقچی: پاسخی کوبنده‌تر از گذشته در انتظار هرگونه شرارت و تجاوز مجدد دشمنان است/ بازگشایی تنگه هرمز به پذیرش شروط ایران و رفع محاصره مشروط شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695405" target="_blank">📅 10:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695403">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8fece29e.mp4?token=Ph3gHuEHZ54tv50g248tukSu-BKmXIYi1VcxrBN1lBd6RwXrnXGIauJgp7YlIl3DuHccogK4PAqjFJ-qnKUc9GeSlIzoCjD4mQ_HSUqj4twze44rWrErWT5S2-VWi7wOZL2ESfyC30At1k6G0Xq4eG8AHq7tuJXkBeKiPtsvpAKa_m3J3WEhGeK_q2VbX4ZU1sSGMw3xBD5AvpJP2uIYw74yJAXw_5Xo2EwR60PIpkpXo59DB624bK90SQYh9F9Wg-mxafrhPPlpqF0SAvIuIMe_Co6x5G96CjoNnZRuCOlLF6KPrMi7skUkJDTcI5UOGJOJkH4bpstOHIESTkCWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8fece29e.mp4?token=Ph3gHuEHZ54tv50g248tukSu-BKmXIYi1VcxrBN1lBd6RwXrnXGIauJgp7YlIl3DuHccogK4PAqjFJ-qnKUc9GeSlIzoCjD4mQ_HSUqj4twze44rWrErWT5S2-VWi7wOZL2ESfyC30At1k6G0Xq4eG8AHq7tuJXkBeKiPtsvpAKa_m3J3WEhGeK_q2VbX4ZU1sSGMw3xBD5AvpJP2uIYw74yJAXw_5Xo2EwR60PIpkpXo59DB624bK90SQYh9F9Wg-mxafrhPPlpqF0SAvIuIMe_Co6x5G96CjoNnZRuCOlLF6KPrMi7skUkJDTcI5UOGJOJkH4bpstOHIESTkCWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سینه‌مرغ رو تکراری نخور، یک‌بار این‌ مدلی درستدکن ببین چقدر لذیذه
😋
مواد لازم:
🔹
سینه یا فیله مرغ
🔹
اسفناج یک لیوان
🔹
شیر یک لیوان
🔹
قارچ چهار عدد
🔹
ارد جودوسر یا ارد کامل گندم یک قاشق غذاخوری
🔹
سیر
🔹
روغن زیتون یک قاشق چای‌خوری
🔹
نمک و فلفل سیاه ‌پودر سیر…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695403" target="_blank">📅 10:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695402">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
قالیباف: اصلاح اساسی وضعیت معیشت پرسنل فراجا و دیگر نیروهای مسلح یک اولویت قطعی مجلس است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/695402" target="_blank">📅 10:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695399">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49da7f30a6.mp4?token=VYSUf2sx5zs--LnVpwKOmWoAyUZQuUwbMhw1dC7g1E470bpys_-tIlAik5w0mAOoekGrGQMApg1maWmcMYct0ZyYRGEoYu0kgMaOUkkwTOSLmqonMvAU0tX1NHkOHwgpEexU4gbmDMVxReR-2GUrhFrWheNhjfPNLJb2dCETwz0oABR6MfaoynT6yNQgvZpHfus-k4FKIc5zLtfGQxG6-CFzuwCF6f85hLqulUohft7XGzwKSRPnhH85GffZ_ywEofnjFDHOWzRVv-hooeqh6kQ9SGs6KxNiCUCG67H23H0o1cASNlvph-Y9oPVQbr7fz2HU48ytqWITzP8C51-RxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49da7f30a6.mp4?token=VYSUf2sx5zs--LnVpwKOmWoAyUZQuUwbMhw1dC7g1E470bpys_-tIlAik5w0mAOoekGrGQMApg1maWmcMYct0ZyYRGEoYu0kgMaOUkkwTOSLmqonMvAU0tX1NHkOHwgpEexU4gbmDMVxReR-2GUrhFrWheNhjfPNLJb2dCETwz0oABR6MfaoynT6yNQgvZpHfus-k4FKIc5zLtfGQxG6-CFzuwCF6f85hLqulUohft7XGzwKSRPnhH85GffZ_ywEofnjFDHOWzRVv-hooeqh6kQ9SGs6KxNiCUCG67H23H0o1cASNlvph-Y9oPVQbr7fz2HU48ytqWITzP8C51-RxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مانور هایملیش؛ چند حرکت ساده برای نجات فردی که دچار خفگی شده است
🔹
در شرایط خفگی، دانستن اقدامات درست می‌تواند حیاتی باشد. مانور هایملیش یکی از روش‌های کمک به فردی است که به‌دلیل گیر کردن جسم در راه هوایی نمی‌تواند نفس بکشد؛ آموزش صحیح این مهارت می‌تواند در مواقع اضطراری بسیار کمک‌کننده باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/695399" target="_blank">📅 10:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه چهاردهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه چهاردهم؛ مسیر توحید
🔹
راه حل اساسی در بحران‌های بزرگ‌، این است که انسان با اتفاقات ترکیب نشود و فقط مشاهده‌گر حکمت الهی باشد که به جریان حق، قوت می‌بخشد و جریان باطل را آشکار می‌کند.
🔹
علت اساسی رنجش انسان، بزرگ شدن «من نفسانی» است که با قرار گرفتن او در مسیر توحید، هر روز گستره‌ی نفس کاهش می یابد.
🔹
در تفکر توحیدی، انسان همه چیز را خیر الهی می‌داند و دست از دلسوزی نسبت به خود و دیگران برمی‌دارد.
🔹
انسان در مسیر توحید، باید دائم در حال توبه و استغفار باشد و با حذف من در جایگاه روح الهی قرار گیرد.
🔹
انسان سالک باید در نور اسمای الهی زندگی کند و در جایگاه وظیفه‌محور خود در پذیرش حکم الهی قرار گیرد.
🔹
نور«الواحد» پروردگار از طریق قلب به محیط پیرامون تابش می‌کند و هر گونه بندشرک را پاره کرده و قوت توحید می بخشد.
🔹
نور مبارک «الواحد» به انسان آزادگی می آموزد و از طریق بندگی حضرت حق به وارستگی می‌رساند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/695397" target="_blank">📅 10:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695396">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بانک مرکزی: ثبت درخواست وام ازدواج و فرزندآوری رایگان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/695396" target="_blank">📅 10:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695395">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83944e4621.mp4?token=CB1VFBzPiiMUJOvcKZUUlvf56S1rwAQ8ypuGxPCiiP5PZ3obc_qM9aJM71Xbud8nClcITRTrCin2sWpeDdMLYlrFqxr_4tOq7kJVMlXRQhj1_mOBpP2_clqy7TT9fsE98W1FHmqrCZ6HFEqpOZGcgyILOmt9NhPHXEWImDZxt22dS4diZNXlSS9rOZ8pxESS_ehyJFirEwEIKgsmAVgqjWyM2K-LJJO7Ly5_KP4EUp5_DQfm8hndP0iwHPB1O2qn8Xo5t15oZ3aSR5XfcFWXbwydd0riY04XEHkNZob3kdLR9OpFWReO1sYeyii8rLYlp0ziMVIgJMeDVtSFYqTUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83944e4621.mp4?token=CB1VFBzPiiMUJOvcKZUUlvf56S1rwAQ8ypuGxPCiiP5PZ3obc_qM9aJM71Xbud8nClcITRTrCin2sWpeDdMLYlrFqxr_4tOq7kJVMlXRQhj1_mOBpP2_clqy7TT9fsE98W1FHmqrCZ6HFEqpOZGcgyILOmt9NhPHXEWImDZxt22dS4diZNXlSS9rOZ8pxESS_ehyJFirEwEIKgsmAVgqjWyM2K-LJJO7Ly5_KP4EUp5_DQfm8hndP0iwHPB1O2qn8Xo5t15oZ3aSR5XfcFWXbwydd0riY04XEHkNZob3kdLR9OpFWReO1sYeyii8rLYlp0ziMVIgJMeDVtSFYqTUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: پاسخی کوبنده‌تر از گذشته در انتظار هرگونه شرارت و تجاوز مجدد دشمنان است/ بازگشایی تنگه هرمز به پذیرش شروط ایران و رفع محاصره مشروط شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/695395" target="_blank">📅 10:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695394">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d1f7e849.mp4?token=gdMcLdjzUcIj5p027QGfFpfpJlUXjrcd8yNEER4Mybd1VbQjyTAyOY_mgf2jAiCl9lTP9THYbVKWP_g2gSw-U3wCsi4QppmSMrsMd3x3H1fMWpRqPRFWOuJu2FUefx5iIjqNuC65y9vnpdNq4rvGyek1z72arPFwMN0Jkvn0Tj8mR5qtpiJJgvxowZMlRNqxINBxRMIUGBgPseZ62nFikZw1L7he7O17zSG1LPE1bRDekWNWVFf5j5Qf03VE85PMZq1_tNKq03_f3livLi0SlSjUaWGnWvXqNkkroNa6qy6h7QgHtqQGU-H8bv5BGf-CAD43kUSNi1-tyjDseQKFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d1f7e849.mp4?token=gdMcLdjzUcIj5p027QGfFpfpJlUXjrcd8yNEER4Mybd1VbQjyTAyOY_mgf2jAiCl9lTP9THYbVKWP_g2gSw-U3wCsi4QppmSMrsMd3x3H1fMWpRqPRFWOuJu2FUefx5iIjqNuC65y9vnpdNq4rvGyek1z72arPFwMN0Jkvn0Tj8mR5qtpiJJgvxowZMlRNqxINBxRMIUGBgPseZ62nFikZw1L7he7O17zSG1LPE1bRDekWNWVFf5j5Qf03VE85PMZq1_tNKq03_f3livLi0SlSjUaWGnWvXqNkkroNa6qy6h7QgHtqQGU-H8bv5BGf-CAD43kUSNi1-tyjDseQKFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های عباس کیارستمی با پسرش بهمن که هفت تا تجدیدی آورده بود
🔹
کیارستمی‌ سازنده فیلم «مشق شب» می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/695394" target="_blank">📅 10:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3f94ab86.mp4?token=HmjvxVnPigUq_l2u0P6kSkvWTv42UDmMbOtXdJRuDrCdpLb7KroKkC0Rb2NRyksSsAekehhVctHMTlESEGoYMdgrrTE_MGkob-SP7QOEqX_oWQ49pQeSw-cR3_9hWiPPHu4w0kVmNr6_kFJqq80hJtPHqwYVowkuAfMa9DWqpJfVZMHj4wj_q3cWP0JWRSCK9p9Xkf6Ccbd5AYmUjVxpr3I80FdwfCUjwMrziF1NJWl5qlzS37UDOjgsz7zEXIFUhLJFubMO1M4ZS6zZj3NU1tcIW8opo_kFL-0RqXO5Wx6ChoDg8RJIdpVk-iGBuS4asvuweu7Eabd6FHNbAH5db43vj63BdHeZ4dm-hX7ONz3nyD-Au5bDf-nsuDJawOxS0RBaCbWavscpQ_kzEqpq2RZz0Br8d6UGO_-WB3O7Gaz_SoxOwRYTx_XrMZ1qJ0BUm2SLDFfTvJ-CkKszq6MqjmHU6uIsPWzoBy8_0Sua2TPwuA43RRLPhLwJsT0xf7ArT2lUK38IxOtMysd7QRo2EKXEUCK9nHkU2vXe2-dmKWZLxNuGkHzay4LKfi7kAsRFP-GZaaPAI8EtH8v5DH2pc2aidQXF4VmbP3Br1JBz1wdtxlW_REcHMB9yA-XX0sJK4s_sl2ubrvhSZSYQ7cd2Sp3NEVVSMj1ax7Zok4A2-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3f94ab86.mp4?token=HmjvxVnPigUq_l2u0P6kSkvWTv42UDmMbOtXdJRuDrCdpLb7KroKkC0Rb2NRyksSsAekehhVctHMTlESEGoYMdgrrTE_MGkob-SP7QOEqX_oWQ49pQeSw-cR3_9hWiPPHu4w0kVmNr6_kFJqq80hJtPHqwYVowkuAfMa9DWqpJfVZMHj4wj_q3cWP0JWRSCK9p9Xkf6Ccbd5AYmUjVxpr3I80FdwfCUjwMrziF1NJWl5qlzS37UDOjgsz7zEXIFUhLJFubMO1M4ZS6zZj3NU1tcIW8opo_kFL-0RqXO5Wx6ChoDg8RJIdpVk-iGBuS4asvuweu7Eabd6FHNbAH5db43vj63BdHeZ4dm-hX7ONz3nyD-Au5bDf-nsuDJawOxS0RBaCbWavscpQ_kzEqpq2RZz0Br8d6UGO_-WB3O7Gaz_SoxOwRYTx_XrMZ1qJ0BUm2SLDFfTvJ-CkKszq6MqjmHU6uIsPWzoBy8_0Sua2TPwuA43RRLPhLwJsT0xf7ArT2lUK38IxOtMysd7QRo2EKXEUCK9nHkU2vXe2-dmKWZLxNuGkHzay4LKfi7kAsRFP-GZaaPAI8EtH8v5DH2pc2aidQXF4VmbP3Br1JBz1wdtxlW_REcHMB9yA-XX0sJK4s_sl2ubrvhSZSYQ7cd2Sp3NEVVSMj1ax7Zok4A2-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای الجزیره: میانجی قطری مجموعه‌ای از پیشنهادها را برای نزدیک کردن مواضع دو طرف مطرح کرده است/ تهران در حال بررسی این پیشنهادها در شورای عالی امنیت ملی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/695392" target="_blank">📅 10:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04be7edc94.mp4?token=MrJBJPUHbEHVm0-5HEXI1woC6Ufm8clz_-kXKL9k--5UqnOqm2FuQMQn1XKstbT_4kTpGM69_1TpsDUSzQ8J7n34zpwkgmr9u-hFdzwfznkys03EuKjUnedTY3rVU4u9sCrNIPlbnCEcJvAKGL8u_L23QeS7waPv2ZIl-7GAHG7vGNroz2CThdtCylKaHuhOU5uKzOzyw06uJKpoxsgkNMWUJKTsa4P1VN7vHQJkWHXRs7ZYB98OYGE8EJZ02sz8r0ICr0G_8GOeKMXbT8QtDHH6QQfRpmg6e1VByPkf_rB3yUGIrVw_2XzJ8d2Og_g_2pLjfwRngHc0C7dv2tCCzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04be7edc94.mp4?token=MrJBJPUHbEHVm0-5HEXI1woC6Ufm8clz_-kXKL9k--5UqnOqm2FuQMQn1XKstbT_4kTpGM69_1TpsDUSzQ8J7n34zpwkgmr9u-hFdzwfznkys03EuKjUnedTY3rVU4u9sCrNIPlbnCEcJvAKGL8u_L23QeS7waPv2ZIl-7GAHG7vGNroz2CThdtCylKaHuhOU5uKzOzyw06uJKpoxsgkNMWUJKTsa4P1VN7vHQJkWHXRs7ZYB98OYGE8EJZ02sz8r0ICr0G_8GOeKMXbT8QtDHH6QQfRpmg6e1VByPkf_rB3yUGIrVw_2XzJ8d2Og_g_2pLjfwRngHc0C7dv2tCCzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوتاهی بانک‌ها برای پرداخت وام‌های ازدواج و فرزندآوری به بهانه تورم
بیگدلی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
سال گذشته حدود ۶۰۰ تا ۷۰۰ هزار نفر برای وام تکلیفی ازدواج و فرزندآوری در نوبت بودند.
🔹
در بودجه ۱۴۰۵ عدد برای تسویه این تعداد و پیش‌بینی نفرات جدید دیده شده است، اما بانک در بانک مرکزی نظرات مختلفی حکم فرماست.
🔹
برای عدد تسهیلات حتی با آقای همتی و مدنی‌زاده به تفاهم رسیدیم، اما عده‌ای می‌گویند این منجر به تورم می‌شود درحالی که ربطی به تورم ندارد و منجر به تولید می‌شود. متاسفانه بانک مرکزی به بهانه تورم و کمبود منابع کوتاهی می‌کند.
🔹
تعداد مراجعین و تماس‌های مردمی در این زمینه هر روز بیشتر می‌شود. فکر میکنم مجلس هم باید این موضوع را از بانک مرکزی پیگیری کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/695391" target="_blank">📅 10:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo8rCTXzSTV8Z3GrX867Qvh560jOvU4sC-mL7T-d8tjrkpdyScXnLnpNzuiBqYaWrVvuZRxBciKjUr2DHBv9d7HzLzbJGh2BgPhbhe5fi1sraBlcoFyGLZ1aCXqg-znNesD9aggZcC4K4lCxbvgHvDzKceYvLtQRcOJ7dkbyzT4RyAujGRXq2Izsxp4EHsPrhOBvX3xXJzDT97LKb3db8afdPyfpisEL5NE-FLzqNY5hr0PPeiGQtkrjQD6YQalQ7glg8mxpHVBp7bFAbTPpPufAdxLea3O672Gw0HPuemdn5Ik762e76dS8sZFU8VJws-HgMglYbBP8e7ZTRCAcOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای اولین بار در دنیا، داخل کشور هلند یک بچه ۲ ساله که دارای معلولیت بود، به طور قانونی به قتل (اتانازی) رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/695390" target="_blank">📅 09:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
بازار داغ شایعات؛ پروژه دشمن برای ایجاد انگاره ترس و تهدید
🔹
در روزهای گذشته، رسانه‌‌های معاند روند تولید و انتشار اخبار جعلی و شایعات را تشدید کرده‌اند. آن‌ها با انتشار اخبار جعلی و ادعاهای بی‌‌پشتوانه در رسانه‌‌های رسمی و کانال‌‌های پوششی خود، درصدد ساختن تصویری غیرواقعی از وضعیت کشور هستند.
🔹
هدف این عملیات، مهندسی ادراک و ایجاد انگاره تهدید، ناامنی و ترس در ذهن مردم است. وقتی یک شایعه بارها بازنشر می‌‌شود، حتی بدون ارائه سند، به‌ تدریج از یک ادعای بی‌‌اساس به یک واقعیت ذهنی تبدیل می‌‌شود؛ این همان نقطه‌ای است که عملیات شناختی دشمن اثر خود را بر جامعه می‌‌گذارد.
🔹
در این میان، برخی اظهارات ناآگاهانه، مانند ادعای ورود عناصر مسلح و استقرار آن‌ها در محلات، ناخواسته در خدمت همین سناریو قرار می‌‌گیرد و به روایت‌‌های جعلی دشمن اعتبار می‌‌بخشد.
🔹
رسانه‌ها، فعالان فضای مجازی و چهره‌‌های اثرگذار نباید به بلندگوی شایعات تبدیل شوند. هر خبر هیجانی، ادعای امنیتی یا روایت حساس، پیش از انتشار نیازمند راستی‌ آزمایی و بررسی دقیق منبع است.
🔹
مقابله با جنگ شناختی، صرفاً پاسخ دادن به شایعات نیست؛ بلکه قطع زنجیره تولید و بازنشر اخبار جعلی و جلوگیری از تثبیت آن‌‌ها در ذهن جامعه است. دقت در انتشار اخبار و مسئولیت‌‌پذیری رسانه‌ای، بخشی از پدافند شناختی جامعه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/695389" target="_blank">📅 09:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
قالیباف: تا زمانی که ۷ شرط ما براساس تفاهم‌نامۀ اسلام‌آباد، محقق نشود تنگۀ‌ هرمز باز نخواهد شد
🔹
این فقط صهیونیست ها نیستند که‌ در استیصال و درماندگی‌ گرفتار شده‌اند، آمریکایی ها نیز در مقابل ایستادگی و مقاومت ملت ایران مستاصل گشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695388" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f963fa385.mp4?token=gRgC8YeodElF2xYT-BzpOsus_WN0g888BuIqL-6z2OBRGf38N2OIRCJhHoPzIRGZNQe119-fDaK15dTq0EhZzwbz6woxDUG0MNlPREA0eqD2d7EyWdCARqZH3fZMBRruhaLbqV8Oc38WfbMWIBAmfHyNWJQ5npGOwd_lEkNCKLPqyiJF-5eOKZEB6ntDCRVMrD0yYo1QUvmTkJzvDjE2pHrhODwgEPKJ1zFMM1uSPip1T9Jl5jVdWlWxvU0Gnb9c1qZewT3EFT0DhDO1FEZb2mBsnVr5-kiBLP6JpZzN0-BXfEbIOioaMreV8xeOEfXj39VowaIwxpFRycEGtXbxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f963fa385.mp4?token=gRgC8YeodElF2xYT-BzpOsus_WN0g888BuIqL-6z2OBRGf38N2OIRCJhHoPzIRGZNQe119-fDaK15dTq0EhZzwbz6woxDUG0MNlPREA0eqD2d7EyWdCARqZH3fZMBRruhaLbqV8Oc38WfbMWIBAmfHyNWJQ5npGOwd_lEkNCKLPqyiJF-5eOKZEB6ntDCRVMrD0yYo1QUvmTkJzvDjE2pHrhODwgEPKJ1zFMM1uSPip1T9Jl5jVdWlWxvU0Gnb9c1qZewT3EFT0DhDO1FEZb2mBsnVr5-kiBLP6JpZzN0-BXfEbIOioaMreV8xeOEfXj39VowaIwxpFRycEGtXbxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام سابق وزارت ارشاد: مسئولان فکر می‌کنند باید خودشان مردم را تربیت کنند!
یاسر احمدوند، معاون سابق امور فرهنگی ارشاد:
🔹
اگر کسی در جایگاه مدیریت فرهنگی تصور کند وظیفه‌اش تربیت کردن دیگران است، دقیقاً همین‌جا کار دچار اشکال می‌شود. جامعه باید به‌صورت دسته‌جمعی و مشترک رشد کند./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/0cuD286vrzc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/695387" target="_blank">📅 09:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
قالیباف: ایران سیاست کلان و امنیت ملی‌خود را با توییت‌ها یا مصاحبه‌های روزانۀ مقامات آمریکایی تنظیم نمی‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/695386" target="_blank">📅 09:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/695385" target="_blank">📅 09:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/695384" target="_blank">📅 09:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca433618ee.mp4?token=YNzDd7i5Jxc7aRWVVzhuN3A00f3NIp9-Lr_ukZxWcy9qwPB09dGNtmF4Od1ClKbGrnxsVUspl-_mg6Sy9Fpu767yTcK1lp2vtz8BHAAxG0TIzLmoXzgPJBDLssuagjYRu4Q0m2-pBpZGQl3ELuNxuJ7FL09QS3yQ3UWAYsTu8FWwD_yQWZgBJFbZ10yI3ZIVkY1Kdw_o1AwWnHxqhOnMI_UXu0a-Ix2m3DhzJOJe2yhUJzHdOup_7QezjZjDILETc2yprUA2xEuhdNnYioQSvnj2SdmIn8K0K9AL90Q_qSHdhG5oA7kBhCyB-jJjf-ArhDiVOAg0NWaxWkv61gr8ubsRcN12sdvdg4w7G2pjwK5j-wCzj8eWAzhm3f7QmNbDFeoTNxpB_b4QtBzvkF2Vur5cK17V-ejMdCPdiNRFkp-1geH41ehNR3ni7r_BhBMb1r5e_fUo-6gFkEmmRZ8ib8KMgPrR09oDUSIqNOSCX10pm7u6XPMjE525cGDiTY3qum1vbKx_fS9yNeBxWgBdyJp7PVhqKFitEXLLVSDEstQQyoN6AN-RrB0s6swbK4g1m0e9T1LhfSAtMvgWqwBNrZqURyOP7hJEE2jEuPaCT3JsvarcGKnFiKyS-YDnzfryw0Y5GCH-uUEST8-4502QBHYD6mqpudttsjxn53cZjwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca433618ee.mp4?token=YNzDd7i5Jxc7aRWVVzhuN3A00f3NIp9-Lr_ukZxWcy9qwPB09dGNtmF4Od1ClKbGrnxsVUspl-_mg6Sy9Fpu767yTcK1lp2vtz8BHAAxG0TIzLmoXzgPJBDLssuagjYRu4Q0m2-pBpZGQl3ELuNxuJ7FL09QS3yQ3UWAYsTu8FWwD_yQWZgBJFbZ10yI3ZIVkY1Kdw_o1AwWnHxqhOnMI_UXu0a-Ix2m3DhzJOJe2yhUJzHdOup_7QezjZjDILETc2yprUA2xEuhdNnYioQSvnj2SdmIn8K0K9AL90Q_qSHdhG5oA7kBhCyB-jJjf-ArhDiVOAg0NWaxWkv61gr8ubsRcN12sdvdg4w7G2pjwK5j-wCzj8eWAzhm3f7QmNbDFeoTNxpB_b4QtBzvkF2Vur5cK17V-ejMdCPdiNRFkp-1geH41ehNR3ni7r_BhBMb1r5e_fUo-6gFkEmmRZ8ib8KMgPrR09oDUSIqNOSCX10pm7u6XPMjE525cGDiTY3qum1vbKx_fS9yNeBxWgBdyJp7PVhqKFitEXLLVSDEstQQyoN6AN-RrB0s6swbK4g1m0e9T1LhfSAtMvgWqwBNrZqURyOP7hJEE2jEuPaCT3JsvarcGKnFiKyS-YDnzfryw0Y5GCH-uUEST8-4502QBHYD6mqpudttsjxn53cZjwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدواج در حد داستان‌های جم تی وی
🔹
وقتی داماد منتظر زن برادرش بود و از فوت برادر خود استفاده کرد تا با معشوقه‌اش ازدواج کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/695383" target="_blank">📅 09:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سامانه مجازی انتخاب رشته امروز فعال می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695381" target="_blank">📅 09:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695380">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695380" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b15a175ff6.mp4?token=fvqH8Qftg31aDfWeIcqCkSLWMEcDVLHLPomT70CVoEA0JY1vKnjUIILt02WimYngaca5-iK5lXDczxPyn3UrYwYRWyxnSPyKNnpxkFNPbAD4AL9-hlEqjDQHnbIMySi8SSTXRo6mM9VFLjCsCyoNN6VFLLpN1DGVtAoW4u_jg_BXT8sGVhW665WHaWTNG1v9-LewQs73IBnt_IzQ3AVvlrSas8xHIHffte2Anfyb1D-64cDPKDqVx0jftS-H3mLpXvf4CIY4nXpywTCb3CuDHj3gCQJXTo1Y35eQ1JbT1vWcc8fqTLNB7tvDuvHOWYbqI8dVMg9B3EvxP5FectOXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b15a175ff6.mp4?token=fvqH8Qftg31aDfWeIcqCkSLWMEcDVLHLPomT70CVoEA0JY1vKnjUIILt02WimYngaca5-iK5lXDczxPyn3UrYwYRWyxnSPyKNnpxkFNPbAD4AL9-hlEqjDQHnbIMySi8SSTXRo6mM9VFLjCsCyoNN6VFLLpN1DGVtAoW4u_jg_BXT8sGVhW665WHaWTNG1v9-LewQs73IBnt_IzQ3AVvlrSas8xHIHffte2Anfyb1D-64cDPKDqVx0jftS-H3mLpXvf4CIY4nXpywTCb3CuDHj3gCQJXTo1Y35eQ1JbT1vWcc8fqTLNB7tvDuvHOWYbqI8dVMg9B3EvxP5FectOXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهین تسلیمی: زندگی با دیسکو رو هم دیدم!
اما هیچی قرآن نمیشه... هربار قرآن رو میخونم و روی قلبم میزارم آرامش میگیرم...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/695379" target="_blank">📅 09:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
فیلمی از لحظه بخشش قاتل امیرمحمد خالقی توسط پدرش در دادسرای جنایی تهران
🔹
پدر مقتول با حضور در دادسرای جنایی تهران از حق قصاص قاتل گذشت و شرط گذشت را انجام ۲ روز خدمات عام‌المنفعه در هفته از سوی قاتل اعلام کرد. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/695378" target="_blank">📅 09:22 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
