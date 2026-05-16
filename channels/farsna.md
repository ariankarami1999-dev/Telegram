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
<img src="https://cdn4.telesco.pe/file/OqEMc-0B_TqTU76iXe6lEFkpb9JMDhqk83F8EKJJ7lxvqFIAdr9Cq5NvMniWFNkpUlKgig61HnISHNpZpcArr9S62-FMGQGR3Z7o1hIc9twzrDgMU0Z6Xe3rCQCbcLyySCQU1Z5v3LDswpeSEG_Id46UkT0n8fVusbkHeGjExLcIc3XJfdHCkgyJaWRU2BwYPVKuqFyHrPNbiLhi5GM-cFUnvVuC7UztBBJjL7AjaC2yA9dNmHZuZqIP4kyyNYE1Z3Te66pM5GlzRWDC8TH5wlFgcFWvqqj4NXNSIpQpsPovNgNChDwN4OxHAXEMFMxmnKrGPBtMZUHwdo2fy5uIpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 02:07:18</div>
<hr>

<div class="tg-post" id="msg-436042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">«افت شدید توان رزمی» دلیل عدم مشارکت انگلیس در جنگ علیه ایران
🔹
شبکۀ فاکس‌نیوز با استناد به دو گزارش رسمی از اندیشکده‌های نظامی و پارلمان بریتانیا فاش کرد، دلیل اصلی عدم مشارکت لندن در حملات تهاجمی علیه ایران، «افت شدید توان رزمی و خالی بودن انبارهای تسلیحاتی» این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/farsna/436042" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
مردم شهرکرد ۷۷ شب است که سنگر خیابان را رها نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/436041" target="_blank">📅 01:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5IhJ0hCiT9I01SjvvnBjBhKIbCHdhpjes13h3ocXVvAStYN99MWg9ytyYkEOlfEwKBbZ8tDQ-azKkZ4oHDwpEpwyY2Q359CJCvoOnzZ8_ee1oAVrV8ll9aqI92o7n6fQ5XGFn3O6sQgJFL8o26q9k_rpUpnPfaXkUaNR9xvEwWujRXhNoXz-OPVEcH6OCWZLduRfEmx-m5l_tTlUgooAr3bhPQvyW9cXS8Y_F6-XascwSWPhhmUJSHtf3VNwyIRYqmZnPZZj5uov4N8dA9JOzViZqswuLR2kKzoXVQCHvTb34RHl-PbTNYee9HsKzw37qcKFrqeV08VTTTQhQfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیۀ وزارت امور خارجه دربارۀ ترور فرماندۀ کل گردان‌های قسام در فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/436040" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی سرود نوستالژی توسط بوشهری‌ها
@Farsna</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/farsna/436039" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfGNUYt-3IKoXMl7l4ukTpNlj7P6CoghjsWi9irJPvqd1-b7LYCRY_gzOrBbsErmcVWwpQaacqpuU2C_jSGaz4gFY0CFEiUVQRH4gUoaaFm1_YX9NPHnbHttNYTBPxUxT8m9dsfZeGl58AleqWnmDBGIpB_7Sg6o9Xbm9ejS2YN1pcf_aVhdBlHmOP12K0Id8LrBBUTtg2rRJGYLnoc2bNYEJaKJsi7j3WlTG_sb9os_PX9m10wRQ48nhTwNqNQBZ-1aUGq48P5Mk3HjS_ZPcBp5D7xB-lDZU1sndhGGZcBc9cyIrBEX8Suu22SQTwBGP2V5pR3GrWVRk_oOzh8lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس مشکلی برای آسیایی شدن ندارد
🔹
باوجود اینکه هنوز نمایندگان ایران برای معرفی به آسیا به‌صورت رسمی اعلام نشده‌اند اما گمانه‌زنی‌هایی در این زمینه وجود دارد.
🔹
گفته می‌شود شاید برخی از باشگاه‌ها با مشکلاتی برای کسب مجوز حرفه‌ای روبرو باشند، که از جملۀ این مشکلات، می‌توان به پرونده‌های باز مالی اشاره کرد.
🔹
حالا یکی از مسئولان ارشد پرسپولیس ادعا کرده که این باشگاه مشکلی برای کسب مجوز حرفه‌ای آسیا ندارد و درصورتی‌که شرایط رقم بخورد، این تیم می‌تواند مجوز حضور در آسیا را به دست بیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/436038" target="_blank">📅 01:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2mu94z5vDXFjn49qvez8lzce-enl3rftq1ls6fqwSOlEFEhYsUx2v4Xsm6iJOJ_0k4b5gAg2gqYUOus_8cfGm-JPbyDuv_pWVNskZmRXjAkrQSdcPiE-60NwFAWGFKNl4vI7NjYqKnFHbNacEAU1CinxL3GFNCsC3BDEeX6lr_OkkVZLphnNLKqooUrBUOl1u1SiLsZ15e7Z0mxF0rS-ZTz0Ks0NaUQu0XOgtL8-KjzRk2eE0aoWRvN-IdBzhDSpwVo4tcfDE84AmhozXNXVq-o-5_ar1hoIEv5YSGnwPRlvZVFKMP6rh36FfQdOdFpOTsS_ekKixtuxJn2PUhLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو جنجالی آمریکا سرانجام به خانه بازگشت
🔹
ناو هواپیمابر «یو.اس‌.اس جرالد آر. فورد» که آمریکایی‌ها از آن به عنوان «بزرگ‌ترین و پیشرفته‌ترین ناو جنگی جهان» یاد می‌کنند پس از ۳۲۶ روز حضور در مأموریت‌های جنگی روز شنبه به بندر نورفولک در ویرجینیا بازگشت.
🔹
این ناو که از زمان جنگ ویتنام تاکنون رکورد طولانی‌ترین استقرار عملیاتی یک ناو هواپیمابر آمریکایی را به نام خود ثبت کرده، در طول این مأموریت طاقت‌فرسا در جنگ علیه ایران و ونزوئلا مشارکت داشت.
🔹
جرالد فورد در این دوره با مشکلات متعددی از جمله آتش‌سوزی گسترده، خرابی‌های مکرر سیستم فاضلاب و اعتراض خدمه به دوری طولانی از خانواده مواجه شد.
🔹
گزارش‌ها حاکی است ناو فورد سال‌ها با تأخیر در تحویل و میلیاردها دلار بودجه مازاد روبرو بوده است.
🔹
یکی از بزرگترین رسوایی‌های تکنولوژیک این ناو، خرابی مداوم «آسانسورهای پیشرفته مهمات تسلیحاتی» (AWE) بود.
🔹
این آسانسورهای مغناطیسی که وظیفه انتقال بمب‌ها از انبار به روی عرشه را دارند، تا سال‌ها پس از تحویل ناو کار نمی‌کردند و باعث شدند منتقدان، این ابرسازه را یک «آهن‌پاره بی‌مصرف ۱۳ میلیارد دلاری» بنامند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/436036" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورایی تهرانی‌ها در میدان انقلاب، در شب شهادت جوادالائمه علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/436035" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIgK3yzuV2BeBWcOZDEuoe0jOYkQzPct9wH_YIRp6x1t5phylkGgRyGEwIrlSDpH2yLQS0nfNxQD43w1IRfzI6sXx7c4vXAJJ_qrBNcNHfTNB-S5MH7FHmtRmP5VwM3_sojv6NoI261bacizzle2VKOXtFaHPoRihtW64K7ZK5jZR0ncbBIN5Nz38vYt3OnQ4mZY-a9kODlCK97sqj7unQTKHTFEPkveT7CsQ7vX6NKzpZSe7r_BIwq04wdmQj9HlvFh6KUGjX8snMEz5ei2hwPqoXZegcMzHTZCtlFZkTQZGjKhhsrRpfIxwiM5Z0M7PAHRGlVuhF9ge40A4sZrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4JyAJIys9fwRyLJ-mpznkan2aiNtM9VWNsmkOjGVhOrdqs4LYB5ZqeC3TO6pkuNev3-lxMhfyKs6RB7-sKidgaBn2Al_F5QVtwZJCrfoon8pShNiWFitwaPP0Tlbkttw-rtyX_D97TNFNza9YQlP3OaEAPVP9eiTlUUvCmQMGSEgjDlnhEjkbNBREenC-ONG8-1ndOGzvgeMP8I0A2RSPO505wag401xMJo-Qxib5lIWeSgEPMMHwYT0VndQ7CsCiBBUEqggC5xwmNa2ISwnCy4o2j5qruczhJBPBp1KOUYHje7GiCkn2jc0KalqnabJbSvj9H12xqA4Z-HyMCjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhZyvp5_9_GaVd-HPbi6LxmoJ-3BmCd-BQIhK17nR4a8JGkx3-QE05iYTaLTLy2Wisq8RZjQGAtFs1NMj4CPJQryf4hzmecAePNOxjkI8sJPIA5bD-MywHI02eVYb22iUA-OapLq9d13tEyEDCWLbW1gpPg9B5t24csfKyzDUId1GaYWe6599tKz-TXm5wV7ywLUV4Y2WQNILZRqWSPxnZUATLS3UqqkC-oeoO_MlNhtc-RIG3X0qkrNz2Km13nsjogVyFHrYedmWZzlQYfJcL4V_kjKLzRZDAVUlJAzXA8h1VhZ_q9Wq6ptyTkZkjIDLBMR8kCFol74AW6PSwCoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiOC2lUzPqJsC83xAvdtsbfTdjlYS9EMtfoOA_zKtxbuZ9-W8Ns50Mz6Ypn43R8c3PNk8Vg7ozlBGWNfyDhpO1XF1rJxuuYuGo-kH81XhqI2Z3n1qDty6GdM2xKjffM3N0aYD3cYS51aHEh5G1eDmfOrmrWPVFuxeRTuLsxOXdnf2znD00-zmA41lF0H1sLZ0tqfvt7qb99zZ3TtT1Q9Ju9t8GCB0TdwgBbHqF7HT7EdPGVwzsbr4B6Y6w436LXoO6hRyVJjAjzUJRrOE_aSSt1Ef4RZbz9trGnq6C_We-ZcBN9Rr645WGjZ-W2gTOJPyXFTfrWatp_EgbD69AcNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKKduC4IoVAbrPfMsbAyy0ASOfSLI-LAKJEblZUNzWM3pqKnMtVomO1CZ9ds_yUkJHCILmYEbLwl4e6ljKtkjJkEiBj5oPdCs6TUAhiklTauMV_oaNnIRa9A-b1EmlMXopWBI9YIt0pFD0aprfJaB3KsDDQe9bzMj7MePdGuETSNc5itX2J1JOUG3mB9pXuHGnn8SK-TDXb4yScD5iXUaEt3s8cPbQePumVJCu0inmdpkMoOirTYv4j_j12go9FgYyYtdnUFTte-1fxz-hYicaFPkPqbiL8Cl6grahw-UyROlzNw7j83on8cwGDoTLbmociqjWp0HUxYKlrrFElrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۷ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/436030" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN9dG5feGevYBznWq2KvQeVcl2qW6k-CXs54xrpkEriRnC9qEXpM2ojFM3sxB4TOUuxPbidgyBVZcKxizgSKxm3XDr3k5k67ySUeP1nbpO55_IzUqx344Ppj4JI_5NlnkSiOzKdMa5ukON3vKHyCV9d3Y0P2tGioDoCJJNdjAOUu0bzGkm5-wTlwu63BqXuZjHk_bJ_I9iYFMFqkrISTT4h2Wk4oQ1JJzUxklb4Rx7h1Ykb6C35MFWCVcD11RtuUaBZwGE7lz2ED5oiAEORdfs08KSuhNV-CvLSJRMIY-AwQshqZnrBiJ_qWwXTSVXwMNG8Jmf10N8XbNQrN97C5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZYmeiJmTYEA4q-_UGMiO8Elda4raezFtOJA91xVFIOFtiQq2dr_96zogLChpf4jlNJN_wafKBCwQa4N47DPGCMDsq8n2os4wgiX875i90rbbDFRvl84v91n__pZFmlG6KGTwBXKITuFMi2N4iQIGyI_HKPvXggl6Pjh1qfu0CpSrar5vLKEKWS9lZU8Txyc04GMq7RBJaA8kAfOaTXUzWPOaMMLB715MQKHEH4Iq2dynDFxAN0xfHvtLE6GeY8eFQaGuRfKSwbXvrrp84gepntdMCLHnDGBzPF_fG3rDpSgTDoz-43INcf-QcvYj_grwaRkzhDBk68uX9DgG2vHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9TFK84mrR3nMgg1uTJsMHnpDEmH0q4KKBSseq8HW6DVhfptlYoZkwV4ax2Vrq_gIvypaf9jWep-_4sp5VygGuhrZadHfRbXCqDGSNNhYx7brg7Q9NaaGwch9Xm8ajQ437LcULvP8SaQXwkJq8cVenhSWk4csYHlRg-89gNnJYENQkzy_2c4j4kjqvYrpki-LblQE5cNwh_0m_trvlnVOUPZZWBAqvtx7eRPnusJUNwQG1OuUxzpGdVt7Cs4KRMDbVftWUe0q0ly_9SNzOwgixtR-sN_VNw_Of2bre0RXSYCM2Vvg2ch8nmWPVUYHDWxl5quh-QOeFJIuhUYr6zuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfSpSLPCtprlhAv6gFkjwD6XlJ8lRhWWxFOII6J9LLFqX4toYjb4431uzVjKtnhQykQCo55Z9k_tBW-pRNqXgb79y-UiDMXvDIOWqs5v68hzPimQRf_gsD-lUBSAvzt5cEjLUiPyqK3vh-P4w43nHISYCwUilWv1hoVfKEw48xiRVjs7a5BPd875tz-d7i0yJJ5gpr96kdS0WyWldkI9F6RK_3YPbR4viPlsb6-tQRoqUHAonJ_Z3su0Ba3gU_sErKH3wx5FeD9NPX88U4SWyFapqeCsPLOssb5P0KhnRDvcGAYIxwgny0K1GCuSIJdwDabOOzXdP_vvvUW0G-p4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOgTzrWaocC8DUnK1G8OT0u0pLLJ9BDfmZwmnZfxvJOvEaAc84lTFJXPil3gDUgT6j3dGxpV4kfby-rK__R8Rkc_gfxBdEJjEoRA9QdqfbIH8zhrSnxwrlJsOANi0LSiqukKpvv8TeHhXxHG80nbKtVGcchBqEU7QrBe8d2h8CnGlAMBMI8dYqaUsPM9eu6oRol_W0JUlBNE_1lCGq2oDXvszRJ-m8qyIJWduLDdNpM-OdKTuQnxlywqFP65TLFRsYrxy6m783wSS4x2CMMG_c_Ciavdcio2R18leIg1sgDF0aKQjm7Kgt7xiDKuLbfFc_AAGDy89lszpc3vEbZ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bdffc4vkQalLOcD486iZLSnKf7kZ_XxHavjzwZGPAmnpkTB8vol0QelQuHYxW7MzeYsuXj1Qknc8EJuRpSfobMxO_TqezAn6BjXVy62_2a8mUI1LsWnD8NIyymlYKyizepPbiWeUxCetG-3wuj1-qYEFidba6oFSDoiPiLB64VLd-fXReeHvdNd71Tgwhqf46eS5yKzkTXN2Ck2S2o5jyVQXh3kjrdbWPbXI_FSrhXrcqoeaBauU_cu2RM30tjnam1ij6Dn8fBbSYlVA9g9N4ACXjRD0Ogj8rC5NBZRS6LvZs0hHNabVGy2d44iZqKLRCelrHtecR9sUBq3CH8rMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3sfW39HmcZbAXFyTD4IdPomHjRuucXcaXCGZgpZTVAUrfCo0lJSSDueZh1qvyZFWadzvr92orhAjJPvv7AnD7vRubZSN8XtveuLOPUp0zf9IXJ9l61zie4sDKV4mWW8DW5VVeqsLHUbXUPOy6LwNxDbpunURBcT8zCeoZB0-97ieYAGnFH4sVLW3SRxUzgS5aad0p5rncg5n0oGy5i-GPFNHAEzOckgks6J444s4nWPxbfeLOcHkDW3VMKqPw6sg8FwBLZhj_7ZUYIplPLHSqJDF4Syt8ArT07gVI5DgwPqvFYh4sWWSX_Oj_w5V4iPqQe3tWUr5H-HQBPPC8JoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAdat1ofGlrw9OrQMkAeFGXMex6qEAMfvf0vNC0OEUoVxFWDOeWhAwSGDgFR_kpGDzyZ7cC33v3N3kwjYa-1u2_TDBT-OTrM-sHon2GkJKV84cl-M_A2KyHyrlYgLCqMgJyaua9QoYqvFF5ByfBAreDNTyjwjPi4Kr7lZ1cDu-YF5uMA5M4wCJiFkfZva2MsVn_eLNP3iV0TzR6dEhz3Vcj-gzG5EHV1Lqt7xOR9SPctSWJ-Wu1mYmaFZIkEzpZCxQ7k018lt6PKjk8Ff2EYj6k5yxCvILGZeBH7QCo4lDhMIRSwhmHxXn3__HXL4VS_U_UaWXTUl7qXwZkHsreLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6UH0Oe0t1OrwurdPB823svpIMrf0UFE_-ABsI7eCyzXUukVkmoOQLfOm2rKph5TGrlz0FDSehjzs5L7affimYrJfyVpi-kplcCLD05JAQK-r01Z6CLsQDQwZ20ABtwrINmMr50PmsIJeD5B1GB-slapZPqCqZMU9OiNXomsCRYQgvX3EdEGxDmvNRu4m2RcTLRLb6qVJ1rd6rg5gBY2Qj6azzkiYkfCzMTCS7cM7gIlppF6qZRleBqvmnptXmx1F2UCyAdp1jR-cQXg0-4XSp8vMY_xNhu-x_3abRkX1LCPc9jJNvCeLEDt9YKr6U5f544O03Fp75i0_Nf6pHBqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULqfX2e3NpixDRlVSAM1GmpyfXg-ncuZSpnMfgYV-CccyoIWiBRLzHjZNvY7YGP8py1DGPiZN6AmP1vjEB5uytA23jfR9bXH0O0TXutbHQxDQsHRs2kYeKEF-FjFnKkoY0f7_jSASZ_swfCVqzQsxe20t8DSu53aUMkTq2fFmTh3jQBJBYaPiQVkHlo3IXWNU-uhERUa0RYCmWN9fpS_5PUoGJqICw-l5fl4zQ27B1G7EnFsmVIeZSbw2FCzzb5xYGAS2kBFmaMqjThs1vHqUgIDLK67qXPrx2BXiaBy0ldhKpwUNNKkZzg704_ZT8FMkXdMtB8MNDAwAv6lZdDGgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/436020" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_6I2ZZgVX_EUZzKN3bmXdYhYpOjo7HingeU5nUeErkTPTvnacRCd3dGTiBhnI-HQjlpRojvqR4AEfXWA5JLNcj4vKnWlC-QLjZwte4eUNodVSUYgfj7E1td8G-tpw2qqJByYoFA8kgAlwPo--ptfIob7c_D_OVngyGd0syP1J8qUZak29zTdyJW3u6KhufiPsD8kSPEMXSTmiP1fXGuXwjl-Ey7DUKMiWU4Wxc8jr8ccYMi7SVEX8Wn28Ah9b1QKPn_nTNDBJjS2NpdsI2AFHZVjlNiVexi6G_kQqqkLHM3Cv8NcfxlGHAecBKOXSOYbZOW9XIoPN8rbmlwXlOtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اتفاقات مشکوک در انفجار بیت‌شمش در فلسطین اشغالی
🔹
شبکۀ صهیونیستی کان مدعی شده که آتش‌سوزی مهیب در بیت‌شمش واقع در غرب بیت‌المقدس در نتیجۀ انفجار کنترل‌شده صورت گرفته است.
🔹
با این حال، کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/436019" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
در نتیجهٔ انفجار سهمگین در بیت‌شمش آتش همچنان شعله می‌کشد  @Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/436018" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌ ثبت‌نام وام یک‌ میلیاردی کسبۀ بازار جنت آغاز شد
🔹
مدیرعامل شرکت ساماندهی مشاغل شهر تهران: از هفتۀ آینده با کمک بنیاد مستضعفان، وام یک‌میلیاردی با بهرۀ کم و اقساط ۵ساله به کسبۀ پاساژ جنت پرداخت خواهد شد.
🔹
بازار جدید به‌صورت موقت و با نظر ۲۵۴ کسبه در نزدیکی…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/436017" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/436016" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3Axz81fA_VJRg0yYp3kQRecYOWSG5lsRoPamKu0Q20q-vI1c9teOFgwlfjXutboguR0uzeWslS85elE-7aYGNlZZIZpFq3KSQXKmv5tfoU1S2hF-yg755PGHF3Kh8EO_Rcp7K2hj6Hphsh3Ms6xRWBdA1BiC6chw37JvWddLLo_OW-BJgXTEgu92as9Zf_-awuYlxHcKMywTXcOPWokU8cYJDA8Co8ofutE3jpIjGdupksTRvwubRLNONnTtETTHaeQNYa4VEazMAZ5KnGKaMOtksaEXsMCJ3wnrPE4LtOolJSdxaT3BdByyL1Gpw9N5rVeL4Rde3dSlmXAvwF8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلیس و فرعون
🔹
روزی ابلیس نزد فرعون آمد؛ درحالی‌که فرعون در کاخ خود نشسته بود و خوشه‌ای انگور در دست داشت. ابلیس به او گفت: «آیا کسی هست که بتواند این خوشه انگور را به مروارید تبدیل کند؟»
🔹
فرعون که ادعای خدایی داشت، در جواب درماند.
🔹
ابلیس بر آن خوشه انگور دمید و در یک لحظه تمام دانه‌های انگور به مرواریدهای درخشان تبدیل گشتند.
🔹
فرعون مبهوت شد و گفت: «عجب استادی هستی!»
🔹
ابلیس گفت: «با وجود این استادی و هنری که دیدی، مرا به بندگی قبول نکردند. حال در شگفتم از تو که با این همه کودنی و نادانی، چگونه جرئت کرده‌ای که ادعای «خدا بودن» کنی!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436015" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">هواشناسی ایران اسیر چشم کور رادارها و مدیریت غلط
🔹
سازمان هواشناسی ایران به‌عنوان متولی اصلی پایش و پیش‌بینی وضعیت جو، نقشی حیاتی در مدیریت بحران‌های طبیعی مانند سیل و طوفان‌های ویرانگر ایفا می‌کند.
🔹
با این حال، شواهد میدانی و اظهارات متخصصان نشان می‌دهد که این سازمان در ارائه پیش‌بینی‌های دقیق، به‌ویژه در بازه‌های کوتاه‌مدت و برای نقاط حساسی مانند کلانشهر تهران، با چالش‌های ساختاری و فنی عمیقی دست‌به‌گریبان است.
🔹
وضعیت نامناسب شبکه رادارهای هواشناسی، ضعف در شبکه مشاهدات جو بالا (رادیوسوند)، خلا یک مدل عددی بومی و منطقه‌ای در کنار مدیریت ضعیف از جمله نارسایی‌های گریبانگیر هواشناسی کشور است.
🔹
به‌روزرسانی و تجهیز زیرساخت‌های دیده‌بانی، سرمایه‌گذاری بر توسعه مدل‌های بومی و خروج از انفعال در برابر خطاها، ضرورتی است که تأخیر در آن می‌تواند تاوان‌های جبران‌ناپذیری به همراه داشته باشد.
https://farsnews.ir/Economy/1778961014305887280</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/436014" target="_blank">📅 23:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقامت شبانهٔ مردم مازندران به ایستگاه ۷۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/436013" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gClF8lpc8VZp2M0ddoNfhsbjgGdXftPfD9QrLgetxomtacpAN-JJ8Nl9xAsQsJP7O8xkXrwvIvpEaM076aTdHyZr8K21r1-filS4JV6amhxT9Mq6LvY6gNgHiKjurngxE_J0XCFAGkDqXkHJAHw6-3PjY3ik1iBw4-YiSmbeEtJAz80WcYgFao4ETB7hV1jT6MseqmPNFSLSanTo_u8NMnwKWUhN3NWPATJfkt6CnlMEWDlGBYU9hpWHGSjFP-4lVqHdgNOBSExrFAOkKUsaqfvT90RXdQtv5iLqIKvmqog4c1zRnxTfxMFekenEhBrEmUvdmRKYfXWps11JOQOd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTNkm9uxXwlJnqBQ-hUeGti8wXs3Dua-qAb3WhdWU_hJUYFuwmPm3ltvpMXHOHtAMI1SxzKenpyyR-WLiRgFKae3GcNYWJVIW2Gew5ivrUGMe_TH5KqE3TdXGvku-cSdywNjQ91he4x4hoYnUge3VSPhfE7rw5cijlGyi8vWizQMEn6wo0YndEBJaOELQVk1kjxZUK4eOolFg-ymww4naDDorpX3UtlsvRAl5oQzu9dxXJMgqDNCt6w4pt7AsquKiXrw0rKvkkK2sQYPl15MN_cFO7e6QxKVoG3DaFASfJhQPqEquzmA0KNAy-6OE7xU9o2jMMskcjYUixoc71ancw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saClPrqEVBPlL-MY1YXnktVcfMzug1Wnd2oyVvgqyAXfGMVd8bc5hmW0mhjGIM0Au2XvsngQdaGARdrrCzqJMEp3kywrYlRkM6BIcitxzJw-8tJRTO5AOw2X6WlB6lUXWzY-dJYeyL6Gubd-z9ksjPPJhU8cqpsFil28Rz9-QPnNNPCNEGlgcQgVGjaVAEMpLrMb5oLeu9EcmI_P5diMorCJzvpi_2jBDMgPkuefCUPd1eJYXqEiBWeZ47JJc_9C6YBjfGgrw2KiT4mmjsPAMVBNDqN6a-fEi-ozYmzJMNoQyX8L0kUHxz1fGNSerPaxSOEoJI_vtVAAEwC6_1rqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gx75Oym-QFz0U9J51NmLpi2J58sgjcGHuePbPWw3jt8ohDR2BzHEF_qRfN4brTakfIsS8v36PlufX8EcfsCDEkcLUZ1k2Qov3MZ8Q7glBo2RZQCSspX1x6ZGCzMqsOFwCXvSxqwNGNEcqe-3GHTdS0a_7UPVQTlp_jkRlXYIM0CYLn7Fj1s8PwbYEWKitadj_SXQY24GnV0oAcp7wI3OcUuRNmOpF1R4INw6R6MMvev-0r8a3Y3VvA2I5fqD77WAxLp4wIH3oIjSYqI6xpCk9wEwrNp6RbpUreC6hw-rr2XOHZN5FAMUYejCaxrtGGV570JJVCdtcqvekbAG6D9cCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgTw24YvLTkYD_ORvbd972L0vypVrlFIGim_0wERjAXKK0k3A2atnQOef5qtAKbFOvtPUxisDejW1rB9_vrso3ltD4ws2tz7QADDsUGc7eWOraL3nmvR0ZyAyYBG3Imv8CIXA1yaE-YXudUs-c2KwlobfbDen-m72YxoQhf2_18Xf2ZSVcFTMdKTY0LDNn1PFvMoFTJOLdMtEl43ZSI_SZZzy7_MmrJaxFycV2X1Bd6zCXZo8umHNDcwRznbIDxHaEYjxM_HwUgESuFJuOqV179x0ebgnv8Vmgc_-tI9FhT0AQMgHnQZY9E9Rtopvl6spuknYfisn_FqSjPlCB3uRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم رضوی در عزای جوادالائمه(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/436008" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/436007" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع پرجمعیت مردم علی‌آباد گلستان هم‌زمان با شب شهادت جوادالائمه(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/436006" target="_blank">📅 23:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
سقوط درخت در نوشهر پس از تندباد شدید و رعد و برق مهیب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436004" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436003" target="_blank">📅 23:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt_LFv4j2GisQa-aa0vr5o-Ltirp9pjAgr4CSVS0LOIp7odY40jhmjgtcv4jjh6ydekbKcbEePJpsaHp9L5DSjHj0v1TfMJ8kjpOO5dt1M3DvwCSvr-vC7kGGDiYzSd207WPmxWE-GkVHKGTtRMKC4TdfdvmaS1l27SGalkK5gNwe0XFQwqzGRBLDsWzQVaYwgHpQdjOvXQoYQGUa7QlIjSmKi76lidf38Ttanq5MbgS7KY1u7aqWtFcf5bVY-trCj9ypgRe4QEJUEnaNnErI__nIKX6byC6sWRg-PSuth4-wh4xT3T5vyIp9-CZKBS237j5AEQEvIsvZK1LQon2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: مقاومت ملت ایران، تحول جهان را سرعت بخشید؛ آینده از آن جنوب جهانی است
🔹
جهان در آستانهٔ نظمی نوین قرار دارد. چنان‌که رئیس‌جمهور چین گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/436002" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
بروجردی‌ها امشب برای شهادت امام جواد(ع) سوگواری کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436001" target="_blank">📅 22:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gShIsPjckJ0Syi7hUA-97_I7MiSXZSrSJe8AbNMKvv0nNRPJkKfrKNuO9aPoVE_-iQFbymrTVV_jsYK1ISGpKMQCDL1FXYLPvl2Tq2H2UYvgoCW7uoKInoc2ukREQSaogkwNSfK_qeS9GthA3HoK3ZZTHO283jGnpci7PPmEnYhb4HxbpfFGXwmja2gfdet_NcBtsXMmv2O0WEXSunvENhdxB90EJWQN0LiFSTk9JuPJMynn8udhkVhtY-UpmFB-wbUiu2VyfeaybJ2fPUwEj7qoRhGZgArpyKbIlySxbGSyMEP2P6dXRTa9XvK_IeTGYaPk5s-mVT2f9gwAujSFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوثری: هر تعرضی با پاسخ کوبنده مواجه خواهد شد
🔹
عضو کمیسیون امنیت ملی مجلس: اگر آمریکا یا رژیم صهیونیستی کوچکترین تعرضی انجام دهند، مردم ما، چه زن و چه مرد، در صحنه حاضر هستند.
🔹
دشمن هر توانی داشت در ۴۰ روز گذشته انجام داد، آنها نمی‌توانند به راحتی بمب‌ها و موشک‌های از دست رفته خود را جایگزین کنند، اما ما به راحتی میتوانیم جبران کنیم.
🔹
آنها در هر نقطه‌ای که حضور پیدا کنند، رزمندگان و مردم چنان ضربه‌ای میزنند که جز ذلت و خواری نصیبشان نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436000" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435999">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4yYB-12x11Z6z2e1IY_nGKhM7IQQBWcYxg79kAq7f2EuHauE2g3qgyuxOEelfvlDCey5mjktBDq-TAivlsrC6lFA2PA9BYtkjWRo2rKkvG42lBVLRpu_E3kx9zTRf2cTegG1FZD9T-ew8vIn69aFZR6i_873YjM7rnA7Va8qevVTPvwSJbhdgprIWSA9Ei1EX8qIN5LgpX6z4_cjvN0V9B-3SXcxpDy46b6TNfQPyGJaSusDAmeZryzk9kKjZ3iC7l92pDbCa6VmGRxsyNj5E-Ohf3z7XW2XIIekCGCXAYr9sGkhwW4PGWWgaO5d8YNukmQFrvlOf9xF7RwzKqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست با پهپاد انفجاری حزب‌الله
🔹
ارتش رژیم صهیونیستی از هلاکت «یسرائیل ریکانتی»، از عناصر تیپ گولانی در نتیجه اصابت مستقیم پهپاد انفجاری حزب‌الله در جنوب لبنان خبر داد.
🔹
ارتش اسرائیل با وجود سانسور بسیار شدید تلفات و خسارات این رژیم در جنگ، اذعان کرد که شمار نظامیان کُشته شده در جنوب لبنان از زمان جنگ جاری به ۲۰ نفر افزایش یافته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/435999" target="_blank">📅 22:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بورس آمادهٔ بازگشایی شد
🔹
سازمان بورس: آمادگی برای بازگشایی بازار سهام از اواسط هفتهٔ آینده وجود دارد. زمان دقیق بازگشایی بازار به‌زودی اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435998" target="_blank">📅 22:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد الله اکبر مردم بندرعباس در شب ۷۷ بعثت ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/435997" target="_blank">📅 22:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzXVK9hGE3Z52Yjib6fqyNtCH9uwL97-TLXGd0DG238nM8XGOu0AtBg5atFm4VaPFqTED5APakrXV6V4XVsvXEempGl3mAW_23Cmxz2kzy9ifRsAwUtFzgV7cyZn4dOTjH7LCqMnM6YmdXesagoAmvkkCwBFwYljkviSArjo5t85Q3IHav7fuJhwVk7Vsd-F3qeV_l_HmSpbaWzC4r58CxjCidf1if7JgAbJ4BpnnyAQHl6nukQlpU_4_AJ2SjG1c7fxj0yBfXQTvPJYabzonsmhNOljmLPXNDlwinDiIAdxG1d-riGyU8Ik1VZmQ4WNi9WDrjwIv98uhVtKFVhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارنمای بیمهٔ ایرانی تنگهٔ هرمز راه‌اندازی شد
🔹
تارنمای «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگهٔ هرمز را شروع کرد.
🔹
مقررات این تارنمای بیمه می‌گوید، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435996" target="_blank">📅 22:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiI3rQRj6C_r406i0dastJRhmSi4wxHuqE4S8aoTHxxmjVJdmvaqf4PIRqmW4qpmp7nmlHmArtU9jBjqyBrf9AMJttHDJki9LoYc3-_0XSHnhwbDVz_JyoSp9SCetSIaEEaRqTYHWjpgbO0L8QGNcBXAeljVoXhPgxQOHhqKRQP92uraoCxlr0B1bJjuZtnsq08GQPvXHX0MSKJK6fa1ACyOnCN5xTnZZJEGDc2zzZ9cqSo48bVBZ1un97lhdEQB7teFtIarlXRGd3cokvCw390tqFJMEK4N4pWJvRCQM6YLjtkEZz_duX6XDKEhj5NpQzisvxh6uyJn23FRgJL9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران از طریق امارات با اختلال مواجه شده است.
🔹
پاکستان علاوه‌بر تخفیف ۳۱ تا ۴۰ درصدی در تعرفه‌های بندری خود، یک ماه انبارداری رایگان هم برای کشتی‌ها درنظر گرفته.
🔹
کارشناسان معتقدند که اگر این روند ادامه یابد، وابستگی تاریخی ایران به بندر جبل‌علی امارات که تاکنون سهم اصلی ترانزیت ایران را در دست داشته، برای همیشه پایان می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/435995" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دعای چهاردهم صحیفه سجادیه در مقتل رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/435994" target="_blank">📅 21:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323911a5b.mp4?token=YpGhL1p1Veu9Xe_UJ9u4MBx72Rj3WQahVX08C2z36ezcRc4p6D0kf_9JjjVvFAQKo_OXD2vCFjseugrF5sNBZauF-saEG8UP3h-vAxhY4q8CrxMuz9iNmquu49IzsOPCskMTQLvMq8p4TCBbvx3gcEg5F4A1FziTmCFeGWtb1FCrVvIujHgW5NqevI5U9AbNJwAkSvkIk-D195sjeaAFhhCfv3nvc9XH4iQmGBL2g562uIwMuFoYF7B_XaF93KzvtmWaMZx5eTzHF1EbU3eKteNsZlf96mwXC5rf8IINL1dlfhtP6OSkDCWy2R9AF5jOLDz3l9VlAzeeVQpWjA9jhAuKzUE8ImLpKdE98CChNyPYONH_IXxBHIF0sfLGXrkJRK0hpMvFvAJhqHfO9aj0lTubupCS4nn5WKtz2fwy0F0EM4R2xF_goCGzyO4PgxBqI660_1oQFeUWWm9ek0q2mbryRGYDX7JCG8mdDtxO8hMKc9Af0junKUkusGlFXwo676yMzMttVJZS6BgcMlvu6Bys2VcKe_EONMqqxlzrxex051KWAarFQPc_zUJRDwkaNGXSFj4cXRD1667p-dHaxeGEPC3P8ScQWsxKdN9vGlZCtuwAFy8SYcqhSf8qs0J3g9Rs8aeBfSY4poHYAColQTdqTaCGlIgtRdOhN_fZ_I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323911a5b.mp4?token=YpGhL1p1Veu9Xe_UJ9u4MBx72Rj3WQahVX08C2z36ezcRc4p6D0kf_9JjjVvFAQKo_OXD2vCFjseugrF5sNBZauF-saEG8UP3h-vAxhY4q8CrxMuz9iNmquu49IzsOPCskMTQLvMq8p4TCBbvx3gcEg5F4A1FziTmCFeGWtb1FCrVvIujHgW5NqevI5U9AbNJwAkSvkIk-D195sjeaAFhhCfv3nvc9XH4iQmGBL2g562uIwMuFoYF7B_XaF93KzvtmWaMZx5eTzHF1EbU3eKteNsZlf96mwXC5rf8IINL1dlfhtP6OSkDCWy2R9AF5jOLDz3l9VlAzeeVQpWjA9jhAuKzUE8ImLpKdE98CChNyPYONH_IXxBHIF0sfLGXrkJRK0hpMvFvAJhqHfO9aj0lTubupCS4nn5WKtz2fwy0F0EM4R2xF_goCGzyO4PgxBqI660_1oQFeUWWm9ek0q2mbryRGYDX7JCG8mdDtxO8hMKc9Af0junKUkusGlFXwo676yMzMttVJZS6BgcMlvu6Bys2VcKe_EONMqqxlzrxex051KWAarFQPc_zUJRDwkaNGXSFj4cXRD1667p-dHaxeGEPC3P8ScQWsxKdN9vGlZCtuwAFy8SYcqhSf8qs0J3g9Rs8aeBfSY4poHYAColQTdqTaCGlIgtRdOhN_fZ_I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگرِ خیابان همدانی‌ها در مدار ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/435993" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff25f4162.mp4?token=a4suji7b2DbVp_K_im8xMtKpYFH9wBTvbJCpZYa48gzfDuM_Go87ZC8lGc6pDvETfoe-uu9rHZ-sRR15XUno9nruH81yJ_u-YQDnhkA5YyzxgeLovDJBjVO2ev7weSrAhaE05fmiH-eG-3I214oEcllvwcdS-cfwNXbxZ3SjxVcKIRwnD4sSIpX9vzJZ4LmK0LC5YwTkC5IYc7p_qQugMaZGzMyENBCYT7ltyPVA63DCXmIQ37qQi7QTirmj5A5gyMO7TBTyBcqyajxcZ1ZKKi8itm2yUb_wmShnmAOGLgvyz99GjZf_ai4bN0zQ-1MnuJm7-bdXp9zD6MDG_oZocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff25f4162.mp4?token=a4suji7b2DbVp_K_im8xMtKpYFH9wBTvbJCpZYa48gzfDuM_Go87ZC8lGc6pDvETfoe-uu9rHZ-sRR15XUno9nruH81yJ_u-YQDnhkA5YyzxgeLovDJBjVO2ev7weSrAhaE05fmiH-eG-3I214oEcllvwcdS-cfwNXbxZ3SjxVcKIRwnD4sSIpX9vzJZ4LmK0LC5YwTkC5IYc7p_qQugMaZGzMyENBCYT7ltyPVA63DCXmIQ37qQi7QTirmj5A5gyMO7TBTyBcqyajxcZ1ZKKi8itm2yUb_wmShnmAOGLgvyz99GjZf_ai4bN0zQ-1MnuJm7-bdXp9zD6MDG_oZocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خزر به کمک خلیج فارس آمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/435992" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqeDeKe9axapPNpKn4-pprC3oOLfOX08ieOSuzoFoIg723nBNn-ZFNrYiznjlnV_qqn_hFEvd3qEB0aTiSBBwXvrU-mEyGVh3c0uMDxdQKhgkWGgj8lxTUuHH8izNSwJaVIxznak1Imfa-c4RG30dq99d-GWwOdOHLvHSN9dWNZ1Zry-kJMJwasORuPYEf-J3X9jcIwkZauZ6l5DfdjpnnMwbS3ZS3uw0Z-Z8l3q56lp1EaCGa9T2afPiD5bwJewYkAFmbUKJWrLINM4FSLqrY9sYqxNS5u3BCKDBBb1SMKHLeDeQtkbd1I69jdDkBg9xkTzaPR-7KN8DZuLrc04_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/435991" target="_blank">📅 21:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6e243109.mp4?token=Z0lnbwfqWJfpnem2NTklhgDUx2RCHj7aVPgbHFRLpPi7JqEQ6NzkXOFEzEhAubJNqbyMJtmt1hsiuQpbMGT8chFHCJrHy1daYUdd6ceS7AK9o9SC_u5tnyQpatlNyqO9_-_1CkLiuu4HoJLphJhYPT_chz7tKVTgzU0ZOsVPk0OBvxKx7DTyYFvsI7S80CIMhKDCSuIPy3thUDwIoVEo_6O8uRSWUCyn70wa1kpKcb4CCgXx7LNyiJ-zo-Nx6-WY2mVW2nUFUBucFKkdNYnl065e1Pdi8QPUj1L1t0QpQU-LGvjIYVgc9wPOVl8f1S3ggEGNIVPn9P04Gyvqg10hyoXl-GAsnEstIkrn1jWjYmXMP7yR6xOFnLRkVM-xaDmpjksK7QCdjnabRNHWpfdrhxMv4OvP4cf2sQ5RzrCnJX5a0yzDCHcK-KwVbhG-0PwvnpPqWKu49kcA2kTyg2ZC2Q6aT7q_5ZZ4Sn1MOvrOfCMFWiagsprmtgmDG1tzQ_y7FqRRauR6x7nEZgX7oE9Igq2gyUl71CIVeLQFKrE3V5wk9TglAOxs2lTGvM_N4sh_RoyX-0GMuldl6on4J1vSlIBXIZI1G1z_fGFXCEbk4vF00OZsfPuVCz7sRd7LO208-FKOezeOZIqrFlF4CJccf0vqvdh8TNEAPOqMKaSJliY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6e243109.mp4?token=Z0lnbwfqWJfpnem2NTklhgDUx2RCHj7aVPgbHFRLpPi7JqEQ6NzkXOFEzEhAubJNqbyMJtmt1hsiuQpbMGT8chFHCJrHy1daYUdd6ceS7AK9o9SC_u5tnyQpatlNyqO9_-_1CkLiuu4HoJLphJhYPT_chz7tKVTgzU0ZOsVPk0OBvxKx7DTyYFvsI7S80CIMhKDCSuIPy3thUDwIoVEo_6O8uRSWUCyn70wa1kpKcb4CCgXx7LNyiJ-zo-Nx6-WY2mVW2nUFUBucFKkdNYnl065e1Pdi8QPUj1L1t0QpQU-LGvjIYVgc9wPOVl8f1S3ggEGNIVPn9P04Gyvqg10hyoXl-GAsnEstIkrn1jWjYmXMP7yR6xOFnLRkVM-xaDmpjksK7QCdjnabRNHWpfdrhxMv4OvP4cf2sQ5RzrCnJX5a0yzDCHcK-KwVbhG-0PwvnpPqWKu49kcA2kTyg2ZC2Q6aT7q_5ZZ4Sn1MOvrOfCMFWiagsprmtgmDG1tzQ_y7FqRRauR6x7nEZgX7oE9Igq2gyUl71CIVeLQFKrE3V5wk9TglAOxs2lTGvM_N4sh_RoyX-0GMuldl6on4J1vSlIBXIZI1G1z_fGFXCEbk4vF00OZsfPuVCz7sRd7LO208-FKOezeOZIqrFlF4CJccf0vqvdh8TNEAPOqMKaSJliY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخت عزای حضرت جوادالائمه(ع) بر تن صحن و سرای حرم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/435990" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KUGnahVyDpOR5P3V6AqFfNGrG8Di1v11tuSzkaBFwaIexuQ2Rvrj1c_HI4XzNFui675ogL5_BSZEYTs3YNi-rfBHEd-g05ylNMjf125Ee7f-HZQ5RDkv98QepVf_1zjYS4KBpoKebUB-92Z4VPTGPo70uWBxZ7FSOTSFbHaTkXzwYFhRvc5eWL_BF5mI0R67raSAENnJh0yi7OuAxz6dDeC1-cmpSU2plaEKWeHATKto-FZ5dGBFNJMqCmqA1MLN_9qPx5R23nOQKVN1nB7D9r4p_6ChxM4Q7-_dv-OvulzNokoevIjMm9gSIgYztLRnLQ3cy7VrkZbw0bZe1GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارنمای بیمهٔ ایرانی تنگهٔ هرمز راه‌اندازی شد
🔹
تارنمای «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگهٔ هرمز را شروع کرد.
🔹
مقررات این تارنمای بیمه می‌گوید، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج فارس، تنگهٔ هرمز و آبراه‌های اطراف آن عبور می‌کنند، ارائه می‌شود و پرداخت‌ها با ارز دیجیتال تسویه خواهد شد.
🔗
جزئیات و آدرس این تارنما را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435989" target="_blank">📅 21:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3wwh51ifO-Bqgu2GKzdjmWOgyGpZU9ZnPKlOcnLnnVHe5_bA5NldtxxurUco9Rg6I_ny4G-CXXtRy1Er4yKp3_1RMuf_78BPciOBY6nPdrJn5SM6WIoQEfVJOOZqF6Qg4BFTMtQUd2mXTUJUCH0hfITUltNVc5lsgi5s-OFz54Vd2I6B7A3bgzgEbHwMko5KPnepoVm5ffk7Q8GdreRZ8qIXB44g9wiiEuVhlRpkViuL06NXIdlVgf29s4rZhyO2-skj-WGFashAEUUqvMAzURxTrOa6XdVV79bcHpNzhmMFS_0_oxZ-Hj8Y2IOJjsk4-2iFrZZExme5tX0ucxwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: تحریم گزارشگر حقوق‌بشر سازمان ملل چهرهٔ واقعی حقوق‌بشری آمریکا را آشکار کرد
🔹
معاون حقوقی وزیر خارجه: حقوق بشر در قاموس آمریکا تا زمانی محترم است که به رژیم اسرائیل نرسد. هرجا پای پاسخ‌گویی رژیم و حامیان آن در برابر جنایات غزه به میان می‌آید، واشنگتن به‌جای دفاع از قانون، به ابزار تحریم، تهدید و ارعاب متوسل می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435987" target="_blank">📅 21:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس، روزبه چشمی، امیرمحمد رزاق‌نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قایدی، مهدی ترابی
🔸
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علی‌پور
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435986" target="_blank">📅 20:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5abfed34.mp4?token=qg_DSxUJdwk8ljq4nfdYLg3PnbrPJrEpLOpa8qItAoruuI4nqOq3CbHEe_Ai7Dgfz2_siRwvf5gszSUwNONGon2ifFnozRbfsFDHN3e5x9JgJH8aHtxBJJA0DQJt6bH--b3orSYoVHbfQqdKKXlledUelTlhhOMB5s_qJsDr5No4nUzq827-zUUHoPjCpgjFzmV0gADe5s4USjrAZ9g-tA873bIuEcPnHnBT1oVeP9lGME1ZbMUF-iHDyFDmXKYEYiK4iuu_PmIvlliLybeAWJi0OPXIha3aZGu1wo405dL5HnFOIaMmHZP6ZLglLQZNSww2eMmCZ_nBVnicgvg9DHxZE_-4d7MbfQH1weOIWMI3y18DaqDysJvDBh-ygZ_XM0CVf-0uAofHGktmzpYaroVnbBzZtWSYQV4KgSAIYO2yjYwwQn3o3HtgDcpSEBR5hM98wYZBEpc4eAE7fmL4PeeHbhslKl133yQgnhBpwGZzHC9Z3qUd6PUmY6WKZR0Zb9fZMVsniMs15s6hxoO7lGzPBce5jHkF_keSTOiz4J6cL_JgSsfRsr4wVAvW0zbPsqnQcQa0FgG6MarM_uLKR0EeXjScr8lG63aBrbcdNUYjTycaUseOUks8HLP4ov7O7MBpay7EMVz3plHI8ysDU_wgokDi9zlhwH7KZMD2I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5abfed34.mp4?token=qg_DSxUJdwk8ljq4nfdYLg3PnbrPJrEpLOpa8qItAoruuI4nqOq3CbHEe_Ai7Dgfz2_siRwvf5gszSUwNONGon2ifFnozRbfsFDHN3e5x9JgJH8aHtxBJJA0DQJt6bH--b3orSYoVHbfQqdKKXlledUelTlhhOMB5s_qJsDr5No4nUzq827-zUUHoPjCpgjFzmV0gADe5s4USjrAZ9g-tA873bIuEcPnHnBT1oVeP9lGME1ZbMUF-iHDyFDmXKYEYiK4iuu_PmIvlliLybeAWJi0OPXIha3aZGu1wo405dL5HnFOIaMmHZP6ZLglLQZNSww2eMmCZ_nBVnicgvg9DHxZE_-4d7MbfQH1weOIWMI3y18DaqDysJvDBh-ygZ_XM0CVf-0uAofHGktmzpYaroVnbBzZtWSYQV4KgSAIYO2yjYwwQn3o3HtgDcpSEBR5hM98wYZBEpc4eAE7fmL4PeeHbhslKl133yQgnhBpwGZzHC9Z3qUd6PUmY6WKZR0Zb9fZMVsniMs15s6hxoO7lGzPBce5jHkF_keSTOiz4J6cL_JgSsfRsr4wVAvW0zbPsqnQcQa0FgG6MarM_uLKR0EeXjScr8lG63aBrbcdNUYjTycaUseOUks8HLP4ov7O7MBpay7EMVz3plHI8ysDU_wgokDi9zlhwH7KZMD2I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادر دانش‌آموز مینابی از لحظهٔ شناسایی پیکر دخترش
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/435985" target="_blank">📅 20:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97746987ce.mp4?token=ThJEBb_F8n1iZURdMKgxShrFmIQ-CD8ccoiw0qPsXeYN4TcjrDa0isHdXMNYer1Ozs5sbJdPiP7H_pWHtCEeAupfBA3c23Mz13Fd4qSxcBiTLtXS3H6OVtNHarSTuJMLdzwsqeBY7FIB5UQdXifKNpRo_LoVWbAKHpAvU-ObX36THlkNAWF1qCucpdE909RRxAHeoT8sDkPNWg6SlQc2Eu8gKxIhSKJL0gi9Owil1hi7cbqL8Tm7Sfp5nWk30qx4msFcZ1v8QtZ4M5G1XjGJpTEx4C3ruDWCCgFVczx1dhNiBEkRVi3QKh8M-5516_TQ_U7I4ASNvCzfdT73WjWbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97746987ce.mp4?token=ThJEBb_F8n1iZURdMKgxShrFmIQ-CD8ccoiw0qPsXeYN4TcjrDa0isHdXMNYer1Ozs5sbJdPiP7H_pWHtCEeAupfBA3c23Mz13Fd4qSxcBiTLtXS3H6OVtNHarSTuJMLdzwsqeBY7FIB5UQdXifKNpRo_LoVWbAKHpAvU-ObX36THlkNAWF1qCucpdE909RRxAHeoT8sDkPNWg6SlQc2Eu8gKxIhSKJL0gi9Owil1hi7cbqL8Tm7Sfp5nWk30qx4msFcZ1v8QtZ4M5G1XjGJpTEx4C3ruDWCCgFVczx1dhNiBEkRVi3QKh8M-5516_TQ_U7I4ASNvCzfdT73WjWbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دفتر شهید رئیسی: کوتاه‌‌آمدن از تنگه هرمز ظلم به دولت پزشکیان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/435984" target="_blank">📅 20:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae639e1d5.mp4?token=k7pegYwmNaLgwn1ang9_HGVDR03yOPJBnxx4VPWtyOkuil6Vh1j7pPNyYNPev3nfrtyL-FzT7nm4YkFplHLtM9BwkuAgEDy1b6_sNFtwN1rBl04YBOJZhYnfxqNKbXCZVtKo42kYIyb-53nzl87hwFPasILnJt_faaQW0EcrruUY3QOtLEAVy5Xo4ZANHU5vWV4Yvk84QJFe8zg-SR6hsENhhI1MlvBN5bsIWDi5Fe4k64WXv1VXjnSyl5HBPCu-WWqHsXSma-Exm0horLFnAss3LN9v-bhvPZzG9p_ijtQYgPu50hR2gjDL2OTmAbiKY24u8jqeuqt_4ejfq9FMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae639e1d5.mp4?token=k7pegYwmNaLgwn1ang9_HGVDR03yOPJBnxx4VPWtyOkuil6Vh1j7pPNyYNPev3nfrtyL-FzT7nm4YkFplHLtM9BwkuAgEDy1b6_sNFtwN1rBl04YBOJZhYnfxqNKbXCZVtKo42kYIyb-53nzl87hwFPasILnJt_faaQW0EcrruUY3QOtLEAVy5Xo4ZANHU5vWV4Yvk84QJFe8zg-SR6hsENhhI1MlvBN5bsIWDi5Fe4k64WXv1VXjnSyl5HBPCu-WWqHsXSma-Exm0horLFnAss3LN9v-bhvPZzG9p_ijtQYgPu50hR2gjDL2OTmAbiKY24u8jqeuqt_4ejfq9FMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435983" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">زلزله ۴.۵ ریشتری گلوگاه مازندران را لرزاند
🔹
دقایقی قبل زمین لرزه به بزرگی ۴.۵ ریشتر گلوگاه مازندران را لرزاند؛ این زمین لرزه در عمق ۶ کیلومتری رخ داده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/435982" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
اطفای حریق در انبار کارخانهٔ روغن موتور مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/435981" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfc6325c4.mp4?token=n7FHrgpYOk-_ebXRT672gARIDoIGPd1_fVFrUDFb-KQdh-vCcuv5EHtEMl8ONLkoCMIR6kIvK55VwxCpVU2NeZCCcxnSJDnutBQbu5l9CecLfUNrM4m1LANUYU5KgTSxVddWlChi1D-WSVYSRL_RBrAUGcNih4UHkIVGAigFFoj64nq5JBByxsYT690rmR0E6rY1MeDAtGxbPAHyWH7W-MQZyq3GdCjJXFfFC8UKrvkn01DR-5P7ikfu4NpUFiO3RDLpnYIXJH9ynQefwK3h36ZZ9b0LBRl2gARsD5M4hykmeKSC7a_Vyp9brSEgtOWNo-DbBwl8uOjotjujG60PX25NAXdWAsPJn-xSif9riEc70R981oMSI-OONP-PPq1tx7fbU9VGzNebz6-zUfOl9_IOJ82PCUyW81V07sIgE1_Io9aaW1K29iVZ9rh1i6OSYXSzn2sVorw5vba8ZgTLcsfocQjQ6I-3cwCiyYB4gOSgcfJdaCzfOBJVMNy9EA_2uFjk6zcOc9CPJPdEjvQUdQ1jSJfoaeZ71QxoEdg-LWxmuP1J_SceSmCAo-APur4lHER7-PGFiIg64RFU4ZeYA-IuBoBmP8kXZF55WJmXWcmHKKCICLG8DHQAxWqDsBgY3aYeO03zJDD7fiBnq-Guulr55106KH5d-cluwor01Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfc6325c4.mp4?token=n7FHrgpYOk-_ebXRT672gARIDoIGPd1_fVFrUDFb-KQdh-vCcuv5EHtEMl8ONLkoCMIR6kIvK55VwxCpVU2NeZCCcxnSJDnutBQbu5l9CecLfUNrM4m1LANUYU5KgTSxVddWlChi1D-WSVYSRL_RBrAUGcNih4UHkIVGAigFFoj64nq5JBByxsYT690rmR0E6rY1MeDAtGxbPAHyWH7W-MQZyq3GdCjJXFfFC8UKrvkn01DR-5P7ikfu4NpUFiO3RDLpnYIXJH9ynQefwK3h36ZZ9b0LBRl2gARsD5M4hykmeKSC7a_Vyp9brSEgtOWNo-DbBwl8uOjotjujG60PX25NAXdWAsPJn-xSif9riEc70R981oMSI-OONP-PPq1tx7fbU9VGzNebz6-zUfOl9_IOJ82PCUyW81V07sIgE1_Io9aaW1K29iVZ9rh1i6OSYXSzn2sVorw5vba8ZgTLcsfocQjQ6I-3cwCiyYB4gOSgcfJdaCzfOBJVMNy9EA_2uFjk6zcOc9CPJPdEjvQUdQ1jSJfoaeZ71QxoEdg-LWxmuP1J_SceSmCAo-APur4lHER7-PGFiIg64RFU4ZeYA-IuBoBmP8kXZF55WJmXWcmHKKCICLG8DHQAxWqDsBgY3aYeO03zJDD7fiBnq-Guulr55106KH5d-cluwor01Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری کمتردیده‌شده از شهید سپهبد موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435980" target="_blank">📅 20:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهلوانی ستارگان کشتی در میان مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/435979" target="_blank">📅 20:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGJyRGFgEkM6BYw3Tt4w_8_TEJvgTqonxU-MnXZRunwH6_cbSXLwaTx_NKXDFn72QUfKnKrJzZ_Nd-OFwrX62SIaB60_2t1wAIWVifsPLjyp4ya-jjbcdrRtOOCWJSBgNhPkC8erKdaDlgLLvU_NHrHg9sCTkQ7TAamoMdFSswpsrK6je5voAkvt6oG39N1hGts-8RwI4EM4UB5e5VG7RG_j-ol90dxydQOeT-dKwNGe6hJIATv-OiRMUQUClH4cfsIXu3PqASpRIVV9EIgzHjsww9U0Tybof5V7W757l8sH9HR0wq4ZqZwyxuKpr2B50w99f4-SqqBFNXDJVZPxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: ساخت‌وساز‌ها در نیروگاه اتمی بوشهر از سر گرفته شده است
🔹
رئیس روس اتم: «عملیات بتن‌ریزی و آرماتوربندی ساختمان‌های واحد دوم نیروگاه اتمی بوشهر از سر گرفته شده است. متخصصان ما که در محل باقی مانده‌اند، همکاری فعالانه با پیمانکاران را در چارچوب تعهدات قراردادی خود آغاز کرده‌اند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/435978" target="_blank">📅 20:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_MkoY1Ran_XQOFcT42LlckLd85yYBzLxjCfbJIexakQqScjgflpdia_CUtqjJRCstSSgktpWPgJYzVctL8oWrNek6W09piG6FMOvpWWuV3LBaiodNcQCOkUWA_whuYvXFiDXHPTLa5Hpb5skD_L-5UGqIQEqu_7XUhNEsM-7FnKmAjSb1bd2JuISFVEyRXy-VHml5ZLQi4iyg-2D8AbwqvkOS21zcvAWHEAspOFbujw9JPkGBedql0zyCEXPbu--J-eiBwzFS67SptuJwKbNIih4mnmNq5oUqkk_m9_EzkvP66V3fulz2nfL-un44vKnaf3N2D8V3BcZlNezeDt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHrUJ-q9lnjsXVEoh5lC--hIperwCNk4-gfcqqjFIjKz-psh_oJZbBG-lkbLCw0MDtKY8aKAbmjyskKIEbnTgvz2bjUtypT-aoReJT7ETKv1Ng4IzQmweqI2RhUlnUWkv6C7iwIWtkNFne8CBs4QNwHKV0jdtNSuG9H5KY847jJ4_O1AoJHzArs7cFiEkpysCyCbb3EyoJY31R_HOXGbC3D3VwIADGtkyZokWcX0EpFPZawaQUd3cv2YO-D7dzKzicTAK1MmGd82kAT_NfnCTmcJMCPXq50Z3pgElfMrZRaZH2QWAoWjp3EQEflXphNxarFCIG--dCIu4LE6ughJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sATRFv2-CDdhUamYmjckxkwZz7aQVZhP6Zc5LtTCH9SGfIJ3ZwZFhHlxwGmH-3EoB0HrJvPu67VUg9l2XHUclF4NZKPIcotq-4Q2d7iNohQC6SsnrCFSPHRCHSSLyzeb127C5moyKIvhe2896KqvBxaxOcMI6cpOfd35LNsTGuQpy5GXDwXmn8resJehAxQ1tI43c20NFwOQl1LullRUi0uJXidFmed2BCXCbobiRHl_CWao8Ch81GzBlsLelevw3fwdVYsSQPjxOZb22cg6kTXBj883N-C_tVzOqNEVrwzg-x4vKvs5M1aMnQkfslJgPfMsN2fV3mHUvHvBRP53JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caRDaADv3CqjBl3GEsbfEn1KwkdV75Wz41K7uEjnrHnCCPs5Wn0ZF6VF3d4t7zTH79aQtHMkPS37A5ayGm_XHMDKeC_CBElfJC6aiPoanrrkSw0T5BydDmQAfrt0y0WHY3KxH3PiuF1uVR4d0llHLjcRVmLVHSHFCoaQdqv1-uw2xETzzOkTJJPGbo04KtjqK28Hw6aFDzX0muQ6gidoNQ2q_5qgAqdCCSwO5Ru-a0ItfrA_ViqN4vpJZxER5lNtDwJmuaNDbTGW7aIHXywL2oOJbC6Bd9oXBJwjBp_cq2D10V2taFsi6EYo_Nyr4e8VcufOB8QOZ4FJAS7QKsZcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzGXX0qWnDOXsQ_aur9DC59bvY55pNVUfuT81AbBlAZLSisi5My43l95q_9ODfvI5gyxOa4SuliKLKrjN0zUed50MaugefXi7pToN1cbu8WfcqCeeWAu03haBLbj8TBHspGl64PVkl4vFcoWtggKWPK6QTfcE99JPOaG2g1J98Lj-n5r4oj7bbnVy3nhYRSrf3poWAg_RKPb3f0tWDSws7gYIje9HDGj8hkEcJZ_5-Il6EBOy2DKXM2Pg7p-e84Kea2Ntccjf-FoG72R1s543aO2I6qJEoJrmfRAeutIOe2A18ZpkzWONE7G4FY96q_7sNHfz8mxm32tCxAFiXyIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzDtauggh3zeKR3HC7AtuUieC4cH5ixUWfzm434vN8tmdml8FPnYiH9aiu82vLkh0-JF8SEF5LRYxgx8o69khmoHdZwZ5MTcDDmMe7Q_i0v-HubLkrEtTDvMDkDsy16p1JVNTVekqYpOwyIcOMXf1kyNO8yK17AJHoq4vs-Fb0VT5eg0bYX699SaQbHnMSMIbTInQvIy8ucQMDotlAirobtKimJ2N-wSC4uVVgOAdz2SyXjzOQJ33WSKUgKj8iBiPni0hN42-ytLDU2pQiSJ27wpoVDTdaF-gJiLTO1i09yJYfxtNbskC37p0_sQaU_2dayHzvO1qWhXrAW9krKkIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طعنۀ تصویری هنرمندان جهان به سفر ترامپ به چین
🔹
سفر ترامپ به چین واکنش اهالی هنر را نیز به همراه داشت که البته همراه با طعنه و تحقیر بود؛ برای مثال، کمال شرف، کاریکاتوریست یمنی در سه تصویر ترامپ را تحقیر کرد: اژدهایی که نماد چین است با یک فوت، ترامپ را به باد می‌دهد.
🔹
اکونومیست نیز تصویری منتشر کرد که در آن ترامپ به شکل فردی بدبو (که اطرافش را حشرات موذی گرفته است) در حال گفت‌وگو با رهبر چین است؛ علی نجدی، تصویرگر جوان عرب نیز با تصویری با زمینه پرچم چین، ترامپ را پشت سر رهبر چین نشان داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435972" target="_blank">📅 19:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این روزها مردم دنیا ۲ صحنه از ایران می‌بینند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/435971" target="_blank">📅 19:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk3wpqTw8uZdOtveQxOuo-3mEVp-BJTlPMViIJb9-ijLYGG14vBLeACWcSu2QsiPe1KgnDOlFSB10BBKbDGwW8qaG47bbOWFSdBwOJfnVdxOHBpEg7OejQ9rE8bLdsCIX7pPwQNc-UxM3kBI7Qx6Nz8LxCAIkMkggPu6iCg_4CFsyBj7-_KP5HF0GJ2o3cIVLfE67zaIk28wTmkAog-3yk5DN5btGS8q00bHVCRQeCVGVEYNXIV8R-ItCktlexhlWXNwjbWwwiGOFqyiUz0tA1d_QHVP8WubEom7viqlifKc2lVvaCZVW2UPfcLSoMlMqH9RVSPRe5n3dPIIcPobaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: سرو ۴۵۰۰ سالهٔ ابرکوه ریشه در ایرانِ کهن دارد
🔹
کهن‌ترین موجود زندهٔ آسیا، سرو باستانی ابرکوه، با قدمتی دست‌کم ۴۵۰۰ ساله، در سرزمینی ریشه دارد که در همان زمان نیز با نام ایران شناخته می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435970" target="_blank">📅 19:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزش باد شدید باعث گردباد در اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/435969" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435967">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/435967" target="_blank">📅 19:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435966">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌ ‌حزب‌الله: تجمعی از سربازان ارتش دشمن اسرائیلی در شهر الناقوره با ۲ پهپاد انتحاری هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435966" target="_blank">📅 19:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435965">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌هایت را ببند برایت یک داستان تعریف کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/435965" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435964">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخت عزای حضرت جوادالائمه(ع) بر تن صحن و سرای حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/435964" target="_blank">📅 19:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435962">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfDzm1HmzvVMoJm2t1aDE58zDIc3g-oVy3iM2ut4QZsZjOzvhafKgzbrMTsaSt_irpabC9u-Vgf2b5XbXff6fbtT0o7PWI6Zs2EjFZiHQoZKSBwDj9rDjjfYli5h-bK1-jCcPyz2hrSvFeH8_HAYSgchbzEiKt9Cklgej8veRFIJ2-RtMTP_mNTY--_1_9hl1iGWkI8oWvH6_BeFfquGRpTwki5311UK0jqOg5fIRdMOYqGB14PcaFZXnq7K-4FF1apDg2LD12Rhk2LafcTqpBvgKHiVIJ03_5RBD8HO2VmnNrocAdSxwxqWfeAnKAnOFVBnseZ0kJQnm2AVzsiiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله راهکار صهیونیست‌ها در برابر «FPV» را به سخره گرفت
🔹
حزب‌الله با انتشار تصاویری، اقدام ارتش اسرائیل در نصب تورهای فلزی برای محافظت از حملات کوادکوپترهای مقاومت را به سخره گرفت.
🔹
حزب‌الله در این ویدیو بخشی از سخنرانی معروف شهید سیدحسن نصرالله را آورده که او با اشاره به آیه قرآن، گفته بود اسرائیل «سست‌تر از خانه عنکبوت است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/435962" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqG68xyDFNSzpXW9v8khJwGKWiotzhHXsZXj1RQHyyvxm9xUH0A8gZiGjcB3K5ELiHZeR2hL_6WQSDORk0tCGGwdw_zKMOIRUppw2SdJeKXpx1gfjD2J3rg8wwu7PNKiFGTV8L6RUMbVgeI2sDh3vdNwit00BgyMyvC5CbRPC9cbjaGuqIS8_kOH0PozCWYOOlkyLKyj5rP2owb_VQKNYW4Xpw6koJmlh5I56mRJEyOSrjC3ILITXOAgFTmMOwO-_TspNsCbB8bIaBTqUWgwkZAToIwdNBT8DRwjhZ4P7eUtPLd04ztYsWsQRoxchF8pLQAjhyCd7fUWXZiXLNFZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8YX96WknMUmpHSMOgOmSj0bGMuuebRrmfYGj1J0MTsmssKLoZ-qWO_F63D9mzSDt6UkUxJKasTcmLVjBtIuJ54dplLL2yTtVbMbITnos0aRWVzVZiCxKZ66wOTUW_Oq_Gx5ap3N4by8c8Sdoz7fhDUhKWM63ZIQuwSpVpywNre-7KSlAA9vl49amMQO6ZVg-K1cErBHCpfMDXYj-W4U83kfoABPr1GzqnsEXAqoEk9xC6_Ce3D4VHlqiYQ7q_8dIczkAr_O9fJPe4MQ1-okjOX0B27lLkbpGD1ttbUOzOXHTqWqsLl9g-G2kz-Qxenl1CaVRC2MqXFiV_pBo1ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz08Am-AJDXsetI6pkH8wNt_XbIfv8IJGoydAjwZ6rSm45P5xOvUKo7VWvgwK1JbCzEWvqXqhGEHPBQjr_zo8IRiif1YKbpwUihJX53hVWyYf6OVLkGA6f7ZIrsSI4ynzHJBcH_fGo6Nd9OW_HZNP00uzYjTj3pk8w1f1ND37icjqSOqWzFGG_tisWkRVhSJnfaQKWuIrMpGCFajxpDVQFQo0Y5phXa3MCgtTyBhS87m_TCA8D8rI7hzymGTyqheStsEXxzLXg1HomR-SMH_khDQsa9goruIvgFit5eC2p8MWfQRG0VNnCOiTECof2ntCcSyXp40eD3-gMO2jvSN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRe1-WFR_Xa86tthnlN2wSBSfug-nllNfT3PYMSt33f25EUYdkQdirhljpmw27MgQOmjDzJim-DyCTj9nMc0HJ-U4XtdkzE4KwkgYG5scNA15EKFaKiOSi059lwvFPB4AGp2q2B2zBx-bSMv-LIEj_D_rqCMrO1vG2RkyG8L7SM_LDmcU_Fi14CtDnhGthFuju7Mcr1IYBMWgoY1tIYDnv7wLV3HXWoNsHxxnu18cv84k71qLcPfmcrS4gyRai9N8mo8MF6jF6yWUHLRkfBjhfkVVhO-9WJz31uuN9ACqi6IqGaETatEEbbT7nTsK97BHI6mPAXWXGUeBYTNcefDyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/to-aldTPZcWbZlkO4NvKh4cexqPsIcrvftrUsIvqtX_KwPF4qFM7QNDm0h9-mq64b5wWzTQC3qU9FO37gIs-zTYspx-ZCjuWnkiI_LdRmrG3pvbyVd7o0Ze3OFqffvGPQF9nirZVtBHm-6KEPVsaYeYabZeYu8c3YlEZkT0NrJbu739T7vmdFEZrMUvSUjSu5vvyYG4uFm451PzxARKSLaQqbnY1KGeZtmhQOjuY04mIfMlJ9U-eODJ5fhlgt05Y90JjySE5Dneje4Wi-Oh5A7fl1kT0g2fRdq9OSjhwhRkTFnIqBM0tHKrwnq21ZidgGpQ3g18BOv59kRj-jhss0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt0zuaPb2TcQnpYbXyAoYv55uu6Z6UJkHJcMKKG5EZiW8IPm4CyAMllQzMn4LniS5LHTKZ5jc-lGCRJ54GypvP48HJTF5fFPujrTYil69SgZGaoIGFmVkulfDWEfigxkHwN-3EDYoEYc2Ayr_uEoZ7I0CkIYtwRXF6Lsu1_8ZuK8MzoPWTAFuwLveJOow_fiwuC2EVBygCZfuosyQF0GN3svbhqYvHtM30vYcQ4VYKtVlKUwqv32j8QX3XisJSvXQjBLQz6vdWYQGY7Kb_iLpJZDxGZFHITJprV2m5UiTo63VoS4rt2tQV2Ymgyu4g7OZH8uSaojczxW3LG4QIJ4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrFYkYTZ5aGh-j4eDTHlup2ExiLm9zhoNwYi5Z3GENhEzm6jxmk7V3GyjtW3u0KTcvRw8lGjgYo1e0SUq9B6WTR7Jm2j6sskHk4f3EmWQymC2VD_CXM0bv1w3ohITRXtNdZDqhMiEIGtXT8ahAf3v8umi6PXomYVY-YDcq6qcA59KyUDcSKOWw78nadL2bN6LtrCdYWRc4Bq0oVXpIfNwJWm0QgANxNXOHiuo_fhfkQeqhBXaKzlY7WB9zcvI7KVr1H_lPGdi-LczTnvXxAKiBTT8oIDGZkMRGSm90GmuDpHSeTHkKsqg1oXSCV7YDlSPtsmjgMlGWUXhD7ZifgH4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جریان زندگی در ساحل خلیج فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435955" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsW9-4-b6p9dPMZ4yQMdJDIfJ4lEDG-G0xDkyf5Ql2mV_GiJEPRy1T6JC3QIUgcBVhQmAZC_SsZLq0M-Q6kA3xPVL3mX24nCJHK1PXxtsSMJHsHTLQrUpdCbcRempiP0Gc2g90lnw6tO6muKG_0485_S9nu4dtYL1NIJWYWnj971_xfs9fqMGUlUSGJDU6hdMuKHu-1lcZGLBJodCLSsOvD00o-nk2HeHor_RxWgPgUdn-j34fsgDT4vSrNHDJgKGYtCad4VhgYlVpVPYxMfjhf_xJPzsam5AvFHT9Y2X15tvek92M7d8M85vchcvfSA34M27u8JAnAK6-wMZePOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد  سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/435954" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@Farsna.pdf</div>
  <div class="tg-doc-extra">1.7 MB</div>
