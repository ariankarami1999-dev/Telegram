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
<img src="https://cdn4.telesco.pe/file/SCNDJvpLe9ryw6ZYHRC0G8-arji2s-I_48XobwpVxRZzDzjW8RmIIHtsYH1CozwxvER-GNVtP5C9uUO4JUBoomHneXtD7ilh-UTw0nxwpXnav-YBn7xTtwxzCrbLAF8n_8FfDMhjrz7XmGGosLG8Z41KV4iEwIEhOd7zpb7SVlUxYZyCKJmhq2AhzW2go2Wc0Bhr1RieNNz24xL60wrxl8tjiq9BITvcpyJQQAjBsou88LF0ktPzN9k15lBtOxfCYNW65W7KqNSfI2m9F4j307IsOuId6p7r7celpO3Q1NPzbqrp6816p3jzWKUcR6aRkoMF8Opk_q7hdEhIWxeoqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 08:44:01</div>
<hr>

<div class="tg-post" id="msg-135538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
به‌دلیل شرایط خاص استان هرمزگان در وضعیت فعلی، وزیر نیرو دستورات لازم برای خروج این استان از برنامۀ خاموشی‌های برق را صادر کرد.
🔴
بررسی وضعیت سایر استان‌های جنوبی دارای شرایط مشابه نیز در دستور کار قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/135538" target="_blank">📅 08:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e002a969.mp4?token=knPi41w6n1hRR7eAlLwPCoRt_2yvEDLA9eoJOTvtGbCX3bPvGc_3aI_un-vAyw76RPivj7yWw6I1C2ZlU_cRV60oS7cn0AzOrCbqvkcgAaaUhOouJEi93-I9ks7BUVQL_HX1_m4x5xmCO0KO9RJTTb1hjIYGX5YpYEGgSJp3DII4pWYbXZfGyPgARhS_z3hGdd3eUr8JRIuQWn0qLg2Oo5NoFc7Ze1DQQkLS-HigdANMWR3C7JTgl6cPhj4Q1mzSwpB2UN2gOl0pIaewZnjeSsPfmnG1ERjOglWsPAwpCZeon0okB4NoZAvYUlb1wLz8v7FoAexO27BHk4YoYJIfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e002a969.mp4?token=knPi41w6n1hRR7eAlLwPCoRt_2yvEDLA9eoJOTvtGbCX3bPvGc_3aI_un-vAyw76RPivj7yWw6I1C2ZlU_cRV60oS7cn0AzOrCbqvkcgAaaUhOouJEi93-I9ks7BUVQL_HX1_m4x5xmCO0KO9RJTTb1hjIYGX5YpYEGgSJp3DII4pWYbXZfGyPgARhS_z3hGdd3eUr8JRIuQWn0qLg2Oo5NoFc7Ze1DQQkLS-HigdANMWR3C7JTgl6cPhj4Q1mzSwpB2UN2gOl0pIaewZnjeSsPfmnG1ERjOglWsPAwpCZeon0okB4NoZAvYUlb1wLz8v7FoAexO27BHk4YoYJIfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی سنتکام از دور جدید حملات خود به ایران
🔴
تجهیزات مهندسی برای باز کردن در یک سایت موشکی هدف قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/135537" target="_blank">📅 08:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnbN9uTF4GFBof7MjQeJ__V9BtC-xYUzm8UdG4mJHnh1WbatsySA1MMXroWQsvvyieTwDM7uzB5pftr94yUS7gK_oaAI2Fqxz3vH4OgHS84b7N9wzDlXzirfXQQNm1wQKNHqSbgktxjdvDuwaeWA4Po_FPOsDqEkk3ThvtB2VovHparf4JWNPI0vkn_LtMEjGiRWAqwq66rNYfaSfch2GOs1OJF4u8bbaBjQ76ah4AgZlRQT5ZZobDcppX1eU2Xi-UhBhZB7ePSOgP7sYT9MC5Cbtv98lCk5LSVLCxDWyfKLSF4fiUOopnMFpXLzMUNZtIK_PIAbf6cxa1BlsbSJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده آمریکا یک "هشدار جهانی" صادر کرد و هشدار داد که "گروه‌هایی که از ایران حمایت می‌کنند، ممکن است به سایر منافع آمریکا در خارج از کشور یا مکان‌هایی که با ایالات متحده و/یا آمریکایی‌ها در سراسر جهان مرتبط هستند، حمله کنند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/135536" target="_blank">📅 08:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سایت موشکی حاجی آباد در هرمزگان مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/135535" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/135534" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش انفجار در چهارمحال و بختیاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/135533" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHr04n9zF_xJLz0mY-H5Z7s3_RnOL54pRpdqr4chiiCw8N7sNcrqnNhwJ0YDoqHamibnm2qpCUBS0vY6AZz0j4I-vKFdORoM6N8sG4ccFYsWR2zTL21IeHE2ub2rf0TpsmNVwUQ7YgOWZoE6D3gtUlyMNDFKFn1A_S5-sztnyijUN2zF3svCDRGrID8UlsFFTZDNOsyI-6wVnX873rHc-TB00izzjpIeDbedAI2PeibHkrSFAD_Vb8SGCUK-ufLRQdiNxqdepuATwRCvYLCHoWa5Zr59Io55PzYbaYOrIpu-J8vyZjZcTqXH6vWI_fa9TsjqnjqhBub_dqFHWyz4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پایان بازی
🇫🇷
فرانسه
😃
🆚
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس به نقام سوم رسید
@AloSport</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/135532" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/135531" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سنتكام:
به سرعت نیروهای سپاه را که دیشب حملاتی علیه نیروهای خدماتی آمریکایی در اردن انجام دادند مجازات خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/135530" target="_blank">📅 02:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135528">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
۲ انفجار شدید در بهبهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/135528" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135527">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/135527" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135526">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نمیدونی طلا یا دلار بخری؟/
اینجارو بخون
تحلیل قبلیش همه سود کردن</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/135526" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شنیده‌شدن صدای دو انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/135525" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انفجار در بلد اراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/135524" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=XHJ8NHtyxLVXa4JqnmyZF9A1XR88ohc2OIF16NTu9XWovLZQcEpUN_OACDxXSMflm7flAU5jZvL5-DO_iRq5ptO_Uun0GPHaae9k5foQhiwYsRa-cGCc5b4YN6tdRbPxJLPwRKOchHFQV_V8W9W-hw-KFwmmx3I8T7FN3l8n7AGHCmEiWrFWs3nKcXK7TW0O4Ru5wsIs-PYW8VN0cfB4CxSV2dePC9tEmtf5WaR3irxW_1CTq24oVUCGIvvI6-e4fu2egnSmLD-xVJMCqJ23BgOcVCQEbfWbbejMHR1L-4PxNd8vEvJA_Sp6Lo5pRaKc4erWd1AyF5o2N1QV1dSxCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=XHJ8NHtyxLVXa4JqnmyZF9A1XR88ohc2OIF16NTu9XWovLZQcEpUN_OACDxXSMflm7flAU5jZvL5-DO_iRq5ptO_Uun0GPHaae9k5foQhiwYsRa-cGCc5b4YN6tdRbPxJLPwRKOchHFQV_V8W9W-hw-KFwmmx3I8T7FN3l8n7AGHCmEiWrFWs3nKcXK7TW0O4Ru5wsIs-PYW8VN0cfB4CxSV2dePC9tEmtf5WaR3irxW_1CTq24oVUCGIvvI6-e4fu2egnSmLD-xVJMCqJ23BgOcVCQEbfWbbejMHR1L-4PxNd8vEvJA_Sp6Lo5pRaKc4erWd1AyF5o2N1QV1dSxCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فووووووووری/چند جنگنده جمهوری اسلامی به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/135523" target="_blank">📅 02:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فووووووووری/چند جنگنده جمهوری اسلامی به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/135522" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
هم اکنون شدت حملات به تمام خط ساحلی جنوب رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135521" target="_blank">📅 02:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
صدای جنگنده در کیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/135520" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/135519" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/135518" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPBPx63dDISE0Ua20w3ci1NUaFZ3kEVPfB4S6Sd93usxRyNAG9ZYTloED9z9yzeqj-2EnIyO6EU6P35BJOvRDjHnwFaTDLf6P-26Dvya-SgnFPuMHYQKaGQiJDeA9NbYNqhM9T5hy1QB7nSLWvRHtqfb2P6o_AJaVmtVTEY-0yf-GAhnId2R2vLipZSsSegzQM_xLPliF3XNbV24YU-L7nFlJBfdbPqLHCWY9Ddc7pfqTxgehXXQixQTc6FrEgOLzRf4jfaKm0LRxi3F81RLpXcN8VXz95DntlPUuhQPnsaDynwFjhpmQ9H8fOnCuksaeAXH792OmMu5yDlFUsExAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام از آغاز حملات علیه ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/135517" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb7277feb.mp4?token=KSmkG5UxgEI4PgteI2frGssJwvAeW8KXC-1uXVr0aM2Yp611gHk-i7aB1QzMtZsZktoAuH52sI-t-3ydm8rfSrdk4EdCfJ8yeqKcV-IIg_9MzVqoUcaMYPWMwEn3uJ6MxJykM9nb4veRBt6XhM5O_7U8y7F13lb14QFifYNmu5zIsn275kwh5z2jbVIoGPWRsBiy3alBt2voprbxAVQ3GrY671isSdtMpIuLJgTydyH2W6Hc8eGZexe56ptbONZdLi80eOcUHhFMyCoTNTQucttcR4X_5HGWFeXMeaGBLzVlSe7LCBByU-oA1f27OSvQD8JITdqlVxOeXP3OwGxhBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb7277feb.mp4?token=KSmkG5UxgEI4PgteI2frGssJwvAeW8KXC-1uXVr0aM2Yp611gHk-i7aB1QzMtZsZktoAuH52sI-t-3ydm8rfSrdk4EdCfJ8yeqKcV-IIg_9MzVqoUcaMYPWMwEn3uJ6MxJykM9nb4veRBt6XhM5O_7U8y7F13lb14QFifYNmu5zIsn275kwh5z2jbVIoGPWRsBiy3alBt2voprbxAVQ3GrY671isSdtMpIuLJgTydyH2W6Hc8eGZexe56ptbONZdLi80eOcUHhFMyCoTNTQucttcR4X_5HGWFeXMeaGBLzVlSe7LCBByU-oA1f27OSvQD8JITdqlVxOeXP3OwGxhBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند هوایی C-RAM در اربیل، کردستان عراق.
🔴
پهپادهای سپاه در حریم هوایی در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/135516" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
چت و ویسی که از بیرانوند منتشر شده تو دایرکت یه دختره حسابی داره........  ببینید این جانور چی هست که به اسطوره ایران توهین‌کرده
◀️
◀️
◀️
جهت مشاهده کلیک کنید  موقت هست و پاک میشه
🚫</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/135515" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/135514" target="_blank">📅 01:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کان نیوز: سطح آماده باش ارتش اسرائیل بسیار بالا رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/135513" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال:
جنگنده های F35 ارتش آمریکا از بریتانیا به سمت خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/135512" target="_blank">📅 01:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/135511" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری/ترامپ :
دیگه توافق با ایران هیچ اهمیتی برام نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/135510" target="_blank">📅 00:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ به نیوزنیشن در مورد کشته شدن سربازای آمریکایی:
این موضوع بسیار غم‌انگیز است، اتفاقی بسیار ناگوار. ما از اینکه شاهد این اتفاق باشیم، ناراحتیم. این [اقدام] در راستای خدمت به کشور ما بود."
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/135509" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqCSzNlIza8oth_iXKeM_znc40VU_aA2x1QnlRDgAbLzanqX7jK2UR12Zk2z6ul8I9hJI2iswRFz5tA7uUjN9qIj8LlY-jxc4dtKzv3LArYNtn51gjGuk0v7UIKvg1xrlLVyq3GGS4MoAUfAlC9WNjiQtkNkJlX8eCghkYjHzzib8Mr5Lb83fwYLgiL2kjCoHI3qHx6kSbJLrHm8pRIxebSoXjliXWwxHd-sOA4ziXMWyDZpa5bbTueqAJSp1B_4_vDpLgiEPgAjV2vCudMJ4QvT6bCuZow90VKi31sfcYfZCFmkpdxtjiMyOUltFodkZp5CeEzTORvOOT81rBzL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرچم شیر و‌ خورشید در بازی انگلیس و فرانسه و پخش زنده صداوسیما که از دست سانسورچی در رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/alonews/135508" target="_blank">📅 00:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
زلزله در بندرعباس
🔴
قدرت: 3.7ریشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/135507" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
چقدر آرومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/135506" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
تسنیم: انفجار تو چابهار صحت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/135505" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhmJtAkpJVJcn7BZrvj9ljxZtBpGPriTP8x2cZ7Oo8qtqZwaEoYWxpM1N1K6HsZIw4MkVoIHuDUtFEW1D7nJhCvERQqXhyCrWiwU8d5KXAxa-NN-i_ruxkt4R8pu7Xhg5pHpUSQdOBYD0L_xFz_xdEu3dRrmS9nZPpqcikbwMfVHdTO_MljfZX3YmFUb_y3KmZDZeOpkzdCdVZwThJhx9otBRHyezZhiI4BL-T1bryKJP4ySZMqm4O8yqOXBBn29BA0IN_hr6gbOT6S-_1A_UYDHzDsjdFm4dSPw3Dwhyis7YZ1_Q3Bkr8DTnm_k_AohMNHprSWZCNFeAdMb54jx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوررررررررری/کانال ۱۴ اسرائیل: بعد از تلفات سربازای آمریکایی، ترامپ دستور داده که سنتکام، دروازه‌های جهنم رو به روی ایران باز کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/alonews/135504" target="_blank">📅 00:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iyyPCEzBqD0h7q-gvtWXC0gstvXWBK1I_xId_NuWrdYMBzRqSQ8KxUTt8WcKcjlCuaBZtRm2esa4VhkNh4vu5aF8fS-amFk_9LUrOsFtL3tSlsflfIgNi7p54KWp4uqw16JC1QtySEpQe1L5kyho1DSy9oIIrPJfIB9x2g9YUuPy2wGv8uPRK5JISW2_soycyjXAweRReazh8g2Z0eG3brlUJs-vfD4yOEKWvB17FRmfIUgV-2pZh3lLABiMfbJUVi4shklqouxCB6CYBgh842hA2Eh99r1j0aTmEz2Px_lVNc6a57HRWYloaolzsYnCxo80ljYWFNVYoW8YA42wQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TOfjiRLQIkbPr6z3YiNGyjRdCutiLlXEwQEErymLKufJKli4LnuGFiizD5EAu-qvEkvv7xF8nBtVyqSi43smXIWLOKlRdMBDwnXLyJouU1VBs4gY254-Rsxgl2b0jaLMjFJilZ0S5fORGmeEl1dRC-geZLkfHY-cvPgOv7Ho3c1NO3o4tBRTr3QNo1yGgw06uWN848pph-uFIjpx6I-xkGbX6yPlBJQTuQZ7ng_qClsHgBqjD-YQT83xuHy0oMjT8Jx9s65DhcbqDFFo5YGfCfffdtjBaZobzJiyN33OqTaK50rtT00qx4M8I5RZZprvbd5VtXwTI8zN3_rJnH85Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/seplKVYobZJWnMdQCmDSoArahx1BSqGD9jeUq0s-tGnu0kum141vx5PG-bJkP92KB5CfmNok0TOr2asVikW_hzkPCrHxQSIg-VlIn7tZwQBatUYQZtONuVbAKPiNExeKxmXwlt7iKevXuDBMW2dPOeidlKO-yUObWenLrty1IynjBlf7fmQjixOYlekNd4QisxkEH1ArQcda9sSeD_1hrCdVSfLbGAs4ALgmW8od3uNeVh5Kkb8GHpXlAfLAQkEY4zvjeIRaZkzJuDJHeSXy3fb1Tm4RIxcv3Ogha_5BCcTDvnIJ8ZIha-O6fXL8A2SPf3R5uzonbOLrubho3H-dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E6eSCAA-NWGPDDMbZnWp8iFjG8H4wsm-XGOoF27zoCaFaGTAz4YvlgNaRhUhSMwDG5mNuaLo5Sfe5oedisWzWnjkMQIwVj1SBYygnd5UO7Hm2MGjX-x1VLISxSO9Dfa_C-Dv1Lkt_tsu2WOKMj8NUgoBYAKUy3pdGw6gWyN7d7DDPqNTibKtJQmnHCg3AnIbC2MInCCC6A7pYIkP3pNMMsOLJYqJkHEIiRPubLSW_X_yaj15cyMSmNw4iSBSBaNZ0ziUIr3e8teCqVyIrNn_4t_8zkgOIeZ7tBgbOKyYKClXQ2zyzPAzlq495RCKCxZ7ErVaxh2emC5yWVO_qMigpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور یک اردبیلی به عنوان مدل در برند dior
ملت هم ریختن کامنت گذاشتن و آبروریزی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/135500" target="_blank">📅 00:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: حمله ایران به اردن به تعدادی بالگرد آسیب رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/135499" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سی‌ان‌ان: دولت ترامپ توافق همکاری هسته‌ای با عربستان را تدوین کرد که امکان غنی‌سازی اورانیوم را می‌دهد
🔴
این توافق به عربستان اجازه می‌دهد برای برنامه هسته‌ای غیرنظامی خود اورانیوم غنی‌سازی کند. متن کامل شده اما هنوز توسط ترامپ امضا نشده و به کنگره ارسال نگردیده است.
🔴
موضوع بحث‌برانگیز این است که این توافق، عربستان را ملزم به پذیرش قوی‌ترین رژیم بازرسی آژانس بین‌المللی انرژی اتمی (پروتکل الحاقی) نمی‌کند و در عوض بر یک توافق پادمانی جداگانه بین آمریکا و عربستان تکیه دارد. منتقدان هشدار می‌دهند این مسئله می‌تواند مسیر دستیابی عربستان به توانایی ساخت سلاح هسته‌ای در آینده را آسان‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/135498" target="_blank">📅 00:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فرمانداری خارک: زندگی عادی در خارک در جریان است و هیچ دستوری هم برای تخلیه صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/135497" target="_blank">📅 23:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPYsWvcCbYs-WAQn4S8MhPRdnXKGD4jH67YG__Tja6AwVCAIC1Ps8Yq8wyw7RNIIPVw5MOP88xlgF4v15y-eN0W1jRIiFKF7VsnklYn3h8rKldrc6ZQ3lSZAcNOSpbWt7ad_RHxEPimdskK0At1OOoIxrp-9pUD4mmyl-UnYAalrZ4y4uYsTHMU0NKu3-s1BYXBaKpXgiiDXXhgZPEyDQjH4CdmPG30GNIZCEKZ3YAJIe1HY1rs00ZIsfVcVzC1Mh_2NAhr4EP3xeRL7sPstJQSWbWSMZs9Q-SBUYKm-0BvWSYz6pVeYFMgdAU4WlY7q5N8_onxFvBt-lrYG2JKpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : به اجرای سختگیرانه محاصره دریایی علیه جمهوری اسلامی ایران ادامه میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/135496" target="_blank">📅 23:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یک مقام ارشد شرکت انرژی آمریکایی به نام HKN به شبکه خبری روداو اعلام کرد که این شرکت به دلیل تنش‌های بین ایالات متحده و ایران، تمام فعالیت‌های خود را در عراق و منطقه کردستان متوقف خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/135495" target="_blank">📅 23:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2f6992f6.mp4?token=VvzruHsgpEfj191jHOSW0_wpUoUIJK-wVtp0tR7w09rxKRuOHTctCip0awlXmDfWSKdcbaBj3BrkvDL3sVkdiTdL_hnCsu_YohQ5jdwVmI9oay2yppZ7z5cct8th0R7mE_OVFrDULsrM8YGTekASUdCUAhaVjfZjqPvKcV6uCdmtUWb3NY4_tKljOB3zYxnH-uMh-r1o-QZnyd6dmQoQimn8AyUlUgrjHG4MRwv9mO_BijQbWSnTOAGUVh9YFNuflEAxLUaWbr280g2gZi7EEPR_jwlqwtCMRfe7XwYPPKc2RDneCj7BvcmdLSTpcMJuwHHIHxTiCHgqNg5lp4cZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2f6992f6.mp4?token=VvzruHsgpEfj191jHOSW0_wpUoUIJK-wVtp0tR7w09rxKRuOHTctCip0awlXmDfWSKdcbaBj3BrkvDL3sVkdiTdL_hnCsu_YohQ5jdwVmI9oay2yppZ7z5cct8th0R7mE_OVFrDULsrM8YGTekASUdCUAhaVjfZjqPvKcV6uCdmtUWb3NY4_tKljOB3zYxnH-uMh-r1o-QZnyd6dmQoQimn8AyUlUgrjHG4MRwv9mO_BijQbWSnTOAGUVh9YFNuflEAxLUaWbr280g2gZi7EEPR_jwlqwtCMRfe7XwYPPKc2RDneCj7BvcmdLSTpcMJuwHHIHxTiCHgqNg5lp4cZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز درباره کشته شدن سربازان:کاخ سفید اعلام کرده است که سکوت خواهد کرد، به این معنی که انتظار نداریم ترامپ امروز در هیچ رویداد عمومی حضور داشته باشد یا اظهار نظری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/135494" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
امارات: از طرف‌های درگیری می‌خواهیم به میز مذاکرات بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/135493" target="_blank">📅 23:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بیانیه مشترک کشورهای خلیج فارس و اروپا: ما از ایران می‌خواهیم که فوراً حملات و دخالت‌های خود در ناوبری را متوقف کند و تنگه هرمز را بدون هیچ قید و شرطی باز نگه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/135492" target="_blank">📅 23:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1beb607113.mp4?token=LkmwsHQuXXwfx7hgAQEzikiGbYTQVOEMeF6leuUlU8oHb5ZpvHYgMc6UUQCkUW6gs13U77vgl4E0-N-dpzSbsmErchCGTWNqRNy8ZFgKsvGr7b_LvIDS8FibYqFORQR4AZ2qk3sTRhiL_hoqYaA5v-vvtiLkt20IfrREfGmoQchnl2azujGXubFIPv2D5WtWvxu1oeWlQzSur3S06sYrQjj16EIdXUs_jZUOyREcGlFa7ocsegAoUBoKH9qp8mNjgRVPxt_7l8o6Sb-vG7mTkdo-K46vwHILlNH-Z51oCTLaHdyYikfIl5MF86-rwEJ_Yv5r_49r4-BehsCFE8I_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1beb607113.mp4?token=LkmwsHQuXXwfx7hgAQEzikiGbYTQVOEMeF6leuUlU8oHb5ZpvHYgMc6UUQCkUW6gs13U77vgl4E0-N-dpzSbsmErchCGTWNqRNy8ZFgKsvGr7b_LvIDS8FibYqFORQR4AZ2qk3sTRhiL_hoqYaA5v-vvtiLkt20IfrREfGmoQchnl2azujGXubFIPv2D5WtWvxu1oeWlQzSur3S06sYrQjj16EIdXUs_jZUOyREcGlFa7ocsegAoUBoKH9qp8mNjgRVPxt_7l8o6Sb-vG7mTkdo-K46vwHILlNH-Z51oCTLaHdyYikfIl5MF86-rwEJ_Yv5r_49r4-BehsCFE8I_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنیتا "خواننده اینستایی" رو گرفتن که بخاطر ویدیوهاش ۷۴ تا شلاق بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/135490" target="_blank">📅 23:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/135489" target="_blank">📅 23:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4uvkWSyDF2SNdvCcYSgJJtaHYCu9ZNn9gKHznF3Ig4sMANf1cyHYDEWiYrQKD3_uv4e3xSlGnvNE4yHyvcM2Rr88QfRUReHbrUnS86niUo13WAK5mHArcP2rRA1-UBZ0_WwPYdbVAKwv6Tyq7OaIw4i1esysnLHk3VKEq5KfFE_Fpny7j5N-NktP5isrr5yg2IaCFxlhhsGE2v9yO_CjyevYUlDQVivZCC9_uUxWlFmoGcuJKjmK2wf5SJQWU5vcP-Emg7MHMGplGilvoBATL39q1OvFXRXdSGMvQjJLLz_ndoZinvQrDQxvU7sdBUTpt6xBwskyynqtNVc61L1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار وزارت خارجه آمریکا : به همه شهروندان آمریکایی
🔴
مخصوصاً تو خاورمیانه، هشدار میدیم با احتیاط بیشتری رفت‌وآمد کنن؛
🔴
چون احتمال حمله به منافع و شهروندان آمریکا وجود داره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/135488" target="_blank">📅 23:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
عراقچی: روابط ایران و عراق نباید تحت تأثیر برخی اظهارات شخصی و غیر رسمی قرار گیرد.
🔴
ایران بر احترام متقابل، حسن همجواری و توسعه هرچه بیشتر مناسبات با دولت و ملت عراق تأکید دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/135487" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
چت و ویسی که از بیرانوند منتشر شده تو دایرکت یه دختره حسابی داره........  ببینید این جانور چی هست که به اسطوره ایران توهین‌کرده
◀️
◀️
◀️
جهت مشاهده کلیک کنید  موقت هست و پاک میشه
🚫</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/135486" target="_blank">📅 23:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwu7BP_J_mEstobV8kph1y_zgJLASQ-_uPLZNco2QWwvUJjPTus6KjoCnqxJtOtRcYggRSl588MBWNxawvSwVL_617-bzTzSJhzZ8wTbam9-nYfTbC4SQPwWhVe22sip-gUOnTUj_zFWEFN92fyUbe-QsBMzIacR-VyyD_Km6-qI6ZnXuvrj80d78zUCZk7KznVEi8h4IHRyEZAWisOKhDTjEKYdxm1859FZaIe0xhyjGiH9u-ncG6knbbHM0JGJXq6wBQbfjPZPBHnmoZrQSTN3KwLOhnhIsYfC-aKEVCQho8MlLjvWlaLQ2Tx0MMyJSbzGh0GBpRZ6-UuYyvN_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین بیش از 300 پهپاد به سمت روسیه شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/135485" target="_blank">📅 23:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/135484" target="_blank">📅 23:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6119426f.mp4?token=TzIybiTI5hdJ_s49a0PXqJ5mfCRAnSGyroJIR1lMzTZ7s9ziyJrm70ZaD56rv7Pw5Fy6H9bxtjsfFOF-4BPJsmP8vGpXI06h8M_V_KhVDaq8WXz8Hz7Qugm68tX-QkeumWZADXOo94IzCBLUUVegDJb-1OY5kHtX3QntnsvBrwOzEHV43qU4kvcnk8hSo61eyDYh8msTCPTvKQlHxeHDHdukv6P8-3SkXpt6_AmPymnP1V4kaD8nCHH8NQY1Usl1y_4NojeGN-Ebl-D97L1SG9nrjWVnVpK7guwwmu1OZrxIGbC-iacmc5oz0B5wCHRpqYpZARfwNM8NnMrdF_xVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6119426f.mp4?token=TzIybiTI5hdJ_s49a0PXqJ5mfCRAnSGyroJIR1lMzTZ7s9ziyJrm70ZaD56rv7Pw5Fy6H9bxtjsfFOF-4BPJsmP8vGpXI06h8M_V_KhVDaq8WXz8Hz7Qugm68tX-QkeumWZADXOo94IzCBLUUVegDJb-1OY5kHtX3QntnsvBrwOzEHV43qU4kvcnk8hSo61eyDYh8msTCPTvKQlHxeHDHdukv6P8-3SkXpt6_AmPymnP1V4kaD8nCHH8NQY1Usl1y_4NojeGN-Ebl-D97L1SG9nrjWVnVpK7guwwmu1OZrxIGbC-iacmc5oz0B5wCHRpqYpZARfwNM8NnMrdF_xVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متکی: طبق قوانین بین‌المللی هر کشوری که در جنگ علیه ما، امکانات در اختیار آمریکا قرار می‌دهد برای ما می‌تواند هدف مشروع باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/135483" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وال استریت ژورنال: مقامات آمریکایی می‌گویند توانایی ایران در هدف قرار دادن اهداف حساس، نگرانی‌هایی را در مورد دریافت کمک از چین یا روسیه برای هدف‌گیری این کشور ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/135482" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رهبر انصارالله یمن: اگر عربستان سعودی در حمله به کشور ما دست داشته باشد، تمام تأسیسات نفتی و حیاتی‌اش هدف موشک‌ها و پهپادهای ما خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/135481" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogdWWqRV6vkzuya71igIXHPfasUZNo34cCW2GZPCM0Gvy7LB6lkgeYAt5Pul3RFEN-U9zvc95FOodnPA7RnTuLyGhYx8PBxAlsugzBnU0IOVcIaVkygz-l8hwmIQEKFVpkVDvks5xO8J4N4hxVMqFqftCrrAGLyoDHSW-8FDv9Kq2dO8OdCsFsOgoTWySdllwqEpqGFy_QLNyl1iZd5OAAtfOXaVmd1sbbBFqGnVMNGh2qSYtyjeRug2k5KUrbkV_YyhnB6TfAXS9z0cP3dJpOmYgtcmvr9pOpLTFkDxnjkBq-cXaEMsPYDnfC5ewILVdqNaEy4wFirbm66V5BYVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر ارتباطات: خبر قطع اینترنت پس از جام جهانی با دستور قضایی هیچ سندیتی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/135480" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXGt2DSWl1U3hLmisfpY3k2yklux0jyahKJ9juNdSztSIt2IhWHb30kOVRMl7zc-2BkPN8OxD5sIKjKLfTyhYEgk1BfyiE7f9vj-qv8lmxAWRrPbtpJyeg66C4z0L85FoR07yY6fLfI9l_0gBniuiHKt89dNnZgjyF5OGWH57e_DbCnipZoWaMFqzayV6U24KhBDoAp8tZhlmUlNDfFkZ6dpAQahgAskSg6j1Fqikin2erVhFOzojqFmEM7Xglb6flccOH57B5SuaeW9-nodpMetpy8uqARinCQR7dfxSl-fG0y7AuQa3i7M3NGm2bwx1IqmU-tjLGFBtJFrJD2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت:
از مراکز نظامی هدف قرار گرفته فیلمبرداری کنید سریع میرید تو گونی و تا چندسال زندانی میشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/135479" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0d5215ce.mp4?token=cNAzuQqW-qFpn5nHvRqJWH-y2rvH8fxzenOx-4WbMYczYNoZ6ggtdwxovHE_7uNdp_tRGPPtAsN2ZAqyjSa3TRclSquHCd3MyNuKIc38QNXX_9dvoO7uftScVpAvV-CngLtRZ0R0FJfPraS1TWbTU5kwyITBiuue7io71n5BLRG3rTlUphwwZunJJdIChF-OBonr54qCfYZlL5c3F53FGQyFMbsgx_08K6jDC3VTvXo7lXVCs3sOgfAnM6AM09foE81kC-G_YEEhg1nCLN9eGyxO8t64Bz9H0emcYzunOkmWyMe5kd0wn325DwSXtdnTTHI-dOS0w4D2oVXoJGPmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0d5215ce.mp4?token=cNAzuQqW-qFpn5nHvRqJWH-y2rvH8fxzenOx-4WbMYczYNoZ6ggtdwxovHE_7uNdp_tRGPPtAsN2ZAqyjSa3TRclSquHCd3MyNuKIc38QNXX_9dvoO7uftScVpAvV-CngLtRZ0R0FJfPraS1TWbTU5kwyITBiuue7io71n5BLRG3rTlUphwwZunJJdIChF-OBonr54qCfYZlL5c3F53FGQyFMbsgx_08K6jDC3VTvXo7lXVCs3sOgfAnM6AM09foE81kC-G_YEEhg1nCLN9eGyxO8t64Bz9H0emcYzunOkmWyMe5kd0wn325DwSXtdnTTHI-dOS0w4D2oVXoJGPmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">-جناب شما جان فدا ثبت نام کردید؟
+بله چطور؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/135478" target="_blank">📅 23:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
ساده بگم، جمهوری اسلامی تابستون رو مجدد نمیبینه.
🔴
بزودی منتظر تغییرات خیلی بزرگ تو ساختار سیاسی ایران باشید.</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/135477" target="_blank">📅 23:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/135476" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
خبر فووووری/4000تفنگدار دیگه عازم خاورمیانه شدن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/135475" target="_blank">📅 23:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1574a01f69.mp4?token=JcHIQGM7n_b8oAQ2kymc_AhaILHsynXWPyNk0RjgJFcEMQnU_qJ0MDw4ynjulooP3cnKviSVSyo6tJCddOg6kx2BSL_-xoCXdtglc1oLTZfq1eeR4FnYq5UdxKcN_wIgFsBjSFQLXaVfZsSjT5M1yNPBcB8HuJ5pDZeD3LS3e9QNUO6btsMPBbYI7YQm7BSH71LMRd7EhONrgosBtkEdAP6zpoQEmnOrYAgsr3KLokACrNGZXls-l2_InxHemIWMokIXUZ8lbLBFzboFFTMWEXpNZ1et8eBXcwA4JUR6lsXU_gKwul8HLl2xDMuINraEbrigbtPF7BfdymNktHg5IIuBwBmswqGXtkkD_uH1L2MRTJQYmymvDqHu-5MtaaiB3MN4pKslbFfqUGsstlhygkuyrfJvlcKp99pHJ5zwx0O_bCOoH3WK-dcO7QifEvYpv55wiOvwE7fK3Q_bMh_vTpfZTXFD3Zz4xZOim4y2yoHAdvLos2twjCbcFgQrG6URca_mriKI-AjTAe5hXVzG6oUaQR5XRFcthRoLGt-vHl1CtzvV1EYZuIPKMOVAZWKF-Acw7aSza4V6hV19gBnvuB8HPL_dJyPrZVDLgNFYOmMWfPqflR8_Zv73FPcuADsMxLUNVcJiLkg9Pyv8eG9Yf78YwfoSgBp2-RUcyOTg_vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1574a01f69.mp4?token=JcHIQGM7n_b8oAQ2kymc_AhaILHsynXWPyNk0RjgJFcEMQnU_qJ0MDw4ynjulooP3cnKviSVSyo6tJCddOg6kx2BSL_-xoCXdtglc1oLTZfq1eeR4FnYq5UdxKcN_wIgFsBjSFQLXaVfZsSjT5M1yNPBcB8HuJ5pDZeD3LS3e9QNUO6btsMPBbYI7YQm7BSH71LMRd7EhONrgosBtkEdAP6zpoQEmnOrYAgsr3KLokACrNGZXls-l2_InxHemIWMokIXUZ8lbLBFzboFFTMWEXpNZ1et8eBXcwA4JUR6lsXU_gKwul8HLl2xDMuINraEbrigbtPF7BfdymNktHg5IIuBwBmswqGXtkkD_uH1L2MRTJQYmymvDqHu-5MtaaiB3MN4pKslbFfqUGsstlhygkuyrfJvlcKp99pHJ5zwx0O_bCOoH3WK-dcO7QifEvYpv55wiOvwE7fK3Q_bMh_vTpfZTXFD3Zz4xZOim4y2yoHAdvLos2twjCbcFgQrG6URca_mriKI-AjTAe5hXVzG6oUaQR5XRFcthRoLGt-vHl1CtzvV1EYZuIPKMOVAZWKF-Acw7aSza4V6hV19gBnvuB8HPL_dJyPrZVDLgNFYOmMWfPqflR8_Zv73FPcuADsMxLUNVcJiLkg9Pyv8eG9Yf78YwfoSgBp2-RUcyOTg_vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووری/ویدیوی منتشر شده در اینستاگرام ترامپ که حاکی از حمله زمینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/135474" target="_blank">📅 22:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/گزارشات از تحرکات شدید نیروهای آمریکایی در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/135473" target="_blank">📅 22:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23a9e6418b.mp4?token=AbcbyKRszAdZv8vyRSswFroRSE35EesGA7lwqwghyx-uAbklBq-9loVe1DDcPnXp8lF-OXSatbOu2vf3yR-RqSy8-iDsyFddI22eWC1gei649atInva7PQltvI00yw6atZFHE14L4cJ0qGXp_UY9JvgCZ2LTNJ8dPohf0xT4Q7sdOySdrTyzpVV3eLOYqK8jsD1MbWQhafCVJkRXeWj6SohB-4RrS5k6KFIhfnSj9g8lgADe6VQzHBqIaMTYWnj01FVlzV61baU_tqJDmi2dplwvONSzKTlqciELxphhK9ZcmBwK7BCWDLJa01DwZygSnCRiInNneqQ61fuqCV3HMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23a9e6418b.mp4?token=AbcbyKRszAdZv8vyRSswFroRSE35EesGA7lwqwghyx-uAbklBq-9loVe1DDcPnXp8lF-OXSatbOu2vf3yR-RqSy8-iDsyFddI22eWC1gei649atInva7PQltvI00yw6atZFHE14L4cJ0qGXp_UY9JvgCZ2LTNJ8dPohf0xT4Q7sdOySdrTyzpVV3eLOYqK8jsD1MbWQhafCVJkRXeWj6SohB-4RrS5k6KFIhfnSj9g8lgADe6VQzHBqIaMTYWnj01FVlzV61baU_tqJDmi2dplwvONSzKTlqciELxphhK9ZcmBwK7BCWDLJa01DwZygSnCRiInNneqQ61fuqCV3HMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: مقامات جمهوری اسلامی، هیچ جوره از مقامی که دارن کنار نمیکشن، یا باید اسرائیل اونارو کنار بزنه یا عزرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/135472" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/135471" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
به بهانه توهین بیرانوند به علی دایی بریم یه افشاگری ازش رو بزاریم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/135470" target="_blank">📅 22:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به بهانه توهین بیرانوند به علی دایی بریم یه افشاگری ازش رو بزاریم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/135469" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6DVefhegSKKcmzjDGY_5stqXewnv2oInwA1SKCwNkFFs16Hk-Tu5Kwj9-NQ-9F0aEyzfcjKY7tvucxmoqN3sUpGsIWB6FkrQHK4deltMfR3TieIAeTVLdaUJYE7KZ-5L7-vOfmPkxhKqFDIxoYDgwAxaGSkhJnyPPRLuPSGG5eRsbNEKhwbNS-_1aBJU_zuaz2XAG8LKYpWJOJ03CfX0z-Hh2d0cIYu0z0WWa3VQfTKQrkZ6gksi5DaLb4_FQ0TYhgXzEqjqmH1XdzYBSanhxg6goUpnkpgyE8BXDzdC6Wb7ZtJ4HTGYlz_1LlCGmRGuwyOo2DfUEP1xj-FsO4wJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم تا آخرین قطره خون جلوی دشمن مقاومت میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/135468" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/135467" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/135466" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/135465" target="_blank">📅 22:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرماندار بوشهر: همه چی عادیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/135464" target="_blank">📅 22:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش صدای بلند در روستای لنگر شهر بجنورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/135463" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmdV0K1cTjg4Tp3ThMH4SZmCM25-sdFKHPpRAKMmaMd-yI2p9hO70Nvre7kToiCxtlAWWcdh3QT9blRqCPwGVTl_wxxJ6Dmi8DLTqdcMepwB3f8IiBpyYwcbUGkL5T2ZSSXTa129P7-AiX5aGwDAU_jFE0h81ptJbaCv9KYnt2cmn3B92nAKVk2TgkM44op9elJE8ZWFWBRXCM0QV_dgkRR9ewpJ09fZn3rqMseK2NcmhP1hc-I-E53FlZ8FJv6n_WG3CrYJFPDX8cARKCE09CWOQkoU6aZ2rw6Deq7jIyrhnj8KISoIhDtfFf2Xe8hrf6cHn8hgx02zaWSRJzXaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سطح اختلال شدید
GPS
تو کشور‌های خلیج فارس :
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/135462" target="_blank">📅 22:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش‌ها از اختلال شدید اینترنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/135461" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2GiiwfCsf27fUOAsdJffWYp9PVpMFK9voMeC9YDJAwdANn-YSFTP7X4R8OdUIxrht6PzlsZqJvHCFxIRfubF5bjv_deqT7Igsel_e6REAUqfK0dFCjAP_RzJq8E5c0BjSoCDygOTpXWrV88AI9SsUVdnYPsvNmN0DxKdaLgwNjbQYdXUoM63fkq2zyOWRNvmEWbAI-nQdMsGd5ADoAto0V9GCyqOd3LMyoGx_RP1j8F9D9M7p0FLYmTqtomVNKCvY2mvmohvM9_ACAyErmTlrFTzs7e2P6xb-SvV-KwaZDWh8pG4Tao6Xgb8Y1AQMAp_ATDj_52nTD0DtEQaMpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست : فداکاری‌های شما، تنها باعث افزایش اراده ما میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/135460" target="_blank">📅 22:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما:
اگه اینا بیان جزایر ما رو هم بگیرن بازم دنیا به اخر نمیرسه که.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/135459" target="_blank">📅 22:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وقتی به اعتراض میگی اغتشاش،
به جاوید نامان دی ماه میگی تروریست،
مردم هم به حمله ترامپ میگن کمک بشردوستانه
🤔
چیزی که عوض داره، گله نداره...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/135458" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
استانداری هرمزگان: دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در حاشیه شهر سیریک و جاسک منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/135457" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wx0upt5R8nlXOJ7RXHwgzhiBeDZI0hcSaoYZOSYhxFpUhtUrFIj4td5ZvbqN983ic5P1YLUv1zHcECK1iRnBHagPSOYjoEa0i8FNFq1zmpRz6uo_BcB6Xg9ls20lS_uYgAYUZxGfjnGCLPwg_28iZKtZDqD2ZrtQVl9HLhQJ4HTZkZNalwuRUXT7RVaBHJdHCDBUDIW3-iIbr5mcZuUaT36f220sJrvxVLZCP6U-zhIRsVduoW9U_2SZ99Dke-pSodYJIY6FFRPmVG4GwojnGfPcizT8Ur7mCoAxSlqA4OO3BR58W0pR0AFOrv5finzDIKQhXAZ2VtXp7k5ibbKJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود از شهر جاسک در ایران به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/135456" target="_blank">📅 22:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از شلیک موشک های بالستیک-تاکتیکی اتکامز از سامانه هایمارس به سمت اهدافی در داخل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/135455" target="_blank">📅 21:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید…</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/135454" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135453">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sih38NvYYzcl2QoXn4FQwK-N1lgV12keqh2RwTgJayadDX_u_07whNk9tu1EruPyb29FjIqKm3MFzml5WD1W1r8ldl97DZVaydc1aMF0SKji7qi24ilezYj94JsI54p8O7f30Y9l84VjYPgGZhD5k_uzvCX_9ZUoZQ6-u7FEibIC7jaT7RDskpcXr_zVXmnUA5YZ004_AsDP6d01KIU17FZYamQdq6r-S0-qr-MSBPXsqYF20O4wyMO2R1Wzel_i__Ln6OQ-vSRatgCVie-Pp0gW9zcHZTuUMnnBSSJJGBCq7rKinlLsnpWUbhayEaWsoNnf76HUGUmT9V_imV6vPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ هواپیمای سوخت‌رسان آمریکایی اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/135453" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/خبرگزاری i24news: نهادهای دفاعی اسرائیل در حال آماده‌سازی برای وقوع یک جنگ بسیار جدی در کل منطقه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/135452" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / رویترز: ترامپ دستور شلیک قدرتمند در ساعات آینده را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/135451" target="_blank">📅 21:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDSPnfkxpE6jQavJA139mxfCItzgxCJ6GKK-qmby289D6grrlrncaWw9HsSCGYV9df2p1AU-JEBrYZwaTMVSK3nyE0aM7J_LikIhXknSdtv2c6tQYuXS6jO3bjg2dQeKZ5nfiBNovo-KF132XSmImR0E0b925N0rVKhFgbEybVdt2i3dPVaItcd8quWGRIuaD521qtVykC5dbAITJpI7KhMbeScSLaSyunPghgTqXcIufappMiWoVk1aJRH_U-wRDoSXUBzuIqdcEng3KhVqguJ5l5mVEs-f3Z0HcM08vT-gcfJ0w5Szp4w1JIWmFoXsDlMhzrAIMOFzg8aDb-eeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DbZBcjFYM8JJrNCwG2GdIhYhQvWxMZkF316N5owk2ogF71Un67QHGlpf2VBjM4EBS48BOXl4ZhL26MD-hMt0iqOTLu9BLyige-UNywuX0GxBI_U_ykHGTEQh9Y7e1UdEAbajxapr2qiIyDD6BJZaHIpMHYo463WlSWbttK3PSGaHR1qiE46FTbTGqa9EhhmKTNMpmkOZQPilG9uPzr9AzOo619GwpZ6ahft85akIcoqjeePLu7B1J_4h6yLzFyeIiG-bXzoJ1pOUF_ky03Bz6i3jma1vXR_KNt3oJksZo4-hNsrL9Tg1LtvdIHhiOpv_GAgOM6D4hv43U3JIFfgLxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای هشدار زودهنگام و کنترل هوابرد E-3G از عربستان سعودی برخاسته و هم‌زمان هواپیماهای سوخت‌رسان نیز از تل‌آویو به پرواز درآمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135449" target="_blank">📅 21:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌های بالستیک ایران شبانه به پایگاه هوایی موفق السلطی در اردن حمله کردند.
🔴
دست کم دو اصابت مستقیم تأیید شد، دو نظامی آمریکایی کشته و یک نفر نیز مفقود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/135448" target="_blank">📅 21:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135447" target="_blank">📅 21:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر اختصاصی که میزان تخریب گسترده در کشور بحرین را نشان می‌دهد، در پی حملات موشکی ایران به یک مجموعه استخر مورد استفاده سربازان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/135446" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/135444" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135443" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmA2v7UTPvoRSPI8PBqktnQyPIcqlBi6oUS6FkacP0VeVrsnu5vXx6YhTUHjb6em2OGbTdQRffztUsJ1C30SKWZaeoFNWtwmikQNYiL5AtILhAxPilnK0A8LnAFgGoXyJbvKjVJ9goZ6SRPvqPqgqjEccMLoNRQc9XgAESVVzYZXtOTrbS475TDVCKevDyIQvR9_UZnDtyXJqhyqXJ9g8fXOoSPi6GvjmkutujNQGc5OIp0WsNd3ahExeiVYCuOTHechaHzuUGL48-qKfH-V9nDTGQe6xqONX2WvPv2gHk2Vbd1DHYxGPSbSLK3jaHIipsOHGlvlhem65ARu_HDJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی روسیه به قطار مسافربری در زاپوریژیا؛ تلفات جانی گزارش نشد
🔴
رسانه United24 اعلام کرد در پی حمله پهپادی روسیه به یک قطار مسافربری در منطقه زاپوریژیا، لوکوموتیو و چند واگن این قطار آسیب دیدند.
🔴
با این حال، به‌دلیل تخلیه به‌موقع مسافران و خدمه پس از اعلام هشدار حمله هوایی، این حادثه هیچ‌گونه تلفات جانی بر جای نگذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/135442" target="_blank">📅 21:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تعدادِ سرباز‌های کُشته‌ آمریکا؛ از اول جنگ، توسط ایران، به عدد ۱۶ رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/135441" target="_blank">📅 21:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / رویترز‌ : خبر کشته های امریکا به کاخ سفید رسیده است و ترامپ بسیار عصبانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/135440" target="_blank">📅 21:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135439" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
استانداری هرمزگان: فعالیت ادارات در روز یکشنبه با حضور ۵۰درصدی کارکنان و براساس تشخیص مدیران دستگاه‌ها خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/135438" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/135437" target="_blank">📅 21:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از تجمع مردان عنکبوتی تو تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/135436" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/135435" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در خلیج عدن ربوده شد
🔴
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی تجاری در فاصله ۶۵ مایل دریایی جنوب المکلا در یمن، هنگام حرکت به‌سمت شرق در خلیج عدن، توسط افراد غیرمجاز تصرف شده است.
🔴
بر اساس به‌روزرسانی UKMTO، کشتی پس از تصرف به آب‌های سرزمینی سومالی منتقل شده و این رویداد رسماً در طبقه‌بندی «کشتی‌ربایی» قرار گرفته است.
🔴
تحقیقات درباره جزئیات حادثه ادامه دارد و به کشتی‌های عبوری توصیه شده با احتیاط حرکت کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/135434" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IZsXetjzfHuF5_enEVYzDtlgbb1q2vQu2noQgqs0WUt1jtCuyWy6nAMNNTpRQiEYu2B_kD7zXG2H5m4Kaw8hoQoH43kYTyt1PeL84JMjrfBhY-3moRAqV9T77TZw-aAEdUipB0L2_vBAKpKckxh2y8zwoJR7P8X6hC_h7lDFH1pxtxZFOtg7XH_4mqTMOpB83fjmJyXaX3ny23Qb_xFL_C3KK-A3rs3p0pvPJheCzWS0zQ5rqtk1DRfMztExhzKHds_1UACB819Cw3wOzcbgw-8h2e-xkv6z0SW4gEjpq3jsWrx9ch0wlqSPRz_-L5MVTfV-vJvNeRMFQpJv5y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/135433" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری /ادعای کانال ۱۳ اسرائیل: در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود:
هفته‌ای سرنوشت‌ساز در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/135432" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
