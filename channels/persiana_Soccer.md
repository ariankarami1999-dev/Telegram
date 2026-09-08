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
<img src="https://cdn4.telesco.pe/file/Jiw9pe1vta3Gog8mIMz1nQVW0XegOH7KG_VvJzsP-GEQmcdKN-PyCwF1eZlxVBLUQkNwPNkKv-XGIuBKCdRd4L3fGyz1lvZTBYMEhmknE00td56WVSuMAxIG9MRWUEOmGkosGtQ7voKUqQDD269zyo3x6rIdpaWfO2InDF1vWIjrarr4tAvLVt5fHSLkdsab0g5Ia37psYObv3tBlm4xCBAp2tWs8CaQa_xqyfK0H7gbBymgPiOj6c3RjCwy1U_ddrVGfLyxyF7KH28VEYyk2vtXRQXbRNJA6NVcCBQS9egSbL1jcvDrUm61CUzHbg_F_ib40binEsXso8SwYUYwuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 567K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 02:34:10</div>
<hr>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h783phW4ZZZ5QLbAew2wB1vjinSN0tOGDOAEsJzBWuQ0G-n9jPBOiaWijrs5W9LkVfy8e1MALW_4AovuJpc_wYz6MhMD7SzW8VyUkv17pWAkzg3uUVYUgaCv_itrRaCIzQ2YWCahaFBF87b1NT5FRnviY7r6yX_F3HW22ViOIrEt23Ph7rd4ZFlsGtEfQhNBtRwueHyzn4PtrggpZUuuaCzgi6lI9E_A3Q9cqSZafGh5QkBiBndwU-_ArqZHwy6f919TLetRSKA61vKzeZaQJWM0qdzOII-gshxPWntckzEbyqXPJ9yyzKxxPnAbYLpsbVuFqxWC8RTsv8F8LJK0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJCim-h1z4QmxU9PRNgLXeMBlKuHLYhdvl_uvtBjTXP7YejcyFzdyfdVRQKHcXban33TtZrYVj5OV8IlnjcMYw0VNKNYlpR3LYvVYlqrYr-2hyVMMUSbqlfaV_gHoZvMMkDXNrQST4Kptj1IPllZuam3Jo3ag_Qx1-oRITbAgfYSn3PsAnXJx105EvB8B2vgdCnQ4__KcoqpDfqUyJt0C9ziuGfndq5VpmazgKK4EYgl_0-Gg2gkiXyrurk9AyVz0td2p4c231cWNCHek9Kl5mcV4xIHTRPAkjPWPeMs-Y5IJ_UU3uesdZA7bsqdPwV1Y4z57kLpFwySr0j6-9iPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2c4L9-9btVa_WAvUpowDUzOqshdTRWYlSsD_fAoAthcX2_nCVSQ5MZ72lM0dB8d1wseCiQRi2jVKNbPXRR2PdbtXi8aIsuogfxUBTUtzE9JfIwr2CauWAZTJhmIeHS01FJJzg27edvqfSy7Y5AhOet8PgqGNG63V3uwu6V1ohfRvAu4L4quYcG6rJpCISIoBr0Z5rmbQHrY_gHloScIpkjWrUMdWWmDFnOMp2GEv40QuPY6cN8IQ8zaP1W9u86IDiXp-I6iYEQUpI_aPFHUFy0a-Y13N2vfI9mS-gLuFOMHikmz5FNVf998mx-Kw2jvomxhc-qf1w2XbBj1jkpQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRPj_xMmmr0j3jK3PoDqPYK-EgRGkBga9kP4gWkfR5hBclZ7CErTTYtzM_SRem_DW1YmY0pYbLcVxFu6YTEpE8lKrKKZR7DhoZS9WZzCebLxOg2SMyakiiQaDkemz7a1Gu5IWXc6bZVUpzxm7uRrXs1_Q-_tKo8LvVIJGv0gcM6PBtn5xCm0DTGCqW2u_aHLwTJsIcbj94U9vbOUJzFa_Tlnli9Kb74Ttx8byBnI71EP-7-XbglLNanTcX162VZGSHrYsBepin5o5WcWRy1Xk3ggu35uEVwG3JBRE347Y3D6rF8fW5RP_6mramcfrG2BYKEk6WJoUdEgmZXNFdqUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIPi3Ot3WcnJPe3R6qwthnqFZesSgQhWqDuq1XVLzBaUk2ZDmCHcLkOgqouSE_znt9LDAK_GsMnyf4yhOkXm81j8WKYnPkoKkOxg53fqL6SGf0Qr0A7wEdhNZG9eNbdBwRj7LHQM4jtin5xace42X7tEDur-6Zg8iPF-OihIp3lvcYF0F2Vwx1rPMzyoMbIozHdhVG9VlcnbfSxVGboxKgQFOWKZKRydnHUbWQeTZYkR6CM6C7THqVAHJX27zm9af4us-vYFx3iLEXuT3Hi0qiHvvytE54tam8GZxaSmrtbExo8ByjmEyYs9qdTk-BVaS5RLl5rBrKQsQbnwAtBINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6ILYtxTDyveZ_ivrJEo4hJC5M-NSsrR9Qgea3D5BFPwXviFl7pBoSSMUyUZRJWO5PuAtyliAJ6YV7BMplDxCFMdaI_Bf1acf0sG-98pdeRHYojXbUDrQ1pgMx9Oqt_yV0Mt0sV_KJCHDYQoAkK4vLPkI2fjtm0mI0KYLnWopNscLq9tCBA7nKMlgvopKE1ryh_MBGFj1-yZMeHzHYc9c9NX3LtiYkCyYee9-C_ko8sp39ox1IEbS0ux53ja4XIvV8jFSZdVtTKXG1fM4Dj9a2xrHZiowZ-oBL1pOVywm47Upnpe2umVx6Ih4n8Ij6a3fKYblXdJ0yqgfCpR0SSsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odYA-oqOu3VSZ98wVP31XHnxfQK3YWYG5XJ2LQwDY4yO-vfSQDjiGmzH6Ie3zsMJ7kvxXyNWnI-b_k2lzNItq4z8dLSr-EMx3qDniWbNb2ng6PDD8qKE4vwXYP-ogVRiaCPBPEjdegz7a5z2qouL8E50K7Q43A9H_iEWB7IxWP-05j8p1mowvY5BnhF22Yi8xBg11XSqyvZQrqnw2IADE-MJVsLsFbZxatFarx7ify0j5H6gDPFhr_KpHgezmh971NcRacdz8iAlIvV52-2UUCOzikjDK3O-UlScApTMX-AK3qwr1zZNmMogCTvhYEOHU1u4GlFXzVPQsNnOQONpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuFe7n1tNbAvmNBxFHRaK2_PXvTLgQUqn5lf4f_zFVYYY4Q9pvg3eFas16SND3PaQNe2qwO4X6GQ4ku_ZfKpH5XG42PPbROQ91k_ZqshChZuQff4LTow3l2oHD03Bvr4SWR8K0LZTMAmMDz7aTVyI-tnrM0eKG8dBg9MMbQcHKWHBsTrtVtn1wvd6LnMHS2108Rv5iG7UhCfTJ5oi8kE3oRfDOPB92XU6ES-9TQJjArj0EW8YOfuQlUe4gukPv9UdJwZd-EWdI3vFiZUK8VDRtf7vxf0wKytaeHZ631X4dBcg8QBf451kMXG_U67BvSACXyMviIBV6W2NYQgwMPjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2_9-UBEb4pOar93vmvHfM7U5LtJUzRiQGK-gEVO9kSDEu0kPcMUa04Dl4xuAolrInUaVWS4CBm0eALjmKAJ94UcqdYz_QbRJaYyLcBdBKRHR37dwcPv0MDsy8cVz08VxV-pZdrK3DSM0WIi8TS2mhwOtD0zxLGnnYijxsoDzaJ63ci3uNm0BMlsr8kMwgen7zHlqLoN__eWE9xV_qM5l4FQ4R5GTyyb8BZTA9Dpq5-DPtpiI7v-Ak4Aa3HV0dJrJLmVVyy4qHO2tjLnenJzFAvVJ_Kh6dPKfteY3hYpLvwYPEEFK2xktWLjT2Tko-8qjXWkMpbu0VPgeUrIzj7xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtIVccgzJO7TFRneekJOQDZjjUmu0WdD90ToktTs-KDwbfj9EDco4QWSJ9a7BdeUiB1TaHzfLm0T8BcLO0fxzt-hP3wOzWp266pq3wmpSJvFn4qy-QwXq_KgJMIg8qSgnYWf0YCW8rcefKgrSZtdpE7Wv-kpwj8YCap8LwKKWzADXZM4hjSu4c5GhZDPYNQUQnyb_IIuA9ZuxPX486y-BOKfu2aPnKJ0zAvW_W1s6o71Q95VKtLZoFMFYAeWXYo8aUq7ejDp1y2lGMCHgFdISCtYb7vSxRYvrs0ffl3PmNzuwA18DczU25bNNXetBTBfcxxeDHRcFxTfbE5i6SDpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFibL4_wOkF9V30_VjIxA97niEN2Muj7T5yA06AGK6dNtfugfS30e8FFRmG-BfYHbHTQLFu24jE5IkxQmZyCJTxPd5OoztgSlycB1oSEk7bwmy9Pjg8D4GEx_GcWI59Xdjv02KrDsdBqL0HRlDqiiVCSMA9VnPLjRvd9u2wlMPSAs7QqlLOykgCpWKvsnumdf0PqJT8gQwnRxw8x2rfnQg-QfDlM_bddA4hzgUS_K_VbaWh_0ehyU4tlLpbSxUnT1dZEqPmCIAMZBVEiRtt09_77NUTLOaKBinTc-GIc1f2GUqr_5SFycTJMNNzUK_fXSi-OzM0kN6k_KAPYOOr2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWFqWcAPAvf5QU2D-MfIeZk1mt3fd4VRobLHFxeu9p5vcs6q2XDBD68438kjAZrk5BwRHwvIZLHHdso3VgVbQFI9R17nLM152f8R6DTEAMOqWRKWgBvB1F9NTH8gWPWY0QRePV9Ne0auSW6qsKvhCNDN5ADFVOFwdWYX5fltWwQeXKwfzgpkVI55Pr5BrhJtlPGIPJCo8fFT-A3u40AqAAPqZ49hk7cGxRMDpZ5MQKLBIf1xSK2eseVJTrQPdR9z9jb2nPvbR8qDwsdxE66biYO_x7_DS0-6NW5zw38IUEy3B5347YwwnEQj2tpbsDsRslJwq03w658MpoaG8uXLuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=Nfoau2PMfsHfOkf1SB81wWhaZAwnDaqwpqe1xSamGRpB8FL5vEsmAvOz1qTdT97airJlXIUDaCAdJZ_eg_GoqnlQMAeqV_n8w9l5sSnpBSdoYrl-GuNZB7nDLoGUyptdNfziuCI22rmqV1rjXKr20iooySxW_Ng1L_HzUdLrzTmxRSaFz6M2RlJK7_drdeDSmAfndBVul_huRdWiI-22UoG18qp5-OjDiYsErl2llAyJEUb8xvCs8RB9NwyNvOMg07vmY6TNbKWb-ro6J6ZDL6L1DHxXS9ik0zWUB629yxWh6Wb0ndupkyOh_YXRCN4dllwbvmHg-naty939SGthOBhXFeXtaM_aaQbR9OkmgeRXC6za-vImMLYg1_FT1Sn2tCQQ5Mo0Nh9qn9w5RkAGCxDeqFhJH1MA-gLhyXpmHU4qSUD39UYkOHpnfd-GPltdgMCLiJrIVnIrVUB7LzuWHI93peXn65iDuVeQ6pad5OoGVOprmKaLi2pEoFJKG5snfEWoiuDKxQnkqbNROg-c7ij7BAoOw_UUe7uxtsyORNvr0P669p_p2UmY1zdzGLQAPvUaCciA9VLI9MJEwQft4w-zRScKy_bCq28Y4PqvltoSkQngjKhGB9RsvHz40Wyk3c02Yy5yTlcbFzSQ1oq-dHQ3CKeKJzo0fiSZoRCMJ18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=Nfoau2PMfsHfOkf1SB81wWhaZAwnDaqwpqe1xSamGRpB8FL5vEsmAvOz1qTdT97airJlXIUDaCAdJZ_eg_GoqnlQMAeqV_n8w9l5sSnpBSdoYrl-GuNZB7nDLoGUyptdNfziuCI22rmqV1rjXKr20iooySxW_Ng1L_HzUdLrzTmxRSaFz6M2RlJK7_drdeDSmAfndBVul_huRdWiI-22UoG18qp5-OjDiYsErl2llAyJEUb8xvCs8RB9NwyNvOMg07vmY6TNbKWb-ro6J6ZDL6L1DHxXS9ik0zWUB629yxWh6Wb0ndupkyOh_YXRCN4dllwbvmHg-naty939SGthOBhXFeXtaM_aaQbR9OkmgeRXC6za-vImMLYg1_FT1Sn2tCQQ5Mo0Nh9qn9w5RkAGCxDeqFhJH1MA-gLhyXpmHU4qSUD39UYkOHpnfd-GPltdgMCLiJrIVnIrVUB7LzuWHI93peXn65iDuVeQ6pad5OoGVOprmKaLi2pEoFJKG5snfEWoiuDKxQnkqbNROg-c7ij7BAoOw_UUe7uxtsyORNvr0P669p_p2UmY1zdzGLQAPvUaCciA9VLI9MJEwQft4w-zRScKy_bCq28Y4PqvltoSkQngjKhGB9RsvHz40Wyk3c02Yy5yTlcbFzSQ1oq-dHQ3CKeKJzo0fiSZoRCMJ18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ay5NHYDZ8m69MAo2O1UxTNeA0JkyMBy4_yoAM8_9m4n9_Dh0d7tesJVZB86zngUwh_WzReNfpx1LMrI5fHu3j23pTdHkxJL2HovB9aQnfeTT2jglSZ0MurrOR-tYGZ9BJV3p3avyICY9ivFORmzkHGNyWJF85JX4Yfp97nsXuHJNd_Hn5XxGEGzS1dHbBzeBc5-moxgGZquR_gvMRVF1mVq0gyw-8Xr7AFxXCYX8o6ZQ4O7JnlwzG12yp_ajEFOV6CXKY7XGaPfshUernXCH04Qoyj8RdBWlxgdDXvH_BgNQV3eeNhi7EUykD616tXlh_hP9Cx7LbHtTIj4ODVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7emQnQv9SWOspBpziPT9Sku9V5zjhRTAyvihejg_hkyf-yJUWHt0HsEemgFGNhu_f7ETq-mHWjMG7HXFv1BoRZzjoJXCmJEeBRwLpMDsKw2-HaD7SrsGPzK4ORyAIOnsXlQsKSxTRr57ZX5WrbM9mHF5W1q363EV5d6D_-VsUvujs9Bo59bZ4y97ghFE0GctHHKjWM_CEa27-y9DfVd4gViub1ENcvSD4MbZUQsWTq4Mr--8zTYaWHtrxNlswsnD7HgIlNkbA1k4I0wuD6YqmKblaW1W51qFs-QGo_r0cXrMO21m5kNFILpH4rSvoC514bigTwkcC5tNeWlFLzF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR1_eRXY7W2GEExw1HHGfRP_Y2e9QJMMwDEZqInBD7tAL_OxY1vaHZRb2yNNySRVEFW22oXAEAjNKlGLaAUWVLTllHYnmIX5DTs5LD2Y1C62bbXmC5GMDRypj3v0Ksxi3onV4QJ87DkZwk9wA4TNELM8l0HnrXpGhuYwQxXDnDV06WYfVy2msQORvlNWCd82thGBDqcwIVdwxNVafVp4ZvxQs8Z7SYqdeR6e2VKw0hzaRqMO7tVf1Bauc_QVhWsfE97vk0w-f1HnegMsUhlj_1fp3EtZPazP3DMKA99MiEgOKLbYruYSu0Y4CinOpsMGe272C3L6Nw3MeH0btIcCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scAE8TZM7FwEcFEDe8_fD_M_zWUmiTbo2O43_qM88yAa6XN10uGAJUysEkTP9QTvrmFJm-IP8zNHbjl012dyEzoNyPSrRcaQ3Ebf5ekeNzrbw7Y22QazzGNYDNjLBHg4nfn9JilLVv7I3KZ1LtC29AY0Fm2F7nslN19sKL--lZ7qba5tClGy8zTtLQAdkj1jUzBUo_8w0oKpaH46DfzX_46N3lZpT_giPbqIrPWJ-r6gjjhCTMdtBPj3Zevpx8i3YDzikCBrYtxPvzEt00CCUX1GSinOTWy8rGH_JA77L5q_hGLeXWfTiO0ZY_r8gjZekXmPZAh6wkXYA8U3B-0-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BioZb-vyVR1ZUHejTYoY-SJ66f5UhLzgQS_77kaqhtWHKWQaPJ__vvUaTLaZrNiOFMNJcB35VMv4PsyjULjM2KRQYkNRxnY-7j33U2EqG-tWIU4i1t_-Dsr_uxW5yEsM5ITDN8lfA9r6CXJMzNZVGqIOUf_B_TdmkWkpfbQWjLdqv91ycSo457T5HSmlVtDk_7G2pkwpfXCTZgtgjTinJoUdUfTzKOrBo8RArHE2s-z60sRqKvAQv-UztGCHTzVbtfRnLkIb-UvwGBUpM3hDj0VMCSfZDliPtDAfViGNXVHGlIeCmUssF6D0NvXpxdDvxFam0X4wEc5f3oshuX9JHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3X-g5610QD6QJImhkIh6jC4XexvBJVu8_Iw1HsBMfdf69rJ0m5uCLZH4cbWekUp7eux8Edvl4YJyWYJq1Do4Qr8pg1SZFDRMXNBaSb9plhlRqggPTg1Wj5xgrwbUFlc_1ERsOdx3voVx_laqG7RDc1RhN1Ss49easOnvjGxVhbJF1dwoYga1NeNwx5oVP0bD3-BDqkzf4zK9ELmXMEiEAE12pDgWFtbE-QkpTYpWAYiWJuAxxBzeyDHbwpvsZVzX08HCPlKqw_xCClDJJmFoylMsVH1mfe6HkxutoQRxGHpRtLj1BcFLbkyfv3NCa70KORPblDxLTKgkmOnvh1-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkcBE9UPaNYjv0wa0GGPByGDfTYMS2EBDKVfdiCipfwwLSC9IV6caf6aOc0Z7-v1pwd5VEVwEVhaNaZYRkRLzDjJ8Y6WQS6wKvjPfbublg-3IKBcX8rjqHZqFsIQg1fiXtmfc8_F33d9vDYQzM1daBlaUtBLQ2m4VEFhA23lKh5jXgGAXi21vMaET62KdXAvq0QOrOO5l2lTQsh0Z-EeFLx7Dbb4RArz_33xoh81gN0lOOlCNLpCSgivpb-vuO1_tKYGebxw-Of-gCOPuhnkijJLQqgg3qjh0A61oOrvpYwl0n4-CJnGshQNPArbQOBnznzbjjicnrN9kdLx2WLmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4y2_gPVqVvapKJUKCxAUiS9myHcip5gXauIyJ1Be5ST-9IuiYU8qIXTWSRy9UMAht9MaAKM8Mg4vkMXXLuKJ04SVo8XY7SHNdhuj6AT3nKe8YgOGZIa1L8jKcqaV76mJYuEcwHWdRjDH4O4vups7AG4AfPivCuHzDaoM521dYbXn5q6mFfZf7MJLcGaFwg-U7anzSwqymv6LmLGt4l5s_Y_ZCRsv81dP8mN4Jrbwh0qo72glrLM4t9_DW3E-N_q3lk4murEUWrlhwogtFrvwWFFAqwuxkki3Drtuq_oamjWxuaeL0w5krBgqEmFle6x7QwE3TU4jMwE-ladRS7ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mhde4g5pG2-d69mPjtdGmbPZqB_j6OoWxtVCufQR3tSN-rM6EnqYIomuVSs01N07260sEYlsQWNub502MuiKNLY13JJuDQ-MBsbraCHe5wJF2FmHN7bpu1kdfLCeUVAHdgQ-OOHoBML6G8-bO6yySC1rueUt4VGDvPb-zfjqOJToIhmmUoLVl-PVyRTeeU_QSmrCFqgJkJjKoiLGZ1mKhs7B8qjImuQ8S5slW2X_rPNX6skiSjvxHIu_4kEeOYrJxkhdX3-unHO2qnFJAwDhx0SkKXyWw-DgB7dW_9K5LhLh207cJ7O3j7H2p24s9ssn5yPz7YAdI8fTGwUFudGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=GWLevFQxYXoyQQHwh5u1Gvdi6yD0IR1HV1U9JMr6WtVD6dprucslrmM93Ea8L0xDxKa5elzrlRROrLSTuUjcZkYONTbzkC2ImjmKyAFf2EOr99q5jRn-bKQGSrGQCoKB44WSwiUlySzCMr2fvZTz0OlPGAmxnklELUyVnFG6HyBxgCf2Hf8BxJOnGwMbjRX4GgV9-sMA-Qc-ObRxg5e6dVfoJ3rjpyRKbPaN3NMPlXSd3lfSpyAJrH2UAfHx7a4KjfG9iYx9NN9L-gjYnLqWvA_Q-hqEAJWkiDsqyf9SxUnX4c5l4vqwssac86UhOwonKrSwh_NpoHCj2EIPoffFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=GWLevFQxYXoyQQHwh5u1Gvdi6yD0IR1HV1U9JMr6WtVD6dprucslrmM93Ea8L0xDxKa5elzrlRROrLSTuUjcZkYONTbzkC2ImjmKyAFf2EOr99q5jRn-bKQGSrGQCoKB44WSwiUlySzCMr2fvZTz0OlPGAmxnklELUyVnFG6HyBxgCf2Hf8BxJOnGwMbjRX4GgV9-sMA-Qc-ObRxg5e6dVfoJ3rjpyRKbPaN3NMPlXSd3lfSpyAJrH2UAfHx7a4KjfG9iYx9NN9L-gjYnLqWvA_Q-hqEAJWkiDsqyf9SxUnX4c5l4vqwssac86UhOwonKrSwh_NpoHCj2EIPoffFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM2Qk4Nxjj1dHhMV5iDdyQU9e3vOdEWSsnZcuCHeCuM6USsS4lV3pLsURfwGZL1IZogi6czrWAfMVoYvrLbdnSHYEYln5LPazOrtGt0KiMlBgjZLNQD1aETWDUdEeXPW_UTXvipTmuG3Y8dARNuVjjQSykEBOg-BaRkzB4EtQvWcXIP2FVv9u8yeOH7HmGqnM40eChPIyY3QcG7z5XLGCKkA4_lvVDdoqTc4ozDg7RBwjWWZnkHwcCLRgtUZyNG1ShRQXgFUwggkJjmKNNmQZgDo8Wj2Ag2XfBmvTTD8zOUqnLfjJwKHnTOEpZEKkanBj7lV8-D6kytRaQqJFOy52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29320">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbhaUjhPE7VbI4ZNOco_IlqydzZ7j3kD9e-r-lI6SqW-1aN4XOOgCoRfw23w3z1aMOr45PA_Bz1iNuBvmeCQQWEd_Rkc2d9WBKzTAutFya5juVf0PIkVqmr6hsKFexz_kwS_f9wqg1TMVELnmd_NDy7myghITxPpnZK3b7qxkJ7Cz0takgJ8jEP_QikAhsBCvfcvBDovj0fwUq0vZRkTh1TqP7Gmh2MYePXiossbQFQ5yssQmEXcOkqiCIMcE10etSNZXlCZiQHRtBd2v88sVexDrutU6Ba1nwjVyhAaH3fyik7LTL2_z6TUPBtBwAeZSG0gBxmUJ9q3FRjXfTaQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
رئال مادرید
🆚
اینتر
🇮🇹
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29320" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-GKClWE6H0_LxjVA0z4NsIfTWt8i89tm8M5UPbofr-7DodvYD4sspXvhcPBdYX3iAd5xM43UElZKPBops3pHQ4k3WMsUx874jh8-W4koTBHA9FtSRuRxEFPru4nJDZXEdSJEX-XeYqF5bRiNQSnbKJQoUzUccdJjG3CrE-_4syR5mX99WM-VJ_0S1pmACWfg-qDcSDkpO4Lr69L6En0F_LOR2XO8isKko-cNbY6Mpyv724W7oHS69GLYHKOPyJ1nAZvXe0dOO20qfxr_TlT--zgcEmfgP5vQr3y1BVxYSX-Gw_E1d8dPxVWqa0aS_wuWSyD8DVp_j46Kvddhf2uxSIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-GKClWE6H0_LxjVA0z4NsIfTWt8i89tm8M5UPbofr-7DodvYD4sspXvhcPBdYX3iAd5xM43UElZKPBops3pHQ4k3WMsUx874jh8-W4koTBHA9FtSRuRxEFPru4nJDZXEdSJEX-XeYqF5bRiNQSnbKJQoUzUccdJjG3CrE-_4syR5mX99WM-VJ_0S1pmACWfg-qDcSDkpO4Lr69L6En0F_LOR2XO8isKko-cNbY6Mpyv724W7oHS69GLYHKOPyJ1nAZvXe0dOO20qfxr_TlT--zgcEmfgP5vQr3y1BVxYSX-Gw_E1d8dPxVWqa0aS_wuWSyD8DVp_j46Kvddhf2uxSIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9NNU98sb96YAb5n2_cy-eOKyQCf4cxagwZj9hoegtwcdFtG8i9fSAyIvgd5R7gGdSzAntAwRtyMWOy7WXP8TJ6iPueMOyEU5RP6zhrpKEXKWxa7nUf10WfRlus_xDbmu34aiK4lr62gkdxlpxuAehq0eOdMVbnrw2MPOTDFRnzikcLc1OKBi5Nvf6ctMbnphEIna2mVeLcHfsPmbkusNPEwHEJ35EC0pjYvnQiOZLcEOcnFS8hRkcYYYjwQRhhEaj7NoCM8gqE1FwL5dSIXhYvlmk4H6iYiximYq1qvwqUB4sTCjr3SqRuiLjNTKSrqs0GPD8lzKQRDZOXJnWOb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyACSrz4r00Hpk5c9vAJGiBMvXMfK5FbzbtBy3rV7cbyIUrpiXOZpMNQGoY8T-phaqFrgzA6qsrhsdo9skLiZ-52j8XIhxzwNWPj3UAVK7f7STdr9NJO4RgWCzvNub5S4rVvoEU9pdYTWg1N0wYeQ8uzPTyngtexVcjjPVFcEbsWRZrpubhfVAzI23XFvv6lg3TVcKVXvKNz_lZ45SKufXCVuyBnbjGFmhPy53eftGvNDjdch6oScn9drYmpOzEqh9f0Lg94iEyCkb2T-2JjUFaoj55DP8V4x7qAfE5Czvour6AhUIipANo_hJhXVQ86QVgfN40dPvhAZslvkrCQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=epgQa_OI4-atHwdyMBAWRWXZgzfcvnNs2azDeg2poDi4nmQhqg7P9FhoV9mhdADBYKSs0EilGqUzMDrFlWo4jh0CFeHrR8sr9VcvxN6W_59VH4Gn347tEw5tpXnDXGs4DIGOVtIjaCKi90ScJIyw-7WnDbTjOODvwNhOvV-wTS4iMy_dVF7dBLTP0vKgCc1v0oBWOHGpz4ALx9-JSukOWDpJt3dxnab2GjAEkYwLu-gKB4SKctysqlGinWyM7YNffTiRU2NxK4HfGNfaL1Gbes6vZu54xoL9-zjbFAzlkjrTgdIc0V4EFpfqAwF0EL_ooGFlo91m0Y-GW1WgZ5qJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=epgQa_OI4-atHwdyMBAWRWXZgzfcvnNs2azDeg2poDi4nmQhqg7P9FhoV9mhdADBYKSs0EilGqUzMDrFlWo4jh0CFeHrR8sr9VcvxN6W_59VH4Gn347tEw5tpXnDXGs4DIGOVtIjaCKi90ScJIyw-7WnDbTjOODvwNhOvV-wTS4iMy_dVF7dBLTP0vKgCc1v0oBWOHGpz4ALx9-JSukOWDpJt3dxnab2GjAEkYwLu-gKB4SKctysqlGinWyM7YNffTiRU2NxK4HfGNfaL1Gbes6vZu54xoL9-zjbFAzlkjrTgdIc0V4EFpfqAwF0EL_ooGFlo91m0Y-GW1WgZ5qJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=MgHcxvwMaT1JRJCmo2ublJwenHhFnMHGHpJB5siWx95BocXrHBFA07yNgsGwPupGM407dPk02L8ChfB_6QzNHfwpG5ZyyZXPgqWrNGEc1UGIYVHDsIpjdgReG-kyRLsGFje2cMmq8WdhERvOVD7nvK-Wz4cvUKBE53CHclqxHaNLOrRsPl3nkESO6XhfWC6BJyQaW6VHXnzrpQFKMyB4XTZcDr4F9xuO1hMU2j4fKgl05gDIk6MsgW_bua3Sy6PjO3odd--q000C0yoQEYL7N4VykHq0Ej9WSj4bJlkSMFx5ZA-V00TCbXkcHEtD2g8g624ze4s_p6_absgrqYZH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=MgHcxvwMaT1JRJCmo2ublJwenHhFnMHGHpJB5siWx95BocXrHBFA07yNgsGwPupGM407dPk02L8ChfB_6QzNHfwpG5ZyyZXPgqWrNGEc1UGIYVHDsIpjdgReG-kyRLsGFje2cMmq8WdhERvOVD7nvK-Wz4cvUKBE53CHclqxHaNLOrRsPl3nkESO6XhfWC6BJyQaW6VHXnzrpQFKMyB4XTZcDr4F9xuO1hMU2j4fKgl05gDIk6MsgW_bua3Sy6PjO3odd--q000C0yoQEYL7N4VykHq0Ej9WSj4bJlkSMFx5ZA-V00TCbXkcHEtD2g8g624ze4s_p6_absgrqYZH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6IOH2Cc7rrPcWS3qXpyphHgf5MaHrBAh2sh-vbTuXNM_drWiF3xfEG-A7isTN2_1QaYrNyKJAGE7kEUkoizVOWg3T2YUoXpKEgdSrCUBcc48OoxcrSJ3MYfOAz4_SGaoyOdw1s1WmDIR7hQR_UskuHxWbqArvL6c6Aoz8GKw1Hzn6n-2CrzsXuDcCeVxiAw6ghHp1aIPi9wQAKaJis0Y6ZlI3DeudGobYldJCp4LqrlOLhVvZq8k0dFfxZRU2yZKGYFemJmDZ9LF7IYMk7kzl4Iqhb1bptXKLmBk4OCSimzvgovQsirjSRccd_Hmw-yyKpD2a2w9W5ip8iWvrqJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMM6fq_YQttxFVlvM3fU_a8G1N-QCuaWxcthm6DyjAxvp1TKUTiBYdLVbKR6ubYi7zEbnPtrR0ILSRc5Q-8h39npe9-gl0UgeUqpiLqAfAjoaJdlgca-SFXgE89ArbLZkVY13dXhc-QC0I2j6DzJwWpE-AtCVR44x_7I9R0ebTJ77bK9TQq3z2BIZKTOYJADbLVPGeC57eZvrqGvWyBNRpiMMgHHphL-F83Q_quRaJS3N4fEuYv4mHe0X0OIOQwTCq9ys4D2KaO2BaCJ5fxXLBaKCYsOcK1diOxpzPZG_S0QWOJrlAgLVciawEmLwiy-9KXrgguBw_Uhqgf0Of09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6VLdFhfDGc1i958VuJ6Q7mn_RuEl-TD725_GNSYmNxSkW2c3kAuephZzSCwMg--jhVrjR9bDliRGNU3MI2livdj4tkBwVNBCSZUwHuFB7L27yTcUpAmI0E3oCJZZKyF8Ip2MbSQh7iKYI5jTtkE70tc7j8arnV4CzQX46MKZPlNdbWJu0q4dD2FUju9L4OEjZMgt2ht1TtXtL7Q5WmWPM12gVugFjRtkpy7WRzGA4TJr_luAcv2xTa6I7qcU4j6jm4DqYv8e9zbtoIUnZDrtZUT8l1Bt2hzJamUWedFThH8EIUMsoQP7qzbPqYzQHrQNSf0NMsoXYqr9j-ri4Mqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsN8uDVtr86Z5x4Td9np5Z4vGNhmDkzvySceeyssyF1xhyQIjBBZu5wNh_jSQT7dVr_QD_kWEy29LWmUVE58nZIj8MoIOncwuGg4-buKGTQTw53QYIEm4uYm7MSAOBiMRtv_vJ2sBUMsow4PGvi1E7slyZ8g9HSXQQmclit5psxlz_SU2HOWOySRrbx51fwJo6juw_kxX6jK7FLHsh1up7FcfiBR5fYPpLdyBfvfFhqK6V11PsPycOrsu8J7NJFkZIaxjlPAdCypHEXmc6JuDCTULQ-k4A7Fq46o5zcJp5anUT5_OM1Pklgx85gZRZKGp_1omkJTEfCLHfBIpQE77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEKWHPa5i9jQESUwwJoMU6Aj2N1GlIxJZgMNbXysJheBPqVIgXFsK4Nt2A6G-ceYWAWB0-ZW8QVLVrZnicboeVRlC8cRMHEww5kjbIz3P2UVC3-Q_1S-35wXkI-ayKyShSrsPbBx4xBzIM1GpuHEAdetUcSJuwyZjqiKtLBAskv__mCzbQe805YUz951VhWeiD2z_TdJcg9E7uy-MuuZ89f_zVwAeajfsYnIhUtEomfgJycut7BenyKwBHM42KWE3pxjpSLt1V3brYDq594jRcPU3y5ciLL77g7CG764D9CERTtaKsBx_YnG1RXMDI-8iy2WDBbMVbfv-E0nUmYMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roSzH-9DFb_k9j_3yljCBuOeagFIDIimh-n1UdWknKlY6QyAXwDlTndhJAS3f8gHHWPWQ2vyU47Ij6BldzsLBkSlc6Y1_zJLoEsslkFXK5UwE4QtWBe9B0PczhbzBD6wizMhspehw3Xr-1CwPBP6_tZG40poc4bA_Hpfwkpm5SnWRvaP0ZBRGkCyuqv007djPyxIZFe3qcv6QVpEZLnu4T9uR-MZwcO9x0IlpvBD8OtCIU8Y6iFNQhk4JIs-DZH5YXhhgz3urzCnQTyOdXfq61ExTDevjk9sWsb_4CqvLUf-VzwuTnd4XiEHSt1kHSFjYEUahqbHY6EQnSlg8v6h0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=BE-95HFxP5rTq-RcNM4i6uvAA7co-UmAmFSEVyENMYUAgbVQjatk5V0k3VQJwNzsz7vCP649N-3hxRhtWP_1LO_CItWaJKMjrI7xSX6-YLbkp-UUBqxd9M6B2Xvl6KJQbuVpflfyMmFET1VeXkk1RShCJXd9Fi5dcyubXDytEVu-ddOHfyWELQHzzEY8hZw3NJvOi2SHgNe5hNwHsmudYhrlZCsSeDlDWTO5LUEw3kgd50wZF2YWTfeS5WnOeSROcPQGp5EN5qMUe4BlvmmfDJ-UVuCYHnVNJCNRRndisU4WrVcEbHBCrNzcMWh9OZKFcan4lAndo-l7VtaocIYnvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=BE-95HFxP5rTq-RcNM4i6uvAA7co-UmAmFSEVyENMYUAgbVQjatk5V0k3VQJwNzsz7vCP649N-3hxRhtWP_1LO_CItWaJKMjrI7xSX6-YLbkp-UUBqxd9M6B2Xvl6KJQbuVpflfyMmFET1VeXkk1RShCJXd9Fi5dcyubXDytEVu-ddOHfyWELQHzzEY8hZw3NJvOi2SHgNe5hNwHsmudYhrlZCsSeDlDWTO5LUEw3kgd50wZF2YWTfeS5WnOeSROcPQGp5EN5qMUe4BlvmmfDJ-UVuCYHnVNJCNRRndisU4WrVcEbHBCrNzcMWh9OZKFcan4lAndo-l7VtaocIYnvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpvKCQFdl5lMRMYVMtS2QYHK5gG9muCDtwsFUnipwDCiqo1PndRZJSB0qdDCRRH3acHN_-LwqJpwjRk1Fy4sCZhEl2HGKMvWuydN7UHZXRnIaNMbLtS_0LI9_eFbreSikVhjsYQpF89N5c2jg5bAGsljMOhwsoGWPlDKw7UxmW4OciXkzuWA8cVl0iO9v-KntVUsxmru7ebtf7RwZLcpoK0xexLdX6jIkOm6Eh_fO-bDERRdk3XGtbepKlPI4X_AhcnrhrpHuHfd9BDChMSiIblCkNjjKrJiBgXTxPOqUqHxxEEyNgyVfg5xfsfTgS5EPEMVOnnqcNfvp6ysxJs25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxvLGBbl3f2SGItBdUguYm1JhW4fTd8ISwA45GRrqfZdMpae-vc2K1re3C513Q4kWQGrSmRFM560m0Ydl1pIFeLBtfEKZu09etrJ006tYlODvUKlfxi0nMWW02bkttT-7AZbnhs3wOMKgJewF0iDeJlH00ZYGuwtYlvnIocVNLXev6C-5ClNqUCObNazbAk3L4wnR87tpv_z1J09cGt2dkyCc91IYyEPbQIdcLlGNsbecB2SPvSIMPAQ9S40OSfj_SuMsDmYP2s6Cqwg2JbmlSk1WsCfcd3D0xXJ4xN-F4HQ4NOnCkfa3x4fuWmjD0_q3P9o6vkl7-hwYuOFKjemSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUcHhmP9yLywdW_KwwbX3M-X8f4AWsSnaJdclu0FQSfV_-6hhVUdat_6fHeoPbRl8f7lOXenYlJK_fZR9-P54fVwl4zuQ0W1-MYblMOXP3iGyos4aDgpiNoro8nXEkZNaieuZHXNd33EDSoet1yyOHYciQkui53qEhXsrrKPlnR_esQn5Nl1dYXsnQWUva0src6D_1YZyualmJ9AJgP8QaWXwkga1tNeAS1yjT8MGx9FjRKa1W18sPLJdQfhksTORSW54CogcY-Q20MLCWiTHJGw5NNnybA3wPiBEHT3WtbdBkx8yOniz1HrkhF7EoVtygTpo14NioZRX2C7wIctdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=coZpo_T74ERE9b2OSfeP31GgtDZtb6Kc4B90-uUMijowhXjnXXwD5FtXuKizKDxRYVklZiXKPXJZlY08xAmOqMRCR6ljdDq8OAFjIPOHiZqzZf0MqORsCCiCYthS-bkGE8TeolqQNwC_ysIaHxnI3_UesU6vctOcyWQjb9dUxM1rfwayS0bdW0ejhQXdeOP2cn2sW9Nzg2ZtF9_QKocVz-mum36aGw7tgL8VePeDSbetiqmr4qegorM2-fFXBP3X70VNE4QjrjZrZayzY1971pYxqqqySFD8z4qy_zbyd95sWYWnhm38dxl6nDpxLTn3NHD8oKm576eSZ3y5yEGkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=coZpo_T74ERE9b2OSfeP31GgtDZtb6Kc4B90-uUMijowhXjnXXwD5FtXuKizKDxRYVklZiXKPXJZlY08xAmOqMRCR6ljdDq8OAFjIPOHiZqzZf0MqORsCCiCYthS-bkGE8TeolqQNwC_ysIaHxnI3_UesU6vctOcyWQjb9dUxM1rfwayS0bdW0ejhQXdeOP2cn2sW9Nzg2ZtF9_QKocVz-mum36aGw7tgL8VePeDSbetiqmr4qegorM2-fFXBP3X70VNE4QjrjZrZayzY1971pYxqqqySFD8z4qy_zbyd95sWYWnhm38dxl6nDpxLTn3NHD8oKm576eSZ3y5yEGkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga9HmEkpfe2Q736h8fr5PAUXK6reJ6fGqhW_d3bGkcvXaK8SQEwE-Ds17buAtz9jknunbNRQwVEanyh9ZGHdNUmUEgdT12j__RplO6h-p9Y4IJScHi5UIGBjvcUEoAhWhLc_quqqObbBPXmCaqQ31obHZI8_7mvnF25cEpZ0diAiaU5CtVNpcrnxJQa5Wjg6GV2Bu6CiXn6lbyRu3R6pqVxiB_pJtYaRbQwj4HsO0DKKPKqqlmBFrizubhFxcf3KZdZMj_RK_gUniOYl40oKDuXSoY-u2tn7nkU8jxainWzQyDJScfjGFRvQ14BMZBNRvYS5HoyYq1hwT1-Mq-sZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awe7YXob988VLMjbEa3dxRQw16Z1TlH5zuWfvBaCY4xQhJbgUEc6tNXkELOdGh3O1JihYycI2koTkLPEmTuplp9onYksxHrbAre-LS2bQLdiycTXtr_rra6RMrUXfP_AXPxYz057w10vLTqINsM-uCoz_ItKSe5ekgNpxfCwn_xDVkxKCrzIKiTyyuP3RJNzNnsz2qTZ9hrzy2n7LzpGV9Lcd_sGM2davaWD71FndZ7NMkHC9qVb8TOPAyy7fy4sSHY5iGptsoJgVaTACJcCnVighbKdtz54KUANDHMr97lq5bJ1B8ksbCvmPwe1Ib1U80pY9SDjM40T1mqUwe47LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9OA2Zt8ukXnKl2kVGgULqSpYydhusQVgIEv15sAstYWYSz0MqKJqXITE_h4OcJ-OQwvwP9MzSiQvti4erxtecf9fqH3Aesa5YzeO1wqeasEyH8H1LiVFtG5Afsr_bAw_bMfBZW0ppwwn44_Wr6YKi2n8vZ2C2HOnTzguNnPmDL2jjz_SZSI_SAVk5unRUvO2f8XTWkLzvZE8NN0W_vpC9t6Ucc4dpOmi0sCTmyCOEjGWbo2ZJy7Z8tYkGmBq-HeOfikssqQhv-IE-iKswxckv-iF0-G9jD6443nXsf8F5msDa1YmvpkU8LjcPhDYexR2e3-z9YpArbaoqMaTJbSCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyyIE0oV7ATWAmqnYtGsiNRLz0HREuRvN2MsIhCEqGLFZYaQYzcXL0AbtLc7RpMYvV1FkFc570NKXplD_1KwuFrXzaPDZOJmL8bNso_ffHBEA0ch1dl1GOXGgsj8XguIhz4phmBMH_uBNUyDogtH5Ieo90AhQB325_qTcOWZDJajvztcrmDl6titcddvl-L09yecgqsiPIOtn3IfHicOMIGySrqUKdtJZnbW4j-Payr4TLBlyxGenmaf4L4zdbEi5yzfm8DLi0kAww3ISbA16C3ee_LZ8RrU9G68cOTVtsV_VAYtXkD8K9MZPq2cvpSX8MpY9hI4hqIUnL_bFTMwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArL3v39RmUia7_HJ6zzXVVZXtJmfDjFWNYmUmytFPzI7xaBfHRN1bDSdURhbD3eeaze9vxNEv1Ik3NAaBgV5TodM29swEVo_IQSHHXjMRFY4MSIEZTbi2imxihbSJmUADpcbapjfSOshjV7cxSP9VK9IeNtLyjN6eof4L2PCzPdNrWOrMQiw4u_nBf4zpnp4cYHB0uKkkM09Wm1xFzFhHKyE0_GgxmdVvNY-5JtPMhbcczQ0XOB5oeUFbf9szU7ieUTkmjRLziH1gVRegT3yc06-0RP2HAGZ9qFQZSc02K7asaZJNmiwau3-_ZAyoNAWX6xYGffOfYImV2xe0pqWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI1gdQkQIPpIER0BrRLWeFqC1pmRL_dPyOkvAEdkV2DFlEZE35NbZnrLjvLrI7fWYN31tnOCuGmq_sW7U6wKnGm5yp8o9-8oIEkyyQT7QWqDnUXXLI9ldh2-3ueiWGWThSJqe2oSH4ZhlOZlLATDxVXzVKC_Rnn78D9oKrQnKFgHRylrCyZiQEP7njk6mGk2MCtTyFpiPMcRdV__wjlzKK05klVijex_U9PMB8wsdXVDF_oSXzQbtwsXDUILemtLdbo8rQbl0GZu69Bb6_fFQcMqvR4bkZT7E4x51gZF5Cw2PHyTDzw1XdzqLGi1xZyjAeyENhx1qOYCm6WVeB0zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEjaZmwFBHX1p-MTiV5Cr1a1GhKFPxe6HplK5_PGR8E1xmIn-cgmbxDQ2fonoN0CBcebtBXyff3raqHUk9m7PRPoTBhKji6cumNGhZodjL-t4RqTez1JemgX9dBhd2SlESR8Xef5oUfXh04fHpO4lYQO0pTbr-XqoU6c3rcBoi6JSsYe64ScYEg9Uv0XAfZumXb5IA66zAGyEYbQqqclBGyMru40_uxmATCNpiVDuqv3AuDytD8bZmcwwXJLFV-rYTVFmvz6YWCLfQmiDCR35ncLovItW1vNkjyAykaDGSrpWi1zc38LcGjNRngWw0fGW9xJXYvMxexSap9iDam0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUdaTCvD-7nqnWa6GO3qCzyHQFgbJiiKtmhBzTztP59zo8Jn65qEKMwyFxgnGndYI8dOkVvFEoxS5aDVfPd41n0Wr4RRG9TvNc9w1gi8O92YgS3lnbFEYyjuBny00zVD6oPNdcr8fUBg9JzsbO26RRLWHp1zRYox-lxqRKz6cSBMPNvLKSz4wGwDICcrcPv8bG0peDCjRXa4iWtD5Y4t3WVRobZ5gRTfWS44qqF9YHnx7byx0IO5HV8qpyG__O1-tzIzn9jNuwFwE938gncdsS6geMyT1VOPgnOa7qa22CvtpqCSVR1AeiGz1RWEnZhEKJh4YfMWvgK7zFicDNlmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_HdiNt26Yn-I1c0cqhU9YQa1yadTP6nR1Y3L7iXG5sMKk6XSz_mnQWMUBfu0bWs65Iq-KMoapGVUu-rrE2cTVQORwhwKLvGP4F3t8Ijbz4TcqE9yszOXex-vD_eX0Vp4lRwr9710RSZcWVy8z2SgYTJBib3eNxWy8ZWROy6IvsJvohHhCw5W6EWdiQh6W41t1HuwhgvMZv01Uwmvbe2BDhsq5bxpRwR7WmWdV2wr4UKmRs9DbPqHu1NxhzDgZ6YgCGKE12o0jIRfEH1sMRdUJuzoVLhtwwxYb1Nf8iBDxxGeCyT8VIi4oI9mRVXxkv2GSlDcZxadNzDGbKDuame-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGHge9v6PpQDyL2LFZoNJTGpphZVoH4OaYRJI_WdhZy27VhdtAfoN4E8C204Qhk3IAb3X09L23VqwhQYBpdLW2PD8IphdY183gnOAMxCN_eKUqyexvIvBTPfYRvORuNliIhGQOiIuXkZXQ915RBy2wgviULRh1y_Bsuxs8Z2knpSOta5-pZMm9xrBDfBBa6Y29gXUW0q7-UBTq4w9a961AvoAJAJ599NKvHW9mvI-5ElTFiMD4FVnpYJIMQkC0Bb7aS49_1okcjMPN7smceDog2h7CBLqvcYLXlrHqapmBNNliu5-T7JXOygP1OZO6pXD2LGxxxKN62ewCXslo65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxBbQfGnHtFxcGOya9Oi409JI95cMUWJNS71PQ_KJFIP2PbpxjoWjaRXsM3kJUIvNBLRCqIsVcdAoI131MWUo-gAJxVgAdekrjG2PH8UOyrIpw7EglafPSP10rFY6aDkZ7QZkew_BJkOhKrBc5_kytdVZxtrhyWUi-FkP10X-8H4cv7BY756kSeHbTBArfQ1rjHqpe72YlEjONhy62bOzdT_WrQKMuOy5TRcjeZ1K10QpxHCVWcmqXqv7aRea54-ZOt-4k_fOvl10h5HVeyYbOlcFlcBdxrmQWP1zugM1A4zXty83M3Yt58A04nb27z_LSuyXUta9APpidjy4bgKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8J9eK_zW3jYyQp3U3mPQPwkBwWgqb32t6jdQSUesAiq264zJ3PNQf5VYS0F5bu5H6p0ef37ko5XDkoqErOmFWBIydo0O09BI71QDVSIs163ZHECwPpr75PwoI8nWB5N0MYEIp2yGvugNYZXK6OLZuAFmi5hHVxSKHHOieLhIrFk28PyBigP2FziEVP1k8tfky79FsnNv4kDvC87AfPKRGx_puUXUWUydiuyayqAsFC1sake68zzq1CFSf79S7LLIEP3xwkJby8On0yQ6CABqclprxrg1XwvtBFpzdSjaQHfufxliHAACqUG9GLDTr9e1I9lrAZQDrpDwVRJCdbDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO3kpZhKg-3to6qFnY6vROioTkMoiWaW7X1sSzQqgZYRrYKqYota0Gribsqp2jgS7Abj7BHAGE4bnmrfvlVRq7fjF4sgfHaeAPy2a-Ymt-vVSlTeQRob2CYtawuPx4LUVvWne09sc7E3897xaInzYKcnxTV5eijn4CcN51ikjQ2gjGw7XR4cWptQeAMgHtXcKZDaZ_h5hxqNp3BNI71IPXFRDDqAIyp7ml1z0qvdBA4IgyppLboS166mvZcP9_WW9x6_YTGlw6a9rGTLmZn_PNRyAzK3HoI18cYCccDW00X9mG2efxm_jjWWF9JtOowaoZC9gJ1btxiovxZ8biXRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOdd1BcOPyfTOUaJGVlUhXwZIHRTk377nSkEQZDqlQAzNKnpnZShXbYwr3buS6uYgLQ3kYoQNEjZUIuouvUxC2wD_uitakXHyXe3UAGUV6-JssMqAyjmq8aQGUkL9JlUKGYSA6vqEiapUWi2SQFOmdjGHr89lXjtN2jouqRyY0YjSoPmOUP6jazzXvtiYwP_R2H5fRGg9K8Dt99RdflNnMnOEKlbHyfaVLv1LGWiNI1amZxd-v7TB5vYtSzW2Nr2GSFewvCdrllLD5RQUupPrYU4oyGETdMKa-Znl3lIJB5HCucQOZBcKenP4so3lDA8bMtf-ljWY7whQZtYJ-H6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-ksnkc-iYAWiCQv2GWtVFUUDS62HhC6AuvKyTHAFvX4JNgeqA0xIuFOrTtQ1cMrVNqjkw5MNnPytXRu1pqM8wGxuWOyX0g2uoVP4IV0PWtTzH4t-chYazPXgqvJRyAkRaAEnjeKnhQA750mKC43BCusGPxXjAgZQs6EeVph5h8lAp02FJgmE-xP4aODcoZC_rKhh2LNzQtynPYudkMNgGvmxECFzISMJoMpuSL5W0go-ty5dC1dKSHHr-3sHmIQEBb6FarmoUwYLieHPSauRtnyxYX56YFPNpvqNIPWZDXu-b3SNPrZWUBgYeGKixJLOunKAMMeGzv4pKlW5Cgexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=b94Qxj2ZPhIdNLOvRikHtGQli03DLPCIQrermNjgr1JvasVw4K_HG1uD9e3LrqoPDMIMsBPIn7wUrwzm2VRaklHsdovsGWmD8axfdTIJ3c4rBkPovCKbRY-zorkATmf5tyz9vwnXcpeR8_e9F1-9xQgx5YXEycNM374Dg8a0dARcgNb_JEu_GOQAsbdlL5RCoIgk0VnmMdF74PwJ_7r3srOwrIG5IavlWseDWXmgglC0Vuf65qRpm99Snza5pGmCDrxiHShaVf0OcPGSE_ePlKywvt4o4fIYJy5cKLIMO_h81opteONhxN2hprpuGhkwAT2vhyAyw9rCJkEYTYPJog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=b94Qxj2ZPhIdNLOvRikHtGQli03DLPCIQrermNjgr1JvasVw4K_HG1uD9e3LrqoPDMIMsBPIn7wUrwzm2VRaklHsdovsGWmD8axfdTIJ3c4rBkPovCKbRY-zorkATmf5tyz9vwnXcpeR8_e9F1-9xQgx5YXEycNM374Dg8a0dARcgNb_JEu_GOQAsbdlL5RCoIgk0VnmMdF74PwJ_7r3srOwrIG5IavlWseDWXmgglC0Vuf65qRpm99Snza5pGmCDrxiHShaVf0OcPGSE_ePlKywvt4o4fIYJy5cKLIMO_h81opteONhxN2hprpuGhkwAT2vhyAyw9rCJkEYTYPJog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=VFtlcVrNugdmM1ZrbL5qciEoXppwLDYnUAxYV8y4rNpmKJHZua2RZC8Uamr9JtuShScfMF22vP2wGVQvY5AZB_98sg6Ku-jgdgFjszwtJ2mpF4yGZVILa_Gg0clgm2EjrPxp2utsf8Mvdqh3rzM3zfKs-6r2c8ackY7W9Ckedcs4FnzK-KNj3O3ppQLOziXrHGy6_XhnK6YDggERw0i-uImpEv4ahq-jd0ip7GXPff4RDqqYaTruD0HhtT-i9-72tzV2bCdnBdYHcv9jttHHjxl5htIsuGi6BptZCzeqFlo71iHweuwUMdnfPLLAWF50LQRETFPddPv9AkziZD_CvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=VFtlcVrNugdmM1ZrbL5qciEoXppwLDYnUAxYV8y4rNpmKJHZua2RZC8Uamr9JtuShScfMF22vP2wGVQvY5AZB_98sg6Ku-jgdgFjszwtJ2mpF4yGZVILa_Gg0clgm2EjrPxp2utsf8Mvdqh3rzM3zfKs-6r2c8ackY7W9Ckedcs4FnzK-KNj3O3ppQLOziXrHGy6_XhnK6YDggERw0i-uImpEv4ahq-jd0ip7GXPff4RDqqYaTruD0HhtT-i9-72tzV2bCdnBdYHcv9jttHHjxl5htIsuGi6BptZCzeqFlo71iHweuwUMdnfPLLAWF50LQRETFPddPv9AkziZD_CvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=cFdJQhGjTtm74xDOJEvg6FKLfEh-bw6bAAKkfw-Wpe7T7ZDq576SXqo5RKB0Ln9EFDEYU_2gCvlGgcwDn34NKg55DWKkWvDGVQuxDX8AibXPR1iruZbpgzfuN7iTVFyp6-vTXVQplTB9gOhSYLoPgr0RK_wBgQvB0y27oNrRNn0ShgOfie5eK_aEUJBOI3wSLs_2-WT08n3OJJwtLskHjd5Ebfh2KgYavkqX3nK912pEdvZXi1-P0tkXDkFGb3gJY3PC3vU8Px1PNuL2Teo6FcmDYa9OnXY7frCir3ZJLsVClyw3lpJPdIHLFqTSGUrip07KSZNEprQ1SnguzzExaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=cFdJQhGjTtm74xDOJEvg6FKLfEh-bw6bAAKkfw-Wpe7T7ZDq576SXqo5RKB0Ln9EFDEYU_2gCvlGgcwDn34NKg55DWKkWvDGVQuxDX8AibXPR1iruZbpgzfuN7iTVFyp6-vTXVQplTB9gOhSYLoPgr0RK_wBgQvB0y27oNrRNn0ShgOfie5eK_aEUJBOI3wSLs_2-WT08n3OJJwtLskHjd5Ebfh2KgYavkqX3nK912pEdvZXi1-P0tkXDkFGb3gJY3PC3vU8Px1PNuL2Teo6FcmDYa9OnXY7frCir3ZJLsVClyw3lpJPdIHLFqTSGUrip07KSZNEprQ1SnguzzExaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aap-dUCzxVbl1lyOXUri2-NNsze7BumPo6qS96_jero8cN1BTWewH1sPoHFoYUAIAjXIeUMtqH0KaTwjuakc28CstPo_4K4gLI8Rl8D6uHEOh3SwGH7S6TKP1gAaIxj2NzV7gI0odXipoMyCpIZ8kK45FqhacHQFrT4kxf4Iq_POdQdDqyE0iBTSk8MxaCZOT-RElRhEbpXlHTk0qWhG-6BKp1xf_i1QXjrO6Q7WClE0PGwQCPbXFk3wlsIqHuOeXomV35ImB5pHVcCXdCAsglbABQKHR0lPppLZ0XLIi0nvzldYbBf-lYzXU2Sqdh6XkN07lFmLhXwqVIyMS0vCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEqggNQGkIi-q32Q9xEJZIYzjRjNEya2EB4FEyaMC-sYKQk7kki88H4YZEHIvMYx24Ab1JZf9CcDZlMIr3-7pIgnj4oroWqrc8koLVYwBQxtX4-kuYKjhj0YwNLm4nxsNABdovgQr7W7t6tU4P_nT25ALX1Tqa9wtcO5C4OevX1Cv0u-BSEjESTBrEOY2XPRJAov5s8bqiL9KwiAXloIWTL5n5SZ60IU7UpVjAT3ZBw8fBHK081KPaZdViTBpyKcx7Pjmkiiirascd5RqgK7UKVzBA2V-tmvMracooPeeLggFHdRHyvzGMumTO3kxU27ewH5E0pnrALkXKTd-CFwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLQcbIkpnBVLwnhT7qohjk5LBSIBEBjbo__NnNqtiFT1pel0BS66eUbLUcqDV9POTmmjS7ldEOQlvnuWpeWicbr4SX7Zem1RP6ofb09HUKM4G3zoX_5FAvZXhuOjzKQs1GxCzeHi4z2ykcft69Jq58DASgcqRhjqviUesPLGtJmXUBCav0t56b3-iCfd9KA5uFJNru6ZhbXoTl1cTF8dLynU0tV7IzdN1rMzMrJOD-CtuWcrPynugI_4DV4pwCf6l9jeCTD8MoKY-1l0sbhb5rPKPk-AxhgCs43vEd0Q6xFVTdfUExfeQrPbawLjykaYM3b1JcwDDo-xuZhlI2moyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=mfRqPe-8KQ68kN4w66p1tMQwznn_lZbxqAT_NH1bYibKZuYPVrdHI0zAK9yWSEPHerx8Ug8E7pSDME0S_AWy_lRz6Pjxp2tKKC7hg5ctnnvAUY9ybIJvpdzi2e0F0LUE1ntP3H6YL2cZH-Q9snKVkiaHO9xbEioGmloqhRoNkKtHfwOmjnCCqpFLnmNZKqLKqcTxtU-Xee_YKSo5K0DOdbOqWzjw4SNQ4RzIXdFVZQ2jKrhCVtk6CgX0U2g8ONeZADVnRJTscSB_ns1BWVzfLpbXy36H3S40_hsHRVmIgg0Q3PGMkTFtoFD2vLUr5iNgiVTvTUioUL-O2LJCL9qxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=mfRqPe-8KQ68kN4w66p1tMQwznn_lZbxqAT_NH1bYibKZuYPVrdHI0zAK9yWSEPHerx8Ug8E7pSDME0S_AWy_lRz6Pjxp2tKKC7hg5ctnnvAUY9ybIJvpdzi2e0F0LUE1ntP3H6YL2cZH-Q9snKVkiaHO9xbEioGmloqhRoNkKtHfwOmjnCCqpFLnmNZKqLKqcTxtU-Xee_YKSo5K0DOdbOqWzjw4SNQ4RzIXdFVZQ2jKrhCVtk6CgX0U2g8ONeZADVnRJTscSB_ns1BWVzfLpbXy36H3S40_hsHRVmIgg0Q3PGMkTFtoFD2vLUr5iNgiVTvTUioUL-O2LJCL9qxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=VWhx2drzKPNyf8NFcsYrWrlMkpJaTGGTAizmGBqOUe2QLYNl8BtLDY26lGV3NAqdNTxpzalbWYwUULxMIvTNIZqOyE92WmmZPGPzdrDv7qbmLESRAKAlYTw-3zvs3rl7UbGeGAtSJ2hjCLxYcbKgSVD8p7_UzmDJgpTnSZuPgwtXfrpe_UMBEPdY2fpluf92rwq7Ixv6ks2s66Bw6Yb2qwmhB-xA_AjojwC7QDkTOPEhmVU6Rnls7UEgoaGiHcTRGaPcOnd9KFGqnzr-Xr5a32WpK42Pekj-bNmSpdul0cSjvwqXmuGkvcC9AZSglXk5MnoNvFOu8V3mMCgjLQU8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=VWhx2drzKPNyf8NFcsYrWrlMkpJaTGGTAizmGBqOUe2QLYNl8BtLDY26lGV3NAqdNTxpzalbWYwUULxMIvTNIZqOyE92WmmZPGPzdrDv7qbmLESRAKAlYTw-3zvs3rl7UbGeGAtSJ2hjCLxYcbKgSVD8p7_UzmDJgpTnSZuPgwtXfrpe_UMBEPdY2fpluf92rwq7Ixv6ks2s66Bw6Yb2qwmhB-xA_AjojwC7QDkTOPEhmVU6Rnls7UEgoaGiHcTRGaPcOnd9KFGqnzr-Xr5a32WpK42Pekj-bNmSpdul0cSjvwqXmuGkvcC9AZSglXk5MnoNvFOu8V3mMCgjLQU8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyBTp7SFYKLYLTyFqw_LWJCRFPZJ1aAqUQ5iZEVTwX5p_HZMZHg8LmwAT-5NuThNqDQlFqHKvjCIEkt0cm-Vcsi7En0Qp5UGMWatr56Tl7ev9buL3YCF4qAg8eiTURqMLoFNlfrXzDOJu1aYMDVzHSVFbPt5F58blT3eBtLyZsstuPKi2gJGLRNa7jrxG6ucNKsFxjXf3h6kKfBdikASFcLCjF9jbewcOj_d7pXMzmZSZEhSPpcQ7JYW3z0mPPCT-7YoheWuVxnDxiMPcZJs0tlmfl5nrO0nc3UDiR2_TDqzM2xzXkixMfy0HNvmlD_WngH6H1zlcbo6tT0rEgdwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNDsQ727cbDVY_mfvEUZfiePt7rdC4QW2y-I9quVuw41s0ZMBPiQGJpOE-eHzWwrEqEI2KPtQDXeTEfdqMWuhcUapa2zeyIsGQc6-ZEks_7sMA6gPGl2FxHmGR2OYBNvgubg7GfaB0luwhTVl2kNdSbrICgyahXLoI65HuuBWjty8WDrpDvLpdRqIG3J30LTYsR_06Nfq2I7ezPryDvub-UzF2JqOnRRupsC2PhhbkY2BR9xiOqJlHMEHuTNj3Un9-mLfQm-uL1bbl4CmgQeGLw103QdOHBC7s8sMFtm4z9xX5tIx5E8sOGoy_WrQRSfoGOx5xjGx0xWzYuXl2BdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sj2GK0qfwxfbu0-mYsBIepRZ-Z21kveQiNYhPKpK-0hKVIyMmpzw2c06mb8yGSqqJymH1vzQajmZCBRHLMXZvMRK6YBeXO0eAqJ8aEHGva_eafoEP2kJ9yy4OLwai09a4ai_19_4ihZ1Lgzcg3_GtQ46YaytxoGkx9ebnFjCLck12TCvWCM2e_rPcGA1ZBPDeztOPbtBv1syFOsauPltOntD-nW2aZ405Aaapt2-K1Owj9aZ1mDla4SXlq2LPZxAHR7SrvnjqtR3hR8P0o3FpQvVosKOw_ERItEHkV7dhVhd-NrBFvvtBeZEOawd0lZtWBBZZC9ee9DbAQROHEm2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiTp7yclwzWcX5EaTMFo5moHxpdoIaKejlv58N6JdhAsT8viCJn-9qmX1V_qcM4SzWhTyci2RuVs7Q4GOPe3f_1gKj6RdLN_4zivqgionjHPn5PNJwc-mpzc4cNMSdoqavZPWcUcrByNQQto25Ch73slPaz_6l4L87T8q-dTy5L7GJw3Q34NiSgTfeCh4q3MqDDdWmvpoI0ZSljVrh_I_EnIcxLLzrTnybcRJhuYnpvMfZTy52UojN_4ru91IjfsYmtHmAeSmZ-H8KSwfqfiY-UGod1Movn8s6JYd7DOgC7EhgDjTfVUlybtw7YuNYmZbNerP2F4qOr21re_gSLFqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFLr9vlOnVilXX8UxZnWK6iwZGNEHEkHHfV_w-gMcjHntAmAOt1Mu65Z_wjHiNe6ctWbAX-yx-IDZ4xr__Zl-_6Kd_qaRAo3odH4TLsMPeW0qTvyZJvA9UpuT8p8lpR4EQDYIYDKBT8lOuJ6_nbaQoRi66dpbtuYJ9wNBHaIHlp-DEYTEB45V_Bxiy6uOOmykpEb5OCVyXSlmPAjs1eorbToAaMaAsx44rf1jxoSkrHnwdMoI69RxWzTo8bPHlLn-IEDY3q7LraJCdagP_gg4dKJtXYxjrbbwq6XYlcKB-kzAGdM3o3M-_BSHxoePVvKMTiJcWlIDaiUCBJKeJqdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6TxSUL-l04wEPB1YuyGu4ZUHKK2vJQnYKtNtQKc6mk5OpmlrAT1m3CqZZ98t8UYwXFzBs_vPEIYHpmYbiRj82hCB13xyW2sKtmtwjhydM0d-7jp6JLKh8W8f4SoIq_Hd30wrtefDps3F-IFeqH7kNWAbykBPIAmdY7c407SR0OUd7Zn4OvGNSj-zWY95U60tel58AVYLblR217d1zIWUWW9IDwC7_--4-MY_sIqVActEmtjUPfu6CqnLShN4xP-s5kle38cgeFf9efRfVkt5FQXuU5BeboGaA9o1TxsL3TuK1Pig9QWAMyilb2U-H3AX5hCaX8qm2k8flOaD3AuVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=mJ8-WZazo7FsMtD64K_tf8E69X5jDOwuMmsuqSsXhF8l69_h5BCXPo14Nl99St1TTiydAQ_2OZLiX4OHN60RYCHn1BeJvz_MnfJW-2O4TIa8UR3vZKLikn18qEVu8FdNu1xzq0I6TfL5ob1MEYFaLaGvuyJQW3k0mwTZI_2lSyAljo_PiinB4Yw5esZ7wpiETfd6ieZjTP4yVrmPh8YguqewAiNV1ZwRZmx7_XOVR7JWKUu8Az5APQ4bMRuU3syQ-7fSaRTyRShrN7KmUOW7dv-g_hv20vSEcvMNaoEri4H9clxQNz6CuI2HnFz5AfzFm6Si54u5RFywjD8Qn9n9jLUkdqxPGZN6NNIdByYk9xeX1sKXvGaiq6FTGaQZbLqvmOC82nMwj8Kbp8KfJVdaZXZMT8Zm9gVQuOF1ue6iLbNT1n_js5vGSSGsk9uQ4la7dNXBAHLFJFSVU_9Liko-RG1XNSJUQELcouQ40uWfcBirWx4v7q3qk1SOJZirjpjm3KMBSOWIzEY7hl9n33H6Qp3kWOPj-VrNvHYtemq2if1oky-vWphf0H9W00rGxviK5RODkVh4yBdKQ9rnYa7NZ_Mv_9jiqloWUTmayJASyWipI3BDvzDmVnvxv2XJjak_R3aXtAT8URpHRpBgi7zlLetuJH9O0Di-MiVW44X9bnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=mJ8-WZazo7FsMtD64K_tf8E69X5jDOwuMmsuqSsXhF8l69_h5BCXPo14Nl99St1TTiydAQ_2OZLiX4OHN60RYCHn1BeJvz_MnfJW-2O4TIa8UR3vZKLikn18qEVu8FdNu1xzq0I6TfL5ob1MEYFaLaGvuyJQW3k0mwTZI_2lSyAljo_PiinB4Yw5esZ7wpiETfd6ieZjTP4yVrmPh8YguqewAiNV1ZwRZmx7_XOVR7JWKUu8Az5APQ4bMRuU3syQ-7fSaRTyRShrN7KmUOW7dv-g_hv20vSEcvMNaoEri4H9clxQNz6CuI2HnFz5AfzFm6Si54u5RFywjD8Qn9n9jLUkdqxPGZN6NNIdByYk9xeX1sKXvGaiq6FTGaQZbLqvmOC82nMwj8Kbp8KfJVdaZXZMT8Zm9gVQuOF1ue6iLbNT1n_js5vGSSGsk9uQ4la7dNXBAHLFJFSVU_9Liko-RG1XNSJUQELcouQ40uWfcBirWx4v7q3qk1SOJZirjpjm3KMBSOWIzEY7hl9n33H6Qp3kWOPj-VrNvHYtemq2if1oky-vWphf0H9W00rGxviK5RODkVh4yBdKQ9rnYa7NZ_Mv_9jiqloWUTmayJASyWipI3BDvzDmVnvxv2XJjak_R3aXtAT8URpHRpBgi7zlLetuJH9O0Di-MiVW44X9bnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWslKsndiHubUneuSYl9uk34cT2GYvxxDXgnQ33XuQc1atdcC8y7MVgDzKmxMGvnwGpUB2-2f1R6tFcyWGoZgE2PQOdXB4G71fzdgg-hK8kRYcugr0rHyRUpjitsyeB3hm7TLWhkIc4yeylG2e-fCTxRrXZZcK0c8BMQft7UeIf67gk1yEXSvVmIBRr0Ds1pTdmuQp5yVRqRAhqE5ZIdHYfSpNpSkhExrnTkRa9qqnIsHWgOqL4NhAd9DGPSDs7X8qLTmnmZ6495j7UIJGB_Yw_bb7SYvtSDSoi_poJMJYfnjw0RHZ_iEBUf9NOyXtntN7UXLKLdPQNupKHVW6ylzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgFZFcAKumDAJDGdMPslGbGxrNc4I1vKKFcMbuKiq0w8bnEFdy7nympbIFY-OScaNm0cMjkXWcp5R8RLu9ZXLIPYhIbveTPEmOGanPsacsNOvjMke0hOda17edNBhyQ6zOBEfmJDihv2JvB2rIgBhR52NfjvZGCeWolq3lsg-L8SOb8j1VuHOyIPtrWMNbuuOtceTR-5NNMxfO7_RkeVLpoYFoOwOLhKKXG6mPcWmlP4AN-pVX9NA5IwBikqHnBulUKvl3qPnzcEfEnjp3c0BCedUwXHPwovRLxaoYwCF7ZGsUbNEJpdZIGV8bAWCfk8VkfcMhnJbizcd4gHbtMQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=PRK8nbvBVp48XIuefPaoYLggkyJJSGaGNG7mKc-VRn4c-R5gU-x2TkbtvgqeD3igsWbGVTxgAfpEWEjmoMsF6aLzfc6R3KZeKFVHrw2EKUuActN8e3WEpKAR_dnA9VZNjG8ZYvncAzsNa99qFDZPcsYNwTbREVkGgDEqqo8SO4sYUKg1AOM6is1GM7ZjYj2AulZB9CjFvwIYnsAS9T_F3XuVHLo6SqXZTq--f_ujXNe72KTl-KgaWIP4-UVe3NLoJdaci9nsfVO5q2uvYktVJ9TZWkDO2jv31X7VLzHbaPfPbgvmuW8LSMArMGFBMjy02PhfDvVT85VPYSkGWdgskA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=PRK8nbvBVp48XIuefPaoYLggkyJJSGaGNG7mKc-VRn4c-R5gU-x2TkbtvgqeD3igsWbGVTxgAfpEWEjmoMsF6aLzfc6R3KZeKFVHrw2EKUuActN8e3WEpKAR_dnA9VZNjG8ZYvncAzsNa99qFDZPcsYNwTbREVkGgDEqqo8SO4sYUKg1AOM6is1GM7ZjYj2AulZB9CjFvwIYnsAS9T_F3XuVHLo6SqXZTq--f_ujXNe72KTl-KgaWIP4-UVe3NLoJdaci9nsfVO5q2uvYktVJ9TZWkDO2jv31X7VLzHbaPfPbgvmuW8LSMArMGFBMjy02PhfDvVT85VPYSkGWdgskA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M83I3TS5EiIsL34eHT8nvxznwo4cwTgL_DeBC6Q607saYQSsVsLr7CbMLikDNQ4GYPCXRXSuzb-eANNe5cSFbQhVtxo1H85Z8UTFuBbbsoz1oEGEwSjj19AbQRjV3FdwUe24_DFoum3PlTCm5TGZxe-SCLZSsugDP-cFEXB7xQIQJ4Y0IKuK5MO5EUweO0uSlgUymVMH0hVJRpxQ0dbCN8jhwB3veM93KTNzswf7HXMHEJ9fAcX-orDdBGa2b4bSHXjmd9L8NIzhxqivrVTVZ7GHyt2VpUNUPvxgBwVSzmfXtj73w8WzcsfqU7OE1_8WOrGuOYEhHVcfKpQ3Hpaqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE1Ts1vD-mwllA933fLHU-Q_Q4hmP4sS7d1GfgWlLo1zxfp8F3oKI0uOP2H1DjUGsorBmx961MXdN8U6OMFhfqvyzNDzkMhTxF71FhFaIL8s9FNCZ4fFsf__bl5krc9tpAursfVt9J67W5tLuwg7NNn7vxDGbFgcyzPk9_7wCdVcpuqL2xmJXm7gSY3Sb0Q1KR9LGa5YN8UgTLDaB-nwXBxNEVoTIBaCKPT6viA2V_CZQbWbZX7Y2POmvOLYcOc9aR0nK3tToLBVLwLpjrGXFhOzI023K1MIs_qrE76JGBjzoG8Au2t0JPDsc5q2rME_9ODK8BEAfs7ZGbmXEF1N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=f8cHht9KR7p6kzA49LG3fdmijRvX3XZ0hEb4gfrbK762LQ1_vGQmA0AJXVTeonCBRj5gufcQftxH0rzCBH8zeZILa0_YrSQIFE8_dUfqT8a5zj4yg63fT3JOJq0oxoez5myGphIt1rAVeX5U9gBoUm5GJweOp7z86RaAP0NnbmF1A7sP5DFEaJ_ndvdmB7wQNfIuuIgLRdW4bIsWz6XhPQFKLq8Jj_lTDkHbfcinLycRzZa5o4CSfEMUHXY73EYK07fZke1IDa6Pv1dKF6r0QsKcv0bHWZeHw4cSyNfa4Yg8rxIp6bRUSf8yAkqiWK-DoRaZ6QHLRma-i_i89J5m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=f8cHht9KR7p6kzA49LG3fdmijRvX3XZ0hEb4gfrbK762LQ1_vGQmA0AJXVTeonCBRj5gufcQftxH0rzCBH8zeZILa0_YrSQIFE8_dUfqT8a5zj4yg63fT3JOJq0oxoez5myGphIt1rAVeX5U9gBoUm5GJweOp7z86RaAP0NnbmF1A7sP5DFEaJ_ndvdmB7wQNfIuuIgLRdW4bIsWz6XhPQFKLq8Jj_lTDkHbfcinLycRzZa5o4CSfEMUHXY73EYK07fZke1IDa6Pv1dKF6r0QsKcv0bHWZeHw4cSyNfa4Yg8rxIp6bRUSf8yAkqiWK-DoRaZ6QHLRma-i_i89J5m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgpBMaSmHxyStAtK-qLESZ_r7g8tanSA3ftZggUP8o0dUFEUQXW4yxhNdO_SnXMeRxkVHr-4aPJvuQx85yoEmw-wylzFU8Fgd0AvIJDPyIvUvezMdy3ryXd083p6hif9BdnhfQ6CFxXE0ZZe3qtkHsw-Wz3tYzt9xj93uyZjWNEOYJloZ_eWnAJpi2vsIx-rgiYop8d7Zws7biPkAE9t7fMj-7bBYmWHmpZI96437desbj0w86EqmsvT5ppJS79ttzqSOkOjkdjaBLRbnkunvIe-HszL93jY986FXFj1piG4FxkJVy0Vjw57OloQGLDVL2luFxapaTaJY8sCEDXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=NznFLut-9ApLXuPmtliggdBdxJpZOMEkkmAff3DgrJppYbmXtxMc2k7G-rICjtCLB4nNeOM0xsErgmDqkXUf0XD6iXXg7yYkbi_oqub9dEDQhxk8tkObnoi5aR7tU18bxh92C4GJypUSccy0-dEbJNVdkFfQY0zrE_p7veDhrEQWvcdIfgy60XrzdTnAgvzYV5EoeRwOVlg6Da8vJGw_NY_Qk1SdKJBVz7Ea3vXQj0gEiD6PMyM0dI3_ovyWT0f379KsM5Rw07QHK3hKX1Xh446l0fyugUsPVoXbTtOwAtAAgiI82lktug5MQYv5B9XK1q_b1qpCIgI-IkEeUI25EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=NznFLut-9ApLXuPmtliggdBdxJpZOMEkkmAff3DgrJppYbmXtxMc2k7G-rICjtCLB4nNeOM0xsErgmDqkXUf0XD6iXXg7yYkbi_oqub9dEDQhxk8tkObnoi5aR7tU18bxh92C4GJypUSccy0-dEbJNVdkFfQY0zrE_p7veDhrEQWvcdIfgy60XrzdTnAgvzYV5EoeRwOVlg6Da8vJGw_NY_Qk1SdKJBVz7Ea3vXQj0gEiD6PMyM0dI3_ovyWT0f379KsM5Rw07QHK3hKX1Xh446l0fyugUsPVoXbTtOwAtAAgiI82lktug5MQYv5B9XK1q_b1qpCIgI-IkEeUI25EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=AoTCsNQfHzRhHEL4ovMLkVUs300NzvFrzLCZh_dXYhtaTXPJ5wo71-jBTD75sQ6nI1O-xinQfREahN1w1L6w5L1vGbA4JSa3k06WpyTEOEkFDtz1DxIBDzsvpNhJv-OOWKW70ImDaGlQrtHmRwIAZA5LdgAJyNVdgSVbHtvEWHSQN4jTpkG3E9DTlAGOkT57pqB7LKiPQbD-I4OOmrywI8y0e-B4rLQH9_DfNKvSRvcPahTGZrtsY2bFHY3r5f4xRj-RZ9p7dpC3rZdcKu5dZK7-BJyuzJHgDDVEgz-QeK-7WJN2DI1_O99d-9zdAYWwpkzEAUcp3vqCf7BZb63_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=AoTCsNQfHzRhHEL4ovMLkVUs300NzvFrzLCZh_dXYhtaTXPJ5wo71-jBTD75sQ6nI1O-xinQfREahN1w1L6w5L1vGbA4JSa3k06WpyTEOEkFDtz1DxIBDzsvpNhJv-OOWKW70ImDaGlQrtHmRwIAZA5LdgAJyNVdgSVbHtvEWHSQN4jTpkG3E9DTlAGOkT57pqB7LKiPQbD-I4OOmrywI8y0e-B4rLQH9_DfNKvSRvcPahTGZrtsY2bFHY3r5f4xRj-RZ9p7dpC3rZdcKu5dZK7-BJyuzJHgDDVEgz-QeK-7WJN2DI1_O99d-9zdAYWwpkzEAUcp3vqCf7BZb63_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=ESroG4OSyQuqxlj_gCb7g4yvlUB2mUYMRrDAVRRE0BETGiAH8xGrdUSKkClID3j8zGfVejbBKCeK4HuLxLMQFzpaKNQJTLVEYuSakLQARhFF9D9y0hBb5_cI9lkFvaRWgjBdOzb7Ah7MHj9hbUInvLG0p4YeRmGaz1v7VJQM1v74klKnblfBCXDcbgNVQHpvt3jvv6UJY6FDxX6z50w6At8bUiAwynuNIPetvIo9J27NKQEwq1b53wzGvpIbrrTjsrSshij7v9pvMWL0TOYeLED5bZgeVWonBr07B5NyNjLeYggPQJGTFgtKGAvcZVd1e8EVtIQJvyw7bQOmttBH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=ESroG4OSyQuqxlj_gCb7g4yvlUB2mUYMRrDAVRRE0BETGiAH8xGrdUSKkClID3j8zGfVejbBKCeK4HuLxLMQFzpaKNQJTLVEYuSakLQARhFF9D9y0hBb5_cI9lkFvaRWgjBdOzb7Ah7MHj9hbUInvLG0p4YeRmGaz1v7VJQM1v74klKnblfBCXDcbgNVQHpvt3jvv6UJY6FDxX6z50w6At8bUiAwynuNIPetvIo9J27NKQEwq1b53wzGvpIbrrTjsrSshij7v9pvMWL0TOYeLED5bZgeVWonBr07B5NyNjLeYggPQJGTFgtKGAvcZVd1e8EVtIQJvyw7bQOmttBH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOvALLPuruygOA7X9Q-5mLuulqWKbkyRtxYW5P7JF_xD0qpzsInhJEARV4rVrGQx7Cxn2rinERLEJ-u6TvxzRW5bRqm0JfQchaYce_U881i0116CzGjXSNkaU6SXN_o_IfSY2EX7kpeM0d83z6lbpEx8wc6HwJDSeuXX_QO8gb3Pd7BgLsLXkA0DZImecfje04fZp_DW8L1Sfla85XSod9elOARETIu36fJyEliepn9Akm4dcZMtU61RH_IJsfS3s3tn46BtwdF7Q5MO1ZSNGxUU2lpXv2NDVKqqGwoLgwItkqFdPPFw3NNIFPdcznFubf4xtzT4HZdaL4anEYdUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=NN6WIf4rEg7y9NarTVVxPReMIE0X1NCdCymCgnAzo1VNTj-uHenp1h0Q6UEwmMO-Ag7fF3XW2jzt3qmTYM0_8M8UA8D4YXmgT3s0cgmrHnzYszGJ7B0dl4YyUU83zddvg91I9cu_Acb4Pi3qk2ZRsxtx5PTl1HS3B9jhbBNvICjBbCuEFAgs2xDPG_yD5QL5OqLJDBoLfj6dAITVLzClk-5cqbnlG2VTNvQ725OyHAHpvP6TVh-4FpI0bI6m6mp7DsMEVuAFJWnwCCoRGpKISbpQ4reX7e8LhUE6pqi2bgQDzzLYdtL_FtZQAIQGb0saZ2X3XwjZf4cLzFsXRK_tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=NN6WIf4rEg7y9NarTVVxPReMIE0X1NCdCymCgnAzo1VNTj-uHenp1h0Q6UEwmMO-Ag7fF3XW2jzt3qmTYM0_8M8UA8D4YXmgT3s0cgmrHnzYszGJ7B0dl4YyUU83zddvg91I9cu_Acb4Pi3qk2ZRsxtx5PTl1HS3B9jhbBNvICjBbCuEFAgs2xDPG_yD5QL5OqLJDBoLfj6dAITVLzClk-5cqbnlG2VTNvQ725OyHAHpvP6TVh-4FpI0bI6m6mp7DsMEVuAFJWnwCCoRGpKISbpQ4reX7e8LhUE6pqi2bgQDzzLYdtL_FtZQAIQGb0saZ2X3XwjZf4cLzFsXRK_tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=UWfHA-ha5X9wZbG1bR-wMQDPZemkuQRf3zP5PI50jEmwP8A_cJLR3J5TOYfQRiyiUtFv-k_8srq6zIE07sD4xLxVB1fO0IaVc46a1qvHeHIO3HRCeL0Vy5Y8Lc0TqlvOPLz5H3dko4KK9AWBRdp0VUjheEbMX_s1pa6lrrwyVtgsiSi769sHUMn2qM_X2Kv-5AeS0-_IBkae4cvWusVtvV2RZCTh4rcvnMT25Ws2_S7_crlBftDDHeJ3p3AcRxYikn823chDlogM0MtmF9zxz461dSX03vMdgIJ1w1Ae99v-F5t8i0AxhUn2RBNiX3790dFKU9DVFrgowU-BPZVUTyH0oAH3NyaqfF4Ein4_lT0V-Tfwc00J61lijp8V4P61OtJzt08cCeWSAqCeOKFITNbAvuIikMWoZuvxEiWVOEsxXDtRdBJnsy_fpWcK2PbjkPYOx8afpxpz2us3qpFA1AZzQZK3MnKuQob1OpBJjxBN6g_N45-8LP_cOy1h42flByt-SYZ8AJ2oGs27ZVvcg0_4Jw9e3u09zIZFomB-AlOdZzDjniSp9wK88bXdiayJbfTp7wgPcr7uJXkCbYkJK3YbDF6MRsFOytOn45J6X_Udbxul-oETh4bsSf0qJEtUCgVdM2tDjy181WqnJqGzIfa_2Jjf0NxtQoeHSUBRdUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=UWfHA-ha5X9wZbG1bR-wMQDPZemkuQRf3zP5PI50jEmwP8A_cJLR3J5TOYfQRiyiUtFv-k_8srq6zIE07sD4xLxVB1fO0IaVc46a1qvHeHIO3HRCeL0Vy5Y8Lc0TqlvOPLz5H3dko4KK9AWBRdp0VUjheEbMX_s1pa6lrrwyVtgsiSi769sHUMn2qM_X2Kv-5AeS0-_IBkae4cvWusVtvV2RZCTh4rcvnMT25Ws2_S7_crlBftDDHeJ3p3AcRxYikn823chDlogM0MtmF9zxz461dSX03vMdgIJ1w1Ae99v-F5t8i0AxhUn2RBNiX3790dFKU9DVFrgowU-BPZVUTyH0oAH3NyaqfF4Ein4_lT0V-Tfwc00J61lijp8V4P61OtJzt08cCeWSAqCeOKFITNbAvuIikMWoZuvxEiWVOEsxXDtRdBJnsy_fpWcK2PbjkPYOx8afpxpz2us3qpFA1AZzQZK3MnKuQob1OpBJjxBN6g_N45-8LP_cOy1h42flByt-SYZ8AJ2oGs27ZVvcg0_4Jw9e3u09zIZFomB-AlOdZzDjniSp9wK88bXdiayJbfTp7wgPcr7uJXkCbYkJK3YbDF6MRsFOytOn45J6X_Udbxul-oETh4bsSf0qJEtUCgVdM2tDjy181WqnJqGzIfa_2Jjf0NxtQoeHSUBRdUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp7lFCXTzQFfFFTR62t0xDpT2zbfkLH-7tayTuJAeLL8WIF4JyuaSv_FeyIFjXWzTcGGoZRKUIdyoz1EdDNxVszL_NpowGzoWcda6E5AdI9WBNisCLYq_wPYRdtazPhZwC8YOO_c7935GDW6BIOfQ3KzLkYhPnMZ_BXfX0SJmKwxvg37uz_zpuYm6jg4mlEo7PD085HDydMiDO1iWwxlzexAazHiZKphjHKYC2o9zqEZbcp4_tnT5lF_DiJe7Y3vKdlOyUhS3xK8TqHNfAMTnY26fUw1MYJ2J2tJ7GO_3Pn1cDLGQDpQHi9Kiqq18JoIqrCbL_X3-RqFFDNYz3rVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diEAf326o_kjFLw2JpQYU0dtMKl8xHQe7WIeStFBHPTHh-S582z4eSkPT-VIxF2B6gxnhN6t27WoQT5CodSmnhzEFo6OhjpheoJIbNZXb4KnmgOKjBPV3ry692EAjabrVLvS3xj6KbpXVtjxdGYQa3fFS-sNUvbUSFJoEngjTcMydMTY3euwWbELhFWa4tb2BK-lnTjSbaDBFo2rp1N_anGeFzFsaPCHRq2i7s8QXU7oNRBsdwb6gdG-kpw9bFHAQrNSf28KuN6nIwX7OELJTPtDv1mk7HLqH8YzkPjq8seq_Gygdq75fYpQUHYaoens4hdeiItUPYxG-W17OoIz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcnT5UyEeoKhkMDXIrn9wp2PKUih6uXrNXwOqzeht6pdPWl_X9Bn6dmsdewj3uXLsbkOxzKcJ3S4Aj7a03Nqhof353Q7wdBwMT8VBhPOs7UvisJP_HDY8GXn4IkPZGoOYF9TqCAAYay01p-YcdEQSi2baHXs9M9C4Pdtf5GJKhBm44v5mVVwAzQRgYPQtyv8w8q-6FiA-NGsomExYNs_GZNTV-BnJ-df7zSUSXlbUun6P3sxHEMiJvy9SmIc5NUDN9w4OeiiY7EGsOK5m5T-SaS8nrq31lND4MDCJ4nqvcqPS39smzn8gctKh9qoa8pDoxqKxrPe0cZFIYPf_kdoaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdIIj5SlVhjrtx5YX6HvqdLmQBTZ4v5myCLDRpSVLkNpCM4o-AbC9ECyV65CanA8RqP0pDn511IbjvgKNi-JVtw7PlD7oE3JPTGNvf5tg-WctOCqJBF-5q3-fByW2AcoaAdurqfH_4cqyxUZ3f_E8WZsnGYLOl8g0N422uRvo7C6sdbHEiAnFiR94NUaqHuDZXoabAUO4eLtN9Wg-CWhtNB_1yBUQBaY2-6dcH7P3AeHj_WC921yMfvg-CQKvFgFW00HtwyjX3khTcGdLQbH2UsnnNYsMAjFJirPxflWTrjNSVMh2WDiZjFHE958PhGpBLy_cgLjXJDpsNhEKiHc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=sqdg_boQXDvGG5JgQW-mSI8Bg-D92X3amQQPVxPlV-vdMM0T68yTDu55LYDd9UthcrMNM1zSdYw_oR9F1MBBr1YupVh1tjINhehPvkZs2bqbaoQ5ZHLkGI18kE4sILTerFpagBZRdysKLX43n9GRX07UDYzkjlDnEyIQNV1AFI7BvYd3jHE960RsCPsAzKJBjw2fmPcRyaDIeQ_uyDGakCnG_U7x3HsMrJrD34QPZ7Pkmqd5732mu8izoeOoyyCczVuPclq5nruwnMINPlWMPqK5eLwAy3scs2qS4aLx-wSAUUrZ-GOB6uqePZV67ZbNpsuyUSebHcMhTBrG_X9mNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=sqdg_boQXDvGG5JgQW-mSI8Bg-D92X3amQQPVxPlV-vdMM0T68yTDu55LYDd9UthcrMNM1zSdYw_oR9F1MBBr1YupVh1tjINhehPvkZs2bqbaoQ5ZHLkGI18kE4sILTerFpagBZRdysKLX43n9GRX07UDYzkjlDnEyIQNV1AFI7BvYd3jHE960RsCPsAzKJBjw2fmPcRyaDIeQ_uyDGakCnG_U7x3HsMrJrD34QPZ7Pkmqd5732mu8izoeOoyyCczVuPclq5nruwnMINPlWMPqK5eLwAy3scs2qS4aLx-wSAUUrZ-GOB6uqePZV67ZbNpsuyUSebHcMhTBrG_X9mNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgWihvBD0KQHF2y8Op1oB0Jc6oRN1KsnaAxqkL5RmM22Ku_w7cBQY3QDsKoTT57u-19GGTFC3CsPsHq7aUyhEA8UrDtNJ_RcOz4GLt_9f8ymmx9fsXWCL6YAvCO0N5p7AgThNQbJYilMQn-aSqAIA8z33bvgZJ2R6zm438idBiWr5vDz37r7PfZwzilQ2493r1t33ur4eSUIm9HENFcx9M9j52vaU6nyfHeXZqghNml29Z26h5tpeXKwSD_VOIBDCsjqJ8QnslXU0FBo6gIniS3r_UBaCkN9HbAyJ15NZ2AinvrnsfoiQu1YbNxXPCNl4llnX0usNW4itGDBp_nSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=rGA1vt1C32B3Jwe8XcTLJxColvI3GirYsDEJqYT8_VJuqHROdBtj-cMxKDC_p5CiyScgYrz45SinxvYAPIIQ8Qj43iVezBGWvVKjz7Aprr7e00aB8RdabEergP2rMn8ag12oX4iuuRnKx98SIKIZzpSeNw_R5UVXzOHbvPyLVx3XWUeCbbZ8ZMUVnBVj7hEYwAnolpS_ETKJXEvRN2tP4Bg5FLvJtadc48Xh2AFOBVLxcJgMILezkc-IS_IQWWn4MEQqS6TZG63ufxf2TzTwpkxSnQpdWoIXApvyVBUJDC_ggVy9W8pkhXGOBJBFnq__DjeedvIHe5uO0dqOS6rfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=rGA1vt1C32B3Jwe8XcTLJxColvI3GirYsDEJqYT8_VJuqHROdBtj-cMxKDC_p5CiyScgYrz45SinxvYAPIIQ8Qj43iVezBGWvVKjz7Aprr7e00aB8RdabEergP2rMn8ag12oX4iuuRnKx98SIKIZzpSeNw_R5UVXzOHbvPyLVx3XWUeCbbZ8ZMUVnBVj7hEYwAnolpS_ETKJXEvRN2tP4Bg5FLvJtadc48Xh2AFOBVLxcJgMILezkc-IS_IQWWn4MEQqS6TZG63ufxf2TzTwpkxSnQpdWoIXApvyVBUJDC_ggVy9W8pkhXGOBJBFnq__DjeedvIHe5uO0dqOS6rfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZm9aigvGfjj1uU9hc-y7iARp4h9Xxjap9QpLsG8YysPRhL04jMZYZzPsJU_OKtP74xSFDHObBCL0GdyLDv6uwWHFMPzrgU6Bpf-2cIvA16wHEvY39lc5JpdRtx2Nk47tvOyiu54kRbAcrstW7d0kbdgS5v7p9zLaG0kjbj-8q7jW4gJv78tCJn2dVvz6Nyp7ihKeG0BtMiwHVLQcFENyGULDjGyhNoycoV7bFkqni1iIP3E-DIN1PwtbHNx8_85C0VSW-7wAMG08uLEM5iLb4VUPPWMoe4fdp5S-utdTWlRS1nYDRZ8zufWWVTwQBVWd54567msRKHDTzvWUE1CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnWSrwKhxUXq1v1H7C8D1ox3-5ZMsWClGTaYuG8FFec18GG2LLPCEETOEPljdfL6yKiG1YbRCn3j4iNMa7DrdlAtSP36eXjSpSRCHABB4rKWtacS3IqV3Hpi5vXrBWsfQGHqb9i77liU5JObHhpKnzd3ozOMxdRRovy_gTLOXt6-aiihDkCBpfPMUatfjyb4zsrcQVSig5fnnReVH4hjWXZJAh7xZPGLDt0NbJjLgR9rErSGxiqbH5rccJg0WkeWahjtwXEeJMic7QaiZHSJk7DShvCnYoTO9fUGCId0xX8BpwpJ556Nrrh09UFZsJjJK0005VRym4oKXYTXKUG5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSVHqJEY9a8LEG7Eh2yj3Puhav7zxy5l6z01hn-3SEUDg-LtIISIjXY9YhfNuZTwHb2qNF66ieRALD-ucIpx8KlIRnYGT6GjUyLUioQGr_3gMP8IeIq1iAx6wGJWA4471baioaZoDWqccbY-E4oDOllJ1HNOZ8eD24HCQJXJrnnOFuoiYhcPNcLS2IujjghUZ6WI2hM668g-a4-8XizVAprZel_laX3XWCilJ7tWrAeBlnJQ-8F7IGkZuMSSjMV_mazHHfLOtS8mGE7Cophq_5V9Yj_OpRKHRwrgMpXBXSy3SdEs3VF7Y0ctm4QLrxDvhktilWueE3lWA3O_PvE2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=CzrnFal7QeCgvIDvQoQz2iWN_1P6FofS5WxLhxH8hBG3bbYsMATQ7C-am7f5TFmYrRBsbnB87O3PIv8CzJDIuVNvTHHfIXJm42aCoyd-MP4v_vUWPhK6w4TwT51dUmu3hrKQ7QLMPbnh1CyPfx_D_rgiHmvHhLqdzkHGloQgdf8nzN86hhNsBJIapfmS_Ine-WRILtkkD3O4afU7qi3iKUnET4Zu50rmAXmZgJL8GA2jZPWaU6BuGTjjOMoLgn4yhNLipndWGPoRNoXa3IREztBcxJAW1eHIvHolIBVqFJeGw7cwzlewuxGZgqDQWhxj1T3kwIaMNo8c6Sdc7hNVEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=CzrnFal7QeCgvIDvQoQz2iWN_1P6FofS5WxLhxH8hBG3bbYsMATQ7C-am7f5TFmYrRBsbnB87O3PIv8CzJDIuVNvTHHfIXJm42aCoyd-MP4v_vUWPhK6w4TwT51dUmu3hrKQ7QLMPbnh1CyPfx_D_rgiHmvHhLqdzkHGloQgdf8nzN86hhNsBJIapfmS_Ine-WRILtkkD3O4afU7qi3iKUnET4Zu50rmAXmZgJL8GA2jZPWaU6BuGTjjOMoLgn4yhNLipndWGPoRNoXa3IREztBcxJAW1eHIvHolIBVqFJeGw7cwzlewuxGZgqDQWhxj1T3kwIaMNo8c6Sdc7hNVEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3MHNMPTu0sLZQQZu1nIx8jeY5WKa_1fU-V5l6n5e89XlTyuRvJ1RL2tIhkjmkAHPnWw56rsgz8JXVKlEsdMoOF6CYjKgf7FxrkyykiTKZv9mcDztgx2GkLuSHV9uexZzZvO7Mpe4sWk7PooMHUih5AotAEkgTVpnAXcpA47nSu5FUe8nE9AwO0_WeRVu1vvva-yzGxwYtTxvTswyiXaY6du7Xh7KAV4ce_xvbWAbCp3vptswdNEhq86Np5040OPt7WYa1DcjYinQb3_i7MQmuYt3EpM1wIImpthDAXqPRMRZjwy4Pe-Zz1ksfXhgSDdEv0dUVPv2MCg-rvnLC6bYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMsxZsRfTVPZZ_agtmarLJL3bJsUkKoxQjccL7EaXaZu1ra2eESDucRvLqjNMey_XL0gd6ZT89PMCdhLhhnDxi6QBjAGAq423xpOS2euAi51KkWD4eNXiEMK7aUMm-3NJ8uPacMiRFg-iSVDjsN5K-AgVM9LTBXwQI7Fa_Pyd946szQBpp3E0_pBX-LIY3wBMiTOJjUlPtEiZVnxmx8Xe1z-MCOHu9b7NvOTYqIprCKe0sEozHDBaBERASubgSx6opZqIT7Ds7aUg8EwrHvfKQ0UeK7pUgXaGoUJdukwv4TVCOysj19werjm2faLYFcGJtDjqzbuBCFec1tksqp5AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