</div>
<a href="https://t.me/farsna/435953" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موافقان و مخالفان حمل و نقل رایگان در شورای شهر چه کسانی هستند؟
🔹
همزمان با نزدیک شدن به پایان اجرای طرح موقتی رایگان شدن حمل‌ونقل عمومی در تهران، برخی از اعضای شورای شهر از بررسی طرحی خبر داده‌اند که هدف آن رایگان شدن دائمی مترو و اتوبوس در پایتخت است. قرار است فردا این طرح در شورای شهر تهران به رأی گذاشته شود.
🔹
براساس اظهارات مطرح‌شده در شورا، ۱۰ نفر از اعضای شورای شهر تهران از این طرح حمایت کرده‌اند و معتقدند رایگان شدن حمل‌ونقل عمومی می‌تواند به کاهش ترافیک، کاهش آلودگی هوا و افزایش استفاده شهروندان از حمل‌ونقل عمومی کمک کند. به گفته موافقان، این سیاست در برخی شهرهای جهان نیز تجربه شده و نتایج مثبتی داشته است.
🖼
اما چه کسانی در شورای شهر با این طرح موافق هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435953" target="_blank">📅 18:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کپیتال اکونومیست: درگیری طولانی با ایران، قیمت نفت را به ۱۵۰ دلار خواهد رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/435952" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدور دستور توقیف اموال ۱۲۹ عامل دشمن در آذربایجان‌غربی
🔹
رئیس دادگستری آذربایجان‌غربی: دستور توقیف اموال ۱۲۹ نفر از عوامل دشمن به‌دلیل اقدامات ضدامنیتی و همکاری با کشورهای متخاصم صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435951" target="_blank">📅 18:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435949">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط یک شهر پاکستانی به دست جدایی‌طلبان
🔹
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435949" target="_blank">📅 18:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435948">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای سربه‌زیر شدن ترامپ در چین  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435948" target="_blank">📅 18:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnJh71IbW4LjEIsrKwOrsDWGqBUAsUs896ASWJjITS-cfNpqM0cgr5d-7X5B4GMS_UZHVJpzORwinWZn-3x9d-hiUP3CTOYS8MBsG7Y-5ZvN7I3cf1pQ4D7yLKA7mBA4GAsnpCkfKja8nGftdKGLHyjakInTQm22U5mkc2nQN-YFB5BVY6-ORwxEtCI7qsJHsvjkPPF5w11mkIg5tqca7T_jJcpFYuaXKq48GxP_sUzL3osnYJjlX3-vaae97U_qddJRfnh06hMWXUkwk0Wb_c7prMO5Dj36JYKFWj__QgIicxed3LlAi0Hl6KKogzpdJJtn39hK0m8N6HRZ-OuG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLlJBpOqHSLMLSmFceiIpzKgk8mpCQzsi3CdEGZuYikpFp5lhEF_ZQ2b1vyY9lcpZzUAzE68Xm1n50mKooK-loTHRm9nMLcHPgTO4SjCvb32IO5JSPTK8JcJWE2u1wAeLomiWwXkR5rr54tdbAuA7oeKfbuoCvjZjQ4rtlCM7883eRqHp8iO1QuNEmhAjmht4SxQwCxqA9vRx-rLYwfWqsiDCL9WAwRpSohTGn0a293PtXwOkfMNZU8NnDJaQAoD8hC1zc0SfLI4s8DrKIYxeS7dD9ZyeXTqOYoAMxxzrva8vy9tsmAhr20VxfNX4O7CmWh0qkjdqDPw8H_NDcNHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJYydWuwxNlv7fsNDs_HUUpow-D1lVcw7cO-Gip9a9JEkhs2pUuQwNLgIHSkE2RYIChGBaJE7hqDW1GuDBESBZdJYPYtiEOu_vnhL8HK87gfbYEeY5soa8mxRJQPNgRECJsnlAfca4_I6xJsMCGCaeUfHwCNQM94h9p4pV4JKWfkBqj5Vw7Ny7KT2ceU2bAtNiRA7wh5xBkFbGThtRMGCu78x3iD7211_RI2wSFZBhYAfVtuMDkLdFE_Mm1giAm57cRXAqTeD7ZPpPInDeLzw3BrVepYQA3uhKCh1FHLbWnEN6-zdipSNjpen49LQ33rEYk35HecvcI19PMg48IEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrd7XNNB9bftbpHJ8ZUYDtuDTMAK3-iLKBk3veFptJfbEbLlQVLUmB7paTUigYzcRy3kwXquAer-lCbQ7c5G3YygeSBUuggzMSPh58BVy-NkQNOlbNy9P7jlcNezkKfg-f4V3wwe3I8zMiLk8P4gPtstBxTGhJx7EHTNVN9ciMginJ0EMmxNssFxYM2kOiipmQUHQAlquMKFVwZ6YoOStVOUvgtCupTTZA99jIciIh4yzPV77czBuf7CLUK7UCcTo6KAZ6SJ-v5qW6CyrT2EVnC8WKq1RC1OD_pnPsTaqnjoQ7c3-kzQTWyGO14rHXCFsFpLRIXvMMrvlfruEcEFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGsoiLw5IlWg25iUZyTMHz8jjpTQBOoe8XqQtHvFyXKnukVULQsNxLXU-ABGSyoeQ2Iw7D17PgXxFYbzTkUJNp5lXiEmyBHdM7GrqIKAGx7SZZU5q0kXsAdKVKZH21zXGlxmapUdBcxQreBkEFi53bF2SOb41FZyV_8mnr6DDgJ1r92PcXlOQXOPNBLcE9lR2Yk42yXg3v-9N6JaDttUwf9pCspK5MuMcQ9O_Owvly2M2RdoiPoVswkVq6_i2xNE1MZjBS4SRy8bSgQScFyWsbOvnolZCuB6Qm7fu39WuhG7_WL3DTY0Xu2yk4LKUA4ux0QC07KSbqnvixz3dCwbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRACJDK27nND3NM_XmofSEhGiTuU7Gt6q15ccwq22482TwcH5J1JaEs1mYU918YMiErb09OnRvWS34mEZ0dH8RV-CUmBLsghWdluQzrFEB2BsuhxdpvYWkO-QNfHXcc3bi447UtvfsTcLsmvKcIbZpZS96nzY2uSYbb9zNsfFqOCQgtSVHbisDr6BjkaBA6a9yRZ3VAe_-e6eunMCZe_YqnIyBUE9GMw_11FQ-yFkqou1-H4cK_D0r4GmKd6DQVERdHqg7apAafLcdNlA0WnC81Lu1e86IW6_TuJJOvhuk99Ixo84_knNJfImBFWwyzUjAQKojIeIlGx-FHELNL8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkdR2WYttbH_dib2MlzG87nsaX4jypLOC6ZD4KMZ2tO2IiK4hTXDHndhcd9DEVRDX-VgaHliL8OLurZrPIKXFvvv3H3PD0I2NLTAQ0Zh_FSIBWix8soW5-LCMzKzEhVa-xFuneVxnjf6bvYW7V-_jxiYde4GDNHOXm6tr8ml0VRLQccaQH1m3AMoRBOTG2X-DPlknUOJhaOnaUoELGM933IKgNz44DoEppVPefIRdwjHMzQ2MW3Cg1qheqyVhWpDHZhD8mi0QNcOG65CZZsPK-hJTDcUKq32rLsOplhO3eGlN8S3hd1DIhIm4o9HHEt6nVfsCRE0FxYdBw626TXKSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فلامینگوهای مهاجر میهمان بهاری بوجاق گیلان
عکس:
یعقوب رخش بهار
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/435941" target="_blank">📅 18:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به یک بولدوزر رژیم صهیونیستی
@Farsna</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/435940" target="_blank">📅 18:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435939">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-37.pdf</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/farsna/435939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-36.pdf</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/435939" target="_blank">📅 17:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va2922388hGoouYqbApRzFEbsy4ZySDk1YQE6pspASHnUboUZqdXf6VdzXYR5Kd0zEmqR5MDXAlBlmj8hONqkCA98RMU7Zts6M4k6ZuCQQ3HkazVYVGXNXHwmB_wdOoWZ7mDwHMjFSd41You7JzrLEPSwuDgl1f41ya5IcgHZQzOqQPpi2Mwx4MtIpAKXNe82kv-alrIYMI_c0cQnFU8QHWDJT8b2u2Juyf50PCrrG6hoeEvp1tczzKxuxMwoqDVCEPP_fpWfHf-WTjL6SAyg9Ggju6_gGkrX2K1Gm-Gbm7MKbTpxktK_RNN2dz6Avyc1S44EU0WoZ29_3wDEQuSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگردانی ۲۰ هزار ملوان در تنگهٔ هرمز
🔹
حدود ۲۰۰۰ کشتی با ۲۰ هزار ملوان همچنان در تنگهٔ هرمز سرگردان هستند. از زمان شروع جنگ رمضان، ایران کنترل کامل این آبراه استراتژیک را در دست گرفته و قوانین جدیدی برای تردد کشتی‌ها وضع کرده است.
🔹
برخی از این ملوانان حتی وضعیت قانونی خود را از دست داده‌اند. شرکت‌های کشتیرانی پوشش بیمهٔ آنها را لغو کرده‌اند و حالا دیگر نمی‌توانند وارد هیچ بندری در جهان شوند.
🔹
جکلین اسمیت، هماهنگ‌کنندهٔ دریایی اتحادیهٔ بین‌المللی حمل‌ونقل، وضعیت ملوانان را با دوران کرونا مقایسه می‌کند. او می‌گوید: «در کرونا ملوانان ماه‌ها در کشتی‌ها گیر کرده بودند چون اجازهٔ پیاده‌شدن نداشتند. حالا دوباره همان وضعیت تکرار شده است.»
🔹
این درحالی‌ست که سازمان بنادر و دریانوردی ایران اخیرا با صدور پیامی علام کرده تمامی کشتی‌های درحال تردد در آب‌های منطقه، به‌ویژه شناورهای مستقر در آب‌های سرزمینی و لنگرگاه‌های ایران، می‌توانند در صورت نیاز از خدماتی نظیر تأمین آذوقه، سوخت، خدمات بهداشتی و پزشکی و همچنین اقلام مجاز مورد نیاز تعمیراتی بهره‌مند شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/435938" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435937">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ هدف‌قراردادن یک خودروی دیگر اسرائیل توسط حزب‌الله
🔹
حزب‌الله: یک خودروی نمیرای وابسته به ارتش دشمن اسرائیلی را در میدان شهر الطیبه هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/435937" target="_blank">📅 17:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435936" target="_blank">📅 17:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahp8cv6NXJo916Ywu7yVobAfzzDQbqa0RUzfECPP4TbfkX8VSz40CldadQdOcv9wOiWA2fZ0wogRoex1iZiPA6Gp5X37zrHrNC_txFjx6FO2IriySsJjFzopxN62SRJWFGkdyBpPfeC2QmjxPvVRyciO3hgAZsHqs3U0By9LOiDtDKoT-X_AO5e2y34c-5Oc1-OBTzWXxhlwABgK2Nwr6topA2PXAkUJyjB6w8sEMslpD3H95hzQcdF_-8OOVIIXm_E9bYclCl9NsEtzqrT05N2foZqSL4-ZAdY4-JmPidwtB9kOy0d8gn4Hpa_8LQ0z073IMb-eJjkmPeJtV5TKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYibfWk_xIdW5uwkcdWRq4NSpvGzQ6nIjOqMbkgm5ohbLE0pfCCtzuF86sabJ6zq20nZdq5BUHjrDME1Hquk6CNBCgghM4NDtYqPxUAvC8-TNjNxwnBchblcahB4kzEiIntSp4MtPH4KaQNTNChiHygl2MLKH9hwpDVrXig_NxOcNs0PUuTVamtbjor_f_r-MRqNKNldUmLxa0iPmZctYlyj-Jjwon8peTZJ01Q5s4-dwcSjt-z0YuViNLdG-fRL6cowB90z2q0mjIiN0w-mCNLETOyAtoDvYP6npuVg3kZyIL2S_knRcXNrF6N7EIcecv7rfY3DtAbnxF7faMRa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh8YNmetgxsH2d5VRy2UTQWhdNnAUivqIiBipNGNl8LPxE-2GjterFxa4cEWseuKgNNzQpE3XEfgpWlWvl0ROy7FPklAcsOShKwQm6ErTIaro5uo-Uld_9CoPWCrDIz_uqti9OLEd9AY58OC4h5eB1r70LhA-euW9nc7sosu5X8a5xEqQhsInLUFEDdjWurCNAb-LzgahJbwu0lfHoeaTxjYO3xVqII-oHPnP8w9iTeyb2CRQSH5df-SpDeinWLzJL5SV6KY4QqDv01xS9q0qnvBmzeKBNx0084vudeFSRXXi7XZZQlcygHoUiduUSAC79D5ffj5oBD1AE1DJN6mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4XexA960kwiNh5QeaeGtiOjoWE_5Q3uXbCP5s1bfs0RJEqgL3Mo8uZG5lLiLvPzVpvQotA6pQabk_sBWC4b4zjX8cp12cJDjR5wzedmP9003K6HPLDXpGW03lsgDG3SihUzdMyWqtw0YW4_zVj9Xw8vH8n2ZfGVNqvUsh7p0T0tFdgHG_CFwJV61-qHt5KT1Gbd2ZLlC3_N-m6STm-xEw52E0f3b8oEwVTcgDbNoPMgyHU2iW-7kNqsGUw1VF7gez9sbXo9z1eVdqtBENAPsZlXRle_xbPjYHcwyiPM6zcJ4u3Dpc3dmCvjw08HYHKEfcCxraO9C_9IKvwiLlQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmC07ykMHqXlEkrQyyGMgL77wdkA1CVbraWfDSz2r5WZlHxVSb2XcGAR_sfb4XLii6ehfCrhOeHm1SDd5LeD8B_bsLaDJ0NNevYGCPMQPoHkj-aKdLoeL_0uxulbTLp1RdavPh0Ko8lbLDt4gIbQHPt21nFnNdEQQK6LBYm3aTNseeKvQ-TrDiu2dDK06Tuv-62mhTt0-ULFyH1nSo5OoufV6E03sgcb7d766P-Qpwa5Kv4CfBnTK1Css8TV4FpJRwZooQUsB1UKvvHL21OcoGznQsCz50o4rltk_7twi4-X9AL5aaqjb_G1NwmqHW2f5ouHH7TycSFkr53d9ai_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxze38A2L8dc7Ojj4EVFolKR9eDa9Mc9YafPEO-OP5BWSaUZa7tQ1oii_BgZWUev0GYnw6e4WXMZ9oiObuQuIeBO-ar6eQTR-Oc4umqhhtbyq02OGSqrBbodj-uyz0shTWNeN-ATt_GK1d1s14b7_oxVb7NIB_qbycIwSO5Ra0Vu8rlEuW-_kBbph95HsgRp9aumyxoHpylHIrjq_nuDJ-qWm5OuoUScaVpnMNleICV8LhTTQBd8tfFehQ9FXaaWek9C_lO9-j75K_kWDvtqflJmWVmQxMIC0XHAIclgXc1VpcXbUbmQ0ENhsDUpel6ew2jWJ5gOBnBI2nVWv8GL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh74LciT7Pxf6nqKlfHau0DrUOzwXEl0lXzuYjifeJZr4HnHodpa8aMNblaNZ0qOPZr6UC5mvZkud293HY8bRYkeYJfcj82l4pokGiCMcDeY1KLBYRM_BkKEF9jzexWt1mF4mtF4af8tIP3U_bFTkLxldHtZ-KMPJDAy_jvs8-tz_BZvoLy3dRCbnQesnrLbxvtYeuDxAUX-cj9SMvO7_LFqsDM__ceCpHniOYG15TSpMiYXNAaInDiKG9Tpt9gN9_XflMj0d-346j8ROkur_wiQMCinaGFtZVFWN48hwQEMA-n7rJYUb0floF2F90wVo9C74nNyH5jq4aAfV1GdZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اکران فیلم «نیم‌شب» روی پل طبیعت
عکس:
محمد وحدتی
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435929" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/435928" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه آمریکایی: دولت ترامپ، کوچک‌‎ترین درکی از تحولات جهان ندارد
🔹
کاتسیافیکاس: باز کردن تنگه هرمز برای آمریکا غیرممکن است؛ درخواست آمریکا از چین برای اعمال فشار بر ایران نشانه‌ای از درماندگی و ناآگاهی از تحولات جهان و فقدان هرگونه راهبرد مشخص در دولت ترامپ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/435927" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1MLmsfUJielzYvJ3gRZk4iqBMyW_1BQxf2LUAOXoJfbJbJKO42SwrOtMm2R-4sx59WJh0Bs1I1e96aaDEEd9zK9iqW1Wc7lO8jRfkpgDeh2xCen-t4fJMfy9defHBhhBgPT6jg-P7aRrBNMkKU0bCGCgJwqzXs3pMHUiT_c-h9EbbMy2nZpGcBWEbcVu2fZO31QjF5GOcaIThMMNBmUosPAyWnKLFljy9wX26YCm87t2kI55-5fRWISzMKWsMAgCbIh0qJvZ2077KzDMAKac29UTgO6bM25JP6SfrTegZiTtM3vJGoU_RO5XAslIPT55Kh8Xma-RQrMYNBPP_qjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGeaQFdHBtouF6yElUEhEGxU0FV5p6t57wHhdaFhW_5FJek9uB96xl-SGTct7sV2xqPoaZSt9OiUkqq6pEb6SVtc7w5kr6eV1IzfXJu5sS1DYAktslXlv5LkTIGaKkJS9xOI3kTZcPFWtN_RefTH6YMQdXLcDvE3qoFxquraEQjqheEUvg2lzcw4_zUIzuxQ1_RBLJgb0w76gThmwmPcAOFrtjScxoKgaz7Zq7CwrdS_BxyB_vqRzTqcGS1uQDl9cRtSSUXNHn3Abu1EHpVjxGXPcNx9sAxy2BRWkKoKGZDNZJ9Wh40nXFBboFhtkqvCZl5eBLSfsAA9qW2IZXWYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4PW2ZXlOGmscMbXuKC0TEtdEq-fCM5H378K48AZfSHs-O7YA_vS7vSHOIY28xEo-_-DQOIlUo7E1h1pP4aCYLoIVV3AibnKhxY7zR1CZvuPkc5q1WjKylNzAQ2qo3D_xL0U4F1bRyJxhibA9fXFfhLKAb2WKmG4wpddZI4MZlUjOzZQ-29voO-IJtdTCELtKPSKcAN4j7Lp8OQRFxJFazrs4i7zuFZv4Q4qSiPoyWaOgQPz70OEC1eMjvyC66pfSGWNRsTxspZerYKEZKNF-ymSMbOGeNPr22Anrst2lTTfhQ8abgE3alAE85YuViejx0sVhXIsQxhMx8DhKEEhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSoDtG8MULu-wKCeoTuKnAlPU8sBR3Ria5gAiuwlmJaWGd6O5fMj5o8w_nRYqjQWwvpUZdCNv-m80G257AKIhfvQRlIBS4n2hLZNAAg1gFySIs7gJFJnT-Lf0BxHvRcTwe4aNSNbQ8xCz_6St3_L6htg1xqO0_tGrbU0wLn6P0XMpPj6FIswHeBkDtnrNpOTPkXi1QUiJo2H33b0FnGXaahy7gnvnVm0FZfv8y0tJJ2-fT_6N_HypS6ivONzhKQ1m4W83BmR_mhveUvu_dyayXz9xXIwSH_smDSIW1cEnG8nXCbnO0E1SA56ml1yxvsg17cDbWO9XnUImYkArs8iHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e83XnV0Uwd9kyS7cTyhSdcwqdbJoIRRNWC95wbAqSTfoewpgJsyKmjNNvX-nChZvxXvANcx1OPym23YH20_UO38esaOTI-kqQWIs4SeGRUxuleot1p7HhGBqJgogm4Uf8c5G8-V8cmwyn4PJMN-30dnCVdY0woHj-OICrKQT73dT0iMuUfTPiuwCoGdpS8fHxrSSMpmQwUCbrj-Dap_-KgS8j1PLwfzzwS4x71v2tarYTvyfjB93X_iYlp6ChW0Qc9W67z78kbgC7TejYvw3h4-thebl8D2X1sJorDdsGYs3MPtt2Y54D3rf2GjiZq6E62Uyx1raxKN3Sdx4DVK05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaIY-2m6Q0brlfNRYJx9YUXK396Hawk1IQYnwjX4odv11Oak_AT-hnE4JpPGyMlXxLdevGyBe4iuvrRqcp4TQVOEZXznWNrkkfusoi9VmFeO9HS2qSzp9_v3PK1ItzMp6L25jngKzQ6SH6dyi1I56YFVeLVz64euV-VaaGhtPswCjdY3Nqkdpl6dNshBtIzbBi0ZjRfRN_Qrnf7PkfrVega7WlCXAQB9apy99OEn97lCoohfGzBW0rVk3n5BxJQ3Y7Pj_oKyD1OUCKbyf48j7LrsJJedskFhIy7LPdMRCIrXZpop20I1OC3CqbyPyAc1CF9UMSRYEFBEDwnZsFis_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuLMNE-wTKexAwpQ_dgGPod4WqjrI3xMSB8kLy735skYp0_kA7TPUQlSJVunkssQvF22EfW82uOsUiP7pASxdVfNFrwiLaOUh3TRe9pvcnQ7Ug3mORXyzdJ5b41-99sFXnP-x3RLpXMg3bSgfNyvovrs4oVIwaOaxss3HAZ6j3OfxaCSDKYo9wf6X8_LU0fJarQ_FkB10JZNkoSsJe5dEVztr76-97ghuSkMXi25s4c8CKNZCDnvJdaZxfB6fU3JTBbffSVXDekEKTSPfOabCap3qZUTpDqNtoVcbOXnPS4A73zOt8FMQJd8TeqMFSz79hRm1J301qpEybP2pkTnjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله رئیسی
🔹
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله سید‌ابراهیم رئیسی و همراهانشان با حضور وزرای دولت سیزدهم امروز در خبرگزاری فارس برگزار شد.
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/435920" target="_blank">📅 17:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwNbqLOXOPX16QkO2eRgrA-KBxKyNChCRx1uELhNlH-FhO-lBDNgC3uriK-fqytr21IsF18tz3gKbo-6i9W_nzox7_cYhQWxk_Q2Pi7imsEgVm2qsUP47rryDxcNIunGjfnDbrgo75GxFAYJX8_IF1NOgxIteVoh9DWK1-sKaWuVq_NFvxlqJvL_UOzt74onU0ajA2QutmQOQQ-Cg4KuWVTiqX8sTjk4Z7BQ-U7imRqitUpL8_QfCtTbR5-dDlKDkmm_hd8nF3TKSDUZ6DjIz0Cq5bCzypJMvpqLmu8CyFLhohcQW5E6bZPwemPMVP_PVNuMCqpz4lbNg16LG28xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار لوازم خانگی در شوک گرانی‌های پی‌درپی
🔹
بازار لوازم خانگی در ماه‌های اخیر با موج تازه‌ای از افزایش قیمت‌ها مواجه شده است؛ به‌طوری‌که قیمت برخی کالاها در فاصله چند ماه تا ۲ برابر افزایش یافته و فعالان بازار از بلاتکلیفی قیمت‌ها و سردرگمی خریداران خبر می‌دهند.
🔹
بر اساس مشاهدات میدانی خبرنگار فارس، قیمت جاروبرقی که زمستان سال گذشته بین ۱۲ تا ۲۰ میلیون تومان بود، اکنون به حدود ۳۵ تا ۴۰ میلیون تومان رسیده است.
🔹
قیمت ماشین لباسشویی در بازار حدود ۸۰ تا ۹۰ میلیون تومان اعلام می‌شود؛ در حالی که همین کالا در اسفند ماه سال گذشته بین ۳۰ تا ۴۰ میلیون تومان قیمت داشت.
🔹
فروشندگان بازار لوازم خانگی از شرایط فعلی بازار به شدت گلایه دارند و می‌گویند نه خریداران و نه فروشندگان چشم‌انداز روشنی از قیمت‌ها ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/435919" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جادهٔ چالوس مسدود شد
🔹
پلیس‌راه البرز: جادهٔ چالوس حدفاصل کرج - شهرستانک و محدوده خوزنکلا و پلیس‌راه کرج، از کیلومتر ۱۸ تا ۳۰ به‌دلیل اجرای عملیات تور سنگ مسدود خواهد شد.
🔹
این محدودیت ترافیکی در روزهای یکشنبه، دوشنبه، سه‌شنبه و چهارشنبه از ساعت ۰۹:۰۰ تا ۱۴:۰۰ اعمال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/435918" target="_blank">📅 17:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان با استقبال همتای ایرانی وارد تهران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/435917" target="_blank">📅 16:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435916">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه‌پرداز مطرح آمریکایی: واشنگتن در ایران کیش و مات شده
🔹
«شکستِ» راهبردهای آمریکا در جنگ، حتی تحلیلگر برجسته آمریکایی رابرت کِیگن را هم به اعتراف واداشته است. او که از جمله حامیان سرسخت سلطه آمریکا بر جهان بوده، اکنون معتقد است که ایالات متحده در ایران…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/435916" target="_blank">📅 16:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکاری یک اسرائیلی با ایران، بدون دستمزد و به‌دلیل نفرت از اسرائیل
🔹
پروندۀ یک فرد ساکن فلسطین اشغالی که بدون دریافت دستمزد و بر اساس نفرت از اسرائیل با مأموران ایرانی همکاری کرده مورد توجه رسانه‌ها قرار گرفته است.
🔹
«احمد دعاس»، رانندۀ کامیون ۲۷ ساله  متهم…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435915" target="_blank">📅 16:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انسداد مسیر جنوب به شمال کندوان
🔹
پلیس‌راه مازندران: از ساعت ۱۶ امروز مسیر جنوب به شمال کندوان مسدود شده است؛ حدود ساعت ۱۸ از پل‌زنگوله تردد به سمت شمال نیز ممنوع خواهد شد.
🔹
همچنین از ساعت ۱۹ مسیر شمال به جنوب مرزن‌آباد به سمت البرز و تهران یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/435914" target="_blank">📅 16:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScuAbZ7mAUDRUNtAl-ZdUt7-2_QaccBkYnCNO5vkNehbGyzISaH2uUcyJaQ_VStyWzF4QGj5dfEZrdmMFaoqy5LJVQdjO8563Abf3Yfq_LvVh-Q_eJceWd5UEeH6aK67nAVsla_-j47jGagj7sHifJY8Fhlc7LSt5XHokjl6LQ_bMWd_8UdSNjNCK8RI4GXPEwawB6j69UeHU1qfcq_EGrQGJJ7dB9u8RaM2Df79Is3HUAAkU0dgz2ygBVNUHjVpC4naD3qnmpDmeuTRL5ccGt-o0xXuPHBt8hXVt_JypjyVWK1CeX1lKJ3CKzVxqDzuHJD29rYTFQ2BGFPYyNvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری خبرنگار فارس از چندین بانک نشان می‌دهد که اغلب بانک‌ها با وجود گذشت ۲ ماه از سال یا پرداخت وام ازدواج را شروع نکرده‌اند، یا اگر شروع کرده‌اند بسیار کند این وام را پرداخت می‌کنند.
🔹
یکی از بانک‌ها در پاسخ خبرنگار فارس در مورد تعداد افراد در صف می‌گوید: «سیستم ما آمار در صف را نشان نمی‌دهد فقط بانک مرکزی می‌تواند آمار را ببیند.»
🔹
در صورتی که پرداخت وام ازدواج به همین روال پیش برود نه تنها افراد در صف موفق به دریافت وام نمی‌شوند، بلکه تعداد بیشتری به سال بعد منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435912" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ book.icfi.ir آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435911" target="_blank">📅 16:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلیل امارات برای خروج از اوپک
🔹
وزیر انرژی امارات، در شبکهٔ ایکس نوشت که خروج از اوپک یک انتخاب حاکمیتی و راهبردی بر اساس چشم‌انداز اقتصادی بلندمدت و تعهد به امنیت انرژی جهانی است. این تصمیم تحت تأثیر ملاحظات سیاسی نیست و هیچ اختلافی با شرکا را منعکس نمی‌کند.
🔹
امارات قصد دارد تولید نفت خود را به ۵ میلیون بشکه در روز برساند. خط لوله‌ای که میادین نفتی ابوظبی را به بندر فجیره در دریای عمان متصل می‌کند.
🔹
حتی با خط لوله جدید در ۲۰۲۷، بخش زیادی از نفت امارات ناگزیر از تنگهٔ هرمز تحت کنترل ایران عبور می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435910" target="_blank">📅 16:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435909">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6643075c39.mp4?token=tmQQSTpOn1OjQHh4vYHQailIgTrMgfx-hvyiZnI-ZKw0DY9593CSo4J4enZeHkpvh5CKHc_6L55gSBITXbhMgwY-Y6wyt6sorWnzTMR_rVGUvqIbCvhB_Mcutz54OxAhKa32fMMbbPmyfHY5YgEMAjwYtFIAp_tM6te0-1KW3wisslDMGgttFZIQSfEaljqyWfvpbYDYyYXZ2ro4ERDcP3BhkIh2JgvCPyOkbdlp6gxT9Ox2cSWW6aRb9xZZ2dwA6hWeQXtK4Gw_KVQvb-MVJm9s4zg1q2Nw0XbYyVXY_Y44C0vS1L8Miumu-DlWNEFoi40wsMdCZPrlfqc9_ltIdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6643075c39.mp4?token=tmQQSTpOn1OjQHh4vYHQailIgTrMgfx-hvyiZnI-ZKw0DY9593CSo4J4enZeHkpvh5CKHc_6L55gSBITXbhMgwY-Y6wyt6sorWnzTMR_rVGUvqIbCvhB_Mcutz54OxAhKa32fMMbbPmyfHY5YgEMAjwYtFIAp_tM6te0-1KW3wisslDMGgttFZIQSfEaljqyWfvpbYDYyYXZ2ro4ERDcP3BhkIh2JgvCPyOkbdlp6gxT9Ox2cSWW6aRb9xZZ2dwA6hWeQXtK4Gw_KVQvb-MVJm9s4zg1q2Nw0XbYyVXY_Y44C0vS1L8Miumu-DlWNEFoi40wsMdCZPrlfqc9_ltIdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پانتا، رئیس اسبق سیا: انسداد تنگهٔ هرمز اهرم فشار فوق‌العادهٔ ایران علیه آمریکا است
🔹
شگفت‌زده شدم که ترامپ از انسداد تنگهٔ هرمز توسط ایران غافلگیر شده؛ در زمان تصدی وزارت دفاع، از وقوع قطعی این اتفاق آگاه بودیم.
🔹
به‌دلیل انسداد تنگهٔ هرمز، ایالات متحده درحال تحمل پیامدهایی سنگین است و اقتصاد ما آسیب جدی دیده است.
🔹
باید اذعان کرد که ایران با انسداد تنگهٔ هرمز، اهرم فشار فوق‌العاده‌ای در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/435909" target="_blank">📅 15:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435902">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GClt5GQlCl33_JngVQkWE4uOPuNLCvVSYzvDEXzNYIVMZ-Tn_k6XEs68CN0-KuXl8xgFhH95i1zLHexcR8G6mKjjrZoulrEnbnPamBsDl_zHiXQkpKjGyfpr78CXIgITo1YvxG9kgSaBOEoOL6NpNN_LEKfxTGFrAuxKZFdnF_0U8MPIeJIARU-7d26cemRRREn-d5goRQqt-baxGkP32Eyo173oMUg_aMDre3PEupTO1bZoRbHAB2snOfA9Ly3wFqbKDt1Iv16REihRp-IUvZK6Cn7h8x8rj_8iwZ3iXNRNSPuBcqGJvBqeNBxmkFGKU0VGCtc-oQZm2zPykjUkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTY3LeGjKZPdeo53iigiO4h-od-MpZA3FILUyBWFD0UitavLfvIQW7hXqEVPiNQIxh-xiS3U7DFF4azQFaEybuGSAEgHE7MizBGsPoM_lKDOkvkaKUyP1rHsgIFnsgD_6yNzPAJMcFViU8Wss0HSHuTtf14vM6hdp4h8zk4uRoWBORNAPeF6ShOg5e5EkvQpYJoKgxCZxHccRqn2woKwbtVpX77fPPcYGvZca2u_5Xp5be1Xw1SYgjoEMfmaYbyEUhLEvtNR-k7GrGfEiqdd_ApIBsPqSuOS-G_HtzF80Fx75h-QsxzOEVUVxJemxHBIH4IOjEa23aEkODT8P29-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYbj9bLSbB_dv3C8WM0E5Hh5cUY8mdDlNe1paSMtmtqTerZzEKekfTjYjwkLJJzYMggKnokdSFY49zJGDD5MxMYhaPR3z8Xhom-NmLPRabst4mc2oWoq1dciejTvGDzHMsW7jJLHAruEKxh6WuEKG2w6M-XLqWziQkyvbzLVwuXDIaDUszl06UdOW5b-iUL3SI2uYK4iA1BqrC7NQ7FMAVAO52e8G3yeq3TolYQFq_PfNIy5-0EDoaL9LnzYBfoXLbwwJfIs6doGHQntkSHoT4cCprcz63viWPvEaH57Pbi3YmiTwcY9_Ic6c7oY6F6ooji7q-G1ZL6kCWWJRTVaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-QO0HP_vA6aDulpTUm6FWtO4R4mFoWIbBTeoWOoFy8ilTVLiJZ_MuZDFW1O7n1LSQWEnIMxsdgkBQoOPJeLiHiXtN1wsdqQ-o64JVnNCkXDlmD2M01vnYkdJh2rfbw0sU1IrhKCghncKeQMwdGLsI70hlzgpo9NNIJqDSiWlca28jimI1gqWrjZ56xQLnzFeI27BJNWpKvlXOZ7BwVB1aL6d8J94aAOTO9QCNNs5nJEAmWWyZ5_D0u46nIzhNU2Pjrc7CeuXEiEKCwI3_z_jdSIM3OpGSk7aCZC5JFzyQ3EClPH7r7uvRdj14D2-x3oSkRuGPDPsQcS_583OtMsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuZZsWh1kUZjQKf-NLiC2Z8qEV6-XVWo1dt4lpgcLL-pxMArlEOkvSx53vVJIrjTeK_8NtkiRYpFCpburKorPqdLS_vNTTG0yDK8367EGuUQZJjE8eyKoaDNXALGUI_KekgoNjYrd7986gIjZG-MbvQKt4qdqVqwNjT9VBONMREaAC1XMcqN26JMvSkfJrVpDcP5DtGEUk_plPCdv_Q6gGJWAEMFg5OgXllDhCT3OdmgCWTO6eBQnUq8dwKnb3UpolBt9Mcdh9Vnp6IgYWSwEKBu8dXDcF-CK9Q5mNVYkdvCOWw7MuRmBzEh5JZG8YCknzMNJnIbH0qAGc2NXIfmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdXCFrLVhmCdQoayspH_6BrWvdlaWBCT7rHhcPewmS-wVmNaI5k_lov62QZ9sKWrEh2ACzNFlKVnTAEbDK-0bIBs-JCk11gF4eWJM5Q59Em6OFnrggU1jnIvmEXs-Z5B7sjorzeJZ0ZQg5JPu-suU9_FQnqlFoW4dL0oBnm1woCNKkS6ScWMsVPM-2VZHi8iV8IaNPlnydy_t2mWHLPTRmLoOyDKMFR71pLINy7Rleo73D08x18IX8_ncMxZSBa9WmvcNq6vRUPLlSA7eAT1-aTZKiHj07wpCRLGPZ0J-o7tU6K6re8gkP8y-PzbA90C_a-CDmvISDdZXO3mvLCMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNbYKHx6OlSit-GDpAXCTcKUJU9lrRunjjKfCsi4xlpiocSlziTgdTpfA8p02geYfazZJUBxdYOioyUTGZ-QHinjCrSDiRyJRuAv8eZOv6GqB1paRIi3tESF7ODrYfE6C7oAD82NjiMJkM-_pyLqrhEMme17jqtF3Ys-LHeJSNxEHAqrySX8ULeVCnpTiil_zdHOg75H_sQaov8S1ETjyWMDO2dU_aLOXiGieuD8Qqg4TeLj8A7QdDODsVHDkcdR6zJiZrrykFuh-u0clC0Fbfq2BPxoGAKUzaAZi8C6y-fXZDeGHhv4f3FNlMawhOeNSN_P7gDS5xqKhQESBIZ0pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
صید ماهی صُبور در سد سلولی صنگور خوزستان
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/435902" target="_blank">📅 15:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796c415e0e.mp4?token=uuYvtUmkR1VtUuXBKut_IRKryta1GpovezMS-ZAb_Ao-2rI2-FbRl2vH5y6U3_5YG3rWmoHm2zT6hCEFflupGoDcaUjVj1RM4VzcO6GUWHjdNphACzhUnxxPHg6KnMjou3Gw98jXhTUDGe3LgkhBukmlKzFwMkkn_ky8Os2vDVvxW7kf1rbu0aCGvpLV89OT9gHEp6RdEbU5HM8NDBHsB40U1uzwr44Kz9kVxASjCEHRqbj4Ol_UP6RxB35ZjxNkkfzsbQcyW85QYJYXzhFDThwnr4itXs4kRX-keNaHVdhcN5PptD96MwYr9hU1KRK2iMZNWC9JhIfb2mXJ56smRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796c415e0e.mp4?token=uuYvtUmkR1VtUuXBKut_IRKryta1GpovezMS-ZAb_Ao-2rI2-FbRl2vH5y6U3_5YG3rWmoHm2zT6hCEFflupGoDcaUjVj1RM4VzcO6GUWHjdNphACzhUnxxPHg6KnMjou3Gw98jXhTUDGe3LgkhBukmlKzFwMkkn_ky8Os2vDVvxW7kf1rbu0aCGvpLV89OT9gHEp6RdEbU5HM8NDBHsB40U1uzwr44Kz9kVxASjCEHRqbj4Ol_UP6RxB35ZjxNkkfzsbQcyW85QYJYXzhFDThwnr4itXs4kRX-keNaHVdhcN5PptD96MwYr9hU1KRK2iMZNWC9JhIfb2mXJ56smRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/435899" target="_blank">📅 15:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435891">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور در دورهٔ اصلاحات: مدال افتخار موشکی‌شدن ایران را باید به سینهٔ رهبر شهید زد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/435891" target="_blank">📅 15:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435890">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIyymL9L8dfx4PdBZgArmR-AzwRqxBZoObn5CLsgXpAzfE5JKjbCQu7ziA6lqZUZavglIGSxutXwYad-2o2LY7ScGuxx9EZDeVz1DQJkbd49r1WueeOmNCcwi61iU2UdhrnHO6z3RbVvCkM-O0EJJP6OuBrqXY9Yz3xJniUBNTA7cHkURxtjbWxc09OkEGpI9lGgMQ2qVVVH584Suf2fPJ4Au-hPSp5gLKxIHSs15w-Vtw3VrEDXYmsGubIY5-MIJeLfqp3oOkHRnJ25ce0wj0mbsA6zKxgLyDMtoP9e5dRQiFQ-Z5AhF_nhEQnpjlOn1wPhoDiTjWLq2XyOmwAIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
جزئیات تسهیلات ویژه بانک صادرات ایران به کسب‌وکارهای آسیب‌دیده در جنگ رمضان
🔹
بانک صادرات ایران با هدف حمایت از تولید ملی و اشتغال کارگران، فرآیند پرداخت تسهیلات ویژه به کسب‌وکارها و بنگاه‌های اقتصادی آسیب‌دیده در جنگ رمضان را سرعت بخشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435890" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435889">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S66AEe88z8M89aai-FZE-FzhIFp95i52TXVXIp4YQqq_5s5ZSYwY5g1_zR4PfDqJ6CrIYcMQS1rWsidMg5zY4GnjDi3cwJt0KC-KII6LDozQ0b3VF6Ufw8QKO4GWsUop3iznnhd5F2RkeZybW55bqkPdalRqxvlRXbYKCAwoXYrjoNxjgTMsAUJV2UrrBdnP756b7qp-s57x7Pq07A5drOuxttxD6cEBizLwTPyhkQ9UZXpQbkfvjySJt3b68D_YAzLLy_d6oMjuIRX2ApLyNXnGSLsxoQC2m-Tn9BEBYaFlK5kHWhzFgVblhuLRtqwclxTyJ-DIe3vcf1pPV98zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مس دوباره از ۱۴هزار دلار گذشت؛
🔰
بازار جهانی در تنگنای عرضه
🔻
قیمت جهانی مس در معاملات اخیر بیش از ۲درصد افزایش یافت و برای دومین‌بار در سال جاری از مرز ۱۴هزار دلار در هر تن عبور کرد؛ رخدادی که از نگاه تحلیلگران، نشانه‌ای روشن از فشرده‌تر شدن توازن بازار جهانی این فلز راهبردی است.
🔸
مس که اوایل سال جاری رکورد تاریخی ۱۴هزار و ۵۰۰ دلار در هر تن را ثبت کرده بود، اکنون از ابتدای سال حدود ۹.۳ درصد بازدهی داشته و بار دیگر به بالاترین سطح پایانی تاریخ نزدیک شده است.
🔸
تحلیلگران، جهش اخیر قیمت را حاصل هم‌زمانی ریسک‌های فزاینده در سمت عرضه و تقویت چشم‌انداز تقاضای بلندمدت می‌دانند.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QK
@mespress_ir</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435889" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435888">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/435888" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435887">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف نفتکش متخلف در تنگه هرمز
🔹
محمولۀ ۴۵۰ هزار بشکه‌ای نفتکش متخلف به مخازن ساحلی استان هرمزگان بازگردانده شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/435887" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین خبرها از تنگه هرمز
🔹
پس از گذشت کشتی‌هایی از کشورهای شرق آسیا و به‌ویژه چین، ژاپن و پاکستان امروز خبر آمد که اروپایی‌ها هم وارد مذاکره با نیروی دریایی سپاه شده‌اند.
🔹
نظم ایرانی در تنگه هرمز هم در مبادی ورودی از جنوب جزیره هرمز تا مبدا خروجی در جنوب جزیره لارک همچنان پابرجاست.
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/435886" target="_blank">📅 14:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435885">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABb9s_vTfuHu6R1yt2oY0H4iFAOeUimzjerK0JLQKr0Yxqnkq4wPeNVwA0sFkJOp7Jp4kc3cxaVxVhX7zNuBBCcyF9wznczkJXZu84ZLRtcs67iTuL9yviIlVN3BdilHssNrtENVBaj9HSsgr_0wP4BK1HBpjVuJxO33PT6TdkQC2npxcy_4TQgD3cnsGWqR_sVvY8kVdoeL1hKAqaE2o5Cv_M6d8hAG8ujWNpsOcHS8wtPgFDU4sHtUdHFG1_nYgsOUXjiv0GCxTmHTwhmMk3NMQ_lC4dPR_v98JVEgSq2EOhxxZJC04DgsRFxdCXYgF1TKxuRC47HqJJ-jt-LTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب: این خویشتنداری همیشگی نیست
🔹
ایران سال‌ها به چشم دوست و برادر به آنها نگاه کرد ولی آنها با پیش فروش استقلال خود، حتی خاک و خانه‌هایشان را در اختیار دشمنان فلسطین و ایران قرار دادند.
🔹
پاسخ جمهوری اسلامی به سنگرهای استیجاری سنتکام در جنگ اخیر تمام عیار نبود؛ اما قطعا این خویشتنداری همیشگی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/435885" target="_blank">📅 14:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435884">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQrUSVddRLvMzpm0h6WbeRR1xm5WqIGX4FzNrIGT2q4oTij7voAJh8PA1G25lweykGc9AVNVNGTeW51IRi45pyv5n7w3acpgcsw6T-hkqyM_-SY2699yJFWPq2M2BVaJcmWk4jJZ45CGfOucbHU0ldAnVu2ZoTg3NRuwatn1Y378PPO8-cQgH9yAoJbdQrhYq1dCiv8uoOtEJayDQHD8wVM0fppEWuB5okR2jMfEBKw6hKEtGfe_cm079M7wAK1V_ufWdQiMvOHVXTRYYLeeNhEU05U_lsmLGB7D3XaiIfrT61P4LTxqlbPrGfH9SDCuqu3VMskjQZMrIEkjIyi1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت‌ملی مجلس: فقط کشتی‌های طرف همکاری با ایران حق عبور از تنگهٔ هرمز دارند
🔹
ایران در چارچوب حق حاکمیت ملی و تضمین امنیت تجارت بین‌الملل، سازوکاری حرفه‌ای برای مدیریت ترافیک تنگهٔ هرمز در مسیر تعیین‌شده تهیه کرده که به‌زودی رونمایی می‌شود.
🔹
در این فرآیند، فقط کشتی‌های تجاری و طرف‌های همکاری با ایران از آن بهره‌مند خواهند شد. حقوق لازم در ازایِ خدمات تخصصی ارائه شده، با این سازوکار برای ایران اخذ می‌شود.
🔹
این مسیر کماکان برای عاملین پروژهٔ به اصطلاح آزادی بسته خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/435884" target="_blank">📅 14:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYVHWixb6PK2D5tj9GpGE6gLVVemjTfFl7CQKHCLL5FUcA35pU-GwmaQs6bY797Fc2VhYrWMPFiQi6aRqvB2K7eGwluNzACWpNFpaKTN2WXGYQ-w5x-zknZtxdHSjzno_pzJKNV2f1YP5Z6cFSi_5t5mEgTPeJRY3FnrEOtGAVSzmYECnLFBbpctL9Yd3XzTAvZg0W_8o6XmWT0VqXeAvQqmTAdrq5HCVZyrJWEDw25r5BJD2bds3Sb0YnYy6f0MYFzO1kJbVowDX60rmacZO233xsPQ-EWJ1Ea1nwtcerPwcyaaH-ja7QCHuYT01OMoR5TvocmiUlviJMOrluSGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVJSl79NZJS1Rl4GuQ5wzR6PJo_3bS5oZZbJZ2B02Rx7cM6NlND-7Nfn3RTSeTydWvJXP01-wwY-_oinZbVoGZsthhpcCcLUMcLG6Nnn2BnynZ7jB5Mar2hrZZKqk0ZacX4yJ_5377xUhI02UCaN-P8rEkepktg4V0FyxGeeAppjRNIz-1fviOj_B6lmbG0jvtlkf1g0w-fxy1PfyjJsaQkfdeiMoGmZfDt2bnu9aL9uE5xTxSlqX7o40-j1DP_qa5PsDXk6NK9HxzR8_LAShZzJOqre5PauqKz0Zc_hOeeF04Cly8IKBuIi97Whox8V3gm3zD3m5XBgZZoaAtQdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLgjFIvO_wNvpB83bHJPC7TmzuvJBEhB7jkHK7kb3NMQo-bSDKovL_onj8BBIywZenkq6pZ-IFnlo0EXM9uSMRRSjUCRu6oqbBdXGLBgZjggEjDVTwlacBR7pcfrklztoXqlllQ5F5vQD4xAq1P2Sw3ZQp1y8I2UTX0-XAZNmHcERRyplnDfEVzHPslHBBStHXegVKZ2pUambJEpWi4Sq_p8NpMriS6eEOjIeMmTpIdshx9IF_bXqZwMvJgSsjsFACNLqqksdZpUMxPuDOEeL7ZI1A53x6Uhigqd52dLudPpDEGhz1PxiVQkmJEuz1FUIN8kfAWMDEHE8D-3elNRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0JHpTciA4j2qVaKrENReT6g0EyR_TL8NQY_bTi1brIKwaTOgrQSxHq6Nz8TN1cg7tHsJjUfRMtW_yzEty6mMOf2A42a23v8RY7U7m5ZtNezaslUDX9S4bF1G4MmUzJs6Vd_O0QfGvBo9oaCzoqZrD7ls6aW1_livDgKVTmmSs7hFyA46Qwju-LLFbLvIYSzxraK9Sh8rjLwkkdHu47DoS2VFk7cpfRW83l4tabZ1Ht6JY100bWVg4c7ThrXSlf0t9wXqegbL0RecvuW3athMdcdv41U4mOqJN2N8aoP59I2XI_2GmumAeWj5M1aHC2cBDoo80qf4LlqKHycm6fGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaCJjCYyl7_XaNZ7PCyGXx5Z-Noxtj5ZyrjDpFwb9QZJ18z7_rhcHFSCLRIohva-m8cNxUzCjjnuYwZmaLkQK1TwK0rn2NA69f6_LxypHUiY4XDSGqIpsfg9AaUG1rH7agl5e9mQmxpUDBCXzleI5CcKTfuA2zWIhAg_XU_GPXP6_8OnhDRdGEnHaiGSQ_Q0hXA9VanHrMVV5Qr4fpUh17aIwVVpjyZKbuj97M7R7fm_qxBH9eWHpec_2Q4ImQ3BybKY6BbjCcawSwcXbew38AMzOu9aUx-yqSl5nRPThwqpE6booH8pusQPoaoSflUwzeMqEz0qd-igarn02z4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQGAQJ1V4wz1WEcCi7JKyErbKDC3oznXk5m5SC0LrfVY1w-XRnMFTFfaf7g7Hx5ZmQBOjm1MNaqtNp4YqXCWu17A4zKJAZ-56dPaCndMhRffkatkgFZ7TOoxPlbahJBK3oM-jxqS2jqPTW1A0yi2HLMueckcPcPYGW7B3TsrSxEt41ySqN-plLfGSwZ-G2SD3HP8DMG5kBrYSwdGrdu3J21nSlAGc63AoPAYSItI_X9PRI1bLm7XzpHGSMGg7YzS8qbNbDKmkP7OO4fiS1qTWX7b7-RqiUuuCwlCJKo2NX4710ICMw-5PGvHg3JyfW8-pAWlsnkOuFQOPaPJ-h2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYkYr-NWO8Tf-rZWMupC67YypKPkIMIb6Zy74IitfFMVoaMc__-1MBjWBaQ3whqU0s6qSXmph5doyu39qhoRHfS7wSS5mi1hHP4G-6pVhVxEP_5KIsWfzYefuueKex7Sjxzr4nvR0WckJQXorrURtuaiSzeWO3cgbHo5xtBWNULF1HbjCabxbH9vbX6lz3OoT-V7J3n89oW0t_N14Cb-wLkquECM2R9n-kxgRw84q2stMdmpl4SXjY-IHYnDSy41LM4eys9GnIm8bY2zEZuExddKcVT5A_X_ilU3MolzyD414GZPbB7mfr1c-WAUgVwAidb0_ekhaTC-Ti9UprkdnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیاه‌پوشی حرم امیرالمومنین(ع) در آستانهٔ شهادت حضرت جوادالائمه(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435877" target="_blank">📅 14:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در شیراز
به‌مدت ۳ روز
🔹
روابط‌عمومی ارتش فارس: عملیات خنثی‌سازی ‌بمب‌های عمل‌نکرده از حملات اخیر در شهر شیراز از امروز تا ساعت ۱۴ به‌مدت ۳ روز انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/435876" target="_blank">📅 13:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdRcLurr78cVtVPZVj_l_dsHpIsy4W2LWzJxZkfJ_yHHc9f_Qj2gxOz7AcsGlmBld6ZYwA4tfQO7XCakWraSDbKJ1cgu1I6iRV0puFocv4Mm4E5Q7RTjDiCTfox_vtBBLB9MrnlaTiJFVR82UXSRVFPjwpzo8upIAFyaRXqWp0cRBDQMEBqzfwx5znT8Jp6v098giqj2B54TQpDTSZY2acLnig8A774iLEhpJmfAnGBslRxKnABlN_8yj8ryexZMczc444LeGTugtlhFONxR75lZ7TAekk9W1MV89jVZ1qMa0jmhZN6Ls57D39biEHmunrnOKh5BCWDYdPmRs5qWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌های بزرگ روسیه وارد همکاری مالی با ایران شدند
🔹
پیمان‌پاک، رئیس اسبق سازمان توسعهٔ تجارت ایران: برخی از بانک‌های بزرگ روسیه از جمله اسبربانک و وی‌تی‌بی‌بانک که هر یک دارای دارایی‌هایی در حدود ۴۰۰ تا ۵۰۰ میلیارد دلار هستند، با بانک مرکزی ایران و بانک‌های عامل کشور حساب‌های کارگزاری فعال ایجاد کرده‌اند.
🔹
این بانک‌ها از نظر حجم دارایی تقریباً ۲ برابر مجموع دارایی بانک‌های ایران منابع مالی در اختیار دارند و همین موضوع ظرفیت قابل‌توجهی برای توسعهٔ مبادلات مالی فراهم کرده است.
🔹
اتصال سامانهٔ مالی ایران «سپام» به شبکهٔ روسی SPFS باعث شده انتقال ارز تجار از چند ماه به حدود ۴۸ ساعت کاهش یابد و حجم مبادلات ارزی رشد شدیدی پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/435875" target="_blank">📅 13:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m72PdbE82vtuDTDAxaZgz2ifDzqqgnmL8cnCGAW-2JYa4w1uZDV_7cU-HG7azhuFSQinuzyGubTQ6CrhXRKQVlkTBY3h5Ew6zzauyZC3pqDufu3juZgOcLjndo9EwyOOw5CtFKeZeTxvGTbb_F9RzhtoSRpjCJMuRJF1hVt_qy1LOVrBlQxp_2drkB9yqB0TC_KG4eYiYBhzqBMHgGO1-D5fgzcLf9sgQjncH49J0ST4RPTUDjMOxNbgR0dk3g-zFBVaNBgjBPy84DKAcTQQ2pDqpNMT_NIcaWdTAu_3237E1uiaN-SDifck8ADkPFNE7qUNSt9lHcNPjU5Z5_tkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاتک ایران به محاصرهٔ آمریکا با مهرهٔ چینی
🔹
یک نفتکش غول‌پیکر چینی که از تنگهٔ هرمز عبور کرده بود، خارج از خط محاصرهٔ آمریکا رویت شد.
🔹
این نفتکش پیش از آغاز مذاکرات رئیس‌جمهور چین و ترامپ درحال عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز در کنار جزیرهٔ لارک دیده شده بود.
🔹
حالا پایش داده‌های ماهواره‌ای نشان می‌دهد که نفتکش «یوان هوا هو» از خط محاصرهٔ آمریکا رد شده و آخرین سیگنالی که ارسال کرده است به روز پنج‌شنبه بازمی‌گردد؛ یعنی زمانی‌که ترامپ در پکن حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/435874" target="_blank">📅 13:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU7GznrVP4Ac3WkBY8cD5PbDAkpIPlHpusB1cYD5v2G041Cp7x45HEIaCujdbOmHLBTJwGd-Pil_6jIFSDzuu2bhzVMuSTSdY525iRnUCI1Zm1GC63_V6tOOX2G9gM2W7ggG1R9AgV6V_WQMUqVgtX8AKXq5GBhWxRRYTKWyh7lT-YVF-09JkK8hR4zEp0q9ii1A5PoFTRYkLRVd65BfLWyQ7McIWCbolYij7vHajgWmA5MVnoNMkhzizLUzB0rYqm-JJLySbe1kOmJFF2T1qOnjiJu7iQ0jvCGOG0G8SboHz4SkgDeGdmc-gHYopJmKEItmogDIyc_kYGrcXGybTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ، تجارت ایران و عمان را ۲.۵ برابر کرد
🔹
باجلان، فعال اقتصادی ایرانی ساکن عمان: حجم مبادلات تجاری ایران بعد از جنگ رشد بسیار زیادی پیدا کرد؛ به‌طوری که در این مدت از ۲ میلیارد دلار به ۵ میلیارد دلار رسیده است.
🔹
بعد از جنگ با حرکت خوبی که در بحث مدیریت تنگهٔ هرمز اتفاق افتاد، حجم بسیار سنگینی از کالاها از سراسر جهان وارد اسکلهٔ سلطان قابوس، بندر سویق و بندر صحار شد.
🔹
عمانی‌ها نسبت به ایرانی‌ها احترام بسیار زیادی قائل هستند و مفتیان عمان در زمان جنگ به‌نفع ایران اعلام جبهه کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/435873" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P583t9P1AHP4fkOeyfudQV8DnenTu_mSiQvyTaQ_XcQq_gDOxjmkxftOdOsYFVgYmd8809IsO86qsT-qGEoRk596qievSZA68Loji-CKhW1ruMy-QGQ1Fa3igqP-M81V8Bx4YFZkhGO4YTHtdTPHtivzb-ILMxHdQsao9P1Q56woyI4ym_FKD82nh3qgE0t3NlJ1tpLWRPvYR51X9zGwV9l88ZypSadpOLLWYBrMv8jK1CsgnkuZRAU-EexZZJpcmc1ZwW5ALKdA3WSQnILr962aId9l1XZVJqbXxNAQJDv5_aJq6PctHEkpWPFXFJJxajErCL3jIQ9zEs0hsnkR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماموریت ویژۀ رئیس‌جمهور به معاون اول در سِمت جدید
🔹
پزشکیان نظر به ضرورت فوری استقرار حکمرانی یکپارچه، منسجم و کارآمد در فضای مجازی عارف را با حفظ سمت به‌عنوان رئیس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب کرد.
🔹
رئیس‌جمهور همچنین «تدوین و اجرای…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/435872" target="_blank">📅 13:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: شهید حاجی‌زاده، دورۀ مدیریت شهید رئیسی را نقطه عطف پیشرفت‌های فضایی کشور می‌دانست
🔹
معاون پیگیری‌های ویژۀ دفتر دولت شهید رئیسی ادامه داد: گمان من این بود که اگر دولت شهید رئیسی ادامه پیدا می‌کرد، بسیاری از مشکلات کشور و مسائل ما حل می‌شد.  @Farsna…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435871" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلجی: شهید رئیسی پنجشنبه و جمعه‌ها را نیز به روزهای پرخبر تبدیل کرد
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: رهبر شهید انقلاب دولت و شخصیت شهید رئیسی را با دوران پرافتخار امیرکبیر مقایسه کردند؛ این اتفاق بسیار مهمی است.   @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/435870" target="_blank">📅 12:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی: شهید رئیسی ایران قوی را در سایۀ اجرای عدالت اجتماعی تعریف کرده بودند
🔹
وزیر رفاه دولت سیزدهم: اولین دستوری که آیت‌الله رئیسی به من دادند موضوع کالابرگ بود. به من گفتتند به هر شکل ممکن باید این کار عملیاتی و اجرایی شود.   @Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/435869" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
