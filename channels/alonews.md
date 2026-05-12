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
<img src="https://cdn4.telesco.pe/file/BATi9_Ql3aQ63YXJHHWB6xA4cH7MBp2jfngAbVOhFvy_jcQiA6sWenrGzhd_mWdH_7xWL9hU6UeSGl2B2ElKyvwjat0GIv_QfyD8cLtf84lAKUV2ysyJYe5NTySd8Ta-zlj49itAxiiF2yOB9PuvpDBXRDfXcTnb0y1oSmv9hgFIyIv2vcDtclvy3Qz38y_3bvXd1YJJInefVWvhEWmZ3TYcRWseyWl0hTpli66p8YffDAaqXwmxBM5WvGfBTzGRaMbaCwzhSb8YdJIcV3LV1n5WJ6MhDxOxvbfp4bo-7P0I-_9JeZDxXMuUoiDnxwDqF9a--tJ9SsAFO8Ap5Y5nqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 14:59:35</div>
<hr>

<div class="tg-post" id="msg-119476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت دفاع کویت از دستگیری چهار نفری خبر داد که تلاش کردند با یک قایق ماهیگیری اجاره‌ای وارد کویت شوند.
🔴
وزارت کشور بعداً اعلام کرد مظنونان اعتراف کردند که به دستور سپاه پاسداران انقلاب اسلامی برای نفوذ به جزیره بوبیان و انجام عملیات خرابکارانه هدایت شده‌اند.
🔴
مقامات گفتند این گروه پس از فرود در جزیره با نیروهای امنیتی کویت درگیر شدند که در نتیجه یک نفر از آنها مجروح و دو نفر دیگر فرار کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/alonews/119476" target="_blank">📅 14:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: شواهد و قرائن حاکی از آن است که چین تمایلی به میانجی‌گری بین تهران و واشنگتن ندارد، و دو طرف نیز از این موضوع آگاه هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/alonews/119475" target="_blank">📅 14:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: شواهد و قرائن حاکی از آن است که چین تمایلی به میانجی‌گری بین تهران و واشنگتن ندارد، و دو طرف نیز از این موضوع آگاه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/alonews/119474" target="_blank">📅 14:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dcf15e48.mp4?token=diUKPp9C0nqHGmcY2FOH9dAFVq4JdfpHo3LJgASP3_C6Lkw9lTC2bkmuf7ne-sBQlaacq9hnaZ8p1RIhoTBf7uHM_bFbzsdG7D8Bmk-n4CKg73szHFdhjLxBU_GLDwPAHw2Sxi1JQ2AtJBKNGEBg-cU9vRFmEwsD5XLwaUjoCaXa3vihusNstDowl588erB6H-gXfKtGg5n-E7_67Ftn5lahO0fylftzL6s_8-DYCrIugZ9n5vOtLrtv48xgIUSbcD7gDP-f8wBBUCdXfjVmtbFfJwYOWY43qgKwfJYbQUh8-_NBjbxT7YbhtyayZjULg3giLZOcadSYZbbpzXLv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dcf15e48.mp4?token=diUKPp9C0nqHGmcY2FOH9dAFVq4JdfpHo3LJgASP3_C6Lkw9lTC2bkmuf7ne-sBQlaacq9hnaZ8p1RIhoTBf7uHM_bFbzsdG7D8Bmk-n4CKg73szHFdhjLxBU_GLDwPAHw2Sxi1JQ2AtJBKNGEBg-cU9vRFmEwsD5XLwaUjoCaXa3vihusNstDowl588erB6H-gXfKtGg5n-E7_67Ftn5lahO0fylftzL6s_8-DYCrIugZ9n5vOtLrtv48xgIUSbcD7gDP-f8wBBUCdXfjVmtbFfJwYOWY43qgKwfJYbQUh8-_NBjbxT7YbhtyayZjULg3giLZOcadSYZbbpzXLv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند اسرائیل برای رهگیری پهپاد یمنی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/alonews/119473" target="_blank">📅 14:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مطمئن هستم هر کسی که جرأت کند پا به خاک ایران بگذارد، به‌شدت آسیب خواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/alonews/119472" target="_blank">📅 14:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/هم اکنون ارتش اسرائیل از رهگیری یک پهپاد که از سمت ایران یا حوثی ها به سمت جنوب اسرائیل شلیک شده بود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/alonews/119471" target="_blank">📅 14:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر امور خارجه قطر: قطر و ترکیه در حال هماهنگی تلاش‌ها و حمایت از دیپلماسی پاکستان برای دستیابی به توافق در اسرع وقت هستند.
🔴
ما مسئولیت داریم که اطمینان حاصل کنیم جنگ از سر گرفته نمی‌شود و دیپلماسی راه پیش رو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/alonews/119470" target="_blank">📅 14:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
هاکان فیدان: بازگشت به جنگ جز خسارت و ویرانی چیزی به بار نمیاره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/alonews/119469" target="_blank">📅 14:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پنج پیش شرط ایران برای مذاکره
🔴
این 5 شرط که هم در ویراست رئیس سازمان تبلیغات امده است و هم در مصاحبه سردار جعفری بدین شرح است:
🔴
یکم : پایان جنگ در تمام جبهه مقاومت،
🔴
دوم : رفع تحریم
🔴
سوم: آزادسازی اموال
🔴
چهارم: پرداخت غرامت
🔴
پنجم : حاکمیت بر هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/alonews/119468" target="_blank">📅 14:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjkRWelIkSgVStE--hiRezITNlivbxZ5o4i_3MXXIBGA4KfoS6dkmUUjxGXbBTJWXtRyjR9k26ZzSGhSLsLe8dqed1RgLt21U39EatQT_kWffDqyD3GVgQpOE70CxYRPuA84v59jcsb6USByOG00izsxgdv4S0Sk5HJdlYm5U-376ox-RO_F8bME3YC5DO2D5VFvfj2WH0TNxEiB6w4AqdtLq2Ggmgj_xbnTSyPtY-yGzvjw6Wtv-3vDUoGb8w7N7OL8JhCCCZCHv1a7MrOcY8Q0Xvm9rB6ZxbnrtCLZDeGzMhYqh705zDsiSKaSq7M11OZ-lGIb91aky78WN0Xtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علیرضا دبیر عکس‌ کارولین لیویت سخنگوی کاخ سفید با بچش رو گذاشت و نوشت الهی داغشو ببینی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/119467" target="_blank">📅 14:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سپاه اصفهان: امروز از ساعت ۱۵ تا ۱۸ در محدودهٔ زردنجان احتمال شنیدن صدای انفجار کنترل‌شده وجود خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/119466" target="_blank">📅 13:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUXQzbhrO24PvwFtnTL6DmkuM7tan6Y3cioXGuNnoWJbJE9Yd4dE5PpZwmIydc07fX82-yX9kUWhpEcu6F2itFBfP5eEFj43czRvmmUDyVf_2Ig-UkHZEeWBfXow1KqlfUXll6FIiASMaSlscFo0lFTSS8erjPv7pDxK397QTF3GRqUVInmTlwXQ-yFw12BeceM2vkWwFugsZa_q7RzLO6O_ZiF8Bq8aSNBsM3ys6-49gv4vYdljTAe1IEPoNtmMCn-LqnlvxEikQeYvUGhqbuZ07KvqAHQ_6oRR7xmwnyVOkvUMuYOWS3snXsVaoYa0PkOp6wVDBqDBD2vSbGe-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLtLH4xzkkAMGS39H1NfCGnTzn87c9cNJEOXLzNkK4OHe7HROyZn4-JD60_S6cPQPZ8FER0_MO3YWEEJ7wLHvJ1UU7dGR-TEqFyD93fq8qwh4eoIht3VJGhjVs9Si8UU6WBO0HbW3mwcvz6FYwFOm5mxOFvDRbTsa1vcBeA_pVWaZD7cF_X9kbwiNKjB0Idcvp2Il89jSBhcUn4HgxP_cIQFwW4FqoCosCGsHltTnZ8ZwtbvH90NcEyIn6s1899lWTFVLsPu-6D-FBKkyGVdPn9Ua79sNW8QAuxTSfybNY3Z4jSzquLA9lTeDO7k4fpBXPnDfotx1TT4Or3K1vhOiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به فاصله کمتر از یکسال بسیجی‌های دانشگاه تهران به اونایی که میگفتن قمار باز الان میگن شهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/119464" target="_blank">📅 13:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/119463" target="_blank">📅 13:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej27_QNFbEcNEPUFdiDwklWH3RTuLNSLyFPvrbnuyaNyrcH7---mih5PJZVAiQ0dXGHpsxippnil-IdVF5m8O0yqddAwo3PIpXS0SeeB7tgwU_LVG3fwQL7O-3f0s_FdPVtuLEq7Kt93jAPhW9QEXrcPU51LbU9aLXf1-lJKAA3H2tvExwkcDF3VZJ7WWWG8DzFN17d2Nz4ERdupgga7FhN-zr3L6r2kAGU0qosy7ts13SDrsO66m86BBWPEW5sGdnpjauZP6IwJ_lwfZrACZjma1NSnHBN9GdXc5g-152-mLad69hNBsP_yOyMknKxA9xQI-zWfeRa4JG6w5xRKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
علی خضریان نماینده مجلس خیلی شیک و مجلسی گرای یه پتروشیمی بسیار مهم کشور رو داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/119462" target="_blank">📅 13:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دیوان امیری قطر: امیر قطر با وزیر خارجه ترکیه در مورد اوضاع منطقه و آتش‌بس بین تهران و واشنگتن گفتگو کرد.
🔴
دو طرف در مورد تلاش‌ها برای کاهش تنش‌ها و تثبیت اصل راه‌حل دیپلماتیک گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/119461" target="_blank">📅 13:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGcqsntREKVIrEbDJqL387RdJGcSjuoPRFQ8Ytx2bO2Hff4D64qiM1LzCsJNcgwKNhtu6Y4MXOIGOBjYAlk8gYVn4qzVBCbKpi1h9Ro5_lkiRCkCn5oY0CMe4Ekr7BeQpQ_HGXfBl_rGuLt6hNknGqmK2BbcR8MrX0jlAsEViloMTycJETdqN5QXRofgrORFXtdU7SRnHhNVF_K-mbbGc2ekgEZhFNH-wUnhbRmjayiDofQyvf2iO32amESLSrStp2W9etMYZylehIit2_hFsw7wy_j4mf9A7sxo6kNj4tcHRSIPRxzZrFdqIdC7tvBnzMh1vof8sMujdk1pFjJwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
هر گیگ فقط 150 تا 100هزار تومان
🔥
🔥
💥
🔝
تخفیف ویژه به مناسبت 100کا شدن مون از دست ندین
💰
🔍
دنبال یه خرید مطمئن و ارزونی؟
🔄
💯
فقط با 150 تومن، مستقیم و بدون واسطه خرید کن.
این فرصت ازت دست ندی دیگه نیاز به هزینه اضافی برای فیلتر نداری واسطه پاک‌کن مستقیم خرید کن
✅
📣
💎
ما ۲۴ ساعته پشتت هستیم و اگه راضی نبودی، وجهت رو برمی‌گردونیم.
بزن رو لینک و امتحان کن:
🎮
🛡
@premiumzone6bot
🎮
🛡
@premiumzone6bot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119460" target="_blank">📅 13:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzcwjxNY02wjI12w1kLuQIo5WdATW2AJcwe7BcRceSQkkYf77L7qbOlvz7yfpvgH_1AruI60vVu2-2iPG8gIz1kw52eHLBBLeGe_55X-mcWYAcCojIv4BBQXiP11_BtCfgGw62XByEDm2UK8o2PGHhH0t2mHc5NX5Lwu73LM4VStmUIJ58hph-jJZ2N8D6W8vgzbg8jR6QSTX9JWwCbGxZJTd2k24C5dmGnRASk8kmlb349op2-7HPatl_BwkhsqDxZizp9TE-Re1yCiUCIXmekQm8QDwY4LqopC2qFgbfID484qrSP1wD_wPfb_Ex_9CR3sNSvjvB58PuuPoGgyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۷.۱۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/119459" target="_blank">📅 13:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بحرین : برای ۳ نفر که متهم به جاسوسی و ارتباط با سپاه پاسداران ایران بودن، حکم حبس ابد صادر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/119458" target="_blank">📅 13:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تداوم اختلال GPS در تنگه هرمز
🔴
داده‌های شرکت ردیابی دریایی WINDWARD وارد نشان می‌دهد که اختلال GPS در تنگه هرمز همچنان تداوم دارد.
🔴
حدود یک هفته است که اختلال سیستم‌های ناوبری دریایی و GPS به دلیل تحرکات تجاوزکارانه آمریکا در تنگه هرمز افزایش پیدا کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/119457" target="_blank">📅 13:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سفیر آمریکا در تل‌آویو می‌گوید اسرائیل سامانه‌های گنبد آهنین را به امارات متحده عربی ارسال کرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119456" target="_blank">📅 12:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس : اگه دوباره به ایران حمله بشه، یکی از گزینه‌های روی میز می‌تونه غنی‌سازی ۹۰ درصدی اورانیوم باشه و این موضوع تو مجلس بررسی میشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/119455" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLG_KwmTXUejifju72LB-Kh2NQ142qDYcV7Yh120F5b0N-XaVaaTpydLoPygiOrcDJgJXODM9ibw9RtA22wk5Mm99xAxPJ6L7axx83K4JT0NCIBaTwxflEEr0nifMEaeJ8ArJVLzSm8-UYH0YYaxdiAZCaaph66oaSmRisEMYIonM7IgXSMsmTx93TKicH7teulc9jkPTpcgW3l3uJidcBDb6nR-iIfV1ABPGSRuAPLFyzv3xQIbDYt9HalYbiyRsw-iq47RiRrzJDiys5avDIAH1xngafqVdyc00iHIZqeOp69kc9XTGfm4SRRpb6W-nsWv8mcENGXxOyCdMqnyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: به دلیل کمبود نفت، ژاپن چاپ بسته‌بندی مواد غذایی را به صورت سیاه‌وسفید آغاز کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/119454" target="_blank">📅 12:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
داده‌های ناوبری کپلر: ۸ کشتی روز دوشنبه از تنگه هرمز عبور کردند؛ ۵ کشتی از تنگه خارج و ۳ کشتی وارد شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/119453" target="_blank">📅 12:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
صدر اعظم آلمان: توسعه اقتصادی ما برای سال‌ها راکد مانده است — حداقل هفت سال — در حالی که کشورهای دیگر اطراف ما رشد می‌کنند، برخی به طور قابل توجهی.
🔴
پیش‌بینی می‌شود رشد بالقوه کمتر از نیم درصد برای سال‌های آینده باشد.
🔴
برای کشور ما، برای رفاه ما، برای اقتصاد ما — این به سادگی خیلی کم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/119452" target="_blank">📅 12:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سفیر آمریکا در تل‌آویو می‌گوید اسرائیل سامانه‌های گنبد آهنین را به امارات متحده عربی ارسال کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119451" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqD-geYRu-NZOWNF6h-2r2gQCSh4fivGpnjRqfZb37d8Ni5d3646NNfQT8hwU8COLLLP3tmYiPbZS842d303_qopZ4nmuSCdhJ88yZfZeAmncC1hAPmKftaq_VKIXH5bMYlV6cDtZNMuh-0hu86wcS0jZSZKVw518mIKGeOHXX6RDpHkzZl7UK9HJosGS8UMgFMlBP9yYq5iq9RyRHp8HaYLf116wOBhudM5CivIFH5J8x-IDmwygH1JSlJLV9rJzOwuQ7wTRRWKmvnZWo7nDlmPibSzWtxZsszPUhiFJuNhZbLZlT43e4zbviz6jsQISQ2urpXcqPPFjj87rJ2ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرا ‏گوشی ۱۱۰۰ دلاری در ایران ۳۰۰۰ دلار فروخته می‌شود؟!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119450" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر کشور پاکستان: انفجار یک بمب در ایالت خیبرپختونخوا واقع در شمال غرب پاکستان دست کم ۷ کشته و ۱۸ زخمی برجای گذاشت.‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119449" target="_blank">📅 12:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119448" target="_blank">📅 12:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا و ایران در یک بن‌بست دیپلماتیک بر سر موضوعاتی قرار گرفته‌اند که سال‌هاست دو طرف را دچار مشکل کرده است، و این درگیری اکنون در وضعیتی نامشخص و خاکستری قرار دارد؛ حالتی که نه جنگ است و نه صلح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/119447" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سی‌ان‌ان: بسته‌های چیپس کالبی ژاپن با تشدید جنگ علیه ایران، تک رنگ می‌شوند
🔴
شرکت تولیدکننده تنقلات ژاپنی Calbee به دلیل مشکلات زنجیره تأمین ناشی از جنگ خاورمیانه، بسته‌بندی خود را به سیاه و سفید تغییر می‌دهد.
🔴
این شرکت در بیانیه‌ای اعلام کرد که این اقدام در واکنش به «بی‌ثباتی عرضه که بر برخی مواد اولیه در بحبوحه تنش‌های جاری در خاورمیانه تأثیر می‌گذارد» صورت می‌گیرد.
🔴
نفتا یک محصول جانبی نفتی است که گاهی اوقات در بخش‌هایی از فرآیند تولید جوهر استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119446" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فاطمه مهاجرانی: وزارت علوم مکرر و روزانه پیگیر دانشجویان دستگیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119445" target="_blank">📅 11:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مشاور نخست‌وزیر عراق: گزارش روزنامه «وال‌استریت ژورنال» درباره ایجاد یک پایگاه نظامی مخفی اسرائیل در صحرای نجف صحت ندارد.
🔴
آنچه در صحرای نجف رخ داده، نه ایجاد پایگاه نظامی بلکه یک «تلاش برای عملیات هلی‌برن» بوده که توسط نیروهای عراقی ناکام مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119444" target="_blank">📅 11:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بی‌بی‌سی: ایالات متحده مذاکرات منظم و محرمانه‌ای با دانمارک برای افتتاح سه پایگاه نظامی جدید در جنوب گرینلند برگزار کرده است.
🔴
این پایگاه‌های جدید به عنوان قلمرو حاکمیتی آمریکا تعیین خواهند شد.
🔴
تمرکز این پایگاه‌ها بر نظارت بر فعالیت‌های دریایی روسیه و چین در گذرگاه GIUK خواهد بود.
🔴
ایالات متحده در حال حاضر تنها یک پایگاه در گرینلند دارد — پایگاه فضایی پیتوفیک — که این تعداد در دوران جنگ سرد حدود ۱۷ پایگاه بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119443" target="_blank">📅 11:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل : ما نمی دونیم که اوضاع در مورد ایران به کجا میرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119442" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
گزارش شبکه i24 اسرائیل نخستین بار از شروع جنگ نیروهای واحد گولانی ارتش اسرائیل درگیری در آن سوی رودخانه لیطانی با نیروهای حزب الله داشته اند که منجر به زخمی شدن ۸ نیروی تیپ گولانی شده است و به ادعای آنها پس از کشته شدن چندین نیروی حزب الله، مابقی دسته اقدام به عقب نشینی از منطقه مورد نظر(روستای زوطر الشرقیه) کرده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119441" target="_blank">📅 11:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
العربیه به نقل از سفیر آمریکا در اسرائیل:
نمیدانیم اوضاع با ایران به کجا خواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119440" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: اگرچه مذاکرات رسمی هنوز از سر گرفته نشده است، اما تماس‌های دیپلماتیک در سطح بالا ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119439" target="_blank">📅 11:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کره جنوبی هم به مذاکرات چندملیتی بازگشایی تنگه هرمز پیوست
🔴
سئول قرار است امروز سه شنبه به یک نشست چندملیتی سطح بالای وزرای دفاع برای بحث در مورد امنیت تنگه هرمز بپیوندد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119438" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d23b20d8.mp4?token=a9DaMaObRTVamUSown_XzJSv8piyyp88PgOz99v1dk4rHnDxX4LGRm7bFZ9dzigXqtq7siMUjuvgrxAWJu-_-wqVnRQPysNMImEJROT2hxbLb9p20FZQUpzrJR8tawKOrEsZHeF2YaBtB6q1cF3nyIukIahSLeFFOr6YeO-UzXlqAoagkBGuAOHmIG0zUt8P1Ozd5uJEj9ml60toOKMAQB3so7Wt0Sj_qXWeu9U58IofsWdq9L5kF30wY_2mh1e_i2XHk_98ZKTeq13YFyFWbLo9GgOcsHa4yDISsUR0ackyhUEDWEqtZ8G8qgy-1THvrl4XUYtqVTzX5qsuCyEMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d23b20d8.mp4?token=a9DaMaObRTVamUSown_XzJSv8piyyp88PgOz99v1dk4rHnDxX4LGRm7bFZ9dzigXqtq7siMUjuvgrxAWJu-_-wqVnRQPysNMImEJROT2hxbLb9p20FZQUpzrJR8tawKOrEsZHeF2YaBtB6q1cF3nyIukIahSLeFFOr6YeO-UzXlqAoagkBGuAOHmIG0zUt8P1Ozd5uJEj9ml60toOKMAQB3so7Wt0Sj_qXWeu9U58IofsWdq9L5kF30wY_2mh1e_i2XHk_98ZKTeq13YFyFWbLo9GgOcsHa4yDISsUR0ackyhUEDWEqtZ8G8qgy-1THvrl4XUYtqVTzX5qsuCyEMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ پس از شنیدن صدای یک پرنده در نشست خبری کاخ سفید: اوه! فکر کردم یه پهپاده؛ این روزها پهپادها رو در اندازه‌های مختلف درست می‌کنن و می‌تونن خیلی مخرب باشن، همون‌طور که احتمالا شنیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119437" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
معاون نیروی دریایی سپاه: تحرکات را با دقت زیرنظر داریم در یکی از موارد اخیر، یک ناوچه آمریکایی قصد عبور از محدودهٔ تنگهٔ هرمز را داشت که با رصد دقیق نیروهای مسلح مواجه شد و پس از مشاهدهٔ برخی رفتارهای تحریک‌آمیز، نیروی دریایی ارتش با شلیک‌های هشداردهنده و هدفمند، پیام لازم را منتقل کرد و این شناور نیز بلافاصله مسیر خود را تغییر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119436" target="_blank">📅 11:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9Eppm7h2mUB0ZCks3b-qD6YV_Lo33EMDNA4gXqE-zx6AwHd2xJbfcvBpPEefIqo_CByWQSpwekdXcyHbHdPC1xqJ2nJsCVJkCIzbI2nJUXcQ87Ok7L3isG9Ws2xcE824koFZIRhQno-N4c5mgO0JSZAXrikkH1zqSNyfIP1zbWydlW_tB1MhVpjYrhFRE2W9ZLpBcgqTzyuQIMX3qEYN89RCxbEN20FYOGfy_cjAtrcEZCD9ACRS16DFS0Teciu7bbCKmuMoRzaIgIafRs2BUSSVjN9DAIquQRIcdyJaJXDGFniRKquzHhLApMCt1VAyxkSMW9tUMAPb5RZUHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاکان فیدان وزیر خارجه ترکیه با خلیل الحیه رهبر گروه حماس دیدار کرد
🔴
الحیه تحت تعقیب اسرائیل قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119435" target="_blank">📅 11:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سخنگوی دولت: اینترنت پرو مصوبه‌ شورای‌ عالی امنیت ملی را دارد و اين شرايط موقت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/119434" target="_blank">📅 10:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3823c68f75.mp4?token=bFl6ZJCZhW7bwKJIEEuPgiJNxPH9i9L6RmDDm53qxQS9mvNfSLm7s1kxsGSdibSCLFZ0WgPPtH62LjDVV9xhOxYYz0BkOrv_2JsUUSF4thv_cA6wh7mPfMq6bivfFopzZJh-6Ihmzo6983sp8KUu-RRB8TYgvjTOl2hm1BMTA6n2qInAxnlm1IKddDlpOW3G8StrQ_OtPyC8QIaVRNt6suoEp2Wp-PrL8WlJ0GG9xkw3kzBIXSnOjqDvYmoZRWwsIFc2Jd40fsu_I8ivWLelyKYO0CUxyHd9d5-pdltRYArxiuol2hzmuefYXV9TbaZA2mo4hhZPd-EHXh1aw04gv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3823c68f75.mp4?token=bFl6ZJCZhW7bwKJIEEuPgiJNxPH9i9L6RmDDm53qxQS9mvNfSLm7s1kxsGSdibSCLFZ0WgPPtH62LjDVV9xhOxYYz0BkOrv_2JsUUSF4thv_cA6wh7mPfMq6bivfFopzZJh-6Ihmzo6983sp8KUu-RRB8TYgvjTOl2hm1BMTA6n2qInAxnlm1IKddDlpOW3G8StrQ_OtPyC8QIaVRNt6suoEp2Wp-PrL8WlJ0GG9xkw3kzBIXSnOjqDvYmoZRWwsIFc2Jd40fsu_I8ivWLelyKYO0CUxyHd9d5-pdltRYArxiuol2hzmuefYXV9TbaZA2mo4hhZPd-EHXh1aw04gv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : همه ۱۱۱ موشک ایرانی که به سمت یک ناو آمریکایی شلیک شده بودن، رهگیری و ساقط شدن
🔴
خدمه فقط حدود ۱۳ ثانیه وقت داشتن برای تصمیم‌گیری در هر درگیری
🔴
اگه یه محاسبه اشتباه بکنی، هم کلی نیرو از دست میدی، هم یه عالمه کشتی چند میلیارد دلاری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119433" target="_blank">📅 10:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7QETnACDp3vQOCMuLIMetrUvKu4ZYKORRBmNKMKMrsA_Ct0T9C-4qSXskohSpXTJ7uRkpT3imopfSqLWCb7ey-fvjGVfQv3nLoajU2SOhY1RodFxKq7VSNGfYpEiTWNbOzbN7CMt6EQFZiAm0bpq0fVYKq3eVV_pznRF4GkJ4VIShfs4qNtqQ3cJcJ5DsdoW6fba1EjF0nTZhFei9mzCGWAoRC8fQX_dnNamwDgf4p4MoYjVRTIXObWdj6iPbGrsSaL1drOYp7Sn4Ra3tC-rZ6fUdYO-1LUVqtwaMV3h_zHMuKbEwW2CReWQNICx2yLlm1akAwFelFzFHwlPdkZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۶.۳۸ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119432" target="_blank">📅 10:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قراردادهای آتی نفت خام برنت بیش از ۲٪ افزایش یافت و به ۱۰۶.۳۸ دلار در هر بشکه رسید، طبق گزارش رویترز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/119431" target="_blank">📅 10:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شیخ حمد بن جاسم بن جابر آل ثانی، نخست‌وزیر سابق قطر: عملیات نظامی به طور کلی به نفع منطقه نبود. آمریکا به دوستان خود در منطقه آسیب زد.
🔴
عملیات نظامی به طور شخصی به نفع نتانیاهو و برنانه‌های او بود
🔴
او به صراحت درباره نقشه جدید منطقه، اتحادهای جدید و اسرائیل بزرگ صحبت می‌کند.
🔴
آنها از ساختار قدرت در ایران بی‌اطلاعند. این هرم طی ۴۷ سال ساخته شده است،  اینطور که آنها فکر می‌کنند فرو نخواهد ریخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119430" target="_blank">📅 10:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b814539f.mp4?token=C0e63bPzWbVZ8oRa6juC2wfQ9vkqqwIiPcZKa7dZ0mV5cVwbHBKHWuUslBWLNhleqctB423OC3Q0rWMVbN032sL2RLg2GFIDBwYBtO2dYCE02wgK4tWr1n0n7wVF1g3YcoKnaWE9T9il7L4EOjk0YYefnElxVrP6s_qICct3j1h0VsIRXuG4LNU_Fd1gg3GlR1Q9eNvwazFnpnHcP101akLhAakP3OpAT9Mshzmq09HyPSkXjdbTSz_D6-PZNPW7cqFRslgAIMBNiTT62khxczhnmXMCfq-2d8-TVNlVxZsxTAYEgPSSk6mBM4Io75MfvzP2j-FiQgc_FhL7E3Gnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b814539f.mp4?token=C0e63bPzWbVZ8oRa6juC2wfQ9vkqqwIiPcZKa7dZ0mV5cVwbHBKHWuUslBWLNhleqctB423OC3Q0rWMVbN032sL2RLg2GFIDBwYBtO2dYCE02wgK4tWr1n0n7wVF1g3YcoKnaWE9T9il7L4EOjk0YYefnElxVrP6s_qICct3j1h0VsIRXuG4LNU_Fd1gg3GlR1Q9eNvwazFnpnHcP101akLhAakP3OpAT9Mshzmq09HyPSkXjdbTSz_D6-PZNPW7cqFRslgAIMBNiTT62khxczhnmXMCfq-2d8-TVNlVxZsxTAYEgPSSk6mBM4Io75MfvzP2j-FiQgc_FhL7E3Gnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ از رئیس جمهور بعدی آمریکا گفت: ترکیب ونس-روبیو رویایی است!
🔴
«چه کسی جی‌دی ونس را دوست دارد؟ چه کسی مارکو روبیو را؟ بسیار خب. به نظر ترکیب خوبی می‌آید. ضمناً، من معتقدم که این یک تیم رویایی است. فکر می‌کنم به نظر می‌رسد کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119429" target="_blank">📅 10:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhaMAK-DMGJjsaNnjyjsNHmpPIoERqwFQ-LIykRaAJNdmjbi-KOCD0CaY5q4d-zSHRyBV1lvHxtLfzQ0eZzwHsVetEMhcWFb9VSvaScpKrqkVOoIy81VASvijP_6zF-MrqWFOM1w_ly6rxUHnxXJGIjxJEELVewXxl7KqnMBLjZGPGrIdNWvKf1BIofX6Yj7U6Ux6OEw0fMVqZLo1KW0kZBZqomQxorX-bHvip-eHVRTZJW1F03oy7BBPD6PKh-gLxxwO6aouGc5x7cRrIBEB0KtooJdUuMLPMA6u9E_5WFyvQO9YmOtJO1obMSnyJzMNOw66DHgIALihQqETJvhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: از نظر من باید با خانم‌های بی حجاب برخورد فرهنگی و انتظامی بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119428" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSpfXsbx-G5b26k2baSEbscjWFk-xC5EJzlxA8JDM3j6dy3C-ETaQ0zGPB2oyhe5pVOdJruprzxYSmy-GD6c9uoaqVcu7m1SxsNf64mjpSStUjtJVtL3a_S-p6-1_jqP8oPCvEnhw52IikCfx46IqlzTVuikgH55sT4GoUFpfWFA8JKmXQAsHikMcp2EGh-XnC5EbI8vPImLWgzqDXHsgn1PQPt3zH0B0ZAr1UATgDisTa5KG2FD60Bl2-xIwh9DHpu4gNvKp9EiXU4K8ntQhUYOZUvYuWWdEO6nWYNLA9TcRbECS44oJrPp8Hi-t092aOgOb3u2a3byU28gxrz98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل، آویخای آدراعی، هشدار فوری به ساکنان ارزون، طیر دبّه، البازوریه و الحوش در لبنان صادر کرده است تا فوراً خانه‌های خود را تخلیه کرده و حداقل ۱۰۰۰ متر به سمت مناطق باز حرکت کنند، با اشاره به نقض آتش‌بس توسط حزب‌الله و هشدار اینکه هر کسی که در نزدیکی اعضا، تأسیسات یا تجهیزات حزب‌الله باشد در معرض خطر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119427" target="_blank">📅 10:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759573b975.mp4?token=GfwmMufn-aau0R7JarmKVXZOG4OXARKhX0mRiizwroTApIVfKgGwCBF2orgmnyXByB_JQIeW-Qf6uNgtOGiMdOm9W90-xcqx793ZgF4WWS8WogKmceN3lpdlr1bVU-gZ-BOTX-1A-aG1bhlHpeMb8mGAP0KV_NuhuHoM4ToBrZKKCKIAN37YuGILk-uzNvQkQ6X5D1vnmVaRrF-XcipKFEQCNyLNi6HF7lLGufyFh5mwF-yZKi5lNvYm94hN0IEAbyq1dU9lyDVuJlKMZA311mPH2D5idSG_ux85Zqmrxc8eriyi-ZCx01fqFXydvPMCp6mKMTa_RYv5NplRLM1hrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759573b975.mp4?token=GfwmMufn-aau0R7JarmKVXZOG4OXARKhX0mRiizwroTApIVfKgGwCBF2orgmnyXByB_JQIeW-Qf6uNgtOGiMdOm9W90-xcqx793ZgF4WWS8WogKmceN3lpdlr1bVU-gZ-BOTX-1A-aG1bhlHpeMb8mGAP0KV_NuhuHoM4ToBrZKKCKIAN37YuGILk-uzNvQkQ6X5D1vnmVaRrF-XcipKFEQCNyLNi6HF7lLGufyFh5mwF-yZKi5lNvYm94hN0IEAbyq1dU9lyDVuJlKMZA311mPH2D5idSG_ux85Zqmrxc8eriyi-ZCx01fqFXydvPMCp6mKMTa_RYv5NplRLM1hrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد خوش چشم سری قبل گفت جنگ نمیشه اما شد، اینسری گفته جنگ میشه ظرف ۱هفته و باید ببینیم دوباره گلشعر گفته یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119426" target="_blank">📅 10:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad4ea0df5.mp4?token=i9YwiqMyzSq5AgK4ZeoKgC2rgRERYKAxhDiB_uI9MdjTsi4eLbwIVPJUtETbBFmasnKcf5CL28xF6ufqcuegNqRbVUoqytLqSd5MxHcfWe0VIIK--VpDCmGuaaPDmp5fRYpvWwErj9e0FVPDeEch9q7oQsnjw6YA4wzuVml8FdMkUExEuav4QkjbsNgvVjB-_OzoEI_pNo4Uc0Uzj5NDHwV7Z25XG-3R-n6oUh9vU7aZhAimEPFl7-5EDWWfCakP37T-uM438vjbxa3BNzNlyfcFIP5W1P_uQNcXCdGlBwbj4hXj27SjdWWb1-7D9NI2t7IT2D9IdtzQmxbQXHSVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad4ea0df5.mp4?token=i9YwiqMyzSq5AgK4ZeoKgC2rgRERYKAxhDiB_uI9MdjTsi4eLbwIVPJUtETbBFmasnKcf5CL28xF6ufqcuegNqRbVUoqytLqSd5MxHcfWe0VIIK--VpDCmGuaaPDmp5fRYpvWwErj9e0FVPDeEch9q7oQsnjw6YA4wzuVml8FdMkUExEuav4QkjbsNgvVjB-_OzoEI_pNo4Uc0Uzj5NDHwV7Z25XG-3R-n6oUh9vU7aZhAimEPFl7-5EDWWfCakP37T-uM438vjbxa3BNzNlyfcFIP5W1P_uQNcXCdGlBwbj4hXj27SjdWWb1-7D9NI2t7IT2D9IdtzQmxbQXHSVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار پالایشگاه سالیناکروز در مکزیک
🔴
براثر انفجار پالایشگاه سالیناکروز در مکزیک، ۶ نفر زخمی و بخشی از این پالایشگاه تخریب شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119425" target="_blank">📅 10:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ارتش اسرائیل تصمیم گرفته است کارخانه‌ای برای تولید پهپادهای انفجاری به عنوان بخشی از پاسخ خود به توانمندی‌های پهپادی حزب‌الله تأسیس کند، طبق گزارش یدیعوت آحارونوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119424" target="_blank">📅 10:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سفیر پاکستان در مسکو: مذاکرات ادامه دارد و ما معتقدیم که دیر یا زود به نتیجه خواهیم رسید
🔴
بن‌بست زمانی است که شما کاملاً از گفتگو با یکدیگر دست بکشید
🔴
خدا را شکر، آنها هنوز از طریق پاکستان در حال گفتگو هستند و مذاکرات ادامه دارد. این چیزی است که به من امید زیادی می‌دهد
🔴
مهم‌ترین مسئله در حال حاضر باز شدن تنگه هرمز است که در ابتدا حتی روی میز هم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119423" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdzzrx878DC3ZZqPaSWCLqfe41XEI2nEG51hFBcXkV5qdp-qfmNWKMMn8YVscW2pD14RCpd1ShY6arEbNI4pypBvKGemDzGYH8fTErg7YWKlgcSvjxafh1i0HDjxHYZahvh_nH39En7sm1ir5psGE76FEFXzBFdKKT-dlKmmCV58tYdoYgHP4LTyf0uPKtyh4Dp3MyW2mlAeGhFUrsu6_VZlUceOuvAtZ5-u_KRJliSXInKT3E40M4KpYOcaAX5fmvqlundvPdyBSta78LEWbD8SKsvW1_zgvf1ZNqEWfIDR489ZCd4WCpMDf6RT5xBErlM-8GXKEetYos4yJivvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پستی را بازنشر داده که خواستار بازداشت اوباما شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119422" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
انفجار برنامه ريزی شده در 3 شهرستان آذربایجان شرقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119421" target="_blank">📅 09:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روزنامه تایمز: وزیر کشور انگلیس، به همراه شماری دیگر از وزرای دولت از استارمر، نخست‌وزیر این کشور خواسته‌اند که به تعیین زمانی برای کناره‌ گیری از مقام خود فکر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119420" target="_blank">📅 09:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت علوم: به دنبال حضوری شدن کلاس‌های درس و امتحانات هستیم
🔴
دفاع دانشجویان حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/119419" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTynI6NPyjwV2NJotc_4val6cZ5rrhLeVjTmaZpcc9z4GD43W_4amzYFoSiguNHVT5xifliLve0cXnkbd3jAzxhHMkISlGTrIxnaeEH35z5nzGqgtm2skZtklIQnAPFD067hRWYrXO-4d5xzjmhs25zhRf3Ut5b-0TSua7O_SbSC1ZAwboATH1mLoYjXJlEXN0_jmSMmZ2W1ekQdDDcoXgJr5ZS06wZXQgVr-6c5-JLpy2fEEIebZUHAYhEeJtasqFPGZgiRpcYaQy0jv_7m7eeZ_r5-GEIVGhRCeaGHqVILqqF3kBBrQoZYXvNa01Ip0k33CX4vRzfs0ZFdXsQg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش سی‌ان‌ان، بسیاری از افراد در دایره نزدیک ترامپ می‌خواهند میانجی‌گران پاکستان رویکردی سخت‌گیرانه‌تر و مستقیم‌تر با ایران در طول مذاکرات داشته باشند.
🔴
برخی مقامات دولت ترامپ به این موضوع شک کرده‌اند که آیا واسطه‌های پاکستانی به طور کامل ناامیدی ترامپ از مذاکرات متوقف شده را منتقل می‌کنند یا خیر.
🔴
دیگران معتقدند پاکستان ممکن است تفسیری خوش‌بینانه‌تر از موضع ایران را به ایالات متحده ارائه دهد تا آنچه مقامات فکر می‌کنند واقعیت را منعکس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119418" target="_blank">📅 09:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: بی‌صبرانه منتظر سفرم به چین هستم؛ اتفاقات بزرگی برای هر دو کشور رخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119417" target="_blank">📅 09:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCpL1RaQZyALN0In5jCPmFyCq7sXzy_BgChmGgJc9ISd77PM5nM7i3c9tAZGhiQ_XrAB5Vnq3LKd36gaAqYJk5J2_jW4DqQ47uEklvy7nGNC244rrZ4Lxn3hz-3xZoazAIxW1fxwl87d4MzrCnkNzL5k4fWxNvHRNs5YY5vxjXQdaVGhvaGkyX4fegXbugeUgY0tSPQTT3sGH7nCQINl1dVdgmlLPBCqNlzOdkE_XO6KJaZ7HXIMW5G8jbdj_wklRuuE2ty57LLM4H3_8SmB8c9dqr0KFQd4Q2ztDlOuHHaYgffAhNfRARdEO9yQPiqTPl7lSYgkAFs7b7eAqZuQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : لنسر B-1B نیروی هوایی آمریکا در طول یه ماموریت آموزشی تو خاورمیانه پرواز می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119416" target="_blank">📅 08:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فایننشال‌تایمز: قیمت کودهای نیتروژنه که بخش عمده‌ای از آن در خاورمیانه تولید می‌شود، از زمان آغاز جنگ با ایران بیش از ۳۰ درصد افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119415" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بلومبرگ: آمریکا تصمیم دارد بیش از ۵۳ میلیون بشکه از ذخایر استراتژیک نفت را برای جلوگیری از افزایش قیمت‌ها به دلیل جنگ آزاد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119414" target="_blank">📅 08:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پاکستان هرگونه حضور نظامی هواپیماهای ایران را رد کرد و بر تعهد خود به صلح تأکید نمود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119413" target="_blank">📅 08:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
استرالیا 7 فرد و 4 نهاد ایرانی رو تحریم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119412" target="_blank">📅 08:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وال استریت ژورنال: هنوز شکاف‌های بزرگی بین مواضع واشنگتن و تهران در مورد مدیریت آینده تنگه هرمز وجود دارد.
🔴
همچنین در مورد نوع محدودیت‌هایی که تهران برای برنامه هسته‌ای خود خواهد پذیرفت، شکاف‌های عمدهای وجود دارد.
🔴
دولت ترامپ، تاکنون هیچ هدف راهبردی را محقق نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119411" target="_blank">📅 08:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به طور جدی در حال پیگیری تحقیقات درباره نشت اطلاعات پس از جنگ ایران است.
🔴
ترامپ شخصاً به دادستان کل موقت تاد بلانچ دسته‌ای از مقالات خبری با برچسب «خیانت» تحویل داد و وزارت دادگستری را تحت فشار قرار داد تا سوابق خبرنگاران از رسانه‌هایی مانند وال استریت ژورنال، نیویورک تایمز و واشنگتن پست را احضار کند.
🔴
این احضاریه‌ها مربوط به داستان‌هایی درباره هشدارهای نظامی پیش از جنگ، لابی‌گری نتانیاهو با ترامپ و عملیات نجات جت‌های سرنگون شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/119410" target="_blank">📅 08:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دفتر نتانیاهو خطاب به اروپا :  چاز آنجا که اسرائیل و آمریکا «کار کثیف اروپا را انجام می‌دهند» با مبارزه برای تمدن در برابر دیوانگان جهادی در ایران و جاهای دیگر، اتحادیه اروپا ورشکستگی اخلاقی خود را با ایجاد تقارن نادرست بین شهروندان اسرائیلی و تروریست‌های حماس نشان داد.
🔴
تلاش‌های اتحادیه اروپا برای تحریم غیرنظامیان اسرائیلی نشانه‌ای دیگر از ضعف است و موفق نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/119409" target="_blank">📅 08:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPbzQKgDi5PB4cFqL4sOr77QCFJrveKyxm7eegCEe9B-idvv2fooofaFSVxBCw5bbfubeCYxQAiLM9sF9oxdw2qYtn6xbFSKdeR2z-g4Sit0nwXUMtGDhiO89ZQw9ea9dM397omA0ITDnA7NNzDYoxB59rdFrB0Qkq0RQ2ssiBQztspUKyqa6hILHKJf-E-XwRMGB1NuBTwyVa6ldrI2fyryW6Oph2Tlzx5g3_Q2QvuairJPS5LgduGU3IQLEvVT2A-SuVtWwwNbfKJ_R6UttWSIY2vdukTB5i77_2x7LmYF3ZINpN72gYOJaN9oHRDY6ksbMq79tiNFcUrbqwLSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش والای اسرائیلی
: ایالات متحده هفته گذشته به از سرگیری حملات به ایران نزدیک شد، اما تصمیم به تعویق افتاد پس از آنکه مشاوران در دایره نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند
همزمان، مقامات ارشد ارتش اسرائیل به گزارش در جلسات بسته موضعی سخت‌گیرانه یکپارچه ارائه می‌دهند و استدلال می‌کنند که رهبری سیاسی اسرائیل باید به طور جدی حملات استراتژیک به زیرساخت‌های ملی ایران را در نظر بگیرد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/119408" target="_blank">📅 02:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629e528bb8.mp4?token=hB8x4ytEgYT7bjJSx0IO2-UGHR8Sn706jOh4E-hqdWVV6buvkc5LLSL2wP_Ri8EUcK12X2nMFk2TVwYRXUNUj2rOjFc89DShETUh9YOuJJtEzMuclcz8qWt_PEVyQMiAhycMpy2NnGpoQzTPK9-8F3bE70XELHdxwfbuVQzfAyX_Eu9-1pmnPveVzH6poAbTZGqMN7cMVUjk5yuXTvvdqMgjdTuBMVqckY_sHkIMhkSkmgGYiL_j-K0HljW0yzhjn3rXSx3T-OllbWORAdzj6rdjgwfstTXTob_5GyMatsd2ixYJtgVUv3-WW7DYYC_rbpIkq3GxAg8MOlwSmZVDbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629e528bb8.mp4?token=hB8x4ytEgYT7bjJSx0IO2-UGHR8Sn706jOh4E-hqdWVV6buvkc5LLSL2wP_Ri8EUcK12X2nMFk2TVwYRXUNUj2rOjFc89DShETUh9YOuJJtEzMuclcz8qWt_PEVyQMiAhycMpy2NnGpoQzTPK9-8F3bE70XELHdxwfbuVQzfAyX_Eu9-1pmnPveVzH6poAbTZGqMN7cMVUjk5yuXTvvdqMgjdTuBMVqckY_sHkIMhkSkmgGYiL_j-K0HljW0yzhjn3rXSx3T-OllbWORAdzj6rdjgwfstTXTob_5GyMatsd2ixYJtgVUv3-WW7DYYC_rbpIkq3GxAg8MOlwSmZVDbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل: بخشی از
اهداف بعدی در خاک ایران:
🔴
تاسیسات انرژی و صنعت پتروشیمی
🔴
صنعت خودروسازی و پایگاه‌ های موشک بالستیک
🔴
صنعت نفت و صنعت فولاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/119407" target="_blank">📅 02:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z24JfmSVGwvo7kkjJosLMads3rzC6yrHq60XgdocWEZhkei6t4K1pIh0PogbW9kmttzeY-wgRGWH-0s52rcntqvE6PfRNsJUfBXfEQjC81pd-fcvlq2LuYoZ0kcUFXMd54QYNYKWNsSuPIHFrg4mi2qcxEgfSWFpJXvkr2yrsafCbx8iKRAwI6hOgLacoaUtGXvQhiKxkGe2gX8hfs2mFVpOTOKHxsdnX7KVN8MSU5ufDtPuW8tyUis6kskHvv1dY4Ss0vmwggNi_4ZkMqbYl2S7iFa2m1TDaSpRT4Hz3y1RBSnY0qUmR3f25Wvc893oT7b-Gwxj0hT0qlR8iXY7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGT7G3DsEwdLd4g8jztcDZg4DhGuSJHIReg4nipzbdBnxNSGzDRYQcCNE1HzQ--lubCxhrjGSbPbLv64cmK9iSEu5eN1nzZA-rHsBVWITKgxtI9-_z8F4Yw2Gw2tYHdpfFcZEY6WYxwLZOv4q25Yv_pniuRgltGr1c8EYMQ6LbyVHCe87wmPPTSQ4UpdcRuasKMIMPPZqMA6U5J7fx7ndw8qHuWUWW3AQFFHVYCAqQYMBzdYPX-YoNvYh-zR-KFLEcvY-ND60g2zSK5c5FxM1_l8SUT377ntFdjZWSjucR8VsluKcIKnnsPKwQvZJ9E2_DkdLEnYEeyiWc9098PTCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دو روزنامه تندرو و کم مخاطب داخلی مذاکرات با ایالات متحده را رد کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/119405" target="_blank">📅 02:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbdEeqAi0f7SrOAdT-UjJmm3ML_7sgG01xfvfERW5977OefbEwghhzW1DTgDbKf9EmSRC8upNXSTTElmUXMAehY8M2x7Ru2MQihbNGUQiKciH5yY0gEsgBUJYCM1hlt3AXpDu9QpTZDX0VTqLhX8cfczYkIJTRZJzfaBAZjuZyD8HF-NMslyZd_XQwCAyz4w9RbUDhgwsJz5q_hy_qCouX6Pqk5P-45cpwcndprtue11H41EooTdM5anU5XuW9ygRNbSAgQGKCy24WfNtfHygt9_7qeeub0nhoqHZHAS3e-Sp77kxFnAKcXy8-14CQxoVtc-OSSxWtY0IOfZzRwEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر جالب روزنامه سازندگی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/119404" target="_blank">📅 02:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqekmOaBtdeskR6QoOBcwuXldx4aDbvbU3-AtAsoUt7RPft3cokw0gZdBltcZZujjbVLJ528oxXZkiLTFBkOegy6lasdezCDhxOSsDzGINWoMy3HtxsanLx-j1r6S6s-np60oCu2epmMQxzj9KfbAGrqBH2ckn_e4PdxBdG_ZbRAm_BAY-xq6FuDNLpWshiGc6Vv3xdP_6YwhTWotFMnCNdep3cZ3JXB5s2Js5kpnjEvnaxLQLpl2b5uxmkwUX6eLuBjNp1sqsGOuBpjtoQWTba-HZhuZOE8CJxKN_ZFzRifrrLh5P8IcmwG73nyGDzj5-rk4Z6fA1rMN_87mLo32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری والا
: ساختار دفاعی اسرائیل ارزیابی می‌کند که مجتبی خامنه‌ای مانع اصلی پیشرفت در مذاکرات ایالات متحده و جمهوری اسلامی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/119403" target="_blank">📅 02:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62afb37ea2.mp4?token=IrPsXEHcTXZ5MUWbp98XK_RhpBu9CeYh8_JHLJpjSibrXQ9n9r27CIYyidpwQbiUXr42AMSYkZ2Pv-q_G2chrJltMgCrzvlqRqAkQvcNv4BNv2qlHh3rFfmtoZGsOR4-qklnVviiAUeVdCDcjVsrQX6z7OJX_yGnm-9vff9Wi-FWmdrPkuuVtz4SSzV3AYQjKffG2W6bvghjYaQdJxbRLrqAljGh-Vx9UXzNnR4CUpM5qZ6xLmB2l1hBfk-8IDjo4a_-i7DEo9hdrBwBokulzyzcTVoXuQ_xvHxaKJ6NmOmzvLjrVYsJwIWPTp2pS7z-EILwHOpLTqMCteoyqeOCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62afb37ea2.mp4?token=IrPsXEHcTXZ5MUWbp98XK_RhpBu9CeYh8_JHLJpjSibrXQ9n9r27CIYyidpwQbiUXr42AMSYkZ2Pv-q_G2chrJltMgCrzvlqRqAkQvcNv4BNv2qlHh3rFfmtoZGsOR4-qklnVviiAUeVdCDcjVsrQX6z7OJX_yGnm-9vff9Wi-FWmdrPkuuVtz4SSzV3AYQjKffG2W6bvghjYaQdJxbRLrqAljGh-Vx9UXzNnR4CUpM5qZ6xLmB2l1hBfk-8IDjo4a_-i7DEo9hdrBwBokulzyzcTVoXuQ_xvHxaKJ6NmOmzvLjrVYsJwIWPTp2pS7z-EILwHOpLTqMCteoyqeOCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت جنگنده های سنگین امشب بر فراز بغداد پایتخت عراق مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/119401" target="_blank">📅 01:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZOqCf_DjI6cR_vj4eNIZ5HqPX8vbA13pT43Qik4SvTvbngwbZEIY-awESxF6U0phHrIj2kRwA191yy4HGJJ2PShBOXgJWWXXSTCBXiXMrp5TE7JjEh02FieQuX9GlfKgap9qHSIB_8vabMDFYUl-AG7Qg4qMBruS3EemaAeVDMfc6erXzFc7KpXfpNobqfybtXeTUAQ5TceLTVhHmVc_TdS9nI3BZqwbCjMEMn8JF8liT8RXkWgx39CIYWvmLLpVr0Ec36ws_i7oqVqQEAAD2qmiCAV_Ecwyigwbp9hYneB1-vr0ar6xqcg_Woq2-nmZGQihgaCkjX5rg8HzEpHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیر استارمر: استعفا نمیدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/119400" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وال استریت ژورنال:
در پی حمله امارات به لاوان ایران پس از اعلام آتش بس ترامپ و تهران، ایران با حملات موشکی و پهپادی به امارات و کویت پاسخ داد.
🔴
ایالات متحده از این حملات امارات ناراحت نشده و به‌طور خصوصی از مشارکت امارات و دیگر کشورهای حوزه خلیج فارس که مایل به پیوستن به نبرد هستند، استقبال کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/119399" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDUNRANTTFwqHa2J-H-uppy5qzSFPu9ftLHb5-8ZJcHExBx-Pdvc42lTp2RscuQ1-QMopIIL_ue6CzC6m8bDgjn4R91hWoG_76TUDKVktXrZa6fZP1Sk4nE2Ipg8lCIE_aWvyiDj1plTakVrLELf_n4EWQDkRlunY5StE2pEwDeoIrSbZ4mTDw4w1yj0xcxCtXM1xNaEvkQsU-iwCvuPXfqADAzb8va2QaVGtmUTnoZ1YDcht856jlgDD6vZ6hxqO1CJZH2zhT6OU6xwJSDJTGPhfj5HOTGiA5gUNn-Hj4s7agbkZMaJLWQF3W8Uat3tREJ0_mcku9h4Me5YIHPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیخ منصور، معاون رئیس امارات: ایرانی ها در حد امارات متحده عربی نیستند و بهتر است اراده ما را محک نزنند زیرا ما خود آتش هستیم
🔴
آنها باید جزایر ما را پس دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/119398" target="_blank">📅 00:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258fb92ec4.mp4?token=OfzlE-CHKopRYSxUK9pf__0SLdahnoh2dkJ3H8m9_2x8r6a5JWlGZ5gpHigzYO7nbfapmnw4O_g2C7hVS3dUwsW4rij3JydkowkIj4-dJmZ4Yj0vTXfrLOgneG_b_VAdN_AnzI6etCN7-Sh1ofk8_tTH9Zskk7IcrBqZnD1OLzLQ5BYq4CUxjBhI1f1wBj-Cv11llPfCwdcXbfi-DlvAVp1aNZejCAFldto2VRQ6rxcfAu3JssowJkOslZJ_87DzDygFzETY8cxxIGR5hmeP2kFR2htW0ZBnwn8uAEwdOV4gz_Gtl7B6gF6qe9IqW0e3VxJTVaKNZuYeqUpDJI6l0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258fb92ec4.mp4?token=OfzlE-CHKopRYSxUK9pf__0SLdahnoh2dkJ3H8m9_2x8r6a5JWlGZ5gpHigzYO7nbfapmnw4O_g2C7hVS3dUwsW4rij3JydkowkIj4-dJmZ4Yj0vTXfrLOgneG_b_VAdN_AnzI6etCN7-Sh1ofk8_tTH9Zskk7IcrBqZnD1OLzLQ5BYq4CUxjBhI1f1wBj-Cv11llPfCwdcXbfi-DlvAVp1aNZejCAFldto2VRQ6rxcfAu3JssowJkOslZJ_87DzDygFzETY8cxxIGR5hmeP2kFR2htW0ZBnwn8uAEwdOV4gz_Gtl7B6gF6qe9IqW0e3VxJTVaKNZuYeqUpDJI6l0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی در صداوسیما:
امام علی شوهر زنی را کشت اما چون مهربان بود با زن بیوه دوست شد با او به خونه‌‌اش رفت، بعد شام هم با بچه‌های زن بیوه بازی کرد هم با خود زن بیوه
🔴
پ.ن: سوال اینجاست که این روحانی چطور از تمام جزئیات هم خبر دارد؟ مشخص است فقط دروغ میگوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/119397" target="_blank">📅 00:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دبیرکل سازمان ملل: جنگ باید تموم بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/119396" target="_blank">📅 00:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc1e86de1.mp4?token=pQqeql8uWSC3F8xRS4qfNG5qwEuf6Zgho3EwW2BwbHOveZSCibj168uBpRR9Pto-yJYQWe8_3mdA2-OodkX42J8gP6tIB5WdyYvHC1GJrGNQrxBfxTZHRIluKIYAVLyFFMVihgDUJVk9FEH7jTh-ntBiHeDygmRzd4HVsaNgOLCOIq53B4xR76r82tovnLkyZqwMY_mr2ioDkD8k8DmA_jfPfI6L7XEGvIvlu4yD2Rbd9dSddK37tfXVMqRVaTrXuKLg7pVWaEDAgsUqHiOVwH3FRFI9rV-ZItc0Q5ZENohZI-2mXLkfK9sB3ahBPuljPsmWPSYfGqSlC-7f-Myfjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc1e86de1.mp4?token=pQqeql8uWSC3F8xRS4qfNG5qwEuf6Zgho3EwW2BwbHOveZSCibj168uBpRR9Pto-yJYQWe8_3mdA2-OodkX42J8gP6tIB5WdyYvHC1GJrGNQrxBfxTZHRIluKIYAVLyFFMVihgDUJVk9FEH7jTh-ntBiHeDygmRzd4HVsaNgOLCOIq53B4xR76r82tovnLkyZqwMY_mr2ioDkD8k8DmA_jfPfI6L7XEGvIvlu4yD2Rbd9dSddK37tfXVMqRVaTrXuKLg7pVWaEDAgsUqHiOVwH3FRFI9rV-ZItc0Q5ZENohZI-2mXLkfK9sB3ahBPuljPsmWPSYfGqSlC-7f-Myfjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهران در روزهای آتش بس
البته تهران پُرو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/119394" target="_blank">📅 00:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0qp0HpS8rVoLRTyp5JF9Y7ZD7I9hqbcAKTn5hxZ5ulY_TS4cyZOMikNs9s5u0b9d0eCaHYy8XCyLp8uEb1IFQDVCCy-tcPcX1bPfEemcnHpXwfvOJ13aZrOWB2fGg6y-30RkX-QoX4KVCC4wvBKBPUj89x7uQ12GGgtzJUUAropU3hXSYzArRf1TSryi4-jUR5lZqq3de8sTYVKI3goBy17QNP5L6Fhvv_2aehPl0qxEpvOJR-41LxiUD7ImePACPJDzxPyhCenq-YXVvzAIukuco3_HY22Ws78mgEPG_86wTKtiNllgZMlbuR_0vRGxkTT6A0qa1FLwnekSXysbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
راه دیگری جز پذیرش حقوق مردم ایران که در پیشنهاد ۱۴ بندی آمده است، وجود ندارد.
🔴
هر رویکرد دیگری کاملاً بی‌نتیجه و شکست‌ پشت شکست خواهد بود.
🔴
هرچه بیشتر تعلل کنند، مالیات‌دهندگان آمریکایی هزینه بیشتری از جیب خود خواهند پرداخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/119392" target="_blank">📅 00:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سایت خبری اسرائیلی والا به نقل از منابع: واشنگتن یک هفته پیشدر آستانه تصمیم گیری برای از سرگیری حملات به ایران بود
🔴
افراد نزدیک به ترامپ هفته گذشته در آخرین لحظه او را متقاعد کردند که تصمیم به بازگشت به جنگ را متوقف کند.
🔴
اسرائیل ارزیابی می‌کند که سید مجتبی خامنه‌ای همچنان مانع هرگونه پیشرفتی در مذاکرات می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/119391" target="_blank">📅 00:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119390">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوووووووووووری/ ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/119390" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119389">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
2 مقام ارشد آمریکایی به فاکس نیوز:
ترامپ به از سرگیری جنگ با ایران متمایل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/119389" target="_blank">📅 23:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119388">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgkxiC3Smjc-HfLrLgOCZ1mlhcuHe_u_pyXA_SVkQsBY3iJNQSINPh5_Po5nfxgK2R4PIqhnSNeRkYWUn5i-o4UVco6LUxqhbT24_m2pMUk6HZQ3VCqhgXAcvmkfNj8_XzsT732V-KqdyqyGkr6-4JSq5WttvBIna2eyvnelQBv3kaBZ6B-fc3v4_qtOBbP3jJzE4tlom-Ql3SmJU7Cf8UxSk38yQmI6swjiakmX8YcKfiyZxDr0pstKkVIlEUmzpbI3n3YUNuE2YRrrXbo1SPYzpNa19zbXd1ooaWY8-_Wi1Pt3zXLT2tkzM2XtBPlUwDco_OVVlp-5Zygxy9W4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۴.۲۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/119388" target="_blank">📅 23:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مدیرعامل آرامکو: اگر تنگهٔ هرمز همین امروز هم باز شود، بازگشت تعادل به بازار نفت ماه‌ها زمان خواهد برد
🔴
اما اگر بازگشایی تنگه چند هفتهٔ دیگر به تعویق بیفتد، عادی‌سازی شرایط تا سال ۲۰۲۷ طول خواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/119387" target="_blank">📅 23:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119386">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وال استریت ژورنال، با استناد به منابع:
امارات متحده عربی حملات نظامی علیه ایران انجام داده است، از جمله حمله به یک پالایشگاه در جزیره لاوان ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/119386" target="_blank">📅 23:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فرماندهی عملیات مشترک عراق تأیید کرد که نیروهایش در ماه مارس با «واحدهای ناشناس بدون مجوز» که توسط هواپیما پشتیبانی می‌شدند در بیابان کربلا درگیر شدند، در حالی که تأکید کرد در حال حاضر هیچ نیروی غیرمجاز یا پایگاهی در خاک عراق وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/119385" target="_blank">📅 23:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رئیس‌جمهور ترامپ تمایل دارد دستور ازسرگیری درگیری با ایران را صادر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/119384" target="_blank">📅 23:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کارکنان یک بیمارستان در هلند پس از اشتباهات رویه‌ای مرتبط با یک بیمار مبتلا به هانتاویروس، ایزوله شده‌اند، به گفته خبرگزاری AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/119383" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c3e0d408.mp4?token=Cn80jLHDs8SGgTk6gZ6MjfveE3cFb7G_QTUpGmz7I_cHfpNKzzYEmZsUyQZ6Vgc3o-LY5VX6ffGtyGDM0qHBO_BJGld_b6cMWIUMCOliBSt76gMYtWWEK6hWzXEN05oHBsV5QMaC5xNUaDfUCha4DKQYFxh-_665OhnxjvH6WCnbu6uQMeDD-Z9KazRGyxxo-CLQ5Wckv1WgbcV-IBv4W0tAiOitv1hx1Nim7koGdTJj18d_f7_HJndZ5IUx8L0g-GV4YXN_pliZQVY_IxtJ_EOvsMiGsW8tQ1ehOrOE3kvjawCjGPLIDBk6IozW8aNbuJxtSfpQCKuNrQn-4YeIX01FfffrvE_x5p1LZNlpQFEppmoH_pcnUuxOdegmGz3szkH0dQwGmNyyoaT8V37NlBQQDpbLLx0YYpOz9JTh8R4jyMZB7q1Gf8tp6wQ3wPfy30yooj74hTLn3mbCYHRr9Ym2iXhkPQdMwe986o2Y-o0ql3219424HPyfGHPNaFRsngH6zXm12aNCrKUCPeyS-os69FZxFcs99YUR1WUbKZdsQOWHWCNc6At7qA88k0j-2asKwRAvbJR-VsEjv-ImIjMAVbfhANfoz0P2PuVhVDL0e1WsmFNLce5Woe_9r_0dTfth3A1MmkiKBFnXQAaDtU0mYGf4OLmgi2wl0z7w1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c3e0d408.mp4?token=Cn80jLHDs8SGgTk6gZ6MjfveE3cFb7G_QTUpGmz7I_cHfpNKzzYEmZsUyQZ6Vgc3o-LY5VX6ffGtyGDM0qHBO_BJGld_b6cMWIUMCOliBSt76gMYtWWEK6hWzXEN05oHBsV5QMaC5xNUaDfUCha4DKQYFxh-_665OhnxjvH6WCnbu6uQMeDD-Z9KazRGyxxo-CLQ5Wckv1WgbcV-IBv4W0tAiOitv1hx1Nim7koGdTJj18d_f7_HJndZ5IUx8L0g-GV4YXN_pliZQVY_IxtJ_EOvsMiGsW8tQ1ehOrOE3kvjawCjGPLIDBk6IozW8aNbuJxtSfpQCKuNrQn-4YeIX01FfffrvE_x5p1LZNlpQFEppmoH_pcnUuxOdegmGz3szkH0dQwGmNyyoaT8V37NlBQQDpbLLx0YYpOz9JTh8R4jyMZB7q1Gf8tp6wQ3wPfy30yooj74hTLn3mbCYHRr9Ym2iXhkPQdMwe986o2Y-o0ql3219424HPyfGHPNaFRsngH6zXm12aNCrKUCPeyS-os69FZxFcs99YUR1WUbKZdsQOWHWCNc6At7qA88k0j-2asKwRAvbJR-VsEjv-ImIjMAVbfhANfoz0P2PuVhVDL0e1WsmFNLce5Woe_9r_0dTfth3A1MmkiKBFnXQAaDtU0mYGf4OLmgi2wl0z7w1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ذوالنور عضو کمیسیون قضایی و حقوقی مجلس: هر شناوری که بخواهد از تنگه هرمز عبور کند را می‌توانیم از سمنان ،تهران و مشهد بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/119382" target="_blank">📅 23:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کالاس: اروپا آماده انتقال تجربه مذاکرات هسته‌ای با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/119381" target="_blank">📅 23:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWByR4eGFsz-rscFF-zjDVtPoUiy81R244f4OGCBy4-cDIrBeVbeLJWEt7JnLclCTDYgdjwSzSK50a6gspECc9d1XSnA5UHyQPE9R3YxOTgzEYTaFUhOITeAucguR-4nzwHVNLAblFTISfqkVQ7OVUa6jDfhocSlbXFgkethi-9-XooPfRKshCs8lVsBBseFh54DL5mkSFfuosMbK4eoPgd3OkjKeZUQNlZZggjK_0jTSJYNwhNpC7KDPnB1QoqgIH78TK7Rtd0CCturT_yoP0HjguOafk3XSoPcgz8sm5jU0OzhZ8BbqVieNIchbMPMY3yaS4UZ_EtEeADtf6l6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afGAqxKRwCyiER8UjWxBuew2H11JLK9xgR2HGTCZ6R7WusicT896q0RZWVEKe_LRwGWRsppWALnU_rBJoXJ2K-l2XAomX68ABAR2JO0HqFA2yDuZQSARpguos0DNeD_CRni9ZdYQGaFwd1MzEMJpcR1ZI_tBT3UVaDzeJZscyOVPlGQkT3wqD2bk6YWYe_roBW9qSi0LYI9KFvN2SKyum9kjxd9WfpIVgnwxBUuqbB7QcK20nWdo14ZZ8KZjNaorA1QBgQyMZ2j4CrYNG-D0UL1yYucFxwvhS7BRwT3ulIM5CG0Ny7JY8i8_pVdWfPDIKqQ76dYuMzhxAzccfW8_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGI89pOdQfwoca08F9vBfIKAB7-whsycDa73Is80n_PnYpdo5F-v4_VW_RuqwSQdW0pgO8n5IGbKhbBUFnGV9TbQDhJWMAT3LUWmhHl8nMJgZDsH2W-nBYVwgHUtwx9OpndwBgZ8G6kSIXyJir5ttRbe_kSH8E3ucO5WnqD8tDizkLx3DeC7E5Zb9qcjueHSOrJmeEFx3Z5xX35S3TlJC1uFZWPau5VFQAED_2MnQtgcJkYV6M4WEdEhEBk4MvsCdKOqGDMSyzz8NZU-am1aZ5tQMfMNYXEJd7-5cpPX8qT5_RT7dn8y7SKmjx0VDn13BH6DNVlmTbxDa9Z8jyPdqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fab5e608.mp4?token=tsNpYb_H0Sbv63ORmqY6U4Z6zabcd7pBUR2bBR8pil27eZ5xXAZHsCZbY4LvGKl3m2-wXY1uaT3WEmvQax1w5X9B8qUcuDF2nam0IuOUQAM7uvY3sGdUqtmfXqIjRQRA6Bw64-Ry2JCqFw5WxWE0fBcUeUDdmSiIK69BSZmfZOW63I-ds1govMm0EVH1ToUWI__9yQEy_q5wfGHnaIUYXptNSOf7Tr1a8GnCNvCEgDODFWoOLQm-ZwjVdMh4_TPwbkltWOzyWjE_ptnN1yTwK2x-3h_NV1z8d_TJz27T5jUfWY1gYz6A247ByBj-qwykw3oN4u8dfPcqKNfH7Klt9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fab5e608.mp4?token=tsNpYb_H0Sbv63ORmqY6U4Z6zabcd7pBUR2bBR8pil27eZ5xXAZHsCZbY4LvGKl3m2-wXY1uaT3WEmvQax1w5X9B8qUcuDF2nam0IuOUQAM7uvY3sGdUqtmfXqIjRQRA6Bw64-Ry2JCqFw5WxWE0fBcUeUDdmSiIK69BSZmfZOW63I-ds1govMm0EVH1ToUWI__9yQEy_q5wfGHnaIUYXptNSOf7Tr1a8GnCNvCEgDODFWoOLQm-ZwjVdMh4_TPwbkltWOzyWjE_ptnN1yTwK2x-3h_NV1z8d_TJz27T5jUfWY1gYz6A247ByBj-qwykw3oN4u8dfPcqKNfH7Klt9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از زیردریایی موشک بالستیک کلاس اوهایو USS Alaska (SSBN-732) که دیروز به جبل الطارق رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/119377" target="_blank">📅 23:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دیدار معاون وزیر خارجه نروژ و سفیر فرانسه با غریب‌آبادی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/119376" target="_blank">📅 23:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اسکای نیوز:اکنون ۶۰ نماینده حزب کارگر خواستار کناره‌گیری کیر استارمر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/119375" target="_blank">📅 23:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b7a78836.mp4?token=k9w7tedSV5OeVZPj9xSOed6vNPSOu-IJjGRyFiwLOKk0AUTpEF6251hziUYMYN-zRyXYSjOXjGTXenVHy_CID4gy_pDCBaw2oZuYdjYSnv6Mpe7Yl1pSQydryGvYnQiQzQpk1egicetHYQRaCoIQMjfb6N7HhuUmumuqkZGRvxfmoTjB0OlTsmF6ULdzCLEY5zW7ystmsKAF_herK5jsHBVLDxuRXi2esrLSWTfPuG3WJkHgfRJbqvRVeC4eGPst53waSqnLdSuPuZ3ItWsk5k8QURBhfhG2vYGPqPfqLT23WPcOzJfS9KicS7L40clQcHOYmayMl4dkB5w81Ffx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b7a78836.mp4?token=k9w7tedSV5OeVZPj9xSOed6vNPSOu-IJjGRyFiwLOKk0AUTpEF6251hziUYMYN-zRyXYSjOXjGTXenVHy_CID4gy_pDCBaw2oZuYdjYSnv6Mpe7Yl1pSQydryGvYnQiQzQpk1egicetHYQRaCoIQMjfb6N7HhuUmumuqkZGRvxfmoTjB0OlTsmF6ULdzCLEY5zW7ystmsKAF_herK5jsHBVLDxuRXi2esrLSWTfPuG3WJkHgfRJbqvRVeC4eGPst53waSqnLdSuPuZ3ItWsk5k8QURBhfhG2vYGPqPfqLT23WPcOzJfS9KicS7L40clQcHOYmayMl4dkB5w81Ffx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
شاه چارلز امسال رفت استیت ویزیت از آمریکا! چنین استقبالی از ایشون شد؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119374" target="_blank">📅 23:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119373">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا تحریم های جدیدی علیه افراد مرتبط با ایران اعمال کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/119373" target="_blank">📅 23:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ای بی نیوز مطرح کرد: پیت هگست، وزیر دفاع آمریکا گفت پنتاگون بررسی خواهد کرد که آیا سناتور مارک کلی، زمانی که این دموکرات آریزونایی نگرانی خود را درباره فشاری که جنگ با ایران بر انبارهای تسلیحات آمریکا وارد کرده، مطرح کرد، اطلاعات طبقه‌بندی‌شده را به طور نامناسب افشا کرده است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/119372" target="_blank">📅 22:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119371">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت بهداشت: هانتاویروس جدید نیست و در گذشته هم وجود داشته است
🔴
انتقال انسان به انسان هانتاویروس بسیار نادر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/119371" target="_blank">📅 22:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شلیک موشک به سمت جنوب اسرائیل شناسایی شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/119370" target="_blank">📅 22:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/alonews/119369" target="_blank">📅 22:51 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
