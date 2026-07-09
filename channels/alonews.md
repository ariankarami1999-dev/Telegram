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
<img src="https://cdn4.telesco.pe/file/qRS-uAkzLeqVWn50OxhChxm-wHS6G6XWyB9bIZKZAHeLP03JKx-bm3B2CBBjCOuHv13uOO39Kya2DeGEy9QprTUHHTQ7ck2Wef4AK9Z-oGbL8u7k34kSuASUGNUhu1AQ-nWBuNjPhubPQRr-YhfVLPryQsZSCHXgxYT12kh9GA3X_Iuo0jJdWr_aGh_HcJbbBd67zhOPPttWi8d76HRNSWbtDREJy8-lXNYznHXAx6eZdkWUWApogTHg-5VyVZuiUBY502wrR1H8XWfrieFCKUDVqTtYjERZttBjiPFcWSUkfVqR936iI054xBuWmDdCRU_xve6Eob99BvFw13mjSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-132808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دو موشک دیگه از ایران به سمت اردن شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132808" target="_blank">📅 15:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkaVLJTT-re3ARmr7HkVeXK2qqN6A6JgvxitBg5CI6LsMYPz1HZ21q2ibOOQfIzWeBS8I1IKw-XfSLecPIxar3DpfPo13IooO4WbQHkyfBoCZfsMUA_OzEPUUrdebYJK0FY7ogfX0ey7RctmybYQVLi8RVDcDyLw5zbNNNATfV8pjynF51rooZrjciO_HML9f9gsUHAkVi295-Z4-bHeuXyHQWH6u0Eaa_AVgjt47FGatd9XqY59OA1szNJ-GylOaeFYOw748NM0h8eC1RFoGJg0v1stGbNvfiGDdNb9QnSeaP6D2e97yX0vRKrBPH3edht4BRdLyIsKqNdjzAWMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گشت زنی جنگنده اف ۵ نیروی هوایی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/132807" target="_blank">📅 15:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTaEVwcF3Wh0-wHb0mRe1PKVRHPN-a0wPKTAxOI3TOX6aNjakH1qP8tHrNvUI8-XHyMDqZdn0PzXNv9US70r2keXW91IZW_pAmHZqg9P7M96wXLcG78tVzWkzPDynDEj716B7PZUsjDOxtpzDy1Vn_j1GdjPwOx32VqLy6ZdT5OtV7ul8UWMT9xZhqzEIpv_iYxonzkPW6hb_kqnjbMhqhnY8ZZoiShqmk8mNaDKGOphZWlR0ExK0nrjZWNl7qAe1RpJvnf-WkSQ0yD1Yhr0mlPcz4BDAqMaTjUJFkVTbV-q3D-tZgUXXjsrCjvxIH7LBYv-jh2SdrSO68QJsDVYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlIttarHFBYpoNr5glMtFsqk6QZS7qAwK_zpDkiMX2viQWEZCBaNvCIPbgL8rNv3ELsf9FSu0NhBXlSgvUylfHl-g7J52pFxzpewDsJygHfbjZtw0uIKZjh04ODvg2Bqb6-PulqJAGqbSzmEQpjwaJaHsAbwPmeVr5HbW3ykiYyMFFOodQh2eRRfGsnC0z6Mt-iU_zWEo0mLH9YeMs23J7Vk3NH1E1EJdAPJnk40B4MD62EL5O8I-48Dvffrfxt5uBIwq1cxBPfywhakzyOPIlzs0RCwSY4xnUBKbWD0Q_8wyW0HUCf7DdAaoVhuG5_F12BtQ-kty-_PbuPy343aRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شرکت هواپیماسازی متحد روسیه (UAC) محموله‌ای جدید از جنگنده‌های چندمنظوره Su-30SM2 و هواپیماهای بمب‌افکن جنگنده Su-34 را به نیروی هوایی و پدافند هوایی روسیه (VKS) تحویل داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/132804" target="_blank">📅 15:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc5EdW3WAwI2p0Z7-wYXqo2uVcogQ7kc3PGQIuesF1R76E5OZj_g1CASKlEG1pNoGfByEJ-rce3fhNVk0BC5BrUavZMeIQG4XOs0DS_L6uCzZBP0Ozkj-oX5dIAJDMv2C6dU-EZM2CHWvn8eQAuXoT43TisVis22sau6zcb6y_IvLOmCstMd20lfGpjuBfEQ4UlcYrxEyx-EypicHgQlclc4Rpwjtdm0fJ_eRqAI281KFGX2U07iI0P6-5NnWDhe-Cw1Q5ZgpuzU2LeDNa1XvRwsZdoYztOOW3KFl64CCJTaGuF281cxgPk9mO2ulhKcpepoSG1RykMouEsz7wt5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ داره بصورت زنده از تنگه هرمز گزارش تهیه میکنه برای صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/132803" target="_blank">📅 15:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/ آژیر ها مجدد در اردن فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132802" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2e74886f.mp4?token=uFvRTIU4tsjrLfLzHlZ0IwsYiJkiKv-_yPja28qnCbfcSjq8px_finqrap1q3zsaAkEddumtXpuZKCtweJer3aXhk6O24x1-9XbJ6FJCaIT9J2_D9_lN39EgRhUMdtqJnb8yfrwqg9R4HXxF84KVQm60iPP49SvWDMTnlJiBlupuqWd96o368hEJnAjJV3kCy6k3attQtkP-YBmSkRy7aCItTnLKOF-56pnnGmnbiCUaw_h4NiCzq2GO2ARQerJKj5DygLMQQwRWjk2NcuPg0oyLptUCVDn-jzXRtJBwW7DQChV2bTikxrFbkoWHzFfDAMQLXJ5q53NBtv3MPNOdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2e74886f.mp4?token=uFvRTIU4tsjrLfLzHlZ0IwsYiJkiKv-_yPja28qnCbfcSjq8px_finqrap1q3zsaAkEddumtXpuZKCtweJer3aXhk6O24x1-9XbJ6FJCaIT9J2_D9_lN39EgRhUMdtqJnb8yfrwqg9R4HXxF84KVQm60iPP49SvWDMTnlJiBlupuqWd96o368hEJnAjJV3kCy6k3attQtkP-YBmSkRy7aCItTnLKOF-56pnnGmnbiCUaw_h4NiCzq2GO2ARQerJKj5DygLMQQwRWjk2NcuPg0oyLptUCVDn-jzXRtJBwW7DQChV2bTikxrFbkoWHzFfDAMQLXJ5q53NBtv3MPNOdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / هم اکنون وقوع آتش سوزی در اسکله عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/132801" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مجددا صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/132800" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حریم هوایی سوریه بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/132799" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل: وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/132798" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سازمان ملل در پی تنش ها بین ایران و آمریکا هشدار داد و ابراز نگرانی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/132797" target="_blank">📅 15:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/132796" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
توقف دریانوردی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/132795" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار های عظیم در اربیل اقلیم کردستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/132794" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیروهای مسلح پادشاهی اردن: ما 8 موشک را که از ايران به سمت پادشاهی اردن شلیک شده بود، رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/132793" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTjPjqHypxfh6Ht8IdSDVZvaTH2keo_IB1IUOfOBq5F_BzBnpEqzRAV5cmGSw-H3SMT0kIutoWnKy4tfoQNtCjljDM7yqS-yBun6IY7S4yk9iA-NJvBaqTRLejdKUxOvWdbfrbBEPBefAY5bcXGD1sZzHgpqBJm0nWSHSCJmVfQOsG416ZOo5135J2hCtnn9nU-DWdG6f70QKgOIrtHfFAdEucTNLg3OpkTPb9LwD1ur2nu1IF_3hGCEB1uA4tHHpi1mKztGCcpB6--VVpt56kxJwpQyZQLZJUKiBugKALnSGiI5MDRZ8MGM7X8BHa3qi4Lgsx2NYq3rizLo0Xcdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxgFy9AZTf4vBeNYZzOHdrz58rAPDRnkP-7U7ucLJd0ZuC2taTUGVTKSPp_KRve7kcjxiFnZSbmTmXQNCLyJZjTDpTaUI5Blq8tXD2-iUDYS7NXEflZZwP6AOhjTV59_3V6lwzmWjHmm-TGI1T-vjY3FLWflD9YrdkEWzkkRP0W79Oikz_-ykX5Bj6iQ73NSvIz5jTRQ98e_sC0uROtekQ5evTNtoVeteGCuYDMruFvot3jN2UBVZmD7qdJeSYV9U6ScSU1JtJZKibKOsMWl24e-_CQQd-7mmnB5lpaNIwncIhu5AppE9Pix4jgU1Jwrbd6FpGv5AW8B-NRFqZdbqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از حملات آمریکا به عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132791" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عربستان: حملات به کویت و بحرین رو با شدیدترین لحن محکوم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132790" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
صدای آژیرها در پایگاه ویکتوریا، نزدیک فرودگاه بین‌المللی بغداد، شنیده میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/132789" target="_blank">📅 14:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293667c56d.mp4?token=BzWkceT0d344GfHASc1UoFrWeh9bZ0Bo3NfykIooPXeVD_yw8ScP_rmcbx63b5wtdJ1MDerqMEZ1sA6ucx5CYqetUdDldkTVLReBxTu3ILd6R4ZlG6IjjJGkgfojYgJlP_7XHuXpR2_SFstITmKbz4EW70A_oLkF9VP1X2x0uMuKiOevb-g-B0IG_C1Wv-cgBe6U3fQZ0535sD21mEjRRooPrL587QZnjii9W5AgHMbqbGDUC9A8B8DM3GI0rfyn-gaf1oGFLQJnfIuJUVq0uqKF6bm_BnzeuRFTuK9Odpq4WZX1n4Dx9f4m1SfYZ7iX2FolmbtQFbklroWqe1tK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293667c56d.mp4?token=BzWkceT0d344GfHASc1UoFrWeh9bZ0Bo3NfykIooPXeVD_yw8ScP_rmcbx63b5wtdJ1MDerqMEZ1sA6ucx5CYqetUdDldkTVLReBxTu3ILd6R4ZlG6IjjJGkgfojYgJlP_7XHuXpR2_SFstITmKbz4EW70A_oLkF9VP1X2x0uMuKiOevb-g-B0IG_C1Wv-cgBe6U3fQZ0535sD21mEjRRooPrL587QZnjii9W5AgHMbqbGDUC9A8B8DM3GI0rfyn-gaf1oGFLQJnfIuJUVq0uqKF6bm_BnzeuRFTuK9Odpq4WZX1n4Dx9f4m1SfYZ7iX2FolmbtQFbklroWqe1tK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک ایرانی در آسمان اردن در حال حرکت به سمت اهداف خود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/132788" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گزارش‌ها حاکی از آن است که حملات هوایی اخیر ایالات متحده به اسکله تجاری و ماهیگیری در منطقه سیریک، در جنوب ایران، منجر به کشته شدن ۳ صیاد و زخمی شدن ۱۵ نفر دیگر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132787" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/132786" target="_blank">📅 14:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دولت اردن : موشک‌های ایرانی رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132785" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش های تایید نشده مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132784" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرگزاری رسمی اردن اعلام کرد که آژیرهای هشدار پس از شلیک موشک‌هایی از ایران به سمت این کشور، فعال شدند.
🔴
این خبرگزاری همچنین افزود که نیروهای مسلح اردن در حالت آماده‌باش کامل قرار دارند و برای مقابله با هرگونه تهدیدی که امنیت اردن را هدف قرار دهد، آماده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132783" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
منابع عراقی: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132782" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRo5gfftrqZb1wDtt-PgFCge8eA6rTrAULXcbK1Njug6uJJvUEJBAt_KxLoDvLXVk9youxpJcj-c9W5NQ6J4w9GqgrdIi2lXpUXtulJRvBSKoT0HHsryKRzNvW9MxOJRVjNkZF7qoIPCtpKFw5aGuPvXsHKC0vXbZvpUsl0JTYS93vGHuIR7EDJS0dBj6nQUqpa92jJegu154bspOvMI66X3PXVp7UIYuswD1cfatdF5cLamS7BlnL1u2F339GeGWyGCS_dfkjHXBSljGiXHOzsJ-9hW9-SOhpiF5kc3suRY4YsRCgp9-BqobucNkvJUChqXcS3OxzyZPdTxKcuk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
🔴
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132781" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رسانه‌های اردنی: یک موشک مستقیماً به یک مجتمع صنعتی در شرق اردن اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132780" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132779" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دولت اردن: حریم هوایی کشور با موشک‌هایی که از ایران شلیک شده بودند، نقض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132778" target="_blank">📅 14:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiSfYDcNNndX9atcoj2dgHwcgQSCH8J6PiIt94KkaOS3GVKdHhlS9hsao6BAEtFC0PaJncV-7k53Ot0xqWnct3JrbP70qAWyWqa4ZFiGQ4P_Ui1caz3b-NrMZpBjKIBQJxmOr0l2HlzwJnIUeCtzlFQAGezYI2iTOXav1qBs2LmKLegnlYSsA9O5CsdaK-X53CCxZBlgfSSirJQ_Nk-ZTD4DPFXGGB1r5mN-nnQqK_1UmA7WfXAxSxf3TpBr-U_fGFHH1kuwGcCbobvxKs9JYrMCX6qNDonxn5_CXMYDm-Eeyjlkr8hXUwBQJ9Anq1WBXBnxcgAQUKpGn5rFJXTq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFhkrxmfKtrMTaNeaMLs0TUwsRQ1siaiw4IgU4ICjIYDTUaubKZSf-tSrUNUDyQt01tLD4LN_-CpuqM0z-JdMAEEvwFggbVvvbpj1KjH66PN4a1dVNxQXLp6DedM3iZRRhSw-CBECfnhD63wtPKtaoOpT9q2Owt13PhjgODUhpm8kfcCnTNVwcxMUf7c3VmzKmp0xbbxhLD2OdI_JMbhx2Zst5cUfo23gsv6AWjbPeUFEWDjzYAZI7cvJRjUDz_qimtvp4qqMVdhpXo3-kXufA4z7jc1mnAxWOOlQiS5I_XDOWxd0xeAc8rNzkFeHfAJ8alI7N67EBD6Wvuam9NnCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دقایقی پیش، شیراز مورد حمله قرار گرفت.
🔴
دود از منطقه مجتمع صنایع الکترونیک به هوا برخاسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132775" target="_blank">📅 14:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صدای انفجار در کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/132774" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132773" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9jF4Jf5XYGjYzYF2esYF8UoGQszpNnGCgF46-TYk8imtEUvjTnl8ymHol9HHvhCmzFxahY0gs2sKiQhEWm97CZ_kCOOQT3G2AI-gh3FwQ-2j8hjq7gI-nf4j2cGYOOOJ-sDMBIuuFULDCPYpAT9lu2q9LYPthndYrTxqlB75uPmFIoq3yQg134S-4Tq8vHnkkfjrWon3m9_GO-5wULKSOC69MRe1SExqM4tG3Pp1d3dO5VkqUOc4LxTDjpKEz461yNlRNTaM-ZhdM6g-QYyGIe6pW8YiVC2YnRb9TVz-3ZY8zRWmZ5wAznbixMl_uibsJIddF5Cyla8b76jNzmW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده بوسیله موشک‌های کروز "BGM-109 تاماهاوک" بوشهر را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/132772" target="_blank">📅 14:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / سفارت آمریکا در اردن به دلیل «گزارش‌هایی مبنی بر وجود موشک، پهپاد یا راکت در حریم هوایی اردن»، دستور فوری برای پناه گرفتن در اردن صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132771" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / آژیر خطر در پایگاه هوایی تاجی ایالات متحده، در شمال بغداد، عراق به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132770" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DabfTgTGkqfi8wO2M3gcXzbqJhvUd50-ChllXym8isTaUh7H2v-WhHDtcKcWVBQgDJgyIJ1pQDs5IDZ3YF6zW74M97PZULNtEQ8U5ApxlZmWKjjXxcX0AM5FGIuIJyUvCnrNEemqXKmT4v5bA0purYqLEW9aYn76atIkEUTqizoklvBtg8gB5JN1CrZZBfxeMrI8KEgsxB2b45qE6DuMIH7B4hxJ2AXPmpainOipEW29RAjDCE346Ht6HW0nxh_j92aeoltjaz9ZXK2tSxEtu4mfUVuMIz7STTOE0wB9xvh_o4tckHSoA6vaawBLVvYwwQV7O9fgXKEOxfYiPWJiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک از استان مرکزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132769" target="_blank">📅 14:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد که پنج موشک ایرانی به پایگاه هوایی موافق سالتی در اردن شلیک شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/132768" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0kQ-FSmXfmNuR8DbeofH2rIReOS6RPLx_FHQd5XSuKWluHZcYZN6uYP8s70BIU86SF2zUxA8sofPSrr_z5mQL8c2PVAHNLSlyQfVtjNfPs-M_ZhFrJzYv4iENOUr5Mij3dKDFcJLDdDs2b81xEHOdbsHVwzvNvVB2p_3Dh3b5oM80YscOdeVIvqRA_9chzb1QAWUX2b_3KxmrLPkoL-Qownp0eq4NuHtD_OyBM3Qe_RdXcwG1dc_WMz_2FbsPU66-zMFwONO5w4EkQmu-Lc9prQfNEsBvtOFgsfe5zmc8HJxz9WJgl-vLeoYoCIKfw8qrFU2ACSLNIsA2rxo2bm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک از حوالی تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132767" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / وای‌نت : یه کشتی جنگی آمریکا تو خلیج فارس مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132766" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfdb50915.mp4?token=uVtw1y3LUhrXXca24RUgZROBIudiJIIUBIxrWpGbUjolwbYDPOF9Aux6ZCFk9XMc5tiHQwyd6F6j4qXhv1f5JqbUFV7dY9bAelWZDBnGSBUe_IWGJUWgHjeeVo9zFOjCDL9K6NVmcDRFfRDxscNN5_IAgv86NnPE7_Ch2JDBAJjXH6lC9kPOTHR6gugDi0lrjdQsmjt6YBh6GsGSVYwSAQAWr6aPivsb6sV2mWfQPSgnxVms_xSIQ3trYpx6Vr0GhQREjg84j_NsfqXVKf15UTnwQuMEN6emsgTx5rbavxX7M5Ua_7oavYcI0THtFIdP8jyfXVgOeSj5siHr1KIFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfdb50915.mp4?token=uVtw1y3LUhrXXca24RUgZROBIudiJIIUBIxrWpGbUjolwbYDPOF9Aux6ZCFk9XMc5tiHQwyd6F6j4qXhv1f5JqbUFV7dY9bAelWZDBnGSBUe_IWGJUWgHjeeVo9zFOjCDL9K6NVmcDRFfRDxscNN5_IAgv86NnPE7_Ch2JDBAJjXH6lC9kPOTHR6gugDi0lrjdQsmjt6YBh6GsGSVYwSAQAWr6aPivsb6sV2mWfQPSgnxVms_xSIQ3trYpx6Vr0GhQREjg84j_NsfqXVKf15UTnwQuMEN6emsgTx5rbavxX7M5Ua_7oavYcI0THtFIdP8jyfXVgOeSj5siHr1KIFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132763" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / گزارش ها از نزدیک شدن جنگنده های اسرائیل به مرز عراق و سوریه خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132762" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132761" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/ صدا و سیما: یک موشک آمریکایی نزدیک نیروگاه اتمی بوشهر را هدف قرار داد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132760" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گزارش‌های اولیه حاکی از حمله به یک مجتمع صنعتی در اردن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132759" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=heAnheaCSubNg-sChvjp_9U4oap7n6FTEavfOfyvNCUpSIGBqFphn-Gh8hXyI45yodz4lUBk7BfaGLPjdncwyd-ZvCuxAPaHJRlrqyinfJKl0YDdjx89mZoqFnuy4r13f26VvjyK4Vsn3224fyIeCmR7zMzXHvYQqqIIDqeoepIwqNhu9BGvzcqZUXHpKU6V70ksrN7xtPyjYfUJDz0wacszT6WsV5smxsQc3RrkT7ihC2MhMLzrOmwN-qMWsDx2Lbq_7JRRLhLBli0T11-dtfV7scEJjNVoWhh1WFq8QV6zbe-Ea9QK9K4TgnU5-GnND8nWzG9gAcY0PKGnS2MTnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=heAnheaCSubNg-sChvjp_9U4oap7n6FTEavfOfyvNCUpSIGBqFphn-Gh8hXyI45yodz4lUBk7BfaGLPjdncwyd-ZvCuxAPaHJRlrqyinfJKl0YDdjx89mZoqFnuy4r13f26VvjyK4Vsn3224fyIeCmR7zMzXHvYQqqIIDqeoepIwqNhu9BGvzcqZUXHpKU6V70ksrN7xtPyjYfUJDz0wacszT6WsV5smxsQc3RrkT7ihC2MhMLzrOmwN-qMWsDx2Lbq_7JRRLhLBli0T11-dtfV7scEJjNVoWhh1WFq8QV6zbe-Ea9QK9K4TgnU5-GnND8nWzG9gAcY0PKGnS2MTnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون فعالیت پدافند هوایی در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132758" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl_lxNdGAtawMr489VH5vKWKGf19as4IlzLcbAC4kd-WTG2-V5gc9ebB3ivvsd6J23atcfBY1i3oo6a6bnAtVRdTASjWtQqPzXo1nF1HtecJh9QaQ3Vki8Ndr9slj3lamgMqZxOYa-Laiyo9g_rGmY9LAkrYjVGY_rDxFlcOZ4t7wbUuxVhWzW55XMvncxnhysP4rFe_w2AOhofkR-0xYGBDKT1XciG9iALnyRpAUv396xEE-HmLbiaxquVkmE15U3eWurCpJHJTooRtpUSB4-1zZDhp3f2jYBf4Ug4aSFtg6ou35zl5221Y48eAg7A8rVTBxh3Qk04J-up7zbOxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: ‏تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132757" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: یک مسئول اسرائیلی گفت: ما طرح‌های تهاجمی آماده‌ای علیه ایران داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132756" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132755" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
صدای چند انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132754" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/ هم اکنون آغاز حملات موشکی ایران به سمت پایگاه های آمریکا
🔴
آژیر های خطر در اردن به صدا درامد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132753" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/ صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132752" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzaUyfkdWkt4y2mtZsJCAq4ZN-R-CRpeNHhftoIXhSCCo38pRRP4BXY51PhgU_EIW44TZw_l6vuENlsyvVQa4PWTUwDQ91HzeXaxe1MLNz9T0x93p3Skb76bgyZ35X3Xfn5W4JEyblo7u_ZEcXTneHO4ZWWssr0kt4DaW9lDw3vvyp5LMdpfAbTFfU3EAnjJU5TwU8sjtq6slZRzg0z8lD5sKShWrwoU4_VVYRMIyKWHOc_eoKYvRtIGPtXPkh7SWnAqZh5UJjPSnLa9YYQ2L7Pa8yfWSMWs0OsEVP6hVr8bXuIKkjJ3bkaKAFPgSOMHYgdZxdgL2l83w0aUUZyNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132751" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/ هم اکنون آغاز حملات موشکی ایران به سمت پایگاه های آمریکا
🔴
آژیر های خطر در اردن به صدا درامد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132750" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4823c17261.mp4?token=HyAsEba4qDxbr2ohPHqdr5ZOyZakYlxULTkwNV2qnmtHkoH7Vfr880Ilqt6srBa9C9FrHfVEWl7lFNkZB4Go5cSyfO_f1HgseaheUU0JjruugtZisAGA-LNC6f2bistBjwuNprBIY2WUSqa6CZu7WW8TQLAK_ZX7JRSP9m3FpAG6jV9RWUEm5tMfVC8G0-Cg3lmSrFRBmOopjySvVyKl-qlYQ5JT0yFxeROQT9CrIv-NyDPh5l1E5fMGPyBm8AcSMVR7J3wHgbxULypY3eT5cs9_OrtMTliOs-a4lkBmfo0b5B9GlQvyLjuFXAQrTvfiKh0g1vhZSoQMKlQfGgbUtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4823c17261.mp4?token=HyAsEba4qDxbr2ohPHqdr5ZOyZakYlxULTkwNV2qnmtHkoH7Vfr880Ilqt6srBa9C9FrHfVEWl7lFNkZB4Go5cSyfO_f1HgseaheUU0JjruugtZisAGA-LNC6f2bistBjwuNprBIY2WUSqa6CZu7WW8TQLAK_ZX7JRSP9m3FpAG6jV9RWUEm5tMfVC8G0-Cg3lmSrFRBmOopjySvVyKl-qlYQ5JT0yFxeROQT9CrIv-NyDPh5l1E5fMGPyBm8AcSMVR7J3wHgbxULypY3eT5cs9_OrtMTliOs-a4lkBmfo0b5B9GlQvyLjuFXAQrTvfiKh0g1vhZSoQMKlQfGgbUtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از زنجان موشک پرتاب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132749" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsW4VsYyR8oUCGQuDwXOnRtni_2mfXultvkPQvFcuZpWUJHlFUKltr46aW7K19YCumHRsMs3j8k8pveVYRd0y2a-Gg_dBLpZbIFv05QqF4f-41EaOuip8vf7InhWLi4OXo4kh7SE7cvqgU7D57M1Y52Uu60qTyq0-UPGab43lix5RZA1qcqtafL3UFafjNCXUhVQqHRnyBJnMbR6uuRcmuDWdIs2hAdq6IIo3OkzEm17aurBcg2xjhk42wBD_y3UZp9G3ejnAHwx8hhICqsjBFETZnx96-cusQ6FnVX4Y_pawi5zOUm3y6c2WlvgyTerC6heLt0bRFpLSW81j1sSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132748" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دوحه: گفت‌وگوی تلفنی وزرای خارجه قطر و ایران
🔴
بررسی آخرین تحولات تشدید تنش نظامی بین تهران و واشنگتن
🔴
نخست وزیر قطر:  بر ضرورت پایبندی تمامی طرف‌ها به دیپلماسی و اجرای آنچه در یادداشت تفاهم آمده، تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132747" target="_blank">📅 14:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d87ca9107.mp4?token=LIncYJneqFY1WdQqGzu8J6ZwUoOT-N08kt0yr1N9tq-c2K2AE0op3zT5AgCYpl5tsr5tqslby1ygc7lKIoxUcwRNOs6iaVSv_Fozh7wly-gYlIKBn0R1uVRvf7xI4uZ_Kn2kCkzuw-DGubhOSbWUNMtiBdzK9L8yVSpvME3tVgMfREl3nZuGc1iSa1utbXQpkfgzqOkw-2xlh7JHSW4MV9dO6ZCA5tLN8N_1cXhz6l7ZhbSeG7_eAH__C1-TR1Zd5JbSurJKKhp_zRcEcN7p0DVHEIjJBDGdraXQ3B52kZvm6SEp_p_TGkpZDQs1_ZBcQcZak1bapwa3KS7mffHhGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d87ca9107.mp4?token=LIncYJneqFY1WdQqGzu8J6ZwUoOT-N08kt0yr1N9tq-c2K2AE0op3zT5AgCYpl5tsr5tqslby1ygc7lKIoxUcwRNOs6iaVSv_Fozh7wly-gYlIKBn0R1uVRvf7xI4uZ_Kn2kCkzuw-DGubhOSbWUNMtiBdzK9L8yVSpvME3tVgMfREl3nZuGc1iSa1utbXQpkfgzqOkw-2xlh7JHSW4MV9dO6ZCA5tLN8N_1cXhz6l7ZhbSeG7_eAH__C1-TR1Zd5JbSurJKKhp_zRcEcN7p0DVHEIjJBDGdraXQ3B52kZvm6SEp_p_TGkpZDQs1_ZBcQcZak1bapwa3KS7mffHhGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که ترامپ از بمب افکن ‌B-2 تو ثروث سوشال پست کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132746" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / گزارشات از صدای انفجار در شیراز ، بندرعباس و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132745" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / گزارشات از صدای انفجار در شیراز ، بندرعباس و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132744" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نخست‌وزیر عراق : به‌زودی یه همکاری سیاسی و شراکت اقتصادی با آمریکا اعلام می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132743" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDSTSU4L78i9QHIJVDgAQVfo51Lry_hfbsk9cwQt0iqjGGGAZl7Xb8mPLaoAuAWWtR3qSukm-xmLxZnh7sWYNfiJnpD7G4mUOI8OTp4H6Mpd68Qhr42Gcs6mkT_uhQSxV0d-w_VVgrbBXfXxz18R86bRf5qIdzFFyYWFliC9VOMiqK-T97HINyNx4nkFwraa2QnMGdcxqeBAI0Nx_YjaS15ofhzMcSjmL2p_dSPKgVW67Pr5rdjHAvd2xPDx8jVJW_lFAEmfV3R3uMBGE2hIdqsvtJNfBYyC4rt8p3HZwRqTa_yTozgO6yyUrEIXV_50bW6qkh157EcD0inDVo_mCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس: کاخ سفید داره خودشو برای یه درگیری با ایران آماده میکنه که ممکنه 1 یا 2 روز، یه هفته یا حتی یه ماه طول بکشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132742" target="_blank">📅 13:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRpNq5Owjf2pnGcKb4159Vxz3ZTpgEpXtB9M9IhUYtEDqHk2JtwtSSOt5gCl3kPbMUllHqyR4AyAqb5oYiNjHgMEs2Hpx6fe4lMds71xYPm7Ph13qJeZ2RfyVI8sxoK2vaiyrES_KXFZgjuGd_4ANiSjR1ssGfBcqsOgNXvI7aplu4oj11JWBCRXzlPFpLFFOmLxgu7v6pBHEsVg_4Yvf94uZDDHjw6KZB1s5FTkD3GFxvee5Nh2pOANQ8AcW1DrYJSd7X_TCtmyyWSEf_FEOojEzvVfwlEWJA1ZPz6w51DXTLRqtMOKTtQQho64eqZ969cnZULKJG7OfS7jaSunUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی نماینده مجلس: اصلا انتقام حضرت آقا به کنار اینا حتی جرعتشو ندارن جواب فحاشی های ترامپ رو‌ بدن؛ دیروز این همه فحش داد به همه یکیشون پا نشد بگه آینه آینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132741" target="_blank">📅 13:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYHvqr5nFgQN3UjAzIt5JL1XFkEo2OepEPaWsNYH_pvAD71oNlIZHSGn5xeiVc5jMUTkOkrujtUO3X2u7-RZ8MjRJzS0V9WMK1gOmeofX4Lw6cEQxeuEye6hPNBZX_B2XCryKZ1KVqOiWk4xeqgWUZ4G_OU6UH29lWc5jWntssKmOSOWc4qYwQxkb2dJuuZHKxPyHkOegAQ8-daquqBzpU5S8My-1RqKhIcw5RsF85VNehONzq2miV6hqxDiDk54E9fAz34pfuqBCTdZcBFUd2mWO82_pmGUy86C-Tbgdd3MBwAVD5OCKCnHi2dX3_-ZdV-7R5zzGSJ6FB125HZtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: منتظر سیلی سخت ایرانی‌ها باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/132740" target="_blank">📅 13:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دلار هم اکنون 181,200
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132739" target="_blank">📅 13:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای چند انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132738" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مقام آمریکایی: آن‌قدر ضربه می‌زنیم تا باور کنند ما جدی‌ هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132737" target="_blank">📅 12:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نماینده دائم روسیه در سازمان ملل: رقیق‌سازی اورانیوم در خاک ایران یک گزینه عملیاتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132736" target="_blank">📅 12:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqvbPKYLTzbLvY7CKAySHfq_PAcZgBemT-RYkkMq4827Kpt3Vl05IgG5vkldpkE_sXkQTFCDJG41El-IhjAHQNvKm91Idl29R0F3hSfCakn-Q9mKZfC06prMkQZPg5XL28MOUq8Ienjg-ptj56PO_rBmEZPR6AmLX3nZDAfC42pYs2lO3jK5eO5NdLg7yyEji4QxrkLyP55MrzFmdASO8kNBnLlvFz2WH5eOBk37ZtiItugwOQUbqID342GehTFXDeLF9A-7AdlV4SEHPbGdbdmJMI6545JDZ6jVCfdkzEmpAA5pXrguHOYpsa0Reh7BrphUlnWARFrmr9K8UmUqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس: آمریکا بامداد امروز پل کریدور ریلی چین-ترکمنستان-ایران را در آققلا هدف گرفت
🔴
این پل روی مسیر کریدور بین‌المللی چین-قزاقستان-ترکمنستان-اینچه‌برون قرار دارد که از مرز شمال شرقی وارد ایران شده و از گرگان به تهران متصل می‌شود.
🔴
این مسیر، بخشی از ابتکار کمربند و جاده چین (BRI) است و از شهر شیآن چین تا تهران امتداد دارد.
🔴
در سال گذشته حداقل ۶۵ قطار از مبدا چین به ایران آمده بود و بعد از آغاز محاصره ترامپ ضدبنادر ایران، به گزارش رسانه‌های خارجی، تعداد قطارهای عبوری سه برابر شده بود.
🔴
روسیه از آبان ماه ۱۴۰۴، ارسال کالاهای خود به ایران را از همین مسیر ریلی آغاز کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132735" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3qpauOvxYTCt6xo67F0FZW_JMzraaDvKX4MBompTxrZwQDvKMJCI9-2uUkqzhvQOlmx6AB-dzvB9ef3N-IlmkpLetQVTZgnqzMw7mpiTqp9A3H6jT2V2axKhb-qUQJLmAMgSDy8xuTfBAkL1Txr-y-5YbXteg5xB4068E9IbAwbh4F3JsPqqFSqFfERnN3p4O8s7UMlp76z7fQ0U0QuunbbwAjRk8dQ1p0Dp88Nthti7RkfVjCan3pS-Pf_tntlN-Xhwgk-gk7cj3rWF9jozrUhc-se1UBzACcamjG5RSWGjQ0zZFsE9mmhaSfQU85d35NvtI6dXwxFU6xbt2yByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع کویت : امروز پدافند هوایی ۳ موشک بالستیک
🔴
۱ موشک کروز و ۱۰ پهپاد مهاجم رو که وارد حریم هوایی کشور شده بود، با موفقیت رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/132733" target="_blank">📅 12:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست وزیر عراق: ما اوپک را ترک نخواهیم کرد، اما به دنبال سهم منصفانه از فروش نفت اوپک هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/132732" target="_blank">📅 12:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آکسیوس: حملات آمریکا ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132731" target="_blank">📅 12:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💢
فووووووووری/جنگنده در آسمان تهران  احتمالا جنگنده خودی است
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132730" target="_blank">📅 12:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری / بوشهر صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132729" target="_blank">📅 12:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4156a27b.mp4?token=i91eyx6Cn6fLHEUauKboZeD9Fp9hYYz5XYnLo73gR6uCPoumnTHeYX5CKe2XVMWQcVVeN1a2Qbq6ezv4Pavwlramtee8M_4cPH8zh9jCxQ9yAxvFIHBvJ9y-3KkFRbQkjrHHB3fE3lcSXc4EK9KvJPvfxxcgGyD9qCBWKJsRh6BfUJV1aoWMVp4juJ02tbWfeFvMg3LVGrfOw8pRP3P9ywKwgouSqY29Ln9GWUP_CyBrtlJvelE-xl1TV3KULYVPEnf7U9Wdr_eQr2AhEd-YeT6pWJ1h8vQllA8P_Bx0AvXB_EtIPR-idK1VKeKTizy6vwTk16S-aY8dMYhJYvgvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4156a27b.mp4?token=i91eyx6Cn6fLHEUauKboZeD9Fp9hYYz5XYnLo73gR6uCPoumnTHeYX5CKe2XVMWQcVVeN1a2Qbq6ezv4Pavwlramtee8M_4cPH8zh9jCxQ9yAxvFIHBvJ9y-3KkFRbQkjrHHB3fE3lcSXc4EK9KvJPvfxxcgGyD9qCBWKJsRh6BfUJV1aoWMVp4juJ02tbWfeFvMg3LVGrfOw8pRP3P9ywKwgouSqY29Ln9GWUP_CyBrtlJvelE-xl1TV3KULYVPEnf7U9Wdr_eQr2AhEd-YeT6pWJ1h8vQllA8P_Bx0AvXB_EtIPR-idK1VKeKTizy6vwTk16S-aY8dMYhJYvgvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار‌ تو جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132728" target="_blank">📅 12:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvz255RnSoaOb306KBTlNJtOqshKrbccC0BJxEMC0qYmnxRV4KCyfELabIpKSwfkn4OloqrEOnjmXocpgUPH_sEwZIhDQL6mOfMRGbknBIYHMmf5m0yfJdEIVPblORDD-BiW46FoIYCUUSMC6M-_bl3Nt-YwgZrxCwvndS22BffUqcTKdDFsX8MG2ZF6w7mAWPvPesyeem7UMiy2-dn1JgeJFakAOHeb5RTquyAm7vghVEHJV6l7cBnALyUiWSz9wOq8Q4QmMOJiGnSZMxhAcdVqyb72YaFvUfcwzcii5HF4jIO9sJWAN7H_8W18xK1I2ML6NsDvXj4OAIq-Q2zpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب‌آبادی: اگر آمریکا تعهداتش را کنار بگذارد، ما هم کنارمی گذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132727" target="_blank">📅 12:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">جمهوری اسلامی میخواست جلوی حملات به جنوب لبنان رو بگیره که حملات به جنوب ایران شروع شد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/132726" target="_blank">📅 12:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132725">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZDMd_HOpQSNt_gIUL5miMgBnbBqqPLID4AVEY7vSEozBw8Z0L407uAWwm6k44b5VdrEcdXXW9AbcQ4_-4Zc6ip99EorHU1Oh2Gp_j9Ku9LbxrQp_LXf-6v1Kr7k3v_eFU33-RXCP7tJLPqzpuzrFy6wKlfK18NSx0mkF_u4E0QtBqMUJ5pWoM9pkEa5pD1GLJirbVC9XpLlshDkAJidRaIpWgqEkAgLY-z2bF532l6lhMm0jtFBUHD4mI-sYIEOq0uw2sFbMcIFAkEYkrmKOzadtb9p0SNpV_mgtzmf1b4DwDKpvJP2Odwx4ONdbFgBBP4TfqBaqbZhllhrInbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت پروازها در آسمان منطقه، امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132725" target="_blank">📅 12:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / بوشهر صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132724" target="_blank">📅 12:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbPFiwAR0txri9P6ZC2cyCeItdB57-Uy_en4Kg3mYQfPkOS2jSm0SbihCaiZ3zLDJEEacsHtMR-f5p4SO0OFgqL26pAz5H-0u_s-m2PJp4CH27rjV9Q7XDpM6ubJXsOZ2LRPS68B3DdnGF7fFBpeFMGgKq5Al1TRoDiAi0U60VQ7M45HtHsQEBlv-4bmaaXgFJvfJrzam8bdcF6ggezGxE5dFcFozcVsqfCPfTmaUzeKRRUW9o4o6hvzzAjmkgnaCU_l_vCSvc20bYCw0O1JZZTUWH8sYKNuHfed3CeepXZxgQmL778CpSrxIQPyEIp8_oEL1nKeJxZxS5rA-so6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آثار حملات هوایی شب گذشته ارتش آمریکا به پل ترانزیتی و مسیر ریلی آق قلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132723" target="_blank">📅 12:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سفیر انگلیس در تهران احضار شد
🔴
اطلاعیه وزارت خارجه ایران: سفیر انگلیس در تهران در پی تکرار اتهام‌های مقام‌های این کشور علیه ایران، از سوی مدیرکل غرب اروپای وزارت امور خارجه احضار شد و اعتراض رسمی تهران به وی ابلاغ شد.
🔴
ایران با رد ادعاهای انگلیس درباره تلاش تهران برای اقدامات ضدامنیتی، این اتهام‌ها را بی‌اساس و ناشی از فرافکنی لندن دانست.
🔴
وزارت خارجه ایران همچنین انگلیس را به همدستی با آمریکا و اسرائیل، نقش‌آفرینی در ناامن‌سازی منطقه و میزبانی از شبکه‌های ضدایرانی متهم کرد و خواستار توقف حمایت از این گروه‌ها و تغییر رویکرد لندن شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132722" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فرماندار بوشهر: حمله به نیروگاه اتمی و جزیره خارک صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132721" target="_blank">📅 12:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9swKQohgZgMRv5Wgeregrl3xG4i1gI7wosvqD-OlcNX9NeJ6-okWH8yOmXhUQAYpPneOn3HshaZU5p9JONE1X5pTYTU7g_xh5ecXFG3OcxB8eWLzpm47agmG68K216MSZ0-Cc0_xIFYCrP4amzHHhopdoKV8z-5EnR7G7sAJtKSNdXJFVQ99seCdUTe3D6S-PqYhHFeY1yQG6oezFOIlj6_Mv_TXdiGE3BqxH_EAcQCxx8LjNq8dXNkWUjejBKrhknrxbJpbjzjgQJLXiaSlO--v8GY4W1f97WMW5oJof3Wck_e-jA-pRayM4nP8Oodt-8DmFqfKa2FZYUYRy1jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهم‌ترین گلوگاه‌های نفت در جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132720" target="_blank">📅 12:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سنتکام: توی حمله شب گذشته حدود 90 هدف نظامی در ایران زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/132719" target="_blank">📅 12:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / منابع خبری از وقوع سه انفجار مهیب و پیاپی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132718" target="_blank">📅 12:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMuArSSEtA-vMIiRE-pwCpYDCtKDazVnYbncUs54bkVTpcxJpJQngzUAR3gyKIcZYWINd16uOgyOjuSaVOSb-6XBBlAyvr56QWJmx0IbrTcCgeXu91wVFtz-CW5UdRRZSCal1rndRyYMc7o6eQLI6XHxDS2debDaYj8-ElopdBsPRZtoLgopFPP5chGkqulc5-Fdymcy5nWDt5gz3z-NpaC3ZbL3aKrzqKi1KgllP_CrS09JlqHkC332Em_b6KHZUkWhplXCDCU6Egb_05z6bzERJ_GCI3ryywU4rrCi4G20K_a1t7D5iCZjValls9z5iszWh_bSqkyB-5DYrON9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون حضور 5 سوخت‌رسان آمریکایی در منطقه
🔴
مبدا پرواز ها از جایی است که ایران بعد از آتش‌بس به آنها حمله نکرده‌است: بن گوریون و العدید!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132717" target="_blank">📅 12:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / منابع خبری از وقوع سه انفجار مهیب و پیاپی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132716" target="_blank">📅 11:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخست‌وزیر عراق:  برخی گروه‌های مسلح تصور می‌کنند نیروهای ائتلاف بین‌المللی از عراق خارج نخواهند شد. برنامه‌ای برای تحویل سلاح تدوین خواهیم کرد و پس از پایان مهلت تعیین‌شده، سلاح این گروه‌ها در اختیار دولت خواهد بود
🔴
به زودی با واشنگتن اطلاعات امنیتی سیاسی مبادله میکنیم‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132715" target="_blank">📅 11:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUOZKGx7LhSTKYBLqKp2ROobQT5f_2Sdq_bz90m4BJJHJWvzcvD5nYaYJFh7iqaS9w9SbBEnIHZnIm6eLyB_g2yL4VBTOGhbl0nCFbbwWnDYdf9VV4CawxtvDsMZ9dqsXcAJun7e_IgpM4KXsm26KNlmZgeN9BDEpQsVkvmVeBYsg0kdNG0JMB79wdsrVQo5XTORnGaHtP4jL8NJjVmXWihCQmFayOWPuZVtB14aLrsIwVzdbCftvJLzXvXznZs5mXk-qgv2nFSVNdemB5B-p0gR1ob0VNL726Cjt6QSRmOfLtWfTGJXNSRoaWdPSqZhu2jXdAv6J2lIN6YeR858eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود درگیری‌های شب گذشته ، قیمت نفت امروز کاهشی شد و به ۷۶.۹۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132714" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f85ee64a81.mp4?token=BjK3yCGq9sq5LttfaoJ2ras9BO83TBsMo7VV3ebvpcgH0xVVJjdjg9YJD3Xw3Bcc7E9FtaQc19G29z64nNKXUycxdLtj_NQNML42AMA0U2BuZWfaN_21-hk3SOEiCT9NJin9Jt-yndMXjaTdKBhIEE_6TsZzv25dbErCaQQs1ng0t3nsURX9DGjJm1daQwH8-fVG2bzdaFjdAieaw0EgbQQDKI1fCyD214hkVpx-ARfNwwRayqhJcwBLDmcyDcpDmMxgStCHpQcv8HeqMiIOVnU7YnwaOf6KanMRWUZpUrJBoeBJ6YUCQ4VRC0RULRjN4zYJfhg29kMPVJwv-uzHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f85ee64a81.mp4?token=BjK3yCGq9sq5LttfaoJ2ras9BO83TBsMo7VV3ebvpcgH0xVVJjdjg9YJD3Xw3Bcc7E9FtaQc19G29z64nNKXUycxdLtj_NQNML42AMA0U2BuZWfaN_21-hk3SOEiCT9NJin9Jt-yndMXjaTdKBhIEE_6TsZzv25dbErCaQQs1ng0t3nsURX9DGjJm1daQwH8-fVG2bzdaFjdAieaw0EgbQQDKI1fCyD214hkVpx-ARfNwwRayqhJcwBLDmcyDcpDmMxgStCHpQcv8HeqMiIOVnU7YnwaOf6KanMRWUZpUrJBoeBJ6YUCQ4VRC0RULRjN4zYJfhg29kMPVJwv-uzHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیویی از چند حمله به ایران منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/132713" target="_blank">📅 11:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فرانسه خواستار خویشتن داری و ادامه مذاکرات میان ایران و آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132712" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjEwhYDwVFxCtYAXnZLLyK6Zn3jJCcgYDYw20LOwB1tuH0Ynp5bwv0KKYi2jF2H85Gwje3OilDMCQMSLk8P7FMeRf00Cx1wI6StYTsFWeJADC7BtDrdfhZw-yb1rBClWStnkk44ARVXbi_zVBM3eTSo6lV0DC749TjhMqiwDd0w3SSxAeVvmoSBZlvyNmDG0M--f1F44FkgCFol_FerltOmDWJDq693GkYV-NyKYLyW3jk88F5C5H96V5_GQD7aRzl6T881l3FTb7rSjLfLFFU-IaY3WS8RxBSDqdoRApcj-bmrL0-e5isGdGdeRVcws7DABkIRdKCuIymnLc_JU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنری در مشهد ، ما ترامپ را خواهیم کشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132711" target="_blank">📅 11:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132710" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قطاری که عصر چهارشنبه از یزد به سمت مشهد حرکت کرده بود صبح پنجشنبه به دلیل حمله آمریکا در ایستگاه تربت حیدریه متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132709" target="_blank">📅 11:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132708" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYO2mpeE8WfmXDMticpI-pC8_WeLYssrgIes7kCc5S0K-dn-hnid8cPOhiw2qEbOeKhjpHrlbn5Cu_O7s2c6iPNmFEMo7kdQNFyyDJjipVybuX4wuGpm0wPW7RsZJZyT8m3i_Wcvk12KkUG1GFSgUqvJ3vVBFH65bw6xZECtGk1OXnPUdXSm0EusgU7iYx-VLx8_EgcTttFHiHSJL22L-7jnYANva5NoBC3ASgcsbSAHDpOJ4P_0BUuVwQ93TSRlNrdhWtLi77BGNL1RTPefHzD702nGAMKzw_kGgauEgl48Xctu5IWs9B1J3KZGFLva8vJGUBHUhko0LVB5l3_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه: حملات آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132707" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6rMYMwLA745BNKYeH7BgjOW9d6N75nF5Nn_cJSt5Rq7H5f_lKaQlvOMV787VyDQ2IfGFrKYj8XL_JA4sXlhYUU83xuAl1ZfxZYWchbf5zrDMIm90m9ssidb84b0H-i_1WIY20zbrK7LTpgSa170Y1LpRBuO34liSi1szm50Tkq__NMBtpzptsIo45pe-0MHD8VhPY1ymWvL4q1OvPQ-OtsMVmpo1b0lsdID3qI69YIz3JJuU5lYyQYhcsIAj3VczLCO_QcIg_IkrOD9rFtlJaEmYMAJ1rWGilApfESGJ6W0jU6NxebSjwVTZcZBuSkChFM70fpZWLl-689Kn82XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر نصب‌شده در مشهد: بی‌بی را بکش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132706" target="_blank">📅 11:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
حمله آمریکا به استان همدان تایید شد
حمزه امرایی، معاون سیاسی امنیتی و اجتماعی استانداری همدان:  بامداد امروز نقاطی در شهرستان کبودرآهنگ مورد حمله آمریکا قرار گرفت.
🔴
این حمله خوشبختانه آسیب انسانی و خسارتی در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132705" target="_blank">📅 11:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTnJAIYwywab8w8KJtCxyO_Ni1UB-u-hJ7_anTFix-GmtEMNnlKf7gjEzYtdac2Zyr8HCA-XvHRkJ58S4b5zkAg45yFXxfb7ucBcDjqrG07lQjYxhdUzvtCj_-nc62aMphxa9_6kA8PeIIQlHqAh8uWG02uZEyDDmSgBZmffiIRhhdWH15tAMAJgs4Iv1lOHWvXL89dpv4InXXmjT62yOOD78WDrQ-74CyJsjf1LbWAi1L3djkGd3TLco9b1uoEvxi3-HPNSrOOhld5tW5mnSvTXZYe1oG6VFKgL6awuJeQW5F19YYLvd8sRsN8GwbbAzY8Z8Jrl6Jh9utEJTr1bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9G7H_mUC_m7LYgL8juQ_lejz_qrPSrhT7MiEMbGJcH_7pg_m2uyVEJ3Hld7Ph4Jk55l2K87SV7r4mgKmioo8LyxCiubw_Y3z6J4W3VvhJF5rVwSP99bosyYUYJAVN6zwsZKFS_LjOMQDZNgq2bdGZ968aE3qtMWKeokZ8Qv4ZLks0ldLBLfjj23OepGQikn-9HWSfL3xI_P7HPsfvwV2t8c7WCXnawRRz6dJGc2bC4cz0VXlG5noZ6x3gItvx-5IkVy6e4a09DPulbjxC97LGtPZw6GoM1-PjyNIZqiYYJ11QXQMBuSx_vw_nIAoJKe6vojSq8h9vDBTjlI8QluFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132703" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132702" target="_blank">📅 11:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTLijMKpc-LCzGXK1NRvN_4mEhxjQMWpqVnJStqC19AZuK4wzh4ozHamNWu74mvTbmeOq5VkHQtyIR9hiubgQfL-6UHgllPXU4xbnAvjkuZfLhUm5toPav5WVVn0AyRjc4vCvFfOyJKfC7N0w8rKiwT6lcfaKGV0dOGyAVE5mY4fwplwkuBuZoU1lR7igm_4FKyQ1dGVkJU3ePtSahAjCAr71oZAlBp14p-svXVMHyqbKZMpsHubh3cLf-5S7THHdaurv1AqFMapcj-HNATh6DBVLl5BbKut_f5cCkoDmcyWbwHrbgqoVtDBY-zchzJEXT7Fn39FADaQhJLvxqrS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد لاریجانی: برای سر عاملان ترور رهبر انقلاب جایزه بگذاریم
🔴
هرکسی اقدام کند به بهشت می رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132701" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132700">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132700" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
