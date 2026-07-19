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
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Comming soon.....</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/alonews/135837" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گویا صدا و سیما مراسم اهدای جام رو به دلیل حضور ترامپ نشون نمیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/135836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIVdJ9vLRunhhLHVRw-w-s1XZWuVxMlI9o3yeClJ5Dx-LrunbLGkBK-aq9e0xQGaNxu1szaFVItKH9NyFinFaPHNTjhZVw2HNbUuRwWlUI5c9F7LIMD0pbp6SzsF0hmwlTcETdu-mEDivzvl7gmVhJCC_-Ne278RNKjPJoM49j77wbvdi47gbytoZ_GZE0Tk_-8Y4Kw38cDtKKHg6eF3x2li5UTm_M3aSKzvpcsXkiXbCvgsofIoKBXweHaXfAZvWkGpJ8su5CnIi9-nwxpwEqfQzhfI60t2v-gJLWgV36U04Ykdn2fDRu-nf-RkfNpGvu1YCrHGJD09BoowUyKrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مسی بعد بازی
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/135835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اوه اوه پشمااااااااااااام
😐
😂
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135834" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تنها دو تیم اسپانیا و ایران نباختن
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/135833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzw_Gmdms7SGIIaRfCWq_rnpbzSDhiyDhS05eNG58DFKBvL11swBsx_b0Zkn_E3CLLbxNS_yxnPxEuVoRJZ6S5rWJWr-redR7oZPEHQeWW86rxVY69Z_N2DijJfW2zEcWuTJHCmf8IIgltXwgdxBC_9NGY1VeySLkxGDi_GPtNvrZ6O7kCFFQ8kRHG7uRCPMkE5wFiikNIoyqbNuolpSxcMvpg4Hgxzj0BgBUjoJ4r3OzoatYHRVhug7_koixei1FasSn7oULPRH1s6fI_vAjJbtftkoeXiyFcqsFAPPEwwAGoHssWTqOQUiValltoHsBKPJypR0snKHUmIFIsN_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلیل قهرمانی اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135832" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسپانیا با شکست آرژانتین قهرمان جام جهانی شد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/135831" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمااااام</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/135830" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/چند سوخت‌رسان از عربستان، برای عملیات علیه ایران بلند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135829" target="_blank">📅 01:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فک کن هم طرفدار آرژانتین باشی هم طرفدار جبهه مقاومت</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/135828" target="_blank">📅 01:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کجاش آفساید بود آخه؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/135827" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آفساید شد
😂</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/135826" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دومیییییییی</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/135825" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مجری تلوزیون: اسپانیا طرفدار جبهه مقاومته و ما خوشحالیم، این بهترین جام تاریخ بود چون هم ایران هم اسپانیا نتایج عالی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/135824" target="_blank">📅 01:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkMJv4fqe-StabwjI2Ivp-s4lY2tCkwaj6n7r7BcI7ldGlJxUsJYjcmwTIOqV7RwI0JOkeFWPaplxxO7yigCAfwrNsyYAIwuMkSZYunWDyerTl6-IssiwMhdUeS9y2FErwMQ9ekD-5MWnHVMAO-1evD3WyW8fB-UgkuE6-WelZHtoPks3_y-xq3UGtNGGWluY_1lzZzhwp_HRePh4lTr90-Ga3iviA1wk9KqiTUGka5vlbZ51QCKFeA6uM9mfWUQAyDhGTPlbDeOuMkNSPa33sN5K03FVqaWs1brdbYAzNh_Yyj2Syo5mAdNqlIacqOuQuQNumNnfyzqyz24nAzQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفانتینو بعد گل خوردن آرزانتین
@AloSport</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135823" target="_blank">📅 01:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=Y5e3x_VEMT051GSb6t8-3x9MHm6QuHAuWUYnjP1jGab1cK2KEes1wmru49w6411M1e0UDuTMDP4exmjIejiqWOvLTxhAJ3wxp1n4H8jjwtl_vhrQDu-VvYKW4GS-MFlVG3pD4kK2Of0bc4KXZV5pnXFlirY7Iqx5cftbex4RBTf_LjlmTBRlDf61aaIX3pEJ8d13FTpXkgoGti5VtKlzc3THxxoOYVLs-5DpgnlSVOEE5u_90QGOMRJ1Ggw_BrQHvyYdoyvrtwLoLlOp4bxus873p358k1pqZ7TF4Ewm3Qm8FwEy1iqP-g-BdU_gV2ImKabAM8GhTa3BXW88BswVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=Y5e3x_VEMT051GSb6t8-3x9MHm6QuHAuWUYnjP1jGab1cK2KEes1wmru49w6411M1e0UDuTMDP4exmjIejiqWOvLTxhAJ3wxp1n4H8jjwtl_vhrQDu-VvYKW4GS-MFlVG3pD4kK2Of0bc4KXZV5pnXFlirY7Iqx5cftbex4RBTf_LjlmTBRlDf61aaIX3pEJ8d13FTpXkgoGti5VtKlzc3THxxoOYVLs-5DpgnlSVOEE5u_90QGOMRJ1Ggw_BrQHvyYdoyvrtwLoLlOp4bxus873p358k1pqZ7TF4Ewm3Qm8FwEy1iqP-g-BdU_gV2ImKabAM8GhTa3BXW88BswVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلللللللللللللل اووووووول اسپااانیاااا به ارژاااااانتیییین تووووسط فرااااان کوووسه دقیقههههه 101
@AloSport</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/135822" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسپانیا زد. فران تورس</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/135821" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/135820" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW3pCHzt2ImYKY161s2a3O2Un0zrclCqvAUYR_21CEZnUT2b15HvtlOsgmCm-5OGwWxHy9Z6OvLqpZYp95Bu6zNaUFj3Aqw7KUfyipM1EM43WBlyZITZ_v78ex90VhQVFBUr9T8zRPr8KDQan-EmYuMmy76h033_eyCyDNeYcn5Yaj5hH-pSqWkb17A4pjsPiy4Mjl4FHPws418xK8ZlkC8FiNLzCqochx73ZLaG-7whu5WVCooH1f-C4j1teGjQlPPlg_bx0IDnV6yjD470cvF77-R53J17_pjWenY6SCkMUtzCFlKjiA-Luw6jTW5ErLvwjeN72EwHM1E5z-ceWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر فیفا
👍
👎
؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/135819" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مقاومت اسلامی عراق اعلام کرد در صورت ادامه تشدید تنش‌ها علیه ایران توسط ایالات متحده، مستقیماً نیروها، پایگاه‌ها و منافع ایالات متحده در عراق و سراسر منطقه را هدف قرار خواهد داد. این گروه افزود که در روزهای اخیر هیچ حمله‌ای به پایگاه‌های آمریکایی انجام نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/135818" target="_blank">📅 01:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlHKmb_Wg6Uiv636pOQj6yd3kVxKbr6TINgFkthDxhn3RCqy4gejI-8EqH-029_DQ4M9ia88ureDPmF-tBLEaPWjcVh6Wf0YpqRbVrWdlF15JNrP4BeD0H4AU9mywOddTNZXtJl7QFqMwqd0-hxNO5WgsQcvcfXTKPSCyg-fpj8alMb0irjsPxWaYBmvCPY-QV5fRW4BgsM3toanaIL3wRV03INjUXCbOXa3uzrRoFNVDKlmJ9zeGb8FAdTKS3nxNuhlrSw_AdvMuS5Y3EzYNAKJerKQEnZgDpE3D4wjWd9HDD91aRr6YLaigQyKnHb137dMUbfJxlZYtlLKvo9wSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینفانتینو بعد اخراج دادن آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135817" target="_blank">📅 01:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=UNzzZHXkM3QluLkDfOSS4vvwKhyu9wd8mIKKctlMYip9t2P3JgDek1Co30CS_6z981fZ3VR6mB32r36HR-SOZgYytVZov1DwdBTg7ED9lSbt69FQNU-dX-p2dR0yE7SnIvvBD2BN8WHIrMbE6-s__hIeSuVrdqj6uFnbPAW2rJsGJUW9n00fjxEDY0UXZx7iqL7FBo0ZbtamFIFvQZyTyPtsgqEeCd_apCmUqd-ZtF_5FveQqt-jOvb4SI6_Y4PDXZ0WKJ7GnLP6LeuXgFhenJumJszPphTNOCLFXuhAjxOQx9b2vD1umxYrKwQxNNom620Z_x_Uw2RyzSjAqQgQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=UNzzZHXkM3QluLkDfOSS4vvwKhyu9wd8mIKKctlMYip9t2P3JgDek1Co30CS_6z981fZ3VR6mB32r36HR-SOZgYytVZov1DwdBTg7ED9lSbt69FQNU-dX-p2dR0yE7SnIvvBD2BN8WHIrMbE6-s__hIeSuVrdqj6uFnbPAW2rJsGJUW9n00fjxEDY0UXZx7iqL7FBo0ZbtamFIFvQZyTyPtsgqEeCd_apCmUqd-ZtF_5FveQqt-jOvb4SI6_Y4PDXZ0WKJ7GnLP6LeuXgFhenJumJszPphTNOCLFXuhAjxOQx9b2vD1umxYrKwQxNNom620Z_x_Uw2RyzSjAqQgQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آرژانتین امشب قهرمان جام‌جهانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135816" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ITIGqZnwfnobmGTrWRRC_ZrNzlYFNQ7XFxGIcmaZsX0c_4R94lrzzO10BjAu3ngtCTfLK9DbXzQVwcyMQ1d6I3Iyv1N1vC7QFDvcdlCeEeHtx_nLyhU2rV1rInmVJv_l-tyyU2SsOWMzfI864UdETOpUkkykZw_qq0snvrX5bnwcx_xO9oOYYw5pbYF7XUpG-DeYzfVhwZisqH5No9M_4D6OYqpD8GKMa40sGfDvt_TugCUKNzx1Ck43QChGm57euAbepAEuJ4BHJ-nfepJ3GN7XMq5n3E69vOlOD13Nsz24Rt-27zCHW4CV_xtJaPT2jdgPfg7oScBNK7HzHL8AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/a_NayItX7DdhDdDZzLh-MSmZxHKa6cSFRNwFKEAI0SrioAPdvXBtWWowmmXJZZDaH4CHhlHua4Wi_xSclz5C-Z5lk_58T8BEPGGMYGYyP6sGG4R71f8QT6_8WGBwAe73YWDcnlZkw1WwGjvBKtupt_fCAQet5PANdnQwqpVFJnbRPK0aCO6NZpA-QXYt826uU4N50o_jGrah7tJl8wF90NPwMUBJWbmKGPPI_HtWTP1IU2HSSs_l-yzyqMSFUkOvBVoI8-q44R7kO4UiXqeYZvUR7newxZ9N-30Fm1d0ZQjLrr0jHaQr9LRnN5FXjf4QXX7NjlyuWNqLp4TAcN7lcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آخه این کجاش خطا بود؟
#لابی_صهیونیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135814" target="_blank">📅 01:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttzdvsqBIvNEz7oV-dUtmDxyvRFBSlxIIt4cl2VMhT5LIPGx9TSY4V8-HBvhvx8Ug0ZqaIDpYJrxOsyghHqdGami4OaQyqWAfsWiiqPj9U-Ki-TzykIi3K6D8ZAIML54xH-Xo3z2wwfctyGdcGtGw8CczfOz8ezZcI1HoRHHC1m4ofFBFJqClD_fzoNbIrVBze9cCJfgjpLrtaQskPgM5i5oCzsCM3HvtgOogPt553m16fDdA2Q-6r8sIYxF3x1fgrLwcUbhJVA_562vjp1_RwK2RZDquOWFemHlAnaCOT9_F6IUJY-PoshBNLjFQ9zUFWFYjRNkORDDZGyvyq_q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرچم شیر و خورشید پشت دروازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/135813" target="_blank">📅 00:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
داور حکومتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/135812" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اسپانیا گل زد ولی خطا بود قبلش و رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135811" target="_blank">📅 00:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWsVyLcQZUwJ7sxvnfwhjpVPvQNySjhzSspWgj_Zv7ZvlbctRDPDvPx1a29SCjvXyyIBuKuptnGKvzhrL2Lrdi1Ndgl07y9PYp3lhDxBGqoh2L9iawG2B0jm4uSZNYxe8ov7Oi8ErAAxfCZrtAlE49Rj7sZWccfJt4CN3ZtB22L1mwaA6Kzz7lAb4mRUeCBVVb80RGZaV1QE2HXZPQNW3L4hVT4RTOfl5P3hOWqFm3vn065kQYDMrCj70zXplgpOXfsinVceiuryMI_YFWrPDcUUsBXOTgrg8ZdmdiVWPUamzdcKeiDtBo8Z7-ICWvhz7RbubP1FrU5mybbap7phcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست خدایی که آرژانتین برای قهرمانی نیاز داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135810" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skz9IIW0yaSKFKJE7zlUkaDTfssLQVY_3-BggI1IbNwhkeaWQKyYER-OfQPVytJsck6w5Qx4NjJWPLv5q9U3nrmRcb18bk37T_RSo7w8SMPX0SkJITa0IjNOKW-o7aMkqV8a_s1XNjsohkhtB9PFP3jVe7yOcu4Xz9uFZ9au8VU9MdNwdfiR9mgY0UbXWIX64F2pilSLwSXjn06mrJKseTCZlXjQ3HdO2q2YPe6PNbL4myfoWw9iYKADcuTK8BA7BrRY_DCjNq2gKihBQ_gtU-xxLJrQ1O0yQvIliYyMtXdUZk20ZG5XxoXl07hpO2fjki35xEKB8OKL7l7g-E1ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی، از زمان از سرگیری محاصره بنادر ایران، ۶ کشتی تجاری را تغییر مسیر داده و یک فروند دیگر را با شلیک غیرفعال کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135809" target="_blank">📅 00:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCIbK-DC86hsVtaeqBms3srul_mIT7oOSFe0devN3vQERmT3MOCzauiyFiYJWeOGwtRW67_e5dJL6nH_fnlEzTpdWP8UFZA1RRZrWqKFANSHxdmti_NVHHey9VdRK4ZEubhpf_4ZUhHQY452T30ugQza3wocBum-idd5HgMwo_iMf-R51C44p6vyioBZc7oRimwSzyKOYOv4A3M8vsQhJg49cKQ5RlP2NeKiZ3B9NHPfNEafifMsq52LnQnaRG26TW3PtF_Hs6AAETH0EvEe_DSiwaDg7tGj5NXymUEVQWVuEKKqN1wbLG8UkPLpJrXhq5ouiinsQJG1WNJeZ6Wjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار باورنکردنی 90 دقیقه؛
😐
آرژانتین 0 شوت در مسابقه ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135808" target="_blank">📅 00:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f213bec9.mp4?token=ItdxyOkKdmKI-kZuy4T_7bodsGaEPPvAWlb1JT2yRVGsvIUqRx0Kkyk1T9nQNuoZlGGCVRisPPfB-aXTDbU8q8KajPJv5NW1Twmk8brX6y8qOeaehvD3HxRyJ68IZzON4Zpgt8wnmCu6kJ18TlMIG9cdohVtTzg-qutBLcLTehKLWA7_p24L7VMyp639G2619IskYTtCXI1REA3_5uOnmnlZ6EuMZsWL6Tvdo3DHJsxSp8Y73uNVEtvNnV3TUGAHKnpLFiE8S4PXEyLcYZ-0Cdy730tCmfY0UNvVCELB0L2FpgFZUwt2E5vazQ7dq1bkf8Jm-7mQDNe-znX_aU1MRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f213bec9.mp4?token=ItdxyOkKdmKI-kZuy4T_7bodsGaEPPvAWlb1JT2yRVGsvIUqRx0Kkyk1T9nQNuoZlGGCVRisPPfB-aXTDbU8q8KajPJv5NW1Twmk8brX6y8qOeaehvD3HxRyJ68IZzON4Zpgt8wnmCu6kJ18TlMIG9cdohVtTzg-qutBLcLTehKLWA7_p24L7VMyp639G2619IskYTtCXI1REA3_5uOnmnlZ6EuMZsWL6Tvdo3DHJsxSp8Y73uNVEtvNnV3TUGAHKnpLFiE8S4PXEyLcYZ-0Cdy730tCmfY0UNvVCELB0L2FpgFZUwt2E5vazQ7dq1bkf8Jm-7mQDNe-znX_aU1MRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ببینید چطوری زیر ساخت های مهم وطن رو زدن ولی یه عده حرام زاده نفهمیدن چون سودشون تو نفهمیدنه.
#علیه_فراموشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135807" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جذاب ترین بخش فینال تا الان این بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/135806" target="_blank">📅 00:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
میثاقی: آه مردم مظلوم غزه و ایران یقه آرژانتین رو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/135805" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رفت وقتای اضافه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/135804" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مجری تلوزیون: مردم ایران از آرژانتین تنفر دارن چون حامی اسرائیله
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/135803" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135802">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
آرژانتین اخراج داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/135802" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135801" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">الان ترامپ میاد وسط فینال میگه ایران نباید سلاح هسته ای داشته باشه.
اونا میخان توافق کنن…
خواهیم دید چه خواهد شد!</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135800" target="_blank">📅 00:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=g7ZhiZj6O_TzMqlVxFwmeYoF-Qan2fHQJwutLB_2fqOPqqyIr-F-CtwidTmTo9mzyOkDEri1q9Ch3y7C_t56OU6KW3a0VJxSOx-s7XuoYYft9LwZGLcZL6HWIHIG16oiAZl0TD26MPMk0DMBCSiPFpHdHhSDRzahDmKDYiyvDhcya-8IUGV4sLTOCpnffmp6ccYb37nupJFNZwF97_X0eIx3-lGfaAnXt5amGhfUfo6QsWtJXYzWL_W0l-Q0xSCaWFnhRGHBa9mFxUNNOTyxe_VyI9xRxx7CQsQe2Pj1XZ3eFIyO-uTjv2O1lcye37XrGeVyjcn4TUkq-B-EQC065Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=g7ZhiZj6O_TzMqlVxFwmeYoF-Qan2fHQJwutLB_2fqOPqqyIr-F-CtwidTmTo9mzyOkDEri1q9Ch3y7C_t56OU6KW3a0VJxSOx-s7XuoYYft9LwZGLcZL6HWIHIG16oiAZl0TD26MPMk0DMBCSiPFpHdHhSDRzahDmKDYiyvDhcya-8IUGV4sLTOCpnffmp6ccYb37nupJFNZwF97_X0eIx3-lGfaAnXt5amGhfUfo6QsWtJXYzWL_W0l-Q0xSCaWFnhRGHBa9mFxUNNOTyxe_VyI9xRxx7CQsQe2Pj1XZ3eFIyO-uTjv2O1lcye37XrGeVyjcn4TUkq-B-EQC065Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرتاب موشک از ایران به سوی اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135798" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0dg6JAE2vL8uKP9fOxTHntSR15B2I5SWBUyH-GFmHybsiD-NbfPZYjX4Kqt74zCgfPwsn1bA42hKB0_4KpILZ3KlW0jFAEtK7f21pPLkcZOgXh4IjoDWSoFnfswoYrSccPbzrcc3disC0Ld6qeiMP7CB90OCWusId_NJzidkaHGIOqD3m7aaI0pR4XZHOZulaZ2v7NrSJL0dpEQdprYeEfXAuB9K0Oe6bBRdls264YfyWfdTUBKCR85f7lY8SmXaJfU1GXaN8XIFVYxtcI_x7HgGOVnnLRbeK-NYOKMhKeCSojusbaiTj_3DcqlC-Ecrn2BSK7Xp9jQaxw_kX97QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاتی جالب از مراسم که یادآور تجمعات شبانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/135796" target="_blank">📅 00:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135795" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/واشنگتن پست: آمریکا در حال برنامه‌ریزی برای جنگ  گسترده‌تری علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135794" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
@AloSport</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135793" target="_blank">📅 00:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در قم و اراک
🔴
ممکنه شلیک موشک هم باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135791" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135790" target="_blank">📅 23:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135789" target="_blank">📅 23:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrmU1tF-sYpjg_MX6tz3Ncnaw9fEMazaDLfthamvzDgAUArNPIVW8PKCEYkztdcOnoWaa-P6G4tsb0LgM27fslmNbqqQckQNB9B-PJ5Uu8skBKMUvCQuCnf5MtVGhCFHSej66K1Gjbbbbm6MD0XJptFT7B5Ww4_B_qqz1QUPa4Xr2_gUlTTQ8VlnMtZ2qCXz-iHxALduPj-FwXNsnG4CjIOMQRg99HFY_FuwaKUG-g9qJleqo9rhn3Phny27FSrHyKz6jiPi98W84va9qOEAWr5dC92mWDwTbp4--81dTiVWIKFXH2DZMGdyt2vwf1WtBwqqB8a_uvrUACFvWr5A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاتی زیبا از اختتامیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135788" target="_blank">📅 23:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
محور قدیم بندرعباس - کهورستان - لار بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135787" target="_blank">📅 23:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">عادل تو پخش زنده: آرژانتین بار ها ۵ سانت و ۱۰ سانت و ۳۰ سانت از حذف شدن فاصله داشته
😂
@AloSport</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135786" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
از اجرای بین دونیمه و شکیرا لذت ببرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135785" target="_blank">📅 23:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YExjjaDjXdJQ7CSlCczo2HYmxanAb8rt1Dj3QBMYVcrz2cyz9yrt_3b11UQ8eVWCeIo13WMD-jjinRWyMZ0XWy8qHrYc0PRwaJHoeArX0GU2QUUwaM6G_mDWgux6dgEM7M_vP4H5I4WC5zlO8ni4Gt8OyL2-IZVVfBZw-PMUojET9q29LOvCua6pfbQMd7CUC07xvmNZPmjKojyEoB3UBS8nodCpFWFe9x6RZjAVGs_Vd4I8goOLu2LMGZQc0EyT6o4WZ7x3DfymQG5g56uZd2oq6pRZxoprVZQkNSTxFYwOt9vxt8_c0_Zu1_CcM350RqrK0VqMrnn2Ahi25igJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تماشای بازی نیروهای ارتش اسرائیل تو لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135784" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اجرای بیژن مرتضوی بین دو نیمه فینال جام جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135783" target="_blank">📅 23:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7492701943.mp4?token=OnyeJKveunLyhTDNpKbD_fptU3Be930BzTWDWWdMgPNVPkSgAg8-iM9bwbl9RoL566K43SNk74q1WB7nVcsoyqxvm01O5rwSV90Xek2LYyg1Nl7jVsR8iTCptWxwKQ8UUVWpgsgSMPXpWmhwzLn4PNPWqQARKUXEgR58CRGmgx5tDUwslVaLTQb4Oo0tXHqkaqnOwlDZmujHLsBHT42oLzdP4HPeI_sYLT2arB4FofTmpucjWqTsucxgWfzxl7Ld5OrCSCeLnW89G45fAcJAGM6TlqU3XPF_vS_LtLZsyjBGHhODcV3bxcti_1zwTe5wJnnLDp02ynivMnKDbdDrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7492701943.mp4?token=OnyeJKveunLyhTDNpKbD_fptU3Be930BzTWDWWdMgPNVPkSgAg8-iM9bwbl9RoL566K43SNk74q1WB7nVcsoyqxvm01O5rwSV90Xek2LYyg1Nl7jVsR8iTCptWxwKQ8UUVWpgsgSMPXpWmhwzLn4PNPWqQARKUXEgR58CRGmgx5tDUwslVaLTQb4Oo0tXHqkaqnOwlDZmujHLsBHT42oLzdP4HPeI_sYLT2arB4FofTmpucjWqTsucxgWfzxl7Ld5OrCSCeLnW89G45fAcJAGM6TlqU3XPF_vS_LtLZsyjBGHhODcV3bxcti_1zwTe5wJnnLDp02ynivMnKDbdDrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اجرای بیژن مرتضوی بین دو نیمه فینال جام جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135782" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lkORT7pRBLCfaH9uGWdoDnbr0SmLOmYMbMES1_0ePi6FmD5K_BwEwjmJ78J0CprMI41goObdp8PrEpYLVqCwM1wD1RxKSm-liB2AAva0yqI3W2KJELglKOLqKF5A4s6IVQxKWANhtmZWj2StDycLvP7T38qP6K9zguHq0QjgcP3XW83eaecQkMaSc2lOTq2acogPbBwlQbktdaWSysWXF2DOby_e5h7LY652c2xHKHEprcd1uiEtD1oZok9Xxswt7U4twMvb7TY_B0UM78HqcMzX8eiD3Q1MgQmZ2-1veb0tnrfsCxBjA2AKJHjxM9fAy8t-sBkHAqdg4JuH0ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مینوازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/135781" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21017332c0.mp4?token=WEgrYwasRyvH9Y8t8-kNfK449gxmMdeGYKdoo7BFa0Z5SRRytH8AIeayEBQzYb450wTD_DATbgSWnLQPrY4U5MY2QdT9_xm-BIrE0IhDT_sbU-pCfYZaxUo45I8VsVcwaYOCHkWCsx-MQwdqNFYBpG5iGstpQ0Up_hT1DBW6zioxaappkTnPHBtFvxYSmPcJEk-zXNVa9xasxfCnFOoFhWZepURZ6F5Sq5nQMHTdUsStVVHCsauwXfeXCuNHU-GXmJHSweyr6_CupHSGh1oCEnhj2RGWQ9PsOfHDFtAhTZpV49FlDs0UQFLz9p4d0TLbBg-UZBt_AO_UQzgAqq5nFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21017332c0.mp4?token=WEgrYwasRyvH9Y8t8-kNfK449gxmMdeGYKdoo7BFa0Z5SRRytH8AIeayEBQzYb450wTD_DATbgSWnLQPrY4U5MY2QdT9_xm-BIrE0IhDT_sbU-pCfYZaxUo45I8VsVcwaYOCHkWCsx-MQwdqNFYBpG5iGstpQ0Up_hT1DBW6zioxaappkTnPHBtFvxYSmPcJEk-zXNVa9xasxfCnFOoFhWZepURZ6F5Sq5nQMHTdUsStVVHCsauwXfeXCuNHU-GXmJHSweyr6_CupHSGh1oCEnhj2RGWQ9PsOfHDFtAhTZpV49FlDs0UQFLz9p4d0TLbBg-UZBt_AO_UQzgAqq5nFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از گاوی ک صاحب خودشو کشته و پلیسی ک رفته بوده اوضاع رو درس کنه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/135780" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ببینید چطوری زیر ساخت های مهم وطن رو زدن ولی یه عده حرام زاده نفهمیدن چون سودشون تو نفهمیدنه.
#علیه_فراموشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/135779" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdoOC7wd_im8aHakzgNpvm39Tm5TgmUGimfDp_sVzqIZ9B08LM1toa63E2PpeQMgOlGYx8l5wKkutI-7UifLxV-lTOTFlcAmdlGmL1-hukx7sfi6yW-SAR_RhOj7bzukZuDrdwqgj4urMLr00WBnQzT10rx4uXcWn17lhECqLHEkh-N8tATYHJkUBcl2spNvCPilnHCMSvVZldjgCxH2uDh6xF2ZDVLoC8xT3G8_iE9aMjIL-7G8ZqBlLW7Gf6IOx86ij5A-OzBJdm9ntE0AU548d5fi3_q6j1tzRMmqvEmkMTt9arROTkWAxbZyR5PQCL6OgTX1pfDUwKUHBkNNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsmvbeySqL4vQdWiAdFA6z75XqPJfwnZ4MtOks2RVSt3bKoyUWd_3d5ARuE12U2uht2V4YpzTwTUQazzlp09CCcD-7Zxq4XPkNDOlbhpSFiSXFKQhTjbjd8A3mIoW0A0a8ll57RPS_IMYrfXTQreHrbOtZygu2LtbmArQumPfV1aBHcJyI7MNYxe4Wl4h2zjyqt7KqnUwE5K7nvXaCbPvrgdo_y8sfMNcQemK2rN3TBPdHNSlSNHAOrIv3F51XnUjxH0LVmusaFf3JboAeDo-euLhEIid1Dogigp0MOWmEQdUft2Lym4mIXYE-J5hKI6iEpnhaTnfXsEiDxxGVxBhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ملت موتور پهپاد MQ9 رو انداختن پشت الاغ بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/135777" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اسرائیل هیوم: مقامات می‌گویند سفر برنامه‌ریزی‌شده نتانیاهو به آمریکا برای شرکت در مراسم تشییع جنازه سناتور لیندسی گراهام در هفته آینده به دلیل تنش‌های امنیتی منطقه‌ای در معرض خطر لغو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135776" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgMXBNtUcFQYPDT9EWPjYINEaJVv-BLwBkJypERCWBfw14a-O2jwziY6qZqsVYRgDFLcBJHPaNz25xWgEIcZiii9ZoV0cQgio_yHOK6TP-1Z5CdHI8ty0rTO0z500SNjh0zm7F3gA6IdjMj5caJlgje3egchuXU6qS_x3mR3V2IOT9aKfY7vrtheHMoofwSzfi6TS6Q28LuJHj8ywgVGNbomCBh6D0SQ75OuN35y1Kg5UzuU14yeXEG5N2KVGk1cxX-gZ9TGzl_1gRe8G7PV9p2GFTjZfIy9anEZCRTqw1RlWlwKOJDiHBqaegWmA0xCa7GU4aXUYNxRm9UY3YvP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه پشمااااااااااااام
😐
😂
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135775" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیمه اول تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135774" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88873c492c.mp4?token=p_UUF8TmKJE477JXmy9Pqp70appydzIx5oDMJBV_-pNsM-7eAWmJMl50QWW2SwDp2tWkXBXDtBFsmMQtGDLHdTfl4-QlAz9CJmCSpG9HppuJKUROcOVXMooRrjSEEHG_eYKskJtdgqg3ccb29O92pMqsYXy9jvti06UMNKOl1my6yhQPTxtTm20AM_hbL4mPRpXJUwyRAHDv4-Z-W-y120__GNbY3PRQHi4LI9_EldokNs64Ggb_u7gTNWn5xJ-rN0NrxMF57RQ70uuA6_Tv-jF3acgqrcI6DhmY28XYJsaN6Jsw_hy_k8rqv29sUaUZYHD-Q4GSlFFKwqm1gK56IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88873c492c.mp4?token=p_UUF8TmKJE477JXmy9Pqp70appydzIx5oDMJBV_-pNsM-7eAWmJMl50QWW2SwDp2tWkXBXDtBFsmMQtGDLHdTfl4-QlAz9CJmCSpG9HppuJKUROcOVXMooRrjSEEHG_eYKskJtdgqg3ccb29O92pMqsYXy9jvti06UMNKOl1my6yhQPTxtTm20AM_hbL4mPRpXJUwyRAHDv4-Z-W-y120__GNbY3PRQHi4LI9_EldokNs64Ggb_u7gTNWn5xJ-rN0NrxMF57RQ70uuA6_Tv-jF3acgqrcI6DhmY28XYJsaN6Jsw_hy_k8rqv29sUaUZYHD-Q4GSlFFKwqm1gK56IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: کشورهای حاشیه خلیج فارس بداند وضعیتش در پایان این جنگ عادی نخواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135773" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750cf8516c.mp4?token=YCQ5DK5qFO7dEOIX0IaisLrYASu0SmXRWfHeQ8jIw06UZ_t9wFfk-RpfM3JkWGiS92ZN8N3Tr8GsI8U1D3xZAJXkkGZ0XRKHi7oseQofkfVq7TZmxdlC9WjHpDQy7sebaoY_WBQifqp-KJMfiM8EB8DtcTQx09fzJOECFNo6jgKSk5lQLjluC0ilnUrfIRnOCLy5x77jDeva4UdZ7zlCw59dwwfFOAbtELlFohY74BakQk8HHS6nDZsRUAFLqHejp53KNIsMsHAGrtZwWnEgptLG0xbuaRPrgHcIcGBOIaswAC_veYipShmRtywylTkdyn1SIFqjGmoPKEjWG7wqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750cf8516c.mp4?token=YCQ5DK5qFO7dEOIX0IaisLrYASu0SmXRWfHeQ8jIw06UZ_t9wFfk-RpfM3JkWGiS92ZN8N3Tr8GsI8U1D3xZAJXkkGZ0XRKHi7oseQofkfVq7TZmxdlC9WjHpDQy7sebaoY_WBQifqp-KJMfiM8EB8DtcTQx09fzJOECFNo6jgKSk5lQLjluC0ilnUrfIRnOCLy5x77jDeva4UdZ7zlCw59dwwfFOAbtELlFohY74BakQk8HHS6nDZsRUAFLqHejp53KNIsMsHAGrtZwWnEgptLG0xbuaRPrgHcIcGBOIaswAC_veYipShmRtywylTkdyn1SIFqjGmoPKEjWG7wqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک تایسون قهرمان اسبق بوکس جهان با لباس آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135772" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ca28438f.mp4?token=PkkRWtra4DBPCL-s1arCvwBJuZNUX3rcR3nprCNLljjYRtGlWkAtwNznWDiwxtO8d4iaDuEqhEJToyn_p22gQyQaNYYjDPZD-ZYiZSZCQVmO603tpEXZbOmdGM76ZZhH1_hoNygZrkbxiuvmPygcEzvcajl2ygKK3lm2iP5DD6WuP0ehAbUDdVWKTEk9uOETiDov_A1yAS3iTGHDgMj3N_KFi26rqFC61_FkYrmwFhcpKLpZuy61SenC0Kybi4Z3o9a_wVWyGGDIwJEyRODcieqPXl9qymJtuY08I0ChmzHIK93dx0rsQ1kXHmWRZnltIxMOtBqE3pARTTBnjxTQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ca28438f.mp4?token=PkkRWtra4DBPCL-s1arCvwBJuZNUX3rcR3nprCNLljjYRtGlWkAtwNznWDiwxtO8d4iaDuEqhEJToyn_p22gQyQaNYYjDPZD-ZYiZSZCQVmO603tpEXZbOmdGM76ZZhH1_hoNygZrkbxiuvmPygcEzvcajl2ygKK3lm2iP5DD6WuP0ehAbUDdVWKTEk9uOETiDov_A1yAS3iTGHDgMj3N_KFi26rqFC61_FkYrmwFhcpKLpZuy61SenC0Kybi4Z3o9a_wVWyGGDIwJEyRODcieqPXl9qymJtuY08I0ChmzHIK93dx0rsQ1kXHmWRZnltIxMOtBqE3pARTTBnjxTQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رونالدو جام‌ جهانی را به ترامپ اهدا کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135771" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a6cda5ad.mp4?token=BhPNjdeuAyS-n6j64aTWioljIXx21tr2Y6RknTnlt8B4dhCgBJQv5HzNeJdFI2RYncum9N-t0bLbxSFRHvILBKZkoE_AUDehn3V139Ds9O-cKF41u0j7tFgdT0HKMLuKlSyPSX9H-kfN7nbYP5gZG-lM0jdUcmTYBq9TOA93jd6AYny8M8vCRWmGwsFE7OKrs99Rgf5Pk2hkhrif8lfU1yASGcmXW5F8SkGqgZ-sCiuqWXRboFB6JoJNDjaZSIFXaP3FV8W5SfcwJdvBkZ5vyqMnOQL3Sc7EeWKu9QjjIV3Mh63FBdApbNxTO1I6tJQGwy0PI4OhJjJaTWHDJesYuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a6cda5ad.mp4?token=BhPNjdeuAyS-n6j64aTWioljIXx21tr2Y6RknTnlt8B4dhCgBJQv5HzNeJdFI2RYncum9N-t0bLbxSFRHvILBKZkoE_AUDehn3V139Ds9O-cKF41u0j7tFgdT0HKMLuKlSyPSX9H-kfN7nbYP5gZG-lM0jdUcmTYBq9TOA93jd6AYny8M8vCRWmGwsFE7OKrs99Rgf5Pk2hkhrif8lfU1yASGcmXW5F8SkGqgZ-sCiuqWXRboFB6JoJNDjaZSIFXaP3FV8W5SfcwJdvBkZ5vyqMnOQL3Sc7EeWKu9QjjIV3Mh63FBdApbNxTO1I6tJQGwy0PI4OhJjJaTWHDJesYuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چه کسی به خوزستان شلیک کرد؟!
🔴
چه کسی خوزستان را کُشت؟!
🔴
یادتان می‌آید؟ دقیقا همین روزها، پنج سال پیش، تیر ۱۴۰۰، زن خوزستانی فریاد می‌کشید: «چرا تیر می‌ندازی؟ تو که خاکتو نبردن! ما آب و زمینمون رو می‌خوایم.»
🤔
هر طرف این حکومت و طرفدارهاش رو میبینی حرام زادگی بیداد میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/135770" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت خارجه قطر در جریان رایزنی‌های جداگانه با وزرای خارجه عمان و عربستان بر ضرورت کاهش تنش و تضمین آزادی کشتیرانی در تنگه هرمز تأکید کرد.
🔴
همچنین بر احترام به حاکمیت عمان و پایبندی طرف‌ها به دیپلماسی تصریح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135769" target="_blank">📅 23:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / روزنامه «معاریو» به نقل از یک منبع لبنانی مدعی شد ژوزف عون رئیس‌جمهور لبنان و مارکو روبیو وزیر خارجه آمریکا، به توافقی درباره خروج کامل نظامیان اسرائیلی از جنوب لبنان دست یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/135768" target="_blank">📅 23:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارشگر صداوسیما : خیالتون راحت باشه که تا پایان بازی هیچ تصویری از ترامپ کودک کش و جنایتکار پخش نمیشه تا اذیت نشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135767" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWEXElFgmV_sv6SSdz48WWCZR7txUC7I1Es3K13QENEstekxdTEK5VuD0wzioFIRGqAXg9q1WUhTU5YCbLjp-wMV1O_68Jx1EfCMPKjGq1p_EmYa2vN4s6MVl7VZQoFEJWH0JgoQhrCSaqRKvY9E5LN976pI_pRiQXumaZ5f7-zuJ5yRxxPGAzcMu8kEgzZ95v2phYnUT1r9uzbk98UG1jIkCA6jpq-ktNlOrp0TF3mpBVQxDU4mgBMFrXcEkGFe5n2vh3gH070jpcATPu73SjoTpTvIUdnw3oeW2BllNDe-YB4JZfDBwLgJ9f7aK0Uki9aN3fYDdSeIKWP1zQaf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
المیادین: صدای انفجار در اطراف شهر اربیل، مرکز اقلیم کردستان عراق، شنیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135766" target="_blank">📅 23:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAloMedia | پخش زنده ماهواره و مسابقات ورزشی | اَلومِدیا</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ie_GM3540DEFV3-MixkdTLwDqGpWKOKZqgoOVuU-VpgLXblBGvfzHUK4KcdcT3ztVmTaCI3kpHPkUuSE4cgl3c2WDY7D0WOc2oBGhDGTIpWVAYcEA_HjSk2ctHUS2G5smq83Ef0KzYaLMCi2v9ovgGYtbXJHIouO5JOpfJTEwibqsUunhIlrLMrvtCnG75WfWc8BpT7cuZD7z6RMOkkKaNVCsKB0fT8-9SMM25XSFFWGHToKrkgfk_YxRpaze7yyRPjFhWUw9plYX4SF1AmlPIS_reNLIr7eA-kKDEd3OJtM_8812FVRUFtgrHjZxLfRxOL6_DITCfFINKr66sjTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده فینال جام جهانی
🇦🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135765" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود؛ کویت درس عبرت بقیه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135764" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135763">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb1ac4cac.mp4?token=jyunEP928FqxIy-48zrKpYiOL6Q9PbKIEnG_bgXkqk805cuIaNoRGyVRAh5G_610utpUYKQIbyWGpdPztbbJWeryHUX5f2YH8NWjz1v4RcooJZaBezgiumBXlk8ajCAnrHeYxfFNbed39xcjm6vgg1mFC9XqHdBlrhpuRofvcE6xCnVSuYb7zmlReC6p_8KTwv5fKxJoaFpdqLwEGklIOdKDss015RzOtvF-YNV2vZVUINRx0Cxofp6iAZ1AackgQmBhm_2iXEMiZ5St3-Zg0AgSd8mmq6SDJJT5tWosJ-RW9qg27WVXJ4ItHDbZoukaDxDm_1c20bQO32cid1Yqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb1ac4cac.mp4?token=jyunEP928FqxIy-48zrKpYiOL6Q9PbKIEnG_bgXkqk805cuIaNoRGyVRAh5G_610utpUYKQIbyWGpdPztbbJWeryHUX5f2YH8NWjz1v4RcooJZaBezgiumBXlk8ajCAnrHeYxfFNbed39xcjm6vgg1mFC9XqHdBlrhpuRofvcE6xCnVSuYb7zmlReC6p_8KTwv5fKxJoaFpdqLwEGklIOdKDss015RzOtvF-YNV2vZVUINRx0Cxofp6iAZ1AackgQmBhm_2iXEMiZ5St3-Zg0AgSd8mmq6SDJJT5tWosJ-RW9qg27WVXJ4ItHDbZoukaDxDm_1c20bQO32cid1Yqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد عزیزی: آقای قلعه نوعی اوت شدین.
🔴
تو این تحریما مردم نون ندارن بخورن تو ساعت ۱۰ میلیاردی تو نشون مردم میدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/135763" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgvtWbCZvCgeDi574cND2iyUpIv7hZrTXb47g1eDey0e8CI_kuGG9mpffosZATiqbEYPx_d1_WroYN1GIc1-BIMSfUvX0ZrfXjFuUoniSXzLsvSFcjr2i2VH3-5QMLZTyBqti7ekTOz3Giiymuhc9_0YM2TogRQkE05xhj3pJEoMOwMkb-dVAQsBjVgLsz_1OvU0ReCotj5AJsBR5F28qpxSBL5722Su62u4UodVPsjdjE4vh2tdjWzjrH7C4pe6-r41gsSn_xDIU1_jMJDVYTFMMcV6rWfoyFZ-niBdhEzC9Gyir-0rLZixiIOxcP7pXV_koC7QxnJogPB1mA8NJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اینجوری داره پشت شیشه ضدگلوله بازی فینال جام جهانی رو میبینه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/135762" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d43bfdaa.mp4?token=iXjo5FtPfJD4e_SVbXlXSSCkKIicvWYfdgn9eZkQWEQTgunZnrK5X6cu6tWQMbDgLLgXrPtRbWMkz9a5e9cUam3SyeTw41yHvcLn0wiDfA6Q-hMukdxNULCmHjrJcs-sAyR0cKFYRb34UExOP2zup3O766YVdk3p2DegTbS-w8LDys13VNOWz9czjbGSzM8NZjhTYDP9CAynkQvGU_OvX8KhY8fi1MfZlJqIY9CvKv9ssq0P2Qf1QDMs3QAUGBu8snCACYiDPLouAi7EXQVBUUuNrhd3UlW8nzp9DbFbnCHmTE9A-D8BfTD2PbHkeikgPbDpS1CFlpzeHS0wRzxTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d43bfdaa.mp4?token=iXjo5FtPfJD4e_SVbXlXSSCkKIicvWYfdgn9eZkQWEQTgunZnrK5X6cu6tWQMbDgLLgXrPtRbWMkz9a5e9cUam3SyeTw41yHvcLn0wiDfA6Q-hMukdxNULCmHjrJcs-sAyR0cKFYRb34UExOP2zup3O766YVdk3p2DegTbS-w8LDys13VNOWz9czjbGSzM8NZjhTYDP9CAynkQvGU_OvX8KhY8fi1MfZlJqIY9CvKv9ssq0P2Qf1QDMs3QAUGBu8snCACYiDPLouAi7EXQVBUUuNrhd3UlW8nzp9DbFbnCHmTE9A-D8BfTD2PbHkeikgPbDpS1CFlpzeHS0wRzxTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هم رونالدو را دوست دارم و هم مسی را
🔴
من همیشه رونالدو را دوست داشته‌ام، همیشه مسی را دوست داشته‌ام. من اخیراً با مسی آشنا شدم... آنها زندگی خیلی خوبی دارند.
🔴
من فکر می‌کنم آنها زندگی خیلی خوبی دارند، در واقع خیلی راحت‌تر از زندگی من. من دوست دارم حدود یک ماه یا بیشتر زندگی‌ام را عوض کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135761" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135760">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b2786fce.mp4?token=aNPxzxAVhoULtZ_lX4fkXmkbrTrGTWkTjmvT8uOfk6VMRQLT-FkyuNFXKGnqbvxGmwWm9WlT0iAUhdEjPhRGEE6FCGEe_vuAuqo9URpdoK7yVKUWnbtzswLWXBaTM3qOnUyXai4rSnIT1G1djEDZsZ5KEYQgx9SDbx_nJgPW8Ew6WJ6yiATZlKOdXVT1Dcj55kbzxrNaXoRjj_J-WNbzx_aAU7K0r1ymtuIwJS2_goP_iGcEYD5VyT2zfJqNHtMYQFcjhU2JusbX7XqHagB7QuPZxydEzY1Yh4IcArheWC2mBcwhr-MiKh7GgJNeHqZw8O4oQT980qzVnYMEigb9CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b2786fce.mp4?token=aNPxzxAVhoULtZ_lX4fkXmkbrTrGTWkTjmvT8uOfk6VMRQLT-FkyuNFXKGnqbvxGmwWm9WlT0iAUhdEjPhRGEE6FCGEe_vuAuqo9URpdoK7yVKUWnbtzswLWXBaTM3qOnUyXai4rSnIT1G1djEDZsZ5KEYQgx9SDbx_nJgPW8Ew6WJ6yiATZlKOdXVT1Dcj55kbzxrNaXoRjj_J-WNbzx_aAU7K0r1ymtuIwJS2_goP_iGcEYD5VyT2zfJqNHtMYQFcjhU2JusbX7XqHagB7QuPZxydEzY1Yh4IcArheWC2mBcwhr-MiKh7GgJNeHqZw8O4oQT980qzVnYMEigb9CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موگویی: «ترامپ درباره مشهد درست گفته بود، مشهد سقوط کرده بود.»
🔴
یادتونه ترامپ اون شب چی توییت کرده بود: یک میلیون نفر در مشهد تظاهرات کردند!
🔴
یک میلیون نفر در یک شب فقط در مشهد  اومدن بیرون، جمهوری اسلامی قتل عامشون کرد و هنوز داره تک به تک جوون‌ها رو اعدام، بازداشت و شکنجه می‌کنه و چپ و اصلاح‌طلب خائن ایرانی هم فریاد مردم، ابهت بی‌نظیر حضورشون و بزرگترین قتل عام خیابانی تاریخ رو انکار و کوچک نمایی می‌کنه.
🤔
شرم بر شما حرام زاده ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135760" target="_blank">📅 22:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=MDf624_dysnEWOrDw5lLVrNxyEcdO5Te9bfpH-3be7X7rwW4rpVKc4bTc_fA12hRPCBTPPxRYnMMUQie-EbAs9mzHul6SlEA0LldP42_85dyX9miPn3ZlhMy71_3gaLDy5npnNdBViAM5OzRTErNZn31op6ltQhJXFPUfF_wxjNxohneBRwac3cLQ5Tf7l7CgoqkuY12nw58kLsSXSPtP4BdG7XYbFFELOGf7GzWXPwVWd9iooWyuqSkQjEjWTdXieyqrkPHI4vqRFkkKKvqah3hY4GNdN2_6DsGtDmdXXTZygvw8glZZR7zP5oCrRLZnKl9fI0R465S9TKT9i-0O6h3R_vRFC-dlO0AyxpKXWEd5rVX2ZvbnjRgE2rvar9vtkADbJaD_pjNY4Ss9sUsojUqCbQQVr4OLXrMYG39YAIXSrvy5nFaMM4r4lohnkhqGU7VyKe8t5Q9i7bb4jnLs13m1Pu-nOy99GhF3ew6aSVMvhjdjxqBpCqK5Me1BAMJPUzKKB0G-3nzd_8GGVtCZW_sJCknga-nw29IcRORoeDsdckZR-fjCm00eRpteJiOKDGGB1M6rW0KDadCWK_3UCRafZwOqWuTVeG1HAVS-KH0OHCkHmpLgPGU0OMAS103c0E7YIrD4pmEpNNePNAJI7B-K1U5riW2KRWBbKoO6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=MDf624_dysnEWOrDw5lLVrNxyEcdO5Te9bfpH-3be7X7rwW4rpVKc4bTc_fA12hRPCBTPPxRYnMMUQie-EbAs9mzHul6SlEA0LldP42_85dyX9miPn3ZlhMy71_3gaLDy5npnNdBViAM5OzRTErNZn31op6ltQhJXFPUfF_wxjNxohneBRwac3cLQ5Tf7l7CgoqkuY12nw58kLsSXSPtP4BdG7XYbFFELOGf7GzWXPwVWd9iooWyuqSkQjEjWTdXieyqrkPHI4vqRFkkKKvqah3hY4GNdN2_6DsGtDmdXXTZygvw8glZZR7zP5oCrRLZnKl9fI0R465S9TKT9i-0O6h3R_vRFC-dlO0AyxpKXWEd5rVX2ZvbnjRgE2rvar9vtkADbJaD_pjNY4Ss9sUsojUqCbQQVr4OLXrMYG39YAIXSrvy5nFaMM4r4lohnkhqGU7VyKe8t5Q9i7bb4jnLs13m1Pu-nOy99GhF3ew6aSVMvhjdjxqBpCqK5Me1BAMJPUzKKB0G-3nzd_8GGVtCZW_sJCknga-nw29IcRORoeDsdckZR-fjCm00eRpteJiOKDGGB1M6rW0KDadCWK_3UCRafZwOqWuTVeG1HAVS-KH0OHCkHmpLgPGU0OMAS103c0E7YIrD4pmEpNNePNAJI7B-K1U5riW2KRWBbKoO6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135759" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuBWLx0EB0Q5331gUe6X8DscdeLVkLebzSzo472ojSAqgyG5R-s8hFx4iKCPwISz04ghMixT59VHGm8QHx_3hj6e_pQbdU9h-NBcvcfedlP_SWNg9ZbRd0YHJbIrkNiKefMH9jB2-NzZOiYfUDHaHwSL5Ycp5AmfhtJYwc-LmgwO6VJubbm4tRkBz6Xm7KP-5WzEPnw94kjjjC09g5Juif011cNpaa1l484edWFqxPFRFEcMqORwrB5h4JJcnCt0Fq9vKEQOiS8Q7Wp9qOCXQWscZzptmBDZJJJkaDlfyCCwglbouL6K5MbGpaHZu0H7u_e_vbkY7Ak9_PGWR0m6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظامی دیگر آمریکایی کشته شد
🔴
سنتکام: فرماندهی مرکزی ایالات متحده (سنتکام) روز گذشته اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه، دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد.
🔴
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
🔴
به‌طور جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
🔴
یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی تحت درمان پزشکی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135758" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/135757" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گفت‌وگوی وزیر خارجه قطر با وزاری خارجه عمان، اردن و عربستان درباره تلاش‌های انجام‌شده برای کاهش تشدید تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135756" target="_blank">📅 22:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf8f7HM0Wx_BQTo6PTcPXMJtXztq6laWBqmpD_IXG_VM9tSW3JwlrWvaPCxIyIdk34m3c9inY78tMa77KExOQ2PWBgaW19GpDtmqBQ1KcsRfaPxsZw8INbBKQuvycZC9RBNGglOJK3i1ENBl1jGSfkA6lGtlazVYG71O_AIxOeSxmG7w3W0EjZ7DqOvSCcyIHMMEzyryK6QzKqfCxsPX112ogIWMBjhjYIUpoiRnd-xe8tACqzIs7fgGaVrMWzPbWrFXDr2Bsp9DLbfOK9t7bVe0q7rfkun_T9mqMB50oGspsGwS1wqkWlU9J4V6ISkqfeFKpT2Ot8EeoMX3xGaLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با هلیکوپتر وارد ورزشگاه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135755" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doQWz6bXOOF_HTmg6NHcQawiK26uussfYsFouqUAhmyO5xJJgLvU4HpD22TOikIzNeLTZ3CTBfllXlOK71FyldDk03tcg5pLk79Ys69LrPWu5nUkM2DwnvmNCxWPs0IyB4jRrVAK7ahWNH4mgifA-4eaTBZoBizdpes7eETNwDJLntkZTpOI_dx6SGCeGU2mRtWkyLAXsiVj7vPIW2MqcD-CVMp1M5UO_5Jo4woSdrONw8yfzIi0cwVx3caX-ulZNOPSR3pWT_f98qY8kJh9eZ-gVjdnyJO-taiagUKecDZzVPJfiqN5WZCpGDyb23Yvi5eHQyhUTGSseGQYCeGm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از دونالد ترامپ و جیانی اینفانتینو در ورزشگاه مت لایف
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135754" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d206001ec.mp4?token=ugQJ58_Zn5xO8G7zGlDSVEvNsStqi1zZWwqJcbJxVF3sgYyotHunm9EG9TDJjEkeOPkrwfcfT2X0bFOLYEEHXpqGKEu24z-hcezFW2tA6QUwh3ULM7zmheRPDfTZ7cHQMfRbgMwl8IgRsmfjUXpLwmQGh-vRuzFcMp84nDfyGAi3SCjp8CiGDS3e9kOMSBYL8zkGEu9TECeN5zzxXPGg8f8IZu9s-AcF5up_UHdBkvnc95Sg_rBoMGAYRqDXv3XOF3bdesMhoInl4McpmxOjYsQiqS_kuSwU2y8-xhz7PBLqsU7kuLPKeMaIokL9qSGX3SiEGN8kuZp7vhbaSxEJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d206001ec.mp4?token=ugQJ58_Zn5xO8G7zGlDSVEvNsStqi1zZWwqJcbJxVF3sgYyotHunm9EG9TDJjEkeOPkrwfcfT2X0bFOLYEEHXpqGKEu24z-hcezFW2tA6QUwh3ULM7zmheRPDfTZ7cHQMfRbgMwl8IgRsmfjUXpLwmQGh-vRuzFcMp84nDfyGAi3SCjp8CiGDS3e9kOMSBYL8zkGEu9TECeN5zzxXPGg8f8IZu9s-AcF5up_UHdBkvnc95Sg_rBoMGAYRqDXv3XOF3bdesMhoInl4McpmxOjYsQiqS_kuSwU2y8-xhz7PBLqsU7kuLPKeMaIokL9qSGX3SiEGN8kuZp7vhbaSxEJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 14 عبری: دستورالعمل‌هایی برای گروه‌های مختلف در عراق صادر شده است تا برای رویارویی آماده شوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135753" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرگزاری عراق: نخست‌وزیر عراق در پایان هفته از تهران بازدید خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135752" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8rKz6nawNYrkvjiEjK1Th2hHrsBoKACd0908jfA3ACQS-k-JCteFCYUOTApj0ICfl4GhNEt5QbDTpRMMLNeGTBtxIW9swaFw0ariJffFmaaK04CzOF6Q1A8JPCsOC-4tY4izGXI_bhhRYjwmc1HGyrzckyxZJ5OvwcWytY8MQuQMb0wZJcDWJgZZxZEeq7GY5qwLoq2RcThgmAgDOPWoxd0dJNQJL8nnJlnfX1ENFhFbVJ6shf4B0CLVT15KXLTgn-vT1N50F_1rhWjqrMmL0TwXWGqX2MN-I_eg6vAcezqbxxXdUKkCv20K7evOshXEHLkupFMWNTJELTsvEDUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvp2Of2lhq4nSf7KbI9H_xjbhjDaKqBmaiauCPKrCUd3nDpVnaAtsvZ8taRv6Rv0yh_d3_zhfPGQ3H8bETe4hKUstqwFmojAzNzQeePffm8FOjApFOTGlYxBsYfQxoCGW0XOfcrZ_E9izZH-29wx6FddI4uSYexfSRhHGThtxp4eOjsOBvhagT8_IqN5nhLzN_Vt9eGjrCLxz_9tWQft5JNcsmV_Hpgl2-P-VfiJe0Qmkl_oJY6swZF6gJQHPxNn6zX3aGkY4Fpwyqm4b-KEmNjf5l31lSEaepvme3P7GcQ7ql5gB_zOwarmpB_Z_IY-Sbe2Whxq0Vyfp0xuyCo9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-q6_ezigMdcXLN_XAuBf_5XqJqf2gI_yAMk40KKCWXR-8Ir0Eorf-OUbQke_wsoZXsJBRJlTZ9ApfJpmpa8pqBaBn7teZKXWvm9YE64mkizW37JW4SzUYGxHJcBVH-5GM5C8BNs_n_fgWMv0fUO7QJTyLL1jN3Afgsnnf_Il9IuHsDQNpD9i64WUPt3NIFksGlbK4Kj8XNSPe1vlxPcQ5lLcp95TQLbD1IVF6FWVROUbtpdGKs1HasbEy6WcNBJOJboGcdk-N_-SN4d2GZvEk9kPCiRwCAtFNeD7WwQ0kJ7Msh4cHbRtsDtlP4lW8D1akWoB0rqeXUnCFxSQpRcuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ در Truth Social:
کاشت درختان زیبا در کاخ سفید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135749" target="_blank">📅 22:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کانال ۱۳: ترامپ به میانجی‌ها گفته اگر تا پایان هفته آتش‌بس نشود، باید خود را برای تشدید تنش آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/135748" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بر اساس اعلام مقامات آمریکایی، ایالات متحده جنگندههای اف-۱۶ و اف-۳۵ بیشتری را به همراه هواپیماهای سوخترسان به خاورمیانه اعزام میکند.
🔴
این اقدام که پیش از حمله اخیر ایران در اردن که به کشته شدن دو سرباز آمریکایی انجامید، دستور داده شده است، همزمان با افزایش تنشها با ایران صورت میگیرد.
🔴
به گفته یک مقام نظامی اسرائیلی، ممکن است برخی از این هواپیماهای اضافی در پایگاههای هوایی نیروی هوایی اسرائیل مستقر شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135747" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135746" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9J2o-n4bdZaHgj4F562i3OoWq-relBgq0P2T5SzmJ90ZoyNXtlJ0OdLt1VmaLTJyjOnqydOL402jvBwy0AFJR6T3eprtnNEO_opEBNvbaDfL5YYaiuXxolqSLozgTtJzQpUW1A6PNG68fK4URdsj1Wx2qvqKOo28Gp1UTOYBjk7VBPfOHXM7kdEyAxN3bquhfohjI-KawEWktIFwaY86TS_8YWDSHb8mv8r9miFwFETb4hkuXHNOlTNHbFhdkjPBl9-5D6_qNicmUs6IE4-fG0i-eO2sjEHim6J4CUuxbMP-ERM6W_ipUviVNa7rwyFDYym-FU2uBqpiiIISaKWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUa80J9WwaafcLAnyg3fTFHNd1C_C0dgVvh6JPDLQrhbngeJcClRFVej1YB5Zzp3Az2wfRh8_Sg2VL11x9uTivB-xa7HuW9kuDDGlDAi_RR91PxCZZbdmf-qTjMFao9O6POE9-N4r01MUHQySlUV--L78lE7uybLbvbx-AQne1eOexKmIQYcwguEO2KWmDDnf2Aa917intRywGu3IIzh2ZBN0_IUFcJhI47QBNdAvkuazHe8N7bHYTFSy6F4imvt4_g3UQtfyBbit-l2yqMNX5ZdBRiXqNfGm4eYqPj2ukkDm15UGUCXm5mjpl2uLmVgQImJhPUeUjFMfc9RTDANMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای منتشرشده، آسیب به پست برق یک مرکز داده بتلکو (Batelco) در بحرین را نشان می‌دهد.
🔴
این تاسیسات به عنوان یک مرکز فرماندهی و کنترل نظامی ایالات متحده و هاب پردازش داده‌های هوش مصنوعی عمل می‌کند. تصاویر به نظر می‌رسد آسیب به پست برق را نشان می‌دهند، در حالی که خود ساختمان مرکز داده ظاهراً سالم مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135744" target="_blank">📅 22:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نیویورک‌تایمز:  دسته جدیدی از جنگنده‌های F-16 و F-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135743" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وقوع انفجار در اربیل عراق
🔴
هنوز جزئیات بیشتری درباره علت انفجار یا تلفات احتمالی منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135742" target="_blank">📅 21:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135741" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد«گروهک های تروریستی» به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135740" target="_blank">📅 21:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
منابع الحدث:وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135739" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
انفجارهای مهیب کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135738" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کان نیوز به نقل از دو مقام اسرائیلی مدعی شد اسرائیل ممکن است تحت سه سناریو به حملات علیه ایران بپیوندد:
اگر ایران به اسرائیل حمله کند، اگر اطلاعات اسرائیل تشخیص دهد که ایران در حال آماده شدن برای پرتاب موشک یا پهپاد به سمت اسرائیل است، یا اگر ترامپ رسماً از اسرائیل درخواست مشارکت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135737" target="_blank">📅 21:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از یک مقام اسرائیلی: واشنگتن تصمیم گرفته است هواپیماهای سوخت‌رسان بیشتری را در پایگاه‌های اسرائیل مستقر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135736" target="_blank">📅 21:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۳ عبری : پیام ترامپ به کشورهای حاشیه خلیج فارس: اگر ظرف این هفته آتش بس حاصل نشد، برای تشدید تنش با ایران آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135735" target="_blank">📅 21:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135734" target="_blank">📅 21:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الجزیره مدعی شد: خبرگزاری رسمی اسرائیل به نقل از منابع اسرائیلی و آمریکایی گفته که واشنگتن به اسرائیل اطلاع داده است که قصد دارد حملات علیه ایران را در روزهای آینده تشدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135733" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvxUFBwJaNRjtSDlX4mGUErXg4LC0SubmOuSxfsl5pW_wyUiPQ-5vwSODedbuLBOP72pKZzDqatvFBF_8S695-H0WJzbhfQ8wAJZTy946x6HYNMvhjQZE0i5i4zoPS24oP7pZyHfMa1Szq2d5Oxjd8WMvTH9NZ-w4oSOS0f6DG8zsfBhMMao5pPqFnh_Sh_zMaCYNkZ-jlxwA-paEm3s3LmrMg2wuIwiUFcg5_Iqudf__rUJvIph4gj3YY9Sd1CbB3rb0LytjctdU7X8LMP-PP04OJMHgf3IonHPakUdHFbIhzPFdiwVoH-RLlfRVSq9SuavKwqxtXSbfcyvDQhfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی و تام کروز قبل از شروع فینال جام‌جهانی در ورزشگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135732" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135731">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خبرگزاری وای نت: انتظار می‌رود تعداد هواپیماهای سوخت رسان آمریکایی که این هفته وارد اسرائیل می‌شوند از دوران جنگ پیشین نیز بیشتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135731" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135730">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
🔴
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
🔴
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135730" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
