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
<img src="https://cdn4.telesco.pe/file/AvBv1WDOjA-Tdzre853p6XtM6MerS3tgkE0-F_Tb8JyjOTdW0NyqgRhPKo8jdckQtIjH8WmeYPZ3rHOOEkJrPiUIGMa1hUsQtLhl-QOHPhr2WRDTJG9AfLO4IUlT9_OugJQBLy4oUbc5CBaa2HU45qn07SLxyhaRd8RK-yBsWtPHVZqDAdy8axthzPStVBmv2aDBZysWzVTMUWBfqKfRaAT9TWekADyYoBrZhf01NtPpWYpSOI6cUr_pgR85-DbI-8qwFVATSbBPNuW0Eamrm8pyiCzZyqWOToK77EerTYmmTm1h_UQXGG8-Ys7bkIM4CHs_I6wprhaqTSamiMEO1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-458427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cb43c720.mp4?token=afmu9wWjo25XYY0xZqRY_azHe0mMsFGyGWBqfw8MG_gVI3RMnEkAtfhkYM3nDxd-4J1qtYmaBfniFfsvHf7KnFK1c6nL-p4ybyUNTSRpMf5QXj0GeEESYOetw5_noCZzJDBGyHH7vsuEkxfe3MlCncFC-Hv6S4gVXd_x4nX68yDscpuQc65ZVTPzWV3GKNkjl6_sBJisHKdgIhUKmVF4em900cM3f7LttaFnI2avnReY8V9cMJEePzxyZ-blO99yuUfEH24BUkwwqhYSYs6z810Dx52tY4vEYUrpjnbFbwfjwVQjUMMXCiDetU-FaF1qgTxcoJDJqZmsL6rv306bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cb43c720.mp4?token=afmu9wWjo25XYY0xZqRY_azHe0mMsFGyGWBqfw8MG_gVI3RMnEkAtfhkYM3nDxd-4J1qtYmaBfniFfsvHf7KnFK1c6nL-p4ybyUNTSRpMf5QXj0GeEESYOetw5_noCZzJDBGyHH7vsuEkxfe3MlCncFC-Hv6S4gVXd_x4nX68yDscpuQc65ZVTPzWV3GKNkjl6_sBJisHKdgIhUKmVF4em900cM3f7LttaFnI2avnReY8V9cMJEePzxyZ-blO99yuUfEH24BUkwwqhYSYs6z810Dx52tY4vEYUrpjnbFbwfjwVQjUMMXCiDetU-FaF1qgTxcoJDJqZmsL6rv306bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله یمن: دشمن سعودی در کشور ما جای امنی برای مزدوران خود نخواهد یافت.  @Farsna</div>
<div class="tg-footer">👁️ 656 · <a href="https://t.me/farsna/458427" target="_blank">📅 23:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWsCNM5dtAcjHYznUGH7SHHHSnx59xwdCoN0OFf5cFv9Qa8JsAebsihkvGrNDaflI3QqRz7Kc57cWbDZnp-_-qrfnnNIh7cTL87KoJ5J5d5xaUpu2ofR8B28gLpN0EIsEsDhgUGW7vqzsFsKousXQ9WbnSCTkOfoMMkv_D-6e2YykcjIzpSD5TXVZuVAN4jcL2AzGz9Ac1ueyaN_f5QQ-HfWmlWytMkm2AcK_IUBvTTa_hmE0LG07EC8CbPwgyRf7jEtTheXZHw8dqEX5lOrD-aALNJ7jNoJ-pkB0Nhw73fjjrsf-IbdpxGaJ6D2-cmAE6SclDw7IxXy8y1Vzuq6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله یمن: دشمن سعودی در کشور ما جای امنی برای مزدوران خود نخواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/farsna/458426" target="_blank">📅 23:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu7oSgdGQP6tcn8hsFyoCquKZgpKldkwryWBA-6YUsuNBElbUfTFm5HcN1MRCr4jWSa1mR0sDkHT2uZA1Amm1T490NYg3hW-_9gxySNRfQtGrV1ol5gsXpYQDNUOiHtZyTaT9ynTpCtN4SbHVHNY1TwSMeWN9i34VbCvD4ifHm419pxgduK3NBQuhfZXWpS_k0tAB6XErtOYj1r1pFdveKaEymsq_-OulaUnzuK8n1mgv3ATY1f-B2P4tAQFTClvS04wQ_ODaBZcrnufBYvVmRr8Ur4vKh4S6p3KzvwDd3E-WrzRN-AsM7drhGEUj1ctbiBsTRevP094vk5StgnkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: سیاست آمریکا علیه ایران به یک نمایش کاملا مضحک تبدیل شده
🔹
واشنگتن به بحرین متوسل می‌شود؛ کشوری که عملاً هیچ مبادله اقتصادی معناداری با ایران ندارد، تا ثابت کند «ائتلاف» آن در حال کار است.
🔹
سپس مبادلات ورزشی و دانشگاهی ایران را «متوقف» می‌کند؛ مبادلاتی که سال‌هاست عملاً متوقف و بی‌رمق بوده‌اند.
🔹
تحریم‌شده‌ها را دوباره تحریم می‌کند و خلأ موجود را «ائتلاف» می‌نامد.
@Farsna</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/458425" target="_blank">📅 23:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peL3SBZoERx0_eJFOcYH0aOfyKocrMBpfIBnlz_K3vwYQSJ8dqBODvrS1JaGG-J2AS3XXaxt6AmfyorvzjhieZsS29NgY4thQqIifBPejVDuVD_1N1G5FeMSNzMEKm_g68gTZ25vEhQAFCVYi4nKob4rexaoyb5j6XlUvMzzfiJzi6nQpOSmzTq-3y3_4MMroANTIbX5vhp08zm-FSizz0bSNR_4-jUk9f9DBVSpjSG1je1FKUbME0-81OvzY2-gxTfpjocasd3EoHD2L8BVR6bsJI5oY60cAQqGCNXkBchkbpiUt2-WGZJ5d00oTRUBziEkMXQyoYuhgeQmfY73Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
موشک جواب بادبادک!
🔹
پاسخ «کمال شرف» کاریکاتوریست یمنی به تهدید صهیونیست‌ها علیه غزه به دلیل بادبادک‌های کودکان.
@Farsna</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/458424" target="_blank">📅 23:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkWZdiH5zZR35UMuQP7J3DfolxhrRpTfsNpV2tRULaoPWCk1cXmM8_Fawfl_3EjTbgGdgi3JmSw34sNJZpS0rxDVqOeGj0FaunB-HL5lxCG7bZjMF6d3FULzyoHdJCYwzUvgJgwEgd-N5s0iBt-03UAT__Nx1nkLFzOFbzdAM4BE4ID7LYqTbTsJito5dMP3jihosM61kLr_C_DecdkbnbDIbCUmrC4OfkfaAwizHJ80lAGuG2ggXbH44VxH5q43W33sVIr1_U6ukf2XdhwH6uysJ85vvSWPymWKuexk4gIV63TvqdPt1fQ-iMSDbZV_q3VK6Ks2icR1XuAITmFuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNN7BJFN2VAfb5gbvN3QdM40UrJkVNuiCV4QGEvvLYZig7TNbRtsglMyaQfFyuD_YSu__15pZfuJF1PCjz6pck__0j4LDSEwn-OT9inO-retPFAH4bmYFMi05UMl0oPOKl-iOXYofTlIsWUndKN9wkD_ba6OD3rIQVC9eN3BQYsahxZ6PRLDHV70yiAGbIf1C23Ce7d2s2IZBgIh33M9PpoO6pxe2XTZVIHW4bGFgakSn3gSpEulyaayLhfh8_HyhugPCcTVmeHFIM8dmTog5SwLsI5IE38U8Btp7vNTu9Ey8JLC8x-yxXeJ3x4xBcuCeRlUeHVRohWpN8O_BzRBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGfqB6uFdxnrX2x4-XAW0yt9gPyLC0BIqDVVD6-dvirrBS8nDKOPaImkpAXxvzpRQ4vqjZ6Nj5HCSGzbqRQD_UlasAP-fLMGBQhoJq5BROhGG-MDjYgXsOooCjXcut7VwdC9R_DcfdlXsKxbqxqeQyKykTt3jjPrIgvM8DlbzNtCVI1CxqZovca_Qc0pAF33jTKCFVn1l00sYDKkh18ZTbBaQY9dO3uL1HtZzs-6Kd8xpKy8qJG5PJSY6GxUzme5kC-j1Q6MkRr0uO9yN7ZnaQjwsB07u0Yn5rFkhoDxHu2CL3Q5hp2ZOs7UsaKVos07adL1SVxg58j47iD5jSK7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnXlriBBvR4kOCSeUiRTKL5J7RnmGjafqKI6Y0GjaX7ZvatjOo1ZXxuVjhtaX4LIWVGhKdn2Z8yfWbueSQ1CqRlVKdSRK4owUOhSKC-IqFyeud85-8UWs2yN2b1z9JosD6qAtULZeMe2S7oq4840kYP7POG8kVJq4_2Urnq6354Q4aZ7hcOZ0-JBd9JFa4Zz3h1HL6gj-2s0osr6yz02XLeKaPVejkbrT6dkH0IzwSGeFH4aKnf7eNuc4Osv-uZRIVBoO2ZJODJVZgmAL1aMxV7h2zcDtoLscdUYwXYwWU1yz5hjS1-mu3xaFDuCvbgN6uhkbm4GVkZUFSbN_rM46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EguxQI3GTSCxj_P9cKXroDryCsdyArghBqmc0hD3CDPN34P6pj84qNyQFCdKC3HNNg93SHhaw6TkKsNgSSSfxL2ry63xMFjjW9ZRDMWp8V7sUwQYHjYiAqmetYKhjLNAVALygxsNkRlYmvqWm_Nhshk-32aE3tmMy8fVbGM-PqqyYmfOXbhL_rD5CDuD1tcsdPEvPqRNXs3zsENL3eKTDpauLcJWA87HtfasQTssGm1vFzNTYMAq53xRjfAtOchi54GtDBLb4Fz-uagWtjsziUdVtK6LmR1ZmGyQX_BCFGogfiv94BVj5Wj6gbKZGNF9e4ju6vjPSnhEp3WsKP9KnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت شطرنج‌بازان در مسابقات اوپن ابن‌سینا
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/458419" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf7a035dd.mp4?token=ct1nOwWC9qQecEaBVP9SZfrua3ZkhU-FYAEtI-40IQ1wSWlwrhaDE0eNKvNjoA33i63ZyH8BXE2HUzZHDGLQ2TqZCHHDXYnR26DQ1dleBMtllXIFAX9OzBCSnSd5aaGHdjCbFLpp8TxRMUv873qaMxV6kBgcUCTOJTfTbPoiDAWYxHWPFAS1h4MqfKLoUr1-SiEfkykP7s06PryApEQayw4Yyw7WfRA9k1LaWd8i-LT4wtptkO5JOCVwbZWPNKyW3x-bUTEQVyHHbEWx6VPtvCP0Lw5eFw-W0TiGMA0bi_O3LS1MPRM4lJRnBgE3uE5vimb7UaGHved492Imqh9ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf7a035dd.mp4?token=ct1nOwWC9qQecEaBVP9SZfrua3ZkhU-FYAEtI-40IQ1wSWlwrhaDE0eNKvNjoA33i63ZyH8BXE2HUzZHDGLQ2TqZCHHDXYnR26DQ1dleBMtllXIFAX9OzBCSnSd5aaGHdjCbFLpp8TxRMUv873qaMxV6kBgcUCTOJTfTbPoiDAWYxHWPFAS1h4MqfKLoUr1-SiEfkykP7s06PryApEQayw4Yyw7WfRA9k1LaWd8i-LT4wtptkO5JOCVwbZWPNKyW3x-bUTEQVyHHbEWx6VPtvCP0Lw5eFw-W0TiGMA0bi_O3LS1MPRM4lJRnBgE3uE5vimb7UaGHved492Imqh9ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جایروکوپتر پس از گیر کردن در کابل در نزدیکی سدی در شمال ایتالیا
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/458418" target="_blank">📅 22:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962f8ad5d2.mp4?token=amJXDRps-jT4uCXCdGPgm8T0N2-qUiSfLDEJujCVMQ5ucjCfX52gmPe9QaXXEB0b1NgSFLDCzow9uXJjCwTE00mR639nbJIq3Mcx3Wfvf4sMOW-3FbQy77IOJyITnvkXhuphuyqFvgQiHFwcUPuHSelfZm6gBa-w-0rUogOl7Ik0auEClNBjF-H6_bEqICLUaEJhG1KinCDaO8V1kfqgWQky-tkqWhrqk_hmTqkWW9umwBwpic8om6LD18vXCjtV92i0O5XRU51LI6bMcFfmBryhOTcFJFZFF2GEM8pQbnSp_8TPnYDL8F-lx3sO7YJpukzYgYk3wodcmhN2Boxfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962f8ad5d2.mp4?token=amJXDRps-jT4uCXCdGPgm8T0N2-qUiSfLDEJujCVMQ5ucjCfX52gmPe9QaXXEB0b1NgSFLDCzow9uXJjCwTE00mR639nbJIq3Mcx3Wfvf4sMOW-3FbQy77IOJyITnvkXhuphuyqFvgQiHFwcUPuHSelfZm6gBa-w-0rUogOl7Ik0auEClNBjF-H6_bEqICLUaEJhG1KinCDaO8V1kfqgWQky-tkqWhrqk_hmTqkWW9umwBwpic8om6LD18vXCjtV92i0O5XRU51LI6bMcFfmBryhOTcFJFZFF2GEM8pQbnSp_8TPnYDL8F-lx3sO7YJpukzYgYk3wodcmhN2Boxfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ وقوع سیلاب ویرانگر در مرز چین و نپال
🔹
این حادثه تاکنون باعث مفقودشدن ۳۸۴ گردشگر و مرگ قطعی ۲۲ نفر شده است. @Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/458417" target="_blank">📅 22:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42adedf52.mp4?token=Bfpg1zBlu5IQ_4YMfFz2qLc-cP_6UAsmXff8VNuB4uHpzmV6IEDqYivgxqpXAChcpjxEqJKI-iwq1nIhMX15FU2QnqRgaZ9BjN-WuHpYDkFze486obFeW3jtMGIfGm59DRxjGiLMj-Y09u0b-Yie0dFWVonhCmsUon9PhI5CEHHZvyJzi4SOr9otRetLo4lop4CQ-rb0jfSOtqJVqwhdyfJxIJrcGzyVqzu9CPoejriDrszLEexoSGbrAYuzHKLUYs0E9__EedjosrxSKzZAVcq4QD0C0cOrjYHaTSHJ1HkqE8DxH-1cs2XcusU8uWsY4CElQ4CJjB8nBMmKZnVhTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42adedf52.mp4?token=Bfpg1zBlu5IQ_4YMfFz2qLc-cP_6UAsmXff8VNuB4uHpzmV6IEDqYivgxqpXAChcpjxEqJKI-iwq1nIhMX15FU2QnqRgaZ9BjN-WuHpYDkFze486obFeW3jtMGIfGm59DRxjGiLMj-Y09u0b-Yie0dFWVonhCmsUon9PhI5CEHHZvyJzi4SOr9otRetLo4lop4CQ-rb0jfSOtqJVqwhdyfJxIJrcGzyVqzu9CPoejriDrszLEexoSGbrAYuzHKLUYs0E9__EedjosrxSKzZAVcq4QD0C0cOrjYHaTSHJ1HkqE8DxH-1cs2XcusU8uWsY4CElQ4CJjB8nBMmKZnVhTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم مقاومت در شب ۱۷۹ مردم مراغه همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/458416" target="_blank">📅 22:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79725ea990.mp4?token=SrP6I6GG-76eIb0lp7_LE08Ham8rA1nSvj__TjAReC0C-H7R_--sa1lmQtdhROPxiyDkAG6OZCKnp_gJsRDY4tzpfH6xCnTCS3kMzd2p81o0AkiXaY-jyxoX20G2MyxyGc4Oqcgj5rL1BYph9SNSNKQsLZ7AgRXtDheYzWyhdCeKy2JsZpZ2cJ-06V10xquPTOejnhtM_-FrjLS2BOeW_0dS-ApNMvbV5Yy41hFKOzPGiJVkYsuvPadwg401IGlyR1RlRrFXcJuvlzi6dSyddEryScibCoi4zfINLDq7dcYuWqHCihWmZJBBxE7h3CO6euI_uKQ0UgdrwkQeJbE1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79725ea990.mp4?token=SrP6I6GG-76eIb0lp7_LE08Ham8rA1nSvj__TjAReC0C-H7R_--sa1lmQtdhROPxiyDkAG6OZCKnp_gJsRDY4tzpfH6xCnTCS3kMzd2p81o0AkiXaY-jyxoX20G2MyxyGc4Oqcgj5rL1BYph9SNSNKQsLZ7AgRXtDheYzWyhdCeKy2JsZpZ2cJ-06V10xquPTOejnhtM_-FrjLS2BOeW_0dS-ApNMvbV5Yy41hFKOzPGiJVkYsuvPadwg401IGlyR1RlRrFXcJuvlzi6dSyddEryScibCoi4zfINLDq7dcYuWqHCihWmZJBBxE7h3CO6euI_uKQ0UgdrwkQeJbE1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی سخنگوی دولت با بازمانده حمله به مدرسه میناب: همه دنبال انتقام هستیم
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/458415" target="_blank">📅 22:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca671053e9.mp4?token=b0B1zSs1uGSvhXwwbu68Z5fihMPhPU5VGoAKljw7HyUoXOjih3YrTl7mQU0t0pH_0E3UlSbHCDnF1pvKMAMsB6EZtFdBRAk_m48_ZW8WGxMr-5H0_4n3M5kXOFUbz9XwgGJ0TlRMmjZRcN7hQPp5R7sLIucXl_qQLJ5ughTWqqqe-vjjZNFrE8YFjAkEvK8DIthH5nQSlBZbd7vRyF_WXIYQFEoLdy2PMkBt6VUwe8VRSwVqZsC_Z7aD4YuwUBz4vI_7nYFuzXIYuVLr2F7LJR1Tp90K4YaEpqP5WfCEDNo3fzMAq10jUD9KAYAo52bgFKiJyNw_0pR2U9oPs8fflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca671053e9.mp4?token=b0B1zSs1uGSvhXwwbu68Z5fihMPhPU5VGoAKljw7HyUoXOjih3YrTl7mQU0t0pH_0E3UlSbHCDnF1pvKMAMsB6EZtFdBRAk_m48_ZW8WGxMr-5H0_4n3M5kXOFUbz9XwgGJ0TlRMmjZRcN7hQPp5R7sLIucXl_qQLJ5ughTWqqqe-vjjZNFrE8YFjAkEvK8DIthH5nQSlBZbd7vRyF_WXIYQFEoLdy2PMkBt6VUwe8VRSwVqZsC_Z7aD4YuwUBz4vI_7nYFuzXIYuVLr2F7LJR1Tp90K4YaEpqP5WfCEDNo3fzMAq10jUD9KAYAo52bgFKiJyNw_0pR2U9oPs8fflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌پرچم قرار است به‌دست نسل فردا برسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/458414" target="_blank">📅 22:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5YgyZoqZDHwNmmztJxSu4Hxhyi5fYUdBXihyBfHTXlhG3IkSNeisJQ1et65vh82yaoE-NDInPwZAPx5jjq2-bamYXPKFIV4_SfeUeMQGs7DehFB-mEtD61J-2-qxzKEt0xrpMizhT6SrcaXH7gOde8JvtBFXZ1vUwNGQvqM74jJCHD_n_1TrmmPxqdbcBsdNfHj_Ltz1IDtzQBUaH_2g0ZS5rmlRopv6Rx9--MfUg-Cb8XOrIIvfKuigzdVfoIsP_yFNgb6XxuINsxSrgranyNwMbOfwbZtluYNhQ-U5b2jaGYLDpKpD7RzPJ_lx-BvtlI3sWFUoqwLaq3kLnl80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر قطر به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه از سفر شیخ محمد آ‌ثانی، نخست‌وزیر و وزیر خارجۀ قطر به تهران در روز پنج‌شنبه خبر داد.
🔹
این سفر در چارچوب رایزنی‌های مستمر ۲ کشور برای گسترش روابط و تقویت امنیت منطقه صورت می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/458413" target="_blank">📅 22:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680415bf29.mp4?token=r-yRg6Qa6TCZwliUD___PeUHRLidS473Nf2mg3lGTQXquviCVBn-yVNo9g8i0m-GTO_zvMP6Jo8JdkdGLke0g7xL4gl9W368tdSxKHAka1npK4Oci_i4Iyc6zxVzTFf8j-KA2Otth4gdiSH6Ar47D0e35QzLviSSLn1_c9cAaBf6j58UGCZBwoF2QnVRJAGua95QxvNySXXJ3V8cZy4CDIECCLO5bakMbeEB5ca6N2s4XXXO0vAVyR1kzmYBltqqP1FoE-__Vy-svuM95YVL0B2WBp7rsP8KStWqKyLXV8ooI6-cLdO9wq38KXAAfkKo-bFl43qmd030ASJOHLNiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680415bf29.mp4?token=r-yRg6Qa6TCZwliUD___PeUHRLidS473Nf2mg3lGTQXquviCVBn-yVNo9g8i0m-GTO_zvMP6Jo8JdkdGLke0g7xL4gl9W368tdSxKHAka1npK4Oci_i4Iyc6zxVzTFf8j-KA2Otth4gdiSH6Ar47D0e35QzLviSSLn1_c9cAaBf6j58UGCZBwoF2QnVRJAGua95QxvNySXXJ3V8cZy4CDIECCLO5bakMbeEB5ca6N2s4XXXO0vAVyR1kzmYBltqqP1FoE-__Vy-svuM95YVL0B2WBp7rsP8KStWqKyLXV8ooI6-cLdO9wq38KXAAfkKo-bFl43qmd030ASJOHLNiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید اسماعیلی بدون از دست‌دادن حتی یک امتیاز قهرمان تورنومنت کشتی لهستان شد
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/458412" target="_blank">📅 22:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e776ed28.mp4?token=ezrVXfOhQwobSQlobccycU7BFqR1tTFZkMUZUVPtH15yRQWjC9uoYaXmhFQAUIkljjqSYsh8rUaYsNivgHQcmvHO7ZOFh5HdV8SDQy3zXOXUf4aSKepSup4HhZkx-ColjP5DclcbeIREd0earbqazxqiyJuvK7ToPj4_1UmSlsxAw9JAB6h_XwFZzgHaFSIS5WS6xo_pipWCMGwiL5aZM20VOgHxu2YvVOe4ezIa1dGSdki7GP8dwCcGSXrhyI2x3On4xEZJTYb5AphtBm5sgZYsjvec5JEYP1amzOe_sT8FfpRjODKjOKovSuDvdFtugmGdg3vpUicX8hTaes0dgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e776ed28.mp4?token=ezrVXfOhQwobSQlobccycU7BFqR1tTFZkMUZUVPtH15yRQWjC9uoYaXmhFQAUIkljjqSYsh8rUaYsNivgHQcmvHO7ZOFh5HdV8SDQy3zXOXUf4aSKepSup4HhZkx-ColjP5DclcbeIREd0earbqazxqiyJuvK7ToPj4_1UmSlsxAw9JAB6h_XwFZzgHaFSIS5WS6xo_pipWCMGwiL5aZM20VOgHxu2YvVOe4ezIa1dGSdki7GP8dwCcGSXrhyI2x3On4xEZJTYb5AphtBm5sgZYsjvec5JEYP1amzOe_sT8FfpRjODKjOKovSuDvdFtugmGdg3vpUicX8hTaes0dgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب منازل مردم لبنان این‌بار در شهرک بنی‌‌حیان
🔹
ارتش رژیم صهیونیستی در تداوم سیاست تخریب خود، چندین خانهٔ مسکونی را در شهرک بنی‌‌حیان واقع در جنوب لبنان با خاک یکسان کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/458411" target="_blank">📅 22:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458406">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OX99yWhPAi8gbctPmLhKAVE4qovY4tXUzENEH_yer3p8MlNDkbTazsRlYoNTIg85o61v7sMFshFjooceM3LlW7ILcOOUsC4nqT5EsVjjeNqTIU6_iuTxl5u_149sZ_GvJH6FQs4wawsT_egpAsNvdsMGBGhpQEug-r9ioEQPGwoyreRRcHGz3vAWRtOdA8GLAO2cmBKUi7Jz3yGX0rQmXSCsV2cw1imaqqSkORA_ri-iSPpURlEXrqVH0fTcB0GfwM5IywJRjio-i_1118caxeSDH7Rwr1sseVMHuMyO2-HdRMcyko0WY78IdUQImvi16jet-JSsP__kgYmjCb-ung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEpR0pYyN2dSTLRvcaFYeBLFIj7XGS4qe8jtXh4W1ZSaqtCzDGuuv036aGg9K1TOEWl2-pwNHE3GNztQt72I-CLbRTf16pNnDBckMXWJ_utJ05984AcNfkRUijYeNl9CDiUW47neSdKal7NMK1w91-EhMe7vQa15VjhymWm6eD-pjPNpDZwygGlzmJbp6FQsW7JGmYoPItLxYSI8TVVEyrrHHMECTHcd55iiyzOf08KMIY9rxUebKsMnXeZeFlLatwbQjhJn_e42LSeecsp8YJZ--2YumaFUINKT3YYtDh66Y2R-Z-dDozDxPUBwUogN4NKDW2mVoqg0X_vavs4ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqTOk3pLlCxI-NoKxa3oKxwWfXAxgkUm0sGfF9xbyasm37W1YzrVliVEgM34LTU54tLY5aGY4MVjpmwpKVbqdx_d7QWmPWxvdI6LMBBcyc5XhIN1kV6hGq820e2mZorDjrdh5B49pRo6YJGLSg08KG0c4oX01tT8JlM5hQ6MTZNAoyyCJZ4uT12JSPLbyFFclgloH0kPr04fsmUPPewbsVw0YC30oMM7LBMKwBqE3uH4pz0GKig0gIvUN4sBoWtqTfnLoBOUTNMViW3Y86fU3isIBMLjt-L48rE8fQM6YctyZGZJi6Tf3RpS1Stl4_c71jzTmJKqwdAOZ_S_CcbNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CeVESB7SOQCs-uT387DsoY9-W7DviqVoDkNGvFi5oKbDUpMXfuKIE-9yiW6QCipumraX463SYCnElkBzPnOxGy5ApaKnStdoZPppxYORLrGbiX0pLR4T7Fct9n5IyO7A-62d1qHaUYGWAlAHLblppqg05ksJYcQXSUPXdYoM55ZxAB0Q3wY29nh8Wm2wx9-gIdqQdgX4tEVgYh424viUuBsSLlPTF16yDL6-keWQIlqF_fAPFO16ExQlj3Rf8lj2LnjSTnosJee3Xrnpvg8Gf3C5OqZHb85O1jQR-Ymv62F6oUSxJe6lPCfxysgkMdGCvw0JAlZbjtICPgG7QRWONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDdC0QTccbGmZQ1bNSenaZuIRdPEu2R_fKFtXIUHAFtBKUJeSqKGlolY5Z4DCbde3cRlg_n_UHlwKTqBZkk3E02H92mdR519qYGNRVboqGRlZzkDBmVGCmAe_AQ3rib2Tnp8ssUdiBHBLaTEvH365F2J84XtjhyCTu7-2zg0wSJUCjcbNAsXWZy3Yh6zVA_lSh8L7aHQmDVQ7zCBYX9EFRC4ccsSeJe_EjLogWvuug7qbKeUpremKS8afSRyg773lPN7RdCbeDaK6cJU6nv1LpMOLOO0Fm6rHcP7P0ySf7eYD6liKYKfihfm2Fn6nBtMNU1NrAXFmlkheZhMkwDlsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
تصاویر دست‌نوشتۀ شاعر معاصر زنده‌یاد مهدی اخوان ثالث که سال ۱۳۴۱ در دفتر یادداشت رهبر شهید انقلاب اسلامی نوشته است
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/458406" target="_blank">📅 22:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c667f381.mp4?token=wB7hb9NiwTeKNCfDydK1BJHwYfjgOQB4z2hwuQ-KK4gMeLjhtfdJzDvYYHMiWxMZFeOeKhXR1mVG2-OKXzMcv-P5dqGR0q_QKX3wRO7c278jLZFRHjeTu7D38PZUDmvQH3NpIJjPnUDjyF4KAXBscMVhRSVu7bAsO0yIbvjG9EEQMTSBbO0m0R884MKgrag4lamL7DJ4ggt5vPAtgOxZRRo0qVHRfV7kD1Xh-HWa4psXTFyDfwFpvMMkOSQ_gfZGK-CwTxDQAAWQ-p_Yj2BmDh_7syveE5KfJHmgiKICDF06oFSU8-qXcowLq3rWyOi54wXOUX8efYSFdDrBqMx8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c667f381.mp4?token=wB7hb9NiwTeKNCfDydK1BJHwYfjgOQB4z2hwuQ-KK4gMeLjhtfdJzDvYYHMiWxMZFeOeKhXR1mVG2-OKXzMcv-P5dqGR0q_QKX3wRO7c278jLZFRHjeTu7D38PZUDmvQH3NpIJjPnUDjyF4KAXBscMVhRSVu7bAsO0yIbvjG9EEQMTSBbO0m0R884MKgrag4lamL7DJ4ggt5vPAtgOxZRRo0qVHRfV7kD1Xh-HWa4psXTFyDfwFpvMMkOSQ_gfZGK-CwTxDQAAWQ-p_Yj2BmDh_7syveE5KfJHmgiKICDF06oFSU8-qXcowLq3rWyOi54wXOUX8efYSFdDrBqMx8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ حضور مردم در شب ۱۷۹ هنوز روشن است
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/458405" target="_blank">📅 22:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijf3Z7JLBu9QoZUP2rIH6PpZmemH5YnoIMZ2TQ6tyFOxT6As5wTnf9G1pZExaflsudSz3cK0frGhbBt3TWPwsd8O2vH-iOYPNGP7KfiVq_fr4rN1fPoIKSpuwqwrHd1WvhA5HMaOn0mGmkndcrrK--0PCG38p3FZmrbZleY19AC7U1iSvzImnuGRfCbr_RG6D-dfIiTaNwBCmCo1XwJE0wOcB5vAnPswIsQRrgWr01kGRf2hce34CLDgQxKW592Vs5qTt8_vQBivRNzWWURVoIfHijLr-Ch0Xnbpi3gYPWSpGIBeO35aJbBdMAehNE5dY4s5H2lfFQc17AqzH4BfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فولاد شادگان تا مدرسه نابینایان شیراز؛ روایت ۱۴ گام بلند «امید امروز» در گوشه‌وکنار ایران
🔸
۴ شهریور ۱۴۰۵ را در تقویم امیدهای ملی ثبت کنید؛ روزی که خبرهای خوش از ۹ استان کشور، یکصدا فریاد زدند که چرخ تولید، آبادانی و عدالت، حتی در سخت‌ترین روزهای تحریم، از حرکت بازنمانده است. از افزایش ۱۸۵ درصدی صادرات خراسان شمالی تا واریز ۲ میلیارد تومانی به حساب بیماران خاص از جیب نفت مصادره‌شده آمریکا؛ این، تنها گوشه‌ای از ثمره شب‌بیداری مدیرانی است که شکر نعمت خدمت را با عمل ادا کردند.
گاز گرم صنعت در خراسان‌رضوی
🔸
گازرسانی به بیش از ۴۲۰۰ واحد صنعتی در دولت چهاردهم، یعنی نفس گرم تولید در کارخانه‌جات مشهد، نیشابور و سبزوار. این عدد بزرگ، نوید اشتغال پایدار و رونق بی‌وقفه کارخانه‌ها را می‌دهد.
جاده‌های همدان، محکم‌تر از قبل
🔸
با حضور وزیر راه‌وشهرسازی، ۳۵ پروژه راهداری در همدان افتتاح شد. این یعنی ۳۵ گام برای کاهش تصادفات، ۳۵ پل امید برای روستاهای دورافتاده و ۳۵ مسیر برای رشد اقتصادی این خطه.
آبادانی «پشتکوه» در خاش
🔸
۱۹ طرح عمرانی روستایی در بخش پشتکوه شهرستان خاش به بهره‌برداری رسید. از آبرسانی تا مدرسه‌سازی؛ این خبر امید برای مردمانی که کویر را به باغ تبدیل می‌کنند.
۲ برابر شدن مشترکان فاضلاب در سیستان‌وبلوچستان
🔸
رشد ۲ برابری مشترکان شبکه فاضلاب شهری در سیستان‌وبلوچستان، یعنی گام بزرگی برای سلامتی عمومی و حفظ محیط‌زیست این استان پهناور. از زاهدان تا چابهار، لوله‌کشی زیرزمینی، نوید زندگی پاک‌تر را می‌دهد.
رکوردشکنی فولاد خوزستان با «شادگان»
🔸
افتتاح فولادسازی شادگان، ظرفیت فولاد خوزستان را به ۵ میلیون تن رساند. این یعنی ۵ میلیون تن استقلال صنعتی، ۵ میلیون تن اشتغال غیرمستقیم و ۵ میلیون تن قدرت صادراتی برای ایران بزرگ.
جو مطلوب کشاورزی
🔸
افزایش تولید ۱.۵ میلیون تنی جو در کشور، یعنی نان دام‌داران تأمین‌تر و سفره ملت محکم‌تر. این حاصل بذور اصلاح‌شده و مدیریت هوشمندانه آب‌های کشاورزی است.
سرمایهٔ خارجی به کرمانشاه آمد
🔸
جذب ۸ میلیون دلار سرمایه‌گذاری خارجی در یک سال در استان کرمانشاه، یعنی اعتماد جهانی به ظرفیت‌های مرزی ایران. این پول تازه، جان تازه‌ای به واحدهای تولیدی این خطه خواهد داد.
مولدسازی اموال راکد در مرکزی
🔸
۱۳۴ ملک مازاد دولتی در استان مرکزی وارد چرخه مولدسازی شدند. این یعنی زمین‌های بی‌استفاده به کارگاه‌های تولیدی و مسکن جوانان تبدیل می‌شوند؛ یعنی گردش چرخ اقتصاد با دارایی‌های خفته.
صادرات رکوردی خراسان‌شمالی
🔸
رشد وزنی ۱۷۵ درصدی و ارزشی ۱۸۵ درصدی صادرات این استان در مقایسه با پارسال، یعنی بجنورد در مسیر قطب صادراتی غیرنفتی. این عددها، نشان از همت بازرگانانی دارد که از تحریم، تونل عبور ساخته‌اند.
امیرکبیر، مرکز تبادل علم جهان اسلام
🔸
افتتاح دفتر تبادل علم‌وفناوری جهان اسلام در دانشگاه امیرکبیر، یعنی حلقه وصل دانشمندان ایرانی با همتایان مسلمان از قاهره تا استانبول. این دفتر، پنجره‌ای رو به آینده‌ای است که مرزهای دانش را برمی‌چیند.
واریز ۲ میلیارد تومانی به حساب بیماران «پروانه‌ای»
🔸
از محل فروش محموله نفت مصادره‌شده آمریکایی، ۲ میلیارد تومان به حساب هر یک از بیماران پروانه‌ای (بیماران خاص تحت پوشش) واریز شد. این یعنی لبخند بر لب‌های خانواده‌ای که هزینه‌های درمان، دغدغه روزانه‌شان بود. نظام اسلامی، جبران دشمنی دشمن را به خدمت محرومان گره زده است.
هلال‌احمر در میدان خدمت
🔸
از هفتهٔ دولت پارسال تا امسال، بیش از یک میلیون و ۸۰۰ هزار نفر از خدمات داوطلبانه هلال‌احمر بهره‌مند شده‌اند. از کوه‌پیمای مفقودشده تا زلزله‌زده دوردست؛ خیریه‌ای که همیشه در بالین سختی‌ها حاضر است.
۸.۵ همت برای هنرمندان صنایع‌دستی
🔸
پرداخت ۸.۵ هزار میلیارد تومانی تسهیلات به فعالان صنایع‌دستی در یک سال، یعنی سفالگر لالجین، منبت‌کار اصفهان و گلیم‌باف کردستان، صاحب چرخ کار پویاتری شدند. هنری که نه فقط در ویترین‌ها، که در تولید ملی می‌درخشد.
مدرسه‌ای برای فرشتگان ناشنوا و نابینا در شیراز
🔸
بهره‌برداری از آموزشگاه ۱۲ کلاسه دانش‌آموزان با نیازهای ویژه (ناشنوایان و نابینایان) در شیراز، یعنی عدالت آموزشی در معنای واقعی. این مدرسه، پلکان ترقی کودکانی است که با اراده‌ای بیشتر از بسیاری از ما، مسیر علم را می‌پیمایند.
کلام پایانی امید
🔹
به قول مولانا: «شکر نعمت، نعمتت افزون کند / کفر نعمت از کفت بیرون کند». این خبرهای خوب، نشان می‌دهد که در میان هجمه‌های خبری سیاه، صدها دست خستگی‌ناپذیر در گوشه‌وکنار این سرزمین، مشغول روشن‌کردن چراغ‌های امید هستند.
🔹
ما در خبرگزاری فارس، قدرِ این نعمت‌ها را می‌دانیم و به سهمِ خود، این قابِ درخشان را به شما تقدیم می‌کنیم.
🔹
شما هم اگر خبرِ خوبی دارید، برای ما ارسال کنید تا منتشر کنیم. ایرانِ خوب، خبرِخوب می‌خواهد.
@Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/458404" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458403">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a762289db.mp4?token=rx7Vg_g3Z7kiozh2zTTTPBN75TnY09F17s8sIir5EydEP1gWeVfOhvXvohv2h8g8lxlxPPE2R0m7-FWMYHDwyGS-6n2xGN6Ah1ncCwT_gBx3cu1gOpmN1I51Zv5K0yIdspHB5jVWMpK_q9FbC1JHLB0tVCCZMaoNlMjwGJAy05bUMXbu-XpunY6b8SpZNluHcJwqawMuGUcOvoBGoAet290KoBBCew0o8jpuP4gTAkaBri-HWe9nQgusSJ9_pkP3w6yi_TaixrqVmS09DN5Sk3mClEgfXaEuPnOdlPqHGwEYUm-5co4b2DngHgX1-oKjKReXxj6Ry_rh759WkKsV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a762289db.mp4?token=rx7Vg_g3Z7kiozh2zTTTPBN75TnY09F17s8sIir5EydEP1gWeVfOhvXvohv2h8g8lxlxPPE2R0m7-FWMYHDwyGS-6n2xGN6Ah1ncCwT_gBx3cu1gOpmN1I51Zv5K0yIdspHB5jVWMpK_q9FbC1JHLB0tVCCZMaoNlMjwGJAy05bUMXbu-XpunY6b8SpZNluHcJwqawMuGUcOvoBGoAet290KoBBCew0o8jpuP4gTAkaBri-HWe9nQgusSJ9_pkP3w6yi_TaixrqVmS09DN5Sk3mClEgfXaEuPnOdlPqHGwEYUm-5co4b2DngHgX1-oKjKReXxj6Ry_rh759WkKsV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک پلیس به سارقان موتوری در رباط‌کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/458403" target="_blank">📅 21:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458402">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53f1e4c1e.mp4?token=tj6mtAj5690ObNrHeQbCUe27SMfg1U8vqMYQfO1tXqDRrn-ezcWd_T3DVLr8y-ZfjfFufUaDe-9pSzZ7TEvb6pX0dEM10dt17lIrYZZETEjrNKuJ189ODQdgm3kM8H1ekw2ADpDqdy8Kws-azBN85Uj974S6aqtVfDPSohjkf6yync7_RWOgJTTG9D_j1RnS02yDW5H-Y13Gh36xyLNKSgm1ICV0aR_VRjemqcptLLbSJdreNHPyA_gKQ5UcLd-d9x_FClind4H5uCycFV2Aixx6IxmlQ8ogzmZQ22iwM2PSpZbFuprLi9F7EdDkxm-0uVI6SplEvcLcrOuOqgeSiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53f1e4c1e.mp4?token=tj6mtAj5690ObNrHeQbCUe27SMfg1U8vqMYQfO1tXqDRrn-ezcWd_T3DVLr8y-ZfjfFufUaDe-9pSzZ7TEvb6pX0dEM10dt17lIrYZZETEjrNKuJ189ODQdgm3kM8H1ekw2ADpDqdy8Kws-azBN85Uj974S6aqtVfDPSohjkf6yync7_RWOgJTTG9D_j1RnS02yDW5H-Y13Gh36xyLNKSgm1ICV0aR_VRjemqcptLLbSJdreNHPyA_gKQ5UcLd-d9x_FClind4H5uCycFV2Aixx6IxmlQ8ogzmZQ22iwM2PSpZbFuprLi9F7EdDkxm-0uVI6SplEvcLcrOuOqgeSiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان انرژی هسته‌ای: در زمینۀ گداخت هسته‌ای وارد فرایند قابلیت‌سازی شده‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/458402" target="_blank">📅 21:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458401">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1JnJMpKHpSaEWSqKrh5VkW7WcaToYSmccPFdlBbkVIe8ea-cA4AZtanf5y-9Q7EsYIz4ym_avN6iOp-yb-KRdQ416CaqLvWXOQMt6KegKkg3B_rTFbYGWmroACigkFhW7a5fQFtX-4UJa7vek2q4-ySVN2mneHWu6f-EABvnY6nmNuWEx9AtYyM8Z4bWKeF7Adb6Yt7x_jlivBYargwj7TJk0QYFXdnm5UA5WB17MtukzXeW1tBV62DuQGFr-OBe3NIO9xnXgT7_eIAMpHpHZP-_n4GD8b7DvW7BX5DplciInwh3XhCPZE6Puig_qLeoXdLSflD6CaPF7Emvik4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: رابطهٔ راهبردی ایران و چین به اجازۀ هیچکس نیازی ندارد
🔹
ما از موضع اصولی چین در رد تحریم‌های غیرقانونی علیه ایران استقبال می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/458401" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4xryspUEpPOzg_WiGV9XHRs_YaNFXUBJIek_Ka6nWN9GB6gt_2fz04TaxpCU74xp2udP7BTSVimAVbYDY8oYje466DkctQA7qjeayumrnP297G-QbvcVPir2dpJd9OjYPI0_uvz5pb4R6xN0vS0NpROsQXV47uXMr7lWbADDS-Y6_M5IMK2Sj_ar6Uft6ca7qSlwsZTF7pgq9RXURt6HTkrhlNL9TWo-cMJD3vLmZLOaBvYE5FsO2DpwDfRVZfvcj3QAzcAQxq9lcI9_8blqlrbE-Uh2THT0w1mEihUWJn6v8avgN9fEurvJz03ElEMC9Vpvtv6C-JPa_ddOJb6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج بزرگ غلات در روسیه و فرصت طلایی برای ایران
🔹
بحران صادرات غلات روسیه درپی حملات متقابل اوکراین و روسیه به تأسیسات بندری دریای سیاه، صحنه‌ای نادر و متناقض را رقم زده است.
🔹
درحالی‌که قیمت جهانی گندم و ذرت به دلیل اختلال در عرضۀ این ۲ کشور به بالاترین سطح خود در ۳ سال اخیر رسیده، بازار داخلی روسیه با مازاد شدید غلات و افت بی‌سابقۀ قیمت مواجه شده است.
🔹
این شکاف، فرصتی غیرمنتظره برای ایران گشوده تا از طریق کریدور شمال‑جنوب، نیاز فوری خود به نهاده‌های کشاورزی را با هزینه‌ای به‌مراتب پایین‌تر تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/458399" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c442925a09.mp4?token=ZbcdUc6UhsRLmJA9HC7a7FwU2J9amEMjaWJcy5qI4XKZ2W_bax8JtN7w2TipeMk2FsxeqRvsCg7GzAkXB1xsUea9F8ktMcGhhYCX0cnkFNUDY7tG9ClLbGrJ6F0TySe5oTFIxy-NJbf3IGuOpd-puoU0SQsVCCnlSbOYZModq1bNYB0EklaVq-wJA4lRzCfnEgsQDYsV8cJHSMYxdkUNdzeKHQKw1KlyKQmKLLRMPRNwgILre6f5aIoaND8fYfzjQJYe3wbb_lZjMQyPfYH7xUL6n7qRFYfGwV8sUb_B59K9bkV2VBD3g2H4r39Qr5wLtv2s3QYnPufQyd1_XsTBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c442925a09.mp4?token=ZbcdUc6UhsRLmJA9HC7a7FwU2J9amEMjaWJcy5qI4XKZ2W_bax8JtN7w2TipeMk2FsxeqRvsCg7GzAkXB1xsUea9F8ktMcGhhYCX0cnkFNUDY7tG9ClLbGrJ6F0TySe5oTFIxy-NJbf3IGuOpd-puoU0SQsVCCnlSbOYZModq1bNYB0EklaVq-wJA4lRzCfnEgsQDYsV8cJHSMYxdkUNdzeKHQKw1KlyKQmKLLRMPRNwgILre6f5aIoaND8fYfzjQJYe3wbb_lZjMQyPfYH7xUL6n7qRFYfGwV8sUb_B59K9bkV2VBD3g2H4r39Qr5wLtv2s3QYnPufQyd1_XsTBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از ۴ دستاورد صلح‌‌آمیز هسته‌ای
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/458398" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a4a84f53.mp4?token=q4DOyludtbU7L4N8I3VOO7H68J3FYiLddUE9DMrXR1-Eye4-b45HOlTuwk-3MDQksPhOyJmIG0W6kTKG8P_jcZJZcEI96glWwlnzLeH48aLmxZu8ve_BWiSVuGBZejRFH1cecGwD9GhHAH0PKQdvd0UsBjGFmHAk5sv0ExgyXyd1tCe1b-tqbOmPQwpVUmeyE4NA_iHuw7_zXstt0eSyWuykVVrgrFBtUQVeV9mkYIWtMmjSyzTRRfV2BjPbv5Xkf1PMYK1WSpqyexecHDsf27FOBqa_U9dx3M6KwpNmjrYK-gF_wIJJs6L6EK_Pq1qrU3h5oaE7s1y_XR-qB-QFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a4a84f53.mp4?token=q4DOyludtbU7L4N8I3VOO7H68J3FYiLddUE9DMrXR1-Eye4-b45HOlTuwk-3MDQksPhOyJmIG0W6kTKG8P_jcZJZcEI96glWwlnzLeH48aLmxZu8ve_BWiSVuGBZejRFH1cecGwD9GhHAH0PKQdvd0UsBjGFmHAk5sv0ExgyXyd1tCe1b-tqbOmPQwpVUmeyE4NA_iHuw7_zXstt0eSyWuykVVrgrFBtUQVeV9mkYIWtMmjSyzTRRfV2BjPbv5Xkf1PMYK1WSpqyexecHDsf27FOBqa_U9dx3M6KwpNmjrYK-gF_wIJJs6L6EK_Pq1qrU3h5oaE7s1y_XR-qB-QFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فن گلادیاتور ایرانی اتحادیه جهانی را به وجد آورد
🔸
اتحادیه جهانی کشتی یکی از فنون تماشایی کامران قاسم‌پور را به عنوان تکنیک هفته معرفی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/458397" target="_blank">📅 21:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmyuw7yV12TYq7TXj46LKvIREYWVxynzBEZnBzUmqM5raBnr33e-wqQa8CD3GSvI5J6Z1w7yghEDXHVzHS0_uPLASmdMNbCKsBcvdxUGiSJVQLzIGOlKbFRtn5RzO0o_tZhjqrS7gdh1khdSp3qswJ6Qp8ZM5rARAfcMiEBesFjSYJhmvh9hDVbq1OHWvcgGG5yPW_i76BSP09gPbEE2PaU6uMWyvHz9nNqiGRvBSQbFP6qD6pbS-iZ-xPvjfsZiDt-PpsY_Oa58M3H5HXZNXfOsvtHlfFvvw0YfmYA0DBdZZ6-NXczKtTpNimz_rSdFCFGbiDBPlqYCH60qXg-XyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور: توزیع بنزین در کشور عادلانه نیست
🔹
قائم‌پناه: طبیعی است باید تغییراتی در نرخ حامل‌های انرژی انجام شود اما میزان و زمان آن را باید در گفت‌وگو با دست‌اندرکاران تعیین کرد.
🔹
توزیع بنزین در کشور عادلانه نیست؛ فردی که چندین خودرو دارد از یارانه استفاده می‌کند و افرادی هم که خودرو ندارند از این موضوع بهره نمی‌برند.
تداوم این مسیر غیرممکن است زیرا تولید بنزین کفایت نمی‌کند و با محاصرۀ دریایی آنمی‌توانیم بنزین وارد کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/458396" target="_blank">📅 21:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292d37aefa.mp4?token=HXKtC13iR9A995OXKx6XmQouL0oqfA8LstO7mN25xjFFrdmli2NAbkhyANdDfQ8_2eKC4PJeyEluMSM4C0t8orZd7J038xRMNc-hFJxQfHuESHWMul-XJE7ROLs0Bz_lbm3iOyD2KZjFzM6Zf-KcgAM7mWhhz9CS9HuknlC_-h84g7BPO1Mg-5EF5pURI1gJ3KR9n41ej2U90LZSfqMySFdIRaaeernSkegUvNa9kfTsEPtshaqFlS1lePYvoS8oYOJdS0Gnl2zM0-q8lJOMwT27GeL_FE2WJHD7mX8AUHEyqjPBarWj2xRA9W_NGCWajtyecDvWDdPRJt9wPtLPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292d37aefa.mp4?token=HXKtC13iR9A995OXKx6XmQouL0oqfA8LstO7mN25xjFFrdmli2NAbkhyANdDfQ8_2eKC4PJeyEluMSM4C0t8orZd7J038xRMNc-hFJxQfHuESHWMul-XJE7ROLs0Bz_lbm3iOyD2KZjFzM6Zf-KcgAM7mWhhz9CS9HuknlC_-h84g7BPO1Mg-5EF5pURI1gJ3KR9n41ej2U90LZSfqMySFdIRaaeernSkegUvNa9kfTsEPtshaqFlS1lePYvoS8oYOJdS0Gnl2zM0-q8lJOMwT27GeL_FE2WJHD7mX8AUHEyqjPBarWj2xRA9W_NGCWajtyecDvWDdPRJt9wPtLPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: مسکن حدود ۴ هزار نفر از ۵ هزار نخبۀ کشور را تامین کردیم
🔹
رهبر شهید سال گذشته از ما خواسته بود برای نخبگان مسکن تامین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/458395" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfOOrVcQO15uEOZVIVhbmtBAtS3XGS-fzNUaerY-VcBoByxJ2AM0W3Pz8Fw4J5a7KazBPqd3iMWKPiupbfAM2wBK6MSouleYxHf4BB2pnTeR99rWYOI9BZW7swdnWsjUtnrC_k4v9dYuOmS47KhX5TZPAvAP5VHfvzlxdMn70y-zDbr8kVYF6CTH5BmHs7TfvPgxZ7zmV1OyagVTI6uVzVVzm40IJEocSZi09OqyLK1HNVHiESSs-jnFf1CVUggsfsCJV_6hy4IZ_E7hSF_o1eIPdiPHny9txKMCi8FgQY-2zvx2ExRKIKc6p1sMpoOPhq-QtW1DpN8qZgpvnr-Fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: مذاکرات اوکراین به بن‌بست رسیده است
🔹
بلومبرگ به نقل از سه منبع آگاه نوشت که روسیه در حال آماده‌سازی برای تشدید حملات به اوکراین است، چرا که به این نتیجه رسیده است که مذاکرات برای دستیابی به توافق صلح به بن‌بست خورده است.
🔹
به گفتهٔ این افراد، روسیه در حال حاضر در حال بررسی تشدید حملات موشکی بالستیک به کی‌یف، پایتخت اوکراین، و همچنین اهداف زیرساختی در سایر شهرهای اوکراین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/458394" target="_blank">📅 21:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458393">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fc5615cd.mp4?token=tWwtaRqk2P4u0_Gmr4_Lh0R-Z4tc_5NX00Zkj54kJe03ULOQALCTo1OgGJd5hYQvKJO-8ECQ3zb0oksPrK1M3ZSa0G4sjJYfODiuPHl4qqrVIpkVukzpYLBr4NqbpOyHeiOjnDQPJJ2TelJPls13g8c7XFHz4-cKk1KmVQnRLxVBWQalVJbHZynKgJ-8sstrizd_aKiBkC6eyUWsT5dMncBM4TIXrvncaDzu9YEOK55jtvq4TyS0rYWWVFIyzhB9dI_46YATPZWV1jYD7-vwYW4uP27dq5RCXGyTSnPRNxQvc1Ez_72gFqtaAyHgePFeJzeL4RKrqNwK7bJQF37RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fc5615cd.mp4?token=tWwtaRqk2P4u0_Gmr4_Lh0R-Z4tc_5NX00Zkj54kJe03ULOQALCTo1OgGJd5hYQvKJO-8ECQ3zb0oksPrK1M3ZSa0G4sjJYfODiuPHl4qqrVIpkVukzpYLBr4NqbpOyHeiOjnDQPJJ2TelJPls13g8c7XFHz4-cKk1KmVQnRLxVBWQalVJbHZynKgJ-8sstrizd_aKiBkC6eyUWsT5dMncBM4TIXrvncaDzu9YEOK55jtvq4TyS0rYWWVFIyzhB9dI_46YATPZWV1jYD7-vwYW4uP27dq5RCXGyTSnPRNxQvc1Ez_72gFqtaAyHgePFeJzeL4RKrqNwK7bJQF37RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی رئیس‌جمهور: سکوی ملی هوش‌مصنوعی که توسط دشمن هدف قرار گرفت را در عرض یک‌ماه بازیابی کردیم  @Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/458393" target="_blank">📅 21:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0f86b5a4.mp4?token=px2q1EgNK2oegut7iH4kmc3PJ8BZhAToZrKuQ4Rh7Ttv-uhBEcU1O8pRb6DWGeCtMpinXnsDoGOaoXHy32JUhvcSd4xqbeuFB3M3wQhVq2LngOdAxFzXrBlY8th4_R9cDThkGMHjN6abfynnmYXjyhFI5SQZYg_K3qSU7cwQFYAaQ5pO62ZPZsolu401cIH0nP0-G_Na6eG35A8kKb72srUpP89j2fi0YZrUuA44Y7gnbyUVlj5L0ltFnU4g3WzZlF9WHdV2vYamkZXcHujAdrTO8oF9qJkaCYLxm7k7tK-09TQD4VJ5kD9q_JCbG8a6P2eeDaoIPLCV7neoLbtbKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0f86b5a4.mp4?token=px2q1EgNK2oegut7iH4kmc3PJ8BZhAToZrKuQ4Rh7Ttv-uhBEcU1O8pRb6DWGeCtMpinXnsDoGOaoXHy32JUhvcSd4xqbeuFB3M3wQhVq2LngOdAxFzXrBlY8th4_R9cDThkGMHjN6abfynnmYXjyhFI5SQZYg_K3qSU7cwQFYAaQ5pO62ZPZsolu401cIH0nP0-G_Na6eG35A8kKb72srUpP89j2fi0YZrUuA44Y7gnbyUVlj5L0ltFnU4g3WzZlF9WHdV2vYamkZXcHujAdrTO8oF9qJkaCYLxm7k7tK-09TQD4VJ5kD9q_JCbG8a6P2eeDaoIPLCV7neoLbtbKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا تحریم کرد؛ چین راه خودش را رفت
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/458392" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
مصرف بنزین خودروهای دولتی زیر ذره‌بین
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/458391" target="_blank">📅 21:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20b3dbec1.mp4?token=CN8VrOB_RXnt2MWb-JusLzCi_x1zz2ZG7RalpwH3hRA1mcWGihK4sy3Lnq2rz4eejQmSdglV4it-Y0cehswBjffWPP4-FBVZ4Sdz6DbmmM2wfTk3AINs-vx2uEXICH5e8kCKLBwrRj6I_x7ei9b9nDX2as5tjf4EnhkvwFJafAmHYMukNyHxxXe5EQ_pb6dqU9VuTHlAg3fBs_374U188GdH5lphrq5HK-Ajh08obbz4ZTs8-ub7TxNacaAlZKZOlsKYFiZEzy15BiqUlPOYT7MQ3dZavLZskIjGrLUJCCJWrvlyZHAg31AEiD6JMBGuSkZGMW9HWbs-jMvT-b4A5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20b3dbec1.mp4?token=CN8VrOB_RXnt2MWb-JusLzCi_x1zz2ZG7RalpwH3hRA1mcWGihK4sy3Lnq2rz4eejQmSdglV4it-Y0cehswBjffWPP4-FBVZ4Sdz6DbmmM2wfTk3AINs-vx2uEXICH5e8kCKLBwrRj6I_x7ei9b9nDX2as5tjf4EnhkvwFJafAmHYMukNyHxxXe5EQ_pb6dqU9VuTHlAg3fBs_374U188GdH5lphrq5HK-Ajh08obbz4ZTs8-ub7TxNacaAlZKZOlsKYFiZEzy15BiqUlPOYT7MQ3dZavLZskIjGrLUJCCJWrvlyZHAg31AEiD6JMBGuSkZGMW9HWbs-jMvT-b4A5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاور راهبردی رئیس مجلس: اگر از تنگۀ هرمز چند میلیون بشکه نفت عبور می‌کند، چرا آمریکایی‌ها همۀ دنیا را بسیج کرده‌اند تا از ایران بخواهند تنگه باز شود؟
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/458390" target="_blank">📅 21:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/306bb628a8.mp4?token=t0X6LyOLscEGfLr7S1VGONuQUo2eZ1aHmmy7nzT5luZMWBI0-1sC-4BdveO1-bAQ1DiNLf8ZWdYM2fCczKj2uQxQnmltijx1b0cfQxOihJYcm4nzr6_fCfihKQP68Zwm7dg2CDMEDIqxR3cn5pxSn_nhcmzvcKWg5702ExnJ3ZUgKdIr9_0O4xhCRJ026VV3LJZunrRT_V-FWf9lkyevQ6IleMJjEMZKWANNzyVlMRSFvwz395lY5S0YUgdBIiG55AJ-oWvgoQ-40ef873bfkFonM3RqapMk2TmdU6F66Dubq0IQhOwZhPjMDnypDdyX6nmTIdCThABjjTsoKk4BpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/306bb628a8.mp4?token=t0X6LyOLscEGfLr7S1VGONuQUo2eZ1aHmmy7nzT5luZMWBI0-1sC-4BdveO1-bAQ1DiNLf8ZWdYM2fCczKj2uQxQnmltijx1b0cfQxOihJYcm4nzr6_fCfihKQP68Zwm7dg2CDMEDIqxR3cn5pxSn_nhcmzvcKWg5702ExnJ3ZUgKdIr9_0O4xhCRJ026VV3LJZunrRT_V-FWf9lkyevQ6IleMJjEMZKWANNzyVlMRSFvwz395lY5S0YUgdBIiG55AJ-oWvgoQ-40ef873bfkFonM3RqapMk2TmdU6F66Dubq0IQhOwZhPjMDnypDdyX6nmTIdCThABjjTsoKk4BpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی دستاوردهای دفاعی از نمایشگاه به میدان عمل می‌رسند
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/458389" target="_blank">📅 21:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7f0a4a3b.mp4?token=RMrBmxasHAZ8vlr9xRtZqPAWQ7C4DN6pS8ObL4gcxepXZyA0nQZmWmQcZeq-WMi-V42L6EQVS1dT6EFWPlL3rl92lHufi1DEpk-PEq3QTa0VsXeZHjdthk_wK3Tv2okvJMp25JxL6MIhwAyNn4_rFdUb6Ym6tEGeFazbtplwyqiNRd1jD8X8WKgYm5f_Mwl51xpfdtJs1g2z-LEtYB-2qMkDT-t-BlLxC8w-qEnp7g3WckCMdF-1Hnrfxhk4uqyWcik6NFpfF89o8fg8NsH60Bh_2nAdEvDPz-b5FQZoOYyTdR79gsHrFq3XEmqYZpL9VmhYQ75yh9t8PmJv-aOpj576rE59N8QkvUu5Gw2uYnAm4wDGWcaVoUXhxJN8Azp4U3JzRu7cimigC7ULeTv3F8D05LY4NYRMC92RP5mqCUDTjuQT7gA1g-SLHWMymNMtG9uor2Z05M9YSEyCpVpQUOrfdFtq3S8uMugXwPJfeNHGPkKNyViG4x3vys2EYoMBrCm8fKo30Qx3GwGo658Q59541hzQSwJGcsseb_WJs1MibQhkHi3oTLPqlFn92ZoBkM1X7jkKjuUihaskepgQ6_UC09ETPfHo344xB_yvojPuVccHKHQGKnFnUOtY_hhFnFBRjWckoiRQm_lDx1_xOycBBHXAgsenqKg9F9TGB9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7f0a4a3b.mp4?token=RMrBmxasHAZ8vlr9xRtZqPAWQ7C4DN6pS8ObL4gcxepXZyA0nQZmWmQcZeq-WMi-V42L6EQVS1dT6EFWPlL3rl92lHufi1DEpk-PEq3QTa0VsXeZHjdthk_wK3Tv2okvJMp25JxL6MIhwAyNn4_rFdUb6Ym6tEGeFazbtplwyqiNRd1jD8X8WKgYm5f_Mwl51xpfdtJs1g2z-LEtYB-2qMkDT-t-BlLxC8w-qEnp7g3WckCMdF-1Hnrfxhk4uqyWcik6NFpfF89o8fg8NsH60Bh_2nAdEvDPz-b5FQZoOYyTdR79gsHrFq3XEmqYZpL9VmhYQ75yh9t8PmJv-aOpj576rE59N8QkvUu5Gw2uYnAm4wDGWcaVoUXhxJN8Azp4U3JzRu7cimigC7ULeTv3F8D05LY4NYRMC92RP5mqCUDTjuQT7gA1g-SLHWMymNMtG9uor2Z05M9YSEyCpVpQUOrfdFtq3S8uMugXwPJfeNHGPkKNyViG4x3vys2EYoMBrCm8fKo30Qx3GwGo658Q59541hzQSwJGcsseb_WJs1MibQhkHi3oTLPqlFn92ZoBkM1X7jkKjuUihaskepgQ6_UC09ETPfHo344xB_yvojPuVccHKHQGKnFnUOtY_hhFnFBRjWckoiRQm_lDx1_xOycBBHXAgsenqKg9F9TGB9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم در تجمعات شبانه: دشمن در جنگ اقتصادی هم شکست می‌خورد
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/458388" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733998fcbb.mp4?token=q6-XcUfowyYaZawgAtW4h-XfsWiqg7iF6Zv-DaWktD_5g9mGktQnL4-bWvi0qSoWZJEFuiSctRrKaTXAg74qPVRZ2tqyxhrCnrtQ2CYQc-3bbV6Hh1aac5jobf2jQmgHYlOlPwmgKOPHWmWGEYJ76CynGgvohDmhomt-RuP4gn5ZBIbrG8GDAOWL7XlixhlRH36ysC_svdTwXaOGyADRe0dU3pogbfWJqekD-P3tCigHP3jViSxz1zQp3ceMSAV2CNTidjwcWny0YICcViQMWBEWGMrXCL33ASzvaL0xUVQsQtXqkeQbieDlLug3bRnw0tYFReZTlKNCFPkTIyxopA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733998fcbb.mp4?token=q6-XcUfowyYaZawgAtW4h-XfsWiqg7iF6Zv-DaWktD_5g9mGktQnL4-bWvi0qSoWZJEFuiSctRrKaTXAg74qPVRZ2tqyxhrCnrtQ2CYQc-3bbV6Hh1aac5jobf2jQmgHYlOlPwmgKOPHWmWGEYJ76CynGgvohDmhomt-RuP4gn5ZBIbrG8GDAOWL7XlixhlRH36ysC_svdTwXaOGyADRe0dU3pogbfWJqekD-P3tCigHP3jViSxz1zQp3ceMSAV2CNTidjwcWny0YICcViQMWBEWGMrXCL33ASzvaL0xUVQsQtXqkeQbieDlLug3bRnw0tYFReZTlKNCFPkTIyxopA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس حوزۀ زنان: خانم‌ها باید بیشتر در سطوح تصمیم‌گیری نظام حضور داشته باشند
🔹
بعضی مسائل جامعه مربوط به زنان است که در این مسائل خانم‌ها بهتر می‌توانند مشکلات را درک کرده و تصمیم‌گیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/458387" target="_blank">📅 20:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7ner870cgzTzlqPtTjrZVjGSMpUYObKe0bcET93x1nAeDw80bAvlsM3aXyDTMSXz8rMAFfhVtZMOMfBY4EpmpeaHzfymmc7x0lI781pYRp54F31bd1qVMYE7lqNEcJSCojTZYX8FeGnjdGUDlRY_vwKcS7rJpRlSiROSV-kGIv1BqzMjWfSZaf835KFGbKHHiF-WhtSqcobAKaJGYu7viBPxH_ANCabIFplaaRMh0Kudky56DFn1_GDywnmZkw_OHK_x8AmZONth81dNEV4ukL33C47mPd4g1yINz54ye95hokHqwnzWTOdcC65Fa1B9Q5Jz6b1MIu8Hl0oB3i8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: زندگی و شخصیت بی‌نظیر پیامبر اکرم(ص) برای همه‌ی دوران تاریخ اسلام یک درس و الگوی همیشگی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/458386" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBnc-JC3yo5dQ6qxfIwSr77La3d8iL-PHyYjzUscKLHTcRUZxYGsCztib5JphQyisRf_O2SuSPkD3wsOFjBVqwqCRaaUBspLfjRjESZijd4Qxm5xaRGuV31vmcD1VdIbrywHYYUXoVBKM9c9t0z7aiXeet1Df0HGNiGpUMELzz-HibwiGcwq0PDU_4CS09TUc-hj0h72MO1XMWbv6tLrUhr_VAFgg0E317EA_-BJU6aEOzK_bkK0nDX0M6KGIhetFiWbHr4UnTvf201Tkn7xMavhYttV6GaZfEIW5rkAwRVAFRY05SYN2safDkcYZxRZKoSw35uK2sbqw_-UtW7CZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آمریکا برای اقدامات غیرانسانی در جنگ اقتصادی علیه ایران پاسخگو خواهد شد
🔹
وزیر خارجه در نامه به دبیرکل سازمان ملل: جمهوری اسلامی ایران حق خود را برای پیگیری تمامی راه‌های موجود به‌منظور تحقق پاسخگویی، جبران خسارت و احقاق حق، محفوظ داشته و حق دارد متخلفان را در قبال پیامدهای این اقدامات غیرانسانی و غیرقانونی پاسخگو نماید.
🔹
فعل متخلفانه بین‌المللی ایالات متحده در اجرای کارزار تروریسم اقتصادی از طریق اقدامات قهرآمیز یکجانبه، واجد مسئولیت بین‌المللی آن کشور، به شمول تعهد به جبران کامل تمامی خسارات واردشده، اعم از مادی و معنوی، از جمله اعاده وضع سابق، پرداخت غرامت و جلب رضایت، مطابق الزامات حقوق بین‌الملل می باشد.
🔹
آمریکا مسئولیت کامل بین‌المللی و در صورت احراز عناصر قانونی مربوطه، مسئولیت کیفری فردی در قبال تمامی پیامدهای این اقدامات مجرمانه و غیرقانونی و خسارات واردشده به مردم ایران در نتیجه این اقدام تروریسم دولتی را بر عهده دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/458385" target="_blank">📅 20:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dfd8818c.mp4?token=rM0kdKVA3U0gvFucNYiFjOJI4Os1KLRTN16cUakB-xksy443zLfai-E9Cv9k08XZRe9ipJ9J_7ax8wOJhlGngMn9vxSRcWXUwK6kNUhwezqpEi6YEjjpHZizvdAOihmdUqfKHc48uVft917v2Ai_HQ9jjgi0zpHOLR6Ax-YY8aD6MrsqsJAOMwPBN8-fpyrQ9nImbvbsPMXPY3H0RgD5mQ1j_VVlKQ77nigsrJY5n1rqzKDAaRb6YvSJBpw5U3Y7D0Ncic6H3J62ShsVej5CBoVeDQ4M6a_reNfNN2e4nsbpwau1zE_l3vxzagOiRr9Dmx02HfQptj0DU0d46OgPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dfd8818c.mp4?token=rM0kdKVA3U0gvFucNYiFjOJI4Os1KLRTN16cUakB-xksy443zLfai-E9Cv9k08XZRe9ipJ9J_7ax8wOJhlGngMn9vxSRcWXUwK6kNUhwezqpEi6YEjjpHZizvdAOihmdUqfKHc48uVft917v2Ai_HQ9jjgi0zpHOLR6Ax-YY8aD6MrsqsJAOMwPBN8-fpyrQ9nImbvbsPMXPY3H0RgD5mQ1j_VVlKQ77nigsrJY5n1rqzKDAaRb6YvSJBpw5U3Y7D0Ncic6H3J62ShsVej5CBoVeDQ4M6a_reNfNN2e4nsbpwau1zE_l3vxzagOiRr9Dmx02HfQptj0DU0d46OgPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک پلیس به سارقان موتوری در رباط‌کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/458384" target="_blank">📅 20:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075b1f1ed3.mp4?token=Mpte2kCAXcKlfoPKtvH0EKVeRg4W3ei7svV91uHLbx58pZk39cVU0cdiOyTKh-k48btPW_gJTF1NgerHxuTOaAJIKeWwvfsey1n6_gi9oOn0R1tHS1X7wDr3OXpFT4Rn5oepNEayn32n-KwDzPCwyPe1b121JxW3mq0SFuSOk2xBGsTAiGYSwe7hABIHHBF8NEXoKeAgLOabtLzatL1aI2bm8qACW7smKPxUIW0vCo6fc5MxZtpbvD_tU-0u9PcEuE5wdHjcld3O8-gf9kOodC0rH-YMwx89BV61iCe4YR3FFugMP8ICpns--4ebe36H3-YGAOrHPl-WeLcCV5Lt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075b1f1ed3.mp4?token=Mpte2kCAXcKlfoPKtvH0EKVeRg4W3ei7svV91uHLbx58pZk39cVU0cdiOyTKh-k48btPW_gJTF1NgerHxuTOaAJIKeWwvfsey1n6_gi9oOn0R1tHS1X7wDr3OXpFT4Rn5oepNEayn32n-KwDzPCwyPe1b121JxW3mq0SFuSOk2xBGsTAiGYSwe7hABIHHBF8NEXoKeAgLOabtLzatL1aI2bm8qACW7smKPxUIW0vCo6fc5MxZtpbvD_tU-0u9PcEuE5wdHjcld3O8-gf9kOodC0rH-YMwx89BV61iCe4YR3FFugMP8ICpns--4ebe36H3-YGAOrHPl-WeLcCV5Lt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوکر لژیونر ایرانی در لیگ مالزی
⚽️
شهاب زاهدی مهاجم ایرانی جوهور مالزی، امروز موفق به ثبت ۴ گل در برتری ۹ بر ۰ تیمش شد.
🔸
زاهدی گفته قصد دارد باتوجه به حضور تیمش در لیگ نخبگان آسیا، با تثبیت عملکرد خود زمینه را برای بازگشت به تیم ملی فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/458383" target="_blank">📅 20:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb3kx5umcwaKPPOmhPNKaQhvvcQEldxjuxhpcc_6tknd3Bm_YdF4GBlcBpv8lEAHFmweKguR4my-iGYnPEdrqNpSL4H9UBgQTojSVar_4aYvFFdqD5X5_GQqJnxlHD5Yo1sKlFRIf7abHhUdsgRvfPVGoH7twSblU2jjJ1CaoMTAu8j7ldRbqeWSfFBnhvywuT77TwgWRxgaCtX5uU6Q5DFghLu4ibXnYBhx-WsmA07zqe-8Ra18MfeO-qMQTdfi7_jZxaQu1j_V_AWtjbLtfBpMKkCj4dBLUOowGNr3I7fjQBB5xLbyORawwIFu9fM0jPrxEhIbtCBTTBOk_n_0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی: تورم مردادماه نسبت به تیرماه یک‌دهم درصد افزایش داشته و به ۳‌.۷ درصد رسیده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/458382" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458375">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aC9j99i0W5zxlKDdiL15r4XBvvdbRXfJq67Gel-EBCA49uFuuyYkWA82wbg1AVRp77KLgYfqRCJXwnYPtikYiZ02PN7XyQlLYYc-a-7tcoALbpJFGGuF1vKLON1DVBB7_tMb8P_kmjJ4Vbr7ELVtPXPlkX0ZhsrcYQWXkKLAKy96YqaZRhWc5GRDQS4OIu84m1YCCV_qUmQdhPb7zpNJ8qjc5yXRuviO6fgeKD2tI237MbeWppKGCMNnj9kaHbXRoUdPSeXyS0Z5K3CPT02NIqpCbVxYnfXyy5S0t9fS1aphm4cCR3X38oofBXNNuM0oPIBPxyKbdqeYPL-stqxGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGgroDgIfusKSHHyjTrPtMRDyM8XecJnApZBOxAoz787Kr8W0M7tjCpXGu99e_ZXtL8tWnk_2ZTK2lHSVWgxVfez1VAfYken5Ycf_MG59TfqEG7abJtu4HvY8vYHbrrO4xvhpAH0K6sK-ect7KZWbs3SUdTI5Itj9-G5Z2Mo6QjWD822pwlrk2r25meBAYy3mdD9F_cKJENt1sxjXyTS9ejVauHkv0XOAEkIZuV5SBdVRni9ONo4ue_LOkGeXCrfbXs3RzMqMtOnT-6XeApvo4qmtQJEXp2XlMwIyG2zpNA-d2JC8X94WESzirDPtyKhyHvFSi4_RZBOJgw6lRbSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrEUB7E6Tl3pG0Z4OsC8Oo86aiyh7Sk9b5TYyitL4knb5O2w8NSrA_ceGdGA1DWpSCrVPWiwSNMHxb9xxRusTuQo5mSxPsLeBgzT86xmAeNEsoINZHuEoqfhzY1e380JjRqlwaiGpSy0S8TDV1WGXPKHs-EDwsUi_7HHXYhnYMh-PkxpyAHrIKQpYN2YC6Dkin3Ou7H9B1sDa6EuGG0xsfzuxvWJ021wVc7usoTKhfWgDONg6P2Cz5OXRvdvphsz16AV5PftyhkhaHi2120e-sGDyHrmtk5tBREh8jVjVuEYw5dBwyXWK48bjDtApJ7PgJCPtK6Uln2xCKBjeAwn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUucuSzmaXnvljUxYYy5Q3y0Afc_m8_6BBL4cnBu3ksNUkfHM1jBQXXCpk_7eS5ZXJMQTL_WAnVMKmB_E8s6hV9f4KZAFp9yD9IBJ42-hIVWygnmYdONb_iyaY7UOVpjX2Gn143hymYl9XCcXoa0wQUoAJCLmXyhnU5eMIIuveSRf9ufPUCqggNGOFAvgUL5Dtjw7XczP8DyVVWkgxQJnnYYuggTYtl9xqUmNkAXHnEjqKiU1EicYJUQ__bQW0AVUBxM1C-P1VsYGzew7NNcHqunsDEidHx_rXVZygUuyZ9qPxMlqPeYj5GAM8nn7ACPRqWYS3aueFziIAsGL5tQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAFEvRDs0enKu0nTL6eK0Wc6uGmNCMB4YCldXOtgFzRrXDc1B7oAAxTUjkOmPgjXMP1DLE8MdquvC5IWYFGHydWXRHdxS_mOdDiSkHcjtoPSNTlA2K1SI8iVsAlWx-llOkvP9OuOhziwnGuQaU1dwuZ6yvFa0J22K5pSjLkJf2OHHcbLbfFa4SlJ8IqSy7rEkVq0Y4hNA_zVbBRnBABmZtV_6rxCqkFfyXmUjrCOOgDN0FK2t9_jggmOqWlLbPcL-M1XjFjQ1EsoK9jBRbRAhz9-6TwJDhiAk3T_Z4giWaj6iYSBoqw7Au4B9cxxW41A9VqeithdXshdDLgi08Fmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVBYxXZe09wM247fH9w9FTyDyblE3kaXA2-xNOVLcmyjzh-a3x-KVwXRF4SPodlNSyG22SYeSP4lV_5GXhDacOg4zpOMMuVEIiItHBziD-N_EGu3gb4F-Bckmlc5YgO46XmLfZUN-hyD1GoP6CpEXHMKRZB0ArkFqIsi6vsLU78nO0aRlAj5eycF_hUn0EXXkp1uxdZNQWvxU8OOroPn0EHkKbiijGpDkBiC-pJCiW4Rui-zIlJdKQl6B1PJLYgUy08W8KZqQBjDmDmaXq-nPRi4LYc7NXyypG7HfMCVGhGd3N5jtF-6iircCCnP5OBcQ2rQL9aWg3eQz319i1WsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8kX3I29uwycTEzpQHCGu7pkae3OEvF4SchG-OIl0k6sAsoB01Hunm2og8vSkb6zmVED90mlISItzTtF9Gkzfyd-8Y6wROvUyJLNKFyd9MWdIkqRQeTAOwlt_2NBVUbW3xlM-lSa8QLzg4aKVs9fN_GSg2yy46wZcQ_NFk7putAsItHN-w9IHs2qTpT0UVHe1T6r2kh8__B6ZWJCOF7LYb3YOvM7rL28T5uvHcfzAztxBw3YUuVDUrsTmnPk1pB7c1Bnmxxh8EjQdPKsxsr_wADsesFlP_mbdbmH1nzQIkzZ8lwE0U3hPXfXkcyf8lCnP2rSRgnzHq_gtaQTV4cL2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات دانش‌آموزی ربات جنگجو
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/458375" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab762c3416.mp4?token=GLX4wqNvrJ7r-5X2qGSAwpSIOa73RJM8ioZMibmtWaRchAnIncyOrl-zTMX3Irn-tY33q8umKgk_h246q0G6rfFAD2MRD0niXQFpLSZQsw8LdqsL2Q2lDqBuphaYtREO84-1fPzcnYyC2IPEKwZEDlV5nXbVzS4osKchEAC-a4ANTtJbgGqHMyB1BVVXLxo3GUe7z_lEvhbZ73hIruqqo6SqTaDG70ZctBGUt8EwrMzJW4Q2H5G4YjvxSxhGcwajV8TR20O5e_0vq0lbnwuXKNqs-xHXC7e8qCLV8rC2iUuSAwiOGRvdhrHn2ugBsNq-frcA2JGmlHMfE5aOS7vVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab762c3416.mp4?token=GLX4wqNvrJ7r-5X2qGSAwpSIOa73RJM8ioZMibmtWaRchAnIncyOrl-zTMX3Irn-tY33q8umKgk_h246q0G6rfFAD2MRD0niXQFpLSZQsw8LdqsL2Q2lDqBuphaYtREO84-1fPzcnYyC2IPEKwZEDlV5nXbVzS4osKchEAC-a4ANTtJbgGqHMyB1BVVXLxo3GUe7z_lEvhbZ73hIruqqo6SqTaDG70ZctBGUt8EwrMzJW4Q2H5G4YjvxSxhGcwajV8TR20O5e_0vq0lbnwuXKNqs-xHXC7e8qCLV8rC2iUuSAwiOGRvdhrHn2ugBsNq-frcA2JGmlHMfE5aOS7vVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: به استعدادها در هر نقطۀ کشور توجه می‌کنیم  @Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/458374" target="_blank">📅 19:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffaadb724.mp4?token=kHmkzoyu1Ni7VI4UhdzWfhlncMwm_Qom-0zKmoT7zIIhjnEiC5SRtokSGn6rRf7o-WEYUIWS7PCF-0EsE6oahQEejTA7qLSxjWfjiOSSPadsODiy1JkOTY8WvUzPZKhip4x-F5BhAhu2IN29OeTtZt0_OqByQ2mp2vPMzAC_CK2F1mAz2EufRgl4b8KSBDqbm7lKJCv_0nOj_vP9dxvhzkxDXwu49VS_ZaFu8iCP1jHqg63t7FzQ1sE18ySGEfdnNR5Fh1f0Ynf83rP7IgkRBQjIcy3aFPa-05OCA5TS4M8fcXNuoArMMCvwajv5J6qgFqRga2bJQqqjIjgINuaD7RfG9PHUA_XmXMYU0fPxt_ovG8U5NRBX8Qgef7b3KDWKVouCApMsNAEiGML-r-ohVM3CdHWnje8JantAgQPcU3EsyEWevkXwZ2uiXzisnplYkNI3JE2vsE_7aMc9G6Yjjrx84IAmoQx6SKb5T4mH5xUSYcIgi4y62DUQSUEeS932JDnzgwjLt41jVM9g0qGc8ZSKtv8ggY8DgFzVr5qheSbZqgP8eYSnOkM27G1TLBcu_mzzPdwign2FwDE5w3_KtUgQjeUt7LX1OdZY8C7EIEtZJCV4Tdj8Zzmk0NR2a9DEF2qcgpT8t7YB4wEF12F0THup1VHAgqOVqloy-zsYXLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffaadb724.mp4?token=kHmkzoyu1Ni7VI4UhdzWfhlncMwm_Qom-0zKmoT7zIIhjnEiC5SRtokSGn6rRf7o-WEYUIWS7PCF-0EsE6oahQEejTA7qLSxjWfjiOSSPadsODiy1JkOTY8WvUzPZKhip4x-F5BhAhu2IN29OeTtZt0_OqByQ2mp2vPMzAC_CK2F1mAz2EufRgl4b8KSBDqbm7lKJCv_0nOj_vP9dxvhzkxDXwu49VS_ZaFu8iCP1jHqg63t7FzQ1sE18ySGEfdnNR5Fh1f0Ynf83rP7IgkRBQjIcy3aFPa-05OCA5TS4M8fcXNuoArMMCvwajv5J6qgFqRga2bJQqqjIjgINuaD7RfG9PHUA_XmXMYU0fPxt_ovG8U5NRBX8Qgef7b3KDWKVouCApMsNAEiGML-r-ohVM3CdHWnje8JantAgQPcU3EsyEWevkXwZ2uiXzisnplYkNI3JE2vsE_7aMc9G6Yjjrx84IAmoQx6SKb5T4mH5xUSYcIgi4y62DUQSUEeS932JDnzgwjLt41jVM9g0qGc8ZSKtv8ggY8DgFzVr5qheSbZqgP8eYSnOkM27G1TLBcu_mzzPdwign2FwDE5w3_KtUgQjeUt7LX1OdZY8C7EIEtZJCV4Tdj8Zzmk0NR2a9DEF2qcgpT8t7YB4wEF12F0THup1VHAgqOVqloy-zsYXLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیلگر امنیتی آلمانی: جنگ با ایران بر همگان ثابت کرد که این پادشاه (ترامپ) هیچ جامه‌ای بر تن ندارد و درمانده است
🔹
اکنون سایر بازیگران با قاطعیت بیشتری الگوی ترامپ مبنی بر قلدرمآبی و اعمال فشار بر دیگران را پس می‌زنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/458373" target="_blank">📅 19:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teORk6BKKMdF8YUOaJ3-KEC3Z9guSHwtIf5jQkdJtgKgSu_NWs0JqGIZnIOvwC6ru22QNOaSnTMhw9MqNKVLJcTU5Vh7tWCTRyqjPrWbln0yoPZSozrP2unSp58-lu51ZfnMcS77Jqd6S5_wZMXVmuNjJYc6oAad9EbXYvEzFRwT16MyCFZdUvca0WWh-P1gtkV7JQ1T9FdakcIgIjsiYso6uvKacTOxXjcqvzGSP8G7qnCulBkyeKYJYx2T5Xe0__T3BwzBIWmHzqTAjjs95exwGhgJS-fR_CgFM2tLxHJpmR74SJA9o9O2vLv8eh3aeSO4P_YEbe1z9gO7wVWrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک قابلیت پولی دیگر چت‌جی‌پی‌تی رایگان شد
🔹
انگجت:
چت‌جی‌پی‌تی
استفاده از ابزار ارتقایافتهٔ زمان‌بندی وظایف را برای حساب‌های رایگان هم فعال کرد.
🔹
این قابلیت که پیش‌تر فقط در اختیار کاربران پولی بود، به کاربران اجازه می‌دهد درخواست‌هایی را برای اجرا در آینده تنظیم، پیگیری و ویرایش کنند.
🔹
همچنین امکان اشتراک‌گذاری وظایف زمان‌بندی‌شده با دیگر کاربران فراهم شده است تا افراد بتوانند از تنظیمات و ایده‌های یکدیگر برای خودکارسازی کارهایشان استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/458372" target="_blank">📅 19:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458371">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGD9GZwWoqwUMAjtZResc4U3E9Chvv2JOg-uHB_qFf6DG7SjJ4vqrfm2KGUC6xyOWQlomSZ63zWArjQREwDguuOC7Uwk8bZjKVTwMolXwEYQ0amOLFGioIMoMbrb7d0e4GcXsdJ4xxqx5fvB126Gf3fVcOfiklZatOiYTL1UknqNqWwU90GLvxbpgyczS9YBJ3RhbgeL-Xgb7jOMMVVU2cR-w6cAHArwjsJCeXT17L8YvPvWqrFhqTcDe5ZtAoCMl7eYdMRoq7TwsRvmv2nGmfTl_p_8Vn8vidkUAiPIAVylJ1LKs4KgagSma9Uj5f4jzxP1wsMShC7a5LRYD6eWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی نامه ضدایرانی نتانیاهو را منتشر کرد
🔹
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین در حساب کاربری خودش در شبکه ایکسی متن نامه نخست‌وزیر رژیم صهیونیستی که به مناسبت روز استقلال اوکراین صادر شده را منتشر کرده است.
🔸
نتانیاهو در این نامه نوشته که اوکراین و اسرائیل با «تهدید مشترکی» از سوی ایران مواجه هستند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/458371" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458370">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065bec9c7.mp4?token=SQ_bCrVKDhJIsVLvR-kegesqr8GL9alzbuQwenCJAEJofNFsDQ_kUUgR0axt1aw0kT_5ukvh9X27A4qGOBQkI7znVEP7dB0wnn7y_9v6Sga267qbNBQuulj5BVAdCtvjCcM12eD6eotujfFpTHuxBv-R9iFIuV2_aNwotCU0oeME5L20ilPSRMnc7BfpgnNWSUPAmBxz1DiWFC_KRm0lBEAX440DteNkLEic-xYnVjgHCM9trKeL9xwoukMaBlEfQh2NDVGIIB5UFIsG7F2WRGm0mEXymMmLWs8Duua7t_PGdabyM2zoslEZ4ml3G6Q7hQTiYi2eTPHGT0b5oq3gwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065bec9c7.mp4?token=SQ_bCrVKDhJIsVLvR-kegesqr8GL9alzbuQwenCJAEJofNFsDQ_kUUgR0axt1aw0kT_5ukvh9X27A4qGOBQkI7znVEP7dB0wnn7y_9v6Sga267qbNBQuulj5BVAdCtvjCcM12eD6eotujfFpTHuxBv-R9iFIuV2_aNwotCU0oeME5L20ilPSRMnc7BfpgnNWSUPAmBxz1DiWFC_KRm0lBEAX440DteNkLEic-xYnVjgHCM9trKeL9xwoukMaBlEfQh2NDVGIIB5UFIsG7F2WRGm0mEXymMmLWs8Duua7t_PGdabyM2zoslEZ4ml3G6Q7hQTiYi2eTPHGT0b5oq3gwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: به استعدادها در هر نقطۀ کشور توجه می‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/458370" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458369">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK753ReJeMxl71fycR5-CIYm59Kkfn1lLHPJpnoOmHqZ3dtfg0Ilfl74pa3pCXebs_6iNScjRD53ECYZVu1Z2FOV00FpNEiyapiJJCFjT8HuUJtYkTXLeGxy-9kOgoiLmVOLbGtT9pLxbJPI6xg17SW74LuzawNP_obXtJxkhO-uwZOSKao0eaNOmINdAOA02zQ1gfbzLKyXTZH_E1sSlzvnh8NFdEIywzO74dDJ4kFM5xpP2-uJ-SGZw9dUNzjiihrSVv_80jQ6qkpmnoeeWHtriq6Rn82cTLfwxA5C-fR_NLr6-0pNx4mcfbcq8P4FMBMkPnV5da_iqgad9hAwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودای رئیس‌جمهور لبنان برای پایان دشمنی با اسرائیل
🔹
جوزف عون در دیدار با ترامپ در کاخ سفید تأکید کرد که هدف نهایی، پایان دادن همیشگی دشمنی بین لبنان و اسرائیل است.
🔹
عون، همتای آمریکایی خود را به ادامۀ حمایت از ارتش لبنان در آغاز اجرای توافق اولیه با اسرائیل…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/458369" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458368">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6kCQBQOaQLDHgjYKF-ySKDXTB4Y__rOliltuhQfiTi7bZAs1-34-clQEfhLgPzoC73L5Ff4cAQbKgUy0fYvFUjN5c0I93eAdffNf3lCRa7uXb4vWUEY5RZgK2I7knEh_c8NUkIJW3GxeJc2x2EFnBX13VX7cuuKclBV_ybdCQy_xcfJcjTh-kn-ZRufRS5xxmmJIEayECTVT01oT0PuD6KZ0WL-LPc2xQytC08FMtj1M4YZ9Z3B5G1upbsOyN8QwGYRQynMuRzRR7ro8KdDY4MMTogdcQwY2Ju4VIo1bAZid0PSucz-d8HYwzwAqXDucbXR1-aCTi9Kmy0rbed3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان انرژی اتمی: تا تدوین پروتکل بازرسی از سایت‌های موردحمله آژانس نمی‌تواند از سایت‌های هسته‌ای بازرسی کند
🔹
آژانس با محکوم‌نکردن حمله به سایت‌های هسته‌ای ما صلاحیت خود را زیر سوال می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/458368" target="_blank">📅 19:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1845034f.mp4?token=jHt_Q1aW9dT6pwhtKjXRXGCoDpRI4CgMyOvJ_pybboGbHfFP--XKtLPF5jyx8xHAPlMffHs0xdVp2ZcPQR5r5Gxk8aUQKmVQcyp8jLTBz7UtwVPu5ojGwmxPe1nBLY59QJ_sRulfnaLvOSKObENnuBF4mRc7FpZwuCwItZfV1M8Epyl1fhsBb2AGQlHCMom4RH5xAB6Wrfd3qPF9_4Su28ELwTKjtCq7rbUpIcb5FPdDtRtWUORaJsoEwp_3Pj5ffVpAMbLLC-wbW8ARrmkumF9sCT70HWpRoDuPmCdinP3MtoLcUPYic-syZAZRc3AYCniJjbp34w56_7EmfKs1YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1845034f.mp4?token=jHt_Q1aW9dT6pwhtKjXRXGCoDpRI4CgMyOvJ_pybboGbHfFP--XKtLPF5jyx8xHAPlMffHs0xdVp2ZcPQR5r5Gxk8aUQKmVQcyp8jLTBz7UtwVPu5ojGwmxPe1nBLY59QJ_sRulfnaLvOSKObENnuBF4mRc7FpZwuCwItZfV1M8Epyl1fhsBb2AGQlHCMom4RH5xAB6Wrfd3qPF9_4Su28ELwTKjtCq7rbUpIcb5FPdDtRtWUORaJsoEwp_3Pj5ffVpAMbLLC-wbW8ARrmkumF9sCT70HWpRoDuPmCdinP3MtoLcUPYic-syZAZRc3AYCniJjbp34w56_7EmfKs1YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما قادریم همۀ مشکلاتمان را حل کنیم
🔹
من معتقدم می‌توانیم خیلی بهتر از این عمل کنیم، ما قادریم به سرعت تمام مشکلات خودمان را با همدلی مردم حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/458367" target="_blank">📅 19:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBVeQ09E4KUb9BRigP98u0QRrZm51oG8L9TN87-6zcZyv9xrMCijm-_pjr9qDrSd1mBRMZpsSnM9x72xhs1zeMuPMAaFFYCJfqyRZT0-xFeS0ZKJWtUclP7xbb7PTsD9ihywawenY3UkLfYpVTJfmX2AdMw_apN2h8oGaFPY0ZrJ3K9z9mIDDHYH5mzvqM3gfeTCJ_ZyLl9fXenA51Spym6Mlrgw1ogBupMpR8P5Si8HAgWV8fFDnhIIIqCtSpS_ll_np_tDNN6E5zstSLFFx53eBQGefuhJtZjtm_kaI8HLminHtFSNO6D8N-zw6lrvTG9ceB85PmqaJY4_rrJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
🔹
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
🔸
در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگهٔ هرمز مشاهده نشده است.
@Frsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/458366" target="_blank">📅 18:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e0bc9c28.mp4?token=gOi_phsxcLgZdME8I7Fk1WXluqlZ3j3u7pRAc7e_sQuygwOQ7N9lof8E_5OiGZv8opasnlm2NfV0ioPgJ-Sh-ZcQjXQFcv5LJngj-92eVnuiKxRK8Wa_5jMaJKRxCpZo99S2INwnow3JC8NSPvfcCsdE6Z78EmMw6nvDPbAVhXf-FEJW5-7X2MZI0EKop3IRWM_CNxnBBXWFxSataYKxqEllh9itu2WTsED824xzSLjZ-JNINrTAJ3n5bdnjO61PD3L9QX1JTLeEfAPcr0OQr6dJ178kdOE8af8C8IeVYoaxGM-rFbrG7goUZWKa5igZiUN40HUEDyiSh9Az26Ej0zTzym9vKUdrMhrLBQPctfeoCEjvi5h05oLQETjc5GFVH-EmKreWEd5EJhhOjSPxfLQzb3ysG1JBRZzF5SfYX7luv2CxrSwxSLPHHr60PKd-KJ64SGcsxqbEQoc4mIkBm4Qk0cHs3vERHGRuaMy_32yxAHMs0rZ-39Bwz_lubP4ainvRgU9yJEKMhYMAsVVQnyk1yVLj5ZUizw2btzft-62vcQM5USevJihPQdhkQLtTQBBwboPrYfRe67i8St7RRsPVQd7VD8znTyMxRfFzZv9QYFL3QNGVEFlZri1qKRFXGfV8UqAzfr16GiUVjuV1rSngqATflDReyCCNXw4mvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e0bc9c28.mp4?token=gOi_phsxcLgZdME8I7Fk1WXluqlZ3j3u7pRAc7e_sQuygwOQ7N9lof8E_5OiGZv8opasnlm2NfV0ioPgJ-Sh-ZcQjXQFcv5LJngj-92eVnuiKxRK8Wa_5jMaJKRxCpZo99S2INwnow3JC8NSPvfcCsdE6Z78EmMw6nvDPbAVhXf-FEJW5-7X2MZI0EKop3IRWM_CNxnBBXWFxSataYKxqEllh9itu2WTsED824xzSLjZ-JNINrTAJ3n5bdnjO61PD3L9QX1JTLeEfAPcr0OQr6dJ178kdOE8af8C8IeVYoaxGM-rFbrG7goUZWKa5igZiUN40HUEDyiSh9Az26Ej0zTzym9vKUdrMhrLBQPctfeoCEjvi5h05oLQETjc5GFVH-EmKreWEd5EJhhOjSPxfLQzb3ysG1JBRZzF5SfYX7luv2CxrSwxSLPHHr60PKd-KJ64SGcsxqbEQoc4mIkBm4Qk0cHs3vERHGRuaMy_32yxAHMs0rZ-39Bwz_lubP4ainvRgU9yJEKMhYMAsVVQnyk1yVLj5ZUizw2btzft-62vcQM5USevJihPQdhkQLtTQBBwboPrYfRe67i8St7RRsPVQd7VD8znTyMxRfFzZv9QYFL3QNGVEFlZri1qKRFXGfV8UqAzfr16GiUVjuV1rSngqATflDReyCCNXw4mvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: سیم کارت سفید مصوبه سال ۱۳۹۹ بود، اما در سال ۱۴۰۴ رسانه‌ای شد
🔹
پرونده فیلترینگ باید بسته شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/458365" target="_blank">📅 18:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBU8nIvIzhNbyeqmHcHRXkiUUNnQ0o7zCGJzjVPcaT-_7pGq8dX2FhPhFgIDfFMvd2sBalhiFkGmkalyF5PqzntOlG3eGAGOc3w00Kvhc5V9OpcX3qHr_rHU7UMxTh8nAWzyFjASCV-QRt0mJNSsYN2D6U1Fkb2biC3-dUwAm8NNraNaBguK4XviuausTg6b573ggM96TiJn_-kaMd2X7QngpLm0GyI_kwD6_cBlryWF3HhQNFCVAdwnxL2qlaayLautKeXZmDeSA1eci2sG5A707-0VrWuF1dV1dwseFyJ8TxVkbjnMeUSFzMoMepuMeG_HMUFAp8CMRjL6agxngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاوضۀ لحظه‌آخری پرسپولیس در خط دفاع؟
⚽️
ابوالفضل صفرزاده، مدافع تیم خیبر که مورد توجه تارتار قرار گرفته، در آستانه حضور در جمع سرخپوشان قرار دارد.
⚽️
گزارش‌ها از مذاکره برای معاوضۀ او با حسین ابرقویی حکایت دارد تا درصورت وقوع این انتقال، ابرقویی به خیبر برگردد و صفرزاده سرخپوش شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/458364" target="_blank">📅 18:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e992600fd2.mp4?token=toiwjDMgxzR2xyYeFQ2ojBBco9iThaCXHhYjAXbExM_ydqXTIZhDQ7txUt1p6rYO9VcB8mTesVSUiVKpJpGpxVOitELIDbDKJsnVoizge4x5JvOhpFZ4P3ZRpYFRSxIbfGITJlREPUbVJYPY-12AVVUT5URcEO7PAumIELdY2N07Y5HbZrszuaiHk0BMDZSzpQdN2dvciwn-Mri_RdWTghxlvlzFwn5P_FTYMd7BjL84_I-eC_DOm0upCzPXkig6fPTlxey96CKOCZ-4QZy6_JpNvl0riVAH8oivspIq2h3mUAXExAdFFe1GYjbZK9qNOfHofqqbjobW1qTECtccHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e992600fd2.mp4?token=toiwjDMgxzR2xyYeFQ2ojBBco9iThaCXHhYjAXbExM_ydqXTIZhDQ7txUt1p6rYO9VcB8mTesVSUiVKpJpGpxVOitELIDbDKJsnVoizge4x5JvOhpFZ4P3ZRpYFRSxIbfGITJlREPUbVJYPY-12AVVUT5URcEO7PAumIELdY2N07Y5HbZrszuaiHk0BMDZSzpQdN2dvciwn-Mri_RdWTghxlvlzFwn5P_FTYMd7BjL84_I-eC_DOm0upCzPXkig6fPTlxey96CKOCZ-4QZy6_JpNvl0riVAH8oivspIq2h3mUAXExAdFFe1GYjbZK9qNOfHofqqbjobW1qTECtccHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی دولت: سهمیۀ بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/458363" target="_blank">📅 18:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGZzKjcqu_Lp3RUw03Ljf6mHuOjg7yfwivuyaDIRaeEX_lYiQ3MP-YdW-ZEbZeA1StLOApscHIrXgwdL_CmUd4CYtfvvNMRygQP7seyqjY7d_H_226A7kKNF9juLW2p7wKDOKMy2blK-NOv5VqEAufX3iRut8lsSf9hb98h4JGIomGPYeUOPM6OEnmvUPfGvub_XsvSrazzE0rXLWyuL8RWjwMXnbuq3fqysjmBuQUHd2MEfMhIdJG7gFfTpgOdgVFF8n0ZjXzetH2YvHTGj4GOEeC5vyW2gz5WikXoqQAvTB9CNNk0CS5w6jxoDCmscYwrCqRhS5ppZmLdmEUqtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت بی‌سروصدای نادره رضایی به دولت
🔹
نادره رضایی، معاون پیشین امور هنری وزارت فرهنگ و ارشاد اسلامی، پس از پایان حضور پرحاشیه‌اش در این وزارتخانه، بار دیگر به ساختار دولت بازگشته است.
🔹
او این‌بار به‌عنوان مشاور مسئولیت‌های اجتماعی معاونت توسعه روستایی و مناطق محروم ریاست‌جمهوری فعالیت می‌کند و بر اساس اطلاعات موجود، در برخی تصمیم‌گیری‌ها و موضوعات مرتبط با زیرمجموعه‌های این معاونت نیز نقش خواهد داشت.
🔹
اعتراض هنرمندان تئاتر و تئاتر عروسکی به حضور رضایی و عملکردش در معاونت هنری، حضور در جمع‌های مختلف مخالفین کشور، بی توجهی به حجاب و پوشش رسمی کشور در تعداد زیادی از برنامه‌های زیر مجموعه و ماجرای پرحاشیه کنسرت همایون شجریان نیز از آخرین اتفاقات مهم دوران مدیریت او بود و پس از آن، رضایی از معاونت هنری کنار رفت.
🔹
با این حال، حاشیه‌های او به دوران حضورش در وزارت ارشاد محدود نشد. رضایی مدتی پیش و بعد از اعدام قاتلان نیروهای امنیتی که در اصفهان به بدترین شکل تعدادی پلیس را سوزانده بودند با انتشار استوری «نه به اعدام»، مخالفت خود را با اجرای حکم اعدام شماری از محکومان پرونده‌های امنیتی و تروریستی اعلام کرد.
🔹
همه این اتفاقات در حالی رخ داده که شما با سوابق و نظرات رضایی شاید امکان استخدام موفق در یک شرکت کوچک دولتی را هم نداشته باشید.
🔹
نام نادره رضایی همچنین به عنوان دبیر کل خانه رسانه‌های دیداری ایران مطرح شده است؛ حوزه‌ای که در ماه‌های اخیر خود به یکی از پرتنش‌ترین عرصه‌های فرهنگی تبدیل شده است. توقف و بازگشت ناگهانی برنامه عادل فردوسی‌پور و همچنین بسته شدن صفحه «آزاد» وابسته به دبیرکل خانه رسانه‌های دیداری ایران، نمونه‌هایی از حاشیه‌ها و مناقشات این حوزه است.
🔹
همراهی و ارتباط برخی چهره‌های فعال این نهادهای صنفی و رسانه‌ای با رضایی نیز بر حساسیت‌ها درباره فعالیت‌های او افزوده است؛ به‌ویژه حالا که او بار دیگر به ساختار رسمی دولت بازگشته و در جایگاهی قرار گرفته که می‌تواند در تصمیم‌سازی‌های مرتبط با حوزه مسئولیت خود اثرگذار باشد.
@Fsrsnart
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/458362" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا یک گروه حامی فلسطین در انگلیس را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا روز چهارشنبه اعلام کرد که گروه اقدام فلسطین را به فهرست تحریم‌های خود افزوده است.
🔹
واشنگتن همچنین یک گروه حامی فلسطین به نام مسار بدیل، به علاوه دو تبعه فلسطینی را تحریم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/458361" target="_blank">📅 18:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnk91txzRB8lXXvGN-GqQaX-3oOgrRyAYFg4S1u1VaP5Mh0qCj38oWJ18BcZ8R7R7jfy54oxdQcWKJHUjZJdL0xo7DW0jLK78LEBrpJpKZMRMWjEMfNGXfER3pivLnjm01FcoAbsJBAhuJlPdwM82BsI6pskBjnf7VWmnb-YZd7WlR3Ib9mHXE0ic761cwbieWvp6pf5zBkzvqZLq-F-XsMnTWI15wisFto_9WFyuhfbMaBDGMedDM2IjDgpSu3ZB1bsrxcdjdLY-i9xiRI3ymloiVMd_JfUb6qOe-S4QIkCxv1zMqM5E46BYwN6eH_R2gsB4eWO7fGNpGxeOZTXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعات
سرنوشت‌ساز برای بیرانوند در لیگ برتر
🔹
ساعت ۲۴ امشب پنجره نقل‌وانتقالات لیگ برتر کشورمان بسته می‌شود و تنها ابهام باقی‌مانده وضعیت علیرضا بیرانوند است که طبق قوانین از اول مهرماه سرباز می‌شود.
🔹
بااین‌حال کنکاش فارس نشان می‌دهد که بعید است بیرانوند از تراکتور جدا شود و او از اول مهرماه که دفترچه اعزام به خدمت بگیرد حداقل یک‌بار می‌تواند تاریخ اعزام به سربازی‌اش را تمدید کند.
🔹
به‌این‌ترتیب به نظر می‌رسد بیرانوند تا پایان جام ملت‌های آسیا در خدمت تیم ملی و تراکتور خواهد بود و بعد از آن این بازیکن احتمالاً به یک تیم نظامی می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/458358" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ca08c30a.mp4?token=eznwAv00xSgiZBfS1RiJ76PXn5B_tBGTNKDy0SbUMOhq0zG5ayAnJuteU7YmAeHhSM8v-EIEbxvaxo8U_0bt9zsHF88LQpzB9dm6CpN0byQUse1_HhZhX2hpRCALMLicuZ8qxG9ZDEWIGrO_uu--fGUlJisP8i3IFhfAf3A4zfMh9H8CzM-3ZrvQnFdiqTMYsJHS0nlfFcgS0BCTty7UEIv3NCD_lNid8f32cuTR57G5G3W71urhG2JG2Bv9lcrAn9c491D3-G_3V0_WhJiIov34pyQimIc6yCZkA7brdOfKcsFto2_H1xSoEVug-PWpF5m_vyrny2D57pBFBGQepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ca08c30a.mp4?token=eznwAv00xSgiZBfS1RiJ76PXn5B_tBGTNKDy0SbUMOhq0zG5ayAnJuteU7YmAeHhSM8v-EIEbxvaxo8U_0bt9zsHF88LQpzB9dm6CpN0byQUse1_HhZhX2hpRCALMLicuZ8qxG9ZDEWIGrO_uu--fGUlJisP8i3IFhfAf3A4zfMh9H8CzM-3ZrvQnFdiqTMYsJHS0nlfFcgS0BCTty7UEIv3NCD_lNid8f32cuTR57G5G3W71urhG2JG2Bv9lcrAn9c491D3-G_3V0_WhJiIov34pyQimIc6yCZkA7brdOfKcsFto2_H1xSoEVug-PWpF5m_vyrny2D57pBFBGQepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: شرایط امروز نتیجۀ تلاش‌های پزشکیان است
🔹
بیشترین جایزه را باید به آقای دکتر پزشکیان بدهیم؛ با پیگیری‌های شبانه‌روزی ایشان، پایداری مالی کشور حفظ شد.
🔹
شرایط امروز نتیجه تلاش‌ها، صداقت و دستورات مؤکد رئیس‌جمهور است.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/458357" target="_blank">📅 17:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy3HplBhOE5XyvoUZ-4HuUZaQd4AiQ1L3-pQ9FqoKy8unTa8LSIoQT-jHHc7c3KFEEEnNkEpMO4QfN3Yb6Rm39Rg1YMcgwIK8IEiYV_YaS8FnxXgrcvUEW7x61LNYQdPkvGuLxGjw4Tpadzm0J_tqgp--j2ogLibUunYk5KltbyNqJM8hyt_7xwD9K07zwVbZrqGs0luVj-Eo0yAnJcinWAbpTw-lmFYmhl1p2awdQ__IPS-gsGxhKCx8vn-hpIZbKCiztmhLjhD29s3INxtj66BxXASBdTOp5iLE9InsLg_YFbc_jrql8mP9ouqauNgcTKoOtQD082yEAkuSOaVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۶ ساختمان و یک مدرسه نوساز را در جنوب لبنان تخریب کرد
🔹
ارتش اسرائیل صبح روز چهارشنبه با بولدوزر و مواد منفجره دست‌کم ۶ ساختمان مسکونی و یک مدرسه نوساز را در جنوب لبنان تخریب کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/458356" target="_blank">📅 17:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac73baf88b.mp4?token=h95qN6utgRv-t6dLyI4UXcMrew-UNtnEtlCJ2XVbQZW0VlVhq3IO8gu5SZ1PmHTXoh_46cb55-c6tbb4YfnNrhyj173LeX-k75STg9Ljr8e19ckxdBn_tbvrjZkp01Gy97nTeapXEmgaOdqwiRsroM2lgBvAzmtKOSCEPDwxZZa8j8IbgT5g_xbqKSPQ6RoIgV-r6O0U5q7iOnDBtqjsdOjfya1re_YmdOf55GdXG5OTB4zsHW5ns2NEZoH_D8T85KKAw6BV07mxlmxwaHMnOczJXVVeeI3EfJlgW-Eo599pfNUIFhu-A3VMfR-MlUq02tPp0qazGtUoJdvQkJ2FWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac73baf88b.mp4?token=h95qN6utgRv-t6dLyI4UXcMrew-UNtnEtlCJ2XVbQZW0VlVhq3IO8gu5SZ1PmHTXoh_46cb55-c6tbb4YfnNrhyj173LeX-k75STg9Ljr8e19ckxdBn_tbvrjZkp01Gy97nTeapXEmgaOdqwiRsroM2lgBvAzmtKOSCEPDwxZZa8j8IbgT5g_xbqKSPQ6RoIgV-r6O0U5q7iOnDBtqjsdOjfya1re_YmdOf55GdXG5OTB4zsHW5ns2NEZoH_D8T85KKAw6BV07mxlmxwaHMnOczJXVVeeI3EfJlgW-Eo599pfNUIFhu-A3VMfR-MlUq02tPp0qazGtUoJdvQkJ2FWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب در مرز نپال و تبت چین، ۱۷ کشته و صدها نفر مفقود برجای گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/458355" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
زاکانی: قصد داریم ۳ ورزشگاه جامع در تهران بسازیم
🔹
قصد داریم ۳ ورزشگاه ۴۰ تا ۱۰۰ هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد؛ کارهای تملک زمینش هم انجام شده.
🔹
آمادگی داریم که ورزشگاه ۱۲ هزار نفری که در جنگ موردحملۀ دشمن قرار گرفت را بازسازی کنیم.
🔹
۴۰۰ میلیارد تومان برای ساخت ساختمان جدید فدراسیون وزنه‌برداری اختصاص دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/458354" target="_blank">📅 17:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5OGDBXsPSFbJKgJKakGT_D8DBtbXWQZoAkfic-ATUGRp87xv0FX71v3qYgLO3zr4K_3GVCL3ZSzbYrA-gOB44llDCBwZVEV4ygLO0u3vLT2Dqmhxg4KgKI59qRT-9AU1DOzNzc8EW96Kpwukvbjme6i4OtJZl2qRMYQS4kqVlGCqJnJUrFfBCQAvJYOXHwLTYcyyA-BsIdnt60A9T5Vu_kjA3ZNjLOk_dwSYZ6jiwZl3oxm5ZfYNq4asPvWZISVQpHyjCs8DpASHsjr6pAFkz4syv2HshEyhABE_33Wwi6_3DPusKImc_RxePd2wgSD8tk_Uu5RRJy0MqfsLU_C0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ برنامۀ زمانی برای مذاکره با ایران وجود ندارد
🔹
هم اقدامات اقتصادی و هم نظامی «موثر» هستند و عجله‌ای برای مذاکره با ایران نداریم.
🔹
رویارویی آمریکا با ایران هیچ جدول زمانی مشخصی ندارد و هر چقدر هم که طول بکشد، ادامه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/458353" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2def08b9.mp4?token=oKbh1Y497ugmFb6qaeNiSFJ8A2a5oiVNxCfj1CKPJD3O0bULYCuFd--4xYfkJny-264XDQr1bh5shnTW8POvqJwjGzAUDwbTLylmqs4U6YFN_yiY-K9H-ZoIqDn9POUFESeOcyKkZLeBkxSgw8dpi-dXl1NcZ4Xa705bzxISJ6Z3YRjGr44AEW7D6Dh8ZPWg0JZdsxQcwf_tGaSu6aeSwFLz6JrzUGTM3tY9z_p-FGU1LDDveKU4JLzbiP2BVb4Ai0YRUCg2k4ou3koZ1igm9u8sf6qbCjdBEUHQznSlRLnR-Bf--4WiNteoGEWl3Xmfi69W58cC0IEqnzclhS6M4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2def08b9.mp4?token=oKbh1Y497ugmFb6qaeNiSFJ8A2a5oiVNxCfj1CKPJD3O0bULYCuFd--4xYfkJny-264XDQr1bh5shnTW8POvqJwjGzAUDwbTLylmqs4U6YFN_yiY-K9H-ZoIqDn9POUFESeOcyKkZLeBkxSgw8dpi-dXl1NcZ4Xa705bzxISJ6Z3YRjGr44AEW7D6Dh8ZPWg0JZdsxQcwf_tGaSu6aeSwFLz6JrzUGTM3tY9z_p-FGU1LDDveKU4JLzbiP2BVb4Ai0YRUCg2k4ou3koZ1igm9u8sf6qbCjdBEUHQznSlRLnR-Bf--4WiNteoGEWl3Xmfi69W58cC0IEqnzclhS6M4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ اقتصادی آمریکا و پدافندهای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/458352" target="_blank">📅 17:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGBgBAxr6kOo_hDemANXFrztAz3XmtttAMm4ImjVWMZyIYZzv5Kv3l9njQZwQM6msRglt9TouuvPc9cL1Ihw7d1dfa1Zd74v9MJbOrWO87SyJmZJkigaPmSKiysH4bprYc7F4kQDlA8l8fz9vbL2PNHRGnqak7Ytnfkiv940WSdCRb07Atb6FrbVOTCIj8Jomr_EXrqu-w2327z0x8JYq75Ug5KtmtTXbpRA3ZvUuLA5c_9ri8rBsODSypDSOYKMWqLM98tsxP1VW3AiKX_zKOdnmHUN3BTkxmNS7yWvfj3peueY1c3CeBn_W1NkMGJbv1Wt7S2MY1tW7JBvLePd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت قاطع رأی‌دهندگان دموکرات‌ آمریکا از تحریم رژیم صهیونیستی
🔹
نتایج یک نظرسنجی جدید که توسط مؤسسهٔ یوگاو انجام شده، نشان می‌دهد که اکثریت قاطع رأی‌دهندگان حزب دموکرات آمریکا در نخستین ۶ ایالتی که در انتخابات مقدماتی ریاست‌جمهوری سال ۲۰۲۸ رأی خواهند داد، خواستار اعمال تحریم و توقف کامل ارسال تسلیحات به اسرائیل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/458351" target="_blank">📅 16:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptKUQV-ZvmQYYaKRmzmpzbn6lsKtSi30R7YGwsMV5lwzlXpojT0YIfbIhCAaWQsfwmy5R0zmFmDOJB7aBX_46L4b_xIcG1_Q-1iOiYE5iApuAT0cZ-zzoNTiRieubJbmNVgfmECr-UClANF1qIHLJEC6jteWzLlYwSb-lzvL3MN9mrV_QGMZK3fsUPdrz4eRLTzBoU_2OhIblGvUbm3dU7_2M6hQiEuMHm5VBO3Ek3ZW_jkssuNZN-BIJm1Pdaoi3eU5Mi4Ua3Y-EVB92aNaa8Y03XJwz_TTaMKHoI-n1961jGLDo2_FAJNLpD47yFhBofTT0cI9DOzD7YKRRdh8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شکارچی: می‌توان رسانه‌های معاند را در بانک اهداف نظامی قرار داد
🔹
سخنگوی ارشد نیرو‌های مسلح: رسانه‌هایی مانند بی‌بی‌سی، ایران‌اینترنشنال و رادیو فردا مستقیماً به موساد، سیا و سازمان‌های اطلاعاتی دشمن متصل هستند و از آن‌ها خط کاری و پشتیبانی دریافت می‌کنند.
🔹
افرادی که در این رسانه‌ها فعالیت می‌کنند، سربازان صهیونیسم و آمریکای جنایتکار محسوب می‌شوند و حتی می‌توان آن‌ها را در بانک اهداف نظامی پیش‌بینی کرد؛ زیرا از نظر ما این‌ها رسانه نیستند.
🔹
هر خون‌ریزی و خشونتی در عالم با پشتیبانی این شبه رسانه‌ها انجام می‌شود؛ این شبه‌رسانه‌ها منشأ ترویج، تبلیغ و گسترش خشونت در جهان هستند و روان بشریت را برهم ریخته‌اند.
عکس: محسن باغستانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458350" target="_blank">📅 16:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjROvNzaGTxLeKkdgclp7x29asLD1F6qW_oLEOreQM6a1a_EBAJDMILDpgyrNb6bcrTT1gZL2J9DdPAf6o-hBzxnznVW0Ur3JXU1J9rzTKUMyf_qNQNuMqdfJV78wMhDjx-gPrw6uh_ichoOpgiO3cRCC3nLAIXnnTzbdxv3sFQDjTwoRVa4ydHotqJUjobLVOIxAjc-uV4A3jiPdclM4xOaveKFKYIASWikguUMJ8dqYQPKDIXRfa7rUWz_3KlxhoFou-pyHoPcu8GP2la1DQVDAGsCpLzHY-omWq3wOAkr5g9MF4FMOODjxLapbLbmM3fY5g71nYr46Npf5l7FAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریتانیا در آستانه ممنوع‌کردن تجارت با شهرک‌های صهیونیستی در کرانه باختری
🔹
رسانه‌های بریتانیایی گزارش داده‌اند که اندی برنهام، نخست‌وزیر بریتانیا احتمالاً طی هفته‌های آینده ممنوعیت کامل تجارت کالاهای تولیدشده در شهرک‌های صهیونیست‌نشین واقع در کرانه باختری را اعلام خواهد کرد.
🔹
روزنامه «تایمز» گزارش داد رهبر حزب کارگر که در پی اتخاذ موضعی سخت‌گیرانه‌تر در برابر اسرائیل نسبت به نخست‌وزیر قبلی، کی‌یر استارمر است، «تحریم‌های جدید و قدرتمندی» علیه شهرک‌های صهیونیستی اعلام خواهد کرد. بر اساس این گزارش، احتمال دارد تحریم‌هایی نیز علیه وزیران راست‌گرا و شهرک‌نشینان اعمال شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/458349" target="_blank">📅 16:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7088b0e406.mp4?token=BIOBT0ERwClltgcf09kK_qce46g2oWTzibybUAw0yPPqEwi-rZ-ZxAIX1xeRbiC31T_RrsXsza9t8ObBrLMGV8oa7zitkWqwk_1q7oNnM_hF2A9opMYBCwUk6dj1s5NMISLWV5B2WXyhZfgVQE2FyDTDCRMmZ2XMbveoPL1Xi5dXj4w_2UcSmLVwSJRT7XpTVTb7ZQAMJ_UMZPzKkfFd8WGrb6RS9v7CuI3Y3GqWH5wazA2kywYq-9TsoDP8KjIgLG_WnLdH8NizuJcN_HkGKuQ2_P_2hxAJNO73lZc9H8WiokXSGS7obS5515xg78Q1sxmeOn-ba0jy3uoDQMOziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7088b0e406.mp4?token=BIOBT0ERwClltgcf09kK_qce46g2oWTzibybUAw0yPPqEwi-rZ-ZxAIX1xeRbiC31T_RrsXsza9t8ObBrLMGV8oa7zitkWqwk_1q7oNnM_hF2A9opMYBCwUk6dj1s5NMISLWV5B2WXyhZfgVQE2FyDTDCRMmZ2XMbveoPL1Xi5dXj4w_2UcSmLVwSJRT7XpTVTb7ZQAMJ_UMZPzKkfFd8WGrb6RS9v7CuI3Y3GqWH5wazA2kywYq-9TsoDP8KjIgLG_WnLdH8NizuJcN_HkGKuQ2_P_2hxAJNO73lZc9H8WiokXSGS7obS5515xg78Q1sxmeOn-ba0jy3uoDQMOziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی چگونه به درمان کمک می‌کند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/458348" target="_blank">📅 15:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA9EBF_aOjy5h2bDXr66XQvB4Lt5_Wq_dp6YEa9DPlahmn4Y1jQaP5zzFT4kRluBEEiLa8DxEsOQlXsoJrX_0W23jesh2zRn9pjJ6TqmINJ15JSGJEU_Xejt0ymB8rAMfyxBrN356JsZ_lW_sGEi133rbyBh52jFK9Ir7kw0NotMvgt9WMTX3yEPZYYXtkhYII5RrU_ND-CaBN_4fLmAgnZmoB9XFsRLeHs8KQMFTf0geXaORDW8K2n7A3t6swom8xJpxsmAupsmXlp7Hgj4B6xryv_V3fJ77KFWbRAEr1jSO1CNDXP9Tu2u2DKqMMIjVS6fZ-iZikkz83-2sY_M1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندهٔ ۹ سالهٔ جذب استاد روی میز رؤسای دانشگاه‌ها ماند
🔹
رئیس هیئت‌عالی جذب اعضای هیئت علمی: دانشگاه‌ها در جذب، تبدیل وضعیت و بورس اعضای هیأت علمی اختیار دارند و هیئت‌عالی جذب در اجرای پرونده‌ها دخالت محتوایی نمی‌کند.
🔹
یکی از آسیب‌های فرآیند جذب، ورود نگاه‌های سیاسی و دخالت افراد خارج از دانشگاه است؛ در حالی که جذب استاد باید بر اساس ضوابط علمی و بدون مداخلات سلیقه‌ای انجام شود.
🔹
حدود ۳۷ هزار نفر ثبت‌نام کردند که ۱۷ هزار نفر واجد شرایط بودند و برای جذب حدود ۱۲۰۰ نفر مجوز صادر شد.
🔹
شکایت متقاضیان در ۳ مرحلهٔ دانشگاه، وزارتخانه و در نهایت شورای عالی انقلاب فرهنگی بررسی می‌شود و بخش زیادی از افراد پس از توضیح درباره روند انتخاب، قانع می‌شوند.
🔹
حتی افرادی که در یک دانشگاه پذیرفته نمی‌شوند، نباید از چرخهٔ علمی کشور خارج شوند و می‌توان برای ادامه فعالیت آنها در دانشگاه‌های دیگر، مؤسسات پژوهشی یا شرکت‌های دانش‌بنیان مسیرهایی ایجاد کرد.
🔹
نیازهای آیندهٔ کشور باید پیش از ایجاد رشته‌ها و تربیت اعضای هیئت‌علمی مورد توجه قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458347" target="_blank">📅 15:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce73d744a.mp4?token=vULQoSk-bt8U_oaHvA2F4a4FjKa7fm7XWA2dZGoeE2oNGzVNWp9mPrjyYdSOE76Aqi1XROeJV9wrMD90L2O0zKLjkenXlwo9pJvYjImvK-5QMl5szTBUJE7pzcTubEHf_IsC0kheDctVKI6pGvlHgx7EOHGFOWm3So0gMJn4Kpmuz5uG5iJyWpXL91CwGAa-gkwm6yaLksyLZ8-mttQQA8T1leIRSZp9SaIcflwbIUu-73DvmEAh_DIGR8P9vqaq52cZGP_BMAJ3HotHdJY3nWv9rZPRngYSYk7Z7_5saTWJEAJeabgCF9vXPvULzu_otTyp9_40CUZTZizOL9OBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce73d744a.mp4?token=vULQoSk-bt8U_oaHvA2F4a4FjKa7fm7XWA2dZGoeE2oNGzVNWp9mPrjyYdSOE76Aqi1XROeJV9wrMD90L2O0zKLjkenXlwo9pJvYjImvK-5QMl5szTBUJE7pzcTubEHf_IsC0kheDctVKI6pGvlHgx7EOHGFOWm3So0gMJn4Kpmuz5uG5iJyWpXL91CwGAa-gkwm6yaLksyLZ8-mttQQA8T1leIRSZp9SaIcflwbIUu-73DvmEAh_DIGR8P9vqaq52cZGP_BMAJ3HotHdJY3nWv9rZPRngYSYk7Z7_5saTWJEAJeabgCF9vXPvULzu_otTyp9_40CUZTZizOL9OBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدۀ تازه مدیرعامل شرکت توسعه: ورزشگاه آزادی آبان یا آذرماه آماده است.  @Sportfars</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/458346" target="_blank">📅 15:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suc83JkeckUduFe12OIUhRzLy17LOekWoyKy38G2SiUoYCF0b5iwSBgoe76evQHt9okqGIDEo8eOjCXOSShCVvr-hQBlMXFpswFm3cOe1iZlF2DtgEKsbjU1YaEKkAcDXpMgfrNUBssywDgKhSaHI6Vh_lb5onlfx9BmwDuIrPxfauDDrtYhUTEZ8xg0u4pHenV2c1CgDo4OMMG0wL8I4DNuEjPLsekbeYSTLnQ2PejXhX2-td1HXIKIackBwhMpNQVVgnSF5Z82ypdN3Ova-haQJyD7cS-sbapZkuzw7CTEelJnTcyEm0C8-bNSCGBzUb8uTUTYZBm2tnsFMBk2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ایران در جنگ رمضان آسیب‌پذیری آمریکا را آشکار کرد
🔹
سردار محبی در نشست تبیینی دفاع مقدس سوم ویژهٔ اهالی رسانهٔ اصفهان: ایران در جنگ رمضان توانست در همان عرصه‌هایی که آمریکا قصد داشت کشور را تحت فشار قرار دهد، آسیب‌پذیری راهبردی این کشور و متحدانش…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/458345" target="_blank">📅 15:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/347ead572c.mp4?token=o2_jIvkSk4RR7WvPR7tHUkIatWC_nhp4Zyw8DBKFHdxeKWpWlx1tti6t6ryUZnzLUrCUHZ7ximEdzuXB5Y9MHM63BrJsyPepf3gdO7xZDc16UqHaQ-_Jw-aJAmA3EZ1P82oFLGTX0jexTalOLWJ36zEcIavgirIpTL107xgVc1Ue4QeaIV5-bVFw-4sNNPufuLwxK9OfNjL_vSNhB6YL5mN88jRYHqJPIvtcH47Vr4_B2W-qi_eV0l_51FVHwsEK7l0_BHVyg07uVKLIlQd8bUkeaXZNbvT1HdxzcFQ1npOjgAF0p8oPuiGviIh7bgZRY6L2e42nkQrb0LBRB8EDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/347ead572c.mp4?token=o2_jIvkSk4RR7WvPR7tHUkIatWC_nhp4Zyw8DBKFHdxeKWpWlx1tti6t6ryUZnzLUrCUHZ7ximEdzuXB5Y9MHM63BrJsyPepf3gdO7xZDc16UqHaQ-_Jw-aJAmA3EZ1P82oFLGTX0jexTalOLWJ36zEcIavgirIpTL107xgVc1Ue4QeaIV5-bVFw-4sNNPufuLwxK9OfNjL_vSNhB6YL5mN88jRYHqJPIvtcH47Vr4_B2W-qi_eV0l_51FVHwsEK7l0_BHVyg07uVKLIlQd8bUkeaXZNbvT1HdxzcFQ1npOjgAF0p8oPuiGviIh7bgZRY6L2e42nkQrb0LBRB8EDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: بیش‌از ۳۰ هزار نفر از عصر امروز خانه‌دار می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/458344" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPcrwpO0JhKFf2bJjd9c0Em6BfS3F2aR1ze2MTk7u2rwXkE-ans7rzsaHFohU9FV_iV3Oe5kL5tfTCzYngAhPaC_ZtvJSo6BW50v9XdJJ7LDgrAsml4H6KuIh8SzzkDBwLJ7ngUjwNHoLUilc4VWSZgTltmB1EUZhVlTyKBJb4s4Bap-sVXgtGDY9kVvd8jrg2_UE66hIZd9eiln4L0as64lHr3B_V76Xy_SjQ-s_hzhoM7gBDeKIHakAf7qjIXSrTCKPXF1zysbTrugPwsdtsWaPjS0dkjncv_rHdRQWKsnWltYPDHshIzb87Ilt59v7RuoKUWhDvyCEgKM-O_ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ایران در جنگ رمضان آسیب‌پذیری آمریکا را آشکار کرد
🔹
سردار محبی در نشست تبیینی دفاع مقدس سوم ویژهٔ اهالی رسانهٔ اصفهان: ایران در جنگ رمضان توانست در همان عرصه‌هایی که آمریکا قصد داشت کشور را تحت فشار قرار دهد، آسیب‌پذیری راهبردی این کشور و متحدانش را آشکار کند.
🔹
دشمن با استفاده از عملیات نظامی، رسانه‌ای و فناوری‌های پیشرفته از جمله هوش مصنوعی به دنبال تغییر ادراک جامعه و ایجاد زمینه برای ناآرامی بود، اما انسجام مردم و همراهی نهادهای مختلف مانع تحقق این هدف شد.
🔹
آمریکا با بهره‌گیری از شبکه‌ای متشکل از ماهواره‌ها، پهپادها، رادارها، حسگرها و هوش مصنوعی توانست سرعت شناسایی تا اقدام عملیاتی را به چند ثانیه کاهش دهد؛ اما ایران نیز با ارتقای فناوری موشکی و هدف قراردادن اجزای شبکه عملیاتی دشمن به مقابله پرداخت.
🔹
کاهش ذخایر تسلیحات راهبردی آمریکا و آسیب‌پذیری زیرساخت‌های این کشور و متحدانش از عوامل عقب‌نشینی آمریکا بود.
🔹
پیروزی‌ها و دستاوردهای این جنگ باید توسط رسانه‌ها برای نسل‌های آینده تبیین و ثبت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/458343" target="_blank">📅 15:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
سیلاب در مرز نپال و تبت چین، ۱۷ کشته و صدها نفر مفقود برجای گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/458342" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP0IJr2i_dRilWVRnKNKf8K8BEvwi0g1BRsZE9-t14TRK-RsecPnED9XmxyXz7HRHMaRbwiwT7JRtgpV580sRO6EYN4w0GctK5x9cmDr0QV2rh5tCcOsSHVBayCJFyXuZCQoghixix5QXAomtK5tce6na17W8PYq0vrQP4mw0nM0mKRmRUe7ZYfGoGXaGett0DKHS2_zk8WLh5lB5JgaFsCV9sNIQ_g1M2LrT5atFC3KONQX18IPm-UGNtKt1Iyo47b_Zz0liKkKHX_JJR2ar2jtnsV2qWM5WcdcalfWYn3yDaierg4qpq2xl0-0Tk87gNMQa_j-L5lkMLMNuVQlcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۸۲ سلاح قاچاق در ۲ استان
🔹
سخنگوی ناجا: در ۲ روز گذشته ۳۸۲ قبضه انواع سلاح های جنگی و شکاری قاچاق و ۴۴۹۵ فشنگ در استان‌های کرمان و خوزستان کشف و ۱۲۸ نفر دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/458340" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egLE_KOYefNNgmORyZATGeef5iEvbRQNkrpuOkmZz1jxCFoTt2hvNW6VOmLra87e752Do22UxfLNSBoB0jqZaKApYXkB80qDe7hsmkh891nm6i07YXnyIm_xCnsqVDVKvdvzpxFvDjHwOMZst9-z9iDMp0vy6hRWbKWAr599bPeEzVFM4yHtVO0UFuGqoXUJQD4hzVS3vgGaPFXJm3bmeXDhEMlEskmaJr-_CPouR0CNeUR6PPjrhybUZ2iI78c3yaK0s4u2u4G_QZNcQEXqAwkH_3rZE4cKn2lfNvfLngSpGvw5NW6N-ySLLfWhTjBufkyDEBka-Vok8Z5R0uPGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: واکسن آنفلوآنزا هنوز وارد شبکهٔ توزیع نشده است
🔹
به‌طور متوسط سالانه حدود ۳ میلیون دوز واکسن وارد کشور می‌شود؛ اما امسال هنوز اطلاعات دقیقی از تعداد واکسن‌های واردشده، منشأ تأمین آن‌ها و زمان توزیع در دست نیست.
🔹
اکنون زمان طلایی واکسیناسیون است و واکسن باید در شهریور و نیمهٔ نخست مهر تزریق شود.
🔹
با این حال، هنوز واکسن وارد سیستم توزیع نشده و دربارهٔ تعداد واکسن‌های احتمالی واردشده نیز اطلاعاتی در اختیار نداریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458339" target="_blank">📅 14:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igvqeQjeviqqe-dewpTK31JQgP8hYvq2fLEWpbDyY8xCazIXeXgVuAYWvRBVtN5S7iXRES_TDgSMHpn82iRhVLLppSHY4wzPoFCpM2g0C9meLIO29FjxqE58kVz1t6Q2fHeHujMViH4IRrb7Dpij9J1xQTuhUDrmb37al2cZmKmwftCPSZ5b2396LEdx1S7O1nzfhy0TBa8oFLyI_e90NWgNoJNv5Cp3-1Em1F5k2fhZsFlWmQ450lcARBE6jvuxG3zuF9xSWccvCYDg0XQHPnZKfFXO2WkvkreNTkNzRzcDjXJPjstAnAqxjV9OB1uIuTR6kNZ92TScuE-WlirCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار با کارت ملی مشخص شد
🔹
نرخ پایهٔ دلار برای خرید با کارت ملی امروز ۱۹۵ هزار تومان اعلام شد؛ دلار در بازار آزاد نیز ۱۹۸ هزار و ۵۰۰ تومان معامله می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458338" target="_blank">📅 14:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHeXwfQ9wJZ78ETr1o_lqRit2ZJJpnDxG3H78Zk6-Vs_gv_4634b1TqzsZXiCRotoR6xwRH6y3vWKWXnhLXAGXcctulWaiaw5cqRueWpgoxWW5RwOgLkv6bE_buK7ZPmtJl6e_gosjh6_ocfxMefRwwh2F0npvocyvll9zdSy3KUUMjFcrzvq3xPiNIL1q6BmziqbOSWInaHS4oLWQMOdaBYkaQjQcA5RiUVxEemyY31-WT5Sew-smvLL6PS7W-WkgJV9pQKOibr-xN-e1s1E7gjavaIXlkuAtaT9qgqiM5HhxAxxPv-H1CUQAOsBpwfb_dDZ8DQZCD9b1yyaCrJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ میلیون لیتر بنزین بیشتر در راه است
🔹
شرکت ملی پخش فرآورده‌های نفتی: با بهره‌برداری از پالایشگاه‌های آدیش جنوبی و مهر خلیج فارس تا پایان سال روزانه حدود ۱۲ میلیون لیتر، معادل حدود ۹ درصد مصرف روزانهٔ بنزین، به ظرفیت تولید بنزین کشور افزوده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458337" target="_blank">📅 13:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1ea55ed6.mp4?token=ZgEdfQkhIj5OjjLY-tJpXx8iai5IU4XArtyEI6uZE0ATsnt_-479Q_uHujLEacDv1Qt05OgAB-nwuMoGh4wG6v9ceUSG9fjs5a-lB1mH_raZsZuujn7F2MypTkbWeIPxSi-_IY5cxS8pGGBEQAB6piDF8dVcAozLYa2EZbUQgEQFBWoprIRNhxgGGFh_HpjpXDzH6sWjYJa6j_70DHqsskZDVsGYIKjyHiNrOSKJOBzgXujwNmGqk6uO_Crb_FoBPTWsjgjDnJ8F6iBLu_cofqF7kj7OTzlA_A2IeP6SpHdz6pVPGlGqdSTFJznSUhUqg2iEhgg-FJHQV1Kf_JX5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1ea55ed6.mp4?token=ZgEdfQkhIj5OjjLY-tJpXx8iai5IU4XArtyEI6uZE0ATsnt_-479Q_uHujLEacDv1Qt05OgAB-nwuMoGh4wG6v9ceUSG9fjs5a-lB1mH_raZsZuujn7F2MypTkbWeIPxSi-_IY5cxS8pGGBEQAB6piDF8dVcAozLYa2EZbUQgEQFBWoprIRNhxgGGFh_HpjpXDzH6sWjYJa6j_70DHqsskZDVsGYIKjyHiNrOSKJOBzgXujwNmGqk6uO_Crb_FoBPTWsjgjDnJ8F6iBLu_cofqF7kj7OTzlA_A2IeP6SpHdz6pVPGlGqdSTFJznSUhUqg2iEhgg-FJHQV1Kf_JX5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ۴ نیروگاهی که اوایل جنگ مورد حمله قرار گرفتند را بازسازی کردیم.
🔹
بقیهٔ نیروگاه‌های آسیب‌دیده نیز احتمالا تا تابستان به مدار باز خواهند گشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458336" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458335">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0y4bn_9Ft2WsVfCeydtaijT-OQPXzXhYEEoY5Ij6p224boXwF25jYm_ooGm5DstQs2YLP_AWme4xeE9cB721dIHeqzy5U-BHoYxcfB_4u1XA5ykNa_SRHp-0GiMJqOlOwp1QQ6Ayxw53xOol3K8vLCtXi_uwdILeELTE2Fty61YvgDZFoTDAI5AvZGVftG_5MiNa2grqTrhwA5yd8IwfCXi8CPMbxH8Vzy7qnstEGVIMUZx1rovpzoOcwxMk_nVljjF2-7KqoyjPKeTaFS2imTKZkZxmUYur7kO0qnmbPToPipLnQUKOyASe4G5zrgvnqDojykFyNn3WeeDwqLN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را با رکورد جدید به اتمام رساند
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۱۶۲ هزار واحدی به ۶ میلیون و ۳۸۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458335" target="_blank">📅 13:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pW6l6YC-oAlcga1Fg1UcdHZVNaIfI2LrI98y5ADAxr60VmdzOmubyjZpPRKEXYAUC3rS6Xdm55Hu2ENQ5KO00HDJ5AK_JYQlYHzQauylFhXTEjwqKY9NXyhw_12Sc7Cl7FeCAt3ddbxDZbU5aJZmiqxwAlwmBq8gTsVJjm2zhUg1tgijV-0mOrbz9DnJcPsPldwzqD_M1woU7yTIcJkkWDQieXhAgts5sYAUR3M83EPeWUfQW8wZooVNIN3EVCVL5Zec6YTt-jJL13LlePCyG8ZypHOHHWn35yKD5-ubg811Um5oWxtFVItWXk9EtCYU2rrmiJ38AHckymOW9EWCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی فدراسیون فوتبال: قلعه‌نویی تا پایان جام ملت‌های آسیا سرمربی تیم ملی است.  @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/458334" target="_blank">📅 13:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b345137d.mp4?token=vtG1zXXNYgAJLzXTwft74j5L2jhzHLADo_eUTKa0Lonx9gvIAQ1PbsM9cQH6e2F9R9rhAkUEpuMEmqgWUTrtR_18bH4k1VDeFl647DTFD8gPWyAo00mfgMAkbeTX9-Caf_D87lUTi2CRluMImKj-S1GC2ySglwURgnAU1drkHOFNx696NB7lqIG6KJvLhx5TL-1Sxax4ftRac9sN8c-vtiMGdfKHc4vIcltE1-vQbjj0G6tQIdP9pi6lx45HkNIVj86Hgbv8GE6sfL9Lo5B76sVXSPlLimnzJXezYpbfaIurJvMGls95ugynlXecsT8_4GAEYHnB6L4UpJT3WTMt2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b345137d.mp4?token=vtG1zXXNYgAJLzXTwft74j5L2jhzHLADo_eUTKa0Lonx9gvIAQ1PbsM9cQH6e2F9R9rhAkUEpuMEmqgWUTrtR_18bH4k1VDeFl647DTFD8gPWyAo00mfgMAkbeTX9-Caf_D87lUTi2CRluMImKj-S1GC2ySglwURgnAU1drkHOFNx696NB7lqIG6KJvLhx5TL-1Sxax4ftRac9sN8c-vtiMGdfKHc4vIcltE1-vQbjj0G6tQIdP9pi6lx45HkNIVj86Hgbv8GE6sfL9Lo5B76sVXSPlLimnzJXezYpbfaIurJvMGls95ugynlXecsT8_4GAEYHnB6L4UpJT3WTMt2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: آیین‌نامه برای سهولت در کارهاست نه ایجاد پیچیدگی و ابهام
🔹
در نوشتن آیین‌نامه‌ها دقت کنیم که خود آن‌ها پیچیدگی ایجاد نکنند؛ آیین‌نامه‌ها به گونه‌ای نوشته شوند که کسی برای ابطال آن‌ها اقدام نکند. @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/458333" target="_blank">📅 13:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb90b20a2e.mp4?token=tQS2AO2b2URCM-bnrPL6ZNCDwRGOBVxm3hyt5I9l-82C_VDFSjqhTjgtHySE3zHzx6PtAxa6fTkRU0xsQbhsSACzqXxi-1NEByCThhDWZiT_Dua80N1iCoHvCJzQvQh49pgXl5_dxoA1lRlYnDPFnlHaKaXTFCeLkxYDmEmP7_904WBUx29SFD8H6Sw65DOQcNz_Voaxr16MLHBs2BoW-YsPrmuKcwTbxHAi49SqOOV89U4aoMEIlbdFehVm3Pv7o5liV3SUq8o3JnCV8DXEVfrGZh7U1sTgVcvD2fiss8_QpIIb5HPuvxulv-GSu4AYg_ooUwYc4DALXw5k_rOw8G3QoTJuHfsMNuayzDj4H1VWxYl6Wc4E-UAC4iPk0ZgowXbvXSQuJPKWCmGotPrVSAYxTMMyngO5M26XvG1z6ftLarqMxHMLHhs94Rp1Ej1NhGmWsaxhD2UG3Z7FtWFxDwVZplc53YT9Ve4qhfDOVEDsbQd7QKBOaJrzv5HwVVIt-vn9xEZFxiSzBJFrTe2ZZGZhENt0nGhUCo5XSPBuGAfW7G_EUFsovL-HIUJlN_1eE08vjBNEidbhaBWEoQ0sfqnRkKGNH4xnlA6EOntjCvZ-BizqwOFePc_mUpvhBeueyib33BnoVo54qQhTTdP8AJ0HgnBRbPFN2TGz4FuaHO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb90b20a2e.mp4?token=tQS2AO2b2URCM-bnrPL6ZNCDwRGOBVxm3hyt5I9l-82C_VDFSjqhTjgtHySE3zHzx6PtAxa6fTkRU0xsQbhsSACzqXxi-1NEByCThhDWZiT_Dua80N1iCoHvCJzQvQh49pgXl5_dxoA1lRlYnDPFnlHaKaXTFCeLkxYDmEmP7_904WBUx29SFD8H6Sw65DOQcNz_Voaxr16MLHBs2BoW-YsPrmuKcwTbxHAi49SqOOV89U4aoMEIlbdFehVm3Pv7o5liV3SUq8o3JnCV8DXEVfrGZh7U1sTgVcvD2fiss8_QpIIb5HPuvxulv-GSu4AYg_ooUwYc4DALXw5k_rOw8G3QoTJuHfsMNuayzDj4H1VWxYl6Wc4E-UAC4iPk0ZgowXbvXSQuJPKWCmGotPrVSAYxTMMyngO5M26XvG1z6ftLarqMxHMLHhs94Rp1Ej1NhGmWsaxhD2UG3Z7FtWFxDwVZplc53YT9Ve4qhfDOVEDsbQd7QKBOaJrzv5HwVVIt-vn9xEZFxiSzBJFrTe2ZZGZhENt0nGhUCo5XSPBuGAfW7G_EUFsovL-HIUJlN_1eE08vjBNEidbhaBWEoQ0sfqnRkKGNH4xnlA6EOntjCvZ-BizqwOFePc_mUpvhBeueyib33BnoVo54qQhTTdP8AJ0HgnBRbPFN2TGz4FuaHO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: آیین‌نامه برای سهولت در کارهاست نه ایجاد پیچیدگی و ابهام
🔹
در نوشتن آیین‌نامه‌ها دقت کنیم که خود آن‌ها پیچیدگی ایجاد نکنند؛ آیین‌نامه‌ها به گونه‌ای نوشته شوند که کسی برای ابطال آن‌ها اقدام نکند.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/458332" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW87AViHSh5IfRpqKgLZhi6C-v7WsWRQ51FGvvl-AkLHQOK0ETt5S9RMFG6CFE9fZArOg3bGtZ-QNLviLBhsg-PrCSHIg03Jdkllpth3XK_XIGPlMLz8_l1E05_YnhffFPpiPkRSoCmsURRXfB4EzoELdL4-EqwC6NdBZyitHcu9YhgSKp5UmTquS1JQKcciyn99abZ62Ar4B3a2Lgf1deApEGMo39L_FiyeY298Uuut4Y4YqsLNcHQ_jOZQdZGAk2B2C7BdlCeXWYKX08S9UXMgLHmDyjfgY05_jI7cwqwJgBn_XnZ8RrMlP3Xpaexh9K5Zwhzbo-SfwDNdCKWSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی در تیم ملی ماندگار شد
⚽️
دبیرکل فدراسیون فوتبال: به جمع‌بندی رسیده‌ایم که آقای قلعه‌نویی تا پایان جام ملت‌ها سرمربی تیم ملی باشد.
⚽️
انتظار داریم او تیم ملی را در جام ملت‌ها قهرمان یا فینالیست کند. @Faresna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/458331" target="_blank">📅 12:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W14I42kLGVkeStxHa0HC3YrN3TrmNbJJ26U3oZB1_fKN4h5-akquf_oW3KMP-K6QpwXGkFdj2dSF_0rdOVZaFoQIYgyaqgyLy4_HFAC95BvxJVPB1kNIOZePRxQYDeLwzDyFnGaQLJt_9FqtiDVrlhGCA5g2kC2Fkb5HolO631b5i_CciXrc5M-vR5rL8GQXWH-PX-XrHKy6uCo8zOIVU-JGMsOSVMJL8oJrI46aK8aO1jPgtTXYxFgF4WBGWGi72SZ32MSSpj6gcjnVpE5SYF2Kw-Kg3yoZBTd9rUedssghB_8TbdoudIOJUr7BMn9A9xQ8ksrX9iAHjqZCe5oqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: بدهی ۷۷ همتی بیمه‌ ریشهٔ کمبودهای دارویی است
🔹
رئیس انجمن داروسازان ایران: کمبودهای دارویی کشور ناشی‌از مشکلات اقتصادی و اختلال در گردش نقدینگی است، نه شرایط جنگی.
🔹
بدهی بیمه‌ها به داروخانه‌ها در یک سال گذشته به‌شدت افزایش یافته؛ بدهی تأمین اجتماعی از حدود ۴ ماه به ۸ ماه و بدهی بیمه سلامت به ۱۰ ماه رسیده است.
🔹
تأخیر در پرداخت مطالبات، توان خرید داروخانه‌های خصوصی را کاهش داده و باعث شده شرکت‌های پخش و تولیدکنندگان نیز برای ادامه فعالیت با مشکل نقدینگی مواجه شوند.
🔹
پرداخت بدهی‌ها در قالب اوراق نیز مشکل داروخانه‌های خصوصی را حل نمی‌کند؛ چراکه این اوراق برای بخش خصوصی نقدشونده نیست.
🔹
درحالی‌که بیش از ۸۰ درصد خدمات دارویی در داروخانه‌های خصوصی ارائه می‌شود، ادامهٔ این روند می‌تواند فشار بیشتری بر این بخش و در نهایت بر تأمین داروی مورد نیاز مردم وارد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458330" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQdAii93td1yjleJr-JqxuYVuyHfMspEQ9aNvc1K0Qgaf3E0uPtzcbmsABDE1v_5-ISLN22SqGfbjYYEo0I7bOV4KGbbB6klxi3Wm1qEFuc_lC4xMpJ7zlPGSKnakpphd3Zlv179EAgUMtu0IulTwkVwh4_lwyMr2sUytRUw_7hq8FKayZpNWaYt61Cb5sZyR7Vwgu5AiecyZRpeOsnGGz2MmB8JHNKz5X1a0_mIH4Z66i10Gwm2EHyHtG5DxsktesF9HltplUoEI_NvR_MS8eiSxAp6ZElnfQ5yqUzzZAhdfZj82jIKkFOBXiItZqZwTXQB0fPqzoRA0NOd4aR8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جهش بزرگ 5G همراه اول در آمل
🔹
همراه اول با اجرای کمپین «سرتاسر آمل در مدار 5G» سایت‌های خود در این شهر را به نسل پنجم مجهز کرده است.
🔹
مشترکان مشمول طرح می‌توانند با شماره‌گیری کد دستوری ستاره ۱۰۰ ستاره ۵۱۱ مربع، یک بسته ۱۰ گیگابایتی اینترنت یک‌روزه دریافت کنند. این بسته برای هر مشترک تنها یک‌بار قابل فعال‌سازی است.
http://mci.ir/-QSZV3Q
@mcinews</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/458329" target="_blank">📅 12:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">🌀
آپشن‌های نقرابی از راه رسید
قراردادهای اختیار معامله صندوق‌های نقره در بورس، با صندوق نقرابی آغاز شد. به همین بهانه‌ با دکتر امیر تقی‌خان تجریشی، رئیس هیئت‌مدیره گروه فیروزه گفت‌وگو کردیم.
این گفت‌وگو به تاثیر‌ این اقدام بورس کالا بر تغییر در سازوکار قیمت‌گذاری و داینامیک بازار، بهره‌مندی سرمایه‌گذاران از مزیت آپشن‌های نقرابی و تاثیرات این اتفاق بر بازار نقره
در ایران می‌پردازد.
🌀
افتتاح حساب بورس کالا برای آپشن
#نقرابی
😦
سامانه ایبیگو
https://firozeasia.ebgo.ir
😦
سامانه کوین‌آنلاین
https://coinonline.firouzehasia.ir
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/458328" target="_blank">📅 12:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/458327" target="_blank">📅 12:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CteJ4MXe6VMDuYR_M5S3tS6FDPNhh2lekzZdlKe7cT4P6bOld32A8ZdkPa64TjcGHV5sMD25Oj288UITun6RNM2_cKutSrztBrUVXzz5Y0zSn2TbPO1cRdA_Hg36z90PfFd1wNuy0k-_WoQis4kZcN5yzu-Q61Er1u9Q0dL4p5FWkv7n9TJq9PZ9BwcxruCWSuFJ4J1s3m9rdZ0oaWJtfd_3TXWDefGoAWMZ0UZDbfrs9rJJsn9KJQO0g-_AL4CiS4HnJRoKDF85UoCzhQVFvg2SFuGIJQMmHT2ODrkpoopQKchv8vnpS9FZ-AVDVEWh4ZDbSwZweLcbEiUM3lnDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌‌مجلس: نقش ایران و عراق در ایجاد نظم منطقه ای تعیین‌کننده است
🔹
قالیباف در دیدار با رئیس شورای‌عالی قضایی عراق: آمریکا در جنگ نظامی و سیاسی از ایران شکست خورد و در اقدامات اقتصادی نیز شکست خواهد خورد.
🔹
این‌که قرار است نیروهای ائتلاف آمریکایی از عراق خارج شوند، یک افتخار تاریخی برای دولت و ملت عراق است؛ امیدواریم این خروج به طور کامل از زمین و هوای عراق محقق شود.
🔹
لازم است کشورهای اسلامی بحث‌های اختلاف انگیز را کنار بگذارند، همانطور که دیگران دیدند در جنگ غزه همه شیعیان کنار مردم غزه بودند.
🔹
تردید نداریم ایران و عراق در نظم منطقه‌ای به‌ویژه در حوزهٔ خلیج فارس می‌توانند نقش تعیین‌کننده‌ای داشته باشند.
🔹
فائق زیدان هم در این دیدار گفت: من پیام همبستگی ملت و حاکمیت عراق را برای شما آوردم و آمادگی خود را جهت همکاری با جمهوری اسلامی ایران اعلام می کنیم.
🔹
همکاری و توافق و ائتلاف‌سازی بین کشورهای منطقه راه رهایی از ناامنی است و تصور می‌کنم این موضوع بسیار نزدیک است.
🔹
معتقدم هم آوایی و همبستگی ملت ایران و عراق یک همبستگی ابدی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/458326" target="_blank">📅 12:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/458325" target="_blank">📅 12:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpm7KofZ6_1AlHl3XuJ8CeAcObPZedL5HEBpTB4clYitNP6uQuvFLA-fdGfZdKtxDuUJP56BTUdrlRDzuesXYeVhKybikKqdHpsct_qWP-d3wU0tZ0p97804Bst4KUjyW7AqtIzXOhv5vb2HfpiqZ9ZP0IXSJWzgkP14RYbGURPp5PX68EmXSnuiJ5v6XOnNvo3Yp3gQ1cKYw3gHBVPvwXzbZhlOhSz62FUpSqNQrteaLN4rVPAJjpgxVULLogPVbk_nmbm_2_6J0GfeKZdqNCN6GZpuqK1UjHsosaOkjtbc5KekX-5VYZgMuO3FdGlIaBgk-N95_8wxEmkneMyuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ حملات جنگنده‌های اسرائیلی به جنوب لبنان
🔹
به‌گزارش خبرگزاری رسمی لبنان، جنگنده‌های رژیم صهیونیستی بامداد امروز شهرک مجدل زون در صور را هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/458324" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ZAcOEoWW56A-eJ03Vm2O8CFEHpfZM2h_SgMTCTLZW2jXSixQj2XdfW5q3HK0c22otisnKWSUk0rcryLulwmIESrfFlrW3FCfFGLsBlrTwyfaixy1nsAFabiJlglBOyZbG6YnFsqJbuOLJ_hwk41HKIz6Ny7xfwo0H7LwG47GsS2kVu3POVz5Bh_dy872zpd06CIZ4VLTh0Fert9MtKuipihYfQLMSFGlwET5YsGv9hTr2RJl_YRx5LqJ8s1uzAaSknyg72mcoC13w7P6T57-ciOTg48DhrfaFXFXglzoWtrQ_qJUklXZeQqjiDvYp-hibiwf3_xsTstZh37tInGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل شلوغی پمپ‌بنزین‌های تهران در روزهای اخیر چیست؟
🔹
صف‌های طولانی در برخی جایگاه‌های سوخت تهران در روزهای اخیر، همزمان با افزایش مصرف بنزین شکل گرفته است؛ به‌طوری‌که مصرف روز گذشته به رکورد ۲۶.۲ میلیون لیتر رسید.
🔹
افزایش سفرها، استفادهٔ بیشتر از کارت جایگاه‌ها، گرانی تاکسی‌های اینترنتی و برخی ابهامات در اطلاع‌رسانی دربارهٔ سوخت از عوامل افزایش مراجعه به جایگاه‌ها بوده است.
🔹
از سوی دیگر، محدودیت سوخت‌گیری با کارت جایگاه و اتمام سریع موجودی در برخی جایگاه‌های پرتردد نیز به طولانی‌شدن صف‌ها دامن زده است.
🔹
این شلوغی‌ها درحالی‌ست که شرکت ملی پالایش و پخش اعلام کرده تأمین سوخت کشور پایدار است و مشکلی در تأمین بنزین وجود ندارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/458323" target="_blank">📅 12:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekJb9xsFYB7TA8paWUj4ksMVq2xE2_qNhoEdGJrCVnoUWfelBr0iWW2tvx6akSDsV_Os8KxJZsPvoMGzfUK37CodzS0kyxwOoxRqbGtxOvdXHjUkDeWMSQ12oY5gzdgPLDDlfEwQg0DoCs3IanN2KBY8AdR9gHz2P_ncfEbXRoBB0FwuaqMq3FzWO5f7l9NYrLQV7zbsSqx12c9-MXST_mgqmP49Yu1esTygERAgobMmIpfodaFl0yhXJ6-L78aAKPql7hoDI_rdrKT9tkWLMapAZYTEvd8aXYUJMMzy01NsZkfrEb6PZGceRddXIK0pQS__JqluH0o1yp-FW4t3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۷ کیلومتری زمین، نوار مرزی کردستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/458322" target="_blank">📅 11:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در پاکدشت
🔹
سپاه استان تهران: درپی انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت، احتمال شنیدن صدای انفجار ناشی‌از این عملیات تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/458321" target="_blank">📅 11:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9lr2jihaCPZ_P-ZLg7qdiQPMYghyBHoV9WmTcoaqWgQ9WD7lcMN-QZmD6fyzEhUTR4fN4JXz-PnbDKN4tC97mMzJY8uUBKhBO26F0TI0Gw48Zv3XA35G8ST4C9qXRbJ5Ewiaxp11wEe5ZWQkpvs787yj5YGA79a6uAldeLZYwYDMR767fq_0mNhgG0GvFSRNiC7fjzEbIlyzeXrqRVIDasoL7icM34ojDQZzAN_0KLgyzwoKeq4qy5NhikzVUEhhVxiQ0q5_a45BCyA9T0ls1BbAoC3fKEgkx7bWOXfKj7SSXs2tFHhIHNd6aOheOzAvWQiAEFrmP_BpVuZcfIfBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج آزمون کارشناسی‌ارشد اعلام شد
🔹
سازمان سنجش: نتایج اولیهٔ آزمون کارشناسی‌ارشد ۱۴۰۵ اعلام شده و داوطلبان مجاز از ۵ تا ۱۰ شهریور برای انتخاب رشته فرصت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458320" target="_blank">📅 11:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAsWtUvNpkgR7jr17WBudeafFZ_IWDaq0GOTWh2d9os5ZVjWmonunhJYlLQVnvqxVy-YDK3eoi5wKBCRc6fJm_3av7XCFxNSFlzi7zmIlM0dZWGYDMGR7LRzOcTUdbpn4ZuoiQOkckcBso9gbSRIP2gdROKNPEQ1cJa54_vOiRcT2V8BHX2c1yGVCGRLzENCjq984acs4rhm7epKAtJeqTo4QlbKR4YGbeFhweYaSgMn7B_60LCsYWOmIDxE5NZn0JbczbxA6WwUaANWa_9kv97r7mj-rquCIxM9FWS-zaGnPTZEPHnXTRUcPbJ_LChanJhoCvGheNuvLLCNaBGnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: آموزش دانشگاه‌ها در سال تحصیلی آینده حضوری است
🔹
نتایج آزمون سراسری در نیمهٔ دوم آبان‌ اعلام خواهد شد و به‌همین‌دلیل دانشجویان ورودی جدید با تأخیر وارد دانشگاه‌ها می‌شوند.
🔹
کلاس‌های دانشگاه‌ها در سال تحصیلی آینده حتماً به‌صورت حضوری برگزار خواهد…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458319" target="_blank">📅 11:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoLI8IDkPxb-yns7D3EXkDxQsGxzMBOHiDNymbSui-3vsdVMLs1juj50tDcCCKOfrOMEf8J_BAemzfnITmEF0HSzdX_8x2oKPt1dJ9ngyiEQ0oiNjKF1_RAG3Z6c-MsliYoilep8-INjiFqxKvxklTVKTzgxez4YUs5LO03sJEfFcNYIM2-UFQ1NH4LJz3xXII_lLG7dN_byaxhRzfTTCuy-XZtRYqoBZyD_yak1QvnradLxaEkURB9twauK6iaPI7nKaatg5ZY4gAnpH9djgFbiY37hYGcb1h91DPP7mANDE_hC4xpbAcjPKtWAjgrVlCE7GJ8MGWqE60rP4VPo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات لندکروز و لکسوس برای ایرانیان مقیم خارج مجاز شد
🔹
طبق اعلام گمرک، واردات تویوتا لندکروز هیبرید و لکسوس LX600 و LX700 صرفاً از مسیر ایرانیان مقیم خارج از کشور امکان‌پذیر است.
🔹
براساس این بخشنامه، ایرانیان واجد شرایط خارج از کشور می‌توانند یک خودروی سواری شخصی وارد کنند و این خودروها باید از محل ارز در اختیار متقاضی و به‌صورت بدون انتقال ارز وارد شوند.
🔹
لندکروز هیبرید و لکسوس‌های LX600 و LX700 مشمول مقررات خاص هستند و از سایر رویه‌های واردات خودرو امکان ورود به کشور را ندارند.
🔹
خودروهای وارداتی همچنین باید استانداردهای بین‌المللی را داشته باشند و در گمرک مورد بازرسی قرار گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458318" target="_blank">📅 11:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml5dfsJ5kU5BkiUOECI_jQPniagV5HOCljPq0Wgz5UHU-33D434_SeyJPfw05MwbT7dLOG2VS873KeYwwii3CVGLSfTnrpi29Ez-dOhQTosebelsTrf70fxyz9rQwamn5IIX8z41xnNRniO_pTuSn57xyNJ3-kJHEn5yTnOXtpDWv1f0IgwATIUcL8l-ZnPzQA23YwzC4eTP0QLg2RbavOqXyOFHKWzFkpp78TJTNRjbk8t5TK4JApixzDTMSPSHjr73pPokFMBTla23B2_SvyXB5rIIj7XiGTVhWDZfyIlH87HSbdYYglgWkmSxYPw16r9_HWGIDf7iNoweihl0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: تولید و جایگزینی سامانه‌های پدافندی درحال انجام است
🔹
فرمانده نیروی پدافند هوایی ارتش: تجربیات ارزشمندی در جنگ تحمیلی سوم داریم که در تاکتیک، تولید سامانه‌ها، چیدمان و آمایش سامانه‌ها برای ما مفید بود و تغییراتی ایجاد کردیم.
🔹
هم‌اکنون در شرایطی هستیم که با تکیه بر ظرفیت‌های ۱۰۰ درصد ایرانی پیش می‌رویم و سامانه‌های خود را اضافه می‌کنیم و سامانه‌هایی که در جنگ تحمیلی سوم امتحان خوبی پس داد را تکثیر می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/458316" target="_blank">📅 10:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6botjMJzeT5gX83y3opkAahSEC9Ol9PlWa4V4TRcOo0FKSZwJCoY1njAbrOWLsq0TyYOOZmJbZPScKSsMbkBLl6sl3zyVUbEgVv1ghTmSj5pmRR1Y7-PShfdlORMIEg9kJjKkqd5YW3zjOi7PZhKTvqZHOWoCC14X3djKQW-5J5gx769S2VVJa1JAsQgH9CnTOXvtvvBHYT0ua4XlqPozykn_-S4Y9XmUYN0Sx6G6bv1j34m6AwGybeY3_jnAwAihfw9PMm3WfWW-qWSVwx3zkeo8pcQ82p4xkX5TUaWaMfCJ29OGt0MM4LUL6AqpAQ17__2mfFfhSgyFniP6fnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۸۵ کیلوگرم مواد مخدر در کردستان
🔹
فرمانده انتظامی کردستان: در طرحی ۴ روزه ۴۸۵ کیلوگرم انواع مواد مخدر کشف، ۶۶ خرده‌فروش و توزیع‌کننده دستگیر و ۳۱ معتاد متجاهر نیز جمع‌آوری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458315" target="_blank">📅 10:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuDZsyjHsY5Qwha4VZo3oL7K0ZD-k9m7UFqKlkGy70Oafr7G3S4Ew3oAjg-DtA_MZxhedLA7iCAti9EJv5-FRSYOhuq1nSlc8O4L2mgYQDzQtCVOgnlzhQU4bzO7y2had8TW3ZDVq89WzshVt7xOYBqV5aL56jVEIi517GmGWu-ZHo4DL1UDDnSBHoFqxXxoHYz0xxcGejBHMOaXiDpvEHhJXRkYQhBUeFodjYBjecV0W2XHcM63cUDSyTIYwFLJFQfmVE5JOwbQH0GM2xaLCY04PKyBE5q5MFzhQQB5ZwLMmDPoEBh5AhIXobLmr_yrPDlo3vLyOd4EIoOPSBkdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۱۳ کودک درپی آتش‌سوزی در یک بیمارستان پاکستان
🔹
درپی وقوع آتش‌سوزی در بخش زنان و زایمان بیمارستان مؤسسه علوم پزشکی پاکستان، دست‌کم ۱۳ کودک که بیشتر آنها نوزاد بودند، جان خود را از دست دادند.
🔹
مسئولان بیمارستان موفق شدند یک کودک را از محل حادثه نجات دهند، اما شماری دیگر از نوزادان در وضعیت وخیم قرار دارند و احتمال افزایش شمار قربانیان وجود دارد.
🔹
منابع امدادی اعلام کردند که آتش‌سوزی احتمالا پس از انفجار کمپرسور دستگاه تهویه در بخش نوزادان آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/458314" target="_blank">📅 10:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8Gu8xGqwFWpkhrwnvRmPuJPP5GGB1puzo8GB8KsIi7PfyviloRTx9bKaRb4-HV0s41njVANa_9oBsrrORCj3ZQX2WYSLdgealVT_hw3NCGDecAJ5pFTYL93ipQHD3SMC7mmiW-_pCYOQRJpgtdu7B88EagSZW81P1e_lkDG5Kci-3GlOReF3CpaBFr6E2nOk-gghJDoepU0P-VFZg4eQx_bBLSpbe9mu-9q7jLJqGD0uomRgj9Gc0i82FcBEOZvszcYVHrlHMWh_O9sBg0PX6DbysADJ5GvCs5znuW9Y2fgC6zzWkk1-bmNiOkEOVUNm03v8Z5dM9op_XKUFofKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ فردا شارژ می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/458313" target="_blank">📅 10:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458305">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUNwCIYb_wcxKKZA2D4Pg1S3B_SiFYb5MAfPiV87yCmRggLDh55zOJM9C0E8NpOdBUtZ2vZ8ggYu3cVDwxegzOAZF6vkZqtER98mL6-yYUlKRVGA5ZLDNGeM6e9As5SW_sykmPSsqWF6xD5kQzX5_ZlfpXZVkttDM47P8EuLPVuFc9Wcl0q5RlA6TQ9-aRN-Hcu9YpwxeUV0NT9eNs95qjMXbMZE7SL2FhGnQF9B2mCGr5yPLyZ8DdUnBOZUML1oR4pr6wCcjYW0lzLfqwOQz_DWc7nA_m9YD4hXndImYClP0RWsIlq5iLl4iDzUKzZIfWxxhxoulmOEpdOpAAqlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سندی که برای جبران شکست‌های برجام امضا شد
🔹
پس‌از خروج آمریکا از برجام و بازگشت تحریم‌ها در سال ۱۳۹۷، بخش مهمی از وعده‌های اقتصادی این توافق عملی نشد و شرکت‌های بزرگی مانند توتال و رنو از همکاری با ایران کنار کشیدند.
🔹
در صنعت هوایی نیز قرار بود با اجرای برجام، قرارداد خرید حدود ۲۰۰ فروند هواپیما از شرکت‌هایی مانند ایرباس و بوئینگ اجرایی شود، اما در نهایت تنها ۱۶ فروند هواپیما وارد کشور شد و هیچ هواپیمای بوئینگ به ایران نرسید.
🔹
در چنین شرایطی، دولت دوازدهم به‌سمت امضای کنوانسیون رژیم حقوقی دریای خزر رفت؛ سندی که از همان ابتدا با انتقادها و اختلاف‌نظرهای گسترده‌ای همراه شد.
🔹
قرار بود پس‌از امضای این کنوانسیون در ۲۱ مرداد ۱۳۹۷، ۴ موافقت‌نامهٔ جداگانه دربارهٔ مسائل مورد اختلاف، از جمله موضوعات اقتصادی و زیست‌محیطی دریای خزر، ظرف ۶ ماه تدوین و برای تصویب به مجالس کشورهای ساحلی ارائه شود.
🔹
اما حالا با گذشت ۸ سال، این وعده‌ها همچنان محقق نشده و موافقت‌نامه‌های مورد انتظار به سرانجام نرسیده‌اند؛ مسئله‌ای که بار دیگر عملکرد دولت دوازدهم در دورهٔ پسابرجام و نحوهٔ پیگیری تعهدات مرتبط با کنوانسیون خزر را در کانون توجه قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458305" target="_blank">📅 09:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458304">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bdd39e3.mp4?token=c6OIb-7sZokfZhKe-rsGmZSJYyxDS-Qx5TH3evAACPVbGx4LUPJyAHFfwpUCCK-IsRCWxG4LD1lkBgXbByE35EPsWRjr8IxZuHzTROIbBJTIsPX-N5jBirlml3NxO1aHaKLZitrpZyIN3Pw4kNywR1SjVHs9uYOhhAI6LRZAXir_7zDH48f3XniWZb1rvB4zPFoxfMNpz7bfyYB1a-7FXUJCtu2Fm8MU2ljJQwETAAgIENFjdRsKUSEI_-llw9CcY9rpxaW94l3IUi_RaceBlqrfDh6EpbbW7II0QAhlB1VE6SW5XHmtahu56asxqRUjz_0oAiSS2XhHFYll1M8DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bdd39e3.mp4?token=c6OIb-7sZokfZhKe-rsGmZSJYyxDS-Qx5TH3evAACPVbGx4LUPJyAHFfwpUCCK-IsRCWxG4LD1lkBgXbByE35EPsWRjr8IxZuHzTROIbBJTIsPX-N5jBirlml3NxO1aHaKLZitrpZyIN3Pw4kNywR1SjVHs9uYOhhAI6LRZAXir_7zDH48f3XniWZb1rvB4zPFoxfMNpz7bfyYB1a-7FXUJCtu2Fm8MU2ljJQwETAAgIENFjdRsKUSEI_-llw9CcY9rpxaW94l3IUi_RaceBlqrfDh6EpbbW7II0QAhlB1VE6SW5XHmtahu56asxqRUjz_0oAiSS2XhHFYll1M8DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ مرگبار آمریکا به یک قایق دیگر در شرق اقیانوس آرام
🔹
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که در ادامۀ سیاست بهانه‌جویانۀ «جنگ با مواد مخدر»، جان یک سرنشین را گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/458304" target="_blank">📅 09:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d2a92f83.mp4?token=IZVdiOW2pSwaZd_5OD55s5Mdho1s_Xh8z1lKeqN9VTRZ5dKTemU60wxYYhdPRl3-ZK8U7Ref6NWF5Rh1VBorXyPW6CGUgfON-_ksH0LaNJphpsr-FP0a6Yk_zqzTu3UJ0H-AIXQKmWJxwzsgF60F-HyhFw0PGOBcSFJV7XFFBy3LVH2PtHrLSDowEyqnWV4rnPc_cy1B8XT6_giZOy2sXabQWsSPfGWDY-9pU2ZI0KXOogyGQaj3Bl2Yh2nF4i_wLsxZUK9H5E-zOsj30iXELvfCTduO3IcAo5nwUZLR7JDx8PXnyR2_Fh_BQa0uvROZbPIg_HIHzEO76S8zxnn2gULxEwdKlq8LxGkMNWcR3LS11jWrHKDh9bXv_bgt4KDtdhJ2VkpzhostdrOCraZ5L1U2g_H9RTdKoJkpsDofIHokWQ1WwppFv-fMAtTs4g_JyjxSpzmvh8lar2D1DImE3Mo0VFAzojgVTNYx7PTfxS_Y8ikgiQe_c8YS-COynJU6F5ZVD6PiBcJDtfi6c1IvXCZISDW0AUUb5YqGx2iH29QHcDoFC1_3RwPW1OR3z3izprQzqlQKNgI6ph7uaod5jKswXLZFYCAaqe1rQjFF_0FqJw4En6nC5U4em0-YBCNHKS5ThdnPyax7OVLCkW66TiW0id7PKjWr9WXD65V3F74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d2a92f83.mp4?token=IZVdiOW2pSwaZd_5OD55s5Mdho1s_Xh8z1lKeqN9VTRZ5dKTemU60wxYYhdPRl3-ZK8U7Ref6NWF5Rh1VBorXyPW6CGUgfON-_ksH0LaNJphpsr-FP0a6Yk_zqzTu3UJ0H-AIXQKmWJxwzsgF60F-HyhFw0PGOBcSFJV7XFFBy3LVH2PtHrLSDowEyqnWV4rnPc_cy1B8XT6_giZOy2sXabQWsSPfGWDY-9pU2ZI0KXOogyGQaj3Bl2Yh2nF4i_wLsxZUK9H5E-zOsj30iXELvfCTduO3IcAo5nwUZLR7JDx8PXnyR2_Fh_BQa0uvROZbPIg_HIHzEO76S8zxnn2gULxEwdKlq8LxGkMNWcR3LS11jWrHKDh9bXv_bgt4KDtdhJ2VkpzhostdrOCraZ5L1U2g_H9RTdKoJkpsDofIHokWQ1WwppFv-fMAtTs4g_JyjxSpzmvh8lar2D1DImE3Mo0VFAzojgVTNYx7PTfxS_Y8ikgiQe_c8YS-COynJU6F5ZVD6PiBcJDtfi6c1IvXCZISDW0AUUb5YqGx2iH29QHcDoFC1_3RwPW1OR3z3izprQzqlQKNgI6ph7uaod5jKswXLZFYCAaqe1rQjFF_0FqJw4En6nC5U4em0-YBCNHKS5ThdnPyax7OVLCkW66TiW0id7PKjWr9WXD65V3F74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری پزشک قلابی که با سرم بیهوشی وارد خانه‌ها می‌شد
🔹
پلیس پیشگیری تهران بزرگ: مردی که با معرفی خود به‌عنوان پزشک و با پوشش «ویتامین‌تراپی» وارد منازل شهروندان می‌شد و پس‌از بیهوش کردن قربانیان اموال باارزش آنان را به‌سرقت می‌برد، دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/458303" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d45ba451.mp4?token=HP6XoKx8PptfJ4935MHl39lNSGK2C1HSr3KYqpuYq8xZdi9EWOLfbWt025uTkLZ36xJk_gJJocD95EYAx6b77BSoR6W_oqyJWg6O3UJooRD-hdi25wwLTqPcGBcIUFCdOqVNHqUO6Xyexe3ZAEBgPuKJoDeRtCAlMYBAvLhBmjW04VhzQrnO1lq0Yts_sxI30XcZjdNLKd_GKusGgJwlmEuEJwoCMISDf7IKMf68R86HvrZ4dE69saEVvsQDzRmYb9UUdQqrdFQFoi9enwG7Bt_eJ4CRpWF5yRstuxYXRELwRF9YZ-Ys-UA4QOk0GGl03Muw6QimnYzFAYyT4QHxzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d45ba451.mp4?token=HP6XoKx8PptfJ4935MHl39lNSGK2C1HSr3KYqpuYq8xZdi9EWOLfbWt025uTkLZ36xJk_gJJocD95EYAx6b77BSoR6W_oqyJWg6O3UJooRD-hdi25wwLTqPcGBcIUFCdOqVNHqUO6Xyexe3ZAEBgPuKJoDeRtCAlMYBAvLhBmjW04VhzQrnO1lq0Yts_sxI30XcZjdNLKd_GKusGgJwlmEuEJwoCMISDf7IKMf68R86HvrZ4dE69saEVvsQDzRmYb9UUdQqrdFQFoi9enwG7Bt_eJ4CRpWF5yRstuxYXRELwRF9YZ-Ys-UA4QOk0GGl03Muw6QimnYzFAYyT4QHxzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت نفت: توییت‌های نفتی ترامپ خنده‌دار است!
🔹
توییت ترامپ در مورد احتمال پر شدن مخازن و ترکیدن خطوط نفتی کشور از نظر فنی و تخصصی خنده‌دار و خام و نپخته است.
🔹
مدیریت تولید و شبکۀ نفت کشور به‌طور کامل در اختیار متخصصان داخلی قرار دارد.  @Farsna…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/458302" target="_blank">📅 09:22 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
