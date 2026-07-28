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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 608K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-jruXWwQac-cDhj01TRfsoiIlgfFRyL-MQRXAiPhYaSZ-Mj7RR0XNEMM6QLMxHFQaMneRjXcPrGuefXZZHLBiGhijx5J2gA-viYYACDcAO1GSpBqQ9Yn522wvi_-PTdbmrAWRJ2XP218ZcWPskA8UqnP2hP7nQZ4faxhVGT-PhPdTe0iMUIkKLD_-S1iFTO9XuRSfG6P1bPXzuRDshnJjZxbuS_v3GqT1GoCTumjU1U14t7Cev6L9yCUkzk-s-QBGyRuPh8E2K9MlIJT7Q0w46qNADnKz1fKBQdYthRj3hMkWpeOIsUpjLsXuvfI4XGnGBWy5qRgND-3pp1mqKvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gioTHkulBy2ba-rQ0koi4FZGYVRXh6WSOzneU40V36RAq_RJhWkYVUwG6ygUKByTpMFQfhSobaDTX2yD1DiM0rSrWqtDIqpdrkDpW2hBrCemm7erv1zyrxRD19eAPVWY_j_qEWdzGNQbuP2XAtqE5tY85ZIsiMgTotj2RpTVYpqZlKSYJgjFtdvcWSQiOh5dzBEC06zmMM5xZIq4htBfv8EaAJKRPfGb6qvg5to7ZKosFhegjYI9PjZRXBh702t6MMJsAxJ4mx1vmLWciOxM3yvqyd-mIremH6XwsEGP0MH3hR0-TQ5wORz0OlISSzBZKEyHbhH17NvJ48Dlv1ikTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_I0HK3_siwNlgg_UEAeL1uqOXcr0TecIV96vcx395cL-cjAcPbIPdghqg-I-2kjx3XSnxCmBpKt54sAVcnbil2prkHXD3klDBQVRS6XKcldLVxxWWKcxLtXXxoOleCp4Nvc_rMIVrmpMfbbxS7EUok2BT_QupAy70VuvMLyIQNUbHYOfMkL0tf4t7KFgKQydI2pHhHwiMF0M4GO6srAA9xoEm-aSn7wtPrdghYTgYc-N-hgvapo6bZol4gHpSjViPVoASwBaiKLZJHRcmEjm9P29OkgrWETwzcRMlJ68unhXifwv5oIvVR0Z-l_EtydPUA0IuSWcD_pqtwueHlbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfAtp2NwqpNorMP-c4SS7esh1sMyHrwpok8DH4sJZDPMS8VLgzULZjqkXY5qjiHNzW6fy3MKz9SmgsOF52HyFDpmgIVxH5cydUHqnXoxi0NTatiAkGBF0pLfGYL8PbGPsJuT2dfLS_40jRXSbPMsBy-sgiTR9wCTUOa5HDMSWR50QcZSg8Y2WqQY2d6eRZ_8ZrTtLH5B3ttnmVP70ijPoxOq0EDk_qTYWR7qKZcPKCLc9ypEM84vfW6FgtML7E2CBfkZso0M5gaZvC7xoTXXm5IrodFHxQJolPCnU0A9Uwt6soTAk4zZyLHxFxYcuJhOBAS-2clICzGkPTFJy4G6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKnH2uvswPXzS_PNqzKe-u9Vmq4PSC_dGSxuC4JnincKNnIwoeYb3FXx90udiq60dfjwMkKEF98fbNQv4LUbsVL-bb--CRoTM0Fb8A9TPzoHbXEJOOw34FEB-NnT3MDXeFWGW7cDMwz4BbP8jpuWLqwI27vDuTCqBVIpwTvEbC5xhsqRnfqroqPyu1xD5NwzNUdSWWaJbqcgCu6dSlICQbGBlyYnRWPWb-d9B89TTVG6CpIu0TelhsVosQImLjtXfEbco9Zy3nRWpyHx2GhFJ-vyfW7zhHwFFmOdWsDUuQgaub_fPMKTYnWIJ8r-66iE_E5ZzadSrGiLEMTP8t-wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BHKnm79gjEBfJ8ElbmL9c3CVsNuGgXIPTVkdX8zRg-ta5vFprBmN8mMTNw-XH0RELajr3Q-PuB2i3NS-aOOygbdZMRtey2a9c3sAaq-F6Lzuc5cNmxHRXJaT4n7gLSod2bzPsvqGq4ORUK07GVsl3r-ILMtKBcb49kN6X8VgrN5Bfi9Z6dQd00DI7QlGe2C3doSo2b4GpC_jSpgdwE8fvdeDQAUhkA_N9gig4AU8LiJiw7zEul6SUzU58EoJ75Tohb39ZiuuQNW7rIjAfe5PBKglFS0pz3QzfqrL8iZxwFvedcSzILQUTI6qcU-qjbiiFDv_gwPRgI4DNDe8VFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIwTSOWrBNNjqbgmjE0Puzcp-fTcd1s93gwBqkGCeFsZG9FMWHmc4lI8QhI1z-5TjqI2LQOD_cGK9aKYk72NhwRZ_jrqIa6chUfbEjY5_HnFbOAASeIYvn0ZDlDhaSs5j1eRPmBvYyaslIQm9ZxfetXBINmboU6ssgx1CLhVd380q0S8fJfImk6bXmnzPkAXXcuDOW4MPAkxUpdOo-DUeg_VAEewKtPxsvAE-jZI9KzKCEYM6T4ImD671tD5jZYfG24urvJ0XjykAbYKNhkJyRWP_TbbsKll56RpSbUq80Te5TyGNeb72wHXCqga4F3VZaD7-Cl6Ju9bflO5QkFDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq35Sgnu8-uBWFRQg21Oo8QtnYwsVKZOXztQuRNBY5zloy8qGkZWkByWtp0y_02GZHr23usw0ltP6vyOkJbvL5PoT98pxGM70v2EKLkGBqD3_kLzZN5p3v0aPSFSZ1kbqteokVzYbWlFAa_FP4RTenPrDHA6o-bwjgwFMZERiAyr6JWTKF_6a9PT3H-QdhV_V0it8FUy3ZmKA50zEPMmXALhgX24KKAs9-3sln6xzt81t-5Nu2VW7EhmC6y8ydTV55XbqdUQde-Mj22dskd7lJue0P4aBZ0mH0fPGfFthB4YcC3SAo2teW4Tf9-hYUp4Jkop7yECjnJ0DQkbem-ZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2la9Fewv550c2XredFBbeEOExIdL8o-tNu_nqO3FuuUg0ZmbGfIxBO_m1k4MSbhnotbB-Dbvdoj4W0FEznPLwsTIKOoDer7iRMSoUpTQaqyu0wXKAkCM6jjxczG3hVaKgCapIfPdw9Eb3737ZNH9aVPpvCC7uf1cdBUG9-x7DIFtHhRDMjeF2j07F9YqgmsBINZmgoJmrqByPf6ZHfRnMSlo0H1u7frn-d7pswspCfUY3qFw0ch6WD1qsW5-x5BaZ34cxEzbV35OFGypqVzjA9Cd3OlRgzYzH2CNwSl3uuIyFZtzZSc0TYprfsfO_qDy1hYPrSHJroMkCWuvj9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp3IsqscX0dTtbyHSEXZDVEE4nZ42AKFso1H57mssfRbdOmZPZEE0ITYqicVCTZ3SixM6MST9Dxs1l0VxcuDOehOErdWVYwvSxv_pNZ2FrIzxGLFXONyBRHFITV7OsVtsrtJGiMozTYWrsngfjgWaBnmSrjm5XFSkZriRRrWIV3-l55mAa-v3ZViJ0LTU7-6NyggFfQb_7QiXPy3ISSTVtwBoXMhWiHzcV9PjdXq0v_apkCYDalyQqQ96ZdCnO9TYA61swZh6UeB8M4e_rVKt9O1fwtSMUitjRMh1yaA2idJGLFdGlNrc7axwJXOGTZP3-0b3AnHQKY0yrlEpPhzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4SczvTLZnQPB--UaMZFUaAuferm5AYK2OkQRDBumtSdPGkOfCrV6duR8U0fKE4f9_qKOFbhrt2umNGtw1ZUZ87jpmyLzjkkpSEkciHdT4AeG6SYP9D2MpHq84LpPWZOJJUjqZToyQY8g-MzpXaGc2XYURm2RV1_AwMWbBK-ckF1sAOImVj-JBT_3YC10bH0BqUxcEUs3_sdSXgqOL62Wm0KohkMunxFFhX5GLyVWlv8IniBQkLHZ2ZI-J0A6lbYmkuK8AdcqXQOMMY5O2_YnXa21atjrkxIWYXBehgjCfQT0lt8dqXUwvLP72HINb6aD342txNSFjNUDcF1iA6T6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1z5Sz391KUDJ--Opal7FfC_6HUB5enBYnzmVi-_o6GAbnuO7-_3x0ZErdDco00SaWf1861lDG0vr-QzbT9h3GKXFyMSzHPRCiD-xenip88L0lH5rBvwihUoIRvpY3PGOFr3sqJPsxx5jNgUWvVMRxHvDAIt-ckdsqtkHvVprorcEg5ZbEQdUux65HTUroZBlDlDdm-RsZLnEPJeRHfHRTHMwNRU4xny_MD9plI7QGUKYpZf16Ryti2ARPFG0jVA2sw0Lneafn8TAzc16WSH4zi3Q0WErewItJNK52OKBf2hxCquJU6t5zVu5QuojiYQ9cz7wvcK5DWt63uelXAXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKmKYSihFxcb5BcRdtx6UwtoLWV2FczP5P9iuHA-erVAbtK5_MDlSUlcjCjLvSLMrY6wTGQlQqxy2ZPzfi5_eH8ULmwA8Higwa1GTekGBhix80AVCrYU4VZG8IoIIIF1FHtjPGf2UIIgZ1QFj6ilYXylHhWoH7inLeRpPJPiZ1pUR9Gm8brCmcWIO5aDDTJhjL6Pn1R8meFpDDE7trWWGBACM6Nik--Hr7UkHGNHXEScBEDeTyIhAxion5W4Q2Km1lpFPhC33HaHu3r6KnMXqf_w3BEjlGBjHxFtIWpFtSEDqafup5nDDE_E3I2rlFms7fb56ycMz5kY9bQupNQl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWouwpLlvUekbUK4KDUPuZ6-YdX0WylQV288me3TktQW_8GHy5K_S_Bzo1HSyTghcYtYqRba-0bSfv1UVEHPrU2OirjqlQTroueqpmoKDomJnEep3Y-U7YKxhEEvt0QugR1-ycIdwdCeESwc-PwwZjRNxDk_KKpTHKuqxY9TdJ_wyYsU0wvoOFS7wXpYeuzX3vPLF8BJEXcX-kzEISCnIoyUqYQ4WPIrUKnDhFxswGKIjzkqDouxBhysdjV664_dsvgvj3ycXQyOyQxkIMS7R20_s-IqsvOtSga7uQIDHRVq-gc9tFO99sMyEkmY3vas4dcKKH7Z_oEyPmS1FfQd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHbJGP557MJn6kXmshVxbkwpuA--j2UkdKrvtyE30uQxZG_VW71mElKGgQdjlUbZXPVzMUJ2Yj_J8daiAv6VssJCIoPSAJFRWQzsXl2-BJlBVHx4K2l2EgCTjFsgwpOXkK8D9qmqw37WZVIsDhEuCg1YEk4VizdmC_bgMTtDmFt-Nek0wXygf3tMbxDqYc8xmb7ho402WrfPgj2MXcL0Bw7Szyb-Jv6tjILYMXfCgMVENfj3qWdLqrpFJK1hQgtSumQOplKK2D7_aPzxt68cktxXLkNncogeCmYV9FyC7_aWIWy2IhTrfa_Tpol32boexYevOvanYtio1GJpLXFJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oOFR8yV_T_PQMM0kzLnGjOuwFK8opU9d_C0DBhEzeLnmDF8tQIkg01nOPTwYLT3AkIZ1YUQpvj1Qr6ErkW9dHa16REiDpHnYHp6bI24XTPvmTBwn3REYmHqUoBncuRO93Ojt2lBDe6YfRdHvdXafJwzNFGpDUFk3sizQZd1BhMIpEr2ErHkopmxpiMjKFeP59w45GQ8ckCuxL2WH8OaZAFsqJa9zZfIhTP6ysyXkeQ9MxozLR5c-JaLq0WnE_qVQsUS364BLEoz3l8QqechHYzjJpDTmSYLTztijhcMUvWIDxGVTCQYkRCeGQWVlwCr19Zn5Cg3lVYu_Do0H1cAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgnDPLr0n5pjHlsTEH1ZL9EAELHbaXYFtGRGzD5GDNFBbg-UQ3TJ5gmVvkppbrbAwDUMUEq7c-7Xai7t1EKhkb8E_4L887U9naSiN3EKqL2xdac8GhSXvnhweti9xUQkoDTHDyIFa_EMbpnmG7o-XdQlLyjV6AlVoeZXIpkQ5T0h-Pbx-azgFS5QWKSALZm5k2U3YlM79bWVUefKvx9O2nfWAQV08_D9dpsqDY7pXC00bmp24tjufBO0ymnafLDEf6thGDukdv8QmbJERKsdtTczDdwroT3xZOXYXqJ3hfYK6tBFKPovf0V8QKo0gIJiTybis6m-q5s7X8RTzZJ82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNznNpa-xE3SbvknZpDbBLdYMa8v1Qn7iQqDGAAhta3E98_tgiXXbQqC5TmXJIMUoFwUEb-BCgYVq1nWxQc6bA1UHtQejeHwieMLVTH0H6F1-AdnCjHvXNFH25Z0u9XW3wrc85TGrZ2p1fG-lC8EpwhaFtJKii7DHWurRZp0686lw3Kvift1Rbo_iEqWgIYCEso87QRACaCojcHveLk2v9fS6FiqFITOhvSodlds2ClkMdZ1pXD2klWLbnhtLhTdHLVAQpfi97_I3TQclmJASzEdGttIDTTTPveI2W8etpT68u9W59r97YrVqldMqJiIOlZgbZ52gYnqO5yOZL25cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=vH3c-Y5qtBisXryZrkX4VuqoV4MA4f0X6atApAUWKE6CyzpfT63mQWxnRDBIXxXGxQRQtDU6FvcelqIYojHvGuVA1f-BXdOud8V19E3YKcWJzsO7PU_WZfajPtMHpg3Y1l2zjROlCtttz3Ej-VKp9vYewFHVeXNtPgoZMG8In2TNadeg__Eg1XtuCU8vLvsKgKj7vxXl-JN43noxq5SM8BsB24RCfk0y5hfn6M-xZGTchytLkpclCRvvsd13fGso1acgi6hQRi23Uw2hwfc1RpQna8FwT10Wxmu68sWEptrPJyvTESvyOu0EN7PLdcBz-NVGXH5Gj0soEGdehR0kvWECXFsd7Eag_q4ITNLwRPs2YuZWQWDbvgJBnXs_h3IrVIsKXMdoWP17TunVDVi-S7nON-5BswEWugkTotcBUIjz-uwRENjczZgj615EHI4o7qzwDiAgq7Mn7kcJOjRqsmUFoUaKk2Mkur41FWyTbq-CiYJ_T3_EC-790c7885baj1eJzTQiTqFa-K628Mw1csmhgZLIHxOOE-JxuMBTcZkPtx6XRkkfDAbqSjfxRg3PgnQreODX1GUdLHVVQ8S-esoHr17tB5CSvH5ChmBZXj95aLeZd1dscwMwNHczcnrAyMtfw3TDusT2-BcwI8FjTDLE9Ix7z0UMPhVgtSqUtIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=vH3c-Y5qtBisXryZrkX4VuqoV4MA4f0X6atApAUWKE6CyzpfT63mQWxnRDBIXxXGxQRQtDU6FvcelqIYojHvGuVA1f-BXdOud8V19E3YKcWJzsO7PU_WZfajPtMHpg3Y1l2zjROlCtttz3Ej-VKp9vYewFHVeXNtPgoZMG8In2TNadeg__Eg1XtuCU8vLvsKgKj7vxXl-JN43noxq5SM8BsB24RCfk0y5hfn6M-xZGTchytLkpclCRvvsd13fGso1acgi6hQRi23Uw2hwfc1RpQna8FwT10Wxmu68sWEptrPJyvTESvyOu0EN7PLdcBz-NVGXH5Gj0soEGdehR0kvWECXFsd7Eag_q4ITNLwRPs2YuZWQWDbvgJBnXs_h3IrVIsKXMdoWP17TunVDVi-S7nON-5BswEWugkTotcBUIjz-uwRENjczZgj615EHI4o7qzwDiAgq7Mn7kcJOjRqsmUFoUaKk2Mkur41FWyTbq-CiYJ_T3_EC-790c7885baj1eJzTQiTqFa-K628Mw1csmhgZLIHxOOE-JxuMBTcZkPtx6XRkkfDAbqSjfxRg3PgnQreODX1GUdLHVVQ8S-esoHr17tB5CSvH5ChmBZXj95aLeZd1dscwMwNHczcnrAyMtfw3TDusT2-BcwI8FjTDLE9Ix7z0UMPhVgtSqUtIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rER--NWGUX0NRonOBiXegtSYZeJYmZcfrY4hZzlXpspeNyvrC30oNAH7hcBe_jpakmEugofcWAciWV46A5BH1Y5U1gZL_7afT2ciVfYKEl-IdRmxz8PArUt_viT7LnpLVgjo8BpQNLES_HcB7M19m9P_Wk6rm3jcWC9jjnAyvsFZJXYvBocZUVqkX5pRYpGX9VooAgCKrNZQ7E94Al-cXHnRkeKOxTvwfkG6Yw8V4Kb1eSgQsTxz9_cuoT790ipnV6wsT4nFjlexZOu_5y-mvlppXjrpkuDdwXwE5-rwfJSClpTrg_CKj_wesZZBIrWILFbe2ham5tRNMyq7_28WjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPN5tJ_UuyR2BN5AW5sRrR53-JEGDk0hmA82kn585ETeI-acSFR5Ll_PN-wCEyFahdno2CHPEQwlaHvvHrkx7jIvU5Pttu-NAeUrTpTsyDEjgpJoVXOHHKPNubPNbqTpICE31kXePEGSukl-x3VmSyDhtODsDhrBJ65X3qWb5kOCSmOiq9ioAS2-XbUW0PPyVnZhTaQ60M1DaC1kV6unwEOef_rgpMuA6O3Qo5tttVJUTSxXNnf0GhoVAulPDw48lwTwISNrUDa4Wm7FdMnU4f0_iVLaIvF4iVBiotvoLiXjIHwPCj0KUlg7qvNSh1eyA1nuAk-N-Ktx39MQby49jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAbiX5d0oPsJ4e3feuIFIW9otfx3im_aXH6WAi4KF2JxMPL05f2o3pb_zowbGjemDTvdHaZroWmSYvcx7Y505oQ2uk403QPx-D1Vkr1EJTAk6KGmYbicZdF4fy91IzVxfK2vOaVcTcLckjyH_3HTHfIDqaCaq88WjsvKBgvnrohPrPmHZhJ1hSRWsHNmh8_7Z1poTtbdy0B9c23wGFCS24NkXXgM4NH5290zSzjW0l-BwkKEugRLWUvRAPFxSR913ehEvyvFGpLtC4lulbjgZ5DJM6HWtnSBH87gybBR7M2PvW78pKayR0ojs3wmbO9jVIHhK6XWAggeph1Zyiv4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4PXTMTVNOJwQ6qqHtbqic6_hQYMmwJv9A6R911Ir8Dsy6diuHzn-kt36DXdBQSrgn-u4h-oPrkzsJwyaV9ObMT9L5PMW9YIqWNVNX93GbPIKyIt4G-iK_i8W__SL22H3XSOAvlvSoCo58v_hEfr7H5arUjGi2lex3dKMK73rSaXxBAmqi7DvVeoYRvtf-CvHWR_lRB9dUu-VWGp802RhcQUzHloXntTcR0N4A51vd4kGLgcIO9gsEwm8A57a7_2yez8mRj9crOjR-0BcEM7xfff9yqPni79aS4IwdrDUtZdZT8LMYkC2D3i9si3rLKDTmcaqPkdWVqnIGnlhfJvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCIVAxoeTRRCl6ybBc5SDr_Pwoz5qK58keffpq6KvmW6xyc7oD71sru-gpDLIIS-qodNFpdNZ5M444F6e11bA7oOTfIa8Sl8xnQSYEPksr51lCA22nlA97O8htYvpc3PkRUKjkb12e1lgjZXcTZuTwSKdA0tK_W1QI6DGKsnChrFR7LE8yLCs8orTwoq5quwbHA1t9zzk7DtbUU5fzwxgGo821KRa1yyy6TY1njuQ4VZwSoODuNx01T658pmtCHcQxvckjjIjIkTdEQoMVqITgyQXwrwWMBOm4Z8iDYnlK5YPC_CD2lbVUrvFwBO_vxhaei5evVaZpjJVyFnC0bVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRmbnMUF8DPMWoTkrf76s3vLRImJehQp4l9pRQIpDkpwxIsv_VWLBs_yL5uY9Bb76JtstDslRq25BX5s-Z6lq4WLQrCWne9mN56XQo5jehRxW4xsPeZqis3cxVOt30T1cRUuku0edBGhT3bu4TKvvb4y8DV2uxym5kn8x0W2RE68c7YYfe8djDZ_XTQ5x91Qsidgqoun6eZg9vQAqXaAcJVAMyAEXGQ4GSFB3nB4IcIuQS-tTRkePy8ltT2kNiK2cCIOYbpSxDU2mLm05bxwr4qOExOAaw4PSzzeLzlJGypnUbvj0We1Y_3uPnfr0yZl74dWbBMq3ZZvUXGXlSwqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJtij5Os5MmJHbgg7X0rElfPZGpLhEkRREFKrCbE5mG0wzMdB0NjWfNM7uUF0DtY-x1TWiZKbuImpHfHyT_eqE13LPQVd78FgsSMxaXariL7_J37ftNEKX5sOdzvEb0M4z-nWkhsGo8PRKuSKN3EWgW2KVNDPPWUvWJR75z8AowP7nFCwPPH566fXLmfob1CrDqNloEu0RTm3CiTIZSZzDcyQZShoMwD7-0uCaJVWZBBWE991BkmZVmfeyFyYrW61KgEXqLwM6f5tdna8a3AiR0cLqC6rbxtQDRWLDikjV5wG3MM18oBGhe7vksLlE9mN2vEfKd3YJ1OcqIdrGMV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAp9dgw9ADY1kPODgp_SS8PHLUYQbdqlNjEnMI0-a8DaLQJg2nUcHOYLadtrEKaTfGTcRgLMoQG_yA5UX0pBx9flLgLqelRGI5qqb7TboyqwCdV-PVeSnG97NIZ-DssPu3w0ByfCvOG219UFAEol4hPKg-8WsoiGNXipLfNSzT2XmDZMAicJiDH6nkZsXxbT2G60U_LYxiEvYqQigyYarVDHp29hCthJCdBG3WIdKkxbaraAxDwZ-yE_uI8WUGiNNsH0bnfq6pFqo6YPadyRS4XGqZCuF6n-JQMmiJdGtMgUBLu6ThcOo2uUREHf5O_FIB7YEcOUN07k_kAnKbzyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KyClrn_Wej310DtgBg7bZAjOQKpLAk_DK2ySA_EbA3E0HRUPQHT1YPwNAefK7AHAW6kSMnonMP0Wiz9xod3-MJldtn6LLTuJs3N30CHxABKVczBaeLKWgfpWhlOz63TkubaddItHB1IoF5OWGo-mdgnTiEXAqqqfKa4lIxNbT4mMK56tfbgkOxTK2qKJc20-pcD8ZNgb0wYt-Mlzks5z2yp4Cc4rcx0_MCNLZa2n4n5gtf8TiCWpGYNoZS4pEj1qjQaCWlPsJgMvkHFOxJ3WFFI1O6teGk2wFG6RMCF4Mqq-ohe4GLDYKR1a09C9X_C1WapO7Gt1iGDOmZpc1UPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgJMqdMbuaW-x9ui-rKKWuBBk593yX71wXNn9MtDX34g6SNBrmDAzOI021smqjFGbnjjvWID3TSQ-CnmNoplj-F4FmE_ubYMI3J95LGgMj3loRjB1l0enuvjGYPfDAqbsWAdF8_-nM8ylfZiF4hVczHwKJMQddLWbgoQvGeslmy0dvK3zNxLyG80U-ilPO4V6lp-7EWLoVvHMnKTIaJ0AOMmWwttLBDQcpi6i9f5nfBRkpvHkV-4piLpGfNynDboEC2sPPgjTSI0Mv6dGpnjHO-DPs2ASiquS7ZTjMIQTwdnQMAIOjGEncGva-jY2tW3642rmY0ixeR3vt1A72RBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRxZYymahxCnNUXSNaPcZNGVYdmutff1R_xkaO2fmUBVVTTuJX4wX-04wSYk2slJD0q12Cr6Lu545g0MMDGcouaJQdtLytIjl9vB33ZycY4g8jT2gSjVLgoAAnjX05Fm4SfXrQfYYxMsxdYpYH4rBIrq65bFDouBB62fF7WSkRNrGw0uRa2L5okWNdpHR9dYVBHr7kXVsYeD-ehR6oxOSfk5bJUFuhT43HBWxE2SSC8FV3hl6qSgkA-v_CIySIltG6KlmtyqBFdCMsxn-PIb7Y6rmhlA11Ka53P_PyRX0Z8nzMfgjwiOIW01QIqJDnYpzu004cxOJNWTjk4wgzgVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpM4_oONkl7285N16_CwukXXTawHwUu9XpOVrht_2JgOKhnEX2mH7mt9iytTZXocaF0NmxsCCkOvse3Mp3NlavHT2cxp-2_zEeR6rv1Jej7XL_rjxLzngGLFXK5nbhljIBkvEwY3WbNrk_qzkLC6Y1CEpPz0eEMtJvYzy7oEUBcon2Dw6UGeTMTkJDcL4ZTtLxQ0KNDxVTxifWfnfqnOneQ9k1jARMv5et47cpBZNoCzpXfMCHd5S2aH1i5q7UQZfpnyWTHVwi0QwRfqskXhboAbozXvqxSFF05iJfeKxhyfUD16WD86_65OWabLpzbolrMQu1Jy_uJRIbejTi4ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh8ZrS03wW_OGY21Q6A_i_wfQlY-XMPwYyx4vJhAblzAg1QpnYJWErPrgfMjnfQfB3nwCxnAYqRtMHHT_uX9fvoJiMf1aDzz6CFQ8ARNupuM_xM_Dhy6MkWpJt5c6kUNwYlsaCHcpUTshz6tm-9Hhc9vVq2qEgubOxYcSKUVClNm7jlZXRzeqNRWTjQ0kPiu7MeZxUSIWlxNb-hv0KF2K3SdTcHqKzv0XIPvdjaOOvxDxfcpgh8UOPxNjKpiiFQxEqhtSNSPpSRIivNIDtBgbCVol5vVy_czqBwR1dvv3IOUCUeNlLg3NinRpyEWtwBrZhezlhzMutzDvqH8ZUrUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWG7zQne2TXr6K8oPo3GgxVmQWTgIPKaO5hP1Xf2utPRL7FT6PMz8er-iroLvgQeQWS0dkt4XvBCHXCBarDrEGfWyijJFxvupS4RlRQOvJQxHKX6BZMdci7uKPkQFzb8nxRGCq8-nA-FxGMZRlbX8DUUsDydIYoKFLQg4vIGPbbo3shDqUpMDtjOE53BwOcwcmIfx-MUf_To4WuiwWk8_nA_dCnVEItgtx87iBdsls-xTgXebvqdSh0uGqtjuZ8SL8NdyPCW7H-jn9e_Kddfd56veyRwbmtaUsHJUUCxJRoBJ4qj0IhJoTQZqxF29LFbc-6GFlHfUZefiudmVABrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWTjKH0ews5z3dQj7QMfhvoQP9Vf9BCoO3785wgvWzG0i2ggTGDBQ1GgGAps4kun1l_8uiEcDyQWKdZIMEEdoLzIJS1JMwLajEorKUaPG38L_-JNIa8Vc_4ArIQfOc5KBD0Be3XTo5_HdUwWuTB5KAGFL0zP1Q9NbuAOaGX03TvUeytXr5ua7ObKKWycU7gvtG-vgSRbR58X-QdyMn3RQZhimTjQUQ8exqjJtwM5u9DwUU-KUeaqGLa33m-t6J8gGXwYZinwsxmwepsI_H5FHGecWJRdUocAAgLkQkhzVDk3Rg06isjep_eMV67HOFh07JKvONFDyHh1XdrDvKopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMIFOfH4Ummqqud_YBRfq0AiFDlGbA7RzWqA2MxFlK-5jDie6gokfT3VgxxLWFGyo-Hu3NZym_co3yKzoSEJa0ETLeAuEVThhCh25NpkYR85No9-v_-ycjQsmfP253qcJEtx4ytcgX9Yt-k9bfO1yM-Q09OyOH5bi7QZg2H8g0YEvMQm9Jh5dyOPO26990RzT9IGXfhokbC7rEiyZwLzkamh5HiMUr3pfcDvZxpuC6t29yJtfMbwTVLEHz9g3WZxUP9GcTeIEMWpavkOYTXUscTBmFJ8tahWrWHiYFyTyntQ0eqmIqfza2f-rMv-UE9aArM4TrCfIf_7V1tu_dQVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhrSL4OT7akFezOOV20GpJWTOFYBa3Lsrd1PrtOOYNqTmqvksoxcreEoUPLp81lFkesoQnZiLxIpKyhv01unkIldYtRFIYi_CreErjDVgetEARo94OVb5QD2geOxAkBumhYxA7Gl-53_9xFNoDlYocnk0EJPznETJn-PtnKqXBZqxCxPJExXzNJ9XdN2E3BaWK_uQkzHWlwd-4MMGT44WLVVe2fMwdy6mUyP4UfONuNEPeX3uKrwCeiAq_oUVdaTBAaefzfzBtSOiKyMMkpCmxEg20Nym4QgH2QASvpvcMltuedn4p2mkee0WTjN2X9tRn1ngCWtC4yrEjRr6BIdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH35vkLx73p97lKobRGHZtRuFhMS1jSojwFB_NQbS-pfafOqL1pWZP7dSyt5AY1iiqDlkZ9bPI8_6mxRBougXdoc6Erxqp8x58qu-4XK_ZJmCzmw12-oQrRPF4WGn8F7lfAUUvAhUJdbU4p2r7xNOyQBUKyWbPXeHDBxyN-iTbooDCWFMBwYkQD8vkpPhpUsMJLinzZdWQ47GIzejgxyIFOwDBdtvGFyWnHoWpiMW9oky4-eHAe9Jwi63YDRlNDxr0SZdMk5rO1VRcxRK6xPbGp7BpUTbRAx9xfkhYw3ompBGZbUPbseJAPFEjSVnKXxjIOiJhBSsbHndzFjTOth1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAwHdQOmxfYUGy8JWGaIaJusKbocTwlnm7aRxcRYRqCOzp0i2mjwd3z0VWugnE1ld5EDTgT6ifWsQmCYKSalqw-eWoZddEA05oLI91_aTC0pbQNR6-uIszKvzt2EABG8ldCck8YpPuhFS1EqcXgNa7sAqoIZtWUZwPW798xMXrx5Q8Cw93RIC5c0P_y9GaII5lopeV8E7VoHmm_YFiVfGSPhKAcF2h0b3nZuXbtPk68jesI9lzXqqyPbBh8kCECxUVGcOXFpbZ4UTXbqBmnaPj8HC7wqEnHih9xp_iMT6GGrFFpuldgZgHVza19kw_IbZgn6Evzx9-8W5dhYSZrMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKstkzQk0pYRoO-ZX_Krvouj0Neg50IqDSpz8tKuXq-9zeTDHJcXpG_uAxKY0ccCV4Mk9Y9Hm5iiLf105eT2xhCf94QyEh2Q1sdsIcy3ZgrJfZxZOA54t30UgpjxnGSxtT-2CoyKjiWyKLZSMB1nHIsMbkabxJoskcpksRtCcVt_AaqanmqsEHMfRmKIxI2DeGCVZ3XKRVn9PEsN2YIdagBQnewZm-7BiJUhT2D1GKUC1UHi1c171StZS7eglR7yG1ZfhynHm36no6DiEmAO69vBAiT6VYLLr58ARFMhEpW5kNSrcFm7SS2IENmOHSxzjN4KZ01Ms4Z9OBEwCTNZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWLWsG6YadG656WnxKozKADG0iQ49TIaFbSM-Ne_Nbs6h8Drotm-VZz3zXkdci3PdKLjopJN_MLvEAoDvBCLTbq_mGlheFldoZX7DJ2E_RNO58MAkdGPQJCczWQ-8KExN05971mfGIoV7rWVPp4brpWTXX3ebuWe-Azjax2AJdTfUwcaXscNxjrzacNXq_-SFCJr896PCXa7AiuREkTWnXzAhN0QQUmnQ_5lHf4pqLEuDN_0mbMK_qTYL_BC550YJWXo4HcqxNgKSd0DCx4CXQLe2ml6B0XxeTEC2YRusPRBQSmMfKH4OmXrWbfCYaCBedn6ddh9yaXhH5mwkVh5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgcmH24btp9cC18co-Ja5TIg528jwfK9g-i6bLZ_FKi17xu3MRu4KQDRM_MRvnbUxseGZKZfwnUvDuYtbTkpaTkALpgVTAgxBR6Gc40rbWzZBUCPHT632CiNF_mGqqzBHUb4L4h0qw-g7OCwF0K2P5tqkjgjVEj1ze8H2-YMw_RcXdHn2nPDkQtcth5m_9NJwjr-cfI6mYLHYytMm9boM-ai2I2rnWstGSESXb4u-exYYwwgGQjPkkZma1ilElMERbWdSMbMVzJp6uyHo_VHCwUkxvg2zwHNYtjEXMkn4Sf5LzijzJOjh4PH9Xy0vEFvrwTbGbhJZXmXBqgNv-LS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=EtCGOYohlRZ8KpU6MsjN885jXgkNYZfLWdNsrWrUWg_G9kkQHGEVcrdUg0qRR324haVK-uBrW8SXPkci1zlDAe21qaEFcq4y769sdqKYswO-5A2ODkKLtk2GN6ALR2nHZDqgFSMAw-Q2ZRLtt7tbkRKrbGm5Xbdhm0-XzXQxrNhgyGS9C9ozxaXgLECzE65FjdO3M5tXBrhbvs7jSGKSJXyB9KMgAY59OAE1JWRIZk9wfLDg34Gwyz52zVYkc4yZQ5D6ictI-fVkxN2boPHJZ3j6yQ_yg7zuDxjRfVbB3voq45ohfdEfdB9xnR0ZOjx1S1S36eHAIELEvOItHYDVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=EtCGOYohlRZ8KpU6MsjN885jXgkNYZfLWdNsrWrUWg_G9kkQHGEVcrdUg0qRR324haVK-uBrW8SXPkci1zlDAe21qaEFcq4y769sdqKYswO-5A2ODkKLtk2GN6ALR2nHZDqgFSMAw-Q2ZRLtt7tbkRKrbGm5Xbdhm0-XzXQxrNhgyGS9C9ozxaXgLECzE65FjdO3M5tXBrhbvs7jSGKSJXyB9KMgAY59OAE1JWRIZk9wfLDg34Gwyz52zVYkc4yZQ5D6ictI-fVkxN2boPHJZ3j6yQ_yg7zuDxjRfVbB3voq45ohfdEfdB9xnR0ZOjx1S1S36eHAIELEvOItHYDVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=g0h3M83KJgXE50MlBnBjxgLAwS3HT2HlqHxPDO62A6-fQ8Asr-iIO-cPYyLiIu-g45oqIaekmnNEBAU-oo2mTeuCa9GYI9HKpC0WTcbl8L4E3T3KR9pEAAmkKWTmCLl1Vx1K48LpLx8NSYdSi77kuFgc4E_pOzWgTXaWbrQ459gjk_IjD1ACpwf13SRjpgvC69fVfrtnOkew3ietc1bLy6IdInuSa61vVwbIiv6Vc3KkwSSRxgtY1DZ3517XeNKbm4F-mq6rLsDKr-Q7KE1fBJJVTxpklRFejSBGpGWKSbjUdsIEkkfoDYullKlqOgguOK5sn3l95XVZqcuiIzVIr2VipJj6L_fH2m0hNAn_DU0FnKPfdABOed0rLnudrtD4_hMzGHxVi838gYuhvQ-dRjRKgv5jpbjMtLAXSj9zjXkERTcA_HjaKp7AjKseIO4X_AsUoaKYvaDLct-xnFWlJHeN5ekRTNAR4zSVrNKBRUa2fNd97UFnSKkZjQajlNbCEC6AGyk7-NGDck-XCA_MEwUbGV8GgVOwEjijHKygC3XyK6Z0x1EF-9g0wWWv6-f4cMRtHqjUwZ2PV_slwEOvjgWLPVJ8mFj1YsWcGcOrpAx1QzCjS5lXvWfOe7IOkqaKGj6XF7Zeb9tRtpFWR01snUeihb2vhpRceRuQR3_2bYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=g0h3M83KJgXE50MlBnBjxgLAwS3HT2HlqHxPDO62A6-fQ8Asr-iIO-cPYyLiIu-g45oqIaekmnNEBAU-oo2mTeuCa9GYI9HKpC0WTcbl8L4E3T3KR9pEAAmkKWTmCLl1Vx1K48LpLx8NSYdSi77kuFgc4E_pOzWgTXaWbrQ459gjk_IjD1ACpwf13SRjpgvC69fVfrtnOkew3ietc1bLy6IdInuSa61vVwbIiv6Vc3KkwSSRxgtY1DZ3517XeNKbm4F-mq6rLsDKr-Q7KE1fBJJVTxpklRFejSBGpGWKSbjUdsIEkkfoDYullKlqOgguOK5sn3l95XVZqcuiIzVIr2VipJj6L_fH2m0hNAn_DU0FnKPfdABOed0rLnudrtD4_hMzGHxVi838gYuhvQ-dRjRKgv5jpbjMtLAXSj9zjXkERTcA_HjaKp7AjKseIO4X_AsUoaKYvaDLct-xnFWlJHeN5ekRTNAR4zSVrNKBRUa2fNd97UFnSKkZjQajlNbCEC6AGyk7-NGDck-XCA_MEwUbGV8GgVOwEjijHKygC3XyK6Z0x1EF-9g0wWWv6-f4cMRtHqjUwZ2PV_slwEOvjgWLPVJ8mFj1YsWcGcOrpAx1QzCjS5lXvWfOe7IOkqaKGj6XF7Zeb9tRtpFWR01snUeihb2vhpRceRuQR3_2bYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlVLgZDsslMddq7WTmSgktR6QE_d_fnCTkPJKSqy-jf0xUBgpuOgyVwxmGxfK2AR9T6bL23GJGFNgWptbxjd4c75HbmAO1ipRfhj_XATQ1PSBc4MRqYkfrhW2ynzxM6ZbAC4oAfcon0Q0Pg10Utc1fs8Vr-nudFfunv_smu45-tsyIf6esQRn9LZ7ZkQc5nVtikiS_RmP2JoDawI9f4SqnR7kNMrU-od7JRtfn7SDgAllzrV6zb9TsU73lFTQCrHuN2Y5l8sbe52FXjDropIR7gytR56OorNAp0GJnEfWW0vYWNhfHvg12mp51h0C81dfQH-IXX9JatlBkNkDqKsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7murMx4GAhdTCY0E_ln4taZ087wxoVETLWuAbVDX8Zfm487bEi0cJAA1pu0YU1_LHx_3EdykELFmYpECHb0Nzl7yyWgL0gv-KEToSXwdjeq9G9M3aW9dKp8v_o5oAmMfhlWY61xC1pGyonobaiPvWltkMzG_SDVn2kXqayHOEVfESwbHJtOlWumSGdY_R-E6BirQljalt4NjxHXY4TEEVfQ0GFNos7YmkiJuWcIHnMcxTFIxhZI-NXe5GxyEvX7NkgFf_aY6ZsGx2auejrTo8Yc3EqnqJHUzQr8JOBje9LkA2rEufPy-0AxX4Un4MIqF-AaUuv7pSOKWKenD3GaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikSL_kY8PkdAwMpUMg1Dnp1Uso-7oaMm0TCVMBLlwvJvhRzdjeCsOmz8uEF3gmob5NL7Q3Exsp77xOyXoSezTEsEEn36VXxk7nd5xuAsHAS3Rk52VwDNNHvZtKuYR67vvA0Sf0Dn9TE-uf8Mx5q7QmKZI2i-ipyjtkkD9wF1uSUu8FRfw3MUH2cBw91XeHqAfawzkuLNd-fCQLq3bA5d6u48IQdJqu1UI7o97d62lvHNsCYCZqBr0MIlGk5MkczsH38nz9mOMY6bPfRtueNHN4giz3iEgybQH6dByasdtz8HkDZ_qeNRNHerPD9f6BhWDtvLaBHDfEVvOzD61EA3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVoBwSZn3fxb2uYBnhjyZbo-R4TeIH0CW3gsAFgGQ0YBAOfYUYuqsErfeLZLMkHofxrLyyNyPfDP1SHtasPrx54EQPUlmu9LBNV5Ql6g2uKUOpVMdzuPXskWysu6xZt-96jGx0az_KRUcwXB0bvG5eY-eFvGfHJr1qK5_mdlWX2DHuyN7BTfFH-kVXRoBFCitLHtro6Dk-SBxvxENFnxht4fwJAr2pMAqXUy7OelNsp2wPwwAxJ_4RB7MxpeHkkEH1jIVlSUANqKpsmxgkYKGSw0OCmsCAssBOost4Lx5LGT_hhJsUJGXVi9gi_ffAQRF9njkubCVaCC6f1_JVif1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlmdfBKMbN290A0wjJK4YKu5oIkVSawHSZ5-8WyTGU84cZWEPJrxWcKBoJlMeM0OeJZMx5jjlueeKVUSpGUHz2EFKVdwYez1CHFS4zJRCQRyZnUQwJd82qUTEElRcVGQtG0nGLZnbkWU8Wr9V-S0eaw0BPALnw6JrFL4aCm2Sk2qbQtVxik8HFb2UPj0PBIjjkOxUWEX5gS4AkJDoIk2TQmtf94V5bHOwYVrMfBWPw_4ZfjdH9Jv5yUuup1eM6Jhm3YY6zWmqw_sID7Tn_OYRftgZfuWJThlCAYZ9YMlRknCkuUXV2aa6Uzkl2Aj7ZdAD1IIZN-A_uofTjP6IbEa6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw7cXuVeFfHT4edB2Wbue06uzWnVLDMjjP57vPmNNZ9V7Ef5Xh4_19B_8A9Gp4LzkVJYbLpBoMSuVs4Hac1XAVudr7lLENdGg3afnLulZ8ZQWqfM87nAFBwZrv9mTPOKbA7hC44RRrsKlPkONdbDMQYJtuku_Iu6RIVLQT0-ljpGIniOXPD4ltTIqDNSPDM8yl3sPrLIvX82MQ0KqK2RA1pjYYFoa1IzUV7kmnNmAxYXWoOm5Q5YTyQfVNbIjE8WR0xcC0FYbk0owS3wfrYM6xJL77Qhoz8KIV4OWLtocrhWkJEI7CoI7Ht06QqpzOHbjBgsKg0ns_ze504Qw3o7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDoCyuVv3HbPKYfO_9wzYwX79qIQ5ZSceK8_r-HdTQLaDNgk8L3BaLapZ6bR4M1CaGTT98eCTVxphGDUqF_hNPL2AnuAZetusdMukvA9RUKmWIjagE1tzZpmq00yWdM9Q2wGvyuemeJaMPVM934CSJeoMXvQ9pvdyY42Jx8xVbMtFMN19ztAqmPtzeqzOheFUtoch4U5O_Aq6vDD_wBvw_tq6j0-4-NpLplwsp4WNjcOIjnhdeE_WvXqOAz5Y32jYwZqcmj1pIdnuymbtDA7gFGwO6mnv6x1TTGRakhHymb6RqEmqM0b-wvFpYCcEVmgAIFLYEEgMTOlrChwmWSl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iopv1dWJcgFFjVtjxkkNzttFEEwR2KLwZKwpr1hgaXMxW5xJEMAS5bvk23PqPJDAGVz7guQ-6pbm9gj0e9JVZ1az73M49MVuE_JWNOizct1jVeGLB6Id5M1d5CRJz2wsq35N6ToU-9QBGvIkM07ZIYZ9GxqoBpi7DNUC_xqMpNa-2gzVd3nALWDJrnokr0DuyzYamyjWVl7LJCgkgzZK0LnoFv35dxIxAVXWo5KP_afrPxiJg3rFEesrOl0_OCVpKGJ77AYJLYAyMqrE46yf74-pdpyHbGWiLjSST3ZsYNqOekdb4enplQMoPYyOzaeo61AR5kAsnEMTfh1KRfJAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbbrMhnM0lRffeNJKsxD4b1njxILZPRl9rC0axiomAT4Owjg1csNFbvwMJxzzynVMJHnExwVYUxbYEnFpgKPhJzejAHK5G4j1oYANj4xZ_mVWWE712GeyuxDrMIPqUnHEMpwayOl6JLOcKUxjwwn9a-aJHxsKDjcIhCRzo1_y_XZLqO2PyMf8kcz0AELWvYk9zXwoaafqQwU3Prt5dLu3gJf0YNi6G1LDaVK5Lh8urdstV4c0UAWvxmU_oKLUewHsIWWOAlzwt0XOiNE2E17nPCtPeY4vU-LMQCqr0DDBkVSzLoQchl6e2DOTgfbewg7tOxkfMLR6_nYJUqxc7QbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXvH-o4KeFEywPDTLvoAnAfRaZCmSrl5onPKinxPv2jQ3Rm-MWvLucwCXUFvee3bsBP1Af2taxbHS9G854U2iE8GiJsiI0AniFR_k6p6c0eL_Ry1sGyliteEpoELnj6bVwWgsZS7F8yDC0-HCklNppLcYtMW8pKhtyTAhgvGBylayAhRCLi_j11uNa09BYifmrrxMqrvFn6-T4e7NbWKNRLRV5W93FLEwRd0Ryh5sQwhcY5LS0p0H2YjfOGxyA9najb2DtCLCAlqYWgJVR-lpp-Mz6JWN_fpc_hpqP5SrvQOYbLwxxUNPuHB50uyIvMQ0odXfXSStIlOr4K7nH2tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8wIVs9xwH0m06Co4hqYGGUfAL58wEy18XP3tkK_HyHHU06KbIW1VRIUXi46k07ewBEmtEx3HSiqimeab32hmHRIq6oPA_WvfGMFKL08MBrDPwmUN07NX_F2XVjMaIWyf0HBZYHcfRurfEmS6WXzfzAOzVSZ5l2QCKNwBpY4hMcn-fzl701YQUK3fQElS8xNykxvuSHOM50Btyqs_G9NoW45iCchV6Ytg2eEd76X2G8BjCi4uyuEflcwpDigY9BOf_BE_coefbn3_xI5dJhqeLyHsu8D_Of3X3ubshIRMCC8Ww0jIe_0ZkhScBjp9IYmcsbIZIUbDa-JjKFYS02TMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=tuIhry9dKuZp1pVjkvGN-xqMo511Uvr94qjtnRLNHTITWuT8KSrIieP3NGF8TNpI13Ufu-F9n_ABCDJ6ktLSkt1v8cI8qlS8S1PV1y7wd0Lk0vJzTM5pD49OVnAhY8s-vaTz_tp2mf_0DViFda_UcSGyuyhurWOZ4TT9XhFkzeI6dy2Mmo6mliHE8eUlR0SmYGVE7c_ampAPz1MMFh03grzIPOrC45KevRIYlofVWd-dwbZ2e0FuggRAaApDO9-zD_2wgFhHv3jWA7_QFLfGgPcNCm4ieG715s_1DZuP8JW8MvrTtAmk5ChXIg64tLdoRuJ8loIBDnKjVnnyUDg65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=tuIhry9dKuZp1pVjkvGN-xqMo511Uvr94qjtnRLNHTITWuT8KSrIieP3NGF8TNpI13Ufu-F9n_ABCDJ6ktLSkt1v8cI8qlS8S1PV1y7wd0Lk0vJzTM5pD49OVnAhY8s-vaTz_tp2mf_0DViFda_UcSGyuyhurWOZ4TT9XhFkzeI6dy2Mmo6mliHE8eUlR0SmYGVE7c_ampAPz1MMFh03grzIPOrC45KevRIYlofVWd-dwbZ2e0FuggRAaApDO9-zD_2wgFhHv3jWA7_QFLfGgPcNCm4ieG715s_1DZuP8JW8MvrTtAmk5ChXIg64tLdoRuJ8loIBDnKjVnnyUDg65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnWvuy_KhCIVs-Zv-1iN1B2iZf6IY_TU_yYXbPN8tttJckVQHv4Cyu4eBLvs93Fu_v0y02hgmi2iNdWuCnpzgMHrzyZXOpEn8Rw-IFhD_qVyIb7PNmMtY1ZbM2--LDmimdZOWXWZ7w52i0MDm2tyUQOry1nf_LsT_6L3jRYbo4cGwlLnLsFQRtZaM4JLJEbXtoqHX5jkXT3t6Jz8qXIJPayRNDzLXpE_zdWdy-zUIhFiT3PnG2X13mePqbFhQZiAJGqUEFPpWn7aXJ2FISKMQRjGqwWlw2kXxrXjXtaJn99ktatzdL1R8v5DXrqyBsoc7cP4cG6yNxj0F7h3u5I1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odLk4n51BRyekBtJqhJ_GPen4TfV42OAv6UzwZZELVVeH4nbg_lBWTv6nbbdSqPG4tFMJRNxZMpUXKVwOxfDH7bjHZJAUZKiWgenB3T6w3rPyAKpXRLgWqsq8npPxJmC52vpPMRHCnjd2nbrzNpj4E7MCNLlroi8dZl1-fkFHsihsZd8VLbIKQPRhEPC_YolLV9lX9I_zHNkk_5zsvgNmVNjAJJyiAwAYAStFr0_r1keCALO_4eh2sQubuMUid-AKD0uKuZ5REWeg9fPT1YgGrnGaHvDaZom7eYPDC2J6st3Jwjb9mvv6IfkwrvTfNj1m-Qs8D0w0Wi83Pn-KvpKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5sUuwXae6UA95ZJSSiWIHa4weMIF5-32kEfr0XtSXLWac9LpDfpi-BUx9SXDx673iv4Zp84ndGpv-dHsFkrla2gyVKavqqs-1BRMVWq4FDG7jBykL_uwB3-p0vo7NsTUxg5ILkZ5RHcICx0W9VWepFD-Luv9JNpaMLx0zcLSCq7_IuV2AyotFHmgM6NkgON0XyYzjTgil1UC3FIXCQ1CgMdptJRaJhoQSz_fNcciD5AdNmLxxb8cL437Li2YPRuuv0OzR6Y1GU-E_9JEWjV4yKQuPFM2Iim-Jkd-nrCGa89vRawglsExk_TUGUC78VjO6wN1Nak1n5D8vWdQ3B--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyU5_108jR8CrewxBE_RJEO0NMmLK70sgfSwTcvNGiakszUHpo0kadT3q9LOjf6WVQWb-O-7GcWpNlnOPf5L1HDt6rDIPwmQYSvnnu7vIFHpqnhkzLQ2H1ZX6LrMb5qoLPOhZD8QPE8NGut0fDKLduxtyq0geb4ItcVrWPxUbSl1AoiL-oGJbkw85UdsrXQVje2V201UoBNCAubVXy6V1hAXPYIEnb-A23ZYF-oAmaQLsXaOIuGLlWdlep-ALxW4_19jxa-kFTqpQS9lKrCtd5YGkt_MTJwYBJCXCsrSURmr2vONicyjRfbEwd_VL-qX1AKs1FJm2sX7iKz1g7GHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DohZYQ6xEPoFcLc35FXhUfwvLcsEDPfbxqaJa_GoFKn5rDG0Ot9_XF8Vvln5uwJaPG2O_S3G6m1vSncoYFxwVEYXxI0Pf-nRwAk1dcTRq2_6iVzqjTeR_IJmD3W9UbmWGdLkxSFAn5mQAOZ2Dc3b62Eg5xulvUzmZzCO35fNkKHRwnZ80suy55kGGeqYAddndf9ej4PJAoiRJJmgXxP2cDYv0PHLGa_8d627kvSSDBqmLs50RfMn-V8qrJENqyo7CwChchMKxnDLVGIotkQhjgZ3AyXwfFMH0m70ipHeLBVp8Ga4mqxHnMYaXfmZjYnN1aYpGDJzrMb_Ht6MSNI3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=eaqbDif_8Zmtqn2fr6TLaGReJnTSpe1Cv4VFu0NlxU7mhvFGoagIcxAbWd6GCDElkcbWpa8wmjrBGJXCFHuoW_IqvOXlP5LVyLCvTzPOLKH-XGF62Damo_OB9rFcJd9rDCZMvuC8ClTLac1Sa0l48qERcbUDbGPdHRRseJvWqx4UWThVsVL-DfAxoyNXnTwg5uVxa_AUk0wei1Z-hE4KWNsuWsV1LuTGn5XfPWaiMNZYxqLg8uSpRO9ERFg8msw9HRkHR7KCzE-tnPyBQmL6WRwZwumgmCgjgWVyLABQoqiwpBi_AacR89GuN4OcCJs5UqiWNL6pMjaRHHFIz-leOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=eaqbDif_8Zmtqn2fr6TLaGReJnTSpe1Cv4VFu0NlxU7mhvFGoagIcxAbWd6GCDElkcbWpa8wmjrBGJXCFHuoW_IqvOXlP5LVyLCvTzPOLKH-XGF62Damo_OB9rFcJd9rDCZMvuC8ClTLac1Sa0l48qERcbUDbGPdHRRseJvWqx4UWThVsVL-DfAxoyNXnTwg5uVxa_AUk0wei1Z-hE4KWNsuWsV1LuTGn5XfPWaiMNZYxqLg8uSpRO9ERFg8msw9HRkHR7KCzE-tnPyBQmL6WRwZwumgmCgjgWVyLABQoqiwpBi_AacR89GuN4OcCJs5UqiWNL6pMjaRHHFIz-leOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgNGDiOYgnwihbnio2IUXwe0_B7o8bzUFDPXVgypQ21eaqIrNaaiNTrnXCwqYbA6u5A7c1TFzVobpTjvlcqQH8yKr1tB_XlKf9lP_24WKo0-1WTvPm2ii1LAZwWhH3xK-cEeWpy7_GUBi4CSVaP07Z8dog4BHLeT0MjziEhxPxGoBTX0Dj51xKzwpIL3vy4bVDf0MKxVccXGDDRo-TONfh13n3ekBElnJ2DwzRQj5ACAX4lcZyKsN3IohoUyUOyt9TJMY-K-IkiQtKBC2foT7QI-CZ_r4bygQY8v6Men3h3YU6IvVVnvZJMfgmfTyTrLHykkgukd898X9BdD6Et9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyUlmJ6P_Iw6elT6kbshdBRUBrKLGtZnBaPhkZeDWSDmQ2sYUF5CGlkLhxVldUCoG0GMQ0PngNFdQ5l6URkpq-e4nh1pnCNQL6o_zaqz4lF5LuXE4bZWEOWFx0hHGwEaqlth_EdvgbImRU0vSlhU33BOIansmSwXZcuVPICW8L1qqrH2NTQz5z7rJ_MRRhhomlPxFxFl5qfLS8SG-K6NBu9jEqRbBgOszc-CUMbOOkll3MixNTsVhqSwO2EseKxxCkiT0i_GlGeXPl8WCEpfL8jRK0n5fMyw2IAn5Uk7V-M17akoMy0uYPzhDP2orBqJRD6tITLMP8kjbfQzy7plDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX8em_EEl9Jnt-ydp-902VMn_GCux12iUmQmh440swq8gY2Oco7F0hXZmgsnty9KTC4FE1pukI2O_pzB2PdShQ9y4JRl6GUfs59FKTWDJnhXrFlkgsEe0lPMWfxEt4pcg_IKUYvaYK_DGL_6zyuFy94lKnm8zCfyvoF1SnjKU6vxPS14JCWlqbLZiJMYWnMzQSE_SvrdW9b5N6MeNe8jIseVu-IlKvn_mO8fgslNmQapzg_r6J0N7sTOvL8HOSP30ZmxnG2jBZ30yudD3i_My1v1F1KlA3PoR2yI66f21maP7rguTgDMULG0peEXWIljBH2lu_GYuPwF9eq0OmoUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzDyPkm8cjPhMAHEZjS7y4vUTK3kNnHyOrEBgVhXvJDwi0oOd5muBVk4shzE_2h4UElyGEzMsILkfh8NSARY7mlwn4rWTtsaMnLk75WArD7mM62SPR5JstWiUtcGmp14Pk8nqQjzB5JnH8mjEFqO58tR3NGxZT-VABVtOz56x6Vzd15E_UaXX2Ig3vA6N2NkeamRjrM_KFyvjZbOWCrAszF61nmXotiTEhTxliUHpuGkd3hzQUc_u6BsaHhWuWF0_1g9BsvZpPBdnB5v4IzWQV1gzixw3WIUKPOw9undKPwT2XRSmeMJDOFP03Z7DA7i7cgDGsEJhxbYnFuXl8pWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXG0SqKIW_hyc14w10rUAip33LUnwZyr4uyBilNSgJ5phGLib8zWztZGApb9XWeRrtcaqPsrNeZMyeoiXDSbIa_tGduA0YlJ7t480089OWn77kWhAcCBCAU7YSwcLZ-S_PhUGZNrDQgA8_t812JsFhQTUXYHjugQ2J2a6LzunSPBVyCK08bHbeyrvfP9kbxnHYyHbvDQngeB74cl7T0OPX2n8BcLU_qp3I3-O4dftRp3KgUXa--wpubF7EusAieX2KgeV5TsV1Si69XKrVWyLKnv3pENKeDRKUigLZgUW-08p2fDvIMM1IUUL9RPyztPZXeE3zON--PzpMzqnELrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=mM-PH33LQfo_tOgOZCEGMbGKNLN_79HCRMdUrpFX1tQ5wSI_tcNfJXvAKhT_H_cJesgVRTWuFOgTNhDaeH0xUVlYDWT08vTZIRi8S9AuNbFX8q3YTsVMVLgvjwhC4eCIdjBh5YZPZRWdmc5_p3C4RRCLvdKTDoQihjU4r-6h91-lYZn-GrSOVMWX_DiKUkU-ZQ6uilYjpP0pXEbOYtS49yhY82QsJxPgpRZKn5rn-gkaWVQiQXY1qPmUvRo_3JeaxyUPa0NVdb-Dt5nPKpPV4-u9FSA5vMvrbdYr5x3RoMejLnFMt3Lvk0TEaVOzGVGwxHEj26dKehhxMxS-hVr8WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=mM-PH33LQfo_tOgOZCEGMbGKNLN_79HCRMdUrpFX1tQ5wSI_tcNfJXvAKhT_H_cJesgVRTWuFOgTNhDaeH0xUVlYDWT08vTZIRi8S9AuNbFX8q3YTsVMVLgvjwhC4eCIdjBh5YZPZRWdmc5_p3C4RRCLvdKTDoQihjU4r-6h91-lYZn-GrSOVMWX_DiKUkU-ZQ6uilYjpP0pXEbOYtS49yhY82QsJxPgpRZKn5rn-gkaWVQiQXY1qPmUvRo_3JeaxyUPa0NVdb-Dt5nPKpPV4-u9FSA5vMvrbdYr5x3RoMejLnFMt3Lvk0TEaVOzGVGwxHEj26dKehhxMxS-hVr8WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlSfgoYRy46PuL0DBn9F_k0deDdOO4J3ouYlwPDQuDfjEB9UzZizovwHEz72ADgMtoAvBRyWeQIuhj6sJjv3APa05dLT2nyomM5OH2Sefv3lQ3HOPO2PfSyqnt7inGk5vnulDuh2j0iFwd_fboURE7m2JeyoY2CkqQuowWZwqIBMngJWVxzdKFpNa8dxoi5XlmYPE7Dd4LsYfO8vprxLdWOjzqkD8-5MWdQAdiaIGnMQnCD_mJD-qTBTcsJNydHstqHLnPis5IYqiM3ZmlNYejFUgpeu6AOypg14cARvqbL2ue4sJgX1WgOV6ehoy_ebM2cxo_vCZm4EXpdOM-FuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7WYFPA9tA5qGGzvawIDZgbvNfAvhCZI_pVY5UQwrb0eMnDDrR7JVvK7PZjP8GybMdUfK19ZjJYuL4SqYT_Vwy4dBwuHLYjGbeE15X3womKH4NHhY5jgogy1J6xPn83EpHAk6rmW1-SjSRnPQHv5_4LacE4ymGkbiZlA2eM0gSl9WXQfxezjFJxlZ1byDPEbHQdlK6fEOJJk3BRZOCJWnRjgogmBuAiOAkzo1JQiz8p6GL4Wyk3JyL4XvZXYw2IBgUPErJJUkwk589X5sX1dKpumnxlvxvb7eE67Y7WoV3JKumh-DPHq3rW5gpC9VFXvC_xp3xvu0aXaYQg04tI3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J10a3QmivdMhQeKjGQeydjOUC2SyMiG_CcouWVvUiETFmPd5Asfhhj_Ge65PIC_Hsoxdmx-HPweA7F42iNuD515mWPzjTC71m67zmKZky_-PAPZDKUBZrJtmFOBr8pku_gxlgFvw-o3arEcSU2pjqKEwAGHQkmBYkhKLBR7zzPJhV0DTb9WCjfS93G6Dv3egkjTXghsqUyTS3Aar2wY7fmD7eXgPDGn5-Ki6tckW0lVh6sGkoQQwObrmIpYgY8cl7rP8ejx4h_fV6llgkTH2CbnysnxechjvRFfnSJEzchtIL09rcjFQsixfLvIUMo4VqlxqCqzi20JiATTeWRejzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXsiIj0oXeDXW2K_w_uv992aH0_Hfz4MbRYRdfe8iaft3e1zuJ20lI-qqB6jrRLDgO_5ROEnGM70IkJHMp80WRvEo2iZ8GGvdQSnY_bkXMYVBUHPR9hlehTU_5K16x6MA7iNhZjtsWJEkKQGiKCX8PntmwryJ-kyVXYl7fm5RfgeHY6t8DjeuizPChiQUMZC4XCx0VtlfLNLX_VYehvK5yMj3ekez1LwGTmQ5QmxNvNJOHTZni7HHsK2ZpZp-48nm7MFhTjvrGNdbrcBsNnakFx8D_pzvJiCFCQcPkBpQTfL3Krz5-gpF_MhvA_GEokzBjLpmPjoet17Q0mWwluFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_hr2yyPCkxO9YtjNInuRRZMOhPWVOVfTCIOce5NJPdjohYssZbfLxsIZFlVKGyTRVeVVKx_z698dZBRcllfkYTw1VFj1JBDLHww-iLI8m2nng7X59Vzi2DcUae-LMiqkiN3XRZaqjRPI3O0mnzcjEN-vtKl4DJf3lTz5CXqXmfRZ_mkbbWqhiQFncP6aT1yIFlVVa2gXiJMaeK_k3alzEw7GlqQTDwiry6H3DDUPxoPPX_Srred4ZmFTUBuNArnveK7KD_Gh-rywHNyCCtGZqgvrkRzgHbC7gS4Ct0t7oF-e8Q-9-itq5Wpu6xuLVP_eF5ffguCfDIJWiTnRDamNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8ciwIgPze-e-3NS282CnHD61PzCQACC8-iVBjd0nZ8dxHwj3KJceH2M56EtRkYRuQ6VEhce-OJorfLWCrCToOCLVT8s-r9Ta0DOt3Afh538Ay_jvVoE1vsLDPqlyB_80gCRNRaTHUNZybbLmfm5xGk1qjyFmYCYphQd9ym7IR4RFfDrpfh8av-aqn4Y_FNzY3cBtYXAwWqJ2xOZSICYiYCOXfFxlP0FYiWK9AKU6kcAqRntJl3IGH2I9XLpwkriMGajUDlwkwF2sn4_cvBAgW4x53J_HDWgy0RR1ersnRtH5r-d76xlEKh8DmK2MtZ-42Awum38YuyBQmWwMKXeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woxjrg4h7ZWkx46CcDEktzp69E7_23lfU_QUvtqeuEGW0ASXSHSb0SEIDWsQ2KH67AOjXn1Zxfs6FhryQCBWIR0JTfC2xtAOB-Apq4q3YlOyaTOQro4i2F8_x0cGiFlAIXYDNspZY8zMrxSSEtCzNyu-OzbPF8AT-2F9FR3JjwUvZQWr7OiE7vOou4PY1n_BNRud7BDGDLiDuQLMp3KAr-rCaZHQuKqwNwqHOc8swf5EqhsyxmhF95g_A-vogW4WP9yiOrJWqusfy_PirCaR76-3VYi1YZPYIuZ1-fWVsvLeGCM5Wl0uPNVo_XwvmbguvEvGUpDp9JLPXX5cboGhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=oj_NhUK-YRJnWigxfwcQsHgruOw3dQ6TkJ_GzB-f5v8mINNyKw7irWMQzvYWB5MUDXOYZ1kYJEkZMtkavx9cGd0LqJ5b0-WXx51ZUj7uYf6ewMbsTJ6HYlwq-ZL9MVcZFXQjVmWBV1womcFLNw_skA8z4rpCMxU4LrHp0NSkgTDX1rf_2THtWrDSX2CknK_qNyMSVsrWqJVDALHXZJYulW1mdPt141KZpkXnICljN6kKLJi5_VGWcJ5biH_beoxR3aVKP1-l4HdodbI-0XheOa28Wi8raSxjAryJvlwpGAxZIMyb12jm5r7_yDK7odPjC-8nd-nmigyaHs4nJYDDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=oj_NhUK-YRJnWigxfwcQsHgruOw3dQ6TkJ_GzB-f5v8mINNyKw7irWMQzvYWB5MUDXOYZ1kYJEkZMtkavx9cGd0LqJ5b0-WXx51ZUj7uYf6ewMbsTJ6HYlwq-ZL9MVcZFXQjVmWBV1womcFLNw_skA8z4rpCMxU4LrHp0NSkgTDX1rf_2THtWrDSX2CknK_qNyMSVsrWqJVDALHXZJYulW1mdPt141KZpkXnICljN6kKLJi5_VGWcJ5biH_beoxR3aVKP1-l4HdodbI-0XheOa28Wi8raSxjAryJvlwpGAxZIMyb12jm5r7_yDK7odPjC-8nd-nmigyaHs4nJYDDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7Gi1mGbOBYLZWF97xnjSwUX6ddxA1toP1ujL__aOnAvhOwrjsYWGCIzVNadu3qNHZkspOEZMWq2dJ4RdMrhIQy67L8gwXN3zTERqOYlbZmNVbocCNXF3fbVC-tORORu74Nlev7G_uM41fcrb68GIyx2BVMFgdsKGacIlFFtbVMtlC0gc5MhfA8Vv-lVelk2neZWvxZMr2PpEtuUZkk1CudLHQbZvvE5oaEysg4lV5uDP_HfwTVdQiuDoH68sYpYxLNYtg3DUtl7RkHA2e1frSUaorKZEqAMTNxoN3LPcTdMpXHyE-I7xoGfNmUqzBTVf-9lYFr9GkMidrRNU-dS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXyET77-sw_MZqnu-mnipAnkcPybYZh1kLiTfisZ3L3zDU7CbnBNZaYYA6ffCu0PAw0yuFzG0eIN-6NsvkNUBOLAXIJcoHfs3lOkkhGo9LIaAQNGvPjja3J960Vm3tcB4X0ZZzOyWsdXbJECx3zpW92wnqtWox-VCQIT_1TVtfBHJ08RUJlVH7tL6NtFcRB8VB_BE86fdf1SWaefrHC7O-K-aA1H2qdu8r4W793ANV2w6Y67t6FI-WojR-YNxph4G4LvfkMQ8YrFo_guGPXF311IziEoQHo-JsPVFZerEej3mhJMa6HhmHlCdZQvVIzFvANIOaohjfdtJ3aonSF3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhlB7gyR40rHXJuHCYH7B7rovf6QyHQBhnBgPF7-SZoT3S0DsvYOx72VNmTda0gz62ANT5lEeIT9g4FArj5mxcBxI3AhEeGPdK5cB5KpDNwvDc7_g52RbSYVyPNwnsR4vCcQK_oFSy04OicZitbUaKvTIqvEcZ4pvEmzETj-MLLll88dBHs1m0dLxpLJVM3mpzc6cHalIkIYz5e19tGOnvMcutQOzymUwrxGc-m1JkyGxWPr7RTjTgNY3hNZmkPXxU5Daw5nY_GVS0HLVpvTds7S2lxtFGlDTl9XA8gVtERAw5elvhWDyRfn4FnbKxIH6uLntiUhL6OekWxn_NJWPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajFXem35tSPkopiynm2pYTOq6vbhYBD0U0RqtBP0BwMmB3jL1Ho_TPI_XxuAvqRAhFtMoJ4AmK9QtnpUn3X0PMGe0bmrWpWkD2zCP2O82o6Lrq4iwF5--410mu0HOBqJvfVbkOImkGXK1e__efY3KFxzHcKx9LqVTZSCPYaF0n1xwoX54DK1nY-22ljT_1sfmZLpJN4RFzH0WpVYiZaMaTz3qb7FB9NJs_40qYnSENyhmwHHmQqWxYuTmHW_pS8oYwult21zEc-O1z1ufedV4v4JH1zGKEjdz0Y-ECf5xnZ1DmqcT37iC_XE4poVJtuzHI6_PJX7oyhf3qWAZJmn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYJ1jNc6ZqBloTwTQzspeJlc8WTSkKE9ZxUjEvRCNhMzTeLCGHy7dwSTyG7YCGmldzNFplX8LdDgj87zbkUy29UL0XXYL57ua9hJOtFa8ZUeRkHOGIfwEuOa1kEF70fyVrXNwwX-WSB1A0Oeh1OuWyA4r6d9w11FSjS7brN5gu9sFa369PiPojTC7Bx8QE-JiPhHA44Na8HsSmsBmhNqnWn_hGCVBf4kQVQsV75EOUfKQTv6avMonO7Rs5k5eDtbgnE2bLrsPqOtsu7I_8SX7pVJnLm0WROYzyq0GsPNJ4GyiRx8I9aqcd2I220OPaBf5TWOlqZhN6k-ooSrody2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu0TDisJVRy6Gzv4LOVLDbq06Nkriz0oUqPliYpVrEtX9f4uSrvYj5VC-jfYIqCJ6KxdyyFJbe43B9oMVEBd7Hd7McHIlcVpxEAIkVq549YYSCqqhjBC8H_hJjWRoJzno0k3sz191LG8vWhBkFqpw5VcToptZ9LxZf4CjkRq5WVI7AxO9rOjIpVb2HVC_mcfDIDUxvSOum9f9tudN3n63q6ttTEKgT5BFFtK76UH7yPwLUt9j9uQq10H18UPDXsxFSkWPzH8PDqdIa7HkG91RfPLb6i0nG8SAuBOHd5KX_ERbPDSMR9YUeTmhKK0Agxy8vBGfx5Qyt2MCN_snJrl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRJQTT2g-LYj3BeTPh9wqMQI2x4mfmewpiDZwQqHD0YHA6YRwS1_PpCZuPBAxUd6qYn8QVohacsR7hBgdxf4s1kpSIEmESzN-hxQ4Mrpj7abTtuon56YBNRdMZGQHoBRSOMH_3S4p22DWo4SoCOgsJDipz2aybz8staVVLwjgWCYfiLS0w4jwqxKyQ7NH3gnQZcQQQ2lgigFAzM22mkVcY33ZCMas7Ei1s6I9HBadss69nKFqhhBXOsZdgDEp8fvldCRMNiAvoF80-uQN95Wbhuym3biqOGzxH1BEYls0-sNcU3ZHdSUzzn6YIZ0LesqHguPcf4zErRdcYkuIszg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chO58Ph8fQzKiaeJSXecLA3UArISiMayPHuN8RBveRg63QsCbQqKZDxnnjlwMJ9FXHLYrDrt4ZHoJMiMIvybg7-xvpq6aERVX83MuM142-39ttUkbtG3DsrBDUr1xZby1dk2lT9GJ8WpBnwGrlOgLWn9H7H4GuDzROD-4V5a8ZIgj9sm-jzXR6Eox0fAVCLnhtcfIh5rj8rI0NEXomT3yEuhRdpN5UdiKHEBgpSiMLHCD-se09rti0CzBaNSIylfAn0YNICR97A_oaCcfb_bJfSw9gzQhsM7jrpJOMboBeb3d5h5apROr0CL_HpfM6ksR2gt2-j1WZUcBOXm8pucLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrU8VFRDG5empj0tT21HdEjZETut7zODgWjrUx4Ks95koZchrd-Ke0AW9TkwGWptHoczBoEOnnwbjm9cTrlBRabqQz2NIt4T-XQd2ZgFV4aSOixIukyg0H93nuqwwF9pzmnmGbbcjNjHBWIBQkZNWqJKUkG9hoyXos64e3KLmjs8hFQBD221QerKbKsQMLwns884VchU72s_CELUb9IAEb6rv9UCQ8-ulSCIzPgSQ6mATeQUzSpm1zwOq8sBT3ZGcBx1iF9xRWTXGExCS9zp9cKGd1wp9uVgaqHmLnbZEXEbO3ebo665Q2BQF3MNES-28IC-BDlMtIMU-sKqaTkR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=IwYQeBW4lHfZ2mWwdl12r-WOVGvgNxdu7m4QFYH_UE7dVcj-FPm_xjE7UTVuZLJJHuLiZBMTZTkU-z28b27Nm1YMDyzZJ0egnTxGbmTM701SRc6Fhh-__ZU682N52Mdpu2IDk8p_0cPBYRXgL-7g6X-EKNM05fb7Sc_EWkLDQgALOm0ZQJNBSFC1FHxknpKiei65tZ0PaUeKhewGiH62s5D2UpeiAv3-0k9B-FDJyKDxwdNQI71wp0cpQjN3ThjfzY1aMu22FnZctw_QxTyl7Lqk_rBqjkn0N0cJvdqpJfMnu-68g8taKaskuzRWmLILrXfYduqmVl-BRM5gcRNqvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=IwYQeBW4lHfZ2mWwdl12r-WOVGvgNxdu7m4QFYH_UE7dVcj-FPm_xjE7UTVuZLJJHuLiZBMTZTkU-z28b27Nm1YMDyzZJ0egnTxGbmTM701SRc6Fhh-__ZU682N52Mdpu2IDk8p_0cPBYRXgL-7g6X-EKNM05fb7Sc_EWkLDQgALOm0ZQJNBSFC1FHxknpKiei65tZ0PaUeKhewGiH62s5D2UpeiAv3-0k9B-FDJyKDxwdNQI71wp0cpQjN3ThjfzY1aMu22FnZctw_QxTyl7Lqk_rBqjkn0N0cJvdqpJfMnu-68g8taKaskuzRWmLILrXfYduqmVl-BRM5gcRNqvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdJd6RkkK-x6uSTfwqaQpJYQJSfBRCufOVS7RuK7RIX4bJcJ4u6geId4T0Y_OH5ftm258nqAiDq5R-gSKs5Cm3tlqdGzMeJY20LnAX2uXk-DLrIz0r0l8i3ss28zba6GFbpEm3rzcVZleIAB5LOX4k4ujPyMwq702T5qguJ616G-DzCbRF2LlaCz5umtxVUaoBJ-lEXXct_jD9E73mhifIEsNFElO7PRAgsqjYERPinUOhE-ZXDBvkV5HSOW4N0Pg4A-_9ayPz1rCxhAUdoUx3M-9MPUW49sYUmqUGmz8aGPFA35L6hpt6nN_zUu7QQzSBp9ygQSWXcDOknVcG6A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwLve9P0ldfWj7qlSl6cHc8I4w_qNB5IMrqUhhbxSc_XMEgmXwMdB26co6h2rP4BCWawsV3tI_C46euNgf8NCEpYv8kT1qrSHfqk3g9AyNxFDDRB2e63BVJn_c_msPL8mrQluHZ42xj4bekQhHmCCoEf65l1tuJA2fPYC_F6vSksC9miTlanFzoJuhWntEZN6k3oAWeDv8WVdQNc7PMI4ziQMLNQ31G_03j-cP_rTyObwvFaq29OikOT8YxnHu19T8vKiSUZ_I8g5S8Dt3hhNRai-0pNsls4xoLyacr0i5SRM51onD4JBbY7265sIMd8Xrbzbur1GVdj-jqD7Azgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNy9Olf-ylCdYdIANVyChtgTNoBDRvePP0VH7lPmuqzQJTWA1_WRxBBYrzmUWYyDoixGCtXJAroN5GVm4xTY0KoHIqNe9LvzuettNKWbzulJve5CIoA_dD4LonZSsPrpLH0zsLjRiyL1Qu2z_dqoHWcMpPh2mo6-QW4AFrkgCB_tDTIrxUgVPlz8CJMJNdFp0wMIU7pVHeMmZJC1mHlokvsKjKbjtmFBVdV-9WOCQ4XNnwQlOaMf1LCNbV_mHKJ8SYpyA2t6zxpKhs1ab_FJ3RxWx-Ob4p2odfyaH2VabEysGgqkUa3bGa7g3Q5PXCBfrWwjTfIOfPmGg7bqsklT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cujyg-QSnb0SG1Axd2xYz8Cz8iTOMzV6bv8rMHBjKTiwrY_kg79CbWPlvf08QQEhzvSOZevXft-ok_pOjQpJLDRkon6I67M9uIyIxmib93P6wAdzk7j5zYkYZMRN5akuSXILTLc7qsX_35EOret2vA4JJ4UBFgtnX__tx08q-pgl2ySXp2VhAbSOxw5xH2hHrQhfAURu45TaQ65MJxUFPGIgyF3tOWKYmjVPYEdoWGfo7rlZSqVdXYBDjwBZ7ef6kvvDdidex1iIcahT1xz2xyVyzNXCw20oxzU_drKr-WC2MlJ7-fbUrZNMqiHjVK7YYGW0cyyvbvEcLn1NrctMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
