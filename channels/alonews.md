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
<img src="https://cdn4.telesco.pe/file/oTF_naOUns1QMXRzE2BIOHta7yf28o7ulF5EO_D-BOdrex52rFOqMkHqEdohTTJBj82UcrfMsq6khu0qPlXUHkebJWLX0GZf8k1zIfmdjXFsJTvRt5-wU_d4ZNn2V5mBiTaQEY4hL9ZfdSqQCL3VBgfgCggL1_tIVoy5hZ5X5ZxOIg99AYGWHWF6K91fGSgjbLXoXxEysZarV4mYY1xbHiqbefNRSW6vG7h3vu_eaQidqoYZHkEhT6vJCgOV0N13Uy7TKU1wHba_5NXRQEllpjJ6DjRPtMOivGY5XzOL5ADjob4U5a__tZ7aoUlNqx5wvdp5LF-FrLcpi6Vz_Wjg8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-144430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه چترکوت در استان مادھیا پرادش در هند نشان می‌دهد که آب‌های سیلاب تا ارتفاع نزدیک به یک ساختمان یک طبقه بالا آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/144430" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144429">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
استیون میلر، مشاور کاخ سفید: تنگه هرمز برای ایالات متحده باز و برای ایران بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/alonews/144429" target="_blank">📅 19:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144428">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصویری جدید از ورود وحشتناک سیل در نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144428" target="_blank">📅 18:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144427">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
الجزیره: قیمت بنزین ترامپ را تحت فشار قرار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144427" target="_blank">📅 18:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اقلیم کردستان عراق: شرکت‌های نفتی پس از اختلالات ناشی از حملات پهپادی، فعالیت و تولید را از سر گرفته‌اند
🔴
قائم‌مقام وزیر منابع طبیعی اقلیم کردستان عراق روز شنبه به رسانه‌های محلی گفت تولید نفت در این اقلیم از سر گرفته شده و اکنون بین ۲۲۰ هزار تا ۲۳۰ هزار بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/144426" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کرملین: در حال حاضر هیچ زمینه‌ای برای بهبود روابط بین روسیه و اتحادیه اروپا وجود ندارد.
🔴
اروپایی‌ها به طور کامل منابع نظامی خود را علیه فدراسیون روسیه بسیج کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/144425" target="_blank">📅 18:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqHAZGIuKShZbFpkarzj6EYec6qH-a--oMYBTZW0vKNJB-B1I2ZakxLp2aCE_jEoduKBvPrgmgK2m-oEFvztsNfvisDc5DIJvSNkqyhtiuxJ2ik5SnD2n-c4qEYaBw7qgDbal7Drgze5fjDK9AEFJwCJ3M1tDRYxBb0MvkD7pM9f0GwvpoaELeL7prgazeX2Veg7YsynszPtoZ4hrGfRHaZkXz6z7FucRpMbar5Lzl0rb_uFsZou82QYO_1aIQOGgUt_BzmtIX-Mkc1x0qLBKxMqV7dJJd4hoi-tFuKwV76I67GczwXGtSD-ZC61tv1dhWrWIGreN9m6CPdkM81YUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGn1BIpsU9WcsWrFbLZyLCZZYum95S19YAPG06zkl5grSS7vNPvBB0593qbxby7s4NesUP-Hp7pqpTKgSwEyNdrmVp3sEC4-4VW34RYpTjLMxImSr1sejt2AIbrokeuC2CB_Q7yrUAoBKbFkXS57Op2SmC3A1yloZTsv0it7y8cfFKBtt4BafVsZG-BDjLSegvQZu6AkYH11DWbEEzfxIRzDuCsZ6W7rYYV2WxEu5_Br4p0mA64MnY8Sihs0SE3kgWUgaZZkPxKFM_9KtXG3Fd9ocDj33z_YOK8-P-s1jAuG_GX31ZDSSoS57mWYZu65k2ZWYlF1Dt85WFYT-yBjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g31TNxkllOAleHnHeGeBWLmZ8Y9Y5FOk4FF6z05Dh6fGOsValmAhbHZ1D73Mu6G_pakD0eAWT0xm9fwDL9fUk5pPuqdllW5cRD80Hixl01u868DDAqL3A-XONsGZJBEgl-Ojk7PbHFylFdfqZQbAhInhwpR3Wpv6qGVJZW-_H5SnOUNxuhAmH5H17kjPqO9HR5MhfRxKLkibInvI0UU4k-UwDtUvW2hRx3b7db7J2S0yipN6lQxd_PFi2dljBRcYwykkkwDleLXEZlJYuAvSw5ZizE-Zrh0bNnetT65AKwoD98F5HPgXbTgoNMtQU4naaSfJnX2WjpEgZJkD7YoTxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون جت های اسرائیلی در حال بمباران جنوب لبنان می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144422" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
۳۷ نفر در حمله روسیه به کی‌یف کشته شدند؛ اوکراین نیز به کریمه حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/144421" target="_blank">📅 18:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ، به سی‌ان‌ان و ام‌اس‌ان‌بی‌سی حمله می‌کند و هر دو شبکه را «مارپیچ مرگ» می‌نامد و می‌گوید «واقعاً، هیچ‌کس به هیچ‌کدام از این دو شبکه نگاه نمی‌کند».
🔴
ترامپ از تحلیلگر نظرسنجی سی‌ان‌ان، هری انتن، تعریف کرد و گفت که او نباید اخراج شود، پس از ارائه نظرسنجی‌هایی که نشان می‌داد ترامپ «شش برابر محبوب‌تر» از آبراهام لینکلن، جورج واشینگتن یا هر رئیس‌جمهور دیگری است.
🔴
ترامپ گفت که سی‌ان‌ان می‌تواند از طریق «رهبری و مجریان جدید» احیا شود، در حالی که استدلال کرد که ام‌اس‌ان‌بی‌سی نمی‌تواند به همین شکل نجات یابد، زیرا «یک برند بزرگ هرگز واقعاً نابود نمی‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/144420" target="_blank">📅 18:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فارس: ترامپ رو تحت فشار گذاشتیم و درحال پیروزی مجدد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144419" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=S_1vrnHJKjFIHiZ2UPKA6w2_EMbB8JQPpQnCfkg4fgRDaqFsfHOgKzk2iRolYeUse9AGTynktZ4xloVnRtVqg166xX53T-FxnVyf1V0y_HJpItB8KNddT9vcOmkZCstV3sZqzt6vJgRl166UvPWHlTo6G8WzfjRY7CqwvtfHxENCzVyHCWbdaMMf1I9VoY99-YKUKW0MEgYwH2R_i5iVqIxFptptUbKogoXVJrIF_hEgQSedanJXDHhNyOz97wi7OiWDZbYpsTsj89q8QcCa32zQsUdaO-ygIW_EBzyMy_mGMs9tiTuQZDKoTBRTGgZ1-t9csarqKgtC6pwtwY5nzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=S_1vrnHJKjFIHiZ2UPKA6w2_EMbB8JQPpQnCfkg4fgRDaqFsfHOgKzk2iRolYeUse9AGTynktZ4xloVnRtVqg166xX53T-FxnVyf1V0y_HJpItB8KNddT9vcOmkZCstV3sZqzt6vJgRl166UvPWHlTo6G8WzfjRY7CqwvtfHxENCzVyHCWbdaMMf1I9VoY99-YKUKW0MEgYwH2R_i5iVqIxFptptUbKogoXVJrIF_hEgQSedanJXDHhNyOz97wi7OiWDZbYpsTsj89q8QcCa32zQsUdaO-ygIW_EBzyMy_mGMs9tiTuQZDKoTBRTGgZ1-t9csarqKgtC6pwtwY5nzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون وقوع سیلاب شدید در شهرستان راز خراسان شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/144418" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/al9AUkibZN1uNZODE_kmHyX8SIjMZ6J2TDGdbHG744dp-KqvzoXF3BerYZncpvjtDXCKJcpd76THxBojfLetrvJWHDIKUEnqGt4SuVduuwm5iMydob-if2tM8R2lktUhUOUjCBm3kpTpsSn-EsiVkf9Upg-x-uJ3sT5woV9-iQYrCxLxvoGkO5BzruXi6fIQAi6SmGJmaBpl0wgo9liF4-DIzxI0S4au0IoPPYU4QG-VSBU59sCcHuR0ntvbdY1iPA0r36f09siI3ZRh1-zu_NTh0qmA8Rr_WnC2y-jj6GpXSEml83qpLOoxZv4B6HlsDKp0MQ_pHi-7TRilOVBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0zxoyA1GnYTmfqDkN1pLrC0DVO41CGnkRcRorNzSVHT3MyAVs0H3Q7Mk39WgZNHFKin78DElyaAiyCrd47za6nSBkt0egbWLdr-Or_nGfeC_z_9Jk_m7xuyZIpyqSW5Sj-c1xrWHTI1J0r5EEB7zpnrzB92GD1kq8TTG88MSkHMpOw2kGdTrScdwDZQfTEzR1bGs8RHR6JQ932h4xhz4YIVpbIAgYexIUwmc0Sug650nr0MD7-GRSOGxUGio-rRDxglPdPKjS1zsV5JRjJHo-2hQqRcanazlITkds3rESLTA46c-jcNTN_Byo-7c1ZGFOl1nMUuwKUTVYsZddtgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWiARiHB_Y8w5pAiIm5kUYwTzDK7tjI7OfULTH-9ST4FxM8GVk5hTsB-DYooPOQ_f6cLuy6Z09oQ_8x74enIXNphGqQoafor6-ULGxhLGUvRTqCjDc5CxxOrUSFDH5J5wA_2VG3aCfYVquNuU3sr3eWlGvk_M1ctD3ZYazVNf6c5JR8-CCbkh5NF2w6_0BR7G1Acziqk8ho6JiDVwY2vD1nCPmrwnzFLg7AQcqdV2EjXEQVSMJYKmcUcSqQaIvCPZfNflLoZHtnr_KpCcPDM9316Uab6NB4rnWHFDnGnjH_fIVKD1AIInXD3dRMUuSuFwdKmYZ1nb55vG29MGty3vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر از حملات هوایی اسرائیل که علی الطاهر را در جنوب لبنان هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144415" target="_blank">📅 17:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
👈
هم اکنون قیمت دلار به ۲۰۷ هزارتومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/144414" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK8mbCnV5efNwGuoPhw50-iWsM57k2MS3mh3QRfYRHSheBHyNa-bApM60s95i47otOM6OC9wd0sNGlFsxnJnd2F6lxsPOyfMG0RlEfX2Km7w99s5TKgqEt7qihxFm_FBAKpNcM724ZV4_zGXMwQnGtxfk5rGIlZm30P3ZVL6nStFd_7qNCkGrfDW4le9j7iJ7vih7KrBGHhA8D35_UWfXJb-7_mGPjXrXVHZa6oOR7bET1xI6MKW2fsousegFFcquKGVf64dq-zVuYbd-SWZK8vyrJtKaUEA7dy0lywZdEUhTgP3D6wwYi3uyy1VsQk5SEajVsmbDDqIc7USMKU7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ، مقاله‌ای از روزنامه نیویورک پست با عنوان "ترامپ در جنگ با ایران پیروز می‌شود - بر سر راه خود بمانید" را دوباره منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/144413" target="_blank">📅 17:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9n-RgGA2vRhC-riyTDpZHjYmUGmeBm4wKiUVRPI6Yon4z7RE4mUOKCqNj2STFhDeOZpq9TQgjL7hHlX_sGJB17yEsIxlFlDz0PAdNGQ9qnQu-d4-MB0TS_mhka7Hiu8GOgIYyVV95z182BKCHlMdWOo1uWWUsZHBeLeNMN8QbjcQFzZmHVcV1XpFM2ywAaPuux4hCm6mE_PQM6x4DeTBronct_dg7j76uZpW-00LHUnMeTi7Qb30DyDWyaKw50cZEgnuOM49bMl9WDM6JF41mJ77Eu6aC8cjMv3fwQDCvc0vIZjrhl9ubEJFWMQdnfzRL5kqbm62OSN1mCSAVdi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار ایران آسیب نمی‌رساند.
🔴
اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144412" target="_blank">📅 17:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ys-FeRhm6VHjCQ7h9F5PJ5gnpIt45o83SqpTa-lHfbnb0GLg5RNlsJV4Qj6ivVutIHNS6NkS4ngDkowbW6ThO_msIY42sUcNKaC1cg0QnMvrBa8F0Rcnf4nyJKDJ3X9n4TPcwTuo5IQeU4nd7p5QM2AekFY7BRCQ2ev0FWouAV7LJzcDd7mtgZkTe19SnqlXTB-t2KSkP5a17qif1KAk3T8F59El4cu58XRkMO-WJtaJn8Fd0WGuvkMd_PRnpDn_FJxKRlqEg6ftH_Wj7JQxD7bY71SBZn8nAezUYM8eQxSIBSwadYqXXFgRsr2VRHdbNZIaOMTNkrB7vPk9C5MB3WLrntLMhxF-05vCvLcDM-5yLp2_XLxlrtCpWMM0yCjyGnXRg6pAG8-p0BcrNcOtua6DXulL4E7uL7THMLChwIXW2fs5IqkGSRDOOqM92VqwXVTMS5xXhkh9kMkVKLFFD01xJ634ev8uhNndt04JXcnjCCm-keEiMEdCEtYFycYsP48oHdwp9n_LviPjd2InWmDSODzNWZybJcOU8LFc5yCfCd0LjRBR_pj8lOxqAJ88UHl7cI7XxiDZTVEHbjM1jbbeU7e5U7Wzm8dR0h8O1Ly_8BRq-ei32ZOM51WNbLtnz9m8RDad9bgbaVWJrhafyHZbOZOFFqk5bKKXnmiLnXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ys-FeRhm6VHjCQ7h9F5PJ5gnpIt45o83SqpTa-lHfbnb0GLg5RNlsJV4Qj6ivVutIHNS6NkS4ngDkowbW6ThO_msIY42sUcNKaC1cg0QnMvrBa8F0Rcnf4nyJKDJ3X9n4TPcwTuo5IQeU4nd7p5QM2AekFY7BRCQ2ev0FWouAV7LJzcDd7mtgZkTe19SnqlXTB-t2KSkP5a17qif1KAk3T8F59El4cu58XRkMO-WJtaJn8Fd0WGuvkMd_PRnpDn_FJxKRlqEg6ftH_Wj7JQxD7bY71SBZn8nAezUYM8eQxSIBSwadYqXXFgRsr2VRHdbNZIaOMTNkrB7vPk9C5MB3WLrntLMhxF-05vCvLcDM-5yLp2_XLxlrtCpWMM0yCjyGnXRg6pAG8-p0BcrNcOtua6DXulL4E7uL7THMLChwIXW2fs5IqkGSRDOOqM92VqwXVTMS5xXhkh9kMkVKLFFD01xJ634ev8uhNndt04JXcnjCCm-keEiMEdCEtYFycYsP48oHdwp9n_LviPjd2InWmDSODzNWZybJcOU8LFc5yCfCd0LjRBR_pj8lOxqAJ88UHl7cI7XxiDZTVEHbjM1jbbeU7e5U7Wzm8dR0h8O1Ly_8BRq-ei32ZOM51WNbLtnz9m8RDad9bgbaVWJrhafyHZbOZOFFqk5bKKXnmiLnXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
آذر منصوری: پزشکیان گفته نه تنها استعفا نمی‌دهم بلکه برای انتخابات ریاست‌جمهوری بعدی هم هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144411" target="_blank">📅 17:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brLjXQCDU7PNJzz79kFHxe6JvfE1shZFqGmSEHKfAZCovWSwUShaqsU4wfUEoGg8Rje77BiPOTT5MxX6c2lhdrKiPsjWMnzN1dJ5FlcyBE1RPAGL8THIS48UGv_taI6nSESUieKqVEb318zTeIrjRGFIATR6oXRiCrUHUdMFaPtegO-9Xg4pecbeeV414V7waIq0mvD_uLga3yfFMrp31bFKzxwOaa0cuDPEeNJMJG8KPuvmrA9zXXTPwwaSD5qAYwkoKGmUzAtj6zH6FgcsFTQBCKd8VTnBBLfGoio0wYFCg-t5hYe2ZlFOnneo-KL_Iau1dDTJQD7TkviY-_2ADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری آناتولی: استفاده گسترده از تسلیحات پیشرفته در جنگ علیه ایران، ذخایر نظامی آمریکا را به‌شدت کاهش داده است
🔴
امروز توان واشنگتن برای بازدارندگی در برابر تهدیدهای چین و روسیه محدود شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/144410" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5cf7bf87.mp4?token=th0r3PjCDGWq_RR5d3JOkTHhW03RU8cLXrz6LeN0DMj898DGZC9C5pjlejk_PD7liREbRm1wf1h4Q48DDE3NzKP8X2DPZk7KqS7xnS7ow5CcL9IYt3ex5FPkrQ2ST_cQ47f8pckwyA6T7KqNgr9q6exzwQq2KXUuDbN2zVysLRzAcx7Xq5nkqiKZOfxzlRtGNPW9Gvqr4MK8yxiwxWqDZ0_0QclEwQ_ie0lbCb9lWc5ZxED18e1TbPLAjIj_WSF_qO6w2a7x5imNA3Pbh7coJ7UFa-fVlbj_MyvuALy8sVKNjIPb7XKXQiSCOA5Pf74wA3IcTIe65lN40QSQ2VC1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5cf7bf87.mp4?token=th0r3PjCDGWq_RR5d3JOkTHhW03RU8cLXrz6LeN0DMj898DGZC9C5pjlejk_PD7liREbRm1wf1h4Q48DDE3NzKP8X2DPZk7KqS7xnS7ow5CcL9IYt3ex5FPkrQ2ST_cQ47f8pckwyA6T7KqNgr9q6exzwQq2KXUuDbN2zVysLRzAcx7Xq5nkqiKZOfxzlRtGNPW9Gvqr4MK8yxiwxWqDZ0_0QclEwQ_ie0lbCb9lWc5ZxED18e1TbPLAjIj_WSF_qO6w2a7x5imNA3Pbh7coJ7UFa-fVlbj_MyvuALy8sVKNjIPb7XKXQiSCOA5Pf74wA3IcTIe65lN40QSQ2VC1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای معاون سیاسی سپاه: امروز در دنیا قضاوت و تصویر ایران قوی و مقتدر مطرح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144409" target="_blank">📅 16:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نبویان نماینده۲درصدی مجلس:
اقا مجتبی در صحت و سلامت کامل درحال جلو بردن امور کشوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/144408" target="_blank">📅 16:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144407">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akQ00APMjacJbtcPkT4SvDIGE_swQCSAh4TavjravgXvjpFGCmmnARkIE5bbLvSAjhch2ons-8NJQDrMEhZxX1WKLRue3FL_A-6ezeYlHwwVr1hn0R5uO6WFgP9KFHFhdCqEcro0mCQuFnWVCJn-UutkdcBcPSU1IIyAWhTvjSCNMrjd4xg_sf38GFEL9E0AREbnLG1WutvBzpxWfoX25wZFZ-1s6o08HHn09KwEylDyzPRv0vDursz6IIKG1v69q-m8fqjJRAJYLLqGb51-4Dqin59JXrBGxJ66krmu1t6mhRCcT9_DWV86tZ8kdB44sKCDeQG4vli_66QH3LvSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه ساعاتی پیش تو
فهرج کرمان
، یه پسر ۱۰ ساله از سر شوخی اسلحه‌ی شکاری پدرش رو میگیره و به سمت خواهرش شلیک میکنه؛ که متاسفانه تیر مستقیما به
سر
خواهر ۱۸ سالش برخورد میکنه و در جا فوت میشه.
پلیس‌ها هم بعد چند ساعت اومدن پسره رو بردن، اما پسره به حدی تو شوک فرو رفته که بعد از چند ساعت از این حادثه هنوز نتونسته یک کلمه حرف بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/144407" target="_blank">📅 16:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=M-ofeMxjm9hPbSfj-UGpdk-LwL81dNgyyKA635CNbRecmPMsYPeLnogoftgB5hVS_3GGNp3hnlPGo4TwA0MJ2v595WRH55A76Z15ds43OK4BJk3FoSU2-3N9oRebGjF6OTvRzgAbbxiuIu7SbvJfw5freWbe3lqtmSvLQitNllc6g9EvCjp1QmxJCCrLeVbo6pK0noDa3W9toCiSBzdP0IwOoH_2r8ldPtvVOGGcKOcFm4C1iMW2_yWt0BfGv6PEiEesb33FVz2FrtcLdape2kFDcslljk1oyiAaLTFb-BoDvH7u66CKMvr9JYae2MIreyF7wAvnGWfdOy-oN9e5Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=M-ofeMxjm9hPbSfj-UGpdk-LwL81dNgyyKA635CNbRecmPMsYPeLnogoftgB5hVS_3GGNp3hnlPGo4TwA0MJ2v595WRH55A76Z15ds43OK4BJk3FoSU2-3N9oRebGjF6OTvRzgAbbxiuIu7SbvJfw5freWbe3lqtmSvLQitNllc6g9EvCjp1QmxJCCrLeVbo6pK0noDa3W9toCiSBzdP0IwOoH_2r8ldPtvVOGGcKOcFm4C1iMW2_yWt0BfGv6PEiEesb33FVz2FrtcLdape2kFDcslljk1oyiAaLTFb-BoDvH7u66CKMvr9JYae2MIreyF7wAvnGWfdOy-oN9e5Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزه توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار میشه که حسابی سر و صدا کرده:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144403" target="_blank">📅 16:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دلار منفجر شد
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/144402" target="_blank">📅 16:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOvr3WJ2ObITEkuHc0LYoqOSTTRdhtiVvPvg0pXoA_MH99lyikrqCSGWBHWD4XOxbpIl_7I96hXISh6lWu3WGFnpvTP1ROcDfjdEIagEN7Uh8_yxNtxlKO6qKlPaYEwcwh-A8eUnRkuqJ2t97tyZW2MQuq500YaO3pwR0Vd2GdPeyu1_q3N6_e6hta2XhjqcoK47r30r-dWnS9BZnKrx869zXXdroCnVyEbaMZrMR4_jRo7PeZbuNtW7hw5mvVYhdTXlaxXm5_NuZN4gYJfq7TqiLLEEFSfxy2fdK4Gv-19dwJXZ-zBvQP0zmfoLLGey9S2M-4tb4DeufuxXGPd5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNOqyDiwydTwalYY81Y5tZoKrPKstwAGoZ9yd8mijaTNZVNjCqzH2SlvF1SKplHxZy64nwQEzjS0pH5MnbIHXeKpoMpyFOB12kTQJN2aFeFsIFKltxRk8ldk0Z8hdOE_NvG7PfbOrDvn8wMwwalFfnwL_WEh4sksnXcfdzO9XC2sGxp8zsmpKQHRfD2kpKf7esoEfO6Azp-NdTdqQDclAcE_VbT8Cpm2NQRpRKy18sNY8z3Pqkvp8S14KyYkByHfIaIldN_Ls-2GGeZwy8FNJq6SwxmbDz0tFLKxp9PVTLfObDoTsliyVqvkbiOVhpdwpZc0_nHRZxPeWCe-EPBMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZSvQZrz4OwykPFXvhRWC2smF3lsjNX5jABYTlmqwEtTXPOu9tQ_OukAwePjbSk6tK31eFjz3vMTa0JzYVvHwBrqOXUzyrlNxfzRKoaYPPuMyv_s4mY8pZzGR7nwg3eYNdCpF0NPFam4Yg3OFHzoBwd3mgz2erLaurTTe7RNLSChw9qWCjZna2o_cveR87WfEFhEoPEtoXWAxvuKRC3ZGY_yGNIPGJchXWNw8jGBNfcn_eQ8kGn78NAKtSvV5P9uZ7ODZbLK83XBTuuLGYdpe_3KYmiLiiPuGL1ddGfUE2EeZOoi5lLg4KfkMwdafpc-eYpLnoteof4dWROXFk2kBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQW2XCth3JxjD0fBADivz25grv_85yp5qRJYg_zUshsBIWxpj_9EDMP7sDoRBL_EaK5mK8NH0SUuuo-UebtVV6gJOoX8ocxEhkrb5C1nfxaCI1AuHqE8KLQixJOrSewpCGqn_NZjwIoq6DuPtne9TVA-LI_680dhEubBm_j4fCDVYfgVG4DsWiW-fYHXJU8vVrXQu9gUhwAnPlsdVD15KdtHfIQBCLGhaauKURm3_88JEWGM3OdJSNmA5DCRi_1gEkLKLFk8diP--YcDRdlr2-jPREOdplQgSPtog9bdumSctYcgRfFgSaA6Y7R4G6gbM3-GDo-rOYTEtVPUR5eENQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تجمع مالباختگان بورس برهان سهند شهرستان نقده درمقابل دادگستری کل استان آذربایجان غربی که بیش از۵سال هست منتظرماندن وهنوز به حق وحقوق خود نرسیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144398" target="_blank">📅 15:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p97OB23XQYAfB23ENwdiZkfW3iDtLfikACb2Tj_e31nlpKYsVdf0Nm44h_IjoDKyTu7lfub9FPVwuK2gA99i26XS_Gv6kCBk37k0XWjCRUXKx6kxGjhcDczC8Od1Yi4dB8i4hVN2BURylkaHwUhOyIMvKv0f9t3KOpw35be_QbWPMoEn3RwoA9ep3-pa1G32weypgEECUT55FyIC8Ix73gkuImJGSBYkmNSK9OhLoRX7HrSzTdTUZ2QR-HL8BEf1E2U7KoFMjGosBo1fzOudrVH3T_KqRJoDalAD0NfFvAGq5mdDebvo_K2n2InkPQUOE_7g4BbfCzG2aQy8JIB8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرف حق یوسف پزشکیان: ما باید هر کاری که برای تامین منافع مون لازمه انجام بدیم اگر منافع ما در غنی سازی است، دنبال کنیم. اگر نیست متوقف کنیم. اگر منافع ما در داشتن توان موشکی و پهپادی است دنبال کنیم اگر نیست دست برداریم
🔴
حیات و ممات ما به غنی سازی وابسته نیست اما به توان نظامی ما وابسته است. این دو قابل قیاس نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144397" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گویا قصیر خواننده لس آنجلسی که اخیرا به ایران اومده بود و از جمهوری اسلامی طرفداری کرده بود درخواست خروج از کشور و بازگشت رو داده ولی جمهوری اسلامی مخالفت کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144396" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: از جنگ خوش‌مان نمی‌آید اما با قدرت مقابل تجاوز می‌ایستیم و دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144395" target="_blank">📅 15:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: اگر تفاهم‌نامه‌ را که مورد تأیید همه دلسوزان است، به اجرا برسانیم، می‌توانیم بر مشکلات غلبه کنیم
🔴
با اجرای این تفاهم‌نامه، دشمنان قادر نخواهند بود منطقه را با آشوب مواجه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/144394" target="_blank">📅 15:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWGx0T14SmeIIbRtVEj6xBsCV4YkxIFAQcyf_AlIj_f2GcSW6GB0yNcP0gM-FgYVB2JYE9UcwP55Xf0kvzEVkrna49ChdjwhMMaACq0qwOGlSjz5pIdaUepOeNWy81qY6RAdinHkxFQmYDUfAjV0efrrZhjCmQuxqJfdrjh61Upmpb7csoCI6V0TxGMJfO6NnLOqqX43KLszovims3MssKfsTnT9wGlfN2ynHNs2ab0rW5siZ7malP0Kt_ojj3u4dGaaVINnf4m3ST1MJ2h9BgZflzSqmeYSOraVdWQca211SR4YPEfNsRz2X3mO7uAh6zq68RklyTXRyBhjuHH9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، گزارش NBC درباره بررسی نامزدی او در انتخابات ریاست‌جمهوری ۲۰۲۸ را رد کرد و آن را «۱۰۰٪ کذب» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144393" target="_blank">📅 15:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3063be136.mp4?token=H7k9g77snAHN0uJJdOf8GGV5HTpp7xTTalZys5xZIniO6dskzHoBI0dGHegNSIGg1YgXoU5ykhfflyNOO2xPcgk6KEUXk7s48DUXVKwYzU2aCI3RSmWiOlDo7tIqb03e2pxuDVZejXdaDBT3_r1g-4UPlHmdTwO4VksOYF8XmEYnd-zubT5sKSS3m-QnVVfXIKWE_Mfo6AOxHh8qJ-KaTYNpyfB-9RC13F1goO0VLrG_y2eQdq2XhPkKaCVEQkFccacnjHp9Yrx9NtTQuf6U7ts_FKBE29xhzgeY3kBRUxa7EVYMrPrpEuh_OaezuE9k2MumJvkyiKWmdB5bvBdttA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3063be136.mp4?token=H7k9g77snAHN0uJJdOf8GGV5HTpp7xTTalZys5xZIniO6dskzHoBI0dGHegNSIGg1YgXoU5ykhfflyNOO2xPcgk6KEUXk7s48DUXVKwYzU2aCI3RSmWiOlDo7tIqb03e2pxuDVZejXdaDBT3_r1g-4UPlHmdTwO4VksOYF8XmEYnd-zubT5sKSS3m-QnVVfXIKWE_Mfo6AOxHh8qJ-KaTYNpyfB-9RC13F1goO0VLrG_y2eQdq2XhPkKaCVEQkFccacnjHp9Yrx9NtTQuf6U7ts_FKBE29xhzgeY3kBRUxa7EVYMrPrpEuh_OaezuE9k2MumJvkyiKWmdB5bvBdttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی آمریکا تصاویر بیشتری از این عملیات منتشر کرده است که ورود تفنگداران دریایی آمریکا به یک ایستگاه سوخت‌رسانی شناور را نشان می‌دهد؛ شناوری که گفته می‌شود توسط باند جنایتکار اکوادوری «لوس چونروس» در آب‌های بین‌المللی اقیانوس آرام شرقی مورد استفاده قرار می‌گرفت.
🔴
تفنگداران دریایی عضو یگان اعزامی تفنگداران دریایی ۲۴، با یک قایق بادی تندرو نیروی دریایی آمریکا و با پشتیبانی هوایی بالگرد UH-1Y Venom وارد شناور شدند، سرنشینان آن را خارج کرده و سپس شناور را منهدم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/144392" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0ueyMNtucOYIbxslpb2JckaRpYxZ8HvjgY_ziFfOg9b2Hamd9WCVSdcmQzS0YcEA1K_H-ATSfiDRSv9CmkjRVUbFcCDd4J5RbPz4_09A3AlhSsjgK9xC9xonJ0oVvUfS1qCisIxh3WZEn-v9ZQauvWEyrIgUhM1oIVqrReu2HChP9lpqKATRoZCmO8VTQyLRLQucMBtxc62qrc59pjm9S8jjsRVgyYJ0gRs6Dulpl1AJ4JtxNTiDWQmYWLzhuRCMZCvzQPlohDVjeSgZZcVDwxTfor27UCisL1uK0hxHkEPDpqYlypTCZtAgWvypkvbRw1_neoBntfkZJIjIG0WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست جدید قیمت‌های موبایل در ایران؛ پایین‌رده‌ترین گوشی سامسونگ، A07 نزدیک به ۵۰ میلیون تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144391" target="_blank">📅 15:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbVTs-rWXF_wa7jlazmDDdhRhSvK3nWrT4t2-SV-8aCVGC9dgF7ukomtRuAtPMx87bX8Wc6i_J7FsYi4YP6nfFsUqP2U3bscEjq77mdDzCRxPLRK1zh8j0jtBzc7JbIPNQ6lZlSBIifcO-tL27IYkUbKFVmErc3aFfY3DP5Sk1_7egjcs1OnjmTHlDyK4Yg3sFKjrYe41L9gFuegqfdlG9lamib67nr4809YhkJSh1BUGeURsd8GJlSaAjFfsfkQeAu17ytsrdCzzaAgkfq_U-TDtencq5ojN73qn6SZzmUUd2SkmPWZ9XNvIDM9YZAw61NR8RSBFQk-DjslzoBCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: بر اساس اطلاعات و ارزیابی‌های اطلاعاتی ما، تلاش‌های گسترده‌ای برای دستکاری و جهت‌دهی به بازارهای انرژی در جریان است. برخی عناصر دولت آمریکا با استفاده از رسانه‌های ساده‌لوح و زودباور، درصدد تأثیرگذاری بر قیمت‌ها برای کسب منافع شخصی و در عین حال، گرفتار نگه داشتن رئیس‌جمهور آمریکا در جنگی هستند که در آن شکست خورده است.
🔴
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه و غیرواقع‌بینانه، به دنبال ترویج و تشویق ادامه جنگ هستند.
🔴
مصرف‌کنندگان آمریکایی هزینه واقعی این وضعیت را می‌پردازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/144390" target="_blank">📅 15:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511f12e405.mp4?token=BLmnXvQB7RHCr4kODx7TPYyZC2KkjDcwbJp9IKHLHsVi2d-4qOH82FwhIp4udONJrPfvip-E_PHoomNZmc030T_8f_xHkGPZyyq8mEmWxz6-stw9SNmzlUuiuOZmGA6bsHbW8FIKLQ_KZjqp2kd4xmRh-9JVxGP6M18HHh6sWRW4lJS4SqmZyI75WcImeQF3ntj7Pv_uikXURf7ArR0Yrsiq4XEGCA-9vUxfBslfyCAMNsBCi92Nw-SEFZzCt3jAx1_27kwIhmJr9Ct-RUaay6rHghrB9gindMxAvo_li_IwN-JnzrCGuf0F1ymW7Q952qmCiwIePdx-sWnai2P8kaFwJID4sCCPA8BVtyYsNHQJzu2CfuOQYKqX73QgE6s2MX7LTEXWXdXqfcfLcRD1zqq-x26KkoTEmHT--9HPP3AVaRNRW3I3k4iTVjh0MzLi3Txr30w06PynXYhLBu5eJ3wLmmf4ZqW9OTE_Upv0LJogLrnL3EpZyK3ESzkKyuyhyk7SsrsiliRubo-f_9HlRMW5VlmFPgfLaGz2GL2UEXbgVCpUEH_TkiZXy7e3o8FZJK3uPrmwTz63UsnCuBLtCueugx78vXr_1VLOfgzj8exrLK2Xyl5xXW1-hOsFKw1TAJ0ZfJGd9B4LpJebtM9cRqZO0CpeK9S_rZE_Zgu7qMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511f12e405.mp4?token=BLmnXvQB7RHCr4kODx7TPYyZC2KkjDcwbJp9IKHLHsVi2d-4qOH82FwhIp4udONJrPfvip-E_PHoomNZmc030T_8f_xHkGPZyyq8mEmWxz6-stw9SNmzlUuiuOZmGA6bsHbW8FIKLQ_KZjqp2kd4xmRh-9JVxGP6M18HHh6sWRW4lJS4SqmZyI75WcImeQF3ntj7Pv_uikXURf7ArR0Yrsiq4XEGCA-9vUxfBslfyCAMNsBCi92Nw-SEFZzCt3jAx1_27kwIhmJr9Ct-RUaay6rHghrB9gindMxAvo_li_IwN-JnzrCGuf0F1ymW7Q952qmCiwIePdx-sWnai2P8kaFwJID4sCCPA8BVtyYsNHQJzu2CfuOQYKqX73QgE6s2MX7LTEXWXdXqfcfLcRD1zqq-x26KkoTEmHT--9HPP3AVaRNRW3I3k4iTVjh0MzLi3Txr30w06PynXYhLBu5eJ3wLmmf4ZqW9OTE_Upv0LJogLrnL3EpZyK3ESzkKyuyhyk7SsrsiliRubo-f_9HlRMW5VlmFPgfLaGz2GL2UEXbgVCpUEH_TkiZXy7e3o8FZJK3uPrmwTz63UsnCuBLtCueugx78vXr_1VLOfgzj8exrLK2Xyl5xXW1-hOsFKw1TAJ0ZfJGd9B4LpJebtM9cRqZO0CpeK9S_rZE_Zgu7qMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی بزرگ در منطقه کی‌یف؛ تیم‌های امدادی در حال خاموش کردن عواقب حمله روسیه هستند، — رسانه‌های اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144389" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیرکار: تو جنگ اقتصادی هم مثل جنگ نظامی میخوایم پیروز بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144388" target="_blank">📅 14:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان: اگر لازم شد برق دولت را قطع کنید؛ برق صنایع نباید قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144387" target="_blank">📅 14:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN6qnRR8Q8836Zwjr6AWjxrHFxh4KQ-1VYAm6LEjkrf92tln2IAjLGF3nkjMko68pANNkSQK2irWP4bFMvu0p0SScT3YcD4NHUNNZodWAR-b-b2R4ddw57dObfs7uvAixT3vjCQW8l676086Qfc1VWYDJBLy4UkK0WX_fmhcNyCMi5rhBsS1HvL17RatXszj8WzpJNXIOkz1V1fVWD8T4We6eM7p2DwiniQk6QpkS-j56uToeTaLrpjay9REdWkpmZjehcJM0PRXKq5L6drcEYt8oKRM4YD1eh3O80FdBcX1oTwNbAZdzolEUSnXpWXl21Hfr0wRor8VkJ1n3ILDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای شهر اوتاوا روند بررسی تغییر نام خیابانی را آغاز کرده که حدود ۲۵ سال است به نام دونالد ترامپ نام‌گذاری شده است.
🔴
به گفته برخی اعضای شورا، با تشدید اختلافات تجاری میان کانادا و آمریکا و اظهارات تند ترامپ علیه کانادا، ادامه استفاده از نام او برای یک خیابان در پایتخت این کشور «مایه شرمساری» است و باید تغییر کند.
🔴
این پیشنهاد هنوز نهایی نشده و پس از طی مراحل قانونی، درباره تغییر نام خیابان تصمیم‌گیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144386" target="_blank">📅 14:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما: تو رو به خدا، به ۱۲۴ هزار پیغمبر، به همه اهل بیت باور کنیم ما در جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144385" target="_blank">📅 14:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سیلاب و رانش زمین در شیلی، پرو و بولیوی
🔴
سیلاب‌های ویرانگر، بارش برف و رانش زمین بخش‌هایی از منطقه آند در شیلی، پرو و بولیوی را تحت تأثیر قرار داده و خسارات گسترده‌ای برجای گذاشته است.
🔴
رئیس‌جمهور پرو در پی تشدید این شرایط، وضعیت فوق‌العاده اعلام کرده است.
🔴
کارشناسان هشدار داده‌اند که در صورت ادامه بحران، تا ۱.۲ میلیون نفر ممکن است تحت تأثیر این حوادث قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144384" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=om-sDPAYFcXrEsyLb2rjNquqX3f6LTVWIZS1sbRTb-c4mz9w-1p6S9vAqV1Ym1zB19VFpC4KOWYvEP8y6yXXzO6u3v7q24Lq-db9-UcgvllqCUNPcQ0gZDgGvcUcEMptIKcWGC_lJiNuPO2ANSGvSPN9HFX3DFghA4DjpI_E9EFB9SvUOTkTPNbnP3uMLDoclu5ogHw0wDg4XjqohJZP2JqVgFKRfVwlouF9xSIekVLKPFcYwknf8F2cq7HGIiS65fEV3j3ZRBYM_FjQelFu8_XOC8JuW4h8SR_kKgR1D7kB4LEZ2Ir2okYYxEJnBWIXIslEtvIwAP3vPGEYdH4AbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=om-sDPAYFcXrEsyLb2rjNquqX3f6LTVWIZS1sbRTb-c4mz9w-1p6S9vAqV1Ym1zB19VFpC4KOWYvEP8y6yXXzO6u3v7q24Lq-db9-UcgvllqCUNPcQ0gZDgGvcUcEMptIKcWGC_lJiNuPO2ANSGvSPN9HFX3DFghA4DjpI_E9EFB9SvUOTkTPNbnP3uMLDoclu5ogHw0wDg4XjqohJZP2JqVgFKRfVwlouF9xSIekVLKPFcYwknf8F2cq7HGIiS65fEV3j3ZRBYM_FjQelFu8_XOC8JuW4h8SR_kKgR1D7kB4LEZ2Ir2okYYxEJnBWIXIslEtvIwAP3vPGEYdH4AbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری ازدرگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144383" target="_blank">📅 14:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMwLlKIgHarfVg5NHvcX2ulEiQS98awAXcsBIZT4CGzwZCne45bFFpbSKaLneWoxd2GzvKoLaUzEXEkTB-hrX_1FkfAOepiB5nsgJiCULg48A3MaSdH7VuD_imLPVf7dxJw7me75AWhsM2bMmbKIAsfnWQa-tCgrsTUXxibacEtepIPwfAtzTKc0dNsW8wIafTIgn_PEkRXKrutfErln71yHS1wIAngDpUYLe0UN4QAswbaiwyI_nkVmNik1EaOIZ-bec0qwo9SiAqoGTIYMVnCefm6qlccfggZ_aRCAUUpcICjMkjRFht_Ymt3tXzvIEf_YmkSzMcE53Kg1YrXE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این مرد ایتالیایی بعد از اینکه مادرش فوت میکنه چیزی به کسی نمیگه و اونو توی خونه مومیایی میکنه و بعد خودشو به شکل مادرش در میاره تا مستمری سالیانه ۶۰ هزار دلاری مادرش رو بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144382" target="_blank">📅 14:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5KwNe_nFEg6_gGf_ifHOhjU2OMPjwEmldsLchwXBRkWDrPubAmowxlm8b7kLI2y54Ir7we1hE2uQmIU87Ecv7U9VRDqHC5tgehIs7HsFSevirdQ3aaLB_3PTRwkJUdV0s16I27c3DtqzXx-tSCjKMjqLjCo6L4d3gNHuo-OkBXiaWN2VSB1YVsZYuAndOjd7Q5BPYlvpD5tB2vx6oZUedpz89_dOW3MszJd-5A-D7ecZ0qEGbUix_nFhocIon0wnjmAHXvU25DdWW1vaJ9yRJb7EIhEH9YJi_zbWST7lFVh_8g93WkcfZrzV_8pGyWaMYyxiERJYeyHJ0a4ifuUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع برکنارشده اوکراین به تیم دفاعی ایتالیا پیوست
‏
🔴
میخائیلو فدوروف وزیر دفاع پیشین اوکراین پیشنهاد وزیر دفاع ایتالیا برای همکاری به عنوان مشاور در زمینه نوآوری‌های دفاعی را پذیرفت؛ سمتی که قرار است در کنار فعالیت اصلی او برای راه‌اندازی صندوق سرمایه‌گذاری دفاعی در اوکراین دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144381" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144380" target="_blank">📅 13:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_aur90-31DhknWDB-rnsOnubYK37rAZqlQeg-wy-HA6u9jDD5l9sBbBeiQHn4GuI1Oyg16kHjcl-hETKtbZ-CfugLGkFFS1_aNx1lQofRu2IsfcKvzzfX80eXtgQ0qq8cMgBpO40zTIQNlzeQItsRAiO2xS7Yd7Fvz4SuLOMb0SEQkJ0FgCQm-oK8v0wTRV7nALFCB4i7uBKKgpC4ZuiiG80iU1BAKLrZDTJK4be6QDNdkaXEKCYy3OgbbhM2d5IvHvE3dRWFunr36QkZBgP0r86gbzUX9yS_SHZBMYnwH64dA0RgNse8MHM24J5wa0jaewtngUqqF_RZC7Mg5bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی توافق عظیم نفتی ونزوئلا و آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144379" target="_blank">📅 13:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=Y4yqRe6V_2bFFSfZdZ1soSORbGdWjs-GrY7Qn42eiGIUh6oU6GdSCMK0REktRJWVvo30WCfI9Eh3zURMMFSpkIKC8OTl4ayZJRxcHOZ_th9pm_5G1BHuO7CkO4Mansk66Svij-YrmondndMeVnd8U31zXuRvVxkw1bSvdRjC4f1NOiRSh5hAUUgfTaPpps5MoVXVX-0ev3SmPnVSHzL--gDLJX8JO6hFTdGdIAMhugpW8pIQEBICOni6yJ5C_62rl9L_nuDLglXajlqpGKaK2nhUJrpAx_tkxH09RkI-tAicbEcEWzna5_hLcX8apfgDAJ-lT9tWX69N45_zeke8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=Y4yqRe6V_2bFFSfZdZ1soSORbGdWjs-GrY7Qn42eiGIUh6oU6GdSCMK0REktRJWVvo30WCfI9Eh3zURMMFSpkIKC8OTl4ayZJRxcHOZ_th9pm_5G1BHuO7CkO4Mansk66Svij-YrmondndMeVnd8U31zXuRvVxkw1bSvdRjC4f1NOiRSh5hAUUgfTaPpps5MoVXVX-0ev3SmPnVSHzL--gDLJX8JO6hFTdGdIAMhugpW8pIQEBICOni6yJ5C_62rl9L_nuDLglXajlqpGKaK2nhUJrpAx_tkxH09RkI-tAicbEcEWzna5_hLcX8apfgDAJ-lT9tWX69N45_zeke8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مسعود پزشکیان: برای کسانی که می‌گویند تحریم‌ها هیچ تاثیری ندارند، واقعاً نمی‌دانم چه بگویم.
🔴
منظورم این است که عقل سلیم یک چیز خوب است. این تمام چیزی است که می‌خواهم بگویم.
🔴
عقل سلیم واقعاً یک چیز خوب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144378" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsbEOKLp9mv8Sikk09ZJAL7IYBRQZ-k8DsQ7JVT9kl1HW2QHjBF9GPnl2z8FORmhUbJhTCMMlxFGFRRYVIUvwPTvR3ImeB94TKwU3lpJVI3KQoEdZ7NnwMG5drBv0v1NRbTSHuCpf66UUugLHR06QOYUjHFxF_c527MpP2se5z1oZtXmAEn8QCdreKV8aJLHXdOu3irfs0qrF2fKnZETmvBgxtjSVo-As35nR4vOIFZVe7o_shZ23TU19s4ka8LSvjMpo0_wkzWyHSk8DhYq_C_3g14DmZ6MdnmL9pi_bEVLG681kO8I7x_yQaVWKwCiwHvRGvwZbxByocLOPcaQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: شنیدن خبر درگذشت پادشاه هارالد نروژ بسیار غم‌انگیز است. او مردی قوی، با افتخار و بسیار مورد احترام بود. او به کشورش عشق می‌ورزید و واقعاً مورد عشق و احترام مردمش بود.
🔴
قلب ما با خانواده سلطنتی و تمام مردم نروژ در این دوران سخت است.
🔴
این یک فقدان بزرگ است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144377" target="_blank">📅 13:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144376" target="_blank">📅 13:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNIU7KJg5pJ9MvG43zKZTn8-E_C2Y6zM0_xm0HfqMxRf6_QImx9J3iS3-5t7cu60we4rYIuKZX6FotUbri__Ob4xe3mOs_K9FJiCk-T4jVqlzI4nru0vtvghl0-ACfVMsGwgq8lafXGbTE5WTWk_IioNnGklmch-utA0OdzQioFFTrIT0gWuPYED7_xGcFpfRJXkyIa5Tk26wnLHzcVcJraS2GWh7LlTAKOg9Ndzfn3ySt8mLzq79bmCL-odyKAwAAyjlOnrmZY1fvD4t-nOx21lhDqRaPLc34Jw3TUlZy65eGyaBjezSZaKNpRuKdmTat8wCmsKXFzF1n3t_287Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت دلار از ۲۰۵ هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144375" target="_blank">📅 13:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz4KEztPUxhGFHywa4apoH5xPkZs-Ji2mXJzxrzuPssybL3Sbw4ysy3a_GUrJpZgHGk27_PTiNeVDzJYJcX8C03CLzA_wAdod5syfyhLiLz3QYls-IHXSk_VEOfAj0EP7gvSpvc5oFz_fpCnEzfvekt4uZ8jZoTz_-yjeWSx7PiwuAGbEmRbX2why5MTTEzSiDEPI8GTWBrsIRbsSSI6Dq0nmsOCoraa1d1UqbxOeA-fn_Al9g546CLQNUk5xu5xC0QeJt-j4GBCrapP9_jk-fF9bl595a6etz56k0vBsm35vAfLuXezWRpnf5zMqdDu_aklbHGIHIvMDthm_Gy6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: میانگین عبور کشتی‌ها از تنگه هرمز، از ۱۰۰ فروند قبل از جنگ به ۷ فروند در روز رسیده/ ۵۹ درصد ذخایر استراتژیک آمریکا خالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144374" target="_blank">📅 12:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دادستان تهران: پرونده نتانیاهو و ترامپ رفت دادگاه تا رای صادر شه ایشالله
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144373" target="_blank">📅 12:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۸ ریشتر حوالی قصرشیرین در استان کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144372" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyp5MRT3G2nG9U_E88jg_YIhzkLeuQz_cz5gXxt_FtxVfmayK_fD_KpxiL5azUg2FfwIr9igNgARUTGKrruj-n94EAFNbHKSKjnmhRF5f8mjaambMfUpDGUNoFW84FpToO7TsH_6Len-xMSIJmScXe8I9xexpY5-kmILR2t6AM1by1wsTXwDomhfFaTzDKtePieDfpknXYxkjzB-_XA3Mmno2zuC5y7i_uJZD2Id9G2Y9iIpGHHrAqQROBEhVAyC7saKKFS5ZWg9Q3MovcxrORllTW4hOKRhIHnjWVZ0TzTBCRXsHwlHK0maYxk_Bl9tyAHMjnuwEYijR_8kyN51BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیهان مشاور قالیباف را بی‌غیرت خطاب کرد
🔴
امیر ابراهیم رسولی یکی از مشاوران قالیباف پیش از این گفته بود: خونخواه رهبرم ولی پوشک بچه شده ۸۶۰ هزارتومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144371" target="_blank">📅 12:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlv-TJPZZN-kal5LirOTV2LJJXAZdDWKZFGOCF1X4x0fwhF2ZPz1bPeNA66qVI7fCYJDjE7YaqpaTcTAhB_lYrd264ekZOvJBQ-N9xOvq1zGBiVLA7Kq1VrB3oILoRbLilXN5rci2TAzS8YTY1h-JTq_a9-DJzkMdXHL-Gcsv-jyzU93t_hIxngYfqh-Bk86aji4Ac8AxrNqwk7DTGhardMGyoZVwvcX8ru8BG2swXfv9TvrabNa7cZ-BZqbkkNz7l04gnSvWql3cE-qxVaRx3gL4l4c70EoM4P0zlkANo9ekM90a9zGKTUbzrwY_SeFikddkPntwwK1g84_Em28iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلدمن ساکس: بازگشت میزان صادرات نفت به دو سوم سطح قبل از جنگ
🔴
به گزارش گلدمن ساکس، صادرات نفت خلیج فارس به ۱۵ تا ۱۶ میلیون بشکه در روز بهبود یافته است - که حدود دو سوم سطح قبل از جنگ است.
🔴
نفتکش‌ها به‌طور فزاینده‌ای «تاریک می‌شوند» (ارسال سیگنال موقعیت خود را متوقف می‌کنند) و از انتقال‌های کشتی‌به‌کشتی برای دور زدن اختلالات استفاده می‌کنند، که به کاهش قیمت نفت به حدود ۸۹ دلار از ۱۲۰+ دلار در آوریل کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144370" target="_blank">📅 12:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گاردین: دانشگاه اکستر بریتانیا با عربستان سعودی برای آموزش افسران و مقام‌های نظامی توافق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144369" target="_blank">📅 12:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی اعلام کرد ستاد مشترک ارتش کره‌جنوبی روز جمعه به وقت محلی از برگزاری رزمایش نظامی مشترک این کشور با ژاپن و آمریکا از ۹ تا ۱۱ سپتامبر (۱۸ تا ۲۰ شهریور ۱۴۰۵) خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144368" target="_blank">📅 12:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144367">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ونزوئلا در فکر خروج از اوپک؛ خطری برای انسجام و اعتبار این کارتل نفتی
🔴
بررسی احتمال خروج ونزوئلا از اوپک، هم‌زمان با چرخش این کشور به سمت واشنگتن، جایگاه و اعتبار این کارتل نفتی را با چالشی جدی مواجه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144367" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144366">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=jEHZ4mq99sGmQnq78Q-_7LMNWu9RTWlW0eLSqPwCnBuahUT3_5I76FVDHXRxNjeHGhc-0tCiaM-iWZYH150mcohW0UXyVRF8moqamgBkjQohK_Y7BRMzAFAzweCFq6oXfc73QRfel82djwQY7BbrN_6RAOttKvx3cYm7JNcG0r71coBbDVYtEmDfEEKL55N4eX-magf0ntQSjPPRrnyFOaQTfZgcTyNxnCjHqPeCnRalz8kfBCYGOER9Afzji9ccC9wpVQXc0g2gEc5Z17AcrHyruXYDthCog6oZUqArduiZe5W1qAF6WM-HaRnvUStfXAH9zj23xMhPutc8i_Bodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=jEHZ4mq99sGmQnq78Q-_7LMNWu9RTWlW0eLSqPwCnBuahUT3_5I76FVDHXRxNjeHGhc-0tCiaM-iWZYH150mcohW0UXyVRF8moqamgBkjQohK_Y7BRMzAFAzweCFq6oXfc73QRfel82djwQY7BbrN_6RAOttKvx3cYm7JNcG0r71coBbDVYtEmDfEEKL55N4eX-magf0ntQSjPPRrnyFOaQTfZgcTyNxnCjHqPeCnRalz8kfBCYGOER9Afzji9ccC9wpVQXc0g2gEc5Z17AcrHyruXYDthCog6oZUqArduiZe5W1qAF6WM-HaRnvUStfXAH9zj23xMhPutc8i_Bodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از
آخرین وضعیت تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144366" target="_blank">📅 12:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رسانه نزدیک به ماگا: آمریکا مخفیانه مسیر جدیدی در تنگه هرمز باز کرده است
🔴
«مورس ریپورت» مدعی شده تصاویر ماهواره‌ای از لایروبی یک مسیر کشتیرانی جدید در بخش عمانی تنگه هرمز حکایت دارد؛ مسیری با حدود ۴۸۸ متر عرض و ۲۸ متر عمق که به ادعای این رسانه، کشتی‌های عبوری از آن از خط دید مستقیم نیروهای ایران خارج خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144365" target="_blank">📅 11:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی: ایالات متحده برای مقابله با ایران، حجم بسیار زیادی از مهمات و تسلیحات را با سرعت به خاورمیانه منتقل کرده؛ به گونه‌ای که در مورد تضعیف توان این کشور برای دفاع در برابر تهدید‌های احتمالی از سوی چین و روسیه، نگرانی‌هایی ایجاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144364" target="_blank">📅 11:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtWmr3KZ7AUAQQotBM3sEaQAh7wZff7cZEHm7ckf_kIt0r2q9FAYcTH6wTSVn8aAw9tfySLBQPXaRNTuto_arOL6CqtiDwNi8N46NV0uSnw65Ub1WuPby6iQwl-gieTp7P16crSPfRn-KqNZBhaAw5kucY7v1xC1StltgKkPWJREFzdBIfLf1BYKpI3iQN2HmmK3OKcGrjSl_di9wiwfz4vQWM5D5CbM01CAXrug0zEIUDBtJmQGlAlZazOQEuj7BkTfF5KmUX3LPQezM6MZye0NpaUKHWswWdJw8HcBCbG2RN177KVqIytt06zKLHMhFxwNmaFARuTYPn7dq5UttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای از باقیمانده ناوچه‌های جماران، نقدی ،بایندر و چند شناور دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144363" target="_blank">📅 11:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
شمال کشور از دوشنبه پاییزی می‌شود
🔴
هواشناسی: انتظار می‌رود از دوشنبه و سه‌شنبه، هوای خنک بر بخش‌های گسترده‌ای از کشور حاکم شود. این افت دما به‌گونه‌ای است که بسیاری از نقاط کشور دمایی کمتر از حد نرمال را تجربه خواهند کرد.
🔴
همچنین پیش‌بینی می‌شود شرایط جوی و دمایی در نواحی سردسیر شمال‌ غرب و شمال کشور، حال‌وهوایی شبه‌پاییزی به خود بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144362" target="_blank">📅 11:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حمله اوکراین به بلگورود؛ ۳ کشته و ۹ زخمی
🔴
مقام‌های روسیه اعلام کرده‌اند در حمله اوکراین به منطقه بلگورود، دست‌کم ۳ نفر کشته و ۹ نفر زخمی شده‌اند.
🔴
هنوز جزئیات بیشتری درباره نوع حمله، محل دقیق اصابت و میزان خسارت منتشر نشده است.
🔴
بلگورود در ماه‌های اخیر بارها به یکی از اصلی‌ترین مناطق مرزی درگیر با حملات اوکراین تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144361" target="_blank">📅 11:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz-zQwiLz_eGlv6jYPS2wVLhLMuUKXsBPOmGKrRfK-BGueP3sRZZ2wn-UtmQewTBynJiy-fCO5F5_MU_hdC6MTTSDH0HUxsrrdM4sOIevPvFuJqkHjwFg4o63oYjUvchkEWIpLBSX2mkdb7hNNaPwWhmv7kKee1XjBg-scuqqhW0qoz8LwHZTX0EiTCexigPigVc2R-xM44ZYgvwOxMQPEFocMhzWJwoP5UJwUsYDJxTRDjb-iaP9b3cU-Qw_EfrykOsrg6Q-Ry4ZLvwiuhvy2ktzgcWFS8wRg3K-jqic16n8dU-OJkqpN_75wq5U3xCtjFLC2J6F7pn6ccbuKGTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فضای هوایی نزدیک تنگه هرمز شب گذشته شاهد فعالیت گسترده هواپیماهای آمریکایی تانکربود بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144360" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک‌تایمز: جنگ ترامپ علیه ایران پس از گذشت شش ماه، به نسخه‌ای از «جنگ‌های بی‌پایان» بوش تبدیل شده
🔴
ترامپ در برزخی آزار دهنده میان «نبرد تمام عیار» و «صلح واقعی» گرفتار شده
🔴
شاید نقطه مطلوب راهبردی پیدا شده باشد؛ یعنی «فشار قهری مستمر، بدون جنگی بزرگ یا توافقی غیر قابل‌ قبول»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144359" target="_blank">📅 11:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiVfjhJ9LmQxv-dPkMAx6lWjn8WxyyZJ6_d26EplZGS39HAuN5LTXsk4uJmeSSZIveEKOdPAGuenAwZncHUdSWFfu76Uo7iLEs6XfrhyJOtkuJ4-alvs9tGDXbBrvj9aHGnWyabshwRVgt4Jw5o8VSquTmJ9DwR-JvGVfjXoQ51VMcCgKAJFqTlx_ZqF_40mJ8sbpE3n4u66ndlCOrXb6AfLy-4FHLr-enw-cpnvuFwwa65J8FwEDJqknkpT-MiMQIdtdbnQyGReCj87f_fYGbinGm6U-DEuXbpjzCzTxBqRftzUMoRZcmwVc5EYegReCYC0HTqRhfHEUtTQS9s2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو
:
توافق نفتی جدید با ونزوئلا، ۱۰۰ میلیارد دلار سرمایه‌گذاری برای این کشور به همراه داره!
🔴
این توافق پیروزی بزرگ برای مردم آمریکا و ونزوئلاس!
🔴
با سرمایه‌گذاری ۱۰۰ میلیارد دلاری در ونزوئلا؛ از هزاران شغل پردرآمد حمایت خواهد شد و به بازسازی اقتصاد ونزوئلا کمک میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144358" target="_blank">📅 11:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نیویورک‌تایمز:
جنگ ترامپ با ایران به «جنگ بی‌پایان» شبیه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144357" target="_blank">📅 10:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144356">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/طرفداران پهلوی به خونه علی کریمی حمله کردن و کتکش زدن
🔴
اولین فیلم از دوربین مداربسته منتشر شد
🚨
🚨
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144356" target="_blank">📅 10:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
استیون میلر، مشاور کاخ سفید مدعی شد: آنچه ترامپ در ایران به دست آورد، بزرگترین دستاورد نظامی در تاریخ جنگ‌های مدرن است
🔴
مین‌های ایرانی در خطوط کشتیرانی بین‌المللی در تنگه هرمز خنثی شده‌اند.
🔴
تقریباً ۱۵۰۰ کشتی حامل ۷۵۰ میلیون بشکه نفت تحت حفاظت ایالات متحده از تنگه هرمز عبور کرده‌اند.
🔴
ایران از زمان از سرگیری تحریم در ماه گذشته، هیچ نفتی از سواحل خود صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144355" target="_blank">📅 10:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866482ed98.mp4?token=IFN6L2jWgNtLCg44EatFPqlESCVY1jXXfEL4reu80wRr4l0qGPce_vNcCdlcaWS_2zgPvkXr5kOABSiIK3TX_cNwXoQjDuA5T6n3MDrYGS0VVieQz4ayYSwJvXufoHi8gO0qpoyJX33Z04w734HR5QGm1affR_6AZDgzrSbuc5Kgght2HWiaA1z8T2xFOsQ0pxXoJWNfVyRstfF9PV4gtogFBc355PDe5e_ptyxVy-U1d_KY5kxZzA2UfoLDu6F-sL0s7cct5nZF-e680y7xFnGnYhDU1D-ZV3VcCE_kK8S0h1zP6z2eESfoH1z_qTYNdf3VklbJ0NaJZIYdlSx1Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866482ed98.mp4?token=IFN6L2jWgNtLCg44EatFPqlESCVY1jXXfEL4reu80wRr4l0qGPce_vNcCdlcaWS_2zgPvkXr5kOABSiIK3TX_cNwXoQjDuA5T6n3MDrYGS0VVieQz4ayYSwJvXufoHi8gO0qpoyJX33Z04w734HR5QGm1affR_6AZDgzrSbuc5Kgght2HWiaA1z8T2xFOsQ0pxXoJWNfVyRstfF9PV4gtogFBc355PDe5e_ptyxVy-U1d_KY5kxZzA2UfoLDu6F-sL0s7cct5nZF-e680y7xFnGnYhDU1D-ZV3VcCE_kK8S0h1zP6z2eESfoH1z_qTYNdf3VklbJ0NaJZIYdlSx1Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: در صدا و سیما می‌گویند تورم آمریکا ۲ درصد بالا رفته، تورم ایران که ۱۰۰% رفته بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144354" target="_blank">📅 10:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144353" target="_blank">📅 10:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2ifYoudi5ZgSoOvc8QJC117osc_MyP2XM0MiILekMMBpt2pW2Pcutuev8PJ6tLzCwJ6e8QDZI08ip1v9jccaRQAmL-pMHcMd1D30icgKZmLZvRlrrfcjnmu1NWCs3k4bIPTPHXvIoPHc6qoItHS_kr_nTTbgXT6tdN5EbqRkY66J3eHBeQnNYCLbCJGFF5HEMUnJSmCk2zuGvuRxoWHC1U7VeZq1dAiTx_qTvdBNqkABWYFAnfxVySdf_gxgVsMC5PlAVDb9j5s7M72a5FHmADeVlPu8Wkieg8yXg8kzsptaJnVBjQJ5Fkf2Ne6obMP446I-4cTL0QxmjXiw_dJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف ۵۰ تن تخم مرغ احتکار شده در قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144352" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFJvbs8cYSgmxrUvxR8T7KSwsSYsiNeS_RsA_ofSVCguuj9m2co9AUEb9x7HrrClDV8_JbKWjpq3YjRJikEpjNrNMQzX6YLf42ibZqwaLEB_-jJ_GEI3RrE_rVzeccdUwiq26CInqqdcjMBnb3aCEFbJdKS1lDH-IN-ms-95g4wHlpDUxQsbwlvMJGMel4qA8_5cXKPnuKyeDVJEYbQ8QV_Ozl2ry74H-kUUOdzRmcCiOYvQhKvh1iP5bs0spLFHwGmZxHI_bg2jAauxjm8FOvHMJ1inQ1u77pXWTMI3OP_6CyPOdjB-4JGc5jXznmX3QPVi1F7MdflrppWYAfdZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل شهرک
حاریس
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144351" target="_blank">📅 10:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144350">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روزنامه معاریو به نقل از منبع سیاسی:
نتانیاهو در قبال لبنان با احتیاط رفتار می‌کند تا ترامپ را خشمگین نکند
🔴
یک منبع سیاسی گفت: بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در قبال لبنان با احتیاط رفتار می‌کند تا دونالد ترامپ، رئیس‌جمهور آمریکا، را خشمگین نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144350" target="_blank">📅 09:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به میانجی‌ها گفت هیچ علاقه‌ای به بازگشت به تفاهم‌نامه اسلام‌آباد ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144349" target="_blank">📅 09:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnNhIbcq7Cp121OwFnxYuzDUkMtXbqX1YIIq8Lsj4A-H9OC31UMi2WavjUe_gbnSrfe1GwRDnkaLak3PR4QCFRcMz0e4p_63tkL-6MNc98C5vlVvKCfOeM84VUg59tStTBB83bg5XSIkZGQ-98Lnhkrg3_2RmFU__fGYHhdk3iTOZuzPbpUu7RxZG_pF5hg2-foaUPpmMBDzDMoZMI47D98y36MBwhBjFulYjH_MeAAtaUJO1Oa9-NwtadSm9GjVPN_nU5LXjD-_fVEeGWX5NAGjArSa9OLxDUAPKOIqOEs56_p7pUHshIYKPhDGUEWypUjv3IZzBIQVEVh73ATvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به کاخ ریاست‌جمهوری و فرودگاه پایتخت نیجر
🔴
منابع امنیتی از شنیده شدن صدای تیراندازی و انفجارهای پی‌درپی در نقاط مختلف نیامی، پایتخت نیجر، خبر دادند و اعلام کردند افراد مسلح به فرودگاه بین‌المللی دیوری هامانی حمله کرده و تلاش کرده‌اند حلقه امنیتی اطراف کاخ ریاست‌جمهوری را بشکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144348" target="_blank">📅 09:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144347">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bcdfad7d.mp4?token=e0c8NJ2_2CrZho6uLWEHIRQxNrqTeW9TcWhhrMo7sWDLagRz1UlwBx9rtxSStAS-944ROdcM-Psy12vqfh6Wji5rEQjzrnTffYIHxdlfK5TMoXFqKauTTAM6p2uj8e4UsD0rxWwxT-Y9tQ6PEbDsBjuPmY8lh_YbQN86EZHwQfy2ItfvHwMtYa-V5Fjl5QhoVatXDSPXiJh1CtyLDRkEf77ppjsp8_-8EQusPO4V2gvEu19RVV7Ex_IB05S_1zO1tMg6h97aGwczHpovMYfdi80HiwKDlD9RxPRcX33vZAkjYxyWsQYNIKomKDefWwxbulESBZJw4ukmcqMIYDO95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bcdfad7d.mp4?token=e0c8NJ2_2CrZho6uLWEHIRQxNrqTeW9TcWhhrMo7sWDLagRz1UlwBx9rtxSStAS-944ROdcM-Psy12vqfh6Wji5rEQjzrnTffYIHxdlfK5TMoXFqKauTTAM6p2uj8e4UsD0rxWwxT-Y9tQ6PEbDsBjuPmY8lh_YbQN86EZHwQfy2ItfvHwMtYa-V5Fjl5QhoVatXDSPXiJh1CtyLDRkEf77ppjsp8_-8EQusPO4V2gvEu19RVV7Ex_IB05S_1zO1tMg6h97aGwczHpovMYfdi80HiwKDlD9RxPRcX33vZAkjYxyWsQYNIKomKDefWwxbulESBZJw4ukmcqMIYDO95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط بالگرد بلک‌هاوک در مکزیک
🔴
یک فروند بالگرد نظامی بلک‌هاوک در مکزیک سقوط کرد و هر ۷ خدمه آن زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144347" target="_blank">📅 09:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسانه‌های لبنانی از حمله توپخانه ای اسرائیل به شهرک «حاریص» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144346" target="_blank">📅 09:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htvBqIWm_ThlZ1I6PNOKLi6b8NxJwXPq93nhGElo1ezVqDSbP-I8fqJjfYxP2liLWezVm7Cikr5DqzAmfegT0Om2XMimI3CzrrAUhriSv2kSs80Qmz2bNVRZ4zw1cevf6P4wbacmbW8wngvb5xpS5PjuMYaBBuIgemUVfBnUXBysQzGf_k1E_UA6zWWvYIyALdNculo5GNE7xYkPJbljCFLoSRiAev9eEN37XwyQHhZT2y5nq8_n12KiAyUT8Kn7hqqOAaExd3tZ8kfXSQq4BVaB-dAOPhwyKK0m0v5OVc2rjKUjvR9foW1H_9Ax9SHxPvtSTPWMX0DdZM1nnlApyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی آمریکا (CENTCOM) تا روز جمعه ۲۸ اوت، ۸۲ کشتی را مطابق با محاصره آمریکا تغییر مسیر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144345" target="_blank">📅 09:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فارس: ایران خارج از محاصره دریایی، نفت کافی برای تأمین بودجه سال جاری در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144344" target="_blank">📅 09:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: بحران سوخت در روسیه؛ تولید بنزین فقط ۷۰ درصد مصرف را جواب می‌دهد
🔴
دلیل کاهش تولید بنزین در روسیه، حملات پهپادی اوکراین به چند پالایشگاه بزرگ این کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144343" target="_blank">📅 09:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بر اساس گزارش رویترز به نقل از مقامات پلیس نپال، آمار قربانیان سیل و رانش زمین اخیر در این کشور به ۶۲۶ کشته رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144342" target="_blank">📅 09:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روزنامه دنیای اقتصاد نوشت: بر اساس سه سناریو، تورم نقطه به نقطه پایان سال در صورت تداوم تنش به ۹۹.۲ درصد، در سناریوی میانی به ۸۰.۳ درصد و در صورت تفاهم و تنش زدایی به ۶۱.۷ درصد میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144341" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آموزش و پرورش: همه مدارس دولتی هیئت امنایی و دریافت شهریه ممنوع می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144340" target="_blank">📅 08:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfltF9sDTnRWNRu-6sZghqgJPn2LDYNMGRg_ejNIw-fXpRvM8ov9cQrx4O812eAbMP7gjN4Xlvy5atwAbeczUWUKj25U5Sg8zVcNRr3rqriSbHH2Dj5B5nqGXusGF8fE87aHAvwLYsHlAlyqCfK771zUN6AT2hd4oAmBxk31UF0IWjdlpJB1jU3ByVbHPpscRh1UctIosCFTp12ZXWSG3_nPMWY0WCFhJDgKJDNHVyvDGhBcwLNVQIyZl0RwoBNJOz15f3QVwewkyPl8tGaGosDYE2opTBqN69BvtG2y5Nyqxe00vw9sEVonmc-RlPXg2Bge9HRrTxM0xUTP4fH9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری NBC
:
منابع می‌گویند پیت هگست، وزیر جنگ آمریکا، با دوستان و افراد نزدیک خود درباره احتمال نامزدی در انتخابات ریاست‌جمهوری آمریکا در سال ۲۰۲۸ صحبت کرده است.
🔴
دولت ترامپ تاکنون درباره این گزارش اظهارنظری نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144339" target="_blank">📅 08:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آدام شف، سناتور دموکرات از ایالت کالیفرنیا در پیامی با انتقاد از سیاست‌های جنگ‌طلبانه دونالد ترامپ رئیس جمهوری آمریکا خواستار پایان دادن به جنگ تجاوزکارانه ایالات متحده علیه ایران شد و تاکید کرد که باید به این جنگ پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/144338" target="_blank">📅 08:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس گزارش داد که پس از تخلیه در مراحل اولیه جنگ علیه ایران، روند بازگشت پرسنل دیپلماتیک ایالات متحده به خاورمیانه آغاز شده است.
🔴
دیپلمات‌ها و برخی از اعضای خانواده‌های آن‌ها در حال بازگشت به سفارتخانه‌های آمریکا در کشورهای منطقه هستند.
🔴
وزارت امور خارجه آمریکا محدودیت‌های مربوط به حضور پرسنل را در برخی بخش‌ها کاهش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/144337" target="_blank">📅 08:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
روزنامه وال‌استریت‌ژورنال به نقل از مقامات آمریکایی مدعی شد  واشنگتن با سرعت اقدام به انتقال مقادیر عظیمی از مهمات و ذخایر نظامی به منطقه خاورمیانه کرده است.
🔴
طبق گزارش این روزنامه، هدف اصلی از این انتقال گسترده ذخایر نظامی، آمادگی برای مقابله با تهدیدات احتمالی ناشی از ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/144336" target="_blank">📅 08:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTcNliFMXA6ZXmHRd5KIicT69FzpiUTBR3eYBYyB8wtvVBXZROqvvJWs05tXg7lEDcDcVwO5LaG6yz3T9JBGLfZCAKAChbWRIs355Dm4ZJ7V7YvMp8wXyVs5Jc8GcfCaYk05MFw6IVaVEiq8KSu9pWuu8jh2vzK-Wz8P78KqCrF3AeVmpYoDFEOHlUaDd2zLg6pw9XAZZkqBlRthSmvJC55Tx5p0XSevr20-ZNRHFp-PSVIXxUrOA5j6dO6TL9jWgYOG4nnBpbRKnCBG07WmmH93AzKK4ENKXaExQUxcv4l7UR1HVxtknWCJQs4jqfQjRGxi0oecsJOdoJs49xrsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: همین الان توافق‌نامه‌ای با ونزوئلا امضا کردیم که بزرگ‌ترین قرارداد نفتی در تاریخ جهان است
🔴
وزیران خارجه و جنگ در تأمین دسترسی ما به بیش از ۶۵ میلیارد بشکه از ذخایر نفتی ونزوئلا موفق شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/144335" target="_blank">📅 08:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربیه گزارش می دهد که گروه های عراقی در حال برنامه ریزی برای هدف قرار دادن عربستان سعودی در ساعات آینده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/144334" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xei0HZsSgA6J0-tVQKy4mcpy84nG7zsO242ex5ks_377fdgUPrFmE0UaxMUdbJP9mxp-VtkWAbqLVAP2bE0mUjnf2lpSAAwXcpQt5RsXQwEQpBz0tTtzgqhg-HD9Zhxg9nz9aMWssywJpMjrSc5qpsJQG1niJTda_w0s05P_gRzTanM8hyXHMSKLjMC3zFFdfomTXL_xyQPCP8VbhNcF0Sxgrg2IzYL44MWX2QWQM4a2uzQmn8pvHkOc6m3KX8qGiGTJB8nqbbrbB7t2_EGNsmuLRJtgvPmjZgJrczyUMHG14jKYxZi8NrKfr91lWrmeltXNqlpFxKVUqPvfNvecXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/144333" target="_blank">📅 01:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، محله "دواها" در شهر "کفر رومان" واقع در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/144332" target="_blank">📅 01:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeE5oV1xXKT49KjM67Kqhx72FC8hkEyDNr1m8rv4MUQKPgvQXzmkD88OldFD-XIz60L-Ex0cA4yJjmLyw8tJsZuToXjDA3JYhyQx64vVzhOgSGnHnoRIxyqv_y9AuJhZ0fgGDLvdcXoaclvoiXQJNJLtaJiB1cbSDpwqd2ttuCIYTjwN3dw2Mw_wTLgaD_6fXL47Kxq_4NjhOoylNRp7HnO-bKyqNIt9QLrmAgoCdxihm8ixFaXiGvTJunRXJg3xJtbGPpDUv6JnmGNH9kX44J3DC2tHwAFCLRcy-RFgZ-E1BXuWFY9PP_W1fGl73LjPkEUpUG2TdOsskuZDRxQAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: گرونی چیه بابا فقط انتقام رهبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/144331" target="_blank">📅 01:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKulLJ2r8CCxjJmeYRRr_xEiOQyyPD48bdKB83H-mwbOmjuTfR153aNa2VHC5H31AiBLWkIrpL-hEng43Ya0KORWxL-iMwrdvxQ65lS5Oyfwfvf6_Mrzpde6YQuYbLeP0wiY89QdgEzypRG-GxtkJg0x8e1JVuwTtn-5pgDp-VL8ght9vJEovoKd-hNTw4U_-XSfDtV0DXdd-9jikDC724o0NhkfmnUc5V7pEuH6Uacy9eBXPiS_t_HPWfVI_rOTHKz1kGk21ZSGseqdVDFYc4HCF8yF_jS5zqMq9GYlhRBGV1eHvAnbU48FVk_e1Sgv9-dy9XlH-aTESFd68ZprKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/طرفداران پهلوی به خونه علی کریمی حمله کردن و کتکش زدن
🔴
اولین فیلم از دوربین مداربسته منتشر شد
🚨
🚨
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/144330" target="_blank">📅 01:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYkudS1jNc_HnaaK60YieofscEV6osmlLlmk7FqDFmvoy33DBcC_ukZO3BUUT4dhoIn3iBhEWvGtOzRQLrnN7GIhIMGVrYIqMGQR5LOOqx4FRg82ThYnIZOMGPTKCu4Fym5GxT5mmtk7boylrn_rx4RLboHIifn57t3vYLJDhsP0wNOIeqWcgVS_NHt0qO-8F635nvaSUl0N_caxVZiNaLak5xFERA703iGMklFJJfsUwCuRnXuv7ZOs5i21FPfGziirU6s8CF8Z4dzJa1K0N4VFCNnVEhC-cxMUGVNDuFt7XLvfUz9J_K_0ZMvJHOC9Vek666AT3JcUwjxJVYR5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: پول نداریم، بدبختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/144329" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/144328" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بی‌بی‌سی: آمریکا در حال برنامه‌ریزی برای قطع کمک‌های نظامی به نیروهای پیشمرگه، که متحد اصلی آن در خاورمیانه است، است. وزارت دفاع آمریکا به رهبران اقلیم کردستان عراق اطلاع داده است که برنامه‌ای برای تمدید توافقنامه ارائه کمک‌های امنیتی به نیروهای پیشمرگه کرد ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/144327" target="_blank">📅 00:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
باراک راوید: بیش از ۲۰۰ شیء شبیه مین از مسیر اصلی تنگه هرمز جمع‌آوری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/144326" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=iH7ag0Sm0p6dP7DX3wgQEs3WZqfVmU3IaXIPOhRMdILGrHH_4g8IPWEyLBmCoLnL_AL95kIPA7vhmoyrLcEslIBNsp35sAEb1ucVE2ZxeoTXARlu5l99m1XEFb7p-p-saNRzPV5RVqJ0jKlY2y5eztpAj7emEkorDCGX97kQbZpNP7GHr_IE7F_C1ejZbhBByDQ9UC3kagxGi2fhFWX2VhL5QHsiRAc-e_2j1_iZuAddsSjweY8CjCL8TYwRnLZg-ROiJU4SWeNCB0vBwGMo8UrAK-neu_v-x4ZSY7OzVaCHVApehCUUktF0B3nbkaAR690N6eAdA2txOpVLc2NcQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=iH7ag0Sm0p6dP7DX3wgQEs3WZqfVmU3IaXIPOhRMdILGrHH_4g8IPWEyLBmCoLnL_AL95kIPA7vhmoyrLcEslIBNsp35sAEb1ucVE2ZxeoTXARlu5l99m1XEFb7p-p-saNRzPV5RVqJ0jKlY2y5eztpAj7emEkorDCGX97kQbZpNP7GHr_IE7F_C1ejZbhBByDQ9UC3kagxGi2fhFWX2VhL5QHsiRAc-e_2j1_iZuAddsSjweY8CjCL8TYwRnLZg-ROiJU4SWeNCB0vBwGMo8UrAK-neu_v-x4ZSY7OzVaCHVApehCUUktF0B3nbkaAR690N6eAdA2txOpVLc2NcQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: به دنبال این هستیم که برخی از ادارات را دورکار کنیم
🔴
حقوق پرسنل را کم نمی‌کنیم اما مصرف سوخت و انرژی ما کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/144325" target="_blank">📅 00:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کی‌یف بیش از دو روز است که تحت بمباران مداوم قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/144324" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/144323" target="_blank">📅 00:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پزشکیان: با آمدن محسن رضایی، در حال نزدیک شدن به یک زبان مشترک در دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/144322" target="_blank">📅 23:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlatekfo9CoW8qTqxW0rRZVgF5WxSfzUObcbShYoN46g0BMzQMlgwRynVezF553Y5Wo04GFxmBBly_T9VaVWBx4IcVEbo14nw_NCf1vpMw2GApdfZhWIUDiodXPB7WcX33idkvSruZ4L7PgDhY1YdcEb_YyTrNUy6wHrj5GbexI0NKUcChFqbLVJnqqLLLa1BOjtx1QwHrX4x4pI1Pv26vuMCHwOR0a9rgy-5epAi9k_cQKIIm0qPlP6XoxphBLyjT33j-Hk8t8zBGKMzOHrsbESSqocnZ3yYIJFUnkMXTMGgq7ATC1SOB7NAjbxf-Ome5pZqEQeQ4tQscpvHFnqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=J1RxuN8YpCrmnPnTUVZnFpeheploqfaw7I9smRrWXj7nZPFujLV-fPsSi-PT8ohbWFdyNgqQSedWLyUjYAhuoLyJYB2LzRkUivXMZ8VX2TW1WIISLpSEYFNNfzHrTR61oZrYGcXAAd1nVRAmWg9nTBVeOpBtXsRpGvzYi-iurDuPWOQ8CmDiJf9DoiYk4jeNyogbWqmDmVa4iTcMaPpYWpnV0DPj2DAh-Bhj8pokQCOj2GT3jOdEI6QywF-J0DpXHX2xxcUg-6Kl3hMDzh9P2h5MSeT9Qo390RbPGtgGNZsIcYvfHNpVg0oYDgdHcfQOoW3_OT6gvrsK9vrVQ-UnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=J1RxuN8YpCrmnPnTUVZnFpeheploqfaw7I9smRrWXj7nZPFujLV-fPsSi-PT8ohbWFdyNgqQSedWLyUjYAhuoLyJYB2LzRkUivXMZ8VX2TW1WIISLpSEYFNNfzHrTR61oZrYGcXAAd1nVRAmWg9nTBVeOpBtXsRpGvzYi-iurDuPWOQ8CmDiJf9DoiYk4jeNyogbWqmDmVa4iTcMaPpYWpnV0DPj2DAh-Bhj8pokQCOj2GT3jOdEI6QywF-J0DpXHX2xxcUg-6Kl3hMDzh9P2h5MSeT9Qo390RbPGtgGNZsIcYvfHNpVg0oYDgdHcfQOoW3_OT6gvrsK9vrVQ-UnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار بزرگ در کی‌یف، در نزدیکی بزرگراه ژیتومیر، پس از حمله روسیه به یک انبار مهمات اوکراینی رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/144318" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
