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
<img src="https://cdn4.telesco.pe/file/fqcG5RfpsVYHIqZrI3_9H4bDSdhiTiZg5mSHK-bHT9QE8ob1bFnFNFRMfguH-WLyBjMPtg5LVYKJcT7r2T0YIzq8iXz9V6CykhXiP0QkJhY9_STBEqrXr-nwA35b3sWLggBrHJE5WGRJLDUAgXsisZsHu7-cBvcP1Ns4ZfznKbAv08Vxj34xHNuUfVzq0Dj1q39lfLwSe_SsSMeZqVOIWaiWHtLQryQK-RxOqflpGFFXLj7yDiITIU4w8q0Pt5i18V6KgYGJaejFo5fruS9otrJIV36y-G0FDhc4vpb0hS74M483R1Ig_cguJGlC1M4KZbeND3eWJV3epF6X0Onn3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 126K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 07:06:17</div>
<hr>

<div class="tg-post" id="msg-69965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/news_hut/69965" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/news_hut/69964" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAh2tS-sz56dnkjvHkpL9hHqJFLIPT-u1CPbemsg1M40dQD3KwnJ1lxcnXPhOnldFNnlwkoVXXplMgXFueJ6Wu8X7AtUJgKWhqQvJ7sPNKD74t-1C7XdV6_FBzvc0FzdKW3jTqlrvCcH4f4Y3uBhbm-B0aArj-3rejnW_dRSO35U6VfgLaOG96F48CYjCThSOqCklVExlkMGBdQHB7Kh0dv6gRYzT0Qb58clHrIp5TGY5fNUYdCH76mgBXorn5I5Zi0O78cKuVHchLfbOog_B35D0AmzJdkCoE8vpP8es2CbviAhMYgHCacy4FlI-tEK7mnMlRMlnG0rhLflQLrOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJ05E4FoG7NDRIKeIt35T5jI3z9lBXWw4gbLeHPMS9AFwt-y1YXKZRBxsHncMr5xsFW0tljJN4kPD9VZpFdO5rVNwIOP2azOYjxPrBcNQoxdHLQDp8eik5mqGZZyHARLc9M7x9NwNGJc_iBMJhlkNdwKDlk7HJYIrRgYq9AFQvaU331dbJJhD8UwaaNCHanvThKgnERjs9xTmGpe1HUaIVgMkO_na9K34kIabeOBpMtDpTmtjp8twfCERFuqUk-eZ5zIJCkH2e0V5-xM2gb6OEs821GYrVJmEaFr_uVIewh7P6zVM97c7opnl2Ds1khQWFjIcEQ19RzM4GFcJSNmhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUK5bGKadc4ZMBNZFZshFSYrhTm8_g2AI8lbYYj1dNr5ksKgPVDr3Kv7HlSEfm2xcbjepuXrNFOp72BfTWwy2FqLNo95TRrUif5M9LnLjrJZ9bDHh7j5zEtfqHoYoaZw1MyXnVTEsvisLovdjSL9U4xm1aIAm7jOjVFPfb5WQJnl9zxEJPe28iYYgjFIU6_ykOjmmFa5d3a4H7dCrMkStKZsXc_5C3zna-LtOk3g6FRBTRUm35a4zfvjTAsRvuKV6AifHzaIRQJTT-Qd0hAX0d0M8-sFH0llxpLk2tdVc62eW8eLsdFOA4utzgAo3cpwNADBJMuCSDWd2QT0BhBtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRo7CbM-x3BVMB12PAsnV56yLGG_RGYxxEFHJd-xMeLR1-uOWZzn68MbGfM_6R3r-CtSKbfZtDkh08wg85Px_JiG9DFkplKvfaCrIZoktvPV7KQPEzgWlfp6mmVn9rY3PRuQQIrqrD8cFDRYJryTGbdSLJVjZeF0LTq7A05Z34hWsNPC-2Nzci2m3LsVxI0muob3Xsiwbh15Zb1FfMLGqSGhDTDTOKe-ud5LXZHV7GvkBYxgnt51IbaQbGV9SGYGcZcbWZFDIRBDHRxl4avZGmuEf6BffAg1U2q7Y7Jfr-JHEZn2qQkkie3sizE1aXx9X9NIxCEOTxbhdkDGz8JPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXMpb-aewmNN0W4SWaRkz-SJKq5hQ-zHDDvPackLfvZlvlGVOCLYx2yq3uJLo7RkMSOPuukRk3iuwRbEiRTDShitfebRrV0s7xId4FDruIzhpCUwZD4kUOBo7UocIhJDOtNav783YOQLhOo7Ed7_Zb6qTsmt4U2G4i70K7ePCPbxoCgJxUwUyasT71TBOBSFkgygZTKZFtBBJEIfW13wLnmNkWFQus2_sww3GeDF2tS98FixbpItJ5_6CTtaqhUEr6OMULsotr7-PqqlgrHtHo1_9nFlaQ4-Hrnrj9RiEZEr9Dg9ijld3-JGDTkEZ-24wx17OvUFScyJT4q4ehv7_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW2_BQ7qgc3DhRGumID3RJ1PHXXWov_cZpJ2URPQWnnST-5icDSevcO9Ha_PzLSKDF8BO3egInYGMgTTdce2gXg9szK3t7PkBkSU2fOWhtZN54-C59zP1D2GW2V3DPI8FpFGlzi9mFSB4A4nOFfwGlyqLdTr2qe1RMLLaaNjsFh6mPx10mYUX2FyWDDm8ee--_adNm2AlbQ3tc4ZycHLUb3Q9R32FbJOZD8tEWViB0R_MI_iKiKSEDzn-74OnHl4BOWwzllSVnBicKnbrWyo1nS2gZzCi8_9P9ubqPSkl-1dk66bjYpOHewvDZqv26CJ-VCRxk5jUfG7rQYKgHiOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LleA7F26tngJJsXT4NO8V0CQToxfh70C-i0oC3y7rrpSwip0BcuFCGLFBu5LlfyDnTRReLnRH7trLPYCSlW6nwqvd4JlfGwIVkg8J1vLdCdD_VexHWjIZXpJRLdJoZ3CfIiHebI1zXsi3hC5uIaPxkistUZrLKT7F1QL0D4mxqzo0rH5V17X21KhBsdDHNGys-_5fnoODCNlQHL_nPZ8OGqrIdvwD_ppEI3-UklbiHgfZY3TKTOnHcnyWIfzCqAuMDQMvYfXtG4exSm_O4lS_zLvLvVlI0S9YTpPn0QGoqv049HHZ5zYLT2d-Q8vp0RTQhXYLhQbY0Q8AfVmmTR4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiTMKJ-i1IN51NzH6U-yk4IOK-t658PnDdtXE8ADFeD3Sew-ibwCcEmGge8hV_1oR92o5SSoojmFPKc1Vlu7c7QbYXx-1X3MjIQIN4rtHN-gcW54N-4TkyaFkb9MDz_eLarnjwsAPOWuUrGpmFh5pBqgyU-4DD8ntH9T3pmGIV69j59a5MOF5CnGc2VmKJCNBjqwl0CkSTNdDxlhFKZvdhWoYMit2q9fs4xVFSAC0shKFZBvZijtZCMOJofbAfS9PTXTsSfOjutSo0JsVtOA7yy_NGSqJ4R406-avJmGvF0TiAD1Wf73eEReacndp1v_F5cdSTK44ueIMPOx64EXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et06YdsKblZNEbnI30xcjHRLCeHm-D7P3InAioByjMX-7Mpwe-WrsN_pHBFlKYx3nZRIxhiQtp4zvYzNfLRvV5Ztk9ECYygL19Y02xktiNotQj5-hVLl89GafYrvmRQkJUXZvbi87v5juynh-2nFngUDgQeOjQpyIpfPncYooQbLw4UiGHrU8-KO6uxHpOaFr8HbqONz8Ooy2OM9b_Ko14_PzdyUNjTIxibcU1ksj82wN8yE13z2F5v6Ktzs73-6RD7resQ-2TmbGM8Z2P_YHjV4dd329UCIOMAKzS8XQQ_5aHehFuaE2XOB-xlho6P6d-EIVipH110uwxIE-TSghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kff3DGmIM667V1c1190JiDNQ7YEZjWrETCjyA6Q_2m53ZfvJd69MeeXJWSauUXhS3y6BCiXs6h7Rwf6dIPuUL5e3Q2HMz_fgVTTntMZ56TRbcgtAHgoH2aXcHeDcaqQvWffK58x82zyfKulx5bFkzRHCBGMObV8L7zLA2cEM2PhObjQExwd2c6kYC0BFCtVpHan6A0UEJ1oLnVpFkT8orUL046lfjByi1JX38-AjwP2fb4BXJM61OQLIyaDV1E5dowFtzcznosADdli5vOCRVGCxJ-EM-lxfNWhBoaHNVtqHG-XdaGpYip_XYlCABdafggq-oE2Dx9O7v1tZ24VAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vct1DEK63YEq8hVqrmXGLoU0aqtIyoaVMogkFZNxnHbIXa-vojxxGRarV8sRheYViJkeKvuFuLZX6mjI-7gV5fFyc1AtbKnaqqnJKWrmBrRGUoO5CulBwmrs8me2QIGdJSf0I5X_Lv8J88aU9qhIO9ocVhwCv14Y7bkqbPfNXCFWuwjOEhOA_74gUlKheapY0fjqRMDrgC44l4sSt9hJ3PVqcGkntJpjNwGBbHEU5WhAuLGhphPbzy66kdfqu4cPRvf4g4p2Qg2KqXjNtyw8MS6-h6JJHbKIyUrmzAcL0vpH0u2VTlFp-lik9N9kZLhA3TFZtY2oFDkfGdTINY0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCngHQYJ8Px8QVZzaC9dqLFTCY3mLChmHEfHpit-3YQPbsBYsWdJB09e2BeFQIHMh1Em-k2IDxj_4Sl1PIK8MSFz8x2XQDGxb8YL0z_QeFmTCfYeL0P1TvtPKie6P9qWUv6KBg46bm2fgz52Fa0yX_wyUBFa71hiF7HFWCkBDrLAuLEwVir-WfjHox9R480UXfMKhZAh71RkFsQ-LPMAEB5DUkpkF9FN7-mwhve-_azG8PuWNQtCb4ksMfOhbIfH7N2haOkX0LeIaleocPzFXC8uDCWqOXs0awpsmZc-xd2dSQrA3Fl7xbRcehrlLFHHHD_CpnDH7_1nWclz8FLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=Ca5wcIxu1eTr5hGUhNzv5XhUKFYkpxuYr6XXEAwzasacq8QDBe4mVV8_X8Yofasl7Wa3U1CZQLCtmzApLpMuIo-MsGbt396bLEwrOo0Zum1fbECWT_n-yM93ROzR4qMXB4QJecTsNTzxEMhTGmBcNxoTYWhROh1ix0MOE0IZTaVLXH1oTP99k25eFskHWwJf8c_X-SAk9d7apY6aF6vHtIUM0SNkawaGiFx_bClkkDy_BLvf4ZhtJ78kuV_IqLsE-eBl0bJi6NftajeA-QIQ4IBuxvA0rDMFuqNqkSQy6XiQEaEQpnOD_7R5HW_FIO0Mp7F73uxKn03uNVVx9oSHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=Ca5wcIxu1eTr5hGUhNzv5XhUKFYkpxuYr6XXEAwzasacq8QDBe4mVV8_X8Yofasl7Wa3U1CZQLCtmzApLpMuIo-MsGbt396bLEwrOo0Zum1fbECWT_n-yM93ROzR4qMXB4QJecTsNTzxEMhTGmBcNxoTYWhROh1ix0MOE0IZTaVLXH1oTP99k25eFskHWwJf8c_X-SAk9d7apY6aF6vHtIUM0SNkawaGiFx_bClkkDy_BLvf4ZhtJ78kuV_IqLsE-eBl0bJi6NftajeA-QIQ4IBuxvA0rDMFuqNqkSQy6XiQEaEQpnOD_7R5HW_FIO0Mp7F73uxKn03uNVVx9oSHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=qmMiNApRHc5HGw3xgVdV8CSulUHMKsvfUL2wSQnuWN6bgRc2UVb2rZKnCMDH-vjej2HQznFtYatigltb_XyiAAh8oPzhXiPEK1VNd_OxDqJbqQ5F1AuAtm2uiFis_vGl2EEkGsby1QhHME_7jUxumrd9fpJpnf212Q5O8eEOtnXgCkTbgAcDN2-deBAoXYK0zweHMsYGvw6TzVPqlK6KHKkwRs-2DXWvm6SYAwq8fvcZOA4zGCQl1icbAo0XvQT-bBH_iVbrsVjX3igx9uCfqVekWp0WGuWX9cp1N_J-VxOdckn8VRT8YuoYzLYbYHvMK0ByOYGHAXuH2qY666SK5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=qmMiNApRHc5HGw3xgVdV8CSulUHMKsvfUL2wSQnuWN6bgRc2UVb2rZKnCMDH-vjej2HQznFtYatigltb_XyiAAh8oPzhXiPEK1VNd_OxDqJbqQ5F1AuAtm2uiFis_vGl2EEkGsby1QhHME_7jUxumrd9fpJpnf212Q5O8eEOtnXgCkTbgAcDN2-deBAoXYK0zweHMsYGvw6TzVPqlK6KHKkwRs-2DXWvm6SYAwq8fvcZOA4zGCQl1icbAo0XvQT-bBH_iVbrsVjX3igx9uCfqVekWp0WGuWX9cp1N_J-VxOdckn8VRT8YuoYzLYbYHvMK0ByOYGHAXuH2qY666SK5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZbvVZ5wn76Met5Blz1wZlgzRgPZp30JIKM6kGYPDKd6hHx04VfUjl7UFvk_FtMtIbBZgbpOxEbisKH1maNy6b1k6Drooxu4_kMOaW4y5WZDJYQlFfFQeA3-eDyCbMTdAnNOZ6ufj5EDOcwNQdp8m7poommTiYKHFWkGWC8PhZAqvtVvv8gKbGicN9GXyzaEx1SHrcqKr6iNVUlwF5ZYLMtNNA3L7rifBEFDcWyb6ptTrdZb0wDWv4LxL908iZLbUFKCarZegB5FHhm7j6N97-2T8EOcibNN7ibCr2fdPhx0iyDUIJ499xCatbu6339rP-QO3oADMqiUEnKWNNEBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umWPd7Eo2RiNMUkg2m9LQNnjrkjTUFCBrv9j46ZM6qap4xZ8_424fVJKk5apGymt8TY-7Ija8qhkoaAg8PMyLCdBjAlbDOdwLTLbo0URT59KGa_yCgfM14_dNYL4du7HC4H12cbrYm5ho2JcFEYiwLkPZ9ZJXuLDgEuADVE845FxBpQtdOtc8uGUHy64sZBhZZE9gVDUE2f79eQK-0nSpN4hQh7j_uoyr1AaEec6YeYFBFlKVmTg9qqlLP5hj8tWWj68NxugUcHw-3XWCzmAFuRzBjwB-hUAoBjBz3jFF9uCU-m987E9Ik51q6bPSzSMPwAYYKMkadZz31_lAaC_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8Mv8dX-CDEcKHFbMZlxExsFmY-SZR0bYA__MMfvWSwPhB2zKIqPPiYTNde2KMlJ0a63hDh51r2sQx3xvx3SOAgT3eHAPr0O7t42dqxDW1o16XLLEnDboDQJlaEDMfgwezcw9VnO0XiH38T_NMtJJ8dLnt5eHTusVI2N7u5yKYVj7cfCwXUjNyhLxa-LhyDy429oq3Ex4sWDLlmTyjIkPqpl5rgBOiKzk964eCTR_O_kOe5YIxaApNYD4284a-abhLNi-TP5J3RsH0oFfOzkTxqL3t5dUdXQkZINUIh0j5OPsBTwKLN5i54MUyFdCZtNgVXFFc8N3mDKa-vzGw_N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLYE6454VuX8BTyGaLpbVDPyDosiKCwnGVIvT6kF4jbuTjW0Rd1CYyTlfjaecypK103hgThBNCaAS57cy4HDjM-L0g5YQCNB4PJMPXtCUy7BvAI8wV_o5wNoQa2j7yIlAjs65ztFwMcUpPm9d3W2f0CEXGMQLwAgycaEjOitqo_-Qiwa7P4tXe2xrNoScLVOSQPYKFWJ86AqBQ_EDxtizAgusrrtznxSKzVgb8wqpI8d4NX0GW_72tm0koHlumjiOVJn4ScKDN0GlhmLBGnpNc-SmCGNVFG5XEQvpyrb4QS_5DaaMpH3ScMwmPYP53aXkpnOq93e8GfWtw0IdgbwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2c2yrYQ05g4aoV0Kosei0t_q--sp93HzlMJE8g7YOghI2geAvsywzozRMYXtIx-sEAdJW-8B26R_KCbahTv63SmjTL7_VZmnt9M_gKiTEhMYYzcX1qxLiMdN4vwOnJIFC1nsKKbw37kIlfQnorhgj-5DZoGYgEeGwom1YUfakyxrTtgGOhKP_VkT_iOpcLRiPGcdA0bnf_kI1s2EGhZK49PQk7yZ2JyIQ_JaUtif4022LOWVPyi4cevwQywFmpbWCExorMZKrEEu2kvHgElPznP0h6dGhIExMewLvy73ZiqxmHP-IaP_hsl0sjImFXpjRqkOd7tZN_iDgFaiyQc5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscLmmb2l7O0atTMjicCj3mZ1DmbQ_L5gQmSJfrvDkEncVVEmfzjTOafu1emeYFYWulZsuR6Vmk1eO075Ru36PU8-ma8grTYeioEqStsA4Rd5eZSCdTJjUMDGs5HydG0FjALbIIR0Yo9XCRVwXrPfvYfHIeas7Mmuua0BqSYEYEVa7K83OwXQWLIrgWOqLdYeAHFX9cahqTBTJcT7_6JVX9B8k8zlhmR4bftKH_hTKpVeRh9H4ZCYVLNTif4CNJLEe7JfVpdB12XZfZ0T4B_JbdlDPcTRwk5IKokTrCdhFMxFNMCUayIU838mxFdx3WR99kVJxIWCltB5dnB9hyKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=EBuss5ERUMDZvrA0fO90nku3qhpzVl-lQkxnSffnOaVrvyRYx-28C-CASUsr4lLPQRofJQIWEQB8Nb2czRFNA9uV9dVBkN1lYM8hTwBPkS9OBtH3uBWClihDKg8HL9kQWNZfEUfBrwPWirQx_UJUw6mMo5I4YHpxrBl47iCxUOwSqojqyEqb4gE1GGJSoQKbGLX3FXnbPuxQrdW22KRG7RNrH_pzQVg7RHCBcMjGrGMhE8JmQCTl7sNcPZVFDKZjmo8EHTv1SLp04PJZaJpV3tjgsS6AUCryG1MTq6J3M-yGMzWWezhfyzmZ1qiMM1735wlILjFrQ8Xv8IJYsfwhWbgi_AnO0hW5WrVWVWlMingSMYvg2z1fyQqJS4dYdPoq60DgsJNzMaXrUoRbEypDpMxr4rpgsFDQtw3Pa5SHH7I9Twx3ppBcCtKkwu_JLMFEsxp_t7w1aeXqraMIHrvBai7ux2SbjMLGwrYr8maZONlACtSJx4HQ7G0OjXCjl2wvjPDiJySI8mbTySXd7mbLnGFnpJ6-enj3fHmj7HN3BgNQyRqCyjW5Eu4ezqgfcldXnvsoIsI8aR4CbrXI63YfQGSLaHLwCEy3SP2SNDkuGTru6Jz-hOcHGznwRwjjb4D28IEx_as25S_4ukWI-FcStfQDAU3qjvkk8aHUS76Id64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=EBuss5ERUMDZvrA0fO90nku3qhpzVl-lQkxnSffnOaVrvyRYx-28C-CASUsr4lLPQRofJQIWEQB8Nb2czRFNA9uV9dVBkN1lYM8hTwBPkS9OBtH3uBWClihDKg8HL9kQWNZfEUfBrwPWirQx_UJUw6mMo5I4YHpxrBl47iCxUOwSqojqyEqb4gE1GGJSoQKbGLX3FXnbPuxQrdW22KRG7RNrH_pzQVg7RHCBcMjGrGMhE8JmQCTl7sNcPZVFDKZjmo8EHTv1SLp04PJZaJpV3tjgsS6AUCryG1MTq6J3M-yGMzWWezhfyzmZ1qiMM1735wlILjFrQ8Xv8IJYsfwhWbgi_AnO0hW5WrVWVWlMingSMYvg2z1fyQqJS4dYdPoq60DgsJNzMaXrUoRbEypDpMxr4rpgsFDQtw3Pa5SHH7I9Twx3ppBcCtKkwu_JLMFEsxp_t7w1aeXqraMIHrvBai7ux2SbjMLGwrYr8maZONlACtSJx4HQ7G0OjXCjl2wvjPDiJySI8mbTySXd7mbLnGFnpJ6-enj3fHmj7HN3BgNQyRqCyjW5Eu4ezqgfcldXnvsoIsI8aR4CbrXI63YfQGSLaHLwCEy3SP2SNDkuGTru6Jz-hOcHGznwRwjjb4D28IEx_as25S_4ukWI-FcStfQDAU3qjvkk8aHUS76Id64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=edHIFZQSOLWYfOTkt4QbqS8nIq0LLhpwxCRvCrRLJljOk9GKkKG-gnOZcdiIaIEkKoYY7UW-wZpk_gxNCUoePfP9dEGEbeft3kLH2YntmEO3lAfU932jeZNFephYlajypLrtwoXE7UrXjjSDTV81zlqYWFR91rrQkhueipcnBCcZGc2_y3yhSYGbC6Y81wD6xLN9PPzDo7BRZvoq0wW4dx4D_9KnpTeXSvFazpy5TLSX-AwyaCHnW59ZoGqrTDOVuT2BfR4ovN7of3cq8GImfSOa_ucQE5QR0KGlqm0rdVlJqytnTuFZBD_LQXIe-cKxNfA_oq4zCig4M71JxImZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=edHIFZQSOLWYfOTkt4QbqS8nIq0LLhpwxCRvCrRLJljOk9GKkKG-gnOZcdiIaIEkKoYY7UW-wZpk_gxNCUoePfP9dEGEbeft3kLH2YntmEO3lAfU932jeZNFephYlajypLrtwoXE7UrXjjSDTV81zlqYWFR91rrQkhueipcnBCcZGc2_y3yhSYGbC6Y81wD6xLN9PPzDo7BRZvoq0wW4dx4D_9KnpTeXSvFazpy5TLSX-AwyaCHnW59ZoGqrTDOVuT2BfR4ovN7of3cq8GImfSOa_ucQE5QR0KGlqm0rdVlJqytnTuFZBD_LQXIe-cKxNfA_oq4zCig4M71JxImZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=i6njTgPGuwV5uOK1MmXS4NssecdeToeZuT2R2AYPG0S67h67pJOhr43k8or7McljL01qVkyc2yHkY80SMoyNng_wSCArYtrjSKAmZuGvlB_SnQRj0yuIRZimH1nle19ok_vaJn5Hu7WsaNooU4IUNS_HHCSoytqRZo9y1FFZAiA1M3vNjfrN5mS-Dj0xqIvR2DHnIDwfgOtWfhBLygI57SLCleDS-vaZqnTS3VmyuWjulPh7YEKJnJ54PX1HBrIz06WSUEkbdS7e0Tu1puQ9ugUEKetXrUz16rtNfmoC42WbiQyTyc6cDCDWfU0csr6e8RgFViP6iGUfRUmcUrEx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=i6njTgPGuwV5uOK1MmXS4NssecdeToeZuT2R2AYPG0S67h67pJOhr43k8or7McljL01qVkyc2yHkY80SMoyNng_wSCArYtrjSKAmZuGvlB_SnQRj0yuIRZimH1nle19ok_vaJn5Hu7WsaNooU4IUNS_HHCSoytqRZo9y1FFZAiA1M3vNjfrN5mS-Dj0xqIvR2DHnIDwfgOtWfhBLygI57SLCleDS-vaZqnTS3VmyuWjulPh7YEKJnJ54PX1HBrIz06WSUEkbdS7e0Tu1puQ9ugUEKetXrUz16rtNfmoC42WbiQyTyc6cDCDWfU0csr6e8RgFViP6iGUfRUmcUrEx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=kdyhlIE0pnIc3-EhMRz3W6fO1FW7OIb1FxfBKWoo9ctTVksCISPtt1mYZbhts6Ngu786W8wGO09vGC4H_rh1n7pUI6a_qIQO6ImTovf0p9NpkuSBOsG12IGx4iS7HitEv1bhdc61CN761r8onAzZ67hPbtg-SAqZKlAzyM7woHwqF0kl1oh4TMqR-MaG-X6cNFluis0P0ywt4exnKVB6WY8Q1ct_WrINyLRUTQv-ZyVVmNyfhqbsENMrmV8Qi_PR2BvUNM15Ac46UJpmk9CApWuqDOYuGis5mIDggUzKr1tCkADP4aQaaQuCofc5CLVmOgPYT3bucUCueIyREGi0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=kdyhlIE0pnIc3-EhMRz3W6fO1FW7OIb1FxfBKWoo9ctTVksCISPtt1mYZbhts6Ngu786W8wGO09vGC4H_rh1n7pUI6a_qIQO6ImTovf0p9NpkuSBOsG12IGx4iS7HitEv1bhdc61CN761r8onAzZ67hPbtg-SAqZKlAzyM7woHwqF0kl1oh4TMqR-MaG-X6cNFluis0P0ywt4exnKVB6WY8Q1ct_WrINyLRUTQv-ZyVVmNyfhqbsENMrmV8Qi_PR2BvUNM15Ac46UJpmk9CApWuqDOYuGis5mIDggUzKr1tCkADP4aQaaQuCofc5CLVmOgPYT3bucUCueIyREGi0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOy_R3Cnj8iqsebVTe7dHTqJDDRZsxzsTkB_6JBUsUJIf1_XiGi7WnyYcgd46jwPDwjjBo3Y6SntIBXTX5I-OJeSIG4zJ_AqiAdR7vr4sWpE9vadiFDxXbz17bEL4a4t4VQoq5_N_r0eiG0oHjrQ17ZKSg1LaXdONDRKuKYwlB1TSTsq9cpIXeSCJOnWGOYk3UhPXUzgZmu34FfB9yVJFAvAwQg3Vk6eGqEy-4KvOzGo2iGjYdbsDZvn1avkoGrOe7TsVtjPi67dpKHhWkOhLWA5LsAwxFzYE_4HUfcmfwYdZr9tpoQ-ToXUmw1Uadquuryb27CA-dsnpZTJCLSRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OggyxV9Bvzl4tMRCcbiWRfpE-xmG_oCALcteHIJJKwmQt-qyEAx3j2m21yVKitxVHbmzW8ZdNlWG3hhTc-oYRBJs8NPc7VGLOS2sW4uS-vXsmXa1gwoXQGQ03NcGrDv9iPo1-B8ec1607zVPmTeOnenI7JkMGCpZ9vEib6Ro3ndjvAJnMgJbP0BKJACPZ5I5nxRVIOUTIs5fmIRChYMmwFboW5dXD8nNm5HyGW560cia8XVcwz5S8uzLSXPvv7lUV-zXjSSK9FNehHJeL4Y6e6YPKUHYClZK7qno94tEMIMEEkC0xUYKx_yMepbeSjKjFSqAdui7eaSGMIUpvB3Snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=fmlhSWyaQSkzqmk7Qb6cOqcvae_NN0VwrhUERrGlYR4cZpZxHBNy0nP_YzEYtrhksMvMEoC2FNB4E0Au24WmSI_R-C5_snENp6yQ_OVQpCHRd7zXa1oTUI9c3YM4oP_V6cNCn0AnyEXe0zmHqYTVruQmLO64J8RZ7WtugzPHHaPEVETYS7fgk6kIf1bttQ0-2wXYWxhqRspKongQ54laOf-ixP_Zfga-Xp_esrdbQg7Lw4H6NmS4e15HBgDxPYQuL14-7PqDezUAj9k3w5Pewnji09yWvad6GN3BHVeeAwq-tld7ZIORH-z69mzI7ZvPNRQ-vVJvczhUzkr_wBN4LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=fmlhSWyaQSkzqmk7Qb6cOqcvae_NN0VwrhUERrGlYR4cZpZxHBNy0nP_YzEYtrhksMvMEoC2FNB4E0Au24WmSI_R-C5_snENp6yQ_OVQpCHRd7zXa1oTUI9c3YM4oP_V6cNCn0AnyEXe0zmHqYTVruQmLO64J8RZ7WtugzPHHaPEVETYS7fgk6kIf1bttQ0-2wXYWxhqRspKongQ54laOf-ixP_Zfga-Xp_esrdbQg7Lw4H6NmS4e15HBgDxPYQuL14-7PqDezUAj9k3w5Pewnji09yWvad6GN3BHVeeAwq-tld7ZIORH-z69mzI7ZvPNRQ-vVJvczhUzkr_wBN4LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=kv8g9Xj_AvXPSwSgEmpfhuvChAzNTMWCGj6lyjtOhHzo6bidoE7TDCjROkvkYBomFVr9nqRMrwIg4fTlTAJrIVg7bEj0wS9w60KFIK0tyrNo38Rv-2ceN3Zx-fcWzOWuCnyCNrKZuKUNpQNP-3g6FP3Ukko1iGHdaXonFSGiw4FJTaVoWMdgI0jdGPHytgwXPmGxFfw4pMzDpF2op96yNEi_iOPCqlHh-ocQrBXgfewI-2D2UGg_BaJ0ztq5kqIDHCM7yT5RINWTtAJiNAUsZQ6bZj-PFNlMwlW8wJB4fjvLH9NAeo-6r177-cQLU8tk2dToXmtEfr3NGO9k4-sYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=kv8g9Xj_AvXPSwSgEmpfhuvChAzNTMWCGj6lyjtOhHzo6bidoE7TDCjROkvkYBomFVr9nqRMrwIg4fTlTAJrIVg7bEj0wS9w60KFIK0tyrNo38Rv-2ceN3Zx-fcWzOWuCnyCNrKZuKUNpQNP-3g6FP3Ukko1iGHdaXonFSGiw4FJTaVoWMdgI0jdGPHytgwXPmGxFfw4pMzDpF2op96yNEi_iOPCqlHh-ocQrBXgfewI-2D2UGg_BaJ0ztq5kqIDHCM7yT5RINWTtAJiNAUsZQ6bZj-PFNlMwlW8wJB4fjvLH9NAeo-6r177-cQLU8tk2dToXmtEfr3NGO9k4-sYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LASmtPS7qBeqjNJ1n_yZ_-cza1-tuMLORnnib-E_JAKty0ztMLln3Q6T2fOEHV-gVVqGRmQ38CKPpuk1E6VJKP2DMAnPi231XHZWW9F8gt3pk4QVYRtJs33GLpGtGVTFsBMK7ajwmtq99x0pky0DqJNOdfdDHYly0W34AYiGNqABP-9IVJiFLTImCz1T9APAjIaBDTCV2w4dZS-9Oa3mAGq-f7ZDcKw3dPbX-_sc0CZ334V8kNKZp58AHkhMkcOmaRl4clrRMInDWgp5U8gOWm2s4HR46WVVmuRFg31YLBn3DJmjCK2aSKHHHXTtGK04ShqO1j9viffbkFcrV-Ehxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=YlnTNVTCViDxiWhsbd_EISIWSc4ljLW4DgNPsQA1GmhX2h-B9i3G5kpNEU3JCR9DbRCdirLmKNz6yGO4b_i1TbC6QZtjy3GcgulNtfeUb1gvO6wecGYpZ4-Fz6ezBBLye9G2ofvxej5vkKDD5U296ZXkZ1uKnjc9op_2eV8gG_upgqk0IhAglSbCfvRO4CTmRSJy39WNUIVpdDQ4u5m7sHZ7LqipoJfQEmDbwz-gB2mKSCsFU5e5AM60mKDZUKPuLgmvVlcPlfUiux1IXPzFues_OZnm_KrH-06pTPA1r_lAUTbOAfbb5pEGIMRzMJesujWWmFItJ6GwiiXedmk_8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=YlnTNVTCViDxiWhsbd_EISIWSc4ljLW4DgNPsQA1GmhX2h-B9i3G5kpNEU3JCR9DbRCdirLmKNz6yGO4b_i1TbC6QZtjy3GcgulNtfeUb1gvO6wecGYpZ4-Fz6ezBBLye9G2ofvxej5vkKDD5U296ZXkZ1uKnjc9op_2eV8gG_upgqk0IhAglSbCfvRO4CTmRSJy39WNUIVpdDQ4u5m7sHZ7LqipoJfQEmDbwz-gB2mKSCsFU5e5AM60mKDZUKPuLgmvVlcPlfUiux1IXPzFues_OZnm_KrH-06pTPA1r_lAUTbOAfbb5pEGIMRzMJesujWWmFItJ6GwiiXedmk_8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=tZLBpBrk45GQjlqhSTdKReGx9a_Wiu5xZSFjcDuYq9m_691ZqOZaLF3P_qe09e9-7Pu9oXsHO1DKbrRxUTDlm_fEvm9HHpsDBqVRMlmsNVjtb7D9exCFL6KWqlD8F8N_FTHSjmJi9GmJymeAoKO6DCtfFDEdgb_lI5StNyq4p85aU_H3myqAb7tAWm9DIVehwXM0EaKbzhtV9LpcF1EjTEH3x9HYGUNULj1XMIG9tsa0RE2IIjCo_SXNMlxsiaeLBHpLF31BneW3xlrCnn1yZnepi-nrQsbYaBY79pbK9jYTJSMjY79axVxgd4ZIC7tMbxU3JpLGB6yKiZPvUuTuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=tZLBpBrk45GQjlqhSTdKReGx9a_Wiu5xZSFjcDuYq9m_691ZqOZaLF3P_qe09e9-7Pu9oXsHO1DKbrRxUTDlm_fEvm9HHpsDBqVRMlmsNVjtb7D9exCFL6KWqlD8F8N_FTHSjmJi9GmJymeAoKO6DCtfFDEdgb_lI5StNyq4p85aU_H3myqAb7tAWm9DIVehwXM0EaKbzhtV9LpcF1EjTEH3x9HYGUNULj1XMIG9tsa0RE2IIjCo_SXNMlxsiaeLBHpLF31BneW3xlrCnn1yZnepi-nrQsbYaBY79pbK9jYTJSMjY79axVxgd4ZIC7tMbxU3JpLGB6yKiZPvUuTuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSoGhcjZt7AXW99wjSrvStG0zIypeMZYvK3fNVSrd8rgVbDBdBl41qh7L41ox_-TL4DQbHP7Qhp1asROkqj-5QyMyun55mjgRE5_OZ6xzsotV677TAMrqrnRrnrmIpgOibBnb9AIJeVw-N7DegTV0sjGoicflF_Fhfgsju104841rSbyBnajhnPldYM4b0xas_GbfvSg_dGdB-IU8TcU2PDVkZx1SIuUWdIGe7a7SVB8_Kw9k5cQk7plC6_fEcX7WY3V9HuLmImfweF_i4Y3GqploGpN4LH5Oyxl964OaP18Vj1fnrZpJxdR88uEQUCHg89SPDuf_U4VNxJWB2JSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=pexzhVOm7DHt0ph9Eq936GmwzGMfpAt38Pctfcqd1MKEwexULLs67Q6YCzmO2vPNCinsb7t5sCT3W1DSF5_klvCA2EEpkZaR7TrftdpuqwraG7PURESVuOoSnRs61xvTEpNawpnv-X-5QPKIh-r3TBhkGLHWB2ByOFrvQO360AK9ug4WtcLh6TYa8YMv8ScIcRPl-krULj7DxmfBDLhMkFrYZsjATNq6Xn8na7w7li2uitmLnPBAi-S7VppiNfvXN4wZnML8p3mqLHuUjpwYRpRATzWwY-Omoja0JIaEn1JRVB1cFxSzs7Qp1MZ-eJp_GuRd3-rmGdftv-JgbHE9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=pexzhVOm7DHt0ph9Eq936GmwzGMfpAt38Pctfcqd1MKEwexULLs67Q6YCzmO2vPNCinsb7t5sCT3W1DSF5_klvCA2EEpkZaR7TrftdpuqwraG7PURESVuOoSnRs61xvTEpNawpnv-X-5QPKIh-r3TBhkGLHWB2ByOFrvQO360AK9ug4WtcLh6TYa8YMv8ScIcRPl-krULj7DxmfBDLhMkFrYZsjATNq6Xn8na7w7li2uitmLnPBAi-S7VppiNfvXN4wZnML8p3mqLHuUjpwYRpRATzWwY-Omoja0JIaEn1JRVB1cFxSzs7Qp1MZ-eJp_GuRd3-rmGdftv-JgbHE9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=a9qvh1UlCXmQ3NeVodcz12a-HBjie7JsqG7kD-dtcWrqnPaBx-fqdJH7DAhtaS4e7y1rzaj7Uvaw2TXWubpVAsnaJYYPPC3b29ruNi5EGHPtlmJFf0Gp3pBIzjoyElgjralmHMvPFwrSChlbGIUiPX5V7bCh38RMBvKGP47DaOBKFC-wFWkM9661qEfEPwt_0BI-Vj8B5QlUCKw2rNtE4t-2pmYk5GkjdZmd0tcbNF2U2GKRNS6piJZCcHsPGuhmkABVQZ7fHmhUyd29RXp8RJTNQjm8k8cJ0TgRLOxykTReWvvf75g5vgDeON33gU39LJGqGS-TiEpBLMwRmp-MYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=a9qvh1UlCXmQ3NeVodcz12a-HBjie7JsqG7kD-dtcWrqnPaBx-fqdJH7DAhtaS4e7y1rzaj7Uvaw2TXWubpVAsnaJYYPPC3b29ruNi5EGHPtlmJFf0Gp3pBIzjoyElgjralmHMvPFwrSChlbGIUiPX5V7bCh38RMBvKGP47DaOBKFC-wFWkM9661qEfEPwt_0BI-Vj8B5QlUCKw2rNtE4t-2pmYk5GkjdZmd0tcbNF2U2GKRNS6piJZCcHsPGuhmkABVQZ7fHmhUyd29RXp8RJTNQjm8k8cJ0TgRLOxykTReWvvf75g5vgDeON33gU39LJGqGS-TiEpBLMwRmp-MYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=cZFgmS8p0DOvnBW3wY_k9B-arNEOy_Nf6-wNbG_bXofuM4UohiKGjBxboUPVG2bQXKEfwR433v5U7nyh9gv7FhrQm-9B_ugFUvFyHxutJAfzXYNnypLSW5ASP1JkA2yyI5Ljdx1WHvTBb9matSOrFI4mO0NFNPXp76w75JUttDV2DSWb8RCBbOWf_j7xwNP6HrU8JGRhl2GFgZjjMUVQ00wyZOCUfK_-v4UX1sP07c1ep30zZBqOp0IDOO8J6vc6y1RmHb2sg8fhNGG1ZbaAQ_LzEJwSGY2bKsIxjT2dYJi36qtOHmLgCf_A8pf2nIH-AUlfzj7wwXD0eyKQGW9pSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=cZFgmS8p0DOvnBW3wY_k9B-arNEOy_Nf6-wNbG_bXofuM4UohiKGjBxboUPVG2bQXKEfwR433v5U7nyh9gv7FhrQm-9B_ugFUvFyHxutJAfzXYNnypLSW5ASP1JkA2yyI5Ljdx1WHvTBb9matSOrFI4mO0NFNPXp76w75JUttDV2DSWb8RCBbOWf_j7xwNP6HrU8JGRhl2GFgZjjMUVQ00wyZOCUfK_-v4UX1sP07c1ep30zZBqOp0IDOO8J6vc6y1RmHb2sg8fhNGG1ZbaAQ_LzEJwSGY2bKsIxjT2dYJi36qtOHmLgCf_A8pf2nIH-AUlfzj7wwXD0eyKQGW9pSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=N0neA1irmv_lDTF1ym-4WBnq6By_Ly3M75nM04ds9eD3CRkFkccfpMPy8Gvp4MNIFFOVS40yUhf69GN3cOB4Q8IHQA3ZxoEpnf4T-T-UdoVwUwHQdp0rX995TbcL_3rdf24qTlOInHC3w9u58s19MIVXajXYmUNGqsafceiciMkPeZitFDmREKD4FSRfDHF-z5-gxNjVKVjNoYQlqsUnPpBAK2UsOXz3yEyRJoRIZbVXWgUZ4nFOzxsZidC8jvHxCNH-qAryNkRW9Ba4ibqepEhLwTObtGhqGctpGgfZ_Q_SkddTjJhZ6UwR1FfJc0WY8WkSl3i7KgOsq0fLmaKvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=N0neA1irmv_lDTF1ym-4WBnq6By_Ly3M75nM04ds9eD3CRkFkccfpMPy8Gvp4MNIFFOVS40yUhf69GN3cOB4Q8IHQA3ZxoEpnf4T-T-UdoVwUwHQdp0rX995TbcL_3rdf24qTlOInHC3w9u58s19MIVXajXYmUNGqsafceiciMkPeZitFDmREKD4FSRfDHF-z5-gxNjVKVjNoYQlqsUnPpBAK2UsOXz3yEyRJoRIZbVXWgUZ4nFOzxsZidC8jvHxCNH-qAryNkRW9Ba4ibqepEhLwTObtGhqGctpGgfZ_Q_SkddTjJhZ6UwR1FfJc0WY8WkSl3i7KgOsq0fLmaKvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ihCl9cYoV6m4T7P2ZeTs3r4xi1Og1lEGfXIUe1AJtchzBNx5yqgYY7LVVzSqIotdpevLN9ix13jP2fpslVWTt9jfUbHwmm3MNSzIfyG_0uahBxmW7P6sPvW3yUgrTTh_iOsM1k_LxeSttSpbpJn41dX5izkz8C34RvgRSNZvergZgJCvrWiU8R68w1LVOa-g3lC-RGMWmsWjCOSw1cNwjaPNPwOss6xFUVlAIOyxklYbIHnN2ze1_a1cyq6Chh9szh3nw2bWQGDuLwNpgygm1aga3EKjMqLQwFbuWw3kmMxtNJv7ljIL1ee0IPGUr0P3Pel1MbX79RCQVPUeVZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=dByYhy2sfFbvj-qBSX8Aej2WgO5GSLck7ssWjbYBsNHnNol3zZPXzSpAg3vtqGnS-WqyIh8wBSZ43KdaUrAYclSqwEVCdeBZO0yxcPPkLm3TdxYSsWOgdDANi3Gbi828JqxQjEaF2YJoQFtVFstlF4fhtnKmO2-VLPvgP824iqXOFpEjj-SMmocekt_15OpyPLbdTeQFMhcy7eLbDjGF9tmTjr-Crnmceg6CkHcXSxeN_8RuBg1EgI7UbZ9BfoRoNUVHYU_1XaPvTaeYo1hj-hF5tz9oOt8EHl4657cONfLeYfStDAno3H_JN9T_rhURNAz3DVCf806W4lH-udQxaGTwAD1dVHV9jWcO6COiSAtF9f0jDd4-K0Q-V2uCC9ydYXpCFlLgMxYCW1Iz846pLshB7M1U-kf9__sJidAsIbRGBCZTq_RPlJQRveB4vj_bmtFM_eJUqqaR9b8xdVB6shdZbaYt8uJGy6zxqsKDwsFuSBW00SKG6WfCwWjyC7L12xq8tdMfL7yX9XoRM_Jk7UxRpPMeyHrM-FDntq8Umlapr4sNu8N-N9ryKWMDjdTSBz-dK99mnMLwyt6hx9CIDYkPPqjxcROBv6xhR2oQ9BXbDXnmn-h_FtRSGCEdv83bBkZolZSP14CTTiTQoFwtikVLkZLcw8OChLf6zIRHKDs" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=dByYhy2sfFbvj-qBSX8Aej2WgO5GSLck7ssWjbYBsNHnNol3zZPXzSpAg3vtqGnS-WqyIh8wBSZ43KdaUrAYclSqwEVCdeBZO0yxcPPkLm3TdxYSsWOgdDANi3Gbi828JqxQjEaF2YJoQFtVFstlF4fhtnKmO2-VLPvgP824iqXOFpEjj-SMmocekt_15OpyPLbdTeQFMhcy7eLbDjGF9tmTjr-Crnmceg6CkHcXSxeN_8RuBg1EgI7UbZ9BfoRoNUVHYU_1XaPvTaeYo1hj-hF5tz9oOt8EHl4657cONfLeYfStDAno3H_JN9T_rhURNAz3DVCf806W4lH-udQxaGTwAD1dVHV9jWcO6COiSAtF9f0jDd4-K0Q-V2uCC9ydYXpCFlLgMxYCW1Iz846pLshB7M1U-kf9__sJidAsIbRGBCZTq_RPlJQRveB4vj_bmtFM_eJUqqaR9b8xdVB6shdZbaYt8uJGy6zxqsKDwsFuSBW00SKG6WfCwWjyC7L12xq8tdMfL7yX9XoRM_Jk7UxRpPMeyHrM-FDntq8Umlapr4sNu8N-N9ryKWMDjdTSBz-dK99mnMLwyt6hx9CIDYkPPqjxcROBv6xhR2oQ9BXbDXnmn-h_FtRSGCEdv83bBkZolZSP14CTTiTQoFwtikVLkZLcw8OChLf6zIRHKDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=b8cnQQHT2_8pB5nwwitu_UODth5I6grS1bZbV4W8HWMvCipJlifeaxXGyATEmlcExtSlD7bAYVIrucrJVz-yr3JhnAEB-ElrennYqyKPkJe223Y8CWePO1YsDsiFP7_gDWe77tj71ldm72Um59C38AH_FqGHsKLCsni5dhFH5GX3Do09ln6RqHB64AtITYtoqxDZwBLZVjMx3q97EADWypTAKtL9bzLUq50-1BIsCEO7z4WBXSqEb6U1zIPVbeRO1Sv1Zblt3EALGQxy5ojXFdKHPRI_70ZcNiBaoS7MVUr2konJPad4U5oN2EwnfkC2_CxKqNg1b97k5SJiklLiAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=b8cnQQHT2_8pB5nwwitu_UODth5I6grS1bZbV4W8HWMvCipJlifeaxXGyATEmlcExtSlD7bAYVIrucrJVz-yr3JhnAEB-ElrennYqyKPkJe223Y8CWePO1YsDsiFP7_gDWe77tj71ldm72Um59C38AH_FqGHsKLCsni5dhFH5GX3Do09ln6RqHB64AtITYtoqxDZwBLZVjMx3q97EADWypTAKtL9bzLUq50-1BIsCEO7z4WBXSqEb6U1zIPVbeRO1Sv1Zblt3EALGQxy5ojXFdKHPRI_70ZcNiBaoS7MVUr2konJPad4U5oN2EwnfkC2_CxKqNg1b97k5SJiklLiAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=RUiCZTrXaiByf8rxcNYwqWbkNEqDjf3jEzC3a05stWNcjkj5FkCJxkE_kQkCvVf3NgysrFJrRXOy4GYYgfV93kWovVwrnaJHYqnU1chEgYq-xOURU_Vb3sPBlChCgKsc-yNezgiTNmlGPXRU_BRQDqK_088PHJXE1tpBEdao4q2u_sn0KsG1H3BOHwsLM0IZAQX_xjXgsnAsEahgiluyY63g2WfCItlnmaJP8DJk8vCQ3DUt3dlEpDEJmUabOdSZmgzkFkpZfjM_NIHf5LWzio6f6aREvTq1O3Zfy58DO0k0Hj9CTeZLqYj5LmjVEQXzRb8VZIvv2j1jb_cZSYczxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=RUiCZTrXaiByf8rxcNYwqWbkNEqDjf3jEzC3a05stWNcjkj5FkCJxkE_kQkCvVf3NgysrFJrRXOy4GYYgfV93kWovVwrnaJHYqnU1chEgYq-xOURU_Vb3sPBlChCgKsc-yNezgiTNmlGPXRU_BRQDqK_088PHJXE1tpBEdao4q2u_sn0KsG1H3BOHwsLM0IZAQX_xjXgsnAsEahgiluyY63g2WfCItlnmaJP8DJk8vCQ3DUt3dlEpDEJmUabOdSZmgzkFkpZfjM_NIHf5LWzio6f6aREvTq1O3Zfy58DO0k0Hj9CTeZLqYj5LmjVEQXzRb8VZIvv2j1jb_cZSYczxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=DQfz5fRT4_3PnaJ49BlPvl-gWNE3jx1wqStZGjyGep7L2TWgqujDzNcBRo-ZGyIAOvJ5iThfXAl2OnhTv4gpjzve6_fGbBXxZoj-J4KpeM-8WllgUF3MVRap5Z6ErsqLpegx_kGMQhuo4ybEpjnQAsJJREue1Ge6TnJXyKOdMlTTfuQaEP_iEoaOZ7fv5Ulm4CFNosT_H3z7vhCmXdEjBcPfXqOFUHesYfyzrXv2Erk1CcoSnM0yv8ovKyJ6884AyetbfKxq_IEDEquYno6fnxI9jSnb2Iyt2Vdm6JERFV_Bo-hm0vXPnkptwoXmOuY8MKQoSW7NpT19RVHw2l_Uig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=DQfz5fRT4_3PnaJ49BlPvl-gWNE3jx1wqStZGjyGep7L2TWgqujDzNcBRo-ZGyIAOvJ5iThfXAl2OnhTv4gpjzve6_fGbBXxZoj-J4KpeM-8WllgUF3MVRap5Z6ErsqLpegx_kGMQhuo4ybEpjnQAsJJREue1Ge6TnJXyKOdMlTTfuQaEP_iEoaOZ7fv5Ulm4CFNosT_H3z7vhCmXdEjBcPfXqOFUHesYfyzrXv2Erk1CcoSnM0yv8ovKyJ6884AyetbfKxq_IEDEquYno6fnxI9jSnb2Iyt2Vdm6JERFV_Bo-hm0vXPnkptwoXmOuY8MKQoSW7NpT19RVHw2l_Uig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=JNIR5b97RFr7hUQZrc2LLxlU_mcykiUk35FKPlv6CB1yuDcQJ3eWAt8qRYDXKEcS4acTpK8nEQpo9E7YAxWkE76fK3DKTr1E3RF0-n1qbaYbGWx9Y2WlH5F6jxXmCIh5dbPje-4IdKYI48SIgHsJx0dfgH7yczAxMfIeMk86nGPWrPlXt4C2YfB0LvOnl7CB2y6DgIj0yzCCvvHxGauhGubeyhqiUOTS-YTWEft_bLRSULwp8bN1-zX4ez07yo2tBOXZPcYIlXMBGDKTpWRwiE8wZgyKf4ODtwDLJXz1U-L7_KOIMc8p3H7pqOMGLSvVq6KwfWyOG8fUcI6u1pEk3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=JNIR5b97RFr7hUQZrc2LLxlU_mcykiUk35FKPlv6CB1yuDcQJ3eWAt8qRYDXKEcS4acTpK8nEQpo9E7YAxWkE76fK3DKTr1E3RF0-n1qbaYbGWx9Y2WlH5F6jxXmCIh5dbPje-4IdKYI48SIgHsJx0dfgH7yczAxMfIeMk86nGPWrPlXt4C2YfB0LvOnl7CB2y6DgIj0yzCCvvHxGauhGubeyhqiUOTS-YTWEft_bLRSULwp8bN1-zX4ez07yo2tBOXZPcYIlXMBGDKTpWRwiE8wZgyKf4ODtwDLJXz1U-L7_KOIMc8p3H7pqOMGLSvVq6KwfWyOG8fUcI6u1pEk3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=LUTEEzKu7Gjh-HOSQTtAF2ETaRFo1s9WOc9g10qO836s9lZRsNxvG8XWS_UdiXP5tGoaDlvJ3xqm8qDcU-YxbHaH6T5_Whr_lUPzcYyDWKhJGgKcbsQcPStVDzDmV4oxeDJsKiUuYCzWDh8LpWR9xnTlt_jjljF01Y96aRcNjxFK2UU7-TJgUvaqEXEMpU8mHJdAKod5KxqGmHmJnNdx2DbjneIULHjQ4mtX8mevGszZjBaVOkCLjSUsWtiqpBZ2MflI0MtKJGdB2AuwZ2XMPOJQb6eCxygEPFaZ6JIZ-LyzKC6M45Va67SgfB1Orwvcjy6KQUk2cmnZmxg0HCMsMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=LUTEEzKu7Gjh-HOSQTtAF2ETaRFo1s9WOc9g10qO836s9lZRsNxvG8XWS_UdiXP5tGoaDlvJ3xqm8qDcU-YxbHaH6T5_Whr_lUPzcYyDWKhJGgKcbsQcPStVDzDmV4oxeDJsKiUuYCzWDh8LpWR9xnTlt_jjljF01Y96aRcNjxFK2UU7-TJgUvaqEXEMpU8mHJdAKod5KxqGmHmJnNdx2DbjneIULHjQ4mtX8mevGszZjBaVOkCLjSUsWtiqpBZ2MflI0MtKJGdB2AuwZ2XMPOJQb6eCxygEPFaZ6JIZ-LyzKC6M45Va67SgfB1Orwvcjy6KQUk2cmnZmxg0HCMsMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMQiJPvJn3SYHpqfszeb9aR53QS1RGP2uyggGjgw_iJe0hK8-gVL9YPHc8vZe2WJE45ZGvfsJWRthebIBTgq_767wiQgdft240EnJXfoz1n6Z4HlLT11CuEvJonP1u5eTa-5qWj9k3JfBMaccGydJc2jt_KfIK_8LQpZc3gkSQYLsOGIAE5vJlrWvJY70i3tHf4b2J-8QxWmMUMltxK6yg86aDpP1fQaklUtheLhs7tZ8IBsouMBgY2xFB5kxfgolEBJTu60apUxNutXGAqrU40G5_o5FpJ2xJizfv40lP1lqYlu79t4vlrkxWbmovcWbsxTadMpJewO9U83lKc5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=AY1dpotIq4H-eyIxlmuZTgvu1AXVJcC-iBzX7VMXcsFTUug2_qjWLlVPbmVCLjqrWDKoSx5WY3jP8W8Zpv8ik8Ckize8EPhkTy6yu2nwJ2o99fwN4YIsEwNfqyyq-mGe2xkUqQ52QwDvvRRgq281nU5ml6Mgr0njC-Y7JpX1GSsnLvHYBLHhCfqCMBXwHdHl5GX7OEooj1cc32Gotu5FIJba_CLBzYPou9Eix4rvwt1D0MaySAxA4N9-sKW7ekeNLvPu2FCNmRAYSyVmfaplGggsYFNdcdzoXiprpqZGPsAzrtV6uzZE41I88TbWiZXv-ZUqC_Q9Vga7M--ye5Ke-0MHyk_7gGCYqRxFDGUz7NM_D_-aDo2Sw7VWrb6N8Om_DTlGuUOHHsTxNg6ktSkZDdmgq3zKoAdrWkJqu1GTPc2A7R2_Ney9NEEKTxF8h1pPkCSJFRyB1AWiFkR1kFu2tZ3spaRfXCvWqhgKRZcywTZTFpn_NaouFZfWSmjdn2B6k2QWWemE4LWhuihrcI3MVMbN9AI5g_2Nv_naDkLes75Z_yDbsGaISn2kS3Vcz-lhvbJW0wQPMyvvhLYlDzNMIXex_zjGvcxouCNUomd1Ais0A4HCbqViqgF9NabXmh1cAYBuIUTkM-3b70j6naGZlNZS-Hd-CSqeIPd7Z1yfKh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=AY1dpotIq4H-eyIxlmuZTgvu1AXVJcC-iBzX7VMXcsFTUug2_qjWLlVPbmVCLjqrWDKoSx5WY3jP8W8Zpv8ik8Ckize8EPhkTy6yu2nwJ2o99fwN4YIsEwNfqyyq-mGe2xkUqQ52QwDvvRRgq281nU5ml6Mgr0njC-Y7JpX1GSsnLvHYBLHhCfqCMBXwHdHl5GX7OEooj1cc32Gotu5FIJba_CLBzYPou9Eix4rvwt1D0MaySAxA4N9-sKW7ekeNLvPu2FCNmRAYSyVmfaplGggsYFNdcdzoXiprpqZGPsAzrtV6uzZE41I88TbWiZXv-ZUqC_Q9Vga7M--ye5Ke-0MHyk_7gGCYqRxFDGUz7NM_D_-aDo2Sw7VWrb6N8Om_DTlGuUOHHsTxNg6ktSkZDdmgq3zKoAdrWkJqu1GTPc2A7R2_Ney9NEEKTxF8h1pPkCSJFRyB1AWiFkR1kFu2tZ3spaRfXCvWqhgKRZcywTZTFpn_NaouFZfWSmjdn2B6k2QWWemE4LWhuihrcI3MVMbN9AI5g_2Nv_naDkLes75Z_yDbsGaISn2kS3Vcz-lhvbJW0wQPMyvvhLYlDzNMIXex_zjGvcxouCNUomd1Ais0A4HCbqViqgF9NabXmh1cAYBuIUTkM-3b70j6naGZlNZS-Hd-CSqeIPd7Z1yfKh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVN2yc39Rf-0Nj2snK9GAYXWEXrL_otmGaoVElZTevUH0vTaRIRxLcMYW3Ug4JJrdJ3NEPkx5yhuxlEILvQ-oG2MI7tNRCCgITrNaJCRqOvsn0tr55mrt8W4b2gdqUQMH-DmTWKtZkNtvUxwLnuMPAl97JNlTI_Zw21G3I95WfoPpIYemIlf50ihOETainZfjj30DGYZmz8_5_HDWTz69wQwyjytsQnOsdP-8RARONaoxAE9MQ7-g_eWIn1YRza8vZBk6VMk1mDrXibqTxUKqH-KA5tqwYxCxfN_4PXI-3nCNXC0rH6wJIXy8BMqQvR9deH6r50c3RGXozuckdoZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V86S3wQybcu2YsQEXgVFu0F6u6lHgwmGEXBPb_vjBX8lGb_-3uO2KerIQsIgAvmJGCFaMP3LhZ0QrPF66ZyW8D3zB4bvwFGOenwEGgSSzjVaZRS02QULOsIZybn-fXD477XVYmc9JpZeZkvTCC1HJWhqzrx8hDbWKjqJSBkSoNbpQK5vr4l2PBvlmPW4cVcniOkKqyGV9-wASgA-l57GkJYiD1N4MXgNDOjEJl6V-EVz0KBZ_GBQhCT3Kh6VPFJqIFT9fzgaRBjeIRxrRCy95DGOk0_cHI0bNDwh5P5tEz45hS81TrJ5ySncr6Qj5tc5Au1tPky-5wofet4silV6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=TiQsUyowZEkLxKUdjPTDDPVY09HV6fdJ97zkF6LRIoNQNPs0nQSSm5yMdV7-b097gWr3qaDfON-y06VzPkVcl0JU6oG1ISWTTRN9kZqkp8ML_dIWPfHuprqS2LTHmJGNmC9f2zrU2LOEV6ML2xBGENhgNLYFFCg1e0hE_Xdimiz4uSjrZM-WOozNeIKT3_u6a7G1cEj0pFS5c03t_f5j8RNnZoq9jt5JFupQg5lCW5Cb8SJDDUaKAL9CV4YPi6irC34ZVsVlHzS55E5YSz5TJ5mZZ8x844S0zr9qcsBi3oI23AX7gIqoK0GKWLiC0OPlPTz4sdcEmN7upsdA9pk_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=TiQsUyowZEkLxKUdjPTDDPVY09HV6fdJ97zkF6LRIoNQNPs0nQSSm5yMdV7-b097gWr3qaDfON-y06VzPkVcl0JU6oG1ISWTTRN9kZqkp8ML_dIWPfHuprqS2LTHmJGNmC9f2zrU2LOEV6ML2xBGENhgNLYFFCg1e0hE_Xdimiz4uSjrZM-WOozNeIKT3_u6a7G1cEj0pFS5c03t_f5j8RNnZoq9jt5JFupQg5lCW5Cb8SJDDUaKAL9CV4YPi6irC34ZVsVlHzS55E5YSz5TJ5mZZ8x844S0zr9qcsBi3oI23AX7gIqoK0GKWLiC0OPlPTz4sdcEmN7upsdA9pk_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy7i569fUD_Z3J_GyJYjuQZk9fonCUNa3Szgv6vtcUfgrL7O8HRgDnYcC8k7b9vjm1QhbXL40OBahgncaF6Kun0Ocg8XLMhUFdNpxw4NCJo7bbKNWDhc3YF6gTX6qjRMNWzgnOa6gsHv9L4cC5L5T0xU45XHSB_mdKvxb1NZDo0486ywXpCVY9-DNGvhSvFDin2yb5PH8Pp95TI-zTT33UJv3x2mtfrtju6Y55cHKLJR7qsc-Ui8LRP5SdaUM67zuz613Bg-NMmZ4GVtt1jq2yAEcoyaR2NY4iWrmNYHakKL0RjbByQB48T6Lbiw4CJUFoeynWRGB3ARfPgKIqZ_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
